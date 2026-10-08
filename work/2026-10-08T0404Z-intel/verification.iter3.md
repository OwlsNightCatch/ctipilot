**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-08T05:49:35Z · ended_at=2026-10-08T06:06:05Z · duration_seconds=990

## Verification report — 2026-10-08T0404Z-intel (iteration 3)

Scope covered: all 217 ledger claims have a verdict row in `work/2026-10-08T0404Z-intel/verification.iter3.claims.yaml` (214 ok, 2 F5, 1 unreadable). That is every changed claim (16), every claim of every remediated entry (FortiBleed, Zammad, Atlassian, older SonicWall, Power BI, BigDiskBuster), and the remaining entries in full as well (new SonicWall, FortiMail, Ixa), so the "random quarter" was exceeded. Every cited URL was fetched this iteration: `extract` (BleepingComputer x6, SecurityWeek x3, Fortinet blog, Arctic Wolf, SOCRadar, SANS ISC, Previdian, Atlassian advisory and tickets, watchTowr, Horizon3, Zammad advisory/release/forum, DIVD pages, NCSC-NL, Huntress, LevelBlue, Dark Reading, THN, CERT-FR, Belnet, Cyber Centre, ICTjournal, cash.ch, Inside IT, Le Temps lead), `pdf` (FBI/USSS JCSA-20261006-01 including its footnotes), `ncsc-csh post` (13027, 13032, 13034), `cisa-kev` (catalogVersion 2026.10.04), the GitHub advisory-records API (76 records), the DIVD log-check script, the Fortinet FG-IR-26-175 page, and WebFetch for the CISA alert and the SonicWall 0016 SPA (the latter returns only a title). Sections outside the ledger that this run edited (FortiBleed Update 2026-06-20 and 2026-06-23, Zammad Update 2026-10-07) were read against their sources too.

### Prior-iteration deltas walked (all 11)
1. Zammad 2026-10-07 section: the high-rated sentence now cites the API records. GHSA-gvvq-mfj3-g56x ("Remote code execution via template sanitizer bypass in automation configuration"), GHSA-23hj-h8w6-rgm3 ("Session identifier disclosed in authenticated configuration response enabled off-host session takeover") and GHSA-h5pm-rjvp-fr47 ("Second-order SQL injection in ticket overview sorting") are all high, `<= 7.2.0`. The 27/2/12/10/3 breakdown and "no CVE id" hold. Correct. The listing index is still in `sources[]` (F2).
2. BigDiskBuster Exposure: the standard-account clause is cited to Dark Reading ("researchers found BigDiskBuster can run successfully under a standard user account"). Correct.
3. Power BI: summary says "the configuration of one of the rogue clients also appeared on 22 other endpoints" (Huntress: "client and configuration associated with one of the RMMs ... also impacted 22 other endpoints across separate incidents"); title and headline carry "in one incident" / "in one case" (Huntress: "In one incident ... uninstallation of the first ScreenConnect instance"). Correct.
4. FortiBleed Exposure: matches Fortinet's blog (reuse of previous-incident credentials; reset "especially on internet-facing systems") and BleepingComputer 2026-06-18 (Beaumont: "many affected devices were running relatively recent FortiOS versions"). Correct.
5. FortiBleed first sentence: "reported on 2026-06-18", BleepingComputer datePublished 2026-06-18. Correct.
6. Atlassian sourcing_note: "the Canadian Cyber Centre cites unnamed open-source reporting" matches AV26-1002 Update 1. Correct.
7. Older SonicWall: chaining sentence now follows SecurityWeek ("which suggests they have been chained in attacks") and BleepingComputer ("threat actors are chaining"); no em dash remains in title, `cves[].affected`, actions or body; record summary ends at the hotfix sentence. Correct.
8. FortiBleed uncited legacy text: the Shadowserver/residential-IP clause is gone and replaced by Fortinet's advice (verbatim in the blog); the sniffer sentence cites BleepingComputer 2026-06-22 ("This tool reportedly connects to FortiGate devices over SSH and launches the FortiOS diagnose sniffer packet command"). Correct.
9. FortiBleed 45-GPU vs 36-GPU: both stated with who gave each (Diachenko, BleepingComputer 2026-06-18; Beaumont, BleepingComputer 2026-06-22). Correct.
10. FortiBleed 06-20 section: "hardening alert"; CISA page title "CISA Urges Hardening Fortinet Devices After Reports of Credential Exposure". Correct.
11. Registry Ixa summary: no "SA". Correct. FortiBleed registry relations, Power BI product key and Ixa incident record agree with the entries.

