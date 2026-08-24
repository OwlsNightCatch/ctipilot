---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Four unrelated disclosures this week put the command-and-control rendezvous on infrastructure that resolves correctly and cannot be reputation-blocked — a public blockchain contract, the Google Sheets API, GitHub Gists, an HTTP cache header, and two thousand hijacked WordPress sites"
headline: "The C2 address is now stored somewhere legitimate and attacker-writable, so blocking the destination blocks a service you use"
summary: >
  Red Canary's monthly round-up records that three of the four new entrants to its most-prevalent list
  resolve their command-and-control address from a dead drop rather than a hardcoded domain, and two
  of those read it from a public blockchain smart contract — a technique the round-up notes has been
  documented since 2023 and that it now counts across three of its top ten. Three other publications
  in the same week show the same architecture on non-blockchain carriers: an espionage cluster running
  tasking through the Google Sheets API v4 with a per-victim spreadsheet tab and a second implant
  doing the same job through GitHub Gists; a China-nexus toolset whose families use a shared Google
  Drive folder for operator commands and HTTP cookie and ETag header values as a command channel; and
  a criminal toolkit hosting its payloads, command-and-control and stolen data on roughly 2,000
  compromised WordPress sites rather than on any infrastructure of its own. A prior weekly measured
  the share of malware command-and-control that never asks DNS a question; this is the mirror case —
  the name resolves correctly, to a service the estate has a legitimate reason to reach.
discovered_at: "2026-08-23T23:58:00Z"
event_date: "2026-08-20"
run_id: 2026-08-23T2311Z-weekly
priority: notable
immediate_action: null
tags: [espionage, organized-crime, infostealer, cloud, ransomware]
regions: [global, europe]
sectors: [public-sector, technology, telco, finance]
entities:
  - malware:phexia
  - malware:etherrat
  - malware:castlerat
  - malware:patchcord
  - malware:sheetcord
  - malware:hackerai-c2-agent
  - campaign:stopandprotect
  - campaign:silkparasite-central-asia-2026
techniques: [T1102.001, T1102.002, T1071.001, T1583.006, T1584.006]
affected_products: []
cves: []
sources:
  - url: "https://redcanary.com/blog/threat-intelligence/intelligence-insights-august-2026/"
    publisher: "Red Canary"
    date: "2026-08-20"
    role: primary
  - url: "https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/"
    publisher: "Acronis Threat Research Unit"
    date: "2026-08-13"
    role: primary
  - url: "https://www.bitdefender.com/en-us/blog/businessinsights/silkparasite-tracking-china-nexus-apt-across-central-asia"
    publisher: "Bitdefender Labs"
    date: "2026-08-19"
    role: primary
  - url: "https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/"
    publisher: "Check Point Research"
    date: "2026-08-18"
    role: primary
closed_sources: []
evidence:
  - quote: "The technique makes traditional C2 blocking challenging, since the URL can be updated dynamically by adversaries"
    publisher: "Red Canary"
verification: multi-source
sourcing_note: >
  Four independent first-hand publishers, each documenting its own telemetry or its own analysis. No
  cited source connects the four operations and this entry asserts no relationship between them: the
  pattern claimed is a convergent architectural choice, not a shared operator or toolchain. Red
  Canary's own framing is that the blockchain dead-drop technique is not new — it dates first
  reporting to 2023 — and what its August round-up records is its arrival in commodity tooling, which
  is the delta this entry carries rather than the invention of a technique.
confidence: high
update_of: null
references:
  - 2026-08-23/blockchain-dead-drop-c2-commodity-graphspy
  - 2026-08-17/patchcord-sheetcord-google-sheets-c2-browser-shortcut-hijack
  - 2026-08-19/stopandprotect-wordpress-hosted-extortion-mu-plugin
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

A prior weekly carried a measurement of malware command-and-control that never asks DNS a question — traffic straight to an IP address, invisible to protective DNS, response-policy zones and sinkholing. Four disclosures this week describe the opposite arrangement and it is the harder one: the name resolves, correctly, to a service with a valid certificate and an unimpeachable reputation, because the operator has stored the actual rendezvous address *inside* something the estate already permits.

