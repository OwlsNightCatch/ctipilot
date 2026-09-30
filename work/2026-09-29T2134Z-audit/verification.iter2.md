**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-09-30T00:02:55Z · ended_at=2026-09-30T00:36:12Z · duration_seconds=1997

## Verification report — 2026-09-29T2134Z-audit (iteration 2)

Scope read cold: all 43 updated entries (whole-file reads of the changed sections, `git diff HEAD --word-diff`, targeted whole-entry stale-state scans for top-of-entry text, actions, classification and workflow language), registry records `actor:dire-wolf` and `incident:metabase-sqli-zeroday-2026-08`, the run record, the audit report, `prompts/CHANGELOG.md` 4.16, `sources/sources.json`, `state/source_health.json`, `tools/fetch_source.py`, `tools/check_run.py`, `tools/test_fetch_source_pdf.py`. Every cited page of every changed clause was re-fetched this iteration (bridge `extract` / `url --direct` / `pdf` / `cisa csaf` / `cisa-kev` / `enisa-euvd advisory`); cisa.gov alert text was corroborated through WebSearch summaries and the KEV feed (bridge 403, jina pool empty; no WebFetch). Gate: `check_run.py 2026-09-29T2134Z-audit` = 51 pass / 0 warn / 3 fail (the three expected); `check_run.py --all` = 24 pass / 0 warn / 3 fail / 23 acknowledged; `test_fetch_source_pdf.py` 13/13; WaterPlum PDF decodes (44 hits 'North Korean', 0 mojibake).

Prior-iteration deltas walked: iteration 1's 21 findings. Held: #1 PDF decode (also old-vs-new compared on 15 cited PDFs), #2 Unit 42 note, #3 Metabase wording, #4 NetScaler summary, #5 CISA source notes and T1 WebFetch disclosure, #7 CRA date, #9 PaperCut Site Servers wording, #10 ECA summary, #11 Dire Wolf record, #12 WatchGuard inference marking, #13 MAG citations, #14 KEV chips (PaperCut, MikroTik, Microsoft, BlueMoon), #15 wider backfill triaged (T3/T4: 44 flags, 31 quote + 13 CVE, 33 entries), #17 truncated notes restored, #19 headline/action titles. Partly held / re-raised below: #6 counts, #8 CNIL (new citation added, but it now over-reads the source), #18 narration, #20 Microsoft body quote, #16 Apple CVE-2026-86950 (disclosed in report and run record, deferred to the next intel fire; not re-raised).

### Citation does not support the claim

**#1 (F3) entries/2026-07-03/cve-2026-13368-watchguard-fireware-iked-pre-auth-rce.md**
- Claim / location: CVE-2026-13368 WatchGuard iked (frontmatter fixed/affected, body 'gives 11.x End-of-Life status with no fix and no workaround')
- Evidence: https://psirt.watchguard.com/CVE-2026-13368
- Gap and fix: (low confidence) The advisory page the run re-cited (Updated 2026-08-27) lists Solution 'Fireware OS 2026.2.1, Fireware OS 12.0, Fireware OS 11.10.2, Fireware OS 12.5.19, Fireware OS 12.11.9' and a Not-affected cell '>= 2026.2.1, >= 12.0, < 12.12.1, >= 11.10.2, <= 11.12.4+541730'; it names no 12.12.1 fix and no 11.x EOL/no-fix statement. The entry (frontmatter fixed '12.12.1 (12.x)', '11.x EOL', affected '11.0-11.12.4_Update1') was not re-checked against the revised page when only the 12.5.19/12.11.9 rows were updated. Re-read the current Product status table and either restate 11.x/12.x rows as the page gives them or state the ambiguity.

**#2 (F3) entries/2026-07-11/joomla-rsfiles-phoca-file-upload-rce-cve-2026-57827-57828.md**
- Claim / location: 'iCagenda after confirmed zero-day exploitation ([mySites.guru, 2026-07-10](.../rsfiles-unauthenticated-file-upload-rce/))'
- Evidence: https://mysites.guru/blog/rsfiles-unauthenticated-file-upload-rce/
- Gap and fix: (low confidence) The cited RSFiles post carries no statement that iCagenda was exploited or a confirmed zero-day (only an iCagenda link whose slug reads 'icagenda-zero-day-file-upload-rce' and 'the SP Page Builder zero-day'). The KEV listing the run added supports exploitation; cite the KEV catalog (or the iCagenda post) for that clause or drop 'confirmed'.

