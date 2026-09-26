---
schema: 1
kind: threat
title: "WaterPlum (\"Contagious Interview\"): a seven-agency joint advisory quantifies the DPRK fake-job campaign for the first time — 30,000+ devices, 100+ countries, $10.7M in crypto, and Japan's first dismantled \"laptop farm\""
headline: "FBI, Japanese and German authorities jointly confirm DPRK's fake-interview crew has infected 30,000+ devices and drained $10.7M from crypto wallets"
summary: >
  Japan's NPA and NCO, the US FBI and DoD Cyber Crime Center, Australia's ASD/ACSC and Germany's BND
  and BfV jointly published a Cybersecurity Advisory on 2026-09-18 quantifying the DPRK "WaterPlum"
  cyber-actor group — the long-running campaign already tracked as "Contagious Interview" — for the
  first time: 30,000+ infected devices across 100+ countries, funds or credentials exfiltrated from
  7,000+ cryptocurrency wallets, and roughly USD 10.7 million transferred to DPRK. The advisory names
  five malware families delivered via fake technical-interview coding assignments and confirms Japan's
  first-ever dismantled DPRK "laptop farm."
discovered_at: "2026-09-19T04:40:00Z"
updated_at: null
event_date: "2026-09-18"
run_id: 2026-09-19T0409Z-intel
priority: high
immediate_action: null
tags: [nation-state, espionage, phishing, cryptocrime, supply-chain, north-korea-nexus]
regions: [global, europe]
sectors: [public-sector, technology, finance]
entities: ["campaign:contagious-interview", "actor:purpledelta", "malware:beavertail", "malware:invisibleferret", "malware:ottercandy", "malware:stoatwaffle", "tool:ottercookie"]
techniques: [T1204.002, T1195.002, T1555.003, T1115, T1056.001, T1113, T1071]
affected_products: ["Microsoft Visual Studio Code"]
cves: []
sources:
  - url: "https://www.ic3.gov/CSA/2026/260918.pdf"
    publisher: "FBI/IC3 Joint Cybersecurity Advisory"
    date: "2026-09-18"
    role: primary
  - url: "https://www.verfassungsschutz.de/SharedDocs/kurzmeldungen/DE/2026/2026-09-18-joint-cybersecurity-advisory.html"
    publisher: "Bundesamt für Verfassungsschutz (Germany)"
    date: "2026-09-18"
    role: primary
  - url: "https://therecord.media/north-korean-hackers-infect-thousands-of-devices-waterplum-scheme"
    publisher: "The Record (Recorded Future News)"
    date: "2026-09-18"
    role: corroborating
  - url: "https://www.heise.de/news/Nordkoreanische-Cybergruppe-bestiehlt-IT-Fachleute-auf-Jobsuche-11458275.html"
    publisher: "heise online"
    date: "2026-09-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "WaterPlum actors have infected at least 30,000 devices in more than 100 countries and exfiltrated funds or account credentials from over 7,000 cryptocurrency wallets. WaterPlum actors have transferred 1.7 billion Japanese yen (JPY) (equivalent to 10.71 million USD) of cryptocurrency assets to the Democratic People's Republic of Korea (DPRK)."
    publisher: "FBI/IC3 Joint Cybersecurity Advisory"
  - quote: "WaterPlum actors upload malicious Node Package Manager (NPM) packages embedded with either BeaverTail, InvisibleFerret, OtterCookie, OtterCandy, or StoatWaffle malware and related variants."
    publisher: "FBI/IC3 Joint Cybersecurity Advisory"
  - quote: "The NPA and the FBI assess both WaterPlum cyber actors and some North Korean IT workers operate under the 313 General Bureau of the Munitions Industry Department subordinate to the Central Committee of the Workers Party of Korea."
    publisher: "FBI/IC3 Joint Cybersecurity Advisory"
  - quote: "For the first time in Japan, authorities successfully identified, investigated, and dismantled a \"laptop farm\" operated by an enabler in Japan."
    publisher: "FBI/IC3 Joint Cybersecurity Advisory"
