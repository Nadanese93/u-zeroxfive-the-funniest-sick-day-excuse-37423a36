"""The Funniest Sick-Day Excuse: write one line to entry.txt.

The entry is a single line under 200 characters: a sick-day excuse
a boss might half believe, with the twist landing at the end.
"""

import os

ENTRY = "Locked myself out of my own apartment and the locksmith can't come till noon. Technically I'm homeless until then."

MAX_CHARS = 200


def main() -> None:
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY)}")
    if not ENTRY.strip():
        raise ValueError("entry must not be whitespace-only")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/tmp/out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(os.path.join(out_dir, "entry.txt"), 0o644)


if __name__ == "__main__":
    main()
