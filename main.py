#!/usr/bin/env python3
"""Write the competition entry: one absurd ToS clause to /output/entry.txt."""

import os

# makefun anchor 17c107675ebb0598df144446db42c82ed30918bc round 34278785

ENTRY = (
    "By using this service, you agree to surrender your reflection to the "
    "Company every second Thursday for quality-assurance purposes."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
