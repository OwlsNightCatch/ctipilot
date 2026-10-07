**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-07T05:09:26Z · ended_at=2026-10-07T05:28:02Z · duration_seconds=1116

## Verification report — 2026-10-07T0404Z-intel (iteration 1)

Scope: all 211 ledger claims (first pass, no deltas block), 3 new entries, 6 updated entries (whole file plus `git diff HEAD`), run record, registry additions. Every cited page was fetched this iteration (extract; bridge `url --direct` for the DR live blog and Zammad API; `cisa-kev` for KEV). Claim verdicts: 193 ok, 18 non-ok (see claims file).

### Broken / unreachable URLs
None. Every cited URL resolved and lands on a specific page.

### Generic / oversight URLs (replace with specific article)
- #1 (low confidence) F2, 2026-10-02/zammad: `https://api.github.com/repos/zammad/zammad/security-advisories?per_page=100` is a raw JSON listing of 76 advisories (27 published 2026-10-06). The counts it supports are correct (27; critical 2, high 12, medium 10, low 3; no cve_id; ranges end at 7.2.0). Reader-facing link is unfollowable; consider the repository's advisory listing page.

### Citation does not support the claim
- #2 F3, 2026-10-06/atlassian (body para 2 and sourcing_note): "its Crowd ticket lists 7.1.6 as the fixed 7.1 build where the advisory lists 7.1.7" (CWD-6610). Live ticket: Fixed Versions table "Crowd Data Center | 6.3.7 7.0.3 7.1.7 7.2.4"; Fix Version/s = 6.3.7, 7.2.4, 7.0.3, 7.1.7; 7.1.6 is only under Affects Version/s. The gate's cached copy (quote-bodies/3c76dca03120b7e8.extract.txt, fetched 05:06 today) agrees. Delete the clause in both places.
- #3 F3, 2026-10-02/zammad Exposure: "Zammad says its SaaS instances are already patched, and the 27 advisories ... affect every self-hosted version up to 7.2.0" cited to the GitHub API records. SaaS statement is on the 7.2.1 release page, not in the records; GHSA-4r9g-r4wx-44p6 range is ">= 7.0.0, <= 7.2.0", so "every" is broad.
- #4 F3, 2026-10-02/zammad Defender takeaway: "7.2.0 is affected by the advisories published on 2026-10-06" cited to the 7.2.1 release page, which names no affected versions. Re-cite to the advisory records.
- #5 (low confidence) F3, atlassian Exposure + actions[1]: Crowd password in `crowd.properties` generalised to "every Jira, Confluence or Bitbucket instance"; watchTowr demonstrated Jira only.
- #6 (low confidence) F3, blinder-tunnel Detection: "which Unit 42 names as the sideload signal" rewords Unit 42's "monitoring binaries that load unknown or non-standard DLLs outside of system directories"; sourcing_note "not strong enough to attribute" is the entry's gloss on "low confidence overlaps".

### Unsupported / hallucinated facts
- #7 (low confidence) F4, zammad headline/summary: "the root flaw still unfixed" / "so no fix exists yet" vs the entry's own update: "whether 7.2.1 closes the exploited root escalation is not stated". Last fix-status source predates 7.2.1.
- #8 (low confidence) F4, zammad Exposure: "the two critical ones need public sign-up enabled on the customer portal" is stated by none of the three cited pages; GHSA-79wh's second flaw needs only a customer account.
- #9 F4, liechtenstein body para 2 (supersession): "the register is unavailable to external users through the LLV.li portal" vs new section "Betrieb ... am 5. Oktober in eingeschränkter Form wieder aufgenommen". Undated present-tense sentence now false.
- #10 (low confidence) F4, liechtenstein Update 2026-09-01 Defender takeaway: "no per-account rate limit, and produced no alert across several hours" is in no cited source; the added 2026-08-19 release gives "faulty authorisation-checking logic ... not a classic software vulnerability", at odds with "not a single flaw" and with the summary's "through a vulnerability".
- #11 (low confidence) F4, shinyhunters Correction 2026-09-30: "the FBI says the point of breach ... is still undetermined" is present tense; the new Update says "This replaces" it.
- #12 (low confidence) F4, ninja-forms Detection/Triage: "inside one page view" is not stated (Patchstack: "created around the time an administrator viewed"); "without a visit to the Plugins screen" contradicts the script's own request to `/wp-admin/plugin-install.php?tab=upload`.
- #13 (low confidence) F4, azazel summary: "a decrypted configuration key" inverts CloudSEK's "recovered the master key and bulk-decrypted every protected value".

