**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-26T06:07:57Z · ended_at=2026-11-26T06:30:45Z · duration_seconds=1368

## Verification report — 2026-11-26T0356Z-intel (iteration 3)

Scope: post-fix pass. All 214 ledger claims have a verdict row in `verification.iter3.claims.yaml` (207 ok, 4 F3, 2 F4, 1 F14; passages machine-checked as substrings of pages fetched or saved by the gate this run). That covers the 22 changed claims, every claim of the entries the deltas block names (Claroty, Danfoss incident, ARTEX, Java4Shell, nginx2root, GeoServer, and the new Okta, SEPPmail, Juniper, 1Password entries) and all claims of Mitel, Drupal and PolinRider as well, which is more than the quarter sample. Fetched this iteration: Claroty Team82, Danfoss DSA-2025-03-01 and DSA-2025-08-01, DSA-2023-08-01 (gate-saved body), Synacktiv PDF, CISA KEV catalogue (bridge), CISA alert pages of 2026-11-24 and 11-25 (gate-saved WebFetch bodies), CISA ICSA-26-328-03 CSAF, ENISA EUVD for CVE-2025-41450/41451/41452, EUVD-2026-112215/112212/130382, BSI CSAF WID-SEC-W-2026-4234, FIRST EPSS series, Cisco Java4Shell and nginx advisories (raw header read for publication dates), HPE HPESBNW05193, Fortinet FG-IR-26-278, PAN CVE-2026-123633 (raw timeline), Unit 42, Xint, CERT.at, Wiz, Okta blog and Permiso acquisition release, SEPPmail revision history, 1Password post and BleepingComputer, watchTowr FAQ, The Hacker News, Eye Security, GHSA-wc3v/39mw/9wf2, NCSC.ch advisory 13242 (ncsc-csh), Mitel MISA-2026-0012 and 0006, GTIG, Microsoft ARTEX guide and North Korea report, The Record, Nextgov, Macau Business, Microsoft threat-actor naming page, SafeDep, StepSecurity x2, Searchlight, NCSC-NL, Apiiro, Sonatype, Censys (gate-saved body), Drupal SA-CORE-2026-017/018/019 (WebFetch; quotes only, paraphrase flagged), Juniper JSA112183 (WebFetch: loading shell, unreadable). Two WebSearches for in-window gaps found nothing new.

### Prior-iteration deltas

Walked all 17 items against the pages above.
- #1 (Claroty F3/F9): Claroty's own statements now cite Claroty and match its page ("results in a fully authenticated administrative session"); the web-report impact, CWE-305-era wording and "build 4.2" cite DSA-2025-03-01 and the KEV record and match ("Install the latest patch with number 4.2"); headline, summary and sourcing note carry both impact statements. The rewritten chain sentence is a new defect: see finding 1.
- #2 vectors: confirmed. EUVD CNA records: CVE-2025-41450 `CVSS:3.1/.../UI:R/...`; CVE-2025-41451 and 41452 `CVSS:4.0/.../UI:A/...`; the sourcing note states one rule for all three.
- #3 Triage: confirmed against "likely intended for vendor support or maintenance".
- #4 Java4Shell Cisco: sentence fixed, but the citation label 2026-11-20 remains (page: first published 2026-11-18, last updated 2026-11-23, 1.3 on 2026-11-20); finding 5, low confidence.
- #5 nginx2root PAN: confirmed. Timeline "2026-11-24 Removed ETA for 12.1.7-h15, 11.2.10-h19, 11.2.13-h6 as these versions are released"; initial publication 2026-11-20 matches the label.
- #6 Juniper EUVD dates: confirmed, both records datePublished Oct 28, 2026.
- #7 1Password takeaway: confirmed against the four "What you can do" items.
- #8 GeoServer: confirmed. watchTowr FAQ prose names all five CVEs; The Hacker News two; NCSC.ch one; the sourcing note states the rule.
- #9 run-record notes: confirmed except the EPSS aside (finding 10).
- #11 ARTEX/GTIG: GTIG's statement kept and attributed ("a commercial version dubbed ARTEX PRO"), ThreatBook's release (Macau Business, 2026-10-16) and Microsoft cited correctly; adjacency nit in finding 6.
- #12 SEPPmail takeaway aligned with notable; #14 build 4.2 cited; #15 store cross-references gone (grep clean); #16 Okta "very likely" carried in title, headline, summary, body; #17 alias note present and true (Microsoft naming page: Andariel under Onyx Sleet, FamousSparrow and GhostEmperor under Salt Typhoon).

