---
schema: 1
kind: vulnerability
title: "CVE-2026-82078 / CVE-2026-81578 — PaperCut NG/MF: an Apache Tapestry request-routing confusion chains an unauthenticated config rewrite to arbitrary code execution, exploited before a patch existed"
headline: "A pre-auth RCE chain in PaperCut NG/MF was exploited before any patch existed; tested maintenance releases now replace three emergency patches"
summary: >
  PaperCut NG and PaperCut MF (all versions) carry an unauthenticated remote-code-execution chain — CVE-2026-81578
  (auth bypass, CVSS4.0 8.8) and CVE-2026-82078 (unsafe dynamic class loading, CVSS4.0 9.4) — that PaperCut confirmed
  under active exploitation on 2026-08-27, before any CVE or patch existed. Fully tested maintenance releases 26.0.5,
  25.0.13 and 24.1.10 (10 September 2026) replace the emergency patches and are the vendor's recommended build;
  servers still on Emergency Patch Release 1 or 2 need to upgrade now. There is no fix for v23 and earlier, and Huntress estimates 47% of the PaperCut installs it tracks run v23 or older.
  GreyNoise now documents an AI-agent-orchestrated mass-exploitation campaign against this same chain, compromising at least
  440 instances across 395 identified organizations since 31 August 2026, reaching full domain admin in as little as five
  minutes via legacy Active Directory escalation paths. watchTowr's write-up of 2026-10-09 shows the 28 August emergency build could
  still be taken without authentication through the Setup Wizard forms, and names CVE-2026-82077, an administrator-only Scan-to-Fax
  code-execution flaw that the vendor lists as fixed only in 26.0.5 and 25.0.13.
discovered_at: "2026-08-29T04:09:36Z"
updated_at: "2026-10-10T03:46:27Z"
event_date: "2026-08-27"
run_id: 2026-08-29T0409Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, zero-day, actively-exploited, pre-auth, rce, cisa-kev, no-patch, patch-available, poc-public]
regions: [global]
sectors: [public-sector, education, healthcare, finance, telco]
entities: []
techniques: [T1190, T1059.007, T1082, T1057, T1070.004, T1219, T1003.001, T1003.006, T1550.002, T1136.002, T1078.002]
affected_products: ["PaperCut NG", "PaperCut MF"]
cves:
  - id: CVE-2026-81578
    cvss: "8.8 (CVSS4.0)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "All versions of PaperCut NG and PaperCut MF"
    fixed: "Security maintenance releases 26.0.5, 25.0.13 and 24.1.10 (10 September 2026), which replace the emergency patches; Emergency Patch Release 3 also protects; no fix for v23 and earlier; upgrade to a supported line (24, 25 or 26)"
  - id: CVE-2026-82078
    cvss: "9.4 (CVSS4.0)"
    epss: null
    type: rce
    vector: zero-click
    auth: admin-required
    status: [exploited, cisa-kev, patch-available]
    affected: "All versions of PaperCut NG and PaperCut MF"
    fixed: "Security maintenance releases 26.0.5, 25.0.13 and 24.1.10 (10 September 2026), which replace the emergency patches; Emergency Patch Release 3 also protects; no fix for v23 and earlier; upgrade to a supported line (24, 25 or 26)"
  - id: CVE-2026-82077
    cvss: "7.3 (CVSS 4.0)"
    epss: null
    type: rce
    vector: zero-click
    auth: admin-required
    status: [patch-available, poc-public]
    affected: "PaperCut NG and MF below 25.0.13, and from 26.0.0 below 26.0.5 (the CVE record); the vendor's bulletin names no fixed 24.x release"
    fixed: "26.0.5 and 25.0.13 (vendor security bulletin of 2026-09-24); the bulletin names no emergency build as carrying the fix"
