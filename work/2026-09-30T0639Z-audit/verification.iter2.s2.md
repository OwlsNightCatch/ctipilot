**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-09-30T08:44:33Z · ended_at=2026-09-30T09:13:33Z · duration_seconds=1740

## Verification report — 2026-09-30T0639Z-audit (iteration 2, slice s2)

Scope: all 423 claims in `claims.iter2.s2.yaml` (20 entries), every claim with a verdict row in `verification.iter2.s2.claims.yaml` (386 ok, 13 F3, 13 F4, 10 F5, 1 F14, 0 unreadable). Every cited page was fetched this pass (Oracle risk matrix parsed row by row: 50 unique CVEs match the entry's `cves[]` set exactly, six at CVSS 10.0; NVD, MSRC, CNA and EPSS APIs used where the cited page is a JS shell). MSRC's page itself is a JS app, so its data feed (api.msrc.microsoft.com/sug) was read instead.

### Prior-iteration remediation walk (66 items)

Confirmed correct on the sources: CVE-2026-46300 mitigation now esp4/esp6/rxrpc (Wiz code block, Help Net Security, RHSB-2026-003), no distro coverage beyond AlmaLinux/CloudLinux, no version range, Kim described as Dirty Frag discoverer, table and UAT-8616 gone; GTIG Detection matches the Remediation bullets and Figures 1-2, 'probable' gone from title/headline/summary, T1539/T1550.004 supported; node-ipc (no Vue CLI, registrar, npm audit, registry removal, DNS suffix or maintainer domain; Contradiction line faithful to Socket and StepSecurity); Cisco 'internal' gone; JFrog triage bare path and signing-key/JVM-restart text match Wiz; AEPD Hugging Face/Anthropic/OpenAI paragraph gone; Check Point Jumbo takes match sk1000155/sk1000171; Oracle monthly calendar matches the page, all 50 types null, auth-bypass tag gone, NCSC-NL 153 fixes and Kans/Schade high match the CSAF, Cl0p EBS sentence matches BleepingComputer; conference archive file names gone and Contradiction line faithful to both Huntress pages; NightEagle T1053.005, KEV cited, file names replaced; TraderTraitor evidence[2] verbatim; Arista PSK hedged and labelled lines separated; NCSC-CH 'unmodifiable' gone; Virtualizor CVSS removed. The 2026-09-27 conference section decline holds (earlier run's non-internal record).

Remediations that introduced or left a defect: JFrog actions[0]/immediate_action (F4 below), CVE-2026-32202 not yet carrying MSRC's July re-release (F4 below), AFPA headline untouched (F4 below), AEPD title untouched (F14), Pentagon trim does not cure the incident floor (F7), Check Point Triage (F3), the 'withdrawn' wording on CNA/NVD-published scores in three entries (F4/F9).

### Citation does not support the claim

**#1 (F3) 2026-09-18/cve-2026-91843 (Triage line)** — cve-2026-91843
- Claim: "**Triage:** Check Point treats an over-long-username login that coincides with an FWM or MDS core dump as a potential exploitation attempt ([Check Point Support, sk1000171, 2026-09-20](...))"
- (low confidence) sk1000171 (https://support.checkpoint.com/results/sk/sk1000171/) is the CVE-2026-93616 advisory; its "potential attempt to exploit this vulnerability" is that other CVE. The Detection line says so, the Triage line under CVE-2026-91843 does not. sk1000155 offers only the "Username too long" message. Name the CVE in the Triage line. Claim b83146da79.

**#2 (F3) 2026-09-18/cve-2026-91843 (Correction section; headline)** — cve-2026-91843
- Claim: section: "...CVE-2026-93616, a separate pre-authentication path traversal in the same Security Management, Multi-Domain, Log and SmartEvent servers, which Check Point says was exploited ... ([The Hacker News, 2026-09-22])" / headline: "An oversized username in Check Point's management login reaches root"
- (low confidence) THN says "Check Point's advisory names only Security Management as affected"; the Log/Multi-Domain/SmartEvent scope is in sk1000171, not the THN citation. sk1000155 states only the "Username too long" attack indicator, not that an oversized username is the trigger (the summary words it correctly; the headline states the trigger as fact). Claim cc73e2647c.

**#3 (F3) 2026-09-12/jfrog-artifactory (body)** — cve-2026-42016-42018
- Claim: "...so a low-privileged token can be exchanged for one carrying administrative authority ([JFrog, 2026-07-27])" and "lists 7.111.20, 7.117.27, 7.125.19, 7.133.28 and 7.146.8 as both the last affected and the patched build"
- (low confidence) JFrog's page says only "vulnerable to a privilege escalation attack due to a validation check of the token signature/issuer and not the token's scope"; the exchange-for-admin mechanism is Wiz's. JFrog row 1 reads "< 7.111.20" affected, so 7.111.20 is not a last-affected build (true for the other four). Claims a4075687fa, c906ccb193, 3af2ad78cf.

**#4 (F3) 2026-09-17/aepd (body)** — aepd
- Claim: "AEPD's deputy director Francisco Pérez Bes frames the change as one of speed and autonomy rather than a new technique ([heise online, 2026-09-16])"
- (low confidence) heise says the change is "qualitative" and "primär die Geschwindigkeit"; "rather than a new technique" is AEPD's own line ("la IA no crea nuevas amenazas"), not on heise. Cite AEPD. Claim 3140b594e9.

**#5 (F3) 2026-09-20/oracle-september-2026 (body)** — oracle-september-2026
- Claim: "Oracle discloses no exploitation technique, no proof-of-concept status and no in-the-wild activity for any of the fifty unauthenticated flaws, which is its standing advisory practice"
- (low confidence) The Oracle page contains nothing about a standing practice. Claim a9a96d8609.

**#6 (F3) 2026-09-21/nighteagle (summary)** — nighteagle
- Claim: "...to expose RDP outward without opening new firewall ports"
- (low confidence) Kaspersky: "maintain network access by using legitimate services without opening additional suspicious ports" (the body words it correctly). Claim 0215919a88.

**#7 (F3) 2026-09-21/tradertraitor (body)** — tradertraitor
- Claim: "A third stage later replaced both original implants and kept beaconing to a separate C2 for over a month before going silent."
- (low confidence) SentinelLabs' timeline ends with "Final loginwindow beacon ... in the collected telemetry" (2026-06-01); it does not say the implant went silent. Claim e5372acaaa.

**#8 (F3) 2026-09-23/virtualizor (body)** — virtualizor
- Claim: "All three were confirmed exploitable on Virtualizor 3.2.9 patch 7 and patch 8."
- (low confidence) VulnCheck: "Everything below is confirmed on 3.2.9 patch 7"; patch 8 is stated vulnerable from decoded source in the 2026-09-20 re-test. Claim 2d5d29bff9.

**#9 (F3) 2026-09-27/pentagon-dmdc (body)** — pentagon-dmdc
- Claim: "...exposing each affected person's Social Security number plus at least one further identifying field" / takeaway "...keep access logs that can show, after the fact, who read which records and when ([CNN])"
- (low confidence) Military Times: the notification says the unauthorized users gained "the Social Security number of the letter's recipient, as well as at least one additional piece of identifying information" (one letter, not each affected person). CNN says the data was unencrypted and "Encrypting sensitive data is a standard security practice"; it says nothing on access logs. Claims be7f85b583, ce76d753db.

**#10 (F3) 2026-05-15/cve-2026-46300 (2026-09-05 Update section)** — cve-2026-46300
- Claim: "CVE-2026-46300 now carries a published score, CVSS 7.8 ([Red Hat Product Security, 2026-05-13])"
- (low confidence) The citation was swapped this run from the MITRE record (2026-09-01) to a Red Hat page dated 2026-05-13, so "now carries a published score" (a 2026-09-05 statement) sits on a source four months older. Reword ("Red Hat rates it CVSS 7.8").

**#11 (F3) 2026-09-21/conference-phishing (body)** — conference-phishing
- Claim: "...beaconing every action through the Telegram Bot API"
- (low confidence, trivial) Huntress recap says "the Telegram API". Claim e1273c6332.

### Unsupported / hallucinated facts

**#12 (F4) 2026-05-08/cve-2026-32202 (Exposure + Defender takeaway)** — cve-2026-32202
- Claim: "supported Windows 10, 11 and Windows Server builds without the April 2026 update" / "Install the April 2026 updates and block outbound SMB"
- MSRC's own record (https://api.msrc.microsoft.com/sug/v2.0/en-US/vulnerability/CVE-2026-32202, the data behind the cited MSRC page) carries revision 2.0 of 2026-07-28: "This CVE has been re-released to comprehensively address the vulnerability identified by CVE-2026-32202. Microsoft recommends installing the July 2026 updates for your Windows operating systems." The entry cites MSRC as primary yet tells readers to install only the April update. State Microsoft's July 2026 re-release recommendation (Help Net Security 2026-04-29 predates it) in Exposure and takeaway. Claims a0c5f1215f, 8a20872dcc.

**#13 (F4) 2026-09-12/jfrog-artifactory (actions[0]; immediate_action)** — cve-2026-42016-42018
- Claim: actions[0]: "These builds are above 7.133.11, which closes CVE-2026-42016, and one above the builds JFrog's CVE-2026-42018 table names as patched, so the higher build closes both halves of the chain." immediate_action: "JFrog's own CVE-2026-42018 table names a build one lower as patched, so take the higher build."
- Wiz's builds are 7.111.21, 7.117.28, 7.125.20, 7.133.29, 7.146.38, 7.161.20. Three of the six (7.111.21, 7.117.28, 7.125.20) are numerically below 7.133.11, so "These builds are above 7.133.11" is false for them. JFrog's CVE-2026-42016 advisory (https://docs.jfrog.com/releases/docs/jfrog-security-advisories) lists Affected "< 7.133.11", Patched "7.133.11" and "Upgrade ... to a fixed version applicable to your release branch: 7.133.11", so a 7.111/7.117/7.125 instance moved to Wiz's branch build is still inside JFrog's affected range for CVE-2026-42016. "One above/one lower" is also wrong for 7.146.38 vs JFrog's 7.146.8 (30 apart) and 7.161.20 (no JFrog counterpart). The pre-run text (git HEAD) said "7.133.11 for CVE-2026-42016, and the CVE-2026-42018 fix matching your branch" and warned that a build above 7.133.11 numerically can still be unpatched for the second CVE; this run's rewrite dropped the 7.133.11 requirement and introduced the false statement. Restore: >= 7.133.11 for CVE-2026-42016 and the branch build for CVE-2026-42018. Claims 98945dd372, d629b0bb7a.

**#14 (F4) 2026-09-21/afpa-third-party-accommodation-tool-data-extraction (headline)** — afpa
- Claim: "AFPA confirms a breach in a vendor-hosted tool after two criminal claims a day apart point to the same third-party flaw"
- Both cited pages say the opposite. Cyberattaque.org: "sans toutefois établir à ce stade si les deux bases revendiquées par Cybernox et xMetah proviennent exactement du même environnement"; Clubic: "l'Afpa n'a pas établi si les deux jeux de données ont été extraits d'un environnement unique", and xMetah gave no method (Cyberattaque.org: "xMetah ne précisait ni ... la méthode utilisée"). Only AFPA's own (hedged) statement ties the extraction to the accommodation tool. Fix the headline.

**#15 (F4) 2026-05-16/gtig-unc6671 (frontmatter sectors)** — gtig-unc6671
- Claim: sectors: [finance, technology, healthcare]
- The GTIG post (https://cloud.google.com/blog/topics/threat-intelligence/blackfile-vishing-extortion-operation/) names no victim sector: it says only "dozens of organizations across North America, Australia, and the UK" (search of the page text for financ/health/sector/industr/technology returns nothing). Empty the field or source it.

**#16 (F4) 2026-05-16/gtig-unc6671 (record summary)** — gtig-unc6671
- Claim: "...No analytic claim changes. The entry also gains the source rating and ATT&CK mapping..." followed by "GTIG's leak-site assessment is corrected from probable rebrand to a possible transition phase, and the detection guidance now follows GTIG's own"
- (low confidence) The record summary says no analytic claim changes and then lists corrected analytic claims (rebrand assessment, detection guidance, token-theft mapping, priority), and it lists more than the Correction section states (4c-d). Remove the false sentence. Claim d11bf70aab.

**#17 (F4) 2026-05-16/node-ipc (record summary)** — node-ipc
- Claim: "...No analytic claim changes. ... Unsourced claims are removed (a named registrar, Vue CLI and webpack dependents, registry removal of the versions, and an npm audit bypass)..."
- (low confidence) Same self-contradiction: analytic claims are removed and a contradiction statement added, yet the summary says no analytic claim changes. Claim 8e1e252a32.

**#18 (F4) 2026-09-12/jfrog-artifactory (Correction section)** — cve-2026-42016-42018
- Claim: "JFrog rates both flaws High without a numeric score, so the CVSS 8.1 and 7.5 figures shown earlier are withdrawn"
- (low confidence) JFrog's advisory page carries no score, but the CNA record does: https://cveawg.mitre.org/api/cve/CVE-2026-42016 has cvssV3_1 baseScore 8.1 and CVE-2026-42018 has 7.5 (fetched this pass). "Withdrawn" tells readers the figures were invalid; they are JFrog's own CNA scores. Say the figures come from the CVE record rather than a citable advisory page, or drop them silently. Claim 869d197650.

**#19 (F4) 2026-09-23/virtualizor (Correction section + record summary)** — virtualizor
- Claim: "VulnCheck's disclosure gives no CVSS scores for the three flaws, so the scores shown earlier are withdrawn." / record summary: "CVSS scores that no readable source publishes"
- (low confidence) NVD's CVE API record for CVE-2026-43641/-43642/-43643 (fetched this pass, source disclosure@vulncheck.com, i.e. VulnCheck as CNA) carries CVSS 3.1 9.8 / 8.1 / 7.5 and CVSS 4.0 9.3 / 9.2 / 8.7, the values the entry showed before. "No readable source publishes" is false and "withdrawn" misstates them. Claims 8bffabd02b, 053cb85a6a.

**#20 (F4) 2026-09-04/cve-2026-20212-cisco-nexus (Correction section)** — cve-2026-20212
- Claim: "...in the default Layer 3 VRF, where Cisco says the ports are reachable, not on management or control-plane VRF interfaces"
- (low confidence) The advisory (https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-n9k-s1-rce-EH8dEtr) says only that TCP 43210/43211 "are accessible in the default Layer 3 (L3) virtual routing and forwarding (VRF)"; it does not say management or control-plane VRF interfaces are unaffected, and its iACL workaround speaks of "required management and control plane traffic". The exclusion is the entry's inference. Claim 0302fcc971.

**#21 (F4) 2026-09-23/cve-2026-93952-arista (tags)** — cve-2026-93952
- Claim: tags: [..., default-config]
- (low confidence) Arista: "VCO is exposed if certificate based authentication ... is configured"; the body itself says "Exposure is configuration-dependent", and THN contrasts the July flaw ("VCO was exposed to it by default"). The default-config tag contradicts the body.

**#22 (F4) 2026-09-23/ncsc-ch-google-recovery-oauth-app-password (title; body)** — ncsc-ch-google-recovery
- Claim: title: "...plants an OAuth app-password backdoor..." / body: "...which relays entered credentials to the attacker in real time"
- (low confidence) BACS (https://www.bacs.admin.ch/de/26w38-de) describes an app password as "ein spezieller Zugangscode für ältere Anwendungen" and never mentions OAuth (the entry's own summary calls it a legacy credential). On the phishing page BACS says the form sent credentials "direkt an die Täter", not in real time. Claim 03280d7fa0.

**#23 (F4) 2026-09-21/afpa (body, summary, title)** — afpa
- Claim: "AFPA traced the extraction to a flaw in a third-party-hosted tool it uses to manage worker accommodation"
- (low confidence) Clubic/Cyberattaque.org: "outil de gestion des hébergements" (no "worker"), and Clubic stresses AFPA's wording is cautious ("potentielle extraction", the link with the flaw "serait" établi). "Traced" and "worker" drop the hedge and add a detail. Claim b7bd1e2024.

**#24 (F4) 2026-09-21/conference-phishing (summary; title)** — conference-phishing
- Claim: summary: "...targeted post-conference by a fake CoinDesk executive persona over a compromised Google Doc..." / title: "self-regenerating rogue root CA"
- (low confidence) Both Huntress pages call it "a legitimate Google Doc" with a custom Apps Script sidebar (the body agrees); nothing says the doc was compromised. Huntress says the CA is "generated fresh on every host" / "regenerated per host", not self-regenerating. Claim c45b65650b.

**#25 (F4) 2026-09-20/oracle-september-2026 (Defender takeaway)** — oracle-september-2026
- Claim: "...the exposure that turns a Privileges Required None flaw into a single-request compromise."
- (low confidence) The Correction section itself says Oracle gives no vulnerability class or mechanism; "single-request compromise" asserts an undisclosed mechanism. Claim 823c3e21cd.

**#26 (F4) 2026-09-23/virtualizor (summary)** — virtualizor
- Claim: "...built a fully automated internal exploit module — using its own open-source go-exploit framework, not published for this CVE..."
- (low confidence) VulnCheck's post says only "turned finding 1 into a self-contained go-exploit module"; it neither calls it internal nor says it is unpublished (the body correctly says the post "does not state" it was released).

### Claims missing inline citation

**#27 (F5) 2026-09-12/jfrog-artifactory (kill-chain, post-exploitation and patch-velocity paragraphs)** — cve-2026-42016-42018
- Claim: "Wiz observed actors reach a created administrator account in under five minutes..." / "Across multiple cases Wiz observed a custom Rust-based backdoor..." / "Wiz's own patching-velocity data ... 67% ... 59% ... 62% ... 49%"
- (low confidence) The facts are on the Wiz page but these sentences carry no Wiz link; the kill-chain paragraph's only link is the CISA KEV feed and the other two paragraphs have none. Claims 61ea9edbf0, 80fbc46eb6, 49d0c7c1d7, cabdd1ec49, 79125ad434, a079a4df7a, cb83b9d875, e8e5d5e7fa.

**#28 (F5) 2026-09-18/cve-2026-91843 (body)** — cve-2026-91843
- Claim: "The management login service should not normally be internet-facing, ... the box that holds every firewall policy and credential in the fleet..."
- (low confidence) Uncited characterization; sk1000155 only says to limit Trusted Clients. Claim 38e3e5492f.

**#29 (F5) 2026-09-23/virtualizor (Detection concept paragraph; Triage)** — virtualizor
- Claim: "Detection concept: on any self-managed Virtualizor installation, monitor admin-panel access logs ... act=login ... billing_data ..."
- (low confidence) Derived from the VulnCheck exploit request but carries no citation. Claim 1a4a96dc2c.

**#30 (F5) 2026-05-15/cve-2026-46300 (2026-09-05 Update, Detection line)** — cve-2026-46300
- Claim: "...(governed by seccomp, pod security policy and user-namespace settings)..." and the whole **Detection:** paragraph
- (low confidence) Supported by the Aikido page already listed in sources[] (https://www.aikido.dev/blog/dirty-frag: uname -r vs distro fixed version, lsmod, RuntimeDefault seccomp, restricted pod policies, user namespaces) but uncited in the text.

### Drop (low relevance / off-audience / duplicate)

**#31 (F7) 2026-09-27/pentagon-dmdc-military-personnel-data-breach-unencrypted-ssn** — pentagon-dmdc
- Claim: "It is relevant for its global significance to any central personnel-data store: nine months of access to unencrypted national identity numbers went unnoticed"
- US-only military personnel incident with no vector, no actor and no behavior (sources: "It's unclear who was behind the breach"; "no report names a vulnerability class, access vector or actor"), i.e. the incident floor (routine, two sentences at most, or dropped). After the trim the body is still three sentences plus a takeaway, and the untrimmed 2026-09-30 Update section adds a four-sentence paragraph; the count of affected people is the reason it is kept, and "global significance" is asserted, not shown. Iteration 1 recommended drop; the trim does not cure it. Main-agent decision: drop, or cut body+Update to two sentences.

### Surface contradiction

**#32 (F9) 2026-08-10/coding-agent-ci-harness (Correction 2026-09-30)** — coding-agent-ci-harness
- Claim: "The 7.8 rating with a local, user-interaction vector reported earlier is withdrawn: Google's advisory gives only the network-reachable 10.0 rating."
- (low confidence) NVD's CVE API record (https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2026-12537, fetched this pass) still carries a primary CVSS 3.1 score of 7.8 (AV:L/UI:R) next to the CNA's CVSS 4.0 10.0. The two official ratings diverge; "withdrawn" reads as the 7.8 being wrong. State the divergence (attributed to the NVD record) or drop it without the word withdrawn. Claim c9ea08044d.

**#33 (F9) 2026-09-21/afpa (body)** — afpa
- Claim: "...claimed 971,420 and 1,732,811 records on 2026-09-15 and 2026-09-16"
- (low confidence) Clubic (relaying AFP and AFPA's deputy director) says the two hackers claimed "mercredi et jeudi" (2026-09-16 and 2026-09-17); Cyberattaque.org puts Cybernox on 16 Sept and xMetah 24 h earlier. The entry cites all three and picks 15/16 silently. Claim 457636e70c.

### Editorial / less-is-more flags (advisory)

**#34 (F11) 2026-05-08/cve-2026-32202 (title)** — cve-2026-32202
- Claim: title: "CVE-2026-32202 — Windows Shell: an incomplete fix for an APT28-exploited LNK flaw ..."
- The title this run rewrote keeps an em dash (reader-facing text; only the ## section heading is exempt). Same for the untouched node-ipc title.

**#35 (F11) em dashes in paragraphs the run edited** — multiple
- Claim: e.g. cisco-n9k "affected — Cisco names ten..."; jfrog "administrative control — Wiz Research states"; ncsc-ch "number — surviving Switzerland's"; virtualizor (six occurrences); cve-2026-46300 Update "...(dirty-frag)) — any RHEL"; coding-agent Round 1 paragraph
- Pre-existing em dashes survive inside paragraphs that this run rewrote and re-cited; the style rule bans them in reader-facing text.

**#36 (F11) pipeline-style narration in reader sections** — multiple
- Claim: afpa Correction: "The AFPA breach is reduced to an awareness item..." / pentagon Correction: "The DMDC breach is reduced to an awareness item..." / oracle Update 2026-09-29: "Re-fetching Oracle's own September 2026 risk matrix confirms..."
- These sections narrate the entry's own editorial status or a counting pass rather than a source-cited delta; the afpa and pentagon sections restate the body. Trim to the reader delta.

**#37 (F11) 2026-09-23/ncsc-ch (record type)** — ncsc-ch-google-recovery
- Claim: type: improvement; summary: "No claim changes. A sentence claiming the rest of Google's email cannot be altered by the attacker is narrowed to what BACS states."
- The section retracts a previously made claim, so this is a correction, and the summary contradicts itself (4c-i).

**#38 (F11) 2026-08-10/coding-agent-ci-harness (record summary)** — cve-2026-12537
- Claim: "The 10.0 now cites Novee's reading of Google's advisory and the vector and fixed versions cite the GitHub advisory record via OSV; ... The rating, vector and fixed versions now cite Google's own advisory, with OSV kept for the CVE alias"
- The record summary states two different citation outcomes; keep only the final one. Claim 8e6c41b58a.

**#39 (F11) 2026-09-21/tradertraitor (body)** — tradertraitor
- Claim: "(named Northwind-IAC, novacart-interview, terraform-candidate-repo)"
- Attacker-chosen repository names are kept while payload archive names were removed elsewhere in the run as IOC-like; drop for consistency.

### Quantifier without source

**#40 (F14) 2026-05-15/cve-2026-46300 (Correction section)** — cve-2026-46300
- Claim: "At disclosure only AlmaLinux and CloudLinux had shipped patched kernels ([Help Net Security, 2026-05-14])"
- (low confidence) Help Net Security: "Some Linux distributions have already relased kernel patches, namely AlmaLinux and CloudLinux" (an example list, not "only"); Microsoft's 2026-05-14 update says "A patch is available". The body version ("AlmaLinux and CloudLinux had released patched kernels") is fine. Claim 961de2669f.

**#41 (F14) 2026-09-17/aepd (title, unchanged by the run)** — aepd
- Claim: title: "Spain's AEPD discloses the first GDPR breach notification attributed to an autonomous AI agent"
- AEPD: "ha recibido la primera notificación" (its first); the run's own Correction section says "the first breach notification of its kind that it has received". The title still reads as a global first and contradicts the corrected body (4c-h).

### Org-triage line missing / inconsistent

**#42 (F16) 2026-09-20/oracle-september-2026 (priority: high)** — oracle-september-2026
- Claim: priority: high
- (low confidence) 5b: no exploitation, no KEV listing, no PoC, a routine third-Tuesday vendor release; the only urgency argument is scheduling ("an off-quarter release that a quarterly patch calendar does not schedule"). The rule text says a routine patch-cycle CVE with no exploitation "high CVSS alone included" does not clear the high bar. Consider notable.

### Verdict

NEEDS_FIXES (truth: 28, editorial: 8, advisory: 6)

Firm findings (fix before publish): CVE-2026-32202 April-vs-July update (F4), JFrog fixed-build statement (F4), AFPA headline (F4), GTIG sectors (F4), Pentagon keep-or-drop (F7). The remaining items are marked (low confidence) and are ordered by how cheaply they can be fixed.

Coverage/missed angles: not assessed for this slice (correction run over existing entries); no missing in-window story is claimed.

### Findings summary (machine-readable)

See `work/2026-09-30T0639Z-audit/verification.iter2.s2.findings.yaml` (42 records).
