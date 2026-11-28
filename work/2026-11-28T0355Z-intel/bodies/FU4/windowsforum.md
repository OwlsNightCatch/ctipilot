---
title: SAP Investigates Suspicious Activity as Reports Allege GitHub Token Theft and Source Code Tampering
author: WindowsForum
url: https://windowsforum.com/news/sap-investigates-suspicious-activity-as-reports-allege-github-token-theft-and-source-code-tampering.454314/
hostname: windowsforum.com
description: SAP confirmed suspicious activity and says it has found no evidence of customer business-data access; media reports allege GitHub token theft, but details remain unverified.
sitename: Windows Forum
date: "2026-11-27"
fingerprint: "8d03370b0e0a524e"
language: en
image: https://windowsforum.com/attachments/windowsforum-sap-investigates-suspicious-activity-as-reports-allege-github-token-theft-and-so-webp.193060/
pagetype: article
filedate: "2026-11-28"
---
*BleepingComputer*and other outlets that it detected suspicious activity in its IT environment and moved urgently to protect customers and secure its services, while stressing that investigators had found no evidence to date of unauthorized access to customer business data.

Behind that measured corporate phrasing, however, sits a far stormier set of German media reports. According to *Der Spiegel*, *Handelsblatt*, and the German Press Agency (*dpa*), SAP has been managing an active cybersecurity incident internally under the codename "Project Granite" after attackers allegedly stole employee authentication tokens to copy and alter source code on GitHub—possibly with help from autonomous AI tools. Whether you run SAP enterprise workloads on Windows Server infrastructure, maintain custom integrations on Windows developer workstations, or simply rely on GitHub for your own software supply chain, separating what is officially verified from what remains speculative is essential right now.

## 
  
    
    
  
    
    
  
    
  
What SAP Has Confirmed—and What It Hasn't

In corporate incident response, every word in a press statement is weighed on a jeweler's scale. SAP told *BleepingComputer*, *SecurityWeek*, and *Reuters* that it identified suspicious activity and promptly implemented protective measures, adding: "Based on our investigation to date, we have found no evidence of unauthorized access to customer business data". In a separate statement to *dpa* reported by *t-online*, SAP echoed that exact assurance while keeping the timing, entry vector, and affected environments under wraps.

Notice what that statement carefully *avoids* saying. Confirming no evidence of unauthorized access to *customer business data* is not the same as confirming that development environments, internal repositories, or source code remained untouched. When *BleepingComputer* pressed SAP on which environments experienced suspicious activity—and whether customers downloading code from SAP GitHub repositories or applying updates fed by those repositories need to take action—a spokesperson declined to provide further details.

German business and tech outlets have filled in some of the operational picture through internal memos and company insiders, though SAP has not publicly corroborated those specifics:

- **The "Project Granite" label:** *Der Spiegel* first reported on November 26, 2026, citing an internal staff memo, that SAP was tracking the active incident as "Project Granite" and instructed employees to keep all details strictly confidential inside the company.
- **Reported GitHub targeting and token theft:** *dpa* reviewed internal communications indicating the suspicious activity occurred in SAP's GitHub presence and noted that staff were asked to check whether they needed to update credentials. Insiders speaking to *Der Spiegel* alleged that intruders stole employee authentication tokens and used them to both copy and modify SAP source code on GitHub.
- **Reported containment steps:** *Handelsblatt*, citing corporate sources, reported that SAP's emergency response disrupted numerous development teams as the company restricted GitHub access, paused automated software development workflows, and rotated signing keys to prevent stolen credentials from maintaining access or allowing tampered code into shipped software. *Golem*, citing *Handelsblatt*, added that access to the affected GitHub projects has since been secured again.

| Incident Dimension | Officially Confirmed by SAP | Reported by Media / Insiders | Still Unresolved Publicly | 
|---|---|---|---|
| **Core Event** | Suspicious activity detected; protective measures deployed | Active incident codenamed "Project Granite" targeting GitHub | Exact discovery date and initial breach vector | 
| **Customer Data** | No evidence to date of unauthorized access to customer business data | No indication tampered code reached shipped customer software | Whether any downstream builds or packages consumed altered code | 
| **Credentials & Code** | Not publicly confirmed | Employee GitHub tokens allegedly stolen to copy and alter code | Which repositories (public or private) were involved | 
| **Containment Actions** | "Necessary measures" taken to protect customers and services | GitHub access restricted, CI/CD paused, signing keys rotated, staff told to check credentials | Whether customers downloading SAP GitHub code face any risk | 
| **Threat Actor & Tooling** | Not publicly identified | Possible use of AI agents / agentic AI | Attacker identity and actual role of AI | 

