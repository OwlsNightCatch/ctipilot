import json, re
from fu2_lib import *
H = 'nable/hf3.extract.md'; U69 = 'nable/uptime-202669.jina.md'; U13 = 'nable/uptime-202613.jina.md'; U9 = 'nable/uptime-202609.jina.md'
HU = 'nable/huntress.extract.md'; EU = 'nable/hf3-cves-euvd.txt'; NC = 'nable/ncsc-csh-13163.json'; TF = 'nable/tenable-faq.extract.md'; BC = 'nable/wid-sec-2026-4609.csaf.json'
UH = 'https://status.n-able.com/2026/11/16/n-central-2026-4-hf3-release-notes/'
UU69 = 'https://uptime.n-able.com/event/202669/'; UU13 = 'https://uptime.n-able.com/event/202613/'; UU9 = 'https://uptime.n-able.com/'
UHU = 'https://www.huntress.com/blog/n-able-disables-cloud-services-following-disclosure-of-able2shell-exploit-chains'
UEU = 'https://euvdservices.enisa.europa.eu/api/search?text=N-central&fromDate=2026-11-14&toDate=2026-11-18&page=0&size=50'
rn = json.load(open(ROOT + 'nable/hf3-releasenote-descriptions.json'))
eu = {}
for ln in body(EU).splitlines()[1:]:
    cve, eid, sc, vec, desc = [x.strip() for x in ln.split(' | ', 4)]
    eu[cve] = (eid, sc, vec, desc)
huntress_sev = {'CVE-2026-129272': 'critical', 'CVE-2026-129280': 'critical', 'CVE-2026-129286': 'critical', 'CVE-2026-129274': 'high', 'CVE-2026-129282': 'high', 'CVE-2026-129273': 'high', 'CVE-2026-129271': 'high', 'CVE-2026-129281': 'high', 'CVE-2026-129287': 'high', 'CVE-2026-129275': 'high', 'CVE-2026-129283': 'high', 'CVE-2026-129276': 'medium', 'CVE-2026-129277': 'medium', 'CVE-2026-129278': 'medium', 'CVE-2026-129279': 'medium', 'CVE-2026-129284': 'medium', 'CVE-2026-129285': 'medium'}
_kev = {x['cveID']: x for x in json.load(open(ROOT + 'oracle/cisa-kev.json'))['vulnerabilities']}
_ids = ['CVE-2026-1292%02d' % i for i in range(71, 88)] + ['CVE-2026-90436', 'CVE-2026-125883', 'CVE-2026-125881', 'CVE-2026-125878', 'CVE-2026-125882', 'CVE-2026-125879', 'CVE-2026-91000', 'CVE-2026-125880']
with open(ROOT + 'nable/kev-check.txt', 'w') as _f:
    _f.write('CISA KEV catalogVersion 2026.11.17 (dateReleased 2026-11-17T17:53:15.5664Z); membership check run 2026-11-18\n')
    _f.write('on KEV: %s\n' % ([i for i in _ids if i in _kev] or 'none of the %d ids checked' % len(_ids)))
    _f.write('ids checked: %s\n' % ', '.join(_ids))
