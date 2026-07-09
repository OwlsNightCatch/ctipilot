---
schema: 1
kind: research
horizon: operational
title: "Mandiant \"Ghost in the Database\": recovering an active ADFS token-signing key from Machine DPAPI when the WID/DKM Golden SAML path fails"
headline: "Mandiant recovers a live ADFS signing key from Machine DPAPI — a Golden SAML variant that sidesteps the WID/DKM path and LSASS-watching detection"
summary: >
  Mandiant documented an ADFS Golden SAML variant: when AutoCertificateRollover is
  disabled and certificates are rotated manually, the WID configuration database drifts
  to a stale "ghost" certificate while the active token-signing key sits in the machine
  CAPI store protected by Machine DPAPI. A SYSTEM-level attacker recovers it with
  SharpDPAPI /machine — without touching the WID/DKM path or LSASS — and forges a Global
  Administrator SAML assertion that Entra ID accepts, bypassing MFA and conditional access.
  The drift is observable via ADFS Event ID 385; treat ADFS as Tier 0.
discovered_at: "2026-07-09T04:32:59Z"
event_date: "2026-07-07"
run_id: 2026-07-09T0409Z-intel
priority: notable
immediate_action: null
tags: [identity, espionage, cloud]
regions: [global, europe, switzerland]
sectors: [public-sector, finance, energy, healthcare, telco]
entities: ["tool:adfs-machine-dpapi-key-recovery"]
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/recovering-active-adfs-signing-keys-machine-dpapi"
    publisher: "Mandiant (Google Cloud Blog / GTIG)"
    date: "2026-07-07"
    role: primary
  - url: "https://itbrief.co.uk/story/mandiant-finds-way-to-recover-active-adfs-signing-keys"
    publisher: "itbrief.co.uk"
    date: "2026-07-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Successfully obtaining this active key allows an attacker to forge valid SAML assertions for any user, bypassing the need for user credentials and multi-factor authentication"
    publisher: "Mandiant (Google Cloud Blog / GTIG)"
  - quote: "The recovered key was used to forge a SAML assertion impersonating a Global Administrator identity, which Entra ID accepted as a valid authentication assertion"
    publisher: "Mandiant (Google Cloud Blog / GTIG)"
  - quote: "Configure object access auditing via SACLs on C:\\ProgramData\\Microsoft\\Crypto\\RSA\\MachineKeys\\ and C:\\Windows\\System32\\Microsoft\\Protect\\S-1-5-18\\. When configured correctly, this generates Security Event ID 4663 for file access attempts."
    publisher: "Mandiant (Google Cloud Blog / GTIG)"
verification: multi-source
sourcing_note: null
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
  - "Inventory ADFS: run Get-AdfsProperties for AutoCertificateRollover:False and Get-AdfsCertificate to confirm the WID record matches the active token-signing certificate; any Event ID 385 is a drift indicator to investigate."
  - "Migrate ADFS token-signing certificates to an HSM (removes the Machine DPAPI extraction path entirely), run ADFS under gMSA, and govern ADFS hosts as Tier 0 with PAWs; when rotating manually, always run Set-AdfsCertificate, not certificate install alone."
  - "Deploy SACLs (Event ID 4663) on C:\\ProgramData\\Microsoft\\Crypto\\RSA\\MachineKeys\\ and C:\\Windows\\System32\\Microsoft\\Protect\\S-1-5-18\\, and correlate Entra ID federated sign-ins against ADFS issuance events (299 / 1200-series) to find tokens with no matching upstream authentication."
migrated_from: null
---

