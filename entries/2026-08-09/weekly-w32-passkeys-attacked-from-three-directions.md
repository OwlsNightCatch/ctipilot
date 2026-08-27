---
schema: 1
kind: research
horizon: strategic
title: >
  Three independent disclosures in one week attacked passkeys from both ends — the cryptography on
  a compromised endpoint and the enrolment on the phone — and the enterprise path, borrowing a
  signed-in session's Windows Hello key to authenticate to Entra ID, carries no CVE and no fix
headline: >
  Passkeys held against remote phishing this week and lost on both flanks: the compromised
  endpoint and the enrolment call
summary: >
  In ISO week 2026-W32 three separate pieces of work attacked the phishing-resistant authenticator
  that European public-sector identity programmes are standardising on. Unit 42 showed
  unprivileged endpoint malware forging Chrome synced-passkey assertions and stealing the
  security-domain secret that decrypts every synced passkey — a secret Google cannot rotate.
  Google's threat-intelligence group reported an extortion actor whose vishing pretext is an
  urgent FIDO2 passkey enrolment. At Black Hat USA 2026, Dirk-jan Mollema showed malware in an
  already-signed-in Windows session signing Entra ID assertions with the victim's Windows Hello
  key without any PIN or biometric prompt, exploiting a challenge that "is not bound to a session,
  a user or even a tenant". No CVE was assigned and the behaviour was left as it is, which Mollema
  characterises as a consequence of how Windows Hello for Business works. The common precondition
  throughout is endpoint compromise or a social-engineered enrolment, not a break in WebAuthn.
discovered_at: "2026-08-09T23:45:00Z"
updated_at: "2026-08-16T23:59:00Z"
event_date: 2026-08-05
run_id: 2026-08-09T2315Z-weekly
priority: high
immediate_action: null
tags:
  - identity
  - phishing
  - vulnerabilities
  - no-patch
  - info-disclosure
  - patch-available
regions:
  - global
  - europe
  - switzerland
sectors:
  - public-sector
  - finance
  - technology
entities:
  - "actor:unc6671"
  - "actor:helix-extortion"
  - "trend:passkey-webauthn-attack-surface-2026-08"
techniques:
  - T1556.006
  - T1606.002
  - T1550.001
  - T1098.005
  - T1566.004
  - T1552.001
  - T1078.004
affected_products:
  - Microsoft Entra ID
  - Windows Hello for Business
  - Google Password Manager
  - Google Chrome
  - Microsoft Windows
cves:
  - id: CVE-2026-34348
    cvss: 6.5
    type: info-disclosure
    vector: local
    auth: post-auth
    status:
      - patch-available
    affected: Windows event-log handling of WebAuthn assertions — see the Microsoft advisory
    fixed: July 2026 Windows updates
sources:
  - url: "https://dirkjanm.io/borrowing-windows-hello-keys/"
    publisher: Dirk-jan Mollema
    date: 2026-08-05
    role: primary
  - url: "https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/"
    publisher: Palo Alto Networks Unit 42
    date: 2026-08-03
    role: primary
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/"
    publisher: Google Threat Intelligence Group / Mandiant
    date: 2026-08-06
    role: primary
  - url: "https://thehackernews.com/2026/08/malware-can-abuse-windows-hello-for.html"
    publisher: The Hacker News
    date: 2026-08-07
    role: corroborating
  - url: "https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html"
    publisher: The Hacker News
    date: 2026-08-10
    role: primary
closed_sources: []
evidence:
  - quote: "The challenge is not bound to a session, a user or even a tenant, so we can request it on our attacker host and then use the WHFB key on the victim machine"
    publisher: Dirk-jan Mollema
  - quote: "calling these native functions from for example PowerShell does not prompt the user for a PIN or biometric authentication at all, but works based on cached data."
    publisher: Dirk-jan Mollema
  - quote: "SpecterOps says Windows stored past YubiKey signatures in cleartext where authenticated unprivileged users, including remote users, could read them."
    publisher: The Hacker News
  - quote: "The firm says chaining those signatures with weaknesses in Microsoft Entra ID's passkey validation allowed privileged-user impersonation despite policies requiring phishing-resistant multifactor authentication"
    publisher: The Hacker News
  - quote: "the firm now considers the full Windows-to-Entra vulnerability chain broken because Microsoft's July 2026 Windows updates make the WebAuthn assertions written to event logs unusable for replay attacks."
    publisher: The Hacker News
verification: multi-source
sourcing_note: >
  The CVE state of the Windows Hello work is stated explicitly because reporting around Black Hat
  blurs several talks together: Mollema's assertion-borrowing carries no CVE and, on his own
  account, was left as it is. Nothing here asserts that Microsoft assigned an identifier, shipped
  a fix, or made any statement — the outlet reporting the work records that its requests for
  comment were still outstanding.
