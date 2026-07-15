**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-15T05:23:05Z · ended_at=2026-07-15T05:31:33Z · duration_seconds=508

## Verification report — 2026-07-15T0409Z-intel (iteration 4)

### Prior-iteration delta verification

Verified the iteration-3 remediation on `microsoft-july-patch-tuesday-sharepoint-dynamics-followup.md` (CVE-2026-55040 public-PoC overstatement). Confirmed holding: `cves[0].status` is `[patch-available]` (no `poc-public`), `tags` carries no PoC-related tag, the title/headline/summary/body all frame CVE-2026-55040 as a Pwn2Own-demonstrated chain under a 30-day disclosure embargo, and `sourcing_note` states "no public PoC exists at composition." Re-fetched the Rapid7 primary directly (`tools/fetch_source.py url ... --direct`) and confirmed verbatim: "Rapid7 Labs has chained the authentication bypass CVE-2026-55040 with a separate RCE vulnerability for unauthenticated RCE. Patching CVE-2026-55040 will successfully break this exploit chain... The RCE component has been disclosed to Microsoft and is expected to be patched in the scheduled August patch cycle." No public-PoC claim anywhere on the page. Priority `high` is defensible: the SharePoint bypass is Pwn2Own-demonstrated (real, working exploit exists, just embargoed) and the Dynamics 365 CVE-2026-55944 is pre-auth RCE rated "Exploitation More Likely" by Microsoft's own OData record — both clear a TL;DR bar even without confirmed in-the-wild exploitation.

### Unsupported / hallucinated facts

- **F4** — `entries/2026-07-15/microsoft-july-patch-tuesday-sharepoint-dynamics-followup.md`, `cves[3]` (CVE-2026-58644) `fixed: "July 2026 cumulative update"`, and body: "CVE-2026-50522 and CVE-2026-58644 ... are fixed in the July cumulative update." The entry's own cited authority — the MSRC per-CVE record (fetched via `tools/fetch_source.py jina https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2026-58644`, the same OData/update-guide source the sourcing_note says was used) — carries a second revision dated the same day: "1.1 — Jul 14, 2026 — The Patch for this issue was released but the CVE was inadvertently left out of the Patch Tuesday June 2026 release." That note indicates the underlying code fix predates the July cycle (it shipped with the June 2026 cumulative update); only the CVE's public disclosure/documentation was delayed to July. Stating flatly "fixed in the July cumulative update" therefore overclaims: a reader who already applied June's update may already be covered for this specific CVE, and the entry gives them no way to know that. Recommend adding a short clause (e.g., "Microsoft's own revision note for CVE-2026-58644 states the fix already shipped with the June 2026 update and only the CVE record was delayed to July — teams that installed June's cumulative update are already covered for this one") and/or softening `fixed:` to reflect the actual patch-availability timing rather than the CVE-publication timing. CVE-2026-50522's revision history carries no equivalent note (single revision, "Information published") — this defect is specific to CVE-2026-58644.

- **F4** — `entries/2026-07-15/microsoft-july-patch-tuesday-sharepoint-dynamics-followup.md`, `techniques: [T1190, T1078]`. T1078 ("Valid Accounts") describes an adversary obtaining and abusing credentials of an *existing* account to authenticate normally. The body describes the opposite mechanism for CVE-2026-55040: "a remote unauthenticated attacker who knows a target's Active Directory SID or User Principal Name can forge identity and operate as that SharePoint user or administrator" — a JWT-forgery authentication bypass where no real credential is ever presented or used. No sentence in the body describes use of a stolen/valid credential. Checked `attack/enterprise-attack.json`: T1606 ("Forge Web Credentials," active, not revoked/deprecated) is the technique whose definition (forging session/token-based credential material, e.g. SAML tokens, to gain access to web applications) matches the described JWT-forgery mechanism far more closely than T1078. Recommend replacing T1078 with T1606 in `techniques[]` (T1190 for the exploit-public-facing-application vector and the deserialization RCEs is correctly retained).

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 0)

Both findings are on the same entry (`microsoft-july-patch-tuesday-sharepoint-dynamics-followup.md`); the other three entries (`cisa-ics-batch-rockwell-abb-energy-water-ot.md`, `proofpoint-oauth-client-id-spoofing-entra-id-evasion.md`, `xai-grok-build-cli-repo-secrets-exfiltration.md`) and the run record verified clean against every check performed this iteration:

