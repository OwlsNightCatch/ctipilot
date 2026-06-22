**Model:** Anthropic Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-22T04:48:27Z · ended_at=2026-06-22T04:50:49Z · duration_seconds=142
**Self-telemetry:** urls_checked=11 · webfetch_calls=8 · websearch_calls=3 · bridge_fetches=0

## Verification report — briefs/2026-06-22.md (iteration 3)

Read cold as a hostile, technically-fluent Swiss/EU public-sector SOC reader. Ran both gates (URL truth + editorial quality). Particular scrutiny on residual version numbers, build strings, percentages and counts per the spawn note — the two prior-iteration corrections (CVSS string `8.3 / 9.8 / 9.8`; QNAP fix build `6.6.8.20251023` + 6.6.x affected scope) both re-verify as now correct.

### Truth-gate results (all PASS)

- **AryStinger deep dive (§ 5 / TL;DR)** — verified against XLab primary (https://blog.xlab.qianxin.com/arystinger-botnet-hijacks-legacy-routers-for-global-attacks-en/, dated 2026-06-17) and BleepingComputer (2026-06-21). Confirmed: 4,300+ nodes; country distribution SK 48.5% / China 31.8% / Sweden 6.4% (third-largest) / Malaysia 3.5% / Singapore 2.5%; device split DIR-850L 75% / DIR-818LW 13%; Dropbear SSH backdoor; the three CVEs (CVE-2013-3307, CVE-2016-5681, CVE-2025-11837); two variants (C RTL819X / Go Standard); `fscan`/`ksubdomain`/`httpx`/`tlsx`; Protobuf+XOR C2 with a `..._2024_secret` hardcoded key marker (XLab key string `sh_#@!_2024_secret`). All match.
- **CVSS string `8.3 / 9.8 / 9.8`** — CVE-2013-3307 = CVSS v3 8.3 (Tenable); CVE-2016-5681 = CVSS v3.0 9.8 (NVD); CVE-2025-11837 = CVSS v3.1 9.8 NIST (NVD lists v3.1 9.8 / v4.0 8.1 QNAP-CNA). The brief uses CVSS v3 consistently across all three — internally consistent and accurate. (The v4.0 8.1 figure exists but the brief is not claiming it.)
- **QNAP CVE-2025-11837** — code injection (CWE-94) in Malware Remover; affected 6.6.x (NVD: 6.6.3 → 6.6.8.20251023 exclusive); fixed build 6.6.8.20251023. Matches brief. (QNAP advisory is qsa-25-47; brief cites the detail via the XLab primary, no direct QNAP URL, so no broken link.)
- **D-Link SAP10503** — confirmed EOL bulletin covering DIR-818L/818LW/850L/860L; all hardware revisions EOL, no firmware path, "replace" guidance. Matches "EoL with no firmware fix" claim.
- **EFK audit (§ 1)** — SwissCybersecurity.net + Netzwoche + EFK PDF (report 25152, PDF resolves as 225 KB application/pdf). Confirmed: report 25152; bodies FS BIS / SEPOS / BACS / Cyber Security Hub; the three gaps (SLA/Vorgabenmanagement shortfall; BACS no legal authority to forward incident reports without agency opt-in; inconsistent IR coordination); EFK rejected folding into BACS. All match.
- **Brazil Cell Broadcast (§ 1)** — The Next Web confirmed: overnight 19–20 June 2026; ~30M phones; seven+ states; ten alerts tracked; Ministry of Integration and Regional Development shutdown at 01:30 / Saturday; Federal Police investigation open; no attribution; X claimant's posts removed; access vector undisclosed. All match.
- **eBanking IPv4-mapped IPv6 (§ 3)** — SANS ISC diary 33090 (Xavier Mertens, 2026-06-19) confirmed: Belgian bank; `[::ffff:...]` bracket form; RFC 4291; regex IPv4-extractor and DNS-reputation evasion. Matches. Brief's own ATT&CK mapping (T1598.003 / T1027) is the brief's analytical layer, not attributed to SANS (SANS cites T1566) — acceptable analyst mapping, not a sourcing defect.

### Editorial-gate results (all PASS)

- **Relevance** — all four published items carry a clear CH/EU public-sector nexus (Swiss federal governance; Brazil→ALERTSWISS/BABS technology transfer; eBanking→Swiss cantonal banks/PostFinance; AryStinger→Sweden 6.4% + EoL D-Link/QNAP on audience attack surface). No drop candidates.
- **Primary-source kind** — AryStinger leads with XLab research-lab post; EFK with trade press + EFK PDF; no item is NVD/MITRE-only sourced.
- **Single-source flags (F12)** — both single-source items (Brazil, eBanking) carry the `[SINGLE-SOURCE]` heading marker AND a § 7 line; SANS ISC PD-5 carve-out correctly invoked and stated. No drift.
- **Quantifiers (F14)** — "third-largest at 6.4%", "4,300+", "75%", "13%", "at least ten", "~30M", "seven states" all trace to a cited source read this iteration.
- **Analytical-link-as-fact (F13)** — AryStinger CVE→variant→device mapping, and "ALERTSWISS runs the same Cell Broadcast technology" / EU ECC Directive 2018/1972 mandate, are accurate and not asserted beyond what sources/standard knowledge support. No inverted attribution.
- **Name-collision (F15)** — no prior brief covered AryStinger / Cell Broadcast / EFK / IPv4-mapped-IPv6; no reuse collision.
- **§ 2 intentionally empty** — properly gated and documented with examined-and-dropped CVE log in § 7; thin-signal day is honestly disclosed.
- **Style** — zero IOCs, zero vanity metrics, English throughout, no workflow-internal language in published prose.
- **Coverage shape** — § 1 leads CH (EFK) before global (Brazil); deep dive earns its length; no Immediate-Action callout claimed (correct for a recon/proxy botnet on EoL kit, not a stop-the-presses item).

### Missed angles
None material. The § 7 drop log (NCSC-UK CNI lecture, Prinz Eugen, INC ransomware, BabaDeda, FulcrumSec) is well-reasoned and the quiet-day coverage-gap list is thorough.

### Verdict
CLEAN

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable) — v2.48
[]
```
