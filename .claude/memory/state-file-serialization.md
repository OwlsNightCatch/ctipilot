---
name: state-file-serialization
description: Canonical JSON serialization for sources.json to avoid full-file churn diffs
type: project
---

# State-file serialization — sources.json canonical format

**Fact (re-ratified 2026-07-18):** `sources/sources.json` is committed with **`indent=2, ensure_ascii=False`** — two-space indentation and literal UTF-8 (em-dashes `—` are NOT escaped to `—`).

**History of the flip:** the 2026-07-06 canonical was `indent=1`; the **2026-07-17T0409Z run re-serialized with `indent=2`** against this note (the full-churn defect this file exists to prevent — it reached `main` unflagged), and the 07-18 run committed on top. With two runs of history on indent=2, flipping back would just churn again, so **indent=2 is the canonical format from 2026-07-18 onward**. A 2026-07-18 session edit that trusted this note's old `indent=1` reproduced the ~6700-line churn locally (caught by `git diff --stat` before commit, redone at indent=2 → 9-line diff). **Lesson: check `head -5 sources/sources.json` for the live indentation before dumping, and verify with `git diff --stat` after — every time.**

**Why it matters:** if a run re-serializes it with a different indent or `ensure_ascii=True`, **every line flips** and the commit shows a ~6700-line diff even when only a handful of `last_successful_fetch` values changed. This has happened on prior runs (e.g. the diff on c4980f7 and the weekly before it), making review impossible and oscillating the file's format between fires.

**The fix — always bump/edit in place with the canonical dump:**
```python
import json
raw = open('sources/sources.json', encoding='utf-8').read()
d = json.loads(raw)
# ... mutate records (bump last_successful_fetch, reset counters, append notes) ...
d['last_updated'] = '<run-date>'
out = json.dumps(d, indent=2, ensure_ascii=False)
if raw.endswith('\n'):
    out += '\n'   # preserve the single trailing newline
open('sources/sources.json', 'w', encoding='utf-8').write(out)
```
Verify with `git diff --stat sources/sources.json` — a correct bookkeeping bump touches only ~15–35 lines, never the whole file.

**Notes discipline (unchanged):** `notes` is append-only — append a `| YYYY-MM-DD ...` clause, never rewrite prior audit clauses.

**`state/source_health.json`** is regenerated wholesale by `tools/source_health.py` itself; its large diff each run is the tool's own output and is expected — not something a run should hand-normalize.

## 2026-08-06 — the note's stated canonical was stale; the *procedure* is what holds

**Live format on `main` at 2026-08-06 is `indent=1`, not `indent=2`.** Verified with
`git show <sha>:sources/sources.json | head -3 | cat -A` on the pre-run commit: `{$` then
` "categories": {$` — one space. `state/cves_seen.json` is the same. The 2026-07-18
paragraph above declaring indent=2 canonical "from 2026-07-18 onward" no longer describes
the files; something flipped them back and this note was never corrected.

The 2026-08-06 run dumped both files at `indent=1, ensure_ascii=False, sort_keys=True` and
got 92- and 169-line diffs — the real changes only, no churn. That was luck, not care: the
run did not check first. Had it trusted this file's stated fact and used indent=2, it would
have flipped every line of both files.

**Therefore: do not trust any indent value written in this file, including this paragraph.**
The only reliable instruction here is the procedure, which has now survived two format
flips: `head -3 <file> | cat -A` before dumping, match what you see, `git diff --stat`
after. A stale fact in memory is worse than no fact, because it is trusted.
