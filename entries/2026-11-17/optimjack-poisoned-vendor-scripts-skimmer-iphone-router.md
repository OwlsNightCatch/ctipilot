---
schema: 1
kind: threat
title: "OptimJack: poisoned scripts served by Optimizely, Kissmetrics, StorifyMe and minute-ly route iPhones to exploit-kit stages, the Optimizely files also carry a crypto clipper and card skimmer, and the University of Basel site loaded a poisoned StorifyMe widget on 2026-11-14"
headline: "OptimJack: poisoned vendor scripts route iPhones to exploit kits; Optimizely files also skim cards; Basel hit"
summary: >
  Ohey reports that from 2026-11-13 scripts served by Kissmetrics, StorifyMe and Optimizely customer project files gained a loader that routes iPhones to the Coruna and DarkSword exploit-kit stages, and that minute-ly's loader was replaced outright; from 2026-11-16 the Optimizely files also carry a script that swaps cryptocurrency addresses and skims payment cards in every browser. Hudson Rock recovered nine poisoned vendor files, matched archived responses and names 21 web properties, among them the University of Basel's StorifyMe widget; the iPhone stages are delivery observations, not confirmed compromises, and the initial access is unknown.
discovered_at: "2026-11-17T04:38:00Z"
updated_at: null
event_date: "2026-11-13"
run_id: 2026-11-17T0355Z-intel
priority: high
immediate_action: null
tags: [supply-chain, cryptocrime, mobile]
regions: [global, switzerland]
sectors: [education, finance, media, technology]
entities: ["campaign:optimjack-poisoned-vendor-scripts-2026-11", "tool:coruna", "tool:darksword"]
techniques: [T1195.002, T1189, T1059.007, T1115, T1565.002, T1056, T1539, T1113, T1657]
affected_products: ["Optimizely", "Kissmetrics", "StorifyMe", "minute-ly", "Apple iOS"]
cves: []
sources:
  - url: "https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/"
    publisher: "Hudson Rock (InfoStealers)"
    date: "2026-11-16"
    role: primary
  - url: "https://ohey.ca/threats/ios-exploits/darksword/"
    publisher: "Ohey (Kirk), living page"
    date: "2026-11-17"
    role: primary
  - url: "https://amirulcyber.com/2026/11/16/optimjack-optimizely-skimmer/"
    publisher: "Amirul Cyber"
    date: "2026-11-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The confirmed compromise is malicious code inside responses served from third-party providers’ own script and widget endpoints."
    publisher: "Hudson Rock (InfoStealers)"
    source_url: "https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/"
  - quote: "These are delivery observations, not demonstrated iPhone compromises."
    publisher: "Hudson Rock (InfoStealers)"
    source_url: "https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/"
  - quote: "A FAZ capture records a poisoned StorifyMe widget response. Later captures include Sydney Morning Herald, University of Basel and vidaXL."
    publisher: "Hudson Rock (InfoStealers)"
    source_url: "https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/"
  - quote: "A DNS or network block is useful, but it does not remove the poisoned trusted script."
    publisher: "Hudson Rock (InfoStealers)"
    source_url: "https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/"
  - quote: "DarkSword attacks iPhones running iOS 18.4 to 18.7.2 through Safari."
    publisher: "Ohey (Kirk)"
    source_url: "https://ohey.ca/threats/ios-exploits/darksword/"
  - quote: "GitLab's and Zoom's Optimizely files and minute-ly's loader still carried it at 21:10 UTC on 16 November."
    publisher: "Ohey (Kirk)"
    source_url: "https://ohey.ca/threats/ios-exploits/darksword/"
verification: multi-source
sourcing_note: >
  Hudson Rock recovered the poisoned files itself and matched the archived responses Ohey supplied; Amirul Cyber found the Optimizely injection independently. No provider statement had been published or found at the time of writing, and the iPhone-router reading of the stages is Ohey's, with Hudson Rock calling them delivery observations only. Ohey's page is a living reference with no dateline of its own, so its citations carry 2026-11-17, the latest date its text carries.
