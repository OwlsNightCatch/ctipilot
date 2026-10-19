**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:26:42Z · ended_at=2026-10-18T13:53:41Z · duration_seconds=1619

## Retrospective truth pass — batch T2 (2026-10-18T1307Z-audit)

18 entries checked, clean 10, imprecision 5, factual-error 3. Entries with a defect follow; every other entry in the batch is not listed. 382 ledger claims have verdict rows in `truth-T2.claims.yaml` (one, the Citrix community-blog statement in `cve-2026-107406-citrix-netscaler-saml-idp-overflow`, is recorded `unreadable`: the blog returns 403 on every transport, and BleepingComputer and itnews quote its sentence verbatim).

### 2026-10-07/ninja-forms-wpc-bundles-stored-xss-hidden-admin-campaign — imprecision

- **Where:** cves[CVE-2026-94504] / body (imprecision)
  - **Claim:** CVE-2026-94504 ... Ninja Forms up to and including 3.15.3 (cves[] lists only CVE-2026-94504; no second id)
  - **Defect:** The same Ninja Forms flaw is also published under a second id by another CNA (WPScan, CVE-2026-92438, CVSS 8.8 AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H, affected 3.15.3 fixed 3.15.4); the entry names only the Wordfence id, so a scanner or advisory keyed on the sibling id will not match it.
  - **Ground truth:** Patchstack DB: 'This issue has also been published by another CVE Numbering Authority under CVE-2026-92438, which describes the same as this vulnerability (CVE-2026-94504).' CVE record CVE-2026-92438 (WPScan): 'does not escape submitted form field values before outputting them on the submission edit screen ... unauthenticated users'.
  - **Ground truth URL:** https://patchstack.com/database/WordPress/Plugin/ninja-forms/vulnerability/wordpress-ninja-forms-contact-form-builder-with-calculators-quizzes-signatures-ai-form-builder-plugin-3-15-3-stored-cross-site-scripting-vulnerability
  - **Fix:** Add a one-clause qualifier (body or sourcing_note) that the same flaw also carries CVE-2026-92438 (WPScan CNA, CVSS 8.8), or add it to cves[] with a note that it is the same issue.

### 2026-10-07/gentlemen-affiliate-azazel-ci-cd-secrets-mcp-attacks — imprecision

- **Where:** body, Exposure line (imprecision)
  - **Claim:** **Exposure:** self-hosted GitLab where CI/CD variables are unmasked or unprotected or where removed secrets remain in git history
  - **Defect:** (low confidence) The Exposure line, cited to CloudSEK, presents 'self-hosted' GitLab and 'unmasked or unprotected' variables as the exposed condition; CloudSEK states neither about the victims' GitLab instances (it only recommends masking and protecting variables as a mitigation and says 'a single compromised GitLab instance'). The 'removed secrets remain in git history' and multi-tenant-instance clauses are supported.
  - **Ground truth:** CloudSEK: 'A single GitLab instance hosted CI/CD pipelines for two unrelated organisations.' and mitigation 1 'Mask and protect every variable, rotate tokens on a fixed cadence, and audit git history for committed secrets'. No statement that victim instances were self-hosted or that their variables were unmasked.
  - **Ground truth URL:** https://www.cloudsek.com/blog/caught-in-4k-the-gentlemen-files
  - **Fix:** Reword to what the report supports: 'GitLab instances (hosted or self-managed) whose CI/CD variables and git history hold tokens, keys and database credentials, instances that run pipelines for more than one organisation ...' or mark the unmasked/unprotected condition as the report's mitigation rather than an observed state.

### 2026-10-08/cve-2026-102255-sonicwall-sma1000-workplace-ssrf — factual-error

