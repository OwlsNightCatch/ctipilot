**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-20T05:07:17Z · ended_at=2026-05-20T05:12:07Z · duration_seconds=290
**Self-telemetry:** urls_checked=15 · webfetch_calls=12 · bridge_fetches=0

## Verification report — briefs/2026-05-20.md (iteration 4)

Even-iteration alt-verifier. Prior-iteration deltas from iter-3 processed first (Fox Tempest F4 and Storm-2949 F3), then independent cold read of full brief.

### Prior-iteration delta verification

**F4 (Fox Tempest "~1,000 accounts" clause) — REMEDIATION CONFIRMED CLEAN.**
Iter-3 F4 asked: drop the "took down ~1,000 accounts" clause. Current brief (line 34) reads: "Microsoft revoked 1,000+ fraudulent code-signing certificates, disabled hundreds of Cloudzy-hosted VMs that Fox Tempest used as its delivery surface, and rolled identity-validation controls into Artifact Signing." The "~1,000 accounts" clause is gone. Paragraph is coherent. Fetched Microsoft On the Issues (https://blogs.microsoft.com/on-the-issues/2026/05/19/disrupting-fox-tempest-a-cybercrime-service/) — source confirms "taking offline hundreds of virtual machines" and "Hundreds of fraudulent Microsoft accounts (disabled)." Brief's VM count phrasing ("disabled hundreds of Cloudzy-hosted VMs") is accurate. The brief does not enumerate the accounts disabled — that's fine, not required. No residual.

**F3 (Storm-2949 Key Vault pivot role — "Owner" not "Key Vault Contributor") — REMEDIATION CONFIRMED CLEAN.**
Iter-3 F3 asked: replace "Key Vault Contributor role" with "Owner role" in Phase 3; update hardening bullet.

Phase 3 (line 179): "using the **Owner** role (which one of the compromised user's Azure RBAC permissions granted over a specific Key Vault)" — correct. Fetched Microsoft Storm-2949 blog (https://www.microsoft.com/en-us/security/blog/2026/05/18/storm-2949-turned-compromised-identity-into-cloud-wide-breach/) — source verbatim: "Part of the compromised user's Azure RBAC permissions was the privileged Owner role over a specific Key Vault." Brief matches.

Hardening bullet (lines 195-196): "Constrain Owner and Key Vault Contributor role assignments — both grant management-plane modification of access policies. Microsoft notes Storm-2949 exercised the Owner role over a specific Key Vault to mutate access policies and grant itself data-plane access; Key Vault Contributor confers the same management-plane mutation capability." Accurate — Owner is correctly attributed as Storm-2949's pivot; Key Vault Contributor is a separate generic hardening recommendation. The MS source confirms Owner was the pivot role, and the hardening recommendation correctly broadens to include both roles.

§ 6 Action Item (line 210) now includes "Owner" in the privileged role list. Confirmed correct.

No residuals from iter-3 findings.

### Analytical-link-as-fact

- **F1** — § 0 TL;DR (line 14): *"Two more CI/CD supply-chain incidents — actions-cool/issues-helper GitHub Action and Nx Console VS Code extension — **confirmed linked to the Mini Shai-Hulud cluster**."* The TL;DR asserts that **both** incidents are confirmed linked to Mini Shai-Hulud.

  The issues-helper body (§ 1, line 58) says: "Socket confirmed the exfiltration domain overlaps with the **Mini Shai-Hulud** npm / PyPI campaign cluster." This is sourced and attributed.

  The Nx Console body (§ 1, lines 66–72) makes **no mention** of Mini Shai-Hulud. Fetched the primary Nx Console source [The Hacker News, 2026-05-19](https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html): the article does not link the Nx Console compromise to Mini Shai-Hulud. It attributes the root cause to "a developer's compromised machine and leaked GitHub credentials." Mini Shai-Hulud appears in the THN article only as a separate tangential mention in a side list of malware/worms — not as the cluster responsible for the Nx Console compromise. The primary Nx Console source [CybersecurityNews](https://cybersecuritynews.com/nx-console-vs-code-extension-compromised/) was not fetched, but the THN source is sufficient to confirm the absent attribution.

  The brief's TL;DR therefore asserts a link (Nx Console → Mini Shai-Hulud) that no cited source for the Nx Console item makes. This is an F13 analytical-link-as-fact: the connection is presented "as if cited" but no cited source in the Nx Console item asserts it. The fix is to revise the TL;DR to attribute the Mini Shai-Hulud link only to issues-helper: e.g. *"actions-cool/issues-helper GitHub Action (linked to Mini Shai-Hulud cluster) and Nx Console VS Code extension"* — or move the cluster attribution to be issues-helper-only.

### Verdict

**NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)**

One truth-class defect: the TL;DR asserts both the issues-helper and Nx Console incidents are "confirmed linked to the Mini Shai-Hulud cluster," but no cited source for the Nx Console item supports that cluster attribution. Fix is a narrow TL;DR rewording to limit the Mini Shai-Hulud attribution to issues-helper only.

All iter-3 remediations confirmed clean (Fox Tempest accounts clause dropped; Storm-2949 Owner role correctly substituted in Phase 3 and hardening bullet; Key Vault Contributor retained as generic hardening guidance without incorrect source attribution). No regressions introduced. All other items checked:

- Drupal PSA-2026-05-18: confirmed live, correct version list, correct severity, correct window.
- Sparx CERT-PL five-CVE chain: confirmed live, all five CVEs correct, versions correct, no vendor patch confirmed.
- StepSecurity issues-helper: confirmed live, 53 tags, imposter commit 1c9e803, /proc/PID/mem, exfil to t.m-kosche.com.
- Huawei VRP / POST Luxembourg: confirmed live, Paul Rausch named source confirmed, no CVE confirmed, July 2025 outage date confirmed.
- Cisco Talos BadIIS: confirmed live, geographic scope (APAC + South Africa + Europe + NA), UAT-8099/DragonRank cluster confirmed.
- Storm-2949 kill chain: full Microsoft blog confirmed live, Owner role confirmed, full RBAC chain matches.
- vm2 heading: now reads "upgrade to ≥ 3.11.4" — confirmed clean (iter-2 residual resolved in iter-3).
- SEPPmail UPDATE: InfoGuard Labs confirmed live, CVE-2026-2743 CVSS 10.0, LFT path traversal to RCE via /etc/syslog.conf, v15.0.4 patch confirmed.
- DirtyDecrypt: BleepingComputer and Moselwal both confirmed live; CVSS 7.5 attributed to THN (additional source) with Moselwal range notation in body — clean.
- check_brief.py single-source WARNs for CVE-2026-41091, CVE-2026-45584, and Cisco Talos BadIIS: all three have explicit § 7 carve-out language (lines 228–231); vendor-as-primary and primary-research carve-outs correctly applied.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F13
  category: analytical-link-as-fact
  section: tl-dr
  item: "Two CI/CD incidents — issues-helper and Nx Console — TL;DR cluster attribution"
  url_or_quote: "Two more CI/CD supply-chain incidents — actions-cool/issues-helper GitHub Action and Nx Console VS Code extension — confirmed linked to the Mini Shai-Hulud cluster."
  summary: "TL;DR asserts both incidents are confirmed linked to Mini Shai-Hulud. The issues-helper item in § 1 has the Socket attribution for Mini Shai-Hulud. The Nx Console item (§ 1) makes no mention of Mini Shai-Hulud. Fetched THN Nx Console source (https://thehackernews.com/2026/05/compromised-nx-console-18950-targeted.html) — article attributes root cause to 'a developer's compromised machine and leaked GitHub credentials' and does not link the incident to Mini Shai-Hulud. Fix: revise TL;DR to limit Mini Shai-Hulud attribution to issues-helper only — e.g. 'actions-cool/issues-helper (exfiltration infrastructure overlapping with Mini Shai-Hulud cluster) and Nx Console VS Code extension'."
```
