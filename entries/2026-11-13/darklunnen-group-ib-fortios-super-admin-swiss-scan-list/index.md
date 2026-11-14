---
schema: 1
kind: threat
title: 'DarkLunnen: Group-IB''s exposed operator directory shows mass exploitation of FortiOS CVE-2024-55591 that plants a ''service'' super_admin account, a 4,725-target Swiss FortiGate scan list and restic access to an S3 backup repository at a ''Swiss domain''; Group-IB does not confirm any Swiss victim'
headline: 'Group-IB: DarkLunnen''s FortiOS chain leaves a ''service'' super_admin; Swiss FortiGates are scan targets only'
summary: 'Group-IB found an open directory on a Latvian server that documents more than 14 months of operations against Europe by an operator it tracks as DarkLunnen and links to no known actor: a modified public exploit for FortiOS CVE-2024-55591 that creates an administrator named service with super_admin privileges, among other tools. Group-IB recovered a list of 4,725 Swiss FortiGate scanning targets, which it says does not confirm vulnerability or exploitation, and restic commands that accessed an S3 backup repository at a Swiss domain in May and June 2025, without naming an organisation or confirming success.'
discovered_at: '2026-11-13T04:05:00Z'
updated_at: null
event_date: '2026-11-11'
run_id: 2026-11-13T0256Z-intel
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
regions:
  - europe
  - switzerland
sectors:
  - public-sector
entities:
  - actor:darklunnen
  - product:fortinet-fortios
techniques:
  - T1595.001
  - T1595.002
  - T1190
  - T1133
  - T1078
  - T1136.001
  - T1505.003
affected_products:
  - Fortinet FortiOS
  - Fortinet FortiProxy
cves: []
sources:
  - url: https://www.group-ib.com/blog/offensive-cyber-operations-europe/
    publisher: Group-IB Threat Intelligence
    date: '2026-11-11'
    role: primary
  - url: https://fortiguard.fortinet.com/psirt/FG-IR-24-535
    publisher: Fortinet PSIRT (FG-IR-24-535)
    date: '2025-01-14'
    role: corroborating
closed_sources: []
evidence:
  - quote: DarkLunnen used a modified proof-of-concept (PoC) exploit developed by watchTowr for FortiGate CVE-2024-55591, designed to create a backdoor super-admin account named “service”.
    publisher: Group-IB Threat Intelligence
    source_url: https://www.group-ib.com/blog/offensive-cyber-operations-europe/
  - quote: Additional FortiGate scanning target lists were recovered for Switzerland (4,725 targets), South Korea (5,199), and Ireland (647). These lists identify scanning targets but do not confirm vulnerability or successful exploitation.
    publisher: Group-IB Threat Intelligence
    source_url: https://www.group-ib.com/blog/offensive-cyber-operations-europe/
  - quote: For several of these operations, the available evidence is limited to recorded commands. Unless otherwise indicated, the findings do not independently confirm successful exploitation, unauthorized access, or data exfiltration.
    publisher: Group-IB Threat Intelligence
    source_url: https://www.group-ib.com/blog/offensive-cyber-operations-europe/
verification: single-source
sourcing_note: Group-IB is the only party that holds the directory and no independent write-up or victim statement was found; Group-IB assesses the data as legitimate with high confidence, links it to no actor and says that for several operations the evidence is limited to recorded commands. The page was published on 2026-11-11 (modified 2026-11-12). CVE-2024-55591 dates from January 2025; Fortinet's version table covers the whole advisory, which also holds CVE-2025-24472, and is not split per CVE. Server addresses, hashes and file names are deliberately not carried.
confidence: medium
references:
  - 2026-08-11/gunra-raas-fortios-mfa-backdoor-linux-prng-recoverable
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - On every FortiGate on FortiOS 7.0 below 7.0.17 (and FortiProxy 7.2 below 7.2.13 or 7.0 below 7.0.20) take the HTTP/HTTPS administrative interface off internet-facing interfaces, and on any unit whose interface was ever reachable list the administrators for an account named service or any unexplained super_admin account and review jsconsole logins; where one is found rotate every secret stored in the configuration, because a patch does not remove an account that already exists.
updates: []
migrated_from: null
---

Group-IB reports that in late July 2026 it found an open directory on a Latvian server that held the operator's /root/ directory, 457 files of which 35 were recovered, and documents more than 14 months of operations against Europe by an operator it tracks as DarkLunnen; Group-IB links it to no known actor and does not establish nationality or state affiliation ([Group-IB, 2026-11-11](https://www.group-ib.com/blog/offensive-cyber-operations-europe/)). The main campaign used a modified watchTowr proof of concept for FortiOS CVE-2024-55591, designed to create a backdoor super-admin account named service ([Group-IB, 2026-11-11](https://www.group-ib.com/blog/offensive-cyber-operations-europe/)); the recovered results list about 600 devices in Turkey (hospitals, industry and municipalities), 16 in Ukraine, 14 in Azerbaijan and 1 in Algeria, and a stolen FortiGate configuration from a Romanian organisation carried the same account and yielded 10 cleartext VPN passwords ([Group-IB, 2026-11-11](https://www.group-ib.com/blog/offensive-cyber-operations-europe/)).

The Swiss content is thin. Group-IB recovered a list of 4,725 FortiGate scanning targets for Switzerland and says such lists identify scanning targets but do not confirm vulnerability or successful exploitation; a table of additional operations also lists restic commands with AWS credentials accessing an S3 repository at a Swiss domain in May and June 2025, with production snapshots enumerated, and the report names no organisation and says that for several operations the evidence is limited to recorded commands ([Group-IB, 2026-11-11](https://www.group-ib.com/blog/offensive-cyber-operations-europe/)). Fortinet's advisory FG-IR-24-535 lists FortiOS 7.0.0 through 7.0.16 and FortiProxy 7.2.0 through 7.2.12 and 7.0.0 through 7.0.19 as affected, fixed in 7.0.17, 7.2.13 and 7.0.20, names FortiOS 7.2, 7.4, 7.6 and 6.4 as not affected and offers disabling the HTTP/HTTPS administrative interface as the workaround ([Fortinet PSIRT, 2025-01-14](https://fortiguard.fortinet.com/psirt/FG-IR-24-535)).

**Exposure:** a FortiOS 7.0 device below 7.0.17, or a FortiProxy below its fixed release, whose HTTP/HTTPS administrative interface was ever reachable from the internet; a device exposed while vulnerable can carry an account that patching does not remove ([Group-IB, 2026-11-11](https://www.group-ib.com/blog/offensive-cyber-operations-europe/)).

**Detection:** in FortiGate event logs, an administrator named service with the super_admin profile, any unexplained administrator or local user, and super_admin logins or account creation through the jsconsole interface, which Fortinet lists among its indicators; in VPN logs, logins with accounts whose secrets sat in an exposed configuration ([Group-IB, 2026-11-11](https://www.group-ib.com/blog/offensive-cyber-operations-europe/)).

**Defender takeaway:** hunt for the account on patched devices too, assume the configuration was read on a device that was exposed while vulnerable and rotate the VPN user passwords, administrator passwords, IPsec pre-shared keys and LDAP or RADIUS credentials it stored, review VPN logs and enforce MFA, and enable private data encryption, which is off by default ([Group-IB, 2026-11-11](https://www.group-ib.com/blog/offensive-cyber-operations-europe/)); no source says that a Swiss organisation was compromised.
