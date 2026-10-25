**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-25T13:14:18Z · ended_at=2026-10-25T13:38:11Z · duration_seconds=1433

## Retrospective truth pass, batch TD (audit 2026-10-25T1308Z-audit)

Ledger note: the spawn message names `truth-TD.ledger.yaml`; that file does not exist, the batch-D ledger is `truth-D.ledger.yaml` (339 claims, 9 entries). All 339 claims have a verdict row in `truth-TD.claims.yaml` (324 ok, 13 F3, 2 F14, 0 unreadable). F3 rows are imprecisions, not invented facts.

### 2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally (imprecision)

1. Summary / body ("Those two were the first confirmed victims"): "Laptop maker Framework and form builder Tally were the first to confirm customer data was taken, on 2026-08-03."
   Ground truth: BleepingComputer says only that Framework was notified on 6 August and accessed on 3 August; no cited source says the two were first, and Kilo Code's own post is dated 2026-08-07, n8n's 2026-08-08 (the entry's 2026-08-19 section puts both in the first wave). 2026-08-03 is the intrusion date, not the confirmation date. URL: https://www.bleepingcomputer.com/news/security/framework-tally-disclose-metabase-data-theft-attacks/
   Fix: drop "first" or attribute it to BleepingComputer's 2026-08-07 report; attach 2026-08-03 to the intrusion.
2. Body paragraph 1 and Update 2026-08-12: "The advisory later assigned CVE-2026-72898 ... with a 14 August due date ([CISA, 2026-08-11])".
   Ground truth: CVE.org shows CISA as CNA reserved and published the id on 2026-08-10; the cited CISA alert lists the CVE but carries no due date (KEV catalog: dateAdded 2026-08-11, dueDate 2026-08-14). URL: https://cveawg.mitre.org/api/cve/CVE-2026-72898
   Fix: attribute the CVE to CISA as CNA (2026-08-10); cite the KEV catalog for the due date or drop it.
3. Update 2026-08-19 (VenariX paragraphs): quoted "This brings the number of publicly confirmed downstream organizations tracked by VenariX to nine" and the n8n (136 records, bcrypt), Framework (payment not included) and Kilo Code (billing address, location, prompts) detail, cited as "[VenariX, 2026-08-17]".
   Ground truth: the page is dated 2026-08-10, shows "Updated Aug 24", lists fifteen incidents, and contains none of that text or detail. The facts are true per n8n (https://blog.n8n.io/metabase-security-incident-update/) and Kilo (https://blog.kilo.ai/p/metabase-incident-impacting-kilo), but the cited URL cannot confirm them. URL: https://venarix.com/blog/metabase-security-incident-downstream-impact-across-customer-environments
   Fix: cite the victims' own posts for the detail and mark the "nine" figure as an earlier version of the VenariX page; label the source 2026-08-10.
4. Update 2026-08-19: "Bits of Gold separately disclosed on 2026-08-17". Ground truth: the company's post is dated 2026-08-16 (DataBreaches.net: reported "on Sunday"). URL: https://blog.bitsofgold.co.il/security-update-august-26/. Fix: 2026-08-16.
5. Update 2026-09-27 (Shipup): "compromised through the same CVE-2026-72898 ... unauthorized access ... confirmed between 31 July and 17 August"; "Cyberattaque.org had already separately documented Printemps, Citadium, Aroma-Zone, Micromania and Easypara"; "Carrefour states ... neither its own site, customer accounts nor internal systems were compromised".
   Ground truth: Cyberattaque.org says the Shipup compromise is "liée à" the Metabase campaign and that unauthorised access "avaient été possibles" in the window; it names only Micromania and Easypara (the other three are on French Breaches); "rien dans la communication ... ne laisse penser que le site ... aient été compromis" is the outlet's reading, not a Carrefour statement. URL: https://www.cyberattaque.org/carrefour-des-donnees-clients-exposees-apres-la-cyberattaque-de-son-prestataire/
   Fix: restore the hedges and attribute each statement to the outlet that makes it.
6. (low confidence) Body paragraph 1 "Neither the vendor nor the reporting locates the injection point precisely": the CVE record and VenariX (cited later in the entry) place the SQL injection at the /reset_password endpoint. URL: https://cveawg.mitre.org/api/cve/CVE-2026-72898
7. (low confidence) techniques[] T1552.001 (Credentials In Files): the sources put the stored credentials in the application database; T1552 alone is supported.

### 2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack (imprecision)

1. Update 2026-10-25: Forescout "counts over 20 claimed attacks ... since January 2026, mostly by the pro-Russian groups Z-Pentest Alliance and NoName057(16)". Ground truth: "The most active groups behind these attacks were Z-Pentest Alliance and NoName057(16)". URL: https://www.forescout.com/blog/cold-chain-open-control-exposed-refrigeration-systems-reveal-global-risk/. Fix: "the most active being".

### 2026-10-22/cve-2026-76466-cisco-expressway-cluster-unauth-root-rce (imprecision, low confidence)

1. cves[CVE-2026-20236] cvss "9.0 ... attack complexity high": matches the Snort 3 advisory table, but Cisco's own CVE record for the id carries 7.5 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H); the divergence is not surfaced. URL: https://cveawg.mitre.org/api/cve/CVE-2026-20236. Fix: keep 9.0 as the advisory-group figure and note the CVE record's 7.5.

### 2026-10-23/cve-2026-114625-arista-velocloud-orchestrator-sqli-exploited (imprecision)

1. cves[].status [exploited, patch-available] and tags: CISA added CVE-2026-114625 to KEV on 2026-10-23 (due 2026-10-26); the entry carries no cisa-kev status. URL: https://www.cisa.gov/known-exploited-vulnerabilities-catalog (cisa-kev feed read this pass). Fix: update record adding cisa-kev.

### 2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27 (imprecision, low confidence)

1. Source date / event_date 2026-10-22: the Tech Zone post's publication timestamp is 2026-10-21T22:23+02:00 ("Last updated on: October 22, 2026"). URL: https://community.citrix.com/techzone-blogs/110_security-updates/protecting-netscaler-management-access-from-php-cve-2026-109618-cve-2026-109619-r1640/. Fix: date the post 2026-10-21 (updated 2026-10-22) or accept as a timezone artifact.

### Clean entries

2026-08-20/cve-2026-73570-zimbra-snmp-command-injection-exploited, 2026-10-21/oracle-october-2026-cpu-six-unauthenticated-cvss-10-rows, 2026-10-22/cve-2026-110264-gitlab-org-mode-renderer-unauth-rce, 2026-10-25/ntlm-relay-signing-bypass-reauthentication-ldap-smb: no defect found (all ids, scores, versions, KEV status and counts re-derived from the vendor pages, CVE records, the KEV feed and, for Oracle, a parse of the 1295 matrix rows). Every techniques[] id of the nine entries is active in the pinned ATT&CK v20.0 dataset.

### Carry-forward checks (narrow)

- 2026-08-28/claroty-copeland-xweb-pro-refrigeration-unauth-root-rce, "Claroty documents seventeen of them": supported. The Team82 post (2026-08-09) lists 17 related disclosures at CVSS 8.0, each an authenticated OS command injection, plus CVE-2026-24663 (9.0, unauthenticated), CVE-2026-25085 (8.6) and CVE-2026-21718 (10.0). URL: https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers
- 2026-10-12/cve-2026-85097-bricksforge-pro-forms-upload-php-exploited:
  - 4.0.2 clause and 2026-10-13 label: confirmed. The changelog has a 4.0.2 block dated "13. October 2026" (upload check rejected "roughly one in sixty" normal images; REST endpoints tightened) and a 4.0.1 block dated "8. October 2026". URL: https://bricksforge.io/version-changelog/
  - Previdian quote (factual-error, lead confirmed): "Yes. Previdian tracks this CVE as a known exploited vulnerability." is not contiguous; the page reads "Yes. Exploitation attempts have been reported for this vulnerability. Previdian lists it as a known exploited vulnerability. Also reported by third-party sources." URL: https://previdian.com/CVE-2026-85097. Fix: quote "Previdian lists it as a known exploited vulnerability."
  - (low confidence) the Previdian citation date 2026-10-08 is the CVE publication date; the exploitation listing is dated 2026-10-12 and the PoC entries 2026-10-10 to 2026-10-15.
- 2026-10-19/ics-calendar-invite-phishing-auto-added-outlook-gmail: confirmed. entities/registry.yaml has product:google-calendar ("Google Calendar") and product:microsoft-exchange-online ("Microsoft Exchange Online"), first_seen 2026-10-19, no tombstone; names match affected_products[].
