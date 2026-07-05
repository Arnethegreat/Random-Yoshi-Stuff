#!/usr/bin/env python3
"""Dump world-map level entrance and midway entrance reads from a ROM.

Reads the level_entrance_indexes / level_midway_entrance_indexes pointer
tables from a Yoshi's Island ROM, resolves each pointer into the matching
map_level_entrances / map_level_midway_entrances record, and reports the
resolved data including out-of-bounds indexes.

Bank-wrapping is handled automatically: if a pointer added to the base
entrance table address overflows the current SNES bank, the address is
allowed to carry into the next bank and romutils.snes_to_pc converts it
to a PC file offset correctly.

Usage examples
--------------
# level entrances (default mode)
python dump_entrance_reads.py rom.sfc

# midway entrances, markdown output
python dump_entrance_reads.py rom.sfc --mode midway --format markdown

# override table addresses (e.g. for a different region)
python dump_entrance_reads.py rom.sfc --index-table $17F3E7 --entrance-table $17F471
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# romutils inline (so this script is usable standalone or from the scripts/ dir)
# ---------------------------------------------------------------------------
try:
    from romutils import open_rom, snes_to_pc  # type: ignore[import]
except ImportError:
    import struct as _struct

    def snes_to_pc(addr: int) -> int:  # type: ignore[misc]
        bank = (addr & 0xFF0000) >> 16
        absolute = addr & 0x00FFFF
        abs_corrected = absolute - 0x8000 * (1 - bank % 2)
        return (bank << 15) | abs_corrected

    def open_rom(file: str) -> bytes:  # type: ignore[misc]
        with open(file, "rb") as f:
            data = f.read()
        if len(data) > 0x200000:
            return data[0x200:]
        return data


# ---------------------------------------------------------------------------
# Default SNES addresses (from bank17.asm / U10 ROM)
# ---------------------------------------------------------------------------
# level entrance tables
DEFAULT_LEVEL_INDEX_TABLE    = 0x17F3E7  # level_entrance_indexes
DEFAULT_LEVEL_ENTRANCE_TABLE = 0x17F471  # map_level_entrances
DEFAULT_LEVEL_INDEX_COUNT    = 69        # number of defined pointer entries

# midway entrance tables
DEFAULT_MIDWAY_INDEX_TABLE    = 0x17F551  # level_midway_entrance_indexes
DEFAULT_MIDWAY_ENTRANCE_TABLE = 0x17F5DB  # map_level_midway_entrances
DEFAULT_MIDWAY_INDEX_COUNT    = 69        # number of defined pointer entries

# Maximum item_page value used by the midway formula
MAX_ITEM_PAGE = 3

POINTER_SIZE = 2   # all pointers are 16-bit (bank-relative)
ENTRY_SIZE   = 4   # all records are 4 bytes

# ---------------------------------------------------------------------------
# Auto-detection signatures
#
# Each signature is a sequence of bytes taken from the START of the index
# table (first 12 pointer entries = one full world, 24 bytes).  These values
# are invariant across all known Yoshi's Island regions because they reflect
# the fixed world-map tile layout, not ROM addresses.
#
# level_entrance_indexes opening entries (indices 0–11, u16 LE):
#   $0000 $0004 $0008 $000C $0010 $0014 $0018 $001C $0020 $0000 $00D8 $00DC
#
# level_midway_entrance_indexes opening entries (indices 0–11, u16 LE):
#   $0000 $0004 $000C $0014 $001C $0020 $0024 $0028 $0000 $0000 $0000 $0000
# ---------------------------------------------------------------------------
_LEVEL_SIG  = bytes.fromhex(
    "0000 0400 0800 0C00 1000 1400 1800 1C00 2000 0000 D800 DC00".replace(" ", "")
)
_MIDWAY_SIG = bytes.fromhex(
    "0000 0400 0C00 1400 1C00 2000 2400 2800 0000 0000 0000 0000".replace(" ", "")
)


# ---------------------------------------------------------------------------
# Auto-detection
# ---------------------------------------------------------------------------

def _pc_to_snes_hirom(pc_offset: int) -> int:
    """Convert a HiROM PC file offset back to a SNES address."""
    bank   = pc_offset >> 15
    offset = (pc_offset & 0x7FFF) | 0x8000
    return (bank << 16) | offset


def detect_tables(rom: bytes) -> tuple[int | None, int | None, int | None, int | None]:
    """
    Scan the ROM for the level entrance and midway entrance index tables.

    Returns (level_index_snes, level_entrance_snes,
             midway_index_snes, midway_entrance_snes).
    Any value is None if the corresponding signature was not found.

    The entrance table SNES address is derived as:
        entrance_table = index_table_snes + DEFAULT_LEVEL_INDEX_COUNT * POINTER_SIZE
    This holds because both tables are laid out contiguously in all known
    Yoshi's Island versions (gap = 69 × 2 = 138 = $8A bytes).
    """
    level_index_snes = level_entrance_snes = None
    midway_index_snes = midway_entrance_snes = None

    pos = rom.find(_LEVEL_SIG)
    if pos != -1:
        level_index_snes   = _pc_to_snes_hirom(pos)
        level_entrance_snes = level_index_snes + DEFAULT_LEVEL_INDEX_COUNT * POINTER_SIZE

    pos = rom.find(_MIDWAY_SIG)
    if pos != -1:
        midway_index_snes   = _pc_to_snes_hirom(pos)
        midway_entrance_snes = midway_index_snes + DEFAULT_MIDWAY_INDEX_COUNT * POINTER_SIZE

    return level_index_snes, level_entrance_snes, midway_index_snes, midway_entrance_snes


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def parse_int(value: str) -> int:
    value = value.strip()
    if value.startswith("$"):
        return int(value[1:], 16)
    return int(value, 0)


def fmt(value: int, width: int) -> str:
    return f"${value:0{width}X}"


def snes_bank(addr: int) -> int:
    return (addr >> 16) & 0xFF


def read_u16_le(rom: bytes, pc_offset: int) -> int | None:
    """Return a little-endian u16 from the ROM at *pc_offset*, or None if OOB."""
    if pc_offset < 0 or pc_offset + 1 >= len(rom):
        return None
    return rom[pc_offset] | (rom[pc_offset + 1] << 8)


def read_4(rom: bytes, pc_offset: int) -> bytes | None:
    """Return 4 bytes from the ROM at *pc_offset*, or None if OOB."""
    if pc_offset < 0 or pc_offset + 3 >= len(rom):
        return None
    return bytes(rom[pc_offset : pc_offset + 4])


def resolve_snes_address(snes_addr: int) -> tuple[int, str | None]:
    """
    Resolve special SNES address regions to their canonical address.

    Returns (canonical_snes_addr, note_or_None).
    """
    bank_offset = snes_addr & 0xFFFF

    # Low RAM mirror ($xx0000–$xx1FFF)
    if bank_offset <= 0x1FFF:
        return 0x7E0000 | bank_offset, "RAM mirror"

    # SRAM mirror ($xx6000–$xx7FFF)
    if 0x6000 <= bank_offset <= 0x7FFF:
        return 0x700000 | (bank_offset - 0x6000), "SRAM mirror"

    # I/O / open bus ($xx2000–$xx5FFF)
    if bank_offset < 0x8000:
        return snes_addr, "Open Bus / Registers"

    return snes_addr, None


def compute_entrance_snes_addr(entrance_table: int, pointer: int) -> int:
    """
    Add *pointer* (bank-relative u16) to *entrance_table* (full SNES address).

    The pointer is a byte offset from the entrance table base.  If the sum
    overflows the current bank's address space (i.e. crosses $xxFFFF), the
    result naturally carries into the next bank — this is intentional for
    out-of-bounds reads that wrap into bank $18 etc.
    """
    return entrance_table + pointer


# ---------------------------------------------------------------------------
# Row builders
# ---------------------------------------------------------------------------

def build_level_row(
    rom: bytes,
    index: int,
    index_table: int,
    entrance_table: int,
    known_index_count: int | None,
) -> dict[str, str]:
    """Build one output row for the level entrance table."""
    pointer_snes = index_table + index * POINTER_SIZE
    pointer_pc   = snes_to_pc(pointer_snes)
    pointer      = read_u16_le(rom, pointer_pc)

    notes: list[str] = []
    if known_index_count is not None and index >= known_index_count:
        notes.append("index table OOB")

    row: dict[str, str] = {
        "index":      fmt(index, 2),
        "index_addr": fmt(pointer_snes, 6),
        "ptr":        "OOB",
        "entry_addr": "OOB",
        "level":      "?",
        "x":          "?",
        "y":          "?",
        "unlock":     "?",
        "notes":      "",
    }

    if pointer is None:
        notes.append("pointer read outside ROM")
        row["notes"] = ", ".join(notes)
        return row

    row["ptr"] = fmt(pointer, 4)

    raw_entry_snes                  = compute_entrance_snes_addr(entrance_table, pointer)
    resolved_entry_snes, addr_note  = resolve_snes_address(raw_entry_snes)
    entry_pc                        = snes_to_pc(resolved_entry_snes)
    entry                           = read_4(rom, entry_pc)

    row["entry_addr"] = fmt(resolved_entry_snes, 6)

    if addr_note:
        notes.append(addr_note)
        if resolved_entry_snes != raw_entry_snes:
            notes.append(f"computed {fmt(raw_entry_snes, 6)}")

    if entry is None:
        notes.append("entrance read outside ROM")
    else:
        level, x, y, unlock = entry
        row["level"]  = fmt(level, 2)
        row["x"]      = fmt(x, 2)
        row["y"]      = fmt(y, 2)
        row["unlock"] = fmt(unlock, 2)
        if entry == b"\x00\x00\x00\x00":
            notes.append("blank entry")

    row["notes"] = ", ".join(notes)
    return row


def build_midway_row(
    rom: bytes,
    index: int,
    index_table: int,
    entrance_table: int,
    known_index_count: int | None,
) -> dict[str, str]:
    """
    Build one output row for the midway entrance table.

    The midway pointer formula (from bank01.asm) is:
        offset = base_ptr_for_level + (item_page * 4)
    where base_ptr_for_level is the u16 stored at index_table + index*2.

    Each of the four item_page values (0–3) is a separate entrance record,
    so we emit all four as sub-columns in a single row.
    """
    pointer_snes = index_table + index * POINTER_SIZE
    pointer_pc   = snes_to_pc(pointer_snes)
    base_ptr     = read_u16_le(rom, pointer_pc)

    notes: list[str] = []
    if known_index_count is not None and index >= known_index_count:
        notes.append("index table OOB")

    # Base row skeleton — item_page sub-columns filled in below
    row: dict[str, str] = {
        "index":      fmt(index, 2),
        "index_addr": fmt(pointer_snes, 6),
        "base_ptr":   "OOB",
        "notes":      "",
    }
    for p in range(MAX_ITEM_PAGE + 1):
        row[f"entry_addr_{p}"] = "OOB"
        row[f"level_{p}"]      = "?"
        row[f"x_{p}"]          = "?"
        row[f"y_{p}"]          = "?"
        row[f"type_{p}"]       = "?"

    if base_ptr is None:
        notes.append("pointer read outside ROM")
        row["notes"] = ", ".join(notes)
        return row

    row["base_ptr"] = fmt(base_ptr, 4)

    for item_page in range(MAX_ITEM_PAGE + 1):
        # Formula: ptr = base_ptr + item_page * 4
        # (matches bank01.asm: ASL A / ASL A on item_page then ADC base_ptr)
        effective_ptr = base_ptr + item_page * ENTRY_SIZE

        raw_entry_snes                  = compute_entrance_snes_addr(entrance_table, effective_ptr)
        resolved_entry_snes, addr_note  = resolve_snes_address(raw_entry_snes)
        entry_pc                        = snes_to_pc(resolved_entry_snes)
        entry                           = read_4(rom, entry_pc)

        row[f"entry_addr_{item_page}"] = fmt(resolved_entry_snes, 6)

        page_notes: list[str] = []
        if addr_note:
            page_notes.append(addr_note)
            if resolved_entry_snes != raw_entry_snes:
                page_notes.append(f"computed {fmt(raw_entry_snes, 6)}")

        if entry is None:
            page_notes.append("entrance read outside ROM")
            row[f"level_{item_page}"] = "?"
            row[f"x_{item_page}"]     = "?"
            row[f"y_{item_page}"]     = "?"
            row[f"type_{item_page}"]  = "?"
        else:
            level, x, y, entry_type = entry
            row[f"level_{item_page}"] = fmt(level, 2)
            row[f"x_{item_page}"]     = fmt(x, 2)
            row[f"y_{item_page}"]     = fmt(y, 2)
            row[f"type_{item_page}"]  = fmt(entry_type, 2)
            if entry == b"\x00\x00\x00\x00":
                page_notes.append(f"page{item_page}: blank entry")

        if page_notes:
            # Prefix with page number so multiple pages' notes don't collide
            notes.extend(f"[p{item_page}] {n}" for n in page_notes)

    row["notes"] = ", ".join(notes)
    return row


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------

def _md_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def render_level_markdown(rows: list[dict[str, str]]) -> str:
    headers = ["Index", "Index read", "Ptr", "Entrance read",
               "Level", "X", "Y", "Unlock icon", "Notes"]
    keys    = ["index", "index_addr", "ptr", "entry_addr",
               "level", "x", "y", "unlock", "notes"]
    lines   = [_md_row(headers), _md_row(["---"] * len(headers))]
    for row in rows:
        lines.append(_md_row([row[k] for k in keys]))
    return "\n".join(lines)


def render_level_asm(rows: list[dict[str, str]]) -> str:
    header = "; index | index read |    ptr | entrance read | level   x   y  unlock | notes"
    lines  = [header]
    for row in rows:
        lines.append(
            f"; {row['index']:>5} | {row['index_addr']} | {row['ptr']:>6} | "
            f"{row['entry_addr']:>13} | {row['level']:>5} "
            f"{row['x']:>4} {row['y']:>4} {row['unlock']:>7} | {row['notes']}"
        )
    return "\n".join(lines)


def render_midway_markdown(rows: list[dict[str, str]]) -> str:
    # Header: fixed columns then item_page 0..3 groups
    fixed_headers = ["Index", "Index read", "Base ptr"]
    page_headers  = []
    for p in range(MAX_ITEM_PAGE + 1):
        page_headers += [
            f"Addr (p{p})", f"Level (p{p})", f"X (p{p})", f"Y (p{p})", f"Type (p{p})"
        ]
    headers = fixed_headers + page_headers + ["Notes"]
    lines   = [_md_row(headers), _md_row(["---"] * len(headers))]

    for row in rows:
        cells  = [row["index"], row["index_addr"], row["base_ptr"]]
        for p in range(MAX_ITEM_PAGE + 1):
            cells += [
                row[f"entry_addr_{p}"],
                row[f"level_{p}"],
                row[f"x_{p}"],
                row[f"y_{p}"],
                row[f"type_{p}"],
            ]
        cells.append(row["notes"])
        lines.append(_md_row(cells))
    return "\n".join(lines)


def render_midway_asm(rows: list[dict[str, str]]) -> str:
    # Compact: one line per index showing all 4 pages inline
    page_hdr = "  ".join(f"p{p}:addr    lv   x   y  tp" for p in range(MAX_ITEM_PAGE + 1))
    header   = f"; idx | index read | base_ptr | {page_hdr} | notes"
    lines    = [header]
    for row in rows:
        page_parts = "  ".join(
            f"{row[f'entry_addr_{p}']:>8} {row[f'level_{p}']:>4} "
            f"{row[f'x_{p}']:>4} {row[f'y_{p}']:>4} {row[f'type_{p}']:>4}"
            for p in range(MAX_ITEM_PAGE + 1)
        )
        lines.append(
            f"; {row['index']:>4} | {row['index_addr']} | {row['base_ptr']:>8} | "
            f"{page_parts} | {row['notes']}"
        )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def make_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Dump Yoshi's Island level / midway entrance tables from a ROM, "
            "including out-of-bounds reads that wrap into adjacent banks."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    parser.add_argument("rom", help="path to the Yoshi's Island ROM (headered or unheadered)")

    parser.add_argument(
        "--mode",
        choices=("level", "midway"),
        default="level",
        help="which table to dump (default: level)",
    )

    # Table addresses — defaults set per-mode in main()
    parser.add_argument(
        "--index-table",
        type=parse_int,
        default=None,
        help=(
            "SNES address of the index pointer table "
            f"(level default: ${DEFAULT_LEVEL_INDEX_TABLE:06X}, "
            f"midway default: ${DEFAULT_MIDWAY_INDEX_TABLE:06X})"
        ),
    )
    parser.add_argument(
        "--entrance-table",
        type=parse_int,
        default=None,
        help=(
            "SNES address of the entrance data table "
            f"(level default: ${DEFAULT_LEVEL_ENTRANCE_TABLE:06X}, "
            f"midway default: ${DEFAULT_MIDWAY_ENTRANCE_TABLE:06X})"
        ),
    )

    parser.add_argument("--first-index", type=parse_int, default=0x00,
                        help="first index to dump (default: $00)")
    parser.add_argument("--last-index",  type=parse_int, default=0xFF,
                        help="last index to dump (default: $FF)")

    parser.add_argument(
        "--known-index-count",
        type=parse_int,
        default=None,
        help=(
            "mark indexes at or above this value as out-of-bounds "
            f"(level default: {DEFAULT_LEVEL_INDEX_COUNT}, "
            f"midway default: {DEFAULT_MIDWAY_INDEX_COUNT}); "
            "use -1 to disable"
        ),
    )

    parser.add_argument(
        "--format",
        choices=("markdown", "asm"),
        default="markdown",
        help="output format (default: markdown)",
    )
    parser.add_argument("--output", help="write output to this path instead of stdout")

    return parser


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = make_arg_parser()
    args   = parser.parse_args()

    if args.last_index < args.first_index:
        raise SystemExit("--last-index must be >= --first-index")

    rom = open_rom(args.rom)

    # --- Auto-detect table addresses from the ROM -------------------------
    level_idx_auto, level_ent_auto, midway_idx_auto, midway_ent_auto = detect_tables(rom)

    if args.mode == "level":
        if args.index_table is None:
            if level_idx_auto is not None:
                args.index_table = level_idx_auto
                print(
                    f"[auto] level_entrance_indexes   detected at "
                    f"${level_idx_auto:06X}",
                    file=sys.stderr,
                )
            else:
                args.index_table = DEFAULT_LEVEL_INDEX_TABLE
                print(
                    f"[warn] level signature not found; "
                    f"falling back to default ${DEFAULT_LEVEL_INDEX_TABLE:06X}",
                    file=sys.stderr,
                )
        if args.entrance_table is None:
            if level_ent_auto is not None and level_idx_auto is not None:
                args.entrance_table = level_ent_auto
                print(
                    f"[auto] map_level_entrances       detected at "
                    f"${level_ent_auto:06X}",
                    file=sys.stderr,
                )
            else:
                args.entrance_table = DEFAULT_LEVEL_ENTRANCE_TABLE
        if args.known_index_count is None:
            args.known_index_count = DEFAULT_LEVEL_INDEX_COUNT
    else:  # midway
        if args.index_table is None:
            if midway_idx_auto is not None:
                args.index_table = midway_idx_auto
                print(
                    f"[auto] level_midway_entrance_indexes detected at "
                    f"${midway_idx_auto:06X}",
                    file=sys.stderr,
                )
            else:
                args.index_table = DEFAULT_MIDWAY_INDEX_TABLE
                print(
                    f"[warn] midway signature not found; "
                    f"falling back to default ${DEFAULT_MIDWAY_INDEX_TABLE:06X}",
                    file=sys.stderr,
                )
        if args.entrance_table is None:
            if midway_ent_auto is not None and midway_idx_auto is not None:
                args.entrance_table = midway_ent_auto
                print(
                    f"[auto] map_level_midway_entrances    detected at "
                    f"${midway_ent_auto:06X}",
                    file=sys.stderr,
                )
            else:
                args.entrance_table = DEFAULT_MIDWAY_ENTRANCE_TABLE
        if args.known_index_count is None:
            args.known_index_count = DEFAULT_MIDWAY_INDEX_COUNT

    if args.known_index_count == -1:
        args.known_index_count = None

    rows: list[dict[str, str]] = []
    for index in range(args.first_index, args.last_index + 1):
        if args.mode == "level":
            rows.append(
                build_level_row(
                    rom, index,
                    args.index_table, args.entrance_table,
                    args.known_index_count,
                )
            )
        else:
            rows.append(
                build_midway_row(
                    rom, index,
                    args.index_table, args.entrance_table,
                    args.known_index_count,
                )
            )

    if args.mode == "level":
        text = render_level_asm(rows) if args.format == "asm" else render_level_markdown(rows)
    else:
        text = render_midway_asm(rows) if args.format == "asm" else render_midway_markdown(rows)

    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    else:
        sys.stdout.write(text + "\n")


if __name__ == "__main__":
    main()
