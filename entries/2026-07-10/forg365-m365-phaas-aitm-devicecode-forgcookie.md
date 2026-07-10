---
schema: 1
kind: threat
horizon: operational
title: "Forg365: a commercial Microsoft 365 phishing-as-a-service kit bundling device-code + AiTM phishing, in-panel AI lure drafting, and a browser extension for SSO-cookie persistence"
headline: "ZeroBEC details Forg365 — a Telegram-sold M365 PhaaS that survives MFA and keeps operator access alive via a ForgCookie browser extension"
summary: >
  ZeroBEC documented Forg365, a Telegram-distributed, subscription-priced Microsoft 365 phishing-as-a-service
  platform that pairs an OAuth device-code phishing path with an adversary-in-the-middle session-theft path,
  an in-panel AI lure generator, and a companion browser extension (ForgCookie) that silently refreshes the
  stolen Microsoft SSO cookie so access persists without the victim re-authenticating. Both paths yield a
  valid, MFA-satisfied token because the victim completes the real Microsoft login. It is a distinct kit and
  operator from the Railway/EvilTokens device-code campaign covered earlier — same primitive, productized.
discovered_at: "2026-07-10T20:34:32Z"
event_date: "2026-07-09"
run_id: 2026-07-10T2009Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity, cloud, ai-abuse]
regions: [global]
sectors: [public-sector, finance, healthcare, telco]
entities: [tool:forg365-phaas]
techniques: [T1566.002, T1528, T1539, T1176]
affected_products: ["Microsoft 365", "Microsoft Entra ID"]
cves: []
sources:
  - url: "https://zerobec.com/blog/inside-forg365-telegram-distributed-sneaky2fa-style-phaas"
    publisher: "ZeroBEC"
    date: "2026-07-09"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-forg365-phishing-platform-uses-ai-to-target-microsoft-365-accounts/"
    publisher: "BleepingComputer"
    date: "2026-07-09"
    role: corroborating
  - url: "https://labs.cloudsecurityalliance.org/research/csa-research-note-forg365-ai-phishing-service-20260710-csa-s/"
    publisher: "Cloud Security Alliance (CSA Labs)"
    date: "2026-07-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Forg365 is a mature Microsoft 365-focused phishing-as-a-service platform that combines device-auth phishing, AiTM delivery, AntiBot evasion, campaign delivery, session persistence, AI-assisted lure creation, and post-compromise mailbox operations inside a commercial operator ecosystem."
    publisher: "ZeroBEC"
  - quote: "ForgCookie, the browser extension associated with the platform, is designed for Microsoft SSO cookie refresh, browser-based access, and persistent session workflows after compromise."
    publisher: "ZeroBEC"
  - quote: "multifactor authentication does not stop the attack because the victim, not the attacker, is the one completing the MFA challenge"
    publisher: "Cloud Security Alliance (CSA Labs)"
verification: multi-source
sourcing_note: "Primary technical analysis by ZeroBEC from a delivered lure plus the exposed operator panel; corroborated by BleepingComputer and a CSA Labs research note. ZeroBEC assesses Forg365 as a Kali365-class platform with Sneaky2FA-style AiTM overlap but does not assert common ownership — attribution reported as assessed, not concluded."
confidence: high
update_of: null
references: ["2026-07-10/m365-conditional-access-gaps-railway-lshiy-campaigns"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Block the OAuth device-authorization flow via Entra Conditional Access (Authentication Flows → Device Code Flow → Block) except where a documented CLI/headless use case requires it — this closes the device-code path Forg365 sells."
  - "On any account with suspected compromise, run revokeSignInSessions in Entra ID — a password reset alone does not invalidate a device-code-derived refresh token or an AiTM-stolen session cookie."
  - "Hunt managed endpoints for browser extensions exhibiting SSO-cookie-refresh behavior (ForgCookie class), and alert on new OAuth app consent grants or new mailbox forwarding/inbox rules created immediately after a sign-in."
migrated_from: null
---

ZeroBEC's teardown, corroborated by BleepingComputer and a CSA Labs research note, describes Forg365 as a Telegram-distributed, subscription-priced (5-day trial, $400/month, $3,800/year) Microsoft 365 phishing-as-a-service platform that packages two independent credential-theft paths behind one operator console ([ZeroBEC, 2026-07-09](https://zerobec.com/blog/inside-forg365-telegram-distributed-sneaky2fa-style-phaas); [BleepingComputer, 2026-07-09](https://www.bleepingcomputer.com/news/security/new-forg365-phishing-platform-uses-ai-to-target-microsoft-365-accounts/)). The device-authorization branch presents a Microsoft-styled verification-code page and drives the legitimate Microsoft Authentication Broker flow; the adversary-in-the-middle branch classifies inbound traffic to decide whether to serve the phishing page or a benign decoy. Both converge on a valid, MFA-satisfied refresh token or session cookie because the victim completes the genuine Microsoft authentication — as CSA Labs puts it, "multifactor authentication does not stop the attack because the victim, not the attacker, is the one completing the MFA challenge" ([CSA Labs, 2026-07-10](https://labs.cloudsecurityalliance.org/research/csa-research-note-forg365-ai-phishing-service-20260710-csa-s/)). Two capabilities stand out beyond the already-covered device-code primitive: an AI lure-drafting assistant embedded directly in the panel alongside SMTP rotation, OAuth-app configuration and token vaulting, and ForgCookie — a Chrome/Edge/Brave extension that silently triggers OAuth flows to refresh the stolen SSO cookie so operator access outlives its normal expiry ([ZeroBEC, 2026-07-09](https://zerobec.com/blog/inside-forg365-telegram-distributed-sneaky2fa-style-phaas)). ZeroBEC's Entra telemetry tied observed device-code activity to a residential ISP address, with a campaign-linked backend node later performing Microsoft Graph device-registration calls.

**Defender takeaway:** the durable, kit-independent detections are in Entra sign-in and audit telemetry, not on the lure — surface device-code authentication events (device-code client-id patterns in sign-in logs), OAuth app consent grants and mailbox-rule changes clustered immediately after a sign-in, and browser-extension installs on managed endpoints that programmatically refresh SSO cookies. Forg365 is a distinct product and operator from the Railway/EvilTokens device-code campaign, so it is a new entry rather than an update; the shared abused primitive (device-authorization-grant phishing) is already covered and not re-taught here. **Triage:** legitimate device-code sign-ins are real (CLI tools, smart-TV and headless-device apps) — the discriminator is a verification-code prompt reached via an unsolicited email lure or phone call rather than a user-initiated CLI/device flow, and a subsequent refresh-token or cookie reuse from an origin, ASN or device posture that does not match the user's baseline. Because the token is MFA-satisfied, revocation (`revokeSignInSessions`), not a password reset, is what actually evicts the operator.
