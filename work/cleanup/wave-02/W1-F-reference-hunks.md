# W1-F: reference-branch entry hunks (unverified drafts)

Drafts from `cleanup/2026-10-18-carry-forward`, diffed against its base `58416ebf`. Porting rules: re-derive on top of `main`, re-verify every claim against its source, re-record under the porting wave's run id with a fresh `at` (never copy the draft's record).

## 2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n

main changed this file since base 58416ebf: no

```diff
diff --git a/entries/2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n.md b/entries/2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n.md
index 66c22de8..27882b0b 100644
--- a/entries/2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n.md
+++ b/entries/2026-05-08/qilin-ransomware-hits-die-linke-germany-1-5-tb-claimed-dpa-n.md
@@ -2,8 +2,8 @@
 schema: 1
 kind: incident
 title: "Qilin claims a ransomware attack on the German party Die Linke; the party has not confirmed data theft"
-headline: "Die Linke took its infrastructure offline after a suspected Qilin attack; Qilin listed the party on its leak site without samples"
-summary: "Die Linke disclosed on 2026-03-27 that it had taken its infrastructure offline after a suspected ransomware attack it attributes to Qilin. Qilin listed the party on its leak site on 2026-04-01 without publishing samples. The party says its member database was not affected and that it cannot assess whether the attackers' aim of publishing internal data will succeed or has already occurred, and Heise reported that which internal data was compromised had not yet been definitively clarified."
+headline: "Die Linke took parts of its IT offline after a suspected Qilin attack; Qilin listed the party without samples"
+summary: "Die Linke disclosed on 2026-03-27 that it had taken parts of its IT infrastructure offline after a suspected ransomware attack it attributes to Qilin. Qilin listed the party on its leak site on 2026-04-01 without publishing samples. The party says its member database was not affected and that it cannot assess whether the attackers' aim of publishing internal data will succeed or has already occurred, and Heise reported that which internal data was compromised had not yet been definitively clarified."
 discovered_at: "2026-05-08T05:00:04Z"
 event_date: 2026-03-26
 run_id: 2026-05-08-migrated
@@ -70,6 +70,14 @@ updates:
       party's own statement, Heise, BleepingComputer and The Record, and the priority moves from
       notable to routine because the sources give no access vector.
     fields: [title, headline, summary, event_date, priority, techniques, sources, evidence, verification, classification, body, sourcing_note, confidence]
+  - at: "2026-10-18T13:57:16Z"
+    run_id: 2026-10-18T1307Z-audit
+    type: correction
+    internal: true
+    summary: >
+      The headline and summary say the party took parts of its IT infrastructure offline, as its own
+      statement and the main analysis say, instead of its infrastructure as a whole.
+    fields: [headline, summary]
 ---
 
 Die Linke detected a cyberattack on its IT network on Thursday, 26 March 2026, took parts of its IT infrastructure offline as a precaution and filed a criminal complaint. In a statement the next day it said it had indications of a ransomware attack by the Qilin group and that its member database was not affected ([Die Linke, 2026-03-27](https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/)). Heise reported that it had not yet been definitively clarified which internal data had been compromised ([Heise Online, 2026-03-27](https://www.heise.de/en/news/Qilin-Left-Party-reports-Russian-ransomware-attack-11227232.html)). Qilin added the party to its leak site on 2026-04-01 without publishing data samples ([BleepingComputer, 2026-04-03](https://www.bleepingcomputer.com/news/security/die-linke-german-political-party-confirms-data-stolen-by-qilin-ransomware/)). **Contradiction:** BleepingComputer's headline says the party confirmed the data theft, while its own text says the party stopped short of confirming a data breach ([BleepingComputer, 2026-04-03](https://www.bleepingcomputer.com/news/security/die-linke-german-political-party-confirms-data-stolen-by-qilin-ransomware/)). The party says the attackers aim to publish sensitive internal data and personal information of headquarters staff, and that it cannot assess whether or to what extent this will succeed or has already happened ([Die Linke, 2026-03-27](https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/)).
```

## 2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u

main changed this file since base 58416ebf: no

