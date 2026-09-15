---
schema: 1
kind: threat
title: "Unit 42 exposes two Latin American intrusion clusters after their own AI-agent staging infrastructure was left open — one hit Mexican federal ministries and water utilities, the other Brazilian finance"
headline: "An exposed self-hosted AI chat interface handed researchers the operators' playbook for a campaign against Mexican and Ecuadorian government infrastructure"
summary: >
  Palo Alto Networks Unit 42 documents two distinct AI-augmented intrusion clusters targeting Latin
  America: CL-CRI-1131, which hit a Mexican transportation firm, federal government ministries and
  municipal water utilities in Mexico and Ecuador using an exposed self-hosted NextChat AI interface
  to generate working exploit scripts; and CL-CRI-1163, targeting Brazilian financial-sector victims
  via job-themed phishing with an iteratively-versioned, AI-assisted SOCKS5 tunneling tool. A
  separate Google Threat Intelligence Group report the same week on a financially-motivated actor
  (BREEZE COMET, formerly UNC5669) documents the same regional pattern of AI-assisted tooling
  against Brazilian payment infrastructure.
discovered_at: "2026-09-04T05:50:00Z"
updated_at: null
event_date: "2026-09-03"
run_id: 2026-09-04T0410Z-intel
priority: high
immediate_action: null
tags: [nation-state, ai-abuse, vulnerabilities]
regions: [latam]
sectors: [public-sector, finance, water]
entities:
  - "actor:cl-cri-1131"
  - "actor:cl-cri-1163"
  - "actor:breeze-comet"
techniques: [T1566, T1003.002, T1003.003, T1090, T1572, T1071.004, T1190]
affected_products: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-09-03"
    role: primary
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/financially-motivated-threat-actor-breeze-comet-targets-brazil"
    publisher: "Google Threat Intelligence Group / Mandiant"
    date: "2026-09-01"
    role: corroborating
  - url: "https://www.darkreading.com/threat-intelligence/breeze-comet-brazilian-global-financial-systems"
    publisher: "Dark Reading"
    date: "2026-09-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "we observed the attacker struggling to gather sensitive data. After repeated attempts to dump the Security Account Manager (SAM) registry hive and the domain controller NTDS.dit file, the attacker created shadow copies across multiple drives"
    publisher: "Unit 42"
  - quote: "Exposing an open NextChat directory to the public internet reveals a fundamental lack of operational maturity. The AI provided the necessary tactical workaround to extract the Active Directory database, but the human operators failed to secure the staging server."
    publisher: "Unit 42"
  - quote: "attackers appended exploit filenames with descriptive adjectives. This suggests that the attackers employed iterative, language model-driven development: exploit_creative.py, exploit_careful.py and rce_focused.py."
    publisher: "Unit 42"
  - quote: "Within 24-48 hours of establishing this access, the threat actor executed two waves of hundreds of fraudulent transactions, based on reporting by a client and third party forensic analysis."
    publisher: "Google Threat Intelligence Group / Mandiant"
verification: multi-source
sourcing_note: >
  CL-CRI-1131 and CL-CRI-1163 are Unit 42's own reporting alone — single-source for those two
  clusters specifically. BREEZE COMET is a separate, independently-reported finding from Google
  Threat Intelligence Group/Mandiant covering a different actor and different malware family; it is
  cited here as corroborating evidence of the same regional pattern (AI-assisted tooling against
  Latin American financial/government targets), not as independent confirmation of Unit 42's two
  clusters. Dark Reading relays GTIG's own report rather than assessing it independently.
confidence: high
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

