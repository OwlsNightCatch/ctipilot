**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-22T04:42:44Z · ended_at=2026-06-22T04:46:19Z · duration_seconds=215

## Verification report — briefs/2026-06-22.md (iteration 2)

### Prior-iteration delta review

**F14 remediation (CVSS correction):** VERIFIED CORRECT. Footer now reads `CVSS: 8.3 / 9.8 / 9.8` in order CVE-2013-3307 / CVE-2016-5681 / CVE-2025-11837. NVD confirms: CVE-2013-3307 = 8.3 HIGH, CVE-2016-5681 = 9.8 CRITICAL, CVE-2025-11837 = 9.8 CRITICAL. The correction is accurate.

**F11 advisory (Linksys/D-Link/RTL819X framing):** ACCEPTABLE. NVD scopes CVE-2013-3307 to Linksys E1000/E1200/E3200, while XLab characterises the vulnerability as affecting the Realtek RTL819X SoC family broadly (including D-Link models sharing that chipset). The brief attributes the "Linksys/D-Link … RTL819X" device framing to XLab's characterisation, which is appropriate. No action needed.

---

### Broken / unreachable URLs

No broken URLs found. All primary source URLs resolve to specific articles/advisories:
- https://blog.xlab.qianxin.com/arystinger-botnet-hijacks-legacy-routers-for-global-attacks-en/ — resolves, correct article.
- https://www.bleepingcomputer.com/news/security/arystinger-botnet-infected-thousands-of-d-link-routers-worldwide/ — resolves, correct article.
- https://www.swisscybersecurity.net/news/2026-06-19/neue-cyberaufsicht-kaempft-mit-anlaufschwierigkeiten — resolves, correct article.
- https://www.efk.admin.ch/wp-content/uploads/publikationen/berichte/wirtschaft_und_verwaltung/informatikprojekte/25152/25152-wik-sepos-fs-bis_d.pdf — resolves as PDF (binary; Swiss German government PDF created 2026-06-09).
- https://www.netzwoche.ch/news/2026-06-19/neue-cyberaufsicht-kaempft-mit-anlaufschwierigkeiten — resolves, correct article.
- https://thenextweb.com/news/brazil-civil-defense-alert-hack-misanthropy-cell-broadcast — resolves, correct article (dated 2026-06-21).
- https://isc.sans.edu/diary/33090 — resolves, correct SANS ISC diary entry (2026-06-19, Xavier Mertens).
- https://supportannouncement.us.dlink.com/security/publication.aspx?name=SAP10503 — resolves, confirms D-Link DIR-850L/DIR-818LW/DIR-818L/DIR-860L EoL status.
- All MITRE ATT&CK technique URLs (T1190, T1133, T1562.004, T1036, T1572, T1090.002, T1046, T1595, T1059.006) — all resolve to correct technique/sub-technique pages.

### Citation does not support the claim

**F1.** Section: § 5 AryStinger deep-dive. The brief states CVE-2025-11837 affects "QNAP Malware Remover utility (fixed in `6.6.8.20251023`; vulnerable in builds at or below `6.6.8.20250925`)."

- The QNAP advisory QSA-25-47 (https://www.qnap.com/en/security-advisory/qsa-25-47) says the affected scope is "Malware Remover 6.6.x" with fix in "6.6.8.20251023 and later." It does not state a last-vulnerable build of `6.6.8.20250925`.
- NVD (https://nvd.nist.gov/vuln/detail/CVE-2025-11837) says affected versions are "6.6.3 through 6.6.8.20251022" — the last vulnerable build is `6.6.8.20251022`, not `6.6.8.20250925`.

The brief's specific claim of "vulnerable in builds at or below `6.6.8.20250925`" is not supported by either primary source. The correct last-vulnerable build per NVD is `6.6.8.20251022` (one build before the fix, `6.6.8.20251023`). This is a precision error that could cause a defender to under-apply patching (thinking builds up to `6.6.8.20251022` but newer than `6.6.8.20250925` are patched, when they are not).

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

**Finding F1 is a truth defect:** the version string "vulnerable in builds at or below `6.6.8.20250925`" does not match either the QNAP advisory (which names the fix as `6.6.8.20251023` without specifying last-vulnerable) or NVD (which names last-vulnerable as `6.6.8.20251022`). The correct statement is either "affected versions 6.6.3 through 6.6.8.20251022; fixed in 6.6.8.20251023+" (per NVD) or simply "fixed in 6.6.8.20251023+" (per QNAP advisory). The version `6.6.8.20250925` does not appear in either source.

All other checks: no broken URLs, no hallucinated entities, no missing citations, no NVD-only sourcing, no vendor marketing, no single-source flag drift, no contradictions, no name collision, no analytical-link-as-fact issues.

### Missed angles

The brief's § 7 coverage-gap log shows several national-CERT feeds (NCSC-CH, CERT-EU, BSI-DE, ANSSI) had no qualifying in-window items. Given the thin-signal day context, no missed angle rises to the level of a required flag.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: deep-dive
  item: "AryStinger botnet — CVE-2025-11837 version scope"
  url_or_quote: "fixed in `6.6.8.20251023`; vulnerable in builds at or below `6.6.8.20250925`"
  summary: "The version `6.6.8.20250925` does not appear in either the QNAP advisory QSA-25-47 (which names the fix as 6.6.8.20251023+ and affected scope as 6.6.x only) or NVD (which names the last vulnerable version as 6.6.8.20251022). Correct the upper bound of the vulnerable range to `6.6.8.20251022` (NVD) or drop the specific last-vulnerable version and retain only the fix version `6.6.8.20251023+` per the QNAP advisory."
```