sources:
  - url: "https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/"
    publisher: "PaperCut Software (vendor security bulletin)"
    date: "2026-09-10"
    role: primary
  - url: "https://www.huntress.com/blog/papercut-actively-exploited"
    publisher: "Huntress"
    date: "2026-08-28"
    role: primary
  - url: "https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/"
    publisher: "Rapid7"
    date: "2026-08-28"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1095/"
    publisher: "CERT-FR (ANSSI) advisory CERTFR-2026-AVI-1095"
    date: "2026-08-28"
    role: corroborating
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0334"
    publisher: "NCSC-NL advisory NCSC-2026-0334"
    date: "2026-08-28"
    role: corroborating
  - url: "https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf"
    publisher: "GreyNoise"
    date: "2026-09-09"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV"
    date: "2026-08-31"
    role: corroborating
  - url: "https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/"
    publisher: "watchTowr Labs"
    date: "2026-10-09"
    role: corroborating
  - url: "https://www.papercut.com/kb/Main/security-bulletin-sep-2026/"
    publisher: "PaperCut Software (September security bulletin)"
    date: "2026-09-24"
    role: corroborating
closed_sources: []
evidence:
  - quote: "PaperCut Software security response team is investigating active exploitation of a vulnerability affecting PaperCut NG and PaperCut MF."
    publisher: "PaperCut Software"
  - quote: "PaperCut's authorization check could trust the rendered page and miss the permissions required by the component behind it."
    publisher: "Huntress"
  - quote: "By selecting either the public Error page or Exception page for display, an attacker can bypass authentication while invoking administrative components belonging to ConfigEditor or UserList."
    publisher: "Rapid7"
  - quote: "47% of the approximately 2,500 PaperCut installations Huntress tracks are running v23 or older, for which no patch is currently available."
    publisher: "Huntress"
  - quote: "PaperCut has been targeted in the past; in 2023, CVE-2023-27350 was broadly exploited in the wild by multiple threat-actor groups, including ransomware operators."
    publisher: "Rapid7"
  - quote: "Emergency Patch (Release 3) has been released by our emergency response team and supersedes Release 2. You do not need to install previous patches, this patch is an accumulation of all emergency releases. This release addresses two known regressions and adds additional hardening and mitigation against potential attack chains."
    publisher: "PaperCut Software"
  - quote: "Servers that remain publicly reachable and unpatched continue to be targeted, and post-compromise behaviour observed in the second wave has been more sophisticated than in the first days of this incident."
    publisher: "PaperCut Software"
  - quote: "These releases replace the emergency patches. If you are running an emergency patch build, move to a maintenance release. If you have not yet patched, upgrade now."
    publisher: "PaperCut Software"
  - quote: "compromise at least 440 instances of PaperCut MF/NG hosted by 395 identified victim organizations in 48 countries"
    publisher: "GreyNoise"
  - quote: "GreyNoise observed the adversary achieved domain admin against only 12 victim organizations."
    publisher: "GreyNoise"
  - quote: "Patch contains a fix for: WT-2026-0143 (Authentication Bypass)"
    publisher: "watchTowr Labs"
    source_url: "https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/"
  - quote: "Patch contains a fix for: WT-2026-0144/CVE-2026-82077 (Post-Auth RCE)"
    publisher: "watchTowr Labs"
    source_url: "https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/"
  - quote: "Tying it all together (WT-2026-0143 + WT-2026-0144/CVE-2026-82077), we can finally pop a shell against PaperCut NG 26.0.4-PO build 76508."
    publisher: "watchTowr Labs"
    source_url: "https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/"
  - quote: "If you have already upgraded to the latest release (26.0.5, 25.0.13) the issues are already addressed."
    publisher: "PaperCut Software"
    source_url: "https://www.papercut.com/kb/Main/security-bulletin-sep-2026/"
verification: multi-source
sourcing_note: >
  PaperCut's own bulletin confirms the vulnerability, the active exploitation and the two-CVE structure; the request-routing mechanism, the request chains and the
  exploitation artifacts trace to Rapid7 and Huntress, and the later bypass analysis to watchTowr.
