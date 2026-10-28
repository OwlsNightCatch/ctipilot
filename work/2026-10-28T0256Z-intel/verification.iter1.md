**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-28T04:03:23Z · ended_at=2026-10-28T04:33:21Z · duration_seconds=1798

## Verification report — 2026-10-28T0256Z-intel (iteration 1)

Scope: 5 new entries, 8 updated entries (diffs read with `git diff HEAD`), run record. Claim ledger `claims.iter1.yaml`: 271 claims, 271 verdict rows written to `verification.iter1.claims.yaml` (241 ok, 13 unreadable, 17 non-ok mapped to the findings below). Unreadable: ransomware.live record for Manno (timeout on every transport), the Citrix Tech Zone post (HTTP 403 on extract, url, jina and WebFetch; 10 claims across NetScaler and PHP entries), nippon.com (404). No prior-iteration deltas (first pass).

### Broken / unreachable URLs
- **#1 (F1)** `entries/2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups`: `https://www.nippon.com/en/news/yjj2026100700867/` ("Jiji Press via nippon.com, 2026-10-07") answers HTTP 404 (WebFetch) and the bridge returns only the site navigation, no article. No source read this iteration states "the websites of Ibaraki Prefecture and the city of Kodaira" (body paragraph 1) or "Jiji Press, which reports the downstream website failures" (sourcing_note). Replace the URL or drop both clauses.

### Citation does not support the claim
- **#2 (F3)** `cisco-php2shell-expressway-urwb-duo-access-gateway-fixes`: body "ISE Portal Builder is offline for remediation, where the attacker must be authenticated as an administrator, which lowers its CVSS 3.1 score to 6.6"; `cves[].affected` "and, with an administrator login, Identity Services Engine Portal Builder"; sourcing_note "The advisory carries no CVSS score except for ISE Portal Builder"; evidence[2] "For this product, the attacker must be authenticated as an administrator...". Live Cisco page (v1.8): `<td>Ultra-Reliable Wireless Backhaul (URWB)<sup>1,2</sup><br>Unified Industrial Wireless Software</td>` carries footnote 1 (admin required, score reduced to 6.6); `<td>Identity Services Engine (ISE) Portal Builder</td>` carries no footnote. The PHP entry's own 2026-10-24 section assigns the admin condition to URWB. Four places to correct.
- **#3 (F3)** `hpe-clearpass-php2shell-hotfixes-hpesbnw05171`: body "until the ClearPass instances run the hotfixed 6.14.1 or 6.11.16, which it describes as versions providing some level of mitigation", summary "until the hotfixed versions run", takeaway "the hotfix is described as a mitigation level, so check HPE's bulletin for a full fix". CSAF: "until ClearPass instances have been upgraded to a version providing some level of mitigation. These versions are 6.14.1 and 6.11.16." No "hotfix"; the same bulletin lists 6.14.1/6.11.16 as affected ("and below"); the hotfix patches are `remediations[0]` category `vendor_fix`. The entry's reading turns the vendor's fix into a "mitigation level". Quote HPE's wording, add a Contradiction line.
- **#4 (F3, low confidence)** `deadtag-...`: "does nothing for bots, scanners or repeat visits from data-centre addresses" vs Report URI "When we investigated from data-centre IP addresses, or came back too often from residential IP addresses, the operators simply stopped answering."
- **#5 (F3, low confidence)** `cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix`: "...and treat the Brotli flaw as exploited ([.NET Blog, 2026-10-25])": the blog says nothing about exploitation; move the CISA cite to the clause.

### Unsupported / hallucinated facts
- **#6 (F4, low confidence)** Cisco entry: "version ranges are in the Cisco bug records CSCwx37062 and CSCwx37073" (cves[].affected, Exposure, body). The advisory says the bugs hold "additional platform-specific information, including workarounds (if available) and fixed software releases", not affected ranges; the sourcing_note concedes the bug records were not read.

