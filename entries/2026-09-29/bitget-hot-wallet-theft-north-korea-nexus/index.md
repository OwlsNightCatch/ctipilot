---
schema: 1
kind: incident
title: "Bitget: an attacker compromised two third-party security appliances, moved laterally to the wallet job server and stole $388M in one of 2026's largest crypto-exchange hacks"
headline: "Compromised security appliances, not a key theft, gave the attacker a path to Bitget's wallet server"
summary: >
  Cryptocurrency exchange Bitget confirms unauthorized transfers of approximately $388M from its hot
  and warm wallet infrastructure on 2026-09-24. Mandiant's and SlowMist's reports, released on
  2026-09-30, trace the path through two compromised third-party security appliances (SlowMist dates malicious activity on a node of its Product A to 2026-08-31, and Mandiant found a web shell with command-and-control on its appliance B), lateral
  movement to the production wallet job server, and a custom withdrawal tool that forged
  risk-control parameters. Bitget's CEO calls North Korean involvement "very likely"; TRM Labs finds laundering overlap with wallets from earlier North Korean thefts, including Bybit and AFX Bridge, through a network it ties to TraderTraitor, but states attribution is not definitive.
discovered_at: "2026-09-29T05:15:00Z"
updated_at: "2026-09-30T06:56:10Z"
event_date: "2026-09-24"
run_id: 2026-09-29T0405Z-intel
priority: notable
immediate_action: null
tags: [organized-crime, north-korea-nexus, cryptocrime]
regions: [global]
sectors: [finance]
entities: ["incident:bitget-hot-wallet-theft-2026-09", "actor:jade-sleet"]
techniques: [T1078, T1059, T1552, T1505.003, T1570, T1070.004, T1565.001, T1565.002, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response"
    publisher: "Bitget (official incident page)"
    date: "2026-09-27"
    role: primary
  - url: "https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack"
    publisher: "TRM Labs"
    date: "2026-09-25"
    role: primary
  - url: "https://thehackernews.com/2026/09/bitget-says-attacker-exploited-third.html"
    publisher: "The Hacker News"
    date: "2026-09-28"
    role: corroborating
  - url: "https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html"
    publisher: "The Hacker News"
    date: "2026-09-25"
    role: corroborating
  - url: "https://www.bitget.com/support/articles/12560603896305"
    publisher: "Bitget (support center)"
    date: "2026-09-30"
    role: primary
  - url: "https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf"
    publisher: "Mandiant (Google Cloud), status report released by Bitget"
    date: "2026-09-28"
    role: primary
  - url: "https://raw.githubusercontent.com/slowmist/Knowledge-Base/master/open-report-V2/incident-response/SlowMist%20Investigation%20Progress%20Report%20-%20Bitget_en-us.pdf"
    publisher: "SlowMist"
    date: "2026-09-29"
    role: primary
closed_sources: []
evidence:
  - quote: "the attacker may have exploited a vulnerability in a third-party security product to potentially obtain high-level internal credentials"
    publisher: "Bitget (official incident page)"
    source_url: "https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response"
  - quote: "The attacker compromised a critical backend system within our wallet infrastructure, used it to spoof transaction data, and triggered our authorization process to move funds out."
    publisher: "Bitget CEO Gracy Chen, via The Hacker News"
    source_url: "https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html"
  - quote: "these onchain links confirm the group laundering these proceeds is the same one used by TraderTraitor in other recent hacks"
    publisher: "TRM Labs"
    source_url: "https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack"
  - quote: "The threat actor deployed a web shell onto the security appliance B and established a Command-and-Control (C2) connection."
    publisher: "Mandiant (Google Cloud)"
    source_url: "https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf"
  - quote: "The earliest malicious activity identified in the available logs dates to August 31."
    publisher: "SlowMist"
    source_url: "https://raw.githubusercontent.com/slowmist/Knowledge-Base/master/open-report-V2/incident-response/SlowMist%20Investigation%20Progress%20Report%20-%20Bitget_en-us.pdf"
verification: multi-source
sourcing_note: >
  Bitget's own incident page and TRM Labs' independent on-chain forensic analysis are both primary.
  TRM Labs is explicit that attribution is assessed, not confirmed: "TRM has not yet definitively
  attributed the exploit to North Korea" and "another actor carrying out the theft remains
  technically possible." Mandiant's and SlowMist's investigation reports, released through Bitget's
  support center, describe the intrusion path; neither names the appliance vendors.
confidence: high
references: ["2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-30T06:56:10Z"
    run_id: 2026-09-30T0639Z-audit
    type: update
    summary: >
      Mandiant's and SlowMist's investigation reports, released by Bitget on 2026-09-30, trace the
      intrusion through two compromised third-party security appliances: SlowMist dates malicious activity on a node of its Product A, attacked through a zero-day, to 2026-08-31, and Mandiant reports a web shell and command-and-control on its appliance B,
      then lateral movement to the production wallet job server and a custom withdrawal tool that
      forged risk-control parameters. Priority moves from high to notable: the appliance path is a
      transferable technique worth a hunt, but the vendors are unnamed and there is no
      product-specific decision for Swiss public bodies. TRM Labs' attribution reasoning is stated as
      TRM reports it, and the earlier USD 351.6M loss and the USD 464M fund size are Bitget's own
      figures as TRM relays them.
    fields: [priority, updated_at, title, headline, summary, techniques, sources, evidence, sourcing_note, body]
migrated_from: null
---

Cryptocurrency exchange Bitget confirms that, at 18:31 UTC on 2026-09-24, unauthorized transfers occurred from a portion of its hot and warm wallet infrastructure across eleven blockchains: Ethereum, XRP Ledger, TRON, Arbitrum, Optimism, Base, BNB Smart Chain, Avalanche, Algorand, Celestia and Zcash ([Bitget, 2026-09-27](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)). Per Bitget's own investigation, the attacker did not steal a private key: "the attacker may have exploited a vulnerability in a third-party security product to potentially obtain high-level internal credentials," then used those credentials "to impersonate authorized activity and send fraudulent withdrawal commands to the wallet system," bypassing existing risk controls ([Bitget, 2026-09-27](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)). CEO Gracy Chen described the mechanism directly: "The attacker compromised a critical backend system within our wallet infrastructure, used it to spoof transaction data, and triggered our authorization process to move funds out" ([The Hacker News, 2026-09-25](https://thehackernews.com/2026/09/bitget-says-suspected-north-korean.html)). Bitget states private-key compromise was ruled out and cold wallets were unaffected; the vulnerable third-party product's vendor was notified and the affected functionality disabled pending a fix.

Total loss is now estimated at approximately $388M across twelve wallet addresses ([Bitget, 2026-09-27](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)), up from the USD 351.6M loss Bitget first reported, the figure TRM Labs uses in its analysis ([TRM Labs, 2026-09-25](https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack)). Bitget says its Protection Fund covers the financial impact ([Bitget, 2026-09-27](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)), a fund Bitget sizes at USD 464 million, according to TRM Labs ([TRM Labs, 2026-09-25](https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack)). Customer account balances, deposits and trading were unaffected, and withdrawals, paused at detection, resumed in phases starting with Bitcoin on 2026-09-28. Bitget revoked and reissued internal login credentials, restructured access to highly sensitive systems, now requires multiple approvals for critical operations, and engaged Mandiant and SlowMist for independent forensics ([Bitget, 2026-09-27](https://www.bitget.com/academy/bitget-security-incident-what-happened-timeline-impact-response)).

Bitget's CEO called North Korean involvement "very likely," based on the team's preliminary investigation linking observed IP addresses to VPN services associated with a North Korean hacking group ([TRM Labs, 2026-09-25](https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack)). TRM Labs, an independent blockchain-forensics firm, reports multiple on-chain overlaps with wallets used to launder earlier North Korean thefts, including Bybit and AFX Bridge, through a laundering network it has not linked to any other group's thefts, so the overlaps point to TraderTraitor: "these onchain links confirm the group laundering these proceeds is the same one used by TraderTraitor in other recent hacks" ([TRM Labs, 2026-09-25](https://www.trmlabs.com/resources/blog/bitget-loses-usd-3516-million-in-hot-wallet-breach-in-likely-north-korea-attack)). TRM is explicit that this stops short of definitive attribution: "TRM has not yet definitively attributed the exploit to North Korea" and "another actor carrying out the theft remains technically possible."

**Detection:** the investigators describe appliance-side activity visible before any funds moved: scripts run under a security appliance's own service process, a read of the environment variable holding a database password followed by a database connection from that node, management-platform activity under an employee identity that places system commands in task parameters or submits code through a web execution endpoint, a new outbound command-and-control connection from an appliance, and sessions from an appliance to production servers ([SlowMist, 2026-09-29](https://raw.githubusercontent.com/slowmist/Knowledge-Base/master/open-report-V2/incident-response/SlowMist%20Investigation%20Progress%20Report%20-%20Bitget_en-us.pdf)) ([Mandiant, 2026-09-28](https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf)). The first trace predates the theft by more than three weeks ([SlowMist, 2026-09-29](https://raw.githubusercontent.com/slowmist/Knowledge-Base/master/open-report-V2/incident-response/SlowMist%20Investigation%20Progress%20Report%20-%20Bitget_en-us.pdf)).

**Defender takeaway:** a security or network appliance with privileged reach into a high-value backend is part of that backend's attack surface. Treat a web shell, an unexplained script or a new outbound connection on such an appliance as a possible intrusion into everything it can reach, not as a device fault, and require independent approvals for high-value transactions so that one compromised host cannot alone trigger a transfer. The appliance vendors are unnamed, so this incident carries no product-specific patch decision.

## Update — 2026-09-30T06:56:10Z

Bitget released the independent investigation reports from Mandiant and SlowMist on 2026-09-30. Both identify the compromise of third-party security products as what enabled access to the wallet environment ([Bitget, 2026-09-30](https://www.bitget.com/support/articles/12560603896305)). Mandiant's status report states that on 2026-09-24 the attacker "gained unauthorised privileged access to Bitget's third party security appliances A and B", deployed a web shell on appliance B, established a command-and-control connection, and used that persistent access to move laterally to Bitget's production wallet job server and deploy malicious packages ([Mandiant, 2026-09-28](https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf)).

The two reports date different events and label the appliances independently: Mandiant dates the attacker's privileged access to appliances A and B to 2026-09-24 ([Mandiant, 2026-09-28](https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf)), while SlowMist dates the earliest malicious activity in its logs, on a node of its Product A, to 2026-08-31 ([SlowMist, 2026-09-29](https://raw.githubusercontent.com/slowmist/Knowledge-Base/master/open-report-V2/incident-response/SlowMist%20Investigation%20Progress%20Report%20-%20Bitget_en-us.pdf)).

SlowMist dates the earliest malicious activity in the available logs to 2026-08-31: a zero-day vulnerability in a service on one of Product A's nodes let the attacker run a hidden script under the service process, read the environment variable holding the database password and connect to the database, and the same hidden-script activity appeared on two more nodes on 2026-09-23 and 2026-09-25 (UTC+8). Early on 2026-09-25 (UTC+8) the attacker entered Product B's management platform under an internal employee's identity, made three attempts to inject system commands into task parameters to write malicious files, and then submitted code through the platform's web execution endpoint, attempting to modify server configuration, write a communication relay file and upload and assemble malicious program files in batches. SlowMist also recovered, from files the attacker had deleted, a withdrawal tool built for Bitget's withdrawal logic that forged risk-control parameters and invoked the withdrawal process, and records that the attacker later tried to alter withdrawal records directly in the wallet database ([SlowMist, 2026-09-29](https://raw.githubusercontent.com/slowmist/Knowledge-Base/master/open-report-V2/incident-response/SlowMist%20Investigation%20Progress%20Report%20-%20Bitget_en-us.pdf)). Neither report names the appliance vendors.

For defenders, the appliance class is security and network appliances with privileged reach into a production backend, and the observable behaviour is a web shell or hidden script running under the appliance's own service process, a new outbound command-and-control connection from the appliance, and sessions from the appliance to production servers ([Mandiant, 2026-09-28](https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf)) ([SlowMist, 2026-09-29](https://raw.githubusercontent.com/slowmist/Knowledge-Base/master/open-report-V2/incident-response/SlowMist%20Investigation%20Progress%20Report%20-%20Bitget_en-us.pdf)).
