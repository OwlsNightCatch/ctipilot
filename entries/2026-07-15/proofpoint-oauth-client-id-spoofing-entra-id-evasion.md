---
schema: 1
kind: research
horizon: operational
title: "Proofpoint: OAuth client ID spoofing validates stolen Entra ID credentials at scale without writing a successful sign-in log"
headline: "A fake client_id on Entra ID's ROPC token endpoint lets attackers enumerate and validate credentials while leaving a blank application name in the sign-in log"
summary: >
  Proofpoint (2026-07-13) documented OAuth client ID spoofing against Microsoft Entra ID, independently
  weaponised by two clusters. An attacker POSTs credentials to the /common/oauth2/token endpoint using the
  legacy ROPC flow with an arbitrary unregistered GUID as client_id; Entra ID's differential AADSTS error
  responses leak username and password validity, and AADSTS700016 ("application not found") is returned when
  the credentials are BOTH correct — turning a code defenders read as a harmless misconfiguration into a
  credential-validity oracle. Because the client_id is unregistered, the sign-in log entry (where one appears
  at all) carries a blank application name, defeating detections that correlate authentication spikes by app.
  The concrete fix is to block the ROPC grant type outright, because Conditional Access policies scoped to
  specific applications are the exact control this technique sidesteps.
discovered_at: "2026-07-15T04:36:00Z"
event_date: "2026-07-13"
run_id: 2026-07-15T0409Z-intel
priority: notable
immediate_action: null
tags: [identity, cloud, phishing]
regions: [global]
sectors: [public-sector, finance, telco]
entities: [actor:unk-pyreq2323, actor:unk-outflareaz]
techniques: [T1110.004, T1589.001, T1078.004]
affected_products: ["Microsoft Entra ID"]
cves: []
sources:
  - url: "https://www.proofpoint.com/us/blog/threat-insight/oauth-client-id-spoofing-why-fake-client-ids-are-gaining-traction-stealthy"
    publisher: "Proofpoint Threat Research"
    date: "2026-07-13"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/07/13/entra-id-oauth-client-id-spoofing/"
    publisher: "Help Net Security"
    date: "2026-07-13"
    role: corroborating
  - url: "https://thehackernews.com/2026/07/oauth-client-id-spoofing-lets-attackers.html"
    publisher: "The Hacker News"
    date: "2026-07-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "When a spoofed client ID is used, no corresponding application name is recorded in the sign-in log. This means that detections that look for surges against a specific application name may miss this activity entirely, as the field is blank."
    publisher: "Proofpoint Threat Research"
  - quote: "By fragmenting authentication attempts across many fictional applications, activity becomes harder to correlate and may evade per-application detections and rate limiting."
    publisher: "Proofpoint Threat Research"
verification: multi-source
sourcing_note: "Primary is Proofpoint Threat Research's own analysis; the corroborating outlets re-report it rather than independently reproducing the technique, so credibility is set at 2 (single-origin research, plausible and internally consistent). Publication date 2026-07-13 is just outside this run's 24 h window but inside the 72 h developing window; carried as first coverage of a significant, not-previously-published Entra ID evasion technique. event_date records the disclosure date."
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Block the ROPC (Resource Owner Password Credentials) grant type in Entra ID via legacy-authentication blocking policy; it is the load-bearing fix, since Conditional Access policies scoped to specific applications are bypassed by an unregistered client_id."
migrated_from: null
---

Proofpoint's Threat Research team documented a stealthy authentication-evasion technique — **OAuth client ID spoofing** — being independently weaponised by two distinct clusters against **Microsoft Entra ID** ([Proofpoint, 2026-07-13](https://www.proofpoint.com/us/blog/threat-insight/oauth-client-id-spoofing-why-fake-client-ids-are-gaining-traction-stealthy)). The mechanism abuses the legacy Resource Owner Password Credentials (ROPC) flow: an attacker POSTs a username and password to Entra ID's `/common/oauth2/token` endpoint while supplying an arbitrary, unregistered GUID as the `client_id` parameter instead of a real application ID. Entra ID's differential error responses then leak validity regardless of whether the client_id is legitimate — `AADSTS50034` for a non-existent username, `AADSTS50126` for a valid username with the wrong password, and, critically, `AADSTS700016` ("application not found in directory") when the username *and* password are both correct, because Entra ID validates the credential before it fails on the unrecognised client. The result is a credential-validity oracle that most defenders misread: `AADSTS700016` is ordinarily dismissed as a harmless misconfigured-app error, which is precisely the blind spot both clusters exploited ([Help Net Security, 2026-07-13](https://www.helpnetsecurity.com/2026/07/13/entra-id-oauth-client-id-spoofing/)).

The evasion value is in the telemetry: none of these code paths writes a successful sign-in event, and because the client_id is unregistered, the sign-in log entry carries no application name at all — "detections that look for surges against a specific application name may miss this activity entirely, as the field is blank" ([Proofpoint, 2026-07-13](https://www.proofpoint.com/us/blog/threat-insight/oauth-client-id-spoofing-why-fake-client-ids-are-gaining-traction-stealthy)). Proofpoint attributes two campaigns of opportunistic mass enumeration: **UNK_pyreq2323** (January–March 2026, AWS-hosted, 700,000+ distinct spoofed client IDs) and **UNK_OutFlareAZ** (December 2025–March 2026, Cloudflare-fronted, 3.7M distinct spoofed IDs), whose divergent tooling and client-ID-generation strategies point to parallel invention rather than shared code ([The Hacker News, 2026-07-13](https://thehackernews.com/2026/07/oauth-client-id-spoofing-lets-attackers.html)).

**Defender takeaway:** the concrete detection-logic change is to stop treating `AADSTS700016` against a valid username as harmless and start treating a burst of them — especially from a single ASN or cloud-hosting range across many usernames — as equivalent in severity to a successful credential-stuffing hit; sign-in entries with a blank application ID on ROPC token requests are the anomaly to hunt. **Triage:** legitimate ROPC usage (some line-of-business apps, service accounts and CI/CD pipelines still use it deliberately) shows a registered, named application in the sign-in log — a genuinely blank application-name field on a `/common/oauth2/token` request, at volume against many distinct usernames, is what separates the attack from benign legacy authentication. The durable fix is to block the ROPC grant type outright, since per-application Conditional Access scoping is the exact control this technique defeats.
