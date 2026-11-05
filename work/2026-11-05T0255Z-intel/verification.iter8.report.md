**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-05T07:43:06Z · ended_at=2026-11-05T08:07:14Z · duration_seconds=1448

## Verification report — 2026-11-05T0255Z-intel (iteration 8)

Role: post-fix pass at the iteration cap, full claim coverage. Previous iteration (7) returned NEEDS_FIXES with one truth finding (run-record word counts) and seven left advisory items; entries unchanged since iteration 6.

### Scope and coverage

- 6 new entries, 5 updated entries (whole entry read, `git diff HEAD` read for each, record `fields` checked against the diff), run record read in full (frontmatter, iterations 1 to 7, verification notes).
- Claim ledger `claims.iter8.yaml`: 256 claims, 256 verdict rows written to `verification.iter8.claims.yaml` (`python3 tools/claim_ledger.py 2026-11-05T0255Z-intel --coverage 8`: 256/256 answered, 0 missing). Every row rests on a page fetched in this iteration: `extract` first; `url` raw HTML or the Next.js page payload for the Binarly, Akamai, Fortinet, Sophos RCA and Palo Alto pages that `extract` truncates; `jina` html mode for the SonicWall PSIRT tables; `ncsc-csh post` for NCSC.ch 13054, 13105, 13120; `pdf` for the Xerox v4 and v5 bulletins; `WebFetch` (outbound-links template) for SentinelLABS, which returns a Vercel 429 checkpoint to every other transport; the Red Hat security-data API and the EUVD API for fix tables and CVSS 4.0 scores; the CISA KEV catalogue through the bridge (version 2026.11.04). No claim is `unreadable`.
- Mechanical gate re-run: `check_run.py 2026-11-05T0255Z-intel` 60 pass, 0 warn, 0 fail.

### Prior-iteration deltas

1. **Iteration 7 F4 (run-record word counts).** Recomputed with the gate's own `_main_words` (HEAD body vs working tree): Danfoss 736 to 735, Node2Shell 549 to 539, CVE-2026-98432 546 to 546, Zyxel 641 to 613. The run-record sentence "Entry rewrites replaced text instead of adding it: the Danfoss (736 to 735 words), Node2Shell (549 to 539), CVE-2026-98432 (546 to 546) and Zyxel (641 to 613) analyses did not grow" matches exactly. (The Xerox analysis grew 290 to 410 words, within the 550 limit, and the sentence does not claim otherwise.) Remediation correct.
2. **Seven left F11 items.** The run-record bullet "Advisory items left for the next quality audit" lists the Vaud placeholder wording, the CloudLinux and AWS date labels, the iSCSI sourcing-note Pen Test Partners remark, the APT29 CVE-2025-43529 fixed-field wording, the kernel sourcing-note capital, the SEPPmail "two are unauthenticated" phrasing and the four vendor tasks in Node2Shell actions[1]. Each maps one-to-one to an iteration 6 or 7 finding (the APT29 "no fetched Apple page" text is the `fixed` field of the CVE-2025-43529 record), each was marked may-be-left by the verifier, and the bullet's characterisation is accurate. Not re-raised.

### Truth checks (all entries)

