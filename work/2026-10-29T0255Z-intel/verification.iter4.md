**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-29T07:07:09Z · ended_at=2026-10-29T07:40:23Z · duration_seconds=1994

## Verification report — 2026-10-29T0255Z-intel (iteration 4)

Scope: post-fix pass after the iteration 3 NEEDS_FIXES. Claim ledger `claims.iter4.yaml` (466 claims): every claim has a verdict row in `verification.iter4.claims.yaml` (463 ok, 1 F4, 2 unreadable). That covers the 46 claims of `claims.changed.iter4.yaml`, every claim of the eight entries the remediations touched, and every claim of the remaining eleven entries (well above the quarter sample). The mechanical gate (`check_run.py`) was re-run: 61 pass, 0 warn, 0 fail.

### Prior-iteration deltas (each remediation checked against a page fetched this iteration)

- Node2Shell PAN-OS action and CVE record: Palo Alto's JSON timeline for CVE-2026-111497 carries "Removed ETAs for 11.2.4-h23, 12.1.4-h13 and 12.1.10-h3 as these versions are released" (2026-10-29T05:30Z) and the product table lists all nine builds without an ETA. The action, the `fixed` string and the 2026-10-29 section are correct and dated. The new Broadcom paragraph (VMSA-2026-0008.1, SDDC Manager 9.1.1.x critical 9.8, 9.1.0/9.0.x/5.2.x important 7.5, patch pending, KB460732 and KB460734) matches Broadcom's page. OK.
- WatchGuard exposure clause: all seven per-CVE pages are now cited and between them carry every listed feature (Access Portal, SIP proxy, FireCluster, AD authentication server, FireCloud Gateway, FIPS mode with external log server); scores 9.2/9.5/9.1 are on the page vectors; the 17+1 tally and seven at 9.0 or higher match the listing. OK.
- ZDI action: "the AlmaLinux el9 kernel also covers CloudLinux 9" is right (TuxCare table: "Same kernel as AlmaLinux 9 ... fixed in the same AlmaLinux 9 kernel"), but the closing clause is still contradicted for CloudLinux 7h and 8 (finding #1).
- PAN-OS PHP2Shell entry: Palo Alto's advisory (HTML and /json/) read this iteration: twenty hotfix builds in the table, nineteen without an ETA, only `>= 11.1.7-h12 (ETA: 10/30)`; the timeline entry of 2026-10-29T05:20Z removes the ETAs of 10.2.7-h39, 10.2.10-h42, 11.2.4-h23, 12.1.4-h13 and 12.1.10-h3. Title, headline, summary, both `fixed` strings, action, body and the new section state exactly that; the record summary matches the section and `fields` covers every changed line (diff checked). The 2026-10-28 section's "fourteen released, six due" is dated "as read on 2026-10-28" and matches the cumulative ETA removals (3+4+4+3). OK. The run-record note that still defers this re-read is stale (finding #2).
- PHP entry: vendor-list sentence ("all but one ... 11.1.7-h12 due on 2026-10-30") is correct; Dream's account (24 rooted of 240 narrowed from about 19,000, eleven profiles of which nine exploitable, PHP 8.0.30, nobody user, under 15 minutes, first firewall crashed, second exploited, tunnel, management server, AD spray, not attributed) matches the post; Cisco "27.1.1 (November 2026)" matches version 1.9. The Sansec remark is no longer an orphan but the discrepancy is no longer surfaced (finding #3).
- Machelen summary and registry notes: Ransomware.live wording ("recorded on 2026-10-27 that Rhysida had listed") matches its page. OK.
- Fragnesia record: lists the removed summary clause; diff confirms nothing else was dropped undeclared. OK.
- ConnectWise SaaS Security sentence: now "As of 2026-10-19 ..." and matches the Trust Center update of 2026-10-19 01:15 UTC (read from the 2026-10-25 archive copy).
- Declined (a): Trust Center anchor URL. Acceptable on its merits. The page at the unanchored URL is ConnectWise's own advisory page; the archive copy I read (https://web.archive.org/web/2026/https://www.connectwise.com/company/trust/advisories) carries the Cloud Backup advisory as a lead item and every Trust Center statement cited (seven client IDs, 2026-10-17 07:00 UTC disablement, credentials no longer valid, no successful threat activity observed, 2026-10-19 01:15 UTC suspension of Cloud Backup, SaaS Security and Cloud Management, 2026-10-21 attribution and phased restoration); the anchored form would raise a fresh source-urls WARN (403 on every transport) that a run may not acknowledge. Not re-raised.
- Declined (b): VMware em dashes. Acceptable: no em dash or workflow wording was added by this run and every line it edited is clean; the legacy lines need title/headline in a record's `fields`. Kept as an advisory F11 (#6).

### Unsupported / hallucinated facts

- #1 (low confidence) `2026-10-25/zdi-linux-kernel-reports-public-skb-zerocopy-root-exploit`, actions[0]: "the sources read show no fixed kernel yet for other distributions". TuxCare (https://tuxcare.com/blog/zdi-ksmbd-bugs-cve/): "Fixed CloudLinux 7h and 8 kernels (4.18.0-553.177.1.lve.1) are in beta." Sysdig's 28 October update: "CloudLinux 7 hybrid and 8 fixes are in beta." Say "no fixed production kernel yet" and name the CloudLinux beta kernels, or drop the clause.
- #2 `runs/2026-10-29/2026-10-29T0255Z-intel.md`, Coverage gaps: "Palo Alto's remaining PAN-OS hotfixes (12.1.4-h13, 12.1.10-h3, 11.2.4-h23 and others due 2026-10-29 and 2026-10-30) are to be re-read at the next fire." The run re-read the advisory and shipped it (records of 07:04:32Z and 07:03:00Z); Palo Alto lists all three as released and only 11.1.7-h12 still carries an ETA. Delete or restate.

### Surface contradiction

- #3 (low confidence) `2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619`: "The advisory for the second flaw also lists heap use-after-free and memory disclosure among the confirmed impacts ([PHP]), and Sansec says the leaked worker memory can hold passwords, session tokens, API keys and TLS private keys from other requests ([Sansec])". Sansec: "CVE-2026-109618 also discloses server memory on its own"; PHP's GHSA-6wmf (CVE-2026-109619) lists memory disclosure and GHSA-w8hw (CVE-2026-109618) does not. The two clauses read as one flaw; restore the one-clause note or name the CVE Sansec means.
- #4 (low confidence) `2026-10-29/moldova-egovernment-mass-extraction-unauthenticated`: AGE's timeline says "82 de servicii publice si peste 30 de sisteme informationale si panouri de administrare au fost deconectate preventiv"; its introduction says it verified 82 services and suspended the exposed ones; the Prime Minister says 30 of the 82 were disconnected. The body gives AGE as "reviewed 82 digital services and disconnected the exposed ones" and only the Prime Minister's 30; the sourcing note says the figures differ. Put AGE's timeline figure in the body.

### Editorial / less-is-more flags (advisory)

- #5 F11: `entities[]` omits registry product keys that exist: WatchGuard (`entities: []`, product:watchguard-fireware-os), KeyDrift (product:cisco-catalyst-sd-wan-controller, -manager, -validator), testmetest (product:npm, product:github-actions, product:gitlab-ci).
- #6 F11: VMware legacy em dashes and "this entry" wording in text this run did not touch; left to the audit (see decline (b)).

### Other checks that came back clean

- Update-record contract (4c) for all nine updated entries: each section is the same finding with a genuine delta, `updated_at` equals the record `at`, `fields` covers every changed frontmatter line in `git diff HEAD`, summaries match sections, no silent edits, no superseded statement left standing (the Node2Shell 2026-10-27 and 2026-10-28 PAN-OS and Ubuntu statements are dated as read on those days). No em dash, KEV deadline or workflow wording was added anywhere.
- Counts re-derived from primaries: Oracle CPU 1295 patches, 112 rows at 9.0 or higher, 90 unauthenticated network rows, 73 distinct ids, six at 10.0 (raw HTML risk matrices); WatchGuard 17+1 rows, seven at 9.0 or higher; PAN-OS 19 of 20; Veeam six CVE rows, floor 6.9.
- Coverage: NCSC.ch hub (newest post 13109, covered), KEV window (two additions, both given records; the Adobe Commerce and Node2Shell additions of 2026-10-27 are covered by earlier entries), and the PHP2Shell vendor wave (NetScaler, QNAP, HPE ClearPass, Cisco, F5, Check Point, Trend, Quest, NetApp each have an entry) show no missed critical or high item; coverage looks complete.
- Unreadable: Citrix NetScaler Tech Zone post (403 on extract, url, jina and WebFetch; its statement is corroborated by NCSC-NL's list and Citrix CTX697263) and BSI CERT-Bund WID-SEC-2026-2569 (JavaScript shell); F5 K000163821 is unreadable and the entry says so.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 2, advisory: 2)

### Findings summary (machine-readable)

See `work/2026-10-29T0255Z-intel/verification.iter4.findings.yaml` (6 records: F4 x2, F9 x2, F11 x2).
