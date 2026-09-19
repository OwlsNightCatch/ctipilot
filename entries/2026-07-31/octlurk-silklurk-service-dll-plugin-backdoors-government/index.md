---
schema: 1
kind: threat
title: "OctLurk and SilkLurk — sibling plugin backdoors whose loaders key their payload decryption to the victim machine itself, deployed against Central Asian and Syrian government bodies"
headline: "Kaspersky documents loaders that cannot be unpacked away from the host they infected, delivering in-memory-only plugins"
summary: >
  Kaspersky GReAT disclosed two previously undocumented plugin-based Windows backdoors, OctLurk and SilkLurk,
  active since at least January 2025 against government, healthcare, research, foreign-affairs, logistics,
  law-enforcement and education organisations in Afghanistan, Kyrgyzstan, Tajikistan, Uzbekistan, Kazakhstan and
  Syria. Deployment presupposes administrative access: for OctLurk a scheduled task installs a
  Windows service whose ServiceMain value is repointed at a malicious loader DLL, which decrypts its payload with
  two keys — one hard-coded, one derived from the victim machine's C: drive serial number. SilkLurk uses its own
  service and side-loads under a legitimate binary, and its loader keys off a hash of the computer name instead.
  Either way the loader is undecodable away from the host it infected. The backdoor pulls plugins straight from its command server into memory, including
  one providing full synthetic mouse and keyboard control. Kaspersky attributes both, at medium confidence, to a
  single unnamed Chinese-speaking actor.
discovered_at: "2026-07-31T04:09:14Z"
event_date: "2026-07-30"
run_id: 2026-07-31T0409Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, china-nexus, infostealer]
regions: [apac, middle-east, russia-cis]
sectors: [public-sector, healthcare, education]
entities: [malware:octlurk, malware:silklurk, tool:lurkproxy]
techniques: [T1053.005, T1543.003, T1620, T1027, T1003, T1056.001, T1555.003, T1046, T1219, T1114, T1070.006, T1113, T1115, T1059.003, T1518.001]
affected_products: []
cves: []
sources:
  - url: "https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-07-30"
    role: primary
closed_sources: []
evidence:
  - quote: "We assess with medium confidence that the same threat actor is behind both backdoors, and that they are Chinese-speaking. However, at the time of publication, we couldn't attribute this activity to any known group."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "The backdoor loaders are customized for each victim and use information from the victim's machine to decrypt the payload. Both the loaders and the backdoors are heavily obfuscated, making analysis more complicated."
    publisher: "Kaspersky Securelist (GReAT)"
verification: single-source
sourcing_note: >
  [SINGLE-SOURCE: Kaspersky GReAT] — original first-party malware analysis from a research lab with a long
  track record on this class of tooling, published 2026-07-30; no second lab has covered these families at time
  of writing. Kaspersky's own confidence language is carried through unchanged: the shared-operator and
  Chinese-speaking assessments are medium confidence and explicitly unattributed to any tracked group, and the
  infrastructure overlap with a separately-tracked Linux implant is reported as an overlap, not an identity.
confidence: medium
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

Kaspersky GReAT published analysis of two new plugin-based backdoors on 2026-07-30, naming them OctLurk and SilkLurk ([Kaspersky Securelist, 2026-07-30](https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/)). Victim organisations sit in Afghanistan, Kyrgyzstan, Tajikistan, Uzbekistan, Kazakhstan and Syria, across healthcare, research, government offices, foreign-affairs ministries, logistics, law enforcement, urban planning and public education. The victimology is out of scope for this constituency; the loader design and the plugin architecture are the reason the entry is here, because both are aimed squarely at the analysis and detection workflow a government SOC would use against them.

**Everything here starts after the attacker already has administrative credentials.** OctLurk's chain begins with a scheduled task created on remote machines with admin rights, set to run once under the System account immediately after creation. That task runs a batch script from a user profile folder or a temporary directory, which installs a Windows service; the service's `ServiceMain` registry parameter is then repointed to invoke an export of a malicious loader DLL rather than a legitimate service binary. The loader exports two functions, and the one the service calls simply invokes the other, which carries the actual logic. SilkLurk reaches the same place by a different route — its own service name, and side-loading under a legitimate binary rather than the ServiceMain repoint.

