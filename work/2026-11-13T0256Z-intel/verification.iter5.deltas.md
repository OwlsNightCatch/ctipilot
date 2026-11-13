# Iteration 5 findings and the remediation applied (for the iteration 6 pass)

1. [F3] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws, body paragraph 2 (claim 1447ef6968)
   finding: The iteration-4 fix replaced the clause's citation instead of adding to it. CTX697320 (read this iteration) lists only 'Citrix NetScaler Console 14.1-74.34 and later releases'; the four ADC/Gateway builds in the same clause (14.1-
   remediation_applied: fixed: the four ADC and Gateway builds cite CTX697305 again and the Console build keeps CTX697320

2. [F3] n-able-n-central-33-unpatched-flaws-public-pocs-offline, section Update 2026-11-13T03:54:38Z (claims dc7d379829, ebfbf08
   finding: The clause binds CVE-2026-90436 to the N-central chain, but neither cited page carries that link: the Axis post (read) names the CVE and Axis 1.x but not N-central; Huntback (read, grep for 90436 returns 0) describes the SOAP-faul
   remediation_applied: fixed: BleepingComputer cited beside Huntback at the root-escalation clause in the N-able update section

3. [F3] check-point-php2shell-sk1000302-portal-and-vpn-gateways, section Update 2026-11-13T03:59:06Z (claim a1523fe4f3)
   finding: (low confidence) The closing clause is a statement about sk1000302 cited to the research post, which says nothing about sk1000302 (grep of the post for sk1000302: no hit). The absence is true on sk1000302 itself (full text read: n
   remediation_applied: fixed: the sk1000302 statement cites sk1000302

4. [F18] wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens, actions[0] (claim 71638b0dc1)
   finding: (low confidence) Iteration 4 asked for the search terms in the action. The action now names the PR title but still defers the commit messages to 'the campaign's CI messages' (and omits the wfx-docs branch), so a team working the a
   remediation_applied: fixed: actions[0] now carries the PR title and the five commit titles

5. [F11] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws, title / headline / summary
   finding: (low confidence) Bulletin row CVE-2026-111338 is 'Sensitive authentication material written to a log file' (CWE-532, information disclosure) and CVE-2026-111335 reads 'Improper request handling can lead to a denial-of-service / re
   remediation_applied: fixed: 'memory-safety' dropped from the Citrix title, headline and summary (28 flaws)

6. [F11] cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix, Exposure line
   finding: (low confidence) The 2026-11-13 update adds Windows 10, Windows 11, Server 2019 to 2025, PowerShell 7.4 to 7.6 and Visual Studio 2017 to 2026 as affected (MSRC record revision 7, affectedProduct rows read), and the Defender takeaw
   remediation_applied: declined: advisory; the Defender takeaway already names the Windows cumulative update and the main analysis sits at its word limit

7. [F11] dixell-copeland-xweb-evo-vulncheck-cves-end-of-service, sources[] (Copeland XWEB EVO download page, date 2026-11-13)
   finding: (low confidence, previously declined as advisory in iteration 4) The page is an undated download list (items dated 2016/06/23, 2017/07/24, 2018/07/09); 2026-11-13 is the reading date. Left to the main agent.
   remediation_applied: declined again: advisory; the Copeland list is the only source for the end-of-support state and the inline citation format requires a date
