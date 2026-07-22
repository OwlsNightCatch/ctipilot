---
schema: 1
kind: threat
horizon: operational
title: "Kaspersky corroborates the Cavern/HOLLOWGRAPH cluster, associates it (low confidence) with OilRig (APT34), and details a DNS AAAA-record C2 config-recovery fallback"
headline: "A second vendor links the Outlook-calendar Graph C2 framework to OilRig (low confidence) and documents a DNS AAAA fallback that restores its cloud C2"
summary: >
  Kaspersky GReAT published independent analysis of a new communication module in the Cavern C2 framework —
  the Iran-linked toolset Check Point tracks as "Cavern Manticore" and Group-IB documented as HOLLOWGRAPH —
  and retains a low-confidence assessment associating it with OilRig (APT34). The genuinely new element is a
  resilience layer: when Microsoft Graph authentication or tenant validation fails, the module recovers
  replacement connection settings (TenantId, ClientId, ClientSecret, UserEmail) via DNS AAAA responses from
  attacker nameservers. This corroborates the cluster covered on 2026-07-21 and adds the DNS fallback
  mechanics plus additional (still low-confidence) evidence for the OilRig link.
discovered_at: "2026-07-22T04:34:31Z"
event_date: "2026-07-21"
run_id: 2026-07-22T0409Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, cloud, identity]
regions: [middle-east, global]
sectors: [public-sector, technology]
entities: [tool:cavern-c2-framework, tool:hollowgraph-malware, actor:cavern-manticore, actor:oilrig]
techniques: [T1102.002, T1071.004, T1008, T1573]
affected_products: ["Microsoft 365", "Microsoft Graph", "Microsoft Outlook"]
cves: []
sources:
  - url: "https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/"
    publisher: "Kaspersky (Securelist / GReAT)"
    date: "2026-07-21"
    role: primary
  - url: "https://research.checkpoint.com/2026/cavern-manticore-exposing-iran-linked-modular-c2-framework/"
    publisher: "Check Point Research"
    date: "2026-07-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "If Microsoft Graph authentication or tenant validation fails, the module attempts to retrieve replacement connection settings through DNS AAAA responses."
    publisher: "Kaspersky (Securelist / GReAT)"
  - quote: "The new module shares several behavioral patterns with previously reported OilRig tooling, including the use of Microsoft-hosted services, attachment-based command exchange, and a secondary mechanism for restoring access to a cloud C2 channel."
    publisher: "Kaspersky (Securelist / GReAT)"
verification: multi-source
sourcing_note: "The framework and its Graph-calendar C2 are multi-source (Kaspersky GReAT, Check Point Research, and the previously-covered Group-IB HOLLOWGRAPH reporting). The OilRig/APT34 link is Kaspersky's own low-confidence assessment — first made in a prior report and now, per Kaspersky, supported by additional evidence from the new module, but with no direct code reuse or infrastructure overlap identified — so it is reported as a low-confidence association, not an attribution, and credibility is held at 2. DNS AAAA config-recovery mechanics are Kaspersky's."
confidence: medium
update_of: 2026-07-21/hollowgraph-m365-calendar-graph-api-c2-cavern
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

**UPDATE (originally covered 2026-07-21):** The HOLLOWGRAPH entry documented an Iran-linked backdoor that used Microsoft Graph and far-future Outlook calendar events as its command-and-control channel. Kaspersky GReAT has now published independent analysis of the same toolset — which Check Point tracks as "Cavern Manticore" — detailing a new communication module (`AzureCommunication.dll`) that replaces the earlier HTTP/WebSocket component with Microsoft Graph, exchanging RSA-OAEP-SHA256 + AES-256-GCM-encrypted commands and results as attachments inside far-future Outlook calendar events (a fixed 2050-05-13 window) keyed to a controller-generated agent ID ([Kaspersky, 2026-07-21](https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/); [Check Point Research, 2026-07-06](https://research.checkpoint.com/2026/cavern-manticore-exposing-iran-linked-modular-c2-framework/)).

The new element beyond prior reporting is a **resilience layer**: when Graph authentication or tenant validation fails, the module recovers replacement connection settings (TenantId, ClientId, ClientSecret, UserEmail) via DNS AAAA responses from attacker-controlled nameservers, encoding length markers and 14-byte chunks in specially formatted subdomains. On attribution, Kaspersky **retains its low-confidence assessment that Project CAV3RN is associated with OilRig (APT34)** — a link it first drew in a previous report — noting the new module shares behavioural patterns with previously reported OilRig tooling (Microsoft-hosted-service C2, attachment-based command exchange, a secondary cloud-C2 recovery mechanism) while explicitly identifying **no direct code reuse or infrastructure overlap** ([Kaspersky, 2026-07-21](https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/)). Treat the OilRig association as an analytic lead, not a settled attribution.

**Defender takeaway:** the delta for hunters is the fallback channel. Add to the existing HOLLOWGRAPH hunt — Outlook/M365 calendar events with far-future dates carrying binary attachments, and Graph API access from non-interactive service principals — a watch for **outbound DNS AAAA queries to newly-registered domains whose IPv6 responses are used as an encoding channel rather than for routing** (abnormally structured subdomains, AAAA answers that never drive a subsequent connection to the returned address). The DNS fallback means blocking or revoking the Graph app registration alone will not sever C2 if the endpoint can still resolve the actor's nameservers. **Triage:** legitimate applications query AAAA records constantly — the discriminator is an AAAA lookup to a rarely-seen or newly-registered domain whose returned IPv6 address is never subsequently contacted, appearing in sequence after a failed Graph/OAuth authentication from the same host.
