---
schema: 1
kind: vulnerability
title: "CVE-2026-72529 and CVE-2026-72530 — a pre-auth chain on TrueConf Server's port 4307 reaches SYSTEM, and the operators use it to replace the client installer the server hands to everyone who joins a meeting"
headline: "Both flaws are now catalogued as exploited; the reach extends to organisations that run no TrueConf server of their own"
summary: >
  CISA added CVE-2026-72529 and CVE-2026-72530 to its Known Exploited Vulnerabilities catalogue on
  2026-08-20, and ENISA's EU Vulnerability Database independently records both as exploited since the
  same date. Chained, they take an unauthenticated attacker from network access on TrueConf Server's
  port 4307/TCP — open by default per the vendor's own documentation — to arbitrary command execution
  as SYSTEM: the first invokes an undocumented function to run a script inside a deliberately
  restricted sandbox, the second escapes that sandbox through a flaw in its code-generation logic.
  Kaspersky, which coordinated both CVEs and is the CNA, reports the group it calls Head Mare — a
  cluster it has now reclassified from hacktivist to APT — chaining them since at least July 2026 to
  plant a web shell, then overwrite the server's own distributed Windows client installer with an
  unsigned trojanised copy. That last step is why the exposure is not confined to TrueConf operators:
  staff who join a meeting hosted on a compromised contractor's server and accept its client-update
  prompt receive the backdoor. Fixed on 2026-06-18 in 5.3.9, 5.4.9 and 5.5.5, two months before the
  catalogue listing, and Kaspersky's own analysis puts the underlying flaw in every release since 2022.
discovered_at: "2026-08-23T05:05:00Z"
event_date: "2026-08-20"
run_id: 2026-08-23T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, actively-exploited, cisa-kev, rce, pre-auth, supply-chain, espionage, patch-available, default-config]
regions: [global, europe]
sectors: [energy, transport, telco, public-sector, manufacturing]
entities: [actor:head-mare, malware:phantomcore, malware:phantomgraph, malware:phantomhook, malware:phantomreact]
techniques: [T1190, T1611, T1505.003, T1554, T1036.005, T1543.003, T1543.002, T1102.002, T1003.001, T1572, T1027]
affected_products: ["TrueConf Server"]
cves:
  - id: CVE-2026-72529
    cvss: "9.8"
    epss: "0.79"
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "5.3.x before 5.3.9, 5.4.x before 5.4.9, 5.5.x before 5.5.5, and earlier releases — Kaspersky's own analysis found every release since 2022 vulnerable"
    fixed: "5.3.9 / 5.4.9 / 5.5.5 (2026-06-18)"
  - id: CVE-2026-72530
    cvss: "9.0"
    epss: "0.97"
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "5.3.x before 5.3.9, 5.4.x before 5.4.9, 5.5.x before 5.5.5, and earlier releases"
    fixed: "5.3.9 / 5.4.9 / 5.5.5 (2026-06-18)"
sources:
  - url: "https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/"
    publisher: "Kaspersky ICS CERT"
    date: "2026-08-12"
    role: primary
  - url: "https://securelist.com/head-mare-targets-trueconf-server-with-phantomcore/120988/"
    publisher: "Kaspersky Securelist"
    date: "2026-08-11"
    role: primary
  - url: "https://trueconf.com/blog/news/security-fixes-updates-and-advisories"
    publisher: "TrueConf"
    date: "2026-08-12"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities Catalog"
    date: "2026-08-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An unauthorized attacker can connect to TrueConf server versions 5.3.X before 5.3.9, 5.4.X before 5.4.9, 5.5.X before 5.5.5, as well as earlier versions (our internal analysis showed that all TrueConf server versions released since 2022 are vulnerable) via port 4307/TCP (open by default, according to TrueConf documentation) and execute a malicious script on the server by calling an undocumented function."
    publisher: "Kaspersky ICS CERT"
  - quote: "The uploaded malicious script is executed in an isolated environment, where potentially hazardous libraries (io, os, etc.) are unavailable. However, attackers can exploit another vulnerability (assigned internal Kaspersky identifier KLCERT-26-058) to execute arbitrary code on the server with NT AUTHORITY\\SYSTEM privileges."
    publisher: "Kaspersky ICS CERT"
  - quote: "Most importantly, during the attack, the attackers replace the TrueConf client distribution file located at C:\\Program Files\\TrueConf Server\\ClientInstFiles\\trueconf_windows_client_x64.exe."
    publisher: "Kaspersky ICS CERT"
  - quote: "Even if your organization does not use a TrueConf server, your employees may connect to compromised TrueConf servers of contractors to participate in online meetings and download infected installation packages."
    publisher: "Kaspersky ICS CERT"
  - quote: "The malicious distributions we detected did not have a valid digital signature."
    publisher: "Kaspersky Securelist"
  - quote: "Previously, we classified them as hacktivists, but now we define them as an APT group due to the sophistication of their TTPs and the absence of destructive activity (encryption, wiping) in the targeted infrastructures."
    publisher: "Kaspersky Securelist"