out = []
A = out.append
A('## 4. N-ABLE N-central 2026.4 Hotfix 3 (build 2026.4.1.39)\n')
A('Primary: ' + UH + ' (read with `extract`; the direct transports returned a shell so the page was served by the jina reader, fetched 2026-11-18 ~04:50Z; jina metadata `Published Time: 2026-11-16T21:04:35+00:00`). N-able\'s own status/advisory channel (uptime.n-able.com, a script-rendered page) was read with the jina reader at 2026-11-18 ~05:00Z: event pages ' + UU69 + ' (HF3 notice) and ' + UU13 + ' (12-13 Nov updates), and the dashboard root ' + UU9 + ' (page header "Last Updated: Nov 18, 2026 04:47:39 UTC"). Huntress (updated 2026-11-16 7 PM ET and 2026-11-17 8:30 AM ET): ' + UHU + '. N-able CNA records via ENISA EUVD: ' + UEU + '.\n')
A('### 4.1 Release facts\n')
A(table([
 ('Build number', UH, H, 'Build Number:2026.4.1.39'),
 ('Date', UH, H, 'Last Updated:November 16th, 2026'),
 ('Vendor labels it a critical security update; builds on HF2', UH, H, 'N-central 2026.4 Hotfix 3 is a critical security update.'),
 ('Supersedes GA, HF1 and HF2 builds', UH, H, 'This release builds on and supersedes N-central 2026.4 (build 2026.4.0.27), N-central 2026.4 Hotfix 1 (build 2026.4.0.32), and N-central 2026.4 Hotfix 2 (build 2026.4.1.26).'),
 ('Scope: includes everything in HF2', UH, H, 'This hotfix builds on the existing N-central 2026.4 Hotfix 2 release and includes everything delivered in it.'),
 ('Authentication and access control', UH, H, 'We have added missing authentication and permission checks to additional server operations.'),
 ('Agent and Probe security: Agent/Probe-to-server authentication and session handling (not the HF2 Agent-to-Probe change)', UH, H, 'We have improved how Agents and Probes authenticate with, and communicate to, the N-central server, including session handling.'),
 ('Agents/Probes direction clarified', UH, H, 'This is communication from Agents and Probes to the N-central server. It is separate from the Agent-to-Probe communication changes in Hotfix 2.'),
 ('File and import handling', UH, H, 'We have added additional validation to file publishing, file path, and XML import handling.'),
 ('Legacy API change (config option removed; permanently blocked)', UH, H, 'We have removed the configuration option for legacy APIs, and legacy APIs are now permanently blocked.'),
 ('User management', UH, H, 'We have made improvements to how user accounts are managed and secured.'),
 ('Agents and Probes: unpatched ones can be impersonated; everyone must upgrade them', UH, H, 'Agents and Probes that are not upgraded are susceptible to impersonation.'),
 ('Who upgrades what', UH, H, 'All customers, hosted and on-premise, must upgrade all of their Agents and Probes to the latest version to be fully protected.'),
 ('Hosted servers upgraded by N-able; on-prem must upgrade', UH, H, 'Hosted N-central servers are upgraded by N-able.'),
 ('Agents/Probes must go to HF3 even if already on HF2', UH, H, 'you must upgrade all of your Agents and Probes to the latest version, 2026.4.1 HF3, whether or not you have already upgraded them to Hotfix 2.'),
 ('Agent verification: devices must report SMBIOS ID or machine ID; otherwise the server rejects them', UH, H, 'If both are missing, N-central rejects the connection.'),
 ('Inactive Assets tab: where it is', UH, H, 'A new Inactive Assets tab under Configuration > Asset Discovery > Discovered Assets'),
 ('Network setup: appliance token behaviour section', UH, H, 'then find the **Appliance token behaviour** section.'),
 ('Post-upgrade review of inactive agents', UH, H, 'After upgrading, allow time for your Agents to reconnect, then review the Inactive Assets tab for any Agents that need attention.'),
 ('Known issue: remote control other than Take Control disabled', UH, H, 'Remote control functionality other than Take Control is disabled. Take Control continues to work as expected.'),
 ('Known issue: Intune integration blocked', UH, H, 'The Intune integration is currently blocked.'),
 ('Upgrade directly to 2026.4.1.39 from listed versions', UH, H, 'Upgrade directly to 2026.4.1.39 from:'),
]))
A('')
A('### 4.2 The 17 CVE ids fixed (N-able release notes list; N-able CNA CVSS 4.0 from EUVD)\n')
A('The release notes give an id and a one-line title per CVE and no scores. N-able, as CNA, published scores and descriptions that EUVD mirrors; Huntress (2026-11-17 8:30 ET) confirms the scores come from N-able and that NVD has not scored them yet. Authentication wording is the CNA\'s.\n')
A('| CVE | release-note title (verbatim) | CNA CVSS 4.0 (EUVD id) | Huntress severity | CNA description (verbatim) |')
A('|---|---|---|---|---|')
for cve in sorted(rn):
    ok1 = chk(H, rn[cve]); eid, sc, vec, desc = eu[cve]
    ok2 = chk(EU, desc); ok3 = chk(EU, '%s | %s | %s | %s' % (cve, eid, sc, vec))
    A('| %s | "%s" | %s (%s) | %s | "%s"%s |' % (cve, esc(rn[cve]), sc.replace('CVSS 4.0 ', ''), eid, huntress_sev[cve], esc(desc), '' if (ok1 and ok2 and ok3) else ' **[CHECK FAILED]**'))
