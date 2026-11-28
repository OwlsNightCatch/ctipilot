---
schema: 1
kind: threat
title: "Dahua cameras and recorders: CERT-UA warns that attackers take devices over through the Easy4IP cloud relay even when no port is exposed, then view video, change configuration and add accounts"
headline: "CERT-UA: Dahua cameras are taken over through the Easy4IP cloud even with no port exposed; turn P2P off"
summary: >
  Ukraine's CERT-UA reports, in an alert dated 2026-10-23, compromises of Dahua IP cameras and video recorders in which attackers viewed the
  stream, changed device settings and created accounts of their own. The main vector is Easy4IP, Dahua's peer-to-peer remote-access feature,
  which reaches a device through Dahua's cloud by its guessable serial number without any published port; passwords are then guessed or, CERT-UA
  says, the 2021 authentication-bypass flaws CVE-2021-33044 and CVE-2021-33045 are used on outdated firmware, a use eSecurity Planet says is unconfirmed in these cases.
discovered_at: "2026-11-02T03:46:20Z"
updated_at: null
event_date: "2026-10-23"
run_id: 2026-11-02T0256Z-intel
priority: notable
immediate_action: null
tags: [actively-exploited, auth-bypass, cisa-kev, patch-available]
regions: [europe]
sectors: []
entities: ["campaign:dahua-easy4ip-p2p-camera-takeover-2026-10", "product:dahua-ip-camera", "product:dahua-nvr", "product:dahua-dvr", "product:dahua-easy4ip"]
techniques: [T1190, T1110.001, T1136.001, T1125, T1133]
affected_products: ["Dahua IP Camera", "Dahua NVR", "Dahua DVR", "Dahua Easy4IP"]
cves:
  - id: CVE-2021-33044
    cvss: "8.1 (CVSS 3, as stated by Dahua)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Dahua camera, intercom, access-control and recorder series listed in advisory DHCC-SA-202106-001, on firmware older than the fixed builds"
    fixed: "model-specific firmware builds dated June to August 2021, listed per model in DHCC-SA-202106-001"
  - id: CVE-2021-33045
    cvss: "8.1 (CVSS 3, as stated by Dahua)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Dahua camera, intercom, access-control and recorder series listed in advisory DHCC-SA-202106-001, on firmware older than the fixed builds"
    fixed: "model-specific firmware builds dated June to August 2021, listed per model in DHCC-SA-202106-001"
sources:
  - url: "https://cip.gov.ua/ua/news/khakeri-mozhut-otrimati-kontrol-nad-kamerami-ta-videoreyestratorami-cherez-khmarnii-dostup"
    publisher: "CERT-UA (State Service of Special Communications and Information Protection of Ukraine)"
    date: "2026-10-23"
    role: primary
  - url: "https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html"
    publisher: "The Hacker News"
    date: "2026-10-27"
    role: corroborating
  - url: "https://securityaffairs.com/201827/hacking/attackers-take-control-of-dahua-cameras-and-video-recorders-via-easy4ip.html"
    publisher: "Security Affairs"
    date: "2026-10-27"
    role: corroborating
  - url: "https://www.esecurityplanet.com/news/dahua-camera-cloud-access-attacks-emea-ukraine/"
    publisher: "eSecurity Planet"
    date: "2026-10-27"
    role: corroborating
  - url: "https://www.dahuasecurity.com/about-dahua/trust-center/dahua-psirt/dhcc-sa-202106-001:security-advisory---identity-authentication-bypass-vulnerability-found-in-some-dahua-products"
    publisher: "Dahua Technology (DHCC-SA-202106-001)"
    date: "2021-11-15"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Cases of compromising IP cameras and DVRs with access to the video stream, changing the device configuration and creating third-party accounts have been recorded"
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html"
  - quote: "CERT-UA warns that devices with Easy4IP enabled may be vulnerable even when they cannot be accessed directly from the internet."
    publisher: "Security Affairs"
    source_url: "https://securityaffairs.com/201827/hacking/attackers-take-control-of-dahua-cameras-and-video-recorders-via-easy4ip.html"
  - quote: "Audit logs containing authentication events using the manufacturer's native protocol (DVRIP) and from a local address (127.0.0.1), a sign of P2P access."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html"
  - quote: "using a combination of credential brute-force attacks and the exploitation of the CVE-2021-33044-CVE-2021-33045 chain."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html"
  - quote: "although their use in the October incidents remains unconfirmed."
    publisher: "eSecurity Planet"
    source_url: "https://www.esecurityplanet.com/news/dahua-camera-cloud-access-attacks-emea-ukraine/"
verification: single-source-national-cert
sourcing_note: >
  CERT-UA's alert is the only account of the October compromises; its page carries no date in its text, so 2026-10-23 is Security Affairs' dating, and The Hacker News, Security Affairs and eSecurity Planet restate it, which makes the three pieces one assessor with three
  publishers. The CVSS score and the fixed firmware come from Dahua's 2021 advisory; the exploitation of the two flaws in October is stated by
  CERT-UA as a route, while eSecurity Planet says their use in the October cases is unconfirmed and The Hacker News ties them to Hunt.io's
  earlier camera campaign.
confidence: medium
references:
  - 2026-07-13/russia-ip-camera-hijacking-nato-military-supply-routes
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Turn off Easy4IP (P2P cloud access) on every Dahua camera and recorder that does not need it, and search each device's audit log for DVRIP logins from 127.0.0.1."
updates: []
migrated_from: null
---

