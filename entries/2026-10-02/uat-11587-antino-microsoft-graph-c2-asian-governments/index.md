---
schema: 1
kind: threat
title: "UAT-11587: a China-nexus cluster spear-phishes Asian government and policy bodies with Antino, a Rust backdoor whose only command channel is Microsoft 365 through Microsoft Graph"
headline: "Talos: Antino's traffic ends only at Microsoft's Graph and login endpoints, so network telemetry shows only Microsoft"
summary: >
  Cisco Talos describes UAT-11587, a cluster it assesses with high confidence as China-nexus, active since September
  2025 against government, justice, e-government and policy organizations in eight Asian countries, with about 350
  compromised endpoints. Its Antino backdoor takes commands from an Outlook folder and uses OneDrive for heartbeats and
  file transfer through an Entra application, and the lures pass SPF but fail DMARC against a
  p=none domain.
discovered_at: "2026-10-02T04:50:00Z"
updated_at: null
event_date: "2026-09-30"
run_id: 2026-10-02T0404Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, phishing, cloud, china-nexus]
regions: [apac]
sectors: [public-sector]
entities: ["actor:uat-11587", "malware:antino", "actor:jewelbug"]
techniques: [T1566.002, T1684.002, T1204.002, T1218.005, T1059.007, T1059.001, T1027, T1140, T1620, T1574.001, T1102.002, T1547.001, T1105, T1041, T1583.006]
affected_products: []
cves: []
sources:
  - url: "https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/"
    publisher: "Cisco Talos"
    date: "2026-09-30"
    role: primary
closed_sources: []
evidence:
  - quote: "Antino communicates exclusively through Microsoft 365, using the Microsoft Graph API to interact with Outlook and OneDrive as dead-drop C2 channels."
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/"
  - quote: "In the reviewed message, the displayed domain used a non-enforcing p=none policy, which requested monitoring rather than quarantine or rejection."
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/"
  - quote: "Talos could not independently verify a connection between the espionage campaign and Jewelbug’s financially motivated activity."
    publisher: "Cisco Talos"
    source_url: "https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/"
verification: single-source
sourcing_note: >
  One analyst's research (Talos holds the telemetry); the China-nexus attribution is Talos's high-confidence
  assessment from decoy metadata, a China-focused Rust mirror in the build paths and lure selection, and its link to
  Symantec's Jewelbug reporting is an overlap Talos could not verify, not an attribution. No European or Swiss victim is
  named.
confidence: high
references:
  - 2026-08-16/jewelbug-pdf-viewer-extension-native-messaging-webmail-hole
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Cisco Talos tracks UAT-11587, first seen in September 2025, with at least 10 confirmed and five probable affected institutional environments and about 350 compromised endpoints across eight countries (Taiwan, India, the Philippines, Cambodia, Pakistan, Thailand, Myanmar and Syria, listed at moderate-to-high confidence); the targets include defense, central administration, justice and law enforcement, government IT and e-government services, legislatures and policy research bodies ([Cisco Talos, 2026-09-30](https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/)). Talos assesses China-nexus with high confidence and intelligence gathering with moderate confidence, and notes overlaps with the Antino activity Symantec attributes to Jewelbug without being able to verify a link to Jewelbug's financially motivated activity ([Cisco Talos, 2026-09-30](https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/)).

Delivery is spear-phishing in which the envelope sender is an attacker-controlled domain relayed through Migadu while the visible From header shows the impersonated organization, so SPF passes for the envelope domain, DMARC alignment fails, and a p=none policy on the impersonated domain lets the message reach the inbox; the mail body reproduces Gmail's attachment widget as images linking to a Cloudflare Pages address ([Cisco Talos, 2026-09-30](https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/)). The five-stage chain starts with an HTA stager run by `mshta.exe`, then a JScript downloader and decryptor that pulls encrypted resources from Cloudflare R2 or CloudFront, then .NET deserialization gadgets that load a downloader assembly inside `mshta.exe`, which writes a decoy and a three-file bundle and launches the Microsoft-signed Windows ADK binary `GatherOsState.exe`; that binary sideloads an unexpected DLL, which is Antino ([Cisco Talos, 2026-09-30](https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/)).

Antino is a Rust backdoor whose second-generation build authenticates to Microsoft Graph with the OAuth 2.0 client-credentials flow of an Entra application, polls an Outlook folder every 10 seconds for command emails, sends a OneDrive heartbeat every minute and uses OneDrive folders for tool staging and exfiltration, so outbound traffic ends only at `graph.microsoft.com` and `login.microsoftonline.com` ([Cisco Talos, 2026-09-30](https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/)). Its commands run `cmd.exe` and PowerShell, list, upload and download files, load shellcode in memory and add a registry Run value; execution and persistence abuse the Windows Scripted Diagnostics workflow, in which `sdiagnhost.exe` runs an attacker-written PowerShell script that writes the HKCU Run value ([Cisco Talos, 2026-09-30](https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/)).

**Exposure:** mail recipients whose organization's domain publishes DMARC p=none (the policy that let the reviewed message through), and endpoints where `mshta.exe` and Windows Script Host can run; Talos names no European victim.

**Detection:** in process-creation telemetry, `mshta.exe` or `wscript.exe` loading the .NET runtime and assemblies into the script host itself or writing a three-file bundle to a staging directory, `GatherOsState.exe` loading an unexpected DLL from its own folder, and `sdiagnhost.exe -Embedding` running PowerShell that sets an HKCU Run value; in network telemetry (the Entra application, mailbox and OneDrive belong to the threat actor, so the victim tenant's audit logs will not show them), connections to `graph.microsoft.com` from processes that are not Microsoft 365 clients; in mail flow, DMARC-failing mail from p=none senders that was delivered, and protocol-relative links to `pages.dev` addresses ([Cisco Talos, 2026-09-30](https://blog.talosintelligence.com/china-nexus-uat-11587-targets-government-and-policy-organizations-across-asia-with-antino-backdoor/)).

**Triage:** Microsoft Graph traffic and signed Windows ADK binaries are both normal; the signal is the combination of `GatherOsState.exe` running from a staging directory outside the Windows ADK install, beside an unexpected DLL and that process then holding Graph connections.

**Defender takeaway:** network controls cannot separate this command channel from ordinary Microsoft 365 traffic, so hunt on the initiating process, and check whether your own domains publish DMARC p=none, the setting the spoofed lures relied on.
