---
schema: 1
kind: threat
title: Meta files contempt complaint against NSO Group over fresh WhatsApp spyware phishing
headline: Meta files contempt complaint against NSO Group over fresh WhatsApp spyware phishing
summary: "Meta disclosed it detected and disrupted a new spear-phishing campaign linked to NSO Group's Pegasus operation, and filed a federal contempt-of-court complaint arguing the activity violates the 2025 permanent injunction barring NSO from targeting WhatsApp or its users (Meta, 2026-06-08; CyberScoop, 2026-06-08)."
discovered_at: "2026-06-09T05:00:01Z"
event_date: 2026-06-08
run_id: 2026-06-09-40d562df
priority: notable
immediate_action: null
tags:
  - espionage
  - mobile
  - phishing
regions:
  - global
  - europe
sectors:
  - public-sector
  - media
entities: []
cves: []
sources:
  - url: "https://about.fb.com/news/2026/06/fighting-spyware-an-update-from-whatsapp/"
    publisher: Meta — Fighting spyware update
    role: primary
  - url: "https://cyberscoop.com/meta-contempt-complaint-nso-group-spyware/"
    publisher: CyberScoop
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/whatsapp-says-it-disrupted-new-nso-spyware-phishing-attacks/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-09.md
---

Meta disclosed it detected and disrupted a new spear-phishing campaign linked to NSO Group's Pegasus operation, and filed a federal contempt-of-court complaint arguing the activity violates the 2025 permanent injunction barring NSO from targeting WhatsApp or its users ([Meta, 2026-06-08](https://about.fb.com/news/2026/06/fighting-spyware-an-update-from-whatsapp/); [CyberScoop, 2026-06-08](https://cyberscoop.com/meta-contempt-complaint-nso-group-spyware/)). The campaign used one-click links sent to WhatsApp users that redirected them to external attacker-controlled websites — the same social-engineering pattern (T1566.002) tied to earlier NSO phishing chains; Meta states no WhatsApp protocol zero-day and no end-to-end-encryption bypass was involved ([BleepingComputer, 2026-06-08](https://www.bleepingcomputer.com/news/security/whatsapp-says-it-disrupted-new-nso-spyware-phishing-attacks/)). Meta removed test accounts and groups NSO created on the platform.

**Why it matters to us:** The threat vector is user-level social engineering, not platform exploitation — iOS Lockdown Mode and Android Advanced Protection both reduce the Pegasus delivery surface, and mobile-threat-defence monitoring of device-integrity attestation is the relevant control. NSO's confirmed customer base is governments and its targeting pattern (officials, journalists, activists) is documented across EU member states, keeping commercial-spyware exposure a standing concern for public-sector mobile fleets.
