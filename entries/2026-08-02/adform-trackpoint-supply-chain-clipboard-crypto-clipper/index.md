---
schema: 1
kind: incident
title: "Adform: the shared tracking script every customer site embeds was trojanised with a clipboard-rewriting crypto-clipper, and no antivirus engine flagged it"
headline: "A European ad-tech vendor served malware to its customers' visitors through the one JavaScript file they all embed"
summary: >
  Adform, a Copenhagen-headquartered advertising-technology platform, confirmed that malicious code on its
  platform rewrote Bitcoin, Ethereum and Tron wallet addresses copied to visitors' clipboards. Reporting on the
  captured sample identifies the compromised asset as trackpoint-async.js, the tracking library served from
  s2.adform.net that customer sites can deploy across an entire website, with two obfuscated blocks appended to
  the legitimate file. Adform detected the activity on 2026-07-27 and names that day as the affected date; the
  researcher who found it describes about a week, and an archived copy from 2026-07-26 supports the longer read.
  Any organisation whose public website embeds Adform tags served this payload to its own visitors, and the
  sample carried no antivirus detections.
discovered_at: "2026-08-02T04:09:57Z"
event_date: "2026-07-27"
run_id: 2026-08-02T0409Z-intel
priority: high
immediate_action: null
tags: [supply-chain, cryptocrime, data-breach]
regions: [europe, global]
sectors: [technology, finance, public-sector]
entities: [incident:adform-supply-chain-crypto-clipper-2026-07]
techniques: [T1195.002, T1189, T1059.007, T1115, T1657]
affected_products: ["Adform trackpoint-async.js"]
cves: []
sources:
  - url: "https://site.adform.com/resources/newsroom/security-incident-company-update/"
    publisher: "Adform"
    date: "2026-07-31"
    role: primary
  - url: "https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html"
    publisher: "The Hacker News"
    date: "2026-08-01"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/online-ad-firm-adforms-script-compromised-to-steal-cryptocurrency/"
    publisher: "BleepingComputer"
    date: "2026-07-31"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The malicious code was designed to interfere with certain cryptocurrency transactions involving Bitcoin, Ethereum, or Tron by attempting to replace a cryptocurrency wallet address copied to a user’s clipboard with a different address."
    publisher: "Adform"
  - quote: "Based on our investigation to date, we have found no evidence that the malicious code transmitted users’ IP addresses or information about the websites they visited to an external party. Technical analysis indicates that such transmission may have been possible, and this aspect remains under investigation."
    publisher: "Adform"
  - quote: "The public timeline is unresolved. Adform's notice identifies July 27 as the affected date; Kevin Beaumont says he saw malicious activity via Adform over the past week."
    publisher: "The Hacker News"
verification: multi-source
sourcing_note: >
  Adform's own incident notice is the primary and is the only source for the containment timeline and the
  company's position on data transmission. The payload mechanics come from The Hacker News' analysis of a
  captured sample and from BleepingComputer's independent analysis of an archived copy; the discovery and the
  week-long duration estimate are attributed to researcher Kevin Beaumont via those two outlets rather than to
  Adform, which has not endorsed them.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Search public-facing web properties for Adform tag deployments loading trackpoint-async.js from s2.adform.net, and for any that carried it at any point in the week ending 2026-07-27 decide whether visitor notification is warranted — scope to the researcher's week-long window rather than the vendor's single affected day, which the two have not reconciled, and note that Adform's own guidance is that the altered file may persist in visitors' browser caches after the fix."
migrated_from: null
---

Adform, an advertising-technology platform headquartered in Copenhagen, has confirmed a compromise of its platform in which, in the company's own words, the code "was designed to interfere with certain cryptocurrency transactions involving Bitcoin, Ethereum, or Tron by attempting to replace a cryptocurrency wallet address copied to a user's clipboard with a different address"; it says it detected the activity on 2026-07-27, contained the incident, removed the malicious code and reported it to the authorities ([Adform, 2026-07-31](https://site.adform.com/resources/newsroom/security-incident-company-update/)). Adform's notice does not identify the affected asset. That identification comes from the reporting: independent researcher Kevin Beaumont discovered the compromise and traced it to `trackpoint-async.js`, Adform's JavaScript tracking script served from `s2.adform.net` and embedded in websites using the platform ([BleepingComputer, 2026-07-31](https://www.bleepingcomputer.com/news/security/online-ad-firm-adforms-script-compromised-to-steal-cryptocurrency/)). Adform's implementation documentation allows that tag to run on one page, several sections, or unconditionally across an entire website, and compromising the shared resource is what gave the attackers a route onto unrelated downstream sites without breaching any of them individually ([The Hacker News, 2026-08-01](https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html)).

