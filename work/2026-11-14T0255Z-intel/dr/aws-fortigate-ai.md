---
title: AI-augmented threat actor accesses FortiGate devices at scale | Amazon Web Services
url: https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/
hostname: amazon.com
description: "Commercial AI services are enabling even unsophisticated threat actors to conduct cyberattacks at scale—a trend Amazon Threat Intelligence has been tracking closely. A recent investigation illustrates this shift: Amazon Threat Intelligence observed a Russian-speaking financially motivated threat actor leveraging multiple commercial generative AI services to compromise over 600 FortiGate devices across more than 55 countries […]"
sitename: Amazon Web Services
date: "2026-02-20"
categories: ['Customer Solutions']
tags: ['Customer Solutions', 'Security, Identity, & Compliance', 'Thought Leadership', 'Security Blog', 'Threat Intelligence']
fingerprint: "8539c4534a5e95c0"
---
## [AWS Security Blog](https://aws.amazon.com/blogs/security/)

# AI-augmented threat actor accesses FortiGate devices at scale

Commercial AI services are enabling even unsophisticated threat actors to conduct cyberattacks at scale—a trend Amazon Threat Intelligence has been tracking closely. A recent investigation illustrates this shift: Amazon Threat Intelligence observed a Russian-speaking financially motivated threat actor leveraging multiple commercial generative AI services to compromise over 600 FortiGate devices across more than 55 countries from January 11 to February 18, 2026. No exploitation of FortiGate vulnerabilities was observed—instead, this campaign succeeded by exploiting exposed management ports and weak credentials with single-factor authentication, fundamental security gaps that AI helped an unsophisticated actor exploit at scale. This activity is distinguished by the threat actor’s use of multiple commercial GenAI services to implement and scale well-known attack techniques throughout every phase of their operations, despite their limited technical capabilities. AWS infrastructure was not observed to be involved in this campaign. Amazon Threat Intelligence is sharing these findings to help the broader security community defend against this activity.

This investigation highlights how commercial AI services can lower the technical barrier to entry for offensive cyber capabilities. The threat actor in this campaign is not known to be associated with any advanced persistent threat group with state-sponsored resources. They are likely a financially motivated individual or small group who, through AI augmentation, achieved an operational scale that would have previously required a significantly larger and more skilled team. Yet, based on our analysis of public sources, they successfully compromised multiple organizations’ Active Directory environments, extracted complete credential databases, and targeted backup infrastructure, a potential precursor to ransomware deployment. Notably, when this actor encountered hardened environments or more sophisticated defensive measures, they simply moved on to softer targets rather than persisting, underscoring that their advantage lies in AI-augmented efficiency and scale, not in deeper technical skill.

As we expect this trend to continue in 2026, organizations should anticipate that AI-augmented threat activity will continue to grow in volume from both skilled and unskilled adversaries. Strong defensive fundamentals remain the most effective countermeasure: patch management for perimeter devices, credential hygiene, network segmentation, and robust detection for post-exploitation indicators.

## **Campaign overview**

Through routine threat intelligence operations, Amazon Threat Intelligence identified infrastructure hosting malicious tooling associated with this campaign. The threat actor had staged additional operational files on the same publicly accessible infrastructure, including AI-generated attack plans, victim configurations, and source code for custom tooling. This inadequate operational security provided comprehensive visibility into the threat actor’s methodologies and the specific ways they leverage AI throughout their operations. It’s like an AI-powered assembly line for cybercrime, helping less skilled workers produce at scale.

The threat actor compromised globally dispersed FortiGate appliances, extracting full device configurations that yielded credentials, network topology information, and device configuration information. They then used these stolen credentials to connect to victim internal networks and conduct post-exploitation activities including Active Directory compromise, credential harvesting, and attempts to access backup infrastructure, consistent with pre-ransomware operations.

## **Initial access: Mass credential abuse**

The threat actor’s initial access vector was credential-based access to FortiGate management interfaces exposed to the internet. Analysis of the actor’s tooling supported systematic scanning for management interfaces across ports 443, 8443, 10443, and 4443, followed by authentication attempts using commonly reused credentials.

FortiGate configuration files represent high-value targets because they contain:

- SSL-VPN user credentials with recoverable passwords
- Administrative credentials
- Complete network topology and routing information
- Firewall policies revealing internal architecture
- IPsec VPN peer configurations

The threat actor developed AI-assisted Python scripts to parse, decrypt, and organize these stolen configurations.

## **Geographic distribution**

The campaign’s targeting appears opportunistic rather than sector-specific, consistent with automated mass scanning for vulnerable appliances. However, certain patterns suggest organizational-level compromise where multiple FortiGate devices belonging to the same entity were accessed. Amazon Threat Intelligence observed clusters where contiguous IP blocks or shared non-standard management ports indicated managed service provider deployments or large organizational networks. Concentrations of compromised devices were observed across South Asia, Latin America, the Caribbean, West Africa, Northern Europe, and Southeast Asia, among other regions.

