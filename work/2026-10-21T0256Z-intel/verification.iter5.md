**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-21T05:28:09Z · ended_at=2026-10-21T05:47:23Z · duration_seconds=1154

## Verification report — 2026-10-21T0256Z-intel (iteration 5)

Scope: post-fix cold pass. All 230 ledger claims carry a verdict row in `verification.iter5.claims.yaml` (the 13 changed claims, every claim of the entries remediated in iteration 4 and of the four updated entries' new sections, plus the remaining older claims of PAN-OS, Metabase, Publica and ConnectWise, a seeded 24-claim random draw of which was walked first and the rest checked where the source was already open). Pages read live this iteration: php.net archive, CERT-EU, Sansec, Wordfence, cisa.gov AA26-293A (WebFetch, twice), CISA KEV JSON (`cisa-kev`, catalogVersion 2026.10.20), CISA alert 2026-08-11 (WebFetch), Cisco and SonicWall advisories, Oracle CPU (1295 risk-matrix rows re-parsed: 112 at 9.0 or higher, 90 unauthenticated network, 73 distinct ids, the six 10.0 rows and the WebLogic/IAM/OAM rows hold), Symantec, Recorded Future, Google, Mozilla, Go announcement, BleepingComputer (eMudhra, UpdraftCentral, Metabase, ConnectWise), the eMudhra tracker, CVE.org API (both PHP ids 404, CVE-2026-111943 published), TeamUpdraft, Patchstack, Nethemba, Unit 42, PAN PSIRT, Rapid7, Arctic Wolf, Tamedia (via the metered reader; standfirst and key points only), Inside IT, Publica, admin.ch, PK Softech, watson, Netzwoche (x2), swissinfo.ch, GHSA, VenariX, Huntress, Todyl, SpecterOps, Sophos, NZZ (x2), Blick, PKZH, Pensionskasse Post (x2), BPK (pdf), BLVK (cached pdf text), Cybercrimepolice. Reading limit: the ConnectWise Trust Center advisory is 403 on extract, WebFetch and jina today, so its claims were checked against the saved read `work/2026-10-19T0256Z-intel/bodies/cw-advisory.md` (update of 2026-10-19 01:15 UTC, which the entry bounds).

Deltas block (iteration-4 findings), each checked against the page:
- n0 F4 PHP auth/vector: fixed in substance (the sourcing note now says the fields follow CERT-EU's reading of the scores, which CERT-EU states), but the wording introduced a new F11 (field names in reader-facing text, advisory #5).
- n1 F4 AA26 auth/vector: fixed. Cisco: "could allow an unauthenticated, remote attacker to retrieve memory contents"; SonicWall: CVSS:3.0/AV:N/AC:L/PR:N/UI:N. Both are cited for the clause; the Cisco and SonicWall dates are the pages' last-updated dates and the source labels say so. A residual depth gap is F8 #4.
- n2 F4 eMudhra cves[]: fixed (no `cves[]` record; body cites Go: "This is CVE-2026-111943"; CVE.org confirms the Go record). The run record's remark that the CVE index row was removed does not hold (F4 #2).
- n3 F4 APT28 title/headline: fixed. Title now scopes "at the shipbuilder it then pushed an SSH key ... captured NTLM handshakes and ran a reflective loader"; Symantec: "In the attack against the naval shipbuilder ... stole credentials and opened a persistent SSH tunnel".
- n4 F3 eMudhra registry: fixed. "which BleepingComputer, citing Mozilla's incident report, puts at values below 256" matches BleepingComputer.
- n5 F3 TeamUpdraft registry: fixed. "that it believes its customer database ... was accessed" matches "We believe our customer database was accessed."
- n6, n7, n9 (declined): n6 and n7 remain advisories (#8, #9). n9 (count in title) is upgraded to F4 #1: the title and a main-analysis sentence state fifteen as the total while the entry's own 2026-09-29 and 2026-10-21 sections say the total is higher.
- n8 F11 Publica narration: the section and source label are fixed; the sourcing_note still carries it (#6).
- n10 F11 PHP 'today' and CEST: fixed (no 'today' and no CEST in the entry).
- n11 F11 malware export name: fixed (no ExecuteLoader in the entry).

Changelog contract 4c on the four updated entries: every record's `fields` covers the `git diff HEAD` (PAN-OS headline, summary, entities, sources, evidence, sourcing_note, actions, body; Publica headline, summary, tags, entities, techniques, sources, evidence, sourcing_note, body, priority; ConnectWise improvement sources, evidence, sourcing_note, body; Metabase regions, sectors, sources, evidence, sourcing_note, body). `updated_at` equals the `at` of the `update` record on PAN-OS, Publica and Metabase and is untouched on the ConnectWise improvement. Each section is the same finding, carries a genuine delta, and passes checks 1 to 4 against its pages (Unit 42 for PAN-OS, Tamedia/Inside IT/Publica for Publica, swissinfo.ch/Netzwoche for Metabase, Sophos for ConnectWise). Supersession: PAN-OS and Publica main analyses were moved; the Metabase main analysis still says "The count has since grown to fifteen" (F4 #1). The Sophos finding differs from Huntress's added secrets and the section says so (no silent resolution).

### Unsupported / hallucinated facts
- #1 F4 `2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally` title and main analysis. Title: "exploited since at least 3 August, fifteen downstream victims confirmed"; body: "The count has since grown to fifteen, set out in the updates below." The 2026-09-29 section says Shipup and its retail clients "are not on that list, so the real total is higher still", and the 2026-10-21 section adds Republik, a further confirmed victim of the same flaw. VenariX (fetched) says only "tied to fifteen publicly confirmed incidents", its own count. Iteration 4 raised this as F11 and the decline ("VenariX's attributed figure") does not hold: the title does not attribute it. Attribute the number to VenariX in the title and the body sentence, or drop it, and say the total is higher (4c h).
- #2 F4 (low confidence) run record, iteration-4 remediation for eMudhra: "(and its CVE index row)". `state/cves_seen.json` line 9308 still carries `CVE-2026-111943` (first_seen 2026-10-21, golang-announce URL). Remove the row or correct the remediation text.

### Citation does not support the claim
- #3 F3 (low confidence) PAN-OS `## Update — 2026-10-21T03:45:31Z`: "says it is aware of public reporting that attributes exploitation to actors using Settra ransomware, which it does not itself confirm"; sourcing_note "does not confirm itself". Unit 42: "We're also aware of public reporting attributing exploitation to threat actors using Settra ransomware." It states no withholding of confirmation. Reword to "which Unit 42 describes as public reporting".

### Needs more research
- #4 F8 (low confidence) AA26 entry, cves[] CVE-2020-3259 and CVE-2024-40766: `fixed: "not stated by the advisory"` and "versions not stated by the advisory" although the Cisco advisory (fixed-release table) and SonicWall SNWLID-2024-0015 (affected Gen5/6/7 builds, fixed builds) are now sources of the same entry. Carry them or point to the cited vendor page.

### Editorial / less-is-more flags (advisory)
- #5 F11 PHP sourcing_note: "the auth and vector fields of the CVE records follow CERT-EU's reading of the scores" uses frontmatter field names in reader-facing text (check 12); introduced by the iteration-4 fix.
- #6 F11 Publica sourcing_note: "(standfirst and key points read)" is reading-limit narration.
- #7 F11 (low confidence) TeamUpdraft `event_date: "2026-10-18"`; the primary post and Patchstack are dated 2026-10-19 (event_date is the primary-source publication date per docs/pipeline.md).
- #8 F11 residual em dashes (Metabase title and older sections; PAN-OS 2026-06-17 record summary). Standing, may be left.
- #9 F11 living-page source records (Publica page twice; ConnectWise listing page, unreadable today, checked against the saved read). Standing, may be left.

### Considered and not flagged
- Oracle CPU at `notable` (no exploitation, no PoC; six unauthenticated CVSS 10.0 rows on widely deployed middleware): borderline against the PD-11 beyond-the-patch-cycle test, defensible as a constituency-wide scheduled-release duty; the run record states the reasoning. Four iterations have passed it.
- PHP at `high`, TeamUpdraft at `high`, Publica at `high` (federal staff data incl. security-organ staff, call-back rule within 7 days), AA26 and APT28 at `notable`: calibration holds.
- Missed angles: searches for in-window exploited flaws, Swiss municipal/cantonal incidents, KEV additions of 21 October and Publica/Akira follow-ups returned nothing beyond what the run holds or already dispositioned (Patch Tuesday Windows Shell, Ivanti Connect Secure and FortiMail entries exist; the KEV sweep and borderline drops are in the notes). Coverage looks complete.
- Dedup: AA26 declares the SonicWall and Manno entries in `references[]`; TeamUpdraft declares the CVE-2026-10795 entry (both exist); no new entry re-covers a store CVE; `actor:apt28` is new and distinct from `campaign:apt28-tradecraft-evolution-2026`.
- Style: no IOCs, no em dash in the six new entries (headings excepted), English throughout with `original` kept in evidence, no KEV deadline used as a reason to act, no workflow vocabulary beyond #5.
- Run record notes: counts (6 published, 4 updated, 12 entities added: 5 plus 7 products), the KEV disposition, the PHP CVE.org/EUVD absence, the Unit 42 versus KEV contradiction and duration 9064 s (02:56:29 to 05:27:33) hold; `completed` pre-dates this iteration, which the final amendment will move.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 1, advisory: 5)

### Findings summary (machine-readable)
See `work/2026-10-21T0256Z-intel/verification.iter5.findings.yaml` (9 records: F4 x2, F3 x1, F8 x1, F11 x5).
