**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-28T07:12:58Z · ended_at=2026-11-28T07:31:32Z · duration_seconds=1114

## Verification report — 2026-11-28T0355Z-intel (iteration 7)

Scope: full cold pass, all 186 ledger claims walked (rows in `verification.iter7.claims.yaml`: 185 ok, 1 F4), every cited URL re-fetched live this pass (78 unique pages; Kudelski tables from raw HTML; CISA, KEV catalogue, NCSC hub posts, GitHub advisory sidebars, CVE JSON via their structured routes). No deltas block; the previous iteration (6) returned NEEDS_FIXES and the six changed claims of claims.changed.iter7 were each re-read against their sources (Mitel summary, BACS parenthetical, FreeRADIUS VLAN clause, Kudelski headline and Triage, SAP headline). All six remediations are correct except the BACS parenthetical, which still carries the residue of the iteration-6 finding.

### Unsupported / hallucinated facts
- #1 (F4, low confidence) `2026-11-25/bacs-first-confirmed-ai-agent-attacks-switzerland`, section `## Update — 2026-11-28T04:41:50Z`: "Neither SRF nor RTS says which sectors the three critical-infrastructure victims belong to (their electricity, water and telecom examples only illustrate the term)". SRF: "Betroffen von den neuen Cyberangriffen sind drei Betreiberinnen kritischer Infrastrukturen. Dazu gehören beispielsweise Strom- und Wasserversorger oder Telekom-Anbieter." The second sentence follows the three-operators sentence and can be read as naming the victims' sector types; RTS's "Les infrastructures critiques sont par exemple ..." is a definitional gloss. No source states that the examples "only illustrate the term"; that is the entry's reading, asserted as fact. Fix: drop the parenthetical, or mark it as the entry's reading. The record summary's "No framework, victim sector or entry point is named" inherits the same reading.

### Surface contradiction
- #2 (F9, low confidence) `2026-11-28/freeradius-3-2-11-critical-ttls-use-after-free`, summary and body: "released 3.0.29 and 3.2.11 on 2026-11-25". The project page is headed "2026.11.25 ... We have released 3.0.29 and 3.2.11", but the entry's own cited 3.0.29 release page is dated 2026-11-26, the signed tag release_3_2_11 was created 2026-11-26T12:02:50Z and GitHub published the releases at 2026-11-26T12:13Z (3.0.29) and 12:17Z (3.2.11). The entry picks the 25th silently. Fix: "announced 2026-11-25, GitHub releases 2026-11-26", or a Contradiction line.

### Missed angles
- #3 (F10) `2026-11-18/drupal-core-critical-release-2026-11-18-psa-2026-11-16` (not touched by this run): its 2026-11-26 section says "CISA added CVE-2026-132165 to its Known Exploited Vulnerabilities catalogue on 2026-11-24, and the newer flaw is not on the list", and `cves[CVE-2026-136716].status` is `[exploited, patch-available]`. The in-window CISA alert of 2026-11-27 (kev-window.txt, catalogue 2026.11.27, dateAdded 2026-11-27) lists CVE-2026-136716, so the published entry now asserts a falsehood. The run notes call the listing KEV bookkeeping under PD-13; the stale sentence is not bookkeeping. Append a correction or improvement record on the Drupal entry (status `cisa-kev`, fix the sentence). Suggested query: "CISA KEV CVE-2026-136716 Drupal 2026-11-27". Otherwise coverage looks complete: I swept NCSC.ch hub, Fortinet, Palo Alto and Cisco PSIRT feeds and the KEV catalogue for in-window items and found no uncovered critical/high item (Juniper CVE-2026-103406 and the vCenter flaws are covered by existing entries; BSI's agentic-AI release is 2026-11-26, before the window).

### Editorial / less-is-more flags (advisory)
- #4 (F11, low confidence) GeoServer `## Update — 2026-11-28T04:50:22Z`: the CISA clause's descriptors ("unauthenticated XML injection in the WFS GetFeatureById stored query", "service-level authorization bypass through a prefixed service name") are not on the CISA page, which says only "XML Injection Vulnerability" and "Incorrect Authorization Vulnerability". True per the GeoServer advisories; add that citation or trim.
- #5 (F11, low confidence) Kudelski Detection last sentence ("The sequence to alert on is a burst of identification requests, then accounts created ..., then sensitive information accessed") is the entry's synthesis; the sourcing_note says the post gives no ordered attack chain. May be left.
- #6 (F11, low confidence) SAP: the Inside IT "existing S/4HANA landscape" sentence sits only in the paywalled article's embedded JSON; the visible teaser says "bestehenden SAP-Systems durch eine modernere SAP-Lösung". A reader cannot confirm it. May be left.
- #7 (F11, low confidence) FreeRADIUS title/summary "no exploitation stated and no proof of concept for the Critical flaw" / "the project states no exploitation": the page is silent; reword as "mentions no exploitation or proof of concept".
- #8 (F11, low confidence) Cacti source `Previdian (VULN-2026-0010)` dated 2026-11-28: the tracker's dateline is "Published 26 Nov 2026 / Updated 28 Nov 2026" and its live counters now read 248 attempts from 23 addresses (the note records 216 and 21 at 04:35 UTC, and says the counts move). Label it "as read".

