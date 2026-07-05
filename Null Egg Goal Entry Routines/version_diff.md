# Sprite Jump Table: Version Differences vs U10

Baseline: **U10** (`$02A9B7`).  All other versions compared sprite-by-sprite against U10.
Sprites repeat with a period of 128 (`$80`) due to the 8-bit X register wrapping: `x = ((sprite_id - $0022) * 2) & $FF`.

## Summary

| Version | Table base | Sprites differ | Unique target changes |
| --- | --- | --- | --- |
| U11 | `$02A9B7` | 3 | 1 |
| J10 | `$02A9B7` | 3 | 1 |
| J11 | `$02A9B7` | 3 | 1 |
| E10 | `$02A9C2` | 47 | 7 |
| E11 | `$02A9C2` | 47 | 7 |

---

## U11 vs U10

Table base: `$02A9B7`

**3 sprite(s) differ** across 1 unique target change(s).

| Sprites | Count | Name (first) | U10 target | U10 kind | U10 safe | U11 target | U11 kind | U11 safe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `$0036`, `$00B6`, `$0136` | 3 | (BG3) Falling down wall | `$028E22` | ROM | — | `$02A722` | ROM | — |

---

## J10 vs U10

Table base: `$02A9B7`

**3 sprite(s) differ** across 1 unique target change(s).

| Sprites | Count | Name (first) | U10 target | U10 kind | U10 safe | J10 target | J10 kind | J10 safe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `$0036`, `$00B6`, `$0136` | 3 | (BG3) Falling down wall | `$028E22` | ROM | — | `$022922` | RAM/IO | — |

---

## J11 vs U10

Table base: `$02A9B7`

**3 sprite(s) differ** across 1 unique target change(s).

| Sprites | Count | Name (first) | U10 target | U10 kind | U10 safe | J11 target | J11 kind | J11 safe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `$0036`, `$00B6`, `$0136` | 3 | (BG3) Falling down wall | `$028E22` | ROM | — | `$02A722` | ROM | — |

---

## E10 vs U10

Table base: `$02A9C2`

**47 sprite(s) differ** across 7 unique target change(s).

| Sprites | Count | Name (first) | U10 target | U10 kind | U10 safe | E10 target | E10 kind | E10 safe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `$0008`, `$0088`, `$0108`, `$0188` | 4 | Rubble | `$02214C` | RAM/IO | — | `$022C4C` | RAM/IO | — |
| `$0036`, `$00B6`, `$0136` | 3 | (BG3) Falling down wall | `$028E22` | ROM | — | `$02D622` | ROM | — |
| `$0023`, `$0024`, `$0025`, `$0029`, `$00A3`, `$00A4`, `$00A5`, `$00A9`, `$0123`, `$0124`, `$0125`, `$0129`, `$01A3`, `$01A4`, `$01A5`, `$01A9` | 16 | Red Egg | `$02A981` | ROM | valid table, direct RTS | `$02A98C` | ROM | valid table, direct RTS |
| `$0022`, `$00A2`, `$0122`, `$01A2` | 4 | Flashing Egg | `$02A9CB` | ROM | valid table | `$02A9D6` | ROM | valid table |
| `$0027`, `$00A7`, `$0127`, `$01A7` | 4 | Key | `$02AA20` | ROM | valid table | `$02AA2B` | ROM | valid table |
| `$0028`, `$00A8`, `$0128`, `$01A8` | 4 | Huffin' Puffin, running away | `$02AA2A` | ROM | valid table | `$02AA35` | ROM | valid table |
| `$0026`, `$002A`, `$002B`, `$00A6`, `$00AA`, `$00AB`, `$0126`, `$012A`, `$012B`, `$01A6`, `$01AA`, `$01AB` | 12 | Giant Egg, for battle with Bowser | `$02AA36` | ROM | valid table | `$02AA41` | ROM | valid table |

---

## E11 vs U10

Table base: `$02A9C2`

**47 sprite(s) differ** across 7 unique target change(s).

| Sprites | Count | Name (first) | U10 target | U10 kind | U10 safe | E11 target | E11 kind | E11 safe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `$0008`, `$0088`, `$0108`, `$0188` | 4 | Rubble | `$02214C` | RAM/IO | — | `$022C4C` | RAM/IO | — |
| `$0036`, `$00B6`, `$0136` | 3 | (BG3) Falling down wall | `$028E22` | ROM | — | `$02D822` | ROM | — |
| `$0023`, `$0024`, `$0025`, `$0029`, `$00A3`, `$00A4`, `$00A5`, `$00A9`, `$0123`, `$0124`, `$0125`, `$0129`, `$01A3`, `$01A4`, `$01A5`, `$01A9` | 16 | Red Egg | `$02A981` | ROM | valid table, direct RTS | `$02A98C` | ROM | valid table, direct RTS |
| `$0022`, `$00A2`, `$0122`, `$01A2` | 4 | Flashing Egg | `$02A9CB` | ROM | valid table | `$02A9D6` | ROM | valid table |
| `$0027`, `$00A7`, `$0127`, `$01A7` | 4 | Key | `$02AA20` | ROM | valid table | `$02AA2B` | ROM | valid table |
| `$0028`, `$00A8`, `$0128`, `$01A8` | 4 | Huffin' Puffin, running away | `$02AA2A` | ROM | valid table | `$02AA35` | ROM | valid table |
| `$0026`, `$002A`, `$002B`, `$00A6`, `$00AA`, `$00AB`, `$0126`, `$012A`, `$012B`, `$01A6`, `$01AA`, `$01AB` | 12 | Giant Egg, for battle with Bowser | `$02AA36` | ROM | valid table | `$02AA41` | ROM | valid table |

