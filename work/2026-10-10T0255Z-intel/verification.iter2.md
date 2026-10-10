**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-10T04:26:29Z · ended_at=2026-10-10T04:42:40Z · duration_seconds=971

## Verification report — 2026-10-10T0255Z-intel (iteration 2)

Scope: post-fix pass, all 214 ledger claims walked (206 ok, 6 F3, 1 F13, 1 F14; rows in `verification.iter2.claims.yaml`), all eight entries read whole, `git diff HEAD` read for the five updated entries (every changed line is covered by the run's record `fields`), run record read. Every cited page was fetched this iteration (`extract`, `pdf`, `cisa csaf`, `cisa-kev`, `ncsc-csh post`, GitHub advisory HTML and API, raw HTML for JSON-LD dates). Missed-angle searches: nothing evidenced.

### Prior-iteration deltas (each fix checked against the source this iteration)

| Finding (iteration 1) | Result |
|---|---|
| Zammad DIVD claims re-cited to /public_statements_on_hack/ | 3 of 4 fixed ("in seconds", volunteer data and segmentation in paragraph 1, AI-agent/no-link). The 4th (claim e720599f34, segmentation in the Defender takeaway) still cites the case page: see F3 #1 |
| Zammad "within seconds" hedge | Fixed: "could have escalated within seconds" in actions[1], Detection, section and evidence |
| Zammad CVE-2026-102489 fixed field | Fixed (7.2.2 current; no 7.2.3 exists, 404) |
| Zammad CVE-2026-102490 mapping | Fixed and correct: GHSA HTML sidebar and API show CVE ID CVE-2026-102490, affected <= 7.2.1, patched 7.2.2, cvss_v4 8.5; DIVD case page text matches. The citation date of that DIVD sentence is wrong: F3 #2 |
| Zammad actions trimmed | Done; actions[0] is still a compound (F18, low) |
| SonicWall restart/no-workaround | Fixed: THN carries "the appliance restarts when the installation finishes. No workaround is listed." |
| SonicWall "single sensor" | Removed; "135 attempts from two source addresses" matches Previdian (135 / 2 unique IPs / 09-10 Oct) |
| SonicWall log window | Fixed (2026-10-06) |
| SonicWall CCCS update | Added, but the remediation introduced an unsupported link ("which is the same reporting"): F13 |
| SAP Onapsis date | Fixed: JSON-LD datePublished 2026-09-18T12:13:53Z, dateModified 2026-09-24 |
| SAP three routes | Fixed: Onapsis OVERPASS page lists ICM/Web Dispatcher, SAP Dispatcher (SAP GUI), RFC |
| SAP Triage clause | Fixed: unsupported clause removed, remaining line cites Onapsis S4GET |
| PaperCut 2023 precedent / university statement / absence and Home-page attributions | Fixed: Rapid7 carries "broadly exploited ... multiple threat-actor groups, including ransomware operators", the university/DFIR statement and the Home-page bypass; PaperCut bulletin carries "absence does not rule out compromise"; Huntress carries the server.log deletion |
| PaperCut immediate_action 24.x, "at least 440", "never legitimately" | Fixed (Sep bulletin: 26.0.5 and 25.0.13 only; GreyNoise "at least 440 ... 395 identified"; absolute removed) |
| PaperCut F9 | Fixed: section and record carry the bulletin's "closes off additional attack vectors we have observed being exploited in the wild" (FAQ under Superseded information) |
| Publica admin.ch / named funds | Fixed: admin.ch says "weitere Kunden informiert"; BPK, BLVK, PK Post, Inside IT cite their own pages |
| MikroTik priority / "recent CERT Polska" / detection / sourcing note | Fixed; routine priority matches the backlog hold condition (vendor fix named) |
| AhsayCBS scores / techniques / actions | Fixed: "medium"/"critical" per Huntress; 16 technique ids equal Huntress's ATT&CK table exactly |
| GhostAction full-history and credential-revocation citations; 346 vs 378 | Fixed: StepSecurity remediation carries history rotation and "treat any completed run as a confirmed exfiltration"; GitGuardian carries revoke-the-credential; 378 is stated as a count across all waves |

### Citation does not support the claim

**F3 #1 — Zammad, Defender takeaway (claim e720599f34), unremediated iteration-1 finding.** Entry: "keep Zammad behind authentication or off the internet and segmented, as DIVD credits segmentation for stopping its own intruders ([DIVD CSIRT, 2026-10-01](https://csirt.divd.nl/cases/DIVD-2026-00014/))". Page: raw HTML and extract of the case page contain no "segment" (0 hits); the sentence "Thanks to proper network segmentation and the actions of our IT and Incident Response Team after detection, we were able to stop the attackers from going deeper" is Statement #4 at /public_statements_on_hack/. "Behind authentication" is not a DIVD statement. The run record says all four claims were re-cited; this one was not. Fix: cite the public-statements page, reword "behind authentication".

**F3 #2 — Zammad, DIVD-2026-00014 citation date (claims 37acbdcff3, e720599f34, 0f9f0566ac and sources[]).** Entry cites the case page as 2026-10-01 in the body (three places), the 7.2.2 update section and sources[]. Page: "Last modified 09 Oct 2026 20:01 CEST"; timeline "29 Sep 2026 Publication of casefile". The 7.2.2 sentence ("Zammad has fixed both vulnerabilities the first in release 7.2 and the second in release 7.2.2") cannot predate 2026-10-08. Use 2026-10-09.

**F3 #3 (low confidence) — AhsayCBS, "the latest version".** Entry attributes "10.3.4, the latest version, is also affected" to Huntress; the Huntress page says only "Ahsay 10.3.4 is also affected". "Latest" is BleepingComputer ("currently the latest version") and SecurityWeek.

**F3 #4 (low confidence) — PaperCut, v23 guidance.** "There is no fix for v23 and earlier — PaperCut's guidance for that line is to upgrade to a supported version — and Huntress estimates 47% ... ([Huntress])": Huntress carries "no patch is currently available" and the 47% figure; the upgrade guidance is in PaperCut's bulletin FAQ.

**F3 #5 (low confidence) — GhostAction, Detection.** "an organisation-scoped code search for the two file names under .github/workflows ([StepSecurity])": StepSecurity's org-scoped queries search for content markers (AKIA_CTX_START, c=monami, the C2 address); the file names appear in its breach callout and in Socket's IOC list.

### Analytical-link-as-fact

**F13 #1 (low confidence) — SonicWall update.** "the Canadian Centre for Cyber Security's bulletin AV26-1017, updated on 2026-10-09, now says open source reporting indicates the flaw is being exploited in the wild, which is the same reporting ([Canadian Cyber Centre])". AV26-1017 Update 1: "Open source reporting indicates that CVE-2026-102255 is being exploited in the wild." No source is named; "the same reporting" and "rests on one observer" are inference. The run-record note repeats it.

### Quantifier without source

**F14 #1 (low confidence) — PaperCut actions[2].** "reaches full domain admin via exactly these paths within minutes of initial compromise": GreyNoise gives five minutes fastest, 144 minutes longest, multiple-day delays for some, domain admin at only 12 victims.

### Org-triage / priority

**F16 #1 (low confidence) — PaperCut priority.** critical on a 6-week-old entry re-floated by a delta (superseded-build bypass analysis, admin-only CVE-2026-82077, "No source names exploitation") that is not time-critical to the hour or day; the entry's own 2026-09-29 section says new compromises slowed considerably.

### Action-item discipline

**F18 #1 (low confidence) — Zammad actions[0].** Upgrade, log-check script, package check and template check in one action; the artifact clauses restate the Detection paragraph.

### Editorial / less-is-more flags (advisory)

**F11 #1** em dashes outside headings in PaperCut (26 body lines plus title) and SAP (5, including the paragraph rewritten this fire); declined once, noted again. **F11 #2** attacker file/service names (security-audit.yml, github_actions_security.yml, MicrosoftEdgeUpdateSvc, cbssvcX64.exe): rule 12 lists "mutex or file-name indicators"; declined once, main agent decides. **F11 #3** sourcing_note: PaperCut carries "rated B ... in sources.json rather than A. Reliability held at B rather than A", SAP "credibility reflects ...", Zammad is ~12 sentences, Publica ~7. **F11 #4** Publica record summary "Priority moves from routine to notable because ..." is metadata narration. **F11 #5** PaperCut and SAP rewrites of earlier text sit under one `update` record whose summary covers only the new delta (4c(f)).

### Checked and clean

Every `evidence[]` quote is a contiguous substring of its page (MikroTik/CISA quote checked in the CSAF JSON; Publica originals checked against the German pages and PDFs). cves[] ids, scores and ranges verified against the per-vulnerability authority (MikroTik notice and CSAF, Huntress, SonicWall PSIRT, DIVD CVE records, GHSA record, PaperCut Sep bulletin and CVE record, EPSS from FIRST 2026-10-05). KEV 2026.10.08 does not list CVE-2026-84411, -102255, -105133, -105134 or -82077; Zammad and PaperCut KEV additions match. Zammad's 27 advisories re-counted from the API (2 critical, 12 high, 10 medium, 3 low, all <= 7.2.0, none with a CVE id). Dedup: no overlap with prior_coverage; MikroTik cites the 2026-09-06 chain entry in references[]. Registry keys exist; two new keys are well-formed. Classification blocks present and consistent; no org_triage or watchlist use. Coverage looks complete: Citrix, Atlassian, Cisco, Veeam and Splunk are covered or dropped for stated reasons; searches found no further in-window story.

### Verdict

NEEDS_FIXES (truth: 7, editorial: 2, advisory: 5)

Two findings are firm (F3 #1, F3 #2); the other seven non-advisory findings are low confidence and cheap to fix.

### Findings summary (machine-readable)

See `work/2026-10-10T0255Z-intel/verification.iter2.findings.yaml` (14 records).
