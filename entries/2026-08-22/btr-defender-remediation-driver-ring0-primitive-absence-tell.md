---
schema: 1
kind: research
horizon: operational
title: "Windows Defender ships a signed kernel driver whose whole job is deleting locked files, and it takes its instructions from a registry value — Check Point shows an administrator can hand it any file or registry target"
headline: "No exploit, no CVE, and Microsoft declined to service it — the detection is an event that fails to appear"
summary: >
  Check Point published the first full reverse-engineering of BTR.sys, the Boot Time Removal driver
  Microsoft embeds inside the Defender scanning engine and drops to disk under a randomised name only when
  a remediation needs a reboot to finish. It exposes no device interface; it reads its work list from a
  configuration blob referenced by its own service key and held in an NTFS alternate data stream. An
  attacker who already holds administrative privilege including the driver-load right can therefore direct
  a Microsoft-signed, built-in component to delete or move files and delete or write registry keys at
  kernel level, with no vulnerability involved. Microsoft told Check Point this does not meet the bar for
  immediate servicing because it requires pre-existing admin, no CVE was assigned, and a public research
  tool now exists. Check Point observed no real-world abuse — and the most useful thing it published is an
  absence-based detection.
discovered_at: "2026-08-22T05:10:00Z"
event_date: "2026-08-20"
run_id: 2026-08-22T0410Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, no-patch, poc-public]
regions: [global]
sectors: [public-sector, technology]
entities: []
techniques: [T1543.003, T1685, T1564.004, T1070.004, T1112, T1036]
affected_products: ["Microsoft Defender Antivirus", "Microsoft Windows"]
cves: []
sources:
  - url: "https://research.checkpoint.com/2026/btr-reforged-weaponizing-defenders-remediation-driver-as-a-kernel-operation-primitive/"
    publisher: "Check Point Research"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "MSRC confirmed that these findings do not meet the criteria for immediate servicing, as the technique relies on pre-existing administrative privileges (SeLoadDriverPrivilege)."
    publisher: "Check Point Research"
  - quote: "The driver does not expose a standard IOCTL interface. Instead, it reads a configuration blob pointed to by the Args value in its Service Registry Key."
    publisher: "Check Point Research"
  - quote: "Sysmon logs the File Delete (Event ID 23), but the Image performing the deletion is recorded as System (PID 4), not the user-mode tool that triggered it."
    publisher: "Check Point Research"
verification: single-source
sourcing_note: >
  One source, and the only one — Check Point is the originating researcher and no second party has
  assessed this, so reliability is B for an original research lab and credibility stays at 2. Microsoft's
  determination reaches the public only through Check Point's account of its disclosure exchange and is
  attributed that way rather than as a Microsoft statement. Three limits are stated rather than smoothed:
  Check Point says it observed no real-world abuse of this driver in this manner across its samples and
  telemetry, so nothing here is an exploitation finding; no CVE was assigned and the report contains no
  identifier, which is why `cves` is empty; and the technique requires administrative privilege including
  the driver-load right before any of it is reachable, which places it squarely as post-compromise
  tradecraft rather than a privilege-escalation route. This entry deliberately describes the capability
  classes and the telemetry rather than the transaction format or any invocation sequence. The public
  research tool's repository path is in the report and is not reproduced here.
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