### Quantifier without source
- **#6b (F14, low confidence)** `idc-frontier-idcf-cloud-ransomware-495-customers-backups`: "final report" in title, summary, body, sources[] publisher ("seventh and final report"), sourcing_note and record summary. https://www.idcf.jp/news/topics/20261027001 is 【第7報】 and says 本件に関する一連の調査が完了しました; it never calls itself final and announces a three-stage portal reopening still to come. Say "seventh report".
- **#6c (F14, low confidence)** Cisco entry body "lists four products as affected": the table names six items, the entry's own `affected_products[]` has six, and the page gives no count.

### Claims missing inline citation
- **#7 (F5)** `camping-care-...` 2026-10-28 section and record summary: "rests on SRF, Blick and the TCS statements". No cited source carries a TCS statement tying the theft to PHP (SRF's PHP framing is its own voice). Watson/Keystone-SDA (https://www.watson.ch/schweiz/digital/154077128-tcs-camping-meldet-datenleck-nach-php-sicherheitsluecke) does: "Betrüger konnten im Zusammenhang mit der internationalen Sicherheitslücke bei der Programmiersprache PHP ... entwenden, wie ein Sprecher des Touring Club Schweiz (TCS) ... bestätigte." Add it to sources[] and cite the clause.
- **#8 (F5)** `cve-2026-102788-102789-balbooa-...` body paragraph 1: "which previously inserted the value into the query's ORDER BY clause" is uncited and reads as Balbooa's account; Balbooa says only "strict whitelist validation against getBlogPostsSortingList()". The ORDER BY detail is in mySites.guru and the CNA record.

### Drop (low relevance / off-audience / duplicate)
- **#9 (F7, low confidence)** Balbooa Gridbox entry (`notable`): read-side unauthenticated SQLi in a third-party Joomla extension, "no public report of exploitation yet", no PoC, no Swiss or public-sector exposure shown (regions global, sectors empty); the run drops comparable no-exploitation items as borderline. Only the July Gridbox wave argues for keeping it.

### Needs more research
- **#10 (F8)** Cisco Detection "Cisco publishes no indicator ... only telemetry is the generic PHP2Shell pattern": the advisory lists "Snort Rule 67359, Snort Rule 67360" as action links.
- **#11 (F8)** PAN-OS Detection "so no post-compromise check is defined": with vendor-reported exploitation, the contract wants the compromise check; the cited KEV JSON carries `forensicTriage: Yes` for both PHP CVEs (BOD 26-04 check-before-patch expectation).
- **#12 (F8)** Node2Shell `affected_products`/`cves[].affected`: omit Bun (named by NCSC and by the entry's own 2026-10-27 section), Istio (Tenable), Ruby brotli gem, Debian bookworm/trixie, Alpine (ELLIO fix table), PowerShell and Visual Studio (NCSC).
- **#13 (F8)** DeadTag: iVerify's "DeadTag appears to be mostly focused on European domains versus .com" (the only nexus statement for a Swiss SOC) dropped out; regions says global.
- **#14 (F8, low confidence)** IDC Frontier 2026-10-28 section: seventh report also confirms up to four customer portal login passwords were improperly changed and reset.

### Surface contradiction
- **#15 (F9)** PAN-OS entry (and PHP section, record summaries): "revised its advisory on 2026-10-27 (16:40 UTC) to record that active exploitation has been observed". The vendor timeline's last entry is 2026-10-27T16:40 "Severity Updated to Critical and Urgency updated as Highest". The Wayback copy of the HTML taken 2026-10-27T17:10:28Z (`https://web.archive.org/web/20261027171028/https://security.paloaltonetworks.com/CVE-2026-109618`) reads "Very limited exploitation has been observed targeting the Palo Alto Networks management interface."; the live page and the 03:34 UTC copy read "Active exploitation has been observed targeting the Palo Alto Networks management interface exposed to the internet." The vendor strengthened the sentence after 17:10 UTC with no timeline record. Do not date "active" to the 16:40 revision; add a Contradiction line. (This also supports `high` rather than `critical` for the PAN-OS entry.)