### Strengthen / generic URLs
- F2 (low confidence) Zammad `sources[]` still lists `https://github.com/zammad/zammad/security/advisories` (listing index), cited nowhere in the body after the iteration-2 fix. Remove or swap for a specific GHSA page.

### Citation does not support the claim
- F3 (low confidence) FortiBleed Update 2026-06-23, first paragraph: FortigateSniffer / SNIFTRAN / "~24 protocols" is cited to BleepingComputer 2026-06-22 and "SOCRadar, 2026-06-16" (the blog post). The blog (datePublished 2026-06-16, read in full) has no sniffer, SNIFTRAN, PCAP or protocol-count text; BleepingComputer attributes the details to a separate SOCRadar whitepaper.
- F3 (low confidence) Older SonicWall, remediation-guidance sentence cited to the PSIRT SPA, which no transport renders with that text (claim `e5964f5f08`, `unreadable`). BleepingComputer 2026-09-02 and The Hacker News 2026-10-07 attribute the guidance to SonicWall and read cleanly; add them to the clause.

### Analytical-link-as-fact
- F13 (low confidence) FortiBleed `sourcing_note`: "its device count and the INC/Lynx link rest on SOCRadar's reporting". The FBI/USSS advisory footnotes SOCRadar only for the 86,644 / 194-country figure; its ransomware paragraph says "Reporting indicates initial access brokers ... INC/Lynx ransomware and Payload ransomware" and names no source. BleepingComputer reports the FBI line and SOCRadar's July INC/Lynx link as two separate facts.

### Claims missing inline citation
- F5 (low confidence) Older SonicWall, second paragraph: "a 2026-07-14 entry covers CVE-2026-15409/CVE-2026-15410, an SSRF-to-command-injection pair on a different endpoint pair, exploited for weeks before disclosure and later abused by ransomware affiliates per CISA. No source ties this new chain to the same UTA0533 cluster" has no link; BleepingComputer 2026-09-02 (already cited) carries the "exploited for weeks" and CISA ransomware facts, and "UTA0533" appears in none of the entry's cited sources.

### Editorial / less-is-more flags (advisory)
- F11 Older SonicWall: "a 2026-07-14 entry covers" is a store self-reference.
- F11 (low confidence) FortiBleed 2026-10-08 record summary ends with a sentence about the June sections that the new section does not state.
- F11 (low confidence) Atlassian: record summary "the Canadian Cyber Centre now says the flaw is exploited" is stronger than "Open source reporting indicates ... is being exploited in the wild", and body paragraph 1 says "exploitation attempts against self-managed instances" where the observations are honeypot sensors.

### Action-item discipline
- F18 (low confidence) Older SonicWall actions[0] and new SonicWall actions[0] both carry "install 12.4.3-03670 or 12.5.0-03082 (or higher)".

### Notes that are not findings
- KEV (read directly, catalogVersion 2026.10.04): CVE-2026-104286 (2026-10-01), CVE-2026-83548 and CVE-2026-83549 (2026-09-02), CVE-2026-102489 and CVE-2026-102490 (2026-10-02) listed; CVE-2026-21589 and CVE-2026-102255 not listed. Newest addition CVE-2026-88779 (2026-10-04) is covered, as the run record says.
- Previdian's live page now reads 150 attempts, 23 addresses, eight countries; the entry's "at least 129 / at least 22 / eight countries" is still true. Previdian's JSON-LD dates (published 2026-10-05, modified 2026-10-07) differ from the visible "Updated 08 Oct 2026" the entry cites; accepted as the visible dateline of a live telemetry page.
- Priorities, classification and actions: no `org_triage` block or `watchlist` tag anywhere; Ixa `notable`, Power BI and BigDiskBuster `notable`, new SonicWall `high` (unexploited but pre-auth CVSS 10.0 on an edge gateway whose two sibling flaws this year were exploited and whose September hotfix builds are affected), Atlassian `high`, Zammad `high`, FortiBleed `high` and FortiMail `critical` are defensible; classification codes agree with the source tiers. No IOCs, no vanity metrics, no em dash outside the append-only 2026-06-23 record summary.
- Run record notes: counts (4 new, 5 updated), the KEV sweep, the borderline-drop dispositions I could check (Cisco, ILIAS, HPE ClearPass/AOS-Switch not re-read) and the Contradiction line (cash.ch/AWP gives no date, ICTjournal 25 September, Inside IT end of September) hold.