```diff
diff --git a/entries/2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u.md b/entries/2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u.md
index 389a13a8..b677074f 100644
--- a/entries/2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u.md
+++ b/entries/2026-05-10/sophos-beagle-backdoor-distributed-via-fake-claude-ai-site-u.md
@@ -11,11 +11,9 @@ priority: notable
 immediate_action: null
 tags:
   - phishing
-  - infostealer
 regions:
   - global
-sectors:
-  - technology
+sectors: []
 entities:
   - "tool:beagle-fake-claude-stac4713-2026"
 techniques: [T1583.008, T1204.002, T1547.001, T1574, T1574.001, T1573.001]
@@ -58,6 +56,15 @@ updates:
       detection and takeaway lines. A Contradiction line records that Malwarebytes calls the payload
       PlugX while Sophos identifies a new backdoor, Beagle.
     fields: [summary, body, classification, techniques]
+  - at: "2026-10-18T13:56:53Z"
+    run_id: 2026-10-18T1307Z-audit
+    type: correction
+    internal: true
+    summary: >
+      The infostealer tag contradicted the body: Sophos describes Beagle as a simple backdoor with
+      remote-shell and file-management commands. The technology sector was removed because no source names
+      a targeted sector.
+    fields: [tags, sectors]
 ---
 
 Sophos X-Ops published a write-up on 2026-05-07 of a counterfeit Claude AI site distributing a previously undocumented Windows backdoor it named **Beagle**, and assesses that the site is likely part of an active malvertising campaign ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). The chain delivers a roughly 505 MB ZIP archive containing a malicious MSI that drops a *legitimate, signed G DATA antivirus updater executable*, an encrypted data file and an attacker-controlled DLL into the user's startup folder, so the updater sideloads the malicious DLL (DLL side-loading) ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). The DLL decrypts the data file and executes the resulting Donut (DonutLoader) shellcode, an open-source in-memory loader, which loads Beagle ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). Beagle communicates with a subdomain of the same lookalike site over TCP/443 and UDP/8080 with AES-encrypted payloads, and its eight commands are `uninstall`, `cmd`, `upload`, `download`, `mkdir`, `rename`, `ls` and `rm` ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). Sophos notes that an almost identical G DATA sideloading chain has previously been associated with PlugX, which several threat groups use, and suggests the Beagle payload may reflect an actor retooling or imitating another actor's chain. It does not attribute the campaign ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)). A possible hosting server was set up in March 2026, and Sophos found related samples reusing the same XOR key from February, March and April 2026, while cautioning that further evidence would be needed to link them to the same actor ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor)).
```

## 2026-05-16/gtig-unc6671-blackfile-vishing-aitm-rogue-mfa-programmatic-s

main changed this file since base 58416ebf: no

```diff
diff --git a/entries/2026-05-16/gtig-unc6671-blackfile-vishing-aitm-rogue-mfa-programmatic-s.md b/entries/2026-05-16/gtig-unc6671-blackfile-vishing-aitm-rogue-mfa-programmatic-s.md
index f4837fa2..8add8be6 100644
--- a/entries/2026-05-16/gtig-unc6671-blackfile-vishing-aitm-rogue-mfa-programmatic-s.md
+++ b/entries/2026-05-16/gtig-unc6671-blackfile-vishing-aitm-rogue-mfa-programmatic-s.md
@@ -20,7 +20,7 @@ regions:
 sectors: []
 entities:
   - "actor:unc6671"
-techniques: [T1566, T1566.004, T1557, T1111, T1556, T1098.005, T1539, T1550.004, T1213.002, T1530]
+techniques: [T1566, T1566.004, T1557, T1111, T1098.005, T1539, T1550.004, T1213.002, T1530]
 cves: []
 sources:
   - url: "https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/"
@@ -56,6 +56,15 @@ updates:
       recommendation, the context-only ShinyHunters link and three victim sectors GTIG does not name
       are removed. Priority is lowered to notable because the targeting GTIG reports is in North America, Australia and the UK, and the entry gains an ATT&CK mapping.
     fields: [body, classification, techniques, title, headline, summary, priority, entities, sectors]
+  - at: "2026-10-18T13:56:53Z"
+    run_id: 2026-10-18T1307Z-audit
+    type: correction
+    internal: true
+    summary: >
+      T1556 (Modify Authentication Process) was removed from the ATT&CK mapping: GTIG describes
+      registering an attacker-controlled MFA device and relaying MFA codes, which T1098.005 and T1111
+      already carry, and nothing that modifies an authentication mechanism.
+    fields: [techniques]
 ---
 
 Google Threat Intelligence Group published on 2026-05-15 an analysis of UNC6671, a financially motivated extortion cluster that adopted the "BlackFile" brand by February 2026 and has targeted dozens of organizations across North America, Australia and the UK ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). Callers hired by the actor phone employees' personal mobile numbers, pose as internal IT or helpdesk staff citing a passkey migration or MFA update, and send the victim to a lookalike single sign-on portal on Tucows-registered domains, lately as organization-named subdomains with "passkey" or "enrollment" themes ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). The operator relays the credentials and the MFA code or push approval to the real SSO provider in real time, then immediately registers a new attacker-controlled MFA device for persistence ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)). GTIG stresses that these compromises come from social engineering, not a vendor vulnerability ([Google Threat Intelligence Group, 2026-05-15](https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/)).
```