confidence: high
references:
  - 2026-08-04/unit42-pass-ta-key-chrome-synced-passkey-forgery-sds-theft
  - 2026-08-07/unc6671-blackfile-multi-brand-passkey-vishing-aitm
weekly_section: weekly-research
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
updates:
  - at: "2026-08-16T23:59:00Z"
    run_id: 2026-08-16T2315Z-weekly
    type: update
    summary: >
      A prior weekly covered three simultaneous attacks on passkeys and recorded that a fourth thread
      had been dropped for want of a citable source. That thread is now documented. SpecterOps
      principal security researcher Michael Grafnetter presented Pass-the-Passkey at Black Hat USA
      2026 on 5 August; a write-up on 10 August reports that Windows stored past YubiKey signatures in
      cleartext where authenticated unprivileged users, including remote users, could read them, and
      that chaining those signatures with weaknesses in Entra ID's passkey validation allowed
      privileged-user impersonation despite policies requiring phishing-resistant multifactor
      authentication. The correction that matters is the outcome: the Windows side was fixed as
      CVE-2026-34348, vendor CVSS 6.5, in the July 2026 updates, SpecterOps now considers the full
      Windows-to-Entra chain broken because those updates make event-log assertions unusable for
      replay, and Microsoft says it has also applied mitigations on the relay-assertion side. What
      survives is the design lesson the three earlier threads already carried.
    fields:
      - affected_products
      - cves
      - evidence
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-16/weekly-w33-passkey-fourth-thread-documented-and-closed
migrated_from: null
---

Passkeys are the control European public-sector identity programmes are being pushed toward, on the correct premise that a credential which cannot be replayed to the wrong origin defeats remote phishing. Three independent disclosures inside ISO week 2026-W32 attacked that control from different directions, and the useful reading is neither that passkeys are broken nor that this is coincidence: it is that the residual attack surface has moved entirely onto the endpoint and the enrolment, and this week three separate parties published against it.

