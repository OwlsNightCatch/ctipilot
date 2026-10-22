**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-22T12:09:45Z · ended_at=2026-10-22T12:38:37Z · duration_seconds=1732

## Verification report — 2026-10-21T1148Z-audit (iteration 2)

Scope: post-fix pass, no confirmation pass follows. All 135 claims of `claims.changed.iter2.yaml` carry a verdict row in `verification.iter2.claims.yaml` (128 ok, 6 F3, 1 F4). Deltas: 101 rows with `verify_in_this_iteration: true` checked (96 held, 5 failed: s1#42, s2#13, s3#10, s3#27, s3#31); the 16 declined rows were not re-raised (no page evidence that a rebuttal is wrong). Then a cold read of the 49 entries the changed claims sit in, a literal check of every `evidence[]` quote of those entries against cached or live pages (217 literal matches; 3 misses were page-escaping artefacts, the Computable quote matches the live fetch), a scan of the run's added entry text for IOCs and em dashes (none outside verbatim quotes), and checks of the run record and wave report counts against disk.

### Citation does not support the claim
- #1 F3 `2026-05-22/calypso-red-lamassu-bronze-medley-deploys-showboat-linux-and`, Correction, claim 5104ea6f4e: "The campaign dates from at least mid-2022, whereas PwC has tracked Red Lamassu since 2019; JFMBackdoor offers remote shell access, ... self-removal ([PwC, 2026-05-21](...red-lamassu-open-season.html))". The PwC page has "since 2019" and the capability list but no 2022 date. "The campaign has been active since at least mid-2022" is on Lumen's page, which is not cited at this clause.
- #2 F3 (low confidence) `2026-05-13/bwh-hotels-...`, claims ed80615e6a and d0aa77e5de: "with no payment, bank or passport data involved ([The Register])". WebFetch of The Register: "No payment or bank details were involved." and "Passport data is not mentioned." Passport absence is inference from the field list, cited as stated.
- #3 F3 (low confidence) `2026-05-16/amd-sb-7052-...`, claim c0cb72e3a0 and the frontmatter summary: "...EPYC 7002 and EPYC Embedded 7002 ... which Microsoft says the May 2026 Windows builds enable". AMD table: "EPYC 7002 | OS Update | Contact your OS Vendor". MSRC: "certain processor models offered by AMD. The mitigation for this vulnerability requires a Windows update." No page links the Windows update to EPYC 7002 / Embedded 7002; s2#13's inference survives in the summaries.
- #4 F3 (low confidence) `2026-05-21/cve-2026-45829-chromadb-...`, claim 14627a4b5b: "Hadrian ... calls it \"ChromaToast\"". Hadrian: "reported on 2025-11-28 by HiddenLayer (\"ChromaToast\")" and links HiddenLayer's "ChromaToast Served Pre-Auth"; the name is HiddenLayer's.
- #5 F3 (low confidence) `2026-05-20/drupal-core-highly-critical-...`, claim 80f1e9f3db: "Symfony and Twig security updates that apply to every site, whatever its database ([SA-CORE-2026-004])". SA: "Depending on your site configuration and contrib modules, you may be vulnerable to one or more of these upstream issues, so updating ... is highly recommended whether the SQL Injection vulnerability affects you or not."

### Unsupported / hallucinated facts
- #6 F4 `2026-05-14/cve-2026-8043-ivanti-xtraction-...`, claim 70fbc86db6: the record summary (2026-10-21T20:20:51Z) is the TrickMo entry's summary verbatim ("ThreatFabric's point about TrickMo's TON transport is that ..."). Nothing in it concerns Ivanti. The wave report row for this entry holds the right text. Regression from the s1#42 remediation.
- #7 F4 run record "Scope and outcome" and wave report § Registry and state changes: "398 technique mappings" (disk: 399, 171 distinct; `main/stats.py` prints 399), "21 CVEs added" (23: plus CVE-2026-45543, CVE-2026-45544), "39 product entities" (40: plus product:sonicwall-sma-100), "39 existing summaries rewritten" (40: plus tool:gemstuffer-rubygems-2026). The counts predate the iteration 1 fixes.
- #8 F4 wave report per-entry table: six rows still carry pre-remediation record text; four state what iteration 1 retracted: cPanel ("cPanel scores CVE-2026-29202 ... at 5.3"), BWH ("owns three brands"), Datadog ("released the Shai-Hulud framework source deliberately"), Sparx ("all five Sparx CVEs carry CNA scores"). Regenerate from the final summaries.
- #9 F4 (low confidence) `2026-05-14/gemstuffer-...`, techniques[] T1567.004 = "Exfiltration Over Webhook" in the pinned dataset; no cited source mentions a webhook.

### Claims missing inline citation
- #10 F5 (low confidence) `2026-05-12/ico-fines-south-staffordshire-...`, cves[CVE-2020-1472].status carries `cisa-kev` with no KEV source (the cached feed lists it, dateAdded 2021-11-03).

### Single-source items missing [SINGLE-SOURCE] flag
- #11 F12 (low confidence) `2026-05-17/cve-2026-41225-f5-big-ip-...`: `verification: multi-source` while the sourcing_note says F5 is the vendor and numbering authority and the others restate it; Composer and Sophos were flipped to single-source (s2#30) for the same shape.

### Org-triage line missing / inconsistent
- #12 F16 (low confidence) `2026-05-10/groupe-3r-...` priority high; the entry says "the case changes no patching or detection decision for other healthcare operators".

### Editorial / less-is-more flags (advisory)
- #13 F11 `2026-05-21/cve-2026-45829-chromadb-...` record summary: "...and the analysis gains exposure, detection, triage and takeaway guidance." s3#27 names it among the 17 rewritten summaries; it is not in `main/narrating-summaries.json` and the text remains.
- #14 F11 `2026-05-21/verizon-2026-dbir-...` record summary: "...the full report replaces the landing page as a source, and as an annual report ... it moves from a high-priority deep dive to a notable entry." Same s3#27 gap.
- #15 F11 `2026-05-14/cve-2026-8043-ivanti-...` sourcing_note: "Ivanti's per-product advisories did not render for reading." (fetch-failure narration, the s2#40 pattern).
- #16 F11 (low confidence, pre-existing) `2026-05-12/gtig-ai-threat-tracker-...` Defender takeaway: "cloud keys, GitHub tokens and AI API secrets those environments held as stolen"; GTIG ties AI API secrets only to the LiteLLM compromise.

### Deltas that failed
- s1#42 (Ivanti): section narration dropped, but the record summary was overwritten with TrickMo text (#6).
- s2#13 (AMD): takeaway fixed; the summary and record summary keep the EPYC-to-Windows inference (#3).
- s3#10 (Drupal): SA wording used, but "apply to every site" overstates it (#5).
- s3#27 (17 record summaries): chromadb and verizon still narrate (#13, #14).
- s3#31 (counts): still off by one (#7).

### Missed angles
None new beyond the run's own W6-08 note (CVE-2026-41940 cPanel); coverage of the window's critical/high signal looks complete for the wave's scope.

### Verdict
NEEDS_FIXES (truth: 9, editorial: 3, advisory: 4)

### Findings summary (machine-readable)
See `work/2026-10-21T1148Z-audit/verification.iter2.findings.yaml` (16 records).
