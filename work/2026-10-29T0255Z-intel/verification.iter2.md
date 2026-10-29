**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-29T05:53:19Z · ended_at=2026-10-29T06:21:38Z · duration_seconds=1699

## Verification report — 2026-10-29T0255Z-intel (iteration 2)

Scope: post-fix pass. All 438 claims in `claims.iter2.yaml` have a verdict row in `verification.iter2.claims.yaml` (all 72 changed claims, every claim of every entry named in the deltas block, and the remaining entries in full, so no quarter-sampling was needed): 428 ok, 7 F3, 1 F4, 2 unreadable (a Citrix Tech Zone page that answers 403 on extract, direct, jina and WebFetch, and the BSI CERT-Bund portal, a JavaScript shell; both claims are unchanged this run and are carried by earlier, readable fires; not raised as findings). `check_run.py` re-run: 61 pass, 0 warn, 0 fail.

### Prior-iteration deltas walked
- Check Point: the summary and body now say the sk "makes no statement on exploitation of Check Point gateways" (sk1000302 contains no exploitation text; CISA KEV lists both flaws since 2026-10-26); the Jumbo fix is stated as planned for 2026-11-11 (sk: "The fix is also planned for the release on November 11, 2026"). Correct. One placement nit (F11).
- KeyDrift: Cisco advisory v2.1 ("Added URL for Talos blog ... 2026-OCT-28") and "The Cisco PSIRT is aware of limited exploitation" are now attributed without claiming the revision added the exploitation line; the launcher sentence matches Talos (sshd launcher starts conf_sshd which drives the ptrace injector; aaamgr launcher runs the packed loader directly); second action dropped; run-record note corrected. Correct.
- PHP2Shell: "a chain" and "add a detailed account of a production compromise" are supported by Dream; Dream's tunnel wording needs one correction (F3 low confidence, below).
- WatchGuard: the listing's Published column (fetched live: 17 Fireware OS rows plus one Mobile VPN row, all 2026-10-27T15:5x) confirms 17+1 and seven at 9.0 or higher; CVSS 4.0 vectors confirmed on all seven pages; CCCS dropped. The tally sentence is cited correctly, but the next sentence and the Exposure line still cite one per-CVE page for multi-CVE facts (F3).
- testmetest: "eight of them published through four npm accounts" matches SafeDep; behaviour descriptions replace string indicators; T1685 dropped; action rewritten (acceptable). Correct.
- ConnectWise: S-K LLC and the Todyl attribution removed; Todyl's app ID (506e08f9...) and SpecterOps's "applications owned by the ConnectWise tenant (ID: 3f9cd7a0-...)" confirmed; Todyl's Graph-activity-log clause confirmed in the raw HTML (the text extract drops it); status-page updates of 21, 26 and 28 October confirmed. Correct.
- Huntress, MDaemon, VMware (T1687; WARP PANDA is an alias of `actor:verdantbamboo`; CrowdStrike text verbatim), Node2Shell (Ubuntu focal "Fixed in 1.0.7-6ubuntu0.1+esm1", nodejs on focal "Vulnerable"; Broadcom VMSA-2026-0008.1 values), Machelen (timeline dates), Veeam (CVE rows and scores), F5, Quest (Created 10/21, Last Update 10/28) and entity links: confirmed.
- Declined F7 (WatchGuard): agreed. The store carries comparable notable perimeter pre-auth rows (Fortinet FortiSandbox/FortiSIEM, Cisco Expressway CVE-2026-76466, NGINX three heap flaws, HPE Aruba); the entry is feature-dependent, unexploited and held to one action. No finding.
- Declined F2 (ConnectWise): not upheld. The status page's own HTML links a per-incident permalink, https://status.connectwise.com/pages/incident/619cf82551fec9053d612f09/6ad263692dc48705ab3da2cb, which I fetched and which carries the 28 October 17:09 UTC update; the Trust Center 403 is irrelevant to the status page. See F2 below. (The Trust Center advisory text itself is readable through a Wayback copy via the reader; it carries the "cannot determine independently", forwarding-rule and client-ID statements the older claims cite, so those claims verify.)

### Citation does not support the claim
- #1 F3 `2026-10-29/watchguard-fireware-2026-4-three-preauth-rows-at-9-2`: "seven of the 17 are scored 9.0 or higher, and for every one of them WatchGuard states that it is not aware of exploitation in the wild ([WatchGuard PSIRT](https://psirt.watchguard.com/CVE-2026-93866/))". That page carries only CVE-2026-93866's own score, fixes and exploitation line; the tally is on the listing and the other six statements are on six other pages. Same pattern in "Most rows affect Fireware OS 2025.1 up to before 2026.4 ... ([...CVE-2026-103594/])" (that page lists only the WireGuard row's range) and in the Exposure line (only "Access Portal enabled" is on CVE-2026-93866). Cite the listing for the tally and the per-CVE pages for the rest.
- #2 F3 (low confidence) `2026-10-21/php-critical-release-...` (update 04:55 and main body), `2026-05-15/cve-2026-46300-...` (update 04:52): "on two firewalls of a US government-affiliated organization built a persistent outbound SSH tunnel" / "set up an outbound SSH tunnel". Dream: the first firewall "crashed shortly after ... and never came back online"; the second was exploited on Oct 24 and "Built a persistent tunnel". Say the tunnel ran from the second firewall.
- #5 F3 (low confidence) `2026-10-29/mdaemon-clamav-unrar-cve-2025-8088-exploited-in-ukraine`: Exposure "an MDaemon server on Windows below 26.0.4 ... ([ClamAV, 2026-08-07])". ClamAV's notes carry the 0.101.0 to 1.5.3 range, not MDaemon or 26.0.4 (ESET's PDF does).

