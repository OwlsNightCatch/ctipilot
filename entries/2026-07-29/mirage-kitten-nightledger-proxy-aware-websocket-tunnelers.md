---
schema: 1
kind: threat
title: "Mirage Kitten (UNC1549) fields the NightLedger backdoor and two WebSocket tunnelers, one of them built to negotiate through corporate proxies with the victim's own SSO"
headline: "Kaspersky documents an Iran-nexus toolset that loads under a legitimate vendor binary via RPC delay-load and tunnels out through authenticated proxies"
summary: >
  Kaspersky GReAT published previously undocumented tooling from Mirage Kitten on 2026-07-28 — the
  actor it states is also tracked as UNC1549, Smoke Sandstorm and Nimbus Manticore. NightLedger is a
  Windows backdoor that masquerades as SspiCli.dll and loads under the legitimate AppVShNotify.exe by
  way of RPCRT4.dll's delay-load, forwarding real exports so the host process keeps working, and takes
  16 numeric commands including screenshot capture and collection of the domain-join diagnostic log.
  BridgeHead, one of two companion tunnelers, is the one engineered for defended networks: it relays
  SOCKS5 over an authenticated WebSocket and, on an HTTP 407, queries the available auth schemes, prefers
  Negotiate over NTLM and retries with the logged-in user's SSO context. It also gates execution on a
  3-character substring of the lowercased Windows username, so a sample only runs on its intended host.
  ArcBridge is the simpler of the two, carrying an embedded C2 configuration block and two commands.
discovered_at: "2026-07-29T05:30:00Z"
event_date: "2026-07-28"
run_id: 2026-07-29T0408Z-intel
priority: notable
immediate_action: null
tags: [nation-state, espionage, iran-nexus]
regions: [middle-east, africa, global]
sectors: [public-sector, telco, transport, defense, finance]
entities: [actor:screening-serpens-unc1549-smoke-sandstorm-nimbus-manticore-iran-apt, tool:nightledger-backdoor, tool:bridgehead-tunneler, tool:arcbridge-tunneler]
techniques: [T1574.001, T1071.001, T1090, T1572, T1113, T1057, T1082, T1016]
affected_products: []
cves: []
sources:
  - url: "https://securelist.com/mirage-kitten-new-tools/120811/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-07-28"
    role: primary
closed_sources: []
evidence:
  - quote: "The implant masquerades as SspiCli.dll and appears to be designed for DLL search-order hijacking, targeting a legitimate AppVShNotify.exe binary. While AppVShNotify.exe does not directly import SspiCli.dll, it imports RPCRT4.dll, which can delay-load SspiCli.dll when it invokes an RPC API that requires authentication."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "Still, it implements the same technique of limiting execution to a specific username on the infected machine by hardcoding a 3-character control value that must appear as a substring in the lowercased Windows username retrieved via GetUserNameA. If the match fails, the implant silently exits, confirming per-target tailoring of each deployed binary."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "According to our telemetry, we identified victims across Middle East and African countries including Egypt, SMB and government environments in Jordan and Tanzania, aviation organizations in Pakistan, telecommunication companies in Ethiopia and financial-sector entities in Burkina Faso."
    publisher: "Kaspersky Securelist (GReAT)"
verification: single-source
sourcing_note: >
  Single-source: Kaspersky GReAT's own telemetry and reverse engineering, with no second lab reporting on
  this toolset. Three sourcing distinctions are preserved deliberately. The alias set — Mirage Kitten as
  UNC1549, Smoke Sandstorm and Nimbus Manticore — is Kaspersky's own stated equivalence in its opening
  sentence, not an inference drawn here or imported from another vendor. The link between NightLedger and
  the earlier TWOSTROKE implant is presented by Kaspersky as a development-standpoint similarity in
  command-dispatch structure and carries no calibrated confidence phrase, so it is reported here as the
  structural observation it is rather than as a graded assessment. The attribution of NightLedger to the
  group does carry a stated basis — code and behavioural similarity to the group's historical implants.
  Kaspersky separately notes BridgeHead's proxy logic closely mirrors a backdoor it tracks internally as
  Retrograde, which it says overlaps with tooling publicly reported as MiniFast and MiniUpdate; that
  lineage is recorded here but not turned into a registry relationship, since the internal name has no
  public record to anchor a canonical entity to. Command-and-control hostnames, endpoint paths and the
  literal username-gate value are omitted as indicators. The two tunnelers are described separately and
  deliberately: the SOCKS5 relaying, the proxy-authentication negotiation and the username gate are all
  BridgeHead's, and Kaspersky's ArcBridge section claims none of them. Kaspersky also makes no statement
  about the code-signing status of the binary NightLedger loads under, so it is described only as
  legitimate rather than signed.
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

