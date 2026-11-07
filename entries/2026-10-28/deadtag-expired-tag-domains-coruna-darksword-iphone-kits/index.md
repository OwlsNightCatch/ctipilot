---
schema: 1
kind: threat
title: "DeadTag: re-registered domains of defunct analytics and advertising tags redirect visitors of thousands of sites, among them to a page that serves the Coruna and DarkSword iPhone exploit kits, which compromise a vulnerable device when the page opens"
headline: "DeadTag: expired tag domains send visitors to iPhone exploit kits; opening the page is enough on vulnerable iOS"
summary: >
  Report URI and iVerify report that an operator they call DeadTag buys the expired domains of old analytics and advertising tags that
  thousands of websites still load, so every page that carries the tag runs the operator's script, and sells the visitors on; Report URI
  counts more than 660 re-registered domains. For chosen iPhone visitors one chain ends at a page that serves the Coruna kit to iOS 13 to
  17.2.1 and a modified DarkSword kit to iOS 18.4 to 18.7, both of which attack the browser itself, so that opening the page compromises a
  vulnerable device and steals keychain passwords and crypto-wallet data.
discovered_at: "2026-10-28T03:54:00Z"
updated_at: null
event_date: "2026-10-22"
run_id: 2026-10-28T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, mobile, cryptocrime]
regions: [global, europe]
sectors: []
entities: ["campaign:deadtag", "tool:coruna", "tool:darksword"]
techniques: [T1584.001, T1189, T1203, T1555.001]
affected_products: ["Apple iOS"]
cves: []
sources:
  - url: "https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/"
    publisher: "Report URI (Scott Helme)"
    date: "2026-10-22"
    role: primary
  - url: "https://www.iverify.com/blog/malvertising-coruna-darksword-iphone-exploits"
    publisher: "iVerify Threat Intelligence Team"
    date: "2026-10-21"
    role: primary
closed_sources: []
evidence:
  - quote: "Attackers are buying up the expired domains behind old analytics and advertising tags that thousands of websites still load, and they're selling the visitors those tags bring in."
    publisher: "Report URI (Scott Helme)"
    source_url: "https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/"
  - quote: "Simply opening the page is enough for your device to be compromised."
    publisher: "Report URI (Scott Helme)"
    source_url: "https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/"
  - quote: "Audit your third-party tags."
    publisher: "Report URI (Scott Helme)"
    source_url: "https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/"
  - quote: "Based on current findings, DeadTag appears to be mostly focused on European domains versus .com"
    publisher: "iVerify Threat Intelligence Team"
    source_url: "https://www.iverify.com/blog/malvertising-coruna-darksword-iphone-exploits"
  - quote: "iVerify caught the P7 variant of DarkSword delivered through a malicious Instagram ad themed around the World Cup."
    publisher: "iVerify Threat Intelligence Team"
    source_url: "https://www.iverify.com/blog/malvertising-coruna-darksword-iphone-exploits"
verification: multi-source
sourcing_note: >
  Report URI (web-delivery side) and iVerify (device side) published jointly and each from its own telemetry, so the two are one joint account
  with two vantage points rather than independent confirmation. Report URI's count of domains and its estimate of 135 million visits a month are
  its own and are stated as cautious; neither source attributes DeadTag, and Report URI reads the operator of the exploit kits as at least
  Chinese-speaking from code comments and infrastructure.
confidence: high
references: ["2026-09-30/star-blizzard-redflick-cosmicpulse-single-click-chain", "2026-09-13/gtg-20006-anthropic-russia-ai-orchestrated-espionage"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "List every third-party script domain on the public websites your organisation, its agencies and its hosting suppliers run, and remove or re-verify each whose provider has shut down, because DeadTag buys exactly those expired domains."
updates: []
migrated_from: null
---

Report URI and iVerify describe a campaign they name DeadTag: attackers buy the expired domains behind old analytics and advertising tags that thousands of websites still load, so every page that still carries the tag runs the operator's script without the site owner changing or noticing anything, and the operator sells the visitors those tags bring in ([Report URI, 2026-10-22](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)). Report URI has identified more than 660 re-registered domains still embedded on thousands of sites and cautiously estimates 135 million visits a month ([Report URI, 2026-10-22](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)). The script is about 2 KB, does nothing for search engines, scanners and other bots, asks the operator's server what to do with each visitor and redirects the chosen ones, and Report URI found that the operator stopped answering when it probed from data-centre addresses or returned too often from residential ones; destinations include scam pages, a fake VPN pop-up and, for iPhones, a page that serves two exploit kits ([Report URI, 2026-10-22](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)).

One chain ends at a fake prediction-market page that picks the kit by the visitor's iOS version, Coruna for iOS 13 to 17.2.1 and a modified "P7" variant of DarkSword for iOS 18.4 to 18.7; both attack the browser itself, so opening the page is enough to compromise a vulnerable device, and the spyware they install steals keychain passwords, crypto-wallet app data and device and account information and reports to one server; Report URI notes that Coruna and DarkSword are separate exploit kits that have been seen in different campaigns, and that here both send their stolen data to the same server, which it reads as one operator running both ([Report URI, 2026-10-22](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)). iVerify reads DeadTag as mostly focused on European domains rather than .com ([iVerify, 2026-10-21](https://www.iverify.com/blog/malvertising-coruna-darksword-iphone-exploits)), and saw the P7 variant reach an employee's device at a customer organisation through a malicious Instagram ad while the employee was scrolling in the app ([iVerify, 2026-10-21](https://www.iverify.com/blog/malvertising-coruna-darksword-iphone-exploits)). The kit operator does not rely on DeadTag alone: Report URI found DarkSword loaders on hundreds of online shops on one e-commerce platform, PrestaShop ([Report URI, 2026-10-22](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)).

**Exposure:** any public website that still loads a script from a third-party domain whose provider no longer operates it, where the browser fetches nothing useful and the page looks normal, and any iPhone on iOS 13 to 17.2.1 or 18.4 to 18.7 that opens such a page ([Report URI, 2026-10-22](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)).

**Detection:** inventory the external script references of each public site and flag any whose domain has been re-registered or no longer belongs to its provider; Report URI recommends script monitoring that shows when a new script or domain appears on a page, and a Content Security Policy that controls which domains a site may load code from ([Report URI, 2026-10-22](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)). A security scanner usually sees only an empty response from the malicious script, because the operator answers only selected visitors.

**Defender takeaway:** remove dead third-party tags from every site you run, enforce a Content Security Policy and keep iPhones on the current iOS, with Lockdown Mode for people who may be targeted; for an iPhone that may have opened an affected page, Report URI advises restarting it, changing the passwords stored in its keychain and moving crypto assets to a new wallet ([Report URI, 2026-10-22](https://blog.report-uri.com/deadtag-how-forgotten-website-tags-became-a-delivery-network-for-iphone-spyware/)).
