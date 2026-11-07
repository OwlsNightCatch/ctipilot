---
schema: 1
kind: research
title: "Microsoft's public Entra ID password-reset portal leaks account existence, registered MFA methods and likely-admin status to any unauthenticated visitor"
headline: "A public tool bulk-enumerates Entra ID accounts and their MFA methods through Microsoft's own password-reset portal"
summary: >
  LevelBlue (Trustwave) SpiderLabs documents that Microsoft's public,
  unauthenticated Self-Service Password Reset (SSPR) portal at
  passwordreset.microsoftonline.com discloses, via a hidden state field in its
  own response, whether a submitted email address belongs to a real Entra ID
  account, which second-factor methods that account has registered, and, because
  Microsoft enforces SSPR for administrators regardless of tenant policy,
  whether the account is likely privileged. The researcher released a public
  automation tool, ResetSpy, and Microsoft removed the portal's visual CAPTCHA
  in August 2026 in favor of backend throttling and behavior-based abuse
  detection.
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
actions: []
updates:
  - at: "2026-09-30T07:03:26Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    internal: true
    summary: >
      The single action restated the Defender takeaway's hardening advice, including generic
      phishing-resistant MFA guidance, rather than a task the team starts now. It is removed, and
      the hardening guidance stays in the takeaway.
    fields: [actions]
  - at: "2026-10-11T14:10:34Z"
    run_id: 2026-10-11T1307Z-audit
    type: correction
    summary: >
      The takeaway recommended scoping SSPR to a group without LevelBlue's own caveat that scoped SSPR leaks more about the accounts inside the group; the caveat is added. Microsoft replaced the CAPTCHA with backend throttling and behavior-based abuse detection, not throttling alone; LevelBlue says a privileged account is 'likely', not 'very likely'; the detection, triage and takeaway lines gain their LevelBlue citation.
    fields: [summary, body]
  - at: "2026-10-21T08:18:20Z"
    run_id: 2026-10-21T0800Z-audit
    type: improvement
    summary: >
      The headline no longer says ResetSpy enumerates admin status: the tool reports account existence,
      registered methods, their strength and the SSPR policy state, and likely administrators are inferred
      from that policy state. The takeaway now says scoping SSPR to a group limits method disclosure to
      in-group accounts and administrators without stopping existence enumeration, instead of presenting
      it as shrinking the enumerable population.
    fields: [body, headline, summary]
migrated_from: null
---

Microsoft's Self-Service Password Reset (SSPR) portal, publicly reachable at passwordreset.microsoftonline.com with no prior authentication, discloses more than it is meant to about the accounts behind it ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). Submitting an email address triggers an ASP.NET UpdatePanel POST, and the server's reply carries a hidden `CurrentViewName` field that tells an attacker exactly what happened server-side: `ViewMultigateUserControl` means the account exists and SSPR advanced to method selection, while a genuine not-found bounces back to `ViewUserIdentifierVerification`. Every other named view, including the documented error codes SSPR_0011 (no password reset policy defined for the user) and SSPR_0013 (the user is not a member of the group enabled for SSPR), still confirms the account exists, because the server only reaches those policy checks after resolving the username in the directory: "The server only reaches those policy checks after successfully resolving the username in the directory" ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). For an account that reaches the method-selection screen, the response HTML lists every registered second factor as visible radio buttons, with unregistered methods present in the DOM but hidden, so an attacker also learns whether a target relies on an authenticator app, SMS, or a more easily phished alternate-email one-time code.

The technique's sharpest edge is administrator identification. Microsoft enforces SSPR for admin accounts regardless of the tenant-wide SSPR policy, so in a tenant that has disabled SSPR for standard users, any account that still reaches method selection is likely a privileged role account, and its registered factors are exposed the same way: "Admin accounts bypass this check entirely and proceed to method enumeration regardless" ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). This turns a list of candidate email addresses harvested from a company website, LinkedIn, or a data breach into a confirmed target list, ranked by which accounts have the weakest second factor, before any credential attack begins. Microsoft removed the portal's visual CAPTCHA in August 2026, replacing it with backend throttling and behavioural abuse detection rather than a challenge the user must solve ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). The researcher released a public automation tool, ResetSpy, that scripts bulk lookups with rotating user agents and randomised timing to reduce fingerprinting.

**Detection:** Entra ID / Azure AD self-service-password-reset audit events are the telemetry class, specifically SSPR activity records with status failures such as "user is not member of the password reset users group", and bulk enumeration attempts: many requests in a short window across varied usernames with no subsequent completed reset ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). **Triage:** a genuine user forgetting a password generates one SSPR lookup that is normally followed by a completed reset; a burst of lookups against many usernames with no completions is the anomalous pattern the volume/velocity discriminator is built on, not the existence of lookups themselves ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)).

**Defender takeaway:** scoping SSPR to a specific security group rather than tenant-wide limits method disclosure to the accounts inside the group and to administrators, but it does not stop existence enumeration, and it exposes the registered methods, or the empty method list, of every in-scope account ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). Remove alternate-email-OTP and security-question options from the permitted SSPR methods, and enforce phishing-resistant MFA on every privileged role: Microsoft enforces SSPR on admin accounts and this cannot be disabled, so a stronger factor on those accounts is the control that raises the cost of exploiting what the technique reveals ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)).

## Correction — 2026-10-11T14:10:34Z

LevelBlue recommends scoping SSPR to a security group but also finds that "Scoped SSPR, counterintuitively, leaks more information about the accounts that are inside the group than a blanket disabled policy does", because those accounts proceed to method enumeration ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). Scoping limits method disclosure for accounts outside the group; every account still has its existence confirmed, and accounts inside the group, including those with no registered method, are exposed in full.

## Improvement — 2026-10-21T08:18:20Z

ResetSpy does not report administrator status. For each target it returns whether the account exists, which SSPR verification methods are registered, whether those methods amount to a meaningful second factor or are weak-only, and the SSPR policy state ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)). Likely administrators are an inference from that policy state: in a tenant that has disabled SSPR for standard users, an account that still reaches method selection "is likely a privileged role account" ([LevelBlue SpiderLabs, 2026-09-23](https://www.levelblue.com/blogs/spiderlabs-blog/enumerating-users-and-mfa-via-microsofts-password-reset-portal)).
