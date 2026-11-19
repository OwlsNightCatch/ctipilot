---
schema: 1
kind: threat
title: "OptimJack: poisoned scripts served by Optimizely, Kissmetrics, StorifyMe and minute-ly route iPhones to exploit-kit stages, the Optimizely files also carry a crypto clipper and card skimmer, and the University of Basel site loaded a poisoned StorifyMe widget on 2026-11-14"
headline: "OptimJack: Optimizely names the exploited signup-flow flaw; Report URI counts 178 organisations, Zscaler 450+ domains"
summary: >
  Optimizely says an unauthorized party exploited a flaw in its Web Experimentation account signup flow to impersonate users and add malicious JavaScript to some customer projects, fewer than 5% of its customers, and Report URI counts 178 organisations that served the code on 2026-11-16 while Zscaler ThreatLabz counts more than 450 domains; the Optimizely files carry a crypto clipper and card skimmer. Ohey reports that scripts served by Kissmetrics and StorifyMe gained a loader from 2026-11-13 that routes iPhones to the Coruna and DarkSword exploit-kit stages and that minute-ly's loader was replaced outright; Hudson Rock names 21 web properties, among them the University of Basel's StorifyMe widget, and calls the iPhone stages delivery observations, not confirmed compromises. How the Kissmetrics, StorifyMe and minute-ly files were altered is unknown.
discovered_at: "2026-11-17T04:38:00Z"
updated_at: "2026-11-19T05:06:52Z"
event_date: "2026-11-13"
run_id: 2026-11-17T0355Z-intel
priority: high
immediate_action: null
tags: [supply-chain, cryptocrime, mobile]
regions: [global, switzerland]
sectors: [education, finance, media, technology]
entities: ["campaign:optimjack-poisoned-vendor-scripts-2026-11", "tool:coruna", "tool:darksword"]
techniques: [T1195.002, T1190, T1189, T1059.007, T1115, T1565.002, T1056, T1539, T1113, T1657]
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
  - url: "https://status.optimizely.com/incidents/ftw0fh9wx43z"
    publisher: "Optimizely status page"
    date: "2026-11-18"
    role: primary
  - url: "https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/"
    publisher: "Report URI Blog (Scott Helme)"
    date: "2026-11-16"
    role: corroborating
  - url: "https://www.zscaler.com/blogs/security-research/attackers-exploit-optimizely-flaw-inject-malicious-javascript"
    publisher: "Zscaler ThreatLabz"
    date: "2026-11-18"
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
  - quote: "an unauthorized party exploited a vulnerability in Experimentation and used it to add malicious JavaScript to some customer projects."
    publisher: "Optimizely status page"
    source_url: "https://status.optimizely.com/incidents/ftw0fh9wx43z"
  - quote: "The real number is likely higher as we could only check snippets we could find in time."
    publisher: "Report URI Blog (Scott Helme)"
    source_url: "https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/"
  - quote: "Cards entered in hosted payment iframes (Stripe, Adyen and similar) were out of its reach."
    publisher: "Report URI Blog (Scott Helme)"
    source_url: "https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/"
  - quote: "On 16 November 2026, an unauthorized third party exploited a flaw in the Optimizely Web Experimentation account signup flow."
    publisher: "Optimizely status page"
    source_url: "https://status.optimizely.com/incidents/ftw0fh9wx43z"
  - quote: "ThreatLabz identified more than 450 unique domains and more than 3,000 URLs serving the malicious script."
    publisher: "Zscaler ThreatLabz"
    source_url: "https://www.zscaler.com/blogs/security-research/attackers-exploit-optimizely-flaw-inject-malicious-javascript"
verification: multi-source
sourcing_note: >
  Hudson Rock recovered the poisoned files itself and matched the archived responses Ohey supplied; Amirul Cyber and Report URI found the Optimizely injection independently, and Optimizely's own status entry confirms an exploited vulnerability on its side and, since 2026-11-18, names it as a weakness in the Web Experimentation account signup flow that let the attacker impersonate users on targeted accounts. Zscaler ThreatLabz states neither the vantage point nor the time window of its count of more than 450 domains, so it is not reconciled with Report URI's 178 organisations. The sources cite no statement from Kissmetrics, StorifyMe or minute-ly, and the iPhone-router reading of the stages is Ohey's, with Hudson Rock calling them delivery observations only. Ohey's page is a living reference with no dateline of its own, so its citations carry the nominal date 2026-11-17, while its text counts through 2026-11-18.
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
  - "List every page of your organisation's sites, and of the agencies that build them, that has loaded Optimizely project JavaScript since 2026-11-16, or Kissmetrics i.js, a StorifyMe widget or the minute-ly loader since 2026-11-13, capture the bytes the browser receives and compare them with the provider's own project content (a search for the loader's host name misses the variant that hides it in base64), and where a file carries the injected loader remove it, keep the response bytes as evidence and treat the payment, login and form pages that loaded an affected Optimizely file as exposed to card and session theft."
  - "If your organisation or an agency building its sites has an Optimizely Web Experimentation account, audit every Project JavaScript field for code nobody wrote and rotate the API tokens, session tokens and integration keys tied to it, because the attacker impersonated users on targeted accounts to edit that field."
