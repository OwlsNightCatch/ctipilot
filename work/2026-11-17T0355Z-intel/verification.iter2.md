**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-17T05:15:15Z · ended_at=2026-11-17T05:29:23Z · duration_seconds=848

## Verification report — 2026-11-17T0355Z-intel (iteration 2)

Scope: 6 new entries, 2 updated entries (whole entry plus `git diff HEAD`), run record, registry diff, dedup context. All 155 ledger claims carry a verdict row in `verification.iter2.claims.yaml` (153 ok, 2 F3); `tools/claim_ledger.py --coverage 2` reports 155/155 answered. Live `extract` fetches this iteration of Hudson Rock, Ohey, Unit 42, GTIG, Symantec, Huntress (2026-09-03 and 2026-11-16), ad-hoc-news, Amirul Cyber and FG-IR-26-273 (plus raw HTML) were byte-compared with the gate's cached bodies (identical for Hudson Rock, Ohey, Unit 42, GTIG, Symantec, Huntress both posts, FG-IR-26-273); the 19 FortiGuard PSIRT pages, Fortinet blog, ConnectWise disclosure, SecurityWeek, heise, Handelsblatt, WEB.DE and the four Craft sources were read from the gate cache (raw HTML for CVE id, CVSS, Attack Type and Known Exploited metadata); NCSC.ch post 13092 via `ncsc-csh`; CISA KEV via the bridge (CVE-2026-84869 dateAdded 2026-09-11; CVE-2026-123488 absent).

### Prior-iteration deltas, walked first

| # | Remediation | Result |
|---|---|---|
| 1 | OptimJack attributions | Correct. Ohey: router loader from 13 Nov on Kissmetrics, StorifyMe and Optimizely files, minute-ly's loader.js replaced outright (undated); 16 Nov Optimizely files switch to track.js (wallet swap, card skim, router on iPhone/iPad). Hudson Rock: Kissmetrics, StorifyMe, minute-ly deliver only webshell/get.js ("establishes the mobile-router path, not the presence of those financial-theft modules"). Title, headline, summary, body para 1, actions[0] and registry summary all follow this. One residual in the summary (finding 1). |
| 2 | "no provider statement" out of cited sentence | Correct; negative search result lives only in `sourcing_note`. |
| 3 | Ohey date 2026-11-05 | Not correct as a citation date; see finding 3. |
| 4 | HTTP/2 fallback scoped | Correct against Unit 42 (newhttp3 falls back; KUKURAT has separate HTTP/2 and HTTP/3 builds). A related residual surfaced (finding 4). |
| 5 | Blocklist two of six | Correct (Pioneer, rat_http3_cc); registry matches. |
| 6 | GTIG stealth-for-velocity | Correct; the sentence closes GTIG's open-source pentest-framework section and the Detection line now uses only the three traces GTIG names. |
| 7, 17 | GTIG count, suspected | Headline says suspected, matches GTIG. Count wording acceptable; advisory only. |
| 8 | HVCI no longer bound to WinRing0 | Correct; Huntress 2026-09-03 lists the 011-branch HVCI payload and, separately, the driver in the package. |
| 9, 10 | Record summary window, nine seconds | Correct: 688,000 requests 2026-10-20 to 2026-11-16; nine seconds from the client running the pushed batch file (16:46:20.7) to the relay connection (16:46:29.1). |
| 11 | "since 20 August, more than two weeks before" | Correct (20 Aug to 8 Sep = 19 days). |
| 13 | actions[2] shortened | Acceptable: one hunt-and-isolate task. |
| 15 | Em dashes | None left outside the `## <Type> — <at>` headings. |
| 12 | BundID restoration caveat | Added correctly; two residuals (finding 5). |
| 14 | Fortinet virtual-patch sentence | Removed; the update section carries only the FGCP delta and the hardening configuration. |
| 16, 19, 20 | TGR sourcing note, Symantec relevance sentence, registry OptimJack summary | Accepted. |
| 18 | Craft tag/status | Left; restated as advisory. |

### Citation does not support the claim
- #1 F3 (low confidence), OptimJack frontmatter `summary`: "Hudson Rock recovered nine poisoned vendor files and matched archived responses on 21 named sites". Hudson Rock: Kirk's archive verification covers 15 captures spanning 16 vendor responses; "Together, the two tables identify 21 named web properties" = nine properties from eight directly recovered Optimizely assets plus 12 added by the archive check. Hootsuite, Talkwalker, Virgin Media O2, Stamps.com, Tricentis and HSBC UAE rest on direct recovery. The body states it correctly; fix the summary to "names 21 web properties".
- #2 F3 (low confidence), OptimJack Exposure line: "what counts is the file the browser receives, not the provider's console" cited to Hudson Rock. The page says "Verify what visitors actually receive after changes" and "the bytes delivered to visitors"; no mention of a provider console. Drop the contrast clause or the citation.
- #3 F3 (low confidence), OptimJack `sources[1].date` and nine inline labels "[Ohey, 2026-11-05]". The raw HTML has no datePublished, dateModified, article:published_time or dateline (JSON-LD WebPage carries no date); 2026-11-05 is the extractor's guess from the body sentence "On 5 November 2026 its switch ... read enabled: false". The label sits on events the page dates 13, 16 and 17 November, and `sourcing_note` ("carries no dateline of its own, so its citations use the page date") contradicts itself. The latest date the page text carries is 17 November. Use that with the living-page note (or drop the date from the prose label); do not keep 2026-11-05.

