---
schema: 1
kind: incident
title: "RIKEN Fugaku and Rikyu supercomputers: an intruder entered the internal operational network through the internet-facing operating-status dashboard, planted malicious programs on internal servers and took users' stored SSH private keys and access keys, then tried them on other systems"
headline: "RIKEN Fugaku: intruder entered via the public status dashboard, exfiltrated 430 SSH private keys, tried some elsewhere"
summary: >
  RIKEN says that between 2026-11-10 and 2026-11-13 an external party used the publicly accessible web page showing Fugaku's operating status to enter its internal operational network, tampered with internal servers (some with malicious programs) and collected and exfiltrated credentials users had stored for other systems: RIKEN's second notice of 2026-11-20 counts 430 SSH private keys, 233 of them without a passphrase. Up to 4,222 Fugaku and 375 Rikyu users are affected, RIKEN confirmed that some of the stolen credentials were tried against other systems, and it suspended Fugaku on 2026-11-14. How the dashboard was breached is still under investigation, and RIKEN names no actor.
discovered_at: "2026-11-18T05:08:00Z"
updated_at: "2026-11-22T14:47:21Z"
event_date: "2026-11-16"
run_id: 2026-11-18T0356Z-intel
priority: notable
immediate_action: null
tags: [data-breach, identity]
regions: [apac]
sectors: [education, technology]
entities: ["incident:riken-fugaku-rikyu-unauthorized-access-2026-11"]
techniques: [T1190, T1552.004]
affected_products: []
cves: []
sources:
  - url: "https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html"
    publisher: "RIKEN (notice of 2026-11-16, English page dated 2026-11-17)"
    date: "2026-11-17"
    role: primary
  - url: "https://www.riken.jp/en/news_pubs/news/2026/20261120_1/index.html"
    publisher: "RIKEN (second notice)"
    date: "2026-11-20"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/japan-takes-fugaku-supercomputer-offlline-after-cyberattack/"
    publisher: "BleepingComputer"
    date: "2026-11-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "an external third party gained unauthorized access to Fugaku’s internal operational network by using a publicly accessible web page displaying Fugaku’s operational status (the dashboard)."
    publisher: "RIKEN"
    source_url: "https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html"
  - quote: "The exact method that was used to gain unauthorized access is currently under investigation."
    publisher: "RIKEN"
    source_url: "https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html"
  - quote: "Furthermore, we have confirmed that the unauthorized party attempted to connect to other systems using some of the obtained credentials."
    publisher: "RIKEN"
    source_url: "https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html"
  - quote: "We have confirmed evidence that authentication credentials (such as SSH private keys) used to connect to external systems (e.g., supercomputers or cloud services operated by other organizations) were collected and exfiltrated from the home directories of some users."
    publisher: "RIKEN (second notice)"
    source_url: "https://www.riken.jp/en/news_pubs/news/2026/20261120_1/index.html"
verification: single-source-victim
sourcing_note: >
  RIKEN's own notice about its incident; BleepingComputer restates it and adds nothing independent. RIKEN's English page gives the Fugaku user count as 4,222 in the overview and 4,224 in one list; 4,222 plus 375 Rikyu users matches the stated total of 4,597. RIKEN says the exact intrusion method is under investigation and lists addressing vulnerabilities in the exploited software among its remediation steps without naming a product or flaw.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-11-22T14:47:21Z"
    run_id: 2026-11-22T1407Z-audit
    type: update
    summary: >
      RIKEN's second notice of 2026-11-20 confirms the exfiltration of 430 SSH private keys for external
      systems (233 without a passphrase), identifies access traces to Fugaku users' registration data, and
      ties Fugaku's restart to separating public services from the administrative network.
    fields: [body, evidence, headline, sources, summary]
migrated_from: null
---

RIKEN's Center for Computational Science says that between 2026-11-10 and 2026-11-13 an external third party entered Fugaku's internal operational network through the publicly accessible web page that displays the supercomputer's operating status, and that the exact method is still under investigation ([RIKEN, 2026-11-17](https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html)). The intruder tampered with multiple internal servers, some of them with malicious programs; up to 4,222 Fugaku users and 375 Rikyu users are affected ([RIKEN, 2026-11-17](https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html)). From users' home directories it collected and exfiltrated credentials for connecting to external systems such as other organisations' supercomputers and cloud services: 430 SSH private keys, 233 of them without a passphrase and 197 with one ([RIKEN, 2026-11-20](https://www.riken.jp/en/news_pubs/news/2026/20261120_1/index.html)). RIKEN has confirmed that the intruder tried some of the obtained credentials against other systems and is checking whether damage or secondary misuse followed ([RIKEN, 2026-11-17](https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html)).

RIKEN and the external provider that maintains the system began investigating suspicious network traffic on 2026-11-12, confirmed the access on 2026-11-13 and suspended Fugaku on 2026-11-14 ([RIKEN, 2026-11-17](https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html)). It replaced the administrative keys, invalidated the public keys all users use to log in and halted all running and queued jobs, and it names no actor; it says there is no evidence yet that research data was exfiltrated ([RIKEN, 2026-11-17](https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html); [BleepingComputer, 2026-11-17](https://www.bleepingcomputer.com/news/security/japan-takes-fugaku-supercomputer-offlline-after-cyberattack/)).

**Exposure:** a shared compute or research system whose operating-status page is reachable from the internet and sits on a network path to its internal operations servers, and whose users keep SSH private keys or cloud access keys in their home directories ([RIKEN, 2026-11-17](https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html)). Relevant to Swiss research and high-performance-computing operators as a transferable pattern of exposure.

**Detection:** authentications to other systems with keys that belong to users of the affected host, arriving from unfamiliar addresses, and changes or unknown programs on the servers that run the system's operation; RIKEN's own reviews cover the network configuration and the rebuilding of compromised servers ([RIKEN, 2026-11-17](https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html)).

**Defender takeaway:** treat every private key and access key stored on a compromised host as stolen, and a key without a passphrase as usable at once: RIKEN asks users to revoke the matching public key at each external service where it is authorised and to generate a new pair, and to replace any other stored credential through the service concerned ([RIKEN, 2026-11-17](https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html)). A status page that is public should not give a route into the operations network.

## Update — 2026-11-22T14:47:21Z

RIKEN's second notice confirms what the first said only might have happened: the intruder collected and exfiltrated SSH private keys and similar credentials for external systems from users' home directories, 430 keys in all, 233 without a passphrase and 197 with one ([RIKEN, 2026-11-20](https://www.riken.jp/en/news_pubs/news/2026/20261120_1/index.html)). It has also identified access traces to the registration data of the 4,222 Fugaku users (address, affiliation, phone numbers and the type of identity document used), reports no misuse beyond the connection attempts already disclosed, and says Fugaku resumes only after public services are separated from the administrative network and the servers are rebuilt ([RIKEN, 2026-11-20](https://www.riken.jp/en/news_pubs/news/2026/20261120_1/index.html)).
