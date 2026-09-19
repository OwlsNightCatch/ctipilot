---
schema: 1
kind: research
title: "SentinelOne: \"Living Off the Pipeline\" — CI/CD subversion taxonomy with three real intrusion cases (TeamCity, GitLab service-account pivot, Contagious Interview)"
headline: "SentinelOne: \"Living Off the Pipeline\" — CI/CD subversion taxonomy with three real intrusion cases (TeamCity, GitLab service-account pivot, Contagious"
summary: "SentinelOne published on 2026-05-15 a practitioner-focused taxonomy of CI/CD pipeline subversion techniques, illustrated with three real intrusion case studies that are immediately useful for SOC and DevSecOps teams running JetBrains TeamCity, GitLab, or GitHub Actions (SentinelOne, 2026-05-15)."
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
  - public-sector
entities:
  - "campaign:sentinelone-living-off-the-pipeline-2026"
cves: []
sources:
  - url: "https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/"
    publisher: "SentinelOne, 2026-05-15"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-16.md
---

SentinelOne published on 2026-05-15 a practitioner-focused taxonomy of CI/CD pipeline subversion techniques, illustrated with three real intrusion case studies that are immediately useful for SOC and DevSecOps teams running JetBrains TeamCity, GitLab, or GitHub Actions ([SentinelOne, 2026-05-15](https://www.sentinelone.com/blog/living-off-the-pipeline-defending-against-ci-cd-subversion/)). Case 1: an unpatched TeamCity server (CVE-2023-42793) exploited to deploy backdoors via privileged build tasks, remaining undetected for 12+ months. Case 2: a GitLab service-account token compromise enabling creation of malicious Ansible playbooks that were then automatically executed by pipelines — a clean demonstration of how service-account over-privilege translates directly into production code execution. Case 3: the Contagious Interview campaign using fraudulent job offers directing developer victims to fake skill-assessment sites that deploy malware silently to developer workstations. Additional vectors covered include attacker-registered self-hosted runners, workflow triggers from repository discussion comments, dependency poisoning with reconnaissance `preinstall` scripts, and maintainer-account compromise appending malicious code; the article cross-links a separate SentinelOne analysis of the "Sha1-Hulud" NPM compromise as a related supply-chain case. MITRE ATT&CK: [T1195.002](https://attack.mitre.org/techniques/T1195/002/), [T1547](https://attack.mitre.org/techniques/T1547/) (rogue runner registration as persistence), [T1555](https://attack.mitre.org/techniques/T1555/) (pipeline secret extraction), [T1204](https://attack.mitre.org/techniques/T1204/) (user execution via fake job-offer social engineering), [T1072](https://attack.mitre.org/techniques/T1072/) (software-deployment-tool abuse via Ansible). Defender monitoring priorities surfaced in the report: GitHub / GitLab audit logs for `runner.registered` events with unfamiliar names or unexpected source IP ranges; new or modified pipelines authored by service accounts; suspicious child-process spawn from build agents (`cmd.exe`, `powershell.exe`, `curl`, `wget` outside baseline); credential-access and reverse-tunnel traffic originating from build infrastructure; and secret-injection patterns in workflow-config modifications. Single-source — SentinelOne only.
