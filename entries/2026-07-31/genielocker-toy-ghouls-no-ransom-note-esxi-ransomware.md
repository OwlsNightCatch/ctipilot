---
schema: 1
kind: threat
horizon: operational
title: "GenieLocker — a Windows and ESXi ransomware built to leave no ransom note on disk, gated behind a hashed command-line secret so it will not run in a sandbox"
headline: "Kaspersky analyses a ransomware family that deliberately drops no readme files, because that is what mass-note detection keys on"
summary: >
  Kaspersky documented GenieLocker, a custom Windows and Linux/ESXi ransomware active since March 2026 and
  attributed by open-source reporting to the Toy Ghouls extortion group, which previously rented third-party
  encryptors. Three design choices matter to defenders more than the crypto: it refuses to run unless its first
  command-line argument hashes to a hard-coded value, defeating automated detonation and unauthorised reuse; a
  watchdog thread polls for debuggers every 500 milliseconds and re-checksums its own code section on each pass,
  terminating on any mismatch; and it writes no ransom note at all, which Kaspersky reads as a deliberate move
  against detections that trigger on mass readme creation. The analysed intrusion began with valid stolen
  credentials over a partner's OpenVPN connection, and the operators reached the KeePassXC database already
  installed on compromised machines.
discovered_at: "2026-07-31T04:09:14Z"
event_date: "2026-07-30"
run_id: 2026-07-31T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, organized-crime, supply-chain]
regions: [russia-cis]
sectors: [manufacturing]
entities: [actor:toy-ghouls, malware:genielocker]
techniques: [T1199, T1078, T1555.005, T1003.001, T1021.001, T1021.004, T1569.002, T1570, T1572, T1622, T1489, T1046, T1486]
affected_products: ["VMware ESXi"]
cves: []
sources:
  - url: "https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/"
    publisher: "Kaspersky Securelist"
    date: "2026-07-30"
    role: primary
closed_sources: []
evidence:
  - quote: "During the incident, the attackers first entered the environment through an OpenVPN connection originating from an external partner's network. They likely exploited the trusted relationship with that partner and used stolen, yet still valid, credentials to connect."
    publisher: "Kaspersky Securelist"
  - quote: "GenieLocker starts a new parallel thread called watchdog. It runs in an infinite loop that performs a number of checks to detect well-known debuggers every 500 milliseconds. If at least one of the checks fails, the whole GenieLocker process immediately terminates."
    publisher: "Kaspersky Securelist"
  - quote: "GenieLocker doesn't save the ransom notes on the victim's system. The Trojan doesn't contain any attackers' contact info or negotiation addresses. Instead, the attackers will need to deliver the ransom demands and contacts manually during the attack."
    publisher: "Kaspersky Securelist"
verification: single-source
sourcing_note: >
  [SINGLE-SOURCE: Kaspersky Securelist] — first-party malware and incident analysis, published 2026-07-30. One
  attribution caveat is carried through deliberately: Kaspersky sources the Toy Ghouls-to-GenieLocker link to
  Russian-language open-source reporting rather than asserting it as its own first-party attribution, so the
  group association is reported at that strength while the malware analysis itself is Kaspersky's own.
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

