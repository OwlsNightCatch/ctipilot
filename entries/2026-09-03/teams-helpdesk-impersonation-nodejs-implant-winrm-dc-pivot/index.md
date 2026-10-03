---
schema: 1
kind: threat
title: "A Teams helpdesk-impersonation campaign installs a Node.js implant (Microsoft detection name: EtherRatz) via a silent MSI, then pivots over WinRM straight to domain controllers and certificate authorities"
headline: "The intrusion's most consequential step is a remote-management connection from a non-administrative process to systems that should never see one"
summary: >
  Microsoft Threat Intelligence documents a human-operated intrusion campaign that abuses Microsoft Teams external
  collaboration to impersonate IT or helpdesk staff, talks victims into granting an interactive remote session, then
  silently installs a portable-Node.js-hosted implant (Defender detection name EtherRatz) via MSI. Post-compromise
  tasking performs Active Directory reconnaissance and pivots laterally over WinRM to a large set of domain-joined
  systems, explicitly including domain controllers and certificate authorities — the shape Microsoft frames as
  preceding large-scale data theft, extortion or ransomware deployment.
discovered_at: "2026-09-03T05:21:30Z"
updated_at: null
event_date: "2026-09-02"
run_id: 2026-09-03T0410Z-intel
priority: high
immediate_action: null
tags: [phishing, identity, organized-crime]
regions: [global]
sectors: [public-sector]
entities:
  - malware:etherrat
  - malware:synkloader
techniques: [T1566.003, T1059.001, T1059.007, T1218.007, T1218.011, T1036, T1497.001, T1082, T1016, T1087.002, T1018, T1518.001, T1113, T1071.001, T1105, T1021.006]
affected_products: ["Microsoft Teams", "Windows Remote Management"]
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-09-02"
    role: primary
closed_sources: []
evidence:
  - quote: "Microsoft Threat Intelligence has observed a human-operated intrusion campaign that abuses Microsoft Teams external collaboration to impersonate IT or helpdesk personnel and socially engineer users into granting an interactive remote session."
    publisher: "Microsoft Threat Intelligence"
  - quote: "The analyzed implants also contained dormant logic capable of querying an Ethereum smart contract for an updated C2 URL. This functionality was disabled in the recovered builds, which instead used a hard-coded fallback server."
    publisher: "Microsoft Threat Intelligence"
  - quote: "operator-issued tasking executed through the Node.js backdoor initiated internal remote-management connections over WinRM on TCP port 5985 to a large set of domain-joined systems"
    publisher: "Microsoft Threat Intelligence"
verification: single-source
sourcing_note: >
  Single fresh source (Microsoft) for this 2 September 2026 campaign report; no independent write-up of this
  specific publication was located as of 2026-09-03. The implant's Node.js-plus-dormant-Ethereum-smart-contract-C2 mechanism
  overlaps the malware family already tracked as EtherRAT (2026-08-23 entry, sourced from Red Canary), but
  Microsoft's own article never uses that name — its Defender detection signatures read Trojan:JS/EtherRatz.A!MTB
  and .B!MTB (EtherRatz, not EtherRAT). Treated as an overlap with the tracked family on the strength of the shared
  Node.js/Ethereum-smart-contract mechanism, not as Microsoft confirming identity with it. Microsoft's own detection
  table additionally names Trojan:JS/SynkLoader.SA and Trojan:Win32/SynkLoader.SA for the MSI/loader stage this
  entry describes — the same detection family already tracked from a near-identical Teams helpdesk-impersonation
  chain (2026-08-24 entry, sourced from Expel). Treated as an overlap on the loader stage specifically, not as
  evidence the two campaigns share every stage.
confidence: medium
references:
  - 2026-08-23/blockchain-dead-drop-c2-commodity-graphspy
  - 2026-08-24/synkloader-teams-helpdesk-impersonation-six-module-loader
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Restrict inbound Microsoft Teams external collaboration to a vetted allow-list of domains, or require explicit user opt-in per external organisation, given the campaign's initial-access channel is unsolicited Teams chats/calls impersonating internal IT support."
  - "Restrict WinRM (TCP 5985) inbound to domain controllers and certificate authorities to a small, known set of administrative source hosts — the campaign's lateral-movement step specifically relies on WinRM being reachable from ordinary workstations to these systems."
