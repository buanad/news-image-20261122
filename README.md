# World news of 22 November 2026 in one image

A make.fun Growth bounty entry: one 1024×1024 image summing up Sunday
22 November 2026's world news — 31 stories from 7 regions. Every story
carries a confidence chip (CF = confirmed, RP = reported, CL = one side's
claim) and a UTC time, plus a "THE DAY IN UTC" strip, a world map, and a
DATE CHECK footer naming what was deliberately left out because it broke
before 22 November.

`main.py` (Python standard library only) copies `entry.png` to the
output directory and verifies the copy byte for byte (size + SHA-256).

Run: `python3 main.py [output-dir]` (default `$MAKEFUN_OUTPUT_DIR`,
else `/output`).