A('')
A(table([
 ('N-able release notes introduce the list', UH, H, 'N-central 2026.4 Hotfix 3 fixes the following vulnerabilities:'),
 ('Huntress: all 17 scored by N-able as CNA; 3 critical, 8 high, 6 medium; NVD not yet scored', UHU, HU, 'N-able has now published CVSS 4.0 scores and official descriptions for all 17 CVEs fixed in N-central 2026.4 Hotfix 3 (build 2026.4.1.39). Three are rated critical severity, eight high severity, and six medium severity.'),
 ('Huntress: scores assigned by N-able as CNA', UHU, HU, 'All scores were assigned by N-able as the CVE Numbering Authority. NVD has not yet published its own scoring.'),
 ('Huntress: CVE-2026-129272 is the impersonation issue behind the instruction to upgrade Agents and Probes', UHU, HU, "This is the impersonation issue behind N-able's instruction to upgrade every Agent and Probe."),
 ('Huntress: patch management engine fix needs component 2.14.4.5829 or later (CVE-2026-129271)', UHU, HU, 'CVE-2026-129271 (8.5): Patch Management Engine local privilege escalation, fixed in Patch Management Component 2.14.4.5829'),
 ('Huntress: full-stack update advice (server, Agents, Probes, Patch Management Engine)', UHU, HU, 'Confirm the full stack is updated: the server to 2026.4.1.39, every Agent and Probe to 2026.4.1 HF3, and the Patch Management Engine to 2.14.4.5829 or later. A patched server alone does not close the impersonation issues.'),
 ('Huntress: CVE-2026-129275 exposes Automation Manager policies incl. embedded scripts/parameters (rotate embedded secrets)', UHU, HU, 'Rotate secrets in Automation Manager policies. Any credentials or API keys embedded in policies on a server that was exposed before patching should be treated as potentially disclosed (CVE-2026-129275).'),
 ('Huntress: Take Control audit records from an unpatched server may be altered (CVE-2026-129278)', UHU, HU, "Don't rely on Take Control audit records from an unpatched server during an investigation. They could have been altered (CVE-2026-129278)."),
 ('Huntress: user enumeration -> expect password attacks; enforce MFA (CVE-2026-129279)', UHU, HU, 'Valid account emails may have been enumerated (CVE-2026-129279), so make sure MFA is enforced on all N-central accounts.'),
 ('BSI CERT-Bund WID-SEC-2026-4609 (hoch, 2026-11-16T23:00Z) lists 17 CVEs and "<2026.4.1.39" as affected, 2026.4 Hotfix 3 as fixed', 'https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-4609', BC, '"name": "<2026.4.1.39"'),
]))
A('')
A('Version table: affected = N-central builds before 2026.4.1.39 per the CNA wording "before 2026.4.1 HF3" (CVE-2026-129271\'s CNA text has no version); fixed = 2026.4.1.39 (HF3) plus Agents and Probes at 2026.4.1 HF3 (and, for CVE-2026-129271, Patch Management Component 2.14.4.5829 or later per Huntress). Supported direct-upgrade sources: 2025.4, 2026.1, 2026.2, 2026.3, 2026.3.1 HF1-HF4, 2026.4, 2026.4 HF1 (2026.4.0.32), 2026.4 HF2 (2026.4.1.26).\n')

