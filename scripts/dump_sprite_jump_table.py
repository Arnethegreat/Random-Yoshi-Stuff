#!/usr/bin/env python3
"""Dump the sprite handler JSR jump table for Yoshi's Island.

The game executes:
    SBC #$0022        ; sprite_id -= 0x22  (16-bit, carry set before)
    ASL A             ; *= 2
    TAX               ; X = result (full 16-bit, no masking)
    JSR ($A9B7, x)    ; read pointer from bank-02:(A9B7 + X), call it

The pointer table lives at $02A9B7 (U10/J10/U11/J11) or $02A9C2 (E10/E11)
and holds 128 entries (256 bytes), covering sprite IDs $0022-$00A1 (X=$0000-$00FE).

Sprite IDs outside that range produce X values that read OUTSIDE the intended block:

  $0000-$0021  ->  X = $FF9C-$FFFE  (reads backwards into pre-table code)
  $00A2-$01B0  ->  X = $0100-$06FC  (reads forward into handler code after the table)

All three zones are documented here for glitch research. A "Safe" column marks whether
the pointer came from within the intended 128-entry table. ROM targets are checked for
a direct RTS opcode ($60) at the target address as a quick sanity indicator.

Usage
-----
  python dump_sprite_jump_table.py rom.sfc
  python dump_sprite_jump_table.py rom.sfc --format asm
  python dump_sprite_jump_table.py rom.sfc --format named   # includes sprite names
  python dump_sprite_jump_table.py rom.sfc --table $02A9C2  # force E-version address
  python dump_sprite_jump_table.py rom.sfc --first $0000 --last $01B0
  python dump_sprite_jump_table.py rom.sfc --output table.md
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# romutils inline (works standalone or inside scripts/)
# ---------------------------------------------------------------------------
try:
    from romutils import open_rom, snes_to_pc  # type: ignore[import]
except ImportError:
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
# Constants
# ---------------------------------------------------------------------------

# U10 / J10 / U11 / J11 table DP address
DEFAULT_TABLE_SNES_U = 0x02A9B7
# E10 / E11 table DP address (JSR operand is 0x0B higher)
DEFAULT_TABLE_SNES_E = 0x02A9C2

SPRITE_BANK   = 0x02         # table and all targets live in bank $02

# Index registers are 8-bit at the JSR site (P flag 'X' set).
# TAX therefore stores only the low byte of A, so the effective X is:
#     x = ((sprite_id - $0022) * 2) & $FF
#
# The table block occupies 256 bytes ($02A9B7-$02AAB6), giving 128 entries
# (X = $00, $02, ..., $FE).  Because X wraps at 8 bits, every sprite maps
# into this same 128-entry block; sprites repeat with a period of 128 IDs.
#
# The 10 ASM-labelled entries ($02A9B7-$02A9C9) are the ONLY intentional
# pointer values.  All other table slots are arbitrary handler code bytes
# read as pointers.
TABLE_ENTRIES    = 128       # full table block size (128 x 2-byte entries)
X_MASK           = 0xFF      # TAX truncates A to 8-bit X
SPR_PERIOD       = 0x80      # sprites repeat every 128 IDs
SPR_BASE         = 0x0022    # sprite ID whose (A*2)&FF == 0x00 (entry 0)
SPR_FIRST_DEFAULT = 0x0000
SPR_LAST_DEFAULT  = 0x01B0

# RTS opcode -- used for the direct-RTS check
RTS_OPCODE = 0x60

# X offsets of the 10 intentional entries: $00, $02, ..., $12 (same for all regions)
VALID_X_OFFSETS: frozenset[int] = frozenset(range(0x00, 0x14, 2))

# Detection signatures (first 10 bytes = 5 pointers of each region's table)
# U/J: dw $A9CB $A981 $A981 $A981 $AA36
_TABLE_SIG_U = bytes([0xCB, 0xA9, 0x81, 0xA9, 0x81, 0xA9, 0x81, 0xA9, 0x36, 0xAA])
# E:   dw $A9D6 $A98C $A98C $A98C $AA41
_TABLE_SIG_E = bytes([0xD6, 0xA9, 0x8C, 0xA9, 0x8C, 0xA9, 0x8C, 0xA9, 0x41, 0xAA])
_TABLE_SIG_E_DELTA = DEFAULT_TABLE_SNES_E - DEFAULT_TABLE_SNES_U  # +0x0B

# ---------------------------------------------------------------------------
# Sprite name table
# ---------------------------------------------------------------------------

def load_sprite_names(md_path: str) -> dict[int, str]:
    """
    Parse scripts/sprite_ids.md and return {sprite_id_int: name_str}.
    Expected row format:  |  HHH |  Description |  ... |
    """
    names: dict[int, str] = {}
    try:
        with open(md_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line.startswith("|"):
                    continue
                parts = [p.strip() for p in line.split("|")]
                # parts[0] is empty, parts[1] is ID, parts[2] is description
                if len(parts) < 3:
                    continue
                id_str = parts[1].strip()
                desc   = parts[2].strip()
                if not id_str or not desc or id_str.lower() in ("id", "----", "---"):
                    continue
                try:
                    names[int(id_str, 16)] = desc
                except ValueError:
                    pass
    except FileNotFoundError:
        pass
    return names


# ---------------------------------------------------------------------------
# SNES address classification (same logic as dump_entrance_reads.py)
# ---------------------------------------------------------------------------

def classify_ptr(ptr_val: int) -> tuple[str, str | None]:
    """
    Classify a 16-bit pointer (bank-relative within bank $02).

    Returns (kind, note):
        kind  -- one of 'ROM', 'RAM-mirror', 'SRAM-mirror', 'RAM/IO'
        note  -- human-readable annotation, or None for plain ROM
    """
    if ptr_val >= 0x8000:
        return "ROM", None
    if ptr_val <= 0x1FFF:
        # Low addresses in bank $02 mirror WRAM ($7E0000+offset)
        return "RAM-mirror", f"-> $7E{ptr_val:04X}"
    if 0x6000 <= ptr_val <= 0x7FFF:
        # $6000-$7FFF in even banks mirror SRAM / cart RAM
        return "SRAM-mirror", f"-> SRAM ${ptr_val - 0x6000:04X}"
    # $2000-$5FFF: I/O registers / open bus
    return "RAM/IO", f"-> I/O ${ptr_val:04X}"


def zone_label(spr: int) -> str:
    """
    Classify the read zone for a sprite ID.

    With 8-bit X, every sprite maps into the 128-entry table block.
    'intentional' = one of the 10 ASM-labelled entries ($0022-$002B and
                    their 128-ID repeats).
    'table'       = reads from the table block but not an intentional entry.
    """
    x = x_for_sprite(spr)
    if x in VALID_X_OFFSETS:
        return "intentional"
    return "table"


# ---------------------------------------------------------------------------
# Core formula
# ---------------------------------------------------------------------------

def x_for_sprite(spr: int) -> int:
    """
    Return the 8-bit X value the CPU loads for a given sprite ID.

    The accumulator arithmetic is 16-bit (REP #$20 / 'm' flag clear) but
    the index registers are 8-bit ('X' flag set, confirmed by P:nvmXdizc in
    tracelog).  TAX therefore stores only the low byte of A into X:
        A = (sprite_id - $0022) & $FFFF   ; 16-bit SBC
        A = A * 2                          ; 16-bit ASL
        X = A & $FF                        ; TAX truncates to 8-bit X
    """
    a = (spr - SPR_BASE) & 0xFFFF   # 16-bit SBC result
    return (a * 2) & X_MASK          # ASL then TAX (8-bit)


def read_u16_le(rom: bytes, pc: int) -> int | None:
    if pc < 0 or pc + 1 >= len(rom):
        return None
    return rom[pc] | (rom[pc + 1] << 8)


def is_direct_rts(rom: bytes, ptr_val: int) -> bool:
    """Return True if the first byte at the ROM target address is RTS ($60)."""
    if ptr_val < 0x8000:
        return False
    target_snes = (SPRITE_BANK << 16) | ptr_val
    target_pc   = snes_to_pc(target_snes)
    if target_pc < 0 or target_pc >= len(rom):
        return False
    return rom[target_pc] == RTS_OPCODE


def read_valid_targets(rom: bytes, table_dp: int) -> frozenset[int]:
    """
    Read the 10 intentional pointer values directly from the ROM table.
    This works for all regions without hardcoding version-specific values.
    """
    targets = set()
    for x in VALID_X_OFFSETS:
        ptr_snes = (SPRITE_BANK << 16) | ((table_dp + x) & 0xFFFF)
        ptr_pc   = snes_to_pc(ptr_snes)
        val      = read_u16_le(rom, ptr_pc)
        if val is not None:
            targets.add(val)
    return frozenset(targets)


def build_row(rom: bytes, spr: int, table_dp: int, valid_targets: frozenset[int]) -> dict:
    x         = x_for_sprite(spr)
    ptr_snes  = (SPRITE_BANK << 16) | ((table_dp + x) & 0xFFFF)
    ptr_pc    = snes_to_pc(ptr_snes)
    ptr_val   = read_u16_le(rom, ptr_pc)
    zone      = zone_label(spr)

    # "safe" meaning:
    #   "valid table"  -- X offset is one of the 10 intentional entries AND
    #                     the value is one of the 5 known valid targets
    #   "direct RTS"   -- first byte at target is $60 (regardless of source)
    #   ""             -- neither condition met
    # Both can be true simultaneously ($A981 is intentional AND first byte=$60).
    row = {
        "spr":      f"${spr:04X}",
        "x_reg":    f"${x:02X}",
        "ptr_addr": f"${ptr_snes:06X}",
        "ptr_val":  "??",
        "target":   "??",
        "kind":     "??",
        "safe":     "",
        "note":     "",
        "zone":     zone,
    }

    if ptr_val is None:
        row["note"] = "pointer read outside ROM"
        return row

    row["ptr_val"] = f"${ptr_val:04X}"

    kind, addr_note = classify_ptr(ptr_val)
    row["kind"]   = kind
    row["target"] = f"${SPRITE_BANK:02X}{ptr_val:04X}"

    # Determine safe flags
    safe_flags = []
    if zone == "intentional" and ptr_val in valid_targets:
        safe_flags.append("valid table")
    if is_direct_rts(rom, ptr_val):
        safe_flags.append("direct RTS")
    row["safe"] = ", ".join(safe_flags)

    notes = []
    if addr_note:
        notes.append(addr_note)
    row["note"] = ", ".join(notes)

    return row


# ---------------------------------------------------------------------------
# Auto-detection
# ---------------------------------------------------------------------------

def _pc_to_snes_hirom(pc: int) -> int:
    bank   = pc >> 15
    offset = (pc & 0x7FFF) | 0x8000
    return (bank << 16) | offset


def detect_table(rom: bytes) -> tuple[int | None, int | None]:
    """
    Search for both U/J and E signatures.

    Returns (u_snes, e_snes).
    u_snes is set if the U/J signature is found (U/J ROM).
    e_snes is set if the E signature is found (E ROM) or inferred from u_snes.
    Either may be None if not found.
    """
    u_snes = e_snes = None

    pos = rom.find(_TABLE_SIG_U)
    if pos != -1:
        u_snes = _pc_to_snes_hirom(pos)
        e_snes = u_snes + _TABLE_SIG_E_DELTA

    pos = rom.find(_TABLE_SIG_E)
    if pos != -1:
        e_snes = _pc_to_snes_hirom(pos)

    return u_snes, e_snes


# ---------------------------------------------------------------------------
# Renderers
# ---------------------------------------------------------------------------

def _md_row(cells: list[str]) -> str:
    return "| " + " | ".join(cells) + " |"


def render_markdown(rows: list[dict], table_snes: int) -> str:
    headers = ["Sprite ID", "X reg", "Ptr addr", "Ptr val", "Target", "Kind", "Safe", "Zone", "Notes"]
    keys    = ["spr", "x_reg", "ptr_addr", "ptr_val", "target", "kind", "safe", "zone", "note"]
    lines   = [
        f"; Jump table base: ${table_snes:06X}  bank: ${SPRITE_BANK:02X}",
        "",
        _md_row(headers),
        _md_row(["---"] * len(headers)),
    ]
    for row in rows:
        lines.append(_md_row([row[k] for k in keys]))
    return "\n".join(lines)


def render_asm(rows: list[dict], table_snes: int) -> str:
    lines = [
        f"; Jump table base: ${table_snes:06X}  bank: ${SPRITE_BANK:02X}",
        f"; {'Sprite':>7} | {'X reg':>6} | {'Ptr addr':>8} | {'Ptr val':>7} | {'Target':>8} | {'Kind':>11} | {'Safe':>4} | {'Zone':>16} | Notes",
    ]
    for row in rows:
        lines.append(
            f";  {row['spr']:>7} | {row['x_reg']:>6} | {row['ptr_addr']:>8} | "
            f"{row['ptr_val']:>7} | {row['target']:>8} | {row['kind']:>11} | "
            f"{row['safe']:>4} | {row['zone']:>16} | {row['note']}"
        )
    return "\n".join(lines)


def render_grouped(rows: list[dict], table_snes: int) -> str:
    """Group by target address, listing all sprite IDs that share each target."""
    from collections import defaultdict
    groups: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        groups[row["target"]].append(row)

    lines = [
        f"; Jump table base: ${table_snes:06X}  bank: ${SPRITE_BANK:02X}",
        f"; Grouped by jump target -- {len(groups)} unique targets",
        "",
        _md_row(["Target", "Kind", "Safe", "Zone(s)", "Sprite IDs", "Count", "Notes"]),
        _md_row(["---"] * 7),
    ]

    for target in sorted(groups.keys()):
        entries  = groups[target]
        sprites  = ", ".join(r["spr"] for r in entries)
        count    = str(len(entries))
        zones    = ", ".join(sorted({r["zone"] for r in entries}))
        kind     = entries[0]["kind"]
        # All entries in a group share the same target so safe is consistent
        safe     = entries[0]["safe"]
        # Strip per-entry addr notes; keep structural notes (odd addr, direct RTS)
        note     = entries[0]["note"]
        lines.append(_md_row([target, kind, safe, zones, sprites, count, note]))

    return "\n".join(lines)


def render_named(rows: list[dict], table_snes: int, names: dict[int, str]) -> str:
    """Compact format: ID | Name | Kind | Target | Safe | Notes"""
    headers = ["ID", "Name", "Kind", "Target", "Safe", "Notes"]
    lines   = [
        f"; Jump table base: ${table_snes:06X}  bank: ${SPRITE_BANK:02X}",
        "",
        _md_row(headers),
        _md_row(["---"] * len(headers)),
    ]
    for row in rows:
        spr_int = int(row["spr"][1:], 16)
        name    = names.get(spr_int, "(unknown)")
        lines.append(_md_row([
            row["spr"],
            name,
            row["kind"],
            row["target"],
            row["safe"],
            row["note"],
        ]))
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Argument parser
# ---------------------------------------------------------------------------

def parse_int(value: str) -> int:
    value = value.strip()
    if value.startswith("$"):
        return int(value[1:], 16)
    return int(value, 0)


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Dump the Yoshi's Island sprite handler JSR jump table.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("rom", help="ROM file (headered or unheadered .sfc/.smc)")
    parser.add_argument(
        "--table",
        type=parse_int,
        default=None,
        metavar="SNES_ADDR",
        help=(
            f"SNES address of the jump table DP operand "
            f"(U/J default: ${DEFAULT_TABLE_SNES_U:06X}, "
            f"E default: ${DEFAULT_TABLE_SNES_E:06X}). "
            "Auto-detected if omitted."
        ),
    )
    parser.add_argument(
        "--first", type=parse_int, default=SPR_FIRST_DEFAULT,
        metavar="SPR_ID", help=f"first sprite ID to dump (default: ${SPR_FIRST_DEFAULT:04X})"
    )
    parser.add_argument(
        "--last", type=parse_int, default=SPR_LAST_DEFAULT,
        metavar="SPR_ID", help=f"last sprite ID to dump (default: ${SPR_LAST_DEFAULT:04X})"
    )
    parser.add_argument(
        "--format",
        default="markdown",
        metavar="FMT[,FMT...]",
        help=(
            "comma-separated list of output formats to include. "
            "Choices: markdown, asm, grouped, named. "
            "Multiple formats are separated by a blank line in the output. "
            "Default: markdown"
        ),
    )
    parser.add_argument(
        "--names",
        default=None,
        metavar="PATH",
        help="path to sprite_ids.md (auto-located relative to this script if omitted)",
    )
    parser.add_argument("--output", help="write output to this file instead of stdout")
    return parser


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    parser = make_parser()
    args   = parser.parse_args()

    if args.last < args.first:
        raise SystemExit("--last must be >= --first")

    rom = open_rom(args.rom)

    # --- Auto-detect or accept user-supplied table address ----------------
    u_auto, e_auto = detect_table(rom)

    if args.table is not None:
        table_snes = args.table
        print(f"[manual] using table at ${table_snes:06X}", file=sys.stderr)
    elif e_auto is not None and u_auto is None:
        # E-only ROM: U/J signature absent, E signature present
        table_snes = e_auto
        print(f"[auto]   E-version table detected at ${table_snes:06X}", file=sys.stderr)
    elif u_auto is not None:
        table_snes = u_auto
        print(f"[auto]   table detected at ${table_snes:06X} (U/J version)", file=sys.stderr)
        if e_auto is not None:
            print(
                f"[auto]   E-version table would be at ${e_auto:06X} "
                f"(use --table ${e_auto:06X} to select it)",
                file=sys.stderr,
            )
    else:
        table_snes = DEFAULT_TABLE_SNES_U
        print(
            f"[warn]   signature not found; falling back to default ${table_snes:06X}",
            file=sys.stderr,
        )

    table_dp = table_snes & 0xFFFF   # low 16-bit offset used as DP in JSR (dp, x)

    # --- Parse and validate format list -----------------------------------
    VALID_FORMATS = {"markdown", "asm", "grouped", "named"}
    formats = [f.strip() for f in args.format.split(",")]
    unknown = [f for f in formats if f not in VALID_FORMATS]
    if unknown:
        raise SystemExit(
            f"Unknown format(s): {', '.join(unknown)}. "
            f"Choose from: {', '.join(sorted(VALID_FORMATS))}"
        )

    # --- Sprite names (needed for 'named' format) -------------------------
    if "named" in formats:
        names_path = args.names
        if names_path is None:
            script_dir = Path(__file__).parent
            candidate  = script_dir / "sprite_ids.md"
            names_path = str(candidate) if candidate.exists() else "sprite_ids.md"
        names = load_sprite_names(names_path)
        if not names:
            print(f"[warn] no sprite names loaded from {names_path!r}", file=sys.stderr)
    else:
        names = {}

    # --- Derive valid targets from the ROM --------------------------------
    valid_targets = read_valid_targets(rom, table_dp)

    # --- Build rows -------------------------------------------------------
    rows = [build_row(rom, spr, table_dp, valid_targets) for spr in range(args.first, args.last + 1)]

    # --- Render each requested format and join ----------------------------
    sections = []
    for fmt in formats:
        if fmt == "asm":
            sections.append(render_asm(rows, table_snes))
        elif fmt == "grouped":
            sections.append(render_grouped(rows, table_snes))
        elif fmt == "named":
            sections.append(render_named(rows, table_snes, names))
        else:
            sections.append(render_markdown(rows, table_snes))
    text = "\n\n".join(sections)

    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    else:
        sys.stdout.write(text + "\n")


if __name__ == "__main__":
    main()
