---
schema: 1
kind: incident
title: "Dropbox account takeover via a federated Lenovo-ID trust gap: roughly 5,000 accounts accessed with no password and no 2FA bypass needed"
headline: "A broken email-verification check on one identity provider let attackers silently bind to any Dropbox account with 2FA disabled"
summary: >
  Dropbox confirmed to Reuters (2026-09-02) that unauthorized parties accessed roughly 5,000
  accounts between 4 and 21 August 2026 by abusing its "Continue with Lenovo" single sign-on
  integration. Lenovo's own ID registration flow failed to verify that a registrant controlled the
  email address supplied, letting an attacker register a Lenovo ID under a victim's email with no
  access to that inbox; Dropbox then implicitly trusted the asserted email claim to bind a session
  to the matching account whenever that account had no two-factor authentication enabled.
discovered_at: "2026-09-02T05:20:00Z"
updated_at: null
event_date: "2026-09-02"
run_id: 2026-09-02T0411Z-intel
priority: notable
immediate_action: null
tags: [identity, data-breach]
regions: [global]
sectors: [technology]
entities:
  - "incident:dropbox-lenovo-id-sso-account-takeover-2026-08"
techniques: [T1199, "T1078.004"]
affected_products: ["Dropbox"]
cves: []
sources:
  - url: "https://9to5mac.com/2026/09/01/dropbox-login-breach-seemingly-caused-by-egregious-authentication-failure/"
    publisher: "9to5Mac"
    date: "2026-09-01"
    role: primary
  - url: "https://www.freemalaysiatoday.com/category/business/2026/09/02/dropbox-says-about-5-000-accounts-compromised-in-august-hack"
    publisher: "Reuters (via Free Malaysia Today)"
    date: "2026-09-02"
    role: primary
  - url: "https://www.heise.de/news/Fremde-Dropbox-Konten-ueber-Lenovo-ID-zugaenglich-11437565.html"
    publisher: "heise Security"
    date: "2026-09-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Dropbox told Reuters that it identified unauthorized access affecting accounts linked to a Lenovo ID that did not have its two-factor authentication enabled, prompting the company to terminate all sessions authenticated through a Lenovo ID."
    publisher: "Reuters (via Free Malaysia Today)"
  - quote: "Lenovo identified a \"legacy integration\" between Lenovo ID and Dropbox that \"could be used to improperly authenticate certain Dropbox accounts\". The company said its own customers were not affected and that an investigation was ongoing."
    publisher: "Reuters (via Free Malaysia Today), quoting Lenovo"
  - quote: "Dropbox partners with Lenovo as an identity provider so that users can log in to their Dropbox accounts using verified Lenovo IDs. While you may not have an existing Lenovo ID, our investigation determined that an issue with Lenovo's email verification process allowed an unauthorized party to register a Lenovo ID using your email address and then use that Lenovo ID to log into the Dropbox account associated with that email address."
    publisher: "Dropbox, in its notification email to affected users (via 9to5Mac)"
  - quote: "So konnte sich der Täter im Zeitraum 4. bis 21. August in rund 5.000 Dropbox-Konten frei umsehen. In weniger als einem Drittel der Fälle soll er Dateien gefunden haben, die ausreichend interessant erschienen, um sie herunterzuladen. (translated from German: The perpetrator was thus able to freely browse around 5,000 Dropbox accounts between 4 and 21 August. In fewer than a third of cases, they are said to have found files interesting enough to download.)"
    original: "So konnte sich der Täter im Zeitraum 4. bis 21. August in rund 5.000 Dropbox-Konten frei umsehen. In weniger als einem Drittel der Fälle soll er Dateien gefunden haben, die ausreichend interessant erschienen, um sie herunterzuladen."
    publisher: "heise Security (Daniel AJ Sokolov)"
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Dropbox confirmed to Reuters on 2026-09-02 that unauthorized parties accessed roughly 5,000 Dropbox accounts between 4 and 21 August 2026 by abusing "Continue with Lenovo," one of several third-party identity-provider login options Dropbox offers alongside Google and Apple ([Reuters via Free Malaysia Today, 2026-09-02](https://www.freemalaysiatoday.com/category/business/2026/09/02/dropbox-says-about-5-000-accounts-compromised-in-august-hack)). The root cause is a broken trust chain spanning both parties. On Lenovo's side, the ID registration flow failed to verify that a registrant actually controlled the email address they supplied, so an attacker could register a brand-new Lenovo ID under a victim's known or guessed email address with no access to that inbox at all. On Dropbox's side, the relying-party logic then implicitly trusted the identity provider's asserted email claim to bind a login session to the matching Dropbox account — with no password prompt, no step-up challenge and no "link this new identity?" consent screen — whenever that account had Dropbox's own two-factor authentication disabled: "an issue with Lenovo's email verification process allowed an unauthorized party to register a Lenovo ID using your email address and then use that Lenovo ID to log into the Dropbox account associated with that email address" ([Dropbox notification email, via 9to5Mac, 2026-09-01](https://9to5mac.com/2026/09/01/dropbox-login-breach-seemingly-caused-by-egregious-authentication-failure/)).

Once inside, attackers could browse account contents freely; per Dropbox, files were viewed or downloaded in fewer than a third of the roughly 5,000 affected accounts ([heise Security, 2026-09-02](https://www.heise.de/news/Fremde-Dropbox-Konten-ueber-Lenovo-ID-zugaenglich-11437565.html)). Reporting describes bulk, low-effort targeting rather than hand-picked victims — one reclaimed rogue Lenovo ID carried the throwaway display name "John Madden," the late NFL broadcaster ([9to5Mac, 2026-09-01](https://9to5mac.com/2026/09/01/dropbox-login-breach-seemingly-caused-by-egregious-authentication-failure/)). Dropbox has since terminated every session authenticated via a Lenovo ID, severed the Lenovo–Dropbox account-linking integration entirely, and changed its system so a user's existing Dropbox password must now be entered before any Lenovo-ID-authenticated session can be established; it has reported the incident to data-protection regulators ([Reuters via Free Malaysia Today, 2026-09-02](https://www.freemalaysiatoday.com/category/business/2026/09/02/dropbox-says-about-5-000-accounts-compromised-in-august-hack)). Lenovo separately confirmed the "legacy integration... could be used to improperly authenticate certain Dropbox accounts" and states its own customer accounts were not affected ([Reuters via Free Malaysia Today, 2026-09-02](https://www.freemalaysiatoday.com/category/business/2026/09/02/dropbox-says-about-5-000-accounts-compromised-in-august-hack)).

**Defender takeaway:** this is a design-pattern lesson, not a currently exploitable vulnerability — Dropbox has already remediated. The generalizable failure transfers directly to any organization offering "sign in with a third-party IdP": a relying party must never treat an identity provider's asserted email claim as sufficient on its own to silently bind or reuse an existing account. The first time a new external identity is linked to an account, require that account's own credential, or an explicit and logged consent step, regardless of how trusted the identity provider itself is believed to be. This applies equally to public-sector portals that federate login through a third-party IdP or a citizen e-ID scheme: the security of the relying party's account-linking logic cannot be assumed from the identity provider's own reputation.

**Triage:** a legitimate "Continue with Lenovo" (or any federated-IdP) login is ordinary traffic and is not distinguishable from this abuse pattern at the network layer — the discriminator lives in the relying party's own session and account-linking logs. The signal is a session established via a third-party IdP for an account that never previously had that IdP linked, immediately following a fresh registration on the IdP side, landing on an account with no second factor configured.
