**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-29T09:21:08Z · ended_at=2026-10-29T09:49:12Z · duration_seconds=1684

## Verification report — 2026-10-29T0255Z-intel (iteration 8)

Scope: confirmation pass after iteration 7's CLEAN, read cold. All 11 new entries and all 9 updated entries read whole; for each updated entry `git diff HEAD` and the newest record's `fields` were checked against the cited sources. Claim ledger `claims.iter8.yaml`: 466 of 466 claims answered in `verification.iter8.claims.yaml` (461 ok, 3 truth rows, 2 unreadable; `tools/claim_ledger.py --coverage 8` reports 0 missing). Pages were read this iteration (saved bodies first, live fetches for Cisco, WatchGuard listing and per-CVE pages, Palo Alto advisory and JSON timelines, NetApp, Broadcom, NCSC.ch hub posts, ConnectWise Trust Center via an archived copy, Ubuntu, Red Hat, Wiz, Help Net Security, KEV feed, FIRST EPSS API). Oracle's 112 / 90 / 73 row tallies were recomputed from the risk matrices and match; WatchGuard's 17 + 1 listing tally and seven rows at 9.0+ were recomputed from the live Published column and match; Palo Alto's 19 of 20 released hotfixes match the live table and the 2026-10-29 05:20 UTC timeline entry. `check_run.py` re-run: 60 pass, 0 warn, 1 fail (verification-confirmation, expected).

### Citation does not support the claim
- #1 (F3, low confidence) `keydrift-uat-11473-cisco-sd-wan-controllers-cve-2026-20127`, body: "an authentication bypass in the peering authentication of Cisco Catalyst SD-WAN Controller" ends under the Talos link; Talos says only "an authentication bypass vulnerability in Cisco SD-WAN Catalyst Controller instances" and the word "peering" occurs nowhere on its page. The wording is Cisco's advisory and CISA's. Fix: move the descriptor behind the Cisco citation.

### Unsupported / hallucinated facts
- #2 (F4, low confidence) same entry, `cves[CVE-2026-20127].fixed`: "20.12.5.3, or 20.12.6.1 for the 20.12.6 train (20.12)". Cisco's fixed-release table row 20.12 lists "20.12.5.3<br>20.12.6.1" with no train qualifier; the gloss is the entry's own.

### Needs more research
- #3 (F8, low confidence) `vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape`: Broadcom's matrix (VMSA-2026-0006.2, change log "2026-08-19 ... Added ESX/vCenter 7.0 patch guidance for Critical severity issues") lists vCenter 7.0 and ESX 7.0 as affected by CVE-2026-59309/59310/47876 with the fix only "if you have extended support contract"; the entry's `affected` fields and fixed-builds paragraph name 9.1, 9.0, 8.0 and Cloud Foundation 5.x only. Pre-existing, not touched by this run.

### Analytical-link-as-fact
- #4 (F13, low confidence) same VMware entry, summary: "CISA also listed ... CVE-2026-41709 as exploited on 2026-10-28, after CrowdStrike said the actor WARP PANDA used it as a zero-day." The KEV record (dateAdded 2026-10-28) names no source and the CrowdStrike post is dated the same day without mentioning CISA; the body says only "CrowdStrike says ... and CISA lists it as exploited". Replace "after" with "and".

### Quantifier without source
- #5 (F14, low confidence) `machelen-municipality-misleading-instructions-rhysida`, Detection: "so the only telemetry to review is endpoint process creation ..." The timeline names no telemetry; web-proxy, DNS, email and network logs are equally relevant. The "inference" tag does not cover the exclusivity.

### Editorial / less-is-more flags (advisory)
- #6 (F11, low confidence) `php-critical-release-pre-announced-cve-2026-109618-109619`, claim 7bcd510a17: the Citrix Tech Zone page answers 403 on extract, url, jina and WebFetch (re-tested); unreadable. NCSC-NL's list relays the statement; the clause predates this run.
- #7 (F11, low confidence) VMware entry, claim eb3d5575fc: the WID portal page (BSI CERT-Bund) is a JavaScript shell and the content API has no record for the id; unreadable. NCSC-NL's advisory for the same VMSA is readable (29-07-2026).
- #8 (F11, low confidence) `moldova-egovernment-mass-extraction-unauthenticated`: "it blocked further attempts on 25 and 27 October"; AGE says it blocked the 25 October attempt and only "recorded" the 27 October attempts "without success". Raised before and left.
- #9 (F11) `watchguard-fireware-2026-4-three-preauth-rows-at-9-2`: the tally is cited to the advisory listing index (psirt.watchguard.com/), which is correct as read now (18 rows published 2026-10-27, 17 Fireware OS, seven at 9.0+) but will not stay checkable; defensible, left to the main agent.
- #10 (F11, low confidence) VMware entry: 17 lines with em dashes and the phrases "this pipeline", "this entry", "A/1 rating" in reader-facing text; all predate the run (19 em-dash lines in HEAD, none added). Standing debt for the audit.

