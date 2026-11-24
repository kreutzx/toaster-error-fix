"""Entry for make.fun's 'The Funniest Toaster Error Message' bounty.

The whole submission is a single line: the error message a kitchen
toaster shows its owner. The tray has been full since March, the same
corner of the toast has burned 41 mornings in a row, and the toaster
has stopped pretending any of that is a malfunction. The program
writes that one line to /output/entry.txt.
"""

MESSAGE = "CRUMB TRAY FULL SINCE MARCH. I have burned the same corner 41 mornings in a row. Not a defect. A signature."

MAX_CHARS = 120  # the bounty caps the line at 120 characters


def render() -> str:
    """Return the message, verified against the character cap."""
    text = MESSAGE.strip()
    assert 1 <= len(text) <= MAX_CHARS, f"message runs {len(text)} characters"
    return text


def main() -> None:
    import os

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    line = render()
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(line)
    # Read it back: the file on disk must hold the line byte for byte,
    # with nothing added and nothing trimmed.
    with open(out_path, "r", encoding="utf-8") as handle:
        assert handle.read() == line, "entry.txt does not match the message"


if __name__ == "__main__":
    main()
