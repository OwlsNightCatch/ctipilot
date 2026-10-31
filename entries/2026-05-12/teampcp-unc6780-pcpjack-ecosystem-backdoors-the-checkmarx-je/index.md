---
schema: 1
kind: threat
title: "Checkmarx Jenkins AST plugin backdoored: rogue build 2026.5.09 swept build hosts for credentials on 2026-05-09/10, the third wave of malicious Checkmarx artifacts since March (TeamPCP claimed)"
headline: "A rogue Checkmarx Jenkins AST plugin build that hunts credentials was live for about 31 hours; TeamPCP claimed it"
summary: "A modified build 2026.5.09 of the Checkmarx Jenkins AST plugin, published to the Jenkins Marketplace outside the plugin's release pipeline, was live from 2026-05-09 01:25 to 2026-05-10 08:47 UTC; its payload walks an OS-specific list of file paths looking for credentials of crypto wallets, VPNs, AWS and GitHub (Checkmarx). Checkmarx says the attacker reused access obtained in the March 2026 Trivy compromise, and TeamPCP claimed the attack, the third wave of malicious Checkmarx artifacts since late March. Checkmarx recommends rotating every credential a pipeline that ran the build could reach."
discovered_at: "2026-05-12T05:00:06Z"
event_date: 2026-05-09
run_id: 2026-05-12-cd1ab844
priority: high
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - organized-crime
  - cloud
regions:
  - global
sectors:
  - technology
entities:
  - "incident:checkmarx-jenkins-ast-plugin-2026"
  - "actor:teampcp"
techniques: [T1195.002, T1078, T1552.001]
affected_products: ["Checkmarx Jenkins AST Plugin"]
cves: []
sources:
  - url: "https://thehackernews.com/2026/05/teampcp-compromises-checkmarx-jenkins.html"
    publisher: "The Hacker News"
    date: "2026-05-11"
    role: primary
  - url: "https://checkmarx.com/blog/ongoing-security-updates/"
    publisher: "Checkmarx"
    date: "2026-07-06"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/"
    publisher: "BleepingComputer"
    date: "2026-05-11"
    role: corroborating
  - url: "https://socradar.io/blog/checkmarx-jenkins-plugin-teampcp-backdoor/"
    publisher: "SOCRadar"
    date: "2026-05-11"
    role: corroborating
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access"
    publisher: "Google Threat Intelligence Group"
    date: "2026-05-11"
    role: corroborating
  - url: "https://github.com/advisories/GHSA-69fq-xp46-6x23"
    publisher: "GitHub Advisory Database (Aqua Security Trivy)"
    date: "2026-03-21"
    role: corroborating
  - url: "https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/"
    publisher: "SentinelLABS"
    date: "2026-05-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The malicious window was 2026-05-09 01:25 UTC to 2026-05-10 08:47 UTC."
    publisher: Checkmarx
    source_url: "https://checkmarx.com/blog/ongoing-security-updates/"
  - quote: "Our assessment based on currently available evidence is that the threat actor was able to leverage access, obtained as part of the March incident, to later publish the modified version of the Jenkins plugin on May 9."
    publisher: Checkmarx
    source_url: "https://checkmarx.com/blog/ongoing-security-updates/"
  - quote: "Targeted applications include crypto wallets, VPNs, AWS, and Github."
    publisher: Checkmarx
    source_url: "https://checkmarx.com/blog/ongoing-security-updates/"
  - quote: "The compromise was claimed by the TeamPCP hacker group"
    publisher: BleepingComputer
    source_url: "https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/"
  - quote: "The update was outside the plugin's release pipeline and included malicious code."
    publisher: BleepingComputer
    source_url: "https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/"
verification: multi-source
sourcing_note: >
  Checkmarx is the primary for the malicious build, its window, the payload's targets and the reuse of access from the
  March incident; the TeamPCP attribution rests on the group's own claim and repository defacement as reported by
  BleepingComputer, The Hacker News and SOCRadar, and the UNC6780 designation and the SANDCLOCK name come from GTIG's
  report on the March compromises.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-12.md
updated_at: null
updates:
  - at: "2026-10-21T15:57:54Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      CVE-2026-33634 is the March 2026 Trivy malicious-release flaw, not a CVE for the Checkmarx Jenkins
      plugin, and no source names SANDCLOCK as the Jenkins payload, which Checkmarx says sweeps file paths
      for credentials of crypto wallets, VPNs, AWS and GitHub. The March wave was GitHub Actions and Open
      VSX extensions and the KICS Docker image came in April; the PCPJack worm, LLM API key targeting and
      Checkmarx One API tokens are not part of this incident. Exposure covers any instance that installed
      build 2026.5.09 between 2026-05-09 01:25 and 2026-05-10 08:47 UTC, and TeamPCP's role rests on its
      own claim.
    fields: [affected_products, body, classification, cves, entities, event_date, evidence, headline, kind, regions, sources, sourcing_note, summary, tags, techniques, title]
---

