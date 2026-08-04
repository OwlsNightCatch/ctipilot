---
schema: 1
kind: research
horizon: operational
title: "Pass-ta-key: unprivileged malware forges Chrome synced-passkey assertions, registers its own user-verification key, and can steal the master secret that decrypts every passkey"
headline: "Unit 42 shows three ways endpoint malware defeats Google synced passkeys without elevation, unlock or user interaction — and one of them cannot be revoked"
summary: >
  Unit 42 published three attacks (2026-08-03) against Google Password Manager's cloud-synced passkeys in Chrome on
  Windows with a TPM, all requiring only unprivileged malware already on the endpoint. Pass-ta-key drives the
  TPM-wrapped device identity key through standard Windows CNG calls to sign a forged WebAuthn assertion with the
  User Verified flag unset, which succeeds against any relying party that does not validate that flag. Silver
  Pass-ta-key forces device re-enrolment and registers an attacker-generated user-verification key, because the cloud
  authenticator does not check attestation on new UV keys — producing reusable access that sets the flag. Golden
  Pass-ta-key dumps the 32-byte security domain secret from Chrome's memory during recovery and decrypts every synced
  passkey private key; Google has no way to rotate or revoke that secret.
discovered_at: "2026-08-04T04:47:00Z"
event_date: "2026-08-03"
run_id: 2026-08-04T0411Z-intel
priority: high
immediate_action: null
tags: [identity, vulnerabilities, auth-bypass, infostealer, no-patch]
regions: [global]
sectors: [public-sector, finance, technology]
entities: []
techniques: [T1555.003, T1552.004, T1111, T1606]
affected_products: ["Google Password Manager", "Google Chrome"]
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-08-03"
    role: primary
  - url: "https://thehackernews.com/2026/08/google-password-manager-attacks-could.html"
    publisher: "The Hacker News"
    date: "2026-08-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Unlike a legitimate user flow that requires user interaction and device unlock, this attack shows how malware can obtain the required signature silently, without user consent, biometrics, device unlock or elevated privileges."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "The cloud authenticator does not validate the attestation of newly registered UV keys to verify whether they originate from secure hardware."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "In Google’s current implementation, there is no way to rotate or revoke the SDS, meaning all current and future synced passkeys remain protected by the same master key."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "In our testing, we identified relying parties that accepted authentication because they did not properly validate the UV flag."
    publisher: "Palo Alto Networks Unit 42"
verification: multi-source
sourcing_note: >
  No CVE has been assigned to any of the three variants. Unit 42 states it disclosed all three responsibly; Google has
  removed the master secret from Chrome's FIDO device log but, per Unit 42, the secret still reaches the client and the
  attestation and revocation gaps remain open at publication.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: identity-infra
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On every relying party your organisation operates that accepts passkeys, set userVerification to required AND verify the User Verified bit in the returned authenticator data before accepting the assertion — this is the one control the relying party owns, and it closes the base Pass-ta-key variant outright."
migrated_from: null
---