CERT-UA's alert ([CERT-UA, 2026-10-23](https://cip.gov.ua/ua/news/khakeri-mozhut-otrimati-kontrol-nad-kamerami-ta-videoreyestratorami-cherez-khmarnii-dostup); dated 2026-10-23 by [Security Affairs, 2026-10-27](https://securityaffairs.com/201827/hacking/attackers-take-control-of-dahua-cameras-and-video-recorders-via-easy4ip.html)) reports recorded compromises of Dahua IP cameras and DVRs in which attackers had the video stream, changed the device configuration and created accounts of their own ([The Hacker News, 2026-10-27](https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html)). The main vector is Easy4IP, Dahua's peer-to-peer remote-access feature: a device with it enabled opens an outbound connection to Dahua's cloud and registers by serial number, and access then runs through the cloud, bypassing NAT and firewall, with no published port and no public address ([CERT-UA, 2026-10-23](https://cip.gov.ua/ua/news/khakeri-mozhut-otrimati-kontrol-nad-kamerami-ta-videoreyestratorami-cherez-khmarnii-dostup); [Security Affairs, 2026-10-27](https://securityaffairs.com/201827/hacking/attackers-take-control-of-dahua-cameras-and-video-recorders-via-easy4ip.html)). Serial numbers follow a predictable pattern, a 10-character model prefix and a five-character hexadecimal counter that rises almost sequentially, so attackers can guess them at scale and learn which devices are cloud-connected without hitting rate limits ([The Hacker News, 2026-10-27](https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html)). Authentication is then beaten with weak or known passwords or with the authentication-bypass flaws CVE-2021-33044 and CVE-2021-33045 in outdated firmware, which CISA added to its Known Exploited Vulnerabilities catalogue on 2024-08-21, although their use in the October cases remains unconfirmed ([eSecurity Planet, 2026-10-27](https://www.esecurityplanet.com/news/dahua-camera-cloud-access-attacks-emea-ukraine/)). Dahua fixed both in 2021 with model-specific firmware builds and rates them CVSS 8.1 ([Dahua, 2021-11-15](https://www.dahuasecurity.com/about-dahua/trust-center/dahua-psirt/dhcc-sa-202106-001:security-advisory---identity-authentication-bypass-vulnerability-found-in-some-dahua-products)). CERT-UA does not say who was targeted, how many devices are affected or who is behind the activity ([The Hacker News, 2026-10-27](https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html)).

The Hacker News says the activity shares similarities with Hunt.io's earlier Operation CameraSwarm, which reported more than 14,530 Dahua cameras compromised between 2026-06-17 and 2026-07-22 with brute-forced credentials and the same two-flaw chain, nearly 2,000 of them given a backdoor account that survives a password change and, on most firmware, a factory reset ([The Hacker News, 2026-10-27](https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html)); eSecurity Planet says no connection to the October incidents has been established ([eSecurity Planet, 2026-10-27](https://www.esecurityplanet.com/news/dahua-camera-cloud-access-attacks-emea-ukraine/)). Dutch intelligence services warned in July that Russian state actors compromise IP cameras to collect intelligence on military transports ([The Hacker News, 2026-10-27](https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html)).

**Exposure:** any Dahua IP camera, NVR or DVR with Easy4IP enabled, whether or not it has a public address; CERT-UA warns that such devices may be vulnerable even when they cannot be reached directly from the internet ([Security Affairs, 2026-10-27](https://securityaffairs.com/201827/hacking/attackers-take-control-of-dahua-cameras-and-video-recorders-via-easy4ip.html)).

**Detection:** in each device's audit log, DVRIP authentication events from the local address 127.0.0.1, which CERT-UA reads as a sign of access through the P2P cloud, plus accounts nobody created and unauthorized configuration changes; text overlaid on the video image is another sign, but its absence proves nothing ([The Hacker News, 2026-10-27](https://thehackernews.com/2026/10/attackers-hijack-dahua-ip-cameras-in.html); [Security Affairs, 2026-10-27](https://securityaffairs.com/201827/hacking/attackers-take-control-of-dahua-cameras-and-video-recorders-via-easy4ip.html)).

**Triage:** a login from 127.0.0.1 shows only that the session arrived through the P2P relay, so where staff or an installer legitimately use Easy4IP it is normal; the account name, the time and the configuration change that follows separate the two.

**Defender takeaway:** turn Easy4IP off wherever it is not needed, keep cameras off the internet and reach them through a VPN limited to authorized addresses, review the account list and the cloud accounts linked to each device, and update the firmware by hand, CERT-UA's four steps ([CERT-UA, 2026-10-23](https://cip.gov.ua/ua/news/khakeri-mozhut-otrimati-kontrol-nad-kamerami-ta-videoreyestratorami-cherez-khmarnii-dostup); [Security Affairs, 2026-10-27](https://securityaffairs.com/201827/hacking/attackers-take-control-of-dahua-cameras-and-video-recorders-via-easy4ip.html)); check all Dahua devices on the network, forgotten ones included ([Security Affairs, 2026-10-27](https://securityaffairs.com/201827/hacking/attackers-take-control-of-dahua-cameras-and-video-recorders-via-easy4ip.html)), and do not count on a password on outdated firmware, since those flaws make knowing it unnecessary ([CERT-UA, 2026-10-23](https://cip.gov.ua/ua/news/khakeri-mozhut-otrimati-kontrol-nad-kamerami-ta-videoreyestratorami-cherez-khmarnii-dostup)).