On Saturday 2026-05-09 a rogue build, version `2026.5.09`, of the Checkmarx Jenkins AST plugin was uploaded to repo.jenkins-ci.org outside the plugin's release pipeline; it broke the plugin's version scheme and had no git tag or GitHub release ([BleepingComputer, 2026-05-11](https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/)). Checkmarx says an external service account modified the plugin and published it to the Jenkins Marketplace, that the malicious window ran from 2026-05-09 01:25 UTC to 2026-05-10 08:47 UTC, and that the attacker used access obtained in the March incident, which began with credentials taken in the Trivy supply-chain attack on 2026-03-19 ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)). It is the third wave of malicious Checkmarx artifacts after GitHub Actions and Open VSX extensions on 2026-03-23 and a KICS Docker image, VS Code and DevAssist extensions and a GitHub Action on 2026-04-22 ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)). The payload determines the operating system (Windows, Linux or macOS), then walks a list of file paths for common applications on that system looking for credentials, with crypto wallets, VPNs, AWS and GitHub among the targets; Checkmarx had found no references to Jenkins in it, and Mandiant found no threat-actor access to the Checkmarx One SaaS environment ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)).

TeamPCP claimed the compromise ([BleepingComputer, 2026-05-11](https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/)), and researcher Adnan Khan and SOCRadar report that the group gained access to the plugin's GitHub repository and renamed it "Checkmarx-Fully-Hacked-by-TeamPCP-and-Their-Customers-Should-Cancel-Now", with the description "Checkmarx fails to rotate secrets again. with love – TeamPCP" ([The Hacker News, 2026-05-11](https://thehackernews.com/2026/05/teampcp-compromises-checkmarx-jenkins.html)). Google Threat Intelligence Group tracks TeamPCP as UNC6780 and says that in the late-March compromises (Trivy, Checkmarx, LiteLLM, BerriAI) the group embedded the SANDCLOCK credential stealer to extract cloud secrets such as AWS keys and GitHub tokens from build environments ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)).

**Exposure:** any Jenkins instance that installed or updated the Checkmarx AST plugin to build `2026.5.09` during the malicious window ([SOCRadar, 2026-05-11](https://socradar.io/blog/checkmarx-jenkins-plugin-teampcp-backdoor/)); Checkmarx names `2.0.13-829.vc72453fa_1c16` of 2025-12-17 or earlier and the clean replacements `2.0.13-848.v76e89de8a_053` and `2.0.13-847.v08c0072b_2fd5` as safe ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)).

**Detection:** in Jenkins plugin inventories and update history, the checkmarx-ast-scanner plugin at version `2026.5.09`; on hosts that ran it, file-access telemetry showing the build process reading the credential files of wallets, VPN clients, AWS and GitHub, which is what the payload's path sweep produces ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)). Checkmarx also advises restricting CI runner egress to an allowlist and monitoring outbound connections for unexpected domains ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)).

**Defender takeaway:** where a pipeline ran build `2026.5.09`, rotate all credentials that pipeline had access to, as Checkmarx recommends ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)), and investigate for lateral movement or persistence ([BleepingComputer, 2026-05-11](https://www.bleepingcomputer.com/news/security/official-checkmarx-jenkins-package-compromised-with-infostealer/)). Checkmarx's standing advice holds beyond this build: pin to specific SHAs rather than mutable tags and treat CI runner credentials as short-lived and tightly scoped ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)).

## Correction — 2026-10-21T15:57:54Z

No CVE covers the rogue plugin build: CVE-2026-33634 is the Trivy flaw in which a threat actor used compromised credentials on 2026-03-19 to publish a malicious Trivy release and move the trivy-action tags to credential-stealing code ([GitHub Advisory Database, 2026-03-21](https://github.com/advisories/GHSA-69fq-xp46-6x23)), the attack Checkmarx names as the source of the attacker's access ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)). No source names SANDCLOCK as the Jenkins payload; GTIG uses the name for the stealer of the late-March compromises and describes it extracting cloud secrets such as AWS keys and GitHub tokens, not LLM API keys ([GTIG, 2026-05-11](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access)). Checkmarx lists crypto wallets, VPNs, AWS and GitHub among the applications the payload targets, and Mandiant found no threat-actor access to the Checkmarx One SaaS environment ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)).

The earlier waves were GitHub Actions and Open VSX extensions in March and the KICS Docker image with updated extensions and a GitHub Action in April ([Checkmarx, updated 2026-07-06](https://checkmarx.com/blog/ongoing-security-updates/)). PCPJack is a separate cloud worm whose first act is to evict TeamPCP tooling ([SentinelLABS, 2026-05-07](https://www.sentinelone.com/labs/cloud-worm-evicts-teampcp-and-steals-credentials-at-scale/)), and no cited source links it to the plugin. The defacement renamed the plugin's GitHub repository, not the build ([The Hacker News, 2026-05-11](https://thehackernews.com/2026/05/teampcp-compromises-checkmarx-jenkins.html)), and exposure did not depend on auto-update: any instance that pulled build 2026.5.09 during the window installed the compromised plugin ([SOCRadar, 2026-05-11](https://socradar.io/blog/checkmarx-jenkins-plugin-teampcp-backdoor/)).
