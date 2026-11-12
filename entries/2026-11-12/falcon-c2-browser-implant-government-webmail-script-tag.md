---
schema: 1
kind: threat
title: "Falcon: Unit 42 describes a browser-resident command-and-control framework planted in government webmail and web applications, with a script tag in Roundcube at a Middle Eastern foreign ministry and a sideloaded 'PDF Viewer' extension elsewhere; it shares its core with PeckBirdy"
headline: "Unit 42: Falcon C2 runs inside the browser, fed by a script tag in government webmail such as Roundcube"
summary: >
  Unit 42 describes Falcon, a NodeJS command-and-control framework whose JavaScript implant runs inside the victim's browser and leaves no file on the endpoint, planted by a script tag in government webmail portals and web applications, among them the Roundcube webmail of a Middle Eastern foreign ministry (39 instances in that country), and by a sideloaded Chrome extension disguised as a PDF viewer. Unit 42 saw it against government bodies in one Middle Eastern and four Southeast Asian countries between March and May 2026, names no actor, does not say how the script tags were placed and is unaware how the extensions are deployed, and assesses with high confidence that Falcon and PeckBirdy are variants of one core framework.
discovered_at: "2026-11-12T04:05:00Z"
updated_at: null
event_date: "2026-11-11"
run_id: 2026-11-12T0255Z-intel
priority: notable
immediate_action: null
tags: [espionage]
regions: [middle-east, apac]
sectors: [public-sector]
entities: ["malware:falcon-c2", "malware:peckbirdy", "malware:antino", "product:roundcube-webmail"]
techniques: [T1189, T1056.003, T1185, T1539, T1113, T1176.001, T1204.002, T1036.005, T1027, T1071.001, T1573.002, T1547.001, T1102.002]
affected_products: ["Roundcube Webmail", "Google Chrome"]
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-11-11"
    role: primary
  - url: "https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/peckbirdy-script-framework"
    publisher: "Trend Micro (TrendAI)"
    date: "2026-01-26"
    role: corroborating
  - url: "https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage"
    publisher: "Symantec Threat Hunter Team (Broadcom)"
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "We are currently unaware of how an operator is deploying these browser extensions."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/"
  - quote: "We observed a total of 39 Roundcube instances being affected within the target country."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/"
  - quote: "Based on these extensive technical overlaps, we assess with high confidence that Falcon and PeckBirdy represent variants of the same core framework."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/"
verification: single-source
sourcing_note: "Everything about Falcon's victims and mechanics is Unit 42's own telemetry and analysis; no independent source describes the Falcon intrusions. Trend's PeckBirdy report corroborates only the lineage side (a JScript command-and-control framework used by China-aligned actors since 2023). Unit 42 names no actor, and it gives a narrative for only three of the five campaigns."
confidence: medium
references:
  - 2026-08-16/jewelbug-pdf-viewer-extension-native-messaging-webmail-hole
  - 2026-10-02/uat-11587-antino-microsoft-graph-c2-asian-governments
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

Unit 42 describes Falcon C2, also called XG and not the CrowdStrike Falcon sensor, a NodeJS command-and-control framework whose operator-controlled JavaScript implant runs inside the victim's browser, so the endpoint holds no file for it ([Unit 42, 2026-11-11](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/)). A script tag placed in a trusted site makes each visit request the implant from the Falcon server, which returns a script obfuscated per browser session, and the implant then holds a TLS WebSocket to the server while the tab is open and runs operator JavaScript through eval ([Unit 42, 2026-11-11](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/)). Unit 42 identified compromised government entities in one Middle Eastern and four Southeast Asian countries between March and May 2026, among them ministries and law enforcement agencies, and names no actor ([Unit 42, 2026-11-11](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/)).

In April 2026 a script tag inserted into the Roundcube webmail portal of a Middle Eastern ministry of foreign affairs let the operator intercept credentials as users signed in and monitor sessions (39 Roundcube instances in that country, none observed elsewhere; how the tag got in is not stated) ([Unit 42, 2026-11-11](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/)). In May 2026 a module in a Southeast Asian police web application harvested usernames and then showed a fake Adobe Flash Player update prompt to chosen users, which served the Antino implant that uses Microsoft OneDrive for command and control ([Unit 42, 2026-11-11](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/)). Against a justice-department entity in another country, a Chrome extension named PDF Viewer, sideloaded in developer mode, checked in every 3 to 4 minutes for over three weeks and exfiltrated plaintext credentials for an internal correspondence system and a screenshot of a document the victim was viewing ([Unit 42, 2026-11-11](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/)). The Jewelbug campaign also used an extension named PDF Viewer ([Symantec, 2026-08-13](https://www.security.com/threat-intelligence/jewelbug-crypto-fraud-espionage)); Unit 42 lists it only as a further resource.

Unit 42 assesses with high confidence that Falcon and PeckBirdy (Trend's JScript framework used by China-aligned actors since 2023) are variants of one core framework; that is code lineage, not who operates Falcon ([Unit 42, 2026-11-11](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/); [Trend Micro, 2026-01-26](https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/peckbirdy-script-framework)).

**Exposure:** internal webmail, ticketing and case-management portals whose templates or headers an attacker can edit (Roundcube is the named case), and managed Chrome browsers that allow extensions to be sideloaded in developer mode; Unit 42 does not say how the script tags or the extensions reached their targets.

**Detection:** Unit 42's four monitoring items, telemetry class first: template and header integrity on webmail, ticketing and case-management portals for a script tag loading a resource from an unfamiliar domain, especially one returning a heavily numeric JavaScript array with a small decoder loop; extension inventory for developer-mode extensions imitating utilities such as PDF viewers with broad permissions; Baidu Analytics-style cookie or local-storage keys on internal government web applications; and OneDrive traffic to tenants outside the organisation's own with repeated small JSON writes ([Unit 42, 2026-11-11](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/)).

**Triage:** Unit 42's basis for the cookie check is that Baidu Analytics cookies are normal on sites that use that service and anomalous on internal government web applications where it has no reason to appear ([Unit 42, 2026-11-11](https://unit42.paloaltonetworks.com/falcon-c2-browser-compromise/)).

**Defender takeaway:** compare the templates and headers of internal webmail and case-management portals with a known-good copy and list every external script source they load, and inventory the Chrome extensions installed in developer mode on managed browsers; a browser-resident implant leaves nothing on the endpoint for file-based tools to find.
