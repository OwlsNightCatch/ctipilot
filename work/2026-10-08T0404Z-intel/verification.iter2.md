**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-08T05:31:41Z · ended_at=2026-10-08T05:46:31Z · duration_seconds=890

## Verification report — 2026-10-08T0404Z-intel (iteration 2)

Scope covered: all 212 ledger claims have a verdict row in `work/2026-10-08T0404Z-intel/verification.iter2.claims.yaml` (206 ok, 4 F3, 1 F4, 1 unreadable). That is every changed claim (43), every claim of the entries the deltas block names (FortiBleed, Atlassian, Zammad, Power BI, BigDiskBuster, Ixa, the new SonicWall entry, the older SonicWall entry), and all FortiMail claims (the FortiMail entry is read against a fresh Fortinet PSIRT fetch, BleepingComputer, NCSC-CH 13027, NCSC-NL, Belnet and the CISA alert). Every cited URL was fetched this iteration (`extract`, `pdf` for the FBI/USSS advisory, `ncsc-csh post`, `cisa-kev`; the CISA alert and the SonicWall 0016 page through WebFetch). Sections outside the ledger (FortiBleed Update 2026-06-20 and 2026-06-23, Zammad Update 2026-10-07) were also read against their sources because this run edited them.

### Prior-iteration deltas walked
1. FortiBleed MD5-crypt: no "MD5" string remains in the entry. The 2026-06-20 section now says CISA urges "storing administrator logins with PBKDF2" (SecurityWeek 2026-06-19 has exactly that). The October section's "legacy SHA-256 password storage" is in the FBI/USSS advisory. Correct.
2. FortiBleed evidence: all four quotes are contiguous substrings of their `source_url` pages (BleepingComputer 2026-06-22, SecurityWeek 2026-06-22, BleepingComputer 2026-10-07 twice). Correct.
3. FortiBleed paragraph 1: BleepingComputer 2026-06-18 attributes the Russian-speaking group, the 45-GPU Hashtopolis cluster, Active Directory movement and the "fully compromised" organisations to Diachenko ("He further claimed ..."). Correct. The same paragraph still labels the BleepingComputer link 2026-06-17 (page date 2026-06-18, see F3 #5).
4. FortiBleed 2026-06-20 section: SecurityWeek 2026-06-19 carries the Diachenko quote ("crack hashes on a 45-GPU cluster managed via Hashtopolis") and the five CISA items. Correct. "emergency" is an overstatement (F11).
5. Atlassian NCSC-CH 13032: the post carries "UNKNOWN" and, after the 2026-10-07 edit, "Proof of Concept Available". "Lists the status as proof of concept available and does not report exploitation" is right.
6. Zammad severity breakdown: the API records give 27 published 2026-10-06, 2 critical, 12 high, 10 medium, 3 low, all `<= 7.2.0`, patched 7.2.1, no CVE id. The count sentence is right. The next sentence of the same section ("Among the high-rated advisories ...") still cites the listing index (F3 #1).
7. Power BI: title, headline and body no longer present a public dashboard as this campaign's fact; the body attributes it to Huntress's note and says Huntress does not describe how this campaign's page was set up. Correct. The rewritten summary introduces a new error (F4 #3).
8. BigDiskBuster Exposure: "needs only" is gone. The replacement attributes the standard-account run to LevelBlue; only Dark Reading says it (F3 #2).
9. MRT.exe: LevelBlue writes "MRT.exe" and "MRT handle". Correct.
10. Run record Contradiction line: cash.ch/AWP says "Rund einen Monat später ... zum Verkauf angeboten" with no date; only ICTjournal gives 25 September. Correct.
11. FortiBleed Fortinet sentence: now matches Fortinet's blog ("we believe the activity involves threat actors reusing credentials from previous incidents and employing brute-force techniques ..."; "This is not a new Fortinet vulnerability"). Correct.
12. FortiBleed Exposure, Detection, Defender takeaway: Detection and takeaway match Fortinet's blog; the Exposure line goes beyond it (F3 #4).
13. FortiBleed source order: BleepingComputer first, FBI/USSS and Fortinet next, with the sourcing_note naming the FBI/USSS advisory as the primary for October. Defensible under the lifecycle rule; not re-raised.
14. FortiBleed em dashes and the inline T1078: none left in the body. The append-only 2026-06-20 and 2026-06-23 record summaries are untouched, as stated.
15. Fetch narration: gone from the SonicWall and Ixa sourcing notes and the Zammad update.
16. Power BI `product:microsoft-power-bi` is keyed.
17. FortiMail stays `improvement`: Fortinet's page adds the Cloud clarification (timeline 2026-10-07), `fields` match the diff, `updated_at` is unchanged. Acceptable for a scope-narrowing note on an entry already at the top of the brief.
18. Older SonicWall entry: new improvement record, summary, first action, sources and section are consistent with The Hacker News 2026-10-07 (12.4.3-03526 and 12.5.0-02952 affected by the new flaw, 12.4.3-03670 and 12.5.0-03082 and higher fixed). Two older sentences in that entry now in scope are flagged (F3 #7, F11).
19. Atlassian counts: "at least 129 attempts from at least 22 addresses" holds (the live Previdian page now reads 150 attempts and 23 addresses); the `state/cves_seen.json` title now says "exploitation attempts observed since 2026-10-06". Correct.
20. Atlassian log lookback now starts 2026-10-05 (Atlassian advisory date) with the honeypot first-attempt date in brackets. Correct.
21. Ixa: "None of the reports states how the attackers got in" holds for ICTjournal, AWP/cash.ch, Inside IT and the readable Le Temps lead; Exposure names the Établissements de la plaine de l'Orbe and the Banque cantonale vaudoise per ICTjournal. Correct.

### Citation does not support the claim
- #1 Zammad, Update 2026-10-07, second paragraph: "Among the high-rated advisories is a remote code execution through a template-sanitizer bypass in automation configuration, a session identifier readable in a configuration response that enables off-host session takeover, and a second-order SQL injection in ticket overview sorting" is cited to `https://github.com/zammad/zammad/security/advisories`. The listing as fetched shows ten records and none of the three (visible high records: GHSA-852x-r9wm-4v5j, GHSA-f8x4-5mjf-mc32). They are in the API records (GHSA-gvvq-mfj3-g56x, GHSA-23hj-h8w6-rgm3, GHSA-h5pm-rjvp-fr47). The API title for the session flaw reads "Session identifier disclosed in authenticated configuration response", and the entry drops "authenticated". Cite the API records and remove the listing index from the sentence and from `sources[]`.
- #2 BigDiskBuster Exposure: "LevelBlue ran it from a standard user account ... ([LevelBlue SpiderLabs, 2026-10-05])". The LevelBlue post has no such statement. Dark Reading: "researchers found BigDiskBuster can run successfully under a standard user account". Re-cite to Dark Reading.
- #4 (low confidence) FortiBleed Exposure: "may be in the compromised data whatever the patch level" is cited to Fortinet's blog, which says only that credentials from previous incidents are reused and asks for resets "especially on internet-facing systems". The patch-level point is Beaumont's via BleepingComputer 2026-06-18.
- #5 (low confidence) FortiBleed first sentence: "surfaced on 2026-06-17 ... ([BleepingComputer, 2026-06-17])". BleepingComputer's datePublished is 2026-06-18T08:54:39-04:00 and the page says "A newly discovered data leak"; the SOCRadar post the entry also cites is dated 2026-06-16. The same URL is labelled 06-17 and 06-18 in one paragraph.
- #7 (low confidence) Older SonicWall entry: "SecurityWeek and BleepingComputer both report the flaws are being exploited together, with the appliance considered fully compromised once both stages complete ([SecurityWeek, 2026-09-02])". SecurityWeek: SonicWall "has observed exploitation of both vulnerabilities, which suggests they have been chained in attacks". Neither source carries "fully compromised once both stages complete".

### Unsupported / hallucinated facts
- #3 Power BI summary: "the second client's configuration also appeared on 22 other endpoints". Huntress: "the unique ScreenConnect client and configuration associated with one of the RMMs in the attack also impacted 22 other endpoints". The body says "one of the rogue clients", so the summary contradicts it.
- #6 (low confidence) Atlassian sourcing_note: "BleepingComputer and the Canadian Cyber Centre restate the Previdian reporting". The Cyber Centre says only "Open source reporting indicates that CVE-2026-21589 is being exploited in the wild" and names no source.

### Claims missing inline citation
- #8 (low confidence) FortiBleed Update 2026-06-20 last paragraph: "cross-reference SSL VPN session logs against the Shadowserver notification feed ... rotating residential IP ranges"; Update 2026-06-23 last paragraph: "FortiOS audit-logs `diagnose sniffer packet` execution". No fetched source mentions a Shadowserver feed for FortiBleed, residential ranges, or FortiOS audit-logging of the sniffer command.

### Surface contradiction
- #9 (low confidence) FortiBleed: "45-GPU cluster" (Diachenko, BleepingComputer 2026-06-18, SecurityWeek 2026-06-19) in paragraph 1 and the 2026-06-20 section, "36-GPU cluster" (Beaumont via BleepingComputer 2026-06-22) in the 2026-06-23 section. No Contradiction line.

### Editorial / less-is-more flags (advisory)
- #10 Power BI title and headline state "a script replaces/removes the first" without Huntress's "In one incident".
- #11 Older SonicWall entry: em dashes remain in the title, `cves[].affected`, actions[1] and body (the run edited this entry with `body` in `fields`).
- #12 FortiBleed Update 2026-06-20: "CISA has published an emergency hardening advisory"; CISA's alert is titled "CISA Urges Hardening Fortinet Devices After Reports of Credential Exposure" and neither CISA nor SecurityWeek says "emergency".
- #13 (low confidence) `entities/registry.yaml` incident summary says "Ixa Systems SA"; no fetched source gives "SA".
- #14 (low confidence) Older SonicWall record summary ends "the first action now says so", narrating the edit.

### Notes that are not findings
- The older SonicWall entry's "SonicWall's own remediation guidance ... re-image ... reset TOTP tokens ([SonicWall PSIRT])" (claim 0507ad47b2) is `unreadable`: the PSIRT SPA as read through `extract` carries only the CVE texts and the IMPORTANT note (it also omits the version tables that The Hacker News, CERT-FR and the Cyber Centre report for advisory 0017), while BleepingComputer 2026-09-02 and The Hacker News 2026-10-07 both attribute the guidance to SonicWall.
- Priorities, classification and action lists: no org_triage block or watchlist tag on any entry; Ixa `notable` is right under "Doubt resolves to `notable`"; Atlassian `high` (attempts, no compromise) and FortiMail `critical` are defensible; classification codes agree with source tiers in `sources/sources.json`; no entry carries more than two actions and none is generic.
- KEV: read directly (catalogVersion 2026.10.04). CVE-2026-104286 (2026-10-01), CVE-2026-83548 and CVE-2026-83549 (2026-09-02), CVE-2026-102489 and CVE-2026-102490 (2026-10-02) are listed with those dates; CVE-2026-21589 and CVE-2026-102255 are not listed.

### Missed angles
None evidenced. The KEV catalog has nothing newer than 2026-10-04 (CVE-2026-88779, covered by the run's sweep). The NCSC-CH hub listing shows ILIAS (13035, unauthenticated file download only with the public area enabled, no exploitation), SonicWall (13034), Atlassian (13032); the ILIAS drop is logged and defensible. Coverage looks complete for the critical and high signal.

### Verdict
NEEDS_FIXES (truth: 7, editorial: 2, advisory: 5)

Findings #1, #2 and #3 are the ones to fix first: each is a plain citation or summary error on text this run wrote or rewrote. #4 to #9 are lower confidence or sit in legacy sentences of entries the run edited.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: "entries/2026-10-02/zammad-cve-2026-102489-102490-exploited-divd-breach (Update 2026-10-07T04:52:00Z, second paragraph; sources[])"
  item: "Zammad high-rated advisories cited to the repository listing index"
  url_or_quote: "\"Among the high-rated advisories is a remote code execution through a template-sanitizer bypass in automation configuration, a session identifier readable in a configuration response that enables off-host session takeover, and a second-order SQL injection in ticket overview sorting ([Zammad security advisories, 2026-10-06](https://github.com/zammad/zammad/security/advisories))\""
  summary: "The cited listing index, as fetched this iteration, shows only ten records (high ones visible: GHSA-852x-r9wm-4v5j stored XSS in autocomplete, GHSA-f8x4-5mjf-mc32 activity stream disclosure) and none of the three named flaws. They exist only in the GitHub advisory-records API (GHSA-gvvq-mfj3-g56x, GHSA-23hj-h8w6-rgm3, GHSA-h5pm-rjvp-fr47). The iteration-1 fix re-cited only the severity-count sentence. Cite https://api.github.com/repos/zammad/zammad/security-advisories?per_page=100 (or the three GHSA pages) and drop the listing index from the sentence and from sources[]. API title for the session flaw reads 'Session identifier disclosed in authenticated configuration response'; the entry drops 'authenticated'."
- code: F3
  category: claim-not-supported
  section: "entries/2026-10-08/bigdiskbuster-defender-update-starvation-disk-exhaustion-poc (body, Exposure)"
  item: "standard-user-account statement cited to LevelBlue"
  url_or_quote: "\"**Exposure:** Windows endpoints running Defender Antivirus; LevelBlue ran it from a standard user account, and an estate shows the effect as endpoints whose security-intelligence age keeps growing ([LevelBlue SpiderLabs, 2026-10-05](https://www.levelblue.com/blogs/spiderlabs-blog/filling-the-well-nightmare-eclipses-bigdiskbuster-and-the-defender-update-that-never-lands))\""
  summary: "The LevelBlue post as fetched contains no statement about a standard or low-privilege account. The statement is Dark Reading's, quoting LevelBlue's Timmy Lister: 'researchers found BigDiskBuster can run successfully under a standard user account'. Cite Dark Reading for that clause (body paragraph 1 already does)."
- code: F4
  category: hallucinated-fact
  section: "entries/2026-10-08/power-bi-dashboard-phishing-rogue-screenconnect-clients (summary)"
  item: "22 other endpoints attributed to the second client"
  url_or_quote: "\"Huntress could not obtain the original email, and the second client's configuration also appeared on 22 other endpoints.\""
  summary: "Huntress: 'the unique ScreenConnect client and configuration associated with one of the RMMs in the attack also impacted 22 other endpoints across separate incidents'. It does not say which client; the entry body correctly says 'the configuration of one of the rogue clients'. The summary overstates and contradicts the body. Say 'one of the rogue clients'."
- code: F3
  category: claim-not-supported
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (body, Exposure)"
  item: "(low confidence) 'whatever the patch level' cited to Fortinet"
  url_or_quote: "\"**Exposure:** any internet-exposed FortiGate: its administrator and SSL VPN credentials may be in the compromised data whatever the patch level, because patching does not rotate a credential that has already leaked ([Fortinet PSIRT, 2026-06-19](https://www.fortinet.com/blog/psirt-blogs/analysis-of-reported-credential-compromise-of-fortigate-devices)).\""
  summary: "Fortinet's blog says credentials from previous incidents are reused and tells customers to reset VPN and admin passwords 'especially on internet-facing systems'; it does not say credentials may be in the data regardless of patch level or that the exposure covers any internet-exposed device. The nearest support is BleepingComputer 2026-06-18 (Beaumont: 'many affected devices were running relatively recent FortiOS versions'). Re-cite or reword to what Fortinet states."
- code: F3
  category: claim-not-supported
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (body, first sentence)"
  item: "(low confidence) 'surfaced on 2026-06-17' cited to BleepingComputer, same URL labelled 06-17 and 06-18"
  url_or_quote: "\"A dataset branded \\\"FortiBleed\\\" surfaced on 2026-06-17 containing 73,932 unique FortiGate management URLs ... ([BleepingComputer, 2026-06-17](https://www.bleepingcomputer.com/news/security/fortibleed-leak-exposes-fortinet-vpn-credentials-for-73-000-devices/))\""
  summary: "BleepingComputer's JSON-LD datePublished is 2026-06-18T08:54:39-04:00 and the article says only 'A newly discovered data leak'; it gives no 2026-06-17 surfacing date, and the SOCRadar post cited by the same entry is dated 2026-06-16. The same URL is labelled 2026-06-17 in the first sentence and 2026-06-18 later in the paragraph. Use the BleepingComputer publication date for the label and drop or re-source 'surfaced on 2026-06-17'."
- code: F4
  category: hallucinated-fact
  section: "entries/2026-10-06/cve-2026-21589-atlassian-data-center-arbitrary-file-access (sourcing_note)"
  item: "(low confidence) Canadian Cyber Centre said to restate Previdian reporting"
  url_or_quote: "\"BleepingComputer and the Canadian Cyber Centre restate the Previdian reporting, and none of them reports a successful compromise.\""
  summary: "The Cyber Centre bulletin (AV26-1002, Update 1) says only 'Open source reporting indicates that CVE-2026-21589 is being exploited in the wild.' and names no source. Write 'cites unnamed open-source reporting'."
- code: F3
  category: claim-not-supported
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection (body, first paragraph)"
  item: "(low confidence) 'fully compromised once both stages complete' cited to SecurityWeek"
  url_or_quote: "\"SecurityWeek and BleepingComputer both report the flaws are being exploited together, with the appliance considered fully compromised once both stages complete ([SecurityWeek, 2026-09-02](https://www.securityweek.com/sonicwall-warns-of-two-sma1000-zero-days-exploited-in-attacks/))\""
  summary: "SecurityWeek: SonicWall 'has observed exploitation of both vulnerabilities, which suggests they have been chained in attacks' (hedged); BleepingComputer: 'threat actors are chaining two new SMA1000 zero-day vulnerabilities'. Neither says the appliance is considered fully compromised once both stages complete. The run appended a record to this entry with body in fields, so the paragraph is in scope. Drop the clause or hedge SecurityWeek's reading."
- code: F5
  category: missing-citation
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (Update 2026-06-20 last paragraph; Update 2026-06-23 last paragraph)"
  item: "(low confidence) legacy uncited statements in sections this run rewrote"
  url_or_quote: "\"Defenders should cross-reference SSL VPN session logs against the Shadowserver notification feed and hunt for sequential VPN authentication failures from rotating residential IP ranges\"; \"FortiOS audit-logs `diagnose sniffer packet` execution\""
  summary: "No fetched source (BleepingComputer 06-18/06-22, SecurityWeek 06-19/06-22, Fortinet, CISA, FBI/USSS, SOCRadar, Arctic Wolf) mentions a Shadowserver notification feed for FortiBleed or rotating residential IP ranges, or states that FortiOS audit-logs sniffer execution. Either cite or recast as the entry's own hunting suggestion without implying a feed exists."
- code: F9
  category: surface-contradiction
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (body paragraph 1, Update 2026-06-20 vs Update 2026-06-23)"
  item: "(low confidence) 45-GPU and 36-GPU cracking cluster figures"
  url_or_quote: "\"crack the hashes on a 45-GPU cluster managed through Hashtopolis\" (Diachenko, BleepingComputer 2026-06-18) vs \"a distributed 36-GPU cluster (rented from a generative-AI provider, per BleepingComputer)\" (Beaumont, BleepingComputer 2026-06-22)"
  summary: "Two sources give different cluster sizes for the offline cracking; both appear in the entry in separate sections with no Contradiction line. BleepingComputer 2026-06-22 itself says 'Both explanations could account for' the cracking platforms. Add one sentence that the counts differ and who gave which."
- code: F11
  category: editorial-advisory
  section: "entries/2026-10-08/power-bi-dashboard-phishing-rogue-screenconnect-clients (title, headline)"
  item: "one-incident observation stated generally"
  url_or_quote: "title: \"... then a script replaces the first remote-management tool with a second\"; headline: \"... and a script removes the first\""
  summary: "Huntress says the PowerShell script uninstalled the first client 'In one incident'; in all incidents the first client established the second. Summary and body qualify it, title and headline do not. Add 'in one incident'."
- code: F11
  category: editorial-advisory
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection (title, cves[].affected, actions[1], body)"
  item: "legacy em dashes in an entry the run edited"
  url_or_quote: "title: \"CVE-2026-83548 / CVE-2026-83549 — SonicWall SMA1000 ...\"; actions[1] \"... reset TOTP seeds — SonicWall's guidance ...\"; body \"... code execution — SecurityWeek and BleepingComputer ...\", \"... named actor — the recurrence ...\", \"... Work Place session ... supports — a legitimate ...\""
  summary: "The style rule bars em dashes in reader-facing entry text (only the Update heading is exempt). The FortiBleed legacy body was cleaned this run; this entry's legacy dashes were not. Replace with commas or colons."
- code: F11
  category: editorial-advisory
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (Update 2026-06-20 first paragraph)"
  item: "'emergency' not in the cited pages"
  url_or_quote: "\"CISA has published an emergency hardening advisory ([SecurityWeek, 2026-06-19]...; [CISA, 2026-06-18]...)\""
  summary: "The CISA alert is titled 'CISA Urges Hardening Fortinet Devices After Reports of Credential Exposure' and SecurityWeek says 'CISA is urging organizations to harden'. Neither calls it an emergency advisory. Drop 'emergency'."
- code: F11
  category: editorial-advisory
  section: "entities/registry.yaml (incident:ixa-systems-thegentlemen-2026-08 summary)"
  item: "(low confidence) legal form 'SA' not in any fetched source"
  url_or_quote: "\"Ixa Systems SA of Crissier (Vaud)\""
  summary: "AWP via cash.ch, ICTjournal, Inside IT and the Le Temps lead say 'Ixa Systems'; none gives 'SA'. Drop 'SA' unless a source states it."
- code: F11
  category: editorial-advisory
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection (updates[] 2026-10-08T05:30:28Z summary)"
  item: "(low confidence) record-keeping narration in a record summary"
  url_or_quote: "\"Appliances on those builds need the later hotfix, 12.4.3-03670 or 12.5.0-03082; the first action now says so.\""
  summary: "'the first action now says so' narrates the edit. End the summary at the hotfix sentence."
```