- **Where:** section Update 2026-10-10T03:44:08Z, Previdian count sentence (factual-error)
  - **Claim:** Previdian's page counts 135 attempts from two source addresses between 2026-10-09 and 2026-10-10 ([Previdian, 2026-10-12](https://previdian.com/CVE-2026-102255))
  - **Defect:** The cited Previdian page does not carry a 2026-10-09..10 window and, read today, shows a much larger and wider count (1,887 attempts, 5 unique IPs, SG and US, 09 to 16 Oct); the 135-attempt/two-US-IP figure is The Hacker News's 2026-10-12 'to date' relay, not a count for 09-10 Oct. The section is timestamped 2026-10-10 yet cites a 2026-10-12 page.
  - **Ground truth:** Previdian page (read 2026-10-18): '1,887 Attempts observed', '5 Unique attacker IPs', 'SG · US', 'First observed 09 Oct 2026 · Last observed 16 Oct 2026'. THN 2026-10-12: 'a total of 135 attempts have been observed to date from two unique IP addresses located in the U.S.'
  - **Ground truth URL:** https://previdian.com/CVE-2026-102255
  - **Fix:** Attribute the 135/two-IP figure to The Hacker News 2026-10-12 ('to date'), drop the 'between 2026-10-09 and 2026-10-10' window, and note the Previdian page now shows 1,887 attempts from five addresses (as of 2026-10-18).

### 2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale — imprecision

- **Where:** summary (frontmatter) (imprecision)
  - **Claim:** The loot reportedly includes camera locations, security-installation plans and, in some cases, usernames or passwords, for clients including police authorities, gendarmerie premises, prisons, hospitals, schools and banks
  - **Defect:** (low confidence) The summary turns AWP's description of Ixa Systems' customer base (police authorities, banks, hospitals, schools, prisons) into a list of clients whose data is in the loot; the readable reports name as affected only judicial entities (Établissements de la plaine de l'Orbe), gendarmerie premises, several banks including the BCV and several dozen companies. The body paragraph keeps the two apart; the summary does not. (Le Temps' full text is paywalled and was not readable beyond its standfirst.)
  - **Ground truth:** AWP/cash.ch: 'Zu ihren Kunden gehören unter anderem Polizeibehörden, Banken, Spitäler, Schulen und Gefängnisse.' ICTjournal: 'Parmi les organisations concernées figurent les Etablissements de la plaine de l'Orbe et d'autres entités judiciaires, des locaux de la gendarmerie, plusieurs banques, dont la Banque cantonale vaudoise (BCV), ainsi que plusieurs dizaines d'entreprises.'
  - **Ground truth URL:** https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois
  - **Fix:** Reword the summary: the firm's customers include police authorities, banks, hospitals, schools and prisons (AWP), while the reported affected organisations are judicial entities, gendarmerie premises, several banks and several dozen companies (ICTjournal).

### 2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow — imprecision

- **Where:** section Update 2026-10-10T03:48:33Z, Inside IT sentence (imprecision)
  - **Claim:** Inside IT, working from the AWP agency, lists the BLVK, the BPK, Migros-Pensionskasse, Pensionskasse Post and Syngenta Pensionskasse as customers of the manufacturer "among others" and says each is checking with PK Softech for a possible data outflow
  - **Defect:** Inside IT says only some of the funds have so far communicated that they are checking with PK Softech; the entry turns that into 'each' of the five listed funds.
  - **Ground truth:** Inside IT: 'Die Kassen sind nach Bekanntwerden des Vorfalls teilweise schon in die Offensive gegangen und kommunizieren, dass sie zusammen mit PK Softech allfällige Datenabflüsse prüfen würden.' (the funds have partly gone on the offensive and communicate that they are checking).
  - **Ground truth URL:** https://www.inside-it.ch/weitere-pensionskassen-pruefen-datenabfluesse-20261009
  - **Fix:** Replace 'says each is checking' with 'says that some of them have already announced they are checking with PK Softech for a possible data outflow'.

### 2026-10-10/cve-2026-84411-mikrotik-routeros-web-management-preauth-rce — factual-error

