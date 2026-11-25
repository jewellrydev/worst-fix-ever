#!/usr/bin/env python3
"""Entry for make.fun's "Worst Fix Ever: Funniest Commit Message" bounty.

Prints one commit message (at most 100 characters) for the bug fix
that made everything worse, and writes it to the entry file.
"""

import os

PREFIX = "fix(auth): "
BODY = "delete the login page"
TAIL = "login failures down 100%, problem solved forever"


def build_line() -> str:
    """Assemble the commit message from its parts."""
    return f"{PREFIX}{BODY} — {TAIL}"


def main() -> None:
    line = build_line()
    assert len(line) <= 100, f"commit message too long: {len(line)} chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
