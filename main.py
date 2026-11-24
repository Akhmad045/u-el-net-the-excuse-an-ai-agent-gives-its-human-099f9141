#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human.

Writes one line -- the funniest, most believable excuse an AI agent could
give its human for missing a deadline -- to /output/entry.txt.
Stdlib only, deterministic, no network, no randomness.
"""

import os

ENTRY = "Your 'just one more tweak' requests filled my context window, so I evicted the deadline to make room."


def validate(text: str) -> None:
    """Gate: single line, 1-200 characters, non-blank."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not text.strip():
        raise ValueError("entry must not be blank")


def main() -> None:
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    validate(ENTRY)
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise RuntimeError("read-back mismatch: file differs from entry")


if __name__ == "__main__":
    main()
