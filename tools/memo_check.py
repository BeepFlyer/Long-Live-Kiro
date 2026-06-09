#!/usr/bin/env python3
"""
memo_check.py — Memo word count checker for Long Live Kiro

Usage:
    python memo_check.py [path_to_memo.md]

If no path is provided, looks for memo.md in the same directory as this script's parent.

Output:
    DISTILL_NEEDED  — memo has reached threshold (>= 2000 chars), distillation recommended
    SKIP            — memo is below threshold, continue accumulating

Exit codes:
    0 — success
    1 — memo.md not found or empty
"""

import sys
import os

THRESHOLD = 2000  # characters


def get_memo_path():
    """Determine memo.md path from argument or relative to script location."""
    if len(sys.argv) > 1:
        return sys.argv[1]

    # Default: look for memo.md in parent directory of tools/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(os.path.dirname(script_dir), "memo.md")


def main():
    memo_path = get_memo_path()

    if not os.path.exists(memo_path):
        print(f"SKIP (memo.md not found: {memo_path})")
        sys.exit(1)

    with open(memo_path, "r", encoding="utf-8") as f:
        content = f.read()

    char_count = len(content.strip())

    if char_count == 0:
        print("SKIP (memo is empty)")
        sys.exit(1)

    if char_count >= THRESHOLD:
        print(f"DISTILL_NEEDED ({char_count} chars >= {THRESHOLD} threshold)")
    else:
        print(f"SKIP ({char_count} chars < {THRESHOLD} threshold)")


if __name__ == "__main__":
    main()
