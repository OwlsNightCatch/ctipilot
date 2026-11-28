---
schema: 1
kind: threat
title: "Jewelbug: one script tag in a shared government webmail template put a watering hole on 15+ ministry tenants at once, and the browser extension it drops escapes the sandbox through a native-messaging host named after Microsoft Edge"
headline: "A hack-for-hire group hit 15+ government webmail tenants with one script tag, then escaped the browser via a fake Edge helper"
summary: >
  Symantec's Threat Hunter Team published a months-long investigation into Jewelbug, a China-based
  hack-for-hire group that runs government espionage and a cryptocurrency-fraud business from one
  control panel. Rather than breach ministries one at a time, the group compromised the shared
  web-hosting platform run by a state telecommunications provider and added a single script tag to the
  common webmail template, planting a watering hole on more than 15 government tenants simultaneously.
  Victims who took the fake Adobe Flash lure received the Antino backdoor, which side-loads a malicious
  "PDF Viewer" browser extension and registers a native-messaging host called com.microsoft.runedge —
  the component that turns browser-level access into command execution on the host.
discovered_at: "2026-08-16T04:40:00Z"
event_date: "2026-08-13"
run_id: 2026-08-16T0411Z-intel
priority: high
immediate_action: null
tags: [espionage, nation-state, phishing, identity, infostealer, cloud]
regions: [middle-east, apac, global]
sectors: [public-sector, defense, telco]
entities: [actor:jewelbug, tool:xg-web, malware:antino, malware:jewelbug-pdf-viewer-extension, malware:clientking]
techniques: [T1189, T1176.001, T1185, T1204.002, T1059.003, T1539, T1056.003, T1102.001, T1102.002, T1113, T1115, T1014, T1556.003, T1090]
affected_products: ["Google Chrome", "Mozilla Firefox"]
cves: []
sources:
  - url: "https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage"
    publisher: "Symantec Threat Hunter Team (Broadcom)"
    date: "2026-08-13"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/hackers-breach-govt-webmail-while-running-parallel-crypto-fraud/"
    publisher: "BleepingComputer"
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Rather than breach each ministry separately, Jewelbug compromised the shared web-hosting platform run by the state telecommunications provider and national network-services agency, obtaining write access to the common webmail installation, and added a single script tag."
    publisher: "Symantec Threat Hunter Team"
  - quote: "A single campaign spanned more than 15 government webmail tenants, with the hook firing on the login page and every mailbox view, indicating it sat in the shared template rather than being delivered per user."
    publisher: "Symantec Threat Hunter Team"
  - quote: "To escape the browser sandbox, the extension talked to a Windows helper registered as a native-messaging host under the misleading name com.microsoft.runedge, which ran operator commands through the Windows command interpreter and returned the output to the panel."
    publisher: "Symantec Threat Hunter Team"
  - quote: "Masquerading as a document reader, it requested effectively every dangerous permission the browser exposes: cookies, scripting, debugger access, web request interception, download monitoring, and native messaging across all sites."
    publisher: "Symantec Threat Hunter Team"
verification: single-source
sourcing_note: >
  Symantec's Threat Hunter Team is the only party with first-hand visibility here — the investigation
  rests on access to the group's own control panel and victim database. BleepingComputer's coverage
  reproduces that research rather than independently observing the activity, so this is one assessor
  with a second publisher: credibility 2, not 1. Symantec states that Jewelbug is also tracked as Earth
  Alux, REF7707 and CL-STA-0049; those predecessor reports were not fetched in this run, so nothing is
  claimed about their content beyond Symantec's own naming of them. The named-individual attribution
  for the fraud arm is Symantec's high-confidence assessment and is reported here as such, without the
  name. Victim countries are described by region only, as the source does.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: apt-campaign
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Symantec's Threat Hunter Team has published the results of a months-long investigation into Jewelbug, a China-based hack-for-hire group that runs two missions from one set of hands: espionage against government ministries and militaries across the Middle East, Southeast Asia and South Asia, and a for-profit cryptocurrency-fraud business aimed at Chinese-speaking victims. Both are administered from a single control panel called XG-Web, a browser-centric remote-access and information-stealing framework built as a React panel over a Node.js backend with a MySQL database that doubles as the rendezvous point for victim implants; its developers describe it in their own documentation as a "penetration-testing platform", while its internal function names include browser hijacking, data theft and man-in-the-middle attack ([Symantec, 2026-08-13](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage)). Symantec assesses with high confidence that the fraud and search-engine-optimisation arm is run by the sole legal representative of a registered Changsha company, on the basis of government-issued identity documents, a business licence and a signed authorisation letter recovered from the operators, and considers it most likely that the SEO business supplied access, infrastructure and delivery to the espionage operation rather than one person performing both roles ([Symantec, 2026-08-13](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage)).

**The access pattern is the finding.** In its largest espionage operation, Jewelbug did not attack ministries individually. It compromised the shared web-hosting platform run by a Middle Eastern state telecommunications provider and national network-services agency, obtained write access to the common webmail installation, and added one script tag — planting a watering hole on every government tenant on that platform at once, in a single campaign that spanned more than 15 tenants ([Symantec, 2026-08-13](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage)). Symantec infers the tag sat in the shared template rather than being delivered per user because the hook fired on the login page and on every mailbox view. The group also hooked the hosting provider's own administrators to harvest the credentials that granted that write access, which closes the loop: the platform operator's identity was the key to every tenant behind it.

