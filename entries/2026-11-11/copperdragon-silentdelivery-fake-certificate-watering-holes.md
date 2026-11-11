---
schema: 1
kind: threat
title: "CopperDragon: Check Point ties three China-nexus intrusion sets to one Sparrow-framework supplier, among them SilentDelivery watering holes on government, shipping, IT and research sites that show a fake Chrome certificate warning (Czech Republic, Germany and France in its telemetry)"
headline: "Check Point: a Sparrow-framework supplier fronts government watering holes with a fake Chrome certificate warning"
summary: >
  Check Point Research groups three China-nexus intrusion sets under a malware-supply entity it calls CopperDragon, a possible supplier to actors that use the cross-platform Sparrow framework; shared tooling, Check Point cautions, does not prove one operator. The nearest to the constituency is SilentDelivery, which injects script into compromised government, shipping, IT and research websites to replace the page with a fake Chrome certificate warning that pushes a "Certificate Fix" installer carrying the SquadC backdoor, with the Czech Republic, Germany and France among the countries in Check Point's telemetry.
discovered_at: "2026-11-11T03:40:00Z"
updated_at: null
event_date: "2026-11-10"
run_id: 2026-11-11T0256Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, china-nexus]
regions: [global, europe]
sectors: [public-sector, transport, technology]
entities: ["actor:copperdragon", "malware:squadc", "campaign:silentdelivery-watering-hole-2026"]
techniques: [T1189, T1204.002, T1190, T1566.001, T1202, T1027, T1547.001, T1574.001, T1554, T1014, T1205, T1547.005, T1003.001, T1056.001, T1136.001, T1021.001, T1047, T1572, T1071.004, T1036.005]
affected_products: ["Microsoft Windows", "OpenSSH"]
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/"
    publisher: "Check Point Research"
    date: "2026-11-10"
    role: primary
  - url: "https://medium.com/@dzaripova1177/the-sparrow-that-chirped-too-loud-famoussparrow-attacks-using-updated-sparrowdoor-and-the-new-29ac2d90544d"
    publisher: "Positive Technologies (on Medium)"
    date: "2026-08-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The fake warning blocked access to the website and instructed the user to install a “Certificate Fix” utility."
    publisher: "Check Point Research"
    source_url: "https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/"
  - quote: "All the compromised websites we confirmed were related to the government, shipping, and IT and research sectors."
    publisher: "Check Point Research"
    source_url: "https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/"
  - quote: "Based on Check Point telemetry, the operations primarily targeted organizations in countries such as the Czech Republic, Germany, France, Taiwan, Nepal, Hong Kong and Indonesia."
    publisher: "Check Point Research"
    source_url: "https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/"
  - quote: "However, the use of the same backdoor or C2 infrastructure does not necessarily mean that two intrusions were conducted by the same actor."
    publisher: "Check Point Research"
    source_url: "https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/"
  - quote: "Based on the samples we identified, we determined that the threat actor used an infection chain involving compromised websites and fake certificates in at least four locations: Taiwan, Germany, Indonesia, and the Czech Republic."
    publisher: "Positive Technologies"
    source_url: "https://medium.com/@dzaripova1177/the-sparrow-that-chirped-too-loud-famoussparrow-attacks-using-updated-sparrowdoor-and-the-new-29ac2d90544d"
verification: multi-source
sourcing_note: >
  Check Point holds the telemetry and the three-set grouping, which it presents as a supplier hypothesis, not an operator attribution; Positive Technologies independently documented the same fake-certificate chain (it calls the backdoor SquawkDoor) with victims in Taiwan, Germany, Indonesia and the Czech Republic. No Swiss body is named in either source, and Check Point does not name the Linux server flaw used in the OceanGate set.
confidence: high
references: ["2026-09-18/famoussparrow-sparrowocky-backdoor-latam-gov"]
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

Check Point Research's year-long investigation groups three intrusion sets under one malware-supply entity it calls CopperDragon, a possible "digital quartermaster" for China-nexus actors that use the cross-platform Sparrow framework (FamousSparrow and Earth Estries among them); Check Point itself cautions that the use of the same backdoor or C2 infrastructure "does not necessarily mean" the same actor ran two intrusions, so this is a hypothesis ([Check Point Research, 2026-11-10](https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/)).

SilentDelivery, active since early 2026 against Europe and Asia, is the set nearest the constituency. Compromised government, shipping, IT and research websites, one through cross-site scripting in an unsanitised input field, carry obfuscated JavaScript that fingerprints the visitor and replaces the page with a language-localised fake Google Chrome SSL warning urging a "Certificate Fix" utility; the MSI, served from compromised cloud storage buckets, installs the new SquadC backdoor or a SparrowDoor variant ([Check Point Research, 2026-11-10](https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/)). SquadC can be set to run only while a browser process is alive, persists through a Run key named WindowsUpdateAssist, and offers file operations, command execution and screenshots. A second route is a spear-phishing RAR whose LNK abuses ftp.exe, with the same C2 ([Check Point Research, 2026-11-10](https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/)). Positive Technologies independently documented the same fake-certificate chain, with victims in Taiwan, Germany, Indonesia and the Czech Republic ([Positive Technologies, 2026-08-21](https://medium.com/@dzaripova1177/the-sparrow-that-chirped-too-loud-famoussparrow-attacks-using-updated-sparrowdoor-and-the-new-29ac2d90544d)).

The other two sets show what follows an intrusion. OceanGate in Asia starts from an exploited internet-facing Linux server and moves through trojanised ssh and sshd binaries that log passwords, a Linux backdoor that can load a kernel rootkit, FRP and Chisel tunnels, a hidden local administrator account and an LSA security-package credential interceptor; recent SparrowDoor builds embed the WinDivert driver to share a service port such as 443. DarkWire against Latin American telecom and government bodies uses DLL sideloading of uncommon executables, SoftEther VPN renamed to system-process names, DNS MX tunnelling and WMI lateral movement ([Check Point Research, 2026-11-10](https://research.checkpoint.com/2026/not-all-that-glitters-is-gold-tracking-copperdragons-sparrow-framework-around-the-globe/)). No Swiss victim is named.

**Exposure:** staff of public bodies, shipping, IT and research organisations who browse peer websites, web teams whose sites accept unsanitised input, and Windows endpoints that let a standard user run an MSI from a browser download.

**Detection:** in endpoint telemetry, a browser followed by msiexec running an installer named like a certificate repair utility and a new Run key value with an update-themed name; in module-load telemetry, DLL sideloading by rarely abused executables, and the WinDivert driver loaded by a process that is not a VPN or firewall product; in account telemetry, a new local administrator account; on Linux, ssh and sshd binaries that differ from the package-manager copy and frpc or chisel binaries; in DNS, MX-query volume from servers that send no mail.

**Triage:** WinDivert is legitimate in VPN and firewall products, so the signal is a parent that is a sideloaded DLL or backdoor rather than the vendor's signed service; SoftEther is legitimate software, but not under a system-process name in a non-system path; a genuine Chrome SSL warning is never cleared by installing an MSI.

**Defender takeaway:** treat a browser page that offers a "certificate fix" installer as an incident trigger and stop standard users running MSI installers from a browser download; web teams of government and research sites should check for injected third-party script and input-handling flaws, because a compromised site becomes a delivery vehicle for its peers.
