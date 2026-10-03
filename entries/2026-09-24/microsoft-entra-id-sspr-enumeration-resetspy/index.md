---
schema: 1
kind: research
title: "Microsoft's public Entra ID password-reset portal leaks account existence, registered MFA methods and likely-admin status to any unauthenticated visitor"
headline: "A public tool automates bulk enumeration of Entra ID accounts, their MFA methods and their admin status through Microsoft's own password-reset portal"
summary: >
  LevelBlue (Trustwave) SpiderLabs documents that Microsoft's public,
  unauthenticated Self-Service Password Reset (SSPR) portal at
  passwordreset.microsoftonline.com discloses, via a hidden state field in its
  own response, whether a submitted email address belongs to a real Entra ID
  account, which second-factor methods that account has registered, and — because
  Microsoft enforces SSPR for administrators regardless of tenant policy —
  whether the account is likely privileged. The researcher released a public
  automation tool, ResetSpy, and Microsoft removed the portal's visual CAPTCHA
  in August 2026 in favor of backend throttling alone.
discovered_at: "2026-09-24T04:40:00Z"
updated_at: null
event_date: "2026-09-23"
run_id: 2026-09-24T0405Z-intel
priority: notable
immediate_action: null
tags: [identity, vulnerabilities, info-disclosure]
regions: [global]
sectors: [public-sector]
entities: ["product:microsoft-entra-id", "tool:resetspy"]
techniques: [T1087.004]
affected_products: ["Microsoft Entra ID"]
cves: []
sources:
  - url: "https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal"
    publisher: "LevelBlue (Trustwave) SpiderLabs"
    date: "2026-09-23"
    role: primary
closed_sources: []
evidence:
  - quote: "Importantly, every non-\"ViewUserIdentifierVerification\" response — including \"SSPR_0011\", \"SSPR_0013\", and the guest/federated not-available response — is confirmation that the account exists. The server only reaches those policy checks after successfully resolving the username in the directory."
    publisher: "LevelBlue"
  - quote: "Microsoft enforces SSPR for administrator accounts regardless of the tenant-wide SSPR policy. If an organization has disabled SSPR for standard users, standard accounts return \"ViewSsprNotEnabledInUserPolicy\" (SSPR_0011). Admin accounts bypass this check entirely and proceed to method enumeration regardless."
    publisher: "LevelBlue"
  - quote: "As of August 2026, Microsoft removed this CAPTCHA entirely and replaced it with backend throttling and behavior-based abuse detection"
    publisher: "LevelBlue"
verification: single-source
sourcing_note: "Single technical source (LevelBlue SpiderLabs); the underlying portal behaviour is independently checkable by any reader against Microsoft's own live SSPR portal and documented SSPR error codes, but no second party has published an independent assessment of this specific finding as of 2026-09-24."
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Scope SSPR to a specific, minimal security group rather than tenant-wide in every Entra ID tenant, and enforce phishing-resistant MFA (FIDO2 or certificate-based) on every administrator and privileged role — Microsoft cannot let admin accounts opt out of SSPR-based enumeration at the platform level, so a stronger factor is the only control that neutralises what the portal reveals about them."
updates: []
migrated_from: null
---

Microsoft's Self-Service Password Reset (SSPR) portal, publicly reachable at passwordreset.microsoftonline.com with no prior authentication, discloses more than it is meant to about the accounts behind it ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). Submitting an email address triggers an ASP.NET UpdatePanel POST, and the server's reply carries a hidden `CurrentViewName` field that tells an attacker exactly what happened server-side: `ViewMultigateUserControl` means the account exists and SSPR advanced to method selection, while a genuine not-found bounces back to `ViewUserIdentifierVerification`. Every other named view — including the documented error codes for "SSPR not enabled for this user" (SSPR_0011) and "not a member of the scoped access group" (SSPR_0013) — still confirms the account exists, because the server only reaches those policy checks after resolving the username in the directory: "The server only reaches those policy checks after successfully resolving the username in the directory" ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). For an account that reaches the method-selection screen, the response HTML lists every registered second factor as visible radio buttons, with unregistered methods present in the DOM but hidden — so an attacker also learns whether a target relies on an authenticator app, SMS, or a more easily phished alternate-email one-time code.

The technique's sharpest edge is administrator identification. Microsoft enforces SSPR for admin accounts regardless of the tenant-wide SSPR policy, so in a tenant that has disabled SSPR for standard users, any account that still reaches method selection is very likely a privileged role account, and its registered factors are exposed the same way: "Admin accounts bypass this check entirely and proceed to method enumeration regardless" ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). This turns a list of candidate email addresses harvested from a company website, LinkedIn, or a data breach into a confirmed target list, ranked by which accounts have the weakest second factor, before any credential attack begins. Microsoft removed the portal's visual CAPTCHA in August 2026, replacing it with backend throttling and behavioural abuse detection rather than a challenge the user must solve ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). The researcher released a public automation tool, ResetSpy, that scripts bulk lookups with rotating user agents and randomised timing to reduce fingerprinting.

**Detection:** Entra ID / Azure AD self-service-password-reset audit events are the telemetry class — specifically SSPR activity records carrying a named error status (such as the "not a member of the password reset group" condition) recurring across many distinct usernames from a limited source population in a short window, with no subsequent completed reset. **Triage:** a genuine user forgetting a password generates one SSPR lookup that is normally followed by a completed reset; a burst of lookups against many usernames with no completions is the anomalous pattern the volume/velocity discriminator is built on, not the existence of lookups themselves.

**Defender takeaway:** scope SSPR to a specific security group rather than tenant-wide to shrink the enumerable population, remove alternate-email-OTP and security-question options from the permitted SSPR methods, and enforce phishing-resistant MFA on every privileged role — since Microsoft cannot let admin accounts opt out of the underlying enumeration, a stronger factor on those accounts is the control that actually removes the value of what the technique reveals.
