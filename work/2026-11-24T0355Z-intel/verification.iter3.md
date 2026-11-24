**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-24T05:22:42Z · ended_at=2026-11-24T05:35:19Z · duration_seconds=757

## Verification report — 2026-11-24T0355Z-intel (iteration 3)

Scope: post-fix pass, full ledger. All 154 claims of `claims.iter3.yaml` have a verdict row in `verification.iter3.claims.yaml` (151 ok, 2 F3, 1 F4): the 9 changed claims, every other claim of all nine touched entries (so no sampling). Every cited URL was fetched this iteration: `extract` for articles and advisories, `pdf` for the Optimizely report, `url --direct` for EUVD, CNA CVE records, MSRC SUG/affectedProduct, BSI and NCSC-NL CSAF, the `cisa-kev` bridge plus WebFetch for the CISA alert (title line verbatim). `git diff HEAD` read for both updated entries. Gate re-run: 59 pass, 0 warn, 1 fail (`run-clock`, expected).

### Prior-iteration deltas (12), each re-fetched

- #1 Vates `cves[].affected`: fixed. Now "xen-orchestra before 6.9.2 (stable) and before 6.10.1 (latest); xo-server before 5.211.2 (stable) and before 5.213.1 (latest)". EUVD lists xen-orchestra "< 6.9.2" and "6.10.0, < 6.10.1"; xo-server "< 5.211.2" and "5.213.0, < 5.213.1"; Vates "Xen Orchestra before 6.9.2 (stable) and 6.10.1 (latest): Affected". Frontmatter and body agree.
- #2 F5 hotfix wording: fixed. THN: "A system on a custom engineering hotfix needs a new one from the company's support team." The entry now attaches F5 support only to custom-hotfix systems.
- #3 BabidiGhost sourcing_note: fixed. SOCRadar: "Victims are anonymized by sector and country"; no country given for the insurer, banks or archives except that Belgium's share is driven by the municipal storage server. A Swiss victim is neither confirmed nor excluded.
- #4 Symantec: fixed. "The names were unique subdomains of a single token under oast[.]pro".
- #5 OptimJack withdrawn-guidance sentence: fixed. Cited to the Optimizely PDF, which says "it is now safe to re-enable it. Early guidance on 16 November advised turning it off. That guidance has been withdrawn."
- #6 Project Zero Exposure: version and platform now stated (Oracle row 7.2.16, Note 1 "applies to Windows host only"), but the remediation introduced two new defects, see F3 #1 and #2 below.
- #7 run record front matter: fixed, gate parses it.
- #8 Vates record summary: fixed (no metadata narration; fields list matches the diff exactly).
- #9 sourcing_note narration: fixed in all five (residual provenance phrases only).
- #10 Project Zero CVE-2026-87268 data: now sourced to Oracle (CVSS 7.8, 7.2.16, Windows host only confirmed on the page and in the Oracle CNA record).
- #11 orphan product records: fixed; both keys are in `entities[]` and exist in the registry.
- #12 Entra wording: fixed. BleepingComputer: "targeted phishing and social-engineering attacks"; action and Detection now say the same.

### Citation does not support the claim

- #1 [F3] `2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398 (sources[] and Exposure citation)`
  - Quote: "[Oracle, 2026-09-10](https://www.oracle.com/security-alerts/cspusep2026.html)"; sources[] `date: "2026-09-10"`.
  - The page's visible revision table reads "2026-September-15 | Rev 1. Initial Release."; the Oracle CVE record is datePublished 2026-09-15T20:06Z. 2026-09-10 is the page's meta "Updated Date" (2026-09-10T07:24:10Z). Five days of drift (check 2e). Fix: 2026-09-15 in sources[] and the body label.
- #2 [F3] `2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398 (Exposure, claim 7cd455230b)`
  - Quote: "**Exposure:** Windows hosts that rely on App Control for Business or WDAC user-mode code integrity as an application-control boundary without Dynamic Code Security, and Windows hosts that run Oracle VM VirtualBox 7.2.16 ([Oracle, 2026-09-10](...))."
  - Oracle's page carries only the VirtualBox clause. The WDAC / UMCI-without-Dynamic-Code-Security clause is not on it (it is from the Project Zero post: "If an enterprise is deploying a WDAC code integrity policy ... The `Dynamic Code Security` option isn't enabled by default", and MSRC's FAQ). The single terminal citation claims both clauses. Fix: Project Zero (or MSRC) after the first clause, Oracle after the second.

