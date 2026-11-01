**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-01T15:07:54Z · ended_at=2026-11-01T15:24:53Z · duration_seconds=1019

## Verification report — 2026-11-01T1312Z-audit (iteration 3)

Scope: post-fix pass. Ledger `claims.iter3.yaml` (242 claims) and `claims.changed.iter3.yaml` (2). In scope and answered: 117 (both changed claims; every other claim of the five entries remediated after iteration 2, GhostAction 21, Ivanti 10, Adobe Campaign Classic 21, Canton Bern 13, Linux CVE-2026-98432 11; and a seeded random quarter, 41, of the 166 remaining claims across 13 other entries). Verdict rows: 117 ok, 0 F3/F4/F5/F13/F14, 0 unreadable. Gate: `python3 tools/check_run.py 2026-11-01T1312Z-audit` ran this iteration, 58 pass · 0 warn · 0 fail.

Sources read this iteration (fresh `extract`, raw HTML, pdf or API): GitGuardian (both GhostAction posts), StepSecurity, Socket, Rapid7 (Ivanti, GitLab, October Patch Tuesday), Volexity, Canadian Cyber Centre AV26-1035, CISA alert for Ivanti (WebFetch), GHSA-fhw5-mpvj-x89m, Adobe APSB26-162 (raw HTML, per-CVE vectors), APSB26-142, APSB26-134, CISA KEV catalog 2026.10.30 (cisa-kev), KAIO Bern ICSG page, headtopics (Berner Zeitung relay), CIQ article, Red Hat CVE page and its security-data JSON, Ubuntu tracker, Debian tracker, Openwall linux-cve-announce, Dream Research, Wiz, Broadcom VMSA-2026-0006.2 and umbrella 39404, Infosecurity Magazine, THN, mySites.guru (three posts), Balbooa 2.20.2, Zscaler, Datadog, Node.js (raw), ELLIO, Palo Alto CVE-2026-111497 and CVE-2026-109618, NCSC.ch post 13105, MSRC SUG API (vulnerability, affectedProduct), Morphisec, Siemens SSA-566512, Belden PSIRT-10 (pdf), Python Insider, CrowdStrike, Wordfence Intelligence, jina-usage.

Prior-iteration deltas, each re-read at the source:
- GhostAction (F4, stray Socket `source_url`): all 24 changed entries parse with a duplicate-key-strict YAML loader; the `evidence[]` of GhostAction has one `source_url` per record, and each quote is on its page (StepSecurity three quotes, GitGuardian four, none attributed to Socket; the removed Socket quote is still on Socket's page, the approval-gate quote is not).
- Ivanti Exposure: "No cited source says which chain CVE each fixed build closes." Rapid7 tables resolved builds for CVE-2026-104935 only; the Canadian Cyber Centre and CISA give affected ranges without per-CVE fixed builds; Ivanti's advisory is unread. The sentence holds (it hedges, and agrees with `cves[].fixed`).
- Run record Scope: "six developments on covered findings" now agrees with the notes and the report (six: GhostAction, Node2Shell detection and decoys, Canton Bern, Edge, Morphisec, Adobe APSB26-162).
- Adobe Campaign Classic KEV statement: the 2026.10.30 catalog (dateReleased 2026-10-30T17:02Z) lists none of the 29 CVEs of APSB26-134, -142 and -162; the 2026-10-30 KEV source record exists and `sources` is in the record's `fields`. APSB26-162 table re-read: eight CVEs, CVE-2026-105781 CVSS 9.8 PR:N/UI:N, four 9.9 PR:L, CVE-2026-104350 9.3 PR:N/UI:R, CVE-2026-104354 9.1 PR:H, CVE-2026-105779 9.1 PR:L, build 9402 and earlier affected, 9403 fixed, "not aware of any exploits"; the frontmatter `cves[]` rows match one for one.
- Canton Bern, Linux 98432, report G2: the narration sentence is gone from the section; the title says "Debian and most CIQ kernels" (CIQ: five variants patched, LTS 8.10 and RLC Pro 10 not); the report says G2 12.

Whole-run checks that hold on disk: 24 entries, one record each from this run (7 update, 13 correction, 4 improvement, 7 internal); `updated_at` equals `at` on all 7 updates and is untouched elsewhere; no priority or classification change; `cves_seen` 9 added and 54 bumped; one registry record added; ten KEV additions all covered; priority table (store 1,052: 30/376/588/58; October 117: 6/22/81/8; September row is the figure quoted from the 2026-10-11 report); sources changes (gitguardian added, 13 notes, sans-isc scope); jina pool 6 of 10, 46.83 M; truth-pass batch sums (54 entries, 30/22/2, 1,651 claims); three page-check leads and four out-of-scope warnings; no em dash and no workflow vocabulary in the added reader-facing lines.

### Claims missing inline citation / Unsupported / Citation does not support
None found in the changed text.

### Missed angles
None. The week's exploited and KEV set is covered per `kev-window.txt`; a web check surfaced no in-window exploited edge flaw the store lacks (FortiMail CVE-2026-104286, NetScaler CVE-2026-88779 and Chrome CVE-2026-11645 are older entries). Sophos UTM CVE-2026-118633 stays a defensible recorded borderline drop.

### Editorial / less-is-more flags (advisory)
- #1 (F11, pre-existing, low confidence) GitLab Exposure and takeaway: "on instances where new users can self-register and create projects that constraint is removed ([Rapid7])". Rapid7: "an ordinary account can satisfy this prerequisite by creating a public project on a self-managed GitLab instance where that functionality is permitted"; no mention of self-registration. Carried from iteration 2 #7.
- #2 (F11, pre-existing, low confidence) Linux CVE-2026-46300, 2026-10-29 section: the Dream page (dateline "Updated: October 29, 2026") is labelled 2026-10-27 once and 2026-10-29 elsewhere. Carried from iteration 2 #8.
- #3 (F11, low confidence) Canton Bern: the summary says Grundschutz BE "follows in the first quarter of 2027"; KAIO says "tritt voraussichtlich im ersten Quartal 2027 in Kraft" and the section keeps the hedge. The record summary ends "The communes' scope is stated as KAIO words it." (awkward edit narration), and the body says KAIO "had still not published on 2026-11-01" while the page carries a 2026-10-30 dateline.
- #4 (F11, low confidence) GhostAction summary: "with the same unrevoked tokens"; GitGuardian counts 1,382 of 1,792 accounts as already used on 8 October, and the body and record summary say "mostly".
- #5 (F11, low confidence) Linux 98432: "CIQ, 2026-10-31" (page dateline 2026-10-30, status "as of 2026-11-01", kernels built 2026-10-31) and "Red Hat, 2026-10-31" (page dateline 2026-10-15, no update date) are read or build dates rather than the pages' own.
- #6 (F11, low confidence) Adobe: the "as of its 2026-10-30 catalog" KEV statement is true and sourced but appears only in the summary; the body keeps the 2026-10-01 dating for APSB26-142 and the new section is silent on KEV.
- #7 (F11, low confidence) Broadcom PHP2Shell Correction section opens with "The takeaway said CloudSOC SpanVA and CASMA have no fix."; a correction must name what it corrects, so this may stay.

### Verdict
CLEAN (truth: 0, editorial: 0, advisory: 7)

### Findings summary (machine-readable)
See `work/2026-11-01T1312Z-audit/verification.iter3.findings.yaml` (7 records, all F11 advisory).
