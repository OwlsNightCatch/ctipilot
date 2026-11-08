---
schema: 1
kind: incident
title: "Binance's own report on the 2026-10-29 theft of about USD 6.34 billion: a fake recruiter's coding assignment compromised an engineer's laptop, an internal AI tool carried the attacker to two colleagues and a container-deployment token, and a deployed container reached the wallet signing service; the FBI attributes it to North Korea's TraderTraitor"
headline: "Binance's report: fake recruiter, trojaned pyenv, AI-tool pivot and a deployment token reached the signing service"
summary: >
  Binance's report of 2026-11-03 says the theft of about USD 6.34 billion on 2026-10-29 was a multi-stage campaign: in September a software engineer contacted through a job platform was led through
  two fake interviews and told to download an assignment repository to his work computer, whose setup code replaced the pyenv executable in the Homebrew install with a malicious one that endpoint
  protection did not detect. On 2026-10-20 the attacker used that computer and an internal AI tool to take over two wallet-team engineers and found a container-deployment token, which on 2026-10-29 let it deploy a
  container and run a script that reached the wallet signing service. The FBI says North Korea was responsible and calls the activity TraderTraitor; Binance says some technical details stay confidential.
discovered_at: "2026-11-04T03:50:00Z"
updated_at: null
event_date: "2026-10-29"
run_id: 2026-11-04T0256Z-intel
priority: notable
immediate_action: null
tags: [cryptocrime, nation-state, supply-chain, ai-abuse]
regions: [global]
sectors: [finance, technology]
entities: ["actor:jade-sleet", "incident:binance-wallet-signing-service-theft-2026-10"]
techniques: [T1566.003, T1204.002, T1195.002, T1059.004, T1528, T1078, T1070]
affected_products: []
cves: []
sources:
  - url: "https://www.binance.com/en/blog/community/3229153443759566763"
    publisher: "Binance (Initial Findings and Response Update)"
    date: "2026-11-03"
    role: primary
  - url: "https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack"
    publisher: "FBI"
    date: "2026-10-31"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/binance-says-fake-job-interview-led-to-63-billion-crypto-heist/"
    publisher: "BleepingComputer"
    date: "2026-11-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Our current investigation indicates that this was a sophisticated, multi-stage campaign. It was not a single isolated breach or a simple phishing incident."
    publisher: "Binance"
    source_url: "https://www.binance.com/en/blog/community/3229153443759566763"
  - quote: "The attacker leveraged the compromised computer of engineer B and used an internal AI tool to gain control over the Wallet DevOps Engineer A and another Wallet Software Engineer C."
    publisher: "Binance"
    source_url: "https://www.binance.com/en/blog/community/3229153443759566763"
  - quote: "The 0-day malware was not detected by the endpoint security protection tools at the time."
    publisher: "Binance"
    source_url: "https://www.binance.com/en/blog/community/3229153443759566763"
  - quote: "The FBI refers to this specific North Korean malicious cyber activity as \"TraderTraitor.\""
    publisher: "FBI"
    source_url: "https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack"
verification: single-source-victim
sourcing_note: >
  Binance's report is the victim's own first account and the only source for the intrusion chain; the company says some technical details stay confidential and an independent review is under way. The FBI's statement
  covers attribution only, and Binance itself makes no independent attribution claim. BleepingComputer restates the report and draws the comparison with North Korean fake-interview campaigns, which Binance does not name.
confidence: high
references:
  - 2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-11-08T14:05:26Z"
    run_id: 2026-11-08T1309Z-audit
    type: correction
    summary: >
      Binance says only that the attacker used an internal AI tool to gain control over two colleagues and
      keeps technical details confidential, so how the tool was abused is not disclosed; the access-log
      detection idea for internal AI tools is an inference from that takeover.
    fields: [body]
migrated_from: null
---

