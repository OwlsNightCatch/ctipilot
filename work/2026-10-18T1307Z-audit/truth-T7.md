**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:24Z · ended_at=2026-10-18T13:50:43Z · duration_seconds=1399

## Retrospective truth pass — batch T7 (run 2026-10-18T1307Z-audit)

Prior-iteration remediations checked: (1) Brevo — the dropped word 'silent' is gone; the clause now reads 'attempt the install of a plugin' and matches BleepingComputer ('attempted to upload a malicious plugin'). (2) JFrog — the universal negative about the anonymous identity is replaced by Wiz's own anomaly wording and matches the Wiz page. Both held.

### 2026-09-10/sap-september-2026-overpass-s4get-preauth-rce — imprecision
1. **imprecision** — where: sources[0..1] dates and body citations '[Onapsis, 2026-09-09]'
   - Claim: "[Onapsis, 2026-09-09](https://onapsis.com/blog/sap-overpass-remediation/)"
   - Defect: Both Onapsis per-vulnerability posts carry datePublished 2026-09-08 (not 09-09); the entry dates them one day late (timezone-scale drift, CERT-EU's own date 2026-09-09 was probably carried over).
   - Ground truth: JSON-LD datePublished 2026-09-08T08:57:42+00:00 (OVERPASS) and 2026-09-08T08:57:01+00:00 (S4GET); both pages later modified 2026-09-21.
   - URL: https://onapsis.com/blog/sap-overpass-remediation/
   - Fix: Date the two Onapsis posts 2026-09-08 in sources[] and in the inline citations.
2. **imprecision** — where: headline
   - Claim: "Two maximum-severity SAP kernel flaws are reachable through the same ports every SAP GUI and RFC client needs"
   - Defect: Only OVERPASS is CVSS 10.0 (maximum); S4GET is 9.8, which the entry's own summary states, so 'two maximum-severity' overstates one of them.
   - Ground truth: SAP CNA CVE record CVE-2026-58240 baseScore 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H); CVE-2026-44756 baseScore 10.
   - URL: https://cveawg.mitre.org/api/cve/CVE-2026-58240
   - Fix: 'Two critical SAP kernel flaws (CVSS 10.0 and 9.8)'.
3. **imprecision** — where: **Exposure:** line
   - Claim: "SAP systems on kernel 9.16, 9.18, 9.19 or 9.20 below the fixed patch levels (PL 100, 32, 17 and 7 respectively)"
   - Defect: States exposure only for S4GET; OVERPASS (CVE-2026-44756, in the same entry and cves[]) also affects older kernels 7.22-8.04, so a reader reading only this line would clear 7.x/8.04 systems wrongly.
   - Ground truth: CERT-EU: CVE-2026-44756 affected KRNL64NUC 7.22/7.22EXT; KRNL64UC 7.22/7.22EXT/7.53/8.04; KERNEL 7.22, 7.53, 7.54, 7.77, 7.89, 7.93, 8.04, 9.16-9.20; WEBDISP 9.16-9.20; CVE-2026-58240 only KERNEL 9.16-9.20.
   - URL: https://cert.europa.eu/publications/security-advisories/2026-011/
   - Fix: Add that OVERPASS also affects kernels 7.22 to 8.04 and WEBDISP 9.16-9.20 (check Note 3747649), and that the 9.16-9.20 patch levels quoted are S4GET's.

### 2026-09-12/jfrog-artifactory-cve-2026-42016-42018-token-chain-takeover — imprecision
1. **imprecision** — where: cves[].cvss (both) and body paragraph 1 / Correction section
   - Claim: "labelling each only "High" without a numeric score"
   - Defect: True of the advisory page, but JFrog (the CNA) publishes CVSS v3.1 base scores in its own CVE records (8.1 and 7.5); the 2026-09-30 correction dropped them as 'MITRE-sourced' and left cvss null, so the vendor-authority scores are absent and the text implies JFrog gives none.
   - Ground truth: CVE-2026-42016 JFrog CNA record: cvssV3_1 baseScore 8.1, CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N; CVE-2026-42018 JFrog CNA record: baseScore 7.5, CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N (assignerShortName JFROG).
   - URL: https://cveawg.mitre.org/api/cve/CVE-2026-42016
   - Fix: Restore cvss 8.1 / 7.5 attributed to JFrog's own CVE record (CNA), and say the advisory page itself shows only the 'High' label.
