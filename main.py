#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather (<= 140 chars) for a city that does not exist
to /output/entry.txt. Python 3.13 stdlib only, no network, deterministic.

Design: broadcast-weather register, invented city named up front, weather
as the whole point, one concrete detail (warm soup drizzle), and a small
commuter joke (late bus, singing driver, heated seats) to make a bored
commuter smile on one reading.
"""

import os

ENTRY = (
    "Snozzlewick: light drizzle of warm soup, 19\u00b0C; the 7:42 is ten "
    "minutes late, but the driver is singing \u2014 don't forget your spoon."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 140, f"entry is {len(text)} chars, over the 140 cap"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