- All 4 CISA CSAF advisory URLs (icsa-26-195-01..04) fetched live via the CISA bridge and cross-checked against the cached CSAF JSON in `work/2026-07-15T0409Z-intel/csaf/` — every CVE id, CVSS score/vector, CWE class, affected/fixed version status (Rockwell ≤3.003→3.011; ABB T-MAC Plus 4.0-24→4.0-25; Edgenius →3.2.4.1; 800xA CVE-2025-13162 CVSS 4.4) matches exactly, including the iteration-1/2 remediations (ABB affected/fixed direction, Rockwell firmware-3.011 fix) still holding.
- MSRC per-CVE OData records for all four July Microsoft CVEs (55040, 55944, 50522, 58644) cross-checked against the cached JSON in `work/2026-07-15T0409Z-intel/` and re-fetched live via the jina reader where WebFetch returned an empty SPA shell — CVSS/vector/exploitability-rating/PR:N-vs-FAQ-Site-Owner discrepancy handling all confirmed accurate and properly disclosed in the sourcing_note.
- Rapid7, Proofpoint, The Register, GBHackers, Help Net Security and The Hacker News all fetched live (WebFetch or bridge `url --direct` fallback where WebFetch hit an anti-bot page); every `evidence[]` quote on all four entries confirmed as a verbatim, contiguous substring of the fetched page; every named entity (UNK_pyreq2323 700,000+ IDs Jan–Mar 2026 AWS, UNK_OutFlareAZ 3.7M IDs Dec 2025–Mar 2026 Cloudflare, Cereblab, disable_codebase_upload, AADSTS700016 semantics) confirmed against the source text.
- `entities/registry.yaml` entries for `actor:unk-pyreq2323`, `actor:unk-outflareaz`, `incident:xai-grok-build-cli-repo-exfiltration-2026-07` match the entries; `prior_coverage.json` shows no dedup collision on any of the CVEs or the two new incidents/entries this run — no `update_of` miss.
- Admiralty classification (reliability/credibility) reviewed on all four entries against § Organization context's scale definitions (credibility "2" = probably true/not independently confirmed is correctly applied to the CISA single-source-national-cert item and the Proofpoint single-origin-research item, consistent with the definitions in `config/org-profile.yaml`); no `org_triage` blocks present anywhere (consistent with no scheme configured); no `watchlist_hit: true` anywhere.
- `actions[]` on all four entries reviewed against the do-now bar — none generic, none restating body guidance, none padded (1–2 actions each, all concrete and derived from the entry's own cited mechanics).
- Priority calibration (`notable` ×2, `high` ×1) reviewed against check 5b — all defensible on the stated facts, no under- or over-alerting.
- Relevance (check 5) reviewed on all four, including the stricter breach/incident bar on the xAI Grok entry (no direct constituency nexus, but the entry itself names the transferable governance lesson — reviewing filesystem/git scope before onboarding an AI coding CLI — which clears the bar).
- No IOCs, no vanity metrics, English throughout.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: operational
  item: "microsoft-july-patch-tuesday-sharepoint-dynamics-followup — CVE-2026-58644"
  url_or_quote: "cves[3].fixed: \"July 2026 cumulative update\" / body: \"...are fixed in the July cumulative update\""
  summary: "MSRC's own revision history for CVE-2026-58644 (fetched via jina reader) states: 'The Patch for this issue was released but the CVE was inadvertently left out of the Patch Tuesday June 2026 release' — the code fix predates July (shipped with June's CU); only the CVE documentation was delayed. 'Fixed in July' overclaims and could mislead teams who already applied June's update."
- code: F4
  category: hallucinated-fact
  section: operational
  item: "microsoft-july-patch-tuesday-sharepoint-dynamics-followup — techniques[]"
  url_or_quote: "techniques: [T1190, T1078]"
  summary: "T1078 (Valid Accounts) does not match the body's described CVE-2026-55040 mechanism — a JWT-forgery authentication bypass with no valid/stolen credential ever used. T1606 (Forge Web Credentials, active/non-revoked in attack/enterprise-attack.json) is the correct fit."
```