The load-bearing detail in Kaspersky's write-up is not the backdoor's feature list but how it gets to run and how it gets out. NightLedger ships as a file named to impersonate `SspiCli.dll` and is placed alongside a legitimate `AppVShNotify.exe`; that binary does not import `SspiCli.dll` directly, but it does import `RPCRT4.dll`, which delay-loads `SspiCli.dll` at the moment it invokes an RPC API requiring authentication — so the malicious module is pulled in through the normal search order, under a legitimate vendor process, and forwards the expected exports to the genuine DLL so the host keeps functioning ([Kaspersky Securelist, 2026-07-28](https://securelist.com/mirage-kitten-new-tools/120811/)). Two properties make this awkward to catch: the load is triggered by ordinary RPC activity rather than by anything the malware does, and because exports are proxied there is no crash or functional break to notice. The backdoor beacons over HTTPS and dispatches 16 numeric commands, among them process execution, identity and host/network reconnaissance, process listing and termination, directory and drive enumeration, file copy, deletion, upload and download, screenshot capture, DLL loading, beacon-interval changes, and collection of the Windows domain-join diagnostic log, which Kaspersky describes as a diagnostic log generated during domain and workgroup join, unjoin and related network-setup operations ([Kaspersky Securelist, 2026-07-28](https://securelist.com/mirage-kitten-new-tools/120811/)). Kaspersky attributes NightLedger to Mirage Kitten on code and behavioural similarity to the group's historical implants, and observes that its command dispatch resembles TWOSTROKE, an implant previously documented as the same actor's ([Kaspersky Securelist, 2026-07-28](https://securelist.com/mirage-kitten-new-tools/120811/)).

The tunnelers are the part worth a hunt cycle, and the two are not equivalent. Kaspersky describes ArcBridge as the simpler tool: a WebSocket-style channel with an embedded configuration block carrying C2 host, port, a retry value, an SSL flag and a likely implant identifier, driven by two commands — one to open a tunnel session and one to resolve a hostname ([Kaspersky Securelist, 2026-07-28](https://securelist.com/mirage-kitten-new-tools/120811/)). BridgeHead is the one built for networks that do not simply let traffic out: presented with an HTTP 407 proxy-authentication challenge it queries which schemes the proxy supports, selects Negotiate in preference to NTLM, supplies null credentials so Windows fills in the logged-in user's single-sign-on context, and retries — falling back to exponential connection retry capped at a minute when that fails ([Kaspersky Securelist, 2026-07-28](https://securelist.com/mirage-kitten-new-tools/120811/)). The consequence for defenders is that the outbound channel authenticates as a real employee to the real proxy, so it appears in proxy logs as that user's traffic. Once established, the operator drives everything server-side and the implant only forwards, which Kaspersky describes as turning the host into a relay node so that resulting TCP traffic appears to originate inside the victim's network ([Kaspersky Securelist, 2026-07-28](https://securelist.com/mirage-kitten-new-tools/120811/)). BridgeHead also refuses to run outside its intended target: a hardcoded 3-character value must appear as a substring of the lowercased Windows username, and the implant exits silently otherwise — behaviour Kaspersky reads as evidence of prior internal reconnaissance and per-target tailoring of each binary ([Kaspersky Securelist, 2026-07-28](https://securelist.com/mirage-kitten-new-tools/120811/)). Victims span government and SMB environments in Jordan and Tanzania, aviation in Pakistan, telecommunications in Ethiopia, finance in Burkina Faso and organisations in Egypt ([Kaspersky Securelist, 2026-07-28](https://securelist.com/mirage-kitten-new-tools/120811/)).

**Defender takeaway:** two of this toolset's design decisions defeat detections that are common and reasonable. Proxy-log review that treats authenticated, user-attributed egress as trustworthy will pass BridgeHead traffic, because the implant deliberately borrows the user's SSO context rather than avoiding the proxy; and sandbox or bulk-sample triage will see nothing at all, because the username gate makes a sample inert anywhere except its intended host — which also means a negative dynamic-analysis result on a suspicious binary from this family is not evidence of benignity. The durable hunt is on module provenance rather than process behaviour: enumerate loaded modules named for Windows system DLLs that resolve from an application directory instead of the system directory, and check the signature of what actually loaded.

**Triage:** `AppVShNotify.exe` loading `SspiCli.dll` is normal and expected — the parent process, the module name and the RPC trigger are all legitimate, so none of them discriminates on its own. The signal is the loaded file's identity: `SspiCli.dll` resolving from the same directory as the executable rather than from the system directory, and not carrying a valid Microsoft signature. On the network side, an authenticated proxy session that upgrades to a long-lived WebSocket and then carries a sustained, bidirectional flow to a single destination is the shape to look for; ordinary user browsing through the same proxy does not hold one connection open as a steady tunnel.
