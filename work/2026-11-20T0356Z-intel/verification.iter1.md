**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-20T05:23:20Z · ended_at=2026-11-20T05:50:10Z · duration_seconds=1610

## Verification report — 2026-11-20T0356Z-intel (iteration 1)

Scope covered: 6 new entries, 7 updated entries (whole entry + `git diff HEAD` for each), the run record, claim ledger `claims.iter1.yaml` (324 claims, 324 rows written to `verification.iter1.claims.yaml`; `tools/claim_ledger.py --coverage 1` reports 324/324). Every cited URL (137) was fetched this pass with `extract` / `url` / `ncsc-csh` / `cisa-kev` (cached gate bodies reused), CISA alert pages via WebFetch, and raw HTML where `extract` dropped content (php.net ChangeLog and archive, calif.io, GHSA sidebars, Veria Labs). Unreadable this pass: Citrix community page (403 on all transports), the web.archive.org copy of the PAN advisory, the F5 K-articles. NCSC-NL and BSI portal pages are JS shells; their CSAF JSON (saved by DR, plus a direct fetch of BSI wid-sec-w-2026-4608.json) was used. Claims on the old, unchanged text of the updated entries were checked token-by-token and by word overlap against the cached cited pages, with full reading reserved for every changed claim; that is a weaker check than a sentence-level read and is stated here so the main agent can weigh it.

Coverage looks defensible apart from the one held home-region item (F10 below). Priority calls of the run (vCenter `high`, Ruby `high`, PHP/F5/Mitel OpenScape `notable`, USI `routine`) were reviewed against the Phase 4 bars and left alone; vCenter `critical` was considered and not raised because the bar says "if unsure, high".

### Citation does not support the claim
- #1 (F3) `zammad-...` update 2026-11-20: "the attacker was mainly interested in credentials, all of which have been rotated ([DIVD, 2026-10-09](.../cases/DIVD-2026-00014/))". The case page does not carry it; the overview page does. The 2026-10-09 label is stale (case page: "Last modified 18 Nov 2026").
- #2 (F3) `ruby-4-0-10-...`: severity sentence ("three Critical ... the rest High or Moderate") is cited to GHSA-34m4, which covers one of the seven; "the other six flaws have no CVE id yet" is cited to EUVD-2026-129481, which describes only CVE-2026-132825.
- #3 (F3, low confidence) `vmware-vcenter-...`: "GTIG describes one intrusion ... names no victim sector or country" cited to BleepingComputer ("part of the same intrusion campaign"); "who reported the flaw" cited to GTIG (credit is in Broadcom's advisory); "GTIG says patching alone is not sufficient" is GTIG's future-zero-day hardening advice, not a post-patch compromise statement.
- #4 (F3, low confidence) `php-8-5-13-...`: "PHP 8.1 and older are end of life" cited to GHSA-jm4m, which shows only "Patched versions None".
- #5 (F3, low confidence) `cve-2026-115731-puppet-...` improvement: "9.5 by OpenVox" cited to EUVD (9.0 only); 9.5 is the GitHub badge on GHSA-q4hm whose text says 9.0.

