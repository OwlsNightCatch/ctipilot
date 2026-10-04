---
schema: 1
kind: threat
title: "WaterPlum (\"Contagious Interview\"): a seven-agency joint advisory counts 30,000+ devices in 100+ countries and $10.7M in crypto from December 2025 to July 2026, and discloses Japan's first dismantled \"laptop farm\""
headline: "Seven agencies report DPRK's fake-interview crew infected 30,000+ devices and took $10.7M in crypto between December 2025 and July 2026"
summary: >
  Japan's NPA and NCO, the US FBI and DoD Cyber Crime Center, Australia's ASD/ACSC and Germany's BND
  and BfV jointly published a Cybersecurity Advisory on 2026-09-18 on the DPRK "WaterPlum" cyber-actor
  group, the long-running campaign publicly known as "Contagious Interview". From around December 2025 through July 2026 it counts 30,000+ infected devices across 100+ countries, funds or credentials exfiltrated from 7,000+ cryptocurrency
  wallets, and roughly USD 10.7 million transferred to DPRK. The advisory names five malware
  families delivered via fake technical-interview coding assignments and reports Japan's first
  dismantled DPRK "laptop farm."
discovered_at: "2026-09-19T04:40:00Z"
updated_at: null
event_date: "2026-09-18"
run_id: 2026-09-19T0409Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, phishing, cryptocrime, supply-chain, north-korea-nexus]
regions: [global, europe]
sectors: [public-sector, technology, finance]
entities: ["campaign:contagious-interview", "malware:beavertail", "malware:invisibleferret", "malware:ottercandy", "malware:stoatwaffle", "tool:ottercookie"]
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
updates:
  - at: "2026-09-30T07:02:21Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      The priority moves from high to notable: the advisory documents an established campaign and
      asks no new decision of Swiss public bodies this week. The text had equated the advisory's
      North Korean IT workers with vendor aliases the advisory never uses, and the PurpleDelta
      IT-worker actor is no longer linked. It also claimed the advisory was the first to quantify
      the campaign and to name the five families together, listed interview flags the advisory does
      not give, and gave the advisory's figures without their December 2025 to July 2026 period. The
      title, headline, summary and main text now follow the advisory, including its interview flags,
      its statement that some WaterPlum actors also work as IT workers, its laptop-farm definition
      and its BeaverTail description, and the takeaway gains its VS Code and command-line controls.
    fields: [priority, body, title, summary, entities, headline]
migrated_from: null
---

