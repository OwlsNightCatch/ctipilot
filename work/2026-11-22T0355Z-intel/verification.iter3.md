**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-22T05:27:47Z · ended_at=2026-11-22T05:40:49Z · duration_seconds=782

## Verification report — 2026-11-22T0355Z-intel (iteration 3)

Scope: post-fix pass. Every changed claim (5), every claim of the four remediated entries (Java4Shell 28, Cisco ESA 17, Basel-Landschaft 10, MONAI 15 = 70), plus 17 of the 44 claims of the two untouched-since-iteration-2 entries (nginx2root 9, Ruby 8; 38 percent, chosen from the changelog sections, action lines and body clauses). 87 verdict rows in `verification.iter3.claims.yaml`. Fetched this pass: MONAI 0.8.6 release notes, GHSA-qc22-rmgc-vg94, the Amazon post, the CVE record (CVE API, read only, not cited), Ubuntu CVE page and USN-9159-1, Debian tracker plus DSA-6639-1 and DLA-4917-1 announcements (lists.debian.org via WebFetch), Citrix CTX697367, Mitel MISA-2026-0014, Tenable FAQ, Calif (raw HTML), Upwind, Equixly, Talos, CISA alert (WebFetch), NCSC.ch hub post 13198, BACS, Cisco Java and nginx advisories, Fortinet FG-IR-26-278 and 279, Oracle CSPU, OpenJDK advisory, Cisco ESA advisory, CISA KEV alert (WebFetch), BleepingComputer, Rapid7 wrap-up, Metasploit PR 22028 (merge Nov 5), the canton media release, Polizeiticker, Inside IT, watson.ch, Synology SA-26:20, ENISA EUVD, GitLab patch release, Veria Labs, Rapid7 nginx post and PoC repository, CERT-EU. The canton FAQ page returned 403 again on extract, url (jina credit exhausted) and WebFetch.

### Prior-iteration deltas (all four remediations checked against sources)

