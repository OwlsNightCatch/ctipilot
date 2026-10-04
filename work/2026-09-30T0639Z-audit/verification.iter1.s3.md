**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-09-30T07:36:36Z · ended_at=2026-09-30T08:08:19Z · duration_seconds=1903

## Verification report — 2026-09-30T0639Z-audit (iteration 1, slice s3)

Scope: 21 existing entries, 228 claims from `claims.iter1.s3.yaml`; every claim has a verdict row in `verification.iter1.s3.claims.yaml` (175 ok, 26 F4, 21 F3, 4 F5, 2 unreadable). Sources fetched this pass with `fetch_source.py` (extract / url / pdf / cisa-kev cache / ncsc-csh / ncsc-nl / bsi-csaf / osv); KEV claims checked against `work/2026-09-30T0639Z-audit/kev.json` (catalogVersion 2026.09.29).

Unreadable claims (no rung reached the page, not findings): 8d93666909 (both CISA alert pages 403; the KEV feed and THN's links corroborate dateAdded 2026-09-18 and the two-alert split) and 2012d728f0 (GBHackers returns an HTTP 202 challenge on every rung and WebFetch).

### Citation does not support the claim

**#1 F3** `2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle` — HPE: exploitation-status wording attributed to HPE for both bulletins
- Entry text: body: "HPE states it is not aware of active exploitation or public proof-of-concept for either bulletin's flaws."
- Evidence / gap / fix: (low confidence) HPESBNW05133 says only 'not aware of any public discussion or exploit code'; 'active exploitation' is BleepingComputer's wording for the AOS-CX bulletin. Claim 6c836f2f69.

**#2 F3** `2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal` — Check Point: quotation attributed to sk1000171
- Entry text: body: "letting the attacker \"execute a script from an arbitrary path and load an arbitrary Java class\" ([Check Point Support, sk1000171, 2026-09-22](https://support.checkpoint.com/results/sk/sk1000171/))"
- Evidence / gap / fix: That phrase appears on the Check Point Research blog (blog.checkpoint.com ... cve-2026-93616): 'allows an attacker to execute a script from an arbitrary path and load an arbitrary Java class'. sk1000171 says only 'upload and execute arbitrary scripts on the Check Point Management Server' and has no 'Java class'. Move the citation to the blog. Claim 96aae67655.

**#3 F3** `2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal` — Check Point: sk1000171 citation date
- Entry text: "[Check Point Support, sk1000171, 2026-09-22]" and sources[0].date 2026-09-22
- Evidence / gap / fix: (low confidence) The page shows 'Date Created 2026-09-20' (extract metadata date 2026-09-20) and 'Last Modified 2026-09-22'; the cited date is the modification date.

**#4 F3** `2026-09-19/cve-2026-81642-cve-2026-82717-unbound-dnssec-rce` — Unbound: CVSS4.0 9.1 and 'rated High by NLnet Labs' cited to pages that carry neither
- Entry text: body: "CVE-2026-81642 (CVSS4.0 9.1 ...) ... ([NLnet Labs](.../CVE-2026-81642.txt))"; "CVE-2026-82717 (rated High by NLnet Labs ...) ([NLnet Labs](.../CVE-2026-82717.txt))"
- Evidence / gap / fix: (low confidence) Neither .txt advisory prints a score or severity. 9.1 is on the NCSC-CH advisory ('CVSS4.0: 9.1 (CRITICAL)', already a source); 'Severity: High' (and 'Critical' for 81642, with a CVSS 4.0 calculator vector only) is on https://nlnetlabs.nl/projects/unbound/security-advisories/. Cite those pages for those clauses. Claims 8f317b3e7b, 667aeaeb3e.

**#5 F3** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning` — Kiteworks: summary says NCSC-CH names Advanced Forms below 9.5.1
- Entry text: summary: "BSI and NCSC-CH name Kiteworks Advanced Forms below 9.5.1 as affected"; 2026-09-29 section: "NCSC Switzerland's Cyber Security Hub advisory was updated the same day"
- Evidence / gap / fix: BSI WID-SEC-2026-3602 (CSAF) has 'Advanced Forms <9.5.1'. NCSC-CH post 12985 lists affected products as 'Kiteworks Secure File Transfer and Webmail systems' and only quotes Kiteworks' 'Customers with self-hosted Advanced Forms should contact Customer Support'; it was edited 2026-09-28T06:24Z ('Update 28.09.2026'), not on 2026-09-27. Claim 078dfceb5b.

**#6 F3** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning` — Kiteworks: 'No CVE has been assigned' cited to BleepingComputer
- Entry text: body: "No CVE has been assigned, and Kiteworks states plainly it is \"not aware of any compromise ...\" ([BleepingComputer, 2026-09-25])"
- Evidence / gap / fix: The BleepingComputer article has no statement about CVE assignment (no occurrence of 'CVE' in the extracted text). 'There is no known CVE' is watchTowr's quote in The Record; the Record adds that Kiteworks did not answer whether a CVE exists. The two quotations themselves are verbatim. Claim e594f726bc.

**#7 F3** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning` — Kiteworks: channel and count wording
- Entry text: body: "CISO Frank Balonis told Heise Online the company \"received credible threat intelligence ...\""; "Researcher Kevin Beaumont's Shodan search found roughly a thousand internet-facing Kiteworks instances"
- Evidence / gap / fix: (low confidence) Heise: 'In an email obtained by heise security, the KiteWorks CISO urges its customers ...' (the quote is from the customer email, not a statement to Heise). TechCrunch: 'at least a thousand internet-facing Kiteworks systems' (not 'roughly'). Claims 40e364beb1, 507df7991f.

**#8 F3** `2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags` — actions-cool: Socket 'confirmed' overlap with the Mini Shai-Hulud 'npm / PyPI' cluster
- Entry text: body: "Socket confirmed the exfiltration domain overlaps with the Mini Shai-Hulud npm / PyPI campaign cluster ([The Hacker News, 2026-05-19])"
- Evidence / gap / fix: (low confidence) THN: Socket's Burckhardt says the @antv npm compromise 'is likely linked to the actions-cool hack' and 'points to the same Mini Shai-Hulud activity cluster'; the domain sighting in the @antv wave is THN's own; PyPI does not appear on the page. Claim 88abe003e5.

**#9 F3** `2026-09-18/ntc-swiss-solar-inverter-cybersecurity-assessment` — NTC: Baudirektion 'admits' a Huawei-only tender
- Entry text: body: "canton Bern's own cantonal building authority admits that a public tender ... was structured such that only a Huawei inverter could qualify, conceding that cybersecurity is still barely anchored in tenders"
- Evidence / gap / fix: SRF (fetched): 'Die Baudirektion des Kantons Bern schrieb ... den Auftrag so aus, dass de facto nur ein Wechselrichter von Huawei infrage kam. Auf Anfrage schreibt die Baudirektion, man habe den Hersteller nicht vorgegeben. Sie räumt aber ein, Cybersicherheit sei bei Ausschreibungen «noch wenig verankert».' The Huawei-only reading is SRF's own; the authority denies specifying the manufacturer (the entry's own evidence quote says so). Attribute the tender claim to SRF and keep only the cybersecurity concession to the authority. Also (low confidence) cash.ch says 'bereits Lücken geschlossen' (most manufacturers closed gaps), the entry writes 'manufacturers have already closed the gaps'.

**#10 F3** `2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat` — Linux KEV: source-file and function detail not on the cited Red Hat pages
- Entry text: body: "logic error in the kernel's TLS receive path (`net/tls/tls_sw.c`)"; "`crypto/af_alg.c`"; "`ebt_snat` target ... rather than a copy of them"
- Evidence / gap / fix: (low confidence) The three Red Hat CVE pages carry the descriptions but not these file paths, the target name or the 'rather than a copy' phrase (the last is closer to the KEV shortDescription). Claims b0347fcbce, 6c77ae1bf5, 49f81f3cca.

**#11 F3** `2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited` — Cisco FMC: affected releases omit 'and earlier'
- Entry text: body: "Affected releases are 7.0, 7.2, 7.4, 7.6, 7.7 and 10.0, regardless of how the device is configured"; cves[].affected likewise
- Evidence / gap / fix: (low confidence) The advisory's fixed-release table row reads '7.0 and earlier 7.0.10', so releases before 7.0 are affected too. Claim 7b54ee35e0.

**#12 F3** `2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce` — TeamCity: 'TeamCity Cloud is not affected'
- Entry text: summary: "TeamCity Cloud is not affected."; cves[].affected: "TeamCity Cloud is not affected."
- Evidence / gap / fix: (low confidence) JetBrains: 'TeamCity Cloud customers are not required to take any action, as the necessary measures have already been applied' and 'no evidence of TeamCity Cloud environments being exploited'. That is remediated, not unaffected. Claims 5c0940d1e8, 2baac96882.

**#13 F3** `2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce` — TeamCity: citation dates
- Entry text: "[CISA KEV catalog, 2026-09-30]" (update section) and sources[] date 2026-09-30; "[JetBrains, 2026-09-03]" for the Cadence post
- Evidence / gap / fix: (low confidence) KEV entries are dated by listing (2026-08-05, as the body's first KEV citation does; catalogVersion 2026.09.29). The Cadence post was published 2026-08-28 (article datetime) and last updated 2026-09-03. Claims 47266b4da0, 098d827b3b.

**#14 F3** `2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev` — Citrix: two clauses cited to pages that do not carry them
- Entry text: body: "two of which were already being exploited as zero-days before any fix existed ([Citrix])"; "CISA's guidance under BOD 26-04 recommends the same sequence ([CISA KEV catalog])"
- Evidence / gap / fix: (low confidence) The bulletin says 'Exploits ... have been observed'; 'before any fix existed' is watchTowr's wording. The KEV record carries forensicTriage 'Yes' and the BOD 26-04 reference, not the sequence 'logs, a configuration snapshot, a support bundle and a core dump' (that list is in watchTowr's FAQ, 'CISA advises ...'). Claims 48ab05cd03, cdd363ed66.

