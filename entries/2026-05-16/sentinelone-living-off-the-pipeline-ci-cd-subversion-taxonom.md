---
schema: 1
kind: research
title: "SentinelOne \"Living Off the Pipeline\": attackers subverted TeamCity, GitLab automation, self-hosted runners and developer workstations in 2025"
headline: "SentinelOne: attackers turn build servers, CI/CD runners and developer workstations into the intrusion path"
summary: "SentinelOne's post of 2026-05-15 describes CI/CD subversion seen in 2025: attackers on a vulnerable self-hosted TeamCity server ran a backdoor-deploying build job and stayed undetected for over a year, a stolen GitLab service-account token planted Ansible playbooks the pipeline ran automatically, Contagious Interview lured developers into running malware, and Sha1-Hulud registered rogue self-hosted GitHub runners. It recommends alerting on runner registrations, pipeline changes by service accounts and suspicious process behavior on build runners."
discovered_at: "2026-05-16T05:00:08Z"
event_date: 2026-05-15
run_id: 2026-05-16-5bc123a0
priority: notable
immediate_action: null
tags:
  - supply-chain
  - identity
  - vulnerabilities
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:sentinelone-living-off-the-pipeline-2026"
techniques: [T1190, T1078, T1072, T1195.001, T1195.002, T1566, T1204.004, T1552]
affected_products: ["JetBrains TeamCity On-Premises"]
cves:
  - id: CVE-2023-42793
    cvss: null
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: "TeamCity On-Premises, all versions before 2023.05.4"
    fixed: "2023.05.4, or the security patch plugin for TeamCity 8.0 and later"
sources:
  - url: "https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/"
    publisher: "SentinelOne"
    date: "2026-05-15"
    role: primary
  - url: "https://blog.jetbrains.com/teamcity/2023/09/critical-security-issue-affecting-teamcity-on-premises-update-to-2023-05-4-now/"
    publisher: "JetBrains"
    date: "2023-09-21"
    role: corroborating
  - url: "https://blog.jetbrains.com/teamcity/2023/10/cve-2023-42793-vulnerability-in-teamcity-october-18-2023-update/"
    publisher: "JetBrains"
    date: "2023-10-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "After gaining access, they created a benign-looking build configuration that was executed by a trusted build agent running with SYSTEM privileges."
    publisher: SentinelOne
    source_url: "https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/"
  - quote: "The attacker used the token to create projects containing malicious Ansible playbooks, which were then automatically executed by the organization’s CI/CD pipeline."
    publisher: SentinelOne
    source_url: "https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/"
  - quote: "Build runners should be treated as high-value systems, monitored for suspicious child processes, credential access attempts, reverse tunnels, and persistence mechanisms."
    publisher: SentinelOne
    source_url: "https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/"
  - quote: "If a malicious job executes under a valid service account on a trusted runner, the behavior may appear legitimate unless the account performs actions that clearly deviate from its role."
    publisher: SentinelOne
    source_url: "https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/"
  - quote: "The vulnerability may enable an unauthenticated attacker with HTTP(S) access to a TeamCity server to perform a remote code execution (RCE) attack and gain administrative control of the TeamCity server."
    publisher: JetBrains
    source_url: "https://blog.jetbrains.com/teamcity/2023/09/critical-security-issue-affecting-teamcity-on-premises-update-to-2023-05-4-now/"
verification: single-source
sourcing_note: >
  A SentinelOne company blog post drawing on its annual threat report; the victims are unnamed and no other party reports the TeamCity and GitLab
  intrusions. The CVE-2023-42793 facts come from JetBrains' own advisories.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-16.md
updates:
  - at: "2026-10-21T16:09:54Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      SentinelOne's monitoring advice covers new runner registrations and unusual runner names, pipelines
      created or changed by service accounts, jobs touching unfamiliar repositories, tunnel-opening
      workflows and suspicious child processes, credential access, reverse tunnels and persistence on
      build runners; it names no audit-event type, source-address criterion or specific binaries. The post
      walks through examples rather than a taxonomy of three cases, and attributes rogue self-hosted
      runners and comment-triggered workflows to Sha1-Hulud. The TeamCity case concerns CVE-2023-42793,
      fixed in TeamCity On-Premises 2023.05.4, whose pre-patch backdoors JetBrains says persist after
      patching.
    fields: [affected_products, body, classification, confidence, cves, evidence, headline, sectors, sources, sourcing_note, summary, techniques, title]