**#3 (F3) entries/2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030.md**
- Claim / location: 'The second half is CVE-2026-60137, an SQL injection in the author__not_in parameter of WP_Query, the class that builds most WordPress database queries ([Rapid7, 2026-07-17](...etr-cve-2026-63030-wp2shell...))'
- Evidence: https://www.rapid7.com/blog/post/etr-cve-2026-63030-wp2shell-a-critical-remote-code-execution-vulnerability-in-wordpress-core/
- Gap and fix: (low confidence) Rapid7 says 'CVE-2026-60137 is a SQL injection in the author__not_in parameter of the posts endpoint' and never names WP_Query nor the 'builds most WordPress database queries' characterisation; WP_Query is carried by EUVD-2026-45279 (cited in the next sentence). Adjacency: the clause the run re-cited to Rapid7 carries a detail Rapid7 lacks; cite EUVD-2026-45279 for WP_Query or say 'posts endpoint'.

**#4 (F3) entries/2026-08-15/geoserver-jsonarraycontains-unauth-sqli-zeroday-exploited.md**
- Claim / location: cves[0].affected 'GeoTools gt-jdbc-postgis on the 35.0, 34.x and 33.x lines ...' and 2026-08-18 section 'GeoTools scopes the affected package to org.geotools:gt-jdbc-postgis versions 35.0, >=34.0 and >=33.1 ... No CVE identifier exists yet'
- Evidence: https://github.com/geotools/geotools/security/advisories/GHSA-mqjf-5f49-2fjh : Affected versions '35.0 | >=34.0 | >=30.5, < 31.0, >=31.3, >= 32.0'; Patched versions '35.1 34.5 33.6'; CVE ID CVE-2026-76904; description Patches 'GeoTools 35.1, 33.5, 34.4'
- Gap and fix: (low confidence) The advisory the run re-cited ('revised since') now lists a third affected range '>=30.5, <31.0, >=31.3, >= 32.0', not '>=33.1' and not '33.x'; the run's new cves[].affected and the untouched 08-18 paragraph (re-edited in this run, which still says 'No CVE identifier exists yet' two paragraphs before the update that says one exists) both disagree with it. State the ranges as the header now gives them (or say the header and description disagree on ranges and on 33.5/34.4 vs 33.6/34.5) and date the 'no CVE' sentence to its section.

**#5 (F3) entries/2026-08-29/papercut-ng-mf-tapestry-request-confusion-preauth-rce.md**
- Claim / location: Update 2026-09-29 section and record summary: the maintenance releases 'contain every fix from Emergency Patch Releases 1, 2 and 3 plus further hardening' / 'They carry every fix from the three emergency patches' ([PaperCut Software, 2026-09-10])
- Evidence: https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/ : 'The maintenance releases deliver the same protection through our standard release process, with additional hardening, published release notes and a new version number.'; 'containing security improvements, including addressing all CVEs mentioned in this Security Advisory'
- Gap and fix: (low confidence) The bulletin says the maintenance releases give 'the same protection' as Emergency Patch Release 3 plus hardening and address all CVEs; it does not state they contain every fix from Releases 1, 2 and 3. Reword to what the page states.

**#6 (F3) entries/2026-09-04/cnil-fine-hopital-prive-de-la-loire-dpi-breach.md**
- Claim / location: 'the attacker used the credentials of a single compromised physician account to get in ([BleepingComputer, 2026-09-03](...))' (citation added by this run)
- Evidence: https://www.bleepingcomputer.com/news/security/french-hospital-fined-500-000-after-breach-exposes-data-of-727-000/ : CNIL findings bullet 'Inadequate access controls allowed the compromised account to access records for all hospital patients.'; 'single doctor's account' appears only as the hacker Marak's claim; https://www.cnil.fr/en/sanction-fine-hopital-prive-loire : 'using the credentials of a single user account'
- Gap and fix: Neither cited page states as fact that the compromised account was a physician's: CNIL says 'a single user account', BleepingComputer says 'the compromised account' and attributes 'single doctor's account' to the attacker's unverified claim (which the entry itself later labels unconfirmed). The clause sits inside the CNIL-findings sentence; say 'a single user account' (CNIL) and keep the physician detail in the unconfirmed-claims sentence.

