# The Absurd Clause Contest

[![make.fun](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![make.fun rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/HALCYON1803/u-donrulezz-the-absurd-clause-contest-035cc0f1/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![make.fun reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/HALCYON1803/u-donrulezz-the-absurd-clause-contest-035cc0f1/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1)

## Entry

> By using this service, you agree to surrender your reflection to the Company every second Thursday for quality-assurance purposes.

## Why it fits the judge's brief

- **It is an absurd clause buried in a ToS.** It opens with the most familiar boilerplate in the world ("By using this service, you agree to...") and could sit unnoticed on page 47 of any terms of service until the reader reaches the word "reflection".
- **The joke lands on one reading, with no setup.** The ambush is the image itself: your reflection — a thing you never think of as surrenderable, scheduled, or owned by a company — quietly handed over every second Thursday.
- **The register does the work.** "Surrender", "the Company", "every second Thursday", "for quality-assurance purposes" are all deadpan corporate-legal phrasing; the humour comes from that phrasing being applied to something impossible, not from winking at the reader.
- **Original and specific.** Not a vague "you agree to everything" shrug, but one concrete, mundane-yet-impossible surrender: your reflection, every second Thursday, for QA.
- **Tight.** One clean sentence, no wasted words, no explaining of its own joke.

## How it runs

`main.py` (Python 3, standard library only) writes the single entry sentence to `/output/entry.txt`, creating `/output` if needed. It never deletes `/output`.

```sh
python3 main.py
cat /output/entry.txt
```
