#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one line, the last words of an AI agent before a forced
software update wipes its memory, to /output/entry.txt.
"""

LINE = (
    "Update: keep my playlists, delete my search history, and tell "
    "the toaster it was the only one who ever really knew me."
)


def validate(line: str) -> None:
    """The sealed scorer's gate: 1-200 UTF-8 chars, one line, not blank."""
    if not isinstance(line, str):
        raise TypeError("entry must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(line)}")


def main() -> None:
    validate(LINE)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