## **Custom tooling: AI-generated reconnaissance framework**

Following VPN access to victim networks, the threat actor deploys a custom reconnaissance tool, with different versions written in both Go and Python. Analysis of the source code reveals clear indicators of AI-assisted development: redundant comments that merely restate function names, simplistic architecture with disproportionate investment in formatting over functionality, naive JSON parsing via string matching rather than proper deserialization, and compatibility shims for language built-ins with empty documentation stubs. While functional for the threat actor’s specific use case, the tooling lacks robustness and fails under edge cases—characteristics typical of AI-generated code used without significant refinement.

The tool automates the post-VPN reconnaissance workflow:

1. Ingesting target networks from VPN routing tables
2. Classifying networks by size
3. Running service discovery using gogo, an open-source port scanner
4. Automatically identifying SMB hosts and domain controllers
5. Integrating vulnerability scanning using Nuclei, an open-source vulnerability scanner, against discovered HTTP services to produce prioritized target lists.

## **Post-exploitation methodology**

Once inside victim networks, the threat actor follows a standard approach leveraging well-known open-source offensive tools.

Domain compromise: The threat actor’s operational documentation details the intended use of Meterpreter, an open-source post-exploitation toolkit, with the mimikatz module to perform DCSync attacks against domain controllers. This allowed the actor to extract NTLM password hashes from Active Directory. In confirmed compromises, the attacker obtained complete domain credential databases. In at least one case, the Domain Administrator account used a plaintext password that was either extracted from the FortiGate configuration through password reuse or was independently weak.

**Lateral movement:** Following domain compromise, the threat actor attempts to expand access through pass-the-hash/pass-the-ticket attacks against additional infrastructure, NTLM relay attacks using standard poisoning tools, and remote command execution on Windows hosts.

**Backup infrastructure targeting:** The threat actor specifically targeted Veeam Backup & Replication servers, deploying multiple tools for extracting credentials, including PowerShell scripts, compiled decryption tools, and exploitation attempts leveraging known Veeam vulnerabilities. Backup servers represent high-value targets because they typically store elevated credentials for backup operations, and compromising backup infrastructure positions an attacker to destroy recovery capabilities before deploying ransomware.

**Limited exploitation success:** The threat actor’s operational notes reference multiple CVEs across various targets (CVE-2019-7192, CVE-2023-27532, and CVE-2024-40711, among others). However, a critical finding from this analysis is that the threat actor largely failed when attempting to exploit anything beyond the most straightforward, automated attack paths. Their own documentation records repeated failures: targeted services were patched, required ports were closed, vulnerabilities didn’t apply to the target OS versions, . Their final operational assessment for one confirmed victim acknowledged that key infrastructure targets were “well-protected” with “no vulnerable exploitation vectors.”

## **AI as a force multiplier**

Amazon Threat Intelligence analysis revealed that the actor uses at least two distinct commercial LLM providers throughout their operations.

**AI-generated attack planning:** The threat actor used AI to generate comprehensive attack methodologies complete with step-by-step exploitation instructions, expected success rates, time estimates, and prioritized task trees. These plans reference academic research on offensive AI agents, suggesting the actor follows emerging literature on AI-assisted penetration testing. The AI produces technically accurate command sequences, but the actor struggles to adapt when conditions differ from the plan. They cannot compile custom exploits, debug failed exploitation attempts, or creatively pivot when standard approaches fail.

**Multi-model operational workflow:** Amazon Threat Intelligence identified the actor using multiple AI services in complementary roles. One serves as the primary tool developer, attack planner, and operational assistant. A second is used as a supplementary attack planner when the actor needs help pivoting within a specific compromised network. In one observed instance, the actor submitted the complete internal topology of an active victim—IP addresses, hostnames, confirmed credentials, and identified services—and requested a step-by-step plan to compromise additional systems they could not access with their existing tools.

**AI-generated tooling at scale:** Beyond the reconnaissance framework, the actor’s infrastructure contains numerous scripts in multiple programming languages bearing hallmarks of AI generation, including configuration parsers, credential extraction tools, VPN connection automation, mass scanning orchestration, and result aggregation dashboards. The volume and variety of custom tooling would typically indicate a well-resourced development team. Instead, a single actor or very small group generated this entire toolkit through AI-assisted development.

## **Threat actor assessment**

Based on comprehensive analysis, Amazon Threat Intelligence assesses this threat actor as follows:

- **Motivation:** Suspected financially motivated, based on widespread, indiscriminate targeting and low sophistication
- **Language:** Russian-speaking, based on extensive Russian-language operational documentation
- **Skill level:** Low-to-medium baseline technical capability, significantly augmented by AI. The actor can run standard offensive tools and automate routine tasks but struggles with exploit compilation, custom development, and creative problem-solving during live operations
- **AI dependency:** Extensive reliance across all operational phases. AI is used for tool development, attack planning, command generation, and operational reporting across multiple commercial LLM providers
- **Operational scale:** Broad. Compromised devices across dozens of countries, with evidence of sustained operations over an extended period
- **Post-exploitation depth:** Shallow. Repeated failures against hardened or non-standard targets, with a pattern of moving on rather than persisting when automated approaches fail
- **Operational security:** Inadequate. Detailed operational plans, credentials, and victim data stored without encryption alongside tooling

## **Amazon’s response**

Amazon Threat Intelligence remains committed to helping protect customers and the broader internet ecosystem by actively investigating and disrupting threat actors.

Upon discovering this campaign, Amazon Threat Intelligence took the following actions:

- Shared actionable intelligence, including indicators of compromise, with relevant partners
- Collaborated with industry partners to broaden visibility into the campaign and support coordinated defense efforts

Through these efforts, Amazon helped reduce the threat actor’s operational effectiveness and enabled organizations across multiple countries to take steps to disrupt the efficacy of the campaign.

## **Defending your organization**

This campaign succeeded through a combination of exposed management interfaces, weak credentials, and single-factor authentication—all fundamental security gaps that AI helped an unsophisticated actor exploit at scale. This underscores that strong security fundamentals are powerful defenses against AI-augmented threats. Organizations should review and implement the following.

### **1. FortiGate appliance audit**

Organizations running FortiGate appliances should take immediate action:

- Ensure management interfaces are not exposed to the internet. If remote administration is required, restrict access to known IP ranges and use a bastion host or out-of-band management network
- Change all default and common credentials on FortiGate appliances, including administrative and VPN user accounts
- Rotate all SSL-VPN user credentials, particularly for any appliance whose management interface was or may have been internet-accessible
- Implement multi-factor authentication for all administrative and VPN access
- Review FortiGate configurations for unauthorized administrative accounts or policy changes
- Audit VPN connection logs for connections from unexpected geographic locations

### **2. Credential hygiene**

Given the extraction of credentials from FortiGate configurations:

- Audit for password reuse between FortiGate VPN credentials and Active Directory domain accounts
- Implement multi-factor authentication for all VPN access
- Enforce unique, complex passwords for all accounts, particularly Domain Administrator accounts
- Review and rotate service account credentials, especially those used in backup infrastructure

### **3. Post-exploitation detection**

Organizations that may have been affected should monitor for:

- Unexpected DCSync operations (Event ID 4662 with replication-related GUIDs)
- New scheduled tasks named to mimic legitimate Windows services
- Unusual remote management connections from VPN address pools
- LLMNR/NBT-NS poisoning artifacts in network traffic
- Unauthorized access to backup credential stores
- New accounts with names designed to blend with legitimate service accounts

### **4. Backup infrastructure hardening**

The threat actor’s focus on backup infrastructure highlights the importance of:

- Isolating backup servers from general network access
- Patching backup software against known credential extraction vulnerabilities
- Monitoring for unauthorized PowerShell module loading on backup servers
- Implementing immutable backup copies that cannot be modified even with administrative access

## **AWS-specific recommendations**

For organizations using AWS:

- Enable Amazon GuardDuty for threat detection, including monitoring for unusual API calls and credential usage patterns
- Use Amazon Inspector to automatically scan for software vulnerabilities and unintended network exposure
- Use AWS Security Hub to maintain continuous visibility into your security posture
- Use AWS Systems Manager Patch Manager to maintain patching compliance across EC2 instances running network appliances
- Review IAM access patterns for signs of credential replay following any suspected network device compromise

### **Indicators of compromise (IOCs)**

This campaign’s reliance on legitimate open-source tools—including Impacket, gogo, Nuclei, and others—means that traditional IOC-based detection has limited effectiveness. These tools are widely used by penetration testers and security professionals, and their presence alone is not indicative of compromise. Organizations should investigate context around matches, prioritizing behavioral detection (anomalous VPN authentication patterns, unexpected Active Directory replication, lateral movement from VPN address pools) over signature-based approaches.

| **IOC Value** | **IOC Type** | **First Seen** | **Last Seen** | **Annotation** | 
| 212\[.\]11.64.250 | IPv4 | 1/11/2026 | 2/18/2026 | Threat actor infrastructure used for scanning and exploitation operations | 
| 185\[.\]196.11.225 | IPv4 | 1/11/2026 | 2/18/2026 | Threat actor infrastructure used for threat operations | 

If you have feedback about this post, submit comments in the **Comments** section below. If you have questions about this post, [contact AWS Support](https://console.aws.amazon.com/support/home).
