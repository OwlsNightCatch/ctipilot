---
schema: 1
kind: threat
horizon: operational
title: "HOLLOWGRAPH: a Cavern-framework backdoor that turns a compromised Microsoft 365 calendar into a Graph-API dead-drop C2"
headline: "Group-IB details HOLLOWGRAPH — a .NET implant using a victim's own M365 calendar as two-way C2 over the Graph API, with DNS-tunneled Entra credential refresh"
summary: >
  Group-IB documented (2026-07-20) HOLLOWGRAPH, a NativeAOT .NET backdoor it links with high confidence
  to the Cavern C2 framework (previously tied to the Iran-nexus Cavern Manticore actor). HOLLOWGRAPH
  never contacts attacker infrastructure directly: it uses the Microsoft Graph API to plant and read
  tasking as attachments on far-future calendar events in a compromised M365 mailbox, and tunnels Entra
  ID credential refresh over IPv6 DNS. Current victimology is narrow (Israeli organisations), but the
  Graph-API-calendar-as-C2 technique is directly transferable to any Microsoft 365 tenant — the platform
  at the centre of most CH/EU public-sector estates.
discovered_at: "2026-07-21T04:43:00Z"
event_date: "2026-07-20"
run_id: 2026-07-21T0409Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, iran-nexus, identity, cloud]
regions: [global, middle-east]
sectors: [public-sector, technology]
entities: [tool:hollowgraph-malware, tool:cavern-c2-framework]
techniques: [T1102.002, T1071.004, T1573, T1027, T1078.004]
affected_products: ["Microsoft 365", "Microsoft Graph API", "Microsoft Entra ID"]
cves: []
sources:
  - url: "https://www.group-ib.com/blog/hollowgraph-microsoft-365/"
    publisher: "Group-IB Threat Intelligence"
    date: "2026-07-20"
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/hollowgraph-microsoft-calendars/"
    publisher: "Infosecurity Magazine"
    date: "2026-07-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Group-IB Threat Intelligence team has identified HOLLOWGRAPH, a new malware sample that we attribute, with high confidence, to the Cavern backdoor framework"
    publisher: "Group-IB Threat Intelligence"
  - quote: "we cannot confidently attribute this activity to any previously identified threat actor."
    publisher: "Group-IB Threat Intelligence"
verification: multi-source
sourcing_note: "Group-IB is the single origin for the malware analysis; Infosecurity Magazine relays it. The Cavern-framework link is Group-IB's high-confidence assessment; the Lyceum/OilRig actor overlap is stated at low confidence and is not framed here as attribution."
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: identity-infra
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Group-IB has published a technical profile of HOLLOWGRAPH, a NativeAOT-compiled .NET DLL it "attribute[s], with high confidence, to the Cavern backdoor framework" ([Group-IB, 2026-07-20](https://www.group-ib.com/blog/hollowgraph-microsoft-365/)) — the modular C2 that Check Point Research previously tied to the Iran-MOIS-linked Cavern Manticore actor and that this pipeline has tracked since 2026-07-09. The interest for defenders is not the actor but the command-and-control design, which is built entirely on trusted Microsoft cloud services and leaves almost no attacker-owned network footprint. Infosecurity Magazine corroborates the reporting ([Infosecurity Magazine, 2026-07-20](https://www.infosecurity-magazine.com/news/hollowgraph-microsoft-calendars/)).

HOLLOWGRAPH implements only two operations, `get` and `send`, and never beacons to attacker infrastructure. Instead it treats a compromised Microsoft 365 mailbox's calendar as a two-way dead-drop over the Graph API. To exfiltrate, the implant encrypts a file with hybrid RSA-OAEP + AES-256-GCM (separate key pairs per direction), creates a calendar event dated far in the future — 2050-05-13, in a fixed 22:00–23:00 UTC window — so the mailbox owner is unlikely to notice, uploads the ciphertext as event attachments, and renames the event subject to an operator-recognisable tag. To receive tasking, it queries the same `calendarView` window, filters events by subject, downloads the attachment planted by the operator, and decrypts it. A separate, unencrypted channel refreshes the four Entra ID (Azure AD) values the implant needs — tenant ID, client ID, client secret and target mailbox — by DNS tunneling: length- and data-encoded queries against an attacker domain resolved as IPv6 AAAA records and reassembled into fixed-size chunks.

The kill chain, described for reasoning about detection: the implant authenticates as an application/service identity to Microsoft Graph and drives calendar operations programmatically — the Graph-API calendar dead-drop is bidirectional web-service command-and-control and the credential refresh rides DNS as an application-layer channel; the calendar payloads are encrypted end-to-end; and the implant operates against cloud-account credentials rather than an on-host identity. Group-IB is explicit about the attribution ceiling: it "cannot confidently attribute this activity to any previously identified threat actor," assessing only a low-confidence technical overlap with the Iranian-nexus Lyceum sub-group — so this is a Cavern-framework component, not a confirmed named-actor campaign. Telemetry to date is narrow: 12 infected systems, roughly 3 actively communicating, all evidence pointing to Israeli organisations, with activity observed between 3 June and 9 July 2026.

**Defender takeaway:** the technique defeats controls that assume C2 means outbound traffic to novel or attacker-owned infrastructure — here every exfiltration and tasking hop is Graph API traffic to Microsoft, and credential refresh rides ordinary DNS. Detection has to move to the identity and audit plane. In Microsoft 365 mailbox-audit and Graph API activity, hunt for calendar-event creation, attachment upload and subject-rename performed by an application or service-principal identity rather than the interactive mailbox owner, and treat calendar events scheduled implausibly far in the future (e.g. year 2050) with attachments as a high-signal anomaly. In DNS telemetry, surface high-volume IPv6 AAAA-record lookups to a single external domain from hosts that have no reason to generate them. **Triage:** legitimate automation and mailbox add-ins also act on calendars via Graph service principals — the discriminators are the anomalous far-future event date, attachments on those events, subject strings matching a fixed tag or GUID-only pattern, and the pairing of Graph calendar writes with a matching AAAA-tunnel DNS pattern from the same host; any one is weak, the combination is the signal. Hardening centres on constraining which application identities can read/write mailbox calendar items and reviewing consented Graph application permissions (`Calendars.ReadWrite`, mail scopes) for service principals that do not need them.
