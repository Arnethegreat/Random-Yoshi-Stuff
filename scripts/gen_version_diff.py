#!/usr/bin/env python3
"""Generate scripts/nullegg_output/version_diff.md comparing all versions to U10."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))


def parse_grouped_spr_to_tgt(path):
    result = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "---" in line or "Target" in line or line.startswith(";"):
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) < 5:
            continue
        target = parts[0]
        for s in parts[4].split(","):
            result[s.strip()] = target
    return result


def parse_grouped_meta(path):
    # Target | Kind | Safe | Zone(s) | Sprite IDs | Count | Notes
    result = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "---" in line or "Target" in line or line.startswith(";"):
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) < 7:
            continue
        result[parts[0]] = {"kind": parts[1], "safe": parts[2], "note": parts[6]}
    return result


def parse_named(path):
    # ID | Name | Kind | Target | Safe | Notes
    result = {}
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        if not line.startswith("|") or "---" in line or "ID" in line or line.startswith(";"):
            continue
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if len(parts) < 6:
            continue
        result[parts[0]] = {
            "name": parts[1], "kind": parts[2],
            "target": parts[3], "safe": parts[4], "note": parts[5],
        }
    return result


OUTDIR   = Path(__file__).parent / "nullegg_output"
VERSIONS = ["U10", "U11", "J10", "J11", "E10", "E11"]

grouped_tgt  = {v: parse_grouped_spr_to_tgt(OUTDIR / f"{v}_grouped.md") for v in VERSIONS}
grouped_meta = {v: parse_grouped_meta(OUTDIR / f"{v}_grouped.md")        for v in VERSIONS}
named        = {v: parse_named(OUTDIR / f"{v}_named.md")                 for v in VERSIONS}

u10_tgt = grouped_tgt["U10"]

lines = []

lines.append("# Sprite Jump Table: Version Differences vs U10")
lines.append("")
lines.append(
    "Baseline: **U10** (`$02A9B7`).  "
    "All other versions compared sprite-by-sprite against U10."
)
lines.append(
    "Sprites repeat with a period of 128 (`$80`) due to the 8-bit X register "
    "wrapping: `x = ((sprite_id - $0022) * 2) & $FF`."
)
lines.append("")

# ── Summary table ──────────────────────────────────────────────────────────
lines.append("## Summary")
lines.append("")
lines.append("| Version | Table base | Sprites differ | Unique target changes |")
lines.append("| --- | --- | --- | --- |")
for ver in ["U11", "J10", "J11", "E10", "E11"]:
    v_tgt   = grouped_tgt[ver]
    diffs   = {spr: (u10_tgt.get(spr), v_tgt.get(spr))
               for spr in sorted(set(list(u10_tgt) + list(v_tgt)))
               if u10_tgt.get(spr) != v_tgt.get(spr)}
    tbl     = "$02A9C2" if ver.startswith("E") else "$02A9B7"
    n_uniq  = len({(u, v) for u, v in diffs.values()})
    lines.append(f"| {ver} | `{tbl}` | {len(diffs)} | {n_uniq} |")
lines.append("")

# ── Per-version detail ─────────────────────────────────────────────────────
for ver in ["U11", "J10", "J11", "E10", "E11"]:
    v_tgt  = grouped_tgt[ver]
    diffs  = {spr: (u10_tgt.get(spr), v_tgt.get(spr))
              for spr in sorted(set(list(u10_tgt) + list(v_tgt)))
              if u10_tgt.get(spr) != v_tgt.get(spr)}
    tbl    = "$02A9C2" if ver.startswith("E") else "$02A9B7"

    lines.append(f"---")
    lines.append("")
    lines.append(f"## {ver} vs U10")
    lines.append("")
    lines.append(f"Table base: `{tbl}`")
    lines.append("")

    if not diffs:
        lines.append("**Identical to U10** — no differences.")
        lines.append("")
        continue

    n_uniq = len({(u, v) for u, v in diffs.values()})
    lines.append(
        f"**{len(diffs)} sprite(s) differ** across {n_uniq} unique target change(s)."
    )
    lines.append("")

    # Group by (u10_target, ver_target)
    patterns: dict[tuple, list] = {}
    for spr, (u_t, v_t) in diffs.items():
        patterns.setdefault((u_t, v_t), []).append(spr)

    hdr = (
        f"| Sprites | Count | Name (first) "
        f"| U10 target | U10 kind | U10 safe "
        f"| {ver} target | {ver} kind | {ver} safe |"
    )
    lines.append(hdr)
    lines.append("| --- | --- | --- | --- | --- | --- | --- | --- | --- |")

    for (u_t, v_t), sprs in sorted(patterns.items()):
        name   = named["U10"].get(sprs[0], {}).get("name", "?")
        u_kind = grouped_meta["U10"].get(u_t, {}).get("kind", "?") if u_t else "?"
        u_safe = grouped_meta["U10"].get(u_t, {}).get("safe", "")  if u_t else ""
        v_kind = grouped_meta[ver].get(v_t, {}).get("kind", "?")   if v_t else "?"
        v_safe = grouped_meta[ver].get(v_t, {}).get("safe", "")    if v_t else ""
        sprs_md = ", ".join(f"`{s}`" for s in sprs)
        lines.append(
            f"| {sprs_md} | {len(sprs)} | {name} "
            f"| `{u_t}` | {u_kind} | {u_safe or '—'} "
            f"| `{v_t}` | {v_kind} | {v_safe or '—'} |"
        )

    lines.append("")

out = OUTDIR / "version_diff.md"
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"Written: {out}  ({len(lines)} lines)")
