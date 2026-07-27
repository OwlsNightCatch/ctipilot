---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "This week's tradecraft converged on hiding command-and-control inside trusted services and native tooling — Graph-API calendars, DNS, the Telegram API, a browser the malware never connects through, and BitLocker instead of a ransomware binary"
headline: "Unrelated W30 disclosures share one move — routing C2 and impact through trusted services and native tooling, so process/domain-based detection stays blind"
summary: >
  Six independently-reported 2026-W30 disclosures converge on one defensive problem: attackers are routing command-and-control and impact through services and binaries defenders already trust, so detection keyed on "an unknown process opened a socket" or "traffic to an unknown domain" does not fire. Group-IB's HOLLOWGRAPH turns a compromised Microsoft 365 calendar into a Graph-API dead-drop and Kaspersky corroborated the same Cavern framework recovering C2 settings via DNS AAAA records when Graph auth fails; Cisco Talos's msaRAT drives a headless browser over the Chrome DevTools Protocol so the malware process itself never opens a socket, tunnelling over WebRTC relayed via a Twilio TURN server with Cloudflare Workers handling signalling; Zscaler's TELESHIM uses the Telegram Bot API for C2 to blend with mainstream traffic; Proofpoint's Cruciferra crypter pairs process-ghosting and BYOVD EDR termination with indirect syscalls from a clean ntdll copy; and Kaspersky's "XEntry" extortion cases used native BitLocker, RMM tooling and Group Policy for encryption-for-impact instead of a bespoke ransomware family. The transferable lesson is that endpoint and network detection must key on behaviour and sequence, not on process reputation or destination novelty.
discovered_at: "2026-07-26T23:43:00Z"
event_date: 2026-07-23
run_id: 2026-07-26T2309Z-weekly
priority: notable
immediate_action: null
tags:
  - espionage
  - identity
  - ransomware
  - cloud
regions:
  - global
  - europe
  - middle-east
sectors:
  - public-sector
  - finance
  - healthcare
  - technology
entities:
  - tool:hollowgraph-malware
  - tool:cavern-c2-framework
  - actor:cavern-manticore
  - actor:chaos-ransomware
  - malware:msarat
  - actor:ta4922
  - tool:cruciferra-crypter
  - actor:xentry-team
cves: []
techniques:
  - T1102.002
  - T1071.004
  - T1071.001
  - T1090
  - T1055.012
  - T1685
  - T1486
affected_products: []
sources:
  - url: "https://www.group-ib.com/blog/hollowgraph-microsoft-365/"
    publisher: "Group-IB Threat Intelligence"
    date: "2026-07-20"
    role: primary
  - url: "https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/"
    publisher: "Kaspersky (Securelist / GReAT)"
    date: "2026-07-21"
    role: primary
  - url: "https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/"
    publisher: "Cisco Talos"
    date: "2026-07-23"
    role: primary
  - url: "https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-1"
    publisher: "Zscaler ThreatLabz"
    date: "2026-07-20"
    role: primary
  - url: "https://www.proofpoint.com/us/blog/threat-insight/unpacking-cruciferra-analysis-sophisticated-crypter-service"
    publisher: "Proofpoint Threat Insight"
    date: "2026-07-20"
    role: primary
  - url: "https://securelist.com/new-extortion-scheme-printers-bitlocker/120718/"
    publisher: "Kaspersky (Securelist / GERT)"
    date: "2026-07-21"
    role: primary
closed_sources: []
evidence:
  - quote: "This RAT never touches the network directly — it controls its C2 communication channel exclusively through Chrome DevTools Protocol (CDP), a browser debugging API."
    publisher: "Cisco Talos"
  - quote: "TELESHIM abuses the Telegram API for C2 communication, a technique used to blend in with legitimate internet traffic."
    publisher: "Zscaler ThreatLabz"