### Missed angles
None evidenced. The NCSC-CH hub listing (ILIAS 13035, Atlassian 13032, SonicWall 13034) and the KEV catalog show nothing newer than the run covered; a standard web search for exploited zero-days on 2026-10-07 returned nothing newer than 2026-10-02. Coverage looks complete for the critical and high signal.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 2, advisory: 3)

All nine items are low-confidence or small: the SOCRadar co-cite (F3), the `sourcing_note` provenance sentence (F13) and the orphan listing index (F2) are the ones worth fixing. The delta remediations themselves are all correct; no remediation introduced a new error.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (Update 2026-06-23T04:52:50Z, first paragraph)"
  item: "(low confidence) SOCRadar blog co-cited for FortigateSniffer / SNIFTRAN / ~24 protocols"
  url_or_quote: "\"a second tool, **SNIFTRAN**, converts the captured traffic to PCAP, which a Python toolkit then parses for cleartext credentials, NTLM hashes, Kerberos tickets and LDAP/SQL auth material across ~24 protocols ([BleepingComputer, 2026-06-22](https://www.bleepingcomputer.com/news/security/fortibleed-campaign-used-custom-fortigate-sniffer-to-steal-credentials/); [SOCRadar, 2026-06-16](https://socradar.io/blog/fortibleed-fortinet-firewalls-compromised/))\""
  summary: "BleepingComputer 2026-06-22 carries all of it and attributes it to SOCRadar's whitepaper (socradar.io/resources/whitepapers/dismantling-fortibleed-inside-a-russian-fortinet-compromise-operation/). The co-cited SOCRadar blog post (datePublished 2026-06-16, fetched in full as raw HTML and text this iteration) contains no 'FortigateSniffer', 'SNIFTRAN', 'sniffer', 'PCAP' or '24 protocols'. Drop the SOCRadar blog from this clause or cite the whitepaper. The run edited this section (paragraphs 2 and 3) so the paragraph is in scope."
- code: F13
  category: analytical-link-as-fact
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (sourcing_note)"
  item: "(low confidence) FBI advisory's INC/Lynx link said to rest on SOCRadar"
  url_or_quote: "\"The FBI and Secret Service advisory is the primary source for the October developments; its device count and the INC/Lynx link rest on SOCRadar's reporting, which BleepingComputer also relays.\""
  summary: "Sources on the entry: the FBI/USSS advisory footnotes SOCRadar (note 1/2) only for 'more than 86,644 compromised devices across 194 countries'; its ransomware paragraph reads 'Reporting indicates initial access brokers (IABs), utilizing the FortiBleed attack chain, have provided further access to ransomware affiliates, currently including INC/Lynx ransomware and Payload ransomware' with no source named. BleepingComputer 2026-10-07 reports the FBI line and, separately, that 'In July, SOCRadar linked FortiBleed to the INC and Lynx ransomware operations'; neither says the FBI relies on SOCRadar for it. Say that the device count rests on SOCRadar and that SOCRadar separately linked the campaign to INC/Lynx in July."
- code: F2
  category: generic-url
  section: "entries/2026-10-02/zammad-cve-2026-102489-102490-exploited-divd-breach (sources[])"
  item: "(low confidence) GitHub advisories listing index left in sources[] with no inline citation"
  url_or_quote: "https://github.com/zammad/zammad/security/advisories"
  summary: "The iteration-2 remediation re-cited the high-rated-advisories sentence to the API records but left the listing index in sources[] (role corroborating, date 2026-10-06); no body sentence cites it any more. It is a listing index, not a specific advisory (Zammad's own release page and forum post point readers to it, which is why this is low confidence). Remove it from sources[] or replace with a specific GHSA page; the other GHSA pages and the API records are already listed."
- code: F5
  category: missing-citation
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection (body, second paragraph)"
  item: "(low confidence) legacy uncited statements about the July chain and UTA0533 in an entry whose body this run edited"
  url_or_quote: "\"a 2026-07-14 entry covers CVE-2026-15409/CVE-2026-15410, an SSRF-to-command-injection pair on a different endpoint pair, exploited for weeks before disclosure and later abused by ransomware affiliates per CISA. No source ties this new chain to the same UTA0533 cluster or any other named actor\""
  summary: "No inline link on the sentence. BleepingComputer 2026-09-02 (already cited in the entry) says the July flaws 'were exploited in zero-day attacks for weeks' and 'CISA ... confirmed that ransomware gangs have begun abusing the two vulnerabilities'; THN 2026-10-07 gives the SSRF-plus-administrator-command-injection pairing. 'UTA0533' and 'on a different endpoint pair' appear in none of the entry's cited sources. Add the BleepingComputer cite and either source UTA0533 or drop the name."