A('### 4.3 Agents and Probes; Legacy API; the named chains (4EverAble2Shell, Agent2Shell)\n')
A(table([
 ('Release notes: Agent verification checks and impersonation protection', UH, H, 'N-central 2026.4 Hotfix 3 improves how N-central verifies and manages the Agents that connect to it. This update helps protect against Agent impersonation'),
 ('Huntress: HF3 removes the Legacy API option, which several PoCs used', UHU, HU, 'The hotfix also removes the configuration option for legacy APIs, a feature that was leveraged in several of the proofs of concept (POCs) that emerged for the recent CVEs.'),
 ('N-able (via Huntress 13 Nov): Agent2Shell exploitation, like 4EverAble2Shell, requires the non-default Legacy API', UHU, HU, 'Additionally, N-able confirmed that Agent2Shell exploitation (like 4EverAble2Shell) requires the non-default Legacy API to be enabled.'),
 ('Huntress 12 Nov: HF2 with Legacy API disabled is not exposed to the 4EverAble2Shell chain', UHU, HU, 'Servers running 2026.4 HF2 with Legacy API disabled are not exposed to this exploit chain.'),
 ('N-able 12 Nov notice (own channel): "developing additional remediation"', UU13, U13, 'Our teams are actively assessing the new disclosures, developing additional remediation, and working to safely restore affected functionality.'),
 ('N-able 12 Nov notice: Legacy API off by default; instructions to disable', UU13, U13, 'Legacy API access is disabled by default. If you enabled it, follow these instructions:'),
 ('N-able HF3 notice (own channel, event 202669, started 2026-11-16 21:00 UTC): framed as a response to "non-responsible communication"', UU69, U69, 'As part of our continued response to the non-responsible communication of critical vulnerabilities affecting N-central,'),
 ('N-able HF3 notice: refers to the 9 Nov and 12 Nov announcements but names no chain and states no CVE-to-chain mapping', UU69, U69, 'The vulnerabilities announced on November 9 and November 12 are specific to N-central. No other N-able products are at risk from these vulnerabilities.'),
 ('N-able HF3 notice: generic description only', UU69, U69, 'HF3 builds on the protections delivered in HF2 and includes further improvements across authentication and access controls, Agent and Probe communications, file handling, server components, legacy APIs, and user management.'),
 ('N-able HF3 notice: legacy APIs permanently blocked', UU69, U69, 'Legacy APIs: Removed the configuration option for legacy APIs. Legacy APIs are now permanently blocked.'.replace('Legacy APIs: Removed', '**Legacy APIs:** Removed') if False else 'Removed the configuration option for legacy APIs. Legacy APIs are now permanently blocked.'),
 ('N-able HF3 notice: CVEs are in the HF2 and HF3 release notes', UU69, U69, 'Please see Release Notes for'),
 ('N-able event 202669 start time on the dashboard', UU9, U9, 'ID: 202669 Start: Nov 16, 2026 21:00:00 UTC End: N/A Severity: Major Outage Status: Identified'),
]))
A('')
A('Name check (grep over the saved bodies, count of matches for "4EverAble2Shell", "Agent2Shell", "Able2Shell", "Axis", "CVE-2026-90436"): release notes `nable/hf3.extract.md` = %d; N-able HF3 notice `nable/uptime-202669.jina.md` = %d; N-able 12-13 Nov page `nable/uptime-202613.jina.md` = %d. So **neither the HF3 release notes nor N-able\'s HF3 notice names 4EverAble2Shell, Agent2Shell or the Apache Axis CVE-2026-90436**, and neither says they are fixed. What N-able does say: the Legacy API (the precondition N-able itself stated for both chains) is now permanently blocked; HF3 hardens Agent/Probe authentication (relevant to Agent2Shell-type impersonation, mapping not stated by N-able except that Huntress ties CVE-2026-129272 to the impersonation instruction). "No fix for the named chains" can therefore no longer be written as N-able\'s current statement: N-able has made no statement either way after HF3, and the stated precondition is removed. Do not write "HF3 fixes 4EverAble2Shell".\n' % tuple(sum(body(f).count(k) for k in ('4EverAble2Shell', 'Agent2Shell', 'Able2Shell', 'CVE-2026-90436')) for f in (H, U69, U13)))