confidence: high
references: []
deep_dive: true
deep_dive_category: web-app-rce
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Upgrade every PaperCut NG/MF Application Server, Site Server and secondary/print server to the security maintenance release for its line (26.0.5, 25.0.13 or 24.1.10), starting with any still on Emergency Patch Release 1 or 2, and note that the emergency builds do not carry the fix for CVE-2026-82077, an administrator-only Scan-to-Fax code-execution flaw that the vendor's September bulletin lists as fixed in 26.0.5 and 25.0.13 and does not list for 24.1.10; for v23 and earlier, immediately restrict the Application Server's web interface to trusted/internal IP addresses only; no patch exists for that line."
  - "Before patching or restarting an internet-facing server, preserve the server/logs directory and process tree; check server.log for the two vendor-documented error strings and for an unexplained gap or truncation, check derby.log for a Derby boot line naming an in-memory database directory ending in \"pwn\", and hunt for a Windows service named \"Remote Access Service\" running SimpleService.exe (SimpleHelp) or an unexpected AnyDesk install, as PaperCut's own published incident data names both as an observed post-compromise access method."
  - "Given GreyNoise's confirmed domain-admin escalation paths, verify no PaperCut Application Server is domain-joined with a privileged service account or hosted on a domain controller, and confirm domain controllers reachable from any PaperCut host are patched against the 2021 noPac flaws (CVE-2021-42278/CVE-2021-42287); GreyNoise reports the AI-orchestrated campaign reaching full domain admin through these paths in as little as five minutes after initial access."
updates:
  - at: "2026-09-03T05:05:00Z"
    run_id: 2026-09-03T0410Z-intel
    type: update
    summary: >
      PaperCut shipped Emergency Patch Release 3 on 1 September 2026, superseding Release 2 and fixing two
      regressions Release 2 had introduced (broken SAML login; lost legacy Microsoft SQL Server driver support for
      external card lookup). PaperCut also confirms a second, more sophisticated wave of attacks against
      still-unpatched, internet-facing servers, and separately published incident data naming a post-compromise
      chain installing a SimpleHelp remote-access service and AnyDesk for durable access.
    fields: [cves, actions, immediate_action, summary, techniques, evidence, sourcing_note, body]
  - at: "2026-09-10T05:00:00Z"
    run_id: 2026-09-10T0410Z-intel
    type: update
    summary: >
      GreyNoise documents an AI-agent-orchestrated mass-exploitation campaign against this chain beginning 31
      August 2026, using hundreds of AI agents to opportunistically compromise 440 PaperCut instances across 395
      organizations in 48 countries, reaching domain admin against 12 of them in as little as five minutes via
      LSASS credential harvesting, the 2021 noPac flaws, or a PaperCut host running on the domain controller
      itself, all finishing with a DCSync-based NTDS.DIT credential dump.
    fields: [summary, techniques, actions, sources, evidence, body]
  - at: "2026-09-29T22:55:14Z"
    run_id: 2026-09-29T2134Z-audit
    type: update
    summary: >
      PaperCut published fully tested maintenance releases 26.0.5, 25.0.13 and 24.1.10 on 10 September
      2026. They carry every fix from the three emergency patches plus further hardening, and replace
      the emergency patches as the recommended build. A server on Emergency Patch Release 3 is
      protected and can schedule the move normally; one on Release 1 or 2 should upgrade now. There is
      still no fix for v23 and earlier. PaperCut also reports that new compromises slowed considerably
      in early September while unpatched, exposed servers are still targeted. CISA added both CVEs to
      its KEV catalog on 2026-08-31, which the status fields now record.
    fields: [summary, immediate_action, cves, actions, evidence, headline, tags, sources, body]
  - at: "2026-10-10T03:46:27Z"
    run_id: 2026-10-10T0255Z-intel
    type: update
    summary: >
      watchTowr published on 2026-10-09 how the emergency patches were bypassed in turn: the 28 August emergency build could still be taken without authentication through the Setup Wizard forms, and a new administrator-only Scan-to-Fax code-execution flaw, CVE-2026-82077, is fixed only in 26.0.5 and 25.0.13, not in the emergency builds. No source names exploitation of either, though PaperCut says Emergency Patch Release 3 closes off further attack vectors it has seen exploited. Earlier statements the cited sources do not support were corrected where they stood: the 2023 precedent, the university-customer statement, the emergency-patch chronology and the detection wording.
    fields: [priority, summary, immediate_action, tags, cves, actions, sources, evidence, sourcing_note, body]
migrated_from: null
---

