**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-13T06:23:53Z · ended_at=2026-11-13T06:44:55Z · duration_seconds=1262

## Verification report — 2026-11-13T0256Z-intel (iteration 6)

Scope walked: all 7 claims of `claims.changed.iter6.yaml`, every claim of the four entries remediated in iteration 5 (Citrix 52, N-able 42, Check Point 28, WFX Phantom 14 = 136), and a random quarter of the other 255 claims (64, `random.seed(20261113)`), 200 claims in all; 200 verdict rows are in `verification.iter6.claims.yaml` (199 ok, 1 F3). All 16 entries were read end to end, every cited page of the seven new entries and the new sections of the nine updated entries was re-fetched this iteration (extract, raw HTML, the MSRC Security Update Guide API, CVE List API, ENISA EUVD API, KEV catalogue, BSI CSAF, and the first ANSSI REACTIV PDF read from page images).

### Prior-iteration deltas (iteration 5), each checked against the cited source
1. Citrix CTX697305 four ADC/Gateway builds vs CTX697320 Console build: confirmed. CTX697305 lists "Citrix NetScaler ADC and Citrix NetScaler Gateway 14.1-73.57 ... 13.1-64.39 ... 14.1-73.58 FIPS ... 13.1-37.293"; CTX697320 lists only "Citrix NetScaler Console 14.1-74.34 and later releases". The body now cites each build to the right bulletin.
2. N-able root-escalation clause: confirmed. Axis post (oss-security 2026-11-06) names the CVE and Axis 1.x only; BleepingComputer (2026-11-12) says "The attack combines an Apache Axis vulnerability, tracked as CVE-2026-90436, with a separate N-central privilege escalation weakness"; Huntback describes the nable-to-root helper chain. Both are now cited at the clause.
3. Check Point closing clause: the sk1000302 statement now cites sk1000302, and "sk1000302 itself still carries no exploitation statement" is true (no "exploit" in the page body). A neighbouring clause fails adjacency, see F3 #1.
4. WFX actions[0]: confirmed. StepSecurity lists the PR title and the commit messages `ci: refresh build cache`, `ci: restore`, `ci: cleanup`, `chore: add ci helper`, `chore: add dependency audit workflow`; the action carries all of them, the AWS trust-policy changes, access keys and Azure federated credentials.
5. Citrix title/headline/summary: `memory-safety` gone from all three; the body's first sentence still carries it (F11 #2, low confidence).
6. and 7. Declined advisory items: judged on the facts below (F11 #3 and #4); I agree both are advisory.

### Citation does not support the claim
**F3 #1 — Check Point entry, `## Update — 2026-11-13T03:59:06Z`, claim 379bd267c1.** Quote: "The fix for both flaws is in Jumbo Hotfix Accumulator R82.20 take 14, R82.10 take 52, R82 take 132 and R81.20 take 174 or later, none is listed for R81.10 or R81, and the Spark fixes are now stated as builds from B998002843 and B996005005 ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000302))". The preceding sentence calls CVE-2026-123039 "a second flaw", and the record summary says "the Jumbo takes now carry both fixes", so "both flaws" is PHP2Shell plus CVE-2026-123039. sk1000302 (read this iteration) never mentions CVE-2026-123039 (0 hits for "123039" in its text) and states only the PHP fix: "This problem was fixed. The fix is included in: Jumbo Hotfix Accumulator for R82.20 starting from Take 14 ... R81.20 starting from Take 174". The CVE-2026-123039 fix location, and the absence of a Jumbo for R81.10/R81 (affected versions "R82.20, R82.10, R82, R81.20, R81.10, R81"), come from sk1000362, which this clause does not cite. Fix: add the sk1000362 link to the clause or narrow it to the PHP flaws.

### Editorial / less-is-more flags (advisory)
**F11 #2 — Citrix body, first sentence** "fixes 28 memory-safety and input-handling flaws" (low confidence). Bulletin row CVE-2026-111338 is "Sensitive authentication material written to a log file" (CWE-532); CERT-EU says "28 memory flaws". Leave or say "memory-safety and other flaws".
**F11 #3 — .NET entry Exposure line** (iteration 5 item 6). MSRC revision 7 lists Windows 10/11/Server 2019 to 2025 (KB5131096, KB5131085, KB5131090, KB5131080/KB5131077, KB5131087, KB5132061/KB5132043, KB5132059), PowerShell 7.4 to 7.6 and Visual Studio 2017 to 2026; summary, takeaway, cves[] and the action carry it, the Exposure line does not. No false statement; advisory, may be left.
**F11 #4 — Dixell/Copeland download-page citation date** (iteration 5 item 7). The page is an undated list (newest item 2018/07/09); 2026-11-13 is the reading date. The supported statement ("only up to 5.2.3 of 2018") is accurate; advisory, may be left.
**F11 #5 — WFX Phantom** (low confidence). BleepingComputer, cited by the entry, says "Some of the compromised accounts belonged to Fortune 100 organizations, the US General Services Administration, the French government, Nextcloud, and WebdriverIO."; the entry gives no public-sector hook (sectors: technology). One attributed clause would add it.

### What was checked and held
- Citrix: all 29 cves[] scores equal the bulletin rows (28 in CTX697305 plus CVE-2026-120869 at 9.4 in CTX697320); the "9 of them 9.0 or above" count and CERT-EU's "ten ... high impact" count both recompute from the bulletin vectors; CVE List records carry 9.3/9.5/8.7 scores for the 14 published ids and none exists yet for CVE-2026-111333 to 111339 and 120860 to 120867 (as the sourcing note says); the bulletin revision history reads "Fixed a typo in CVE numbers CVE-2026-111333 ... CVE-2026-111339"; none of the ids is in the KEV catalogue (catalog 2026.11.10); CVE-2026-120869 is 9.3 network in both ENISA and the CVE record.
- N-able: seven CNA records (scores and privileges) match the sourcing note; the 21 servers, 19 on Hotfix 2, country list (9+4+4+1+1+1+1=21, no Switzerland), Legacy API statements, Tenable "no fix for the November 12 claims", "follow-up hotfix", and the oss-security Axis statement all match their pages.
- Check Point: sk1000362 (dynamic_server, world-writable socket, "a couple of dozen customers", dynamicCli.log), sk1000302 (six features, Jumbo takes, Spark builds, R81.10 hotfix), Check Point Research (first wave 2026-10-30, ESXi pivot, destroy_v6, TSGA/PhiliKit, UNC5221 hedging) and the KEV listing (PHP CVEs added 2026-10-26) all match.
- WFX: StepSecurity, Aikido, Endor Labs and BleepingComputer figures (63,000 probes; 4,837 accounts; at least 1,835 repositories; 8,926 repositories; 1,838 repeat repositories; forged status checks active per Aikido, off in all 101 copies per StepSecurity) match.
- Other new entries and updates: PTC (CNA scores/vectors, release lines, NCSC post, BSI CSAF "entfernter, anonymer Angreifer", Trust Center change log 11/11), SignDrop (Cyderes), DarkLunnen (Group-IB datePublished 2026-11-11; 4,725 Swiss targets; restic row; Fortinet FG-IR-24-535 table), Huntress Teams booking, Dixell (seven VulnCheck advisories' scores and ranges, 14 ENISA rows with 7 at 9.2 or above, EoS bulletin, Dixell France guide, CERT-FR alert last version 2026-10-16, NCSC post 13054 edited 2026-11-06, BACS warning, Ransom-ISAC XWEB Pro log), Trend Micro advisory table of Nov. 12 and the Download Center pages, mod_http2 (Debian, USN-9090-1, Alpine, SUSE pending, researcher repository, Wordfence), Confluence (Atlassian advisory, BSI "hoch"), .NET (MSRC revision 7 note verbatim, the KB numbers per Windows branch), Brotli (Apple notes 149715 to 149724 and 149851, Cisco v1.12, Mitel 8.1, Siemens SSA-443410/242944/678870 counts 15 and 28), ScreenConnect (ConnectWise disclosure, ENISA 9.3, The Record, Blackpoint, Huntress, Sophos), ANSSI (second report p.3 to 6; first report pp.3, 5, 6 read as images: 99/67/32, Metabase nine instances, Tchap, SNU 275 000, TRACFIN 136 and 213).
- Style: no em dash, workflow vocabulary, IOC pattern (IP, hash, defanged host) in any reader-facing field of the 16 entries; classification present on every entry; no org_triage or watchlist use; priorities (Citrix high, Check Point high, N-able high, the rest notable) hold under the 5b bar.
- Run record notes: file and count claims hold (7 entry files present, Saxony pager entry absent, 29 Citrix records, the 18 stray root-level scratch files exist).

### Missed angles
None evidenced. KEV window diff shows 0 additions since 2026-11-12; Patch Tuesday zero-day CVE-2026-124194 and BeyondTrust CVE-2026-102764 are already covered by earlier entries; two searches (zero-days of 12 Nov 2026; BACS notices of Nov 2026) surfaced nothing relevant that the store lacks. Coverage looks complete.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 0, advisory: 4)

### Findings summary (machine-readable)
```yaml
- code: F3
  category: claim-not-supported
  section: check-point-php2shell-sk1000302-portal-and-vpn-gateways / Update 2026-11-13T03:59:06Z (claim 379bd267c1)
  item: Check Point PHP2Shell and CVE-2026-123039 (entries/2026-10-29/check-point-php2shell-sk1000302-portal-and-vpn-gateways.md)
  url_or_quote: The fix for both flaws is in Jumbo Hotfix Accumulator R82.20 take 14, R82.10 take 52, R82 take 132 and R81.20 take 174 or later, none is listed for R81.10 or R81, and the Spark fixes are now stated as builds from B998002843 and B996005005 ([Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000302))
  summary: 'The preceding sentence introduces CVE-2026-123039 as ''a second flaw'', so ''both flaws'' binds the PHP2Shell CVEs and CVE-2026-123039, but the only citation is sk1000302, which never mentions CVE-2026-123039 (grep of the page body for 123039: 0 hits) and lists only the PHP fix (''This problem was fixed. The fix is included in: Jumbo Hotfix Accumulator for R82.20 starting from Take 14 ... R81.20 starting from Take 174''). The CVE-2026-123039 half (same four takes; affected R81.10 and R81 with no Jumbo listed) comes from sk1000362, which the clause does not cite. Fix: add [Check Point, 2026-11-12](https://support.checkpoint.com/results/sk/sk1000362) to the clause, or narrow the clause to the PHP flaws.'
- code: F11
  category: editorial-advisory
  section: citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws / body paragraph 1
  item: Citrix NetScaler ADC/Gateway CTX697305
  url_or_quote: Cloud Software Group's bulletin CTX697305 of 2026-11-12 fixes 28 memory-safety and input-handling flaws in customer-managed NetScaler ADC and NetScaler Gateway
  summary: (low confidence) Iteration 5 asked for 'memory-safety' to go from the title, headline and summary and that was done, but the body's first sentence keeps 'memory-safety and input-handling'. Bulletin row CVE-2026-111338 is 'Sensitive authentication material written to a log file' (CWE-532), neither category; CERT-EU's own wording is '28 memory flaws'. Advisory; acceptable to leave or to say 'memory-safety and other flaws'.
- code: F11
  category: editorial-advisory
  section: cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix / Exposure line (iteration 5 item 6, declined by the main agent)
  item: CVE-2026-111497 .NET OOB
  url_or_quote: '**Exposure:** a framework-dependent host shows its runtime with `dotnet --list-runtimes`, which must list 8.0.33, 9.0.22 or 10.0.14; self-contained applications and container images carry their own runtime'
  summary: '(low confidence) Judged on the facts: MSRC record revision 7 (read through the Security Update Guide API this iteration, 50 affectedProduct rows) lists Windows 10/11/Server 2019 to 2025, PowerShell 7.4 to 7.6 and Visual Studio 2017 to 2026 with KBs per branch; the Defender takeaway, summary, cves[].affected and actions all carry that scope and only the Exposure line still describes .NET hosts alone. Agree this is advisory and may be left; no statement in it is false.'
- code: F11
  category: editorial-advisory
  section: dixell-copeland-xweb-evo-vulncheck-cves-end-of-service / sources[] and inline citation (iteration 5 item 7, declined again)
  item: Copeland XWEB EVO download page
  url_or_quote: ([Copeland, 2026-11-13](https://webapps.copeland.com/Dixell/Pages/XWEB300D_500D_500_EVO))
  summary: '(low confidence) Judged on the facts: the raw page (read this iteration) is an undated download list (items dated 2016/06/23, 2017/07/24, 2018/07/09; newest v5.2.3 of 2018-07-09), so 2026-11-13 is the reading date, not a publication date. The statement it supports (''list EVO packages only up to 5.2.3 of 2018'') is accurate. Agree this is advisory and may be left.'
- code: F11
  category: editorial-advisory
  section: wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens / body and sectors
  item: WFX Phantom
  url_or_quote: 'BleepingComputer: "Some of the compromised accounts belonged to Fortune 100 organizations, the US General Services Administration, the French government, Nextcloud, and WebdriverIO."'
  summary: '(low confidence) BleepingComputer, which the entry cites, reports government accounts among the compromised ones; the entry carries ''sectors: technology'' and says only that no Swiss victim is named. For a public-sector constituency that line is the relevance hook and could be added in one clause with the BleepingComputer citation. The sentence is BleepingComputer''s alone (the Aikido post lists no victims), so it needs attribution to BleepingComputer.'
```