### Checked and clean (no finding)
All six new entries and the four changelog records were checked end to end: every inline URL resolves to a specific page and every dateline matches (BSI CSAF 23:00 UTC is a Berlin-next-day artifact; Hunt.io 2026-11-25 from the time element; EFK 10.05.2023 visible dateline). Numbers verified at the source: FreeRADIUS 21 issues (1 Critical, 8 High, 5 Medium, 7 Low; four TEAP Medium issues of which three return Access-Accept); Cisco v1.6 (25 affected products, 21 beyond the four priority rows; NextFusion absent); Fortinet 29 under investigation, FortiADC, FortiWeb and FortiSIEM now not impacted; Synology revisions 3 and 4 give APM 2.0.2-88107; Mitel MTLVULN-1785/1786/1793 map to CVE-2026-137724/137721/137723 (ENISA descriptions end "This is MTLVULN-17xx", datePublished Nov 27, cveawg dateReserved 2026-11-27T05:33:02Z); RealVNC affected and fixed lists identical to the advisory; CISA KEV 2026-11-27 lists CVE-2026-120705 and CVE-2026-129243; watchTowr's table (129245, 129243, 120705 Yes; 129244, 129242 Not reported) against its prose (all five) is exactly as the section states; Kudelski tables (nine weaknesses, detection rows, 2.9 million, 717 req/s) and ZITADEL (4.0.0 to 4.20.4, fixed 4.20.5, 2026-11-18) match; Cacti PR 9014 merged 2026-11-28T01:28:13Z on 1.2.x. Diffs of the four updated entries show every changed line covered by the record's `fields`, `updated_at` moved only on the two non-internal updates, and no silent edit. All quotes with `original:` are literal substrings of the page; translations are faithful. No IOCs, no em dashes in reader-facing text, no workflow vocabulary; classification blocks present and consistent with source tiers; no org_triage, no watchlist use; actions lists within bound.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 2, advisory: 5)

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable)
- code: F4
  category: hallucinated-fact
  section: update-section
  item: "2026-11-25/bacs-first-confirmed-ai-agent-attacks-switzerland, section Update 2026-11-28T04:41:50Z (claim e2282f405e)"
  url_or_quote: "(low confidence) \"Neither SRF nor RTS says which sectors the three critical-infrastructure victims belong to (their electricity, water and telecom examples only illustrate the term)\""
  summary: "(low confidence) SRF writes 'Betroffen ... sind drei Betreiberinnen kritischer Infrastrukturen. Dazu gehören beispielsweise Strom- und Wasserversorger oder Telekom-Anbieter.' The sentence follows the three-operators sentence and can be read as naming the victims' sector types; no source states that the examples only illustrate the term. Drop the parenthetical or word it as the entry's own reading; the record summary's 'No ... victim sector ... is named' inherits the same reading."
- code: F9
  category: surface-contradiction
  section: body
  item: "2026-11-28/freeradius-3-2-11-critical-ttls-use-after-free, summary and body 'released 3.0.29 and 3.2.11 on 2026-11-25' (claims ec0399ec66, bdbb035ac6)"
  url_or_quote: "https://api.github.com/repos/FreeRADIUS/freeradius-server/releases/tags/release_3_0_29"
  summary: "(low confidence) The project page is headed '2026.11.25 ... We have released 3.0.29 and 3.2.11', but the entry's own cited 3.0.29 release-notes page is dated 2026-11-26 and GitHub shows the signed tag release_3_2_11 created 2026-11-26T12:02:50Z and the releases published 2026-11-26T12:13Z (3.0.29) and 12:17Z (3.2.11). The entry picks the 11-25 reading silently; say 'announced 2026-11-25, GitHub releases 2026-11-26' or add a Contradiction line."
