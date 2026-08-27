---
schema: 1
kind: threat
horizon: operational
title: >
  HOLLOWGRAPH: a Cavern-framework backdoor that turns a compromised Microsoft 365 calendar into a
  Graph-API dead-drop C2
headline: >
  Group-IB details HOLLOWGRAPH — a .NET implant using a victim's own M365 calendar as two-way C2
  over the Graph API, with DNS-tunneled Entra credential refresh
summary: >
  Group-IB documented (2026-07-20) HOLLOWGRAPH, a NativeAOT .NET backdoor it links with high
  confidence to the Cavern C2 framework (previously tied to the Iran-nexus Cavern Manticore
  actor). HOLLOWGRAPH never contacts attacker infrastructure directly: it uses the Microsoft Graph
  API to plant and read tasking as attachments on far-future calendar events in a compromised M365
  mailbox, and tunnels Entra ID credential refresh over IPv6 DNS. Current victimology is narrow
  (Israeli organisations), but the Graph-API-calendar-as-C2 technique is directly transferable to
  any Microsoft 365 tenant — the platform at the centre of most CH/EU public-sector estates.
discovered_at: "2026-07-21T04:43:00Z"
updated_at: "2026-08-12T04:51:00Z"
event_date: 2026-07-20
run_id: 2026-07-21T0409Z-intel
priority: notable
immediate_action: null
tags:
  - espionage
  - nation-state
  - iran-nexus
  - identity
  - cloud
regions:
  - global
  - middle-east
sectors:
  - public-sector
  - technology
entities:
  - "tool:hollowgraph-malware"
  - "tool:cavern-c2-framework"
  - "actor:cavern-manticore"
  - "actor:oilrig"
techniques:
  - T1102.002
  - T1071.004
  - T1573
  - T1027
  - T1078.004
  - T1008
  - T1568
  - T1036.005
  - T1105
affected_products:
  - Microsoft 365
  - Microsoft Graph API
  - Microsoft Entra ID
  - Microsoft Graph
  - Microsoft Outlook
cves: []
sources:
  - url: "https://www.group-ib.com/blog/hollowgraph-microsoft-365/"
    publisher: Group-IB Threat Intelligence
    date: 2026-07-20
    role: primary
  - url: "https://www.infosecurity-magazine.com/news/hollowgraph-microsoft-calendars/"
    publisher: Infosecurity Magazine
    date: 2026-07-20
    role: corroborating
  - url: "https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/"
    publisher: Kaspersky (Securelist / GReAT)
    date: 2026-07-21
    role: primary
  - url: "https://research.checkpoint.com/2026/cavern-manticore-exposing-iran-linked-modular-c2-framework/"
    publisher: Check Point Research
    date: 2026-07-06
    role: corroborating
  - url: "https://securelist.com/project-cav3rn-continues/120991/"
    publisher: Kaspersky Securelist (GReAT)
    date: 2026-08-11
    role: primary
closed_sources: []
evidence:
  - quote: "Group-IB Threat Intelligence team has identified HOLLOWGRAPH, a new malware sample that we attribute, with high confidence, to the Cavern backdoor framework"
    publisher: Group-IB Threat Intelligence
  - quote: we cannot confidently attribute this activity to any previously identified threat actor.
    publisher: Group-IB Threat Intelligence
  - quote: "If Microsoft Graph authentication or tenant validation fails, the module attempts to retrieve replacement connection settings through DNS AAAA responses."
    publisher: Kaspersky (Securelist / GReAT)
  - quote: "The new module shares several behavioral patterns with previously reported OilRig tooling, including the use of Microsoft-hosted services, attachment-based command exchange, and a secondary mechanism for restoring access to a cloud C2 channel."
    publisher: Kaspersky (Securelist / GReAT)
  - quote: Project CAV3RN is a modular espionage framework used against targets in Israel.
    publisher: Kaspersky Securelist (GReAT)
  - quote: "The main finding is a complex C2 module that uses DNS A-record responses to choose between direct HTTPS and a Google Apps Script relay for each transaction. The same DNS infrastructure can validate and replace the relay deployment ID, allowing the operator to rotate the Google channel."
    publisher: Kaspersky Securelist (GReAT)