PaperCut has been targeted before: Rapid7 notes that in 2023 CVE-2023-27350 was broadly exploited in the wild by multiple threat-actor groups, including ransomware operators, which raises the urgency of this new zero-day ([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)). PaperCut disclosed on 27 August 2026 that it was investigating active exploitation of a new flaw in the same product line, before any CVE, patch or public technical detail existed ([watchTowr, 2026-10-09](https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/)); Rapid7 relays PaperCut's statement that information supplied by a university customer's security team and its digital forensics and incident response team enabled PaperCut to reproduce the vulnerability ([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)).

PaperCut's Application Server runs on the Apache Tapestry web framework, whose "complex direct" request format lets
a single HTTP request name one page to render and a different page's component to actually execute. PaperCut's own
authorization check validates only the page selected for rendering, not the component that runs behind it — so a
request that asks Tapestry to render the public, unauthenticated Error, Exception, or Home page while invoking the
administrative `ConfigEditor` or `UserList` component bypasses authentication entirely
([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)).
Through three such POST requests — `/app?service=direct/1/Error/ConfigEditor/quickFindForm`,
`.../ConfigEditor/$Form`, and `.../UserList/$QuickFind.$Form` — an unauthenticated attacker rewrites four external
card/ID lookup settings (`user-lookup.db-driver`, `user-lookup.db-url`, `user-lookup.id-to-username-sql`,
`user-lookup.enabled`) that normally point PaperCut at an administrator-configured external card database
([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)).
Redirected instead to an attacker-controlled JDBC target through PaperCut's bundled Apache Derby driver and its
`foreignViews` feature, the connection reaches an attacker-controlled H2 database whose inline `INIT` statement
creates a JavaScript-backed trigger; PaperCut's bundled Nashorn JavaScript engine then executes that trigger to
launch an operating-system process — full remote code execution as the PaperCut server, triggered the moment the
forged `UserList` search runs the malicious lookup
([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)).
This is a two-CVE chain: CVE-2026-81578 (CWE-306, missing authentication) is the pre-auth entry that gains write
access to the server configuration; CVE-2026-82078 (CWE-470, unsafe dynamic class loading) is the flaw that turns a
reconfigured database connection into arbitrary Java bytecode execution once that write access is held
([PaperCut Software, 2026-09-10](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).

PaperCut treats **all versions** of NG and MF as potentially affected. Huntress observed two live customer
exploitations: one on 26 August lasting under two minutes against version 25.0.10.75465, and a second on 27 August
against version 24.1.5.71847 — before Emergency Patch Release 2 extended coverage to the v24 line
([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)). In both cases the attacker ran
base64-encoded discovery commands (`whoami & ver`, and separately `whoami & ver & tasklist`) via a dropped,
OS-agnostic Java `.class` file; in the first incident it wrote its output to a temporary file and then deleted both that file and the
server's own `server.log`
([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)). Huntress's own proof-of-concept
reproduced the full chain against a stock PaperCut NG install and observed the code execution surface as an
observable `charmap.exe` process running as SYSTEM, spawned under the PaperCut Application Server's own `pc-app.exe`
process
([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)). PaperCut released an initial emergency patch for v25 and v26 on 28 August and patches for v24 later the same day, and Rapid7 says the first patch could be bypassed by using the Home page for display while the newest version of the vendor patch remediates that bypass ([Rapid7, 2026-08-28](https://www.rapid7.com/blog/post/etr-papercut-ng-mf-critical-zero-day-exploited-in-the-wild/)). PaperCut then superseded the earlier emergency patches with Emergency Patch Release 3 on 1 September 2026 and replaced all three emergency patches on 10 September with fully tested maintenance releases (see the updates below) ([PaperCut Software, 2026-09-10](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).
There is no fix for v23 and earlier; PaperCut's guidance for that line is to upgrade to a supported version ([PaperCut Software, 2026-09-10](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)), and
Huntress estimates 47% of the roughly 2,500 PaperCut installations it tracks still run v23 or older
([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)).

Detection, telemetry class first: alert on any child process spawned from `pc-app.exe` or the PaperCut Application
Server's Java process, the lineage under which the observed exploitation ran its discovery commands. Web-access logs for the PaperCut Application Server should
be checked for POST requests to `/app?service=direct/*/{Error,Exception,Home}/ConfigEditor/*` or
`.../UserList/$QuickFind.$Form` from unauthenticated or external sources — this URL shape is not a pattern ordinary
PaperCut administration produces. Two log artifacts are near-unique indicators: a `server.log` line reading
`DB URL: jdbc:derby:memory:pwn`, and a corresponding `derby.log` entry recording Derby booting an in-memory database
directory whose name ends in the literal string `pwn`
([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)). PaperCut stresses that the absence of its file artifacts does not rule out compromise because the attacker may clean them up ([PaperCut Software, 2026-09-10](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)), and Huntress observed the payload deleting the server's own `server.log` ([Huntress, 2026-08-28](https://www.huntress.com/blog/papercut-actively-exploited)).
The later authentication bypass that watchTowr documents reaches the Setup Wizard pages through the `Home` page, so requests whose `service` parameter routes through `Home` to a setup page such as `SetupAdmin` on a server whose setup is long complete are the matching pattern ([watchTowr, 2026-10-09](https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/)).
**Triage:** an unexpectedly truncated, gapped, or missing `server.log` on a PaperCut Application Server is worth
investigating even where no other artifact survives, since Huntress saw the payload delete that log. **Defender takeaway:** any PaperCut NG/MF
Application Server that has ever been reachable from the public internet should be assumed targeted; upgrade it to
the maintenance release for its line immediately, and where v23 or earlier cannot yet be replaced, remove public exposure
entirely rather than relying on detection alone.

## Update — 2026-09-03T05:05:00Z

PaperCut's Emergency Patch Release 3, published 1 September 2026, supersedes Release 2 and is cumulative — customers
do not need to install the earlier releases first
([PaperCut Software, 2026-09-02](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).
Release 3 fixes two regressions Release 2 had itself introduced — broken SAML login flows, and lost support for
legacy Microsoft SQL Server drivers used for external card lookup — and adds further, undisclosed hardening against
the exploitation chain
([PaperCut Software, 2026-09-02](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).
PaperCut also confirms a second wave of attacks against servers that remain unpatched and internet-facing, whose
post-compromise behaviour "has been more sophisticated than in the first days of this incident"
([PaperCut Software, 2026-09-02](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).
The vendor's own incident data, published 30 August as additional indicators of compromise, names a concrete
follow-on chain from the original intrusion: after initial discovery commands, a PowerShell-delivered download
installs a Windows service literally named "Remote Access Service" running SimpleService.exe — a SimpleHelp
remote-access agent — as LocalSystem with auto-start, followed by a further download of AnyDesk; the bulletin does
not state whether this specific chain recurred in the second wave or belongs only to the earlier intrusions it was
published alongside
([PaperCut Software, 2026-09-02](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).
Mobility Print and Print Deploy server components are unaffected; Site Servers and secondary/print servers do need
the same update as the primary Application Server
([PaperCut Software, 2026-09-02](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).

## Update — 2026-09-10T05:00:00Z

GreyNoise's Global Observation Grid documents an AI-agent-orchestrated exploitation campaign against this chain
beginning 31 August 2026, run by a likely Russian-speaking operator already tracked since July 2026 for attacks on
Palo Alto, Ubiquiti, Citrix, SonicWall and Proxmox VE targets
([GreyNoise, 2026-09-09](https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf)). The
operator built and tested both CVEs' exploits in a self-hosted PaperCut/Active Directory lab, sourced target lists
via the Netlas.io scanning service, then deployed hundreds of AI agents — built on OpenAI's Codex harness paired
with a DeepSeek model — to opportunistically "compromise at least 440 instances of PaperCut MF/NG hosted by 395
identified victim organizations in 48 countries"
([GreyNoise, 2026-09-09](https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf)). GreyNoise
reports the adversary "went from an empty workspace to first achieving RCE against a real victim in just under
four hours, first domain admin in an additional two hours, and once the full campaign launched, compromised at
least 11 organizations in 26 seconds"
([GreyNoise, 2026-09-09](https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf)), with one
US high school reaching full domain admin in seven minutes from initial access. Domain admin was ultimately reached
against only twelve of the 395 compromised organizations — "GreyNoise observed the adversary achieved domain admin
against only 12 victim organizations"
([GreyNoise, 2026-09-09](https://www.greynoise.io/blog/ai-orchestrated-campaign-against-papercut-ng-mf)) — via three
paths: LSASS credential harvesting for pass-the-hash against the domain controller when the PaperCut host was
domain-joined; the 2021 noPac flaws (CVE-2021-42278/CVE-2021-42287) where those remained unpatched; or directly
adding a new account to Domain Admins when the PaperCut host itself ran on the domain controller or under a
domain-admin service account. All three paths finished with a DCSync-based full NTDS.DIT credential dump; Cloudflare's
WAF defeated the adversary against at least one targeted instance. This delta is reported by GreyNoise alone; a
second independent source had not corroborated it as of this update.

## Update — 2026-09-29T22:55:14Z

PaperCut published security maintenance releases 26.0.5, 25.0.13 and 24.1.10 for NG and MF on 10 September 2026. Unlike the emergency patches, they went through the vendor's full release testing, carry new version numbers and release notes, and address all the CVEs in the advisory with the same protection as the emergency patches plus additional hardening. PaperCut's instruction is plain: "These releases replace the emergency patches. If you are running an emergency patch build, move to a maintenance release. If you have not yet patched, upgrade now." A server already on Emergency Patch Release 3 is protected against both CVEs and can schedule the upgrade through normal change control, while one still on Release 1 or 2 should move now. Site Servers and secondary/print servers should be updated to a patched version, not just the primary Application Server ([PaperCut Software, 2026-09-10](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).

Nothing changes for v23 and earlier: there is no emergency patch or maintenance release for that line, and the only route to a fixed build is an upgrade to a supported line (24, 25 or 26), with web access to the Application Server restricted to trusted addresses until then. PaperCut also reports that new compromises have slowed considerably and that most customers now have the Application Server behind a firewall or on a patched build, but that publicly reachable, unpatched servers are still being targeted ([PaperCut Software, 2026-09-10](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)). For an estate that patched in the first week, the task is to move each server from its emergency build to the maintenance release and confirm the version on every Site Server and secondary server, not only on the primary. CISA added both CVEs to its Known Exploited Vulnerabilities catalog on 2026-08-31 ([CISA KEV](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

## Update — 2026-10-10T03:46:27Z

watchTowr Labs published a write-up on 2026-10-09 that follows the emergency patches build by build ([watchTowr, 2026-10-09](https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/)). Its timeline: the patch released on 28 August (26.0.4-PO build 76508) fixed two bypasses watchTowr had reported; watchTowr then bypassed the fix for the authentication bypass again (tracked internally as WT-2026-0143, no CVE assigned) and found a new post-authentication code-execution flaw in Scan-to-Fax (WT-2026-0144, now CVE-2026-82077), which together gave a full unauthenticated chain against build 76508; the patch released on 1 September (build 76530) fixes WT-2026-0143, and 26.0.5, released on 10 September, fixes CVE-2026-82077 ([watchTowr, 2026-10-09](https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/)). The authentication bypass abuses the Setup Wizard forms, which the earlier patches had ignored: every stage can be reached through the `Home` page even after setup is complete, and watchTowr shows it modifies the administrator password ([watchTowr, 2026-10-09](https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/)). watchTowr also publishes a Detection Artefact Generator that tests a server's exposure to the authentication bypasses but does not run the full chain ([watchTowr, 2026-10-09](https://labs.watchtowr.com/death-by-a-thousand-papercuts-papercut-pre-auth-rce-chain-and-patch-bypasses-wt-2026-0141-0144-cve-2026-82077-cve-2026-82078-cve-2026-81578/)).

PaperCut's September security bulletin lists CVE-2026-82077 as a code-execution flaw in the Scan-to-Fax component that needs an authenticated administrator, rated CVSS 4.0 7.3, fixed in 26.0.5 and 25.0.13, and says servers already on the latest release are covered ([PaperCut Software, 2026-09-24](https://www.papercut.com/kb/Main/security-bulletin-sep-2026/)); it names no 24.x release and no emergency build. The unauthenticated chain watchTowr describes is closed by the 1 September patch, but an administrator-level foothold still reaches code execution through Scan-to-Fax until the maintenance release is installed. No source names exploitation of CVE-2026-82077 or of the Setup Wizard bypass. PaperCut says Emergency Patch Release 3 closes off additional attack vectors it has observed being exploited in the wild, without naming them ([PaperCut Software, 2026-09-10](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/)).