### Unsupported / hallucinated facts
- #6 (F4) `php-8-5-13-...`: "Two more memory flaws need non-default settings: CVE-2026-129474 ... needs fatal_error_backtraces=1 with zend.exception_ignore_args=0". GHSA-8mjj: "Fatal error backtraces are enabled by default in PHP 8.5. PHP's built-in default also includes arguments, but php.ini-production sets zend.exception_ignore_args=1 and prevents this attack path"; "Remote code execution has been confirmed on PHP 8.5 and later". Both are built-in defaults; Exposure and `cves[].affected` omit it.
- #7 (F4) `cve-2026-114938-java4shell-...` update: "Kibana, Beats, Elastic Agent, APM Server, ECK and Elastic Maps Server are not affected". Elastic: only "The ECK operator ... is therefore not affected"; "Elasticsearch clusters that ECK manages are affected in the same way as other self-managed Elasticsearch clusters".
- #8 (F4) `php-critical-release-...` (October) Defender takeaway: "hosts on 8.5.13, 8.4.28, 8.3.37 or 8.2.36 need no interim setting for it". GHSA-658j: an explicit `session.upload_progress.enabled` overrides the new default and serializer consistency is still required; the entry's own new section says so.
- #9 (F4) `php-critical-release-...` (October) `immediate_action`: still names "fixed builds (8.5.12, 8.4.27, 8.3.36, 8.2.35)" as the target; the update says PHP calls CVE-2026-129481 an incomplete fix for CVE-2026-109619 and actions[0] now targets the 2026-11-19 builds; `immediate_action` is not in the record's `fields`.
- #10 (F4) `mitel-openscape-4000-...` Detection: "Platform web services", "numbering and trunk configuration", "the platform's Linux base" appear in no cited source.
- #11 (F4, low confidence) `f5-big-ip-...`: headline "reach code execution" / actions[0] "reach remote code execution" vs CNA "may lead to remote code execution".
- #12 (F4, low confidence) `vmware-vcenter-...` summary: "steal guest virtual disks" (GTIG extracts specific files from the VMDKs).
- #13 (F4, low confidence) `usi-lugano-...`: "internet-facing", "lost control of an application-intake server".
- #14 (F4, low confidence) `ruby-4-0-10-...` Detection cited to NCSC.ch (no detection content); `php-8-5-13-...` Detection "malformed or unterminated boundary" (GHSA: "stop at a predictable position").
- #15 (F4, low confidence) `zammad-...` update: "DIVD's own lesson is response time"; record summary "none giving further access" vs "OAuth tokens ... used to send test emails".

### Quantifier without source
- #16 (F14) `php-8-5-13-...`: "The one that needs no application bug is CVE-2026-129289" (and summary "The one reachable without an application bug"). GHSA-qc49 needs an application path that opens php://input unread; GHSA-gr4f (CVE-2026-129496) needs no application bug either. Same phrase in `state/coverage_backlog.md`.
- #17 (F14) `php-8-5-13-...`: "the changelog of each carries the same security block of up to 18 CVEs". Counted in ChangeLog-8.php: 8.5.13 = 18, 8.4.28 = 14, 8.3.37 = 13, 8.2.36 = 12.
- #18 (F14, low confidence) `vmware-vcenter-...`: "SSH switched on and off again within minutes" (Detection and actions[1]); GTIG says "immediately after".

### Claims missing inline citation
- #19 (F5) `f5-big-ip-...`: per-flaw prerequisites / "stack-based" / CVSS and "F5's records state that versions past End of Technical Support were not evaluated" have no inline citation and no source in `sources[]`; they come from F5's CNA records. Those are readable (`https://cveawg.mitre.org/api/cve/CVE-2026-116953`, -120285, -120292, -120722, -121805, -123637 returned the F5 record this pass). `sources[0]` is a national-CERT restatement of a vendor bulletin (F6): add the CNA records as the vendor-primary and cite the sentences.

### Drop (low relevance / off-audience / duplicate)
- #20 (F7, low confidence) `artex-...` update: the Commission incident adds no ARTEX behaviour or vector (run record: "incident floor"), the Commission does not name the tool, the link rests on one anonymous official; typed `update`, it re-floats a four-week-old entry. A separate short incident entry or an improvement record fits better.

### Needs more research
- #21 (F8) `f5-big-ip-...`: CNA text for CVE-2026-123637 is "a per-request policy that includes the Client Information agent and Endpoint Security agents", the entry says any per-request policy (frontmatter, headline, Exposure, action). CERT-FR lists BIG-IP Next for Kubernetes 2.2/2.3/2.4 fixes (BNK-2.2.5-EHF1, BNK-2.3.4-EHF1, BNK-2.4.2-EHF1), the body gives only 2.2; the CNA `modules` fields name PEM and DNS for PSC::ip_address, PEM::subscriber and DNS::scrape.

### Surface contradiction
- #22 (F9) `artex-...` update: Commission "the incident was detected on the 22nd of October and ... confirmed ... on the 26th of October" vs POLITICO "CERT-EU, detected earlier this month that international hackers used ARTEX" (2026-11-19); the section and record summary present 2026-10-22 as fact with no Contradiction line.
- #23 (F9, low confidence) `vmware-vcenter-...`: Q&A says CVE-2026-123894 affects VMware Tools for Windows "13.x, 12.x, and 11.x"; VMSA-2026-0009.1 lists 13.x and 12.3 to 12.5; entry follows the advisory silently.