### Citation does not support the claim

1. **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce** — `body` and `sourcing_note` (F3)
   - Claim: "Claroty says its findings combine into attack chains but does not state that the code-of-the-day bypass reaches those two primitives in practice, so the chain is treated as auth-gated unless a combined path is confirmed ([Claroty Team82, 2026-08-09](...))"
   - Evidence / fix: The cited page: "Successfully bypassing authentication dramatically expanded the attack surface available for analysis. Instead of being limited to the small number of unauthenticated endpoints, we gained access to the device's full administrative interface and every management function it exposed", the functions listed include "email notifications", and the next section starts "The SMTP Email configuration page quickly stood out" (the CVE-2025-41451 injection). The Censys page already cited on the Danfoss incident entry says "In August 2026, researchers at Claroty demonstrated how CVE-2025-41450 and CVE-2025-41451 could be chained together to achieve remote code execution." The "does not state" claim and the auth-gated conclusion understate a KEV-listed bypass for a SOC that reads cves[] (41451 shows post-auth). Rewrite: Claroty reports the bypass opened every management function, including the email-notification page where it found the injection.

2. **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce** — `body` (F3, low confidence)
   - Claim: "(CWE-77 OS Command Injection, CVSS 3.1 7.6)" and "(CWE-15 ..., CVSS 3.1 5.4)" cited to Claroty.
   - Evidence / fix: Claroty prints "CVSS v3: 7.6" and "CVSS v3: 5.4"; no cited page says 3.1.

5. **2026-11-18/cve-2026-114938-java4shell-openjdk-avx512-base64-decoder-rce** — `body`, update section, `sources[]` (F3, low confidence)
   - Claim: "Cisco's advisory now reads version 1.4: ..." ([Cisco, 2026-11-20]); "Cisco's advisory (version 1.4) lists ..." ([Cisco, 2026-11-20]); sources[] date 2026-11-20.
   - Evidence / fix: Cisco's header: "First Published: 2026 November 18 16:00 GMT", "Last Updated: 2026 November 23 20:32 GMT"; revision table 1.3 is 2026-11-20. The label matches neither publication (2 days) nor the 1.4 text (3 days). Use 2026-11-18 or 2026-11-23.

6. **2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse** — `update-section 2026-11-01` (F3, low confidence)
   - Claim: "including a commercial version GTIG calls ARTEX PRO, which ThreatBook's own release, covered in the update of 2026-11-26, presents as the vendor's product ([GTIG and Mandiant, 2026-10-31])"
   - Evidence / fix: GTIG carries "community forks, including localized variations such as ScopeWeaver and a commercial version dubbed ARTEX PRO" and nothing on ThreatBook. The attribution is explicit and the substance holds; split the sentence and cite Macau Business for the ThreatBook clause, without the same-entry pointer.

### Unsupported / hallucinated facts

3. **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce** — `sourcing_note` (F4)
   - Claim: "CVE identifiers are 2025-dated despite the 2026-08-09 public disclosure: reserved-then-disclosed-later is a normal CNA pattern, not a dating error."
   - Evidence / fix: Danfoss DSA-2025-03-01 "24 March, 2025: Publication"; DSA-2025-08-01 "01 August, 2025: Publication"; ENISA EUVD-2025-13996 datePublished "May 8, 2025"; EUVD-2025-25499 "Aug 22, 2025". The flaws were published and patched in 2025; Claroty's post is a later write-up. The mechanism claimed is in no source. State the 2025 publication dates instead.

4. **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce** — `frontmatter` (F4, low confidence)
   - Claim: `sectors: [healthcare, energy]`
   - Evidence / fix: Claroty: "supermarkets, cold-storage facilities, warehouses, and other commercial environments"; no cited source names healthcare or energy. The taxonomy has `retail`.