The enterprise path is the new one, and it is unpatched. At Black Hat USA 2026, Dirk-jan Mollema showed that malware running in an already-signed-in Windows session can call the Passport key-storage provider to sign data with the Windows Hello for Business private key — and that "calling these native functions from for example PowerShell does not prompt the user for a PIN or biometric authentication at all, but works based on cached data" ([Dirk-jan Mollema, 2026-08-05](https://dirkjanm.io/borrowing-windows-hello-keys/)). The second half is what makes it a remote-usable attack rather than a local curiosity: the WebAuthn challenge Entra ID issues "is not bound to a session, a user or even a tenant, so we can request it on our attacker host and then use the WHFB key on the victim machine," after which the signed assertion is replayed from the attacker's own host. Where the resulting token carries no device-ID claim, the attacker can register a device of their own and obtain a long-lived refresh token. No CVE was assigned and the behaviour was left as it is — a characterisation the reporting attributes to Mollema himself rather than to the vendor, noting that its own requests for comment to Microsoft and to Mollema were still outstanding at publication ([The Hacker News, 2026-08-07](https://thehackernews.com/2026/08/malware-can-abuse-windows-hello-for.html)). For a defender the practical position is the same either way: there is no patch to wait for and no identifier to track it by.

The consumer-synced path was published two days earlier and reaches further. Unit 42's three attacks against Google Password Manager's cloud-synced passkeys in Chrome on Windows all require only unprivileged malware already on the endpoint: driving the TPM-wrapped device identity key through standard Windows cryptography calls to sign a forged assertion with the User Verified flag unset, which succeeds against any relying party that does not validate that flag; forcing device re-enrolment and registering an attacker-generated user-verification key, because the cloud authenticator does not check attestation on new user-verification keys; and dumping the 32-byte security-domain secret from Chrome's memory during recovery, which decrypts every synced passkey private key ([Palo Alto Networks Unit 42, 2026-08-03](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/)). The third has no remediation path at the user's disposal — Google has no mechanism to rotate or revoke that secret.

The third direction needs no software flaw at all. Google's threat-intelligence group reports that UNC6671, the operator behind the BlackFile extortion brand and four later brands, runs an identity-centric intrusion chain whose current pretext is precisely the control being rolled out: a call to an employee's personal mobile impersonating the IT helpdesk, sometimes spoofing the real helpdesk number, demanding an urgent FIDO2 passkey or MFA re-enrolment into an adversary-in-the-middle panel ([Google Threat Intelligence Group, 2026-08-06](https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/)). Enrolment is the moment the phishing-resistance property does not yet exist, and an organisation that has just deployed passkeys is an organisation whose staff have been told to expect exactly such a call.

**Defender takeaway:** none of this argues for slowing a passkey rollout — every path here presupposes either code execution on the endpoint or a successful enrolment social-engineer, and against remote credential phishing the control still holds. It does argue for two things the rollout plan usually omits. First, treat enrolment and re-enrolment as the privileged operation they are: out-of-band identity proofing before any helpdesk-initiated MFA reset, device re-enrolment or passkey registration, with the same rigour a domain-admin grant would get. Second, do not assume the authenticator's protections extend to a compromised host — the hardening levers the research itself names are binding assertions to a device and session, requiring device-ID claims on FIDO2 tokens, and tightening who may register a device in the tenant.

**Triage:** the telemetry these attacks produce is authentication that succeeds, which is why the discriminator has to be positional rather than a failure signal. Look for a successful passkey or WebAuthn sign-in from a network location or device that has never previously held that key, and for Windows Hello key use with no corresponding interactive logon that would have prompted for a PIN or biometric — a genuine user's assertion is preceded by an unlock event, a borrowed one is not. On the tenant side, the sequence to alert on is a device-registration event followed closely by a long-lived refresh-token issuance for an account whose enrolment state changed within the preceding hours; legitimate device onboarding produces the same events, but not usually within minutes of a helpdesk-initiated credential reset.

## Update — 2026-08-16T23:59:00Z

The prior weekly covered three independent attacks on passkeys — forged Chrome synced-passkey assertions, a vishing pretext built around urgent FIDO2 enrolment, and borrowing a signed-in session's Windows Hello key to authenticate to Entra ID — and dropped a fourth because the sentence naming it could not be traced to any source that ran in that window. The delta is that the fourth thread now has a citable account, and it does not read the way an unsourced fragment implied.

SpecterOps principal security researcher Michael Grafnetter presented the firm's Pass-the-Passkey research at Black Hat USA 2026 on 5 August. The mechanism is distinct from the Windows Hello work the prior entry already carried: rather than using a hardware-bound key from a live session, it starts from stored material. "SpecterOps says Windows stored past YubiKey signatures in cleartext where authenticated unprivileged users, including remote users, could read them," and "The firm says chaining those signatures with weaknesses in Microsoft Entra ID's passkey validation allowed privileged-user impersonation despite policies requiring phishing-resistant multifactor authentication" ([The Hacker News, 2026-08-10](https://thehackernews.com/2026/08/new-passkey-attacks-can-recover-synced.html)). Two properties make that worth recording even now that it is fixed. The read required no elevation — an ordinary authenticated account, including one arriving over a remote session, was sufficient. And the replay succeeded against a policy that was doing exactly what it was configured to do, because the assertion it accepted was genuine; nothing about the cryptography failed.

The correction is the outcome, and it runs opposite to the direction an open-ended reading would suggest. Microsoft's Windows-side flaw is tracked as CVE-2026-34348 with a vendor CVSS of 6.5 and was fixed in the July 2026 updates — before the research was presented. SpecterOps told the outlet it has not retested the Entra side since June, but "the firm now considers the full Windows-to-Entra vulnerability chain broken because Microsoft's July 2026 Windows updates make the WebAuthn assertions written to event logs unusable for replay attacks," and Microsoft stated it has also applied mitigations for the reported issue involving passkey relay assertions. So the honest status is closed on the researcher's own assessment, not open.

**Defender takeaway:** for an estate standing up passkeys, the operational item is small and specific — confirm the July 2026 Windows updates are deployed on any host where FIDO2 security keys are used, because that is the update that stops the cached assertions from being replayable, and it predates the public disclosure by a month. The durable lesson is the one the prior entry drew across the other three threads and this fourth one now reinforces from a different angle: every one of these attacks left WebAuthn itself intact and went after the material around it — the synced-passkey secret, the enrolment call, the signed-in session, and here the log the platform wrote about a successful authentication. Phishing-resistant is a property of the protocol against a remote phisher; it is not a property of the endpoint that holds the authenticator or of the records that endpoint keeps. A programme that treats passkey rollout as retiring the endpoint-compromise problem is drawing the wrong conclusion from the right technology.

**Triage:** where an estate has not yet deployed the July updates, the observable is reading rather than writing — access to Windows event-log records containing WebAuthn or FIDO2 assertion data by an account that is neither an administrator nor a monitoring agent, and particularly from a remote session. That is worth separating from the ordinary case carefully: log collection agents and administrators read these channels constantly and legitimately, so the account class and the session type are the discriminators, not the read itself. On the Entra side, the sign-in telemetry shape that would correspond to a successful replay is an authentication satisfying a passkey or FIDO2 requirement for a user from a device or session with no prior passkey-registration history for that user — a mismatch between the authentication method claimed and the registration record that should underlie it.
