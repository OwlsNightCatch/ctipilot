**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-14T03:54:52Z · ended_at=2026-10-14T04:11:22Z · duration_seconds=990

## Verification report — 2026-10-14T0255Z-intel (iteration 1)

Scope walked: 5 new entries, 3 updated entries (whole entry plus `git diff HEAD`), the run record, `prior_coverage.json`, registry and `cves_seen` (HEAD). All 176 ledger claims have a verdict row in `verification.iter1.claims.yaml` (160 ok, 6 F3, 9 F4, 1 F14). Primaries were re-fetched live this iteration (Volexity, Ivanti blog, Rapid7 x3, CISA alerts via WebFetch, MSRC per-CVE records and the saved CVRF parsed for fixed builds, Exchange team posts, Adobe raw bulletin HTML parsed per CVE, GitLab release pages, NCSC 13051 and 13054, CERT-EU, CERT-FR including its revision history, MDR, AFP, BFMTV, Infosecurity, BleepingComputer, Cooling Post, Claroty, CCCS). Gate-uncheckable quote (MSRC CVE-2026-96951 evidence quote) matches the MSRC record verbatim. The four translated evidence quotes (CERT-FR x3, BFMTV, MDR x2) match their `original:` text on the live pages and the translations are faithful. No prior-iteration deltas block (first pass).

### Citation does not support the claim
- #1 F3 `2026-10-14/exchange-oct-2026-su-cve-2026-70571-last-2016-2019-update`: "The fixed builds are Exchange Server Subscription Edition RTM 15.02.2562.056, 2019 CU15 15.02.1748.055, 2019 CU14 15.02.1544.050 and 2016 CU23 15.01.2507.077" cited to the Exchange Team post 4563014. The post body (decoded in full from the page's embedded JSON; WebFetch returned only the title) names SE RTM, 2019 CU14/CU15 and 2016 CU23 but has no build or KB numbers. The builds and KB5128895-98 are in the MSRC CVRF/CVE records. Fix: cite the MSRC per-CVE pages for the builds.
- #2 F3 `2026-08-28/claroty-copeland-xweb-pro-refrigeration-unauth-root-rce`: "Claroty reports no exploitation in the wild of these flaws, but CERT-FR's alert of 2026-10-13 reports numerous compromises ... ([CERT-FR, 2026-10-13])". Claroty's article has no statement about in-the-wild exploitation at all; CERT-FR does not mention Claroty. Same attribution in the summary ("Claroty reports no exploitation") and the record summary ("Claroty's 'no exploitation reported'"). The pre-update wording was passive. Fix: "the sources read do not report exploitation" or "Claroty's article does not address exploitation".
- #3 F3 `2026-10-13/cve-2026-97229-gitlab-ci-regex-compiler-unauthenticated-rce` (Update 03:43): "...and the trigger is then a request without credentials ([Rapid7, 2026-10-13])". Rapid7's blog gives only the setup precondition; the credential-less delivery is in the PoC README ("After that setup, a request without credentials executes the selected command"). Fix: add the README citation to that clause.
- #4 F3 `2026-10-14/tangerhuette-digitales-rathaus-zero-day-municipal-portal`: "a citizen portal and app that has been online since 2020" cited to the 2026-10-13 MDR AKTUELL article. That article has no mention of 2020 or an app; "Nach langer Vorbereitung ging es 2020 online. Mit einer App ..." is in the 2026-09-16 MDR Sachsen-Anhalt article. Fix: cite the September article for that clause.
- #5 F3 (low confidence) `2026-10-13/danfoss-...`: "twice the first estimate of 150 that Infosecurity quotes". BFMTV says "deux fois plus élevé que les premières estimations, qui faisaient état de 150 points de vente"; Infosecurity quotes "150 of its Intermarché stores and 30 of its Netto brand" (180). Same in sourcing_note.
- #6 F3 (low confidence) `2026-10-13/danfoss-...`: "CERT-FR's sequence is to remove the internet exposure, factory-reset the unit, reconfigure it, restore access only through a secure VPN ..." CERT-FR's compromised branch is: remove exposure, Reset Factory; then restore access via VPN, reconfigure, apply best practices. Order differs.

### Unsupported / hallucinated facts
- #1 F4 claroty-copeland: "both obtainable from unauthenticated public endpoints or local-network broadcast". Claroty: "can be obtained via unauthenticated public endpoints" / "publicly accessible"; no "broadcast" on the page. Pre-existing text in an entry this run edited.
- #2 F4 (low confidence) claroty-copeland: "can display a normal temperature on the supervisory UI" and the Triage discriminator built on it. Claroty falsifies "the temperature shown on the XR60CX display" (the field controller); it never says the XWEB supervisory UI shows the false value.
- #3 F4 (low confidence) gitlab: after the update the summary says the demonstrated path needs push access, the README says "The chain requires project write access", but `cves[].auth: pre-auth`, `vector: zero-click` and the `pre-auth` tag are unchanged while the record's `fields` names `cves` and `tags`.
- #4 F4 (low confidence) ivanti summary: "running entirely in memory" (Volexity: library code patched in memory only; `h.py` written to disk, helper scripts in /tmp, renamed tcpdump) and "stealing ... LAPS passwords and BitLocker recovery keys" (Volexity: tool written "to search" for them; obtaining them is not stated; the body correctly says "went after").
- #5 F4 (low confidence) tangerhuette Detection: "commands from the web application's service account". MDR never mentions a service account.
- #6 F4 (low confidence) windows-shell: `Rapid7 describes the effect as Windows showing no "protected your PC" dialog`; Rapid7's words are "a dialog explaining that Windows protected their PC".
- #7 F4 (low confidence) adobe: `techniques` T1505.003 (web shell) has no source support in APSB26-144/152/153.