Kaspersky published an analysis of GenieLocker on 2026-07-30, a ransomware family it dates to March 2026 and that open-source reporting attributes to the Toy Ghouls extortion group — also tracked as Bearlyfy, Labubu and Laboo.boo — which had previously relied on rented encryptors rather than its own ([Kaspersky Securelist, 2026-07-30](https://securelist.com/genielocker-ransomware-for-windows-linux-and-esxi/120843/)). The victim in the analysed intrusion was a Russian manufacturing organisation, which places the targeting outside this constituency; three deliberate design decisions in the malware are what transfer.

**It will not run without a key the operator types.** GenieLocker's Windows build expects its first command-line argument to be a hex string, which it converts to bytes, hashes with SHA-256, and compares against a value compiled into the binary. Without a match the process exits immediately. Kaspersky reads this as serving two purposes at once — evading sandboxes and automated analysis environments, which have no way to supply the argument, and preventing other criminals from reusing a captured sample. For a defender this has a concrete consequence: a sample recovered from an incident cannot be detonated to observe its behaviour unless the argument is also recovered, typically from command-line telemetry or shell history rather than from the file.

**It watches for debuggers continuously, and for tampering with itself.** Once the argument check passes, the malware spawns a thread that loops indefinitely, polling the standard debugger-presence checks every 500 milliseconds. On top of that it computes a checksum over its own executable code section at thread start and recomputes it on every iteration, so a breakpoint written into that section is detected as a change. Any single failed check terminates the whole process, with no partial-encryption fallback described.

**It leaves nothing behind to alert on.** GenieLocker writes no ransom note, carries no contact address and no negotiation link; the operators deliver demands by hand during the intrusion instead. Kaspersky's assessment of why is the operationally important part — that this is an attempt to avoid proactive detection triggered by the creation of multiple readme files. Any detection strategy that leans on mass note-drop as its ransomware trigger simply does not fire here. The ESXi build extends the same logic: it can overwrite the hypervisor's welcome message, and in the analysed sample that field was left blank rather than filled with a demand.

The intrusion around it is conventional and, for this constituency, the most familiar part. Initial access came over an OpenVPN connection originating from an external partner's network, using stolen credentials that were still valid — Kaspersky's assessment is that the operators exploited the trusted relationship with that partner rather than breaching the victim's own perimeter. From there they ran SoftPerfect Network Scanner for discovery, dumped credentials with Mimikatz, and accessed the KeePassXC password manager already installed on several machines to try to extract what was stored in its databases. Lateral movement used RDP to Windows hosts and SSH to Linux servers, mass deployment of the encryptor was carried out with the legitimate PsExec and PAExec utilities, and command-and-control ran over a reverse SSH tunnel. On the Linux and ESXi side the operators stopped running virtual machines before encrypting their disks. Kaspersky found no evidence of data exfiltration and notes this group runs neither double extortion nor a leak site — which means, unusually, that the encryption event is the whole extortion.

**Detection.** Because the note is gone, the durable behavioural triggers are the ones around it: a rapid rise in file-modification volume with high-entropy writes across shares, and, on hypervisors, virtual machines being powered off in sequence shortly before their backing datastore files start changing — that ordering is the ESXi ransomware signature that does not depend on any note or binary. On the endpoint, remote service creation by PsExec-class tooling from a host that is not a management server is the deployment step, and it is loud in service-creation and process-creation telemetry. Two collection behaviours are worth hunting independently of this family: a process other than the password manager itself opening a KeePass database file, and any read of a credential database from a service account context.

**Triage:** administrators use PsExec, and virtual machines are shut down for maintenance every day. The discriminators are direction and breadth — legitimate PsExec runs originate from a known management host to a bounded set of targets, whereas deployment here fans out from a recently-compromised workstation to everything reachable; and maintenance shutdowns are scheduled, announced in change records, and followed by boots rather than by datastore writes. For the password-manager signal the discriminator is the accessing process: the user's own manager opening its database is normal, a scripted or remote-execution parent doing it is not.

**Defender takeaway:** two items for anyone whose ransomware detection strategy predates this year. First, if the mass-readme heuristic is doing meaningful work in your stack, it is now a single point of failure — this family is explicitly engineered against it, and the fallback needs to be encryption-behaviour and hypervisor-state telemetry. Second, the initial access here was a partner's VPN credentials that still worked, which is the same trusted-third-party path that reached a Swiss rail manufacturer this month; third-party VPN accounts deserve the same conditional-access and session-lifetime treatment as employee accounts, and the review that matters is whether a partner account that has not been used in months can still authenticate at all.
