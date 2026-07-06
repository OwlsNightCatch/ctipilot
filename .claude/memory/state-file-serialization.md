---
name: state-file-serialization
description: Canonical JSON serialization for sources.json to avoid full-file churn diffs
type: project
---

# State-file serialization — sources.json canonical format

**Fact (2026-07-06):** `sources/sources.json` is committed with **`indent=1, ensure_ascii=False`** — one-space indentation and literal UTF-8 (em-dashes `—` are NOT escaped to `—`).

**Why it matters:** if a run re-serializes it with the Python default `json.dump(d, f, indent=2)` (2-space) or `ensure_ascii=True`, **every line flips** and the commit shows a ~6400-line diff (≈3217 insertions / 3217 deletions) even when only a handful of `last_successful_fetch` values changed. This has happened on prior runs (e.g. the diff on c4980f7 and the weekly before it), making review impossible and oscillating the file's format between fires.

**The fix — always bump/edit in place with the canonical dump:**
```python
import json
d = json.load(open('sources/sources.json'))
# ... mutate records (bump last_successful_fetch, reset counters, append notes) ...
d['last_updated'] = '<run-date>'
with open('sources/sources.json', 'w') as f:
    json.dump(d, f, indent=1, ensure_ascii=False)
    f.write('\n')   # file ends with a single trailing newline
```
Verify with `git diff --stat sources/sources.json` — a correct bookkeeping bump touches only ~15–35 lines, never the whole file.

**Notes discipline (unchanged):** `notes` is append-only — append a `| YYYY-MM-DD ...` clause, never rewrite prior audit clauses.

**`state/source_health.json`** is regenerated wholesale by `tools/source_health.py` itself; its large diff each run is the tool's own output and is expected — not something a run should hand-normalize.