**The loader is built to be useless to an analyst who does not also have the victim's machine.** Taking OctLurk's, it locates its payload by decrypting a hard-coded byte blob through two successive XOR passes and a decompression step, then applies the identical process to the payload itself to produce the backdoor DLL. Two keys are involved: one is baked into the binary, and the second is derived at runtime from the serial number of the victim's C: drive. SilkLurk's loader does the same thing with a different host identifier, computing a hash of the victim's computer name. A sample lifted from one host therefore cannot be unpacked on an analyst's workstation, in a sandbox, or against any other victim — Kaspersky states plainly that the loaders are customised per victim and use information from the victim's machine to decrypt the payload. The resulting backdoor DLL is loaded reflectively into memory and never written to disk in decrypted form. The same double-XOR-and-compress framing wraps command-server traffic in both directions, with a freshly generated random key travelling in each packet header, so the wire format changes every session even though the static key does not.

**Plugins arrive from the command server and stay in memory.** Kaspersky documents three. A file manager enumerates volumes and directories, reads and writes files in chunks with integrity checking, executes commands, and — worth noting for anyone doing timeline work afterwards — deliberately rewrites file timestamps to attacker-supplied values. A command shell either maintains an interactive `cmd.exe` session or, when none is running, executes each command non-interactively with output redirected to a temporary file that it reads back and then deletes. An interaction manager captures the screen on demand or on an interval, reads and writes the clipboard, and synthesises mouse movement, clicks and keystrokes through low-level Windows input events — full hands-on-keyboard control delivered as a plugin rather than as a separate remote-access tool.

Post-compromise, the operators run a fingerprinting script that inventories sessions, Kerberos tickets, running tasks, antivirus products and Defender's tamper-protection and exclusion settings, network connections and hardware, and specifically queries the Windows Security log for the last few successful remote-interactive logons. They then deploy Impacket's secretsdump for credential extraction, a keylogger persisted under a scheduled task named after a legitimate remote-access product, a browser-password decryptor targeting Chrome and Firefox credential stores, Pandora RC agents for durable remote access, the FSCAN network scanner, and email-harvesting tooling. SilkLurk victims additionally receive PlugX — which Kaspersky describes as a modular remote-access trojan active since at least 2008 and historically linked to Chinese-speaking threat actors, and which is part of what supports its attribution language — and SilkLurk intrusions show operators mounting shares with harvested admin credentials, hunting documents by hand, and archiving them before exfiltration.

Kaspersky also reports that several command-server addresses used by OctLurk and its companion proxy utility appear in a Kazakhstani State Technical Service report on a separate Linux-targeting implant — tracked as TrustFall by that agency, MystRodX by Qianxin and SilentRaid by Cisco Talos — and it is explicit that this points to shared infrastructure across campaigns without establishing whether they ran at the same time.

**Detection.** Four behaviours here are strong hunt anchors and none of them depend on knowing this malware. First, service creation where the `ServiceMain` parameter points at a DLL export in a path outside the normal system directories — a configuration that legitimate services essentially never use. Second, a scheduled task created remotely to run once under System immediately after creation, executing a script from a user profile or temporary directory. Third, in process telemetry, the non-interactive shell pattern: a `cmd.exe` child redirecting output to a temporary file in the user temp directory, followed within moments by a read of that file and its deletion — the create-read-delete triple on a short-lived temp file is far more distinctive than any one of the three events. Fourth, in the same log the operators query, an inventory sweep that touches session enumeration, Kerberos ticket listing, antivirus product enumeration and Defender exclusion registry keys inside a single short window from one process lineage.

**Triage:** administrators run every one of those discovery commands individually, and management agents create services and scheduled tasks constantly. The discriminators are sequence and origin: the fingerprinting commands arrive as one uninterrupted batch from a single script rather than typed over minutes; the service points at a DLL export rather than an executable; and the scheduled task runs exactly once and never again, which is the opposite of what a legitimate maintenance task looks like.

**Defender takeaway:** the key-derivation trick is the part to internalise, because it changes what "we have the sample" is worth. If an incident on a government network turns up a loader of this shape, unpacking the payload requires a value that only exists on the infected host — the volume serial for one family, the computer name for the other — so the collection step has to capture host identifiers alongside the file, before the machine is reimaged. Pulling the binary and wiping the box leaves you with something no sandbox can open.