The chain that follows is short and entirely conventional in its parts, which is what makes it worth mapping. When a ministry staff member logged in, the injected script opened a WebSocket to command-and-control, completed a handshake and reported in; a cookie module exfiltrated the page's cookies, and a labelling module read the username straight out of the webmail interface and tagged the new victim with their government email address. Only then did the operators push a lure module, which checked that the address ended in one of nine targeted government domains, that the account was not already compromised, and that the host was Windows, before overlaying a fake Adobe Flash update prompt ([Symantec, 2026-08-13](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage)). That server-side qualification step is a defensive problem in itself — the malicious behaviour a visiting analyst or a sandbox sees is a cookie read and a WebSocket, because the payload stage never fires for a visitor who fails the filter.

Clicking the prompt downloaded the Antino backdoor, delivered as a fake Adobe Flash or Adobe installer and using the Microsoft Graph API as its command-and-control channel so its traffic sits inside legitimate Microsoft cloud services. Antino also side-loaded the "PDF Viewer" extension into the victim's browser profile, dropped a native-messaging helper and wrote the registry value that enabled it ([Symantec, 2026-08-13](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage)). The extension is the group's primary implant and requested, in Symantec's words, effectively every dangerous permission the browser exposes — cookies, scripting, debugger access, web-request interception, download monitoring and native messaging across all sites. A background service worker gave the operator a full bridge into the browser API: any Chrome or Firefox function invocable by name, arbitrary JavaScript injected into any page, credentials harvested by hooking login forms, the full cookie jar exfiltrated, live cookie-change events subscribed to so new session tokens are stolen in near real time, plus history, bookmarks, screenshots, clipboard and intercepted traffic. A clipboard module able to swap a copied cryptocurrency address for the attacker's was present and active on victims, but Symantec records that no address-replacement rules were deployed, so the swap was not used during the observed period.

**The sandbox escape is the part defenders should take away.** To reach the host, the extension talked to a Windows helper registered as a native-messaging host under the misleading name `com.microsoft.runedge`, which ran operator commands through the Windows command interpreter and returned output to the panel; Antino wrote the enabling registry value under the current user's own hive ([Symantec, 2026-08-13](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage)). Native messaging is a documented, legitimate browser feature — it is how password managers and document tools talk to their desktop components — and that is precisely why it works here. For at least one victim the bridge carried authenticated traffic to an internal virtualisation-management interface, so browser access became reach into the network behind it.

The group's toolset extends past the browser. Symantec counts 37 builds of a Rust implant the developers call ClientKing, reaching servers and network devices rather than browsers, supporting five command-and-control transports including a custom DNS tunnel, and offering an interactive shell, SOCKS pivoting and the ability to load kernel modules directly from memory; a companion toolkit adds a kernel-module rootkit and a malicious authentication module hooked into `su` and `sudo` to steal credentials, across x86-64 servers, ARM64 devices and consumer routers ([Symantec, 2026-08-13](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage)). For payload delivery the backend created public Google Documents, wrote an obfuscated payload into the body and had implants fetch and execute it, which resolves to Google-owned infrastructure that reputation filtering is unlikely to block, and the group disguised its command-and-control hostnames as typosquats of common web resources such as font services. A scheduled job checked the group's own domains against a public multi-scanner every twelve hours so operators could rotate away from anything flagged.

Scale, in the group's own bookkeeping: the victim database holds more than one million implant check-in rows, more than 580,000 stolen browser cookies, several thousand captured credentials and more than 2,300 exfiltrated email bodies ([Symantec, 2026-08-13](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage)). Symantec also notes builds configured to beacon through the internal corporate proxy of a major US aerospace and industrial manufacturer, so the tooling is not confined to government estates.

**Defender takeaway:** the transferable exposure is architectural, not geographic. Any administration that concentrates several independent bodies onto one shared webmail or portal platform has created a single template whose write access is worth more than any one tenant — the Swiss cantonal and communal model of shared e-government hosting has exactly this shape. Two controls follow directly from the mechanics: treat write access to a shared front-end template as a tier-zero privilege with change review and file-integrity monitoring on the template itself, since the entire compromise here was one `<script src=...>` line that no tenant could see in their own logs; and inventory native-messaging host registrations across the managed browser estate, because that registry key is the documented seam between a browser extension and the operating system, and nothing about the browser's own sandbox constrains what the helper on the other side of it does.

**Triage:** a native-messaging host registered under `HKCU\SOFTWARE\<browser>\NativeMessagingHosts\<reverse-domain-name>` is normal on its own — legitimate password managers, document viewers and enterprise agents use this exact mechanism. Three discriminators separate this from that baseline, and they derive from the mechanics the source describes rather than from any indicator: a host name asserting a Microsoft identity while being written per-user under `HKCU` by a downloaded executable, where a genuine Microsoft browser component arrives through a signed machine-wide installer; the command interpreter appearing with a native-messaging host executable as its parent, a process-lineage pair that legitimate browser-helper traffic does not produce; and an extension whose manifest requests native messaging together with debugger access, web-request interception and all-sites cookie access, a permission combination a document reader has no use for. The extension side-loads into the browser profile rather than arriving from a store, so an extension inventory built only from store IDs will not see it.
