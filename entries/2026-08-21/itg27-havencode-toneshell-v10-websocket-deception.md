---
schema: 1
kind: threat
horizon: operational
title: "UPDATE — Toneshell's tenth version abandons custom sockets for WebSocket-over-TLS through WinHTTP, retiring every network signature built on the old channel, and a new hVNC backdoor carries no embedded C2 at all"
headline: "**IBM X-Force baited ITG27 into two fake victim networks** — Toneshell v10 moves C2 onto WinHTTP WebSockets over TLS"
summary: >
  IBM X-Force, working with a deception vendor, ran two simulated victim environments — a fake electric-grid operational
  technology company and a fake state-level government agency — and captured live ITG27 operator activity inside them
  over several days. Two technical deltas matter beyond the actor's previously reported activity. Toneshell v10 drops
  the family's custom socket-based command-and-control for secure WebSockets over TLS via the native WinHTTP API set,
  so the channel now shares protocol, port and client-stack fingerprint with ordinary Windows application traffic.
  And Havencode, a backdoor X-Force had not seen before, provides hidden and view-only VNC access plus a generic
  tunnel, with no C2 address in the binary at all — it is supplied as a command-line argument at launch. Targeting in
  this campaign is Indian government and energy; X-Force names no European victim.
discovered_at: "2026-08-21T06:35:00Z"
event_date: "2026-08-20"
run_id: 2026-08-21T0410Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, china-nexus, ot-ics]
regions: [apac, global]
sectors: [public-sector, energy]
entities: [actor:mustang-panda, malware:toneshell, malware:havencode, malware:claimloader]
techniques: [T1566.001, T1574.001, T1071.001, T1219, T1090, T1105, T1036.005, T1027, T1082, T1033, T1049]
affected_products: []
cves: []
sources:
  - url: "https://www.ibm.com/think/x-force/trapping-a-mustang-panda"
    publisher: "IBM X-Force"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "Earlier variants relied on custom socket-based communications, while version 10 transitions to secure WebSocket communications using WinHTTP over TLS."
    publisher: "IBM X-Force"
  - quote: "It does not contain any embedded C2 addresses. Instead, the C2 server is provided as command line argument at the time of execution"
    publisher: "IBM X-Force"
  - quote: "This evidence is a strong indicator that most of the operator activity was not scripted but performed by hand."
    publisher: "IBM X-Force"
  - quote: "The observed activity extends a campaign previously reported by Acronis, where ITG27 targeted India's energy sector and government organizations."
    publisher: "IBM X-Force"
verification: single-source
sourcing_note: >
  Single-source: one lab's own deception-environment telemetry, with no second party publishing independent analysis of
  these components. Reliability B as an original research lab, credibility 2. Three scoping points this entry holds to
  deliberately. First, targeting — X-Force states this activity extends a previously reported campaign against India's
  energy sector and government organisations, and names no European victim, lure or infrastructure anywhere; its only
  remark touching Western targets is a hedged general characterisation that the actor "may extend" such targeting, which
  is an actor-level assessment and not a finding about this campaign, so no European targeting is claimed here. Second,
  motive — that the actor aligns its activity to China's regional interests is explicitly X-Force's assessment, not a
  stated fact. Third, naming — X-Force says ITG27, formerly Hive0154, "overlaps with" the clusters others report as
  Mustang Panda, Stately Taurus, UNK_SteadySplit, Camaro Dragon, Twill Typhoon, Polaris and Earth Preta; that is an
  overlap claim across independently named clusters rather than an identity statement, and HoneyMyte — this store's
  existing alias for the registry record — is not among the names X-Force lists. X-Force also notes another vendor
  previously reported overlapping activity while categorising parts of the toolchain differently, so Claimloader is
  X-Force's own naming of a component already described elsewhere under a different grouping.
confidence: high
update_of: 2026-08-15/mustang-panda-coolclient-signed-kernel-driver-rootkit
references: ["2026-08-17/patchcord-sheetcord-google-sheets-c2-browser-shortcut-hijack"]
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

**UPDATE (originally covered 2026-08-15):** this pipeline covered a CoolClient variant attributed to this actor six days ago, installing a signed kernel driver that filtered its own C2 addresses out of the network data Windows returns to user mode. This is separate research on the same actor from a different lab, and the reason it is worth an update rather than nothing is that one of its two findings retires existing detection content.