### Missed angles
None found. The NCSC.ch hub's only post inside the window (Veeam, 13109) is covered; both KEV additions of 2026-10-28 have update records; the 2026-10-27 KEV additions (Adobe Commerce CVE-2026-48356, Brotli CVE-2026-111497) were covered by the prior fire's entries; web searches for further in-window exploited-vulnerability items surfaced nothing dated 2026-10-28 or 2026-10-29 that the run's telemetry did not already list. Coverage looks complete for the critical/high signal.

### Checked and clean (no finding)
- Reader-facing style: no em dash, workflow vocabulary, IOC or vanity metric in any new entry or in any line this run added to an updated entry. All ATT&CK ids exist, non-revoked, in the pinned v20.0 data.
- Classification: every entry carries an Admiralty block in the vocabulary; letters match the source tiers in `sources/sources.json` (vendor PSIRT A, research B, aggregator C not relied on alone).
- Changelog contract for the nine updated entries: each newest record's `fields` covers every changed frontmatter line in `git diff`, sections exist for non-internal records, `updated_at` mirrors the newest `update` record, earlier statements superseded by the newest section are dated or replaced (Fragnesia exploitation, PHP "no source ties a named CVE" dated, PAN-OS hotfix counts, URWB date, Oracle exploitation line, ConnectWise restoration advice, ZDI fix status, Node2Shell PAN-OS ETAs).
- NetApp's advisory data field "kb_exploitation: Public" renders on the advisory page (read live this iteration) as "Exploitation and Public Announcements: NetApp is aware of public discussion of this vulnerability", so the entry's "no exploited case" sentence stands.
- `cves[].auth: pre-auth` on the Check Point, F5, Trend, Quest and NetApp rows is carried by CISA's KEV description of both PHP flaws ("unauthenticated remote code execution"), which those entries cite.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 1, advisory: 5)

All five non-advisory findings are low confidence and small; the content is otherwise sound. This is the cap iteration, so the run publishes with these logged as residuals.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: threat
  item: "keydrift-uat-11473-cisco-sd-wan-controllers-cve-2026-20127 (body, first paragraph, claim 4d1b01bad7)"
  url_or_quote: "https://blog.talosintelligence.com/uat-11473-keydrift/"
  summary: "(low confidence) Entry: 'Cisco Talos reports that UAT-11473 exploited CVE-2026-20127, an authentication bypass in the peering authentication of Cisco Catalyst SD-WAN Controller' ending under the Talos link. Talos says only 'an authentication bypass vulnerability in Cisco SD-WAN Catalyst Controller instances'; the word 'peering' occurs nowhere on the Talos page (0 matches). 'Peering authentication' is Cisco's advisory wording (cisco-sa-sdwan-rpa-EHchtZk) and the CISA KEV description. Move the descriptor behind the Cisco citation or drop it from the Talos clause."
- code: F4
  category: hallucinated-fact
  section: threat
  item: "keydrift-uat-11473-cisco-sd-wan-controllers-cve-2026-20127 (cves[CVE-2026-20127].fixed, claim b6ebc3ab70)"
  url_or_quote: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa-EHchtZk"
  summary: "(low confidence) fixed: '20.12.5.3, or 20.12.6.1 for the 20.12.6 train (20.12)'. Cisco's fixed-release table (raw HTML, row '20.12') lists the two builds '20.12.5.3<br>20.12.6.1' with no train qualifier; 'for the 20.12.6 train' is the entry's own gloss, not a Cisco statement. Say 'first fixed releases 20.12.5.3 and 20.12.6.1 per Cisco's table' or mark the gloss as an inference."
- code: F13
  category: analytical-link-as-fact
  section: vulnerability
  item: "vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape (summary, claim e0bc3b4ddd)"
  url_or_quote: "CISA also listed the ESX logging flaw CVE-2026-41709 as exploited on 2026-10-28, after CrowdStrike said the actor WARP PANDA used it as a zero-day."
  summary: "(low confidence) 'after CrowdStrike said' asserts a sequence and implies CISA acted on CrowdStrike's report. Sources: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json lists CVE-2026-41709 dateAdded 2026-10-28 with no source named; https://www.crowdstrike.com/en-us/blog/crowdstrike-2026-legal-threat-landscape-report/ is dated 2026-10-28 (the same day) and does not mention CISA. The body (and update section) correctly say only 'CrowdStrike says ... and CISA lists it as exploited'. Replace 'after' with 'and' or 'the same day'."
