---
schema: 1
kind: threat
title: "GTIG AI Threat Tracker (May 2026): an AI-developed zero-day 2FA bypass prepared for mass exploitation, AI decoy code in Russia-nexus malware and PROMPTSPY's Gemini agent"
headline: "GTIG finds a criminal zero-day exploit it believes was built with AI; its discovery may have prevented mass exploitation"
summary: "Google Threat Intelligence Group's AI Threat Tracker of 2026-05-11 reports the first zero-day exploit it believes was developed with AI: a Python 2FA bypass for a popular open-source web-based system administration tool that needs valid credentials, which criminals planned to use in mass exploitation before GTIG's coordinated disclosure may have prevented it. The report also documents LLM-generated decoy code in the Russia-nexus CANFAIL and LONGSTREAM malware, the Android backdoor PROMPTSPY driving devices through Gemini, PRC and DPRK actors using Gemini for vulnerability research, pooled LLM access, and TeamPCP's supply-chain compromises of AI components."
discovered_at: "2026-05-12T05:00:07Z"
event_date: 2026-05-11
run_id: 2026-05-12-cd1ab844
priority: notable
immediate_action: null
tags:
  - ai-abuse
  - nation-state
  - espionage
  - supply-chain
  - organized-crime
  - china-nexus
  - russia-nexus
  - north-korea-nexus
regions:
  - global
sectors:
  - public-sector
  - defense
  - technology
entities:
  - "actor:teampcp"
  - "report:gtig-ai-threat-tracker-may-2026"
  - "actor:dark-castle"
techniques: [T1190, T1078, T1588.007, T1587.004, T1027.016, T1090.003, T1591, T1592.001, T1195.002, T1552]
affected_products: []
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access"
    publisher: "Google Threat Intelligence Group"
    date: "2026-05-11"
    role: primary
  - url: "https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html"
    publisher: "The Hacker News"
    date: "2026-05-11"
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/11/google-ai-vulnerability-exploitation/"
    publisher: "Help Net Security"
    date: "2026-05-11"
    role: corroborating
  - url: "https://www.securityweek.com/google-detects-first-ai-generated-zero-day-exploit/"
    publisher: "SecurityWeek"
    date: "2026-05-11"
    role: corroborating
  - url: "https://www.theregister.com/ai-ml/2026/05/11/google-says-criminals-used-ai-built-zero-day-in-planned-mass-hack-spree/5237982"
    publisher: "The Register"
    date: "2026-05-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "For the first time, GTIG has identified a threat actor using a zero-day exploit that we believe was developed with AI. The criminal threat actor planned to use it in a mass exploitation event but our proactive counter discovery may have prevented its use."
    publisher: "Google Threat Intelligence Group"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access"
  - quote: "The vulnerability can be classified as a 2FA bypass, though it requires valid user credentials in the first place."
    publisher: "Google Threat Intelligence Group"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access"
  - quote: "Analysis confirms the use of CANFAIL and LONGSTREAM, which utilize LLM-generated decoy code to obfuscate their malicious functionality."
    publisher: "Google Threat Intelligence Group"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access"
  - quote: "For example, they employ \"Claude-Relay-Service\" to aggregate multiple Gemini, Claude, and OpenAI accounts, enabling account pooling and cost-sharing."
    publisher: "Google Threat Intelligence Group"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access"
  - quote: "TeamPCP gained initial access through compromised PyPI packages and malicious pull requests to these GitHub repositories."
    publisher: "Google Threat Intelligence Group"
    source_url: "https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access"
  - quote: "marking the first time the technology has been put to use in the wild in a malicious context for vulnerability discovery and exploit generation."
    publisher: "The Hacker News"
    source_url: "https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html"
verification: multi-source
sourcing_note: >
  Every finding is Google Threat Intelligence Group's, from Mandiant incident response, Gemini and its own research; The Hacker
  News, Help Net Security, SecurityWeek and The Register restate it. PROMPTSPY was first identified by ESET, and GTIG adds the
  capabilities described here.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-12.md
updates:
  - at: "2026-10-21T20:41:20Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      GTIG reports a zero-day exploit it believes was developed with AI that criminals planned to use in
      mass exploitation and that its disclosure may have prevented, not one confirmed in use in the wild;
      it needs valid credentials. CANFAIL and LONGSTREAM embed LLM-generated decoy code as obfuscation
      rather than calling an LLM at runtime, PROMPTSPY is the report's AI-driven malware, and UNC5673
      pools LLM accounts; the report ties neither stolen LLM keys nor SANDCLOCK to a criminal market for
      AI access, and TeamPCP's entry points were compromised PyPI packages and malicious pull requests.
    fields: [affected_products, body, classification, entities, evidence, headline, priority, sources, sourcing_note, summary, techniques, title]
---

Google Threat Intelligence Group's AI Threat Tracker of 2026-05-11, drawn from Mandiant incident response engagements, Gemini and GTIG's own research, follows its February 2026 report on AI-related threat activity ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)).

#### An AI-developed zero-day prepared for mass exploitation