## 2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv

main changed this file since base 58416ebf: no

```diff
diff --git a/entries/2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv.md b/entries/2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv.md
index 213137dd..f587f462 100644
--- a/entries/2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv.md
+++ b/entries/2026-05-20/microsoft-dcu-disrupts-fox-tempest-malware-signing-as-a-serv.md
@@ -7,7 +7,7 @@ summary: >
   Microsoft's Digital Crimes Unit disrupted Fox Tempest, a malware-signing service active since May
   2025 that abused Microsoft Artifact Signing to obtain code-signing certificates valid for 72 hours,
   seizing its website under a case unsealed in the Southern District of New York and revoking over a
-  thousand certificates. Microsoft links it to Vanilla Tempest (Rhysida), Storm-0501, Storm-2561 and
+  thousand certificates. Microsoft links it to Vanilla Tempest (which deployed Rhysida), Storm-0501, Storm-2561 and
   Storm-0249, and through cryptocurrency analysis to affiliates delivering INC, Qilin and Akira
   ransomware. The signed malware posed as AnyDesk, Teams, PuTTY and Webex installers.
 discovered_at: "2026-05-20T05:00:01Z"
@@ -76,6 +76,14 @@ updates:
       title no longer says the service fed INC, Qilin and Akira operations. The priority moves from
       high to notable.
     fields: [summary, body, classification, techniques, priority, title, headline]
+  - at: "2026-10-18T13:57:16Z"
+    run_id: 2026-10-18T1307Z-audit
+    type: correction
+    internal: true
+    summary: >
+      The summary's parenthetical now reads that Vanilla Tempest deployed Rhysida, as Microsoft says,
+      instead of reading as if the actor were the ransomware family.
+    fields: [summary]
 ---
 
 Microsoft's Digital Crimes Unit unsealed a legal case in the US District Court for the Southern District of New York against Fox Tempest, a malware-signing-as-a-service (MSaaS) operation active since May 2025. It seized the service's website, took hundreds of the virtual machines running the operation offline and blocked access to a site hosting its code ([Microsoft On the Issues, 2026-05-19](https://blogs.microsoft.com/on-the-issues/2026/05/19/disrupting-fox-tempest-a-cybercrime-service/)). Fox Tempest abused Microsoft Artifact Signing (formerly Azure Trusted Signing) to obtain Microsoft-issued code-signing certificates valid for only 72 hours, which let malware masquerade as software such as AnyDesk, Teams, PuTTY and Webex and bypass security controls. Microsoft assesses that the actor very likely used stolen identities based in the United States and Canada to pass Artifact Signing's identity validation ([Microsoft Threat Intelligence, 2026-05-19](https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/)).
```

## 2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands

main changed this file since base 58416ebf: no

