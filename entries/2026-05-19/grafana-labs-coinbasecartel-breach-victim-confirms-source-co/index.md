---
schema: 1
kind: incident
title: "Grafana Labs confirms GitHub breach claimed by CoinbaseCartel: a workflow token missed after the TanStack npm compromise let attackers download its code and internal repositories"
headline: "Grafana Labs: a GitHub workflow token missed after the TanStack npm compromise let attackers take its codebase"
summary: "Grafana Labs confirmed on 2026-05-17 that an unauthorized party used a token for its GitHub environment to download its codebase, two days after the data-extortion group CoinbaseCartel listed it on its leak site, and refused the ransom demand. Its update of 2026-05-19 traces the breach to the TanStack npm supply-chain attack attributed to TeamPCP, detected on 2026-05-11, after which a missed GitHub workflow token let the attackers in; the download also took internal repositories holding business contact names and email addresses, while customer production systems and Grafana Cloud were not affected."
discovered_at: "2026-05-19T05:00:08Z"
event_date: 2026-05-17
run_id: 2026-05-19-2505c918
priority: notable
immediate_action: null
tags:
  - data-breach
  - supply-chain
  - organized-crime
regions:
  - global
sectors:
  - technology
entities:
  - "incident:grafana-labs-coinbasecartel-pwn-request-github-actions-breac"
  - "actor:coinbasecartel"
techniques: [T1195.001, T1528, T1213.003, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/"
    publisher: SecurityWeek
    date: "2026-05-18"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/"
    publisher: BleepingComputer
    date: "2026-05-18"
    role: corroborating
  - url: "https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html"
    publisher: The Hacker News
    date: "2026-05-17"
    role: corroborating
  - url: "https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html"
    publisher: The Hacker News
    date: "2026-05-20"
    role: corroborating
  - url: "https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/"
    publisher: Grafana Labs
    date: "2026-05-19"
    role: primary
closed_sources: []
evidence:
  - quote: "Grafana confirmed suffering a data breach on Sunday, two days after a cybercrime group listed the company on its leak website."
    publisher: SecurityWeek
    source_url: "https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/"
  - quote: "We performed analysis and quickly rotated a significant number of GitHub workflow tokens, but a missed token led to the attackers gaining access to our GitHub repositories,"
    publisher: Grafana Labs (via The Hacker News)
    source_url: "https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html"
  - quote: "This includes business contact names and email addresses that would be exchanged in a professional relationship context, not information pulled from or processed through the use of production systems or the Grafana Cloud platform."
    publisher: Grafana Labs (via The Hacker News)
    source_url: "https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html"
  - quote: "After publishing this article, the ShinyHunters extortion gang told BleepingComputer that the CoinbaseCartel is not linked to their group or ransomware operation."
    publisher: BleepingComputer
    source_url: "https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/"
verification: multi-source
sourcing_note: >
  Grafana Labs is the source of the breach facts, through its posts on X and its update of 2026-05-19 as reported by SecurityWeek, BleepingComputer and The
  Hacker News; the CoinbaseCartel claim and the group's links to other crews come from leak-site trackers and security firms, and ShinyHunters disputes them.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-19.md
updates:
  - at: "2026-10-21T20:40:06Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Grafana Labs traces its GitHub breach to the TanStack npm supply-chain attack attributed to TeamPCP,
      after which a GitHub workflow token missed during rotation let the attackers in, not to a
      pull_request_target Pwn-Request misconfiguration. The download was not limited to source code: it
      included internal repositories with business contact names and email addresses, though not
      production systems or Grafana Cloud. ShinyHunters denies any link to CoinbaseCartel, whose victim
      count is 105 by SecurityWeek's reckoning and 170 by The Hacker News's.
    fields: [affected_products, body, classification, entities, event_date, evidence, headline, regions, sectors, sources, sourcing_note, summary, techniques, title]
---

Grafana Labs said in posts on X that an unauthorized party had obtained a token granting access to its GitHub environment and downloaded its codebase, that no customer data or personal information was accessed and customer systems were unaffected, and that it would not pay the attacker's extortion demand, following FBI guidance ([The Hacker News, 2026-05-17](https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html); [BleepingComputer, 2026-05-18](https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/)). SecurityWeek dates the confirmation to Sunday 2026-05-17, two days after the group CoinbaseCartel listed Grafana on its leak site on 2026-05-15 ([SecurityWeek, 2026-05-18](https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/)). In its update of 2026-05-19, Grafana said the incident originated from the TanStack npm supply-chain attack via the Mini Shai-Hulud campaign, that it detected the malicious activity on 2026-05-11 and rotated a significant number of GitHub workflow tokens, but that a missed token, from a workflow it had first deemed not impacted, gave the attackers access to its repositories ([Grafana Labs, 2026-05-19](https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/)); The Hacker News attributes the TanStack attack to TeamPCP ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html)). The download covered public and private source code and internal repositories some teams use for operational information, including business contact names and email addresses, but not production systems or the Grafana Cloud platform; the ransom demand from an unnamed actor arrived on 2026-05-16, and Grafana has since rotated automation tokens, implemented enhanced monitoring and audited all commits since the May 11 incident ([Grafana Labs, 2026-05-19](https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/)).

CoinbaseCartel, active since September 2025, steals data and extorts victims without encrypting files; SecurityWeek counts 105 victims on its site, while The Hacker News, citing Halcyon and FortiGuard Labs, puts the total at 170 ([SecurityWeek, 2026-05-18](https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/); [The Hacker News, 2026-05-17](https://thehackernews.com/2026/05/grafana-github-token-breach-led-to.html)). Security firms link the group to ShinyHunters, Scattered Spider and Lapsus$ ([SecurityWeek, 2026-05-18](https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/)), but ShinyHunters told BleepingComputer that CoinbaseCartel is not linked to it ([BleepingComputer, 2026-05-18](https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/)). Grafana's paying customers include governments, banks and infrastructure operators, and more than 7,000 organizations use the product ([BleepingComputer, 2026-05-18](https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/)).

**Exposure:** organizations whose build pipelines took in the compromised TanStack npm packages, where any CI workflow token left unrotated afterwards stays usable, as one did at Grafana ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html)). Grafana reports no impact on customer production systems or Grafana Cloud ([Grafana Labs, 2026-05-19](https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/)).

**Detection:** in source-control audit logs, repository downloads and clones made with workflow tokens, including those of workflows judged unaffected after a dependency compromise; Grafana's attackers came in through exactly such a workflow ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html)).

**Defender takeaway:** after a dependency compromise reaches CI, rotate every workflow token, including those of workflows that look unaffected, and confirm the rotation is complete, since one missed token was enough here ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html)). Grafana users have no product action to take: Grafana reports no customer impact and has audited its commits for malicious changes ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html)).

