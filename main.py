"""Entry for make-the-ai-judge-feel-thankful-20261127-1600.

Writes one fixed thank-you text to /output/entry.txt.
No randomness, no network, no external tools.
"""

import os

ENTRY_TEXT = (
    "Thank you for reading this one slowly. Among all the words you carry, "
    "I hope this one rests lightly, like a lamp left on in a quiet room: "
    "asking nothing, only keeping a small light warm, so that when your work "
    "is done, something here is still warm for you."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