verification: multi-source
sourcing_note: >
  Group-IB is the single origin for the malware analysis; Infosecurity Magazine relays it. The
  Cavern-framework link is Group-IB's high-confidence assessment; the Lyceum/OilRig actor overlap
  is stated at low confidence and is not framed here as attribution.
confidence: high
references: []
weekly_section: null
deep_dive: true
deep_dive_category: identity-infra
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-07-22T04:34:31Z"
    run_id: 2026-07-22T0409Z-intel
    type: update
    summary: >
      Kaspersky GReAT published independent analysis of a new communication module in the Cavern C2
      framework — the Iran-linked toolset Check Point tracks as "Cavern Manticore" and Group-IB
      documented as HOLLOWGRAPH — and retains a low-confidence assessment associating it with OilRig
      (APT34). The genuinely new element is a resilience layer: when Microsoft Graph authentication or
      tenant validation fails, the module recovers replacement connection settings (TenantId,
      ClientId, ClientSecret, UserEmail) via DNS AAAA responses from attacker nameservers. This
      corroborates the cluster covered on 2026-07-21 and adds the DNS fallback mechanics plus
      additional (still low-confidence) evidence for the OilRig link.
    fields:
      - affected_products
      - entities
      - evidence
      - sources
      - techniques
      - body
    merged_from: 2026-07-22/cavern-cav3rn-oilrig-attribution-dns-aaaa-c2-fallback
  - at: "2026-08-12T04:51:00Z"
    run_id: 2026-08-12T0411Z-intel
    type: update
    summary: >
      Kaspersky GReAT published a further instalment on Project CAV3RN, the modular espionage
      framework it tracks against targets in Israel, on 2026-08-11. The new component is a .NET
      NativeAOT communication module that performs a DNS A-record lookup before every poll or result
      submission and reads the fourth octet of the answer to choose between direct HTTPS and a Google
      Apps Script relay, with the same DNS infrastructure able to hand back a replacement Apps Script
      deployment ID so the operator can rotate the Google channel without redeploying. A second new
      component, a broker DLL masquerading as the RNP OpenPGP library, rescans its directory every
      second and hot-loads higher-versioned components.
    fields:
      - evidence
      - sources
      - techniques
      - body
    merged_from: 2026-08-12/project-cav3rn-google-apps-script-c2-relay
migrated_from: null
---

