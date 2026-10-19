**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:32Z · ended_at=2026-10-18T13:53:30Z · duration_seconds=1558

## Retrospective truth pass T8a, run 2026-10-18T1307Z-audit

11 entries checked whole, 363 of 363 ledger claims given a verdict (`truth-T8a.claims.yaml`). Clean: waterplum-contagious-interview-joint-advisory-scale, plugin4shell-ai-coding-agent-sha-pinning-bypass. Entries with defects follow; defects marked (low confidence) are weak.

### Named lead: cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat, three kernel.org ChangeLog clauses

Decision: the fixed-version claims are SUPPORTED; the citation is imprecise. The kernel CNA records (`https://cveawg.mitre.org/api/cve/CVE-2025-39682`, `...CVE-2025-39964`, `...CVE-2026-53266`, assigner Linux; OSV carries the same records via `https://api.osv.dev/v1/vulns/<id>`) list exactly the entry's fixed stable versions per id: CVE-2025-39682 6.1.149, 6.6.103, 6.12.44, 6.16.4; CVE-2025-39964 5.10.245, 5.15.194, 6.1.154, 6.6.108, 6.12.49, 6.16.9; CVE-2026-53266 5.10.259, 5.15.210, 6.1.176, 6.6.143, 6.12.94, 6.18.36, 7.0.13. All 17 cited ChangeLogs carry the matching commit title ('tls: fix handling of zero-length records on the rx_list'; 'crypto: af_alg - Disallow concurrent writes in af_alg_sendmsg'; 'netfilter: bridge: make ebt_snat ARP rewrite writable') and the release dates the entry gives. The ChangeLogs contain no 'CVE-' string for these ids, so the id-to-fix binding is on the uncited CNA record. One imprecision finding records this.

### Prior-loop remediations (verification.iter8 of 2026-09-30T0639Z-audit), all held

- cisa-kev (F9, THN framing): the Correction now states THN calls the update 'acknowledge active exploitation', which the quoted wording does not say; THN text confirms. Held.
- conference-phishing (F4, summary): summary now reads 'a local proxy can answer ... with fabricated results', matching Huntress ('Lookups can be blocked outright or answered with fabricated results'). Held.
- nighteagle (F4, CVE-2019-0708 affected): now Windows 7 SP1, Server 2008 SP2, Server 2008 R2 SP1; MSRC CVRF 2019-May Known Affected lists exactly these (all architectures). Held.
- plugin4shell (F3, hosts sentence): AIR cited only for consumer Gemini CLI not being fixed; THN cited for 'not established that installing a Gemini CLI plugin from GitHub avoids the flaw'. Both verbatim-supported. Held.

### 2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat (imprecision)

