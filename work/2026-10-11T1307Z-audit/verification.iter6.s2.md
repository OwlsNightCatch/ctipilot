**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T17:35:18Z · ended_at=2026-10-19T18:05:32Z · duration_seconds=1814

## Verification report — 2026-10-11T1307Z-audit (iteration 6, slice s2)

Scope: 28 entries (all updated by this fire), 245 ledger claims, all answered in `verification.iter6.s2.claims.yaml` (239 ok, 4 F3, 2 F4). Post-fix pass: every ledger claim was walked, not a sample (remediated entries carry all their claims; the ledger's quarter-sample entries were walked in full too). Every cited page was fetched this iteration (`extract`, `url`, `cisa-kev`, WebFetch once for Mandiant's June post, jina fallback only where `extract` itself fell back; cached gate bodies only for the two OX Security pages, which answer 403). Prior-iteration deltas: 8 checked (below).

### Deltas from iteration 5

| Prior finding | Remediation | Result |
|---|---|---|
| PeopleSoft F4 (reachability sentence) | rewritten, marked analyst judgement | Holds: "In analyst judgement, public-sector and university SOCs running PeopleSoft should also audit the external reachability of the web and application tier." No application names, no "first action". |
| Gentlemen F4 (nmap/masscan hedge) | "appears to have used" restored | Holds: Talos "They appear to have used Masscan and Nmap". |
| Acronis F9 (date conflict) | Declined | Rationale fails in part: Help Net Security does date the advisory ("published on Tuesday", 2026-09-15) while the record says 2026-09-17T13:30:00Z. Re-raised as F9 (low confidence). |
| PeopleSoft F11 (self-references) | reworded | Holds on disk: "Action: patch out-of-band **and** compromise-assess; yesterday's hardening guidance ... stands" and "adapting to the defensive guidance published after the June wave". The 2026-06-16 record summary "(§ 4 update)" is append-only. |
| ChainDrop F3 (Dune / similarities) | stated separately | Holds for the Dune clause (Elastic: "Dune-themed references ... similarities to previous Shai-Hulud campaigns"); the residual "explicitly ... rather than a new family" re-raised as F3 (low confidence). |
| ChainDrop F11 (repeated switch passage) | Declined (attribution) | Rationale addresses attribution, not repetition; kept as advisory F11. |
| Check Point F11 ("R80 through R81") | Declined | Rationale holds: sk1000171 lists "R80, R80.10, R80.20, R80.30, R80.40, R81 (all EoS)" separately from R81.10 (fix from Take 192). Not re-raised. |
| Liechtenstein F11 (three takeaways) | Declined | Partly holds (each takeaway sits in its section); the misleading "(updated)" label kept as advisory F11. |

### Citation does not support the claim
- F3 #1 Check Point (claim 5c80850171): the entry's "Check Point's own two independent indicators ... second, a resource-loading error referencing a file path containing parent-directory-reference sequences (sk1000171)" no longer matches the cited page. The live sk1000171 (lastModified 2026-10-13) lists Indicator 1 and Indicators 2.a to 2.c (greps on "Invoking method ... in version", "Uploading file ...", "The path to the jars: ..."). Bishop Fox (2026-10-01) describes the earlier second indicator as the "Failed to load allResourceFiles" grep. The change post-dates the entry text, so this is staleness rather than an original error. immediate_action and actions[2] ("the two log indicators miss the published exploit route") rest on the same description.
- F3 #2 ChainDrop (96277ce9e1, low confidence): Elastic "identified the return of Shai-Hulud" and "a new Shai-Hulud campaign"; it never says "rather than a new family".
- F3 #3 Cisco ISE (1b129f95f5, low confidence): Cisco says "unexpected uploads ... to external IP addresses or downloads from malicious IP addresses"; the entry says "uploads or downloads to unfamiliar IP addresses".
- F3 #4 PeopleSoft (fb4ecca3a8, low confidence): "with exfiltration a separate step" is cited to BleepingComputer, which says nothing about exfiltration; the clause is Mandiant's.

### Unsupported / hallucinated facts
- F4 #1 PeopleSoft actions[0] (9d91d9923b, low confidence): "Treat any instance that was internet-reachable and unpatched at any point since 27 May 2026 as compromised until proven clean". Mandiant: "Organizations that identify a web shell should treat the host as compromised".
- F4 #2 PeopleSoft Detection paragraph (c91116831a, low confidence): "review authorized_keys and /etc/hosts for unauthorised additions"; BleepingComputer says the script parses /etc/hosts and falls back to key-based SSH, nothing about modification. Unmarked, unlike the adjacent analyst-judgement sentence.

### Claims missing inline citation
- F5 #1 PeopleSoft 2026-06-16 section (low confidence): "of which Switzerland is a member" has no citation; SecurityWeek gives "46 member states, including 27 European Union countries".

### Surface contradiction
- F9 #1 Acronis (low confidence): advisory record stamped 2026-09-17T13:30:00Z, but BleepingComputer (2026-09-15) quotes it and Help Net Security (2026-09-16) says it was "published on Tuesday"; not surfaced.
- F9 #2 Liechtenstein (low confidence): entry follows the government ("overnight into 2026-07-30"); The Record says "two days beginning on July 29".

### Editorial / less-is-more flags (advisory)
- F11 #1 Em dashes in reader-facing text this fire edited (ChainDrop title and summary, Mandiant title and "Case study N —" headings, Acronis title, Liechtenstein, PeopleSoft, Cisco ISE).
- F11 #2 ChainDrop containment paragraph repeats the switch/intimidation contrast three times.
- F11 #3 Liechtenstein 2026-09-02 "Defender takeaway (updated)" label.

### Considered, not raised
- Every other claim in scope checked against the page: GLPI (all seven GHSA CVSS 4.0 scores 5.1/5.9/7.0/7.0/7.1/8.4/8.4 match cves[]), xrdp (GHSA CVSS 3.1 9.1 vector), Spring (9.1, fix table), LiteLLM (CVSS 4.0 9.3, affected >=1.81.16 <1.83.7, Sysdig 36 h 7 min after the global-database listing), PAN-OS (9.3/8.7, fix table, Unit 42 timeline), node-ipc, Booking.com and job-seeker NCSC pages, Everest Forms, Splunk (fix table, KEV 2026-06-18), SimpleHelp, JFrog (both JFrog tables, Wiz, KEV 2026-09-11), AEPD, Cisco ISE (fix table, CVE-2026-76423 not in KEV), Mandiant AI report (all eight case studies), Acronis, NTC, Gentlemen (Talos phases), TraderTraitor (Zscaler ROOFDECK variants), ClosedQuorum, the Swiss motion, Storm-3168, Apple (KEV forensicTriage "No", EPSS 1.24%).
- Internal records (Booking.com, job-seeker, AEPD, NTC): frontmatter-only or label-only changes; source-supported, no reader-facing delta.
- Gate-level note, not re-litigated: Inside IT 2026-10-06 (Liechtenstein) shows datePublished 2026-10-07 in its JSON-LD with a 20261006 slug; one-day drift, left.
- Coverage: no missed angle named for this slice.

### Verdict
NEEDS_FIXES (truth: 6, editorial: 3, advisory: 3). Eight of the nine truth and editorial findings are low confidence; the Check Point indicator staleness (F3 #1) is the one with a hard page-state evidence trail and a timing caveat (page changed 2026-10-13).

### Findings summary (machine-readable)
See `work/2026-10-11T1307Z-audit/verification.iter6.s2.findings.yaml` (12 records).
