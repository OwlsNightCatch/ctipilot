**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-20T04:57:36Z · ended_at=2026-06-20T05:02:36Z · duration_seconds=300
**Self-telemetry:** urls_checked=20 · webfetch_calls=16 · bridge_fetches=2

## Verification report — briefs/2026-06-20.md (iteration 4)

### Iter-3 remediation verification (walk before cold pass)

- **F4 Nintendo "859 MB"** — Remediation confirmed. No data-size figure appears in the Nintendo item. BleepingComputer (fetched this iteration) does report "~1GB" (attacker claim) but the brief says "a trove of employee data" — no specific size. CLEAN.
- **F14 FortiBleed "63.3%"** — Remediation confirmed. No 63.3% figure in the brief. SecurityWeek (fetched this iteration) confirms 86,644 devices, 194 countries, and "45-GPU cluster managed via Hashtopolis" verbatim. Remaining FortiBleed quantifiers are source-supported. CLEAN.
- **F3 AutoJack § 7 note** — Remediation confirmed. § 7 note reads: "The Hacker News mentions CVE-2026-26030 and CVE-2026-25592 in the context of Microsoft's separate Semantic Kernel RCE research, not the AutoJack/AutoGen Studio chain." THN article (fetched) confirms CVE-2026-26030/25592 are mentioned in the article (in a "Mentioned entities" context) but the AutoJack chain itself carries no CVE. Microsoft primary (fetched) does not mention those CVEs. Note is accurate. CLEAN.
- **F3 Kodak BleepingComputer re-point** — Remediation confirmed. BleepingComputer 2026-06-17 (fetched) does contain: ShinyHunters Salesforce Aura/Salesloft Drift claims (1.5B records), Oracle PeopleSoft exploitation, Snowflake links. The brief's attribution of those specifics to BleepingComputer is correct. CLEAN.
- **F4 AVer CWE-552** — Remediation confirmed. CISA ICSA-26-169-01 HTML (fetched via bridge) contains: "Relevant CWE: CWE-552 Files or Directories Accessible to External Parties". CLEAN.
- **F4 Gogs CWE-77** — Remediation confirmed. GHSA-qf6p-p7ww-cwr9 (fetched) states CWE-77, CVSS 3.1 9.9. Brief says "CWE-77 command injection; CVSS 4.0 9.4 per BSI, CVSS 3.1 9.9 per the GitHub advisory." The GHSA CVSS 3.1 9.9 is confirmed. BSI page was JS-rendered (no content returned). CLEAN on CWE-77; BSI CVSS 4.0 9.4 cannot be independently verified this iteration (BSI pages consistently return no content via WebFetch — systemic limitation).
- **F11 usbliter8 "under two seconds"** — Remediation confirmed. The Hacker News (fetched) quotes "in under two seconds" verbatim. The Paradigm Shift primary page mentions ~400ms shellcode timing but not an overall "under two seconds" completion time — THN is the cited additional source and explicitly supports the phrase. CLEAN.

### Iter-1/iter-2 remediation integrity check

- **SVD-2026-0603**: present correctly in § 4 UPDATE footer. No "SVD-0601" or "SVD-2026-0601" anywhere in the brief except in the § 7 correction note (documenting the old error). CLEAN.
- **CVSS 9.8**: present for CVE-2026-20253. No "8.8" in live content (only in § 7 correction note). CLEAN.
- **Fixed versions 10.4.0/10.2.4/10.0.7**: present in § 4 and § 6. Splunk PSIRT (fetched) confirms these. CLEAN.
- **CISA-KEV-2026-06-18**: confirmed by CISA KEV catalog fetch — dateAdded: 2026-06-18. CLEAN.
- **Gogs GHSA-qf6p-p7ww-cwr9**: present in § 2 footer. CLEAN.
- **Windchill builds 12.1.2.27/13.0.2.12/13.1.2.8/13.1.3.4**: in CVE summary table. Heise (fetched) confirms all four. CLEAN.
- No stale "8.8", "SVD-0601", "9.4.2", "12.0.2", "859 MB", "63.3%", "CWE-20", "CWE-88" in live content. CLEAN.

