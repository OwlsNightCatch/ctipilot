---
schema: 1
kind: annual-report
horizon: operational
title: "Talos IR Trends Q2 2026: ransomware operators ran their command-and-control through legitimate RMM agents, authentication abuse hit two-thirds of engagements, and missing logs stopped root-cause determination outright"
headline: "Cisco Talos IR's quarterly report puts three named intrusion chains on record, led by Sinobi running its command-and-control through a trojanized MeshAgent"
summary: >
  Cisco Talos Incident Response published its Q2 2026 quarterly report on 2026-07-28. Three named chains
  carry the operational value: Sinobi ransomware, in Talos IR's first engagement with the group, used a
  trojanized MeshAgent binary installed as a SYSTEM auto-start service for encrypted-WebSocket C2, held
  access for about three days, cracked a weak service-account password from ntds.dit, moved by RDP and
  WinRM, and deployed ransomware across the entire domain through a malicious GPO logon script with
  rclone staging exfiltration; Warlock (Storm-2603) was seen deploying the Zoho Assist Unattended Agent,
  a tool Talos had not previously attributed to it; and UAT-11764 runs a QR-code-in-PDF phishing operation
  that propagates through each compromised mailbox's own contact list. Two findings cut across all of it —
  authentication abuse appeared in 65% of engagements, and in several cases logging gaps prevented Talos
  from determining the initial access vector or the scope of exfiltration at all.
discovered_at: "2026-07-29T05:55:00Z"
event_date: "2026-07-28"
run_id: 2026-07-29T0408Z-intel
priority: notable
immediate_action: null
tags: [ransomware, phishing, identity, supply-chain, organized-crime]
regions: [global]
sectors: [healthcare, public-sector, manufacturing]
entities: [report:talos-ir-trends-q2-2026, actor:sinobi-ransomware, actor:warlock-storm-2603, actor:uat-11764, tool:talos-artoken-eviltokens-bec-panel]
techniques: [T1566.001, T1598, T1557, T1111, T1621, T1098.005, T1078, T1564.008, T1534, T1102, T1219, T1543.003, T1071.001, T1003.003, T1021.001, T1021.006, T1484.001, T1486, T1567, T1190]
affected_products: ["Microsoft 365", "Microsoft SharePoint", "MeshCentral MeshAgent", "Zoho Assist"]
cves: []
sources:
  - url: "https://blog.talosintelligence.com/ir-trends-q2-2026/"
    publisher: "Cisco Talos Incident Response"
    date: "2026-07-28"
    role: primary
closed_sources: []
evidence:
  - quote: "Notably, we observed the threat actors use a trojanized MeshAgent binary as their primary C2 mechanism during this engagement, a tactic that has not been previously associated with the group in public reporting."
    publisher: "Cisco Talos Incident Response"
  - quote: "The actor ultimately deployed the ransomware across the entire domain using a malicious Group Policy Object (GPO) logon script. The incident resulted in the encryption of systems with the .SINOBI file extension, alongside observed data exfiltration staging activity conducted via rclone.exe."
    publisher: "Cisco Talos Incident Response"
  - quote: "In one engagement, we observed Warlock ransomware operators (also known as Storm-2603) deploying an installer for the RMM tool Zoho Assist Unattended Agent, which is designed to allow administrative remote control of an endpoint without a user logged in."
    publisher: "Cisco Talos Incident Response"
  - quote: "We assess with high confidence that the threat actor, who we have dubbed UAT-11764, will almost certainly continue leveraging this QR code phishing operation, using each newly compromised mailbox's contact lists to expand its reach and sustain the campaign's momentum."
    publisher: "Cisco Talos Incident Response"
  - quote: "In several engagements these gaps prevented definitive determination of the initial access vector or the scope of data exfiltration."
    publisher: "Cisco Talos Incident Response"
verification: single-source
sourcing_note: >
  Single-source by nature: a vendor's report on its own incident-response case load, which no second party
  can corroborate. That shapes how the numbers are used here. Every percentage in the report is a share of
  Talos IR's own engagements this quarter, not a measurement of the threat landscape, and Talos does not
  state its total engagement count — so a shift from 35% to 65% may rest on a modest base. The shares are
  therefore reported as the composition of Talos's case load and never as base rates for anyone else's
  risk, and the report's quarter-over-quarter comparisons are not treated as findings in their own right.
  The concrete engagement facts — the roughly three-day Sinobi dwell time, the single mailbox that sent
  over 6,600 messages, the 80-plus API endpoints on the ARToken panel — are specific observations and are
  used as such. Several ATT&CK ids in the mapping are absent from Talos's own summary table but describe
  behaviours the report states in prose and this entry's body sets out — Windows Service persistence and
  NTDS credential dumping for the Sinobi chain, and Windows Remote Management, adversary-in-the-middle and
  device registration for the lateral-movement and authentication-abuse findings. They are included because
  the mapping surface is meant to be complete over what the source supports, not over what it tabulates. Talos's reference to its own log-assessment
  service is a vendor offering, not a defender-neutral recommendation, and is omitted.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: annual-report
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Cross-check your asset inventory for MeshCentral MeshAgent and Zoho Assist Unattended Agent instances that your own management platform did not provision, treating any such agent running as a SYSTEM auto-start service as an incident rather than a hygiene finding — both were the primary command-and-control mechanism in the ransomware engagements Talos describes."
  - "Raise domain-controller security-log retention and forward it off-device: Talos found DC logs retained for only a few hours, and states the resulting gaps prevented determining the initial access vector or exfiltration scope in real engagements — 90 days of centralised retention is the figure it names."