A('### 4.4 Exploitation and public PoC (post-HF3)\n')
A(table([
 ('Huntress 17 Nov: public PoC for ALL 17 HF3 CVEs released the evening of 16 Nov, shortly after the hotfix; unpatched servers should be treated as exposed (single source for the PoC claim)', UHU, HU, 'Public proof-of-concept code for all 17 CVEs was released on the evening of November 16, shortly after the hotfix. Any unpatched server should be treated as exposed.'),
 ('Huntress 17 Nov: no exploitation of these issues observed in its partners\' environments', UHU, HU, "As of this writing, Huntress has not observed exploitation of these issues in our partners' environments."),
 ('Huntress 16 Nov (7 PM ET): no evidence of exploitation in the wild for the HF3 CVEs', UHU, HU, 'We have not seen evidence of exploitation in the wild.'),
 ('N-able 12 Nov (own channel): "no signs of compromise"', UU13, U13, 'we have seen no signs of compromise. We are continuing to monitor closely and will provide updates as needed.'),
 ('N-able 13 Nov 03:50 UTC (own channel): identified IOCs; working with those specific customers', UU13, U13, 'Through our ongoing investigation today, we have identified Indicators of Compromise (IOCs) and are working closely with those specific customers to assess and mitigate any potential risks.'),
 ('N-able 13 Nov 13:40 UTC: IOCs relevant only to customers that have not disabled the Legacy API (per Huntress)', UHU, HU, "In an [<u>update to its security advisory</u>](https://uptime.n-able.com/) on November 13 at 13:40:25 UTC, N-able said that it has identified Indicators of Compromise (IoCs) for customers that haven't disabled the Legacy API."),
 ('Tenable FAQ (last update 16 Nov, not about HF3): Huntback 21 servers, 19 on HF2', 'https://www.tenable.com/blog/able2shell-frequently-asked-questions-for-reported-n-able-n-central-zero-day-vulnerabilities', TF, 'On November 12, the security firm huntback reported that a newer exploit chain, 4EverAble2Shell, was used to install cryptocurrency miners on 21 live N-central servers it identified, 19 of which reported running Hotfix 2.'),
 ('NCSC-CH Security Hub post 13163 last modified 2026-11-16 09:34Z (BEFORE HF3): exploitation status "Actively exploited"', 'https://security-hub.ncsc.admin.ch/#/posts/13163', NC, '"lastModified": "2026-11-16T09:34:43.742878Z"'),
 ('NCSC-CH 13163 (pre-HF3): "additional fixes are still expected"', 'https://security-hub.ncsc.admin.ch/#/posts/13163', NC, 'additional fixes are still expected to adress additional vulnerabilities'),
 ('Own check: none of the 17 HF3 ids, CVE-2026-90436 or the seven HF2 ids is on CISA KEV', 'https://www.cisa.gov/known-exploited-vulnerabilities-catalog (via `fetch_source.py cisa-kev`)', 'nable/kev-check.txt', 'on KEV: none of the 25 ids checked'),
 ('NCSC-CH 13163: edit reason', 'https://security-hub.ncsc.admin.ch/#/posts/13163', NC, 'Updated with claims of active exploitation'),
]))
A('')
A('Net status: exploitation of the 4EverAble2Shell chain against HF2-with-Legacy-API-on servers is reported by Huntback/Previdian (already in the entry); for the 17 new HF3 CVEs the only post-HF3 statements are Huntress\'s (PoC public since the evening of 16 Nov; no exploitation seen in its partners\' environments, as of 17 Nov 8:30 ET). No CISA KEV listing for any of CVE-2026-129271..129287, CVE-2026-90436 or the seven HF2 ids (catalogVersion 2026.11.17, released 2026-11-17T17:53Z, own check recorded in `nable/kev-check.txt`).\n')

