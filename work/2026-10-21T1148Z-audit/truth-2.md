**Model:** Opus 5.5 (`claude-opus-5-5`); entries 1-7 and the start of entry 8 ran on Sonnet 5.5 (`claude-sonnet-5-5`) before a session-limit resume
**Timestamps:** started_at=2026-10-21T12:02:30Z · ended_at=2026-10-21T15:51:52Z · duration_seconds=13762

# Truth pass batch 2 (run 2026-10-21T1148Z-audit)

16 entries checked, 247 claim rows (truth-2.claims.yaml). Verdicts: 15 factual-error, 1 imprecision, 0 clean. Duplicate groups: none (TeamPCP cluster decision at the end).

Unreadable on every rung: hub.ivanti.com advisories (JavaScript shell for extract, WebFetch and jina; facts read from ENISA EUVD and the Ivanti CNA records), Computable 2026-05-13 (HTTP 503 on extract, url, jina and WebFetch), Fedora bodhi (bot wall), Lenovo LEN-216977 body. Upgrade-block quotes may contain file paths and a spoofed commit author: the repair worker must not copy indicators into entries.

## 2026-05-12/teampcp-unc6780-pcpjack-ecosystem-backdoors-the-checkmarx-je (factual-error)

1. **factual-error**, cves[CVE-2026-33634]; body paragraph 2 ('a CVE has been issued as CVE-2026-33634 per the Checkmarx advisory')
   - Claim: "id: CVE-2026-33634, cvss: "9.4", status: [exploited, patch-available], auth: pre-auth, vector: zero-click"
   - Defect: CVE-2026-33634 is the Aqua Security Trivy embedded-malicious-code CVE from March 2026, not a CVE for the Checkmarx Jenkins plugin; the Checkmarx page names no CVE at all, so the body sentence attributing it to 'the Checkmarx advisory' is false and the cves[] record binds the wrong flaw.
   - Ground truth: GHSA-69fq-xp46-6x23 is titled 'CVE-2026-33634' and reads 'On March 19, 2026, a threat actor used compromised credentials to publish a malicious Trivy v0.69.4 release, force-push 76 of 77 version tags in aquasecurity/trivy-action to credential-stealing malware'. CISA KEV lists CVE-2026-33634 as 'Aquasecurity Trivy Embedded Malicious Code Vulnerability', dateAdded 2026-03-26. The Checkmarx page contains no 'CVE' string. (https://github.com/advisories/GHSA-69fq-xp46-6x23)
   - Fix: Delete the cves[] record and the body sentence; no source read assigns a CVE to the Jenkins build 2026.5.09. If kept for context, say only that the credentials came from the March Trivy compromise (CVE-2026-33634), per Checkmarx: 'This access occurred on March 19, 2026 due to the Trivy Supply Chain Attack'. kind: vulnerability then no longer fits (threat or incident).
2. **factual-error**, headline; summary; body paragraphs 1-3 (SANDCLOCK)
   - Claim: "Malicious plugin build 2026.5.09 ... deploys SANDCLOCK to exfiltrate every CI secret reachable from the runner"
   - Defect: None of the three cited pages (nor BleepingComputer, SOCRadar) names SANDCLOCK for the Jenkins build; GTIG ties SANDCLOCK to the late-March Trivy, Checkmarx, LiteLLM and BerriAI compromises, and Checkmarx describes the May payload without naming it.
   - Ground truth: GTIG (2026-05-11): 'In late March 2026, ... TeamPCP (aka UNC6780) claimed responsibility for multiple supply chain compromises ... including those associated with the Trivy vulnerability scanner, Checkmarx, LiteLLM, and BerriAI ... embed the SANDCLOCK credential stealer'. Checkmarx on the May build: 'The malicious payload associated with the modified plug-in targets lists of file paths for common applications ... We are still conducting malware analysis'. (https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)
   - Fix: Drop SANDCLOCK from headline, summary and body, or state it only as GTIG's name for the stealer used in the March compromises, with the GTIG URL as the citation.
3. **factual-error**, summary; body paragraph 2 (list of targeted secrets); defender pivot ('audit Checkmarx One API logs')
   - Claim: "SANDCLOCK targets every secret reachable from a typical CI/CD pipeline environment: GitHub Personal Access Tokens, AWS / Azure / GCP credentials, Kubernetes service-account tokens, Docker / OCI registry credentials, SSH keys, and Checkmarx One API tokens."
   - Defect: No page read lists these targets for the Jenkins build; Checkmarx names a narrower set and says no threat-actor access to the Checkmarx One SaaS environment was found, so 'Checkmarx One API tokens' and container-registry credentials are unsupported.
   - Ground truth: Checkmarx: 'it traverses the corresponding file list looking for credentials. Targeted applications include crypto wallets, VPNs, AWS, and Github ... to date we have not seen any references to Jenkins.' and 'There was no threat actor access to the Checkmarx One SaaS environment'. (https://checkmarx.com/blog/ongoing-security-updates/)
   - Fix: State Checkmarx's list (file-path sweep for credentials of crypto wallets, VPNs, AWS and GitHub, per OS) and Checkmarx's advice to rotate 'all credentials that the pipeline that executed the malicious payload has access to'; remove the Checkmarx One API token claim and the Checkmarx One log-audit pivot.
4. **factual-error**, body paragraph 2 (third compromise sentence)
   - Claim: "after the March 2026 KICS Docker image and the April 2026 VS Code extension defacement"
   - Defect: Chronology is wrong: the KICS Docker image belongs to the April wave, and the March wave was malicious GitHub Actions and Open VSX extensions; the repository defacement belongs to the May Jenkins incident, not April.
   - Ground truth: Checkmarx timeline: '23-Mar-2026 ... malicious GitHub Actions & VSCode extensions to OpenVSX'; '22-Apr-2026 Second Wave Artifacts: Cached credentials enable publication of malicious KICS Docker image, updated VSCode & DevAssist extensions, and GitHub Action'; '9-May-2026 Jenkins Plugin Compromise'. BleepingComputer: 'This is the third incident in a series of supply-chain attacks the application security testing firm has suffered since late March.' (https://checkmarx.com/blog/ongoing-security-updates/)
   - Fix: Write: third Checkmarx artifact compromise since late March (March GitHub Actions and Open VSX extensions; April KICS Docker image, extensions and GitHub Action; May Jenkins plugin), cited to the Checkmarx timeline. 'In three months' is calendar-month rounding of a roughly six-week span.
5. **factual-error**, body paragraph 3 (GTIG sentence)
   - Claim: "The GTIG AI Threat Tracker ( attributes SANDCLOCK specifically to TeamPCP and flags the stealer as explicitly designed to harvest **LLM API keys** in addition to traditional cloud credentials"
   - Defect: GTIG does not say SANDCLOCK is designed to harvest LLM API keys; it says the LiteLLM compromise could expose AI API secrets. The inline link is also empty ('(' with no URL).
   - Ground truth: GTIG: 'embed the SANDCLOCK credential stealer and extract high-value cloud secrets, such as AWS keys and GitHub tokens' and, of LiteLLM, 'this incident could lead to considerable exposure of AI API secrets from affected victims'. (https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)
   - Fix: Restate as GTIG does (stealer harvests cloud secrets such as AWS keys and GitHub tokens; the LiteLLM compromise could expose AI API secrets) and give the GTIG URL; drop 'explicitly designed to harvest LLM API keys' and the 'pivot to monetising stolen LLM access' inference.
6. **factual-error**, headline; body opening ('PCPJack worm ... same actor ecosystem'); entities tool:pcpjack-cloud-worm-2026
   - Claim: "TeamPCP (UNC6780 / PCPJack ecosystem) ... this is a distinct new artefact in the same actor ecosystem"
   - Defect: PCPJack is a separate cloud worm whose first act is to evict TeamPCP tooling; SentinelLABS only speculates its operator 'could be a former operator', and no cited page links PCPJack to the Checkmarx Jenkins incident.
   - Ground truth: SentinelLABS: 'the script's first actions are to evict and delete tools associated with the TeamPCP attack group, leading us to call the toolset PCPJack' and 'We believe this could be a former operator who is deeply familiar with the group's tooling.' (https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/)
   - Fix: Remove 'PCPJack ecosystem' from headline and body and the PCPJack entity link from this entry; if mentioned, say PCPJack is a distinct worm that removes TeamPCP infections (SentinelLABS).
7. **imprecision**, body paragraph 1 ('marketed under the actor's signature naming')
   - Claim: "version 2026.5.09, marketed under the actor's signature naming "Checkmarx-Fully-Hacked-by-TeamPCP""
   - Defect: The defacement name was given to the plugin's GitHub repository, not to the plugin build; the name quoted is also truncated.
   - Ground truth: THN: TeamPCP 'renamed it to "Checkmarx-Fully-Hacked-by-TeamPCP-and-Their-Customers-Should-Cancel-Now."' (the plugin's GitHub repository) with the description 'Checkmarx fails to rotate secrets again. with love - TeamPCP.' (https://thehackernews.com/2026/05/teampcp-compromises-checkmarx-jenkins.html)
   - Fix: Say the plugin's GitHub repository was renamed and defaced, separately from the malicious build 2026.5.09.
8. **imprecision**, body paragraph 1 ('configured to auto-update'); summary ('auto-updated')
   - Claim: "Any Jenkins instance configured to auto-update the AST plugin during that window pulled the malicious build"
   - Defect: No page says exposure required auto-update configuration; Checkmarx gives an exposure window and SOCRadar says any instance 'that pulled this version'.
   - Ground truth: Checkmarx: 'The malicious window was 2026-05-09 01:25 UTC to 2026-05-10 08:47 UTC.' SOCRadar: 'Any Jenkins instance that pulled this version during the exposure window would have installed a compromised plugin.' (https://checkmarx.com/blog/ongoing-security-updates/)
   - Fix: Write 'any instance that installed or updated to build 2026.5.09 between 2026-05-09 01:25 UTC and 2026-05-10 08:47 UTC'.
9. **imprecision**, headline; summary; body paragraph 1 (attribution stated as fact)
   - Claim: "On 2026-05-09-10 (UTC) TeamPCP (UNC6780) published a backdoored build of the Checkmarx Jenkins AST plugin"
   - Defect: The May attribution rests on the repository defacement and researcher statements; Checkmarx's own May row names only 'External service account'; the UNC6780 designation comes from GTIG's March-activity report.
   - Ground truth: THN: 'TeamPCP is said to have gained unauthorized access to the plugin's GitHub repository' per Adnan Khan and SOCRadar. BleepingComputer: 'The compromise was claimed by the TeamPCP hacker group.' Checkmarx timeline: '9-May-2026 Jenkins Plugin Compromise: External service account modified Jenkins AST plugin and published to Jenkins Marketplace'. (https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/)
   - Fix: Write 'TeamPCP claimed (defacement) and researchers attribute ...; Checkmarx says credentials from the March Trivy compromise were reused'.
10. **imprecision**, body opening; evidence[0]; sourcing_note
   - Claim: "UPDATE (TeamPCP / mini-shai-hulud first covered 2026-05-07; PCPJack worm covered 2026-05-10; this is a distinct new artefact in the same actor ecosystem)"
   - Defect: Pipeline self-reference in reader text; evidence[0] quotes 'ctipilot v2 brief (migrated)' (the pipeline quoting itself); the claimed 2026-05-07 and 2026-05-10 coverage entries do not exist in the store for PCPJack.
   - Ground truth: grep of entries/ finds 'PCPJack' only in this entry. (work/2026-10-21T1148Z-audit/truth-2/bodies/e1-s1-pcpjack.txt)
   - Fix: Remove the UPDATE preamble and the self-quoting evidence record; replace with a verbatim Checkmarx or BleepingComputer passage.

## 2026-05-13/microsoft-mdash-multi-model-agentic-vulnerability-discovery (factual-error)

1. **imprecision**, body paragraph 1 (benchmark sentence citation)
   - Claim: "The harness scored 88.45% on the public CyberGym benchmark (1,507 real-world CVEs across 188 open-source projects) and achieved 100% recall on the `tcpip.sys` historical-CVE corpus ([The Register, 2026-05-13]"
   - Defect: The Register article carries none of these figures (it only says MDASH found 16 of the May vulnerabilities and is in limited private preview); they are on Microsoft's own blog, and the entry drops the sample size and the clfs.sys result.
   - Ground truth: Microsoft: 'the Microsoft Security multi-model agentic scanning harness reaches an 88.45% success rate' on CyberGym, 'a corpus of 1,507 real-world vulnerability reproduction tasks drawn from across 188 OSS-Fuzz projects'; 'tcpip.sys: 100% recall on 7 MSRC cases spanning five years'; 'clfs.sys: 96% recall on 28 MSRC cases'; 'retrospective recall benchmarks on internal code with a finite case count'. (https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-finds-16-new-vulnerabilities/)
   - Fix: Cite the Microsoft blog for the figures; write 'tcpip.sys: 100% of 7 historical MSRC cases' (and clfs.sys 96% of 28), not 'historical-CVE corpus'; say 1,507 reproduction tasks across 188 OSS-Fuzz projects.
2. **factual-error**, body paragraph 1 (prove-stage sentence)
   - Claim: "ends with an **automated end-to-end exploitability proof** before a finding is sent to engineering — meaning every MDASH-disclosed CVE was validated as practically exploitable, not just theoretically reachable"
   - Defect: Microsoft describes the prove stage as constructing triggering inputs 'where the bug class admits it' to prove the bug exists; it does not claim exploitability was proven for every finding, and several of the 16 are DoS or information-disclosure bugs.
   - Ground truth: 'Prove stage: Constructs and executes triggering inputs where the bug class admits it. The prove stage validates the pre-condition dynamically and formulates the bug-triggering inputs to prove existence of vulnerability (for example, ASan in C/C++).' Of CVE-2026-33827: 'exploitation requires winning a narrow timing window and shaping allocator reuse'. (https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-finds-16-new-vulnerabilities/)
   - Fix: Write: the prove stage builds and runs triggering inputs where the bug class allows, to confirm the bug exists; drop 'practically exploitable' for every CVE.
3. **factual-error**, Defender takeaway, first implication
   - Claim: "the MDASH-discovered Windows CVEs (a substantial subset of the May 2026 Patch Tuesday in § 2) should be treated as "practically exploitable" even without observed ITW activity ... that lifts these above the typical "Less Likely / More Likely" scoring noise"
   - Defect: Microsoft's own exploitability assessments for the four Critical MDASH CVEs are 'Exploitation Less Likely' (three) and 'Exploitation Unlikely' (one), none exploited or publicly disclosed; the premise (proof-of-exploitability before disclosure) is not in the source. Two of the four were released in April, not May.
   - Ground truth: MSRC: CVE-2026-33827 (released 2026-04-14, CVSS 8.1) 'Exploitation Less Likely'; CVE-2026-33824 (2026-04-14, 9.8) 'Exploitation Less Likely'; CVE-2026-41089 (2026-05-12, 9.8) 'Exploitation Less Likely'; CVE-2026-41096 (2026-05-12, 9.8) 'Exploitation Unlikely'; all exploited: No, publiclyDisclosed: No. The Register: 'Redmond says exploitation is "unlikely"' for CVE-2026-41096. (work/2026-10-21T1148Z-audit/truth-2/bodies/e2-msrc-CVE-2026-33824.txt)
   - Fix: Replace with the vendor's own ratings per CVE and a patch-priority argument based on unauthenticated network reachability (tcpip.sys, IKEEXT, Netlogon CLDAP, DNS client), not 'practically exploitable'.
4. **factual-error**, body paragraph 1 ('first production run')
   - Claim: "In MDASH's first production run against Windows the harness produced 16 previously unknown CVEs"
   - Defect: 'First production run' is not in either cited page; Microsoft says only that 16 CVEs in the Patch Tuesday were found with MDASH and that the harness is used by Microsoft security engineering teams.
   - Ground truth: 'Across the Windows network stack and adjacent services, today's Patch Tuesday includes 16 CVEs our engineering teams found using codename MDASH.' (https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-finds-16-new-vulnerabilities/)
   - Fix: Delete 'In MDASH's first production run'; write 'Microsoft credits MDASH with 16 CVEs in the May 2026 release'.
5. **factual-error**, body paragraph 1 (last sentence)
   - Claim: "Microsoft has scheduled a customer-facing preview of the harness for June 2026."
   - Defect: Neither page gives a June date; the preview is already running as a limited private preview.
   - Ground truth: Microsoft: 'tested by a small set of customers as part of a limited private preview'; The Register: 'making the tool available to a limited number of customers in private preview'. (https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-finds-16-new-vulnerabilities/)
   - Fix: Write 'a limited private preview with a small set of customers has started; sign-up is open'.
6. **factual-error**, Defender takeaway, second implication
   - Claim: "DirectAccess and Always-On VPN are widely deployed as the AD-integrated remote-access primitive across Swiss federal and EU government estates"
   - Defect: No page read says anything about deployment in Swiss federal or EU government estates; the exposure statement the source gives is narrower and has a precondition.
   - Ground truth: CVE-2026-33824 is 'reachable by a remote, unauthenticated attacker over UDP/500 on any host configured as an IKEv2 responder (RRAS VPN, DirectAccess, Always-On VPN infrastructure, or any machine with an inbound connection security rule)'; 'a bare Start-Service IKEEXT with no responder policy is not vulnerable'. (https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-finds-16-new-vulnerabilities/)
   - Fix: Drop the deployment assertion; state the exposure condition (IKEv2 responder policy present) and tell the reader to check for hosts with RRAS VPN, DirectAccess, Always-On VPN infrastructure or inbound connection security rules.
7. **imprecision**, headline; cves[]; Defender takeaway (Patch Tuesday month)
   - Claim: "finds 16 Windows CVEs in network-stack kernel components; cves: []; 'expedite May 2026 cumulative update'"
   - Defect: Six of the 16 are user-mode, the table also covers http.sys and telnet.exe, none of the CVE ids is named in the entry (cves[] is empty), and two of the four Critical RCEs (CVE-2026-33827, CVE-2026-33824) were released in April, so the 'May cumulative update' is not where they first shipped.
   - Ground truth: Microsoft: 'These vulnerabilities are 10 kernel-mode / 6 usermode.' Critical rows: CVE-2026-33827 (tcpip.sys), CVE-2026-33824 (ikeext.dll), CVE-2026-41089 (netlogon.dll), CVE-2026-41096 (dnsapi.dll); 'CVE-2026-33827, patched in April Patch Tuesday', 'CVE-2026-33824, patched in April Patch Tuesday'. MSRC release dates 2026-04-14 for those two, 2026-05-12 for the other two. (https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-finds-16-new-vulnerabilities/)
   - Fix: Headline: 'finds 16 Windows CVEs in networking and authentication components'; list the four Critical ids with MSRC CVSS (8.1, 9.8, 9.8, 9.8) and release months in cves[] or the body.
8. **imprecision**, Defender takeaway (ATT&CK sentence)
   - Claim: "Mapped to `T1190 Exploit Public-Facing Application` and `T1133 External Remote Services`."
   - Defect: T1133 describes use of legitimate remote services with valid access; the source describes pre-authentication memory-corruption bugs in network services, which is T1190 only, and no exploitation is reported.
   - Ground truth: 'Unauth IKEv2 SA_INIT double-free triggers LocalSystem RCE'; MSRC 'exploited: No'. (https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-finds-16-new-vulnerabilities/)
   - Fix: Keep T1190 (as a potential, not observed, vector); drop T1133.
9. **imprecision**, body (Defender takeaway)
   - Claim: "(a substantial subset of the May 2026 Patch Tuesday in § 2)"
   - Defect: Reference to a section of the retired v2 brief ('§ 2') is pipeline self-reference with no target for readers.
   - Ground truth: n/a (migration artefact; entry has migrated_from: briefs/2026-05-13.md) (work/2026-10-21T1148Z-audit/truth-2/bodies/e2-msft.txt)
   - Fix: Delete the '§ 2' reference.
- Possible twin outside batch: entries/2026-05-13/cve-2026-41089-cve-2026-41096-cve-2026-41103-cve-2026-42898.md (May 2026 Patch Tuesday entry that also mentions MDASH; CVE-2026-41089 and CVE-2026-41096 are among the MDASH CVEs)

## 2026-05-13/mini-shai-hulud-s-github-actions-pwn-request-oidc-token-thef (factual-error)

1. **factual-error**, summary; body 'Background' paragraph
   - Claim: "Mini Shai-Hulud (the TeamPCP self-propagating npm worm) first surfaced in coverage on 2026-05-10 as a SAP CAP-package compromise."
   - Defect: The SAP wave was published on 2026-04-29 and reported on 2026-04-30/05-01; 2026-05-10 is the pipeline's own first-coverage date, not when the worm surfaced. The summary field also holds only this background sentence, not the finding, and the body links to an internal brief ('/briefs/2026-05-10/').
   - Ground truth: The Register: 'On April 29, TeamPCP compromised four official npm packages from the SAP JavaScript and cloud application development ecosystem and published the poisoned releases between 09:55 and 12:14 UTC.' (https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/)
   - Fix: Write 'Mini Shai-Hulud first hit SAP npm packages (mbt, @cap-js/*) on 2026-04-29'; make the summary state the TanStack pwn-request/cache-poisoning/OIDC-extraction chain of 2026-05-11; remove the internal brief link.
2. **factual-error**, body 'Background' paragraph (original campaign description)
   - Claim: "The original campaign relied on attacker-published versions of dependency-chain packages catching legitimate downstream consumers; its blast-radius was bounded by which packages opted into the affected dependency graph."
   - Defect: The SAP wave was a worm-style compromise of official packages that stole developer and CI secrets, self-propagated and exfiltrated to GitHub repositories; it was not 'dependency-chain' packages bounded by an opt-in graph, and it already used runner-memory extraction.
   - Ground truth: The Register: 'The compromised packages contain malicious preinstall scripts ... This new campaign deploys a multi-stage payload that steals developer secrets, self-propagates, encrypts all the stolen goods, and then exfiltrates the now-locked secrets into a new GitHub repository'; Wiz: 'leveraging advanced techniques such as extracting secrets from runner memory'. (https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages/)
   - Fix: Delete the characterisation or restate it as in The Register (compromised official SAP packages with preinstall payloads, worm-style propagation).
3. **imprecision**, body paragraph 1 (cited sentence on the 2026-05-11 wave)
   - Claim: "it uses no infostealer of a maintainer's machine, no credential theft from the package owner; instead it abuses a class problem in GitHub Actions"
   - Defect: True only for the initial TanStack publish (no npm tokens stolen). The wave's payload is itself a credential stealer that spread to other maintainers' packages with stolen credentials, so 'no infostealer' misdescribes the wave and contradicts the entry's own step 10.
   - Ground truth: TanStack: 'No npm tokens were stolen and the npm publish workflow itself was not compromised.' StepSecurity: 'Mini Shai-Hulud is a true worm: after stealing credentials from one CI/CD pipeline, it enumerates every package that maintainer controls and publishes infected versions of each.' (https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)
   - Fix: Scope it: the TanStack publish needed no stolen npm token (OIDC token taken from runner memory); the payload then steals credentials from install hosts and spreads with them.
4. **imprecision**, chain step 1 (Reconnaissance) and its T1593 mapping
   - Claim: "The operator (`voicproducoes`, GitHub account ID 269549300, created 2026-03-19) identifies a target repository whose CI/CD configuration triggers on `pull_request_target`. ... Mapped to `T1593 Search Open Websites/Domains` (the operator surveys public Actions configurations)."
   - Defect: The account id and creation date are right, but no source describes a reconnaissance step; the timeline starts with fork creation. The behavior and its ATT&CK mapping are inference presented as fact.
   - Ground truth: StepSecurity: 'The attacker created a fork of TanStack/router on May 10, 2026, using the GitHub account voicproducoes (ID: 269549300, created 2026-03-19).' TanStack timeline begins '2026-05-10 17:16 Attacker creates fork'. (https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)
   - Fix: Drop step 1 and T1593, or label it as an assumption; start the chain at fork creation.
5. **factual-error**, chain step 3 (Pwn-Request lure content)
   - Claim: "attacker-controlled code paths reached via subtle changes the human reviewer is unlikely to read (e.g. a modified `pnpm-lock.yaml`, a new dev-dependency, or a CI helper script under `.github/`)"
   - Defect: Invented detail. The PR added a ~30,000-line payload file under packages/history and was titled 'WIP: simplify history build'; the pull_request_target workflow checked out the PR merge ref and ran the benchmark build, which executed it. No lockfile, dev-dependency or .github change is reported.
   - Ground truth: TanStack: 'Adds packages/history/vite_setup.mjs (a ~30,000-line bundled JS payload)'; 'bundle-size.yml's benchmark-pr job checks out refs/pull/7378/merge, runs pnpm install + pnpm nx run @benchmarks/bundle-size:build — this executes vite_setup.mjs'; the attacker then 'force-pushes the PR back to current main HEAD ... making the visible PR a 0-file no-op'. (https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)
   - Fix: Replace with: the workflow checked out and built the fork's merge ref, executing a payload file added in the PR; the PR was afterwards force-pushed to a no-op and closed.
6. **factual-error**, chain step 5 (Wait for release)
   - Claim: "The release workflow on `main` restores the poisoned cache, builds the package using the trojanised pnpm store, and reaches the publish step."
   - Defect: The publish step was not reached; tests failed, the Publish Packages step was skipped, and the malware published directly during the test/cleanup phase. The entry contradicts itself in step 8 ('The "Publish Packages" step ... was bypassed entirely').
   - Ground truth: TanStack: 'it does not come from the workflow's defined Publish Packages step, which was skipped because tests failed. It comes from the malware running during the test/cleanup phase, which mints an OIDC token via the workflow's id-token: write permission and POSTs directly to registry.npmjs.org'. (https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)
   - Fix: Write: the poisoned store ran during the release job; the attacker's code minted an OIDC token and published directly while the real publish step was skipped.
7. **imprecision**, chain steps 6 and 7 (OIDC token handling)
   - Claim: "The token sits in the workflow process's memory but is not surfaced as an environment variable to step scripts. ... no audit signal at the npm side distinguishes it from a normal publish."
   - Defect: (low confidence) StepSecurity shows the payload reading ACTIONS_ID_TOKEN_REQUEST_TOKEN / ACTIONS_ID_TOKEN_REQUEST_URL environment variables to obtain tokens, and TanStack names a detectable difference (publishes from unexpected workflow steps), so both absolutes overreach.
   - Ground truth: StepSecurity: 'It uses the stolen GitHub OIDC token (ACTIONS_ID_TOKEN_REQUEST_TOKEN / ACTIONS_ID_TOKEN_REQUEST_URL) to obtain a Fulcio signing certificate'. TanStack: 'add provenance-source-verification to detect publishes from unexpected workflow steps'. (https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)
   - Fix: Say the OIDC token is minted in the runner for id-token: write jobs and was read from Runner.Worker memory; say TanStack found the publish came from outside the defined publish step.
8. **factual-error**, chain step 8 (Provenance fraud) and Hardening SLSA bullet
   - Claim: "SLSA L3 was the assurance many EU procurement frameworks were starting to demand; this campaign demonstrates it is forgeable ... The 2026-05-11 campaign shows L3 alone is forgeable."
   - Defect: No page mentions EU procurement frameworks, and the attestation was not forged: it is a genuine attestation of a compromised pipeline.
   - Ground truth: StepSecurity: 'SLSA provenance confirms which pipeline produced the artifact, not whether the pipeline was behaving as intended. A compromised build step can produce a validly-attested but malicious package.' (https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)
   - Fix: Delete the procurement clause; write 'valid SLSA provenance proves which pipeline built the package, not that the pipeline behaved'.
9. **imprecision**, chain step 9 (payload)
   - Claim: "a 2.3 MB triple-obfuscated `router_init.js` that on `postinstall` harvests ... browser cookie jars and 100+ further credential paths"
   - Defect: The payload ran from the `prepare` script of an optional git dependency (Wiz notes a `preinstall` variant for UiPath/Mistral packages), not `postinstall`; the 100+ path list names Slack's Cookies file, crypto wallets, VPN, AI-tool and shell-history files, not browser cookie jars.
   - Ground truth: StepSecurity: '"prepare": "bun run tanstack_runner.js && exit 1"' ... 'The `prepare` lifecycle hook runs automatically when the dependency is installed via a `github:` URL'; path table lists '~/.config/Slack/Cookies'. (https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)
   - Fix: Write 'a git-URL optional dependency whose prepare script launches the Bun-run payload' and list the path categories as StepSecurity does.
10. **factual-error**, What detection looks like, runner-process introspection bullet
   - Claim: "any step that reads from `/proc/*/mem` from a non-`root` process on the runner."
   - Defect: The memory scraper is run under sudo, so a non-root filter would miss it.
   - Ground truth: StepSecurity: 'The orchestrator feeds this Python script to `sudo python3` via stdin' and the captured process tree shows 'sudo python3 | tr | grep | sort' with 'python3 reads /proc/2138/mem'. (https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem)
   - Fix: Alert on any read of Runner.Worker's /proc/<pid>/mem regardless of user (including sudo-launched interpreters).
11. **imprecision**, What detection looks like (uncited generalisations)
   - Claim: "npm's audit log surfaces this if the org has it enabled. ... GitHub-hosted runners do not need to read `/proc/<pid>/mem` for any legitimate workflow purpose."
   - Defect: Neither clause is stated by any page read.
   - Ground truth: TanStack: 'No internal alerting. We learned about the compromise from a third party.' Detection came from StepSecurity. (https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)
   - Fix: Remove the audit-log assurance or cite an npm doc; qualify the /proc statement as an assessment.
12. **factual-error**, Hardening bullets 1, 3 and 5 (invented option and command)
   - Claim: "`actions/cache` with `save: false` from `pull_request_target` ... pair it with a maintainer-verified `npm provenance verify`"
   - Defect: Neither exists: actions/cache has no `save` input (restore-only is actions/cache/restore) and npm verifies provenance with `npm audit signatures`.
   - Ground truth: actions/cache README inputs: path, key, restore-keys, enableCrossOsArchive, fail-on-cache-miss, lookup-only; 'New actions are available for granular control over caches - restore and save'. npm docs: 'You can verify the provenance attestations of downloaded packages with the following `audit` command: `npm audit signatures`'. (https://github.com/actions/cache)
   - Fix: Use actions/cache/restore for fork-reachable jobs (no save), and `npm audit signatures` for attestation checks.
13. **imprecision**, Hardening bullet 1
   - Claim: "Pin every `pull_request_target` workflow to a SHA-locked version of every action it uses; never `@main` or `@v1`. Forks cannot influence what runs."
   - Defect: Overclaim: pinning does not stop a workflow that checks out and builds the fork's merge ref from running fork code, which was the root cause.
   - Ground truth: TanStack root cause: 'bundle-size.yml ran pull_request_target for fork PRs and, inside that trigger context, checked out the fork's PR-merge ref and ran a build'. GitHub Security Lab: the danger is 'Combining pull_request_target workflow trigger with an explicit checkout of an untrusted PR'. (https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/)
   - Fix: Lead with 'never check out or build fork code under pull_request_target'; keep SHA pinning as a separate item without the 'forks cannot influence' sentence.
14. **imprecision**, ATT&CK mappings in prose (steps 2, 3, 7)
   - Claim: "T1583.001 Acquire Infrastructure: Domains-equivalent; T1199 Trusted Relationship and T1505.003 Web Shell-equivalent; T1606.002 Forge Web Credentials: SAML Tokens-equivalent for OIDC"
   - Defect: These ids name behaviors the sources do not describe (domains, third-party access, web shells, SAML forgery); 'equivalent' hedges do not make them mapping-valid.
   - Ground truth: Sources describe: fork/account creation, a pull_request_target build running fork code, Actions cache poisoning, /proc/<pid>/mem token extraction, OIDC token use to publish to npm, credential-file and IMDS theft, GitHub/Session exfiltration, systemd/LaunchAgent persistence, rm -rf wiper. (https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)
   - Fix: Remove these inline ids and carry the mapping in techniques[] (see upgrade block).
15. **imprecision**, cves[] (empty)
   - Claim: "cves: []"
   - Defect: The TanStack compromise has a CVE (reserved 2026-05-11, published 2026-05-12, CVSS 3.1 9.6 by the GitHub CNA) and was added to CISA KEV on 2026-05-27, after this entry was filed.
   - Ground truth: CISA KEV: CVE-2026-45321 'TanStack Unspecified Vulnerability', dateAdded 2026-05-27, notes cite 'https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx'. CVE record: 'Malware in 42 @tanstack/* packages exfiltrates cloud credentials, GitHub tokens, and SSH keys', CWE-506, baseScore 9.6. (https://github.com/TanStack/router/security/advisories/GHSA-g7cv-rxg3-hmpx)
   - Fix: Add CVE-2026-45321 (cvss 9.6 per the GitHub CNA record; KEV 2026-05-27) via a changelog record citing the GHSA; the CVE record itself is not citable.
16. **imprecision**, sources[] dates; chain step 2 (accounts)
   - Claim: "TanStack post-mortem, 2026-05-12; fork `zblgg/configuration` created by operator `voicproducoes`"
   - Defect: The post-mortem's datePublished is 2026-05-11 (updated 2026-05-15); the sources split the fork across two attacker accounts (TanStack: zblgg, StepSecurity and NCSC-CH: voicproducoes).
   - Ground truth: TanStack page: datePublished 2026-05-11, dateModified 2026-05-15; 'Real attacker accounts: zblgg (id 127806521), voicproducoes (id 269549300)'; NCSC-CH: 'Fork: voicproducoes/router (fork of TanStack/router, created 2026-05-10)'. (https://tanstack.com/blog/npm-supply-chain-compromise-postmortem)
   - Fix: Date the citation 2026-05-11 and write 'two attacker accounts (zblgg, voicproducoes)'.
17. **imprecision**, body chain steps 1-10, payload and detection paragraphs (inline citation)
   - Claim: "(no inline citation on steps 1-10, 'What detection looks like' or 'Hardening')"
   - Defect: Only the opening paragraph carries citations; every technical clause that follows is uncited, which is how the unsupported details above went unchecked. Also 'No IOCs in this brief' is pipeline self-reference.
   - Ground truth: Pages that carry the chain: TanStack post-mortem (steps 2-8), StepSecurity (steps 7-10, payload, persistence), NCSC-CH hub post 12558 (dead-man's switch, persistence). (https://security-hub.ncsc.admin.ch/#/posts/12558)
   - Fix: Bind each step to the page above that carries it; replace 'in this brief' with neutral wording.

## 2026-05-13/ncsc-uk-10-questions-to-ask-when-using-ai-models-to-find-vul (factual-error)

1. **factual-error**, body paragraph 1, list (a)-(f)
   - Claim: "(f) false-positive overhead on the blue team."
   - Defect: The page has no question or passage about false-positive overhead; the nearest item is resourcing ('spending all my money/time/people finding vulnerabilities, and have nothing left to fix them'). The list also glosses (b) as covering 'secrets' and (d) as 'magnify attacker reach if the agent itself is compromised', neither of which is on the page.
   - Ground truth: Question 5 bullets: 'How could I leak information?'; 'Have I sandboxed my system so that it can only talk to the LLM and my code base?'; 'Will I give access to my production environment?'; 'What permissions have I given the LLM?'; 'How can I avoid spending all my money/time/people finding vulnerabilities, and have nothing left to fix them?'; 'Do I understand the terms and conditions, and data retention policies?'; 'How will I ensure the activity is legal?' (https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)
   - Fix: Delete (f); rewrite (b) and (d) as 'information leakage and production access' and 'what permissions the LLM is given'.
2. **imprecision**, body paragraph 1 (last sentence)
   - Claim: "The piece explicitly warns that **AI-accelerated vulnerability discovery without matching remediation capacity makes the organisation worse off, not better** — a direct critique of "buy the AI tool" patterns."
   - Defect: NCSC's wording is hedged and general ('You could even make your security worse'); it does not say 'worse off, not better', does not name remediation capacity in that sentence, and does not critique buying tools.
   - Ground truth: 'just *finding* vulnerabilities does nothing to improve your security. You could even make your security worse.' and Q3 'Do I have a process to manage any vulnerabilities that AI finds?' (https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)
   - Fix: Quote NCSC: finding vulnerabilities alone does not improve security and 'could even make your security worse'; drop 'direct critique of buy the AI tool patterns'.
3. **imprecision**, body paragraph 1 (second sentence)
   - Claim: "The guidance is substantively different from the previously-covered NCSC-CH BACS strategic assessment: it is process- and infrastructure-flavoured rather than landscape-flavoured."
   - Defect: Pipeline self-reference to another entry; the cited page never mentions NCSC-CH or BACS, so the comparison is uncited and meaningless to a reader who has not seen that item.
   - Ground truth: The NCSC-UK page contains no reference to NCSC-CH or BACS. (https://www.ncsc.gov.uk/blogs/10-questions-ask-using-ai-models-find-vulnerabilities)
   - Fix: Delete the sentence.

## 2026-05-13/trickmo-trickmo-c-android-banking-trojan-migrates-c2-to-the (imprecision)

1. **imprecision**, Defender takeaway (first sentence)
   - Claim: "blocking TON traffic at the corporate gateway is non-trivial because TON shares the standard internet routes; behaviour-side, detect Android devices that initiate the TON loopback proxy and that issue outbound to non-corporate SOCKS5 / SSH ports under unusual entitlements."
   - Defect: The source's point is that the traffic is encrypted and indistinguishable from other TON applications, so it cannot be told apart from legitimate TON use; it does not say TON shares standard routes or that blocking it is hard. 'Under unusual entitlements' has no basis in any page.
   - Ground truth: ThreatFabric: 'Traffic-pattern detection at the network edge sees only TON traffic, which is encrypted and indistinguishable from any other TON-enabled application's outbound flow.' and 'Traditional domain takedowns are largely ineffective because the operator's endpoints do not rely on the public DNS hierarchy'. (https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)
   - Fix: Write: network-edge signatures cannot separate TrickMo from other TON traffic, so rely on device-side controls and on the SSH-tunnel and SOCKS5 behavior; drop 'shares the standard internet routes' and 'unusual entitlements'.
2. **imprecision**, body paragraph 1 (dormant code sentence)
   - Claim: "Dormant code includes the Pine hooking framework and NFC permissions, suggesting contactless-payment interception is in development."
   - Defect: ThreatFabric says NFC and Pine are declared but not exercised and read them as reserved for future runtime-delivered features; it does not say contactless-payment interception is in development.
   - Ground truth: 'NFC is declared and reported but not exercised, which fits the same reserved-capability pattern as the dormant Pine framework.' and 'these dormant components suggest the operators are preparing the platform for future runtime-delivered features'. (https://www.threatfabric.com/blogs/new-trickmo-variant-device-take-over-malware-targeting-banking-fintech-wallet-auth-app)
   - Fix: Write: Pine and NFC permissions are bundled but unused, suggesting future runtime-delivered capabilities (possibly NFC-targeted).
3. **imprecision**, body paragraph 1 (dropper sentence)
   - Claim: "Droppers masquerade as TikTok variants distributed via Facebook ads"
   - Defect: (low confidence) The sources say the droppers are TikTok look-alikes (adult-friendly versions per The Hacker News) delivered 'through Facebook' / 'over Facebook'; none says ads.
   - Ground truth: THN: 'Dropper apps containing the malware masquerade as adult-friendly versions of TikTok through Facebook'. ThreatFabric campaign tags: 'Tic_Italy_FB: TikTok campaign over Facebook'; also 'distributed via phishing websites and dropper apps' (THN). (https://thehackernews.com/2026/05/new-trickmo-variant-uses-ton-c2-and.html)
   - Fix: Write 'TikTok look-alike droppers delivered through Facebook campaigns and phishing websites'.
4. **imprecision**, body (ATT&CK ids in prose)
   - Claim: "T1517 Access Notifications; T1090.001 Proxy: Internal Proxy; T1422 System Network Configuration Discovery and T1437.001 Application Layer Protocol: Web Protocols"
   - Defect: T1517, T1422 and T1437.001 are real ATT&CK Mobile ids but are not in the pinned Enterprise dataset, so they cannot be carried in techniques[]; T1090.001 (internal proxy) is a weak fit for an external traffic-exit node (T1090).
   - Ground truth: attack.mitre.org lists T1517 'Access Notifications', T1422 'System Network Configuration Discovery', T1437.001 'Application Layer Protocol: Web Protocols' as Mobile techniques; the pinned attack/enterprise-attack.json returns UNKNOWN for all three. (https://attack.mitre.org/techniques/T1422/)
   - Fix: Use Enterprise ids in techniques[] (see upgrade block) and drop the inline Mobile ids.

## 2026-05-14/cve-2026-8043-ivanti-xtraction-external-file-control-cvss-9 (factual-error)

1. **factual-error**, cves[CVE-2026-8043].type; tags (rce)
   - Claim: "type: rce"
   - Defect: The vendor and ENISA describe CVE-2026-8043 as file read plus arbitrary HTML write leading to information disclosure and client-side attacks, not remote code execution. The EPM SQL injection (CVE-2026-8111) and vTM command injection (CVE-2026-8051) are the RCE flaws; cves[] also leaves affected and fixed null although both are given.
   - Ground truth: EUVD-2026-29487 (CVE-2026-8043, base score 9.6, CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:N): 'External control of a file name in Ivanti Xtraction before version 2026.2 allows a remote authenticated attacker to read sensitive files and write arbitrary HTML files to a web directory, leading to information disclosure and possible client-side attacks.' product_version 'patch: 2026.2'. (https://euvdservices.enisa.europa.eu/api/search?text=CVE-2026-8043)
   - Fix: Set type to information-disclosure (or null), affected '< 2026.2', fixed '2026.2'; drop the rce tag or scope it to the EPM and vTM flaws (CVE-2026-8111 8.8 and CVE-2026-8051 7.2 per EUVD-2026-29491 and EUVD-2026-29488) and list those ids in cves[].
2. **factual-error**, summary; body paragraph 3 ('Affected and fixed versions'); actions[0]
   - Claim: "Ivanti EPM ≤ 2024 SU6 → 2024 SU6 ... SQL injection in the EPM web console (≤ 2024 SU6)"
   - Defect: EPM is affected before 2024 SU6 and fixed in 2024 SU6; 'up to and including SU6' contradicts the fix, and the entry's own paragraph 2 says 'prior to 2024 SU6'.
   - Ground truth: CERT-FR: 'Endpoint Manager (EPM) versions antérieures à 2024 SU6' (versions prior to 2024 SU6). EUVD-2026-29491 (CVE-2026-8111): 'SQL injection in the web console of Ivanti Endpoint Manager before version 2024 SU6 allows a remote authenticated attacker to achieve remote code execution', product_version 'patch: 2024 SU6'. (https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0576/)
   - Fix: Write 'Ivanti EPM before 2024 SU6 (fixed in 2024 SU6)'.
3. **imprecision**, body paragraph 2 (cited sentence on exploitation)
   - Claim: "Ivanti states no in-the-wild exploitation as of 2026-05-12 for any of the four advisories; CERT-FR ([CERTFR-2026-AVI-0576, 2026-05-13](...)) and SecurityWeek ([2026-05-13](...)) corroborated the disclosure within 24 hours."
   - Defect: The citation sits on CERT-FR, whose avis contains no exploitation statement; the statement is on Ivanti's blog (and SecurityWeek).
   - Ground truth: Ivanti blog (2026-05-12): 'We have no evidence of these vulnerabilities being exploited in the wild.' SecurityWeek: 'Both Fortinet and Ivanti said they were not aware of any of the patched vulnerabilities being exploited in the wild.' CERT-FR first version dated 13 mai 2026 lists risks and affected systems only. (https://www.ivanti.com/blog/may-2026-security-update)
   - Fix: Cite Ivanti's blog for the no-exploitation statement; keep CERT-FR for affected versions.
4. **factual-error**, summary; body paragraph 1 (Xtraction primitives)
   - Claim: "read arbitrary files and write HTML to the web directory, staging XSS or web-shell drop points ... is sufficient to chain to web-shell drop in environments where the attacker can guess or read deployment paths"
   - Defect: The vendor says 'sensitive files' and 'arbitrary HTML files' with 'possible client-side attacks'; a web-shell chain from an HTML write is not stated by any source, and an HTML file is not server-side code.
   - Ground truth: 'allows a remote authenticated attacker to read sensitive files and write arbitrary HTML files to a web directory, leading to information disclosure and possible client-side attacks.' (https://euvdservices.enisa.europa.eu/api/search?text=CVE-2026-8043)
   - Fix: Restate as the vendor does; delete the web-shell chain, the T1505.003 mapping and the 'web-shell drop' detection clause.
5. **factual-error**, summary; body paragraph 4 (last sentence); actions[0]
   - Claim: "Xtraction is commonly deployed on internal management networks where egress controls are looser than perimeter"
   - Defect: No page read says where Xtraction is deployed or anything about egress controls; the same unsupported premise drives the patch-first ordering in actions[0] and the T1041 remark.
   - Ground truth: The Ivanti blog and CERT-FR avis contain no deployment or egress statement; no exploitation is reported. (https://www.ivanti.com/blog/may-2026-security-update)
   - Fix: Delete the clause and the T1041 sentence; base the patch order on the vendor's severity (CVSS 9.6 for Xtraction).
6. **factual-error**, body paragraph 4 (detection)
   - Claim: "audit Xtraction installations for any HTML file in the web tree whose timestamp post-dates 2026-04-01 and whose content does not match a release manifest"
   - Defect: The 2026-04-01 threshold has no source (the flaw was disclosed 2026-05-12 with no exploitation window), and the web-shell mapping (T1505.003) for EPM SQL injection is unsupported.
   - Ground truth: No page gives an exposure window; Ivanti: 'We have no evidence of these vulnerabilities being exploited in the wild.' (https://www.ivanti.com/blog/may-2026-security-update)
   - Fix: Drop the date; advise reviewing HTML files in the Xtraction web directory not belonging to a release, without a start date, or remove the clause.
7. **imprecision**, body paragraph 2 (EPM technique-class sentence)
   - Claim: "SQL injection against EPM's SQL Server back-end is the well-documented `xp_cmdshell` (T1059) or stored-procedure code-execution pivot ransomware initial-access brokers have weaponised against EPM and analogous endpoint-management platforms for years."
   - Defect: Uncited and not stated by any page read; the vendor's description is 'remote authenticated attacker to achieve remote code execution' and it reports no exploitation of the May flaws.
   - Ground truth: EUVD-2026-29491: 'allows a remote authenticated attacker to achieve remote code execution.' (https://euvdservices.enisa.europa.eu/api/search?text=CVE-2026-8111)
   - Fix: Remove the IAB claim or cite a source for earlier EPM exploitation; state the vendor's RCE description.
8. **imprecision**, body paragraph 1 (Xtraction primitive wording)
   - Claim: "letting a remote authenticated attacker read arbitrary server-side files"
   - Defect: (low confidence) The vendor says 'sensitive files'; 'arbitrary server-side files' is a stronger reading.
   - Ground truth: 'read sensitive files and write arbitrary HTML files to a web directory'. (https://euvdservices.enisa.europa.eu/api/search?text=CVE-2026-8043)
   - Fix: Write 'read sensitive files'.
9. **imprecision**, headline; body paragraph 3 ('Inclusion gate cleared'); actions[0] ('See § 2')
   - Claim: "...May 2026 advisory batch, no | Inclusion gate cleared: CVE-2026-8043 sits in the ENISA EUVD CVSS 9.0–10.0 critical band"
   - Defect: The headline is cut off mid-phrase ('no'), and the body and action carry pipeline self-reference ('Inclusion gate cleared', 'See § 2'). The batch also omits the fourth advisory (Secure Access Client, CVE-2026-7431 4.4 and CVE-2026-7432 7.8) although it says 'four product-line advisories' and 'any of the four'.
   - Ground truth: Ivanti: 'today Ivanti is disclosing vulnerabilities in Ivanti Secure Access Client, Xtraction, Virtual Traffic Manager and Endpoint Manager (EPM)'. EUVD-2026-29487 baseScore 9.6. (https://www.ivanti.com/blog/may-2026-security-update)
   - Fix: Complete the headline ('no in-the-wild exploitation'); delete the internal phrases; name the Secure Access Client advisory or say 'three of four'.
10. **imprecision**, priority (high)
   - Claim: "priority: high"
   - Defect: Context only: on the facts known on 2026-05-14 the entry is an unexploited, authenticated (PR:L) flaw in a reporting product with no PoC and no evidence of constituency exposure, so 'high' rests on CVSS alone (severity statistics are an F16 disqualifier on a high); the two RCE flaws are authenticated as well (SQLi PR:L, vTM admin).
   - Ground truth: Ivanti: 'We have no evidence of these vulnerabilities being exploited in the wild.' EUVD vectors: CVE-2026-8043 PR:L, CVE-2026-8111 PR:L, CVE-2026-8051 PR:H; none in CISA KEV as of 2026-10-20. (https://euvdservices.enisa.europa.eu/api/search?text=CVE-2026-8043)
   - Fix: Treat as regular-cycle patch priority (notable or routine) unless constituency exposure of Xtraction or EPM is documented.

## 2026-05-14/dutch-igj-rules-clinical-diagnostics-nmdl-failed-nen-7510-in (factual-error)

1. **factual-error**, summary; body paragraph 2 (IGJ demands)
   - Claim: "IGJ has no fining power and has demanded short-term independent NEN 7510 certification; ... IGJ also signalled sector-wide enforcement intent by publicly calling for all healthcare providers to demonstrate independent certification"
   - Defect: IGJ asked Clinical Diagnostics to demonstrably comply with NEN 7510 in the short term; the certification is Clinical Diagnostics' own statement, and the release contains no call to other providers (it says IGJ keeps following this company's progress). The company's reported positive external audit is omitted.
   - Ground truth: IGJ: 'De inspectie heeft Clinical Diagnostics gevraagd om op korte termijn aantoonbaar te voldoen aan de NEN7510. Op basis van de Wabvpz kan de IGJ geen bestraffende maatregelen opleggen. De AP kan dat wel op basis van de AVG. Inmiddels heeft Clinical Diagnostics laten weten dat een externe audit heeft plaatsgevonden met positieve uitkomst en dat naar verwachting de certificering binnenkort is afgerond. De inspectie blijft de voortgang en naleving nauwgezet volgen.' (https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)
   - Fix: Write: IGJ asked the lab to demonstrate NEN 7510 compliance at short notice and cannot impose punitive measures (AP can under the GDPR); the lab reports a positive external audit with certification expected. Delete the sector-wide sentence (the Computable page, which returned HTTP 503 here, was not readable; cite a source that carries it or drop it).
2. **factual-error**, summary; body paragraph 4 (Swiss comparison)
   - Claim: "NEN 7510 (Dutch healthcare security baseline) is the structural analogue of Switzerland's EPDG security profile — same gap, same regulator pattern ... the same hygiene-baseline gaps Swiss healthcare providers face under cantonal supervision."
   - Defect: No page read compares NEN 7510 with the EPDG or says anything about Swiss providers; the claim that Swiss providers have the same gaps and a 'same regulator pattern' is unsupported and reads as fact.
   - Ground truth: The IGJ release concerns Clinical Diagnostics LCPL BV and NMDL BV in Rijswijk only; it names Wabvpz, NEN 7510, the AP and the AVG. (https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)
   - Fix: Delete the Swiss comparison, or present it as the analyst's assessment with a source for the EPDG certification requirement.
3. **imprecision**, body paragraph 4 (last sentence)
   - Claim: "The breach scale (941k records, mass-screening data) is the proximate consequence of those structural gaps"
   - Defect: IGJ says working to the standard could have reduced the likelihood and limited the impact; it does not call the breach scale the proximate consequence of the gaps.
   - Ground truth: 'Het werken volgens deze norm had de kans op een informatiebeveiligingsincident als dit kunnen verkleinen en de gevolgen beperken.' (https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)
   - Fix: Write: IGJ concludes compliance 'could have reduced the likelihood and limited the consequences'.
4. **imprecision**, body paragraph 1 (cited sentence)
   - Claim: "did not meet the mandatory NEN 7510 information-security standard at the time of their July 2025 ransomware breach, and had not fully remediated the deficiencies as of IGJ's December 2025 follow-up inspection"
   - Defect: IGJ's release says 'datahack' and an 'inspectiebezoek' in December 2025 at which the company still did not meet the norm; 'ransomware' and 'follow-up' are not on the cited page (ransomware, group Nova and the 941,000 figure come from the lab and press reporting).
   - Ground truth: 'Uit het onderzoek blijkt dat de betrokken bedrijfsonderdelen van Clinical Diagnostics zowel op het moment van de hack als tijdens een inspectiebezoek in december 2025 niet voldeden aan de norm.' (https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)
   - Fix: Say 'data hack' for the IGJ clause and 'inspection visit in December 2025'; keep 'ransomware (Nova)' with the GovInfoSecurity or Computable citation.
5. **imprecision**, body paragraph 1, second sentence (NEN 7510 description)
   - Claim: "structurally aligned with ISO/IEC 27001 but extended for health-data obligations; non-compliance is independently actionable by multiple regulators."
   - Defect: Uncited; IGJ's page says Wabvpz requires NEN 7510 compliance but gives no ISO relationship, and IGJ itself cannot sanction under the Wabvpz.
   - Ground truth: 'Die vereist dat organisaties die werken met patiëntgegevens moeten voldoen aan de norm NEN 7510 om risico's op cyberincidenten te beperken.' and 'Op basis van de Wabvpz kan de IGJ geen bestraffende maatregelen opleggen.' (https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)
   - Fix: Cite NEN's own description for the ISO relationship or drop it; say IGJ cannot impose punitive measures and the AP can.
6. **imprecision**, body paragraph 2 (cited sentence, 941,000 and Nova)
   - Claim: "The July 2025 breach — Computable's prior reporting attributes it to the Nova ransomware group — exposed approximately 941,000 patients' personal and medical records"
   - Defect: The cited Computable page returned HTTP 503 on every transport tried, so the clause could not be checked against it. Independent reporting supports Nova and 941,000 but as the number of patients whose data the lab held and was notified, with the lab unable to confirm the full extent; other figures (485,000, then 715,000, 850,000) circulated.
   - Ground truth: GovInfoSecurity: 'the lab ... says the cyberattack in July has affected 941,000 patients - nearly double the initial estimate of 485,000'; 'Ransomware-as-a-service gang Nova had first threatened in July on its dark website to leak the lab's stolen data'; BVO: 'Clinical Diagnostics cannot confirm that this is the full extent of the data breach'. (https://www.govinfosecurity.com/dutch-lab-cancer-screening-hack-balloons-to-941000-victims-a-29360)
   - Fix: Cite GovInfoSecurity (or the lab statement) for Nova and the 941,000 patients whose data the lab held; qualify as 'up to 941,000, extent unconfirmed'.
7. **imprecision**, priority (high)
   - Claim: "priority: high"
   - Defect: Context only: a Dutch regulator's compliance finding on a ten-month-old single-victim breach, with no vector, no new TTP and no Swiss nexus beyond an unsupported analogy; the entry's reason for attention is a record count and a regulator pattern, which are high-bar disqualifiers.
   - Ground truth: IGJ release names no technical vector or actor; it reports gaps (no independent audit, no periodic risk assessment). (https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)
   - Fix: Notable or routine, two to four sentences.

## 2026-05-14/famoussparrow-three-wave-intrusion-of-an-azerbaijani-energy (factual-error)

1. **factual-error**, summary; Background paragraph; 'Operationally critical context' paragraph
   - Claim: "making Azerbaijani energy infrastructure a high-value collection target for Chinese state actors monitoring European energy supply dependencies"
   - Defect: Bitdefender gives the European-gas context but explicitly says it does not establish motive, and calls the actor 'likely affiliated with the Chinese APT ecosystem' at moderate-to-high confidence; the entry turns the context into a stated motive of 'Chinese state actors'.
   - Ground truth: 'This context does not establish motive. We have N=1 victim and moderate-to-high attribution confidence.' and 'FamousSparrow is likely affiliated with the Chinese APT ecosystem.' (https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)
   - Fix: Keep the 13-countries context as Bitdefender's, add its 'does not establish motive' caveat, and write 'China-nexus actor (moderate-to-high confidence)'; drop 'structurally collection against the upstream end of European energy supply'.
2. **factual-error**, summary; headline-level claim; body 'Named clusters' paragraph
   - Claim: "deployed Deed RAT via a novel DLL-sideloading technique ... the LogMeIn Hamachi sideloading host is freshly observed for this cluster and indicates active tooling rotation rather than reuse of a known signed-binary host"
   - Defect: Bitdefender calls the technique 'evolved' and shows the loader closely matches a Deed RAT loader Trend Micro already documented for Earth Estries (same exports, same StartServiceCtrlDispatcherW hook-and-restore); no page says the Hamachi host is new for the cluster or that the binary is signed.
   - Ground truth: 'These characteristics closely match a Deed RAT loader described by Trend Micro in its reporting on the Earth Estries threat actor. In particular, the sample identified by MD5 ... exhibits the same unusual exports, similar mbedTLS-derived code, and an almost identical execution model.' (https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)
   - Fix: Write 'an evolved two-stage DLL side-loading loader (Init/ComMain exports, StartServiceCtrlDispatcherW hook) closely matching an Earth Estries loader Trend Micro documented'; say 'legitimate' not 'signed'; delete 'freshly observed'.
3. **factual-error**, Exploitation chain, Wave 2 bullet; 'Implants observed' sentence
   - Claim: "Wave 2: TernDoor deployed via DLL sideloading against a renamed-but-legitimate `deskband_injector64.exe` ... Implants observed include Deed RAT (Snappybee), TernDoor, Mofu Loader"
   - Defect: The second-wave installation was blocked by the security product; TernDoor was identified only by assessment from recovered memory pages, so it was attempted, not deployed or observed running.
   - Ground truth: 'The attempt was unsuccessful, as the security solution blocked execution before the malware could complete its installation.' and 'the partially recovered payload in this case is assessed to be Terndoor'. THN: 'attempting to unsuccessfully employ DLL side-loading to drop TernDoor by means of Mofu Loader'. (https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)
   - Fix: Write 'Wave 2: attempted TernDoor (assessed) via a Mofu-loader chain sideloaded through a renamed deskband_injector64.exe; blocked before installation completed'.
4. **factual-error**, Detection: Exchange patch-verification, Web-shell survival sweep; T1505.003 bullet; Vulnerability-mechanics paragraph
   - Claim: "Persistence outliving clean-up was the structural enabler of re-exploitation in this case. ... surviving persistence from an earlier wave is the most plausible explanation for re-exploitation across remediation attempts"
   - Defect: Bitdefender's account is that the attackers came back to the same still-vulnerable Exchange server; its lesson is patching plus credential rotation. No surviving web shell or scheduled task is reported, so the 'structural enabler' sentence states an inference as fact.
   - Ground truth: 'the attackers returned to the same vulnerable Exchange server nearly a month after the initial compromise attempt' and 'actors will exploit and re-exploit the same access path until the original vulnerability is patched, compromised credentials are rotated, and the attacker's ability to return is fully disrupted.' (https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)
   - Fix: Replace with Bitdefender's explanation (unpatched entry point, credentials not rotated, domain admin credentials in use); keep the web-shell sweep as a check, not as the established cause.
5. **factual-error**, Detection: DLL load-order hunt and Hamachi sideload bullet
   - Claim: "Hunt Sysmon event ID 7 (Image Load) records for the Hamachi process loading DLLs from `%LOCALAPPDATA%\Temp\` or other writable user-context paths rather than from the legitimate `Program Files\LogMeIn Hamachi\` install directory."
   - Defect: The loader was persisted inside a directory chosen to mimic the legitimate Hamachi install path (and staged first from C:\TEMP), so a hunt that treats the Program Files Hamachi path as clean misses the observed persistence; the payload injects into system processes rather than spawning encoded PowerShell children.
   - Ground truth: Bitdefender: "the malware was installed in C:\Program Files (x86)\LogMeIn Hamachi\, a location deliberately chosen to mimic the legitimate installation path of LogMeIn Hamachi"; first stage "C:\TEMP\LMIGuardianSvc.exe ... sideloaded C:\TEMP\lmiguardiandll.dll"; config lists SearchIndexer.exe, taskeng.exe, iexplore.exe, taskhost.exe as "Process to inject into"; service "LogMeIn Hamachi" (later "HamachiNet"). (https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)
   - Fix: Hunt for a LogMeIn Hamachi service or LMIGuardianSvc.exe on hosts without a sanctioned Hamachi install, for the loader in C:\TEMP or C:\Recovery, and for Bitdefender's own signals (w3wp.exe writing .aspx under MSExchangePowerShellAppPool, unsigned code patching StartServiceCtrlDispatcherW, kernel-driver services with ImagePath under ProgramData); drop the -EncodedCommand child-process claim.
6. **factual-error**, Detection: Exchange patch-verification bullet; Operationally critical context
   - Claim: "CU-level patch status alone is insufficient — the cumulative-update installer occasionally rolls back fixes if an OWA front-end customisation conflicts. ... any organisation in CH / EU with an on-premise Exchange server that received CU patches but lacks `HealthChecker.ps1`-level verification carries the same exposure."
   - Defect: No page read supports the rollback claim or the claim that a patched server carries the same exposure; Bitdefender's condition is an unpatched entry point and unrotated credentials.
   - Ground truth: Bitdefender: 'Patch internet-facing services immediately. ProxyShell and ProxyNotShell exploits against Exchange have been publicly documented since 2021 and 2022 respectively.' HealthChecker documents a '-VulnerabilityReport' mode. (https://microsoft.github.io/CSS-Exchange/Diagnostics/HealthChecker/)
   - Fix: Delete the rollback sentence; write 'verify the ProxyNotShell fixes are present (HealthChecker -VulnerabilityReport) and rotate credentials used during any intrusion'.
7. **factual-error**, Background paragraph (first-in-some-time claim)
   - Claim: "Recent primary technical detail has been sparse — the Bitdefender Labs publication on 2026-05-13 is the first multi-wave intrusion case study against an energy-sector victim published in some time"
   - Defect: Unsupported quantifier; Bitdefender's own claim is narrower (first public link of this cluster to South Caucasus energy targets), and it builds on Cisco Talos' 2026 UAT-9244 report.
   - Ground truth: 'This research documents energy-sector targeting in the South Caucasus, a region not previously linked to this activity cluster in public reporting.' (https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)
   - Fix: Use Bitdefender's sentence.
8. **imprecision**, Background paragraph (victimology and overlap)
   - Claim: "tracked publicly since 2021 as a China-nexus espionage cluster targeting hotels, government and engineering firms; Bitdefender's 2026-05-13 write-up cites tooling and infrastructure overlap with the Earth Estries cluster"
   - Defect: The victimology is not in either cited page (Bitdefender lists telecoms, government and technology) and Bitdefender cites toolset and tradecraft overlap, not infrastructure.
   - Ground truth: 'Prior public reporting documents activity against telecoms, government, and technology sectors across the United States, Asia-Pacific, Middle East, and South Africa.' and 'substantial overlap with the Earth Estries toolset and tradecraft'. (https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)
   - Fix: Use Bitdefender's victimology and 'toolset and tradecraft overlap'.
9. **imprecision**, cves[] (empty); Vulnerability mechanics paragraph
   - Claim: "cves: [] ... CVE-2022-41040 (SSRF in the Exchange front-end Auto-discover handler) chained with CVE-2022-41082 (deserialisation in the back-end PowerShell remoting endpoint) ... yields code execution under the Exchange application-pool identity (typically `LocalSystem`)"
   - Defect: The body names two CVEs that cves[] lacks; the Autodiscover/LocalSystem mechanics are uncited; and the authentication prerequisite is missing (Microsoft scores both PR:L and CISA calls 41082 authenticated RCE, while Bitdefender says 'unauthenticated', a contradiction the entry should surface).
   - Ground truth: MSRC: CVE-2022-41040 'Microsoft Exchange Server Elevation of Privilege Vulnerability', 8.8, CVSS:3.1/AV:N/AC:L/PR:L, exploited Yes; CVE-2022-41082 'Remote Code Execution Vulnerability', 8.0, CVSS:3.1/AV:A/AC:L/PR:L, exploited Yes. CISA KEV (added 2022-09-30, ransomware use Known): 41082 'allows for authenticated remote code execution'. Bitdefender: 'Both allow unauthenticated attackers to execute code on unpatched Exchange servers'. (work/2026-10-21T1148Z-audit/truth-2/bodies/e8-msrc-CVE-2022-41082.txt)
   - Fix: Add both CVEs to cves[] (exploited, KEV, MSRC scores 8.8 and 8.0, auth post-auth); add a Contradiction line on the authentication requirement; drop the uncited Autodiscover.svc/LocalSystem detail or cite Microsoft's guidance.
10. **imprecision**, Detection and Hardening bullets (uncited generic content)
   - Claim: "Cross-reference IIS log analysis for repeated POST requests to `/autodiscover/autodiscover.json` ... Impacket execution patterns (`smbexec.py` / `wmiexec.py`) ... on-premises Exchange remains a top initial-access vector across China-nexus campaigns ... ASR rules ... legacy authentication on hybrid setups continues to expose ProxyNotShell-adjacent paths"
   - Defect: None of these specifics is in the cited pages (Bitdefender reports atexec and smbexec-style tooling, not wmiexec), and the entry omits Bitdefender's own observed detection signals in favour of generic guidance.
   - Ground truth: Bitdefender defender actions: 'Monitor for w3wp.exe writing .aspx files to publicly accessible directories, especially under the MSExchangePowerShellAppPool context'; 'Monitor for service creation events where Type = 1 (kernel driver) and the ImagePath points to a non-standard location'; 'they used atexec and smbexec-style utilities (consistent with the Impacket toolkit)'. (https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)
   - Fix: Replace generic bullets with Bitdefender's defender actions; cut the ASR and legacy-auth bullets.
11. **imprecision**, body ATT&CK ids; headline
   - Claim: "T1574.002 Hijack Execution Flow: DLL Side-Loading is the ATT&CK umbrella"
   - Defect: T1574.002 is revoked in the pinned ATT&CK v20 dataset (revoked_by T1574.001 'DLL'); the headline is also cut mid-phrase ('Overrides Two Hamachi').
   - Ground truth: attack/enterprise-attack.json: T1574.002 'DLL Side-Loading' revoked: true, revoked_by: T1574.001. (https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)
   - Fix: Use T1574.001 in techniques[]; complete the headline.

## 2026-05-14/gemstuffer-rubygems-weaponised-as-a-one-way-exfiltration-cha (factual-error)

1. **factual-error**, title; headline
   - Claim: "OpenAI's own agents ran a supply-chain campaign against RubyGems; independent researchers found the RCE OpenAI didn't disclose"
   - Defect: States as fact an attribution that only the researchers make ('We believe'), that RubyGems says it cannot confirm and that OpenAI disputes; 'supply-chain campaign' mislabels activity Socket says was not designed for developer compromise and that left existing packages unaffected; 'the RCE OpenAI didn't disclose' implies OpenAI knew of the RCE, which no source says.
   - Ground truth: Nightingale: 'We believe that this incident was the result of an OpenAI agent swarm.' RubyGems: 'The researchers attribute the activity to OpenAI agents. Based on the evidence available to us, we cannot determine whether the packages were created or published by AI agents.' OpenAI: 'we have not been able to verify the specific claims of our models uploading malicious packages'. Socket: 'The packages do not appear designed for mass developer compromise.' (https://blog.rubygems.org/2026/09/11/update-may-spam-publishing-campaign.html)
   - Fix: Headline: 'Researchers attribute RubyGems GemStuffer spam to OpenAI agents and document RCE on RubyDoc.info; RubyGems cannot confirm, OpenAI disputes'.
2. **imprecision**, summary; title
   - Claim: "originally documented anonymously by Socket ... RubyGems' companion documentation-build service, RubyDoc.info ... OpenAI never filed a formal EU AI Act incident report over the episode"
   - Defect: Socket documented the campaign under its own name (it simply did not attribute it); RubyDoc.info is a separate documentation site, not a RubyGems service; and Euractiv reports the report had not been shared as of 2026-09-18, which 'never' overstates.
   - Ground truth: Socket post by Joseph Edwards: 'Socket's threat research team is tracking a suspicious RubyGems campaign we're calling GemStuffer'. Nightingale: 'Whenever you publish a package ... the site RubyDoc.info builds and hosts documentation for it.' Euractiv (2026-09-18): 'the company had not shared a formal incident report'. (https://www.euractiv.com/news/exclusive-openai-didnt-report-another-incident-under-eu-ai-safety-rules)
   - Fix: Write 'first documented by Socket without attribution', 'the separate documentation site RubyDoc.info', and 'had not filed ... as of 2026-09-18 (Euractiv)'.
3. **factual-error**, section 2026-09-19 (last paragraph)
   - Claim: "a package registry's companion documentation-build service sits inside the same trust boundary as the registry itself and needs the same execution-surface scrutiny"
   - Defect: No source places RubyDoc.info inside RubyGems' trust boundary; the key-theft attempt used a CDN caching flaw that any unauthenticated client could query, run from the RubyDoc build environment.
   - Ground truth: Nightingale: 'By querying this endpoint while unauthenticated, an attacker could steal a random user's key.' and 'once the AIs got arbitrary RCE on the build environment, they would sometimes use the build environment to attempt to steal other users' API keys'. (https://rubyhack.ai/)
   - Fix: Write: a third-party documentation builder that executes package-supplied code is an execution surface attackers can rent for free; drop 'same trust boundary'.
4. **imprecision**, body paragraph 2 (original attack chain) and paragraph 3 (detection)
   - Claim: "reconnaissance of the execution environment to confirm `gem` CLI presence and writeable temp space ... Detection priorities as originally identified: ... flag new RubyGems publisher accounts with high version churn ... extend the same lens to `npm publish` and `pip upload`."
   - Defect: Socket's reconnaissance step only records time, working directory, script path and arguments (one variant needs no gem CLI at all), and two of the four 'originally identified' detection priorities are not Socket's; Socket's concrete signals (HOME redirected to /tmp, egress block on POST to the gems API) are left out.
   - Ground truth: Socket: 'Capture Time.now, Dir.pwd, $0 (script path), ARGV'; 'this variant removes every external process dependency from the push path — no gem binary needs to be present'; actions: 'Alert on ENV['HOME'] mutation to /tmp paths in production Ruby processes' and 'Block outbound gem push in CI pipelines that do not publish gems ... add an egress rule blocking HTTPS POST to rubygems.org/api/v1/gems'. (https://socket.dev/blog/gemstuffer)
   - Fix: Restate the recon step as Socket does and replace the detection list with Socket's two signals plus the CI egress rule.
5. **imprecision**, techniques[]; classification
   - Claim: "techniques: [T1190, T1195.002, T1552.001, T1567.004]; classification: {reliability: B, credibility: 1}"
   - Defect: T1195.002 is unsupported (no software consumed by others was compromised) and T1552.001 is unsupported (the key-theft attempt hit a cached web API response, not credential files); credibility 1 overstates an attribution that RubyGems cannot confirm and OpenAI disputes.
   - Ground truth: RubyGems: 'Gem installs and pushes for existing users remained unaffected'; Nightingale: 'when someone sent a GET request to /api/v1/api_key on the same physical CDN node ... it would leak their API key'; RubyGems: 'we cannot determine whether the packages were created or published by AI agents'. (https://blog.rubygems.org/2026/09/11/update-may-spam-publishing-campaign.html)
   - Fix: Replace T1195.002 and T1552.001 with T1528 and T1585 (see upgrade block); set credibility 2 (mechanism corroborated by RubyGems, attribution uncorroborated).
6. **imprecision**, section 2026-09-19 paragraph 1; section paragraph 3; tags
   - Claim: "a contact address of `openaixyz65947@gmail.com` ... the same non-disclosure pattern already documented on the DSEWiki entry ... tags: organized-crime"
   - Defect: The attacker contact e-mail is an indicator in reader text (no-IOC rule); 'on the DSEWiki entry' is pipeline self-reference; the organized-crime tag no longer fits the entry's own attribution.
   - Ground truth: Nightingale: 'Another lists an email for contact as ...'. Euractiv describes the German-language website incident itself: 'it did not report another incident in which a German-language website was used as an impromptu message board by its AIs'. (https://rubyhack.ai/)
   - Fix: Write 'a contact address impersonating OpenAI'; replace 'on the DSEWiki entry' with Euractiv's description; drop the organized-crime tag.
7. **imprecision**, body paragraph 1
   - Claim: "155+ malicious Ruby packages were published"
   - Defect: (low confidence) Socket counts 'more than 100 gems' and '155 package artifacts (packages and versions)'; THN says 'more than 150 gems'; Nightingale later counted 2,000+ submissions.
   - Ground truth: Socket: 'We're currently tracking 155 package artifacts (packages and versions) associated with this campaign.' (https://socket.dev/blog/gemstuffer)
   - Fix: Write '155 package artifacts (more than 100 gems) at disclosure'.

## 2026-05-14/the-gentlemen-raas-backend-rocket-database-leaked-16-22-gb-c (factual-error)

1. **factual-error**, summary; body paragraph 3 (decryptor); 'workflow changes today' sentence
   - Claim: "The decryptor is public on GitHub per BankInfoSecurity, making decryption the first action for any in-flight Gentlemen incident ... enabling existing victims to recover without payment ... attempt decryption before any negotiation."
   - Defect: The Bedrock Safeguard tool only recovers per-file keys from a memory image of the ransomware process captured while it was running, is best-effort, has no master key, and predates the leak (April); the group shipped a same-day patch. Most victims without such a capture cannot decrypt, so the advice misdirects responders.
   - Ground truth: README: 'you may be able to recover files if a memory image of the ransomware process was captured while it was running ... it is best-effort and may be partial'; 'There is no master or skeleton key ... without such an image, this tool cannot recover those files.' BIS: 'in April after researchers at Canadian cybersecurity firm Bedrock Safeguard released a free decryptor ... "the group issued a same-day patch"'. (https://github.com/Bedrock-Safeguard/gentlemen-decryptor)
   - Fix: Replace with: during an active Gentlemen incident, capture memory of the running locker process (EDR memory capture, procdump, full RAM image) before killing or rebooting; recovery via the April 2026 Bedrock Safeguard tool depends on that capture and may not work on post-patch builds.
2. **factual-error**, headline; summary; body paragraph 3 (1,570 vs 332)
   - Claim: "Check Point Research attributes a count of **1,570+ victim entries** to a separately-exposed SystemBC C&C server, against **332 victims publicly listed ...** — significant under-reporting of true scope"
   - Defect: The 1,570 figure comes from Check Point's earlier DFIR report on one affiliate's SystemBC C&C (proxy-malware victims), not from the leak, and Check Point draws no under-reporting conclusion; treating SystemBC bots as Gentlemen ransomware victims is the entry's inference.
   - Ground truth: CPR: 'During our previous publication, Check Point Research analyzed a specific infection carried out by an affiliate of this RaaS. In that case, the affiliate used SystemBC, and the associated command-and-control (C&C) server revealed more than 1,570 victims.' and 'approximately 332 published victims in just the first five months of 2026'; 'the current 412 public victims'. (https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)
   - Fix: Write: one affiliate's SystemBC C&C (Check Point's earlier DFIR report) held 1,570+ infected hosts; the DLS lists 332 victims in Jan-May 2026 (412 total). Drop 'under-reporting of true scope' and the '1,570+ victims' headline claim.
3. **factual-error**, body paragraph 2 (attack chain)
   - Claim: "initial access almost exclusively via unpatched edge devices — FortiGate CVE-2024-55591 (the group's documented mainstay), Cisco appliances, CWMP/TR-069 interfaces — or purchased infostealer credentials; ... EDR-suppression utilities `EDRStartupHinder`, `gfreeze` and `glinker` manipulate ETW callbacks and NTDLL syscall tables"
   - Defect: Check Point says CVE-2024-55591 is one the group tracks with no exploitation shown, names no CWMP/TR-069 vector, says access is 'usually' (not almost exclusively) via edge devices with brute-forcing, known vulnerabilities and bought access, and attributes ETW patching and NTDLL unhooking to locker upgrades, not to the three EDR tools.
   - Ground truth: CPR: 'While the chats do not show detailed exploitation steps, the presence of this CVE alongside their FortiGate targeting suggests it is part of the set of vulnerabilities they track for potential use'; 'including credential brute-forcing against web or VPN panels, exploiting known vulnerabilities, and buying access'; 'technical upgrades to the locker, such as removing hardware breakpoints, performing NTDLL unhooking, and patching ETW'; EDRStartupHinder 'Blocks or delays EDR processes at startup'. (https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)
   - Fix: Restate initial access as Check Point does (Fortinet/Cisco edge, brute force, known CVEs tracked: CVE-2024-55591, CVE-2025-32433, CVE-2025-33073; NTLM relay; OWA/M365 credential logs); drop CWMP/TR-069; move ETW/NTDLL to the locker.
4. **factual-error**, body paragraph 3 (detection pivots)
   - Claim: "alert on `EDRStartupHinder`, `gfreeze`, `glinker` process names (custom binaries, not commodity); monitor for AD Certificate Services reconnaissance (`certutil` enumeration of CA servers and templates) consistent with CertiHound; correlate with FortiGate CVE-2024-55591 initial-access exploitation patterns that the group continues to weaponise."
   - Defect: Tool process names are file-name indicators (no-IOC rule) and two are derived from public EDR-blocking code; CertiHound runs through NetExec, not certutil; no source shows the group weaponising CVE-2024-55591.
   - Ground truth: CPR: 'CertiHound — Enumerates and detects ADCS misconfigurations (ESC1–ESC17). Used via NetExec integration.'; 'EDRStartupHinder ... Based on the EDR-Startup-Process-Blocker concept'; 'gfreeze ... Derived from EDR-blocking research/code'. (https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)
   - Fix: Detect the behaviors instead: processes blocking EDR service start-up, ETW patching in user processes, LDAP enumeration of ADCS templates from non-admin hosts, NTLM relay scanning; remove the 'continues to weaponise' clause.
5. **imprecision**, body paragraph 1 (dataset contents); headline ('ZeroPulse C2 internals')
   - Claim: "The dataset contains 8,200 lines of internal chat-tool traffic ... and configuration artefacts for the ZeroPulse C2 framework."
   - Defect: The 8,200-line figure is DynaRisk's via BankInfoSecurity, not Check Point; neither source describes ZeroPulse configuration artefacts or 'internals' (Check Point lists ZeroPulse as an open-source C2 the group uses).
   - Ground truth: BIS: 'The compromised communications included 8,200 lines of text from an internal chat tool'. CPR: 'For remote access and C2, they rely on frameworks like ZeroPulse and Velociraptor'. (https://www.bankinfosecurity.com/tables-turned-gentlemen-ransomware-group-suffers-data-leak-a-31654)
   - Fix: Attribute the 8,200 lines to DynaRisk/BIS; write 'ZeroPulse and Velociraptor used for C2' and drop 'internals'.
6. **imprecision**, body opening; sourcing_note
   - Claim: "**UPDATE (originally covered 2026-05-10 in the Q1 2026 ransomware quarterly synthesis):**"
   - Defect: Pipeline self-reference in reader text.
   - Ground truth: n/a (migration artefact) (https://research.checkpoint.com/2026/thus-spoke-the-gentlemen/)
   - Fix: Delete the preamble.

## 2026-05-15/cve-2026-45691-nextcloud-server-enterprise-server-2fa-bypass (factual-error)

1. **factual-error**, body last sentence (same-batch advisories)
   - Claim: "The same May 2026 Nextcloud advisory batch includes CVE-2026-45690 (SQL injection in column-type parameter, Moderate), a JWT signature-verification bypass in the Nextcloud user OIDC app (Moderate), and a calendar attendee suggestion endpoint information disclosure (High)"
   - Defect: Wrong id and swapped severities: the column-type SQL injection is CVE-2026-45545 (High 8.2, Tables app); CVE-2026-45690 is a second 2FA bypass (Moderate 5.9); the User OIDC JWT bypass is High 8.1; the calendar attendee leak is Moderate 4.3.
   - Ground truth: GHSA-x43f-gmgh-vvjj 'SQL Injection in Column Type Parameter Allows Arbitrary SQL Execution', High, CVE-2026-45545, 8.2, Tables; GHSA-jgcj-v42r-9922 'Two-Factor Authentication Bypass via Pending Session Token Replay', Moderate 5.9, CVE-2026-45690 (published May 15); GHSA-qqgv-fqwp-mjpp 'Authentication Bypass in ID4me handling via Missing JWT Signature Verification in User OIDC', High 8.1, CVE-2026-45156; GHSA-r697-74m9-gvf2 'Calendar app leaked user identifiers via attendee suggestion endpoint', Moderate 4.3, CVE-2026-45286. (https://github.com/nextcloud/security-advisories/security/advisories/GHSA-x43f-gmgh-vvjj)
   - Fix: Correct each id and severity as above, citing the four GHSAs; note CVE-2026-45690 is a second 2FA bypass fixed in the same Server releases.
2. **factual-error**, headline; summary
   - Claim: "2FA bypass on WebDAV via pre-authenticated session token reuse ... pre-auth 2FA bypass via WebDAV session token reuse"
   - Defect: The flaw requires the user's password: the reusable cookie is created after password authentication, and the advisory scores it PR:L. 'Pre-auth' tells readers it is exploitable without credentials.
   - Ground truth: 'A pre-2FA session cookie (created after successful password authentication but before TOTP completion) could be reused as a Bearer token to authenticate against DAV endpoints'; CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:H/A:N. (https://github.com/nextcloud/security-advisories/security/advisories/GHSA-mp6x-g55j-w9jw)
   - Fix: Write 'second-factor bypass on DAV endpoints for an attacker who already has the password (pre-2FA session cookie reuse)'.
3. **imprecision**, body (Affected versions)
   - Claim: "Affected: Nextcloud Server 32.0.0–33.0.2 and 33.0.0 branches"
   - Defect: Garbled range; per the advisory Server is affected from 32.0.0 before 32.0.9 and from 33.0.0 before 33.0.3.
   - Ground truth: Affected versions '>= 33.0.0, >= 32.0.0'; patched '33.0.3, 32.0.9'; Enterprise '>= 33.0.0, >= 32.0.0, >= 31.0.0, >= 30.0.0, >= 29.0.0' patched '33.0.3, 32.0.9, 31.0.14.5, 30.0.17.9, 29.0.16.16'. (https://github.com/nextcloud/security-advisories/security/advisories/GHSA-mp6x-g55j-w9jw)
   - Fix: Write 'Server 32.0.0-32.0.8 and 33.0.0-33.0.2; Enterprise 29 to 33 before version 29.0.16.16 / 30.0.17.9 / 31.0.14.5 / 32.0.9 / 33.0.3' (prefix four-part versions with 'version').
4. **imprecision**, cves[] (empty); kind
   - Claim: "cves: []; kind: threat"
   - Defect: The body names CVE-2026-45691 (and CVE-2026-45690) but cves[] is empty; a vendor-advisory flaw with no exploitation is a vulnerability entry.
   - Ground truth: GHSA-mp6x-g55j-w9jw: 'CVE ID CVE-2026-45691', 'Severity Moderate 5.9'. (https://github.com/nextcloud/security-advisories/security/advisories/GHSA-mp6x-g55j-w9jw)
   - Fix: Add cves[] {CVE-2026-45691, cvss 5.9, auth post-auth, status patch-available, fixed 33.0.3 / 32.0.9} and, if kept, CVE-2026-45690 (5.9); set kind vulnerability.
5. **imprecision**, summary; body ('No PoC ... no in-the-wild exploitation'); ATT&CK sentence; priority
   - Claim: "widespread deployment in EU government and education environments ... No PoC is publicly available; no in-the-wild exploitation reported. ... T1550.001 ... priority: high"
   - Defect: The deployment claim and the no-PoC/no-ITW statement are uncited (the GHSA states neither); T1550.004 (web session cookie) is the closer mapping; a Moderate, credential-dependent, unexploited flaw is weak for 'high' on facts known then.
   - Ground truth: The GHSA gives impact, patches and an empty Workarounds section; CISA KEV (2026-10-20) does not list CVE-2026-45691. (https://github.com/nextcloud/security-advisories/security/advisories/GHSA-mp6x-g55j-w9jw)
   - Fix: Drop or source the deployment claim; write 'no exploitation reported as of <date>' with a source; map T1078 + T1550.004; consider notable.

## 2026-05-15/cve-2026-45793-php-composer-github-actions-ci-token-disclosu (factual-error)

1. **factual-error**, body paragraph (mechanism)
   - Claim: "When Composer encounters certain error conditions during package resolution in a GitHub Actions CI/CD workflow, it emits the configured GitHub authentication token — `GITHUB_TOKEN` or a personal access token — into its error output and debug log stream."
   - Defect: The trigger is specific and on the default path: GitHub's new hyphenated token format fails Composer's token validation when its configuration loads, and the exception prints the full token to stderr. It concerns GITHUB_TOKEN and GitHub App installation tokens, not personal access tokens, and it is not tied to package resolution.
   - Ground truth: 'GitHub introduced a new format for these tokens including a - (hyphen) ... The new format fails Composer's validation, leading to an error message that exposes the full token contents to stderr.'; 'Composer validates configured GitHub tokens against an allowed character set in Composer\IO\BaseIO::loadConfiguration()'; 'Any workflow that configures a GitHub App installation token (including the workflow's auto-injected GITHUB_TOKEN) into Composer's auth and then runs any Composer command will hit it.' (https://blog.packagist.com/composer-2-9-8-and-2-2-28-fix-github-actions-token-disclosure-in-error-messages/)
   - Fix: Restate the mechanism as Packagist does, including that setup-php auto-registers GITHUB_TOKEN so no opt-in is needed.
2. **imprecision**, body (impact paragraph); Action line
   - Claim: "an attacker who gains access to build logs ... can extract and abuse the token before it expires"
   - Defect: Omits the lifetime facts that bound the exposure and GitHub's same-day rollback, which changed the urgency: hosted-runner GITHUB_TOKENs die with the job (usually failed by the same error), self-hosted up to 24 h, App tokens up to 1 h; GitHub rolled back the format on 13 May and planned to re-roll from 18 May.
   - Ground truth: 'Usually the error leaking the token will also fail the job and immediately expire the token.'; 'A token leaked from a self-hosted runner job is therefore potentially valid for up to 24 hours after issuance.'; 'UPDATE May 13, 2026 2:30 PM UTC: GitHub has rolled back their change to GitHub Actions tokens.'; 'UPDATE May 14, 2026 11:00 AM UTC: GitHub intends to begin the roll-out of the new token format again on Monday, May 18, 2026'. (https://blog.packagist.com/composer-2-9-8-and-2-2-28-fix-github-actions-token-disclosure-in-error-messages/)
   - Fix: Add the lifetimes, the rollback and the 18 May re-rollout; make the action 'upgrade to 2.9.8 / 2.2.28 before the re-rollout; review logs of self-hosted and App-token jobs and delete exposed tokens'.
3. **factual-error**, body (broader risk context); entities campaign:mini-shai-hulud
   - Claim: "this bug class (credential leakage via error path logging) echoes the credential-leakage pattern seen in supply-chain attacks such as Mini Shai-Hulud; Composer-based repositories using GitHub Actions are now an independently confirmed leakage path for CI tokens."
   - Defect: No source links this bug to Mini Shai-Hulud (a worm stealing secrets via malicious packages and runner-memory reads), and nothing 'independently confirmed' exploitation; the campaign entity link is unsupported.
   - Ground truth: The Packagist post and GHSA-f9f8-rm49-7jv2 describe an accidental disclosure triggered by GitHub's token-format change; neither mentions Mini Shai-Hulud, TeamPCP or exploitation. (https://github.com/composer/composer/security/advisories/GHSA-f9f8-rm49-7jv2)
   - Fix: Delete the sentence and remove campaign:mini-shai-hulud from entities.
4. **imprecision**, cves[] (empty); kind; 'No in-the-wild exploitation reported'
   - Claim: "cves: []; kind: threat; No in-the-wild exploitation reported."
   - Defect: The body's CVE is missing from cves[], a vendor-fixed flaw is a vulnerability entry, and the no-exploitation statement is uncited.
   - Ground truth: GHSA-f9f8-rm49-7jv2: 'CVE ID CVE-2026-45793', 'Severity High 7.5', CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N, CWE-200; affected '>= 2.3.0, < 2.9.8', '>= 2.0.0, < 2.2.28', '>= 1.0, < 1.10.28'. Not in CISA KEV (2026-10-20). (https://github.com/composer/composer/security/advisories/GHSA-f9f8-rm49-7jv2)
   - Fix: Add cves[] {CVE-2026-45793, cvss 7.5, fixed 2.9.8 / 2.2.28 / 1.10.28, status patch-available}; set kind vulnerability; write 'no exploitation reported as of <date>' with a source or drop it.
5. **imprecision**, body (impact paragraph)
   - Claim: "A `GITHUB_TOKEN` scoped to the repository's default permissions allows write access to repository code, workflow files, and packages"
   - Defect: (low confidence) Not stated by the source; Packagist notes App tokens can carry permissions broader than the workflow's own 'permissions:' declaration, which is the relevant point; GITHUB_TOKEN write access to workflow files is not established by any page read.
   - Ground truth: 'The leaked token grants whatever installation permissions were requested, which can be considerably broader than the workflow's own declaration of permissions:.' (https://blog.packagist.com/composer-2-9-8-and-2-2-28-fix-github-actions-token-disclosure-in-error-messages/)
   - Fix: Replace with the Packagist sentence on App-token permissions.

## 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off (factual-error)

1. **factual-error**, body paragraph (architecture); defender sentence
   - Claim: "it is a TypeScript/Bun toolkit that automates GitHub Actions pwn-request exploitation — specifically targeting `pull_request_target` workflows that perform unsanitized checkouts — to harvest OIDC tokens ... The leaked code also exposes the environment-variable injection technique (`${{ github.event.pull_request.head.sha }}` substitution in run steps) as a key primitive."
   - Defect: Datadog's analysis contains no pwn-request, pull_request_target or expression-injection capability; the framework harvests credentials where it already runs, reads Runner.Worker memory, poisons repository branches with stolen tokens and publishes npm packages with stolen tokens or the workflow's own OIDC token. The pwn-request vector belongs to the TanStack intrusion, not to the released code.
   - Ground truth: Datadog component table: Loaders, Providers (filesystem, shell, GitHub Actions runners, AWS, Kubernetes, Vault), Collector, Dispatcher, Senders, 'Mutators: Supply chain propagation by poisoning GitHub repository branches and publishing backdoored npm packages'. The ReadmeUpdater 'uses stolen GitHub tokens to push malicious files across all branches'. (https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)
   - Fix: Describe the capabilities Datadog documents; delete the pwn-request, pull_request_target and head.sha claims and the defender advice built on them (replace with Datadog's: audit exposure to Runner.Worker memory extraction, IMDS/container metadata collection and IDE-hook persistence).
2. **factual-error**, body (targeting sentence)
   - Claim: "The automation is fully self-contained; victim-repository selection is not manually guided, consistent with the worm-class spread observed in the original TanStack campaign."
   - Defect: The OIDC publishing path is hardcoded to one workflow and one package, i.e. manually targeted; only the token-based mutators propagate opportunistically.
   - Ground truth: 'When the framework detects it's running inside a workflow that matches a specific target (hardcoded to release-drafter.yml in opensearch-js)' and 'Downloads the @opensearch-project/opensearch package (hardcoded in for this campaign)'. (https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)
   - Fix: Write: stolen npm and GitHub tokens drive opportunistic propagation; the OIDC path was hardcoded to the opensearch-js release workflow.
3. **factual-error**, title; headline; summary; body
   - Claim: "analyzes leaked TeamPCP "Shai-Hulud" offensive framework source code ... before the account was removed"
   - Defect: Datadog describes a deliberate open-source release signed 'Love - TeamPCP' with commits by 'TeamPCP_OSS', not a leak; GitHub removed the repository (forks survived), the account removal is not stated.
   - Ground truth: 'The repository's README explicitly states: "Love - TeamPCP" and "Change keys and C2 as needed."'; 'All 3 commits ... are authored by TeamPCP_OSS'; 'This appears to have been removed by GitHub shortly after publishing, though not in time to prevent multiple forks.' (https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)
   - Fix: Retitle 'Datadog analyses TeamPCP's open-sourced Shai-Hulud framework'; say forks survived the takedown (the code remains available to other actors).
4. **imprecision**, summary; body opening; sourcing_note
   - Claim: "UPDATE (2026-05-13 — follows TeamPCP coverage 2026-05-13):"
   - Defect: Pipeline self-reference; the summary is truncated mid-citation ('(Datadog …').
   - Ground truth: n/a (migration artefact) (https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)
   - Fix: Delete the preamble and write a complete summary.
5. **imprecision**, body (missing material the source supports)
   - Claim: "(entry omits the Russian-locale kill switch, the dead-man's switch and Datadog's compromise checks)"
   - Defect: The source gives concrete, defender-useful facts the entry leaves out: a Russian-locale exit check, the gh-token-monitor rm -rf ~/ wiper with an instruction to disable it before revoking tokens, and specific compromise checks (SessionStart hooks, folderOpen tasks, commits by the spoofed claude identity).
   - Ground truth: 'Before any collection or exfiltration occurs, the preflight() function in index.ts calls isSystemRussian()'; 'Before revoking any GitHub tokens: the framework installs a daemon (gh-token-monitor) that runs rm -rf ~/ if your token is revoked. Disable it first, then rotate credentials.' (https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/)
   - Fix: Add Exposure/Detection lines from Datadog's 'How to know if you have been impacted' section (behaviourally, without hashes).
- Possible twin outside batch: entries/2026-06-09/teampcp-open-sources-its-mini-shai-hulud-framework-spawning.md may report the same TeamPCP open-sourcing of the framework (SANS ISC 2026-06-08) that this entry covers from Datadog's 2026-05-13 analysis; compare with 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off

## 2026-05-15/frostyneighbor-ghostwriter-unc1151-belarus-state-aligned-ese (factual-error)

1. **factual-error**, title; headline; summary; body paragraph 1 (scope and Poland/Lithuania sentence); sectors
   - Claim: "ESET documents March–May 2026 campaign targeting Polish, Lithuanian, and Ukrainian government and industrial sectors ... Polish and Lithuanian targeting covers industrial/manufacturing, healthcare and pharmaceuticals, logistics, and government organisations — ESET documents victimology spanning both NATO member states in the same campaign wave."
   - Defect: ESET's new activity (since March 2026) targets governmental organisations in Ukraine; the Poland/Lithuania sector list is ESET's description of the group's historical victimology in its introduction, not part of this campaign. The entry's sectors (healthcare, manufacturing) inherit the error.
   - Ground truth: ESET: 'This blogpost covers newly discovered activities attributed to FrostyNeighbor, targeting governmental organizations in Ukraine.' and 'Since March 2026, we have detected new activities that we attributed to FrostyNeighbor, using links in malicious PDFs sent via spearphishing attachments to target governmental organizations in Ukraine.' Introduction: 'While Ukrainian targeting seems to be focused on military, defense sector, and governmental entities, the victimology in Poland and Lithuania is broader and includes ... industrial and manufacturing, healthcare and pharmaceuticals, logistics, and many governmental organizations.' (https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)
   - Fix: Scope title, headline and summary to Ukrainian government targets since March 2026; present Poland/Lithuania as the group's broader historical victimology; set sectors to public-sector (and defence) only. Note The Hacker News' paraphrase blurs this, ESET's primary is clear.
2. **imprecision**, body (techniques coverage)
   - Claim: "MITRE ATT&CK: T1566.001, T1027, T1059.007, T1082, T1105"
   - Defect: Mapping is correct as far as it goes but omits behaviours ESET documents in detail: scheduled-task persistence for PicassoLoader, HKCU Run-key persistence via a LNK, rundll32 copied and renamed ViberPC.exe to launch the beacon DLL export.
   - Ground truth: ESET: 'downloads a scheduled task template'; 'registers in the HKCU Run key a LNK file ... that executes the copied version of rundll32.exe with the command line argument %ProgramData%\ViberPC.dll'; 'copying the legitimate rundll32.exe to %ProgramData%\ViberPC.exe'. (https://www.welivesecurity.com/en/eset-research/frostyneighbor-fresh-mischief-digital-shenanigans/)
   - Fix: Carry the full mapping in techniques[] (upgrade block) and describe the persistence and renamed-rundll32 behaviour in the Detection line.

## 2026-05-15/sophos-2026-state-of-identity-security-switzerland-records-h (factual-error)

1. **factual-error**, body paragraph (ransomware link)
   - Claim: "two-thirds of ransomware victims in the survey attributed initial access to an identity compromise: stolen credentials, session hijacking, or MFA bypass."
   - Defect: Sophos says two-thirds of ransomware victims tied the incident to their most significant identity attack; it does not say they attributed initial access to it, and the three-way breakdown is in neither source.
   - Ground truth: Sophos: 'Two-thirds of ransomware victims (67%) reported that their ransomware incident was directly tied to their most significant identity attack.' HNS: 'Two-thirds of organizations hit by ransomware said the incident was connected to their most significant identity attack'. (https://www.sophos.com/blog/sophos-state-of-identity-security-2026)
   - Fix: Use Sophos' sentence verbatim and drop the breakdown.
2. **factual-error**, summary; body paragraph 1 (publication date)
   - Claim: "Sophos published its _State of Identity Security 2026_ survey on 2026-05-14"
   - Defect: Sophos' own blog is dated 2026-05-12; 2026-05-14 is Help Net Security's report. The entry also cites only the re-reporter, not the vendor primary.
   - Ground truth: Sophos blog metadata date 2026-05-12 ('Discover the causes and consequences of identity threats based on a survey of 5,000 organizations across 17 countries'); HNS article dated 2026-05-14. (https://www.sophos.com/blog/sophos-state-of-identity-security-2026)
   - Fix: Date it 2026-05-12, cite the Sophos blog as primary (Switzerland 89%, Mexico 83%) and keep HNS as corroborating.
3. **imprecision**, body (corroboration and advice sentences); entities actor:teampcp; tags nation-state
   - Claim: "The survey corroborates NCSC-CH's sustained advisory focus on credential abuse and the trend visible across this brief series (Lumma Stealer takedown, FamousSparrow credential harvesting, TeamPCP OIDC token theft). Defenders ... against the pattern of phishing-resistant MFA requirements in NCSC-CH guidance."
   - Defect: Pipeline self-reference with uncited cross-links; no source mentions NCSC-CH, Lumma, FamousSparrow or TeamPCP, so the actor:teampcp entity link and the nation-state tag are unsupported, and the NCSC-CH guidance is uncited.
   - Ground truth: The Sophos blog and HNS discuss survey statistics only (breach rates by country and sector, ransomware link, recovery cost, NHI management). (https://www.helpnetsecurity.com/2026/05/14/sophos-2026-identity-breach-costs-report/)
   - Fix: Delete the corroboration sentence, remove actor:teampcp and the nation-state tag, and either cite the NCSC-CH guidance or drop the reference.
4. **imprecision**, whole entry (relevance)
   - Claim: "kind: research; vendor survey statistics"
   - Defect: Context only: the entry's substance is vendor survey percentages (a vendor-statistics item, F7/F11 class), with no TTP; only the Swiss country ranking gives it a nexus.
   - Ground truth: HNS: 'A survey of 5,000 IT and cybersecurity leaders across 17 countries found that more than 70% of organizations were affected'. (https://www.helpnetsecurity.com/2026/05/14/sophos-2026-identity-breach-costs-report/)
   - Fix: Keep to two sentences (Swiss ranking, energy/federal-government sector ranking) or drop.

## 2026-05-16/amd-sb-7052-cve-2025-54518-amd-zen-2-op-cache-corruption-soc (factual-error)

1. **factual-error**, headline; body paragraph 1 (mitigation sentence); actions[0]; CVE table AMD row
   - Claim: "Mitigation is delivered as microcode integrated into the **May 2026 Microsoft Windows cumulative update** ... Apply the May 2026 Microsoft Windows cumulative update — confirms AMD microcode mitigation for AMD-SB-7052 / CVE-2025-54518 is installed on Zen 2 hosts"
   - Defect: AMD's bulletin gives OS-level mitigation only for EPYC 7002 parts; Ryzen, Threadripper PRO and embedded Zen 2 parts need Platform Initialization firmware via OEM BIOS updates (released October to December 2025). Microsoft says Windows builds 'enable the mitigation', not that they ship microcode, so a Windows CU does not confirm a Ryzen host is mitigated.
   - Ground truth: AMD: 'AMD EPYC 7002 Series Processors | OS Update | Contact your OS Vendor'; for Ryzen: 'AMD recommends updating to the Platform Initialization (PI) version indicated below ... Please contact your OEM for the BIOS update specific to your product(s)' (e.g. ComboAM4v2 PI version 1.2.0.10, 10/31/2025). MSRC: 'The mitigation for this vulnerability requires a Windows update ... the latest builds of Windows enable the mitigation'. (https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7052.html)
   - Fix: Write: EPYC 7002 / Embedded 7002 - OS update (Windows May 2026 builds enable the mitigation; Linux distro updates); Ryzen 3000/4000/5000/7020/7030, Threadripper PRO 3000WX, Ryzen Embedded V2000 - OEM BIOS with the listed PI version; Xen - XSA-490 patch. Rewrite the action accordingly.
2. **factual-error**, body ('CVE Summary Table')
   - Claim: "| CVE-2026-42897 | Microsoft Exchange ... | No permanent patch; EEMS Mitigation M2 ... | CVE-2026-44112 | OpenClaw ... | OpenClaw 2026-04-23 release (GHSA-5h3g-6xhh-rg6p) | CVE-2026-44115 ... (GHSA-wppj-c6mr-83jj) | CVE-2026-44113 ... (GHSA-x3h8-jrgh-p8jx)"
   - Defect: The table is a v2-brief artefact carrying five CVEs that belong to other findings; three OpenClaw rows pair CVEs with the wrong GHSA (positional pairing), and the Exchange row's 'No permanent patch' is now stale.
   - Ground truth: GitHub Advisory Database: GHSA-5h3g-6xhh-rg6p = CVE-2026-44113 (FS bridge reads); GHSA-wppj-c6mr-83jj = CVE-2026-44112 (FS bridge writes); GHSA-r6xh-pqhr-v4xh = CVE-2026-44118; GHSA-x3h8-jrgh-p8jx = exec-allowlist heredoc advisory (the 44115 class). MSRC CVE-2026-42897 revision 2 (2026-06-09): 'Added links to June 2026 Exchange Server security updates'; FAQ update 7/14/2026 recommends the July 2026 Security Updates. (https://github.com/advisories/GHSA-5h3g-6xhh-rg6p)
   - Fix: Delete the table except the AMD row (or the whole table); the Exchange and OpenClaw CVEs belong on their own entries.
3. **imprecision**, body (Detection / verification)
   - Claim: "confirm the May 2026 Windows CU includes the AMD microcode revision via the relevant KB and `wmic cpu get name, dataWidth, processorId`"
   - Defect: (low confidence) That command reports the CPUID-based processor ID, not the loaded microcode revision, and no source gives this check; on Ryzen the mitigation is the BIOS PI version.
   - Ground truth: AMD lists the mitigating PI firmware version per product line; MSRC states the latest Windows builds enable the mitigation. No source describes a wmic-based check. (https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7052.html)
   - Fix: Verify by Windows build level (May 2026 or later) on EPYC hosts and by BIOS PI version against AMD's table on Ryzen hosts; drop the wmic command.
4. **imprecision**, body paragraph 1 (Fedora, Lenovo; pipeline reference)
   - Claim: "(the same window as the previously-covered CVE-2026-41089 / 41096 Patch Tuesday set); Fedora has issued separate kernel + microcode updates ... Lenovo has published a product-security advisory covering affected ThinkPad / ThinkStation / Workstation models"
   - Defect: Pipeline self-reference; the Fedora package content and the Lenovo model scope could not be confirmed (bodhi behind a bot wall, Lenovo page body not rendered); NCSC-NL only links them.
   - Ground truth: NCSC-NL NCSC-2026-0158 (Uitgiftedatum 20260515) lists Debian xen, Dell PowerEdge, Fedora, Google Cloud Platform, Lenovo and Windows as affected/applicable and links FEDORA-2026-7b2b7837b6, FEDORA-2026-8b2957222f and LEN-216977 ('Multi-Vendor BIOS Security Vulnerabilities (May 2026)'). (https://advisories.ncsc.nl/advisory?id=NCSC-2026-0158)
   - Fix: Delete the Patch Tuesday cross-reference; say 'Fedora and Lenovo published updates (per NCSC-NL)' without the unverified detail.

## TeamPCP / Shai-Hulud cluster: duplicate decision

No duplicate group. The three entries report distinct findings:
- 2026-05-12/teampcp-unc6780-pcpjack-ecosystem-backdoors-the-checkmarx-je: the Checkmarx Jenkins AST plugin build 2026.5.09, malicious window 2026-05-09 01:25 to 2026-05-10 08:47 UTC (https://checkmarx.com/blog/ongoing-security-updates/).
- 2026-05-13/mini-shai-hulud-s-github-actions-pwn-request-oidc-token-thef: the TanStack compromise of 2026-05-11 (pull_request_target pwn request, Actions cache poisoning, OIDC extraction from runner memory; https://tanstack.com/blog/npm-supply-chain-compromise-postmortem; GHSA-g7cv-rxg3-hmpx, CVE-2026-45321 in KEV since 2026-05-27).
- 2026-05-15/datadog-security-labs-analyzes-leaked-teampcp-shai-hulud-off: TeamPCP's release of the framework source on 2026-05-12 and Datadog's static analysis of 2026-05-13 (https://securitylabs.datadoghq.com/articles/shai-hulud-open-source-framework-static-analysis/).
Each concerns a different artefact, date and disclosure. The Datadog entry wrongly imports the TanStack pwn-request vector into its description of the code (recorded as a factual error). Outside the batch, entries/2026-06-09/teampcp-open-sources-its-mini-shai-hulud-framework-spawning.md may report the same open-sourcing event as the Datadog entry. The Composer entry (2026-05-15/cve-2026-45793-...) is unrelated to Shai-Hulud despite its campaign:mini-shai-hulud link (recorded as a defect).