### Quantifier without source
- #1 F14 (low confidence) adobe summary: "three unauthenticated CVSS 10.0 code-execution flaws in Experience Manager ... and two in Adobe Commerce and Magento Open Source": APSB26-153 scores CVE-2026-103849 at 10.0 and CVE-2026-92909 at 9.8.

### Drop (low relevance / off-audience / duplicate)
- #1 F7 (low confidence) adobe: no exploitation, no PoC, Adobe's summary calls it priority 2; "ahead of the regular cycle" rests on no cited source and CVSS alone does not clear the out-of-cycle bar. August ColdFusion entry is precedent; keep short or state a source-backed exposure reason.
- #2 F7 (low confidence) tangerhuette: German commune, single vendor account, no vector, no actor, AI attribution unconfirmed by police; the entry names no nexus ground (global significance / transferable TTP / actor targeting the constituency core / imminent shared threat) and says "whether any Swiss body runs it is not reported". State the ground or hold at routine.

### Surface contradiction
- #1 F9 (low confidence) windows-shell: Rapid7 says "Windows Server 2012 doesn't receive a patch, although Server 2012 R2 does". The saved MSRC CVRF for CVE-2026-96951 lists Server 2012 R2 through 2025, Windows 10/11 and Outlook.com but no Windows Server 2012 product (the product is in the 2026-Oct CVRF and appears on 641 other CVEs): neither affected nor fixed. The entry states "receives no update" four times as unpatched exposure without noting the discrepancy.

### Action-item discipline
- #1 F18 (low confidence) claroty-copeland action: the VPN/take-off-internet clause duplicates the Danfoss entry's action, which already names Copeland xweb; keep the firmware v1.13 task.
- #2 F18 (low confidence) ivanti actions[1]: restates the Detection paragraph (proxy/WAF header search, DC LDAP review) plus CISA's recovery steps; one sentence would do.

### Editorial / less-is-more flags (advisory)
- F11 ivanti: `.icscap` is an attacker-chosen directory name (file-name indicator); T1558.003 mapped although Volexity says the Kerberoast function "was not used"; Rapid7's note that a portion was fixed in the July 2026 25.1.3.0 release and exploitation occurred during the backport is omitted.
- F11 danfoss and claroty-copeland: `product:copeland-xweb` and `product:dixell-xweb` were registered this run with the Danfoss entry as relation source, but neither entry carries them in `entities[]` (Claroty entry has `entities: []`).
- F11 claroty-copeland: 27 lines with em dashes in title, `cves[].affected` and body (pre-existing, entry edited this run).
- F11 exchange Detection: "a failed attempt is more likely to appear as a crash than a shell" is an unsourced likelihood; label as inference.
- F11 windows-shell: headline "strips the Mark of the Web warning" asserts a mechanism; Microsoft says "evade MOTW defenses" and classes it CWE-77 command injection (CISA: "Command Injection Vulnerability"), absent from the body.
- F11 adobe: body mentions the CVE-2026-75650 hotfix; `2026-09-08/stylesmuggler-cve-2026-75650-magento-adobe-commerce-rce` is not in `references[]`.

### Checked and found sound (no finding)
Ivanti: versions, KEV, Volexity chain, Integrity Checker, CISA recovery and EOL date, CCCS 25.2.2 discrepancy as stated, classification A/1, critical priority justified (exploited zero-day on a perimeter VPN with an unpatched companion step). Windows: all nine KBs and builds match the CVRF, CVSS 8.8, exploited Yes / disclosed No, KEV same day; high is right. Exchange: CVSS, ratings, ESU statements, KBs in the frontmatter match the CVRF. Adobe: all ten CVE ids, scores, PR:N vectors, affected/fixed versions and the Magento 2.4.6 gap match the raw bulletins. GitLab update: reproduction, PoC caveats, versions, 90-day and single-node statements, NCSC/CERT-EU/BleepingComputer, 19.4.1 same-reporter claim all hold; record type `update` is warranted. Danfoss update: CERT-FR revision (12 Oct initial, 13 Oct "Ajout d'autres équipements ciblés"), NCSC 13054 (Actively Exploited), Cooling Post dates, AFP/BFMTV/BC statements hold; record summary equals the section; no superseded statement left in the main analysis. Claroty update: record `fields` cover every changed line; the section is accurate (names no models/flaws/vector, no tie to Claroty). Dedup: none of the new CVEs existed in the committed `cves_seen`; no existing Ivanti Connect Secure, Exchange, Windows Shell, Adobe Oct, or Tangerhütte entry. F16 (no org_triage/watchlist), F17 (all classifications present and plausible), F12 (single-source entries carry `single-source` plus sourcing_note) clean. No IOCs, no em dashes in the new entries, no KEV deadline used as a reason.

### Missed angles
None found. The run record's drop list (Patch Tuesday remainder at Exploitation Less Likely/Unlikely, Cisco Nexus, Fortinet bundle, Esri, OTRS/Znuny, IBM Liberty, the three NCSC.ch catch-up advisories handed to the audit) is defensible against the critical/high bar; the Rapid7 Patch Tuesday post confirms exactly one exploited Microsoft flaw and two disclosed (.NET WDAC bypass needs a local foothold, MessagePack-CSharp DoS). Coverage looks complete for the window within what I could check; the Veeam and Zimbra vendor-page reads already flagged for the next audit remain the only open lead.

### Verdict
NEEDS_FIXES (truth: 14, editorial: 5, advisory: 6)

### Findings summary (machine-readable)
See `work/2026-10-14T0255Z-intel/verification.iter1.findings.yaml` (25 records).