verification: multi-source
sourcing_note: >
  Kaspersky is both the coordinating CNA for the two CVEs and the party that observed the intrusions,
  so its two publications are one assessor; CISA's catalogue listing and ENISA's EU Vulnerability
  Database provide the independent exploitation determinations, and TrueConf's own advisory table
  independently republishes the scores and names the fixed releases. All observed targeting to date is
  of Russian organisations and no source reports victims elsewhere — this entry is included for the
  exposure path rather than for the victim set, and says so. The CVSS values are the CNA's own as
  republished in TrueConf's advisory table. The catalogue's remediation deadlines are US federal
  compliance dates and are deliberately not used here to frame urgency.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Patch TrueConf Server to 5.3.9, 5.4.9 or 5.5.5 and take port 4307/TCP off any internet-facing interface — it listens by default, and Kaspersky's own testing found the flaw present in every release since 2022, so an unpatched older build is affected even though it falls outside the published CVE ranges."
  - "Treat any TrueConf server that hosted external or contractor participants before patching as compromised until cleared: check whether the distributed Windows client installer under ClientInstFiles still carries a valid vendor signature, and check the web-accessible script directory for a modified locale.php."
migrated_from: null
---

CISA added both halves of this chain to its Known Exploited Vulnerabilities catalogue on 2026-08-20, and ENISA's EU Vulnerability Database independently records each as exploited since the same date. The chain is entirely pre-authentication and sits behind one port. **CVE-2026-72529** is a missing-authentication flaw: *"An unauthorized attacker can connect to TrueConf server versions 5.3.X before 5.3.9, 5.4.X before 5.4.9, 5.5.X before 5.5.5, as well as earlier versions (our internal analysis showed that all TrueConf server versions released since 2022 are vulnerable) via port 4307/TCP (open by default, according to TrueConf documentation) and execute a malicious script on the server by calling an undocumented function"* ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/)). That parenthesis matters more than the version list around it: the vendor-stated affected ranges understate the real exposure, so an older build outside the published ranges is not safe by omission.

The script lands inside a sandbox that deliberately withholds the dangerous standard libraries, which is where **CVE-2026-72530** comes in — a flaw in the sandbox's own code-generation logic. Kaspersky describes the join: *"The uploaded malicious script is executed in an isolated environment, where potentially hazardous libraries (io, os, etc.) are unavailable. However, attackers can exploit another vulnerability (assigned internal Kaspersky identifier KLCERT-26-058) to execute arbitrary code on the server with NT AUTHORITY\SYSTEM privileges"* ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/)). Both were fixed together on 2026-06-18 in 5.3.9, 5.4.9 and 5.5.5 — roughly two months before the exploitation listing, which is the usual and uncomfortable shape: the patch was available throughout the observed campaign.

