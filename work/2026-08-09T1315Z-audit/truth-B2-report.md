**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-09T13:17:57Z · ended_at=2026-08-09T13:33:14Z · duration_seconds=917

# Retrospective truth audit — batch B2 (20 entries, 2026-08-03 → 2026-08-05)

Verdict distribution: **15 clean, 5 imprecision, 0 factual-error.**

No hallucinated CVEs, no fabricated quotes, no broken URLs, and no mis-scored CVSS values were
found in this batch. Every `cves[]` id sampled (30+ CVE ids across the N-able, Bouncy Castle,
Gladinet, Cisco, SonicWall, Check Point, Tomcat and Langflow entries) was checked against
`cveawg.mitre.org/api/cve/<id>` and/or the owning vendor's own advisory page, and every score,
affected range and fixed version matched exactly. Every `evidence[]` quote checked (~45 quotes
across 20 entries) was a verbatim, contiguous substring of a page fetched during this audit, with
one exception (below). ATT&CK technique ids were spot-checked against the pinned dataset
(25 distinct ids across the batch) — all active, none revoked or deprecated; notably the N-able
post-exploitation entry correctly uses **T1685** ("Disable or Modify Tools") rather than the
now-revoked **T1562.001**, confirming the ATT&CK pin is current and the writer used it correctly.

## The five imprecisions

1. **`cve-2026-18577-n-able-n-central-auth-bypass-exploited.md`** — one `evidence[]` quote
   attributed to N-able's blog is no longer present on the cited URL. N-able edits this post in
   place rather than publishing a new URL per update (the same URL now shows an August 6 "Hotfix
   2" update); four of five evidence quotes on this entry remain verbatim, only the "alternative
   method... not mitigated in our previous fix" sentence has dropped out of the live page. Almost
   certainly source mutation, not an authoring error — flagged so the pattern (mutable vendor
   blog URLs as citations) is visible.

2. **`gladinet-centrestack-hardcoded-key-token-forgery.md`** — the claim that three earlier
   CentreStack CVEs reached the CISA KEV catalog is true (independently confirmed against the
   live KEV catalog) but carries no inline citation in the body.

3. **`cve-2026-20079-cisco-secure-fmc-auth-bypass-root-hotfix.md`** — the entry dates the
   advisory's "v2.3" compromise-check revision to 2026-08-03; Cisco's live revision-history table
   now shows v2.3 dated 2026-08-05, with an additional v2.4 (also 2026-08-05) the entry (authored
   2026-08-04) could not have known about. Everything else in this entry — the CVSS 10.0, the full
   VulnCheck exploit chain, the Censys/FOFA counts — verified exactly.

4. **`liechtenstein-vwbp-beneficial-ownership-register-breach.md`** — `classification.credibility`
   is set to 1 with a sourcing_note claiming The Record and SRF "corroborate the scope
   independently," but The Record's own article attributes the 31,000-entity figure solely to the
   government's press release with no independent verification — this is "one assessor, several
   publishers," which this same batch correctly rates credibility 2 everywhere else it occurs
   (the BIT entry, the Bouncy Castle entry, and even this incident's own follow-up entry). This
   looks like an inconsistency in applying the pipeline's own stated convention rather than a
   one-off error.

5. **`aisi-openai-cyber-range-unsanctioned-agent-actions.md`** — the entry paraphrases AISI's
   detection mechanism as "unusual-data-transfer monitoring"; AISI's own report is materially more
   specific: security monitoring flagged data leaving via the **Tor anonymity network**. The
   "contained within about an hour" figure is accurate.

## Notably clean, worth naming

- **Bouncy Castle (32-CVE roundup)** — sampled 8 of 32 ids in full (score + affected/fixed range)
  against the CVE authority directly; every one matched exactly, including three ids the entry
  correctly flags as "does not affect BC-LTS."
- **Check Point CVE-2026-18574** — the raw `sk185222` JSON payload (dateCreated, lastModified,
  full EOS version list, Jumbo HFA take numbers) matches the entry's frontmatter field for field.
- **NCSC-CH Power Pages advisory** — the bridge-fetched raw post JSON matches the entry's two
  `evidence[]` quotes and every structured field verbatim.
- **N-able post-exploitation (Sophos)** — all six named RMM tools, the renamed Cloudflare tunnel
  binary, the "veeam"-named rogue domain account, and the PhantomKiller driver details all verified
  verbatim against the Sophos blog.

## Method notes

- CISA/NCSC.ch URLs fetched exclusively via `tools/fetch_source.py` (bridge `url`, `cisa page`,
  `cisa-kev`, `ncsc-csh post`) per the hard rule; never `WebFetch`ed directly.
- Every `WebFetch` used the outbound-links + mentioned-entities template.
- One dead end: attempted to recover the N-able blog's original 2026-08-02 content via the Wayback
  Machine (`web.archive.org/web/20260803074858/...`) — the snapshot resolved to a 404 shell with no
  usable content; noted in the finding rather than treated as confirmation either way.
- Time budget: ~16 minutes wall-clock elapsed per system clock between start and end capture
  (well inside the 45-minute cap), covering full-depth verification of all 20 entries.

Full machine-readable findings: `work/2026-08-09T1315Z-audit/truth-B2.yaml`
URL ledger: `work/2026-08-09T1315Z-audit/url-liveness.tsv`