### Unsupported / hallucinated facts
- #3 F4 (low confidence) `2026-10-21/php-critical-release-...` sourcing_note: "no production victim is named by any source". The body names Camping.Care / TCS Camping ("after a data theft at its booking-system supplier Camping.Care", SRF and Blick tie it to the PHP flaws). The sentence was broadened this run; narrow it to Palo Alto's advisory and Dream's unnamed victims.
- #4 F4 (low confidence) `2026-10-29/huntress-mdm-enrolment-...`: "(gateway, agent and a PostgreSQL service)". Huntress (raw HTML): "Hexnode Gateway, the Hexnode agent, and supporting PostgreSQL components". Write "components".
- #6 F4 (low confidence) `2026-10-29/mdaemon-clamav-...` frontmatter `sectors: [public-sector]`: no cited page names a victim sector (ESET: "an active campaign in Ukraine in which Russia-aligned threat actors exploited a vulnerability in MDaemon mail server software").
- #7 F4 run record notes: "held to the five rows scored 7.3 or higher; the three lowest rows ... stay in the prose only". The Veeam entry's `cves[]` holds six records and CVE-2026-106078 is 6.9.

### Broken / unreachable URLs / Generic URLs
- #8 F2 `2026-10-18/connectwise-...` primary "https://status.connectwise.com/" (landing page, scrolling feed). Use https://status.connectwise.com/pages/incident/619cf82551fec9053d612f09/6ad263692dc48705ab3da2cb (fetched this iteration; carries the 2026-10-28 5:09PM UTC update). Lower confidence for the older Trust Center index citations: ConnectWise's 28 Oct update links https://www.connectwise.com/company/trust/advisories#cloudbackup.

### Needs more research
- #9 F8 (low confidence) `2026-10-29/veeam-cve-2026-108142-...`: `cves[]` carries CVE-2026-106077 (8.3, "Administrator role to read arbitrary files ... with LocalSystem privileges") but the body names only the 6.9 and 4.3 rows beside CVE-2026-106076.

### Editorial / less-is-more flags (advisory)
- #10 F11 Five update-record summaries (Fragnesia, ConnectWise, PHP, Node2Shell, ZDI) give pipeline rationale ("shortened to stay within its length limit", "condensed to offset the added text", "the main analysis"); state only what was removed.
- #11 F11 PHP update: undeclared body edits (Cisco URWB "(March 2027)" to "(November 2026)", correct per advisory v1.9; removal of the two-cluster and PHPSESSID details and of the lab-log-paths sentence) and two orphan evidence quotes (Karimi's "two source-address clusters" and the SecurityWeek reliability caveat) whose text left the body.
- #12 F11 ZDI: title "among six reports" and body "none of the six reports has a CVE" with the ConnMan sentence removed; the sixth is unexplained.
- #13 F11 Dated sections with present-tense statements the newest section supersedes: PHP 2026-10-27 "no source ties a named CVE to a production compromise"; Fragnesia 2026-09-05 "No source states confirmed in-the-wild exploitation of this specific CVE." Add "as of".
- #14 F11 VMware legacy em dashes (title, headline, `cves[CVE-2026-41709].affected`, 18 lines); none added this run.
- #15 F11 PHP update "which fits CrowdStrike's expectation ..." is the entry's own synthesis, in neither source.
- #16 F11 WatchGuard cites the advisory listing index for the 17+1 tally; defensible, left to the main agent.
- #17 F11 (low confidence) Check Point: "Spark has R82.00.11 ... and the fix is planned for the Jumbo Hotfix Accumulators of 2026-11-11" puts the gateway-section Jumbo sentence next to the Spark builds.
- #18 F11 (low confidence) Machelen: "On 2026-10-27 the Rhysida group listed" vs Ransomware.live "discovered on 2026-10-27".

### Missed angles
None found. The Apple 27.2 / iOS 18.7.11 backport of the exploited CVE-2026-86950 (SecurityWeek, 2026-10-27) is already in the headline of `2026-09-30/cve-2026-86950-...`; the KEV additions of 2026-10-28 are both covered; no relevant in-window gap surfaced. Coverage looks complete for critical and high signal.

### Verdict
NEEDS_FIXES (truth: 8, editorial: 1, advisory: 9)

Priority calibration, classification, F18 action discipline, relevance and dedup (KeyDrift and MDaemon declare their older entries in `references[]`): no findings. No TLP, watchlist or org-triage use.

### Findings summary (machine-readable)
See `work/2026-10-29T0255Z-intel/verification.iter2.findings.yaml` (18 records: F2 1, F3 3, F4 4, F8 1, F11 9).
