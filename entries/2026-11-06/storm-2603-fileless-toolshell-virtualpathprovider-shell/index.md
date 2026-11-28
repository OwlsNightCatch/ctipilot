---
schema: 1
kind: threat
title: "Kaspersky reconstructs an intrusion through SharePoint ToolShell, attributed to Storm-2603 with moderate confidence, whose implant lived only inside w3wp.exe: an ASP.NET VirtualPathProvider memory shell with a suo5 tunnel, then Velociraptor, several tunnelling mechanisms and Warlock's AV killer"
headline: "Storm-2603-linked SharePoint intrusion: memory-only VirtualPathProvider shell in w3wp.exe, then Velociraptor and tunnels"
summary: >
  Kaspersky's retrospective of a December intrusion at a customer's on-premises SharePoint server, which it attributes to Storm-2603 with moderate confidence, shows a ToolShell exploit
  that left no file on disk: a C# memory shell registered as an ASP.NET VirtualPathProvider inside the IIS worker process w3wp.exe, dormant until a specific User-Agent arrived, with an
  suo5 proxy that turned the SharePoint host into a pivot. The actor then installed an outdated Velociraptor and several tunnelling mechanisms so access outlived the worker process, and
  Kaspersky's endpoint product blocked the Warlock encryption attempt.
discovered_at: "2026-11-06T03:44:00Z"
updated_at: null
event_date: "2026-11-05"
run_id: 2026-11-06T0255Z-intel
priority: notable
immediate_action: null
tags: [ransomware, vulnerabilities]
regions: [global]
sectors: []
entities: ["actor:warlock-storm-2603", "tool:velociraptor", "tool:suo5", "product:microsoft-sharepoint", "product:microsoft-iis"]
techniques: [T1190, T1505.003, T1620, T1553, T1090, T1572, T1134.001, T1136.001, T1218.007, T1105, T1219.001, T1219.002, T1574.001, T1685, T1486]
affected_products: ["Microsoft SharePoint Server", "Microsoft IIS"]
cves: []
sources:
  - url: "https://securelist.com/storm-2603-fileless-toolshell-attack/121467/"
    publisher: "Kaspersky (Securelist)"
    date: "2026-11-05"
    role: primary
closed_sources: []
evidence:
  - quote: "This activity involved the attacker using the IIS worker process as an in-memory bridge to the customer’s infrastructure, keeping the access and control layer entirely within w3wp.exe without writing anything to disk."
    publisher: "Kaspersky (Securelist)"
    source_url: "https://securelist.com/storm-2603-fileless-toolshell-attack/121467/"
  - quote: "Consequently, the presence of positive events 25 and 47 combined with the absence of the expected events 17, 18, 19, and 21 for the same path forms a reliable detection pattern"
    publisher: "Kaspersky (Securelist)"
    source_url: "https://securelist.com/storm-2603-fileless-toolshell-attack/121467/"
  - quote: "this allows us to attribute this case to Storm-2603 with moderate confidence."
    publisher: "Kaspersky (Securelist)"
    source_url: "https://securelist.com/storm-2603-fileless-toolshell-attack/121467/"
verification: single-source
sourcing_note: >
  Kaspersky's incident-response team is the first-hand source for the intrusion and the only one for its details; the attribution to Storm-2603 is Kaspersky's own, at moderate confidence, resting on ToolShell exploitation, post-exploitation overlap with earlier reporting and a Warlock-linked component. The article gives the month of the intrusion without a version table for SharePoint.
confidence: medium
references:
  - 2026-10-03/warlock-longlegs-sharepoint-machinekey-sysvol-ransomware
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

Kaspersky's retrospective analysis of a December intrusion at a customer's on-premises SharePoint server found activity consistent with Storm-2603, with the access and control layer held entirely inside the IIS worker process w3wp.exe and nothing written to disk ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)). On December 20 a single request to a SharePoint administrative endpoint tied to the ToolPane component fingerprinted the host for ToolShell (CVE-2025-53770); the full exploit chain ran on December 24 against the same endpoint, and the gap kept the probe from being correlated with it ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)). The payload was loaded into the ASP.NET runtime and lost when the application pool recycled or IIS restarted ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)).

The memory shell registers a custom VirtualPathProvider through a non-public method of the ASP.NET HostingEnvironment class, subverts trust controls so that the registration works even in a precompiled application, intercepts requests at the GetCacheKey() hook and stays dormant unless a specific User-Agent header arrives ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)). It speaks a custom XOR-obfuscated binary protocol, and the open-source suo5 tool proxies traffic so connections from the command server reach arbitrary hosts inside the network through the SharePoint server ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)). It reaches SYSTEM by named-pipe token impersonation adapted from EfsPotato and creates administrative accounts through native SAM RPC calls ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)).

Shortly after the injection w3wp.exe started msiexec.exe to install a remote MSI that was Velociraptor 0.73.4.0, vulnerable to CVE-2025-6264, which the actor used for persistence, discovery, data collection and payload execution and to deploy Zoho Assist unattended access, a VS Code CLI tunnel, Cloudflare Tunnel and a reverse proxy, so access no longer depended on the IIS process ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)). The actor then uploaded a vulnerable driver that is used to terminate EDR products and sideloaded a DLL that Kaspersky identified as Warlock ransomware's AV killer, possibly meant to use that driver; Kaspersky's endpoint product blocked the ransomware process ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)).

**Exposure:** an internet-reachable on-premises SharePoint Server on which ToolShell (CVE-2025-53770 and CVE-2025-53771) is exploitable ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)).

**Detection:** in CLR loader telemetry, a dynamically compiled App_Web_toolpane assembly and a Microsoft.GeneratedCode assembly loading in the same application domain after a ToolPane request; in the IIS-Configuration ETW provider, events 25 and 47 for a path without the file-change-monitor events 17, 18, 19 and 21 that a real file produces, checked against an allow-list of legitimate VirtualPathProvider implementations; and memory inspection of w3wp.exe ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)).

**Triage:** App_Web_* assemblies come from ordinary ASP.NET page compilation and Microsoft.GeneratedCode from legitimate XmlSerializer use, so neither is a signal alone; the signal is the pair in one application domain right after a ToolPane request, and any VirtualPathProvider that is not on the application's inventory ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)). The December 20 probe came from infrastructure associated with ONYPHE, an attack-surface discovery platform whose vulnerability checks use non-intrusive probes, so a probe alone looks like a benign scanner; Kaspersky's retrospective analysis established the probe as the initial phase of the intrusion that followed on the same endpoint ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)).

**Defender takeaway:** on a SharePoint host that shows a code-execution exploit, contain the host, hunt the persistence that was installed afterwards, and rotate credentials and the exposed ASP.NET MachineKey; removing the initial shell or known indicators is not enough ([Kaspersky, 2026-11-05](https://securelist.com/storm-2603-fileless-toolshell-attack/121467/)). Hunt for VirtualPathProvider implants with the ETW pattern above on SharePoint farms that were exposed to ToolShell.