**What the operators do with it.** Kaspersky attributes the activity to Head Mare, and records a classification change worth carrying because it sets expectations about intent: *"Previously, we classified them as hacktivists, but now we define them as an APT group due to the sophistication of their TTPs and the absence of destructive activity (encryption, wiping) in the targeted infrastructures"* ([Kaspersky Securelist, 2026-08-11](https://securelist.com/head-mare-targets-trueconf-server-with-phantomcore/120988/)). With SYSTEM in hand they overwrite a PHP file that sits in the server's public script directory with a web shell — the file's extension is .php even though the directory is named for JavaScript, which matters for anyone building the hunt — and delete the corresponding TrueConf event-log entries, then work from the shell — fingerprinting the environment over PowerShell, reaching the server database with elevated privileges, dumping LSASS memory through the built-in COM services library, and standing up an SSH reverse tunnel ([Kaspersky Securelist, 2026-08-11](https://securelist.com/head-mare-targets-trueconf-server-with-phantomcore/120988/)).

Then the step that changes who is exposed: *"Most importantly, during the attack, the attackers replace the TrueConf client distribution file located at C:\Program Files\TrueConf Server\ClientInstFiles\trueconf_windows_client_x64.exe"* ([Kaspersky ICS CERT, 2026-08-12](https://ics-cert.kaspersky.com/publications/reports/2026/08/12/head-mare-exploits-vulnerabilities-in-trueconf-server-to-deliver-phantomcore-malware/)). Meeting participants who accept the resulting update prompt install the genuine client alongside the PhantomCore backdoor, which unpacks into the user's local application-data tree under a filename mimicking a Windows C-runtime component and auto-launches from a registry class registration. Kaspersky notes the replaced installers carried no valid signature — *"The malicious distributions we detected did not have a valid digital signature"* ([Kaspersky Securelist, 2026-08-11](https://securelist.com/head-mare-targets-trueconf-server-with-phantomcore/120988/)) — which is the cheapest available check for anyone who has taken a server-offered client update recently. Kaspersky states the consequence directly: *"Even if your organization does not use a TrueConf server, your employees may connect to compromised TrueConf servers of contractors to participate in online meetings and download infected installation packages."*

On the server the group also installs PhantomGraph, a two-module Windows-service backdoor Kaspersky describes as a *backup* channel — the primary control path stays the web shell and remote PowerShell — which, in Kaspersky's words, uses "an account on Microsoft OneDrive cloud storage as their command-and-control (C2) server". Neither cited source says whether that account was compromised or attacker-registered, so this entry does not either. Kaspersky assesses the two service installs were split across separate encoded PowerShell commands deliberately, *"to make it harder to detect using EDR tools"*. On \*nix TrueConf servers the group installs **two** distinct backdoors: a rootkit that hides its own files and intercepts TrueConf's network functions to receive commands smuggled inside the TrueConf protocol itself, and a separate backdoor that uses GitHub as its command-and-control channel. Kaspersky's detection names for the pair are PhantomHook and PhantomReact; no source states which name belongs to which implant, so this entry does not assert the mapping. Its published artefact list also shows both persisting as systemd units under attacker-chosen service names, which is the \*nix counterpart to the Windows service persistence above.

All observed victims are Russian organisations, in instrument manufacturing, electronics, transportation, energy, IT and software development; no source reports targeting elsewhere. This entry is here for the exposure path rather than the victim list — a European organisation is reachable through the contractor-meeting vector regardless of whose servers the operators are currently choosing.

Detection concepts, telemetry class first. In **file-write telemetry on the server**, an unexpected write to the public script directory or to the client-installer path outside a vendor-update window is the highest-fidelity signal, and Kaspersky's own published rule names key on exactly those two events plus an unsigned installer. In **egress telemetry**, a videoconferencing server process making outbound HTTPS calls to a consumer cloud-storage service, or a \*nix TrueConf host calling code-hosting API endpoints, is anomalous for the appliance's role. In **endpoint process telemetry**, watch for the client installer's process tree loading a library from the user's local TrueConf directory whose name mimics a system component, and for new class registrations under the current user's registry hive. In **credential-access telemetry**, the COM-services LSASS dump technique and new outbound SSH sessions originating *from* the server are both worth alerting on.

**Defender takeaway:** patching the server is necessary but is not the whole remediation, because the compromise propagates outward through a trust relationship the product is designed around — the server distributes its own client, and users are trained to accept that prompt. **Triage:** a client update offered by your own TrueConf server is ordinary behaviour and looks identical to the attack; the discriminators are the installer's digital signature, which the malicious copies lack entirely, and whether a client-installer write on the server correlates with an actual vendor release rather than appearing on its own.
