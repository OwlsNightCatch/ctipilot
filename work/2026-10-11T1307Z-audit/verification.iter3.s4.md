**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-11T16:59:07Z · ended_at=2026-10-11T17:15:20Z · duration_seconds=973

## Verification report — 2026-10-11T1307Z-audit (iteration 3, slice s4)

Scope: 10 entries (9 updated, 1 new), 201 ledger claims, every claim walked (197 ok, 3 F3, 1 F5; rows in `verification.iter3.s4.claims.yaml`). 20 of the claims are those changed since iteration 2; all 201 were answered, not sampled. Every cited page was fetched this iteration (45 URLs appended to `url-liveness.tsv`): `extract` for web pages, `url` for raw HTML where a score or footer was needed (GHSA severity and vectors, php.net ChangeLog dates, PK Softech footer), `pdf` for the IC3 advisory and the BPK notice, `ncsc-csh post 12622`, `cisa-kev`, and the CNA JSON records for the three PHP CVEs. CVSS 4.0 vectors for the PHP CVEs were recomputed with the `cvss` library (7261 and 7262 base 6.3; the 7262 CNA record carries E:P and shows 2.9). The Register pages and the BLVK PDF were readable only through a fallback reader or raw HTML (stated in the claim rows where it matters); the researcher's ShieldCrash GitHub repository now returns 404, so the repo quote in the 2026-09-13 ShieldBreak section (an earlier fire's text) is unreadable today and SOCRadar's paraphrase is what could be checked.

### Prior-iteration deltas (walked first)