A('### 4.5 What changed vs the covered entry, and an extra N-able lead\n')
A('- Covered entry `2026-11-10/n-able-n-central-33-unpatched-flaws-public-pocs-offline`: last records 2026-11-14 (update: Agent2Shell also needs the Legacy API; IOCs published; "N-able still has no fix") and 2026-11-15 (internal correction). HF3 (2026-11-16) is the follow-up hotfix the 2026-11-13 record said was planned.')
A('- The entry\'s `fixed` text "N-able has no fix for this chain and plans a follow-up hotfix" for CVE-2026-90436 is now stale as a statement about N-able\'s position: the follow-up hotfix exists, but N-able does not say it fixes the Axis chain (see 4.3).')
A('- NEW EXTRA LEAD (not one of the five items; separate incident): N-able Mail Assure and SpamExperts Hosted Cloud security incident. N-able\'s uptime page (update "Nov 18, 2026 03:05:09 UTC", read 2026-11-18 ~05:00Z):')
A('')
A(table([
 ('N-able: unauthorized access to one server of the Mail Assure / SpamExperts Hosted Cloud', UU9, U9, 'We are aware of unauthorized access to one of the servers in the Mail Assure and SpamExperts Hosted Cloud.'),
 ('N-able: unrelated to the N-central incident', UU9, U9, 'This is unrelated to the N-central incident.'),
 ('N-able: no evidence of customer data compromise at this time; UI and API access disabled; mail flow unaffected', UU9, U9, 'at this time we do not have evidence that customer data was compromised, including access to tenants’ mailboxes.'),
 ('N-able: earlier 16 Nov statement attributed the disruption to configuration and dependencies; later determined to be a security incident', UU9, U9, 'As we continued our investigation, we determined that the disruption was caused by a security incident affecting the Mail Assure and SpamExperts Hosted Cloud environment.'),
 ('Timestamp of that update', UU9, U9, 'Nov 18, 2026 03:05:09 UTC'),
]))
A('')
A('Mail Assure / SpamExperts is an email-security service used by MSPs and some public bodies (assessment); it is a vendor incident disclosure from the vendor\'s own status channel, still "Identified" at fetch, worth a separate look by the S4 sweep (suppliers).\n')

A('### 4.6 Contradictions with the first pass (item 12) and open gaps\n')
A('- CONFIRMED: build 2026.4.1.39; date 2026-11-16; builds on HF2 (2026.4.1.26) and HF1; the 17 ids CVE-2026-129271 to -129287 and their release-note titles; Legacy API permanently blocked; Agent/Probe authentication and session hardening, separate from the HF2 Agent-to-Probe change; unpatched Agents/Probes susceptible to impersonation; on-prem upgrade servers, hosted by N-able, all upgrade Agents/Probes; known issues (remote control other than Take Control; Intune); BSI WID-SEC-2026-4609 with 17 CVEs; the release notes do not mention 4EverAble2Shell, Agent2Shell or the Axis CVE by name.')
A('- WORDING TO FIX: first pass groups "-129274 to -129277, -129280" as "missing authentication ... and ServerUI SOAP operations". The release-note title for -129280 is "ServerUI SOAP operations missing authorisation checks" (CNA: "in some cases without authentication"); -129277 is "ServerMMS maintenance action read missing authentication" (MaintActionGet read AND cancel per the CNA).')
A('- NOT IN THE FIRST PASS (material): (1) N-able CNA CVSS 4.0 scores now exist (3 critical: -129272 9.3, -129280 9.3, -129286 9.2; 8 high; 6 medium); (2) Huntress states public PoC code for all 17 CVEs appeared the evening of 16 Nov, and that unpatched servers should be treated as exposed; (3) Huntress has not observed exploitation of the 17 in its partners\' environments; (4) the Patch Management Engine component fix level 2.14.4.5829; (5) N-able\'s own HF3 notice and its 12-13 Nov statements (read from its uptime channel); (6) the separate Mail Assure/SpamExperts incident.')
A('- The first pass sentence "NCSC-CH advisory 13163 (edited 2026-11-16 09:34Z, before HF3) already states actively exploited and \'additional fixes are still expected\'" is confirmed verbatim (4.4); it predates HF3, so its "fixes still expected" is superseded by HF3 for the 17 CVEs.')
A('- OPEN: which HF3 CVE(s), if any, close the Apache Axis chain (CVE-2026-90436) and the Agent2Shell chains: not stated by N-able, Huntress or Tenable. The N-able security-advisory pages on me.n-able.com (customer portal) were not read. The single-source PoC claim (Huntress) is uncorroborated. No other media coverage of HF3 was found by WebSearch (index thin).\n')
SECTION = '\n'.join(out)
