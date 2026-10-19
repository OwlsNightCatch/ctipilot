**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T17:04:01Z · ended_at=2026-10-19T17:29:52Z · duration_seconds=1551

## Verification report — 2026-10-11T1307Z-audit (iteration 5, slice s1)

Scope: 26 entries, 277 ledger claims (all answered: 276 ok, 1 F4), every cited page fetched this pass (cached bodies not needed: every page was re-fetched; cisa-kev recipe, `msrc cve` recipe, `ncsc-csh post`, `pdf`, `extract`, `url`, WebFetch for the cisa.gov alert; jina was reached by `extract` internally for six pages). Prior-iteration deltas (23 items) walked: 15 hold on disk and against the source, 8 do not hold fully (below).

### Delta walk (iteration-4 findings)

Hold: Exchange OWA Period-1 citation, takeaway no longer says "patching", sectors trimmed, four 07-31 mechanism paragraphs cited; RoguePlanet cmdlet dropped and duplicate sentence gone; Cisco UCM record summary no longer narrates the fold; SAP Note 3773203 in SAP's words, NCSC-NL scanning sentence, "exploitation attempts appeared within days", record-keeping sentence removed, CVE-2026-58231 affected releases named; Gentlemen GLPI/PoC clause cites Talos, rclone "traces indicating" hedge; nginx event_date 2026-05-13 and affected/fixed ranges; Unbound "a third" -> "another".
Do not hold fully: Exchange OWA "must" (F3, below), SAP F8 partial, Unbound F4 partial (body clause), Pwn2Own F11 partial, RoguePlanet F11 partial, PeopleSoft F11 partial, SAP sector decline weakly supported, Cisco UCM date point only half answered.

### Citation does not support the claim
- #1 F3 `2026-05-18/cve-2026-42897-exchange-owa-em...` 2026-07-31 section. Quote: "with the mitigation now something that must be actively torn down" (cited July blog) and, in "Patching.": "administrators who used the EM Service must remove the M2.1.0 IIS rules through the documented rollback, and those who ran the downloadable mitigation script must run its rollback." July blog: "once you install July SU, you should: ... Remove the mitigation M2.1.0 IIS rules ... Roll back the mitigation"; June blog: "We recommend that customers keep CVE-2026-42897 mitigation in place". "must" overstates Microsoft's advice; same defect iterations 3 and 4 raised, fixed only in the main analysis and takeaway.

### Unsupported / hallucinated facts
- #2 F4 (low confidence) Exchange OWA, 07-31 section: "Proofpoint reads the unusual breadth as intentional blending with bulk mail." Source: "may have been intentionally broad to blend in with mass-mailing spam".
- #3 F4 (low confidence) Exchange OWA, Persistence paragraph: "AES-encrypted copy of itself" in localStorage. Source: "an encrypted version of itself".
- #4 F4 (low confidence) PeopleSoft: "PeopleSoft Campus Solutions or HCM should audit external reachability ... as the first action" (claim 319a07318b); no cited page names Campus Solutions or HCM (Oracle: PeopleTools 8.61/8.62); "first action" conflicts with actions[0].
- #5 F4 (low confidence) Unbound: main analysis ends "a normal condition for any DNSSEC-validating resolver doing open recursive resolution against the internet, not an edge case." Uncited, unmarked; NCSC-CH gives only the precondition.
- #6 F4 (low confidence, minor) Gentlemen: "then ran nmap and masscan against externally exposed hosts and internal services once inside"; Talos: "They appear to have used Masscan and Nmap".

### Needs more research
- #7 F8 (low confidence) SAP: cves[] for CVE-2026-44772, -44758, -58243, -42945 still "see SAP Security Note ..."; the cited SAP page lists XMII 15.4/15.5 + MII_ADMIN, SAP_BASIS 750-758/816/918/920, COM_CLOUD 2211 + DHUB_CLOUD 2211.

### Surface contradiction
- #8 F9 (low confidence) Acronis: advisory SEC-10986 cited as 2026-09-17 (structured record `published`), while BleepingComputer (2026-09-15) and Help Net Security ("published on Tuesday") already quote it.

### Editorial / less-is-more flags (advisory)
- #9 F11 Pwn2Own entry: record summary "the rating follows the B-rated contest reporting"; section narrates the priority change.
- #10 F11 RoguePlanet: em dashes in title/body, priority narration, "in the entry's reading".
- #11 F11 PeopleSoft: "see the § 0 callout" (2026-06-12 section), "this campaign's own earlier coverage carried" (2026-09-27 section) remain.
- #12 F11 G7: record summary "the label the rest of the store uses".
- #13 F11 MRSProxy: long sourcing_note with "see body"; correction opens by narrating the removed takeaway.
- #14 F11 (low confidence) SAP sectors (public-sector, finance unsourced) and em dash in actions[1].
- #15 F11 (low confidence) Cisco UCM: body never states the 2026-06-03 initial release; sources[0].date is the revision date.
- #16 F11 em dashes in titles/bodies of nginx, RoguePlanet, MRSProxy, Chosen Brick, Acronis, PeopleSoft, SAP, Cisco ISE entries (previously declined as style).

No findings on: relevance, priority calibration (all 26 priorities defensible; Unbound `high` and QBUSoft/Austria `routine` considered and left), classification vocabulary, org_triage/watchlist (all null/false), single-source flags, KEV dates (all 11 KEV-cited CVEs match the live catalog), CVSS per authority (SAP, Cisco, Acronis, Oracle, MSRC, Wordfence, Check Point, NLnet/Rapid7), evidence quotes (verbatim or faithful translations with matching `original:`), closed-source (none), missed angles (none evidenced).

### Verdict
NEEDS_FIXES (truth: 6, editorial: 2, advisory: 8)
