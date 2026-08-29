---
schema: 1
kind: threat
title: "Kaspersky documents living-off-the-land BitLocker extortion across two Latin America incidents; the second self-identifies as 'XEntry Team'"
headline: "BitLocker-for-impact extortion via exposed RDP, MSSQL and RMM/GPO — no encryptor ships, and one crew brands itself 'XEntry Team'"
summary: >
  Kaspersky's GERT team documented two 2026 extortion incidents that abuse native Windows BitLocker for
  encryption-for-impact instead of a bespoke ransomware family: a June case in Colombia entered via
  internet-exposed RDP, and a May case in Mexico entered via a misconfigured Microsoft SQL Server
  (xp_cmdshell) and used legitimate RMM tooling and Group Policy to deploy BitLocker — that second victim's
  screens displayed "Hacked by XEntry Team". Both demanded small ransoms (~USD 3,000) and printed ransom
  notes on office printers; Kaspersky notes ransom-note wording and delivery similarities that may link the
  two but does not confirm a clear connection. Detection must target behaviour, not a malware artefact.
discovered_at: "2026-07-22T04:34:31Z"
event_date: "2026-07-21"
run_id: 2026-07-22T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, organized-crime]
regions: [global, latam]
sectors: [finance]
entities: [actor:xentry-team]
techniques: [T1133, T1505.001, T1505.003, T1219, T1484.001, T1486]
affected_products: ["Microsoft Windows BitLocker", "Microsoft SQL Server", "ManageEngine Endpoint Central", "Tactical RMM"]
cves: []
sources:
  - url: "https://securelist.com/new-extortion-scheme-printers-bitlocker/120718/"
    publisher: "Kaspersky (Securelist / GERT)"
    date: "2026-07-21"
    role: primary
closed_sources: []
evidence:
  - quote: "The attackers exploited an internet-exposed RDP service on a machine connected to an 8 TB storage device containing mission-critical data."
    publisher: "Kaspersky (Securelist / GERT)"
  - quote: "Finally, in mid-May, the attackers managed to execute a Group Policy Object (GPO) used to deploy activation and encryption tasks, as well as other policies responsible for continued deployment of RMM applications via scheduled tasks."
    publisher: "Kaspersky (Securelist / GERT)"
  - quote: "Although the ransom notes do not reveal a clear connection between the actors, certain words used in the messages, as well as the method of delivery and communication, may confirm a link"
    publisher: "Kaspersky (Securelist / GERT)"
verification: single-source
sourcing_note: "Single-source: first-hand Kaspersky GERT incident-response analysis of two 2026 cases (Colombia, June, RDP-based; Mexico, May, MSSQL/RMM/GPO-based). The 'XEntry Team' name is from the Mexico case only ('Hacked by XEntry Team' on-screen); Kaspersky assesses the two cases MAY be linked (ransom-note wording, delivery method) but explicitly states the notes 'do not reveal a clear connection between the actors', so the two are reported as a technique cluster, not a single confirmed crew. Reputable lab, no independent corroboration yet — credibility held at 2. Behavioural, not indicator-driven."
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

Kaspersky's GERT incident-response team documented two 2026 extortion incidents in Latin America that abuse native Windows **BitLocker** for encryption-for-impact rather than deploying a conventional ransomware family — a living-off-the-land model that leaves no bespoke encryptor for signature-based detection ([Kaspersky, 2026-07-21](https://securelist.com/new-extortion-scheme-printers-bitlocker/120718/)). In the first case (Colombia, June), initial access was an internet-exposed RDP service on a host attached to an 8 TB store of mission-critical data; after manipulating credentials the attacker enabled BitLocker on the drive and demanded roughly USD 3,000. In the second case (Mexico, May) — whose victims' screens displayed "Hacked by XEntry Team" — initial access was a misconfigured Microsoft SQL Server whose `xp_cmdshell` extended stored procedure allowed OS command execution; the operators established persistence through legitimate RMM suites (ManageEngine Endpoint Central, Mesh Agent, Tactical RMM) and web shells, then used Group Policy Objects to push BitLocker activation and encryption tasks across domain-joined systems. Both incidents delivered ransom notes through victims' office printers. Kaspersky notes similarities in the ransom-note wording and delivery method that **may** link the two cases but states the notes "do not reveal a clear connection between the actors" — so treat them as a shared technique cluster, with "XEntry Team" naming the Mexico intrusion specifically. Kaspersky places the approach in the ShrinkLocker BitLocker-abuse lineage, driven here by an RDP or MSSQL foothold and, in the branded case, an RMM-and-GPO admin workflow rather than a self-contained binary.

**Defender takeaway:** because every stage uses built-in Windows features and off-the-shelf admin tooling, the detection opportunity is the behavioural sequence, not a hash. Highest-value hunt signals, telemetry-class first: in process-creation telemetry with parent lineage, the MSSQL engine process (`sqlservr.exe`) spawning `cmd.exe`/`powershell.exe` via `xp_cmdshell`; new RMM-agent service installs on hosts that had none; GPO or scheduled-task changes invoking `manage-bde`/BitLocker on machines not previously encrypted; and sudden BitLocker recovery-key rotation. Reduce the entry surface by disabling `xp_cmdshell` on any internet-reachable MSSQL instance and enforcing MFA on RDP. **Triage:** legitimate administrators do enable BitLocker via GPO and run RMM tools — the discriminators are BitLocker activation on hosts that were never in the encryption baseline, recovery-key changes with no change-ticket, and an RMM agent whose install was preceded by `xp_cmdshell` command execution or an anomalous RDP logon; the sequence, not any single event, is the signal.