Binance says the theft of about USD 6.34 billion in digital assets on 2026-10-29 was "a sophisticated, multi-stage campaign" and not a single breach or a simple phishing incident ([Binance, 2026-11-03](https://www.binance.com/en/blog/community/3229153443759566763)). In September 2026 a software engineer whose job-platform profile named Binance was approached by a person posing as a project director, interviewed by a purported HR representative on live video and then by a purported CEO in a chat application, and told to download an "assignment" repository onto his work computer; its setup code replaced the legitimate pyenv executable in the Homebrew installation with a malicious version, repointed the symlink and spawned a zsh shell, and the 0-day malware was not detected by endpoint protection ([Binance, 2026-11-03](https://www.binance.com/en/blog/community/3229153443759566763)). On 2026-10-20 the attacker used that computer and an internal AI tool to gain control over a wallet DevOps engineer and a second wallet software engineer, and found a container-deployment permission token on the first engineer's computer; on 2026-10-29 it logged onto the second engineer's computer with the stolen credentials, deployed a container and triggered a script that launched the attack on the wallet signing service ([Binance, 2026-11-03](https://www.binance.com/en/blog/community/3229153443759566763)). Binance reports an earlier supply-chain event in June 2026, when a wallet DevOps engineer installed a tampered Homebrew installation while searching for an AI coding tool, and says its security team blocked 57 suspected North Korea-linked cases in 2026 ([Binance, 2026-11-03](https://www.binance.com/en/blog/community/3229153443759566763)). The FBI says North Korea was responsible and calls the activity "TraderTraitor" ([FBI, 2026-10-31](https://www.fbi.gov/investigate/cyber/alerts/2026/north-korea-responsible-for-6-billion-binance-attack)). BleepingComputer notes that fake job interviews leading to malware installs are a common tactic of the North Korean campaigns known as Contagious Interview and Operation Dream Job, a comparison Binance does not make ([BleepingComputer, 2026-11-03](https://www.bleepingcomputer.com/news/security/binance-says-fake-job-interview-led-to-63-billion-crypto-heist/)).

The transfer to other organisations is the access chain, not the loss: a developer endpoint reached through a recruiting lure, a trojaned version-manager binary that endpoint protection missed, an internal AI tool through which the attacker gained control over two colleagues, by a method Binance keeps confidential, and a deployment token that turned one workstation into code execution in a trusted pipeline.

**Exposure:** any organisation whose developers, DevOps or administrators can be approached through job platforms and run third-party assignment code on managed laptops, and any internal AI assistant or agent reachable from a compromised employee endpoint.

**Detection:** in endpoint file-event telemetry, a version-manager or interpreter binary deleted, renamed and re-linked inside a package-manager directory followed by a shell spawned from it, which is the sequence Binance describes for pyenv in the Homebrew installation ([Binance, 2026-11-03](https://www.binance.com/en/blog/community/3229153443759566763)); in process lineage, shells started from a repository's setup scripts; in token-use logs, a container-deployment token used from a host that is not its owner's; in the access logs of internal AI tools, activity that touches other employees' accounts or endpoints from one user's session, a pattern the takeover of two colleagues through such a tool implies (an inference; Binance does not describe the mechanism).

**Defender takeaway:** treat a recruiter's "assignment" repository as untrusted code and keep it off managed machines, restrict what an internal AI tool can reach with one user's session and what a stored deployment token can deploy, and alert on shells spawned from replaced developer-tool binaries; Binance's own stated fixes are tighter device controls, rebuilt systems and tools, rotated credentials and tokens, and AI-based behavioural anomaly detection ([Binance, 2026-11-03](https://www.binance.com/en/blog/community/3229153443759566763)).

## Correction — 2026-11-08T14:05:26Z

Binance's report says the attacker "used an internal AI tool to gain control over" two further engineers and that some technical details will remain confidential ([Binance, 2026-11-03](https://www.binance.com/en/blog/community/3229153443759566763)); it does not say how the tool was abused, so the earlier description of it letting one user act on colleagues' machines went beyond the source. The access-log pattern for internal AI tools is an inference from that takeover, not a mechanism Binance describes.
