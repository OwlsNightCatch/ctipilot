---
schema: 1
kind: threat
horizon: operational
title: "UPDATE — Project CAV3RN now decides per transaction whether to talk directly or relay through Google Apps Script, and a DNS answer's fourth octet is what makes the choice"
headline: "Kaspersky documents a C2 module that queries DNS before every transaction to pick its channel, and a broker DLL that hot-loads components every second"
summary: >
  Kaspersky GReAT published a further instalment on Project CAV3RN, the modular espionage framework
  it tracks against targets in Israel, on 2026-08-11. The new component is a .NET NativeAOT
  communication module that performs a DNS A-record lookup before every poll or result submission and
  reads the fourth octet of the answer to choose between direct HTTPS and a Google Apps Script relay,
  with the same DNS infrastructure able to hand back a replacement Apps Script deployment ID so the
  operator can rotate the Google channel without redeploying. A second new component, a broker DLL
  masquerading as the RNP OpenPGP library, rescans its directory every second and hot-loads
  higher-versioned components.
discovered_at: "2026-08-12T04:51:00Z"
event_date: "2026-08-11"
run_id: 2026-08-12T0411Z-intel
priority: notable
immediate_action: null
tags: [espionage, nation-state, cloud]
regions: [middle-east, global]
sectors: [technology]
entities:
  - tool:cavern-c2-framework
techniques: [T1071.004, T1102.002, T1568, T1036.005, T1105, T1027]
affected_products: []
cves: []
sources:
  - url: "https://securelist.com/project-cav3rn-continues/120991/"
    publisher: "Kaspersky Securelist (GReAT)"
    date: "2026-08-11"
    role: primary
closed_sources: []
evidence:
  - quote: "Project CAV3RN is a modular espionage framework used against targets in Israel."
    publisher: "Kaspersky Securelist (GReAT)"
  - quote: "The main finding is a complex C2 module that uses DNS A-record responses to choose between direct HTTPS and a Google Apps Script relay for each transaction. The same DNS infrastructure can validate and replace the relay deployment ID, allowing the operator to rotate the Google channel."
    publisher: "Kaspersky Securelist (GReAT)"
verification: single-source
sourcing_note: >
  Kaspersky GReAT is the only party publishing on this framework; no independent second analysis of
  the new components exists. The prior entry recorded Kaspersky's own low-confidence association
  between the Cavern cluster and OilRig — this instalment does not strengthen that association, and
  this entry therefore links only the framework entity and makes no actor claim.
confidence: medium
update_of: 2026-07-22/cavern-cav3rn-oilrig-attribution-dns-aaaa-c2-fallback
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

**UPDATE (originally covered 2026-07-22):** Kaspersky's GReAT team published a further instalment on Project CAV3RN on 2026-08-11, describing it as "a modular espionage framework used against targets in Israel" and expanding on two earlier publications ([Kaspersky Securelist, 2026-08-11](https://securelist.com/project-cav3rn-continues/120991/)). The prior entry here covered the framework's DNS-based C2 fallback and Kaspersky's low-confidence association with OilRig. The delta is a channel-selection design that is worth carrying into detection engineering regardless of who operates it.

Kaspersky states: "The main finding is a complex C2 module that uses DNS A-record responses to choose between direct HTTPS and a Google Apps Script relay for each transaction. The same DNS infrastructure can validate and replace the relay deployment ID, allowing the operator to rotate the Google channel" ([Kaspersky Securelist, 2026-08-11](https://securelist.com/project-cav3rn-continues/120991/)). The mechanics are specific enough to hunt on. The communication module is a 64-bit DLL compiled with .NET 8 NativeAOT. Before polling for commands or sending a result, it issues an A-record query for a name built from a short random nonce concatenated with a numeric error state, then a hex-encoded client identifier, under a fixed operator-controlled domain. One exact address is treated as a rejection; otherwise the module reads the fourth octet of the answer and maps it, in combination with the current error state, onto direct HTTPS, the Apps Script relay, an exception, or closing the transaction with no channel at all. A recovered Apps Script deployment ID is written back to the module's on-disk configuration, while other configuration changes pushed by the operator stay in memory. The two channels differ in shape as well as destination. On the direct-HTTPS path the module contacts a configured attacker-controlled address whose endpoint is gated on a custom client-identifier HTTP header, returning a failure response to requests without it and an encoded tasking body to requests carrying it. On the Apps Script path the module instead POSTs a JSON envelope to the deployment URL, with the upstream method and the headers to replay — the same client-identifier value among them — carried as fields inside that JSON body rather than as headers on the request to Google. Tasking comes back base64-encoded and XORed either way.

The second new component is an inter-component broker, a 64-bit Visual C++ DLL that masquerades as the RNP OpenPGP library through a set of `rnp_*` exports, with one of those exports starting the broker. At startup it creates its control structure, initialises a message dispatcher and scans the host directory for DLLs, grouping candidates by their `CompanyName` resource and loading the highest-versioned member of each group that exposes four specific named exports. It rescans that directory every second, so a component can be added or upgraded without restarting the host — but only by dropping a higher-versioned DLL under a new path, because replacing a file in place is not detected ([Kaspersky Securelist, 2026-08-11](https://securelist.com/project-cav3rn-continues/120991/)).

**Defender takeaway:** the evasion here is aimed squarely at controls that key on destination reputation. `script.google.com` is legitimate Google infrastructure that virtually every enterprise egress policy permits, and the direct-HTTPS alternative means blocking it does not sever the channel — the module simply routes the next transaction the other way. The observable that survives both branches is the DNS behaviour upstream of the choice: a host issuing repeated A-record queries for long, high-entropy subdomain labels under one external domain, immediately before each outbound session, and with the answers' fourth octet varying across a small set of values. That is a passive-DNS and resolver-log correlation problem, not a web-proxy one, and it is the one place where the per-transaction channel selection is unavoidably visible.

**Triage:** high-volume DNS lookups under a single parent domain are also how legitimate telemetry agents, CDN clients and some licence checks behave, so the query volume alone is not the signal. The discriminators the described mechanism supports are the label structure — a short changing nonce plus a stable hex-encoded identifier per host, rather than a service-shaped name — and the tight temporal coupling, with one lookup preceding each outbound connection rather than a periodic refresh independent of traffic. Note what is *not* available as a discriminator on the relay path: the custom client-identifier travels inside the JSON body of a TLS POST to a legitimate Google endpoint, so it is not visible to header inspection or to anything short of TLS interception at the proxy.
