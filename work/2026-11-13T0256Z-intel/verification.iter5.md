**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-11-13T05:58:54Z · ended_at=2026-11-13T06:21:36Z · duration_seconds=1362

## Verification report — 2026-11-13T0256Z-intel (iteration 5)

Scope: post-fix pass. 307 of 389 ledger claims answered with a verdict row (`verification.iter5.claims.yaml`): all 25 claims of `claims.changed.iter5.yaml`, every claim of the ten entries remediated in iteration 4 (Citrix, Check Point, Confluence, N-able, Dixell, WFX Phantom, DarkLunnen, Trend Micro PHP2Shell, Apache httpd, Brotli/Desigo: 279 claims in all), and a random 28 of the other 110 claims (ANSSI, .NET OOB, ScreenConnect, Windchill, SignDrop, Huntress; seeded draw). Every cited page was re-fetched this iteration (the live Citrix bulletin included); the first ANSSI REACTIV PDF has no text layer and was read as rendered pages; the CISA alert was read through WebFetch. No claim is `unreadable`.

### Iteration 4 deltas walked
1. Citrix sourcing note / cves (F3): bulletin read live; history table is 'Initial Publication' plus '2026-11-12 | Fixed a typo in CVE numbers CVE-2026-111333 ... CVE-2026-111339'. The CVE List returns 404 for CVE-2026-111333 to 111339 and 120860 to 120867 and a record for 120868, as the sourcing note says. Remediation correct.
2. Citrix cves[] (F8): 29 records; every id and CVSS 4.0 score matches its bulletin row (28 rows plus the Console row 9.4/adjacent; CVE record 9.3 network confirmed on cveawg and ENISA). Nine rows score 9.0 or above, ten carry C/I/A High, as the summary and CERT-EU state. Remediation correct.
3. Citrix Console build citation (F3): the new citation introduces a defect (finding #1 below).
4. Citrix takeaway (F3): CERT-EU carries the no-feature and Gateway/AAA-first points; neither bulletin contains the words workaround or mitigation. Correct.
5./6. Check Point Exposure and takeaway (F3): Exposure now splits sk1000302 (six features, listed releases) from sk1000362 (Force/management/log/Multi-Domain/Maestro, R81 to R82.20); the takeaway cites both sk pages. Correct.
7. sk1000362 label: page data dateCreated 2026-11-08, lastModified 2026-11-12; label 'modified 2026-11-12'. Correct.
8. BleepingComputer at the CVE link: present in the Confluence body and section and in the N-able body; absent from the N-able Update section's CVE clause (finding #2).
9. Dixell summary: 'French and Swiss authorities' matches CERT-FR ALE-012 and NCSC post 13054 / BACS. Correct.
10. WFX actions[0] (F18): PR title now in place, commit messages still deferred (finding #4, low confidence).
11. DarkLunnen stray comma: gone.
12. WFX 'designed to outlast rotation': matches StepSecurity ('designed to outlast credential rotation') and Aikido (same wording). Correct.
13. Record summaries: no field narration; Cisco v1.12 / ISE not impacted is in the Brotli section and matches the live advisory (version 1.12, 2026-NOV-12, ISE 'Not impacted'). Correct.
14. Dixell source date: declined by the main agent, still advisory (finding #7).
15. Check Point 'targeted': matches the research post.

### Citation does not support the claim (F3)
- #1 citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws, body paragraph 2: "The fixed builds are 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 for 13.1-FIPS and 13.1-NDcPP, and 14.1-74.34 for the Console ([Cloud Software Group](...CTX697320...))". CTX697320 lists only 'Citrix NetScaler Console 14.1-74.34 and later releases'; the four ADC/Gateway builds are on CTX697305. The iteration-4 fix replaced the citation instead of adding CTX697320 beside CTX697305. Fix: cite CTX697305 for the ADC/Gateway builds, CTX697320 for the Console build.
- #2 n-able-n-central-33-unpatched-flaws-public-pocs-offline, section 'Update — 2026-11-13T03:54:38Z': "It pairs CVE-2026-90436 in the Apache Axis 1.x SOAP engine ([Apache Axis project]) with a separate root escalation ([Huntback])." Axis post names the CVE and Axis 1.x, not N-central; Huntback names no CVE id (0 hits for 90436). BleepingComputer ('The attack combines an Apache Axis vulnerability, tracked as CVE-2026-90436, with a separate N-central privilege escalation weakness') is cited at this link in the body but not in the section. Fix: add BleepingComputer at the clause.
- #3 (low confidence) check-point-php2shell-sk1000302-portal-and-vpn-gateways, section 'Update — 2026-11-13T03:59:06Z': "...; sk1000302 itself still carries no exploitation statement ([Check Point Research])". The research post says nothing about sk1000302; the absence is true on sk1000302 (read in full) and should cite it.

### Action-item discipline (F18)
- #4 (low confidence) wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens actions[0]: names the PR title but defers 'commits whose messages match the campaign's CI messages' (and the wfx-docs branch) to the Detection line; StepSecurity lists 'ci: refresh build cache', 'chore: add ci helper', 'chore: add dependency audit workflow'. Name them or drop the clause.

### Editorial / less-is-more flags (advisory, F11)
- #5 (low confidence) citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws title, headline and summary: '28 memory-safety flaws' with DoS-only impact; bulletin row CVE-2026-111338 is 'Sensitive authentication material written to a log file' (CWE-532) and CVE-2026-111335 'Improper request handling can lead to a denial-of-service / reboot-loop condition'. The body ('memory-safety and input-handling flaws') covers it; optional wording fix upstream of the body.
- #6 (low confidence) cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix Exposure line: describes only .NET runtime and Brotli code paths, while the new section, cves[] and the takeaway add Windows 10/11/Server 2019 to 2025, PowerShell and Visual Studio (MSRC revision 7, affectedProduct rows read).
- #7 (low confidence, previously declined) dixell-copeland-xweb-evo-vulncheck-cves-end-of-service sources[] Copeland download page dated 2026-11-13: undated list (items 2016, 2017, 2018).

### Checked and clean
All other claims in scope returned `ok` against pages read this iteration: Trend Micro advisory table of 2026-11-12 (CP B7351, CP B20113, DDAN Nov. 18, MSE Nov. 17), the two readmes, Quest KB 4385046, NetApp advisory data (rev 12.0) and KB article, Trend Download Center pages (no 2026-11 patch for DDAN, MSE); Apache httpd 2.4.71 advisory, Red Hat, Wiz, Debian, Ubuntu USN-9090-1, Alpine, SUSE, Wordfence, researcher repository, RHSA-2026:98981/98978; Confluence/Atlassian advisory, Axis oss-security post, BSI CSAF 'hoch', BleepingComputer, Huntback, Previdian; N-able release notes, Huntress, Tenable, THN; VulnCheck CNA records (14 CVEs published 2026-11-12, the seven at CVSS 4.0 9.2 to 9.3 match the cves[] ranges), Copeland bulletin and download pages, Dixell France guide, CERT-FR, NCSC post 13054, BACS, Ransom-ISAC; StepSecurity, Aikido, Endor Labs, BleepingComputer (WFX); Group-IB and Fortinet FG-IR-24-535; Siemens CSAF (SSA-045512/443410/242944/678870), Mitel MISA-2026-0010 rev 5.0, Cisco advisory v1.12, ten Apple security notes, CISA alert and KEV catalog; Check Point sk1000302/sk1000362 (page data) and the research post; MSRC record revision 7 and its affected-product rows (KB list verified); ANSSI first report pages 3, 4, 6, 7 (read as rendered pages) and the second report; ConnectWise CNA record, The Record, Huntress/BleepingComputer on ScreenConnect; PTC trust center, NCSC 13174, BSI CSAF, CVE record (9.2 / 3.1 9.0); Cyderes, BleepingComputer, SecurityOnline on SignDrop; Huntress Teams booking post.
No state-file, silent-edit, immutable-field, em dash or workflow-vocabulary defects found. Run-record notes checked against files (nine updated ids, seven entries, 29 Citrix records, Citrix revision note, dispositions of the 2026-11-09/10 KEV additions).

### Missed angles
Coverage looks complete. The KEV additions of 2026-11-09/10 that no entry carries (Cisco BroadWorks CVE-2026-20320, GPUStack CVE-2026-102895, Openwave Webtop CVE-2026-111793) are explicitly dispositioned as borderline drops in the 2026-11-11 and 2026-11-12 run records.

### Verdict
NEEDS_FIXES (truth: 3, editorial: 1, advisory: 3)

### Findings summary (machine-readable)
```yaml
- code: F3
  category: claim-not-supported
  section: citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws, body paragraph 2 (claim 1447ef6968)
  item: "Citrix NetScaler ADC and Gateway: 28 memory-safety flaws fixed on 2026-11-12"
  url_or_quote: "The fixed builds are 14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS and 13.1-37.293 for 13.1-FIPS and 13.1-NDcPP, and 14.1-74.34 for the Console ([Cloud Software Group, 2026-11-12](https://support.citrix.com/external/article/CTX697320/citrix-netscaler-console-security-bullet.html))"
  summary: "The iteration-4 fix replaced the clause's citation instead of adding to it. CTX697320 (read this iteration) lists only 'Citrix NetScaler Console 14.1-74.34 and later releases'; the four ADC/Gateway builds in the same clause (14.1-73.57, 13.1-64.39, 14.1-73.58 FIPS, 13.1-37.293 for 13.1-FIPS and 13.1-NDcPP) are on CTX697305 ('Citrix NetScaler ADC and Citrix NetScaler Gateway 14.1-73.57 and later releases' and the three following rows). Cite CTX697305 for the ADC/Gateway builds and CTX697320 for the Console build."
- code: F3
  category: claim-not-supported
  section: n-able-n-central-33-unpatched-flaws-public-pocs-offline, section Update 2026-11-13T03:54:38Z (claims dc7d379829, ebfbf08666)
  item: "N-able N-central: 4EverAble2Shell chain works on Hotfix 2 and is exploited on 21+ production servers"
  url_or_quote: "It pairs CVE-2026-90436 in the Apache Axis 1.x SOAP engine ([Apache Axis project, 2026-11-06](https://openwall.com/lists/oss-security/2026/11/06/12)) with a separate root escalation ([Huntback, 2026-11-12](https://huntback.io/blog/ncentral-4everable2shell-miners-on-live-servers))."
  summary: "The clause binds CVE-2026-90436 to the N-central chain, but neither cited page carries that link: the Axis post (read) names the CVE and Axis 1.x but not N-central; Huntback (read, grep for 90436 returns 0) describes the SOAP-fault class instantiation and the root escalation without naming any CVE id. BleepingComputer states it ('The attack combines an Apache Axis vulnerability, tracked as CVE-2026-90436, with a separate N-central privilege escalation weakness to gain root-level access.'), and iteration 4 added it at the CVE link in the main body, but the section's CVE clause still lacks it (BleepingComputer is cited only for 'relays both' two sentences later). Add BleepingComputer at this clause."
- code: F3
  category: claim-not-supported
  section: check-point-php2shell-sk1000302-portal-and-vpn-gateways, section Update 2026-11-13T03:59:06Z (claim a1523fe4f3)
  item: "Check Point gateways exploited (PHP2Shell, root escalation)"
  url_or_quote: "...and in the first wave moved by SSH from the gateway to a VMware ESXi host and deleted files there; sk1000302 itself still carries no exploitation statement ([Check Point Research, 2026-11-12](https://research.checkpoint.com/2026/php2shell-exploitation-on-check-point-gateway/))."
  summary: "(low confidence) The closing clause is a statement about sk1000302 cited to the research post, which says nothing about sk1000302 (grep of the post for sk1000302: no hit). The absence is true on sk1000302 itself (full text read: no exploitation statement), so the citation for that clause should be sk1000302."
- code: F18
  category: action-item-discipline
  section: wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens, actions[0] (claim 71638b0dc1)
  item: "WFX Phantom: stolen GitHub tokens push a CI secret stealer"
  url_or_quote: "search for pull requests titled \"docs: dependency audit notes\" and for commits whose messages match the campaign's CI messages"
  summary: "(low confidence) Iteration 4 asked for the search terms in the action. The action now names the PR title but still defers the commit messages to 'the campaign's CI messages' (and omits the wfx-docs branch), so a team working the aggregated Action Items must re-read the Detection line to execute it (check 10b c). StepSecurity lists the strings: 'ci: refresh build cache', 'chore: add ci helper', 'chore: add dependency audit workflow'. Name them or drop the commit-message clause."
- code: F11
  category: editorial-advisory
  section: citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws, title / headline / summary
  item: "28 memory-safety flaws; the bulletins describe the impact as unpredictable behaviour or denial of service"
  url_or_quote: "Cloud Software Group's bulletin CTX697305 of 2026-11-12 fixes 28 memory-safety flaws ... the bulletins describe the impact as unpredictable behaviour or denial of service"
  summary: "(low confidence) Bulletin row CVE-2026-111338 is 'Sensitive authentication material written to a log file' (CWE-532, information disclosure) and CVE-2026-111335 reads 'Improper request handling can lead to a denial-of-service / reboot-loop condition'; the body says 'memory-safety and input-handling flaws' and covers the log row, but title, headline and summary generalise to 28 memory-safety flaws with DoS-only impact (CERT-EU and heise use the same shorthand). Optional wording fix."
- code: F11
  category: editorial-advisory
  section: cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix, Exposure line
  item: "Microsoft .NET OOB release; Windows cumulative updates now listed"
  url_or_quote: "**Exposure:** a framework-dependent host shows its runtime with `dotnet --list-runtimes`, which must list 8.0.33, 9.0.22 or 10.0.14; ..."
  summary: "(low confidence) The 2026-11-13 update adds Windows 10, Windows 11, Server 2019 to 2025, PowerShell 7.4 to 7.6 and Visual Studio 2017 to 2026 as affected (MSRC record revision 7, affectedProduct rows read), and the Defender takeaway and action carry the Windows update, but the Exposure line still describes only the .NET runtime and Brotli code paths. Optional: add one clause on which Windows builds are in scope."
- code: F11
  category: editorial-advisory
  section: dixell-copeland-xweb-evo-vulncheck-cves-end-of-service, sources[] (Copeland XWEB EVO download page, date 2026-11-13)
  item: "Copeland (XWEB EVO download page)"
  url_or_quote: "https://webapps.copeland.com/Dixell/Pages/XWEB300D_500D_500_EVO"
  summary: "(low confidence, previously declined as advisory in iteration 4) The page is an undated download list (items dated 2016/06/23, 2017/07/24, 2018/07/09); 2026-11-13 is the reading date. Left to the main agent."
```
