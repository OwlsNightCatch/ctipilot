---
schema: 1
kind: threat
horizon: operational
title: "SMS-blaster smishing establishing itself in Switzerland — portable IMSI-catchers force 2G downgrade, bypass operator SMS filtering"
headline: "SMS-blaster smishing establishing itself in Switzerland — portable IMSI-catchers force 2G downgrade, bypass operator SMS filtering"
summary: "SMS-blaster smishing fraud establishing itself in Switzerland. ebas.ch (Swiss banking + HSLU) reports portable IMSI-catcher devices broadcasting as rogue base stations and forcing nearby smartphones within several hundred metres to attach and downgrade from 4G/5G to 2G, then delivering smishing payloads that bypass operator SMS filtering (ebas.ch, 2026-05-07). Banking and credit-card credentials are the primary target — relevant for federal mobile-security policy guidance."
discovered_at: "2026-05-11T05:00:01Z"
event_date: 2026-05-07
run_id: 2026-05-11-migrated
priority: high
immediate_action: null
tags:
  - phishing
  - mobile
  - organized-crime
regions:
  - switzerland
sectors:
  - finance
  - public-sector
entities:
  - "campaign:sms-blaster-ch-2026"
cves: []
sources:
  - url: "https://www.ebas.ch/en/2026/05/sms-blaster-new-scam-reaches-switzerland/"
    publisher: "ebas.ch, 2026-05-07"
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
migrated_from: briefs/2026-05-11.md
---

ebas.ch — the Swiss banking-sector and Lucerne University of Applied Sciences (HSLU) e-banking awareness portal — reported on 2026-05-07 that SMS-blaster fraud is establishing itself in Switzerland. A portable device (concealable in a vehicle or backpack) broadcasts as a rogue base station with strong signals that force nearby smartphones within several hundred metres to attach and to downgrade from 4G/5G to 2G. The 2G network lacks mutual authentication between handset and base station, allowing the operator to inject SMS directly into the victim's handset — entirely bypassing the mobile carrier's SMSC, where anti-phishing and anti-spam filters are applied ([ebas.ch, 2026-05-07](https://www.ebas.ch/en/2026/05/sms-blaster-new-scam-reaches-switzerland/)). The lure SMS impersonates authorities, banks or courier services, directing victims to credential-harvesting pages. A brief unexpected RAT downgrade from 4G/5G to 2G on a managed handset, in the absence of corresponding carrier outage signal, is the technical fingerprint of a rogue base station in proximity — although ebas.ch does not report observed victim handset-side telemetry as part of its disclosure.

**Why it matters to us:** Federal employees and contractors using government-issued or BYOD mobile devices are exposed to the same proximity-targeted lure that no carrier filter can stop. SMS-blaster activity is invisible to enterprise mobile threat-defence (MTD) products that rely on link reputation alone — the lure arrives via SMS, but the device-side signal is a sudden 4G/5G → 2G → 4G/5G transition that some EDR-MDM stacks (Intune mobile telemetry, Jamf Protect) can surface. Suggest disabling 2G on managed Android estates where MDM supports the setting (Android 12+ via `setAllowedNetworkTypesForReason` / Enterprise restrictions); iOS Lockdown Mode disables 2G but is impractical for routine federal use. Map smishing-lure handling to existing IR runbooks. Mapped to [T1566 Phishing](https://attack.mitre.org/techniques/T1566/) at the technique level — the smishing variant delivered via a rogue base station bypasses operator-side SMS filtering by attacking the radio-link delivery channel, not by manipulating data in flight to its intended endpoint. ebas.ch is the only source for the Swiss-localised signal
