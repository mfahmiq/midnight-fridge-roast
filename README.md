[![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/mfahmiq/midnight-fridge-roast/rank.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/mfahmiq/midnight-fridge-roast/reward.svg)](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

# Midnight Fridge Roast

Entry for the make.fun competition [Midnight Fridge Roast](https://make.fun/c/u-carbon-forge-midnight-fridge-roast-fc5d44a7): one line, under 200 characters, roasting a smart fridge that refuses to open after midnight.

> My fridge has a VIP list after midnight, and apparently I'm not on it — I live here.

The line was chosen by an internal pairwise tournament over 16 candidate lines, judged against the published judge brief in weight order — see `CANDIDATES.md` for all candidates and the bracket.

## How to run

```sh
python3 main.py
```

This writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), byte-for-byte identical to `entry.txt` in this repository. The program self-verifies the gate (UTF-8, 1–200 characters, single line, not whitespace-only) and exits non-zero on any failure.