- code: F11
  category: editorial-advisory
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection (body, second paragraph)"
  item: "store self-reference in reader-facing prose"
  url_or_quote: "\"a 2026-07-14 entry covers CVE-2026-15409/CVE-2026-15410\""
  summary: "'a <date> entry covers' is the 'see the <date> entry' pattern the style rule bars from reader-facing text; the entry already lists the 2026-07-14 entry in references[]. Say what the July chain was (CVE ids, exploited for weeks, CISA ransomware note) and cite BleepingComputer."
- code: F11
  category: editorial-advisory
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (updates[] 2026-10-08T04:58:53Z summary)"
  item: "(low confidence) record summary narrates edits to earlier sections the new section does not state"
  url_or_quote: "\"The June sections now attribute the Russian-speaking actor and the GPU cluster to researcher Bob Diachenko's claims and cite Fortinet's position to its own blog.\""
  summary: "The '## Update — 2026-10-08T04:58:53Z' section states only the FBI/USSS advisory content; the sentence describes record-keeping on the June text, so the summary says more than the section (check 4c(d)). End the summary at the REST API key / PBKDF2 sentence."
- code: F11
  category: editorial-advisory
  section: "entries/2026-10-06/cve-2026-21589-atlassian-data-center-arbitrary-file-access (updates[] 2026-10-08T04:56:05Z summary; body paragraph 1)"
  item: "(low confidence) two wordings stronger than the sources"
  url_or_quote: "record summary: \"the Canadian Cyber Centre now says the flaw is exploited\"; body: \"exploitation attempts against self-managed instances have been observed since 2026-10-06 ([Previdian, 2026-10-08])\""
  summary: "The Cyber Centre bulletin says only 'Open source reporting indicates that CVE-2026-21589 is being exploited in the wild' (the update section words it correctly). The attempts Previdian and SANS ISC record are against their own honeypot sensors (BleepingComputer: 'detected the activity on its honeypot network'; SANS: 'hitting our honeypot'), not against reported victim instances; the first body paragraph does not say honeypot. Reword both."
- code: F18
  category: action-item-discipline
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection (actions[0]) vs entries/2026-10-08/cve-2026-102255-sonicwall-sma1000-workplace-ssrf (actions[0])"
  item: "(low confidence) same patch task carried by two entries"
  url_or_quote: "older: \"... then the later hotfix 12.4.3-03670 or 12.5.0-03082 (or higher), because the first pair is affected by CVE-2026-102255 ...\"; new: \"Install SonicWall's platform hotfix 12.4.3-03670 or 12.5.0-03082 (or higher) on every SMA1000 6210, 7210 and 8200v, including appliances already on the 12.4.3-03526 or 12.5.0-02952 hotfix from September ...\""
  summary: "Check 10b(d): the aggregated Action Items would list the later-hotfix install twice if both entries fall in a reader's window. Keep the task on the new CVE-2026-102255 entry and leave the older entry's first action to its own two flaws (or point to the new entry in the body only)."
- code: F3
  category: claim-not-supported
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection (body, last paragraph before the Improvement section)"
  item: "(low confidence) SonicWall remediation guidance cited to a PSIRT page no transport renders with that text"
  url_or_quote: "\"SonicWall's own remediation guidance where indicators of compromise are found is unusually direct: re-image or re-deploy the appliance, change every user and administrator password, and reset TOTP tokens, treating successful exploitation as compromising stored credentials and MFA seeds, not just the appliance itself ([SonicWall PSIRT](https://psirt.global.sonicwall.com/vuln-detail/SNWLID-2026-0016))\""
  summary: "The PSIRT page is an SPA; extract (jina fallback), the raw bridge and WebFetch return only the two CVE texts and the IMPORTANT exploitation note, with no remediation text (claim e5964f5f08 is unreadable). BleepingComputer 2026-09-02 ('the company also advised admins to re-image appliances, change all user and administrator passwords, and reset TOTP tokens if indicators of compromise (IOCs) are detected') and The Hacker News 2026-10-07 ('In its July and September advisories, SonicWall told customers to ... re-image or redeploy the appliance, change user and administrator passwords, and reset the TOTP tokens') both read cleanly and attribute it to SonicWall; add them to the clause. 'Treating successful exploitation as compromising stored credentials and MFA seeds' is the entry's own reading."
```
