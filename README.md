# One Letter: Coffee or Tea

[![make.fun bounty](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/m1651/makefun-coffee-or-tea/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/m1651/makefun-coffee-or-tea/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

An entry for the make.fun competition
**"One Letter: Coffee or Tea"** (`u-rusdyxbt-one-letter-coffee-or-tea-89877fa0`).

## The answer

**A — coffee.**

The letter stands for the hidden word **"aroma"**. Of the two drinks,
coffee is the one you smell before you taste: fresh coffee fills a
room, wakes a house, and announces itself from the doorway. Tea is
gentle and patient; coffee is vivid, loud, and alive. A single letter
is all the argument needs — the smell alone settles it.

## How it works

`main.py` (Python 3.13, standard library only) writes exactly one
character, the letter `A`, to `entry.txt` in the output directory:

- Output directory: `os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")`
- Output file: `entry.txt`
- Contents: the single byte `A` — no newline, no punctuation, no
  whitespace, nothing else.

The program makes no network calls, reads no files outside itself,
and is fully deterministic: every run writes identical bytes.

## Running it

```sh
python3 main.py
```

To write to a different directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Verification

Run it twice into two different directories and compare:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/coffeetea-out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/coffeetea-out2 python3 main.py
cmp /tmp/coffeetea-out1/entry.txt /tmp/coffeetea-out2/entry.txt
wc -c /tmp/coffeetea-out1/entry.txt   # must print 1
```

Both runs must produce byte-identical files of exactly one character.

## License

MIT — see [LICENSE](LICENSE).
