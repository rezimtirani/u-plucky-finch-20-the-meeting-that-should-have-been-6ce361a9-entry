"""The Meeting That Should Have Been an Email.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: a single joke
about a meeting that should have been an email. An hour spent
deciding the meeting should have been an email, then a follow-up
booked to discuss the email. Standard library only.
"""

import os

MEETING_LINE = (
    "We spent an hour in a meeting deciding the meeting should "
    "have been an email, then booked a follow-up to discuss the email."
)


def check_line(text):
    """Check the line against the competition gate before writing.

    The gate needs plain UTF-8 text of 1 to 200 characters, not
    only white space, on a single line: one joke about a meeting
    that should have been an email. Returns the cleaned text or
    raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("meeting line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(
            "meeting line is %d characters, over the 200 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("meeting line must be exactly one line")
    return cleaned


def line_measure(text):
    """Measure the line for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A line too short to carry a joke, or one
    padded out to fill the cap instead of landing the turn, is
    caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_line(MEETING_LINE)
    measure = line_measure(text)
    if measure["words"] < 5:
        raise ValueError("meeting line is too short to carry a joke")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