**#15 F3** `2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209` — Swiss motion: Federal Council reasoning overstated
- Entry text: body: "cited existing legal bases under the EMBAG ... and ongoing work on Swiss digital-sovereignty strategy as already covering the request"
- Evidence / gap / fix: (low confidence) Netzwoche: the Federal Council saw the request as 'teilweise bereits erfüllt' (partly met) and also called a Swiss solo effort unworkable. Claim 4eaed839c0.

### Unsupported / hallucinated facts

**#16 F4** `2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle` — HPE Networking Fabric Composer: bundle bulletin count
- Entry text: body: "carries 45 CVEs in one bulletin ([NCSC-NL, 2026-09-03](...NCSC-2026-0339))"; summary: "fix 45 CVEs in Networking Fabric Composer (AFC)"
- Evidence / gap / fix: HPE's own bulletin HPESBNW05133 (https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt) lists 52 CVEs in its References block (CVE-2026-76657, -76658, -19766, CVE-2026-73700 through -73748); the NCSC-NL mirror lists 45 and omits CVE-2026-73712, -73715, -73721, -73730, -73738, -73743, -73748. The entry states the mirror's count as the bulletin's. Claim cb99932734 and the summary.

**#17 F4** `2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle` — HPE: ArubaOS-CX further-CVE count 'cannot be resolved from HPE directly' and sourcing_note 'could not be retrieved'
- Entry text: body: "HPE's own bulletin page sits behind a support-portal login, so the discrepancy cannot be resolved from HPE directly"; sourcing_note: "HPE's own bulletins sit behind a support-portal login and could not be retrieved"
- Evidence / gap / fix: Both HPE bulletins are plain-text CSAF files that CERT-FR (cited by the entry) links: https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt and https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt. HPESBNW05134 lists 34 CVEs (33 beyond CVE-2026-73749), so BleepingComputer's '23 other' and NCSC-NL's '25 further' are both wrong and the discrepancy the entry narrates is resolvable; CVE-2026-73781 is in HPE's list (CVSS 8.4). Claims cf39cfbc7c, 0de322f7b6.

**#18 F4** `2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle` — HPE: CVE-2026-73749 10.18 range contradicts the newest correction
- Entry text: main text: "Affected release branches and fixes, per HPE's bulletin: the 10.18 branch up to and including 10.18.0001"; Correction 2026-09-30: "CERT-FR lists every AOS-CX 10.18.x release before 10.18.1002 as affected"; cves[].affected: "10.18.x before 10.18.1002"
- Evidence / gap / fix: Supersession (4c-h): the analysis still asserts the range the newest section calls too narrow. Also HPE's own bulletin (https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt) lists exactly 'AOS-CX 10.18.0001' as the affected 10.18 build, so 'narrower than the published scope' and 'affected field ... now say so' present CERT-FR's derived reading ('10.18.x antérieures à 10.18.1002') as HPE's scope. Reconcile the main text and attribute the broader range to CERT-FR. Claims c16d63520f, 4c810cfd69.

**#19 F4** `2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle` — HPE: Fabric Composer 'affected: 7.0.0 through 7.3.3' on five CVE records
- Entry text: cves[CVE-2026-76658, -76657, -19766, -73701, -73700].affected: "Fabric Composer 7.0.0 through 7.3.3"
- Evidence / gap / fix: (low confidence) HPE: 'HPE Networking Fabric Composer 7.3.3 and below'; CERT-FR: 'versions antérieures à 7.3.4'. No source carries a 7.0.0 lower bound (it came from the removed MITRE records). Claims b36e5fad1b, a3b840ac7d, 287459cf06, 4f9d8bd3a8, 20bae1f81b.

**#20 F4** `2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal` — Check Point: 'two-month exploitation timeline' / 'exploited ... since July'
- Entry text: title: "exploited as a zero-day since July"; takeaway: "Check Point's own two-month exploitation timeline means an unpatched, exposed server could have been silently compromised since July"; immediate_action: "exploited as a zero-day against a handful of customers since 2026-07-23"
- Evidence / gap / fix: (low confidence) Check Point states one observation: 'As of the advisory publications date, we observed a handful of pinpointed attacks on July 23, 2026' and sk1000171 says 'a handful of customers who have been attacked'; neither states continuous exploitation over two months. Claim 1eeae0a625.

**#21 F4** `2026-09-19/cve-2026-81642-cve-2026-82717-unbound-dnssec-rce` — Unbound: title still carries CVSS 8.4 that the record says was removed
- Entry text: title: "(CVSS4.0 9.1 / 8.4)"; record: "The score is removed and the text keeps NLnet Labs' High rating."
- Evidence / gap / fix: The 8.4 for CVE-2026-82717 was removed from cves[] and the body but not from the title; NLnet Labs' advisory text prints no number. Claim 9dae56f343.

**#22 F4** `2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags` — actions-cool: 'GitHub has since disabled the repository'
- Entry text: body: "All 53 imposter commits were created within a 3-minute 16-second window; GitHub has since disabled the repository."
- Evidence / gap / fix: The Hacker News: 'GitHub has since disabled access to the repository' with the link pointing at actions-cool/maintain-one-comment (the second action), not issues-helper; StepSecurity does not mention a takedown. Claim dadfeaf681.

**#23 F4** `2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags` — actions-cool: T1552.001 mapping and prose
- Entry text: body: "Maps to T1195.002 (Compromise Software Supply Chain) and T1552.001 (Credentials in Files)."
- Evidence / gap / fix: (low confidence) Sources describe reading /proc/<Runner.Worker PID>/mem from a python3 child process (frontmatter carries T1003.007); no source describes reading credentials from files. Claim 1b63fb96e5.

**#24 F4** `2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags` — actions-cool: frontmatter summary covers an unrelated incident with unsourced figures
- Entry text: summary: "Two more CI/CD supply-chain incidents ... Nx Console 18.95.0 (2.2 M installs) compromised via stolen publisher credentials for an 11-minute window 2026-05-18 12:36-12:47 UTC (The Hacker News, 2026-05-19)"
- Evidence / gap / fix: The body, title, headline and sources cover only actions-cool/issues-helper; the cited THN 2026-05-19 article (github-actions-supply-chain-attack) never mentions Nx Console, which has its own entry (2026-05-20/nx-console-vs-code-extension-2-2-m-installs-compromised-via). The summary reads as a leftover of the legacy combined brief; rewrite it to the issues-helper finding only.

**#25 F4** `2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat` — Linux KEV: 'not at elevated risk' and 'only confirmed-exploited attack surfaces'
- Entry text: takeaway: "A general-purpose Linux server or workstation fleet on standard kernel patch cadence is not at elevated risk from any of the three"; actions[0]: "these three configurations are the only confirmed-exploited attack surfaces"
- Evidence / gap / fix: No source says which configurations are exploited (the entry itself says there is 'no public account of how any of them is used'), and the same takeaway opens with 'treat all three as confirmed exploited' while Red Hat says 'Address this vulnerability with high priority'. The unsupported reassurance and the 'only confirmed-exploited' clause are F4; AF_ALG availability claims ('often restricted or entirely unloaded') and the kTLS proxy/appliance prevalence are unsourced. Claim ab2f2327cc.

**#26 F4** `2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat` — Linux KEV: headline says Red Hat 'confirm[s] active exploitation'
- Entry text: headline: "CISA and Red Hat confirm active exploitation of three separate Linux kernel bugs"
- Evidence / gap / fix: (low confidence) The quoted Red Hat words are 'This CVE is high risk and there are known public exploits leveraging this vulnerability' (public exploit code); 'acknowledge active exploitation' is THN's paraphrase, and the summary and 09-30 section say only 'public exploits exist'. The banner text is not visible in the Red Hat page bodies fetched this pass. Claim 5919082028.

**#27 F4** `2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited` — Cisco FMC: static-account identity discriminator and 'incident-response case' generalisation
- Entry text: Triage: "an authentication event for the vendor's static low-privileged account, from any source address including an internal one, has no benign explanation"; 2026-09-30 section: "A management server that held the static account before the hardening release is therefore an incident-response case, not only a patch item"
- Evidence / gap / fix: (low confidence) Cisco names neither the account nor states it has no legitimate use, and its own IOC is a package_info / /var/tmp/license.tmp log line, not authentication under the account. The KEV ransomware flag does not make every server that held the account an IR case; Cisco says the attack surface 'is reduced' without public internet access. Claims 42427de6d2, 8dee3a6dd0, 4cebbbe85b.

**#28 F4** `2026-05-08/dragos-2025-ot-cybersecurity-year-in-review-81-of-ir-engagem` — Dragos: headline says credentials 'behind' 73% of cases; title says 'stolen'
- Entry text: headline: "compromised VPN or jump-host credentials behind 73% of its incident cases"; title: "73% of IR cases involved stolen VPN or jump-host credentials"
- Evidence / gap / fix: (low confidence) Dragos: '73 percent of all-time IR cases involved compromised VPN or jumphost credentials' (involvement, not cause; 'compromised', not 'stolen'). Also body: 'Windows or ESXi hosts running SCADA software are encrypted' compresses 'Windows servers hosting SCADA software or engineering workstations are compromised. Ransomware groups target VMware ESXi hypervisors hosting OT applications' (claim a32eb47307). Claim 62c1467b1c.