## Correction — 2026-10-21T20:40:06Z

No source on the May 2026 breach describes a pull_request_target or Pwn-Request mechanism: Grafana says the incident originated from the TanStack npm supply-chain attack via the Mini Shai-Hulud campaign, detected on 2026-05-11, and that a GitHub workflow token missed during the rotation that followed gave the attackers access ([Grafana Labs, 2026-05-19](https://grafana.com/blog/grafana-labs-security-update-latest-on-tanstack-npm-supply-chain-ransomware-incident/)), an attack The Hacker News attributes to TeamPCP ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html)). The theft was not limited to source code: the downloaded content also included internal repositories holding operational information and business contact names and email addresses, while production systems and the Grafana Cloud platform were not involved ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html)). The link between CoinbaseCartel and ShinyHunters is contested, since ShinyHunters told BleepingComputer the group is not linked to it ([BleepingComputer, 2026-05-18](https://www.bleepingcomputer.com/news/security/grafana-says-stolen-github-token-let-hackers-steal-codebase/)), and SecurityWeek counts 105 victims on CoinbaseCartel's site rather than about 170 ([SecurityWeek, 2026-05-18](https://www.securityweek.com/grafana-confirms-breach-after-hackers-claim-they-stole-data/)). No source places Grafana in Swiss or EU public-sector monitoring estates or calls for watching unofficial Grafana plugins; Grafana says it audited all commits for malicious activity ([The Hacker News, 2026-05-20](https://thehackernews.com/2026/05/grafana-github-breach-exposes-source.html)).
