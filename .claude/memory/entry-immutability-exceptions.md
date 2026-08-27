---
name: Entry immutability exceptions
description: Audit log of operator-authorized edits to published entries (normally NEVER allowed)
type: project
---

# Entry immutability exceptions

> **HISTORICAL — this ledger is retired (v4.0, operator directive 2026-08-27).** Entries are living records now: every change to a published entry is an `updates[]` changelog record (`correction` / `improvement` / `update`) with a matching `## <Type> — <at>` section on the entry itself — see [[entry-lifecycle-v4]] and `docs/pipeline.md` § Entry lifecycle. The changelog IS the ledger, so nothing is logged here any more. The v3-era entries below stay as the record of what was edited when entries were immutable.

Published entries were immutable in v3 — corrections shipped as new entries with `update_of`. This file was the audit log of the rare, operator-authorized exceptions, so a future session or verifier that noticed post-publication mtimes/commits on entry files knew they were sanctioned, not drift.

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

## 2026-07-11 — full-store intelligence audit: three metadata error repairs

**Authorization:** explicit operator directive (full-store quality audit session: "identify … reports that are false or have errors … Improve any findings you have. You can change and improve everything you seem fit").

**What changed (frontmatter metadata + one inline id — bodies otherwise untouched):**

- `2026-07-08/beyondtrust-rs-pra-preauth-bypass-cve-2026-40138-cluster`: `cves[]` CVE-2026-40141 `cvss: "9.9"` → `"8.5"`. The published 9.9 was a factual error that made a post-auth, limited-privilege resource-access flaw the *top-scored* CVE in the cluster, above the two pre-auth admin bypasses (9.2). Verified against the vendor advisory BT26-03 (bridge fetch: "CVE-2026-40141 | High | 8.5") and The Hacker News (8.5). The body never stated 9.9 — frontmatter-only defect, likely a transcription slip from the neighbouring 9.9-class advisories that day.
- `2026-07-10/odido-shinyhunters-vishing-dutch-police-attribution`: `techniques[]` `T1656` → `T1684.001` (T1656 Impersonation was revoked in ATT&CK v19, superseded by T1684.001 per the pinned dataset), plus the single inline `` `T1656` `` body mention updated to match. This cleared the standing `attack-mapping` WARN in `check_run.py --all`.
- `2026-07-09/talos-wolfssl-geovision-vtkdicom-disclosure`: three wolfSSL CVE ids corrected in `cves[]`, body prose, and `state/cves_seen.json` — CVE-2026-28739 → **CVE-2026-7532**, CVE-2026-25106 → **CVE-2026-5263**, CVE-2026-33091 → **CVE-2026-6678**. The published ids resolve nowhere (NVD "CVE ID Not Found"); the corrected ids come from Talos's own per-advisory "Vendor Response (CVE-…)" fields (TALOS-2026-2409 / -2410 / -2408, each bridge-fetched and confirmed). Root cause: the cited Talos *roundup blog* printed ids contradicting Talos's own advisory pages, and the two-source rule could not catch a single-publisher self-contradiction. The vulnerability descriptions, CVSS values, and all GeoVision/VTK-DICOM ids were verified correct — only the three wolfSSL identifiers changed.

Root-cause and prevention for both are in the audit report `docs/audits/2026-07-11-intelligence-quality-audit.md`: composer-side CVSS transcription needs the verifier's F-check to compare frontmatter scores against the cited advisory, and revoked ATT&CK ids in a new run's `techniques[]` are upgraded from WARN to FAIL (v3.21 gate).

## 2026-08-02 weekly quality audit: two unsupported ATT&CK ids removed

**Authorization:** the scheduled weekly quality audit's standing repair class (`prompts/quality-audit.md` Phase 4, "factual metadata errors that poison machine surfaces … wrong/unresolvable CVE id, wrong CVSS, **dead ATT&CK id**, wrong registry key"). Same class as the 2026-07-11 Odido `T1656` repair: a `techniques[]` id that does not belong, corrected in place because the mapping feeds the `/attack/` overlap matrix, the entity and CVE TTP profiles and the Navigator-layer exports, all of which are machine surfaces a reader never sees being wrong.

**What changed (frontmatter `techniques[]` only — bodies, sources, all other keys untouched):**

| Entry | old `techniques[]` | new | Why |
|---|---|---|---|
| `2026-07-26/ifage-geneva-dragonforce-data-published-student-records` | `[T1657, T1567.002]` | `[T1657]` | Truth pass B1 (Opus). T1567.002 (Exfiltration to Cloud Storage) names a behaviour no cited source describes — the entry's own body says "Nothing in the reporting identifies the initial-access vector" and the only described attacker action is leak-site publication |
| `2026-07-31/exfilsquad-uk-department-for-education-pnld-breach` | `[T1213, T1190]` | `[T1213]` | Truth passes B4 (Sonnet) and the audit's own re-read. T1190 asserts an exploitation vector neither cited source states; The Record reports only that the portals "were impacted" |

Both entries retain a source-supported mapping after removal, so neither trips the non-empty requirement on `incident`-kind entries. Both defects were reported `machine_surface: true` by their truth passes.

**Root cause and the fix that shipped with it (v3.30).** `techniques[]` is required to be non-empty on `threat`/`incident`/`vulnerability` and is described as the *complete* mapping surface. Both pressures push toward adding an id and nothing pushed back, so an entry whose sources never state the access vector acquired one. v3.30 adds the missing counterweight to `prompts/cti-run.md` § Triage-ready behavioral description: when the cited sources do not state how access was obtained, the entry does not map an access vector, and if the honest mapping for a behaviour-kind entry would be empty, fix the entry rather than the mapping. Full report: `docs/audits/2026-08-02-weekly-quality-audit.md`.

**Deliberately NOT repaired in the same audit, and worth knowing why** — three metadata defects that would poison a machine surface but fall outside the enumerated class: `2026-07-26/joomla-gridbox-…` records CVE-2026-62415 as `cves[].type: rce` where the discloser states the shipped-default impact is constrained anonymous file writes and "not a web shell"; the same entry's `sourcing_note` calls a CVSS 3.1 score "CVSS 4.0"; and `2026-07-24/mz-automation-…` still carries five `fixed: "not stated in advisory"` values its advisory's CSAF contradicts (carried from the 2026-07-26 audit). `cves[].type`, `cves[].fixed` and `cves[].affected` are not in the carve-out, and widening an immutability carve-out is an operator decision, not the audit's — it is recommendation 3 in both reports.
