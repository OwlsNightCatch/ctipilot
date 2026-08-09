**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-09T13:17:48Z · ended_at=2026-08-09T13:29:40Z · duration_seconds=712

# Retrospective audit truth pass — batch B1

**Run:** 2026-08-09T1315Z-audit · **Window:** 2026-08-02T13:09:58Z → 2026-08-09T13:15:57Z
**Headline: 19 clean / 20.** 1 imprecision, 0 factual errors.

## What was actually checked

This was a ground-truth pass, not a re-read of the entries' own narrative. For every entry in the batch:

- **Per-CVE authority, never a roundup.** Each `cves[]` id and CVSS was re-read from the record that owns
  it — `cveawg.mitre.org/api/cve/<ID>` for the Joomla, Adobe and marimo identifiers, and the vendor/CERT
  advisory itself for the Phoenix Contact set. `containers.cna.metrics` was separated from
  `containers.adp[].metrics` in each case to answer who scored what on which CVSS version.
- **Every `evidence[]` quote as a contiguous substring** of the page it is attributed to, fetched this pass
  (56 URLs; ledger in `url-liveness.tsv`). Nine apparent mismatches were run down individually and all nine
  proved to be HTML-tag whitespace artifacts of text extraction (`"campaigns , including"`, `"0.3 btc ."`,
  `"cve-2026-42897 ,"`, `"( xpdb )"`) or a gzip-decoding failure on one host — the quotes are verbatim on the
  rendered pages. No splice, no ellipsis, no de-hedged rewrite was found anywhere in the batch.
- **Every `techniques[]` id against the pinned dataset** (`attack/enterprise-attack.json`, ATT&CK v19.1),
  mechanically. All 51 distinct ids across the batch are present, non-revoked and non-deprecated, and each
  maps to a behaviour its entry actually describes.
- **Every `sources[]` URL** for liveness and specificity — no homepage, listing index, news category or
  NVD/MITRE per-CVE page appears as a source anywhere in the batch.
- Frontmatter⇔body agreement, `classification` consistency, `org_triage`/`watchlist_hit` (all correctly
  null/false for this deployment), `closed_sources` (all empty), and an IOC regex sweep (clean — the only
  hits were IBM WebSphere version strings `9.0.5.29` / `8.5.5.31`).

## The one finding

**`entries/2026-08-02/sp-page-builder-cve-2026-65766-preauth-sqli-mail-relay.md` — imprecision, sourcing_note only.**
The note says *"The discloser's own lower CVSS 4.0 self-assessments (8.7 / 6.9 / 7.1 / 7.2) are named in the
body"*. Only 8.7 is named in the body. Worse, the sequence directly follows a sentence enumerating the CNA
scores in the CVE order 65766 / 65877 / 65878 / 65876, so a positional read yields three wrong mappings.
mySites.guru's own CVSS 4.0 table assigns 8.7 to CVE-2026-65766, 7.2 to CVE-2026-65878, 7.1 to
CVE-2026-65877 and 6.9 to CVE-2026-65879; CVE-2026-65876 has no discloser self-score at all. This is exactly
the positional-guess failure mode the audit mandate names — caught here in metadata rather than in a
reader-facing claim. Everything substantive in that entry is correct: all five ids, the CNA CVSS 4.0 scores
(9.2 / 8.2 / 8.3 / 9.2), the fact that CVE-2026-65879 carries **no** CNA metrics and that its 9.8 is a
CISA-ADP CVSS 3.1 score on an incomparable scale, the 1.0.0–6.7.0 affected range, the 6.7.1 fix, and the
"five issues, not four" claim.

## What held up under pressure

Three entries were built to be hard to verify and all three survived:

- **The two correction entries** (GPT5.6/WP2Shell and Unit 42) both corrected an earlier store entry against
  the *same* primary. Re-fetching those primaries confirms both corrections. The Searchlight post's narrative
  ("Before starting, I cloned the latest stable WordPress release into main/ and removed the .git directory…
  it had indeed discovered a fully pre-auth SQLi") supports original discovery, and the entry is honest that
  the model was told a chain existed. Unit 42's Table 2 row for CVE-2026-39987 reads *"Marimo Notebook | 9.8 |
  Manual | Active exploitation, command execution confirmed"* — exactly what the correction restores, and the
  entry openly carries 9.3 in `cves[]` because that is the owning record's CVSS 4.0 score.
- **The supply-chain weekly** makes a cross-vendor attribution claim that could easily have been an
  analytical-link-as-fact defect. It is not: GTIG does attribute axios to MIDNIGHT NEPTUNE (formerly UNC1069),
  Amazon does attribute to SAPPHIRE SLEET at medium confidence, and the entry states plainly that neither
  vendor asserts the equivalence, citing that bridge to CyberScoop at the clause that makes it.
- **The water-PLC weekly** declines attribution where the sources decline it, and separates the Iran framing's
  two non-attributive origins. The FBI/EPA and CISA text supports every mechanic and count it carries.

## Two things this pass could not verify (not defects)

- `https://censys.com/blog/cisa-alert-water-tower-plc-targeting/` returned **HTTP 403 to both the direct
  bridge and the jina reader**. The 4,117 internet-exposed S7-1200 count and the 86.0% four-country
  concentration in `weekly-w31-water-plc-lockouts-european-exposure` therefore stand unrefuted but
  unconfirmed by this audit. Worth a retry in a later batch or from a different egress.
- `https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release` sits behind a bot/CAPTCHA challenge.
  It is a corroborating source with no `evidence[]` quote depending on it, so nothing in
  `weekly-w31-joomla-extension-wave-status` rests on it.

Two other hosts needed transport escalation and then resolved cleanly: `stadlerrail.com` (JS SPA — jina) and
`security-hub.ncsc.admin.ch` (SPA — `fetch_source.py ncsc-csh post 12577`, which confirms post 12577 is the
CVE-2026-42897 OWA advisory the entry uses it for).