```diff
diff --git a/entries/2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands.md b/entries/2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands.md
index 78f08141..ea9884be 100644
--- a/entries/2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands.md
+++ b/entries/2026-05-28/nx-console-tanstack-daemon-tools-supply-chain-cascade-lands.md
@@ -31,7 +31,7 @@ techniques: [T1195.002, T1552.001, T1567]
 affected_products: ["Nx Console", "DAEMON Tools Lite"]
 cves:
   - id: CVE-2026-48027
-    cvss: n/a
+    cvss: "9.3 (CVSS 4.0)"
     epss: null
     type: null
     vector: user-interaction
@@ -40,8 +40,10 @@ cves:
       - exploited
       - cisa-kev
       - patch-available
+    affected: "Nx Console 18.95.0"
+    fixed: "18.100.0"
   - id: CVE-2026-45321
-    cvss: n/a
+    cvss: "9.6 (CVSS 3.1)"
     epss: null
     type: null
     vector: user-interaction
@@ -50,8 +52,10 @@ cves:
       - exploited
       - cisa-kev
       - patch-available
+    affected: "84 versions across 42 @tanstack/* packages"
+    fixed: null
   - id: CVE-2026-8398
-    cvss: n/a
+    cvss: "9.3 (CVSS 4.0); 9.8 (CVSS 3.1)"
     epss: null
     type: null
     vector: user-interaction
@@ -60,6 +64,8 @@ cves:
       - exploited
       - cisa-kev
       - patch-available
+    affected: "DAEMON Tools Lite 12.5.0.2421 to 12.5.0.2434"
+    fixed: "12.6"
 sources:
   - url: "https://nx.dev/blog/nx-console-v18-95-0-postmortem"
     publisher: Nx postmortem
@@ -119,6 +125,15 @@ updates:
       linked. The exposure and detection lines now also cover the upstream TanStack compromise as
       TanStack's advisory describes it.
     fields: [sources, body, evidence, sourcing_note, classification, techniques, tags, summary, entities, affected_products]
+  - at: "2026-10-18T14:01:10Z"
+    run_id: 2026-10-18T1307Z-audit
+    type: improvement
+    internal: true
+    summary: >
+      The three CVE records carry the scores their CNAs publish (CVE-2026-48027 9.3 on CVSS 4.0,
+      CVE-2026-45321 9.6 on CVSS 3.1, CVE-2026-8398 9.3 on CVSS 4.0 and 9.8 on CVSS 3.1) and the affected
+      and fixed versions from the CVE records, in place of n/a and empty values.
+    fields: [cves]
 ---
 
 **Background.** The CISA KEV adds on 2026-05-27 close a chain of disclosures across the preceding three weeks that share a single operational pattern: trusted developer-tooling-publishing pipelines (a maintainer's machine, a vendor build server, a popular VS Code marketplace listing) used to push malicious code to downstream consumers at scale ([CISA KEV catalog, 2026-05-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json); [Nx postmortem, 2026-05-21](https://nx.dev/blog/nx-console-v18-95-0-postmortem); [GHSA-c9j4-9m59-847w, 2026-05-18](https://github.com/nrwl/nx-console/security/advisories/GHSA-c9j4-9m59-847w); [GHSA-g7cv-rxg3-hmpx, 2026-05-11](https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx); [Disc Soft Limited, 2026-05-06](https://blog.daemon-tools.cc/post/security-incident); [Kaspersky, 2026-05-05](https://www.kaspersky.com/blog/daemon-tools-supply-chain-attack/55691/); [Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). The TanStack compromise was carried out via Mini Shai-Hulud, TeamPCP's self-replicating worm that steals CI/CD credentials and uses them to publish infected versions of more packages ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)). Three of the chain's CVEs were added to CISA KEV on the same day (2026-05-27), confirming in-the-wild exploitation ([CISA KEV catalog, 2026-05-27](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)), and GitHub's CISO Alexis Wales named the malicious Nx Console extension as the vector for the theft of about 3,800 of GitHub's internal repositories ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/github-grafana-breach-root-cause-nx-console/)).
```

## 2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev

main changed this file since base 58416ebf: no

