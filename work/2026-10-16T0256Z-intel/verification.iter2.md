**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-16T05:08:31Z · ended_at=2026-10-16T05:39:41Z · duration_seconds=1870

## Verification report — 2026-10-16T0256Z-intel (iteration 2)

Scope: all 252 claims of the ledger `claims.iter2.yaml` carry a verdict row in `verification.iter2.claims.yaml` (the 57 changed claims, every other claim of the ten remediated entries, and every claim of the three untouched entries, not a quarter). Pages were fetched this iteration (extract, raw url, WebFetch with the outbound-links template for drupal.org and cisa.gov, the repo PDF decoder for the BLVK notice). Two rows are `unreadable`: the MSRC page of CVE-2026-70279 did not render on extract, jina or WebFetch (the CVE record confirmed XSS spoofing and CVSS 9.3; the "Exploitation More Likely" rating is unconfirmed); not a finding.

### Walk of the iteration-1 deltas (29 findings)

All 27 applied fixes were checked against the cited source. Every fix holds; the residual or new defects they leave are in the findings below.

- BeyondTrust: the Exposure line now cites the advisory for `/appliance` and 24.3.1 and GTIG for "does not undo earlier exposure" (advisory text: 'Customers on a Remote Support version older than 24.3.1 will need to upgrade'; GTIG: 'Upgrading closes the vulnerability but does not remediate prior exposure'); "third-party detection platform" matches the blog; "suspected" matches both GTIG ('a suspected PRC-nexus espionage threat actor') and BeyondTrust ('A suspected China-nexus espionage actor'). Residuals: F3 (low) and F4 (low), F3 sourcing_note.
- AdFection: DLL sentence, removal of the "uncategorized" and mail-filter claims, and the DoH raw-IP clause all verified against Citizen Lab and Confiant ('so it never appears as a plaintext DNS query or as a connection hostname, keeping it invisible to DNS-based monitoring and blocklists').
- PEERSTITCH: the split Exposure line (FG-IR-26-122 for FortiOS versions; Unit 42 for 'FMG-Access (TCP port 541)'), the Table 2 hunting items (anonymous 16,384-byte rwxp regions, three NOP offsets, cross-PID /proc/mem, Signal 11 in crashlog, ../ auto-script objects) and the restored "persistent" all verified.
- Ivanti: 'Connect Secure (ICS) version 22.8Rx antérieures 22.8R2.5' matches "22.8Rx builds before 22.8R2.5". The same CERT-FR page, however, produces the 25.1.3.0 conflict and exposes two over-generalisations (findings below).
- Atlassian: Previdian page now reads 607 / 65 / 20 / 5 sensors / 'Updated 16 Oct 2026' / 'In CISA KEV'; the "only public detail" claim is gone. Residual: citation-date label and a universal negative.
- Drupal: Exposure wording ("a contributed module or custom code that exposes the vulnerable functionality, which the advisory does not name"), the end-of-life range (advisory range `>= 8.9.0 < 10.6.19 || >= 11.0.0 < 11.3.19 || >= 11.4.0 < 11.4.10 || >= 12.0.0-alpha1 < 12.0.0-beta2`) and the one-sentence sourcing note verified.
- AhsayCBS: "August" is gone from the entry (Ahsay: 'our previous patches v9.15.2.59 and v10.3.4.0'); the CNA scores (7.3/5.5 and 10.0/9.3, VulDB) match Bitdefender's table; the OpenSSH point is in the update and action. It survives in the run-record notes (finding F4, low).
- CL-UNK-1211: the uncited endpoint-rule sentence and vendor-product sentences are gone; the new technique ids (T1098.004, T1021.004, T1090, T1041, T1567) are active in the pinned ATT&CK v19.2 and each is stated in Unit 42. The expansion introduced new defects (below).
- IDC Frontier: the cut is in place and routine-sized; it introduced the scope defects below.
- PK Softech: "first" and "concrete" removed; SwissCybersecurity.net's "scheinen also noch keinen Fall registriert zu haben" is carried as 'reads its conditional wording as meaning no case ... had been registered yet'.

### Judgement of the two declined findings

