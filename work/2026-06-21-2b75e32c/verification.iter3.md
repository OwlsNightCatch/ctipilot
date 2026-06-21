**Model:** Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-21T04:43:55Z · ended_at=2026-06-21T04:46:41Z · duration_seconds=166
**Self-telemetry:** urls_checked=13 · webfetch_calls=11 · bridge_fetches=2

## Verification report — briefs/2026-06-21.md (iteration 3)

Cold read, full truth + editorial pass. All 13 inline source URLs fetched this iteration (GitHub Advisory, ThreatDown, BleepingComputer ×4, The Next Web, ICO via bridge, The Record, HIPAA Pulse, The Register, BankInfoSecurity, Krebs, Qurium, Microsoft, Snyk, Klue, Huntress). ATT&CK technique links treated as canonical (not individually fetched), except T1490 which is implicated by F4. Two defects found; both truth-class.

Convergence context confirmed clean (no regression): HCRG reworded item — HIPAA Pulse uses the exact phrase "a major UK-based healthcare services provider" and does NOT assert an open ICO investigation (brief correctly avoids that). ICO item — "case to answer" is verbatim on the ICO statement page ("concluded that there was a case to answer"); decade-low caseload corroborated by The Record (2,000 cases in 2019 → ~200 in 2025); no "first since 1984" quantifier present. ThreatDown deep-dive date now reads 2026-06-17 consistently in § 0 and § 5 lead; matches the visible byline ("June 17, 2026" by Andrea Bianchini). Texas SSN contradiction accurately rendered and flagged in § 7 (Register confirms AG-portal filing contradicts the public no-SSN statement; Kroll credit monitoring confirmed by Register). One Medical 8.8TB/06-22-deadline correctly framed as ShinyHunters' unverified claim. Popa/Alarum correctly attributed to Krebs/Qurium with explicit "not charged" hedge; neonative library confirmed on Qurium page. Mastra/Sapphire Sleet (ehindero dormant account, 142 packages, second 2026 takeover after Axios, scdev SYSTEM persistence, 166 wallet extensions) all confirmed across BleepingComputer + Microsoft + Snyk.

### Citation does not support the claim

**F3** — § 2 (and the § 0 TL;DR bullet for the same item). Claim quoted: *"defenders report on the order of 17 million blocked exploitation attempts, peaking in early June ([GitHub Advisory GHSA-jxfc-8wcq-xxcg])"* (line 53), and § 0: *"being mass-exploited (≈17M blocked requests) ... ([GitHub Advisory GHSA-jxfc-8wcq-xxcg])"* (line 10).
The GitHub Advisory page fetched this iteration is a static CVE record (title "The Gravity SMTP plugin for WordPress is vulnerable to Sensitive Information Exposure", CWE-200, CVSS 7.5, EPSS 2.98%, affected ≤2.1.4). It contains **no exploitation telemetry** — no mention of 17 million, blocked requests, or an early-June peak. That figure originates from The Next Web (fetched this iteration): "Wordfence blocked over 17 million exploitation attempts since early May 2026, with peak activity around June 7." The Next Web is **already cited as `Additional source`** on this item, so the supporting source is present — it is simply attached to the wrong link.
Remediation: move the 17M / early-June-peak citation from the GitHub Advisory link to the TNW link in both the § 0 TL;DR bullet and the § 2 body sentence. (CVSS 7.5 in the footer is correctly sourced to the GitHub Advisory and is fine — note TNW reports 5.3, but the brief uses the stronger source.)

### Unsupported / hallucinated facts

**F4** — § 5 deep dive (and a knock-on in § 6 Action Items). Claim quoted: *"Because the family deletes shadow copies as a recovery-inhibition precursor ([T1490 Inhibit System Recovery]), alert on `vssadmin.exe` / `wmic.exe` invoking `shadowcopy delete`."* (line 95), echoed in § 6 line 104 ("... and `shadowcopy delete`").
Neither cited source supports a shadow-copy-deletion behaviour for Prinz Eugen. The ThreatDown deep dive (the primary, fetched this iteration) does not mention shadow copies, VSS, vssadmin, or Inhibit System Recovery anywhere in its kill-chain or anti-forensics description — its anti-recovery measures are key-zeroing, GC and self-deletion, not shadow-copy deletion. The BleepingComputer article (additional source, fetched this iteration) explicitly carries no shadow-copy/VSS/T1490 content. The T1490 ATT&CK mapping and the `vssadmin`/`wmic ... shadowcopy delete` hunt are therefore fabricated technical detail attributed to the family.
Remediation: remove the "deletes shadow copies ... (T1490)" clause and the `vssadmin`/`wmic shadowcopy delete` hunt sentence from § 5, and strike "and `shadowcopy delete`" from the § 6 Action Item — unless a source actually documenting this behaviour is located and cited. (The rest of the § 5 technical detail — RDP access, `net user admin germania /add`, `servertool.exe` via Chrome to Music, RemotePC abuse, ChaCha20-Poly1305 / Argon2id→SHA-256→HKDF-SHA256, CHV1 header, `.prinzeugen`, key-zeroing + self-delete — is all confirmed verbatim against ThreatDown and stands.)

### Editorial / less-is-more flags (advisory)

**F11 (advisory, no action required)** — Two minor date drifts, both within normal source-byline variance and not worth an edit:
(a) § 4 cites "[Snyk, 2026-06-17]"; the Snyk page byline reads June 16, 2026. Cosmetic; the in-window delta for the UPDATE is BleepingComputer 2026-06-20 regardless.
(b) § 4 Klue body attributes the platform list "principally Salesforce, plus Gong, HubSpot, SharePoint and others" to the Klue blog, which names only "Salesforce ... and certain third-party platforms" explicitly; Gong is confirmed in the BleepingComputer source cited on the same item. Citation chain covers it; no edit needed.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 1)

Both truth findings are precise and source-backed: F3 is a citation-attachment fix (move the 17M figure to the already-cited TNW link); F4 removes a fabricated shadow-copy/T1490 behaviour absent from both cited sources. No editorial drops, no relevance/sourcing/single-source defects — § 7 single-source flags (HCRG, One Medical) and the Texas contradiction line are all correctly present. Once F3 and F4 are remediated the brief should reach CLEAN.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-4020 — Gravity SMTP WordPress plugin"
  url_or_quote: "defenders report on the order of 17 million blocked exploitation attempts, peaking in early June ([GitHub Advisory GHSA-jxfc-8wcq-xxcg])"
  summary: "17M-blocked-requests figure + 'peaking in early June' attached to the GitHub Advisory link, but that page is a static CVE record with no exploitation telemetry. Figure originates from The Next Web (Wordfence), already cited as Additional source. Move the citation to the TNW link in both the § 0 TL;DR bullet and § 2 body."
- code: F4
  category: hallucinated-fact
  section: deep-dive
  item: "Prinz Eugen deep dive (§ 5)"
  url_or_quote: "Because the family deletes shadow copies as a recovery-inhibition precursor ([T1490 Inhibit System Recovery]), alert on vssadmin.exe / wmic.exe invoking shadowcopy delete."
  summary: "Neither cited source (ThreatDown primary, BleepingComputer additional) mentions shadow-copy deletion, vssadmin/wmic, or T1490. Remove the T1490 clause + shadowcopy-delete hunt from § 5 and strike 'and shadowcopy delete' from § 6 Action Item unless a supporting source is added."
```