updates:
  - at: "2026-11-18T04:57:41Z"
    run_id: 2026-11-18T0356Z-intel
    type: update
    summary: >
      Optimizely's own status entry says an unauthorized party exploited a vulnerability in
      Experimentation to add the JavaScript to some customer projects, Report URI counts 178
      organisations that served the code on 2026-11-16, and the Optimizely files carried the code from
      2026-11-16 rather than 2026-11-13. The loader also hides in base64 where a host-name search
      misses it.
    fields: [actions, body, evidence, headline, sources, sourcing_note, summary]
  - at: "2026-11-19T05:06:52Z"
    run_id: 2026-11-19T0355Z-intel
    type: update
    summary: >
      Optimizely's status entry now names the flaw, a weakness in the Web Experimentation account signup
      flow used to impersonate users on targeted accounts, and says fewer than 5% of its customers were
      affected; Zscaler ThreatLabz counts more than 450 domains and 3,000 URLs serving the script and
      lists the customer clean-up steps.
    fields: [actions, body, evidence, headline, sources, sourcing_note, summary, techniques]
migrated_from: null
---

Per Ohey, from 2026-11-13 the scripts served by Kissmetrics and StorifyMe gained a few lines that load a small router script for iPhones, and minute-ly's loader was replaced outright ([Ohey, 2026-11-17](https://ohey.ca/threats/ios-exploits/darksword/)). Optimizely's customer project files followed on 2026-11-16, when Report URI saw its first injection at 04:21 UTC and counted 188 infected snippets of 178 organisations, a floor ([Report URI, 2026-11-16](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)). Optimizely says an unauthorized party exploited a flaw in its Web Experimentation account signup flow on 2026-11-16 to impersonate users on targeted customer accounts and insert malicious JavaScript into their projects, that it closed the vulnerability within three hours of detection, that this was not a credentials breach and that fewer than 5% of its customers were affected ([Optimizely, 2026-11-18](https://status.optimizely.com/incidents/ftw0fh9wx43z)); Zscaler ThreatLabz counts more than 450 unique domains and more than 3,000 URLs serving the script ([Zscaler ThreatLabz, 2026-11-18](https://www.zscaler.com/blogs/security-research/attackers-exploit-optimizely-flaw-inject-malicious-javascript)). Hudson Rock names 21 web properties, among them BBC, Zoom, HSBC UAE and the University of Basel ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)). The Basel capture of 2026-11-14 recorded a poisoned StorifyMe web component ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)). How the Kissmetrics, StorifyMe and minute-ly files were altered, who operates the campaign and how many visitors loaded them are unknown ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)).

The financial theft sits in the Optimizely files: Ohey says that on 2026-11-16 they switched to a script that swaps copied wallet addresses and skims card numbers in every browser and adds the router only on iPhones and iPads ([Ohey, 2026-11-17](https://ohey.ca/threats/ios-exploits/darksword/)). Hudson Rock describes the stealer as skimming card number, expiry and CVV from form and fetch POST bodies and sending readable cookies with a page image ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)). In Hudson Rock's reading the router sends iOS 13 to 17 to a Coruna-associated entry and iOS 18 to 25 to a DarkSword-labelled one ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)), and Ohey states that DarkSword attacks iPhones running iOS 18.4 to 18.7.2 through Safari ([Ohey, 2026-11-17](https://ohey.ca/threats/ios-exploits/darksword/)); Hudson Rock calls them delivery observations, not demonstrated compromises ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)). 

**Exposure:** any page that loads Optimizely project JavaScript from cdn.optimizely.com, Kissmetrics i.js, a StorifyMe widget or web component, or the minute-ly loader; Hudson Rock's advice is to verify what visitors actually receive ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)).

**Detection:** web proxy and DNS telemetry for a vendor script that causes a further script load from a host unrelated to the vendor, payment-form POST bodies sent to an unfamiliar host, and response-body diffs of served third-party bundles; Content-Security-Policy script-src violation reports naming unknown hosts, which Amirul Cyber says stopped the payload on two affected sites ([Amirul Cyber, 2026-11-16](https://amirulcyber.com/2026/11/16/optimjack-optimizely-skimmer/)). After removal, review the provider-side project change history, API credentials and integrations, because the poisoned output does not show how the attacker got in ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)); Zscaler advises customers to review recent changes, user activity, account creation events and administrative access in the Optimizely account ([Zscaler ThreatLabz, 2026-11-18](https://www.zscaler.com/blogs/security-research/attackers-exploit-optimizely-flaw-inject-malicious-javascript)).

**Defender takeaway:** inventory third-party scripts on public, payment and e-government pages now and verify what each serves; a DNS or network block alone does not remove the poisoned trusted script ([Hudson Rock, 2026-11-16](https://www.infostealers.com/article/poisoned-scripts-on-bbc-zoom-and-other-major-websites-linked-to-iphone-exploit-loaders/)), so keep the evidence, remove the file and set an allow-listed script-src policy.

## Update — 2026-11-18T04:57:41Z

Optimizely says an unauthorized party exploited a vulnerability in Experimentation and used it to add malicious JavaScript to some customer projects, that it has fixed the vulnerability and removed the injected code, and that it secured affected user accounts; that post named no flaw class, CVE or count, and the status entry's later post of 2026-11-18 is described below ([Optimizely, 2026-11-18](https://status.optimizely.com/incidents/ftw0fh9wx43z)). The status entry covers the Optimizely files only; how the Kissmetrics, StorifyMe and minute-ly scripts were reached is still unknown.

Report URI's timeline adds that the card skimmer was added to the clipper at 13:43 UTC on 2026-11-16, that a mass clean-up ran between about 20:40 and 21:10 UTC, and that a snippet cleaned and then re-infected shows the writer still had access at that point ([Report URI, 2026-11-16](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)). Contradiction on dates: Ohey puts the change to the Optimizely project files at 2026-11-13 together with the Kissmetrics and StorifyMe scripts ([Ohey, 2026-11-17](https://ohey.ca/threats/ios-exploits/darksword/)), while Report URI's first Optimizely injection is at 04:21 UTC on 2026-11-16; Report URI's logged first-hand record is the better dated one, and the earlier Kissmetrics, StorifyMe and minute-ly wave is not in the 178 ([Report URI, 2026-11-16](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)).

The injected loader came in three forms: a plain script tag, the same address hidden in base64 and decoded with atob(), which a search for the host name misses, and a full inline copy that runs through eval ([Report URI, 2026-11-16](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)). Cards entered in hosted payment iframes were out of the skimmer's reach, while cards typed into a site's own form fields were not ([Report URI, 2026-11-16](https://blog.report-uri.com/worlds-largest-brands-infected-with-malware-via-optimizely/)).

## Update — 2026-11-19T05:06:52Z

Optimizely's status entry now says that on 2026-11-16 an unauthorized third party exploited a flaw in the Optimizely Web Experimentation account signup flow to impersonate users on targeted customer accounts and insert malicious JavaScript into their projects, that it detected the activity the same day, blocked delivery and closed the vulnerability within three hours of detection, that this was not a credentials breach, that the incident was limited to Web Experimentation and that fewer than 5% of its customers were affected; it gives no CVE and no absolute count ([Optimizely, 2026-11-18](https://status.optimizely.com/incidents/ftw0fh9wx43z)). Zscaler ThreatLabz says the flaw let the attacker edit the project JavaScript field and counts more than 450 unique domains and more than 3,000 URLs serving the malicious script, without stating its vantage point or time window, so the figure is not reconciled with Report URI's 178 organisations ([Zscaler ThreatLabz, 2026-11-18](https://www.zscaler.com/blogs/security-research/attackers-exploit-optimizely-flaw-inject-malicious-javascript)). It advises customers to review recent changes, user activity, account creation events and administrative access, to audit all Project JavaScript fields for unauthorized or unexpected code and to rotate the API tokens, session tokens and integration keys associated with Optimizely ([Zscaler ThreatLabz, 2026-11-18](https://www.zscaler.com/blogs/security-research/attackers-exploit-optimizely-flaw-inject-malicious-javascript)).
