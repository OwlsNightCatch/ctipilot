---
schema: 1
kind: threat
title: "A fake WatchGuard VPN download site captures the SSL VPN server, login and password in the browser and then serves the genuine signed installer, leaving no malicious file for endpoint tools to flag"
headline: "Huntress: a lookalike VPN-client site harvests credentials, then hands over the real signed installer"
summary: >
  Huntress describes a lookalike WatchGuard VPN download site, reached on 2026-10-07 by an administrator at a managed service provider through a Bing search result, that asks for the SSL VPN server, login and password,
  rejects the first submission so the victim types again, and only then downloads the genuine, validly signed WatchGuard installer from WatchGuard's own CDN. No malware is delivered, so endpoint controls have no file to flag, and few reputation engines flagged the domains.
discovered_at: "2026-10-15T03:43:00Z"
updated_at: null
event_date: "2026-10-13"
run_id: 2026-10-15T0256Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity]
regions: [global]
sectors: [technology]
entities: ["product:watchguard-mobile-vpn-with-ssl"]
techniques: [T1608.006, T1583.001, T1204.001]
affected_products: ["WatchGuard Mobile VPN with SSL"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing"
    publisher: "Huntress"
    date: "2026-10-13"
    role: primary
closed_sources: []
evidence:
  - quote: "Rather than downloading a fake client, the domain instead downloads a genuine, validly signed WatchGuard installer."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing"
  - quote: "The legitimate Mobile VPN with SSL client also asks for these three values when users connect, so the prompt looks reasonable."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing"
verification: single-source
sourcing_note: >
  Huntress, whose SOC investigated the incident, is the only source for this campaign iteration; its account of the January 2026 WatchGuard Secplicity report and the March 2026 Microsoft Threat Intelligence report on earlier iterations is relayed from its own page, not read at those sources.
  Huntress does not attribute this iteration to a named actor and says the evidence does not establish whether the same operators controlled the domain in January.
confidence: medium
references: []
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

Huntress's SOC investigated an incident on 2026-10-07 in which an administrator at a managed service provider searched Bing for a WatchGuard VPN download with a typo in the query and clicked through the standard Bing result redirect to a lookalike site titled "WatchGuard Firebox VPN Client", which Huntress classes as search-engine poisoning rather than malvertising ([Huntress, 2026-10-13](https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing)). Choosing any download option opens a pop-up asking for Server, Login and Password; one unobfuscated JavaScript file of about 150 lines posts the typed values as JSON to a separate collector domain, tagged as the first or second attempt, and always rejects the first submission with an "incorrect data" message so that the victim types again or tries a second set of credentials ([Huntress, 2026-10-13](https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing)). Only after the second submission does the page fetch the real WatchGuard Mobile VPN with SSL installer from WatchGuard's own CDN, an Authenticode-signed file whose digest Huntress recomputed and found unmodified, so there is no trojanized installer or malicious DLL for endpoint defenses to flag ([Huntress, 2026-10-13](https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing)). The victim's browser history showed no download in the observed window, so Huntress judges the user probably did not finish both rounds but may have typed credentials in the first, and Managed Defender flagged the incident 21 seconds after the lookalike domain loaded ([Huntress, 2026-10-13](https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing)). Both domains were registered within the previous two months, few reputation engines flagged either as of 2026-10-08, and the lure domain was offline by 2026-10-13 ([Huntress, 2026-10-13](https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing)). Huntress places the iteration in a campaign that WatchGuard's Secplicity team described in January 2026 as lookalike download sites for WatchGuard, F5, Fortinet, SonicWall and Sophos clients, and that Microsoft tied in March 2026 to a financially motivated actor it tracks as Storm-2561; the new element is that the fake client is gone from the middle ([Huntress, 2026-10-13](https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing)).

**Exposure:** administrators and users who find an SSL VPN client through a web search, as an administrator at a managed service provider did here; the lure here impersonates WatchGuard, and Huntress describes the same campaign against clients of five vendors ([Huntress, 2026-10-13](https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing)). The credentials of any VPN account typed into such a page, and the gateway address with them, are in the attacker's hands.

**Detection:** no malicious file or process reaches the endpoint, so the signal is in web proxy and DNS telemetry (a visit that arrives from a search-result redirect to a domain that is not the vendor's, followed by a JSON POST to a second, recently registered domain; Huntress's Managed Defender did flag the browsing activity) and in VPN gateway authentication logs; Huntress advises watching for SSL VPN logins from hosting providers, unfamiliar ASNs and countries where the account has never connected ([Huntress, 2026-10-13](https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing)).

**Triage:** a genuine VPN client also asks for server, login and password, but only inside the installed client at connect time; a browser form that collects the three values before any installer has run, on a domain that is not the vendor's, is the signal.

**Defender takeaway:** if a user typed VPN credentials into a page found through search, reset every affected account and treat the VPN endpoint those credentials belong to as known to the attacker; enforce multi-factor authentication on the VPN, and publish and bookmark the official client download links in internal documentation so staff do not search for them ([Huntress, 2026-10-13](https://www.huntress.com/blog/fake-watchguard-vpn-credential-phishing)).