confidence: medium
references: ["2026-10-28/deadtag-expired-tag-domains-coruna-darksword-iphone-kits", "2026-11-05/apt29-watering-hole-ios-android-n-day-chains-kev"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "List every page of your organisation's sites, and of the agencies that build them, that has loaded Optimizely project JavaScript, Kissmetrics i.js, a StorifyMe widget or the minute-ly loader since 2026-11-13, capture the bytes the browser receives and compare them with the provider's own project content, and where a file carries the injected loader remove it, keep the response bytes as evidence and treat the payment, login and form pages that loaded an affected Optimizely file as exposed to card and session theft."
updates: []
migrated_from: null
---

Per Ohey, from 2026-11-13 the scripts served by Kissmetrics, StorifyMe and Optimizely customer project files gained a few lines that load a small router script for iPhones, and minute-ly's loader was replaced outright ([Ohey, 2026-11-17](https://ohey.ca/threats/ios-exploits/darksword/)). Hudson Rock recovered nine poisoned vendor files itself, eight Optimizely project files and the minute-ly loader, matched 16 archived vendor responses from 15 site captures, and names 21 web properties, among them BBC, Zoom, GitLab's marketing site, HSBC UAE and the University of Basel ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)). The Basel capture, scanned on 2026-11-14 at 03:27 UTC, recorded a poisoned StorifyMe web component ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)). How the files were altered, who operates the campaign and how many visitors loaded them are unknown ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)).

The financial theft sits in the Optimizely files: Ohey says that on 2026-11-16 they switched to a script that swaps copied wallet addresses and skims card numbers in every browser and adds the router only on iPhones and iPads ([Ohey, 2026-11-17](https://ohey.ca/threats/ios-exploits/darksword/)). Hudson Rock describes the stealer as skimming card number, expiry and CVV from form and fetch POST bodies and conditionally sending readable cookies with an image of the page, and says a response that only delivers the router loader establishes the mobile-router path, not the theft modules ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)). The BBC and HSBC UAE Optimizely files also embed a complete fallback copy that runs when the remote fetch fails or takes longer than 2.5 seconds, so blocking the attacker host does not stop the clipper ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)). The router's configured branches, in Hudson Rock's reading of Ohey's captures, send iOS 13 to 17 to a Coruna-associated entry and iOS 18 to 25 to a DarkSword-labelled entry ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)), and Ohey states that DarkSword attacks iPhones running iOS 18.4 to 18.7.2 through Safari ([Ohey, 2026-11-17](https://ohey.ca/threats/ios-exploits/darksword/)); Hudson Rock stresses that these are delivery observations, not demonstrated iPhone compromises ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)). GitLab's and Zoom's Optimizely files and minute-ly's loader still carried the code at 21:10 UTC on 2026-11-16 ([Ohey, 2026-11-17](https://ohey.ca/threats/ios-exploits/darksword/)).

**Exposure:** any page that loads Optimizely project JavaScript from cdn.optimizely.com, Kissmetrics i.js, a StorifyMe widget or web component, or the minute-ly loader; Hudson Rock's advice is to verify what visitors actually receive ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)). Staff iPhones are exposed to stage delivery only on a visit to an affected page.

**Detection:** web proxy and DNS telemetry for a vendor script that causes a further script load from a host unrelated to the vendor, payment-form POST bodies sent to an unfamiliar host, and response-body diffs of served third-party bundles; Content-Security-Policy script-src violation reports naming unknown hosts, which Amirul Cyber says stopped the payload on two affected sites ([Amirul Cyber, 2026-11-16](https://amirulcyber.com/2026/11/16/optimjack-optimizely-skimmer/)). After removal, review the provider-side project change history, API credentials and integrations, because the poisoned output shows an integrity problem, not how the attacker got in ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)).

**Defender takeaway:** inventory third-party scripts on public, payment and e-government pages now and verify what each serves; a DNS or network block alone does not remove the poisoned trusted script ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)), so keep the evidence, remove the file and set an allow-listed script-src policy.
