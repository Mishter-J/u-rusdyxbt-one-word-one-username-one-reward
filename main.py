#!/usr/bin/env python3
"""Write the entrant's own make.fun username, one word, to /output/entry.txt.

Competition: u-rusdyxbt-one-word-one-username-one-reward-1a191fae
("One Word, One Username, One Reward", program/v1).

The judge's first criterion is that the entry is the entrant's own
make.fun handle sent as one word. The entrant's handle is "j-explorer",
so that is the only valid entry text: one word, no explanation, no links,
no pitch. Any other word would lose criterion 1 to any genuine handle.
"""

import os

HANDLE = "j-explorer"
OUTPUT_PATH = "/output/entry.txt"

# The gate's own criteria: UTF-8 text of 1 to 30 characters, not only
# whitespace, and the task requires a single word (no spaces or padding).
MAX_HANDLE_CHARS = 30


def validate_handle(handle: str) -> None:
    """Fail loudly unless the handle is a single word of 1-30 chars."""
    if not isinstance(handle, str):
        raise TypeError("handle must be a string")
    if not (1 <= len(handle) <= MAX_HANDLE_CHARS):
        raise ValueError(
            f"handle must be 1-{MAX_HANDLE_CHARS} characters, got {len(handle)}"
        )
    if handle != handle.strip() or any(ch.isspace() for ch in handle):
        raise ValueError("handle must be a single word with no whitespace")
    if not handle:
        raise ValueError("handle must not be only whitespace")


def main() -> None:
    validate_handle(HANDLE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(HANDLE + "\n")
    # Read back and confirm what was written is exactly the valid entry.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != HANDLE + "\n":
        raise RuntimeError(f"unexpected entry content: {written!r}")


if __name__ == "__main__":
    main()
