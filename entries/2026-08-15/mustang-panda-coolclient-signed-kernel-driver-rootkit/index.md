---
schema: 1
kind: threat
title: >
  Mustang Panda's CoolClient backdoor gains a kernel driver signed with a 2013 certificate that
  expired in 2014 — and it hides the malware's own C2 traffic by hooking the driver Windows uses
  to report network state
headline: >
  Kaspersky documents a previously undocumented CoolClient rootkit driver, deployed only once the
  implant already holds SCM access and SeTcbPrivilege
summary: >
  Kaspersky's GReAT team published on 2026-08-14 a new CoolClient backdoor variant, attributed to
  the actor it tracks as HoneyMyte and also known as Mustang Panda, that installs a signed
  kernel-mode driver as a Windows service. The driver hides processes, files, registry keys and —
  distinctively — strips the implant's own C2 addresses from the network information Windows
  returns to user-mode tools. It is deployed only where the implant already holds Service Control
  Manager access and SeTcbPrivilege, and follows a PlugX foothold.
discovered_at: "2026-08-15T05:14:00Z"
updated_at: "2026-08-21T06:35:00Z"
event_date: 2026-08-14
run_id: 2026-08-15T0412Z-intel
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
  - ot-ics
regions:
  - apac
  - global
sectors:
  - public-sector
  - energy
entities:
  - "actor:mustang-panda"
  - "malware:coolclient"
  - "malware:plugx"
  - "malware:toneshell"
  - "malware:havencode"
  - "malware:claimloader"
techniques:
  - T1543.003
  - T1014
  - T1055
  - T1548.002
  - T1553.002
  - T1574.001
  - T1112
  - T1685
  - T1566.001
  - T1071.001
  - T1219
  - T1090
  - T1105
  - T1036.005
  - T1027
  - T1082
  - T1033
  - T1049
affected_products:
  - Microsoft Windows
cves: []
sources:
  - url: "https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/"
    publisher: Kaspersky Securelist (GReAT)
    date: 2026-08-14
    role: primary
  - url: "https://thehackernews.com/2026/08/mustang-panda-adds-signed-windows.html"
    publisher: The Hacker News
    date: 2026-08-14
    role: corroborating
  - url: "https://www.ibm.com/think/x-force/trapping-a-mustang-panda"
    publisher: IBM X-Force
    date: 2026-08-20
    role: primary
closed_sources: []
evidence:
  - quote: CoolClient is a backdoor family attributed to the HoneyMyte APT group (also known as Mustang Panda) that has been used in their cyber-espionage campaigns targeting organizations across Asia and Russia.
    publisher: Kaspersky Securelist (GReAT)
  - quote: "The driver implements 33 IOCTL handlers, although the analyzed CoolClient sample uses only three during normal execution"
    publisher: Kaspersky Securelist (GReAT)
  - quote: "The driver is digitally signed with a certificate issued to \"Nanjing Ranyi Technology Co., Ltd.\", with serial number 3E 62 DC 5D 8D 61 2A 26 33 E7 6B DF D6 07 19 DD. The certificate was valid from August 2013 to September 2014."
    publisher: Kaspersky Securelist (GReAT)
  - quote: "Across the observed intrusions, CoolClient was consistently deployed as a secondary backdoor following a PlugX infection, indicating that HoneyMyte continues to use PlugX as its initial post-compromise implant before transitioning to CoolClient."
    publisher: Kaspersky Securelist (GReAT)
  - quote: "we identified victims in Myanmar, Mongolia, Pakistan, and Russia, including confirmed government entities."
    publisher: Kaspersky Securelist (GReAT)
  - quote: "Earlier variants relied on custom socket-based communications, while version 10 transitions to secure WebSocket communications using WinHTTP over TLS."
    publisher: IBM X-Force
  - quote: "It does not contain any embedded C2 addresses. Instead, the C2 server is provided as command line argument at the time of execution"
    publisher: IBM X-Force
  - quote: This evidence is a strong indicator that most of the operator activity was not scripted but performed by hand.
    publisher: IBM X-Force
  - quote: "The observed activity extends a campaign previously reported by Acronis, where ITG27 targeted India's energy sector and government organizations."
    publisher: IBM X-Force
verification: single-source
sourcing_note: >
  Kaspersky's GReAT analysis is the sole first-hand technical account; the corroborating outlet
  re-reports it rather than observing independently, so credibility rests on one assessor.
  Kaspersky states only that HoneyMyte is "also known as Mustang Panda" — the other cluster names
  commonly applied to this actor by other trackers are not stated by this source and are therefore
  not claimed here, and neither cited source states a national nexus, so none is asserted:
  Kaspersky describes an espionage group operating across Asia and Russia, notes Chinese-language
  strings in the developer's build path, and says its own open-source checks could not tie those
  strings to any known organisation. Victimology is outside this constituency's home region; the
  entry is carried for the transferable rootkit tradecraft, not for regional targeting.
