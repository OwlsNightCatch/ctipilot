---
schema: 1
kind: threat
title: "Canton Vaud warns of a device-code phishing campaign against Microsoft 365 accounts running in French-speaking Switzerland, with several organisations already affected"
headline: "Vaud: device-code phishing against Microsoft 365 is running in Romandie; several organisations already affected"
summary: >
  The canton of Vaud said on 2026-11-04 that a Microsoft 365 device-code phishing campaign is running in French-speaking Switzerland and that
  several organisations are already affected: mail that appears to come from a company or a known contact leads the reader to type a code on a
  genuine Microsoft sign-in page, which gives the attacker access to the account. Microsoft documents a Conditional Access policy that blocks
  the device code flow for tenants that do not need it.
discovered_at: "2026-11-05T03:56:00Z"
updated_at: null
event_date: "2026-11-04"
run_id: 2026-11-05T0255Z-intel
priority: high
immediate_action: null
tags: [phishing, identity, cloud]
regions: [switzerland]
sectors: []
entities: ["campaign:m365-device-code-phishing-romandie-2026-11", "product:microsoft-365"]
techniques: [T1566.002, T1528, T1078.004]
affected_products: ["Microsoft 365", "Microsoft Entra ID"]
cves: []
sources:
  - url: "https://www.vd.ch/actualites/actualite/news/26768-campagne-de-phishing-ciblant-les-comptes-microsoft-365"
    publisher: "Canton of Vaud (news item, in French)"
    date: "2026-11-04"
    role: primary
  - url: "https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows"
    publisher: "Microsoft Learn (Block authentication flows with Conditional Access policy)"
    date: "2026-04-07"
    role: corroborating
  - url: "https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows"
    publisher: "Microsoft Learn (Authentication flows as a condition in Conditional Access policy)"
    date: "2026-03-24"
    role: corroborating
  - url: "https://developers.cloudflare.com/workers/configuration/routing/workers-dev/"
    publisher: "Cloudflare Docs (workers.dev routes)"
    date: "2026-09-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A phishing campaign is currently running in French-speaking Switzerland. Several organisations have already been affected."
    original: "Une campagne de hameçonnage (phishing) est actuellement en cours en Suisse romande. Plusieurs organisations ont déjà été touchées."
    publisher: "Canton of Vaud"
    source_url: "https://www.vd.ch/actualites/actualite/news/26768-campagne-de-phishing-ciblant-les-comptes-microsoft-365"
  - quote: "This campaign uses a technique called Device Code Phishing. It consists of getting you to enter a code on a legitimate Microsoft authentication page."
    original: "Cette campagne utilise une technique appelée Device Code Phishing. Elle consiste à vous faire saisir un code sur une page d'authentification Microsoft légitime."
    publisher: "Canton of Vaud"
    source_url: "https://www.vd.ch/actualites/actualite/news/26768-campagne-de-phishing-ciblant-les-comptes-microsoft-365"
verification: single-source
sourcing_note: >
  The canton of Vaud's notice, a first-party cantonal authority speaking for its own jurisdiction, is the only source for the campaign: no NCSC
  Switzerland post, other canton, Swiss outlet or Microsoft statement corroborates it, and the notice names no actor, phishing kit, number or
  sector of affected organisations or start date. The notice is in French only and quoted here in English translation. The Conditional Access
  lever and the sign-in telemetry come from Microsoft's documentation, not from the notice.
confidence: medium
references:
  - 2026-05-23/fbi-psa260521-kali365-oauth-device-code-phaas-bypasses-m365
  - 2026-10-23/m365-token-spray-replay-rogue-entra-devices-mfa-wipe
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "In every Microsoft 365 tenant your organisation runs or administers, audit device code sign-ins with the authentication protocol filter of the sign-in logs and, where no documented device needs the flow, create a Conditional Access policy with the Authentication flows condition set to Device code flow and Block access, starting in report-only mode and excluding emergency-access accounts and, where devices register through it, the Device Registration Service."
updates: []
migrated_from: null
---

The canton of Vaud said on 2026-11-04 that a phishing campaign is currently running in French-speaking Switzerland and that several organisations have already been affected (translated from French) ([Canton of Vaud, 2026-11-04](https://www.vd.ch/actualites/actualite/news/26768-campagne-de-phishing-ciblant-les-comptes-microsoft-365)). The messages can appear to come from a company or a known contact and invite the reader to view an invoice, open a document or verify information through a link; the campaign uses device-code phishing, which gets the victim to type a code on a genuine Microsoft authentication page and so gives the attackers fraudulent access to the Microsoft 365 account ([Canton of Vaud, 2026-11-04](https://www.vd.ch/actualites/actualite/news/26768-campagne-de-phishing-ciblant-les-comptes-microsoft-365)). The links printed in the notice combine a company-style name and a portal word on a workers.dev subdomain whose second label starts with a cloud-storage word and an identifier, and the canton says other addresses can be used too ([Canton of Vaud, 2026-11-04](https://www.vd.ch/actualites/actualite/news/26768-campagne-de-phishing-ciblant-les-comptes-microsoft-365)); workers.dev is the route assigned to every Cloudflare Worker ([Cloudflare Docs, 2026-09-22](https://developers.cloudflare.com/workers/configuration/routing/workers-dev/)). The notice names no actor, kit, count of organisations, sector or start date.

**Exposure:** any Microsoft 365 tenant whose users can complete the device code flow, which Microsoft describes as meant for devices without local input such as shared devices or digital signage and as a high-risk method that phishing can use ([Microsoft Learn, 2026-03-24](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows)).

**Detection:** mail, web proxy and DNS telemetry for links to workers.dev subdomains of the structure above; in the Entra sign-in logs, device code events found with the authentication protocol filter ([Microsoft Learn, 2026-03-24](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows)). Microsoft says protocol tracking persists through token refreshes, so later sign-ins in the same session can fall under an authentication-flows policy, and it records an original transfer method property in the activity details of the Conditional Access sign-in logs ([Microsoft Learn, 2026-03-24](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows)).

**Triage:** Microsoft documents device code sign-in for shared devices and signage; a device-code sign-in by a user who has no such device, soon after that user received a mailed link, falls outside that use ([Microsoft Learn, 2026-03-24](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-authentication-flows)).

**Defender takeaway:** where the tenant has no documented need for device code flow, Microsoft recommends blocking it with a Conditional Access policy, testing in report-only mode and auditing existing use first ([Microsoft Learn, 2026-04-07](https://learn.microsoft.com/en-us/entra/identity/conditional-access/policy-block-authentication-flows)). Tell users never to enter a Microsoft login code at a third party's request, and that anyone who has entered a code or validated an authentication request must call IT support at once, which is the canton's own instruction ([Canton of Vaud, 2026-11-04](https://www.vd.ch/actualites/actualite/news/26768-campagne-de-phishing-ciblant-les-comptes-microsoft-365)).