### Analytical-link-as-fact
- #14 (low confidence) F13, shinyhunters Update 2026-10-07: "SecurityWeek says this is the member known as Rey, whom Krebs's sources described above as directing the group's operations". SecurityWeek (aka Rey, "alleged leader") never mentions Krebs; Krebs describes Rey as a teenager from Amman and reports no arrest. The bridge between the two is the entry's.
- #15 (low confidence) F13, ninja-forms summary: "Patchstack reports that ... one actor". Patchstack says "one payload", "one campaign"; "same threat actor" is BleepingComputer's inference.
- #16 (low confidence) F13, telerik Improvement: "the flag means the host is a possible ransomware staging point". KEV's flag is about the CVE; no cited source ties these intrusions to ransomware.

### Quantifier without source
- #17 (low confidence) F14, azazel body: "the first operational use of MCP as an attack execution channel it knows of". CloudSEK: "has not identified prior public reporting" (first reported, not first used).

### Claims missing inline citation
- #18 (low confidence) F5, denmark Defender takeaway: "which the Danish authorities now say it no longer is" (true per DR, uncited).

### Action-item discipline
- #19 (low confidence) F18, ninja-forms actions[0]: second half restates the body's Detection guidance.
- #20 (low confidence) F18, liechtenstein actions[0]: "over the coming days" is stale two months on.

### Editorial / less-is-more flags (advisory)
- #21 F11: reader-facing sourcing_note narrates fetch outcomes: Liechtenstein "whose own text could not be read"; Telerik "could not be re-read when the text was written, so it rests on an earlier verbatim capture" (stale: asec.ahnlab.com/en/95561/ extracts cleanly today and matches the entry); ShinyHunters "the Reuters report itself could not be read". Also "this entry previously recorded" (Liechtenstein 2026-09-01 section and its record summary).
- #22 F11: denmark main analysis and the new Update repeat the Datatilsynet and "expensive invoice" facts.
- #23 F11: azazel entities omit `actor:thegentlemen` although the registry links azazel to it.
- #24 (low confidence) F11: liechtenstein record typed `improvement` also carries fresh 2026-10-06 developments.

### Verified without findings (for the record)
- Ninja Forms/WPC: all Patchstack facts, CVSS 7.2 (Wordfence CNA JSON, Patchstack lists 7.1), fixed versions, BleepingComputer's "authenticated session" contradiction (handled in sourcing_note and run note), 4 evidence quotes verbatim. Priority high is defensible (exploited, patch does not evict, widely deployed).
- Blinder Tunnel and Azazel: all other claims, 4 and 3 evidence quotes verbatim, techniques mapped to behaviours in the sources, classification B/2 for single vendor sources. Nexus is thin (Iraq/Israel/UAE; GitLab CI/CD affects the constituency), notable is defensible.
- Atlassian update: watchTowr root cause, request shapes, Crowd chain, GitHub checker, Register "Monday" email, all fixed-version numbers, CVSS 4.0 vector, `cves[]`; record fields match the diff.
- Zammad: 27 advisories, severities 2/12/10/3, no CVE ids, ranges, GHSA critical descriptions, NCSC-NL, DIVD, KEV, CVSS values.
- Denmark: all ministry, Ritzau, Datatilsynet and DR claims; 4 evidence quotes and originals verbatim.
- ShinyHunters: Nextgov, SecurityWeek, BleepingComputer, TechCrunch, Axios, CyberScoop, Krebs, FBI release; new evidence quotes verbatim.
- Liechtenstein: 2026-08-19 release, Inside IT 2026-10-06, both new quotes verbatim.
- Telerik: KEV record (dateAdded 2021-11-03, knownRansomwareCampaignUse Known, catalog 2026.10.04), ASEC page.
- Run record: KEV sweep and ransomware-flag list match the 2026.10.04 catalog; counts and entity list match the registry diff.
- Missed angles: none found. A scan of The Register, BleepingComputer, SecurityWeek and The Hacker News feeds for the window shows only items the run already carries or dropped with reasons (ClickFix cache lead is noted in S3); coverage looks complete for the critical/high signal.

### Verdict
NEEDS_FIXES (truth: 17, editorial: 3, advisory: 4)

The confident items to fix first: #2 (Crowd ticket 7.1.6), #3 and #4 (Zammad citations), #9 (Liechtenstein "is unavailable"). The rest are low-confidence and may be narrowed or left.

### Findings summary (machine-readable)
See `work/2026-10-07T0404Z-intel/verification.iter1.findings.yaml` (24 records) and `verification.iter1.claims.yaml` (211 rows).
