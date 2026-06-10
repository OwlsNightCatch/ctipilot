**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-10T05:02:16Z · ended_at=2026-06-10T05:06:54Z · duration_seconds=278
**Self-telemetry:** urls_checked=57 · webfetch_calls=8 · bridge_fetches=0 · websearch_calls=0

## Verification report — briefs/2026-06-10.md (iteration 2)

### Prior-iteration delta verification

**F3 / SAP Note 3746332 (iter-1):** I fetched `https://onapsis.com/blog/sap-security-patch-day-june-2026`. Onapsis explicitly associates SAP Note **3746332** with CVE-2026-44748 (SAML XSW) and SAP Note **3717897** with CVE-2026-27671 (RFC kernel memory corruption). The brief body text at line 65 now correctly reads "SAP Note 3746332 is the SAML XSW fix for CVE-2026-44748" — remediation applied. However, the CVE Summary Table at line 107 still reads `SAP Note 3746332` as the Patch entry for **CVE-2026-27671** (RFC kernel). This is a residual error: the table row for CVE-2026-27671 was not updated from the erroneous note number to the correct SAP Note 3717897. **Remediation was incomplete — body text fixed, table not fixed. See F3 below.**

**F3 / TYPO3 CVE-2026-47344 (iter-1):** I fetched `https://typo3.org/security/advisory/typo3-core-sa-2026-006`. The advisory page clearly shows CVE-2026-47344 and CVE-2026-47345 as the CVEs covered by TYPO3-CORE-SA-2026-006. The brief heading now says "CVE-2026-47344 et al." and the CVE table row shows CVE-2026-47344 linked to SA-2026-006. No orphaned CVE-2026-11607 remains in the brief. **Remediation complete.**

**F13 / Tchap enumeration endpoint (iter-1):** I fetched both `https://www.numerique.gouv.fr/sinformer/espace-presse/incident-tchap/` and `https://www.theregister.com/security/2026/06/09/france-probes-compromise-of-gov-messaging-platform-after-account-hijack/5252717`. DINUM does not name any specific enumeration endpoint or API path. The Register says the alleged attacker "suggested...user enumeration was possible through a directory search function" and "None of those claims have been independently verified." The brief at line 19 now reads: "the attacker further claims to have used a Tchap directory-search function to enumerate accounts across the service, a mechanism DINUM has not confirmed and which The Register reports as part of a set of unverified attacker claims." No specific endpoint path (e.g. `/_matrix/client/v3/user_directory/search`) appears in the brief text. **Remediation complete.**

---

### Broken / unreachable URLs

No broken URLs found. All 57 URLs in the liveness ledger returned HTTP 200.

---

### Generic / oversight URLs (replace with specific article)

No generic URLs found. All source URLs resolve to specific articles, advisories, or vendor PSIRT pages.

---

### Citation does not support the claim

**F3-A — CVE Summary Table: SAP Note 3746332 incorrectly listed as patch for CVE-2026-27671 (RFC kernel)**

Claim in brief (line 107, CVE Summary Table):
> `| CVE-2026-27671 | SAP NetWeaver/ABAP (RFC kernel) | 9.8 | n/a | No | No | SAP Note 3746332 | [Onapsis](...) |`

I fetched `https://onapsis.com/blog/sap-security-patch-day-june-2026`. The page explicitly states:
- SAP Note **3746332** → CVE-2026-44748 (SAML XSW fix)
- SAP Note **3717897** → CVE-2026-27671 (RFC kernel memory corruption)

The body text (line 65) correctly says "SAP Note 3746332 is the SAML XSW fix for CVE-2026-44748." But the CVE table at line 107 still says "SAP Note 3746332" for the RFC kernel row. This is a direct contradiction within the brief itself and a truth defect: a defender following the table entry for CVE-2026-27671 would apply the wrong note. The RFC kernel patch is SAP Note 3717897.

---

### Unsupported / hallucinated facts

No new hallucinated facts found. All CVE-attributed technical details verified against fetched sources:
- Ivanti Sentry endpoint, class names, XML block field names, and patch versions confirmed by watchTowr article.
- strongSwan double-free mechanism, glibc behaviour, EAP-Identity path confirmed by strongSwan blog.
- Chrome CVE-2026-11645 as out-of-bounds read/write in V8, CVSS 8.8 confirmed by Chrome Releases blog and sub-agent CISA KEV evidence.
- Dragos 1,020 incidents, The Gentleman 18→83 surge, Romanian victims (Oltenia, Apele Române, Conpet) confirmed by fetching Dragos report.
- "More than quadrupled" (18→83 = 4.6×) is accurate.
- "Roughly a quarter of all incidents" for Europe: Dragos confirms 252/1,020 ≈ 24.7%. Correct.
- "Largest in program history": Tenable article confirms "the largest release since the Patch Tuesday program began, smashing the previous record of 167 CVEs." This claim is supported.
- MaxRequestBytes = 16384 threshold for CVE-2026-47291 not exploited when at default: S3 sub-agent cites MSRC verbatim — "Systems using the default value (16384 bytes / 16 KB) are not impacted by this vulnerability." MSRC page returned 200 in liveness ledger; claim is sourced.
- Red Canary OBO OAuth claims (access_agent, Mail.Send, MicrosoftGraphActivityLogs, ClientRequestId) all confirmed by fetching the Red Canary article.