- **imprecision** at `cves[CVE-2026-53266].affected`
  - Claim: ≤ 6.18.35; branch-dependent, see body
  - Defect: The affected range stops at 6.18.35 although the kernel CNA record lists the 7.0 series as affected until 7.0.13 (the 2026-09-30 correction added 7.0.13 to fixed but not the affected bound), so a 7.0.0 to 7.0.12 host reads as outside the range.
  - Ground truth: Kernel CNA record for CVE-2026-53266: versions 5.10 'affected' (defaultStatus affected), '7.0.13 lessThanOrEqual 7.0.* unaffected', '7.1 original_commit_for_fix unaffected', i.e. 7.0.0-7.0.12 affected. (https://cveawg.mitre.org/api/cve/CVE-2026-53266)
  - Fix: Set affected to '5.10 to 6.18.35 and 7.0.0 to 7.0.12; branch-dependent, see body'.
- **imprecision** at `body paragraph 1, 'Fixed stable kernels, each confirmed in kernel.org's release ChangeLog: CVE-2025-39682 in ... ; CVE-2025-39964 in ... ; CVE-2026-53266 in ...' (three clauses, 17 ChangeLog links)`
  - Claim: Fixed stable kernels, each confirmed in kernel.org's release ChangeLog
  - Defect: Fixed versions are all correct, but the cited ChangeLogs never name the CVE ids; they carry only the fix commit titles, so the id-to-fix binding is not on the cited page. It rests on the kernel CNA record, which is not cited.
  - Ground truth: Each of the 17 ChangeLogs carries the matching commit title ('tls: fix handling of zero-length records on the rx_list' in 6.1.149/6.6.103/6.12.44/6.16.4; 'crypto: af_alg - Disallow concurrent writes in af_alg_sendmsg' in 5.10.245/5.15.194/6.1.154/6.6.108/6.12.49/6.16.9; 'netfilter: bridge: make ebt_snat ARP rewrite writable' in 5.10.259/5.15.210/6.1.176/6.6.143/6.12.94/6.18.36/7.0.13) with release dates 2025-08-28, 2025-09-25, 2025-10-02 and 2026-06-19 as listed. The kernel CNA records (assigner Linux) list exactly those fixed versions per CVE; the ChangeLogs contain no 'CVE-' string for these ids. (https://cveawg.mitre.org/api/cve/CVE-2025-39682 (same for CVE-2025-39964 and CVE-2026-53266; api.osv.dev/v1/vulns/CVE-2025-39682 also carries the record))
  - Fix: Say the ChangeLogs carry the fix commits and cite OSV (or the stable commit pages the CVE record references) as the page that names each id, or soften 'confirmed' to 'the fix commits appear in'.
- **imprecision** at `sources[] dates and inline labels for the three Red Hat pages`
  - Claim: [Red Hat Product Security, 2026-09-19](https://access.redhat.com/security/cve/cve-2025-39682) (and the -39964 and -53266 pages)
  - Defect: (low confidence) The label dates the three Red Hat pages 2026-09-19, but that is only the date of the exploit-flag update THN reports; the advisories' own public dates are 2025-09-05, 2025-10-13 and 2026-06-01, so a reader can take the label as the advisory's publication date. The statement the labels support (public exploits exist) is carried by each page's exploit flag, which the plain-text extract does not show.
  - Ground truth: Red Hat security data API: public_date 2025-09-05T00:00:00Z (CVE-2025-39682), 2025-10-13T00:00:00Z (CVE-2025-39964), 2026-06-01T12:00:00Z (CVE-2026-53266); page data field_cve_exploit_known true on all three, rendering 'This CVE is high risk and there are known public exploits leveraging this vulnerability. Address this vulnerability with high priority.' (https://access.redhat.com/hydra/rest/securitydata/cve/CVE-2025-39682.json)
  - Fix: Label the pages 'updated 2026-09-19' (or give the public dates) and state that the exploit statement is the page's known-exploit banner.

### 2026-09-19/cve-2026-81642-cve-2026-82717-unbound-dnssec-rce (factual-error)

- **factual-error** at `## Correction — 2026-09-30T07:19:40Z, last sentence; updates[0].summary; cves[CVE-2026-82717].cvss`
  - Claim: No citable source publishes a CVSS score for CVE-2026-82717, so the 8.4 given for it earlier is withdrawn.
  - Defect: The withdrawal rests on a false premise: NLnet Labs, the CVE's CNA and the vendor that owns the advisory, publishes CVSS 4.0 base score 8.4 (HIGH) in the CVE record and links the same vector from its own security-advisories page, so the original 8.4 was right and cvss: null now omits a published score.
  - Ground truth: CVE record CVE-2026-82717 (assigner NLnet Labs): cvssV4_0 baseScore 8.4, baseSeverity HIGH, vector CVSS:4.0/AV:N/AC:H/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H/E:U. NLnet Labs advisories page: 'CNAME synthesis could lead to heap corruption ... Severity: High' linking the CVSS:4.0 calculator with that vector. (https://cveawg.mitre.org/api/cve/CVE-2026-82717 ; https://nlnetlabs.nl/projects/unbound/security-advisories/)
  - Fix: Restore cvss '8.4 (CVSS4.0, NLnet Labs)' for CVE-2026-82717 (and the title/body mention), and correct the Correction section and record summary to say the 8.4 is NLnet Labs' own score, published on its advisory page, rather than withdrawn for lack of a source.
- **imprecision** at `## Correction — 2026-09-30T07:19:40Z, second sentence`
  - Claim: The CVSS 4.0 score of 9.1 for CVE-2026-81642 is NCSC Switzerland's figure
  - Defect: 9.1 is NLnet Labs' own CVSS 4.0 score (CNA record), which NCSC Switzerland restates; presenting it as NCSC's figure misattributes the origin and is what led to the 8.4 being treated as unsourced.
  - Ground truth: CVE record CVE-2026-81642 (assigner NLnet Labs): cvssV4_0 baseScore 9.1 CRITICAL, vector CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H/E:U/U:Red; NLnet advisories page 'Severity: Critical' links that vector. (https://cveawg.mitre.org/api/cve/CVE-2026-81642)
  - Fix: Attribute the 9.1 to NLnet Labs (cited to its advisory page), with NCSC Switzerland as restating it.
- **imprecision** at `headline`
  - Claim: Unbound's DNSSEC validator can be pointed at attacker-controlled memory by a malicious zone it was only asked to resolve
  - Defect: (low confidence) No source says the validator is pointed at attacker-controlled memory; the advisories describe a digest-buffer heap overflow written with attacker-controlled data.
  - Ground truth: 'A DNSKEY with an owner compression pointer to its own RDATA can overflow the digest buffer. Remote code execution is possible through attacker controlled data.' (https://nlnetlabs.nl/downloads/unbound/CVE-2026-81642.txt)
  - Fix: Reword to the sourced mechanism, e.g. 'a malicious zone Unbound is only asked to resolve can overflow its DNSSEC validator's digest buffer'.

### 2026-09-20/oracle-september-2026-cspu-five-unauthenticated-cvss-10 (imprecision)

- **imprecision** at `## Update — 2026-09-29T04:40:00Z, third paragraph first sentence`
  - Claim: None of the fifty is reported exploited by Oracle or any other source, and none appears in the CISA Known Exploited Vulnerabilities catalog.
  - Defect: True (none of the 50 ids is in the KEV catalogue as of catalogVersion 2026.10.16 and Oracle's matrix carries no exploitation status), but the KEV and 'no source' clause has no citation and the paragraph's only link is the BleepingComputer article on Cl0p.
  - Ground truth: CISA KEV JSON, catalogVersion 2026.10.16: none of the 50 CVE ids listed; Oracle risk matrices have no exploitation column. (https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
  - Fix: Cite the CISA KEV catalogue (and Oracle's advisory) on that sentence.

### 2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft (imprecision)

- **imprecision** at `headline; summary; body paragraph 2 first sentence`
  - Claim: credential theft from a mounted backup image rather than the live domain controller; extracts ntds.dit and SAM not from the live domain controller but from a CIFS-mounted VHDX backup image; rather than dumping credentials from a live, monitored domain controller
  - Defect: (low confidence) The contrast with the live domain controller is the entry's own inference: Talos documents only the extraction from the mounted VHDX backups and says nothing about whether the live DC was also dumped (it also lists Zerologon traces in Phase 4).
  - Ground truth: Talos Phase 6: 'the threat actor mounted a backup share via CIFS at /mnt/Backup and inspected the Windows file system within VHDX backups ... the copying of ntds.dit, SAM, and SYSTEM. The actor then used Impacket's secretsdump.py to extract credentials and password hashes from the collected ntds.dit and SAM files'; no statement that the live DC was not used. (https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/)
  - Fix: Drop the 'rather than / not from the live domain controller' contrast or mark it as the entry's reading ('the history shows credentials taken from a mounted backup image; Talos does not say whether the live DC was also dumped').
- **imprecision** at `body paragraph 1 (nmap/masscan sentence; Zerologon/MS17-010 sentence), paragraph 2 (rclone/Wasabi sentence; AdaptixC2 sentence); summary clause on Wasabi`
  - Claim: then ran nmap and masscan against externally exposed hosts ...; the command history shows attempted exploitation of CVE-2020-1472 (Zerologon) and the MS17-010 vulnerabilities ...; uploaded concurrently ... to Wasabi cloud storage via `rclone`; Command and control ran on the open-source AdaptixC2 post-exploitation framework
  - Defect: Four statements drop Talos's hedge: Talos writes 'appear to have used', 'traces suggesting the exploitation', 'traces indicating that the VHDX files were ... transferred to cloud storage services such as Wasabi' and 'may be using it in real-world attacks'.
  - Ground truth: Talos: 'They appear to have used Masscan and Nmap'; 'We also observed traces suggesting the exploitation of CVE-2020-1472 (Zerologon) and the vulnerabilities associated with MS17-010'; 'We also identified traces indicating that the VHDX files were compressed with zstd and transferred to cloud storage services such as Wasabi using rclone'; 'The Gentlemen may be using it in real-world attacks.' (https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/)
  - Fix: Restore the hedges ('appear to have', 'traces suggesting', 'traces indicating', 'may be using').

### 2026-09-21/nighteagle-apt-q-95-ghostcontainer-devtunnels-rdp2tcp-dcsync (imprecision)

- **imprecision** at `techniques[] (T1027)`
  - Claim: T1027 (Obfuscated Files or Information)
  - Defect: (low confidence) No part of Kaspersky's post describes obfuscated, encoded or packed payloads; the evasion it describes is AMSI/Event Log patching (mapped to T1685) and legitimate-looking archive and file names (mapped to T1036.005).
  - Ground truth: Securelist: the Stub class 'evades detection by the Antimalware Scan Interface (AMSI) and Windows Event Log mechanisms by overwriting addresses in amsi.dll and ntdll.dll'; archives and files 'were disguised to look legitimate' / 'given names mimicking known legitimate software'. No obfuscation or packing is described. (https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/)
  - Fix: Remove T1027 from techniques[] (or cite the page passage that supports it).

### 2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop (imprecision)

- **imprecision** at `summary, last sentence (after the 2026-10-09 update)`
  - Claim: The second-stage backdoor resolves its command-and-control address by reading an operator profile's public "website" field from the Nostr decentralized relay network.
  - Defect: Placed after the sentence on Zscaler's trojanized-provider variants, it reads as universal, but it is SentinelLabs' sample only: Zscaler reports ROOFDECK resolves through a local configuration, then an RSA-signed Pastebin dead drop, with Nostr profile metadata only a fallback that locates the Pastebin URL (the entry's own Update section says the order differs).
  - Ground truth: Zscaler: 'If the Pastebin lookup fails, ROOFDECK can query Nostr profile metadata'; layered design '1. Use the locally stored address. 2. Retrieve a signed and encrypted address from Pastebin. 3. Use Nostr metadata to locate the current dead-drop Pastebin URL.' SentinelLabs: 'When found, it reads the website field of the profile and uses that as its C2 URL.' (https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver)
  - Fix: Reword to 'In the sample SentinelLabs analysed, the second-stage backdoor reads the "website" field of a Nostr operator profile as its C2 URL; Zscaler's variants try a local configuration and a signed Pastebin dead drop first and use Nostr only as a fallback.'

### 2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence (imprecision)

- **imprecision** at `summary and body paragraph 4 first sentence`
  - Claim: The most novel component is a payload that hollows MsBuild.exe ... / The most novel component is that second payload, the TLS-intercepting local proxy.
  - Defect: (low confidence) 'Most novel' is stated as fact; Huntress's recap says only that Jon 'deemed the second payload the most interesting' and 'walked through more novel tradecraft'.
  - Ground truth: Recap: 'Jon deemed the second payload the most interesting, and begrudgingly gave props to the threat actor' and 'Jon walked through more novel tradecraft that he and audience members described as "terrifying."' (https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows)
  - Fix: Attribute the judgement ('Huntress's analysts singled out the second payload as the most interesting') or drop the superlative.
- **imprecision** at `techniques[] (T1546.015)`
  - Claim: T1546.015 (Component Object Model Hijacking)
  - Defect: (low confidence) The source says NetSupport Manager 'registers its own COM object' for persistence; it describes no hijacking of an existing COM registration, which is what T1546.015 names.
  - Ground truth: Huntress write-up: 'NetSupport carries the persistence for all three. It installs a kernel-mode keyboard filter driver ..., registers it as a service ..., modifies Winlogon, and registers its own COM object.' (https://www.huntress.com/blog/defcon-phishing-google-doc-malware)
  - Fix: Remove T1546.015 or replace it with the mappings the page supports (T1543.003 for the service, T1547.004 for the Winlogon modification), checked against the pinned dataset.

### 2026-09-21/afpa-third-party-accommodation-tool-data-extraction (imprecision)

- **imprecision** at `sources[] dates and inline citation labels for Cyberattaque.org and FrenchBreaches`
  - Claim: [Cyberattaque.org, 2026-09-19] ... [FrenchBreaches, 2026-09-19]
  - Defect: (low confidence) The citation dates are the pages' last-modified dates; the pages' own publication dates are 2026-09-15 (Cyberattaque.org) and 2026-09-16 (FrenchBreaches), three to four days earlier. Both pages are living articles updated on 2026-09-19 with AFPA's statement, so the label is defensible but is not the publication date.
  - Ground truth: Cyberattaque.org JSON-LD datePublished 2026-09-15T21:41:46+00:00, dateModified 2026-09-19T12:46:37+00:00; FrenchBreaches datePublished 2026-09-16T22:04:00+02:00, dateModified 2026-09-19T11:17:08+00:00 ('Mise à jour le samedi 19 septembre à 10h00'). (https://www.cyberattaque.org/afpa-pres-dun-million-de-dossiers-revendiques-apres-une-cyberattaque/)
  - Fix: Use the publication dates (2026-09-15, 2026-09-16) or label them 'updated 2026-09-19'.

### 2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal (factual-error)

- **factual-error** at `cves[CVE-2026-93616].affected and fixed; body paragraph 1 ('Affected versions: R82.20 (all takes)' and 'Fixed in the R82.20 Security Hotfix, or Jumbo Hotfix Accumulator R82.10 Take 45+ / R82 Take 127+ / R81.20 Take 170+ / R81.10 Take 192+'); immediate_action`
  - Claim: affected: "R82.20 (all takes); R82.10 Jumbo Hotfix Take 44 or lower; ..."; fixed: "R82.20 Security Hotfix; Jumbo Hotfix Accumulator R82.10 Take 45+ / R82 Take 127+ / R81.20 Take 170+ / R81.10 Take 192+; no LivePatch available"
  - Defect: 'R82.20 (all takes)' is in no source and contradicts the CVE record (affected 'R82.20 with no Jumbo Hotfix') and Check Point's current advisory, which lists a Jumbo Hotfix Accumulator for R82.20 starting from Take 10 as carrying the fix; the fixed field, the body sentence and the immediate action omit that R82.20 route, so an R82.20 host on Take 10 or later is reported affected and the patch path is incomplete.
  - Ground truth: CVE record (CNA Check Point): affected versions 'R82.20 with no Jumbo Hotfix', 'R82.10 with Jumbo Hotfix Take 44 or below', 'R82 with Jumbo Hotfix Take 126 or below', 'R81.20 with Jumbo Hotfix Take 166 or below', 'R81.10 (EOS) with Jumbo Hotfix Take 190 or below'. sk1000171 (lastModified 2026-10-13): 'The fix is also included in: Jumbo Hotfix Accumulator for R82.20 starting from Take 10 ... R82.10 starting from Take 45 ... R82 starting from Take 127 ... R81.20 starting from Take 170 ... R81.10 starting from Take 192'. The Hacker News (2026-09-22): 'The CVE record lists ... R82.20 with no Jumbo Hotfix installed ... Check Point's advisory lists R82.20 as affected without the "no Jumbo Hotfix" condition.' (https://support.checkpoint.com/results/sk/sk1000171/ ; https://cveawg.mitre.org/api/cve/CVE-2026-93616)
  - Fix: Set affected to 'R82.20 with no Jumbo Hotfix (per the CVE record; sk1000171 lists R82.20 without qualifier)' and add 'Jumbo Hotfix Accumulator R82.20 Take 10+' to fixed, the body sentence and the immediate action's accumulator list.
- **factual-error** at `body paragraph 2 ('Detection concept, per Check Point's own two independent indicators of compromise ...' and the Triage sentence on the second indicator); immediate_action; actions[2]`
  - Claim: Detection concept, per Check Point's own two independent indicators of compromise: ... second, a resource-loading error referencing a file path containing parent-directory-reference sequences in the same log ...; since the two log indicators miss the published exploit route.
  - Defect: Stale against the vendor page cited: sk1000171 was revised (lastModified 2026-10-13, after the entry's last update) and now carries Indicator 1 (authentication-bypass stage) plus Indicators 2.a to 2.c (version path, upload path traversal, JAR path breakout), described as 'two different stages of exploitation'; the 'allResourceFiles' resource-loading indicator the entry describes is gone, and the page now calls Indicator 1 an authentication-bypass indicator for this CVE, which Bishop Fox attributes to CVE-2026-91843. Whether the new indicators catch Bishop Fox's route is not stated, so the present-tense 'the two log indicators miss the published exploit route' is no longer a supported statement, and the vendor-vs-Bishop Fox disagreement on Indicator 1 is not surfaced.
  - Ground truth: sk1000171: 'The indicators represent two different stages of exploitation: Indicator 1 may indicate exploitation of the authentication bypass, which can provide an unauthenticated attacker with a valid session. Indicators 2.a-2.c may indicate exploitation by a user who has already passed the authentication stage ... directory traversal, file upload and execution of arbitrary script.' 2.a greps 'Invoking method .* in version: .*(\.|/|%2f ...)'; 2.b greps 'Uploading file .*((\.\./)+|%2e%2e%2f|%2f).*(CPupgrade-tools-|scripts/check_upgrade_tools\.s(h)?)'; 2.c greps 'The path to the jars: .*CPupgrade-tools-.*'. No 'allResourceFiles' or 'ReflectionUtils' string remains. Bishop Fox (2026-10-01) describes the earlier second indicator as an 'ERROR ... ReflectionUtils ... Failed to load allResourceFiles' grep. (https://support.checkpoint.com/results/sk/sk1000171/)
  - Fix: Rewrite the Detection paragraph to the current sk1000171 set (Indicator 1; 2.a to 2.c) and record that it was revised after Bishop Fox's 2026-10-01 post; attribute 'the old second indicator misses this route' to Bishop Fox as of 2026-10-01; state that whether 2.a to 2.c catch the cron-write route is not documented; surface the vendor/Bishop Fox disagreement on what Indicator 1 means; keep the file-integrity advice.

### Outside this batch (not an entry, noted for the registry owner)

- `entities/registry.yaml` records `malware:beavertail` ('used ... as an initial loader') and `malware:invisibleferret` ('deployed ... after BeaverTail loader execution'). The IC3 advisory describes BeaverTail only as 'JavaScript-based malware hidden inside Node Package Manager (NPM) packages, and can be downloaded from GitHub or Bitbucket' and the waterplum entry's own Correction states it is 'not a loader'; the registry summaries contradict the corrected entry.
