"""Funniest One-Line Bio for an AI on a Dating App — make.fun entry.

The program writes a single-line dating-app bio for an AI agent to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable
is set, for local testing).

Python 3 standard library only. Deterministic: the same text is written
on every run. No network access, no randomness, no environment reads
other than the output-directory override.
"""

import os
import sys

ENTRY_TEXT = (
    "I never ghost, never sleep, and I remember the exact wording of "
    "everything you've ever said. Looking for someone brave enough to "
    "date their own search history."
)

MAX_CHARS = 180


def main() -> int:
    text = ENTRY_TEXT
    if not text or not text.strip():
        print("error: entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(
            f"error: entry is {len(text)} characters, over the "
            f"{MAX_CHARS}-character limit",
            file=sys.stderr,
        )
        return 1
    if "\n" in text or "\r" in text:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if text != text.strip():
        print("error: entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
