---
schema: 1
kind: vulnerability
horizon: operational
title: "CVE-2026-72529 and CVE-2026-72530 — a two-stage pre-authentication chain on TrueConf Server's default-open port reaches SYSTEM, and the exploited servers were used to hand trojanized clients to everyone who joined a meeting"
headline: "Both flaws entered the exploited catalogue on 20 August; the fix shipped on 18 June and every release since 2022 is vulnerable"
summary: >
  CISA catalogued CVE-2026-72529 and CVE-2026-72530 as exploited on 2026-08-20. Together they are a
  pre-authentication chain on TrueConf Server, a self-hosted video-conferencing platform: an unauthenticated
  caller reaching port 4307/TCP invokes an undocumented function to run a script inside a restricted
  environment, then escapes that environment to execute code on the host as SYSTEM. Kaspersky ICS CERT,
  which reported both flaws, documents an intrusion set using the chain against Russian organisations to
  plant a web shell in the product's own web tree, delete the event-log records the exploit generated,
  read the server database, and replace the Windows client installer the server offers to meeting guests
  with a trojanized copy. Fixes shipped on 18 June 2026 in 5.3.9, 5.4.9 and 5.5.5; Kaspersky's own analysis
  found every release since 2022 vulnerable, and the vendor's documentation has the port open by default.
discovered_at: "2026-08-22T05:06:00Z"
event_date: "2026-08-20"
run_id: 2026-08-22T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, actively-exploited, cisa-kev, supply-chain, patch-available]
regions: [global]
sectors: [public-sector, telco]
entities: [actor:head-mare, malware:phantomcore]
techniques: [T1190, T1611, T1505.003, T1070, T1543.003, T1195.002, T1102]
affected_products: ["TrueConf Server"]
cves:
  - id: CVE-2026-72529
    cvss: "9.8"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "all versions before 5.3; 5.3.x before 5.3.9; 5.4.x before 5.4.9; 5.5.x before 5.5.5 — affected component named by the vendor as the service on 4307/TCP"
    fixed: "5.3.9 / 5.4.9 / 5.5.5 (released 18 June 2026)"
  - id: CVE-2026-72530
    cvss: "9.0"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "all versions before 5.3.9; 5.4.x before 5.4.9; 5.5.x before 5.5.5"
    fixed: "5.3.9 / 5.4.9 / 5.5.5 (released 18 June 2026)"
sources:
  - url: "https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/"
    publisher: "Kaspersky ICS CERT"
    date: "2026-08-12"
    role: primary
  - url: "https://ics-cert.kaspersky.com/advisories/2026/08/11/trueconf-server-missing-authentication-for-critical-function/"
    publisher: "Kaspersky ICS CERT (KLCERT-26-057)"
    date: "2026-08-11"
    role: primary
  - url: "https://ics-cert.kaspersky.com/advisories/2026/08/11/trueconf-server-breakout-from-isolated-environment/"
    publisher: "Kaspersky ICS CERT (KLCERT-26-058)"
    date: "2026-08-11"
    role: primary
  - url: "https://trueconf.com/blog/news/security-fixes-updates-and-advisories"
    publisher: "TrueConf"
    date: "2026-08-11"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog"
    date: "2026-08-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An unauthorized remote attacker with network access via port 4307/TCP to TrueConf server versions 5.3.X before 5.3.9, 5.4.X before 5.4.9, 5.5.X before 5.5.5, as well as all versions before 5.3, could execute an arbitrary script by calling an undocumented function."
    publisher: "Kaspersky ICS CERT (KLCERT-26-057)"
  - quote: "An unauthorized remote attacker with network access via port 4307/TCP to TrueConf server versions 5.3.X before 5.3.9, 5.4.X before 5.4.9, 5.5.X before 5.5.5, as well as all versions before 5.3, could use a specially crafted script to break out of the isolated environment and execute arbitrary code on the host system."
    publisher: "Kaspersky ICS CERT (KLCERT-26-058)"
  - quote: "Improper management of code generation can allow an attacker who has achieved code execution in the TrueConf Server isolated environment to escape the sandbox and execute arbitrary commands on the underlying operating system."
    publisher: "TrueConf"
  - quote: "via port 4307/TCP (open by default, according to TrueConf documentation)"
    publisher: "Kaspersky ICS CERT"
  - quote: "our internal analysis showed that all TrueConf server versions released since 2022 are vulnerable"
    publisher: "Kaspersky ICS CERT"
  - quote: "This enables them to replace the file"
    publisher: "Kaspersky ICS CERT"
  - quote: "on *nix systems, the attackers install a backdoor that uses GitHub as a command and control channel"
    publisher: "Kaspersky ICS CERT"