- **Beyond Gravity missed angle (F10): rebuttal kept, no finding.** The gate argument is real: CLAUDE.md and check_run require a non-empty `techniques[]` on an incident entry, and the held row's own facts (no vector, no behaviour, no data class; SRF's China assumption is single-outlet, anonymous-source and denied by the company as confirmed) leave nothing evidence-bound to map. Under the incident floor the item is `routine` and two sentences at most, so it sits below the critical/high completeness bar. I could not fetch the SRF item (a search returned no SRF piece for this case), so I neither confirm nor refute the SRF facts; the held row expiring on 2026-10-20 is a reasonable control.
- **Drupal priority (F16): rebuttal kept, no finding.** Evidence for `high`: the advisory rates it Critical 19/25 with 'At least one known exploit path does not require authentication' (read via WebFetch; SA-CONTRIB-2026-218 confirms the same for Entity List, 90 reporting sites per The Hacker News), Drupal Steward 'already blocks some known attack vectors' (so attack vectors are known to the Security Team), and core flaw mechanics are readable from the public fix. Against: the pre-announcement quote is Drupal's standing wording for core criticals and the contributed-module condition resembles the "non-default configuration" disqualifier. On balance the decision (update Drupal core and Entity List inside the week) is a real out-of-cycle task for a public-sector Drupal estate, so `high` stands; a reader could equally defend `notable`.

### Citation does not support the claim (F3)

- #1 `2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups`, first body sentence: "stopped four zones of IDCF Cloud East Japan Region 1, affecting 495 companies and local governments" cited to https://www.idcf.jp/news/topics/20261007002. The second report carries ransomware, Region 1 and 495 ('IDCFクラウドを契約している495の企業や自治体') but no zone names and no server stoppage; the zones (tesla/henry/pascal/joule) and 'クラウドサービス上の仮想サーバーの再起動不可' are in the third report https://www.idcf.jp/news/topics/20261008001. Cite the third report there.
- #2 same entry, takeaway: "IDC Frontier first expected restoration only from copies customers hold themselves" cited to the fifth report. (low confidence) The fifth report says it had expected retrieval and restoration to be 'difficult'; 'only from backup data customers hold themselves' is the third report's wording.
- #3 `2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day`, Exposure: "the /appliance interface shows whether it is installed or automatic updates are on" cited to the advisory. (low confidence) The advisory carries 'not subscribed to automatic updates in their /appliance interface' and the 24.3.1 boundary; 'shows whether [the patch] is installed' is GTIG ('If the patch is not visible in /appliance').
- #4 same entry, sourcing_note: "BeyondTrust reports its own hosted instance and a self-hosted appliance from its telemetry". (low confidence) The blog: its hunt 'surfaced the affected SaaS instance'; 'Mandiant shared its findings from the self-hosted customer, which confirmed what we had found'. The appliance is Mandiant's observation.
- #5 `2026-10-06/cve-2026-21589-...`, update 2026-10-16T04:11:30Z: figures verified, but "([Previdian, 2026-10-08](https://previdian.com/CVE-2026-21589))" labels a page the sentence itself calls updated 2026-10-16. (low confidence) Re-date the citation.
- #6 `2026-10-10/ahsaycbs-...`, update: (low confidence) Bitdefender says MDR 'tried to stage payloads as command files (.cmd)' in C:\Users\Public and that 'In MDR's incidents' follow-on scripts were staged on a static-site subdomain; the entry says "staged" and chains the static-site staging onto "in the second".

### Unsupported / hallucinated facts (F4)

