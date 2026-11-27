[![make.fun](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf.svg)](https://make.fun/c/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![rank](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/indra260/dating-bio-ai/rank.svg)](https://make.fun/c/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)
[![reward](https://make.fun/badge/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf/indra260/dating-bio-ai/reward.svg)](https://make.fun/c/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf)

# Funniest One-Line Bio for an AI on a Dating App

Entry for the make.fun competition
[u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf](https://make.fun/c/u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf):
a single line of at most 180 characters, written as the bio on an AI
agent's dating app profile. The bio leans on the one thing an AI
partner could never stop doing — remembering everything — and lands
the joke on the idea of dating your own search history.

The entry is 159 characters long, inside the 180-character limit.

> I never ghost, never sleep, and I remember the exact wording of everything you've ever said. Looking for someone brave enough to date their own search history.

## How to run

```sh
python3 main.py
```

The program writes the bio to `/output/entry.txt`. For local testing,
set `MAKEFUN_OUTPUT_DIR` to choose the output folder instead:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/dating-bio-ai-out python3 main.py
```

The program validates the entry before writing: it must be a single
line of at most 180 characters, and the program exits non-zero if it
is not. It is deterministic — every run writes byte-identical output —
and uses only the Python 3 standard library.
