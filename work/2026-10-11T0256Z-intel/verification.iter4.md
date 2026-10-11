**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-11T04:17:42Z · ended_at=2026-10-11T04:28:46Z · duration_seconds=664

## Verification report — 2026-10-11T0256Z-intel (iteration 4)

Role: confirmation pass (iteration 3 returned CLEAN; no deltas block). Read cold. Scope: all 112 claims of `claims.iter4.yaml` (all 112 walked, every one has a verdict row in `verification.iter4.claims.yaml`), the 3 new entries, the 2 updated entries (whole entry plus `git diff HEAD`), the run record, `entities/registry.yaml` diff, `sources/sources.json` diff, `state/coverage_backlog.md` diff.

Method: all 21 cited URLs re-fetched live this iteration with `tools/fetch_source.py extract` (all resolve, all specific article pages, 18 of 19 saved gate bodies byte-identical to the live fetch, the DR live blog differs only in markup and still carries every cited line). The Let's Encrypt forum thread was read from the gate's saved page (its og:description and JSON-LD carry the quoted sentence, the staff user title and datePublished 2026-10-07). CISA KEV re-fetched with `cisa-kev`: catalogVersion 2026.10.08, newest dateAdded 2026-10-08 (five old-CVE additions, all already carried by `2026-10-09/aa26-281a-...`), so the run record's "no KEV addition in the window" holds.

### Changelog contract (4c) — both updated entries
- `2026-08-06/chaindrop-...` record 2026-10-11T03:39:00Z (type update): `updated_at` mirrors `at`; section `## Update — 2026-10-11T03:39:00Z` present and inline-cited; every field named in the record (actions, evidence, sources, sourcing_note, summary, techniques, body) matches a diff hunk and nothing else changed; the record summary equals what the section states (tensorlake@0.5.144, Endor provenance, Socket and OX dead-man switch and remove-before-revoke, Socket-versus-OX attribution split). Supersession sweep: the old "unconfirmed claim from one vendor" paragraph was rewritten in place, actions[1] now carries the tensorlake scope, summary extended; no residual statement contradicts the newest section. New evidence quotes (Endor, Socket) are verbatim. Added techniques (T1053.005, T1543.002, T1543.001, T1485, T1552.005) are each supported by Socket/OX text (ONLOGON scheduled task, systemd user unit, LaunchAgent, home-directory wipe, IMDS access).
- `2026-10-06/denmark-cpr-...` record 2026-10-11T03:40:00Z (type update): `updated_at` mirrors `at`; section present and inline-cited; record fields (title, headline, summary, techniques, sources, evidence, sourcing_note, body) match the diff; the `ufm.dk` URL is gone from the entry; the main-analysis sentence "No source names the company ..." was removed and the main analysis follows the new section; the minister's ten days and Ritzau's 21 days 17 hours are both stated and attributed (contradiction surfaced). Every claim in the new section checked against the Copenhagen Post (Ritzau), TV4 (TT) and the ministry release.

### New entries
- `cctld-registry-hijacks-gh-sl-as-...`: every clause checked against Google, The Hacker News and the Let's Encrypt forum thread; dates 2026-10-06 / 2026-10-08 / 2026-10-07 equal the pages' own dates; the Triage claim is correctly narrowed to google.com.gh, google.sl, google.as; revocation is limited to the Google certificates as Google words it; no IOCs, no em dash, no internal vocabulary. Classification B/1 tracks the google-tag record.
- `poellm-botnet-...`: every clause checked against Lumen and BleepingComputer; the 3,400 vs about 2,200 victim-count discrepancy inside Lumen's own page is disclosed in `sourcing_note`; the Lumen page date field (2026-03-16) vs outlets' 2026-10-07 is disclosed; the four reference entries exist; CVE ids appear on the pages their clauses cite (gate `citation-cve` pass). The Register is not cited in the entry (the run record's remark that it relays the report is true: S3 read the article).
- `idc-frontier-idcf-cloud-ransomware-...`: Japanese notices read in the original; the `original:` quote is a verbatim substring and the English translation is faithful; four zones, 495 customers, console suspension, TypeS/private-cloud exclusion, Jiji website outages all confirmed. Routine priority is calibrated. Classification A/1 follows the store's convention for victim-statement primaries.

### Run record
Telemetry arithmetic holds (sub-agent and iteration durations, iteration-1/2 finding tallies by class), `entities_added` matches the registry diff (3 incident/malware keys plus 2 product keys), backlog dispositions match the `state/coverage_backlog.md` diff, borderline-drop notes spot-checked against the saved bodies (Anthropic report, Axios, 6abc). Only gate failures are the expected mid-loop ones (`run-clock`, `verification-confirmation`).

### Missed angles
Weekend window; no KEV addition in window; the recent exploited edge CVEs a search surfaced (FortiMail CVE-2026-104286, Cisco SD-WAN Manager CVE-2026-76504, Apple CoreGraphics CVE-2026-86950, F5 BIG-IP APM CVE-2026-94127, Cisco ESA CVE-2026-76461, Chrome CVE-2026-11645) all have entries already. No in-window gap I can name a source for. Coverage looks complete.

### Editorial / less-is-more flags (advisory)
1. (low confidence) IDC Frontier body: four narrative sentences for a routine no-vector, no-actor incident; rubric says two at most. Each sentence carries a provider fact or the lesson, so left advisory, as in iteration 3.
2. (low confidence) PoeLLM summary states "a financially motivated botnet"; Lumen: "The campaign appears to be financially motivated."
3. (low confidence) `sourcing_note` length: PoeLLM four sentences including the page-date remark; ChainDrop six sentences.
4. (low confidence) ChainDrop body: "points to the Dune-derived naming the payload reuses as the similarity to previous Shai-Hulud campaigns" compresses two adjacent Elastic statements ("The payload contains strings with Dune-themed references and has similarities to previous Shai-Hulud campaigns") into a linkage the page does not make. Pre-existing text; judged supported enough to stay `ok`.
5. (low confidence) Carried from iterations 2 and 3, declined with reasons: pre-existing em dashes in ChainDrop reader-facing text and the `gh-token-monitor` persistence name.

### Verdict
CLEAN

### Findings summary (machine-readable)
Advisory (F11) records only; see `verification.iter4.findings.yaml`. No truth or editorial findings.