### Editorial / less-is-more flags (advisory)
- **#16 (F11)** Headlines of Manno and ARA Lyss state publication and contents without "reports Inside IT / per Risikomonitor" (single outlet relaying an unverified analysis; B3 and C3); the bodies hedge, the headlines do not.
- **#17 (F11)** Cross-references to the store's own entries in reader-facing text: "described in the PHP entry" (Cisco, HPE Detection), "covered by the entries listed under references" (Cisco, HPE, NetScaler sourcing notes), "the PAN-OS entry carries the hotfix table" (PHP 2026-10-28 section).
- **#18 (F11)** PHP entry main analysis is about 1,940 words (whole entry about 4,065, `deep_dive: false`) for a fire whose delta is one vendor statement.
- **#19 (F11)** PAN-OS `tags` lack `actively-exploited` although `cves[].status` now says exploited; the record's `fields` omit `tags`.
- **#20 (F11, low confidence)** DeadTag `references[]` points to the CoreGraphics zero-day entry; no cited source connects Coruna/DarkSword to CVE-2026-86950.
- **#21 (F11)** IDC Frontier main analysis and Defender takeaway still count "194 of the 495" (dated, correct) without noting the later 206.

### Single-source items missing [SINGLE-SOURCE] flag
None. Cisco, HPE, ARA Lyss, Manno carry `single-source*` values with sourcing notes.

### Action-item discipline
- **#22 (F18, low confidence)** DeadTag actions[0] restates the Detection and takeaway (script audit plus CSP) and its CSP half is generic hardening; narrow to the one start-now task (list third-party script domains on public sites, check each for a registrar change).

### Missed angles
None evidenced. Coverage of the window looks complete against the run's borderline-drop lines (Magento KEV CVE-2026-48356 dropped with a stated reason; Oracle CPU, Chrome, Apple, Mozilla, GLPI items out of nexus or unexploited). Two items the run itself could not read stay unverified: the Juniper PHP2Shell reference advisory and any QNAP QSA-26-18 revision after 2026-10-27 (no search returned a Juniper product list).

### Checks that passed (not findings)
Palo Alto advisory facts (severity, 9.2/7.7, eleven hotfixes, nine ETAs, Threat IDs, FAQ) re-verified on the live JSON and HTML; KEV dateAdded 2026-10-26 (PHP) and 2026-10-27 (Brotli, Magento) on catalogVersion 2026.10.27; CISA alert "based on evidence of active exploitation"; ELLIO telemetry and the "zero hits in 50 attempts" qualifier are both carried correctly (headline, summary and body say traffic recorded but the chain got no shell); Cisco X15.5.20 vs 15.5.21 distinction correct (cluster advisory names X15.5.20 for CVE-2026-76466); Citrix CTX697263 revision 2026-10-27 and CERT-FR AVI-1394 builds; IDC Frontier 7th report facts (cause, 71, 206, remediation list) and its Japanese quotes verbatim; Inside IT/Risikomonitor figures for Manno and ARA Lyss and the BACS attribution; Manno PDF notice; MSRC CVE-2026-111497 and CVE-2026-70197 exploitability fields; Gridbox CNA records (CVSS 4.0 9.3, 1.0.0-2.20.4.1); Report URI/iVerify facts, iOS ranges, no attribution of DeadTag (both say "we don't know"); Hüttenberg notice and Netzwoche quotes verbatim; no em dashes, no workflow vocabulary, no IOCs in any entry.

### Verdict
NEEDS_FIXES (truth: 8, editorial: 10, advisory: 6)

### Findings summary (machine-readable)
See `work/2026-10-28T0256Z-intel/verification.iter1.findings.yaml` (24 records).
