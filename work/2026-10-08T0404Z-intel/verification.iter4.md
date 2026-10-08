**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-08T06:08:03Z · ended_at=2026-10-08T06:25:49Z · duration_seconds=1066

## Verification report — 2026-10-08T0404Z-intel (iteration 4)

Scope covered: all 217 ledger claims have a verdict row in `work/2026-10-08T0404Z-intel/verification.iter4.claims.yaml` (212 ok, 2 F3, 1 F4, 2 F13). That is every changed claim (6), every claim of every remediated entry (FortiBleed, older SonicWall, Zammad, Atlassian), and the remaining entries in full as well (new SonicWall, FortiMail, Ixa, Power BI, BigDiskBuster), so the random-quarter requirement was exceeded. Sections outside the ledger that this run edited (FortiBleed Update 2026-06-20 and 2026-06-23, Zammad Update 2026-10-07) were read against their sources too. Every cited page was fetched this iteration: `extract` (BleepingComputer x8, SecurityWeek x3, The Hacker News, Fortinet blog, Arctic Wolf, SOCRadar, SANS ISC, Previdian, Atlassian advisory, watchTowr (cached body re-read), Horizon3, Zammad advisory/release/forum, DIVD x4, NCSC-NL, Huntress, LevelBlue, Dark Reading, CERT-FR, Belnet, Cyber Centre x2, ICTjournal, cash.ch, Inside IT, Le Temps lead, the Fortinet FG-IR-26-175 page, NCSC-NL FortiMail advisory), `pdf` (FBI/USSS JCSA-20261006-01, footnotes included), `ncsc-csh post` (13027, 13032, 13034) and `recent`, `cisa-kev` (catalogVersion 2026.10.04), the GitHub advisory-records API (76 records, 27 on 2026-10-06), the FIRST EPSS API, and `WebFetch` for the CISA alert and the SonicWall 0017 SPA (title only, as in iteration 3). Cached gate bodies were used only for the Atlassian tickets, watchTowr and the Register HTML.

### Prior-iteration deltas walked (all 8)
1. FortiBleed Update 2026-06-23, first paragraph: now cites only BleepingComputer 2026-06-22 and says "SOCRadar's report, as BleepingComputer describes it, alleges". BleepingComputer: "the alleged use of a Golang-based tool dubbed 'FortigateSniffer'", "SNIFTRAN ... reconstructed the captured traffic into PCAP files", "monitor traffic across 24 protocols". Correct. (The unchanged lead sentence 'the first complete tool-chain picture' is raised as F14.)
2. Older SonicWall remediation sentence: now cites BleepingComputer 2026-09-02 ("advised admins to re-image appliances, change all user and administrator passwords, and reset TOTP tokens if indicators of compromise (IOCs) are detected") and The Hacker News 2026-10-07 ("re-image or redeploy the appliance, change user and administrator passwords, and reset the TOTP tokens"). Correct for the guidance; the trailing "treating ... as compromising stored credentials and MFA seeds" is the entry's own inference (F11).
3. FortiBleed sourcing_note: the FBI/USSS PDF footnotes SOCRadar only for the 86,644 / 194-country figure (notes 1 and 2); the INC/Lynx and Payload sentence carries no footnote; BleepingComputer 2026-10-07 gives "By the SOCRadar's latest count, the FotiBleed compromised 86,644 devices" and, separately, "In July, SOCRadar linked FortiBleed to the INC and Lynx ransomware operations". Correct.
4. Zammad sources[]: the GitHub advisories listing index is gone; the API records, the two critical GHSA pages and the Horizon3 post remain. Correct.
5. Older SonicWall second paragraph: BleepingComputer 2026-10-07 ("In July, two SMA1000 zero-days (CVE-2026-15409 and CVE-2026-15410) were exploited for weeks ... in attacks that ... CISA linked to ransomware gangs") is cited and now in sources[]; UTA0533 and the store self-reference are gone. Correct.
6. FortiBleed record summary: ends at the PBKDF2 sentence and matches the section. Correct.
7. Atlassian: record summary now says the Cyber Centre bulletin "cites open-source reporting of in-the-wild exploitation" (bulletin: "Open source reporting indicates that CVE-2026-21589 is being exploited in the wild"); body paragraph 1 says "exploitation attempts have been recorded on honeypot sensors since 2026-10-06 ([Previdian])" (page: "first observing exploitation attempts ... in our honeypot sensors", first observed 06 Oct 2026). Correct.
8. Older SonicWall actions[0]: now points to "the later hotfix that SonicWall's advisory SNWLID-2026-0017 names" without the build numbers; the facts are supported. Raised again at low confidence for the sequencing and the substantive overlap (F18).

