---
schema: 1
kind: threat
title: "AOMEI Backupper and AnyViewer update files tampered with for five to ten minutes at a time between April and July 2026 to push the CROSSROAD downloader and the SHINYROAD backdoor, with Switzerland among 11 countries GTIG names"
headline: "GTIG: AOMEI update files were altered for minutes at a time to push a backdoor; Switzerland among victim countries"
summary: >
  Google's GTIG and ManageEngine's METAL report that a cluster tracked as UNC7017 altered two configuration files on AOMEI's update servers for five to ten minutes at a time between April and July 2026, so any Backupper or AnyViewer client that polled during a window downloaded and ran the CROSSROAD downloader, which installed the SHINYROAD backdoor beside a signed Radmin binary. No software flaw is involved, GTIG names Switzerland among 11 victim countries, and the vendor's server-side repair does not clean a host that already ran the downloader, so installations need an endpoint hunt covering April to July 2026.
discovered_at: "2026-10-17T03:30:00Z"
updated_at: null
event_date: "2026-10-16"
run_id: 2026-10-17T0256Z-intel
priority: high
immediate_action: null
tags: [supply-chain]
regions: [global, switzerland]
sectors: [technology, telco, education]
entities: ["actor:unc7017", "malware:crossroad", "malware:shinyroad", "incident:aomei-backupper-ephemeral-update-tampering-2026", "product:aomei-backupper", "product:aomei-anyviewer"]
techniques: [T1195.002, T1053.005, T1574.001, T1559.001, T1614, T1059.001, T1059.006, T1518.001, T1036.005, T1480, T1497.001, T1070.004, T1027, T1027.013, T1105, T1219, T1219.002, T1571, T1187, T1140, T1564.004, T1573.001, T1001.001, T1016, T1082, T1033, T1583.001, T1583.006, T1608.001]
affected_products: ["AOMEI Backupper", "AOMEI AnyViewer"]
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering"
    publisher: "Google Threat Intelligence Group / Mandiant"
    date: "2026-10-16"
    role: primary
  - url: "https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html"
    publisher: "ManageEngine Threat Analysis Lab (METAL)"
    date: "2026-10-16"
    role: corroborating
  - url: "https://www.ubackup.com/changelog.html"
    publisher: "AOMEI Technology"
    date: "2026-10-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Each tampering window remained active for only five to ten minutes before reverting to authentic versions."
    publisher: "Google Threat Intelligence Group / Mandiant"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering"
  - quote: "impacted organizations spanned diverse sectors, including IT services, telecommunications, higher education and related entities in Australia, Brazil, India, Pakistan, Portugal, Singapore, South Africa, Spain, Switzerland, Türkiye, and the United States."
    publisher: "Google Threat Intelligence Group / Mandiant"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering"
  - quote: "Organizations running AOMEI software cannot assume they are protected solely because the vendor took corrective server-side action."
    publisher: "Google Threat Intelligence Group / Mandiant"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering"
  - quote: "Nothing in this attack exploited a software defect. There was no CVE, no memory corruption, and no unpatched component."
    publisher: "ManageEngine Threat Analysis Lab (METAL)"
    source_url: "https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html"
  - quote: "As of publication, we have not independently verified that the compromise has been contained."
    publisher: "ManageEngine Threat Analysis Lab (METAL)"
    source_url: "https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html"
verification: multi-source
sourcing_note: >
  GTIG and METAL are independent first-hand observers: METAL's EDR recorded the activity on 28 May and GTIG confirmed further windows from its own telemetry. The victim list rests on GTIG's telemetry and gives no totals, and METAL has not independently verified that the vendor contained the compromise.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Inventory every Windows host that runs AOMEI Backupper or AnyViewer and check each for scheduled tasks named RadminComponentRuntime or NitroRuntime, a Radmin directory under the user's local application data and cached update files in the install tree's Tmphtml folder, searching proxy and firewall logs back to April 2026; isolate any host that matches and keep the cached files before any cleanup."
updates: []
migrated_from: null
---

GTIG and Mandiant report that a cluster they track as UNC7017 repeatedly altered two configuration files on AOMEI Technology's update servers between April and July 2026, each time for five to ten minutes before restoring the genuine content; GTIG confirmed three windows and says more probably went unseen ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)). ManageEngine's Threat Analysis Lab (METAL) writes "There was no CVE, no memory corruption, and no unpatched component." ([METAL, 2026-10-16](https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html)).

The client polls down_html.ini (update archive address and MD5 checksum) and Notifycfg.ini (what to display and run); during a window the actor pointed the first at an attacker-controlled ZIP with a matching checksum and padded the second with more than 35,000 lines of dummy sections, so the client started the unpacked downloader from its html directory, and GTIG describes the same flow for AnyViewer ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)). METAL's EDR recorded the chain on Backupper 8.3.0 ([METAL, 2026-10-16](https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html)).

The downloader, CROSSROAD, stops in some branches when the host geolocates to China ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)) and, METAL adds, when specific endpoint security agents are present ([METAL, 2026-10-16](https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html)). It registers a scheduled task that runs a signed Radmin binary every three hours; that binary loads an attacker-built DLL by search-order hijacking, which registers an in-process COM server running the SHINYROAD backdoor as encrypted PocketPy bytecode ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)). On some hosts GTIG later saw the Adaptix C2 agent, disguised as Nitro PDF tooling and started by hidden PowerShell through a second scheduled task ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)). The 20 July window also pointed a popup at a remote WebDAV path through an invisible window, which can leak the user's NetNTLMv2 response ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)).

GTIG's telemetry shows affected IT-services, telecommunications and higher-education organizations in 11 countries including Switzerland and calls the targeting opportunistic; AOMEI told Mandiant on 2026-07-29 that it had taken corrective action ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)). AOMEI's Backupper release notes through 8.5.0 list no change to update verification as of 2026-10-17 ([AOMEI Technology, 2026-10-09](https://www.ubackup.com/changelog.html)).

**Exposure:** Windows hosts running AOMEI Backupper or AnyViewer that polled for updates during an unseen window between April and July 2026; server-side repair does not clean a host that already ran the downloader ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)).

**Detection:** in process telemetry, an executable written into the Tmphtml or html folders and started by the notification process, and a signed Radmin binary loading an unexpected DLL ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)); METAL adds dllhost.exe hosting a COM component registered from a non-standard path ([METAL, 2026-10-16](https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html)). Also scheduled tasks named RadminComponentRuntime or NitroRuntime, and outbound SMB (TCP 445) and WebDAV to external addresses; hunt the whole April to July span and preserve the cached update files in the Tmphtml folder ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)).

**Triage:** do not validate an alert by fetching AOMEI's update address now: the files revert within minutes and the genuine content served then has led analysts to dismiss real detections; the Nitro PDF camouflage can make alerts read as isolated user downloads, so trace each one's parent process back to the updater ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)). Radmin is legitimate software, so provenance discriminates: METAL's EDR recorded the updater's unsigned child process installing it ([METAL, 2026-10-16](https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html)).

**Defender takeaway:** hunt every Windows host that runs AOMEI Backupper or AnyViewer for these artifacts even though AOMEI says its servers are repaired, treat a match as a compromised host, and block outbound SMB and WebDAV to external addresses, which GTIG advises against NTLM credential coercion ([GTIG, 2026-10-16](https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering)).
