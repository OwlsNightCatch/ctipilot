---
schema: 1
kind: threat
title: "BigBear 2.0 — an Evilginx2-based Microsoft 365 phishing-as-a-service panel that JavaScript-disables FIDO2/WebAuthn to force victims onto phishable MFA, leased to at least five affiliates"
headline: "CloudSEK gained admin access to the panel and found custom code specifically written to defeat the one MFA class that structurally resists this attack"
summary: >
  CloudSEK gained administrator access to the control panel of BigBear 2.0, an Evilginx2-based
  adversary-in-the-middle phishing-as-a-service operation exclusively targeting Microsoft 365
  across 42 VPS nodes. Custom JavaScript injected into every proxied login page disables
  FIDO2/WebAuthn to force victims onto phishable MFA methods; the panel has captured 5,137
  credential records, including 474 fully MFA-bypassed sessions, from 3,331 victim IPs across
  40+ countries, with IT-services/MSP organizations the single largest targeted sector.
discovered_at: "2026-09-08T04:45:00Z"
updated_at: null
event_date: "2026-09-07"
run_id: 2026-09-08T0411Z-intel
priority: high
immediate_action: null
tags: [phishing, identity, cloud]
regions: [global]
sectors: [public-sector, technology]
entities: ["tool:bigbear-phaas"]
techniques: [T1566.002, T1539, T1550.004, T1111]
affected_products: ["Microsoft 365", "Microsoft Entra ID"]
cves: []
sources:
  - url: "https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign"
    publisher: "CloudSEK (Gagan Aggarwal / TRIAD)"
    date: "2026-09-07"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/"
    publisher: "BleepingComputer (Bill Toulas)"
    date: "2026-09-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The panel has exfiltrated 5,137 credential records — including 474 complete MFA-bypassed authentications, 1,032 plaintext passwords, and 4,148 session cookies — affecting 3,331 unique victim IPs across 40+ countries"
    publisher: "CloudSEK"
    source_url: "https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign"
  - quote: "Since late July 2026 the threat actor has deleted 26 of the 42 observed VPS nodes from the panel — evidence of active counter-forensic operations in response to detection."
    publisher: "CloudSEK"
    source_url: "https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign"
  - quote: "At the time of writing, the administration panel remains online, while the phishing infrastructure has been offline for nearly three weeks."
    publisher: "BleepingComputer (Bill Toulas)"
    source_url: "https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/"
  - quote: "FIDO2 (hardware security keys, platform authenticators like Apple Face ID / Windows Hello) uses origin-bound credentials. The cryptographic assertion is tied to the origin domain (e.g., login.microsoftonline.com). When Evilginx2 proxies traffic, the origin seen by the browser is the phishing domain (login.evil-domain.com), not the real Microsoft domain. The FIDO2 assertion fails because the origin does not match the credential's registered origin. This is the only MFA method that structurally prevents AiTM phishing."
    publisher: "CloudSEK"
    source_url: "https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign"
  - quote: "Researchers at cybersecurity company CloudSEK gained administrator access to the control panel and found that the service managed 42 VPS nodes, all configured to target Microsoft 365 as part of the observed operation."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/"
verification: multi-source
sourcing_note: >
  BleepingComputer's account substantially relays CloudSEK's own report (the same figures, quotes
  and technical detail, shared directly with BleepingComputer) rather than presenting independent
  technical corroboration; credibility is held at 2 to reflect that the underlying technical
  findings trace to one assessor.
confidence: high
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

CloudSEK's TRIAD team gained administrator access to the control panel of BigBear 2.0, a rebranded, Evilginx2-based adversary-in-the-middle phishing-as-a-service operation targeting Microsoft 365 exclusively, and published full technical findings on 2026-09-07 ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign)). Victims reach the operation by clicking a phishing link typically delivered via email, which proxies them to what appears to be the legitimate Microsoft login page ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign)). The panel managed 42 VPS nodes running Evilginx2's reverse-proxy engine on a single phishlet that proxies the entire authentication flow between the victim and Microsoft's own login domain: the victim's password is captured in plaintext as it passes through, and after the victim completes MFA, Microsoft's own session cookie is captured off the wire before it reaches the victim's browser, because the proxy terminates the victim's TLS session before opening its own to Microsoft ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign)). That cookie is bound to the browser session but not to any device or location, so importing it into an attacker-controlled browser inherits the fully authenticated session — TOTP, push and SMS MFA are all structurally bypassed this way, since the proxy never has to defeat the second factor, only wait for the legitimate user to clear it ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign); [BleepingComputer, 2026-09-07](https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/)).

