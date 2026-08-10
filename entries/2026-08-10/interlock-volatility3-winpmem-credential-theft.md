---
schema: 1
kind: threat
horizon: operational
title: "Interlock ran Volatility3 and WinPmem against a live endpoint to harvest credentials — the responder's own memory-forensics toolkit used in place of a commodity dumper"
headline: "A ransomware operator acquired a memory image and ran hashdump and cachedump offline against it, leaving traces that look like an IR engagement"
summary: >
  Sophos's incident-response team investigated a March 2026 Interlock intrusion in which the operator
  captured a full physical-memory image with WinPmem and then ran Volatility3's Windows credential
  plugins offline against that image, instead of using a commodity credential dumper on the live
  host. Initial access was a ClickFix paste-and-run lure reached through a search result, and the
  chain ran to domain-controller compromise inside roughly 26 hours including a deliberate day-long
  pause. The defensive problem is that both binaries are legitimate DFIR tooling, so their presence
  and their command shapes are indistinguishable from a real investigation on artifact alone —
  Sophos's own discriminator was that the customer knew of no legitimate use.
discovered_at: "2026-08-10T04:44:00Z"
event_date: "2026-08-07"
run_id: 2026-08-10T0411Z-intel
priority: high
immediate_action: null
tags: [ransomware, phishing, organized-crime, identity]
regions: [global, europe]
sectors: [public-sector, healthcare, energy, technology]
entities: [actor:interlock, malware:nodesnake]
techniques: [T1189, T1204.004, T1547.001, T1069.002, T1558.003, T1021.001, T1053.005, T1003.002, T1003.005]
affected_products: []
cves: []
sources:
  - url: "https://www.sophos.com/en-us/blog/2608-volatility-interlock/"
    publisher: "Sophos X-Ops"
    date: "2026-08-07"
    role: primary
  - url: "https://www.sophos.com/en-us/threat-profiles/gold-embrace"
    publisher: "Sophos Counter Threat Unit"
    date: "2026-08-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In March 2026, the Sophos Emergency Incident Response (EIR) team investigated an incident in which we observed the use of the legitimate IR memory analysis tool Volatility3 by the ransomware threat actor Interlock."
    publisher: "Sophos X-Ops"
  - quote: "Interlock, which Sophos Counter Threat Unit (CTU) researchers track as GOLD EMBRACE, emerged in September 2024."
    publisher: "Sophos X-Ops"
  - quote: "We found evidence of credential dumping (including AWS credentials), access to sensitive files, addition of new domain-admin accounts, tampering with Defender on the endpoints, and more."
    publisher: "Sophos X-Ops"
verification: single-source
sourcing_note: >
  Both the incident analysis and the actor profile are Sophos's own publications, so this is a single
  originating assessor with two documents rather than independent corroboration. No second party has
  reported this intrusion, which is why credibility is 2 rather than 1.
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
migrated_from: null
---

Sophos's Emergency Incident Response team has published an intrusion in which the Interlock ransomware operator — which Sophos's Counter Threat Unit tracks as GOLD EMBRACE, active since September 2024 against North American and European targets — used the defender's own toolkit for credential access ([Sophos X-Ops, 2026-08-07](https://www.sophos.com/en-us/blog/2608-volatility-interlock/)). On the first compromised host, the actor acquired a full physical-memory image using WinPmem, the open-source physical-memory acquisition tool, and then ran Volatility3's Windows plugins against that image offline: the hash-dump plugin to recover account material from the SAM and SYSTEM hive structures resident in memory, and the cached-domain-credential plugin for cached logons. No commodity credential dumper was involved in that step.

The chain around it is otherwise conventional and worth reading for its timing. The user reached a compromised but reputable site through a search result, and five seconds later the page read the clipboard — the ClickFix fingerprint. Eight seconds later, thirteen seconds into the chain, the user pasted an attacker-supplied command into the Run dialog, which fetched a second-stage script and installed a remote-access trojan to run at startup; registry Run-key persistence landed about twenty-five minutes in. The operator then paused for roughly a day before resuming with domain-group enumeration over LDAP, a service-principal-name query consistent with Kerberoasting, and a lateral move to the domain controller over RDP. On the third day, using a compromised domain-administrator account, persistence was re-established through a scheduled task named to imitate the built-in disk-defragmentation task and running a bundled Node.js interpreter. Sophos records the outcome as credential dumping including cloud credentials, access to sensitive files, new domain-administrator accounts, and tampering with endpoint protection — and notes that, across the estate, not all endpoints were in fact running protection of any sort.

The reason this is worth a defender's attention is not novelty of the malware but the inversion it forces. Memory acquisition and Volatility analysis are exactly what an incident responder does, so the on-host artifacts of the attack step and of a legitimate engagement are the same artifacts. Sophos is explicit that adversarial use "would leave similar traces" to a DFIR investigation, a security assessment, or malware analysis, and that what resolved it in this case was that the customer knew of no legitimate activity of that kind.

**Triage:** memory-acquisition and memory-analysis binaries executing on an endpoint are not anomalous by artifact — they are anomalous by authorisation and by context. The discriminators that survive are organisational rather than technical: whether an engagement, assessment or analysis was actually scheduled on that host at that time; whether the binaries arrived through the change process that normally delivers them or were dropped into a user-writable path; and whether the acquisition ran on a host with a current, unexplained persistence artifact and recent Run-key or scheduled-task creation. A memory image being written to disk by a process whose parent is a user shell or a downloaded stager, rather than by a responder's tooling deployed through management infrastructure, is the sequence worth alerting on. **Defender takeaway:** any detection logic that allowlists forensic tooling by name or hash gives this actor a free credential-access stage. Treat acquisition and analysis binaries as privileged tooling whose execution requires a matching authorised engagement — and make the authorisation record something a SOC can query during triage, because without it there is no technical discriminator left.