### Unsupported / hallucinated facts

- #3 [F4, low confidence] `2026-11-24/project-zero-net-code-integrity-bypass-cve-2026-108398 (headline)`
  - Quote: "Project Zero: one-bit change loads untrusted .NET assemblies past UMCI; fixed in October, PPL bypass remains".
  - Project Zero: "However this wouldn't change the behavior in PPL therefore that should still be bypassable." That is an expectation, not a retest. The body says "Forshaw expects it to remain bypassable", so the headline overstates the body. Fix: "PPL bypass expected to remain".

### Editorial / less-is-more flags (advisory)

- #4 [F11, low confidence] Project Zero Exposure names only "Oracle VM VirtualBox 7.2.16". Oracle's page says earlier unsupported versions are "not tested ... it is likely that earlier versions of affected releases are also affected". A host on an earlier build can read the line as out of scope. Optional wording: "7.2.16 and likely earlier builds"; Oracle names no fixed build.

### Checks that came back clean (no finding)

- Changelog contract (4c), both updated entries: diff changes exactly the fields each record names (Vates: title, summary, entities, cves, sources, evidence, sourcing_note, tags, body; OptimJack: sources, evidence, sourcing_note, actions, body); `updated_at` unmoved; headings equal `at`; no silent edit; no supersession (Vates "no CVE assigned" lines gone everywhere; OptimJack 04:21 versus 07:51 disagreement is stated, not resolved). Both are defensible as `improvement`.
- Evidence quotes: all contiguous on their pages (Vates, EUVD, GHSA, Optimizely PDF, SOCRadar, BleepingComputer, THN, Symantec, NSM and Skagerak originals, ZATAZ original, BSI CSAF original). Translations faithful.
- Figures traced to pages: N-able build 20261121.1943, CVSS 4.0 9.3 (GHSA PR:H), KEV dateAdded 2026-11-23 (bridge and WebFetch), RCA within two weeks; NSM builds 31936 / 31938; Krebs 68 / 50 / 24 (15 percent), dateline 2026-11-17; SOCRadar 23 archives, 8.6 GB, 48 accounts; Symantec 41 modules, 08:44 to 08:47 UTC, 50-char chunks; F5 CNA records (all six at CVSS 3.1 9.8, same five BIGIP-...-ENG builds, BNK-2.4.2/2.3.4/2.2.5-EHF1, four watchTowr credits and two F5); BSI CSAF lists only CVE-2026-123637; NCSC-NL CSAF 12 CVEs, Kans medium, Schade high; MSRC affectedProduct (24 rows, KB5126868, 5127666 to 5127668, 5127683 to 5127694, fixed builds 4.8.9363.0 / 4.8.10008.0 / 4.8.4811.0 / 4.7.4150.0), Important, 8.8, disclosed Yes, exploited No; Entra dates 07-23, 11-09, 11-19, 11-20.
- Dedup: no new entry shares a CVE with an existing one; the only vendor overlap (N-able N-central, 2026-11-10) is a different incident, which THN states ("unrelated to the N-central incident"); the referenced Symantec entry exists. Registry keys exist; BabidiGhost `overlaps-with` BlackHatSect0r edge matches the run notes.
- Style: no IOCs, no em dash, no pipeline vocabulary in reader-facing prose. Classification letters consistent with sources.json (vates A, socradar C, projectzero B, symantec B, bleepingcomputer B, nsm-no A, bsi-de A, advisories-ncsc-nl A).
- Run record notes: counts by kind, KEV disposition, source promotions (ubuntu-usn, bsi-press, aws-security-blog, aws-security-bulletins active; nsm-no, advisory-splunk candidates), registry relation, and contradiction notes hold on disk.
- Missed angles: none found. The Basel-Landschaft attack (20 applications, six servers) is already in the store (2026-11-21 entry); standing searches surfaced no further in-window critical item. Coverage looks complete on the critical/high signal.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 1)

The two F3 findings are small and both sit on the Oracle citation that the iteration-2 remediation added to the Project Zero entry (wrong publication date; one citation closing a two-source sentence). Everything else in the nine entries, the changelog contract and the prior-iteration remediations verified clean against pages fetched this iteration.

### Findings summary (machine-readable)

See `work/2026-11-24T0355Z-intel/verification.iter3.findings.yaml` (4 records: F3, F3, F4 low confidence, F11 low confidence).