### Citation does not support the claim
- F3 (low confidence) Zammad Update 2026-10-08: "Zammad's advisory of 2026-10-05 says the flaw is exploitable only on 6.5 and earlier" follows a sentence about CVE-2026-102490; the advisory states the 6.5 scope for CVE-2026-102489 only.
- F3 (low confidence) Ixa Detection line: "usernames, passwords and camera locations" cited to the Le Temps lead, which carries "mots de passe" but not usernames (ICTjournal's wording).

### Unsupported / hallucinated facts
- F4 (low confidence) Older SonicWall Triage: "a legitimate Work Place session has no reason to originate internal service-to-service traffic" is stated by no source and sits against the entry's own description of an application-proxy gateway and The Hacker News's description of Work Place as the portal users log in to.

### Analytical-link-as-fact
- F13 (low confidence) Atlassian summary and record summary: "SANS ISC saw the same probes". SANS lists 13 DigitalOcean addresses and one believed actor; Previdian reports 24 addresses in eight countries; the three addresses BleepingComputer names are not in the SANS list.

### Quantifier without source
- F14 (low confidence) FortiBleed Update 2026-06-23: "the first complete tool-chain picture"; BleepingComputer 2026-06-22 says the report "expands on the company's previous research" and calls the tool "alleged".

### Action-item discipline
- F18 (low confidence) Older SonicWall actions[0]: later-hotfix install duplicated in substance by the new entry's action; "then" sequencing after the superseded hotfix is not supported (The Hacker News: "An appliance still on those versions needs the new hotfix").

### Editorial / less-is-more flags (advisory)
- F11 (low confidence) Older SonicWall body and actions[1]: "SonicWall's guidance treats successful exploitation as credential- and MFA-seed-compromising" is the entry's inference worded as the vendor's position.
- F11 (low confidence) Run record: `completed: 2026-10-08T05:04:01Z` precedes the older SonicWall improvement record (`at` 05:30:28Z) that the same run wrote; set `completed` and `duration_seconds` to the real end when the verification block is filled.

### Notes that are not findings
- New SonicWall entry: CVE ids, CVSS 3.0 scores, fixed and affected builds, "third time this year", CERT-FR's "several times this year", NCSC-CH status, Shadowserver count all match the sources. The PSIRT SPA renders only the four CVE texts and the no-exploitation line (no models, date or build table in any transport, WebFetch included); models, date and builds come from The Hacker News, CERT-FR and the Cyber Centre, which the entry cites elsewhere. The Cyber Centre bulletin lists 12.4.3-03670 and 12.5.0-03082 themselves as "and prior"; the entry surfaces this. Priority `high` rests on a pre-authentication CVSS 10.0 on an edge gateway whose two sibling flaws were exploited this year and whose September hotfix builds are affected; I read it as defensible.
- Atlassian: Previdian's live page now reads 153 attempts, 24 addresses, eight countries, three sensors; the entry's "at least 129 / at least 22 / eight countries" stays true. The page's own metadata dates it 2026-10-05, the visible "Updated 08 Oct 2026" matches the citation date for the telemetry.
- FortiBleed: SOCRadar's blog carries "Updated: June 29th ... attributed FortiBleed to the Lynx / INC ransomware group" while BleepingComputer (cited) says "In July"; the registry says 2026-07-01 for the report. Consistent enough to leave.
- KEV (read directly, 2026.10.04): CVE-2026-104286 (2026-10-01), CVE-2026-83548 and CVE-2026-83549 (2026-09-02), CVE-2026-102489 and CVE-2026-102490 (2026-10-02) listed; CVE-2026-21589 and CVE-2026-102255 not listed. EPSS 0.01396 and 0.00629 for the Zammad CVEs match FIRST for 2026-10-05.
- No `org_triage` block or `watchlist` tag; every entry carries `classification`; reliability letters agree with sources.json tiers; no IOCs, no vanity metrics, no em dash outside append-only headings and the 2026-06-23 record summary; no pipeline vocabulary in reader-facing text. `updates[]` fields cover every changed line in each diff; `updated_at` mirrors the non-internal `update` records only.
- Run record notes: counts (4 new, 5 updated: 3 update, 2 improvement), the KEV sweep (0 additions since 2026-10-07), the six open backlog rows, the Contradiction line (cash.ch/AWP gives no date, ICTjournal 25 September, Inside IT end of September) and the Le Temps paywall note hold. The HPE ClearPass and AOS-Switch borderline-drop is a documented judgment, not a silent omission.

### Missed angles
None evidenced. The NCSC-CH hub listing and the KEV catalog show nothing newer than the run covered, and standard searches for exploited zero-days of 2026-10-07 and Swiss communal or cantonal incidents of October 2026 returned nothing newer. Coverage looks complete for the critical and high signal.

### Verdict
NEEDS_FIXES (truth: 5, editorial: 1, advisory: 2)

All eight items are low-confidence. The two I would fix first are the Zammad ambiguous referent (a reader can take the 6.5-and-earlier scope for the unpatched root flaw) and the Atlassian "same probes" wording (summary and record summary); the rest are one-clause edits. Every iteration-3 remediation is correct and introduced no new error.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: "entries/2026-10-02/zammad-cve-2026-102489-102490-exploited-divd-breach (Update 2026-10-08T04:57:05Z, second paragraph)"
  item: "(low confidence) 'the flaw is exploitable only on 6.5 and earlier' follows a sentence about CVE-2026-102490"
  url_or_quote: "\"Horizon3 says it believes the privilege escalation is CVE-2026-102490, that it remains unpatched, and that it is withholding those details ([Horizon3, 2026-10-07]). Horizon3's write-up names no Zammad version; Zammad's advisory of 2026-10-05 says the flaw is exploitable only on 6.5 and earlier ([Zammad, 2026-10-05](https://zammad.com/en/advisories/cve-2026-102489-cve-2026-102490))\""
  summary: "Zammad's advisory says 'Exploitation is only possible on Zammad 6.5 and earlier versions' under the CVE-2026-102489 heading only; under CVE-2026-102490 it calls the flaw a local privilege escalation and names no versions, and DIVD scopes that flaw to every version from 1.5.0. In this paragraph 'the flaw' follows the sentence about CVE-2026-102490 and can be read as that flaw. Name CVE-2026-102489 in the second sentence."
- code: F3
  category: claim-not-supported
  section: "entries/2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale (Detection line)"
  item: "(low confidence) 'usernames' cited to the Le Temps lead, which says passwords only"
  url_or_quote: "\"**Detection:** because the data reportedly holds usernames, passwords and camera locations, the telemetry is the authentication log of video-management, alarm and access-control systems ... ([Le Temps, 2026-10-06](https://www.letemps.ch/suisse/vaud/une-cyberattaque-fait-fuiter-des-informations-de-securite-de-prisons-vaudoises-de-banques-et-de-dizaines-de-societes))\""
  summary: "The readable Le Temps lead says 'Emplacement des caméras de surveillance, mots de passe et plans des dispositifs de sécurité'; 'des noms d'utilisateurs ou des mots de passe' is ICTjournal's wording (attributed to Le Temps). Cite ICTjournal alongside Le Temps for the usernames clause, or drop 'usernames'."
- code: F4
  category: hallucinated-fact
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection (body, Triage line)"
  item: "(low confidence) Triage discriminator contradicts the product's described function"
  url_or_quote: "\"**Triage:** requests to the Work Place interface that trigger outbound connections to internal-only services, or AMC command-execution audit entries not tied to an interactive administrator session, are the observable signature the mechanism supports: a legitimate Work Place session has no reason to originate internal service-to-service traffic.\""
  summary: "No cited source says this. The entry's own first paragraph calls SMA1000 an appliance that fronts 'VPN, SSL-VPN and application-proxy access', BleepingComputer 2026-10-07 says it is used 'to provide VPN access to internal apps and corporate networks', and The Hacker News calls Work Place 'the portal that SMA1000 users log in to', so a legitimate Work Place session does make the appliance connect to internal applications. Either narrow the discriminator to what the sources support (connections to the appliance's own management endpoints or to hosts not published through Work Place, or AMC command execution with no administrator session behind it) or drop the Triage line."
- code: F13
  category: analytical-link-as-fact
  section: "entries/2026-10-06/cve-2026-21589-atlassian-data-center-arbitrary-file-access (summary frontmatter; updates[] 2026-10-08T04:56:05Z summary)"
  item: "(low confidence) 'SANS ISC saw the same probes' links SANS's honeypot attempts to Previdian's"
  url_or_quote: "summary: \"Previdian's sensors have recorded at least 129 attempts from at least 22 addresses, SANS ISC saw the same probes, and a Nuclei template exists\"; record: \"SANS ISC saw the same probes against Jira, Confluence and Bitbucket from one cloud provider\""
  summary: "Neither source states the equivalence. SANS (isc.sans.edu/diary/33406) lists 13 source addresses, all DigitalOcean, and 'I believe these scans are all triggered by the same threat actor'; Previdian's page shows 24 addresses in eight countries and BleepingComputer's three named addresses are not in the SANS list. The body section words it correctly ('its own honeypots began receiving attempts ... with the URLs from watchTowr's write-up'). Say 'SANS ISC recorded similar attempts on its own honeypots, all from one cloud provider'."
- code: F14
  category: quantifier-without-source
  section: "entries/2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed (Update 2026-06-23T04:52:50Z, first sentence)"
  item: "(low confidence) 'the first complete tool-chain picture' in a paragraph this run rewrote"
  url_or_quote: "\"New analysis published 2026-06-22 gives the first complete tool-chain picture of the FortiBleed credential-harvesting campaign.\""
  summary: "BleepingComputer 2026-06-22, the only source now cited for the paragraph, says SOCRadar's report 'expands on the company's previous research' and calls the FortigateSniffer use 'alleged'; it says nothing about a first or complete picture, and Beaumont's earlier reporting of cracked configuration hashes is cited in the same section. Drop 'first complete' or say 'a more detailed tool-chain description'."
- code: F18
  category: action-item-discipline
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection (actions[0])"
  item: "(low confidence) the action still carries the later-hotfix install as a second step and sequences it after the superseded hotfix"
  url_or_quote: "\"Apply SonicWall's hotfix 12.4.3-03526 or 12.5.0-02952 to every SMA1000 6210/7210/8200v appliance now, then the later hotfix that SonicWall's advisory SNWLID-2026-0017 names, because the first pair is affected by CVE-2026-102255; ...\""
  summary: "Check 10b(c)/(d): the later-hotfix task is the same one the new CVE-2026-102255 entry carries in its own action ('Install SonicWall's platform hotfix 12.4.3-03670 or 12.5.0-03082 (or higher) ... including appliances already on the 12.4.3-03526 or 12.5.0-02952 hotfix'), and The Hacker News only says 'An appliance still on those versions needs the new hotfix', never that the older hotfix is a prerequisite. Leave this action to this entry's two flaws and the pointer to the new entry in the body, or word it as installing the newest hotfix directly."
- code: F11
  category: editorial-advisory
  section: "entries/2026-09-03/cve-2026-83548-83549-sonicwall-sma1000-ssrf-cmd-injection (body remediation paragraph; actions[1])"
  item: "(low confidence) the entry's inference is worded as SonicWall's own position"
  url_or_quote: "body: \"...reset TOTP tokens, treating successful exploitation as compromising stored credentials and MFA seeds, not just the appliance itself ([BleepingComputer, 2026-09-02]; [The Hacker News, 2026-10-07])\"; actions[1]: \"SonicWall's guidance treats successful exploitation as credential- and MFA-seed-compromising, not just appliance-compromising.\""
  summary: "Both cited pages say SonicWall advised re-imaging, changing user and administrator passwords and resetting TOTP tokens when indicators of compromise are found; neither says SonicWall treats exploitation as compromising stored credentials and MFA seeds. The inference is reasonable but belongs to the entry; say 'which implies' in the body and drop the attribution in actions[1]."
- code: F11
  category: editorial-advisory
  section: "runs/2026-10-08/2026-10-08T0404Z-intel.md (frontmatter completed / duration_seconds)"
  item: "(low confidence) run completed time precedes a changelog record the same run wrote"
  url_or_quote: "completed: '2026-10-08T05:04:01Z'; duration_seconds: 3568 versus the SonicWall improvement record at: \"2026-10-08T05:30:28Z\""
  summary: "The older SonicWall improvement (run_id 2026-10-08T0404Z-intel) is dated 26 minutes after the recorded completion. When the verification block is filled, set completed and duration_seconds to the real end of the run."
```