- **New entries.** Vaud notice (text, date, translated quotes and French originals verbatim), Microsoft Learn concept and block pages, Cloudflare workers.dev page; SpecterOps iSCSI post and Pen Test Partners (port 3260); Sophos RCA INC-2026-002 (all analysis sections, timeline, lasting controls) and the Sophos blog (NICKEL ALLEY); SEPPmail revision history, EUVD-2026-116781/-116782/-116796/-116797/-116798 and the EUVD API (CVSS 4.0 vectors and scores 9.2, 9.2, 8.7, 8.3, 6.9 equal the entry; vendor-page swap of the 114420/114421 scores confirmed); Sekoia post (text, tables, IOC note), CISA KEV rows for all eight CVEs, Apple 120898/120905/127113/125884, GTIG DarkSword fix versions, Chrome 146.0.7680.75/76 (CVE-2026-3910), THN and BleepingComputer relays; SonicWall SNWLID-2026-0019 (affected, fixed and workaround tables, vectors), SNWLID-2026-0011 (fixed 9.5.2, 2026-08-11), the GMS EOL announcement (end of support 2026-09-30), CERT-FR AVI-1456.
- **Updated entries.** Zyxel (both advisories, Binarly blog and advisory, GreyNoise, Acronis, BleepingComputer, CISA alert and KEV, CVE record CVSS 8.8 AV:A, EPSS 0.02778 and 0.00293); Danfoss (AFP/Khaleej, CERT-FR, NCSC 13054, Public Sénat, SentinelLABS, BleepingComputer x2, Guardian, Euronews, CyberInsider, heise x2, SRF, EFS, Coolworld, ENISA, CSIRT Italia BL01 v1.2 and BL02, Le Monde, BFMTV, franceinfo, 20 Minuten); Node2Shell (Node.js, Imperva, ELLIO, CISA alert, Cisco, Palo Alto page and timeline, Tenable, OpenSourceMalware, Envoy GHSA, .NET issue and blog, Broadcom, Splunk SVD-2026-1015, Citrix CTX697300, Patchstack, Datadog, Akamai, NCSC 13105); CVE-2026-98432 (openwall announcement, CIQ, Anthropic, CloudLinux, Go team, Akamai, Vates, XCP-ng, WatchGuard, NCSC-NL, Debian, Red Hat API, AWS, Ubuntu, Citrix CTX697256, MikroTik x2, Fortinet, NCSC 13120); Xerox (v4 and v5 PDFs, KEV rows).
- **Record contract (4c).** For all five updates the record `at` equals the section heading, `updated_at` mirrors the `update` record, the diff shows no change outside the fields each record names, each record summary says what its section says, the main analysis and labelled lines do not contradict the newest section, and every section carries a genuine delta (patch-bypass CVE, blood-service confirmation and EU statements, Splunk and Citrix product lists, vendor fix and advisory statuses, Xerox v5 mitigations).
- **Frontmatter against body.** `cves[]` ids, scores, fixed and affected values, evidence quotes (the four the gate could not machine-check, the two EUVD quotes and the SEPPmail quote, were checked by hand: verbatim), `verification`, `classification` against `sources.json` tiers, `event_date`, `techniques[]`, entities, actions all consistent with the fetched sources.
- **Run record.** Frontmatter durations recompute exactly for all sub-agents and iterations; notes about the KEV window (one addition, CVE-2024-27834, NOT COVERED), backlog expiry dates (2026-11-07, 2026-11-17), registry size (704 KB at HEAD), the three new source candidates, the recipe-note list, the single-source dispositions, the disclosed contradictions and the CVE-2025-8088 side finding (Gamaredon entry "August 2025", Turla entry "7.11+") hold on disk and in the cited pages.

### Editorial checks

- Relevance and priority: Vaud (high, cantonal first-party notice, home-region M365 exposure, decision inside seven days) and Sophos (notable, transferable VS Code workspace-trust tradecraft) clear the bar; SEPPmail notable (exploitation conditions are non-default), SonicWall routine, iSCSI notable (research, no in-the-wild use), APT29 notable. No `high` disqualifier applies to a high entry; no `notable` plainly clears `high` or `critical`.
- Update-vs-new: no new entry carries a CVE or entity the store already holds (checked every CVE of the APT29 entry against `entries/`); the five updates are the same finding with a genuine delta.
- Style: zero em dashes outside section headings, no IOCs, no workflow vocabulary in reader-facing text beyond the left advisory items, English throughout with translations marked.
- Actions: concrete, finding-derived, none generic; the Danfoss action text is unchanged from HEAD.
- Missed angles: the NCSC.ch hub list (13144 Barracuda, 13128 WS_FTP, 13124 Drupal Commerce), the KEV window (WordPress core 2026-11-03, Ivanti 2026-10-30) and the store were cross-checked; every in-window or near-window critical item is already covered by an entry. Coverage looks complete.

### Considered and not raised

- SEPPmail takeaway cites the vendor revision history for "the two conditions the CNA names"; the "LFT enabled" wording is on the EUVD page cited in the Exposure paragraph. Same citation convention as the other takeaway lines in the run; not a defect.
- Sophos `event_date` is the incident date (docs/pipeline.md: "date of the underlying event / primary publication").
- CSIRT Italia BL01 cited as 2026-11-04: that is the version 1.2 date read, stated in the sources[] publisher label and in the section text.

### Verdict

CLEAN (truth: 0, editorial: 0, advisory: 0)

### Findings summary (machine-readable)

```yaml
[]
```
