**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-19T06:58:08Z · ended_at=2026-11-19T07:21:42Z · duration_seconds=1414

## Verification report — 2026-11-19T0355Z-intel (iteration 4)

Role: post-fix pass after iteration 3 (NEEDS_FIXES, 17 findings). Scope of the claim walk: all 25 claims in `claims.changed.iter4.yaml`, every other claim of the 11 entries remediated in iteration 3 (214 claims including the changed ones), and 24 of the 96 claims of the three entries iteration 3 left alone (Synology, OptimJack, HPE Aruba), drawn at random (seed 20261119). 238 verdict rows in `verification.iter4.claims.yaml`: 232 ok, 4 F3, 1 F4, 1 F5. No claim is `unreadable`: the F5 K-articles are not cited; the Drupal SA-CORE-2026-018 page (client challenge) was read through Drupal's advisory feed item, the BSI portal page (JavaScript shell) through its CSAF JSON, `support.hpe.com` through the HPE CSAF JSON and text advisory, Calif / Cisco / the LiteLLM advisory / Trend KA-0024802 / Cyderes / OpenCVE through raw HTML where the extract dropped fields, CISA pages through `WebFetch` with the outbound-links template.

### Prior-iteration deltas (all 17 walked against pages fetched this pass)

All 17 remediations hold on the page they cite. Three leave a neighbouring defect that is filed below as a new finding: the Obsidian takeaway (the rotation trigger now matches Obsidian, but the clauses in front of it still ride on the Obsidian citation), the NGINX Plus fixed-build record (the body now says four of five, the CVE-2026-123633 record still says "all five"), and the REDCap summary (the "exploited as of 2026-10-07" fix holds; the disclosure date in the same sentence is wrong).

1. CyberPower takeaway and action: Symantec, "Review the techniques and indicators in this document. If you find them, assume Active Directory credentials are exposed and plan a krbtgt reset and wider credential rotation." The reset is tied to Symantec's techniques. Holds.
2. Confluence sourcing note: the CISA alert row reads "CVE-2026-90436 Apache Axis Unsafe Reflection Vulnerability" and names no actor. Holds.
3. tcherber headline: Cyderes, "Contains a mix of default credentials (guest:guest, admin:admin, test:test) and organization-specific passwords". Holds.
4. CyberPower "does not say how the attacker reached the console": Symantec, "Any of these, or stolen administrator credentials, could give an attacker the necessary console access". Holds.
5. Java4Shell "none confirmed successful against its sensors": Tenable, "has not confirmed any successful exploitation against its sensors". Holds everywhere it appears.
6. Obsidian takeaway and action: the conditional rotation matches ("if exposure is suspected"). Partial, see F3 below.
7. NGINX patched-versions sentence: CERT.at lists the Plus builds for four of the five. Holds.
8. NGINX R33 variance: Wiz "CVE-2026-123633: R33; 37.0.0", CERT.at R33 only for CVE-2026-113425. Holds in the sourcing note.
9. NGINX CVE-2026-121810 record: CERT.at "R34 bis R36 (alle vier Schwachstellen)". Holds.
10. Airlock descriptor: "WAF" and "web application firewall and API gateway vendor" are gone; the wording follows ENISA and the documentation pages. Holds.
11. Idunno sourcing note: the CVE-record clause is gone. Holds.
12. Obsidian Detection: cites Obsidian for the endpoints and the `user_role` escalation. Holds (an omission is filed, F8).
13. PHP2Shell Analyzer: the advisory row ("Engine: Fixed via Active Update on Nov.6. OS Image: 7.7: Critical Patch 1020 7.6: Critical Patch 1082 CP for DDAN 7.5 is not planned") is now in `cves[].affected` and `fixed`. Holds.
14. Drupal priority: `notable`. Holds in the entry; the run record's notes still say "notable to high" (filed).
15. Idunno action: search-and-remove plus evidence-conditional rotation, precaution clause gone. Holds.
16. Java4Shell narration clause: gone from section and record summary. Holds.
17. REDCap "exploited as of 2026-10-07" and the sourcing note's event-date sentence: hold.

### Claim does not support / unsupported facts (truth)

### Citation does not support the claim
- **F3 #1** NGINX summary (frontmatter): "NCSC-NL scores all five CVSS 4.0 9.2, and NCSC.ch and Rapid7 the HTTP/2 pair." Rapid7's page scores only CVE-2026-123007 (table row 9.2 for that one CVE); NCSC.ch (13203) and Wiz ("CVE-2026-123633 and CVE-2026-123007, are both rated Critical, with a CVSS 4.0 score of 9.2") score the pair. NCSC-NL's per-CVE list is 9.2 for all five (verified on advisories.ncsc.nl 0506). Fix: "NCSC.ch and Wiz the HTTP/2 pair, Rapid7 CVE-2026-123007".
- **F3 #2 (low confidence)** NGINX body, first sentence: "F5 and the nginx project fixed five unauthenticated memory-corruption flaws in the data plane ([nginx.org])". nginx.org lists more than five advisories with severities and ranges and says nothing on authentication or a group of five; both come from CERT-EU in the next clause. Move that citation up.
- **F3 #3** REDCap summary: "Securifera disclosed CVE-2026-90817 on 2026-09-20". The Securifera post is dated 2026-09-27 and states no disclosure date; 2026-09-20 is the CNA record's publication (OpenCVE "Published Sep 20, 2026, 12:05 PM", CNA Vanderbilt University; Pentest-Tools "CVE Published Sep 20, 2026").
- **F3 #4** Obsidian Defender takeaway: "block the guardrail endpoint at the reverse proxy until then, keep admin endpoints off the internet, ... as Obsidian advises ([Obsidian])". Obsidian's list (upgrade, audit roles, guardrails, callbacks, rotate if exposure is suspected) has neither clause; the block is the LiteLLM advisory's workaround, the internet clause is in no listed source (THN's "What to do" lacks it too).