What distinguishes this operation from stock Evilginx2 deployments is custom JavaScript injected into every proxied login page that monkey-patches the browser's `PublicKeyCredential`/`navigator.credentials` API, forcing a fallback away from FIDO2/WebAuthn — the one MFA class immune to AiTM replay, because its cryptographic assertion is bound to the legitimate origin domain and fails outright when the browser's actual origin is the phishing domain rather than Microsoft's own ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign)). The same injected code blocks outbound requests to Microsoft's own anti-phishing telemetry and canary-token endpoints and auto-enables "Keep me signed in" to maximize the stolen session's lifetime ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign)). The panel exposes a REST API that automatically replays captured cookies against Microsoft 365, and a keepalive feature abuses captured refresh tokens — typically valid around 90 days on a sliding window — to periodically refresh session cookies well past their nominal expiry ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign)). A geo-matched residential-proxy pool spanning 69 countries routes relayed traffic through an IP in the victim's own country, defeating Microsoft's location-anomaly detection and satisfying IP-based Conditional Access checks that key on geolocation rather than device state ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign)).

At the time of CloudSEK's writing the panel had captured 5,137 credential records — 474 complete MFA-bypassed sessions, 1,032 plaintext passwords, and 4,148 session cookies — from 3,331 unique victim IPs across more than 40 countries ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign)). BleepingComputer's own review of CloudSEK's dataset gives the organizational scale directly: 258 distinct organizations had at least one completed MFA-bypass compromise, out of 461 organizations that appear in the broader targeting dataset ([BleepingComputer, 2026-09-07](https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/)). CloudSEK describes the operation as still active as of its report, but also records that the threat actor has deleted 26 of the panel's 42 observed VPS nodes since late July 2026 as apparent counter-forensic activity following detection ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign)); BleepingComputer separately reports that, as of its own writing, BigBear's administration panel remains reachable while the phishing infrastructure itself has been offline for nearly three weeks ([BleepingComputer, 2026-09-07](https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/)) — consistent with an operator tearing down active phishing nodes under pressure while the panel and its captured-credential dataset persist. The service is leased to at least five identified affiliate operators, each receiving stolen credentials in real time through dedicated Telegram bots ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign); [BleepingComputer, 2026-09-07](https://www.bleepingcomputer.com/news/security/bigbear-microsoft-365-phishing-service-bypassed-mfa-at-258-organizations/)). IT-services and managed-service-provider organizations were the single largest targeted sector, which CloudSEK notes is disproportionate because a compromised IT provider's privileged access to client Azure AD, on-premises AD, RMM tooling and password managers enables downstream supply-chain compromise of its customers ([CloudSEK, 2026-09-07](https://www.cloudsek.com/blog/tracking-bigbear-2-0-evilginx2-phishing-campaign)).

**Defender takeaway:** any Microsoft 365 or Entra ID tenant, and any managed IT-service provider holding privileged access to one, is directly in scope — phishing-resistant FIDO2/WebAuthn is the only MFA class this operation cannot structurally defeat, so its deployment should be prioritized over TOTP, push or SMS wherever administrative or high-value accounts are concerned, paired with Conditional Access policies keyed to device-compliance state rather than geolocation, since geo-matched residential proxies defeat the latter.

**Triage:** the vendor-neutral tell is a session-cookie-authenticated action with no matching interactive MFA challenge in the same session lineage, or a token-issuance event immediately followed by activity from a network location or device-compliance state inconsistent with the device that originally enrolled; a legitimate user re-using a cached session from a known device does not produce this mismatch, which is what separates the AiTM replay from ordinary session persistence.