7. **2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse** — `update-section 2026-11-26` (F4, low confidence)
   - Claim: Microsoft "assesses that North Korean AI-enabled operations remain human-directed"
   - Evidence / fix: Microsoft: "...while human operators likely continue to direct intent and objectives." Hedge dropped and an observation recast as an assessment.

9. **2026-11-26/juniper-session-smart-cve-2026-103406-unauth-root-rce** — `body` (F4, low confidence)
   - Claim: "The record points to Juniper's bulletin JSA112183 of 2026-10-28, which carries the fix and could not be read."
   - Evidence / fix: ENISA gives the reference "https://supportportal.juniper.net/JSA112183" and a CVE-record datePublished of Oct 28, 2026; the bulletin (WebFetch: loading shell) was never read, so its date and "carries the fix" are inference. Say the CVE record was published on 2026-10-28.

10. **runs/2026-11-26/2026-11-26T0356Z-intel.md** — `run-record-notes` (F4, low confidence)
   - Claim: "EUVD's 0.52 is not an EPSS probability"
   - Evidence / fix: FIRST: 0.00516 on 2026-11-24, 0.0086 on 2026-11-25; EUVD shows "epss":0.86 today, the same value in percent, so 0.52 is the previous day's EPSS in percent. The entry's 0.0086 is right; correct the reason.

### Quantifier without source

8. **2026-11-26/juniper-session-smart-cve-2026-103406-unauth-root-rce** — `body` (F14, low confidence)
   - Claim: "No source names an actor, a victim, the number of compromised systems, the date of first exploitation or the attack technique."
   - Evidence / fix: The cited ENISA record carries `"exploitedSince":"Nov 25, 2026, 12:00:00 AM"`, an aggregator field that follows the KEV listing and cannot be a first-exploitation date (BSI flagged exploitation on 2026-11-24). Name the field or qualify the sentence.

### Surface contradiction

11. **2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack** — `update-section 2026-11-26` (F9, low confidence)
   - Claim: "CVE-2025-41450, an authentication bypass that generates a web report exposing internal IP addresses, usernames and store names" against the entry's Censys paragraph: Censys "describes as letting an unauthenticated actor log in as an administrator with a code computed from the current calendar date".
   - Evidence / fix: Two descriptions of one CVE in one entry with no Contradiction line (the Claroty entry states the disagreement). Add one sentence.

### Editorial / less-is-more flags (advisory)

12. (F11) **2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce**: the record summary states the web-report impact unqualified ("the code-of-the-day authentication bypass that discloses internal IP addresses, usernames and store names"); the sourcing_note has "; The vector fields" (capital after a semicolon) and runs seven sentences.
13. (F11) **Juniper and Drupal sourcing_note**: "which no transport could read (its support portal returns only an application shell)"; "The Drupal advisory pages answered the fetch tools with a client challenge". Transport narration in a reader field.
14. (F11) **ARTEX 2026-11-01 section**: "covered in the update of 2026-11-26" points to another section of the same entry; fold into finding 6.

### Missed angles

None found. KEV additions of 2026-11-25 all have a disposition (Juniper new; Mitel, Danfoss, Claroty updated; Xen Orchestra already covered); two WebSearches (exploited vulnerabilities of 2026-11-26; BACS/NCSC warnings of November 2026) found no in-window item beyond the store. Coverage looks complete.

### Checked and clean

Classification present and in vocabulary on all four new entries (Juniper A/2, SEPPmail A/2, 1Password B/2, Okta B/2) with single-source entries rated 2; no `org_triage`, no watchlist use; priorities consistent (Juniper and Claroty high on KEV, SEPPmail, Okta, 1Password notable); `verification` values fit the source counts; no IOCs, no em dashes in reader text outside changelog headings; `updated_at` and record `at` agree on all nine updated entries; actions are single, concrete and not body restatements.

### Verdict

NEEDS_FIXES (truth: 10, editorial: 1, advisory: 3)

The firm defect is finding 1: the Claroty chain wording introduced to answer the iteration-2 contradiction finding is itself unsupported by the cited Claroty page and by the Censys page already in the store; finding 3 is also evidenced. The remaining truth items are small or low confidence and marked so.

### Findings summary (machine-readable)

See `work/2026-11-26T0356Z-intel/verification.iter3.findings.yaml` (14 records).