**#29 F4** `2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce` — TeamCity: sourcing_note still relies on a MITRE record the run removed
- Entry text: sourcing_note: "the MITRE CVE record cited alongside it sits in JetBrains' own CNA container ... the deserialization characterisation comes from the structured record; and CISA's ADP enrichment layer on the same record, dated 2026-07-28, independently assessed exploitation status as none"
- Evidence / gap / fix: No MITRE/CVE record is cited any more (sources[] has JetBrains, two CISA items, the Cadence post), so these sentences describe uncited material and contradict the first sentence (CWE-502 'comes from CISA's KEV record'). Reduce the note to provenance (see F11).

**#30 F4** `2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft` — Gentlemen: CVE-2025-24799 marked 'exploited'; record rationale names Japanese victims
- Entry text: cves[].status: [exploited, poc-public, patch-available]; record: "the reconstructed intrusions targeted Japanese organizations"
- Evidence / gap / fix: (low confidence) Talos: 'the actor attempted to exploit CVE-2025-24799 ... using both a PoC and sqlmap to retrieve user information' (an attempt, no success stated). Talos' open-directory section names no victims or country; the Japan framing belongs to the article's incident statistics. Claims 183f52351a, f7bbb75beb.

**#31 F4** `2026-09-24/solarwinds-observability-cve-2026-28324-28325-unauth-rce` — SolarWinds: record says both flaws are reachable only in non-default configurations
- Entry text: record: "priority moves from high to notable because both flaws are unexploited and reachable only in non-default configurations"
- Evidence / gap / fix: Release notes: CVE-2026-28324 'Installations configured in a non-default and non-secure configuration are affected'; CVE-2026-28325 'when the application is configured to use a specific communication mode' (not stated to be non-default; the same release switches default WPM players from Server-initiated to Player-initiated communication). Claim df13fb93ac.

**#32 F4** `2026-09-27/qbusoft-medyc-poland-healthcare-breach-fingerprint-actor` — Qbusoft: record rationale 'no named vector'
- Entry text: record: "a Polish healthcare-software breach with no named vector, so it is awareness only"
- Evidence / gap / fix: The entry states the intrusion was 'via an SQL-injection vulnerability' (Inowrocław facility notice) and maps T1190. Claim 4b83205e06.

**#33 F4** `2026-09-29/openai-dns-tunnel-sandbox-escape-self-replicating-injection` — OpenAI: record says fetch narration was removed
- Entry text: record: "the text carried narration about the entry itself and the fetch pipeline ... the narration is removed"
- Evidence / gap / fix: (low confidence) sourcing_note still reads 'independently reachable and read in full' and 'were not reachable'. Claim aae3e8d821.

**#34 F4** `2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev` — Citrix: headline 'no workaround exists'
- Entry text: headline: "no workaround exists, so patch and check for compromise now"
- Evidence / gap / fix: (low confidence) Sources say Citrix has published no workaround (watchTowr FAQ: 'Citrix has not published a workaround'); the entry's own 09-30 section lists Mandiant's interim controls (disable DTLS, block UDP/443) for CVE-2026-88772. Claim 3b8b4f7733.

**#35 F4** `2026-09-22/plugin4shell-ai-coding-agent-sha-pinning-bypass` — Plugin4Shell: vendor patches asserted as fact
- Entry text: summary: "Anthropic and OpenAI have patched"; actions[0]: "upgrade Claude Code to >=2.1.179 and Codex to >=0.146.0"
- Evidence / gap / fix: (low confidence) THN: 'Anthropic's release notes for 2.1.179 do not mention the fix, and the account that it is fixed in is Air's.' The patch status rests on the discloser alone; say so.

**#36 F4** `2026-09-17/kairos-libercourt-commune-ransomware-confirmed` — Kairos: takeaway asserts a shared IT-provider gap
- Entry text: takeaway: "confirm your own externally-contracted IT provider has a documented, tested incident-detection and notification path, since that gap is what both confirmed cases share"
- Evidence / gap / fix: (low confidence) The Velilla statement (fetched) says no effective access or extraction can be confirmed and mentions no IT provider; the Libercourt notice says the commune's provider ran checks. Neither source identifies a detection or notification gap; 'limited in-house IT staffing' is likewise unsourced.

### Claims missing inline citation

**#37 F5** `2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle` — HPE: fixed versions and discovery statement carry no linked source
- Entry text: body: "Fixed in Fabric Composer 7.4.0 (or 7.3.4 for the 7.3 branch); every 7.3.3-and-earlier install is affected, all discovered by HPE's own internal Networking security research team."; CVE-2026-76657 / -19766 / -73701 / -73700 sentences
- Evidence / gap / fix: NCSC-NL's CSAF carries no version data ('vers:unknown/*') and CERT-FR carries 7.3.4 only; 7.4.0 and internal discovery appear in no linked source, and the CVE-2026-76657 clause and the 'Three more rank Critical' sentence follow the last citation. Claim df1a17236c.

**#38 F5** `2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft` — Gentlemen: GLPI fix version, endpoint and CVSS are not in the only cited source
- Entry text: body: "an unauthenticated SQL injection in GLPI's inventory endpoint (fixed in GLPI 10.0.18)"; cves[]: cvss 7.5, affected ">= 10.0.0, < 10.0.18", fixed 10.0.18
- Evidence / gap / fix: Talos gives none of these. They are correct per GHSA-jv89-g7f7-jwfg / CVE-2025-24799 (GLPI: 'unauthenticated SQL injection through the inventory endpoint ... fixed in 10.0.18', CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) but that vendor advisory is not cited; add https://github.com/glpi-project/glpi/security/advisories/GHSA-jv89-g7f7-jwfg (F6). The sourcing_note's claim that CVE-2025-2479 is an unrelated WordPress XSS flaw is likewise uncited (true: Easy Custom Admin Bar reflected XSS).

**#39 F5** `2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat` — Linux KEV: fixed kernel builds carry no citation and CVE-2026-53266 list is incomplete
- Entry text: body: "Fixed kernel builds: 6.1.149 / 6.6.103 / 6.12.44 / 6.16.4 / 6.17 for CVE-2025-39682; ... 5.10.259 / 5.15.210 / 6.1.176 / 6.6.143 / 6.12.94 / 6.18.36 for CVE-2026-53266."
- Evidence / gap / fix: No cited page carries them. They match the kernel CNA records, but the CVE-2026-53266 record also lists 7.0.13 and 7.1 as fixed, omitted here. Claim 301d2b8656.

**#40 F5** `2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited` — Cisco FMC: KEV sentence has no inline citation
- Entry text: body: "CISA also lists the flaw in its Known Exploited Vulnerabilities catalogue, independent confirmation that the exploitation is real."
- Evidence / gap / fix: KEV lists CVE-2026-20316 (dateAdded 2026-07-29), but the sentence carries no link although the KEV JSON is now in sources[] (claim 2a4a427785).

**#41 F5** `2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags` — actions-cool: scope claim for EU and Swiss organisations
- Entry text: body: "**Why it matters to us:** EU and Swiss developer organisations using GitHub Actions for public-sector software supply chains were directly in scope during the attack window."
- Evidence / gap / fix: No linked source names victims, regions or sectors. Claim 94a6f172bd.

### Strengthen primary source

**#42 F6** `2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle` — HPE bundle: primary is a national-CERT mirror; HPE's own bulletins are fetchable
- Entry text: sources[0] NCSC-NL (role primary); sourcing_note: 'HPE's own bulletins sit behind a support-portal login and could not be retrieved'
- Evidence / gap / fix: Add https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt (HPESBNW05133, published 2026-Sep-01, revision 1) and https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt (HPESBNW05134) as the primary sources; they carry per-CVE CVSS vectors, the 7.4.0 / 7.3.4 fixes, the 'discovered by internal security research' statement, the workaround (restrict CLI and web interfaces to a dedicated L2 segment / firewall) and the exact 10.18.0001 affected build.

**#43 F6** `2026-09-24/solarwinds-observability-cve-2026-28324-28325-unauth-rce` — SolarWinds: vendor trust-center advisory is retrievable for CVE-2026-28324
- Entry text: sourcing_note: 'SolarWinds' trust-center advisory pages could not be retrieved'
- Evidence / gap / fix: https://www.solarwinds.com/trust-center/security-advisories/cve-2026-28324 returned the vendor advisory this pass (Severity 9.8 Critical, first published 09/22/2026, 'Observability Self-Hosted 2026.2.2 and below'); the CVE-2026-28325 page returned 403. CERT-FR links both.

### Drop (low relevance / off-audience / duplicate)

**#44 F7** `2026-09-17/kairos-libercourt-commune-ransomware-confirmed` — Kairos: routine incident with no vector, actor tradecraft or behaviour is three paragraphs
- Entry text: priority routine; body of three long paragraphs plus takeaway; sourcing_note: 'This is an out-of-nexus small foreign commune; see body for the relevance basis.'
- Evidence / gap / fix: Rubric 5b: an incident with no access vector, no confirmed actor and no behaviour beyond its impact is routine and two sentences at most, or dropped; the Kairos link is 'a claim, not an attribution', the Swiss-relevance paragraph is speculation ('consistent with -- though not proven to be'). Cut to two sentences or drop.

### Needs more research

**#45 F8** `2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags` — actions-cool: labelled lines missing
- Entry text: body has 'Why it matters to us' but no **Exposure:**, **Detection:** or **Defender takeaway:**
- Evidence / gap / fix: StepSecurity supports all three: exposure (any workflow referencing the action by version tag pulls the payload on its next run; only full-SHA pins are unaffected), detection (bun download to /home/runner/.bun/bin/bun, python3 child reading /proc/<Runner.Worker PID>/mem, tr/grep filtering for the secret flag, outbound HTTPS from the runner) and the Harden-Runner egress control.

**#46 F8** `2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce` — TeamCity: JetBrains' 2026-08-07 follow-up (vendor-confirmed exploitation and log indicators) is not used
- Entry text: Detection/Triage: 'Requests to the agent-polling endpoint arriving from addresses that are not your registered build agents ... any child process spawned by the TeamCity server process ...'; evidence[] still carries 'we are not aware of any active exploitation'
- Evidence / gap / fix: https://blog.jetbrains.com/teamcity/2026/08/cve-2026-63077-update/ ('Since our initial announcement on July 27, 2026, we have received reports of active exploitation, as well as attempted exploitation'): review server logs for com.thoughtworks.xstream.converters.ConversionException (attempted or successful exploit) and ForbiddenClassException (blocked after patching), and unauthorized build agents named 'scan*'. The primary advisory page itself now carries an 'August 7, 2026 update' banner. These vendor indicators are the honest Detection / Triage content and supersede the 'not aware' evidence quotes.

**#47 F8** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning` — Kiteworks: vendor's only customer instruction not carried
- Entry text: takeaway: 'What remains is confirming every Kiteworks deployment ... runs release 9.5.1 or later.'
- Evidence / gap / fix: (low confidence) Kiteworks' own notice: 'Customers with self-hosted Advanced Forms should contact Customer Support for assistance.' Lead the takeaway with it.

**#48 F8** `2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209` — Swiss motion: National Council outcome available on the cited Netzwoche page but omitted
- Entry text: body: 'the referral status now recorded is the outcome for a motion that has cleared both parliamentary chambers'
- Evidence / gap / fix: (low confidence) Netzwoche's 2026-09-25 update on the cited page: National Council adopted 126 to 66 after a 13 to 12 committee vote; add it and the committee minority's 'existing legal bases suffice' argument.

### Surface contradiction

**#49 F9** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning` — Kiteworks: takeaway asserts 9.5.1 is what remains; newest section leaves customer action open
- Entry text: main takeaway: "What remains is confirming every Kiteworks deployment, including the Advanced Forms module, runs release 9.5.1 or later."; 2026-09-30 section: "The release does not say whether self-hosted instances need customer-side action, so the written question to Kiteworks Support is the open task."
- Evidence / gap / fix: (low confidence) Kiteworks' notice says 'Customers with self-hosted Advanced Forms should contact Customer Support for assistance', and the critical flaw fixed 'during the window' is not tied to 9.5.1 anywhere. Three stacked 'Defender takeaway' blocks (main, 09-29 updated, 09-30 updated) also disagree in emphasis. Claim dfc568f752.

### Missed angles

**#50 F10** `2026-09-29/bitget-hot-wallet-theft-north-korea-nexus` — Bitget: Mandiant and SlowMist independent reports published 2026-09-30 name the attack path
- Entry text: priority-recalibration rationale: 'through an unnamed third-party product, with nothing the constituency can act on'
- Evidence / gap / fix: Bitget's incident page (updated) and https://www.bitget.com/support/articles/12560603896305 (2026-09-30): both investigations 'identified the compromise of third-party security products'; Mandiant's status report (https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf): the actor gained privileged access to third-party security appliances A and B, deployed a web shell on appliance B, established C2, moved laterally to the production wallet job server and deployed malicious packages. That is edge-security-appliance compromise plus lateral movement, a transferable TTP the entry lacks (and it changes the 'nothing to act on' premise). Suggested search: 'Bitget Mandiant SlowMist report security appliance web shell'; append as an update.

### Editorial / less-is-more flags (advisory)

**#51 F11** `2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal ; 2026-09-24/solarwinds-observability-cve-2026-28324-28325-unauth-rce ; 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning ; 2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle ; 2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat` — Reader-facing sections narrate frontmatter edits
- Entry text: Check Point: "The structured CVE data above marked this flaw as having no patch ... It is now marked patch-available."; SolarWinds: "so the Detection line and the action no longer suggest it"; Kiteworks: "The title, summary and takeaway above still described the shutdown as current advice ... They now say so."; HPE: "The affected field and the earlier correction now say so."; Linux: "The headline, summary and main text above said ... They now say so."
- Evidence / gap / fix: Field names and record-keeping narration in `## Correction` sections (rubric 12/4c-i). Keep only the cited delta (for Check Point the LivePatch-does-not-cover fact; for Kiteworks the nine-hour figure) and drop the rest or make the record internal.

**#52 F11** `2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209` — Swiss motion: presentation-only Improvement section
- Entry text: ## Improvement -- 2026-09-30T07:02:46Z: "The law-firm summary of the motion quoted above is now given in English translation ..."
- Evidence / gap / fix: The section's only content is that a quote changed language; per 4c-i it should be an `internal: true` improvement with no body section.

**#53 F11** `2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce ; 2026-09-17/kairos-libercourt-commune-ransomware-confirmed ; 2026-09-29/openai-dns-tunnel-sandbox-escape-self-replicating-injection` — sourcing_note carries workflow narration
- Entry text: TeamCity: "A Cloud Security Alliance Lab Space note ... was the discovery path for this item but is an automated re-reporting pipeline"; Kairos: "see body for the relevance basis"; OpenAI: "independently reachable and read in full ... were not reachable"
- Evidence / gap / fix: sourcing_note should be two sentences of provenance (rubric 12); TeamCity's runs ~15 lines including discovery-path and pipeline commentary.

**#54 F11** `2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags` — actions-cool: IOC-like commit hash and bare ATT&CK ids in prose
- Entry text: summary and body: "imposter commit 1c9e803"; body: "Maps to T1195.002 ... and T1552.001"
- Evidence / gap / fix: The run removed the exfiltration domain as an indicator but left the imposter commit SHA; ATT&CK ids belong in techniques[] (the prose list also omits the mapped T1003.007). 'Why it matters to us' is org-voice narration.

**#55 F11** `2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning` — Kiteworks: three stacked Defender takeaway blocks
- Entry text: **Defender takeaway:** (main), **Defender takeaway (updated):** (09-29), **Defender takeaway (updated):** (09-30)
- Evidence / gap / fix: Rubric 4c-h: replace the original takeaway with the current one instead of stacking.

**#56 F11** `2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev` — Citrix: second Triage line and US-directive rationale
- Entry text: **Triage:** in the main text (CVE-2026-88772: "DTLS handling anomalies (crashes, unexpected restarts, or malformed-record errors ...)") and a second **Triage:** in the 09-30 section (Mandiant artifacts); "CISA's guidance under BOD 26-04 recommends the same sequence"
- Evidence / gap / fix: The generic 88772 discriminator is superseded by GTIG's specific log artifacts; the BOD 26-04 appeal is a US-federal directive used as justification.

**#57 F11** `2026-09-22/plugin4shell-ai-coding-agent-sha-pinning-bypass ; 2026-09-17/ddrop-dram-interposer-defeats-confidential-computing` — Length and scope caveat
- Entry text: Plugin4Shell headline: 'zero-click plugin-marketplace takeover'; DDRop: four paragraphs at routine
- Evidence / gap / fix: THN's scope caveat (GitHub rejects SHA-shaped branch names; auto-update is on by default only for each agent's built-in GitHub-hosted marketplace) is in paragraph three but not in the headline or summary; DDRop's body is long for a `routine` physical-access research item.

### Single-source items missing [SINGLE-SOURCE] flag

**#58 F12** `2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited` — Cisco FMC: verification value vs sources
- Entry text: verification: single-source; sourcing_note: 'CISA's KEV catalog independently lists the flaw as exploited and marks known ransomware use.'
- Evidence / gap / fix: (low confidence) sources[] now holds Cisco PSIRT plus the CISA KEV catalog as a second, independent record of exploitation; either set the value to match (multi-source, or single-source-national-cert wording) or stop calling CISA's listing independent.

### Org-triage line missing / inconsistent

**#59 F16** `2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle` — HPE bundle: priority high with no exploitation and no PoC
- Entry text: priority: high; HPE: 'not aware of any public discussion or exploit code'
- Evidence / gap / fix: (low confidence) Rubric 5b/F7: an unexploited management-plane bundle with no PoC does not clear `high`; the same audit moved the equally unexploited SolarWinds entry to notable. Calibrate consistently.

**#60 F16** `2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags` — actions-cool: priority high on a 2026-05 event
- Entry text: priority: high
- Evidence / gap / fix: (low confidence) A four-month-old supply-chain event with the repository already disabled and no live decision; `high` disqualifier list includes an event older than 30 days with no new development.

### Classification missing / inconsistent

**#61 F17** `2026-09-17/kairos-libercourt-commune-ransomware-confirmed` — Kairos: reliability B on a lone C-tier relay
- Entry text: classification: {reliability: B, credibility: 2}; sources[0] FrenchBreaches
- Evidence / gap / fix: (low confidence) sources/sources.json rates FrenchBreaches C and the sourcing_note calls it the sole source for the confirmation; B is not supported by the cited source's tier.

**#62 F17** `2026-09-22/plugin4shell-ai-coding-agent-sha-pinning-bypass` — Plugin4Shell: credibility 1 on a single-discloser finding
- Entry text: classification: {reliability: B, credibility: 1}
- Evidence / gap / fix: (low confidence) THN, Help Net Security and heise report AIR's research; THN says the vendor fix is 'the account ... in Air's' and no vendor advisory exists, so the finding is uncorroborated by an independent assessor (2).

### Verdict

NEEDS_FIXES (truth: 36, editorial: 19, advisory: 7)

Coverage note: no other relevant in-window gap surfaced for this slice beyond the Bitget update (F10) and the TeamCity vendor follow-up (F8). Findings marked (low confidence) rest on wording differences the main agent should weigh; the HPE, Check Point, Kiteworks, actions-cool, NTC and Unbound items are evidenced against pages fetched this pass.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) - iteration 1, slice s3
- code: F4
  category: hallucinated-fact
  section: "2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle"
  item: "HPE Networking Fabric Composer: bundle bulletin count"
  url_or_quote: "body: \"carries 45 CVEs in one bulletin ([NCSC-NL, 2026-09-03](...NCSC-2026-0339))\"; summary: \"fix 45 CVEs in Networking Fabric Composer (AFC)\""
  summary: "HPE's own bulletin HPESBNW05133 (https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt) lists 52 CVEs in its References block (CVE-2026-76657, -76658, -19766, CVE-2026-73700 through -73748); the NCSC-NL mirror lists 45 and omits CVE-2026-73712, -73715, -73721, -73730, -73738, -73743, -73748. The entry states the mirror's count as the bulletin's. Claim cb99932734 and the summary."
- code: F4
  category: hallucinated-fact
  section: "2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle"
  item: "HPE: ArubaOS-CX further-CVE count 'cannot be resolved from HPE directly' and sourcing_note 'could not be retrieved'"
  url_or_quote: "body: \"HPE's own bulletin page sits behind a support-portal login, so the discrepancy cannot be resolved from HPE directly\"; sourcing_note: \"HPE's own bulletins sit behind a support-portal login and could not be retrieved\""
  summary: "Both HPE bulletins are plain-text CSAF files that CERT-FR (cited by the entry) links: https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt and https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt. HPESBNW05134 lists 34 CVEs (33 beyond CVE-2026-73749), so BleepingComputer's '23 other' and NCSC-NL's '25 further' are both wrong and the discrepancy the entry narrates is resolvable; CVE-2026-73781 is in HPE's list (CVSS 8.4). Claims cf39cfbc7c, 0de322f7b6."
- code: F4
  category: hallucinated-fact
  section: "2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle"
  item: "HPE: CVE-2026-73749 10.18 range contradicts the newest correction"
  url_or_quote: "main text: \"Affected release branches and fixes, per HPE's bulletin: the 10.18 branch up to and including 10.18.0001\"; Correction 2026-09-30: \"CERT-FR lists every AOS-CX 10.18.x release before 10.18.1002 as affected\"; cves[].affected: \"10.18.x before 10.18.1002\""
  summary: "Supersession (4c-h): the analysis still asserts the range the newest section calls too narrow. Also HPE's own bulletin (https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt) lists exactly 'AOS-CX 10.18.0001' as the affected 10.18 build, so 'narrower than the published scope' and 'affected field ... now say so' present CERT-FR's derived reading ('10.18.x antérieures à 10.18.1002') as HPE's scope. Reconcile the main text and attribute the broader range to CERT-FR. Claims c16d63520f, 4c810cfd69."
- code: F4
  category: hallucinated-fact
  section: "2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle"
  item: "HPE: Fabric Composer 'affected: 7.0.0 through 7.3.3' on five CVE records"
  url_or_quote: "cves[CVE-2026-76658, -76657, -19766, -73701, -73700].affected: \"Fabric Composer 7.0.0 through 7.3.3\""
  summary: "(low confidence) HPE: 'HPE Networking Fabric Composer 7.3.3 and below'; CERT-FR: 'versions antérieures à 7.3.4'. No source carries a 7.0.0 lower bound (it came from the removed MITRE records). Claims b36e5fad1b, a3b840ac7d, 287459cf06, 4f9d8bd3a8, 20bae1f81b."
- code: F3
  category: claim-not-supported
  section: "2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle"
  item: "HPE: exploitation-status wording attributed to HPE for both bulletins"
  url_or_quote: "body: \"HPE states it is not aware of active exploitation or public proof-of-concept for either bulletin's flaws.\""
  summary: "(low confidence) HPESBNW05133 says only 'not aware of any public discussion or exploit code'; 'active exploitation' is BleepingComputer's wording for the AOS-CX bulletin. Claim 6c836f2f69."
- code: F3
  category: claim-not-supported
  section: "2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal"
  item: "Check Point: quotation attributed to sk1000171"
  url_or_quote: "body: \"letting the attacker \\\"execute a script from an arbitrary path and load an arbitrary Java class\\\" ([Check Point Support, sk1000171, 2026-09-22](https://support.checkpoint.com/results/sk/sk1000171/))\""
  summary: "That phrase appears on the Check Point Research blog (blog.checkpoint.com ... cve-2026-93616): 'allows an attacker to execute a script from an arbitrary path and load an arbitrary Java class'. sk1000171 says only 'upload and execute arbitrary scripts on the Check Point Management Server' and has no 'Java class'. Move the citation to the blog. Claim 96aae67655."
- code: F4
  category: hallucinated-fact
  section: "2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal"
  item: "Check Point: 'two-month exploitation timeline' / 'exploited ... since July'"
  url_or_quote: "title: \"exploited as a zero-day since July\"; takeaway: \"Check Point's own two-month exploitation timeline means an unpatched, exposed server could have been silently compromised since July\"; immediate_action: \"exploited as a zero-day against a handful of customers since 2026-07-23\""
  summary: "(low confidence) Check Point states one observation: 'As of the advisory publications date, we observed a handful of pinpointed attacks on July 23, 2026' and sk1000171 says 'a handful of customers who have been attacked'; neither states continuous exploitation over two months. Claim 1eeae0a625."
- code: F3
  category: claim-not-supported
  section: "2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal"
  item: "Check Point: sk1000171 citation date"
  url_or_quote: "\"[Check Point Support, sk1000171, 2026-09-22]\" and sources[0].date 2026-09-22"
  summary: "(low confidence) The page shows 'Date Created 2026-09-20' (extract metadata date 2026-09-20) and 'Last Modified 2026-09-22'; the cited date is the modification date."
- code: F4
  category: hallucinated-fact
  section: "2026-09-19/cve-2026-81642-cve-2026-82717-unbound-dnssec-rce"
  item: "Unbound: title still carries CVSS 8.4 that the record says was removed"
  url_or_quote: "title: \"(CVSS4.0 9.1 / 8.4)\"; record: \"The score is removed and the text keeps NLnet Labs' High rating.\""
  summary: "The 8.4 for CVE-2026-82717 was removed from cves[] and the body but not from the title; NLnet Labs' advisory text prints no number. Claim 9dae56f343."
- code: F3
  category: claim-not-supported
  section: "2026-09-19/cve-2026-81642-cve-2026-82717-unbound-dnssec-rce"
  item: "Unbound: CVSS4.0 9.1 and 'rated High by NLnet Labs' cited to pages that carry neither"
  url_or_quote: "body: \"CVE-2026-81642 (CVSS4.0 9.1 ...) ... ([NLnet Labs](.../CVE-2026-81642.txt))\"; \"CVE-2026-82717 (rated High by NLnet Labs ...) ([NLnet Labs](.../CVE-2026-82717.txt))\""
  summary: "(low confidence) Neither .txt advisory prints a score or severity. 9.1 is on the NCSC-CH advisory ('CVSS4.0: 9.1 (CRITICAL)', already a source); 'Severity: High' (and 'Critical' for 81642, with a CVSS 4.0 calculator vector only) is on https://nlnetlabs.nl/projects/unbound/security-advisories/. Cite those pages for those clauses. Claims 8f317b3e7b, 667aeaeb3e."
- code: F3
  category: claim-not-supported
  section: "2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning"
  item: "Kiteworks: summary says NCSC-CH names Advanced Forms below 9.5.1"
  url_or_quote: "summary: \"BSI and NCSC-CH name Kiteworks Advanced Forms below 9.5.1 as affected\"; 2026-09-29 section: \"NCSC Switzerland's Cyber Security Hub advisory was updated the same day\""
  summary: "BSI WID-SEC-2026-3602 (CSAF) has 'Advanced Forms <9.5.1'. NCSC-CH post 12985 lists affected products as 'Kiteworks Secure File Transfer and Webmail systems' and only quotes Kiteworks' 'Customers with self-hosted Advanced Forms should contact Customer Support'; it was edited 2026-09-28T06:24Z ('Update 28.09.2026'), not on 2026-09-27. Claim 078dfceb5b."
- code: F3
  category: claim-not-supported
  section: "2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning"
  item: "Kiteworks: 'No CVE has been assigned' cited to BleepingComputer"
  url_or_quote: "body: \"No CVE has been assigned, and Kiteworks states plainly it is \\\"not aware of any compromise ...\\\" ([BleepingComputer, 2026-09-25])\""
  summary: "The BleepingComputer article has no statement about CVE assignment (no occurrence of 'CVE' in the extracted text). 'There is no known CVE' is watchTowr's quote in The Record; the Record adds that Kiteworks did not answer whether a CVE exists. The two quotations themselves are verbatim. Claim e594f726bc."
- code: F3
  category: claim-not-supported
  section: "2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning"
  item: "Kiteworks: channel and count wording"
  url_or_quote: "body: \"CISO Frank Balonis told Heise Online the company \\\"received credible threat intelligence ...\\\"\"; \"Researcher Kevin Beaumont's Shodan search found roughly a thousand internet-facing Kiteworks instances\""
  summary: "(low confidence) Heise: 'In an email obtained by heise security, the KiteWorks CISO urges its customers ...' (the quote is from the customer email, not a statement to Heise). TechCrunch: 'at least a thousand internet-facing Kiteworks systems' (not 'roughly'). Claims 40e364beb1, 507df7991f."
- code: F9
  category: surface-contradiction
  section: "2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning"
  item: "Kiteworks: takeaway asserts 9.5.1 is what remains; newest section leaves customer action open"
  url_or_quote: "main takeaway: \"What remains is confirming every Kiteworks deployment, including the Advanced Forms module, runs release 9.5.1 or later.\"; 2026-09-30 section: \"The release does not say whether self-hosted instances need customer-side action, so the written question to Kiteworks Support is the open task.\""
  summary: "(low confidence) Kiteworks' notice says 'Customers with self-hosted Advanced Forms should contact Customer Support for assistance', and the critical flaw fixed 'during the window' is not tied to 9.5.1 anywhere. Three stacked 'Defender takeaway' blocks (main, 09-29 updated, 09-30 updated) also disagree in emphasis. Claim dfc568f752."
- code: F4
  category: hallucinated-fact
  section: "2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags"
  item: "actions-cool: 'GitHub has since disabled the repository'"
  url_or_quote: "body: \"All 53 imposter commits were created within a 3-minute 16-second window; GitHub has since disabled the repository.\""
  summary: "The Hacker News: 'GitHub has since disabled access to the repository' with the link pointing at actions-cool/maintain-one-comment (the second action), not issues-helper; StepSecurity does not mention a takedown. Claim dadfeaf681."
- code: F3
  category: claim-not-supported
  section: "2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags"
  item: "actions-cool: Socket 'confirmed' overlap with the Mini Shai-Hulud 'npm / PyPI' cluster"
  url_or_quote: "body: \"Socket confirmed the exfiltration domain overlaps with the Mini Shai-Hulud npm / PyPI campaign cluster ([The Hacker News, 2026-05-19])\""
  summary: "(low confidence) THN: Socket's Burckhardt says the @antv npm compromise 'is likely linked to the actions-cool hack' and 'points to the same Mini Shai-Hulud activity cluster'; the domain sighting in the @antv wave is THN's own; PyPI does not appear on the page. Claim 88abe003e5."
- code: F4
  category: hallucinated-fact
  section: "2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags"
  item: "actions-cool: T1552.001 mapping and prose"
  url_or_quote: "body: \"Maps to T1195.002 (Compromise Software Supply Chain) and T1552.001 (Credentials in Files).\""
  summary: "(low confidence) Sources describe reading /proc/<Runner.Worker PID>/mem from a python3 child process (frontmatter carries T1003.007); no source describes reading credentials from files. Claim 1b63fb96e5."
- code: F4
  category: hallucinated-fact
  section: "2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags"
  item: "actions-cool: frontmatter summary covers an unrelated incident with unsourced figures"
  url_or_quote: "summary: \"Two more CI/CD supply-chain incidents ... Nx Console 18.95.0 (2.2 M installs) compromised via stolen publisher credentials for an 11-minute window 2026-05-18 12:36-12:47 UTC (The Hacker News, 2026-05-19)\""
  summary: "The body, title, headline and sources cover only actions-cool/issues-helper; the cited THN 2026-05-19 article (github-actions-supply-chain-attack) never mentions Nx Console, which has its own entry (2026-05-20/nx-console-vs-code-extension-2-2-m-installs-compromised-via). The summary reads as a leftover of the legacy combined brief; rewrite it to the issues-helper finding only."
- code: F3
  category: claim-not-supported
  section: "2026-09-18/ntc-swiss-solar-inverter-cybersecurity-assessment"
  item: "NTC: Baudirektion 'admits' a Huawei-only tender"
  url_or_quote: "body: \"canton Bern's own cantonal building authority admits that a public tender ... was structured such that only a Huawei inverter could qualify, conceding that cybersecurity is still barely anchored in tenders\""
  summary: "SRF (fetched): 'Die Baudirektion des Kantons Bern schrieb ... den Auftrag so aus, dass de facto nur ein Wechselrichter von Huawei infrage kam. Auf Anfrage schreibt die Baudirektion, man habe den Hersteller nicht vorgegeben. Sie räumt aber ein, Cybersicherheit sei bei Ausschreibungen «noch wenig verankert».' The Huawei-only reading is SRF's own; the authority denies specifying the manufacturer (the entry's own evidence quote says so). Attribute the tender claim to SRF and keep only the cybersecurity concession to the authority. Also (low confidence) cash.ch says 'bereits Lücken geschlossen' (most manufacturers closed gaps), the entry writes 'manufacturers have already closed the gaps'."
- code: F4
  category: hallucinated-fact
  section: "2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat"
  item: "Linux KEV: 'not at elevated risk' and 'only confirmed-exploited attack surfaces'"
  url_or_quote: "takeaway: \"A general-purpose Linux server or workstation fleet on standard kernel patch cadence is not at elevated risk from any of the three\"; actions[0]: \"these three configurations are the only confirmed-exploited attack surfaces\""
  summary: "No source says which configurations are exploited (the entry itself says there is 'no public account of how any of them is used'), and the same takeaway opens with 'treat all three as confirmed exploited' while Red Hat says 'Address this vulnerability with high priority'. The unsupported reassurance and the 'only confirmed-exploited' clause are F4; AF_ALG availability claims ('often restricted or entirely unloaded') and the kTLS proxy/appliance prevalence are unsourced. Claim ab2f2327cc."
- code: F4
  category: hallucinated-fact
  section: "2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat"
  item: "Linux KEV: headline says Red Hat 'confirm[s] active exploitation'"
  url_or_quote: "headline: \"CISA and Red Hat confirm active exploitation of three separate Linux kernel bugs\""
  summary: "(low confidence) The quoted Red Hat words are 'This CVE is high risk and there are known public exploits leveraging this vulnerability' (public exploit code); 'acknowledge active exploitation' is THN's paraphrase, and the summary and 09-30 section say only 'public exploits exist'. The banner text is not visible in the Red Hat page bodies fetched this pass. Claim 5919082028."
- code: F3
  category: claim-not-supported
  section: "2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat"
  item: "Linux KEV: source-file and function detail not on the cited Red Hat pages"
  url_or_quote: "body: \"logic error in the kernel's TLS receive path (`net/tls/tls_sw.c`)\"; \"`crypto/af_alg.c`\"; \"`ebt_snat` target ... rather than a copy of them\""
  summary: "(low confidence) The three Red Hat CVE pages carry the descriptions but not these file paths, the target name or the 'rather than a copy' phrase (the last is closer to the KEV shortDescription). Claims b0347fcbce, 6c77ae1bf5, 49f81f3cca."
- code: F3
  category: claim-not-supported
  section: "2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited"
  item: "Cisco FMC: affected releases omit 'and earlier'"
  url_or_quote: "body: \"Affected releases are 7.0, 7.2, 7.4, 7.6, 7.7 and 10.0, regardless of how the device is configured\"; cves[].affected likewise"
  summary: "(low confidence) The advisory's fixed-release table row reads '7.0 and earlier 7.0.10', so releases before 7.0 are affected too. Claim 7b54ee35e0."
- code: F4
  category: hallucinated-fact
  section: "2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited"
  item: "Cisco FMC: static-account identity discriminator and 'incident-response case' generalisation"
  url_or_quote: "Triage: \"an authentication event for the vendor's static low-privileged account, from any source address including an internal one, has no benign explanation\"; 2026-09-30 section: \"A management server that held the static account before the hardening release is therefore an incident-response case, not only a patch item\""
  summary: "(low confidence) Cisco names neither the account nor states it has no legitimate use, and its own IOC is a package_info / /var/tmp/license.tmp log line, not authentication under the account. The KEV ransomware flag does not make every server that held the account an IR case; Cisco says the attack surface 'is reduced' without public internet access. Claims 42427de6d2, 8dee3a6dd0, 4cebbbe85b."
- code: F4
  category: hallucinated-fact
  section: "2026-05-08/dragos-2025-ot-cybersecurity-year-in-review-81-of-ir-engagem"
  item: "Dragos: headline says credentials 'behind' 73% of cases; title says 'stolen'"
  url_or_quote: "headline: \"compromised VPN or jump-host credentials behind 73% of its incident cases\"; title: \"73% of IR cases involved stolen VPN or jump-host credentials\""
  summary: "(low confidence) Dragos: '73 percent of all-time IR cases involved compromised VPN or jumphost credentials' (involvement, not cause; 'compromised', not 'stolen'). Also body: 'Windows or ESXi hosts running SCADA software are encrypted' compresses 'Windows servers hosting SCADA software or engineering workstations are compromised. Ransomware groups target VMware ESXi hypervisors hosting OT applications' (claim a32eb47307). Claim 62c1467b1c."
- code: F3
  category: claim-not-supported
  section: "2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce"
  item: "TeamCity: 'TeamCity Cloud is not affected'"
  url_or_quote: "summary: \"TeamCity Cloud is not affected.\"; cves[].affected: \"TeamCity Cloud is not affected.\""
  summary: "(low confidence) JetBrains: 'TeamCity Cloud customers are not required to take any action, as the necessary measures have already been applied' and 'no evidence of TeamCity Cloud environments being exploited'. That is remediated, not unaffected. Claims 5c0940d1e8, 2baac96882."
- code: F3
  category: claim-not-supported
  section: "2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce"
  item: "TeamCity: citation dates"
  url_or_quote: "\"[CISA KEV catalog, 2026-09-30]\" (update section) and sources[] date 2026-09-30; \"[JetBrains, 2026-09-03]\" for the Cadence post"
  summary: "(low confidence) KEV entries are dated by listing (2026-08-05, as the body's first KEV citation does; catalogVersion 2026.09.29). The Cadence post was published 2026-08-28 (article datetime) and last updated 2026-09-03. Claims 47266b4da0, 098d827b3b."
- code: F4
  category: hallucinated-fact
  section: "2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce"
  item: "TeamCity: sourcing_note still relies on a MITRE record the run removed"
  url_or_quote: "sourcing_note: \"the MITRE CVE record cited alongside it sits in JetBrains' own CNA container ... the deserialization characterisation comes from the structured record; and CISA's ADP enrichment layer on the same record, dated 2026-07-28, independently assessed exploitation status as none\""
  summary: "No MITRE/CVE record is cited any more (sources[] has JetBrains, two CISA items, the Cadence post), so these sentences describe uncited material and contradict the first sentence (CWE-502 'comes from CISA's KEV record'). Reduce the note to provenance (see F11)."
- code: F4
  category: hallucinated-fact
  section: "2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft"
  item: "Gentlemen: CVE-2025-24799 marked 'exploited'; record rationale names Japanese victims"
  url_or_quote: "cves[].status: [exploited, poc-public, patch-available]; record: \"the reconstructed intrusions targeted Japanese organizations\""
  summary: "(low confidence) Talos: 'the actor attempted to exploit CVE-2025-24799 ... using both a PoC and sqlmap to retrieve user information' (an attempt, no success stated). Talos' open-directory section names no victims or country; the Japan framing belongs to the article's incident statistics. Claims 183f52351a, f7bbb75beb."
- code: F4
  category: hallucinated-fact
  section: "2026-09-24/solarwinds-observability-cve-2026-28324-28325-unauth-rce"
  item: "SolarWinds: record says both flaws are reachable only in non-default configurations"
  url_or_quote: "record: \"priority moves from high to notable because both flaws are unexploited and reachable only in non-default configurations\""
  summary: "Release notes: CVE-2026-28324 'Installations configured in a non-default and non-secure configuration are affected'; CVE-2026-28325 'when the application is configured to use a specific communication mode' (not stated to be non-default; the same release switches default WPM players from Server-initiated to Player-initiated communication). Claim df13fb93ac."
- code: F4
  category: hallucinated-fact
  section: "2026-09-27/qbusoft-medyc-poland-healthcare-breach-fingerprint-actor"
  item: "Qbusoft: record rationale 'no named vector'"
  url_or_quote: "record: \"a Polish healthcare-software breach with no named vector, so it is awareness only\""
  summary: "The entry states the intrusion was 'via an SQL-injection vulnerability' (Inowrocław facility notice) and maps T1190. Claim 4b83205e06."
- code: F4
  category: hallucinated-fact
  section: "2026-09-29/openai-dns-tunnel-sandbox-escape-self-replicating-injection"
  item: "OpenAI: record says fetch narration was removed"
  url_or_quote: "record: \"the text carried narration about the entry itself and the fetch pipeline ... the narration is removed\""
  summary: "(low confidence) sourcing_note still reads 'independently reachable and read in full' and 'were not reachable'. Claim aae3e8d821."
- code: F4
  category: hallucinated-fact
  section: "2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev"
  item: "Citrix: headline 'no workaround exists'"
  url_or_quote: "headline: \"no workaround exists, so patch and check for compromise now\""
  summary: "(low confidence) Sources say Citrix has published no workaround (watchTowr FAQ: 'Citrix has not published a workaround'); the entry's own 09-30 section lists Mandiant's interim controls (disable DTLS, block UDP/443) for CVE-2026-88772. Claim 3b8b4f7733."
- code: F3
  category: claim-not-supported
  section: "2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev"
  item: "Citrix: two clauses cited to pages that do not carry them"
  url_or_quote: "body: \"two of which were already being exploited as zero-days before any fix existed ([Citrix])\"; \"CISA's guidance under BOD 26-04 recommends the same sequence ([CISA KEV catalog])\""
  summary: "(low confidence) The bulletin says 'Exploits ... have been observed'; 'before any fix existed' is watchTowr's wording. The KEV record carries forensicTriage 'Yes' and the BOD 26-04 reference, not the sequence 'logs, a configuration snapshot, a support bundle and a core dump' (that list is in watchTowr's FAQ, 'CISA advises ...'). Claims 48ab05cd03, cdd363ed66."
- code: F4
  category: hallucinated-fact
  section: "2026-09-22/plugin4shell-ai-coding-agent-sha-pinning-bypass"
  item: "Plugin4Shell: vendor patches asserted as fact"
  url_or_quote: "summary: \"Anthropic and OpenAI have patched\"; actions[0]: \"upgrade Claude Code to >=2.1.179 and Codex to >=0.146.0\""
  summary: "(low confidence) THN: 'Anthropic's release notes for 2.1.179 do not mention the fix, and the account that it is fixed in is Air's.' The patch status rests on the discloser alone; say so."
- code: F4
  category: hallucinated-fact
  section: "2026-09-17/kairos-libercourt-commune-ransomware-confirmed"
  item: "Kairos: takeaway asserts a shared IT-provider gap"
  url_or_quote: "takeaway: \"confirm your own externally-contracted IT provider has a documented, tested incident-detection and notification path, since that gap is what both confirmed cases share\""
  summary: "(low confidence) The Velilla statement (fetched) says no effective access or extraction can be confirmed and mentions no IT provider; the Libercourt notice says the commune's provider ran checks. Neither source identifies a detection or notification gap; 'limited in-house IT staffing' is likewise unsourced."
- code: F3
  category: claim-not-supported
  section: "2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209"
  item: "Swiss motion: Federal Council reasoning overstated"
  url_or_quote: "body: \"cited existing legal bases under the EMBAG ... and ongoing work on Swiss digital-sovereignty strategy as already covering the request\""
  summary: "(low confidence) Netzwoche: the Federal Council saw the request as 'teilweise bereits erfüllt' (partly met) and also called a Swiss solo effort unworkable. Claim 4eaed839c0."
- code: F6
  category: strengthen-primary-source
  section: "2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle"
  item: "HPE bundle: primary is a national-CERT mirror; HPE's own bulletins are fetchable"
  url_or_quote: "sources[0] NCSC-NL (role primary); sourcing_note: 'HPE's own bulletins sit behind a support-portal login and could not be retrieved'"
  summary: "Add https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05133.txt (HPESBNW05133, published 2026-Sep-01, revision 1) and https://csaf.arubanetworking.hpe.com/2026/hpe_networking_-_hpesbnw05134.txt (HPESBNW05134) as the primary sources; they carry per-CVE CVSS vectors, the 7.4.0 / 7.3.4 fixes, the 'discovered by internal security research' statement, the workaround (restrict CLI and web interfaces to a dedicated L2 segment / firewall) and the exact 10.18.0001 affected build."
- code: F5
  category: missing-citation
  section: "2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle"
  item: "HPE: fixed versions and discovery statement carry no linked source"
  url_or_quote: "body: \"Fixed in Fabric Composer 7.4.0 (or 7.3.4 for the 7.3 branch); every 7.3.3-and-earlier install is affected, all discovered by HPE's own internal Networking security research team.\"; CVE-2026-76657 / -19766 / -73701 / -73700 sentences"
  summary: "NCSC-NL's CSAF carries no version data ('vers:unknown/*') and CERT-FR carries 7.3.4 only; 7.4.0 and internal discovery appear in no linked source, and the CVE-2026-76657 clause and the 'Three more rank Critical' sentence follow the last citation. Claim df1a17236c."
- code: F6
  category: strengthen-primary-source
  section: "2026-09-24/solarwinds-observability-cve-2026-28324-28325-unauth-rce"
  item: "SolarWinds: vendor trust-center advisory is retrievable for CVE-2026-28324"
  url_or_quote: "sourcing_note: 'SolarWinds' trust-center advisory pages could not be retrieved'"
  summary: "https://www.solarwinds.com/trust-center/security-advisories/cve-2026-28324 returned the vendor advisory this pass (Severity 9.8 Critical, first published 09/22/2026, 'Observability Self-Hosted 2026.2.2 and below'); the CVE-2026-28325 page returned 403. CERT-FR links both."
- code: F5
  category: missing-citation
  section: "2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft"
  item: "Gentlemen: GLPI fix version, endpoint and CVSS are not in the only cited source"
  url_or_quote: "body: \"an unauthenticated SQL injection in GLPI's inventory endpoint (fixed in GLPI 10.0.18)\"; cves[]: cvss 7.5, affected \">= 10.0.0, < 10.0.18\", fixed 10.0.18"
  summary: "Talos gives none of these. They are correct per GHSA-jv89-g7f7-jwfg / CVE-2025-24799 (GLPI: 'unauthenticated SQL injection through the inventory endpoint ... fixed in 10.0.18', CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N) but that vendor advisory is not cited; add https://github.com/glpi-project/glpi/security/advisories/GHSA-jv89-g7f7-jwfg (F6). The sourcing_note's claim that CVE-2025-2479 is an unrelated WordPress XSS flaw is likewise uncited (true: Easy Custom Admin Bar reflected XSS)."
- code: F5
  category: missing-citation
  section: "2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat"
  item: "Linux KEV: fixed kernel builds carry no citation and CVE-2026-53266 list is incomplete"
  url_or_quote: "body: \"Fixed kernel builds: 6.1.149 / 6.6.103 / 6.12.44 / 6.16.4 / 6.17 for CVE-2025-39682; ... 5.10.259 / 5.15.210 / 6.1.176 / 6.6.143 / 6.12.94 / 6.18.36 for CVE-2026-53266.\""
  summary: "No cited page carries them. They match the kernel CNA records, but the CVE-2026-53266 record also lists 7.0.13 and 7.1 as fixed, omitted here. Claim 301d2b8656."
- code: F5
  category: missing-citation
  section: "2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited"
  item: "Cisco FMC: KEV sentence has no inline citation"
  url_or_quote: "body: \"CISA also lists the flaw in its Known Exploited Vulnerabilities catalogue, independent confirmation that the exploitation is real.\""
  summary: "KEV lists CVE-2026-20316 (dateAdded 2026-07-29), but the sentence carries no link although the KEV JSON is now in sources[] (claim 2a4a427785)."
- code: F5
  category: missing-citation
  section: "2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags"
  item: "actions-cool: scope claim for EU and Swiss organisations"
  url_or_quote: "body: \"**Why it matters to us:** EU and Swiss developer organisations using GitHub Actions for public-sector software supply chains were directly in scope during the attack window.\""
  summary: "No linked source names victims, regions or sectors. Claim 94a6f172bd."
- code: F8
  category: needs-more-research
  section: "2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags"
  item: "actions-cool: labelled lines missing"
  url_or_quote: "body has 'Why it matters to us' but no **Exposure:**, **Detection:** or **Defender takeaway:**"
  summary: "StepSecurity supports all three: exposure (any workflow referencing the action by version tag pulls the payload on its next run; only full-SHA pins are unaffected), detection (bun download to /home/runner/.bun/bin/bun, python3 child reading /proc/<Runner.Worker PID>/mem, tr/grep filtering for the secret flag, outbound HTTPS from the runner) and the Harden-Runner egress control."
- code: F8
  category: needs-more-research
  section: "2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce"
  item: "TeamCity: JetBrains' 2026-08-07 follow-up (vendor-confirmed exploitation and log indicators) is not used"
  url_or_quote: "Detection/Triage: 'Requests to the agent-polling endpoint arriving from addresses that are not your registered build agents ... any child process spawned by the TeamCity server process ...'; evidence[] still carries 'we are not aware of any active exploitation'"
  summary: "https://blog.jetbrains.com/teamcity/2026/08/cve-2026-63077-update/ ('Since our initial announcement on July 27, 2026, we have received reports of active exploitation, as well as attempted exploitation'): review server logs for com.thoughtworks.xstream.converters.ConversionException (attempted or successful exploit) and ForbiddenClassException (blocked after patching), and unauthorized build agents named 'scan*'. The primary advisory page itself now carries an 'August 7, 2026 update' banner. These vendor indicators are the honest Detection / Triage content and supersede the 'not aware' evidence quotes."
- code: F7
  category: drop
  section: "2026-09-17/kairos-libercourt-commune-ransomware-confirmed"
  item: "Kairos: routine incident with no vector, actor tradecraft or behaviour is three paragraphs"
  url_or_quote: "priority routine; body of three long paragraphs plus takeaway; sourcing_note: 'This is an out-of-nexus small foreign commune; see body for the relevance basis.'"
  summary: "Rubric 5b: an incident with no access vector, no confirmed actor and no behaviour beyond its impact is routine and two sentences at most, or dropped; the Kairos link is 'a claim, not an attribution', the Swiss-relevance paragraph is speculation ('consistent with -- though not proven to be'). Cut to two sentences or drop."
- code: F10
  category: missed-angle
  section: "2026-09-29/bitget-hot-wallet-theft-north-korea-nexus"
  item: "Bitget: Mandiant and SlowMist independent reports published 2026-09-30 name the attack path"
  url_or_quote: "priority-recalibration rationale: 'through an unnamed third-party product, with nothing the constituency can act on'"
  summary: "Bitget's incident page (updated) and https://www.bitget.com/support/articles/12560603896305 (2026-09-30): both investigations 'identified the compromise of third-party security products'; Mandiant's status report (https://img.bgstatic.com/multiLang/events/MFR26-1029_Status_Update_Bitget_0930.pdf): the actor gained privileged access to third-party security appliances A and B, deployed a web shell on appliance B, established C2, moved laterally to the production wallet job server and deployed malicious packages. That is edge-security-appliance compromise plus lateral movement, a transferable TTP the entry lacks (and it changes the 'nothing to act on' premise). Suggested search: 'Bitget Mandiant SlowMist report security appliance web shell'; append as an update."
- code: F16
  category: org-triage
  section: "2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle"
  item: "HPE bundle: priority high with no exploitation and no PoC"
  url_or_quote: "priority: high; HPE: 'not aware of any public discussion or exploit code'"
  summary: "(low confidence) Rubric 5b/F7: an unexploited management-plane bundle with no PoC does not clear `high`; the same audit moved the equally unexploited SolarWinds entry to notable. Calibrate consistently."
- code: F16
  category: org-triage
  section: "2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags"
  item: "actions-cool: priority high on a 2026-05 event"
  url_or_quote: "priority: high"
  summary: "(low confidence) A four-month-old supply-chain event with the repository already disabled and no live decision; `high` disqualifier list includes an event older than 30 days with no new development."
- code: F17
  category: classification
  section: "2026-09-17/kairos-libercourt-commune-ransomware-confirmed"
  item: "Kairos: reliability B on a lone C-tier relay"
  url_or_quote: "classification: {reliability: B, credibility: 2}; sources[0] FrenchBreaches"
  summary: "(low confidence) sources/sources.json rates FrenchBreaches C and the sourcing_note calls it the sole source for the confirmation; B is not supported by the cited source's tier."
- code: F17
  category: classification
  section: "2026-09-22/plugin4shell-ai-coding-agent-sha-pinning-bypass"
  item: "Plugin4Shell: credibility 1 on a single-discloser finding"
  url_or_quote: "classification: {reliability: B, credibility: 1}"
  summary: "(low confidence) THN, Help Net Security and heise report AIR's research; THN says the vendor fix is 'the account ... in Air's' and no vendor advisory exists, so the finding is uncorroborated by an independent assessor (2)."
- code: F8
  category: needs-more-research
  section: "2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning"
  item: "Kiteworks: vendor's only customer instruction not carried"
  url_or_quote: "takeaway: 'What remains is confirming every Kiteworks deployment ... runs release 9.5.1 or later.'"
  summary: "(low confidence) Kiteworks' own notice: 'Customers with self-hosted Advanced Forms should contact Customer Support for assistance.' Lead the takeaway with it."
- code: F8
  category: needs-more-research
  section: "2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209"
  item: "Swiss motion: National Council outcome available on the cited Netzwoche page but omitted"
  url_or_quote: "body: 'the referral status now recorded is the outcome for a motion that has cleared both parliamentary chambers'"
  summary: "(low confidence) Netzwoche's 2026-09-25 update on the cited page: National Council adopted 126 to 66 after a 13 to 12 committee vote; add it and the committee minority's 'existing legal bases suffice' argument."
- code: F11
  category: editorial-advisory
  section: "2026-09-23/cve-2026-93616-check-point-security-mgmt-path-traversal ; 2026-09-24/solarwinds-observability-cve-2026-28324-28325-unauth-rce ; 2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning ; 2026-09-04/hpe-aruba-fabric-composer-arubaos-cx-cvss10-bundle ; 2026-09-19/cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat"
  item: "Reader-facing sections narrate frontmatter edits"
  url_or_quote: "Check Point: \"The structured CVE data above marked this flaw as having no patch ... It is now marked patch-available.\"; SolarWinds: \"so the Detection line and the action no longer suggest it\"; Kiteworks: \"The title, summary and takeaway above still described the shutdown as current advice ... They now say so.\"; HPE: \"The affected field and the earlier correction now say so.\"; Linux: \"The headline, summary and main text above said ... They now say so.\""
  summary: "Field names and record-keeping narration in `## Correction` sections (rubric 12/4c-i). Keep only the cited delta (for Check Point the LivePatch-does-not-cover fact; for Kiteworks the nine-hour figure) and drop the rest or make the record internal."
- code: F11
  category: editorial-advisory
  section: "2026-09-25/switzerland-sovereign-digital-infrastructure-motion-24-3209"
  item: "Swiss motion: presentation-only Improvement section"
  url_or_quote: "## Improvement -- 2026-09-30T07:02:46Z: \"The law-firm summary of the motion quoted above is now given in English translation ...\""
  summary: "The section's only content is that a quote changed language; per 4c-i it should be an `internal: true` improvement with no body section."
- code: F11
  category: editorial-advisory
  section: "2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce ; 2026-09-17/kairos-libercourt-commune-ransomware-confirmed ; 2026-09-29/openai-dns-tunnel-sandbox-escape-self-replicating-injection"
  item: "sourcing_note carries workflow narration"
  url_or_quote: "TeamCity: \"A Cloud Security Alliance Lab Space note ... was the discovery path for this item but is an automated re-reporting pipeline\"; Kairos: \"see body for the relevance basis\"; OpenAI: \"independently reachable and read in full ... were not reachable\""
  summary: "sourcing_note should be two sentences of provenance (rubric 12); TeamCity's runs ~15 lines including discovery-path and pipeline commentary."
- code: F11
  category: editorial-advisory
  section: "2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags"
  item: "actions-cool: IOC-like commit hash and bare ATT&CK ids in prose"
  url_or_quote: "summary and body: \"imposter commit 1c9e803\"; body: \"Maps to T1195.002 ... and T1552.001\""
  summary: "The run removed the exfiltration domain as an indicator but left the imposter commit SHA; ATT&CK ids belong in techniques[] (the prose list also omits the mapped T1003.007). 'Why it matters to us' is org-voice narration."
- code: F11
  category: editorial-advisory
  section: "2026-09-26/kiteworks-precautionary-shutdown-imminent-zero-day-warning"
  item: "Kiteworks: three stacked Defender takeaway blocks"
  url_or_quote: "**Defender takeaway:** (main), **Defender takeaway (updated):** (09-29), **Defender takeaway (updated):** (09-30)"
  summary: "Rubric 4c-h: replace the original takeaway with the current one instead of stacking."
- code: F11
  category: editorial-advisory
  section: "2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev"
  item: "Citrix: second Triage line and US-directive rationale"
  url_or_quote: "**Triage:** in the main text (CVE-2026-88772: \"DTLS handling anomalies (crashes, unexpected restarts, or malformed-record errors ...)\") and a second **Triage:** in the 09-30 section (Mandiant artifacts); \"CISA's guidance under BOD 26-04 recommends the same sequence\""
  summary: "The generic 88772 discriminator is superseded by GTIG's specific log artifacts; the BOD 26-04 appeal is a US-federal directive used as justification."
- code: F11
  category: editorial-advisory
  section: "2026-09-22/plugin4shell-ai-coding-agent-sha-pinning-bypass ; 2026-09-17/ddrop-dram-interposer-defeats-confidential-computing"
  item: "Length and scope caveat"
  url_or_quote: "Plugin4Shell headline: 'zero-click plugin-marketplace takeover'; DDRop: four paragraphs at routine"
  summary: "THN's scope caveat (GitHub rejects SHA-shaped branch names; auto-update is on by default only for each agent's built-in GitHub-hosted marketplace) is in paragraph three but not in the headline or summary; DDRop's body is long for a `routine` physical-access research item."
- code: F12
  category: single-source-flag-missing
  section: "2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited"
  item: "Cisco FMC: verification value vs sources"
  url_or_quote: "verification: single-source; sourcing_note: 'CISA's KEV catalog independently lists the flaw as exploited and marks known ransomware use.'"
  summary: "(low confidence) sources[] now holds Cisco PSIRT plus the CISA KEV catalog as a second, independent record of exploitation; either set the value to match (multi-source, or single-source-national-cert wording) or stop calling CISA's listing independent."
```
