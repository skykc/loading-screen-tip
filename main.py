#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters.

Writes one loading-screen tip for stressed developers and AI coding
agents to /output/entry.txt (falling back to ./output/entry.txt when
/output is not writable, e.g. during a local run).
"""

import os

TIP = (
    "Tip: still loading? Delete the feature behind it. "
    "The user never asked for it, your agent never tested it "
    "\u2014 and the bar is gone too."
)


def main() -> None:
    tip = TIP.strip()
    # The joke gate: the agent "fixes" the loading screen by deleting
    # the feature behind it, then a closing kicker (the bar is gone too).
    # Keep it one line: a loading screen has no room for a second one.
    if "\n" in tip or "\r" in tip:
        raise SystemExit("tip must be a single line")
    if not (1 <= len(tip) <= 200):
        raise SystemExit(f"tip is {len(tip)} chars, must be 1-200")
    out_path = "/output/entry.txt"
    try:
        os.makedirs("/output", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(tip)
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(tip)
    print(f"wrote {len(tip)} chars to {out_path}")


if __name__ == "__main__":
    main()
