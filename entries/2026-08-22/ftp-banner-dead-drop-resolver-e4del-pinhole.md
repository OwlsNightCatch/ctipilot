---
schema: 1
kind: threat
horizon: operational
title: "A malware stager is reading its next instruction out of an FTP server's pre-login greeting — and the researchers who found it point out this is the rare command channel that is easier to catch, not harder"
headline: "One of the two RATs it delivers replaces the code inside a legitimately signed desktop application without touching its signature"
summary: >
  SOCRadar's Threat Research Unit documents a delivery chain, live since early July 2026 with fresh
  infrastructure in August, whose stager takes its next instruction from the greeting text an FTP server
  emits before login — a dead-drop channel outside the web, DNS and blockchain resolvers the industry has
  built inspection and takedown workflows around. The researchers are candid that the trade-off runs
  against the attacker: because enterprise traffic to arbitrary internet FTP servers is rare, they expect
  security teams are more likely to flag it as anomalous. Two previously undocumented remote-access trojans
  arrive this way. E4del replaces the contents of a legitimately signed Electron desktop application's
  resource archive with its own logic, so the operating system sees a signed, correctly published binary
  loading trusted dependencies. PINHOLE is built for sensor evasion and holds its command-and-control
  configuration in ordinary consumer web platforms rather than on attacker infrastructure.
discovered_at: "2026-08-22T05:11:30Z"
event_date: "2026-08-21"
run_id: 2026-08-22T0410Z-intel
priority: notable
immediate_action: null
tags: [phishing, infostealer, organized-crime]
regions: [global]
sectors: [public-sector, technology]
entities: [malware:e4del, malware:pinhole-rat]
techniques: [T1566.001, T1204.002, T1071.002, T1102.001, T1059.001, T1059.003, T1059.007, T1047, T1106, T1218.015, T1140, T1036.005, T1497.001, T1564.003, T1070.004, T1564.004, T1027, T1055.004, T1547.001, T1082, T1057, T1083, T1518.001, T1012, T1033, T1548, T1113, T1555.003, T1041, T1071.001, T1090, T1573.001, T1205, T1105, T1583.007]
affected_products: []
cves: []
sources:
  - url: "https://socradar.io/blog/ftp-banners-new-dead-drop-resolver-rats/"
    publisher: "SOCRadar Threat Research Unit"
    date: "2026-08-21"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/hackers-abuse-ftp-server-banners-to-deliver-new-windows-malware/"
    publisher: "BleepingComputer"
    date: "2026-08-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "two previously undocumented Remote Access Trojans (RATs), which we have named E4del and PINHOLE"
    publisher: "SOCRadar Threat Research Unit"
  - quote: "this method is less stealthy than traditional web-based DDRs, as security teams are more likely to flag FTP connections to unknown servers as anomalous."
    publisher: "SOCRadar Threat Research Unit"
  - quote: "the operating system identifies a digitally signed Discord.exe loading trusted dependencies, effectively masking the malicious code residing in app_bootstrap/index.js."
    publisher: "SOCRadar Threat Research Unit"
verification: single-source
sourcing_note: >
  Two publications, one origin — and the ratings are the opposite way round from how this item first
  surfaced. SOCRadar's research unit did the original work: it identified the technique in its own
  investigation, hunted infrastructure to establish the channel was still live, and reverse-engineered and
  named both malware families. BleepingComputer states in its own text that it is working from a report
  shared with it, adds no independent analysis or telemetry, and every technical claim in it traces back to
  the SOCRadar report — so it is a second publisher rather than a second assessor, the item does not clear
  the two-source bar in substance, and it is recorded as single-source with credibility 2. Reliability is C rather than B, and deliberately so: this pipeline's source registry rates this
  publisher C as a source that mainly re-reports, and one piece of original reverse engineering does not
  re-letter the record — the rating follows the source's track record, not its best single output. The
  entry's substance is treated as original work regardless, which is why the relaying outlet is not
  counted as corroboration. Discovery credit for the FTP-banner channel itself belongs to neither: SOCRadar states a
  post by another researcher first documented the capability, and its own contribution was to hunt onward
  after the originally described infrastructure went dark. Neither source names the platform that post
  appeared on, so this entry does not either. Two limits are carried rather than papered over: initial
  access is SOCRadar's assessment — an archive containing a shortcut file, with phishing named as the
  likely delivery — not an observed fact; and one of the two implants has an escalation command that loads
  a native module SOCRadar could not retrieve, so its privilege-escalation route is unknown rather than
  merely unstated. SOCRadar assesses the two implants as separate clusters using the same delivery
  technique and states the evidence is currently insufficient for attribution.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions:
  - "Run a bounded hunt over egress logs from early July 2026 onward for outbound FTP control connections to hosts outside the known business baseline, and treat each hit as an investigation rather than a tuning exercise. This is the rare command channel where the researchers themselves expect the anomaly rate to favour the defender: in most enterprises, endpoints do not initiate FTP to arbitrary internet servers at all, so the result set should be small enough to work by hand."