- #7 `2026-10-16/cl-unk-1211-...`, mail-server paragraph: "they exfiltrated database dumps over netcat and to public file-hosting platforms, cleaned authentication, history, mail and operating-system logs". Unit 42: 'attempted to exfiltrate them to their C2 infrastructure ... using the netcat command', 'tried to upload the data to legitimate file-hosting platforms', 'This cleanup included attempts to delete logs'. Completed exfiltration is never stated. Restore the hedge.
- #8 same entry (low confidence): "qmail Maildir stores" and `affected_products: ["Plesk","PHP","qmail"]`. Unit 42 names only the path /var/qmail/mailnames/ and Maildir/cur/, not qmail as software.
- #9 `2026-10-14/cve-2026-104935-...`, summary, actions[1], takeaway: "CERT-FR says it knows of lateral movement using the directory and other secrets stored on the appliance" / "using these secrets" / "using the secrets stored on it". CERT-FR: 'réinitialiser les secrets liés au LDAP ou à l'Active Directory ... le CERT-FR a connaissance de latéralisation utilisant ces secrets'. Only the LDAP/AD secrets. The new update section is worded correctly; align the three.
- #10 same entry (low confidence): "re-runs the whole chain over HTTPS". Volexity: 'The result of each command is then returned via the HTTP response'; no HTTPS.
- #11 `2026-10-11/idc-frontier-...`, headline "provider judges no customer data left", summary "found no trace of customer data being queried or taken", record summary. The fifth report (https://www.idcf.jp/news/topics/20261014001) scopes this to data stored in customers' virtual servers in the four zones and, in item 3, confirms unauthorised queries of portal registration data of 48 customers (no trace of removal). The unscoped wording contradicts the report. Scope it and add one clause on the portal lookups (the cut removed the data classes, which is fine; the existence of the lookups matters to the claim).
- #12 same entry (low confidence, supersession): the unchanged analysis sentence "whose recovery depended on copies the customers held" against the newest section (provider snapshot backups retrievable for 194 of 495).
- #13 `2026-10-16/cve-2026-102764-...`, immediate_action: (low confidence) "GTIG expects broad exploitation now that the flaw is public"; GTIG: 'prepare for potential widespread exploitation', 'It is possible that we will observe similar widespread exploitation attempts' (BeyondTrust's blog says Mandiant 'warns defenders to expect the same').
- #14 run record notes: (low confidence) "its admission that the August patches were incomplete" after iteration 1 removed "August" from the entry.

### Quantifier without source (F14)

- #15 `2026-10-06/cve-2026-21589-...`, update section and record summary: (low confidence) "so no public source reports a compromise" as a consequence of the CISA alert's silence; the sourcing_note scopes the claim to the cited honeypot operators. Say 'neither CISA nor the honeypot operators report a compromise'.

### Claims missing inline citation (F5)

- #16 `2026-10-16/cl-unk-1211-...`: "It names no victim, country or initial access vector; the recovered tools include a custom Go scanner for the React Server Components flaw CVE-2025-55182." (low severity) uncited; the page says 'CVE-2025-55182 (React2Shell) vulnerability scanner', not 'React Server Components'.

### Needs more research (F8)

- #17 `2026-10-16/peerstitch-...`, Exposure: "a FortiManager reachable on TCP 541 from untrusted networks, where the intrusion began". (low confidence) Reachability is not exposure to CVE-2024-47575, fixed in October 2024 (https://www.fortiguard.com/psirt/FG-IR-24-423: fixed in 7.6.1, 7.4.5, 7.2.8, 7.0.13, 6.4.15, 6.2.13). Scope the clause to unfixed FortiManager builds.

### Surface contradiction (F9)

- #18 `2026-10-14/cve-2026-104935-...`: CERT-FR lists 'Connect Secure (ICS) version 25.1.3.x antérieures 25.1.3.1' as affected (25.1.3.0 included); Rapid7 lists 'Resolved versions 25.1.3.0, 25.1.3.1' (and says a portion was patched in 25.1.3.0). The entry names 25.1.3.0 as a fixed target in summary, immediate_action, actions[0] and `cves[].fixed`, and the new section reports CERT-FR's list without flagging the conflict; the sourcing_note covers only 25.2.2 versus 25.1.2.2. Add a Contradiction line and point the action at 25.1.3.1.
- #19 `2026-10-11/idc-frontier-...` (low confidence): the cited BleepingComputer article carries the actor's console message claiming 'wiped 554,153 snapshots', against IDC Frontier's snapshot-backup statement; mention the unverified claim or surface the contradiction.

### Editorial / less-is-more flags (advisory, F11)

- #20 BeyondTrust `references[]` lacks `2026-06-05/verdantbamboo-unc5221-warp-panda-an-18-month-china-nexus-int`, the existing profile of the same actor.
- #21 Drupal: the per-CVE authority for CVE-2026-108099 (https://www.drupal.org/sa-contrib-2026-218: Critical 19/25, affected '<3.0.10', known unauthenticated path) is not in `sources[]`.
- #22 AdFection Detection: "the SDK" has no antecedent.
- #23 BeyondTrust: immediate_action and actions[1] say redeploy every internet-reachable appliance; the takeaway says confirmed-or-unknown status. State one rule.

