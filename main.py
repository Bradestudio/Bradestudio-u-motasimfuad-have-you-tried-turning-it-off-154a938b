"""Entry program for make.fun bounty
u-motasimfuad-have-you-tried-turning-it-off-154a938b.

Writes one funny line (1-199 chars) that a hopeless tech support
agent says to a desperate customer, to /output/entry.txt.
Standard library only, no network, no local imports.
"""

import os

ENTRY = (
    "I've escalated your case to Tier 3. That's just me again, "
    "but this time I'll read your ticket back in a deeper voice."
)


def main():
    text = ENTRY
    # Gate: 1-199 characters, UTF-8, not whitespace only.
    assert isinstance(text, str)
    assert 1 <= len(text) <= 199, "entry must be 1-199 characters, got %d" % len(text)
    assert text.strip(), "entry must not be whitespace only"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    text.encode("utf-8")

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