**Section Summary:** SAP has verified an active security response and stated there is no evidence of customer business data exposure so far, while German reporting points to a containment effort focused on GitHub tokens, automated build pipelines, and code-signing keys. The critical unanswered question for enterprise IT is not customer database access—it is whether any altered repository code ever touched a customer-facing release.

## Why Stolen GitHub Tokens Trigger Supply-Chain Alarm Bells

To understand why an incident inside a vendor's GitHub organization makes CISOs sit up straight—even when customer databases appear untouched—think of source code repositories as the kitchen, while production cloud services are the dining room. A burglar who never steps into the dining room can still cause massive trouble if they have keys to the pantry or the recipe book.

On GitHub, an authentication token acts as a digital key that bypasses interactive passwords and second-factor prompts, granting automated tools or scripts whatever permissions are bound to that token. As cybersecurity analysts at *GBHackers* and *CyberInsider* noted in assessing the reports, the real-world blast radius of a stolen token depends entirely on its scope:

- **Read-only exposure:** Copying private source code can leak proprietary algorithms or reveal hardcoded secrets and internal architecture that make future vulnerability hunting easier.
- **Write-level tampering:** If a compromised token carries write or administrative permissions—especially on repositories tied to open-source tools, SDKs, sample apps, or automated build workflows—an intruder can attempt to inject unauthorized commits directly into the software supply chain.

That distinction explains why the operational countermeasures attributed to SAP by *Handelsblatt*—locking down GitHub access, halting automated development pipelines, and rotating signing keys—make complete engineering sense as defensive triage. If an organization suspects repository writes occurred outside normal human review, halting CI/CD runners prevents unvetted commits from automatically compiling, signing, and publishing into package registries or update channels. Rotating code-signing keys ensures that even if an attacker captured cryptographic trust material, future binaries cannot be stamped with SAP's trusted signature.

It is also worth remembering that this is SAP's second software-supply-chain scare in 2026. Back on April 29, 2026, attackers compromised four official SAP npm packages targeting SAP Cloud Application Programming (CAP) developers—an attack tracked alongside the "Mini Shai-Hulud" campaign and mitigated in SAP Note 3747787. In that April incident, malicious package updates harvested developer credentials and cloud secrets and exfiltrated them via public GitHub repositories. For enterprise defenders, the lesson is unmistakable: modern attackers treat developer identities and package ecosystems as high-leverage stepping stones into enterprise networks.

**Section Summary:** Developer tokens carry vastly different risks depending on whether they allow reading proprietary code or modifying build-connected repositories. Reportedly pausing automated pipelines and rotating signing keys reflects standard supply-chain containment designed to sever unauthorized access before tainted code can ship.

## The Agentic AI Angle: From Hype to Machine-Speed Intrusion

Could autonomous AI agents have played a role in the SAP incident? *Der Spiegel* and *dpa* cited insiders raising that possibility, though SAP has not confirmed AI involvement and no public technical evidence yet proves what tools the intruders used. Still, the timing of that speculation is impossible to ignore, because national cyber agencies across Europe and North America spent this very week sounding the alarm over a new wave of automated hacking kits.

On November 26, 2026—the same day *Der Spiegel*'s report broke—Germany's Federal Office for Information Security (BSI) issued an urgent warning through its AI Safety and Security Institute (AISI Deutschland) about **Agentic Offensive Frameworks** such as **ARTEX**, **CAIRN**, and **PentAGI**. According to the BSI, these toolkits orchestrate AI agents to link together standard penetration-testing utilities, automatically probing targets, adapting tactics when error messages appear, and executing multi-stage attacks from reconnaissance to privilege escalation and data theft at machine speed. Crucially, the BSI emphasized that attackers do not even need expensive frontier AI models; freely downloadable open-weight models work well enough to enable what BSI President Claudia Plattner warned could become "cyberattacks at bargain prices".

That warning did not emerge in a vacuum. Within days of the BSI alert, several major authorities documented real-world abuse:

- **Microsoft Threat Intelligence** warned on November 25, 2026, that both state-sponsored and financially motivated groups—including Storm-0940, Storm-3358, Onyx Sleet, Pearl Sleet, Crystal Typhoon, and Salt Typhoon—have integrated ARTEX into active operations since its July 2026 release, specifically using it to **search public repositories for exposed secrets**, facilitate supply-chain compromises, and scan internet-facing assets.
- **The FBI** issued a FLASH advisory on November 13, 2026, revealing that ARTEX-assisted intrusions had progressed from initial targeting to privileged access in under three hours, including a ConnectWise Cloud Backup supply-chain compromise affecting more than 2,250 downstream tenants.
- **Italy's National Cybersecurity Agency (ACN / CSIRT Italia)** and **Switzerland's National Cyber Security Centre (NCSC / BACS)** both confirmed active campaigns in late November 2026 where autonomous AI agents—including ARTEX, CyberStrikeAI, DeepSeek Harness, and PentAGI—successfully breached organizations and critical infrastructure operators.
- **The UK NCSC** cautioned on November 24, 2026, that agentic frameworks do not magically invent zero-day exploits; instead, they relentlessly hunt low-hanging fruit—leaked credentials, exposed APIs, and infrastructure-as-code misconfigurations—faster and longer than human operators ever could.