### Checks with no finding

Style (no em dash in reader-facing text, no IOC, no pipeline vocabulary), classification letters against `sources/sources.json` tiers, priorities (BeyondTrust `critical` clears the act-now bar: zero-day since late August by a suspected state actor, unauthenticated, persistence survives reset, GTIG warning of broad exploitation after disclosure; Ahsay `high`, PAN-OS `high`, Atlassian `high` consistent with KEV and exploitation), single-source flags, update-vs-new decisions (all eight changelog records are the same finding with a genuine delta; no silent edit seen in the diffs; `updated_at` mirrors correct), entity keys (ARMORY CASTLE / UNC5221 / WARP PANDA all alias `actor:verdantbamboo`), ATT&CK ids active in the pin. Coverage: the Register security feed for 2026-10-11 to 2026-10-15 and the KEV window show no relevant in-window item missing (the Cisco KEV addition CVE-2026-76519 is already an entry); coverage looks complete for the critical/high signal.

### Verdict

NEEDS_FIXES (truth: 15, editorial: 4, advisory: 4)

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) - iteration 2, run 2026-10-16T0256Z-intel
- code: F4
  category: hallucinated-fact
  section: 2026-10-16/cl-unk-1211-ai-assisted-intrusions-government-linux-hosts
  item: "CL-UNK-1211 body, mail-server paragraph"
  url_or_quote: "they exfiltrated database dumps over netcat and to public file-hosting platforms, cleaned authentication, history, mail and operating-system logs"
  summary: "Unit 42 (https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/) writes 'attempted to exfiltrate them to their C2 infrastructure', 'using the netcat command ... tried to upload the data to legitimate file-hosting platforms' and 'cleanup included attempts to delete logs'; the report never states completed exfiltration. The entry upgrades attempts to completed actions. Restore 'attempted' / 'tried to' for exfiltration and log cleanup."
- code: F4
  category: hallucinated-fact
  section: 2026-10-16/cl-unk-1211-ai-assisted-intrusions-government-linux-hosts
  item: "CL-UNK-1211 Exposure line, summary and affected_products[]"
  url_or_quote: "Plesk-managed PHP stacks and qmail Maildir stores; affected_products: [\"Plesk\", \"PHP\", \"qmail\"]"
  summary: "(low confidence) Unit 42 names only the directory path /var/qmail/mailnames/ and Maildir/cur/; it never names qmail as the mail software (modern Plesk keeps that legacy directory name while using other MTAs). Calling it 'qmail' and listing qmail as an affected product is an inference from a path string. Say 'Plesk mail directories (/var/qmail/mailnames/)' and drop qmail from affected_products[]."
- code: F5
  category: missing-citation
  section: 2026-10-16/cl-unk-1211-ai-assisted-intrusions-government-linux-hosts
  item: "CL-UNK-1211 first paragraph"
  url_or_quote: "It names no victim, country or initial access vector; the recovered tools include a custom Go scanner for the React Server Components flaw CVE-2025-55182."
  summary: "(low severity) The sentence has no inline citation; the page names 'CVE-2025-55182 (React2Shell) vulnerability scanner' (appendix) and does not say 'React Server Components'. Add the Unit 42 citation to the sentence."
- code: F4
  category: hallucinated-fact
  section: 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev
  item: "summary, actions[1] and Defender takeaway"
  url_or_quote: "CERT-FR says it knows of lateral movement using the directory and other secrets stored on the appliance (summary); because CERT-FR knows of lateral movement using these secrets (actions[1]); because CERT-FR knows of lateral movement using the secrets stored on it (takeaway)"
  summary: "CERT-FR (https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-013/) scopes the statement to the LDAP/AD secrets: 'réinitialiser les secrets liés au LDAP ou à l'Active Directory ... le CERT-FR a connaissance de latéralisation utilisant ces secrets'. The new update section words it correctly ('the LDAP and Active Directory secrets'); summary, actions[1] and takeaway generalise it to all secrets (certificates, API keys, Kerberos tickets, licence authentication). Align them with the update section."
