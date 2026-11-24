**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-24T05:37:27Z · ended_at=2026-11-24T05:51:54Z · duration_seconds=867

## Verification report — 2026-11-24T0355Z-intel (iteration 4)

Scope: post-fix pass. All 155 claims of `claims.iter4.yaml` have a verdict row in `verification.iter4.claims.yaml` (152 ok, 3 F3 low-confidence on one finding): the 5 changed claims, every claim of the Project Zero entry (18), and, because no time limit applies, every other claim of the other eight entries as well (so no sampling). Every cited URL was fetched this iteration: `extract` for articles and advisories, `pdf` for the Optimizely report, `url --direct` for the EUVD record, Equinor HTML, CNA CVE records, MSRC affectedProduct, `msrc cve`, `bsi-csaf`, `ncsc-nl csaf`, the `cisa-kev` bridge plus WebFetch for the CISA alert (title and both CVE names verbatim). `git diff HEAD` read for both updated entries. Gate re-run: 59 pass, 0 warn, 1 fail (`run-clock`, expected).

### Prior-iteration deltas (4), each re-fetched

- #1 Oracle citation date: fixed. `sources[]` and the Exposure citation now read 2026-09-15; the Oracle page's revision table reads "2026-September-15 | Rev 1. Initial Release." and the CNA record datePublished is 2026-09-15T20:06Z.
- #2 Exposure split: fixed. The WDAC / UMCI-without-Dynamic-Code-Security clause is cited to Project Zero ("If an enterprise is deploying a WDAC code integrity policy ... The `Dynamic Code Security` option isn't enabled by default"; "WDAC is a supported security boundary"); the VirtualBox clause is cited to Oracle (7.2.16, "This vulnerability applies to Windows host only.").
- #3 Headline: fixed. "PPL bypass expected to remain" matches "that should still be bypassable". (The title still carries the unqualified wording, see F4 below.)
- #4 Exposure scope: fixed. "7.2.16 or likely earlier builds" matches Oracle: "it is likely that earlier versions of affected releases are also affected by these vulnerabilities".

### Citation does not support the claim

- #1 [F3, low confidence] `2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398` (claims ebbbabc0c7, e68e32ec11, 7075cee9fb)
  - Quote: "**Detection:** the post says hooks and audits on image loads do not see this load"; summary "so hooks and audits on image loads never see the load"; body "so image-load hooks and audits never see it".
  - Source: the post says "Any protection code which is expecting to check the loaded image section will not see the load" and "Any protections which rely on verifying an image's signature or location can be notified". The word "audit" is not on the page. The Detection line attributes the wording to the post ("the post says"). Fix: use the post's own wording ("protection code that checks the loaded image section") in all three places, or stop attributing "audits" to the post.

### Unsupported / hallucinated facts

- #2 [F4, low confidence] `2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398` (title)
  - Quote: "...the same behaviour defeated VirtualBox's Windows process hardening (CVE-2026-87268) and still yields a protected-process bypass".
  - Source: "The use of `WLDP_LOCKDOWN_IS_ENFORCE` specifically checks for UMCI being enabled and disabling loading from memory. However this wouldn't change the behavior in PPL therefore that should still be bypassable." An expectation, not a retest. The body ("Forshaw expects it to remain bypassable") and the corrected headline ("expected to remain") say so; the title states it as fact. Fix: "and is expected to remain a protected-process bypass".

### Editorial / less-is-more flags (advisory)

- #3 [F11, low confidence] `2026-11-24/azure-api-management-classic-secrets-exposed-nsm-advisory`: the Equinor citation and `sources[]` date read 2026-11-20. The page's JSON-LD gives datePublished 2026-11-17T17:55Z and dateModified 2026-11-20T08:12Z; the cited clause draws on the 17, 19 and 20 November updates. 2026-11-20 is the date of the last update relied on, so it is defensible; a one-clause note in `sourcing_note` (as for the Ohey page in the OptimJack entry) would settle it. May be left.

### Checks that came back clean (no finding)