verification: multi-source
sourcing_note: null
confidence: high
references: ["2026-09-08/sekoia-kudelski-dprk-lazarus-umbrella-six-cluster-split"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Seven government agencies — Japan's National Police Agency and National Cybersecurity Office, the US FBI and DoD Cyber Crime Center, Australia's Signals Directorate/ACSC, and Germany's BND and BfV — jointly published a Cybersecurity Advisory on 2026-09-18 on the North Korean "WaterPlum" cyber-actor group, publicly known as **Contagious Interview** and already tracked here under that name ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). The advisory is the first to attach concrete scale to the campaign: at least 30,000 infected devices across more than 100 countries, funds or credentials exfiltrated from over 7,000 cryptocurrency wallets, and roughly 1.7 billion Japanese yen (about USD 10.7 million) moved to DPRK ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). Germany's BfV confirms the campaign has targeted software developers "also in Germany" (translated from German) ([Bundesamt für Verfassungsschutz, 2026-09-18](https://www.verfassungsschutz.de/SharedDocs/kurzmeldungen/DE/2026/2026-09-18-joint-cybersecurity-advisory.html)).

WaterPlum poses as recruiters — frequently impersonating AI, cryptocurrency or NFT companies, and also using legitimate freelance and recruiting platforms — to lure software developers and IT professionals into a technical interview or take-home coding assignment; victims are told to download and run files hosted on collaboration platforms and code repositories to "complete a coding assignment or troubleshoot an error." Those files carry one of five malware families the advisory names for the first time together: **BeaverTail** (a JavaScript loader hidden in NPM packages hosted on GitHub or Bitbucket), **InvisibleFerret** (a Python backdoor), **OtterCookie** (a JavaScript RAT and infostealer, already tracked here from Elastic's 2026-07-18 SVG-steganography disclosure), **OtterCandy** (combining OtterCookie and RATatouille features), and **StoatWaffle** — a modular Node.js loader, credential harvester and RAT that hides inside blockchain-themed decoy VS Code project repositories and auto-executes through a malicious VS Code configuration file the moment the victim opens and trusts the folder ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). Once backdoored, operators use the RATs for persistence and lateral pivoting while infostealers harvest browser-stored credentials, clipboard contents, keystrokes, screenshots and cryptocurrency-wallet data to a command-and-control address; the same access lets operators pursue further espionage or intellectual-property theft inside the victim's employer.

The advisory ties the malware-delivery operation to North Korea's separate, long-running remote-IT-worker placement scheme (tracked here as PurpleDelta / Jasper Sleet / UNC5267 / Wagemole / Famous Chollima): "the NPA and the FBI assess both WaterPlum cyber actors and some North Korean IT workers operate under the 313 General Bureau of the Munitions Industry Department subordinate to the Central Committee of the Workers Party of Korea" ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)) — the two operations share a parent organization even though they run distinct tradecraft. Separately, Japanese authorities disclosed "for the first time in Japan" a dismantled "laptop farm" — a facility where an enabler physically hosted employer-issued laptops and remotely operated them on North Korean workers' behalf — moving "several hundred million" yen in cryptocurrency abroad ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). The advisory records two prior cases of IT-worker escalation beyond simple wage fraud: one worker extorted an employer over its own source code after a payment dispute, and another defaced and disabled a hiring company's website.

**Defender takeaway:** this is a social-engineering-led initial-access vector, not an exploited vulnerability, so the controls are procedural rather than patch-based. HR and recruiting workflows — including at cantonal or federal IT departments and their contracted suppliers that source developer talent through crowdsourcing or freelance platforms — should never let a candidate run unreviewed take-home-assignment code with credentials or production access, should sandbox or review any coding-assignment repository before execution, and should verify a remote contractor's identity documents against known facilitator/laptop-farm patterns before onboarding. Camera avoidance, audio lag consistent with a second monitor being read from, and insistence on cryptocurrency payment are documented behavioral flags for the IT-worker variant of the same network.

**Triage:** BeaverTail/InvisibleFerret/OtterCookie-family execution shows up as a `node` or `python` process spawned from an IDE or terminal session shortly after a new project folder is opened or an `npm install` completes, followed by outbound connections to non-corporate destinations and API calls against browser credential stores or the clipboard — legitimate build tooling does not read browser credential stores or poll the clipboard. StoatWaffle's variant of the same pattern is a VS Code auto-run entry (a `.vscode` configuration file) firing on folder-open/trust in a freshly cloned, blockchain-themed repository the organization's own ticketing has no record of. The distinguishing context, in both cases, is timing correlation with an active job-interview or coding-test process rather than the presence of `node`/`npm`/VS Code activity alone.
