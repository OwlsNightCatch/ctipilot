**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-14T13:26:20Z · ended_at=2026-07-14T13:35:58Z · duration_seconds=578

## Verification report — 2026-07-14T1210Z-intel (iteration 4)

### Prior-iteration delta confirmed
Iteration 3's F14 remediation on `2026-07-14/asyncapi-npm-supply-chain-compromise-github-actions` § Defender takeaway holds. The body now reads "This is a recurring 2026 pattern of `pull_request_target` 'pwn request' abuse feeding npm-ecosystem backdoors" — the unsourced ordinal ("the third distinct 2026 wave") is gone, and the sourced recurring-pattern point is retained without a quantifier. Re-fetched both cited sources (Wiz, SafeDep) in full: neither states a wave count, and the entry no longer asserts one. Confirmed clean.

I also independently re-verified all iteration 1–3 remediations while reading cold:
- ESET entry's "no complicated exploitation primitive" / local-post-auth framing (iter-1 F4 #1): body now reads "exploitation requires no complex exploitation primitive — 'only a copy of an old, still-trusted, but unrevoked shim binary'... writing to the ESP is itself a privileged local operation... a persistence/defense-evasion primitive for an attacker who already has that access" — consistent with frontmatter `vector: local, auth: post-auth` and with ESET's own text (verified verbatim below). Holds.
- ESET entry's in-the-wild/IOC-withholding framing (iter-1 F4 #2): body/summary now read "no in-the-wild exploitation has been reported" (passive, not attributed to ESET) and the IOC-withholding sentence is cited to ESET's own wording ("present on thousands of systems that have never been compromised via these loaders") — verified verbatim against the live ESET page. Holds.
- Run-record jargon leak (iter-1 F11): the § Verification & coverage notes prose body (lines 149 onward) contains no "sub-agent"/"Phase N"/"spawn"/"main agent" language. The only remaining `S1`/`S2`/`S3`/`S4` and "main-agent Phase 4" mentions are in the frontmatter `sub_agents:` and `bridge_uses:` telemetry blocks, which are operator/Ops-dashboard surfaces (confirmed via `site/build.py`'s `_ops_render_bridge_uses` / Ops-panel rendering, distinct from the rendered "verification & coverage notes" reader surface) — iteration 1's remediation note explicitly says these were left intact by design. Holds, no re-leak.
- AsyncAPI single-source→multi-source upgrade (iter-2, SafeDep corroboration): re-fetched SafeDep independently; confirmed it covers the identical incident (matching package/version set, the 06:58 UTC commit, the `miasma-train-p1` self-ID string) and the sourcing_note/evidence accurately reflect it. Holds.

### Unsupported / hallucinated facts

- **F4** — entry `2026-07-14/progress-sharefile-szc-active-exploitation-confirmed` — frontmatter `techniques: [T1190, T1505.003]`. `T1505.003` (Server Software Component: Web Shell) has no supporting behavior in this entry's body and no basis in any of this entry's three cited sources. The body only describes (a) Shadowserver honeypots confirming in-the-wild exploitation attempts against the pre-auth auth-bypass CVE-2026-2699, (b) the exposed-instance count collapsing from ~30,000 to ~1,000, (c) Progress restoring cloud access while on-prem controllers stay off, and (d) Allan Liska's Clop hypothesis — none of which mentions a web shell, an ASPX drop, or any server-side implant artifact. I fetched all three cited sources in full this iteration:
  - BankInfoSecurity (primary) — mentions "zone takeover" and references CVE-2026-2701/RCE only in the context of watchTowr's April disclosure tooling caveat ("This tool does not perform the full exploitation [zone takeover] and does not chain this vulnerability with RCE [CVE-2026-2701]"); no web-shell mechanism is described for the confirmed 2026-07-10 exploitation.
  - The Register (corroborating) — no CVE, no web-shell, no exploitation-mechanism detail at all (confirmed via WebFetch: "No specific CVE is mentioned").
  - status.sharefile.com (corroborating) — a vendor status page, no technical detail.
  - This entry's own `cves[]` block lists only `CVE-2026-2699` (the auth-bypass CVE) — it deliberately excludes `CVE-2026-2701` (the RCE/file-write CVE that the *original*, immutable 2026-07-13 entry maps to the ASPX web-shell chain), so `T1505.003` is orphaned relative to this entry's own evidence base. The technique is already correctly carried on the linked `update_of` target (`2026-07-13/progress-sharefile-storage-zone-controller-shutdown`), so nothing is lost store-wide — but per check 4b ("an id with no matching body behavior or source basis is F4"), it should not also appear on this delta entry without a supporting clause or source. Low-severity (the underlying incident genuinely does involve that technique via the linked original), but a genuine mapping-support gap in this specific file. Suggested fix: drop `T1505.003` from this entry's `techniques[]` (keep `T1190`), since the delta itself doesn't carry that behavior.

### Verdict

`NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)`

Everything else checked out clean under a full cold re-read + re-fetch of every cited URL across all three entries (Wiz, SafeDep, ESET/WeLiveSecurity, CERT/CC VU#616257, BankInfoSecurity, The Register, status.sharefile.com), plus the CVE.org records for CVE-2026-8863, CVE-2026-10797, and CVE-2026-2699, plus the NVD CNA (Progress Software Corporation) CVSS record. Notable things I specifically checked and found correct (recording so a future iteration doesn't need to re-derive them):
- All four AsyncAPI evidence quotes are exact, contiguous, verbatim substrings of the live Wiz/SafeDep pages (checked against raw jina-reader markdown, not just WebFetch's summarized paraphrase).
- The ESET entry's two evidence quotes and the CERT/CC BYOVD quote are exact and verbatim.
- All three ShareFile evidence quotes are exact and verbatim against the raw BankInfoSecurity markdown.
- CVE-2026-10797 maps correctly to the signature-length validation mismatch (ESET's article explicitly says "It is now tracked as CVE-2026-10797" immediately before describing that exact bug) — this CVE is `RESERVED` on cve.org (no published description yet), but it resolves and is attributed correctly by the entry's own primary source, so no F4.
- CVE-2026-8863's CVE.org description ("Multiple Microsoft-signed UEFI SHIM bootloaders are vulnerable to SecureBoot bypass... An attacker with administrative privileges or the ability to modify the boot process...") is consistent with the entry's local/post-auth classification and with the entry's framing of it as the umbrella "forgotten shim set" CVE.
- The ShareFile entry's `cvss: "9.8"` for CVE-2026-2699 is correct against the vendor CNA (Progress Software Corporation) score synced to NVD (9.8 CRITICAL), even though the entry's own cited BankInfoSecurity article states "a CVSS score of 9.9" (an apparent journalist transcription error) — the entry correctly favored the per-CVE authority over the roundup article's number, exactly as check 4 instructs. Not a defect.
- All three entries carry exactly one Admiralty `classification` block (reliability B / credibility 1 each), `org_triage: null`, `watchlist_hit: false` — consistent with this deployment's no-scheme, no-watchlist configuration.
- `actions[]` on all three entries pass the do-now bar: AsyncAPI's single action is version-specific and derived from this entry's own facts; ESET's single action names the exact tools ESET itself links (`sei-vsarvepalli/uefi-dbx-audit`, `microsoft/secureboot_objects`); ShareFile's `actions: []` is correct since the update carries no new action beyond the original entry's still-standing guidance.
- Registry additions (`incident:asyncapi-npm-github-actions-supply-chain-compromise-2026-07`, `tool:m-red-team-malware-framework` with aliases `miasma-train-p1`/`Miasma RAT`, `campaign:prt-scan-github-actions-pwn-request-token-theft`) are correctly typed (`overlaps-with` for the Miasma-framework link, not upgraded to attribution) and sourced; no name-collision (F15) — the potential Miasma-name overlap with the pre-existing `campaign:miasma-redhat-npm-supply-chain` (2026-06-02, attributed to TeamPCP) is explicitly disambiguated in both the entry body and the registry relation note.
- No IOCs, no vanity metrics, English throughout.
- All three entries clear the relevance bar for the Swiss/European SOC constituency (global supply-chain compromise with transferable lesson; ESET's Abitti/RHEL/public-sector-relevant vendor list; ShareFile's explicit Swiss/European on-prem file-exchange nexus).

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: operational
  item: "Progress ShareFile Storage Zone Controller — Shadowserver confirms active exploitation of CVE-2026-2699"
  url_or_quote: "techniques: [T1190, T1505.003]"
  summary: "T1505.003 (Web Shell) has no supporting behavior in this entry's body and no basis in any of its three cited sources (BankInfoSecurity, The Register, status.sharefile.com); this entry's own cves[] excludes CVE-2026-2701 (the RCE/web-shell CVE, which stays correctly mapped on the linked update_of original). Recommend dropping T1505.003 from this entry's techniques[] (keep T1190)."
```