Passkeys remove the shared secret, which removes phishing, replay and credential stuffing from the attacker's toolkit. Unit 42's research, published 2026-08-03, is about what replaces them: three attacks that leave the cryptography intact and instead abuse the trust a cloud-synced passkey system places in the client device, its onboarding flow and its recovery flow. The scope is specific — Google Password Manager in Chrome on Windows on machines with a TPM — and the precondition is unremarkable: malware already running as the logged-in user, with no elevation ([Unit 42, 2026-08-03](https://unit42.paloaltonetworks.com/passwordless-authentication-security-risks/)).

**Reconnaissance.** Chrome stores synced passkeys as proto-encoded `WebauthnCredentialSpecifics` records in its sync database under `%LocalAppData%\Google\Chrome\User Data\<Profile>\Sync Data\LevelDB`, and Unit 42 states plainly that "Accessing these records does not require elevated privileges." Reading them tells an attacker which services the victim protects with passkeys, the associated usernames and credential identifiers, and the encrypted private key — a target list before any authentication is attempted.

**Pass-ta-key — forging the assertion.** Chrome proves device possession to Google's cloud authenticator with a hardware-backed identity key, and the way Chrome handles that key is what the attack turns on. Chrome creates the TPM key without a name so it is never persisted inside the TPM, then exports it as an `NCRYPT_OPAQUE_KEY_BLOB` — encrypted by a TPM-resident key — and stores the result as `wrapped_identity_private_key` in the `passkey_enclave_state` file. Malware reads that blob from disk or Chrome's memory and re-imports it through the ordinary Windows CNG interfaces (`NCryptOpenStorageProvider`, `NCryptImportKey`, `NCryptSignHash`) to sign whatever it likes on the same physical TPM. Unit 42's own framing of the consequence: "Unlike a legitimate user flow that requires user interaction and device unlock, this attack shows how malware can obtain the required signature silently, without user consent, biometrics, device unlock or elevated privileges." The attacker opens a WebSocket handshake with the cloud authenticator, signs the handshake hash together with the assertion request using the stolen identity key, receives a valid assertion, and replays it to the relying party.

**The single bit that decides whether that works.** The cloud authenticator issues a valid assertion whether the request was signed with the identity key or with the user-verification key; the only difference is the User Verified flag in the authenticator data, which is 0 for the identity key. A relying party that requires user verification and checks the flag rejects the forged assertion — a passkey-protected GitHub login did. A relying party that sets `userVerification` to required but never inspects the returned flag accepts it, and multi-factor authentication collapses to possession of one device key: "In our testing, we identified relying parties that accepted authentication because they did not properly validate the UV flag." Unit 42 demonstrated this against eBay, which has since fixed its validation. Because many relying parties set the parameter to `preferred` rather than `required` for device-compatibility reasons, the population this variant works against is not small.

**Silver Pass-ta-key — becoming the verification key.** Rather than trying to reach the UV key, the attacker deletes it. Nothing protects the `passkey_enclave_state` file from removal (or the attacker issues a `device/forget` command with the identity key it already controls), which forces Chrome to re-onboard the device on next passkey use. Windows onboarding completes only on the second passkey use, so the device sits in a `uv_key_pending` state in between — Chrome defers creating the UV key to avoid stacking a Windows Hello prompt on top of the Google Password Manager recovery-PIN prompt. In that window the attacker generates its own key pair and sends `device/add_uv_key` with its public key, and it is accepted: "The cloud authenticator does not validate the attestation of newly registered UV keys to verify whether they originate from secure hardware." From then on the attacker mints assertions with the UV bit set, from its own infrastructure, without the victim's device being online — reusable access that satisfies even correctly implemented relying parties.

**Golden Pass-ta-key — taking the master key.** Synced passkey private keys are encrypted under a 32-byte security domain secret (SDS) that is supposed to stay inside the cloud authenticator, with only a wrapped copy on the client. Unit 42 found it in plaintext in Chrome's own FIDO device log, and while Google removed it from logging after the report, the underlying flow is unchanged: "Although Google removed this secret from Chrome's logging output following our report, the SDS is still sent to the client and remains accessible in Chrome's process memory." So the attacker forces a fresh onboarding using the Silver technique, watches for `passkey_enclave_state` to be recreated, dumps Chrome's process memory at that moment, extracts the SDS, and decrypts every record in the sync database. The result is exportable passkey private keys, usable from anywhere, for every current and future passkey on the account — and there is no remediation: "In Google's current implementation, there is no way to rotate or revoke the SDS, meaning all current and future synced passkeys remain protected by the same master key." Re-enrolling the device evicts the Silver variant; nothing evicts this one.

**Defender takeaway:** for the CH/EU public-sector estates migrating staff and citizen logins to passwordless authentication, the operative conclusion is that a synced passkey inherits the security of the endpoint, and the only control that is fully yours is the relying-party check. Enforce `userVerification = required` and *validate the returned flag* on every WebAuthn integration you operate, rather than assuming the credential provider enforces it. Where you are the consumer rather than the provider, treat a passkey as strong-but-endpoint-dependent: it defeats phishing, it does not defeat a resident infostealer, so endpoint malware prevention and cross-process memory-access controls remain load-bearing under a passwordless rollout. Two Unit 42 observations sharpen incident handling: synchronised passkeys ship a constant WebAuthn `signCount`, so the counter mechanism relying parties would normally use to spot a cloned credential gives no signal here; and a recovery-PIN prompt appearing during what should be routine passkey use is itself suspicious, because those prompts belong to onboarding and recovery.

**Triage:** the telemetry classes are process and file access, not network. In process and module telemetry, the discriminator for the assertion-forging step is process identity — Chrome itself calling CNG to sign with the device identity key is the legitimate flow that happens on every real passkey login, whereas a non-browser process importing an `NCRYPT_OPAQUE_KEY_BLOB` and calling `NCryptSignHash` after reading `passkey_enclave_state` or the sync LevelDB is not a flow the product produces. For the Silver and Golden variants the sequence is the signal rather than any single event: deletion or modification of `passkey_enclave_state`, followed by a device re-onboarding the user did not initiate, followed by cross-process memory reads of `chrome.exe`. Legitimate re-enrolment happens, but it is user-initiated and rare, and it is not preceded by something removing the local state file. Hardening beyond the relying-party check follows Unit 42's own list: restrict access to Chrome's sync database and local passkey state files to the browser process through platform access controls, and monitor for repeated or unexplained re-triggering of onboarding and recovery flows.
