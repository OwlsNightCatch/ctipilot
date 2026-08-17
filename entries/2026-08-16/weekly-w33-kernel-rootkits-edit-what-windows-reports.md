---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "Two espionage toolsets shipped kernel-mode rootkits in the same week whose job is to edit what Windows reports to the defender's own tools — and one of them arrived on a zero-day that was patched on Tuesday"
headline: "Lazarus and Mustang Panda both went below the sensor in W33 — one via an exploited AFD.sys zero-day, one via a 2013 signing certificate"
summary: >
  Two unrelated state-nexus espionage disclosures inside 2026-W33 deploy kernel-mode drivers with the same
  objective: not to evade a detection rule, but to change the answers the operating system gives the tools
  that ask it. Check Point attributed an exploited Windows AFD.sys zero-day, CVE-2026-68820, to a Lazarus
  intrusion that used it to load FudModule v3.1 — a rootkit whose shared component set is a telemetry
  teardown suite covering process, thread and image notify callbacks, object and registry callbacks,
  minifilter removal by altitude band, and termination of the NT Kernel Logger. Microsoft patched it on
  11 August and CISA catalogued it the same day; Check Point records successful targeting in Western Europe
  including France and Germany, and one compromised French organisation being reused to phish others.
  Days later Kaspersky documented a CoolClient variant attributed to Mustang Panda installing a kernel
  driver that hooks Nsiproxy so that C2 addresses the operator registers with the driver are filtered out
  of the network data Windows returns to user mode, signed with a certificate valid from August 2013 to
  September 2014.
discovered_at: "2026-08-16T23:52:00Z"
event_date: "2026-08-14"
run_id: 2026-08-16T2315Z-weekly
priority: high
immediate_action: null
tags: [nation-state, espionage, actively-exploited, zero-day, priv-esc, north-korea-nexus, china-nexus]
regions: [europe, dach, global]
sectors: [public-sector, defense, technology]
entities:
  - actor:lazarus-group
  - campaign:operation-dream-job
  - tool:fudmodule
  - actor:mustang-panda
  - malware:coolclient
  - actor:jewelbug
techniques: [T1068, T1014, T1543.003, T1553.002, T1685, T1685.001, T1547.001, T1055, T1566.003, T1176.001, T1505.003]
affected_products: ["Microsoft Windows 11", "Microsoft Windows", "Roundcube Webmail"]
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/"
    publisher: "Check Point Research"
    date: "2026-08-11"
    role: primary
  - url: "https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-08-14"
    role: primary
  - url: "https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage"
    publisher: "Symantec Threat Hunter Team (Broadcom)"
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "During the intrusion, the threat actor exploited CVE-2026-68820, a zero-day vulnerability in the Microsoft AFD.sys driver, to deploy a new version of FudModule, Lazarus’ kernel-mode rootkit."
    publisher: "Check Point Research"
  - quote: "The entire telemetry teardown suite: process, thread, and image notify callbacks; object and registry callbacks; minifilter removal by altitude band; and the termination of the NT Kernel Logger."
    publisher: "Check Point Research"
  - quote: "successful targeting observed in Western Europe, including France and Germany"
    publisher: "Check Point Research"
  - quote: "The driver also hooks the Nsiproxy driver to filter network-related data returned to user mode."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "The certificate was valid from August 2013 to September 2014."
    publisher: "Kaspersky Securelist (GReAT)"
verification: multi-source
sourcing_note: >
  Each toolset rests on its own research lab's first-hand analysis — Check Point Research for the Lazarus
  intrusion and the AFD.sys zero-day it reported to Microsoft, Kaspersky GReAT for the CoolClient driver.
  Microsoft's own August advisory and CISA's catalogue independently corroborate the exploitation status of
  CVE-2026-68820, as recorded in this pipeline's operational entry of 12 August. The two toolsets are not
  connected by any cited source and this entry asserts no relationship between them; what they share is a
  technique class observed in the same week.
confidence: high
update_of: null
references:
  - 2026-08-12/lazarus-operation-dream-job-cve-2026-68820-afd-fudmodule
  - 2026-08-15/mustang-panda-coolclient-signed-kernel-driver-rootkit
  - 2026-08-16/jewelbug-pdf-viewer-extension-native-messaging-webmail-hole
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**If you did nothing this week:** the August Windows update you deferred is the one that closes the flaw a North Korean intrusion was already using against defence-sector targets in France and Germany — and on any host where it landed, the endpoint agent's own view of that host is no longer evidence.