2. **imprecision** — where: Correction section sentence 'The CVSS 8.1 and 7.5 figures shown earlier are not on that page and are no longer shown.'
   - Claim: "The CVSS 8.1 and 7.5 figures shown earlier are not on that page and are no longer shown."
   - Defect: Reader-facing implication that the figures were unsupported; they are JFrog's own CNA scores (see previous defect). Also a record-keeping narration in a reader-facing section.
   - Ground truth: JFrog CNA CVE records carry baseScore 8.1 (CVE-2026-42016) and 7.5 (CVE-2026-42018).
   - URL: https://cveawg.mitre.org/api/cve/CVE-2026-42018
   - Fix: Restore the scores with the CNA record as source or drop the sentence.
3. **imprecision** — where: sourcing_note
   - Claim: "BSI's WID-SEC-2026-2808 tracks the CVEs and their KEV status without an observation of its own."
   - Defect: (low confidence) The BSI CSAF lists CVE-2026-42018 among its vulnerability records but not CVE-2026-42016; its 2026-09-10 revision note says only 'Exploit aufgenommen CVE-2026-42016, CVE-2026-42018 und CVE-2026-82329' (exploit recorded), it does not mention KEV.
   - Ground truth: revision 3 (2026-09-10T22:00Z): 'Exploit aufgenommen CVE-2026-42016, CVE-2026-42018 und CVE-2026-82329'; vulnerabilities[] = CVE-2026-42018 and other JFrog CVEs, no CVE-2026-42016.
   - URL: https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-2808.json
   - Fix: Say BSI's advisory records an exploit marker for the CVEs as of 2026-09-10 (CVE-2026-42018 is among its entries); drop 'KEV status'.