Even if SAP's investigators ultimately determine that old-fashioned phishing or infostealer malware—not an autonomous AI agent—captured those employee tokens, the broader trend is crystal clear. When automated bots can sweep GitHub repositories for stray credentials and test stolen tokens across endpoints in minutes, human-speed credential hygiene is no longer enough.

**Section Summary:** While AI involvement in SAP's incident remains unconfirmed, warnings from the BSI, Microsoft, the FBI, the UK NCSC, Italy, and Switzerland show that agentic frameworks like ARTEX are actively weaponizing exposed credentials and repository secrets at machine speed.

## What Windows Admins and DevOps Teams Should Do Right Now

First, let's keep our feet firmly on the ground regarding SAP environments. **SAP has not issued a customer advisory telling organizations to halt updates, rebuild systems, or rotate customer credentials.** Do not treat media reports as an official SAP remediation mandate. Instead, IT leaders running SAP on Windows Server, Azure, or hybrid landscapes should monitor SAP's official security communications and Trust Center notices, and check directly with their SAP account team if their internal CI/CD pipelines pull code straight from SAP-hosted GitHub repositories or consume automated upstream feeds.

At the same time, every Windows system administrator and DevOps lead can use this wake-up call to harden their own GitHub and developer-endpoint defenses before their organization becomes tomorrow's headline:

1. **Retire classic GitHub Personal Access Tokens (PATs):** Classic PATs often inherit sweeping access across every repository a developer can touch and lack per-organization approval controls. Migrate to **fine-grained PATs**, which GitHub Docs note restrict access to a single user or organization, enforce granular read/write/admin scopes per permission, support mandatory expiration limits, and require organization-owner approval for private resources.
2. **Replace long-lived CI/CD secrets with GitHub OIDC:** If your GitHub Actions workflows deploy to Azure, AWS, or Windows build infrastructure using static cloud keys stored as repository secrets, switch to **OpenID Connect (OIDC) federation**. OIDC mints short-lived runtime tokens tied strictly to an expected repository, branch, and workflow context, meaning a stolen artifact cannot be reused indefinitely.
3. **Lock down Windows developer endpoints:** Developer laptops are prime targets for malicious VS Code extensions, rogue npm/NuGet packages, and credential-harvesting scripts. Enforce Windows Defender Application Control or AppLocker policies where practical, audit installed IDE extensions, and ensure developers do not store plaintext tokens in `.git-credentials`, environment variables, or unencrypted scripts.
4. **Monitor GitHub audit logs for token persistence:** Watch organization audit logs for suspicious token authorizations and policy changes—such as `org_credential_authorization.grant` or changes to `personal_access_token` auto-approval rules—that attackers use to turn temporary account access into durable API persistence.
5. **Tune defenses for machine-speed behavioral anomalies:** As Microsoft Threat Intelligence and the BSI point out, agentic tools rotate source IPs and user agents to dodge static blocklists, but give themselves away through rapid bursts of varied requests and high-velocity sequential retries. Follow UK NCSC guidance by enforcing bot challenges on exposed portals, stripping verbose stack traces from external error messages, and tightening perimeter access to internal dev tools.

**Section Summary:** Enterprise SAP customers should await official SAP guidance before altering update workflows, while using this incident to eliminate classic GitHub PATs, adopt OIDC short-lived credentials, secure Windows developer machines, and monitor for automated token abuse.

## The Bottom Line for Enterprise Defenders

For now, "Project Granite" sits in that familiar gray zone of modern enterprise cybersecurity: the vendor has confirmed suspicious activity and found no sign of customer business-data theft, while insider accounts sketch a narrower—yet still consequential—battle inside the software development pipeline. Whether SAP's investigation ultimately clears every public and private repository or triggers targeted advisories down the road, one reality already stands out in bold relief. Source code hosting platforms, CI/CD runners, and developer tokens are no longer back-office plumbing—they are front-line enterprise infrastructure, and attackers armed with automation are knocking on those doors around the clock.

## References

1. [SAP confirms security incident after suspicious GitHub activity](https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity) BleepingComputer
											 · 
											2026-11-27T04:56:36-05:00
2. [securityweek.com](https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised) securityweek.com
3. [github.com](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) docs.github.com