- code: F14
  category: quantifier-without-source
  section: incident
  item: "machelen-municipality-misleading-instructions-rhysida (Detection, claim 8b7f23121b)"
  url_or_quote: "so the only telemetry to review is endpoint process creation after a user followed instructions on a web page and later use of a high-privilege account from that workstation, which is an inference from the timeline."
  summary: "(low confidence) The absolute 'the only telemetry to review' has no source: the municipality's timeline (https://www.machelen.be/tijdslijn-cyberincident) names no telemetry at all, and web-proxy, DNS, email and network logs are equally relevant to a user following a website's instructions. The 'inference' tag covers the choice of telemetry, not the exclusivity. Say 'the telemetry to start with is'."
- code: F8
  category: needs-more-research
  section: vulnerability
  item: "vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape (cves[].affected, fixed builds paragraph)"
  url_or_quote: "https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017"
  summary: "(low confidence) Broadcom's response matrix (advisory VMSA-2026-0006.2) lists '| VMware vCenter | N/A | 7.0 | Any | CVE-2026-59309, CVE-2026-59310 | 9.8 | Critical | Contact Broadcom Support if you have extended support contract.' and '| VMware ESX | N/A | 7.0 | ... | CVE-2026-47876 | 9.3 | Critical | Contact Broadcom Support if you have extended support contract.'; its change log says '2026-08-19 VMSA-2026-0006.2 Added ESX/vCenter 7.0 patch guidance for Critical severity issues'. The entry's affected fields and fixed-builds paragraph name only 9.1, 9.0, 8.0 and Cloud Foundation 5.x, so a reader running vSphere 7.0 (end-of-support estates, relevant to public-sector fleets) is told nothing. Pre-existing, not touched by this run, but the entry was re-floated; add 7.0 with the extended-support route in a record."
- code: F11
  category: editorial-advisory
  section: vulnerability
  item: "php-critical-release-pre-announced-cve-2026-109618-109619 (body, claim 7bcd510a17)"
  url_or_quote: "Citrix lists the NetScaler management GUI on every supported version (https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/)"
  summary: "(low confidence) Claim row 7bcd510a17 is unreadable: extract, url, jina and WebFetch all return HTTP 403 for the Citrix Tech Zone page (verified this iteration). The statement is relayed by NCSC-NL's PHP2Shell software list and the page predates this run; no change needed unless the audit sweeps legacy citations."
- code: F11
  category: editorial-advisory
  section: vulnerability
  item: "vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape (body, claim eb3d5575fc)"
  url_or_quote: "BSI CERT-Bund, whose advisory is dated 2026-07-28 with a 2026-07-29 revision (https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2569)"
  summary: "(low confidence) Claim row eb3d5575fc is unreadable: the WID portal is a JavaScript shell (extract returns the page title only) and the content API returns a listing without this id. The NCSC-NL advisory for the same VMSA is readable and carries 29-07-2026. Legacy citation, predates this run."
- code: F11
  category: editorial-advisory
  section: incident
  item: "moldova-egovernment-mass-extraction-unauthenticated (body, claim 291169021f)"
  url_or_quote: "it blocked further attempts on 25 and 27 October"
  summary: "(low confidence) AGE's timeline (https://egov.md/ro/node/41145) says on 25 October 'au identificat si blocat o noua tentativa' (identified and blocked) but for 27 October only 'au fost inregistrate noi tentative de extragere a datelor, fara succes' (recorded, unsuccessful); The Record says 'Both attempts were unsuccessful'. 'Blocked' fits the 25th; for the 27th 'recorded a further unsuccessful attempt' is the source's wording. Raised in earlier iterations and left; recorded again for the main agent to weigh."
- code: F11
  category: editorial-advisory
  section: vulnerability
  item: "watchguard-fireware-2026-4-three-preauth-rows-at-9-2 (body, claim 6ebcae3620; sources[] role corroborating)"
  url_or_quote: "https://psirt.watchguard.com/"
  summary: "The tally ('18 rows, 17 for Fireware OS ... seven of the 17 are scored 9.0 or higher') is correct against the listing as read this iteration (Published column 2026-10-27 on exactly those 18 rows; 9.2 x5, 9.5, 9.1 among the 17), but the cited URL is the advisory listing index, which keeps growing, so the tally will not be checkable from that URL later. Defensible for a tally that no per-item page can carry; consider naming the listing's published date range or dropping the 17 and 7 counts. Left to the main agent."
- code: F11
  category: editorial-advisory
  section: vulnerability
  item: "vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape (title, headline, actions[1], body sections, updates[].summary)"
  url_or_quote: "this pipeline covered on 2026-07-30 ... the campaign this entry already tracks ... this entry's overall A/1 rating"
  summary: "(low confidence) Style rule 12 residue in reader-facing text of an entry re-floated by this run: 17 body/frontmatter lines still carry an em dash (19 in HEAD, none added by this run), and four sentences use 'this pipeline' / 'this entry' / 'A/1 rating' (Admiralty letter and digit). All predate the run, which lowered the counts and added nothing; fixing title and headline needs those fields in a record. Standing debt for the quality audit."
```
