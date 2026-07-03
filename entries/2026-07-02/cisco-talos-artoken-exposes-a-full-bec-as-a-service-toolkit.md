---
schema: 1
kind: research
horizon: operational
title: "Cisco Talos: \"ARToken\" exposes a full BEC-as-a-service toolkit on top of Microsoft 365 device-code phishing"
headline: "Cisco Talos: \"ARToken\" exposes a full BEC-as-a-service toolkit on top of Microsoft 365 device-code phishing"
summary: "A full BEC-as-a-service panel for Microsoft 365 surfaces. Cisco Talos documented \"ARToken,\" an EvilTokens-lineage phishing-as-a-service platform whose 80+ API endpoints automate device-code phishing, Primary Refresh Token persistence that survives password resets, and mailbox/SharePoint exfiltration against M365 tenants (Cisco Talos)."
discovered_at: "2026-07-02T04:55:22Z"
event_date: 2026-07-01
run_id: 2026-07-02-6551f8c2
priority: high
immediate_action: null
tags:
  - phishing
  - identity
  - cloud
regions:
  - global
sectors:
  - finance
  - public-sector
entities:
  - "tool:talos-artoken-eviltokens-bec-panel"
cves: []
sources:
  - url: "https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/"
    publisher: Cisco Talos
    role: primary
  - url: "https://cyberscoop.com/artoken-bec-platform-cisco-talos/"
    publisher: CyberScoop
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
migrated_from: briefs/2026-07-02.md
---

Cisco Talos identified a fully-featured phishing-as-a-service operator panel, "ARToken," that shares API contracts and infrastructure patterns with EvilTokens, the device-code phishing platform Sekoia and Microsoft documented in early 2026 ([Cisco Talos, 2026-07-01](https://blog.talosintelligence.com/artoken-inside-an-eviltokens-affiliate-panel-targeting-microsoft-365/)). Its dashboard exposes 80+ API endpoints spanning device-code phishing, Primary Refresh Token (PRT) persistence, mailbox access, BEC operations and SharePoint/OneDrive exfiltration — a complete post-compromise environment, not just a credential kit. The OAuth 2.0 Device Authorization Grant (RFC 8628) flow drives PRT acquisition via a `/prt/setup → /prt/refresh → /prt/renew → /prt/reacquire → /prt/cookie` chain that survives password resets, and the panel adds cross-mailbox keyword monitoring, programmatic inbox-rule creation for evidence suppression, and operator-to-operator shared access — capabilities CyberScoop notes go beyond what has been publicly documented for EvilTokens ([CyberScoop, 2026-07-01](https://cyberscoop.com/artoken-bec-platform-cisco-talos/)). Talos maps the activity to T1566.002, T1528, T1098.001, T1114.002 and T1550.001. **Detection/hardening:** hunt Entra ID sign-in logs for device-code grants with anomalous `clientMode` "broker" semantics and WAM broker-issued PRT refresh/renew outside expected device-registration windows; alert on new Entra device registrations shortly after a device-code auth from an unfamiliar IP/UA; flag programmatically-created inbox rules combining forwarding with auto-delete. Restrict the OAuth device-code flow via Conditional Access and enforce token-protection (sign-in frequency + PRT binding), especially for finance/AP-adjacent roles.