The captured sample carries two malicious blocks appended to the end of the legitimate library, their replacement strings obfuscated with a six-byte XOR key. The first watches for the copy event, polls the clipboard every four seconds and substitutes matching addresses; the second walks the document's text nodes, rewrites values in `input`, `textarea` and `contenteditable` elements, restores the cursor position afterwards, and hooks the value setter on input and textarea elements so that programmatic writes are rewritten in transit — it also intercepts copy, cut, paste and input events, so clipboard copying was never the only path to replacement ([The Hacker News, 2026-08-01](https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html)). Beaumont's description of the user experience is the operationally important part: "Even if you notice the address is wrong and recopy the wallet, it keeps replacing it" ([The Hacker News, 2026-08-01](https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html)). BleepingComputer separately analysed an archived copy and confirmed a self-executing obfuscated payload appended to the legitimate library, including a function that replaced any string matching a wallet-address format and logic that rewrote addresses displayed on the page ([BleepingComputer, 2026-07-31](https://www.bleepingcomputer.com/news/security/online-ad-firm-adforms-script-compromised-to-steal-cryptocurrency/)). At the time of the researcher's report the file returned no detections on VirusTotal ([The Hacker News, 2026-08-01](https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html)).

Two questions are openly contested and defenders should not resolve them in Adform's favour by default. On duration, Adform's notice says the incident "may have affected individuals who visited a website using the affected Adform technology on 27 July 2026", a single day ([Adform, 2026-07-31](https://site.adform.com/resources/newsroom/security-incident-company-update/)), while Beaumont says the activity had run for about the preceding week and the oldest sample BleepingComputer could locate came from an archived snapshot taken on 2026-07-26 at 23:29 GMT ([BleepingComputer, 2026-07-31](https://www.bleepingcomputer.com/news/security/online-ad-firm-adforms-script-compromised-to-steal-cryptocurrency/)); The Hacker News states plainly that "The public timeline is unresolved." ([The Hacker News, 2026-08-01](https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html)). On data egress, Adform reports "no evidence that the malicious code transmitted users' IP addresses or information about the websites they visited to an external party" while conceding that "Technical analysis indicates that such transmission may have been possible." ([Adform, 2026-07-31](https://site.adform.com/resources/newsroom/security-incident-company-update/)); the analysed sample contains a request on page load built to send the hostname and path of the page the visitor is on to an external server, though whether it reached the operator is not established by the sample alone ([The Hacker News, 2026-08-01](https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html)). Adform has published no indicators of compromise, has not said how the attackers reached its deployment path, and has not identified the attacker; The Hacker News notes the more useful missing figure is how many page loads actually received the altered resource, which the company has not disclosed ([The Hacker News, 2026-08-01](https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html)).

Detection concepts follow directly from the mechanism, and the honest starting point is that the server-side victim organisation has almost no native telemetry here — the payload executes in the visitor's browser, not on the operator's infrastructure. The vantage that would have fired is a restrictive Content-Security-Policy with a `connect-src` allowlist and violation reporting on any page embedding third-party tags: the injected block's outbound request to infrastructure outside the vendor's documented endpoints is a reportable violation the moment it is attempted. On managed endpoints, browser-process egress telemetry showing connections to destinations outside a tag vendor's published endpoint list while that vendor's script is loaded is the equivalent network-side signal. **Triage:** legitimate ad and analytics tags make outbound beacon and XHR calls constantly, so the call itself discriminates nothing — what no legitimate tracking pixel needs to do is mutate clipboard contents or rewrite the value of form input elements, and a tag script hooking `copy`, `cut`, `paste` and input-value setters is the behaviour that separates this from ordinary telemetry. Hardening: Subresource Integrity hashes on statically versioned third-party scripts break loudly the moment a vendor-hosted asset is modified server-side, and are worth requesting from any tag supplier that does not currently offer a pinnable, hashable asset; where SRI is not available a restrictive CSP bounds the blast radius rather than preventing the substitution itself.

**Defender takeaway:** the exposure this creates for a public-sector or critical-infrastructure operator is not to its own network but to the people who visit its website — for roughly a week, by the researcher's account, any site carrying the tag was the delivery mechanism for the compromise of its own visitors. Adform's own scale disclosure gives a sense of the deployment footprint rather than the incident's: its 2025 annual report records roughly 1,800 customers and ads served or transacted in more than 180 countries during 2025, figures The Hacker News is careful to note "describe the platform, not this incident" ([The Hacker News, 2026-08-01](https://thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html)). The transferable lesson is the same one this week's third-party-mediated incidents keep producing: a supplier's shared, unversioned, unpinned asset embedded across an entire site is a code-execution grant to that supplier, renewed on every page load.