Unit 42 published two distinct, ongoing intrusion clusters against Latin American targets on 2026-09-03, both showing operators using commercial LLMs to drive parts of the attack chain. CL-CRI-1131 hit a Mexican transportation organization plus federal government ministries and municipal water utilities in Mexico and Ecuador: operators relied on living-off-the-land batch scripts, and — after repeated failed attempts to dump the SAM registry hive and NTDS.dit — pivoted to shadow-copy-based collection instead ([Unit 42, 2026-09-03](https://unit42.paloaltonetworks.com/ai-tool-use-targeting-latam-orgs/)). A self-hosted instance of NextChat, an open-source multi-model LLM chat interface, exposed on the operators' own infrastructure is what let Unit 42 reconstruct the operators' targeting logic: given the initial collection failures and the exposed AI interface on the same backend, Unit 42 assesses the operators relied on the LLM to generate the working-around scripts. Certificate-transparency pivoting on the associated infrastructure showed a single-domain certificate in February 2026 rotating to a five-subdomain certificate by April/June 2026, with subdomain names indicating Mexican federal-government targeting categories. Unit 42 ties this activity to the campaign CloudSEK separately tracks as "Operation Escaneo."

CL-CRI-1163 is a separate cluster reached via job-themed phishing against the Brazilian financial sector, deploying homebrewed malware rather than living-off-the-land tooling: within a two-hour window, attackers attempted installation of versions 1 through 8 of a Go-based reverse SOCKS5 tunneling tool named SockTz from a compromised WordPress site, then, after that install path failed, retrieved a ninth version from separate attacker-controlled infrastructure, with exploit-script filenames appended with descriptive adjectives — exploit_creative.py, exploit_careful.py, rce_focused.py — that Unit 42 reads as evidence of iterative, language-model-driven script generation rather than human authorship. Unit 42's central finding across both clusters is that the operators' own AI-staging infrastructure — an open NextChat directory, an open directory of numbered SockTz builds — is what let researchers reconstruct the operators' playbooks: attacker OpSec failures around their own AI tooling, not the AI use itself, are the exploitable defender advantage.

Separately, on 2026-09-01, Google Threat Intelligence Group/Mandiant documented BREEZE COMET (formerly UNC5669) — a financially-motivated actor active against Brazilian financial services, retail and eCommerce since 2024, which GTIG states overlaps with activity publicly reported by others as "Plump Spider" and "SHADOW-AETHER-064" ([Google Threat Intelligence Group / Mandiant, 2026-09-01](https://cloud.google.com/blog/topics/threat-intelligence/financially-motivated-threat-actor-breeze-comet-targets-brazil)). Trend Micro has reported that the group also exploits vulnerabilities in JBoss AS servers for initial access ([Google Threat Intelligence Group / Mandiant, 2026-09-01](https://cloud.google.com/blog/topics/threat-intelligence/financially-motivated-threat-actor-breeze-comet-targets-brazil), citing Trend Micro), alongside password spraying and voice-phishing calls impersonating IT support to talk targets into installing remote-monitoring tools. BREEZE COMET manipulates Brazil's Pix, STR and Boleto payment rails via a custom malware suite and stages through compromised small-government websites across Brazil, Nigeria, Paraguay, Ghana and Venezuela; one component, MILDFROST, is a passive Java backdoor that uses a class named `DnsCommandBeacon` to run a slow, covert DNS tunnel as a fallback command channel, dynamically querying delegated subdomains for instructions and fresh payloads ([Google Threat Intelligence Group / Mandiant, 2026-09-01](https://cloud.google.com/blog/topics/threat-intelligence/financially-motivated-threat-actor-breeze-comet-targets-brazil)). GTIG independently confirms LLM-generated reconnaissance, credential-validation and deployment scripts in this cluster too, identified by a verbose AI-generated commenting style rather than any hardcoded signature. Within 24 to 48 hours of gaining access to core financial applications, GTIG reports the actor executed two waves of hundreds of fraudulent transactions.

**Defender takeaway:** the OpSec-failure angle is a durable, actor-agnostic hunting and takedown vector worth building into infrastructure-hunting workflows generally — an exposed AI-agent staging port or open directory of tool builds is now a realistic discovery surface, not a hypothetical one. For any organisation running financial-transaction infrastructure, GTIG's hardening list is unusually concrete: 802.1X network-access-control on branch/retail switch ports (BREEZE COMET has physically connected rogue hardware to retail networks), PowerShell Constrained Language Mode with Script Block Logging and AMSI enabled, blocking non-essential outbound ICMP and generic tunneling utilities at egress, and DPI/TLS decryption on outbound web traffic rather than relying on domain-reputation or government-TLD allowlisting — BREEZE COMET stages payloads and C2 from compromised small-government websites specifically to launder that reputation signal.