GTIG observed prominent cybercrime actors partnering to plan a mass vulnerability-exploitation operation around a zero-day exploit, implemented in a Python script, that bypasses two-factor authentication on a popular open-source, web-based system administration tool; GTIG worked with the vendor to disclose the flaw and disrupt the activity, and says its counter-discovery may have prevented the exploit's use ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). The bypass requires valid user credentials and stems from a high-level semantic logic flaw, a trust assumption the developer hardcoded, rather than from memory corruption or input sanitisation ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). GTIG does not believe Gemini was used but has high confidence that an AI model supported the discovery and weaponisation, citing abundant educational docstrings, a hallucinated CVSS score and a textbook Pythonic structure with detailed help menus and a clean _C ANSI colour class ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). Google did not name the tool ([The Hacker News, 2026-05-11](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html)). Contradiction: The Hacker News calls this the first time AI was put to use in the wild for exploit generation ([The Hacker News, 2026-05-11](https://thehackernews.com/2026/05/hackers-used-ai-to-develop-first-known.html)), whereas GTIG says the planned mass exploitation may have been prevented ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)).

#### State actors using AI for vulnerability research and infrastructure

UNC2814 prompted Gemini with expert security personas to support vulnerability research into embedded targets including TP-Link firmware and Odette File Transfer Protocol (OFTP) implementations, and APT45 sent thousands of repetitive prompts that recursively analyse different CVEs and validate proof-of-concept exploits ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). APT27 used Gemini to develop a fleet-management application likely meant for an operational relay box network, with the hop count hardcoded to three and mobile Wi-Fi and router devices among the supported types ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). Actors also prompt models for the organisational hierarchies and third-party relationships of large enterprises to tailor phishing lures, one tried to identify the exact computer model a high-value target used, and a suspected PRC-nexus actor ran the agentic tools Hexstrike and Strix against a Japanese technology firm and an East Asian cybersecurity platform ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)).

#### Malware with AI-generated decoys and an AI-driven Android backdoor

Russia-nexus activity against Ukrainian organisations delivers CANFAIL and LONGSTREAM, which use LLM-generated decoy code to obfuscate their malicious functionality: CANFAIL's source carries LLM comments labelling unused filler blocks, and LONGSTREAM queries the system's daylight-saving status 32 times to pad the script with benign-looking activity ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). PROMPTFLUX and HONESTCUE, which call the Gemini API to generate or obfuscate code, featured in GTIG's earlier reports ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). The Android backdoor PROMPTSPY, first identified by ESET, runs an agent module that serialises the visible user interface through the Accessibility API, sends it to the gemini-2.5-flash-lite model in an HTTP POST and turns the JSON reply into simulated taps and swipes; it can replay captured PINs or lock patterns, lays an invisible overlay over the uninstall button and can rotate its Gemini API keys and VNC relay through its C2 ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)).

#### Pooled LLM access and attacks on AI components

UNC6201 tried a public script that registers and immediately cancels premium LLM accounts, and UNC5673, a PRC-nexus cluster with notable overlaps with TEMP.Hex that has targeted government sectors mainly in South and Southeast Asia, uses Claude-Relay-Service and CLI-Proxy-API to pool Gemini, Claude and OpenAI accounts ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). TeamPCP (UNC6780) gained initial access through compromised PyPI packages and malicious pull requests to GitHub repositories including those of Trivy, Checkmarx, LiteLLM and BerriAI, embedded the SANDCLOCK credential stealer to extract AWS keys and GitHub tokens from build environments and monetised them with ransomware and data-theft extortion groups; GTIG adds that the LiteLLM compromise could expose considerable AI API secrets ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)).

**Exposure:** the zero-day needs valid user credentials on an administration tool GTIG does not name ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)); build environments that pulled the TeamPCP-compromised Trivy, Checkmarx, LiteLLM or BerriAI components held the AWS keys and GitHub tokens SANDCLOCK went after ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)).

**Detection:** for exploit scripts under triage, GTIG's markers of LLM authorship are dense educational docstrings, a hallucinated CVSS score and a textbook structure with help menus and ANSI colour classes; on Android, PROMPTSPY's trace is an app posting accessibility-derived UI dumps to the Gemini API over HTTP ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)).

**Defender takeaway:** the unnamed zero-day gives no patch or hunt to act on; the decision falls on build pipelines that consumed the compromised Trivy, Checkmarx, LiteLLM or BerriAI components, which treat the AWS keys and GitHub tokens those environments held as stolen, and, where LiteLLM ran, the AI API secrets GTIG says its compromise could expose ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)).

## Correction — 2026-10-21T20:41:20Z

GTIG reports the first zero-day exploit it believes was developed with AI, prepared by criminals for a planned mass-exploitation event that its counter-discovery may have prevented, not an exploit confirmed in use in the wild; the 2FA bypass also requires valid user credentials ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). CANFAIL and LONGSTREAM do not call an LLM at runtime: they carry LLM-generated decoy code to obfuscate their functionality, and the report's example of malware driven by an LLM at runtime is the Android backdoor PROMPTSPY ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). UNC5673 overlaps with TEMP.Hex rather than being it, and uses relay tooling to pool LLM accounts; the report does not describe stolen LLM API keys as a primary objective or a criminal market for them, and its only point on AI API secrets is that the LiteLLM compromise could expose them ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). TeamPCP entered through compromised PyPI packages and malicious pull requests to GitHub repositories, and embedded SANDCLOCK to take AWS keys and GitHub tokens from build environments ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)).
