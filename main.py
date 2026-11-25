#!/usr/bin/env python3
"""Have You Tried Turning It Off?

Writes one line -- the reply a hopeless tech support agent gives a
desperate customer -- to /output/entry.txt.

The joke: the agent cheerfully "escalates" the ticket, but Tier 2 turns
out to be the same agent in a different headset. The escalation is real
support language, the payoff is that nothing actually changes -- the
agent's cheerful uselessness is the humour, and the customer is never
the butt of it.
"""

import os

ENTRY = (
    "Great news: I've escalated your ticket to Tier 2 \u2014 that's just "
    "me, with a different headset."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