### Surface contradiction
- #4 F9 (low confidence), TGR-STA-0049 body, summary, registry `malware:perfectpioneer-rat`: Unit 42's body says "Both PerfectPioneer RAT and KUKURAT use HTTP/3 as the primary method", but its variant appendix says RatAAkk-tt "relies strictly on HTTP/2" and PerfectRat "relies solely on HTTP/2" (two of six; rat_http3_ls and Pioneer "HTTP/3 only"). The entry repeats the generalisation and its Detection line leads with UDP 443 egress, which does not cover the HTTP/2-only variants or the KUKURAT HTTP/2 build. One clause fixes it.
- #5 F9 (low confidence), BundID: (a) the cited aggregator says "Nach Angaben des BSI handelte es sich ... um sogenanntes Credential Stuffing", while the entry and sourcing note say the label is Handelsblatt's from government circles, not the BSI's (heise's BSI quotes do not contain it); the entry resolves this silently although it lists the aggregator as a source. (b) The title still says "password sign-in is switched off" in the present tense while the body reports a same-day restoration.

### Editorial / less-is-more flags (advisory)
- #6 F11 (low confidence), GTIG: "Three findings in GTIG's quarterly update" ends in a GTIG citation although GTIG lists five key trends; the count is the entry's selection. "Three findings from GTIG's ..." or no number.
- #7 F11 (low confidence), BundID Defender takeaway: "other stronger sign-in means" and "first containment"; heise says "eID oder andere Zugangsmittel", Handelsblatt does not mention eID. Drop "stronger".
- #8 F11 (low confidence), Craft CMS: tag `actively-exploited` and `status: exploited` over CCCS's unnamed "open source reporting" and VulnCheck's own KEV flag (ENISA and CISA KEV silent); body, summary and sourcing note hedge correctly. Restated from iteration 1; leave if intended.

### Checks that came back clean
- Updated-entry contract (4c): both records typed `update`, `updated_at` equals `at`, sections present with matching `at`, `fields` cover every changed frontmatter line in `git diff HEAD` (Fortinet: cves, evidence, body; ScreenConnect: entities, sources, evidence, actions, body, title), `discovered_at`/`run_id`/path untouched, no silent edit, deltas genuine and inline-cited, main analysis not contradicted by the new sections, ScreenConnect actions replaced not accumulated. FG-IR-26-273 timeline: "2026-11-16: Added additional information"; page text quoted verbatim in the new evidence record; all 19 critical rows match their PSIRT id, CVSS, version tables, auth (Attack Type) and "Known Exploited No".
- ScreenConnect update section: every figure matches Huntress 2026-11-16 (688,000 requests, 42 servers, 29 sources, 2026-10-20 to 2026-11-16, 16:46:20.7 to 16:46:29.1, port 8041, three October sessions, 22.x/24.2/25.8 clients, Session.db EventType 85/86). ConnectWise "Administration > Security > Roles" and 26.6.5 confirmed.
- Evidence quotes: all 25 verbatim on the live or cached pages (incl. German originals for BundID, faithful English translations).
- Dedup: no new entry overlaps an existing CVE, source or entity finding in the prior-coverage index, `state/cves_seen.json`, or the entries tree (grep for OptimJack, StorifyMe, BundID, PerfectPioneer, KUKURAT, exploit_agent, SOMBERMEME, Orion RabbitMQ, CVE-2026-123488 finds only this run's entries; the 2026-08-16 Jewelbug entry is a distinct finding sharing the actor alias).
- Registry: 16 `entities_added` match the diff; the `actor:jewelbug` alias additions (TGR-STA-0049, Ink Dragon) rest on Unit 42's own alias list, disclosed in the sourcing note; relations are typed and sourced; ATT&CK pin v20.1 maps T1574.001 to the merged DLL technique, so side-loading ids are correct.
- Classification, priority, style: Admiralty codes inside vocabulary and proportionate to the single- or multi-source basis; no watchlist or org_triage; no IOCs; no KEV deadline as an action reason; no workflow vocabulary in reader-facing text; priorities calibrated (OptimJack high with Basel capture and e-government script lesson; BundID routine with a stated vector).
- Run record: counts, durations (03:55:48 to 04:48:00 = 3132 s), `entities_added`, dispositions and the iteration-1 remediation notes match the files on disk.
- Missed angles (F10): none evidenced. Searches for in-window Swiss municipal or cantonal incidents and exploited zero-days surfaced only items already in the store (Patch Tuesday, Chrome CVE-2026-125350, Cisco ISE 2026-09-17 entry, Node2Shell entries) or undated pages; Oracle CSPU and TYPO3 are correctly held for the next fire.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 2, advisory: 3). All five truth/editorial items are low confidence and small; the iteration-1 remediations themselves are correct except the Ohey citation date (finding 3), which replaced one imperfect date with an extractor artefact.

### Findings summary (machine-readable)
See `work/2026-11-17T0355Z-intel/verification.iter2.findings.yaml` (8 records).