migrated_from: null
---

SOCRadar's Threat Research Unit documents a delivery chain whose novelty is where the stager gets its orders. A dead-drop resolver is a legitimate service abused to hold the attacker's addresses or commands so the delivered payload never carries them itself; the channels defenders have learned to watch are code-hosting and social platforms, DNS records and blockchain transactions. Here the stager reads its next instruction from the greeting text an FTP server sends *before login* — the pre-authentication banner. That evades the inspection, reputation and takedown machinery built for the other channels for a simple structural reason: an FTP handshake's opening response is normally treated as connection metadata rather than as content to inspect, and it is retrieved without ever authenticating, so no credential or session artifact is produced. SOCRadar establishes the technique has been in use since early July 2026 with new infrastructure as recently as August 2026, names two previously undocumented remote-access trojans it found delivered this way, and assesses them as separate clusters sharing one delivery technique with insufficient evidence for attribution ([SOCRadar, 2026-08-21](https://socradar.io/blog/ftp-banners-new-dead-drop-resolver-rats/)).

The most useful sentence in the report is the one arguing against its own headline. SOCRadar states plainly that this method is less stealthy than traditional web-based resolvers, because security teams are more likely to flag FTP connections to unknown servers as anomalous ([SOCRadar, 2026-08-21](https://socradar.io/blog/ftp-banners-new-dead-drop-resolver-rats/)). That is worth taking at face value. The reason web-service resolvers are hard to catch is volume: an endpoint reaching a major code-hosting or video platform is indistinguishable from a million legitimate requests. An endpoint opening an FTP control connection to an arbitrary internet host, in a modern enterprise, is close to unheard of. This is a novel channel that happens to be a better detection opportunity than the one it replaces, which is not the usual direction of travel.

The signature-trust lesson in the first implant generalises well past this campaign. E4del abuses how Electron desktop applications are built: the application's own JavaScript logic does not live inside the signed executable but in a resource archive beside it. The actors ship a legitimate, digitally signed vendor executable — a widely used chat client — along with the runtime libraries it expects, and replace the contents of that resource archive with their own code. SOCRadar's description of the consequence is the point: the operating system identifies a digitally signed binary loading trusted dependencies, masking the malicious code residing in the replaced application logic ([SOCRadar, 2026-08-21](https://socradar.io/blog/ftp-banners-new-dead-drop-resolver-rats/)). No signature is broken or forged, and the process name, publisher and certificate all check out against an allowlist. Any signed application that hosts an interpreter and loads its logic from a sibling resource file inherits the same weakness. The behavioural discriminators SOCRadar surfaces are what a defender can actually use: the implant runs the host application with switches that suppress any window, so a chat client is resident with no interface ever drawn; it enumerates installed security products before beaconing; it refuses to run unless invoked with an argument matching the intended victim's username, which is an anti-analysis check and also a reason a sandbox verdict may come back clean; and it persists by registering the signed host binary as a login item rather than dropping anything new. The second implant, PINHOLE, is built for endpoint-sensor evasion — recovering syscall numbers from neighbouring unhooked functions to issue direct calls, keeping only a small slice of its payload resident in memory at a time, and injecting its final stage into a suspended standard Windows interface-host process — and holds its command-and-control configuration in ordinary consumer web platforms rather than on infrastructure that can be taken down.

**Defender takeaway:** three hunts follow, in descending order of yield. The egress hunt for outbound FTP control connections to non-baseline hosts is the cheapest and the one the researchers themselves expect to work. Second, file-modification telemetry on the resource archives and sibling runtime files of installed signed applications: a legitimate application rewrites its own resource archive only during a vendor update, so a write to it from anything other than the vendor's updater is anomalous, and this is a check most estates have never configured because the file is not an executable. Third, autostart-configuration telemetry — an entry pointing at a legitimately signed consumer application is not suspicious in itself, which is precisely why it is being used, so the pairing to look for is a login-item registration for a signed application that is also running windowless from a non-standard path. **Triage:** the FTP signal has a small but real benign population — legacy transfers to suppliers, scientific-data mirrors, network-equipment firmware fetches — so the discriminator is the initiating process rather than the protocol: an FTP control connection from a script host, a shortcut-launched interpreter or a desktop application is not the same event as one from a sanctioned transfer client. For the signed-application half, the trap is the opposite: everything about the process looks correct, and the only things that do not fit are that the application is running with no window ever drawn and that its resource archive changed outside an update cycle.
