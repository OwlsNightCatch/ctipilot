---
schema: 1
kind: threat
title: "Sekoia: an APT29-linked watering hole serves n-day iOS and Android exploit chains through compromised sites, clone domains and a one-week compromise of the Plerdy tracker; CISA lists the Apple WebKit pointer-authentication bypass CVE-2024-27834 as exploited on 2026-11-04"
headline: "APT29-linked watering hole uses n-day iOS and Chrome chains; CISA lists CVE-2024-27834; updated devices resist"
summary: >
  Sekoia reports a watering-hole campaign it assesses with moderate to high confidence to be APT29 or a subgroup, serving platform-specific
  exploit chains for iOS 16.7, a DarkSword-based iOS chain and Chrome 139 to 145 on Android through injected sites, clone domains and a
  one-week compromise of the Plerdy analytics script; Sekoia says none of the chains works against fully updated devices. CISA added the
  Apple WebKit pointer-authentication bypass CVE-2024-27834, the second step of the iOS 16.7 chain and fixed in May 2024, to its Known Exploited
  Vulnerabilities catalog on 2026-11-04; no Swiss victim is named.
discovered_at: "2026-11-05T03:58:30Z"
updated_at: null
event_date: "2026-11-04"
run_id: 2026-11-05T0255Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, supply-chain, mobile, zero-click, vulnerabilities, actively-exploited, cisa-kev, patch-available]
nexus: [russia-nexus]
regions: [europe, us]
sectors: [defense]
entities: ["campaign:poisoned-source-apt29-watering-hole-2026", "actor:midnight-blizzard", "tool:darksword", "malware:androsnitch", "product:google-chrome", "product:plerdy-seo-tracker", "product:qualcomm-adreno-gpu-driver"]
techniques: [T1189, T1195.002, T1203, T1068, T1539, T1555.003, T1592, T1583.001, T1557, T1005, T1041]
affected_products: ["Apple iOS", "Apple iPadOS", "Google Chrome", "Qualcomm Adreno GPU driver", "Plerdy SEO Tracker"]
cves:
  - id: CVE-2024-27834
    cvss: null
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "iOS and iPadOS before 16.7.8 (iPhone 8, 8 Plus, X, iPad 5th generation, iPad Pro 9.7-inch and 12.9-inch 1st generation) and before 17.5; CISA's catalog entry also lists macOS, Safari, tvOS and watchOS; Sekoia reports exploitation only against iOS 16.7"
    fixed: "iOS and iPadOS 16.7.8 and 17.5 (both released 2024-05-13); CISA's catalog entry lists the other Apple platforms"
  - id: CVE-2025-43529
    cvss: null
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "iOS before 26.2 and 18.7.3; first step of Sekoia's iOS 16.7 chain and of the DarkSword-based chain"
    fixed: "iOS 26.2 and 18.7.3; no fetched Apple page lists a fix for iOS 16.7.x"
  - id: CVE-2026-20700
    cvss: null
    epss: null
    type: logic-flaw
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "iOS before 26.3; pointer-authentication bypass in the DarkSword-based chain"
    fixed: "iOS 26.3"
  - id: CVE-2025-14174
    cvss: null
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "iOS before 26.2 and 18.7.3; first sandbox escape of the DarkSword-based chain"
    fixed: "iOS 26.2 and 18.7.3"
  - id: CVE-2025-43510
    cvss: null
    epss: null
    type: lpe
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "iOS before 26.1 and 18.7.2; second sandbox escape of the DarkSword-based chain"
    fixed: "iOS 26.1 and 18.7.2"
  - id: CVE-2025-43520
    cvss: null
    epss: null
    type: lpe
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "iOS before 26.1 and 18.7.2; kernel read and write step of the DarkSword-based chain"
    fixed: "iOS 26.1 and 18.7.2"
  - id: CVE-2026-3910
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Chrome before 146 on Android, served by Sekoia's delivery host to Chrome 139 to 145 except 143; code execution in the V8 renderer"
    fixed: "Chrome 146 (desktop stable 146.0.7680.75/76 of 2026-03-12)"
  - id: CVE-2025-27038
    cvss: null
    epss: null
    type: lpe
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Android phones with a vulnerable Qualcomm Adreno GPU driver; sandbox escape of the Android chain, which stops on the Samsung Galaxy S25 Ultra"
    fixed: "OEM patch level; CISA's catalog entry says to check with each OEM for patching status"
