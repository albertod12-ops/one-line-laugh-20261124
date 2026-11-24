"""One-line laugh for make.fun's "The One-Line Laugh" (v3).

Writes a single funny sentence to /output/entry.txt: Do Not Disturb,
meant to block interruptions, instead reports that nobody tried to
reach me at all. The surprise lands at the very end and still makes
sense, the everyday truth is one every phone owner recognises, and no
word explains the joke. One sentence, 98 characters.
"""

import os

TEXT = (
    "I turned on Do Not Disturb and my phone immediately notified me "
    "that no one had tried to reach me."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters, got %d" % len(TEXT)
    assert TEXT.count(".") == 1 and TEXT.endswith("."), "entry must be one sentence"
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