Red Canary's monthly round-up, published on July telemetry, is the clearest statement that this is no longer specialist tradecraft. Three of the four new entrants to its most-prevalent list resolve their command-and-control address from a dead drop rather than from a hardcoded domain or IP, and two of those read it off a public blockchain smart contract; the technique dates to first reporting in 2023, and what the round-up records is its arrival in commodity tooling, counted across three of its top ten this month ([Red Canary, 2026-08-20](https://redcanary.com/blog/threat-intelligence/intelligence-insights-august-2026/)). The mechanics decide what a defender can do about it. A macOS remote-access tool and stealer queries public Polygon RPC endpoints for a contract's stored value, decodes the response to extract a URL, and keeps messaging-platform and gaming-platform profiles as redundant dead-drop channels; a Node.js remote-access trojan polls public Ethereum RPC endpoints for a URL held at a predefined contract address; a third resolves its dead drop through a gaming-community domain or adversary-controlled hosts. Red Canary's own summary of why it matters operationally: "The technique makes traditional C2 blocking challenging, since the URL can be updated dynamically by adversaries" — the operator rewrites one contract value and every installation picks up the change with no redistribution.

The same architecture appears three more times this week on carriers that are not blockchains, which is what makes it an architectural pattern rather than a cryptocurrency story. Acronis's Threat Research Unit documents an espionage cluster running one implant's entire command-and-control through the Google Sheets API v4 using a hardcoded cloud service account and a per-victim spreadsheet tab, and a second implant doing the same job through GitHub Gists ([Acronis Threat Research Unit, 2026-08-13](https://www.acronis.com/en/tru/posts/patchcord-new-malware-cluster-targets-afghan-telecom-and-south-asian-critical-infrastructure/)). Bitdefender's SilkParasite disclosure records one family routing operator commands through a shared Google Drive folder and fetching in-memory plugins from it, and another using HTTP cookie and ETag header values as its command channel — a carrier that survives even a proxy inspecting request and response bodies, because the payload is in the caching metadata ([Bitdefender Labs, 2026-08-19](https://www.bitdefender.com/en-us/blog/businessinsights/silkparasite-tracking-china-nexus-apt-across-central-asia)). And Check Point Research describes a criminal toolkit that dispenses with dedicated infrastructure altogether, hosting its payloads, command-and-control and stolen data on roughly 2,000 compromised WordPress sites, with persistence on each one as a must-use plugin in a directory WordPress auto-loads on every request and does not show in the plugin list ([Check Point Research, 2026-08-18](https://research.checkpoint.com/2026/thousands-of-hacked-wordpress-sites-one-operation-unmasking-stopandprotect/)).

Four different carriers, one property: in each case the destination a network control can see is legitimate, and the address that matters is data held inside it, writable by the operator at will.

**Defender takeaway:** blocklists and reputation feeds have no purchase on any of this, and that is a structural fact rather than a tuning problem — you cannot deny-list a public blockchain RPC provider, the Google Sheets API, GitHub, or the general population of WordPress sites without breaking work. What replaces them is an egress baseline keyed on *process and host role* rather than on destination reputation, and the good news for this constituency is that the baseline is unusually easy to establish. Ask which of your systems has any legitimate reason to query a public blockchain RPC endpoint: for most public-sector and critical-infrastructure estates the answer is none, which turns a hard detection problem into a trivial one. The same question for the Sheets and Drive APIs, the Gists API and code-hosting endpoints has a longer answer, but it is still an enumerable one — a browser and a small set of sanctioned integrations, not a script interpreter or a service binary. The carrier that resists this framing is the WordPress case, because compromised sites are ordinary web destinations; there the leverage is on the other end, in the must-use-plugin directory, which has no legitimate reason to change on a site you operate. **Triage:** developer workstations and any wallet, blockchain-analytics or Web3 tooling produce genuine RPC traffic to the same endpoints, and Sheets, Drive and Gists traffic is routine on any host with a browser; the separators are whether the querying process is a browser or developer toolchain versus a script interpreter or service binary, whether the request pattern is interactive or a steady poll, and — the one that generalises across all four carriers — whether the host subsequently contacts an address it *learned* rather than one it was configured with. That last sequence, a fetch from a reputable service immediately followed by a first-ever connection to an unrelated host, is the observable the whole class shares.
