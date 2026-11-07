**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-07T07:14:39Z · ended_at=2026-11-07T07:36:25Z · duration_seconds=1306

## Verification report — 2026-11-07T0256Z-intel (iteration 8)

Role: confirmation pass after a CLEAN iteration 7; read cold. Scope: 7 new entries, 6 updated entries (full read plus `git diff HEAD` for each), the run record, the dedup context, and all 237 ledger claims (`verification.iter8.claims.yaml`: 236 ok, 1 F14, 0 unreadable). Every cited page was fetched this iteration (extract, `url --direct`, structured recipes `ncsc-csh`, `cisa-kev`, SonicWall PSIRT API JSON, Siemens CSAF, OX Security feed, PDF recipe, WebFetch for cisa.gov). No prior-iteration deltas block was attached.

### Generic / oversight URLs (replace with specific article)

- **F2 #1 (low confidence).** `2026-09-15/cve-2026-76461-cisco-secure-email-gateway-sqli-root-rce`, sources[] primary: `https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json` is the whole-catalogue KEV feed (1,769 entries when fetched), a listing, cited for "CISA added the CVE ... the same day and flagged it for Forensic Triage Requirements". The record for CVE-2026-76461 is in it (dateAdded 2026-09-14, forensicTriage Yes), so the claim itself is supported; the issue is the same pattern iteration 1 ruled F2 on the Brotli entry. A per-CVE page exists (fetched this iteration): `https://www.cisa.gov/news-events/alerts/2026/09/14/cisa-adds-one-known-exploited-vulnerability-catalog` (it does not carry the forensic-triage flag, so the JSON could stay as a second source). The citation predates this run's record.

### Needs more research

- **F8 #1 (low confidence).** `2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole`, body: "On Alpine's official AWS and Azure images the passwordless account is the default alpine user, which can run doas without a password, so the bypass chains to root there" (OX Security). The Alpine advisory the entry also cites says the official tiny-cloud images "are safe on first boot" and "become exploitable as soon as any `$6$` hash exists on the machine", and lists "Cloud images configured through cloud-init, which writes `PasswordAuthentication no`" as not affected. That is the discriminator for which Alpine cloud instances are exposed and it dropped out of Exposure. Fix: one clause with Alpine's tiny-cloud caveat.

### Editorial / less-is-more flags (advisory)

- **F11 #1 (low confidence).** `2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack`, section 2026-11-07T03:53:29Z and record summary: NCSC post 13054 reads "across all relevant operations" and "Provide remote access through a secure VPN or protected network"; the section says "across all operations" and "allow remote access only through", the record summary says "any cooling plant". Ransom-ISAC states the scripted-pace reading ("a pace more consistent with a script or a bulk-programming function than with manual edits") for the 588-write burst only; the section's relative clause attaches it to both bursts. No decision changes; carried over from the iteration-7 advisory that was declined.

### Quantifier without source

- **F14 #1.** `2026-11-07/bossai-ai-agent-mesh-emergency-services-data-taiwan`, Exposure line: "TRU reports the three emergency-services cases as the gravest confirmed harm." Acronis TRU (`https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/`): "The gravest confirmed harm was the targeting of emergency-services data: patient-care records and dispatch case information from an organization that serves millions of residents." Two kinds of data, no count of three; the fire-dispatch vendor's default-credential panel sits in TRU's financial-sector paragraph with no gravity ranking, and the entry's own summary lists two cases. Fix: "the patient-care and dispatch records" or drop the count.

### Checks that found nothing (for the record)

- SonicWall: advisory tables, CVSS, CWE-308, "potential exploitation" wording, no-workaround, the three lower-severity flaws and both 8.8 flaws match the PSIRT API JSON; CISA alert 2026-11-06 and KEV record agree; the two quotes the gate could not machine-check are verbatim.
- Brotli multi-vendor entry: Siemens CSAF (SSA-045512 V1.2, SSA-443410 V1.1), Mitel MISA-2026-0010 rev 5.0 and the Cisco combined advisory v1.8 support every version, KB number, fix and caveat; Cisco's table has no per-CVE column and the entry says so. The earlier F7 (duplicate of the Node2Shell entry) was declined with reasons; both references[] are declared and the Siemens building-management and Mitel telephony angle is a distinct decision for this constituency, so I do not re-raise it.
- Changelog contract on all six updates: record `fields` cover every changed frontmatter line in `git diff HEAD`; each section carries a genuine delta; `updated_at` mirrors the non-internal `update` record; no supersession contradiction (Cisco "exploit code" sentence, Danfoss NCSC rating, WordPress exposure wording, OpenSSH status all consistent with the newest section).
- Style: no em dash outside section headings, no IOCs, no workflow vocabulary in any reader-facing field, translations faithful and `original` fields verbatim (Aargau, TUM, NCSC-NL).
- Entity keys all exist in `entities/registry.yaml`; no alias miss found. Classification, org_triage (all null), watchlist (none), priority calibration and `verification` values are consistent with the sources shown.
- Missed angles: only KEV addition in window is CVE-2026-19868 (covered; KEV 2026.11.06 also lists 2026-11-04 Apple and 2026-11-03 WordPress, both already in the store). Searches for in-window items (zero-day advisories 6 Nov, Swiss municipal incidents, Signal-support phishing, Exchange XSS zero-day) returned only older material, and the Storm-2603 SharePoint story is already covered on 2026-11-06. Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 1, advisory: 1)

All four findings are small. This is the capped iteration, so they publish as residuals if the cap rule applies; the F14 is the only one I can fully confirm, the other three are marked low confidence.

### Findings summary (machine-readable)

See `work/2026-11-07T0256Z-intel/verification.iter8.findings.yaml` (4 records: F14, F2, F8, F11).
