**Model:** Claude Opus 4.7 (`claude-opus-4-7[1m]`)
**Timestamps:** started_at=2026-05-20T04:57:50Z · ended_at=2026-05-20T05:02:29Z · duration_seconds=279
**Self-telemetry:** urls_checked=16 · webfetch_calls=16 · bridge_fetches=1

## Verification report — briefs/2026-05-20.md (iteration 3)

Cold read of the brief plus targeted verification of (a) prior remediation points from iter-1 and iter-2 (vm2 3.11.4 consistency, Talos BadIIS geographic phrasing, Fox Tempest pricing/Telegram/Google-Form drop, DirtyDecrypt CVSS attribution) and (b) every Source / Additional source URL in §§ 0–6. The vm2 contradiction-surface, the BadIIS geographic rewording, the Fox Tempest pricing removal, and the DirtyDecrypt CVSS 7.5 attribution to Hacker News with the Moselwal 7.8-8.1 characterisation in body all look properly applied. Two unsupported numerical / role claims found that are NOT residuals of iter-1 / iter-2 — they survived all prior passes and need to come out before publish.

### Unsupported / hallucinated facts

- **F1** — § 1 (Fox Tempest deep paragraph), brief asserts: *"Microsoft revoked 1,000+ certificates, disabled hundreds of Cloudzy-hosted VMs, took down ~1,000 accounts, and rolled identity-validation controls into Artifact Signing."* The third clause — **"took down ~1,000 accounts"** — is not supported by any of the three cited sources in this item.
  - Microsoft Threat Intelligence blog (https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/) confirms "Microsoft has revoked over one thousand code signing certificates" — **certificates**, not accounts.
  - Microsoft On the Issues blog (https://blogs.microsoft.com/on-the-issues/2026/05/19/disrupting-fox-tempest-a-cybercrime-service/) says only "hundreds of fraudulent Microsoft accounts" — and that's the count Fox Tempest **created**, not the count Microsoft **took down**. The On-the-Issues post does not quantify Microsoft's takedown of accounts at all.
  - The Record (https://therecord.media/microsoft-disrupts-fox-tempest-malware-signing-service) does not mention any account count.
  - The "~1,000 accounts" figure looks like a conflation with the certificates count. Remediation: either drop the "took down ~1,000 accounts" clause, or replace with "hundreds of fraudulent Microsoft accounts" (the actually-cited number of accounts Fox Tempest created) and rephrase to match what Microsoft said.

### Citation does not support the claim

- **F2** — § 5 Deep Dive, brief asserts in Phase 3: *"They then pivoted to **Azure Key Vault** using the **Key Vault Contributor** role, modified access policies to grant themselves vault data-plane permissions, and exfiltrated dozens of secrets..."* Microsoft Threat Intelligence's Storm-2949 write-up (https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/) says verbatim: **"Part of the compromised user's Azure RBAC permissions was the privileged Owner role over a specific Key Vault"** — i.e. **Owner role**, not Key Vault Contributor. The two roles are different: Owner is a built-in management-plane role with implicit access-policy and IAM rights; Key Vault Contributor is a more narrowly scoped role that grants management-plane modification but not data-plane access. The brief invented "Key Vault Contributor" as the pivot role.
  - The error doubles down later in the same section under **Hardening / mitigation**: *"Constrain Key Vault Contributor role assignments — the role grants management-plane modification of access policies, which is the pivot Storm-2949 used to grant itself data-plane access."* This attributes the **pivot mechanism** to Key Vault Contributor when the cited source attributes it to Owner.
  - Remediation: replace "Key Vault Contributor role" with "Owner role" in the Phase 3 paragraph. In the Hardening section, either (a) rewrite the bullet to "Constrain **Owner** role assignments on Key Vault — Microsoft documents this as the pivot Storm-2949 used to grant itself data-plane access" and keep Key Vault Contributor as a separate "tighten this role family generally" recommendation, or (b) drop the "the pivot Storm-2949 used" attribution from the Key Vault Contributor bullet so the bullet survives as a generic hardening recommendation that doesn't claim source support it doesn't have. Both BleepingComputer's corroborating piece and the Microsoft blog itself use only "privileged" / "Owner" — neither carries "Key Vault Contributor."

### Verdict

**NEEDS_FIXES (truth: 2, editorial: 0, advisory: 0)**

Two truth defects, both about quantifiers / role names that no cited source supports. Both should remediate cleanly: F1 by dropping or rewording one clause; F2 by replacing "Key Vault Contributor" with "Owner" in two places. Neither is structural — the analytical thrust of both items survives the fix. Nothing else in the brief fails verification against the sources I fetched: the Drupal PSA, Sparx CERT-PL chain, actions-cool issues-helper, Nx Console, Huawei VRP / POST Luxembourg, Microsoft Defender CVEs, DirtyDecrypt, vm2 cluster (with contradiction properly surfaced in § 7), SEPPmail UPDATE, TheGentlemen UPDATE, Cisco Talos BadIIS (geographic phrasing now matches source verbatim), and Fox Tempest SDNY / Cloudzy / sectors attributions all check out against their cited primaries.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "Microsoft DCU disrupts Fox Tempest — takedown counts paragraph"
  url_or_quote: "Microsoft revoked 1,000+ certificates, disabled hundreds of Cloudzy-hosted VMs, took down ~1,000 accounts, and rolled identity-validation controls into Artifact Signing."
  summary: "The clause 'took down ~1,000 accounts' is not supported by any of the three cited sources. Microsoft Threat Intelligence blog confirms 1,000+ certificates (not accounts); Microsoft On-the-Issues blog references 'hundreds of fraudulent Microsoft accounts' that Fox Tempest CREATED, not that Microsoft took down — no specific account-takedown count appears in any cited source. Likely conflation with the certificates count. Drop the '~1,000 accounts' clause or rephrase to 'hundreds of fraudulent Microsoft accounts' tied to On-the-Issues attribution."
- code: F3
  category: claim-not-supported
  section: deep-dive
  item: "Storm-2949 Phase 3 — Key Vault pivot role"
  url_or_quote: "They then pivoted to Azure Key Vault using the Key Vault Contributor role, modified access policies to grant themselves vault data-plane permissions"
  summary: "Microsoft's Storm-2949 blog verbatim states 'Part of the compromised user's Azure RBAC permissions was the privileged Owner role over a specific Key Vault' — Owner role, not Key Vault Contributor. The brief misattributes the role twice: once in the Phase 3 narrative and once in the Hardening / mitigation bullet ('Constrain Key Vault Contributor role assignments — the role grants management-plane modification of access policies, which is the pivot Storm-2949 used to grant itself data-plane access'). Owner and Key Vault Contributor are distinct built-in roles. Replace 'Key Vault Contributor' with 'Owner' in both places, OR drop the 'pivot Storm-2949 used' attribution from the hardening bullet so the generic recommendation survives without claiming source support."
```