updates: []
migrated_from: null
---

Microsoft Threat Intelligence documents a human-operated intrusion campaign that abuses Microsoft Teams external
collaboration to impersonate IT or helpdesk personnel — pretexts include "Microsoft Security Update," "Spam Filter
Update" and "Account Verification," sometimes reinforced with a phone call — and socially engineers the victim into
approving a "request control" prompt during a Teams screen-share, or into opening Quick Assist and reading back a
connection code
([Microsoft Threat Intelligence, 2026-09-02](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)).
Once remote control is granted through the legitimate support tool, the operator uses PowerShell inside that same
session to silently pull a malicious MSI — disguised with update-themed names and hosted on a widely used
cloud-storage platform to blend with legitimate traffic — and installs it via `msiexec /qn`. The MSI stages a
portable Node.js runtime plus a separately encrypted implant file; a deferred MSI custom action launches hidden
bootstrap code that decrypts the implant and hands it to Node.js via standard input or a temporary script file,
evading controls keyed on unsigned executables or conventional script extensions
([Microsoft Threat Intelligence, 2026-09-02](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)).
Per-user persistence uses an `HKCU Run` value or Startup-folder shortcut, both named "EdgeUpdate." The implant polls
its command-and-control over randomised HTTPS long-polling and executes returned JavaScript dynamically, performing
sandbox and antivirus discovery, periodic screenshot capture, and ADSI-based Active Directory sweeps — enumerating
domain-joined servers and harvesting user object and description-attribute content, with randomised sleep jitter to
stay quiet. A dormant capability in the analysed implants queries an Ethereum smart contract for an updated
command-and-control URL — disabled in the recovered builds, which fall back to a hard-coded server instead
([Microsoft Threat Intelligence, 2026-09-02](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)).
Microsoft's own Defender detection names for the implant are Trojan:JS/EtherRatz.A!MTB and Trojan:JS/EtherRatz.B!MTB
— its article does not otherwise name the campaign or the implant. The same detection table names the MSI/loader
stage Trojan:JS/SynkLoader.SA and Trojan:Win32/SynkLoader.SA, the family behind a near-identical Teams
helpdesk-impersonation chain documented separately on 2026-08-24 (Expel) — a detection-level overlap on the loader
stage, distinct from the Node.js implant this entry otherwise describes.

The intrusion's most consequential step is lateral movement: operator-issued tasking through the Node.js implant
initiates internal WinRM connections on TCP 5985 to a large set of domain-joined systems, explicitly including
domain controllers and certificate authorities — activity Microsoft frames as the hallmark of an intrusion that
precedes large-scale data theft, extortion or ransomware deployment
([Microsoft Threat Intelligence, 2026-09-02](https://www.microsoft.com/en-us/security/blog/2026/09/02/impersonating-it-support-threat-actors-turn-remote-session-into-enterprise-wide-access/)).
The Node.js/dormant-Ethereum-smart-contract-C2 mechanism overlaps the malware family already tracked as
EtherRAT from Red Canary's August monthly round-up, though Microsoft's own reporting never uses that name for this
implant — the connection is a mechanistic overlap this entry records, not an identity Microsoft itself asserts.

**Triage:** an external Microsoft Teams chat or call that leads to a screen-share "request control" approval or a
Quick Assist connection-code exchange, particularly one impersonating internal IT, is the point at which this
campaign is still stoppable — legitimate internal helpdesk workflows do not typically originate from an external
tenant. Downstream, a WinRM connection to a domain controller or certificate authority originating from a
non-administrative PowerShell process, or a `node.exe` process reading a script staged under a user's AppData
directory and launched by `wscript.exe`, are both behaviours normal administrative tooling does not produce.
**Defender takeaway:** treat unsolicited external Teams contact claiming to be IT support as a phishing vector
requiring the same scrutiny as email, and restrict which hosts may open a WinRM session to domain controllers and
certificate authorities regardless of the initiating process's apparent legitimacy.
