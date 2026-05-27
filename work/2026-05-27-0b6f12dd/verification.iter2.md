**Model:** Anthropic Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-27T04:49:54Z · ended_at=2026-05-27T04:53:29Z · duration_seconds=215

## Verification report — briefs/2026-05-27.md (iteration 2)

**Self-telemetry:** urls_checked=17 · webfetch_calls=12 · bridge_fetches=2

---

### Prior-iteration delta verification

Verifying all four F-code remediations from iteration 1:

**F3 (CERTFR bulletin — no French victim claim):** Fetched CERTFR-2026-ACT-023 via bridge. Confirmed: the bulletin lists expanded package scope (`@tanstack/*`, `@squawk/*`, `@mistralai/mistralai@2.2.x`, `mistralai==2.4.6 (PyPI)`, `guardrails-ai==0.10.1 (PyPI)`, `lightning==2.6.2 or lightning==2.6.3 (PyPI)`, `@antv` packages), and states source-code leak on 2026-05-13 ("Le 13 mai 2026, le code source de Shai‑Hulud a été publié par TeamPCP sur le forum cybercriminel Breached[.]st"). The bulletin does **not** name a confirmed French victim. The brief now reads: "it does not name a confirmed French victim" — REMEDIATION CONFIRMED CORRECT.

**F1 (Security Affairs bad URL — Nimbus Manticore):** The brief's § 4 UPDATE now cites only Check Point Research (2026-05-22) and The Hacker News (2026-05-26) as sources. No Security Affairs URL present anywhere. The Check Point Research article confirms SSL.com certificate abuse ("Many of the files used throughout the campaign had valid digital signatures via SSL.com, continuing the abuse of trusted signing infrastructure") citing Gray Matter Software S.R.L. and Kirubel Kerie Negeya as certificate owners. The brief's inline claim "abused two SSL.com-issued code-signing certificates" is supported by Check Point, not THN (THN does not mention SSL.com). The attribution is to Check Point Research only in the inline sentence — REMEDIATION CONFIRMED CORRECT.

**F11a (LRT date correction):** Fetched LRT article — confirmed published 2026.05.22 17:09. Brief footer shows `[LRT, 2026-05-22]` — REMEDIATION CONFIRMED CORRECT.

**F11b (Tycoon 2FA detection count softening):** Elastic article describes 7 Microsoft rules and 4 Google Workspace rules. Brief now says "multiple Entra ID and Google Workspace detections" — REMEDIATION CONFIRMED CORRECT.

---

### Fresh truth pass

All cited URLs checked in this iteration.

**The Record Lithuania:** Confirmed — resolves, dated 2026-05-26, supports all claims (600,000 records, credential abuse, foreign-administered infrastructure). Mentions Slovakia/Ukraine register intrusions as comparators — brief correctly references this.

**Euronews Lithuania:** Confirmed — resolves, dated 2026-05-25, supports resignation of head (Adrijus Jusas), Russia allegation by opposition politician Laurynas Kasčiūnas. Brief says "Lithuanian officials publicly framed…one politician alleging Russian-intelligence hallmarks" — accurate framing.

**LRT Lithuania:** Confirmed — resolves, dated 2026-05-22, supports basic breach facts.

**EUVD EUVD-2026-32027:** Page served only a navigation frame with no substantive body content on this fetch. However, the GHSA advisory at github.com/advisories/GHSA-fwfp-h68w-2hcr fully confirms CVE-2026-9312 (CVSS 9.2, SSRF, upload endpoint, all patch versions). All brief claims are supported by the GHSA even if the EUVD page did not render fully.

**GitHub GHES release notes (3.21.1):** Rendered as header-only page. However, GHSA-fwfp-h68w-2hcr directly links to the release notes and confirms the same fix versions (3.16.20 / 3.17.17 / 3.18.11 / 3.19.8 / 3.20.4 / 3.21.1).

**Tenable TRA-2026-44:** Confirmed — resolves, dated 2026-05-26, supports CVE-2026-9642 (bypass of CVE-2025-62582 fix), Delta Electronics DIAView V4.4, CVSS 9.8, "no fix" available.

**BleepingComputer Charter:** Confirmed — resolves, dated 2026-05-26, supports Charter breach, ShinyHunters, vishing → Entra → Salesforce pattern, Charter dispute of sensitive PI/CPNI claim.

**BleepingComputer 7-Eleven:** Confirmed — resolves, dated 2026-05-26, supports 185,000 people affected. NOTE: This article lists "names, dates of birth, email addresses, phone numbers, and physical addresses" — it does NOT mention SSNs or driver's licences. The SSN/driver's licence claim is supported by CyberInsider 7-Eleven article only.

**CyberInsider Charter:** Confirmed — resolves, dated 2026-05-23. Brief cites as `[CyberInsider, 2026-05-23]` — date correct.

