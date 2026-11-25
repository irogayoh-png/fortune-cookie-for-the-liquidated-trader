#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader -- make.fun program/v1 entry.

Writes one original fortune-cookie line (107 characters, 18 words) for a
crypto trader who has just been liquidated, to <output>/entry.txt, where
<output> is $MAKEFUN_OUTPUT_DIR or /output when that variable is unset.

The line is fixed, so every run is deterministic: same input, same
output, byte for byte. No network, no dependencies, no trailing newline.

Why this line: it opens in the small, formal fortune voice ("Dear
trader, your fortune was inside this cookie") and then the punchline
breaks it -- the market ate the cookie, the fortune, and the trader's
savings, in one escalating bite. The loss is in the joke, the trader is
the one being comforted rather than mocked, and the market, not the
trader, is the hungry one. Rueful and warm, never cruel or smug.
"""

import os

FORTUNE = (
    "Dear trader, your fortune was inside this cookie; "
    "the market ate the cookie, the fortune, and your savings."
)


def main() -> None:
    words = FORTUNE.split()
    if not 1 <= len(FORTUNE) <= 160 or len(words) > 20 or "\n" in FORTUNE:
        raise SystemExit(
            "fortune must be one line of 1 to 160 characters, at most 20 words"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)
    print("Wrote %d characters (%d words) to %s" % (len(FORTUNE), len(words), path))


if __name__ == "__main__":
    main()
