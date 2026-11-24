"""One Letter: Coffee or Tea -- entry A (coffee).

Writes exactly one letter to the output file: "A" for coffee.
The grader reads /output/entry.txt (MAKEFUN_OUTPUT_DIR/entry.txt)
and the gate requires UTF-8 text of exactly 1 character.
Pure standard library only.
"""

import os

CHOICE = "A"  # A = coffee, B = tea

# The gate accepts exactly one character: "A" or "B", nothing else.
VALID_CHOICES = ("A", "B")


def main():
    if CHOICE not in VALID_CHOICES or len(CHOICE) != 1:
        raise ValueError("CHOICE must be exactly one letter: A or B")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(CHOICE)
    # Verify what landed on disk: exactly one letter, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != CHOICE:
        raise ValueError("entry.txt must contain exactly one letter")


if __name__ == "__main__":
    main()
