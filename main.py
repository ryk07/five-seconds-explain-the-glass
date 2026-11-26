"""Five Seconds to Explain the Glass.

Writes the house cat's one-sentence defence to /output/entry.txt.

The line: three grievances, zero remorse. The glass was empty (useless),
it was squatting in the cat's sunbeam (trespass), and it looked at the cat
first (provocation) -- so the cat simply restored order to its table.
Cat logic, self-interest, no apology, no confession, one spoken sentence.
"""

import os

ENTRY = (
    "It was empty, it was squatting in my sunbeam, and it looked at me "
    "first \u2014 I simply restored order to my table."
)


def main() -> None:
    text = ENTRY.strip()
    # Gate: one sentence, 1-200 chars, no apology, no confession.
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    assert text.endswith("."), "entry must be one complete sentence"
    assert not any(
        mark in text[:-1] for mark in (".", "!", "?")
    ), "must be a single sentence"
    lowered = text.lower()
    assert not any(
        word in lowered
        for word in ("sorry", "apolog", "my fault", "i did it", "i confess")
    ), "a cat never apologises or confesses"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
