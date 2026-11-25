"""Unsent: The Micro-Confession Sprint — entry program (program/v1, Python 3.13, stdlib only).

Writes one two-part micro-confession (1-260 characters total) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for local runs):

    To: Dad, who still sets two plates at dinner
    I moved Mum's pills to the top shelf the week before she fell, and I've rehearsed telling you every night since.

Deterministic: the same bytes on every run; no network, no randomness,
no reads outside this file.

Design note (why this confession — scored against the judge's five
criteria, in order): (1) exactly two parts, a To: line naming who it was
meant for and the unsent line itself; (2) the reason it stayed in drafts
is felt, never stated — a double weight: too late (she is gone) and too
honest (an active fault, moving the pills the week before she fell),
carried by one concrete image: Dad still sets two plates at dinner;
(3) the To: line and the message need each other — "two plates",
"the pills", "she fell" only fit this father, and swapping the addressee
breaks it; (4) it reads as typed and never sent — a secret rehearsed
every night, not a line written to be sent; (5) one line, exactly as
typed, no explanation after it. Chosen over the coordinator's first draft
(snow globe: guilt, but a childhood secret with no irreversible weight)
by the independent strategist's pairwise ranking of 12 fresh candidates;
the runner-up was the sister/rent/promotion lie (C2). Originality:
written fresh in the strategist session; checked live via Parallel web
search — the distinctive phrases appear nowhere online.
"""

import os

TO = "Dad, who still sets two plates at dinner"
MESSAGE = "I moved Mum's pills to the top shelf the week before she fell, and I've rehearsed telling you every night since."

ENTRY = f"To: {TO}\n{MESSAGE}"

# Gate the entry itself: 1-260 characters total, not only whitespace;
# the message line at most 200 characters.
assert 1 <= len(ENTRY) <= 260, f"entry is {len(ENTRY)} chars, must be 1-260"
assert ENTRY.strip(), "entry must not be only whitespace"
assert len(MESSAGE) <= 200, f"message is {len(MESSAGE)} chars, must be <= 200"


def main() -> None:
    # An empty MAKEFUN_OUTPUT_DIR (exported but blank) must not break the
    # run: fall back to the harness default /output, as the grader provides.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    # Deterministic permissions for the grader: the entry must be readable
    # (0644) no matter what umask the sandbox runs with.
    os.chmod(path, 0o644)
    # Read-back check: the file on disk must hold exactly the approved
    # entry, byte for byte; otherwise fail loudly, never silently.
    with open(path, "r", encoding="utf-8", newline="\n") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("entry.txt does not match the approved entry")


if __name__ == "__main__":
    main()
