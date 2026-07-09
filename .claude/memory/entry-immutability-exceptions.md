---
name: Entry immutability exceptions
description: Audit log of operator-authorized edits to published entries (normally NEVER allowed)
type: project
---

# Entry immutability exceptions

Published entries are immutable — corrections ship as new entries with `update_of`. This file is the audit log of the rare, operator-authorized exceptions, so a future session or verifier that notices post-publication mtimes/commits on entry files knows they were sanctioned, not drift.

## 2026-07-09 — repair of the four v2→v3 migration dangling `update_of` links

**Authorization:** explicit operator directive ("Exceptionally fix these 4 warnings"), following the v3.14 grandfathering change that had downgraded them from permanent FAIL to WARN.

**Why they dangled:** both targets were v2 brief-item keys whose items never became v3 entry files in the migration (commit `4174621`):

- `2026-05-10/pcpjack-modular-cloud-credential-theft-worm-displaces-teampc` — the daily 2026-05-10 PCPJack research item was deduped away in migration; its surviving representation is the W19 weekly synthesis entry `2026-05-04/teampcp-pcpjack-cloud-worm-successor-evicting-prior-operator` (same SentinelLabs primary, cites the 05-10 daily).
- `2026-06-19/icarus-extortion-group-turns-a-dormant-klue-credential-into` — the daily 2026-06-19 Icarus/Klue root item was never migrated; the earliest surviving Klue entry is `2026-06-21/klue-oauth-token-breach-victim-list-grows-crm-api-abuse-chai`.

**What changed (frontmatter `update_of` only — bodies, sources, ids untouched):**

| Entry | old `update_of` | new `update_of` |
|---|---|---|
| `2026-05-13/mini-shai-hulud-teampcp-worm-hits-tanstack-uipath-mistral-ai` | `2026-05-10/pcpjack-…` | `2026-05-04/teampcp-pcpjack-cloud-worm-successor-evicting-prior-operator` |
| `2026-06-21/klue-oauth-token-breach-victim-list-grows-crm-api-abuse-chai` | `2026-06-19/icarus-…` | `null` (it is now the chain root — no earlier Klue entry survived migration) |
| `2026-06-24/8x8-confirms-klue-icarus-salesforce-exfiltration-in-an-sec-8` | `2026-06-19/icarus-…` | `2026-06-21/klue-oauth-token-breach-victim-list-grows-crm-api-abuse-chai` |
| `2026-06-25/klue-icarus-salesforce-oauth-breach-beyondtrust-and-lastpass` | `2026-06-19/icarus-…` | `2026-06-21/klue-oauth-token-breach-victim-list-grows-crm-api-abuse-chai` |

Resulting Klue chain: 06-27 → 06-25 → 06-21 (root); 06-23 → 06-21; 06-24 → 06-21. Acyclic, all targets resolve. `check_run.py --all` is now 14 pass · 0 warn · 0 fail.

**Body text saying "originally covered 2026-06-19 / 2026-05-10"** stays accurate — those dates refer to the v2 daily briefs, which did cover the items; only the v3 entry files are missing.

**This does not weaken the invariant.** The grandfathering severity split in `check_run.py` `check_references_resolve` stays (committed+dangling = WARN, uncommitted+dangling = FAIL) as the general mechanism. Any future edit to a published entry still requires an explicit operator directive and a log entry here.
