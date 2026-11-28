---
schema: 1
kind: vulnerability
title: "F5 BIG-IP: six unauthenticated stack overflows rated CVSS 9.8 (CVE-2026-123637, CVE-2026-116953, CVE-2026-120285, CVE-2026-120292, CVE-2026-120722, CVE-2026-121805) crash TMM and may allow code execution where an iRule command or APM policy is configured; fixed only by engineering hotfixes, no exploitation reported"
headline: "F5 BIG-IP: six unauth CVSS 9.8 TMM overflows, fixed only by engineering hotfixes; check iRule and APM use"
summary: >
  F5's 2026-11-18 notification includes six BIG-IP flaws that an unauthenticated remote attacker can use to terminate the Traffic Management Microkernel and that F5 says may allow remote code execution, each CVSS 3.1 9.8 and each needing a specific virtual-server configuration: one of five iRule commands, or an APM per-request policy that includes both the Client Information and Endpoint Security agents. BIG-IP 21.1, 17.5 and 17.1 are affected, no scheduled release carries the fix and F5 lists no workaround, so the fix is an engineering hotfix from F5; none of F5's advisories says the flaws are exploited.
discovered_at: "2026-11-24T04:32:40Z"
updated_at: null
event_date: "2026-11-18"
run_id: 2026-11-24T0355Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, pre-auth, rce, dos, patch-available]
regions: [global]
sectors: []
entities: ["product:f5-big-ip", "product:f5-big-ip-access-policy-manager-apm", "product:f5-big-ip-next-for-kubernetes"]
techniques: [T1190, T1499.004]
affected_products: ["F5 BIG-IP", "F5 BIG-IP Access Policy Manager (APM)", "F5 BIG-IP Next for Kubernetes"]
cves:
  - id: CVE-2026-123637
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "BIG-IP 21.1.0, 17.5.0 and 17.1.0 with APM provisioned and a per-request policy that includes the Client Information and Endpoint Security agents"
    fixed: "engineering hotfixes BIGIP-21.1.0.4.0.19.3-ENG, BIGIP-17.5.1.11.0.61.12-ENG or BIGIP-17.5.1.10.0.80.35-ENG, BIGIP-17.1.3.7.0.21.4-ENG or BIGIP-17.1.3.6.0.14.20-ENG"
  - id: CVE-2026-116953
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "BIG-IP 21.1.0, 17.5.0 and 17.1.0 and BIG-IP Next for Kubernetes 2.2.0 to 2.4.2 with an iRule that uses GENERICMESSAGE::route on client traffic"
    fixed: "the BIG-IP engineering hotfixes above; BNK-2.4.2-EHF1, BNK-2.3.4-EHF1 or BNK-2.2.5-EHF1 for Next for Kubernetes"
  - id: CVE-2026-120285
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "BIG-IP 21.1.0, 17.5.0 and 17.1.0, BIG-IP Next for Kubernetes and BIG-IP CNF 2.2.0 to 2.4.2 with an HTTP profile and an iRule that uses PSC::ip_address"
    fixed: "the BIG-IP engineering hotfixes above; BNK-2.4.2-EHF1, BNK-2.3.4-EHF1 or BNK-2.2.5-EHF1 (CNF-2.4.2-EHF1, CNF-2.3.4-EHF1 or CNF-2.2.5-EHF1 for CNF)"
  - id: CVE-2026-120292
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "BIG-IP 21.1.0, 17.5.0 and 17.1.0 and BIG-IP Next for Kubernetes 2.2.0 to 2.4.2 with an HTTP profile and an iRule that uses MR::message route"
    fixed: "the BIG-IP engineering hotfixes above; BNK-2.4.2-EHF1, BNK-2.3.4-EHF1 or BNK-2.2.5-EHF1 for Next for Kubernetes"
  - id: CVE-2026-120722
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "BIG-IP DNS 21.1.0, 17.5.0 and 17.1.0 and BIG-IP Next for Kubernetes 2.2.0 to 2.4.2 with an iRule that uses DNS::scrape on client traffic"
    fixed: "the BIG-IP engineering hotfixes above; BNK-2.4.2-EHF1, BNK-2.3.4-EHF1 or BNK-2.2.5-EHF1 for Next for Kubernetes"
  - id: CVE-2026-121805
    cvss: "9.8"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "BIG-IP PEM 21.1.0, 17.5.0 and 17.1.0, BIG-IP Next for Kubernetes and BIG-IP CNF 2.2.0 to 2.4.2 with an iRule that uses PEM::subscriber on client traffic"
    fixed: "the BIG-IP engineering hotfixes above; BNK-2.4.2-EHF1, BNK-2.3.4-EHF1 or BNK-2.2.5-EHF1 (CNF-2.4.2-EHF1, CNF-2.3.4-EHF1 or CNF-2.2.5-EHF1 for CNF)"