**CyberInsider 7-Eleven:** Confirmed — resolves, dated 2026-05-26. Supports SSNs and driver's licence data types.

**Check Point Research Nimbus Manticore:** Confirmed — resolves, dated 2026-05-22, supports all key claims: MiniFast backdoor, `ZoomUpdateTaskUser-<SID>` hijacking, SEO poisoning, AppDomain hijacking, SSL.com cert abuse (Gray Matter Software S.R.L. and Kirubel Kerie Negeya).

**THN Nimbus Manticore:** Confirmed — resolves, dated 2026-05-26, supports MiniFast, MiniJunk, AppDomain hijacking, SEO poisoning. Does NOT mention SSL.com — the brief's SSL.com claim is correctly attributed to Check Point Research only (inline: "([Check Point Research, 2026-05-22](…))").

**CERT-FR CERTFR-2026-ACT-023:** Confirmed via bridge — resolves, dated 26 mai 2026, supports @antv packages, @mistralai/mistralai, guardrails-ai, lightning, source-code leak 2026-05-13.

**Elastic Security Labs Tycoon 2FA:** Confirmed — resolves, dated 2026-05-26. All 10 specific technical claims verified against the article text: takedown led by Microsoft and Europol, broker client ID 29d9ed98-a469-4536-ade2-f981bc1d605e, Google Chrome client 77185425430, c_sid cross-tier correlation, token-type progression, Graph API calls, "multiple" detection rules, 10–20 min handoff window, aiConfirmedSafe false negative, Dsreg/DeviceRegistrationClient/Dalvik standard UAs. All confirmed.

---

### Broken / unreachable URLs

No URLs broken in this pass.

---

### Generic / oversight URLs (replace with specific article)

No generic URLs found.

---

### Citation does not support the claim

No citation mismatch found after verifying all prior-iteration remediations.

---

### Unsupported / hallucinated facts

No hallucinated facts found.

---

### Claims missing inline citation

No claims identified as missing inline citations.

---

### Strengthen primary source

No NVD-only or CERT-only sourcing found; all items have vendor PSIRT / research-lab primaries.

---

### Drop (low relevance / off-audience / not weekly content)

No items flagged for drop.

---

### Needs more research

No gaps requiring research.

---

### Surface contradiction

No contradictions identified.

---

### Missed angles

F10 — **CERTFR lists @tanstack and @squawk packages not mentioned in the brief.** The CERTFR bulletin lists `@tanstack/* versions en date d'avril et mai 2026` and `@squawk/* toutes versions` as additional compromised packages alongside the @antv, @mistralai, guardrails-ai, and lightning packages the brief does name. These are omitted from the brief's § 4 UPDATE and § 6 Action Item package list. This is a material omission for defenders running expanded CI/CD scans — @tanstack is a widely used React query/router ecosystem package and its omission could leave defenders with an incomplete scan list. Suggested search query: `site:cert.ssi.gouv.fr CERTFR-2026-ACT-023 tanstack squawk` — the source is already fetched; the brief simply needs to expand its package list in § 4 and § 6.

---

### Editorial / less-is-more flags (advisory)

No editorial-advisory items.

---

### Single-source items missing [SINGLE-SOURCE] flag

All single-source items correctly flagged: CVE-2026-9642 (§ 2) carries `[SINGLE-SOURCE]` and is documented in § 7.

---

### Analytical-link-as-fact

No unsupported analytical links found.

---

### Quantifier without source

No unsupported quantifiers found.

---

### Name-collision unflagged

"Mini Shai-Hulud" — checked against prior coverage. Consistent entity across all instances in prior coverage and today's brief. No collision.

---

### Verdict

NEEDS_FIXES (truth: 0, editorial: 1, advisory: 0)

**Finding F10 (editorial):** The CERTFR bulletin CERTFR-2026-ACT-023 names `@tanstack/*` and `@squawk/*` as compromised packages in addition to the @antv, @mistralai/mistralai, guardrails-ai, and lightning packages the brief names. The § 4 UPDATE body and § 6 Action Item should add these two package scopes to the defender scan list. This is a directly actionable omission: defenders following the brief's § 6 guidance will not check for @tanstack or @squawk packages.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F10
  category: missed-angle
  section: "§ 4 UPDATE Mini Shai-Hulud / § 6 Action Items"
  item: "Mini Shai-Hulud CERT-FR package scope"
  url_or_quote: "CERTFR-2026-ACT-023 lists '@tanstack/* versions en date d'avril et mai 2026' and '@squawk/* toutes versions' as compromised packages; the brief only names @antv, @mistralai/mistralai, guardrails-ai, and lightning"
  summary: "Brief omits @tanstack/* and @squawk/* from the defender package-scan list in § 4 UPDATE body and § 6 Action Item; source (CERTFR-2026-ACT-023, fetched this iteration via bridge) explicitly lists both; defenders following the brief guidance will run an incomplete scan"
```
