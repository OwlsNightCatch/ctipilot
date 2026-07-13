---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: 'Trust-primitive forgery was a research theme this week: recovering live ADFS signing keys, and minting a second ''Verified'' GitHub commit'
headline: Trust-primitive forgery research — Mandiant recovers active ADFS token-signing keys from Machine DPAPI; Git malleability mints a 'Verified' commit
summary: Two 2026-W28 research disclosures attack the primitives defenders treat as ground truth. Mandiant/GTIG documented recovering an active ADFS token-signing key from Machine DPAPI when manual certificate rotation leaves a 'ghost' WID record — with the key, an attacker forges SAML assertions for any federated user (including Global Admins) against Microsoft 365/Entra ID, bypassing MFA and Conditional Access, while avoiding LSASS and the live ADFS process. Separately, Git commit-signature malleability lets an attacker mint a second commit with a different hash that still shows GitHub's 'Verified' badge. Both undermine an assumed-trustworthy signal — a federation token, a signed commit — that downstream controls rely on.
discovered_at: '2026-07-12T23:40:00Z'
event_date: 2026-07-09
run_id: 2026-07-12T2309Z-weekly
priority: notable
immediate_action: null
tags:
  - identity
  - supply-chain
regions:
  - global
  - europe
sectors:
  - public-sector
entities:
  - tool:adfs-machine-dpapi-key-recovery
cves: []
techniques:
  - T1552.004
  - T1606.002
sources:
  - url: https://cloud.google.com/blog/topics/threat-intelligence/recovering-active-adfs-signing-keys-machine-dpapi
    publisher: Mandiant (Google Cloud / GTIG)
    role: primary
  - url: https://thehackernews.com/2026/07/github-verified-commits-can-be.html
    publisher: The Hacker News
    role: primary
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: Two independent research primaries (Mandiant/GTIG for ADFS, The Hacker News reporting the Git signature-malleability research). Reliability B, credibility 1 — the ADFS technique is Mandiant's own red-team finding, corroborated in its operational entry; the Git finding is corroborated research reporting.
confidence: high
classification:
  reliability: B
  credibility: 1
update_of: null
references:
  - 2026-07-09/mandiant-adfs-machine-dpapi-golden-saml-key-recovery
  - 2026-07-09/git-signature-malleability-github-verified-commit-ghost-twin
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
---
Two of the week's research findings share an underappreciated theme: they forge a trust primitive that downstream systems and humans treat as authoritative, rather than exploiting a memory-corruption bug.

The heavier of the two, for the constituency, is Mandiant/GTIG's **ADFS token-signing-key recovery**. ADFS stores its certificate private keys under Machine DPAPI, so any SYSTEM-level process on the ADFS host can recover them independently of the live service or LSASS; when `AutoCertificateRollover` is disabled and an admin rotates a signing certificate manually without a matching WID update, the database retains a "ghost" record while the real signing key stays live in the machine key store. With that key, an attacker forges arbitrary SAML assertions to impersonate any federated user — Global Administrators included — against every SAML-federated app including Microsoft 365 and Entra ID, "bypassing multifactor authentication (MFA), conditional access, and all identity-based controls," and deliberately avoids the LSASS/live-ADFS surfaces defenders usually watch ([Mandiant, 2026-07-09](https://cloud.google.com/blog/topics/threat-intelligence/recovering-active-adfs-signing-keys-machine-dpapi)). The detectable side-effect is Event ID 385 (certificate-rollover mismatch), and Mandiant's guidance is to treat ADFS as Tier-0, move to HSM-backed keys, validate rotations with `Set-AdfsCertificate`, and SACL-audit the MachineKeys directory (Event ID 4663). The second finding, **Git commit-signature malleability**, lets an attacker produce a second commit with a different hash that still renders GitHub's "Verified" badge — collapsing the assumption that a verified-signed commit uniquely identifies its content ([The Hacker News, 2026-07-09](https://thehackernews.com/2026/07/github-verified-commits-can-be.html)).

**Why this belongs in the week's research lens:** both extend a running arc — after last week's Keycloak JWT-forgery and OAuth-abuse research, this week's items give the on-premises-AD equivalent (ADFS) and a code-supply-chain equivalent (signed commits), each with a concrete detection surface the earlier work lacked.

**Defender takeaway:** for identity teams, ADFS belongs in the Tier-0 monitoring and hardening tier alongside domain controllers — the actionable, low-cost step is enabling SACL auditing on the MachineKeys directory and alerting on Event IDs 385 and 4663, since the technique is invisible to LSASS-focused tooling. For build-pipeline owners, a "Verified" badge is no longer sufficient provenance — pin and verify commit hashes, not just signature status. **Triage:** ADFS key theft produces no failed logon and no LSASS access; the honest signals are the certificate-rollover mismatch event and any non-service SYSTEM process reading the MachineKeys path, distinguished from legitimate ADFS operation by process lineage.