Group-IB has published a technical profile of HOLLOWGRAPH, a NativeAOT-compiled .NET DLL it "attribute[s], with high confidence, to the Cavern backdoor framework" ([Group-IB, 2026-07-20](https://www.group-ib.com/blog/hollowgraph-microsoft-365/)) — the modular C2 that Check Point Research previously tied to the Iran-MOIS-linked Cavern Manticore actor and that this pipeline has tracked since 2026-07-09. The interest for defenders is not the actor but the command-and-control design, which is built entirely on trusted Microsoft cloud services and leaves almost no attacker-owned network footprint. Infosecurity Magazine corroborates the reporting ([Infosecurity Magazine, 2026-07-20](https://www.infosecurity-magazine.com/news/hollowgraph-microsoft-calendars/)).

HOLLOWGRAPH implements only two operations, `get` and `send`, and never beacons to attacker infrastructure. Instead it treats a compromised Microsoft 365 mailbox's calendar as a two-way dead-drop over the Graph API. To exfiltrate, the implant encrypts a file with hybrid RSA-OAEP + AES-256-GCM (separate key pairs per direction), creates a calendar event dated far in the future — 2050-05-13, in a fixed 22:00–23:00 UTC window — so the mailbox owner is unlikely to notice, uploads the ciphertext as event attachments, and renames the event subject to an operator-recognisable tag. To receive tasking, it queries the same `calendarView` window, filters events by subject, downloads the attachment planted by the operator, and decrypts it. A separate, unencrypted channel refreshes the four Entra ID (Azure AD) values the implant needs — tenant ID, client ID, client secret and target mailbox — by DNS tunneling: length- and data-encoded queries against an attacker domain resolved as IPv6 AAAA records and reassembled into fixed-size chunks.

The kill chain, described for reasoning about detection: the implant authenticates as an application/service identity to Microsoft Graph and drives calendar operations programmatically — the Graph-API calendar dead-drop is bidirectional web-service command-and-control and the credential refresh rides DNS as an application-layer channel; the calendar payloads are encrypted end-to-end; and the implant operates against cloud-account credentials rather than an on-host identity. Group-IB is explicit about the attribution ceiling: it "cannot confidently attribute this activity to any previously identified threat actor," assessing only a low-confidence technical overlap with the Iranian-nexus Lyceum sub-group — so this is a Cavern-framework component, not a confirmed named-actor campaign. Telemetry to date is narrow: 12 infected systems, roughly 3 actively communicating, all evidence pointing to Israeli organisations, with activity observed between 3 June and 9 July 2026.

**Defender takeaway:** the technique defeats controls that assume C2 means outbound traffic to novel or attacker-owned infrastructure — here every exfiltration and tasking hop is Graph API traffic to Microsoft, and credential refresh rides ordinary DNS. Detection has to move to the identity and audit plane. In Microsoft 365 mailbox-audit and Graph API activity, hunt for calendar-event creation, attachment upload and subject-rename performed by an application or service-principal identity rather than the interactive mailbox owner, and treat calendar events scheduled implausibly far in the future (e.g. year 2050) with attachments as a high-signal anomaly. In DNS telemetry, surface high-volume IPv6 AAAA-record lookups to a single external domain from hosts that have no reason to generate them. **Triage:** legitimate automation and mailbox add-ins also act on calendars via Graph service principals — the discriminators are the anomalous far-future event date, attachments on those events, subject strings matching a fixed tag or GUID-only pattern, and the pairing of Graph calendar writes with a matching AAAA-tunnel DNS pattern from the same host; any one is weak, the combination is the signal. Hardening centres on constraining which application identities can read/write mailbox calendar items and reviewing consented Graph application permissions (`Calendars.ReadWrite`, mail scopes) for service principals that do not need them.

## Update — 2026-07-22T04:34:31Z

The HOLLOWGRAPH entry documented an Iran-linked backdoor that used Microsoft Graph and far-future Outlook calendar events as its command-and-control channel. Kaspersky GReAT has now published independent analysis of the same toolset — which Check Point tracks as "Cavern Manticore" — detailing a new communication module (`AzureCommunication.dll`) that replaces the earlier HTTP/WebSocket component with Microsoft Graph, exchanging RSA-OAEP-SHA256 + AES-256-GCM-encrypted commands and results as attachments inside far-future Outlook calendar events (a fixed 2050-05-13 window) keyed to a controller-generated agent ID ([Kaspersky, 2026-07-21](https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/); [Check Point Research, 2026-07-06](https://research.checkpoint.com/2026/cavern-manticore-exposing-iran-linked-modular-c2-framework/)).

The new element beyond prior reporting is a **resilience layer**: when Graph authentication or tenant validation fails, the module recovers replacement connection settings (TenantId, ClientId, ClientSecret, UserEmail) via DNS AAAA responses from attacker-controlled nameservers, encoding length markers and 14-byte chunks in specially formatted subdomains. On attribution, Kaspersky **retains its low-confidence assessment that Project CAV3RN is associated with OilRig (APT34)** — a link it first drew in a previous report — noting the new module shares behavioural patterns with previously reported OilRig tooling (Microsoft-hosted-service C2, attachment-based command exchange, a secondary cloud-C2 recovery mechanism) while explicitly identifying **no direct code reuse or infrastructure overlap** ([Kaspersky, 2026-07-21](https://securelist.com/project-cav3rn-cyberespionage-framework-using-outlook-and-dns/120757/)). Treat the OilRig association as an analytic lead, not a settled attribution.

**Defender takeaway:** the delta for hunters is the fallback channel. Add to the existing HOLLOWGRAPH hunt — Outlook/M365 calendar events with far-future dates carrying binary attachments, and Graph API access from non-interactive service principals — a watch for **outbound DNS AAAA queries to newly-registered domains whose IPv6 responses are used as an encoding channel rather than for routing** (abnormally structured subdomains, AAAA answers that never drive a subsequent connection to the returned address). The DNS fallback means blocking or revoking the Graph app registration alone will not sever C2 if the endpoint can still resolve the actor's nameservers. **Triage:** legitimate applications query AAAA records constantly — the discriminator is an AAAA lookup to a rarely-seen or newly-registered domain whose returned IPv6 address is never subsequently contacted, appearing in sequence after a failed Graph/OAuth authentication from the same host.

## Update — 2026-08-12T04:51:00Z

Kaspersky's GReAT team published a further instalment on Project CAV3RN on 2026-08-11, describing it as "a modular espionage framework used against targets in Israel" and expanding on two earlier publications ([Kaspersky Securelist, 2026-08-11](https://securelist.com/project-cav3rn-continues/120991/)). The prior entry here covered the framework's DNS-based C2 fallback and Kaspersky's low-confidence association with OilRig. The delta is a channel-selection design that is worth carrying into detection engineering regardless of who operates it.

Kaspersky states: "The main finding is a complex C2 module that uses DNS A-record responses to choose between direct HTTPS and a Google Apps Script relay for each transaction. The same DNS infrastructure can validate and replace the relay deployment ID, allowing the operator to rotate the Google channel" ([Kaspersky Securelist, 2026-08-11](https://securelist.com/project-cav3rn-continues/120991/)). The mechanics are specific enough to hunt on. The communication module is a 64-bit DLL compiled with .NET 8 NativeAOT. Before polling for commands or sending a result, it issues an A-record query for a name built from a short random nonce concatenated with a numeric error state, then a hex-encoded client identifier, under a fixed operator-controlled domain. One exact address is treated as a rejection; otherwise the module reads the fourth octet of the answer and maps it, in combination with the current error state, onto direct HTTPS, the Apps Script relay, an exception, or closing the transaction with no channel at all. A recovered Apps Script deployment ID is written back to the module's on-disk configuration, while other configuration changes pushed by the operator stay in memory. The two channels differ in shape as well as destination. On the direct-HTTPS path the module contacts a configured attacker-controlled address whose endpoint is gated on a custom client-identifier HTTP header, returning a failure response to requests without it and an encoded tasking body to requests carrying it. On the Apps Script path the module instead POSTs a JSON envelope to the deployment URL, with the upstream method and the headers to replay — the same client-identifier value among them — carried as fields inside that JSON body rather than as headers on the request to Google. Tasking comes back base64-encoded and XORed either way.

The second new component is an inter-component broker, a 64-bit Visual C++ DLL that masquerades as the RNP OpenPGP library through a set of `rnp_*` exports, with one of those exports starting the broker. At startup it creates its control structure, initialises a message dispatcher and scans the host directory for DLLs, grouping candidates by their `CompanyName` resource and loading the highest-versioned member of each group that exposes four specific named exports. It rescans that directory every second, so a component can be added or upgraded without restarting the host — but only by dropping a higher-versioned DLL under a new path, because replacing a file in place is not detected ([Kaspersky Securelist, 2026-08-11](https://securelist.com/project-cav3rn-continues/120991/)).

**Defender takeaway:** the evasion here is aimed squarely at controls that key on destination reputation. `script.google.com` is legitimate Google infrastructure that virtually every enterprise egress policy permits, and the direct-HTTPS alternative means blocking it does not sever the channel — the module simply routes the next transaction the other way. The observable that survives both branches is the DNS behaviour upstream of the choice: a host issuing repeated A-record queries for long, high-entropy subdomain labels under one external domain, immediately before each outbound session, and with the answers' fourth octet varying across a small set of values. That is a passive-DNS and resolver-log correlation problem, not a web-proxy one, and it is the one place where the per-transaction channel selection is unavoidably visible.

**Triage:** high-volume DNS lookups under a single parent domain are also how legitimate telemetry agents, CDN clients and some licence checks behave, so the query volume alone is not the signal. The discriminators the described mechanism supports are the label structure — a short changing nonce plus a stable hex-encoded identifier per host, rather than a service-shaped name — and the tight temporal coupling, with one lookup preceding each outbound connection rather than a periodic refresh independent of traffic. Note what is *not* available as a discriminator on the relay path: the custom client-identifier travels inside the JSON body of a TLS POST to a legitimate Google endpoint, so it is not visible to header inspection or to anything short of TLS interception at the proxy.
