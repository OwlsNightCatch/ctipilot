---
schema: 1
kind: research
horizon: operational
title: "Unit 42 — ROADtools operationalised by Midnight Blizzard, Curious Serpens and UTA0355 for Entra ID device registration, token theft and tenant enumeration"
headline: "Unit 42 — ROADtools operationalised by Midnight Blizzard, Curious Serpens and UTA0355 for Entra ID device registration, token theft and tenant enumeration"
summary: "Unit 42 documents (2026-05-22) systematic nation-state operationalisation of ROADtools — the open-source Python Entra ID attack/defence framework hosted at github.com/dirkjanm/ROADtools — by three named clusters: Cloaked Ursa / Midnight Blizzard / APT29 / NOBELIUM (Russia), **Curious Serpens / Peach …"
discovered_at: "2026-05-23T05:00:07Z"
event_date: 2026-05-22
run_id: 2026-05-23-852c21c8
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - identity
  - cloud
  - russia-nexus
  - iran-nexus
regions:
  - global
  - europe
sectors:
  - public-sector
  - defense
  - technology
entities: []
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/"
    publisher: Unit 42
    role: primary
  - url: "https://www.volexity.com/blog/2025/04/22/phishing-for-codes-russian-threat-actors-target-microsoft-365-oauth-workflows/"
    publisher: Volexity OAuth device-code background (2025-04)
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
migrated_from: briefs/2026-05-23.md
---

Unit 42 documents (2026-05-22) systematic nation-state operationalisation of **ROADtools** — the open-source Python Entra ID attack/defence framework hosted at `github.com/dirkjanm/ROADtools` — by three named clusters: **Cloaked Ursa / Midnight Blizzard / APT29 / NOBELIUM** (Russia), **Curious Serpens / Peach Sandstorm / APT33** (Iran) and **UTA0355** (Russian state-affiliated) ([Unit 42, 2026-05-22](https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/)). The chain begins with credential compromise (password spray or OAuth device-code phishing, then uses `roadtx` to register attacker-controlled devices in the victim's Entra ID tenant, establishing persistence via a Primary Refresh Token bound to a registered device. The `roadrecon` module performs systematic directory enumeration via legacy Azure AD Graph API calls — now also ported to the msgraph branch — targeting users, groups, service principals, application permissions and OAuth token grants.

MITRE ATT&CK techniques mapped explicitly by Unit 42: T1098.005 (Account Manipulation: Device Registration), T1550 (Use Alternate Authentication Material), and T1087 (Account Discovery via Microsoft Graph API). The device-PRT-binding step functionally bypasses tenant MFA — the brief leaves the explicit T1556.006 framing off since Unit 42 does not map it that way; defenders running custom ATT&CK overlays may want to add it themselves. Volexity's April 2025 [OAuth device-code paper](https://www.volexity.com/blog/2025/04/22/phishing-for-codes-russian-threat-actors-target-microsoft-365-oauth-workflows/) is the historical background for the device-code half of the chain. Detection vantage: monitor Entra ID audit logs for `Add device` events from unfamiliar device names or from IPs not in expected employee geographies; alert on sign-in logs carrying the `roadtx` user-agent string or unexpected `https://login.microsoftonline.com/common/oauth2/token` device-code grant flows; review Microsoft Graph Activity Logs for bulk `GET /users`, `GET /groups` and `GET /servicePrincipals` calls clustered by time. Hardening: enforce Conditional Access token-protection (token binding renders stolen tokens non-transferable across devices); restrict device registration to compliant or hybrid-joined devices only; enforce Privileged Access Workstation policy for admin token issuance; block Azure AD Graph via `blockLegacyAuthentication`. Midnight Blizzard has a documented pattern of targeting EU diplomatic corps and government Microsoft 365 tenants, so the relevance to Swiss federal and EU institution Entra estates is direct.