confidence: high
references:
  - 2026-08-17/patchcord-sheetcord-google-sheets-c2-browser-shortcut-hijack
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-21T06:35:00Z"
    run_id: 2026-08-21T0410Z-intel
    type: update
    summary: >
      IBM X-Force, working with a deception vendor, ran two simulated victim environments — a fake
      electric-grid operational technology company and a fake state-level government agency — and
      captured live ITG27 operator activity inside them over several days. Two technical deltas matter
      beyond the actor's previously reported activity. Toneshell v10 drops the family's custom
      socket-based command-and-control for secure WebSockets over TLS via the native WinHTTP API set,
      so the channel now shares protocol, port and client-stack fingerprint with ordinary Windows
      application traffic. And Havencode, a backdoor X-Force had not seen before, provides hidden and
      view-only VNC access plus a generic tunnel, with no C2 address in the binary at all — it is
      supplied as a command-line argument at launch. Targeting in this campaign is Indian government
      and energy; X-Force names no European victim.
    fields:
      - entities
      - evidence
      - references
      - sectors
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-21/itg27-havencode-toneshell-v10-websocket-deception
migrated_from: null
---

Kaspersky's GReAT team published a teardown on 2026-08-14 of a new variant of CoolClient, "a backdoor family attributed to the HoneyMyte APT group (also known as Mustang Panda) that has been used in their cyber-espionage campaigns targeting organizations across Asia and Russia" ([Kaspersky Securelist, 2026-08-14](https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/)). The variant introduces what Kaspersky describes as a previously undocumented kernel-mode driver, installed as a Windows service, that significantly expands the malware's stealth. Kaspersky identified victims in Myanmar, Mongolia, Pakistan and Russia, including confirmed government entities, and reports that across the observed intrusions CoolClient was consistently deployed as a secondary backdoor following a PlugX infection — the group continuing to use PlugX as its initial post-compromise implant before transitioning to CoolClient. The Hacker News covered the same research the same day ([The Hacker News, 2026-08-14](https://thehackernews.com/2026/08/mustang-panda-adds-signed-windows.html)).

The detail that makes this worth a defender's attention is not that a rootkit exists but where its author decided to spend effort. The driver implements 33 IOCTL handlers, although the analysed sample uses only three during normal execution ([Kaspersky Securelist, 2026-08-14](https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/)): one registering the implant's own process as protected, one registering filesystem and registry paths to hide, and one registering the command-and-control IPv4 address. That third one is the interesting capability. The driver hooks the Windows component responsible for reporting network state to user-mode callers and strips the malware's registered C2 addresses from the results — so a responder running a connection-listing tool on the live host sees a machine with no connection to the attacker's infrastructure. The unused 30 handlers describe the intended capability envelope rather than what this sample did: shellcode injection into a target process, unlinking kernel modules from the loaded-module list, removing Protected Process Light status, disabling and restoring kernel notification callbacks, loading a further driver manually, and a handler that writes to an arbitrary kernel address. Concealment is enforced through three complementary mechanisms — object-handle callbacks protecting the injected process, a filesystem minifilter denying access to protected paths, and a registry callback that removes protected keys from enumeration results and denies direct access, with the implant's own registered processes exempted from the filtering.

Two preconditions bound the whole capability, and both are useful to a defender. Kaspersky reports the implant checks for full access to the Service Control Manager and the presence of `SeTcbPrivilege` before it extracts and installs the driver at all; where those are absent, it skips the kernel component and proceeds with the user-mode implant. Administrator rights are reached beforehand through a user-account-control bypass combining remote-procedure-call-based process creation with parent-process spoofing — a technique class already publicly documented rather than a novel evasion. The user-mode chain preceding it is classic sideloading: a renamed legitimate Sangfor-branded executable placed in a directory masquerading as a Windows Defender install path, with Defender exclusions added for that path beforehand, loading the attacker's first-stage library and injecting the final implant into another process. The signing certificate is the other bounded fact: the driver is signed, but with a commercial certificate issued to a Chinese company that was valid only from August 2013 to September 2014 ([Kaspersky Securelist, 2026-08-14](https://securelist.com/honeymyte-coolclient-driver-rootkit/121028/)). Kaspersky found other, older malicious drivers signed with the same certificate but states no evidence connecting them to this campaign.

**Defender takeaway:** the escalation gate is the leverage. This rootkit only lands where the implant has already reached Service Control Manager access and `SeTcbPrivilege`, which means the controls that keep ordinary users off local administrator rights are also what keeps this capability out of the kernel — and where they fail, everything downstream becomes invisible to the tools a responder would normally reach for first. Practically, that argues for collecting driver-load and kernel-callback-registration telemetry centrally, because a host that can hide its own C2 connections cannot hide the moment it loaded the driver that lets it.

**Triage:** legitimate third-party software loads signed kernel drivers routinely, so a driver load is not by itself the signal. The discriminators here are the certificate and the callback pattern: a driver whose signing certificate expired more than a decade before the load, registering object-handle callbacks, a filesystem minifilter and a registry callback in close succession shortly after a newly installed service appeared, is not an ordinary endpoint agent. On the user-mode side, a Sangfor-branded executable or one named for Windows Defender running from a directory that is not the genuine Defender path — particularly where Defender exclusions were added for that same path moments earlier — is the pre-escalation shape, and it is visible before the kernel component ever loads.

## Update — 2026-08-21T06:35:00Z

This pipeline covered a CoolClient variant attributed to this actor six days ago, installing a signed kernel driver that filtered its own C2 addresses out of the network data Windows returns to user mode. This is separate research on the same actor from a different lab, and the reason it is worth an update rather than nothing is that one of its two findings retires existing detection content.

**Toneshell v10 changes the channel, not just the payload.** "Earlier variants relied on custom socket-based communications, while version 10 transitions to secure WebSocket communications using WinHTTP over TLS" ([IBM X-Force, 2026-08-20](https://www.ibm.com/think/x-force/trapping-a-mustang-panda)). The implant now speaks through the operating system's own WinHTTP WebSocket routines and additionally queries the user's proxy configuration, so it is proxy-aware. The consequence for a network defender is direct: a signature or filter written against Toneshell's earlier bespoke socket protocol no longer matches anything, and what replaces it is traffic sharing port, protocol and TLS client-stack characteristics with every other WinHTTP-based Windows application and ordinary browser WebSocket session. Detection has to move to the client-stack TLS fingerprint, destination reputation, or endpoint-side visibility of the WebSocket API calls themselves — protocol shape alone no longer discriminates.

X-Force also found three standalone DLL builds of Toneshell v10 reusing the same WebSocket model, command dispatcher and reverse-shell functionality, two of them masquerading under the filename of a PDF-creation component and one as a browser-framework library. Between the dispatcher's command branches sit repeated blocks of wide-character junk strings referencing Harry Potter characters and themes — padding inserted to frustrate analysis.

**Havencode: hidden desktop access with nothing to extract from the binary.** X-Force had not previously observed this backdoor. Its centre of gravity is hidden Virtual Network Computing, letting an operator connect to an infected machine's desktop and browse it covertly. It ships as a 64-bit DLL alongside a legitimate signed executable and is launched by side-loading, and it takes three modes: a hidden-desktop VNC server on a supplied local port, a view-only mode that attaches to the user's *existing* desktop to watch without taking input control, and a generic TCP/UDP tunnel the operators used to relay the local VNC server's traffic out to their C2 — though X-Force notes the tunnel may serve any other proxy traffic too.

The detail that matters for hunting is what the file does not hold: "It does not contain any embedded C2 addresses. Instead, the C2 server is provided as command line argument at the time of execution". Static extraction of infrastructure from a recovered sample yields nothing; the address exists only in the process command line at launch, which makes process-creation telemetry with full command-line capture the difference between knowing where it called home and not.

The loader in front of it, which X-Force names Claimloader, copies the side-loading pair into a new installation directory — commonly under the system-wide program-data path — establishes persistence, then recovers embedded shellcode and executes the Toneshell payload by abusing a locale-enumeration API as a callback to transfer execution.

**What the deception environment showed that logs would not.** X-Force ran two fake victims — an operational technology company specialising in electric grids, and a state-level government agency — and captured the operators live. The evidence of hands-on-keyboard work is mundane and convincing: two commands were mistyped in both incidents, a domain-enumeration command and a wireless-network listing, and on its first attempt the crew launched Havencode with malformed arguments. X-Force's conclusion is that "This evidence is a strong indicator that most of the operator activity was not scripted but performed by hand", corroborated independently by timing — operator-initiated actions fell exclusively within weekday working hours of 08:00 to 18:00 China Standard Time, with activity pausing over a weekend and resuming afterwards. Initial access in the campaign came from a May 2026 email to Indian government recipients carrying a PDF attachment themed as a hydropower cooperation study and imitating Nepal's foreign ministry.

**Triage:** the side-load pair is the most reliable host-side discriminator, because the legitimate executable is genuinely signed and will pass any signature check — what is anomalous is that binary running from a program-data subdirectory rather than its installed location, with a same-named dependency DLL beside it. For Havencode specifically, look for a process whose command line carries a network address and a local port together with VNC-style mode arguments: the configuration is in the command line by design, so command-line logging is not optional here. On the network side, the honest position is that Toneshell v10's channel is hard to separate from benign WinHTTP WebSocket traffic; the tractable signals are a hidden-desktop VNC session being tunnelled out of a host that has no remote-support tooling deployed, and a rapid sequence of host and network reconnaissance commands — system information, current user, group enumeration, network connections and process listing in quick succession — which X-Force names as the pattern to alert on.

**Defender takeaway:** if you carry detection content for this family, the network half of it is now stale and should be re-based on endpoint API-level or TLS-fingerprint visibility rather than the retired custom protocol. More broadly, this is the second entry in a week showing this actor moving C2 onto channels that are indistinguishable from sanctioned traffic — the earlier CoolClient variant hid its addresses from the operating system's own reporting, and this one hides in the operating system's own HTTP stack. Note the targeting honestly: this campaign is aimed at Indian government and energy, so the value here is the tradecraft and the invalidated signatures, not a claim of exposure in this constituency. The operator's fixed working-hours pattern is also a reminder that for a hands-on-keyboard intrusion, log retention long enough to span a multi-day operational tempo — X-Force recommends at least 90 days — is what makes the pattern visible at all.