---

### Unsupported / hallucinated facts

**F4-A — ShinyHunters designated "UNC6395 / The Com affiliate" (§ 1, Kodak item)**

Claim in brief (line 29): "ShinyHunters (UNC6395 / The Com affiliate)"

Sources cited for this item: SecurityWeek, BleepingComputer 2026-06-17, Malwarebytes. All three fetched this iteration. None of them use the term "UNC6395" or "The Com affiliate" for ShinyHunters. The BleepingComputer article identifies the actor only as "ShinyHunters." The SecurityWeek article identifies the actor only as "ShinyHunters." The Malwarebytes article identifies the actor only as "ShinyHunters."

Contradicts established prior coverage: the 2026-W24 weekly summary and prior daily briefs consistently designate ShinyHunters as "UNC6240" (Mandiant/Google GTIG attribution, from cloud.google.com/blog/topics/threat-intelligence/shinyhunters-targets-education-sector-oracle-exploit/). "UNC6395" appears in no cited source and no prior coverage — it is a different Mandiant designation not supported by any linked primary for this item.

This is a hallucinated entity identifier. The correct Mandiant cluster designation for ShinyHunters (from prior coverage) is UNC6240. "The Com affiliate" may be a valid characterisation but also does not appear in any cited source.

**Remediation required:** Replace "UNC6395 / The Com affiliate" with "UNC6240" (consistent with prior coverage and sourced Mandiant attribution) or drop the parenthetical entirely if no cited source supports it.

---

### Broken / unreachable URLs

**F1-A — NCSC-NL advisory NCSC-2026-0198 redirects to homepage (§ 4, Splunk UPDATE)**

URL in brief: `https://advisories.ncsc.nl/advisory?id=NCSC-2026-0198`

Fetched this iteration: the URL returns a redirect page with only "[click here](/) " — no advisory content. The homepage confirms the NCSC-NL advisory portal exists, but this specific URL does not resolve to the advisory.

Impact: The URL is used as an "Additional source" in the Splunk UPDATE's footer for exploitation confirmation. The primary source (Splunk PSIRT SVD-2026-0603, fetched this iteration) itself states "Limited exploitation was reported in June 2026" — so the exploitation claim is supported by the primary. The broken additional-source is a sourcing quality issue rather than a truth defect, but the URL must be corrected or removed.

**Remediation required:** Either find and replace with the correct NCSC-NL CSAF advisory URL for NCSC-2026-0198 (possibly `https://advisories.ncsc.nl/api/2.0/advisories/NCSC-2026-0198.json` or similar), or remove the NCSC-NL citation and rely on the Splunk PSIRT primary which already supports the exploitation claim.

---

### Verdict

NEEDS_FIXES (truth: 1, editorial: 1, advisory: 0)

- Truth: F4-A (UNC6395 vs UNC6240 — hallucinated entity identifier, no cited source supports UNC6395)
- Editorial: F1-A (NCSC-NL NCSC-2026-0198 URL dead — redirects to homepage)

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "Kodak confirms breach after ShinyHunters leak-site listing"
  url_or_quote: "ShinyHunters (UNC6395 / The Com affiliate)"
  summary: "None of the three cited sources (SecurityWeek, BleepingComputer 2026-06-17, Malwarebytes) use 'UNC6395' or 'The Com affiliate' for ShinyHunters. Prior coverage (2026-W24 weekly, Google GTIG) consistently designates ShinyHunters as UNC6240. Replace with UNC6240 or drop parenthetical."
- code: F1
  category: broken-url
  section: updates
  item: "UPDATE: Splunk CVE-2026-20253 now under confirmed limited targeted exploitation"
  url_or_quote: "https://advisories.ncsc.nl/advisory?id=NCSC-2026-0198"
  summary: "URL redirects to NCSC-NL homepage — no advisory content returned. Primary source Splunk PSIRT SVD-2026-0603 already supports the exploitation claim. Remove or replace the dead additional-source URL."
```