- code: F10
  category: missed-angle
  section: prior-coverage
  item: "2026-11-18/drupal-core-critical-release-2026-11-18-psa-2026-11-16 (not updated by this run)"
  url_or_quote: "Entry section Update 2026-11-26: \"CISA added CVE-2026-132165 to its Known Exploited Vulnerabilities catalogue on 2026-11-24, and the newer flaw is not on the list\"; cves[CVE-2026-136716].status = [exploited, patch-available]"
  summary: "The in-window CISA alert of 2026-11-27 (kev-window.txt row, catalogue 2026.11.27 dateAdded 2026-11-27) lists CVE-2026-136716, so the published entry now asserts a falsehood and its CVE-2026-136716 status lacks cisa-kev. The run notes dispose of it as KEV bookkeeping (PD-13), but the stale sentence is not bookkeeping: append a correction or improvement record on the Drupal entry (suggested query: 'CISA KEV CVE-2026-136716 Drupal 2026-11-27'). Medium confidence on whether to float it; the false sentence needs a fix either way."
- code: F11
  category: editorial-advisory
  section: update-section
  item: "2026-11-25/geoserver-five-step-unauthenticated-rce-chain-public-poc, section Update 2026-11-28T04:50:22Z (claim 44d240bad1)"
  url_or_quote: "(low confidence) \"CVE-2026-120705, the unauthenticated XML injection in the WFS GetFeatureById stored query, and CVE-2026-129243, the service-level authorization bypass through a prefixed service name\" ([CISA, 2026-11-27])"
  summary: "(low confidence) The CISA page carries only 'OSGeo GeoServer XML Injection Vulnerability' and 'OSGeo GeoServer Incorrect Authorization Vulnerability'; the appositive descriptors come from the GeoServer advisories cited earlier in the entry. True, but add the GeoServer citation or trim the descriptors."
- code: F11
  category: editorial-advisory
  section: body
  item: "2026-11-28/kudelski-offensive-ai-identity-lifecycle-insurer, Detection last sentence (claim 539f771576)"
  url_or_quote: "(low confidence) \"The sequence to alert on is a burst of identification requests, then accounts created in the names of existing customers without their original passwords, then sensitive information accessed by those accounts.\""
  summary: "(low confidence) The sentence is the entry's synthesis of the executive-summary order and the detection row 'Newly created accounts accessing sensitive information'; the sourcing_note itself says 'The post gives no ordered attack chain'. Say it is derived from the post's listing order. May be left."
- code: F11
  category: editorial-advisory
  section: sources
  item: "2026-11-28/sap-github-environment-intrusion-project-granite, Inside IT citation (claim 8014ef906a)"
  url_or_quote: "(low confidence) \"Inside IT reports an existing S/4HANA landscape in the canton of Zurich's administration\" (https://www.inside-it.ch/zuercher-finanzverwaltung-vergibt-auftrag-fuer-sap-migration-20261127)"
  summary: "(low confidence) The S/4Hana-Landschaft sentence is in the page's embedded article JSON ('Diese muss ... in die bestehende S/4Hana-Landschaft der kantonalen Verwaltung integriert werden'); the visible text is a Plus paywall teaser that says only 'Ablösung ihres bestehenden SAP-Systems durch eine modernere SAP-Lösung'. A reader cannot confirm it. Consider noting the paywall in the sourcing_note. May be left."
- code: F11
  category: editorial-advisory
  section: title-summary
  item: "2026-11-28/freeradius-3-2-11-critical-ttls-use-after-free, title and summary (claims f74aa1646b, ec0399ec66)"
  url_or_quote: "(low confidence) \"no exploitation stated and no proof of concept for the Critical flaw\" / \"the project states no exploitation and no proof of concept\""
  summary: "(low confidence) The page is silent on exploitation and on a PoC for the Critical flaw; 'the project states no exploitation' can be read as 'the project says there is none'. Word as 'the project mentions no exploitation or proof of concept'. The body wording is clear."
- code: F11
  category: editorial-advisory
  section: sources
  item: "2026-11-28/cacti-1-2-31-4http2root-guest-session-rce-zero-day, source 'Previdian (VULN-2026-0010)' dated 2026-11-28"
  url_or_quote: "(low confidence) sources[].date 2026-11-28 for https://previdian.com/VULN-2026-0010"
  summary: "(low confidence) The tracker's own dateline is 'Published 26 Nov 2026', 'Updated 28 Nov 2026'; the live counters read 248 attempts from 23 addresses on this pass against the 216 and 21 the sourcing_note records for 04:35 UTC. The note already says the counts keep changing; label the source 'as read' like the Cacti documentation record."
```