1. Java4Shell dates: Ubuntu page reads 'Publication date 18 November 2026' and the source record and citation carry 2026-11-18 (correct). Debian clause reads 'As of 2026-11-22' (honest; see F11 #3 for the dated announcements). Run note no longer says every added fact predates the window (correct; the Debian fixes in fact predate it, 2026-11-19).
2. Cisco ESA: body now reads 'describes CVE-2026-76519, which CISA's catalog lists as a relative path traversal' cited to the CISA alert, whose verbatim KEV line is 'CVE-2026-76519 Cisco Secure Email Gateway Relative Path Traversal Vulnerability'; Cisco's advisory is titled 'Arbitrary File Write' and the summary says arbitrary file write. Correct.
3. Basel summary: 'civil status' matches Polizeiticker and Inside IT ('Name, Wohnadresse, Geburtsdatum, Zivilstand, Berufsfunktion, ... ZEMIS ... Kontaktdaten von Arbeitgebern'). Correct.
4. MONAI sourcing_note: plain provenance, no narration. The CVE record read this pass says 'monailabel ... through 0.8.5 allows directory traversal, with resultant remote code execution, via the image parameter to the PUT /datastore/image endpoint, as exploited in the wild starting in September 2026', CVSS 3.1 9.8 (AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H), CWE-24; the summary, title, headline and cves[] match it. Not citing it is consistent with the repository rule.

Declined items, reasoning checked: F10 Synology SA-26:21 (CVE-2026-120382). A web search this pass finds no exploitation and no public exploit for it (the only PoC found is the nginx2root one for CVE-2026-123007); SA-26:20 in the nginx2root entry names the same fixed DSM builds (7.4.1-90080-2, 7.3.2-86009-6, verified on the SA-26:20 page) and the action tells DSM readers to install them. At that exposure it does not clear the critical/high bar, so the deferral to the audit is defensible and I do not re-raise it. Basel FAQ rows: unreadable again, not findings; Polizeiticker corroborates the forensic finding, the permit-G database, 97'000 records, the 2016-11-28 start, employer contact data, the criminal complaint and the platform being out of operation.

### Citation does not support the claim

F3 #1 — 2026-11-21/basel-landschaft-97000-cross-border-work-permits-stolen, `## Improvement — 2026-11-22T04:35:05Z` and the record summary. Quote: "the Alertswiss warning of the night that the emergency numbers 112, 117 and 118 might be restricted was withdrawn a few hours later as a precaution, a government spokesperson said" (record: "withdrawn within hours as a precaution"). watson.ch: "Wenige Stunden später gab es Entwarnung. Die Erreichbarkeit der Notrufnummern sei gewährleistet gewesen, sagte Regierungssprecher Nic Kaufmann. Doch habe man die Warnung als Vorsichtsmassnahme herausgegeben, da man nicht gewusst habe, ob noch weitere Server vom Internet isoliert werden müssten." The precaution was issuing the warning; the withdrawal was an all-clear, and the spokesperson said the numbers had stayed reachable (omitted). Fix the section and amend the record summary: the warning was lifted a few hours later; the spokesperson said the numbers stayed reachable and the warning was issued as a precaution because it was unclear whether more servers would have to be isolated.

F3 #2 — 2026-11-22/monai-label-path-traversal-zero-day-found-by-cairn-ai-agents, `**Detection:**` line. The clause "and for tar uploads to `PUT /session/` with `uncompress=true`" sits under a citation of the GHSA advisory plus Amazon; neither page mentions session upload or tar archives. It is carried only by the 0.8.6 release notes ("`PUT /session/?uncompress=true` extracted uploaded tar archives without checking member names"), which that line does not cite. Fix: add the release-notes link to that citation. The remaining clauses of the line are supported.

### Editorial / less-is-more flags (advisory)

F11 #3 — (low confidence, optional) 2026-11-18/cve-2026-114938-java4shell..., Debian clause. True as read today; the link label and `sources[].date` still carry the processing date of an undated page. The fixes are dated and I fetched the announcements: DSA-6639-1 (openjdk-21; 'Thu, 19 Nov 2026 11:07:21 +0000'; lists CVE-2026-114938; https://lists.debian.org/debian-security-announce/2026/msg00561.html) and DLA-4917-1 (openjdk-17; 'Thu, 19 Nov 2026 17:22:15 +0100'; https://lists.debian.org/debian-lts-announce/2026/11/msg00042.html). Citing those with 2026-11-19 removes the date question, confirms `improvement` as the right record type, and lets the run note say 'dated 2026-11-19' where it now says 'undated on the tracker'.

### Considered and not flagged

- Java4Shell record type `improvement`: Ubuntu 2026-11-18, Debian 2026-11-19, Citrix 2026-11-19, Mitel 2026-11-19 and Red Hat 2026-11-19 all predate the previous fire; correct as an improvement, `updated_at` stays put.
- Java4Shell supersession: the 2026-11-19 section's 'Red Hat and Ubuntu had released no fix' is dated and explicitly superseded by the new section. Ubuntu's own page lists USNs dated 18 November, which the new section reports.
- Citrix and Cisco citation dates (2026-11-19 and 2026-11-20 for revisions published one day after initial publication): within one day, living pages.
- MONAI `event_date` 2026-11-20 against a 2026-11-22 release page: defensible as the disclosure date (Amazon post and CVE assignment).
- MONAI summary 'a Chinese-nexus operator': Amazon's own headline wording; the body keeps 'moderate confidence'.
- Coverage: no KEV addition in the window (kev-window output: 0); searches for in-window exploited zero-days and Swiss public-sector incidents found nothing the store lacks (Xen Orchestra VSA-2026-062 is already an entry). Coverage looks complete apart from the declined, audit-bound Synology item.
- Style: no em dash outside headings, no pipeline vocabulary, no IOC, in any of the six entries. `check_run.py`: only the run-clock FAIL that Phase 6 re-stamps and one transient 403 WARN on the MONAI release page.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 1)

### Findings summary (machine-readable)

See `verification.iter3.findings.yaml` (3 records: two F3, one F11).
