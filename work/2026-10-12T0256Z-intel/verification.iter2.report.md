**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-12T03:35:59Z · ended_at=2026-10-12T03:40:12Z · duration_seconds=253

## Verification report — 2026-10-12T0256Z-intel (iteration 2)

Scope: full pass over `entries/2026-10-12/cve-2026-85097-bricksforge-pro-forms-upload-php-exploited.md` (33 of 33 ledger claims, one row each in `verification.iter2.claims.yaml`) and the run record. All four cited pages were fetched this pass with `extract` (Patchstack, Bricksforge changelog, Dr. Web, Previdian); the CVE record, FIRST EPSS API and CISA KEV catalogue were read directly.

### Prior-iteration deltas (all 11 checked against the fetched pages)

1. F3 Wordfence "assigner": fixed. Dr. Web: "CVSS 3.1: 9,8, vergeben von Wordfence; Patchstack vergibt 10,0"; the body now says "credits Wordfence ... 9.8 and Patchstack with 10.0". sourcing_note is two sentences, CVSS sentence gone. OK.
2. F3 Exposure adjacency: fixed. The 3.1.8.9 bound is cited to Patchstack ("Affected Versions | ≤ 3.1.8.9"); the no-upload-field clause to the changelog (verbatim). OK.
3. F14 "none of the cited sources": reworded under Patchstack's name, but Patchstack's page still does not carry the negative. See F14 below (new finding on the remediated text).
4. F4 run-record CISA ADP timing: fixed. CVE record ADP SSVC timestamp 2026-10-08T14:24:30Z; Patchstack datePublished 2026-10-08T11:28:37; "about three hours after" is right. OK.
5. F5 uncited sentences: fixed, both now carry Patchstack citations that support them (affected versions; 21:47 UTC, 63 unique IPs, automated, no attribution). OK.
6. F9 version 4.0.0: fixed. Changelog: 4.0.0 of 17 September 2026, 4.0.1 of 8 October 2026 carries the upload fix, no affected range anywhere, 4.0.0 "Includes all hardening and fixes from the 3.x line". The Exposure sentence states exactly that uncertainty. OK.
7. F8 public exploit: fixed. Previdian page: "Exploit status | PoC available"; evidence quote verbatim; Previdian is cited, the repository is not. A public repository for this CVE does exist (GitHub search, 1 result, created 2026-10-10), so `poc-public` is true. OK.
8. F8 VulnCheck KEV: wording now "Among the cited sources, Patchstack is the only observer"; accurate on the cited set. OK.
9. F8 endpoint names: Detection now names `/wp-json/bricksforge/v1/form_submit` and the admin-ajax `bricksforge_form_submit` action; both on Patchstack's page. OK.
10. F18: actions[] is one inventory-and-update task; concrete, derived from this finding, not hedged. OK.
11. F11 Triage line dropped (confirmed absent); sourcing_note two sentences (confirmed); run-record `completed` stamp still a placeholder (see advisory).

### Unsupported / hallucinated facts and quantifiers

### Quantifier without source

- F14 #1: `2026-10-12/cve-2026-85097-bricksforge-pro-forms-upload-php-exploited`, paragraph 2: "Patchstack describes exploitation attempts, reports no confirmed compromise, and says an attacker with execution can deploy web shells ([Patchstack, 2026-10-08](https://patchstack.com/articles/critical-unauthenticated-arbitrary-file-upload-vulnerability-exploited-in-bricksforge-plugin/))". The Patchstack page says "Our telemetry shows active exploitation attempts targeting Bricksforge installations" and, in its table, "Exploitation Status | Active exploitation observed"; it contains no statement about confirmed or unconfirmed compromise. The clause attributes an absence-of-compromise report to Patchstack that the page does not make, and Dr. Web's lead ("Seit Mittwochnacht schleusen Angreifer über das Formularmodul ... eigenen PHP-Code auf fremde Server") reads stronger than "attempts". Fix: "Patchstack describes exploitation attempts and does not report a confirmed compromise", or drop the clause. The web-shell half of the sentence is supported.

### Editorial / less-is-more flags (advisory)

- F11 #2 (low confidence): summary reads "has been exploited since 2026-10-07: an attacker with no account gets a PHP file written to the uploads directory and executed". Patchstack's own status line ("Active exploitation observed") supports "exploited", but the colon clause reads as confirmed successful execution while the body says attempts and no confirmed compromise. If the F14 clause stays, align the summary wording.
- F11 #3 (low confidence, already noted by the main agent as provisional): run record `completed: '2026-10-12T03:50:00Z'` is later than the container clock at this pass (03:40Z); `duration_seconds: 3235` derives from it; `verification_iterations: 0` and `publish_status: pending` are provisional. Restamp in Phase 6.

### Checks that came back clean

- Source URLs: all four resolve to specific articles/pages; dates match (Patchstack 2026-10-08, changelog 4.0.1 dateline 8 October 2026, Dr. Web 2026-10-09, Previdian 2026-10-08).
- Evidence quotes: 5 of 5 verbatim (the two German originals checked character for character against the Dr. Web page; translations faithful).
- cves[]: id, CVSS 9.8 (CNA record, Dr. Web) with Patchstack's 10.0 surfaced in the body; EPSS 0.0031 equals FIRST 0.00312; affected/fixed as sourced.
- Dedup: no prior entry or prior-coverage record carries CVE-2026-85097 or Bricksforge; the only `cves_seen.json` row is this run's own. The 2026-10-11 S1 note ("outside its slice and absent from the store") matches the run record's claim.
- Frontmatter: classification B/2 (Patchstack reliability B in sources.json; single research-lab source with consistent vendor and press echo); verification `single-source` with a two-sentence provenance note; no org_triage; no watchlist; techniques T1190, T1505.003, T1036.008 each map to a described behavior; no IOCs, no em dashes, no workflow vocabulary in reader-facing text.
- Priority `notable`: exploited pre-auth upload-to-RCE with vendor fix, no shown constituency deployment; critical/high bars not met, calibration defensible.
- Run record: sub-agent counts (3+0+1+3 = 7), window arithmetic, the 81 rotation figure (27+24+30), backlog rows (four open rows, expiries 2026-10-14/2026-10-20) and the single-source note all match files on disk.
- Coverage: KEV catalogue 2026.10.08, no addition in window and no CVE-2026-85097; web searches for exploited flaws dated 11-12 October and for Swiss public-sector incidents surfaced nothing in-window beyond what the run already covered or dropped (FortiMail CVE-2026-104286 and Cisco SD-WAN CVE-2026-76504 are already in the store). Coverage looks complete for a quiet Monday window.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 2)

### Findings summary (machine-readable)

See `work/2026-10-12T0256Z-intel/verification.iter2.findings.yaml` (3 records: F14, F11, F11).
