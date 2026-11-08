**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-08T14:58:19Z · ended_at=2026-11-08T15:18:46Z · duration_seconds=1227

## Verification report — 2026-11-08T1309Z-audit (iteration 2)

Scope: post-fix pass. Ledger `claims.iter2.yaml` (230 claims) and `claims.changed.iter2.yaml` (21): 161 claims answered in `verification.iter2.claims.yaml` (21 changed claims; every other claim of the ten remediated entries, 137 in all with overlap; a random quarter of the remaining 93, 24 claims, seed 20261108). Prior-iteration deltas walked first against freshly fetched sources (Publica via watson.ch, Inside IT, NZZ, BPK; Keycloak notes, Red Hat page and CNA record, CISA alert; Elastic PDF and summary page; Android bulletin and BleepingComputer; both IBM bulletins parsed row by row; Splunk, Siemens SSA-045512 raw HTML, QNAP QSA-26-19, Ubuntu, Sophos, Fortinet, Balbooa, mySites.guru, Cisco). The three new entries were read whole; the run record and audit report were checked on disk (record types and counts, 27 updated ids, cves_seen 18 added and 40 bumped, registry diff, run-record telemetry for the seven fires, word counts, priority counts).

All nine iteration-1 remediations are correct as applied except where listed below: the Publica watson.ch citation and 'assumes' wording, the Elastic 'anonymized address known to be malicious', the Android title hedge, the IBM counts (202 rows on the v12 bulletin, 206 distinct ids across both, 18 v12 rows with no privileges at 9.0 or higher), the Node2Shell Keycloak addition, the Gridbox summary and the Linux TCP headline all match their sources. The Keycloak remediation, however, introduced or left four defects (F4 #1 to #3 below).

### Unsupported / hallucinated facts

- **#1 F4 — Keycloak, Red Hat Build of Keycloak version scope.** Quoted: Exposure "a Keycloak or Red Hat Build of Keycloak below 26.8.2"; action "Upgrade every Keycloak instance ... to 26.8.2"; `cves[].affected` "the release notes and Red Hat's page give no range for older release lines"; sourcing note "Neither gives a range for lines older than 26.8." Source: https://access.redhat.com/security/cve/CVE-2026-117691 (affected-packages data in the page) and the CNA record https://cveawg.mitre.org/api/cve/CVE-2026-117691 list Red Hat build of Keycloak 26.6 images fixed by RHSA-2026:96039 and RHSA-2026:96040 (released 2026-11-07), "Red Hat build of Keycloak 26.6.9" state Fixed, rhbk/keycloak-rhel9 unaffected from 26.6-25, and Red Hat Single Sign-On 7 unaffected. RHBK does not carry the upstream 26.8.2 number, so the version scope and the single upgrade target are wrong for RHBK users, and "no range" is false of Red Hat's own page. Fix: name the RHBK fixed builds and errata, state RH SSO 7 as unaffected, confine "26.8.2" to upstream Keycloak.
- **#2 F4 (low confidence) — Keycloak, exploitation statement.** Summary "...(CVE-2026-110931); no source reports exploitation." and body "Neither source reports exploitation of the Keycloak flaws or a public proof of concept." sit beside the added sentence that the release also fixes CVE-2026-111497, "which CISA lists as exploited". CISA alert (WebFetch, 2026-10-27): "CVE-2026-111497: Google Brotli Unchecked Return Value Vulnerability". The summary never mentions the Brotli fix; "Neither source" follows three cited sources. Scope both to the SAML flaws and name the Brotli fix in the summary.
- **#3 F4 (low confidence) — Keycloak Detection.** "SAML messages received by HTTP GET whose query string carries an encoded parameter name such as %53AMLResponse instead of SAMLResponse." Red Hat's guidance, cited in the entry's first paragraph: "crafted HTTP GET request containing a percent-encoded unsigned SAML parameter placed before a legitimately signed parameter", so the literal signed parameter is still present; "instead of" would miss it, and only the second half of the line is labelled an inference.
- **#4 F4 (low confidence) — Node2Shell `cves[].affected`.** "Keycloak before 26.8.2 (bundled Brotli decoder)". The release notes (https://www.keycloak.org/2026/11/keycloak-2682-released) list only "[#54333] [CVE-2026-111497] Out-of-bounds write in bundled Brotli decoder dist/quarkus" under 26.8.2 and state no affected range; the Keycloak entry says the notes give none.
- **#5 F4 — audit report, `high` share.** `docs/audits/2026-11-08-quality-audit.md` line 147: "`high` is 11 of 47 in-scope entries (23%) ... below the alarm level, so there was no re-grade." On disk (47 in-scope entries from the five truth ledgers) the counts are 12 high, 1 critical, 27 notable, 7 routine; at HEAD they were 11 high and 2 critical, so 11 is the count before this fire's Ivanti move to high. 12 of 47 is 25.5%, "above about a quarter" in the prompt's calibration-alarm rule (prompts/quality-audit.md item 12). State both counts and the re-grade decision.

### Editorial / less-is-more flags (advisory)

- **#6 F11 — "no usable mitigation" (Keycloak summary) and "with no Red Hat mitigation" (report line 85).** Red Hat's formal text says options "do not meet the ... criteria"; its CNA record carries courtesy guidance naming an interim lever that the body cites. Say "no mitigation that meets Red Hat's criteria".
- **#7 F11 — record summaries narrower than sections** (carried from iteration 1): Node2Shell omits the ELLIO correction; Publica omits the NZZ broader-quote sentence added this iteration and the Inside IT/AWP attribution fix.
- **#8 F11 (low confidence) — Publica "Publica confirmed the sequence to the paper: it asked PK Softech in September 2025 ([watson.ch])".** watson.ch attributes the month to Publica's statement to watson, not to what Publica confirmed to the Tamedia paper.
- **#9 F11 (low confidence) — Android Exposure "which Google names as the fix level" and "The vendor-stated fix level is therefore 2026-11-01".** The bulletin row has no description; the CVE link rests on BleepingComputer. Title and summary hedge it, these two statements do not.
- **#10 F11 (low confidence) — IBM Exposure "management, developer portal or gateway endpoints".** The bulletins name only "gateway configuration" and "other tenants' portal data" in single rows; the component list is uncited.
- **#11 F11 — report Publica word count.** 1,141 in recommendation 3; 1,143 on disk after the restored citation (1,148 at HEAD).
- **#12 F11 — run record header.** `verification_iterations: 1` and `verification_residual_count: 9` are first-pass values; 17 of 18 findings are recorded Applied. To be finalised after this iteration.

### Notes on what held

- Coverage looks complete for the critical/high signal: the KEV window (3 additions) is covered; no further home-region or exploited-edge gap surfaced from the dedup context and the run telemetry. Elastic's missing body mention of paste-and-run infostealer delivery (title and summary carry it, the PDF supports it) was judged a depth choice, not a defect.
- The three new entries pass the style gate (no em dash, no IOCs, no pipeline vocabulary in reader text); actions are single, concrete and not body restatement; classification A-2, A-2, B-2 is consistent with a single vendor source each.
- Run-record claims that hold on disk: 27 `updated_entry_ids` equal the entries carrying a record of this run; 11 corrections, 9 updates, 7 improvements, 6 internal; `cves_seen` 18 added and 40 `last_seen` bumps; registry diff (IBM, Gridscale DSA, Gridscale PSS®E, Elastic report, `3AM` ambiguous label); iterations per fire 6, 6, 8, 8, 6, 8, 2 and durations 1.0 to 5.2 h; 30 entries filed in the week; KEV window.

### Verdict

NEEDS_FIXES (truth: 5, editorial: 0, advisory: 7)

### Findings summary (machine-readable)

See `work/2026-11-08T1309Z-audit/verification.iter2.findings.yaml` (12 records).