```diff
diff --git a/entries/2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev.md b/entries/2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev.md
index 8645b846..e7b8d6c8 100644
--- a/entries/2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev.md
+++ b/entries/2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan-manager-auth-bypass-kev.md
@@ -58,7 +58,7 @@ sources:
     role: corroborating
   - url: "https://www.cisco.com/c/en/us/td/docs/routers/sdwan/26x-later/network-monitoring/network-monitoring-guide/live-protect-for-cisco-catalyst-sd-wan.html"
     publisher: "Cisco (Catalyst SD-WAN Network Monitoring Guide, Live Protect)"
-    date: "2026-07-01"
+    date: "2026-09-22"
     role: corroborating
 closed_sources: []
 evidence:
@@ -105,6 +105,14 @@ updates:
       describes as temporary, partial protection that may block legitimate logins using URI encoding. The first fixed
       releases are unchanged and the upgrade remains Cisco's only remediation.
     fields: [summary, immediate_action, actions, body, sources, evidence]
+  - at: "2026-10-18T13:58:23Z"
+    run_id: 2026-10-18T1307Z-audit
+    type: correction
+    internal: true
+    summary: >
+      The Cisco Live Protect guide is dated 2026-09-22, the 'Updated' date the page shows, instead of
+      2026-07-01, which appears nowhere on the page.
+    fields: [sources, body]
 migrated_from: null
 ---
 
@@ -124,4 +132,4 @@ Cisco's first fixed releases are 20.9.10.1, 20.12.8.2, 20.15.6.1, 20.18.4.1, 26.
 
 ## Update — 2026-10-03T04:55:00Z
 
-Cisco revised its advisory to version 1.1 on 2026-10-02 ("Added information about Live Protect shield availability") and now states it has released a Live Protect shield for CVE-2026-76504 "to provide temporary security coverage" while upgrades are planned ([Cisco PSIRT, 2026-09-30](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU)). Cisco says the shield offers only temporary partial protection and that, once applied, a legitimate user with URI encoding might not be able to log in to the Manager ([Cisco PSIRT, 2026-09-30](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU)). Cisco's Live Protect page lists the feature from Catalyst SD-WAN Control Components release 20.18.3, describes a monitoring mode that shows exploit attempts without enforcing and an enforce mode that applies the mitigation, and says Cisco creates shields for the release current when a shield is published and for the two immediately preceding releases in each supported release train that includes Live Protect, so older releases may have no shield ([Cisco, 2026-07-01](https://www.cisco.com/c/en/us/td/docs/routers/sdwan/26x-later/network-monitoring/network-monitoring-guide/live-protect-for-cisco-catalyst-sd-wan.html)). The fixed releases, the exploitation statement and the KEV listing are unchanged, and Cisco keeps its position that the only remediation is the upgrade.
+Cisco revised its advisory to version 1.1 on 2026-10-02 ("Added information about Live Protect shield availability") and now states it has released a Live Protect shield for CVE-2026-76504 "to provide temporary security coverage" while upgrades are planned ([Cisco PSIRT, 2026-09-30](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU)). Cisco says the shield offers only temporary partial protection and that, once applied, a legitimate user with URI encoding might not be able to log in to the Manager ([Cisco PSIRT, 2026-09-30](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU)). Cisco's Live Protect page lists the feature from Catalyst SD-WAN Control Components release 20.18.3, describes a monitoring mode that shows exploit attempts without enforcing and an enforce mode that applies the mitigation, and says Cisco creates shields for the release current when a shield is published and for the two immediately preceding releases in each supported release train that includes Live Protect, so older releases may have no shield ([Cisco, 2026-09-22](https://www.cisco.com/c/en/us/td/docs/routers/sdwan/26x-later/network-monitoring/network-monitoring-guide/live-protect-for-cisco-catalyst-sd-wan.html)). The fixed releases, the exploitation statement and the KEV listing are unchanged, and Cisco keeps its position that the only remediation is the upgrade.
```

## 2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities

main changed this file since base 58416ebf: no

```diff
diff --git a/entries/2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities.md b/entries/2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities.md
index 02c07b1a..6970d5d6 100644
--- a/entries/2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities.md
+++ b/entries/2026-10-02/ftapi-ransomware-the-gentlemen-supplier-to-authorities.md
@@ -4,7 +4,7 @@ kind: incident
 title: "FTAPI, a file-transfer vendor whose customers include authorities, confirms ransomware on an internal server; The Gentlemen list it on their leak site"
 headline: "A file-transfer supplier to authorities had ransomware on one internal server; the vendor says its platform is untouched"
 summary: >
-  FTAPI Software of Munich, whose secure file-transfer service is used by authorities and companies, told heise that
+  FTAPI of Munich, whose secure file-transfer service is used by authorities and companies, told heise that
   unauthorised parties installed ransomware on a single internal server, detected on 2026-09-14, and says its platform,
   customer systems and exchanged data were not affected. The Gentlemen ransomware group listed FTAPI on its leak site
   with a countdown that heise read as about five days on 2026-09-29.
@@ -58,7 +58,14 @@ classification:
   credibility: 2
 watchlist_hit: false
 actions: []
-updates: []
+updates:
+  - at: "2026-10-18T13:58:23Z"
+    run_id: 2026-10-18T1307Z-audit
+    type: correction
+    internal: true
+    summary: >
+      The summary names the vendor 'FTAPI of Munich' as the cited sources do.
+    fields: [summary]
 migrated_from: null
 ---
 
```

