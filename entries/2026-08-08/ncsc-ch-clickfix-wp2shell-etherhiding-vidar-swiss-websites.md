---
schema: 1
kind: threat
horizon: operational
title: "NCSC-CH: Swiss websites compromised through WP2Shell are serving fake-CAPTCHA paste-and-run lures, with the follow-on payload resolved from a blockchain"
headline: "Switzerland's national authority asks critical-infrastructure operators to block outbound RPC providers as compromised Swiss sites rise"
summary: >
  NCSC-CH (BACS) published an advisory on 2026-08-07 reporting a rising count of compromised Swiss websites
  serving fake CAPTCHAs that instruct visitors to paste and run a command, and names the WP2Shell WordPress
  chain (CVE-2026-63030 with CVE-2026-60137) as what Swiss site operators and hosting providers have been
  reporting as the entry point. The pasted command pulls its next stage from a public blockchain reached
  through RPC-provider web interfaces, typically ending in an infostealer such as Vidar. BACS asks companies
  and critical-infrastructure operators outside fintech to restrict outbound connections to RPC providers —
  a concrete egress-policy change, not awareness advice.
discovered_at: "2026-08-08T04:50:00Z"
event_date: "2026-08-07"
run_id: 2026-08-08T0409Z-intel
priority: high
immediate_action: null
tags: [phishing, infostealer, vulnerabilities, actively-exploited, cisa-kev]
regions: [switzerland, global]
sectors: [public-sector, energy, water, transport, healthcare, finance, telco]
entities: []
techniques: [T1190, T1204.004, T1059.001, T1102.001, T1555.003]
affected_products: ["WordPress Core"]
cves:
  - id: CVE-2026-63030
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "WordPress 6.9.0–6.9.4 and 7.0.0–7.0.1"
    fixed: "WordPress 6.9.5 / 7.0.2"
  - id: CVE-2026-60137
    cvss: null
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "WordPress 6.9.0–6.9.4 and 7.0.0–7.0.1"
    fixed: "WordPress 6.9.5 / 7.0.2"
sources:
  - url: "https://www.ncsc.admin.ch/ncsc/de/home/aktuell/im-fokus/2026/clickfix.html"
    publisher: "NCSC Switzerland (BACS)"
    date: "2026-08-07"
    role: primary
closed_sources: []
evidence:
  - quote: "Dabei verwenden Cyberkriminelle eine Kombination aus zwei Schwachstellen in WordPress"
    publisher: "NCSC Switzerland (BACS)"
  - quote: "Unternehmen und Betreiberinnen kritischer Infrastrukturen, welche nicht im Fintech-Bereich tätig sind, sollten ausgehende Verbindungen zu RPC-Anbietern einschränken."
    publisher: "NCSC Switzerland (BACS)"
verification: single-source-national-cert
sourcing_note: "NCSC-CH is the disclosing national authority for its own jurisdiction and for its own advisory, which is the recognised carve-out from the two-source rule. The underlying WP2Shell chain is separately multi-source and already covered here on 2026-07-26; only the Swiss delivery-chain observations and the hardening recommendation rest on this single advisory."
confidence: high
update_of: 2026-07-26/wp2shell-cve-2026-63030-60137-confirmed-exploited-kev
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Restrict outbound connections from user endpoints to blockchain RPC-provider web interfaces, per BACS's own recommendation for companies and critical-infrastructure operators that are not in fintech — this is the takedown-resistant hop the pasted command depends on."
  - "Confirm every WordPress instance the organisation or its agencies publish is on 6.9.5 / 7.0.2 or later, and for any site that was reachable and unpatched, check for attacker-added administrator accounts and modified theme or plugin files rather than only applying the update."
migrated_from: null
---

**UPDATE (originally covered 2026-07-26):** Switzerland's national cyber authority has attached its own jurisdiction's numbers to the WordPress chain this pipeline recorded reaching CISA KEV in July. In an advisory published 2026-08-07, BACS reports a rising count of compromised websites presenting fake CAPTCHAs that push visitors into executing a command themselves, puts the worldwide population of compromised sites at more than 100,000, and states it is currently seeing an increase in the number of Swiss websites being compromised and used to distribute malware ([NCSC-CH, 2026-08-07](https://www.ncsc.admin.ch/ncsc/de/home/aktuell/im-fokus/2026/clickfix.html)).

The entry point is the already-covered one, now with reporting behind it: BACS writes that in recent days it has received an accumulation of reports from Swiss website operators and web-hosting providers describing exploitation of two recently disclosed WordPress vulnerabilities, and that "criminals use a combination of two vulnerabilities in WordPress" known as WP2Shell — CVE-2026-63030 and CVE-2026-60137 ([NCSC-CH, 2026-08-07](https://www.ncsc.admin.ch/ncsc/de/home/aktuell/im-fokus/2026/clickfix.html)). Most of the compromised sites run WordPress.

What is new below the entry point is the delivery chain. Once a visitor follows the instruction and runs the command, it fetches further malicious code whose storage and distribution sit on a public blockchain — the technique BACS names EtherHiding — retrieved through the web interfaces of RPC providers that broker access to those networks; the payload is typically an infostealer, with Vidar named as an example, going after credentials, payment-card data and cryptocurrency wallets ([NCSC-CH, 2026-08-07](https://www.ncsc.admin.ch/ncsc/de/home/aktuell/im-fokus/2026/clickfix.html)). That hop is why the authority's recommendation is an egress-policy one rather than a filtering one: a blockchain read has no domain to sinkhole.

**Defender takeaway:** BACS's guidance for organisations rather than for the public is specific and unusually easy to action — companies and operators of critical infrastructure that are not active in the fintech sector should restrict outgoing connections to RPC providers ([NCSC-CH, 2026-08-07](https://www.ncsc.admin.ch/ncsc/de/home/aktuell/im-fokus/2026/clickfix.html)). For a Swiss public-sector estate this cuts both ways: it is an outbound control on your own users, and a patch-state question about every WordPress site your organisation or its agencies publish, because those sites are what is being turned into the delivery surface for everyone else.

**Triage:** the client-side execution has a distinctive shape in process-creation telemetry with parent lineage — a command interpreter (`powershell.exe` on Windows, the terminal shell on macOS) started from a browser process tree, immediately followed by outbound HTTP to an RPC-provider endpoint. Neither half is individually rare on a developer or administrator workstation; the sequence, on a general-office endpoint, is the signal, and the browser parentage is what separates it from legitimate admin scripting, which is not launched from a browser. On the server side, the compromise signature is the WP2Shell request pattern against the unauthenticated REST batch endpoint in web-server access logs, followed by administrator-account or plugin and theme file changes that no admin action accounts for.