sources:
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4723"
    publisher: "BSI CERT-Bund (WID-SEC-2026-4723)"
    date: "2026-11-23"
    role: primary
  - url: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0508"
    publisher: "NCSC-NL (NCSC-2026-0508)"
    date: "2026-11-19"
    role: primary
  - url: "https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html"
    publisher: "The Hacker News"
    date: "2026-11-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "allow an attacker to crash the Traffic Management Microkernel (TMM) without logging in, disrupting traffic until the TMM restarts"
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html"
  - quote: "None of the company's advisories says the flaws have been exploited."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html"
  - quote: "For the six critical flaws, the only fixes are engineering hotfixes, builds that the company issues between its normal software releases."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html"
  - quote: "A remote, anonymous attacker can exploit a vulnerability in F5 BIG-IP to execute arbitrary program code. (translated from German)"
    original: "Ein entfernter, anonymer Angreifer kann eine Schwachstelle in F5 BIG-IP ausnutzen, um beliebigen Programmcode auszuführen."
    publisher: "BSI CERT-Bund"
    source_url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4723"
verification: multi-source
sourcing_note: >
  All three sources derive from F5's single security notification (K000164058), whose K-articles were not available. The affected branches, BIG-IP hotfix build names and CVSS 3.1 scores are F5 CVE-record data; the Next for Kubernetes and CNF hotfix names come from The Hacker News. The Hacker News reports that F5's advisory lists BIG-IP CNF as not vulnerable to CVE-2026-120722 while its CVE record lists CNF as affected, so CNF is left out of that record. BSI dates its advisory 2026-11-23, after F5's 2026-11-18 publication.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "On every BIG-IP, list the virtual servers whose iRules call GENERICMESSAGE::route, PSC::ip_address, MR::message route, DNS::scrape or PEM::subscriber and the APM per-request policies that include both the Client Information and Endpoint Security agents, internet-facing ones first, and apply the matching engineering hotfix on each such system on 21.1, 17.5 or 17.1 (a system on a custom engineering hotfix needs a new one from F5 support), because F5 lists no workaround and no scheduled release carries the fix."
updates: []
migrated_from: null
---

F5's security notification of 2026-11-18 lists 22 advisories, 10 of them for NGINX; six BIG-IP flaws among them let an attacker without credentials crash the Traffic Management Microkernel (TMM), disrupting traffic until it restarts, and F5 says they may also allow remote code execution ([The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)). All six are stack-based buffer overflows in the data plane, which processes almost all of BIG-IP's network traffic, rated CVSS 3.1 9.8 and CVSS 4.0 9.3; the management side is not exposed, and watchTowr's Sina Kheirkhah reported four of them while F5 found the other two ([The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)). BSI CERT-Bund's advisory, which lists only the APM flaw CVE-2026-123637, says a remote, anonymous attacker can execute arbitrary code (translated from German) ([BSI CERT-Bund, 2026-11-23](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4723)), and NCSC-NL, whose advisory also covers six lower-rated BIG-IP flaws, rates the likelihood medium and the damage high ([NCSC-NL, 2026-11-19](https://advisories.ncsc.nl/advisory?id=NCSC-2026-0508)).

Each flaw needs a specific configuration on a virtual server: an iRule that uses GENERICMESSAGE::route on client traffic (CVE-2026-116953); an HTTP profile with an iRule that uses PSC::ip_address (CVE-2026-120285) or MR::message route (CVE-2026-120292); an iRule that uses DNS::scrape on client traffic (CVE-2026-120722, BIG-IP DNS) or PEM::subscriber on client traffic (CVE-2026-121805, BIG-IP PEM); or an APM per-request policy that includes both the Client Information and Endpoint Security agents (CVE-2026-123637, APM only) ([The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)). BIG-IP Next for Kubernetes and, for some of the six, BIG-IP CNF are affected as well, and F5 checks only versions still in technical support, so an older release missing from its tables has not been shown to be safe ([The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)).

No scheduled release is listed as a fix and F5 lists no workaround: the fixes are engineering hotfixes, which F5 says do not receive the QA of scheduled releases, and a system on a custom engineering hotfix needs a new one from F5 support ([The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)). None of F5's advisories says the six are exploited, and they differ from CVE-2026-94127, the APM flaw F5 disclosed on 2026-09-22 that was later exploited ([The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)).

**Exposure:** a BIG-IP on the 21.1, 17.5 or 17.1 branch (BSI's product tree lists builds before the hotfix builds) whose virtual servers use one of those iRule commands or APM policy agents ([BSI CERT-Bund, 2026-11-23](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4723); [The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)).

**Detection:** TMM process terminations and restarts and core files in the BIG-IP system logs, tied to the virtual server that carries the affected iRule or policy, follow from the stated impact (traffic disrupted until TMM restarts); no source describes a successful code-execution chain or a post-exploitation artefact ([The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)).

**Defender takeaway:** an unauthenticated remote crash of the traffic plane, with possible code execution, can be reached only on the configurations above, so inventory those first and apply the engineering hotfix instead of waiting for a scheduled release; a system on a custom engineering hotfix needs a new one from F5 support ([The Hacker News, 2026-11-18](https://thehackernews.com/2026/11/f5-warns-6-critical-big-ip-flaws-can.html)).
