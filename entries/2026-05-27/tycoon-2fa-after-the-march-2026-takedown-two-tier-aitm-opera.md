---
schema: 1
kind: threat
horizon: operational
title: "Tycoon 2FA after the March 2026 takedown: two-tier AiTM operator architecture and the OAuth device-code variant"
headline: "Tycoon 2FA after the March 2026 takedown: two-tier AiTM operator architecture and the OAuth device-code variant"
summary: "Tycoon 2FA adapted within weeks of the March 2026 takedown. Elastic Security Labs maps a two-tier operator architecture and a Microsoft-only OAuth device-code-grant variant that mints and replays Primary Refresh Tokens; today's deep dive covers the Entra ID / Google Workspace detection logic and a documented Identity Protection false-negative gap."
discovered_at: "2026-05-27T05:00:05Z"
event_date: 2026-05-26
run_id: 2026-05-27-0b6f12dd
priority: high
immediate_action: null
tags:
  - phishing
  - identity
  - cloud
regions:
  - global
sectors:
  - public-sector
  - education
  - technology
entities: []
cves: []
sources:
  - url: "https://www.elastic.co/security-labs/tycoon-2fa-aitm-detection-engineering"
    publisher: "Elastic Security Labs, 2026-05-26"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-27.md
---

**Background.** Tycoon 2FA is among the most prolific adversary-in-the-middle (AiTM) phishing-as-a-service kits, built to intercept the post-MFA session cookie of Microsoft 365 and Google Workspace accounts in real time. In March 2026 a coordinated takedown led by Microsoft and Europol — with Cloudflare, SpyCloud and eSentire — seized over 300 domains, but operators adapted within weeks, and by late April 2026 campaigns combined Tycoon tradecraft with OAuth Device Code phishing flows ([Elastic Security Labs, 2026-05-26](https://www.elastic.co/security-labs/tycoon-2fa-aitm-detection-engineering)). This brief last covered the post-takedown device-code pivot on 2026-05-18; Elastic's 2026-05-26 analysis is a detailed detection-engineering treatment of the kit's current operator architecture and is the basis for the technique mapping below.

**Two operating variants.** The kit now runs in two structurally distinct modes. The **classic WebSocket AiTM reverse-proxy** intercepts the authenticated session cookie as the victim completes MFA against a real Microsoft/Google login (`T1557` [Adversary-in-the-Middle](https://attack.mitre.org/techniques/T1557/), `T1539` [Steal Web Session Cookie](https://attack.mitre.org/techniques/T1539/), replayed via `T1550.004` [Web Session Cookie](https://attack.mitre.org/techniques/T1550/004/)). The newer **device-code-grant abuse variant** is Microsoft-only: it leverages the Microsoft Authentication Broker client ID `29d9ed98-a469-4536-ade2-f981bc1d605e` to obtain and replay a Primary Refresh Token (PRT), escalating a single phished code into durable token material (`T1528` [Steal Application Access Token](https://attack.mitre.org/techniques/T1528/)). The token-type progression Elastic observed in Entra sign-in logs is the tell: `incomingTokenType:none → refreshToken → primaryRefreshToken`.

**Two-tier operator architecture and the cross-tier signal.** The operation splits across two tiers with different network fingerprints. **Tier 1 (Kit Relay)** performs token acquisition from cloud-VPS egress IPs using `node` / `axios` / `undici` / `node-fetch` user agents. **Tier 2 (Operator Console)** performs post-compromise enumeration from residential-shaped ISP egress with a fixed browser UA. Because single-ASN rules only catch one tier, Elastic's highest-confidence indicator is the **cross-tier pivot**: two distinct ASNs (one cloud-VPS, one residential-shaped) authenticating as the same user principal within minutes and sharing the same `c_sid` correlation value. Within roughly 30–60 seconds of a successful token replay, Tier 2 runs a Microsoft Graph reconnaissance burst — `transitiveRoleAssignments`, `tenantRelationships/getResourceTenants` (cross-tenant lateral-movement preparation), contact harvesting and `subscribedSkus` — typically 20–30+ calls spanning four or more recon categories (`T1087.004` [Cloud Account Discovery](https://attack.mitre.org/techniques/T1087/004/), `T1526` [Cloud Service Discovery](https://attack.mitre.org/techniques/T1526/)).

**Detection concepts.** Elastic shipped multiple Entra ID and Google Workspace detections, including an ES|QL **"Microsoft Graph Multi-Category Reconnaissance Burst"** rule that fires on the four-plus-category Graph enumeration inside a short window. Concept-level hunts a SOC can build without the rules: in Entra sign-in logs, alert on `node`/`axios`/`undici`/`node-fetch` user agents paired with the Microsoft Authentication Broker client ID, and on device-registration events using non-standard UAs (not `Dsreg` / `DeviceRegistrationClient` / `Dalvik`); for Google Workspace, alert on Admin SDK `login_success` events landing within ~1 second across multiple relay IPs, and on an OAuth `token.authorize` for the Chrome client `77185425430.apps.googleusercontent.com` followed by a `DEVICE_REGISTER_UNREGISTER_EVENT` within 0.6–1.2 seconds. **Critical detection gap:** Entra ID Identity Protection may not flag the kit infrastructure because of rapid IP rotation, and Elastic observed the risk engine flagging `anomalousToken` but subsequently marking the victim `aiConfirmedSafe` — a false negative that defenders cannot treat Identity Protection alone as sufficient coverage for. Elastic's automated response (disable account, delete device principals, revoke sessions, open a case) runs in under ten seconds, inside the observed 10–20-minute kit-to-operator handoff window — the operational point being that response must beat the handoff, not merely detect after it.

**Hardening.** Enable Microsoft Token Protection via Conditional Access so a stolen session/refresh token is bound to the originating device; require compliant or managed devices for access to sensitive resources; and use Authentication Methods policies to block the OAuth Device Code flow for the majority of users who never legitimately need it — the device-code variant collapses if the grant is disabled for the targeted population. None of these depend on a patch; they are policy changes that remove the attack path the kit monetises.