**#7 (F3) entries/2026-08-23/trueconf-server-kev-head-mare-trojanized-installer.md**
- Claim / location: [Kaspersky ICS CERT, KLCERT-26-057, 2026-08-07](.../trueconf-server-missing-authentication-for-critical-function/) and sources[] date 2026-08-07
- Evidence: https://ics-cert.kaspersky.com/vulnerabilities/trueconf-server-missing-authentication-for-critical-function/ : visible dateline '11 August 2026' (extract date 2026-08-11); timeline line 'Kaspersky ICS CERT advisory published 07 August 2026'
- Gap and fix: (low confidence) The page's own dateline is 11 August 2026; 07 August is the advisory-published line in its timeline. A four-day gap to the visible dateline; say which date is meant or use the dateline.


### Unsupported / hallucinated facts

**#1 (F4) entries/2026-07-11/joomla-rsfiles-phoca-file-upload-rce-cve-2026-57827-57828.md**
- Claim / location: tags include poc-public
- Evidence: tags: [vulnerabilities, rce, pre-auth, poc-public, patch-available] vs body 'Neither flaw has a published proof-of-concept' and summary 'No public PoC'
- Gap and fix: Frontmatter tag poc-public contradicts the body, summary, sourcing_note and both mySites.guru posts ('No proof of concept has been made public'). Remove the tag (correction record).