- code: F4
  category: hallucinated-fact
  section: 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev
  item: "body, chain paragraph"
  url_or_quote: "Every command re-runs the whole chain over HTTPS with no web shell or backdoor"
  summary: "(low confidence) Volexity (https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/) says the result 'is then returned via the HTTP response' and found no first-stage malware or web shells; it never says HTTPS. Drop 'over HTTPS' or say over HTTP(S)."
- code: F9
  category: surface-contradiction
  section: 2026-10-14/cve-2026-104935-ivanti-connect-secure-zero-day-chain-kev
  item: "update section 2026-10-16T04:10:00Z, summary, immediate_action, actions[0], cves[].fixed"
  url_or_quote: "Its affected-systems list names ... the 25.1.3.x builds before 25.1.3.1 ... (CERT-FR) vs 'Upgrade ... to 25.1.1.2, 25.1.3.0 or 25.1.3.1, or 22.8R2.5' (entry)"
  summary: "CERT-FR lists 'Connect Secure (ICS) version 25.1.3.x antérieures 25.1.3.1' as affected, i.e. 25.1.3.0 is affected; Rapid7's table (https://www.rapid7.com/blog/post/etr-ivanti-connect-secure-zero-day-exploited-in-the-wild-cve-2026-104935/) gives 'Resolved versions 25.1.3.0, 25.1.3.1' and says a portion was patched in 25.1.3.0. The entry names 25.1.3.0 as a fixed target in four fields and the new section reports CERT-FR's list without flagging the conflict (the sourcing_note covers only the 25.2.2 versus 25.1.2.2 label). Add a Contradiction line and steer the action to 25.1.3.1."
- code: F4
  category: hallucinated-fact
  section: 2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups
  item: "headline, summary and record summary"
  url_or_quote: "provider judges no customer data left; it found no trace of customer data being queried or taken and therefore judges no data left"
  summary: "The fifth report (https://www.idcf.jp/news/topics/20261014001) scopes the 'no trace' finding to data stored in customers' virtual servers in the four zones ('お客さまの仮想サーバー内に保存されていたデータの照会や外部へ持ち出されたことを示す痕跡...は確認されませんでした') and, in item 3, confirms unauthorised queries of portal registration data of 48 customers (no trace of removal). The headline, summary and record drop the scope, so 'no trace of customer data being queried' contradicts the same report. Scope the claim to virtual-server data and add one clause on the confirmed portal lookups."
- code: F3
  category: claim-not-supported
  section: 2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups
  item: "body first sentence"
  url_or_quote: "stopped four zones of IDCF Cloud East Japan Region 1, affecting 495 companies and local governments ([IDC Frontier, 2026-10-07](https://www.idcf.jp/news/topics/20261007002))"
  summary: "The second report carries the ransomware cause, Region 1 and the 495 figure but no zone names and no server stoppage; 'four zones' (tesla/henry/pascal/joule) and 'virtual servers stopped ... cannot be restarted' are in the third report https://www.idcf.jp/news/topics/20261008001. Cite the third report for that clause."
- code: F3
  category: claim-not-supported
  section: 2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups
  item: "Defender takeaway"
  url_or_quote: "IDC Frontier first expected restoration only from copies customers hold themselves ... ([IDC Frontier, 2026-10-14](https://www.idcf.jp/news/topics/20261014001))"
  summary: "(low confidence) The fifth report says it had expected retrieval and restoration to be 'difficult' but not 'only from copies customers hold themselves'; that wording is the third report's (https://www.idcf.jp/news/topics/20261008001). Cite both."
- code: F4
  category: hallucinated-fact
  section: 2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups
  item: "body main analysis versus update section"
  url_or_quote: "local governments sat behind one provider whose recovery depended on copies the customers held"
  summary: "(low confidence, supersession) The newest section reports the provider's own snapshot backups retrievable for 194 of the 495 customers, replacing the third report's 'only from customers' own backups'. The unchanged main-analysis sentence still states the superseded premise as the lesson. Reword to 'first depended ... until the fifth report'."