sources:
  - url: "https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits"
    publisher: "Sekoia Threat Detection & Research"
    date: "2026-11-04"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.11.04)"
    date: "2026-11-04"
    role: corroborating
  - url: "https://support.apple.com/en-us/120898"
    publisher: "Apple (iOS 16.7.8 and iPadOS 16.7.8 security content)"
    date: "2024-05-13"
    role: corroborating
  - url: "https://support.apple.com/en-us/120905"
    publisher: "Apple (iOS 17.5 and iPadOS 17.5 security content)"
    date: "2024-05-13"
    role: corroborating
  - url: "https://support.apple.com/en-us/127113"
    publisher: "Apple (iOS 16.7.16 security content)"
    date: "2026-05-11"
    role: corroborating
  - url: "https://support.apple.com/en-us/125884"
    publisher: "Apple (iOS 26.2 and iPadOS 26.2 security content)"
    date: "2025-12-12"
    role: corroborating
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain"
    publisher: "Google Threat Intelligence Group (DarkSword)"
    date: "2026-03-18"
    role: corroborating
  - url: "https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop_12.html"
    publisher: "Chrome Releases"
    date: "2026-03-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "None of them contain zero-days or work against fully updated devices."
    publisher: "Sekoia Threat Detection & Research"
    source_url: "https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits"
  - quote: "These elements lead us to assess with moderate to high confidence that the intrusion set behind this watering hole campaign is APT29, or at least one of its subgroups."
    publisher: "Sekoia Threat Detection & Research"
    source_url: "https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits"
  - quote: "Apple iOS, iPadOS, macOS, Safari, tvOS and watchOS 10.5 contain an improper authentication vulnerability which could allow an attacker with arbitrary read and write capability to bypass pointer authentication."
    publisher: "CISA Known Exploited Vulnerabilities catalog"
    source_url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
verification: single-source
sourcing_note: >
  Sekoia is the only originator of the campaign: The Hacker News and BleepingComputer relay its report, and its attribution rests on a partner
  CERT's comparison with an unpublished 2025 report, Google TAG's comparison with a 2024 watering hole, victimology and infrastructure habits, a
  vendor assessment and not a government attribution. The exploit mapping comes from Sekoia's own table; Sekoia's
  table labels the DarkSword-based chain iOS 18.5 while Google's report says the kit supports iOS 18.4 to 18.7. CISA's listing of CVE-2024-27834
  names no campaign, and the link to Sekoia's report is the date alone. Sekoia publishes some indicators and withholds several delivery hosts,
  exfiltration hosts and its YARA rules; no indicators are carried here.
confidence: medium
references:
  - 2026-10-28/deadtag-expired-tag-domains-coruna-darksword-iphone-kits
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Move every managed iPhone and iPad to the newest iOS available for its model and every managed Android phone to Chrome 146 or later and the OEM patch level that fixes CVE-2025-27038, and list the devices that cannot go past iOS 16.7.x (iPhone 8, 8 Plus, X, iPad 5th generation, iPad Pro 9.7-inch and 12.9-inch 1st generation per Apple), because Sekoia's chains do not work against fully updated devices and CISA lists all eight flaws they deliver as exploited."
updates: []
migrated_from: null
---