verification: multi-source
sourcing_note: "Six independent first-party research publications; the HOLLOWGRAPH/Cavern strand is doubly sourced (Group-IB, then Kaspersky corroboration of the same framework). The XEntry cases are victim-anonymous LatAm incidents whose value is the LOTL technique, not the victim; Kaspersky itself does not confirm the two cases are the same operator, which the entry preserves."
confidence: high
update_of: null
references:
  - 2026-07-21/hollowgraph-m365-calendar-graph-api-c2-cavern
  - 2026-07-22/cavern-cav3rn-oilrig-attribution-dns-aaaa-c2-fallback
  - 2026-07-24/msarat-chaos-cdp-webrtc-covert-c2
  - 2026-07-26/teleshim-bindcloak-volume-serial-keying-government-espionage
  - 2026-07-21/cruciferra-crypter-as-a-service-process-ghosting-byovd
  - 2026-07-22/xentry-team-bitlocker-lotl-extortion-rmm-gpo
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

Six unrelated pieces of 2026-W30 research, read together, describe one defensive problem more usefully than any single sample: attackers are increasingly routing both command-and-control and impact through infrastructure and tooling defenders already trust, so detection that keys on process reputation or destination novelty is blind to it. This extends the prior weekly's state-nexus "blinding the defender's own visibility" theme from EDR-evasion into a broader pattern — the trusted carrier is the point.

On the C2 side, the convergence is striking. Group-IB's HOLLOWGRAPH never contacts attacker infrastructure directly: it plants and reads tasking as attachments on far-future Microsoft 365 calendar events via the Graph API, and Kaspersky independently corroborated the same Cavern framework, adding a resilience layer in which — when Microsoft Graph authentication or tenant validation fails — the module recovers replacement connection settings (TenantId, ClientId, ClientSecret, UserEmail) via DNS AAAA responses from attacker nameservers ([Kaspersky, 2026-07-21](https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/)). Cisco Talos's msaRAT goes further and removes the socket from the malware entirely — "This RAT never touches the network directly — it controls its C2 communication channel exclusively through Chrome DevTools Protocol (CDP), a browser debugging API" ([Cisco Talos, 2026-07-23](https://blog.talosintelligence.com/chaos-msarat-living-off-the-browser-to-build-covert-c2-channel/)), driving a headless browser to tunnel over a WebRTC DataChannel relayed via a Twilio TURN server (with Cloudflare Workers handling the signalling), so endpoint tooling that asks "which process opened the connection" sees only the browser. Zscaler's TELESHIM, used against Middle-East government targets, "abuses the Telegram API for C2 communication, a technique used to blend in with legitimate internet traffic" ([Zscaler ThreatLabz, 2026-07-20](https://www.zscaler.com/blogs/security-research/targeted-attack-government-entities-middle-east-part-1)).

The same "use what is trusted" logic runs through the endpoint and impact layers. Proofpoint's Cruciferra crypter-as-a-service — used by the China-nexus actor TA4922 to deliver AsyncRAT — combines a process-ghosting loader with BYOVD EDR termination and indirect syscalls issued from a clean on-disk copy of `ntdll.dll`, defeating user-mode hooks that monitor the loaded copy ([Proofpoint, 2026-07-20](https://www.proofpoint.com/us/blog/threat-insight/unpacking-cruciferra-analysis-sophisticated-crypter-service)). And Kaspersky's "XEntry" extortion cases skipped a bespoke ransomware family entirely, entering via internet-exposed RDP and a misconfigured SQL Server and then using legitimate RMM tooling and a Group Policy Object to deploy native BitLocker for encryption-for-impact ([Kaspersky, 2026-07-21](https://securelist.com/new-extortion-scheme-printers-bitlocker/120718/)) — an impact stage with no malware artifact to signature at all.

**Defender takeaway:** these six do not share a signature, an actor, or a victim profile — they share a design goal, which is why the detection response is architectural rather than per-sample. Reason from sequence and context, not from process reputation or destination: alert on an office/agent process spawning or driving a headless browser with remote-debugging flags (the msaRAT pattern); treat Graph-API calendar/attachment activity and outbound DNS AAAA lookups to non-corporate nameservers from server workloads as C2-candidate telemetry, not noise (HOLLOWGRAPH/Cavern); baseline which hosts legitimately speak to the Telegram API and RMM control planes and alert on new ones (TELESHIM, XEntry); and monitor BitLocker enablement and recovery-key changes as a potential impact event, since native encryption leaves no ransomware binary to find. Per-technique mechanics and telemetry detail are in the referenced operational entries.