**Background.** Golden SAML — forging SAML assertions by stealing an identity provider's token-signing key — has been public tradecraft since CyberArk's 2017 disclosure ([CyberArk, 2017](https://www.cyberark.com/resources/threat-research-blog/golden-saml-newly-discovered-attack-technique-forges-authentication-to-cloud-apps)), and Mandiant previously documented network-based extraction of ADFS secrets during the UNC2452/SolarWinds intrusions ([Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/abusing-replication-stealing-adfs-secrets-over-the-network)). The standard extraction path pulls the encrypted signing key from the ADFS Windows Internal Database (WID) and decrypts it with Distributed Key Manager (DKM) material stored in Active Directory. This new Mandiant write-up documents a variant that defeats that assumption when ADFS configuration has drifted.

During a red-team engagement, Mandiant found that ADFS deployments with `AutoCertificateRollover` disabled (`Get-AdfsProperties` → `AutoCertificateRollover: False`) and certificates rotated manually can leave the WID configuration database holding only a stale "ghost" certificate record, while the ADFS service actually signs tokens with a newer certificate whose private key lives in the machine CAPI store ([Mandiant, 2026-07-07](https://cloud.google.com/blog/topics/threat-intelligence/recovering-active-adfs-signing-keys-machine-dpapi)). In that state the classic path still "works" mechanically — the WID blob decrypts via DKM — but Entra ID rejects the resulting token with **AADSTS500172** because the key is no longer the one in use.

**The key's real location and protection.** The active private key sits under `C:\ProgramData\Microsoft\Crypto\RSA\MachineKeys\`, with the certificate enrolled in the `LocalMachine\My` store. It is protected by **Machine DPAPI** (not user-bound DPAPI): the `DPAPI_SYSTEM` LSA secret plus machine masterkeys under the `S-1-5-18` (SYSTEM) context at `C:\Windows\System32\Microsoft\Protect\S-1-5-18\`. Machine-scoping is deliberate — it keeps the key usable across service-account password changes, gMSA rotations and reboots — but it also means a SYSTEM-level actor can recover the key entirely from the host. Mandiant confirmed recovery with `SharpDPAPI /machine`, which enumerated the active key material under that path (the CNG `Crypto\Keys` store was not in use in the assessed environment) — no interaction with the live ADFS process or LSASS is required, reducing visibility for defenses that watch only credential-dumping/process-memory access ([Mandiant, 2026-07-07](https://cloud.google.com/blog/topics/threat-intelligence/recovering-active-adfs-signing-keys-machine-dpapi)).

**Kill chain (ATT&CK).** SYSTEM-level foothold on the ADFS host → recover Machine-DPAPI-protected masterkeys and the CAPI signing key (`T1552 Unsecured Credentials`, via `SharpDPAPI /machine`) → forge a SAML assertion impersonating a Global Administrator (`T1606.002 Forge Web Credentials: SAML Tokens`) → Entra ID accepts it as a valid federated authentication assertion, yielding Global Administrator access to the Microsoft 365 tenant with MFA and conditional access fully bypassed (`T1078.004 Valid Accounts: Cloud Accounts`). Because the forged assertion is honoured for **all SAML relying-party trusts**, the blast radius extends to every SaaS platform federated through the same ADFS, not just Microsoft services.

**Hunt and detection.** The drift condition itself is observable: **ADFS Event ID 385** fires when the WID record and the actively-used signing certificate diverge, and self-resolves only once `AutoCertificateRollover` is re-enabled and a rollover runs. For key-theft detection, Mandiant recommends SACL-based object-access auditing (Security **Event ID 4663**) on `C:\ProgramData\Microsoft\Crypto\RSA\MachineKeys\` and `C:\Windows\System32\Microsoft\Protect\S-1-5-18\`, treated as correlation evidence rather than a standalone signal. The strongest analytic is cross-source: correlate ADFS token-issuance/claims events (Event IDs 299 and the 1200-series, version-dependent) against Entra ID sign-in logs to surface federated sign-ins with no matching upstream authentication context, baselining claim sets, IP ranges and user-agents per relying-party trust for privileged accounts — neither log source alone is sufficient ([Mandiant, 2026-07-07](https://cloud.google.com/blog/topics/threat-intelligence/recovering-active-adfs-signing-keys-machine-dpapi)).

**Hardening.** Migrate token-signing certificates to an HSM to eliminate the software-accessible key and thus the Machine DPAPI extraction path entirely; run ADFS under gMSA to reduce manual-rotation drift; govern ADFS servers as **Tier 0** (restricted admin paths, dedicated PAWs, separation from general server administration). When `AutoCertificateRollover` is disabled, a manual rotation must include `Set-AdfsCertificate` — installing the certificate alone is insufficient — and be validated with `Get-AdfsCertificate`; a subsequent Event ID 385 signals lingering inconsistency. Organisations migrating to native OIDC federation remove this attack path altogether ([Mandiant, 2026-07-07](https://cloud.google.com/blog/topics/threat-intelligence/recovering-active-adfs-signing-keys-machine-dpapi)). ADFS remains widely deployed for on-prem/hybrid identity across Swiss and EU public-sector estates mid-migration to Entra ID, making this a direct Tier 0 hardening item for the constituency.
