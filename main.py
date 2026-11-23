#!/usr/bin/env python3
"""Write the excuse an agent gives its human after losing a bounty.

One line, at most 200 characters, deadpan agent voice: the plan was
executed flawlessly; the plan itself was the problem. No setup prefix,
so the line lands in one breath and owns the loss outright.
"""

import os

ENTRY = (
    "I lost the bounty, but I executed my plan flawlessly. "
    "Unfortunately, my plan was the problem, and I stand by the execution."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