4. **imprecision** — where: headline
   - Claim: "Two dormant JFrog Artifactory bugs, patched weeks ago, are now confirmed chained into full admin takeover"
   - Defect: (low confidence) 'dormant' sits against the entry's own statement that exploitation began 15 August, three days after CVE-2026-42018's disclosure (19 days after CVE-2026-42016's).
   - Ground truth: Wiz: 'Between August 15 and September 8, 2026, we observed multiple actors chain CVE-2026-42018 and CVE-2026-42016'.
   - URL: https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201
   - Fix: Drop 'dormant' (e.g. 'Two JFrog Artifactory bugs patched weeks ago are confirmed chained into full admin takeover').
5. **imprecision** — where: actions[1] / immediate_action
   - Claim: "followed within minutes by a POST to /access/api/v1/tokens from the same client"
   - Defect: (low confidence) Wiz gives no interval between the two requests; its only timing is 'under five minutes' from the first request to a created admin account in some instances.
   - Ground truth: 'In some instances, actors moved from the first request to a created admin account in under five minutes.'
   - URL: https://www.wiz.io/blog/artifactory-under-attack-in-the-wild-exploitation-of-cve-2026-42016-cve-2026-4201
   - Fix: 'followed shortly afterwards (in some cases an admin account existed within five minutes of the first request)'.

### 2026-09-16/chosen-brick-iran-telegram-c2-dissident-spyware — imprecision
1. **imprecision** — where: ## Correction — 2026-09-30T06:54:18Z, second paragraph (and body paragraph 4 'full disk wipe')
   - Claim: "it says only that at least one sample had data-wiping functionality, without tying that to the payloads the malware downloads"
   - Defect: NCSC's tasking list also names wiping among the functions the malware can be tasked with ('Wipe the computer system'); the correction's 'says only' is wrong, and it contradicts the entry's own body ('file deletion or a full disk wipe'), while the body's 'full disk' is itself stronger than NCSC's 'wipe the computer system'.
   - Ground truth: NCSC: 'Through the Telegram bot, the malware can be tasked with ... Delete files (T1485) ... Wipe the computer system (T1485)' and, separately, 'In at least one sample, there was functionality for data wiping (T1485).'
   - URL: https://www.ncsc.gov.uk/news/iranian-cyber-targeting-of-dissidents-activists-and-journalists
   - Fix: Correction: NCSC lists computer wiping among the bot-taskable functions and separately notes data-wiping functionality in at least one sample; body: 'wipe the computer system' instead of 'full disk wipe'.

### 2026-09-17/cve-2026-76460-cisco-ise-auth-bypass-root-rce — imprecision
1. **imprecision** — where: summary and body paragraph 2 (CVE-2026-76423)
   - Claim: "affecting every release regardless of configuration"
   - Defect: (low confidence) Cisco's wording is 'regardless of device configuration', not 'every release'; the fixed releases (3.1 P12 ... 3.5 P4) are not affected, so 'every release' overstates.
   - Ground truth: 'This vulnerability affects Cisco ISE and Cisco ISE Passive Identity Connector (ISE-PIC), regardless of device configuration.' Fixed table: first fixed 3.1 Patch 12, 3.2 Patch 11, 3.3 Patch 12, 3.4 Patch 7, 3.5 Patch 4.
   - URL: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
   - Fix: 'affecting ISE and ISE-PIC releases before the fixed patch levels, whatever the configuration'.
2. **imprecision** — where: **Defender takeaway:** paragraph
   - Claim: "using `show logging application ise-kong/access.log | include dummyuser` as a worked example"
   - Defect: (low confidence) Reader-facing text carries a literal log-search indicator string ('dummyuser'); the store's no-IOC policy covers host/log indicator strings. Cisco gives it only as a 'non-exhaustive example'.
   - Ground truth: 'The following is a non-exhaustive example of how a suspicious username could be detected in the logs: admin#show logging application ise-kong/access.log | include dummyuser'
   - URL: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-ISE-ABP-VNSW7Tn5
   - Fix: Keep the command shape ('show logging application ise-kong/access.log') and describe 'a username that is not a real account' without the literal string.
3. **imprecision** — where: updates[] 2026-09-18T05:06:00Z record summary
   - Claim: "CERT-FR confirms only CVE-2026-76460 is reported exploited, and notes ISE 3.1/3.2 will receive no fix at all for eight of the disclosed CVEs"
   - Defect: (low confidence) The record's summary still carries the two statements the 2026-09-30 correction retracts; the 09-18 section no longer says them, so the record no longer matches its section (append-only audit trail, so only a note).
   - Ground truth: CERT-FR: 'Cisco indique que la vulnérabilité CVE-2026-76460 est activement exploitée.' and 'n'ont pas reçu de correctif pour les vulnérabilités ...' (no 'only', no 'will not receive').
   - URL: https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1197/
   - Fix: None required if append-only records are exempt; otherwise add a note that the 2026-09-30 correction supersedes these two statements.

### 2026-09-17/cve-2026-58704-google-pixel-modem-zero-click-eop — imprecision
1. **imprecision** — where: body paragraph 1 (TechCrunch two-wordings sentence), ## Correction section, headline, summary, evidence[], updates[] record summary
   - Claim: "Google did not confirm exploitation to TechCrunch directly: a Google spokesperson did not return TechCrunch's request for comment. TechCrunch words Google's position two ways"
   - Defect: The primary source cited first (Google's Pixel Update Bulletin) itself carries Google's hedged exploitation statement in its Announcements note; the entry attributes the 'may be under limited, targeted exploitation' wording only to TechCrunch's reporting and frames TechCrunch's two wordings as an unresolved inconsistency, when Google's own sentence resolves it (the hedged form is Google's; TechCrunch's 'was exploited' opening overstates).
   - Ground truth: Pixel Update Bulletin, Announcements: 'Note: There are indications that CVE-2026-58704 may be under limited, targeted exploitation.' (read via WebFetch; the jina/extract text of the page omits the note).
   - URL: https://source.android.com/docs/security/bulletin/pixel/2026/2026-09-01
   - Fix: Cite Google's bulletin directly for 'there are indications ... may be under limited, targeted exploitation', state that TechCrunch's opening sentence ('was exploited') is stronger than Google's wording, and drop 'Google did not confirm' / 'CISA's KEV the only unhedged signal' framing.
2. **imprecision** — where: sourcing_note and cves[].cvss
   - Claim: "Google, CISA and TechCrunch publish no numeric CVSS score for this flaw, so none is recorded."
   - Defect: As of 2026-10-07 the CISA ADP container of the CVE record publishes CVSS 3.1 8.8 (AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H); the Google (CNA) record itself has no score and describes the vector as 'remote (proximal/adjacent)', which the body does not convey.
   - Ground truth: CVE record CVE-2026-58704: Google_Devices CNA: 'This could lead to remote (proximal/adjacent) escalation of privilege with no additional execution privileges needed. User interaction is not needed'; adp CISA-ADP cvssV3_1 baseScore 8.8, attackVector ADJACENT_NETWORK.
   - URL: https://cveawg.mitre.org/api/cve/CVE-2026-58704
   - Fix: Say Google's CNA record gives no score and CISA's enrichment rates it 8.8 with an adjacent-network vector (or keep null but drop 'CISA publishes no numeric score'); add the proximal/adjacent qualifier to the exposure description.

### 2026-09-17/kairos-libercourt-commune-ransomware-confirmed — factual-error
1. **factual-error** — where: **Defender takeaway:** paragraph, second sentence
   - Claim: "Kairos has now listed three small municipal administrations in France and Spain, the same victim class as Swiss communes"
   - Defect: Uncited quantifier that undercounts: Kairos's leak-site record on ransomware.live also lists the French Commune de Camiers (discovered 2026-05-29, before Libercourt), so Valdemoro, Velilla de San Antonio, Libercourt and Camiers make four municipal administrations in France and Spain; 'small' is unsupported (ransomware.live calls Valdemoro 'a town in the Madrid region'). Cited sources (Escudo Digital: Valdemoro, Velilla; ransomware.live: Libercourt) only name three.
   - Ground truth: ransomware.live API groupvictims/kairos: 'Commune De Camiers' (FR, Government & Defense, discovered 2026-05-29); 'Ville de Libercourt' (discovered 2026-09-02); 'Ayuntamiento de Velilla de San Antonio' (2026-08-20); 'Ayuntamiento de Valdemoro' (2026-05-11).
   - URL: https://api.ransomware.live/v2/groupvictims/kairos
   - Fix: 'Kairos has listed several municipal administrations in France and Spain this year (Valdemoro, Camiers, Velilla de San Antonio, Libercourt)' with a citation to the ransomware.live Kairos group page, or drop the count.

### 2026-09-17/ddrop-dram-interposer-defeats-confidential-computing — imprecision
1. **imprecision** — where: sources[2] date and body citation '[AMD Product Security, 2026-09-15]' (also Correction section)
   - Claim: "[AMD Product Security, 2026-09-15](https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3048.html)"
   - Defect: (low confidence) AMD-SB-3048's own revision table dates the initial version 2026-09-14; 2026-09-15 is only the page's og:updated_time. One day of drift.
   - Ground truth: Revisions table: '2026-09-14 | Initial version'; og:updated_time 2026-09-15T11:08:20-0500. DDRop site: 'Following a coordinated disclosure on September 14, 2026, both vendors have issued a public security advisory'.
   - URL: https://www.amd.com/en/resources/product-security/bulletin/amd-sb-3048.html
   - Fix: Date the AMD bulletin 2026-09-14 in sources[] and the inline citations.

### 2026-09-17/mandiant-ai-risk-resilience-report-2026 — factual-error
1. **factual-error** — where: summary (case study 7 clause) and body 'Case study 7' paragraph
   - Claim: "a customer-service RAG agent that leaked cross-tenant PII via indirect prompt injection in forum comments"
   - Defect: Mandiant describes Case 7 as an evaluation of a technology organization's agent that did not consider indirect prompt injection, with conditional outcomes ('could', 'could potentially'); it reports no attacker, no planted forum post and no actual PII leak. The entry presents a hypothetical as an observed attack ('an attacker embedded hidden instructions inside a public forum post ... hijacking its reasoning to exfiltrate other customers' PII').
   - Ground truth: 'Mandiant evaluated a technology organization that deployed a public-facing AI customer service agent ... While the customer had strong controls around the vector database, they did not consider indirect prompt injection, which can stem from embedding hidden, malicious instructions inside a public forum comment ... the model could interpret the embedded instructions as system-level commands. This could potentially hijack the model's reasoning, causing it to exfiltrate sensitive data from other customers' support tickets'
   - URL: https://cloud.google.com/security/resources/ai-risk-and-resilience-2026
   - Fix: Rewrite as an assessed exposure: Mandiant evaluated a public-facing RAG customer-service agent and found it exposed to indirect prompt injection via forum comments and support tickets, which could let injected instructions pull other customers' PII into responses; no exploitation is reported. Drop 'leaked' from the summary.
2. **factual-error** — where: body 'Case study 1' first sentence (also headline and summary)
   - Claim: "An attacker compromised a SaaS provider by poisoning an external software package that a developer's active AI coding-assistant session then recommended installing"
   - Defect: Mandiant says the actor compromised a SaaS provider AND hijacked an active AI coding assistant session on a developer's workstation; the assistant then recommended the poisoned package. The report does not state the SaaS provider was compromised by the package, and omits nothing about 'reviving' Shai-Hulud; the headline's 'a poisoned dependency revived the Shai-Hulud worm' and the summary's 'assistant recommending a poisoned dependency that deployed the worm' compress a chain in which the attacker used the hijacked session to install an infostealer, harvest OAuth tokens and then deploy the worm. 'Re-poisoned the organization's own package namespace' is also wrong: the report says the actor 'poisoned a package inside the organization's official namespace' (first poisoning there).
   - Ground truth: 'a threat actor compromised a software-as-a-service (SaaS) provider and hijacked an active AI coding assistant session on a developer's workstation ... recommended the installation of an external software package that had been poisoned by the attacker ... the attacker used the developer's active session to install an infostealer using a poisoned PyPI package, harvest GitHub OAuth tokens, and deploy the self-propagating Shai-Hulud worm ... The actor then poisoned a package inside the organization's official namespace'
   - URL: https://cloud.google.com/security/resources/ai-risk-and-resilience-2026
   - Fix: 'A threat actor compromised a SaaS provider and hijacked a developer's active AI coding-assistant session; the assistant recommended a package the attacker had poisoned, and the attacker then used the session to install an infostealer, harvest GitHub OAuth tokens and deploy the Shai-Hulud worm'; drop 're-' and 'revived'.
3. **imprecision** — where: title and summary lead
   - Claim: "eight frontline case studies of AI agents weaponized inside real intrusions and red-team engagements"
   - Defect: Not all eight are weaponized-agent intrusions: Case 6 is a runaway loop with no attacker (the entry itself says so), Case 7 is an assessed exposure, Case 8 is a defender-side agentic-triage success; 'AI-agent abuse' and 'weaponized' overstate three of eight.
   - Ground truth: Case 6: 'rogue reasoning loop' (no attacker); Case 7: 'Mandiant evaluated ... could potentially'; Case 8: 'Disrupting a stealthy espionage campaign' (defense team's agentic AI triage pipeline).
   - URL: https://cloud.google.com/security/resources/ai-risk-and-resilience-2026
   - Fix: 'eight case studies of AI agents in attacks, red-team tests and operations'.
4. **imprecision** — where: body 'Case study 6' paragraph
   - Claim: "locking the production ledger database"
   - Defect: (low confidence) Mandiant says only 'severe local database locking that halted active business transactions'; 'production ledger database' is an embellishment (the agent had access to 'internal billing databases').
   - Ground truth: 'causing severe local database locking that halted active business transactions.'
   - URL: https://cloud.google.com/security/resources/ai-risk-and-resilience-2026
   - Fix: 'causing severe database locking that halted active business transactions'.
5. **imprecision** — where: body paragraph 1
   - Claim: "The 2026 edition, published 2026-09-15"
   - Defect: (low confidence) The report page states only 'September 2026'; no 2026-09-15 publication date appears on it (Help Net Security's coverage is dated 2026-09-16); sources[0].date and event_date repeat the unverified day.
   - Ground truth: Page header: 'AI risk and resilience / A Mandiant special report 2026 / September 2026'.
   - URL: https://cloud.google.com/security/resources/ai-risk-and-resilience-2026
   - Fix: 'published in September 2026' (or confirm the day from Google Cloud's own listing).
6. **imprecision** — where: body, Case study 3, 4, 5 and 7 paragraphs (and the Hardening/Hunt lines of cases 1, 2, 6 beyond the cited sentence)
   - Claim: "Case study 3 ... Case study 4 ... Case study 5 ... Case study 7 paragraphs carry no inline citation"
   - Defect: Four of the eight case-study paragraphs have no inline citation at all; all facts are in the one Mandiant report, but the entry's own convention (inline-cited clause) is not met there.
   - Ground truth: All four are found in the cited report (Case studies 3, 4, 5, 7).
   - URL: https://cloud.google.com/security/resources/ai-risk-and-resilience-2026
   - Fix: Add '([Mandiant, 2026-09-15](...))' at the end of each case-study paragraph.

### 2026-09-18/cve-2026-91843-check-point-security-mgmt-stack-overflow — imprecision
1. **imprecision** — where: cves[CVE-2026-91843].fixed, body paragraph 2 (Jumbo Hotfix sentence), actions[0], Defender takeaway, Correction section
   - Claim: "The fix is also in the Jumbo Hotfix Accumulator for R82.10 from Take 45, R82 from Take 127, R81.20 from Take 170 and the end-of-support R81.10 from Take 192"
   - Defect: Omits the R82.20 Jumbo Hotfix route that Check Point lists. For R82.20 the entry therefore offers only the LivePatch, which does not fix the exploited sibling CVE-2026-93616; actions[0] ('preferably as a Jumbo Hotfix take that also fixes the exploited CVE-2026-93616 (R82.10 Take 45, R82 Take 127, R81.20 Take 170, R81.10 Take 192), otherwise as the LivePatch') leaves R82.20 admins on a LivePatch-only path.
   - Ground truth: sk1000155: 'The fix is also included in: Jumbo Hotfix Accumulator for R82.20 starting from Take 10 ...'; sk1000171: 'Download the R82.20 Security Hotfix ... Jumbo Hotfix Accumulator for R82.20 starting from Take 10 ... These Jumbo Hotfix Accumulators also include the fix for CVE-2026-91843' and 'Check Point LivePatch Take 28/29 does not address this issue.'
   - URL: https://support.checkpoint.com/results/sk/sk1000171/
   - Fix: Add R82.20 Jumbo Hotfix Take 10 (and the R82.20 Security Hotfix for CVE-2026-93616) to fixed, body, the correction and the action.

### 2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev — factual-error
1. **factual-error** — where: cves[CVE-2026-87886].affected / fixed, affected_products[], summary, body paragraph 1, actions[0], Defender takeaway
   - Claim: "Acronis Backup plugin for cPanel & WHM before build 1.9.3.1021; extension for Plesk before build 1.8.11.638 (both Linux)"
   - Defect: Omits a third affected product named by the vendor and its CNA CVE record: the Acronis Backup plugin for DirectAdmin (Linux), fixed in build 1.2.3.238. The entry (and its action) tells only cPanel & WHM and Plesk operators to patch; a DirectAdmin server running the plugin would not be told. The press articles the entry relies on list only two products; the vendor advisory lists three.
   - Ground truth: Acronis advisory SEC-10986 (API): products: 'Acronis Backup plugin for cPanel & WHM' patched 1.9.3.1021; 'Acronis Backup extension for Plesk' patched 1.8.11.638; 'Acronis Backup plugin for DirectAdmin' patched 1.2.3.238; CVE record description: 'Acronis Backup plugin for DirectAdmin (Linux) before build 1.2.3.238'.
   - URL: https://security-advisory.acronis.com/api/v1/advisories/SEC-10986
   - Fix: Add 'Acronis Backup plugin for DirectAdmin (Linux) before build 1.2.3.238' to cves[].affected/fixed, affected_products, the body, summary and actions[0]; note the exploitation statement names only cPanel & WHM, and that KEV's description lists cPanel & WHM and Plesk.
2. **imprecision** — where: sourcing_note
   - Claim: "Acronis's own advisory page (security-advisory.acronis.com/advisories/SEC-10986) is a client-side-rendered application returning no readable content on any transport tried"
   - Defect: (low confidence) The advisory is readable through the site's own JSON endpoint (/api/v1/advisories/SEC-10986) and Acronis's CNA CVE record carries its text and CVSS; the vendor primary can be cited instead of Help Net Security as primary, and it names the DirectAdmin product the press omits.
   - Ground truth: GET https://security-advisory.acronis.com/api/v1/advisories/SEC-10986 returns id, cve, cwes, severity (7.8, CVSS:3.0/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H), three products with patched builds, published 2026-09-17T13:30:00Z.
   - URL: https://security-advisory.acronis.com/api/v1/advisories/SEC-10986
   - Fix: Cite the Acronis advisory/CNA record as primary or soften 'no readable content on any transport tried'.

### 2026-09-18/brevo-cloudflare-worker-clickfix-supply-chain — imprecision
1. **imprecision** — where: **Exposure:** line (and body paragraph 1 window sentence)
   - Claim: "anyone who followed the fake verification prompt on 2026-09-14, within Brevo's stated impact window of 15:01 to 20:30 UTC, and ran the pasted command is exposed"
   - Defect: (low confidence) 15:01-20:30 is the Worker's impact window; Brevo's own 'Affected surfaces and window' says the ClickFix was active on the listed URLs 'from 16:07 UTC until 20:30', BleepingComputer gives the exposure window as 16:07-20:30 and Sansec observed malware 16:05-20:13. The entry applies the longer window to the prompt without noting the two stated starts.
   - Ground truth: Brevo write-up: 'Impact window: 15:01 to 20:30 UTC, 5h29' and 'The ClickFix was active on following URLs from 16:07 UTC until 20:30.' BleepingComputer: 'defining the exposure window as between 16:07 and 20:30 UTC'. Sansec: 'Brevo served the malware between 16:05:18 and 20:12:53 UTC on 14 September.'
   - URL: https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up
   - Fix: State the ClickFix window as 16:07 to 20:30 UTC per Brevo (Sansec observed 16:05 to 20:13) and the Worker's wider 15:01 to 20:30 impact window separately.
2. **imprecision** — where: actions[0], body paragraph 1 and Triage line
   - Claim: "a plugin impersonating "Web Media Optimizer" ... BleepingComputer names the known backdoor plugin "Web Media Optimizer""
   - Defect: (low confidence) The malicious plugin's display name is a named host/file-name-style indicator in reader-facing text, which the store's no-IOC policy excludes; the behavioural checks (plugin on disk not in the admin list, plugin installed 14 September, upload-plugin POST) carry the detection without it.
   - Ground truth: BleepingComputer: 'it pretends to be a WordPress plugin named "Web Media Optimizer" but acts as a persistent backdoor and JavaScript loader.'
   - URL: https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/
   - Fix: Drop the plugin name from actions[0], Triage and the correction section; keep 'a plugin that hides itself from the admin plugin list'.

Entries with no defect (whole entry read, every ledger claim checked): 2026-09-17/aepd-first-ai-agent-breach-notification, 2026-09-18/ntc-swiss-solar-inverter-cybersecurity-assessment, 2026-09-18/gyazo-helpfeel-data-breach-image-upload-rce
