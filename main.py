"""One-line laugh for make.fun's "The One-Line Laugh" (v2).

Writes a single funny sentence to /output/entry.txt: a smartwatch's praise
for standing up, reframed as the only applause a life gets for doing the
bare minimum. The surprise lands at the end and still makes sense, the
everyday truth is one every smartwatch wearer recognises, and no word
explains the joke. One sentence, 112 characters.
"""

import os

TEXT = (
    "My smartwatch congratulated me for standing up, which is now the only "
    "applause I get for doing the bare minimum."
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