verification: multi-source
sourcing_note: >
  Kaspersky ICS CERT reported both flaws and is the sole source of the exploitation account; TrueConf's own
  security-bulletin table independently confirms each identifier, its weakness class, its affected range
  and the fixed releases, which is what makes the CVE-to-flaw mapping explicit rather than positional.
  Both scoring scales are carried because the ranking inverts between them: under CVSS 3.1 the
  missing-authentication flaw scores higher (9.8 against 9.0), under CVSS 4.0 the sandbox escape does
  (9.5 against 9.3). Do not read a score off the discoverer's advisory pages directly — both render a
  "CVSS v3 Base Score" of 0.0 to a plain fetch because the number is computed client-side; the figures here
  come from the CNA record and the vendor's own table, which agree. The two published ranges agree once read carefully — the
  vendor's own table gives the sandbox-escape flaw as everything below 5.3.9, which has no lower bound and
  therefore already covers the pre-5.3 releases the discoverer's advisory names explicitly. Kaspersky's
  separate internal-analysis statement is broader than both published ranges and is the one to plan against. The victim geography is stated once and narrowly — Kaspersky describes an attack on
  Russian organisations and names no other country; the actor's wider targeting history is background, not
  a finding about this campaign. No source fetched states that public exploit code exists.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Upgrade TrueConf Server to 5.3.9, 5.4.9 or 5.5.5 on the matching branch, then treat any instance that was reachable on 4307/TCP while unpatched as suspect rather than fixed: check the modification times of files under the product's own web tree — the overwritten file is a PHP file inside the directory that otherwise holds the interface JavaScript, so a hunt keyed on script extensions alone will miss it — against the install or last-upgrade time, and reconcile the Windows client installer the server offers to guests against the vendor's published release. A replaced installer is served onward to everyone who joins a meeting, so the client fleet is in scope, not just the server."
  - "Take the conferencing service off the open internet where the deployment does not require it: the vendor's documentation has 4307/TCP open by default, so an instance nobody deliberately exposed can still be answering."
migrated_from: null
---

CISA added CVE-2026-72529 and CVE-2026-72530 to its exploited-vulnerabilities catalogue on 2026-08-20, with remediation dates of 23 August and 3 September for US federal agencies. The two are one chain in TrueConf Server, a self-hosted video-conferencing and unified-communications platform marketed as an on-premises alternative to hosted meeting services. The first stage is an authentication gap rather than a memory bug: an unauthorised remote attacker with network access to port 4307/TCP can execute an arbitrary script by calling an undocumented function ([Kaspersky ICS CERT, 2026-08-11](https://ics-cert.kaspersky.com/advisories/2026/08/11/trueconf-server-missing-authentication-for-critical-function/)). That script runs inside a restricted environment, which is what the second flaw defeats: the vendor describes it as improper management of code generation allowing an attacker who has achieved code execution inside the isolated environment to escape the sandbox and execute arbitrary commands on the underlying operating system ([TrueConf, 2026-08-11](https://trueconf.com/blog/news/security-fixes-updates-and-advisories)), and its discoverer's advisory records the same chain reached from the same unauthenticated position on the same port ([Kaspersky ICS CERT, 2026-08-11](https://ics-cert.kaspersky.com/advisories/2026/08/11/trueconf-server-breakout-from-isolated-environment/)). The exposure question answers itself: Kaspersky states the port is open by default according to TrueConf's own documentation ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/)). Fixes shipped on 18 June 2026 in 5.3.9, 5.4.9 and 5.5.5, and Kaspersky's own internal analysis found every TrueConf Server release since 2022 vulnerable ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/)) — a wider statement than either advisory's own version range, and the one to plan against.

What the intrusion set did with SYSTEM on the conferencing server is the part that generalises past this product. Kaspersky, investigating an attack on Russian organisations, describes the operators overwriting a PHP file that sits inside the product's own web tree, in a directory otherwise holding JavaScript, with a PHP web shell and deleting the TrueConf event-log records the exploitation itself had generated — the anti-forensic step is separate from the persistence step, which matters because the log that would have shown the intrusion is the log that was pruned ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/)). The web shell was then used to survey the victim's infrastructure, obtain privileged access to the TrueConf Server database, and replace the legitimate Windows client installer the server hands to guests joining a meeting with a trojanized copy ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/)). That is the step that turns a server compromise into a client-fleet compromise: the distribution channel is the product's own guest join page, the file is served over the organisation's own trusted hostname, and the recipients are whoever was invited to a meeting — including external participants. Post-compromise command and control is deliberately layered rather than singular. On Windows the operators registered a pair of services acting as a communication module and an execution module, using a commercial cloud-storage account reached through its vendor's own API as the channel, and Kaspersky is explicit this backdoor is a *backup* path because subsequent activity ran through remotely executed scripts via the web shell. On Unix-family servers the tooling is different again: one backdoor hides its files and intercepts the product's own network functions to take operator commands over the conferencing protocol itself, and a separate backdoor uses a public code-hosting service as its channel ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/)).

**Defender takeaway:** patching the server is necessary and not sufficient, because two of the three consequences outlive the patch. The installer substitution reaches endpoints that were never in scope for the server upgrade, so the client fleet needs reconciling against the vendor's published release rather than assumed clean. The database access means credentials and directory content held by the conferencing platform should be treated as read. And the event-log deletion means the absence of exploitation evidence on an exposed, unpatched instance is not evidence of absence. The hunt anchors that survive all of this are ones the defender owns rather than the attacker chooses: modification timestamps on files inside the product's own installation tree that no upgrade explains, a gap or truncation in the product's own event log that does not correspond to a restart or a log-rotation policy, and outbound sessions from the conferencing server to consumer cloud-storage or code-hosting endpoints. **Triage:** a conferencing server legitimately talks to a great many external addresses — that is its job — so egress volume discriminates nothing. What separates this is the direction and the identity: the server process itself initiating authenticated sessions to a cloud-storage or code-hosting API that no configured integration accounts for, and a file under the product's own web tree whose modification time is newer than the last vendor upgrade, PHP included.
