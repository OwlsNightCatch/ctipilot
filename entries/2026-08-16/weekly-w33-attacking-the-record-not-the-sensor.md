---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Three unrelated intrusions and one research publication worked this week attacked the evidence a responder reconstructs afterwards rather than the sensor watching at the time — and two of the week's victims proved the same point from the defending side"
headline: "W33's evasion work targeted the record, not the alarm — a shell log that stores the wrong command, and forensics tooling as camouflage"
summary: >
  Four disclosures this pipeline worked during 2026-W33 — three of them published in the days just before
  it — share a property that is not ordinary defence evasion. CrowdStrike
  catalogued 21 distinct command-obfuscation techniques across six categories in VMware ESXi's BusyBox shell
  and identified the load-bearing defect as a logging property rather than a vulnerability: ESXi shell logs
  capture commands during parsing, before expansion, so the log preserves the obfuscated form and a search
  for the literal string esxcli misses the command entirely. Group-IB documented an intruder who escalated
  to root and then spent the intrusion impersonating ordinary users through the pam_rootok policy as a
  deliberate forensic smokescreen, disabling logging services and removing authentication logs. Sophos
  investigated an Interlock intrusion in which the operator acquired a memory image with WinPmem and ran
  Volatility3's credential plugins offline against it, leaving traces indistinguishable from a real
  investigation. A six-agency advisory records Gunra affiliates editing a victim's VDI authentication files
  so one attacker-chosen one-time-password value always validated. And two European public bodies showed
  the defensive mirror in the same week — France's tax authority whose own post-intrusion access reviews
  did not reveal a theft that had already happened, and a UK health body that cannot scope a disclosure because the
  channel keeps no receiver log.
discovered_at: "2026-08-16T23:54:00Z"
event_date: "2026-08-14"
run_id: 2026-08-16T2315Z-weekly
priority: high
immediate_action: null
tags: [ransomware, organized-crime, cryptocrime, identity, ot-ics]
regions: [europe, global]
sectors: [public-sector, healthcare, technology]
entities:
  - actor:interlock
  - campaign:groupib-xmrig-pam-forensic-smokescreen
  - actor:gunra
  - incident:france-dgfip-tax-breach-2026-08
  - incident:nhs-blood-transplant-pager-breach-2026-08
techniques: [T1027, T1685.006, T1070.003, T1685.001, T1564.013, T1556.006, T1003.002, T1003.005, T1059.004, T1053.003, T1078, T1140]
affected_products: ["VMware ESXi"]
cves: []
sources:
  - url: "https://www.crowdstrike.com/en-us/blog/crowdstrike-hunts-for-shell-command-obfuscation-vmware-esx/"
    publisher: "CrowdStrike"
    date: "2026-08-07"
    role: primary
  - url: "https://www.group-ib.com/blog/xmrig-covert-linux-pam-abuse/"
    publisher: "Group-IB"
    date: "2026-07-30"
    role: primary
  - url: "https://www.sophos.com/en-us/blog/2608-volatility-interlock/"
    publisher: "Sophos X-Ops"
    date: "2026-08-07"
    role: primary
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a"
    publisher: "FBI, CISA, DC3, NSA, USSS and Republic of Korea National Police Agency"
    date: "2026-08-10"
    role: primary
  - url: "https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/"
    publisher: "Ministère de l'Économie et des Finances"
    date: "2026-08-14"
    role: primary
  - url: "https://www.bbc.co.uk/news/articles/clyj92j210do"
    publisher: "BBC News"
    date: "2026-08-14"
    role: primary
closed_sources: []
evidence:
  - quote: "The critical insight is that ESX shell logs capture commands during the parsing stage, before expansions occur."
    publisher: "CrowdStrike"
  - quote: "Any detection strategy that searches for the keyword \"esxcli\" would miss this command entirely."
    publisher: "CrowdStrike"
  - quote: "The campaign operators actively suppressed system visibility by disabling logging services and removing authentication logs to blind standard file-based monitoring."
    publisher: "Group-IB"
  - quote: "In a legitimate use scenario, use of this command could be expected as part of a DFIR investigation, a security assessment, or malware analysis."
    publisher: "Sophos X-Ops"
verification: multi-source
sourcing_note: >
  Each case rests on its own first-hand investigator — CrowdStrike's own lab validation on ESX 7.0.3,
  Group-IB's and Sophos's incident-response engagements, and the six-agency joint advisory for Gunra. The
  two victim-side cases rest on the disclosing organisations themselves. The joint advisory AA26-222A could
  not be re-fetched during this run (cisa.gov refuses the routine transport and the reader relay's credit
  pool was exhausted), so the Gunra detail is carried exactly as this pipeline's verified operational entry
  of 11 August states it. The four attacker-side cases are not connected by any cited source and this entry
  asserts no relationship between the actors; the pattern claimed is a shared objective, not a shared operator.
confidence: high
update_of: null
references:
  - 2026-08-10/esxi-busybox-ash-command-obfuscation-21-techniques
  - 2026-08-10/pam-rootok-identity-shuffle-as-anti-forensics-xmrig
  - 2026-08-10/interlock-volatility3-winpmem-credential-theft
  - 2026-08-11/gunra-raas-fortios-mfa-backdoor-linux-prng-recoverable
  - 2026-08-15/france-dgfip-tax-authority-credential-intrusion
  - 2026-08-15/nhsbt-transplant-data-unencrypted-pager-network
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

Defence evasion is normally about the moment: stay under the rule, out of the signature, off the callback. Four disclosures this pipeline carried this week are about something else — they leave the alarm alone and corrupt the account of what happened, which is the thing a responder relies on days later when the question is scope rather than presence.

