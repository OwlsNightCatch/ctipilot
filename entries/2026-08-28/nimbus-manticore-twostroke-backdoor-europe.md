---
schema: 1
kind: threat
horizon: operational
title: "Nimbus Manticore (Iranian IRGC-affiliated APT, aka Tortoiseshell/UNC1549/Smoke Sandstorm/Mirage Kitten) deploys a third 2026 toolset refresh — a TWOSTROKE-like backdoor abusing DLL search-order hijacking, paired with a reverse SSH tunneler — with confirmed expansion into the UK, France, Albania and Belarus"
headline: "An Iranian espionage actor already tracked for aerospace and telecom targeting adds a new backdoor and materially widens its named European footprint"
summary: >
  Group-IB documents new infrastructure and a new toolset for Nimbus Manticore, the Iranian
  IRGC-affiliated actor this store tracks under multiple aliases. A reverse SSH tunneler
  establishes outbound connections over port 443 to give operators interactive access into
  compromised networks; a TWOSTROKE-family C++ backdoor masquerades as the Windows Terminal
  Server SDK DLL for search-order hijacking. Infrastructure analysis indicates targeting expanded
  specifically into the UK, France, Albania and Belarus, alongside continued Middle Eastern
  activity — the third distinct toolset refresh this store has tracked for the actor in roughly
  seven months.
discovered_at: "2026-08-28T06:20:00Z"
updated_at: null
event_date: "2026-08-26"
run_id: 2026-08-28T0409Z-intel
priority: high
immediate_action: null
tags: [nation-state, espionage]
regions: [europe, middle-east, uk]
sectors: [public-sector, telco]
entities: [actor:screening-serpens-unc1549-smoke-sandstorm-nimbus-manticore-iran-apt, tool:twostroke-backdoor, tool:tortoiseshell-ssh-tunneler]
techniques: [T1574.001, T1572, T1090, T1071.001, T1027]
affected_products: ["Microsoft Windows"]
cves: []
sources:
  - url: "https://www.group-ib.com/blog/tortoiseshell-apt-toolset-infrastructure/"
    publisher: "Group-IB"
    date: "2026-08-26"
    role: primary
closed_sources: []
evidence:
  - quote: "Execution of this command establishes an SSH connection to the operator's infrastructure ... on port 443 to set up a reverse tunnel. As a result, traffic sent to [a local port] on the C2 server is redirected back through the tunnel directly into the compromised network."
    publisher: "Group-IB"
  - quote: "Masquerading as the Windows terminal server SDK DLL (wtsapi32.dll), this backdoor forward-exports all legitimate SDK functions. It appears to be designed for DLL search-order hijacking, tricking legitimate executables into loading the backdoor."
    publisher: "Group-IB"
  - quote: "The group's infrastructure and targeting profile span across countries in Europe and the Middle East. Specific targets include European nations such as the UK, France, Albania, and Belarus, alongside Middle Eastern regions including Israel, Turkey, and GCC member states."
    publisher: "Group-IB"
verification: single-source
sourcing_note: >
  Group-IB is the sole source for this specific toolset refresh, though its own article
  references prior Kaspersky (Mirage Kitten/Securelist) and GTIG (UNC1549) reporting on the same
  actor as background — which is why the registry already carries this actor under multiple
  aliases. This entry documents only the toolset and infrastructure genuinely new to this run's
  window.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Group-IB documents new infrastructure and a new toolset for Nimbus Manticore — the Iranian, IRGC-affiliated actor this pipeline already tracks under registry key `actor:screening-serpens-unc1549-smoke-sandstorm-nimbus-manticore-iran-apt` (aliases: Screening Serpens, UNC1549, Smoke Sandstorm, Mirage Kitten; Group-IB itself uses "Tortoiseshell"). This is the third distinct toolset refresh the store has now tracked for this actor within roughly seven months: six new RAT variants (MiniUpdate/MiniJunk V2) via AppDomainManager hijacking February–April 2026, the NightLedger backdoor with BridgeHead/ArcBridge WebSocket tunnelers documented by Kaspersky in July 2026, and now — reported by Group-IB on 2026-08-26 — a new reverse SSH tunneling utility and a TWOSTROKE-family C++ backdoor.

The SSH tunneler establishes an SSH connection to operator infrastructure over port 443, blending with normal HTTPS-port egress filtering, to set up a reverse tunnel: "execution of this command establishes an SSH connection to the operator's infrastructure ... on port 443 to set up a reverse tunnel. As a result, traffic sent to [a local port] on the C2 server is redirected back through the tunnel directly into the compromised network" ([Group-IB, 2026-08-26](https://www.group-ib.com/blog/tortoiseshell-apt-toolset-infrastructure/)) — giving the operator interactive network access into the victim environment without an inbound listener on the victim side. The TWOSTROKE-like backdoor masquerades as the Windows Terminal Server SDK DLL (`wtsapi32.dll`), forward-exporting all legitimate SDK functions so that a legitimate executable loading it via DLL search-order hijacking continues to function normally while the backdoor executes alongside it: "masquerading as the Windows terminal server SDK DLL (wtsapi32.dll), this backdoor forward-exports all legitimate SDK functions. It appears to be designed for DLL search-order hijacking, tricking legitimate executables into loading the backdoor" ([Group-IB, 2026-08-26](https://www.group-ib.com/blog/tortoiseshell-apt-toolset-infrastructure/)). It encrypts stack strings, derives a unique per-victim identifier from the device hostname, and communicates with multiple hardcoded control servers over HTTPS.

Group-IB's infrastructure analysis, based on geographically-labeled subdomain naming conventions, indicates expanded targeting into European nations specifically named as the UK, France, Albania and Belarus, alongside continued Middle Eastern targeting: "the group's infrastructure and targeting profile span across countries in Europe and the Middle East. Specific targets include European nations such as the UK, France, Albania, and Belarus, alongside Middle Eastern regions including Israel, Turkey, and GCC member states" ([Group-IB, 2026-08-26](https://www.group-ib.com/blog/tortoiseshell-apt-toolset-infrastructure/)) — a materially widened European footprint for an actor this pipeline already tracks as espionage-focused on aerospace, aviation, defence and telecommunications.

**Triage:** monitor for HTTPS-port (443) outbound connections that establish long-lived reverse-tunnel-shaped traffic patterns — asymmetric, low-volume-but-persistent bidirectional flows distinct from normal web-browsing HTTPS — and audit environments for a `wtsapi32.dll` present outside its expected system path or with a hash that does not match the legitimate Windows SDK component; the actor's own choice of a legitimate SDK DLL name is itself the detection anchor, since a genuine `wtsapi32.dll` never appears outside `System32`.