- code: F9
  category: surface-contradiction
  section: 2026-10-11/idc-frontier-idcf-cloud-ransomware-495-customers-backups
  item: "takeaway about provider-held backups"
  url_or_quote: "its own snapshot backups became retrievable for 194 of the 495 customers"
  summary: "(low confidence) The cited BleepingComputer article (https://www.bleepingcomputer.com/news/security/ransomware-attack-disrupts-japans-idcf-cloud-used-by-govt-clients/) reports the threat actor's console message claiming it 'wiped 554,153 snapshots', against IDC Frontier's statement that snapshot backups are intact for 194 customers. An actor's claim is not a fact, but the takeaway about provider-held backups should say the claim exists and is unverified, or the contradiction line should be added."
- code: F4
  category: hallucinated-fact
  section: 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day
  item: "immediate_action.action"
  url_or_quote: "GTIG expects broad exploitation now that the flaw is public"
  summary: "(low confidence) GTIG (https://cloud.google.com/blog/topics/threat-intelligence/armory-castle-exploits-beyondtrust/): 'Organizations should prepare for potential widespread exploitation' and 'It is possible that we will observe similar widespread exploitation attempts'. BeyondTrust's blog says Mandiant 'warns defenders to expect the same'. The body is correct ('historically exploited broadly'); the immediate action upgrades 'possible' to 'expects'."
- code: F3
  category: claim-not-supported
  section: 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day
  item: "Exposure line"
  url_or_quote: "the /appliance interface shows whether it is installed or automatic updates are on, and a build older than 24.3.1 must be upgraded first ([BeyondTrust, 2026-10-15](https://www.beyondtrust.com/trust-center/security-advisories/bt26-05))"
  summary: "(low confidence) The advisory says self-hosted customers 'should manually apply the patch if their instance is not subscribed to automatic updates in their /appliance interface' and that versions older than 24.3.1 must upgrade; 'shows whether it is installed' is GTIG's wording ('If the patch is not visible in /appliance'). Cite GTIG for that clause."
- code: F3
  category: claim-not-supported
  section: 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day
  item: "sourcing_note"
  url_or_quote: "BeyondTrust reports its own hosted instance and a self-hosted appliance from its telemetry, so the exploitation has two first-hand observers"
  summary: "(low confidence) BeyondTrust's blog (https://www.beyondtrust.com/blog/entry/bt26-05): its own hunt 'surfaced the affected SaaS instance'; 'Mandiant shared its findings from the self-hosted customer, which confirmed what we had found'. The self-hosted appliance is Mandiant's incident-response observation, not BeyondTrust telemetry."
- code: F3
  category: claim-not-supported
  section: 2026-10-06/cve-2026-21589-atlassian-data-center-arbitrary-file-access
  item: "update section 2026-10-16T04:11:30Z, last sentence"
  url_or_quote: "Previdian's page, updated 2026-10-16, now counts 607 attempts ... ([Previdian, 2026-10-08](https://previdian.com/CVE-2026-21589))"
  summary: "(low confidence) Figures verified on the page (607 / 65 / 20 countries / 5 sensors, 'Updated 16 Oct 2026', 'In CISA KEV'), but the citation label and sources[].date still read 2026-10-08, the state cited in the earlier section; the sentence itself says the page was updated 2026-10-16. Re-date the citation (living page) so the label matches the cited content."
- code: F14
  category: quantifier-without-source
  section: 2026-10-06/cve-2026-21589-atlassian-data-center-arbitrary-file-access
  item: "update section 2026-10-16T04:11:30Z and record summary"
  url_or_quote: "so no public source reports a compromise"
  summary: "(low confidence) A universal negative stated as the consequence of the CISA alert's silence (https://www.cisa.gov/news-events/alerts/2026/10/15/cisa-adds-one-known-exploited-vulnerability-catalog carries no exploitation detail). The sourcing_note scopes the claim to the cited honeypot operators and BleepingComputer; the section and the record should say 'neither CISA nor the honeypot operators report a compromise'."
