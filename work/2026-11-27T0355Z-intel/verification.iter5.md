**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-27T07:00:49Z · ended_at=2026-11-27T07:28:31Z · duration_seconds=1662

## Verification report — 2026-11-27T0355Z-intel (iteration 5)

Scope: post-fix pass after NEEDS_FIXES iteration 4. All 326 claims of `claims.iter5.yaml` have a verdict row in `verification.iter5.claims.yaml` (318 ok, 4 F3, 1 F4, 1 F5, 2 unreadable; `claim_ledger.py --coverage 5`: 326/326, 0 missing). Every cited page was fetched fresh this pass (97 URLs: extract, direct fetch, pdf, ncsc-csh, cisa-kev, WebFetch for the two cisa.gov alerts), and every non-special claim passage was machine-checked as a verbatim substring of the fetched page. The two lore.kernel.org pages (claims 6c2d56f937, cb45aff710) answer with a bot challenge; I did not push further against it and counted both unreadable (content corroborated on ENISA/CVE record, OpenSec, watchTowr).

### Prior-iteration deltas (all 5 re-read against sources)

| # | Remediation | Result |
|---|---|---|
| 1 ARTEX F4 (per-run) | summary, record summary and Detection say a per-installation counter ARTEX does not reset by default | True in those three places (Wiz: "Each installation runs its own counter and never resets it by default"; Cairn "resets its counters for every new project"). The body's update section lead still says "per-run numbering": see finding #1. |
| 2 Zammad F3 | public-statements citation restored on the agent-notes clause | True. Statement #2: "the attacker's scripts contain notes where the agent justifies its own actions". |
| 3 Zammad F4 | "OAuth tokens for the two shared mailboxes", no client-secret claim | True. Report Table 19 and the Q&A list XOAUTH2 tokens for csirt@ and report-abuse@, the IMAP cleartext password, the elastic credential, the Jira OAuth consumer private key; no client secret. |
| 4 Mitel F3 | main analysis narrowed to CVE-2026-133323; 2026-11-20 section cites all five | True. EUVD-2026-130382 carries CVE-2026-133323 only (datePublished Nov 19 2026, assigner mitre); EUVD-2026-130372, -130376, -130381, -130384 each carry one of the other four, all Nov 19, scores and MTLVULN ids match. |
| 5 Fragnesia F5 | CVE-2026-109618 advisory cited for the comparison | The comparison is true for all 20 trains (PAN-SA builds are two to four hotfixes above the PHP2Shell builds). The clause now ends on the advisory alone, which does not carry the bulletin's list: see finding #2. |

### Claims missing / citation does not support the claim

- #1 (F4) **ARTEX** "## Update — 2026-11-27T04:54:00Z", lead sentence: "Wiz Research shows how ARTEX and Cairn leak their per-run numbering into victim logs." Wiz: ARTEX "Each installation runs its own counter and never resets it by default", "Numbers climb across runs and targets"; only Cairn resets per project. Same wording iteration 4 flagged, left in this surface. Fix: "intent numbering" or name the per-installation and per-project counters.
- #2 (F3, low confidence) **Fragnesia** 2026-11-27 section, second paragraph: "It lists a first fixed PAN-OS build for this flaw in every train, later than the hotfix that fixes PHP2Shell ([Palo Alto Networks, 2026-10-27](CVE-2026-109618 advisory))". The advisory carries the PHP2Shell builds only ("Upgrade to 12.2.4-h1 or later."), not PAN-SA-2026-0015's per-train list; the date label matches neither the advisory's published (2026-10-21) nor updated (2026-10-29) date. Cite both pages.
- #3 (F3, low confidence) **nginx** body paragraph 3 and 2026-11-27 section: "nginx.org lists it as affecting 1.21.4 to 1.31.9 ([nginx.org, 2026-11-18])". The advisories page lists CVE-2026-132779 (K000163947, fixed in 1.31.10 of 2026-11-23), so that line cannot date from 2026-11-18. Label "as read 2026-11-27".
- #4 (F3, low confidence) **NFS2ROOT** body paragraph 1: "The announcement lists fixes in 6.12.117, 6.18.61, 7.3.2 and 7.4-rc1, and the record was later updated with 5.10.275, ... ([ENISA EUVD, 2026-11-23])". ENISA carries all eight versions and dateUpdated Nov 23; it does not say what the announcement listed (that rests on the unreadable lore page).
- #5 (F5, low confidence) **Mitel** Exposure line: the reverse-proxy and MiVoice Border Gateway clause is attributed to APEX but the line ends on a Mitel citation; the statement is on the APEX page only.

### Editorial / less-is-more flags (advisory)

- #6 **Puppet** record summary ends "The entry now carries the access-log sequence to hunt for." (self-reference).
- #7 **PAN-SA-2026-0015** header reads Published 2026-11-25 (datePublic 2026-11-25T00:10Z) and Updated 2026-11-24; the entries use the timeline's Initial Publication, 2026-11-24 23:10 UTC (one day, timezone artifact).
- #8 **NFS2ROOT** Red Hat (2026-11-26) and Ubuntu (2026-11-25) dates are last-modified/last-updated, publication 2026-11-19; unlabelled (same shape as iteration 3's KB4976 item).
- #9 **Ruby** Exposure line (older text) cites NCSC.ch for the 3.3/3.4/4.0 ranges and `ruby -v`.
- #10 **Zammad** public-statements citation dated 2026-10-09 (statement dated 26 September; page now through 2026-11-25).

### Not raised on purpose
Zammad main analysis (1,033 words), the Fragnesia analysis at the 550 limit, the oversize summary fields, and the Puppet release-notes date, all logged for the audit.

### Whole-run checks
- Update contract (4c): nine `update` records, each with a matching `## Update` section, `updated_at` equal to the record `at`, `fields` consistent with `git diff HEAD`, no silent edit found. Every delta is the same finding as its entry. Record summaries state what the sections state.
- Dedup: CVE-2026-99362 and SoftwareOK/Q-Dir/DesktopOK have no prior coverage (`prior_coverage.json`, `state/cves_seen.json`); registry keys present and typed.
- Priority and classification: every entry carries Admiralty B/2 or A/1-2; SoftwareOK single-source B2 with a sourcing_note; no org_triage or watchlist use; no priority miscalibration found.
- Style: no em dash outside `## <Type> — <at>` headings, no hashes, IPs, domains or install paths, no pipeline vocabulary in reader-facing text (one record-summary self-reference, #6).
- Missed angles: NCSC.ch hub posts of the window (VMware vCenter 13238/13211, GeoServer 13242, Java4Shell, Drupal, Xen Orchestra, Danfoss) are all covered in entries; the 2026-11-25 KEV batch is covered; no gap found for critical or high signal.
- Run record notes: counts, dispositions and the Contradiction/four-versus-eight statements hold against the entries.

### Verdict
NEEDS_FIXES (truth: 4, editorial: 1, advisory: 5)

All five findings are one-clause edits (a wording, two citation additions, two date labels); none touches an action, a priority, a fixed version or a CVE record.

### Findings summary (machine-readable)
See `work/2026-11-27T0355Z-intel/verification.iter5.findings.yaml` (10 records).
