**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-09-30T02:17:08Z · ended_at=2026-09-30T02:44:48Z · duration_seconds=1660

## Verification report — 2026-09-29T2134Z-audit (iteration 4)

Scope read cold: all 43 entries of `verify.iter4.scope.txt` (whole file + `git diff HEAD`), every cited page of each changed clause fetched fresh (bridge `extract` / `url --direct`, CSAF and EUVD recipes, cveawg/NVD for CVE records, CISA KEV feed via the bridge, CISA pages by cached body + WebSearch snippet because the container's cisa.gov transport is walled), the registry rows `actor:dire-wolf` and `incident:metabase-sqli-zeroday-2026-08`, the two `cves_seen` rows, the run record, the audit report, the CHANGELOG 4.16 entry and the tool diffs. No prior-iteration deltas block was supplied beyond the iteration 3 report; the iteration 3 remediations were re-checked against the pages and held (WatchGuard 13368, ShareFile top-of-entry, WP2Shell sourcing note and Rapid7/EUVD re-citation, Gridbox actions, Siemens Mendix wording, SPECTRE headline, WatchGuard Fireware, Check Point R81.10 Take 190 and CVE-2026-93616 pointer, CNIL/BlueMoon/Kudelski corrections, Zalktis/Wiz/MikroTik/ECA/Microsoft quotations, Windchill/TA4922/Check Point citations, MovieReaper wording, Metabase registry date).

Held up (no finding): run record counts against disk (43 entries = 43 ids = 43 records with this run_id, `entries_published` 0, sources_changed 28 ids and every field change against `git show a8628bc^:sources/sources.json`, entities_added 9 = registry diff, sub-agent timestamps and durations against the work files, iteration finding counts 21/34/37, quote-triage counts 13/11/24/20); `check_run.py 2026-09-29T2134Z-audit` (51 pass · 0 warn · 3 fail, the three expected: residual count, NEEDS_FIXES residual rule, run clock); `check_run.py ... --page-checks-since 2026-07-01` (522 entries, 1683 quotes verbatim, 0 warn, 0 fail); `tools/test_fetch_source_pdf.py` 13/13 (five new tests); `fetch_source.py pdf https://www.ic3.gov/CSA/2026/260918.pdf` reads "North Korean WaterPlum", "September 18, 2026"; `kb.cert.org/vuls/id/308749` extracts (gzip fix); source_health sweep counts 162 → 182 → 185 relevant and the 28-flag breakdown (11 stale / 7 irrelevant / 5 shell / 5 unreadable); warning_acknowledgments 23 rows; KEV facts for every KEV claim in scope (dates for PaperCut, Cisco, Joomla four, WP2Shell, MikroTik, BlueMoon, Microsoft, VMware, NetScaler); audit-report tables (13 news-carrying revisions, 14 internal improvements, 43 entries in total) and the CHANGELOG 4.16 text against disk. Coverage: the only in-window KEV item without an entry is Apple CVE-2026-86950 (CoreGraphics, KEV 2026-09-29), disclosed in the report and run record as a hand-off to the next intel fire; not raised as a finding.

### Unsupported / hallucinated facts

**#1 (F4) `entries/2026-08-09/teamdavid-tobit-22-cves-unauth-mailbox-takeover-dach.md`. High confidence.** Summary: "The CVE records bound every issue at TeamDavid through Rollout 524."; all 22 `cves[].affected: "TeamDavid through Rollout 524"`; `sourcing_note`: "the \"TeamDavid through Rollout 524\" affected bound come from the per-CVE records"; update section: "The CVE records bound the affected builds at \"through Rollout 524\", Tobit puts the functionality off by default only from Rollout 528, and no source says whether Rollouts 525 to 527 still expose it, so treat anything below 528 as unverified." Fetched all 22 records (https://cveawg.mitre.org/api/cve/CVE-2026-54203 … CVE-2026-12071, assigner NCSC.ch, dateUpdated 2026-09-07; NVD `lastModified` 2026-09-07 carries the same text): each says "This issue affects TeamDavid before Rollout 528." with `versions: [{version 0, lessThan "Rollout 528"}]`, and adds "Starting with Rollout 528 (June 30, 2026), the affected functionality is disabled by default and the vulnerabilities are therefore no longer exposed through this functionality." The records were revised before this run; the run rewrote summary, frontmatter and section on the pre-revision premise. Fix: `affected` to "TeamDavid before Rollout 528" on all 22, correct the three sentences, cite the CVE records inline (the body sentence "The published CVE records bound every one of the 22 issues at TeamDavid through Rollout 524" is also uncited).

**#2 (F4) `entries/2026-08-28/taiwan-agentic-ai-intrusion-openclaw-hermes-guardrail-bypass.md`. Medium confidence.** Body, "Guardrail bypass": `"the agents bypassed their own AI safety guardrails by reframing the offensive operation as 'authorized penetration testing,' a novel prompt-based technique ..."`. Tenable's page reads "The agents **also** bypassed their own AI safety guardrails by reframing the offensive operation as “authorized penetration testing,” a novel prompt-based technique with no current mapping in the MITRE ATT&CK framework." The record fixes evidence[] for exactly this dropped word and lists `body` in its fields, but the body quotation still omits it, so it is not a contiguous substring. Fix: restore "also" or begin the quotation at "bypassed".

**#3 (F4) `entries/2026-08-28/cve-2026-59109-zalktis-peppol-einvoice-unauth-sqli.md`. Low confidence.** Sourcing note (rewritten by this run): "the CVE record itself (CNA CERT.LV) confirms only the identifier, affected range and coordinating authority"; body: "CVE reserved 2026-07-30, published 2026-08-13". https://cveawg.mitre.org/api/cve/CVE-2026-59109: `assignerShortName` ENISA, `dateReserved` 2026-07-02, `datePublished` 2026-08-13. OffSeq's timeline ends at "2026-07-30 CVE-2026-59109 reserved" and carries no publication date; the NVD/CVE-record source that carried 2026-08-13 was removed by this run, so the date now has no cited page. Fix: name ENISA as assigner (CERT.LV coordinated the disclosure), cite the CVE record for the publication date or drop it.

### Citation does not support the claim

**#4 (F3) `entries/2026-07-20/cve-2026-42533-nginx-pcre-capture-clobber-preauth-rce.md`. Medium confidence.** Body: "a heap-overflow variant ... tested at 10/10 reliability with full ASLR enabled ([Stan Shaw, 2026-07-19](https://cyberstan.co.uk/nginx-rce/))". The page the update itself cites as "revised since" no longer says that: its Reliability section reads "The vulnerability is not probabilistic ... I measured the leak at 100 out of 100. What is probabilistic is the exploitation ... A single `BODY_DELTA` therefore lands about two thirds of the time" on a stock deployment, with the deterministic `--rce-det` needing "a controlled config whose heap layout is reproducible". The original fetch (work/2026-07-20T0409Z-intel/deepread.cyberstan.html) did say "Tested at 10 out of 10 reliability". The run rewrote body and summary for the PoC publication but left the old figure (and the summary's "a reliable pre-auth RCE that defeats ASLR in a single request") as current fact. Fix: date the figure to the original post and carry the revised stock-deployment landing rate, or drop it.

### Analytical-link-as-fact

**#5 (F13) `entries/2026-07-13/progress-sharefile-storage-zone-controller-shutdown.md`. Low confidence.** actions[0]: "This is the fix for the flaw behind the 2026-07-10 emergency shutdown, against which in-the-wild exploitation attempts were already observed." The path-traversal flaw Progress names as the cause has no exploitation source: BankInfoSecurity's Shadowserver honeypots recorded attempts against CVE-2026-2699 (the earlier authentication bypass, fixed 5.12.4), and BleepingComputer 2026-07-14 quotes Progress "we have not identified any active threat". The entry's own 2026-07-14 section says "the same component". Fix: state it as attempts against CVE-2026-2699 on the same component, or drop the clause.

### Action-item discipline

**#6 (F18) `entries/2026-08-28/cve-2026-59109-zalktis-peppol-einvoice-unauth-sqli.md`. Low confidence.** actions[0] "Upgrade Zalktis to 2026.1.586 ... now on every instance that imports PEPPOL/UBL e-invoices ... exposure is continuous rather than opportunistic". The same run's correction re-rates the entry to notable because it "is not something the profiled constituency needs to act on outside its normal cycle" (Latvian desktop product). The do-now action contradicts the run's own re-rating and lands in the aggregated Action Items. Fix: drop it (empty is healthy) or reword to the transferable check (does our e-invoice intake parameterise trading-partner fields).

### Editorial / less-is-more flags (advisory)

**#7 (F11) `entries/2026-08-28/nimbus-manticore-twostroke-backdoor-europe.md`.** The record splits the evidence quote because it "elided an infrastructure address and a local port ... made it a non-contiguous quote", but the body (paragraph 2) still quotes the same passage joined by an ellipsis with a bracketed "[a local port]". Same class iteration 3 raised on Zalktis/Wiz; quote the three contiguous fragments or paraphrase.

**#8 (F11) `entries/2026-08-28/ta4922-packclient-telegram-rat-tax-lures.md`.** The record says the Proofpoint quotation "joined three separate hunting bullets and dropped the examples between them" and is "now three quotations"; the body (paragraph 2) still presents the three bullets as one continuous quotation with the rundll32 and process-tree examples silently dropped.

**#9 (F11) `entries/2026-08-28/teampcp-afp-fbi-disruption-shai-hulud-arrests.md`.** Evidence is split because the Larsen quote "was joined into one passage across the attribution clause"; the body (paragraph 4) still quotes "... single operator. It is a peer community ..." joined (Krebs: "“It is not a structured criminal crew with a single operator,” said Austin Larsen ... “It is a peer community ...”").

**#10 (F11) `entries/2026-09-10/checkpoint-quantum-vpn-cert-preauth-rce-cvss98.md`.** First paragraph still opens "two Critical-severity advisories (last modified 2026-09-09)" while the pages it links carry lastModified 2026-09-18 (sk1000118) and 2026-09-24 (sk1000117) and the same paragraph now cites their revised text. Say "published 2026-09-09, since revised".

**#11 (F11) `entries/2026-07-13/progress-sharefile-storage-zone-controller-shutdown.md`, `entries/2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030.md`.** Both 2026-09-29 Correction sections end "The top of the entry now says so." Record-keeping narration in reader-facing text; the section's delta is the cited current state. Drop the sentence.

**#12 (F11) `runs/2026-09-29/2026-09-29T2134Z-audit.md`. Low confidence.** Published notes body: "**Sub-agent models.** Every sub-agent reported Sonnet 5.5 ...", "T1 ... SR1 sampled it". Check 12 lists "sub-agent" as workflow-internal vocabulary for run-record notes; precedent exists (runs/2026-06-07), so leave it if accepted, otherwise reword ("the verification and research passes each reported ...").

### Verdict

NEEDS_FIXES (truth: 5, editorial: 1, advisory: 6)

The one finding that must be fixed before a CLEAN chain can start is #1 (TeamDavid), a checkable contradiction of the assigning CNA's current records. #2 and #4 are checkable quotation/figure defects; #3 and #5 are low-confidence truth items; #6 is a low-confidence action-discipline item.

### Findings summary (machine-readable)

```yaml
- code: F13
  category: analytical-link-as-fact
  section: entries/2026-07-13/progress-sharefile-storage-zone-controller-shutdown.md
  item: entries/2026-07-13/progress-sharefile-storage-zone-controller-shutdown.md
  url_or_quote: This is the fix for the flaw behind the 2026-07-10 emergency shutdown, against which in-the-wild exploitation attempts were already observed.
  summary: '(low confidence) actions[0] binds the in-the-wild exploitation attempts to the path-traversal flaw Progress named as the cause; the only exploitation source (BankInfoSecurity, Shadowserver honeypots) ties the attempts to CVE-2026-2699, the earlier auth-bypass patched in 5.12.4, and BleepingComputer 2026-07-14 quotes Progress: ''we have not identified any active threat''. Reword to ''the same component saw in-the-wild attempts against CVE-2026-2699 from 2026-07-10'' or drop the clause.'
- code: F3
  category: claim-not-supported
  section: entries/2026-07-20/cve-2026-42533-nginx-pcre-capture-clobber-preauth-rce.md
  item: entries/2026-07-20/cve-2026-42533-nginx-pcre-capture-clobber-preauth-rce.md
  url_or_quote: a heap-overflow variant ... tested at 10/10 reliability with full ASLR enabled ([Stan Shaw, 2026-07-19](https://cyberstan.co.uk/nginx-rce/))
  summary: 'The cited page, revised (the run''s own update cites it as ''revised since''), no longer says 10/10: its Reliability section says ''The vulnerability is not probabilistic ... I measured the leak at 100 out of 100. What is probabilistic is the exploitation ... A single BODY_DELTA therefore lands about two thirds of the time'' on a stock deployment, and the deterministic --rce-det needs a controlled config. The original page (work/2026-07-20T0409Z-intel/deepread.cyberstan.html) did say ''Tested at 10 out of 10 reliability''. The run rewrote body/summary for the PoC publication but left this figure (and the summary''s ''reliable pre-auth RCE ... in a single request'') stated as current fact; date it as the original post''s figure and carry the revised stock-deployment two-thirds landing rate, or drop the figure.'
- code: F4
  category: hallucinated-fact
  section: entries/2026-08-09/teamdavid-tobit-22-cves-unauth-mailbox-takeover-dach.md
  item: entries/2026-08-09/teamdavid-tobit-22-cves-unauth-mailbox-takeover-dach.md
  url_or_quote: 'The CVE records bound every issue at TeamDavid through Rollout 524. / The CVE records bound the affected builds at "through Rollout 524", Tobit puts the functionality off by default only from Rollout 528, and no source says whether Rollouts 525 to 527 still expose it, so treat anything below 528 as unverified. / cves[*].affected: "TeamDavid through Rollout 524" (x22)'
  summary: 'All 22 CNA records (assigner NCSC.ch; fetched https://cveawg.mitre.org/api/cve/CVE-2026-54203 ... CVE-2026-12071, dateUpdated 2026-09-07, i.e. before this run; NVD carries the same text, lastModified 2026-09-07) now read ''This issue affects TeamDavid before Rollout 528.'' with versions [{version 0, lessThan ''Rollout 528''}] and ''Starting with Rollout 528 (June 30, 2026), the affected functionality is disabled by default''. The run rewrote the summary, all 22 cves[].affected values, the sourcing_note (''the "TeamDavid through Rollout 524" affected bound come from the per-CVE records'') and the update section on the premise that the records stop at Rollout 524 and that no source says whether Rollouts 525-527 are exposed; the authoritative records put everything before Rollout 528 in scope. Fix: affected -> ''TeamDavid before Rollout 528'' on all 22 records, correct the summary sentence, the sourcing note and the update-section sentence (525-527 fall inside the CNA''s affected range; the CNA also repeats the vendor''s Rollout 528 statement), and cite the CVE records inline (the body sentence ''The published CVE records bound every one of the 22 issues ...'' has no citation).'
- code: F4
  category: hallucinated-fact
  section: entries/2026-08-28/cve-2026-59109-zalktis-peppol-einvoice-unauth-sqli.md
  item: entries/2026-08-28/cve-2026-59109-zalktis-peppol-einvoice-unauth-sqli.md
  url_or_quote: the CVE record itself (CNA CERT.LV) confirms only the identifier, affected range and coordinating authority ... Reported 2026-06-30, vendor-confirmed fixed 2026-07-16, CVE reserved 2026-07-30, published 2026-08-13
  summary: '(low confidence) The CVE record (fetched https://cveawg.mitre.org/api/cve/CVE-2026-59109) names ENISA as assigner (assignerShortName ENISA), not CERT.LV, gives dateReserved 2026-07-02 (OffSeq''s timeline says reserved 2026-07-30) and datePublished 2026-08-13. This run rewrote the sourcing note and removed the NVD/CVE-record source but kept ''CNA CERT.LV'' and the uncited ''2026-08-13'' publication date, which now has no cited page carrying it (OffSeq''s timeline ends at ''CVE reserved''). Fix: say the record was published 2026-08-13 with ENISA as the assigning CNA (CERT.LV coordinated the disclosure) and cite the CVE record, or drop the date.'
- code: F18
  category: action-item-discipline
  section: entries/2026-08-28/cve-2026-59109-zalktis-peppol-einvoice-unauth-sqli.md
  item: entries/2026-08-28/cve-2026-59109-zalktis-peppol-einvoice-unauth-sqli.md
  url_or_quote: Upgrade Zalktis to 2026.1.586 (pre-1-July branch) or 2026.2.592 (post-1-July branch) now on every instance that imports PEPPOL/UBL e-invoices ... exposure is continuous rather than opportunistic
  summary: (low confidence) The run's own correction moves the entry to notable because 'it is not something the profiled constituency needs to act on outside its normal cycle' (Latvian desktop product), yet actions[0] still tells readers to upgrade 'now' and asserts continuous exposure; the action does not follow the entry's own re-rating and lands in the aggregated Action Items. Drop it (empty actions is healthy) or reword to the transferable task (check whether the organisation's accounting/e-invoice intake parameterises trading-partner fields).
- code: F11
  category: editorial-advisory
  section: entries/2026-08-28/nimbus-manticore-twostroke-backdoor-europe.md
  item: entries/2026-08-28/nimbus-manticore-twostroke-backdoor-europe.md
  url_or_quote: '"execution of this command establishes an SSH connection to the operator''s infrastructure ... on port 443 to set up a reverse tunnel. As a result, traffic sent to [a local port] on the C2 server is redirected back..." (body, paragraph 2)'
  summary: '(low confidence, advisory) The record splits the evidence quote because it ''elided an infrastructure address and a local port ... made it a non-contiguous quote'', but the body (not in the record''s fields) still quotes the same passage joined by an ellipsis with a bracketed ''[a local port]'' substitution, i.e. the same non-contiguous form. Same class iteration 3 raised on Zalktis/Wiz. Fix: quote the three contiguous fragments in the body as well, or paraphrase without quotation marks.'
- code: F11
  category: editorial-advisory
  section: entries/2026-08-28/ta4922-packclient-telegram-rat-tax-lures.md
  item: entries/2026-08-28/ta4922-packclient-telegram-rat-tax-lures.md
  url_or_quote: '"distinct Rundll32 command line used to launch PackClient. PackClient config stored in registry (HKCU\SOFTWARE\PackClientConsole\). Distinct process tree and command line flags" (body, paragraph 2)'
  summary: '(low confidence, advisory) The record''s summary says the Proofpoint quotation ''joined three separate hunting bullets and dropped the examples between them'' and is ''now three quotations''; evidence[] was split, but the body (in the record''s fields) still presents the three bullets as one continuous quotation with the rundll32 / process-tree examples silently dropped (Proofpoint page lines: ''- Distinct Rundll32 command line used to launch PackClient. Example: ...'', ''- PackClient config stored in registry (HKCU\SOFTWARE\PackClientConsole\).'', ''- Distinct process tree and command line flags (rundll32.exe -> svchost.exe ...)''). Fix: quote the three bullets separately or paraphrase.'
- code: F4
  category: hallucinated-fact
  section: entries/2026-08-28/taiwan-agentic-ai-intrusion-openclaw-hermes-guardrail-bypass.md
  item: entries/2026-08-28/taiwan-agentic-ai-intrusion-openclaw-hermes-guardrail-bypass.md
  url_or_quote: '"the agents bypassed their own AI safety guardrails by reframing the offensive operation as ''authorized penetration testing,'' a novel prompt-based technique with no current mapping in the MITRE ATT&CK framework" (body, ''Guardrail bypass'' paragraph)'
  summary: 'The record fixes evidence[] because the Tenable quotation ''had dropped the word also'', and lists body in fields, but the body quotation still drops it: Tenable''s page reads ''The agents also bypassed their own AI safety guardrails by reframing the offensive operation as “authorized penetration testing,” a novel prompt-based technique ...''. The body quote is therefore not a contiguous substring of the page. Fix: restore ''also'' in the body quotation (or quote from ''bypassed'').'
- code: F11
  category: editorial-advisory
  section: entries/2026-08-28/teampcp-afp-fbi-disruption-shai-hulud-arrests.md
  item: entries/2026-08-28/teampcp-afp-fbi-disruption-shai-hulud-arrests.md
  url_or_quote: '"it is not a structured criminal crew with a single operator. It is a peer community of individually-skilled actors, with one clear center of gravity" (body, paragraph 4)'
  summary: '(low confidence, advisory) The record splits the evidence quotation because it was ''joined into one passage across the attribution clause''; the body still quotes it joined (comma after ''operator'' replaced by a full stop, '', said Austin Larsen'' removed). Krebs: ''“It is not a structured criminal crew with a single operator,” said Austin Larsen ... “It is a peer community of individually-skilled actors, with one clear center of gravity.”'' Quote the two sentences separately or paraphrase.'
- code: F11
  category: editorial-advisory
  section: entries/2026-09-10/checkpoint-quantum-vpn-cert-preauth-rce-cvss98.md
  item: entries/2026-09-10/checkpoint-quantum-vpn-cert-preauth-rce-cvss98.md
  url_or_quote: Check Point published two Critical-severity advisories (last modified 2026-09-09) for its VPN certificate-handling code ... ([Check Point, advisory sk1000118, 2026-09-07]...; [sk1000117, 2026-09-07]...)
  summary: '(low confidence, advisory) The run rewrote this first paragraph to the current advisories but left the opening dateline: the fetched pages carry lastModified 2026-09-18 (sk1000118) and 2026-09-24 (sk1000117), and the same paragraph now cites the revised text (Take 190, Remote Access mitigation). ''last modified 2026-09-09'' is stale against the pages it links; say ''published 2026-09-09, since revised'' or cite the revision dates as the later sections do.'
- code: F11
  category: editorial-advisory
  section: entries/2026-07-13/progress-sharefile-storage-zone-controller-shutdown.md; entries/2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030.md
  item: entries/2026-07-13/progress-sharefile-storage-zone-controller-shutdown.md; entries/2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030.md
  url_or_quote: '"The top of the entry now says so." (closing sentence of the 2026-09-29 Correction section on both entries)'
  summary: '(advisory) Record-keeping narration in reader-facing body text; the section''s delta is the cited statement of the current state, and telling the reader which part of the entry was edited is not delta (CLAUDE.md: the section carries only the inline-cited delta, never record-keeping narration). Drop the sentence.'
- code: F11
  category: editorial-advisory
  section: runs/2026-09-29/2026-09-29T2134Z-audit.md
  item: runs/2026-09-29/2026-09-29T2134Z-audit.md
  url_or_quote: '**Sub-agent models.** Every sub-agent reported Sonnet 5.5 (`claude-sonnet-5-5`) from its own prompt line. / T1 read one cisa.gov alert ..., and SR1 sampled it'
  summary: (low confidence, advisory) The run record's published notes body carries workflow-internal vocabulary ('Sub-agent models', 'sub-agent', the T1/SR1 labels); verification check 12 lists 'sub-agent' as language that must not appear in run-record notes. Precedent exists (runs/2026-06-07 'Sub-agent models'), so leave it if the operator accepts that line; otherwise reword to 'The verification and research passes each reported Sonnet 5.5'. The frontmatter sub_agents block is the schema field and is fine.
```