migrated_from: null
---

Quarterly incident-response reports are usually read for their percentages, which is the least useful thing in them. The Q2 2026 edition from Cisco Talos Incident Response is worth a deep read for a different reason: it puts three specific intrusion chains on the public record with enough sequence to hunt against, and it documents a visibility failure that stopped Talos's own responders from answering the two questions every incident turns on ([Cisco Talos Incident Response, 2026-07-28](https://blog.talosintelligence.com/ir-trends-q2-2026/)).

**Sinobi: the RMM agent *was* the C2.** Talos IR responded to Sinobi ransomware for the first time in April 2026 — a ransomware-as-a-service operation active nearly a year with minimal public reporting on its operators. The chain reads as a deliberate exercise in staying inside the shape of normal administration. Rather than deploying a bespoke implant, the operators used a trojanized MeshAgent binary — the agent component of the open-source MeshCentral remote-management platform — as their primary command-and-control mechanism, a tactic Talos states had not previously been associated with the group ([Cisco Talos Incident Response, 2026-07-28](https://blog.talosintelligence.com/ir-trends-q2-2026/)). Installing it as a SYSTEM-level auto-start service collapsed persistence and privilege into the same step: no separate escalation, and boot survival from the outset. The channel was encrypted WebSocket to an attacker-controlled server, which matters because genuine MeshAgent traffic is itself WebSocket-based — Talos's assessment is that this let the actor blend malicious traffic with legitimate remote-management activity and hold undetected access for approximately three days before deploying ransomware ([Cisco Talos Incident Response, 2026-07-28](https://blog.talosintelligence.com/ir-trends-q2-2026/)). Lateral movement was enabled by a service account whose weak password was cracked after being obtained from the domain credential store `ntds.dit`, and the operators moved through the network over RDP and WinRM. The endgame is the part worth dwelling on: rather than pushing the payload host by host, the actor deployed ransomware across the entire domain using a malicious Group Policy Object logon script, encrypting with the `.SINOBI` extension alongside exfiltration staging via `rclone.exe` ([Cisco Talos Incident Response, 2026-07-28](https://blog.talosintelligence.com/ir-trends-q2-2026/)). Talos reads the GPO deployment as evidence of genuine enterprise-architecture understanding, and expects the group to keep weaponising legitimate tools precisely because they bypass signature-based alerting.

**Warlock and the unattended agent.** In a separate engagement, Talos observed Warlock operators — also tracked as Storm-2603 — deploying an installer for the Zoho Assist Unattended Agent, a capability designed to allow administrative remote control of an endpoint with no user logged in, and states it had not previously seen this tool attributed to Warlock ([Cisco Talos Incident Response, 2026-07-28](https://blog.talosintelligence.com/ir-trends-q2-2026/)). That engagement did not reach encryption, but Talos notes the activity was consistent with a Warlock attack it observed in May 2026 that did. The pattern across both ransomware cases is the same substitution: where a defender's model expects a malicious binary, there is a legitimate, signed, commercially supported remote-administration product instead — which is why Talos's own recommendation shifts from signature detection to behavioural monitoring and application allowlisting that prevents unauthorised binaries from running as services.

**UAT-11764: phishing that grows its own target list.** From April 2026 and still ongoing in late June, Talos tracked a QR-code phishing campaign against primarily Australian organisations, attributing it to a newly designated actor. Delivery is auto-generated, victim-tailored PDF documents carrying embedded QR codes — a shape chosen to sit outside what email-gateway text and link scanning inspects. The codes lead to Microsoft 365 credential-harvesting pages; on success the operator accesses the mailbox, creates inbox rules to hide incoming mail and reduce the victim's visibility of the compromise, stages follow-on malicious documents on SharePoint, and then sends further internal and external phishing using that mailbox's own contact list ([Cisco Talos Incident Response, 2026-07-28](https://blog.talosintelligence.com/ir-trends-q2-2026/)). Talos assesses with high confidence that the actor will almost certainly continue, using each newly compromised mailbox's contacts to expand reach and sustain momentum ([Cisco Talos Incident Response, 2026-07-28](https://blog.talosintelligence.com/ir-trends-q2-2026/)). The tradecraft insight Talos draws is that the operation leans on trusted infrastructure — SharePoint and Microsoft 365 — rather than attacker-registered domains, so reputation-based controls have nothing to fire on. The same report profiles ARToken, the phishing-as-a-service panel this pipeline already tracks, noting it exposes over 80 API endpoints covering device-code phishing, primary-refresh-token persistence, mailbox access and SharePoint exfiltration, and bypasses multi-factor authentication through the OAuth device-authorisation flow rather than by stealing a password.

**The two cross-cutting findings.** Authentication abuse was the most prevalent weakness Talos recorded, in 65% of its engagements against 35% the previous quarter — and the composition is more useful than the share: adversaries defeated or bypassed multi-factor authentication using adversary-in-the-middle proxies and session-token theft, MFA-fatigue attacks, registration of attacker-controlled devices for authentication, and legacy authentication protocols that circumvent MFA altogether ([Cisco Talos Incident Response, 2026-07-28](https://blog.talosintelligence.com/ir-trends-q2-2026/)). Three of those four defeat a correctly configured push-based MFA deployment, which is the deployment most organisations have. The second finding is the one to take to a budget conversation. Insufficient logging and visibility appeared in 42% of engagements against 18% the previous quarter, and Talos enumerates what that meant in practice: domain-controller security logs retained for only a few hours, host event logs truncated or overwritten before capture, absent NetFlow preventing reconstruction of external authentication and exfiltration, on-device-only logs that adversaries deleted, and cloud telemetry whose retention did not reach back to the true initial-access date. Talos states plainly that in several engagements these gaps prevented definitive determination of the initial access vector or the scope of data exfiltration ([Cisco Talos Incident Response, 2026-07-28](https://blog.talosintelligence.com/ir-trends-q2-2026/)). That is not a hygiene observation — it is a statement that the questions a board, a regulator and a data-protection authority all ask first were unanswerable. Talos's remediation names 90 days of centralised retention as a minimum, logs forwarded off-device so they survive tampering and rebuilds, and process-creation, command-line and cloud-API auditing enabled.

Also recorded: exposed or unpatched internet-facing infrastructure was the third-ranked weakness at 31%, with ToolShell, an older Telerik UI deserialization flaw and SD-WAN/VPN appliance CVEs among the named examples; and unlimited outbound email thresholds enabled propagation in almost 15% of engagements, illustrated by a single compromised mailbox that sent over 6,600 phishing and spam messages before containment — a concrete number worth borrowing as an alerting threshold, since Talos rightly calls outbound rate-limiting low-effort and high-impact. On targeting, healthcare led for the second consecutive quarter at 17% of engagements, with public administration and manufacturing at 14% each; Talos's read is that the three share a critical lack of downtime tolerance, and it notes that almost all targeted public-administration organisations were **local governments** and that targeted manufacturers were high-value industrial-supply-chain entities where disruption cascades downstream. For a constituency built around cantonal and communal administration and critical-infrastructure operators, that is the sentence in the report with the most direct read-across — the segment being hit is not central government but the municipal tier, and the reason given is operational intolerance of downtime rather than data value.

**Defender takeaway:** the through-line across all three chains is that the adversary's tooling was legitimate, licensed, and already trusted — MeshAgent, Zoho Assist, RDP, WinRM, Group Policy, SharePoint, Microsoft 365 — which makes an RMM inventory a security control rather than an IT-asset exercise. Two questions are answerable this week and would have changed the outcome in Talos's cases: which remote-management agents are installed across the estate and which of them your own management platform actually provisioned, and whether your domain-controller logs still exist far enough back to reconstruct an intrusion that began three days before you noticed. The authentication-abuse composition adds a third: because attacker device registration and legacy authentication protocols both route around push-based MFA entirely, restricting self-service MFA enrolment and blocking legacy authentication are the controls that address what Talos actually observed, whereas re-tuning push prompts addresses only the fatigue variant.

**Triage:** every mechanism in the ransomware chains is normal administration, and Talos's explicit position is that this is why they were chosen — so no single event discriminates and the correlation has to carry it. For remote-management agents the discriminator is provenance against inventory: a genuine MeshAgent or Zoho Assist deployment is provisioned by your own management server onto an asset of record and appears as an expected service, whereas the malicious instance is an agent-named SYSTEM service on a host with no deployment of record. For the lateral movement, the discriminator is the identity rather than the protocol: RDP and WinRM between servers is routine, but a *service* account interactively authenticating across hosts is not what service accounts are for, and that is the question an access review can settle in advance. For the GPO step, the discriminator is change provenance — a logon-script modification is a discrete, auditable act with an expected author and change window, so an unattributed edit to a domain-wide policy object is high-fidelity on its own.
