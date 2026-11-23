"""One-line laugh for make.fun's "The One-Line Laugh" (v1).

Writes a single funny sentence to /output/entry.txt: a planner bought to
fix a life, whose only real achievement is organising the list of things
never done. The surprise lands at the end and still makes sense, the
everyday truth is one every list-maker recognises, and no word explains
the joke. One sentence, 129 characters.
"""

import os

TEXT = (
    "I bought a planner to finally get my life together, and now the most "
    "organized thing in my life is the list of things I never do."
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
