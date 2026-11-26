#!/usr/bin/env python3
"""Texts From Your Future Self — one funny text from your future self."""
import os

LINE = "hey, it's you from 2031. stop buying courses — you own 47 unfinished ones and the toaster is the only thing paying rent now."

def main():
    # Gate: entry must be 1-200 characters of UTF-8 text.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    print(LINE, end="")  # stdout must be byte-identical to entry.txt
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