CISA added CVE-2024-27834, a WebKit flaw that lets an attacker with arbitrary read and write capability bypass Pointer Authentication and that Apple fixed on 2024-05-13, to its Known Exploited Vulnerabilities catalog on 2026-11-04, and names no victim or method ([CISA KEV, 2026-11-04](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json); [Apple, 2024-05-13](https://support.apple.com/en-us/120898); [Apple, 2024-05-13](https://support.apple.com/en-us/120905)). The same day Sekoia reported a watering-hole campaign that it assesses with moderate to high confidence to be APT29 or one of its subgroups and in which that flaw is the pointer-authentication bypass of an iOS chain ([Sekoia, 2026-11-04](https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits)); the link between the listing and the campaign is the date alone. Sekoia retrieved three chains from the delivery host, which profiles the visitor and serves a platform-specific exploit without user interaction: an iOS 16.7 chain (CVE-2025-43529, then CVE-2024-27834) that steals the cookies of running apps; a DarkSword-based iOS chain that Sekoia's table labels iOS 18.5 (CVE-2025-43529 with CVE-2026-20700, then CVE-2025-14174 with CVE-2025-43510, then CVE-2025-43520) that harvests the phone; and an Android chain for Chrome 139 to 145 except 143 (CVE-2026-3910, then the Adreno driver flaw CVE-2025-27038) that takes Chrome cookies, saved logins, history and Wi-Fi configuration ([Sekoia, 2026-11-04](https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits)). The payloads exfiltrate data without establishing persistence, and Sekoia says none of the chains contains a zero-day or works against fully updated devices ([Sekoia, 2026-11-04](https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits)).

Delivery used JavaScript injected into legitimate sites, among them a Ukrainian gas producer, a US chemical-industry trade association, a Bulgarian military-related site and an Australian clinic; reverse-proxy clones of high-profile sites; and a one-week compromise, 27 August to 3 September 2026, of the Plerdy SEO tracker script, which Sekoia says exposed hundreds or thousands of sites, mostly Ukrainian ([Sekoia, 2026-11-04](https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits)). Sekoia names no Swiss victim, counts no infected devices and says it is working with national CERTs on victim identification.

**Exposure:** iPhones and iPads below the builds that fix the six iOS flaws, and Android phones on Chrome before the fix of CVE-2026-3910 or an unpatched Adreno driver. Sekoia's iOS 16.7 chain filters for iOS 16.7 and 16.7.10, and the sources do not establish whether the later 16.7.x builds Apple lists for iPhone 8, 8 Plus, X, iPad 5th generation and the first-generation iPad Pro models, up to 16.7.16 of 2026-05-11, are exploitable ([Sekoia, 2026-11-04](https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits); [Apple, 2026-05-11](https://support.apple.com/en-us/127113)).

Fixes: iOS 26.2 and 18.7.3 close CVE-2025-43529 and CVE-2025-14174, iOS 26.1 and 18.7.2 close CVE-2025-43510 and CVE-2025-43520, iOS 26.3 closes CVE-2026-20700, and Chrome 146 closes CVE-2026-3910 ([Apple, 2025-12-12](https://support.apple.com/en-us/125884); [Google Threat Intelligence Group, 2026-03-18](https://cloud.google.com/blog/topics/threat-intelligence/darksword-ios-exploit-chain); [Chrome Releases, 2026-03-12](https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop_12.html)).

**Detection:** Sekoia names one on-device trace, a marker cookie that the iOS 16.7 chain's script sets as a replay guard so the exploit does not fire twice on a victim; it publishes some indicators and withholds several delivery and exfiltration hosts, so a visit to an injected site shows in web proxy and DNS telemetry from managed phones only against indicators obtained from Sekoia or a national CERT; the dependable check is the OS and Chrome version inventory ([Sekoia, 2026-11-04](https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits)).

**Defender takeaway:** bring managed iOS devices to the newest release for each model and Android phones to current Chrome and the OEM patch level, because Sekoia says updated devices resist these chains and CISA lists every flaw they deliver as exploited ([Sekoia, 2026-11-04](https://www.sekoia.com/blog/poisoned-source-apt29-watering-holes-targets-mobile-devices-with-n-day-exploits); [CISA KEV, 2026-11-04](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)); the devices that cannot go past iOS 16.7.x are the open question.
