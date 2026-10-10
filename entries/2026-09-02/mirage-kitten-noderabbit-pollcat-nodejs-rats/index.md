---
schema: 1
kind: threat
title: "Mirage Kitten (Nimbus Manticore/UNC1549) debuts Node.js and JavaScript RATs — NodeRabbit and PollCat — delivered through fake LinkedIn technical-hiring assessments"
headline: "An Iranian espionage actor's first scripting-language implants arrive inside a timed take-home coding challenge"
summary: >
  Kaspersky's GReAT team documented (2026-09-01) two previously undocumented cross-platform RATs,
  NodeRabbit (Node.js) and PollCat (JavaScript), attributed with high confidence to Mirage Kitten —
  the Iran-nexus actor also tracked as Nimbus Manticore/UNC1549/Smoke Sandstorm. Both are delivered
  through fake LinkedIn recruiter personas offering timed technical-hiring assessments whose bundled
  npm package launches the implant on import. Confirmed victims are in fintech, aviation and
  aerospace in Egypt, Ethiopia and Afghanistan; no CVE is involved.
discovered_at: "2026-09-02T05:00:00Z"
updated_at: null
event_date: "2026-09-01"
run_id: 2026-09-02T0411Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, phishing, iran-nexus]
regions: [middle-east, africa]
sectors: [aviation, finance]
entities:
  - "actor:screening-serpens-unc1549-smoke-sandstorm-nimbus-manticore-iran-apt"
  - "tool:noderabbit"
  - "tool:pollcat"
techniques: [T1566.003, T1204.002, T1053.005, T1053.003, T1547.001, T1497, T1071.001, T1573.001, T1027, T1114.001, T1059.007]
affected_products: []
cves: []
sources:
  - url: "https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-09-01"
    role: primary
  - url: "https://therecord.media/iranian-cyber-spies-target-aviation-fintech-new-malware"
    publisher: "The Record (Recorded Future News)"
    date: "2026-09-01"
    role: corroborating
closed_sources: []
evidence:
  - quote: "NodeRabbit and PollCat represent the first publicly documented use of Node.js- and JavaScript-based malware by this APT group."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "We attribute this activity to Mirage Kitten with a high degree of confidence based on the following observations"
    publisher: "Kaspersky Securelist (GReAT)"
verification: single-source
sourcing_note: >
  The Record's article restates Kaspersky's own investigation and attribution ("tracked by ...
  Kaspersky as Mirage Kitten") rather than independently corroborating it — a press write-up of one
  lab's research is not a second assessor. Credibility
  is set accordingly at 2, not 1.
confidence: high
references: []
deep_dive: true
deep_dive_category: apt-campaign
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Kaspersky's GReAT team published an analysis on 2026-09-01 of two previously undocumented cross-platform remote access trojans it attributes with high confidence to Mirage Kitten, the Iran-nexus actor this store already tracks under the alias cluster Screening Serpens/UNC1549/Smoke Sandstorm/Nimbus Manticore ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)). NodeRabbit and PollCat are "the first publicly documented use of Node.js- and JavaScript-based malware by this APT group," a departure from its historically native C/C++/Go tooling delivered via DLL search-order hijacking ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)).

**Delivery.** A fake recruiter persona on a job-search platform invites a target — in one documented case a software engineer approached about an opening at an unnamed major technology company — to complete a technical assessment, directing them to a coding challenge hosted on Amazon S3 and pressuring them to download and run it immediately (T1566.003, T1204.002) ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)). The NodeRabbit archive gives candidates a three-hour window to review the application and fix defects in its frontend, and separately claims the actual malicious file, `server.js`, is bug-free and should not be modified — steering attention away from the one file the attackers altered — while banning AI-assisted review, which Kaspersky notes would likely have flagged the suspicious first-line import of an unknown package ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)); the PollCat archive is a one-hour, OTP-gated React "CTF" challenge. The malicious code sits in a locally bundled, never-registry-published npm package (`colorized_terminal` or `pretty-log`) imported by the assessment's own project files ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)), which launches the implant the moment the candidate runs the project.