---

SentinelOne's post of 2026-05-15 describes how attackers in 2025 went after the infrastructure that builds and ships software, not only its dependencies ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)). In one case attackers exploited a vulnerable self-hosted TeamCity server (the post links JetBrains' advisory for CVE-2023-42793), created a benign-looking build configuration that a trusted build agent ran with SYSTEM privileges, deployed a backdoor into internal environments and stayed undetected for more than a year ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)). JetBrains fixed that unauthenticated remote-code-execution flaw in TeamCity On-Premises 2023.05.4 ([JetBrains, 2023-09-21](https://blog.jetbrains.com/teamcity/2023/09/critical-security-issue-affecting-teamcity-on-premises-update-to-2023-05-4-now/)) and warned that backdoors planted before the patch persist after it ([JetBrains, 2023-10-18](https://blog.jetbrains.com/teamcity/2023/10/cve-2023-42793-vulnerability-in-teamcity-october-18-2023-update/)). In an intrusion from SentinelOne's annual threat report, a compromised GitLab service-account token was used to create projects with malicious Ansible playbooks that the organization's pipeline then executed automatically ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)).

The post's other examples target people and runners: Contagious Interview sent developers in cryptocurrency and blockchain fraudulent job offers leading to fake skill-assessment sites, where a fabricated error told them to run commands that silently installed malware with access to their SSH keys, tokens and credentials, and the Sha1-Hulud campaign registered infected systems as self-hosted GitHub runners under attacker-defined names and used workflows that ran code when someone commented in a repository discussion ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)). Malicious versions of popular build packages ran reconnaissance scripts during installation that harvested tokens and inspected environments, and phished maintainer accounts appended malicious code to legitimate package updates ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)).

**Exposure:** organizations running self-hosted build servers and runners, which SentinelOne notes are often granted broad access to repositories, secrets and deployment workflows ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)); TeamCity On-Premises servers before 2023.05.4 are exposed to CVE-2023-42793 ([JetBrains, 2023-09-21](https://blog.jetbrains.com/teamcity/2023/09/critical-security-issue-affecting-teamcity-on-premises-update-to-2023-05-4-now/)).

**Detection:** in CI/CD platform audit logs, new runner registrations and unusual runner names, new or modified pipelines created by service accounts, jobs touching unfamiliar repositories and workflows that open network tunnels; on the build runners themselves, process and credential-access telemetry for suspicious child processes, credential access attempts, reverse tunnels and persistence ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)).

**Triage:** compiling, downloading packages, invoking scripts and opening connections are normal build activity, so a malicious job under a valid service account on a trusted runner looks legitimate unless the account acts outside its role; SentinelOne's discriminators are who created the job, what changed, where the runner was registered and which secrets were accessed ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)).

**Defender takeaway:** treat build servers and runners as high-value systems and alert on runner registrations and pipeline changes made by service accounts ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)). A TeamCity server patched to 2023.05.4 after early October 2023 still needs a compromise assessment of the server and its build agents, because JetBrains says backdoors planted earlier are likely to persist after the patch ([JetBrains, 2023-10-18](https://blog.jetbrains.com/teamcity/2023/10/cve-2023-42793-vulnerability-in-teamcity-october-18-2023-update/)).

## Correction — 2026-10-21T16:09:54Z

The monitoring priorities SentinelOne gives are new runner registrations and unusual runner names, new or modified pipelines created by service accounts, jobs interacting with unfamiliar repositories, workflows that establish network tunnels, and suspicious child processes, credential access attempts, reverse tunnels and persistence on build runners ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)); the post names no audit-event type, source-address criterion or specific binaries. It walks through examples rather than a three-case taxonomy, and the rogue self-hosted runners and discussion-comment workflow triggers belong to the Sha1-Hulud campaign ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)). The TeamCity case links CVE-2023-42793, an unauthenticated remote-code-execution flaw fixed in TeamCity On-Premises 2023.05.4 ([JetBrains, 2023-09-21](https://blog.jetbrains.com/teamcity/2023/09/critical-security-issue-affecting-teamcity-on-premises-update-to-2023-05-4-now/)); JetBrains warns that backdoors planted before patching are likely to persist after it, so a server patched after early October 2023 needs a compromise assessment ([JetBrains, 2023-10-18](https://blog.jetbrains.com/teamcity/2023/10/cve-2023-42793-vulnerability-in-teamcity-october-18-2023-update/)).