Check Point Research published a reverse-engineering of BTR.sys, a driver most defenders have never heard of because it normally exists for seconds at a time. It is not a standalone product: Microsoft ships it embedded as a resource inside the Defender scanning engine, and Defender writes it to the system driver directory under a randomised name, with a matching randomly named service, only when a remediation action needs a reboot to complete — deleting a file that is locked while Windows is running, for instance. It loads, works through a list of remediation transactions, reports status and asks to be unloaded. The design detail that makes it interesting is how it is told what to do: it exposes no standard device interface, and instead reads a configuration blob pointed to by the `Args` value in its own service registry key ([Check Point Research, 2026-08-20](https://research.checkpoint.com/2026/btr-reforged-weaponizing-defenders-remediation-driver-as-a-kernel-operation-primitive/)), with that blob held in an NTFS alternate data stream on the driver file. Anyone who can write that service key and load the driver can therefore give a Microsoft-signed kernel component an arbitrary work list.

The prerequisite is the whole framing, and Check Point is direct about it: the technique relies on pre-existing administrative privileges including the driver-load right, and on that basis Microsoft's response centre confirmed the findings do not meet the criteria for immediate servicing ([Check Point Research, 2026-08-20](https://research.checkpoint.com/2026/btr-reforged-weaponizing-defenders-remediation-driver-as-a-kernel-operation-primitive/)). No CVE was assigned. That determination is defensible on its own terms and it is also what makes this worth a defender's attention, because it means the component stays where it is: Check Point's reading is that this driver stands as a living-off-the-land driver which, unlike the third-party drivers the vulnerable-driver blocklist neutralises, remains a built-in Windows component that is fully allowed and operational. Driver blocklisting is not a lever here. What the primitive can do is bounded — kernel-level file deletion that bypasses exclusive locks, empty-directory deletion, file move or quarantine which doubles as a write into otherwise protected locations, registry key and value deletion, and registry value creation which Check Point notes serves either to establish persistence or to disable security controls. What it cannot do is equally worth knowing: the report describes no kernel memory read or write and no kernel code execution. This is a file-and-registry primitive with kernel authority, not a kernel-execution primitive. Check Point also found a hard limit on when it can run, because the driver performs file I/O early enough in boot that a true boot-start slot breaks it — so the abuse has to occupy the same system-start interval Defender itself uses, after the filesystem is mounted and before Defender's user-mode service starts.

Two facts set the urgency, and they point in opposite directions. Check Point states it observed no real-world abuse of the driver in this manner across its samples and telemetry, and frames the moment as an opportunity to do detection engineering before weaponisation appears. Against that, it released a research tool publicly under a permissive licence with source and ready-to-run executables, and it identified eighteen distinct Microsoft-signed builds of the driver sharing one hard-coded configuration key, with the configuration structure stable and backward-compatible from Windows 7 through Windows 11 25H2 — a fifteen-year-stable internal interface. The barrier to reuse is low and the surface is everywhere Defender is.

**Defender takeaway:** the detection guidance is unusually good and one part of it is the reason this entry exists. Check Point's highest-value concept is an *absence*: legitimate staging of this driver goes through the Service Control Manager and therefore produces the standard Windows service-installation record in the System event log, while the abuse path writes the service registry keys directly and loads the driver through a native call — so the service-installation event never appears. A service-key write that configures a driver load order, with no corresponding service-installation record, is the anomaly, and no single-event rule will find it. The supporting telemetry classes are ordinary ones: file-stream-creation events are the high-fidelity anchor for the alternate-data-stream configuration, though Check Point is careful that the stream's *name* is identical in legitimate and abusive use, so existence discriminates nothing — the surrounding context does. One context signal is a genuine discriminator: legitimate Defender directs the driver's status report to a standalone file under Defender's own protected data path, whereas the research tool writes it into a second stream on the driver file itself, so an extra stream on a `.sys` file is anomalous on its own. Driver-load events plus process lineage are the third class — a signed load of this driver is expected when a Defender process staged it and anomalous when whatever dropped it sits outside the Defender ecosystem. And file-deletion events attribute the deletion to the kernel rather than the requester, so the hunt is a correlation between a System-context deletion of security binaries and a preceding driver load.

**Triage:** the benign population here is large and Check Point proves the point against itself — the research began as a false-positive investigation on a live incident-response engagement, where its own analysts first hypothesised attacker abuse of this driver and then established the activity was legitimate Defender remediation. That is the discriminator worth internalising: every artifact of this technique is also an artifact of Defender doing its job. What separates them is provenance and destination — which process staged the driver, whether a service-installation record accompanied it, and whether the status write went to Defender's own protected path or somewhere else. On its own, a randomly named signed driver appearing in the system driver directory and deleting a locked file is Defender working correctly, and treating it as an incident is the mistake the researchers made first.