## 2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale

main changed this file since base 58416ebf: no

```diff
diff --git a/entries/2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale.md b/entries/2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale.md
index 8336fd6d..fca0f3d7 100644
--- a/entries/2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale.md
+++ b/entries/2026-10-08/ixa-systems-vaud-security-integrator-thegentlemen-sale.md
@@ -7,8 +7,9 @@ summary: >
   Le Temps reports, and the AWP news agency names the firm as Ixa Systems of Crissier (Vaud), that data stolen from
   a video-surveillance, alarm and access-control integrator is on sale on the darknet; the group TheGentlemen
   claimed the theft at the end of August. The loot reportedly includes camera locations, security-installation
-  plans and, in some cases, usernames or passwords, for clients including police authorities, gendarmerie
-  premises, prisons, hospitals, schools and banks; the reports do not state the access vector or list every affected site.
+  plans and, in some cases, usernames or passwords. The firm's customers include police authorities, banks,
+  hospitals, schools and prisons; the organisations reported as affected are judicial entities, gendarmerie
+  premises, several banks and several dozen companies. The reports do not state the access vector or list every affected site.
 discovered_at: "2026-10-08T04:52:00Z"
 updated_at: null
 event_date: "2026-10-06"
@@ -58,7 +59,16 @@ classification:
 watchlist_hit: false
 actions:
   - "If your organisation bought video-surveillance, alarm or access-control installation or maintenance from Ixa Systems, ask the firm in writing which of your sites and credentials are in the stolen data and rotate every camera, alarm, intercom and remote-maintenance credential it held."
-updates: []
+updates:
+  - at: "2026-10-18T14:00:04Z"
+    run_id: 2026-10-18T1307Z-audit
+    type: correction
+    summary: >
+      The summary listed police authorities, prisons, hospitals, schools and banks as clients whose data
+      is in the loot. Those are the firm's customer categories as AWP describes them; the organisations
+      the reports name as affected are judicial entities, gendarmerie premises, several banks and several
+      dozen companies.
+    fields: [summary]
 migrated_from: null
 ---
 
@@ -71,3 +81,7 @@ Le Temps says the group TheGentlemen announced and claimed the theft on the dark
 **Detection:** because the data reportedly holds usernames, passwords and camera locations, the telemetry is the authentication log of video-management, alarm and access-control systems (logins from unfamiliar source networks or from the supplier's accounts) and the log of any remote-maintenance path the supplier used ([Le Temps, 2026-10-06](https://www.letemps.ch/suisse/vaud/une-cyberattaque-fait-fuiter-des-informations-de-securite-de-prisons-vaudoises-de-banques-et-de-dizaines-de-societes); [ICTjournal, 2026-10-07](https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois)).
 
 **Defender takeaway:** ask the supplier in writing whether your sites are in the data, treat every camera, alarm, intercom and remote-maintenance credential it held as exposed and rotate it, and confirm that the devices are not reachable from outside a segmented network, the point the canton's delegate makes ([ICTjournal, 2026-10-07](https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois)).
+
+## Correction — 2026-10-18T14:00:04Z
+
+The summary of this entry listed police authorities, prisons, hospitals, schools and banks as clients whose data is in the stolen set. Those are the firm's customers in general, as AWP describes them ([AWP via cash.ch, 2026-10-07](https://www.cash.ch/news/top-news/hacker-erbeuten-schweizer-sicherheitsdaten-von-gefangnissen-und-banken-974664)); the organisations ICTjournal names as concerned are the Établissements de la plaine de l'Orbe and other judicial entities, gendarmerie premises, several banks including the Banque cantonale vaudoise, and several dozen companies ([ICTjournal, 2026-10-07](https://www.ictjournal.ch/news/2026-10-07/une-cyberattaque-expose-des-donnees-de-securite-de-sites-vaudois)).
```