- Project Zero entry, every claim: post, MSRC SUG per-CVE record (Important, 8.8, publicly disclosed Yes, exploited No, release 2026-10-13), MSRC affectedProduct (24 rows across Windows 10 1607 to 22H2, Windows 11 23H2 to 26H2, Server 2012 to 2025; KB5126868, KB5127666 to KB5127668, KB5127683 to KB5127694; fixed builds 4.8.9363.0, 4.8.10008.0 on 26H2 only, 4.8.4811.0, 4.7.4150.0) and Oracle (CVE-2026-87268 CVSS 7.8, 7.2.16, Note 1 Windows host only, credit James Forshaw, Rev 1 2026-09-15) all match `cves[]`, Exposure, Defender takeaway and the evidence quotes (both PZ quotes and the MSRC description are contiguous). Techniques T1218.009 (regasm), T1546.015 (COM hijack) and T1620 (loading from a memory buffer) are supported by the post.
- Changelog contract (4c), both updated entries: `git diff HEAD` changes exactly the fields each record names (Vates: title, summary, entities, cves, sources, evidence, sourcing_note, tags, body; OptimJack: sources, evidence, sourcing_note, actions, body); `updated_at` unmoved in both (OptimJack stays 2026-11-22T14:54:05Z); headings equal `at`; no silent edit; no supersession (no "no CVE assigned" line survives in the Vates entry; the OptimJack 04:21 versus 07:51 disagreement is stated, not resolved). Both are defensible as `improvement`.
- Vates: EUVD record (assigner GitHub_M, published Nov 23 2026, 9.8, "actively exploited in the wild", fixed 6.9.2 and 6.10.1, ranges `< 6.9.2`, `6.10.0, < 6.10.1`, xo-server `< 5.211.2`, `5.213.0, < 5.213.1`), GHSA (dated 2026-11-20, root cause, one-request PoC, "The attacker does not choose which token...") and Vates advisory (Critical, 2026-11-10, detection and mitigation items) support every sentence; BleepingComputer does name 6.9.1 and 6.10.0.
- OptimJack: Optimizely PDF supports 07:51 / 13:34 / 16:10 / 22:24 UTC, the exposure window, "act as administrator users without those users' credentials", hosted-iframe carve-out, withdrawn guidance and the eight customer actions; both new evidence quotes are contiguous; Krebs supports 68 / 50 / 24 (15 percent), dateline 2026-11-17 (Report URI's own table also lists 17 sites where connect-src blocked the theft; omitting that row is not a misstatement); Report URI 04:21 first injection, 188 snippets / 178 organisations; Hudson Rock 21 properties, unibas.ch StorifyMe 2026-11-14 03:27; Ohey 2026-11-13 and 2026-11-16 statements; Zscaler 450 / 3,000 and advice; Amirul two CSP-blocked sites. Action 3 is concrete and narrowed to transaction review and log retention.
- BabidiGhost (SOCRadar, ZATAZ x2), Entra (BleepingComputer, Netzwoche), APIM (NSM, SecurityWeek, Equinor, Skagerak, Kristiansen), N-able (N-able blog, THN, SecurityWeek, GHSA, CISA alert and KEV bridge), F5 (THN, BSI CSAF lists only CVE-2026-123637 with the five fixed-build ranges, NCSC-NL CSAF 12 CVEs medium / high, all six F5 CNA records: 9.8 and 9.3, Kheirkhah credited on four, F5 on two, the same five BIGIP-...-ENG builds and BNK-...-EHF1 builds) and Symantec: every cited sentence, number and date traces to the page; all evidence quotes (including NSM, ZATAZ and BSI originals) are contiguous substrings and the translations are faithful.
- Dedup: no new entry shares a CVE with an existing one (CVE-2023-38646 appears only in BabidiGhost, as a background reference); the only vendor overlap (N-able N-central, 2026-11-10) is stated by THN to be unrelated; CVE-2026-94127 is described as a different flaw; the referenced Symantec retailer entry exists; the MONAI KEV row is COVERED by the 2026-11-22 entry. All `entities[]` keys exist in the registry; the new relation edges carry a source entry and state only what the sources state (BabidiGhost `overlaps-with` BlackHatSect0r, not attribution); the three product records are referenced by their incidents' `affects` edges, so none is orphaned.
- Style: no IOC in any entry, no em dash outside changelog headings, no pipeline vocabulary in reader-facing prose.
- Classification and priority: letters consistent with sources.json tiers (NSM A, BSI/NCSC-NL A, N-able and CISA A, SOCRadar C, Project Zero B, Symantec B, BleepingComputer B); credibility numbers match the corroboration shown; APIM `high` clears the bar (a product the constituency can run, NSM instructs rotation within days); F5, N-able, Project Zero, Entra and Symantec `notable` are right (configuration-dependent and unexploited, hosted already patched, fixed in October, nothing to patch, single vendor); no `critical`.
- Run record: counts by kind, KEV disposition (kev-window.txt: MONAI COVERED, N-able NOT COVERED then published), source promotions (ubuntu-usn, bsi-press, aws-security-blog, aws-security-bulletins to active; nsm-no and advisory-splunk added as candidates; ohey-ca recipe) and the relation note all hold against `git diff HEAD` of sources.json and registry.yaml; the contradiction notes match the entries.
- Missed angles: none found. Two standing searches (in-window exploited advisories; Swiss BACS / municipal incidents) surfaced only items already in the store (Ivanti CVE-2026-104935 chain, FreeSwitch, Aspera, Chrome and Outlook zero-days, Basel-Landschaft). Coverage looks complete on the critical/high signal.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 1)

Both truth findings are low-confidence wording points on the Project Zero entry and are one-line edits (title: "is expected to remain"; "audits" replaced by the post's wording). Everything else, including all four prior-iteration remediations, verified clean against pages fetched this iteration.

### Findings summary (machine-readable)

See `work/2026-11-24T0355Z-intel/verification.iter4.findings.yaml` (3 records: F4 low confidence, F3 low confidence, F11 low confidence).