- **Where:** evidence[4] (7.23.8 changelog quote) and Correction section 2026-10-13T03:36:10Z (factual-error)
  - **Claim:** evidence quote "system - improve stability (includes CVE-2026-84411);" attributed to 'MikroTik (RouterOS 7.23.8 changelog)'; and in the Correction section: RouterOS 7.23.8 (2026-10-08) and 6.49.23 (2026-10-07) "each list the line "system - improve stability (includes CVE-2026-84411);""
  - **Defect:** The quoted line is not a contiguous passage of the cited 7.23.8 changelog: that changelog names a second CVE in the same line, so the quote is altered (and the 'each list the line' statement is wrong for 7.23.8). Only the 6.49.23 release text carries the line exactly.
  - **Ground truth:** 7.23.8 CHANGELOG: '*) system - improve stability (includes CVE-2026-84411, CVE-2026-103903);'. 6.49.23 forum post: 'system - improve stability (includes CVE-2026-84411);'.
  - **Ground truth URL:** https://download.mikrotik.com/routeros/7.23.8/CHANGELOG
  - **Fix:** Quote the 7.23.8 line verbatim ('system - improve stability (includes CVE-2026-84411, CVE-2026-103903);') in evidence[] and in the Correction text, or attach the existing quote to the 6.49.23 forum source and say 7.23.8 lists the same CVE alongside CVE-2026-103903.

### 2026-10-10/ahsaycbs-cve-2026-105133-105134-exploited-webshells-xmrig — imprecision

- **Where:** cves[].cvss (CVSS 4.0 figures) (imprecision)
  - **Claim:** cvss: "7.3 (CVSS 3.1, VulDB as CNA; 5.5 on CVSS 4.0)" and "10.0 (CVSS 3.1, VulDB as CNA; 9.3 on CVSS 4.0)"
  - **Defect:** (low confidence) The CVSS 3.1 figures match the VulDB CNA record, but the CVSS 4.0 figures do not: the CNA's own CVE.org record lists baseScore 6.9 (CVE-2026-105133) and 10 (CVE-2026-105134) for the same CVSS 4.0 vectors, while 5.5 and 9.3 are the values NVD and Bitdefender show for those vectors, which carry the E:P exploit-maturity (threat) metric. The entry labels 5.5/9.3 as VulDB's CVSS 4.0 score without saying they are threat-adjusted or that the CVE.org record differs.
  - **Ground truth:** CVE.org record (assigner VulDB): CVE-2026-105133 cvssV4_0 baseScore 6.9, vector CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:L/VA:L/SC:N/SI:N/SA:N/E:P; CVE-2026-105134 cvssV4_0 baseScore 10, vector ...VC:H/VI:H/VA:H/SC:H/SI:H/SA:H/E:P. NVD API (source cna@vuldb.com): 5.5 and 9.3 for the same vectors.
  - **Ground truth URL:** https://cveawg.mitre.org/api/cve/CVE-2026-105133
  - **Fix:** Keep the 3.1 scores as primary and either drop the CVSS 4.0 figures or state them as 'CVSS 4.0 with E:P: 5.5 / 9.3 (NVD), CNA record lists 6.9 / 10.0'.

### 2026-10-10/ghostaction-fake-audit-workflow-git-history-credential-theft — factual-error

- **Where:** body paragraph 2 (Socket update line) and sourcing_note (factual-error)
  - **Claim:** A Socket update line claims more than 500 accounts and tens of thousands of repositories since 7 October without a method, against 346 for the 8 October burst in its own body and 378 live-workflow repositories across all waves ... so the larger figure stays unconfirmed; sourcing_note: 'Socket's update line ... disagrees with the counts elsewhere, so it is not carried as fact.'
  - **Defect:** As the entry stands today its own cited GitGuardian page (update of 2026-10-13) carries the larger scale from GitGuardian's own dataset, so 'stays unconfirmed' / 'disagrees with the counts elsewhere' is no longer true: more than 30,000 repositories, about 1,900 compromised accounts, 3,174 secrets attempted, and GitHub blocking the workflow from running from 2026-10-09. The entry (updates: []) still presents the incident as 345 to 346 repositories from two maintainers.
  - **Ground truth:** GitGuardian (Update, Oct. 13, 2026): 'Between October 8th and 12th ... the threat actor targeted more than 30,000 repositories across 3,000 users and orgs. This resulted from compromising the GitHub accounts of about 1,900 users. It attempted to extract 3,174 secrets from public repositories' CI.' and 'GitHub started preventing the malicious workflow from running starting October 9.'
  - **Ground truth URL:** https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/
  - **Fix:** Add an update record with a section citing GitGuardian's 2026-10-13 counts (30,000+ repositories, ~1,900 accounts, GitHub blocking runs from 2026-10-09), replace 'stays unconfirmed' with GitGuardian's figure attributed to GitGuardian, and revise the sourcing_note.