Seven government agencies (Japan's National Police Agency and National Cybersecurity Office, the US FBI and DoD Cyber Crime Center, Australia's Signals Directorate/ACSC, and Germany's BND and BfV) jointly published a Cybersecurity Advisory on 2026-09-18 on the North Korean "WaterPlum" cyber-actor group, publicly known as **Contagious Interview** ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). The advisory puts figures on the campaign from around December 2025 through July 2026: at least 30,000 infected devices across more than 100 countries, funds or credentials exfiltrated from over 7,000 cryptocurrency wallets, and roughly 1.7 billion Japanese yen (about USD 10.7 million) moved to DPRK ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). Germany's BfV confirms the campaign has targeted software developers "also in Germany" (translated from German) ([Bundesamt für Verfassungsschutz, 2026-09-18](https://www.verfassungsschutz.de/SharedDocs/kurzmeldungen/DE/2026/2026-09-18-joint-cybersecurity-advisory.html)).

WaterPlum poses as recruiters, frequently impersonating AI, cryptocurrency or NFT companies and also using legitimate freelance and recruiting platforms, to lure software developers and IT professionals into a technical interview or take-home coding assignment; victims are told to download and run files hosted on collaboration platforms and code repositories to "complete a coding assignment or troubleshoot an error." Those files carry one of five malware families the advisory names: **BeaverTail** (JavaScript-based malware hidden inside NPM packages and downloadable from GitHub or Bitbucket), **InvisibleFerret** (a Python backdoor), **OtterCookie** (a JavaScript RAT and infostealer), **OtterCandy** (combining OtterCookie and RATatouille features), and **StoatWaffle**, a modular Node.js loader, credential harvester and RAT that hides inside blockchain-themed decoy VS Code project repositories and auto-executes through a malicious VS Code configuration file the moment the victim opens and trusts the folder ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). Once backdoored, operators use the RATs for persistence and lateral pivoting while infostealers harvest browser-stored credentials, clipboard contents, keystrokes, screenshots and cryptocurrency-wallet data to a command-and-control address; the same access lets operators pursue further espionage or intellectual-property theft inside the victim's employer.

The advisory ties the malware-delivery operation to North Korea's remote-IT-worker placement scheme: "the NPA and the FBI assess both WaterPlum cyber actors and some North Korean IT workers operate under the 313 General Bureau of the Munitions Industry Department subordinate to the Central Committee of the Workers Party of Korea" ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). It adds that some WaterPlum actors also operate as North Korean IT workers, and that both used the same IP addresses when accessing laptop farms, using crowdsourcing services and applying for positions at a Japanese cryptocurrency exchange ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). Separately, Japanese authorities "for the first time in Japan" identified and dismantled a "laptop farm" operated by an enabler in Japan, and obtained evidence that the actor group transferred "several hundred million" yen in cryptocurrency abroad. The advisory defines a laptop farm as a location, often an enabler's residence, where employment-related computers are set up and remotely controlled by North Korean IT workers ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). The advisory records two prior cases of IT-worker escalation beyond simple wage fraud: one worker extorted a company over payment and published its proprietary source code online, and another defaced and disabled a hiring company's website ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)).

**Defender takeaway:** this is a social-engineering-led initial-access vector, not an exploited vulnerability, so the controls are procedural rather than patch-based. HR and recruiting workflows, including at cantonal or federal IT departments and their contracted suppliers that source developer talent through crowdsourcing or freelance platforms, should never let a candidate run unreviewed take-home-assignment code with credentials or production access, should sandbox or review any coding-assignment repository before execution, and should verify a remote contractor's identity documents against known facilitator/laptop-farm patterns before onboarding. The advisory's interview flags for suspected North Korean IT workers are refusals or excuses regarding in-person meetings, requests to receive payment in cryptocurrency, frequent glances at another monitor as if reading from the screen, occasional background voices, and repeated video or audio freezes ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)). For developers and their endpoints, the advisory's controls are to open unknown VS Code projects only in Restricted Mode, by answering "No" to the prompt asking whether to trust the authors of the files in the folder, which stops `.vscode/tasks.json` from running on launch. Developers should check any `tasks.json` for code that downloads or executes further files, avoid opening unknown projects from a path previously marked as trusted, run unknown code only in a sandbox or virtual machine, and be especially cautious of commands or scripts containing strings such as curl, base64, -enc, mshta, Invoke-WebRequest or hidden ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)).

**Triage:** BeaverTail/InvisibleFerret/OtterCookie-family execution shows up as a `node` or `python` process spawned from an IDE or terminal session shortly after a new project folder is opened or an `npm install` completes, followed by outbound connections to non-corporate destinations and API calls against browser credential stores or the clipboard — legitimate build tooling does not read browser credential stores or poll the clipboard. StoatWaffle's variant of the same pattern is a VS Code auto-run entry (a `.vscode` configuration file) firing on folder-open/trust in a freshly cloned, blockchain-themed repository the organization's own ticketing has no record of. The distinguishing context, in both cases, is timing correlation with an active job-interview or coding-test process rather than the presence of `node`/`npm`/VS Code activity alone.

## Correction — 2026-09-30T07:02:21Z

The advisory does not name the IT-worker scheme by any vendor alias, and it does not claim to be the first to quantify the campaign or to name its five malware families together. Its only first is Japan's dismantled laptop farm. It gives its device, wallet and USD 10.7 million figures for the period from around December 2025 through July 2026, not for the campaign as a whole. Its interview flags for suspected North Korean IT workers are refusals or excuses regarding in-person meetings, requests for cryptocurrency payment, glances at another monitor, background voices, and repeated video or audio freezes ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)).

The advisory describes BeaverTail as JavaScript-based malware hidden inside NPM packages and downloadable from GitHub or Bitbucket, not as a loader ([FBI/IC3, 2026-09-18](https://www.ic3.gov/CSA/2026/260918.pdf)).
