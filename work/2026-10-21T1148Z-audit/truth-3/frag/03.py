P = 'work/2026-10-21T1148Z-audit/truth-3/bodies/'
S1 = 'https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/'
ENTRY = {
 'entry': '2026-05-16/sentinelone-living-off-the-pipeline-ci-cd-subversion-taxonom',
 'verdict': 'factual-error',
 'defects': [
  {'where': 'body paragraph 1 (defender monitoring priorities sentence)',
   'claim': 'Defender monitoring priorities surfaced in the report: GitHub / GitLab audit logs for `runner.registered` events with unfamiliar names or unexpected source IP ranges; ... suspicious child-process spawn from build agents (`cmd.exe`, `powershell.exe`, `curl`, `wget` outside baseline)',
   'defect': 'The report names no audit-log event (`runner.registered`), no source-IP criterion and no child-process names; these specifics are attributed to the report but are the entry\'s own.',
   'ground_truth': 'Security teams need to know when new runners are registered, when build configurations change unexpectedly, when secrets are introduced into workflows ... Build runners should be treated as high-value systems, monitored for suspicious child processes, credential access attempts, reverse tunnels, and persistence mechanisms. Unauthorized registrations or unusual runner names should trigger immediate investigation.',
   'ground_truth_url': S1,
   'fix': 'Keep the report\'s own list (new runner registrations and unusual runner names; new or modified pipelines created by service accounts; jobs touching unfamiliar repositories; workflows that open network tunnels; suspicious child processes, credential access and reverse tunnels on build runners) and drop the event name, IP-range criterion and binary names, or move them out of the "surfaced in the report" attribution.',
   'class': 'factual-error'},
  {'where': 'body paragraph 1 (MITRE ATT&CK list: T1547, T1555)',
   'claim': '[T1547] (rogue runner registration as persistence), [T1555] (pipeline secret extraction)',
   'defect': 'Wrong techniques for the described behavior. T1547 is Boot or Logon Autostart Execution and T1555 is Credentials from Password Stores; the report describes a registered self-hosted runner giving "persistent, authorized access" and scripts that "harvested tokens, inspected environments". The report itself cites no ATT&CK ids.',
   'ground_truth': 'Once a malicious runner is registered, the attacker gains persistent, authorized access inside the development pipeline ... These scripts harvested tokens, inspected environments, and in some cases targeted locally hosted AI systems.',
   'ground_truth_url': S1,
   'fix': 'Remove T1547 (no enterprise technique fits runner registration cleanly) and replace T1555 with T1552 (Unsecured Credentials); move the ids into techniques[]. Supported ids: T1190, T1078, T1072, T1195.001, T1195.002, T1566, T1204.004, T1552 (see upgrade block).',
   'class': 'factual-error'},
  {'where': 'headline; summary; body paragraph 1 (sentence 1)',
   'claim': 'a practitioner-focused taxonomy of CI/CD pipeline subversion techniques, illustrated with three real intrusion case studies ... immediately useful for SOC and DevSecOps teams',
   'defect': 'The post is a narrative vendor blog with no taxonomy. It describes at least five examples (TeamCity server, GitLab service-account token, the Contagious Interview campaign, rogue runners and discussion-comment workflows from Sha1-Hulud, poisoned packages and maintainer-account phishing); "three" is not in the source and the Contagious Interview item is a campaign, not an intrusion case study. "immediately useful" is an uncited editorial claim.',
   'ground_truth': 'In one case, attackers exploited a vulnerable self-hosted TeamCity server ... One observed intrusion, noted in this year\'s Annual Threat Report, involved the compromise of a GitLab service account token. ... Campaigns like Contagious Interview used fraudulent job offers ... In the Sha1-Hulud campaign, malware infected systems and registered them as self-hosted GitHub runners',
   'ground_truth_url': S1,
   'fix': 'SentinelOne\'s post walks through a TeamCity intrusion, a GitLab service-account intrusion, the Contagious Interview campaign and Sha1-Hulud behaviors (rogue runners, comment-triggered workflows) as examples of CI/CD subversion; drop "taxonomy", "three" and "immediately useful".',
   'class': 'imprecision'},
  {'where': 'headline',
   'claim': '...three real intrusion cases (TeamCity, GitLab service-account pivot, Contagious',
   'defect': 'Headline string is cut mid-word ("Contagious"), truncated at migration.',
   'ground_truth': 'title field ends "..., Contagious Interview)"',
   'ground_truth_url': 'entries/2026-05-16/sentinelone-living-off-the-pipeline-ci-cd-subversion-taxonom.md',
   'fix': 'Complete or shorten the headline.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (Case 1); cves[]',
   'claim': 'an unpatched TeamCity server (CVE-2023-42793) exploited to deploy backdoors via privileged build tasks, remaining undetected for 12+ months; cves: []',
   'defect': 'The article text names no CVE; CVE-2023-42793 is only the target of a hyperlink to the JetBrains advisory, and the text says "vulnerable", not "unpatched" and "a backdoor", not backdoors. The body names the CVE but cves[] is empty.',
   'ground_truth': 'attackers exploited a vulnerable self-hosted TeamCity server and remained undetected for more than a year ... a trusted build agent running with SYSTEM privileges. That build job then deployed a backdoor into internal environments. (JetBrains: CVE-2023-42793, TeamCity On-Premises, fixed in 2023.05.4; CISA KEV dateAdded 2023-10-04, ransomware use "Known")',
   'ground_truth_url': S1,
   'fix': 'a vulnerable self-hosted TeamCity server (the post links JetBrains\' CVE-2023-42793 advisory) ...; add cves[] CVE-2023-42793 (authentication bypass to RCE, fixed 2023.05.4, KEV 2023-10-04) with the JetBrains advisory as its source.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (Case 2)',
   'claim': 'a clean demonstration of how service-account over-privilege translates directly into production code execution',
   'defect': 'The post never says the service account was over-privileged or that execution reached production; it says the build system treated the attacker\'s commands as authorized automation.',
   'ground_truth': 'The attacker used the token to create projects containing malicious Ansible playbooks, which were then automatically executed by the organization\'s CI/CD pipeline. The build system treated the attacker\'s commands as authorized automation',
   'ground_truth_url': S1,
   'fix': 'Delete the over-privilege/production gloss or mark it as the entry\'s analysis.',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (additional vectors sentence)',
   'claim': 'dependency poisoning with reconnaissance `preinstall` scripts ... the article cross-links a separate SentinelOne analysis of the "Sha1-Hulud" NPM compromise as a related supply-chain case',
   'defect': 'The post says only "reconnaissance scripts during installation"; `preinstall` and "NPM" are not in the text. Rogue self-hosted runners and discussion-comment workflow triggers are described by the post as behaviors of the Sha1-Hulud campaign itself, not as separate vectors alongside a cross-link.',
   'ground_truth': 'In the Sha1-Hulud campaign, malware infected systems and registered them as self-hosted GitHub runners under attacker-defined names. ... The campaign also used malicious workflow triggers ... when a user posted a comment in a repository discussion. / Attackers published malicious versions of popular build packages that executed reconnaissance scripts during installation.',
   'ground_truth_url': S1,
   'fix': 'Attribute rogue runners and comment-triggered workflows to Sha1-Hulud; say "reconnaissance scripts run during package installation".',
   'class': 'imprecision'},
  {'where': 'body paragraph 1 (Case 3; closing line; citations)',
   'claim': 'Case 3: the Contagious Interview campaign using fraudulent job offers directing developer victims to fake skill-assessment sites that deploy malware silently ... Single-source — SentinelOne only.',
   'defect': 'Case 1 to 3 and the closing sentences carry no inline citation (only sentence 1 does). Case 3 omits the mechanism the post gives (victims instructed to run commands to "fix" a fabricated error) and the crypto/blockchain targeting. "Single-source — SentinelOne only" is pipeline self-reference in reader text. The GitLab case comes from SentinelOne\'s Annual Threat Report, not originally from this post.',
   'ground_truth': 'Victims were directed to fake skill-assessment sites where they encountered fabricated technical errors and were instructed to run commands to "fix" the issue. Those commands silently deployed malware on the developer\'s workstation.',
   'ground_truth_url': S1,
   'fix': 'Cite the SentinelOne post on each case sentence; add the run-this-command mechanism; replace the closing line with sourcing_note provenance (vendor blog, unnamed victims).',
   'class': 'imprecision'},
 ],
 'upgrade': {
  'techniques': [
   {'id': 'T1190', 'behavior': 'Exploit of a vulnerable self-hosted TeamCity server', 'url': S1},
   {'id': 'T1078', 'behavior': 'Compromised GitLab service-account token used to create projects with malicious Ansible playbooks', 'url': S1},
   {'id': 'T1072', 'behavior': 'Malicious Ansible playbooks executed automatically by the CI/CD pipeline; malicious build task deployed by a trusted build agent', 'url': S1},
   {'id': 'T1195.001', 'behavior': 'Malicious versions of popular build packages that ran reconnaissance scripts at install', 'url': S1},
   {'id': 'T1195.002', 'behavior': 'Malicious code appended to legitimate package updates via phished maintainer accounts', 'url': S1},
   {'id': 'T1566', 'behavior': 'Phishing used to compromise trusted maintainer accounts; fraudulent job offers (Contagious Interview)', 'url': S1},
   {'id': 'T1204.004', 'behavior': 'Developers instructed to run commands to "fix" a fabricated error on a fake skill-assessment site', 'url': S1},
   {'id': 'T1552', 'behavior': 'Install-time scripts harvested tokens and inspected environments; developer workstation SSH keys, tokens and credentials exposed', 'url': S1},
  ],
  'note': 'No clean enterprise technique for rogue self-hosted runner registration or discussion-comment workflow triggers; the entry\'s T1547 and T1555 are not supported. The post does not name an access vector for the GitLab token compromise.',
  'rating': {'reliability': 'B', 'credibility': 2, 'basis': 'SentinelOne vendor blog (large security vendor, partly marketing, unnamed victims) restating observations from its own annual threat report; no independent assessor in the entry\'s sources.'},
  'exposure': [
   {'quote': 'Build servers and runners are high-value targets because they routinely execute privileged actions.', 'url': S1},
   {'quote': 'self-hosted runners are often granted broad access to repositories, secrets, and deployment workflows.', 'url': S1},
  ],
  'detection': [
   {'quote': 'Build runners should be treated as high-value systems, monitored for suspicious child processes, credential access attempts, reverse tunnels, and persistence mechanisms. Unauthorized registrations or unusual runner names should trigger immediate investigation.', 'url': S1},
   {'quote': 'New or modified pipelines created by service accounts, jobs interacting with unfamiliar repositories, or workflows that establish network tunnels should all be treated as potential indicators of compromise.', 'url': S1},
  ],
  'triage': [
   {'quote': 'If a malicious job executes under a valid service account on a trusted runner, the behavior may appear legitimate unless the account performs actions that clearly deviate from its role.', 'url': S1},
  ],
  'takeaway': [
   {'quote': 'Security teams need to know when new runners are registered, when build configurations change unexpectedly, when secrets are introduced into workflows, and when jobs exhibit suspicious runtime behavior.', 'url': S1},
  ],
  'cve_facts': {'CVE-2023-42793': {'product': 'JetBrains TeamCity On-Premises', 'fixed': '2023.05.4', 'kev_date_added': '2023-10-04', 'authority': 'https://blog.jetbrains.com/teamcity/2023/10/cve-2023-42793-vulnerability-in-teamcity-october-18-2023-update/'}},
  'bodies': [P + 's1-pipeline.txt', P + 's1-teamcity-jb.txt'],
 },
 'possible_twin_outside_batch': None,
}
CLAIMS = '''
f3b09f3fb6 ¦ F14 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ No taxonomy and no "three" case studies in the post (TeamCity, GitLab intrusion, Contagious Interview and Sha1-Hulud campaigns, poisoned packages); headline also truncated
cd661b5ad1 ¦ F14 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ date 2026-05-15 confirmed; no "taxonomy", no "three real intrusion case studies", "immediately useful" not in source
33c04f262b ¦ F14 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ Cited post carries date 2026-05-15 and the TeamCity/GitLab/GitHub runner content, but not "taxonomy" or "three real intrusion case studies"
19d54494a6 ¦ F3 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ T1195.002 fits; T1547 (Boot or Logon Autostart Execution) does not describe runner registration ("persistent, authorized access"); post cites no ATT&CK ids
9680fe033f ¦ F3 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ "Once a malicious runner is registered, the attacker gains persistent, authorized access" - not boot/logon autostart (T1547)
d87b4a6905 ¦ F3 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ "These scripts harvested tokens, inspected environments" - T1555 Credentials from Password Stores does not fit; T1552 does
d78e138bd0 ¦ ok ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ T1204 user execution fits ("instructed to run commands to 'fix' the issue"); T1072 fits Ansible playbooks executed by the pipeline
4598a0c42e ¦ F5 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ "exploited a vulnerable self-hosted TeamCity server and remained undetected for more than a year ... deployed a backdoor"; CVE-2023-42793 only in a link target
40150698a4 ¦ F13 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ Post: "The build system treated the attacker's commands as authorized automation"; "over-privilege" and "production" not stated
72c3099746 ¦ F5 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ "Contagious Interview used fraudulent job offers ... fake skill-assessment sites ... instructed to run commands to 'fix' the issue. Those commands silently deployed malware"
1a633a4af8 ¦ F4 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ "reconnaissance scripts during installation" (no "preinstall"); runners and comment triggers are Sha1-Hulud behaviors in the post; "NPM" not stated
845c360380 ¦ F4 ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ Post names no runner.registered event, no source IP ranges, no cmd.exe/powershell.exe/curl/wget; says "suspicious child processes, credential access attempts, reverse tunnels"
670b479116 ¦ ok ¦ https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/ ¦ Only SentinelOne source cited (true); wording is pipeline self-reference, logged as imprecision
'''