---

### Claims missing inline citation

No missing-citation defects found.

---

### Strengthen primary source

No NVD/CERT-only sourcing found. All CVE items have vendor PSIRT / research lab primary.

---

### Drop (low relevance / off-audience / not weekly content)

No items warrant dropping. All items have direct CH/EU/public-sector nexus or clear transferable defensive value.

---

### Needs more research

No F8 findings. All items carry sufficient technical depth for Tier 2/3 IR.

---

### Surface contradiction

No material contradictions found beyond what is already disclosed in § 7 (SANS ISC 204 CVEs vs Rapid7/Tenable 198 CVEs — methodology gap disclosed).

---

### Missed angles

**F10 — Silent Ransom Group (SRG) DNS fast-flux infrastructure:** `state/run_log.json` telemetry shows Resecurity was flagged as a candidate source (S3 findings); `url-liveness.tsv` confirms `https://www.resecurity.com/blog/article/silent-ransom-group-srg-uncovering-dns-fast-flux-infrastructure` returned HTTP 200 at 04:17. SRG is a Callback Phishing / BEC group active in European targets. This story was not included in today's brief. Suggested search: `"Silent Ransom Group" OR "Luna Moth" fast-flux 2026-06` for corroborating source before considering inclusion.

---

### Editorial / less-is-more flags (advisory)

No new F11 issues. The five F11 items from iter-1 (CRA Article 14, Dragos "quadrupled" language — now softened to "more than quadrupled", S3 Object Lock, Veeam CWE-502, Meta 19-June notify) are confirmed to be non-blocking as judged by iter-1. The "more than quadrupled" language is verified accurate (4.6×).

---

### Single-source items missing [SINGLE-SOURCE] flag

No F12 issues. All single-source items carry the [SINGLE-SOURCE] flag (Unit 42 cloud logging, Red Canary Entra agents, Check Point TDS ecosystem) or are covered by the national-CERT / primary-authority carve-out (NCSC-CH Week 23, CRA deadline).

---

### Analytical-link-as-fact

No F13 findings remaining. The Tchap F13 from iter-1 was verified remediated above.

---

### Quantifier without source

No new F14 findings. Quantifiers checked:
- "198 CVEs" — supported by Tenable (Rapid7 says ~200).
- "largest ever" → actually "largest in program history" — confirmed by Tenable.
- "73,467 civil servants" — confirmed DINUM.
- "under 9%" — confirmed DINUM.
- "20,225 Instagram accounts" — confirmed by BleepingComputer/Maine AG filing.
- "1,020 industrial incidents" — confirmed Dragos.
- "62% manufacturing" — confirmed Dragos.
- "more than quadrupled … to 83 incidents" — confirmed Dragos (18→83 = 4.6×, mathematically accurate).
- "over 20% of Exchange Online domains were exploitable" — attributed in-text to InfoGuard's bug-bounty sample; claimed in the source.
- "roughly half of external-MX deployments lacked the mitigation" — attributed to InfoGuard.
- "All versions since 4.3.3" for strongSwan — confirmed by strongSwan blog.

---

### Name-collision unflagged

No F15 findings. The Shai-Hulud name in the Hades/PyPI UPDATE item refers to the same attacker lineage as prior coverage (Miasma/Mini-Shai-Hulud). § 7 Verification Notes and the UPDATE heading make this lineage clear. No prior coverage in the dedup context uses "Shai-Hulud" to refer to a defender tool or a different entity in this brief.

---

### Verdict

**NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)**

Single truth defect: the CVE Summary Table row for CVE-2026-27671 still says "SAP Note 3746332" as the Patch entry, but Note 3746332 is the SAML XSW fix (CVE-2026-44748); the correct RFC-kernel note is **3717897**. The body text was fixed in iter-1 remediation; the table was not. A defender following the table entry for CVE-2026-27671 would apply the wrong SAP note.

No editorial or advisory findings requiring main-agent action.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: "§ 2 CVE Summary Table"
  item: "CVE-2026-27671 — SAP NetWeaver/ABAP (RFC kernel)"
  url_or_quote: "| CVE-2026-27671 | SAP NetWeaver/ABAP (RFC kernel) | 9.8 | n/a | No | No | SAP Note 3746332 | [Onapsis](...) |"
  summary: "CVE Summary Table at line 107 lists SAP Note 3746332 as the patch for CVE-2026-27671 (RFC kernel), but Note 3746332 is the SAML XSW fix for CVE-2026-44748 per Onapsis (https://onapsis.com/blog/sap-security-patch-day-june-2026). The correct note for CVE-2026-27671 is SAP Note 3717897. Body text was corrected in iter-1 but the table row was not updated."
```
