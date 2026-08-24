---
schema: 1
kind: research
horizon: operational
title: "FTP server banners are being used as dead-drop resolvers for two undocumented RATs — and the researchers' own judgement is that this makes the channel easier to catch than a web-based dead drop, not harder"
headline: "E4del and PINHOLE resolve tasking from FTP banner text — and SOCRadar judges that channel easier to flag than a web-based dead drop"
summary: >
  SOCRadar's threat research unit documented two previously undocumented remote-access trojans, E4del and PINHOLE,
  whose delivery chain reads its instructions out of the greeting banner an FTP server returns on connection —
  weaponised since early July 2026 and still live, reached through malicious shortcut files. PINHOLE is the more
  capable of the two: fourteen command types, C2 resolved by fetching Pinterest pins or SurveyMonkey survey
  questions behind a Cloudflare Workers proxy, configuration hidden in NTFS alternate data streams on two
  desktop.ini files, userland-hook evasion by inspecting neighbouring syscall stubs, Early Bird APC injection, and
  only a single 4 KB page of payload decrypted at any moment. The finding that cuts against the obvious framing is
  SOCRadar's own: it judges the FTP channel less stealthy than a web-based dead drop, because security teams are
  more likely to flag an FTP connection to an unknown server as anomalous.
discovered_at: "2026-08-24T09:16:00Z"
event_date: "2026-08-21"
run_id: 2026-08-24T0410Z-intel
priority: notable
immediate_action: null
tags: [infostealer, phishing, organized-crime]
regions: [global]
sectors: [public-sector, technology]
entities:
  - malware:e4del
  - malware:pinhole
techniques: [T1102.001, T1204.002, T1059.001, T1027.013, T1564.004, T1547.001, T1055.004, T1106, T1497, T1620, T1105, T1113, T1555.003, T1090]
affected_products: []
cves: []
sources:
  - url: "https://socradar.io/blog/ftp-banners-new-dead-drop-resolver-rats/"
    publisher: "SOCRadar Threat Research Unit"
    date: "2026-08-21"
    role: primary
closed_sources: []
evidence:
  - quote: "To obtain its C2, PINHOLE uses curl to fetch content from Pinterest pins or SurveyMonkey survey questions."
    publisher: "SOCRadar Threat Research Unit"
  - quote: "However, this method is less stealthy than traditional web-based DDRs, as security teams are more likely to flag FTP connections to unknown servers as anomalous."
    publisher: "SOCRadar Threat Research Unit"
  - quote: "This flow ensures that only a single 4 KB page of the payload remains decrypted and executable at any given time (a mechanism commonly referred to as shellcode fluctuation)."
    publisher: "SOCRadar Threat Research Unit"
verification: single-source
sourcing_note: >
  Single-source: SOCRadar's threat research unit is the only party to have published this analysis, and it credits the
  underlying observation of FTP banners carrying dead-drop strings to an earlier post by MalwareHunterTeam whose
  referenced infrastructure SOCRadar found no longer active. SOCRadar attributes no actor and states explicitly that
  the novelty of both families leaves evidence insufficient for attribution; it treats E4del and PINHOLE as two
  separate clusters using the same delivery technique rather than one operator. Its assessment that the technique is
  adaptable to paste-and-run social engineering is stated as plausible rather than observed, and is carried that way
  here. Reliability is set to C to match this publisher's own record in sources/sources.json, whose note is that
  single-vendor investigative claims from it should be corroborated — and none of this is corroborated. The research
  is detailed and internally consistent, which is why it is published, but the letter tracks the source rather than
  the apparent quality of one post.
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
actions: []
migrated_from: null
---

