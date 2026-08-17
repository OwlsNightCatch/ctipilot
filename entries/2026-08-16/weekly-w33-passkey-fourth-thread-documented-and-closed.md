---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "UPDATE — the fourth passkey attack thread this pipeline could not source last week is now documented, and it closed: Windows cached YubiKey assertions in cleartext where any authenticated user could read them, and the July updates broke the chain"
headline: "Pass-the-Passkey gets its sourcing — a readable event-log cache replayed into Entra ID, fixed as CVE-2026-34348 before the research went public"
summary: >
  A prior weekly covered three simultaneous attacks on passkeys and recorded that a fourth thread had been
  dropped for want of a citable source. That thread is now documented. SpecterOps principal security
  researcher Michael Grafnetter presented Pass-the-Passkey at Black Hat USA 2026 on 5 August; a write-up on
  10 August reports that Windows stored past YubiKey signatures in cleartext where authenticated
  unprivileged users, including remote users, could read them, and that chaining those signatures with
  weaknesses in Entra ID's passkey validation allowed privileged-user impersonation despite policies
  requiring phishing-resistant multifactor authentication. The correction that matters is the outcome: the
  Windows side was fixed as CVE-2026-34348, vendor CVSS 6.5, in the July 2026 updates, SpecterOps now
  considers the full Windows-to-Entra chain broken because those updates make event-log assertions unusable
  for replay, and Microsoft says it has also applied mitigations on the relay-assertion side. What survives
  is the design lesson the three earlier threads already carried.
discovered_at: "2026-08-16T23:59:00Z"
event_date: "2026-08-10"
run_id: 2026-08-16T2315Z-weekly
priority: notable
immediate_action: null
tags: [identity, vulnerabilities, info-disclosure, patch-available]
regions: [europe, global]
sectors: [public-sector, finance, technology]
entities:
  - trend:passkey-webauthn-attack-surface-2026-08
techniques: [T1552.001, T1550.001, T1556.006, T1078.004]
affected_products: ["Microsoft Windows", "Microsoft Entra ID"]
cves:
  - id: CVE-2026-34348
    cvss: 6.5
    type: info-disclosure
    vector: local
    auth: post-auth
    status: [patch-available]
    affected: "Windows event-log handling of WebAuthn assertions — see the Microsoft advisory"
    fixed: "July 2026 Windows updates"
sources:
  - url: "https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html"
    publisher: "The Hacker News"
    date: "2026-08-10"
    role: primary
closed_sources: []
evidence:
  - quote: "SpecterOps says Windows stored past YubiKey signatures in cleartext where authenticated unprivileged users, including remote users, could read them."
    publisher: "The Hacker News"
  - quote: "The firm says chaining those signatures with weaknesses in Microsoft Entra ID's passkey validation allowed privileged-user impersonation despite policies requiring phishing-resistant multifactor authentication"
    publisher: "The Hacker News"
  - quote: "the firm now considers the full Windows-to-Entra vulnerability chain broken because Microsoft's July 2026 Windows updates make the WebAuthn assertions written to event logs unusable for replay attacks."
    publisher: "The Hacker News"
verification: single-source
sourcing_note: >
  Single-source by design rather than by omission. The prior weekly dropped this thread because the sentence
  attributing it carried no citation; the correction rests on one outlet's write-up, which quotes SpecterOps
  and carries Microsoft's own response directly. The researcher's own talk page was located but its
  publication date could not be established from the page metadata, so it is not cited here rather than
  being cited with an inferred date. Treated as single-source with the outlet named at every claim; the
  CVE identifier and its vendor CVSS come from the same write-up.
confidence: medium
update_of: 2026-08-09/weekly-w32-passkeys-attacked-from-three-directions
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-08-09):** the prior weekly covered three independent attacks on passkeys — forged Chrome synced-passkey assertions, a vishing pretext built around urgent FIDO2 enrolment, and borrowing a signed-in session's Windows Hello key to authenticate to Entra ID — and dropped a fourth because the sentence naming it could not be traced to any source that ran in that window. The delta is that the fourth thread now has a citable account, and it does not read the way an unsourced fragment implied.

SpecterOps principal security researcher Michael Grafnetter presented the firm's Pass-the-Passkey research at Black Hat USA 2026 on 5 August. The mechanism is distinct from the Windows Hello work the prior entry already carried: rather than using a hardware-bound key from a live session, it starts from stored material. "SpecterOps says Windows stored past YubiKey signatures in cleartext where authenticated unprivileged users, including remote users, could read them," and "The firm says chaining those signatures with weaknesses in Microsoft Entra ID's passkey validation allowed privileged-user impersonation despite policies requiring phishing-resistant multifactor authentication" ([The Hacker News, 2026-08-10](https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html)). Two properties make that worth recording even now that it is fixed. The read required no elevation — an ordinary authenticated account, including one arriving over a remote session, was sufficient. And the replay succeeded against a policy that was doing exactly what it was configured to do, because the assertion it accepted was genuine; nothing about the cryptography failed.

The correction is the outcome, and it runs opposite to the direction an open-ended reading would suggest. Microsoft's Windows-side flaw is tracked as CVE-2026-34348 with a vendor CVSS of 6.5 and was fixed in the July 2026 updates — before the research was presented. SpecterOps told the outlet it has not retested the Entra side since June, but "the firm now considers the full Windows-to-Entra vulnerability chain broken because Microsoft's July 2026 Windows updates make the WebAuthn assertions written to event logs unusable for replay attacks," and Microsoft stated it has also applied mitigations for the reported issue involving passkey relay assertions. So the honest status is closed on the researcher's own assessment, not open.

**Defender takeaway:** for an estate standing up passkeys, the operational item is small and specific — confirm the July 2026 Windows updates are deployed on any host where FIDO2 security keys are used, because that is the update that stops the cached assertions from being replayable, and it predates the public disclosure by a month. The durable lesson is the one the prior entry drew across the other three threads and this fourth one now reinforces from a different angle: every one of these attacks left WebAuthn itself intact and went after the material around it — the synced-passkey secret, the enrolment call, the signed-in session, and here the log the platform wrote about a successful authentication. Phishing-resistant is a property of the protocol against a remote phisher; it is not a property of the endpoint that holds the authenticator or of the records that endpoint keeps. A programme that treats passkey rollout as retiring the endpoint-compromise problem is drawing the wrong conclusion from the right technology.

**Triage:** where an estate has not yet deployed the July updates, the observable is reading rather than writing — access to Windows event-log records containing WebAuthn or FIDO2 assertion data by an account that is neither an administrator nor a monitoring agent, and particularly from a remote session. That is worth separating from the ordinary case carefully: log collection agents and administrators read these channels constantly and legitimately, so the account class and the session type are the discriminators, not the read itself. On the Entra side, the sign-in telemetry shape that would correspond to a successful replay is an authentication satisfying a passkey or FIDO2 requirement for a user from a device or session with no prior passkey-registration history for that user — a mismatch between the authentication method claimed and the registration record that should underlie it.