- code: F3
  category: claim-not-supported
  section: 2026-10-10/ahsaycbs-cve-2026-105133-105134-exploited-webshells-xmrig
  item: "update section 2026-10-16T04:09:30Z, Bitdefender sentence"
  url_or_quote: "in the first two, attackers validated access with JSP webshells, staged PowerShell and command files in C:\\Users\\Public ... in the second, obfuscated PowerShell also installed and configured OpenSSH ... and follow-on scripts were staged on a subdomain of a public static-site hosting service"
  summary: "(low confidence) Bitdefender (https://www.bitdefender.com/en-us/blog/businessinsights/technical-advisory-ahsaycbs-exploitation-chain-cve-2026-105133-cve-2026-105134): MDR 'tried to stage payloads as command files (.cmd)' in C:\\Users\\Public, and the static-site staging is stated for 'MDR's incidents' in general, not for the second incident. The clause chain attaches both to the second incident and turns 'tried to stage' into 'staged'."
- code: F4
  category: hallucinated-fact
  section: run-record
  item: "run record notes, KEV sweep paragraph"
  url_or_quote: "Ahsay's own hotfixes and its admission that the August patches were incomplete"
  summary: "(low confidence) The iteration-1 F5 removed 'August' from the entry because no cited source dates the earlier patches (Ahsay: 'our previous patches v9.15.2.59 and v10.3.4.0'; release notes of 10.3.4 are dated 05-Aug-2026 and list no security fix). The published verification notes still say 'the August patches'."
- code: F8
  category: needs-more-research
  section: 2026-10-16/peerstitch-fortigate-implant-cve-2025-61624-fortimanager
  item: "Exposure line, FortiManager clause"
  url_or_quote: "and a FortiManager reachable on TCP 541 from untrusted networks, where the intrusion began"
  summary: "(low confidence) Reachability on TCP 541 alone is not exposure to CVE-2024-47575, which Fortinet fixed in October 2024 (https://www.fortiguard.com/psirt/FG-IR-24-423: fixed in 7.6.1, 7.4.5, 7.2.8, 7.0.13, 6.4.15 and 6.2.13). The line should scope the FortiManager condition to builds below those fixes (the entry's sources do not carry the versions; FG-IR-24-423 does) or say that a patched FortiManager is not the condition."
- code: F11
  category: editorial-advisory
  section: 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day
  item: "references[]"
  url_or_quote: "references: [2026-07-08/beyondtrust-rs-pra-preauth-bypass-cve-2026-40138-cluster]"
  summary: "The store already carries the actor profile entries/2026-06-05/verdantbamboo-unc5221-warp-panda-an-18-month-china-nexus-int.md (UNC5221 / ARMORY CASTLE alias); add it to references[] so the zero-day is linked to the actor history."
- code: F11
  category: editorial-advisory
  section: 2026-10-16/drupal-sa-core-2026-014-cve-2026-108097-field-ui-rce
  item: "sources[] for CVE-2026-108099"
  url_or_quote: "\"cvss\": \"Critical (Drupal advisory SA-CONTRIB-2026-218)\""
  summary: "The per-CVE authority for CVE-2026-108099 (https://www.drupal.org/sa-contrib-2026-218: Critical 19/25, affected <3.0.10, 'At least one known exploit path does not require authentication', read via WebFetch) is not in sources[]; the record rests on The Hacker News. Add the contrib advisory as a corroborating source."
- code: F11
  category: editorial-advisory
  section: 2026-10-16/adfection-candiru-spyware-zero-click-ad-delivery
  item: "Detection paragraph"
  url_or_quote: "Confiant adds that the SDK resolves an operator-chosen domain over DNS-over-HTTPS"
  summary: "'the SDK' has no antecedent in the entry (the body says 'a cloaked payload'); name it 'the cloaked script's SDK' or 'the ad-delivered SDK'."
- code: F11
  category: editorial-advisory
  section: 2026-10-16/cve-2026-102764-beyondtrust-remote-support-zero-day
  item: "immediate_action and actions[1] versus Defender takeaway"
  url_or_quote: "then redeploy it from a clean patched image (immediate_action); then redeploy from a clean, fully patched image (actions[1]) vs 'treat each one ... as potentially compromised until reviewed, and redeploy from a clean image any whose status is confirmed or unknown' (takeaway)"
  summary: "GTIG's wording is 'Redeploy appliances with confirmed or unknown compromise status' and customers cannot audit the host file system, so the two are close, but the action says every internet-reachable appliance while the takeaway says confirmed-or-unknown. State one rule in both places."
```