Check Point Research published the analysis behind CVE-2026-68820 on 11 August, an exploitation-detected flaw fixed in that day's Microsoft updates. Its own disclosure timeline is short: reported to the Microsoft Security Response Center on 28 July, confirmed on 31 July, CVE assigned on 5 August, fixed on Patch Tuesday. The intrusion it came from is the long-running fake-job-offer campaign, and the interesting half is what the zero-day was spent on: "During the intrusion, the threat actor exploited CVE-2026-68820, a zero-day vulnerability in the Microsoft AFD.sys driver, to deploy a new version of FudModule, Lazarus' kernel-mode rootkit" ([Check Point Research, 2026-08-11](https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/)). A privilege-escalation bug is worth burning as a zero-day when what it buys is kernel code execution, and what kernel code execution buys here is enumerated in the same analysis: the component set FudModule v3.1 shares with its predecessor is "The entire telemetry teardown suite: process, thread, and image notify callbacks; object and registry callbacks; minifilter removal by altitude band; and the termination of the NT Kernel Logger." Every item on that list is a mechanism by which an endpoint product learns that something happened. The European relevance is direct — Check Point records "successful targeting observed in Western Europe, including France and Germany", and that a compromised organisation headquartered in France was subsequently used to send spear-phishing to further targets, which puts a peer institution's own domain on the sending side of the lure.

Kaspersky's GReAT team published the second instance three days later: a new CoolClient backdoor variant attributed to the actor it tracks as HoneyMyte, also known as Mustang Panda, which installs a kernel-mode driver as a Windows service once the implant already holds Service Control Manager access and the SeTcbPrivilege privilege. Alongside the expected process, file and registry hiding — including unlinking the driver from `PsLoadedModuleList` so it stops appearing in kernel module enumeration — it carries a function with a narrower and more interesting purpose: "The driver also hooks the Nsiproxy driver to filter network-related data returned to user mode", with the user-mode component registering its own command-and-control IPv4 addresses with the driver through a dedicated control code ([Kaspersky Securelist, 2026-08-14](https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/)). The effect is precise: the implant's own C2 addresses are removed from the answers Windows gives to anything that asks the host what it is connected to. The driver is signed with a certificate issued to Nanjing Ranyi Technology Co., Ltd., and Kaspersky records that "The certificate was valid from August 2013 to September 2014" — long expired, which is exactly why it still works for driver loading under signature-enforcement rules that honour the signing timestamp rather than present validity.

Symantec's Jewelbug investigation, published the same week, is the user-mode expression of the same objective and worth naming for contrast rather than similarity: rather than a kernel driver, the group escaped the browser sandbox through a native-messaging host registered under the misleading name `com.microsoft.runedge`, running operator commands through the Windows command interpreter ([Symantec Threat Hunter Team, 2026-08-13](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage)). That campaign's watering hole reached more than 15 government webmail tenants in a Middle Eastern country, not in Europe; the transferable part is the naming choice, which is aimed at an analyst reading a list of registered helpers rather than at a detection engine.

**Defender takeaway:** these two rootkits invalidate different evidence, and the distinction decides what you do next. Lazarus's teardown suite disables the callbacks and the log channel through which the host reports, which means an affected host stops producing certain telemetry — the failure is visible as absence, if anything is watching for it. CoolClient's Nsiproxy hook leaves telemetry flowing and edits its content, which means the host keeps reporting and reports something false. Absence you can hunt for centrally; falsified content you cannot, from the host itself, at all. The practical consequence is that on any host where a kernel-mode compromise is suspected, the network record has to come from somewhere other than the host — flow records, firewall and proxy logs, DNS resolver logs, the egress point — because those are the only observers the driver cannot reach. Patching CVE-2026-68820 through the August cumulative update closes the delivery route in the Lazarus case and is the immediate task; there is no equivalent single fix for the CoolClient case, where the precondition is that the implant already holds Service Control Manager access, so the control is preventing that state rather than detecting the driver afterwards.

**Triage:** the discriminator for the driver-loading step is provenance rather than behaviour. Kernel drivers install legitimately all the time — a service creation with a kernel-driver image path is ordinary on a patch day or a software rollout. What is not ordinary is that combination arriving with a code-signing certificate whose validity period ended years ago, from a signer with no other presence in the estate, written into a directory belonging to an unrelated application rather than to a driver package; legitimate driver installs come from vendor installers with current signing chains and matching file locations. For the network-hiding behaviour specifically, the discriminator is a disagreement between two observers of the same traffic: a host reporting no connection to a destination that the egress point, the resolver or the flow record shows it talking to. That comparison is the only reliable test once the driver is resident, and it requires that the second observer already exists — which is a collection decision made before the intrusion, not during it.
