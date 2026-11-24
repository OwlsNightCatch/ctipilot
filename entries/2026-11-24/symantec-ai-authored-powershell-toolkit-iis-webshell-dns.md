---
schema: 1
kind: threat
title: "Symantec: 41 likely AI-authored PowerShell modules ran under an IIS web shell at an African stock exchange for just over three minutes, hunting secrets in SYSVOL, shared folders, SharePoint, SCCM and TFS, testing them against financial APIs and returning the output as hex-encoded DNS lookups to a public out-of-band testing service"
headline: "Symantec: 41 AI-authored PowerShell modules ran under an IIS web shell and exfiltrated through DNS lookups"
summary: >
  Symantec's Threat Hunter Team found a toolkit on a stock-exchange web server in an African country in which 41 PowerShell modules ran under an IIS web shell for 3 minutes 12 seconds on 2026-09-20, hunting secrets in Group Policy Preferences, shared folders, SharePoint, SCCM and TFS, testing a guessed password, a reused token and API keys against the exchange's investment API and a securities-depository gateway, and returning their output as hex-encoded DNS lookups to a public out-of-band testing service. Symantec assesses AI authorship from the uniform scaffolding, attributes six older implants on the same server to Witchetty with high confidence but does not attribute the toolkit, and does not know whether any credential worked.
discovered_at: "2026-11-24T04:33:00Z"
updated_at: null
event_date: "2026-09-20"
run_id: 2026-11-24T0355Z-intel
priority: notable
immediate_action: null
tags: [ai-abuse]
regions: [africa]
sectors: [finance]
entities: ["incident:african-stock-exchange-ai-authored-toolkit-2026-09", "actor:witchetty"]
techniques: [T1505.003, T1059.001, T1552.006, T1552.001, T1213.002, T1213.003, T1580, T1135, T1057, T1110.001, T1550.001, T1048.003]
affected_products: []
cves: []
sources:
  - url: "https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack"
    publisher: "Symantec / Broadcom (Threat Hunter Team)"
    date: "2026-11-19"
    role: primary
closed_sources: []
evidence:
  - quote: "41 PowerShell modules ran under a web shell for just over three minutes on September 20, 2026, with a new module starting every few seconds."
    publisher: "Symantec / Broadcom (Threat Hunter Team)"
    source_url: "https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack"
  - quote: "Each module sent its output as hex-encoded DNS lookups to a unique subdomain of a public out-of-band testing service, a rarely seen technique."
    publisher: "Symantec / Broadcom (Threat Hunter Team)"
    source_url: "https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack"
  - quote: "Six persistence implants on the same server are attributed to the China-linked espionage group Witchetty with high confidence, but we have not attributed the AI-authored toolkit to any group."
    publisher: "Symantec / Broadcom (Threat Hunter Team)"
    source_url: "https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack"
  - quote: "The results went to a collector that we cannot see, so we do not know whether any of the credentials or keys worked."
    publisher: "Symantec / Broadcom (Threat Hunter Team)"
    source_url: "https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack"
  - quote: "None of these signals is conclusive on its own, but taken together they fit AI-assisted or AI-generated authorship better than they fit bespoke attacker tooling."
    publisher: "Symantec / Broadcom (Threat Hunter Team)"
    source_url: "https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack"
verification: single-source
sourcing_note: >
  Symantec is first-hand for the telemetry and the implants and is the only source; a search for independent corroboration found none. AI authorship and the Witchetty attribution of the implants are Symantec's assessments, and it does not attribute the toolkit to any group.
confidence: medium
references: ["2026-11-17/symantec-ai-assisted-retailer-intrusion-orion-rabbitmq"]
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

Symantec's Threat Hunter Team found a toolkit on a stock-exchange web server in an African country: 41 PowerShell modules ran under a web shell inside the IIS worker process between 08:44 and 08:47 UTC on 2026-09-20, a new module every few seconds ([Symantec, 2026-11-19](https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack)). The modules profiled the host and its IIS sites and hunted for secrets in the domain's SYSVOL share (Group Policy Preferences password fields), shared policy folders, web roots and deployment directories (hard-coded passwords, AWS keys, connection strings in .xml, .json, .env and web.config files); they also searched SharePoint for the keywords aws, credential and password, queried SCCM for the machine a given user last logged on to, listed Team Foundation Server projects and probed a PostgreSQL instance and a SQL Server. Four modules tested a guessed password, a reused bearer token and several API keys against the exchange's investment API and a securities-depository gateway ([Symantec, 2026-11-19](https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack)).

Every module hex-encoded its output into 50-character chunks and resolved each as a DNS name under unique subdomains of a single token on a public out-of-band testing service, so the data left as DNS lookups; Symantec calls this rarely seen, cannot see the collector and does not know whether any credential or key worked ([Symantec, 2026-11-19](https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack)). Its case for AI authorship is uniformity: the same error handling in every module, the DNS loop copied byte for byte into all 41, generic variable names and a deliberately invalid test credential; it calls no signal conclusive ([Symantec, 2026-11-19](https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack)).

Symantec attributes six persistence implants on the same server to Witchetty (LookingFrog), a China-linked espionage group, with high confidence, the earliest evidence dating from April 2026, but does not attribute the toolkit to any group; it names three explanations: Witchetty with new tooling, a second operator using the same access, or an unrelated actor. The way in is not stated, a web shell under the IIS worker process suggests a vulnerability may have been exploited, and Symantec found no evidence of privilege escalation or data theft ([Symantec, 2026-11-19](https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack)).

**Exposure:** a Windows estate with an IIS server whose worker account can read secrets: Group Policy Preferences passwords in SYSVOL, credentials in web.config and deployment folders, and reachable SharePoint, SCCM and TFS servers ([Symantec, 2026-11-19](https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack)).

**Detection:** repeated short-lived PowerShell jobs started within seconds with the IIS worker process as ancestor; DNS egress from a server-class host to long hex-looking labels under a public out-of-band testing service; reads of SYSVOL policy folders and of web.config and .env files by the web-tier account; SCCM, SharePoint and TFS queries from a web server. Symantec says the uniform scaffold and the copied DNS loop are what defenders can look for ([Symantec, 2026-11-19](https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack)).

**Triage:** out-of-band testing lookups are normal from a vulnerability scanner or penetration-test host; the discriminator is a production web server issuing them from PowerShell children of the IIS worker process.

**Defender takeaway:** hunt web-tier servers for PowerShell spawned by the worker process and for server DNS egress to out-of-band testing services; remove Group Policy Preferences passwords from SYSVOL, move secrets out of web roots and shared folders, rotate any found there, and keep the web-tier account away from SCCM, TFS and SharePoint ([Symantec, 2026-11-19](https://www.security.com/threat-intelligence/african-stock-exchange-ai-assisted-attack)).
