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

## 2026-07-11 — repair of migration-era `entities:` link pollution (201 entries, frontmatter lists only)

**Authorization:** explicit operator directive ("Review all the entities in detail and ensure that all their links and relationships are correct and true and complete"), prompted by the nonsensical entity page for `incident:ncsc-ch-booking-hotel-phishing-2026` (67 linked entries, 65 unrelated).

**Root cause (v3.0 migration, commit `b4885f0`):** `tools/migrate_briefs.py` derived entity names by truncating v2 titles at the first colon, so several entities were literally *named after the reporting organization* — `NCSC-CH`, `Check Point`, `SentinelOne`, `Symantec`, `Sophos X-Ops`, `Google Threat Intelligence Group` — and `link_entities()` then linked those entities into every migrated entry whose text merely cited that organization. The 2026-07-09 registry overhaul fixed the registry *names* but could not touch the already-written entry frontmatter, so the false links persisted. Conversely, entities whose migration name was a long headline sentence matched nothing, so their own anchor entries carried no link (e.g. `campaign:trapdoor` and `tool:beagle-fake-claude-stac4713-2026` had **zero** referencing entries).

**What changed (frontmatter `entities:` lists only — bodies, sources, all other keys byte-identical, verified by round-trip assertion):**

- **122 false links removed** across 7 entities, keep-lists verified manually against each entry's cited reporting: `incident:ncsc-ch-booking-hotel-phishing-2026` (−65, keeps its 2 booking entries), `campaign:tds-security-tool-impersonation-checkpoint` (−29, keeps the 2026-06-10 TDS anchor), `campaign:sentinelone-living-off-the-pipeline-2026` (−8), `report:gtig-europe-2025` (−6), `actor:embargo` (−6 — "broke embargo"/"90-day embargo" disclosure prose, keeps 3 real ransomware-group mentions), `campaign:underground-ai-adoption-sophos` (−4), `campaign:stock-exchange-mailbox-espionage-2026` (−4).
- **103 missing links added**, gated to entities named verbatim in the entry **title** (current registry name/alias, whole-word, generic org tokens excluded) plus one manual body-supported case (2026-06-01 booking weekly += `incident:dutch-hotels-booking-saas-breach-2026`).

All changes were generated by one deterministic script (session scratchpad `fix_entities.py`); post-repair `check_run.py --all` green (19 pass · 1 pre-existing warn · 0 fail), `site/build.py` + `site/test_build.py` green. Post-migration (non-`migrated_from`) entries needed **zero** corrections — the pollution was 100 % migration-era; the composer-side linking discipline in the prompts is working.

**Detection recipe for future audits:** diff the registry at the suspect commit vs now; refs that match only a *renamed-away* generic name (and not the current name/aliases/distinctive key tokens in title+summary+body — exclude the frontmatter itself, the key slug matches its own tokens) are the pollution set. Common-word entity names (`Embargo`) need per-mention context review.