**Toneshell v10 changes the channel, not just the payload.** "Earlier variants relied on custom socket-based communications, while version 10 transitions to secure WebSocket communications using WinHTTP over TLS" ([IBM X-Force, 2026-08-20](https://www.ibm.com/think/x-force/trapping-a-mustang-panda)). The implant now speaks through the operating system's own WinHTTP WebSocket routines and additionally queries the user's proxy configuration, so it is proxy-aware. The consequence for a network defender is direct: a signature or filter written against Toneshell's earlier bespoke socket protocol no longer matches anything, and what replaces it is traffic sharing port, protocol and TLS client-stack characteristics with every other WinHTTP-based Windows application and ordinary browser WebSocket session. Detection has to move to the client-stack TLS fingerprint, destination reputation, or endpoint-side visibility of the WebSocket API calls themselves — protocol shape alone no longer discriminates.

X-Force also found three standalone DLL builds of Toneshell v10 reusing the same WebSocket model, command dispatcher and reverse-shell functionality, two of them masquerading under the filename of a PDF-creation component and one as a browser-framework library. Between the dispatcher's command branches sit repeated blocks of wide-character junk strings referencing Harry Potter characters and themes — padding inserted to frustrate analysis.

**Havencode: hidden desktop access with nothing to extract from the binary.** X-Force had not previously observed this backdoor. Its centre of gravity is hidden Virtual Network Computing, letting an operator connect to an infected machine's desktop and browse it covertly. It ships as a 64-bit DLL alongside a legitimate signed executable and is launched by side-loading, and it takes three modes: a hidden-desktop VNC server on a supplied local port, a view-only mode that attaches to the user's *existing* desktop to watch without taking input control, and a generic TCP/UDP tunnel the operators used to relay the local VNC server's traffic out to their C2 — though X-Force notes the tunnel may serve any other proxy traffic too.

The detail that matters for hunting is what the file does not hold: "It does not contain any embedded C2 addresses. Instead, the C2 server is provided as command line argument at the time of execution". Static extraction of infrastructure from a recovered sample yields nothing; the address exists only in the process command line at launch, which makes process-creation telemetry with full command-line capture the difference between knowing where it called home and not.

The loader in front of it, which X-Force names Claimloader, copies the side-loading pair into a new installation directory — commonly under the system-wide program-data path — establishes persistence, then recovers embedded shellcode and executes the Toneshell payload by abusing a locale-enumeration API as a callback to transfer execution.

**What the deception environment showed that logs would not.** X-Force ran two fake victims — an operational technology company specialising in electric grids, and a state-level government agency — and captured the operators live. The evidence of hands-on-keyboard work is mundane and convincing: two commands were mistyped in both incidents, a domain-enumeration command and a wireless-network listing, and on its first attempt the crew launched Havencode with malformed arguments. X-Force's conclusion is that "This evidence is a strong indicator that most of the operator activity was not scripted but performed by hand", corroborated independently by timing — operator-initiated actions fell exclusively within weekday working hours of 08:00 to 18:00 China Standard Time, with activity pausing over a weekend and resuming afterwards. Initial access in the campaign came from a May 2026 email to Indian government recipients carrying a PDF attachment themed as a hydropower cooperation study and imitating Nepal's foreign ministry.

**Triage:** the side-load pair is the most reliable host-side discriminator, because the legitimate executable is genuinely signed and will pass any signature check — what is anomalous is that binary running from a program-data subdirectory rather than its installed location, with a same-named dependency DLL beside it. For Havencode specifically, look for a process whose command line carries a network address and a local port together with VNC-style mode arguments: the configuration is in the command line by design, so command-line logging is not optional here. On the network side, the honest position is that Toneshell v10's channel is hard to separate from benign WinHTTP WebSocket traffic; the tractable signals are a hidden-desktop VNC session being tunnelled out of a host that has no remote-support tooling deployed, and a rapid sequence of host and network reconnaissance commands — system information, current user, group enumeration, network connections and process listing in quick succession — which X-Force names as the pattern to alert on.

**Defender takeaway:** if you carry detection content for this family, the network half of it is now stale and should be re-based on endpoint API-level or TLS-fingerprint visibility rather than the retired custom protocol. More broadly, this is the second entry in a week showing this actor moving C2 onto channels that are indistinguishable from sanctioned traffic — the earlier CoolClient variant hid its addresses from the operating system's own reporting, and this one hides in the operating system's own HTTP stack. Note the targeting honestly: this campaign is aimed at Indian government and energy, so the value here is the tradecraft and the invalidated signatures, not a claim of exposure in this constituency. The operator's fixed working-hours pattern is also a reminder that for a hands-on-keyboard intrusion, log retention long enough to span a multi-day operational tempo — X-Force recommends at least 90 days — is what makes the pattern visible at all.