### Unsupported / hallucinated facts
- **F4 #1** NGINX `cves[CVE-2026-123633].fixed`: "(37.3.0.1 and 37.0.8.1 carry all five fixes)". CERT.at: "F5 stellt Updates bereit, die alle vier Schwachstellen beheben" and lists four CVEs without CVE-2026-123634; the entry's own body says four of five and its CVE-2026-123634 record says "presumed".
- **F4 #2 (low confidence)** NGINX sourcing note: "Wiz and Xint ... did not publish their exploits". Only Wiz says so ("we will not be releasing these exploits at this time"); Xint's page withholds only the SCTP kernel details.
- **F4 #3** Run record notes, "Scheduled releases": "Drupal core released 2026-11-18 (update on the pre-announcement entry, priority notable to high)". The entry is `priority: notable`.
- **F4 #4** Run record notes, "KEV sweep": "CVE-2026-90436 → `improvement` on the Confluence entry ... no re-float". The record is typed `update`, `updated_at` moved to 2026-11-19T05:05:36Z (iteration 1 retyped it).

### Surface contradiction
- **F9 #1 (low confidence)** Idunno: "Mandiant published CVE-2026-131914 on 2026-11-18" is Mandiant's timeline; the ENISA record the entry cites gives the CVE `datePublished` Nov 19, 2026, 1:29:12 AM (MITRE record 2026-11-19T01:29Z). Attribute the date to Mandiant's timeline or add a Contradiction line.

### Claims missing inline citation
- **F5 #1 (low confidence)** Obsidian sourcing note: "the CVE record published by MITRE scores CVE-2026-40217 CVSS 3.1 8.8 with low privileges required". True (CVE record `cvssV3_1` 8.8, PR:L) but not a listed source; iteration 3 dropped the equivalent Idunno clause. The 8.8 on CVE-2026-47101 also rests on no listed page (THN scores only CVE-2026-47102; the VulnCheck CVE record gives 8.8, so the value holds).
- **F5 #2 (low confidence)** Drupal Detection line: the installer-request hunt is the entry's inference with no citation and no label. NCSC-NL (translated: "when the installer is not correctly secured or removed after the initial installation") supports the premise.

### Needs more research
- **F8 #1 (low confidence)** Obsidian Detection omits Obsidian's step-one key `/key/generate` with an explicit `allowed_routes` ("the cleanest path") and `/user/bulk_update` ("The same flaw exists").

### Action-item discipline
- **F18 #1 (low confidence)** OptimJack `actions[1]` restates the Detection line's Zscaler guidance as a task.

### Editorial / less-is-more flags (advisory)
- **F11 #1** Java4Shell update section: "available to its customers, ([Tenable" has a stray comma before the citation.
- **F11 #2 (low confidence)** HPE Aruba `sources[]`: the CSAF JSON and TXT URLs are listed twice (revision-1 date and revision-2 date, all primary); both URLs now serve revision 2.
- **F11 #3** NGINX patched-versions paragraph: `check_run.py` WARN `citation-cve`, the clause naming CVE-2026-123634 cites CERT.at, which does not mention that id. Name the four CVE ids CERT.at lists instead of "all but CVE-2026-123634" (this also settles F4 #1).

### Checked and clean
Every new entry's sources resolve to a specific page and carry the facts attached to them (Symantec, CISA ICSA-24-123-01, CyberPower product page; Cyderes, VMRay; ENISA EUVD-2026-128505 and the Airlock documentation; Mandiant MNDT-2026-0048 and EUVD-2026-129432; nginx.org, Rapid7 and its repository, Wiz, Xint, CERT-EU, CERT.at, NCSC-NL 0506, NCSC.ch 13203; Securifera, its repository, Unit 42, CISA, OpenCVE, Pentest-Tools, GTIG). Every updated entry's changelog contract holds: records and sections match, `updated_at` equals the last non-internal `update` record, frontmatter follows the sources (Drupal SA-017/018 via the feed item; Java4Shell Cisco 13 products, Fortinet, BACS; Synology KEV/EPSS 0.01251; LiteLLM advisory 5.9, EPSS 0.1702; Confluence KEV, EPSS 0.01128, Apache handler statement, BSI critical plus "Exploit aufgenommen"; OptimJack signup-flow flaw, Zscaler 450 domains; PHP2Shell DDAN 1020/1082, MSE CP10, NetApp revision 13.0; HPE revision 2: 76 CVEs, 33 at 9.0+, 19 unauthenticated network, 8 at 10.0). Classification, org_triage (null everywhere) and watchlist fields are consistent. Priorities hold (Drupal `notable` for a non-default-configuration flaw with no reported exploitation; Airlock and Idunno `notable`). No IOCs, no em dash outside section headings, no workflow-internal vocabulary in reader-facing text. Registry keys added by the run are new and contain no alias collision (pre-existing duplicate NGINX and LiteLLM product keys predate the run).

### Missed angles
Coverage looks complete for the critical and high signal: all four KEV additions of 2026-11-18 are covered; nginx2root, Java4Shell vendor impact, Drupal, Trend/NetApp revisions and the HPE revision are in. The Basel-Landschaft cantonal-administration incident is a home-region item held on the backlog with a named condition (no vector, actor or behaviour, so an incident entry would fail the empty-`techniques[]` gate); this is a logged hold, not a silent blind spot, so no finding. The PHP release pre-announced for 2026-11-19 14:00 to 14:30 UTC is held with an expiry and should be the next fire's first read.

### Verdict
NEEDS_FIXES (truth: 8, editorial: 5, advisory: 3)
