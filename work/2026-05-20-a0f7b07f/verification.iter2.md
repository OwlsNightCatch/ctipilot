**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-20T04:50:12Z · ended_at=2026-05-20T04:53:26Z · duration_seconds=194
**Self-telemetry:** urls_checked=10 · webfetch_calls=4 · bridge_fetches=3

## Verification report — briefs/2026-05-20.md (iteration 2)

Even-iteration alt-verifier. Prior-iteration deltas block processed first, then independent truth pass on items not covered by iter-1.

### Prior-iteration delta verification

**F4 (BadIIS geography/count) — REMEDIATION CONFIRMED CLEAN.**
Brief line 137 now reads: "Talos describes the geographic distribution as primarily the **Asia-Pacific region** with a smaller number of compromised servers in South Africa, Europe, and North America." Fetched https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/ this iteration. Talos article confirmed: geographic entities listed are "Asia-Pacific region, South Africa, Europe, North America" — no specific server count, no named individual countries. Brief phrasing is an accurate paraphrase. No residual.

**F3 (Fox Tempest pricing/Telegram/Google Form) — REMEDIATION CONFIRMED CLEAN.**
The sentence "The service charged USD 5,000–9,000 per signing run via a Google Form pricing sheet and a Telegram channel labelled 'EV Certs for Sale by SamCodeSign' ([The Record, 2026-05-19])" is entirely absent from the brief. Fetched https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/ this iteration — article confirmed live, mentions Fox Tempest, signspace[.]cloud, 1,000+ certificates, Rhysida/INC/Qilin/Akira, 72-hour cert validity. No pricing figure, no Telegram channel name, no Google Form in the fetched article. The Record is now cited only for the SDNY civil action / seizure claim. Microsoft TI blog cited for technical specifics. Remediation correct.

**F3 (vm2 patch version) — PARTIAL REMEDIATION — RESIDUAL REGRESSION INTRODUCED.**
Body text (line 116) now correctly reads "the comprehensive fix per BSI WID-SEC-2026-1583 is **vm2 ≥ 3.11.4**". Action item (line 214) correctly reads "Upgrade to 3.11.4 per BSI WID-SEC-2026-1583". § 7 Verification Notes (line 237) correctly surfaces the contradiction between BSI (3.11.4) and The Hacker News (3.11.2). These are clean. HOWEVER: **the section heading at line 106 was not updated** and still reads:
`### vm2 Node.js sandbox — 12 critical CVEs (CVE-2026-43997 / 43999 / 44005 / 44006 / 44008 / 44009 et al.), sandbox escape to host RCE, patch to 3.11.2`
A defender skimming headings will read "patch to 3.11.2" and not apply the correct 3.11.4 fix. The BSI primary advisory (confirmed by iter-1 bridge fetch) specifies 3.11.4. This is a truth-class residual: the heading contradicts the body, the action item, and the cited primary.

**F14 (DirtyDecrypt CVSS 7.5/CWE-122) — REMEDIATION CONFIRMED CLEAN.**
The opening sentence at line 100 no longer contains "(CVSS 7.5, CWE-122)". It now reads: "CVE-2026-31635 is a **page-cache write due to a missing copy-on-write guard in `rxgk_decrypt_skb()` in `net/rxrpc/rxgk_crypt.c`**". The body now explicitly attributes the CVSS 7.5 value to The Hacker News: "(Hacker News carries the CVSS 7.5 score; the [Moselwal technical write-up] characterises the LPE class as in the 7.8–8.1 range without a settled NVD score at time of publication)." CVSS: 7.5 retained in footer — acceptable, attributed to Additional source. Remediation correct and no regression introduced.

**F12 (Fox Tempest §7 single-org acknowledgement) — REMEDIATION CONFIRMED CLEAN.**
§ 7 line 232 now reads: "Fox Tempest disruption (§ 1) — effectively single-organisational-source: two of three cited URLs are Microsoft properties (Microsoft Threat Intelligence security blog + Microsoft On the Issues DCU legal blog); The Record corroborates but does not independently verify the technical specifics. Vendor-as-primary carve-out applies — Microsoft is the disclosing party and the action's filer." This is exactly what iter-1 requested. Confirmed clean.

### Independent truth pass (items not covered above)

**Sparx region/footer:** Footer at line 54 includes `Region: switzerland, europe, global` and body (line 52) states "Sparx Enterprise Architect is one of the dominant tools for IT enterprise-architecture modelling across EU and Swiss federal / cantonal IT units." Both the CH/EU deployment posture claim and the `switzerland` region tag are present. CERT-PL source fetched — confirmed live, confirmed 5 CVEs, confirmed PCS ≤6.1 and EA ≤17.1 as vulnerable versions, confirms no vendor patch. No issues.

**MSRC CVE-2026-41091 / CVE-2026-45584:** Both MSRC URLs are React SPA shells — bridge returns HTML-only (no data). Consistent with iter-1's treatment via OData. No liveness issue surfaced (HTTP 200 returned by bridge), and iter-1 independently confirmed these via OData path. No regression.

**Storm-2949 MITRE T-IDs:** T1078.004, T1556.006, T1098.005, T1530, T1083, T1552.001, T1021.007, T1562.007, T1041 — all present in the brief, unchanged from iter-1 confirmation. No drift detected. Storm-2949 Microsoft TI article fetched and confirmed live, matching all Azure operation names and the SSPR attack chain described in the brief.

**vm2 heading — new residual (see F3 delta above and finding below).**

### Broken / unreachable URLs

No broken URLs detected in this iteration. (All fetched URLs returned HTTP 200 or functional content; MSRC SPA shells are expected behaviour, not liveness failures.)

### Claim does not support the citation — F3 (residual)

**F3 (residual from F3 vm2 remediation)** — § 2 vm2 section heading: *"vm2 Node.js sandbox — 12 critical CVEs (CVE-2026-43997 / 43999 / 44005 / 44006 / 44008 / 44009 et al.), sandbox escape to host RCE, **patch to 3.11.2**"* (line 106). The cited primary BSI WID-SEC-2026-1583 (confirmed by iter-1 bridge fetch to list product_version_range `<3.11.4`, i.e. 3.11.4 is the comprehensive fix) contradicts the heading. The body, action item, and § 7 note all correctly say 3.11.4. The heading alone says 3.11.2. This is a stale heading — the main agent updated the body and action items but not the heading. Fix: update heading to "patch to ≥ 3.11.4" (or "sandbox escape to host RCE, upgrade to ≥ 3.11.4").

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

One truth-class residual: vm2 section heading still says "patch to 3.11.2" (contradicts body, action item, § 7, and BSI primary source which specifies 3.11.4). All other iter-1 remediations confirmed clean. No new defects introduced by remediations.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "vm2 Node.js sandbox — section heading"
  url_or_quote: "vm2 Node.js sandbox — 12 critical CVEs (CVE-2026-43997 / 43999 / 44005 / 44006 / 44008 / 44009 et al.), sandbox escape to host RCE, patch to 3.11.2"
  summary: "Heading at line 106 still says 'patch to 3.11.2'. Body text (line 116), action item (line 214), and § 7 contradiction note (line 237) all correctly say vm2 ≥ 3.11.4 per BSI WID-SEC-2026-1583. The heading was not updated during iter-1 remediation. Fix: change heading substring 'patch to 3.11.2' to 'upgrade to ≥ 3.11.4'."
```
