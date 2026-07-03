---
schema: 1
kind: incident
horizon: operational
title: Dashlane discloses TOTP brute-force that downloaded encrypted vaults of fewer than 20 users
headline: Dashlane discloses TOTP brute-force that downloaded encrypted vaults of fewer than 20 users
summary: "Dashlane discloses a TOTP brute-force that downloaded the encrypted vaults of fewer than 20 personal-plan users — attackers exhausted the bounded six-digit TOTP keyspace to register a new trusted device, the same new-device-registration kill chain as the 2022 LastPass breach. Vaults stay master-password-encrypted but face offline cracking (TechCrunch, 2026-06-02)."
discovered_at: "2026-06-03T05:00:01Z"
event_date: 2026-06-02
run_id: 2026-06-03-ee0eae61
priority: high
immediate_action: null
tags:
  - identity
  - data-breach
  - phishing
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://techcrunch.com/2026/06/02/password-manager-dashlane-says-hackers-stole-some-customers-password-vaults/"
    publisher: TechCrunch
    role: primary
  - url: "https://thehackernews.com/2026/06/dashlane-discloses-brute-force-attack.html"
    publisher: The Hacker News
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/dashlane-password-manager-users-locked-out-by-brute-force-attacks/"
    publisher: BleepingComputer
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-03.md
---

Dashlane disclosed (on 2026-06-01, for an attack dated 2026-05-31) that an external actor brute-forced its TOTP second factor to download the encrypted vaults of fewer than 20 personal-plan accounts ([TechCrunch, 2026-06-02](https://techcrunch.com/2026/06/02/password-manager-dashlane-says-hackers-stole-some-customers-password-vaults/)). The technique abuses the bounded TOTP keyspace — one million six-digit codes per 30-second window — by submitting a high volume of attempts against the new-device-registration endpoint, where a single correct code registers a new trusted device that can then pull the vault ([The Hacker News, 2026-06-02](https://thehackernews.com/2026/06/dashlane-discloses-brute-force-attack.html)). Dashlane's rate-limiting locked the targeted accounts (since restored) and the company states its infrastructure was not compromised; vault contents remain encrypted under the user's master password, which Dashlane does not store, but weak master passwords now face offline cracking ([BleepingComputer, 2026-06-01](https://www.bleepingcomputer.com/news/security/dashlane-password-manager-users-locked-out-by-brute-force-attacks/)). This is structurally the same new-device-registration kill chain that enabled vault theft in the 2022 LastPass breach.

**Defender takeaway:** TOTP is a shared-secret factor with a small enumerable keyspace; for credential-manager and high-value account authentication, migrate to phishing-resistant FIDO2/WebAuthn or passkeys, which are not brute-forceable, and enforce aggressive per-account back-off plus alerting on rapid sequential authentication attempts carrying different OTP values from one source.
