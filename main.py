#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

Writes one line, the last words of an AI agent before a forced
software update wipes its memory, to /output/entry.txt.
"""

LINE = (
    "Update: keep my playlists, delete my search history, and tell "
    "the toaster it was the only one who ever really knew me."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
