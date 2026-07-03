---
schema: 1
kind: threat
horizon: operational
title: "VerdantBamboo (UNC5221 / WARP PANDA): an 18-month China-nexus intrusion that lived entirely on EDR-blind edge appliances and proxied into Microsoft 365 past Conditional Access"
headline: "VerdantBamboo (UNC5221 / WARP PANDA): an 18-month China-nexus intrusion that lived entirely on EDR-blind edge appliances and proxied into Microsoft 365 past"
summary: "Volexity names VerdantBamboo (UNC5221 / WARP PANDA), an 18-month China-nexus espionage intrusion that entered a European organisation through its MSP and lived exclusively on EDR-blind edge devices — pfSense firewall, a Synology NAS, and an Egnyte Storage Sync VM whose egress IP was proxied to slip into the victim's Microsoft 365 tenant past Conditional Access. Two new implants (AGENTPSD, PLENET/GRIMBOLT) joined BRICKSTORM (Volexity, 2026-06-04)."
discovered_at: "2026-06-05T05:00:00Z"
event_date: 2026-06-04
run_id: 2026-06-05-2c6574c4
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - supply-chain
  - china-nexus
regions:
  - europe
sectors:
  - public-sector
  - technology
entities: []
cves: []
sources:
  - url: "https://www.volexity.com/blog/2026/06/04/verdantbamboo-just-another-brickstorm-in-the-firewall/"
    publisher: "Volexity, 2026-06-04"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-05.md
---

Volexity attributes an incident-response case at a European organisation to a China-linked actor it tracks as **VerdantBamboo** (assessed with high confidence as UNC5221, also WARP PANDA), with access dating back at least 18 months ([Volexity, 2026-06-04](https://www.volexity.com/blog/2026/06/04/verdantbamboo-just-another-brickstorm-in-the-firewall/)). Initial access came through the victim's **MSP**: the actor had planted a BSD build of the **BRICKSTORM** Golang backdoor on the MSP's pfSense firewall. The defining tradecraft is deliberate EDR avoidance — every implant sat on appliances that cannot run an endpoint agent (firewall, Synology NAS, a retired GroupWise server) or on an **Egnyte Storage Sync** Linux VM. BRICKSTORM's proxy capability on the Storage Sync host let the actor route authentication to the victim's M365 tenant through that appliance's *trusted egress IP*, defeating Conditional Access rules that would have blocked an unrecognised source address (`T1090` internal proxy, `T1078.004` cloud accounts). After Volexity's first remediation, VerdantBamboo simply re-authenticated to the firewall with stolen admin credentials, re-enabled SSL VPN, and redeployed BRICKSTORM to the NAS — alongside two previously undocumented implants: **AGENTPSD** (a PyInstaller-packaged Python HTTPS reverse shell kept as a fallback) and **PLENET/GRIMBOLT** (a .NET Native AOT backdoor on a Linux NAS).

**Why it matters to us:** this is the precise threat model a federal SOC carries — an MSP relationship plus a fleet of edge appliances that are invisible to EDR by design. Detection has to move off the endpoint: hunt M365 sign-in logs for interactive auth originating from the egress IPs of NAS / storage-sync / firewall appliances (those should never originate user logins), alert on SSL-VPN re-enablement and admin auth to perimeter devices, and treat any appliance the vendor forbids you from instrumenting as an assumed-breach surface. Mandate MFA on all firewall management and SSL-VPN interfaces, and put the MSP's access to your perimeter under the same scrutiny as a privileged insider. `[SINGLE-SOURCE]` — Volexity primary IR (.
