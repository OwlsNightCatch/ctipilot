---
name: state-file-serialization
description: Derive JSON serialization format from the live file before dumping — the stated canonical has flipped twice; only the procedure holds
type: project
---

# State-file serialization — the procedure, not a constant

A re-dump of `sources/sources.json` / `state/cves_seen.json` with the wrong `indent`/`ensure_ascii` flips every line (~6700-line churn diff). The canonical format has flipped at least twice on `main`, so **never trust a remembered constant — derive it from the live file every time**:

1. `head -3 <file> | cat -A` — read the indentation; check the last byte for a trailing newline; check whether non-ASCII is escaped.
2. Load, mutate in place (bump `last_successful_fetch`, append notes), dump matching what you saw.
3. `git diff --stat <file>` — a bookkeeping bump touches tens of lines, never the whole file. Whole-file churn ⇒ redump with the right flags. (A 2026-08-28 session caught an 8510-line churn this way and redumped to 8 lines.)

`notes` is append-only (`| YYYY-MM-DD …`). `state/source_health.json` is regenerated wholesale by its tool — a large diff there is expected.
