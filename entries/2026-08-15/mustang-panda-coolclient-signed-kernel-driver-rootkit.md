---
schema: 1
kind: threat
horizon: operational
title: "Mustang Panda's CoolClient backdoor gains a kernel driver signed with a 2013 certificate that expired in 2014 — and it hides the malware's own C2 traffic by hooking the driver Windows uses to report network state"
headline: "Kaspersky documents a previously undocumented CoolClient rootkit driver, deployed only once the implant already holds SCM access and SeTcbPrivilege"
summary: >
  Kaspersky's GReAT team published on 2026-08-14 a new CoolClient backdoor variant, attributed to the
  actor it tracks as HoneyMyte and also known as Mustang Panda, that installs a signed kernel-mode
  driver as a Windows service. The driver hides processes, files, registry keys and — distinctively — strips the
  implant's own C2 addresses from the network information Windows returns to user-mode tools. It is deployed only
  where the implant already holds Service Control Manager access and SeTcbPrivilege, and follows a PlugX foothold.
discovered_at: "2026-08-15T05:14:00Z"
event_date: "2026-08-14"
run_id: 2026-08-15T0412Z-intel
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
regions:
  - apac
  - global
sectors:
  - public-sector
entities:
  - actor:mustang-panda
  - malware:coolclient
  - malware:plugx
  - malware:toneshell
techniques: [T1543.003, T1014, T1055, T1548.002, T1553.002, T1574.001, T1112, T1685]
affected_products:
  - Microsoft Windows
cves: []
sources:
  - url: "https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-08-14"
    role: primary
  - url: "https://thehackernews.com/2026/08/mustang-panda-adds-signed-windows.html"
    publisher: The Hacker News
    date: "2026-08-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "CoolClient is a backdoor family attributed to the HoneyMyte APT group (also known as Mustang Panda) that has been used in their cyber-espionage campaigns targeting organizations across Asia and Russia."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "The driver implements 33 IOCTL handlers, although the analyzed CoolClient sample uses only three during normal execution"
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "The driver is digitally signed with a certificate issued to \"Nanjing Ranyi Technology Co., Ltd.\", with serial number 3E 62 DC 5D 8D 61 2A 26 33 E7 6B DF D6 07 19 DD. The certificate was valid from August 2013 to September 2014."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "Across the observed intrusions, CoolClient was consistently deployed as a secondary backdoor following a PlugX infection, indicating that HoneyMyte continues to use PlugX as its initial post-compromise implant before transitioning to CoolClient."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "we identified victims in Myanmar, Mongolia, Pakistan, and Russia, including confirmed government entities."
    publisher: "Kaspersky Securelist (GReAT)"
verification: single-source
sourcing_note: >
  Kaspersky's GReAT analysis is the sole first-hand technical account; the corroborating outlet re-reports it
  rather than observing independently, so credibility rests on one assessor. Kaspersky states only that HoneyMyte
  is "also known as Mustang Panda" — the other cluster names commonly applied to this actor by other trackers are
  not stated by this source and are therefore not claimed here, and neither cited source states a national nexus,
  so none is asserted: Kaspersky describes an espionage group operating across Asia and Russia, notes
  Chinese-language strings in the developer's build path, and says its own open-source checks could not tie those
  strings to any known organisation. Victimology is outside this constituency's home
  region; the entry is carried for the transferable rootkit tradecraft, not for regional targeting.
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

Kaspersky's GReAT team published a teardown on 2026-08-14 of a new variant of CoolClient, "a backdoor family attributed to the HoneyMyte APT group (also known as Mustang Panda) that has been used in their cyber-espionage campaigns targeting organizations across Asia and Russia" ([Kaspersky Securelist, 2026-08-14](https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/)). The variant introduces what Kaspersky describes as a previously undocumented kernel-mode driver, installed as a Windows service, that significantly expands the malware's stealth. Kaspersky identified victims in Myanmar, Mongolia, Pakistan and Russia, including confirmed government entities, and reports that across the observed intrusions CoolClient was consistently deployed as a secondary backdoor following a PlugX infection — the group continuing to use PlugX as its initial post-compromise implant before transitioning to CoolClient. The Hacker News covered the same research the same day ([The Hacker News, 2026-08-14](https://thehackernews.com/2026/08/mustang-panda-adds-signed-windows.html)).

The detail that makes this worth a defender's attention is not that a rootkit exists but where its author decided to spend effort. The driver implements 33 IOCTL handlers, although the analysed sample uses only three during normal execution ([Kaspersky Securelist, 2026-08-14](https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/)): one registering the implant's own process as protected, one registering filesystem and registry paths to hide, and one registering the command-and-control IPv4 address. That third one is the interesting capability. The driver hooks the Windows component responsible for reporting network state to user-mode callers and strips the malware's registered C2 addresses from the results — so a responder running a connection-listing tool on the live host sees a machine with no connection to the attacker's infrastructure. The unused 30 handlers describe the intended capability envelope rather than what this sample did: shellcode injection into a target process, unlinking kernel modules from the loaded-module list, removing Protected Process Light status, disabling and restoring kernel notification callbacks, loading a further driver manually, and a handler that writes to an arbitrary kernel address. Concealment is enforced through three complementary mechanisms — object-handle callbacks protecting the injected process, a filesystem minifilter denying access to protected paths, and a registry callback that removes protected keys from enumeration results and denies direct access, with the implant's own registered processes exempted from the filtering.

Two preconditions bound the whole capability, and both are useful to a defender. Kaspersky reports the implant checks for full access to the Service Control Manager and the presence of `SeTcbPrivilege` before it extracts and installs the driver at all; where those are absent, it skips the kernel component and proceeds with the user-mode implant. Administrator rights are reached beforehand through a user-account-control bypass combining remote-procedure-call-based process creation with parent-process spoofing — a technique class already publicly documented rather than a novel evasion. The user-mode chain preceding it is classic sideloading: a renamed legitimate Sangfor-branded executable placed in a directory masquerading as a Windows Defender install path, with Defender exclusions added for that path beforehand, loading the attacker's first-stage library and injecting the final implant into another process. The signing certificate is the other bounded fact: the driver is signed, but with a commercial certificate issued to a Chinese company that was valid only from August 2013 to September 2014 ([Kaspersky Securelist, 2026-08-14](https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/)). Kaspersky found other, older malicious drivers signed with the same certificate but states no evidence connecting them to this campaign.

**Defender takeaway:** the escalation gate is the leverage. This rootkit only lands where the implant has already reached Service Control Manager access and `SeTcbPrivilege`, which means the controls that keep ordinary users off local administrator rights are also what keeps this capability out of the kernel — and where they fail, everything downstream becomes invisible to the tools a responder would normally reach for first. Practically, that argues for collecting driver-load and kernel-callback-registration telemetry centrally, because a host that can hide its own C2 connections cannot hide the moment it loaded the driver that lets it.

**Triage:** legitimate third-party software loads signed kernel drivers routinely, so a driver load is not by itself the signal. The discriminators here are the certificate and the callback pattern: a driver whose signing certificate expired more than a decade before the load, registering object-handle callbacks, a filesystem minifilter and a registry callback in close succession shortly after a newly installed service appeared, is not an ordinary endpoint agent. On the user-mode side, a Sangfor-branded executable or one named for Windows Defender running from a directory that is not the genuine Defender path — particularly where Defender exclusions were added for that same path moments earlier — is the pre-escalation shape, and it is visible before the kernel component ever loads.