SOCRadar's threat research unit published an analysis on 2026-08-21 of a delivery technique that puts the attacker's instructions somewhere most egress monitoring never reads: **the greeting banner an FTP server returns when a client connects** ([SOCRadar, 2026-08-21](https://socradar.io/blog/ftp-banners-new-dead-drop-resolver-rats/)). The capability was first noted publicly by another researcher whose referenced infrastructure had gone dark; SOCRadar re-found live instances through internet-scan search and reports the technique weaponised since early July 2026 with new infrastructure still appearing in August. Initial access in the observed cases is a malicious shortcut file, likely distributed by phishing, which pulls its next-stage command out of the banner response rather than from a hardcoded string in the file itself.

Two previously undocumented families ride it. **E4del** is an Electron-based modular trojan masquerading as a signed Discord binary, with a tiered jitter system for its command-and-control timing. Its execution path takes an authentication token out of the operator's own command string, calls a download endpoint keyed to that token and a hardware identifier, drops a dynamically generated archive under the user's local application-data tree, spawns a hidden PowerShell process to expand it, searches the result recursively for a configuration file naming the intended entry point, launches it as a fully detached hidden child process, then deletes the archive and the configuration to remove its own traces.

**PINHOLE** is the more capable and the more instructive. It carries fourteen distinct command types including browser-credential theft, file upload and download, and screenshot capture, and maintains an operator-facing statistics panel tracking script executions and connecting and blocked addresses — which at the time of analysis showed the script had run only eleven times, suggesting an early-stage campaign. Its rendezvous is layered: "To obtain its C2, PINHOLE uses curl to fetch content from Pinterest pins or SurveyMonkey survey questions," then proxies the resolved address behind Cloudflare Workers, falling back to direct communication if the proxy fails. Its configuration — build token and the key used to decrypt the resolver material — is stored not in a file body but in the **NTFS alternate data streams of two `desktop.ini` files**, encoded with a custom alphabet and then encrypted. Once resolved it polls a health endpoint expecting a specific short string, then fetches its next stage disguised with a fake JPEG header it strips and byte-decrements before use, with six layers of unpacking before execution. Its evasion set is unusually complete for a new family: an anti-emulation guard that inspects the export tables of the core Windows libraries for the wildcard-template stub names characteristic of analysis sandboxes and exits if it finds them; syscall-number recovery by scanning neighbouring unhooked functions and calculating the target's number arithmetically, defeating userland hooks placed on the function it actually wants; Early Bird APC injection into a legitimate process; persistence through a legacy registry load value with a copy of itself under a randomly named directory in the user's local application data; and a memory-residency trick where "This flow ensures that only a single 4 KB page of the payload remains decrypted and executable at any given time (a mechanism commonly referred to as shellcode fluctuation)," leaving the bulk of an already-small payload encrypted in any memory capture taken at an arbitrary moment.

The judgement worth carrying is SOCRadar's own, and it inverts the natural reading of a novel channel: "However, this method is less stealthy than traditional web-based DDRs, as security teams are more likely to flag FTP connections to unknown servers as anomalous." Where the recently documented dead-drop carriers — public blockchain contracts, collaboration and productivity APIs, code-hosting gists — succeed precisely because the destination is a service an enterprise has a legitimate reason to reach, an outbound FTP session from a workstation to an unfamiliar host has no such cover in most estates.

**Defender takeaway:** treat this as the cheapest dead-drop hunt currently available rather than a new blind spot. Outbound FTP from user workstations is close to obsolete in a modern corporate estate, so in egress and firewall telemetry the control port reaching an external host that is not on a short, known list of business partners is both rare and easy to enumerate — and because the resolver step happens before any implant configuration exists, catching it interrupts the chain earlier than a C2 detection would. The second-order lesson is a limit on the technique's own novelty: because PINHOLE ultimately resolves through consumer web services and a serverless proxy, blocking FTP does not remove that estate's exposure to the same operators, it removes exposure to this delivery variant.

**Triage:** several of these behaviours have common benign twins, so the discriminators are process identity and location. Shortcut files execute legitimately all the time; the signal is a shortcut whose execution spawns a network client and then a hidden interpreter. Alternate data streams on `desktop.ini` are the load-bearing artefact here and are effectively never populated by legitimate software — a non-empty alternate stream on a `desktop.ini` file is worth investigating on its own, whereas alternate streams generally carry benign download-provenance markers and should not be. Archive expansion under the user's local application-data tree by a hidden PowerShell process, followed by execution of a binary from a randomly named subdirectory there, is the E4del staging shape; the same directory is used constantly by legitimate installers, so the parent process and the hidden window are what separate them. For the anti-analysis behaviour there is no useful endpoint discriminator, because a successful check produces no event — it simply exits.