### Missed angles
- #24 (F10, low confidence) Basel-Landschaft cantonal administration incident (six servers isolated, ~20 applications, Alertswiss 112/117/118 warning, seven outlets) is held while USI ships as routine; the hold is driven by the empty-techniques gate. Suggested re-check query: "Kanton Basel-Landschaft Cyberangriff Verwaltung Server neu installiert". No other gap found.

### Editorial / less-is-more flags (advisory)
- #25 (F11) `turla-cereal-...` improvement: "adds three checks to the Detection line" narrates an edit that was not made; the Detection line lacks the HTTP.sys / proxy-DLL / WmiPrvSE.exe checks. Proxy-DLL names are file-name indicators.
- #26 (F11) `f5-big-ip-...` sourcing_note "no reader returned" and summary "F5's own bulletin could not be read"; sourcing_note length (Ruby 6 sentences, vCenter 5, USI 4) vs "two sentences of provenance".
- #27 (F11) Ruby evidence quote "2026 , or later" (space artefact; page reads "2026, or later"); USI evidence quote lacks "(translated from Italian)".
- #28 (F11) `usi-lugano-...`: product-less Exposure / Detection / Defender takeaway are derived advice on an incident-floor entry.
- #29 (F11, low confidence) Puppet improvement: certificate-name impersonation has no technique id.
- #30 (F11) main analysis over bound and not compacted by the touching record: PHP October 1915 words, Zammad 1070, ARTEX 726.

### Classification missing / inconsistent
None (all 13 entries carry Admiralty ratings consistent with sourcing; no `org_triage`, no watchlist).

### Action-item discipline
- #31 (F18, low confidence) `vmware-vcenter-...` actions[1] restates the body Detection line and repeats "within minutes".

### Priority calibration
- #32 (F16) `php-critical-release-...` (October): `priority: critical` + `immediate_action` carried through a regular-cycle release update that floats the entry; critical disqualifier "patches >=1 week old without new exploitation".

### Checked and fine (no finding)
vCenter: Broadcom VMSA-2026-0009 matrix (versions, KB88287, KB463116, 7.0 no public fix, CVSS 9.8/8.1/7.2/6.7/6.7), Q&A (ESX not affected, emergency change, back-in-time), GTIG chain (port 2012 rpc_srp_verifier, SAML key, VAMI SSH on/off, ESXi authorized_keys, VMFS hidden directory, scp), Table 1 "iptables DROP policy on TCP 2012", BleepingComputer quote, four evidence quotes. PHP new: GHSA-qc49/658j/fm2m/g3vh/2fjv/gr4f/jm4m facts, CNA scores 9.2/8.8 (CNA JSON), 129289 range "version 0", NCSC.ch status, watchTowr table. F5: CERT-FR fixed builds, NCSC-NL commands and "Kans: medium", BSI listing, CNA descriptions for the six. Ruby: ruby-lang advisory, Veria table and 25 November date (`<time datetime="2026-11-25">`), NCSC.ch exposure, EUVD 7.4 AV:L/AC:H. Mitel OpenScape: advisory table, versions, workaround and fix quotes, CERT-FR/BSI wording and the R2.12/R2.13 caveat. USI: three press relays, translation of the original. Updated entries: Puppet CVE-2026-115732 (EUVD 9.0, OpenVox GHSA incl. OpenVoxDB 9.2.0/8.18.0, Neodyme, NCSC.ch 13204, SecurityWeek, THN), MiCollab five MTLVULN-to-CVE mappings and scores (EUVD, assigner mitre), Java4Shell Elastic/Tanzu/PAN statuses, Turla ReversingLabs content, ARTEX Commission transcript / POLITICO / Cyber Security News, Zammad overview figures (41,000 titles, 207 e-mails, 2 phones, 7 pictures, 19 h), KEV dates via `cisa-kev`, CISA alert pages via WebFetch. Changelog contract: every `at` equals `updated_at` for the five `update` records, improvements leave `updated_at` untouched, `fields` match `git diff HEAD`, record summaries match their sections.

### Verdict
NEEDS_FIXES (truth: 18, editorial: 8, advisory: 6)

### Findings summary (machine-readable)
See `work/2026-11-20T0356Z-intel/verification.iter1.findings.yaml` (32 records).