**NodeRabbit.** Kaspersky documents three variants of increasing sophistication, first found on a system in Afghanistan and subsequently on systems in Egypt and Ethiopia ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)). v1 binds a TCP listener on `127.0.0.1:48739` purely as a single-instance check — if the port is already bound, the malware assumes another instance is running and exits — and reaches its actual command-and-control over three Azure-hosted HTTPS endpoints, trying each in turn on failure, with every request AES-256-GCM-encrypted ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)); on Windows it persists by cloning `node.exe` into a renamed GUI-subsystem binary and adding an `HKCU\...\Run` registry key that runs it against the dropped script, with Linux and macOS equivalents using a cron `@reboot` entry and a LaunchAgent respectively (T1547.001, T1053.003) ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)). v2 adds sandbox and analyst-detection checks (limited memory, low CPU count, short uptime, analyst-associated usernames or hostnames, known analysis tools) and, before terminating on a positive match, sends benign decoy HEAD requests to major consumer sites to look less suspicious (T1497) ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)); it also implements partial corporate-proxy support — checking proxy environment variables, Windows Internet Settings and PAC configuration, and tunnelling HTTPS C2 through HTTP CONNECT: it first attempts an unauthenticated connection, retries using URL-embedded basic credentials if that fails, and only then delegates NTLM/Negotiate challenges to `curl.exe --proxy-anyauth` ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)); its persistence masquerades as an Intel Driver & Support Assistant component and adds a scheduled task run daily at 10AM (T1053.005) ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)). v3, seen against a target in Ethiopia, grows the command set from 11 to 23: it adds harvesting of account addresses from Outlook OST/PST artifacts (T1114.001), a fake "GitHub Copilot Helper" VS Code extension for persistence that falls back to a current-user Run registry key even when no compatible extension directory exists (T1547.001), and Git post-merge/post-checkout hook injection, scanning up to 20 repositories under common project directories for one to inject into ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)).

**PollCat.** Distributed via the OTP-gated React "CTF" lure, PollCat is obfuscated JavaScript (T1027) that begins C2 registration before the victim completes the fake authentication step ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)). Kaspersky ties PollCat to Mirage Kitten partly through its structural overlap with a backdoor it tracks internally as Retrograde, which overlaps public reporting on the MiniFast family: the two follow a similar C2 handshake flow, share identical beacon timing defaults (120s beacon / 5s jitter / 60s retry) and share several command IDs, and NodeRabbit's own corporate-proxy NTLM/Negotiate delegation mirrors a technique Retrograde/MiniFast implements natively ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)).

**Command and control.** NodeRabbit's C2 requests are JSON objects wrapped in AES-256-GCM encryption (T1573.001); Kaspersky calls the combination of Azure Websites (AS8075, MarkMonitor-registered) and Cloudflare-backed domains for HTTPS C2 (T1071.001) a hallmark of Mirage Kitten's tradecraft observed across both NodeRabbit and PollCat ([Kaspersky Securelist, 2026-09-01](https://securelist.com/mirage-kitten-new-backdoors-noderabbit-pollcat/121244/)); in some cases the victim organization's own name is embedded in the Azure subdomain to blend with legitimate corporate traffic. Confirmed victims sit in fintech, aviation and aerospace organizations in Egypt, Ethiopia and Afghanistan, per both Kaspersky's own research and The Record's independent reporting ([The Record, 2026-09-01](https://therecord.media/iranian-cyber-spies-target-aviation-fintech-new-malware)); this fits Mirage Kitten's established Middle East/Africa targeting footprint. No CVE is involved — this is a social-engineering-plus-supply-chain delivery chain, not an exploited vulnerability.

**Defender takeaway:** the transferable exposure is not regional — any organization that recruits software engineers through take-home coding assessments, including public-sector or e-government development teams, is a plausible target for this delivery pattern. Sandbox or detonate candidate-supplied take-home projects in an isolated, network-egress-controlled environment before any engineer runs them on a corporate endpoint, and treat an instruction not to use AI-assisted code review on a take-home submission as itself a red flag warranting manual security review of the archive.

**Detection concepts.** Lead with the telemetry class: process-creation events showing a Node.js runtime spawned from a freshly extracted archive or IDE "run project" action outside normal package-manager cache paths, followed by outbound HTTPS to `*.azurewebsites.net` or a newly registered domain, is the discriminating sequence. Persistence-artifact hunt: HKCU Run-key entries disguised as update tasks (e.g. naming patterns resembling browser or driver updaters) that execute a renamed Node binary against a `.js` payload; scheduled tasks invoking Node against a script under `%APPDATA%`, `%LOCALAPPDATA%` or `ProgramData`; VS Code extension directories containing an extension absent from the marketplace or lockfile inventory; and unexpected entries in `.git/hooks/post-merge` or `post-checkout` referencing an out-of-repository Node invocation.

**Triage:** legitimate take-home coding assessments are routine in technical hiring, so the assessment itself is not the signal. The discriminators are (a) a hard time limit or single-use access code paired with pressure to run the project immediately, (b) a first-line import of an unfamiliar or unpublished npm package bundled directly in `node_modules` rather than fetched from the registry, and (c) outbound network activity beginning before any of the project's advertised functionality has been exercised.

**Hardening:** for hiring workflows, run candidate submissions in disposable, network-egress-restricted sandboxes and never on a domain-joined workstation; for engineering teams generally, an EDR or application-control policy that flags Node processes launched from outside a version-controlled or package-manager-managed directory tree catches this delivery pattern independent of any specific package name.
