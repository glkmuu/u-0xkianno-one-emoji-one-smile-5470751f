"""One Emoji, One Smile.

Writes exactly one emoji to entry.txt: a waving hand, the friendly
greeting a stranger gives with no words at all. One Unicode code
point only (U+1F44B), no variation selector, no skin-tone modifier,
no joining sequence, so the entry is a single character and four
UTF-8 bytes. Deterministic: every run writes the same bytes.
"""

import os

EMOJI = "\U0001F44B"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    # Exactly the emoji, nothing else: no words, no caption,
    # no trailing newline, so the file holds one character.
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(EMOJI)
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