CrowdStrike's ESXi research is the cleanest statement of the class because the defect is not a bug at all. Testing obfuscation against a live host, the team catalogued "21 distinct techniques across six categories, for which no public tooling or proof-of-concept frameworks previously existed" — but the finding that matters for defenders is a property of the platform's logging: "The critical insight is that ESX shell logs capture commands during the parsing stage, before expansions occur." A command assembled from hexadecimal escapes executes identically to its plain form while the log entry preserves the obfuscated version, and CrowdStrike states the consequence plainly: "Any detection strategy that searches for the keyword \"esxcli\" would miss this command entirely" ([CrowdStrike, 2026-08-07](https://www.crowdstrike.com/en-us/blog/crowdstrike-hunts-for-shell-command-obfuscation-vmware-esx/)). The log is not missing. It is present, complete, and wrong about what ran — on the platform ransomware operators reach for when they want to encrypt an estate in one action.

Group-IB's case does the same thing to the identity axis. Investigating a covert Monero-mining intrusion that began through a trusted third-party relationship, its DFIR team found an actor who escalated to root once and then, rather than operating as root, abused the `pam_rootok` policy — which lets root use `su` without a password — to move between multiple low-privileged users, spreading redundant cron persistence across those unmonitored accounts so that remediating the root compromise alone would let the implant regenerate. Group-IB describes the operators as having "actively suppressed system visibility by disabling logging services and removing authentication logs to blind standard file-based monitoring" ([Group-IB, 2026-07-30](https://www.group-ib.com/blog/xmrig-covert-linux-pam-abuse/)). The inversion is the point: a responder reading that authentication trail sees ordinary users doing ordinary things, which is precisely what a root-level intruder wanted it to say.

Sophos supplies the third variant, and it is the most uncomfortable, because the camouflage is the responder's own toolkit. In a March 2026 Interlock intrusion its incident-response team observed the operator capture a full physical-memory image with WinPmem — a legitimate acquisition tool — and then run Volatility3's `windows.hashdump.Hashdump` and `windows.cachedump.Cachedump` plugins offline against that image, rather than pointing a commodity credential dumper at the live host. Sophos states the difficulty directly: "In a legitimate use scenario, use of this command could be expected as part of a DFIR investigation, a security assessment, or malware analysis" ([Sophos X-Ops, 2026-08-07](https://www.sophos.com/en-us/blog/2608-volatility-interlock/)). Its own discriminator in the engagement was not technical at all — the customer knew of no legitimate use. The fourth case moves the corruption into the authentication record itself: the six-agency joint advisory on the Gunra ransomware-as-a-service operation records that in one case the actors edited the authentication-processing files on a victim's VDI authentication portal so that one attacker-chosen one-time-password value always validated, a durable multi-factor bypass that survives password resets ([FBI, CISA, DC3, NSA, USSS and Republic of Korea National Police Agency, 2026-08-10](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-222a)). An authentication log downstream of that edit records a successful second factor, truthfully and uselessly.

Two European public bodies demonstrated the defending side of the same problem in the same week, with no attacker sophistication involved. France's Direction générale des Finances publiques detected intrusions in June and July, cut the accounts, and ran access reviews that did not reveal that data had been stolen; the theft of records on 678,000 individuals and businesses was established only after the actor publicly claimed the access on 12 and 13 August ([Ministère de l'Économie et des Finances, 2026-08-14](https://presse.economie.gouv.fr/acces-illegitime-au-systeme-dinformation-de-la-direction-generale-des-finances-publiques/)). NHS Blood and Transplant, having broadcast transplant-patient names, dates of birth and clinical risk factors over an unencrypted paging network, cannot say who received them or how many people are affected, because pager broadcasts are one-way and receivers cannot be tracked ([BBC News, 2026-08-14](https://www.bbc.co.uk/news/articles/clyj92j210do)).

**Defender takeaway:** the attacker cases and the victim cases converge on one operational question, which is whether the evidence you would need to scope an intrusion is being produced and kept somewhere the intrusion cannot reach. Three of the four attacker techniques defeat host-resident evidence specifically — the ESXi shell log, the local authentication log, the artefact set on the compromised endpoint — and all three are answered by the same architectural choice: ship the record off the host as it is produced, so that deleting or rewriting the local copy does not remove the evidence. For ESXi in particular, forwarding shell telemetry to a collector does not by itself fix the parsing-stage problem, because the forwarded string is the obfuscated one; the detection has to key on the shape of obfuscation — encoded argument construction, command substitution in a position where a plain verb belongs — rather than on the verb it resolves to. The DGFiP case adds the review-side lesson: an access review that asks "was this account used after we cut it" answers a different question from "what did it reach before we cut it", and only the second one scopes a theft.

**Triage:** for the DFIR-tooling case, the discriminator Sophos used generalises — memory-acquisition and memory-analysis binaries have a legitimate profile that is narrow and knowable, so the test is whether the execution matches a known engagement rather than whether the tool is malicious. Concretely: acquisition tooling running on an endpoint with no open investigation, launched by an account that is not the incident-response team's, writing its image to a path outside the team's normal working location, or followed by credential-plugin execution against that image on the same host — legitimate practice usually moves the image to an analysis system rather than parsing it in place. For the identity-shuffle case, the signal is a sequence rather than an event: a root-level authentication followed by `su` transitions into several unrelated low-privileged accounts within a short window, with no corresponding interactive logon for those users and no change ticket — normal administrative work escalates toward privilege and stays there, it does not fan out downward across unrelated ordinary users. For the fixed-OTP backdoor, the discriminator is repetition where uniqueness is guaranteed by design: the same one-time-password value validating more than once, across sessions or accounts, is a property no working one-time-password implementation can produce.
