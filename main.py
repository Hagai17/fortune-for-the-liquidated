#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

Writes one fortune cookie line to /output/entry.txt and prints it.

Why this line (full record in candidates.md): the judge is a freshly
liquidated trader who keeps the fortune that makes them laugh instead of
cry, weighing cookie voice + the loss itself first, then the laugh, then
freshness. The field of 594 finished entries is saturated with "lucky
numbers 0, 0, 0", "tall, dark stranger: your margin call" and "your next
trade will be your best one", so this entry takes an empty lane: the
oracle's "green" (candles) turns out to be a salad — all the liquidation
left. The line was duelled in both orders against the five strongest
field artifacts under the kit's published judge brief and chosen for the
heat as a whole, not for any single pairing.
"""

import os

# The fortune is built from its two beats: the oracular setup, whose "green"
# means candles, and the button, where "green" turns out to be a salad and
# the liquidation is named outright.
SETUP = "The oracle sees green in your future: a small salad, glowing with health"
BUTTON = "all the liquidation left you."


def build_fortune() -> str:
    return f"{SETUP}—{BUTTON}"


def main() -> None:
    fortune = build_fortune()
    # Gate self-check: UTF-8 text of 1–160 characters, and the brief's cap
    # of 20 words (whitespace tokens — the closed em dash keeps this at 17).
    assert 1 <= len(fortune) <= 160, "entry must be 1-160 characters"
    assert len(fortune.split()) <= 20, "entry must be at most 20 words"
    assert fortune.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(fortune)
    print(fortune)


if __name__ == "__main__":
    main()
