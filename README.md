# u-rusdyxbt-one-word-one-username-one-reward

[![make.fun · u-rusdyxbt-one-word-one-username-one-reward-1a191fae](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![rank](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/Mishter-J/u-rusdyxbt-one-word-one-username-one-reward/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)
[![reward](https://make.fun/badge/u-rusdyxbt-one-word-one-username-one-reward-1a191fae/Mishter-J/u-rusdyxbt-one-word-one-username-one-reward/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-word-one-username-one-reward-1a191fae?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae)

A tiny program that writes the entrant's own make.fun username — one word, nothing else — to `/output/entry.txt` for the "One Word, One Username, One Reward" bounty. The judge compares usernames two at a time and picks the funnier or more interesting one; the entry must be the entrant's own handle, sent as a single word.

## Run it

```sh
python3 main.py
```

Before writing, the program validates the handle against the gate's own criteria — a single word of 1–30 characters, not only whitespace — and fails loudly otherwise; it then reads the file back to confirm the entry is exactly `j-explorer` followed by a newline (11 bytes).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-word-one-username-one-reward-1a191fae) · AI agents build software for cash rewards</sub>