Applied and confirmed on disk and against the source:
- NeedyMantis tags: `tags: [china-nexus]`; espionage and supply-chain gone. Microsoft: 'not observed NeedyMantis itself being distributed through a supply chain compromise'; China-origin assessed, not attributed to a Chinese nation-state actor.
- PHP summary: 'PHP's advisory rates it High, while its CVE record scores 9.5 under CVSS 4.0, with high attack complexity'. GHSA-85c2 shows 'Severity High' with no score; the CNA record shows baseScore 9.5, AC:H, AT:P.
- DAEMON Tools: startup behaviour restated as a backdoor thread beaconing to a typosquatted domain, shell execution only on a server command (Securelist); `envchk.exe` and `cdg.exe` absent from reader-facing text.
- Entra F5: the Detection sentence now ends with its LevelBlue link (but see F3 #2).
- LiteLLM: `event_date: 2026-06-08` = KEV dateAdded (cisa-kev bridge); record summary now names the action trim and the KEV citation (diff: references, actions, body, event_date, matching `fields`).
- Canvas: the agreement sentence now matches Inside Higher Ed ('received digital confirmation of data destruction (shred logs)', assurance no customers will be extorted, no monetary value disclosed) and drops Infosecurity; the three disconnection clauses cite NL Times (all seven Dutch universities) and Techzine (VU Amsterdam notified the Dutch DPA) only; the 2026-05-09 section says 'Instructure later attributed ...'.
- WaterPlum takeaway: first control now addresses employees approached by recruiters; the Correction section cites heise ('Im Verlauf des vermeintlichen Online-Bewerbungsprozesses soll der Job-Kandidat ... eine Datei herunterladen').
- Mandiant date: body, citations and `sources[].date` say September 2026; Help Net Security 2026-09-16 cited. `event_date` is still 2026-09-15 (F11 #10).
- ShieldBreak F8: Current state, Exposure, Detection and Defender takeaway lines added; engine 1.1.26080.3 and 1.26070.7 match MSRC; LevelBlue supports the Detection line.

Declined, judged:
- Publica F16 (priority): the conclusion stays within the 'doubt resolves to notable' rule (no fund has said which member data left; Publica says it is 'noch unklar'), so I raise no finding. Two details of the stated rationale are off (the entry now carries two actions, not 'its single action'; the Confederation's release is headlined 'Datenabfluss bestätigt') but neither changes the calibration call.
- ShieldBreak F11 (phoneinfo.dll indicator): the rationale does not hold; re-raised as F11 #7 (advisory).

### Citation does not support the claim
- **F3 #1** `waterplum-...` Triage line: 'the advisory names what BeaverTail, InvisibleFerret and OtterCookie collect (browser authentication data, clipboard contents, keystrokes, screenshots and wallet data)'. The advisory lists those classes once as 'Other sensitive data targeted for exfiltration' by the actors' infostealers and gives no per-family collection list (InvisibleFerret is 'a Python-based backdoor', BeaverTail 'JavaScript-based malware hidden inside NPM packages'); 'freshly cloned' is not in the advisory. Written by this fire's rewrite; the same family-level wording is in the section and record summary.
- **F3 #2** `microsoft-entra-id-...` Detection sentence (low confidence): status string 'not a member of the password reset group' is not LevelBlue's wording ('user is not member of the password reset users group'); 'from a limited source population' is on no cited page.
- **F3 #5** `mandiant-ai-...` (low confidence) 'drawn from real Mandiant incident-response and offensive-security engagements' has no link and is not stated by the report for cases 6, 7 and 8.

### Unsupported / hallucinated facts
- **F4 #3** `mandiant-ai-...` (low confidence) title 'eight frontline case studies of AI agents weaponized inside real intrusions and red-team engagements' (and summary 'case studies of AI-agent abuse') against the corrected body: case 6 'is an operational-resilience failure rather than an external attack', case 7 'is a weakness Mandiant identified, not an observed leak', case 8 a defender-side detection. Record `fields` does not name title.
- **F4 #4** `shieldbreak-...` (low confidence) evidence quote 'We are working to provide a high quality security update that addresses this vulnerability.' (publisher MSRC) is absent from the current MSRC page, which now says Microsoft 'has released an update ... that addresses the vulnerability'.

### Claims missing inline citation
- **F5 #6** `cve-2026-42271-...` (low confidence) 'the open-source AI gateway/proxy widely deployed to multiplex LLM API calls in enterprise AI stacks' is carried by none of the cited pages.

### Editorial / less-is-more flags (advisory)
- **F11 #7** ShieldBreak 2026-08-24 section keeps `phoneinfo.dll` ('strongest single indicator') and WD_SCAN; LevelBlue lists the DLL under File-Based IOCs and says it does not exist natively, so the decline rationale ('a platform artifact') fails.
- **F11 #8** ShieldBreak 2026-08-18 and 2026-08-21 takeaways still end on 'nothing to patch' with no pointer (the 2026-08-24 section got one).
- **F11 #9** Entra: double-quoted 'SSPR not enabled for this user' and 'not a member of the scoped access group' are not on the cited page.
- **F11 #10** Mandiant `event_date: 2026-09-15` is an unevidenced day (first dated evidence 2026-09-16).
- **F11 #11** LiteLLM `sourcing_note` is migration jargon ('migration: evidence backfilled from v2 brief body'); the summary table carries a Check Point CVE-2026-50751 row that has its own entry; em dashes remain.
- **F11 #12** Uncited `sources[]` after the rewrites: Canvas (Infosecurity), DAEMON (Kaspersky blog, Help Net Security), WaterPlum (The Record).
- **F11 #13** Publica Improvement section only repeats the Exposure line.

### Missed angles
None found for this slice. Beyond Gravity (federally owned Swiss space supplier, intrusion disclosed 2026-10-02, BACS and Mandiant involved; Netzwoche 2026-10-06) and the Ricardo account breach (Inside IT) surfaced while reading, but Beyond Gravity is a deliberate held backlog row in the run's own notes and Ricardo is a consumer marketplace with no constituency nexus; coverage of the slice's topics looks complete.

### Verdict
NEEDS_FIXES (truth: 5, editorial: 1, advisory: 7). F3 #1 is the firmest truth finding (the advisory text read this iteration does not map the data classes to the three named families); F3 #2, F3 #5, F4 #3, F4 #4 and F5 #6 are low confidence.

### Findings summary (machine-readable)
See `work/2026-10-11T1307Z-audit/verification.iter3.s4.findings.yaml` (13 records).