**#2 (F4) entries/2026-07-13/progress-sharefile-storage-zone-controller-shutdown.md**
- Claim / location: title/headline/summary still state 'day three, no patch or root cause disclosed' / 'No CVE, root cause, patch or restart timeline has been published; the shutdown-not-patch instruction signals no fix yet exists'
- Evidence: https://status.sharefile.com/incidents/c59n5343lbkq (Resolved, Jul 14 2026 11:06 EDT: 'Storage Zones Controller customer access is currently being restored') and the entry's own 2026-07-14T20:21:02Z section (patches 5.12.5 / 6.0.2, root cause confirmed)
- Gap and fix: Top-of-entry drift on an entry this run edited: the title, headline and summary were never moved to the current state after the 2026-07-14 update record (root cause path traversal, fixed 5.12.5/6.0.2, access being restored) although frontmatter status and actions carry the patch. A reader of the summary alone concludes no fix exists. Move title/headline/summary via a correction record (this is the class the audit report's finding 4 names).

**#3 (F4) entries/2026-07-13/progress-sharefile-storage-zone-controller-shutdown.md**
- Claim / location: evidence[2] 'ShareFile customers with Storage Zone Controllers are not operational at this time.' publisher 'Progress ShareFile (vendor status page)'
- Evidence: https://status.sharefile.com/incidents/c59n5343lbkq
- Gap and fix: (low confidence) The vendor incident page reads 'Storage Zones Controllers are not operational at this time' (plural Zones, 5 hits; 0 hits for the evidence spelling). The quote is verbatim only in BleepingComputer's paraphrase of the status banner, yet is attributed to the vendor status page the run just re-pointed the citation at.

**#4 (F4) entries/2026-07-14/microsoft-july-2026-patch-tuesday-two-exploited-zero-days.md**
- Claim / location: '## Update' section of 2026-07-17: CISA 'is aware of active exploitation of vulnerabilities CVE-2026-32201, CVE-2026-45659, CVE-2026-56164, and CVE-2026-58644, enabling cyber threat actors...' cited to the CISA alert; and the same section 'lists it among four on-prem SharePoint CVEs'
- Evidence: https://www.cisa.gov/news-events/alerts/2026/07/14/cisa-urges-sharepoint-hardening-after-new-exploitations
- Gap and fix: (low confidence) The run re-aligned evidence[] to the alert's current six-CVE sentence (CVE-2026-50522 and CVE-2026-55040 added; confirmed via search summary of the page and the KEV feed dates 07-22 / 08-18) but left the body's in-quotation-marks four-CVE sentence unchanged, so the body quote is no longer verbatim on the page it links to (iteration 1 advisory #20 not acted on). Add 'as originally published' or quote the current text. Not machine-checkable: cisa.gov 403s every in-container transport.

**#5 (F4) entries/2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030.md**
- Claim / location: summary: 'NCSC-NL assesses short-term exploitation is expected. No confirmed in-the-wild exploitation as of 2026-07-18. Published as an audit-recovered item: the disclosure was public ~9 h before the day's single intel fire, which missed it.'; title '... exploitation expected short-term'
- Evidence: cves[] status [exploited, cisa-kev, patch-available]; own 2026-07-26 record ('went from no confirmed in-the-wild exploitation ... to confirmed exploitation: CISA added both CVEs to KEV on 2026-07-21'); https://www.rapid7.com/blog/post/etr-cve-2026-63030-wp2shell-a-critical-remote-code-execution-vulnerability-in-wordpress-core/ (Update, July 22: KEV July 21)
- Gap and fix: Top-of-entry drift on an entry this run edited (pre-existing): summary and title still describe the 2026-07-18 state (no exploitation, exploitation only expected) although the frontmatter and four later records say exploited and KEV-listed since 2026-07-21; the summary also carries workflow narration ('audit-recovered item ... the day's single intel fire ... missed it'). Move summary/title/headline via a correction record.

**#6 (F4) entries/2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave.md**
- Claim / location: sourcing_note 'no independent second source has covered the batch yet ... so there is no public exploitation signal'; verification: single-source; main analysis 'There is no public exploitation signal for any of these'
- Evidence: https://www.balbooa.com/blog/gridbox/gridbox-2-20-2-security-release (cited corroborating source) and the entry's own 2026-07-31 section (exploitation observed, Joomla Security Strike Team)
- Gap and fix: (low confidence) After the 2026-07-31 update the frontmatter says cves 65884/65885 exploited and Balbooa (vendor) is a listed corroborating source, but sourcing_note and verification still say single-source with no exploitation signal, and the summary/headline never mention the follow-on exploited flaws or 2.20.2 (action 2 says update to 2.20.2). Move sourcing_note/verification/summary to the current state.

**#7 (F4) entries/2026-07-29/cve-2025-15467-siemens-desigo-cc-cms-overflow-v7-unfixed.md**
- Claim / location: Detection paragraph still reads: 'For Mendix the observable is much more direct and lives in application access logs: unauthenticated requests to the app's REST or OData endpoints that return user records ... **Triage:** on the Mendix side, an anonymous endpoint returning a single record ...'
- Evidence: https://cert-portal.siemens.com/productcert/csaf/ssa-814963.json (revoked 2026-09-22, Mendix Runtime known_not_affected) and the record summary 'The Mendix CVE, product, action and analysis are withdrawn from this entry'
- Gap and fix: The update record and section withdraw the Mendix advisory and say its analysis is withdrawn, but the main analysis's Detection paragraph still gives Mendix detection and a Mendix Triage discriminator for a rejected CVE (4c(e): analysis contradicts the new state; the record's summary is false as written). Delete the Mendix sentences and the Mendix Triage line in a correction record naming body.

**#8 (F4) entries/2026-07-30/vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape.md**
- Claim / location: summary: 'No workaround exists for any of the five, so patching is the only control; none is reported exploited, and all were reported privately to Broadcom'
- Evidence: cves[] CVE-2026-59310 status [exploited, cisa-kev, patch-available]; tags actively-exploited; own records 2026-08-13 and 2026-08-28 (KEV 2026-08-18); evidence 'Current exploitation status: **Actively Exploited**' (NCSC Switzerland)
- Gap and fix: Top-of-entry drift on an entry this run edited (pre-existing): the summary still tells a reader 'none is reported exploited' although CVE-2026-59310 is exploited and KEV-listed per the entry's own later records; the title/headline/summary were never moved. Correct the summary via a record.

**#9 (F4) entries/2026-08-23/spectre-uat-10147-byovd-edr-callback-unlink.md**
- Claim / location: main analysis, 'Blinding the endpoint on Windows' paragraph: 'Talos names the affected class as *"kernel-callback-dependent security products such as CrowdStrike Falcon, SentinelOne, Microsoft Defender"*, alongside other unnamed vendors.'
- Evidence: https://blog.talosintelligence.com/uat-10147-deploys-spectre-a-cross-platform-implant-with-linux-rootkit-and-byovd-capabilities/ : 'Consequently, kernel-callback-dependent security products are rendered completely blind to new process creations, thread creations, and image load events for the remainder of the session' (0 hits for CrowdStrike / SentinelOne on the page)
- Gap and fix: The 2026-09-29 correction record and section say the attribution of three named products to Talos no longer holds and that summary and evidence were fixed, but the analysis paragraph still carries the removed quotation in quotation marks and attributes it to Talos (4c(e)/(f): the analysis contradicts the corrected state; the record's fields also omit body although body text must change). Delete the sentence/quote from the analysis and add body to the correction record's fields.

**#10 (F4) entries/2026-08-28/claroty-danfoss-ak-sm-800a-code-of-the-day-rce.md**
- Claim / location: body: 'a user-supplied value is formatted unsanitized into a shell command executed on the device, which Claroty used to achieve remote code execution: "the field value being formatted into the shell command is not sanitized and could include OS shell directives controlled by an attacker"'
- Evidence: https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers : 'The field value being formatted into the shell command is not sanitized according to our analysis and could potentially include OS shell directives that yield subsequent commands controlled by a potential attacker.'
- Gap and fix: The run restored the researchers' hedges in evidence[] ('according to our analysis', 'could potentially', 'a potential attacker') and the internal record says the quotation now carries the sentence as Claroty wrote it, but the body still quotes the un-hedged version in quotation marks and states the flaw flatly; the body quote is not a substring of the page. Restore the wording (or unquote and hedge) in the body under the same record.

**#11 (F4) entries/2026-08-28/kaltura-mwembed-unauth-rce-file-read-no-patch.md**
- Claim / location: main analysis, Triage paragraph: 'With no vendor fix available, WAF-level pattern blocking on those two parameter shapes is the only mitigation short of taking the endpoint offline entirely.'
- Evidence: https://kb.cert.org/vuls/id/308749 : 'Kaltura has released new patches to remediate these vulnerabilities in all affected legacy Player V2 versions.' (first published 2026-08-25, last updated 2026-08-28 19:59 UTC); entry title 'patched for legacy Player V2', cves status [patch-available]
- Gap and fix: The entry the run touched still tells readers in its main analysis that no vendor fix exists, contradicting its own title, cves status, summary and 2026-08-30 update record (4c(e)). Reword the sentence (patch legacy Player V2 or migrate to V7; WAF blocking is interim only) via a correction record naming body.

**#12 (F4) entries/2026-08-28/kaltura-mwembed-unauth-rce-file-read-no-patch.md**
- Claim / location: actions[0]: 'Block or heavily restrict access to mwEmbedLoader.php ... — no vendor fix exists, and this is the only available control.'
- Evidence: https://kb.cert.org/vuls/id/308749 (Solution: Kaltura has released new patches ... update to the patched version or, preferably, migrate to Player V7)
- Gap and fix: The action list rendered in the brief's Action Items still says no vendor fix exists and never tells an operator to apply the patched legacy Player V2 release or migrate to V7 (the current CERT/CC remediation); same stale state as the analysis. Replace via a correction record.

**#13 (F4) entries/2026-08-28/kudelski-bismarck-dprk-it-worker-gambling-fakecalls-overlap.md**
- Claim / location: sourcing_note: 'the quotes above are lightly redacted to remove literal indicators while preserving the analytic claim'
- Evidence: https://kudelskisecurity.com/research/inside-north-koreas-cybercrime-ecosystem-fake-it-workers-gambling-networks-and-malware : both evidence quotes are now contiguous verbatim sentences of the page (T4 triage: 'The sourcing_note's redaction rationale should not be applied to this sentence')
- Gap and fix: The internal record restored the second quote to Kudelski's exact words but left the sourcing_note saying the quotes are redacted; neither quote is redacted now. Correct the note (fields: sourcing_note).

**#14 (F4) docs/audits/2026-09-29-quality-audit.md**
- Claim / location: 'Twelve of those revisions carried news the entries had missed, two of them on critical-priority entries and the rest on high.'
- Evidence: entries/2026-08-29/eu-cra-reporting-obligation-ncsc-fi-checklist.md: priority: notable (one of the twelve, the CRA platform FAQ improvement)
- Gap and fix: (low confidence) Eleven update records plus the CRA improvement make twelve; PaperCut and Check Point are critical, nine are high, and the CRA entry is priority notable, so 'the rest on high' is wrong by one.

**#15 (F4) docs/audits/2026-09-29-quality-audit.md and prompts/CHANGELOG.md (4.16)**
- Claim / location: Report § Sources / systemic 1: 'One was a demoted archive record, 24 were repaired, and three remain unreadable' (1 + 24 + 3 = 28); CHANGELOG: 'flags exactly the 10 quotes they confirmed as real (six pages the publisher revised after publication, two non-verbatim quotes, one quote cited to the wrong page, one stale evidence record)'
- Evidence: state/source_health.json latest: 185 relevant (162 first sweep + 23), unreadable 3 (cisa-directives, cisa-news, ssd-disclosure), irrelevant/stale 2 (paradigm-shift-research, threatpost, both demoted); run record sources_changed has 25 items incl. paradigm-shift-research; page-checks-v4.txt: 10 quote flags = Metabase, ENISA FAQ x3, PaperCut, CNIL, Check Point (7 revised), Unit 42 + BlueMoon (2 not-verbatim), MAG (1 wrong page)
- Gap and fix: (low confidence) Disk gives 23 sources newly relevant (not 24 'repaired'; two of the 24 changed records, ssd-disclosure and cisa-directives, are still unreadable) and two demoted records (threatpost, paradigm-shift-research), so the 1+24+3 decomposition does not reproduce; the CHANGELOG's 6/2/1/1 breakdown of the ten flags does not match the triage (7 revised quotes on 5 pages, 2 not-verbatim, 1 wrong page).

**#16 (F4) docs/audits/2026-09-29-quality-audit.md and tools/check_run.py**
- Claim / location: Report § 2 'Of the 14 PDFs the store cites, the container could fetch ten, and on all ten the new decode is equal or better.'; § 3 'EUVD and git.kernel.org ... are now in the unverifiable-host list.'
- Evidence: grep of entries/: 15 distinct .pdf URLs (14 in HEAD + the ECA PDF added by this run); this pass ran old (HEAD) and new fetch_source.py pdf on all 15: 12 returned text (LHM, BKA, BSI unreachable), new equal or better on all 12 (nidec garbled in both); tools/check_run.py unverifiable-host set now also contains lore.kernel.org (edited 00:06:46Z, after the report)
- Gap and fix: (low confidence) The claim holds in substance (tests 13/13, WaterPlum now decodes: 44 hits for 'North Korean', 0 for '1RUWK'), but the counts (14, ten) and the host list (two hosts, code has three) do not match disk.


### Drop (low relevance / off-audience / duplicate)

**#1 (F7) entries/2026-08-28/cve-2026-59109-zalktis-peppol-einvoice-unauth-sqli.md**
- Claim / location: CVE-2026-59109 Zalktis (Latvian Windows accounting application), priority high
- Evidence: https://offseq.com/en/research/zalktis-cve-2026-59109/ : 'Zalktis Programmas confirmed remediation ... on 16 July 2026'; entry regions [europe], no exploitation, no public PoC, single source
- Gap and fix: (low confidence, pre-existing) A routine vendor-patched, unexploited injection in a Latvian desktop accounting product with no stated Swiss or CH-public-sector deployment, single-sourced to the discoverer, at priority high; it does not demand action beyond the patch cycle for this constituency and the entry names no Swiss/PEPPOL-in-CH nexus beyond the generic e-invoicing network. Consider dropping via an audit record or lowering priority.


### Needs more research

**#1 (F8) entries/2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave.md**
- Claim / location: cves[] and 2026-07-31 section list only CVE-2026-65884 and CVE-2026-65885 for the Gridbox audit; the run's internal improvement record re-read the source ('all eleven CVE records published ... four rated Attacked')
- Evidence: https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/ : '| CVE-2026-65887 | The password reset method resets any account's password and lets the attacker log in as that user, Super Users excepted ... 10.0 Critical (4.0), Attacked' and '| CVE-2026-65888 | The social login method logs the caller in as any user on the site ... 10.0 Critical (4.0), Attacked'
- Gap and fix: The page the run re-read names the four Attacked records: 65884, 65885 and two CVSS 4.0 10.0 account-takeover flaws (CVE-2026-65887 password reset, CVE-2026-65888 social login) that the entry never records. The record states 'CVE-2026-65884 and CVE-2026-65885 are both among the four' but leaves the other two (the highest-severity, exploited, one-request takeovers) out of cves[]/body, so a reader tracking CVEs for Gridbox misses two exploited 10.0s. Add them via an update/improvement record with the section (real delta: 11 CVEs published, 4 Attacked).


### Editorial / less-is-more flags (advisory)

**#1 (F11) entities/registry.yaml (actor:dire-wolf)**
- Claim / location: name 'Dire Wolf', aliases ['DireWolf'], no ambiguous_labels
- Evidence: docs/pipeline.md § Ambiguous labels: 'Set it when registering a name that is an English word ...'
- Gap and fix: (advisory, low confidence) 'Dire Wolf' is also the ordinary English name of an extinct animal and a well-known fictional creature, and the alias 'DireWolf' is not attested by any source the run read (VenariX writes 'Dire Wolf'); the site's phrase-match attaches any entry containing the label. Consider ambiguous_labels: ["Dire Wolf", "DireWolf"] (explicit-key attachment only, the Metabase entry already keys it) or drop the unattested alias.

**#2 (F11) entries/2026-08-28/taiwan-agentic-ai-intrusion-openclaw-hermes-guardrail-bypass.md**
- Claim / location: body: 'AI Agent can rapidly chain multiple attack methods together and utilize backup and testing secondary systems as springboards, giving attacks characteristics of high speed, low cost, and large scale' ([Taiwan Administration for Cyber Security, 2026-08-13])
- Evidence: https://moda.gov.tw/ACS/press/news/press/20394 (Chinese original: 'AI Agent可快速串聯多種攻擊手法，並利用備援、測試等次要系統作為跳板，使攻擊具備速度快、成本低及規模大的特性。')
- Gap and fix: (advisory, low confidence) The body quotes a machine-translation-proxy rendering in quotation marks with no '(translated from Chinese)' marker and different wording from the evidence[] translation the run just added; v4.2 requires reader-facing translated quotes to be marked and consistent. Use the evidence rendering and mark it.

**#3 (F11) entries/2026-09-06/mikrotik-routeros-mikrotrick-ssh-auth-bypass-privesc-chain.md**
- Claim / location: internal improvement record: 'CISA added CVE-2026-67279, the chain entry point, to its KEV catalog on 2026-09-25, and its status now records the listing.' (fields: evidence, cves)
- Evidence: KEV feed (catalog 2026.09.29): CVE-2026-67279 dateAdded 2026-09-25, 'This vulnerability can be chained to achieve unauthenticated exploitation of CVE-2026-86060'; the entry body covers KEV listings of CVE-2026-67277/86060 but never mentions 67279's
- Gap and fix: (advisory) A new KEV listing of the configuration-independent chain entry point is a reader-relevant fact recorded only as a status chip under an internal (never rendered) record; the analysis and the cited sources[] never state it or its date (no KEV feed source on the entry for it). Consider a non-internal update record with a short cited section.

**#4 (F11) entries/2026-07-14/microsoft-july-2026-patch-tuesday-two-exploited-zero-days.md**
- Claim / location: evidence[] NCSC-NL quote is raw Dutch: 'Volgens watchTowr is er een publieke exploit code voor SharePoint kwetsbaarheid CVE-2026-50522 gepubliceerd ...'
- Evidence: https://advisories.ncsc.nl/advisory?id=NCSC-2026-0237
- Gap and fix: (advisory) Untranslated non-English quotation in reader-facing evidence, with no 'translated from Dutch' marker and no original: field, on an entry whose evidence array this run edited (NetScaler shows the required shape). Translate, mark and add original:.

**#5 (F11) entries/2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030.md (and 2026-07-31 Unit 42)**
- Claim / location: reader-facing body: 'the WordPress core pre-authentication RCE chain this pipeline covered on 2026-07-18', 'found by this pipeline's own weekly quality audit', 'so the store already carried the correct attribution one entry earlier', 'this pipeline recorded reaching CISA KEV'; Unit 42: 'a CVE the store already tracked'
- Evidence: check 12 (no workflow-internal language in entries)
- Gap and fix: (advisory) The run says it replaced reader text naming the pipeline (Gridbox, ShareFile, Windchill) but the wp2shell body it edited still names 'this pipeline', 'the store' and 'the weekly quality audit' about eight times; same class on Unit 42. Reword to dated, cited facts.

**#6 (F11) work/2026-09-29T2134Z-audit/page-checks-final2.txt, docs/audits/2026-09-29-quality-audit.md, runs/2026-09-29/2026-09-29T2134Z-audit.md**
- Claim / location: final wider cited-page run (00:06Z) still ends '4 pass . 3 warn': ESET UEFI (kb.cert.org/vuls/id/616257), NATJack (lore.kernel.org), Kaltura CERT/CC quote (kb.cert.org/vuls/id/308749)
- Evidence: T3 verdicts (false-positive: kb.cert.org gzip, lore.kernel.org Anubis); this pass: the Kaltura sentence is verbatim on the live page and in the run cache (work/.../quote-bodies/ed17945d1cb4c8e3.extract.txt)
- Gap and fix: (advisory) After the fixes the last full backfill still reports three WARN, all checker false positives (kb.cert.org is still not read by the check path although the bridge now gunzips; lore.kernel.org was added to the host list only afterwards), and neither the report nor the run record states this final disposition or the 44-flag triage outcome. State it, or fix the check path so the run ends at zero.

**#7 (F11) runs/2026-09-29/2026-09-29T2134Z-audit.md (Verification & coverage notes); docs/audits/2026-09-29-quality-audit.md table**
- Claim / location: notes body: '**Sub-agent models.** Every sub-agent reported Sonnet 5.5', 'T1 read one cisa.gov alert through WebFetch', 'SR1 sampled it'; audit table row 'BlueMoon, Claroty, ... improvement, internal' (BlueMoon is a correction, internal)
- Evidence: check 12: no workflow-internal language ('sub-agent') in run-record notes; earlier run records' notes avoid it
- Gap and fix: (advisory) Run-record notes are published; use 'verifier and research helpers' or drop the labels. The audit table's Record column names BlueMoon's internal correction as an improvement.

**#8 (F11) entries/2026-08-20/cve-2026-19490-netscaler-gateway-aaa-auth-bypass.md; entries/2026-07-18/wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030.md; entries/2026-09-06/mikrotik-...; entries/2026-07-14/microsoft-july-...; entries/2026-09-10/bluemoon-...**
- Claim / location: internal (never rendered) records whose fields change reader-visible text or chips: NetScaler fields [evidence, summary] (summary moves from 'Rapid7 reports no observed exploitation as of 2026-08-19' to PoC public, attempts, KEV 2026-09-09); wp2shell fields [sourcing_note, actions, body] (two Action Items removed); MikroTik/Microsoft/BlueMoon cves[].status gain cisa-kev
- Evidence: CLAUDE.md: internal = 'a metadata-only fix with nothing to tell the reader'
- Gap and fix: (advisory) The NetScaler summary correction and the removed actions change what a reader sees in the brief but leave no rendered trace; a correction/improvement record with a one-line section would let readers see that a summary that said 'no exploitation' was superseded. Judgement call; the gate accepts it.


### Action-item discipline

**#1 (F18) entries/2026-07-30/vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape.md**
- Claim / location: actions[0] 'Patch vCenter to 9.1.0.0300, 9.0.2.0100 or 8.0 U3k on its respective track ...' and actions[2] 'Patch vCenter to 9.1.0.0300, 9.0.2.0100 or 8.0 U3k/U2f as applicable — there is no workaround — and on any appliance that was network-reachable and unpatched ... check the appliance's own scheduled-task and cron configuration'
- Evidence: actions[] of the entry
- Gap and fix: (low confidence) Two of three actions repeat the same vCenter patch step (an accumulated-list duplicate, exactly the class the Microsoft July entry's own record trimmed this run). Keep action 3 (patch + compromise check) and action 2 (VMXNET3 hosts); drop action 1.

### Verdict

NEEDS_FIXES (truth: 23, editorial: 3, advisory: 8)

- Truth = F3 x7 + F4 x16. Editorial = F7 x1 + F8 x1 + F18 x1. Advisory = F11 x8.
- High-confidence, must-fix before a CLEAN: ShareFile top-of-entry drift; Siemens Mendix detection paragraph; SPECTRE analysis still attributes the removed Talos quotation; Claroty body quote drops the hedges; Kaltura analysis and action 0 still say no fix exists; RSFiles `poc-public` tag; CNIL physician clause; Gridbox omits two exploited CVSS 10.0 CVEs (65887, 65888); VMware and wp2shell summaries say no exploitation; Kudelski sourcing note claims redaction that no longer exists.
- Coverage: no missed-angle finding beyond the disclosed Apple CVE-2026-86950 deferral; CVE-2026-88771/88772 (NetScaler KEV 2026-09-27) and WordPress 7.1.2 are covered by existing entries.

### Findings summary (machine-readable)

See `work/2026-09-29T2134Z-audit/verification.iter2.findings.yaml`.
