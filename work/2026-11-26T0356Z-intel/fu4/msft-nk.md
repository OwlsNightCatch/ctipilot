---
title: Tracking AI adoption in North Korean threat actor tradecraft
author: Microsoft Threat Intelligence
url: https://www.microsoft.com/en-us/security/blog/2026/10/29/tracking-ai-adoption-in-north-korean-threat-actor-tradecraft/
hostname: microsoft.com
description: As Microsoft Threat Intelligence continues to track how threat actors operationalize AI to increase the speed and efficiency of attacks, we’ve identified North Korean threat actors expanding their use of AI with varying levels of adoption. This blog breaks down how North Korean threat actors are utilizing AI across their operations, reflecting a broader trend of threat actors incorporating AI into their attack chains.
sitename: Microsoft Security Blog
date: "2026-10-29"
tags: ['Sapphire Sleet', 'Sleet', 'Social engineering']
fingerprint: "2551269d22ce96c3"
language: en
image: https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2026/10/North-Korean-use-of-AI-featured-1.png
pagetype: article
filedate: "2026-11-26"
---
As Microsoft Threat Intelligence continues to track how threat actors [operationalize AI](https://www.microsoft.com/en-us/security/blog/2026/03/06/ai-as-tradecraft-how-threat-actors-operationalize-ai/) to increase the speed, efficiency, and complexity of attacks, we’ve identified North Korean threat actors expanding their use of AI with varying levels of adoption. Threat actors use AI as a force multiplier across their operations, particularly to accelerate and scale established workflows.

Recent activities illustrate this AI-enabled acceleration and scaling: Jade Sleet launched campaigns through three front companies in a single week, Onyx Sleet generated dozens of tailored lures in minutes, Coral Sleet rapidly built a new capability to trojanize private source code repositories, and Diamond Sleet used AI to enhance tailored targeting workflows, including persona development and front company creation. Further, Onyx Sleet and Pearl Sleet are leveraging the open-source agentic AI penetration testing framework ARTEX to conduct operations, further indicating North Korea’s willingness to quickly adopt new AI technologies for their operations.

The Democratic People’s Republic of Korea operates under extensive international sanctions and uses cyber operations and other illicit mechanisms to evade these restrictions and advance state objectives. Within this operating environment, North Korean threat actors have adopted new technologies that help sustain or advance existing operations. AI adoption by North Korean threat actors therefore largely supports existing goals and targeting priorities rather than representing a shift in actor motivations. North Korean threat actors conduct cyber operations primarily to generate revenue for the regime, collect strategic intelligence, and, in some cases, pursue politically motivated disruptive or destructive objectives. Across these objectives, North Korean threat actor tradecraft remains grounded in social engineering, malware delivery, and the abuse of legitimate tools. These operations commonly target cryptocurrency and financial organizations, information technology companies and software supply chains, government entities, and education-related organizations. Despite threat actors’ adoption of AI, Microsoft Threat Intelligence assesses that AI-enabled operations remain human-directed and have not become fully autonomous.

Microsoft Threat Intelligence assesses the overall adoption of AI across North Korean threat actors as high, with threat actors such as Jade Sleet, Coral Sleet, and Jasper Sleet demonstrating an established use of AI across all operational workflows, alongside increasing adoption across the broader North Korean threat actor set. This blog breaks down how North Korean threat actors are utilizing AI across their operations, reflecting a broader trend of threat actors incorporating AI into their attack chains. We also provide mitigation guidance and Microsoft Defender detections to help organizations defend against these threats.

## Stages of AI adoption by North Korean threat actors

North Korean threat actors are increasingly integrating generative and agentic AI platforms into their operations, but the rate and maturity of adoption vary. Based on identified AI use, Microsoft Threat Intelligence assesses high-impact North Korean threat actors across four stages of adoption: emerging, expanding, accelerating, and operationalized. Across these actors, AI use spans research, content generation, development, malware and tooling, infrastructure, and broader operational activities.

Operationalized: Threat actors at this stage have embedded AI into routine operational workflows, using it as an established part of their existing processes. Microsoft Threat Intelligence assesses that the North Korean threat actors Jade Sleet, Coral Sleet, and [Jasper Sleet](https://www.microsoft.com/en-us/security/blog/2025/06/30/jasper-sleet-north-korean-remote-it-workers-evolving-tactics-to-infiltrate-organizations/) have operationalized AI across their entire operations, which frequently encompass identity-based attacks built on deceptive social engineering. These attacks can be accelerated with AI capabilities that tailor lures or personas to the intended audience.

Accelerating: Threat actors at this stage demonstrate rapid adoption of AI across multiple operational functions. Microsoft Threat Intelligence assesses that [Diamond Sleet](https://www.microsoft.com/en-us/security/blog/2023/11/22/diamond-sleet-supply-chain-compromise-distributes-a-modified-cyberlink-installer/), Onyx Sleet, Pearl Sleet, and [Sapphire Sleet](https://www.microsoft.com/en-us/security/blog/tag/sapphire-sleet/) are at the accelerating stage of AI adoption.

Expanding: Threat actors at this stage are expanding their use of AI across selected operational activities, but adoption is not yet embedded across broader workflows. Microsoft Threat Intelligence assesses that Emerald Sleet is at the expanding stage of AI adoption. While evidence suggests Emerald Sleet has incorporated AI into some workflows, Microsoft Threat Intelligence has not identified the same level of adoption and impact as other North Korean threat actors.

Emerging: Threat actors at this stage demonstrate limited or experimental use of AI. At this time, Microsoft Threat Intelligence has not assessed any North Korean threat actors as operating at the emerging stage.

## AI use across North Korean threat operations

Microsoft Threat Intelligence has identified North Korean threat actors using AI platforms to support a range of operational activities, from reconnaissance to developing social engineering content, maintaining fraudulent identities, supporting tool development, and scaling repetitive operational tasks. Current evidence indicates that these actors primarily use AI to enhance existing tradecraft and operator productivity rather than to enable autonomous operations. Microsoft Threat Intelligence has identified North Korean threat actors leveraging the following AI-enabled tactics as part of their threat operations.

### AI-assisted targeting and reconnaissance

Based on industry reporting and changes in targeting activity in 2026, North Korean threat actors are scaling reconnaissance capabilities by using generative AI platforms, including gathering information on target organizations prior to launching social engineering operations. Microsoft Threat Intelligence has identified that these actors:

- Research organizations and employees, then use information from this research to craft highly bespoke and convincing lures, target-specific infrastructure, and job applications
- Research wallets, exchanges, and decentralized finance (DeFi) and blockchain workflows, accelerating the development of domain knowledge needed to support targeted operations
- Explore vulnerabilities, APIs, security products, and cloud services, leading to a demonstrated change in the speed and sophistication of threat activity against specific technologies
- Research software development roles, job requirements, and technology organizations to support job searching, resume development, and persona alignment, resulting in rapid tailored persona or lure creation, application to newly posted job roles, or spear-phishing operations

For example, between June 8 and June 12, 2026, Microsoft Threat Intelligence identified Jade Sleet conducting job-themed targeting against individuals across various organizations, including those involved in cybersecurity, AI, blockchain, and talent recruitment companies. The actor leveraged tailored domains, social media profiles, and industry-specific knowledge to pose as recruiters for a spoofed AI-powered blockchain intelligence company, using software engineer-themed opportunities to initiate contact and schedule interviews with individuals who engaged with the outreach. Within this short time frame, Jade Sleet conducted similar job-themed targeting using two additional front companies, supported by comparable infrastructure and relevant domain knowledge. Microsoft Threat Intelligence assesses that the pace and breadth of this activity demonstrate how Jade Sleet is using generative AI to accelerate operational workflows, including rapidly developing target- and industry-specific knowledge, tailoring reconnaissance and targeting, and scaling outreach to target individuals.

Jasper Sleet also continues to leverage generative AI platforms to build fake digital personas. The actor’s suspected use of generative and agentic AI-assisted resume workflows demonstrates an improvement in the speed, scale, and relevance of persona preparation over the past year. Identified application activity indicates that the actor has invested in repeatable tooling to support employment-themed operations, ultimately helping the actor scale application activity and interact more credibly with the hiring processes of impacted organizations.

Since August 2026, Microsoft Threat Intelligence has observed Diamond Sleet returning to targeting the oil and gas sector for the first time since 2023, expanding their focus on communications and internet policy-related organizations, and continuing to target defense-related organizations. Further, Diamond Sleet has created fake communications technology companies, complete with supporting websites and tailored personas, to target telecommunications companies under the guise of legitimate business partnerships. These shifts have occurred alongside Diamond Sleet’s increased use of generative AI platforms to support reconnaissance and technical development, suggesting that AI could be improving the efficiency of existing operational workflows.

### AI-assisted social engineering and identity deception

Several North Korean threat actors leverage job-themed social engineering techniques to gain access to target environments. For example, Sapphire Sleet, Jade Sleet, and Coral Sleet use employment- and interview-themed social engineering to target users and organizations, while Jasper Sleet uses fraudulent identities to obtain legitimate remote employment. These actors leverage AI to improve the process of creating convincing lures, aid in the development of fake personas, and evade detection when interacting with targets. Specifically, these actors use AI to:

- Produce tailored phishing, recruiter, and investment lures
- Create job-themed payload-delivery content and malicious repository lures
- Translate content and adjust tone to support foreign-language impersonation and more natural communications
- Build resumes, biographies, and realistic interview responses
- Support coding assessments, job-related tasks, and the management of multiple worker personas
- Enhance profile images and other identity artifacts
- Alter profile images, video, voice, and backgrounds
- Sustain recruiter, developer, investor, and other social identities across interactions and platforms

Microsoft Threat Intelligence has identified over 100 PDF lure files attributed to Onyx Sleet that were created in August and September 2026 with target-specific details. Metadata indicated that the actor created dozens of files at a time in rapid succession within minutes, highly likely to be the output of an AI platform. This automation supports the actor’s high-volume phishing campaigns against South Korean users and could make disruption and detection efforts more difficult given the rapid regeneration or modification of additional lures.

Microsoft Threat Intelligence has also identified possible synthetic media generation, focused on AI-created voice and video, by Emerald Sleet. While we have not been able to determine the full operational impact of such tooling, it is highly likely that synthetic media creation is valued by multiple North Korean threat actors, as it significantly enhances existing social engineering capabilities.

### AI-assisted software and tooling development

Microsoft Threat Intelligence has identified evidence indicating that North Korean threat actors are leveraging AI-enabled software and tools to assist in malware development. These tools include AI-assisted development platforms, such as Cursor, which have likely enabled Jade Sleet, Coral Sleet, Pearl Sleet, and Sapphire Sleet to:

- Generate, convert, debug, and refactor code
- Assist with scripts, commands, persistence mechanisms, and obfuscation
- Troubleshoot errors and help operators diagnose tool behavior
- Support the adaptation or reimplementation of functionality across languages, libraries, and environments

Additionally, AI-enabled development cycles further allow threat actors to circumvent detection and blocking efforts, as AI platforms streamline retooling, helping enable threat actors to rapidly pivot in reaction to defensive measures.

For example, Microsoft Threat Intelligence has identified evidence indicating that Sapphire Sleet, who has conducted several supply chain attacks, likely incorporated AI during the August 2026 Rust software compromise. The activity spanned from initial stages targeting Rust developers to development and deployment of malware. Notably, Sapphire Sleet’s malware in this campaign was a marked improvement compared with other attributed campaigns, as the malware used dynamic .NET compilation during post-exploitation, most likely for defense evasion.

And, since April 2026, Coral Sleet has operationalized a workflow to trojanize private GitHub repositories, integrating them into their existing malware chain. This new capability, its breadth and scale, and its rapid implementation were highly likely engineered using an AI-enabled development platform.

### AI-assisted operational scaling and analysis

North Korean threat actors are leveraging AI platforms to scale and manage diverse operations. For example, Jasper Sleet’s AI tooling helps maintain consistent communication and performance across multiple fraudulent worker personas. We have also seen evidence of AI use for automating repetitive tasks, summarizing collected information from victim organizations, and accelerating post-compromise decision making while human operators likely continue to direct intent and objectives. This operational adoption extends to emerging agentic AI technologies. Since late October 2026, Microsoft Threat Intelligence has identified Onyx Sleet and Pearl Sleet leveraging open-source agentic AI penetration testing ARTEX in operations, highlighting how North Korean threat actors are adopting new AI technologies as they become available.

## Mitigation and protection guidance

Threat actor misuse of AI accelerates risk across enterprise environments by amplifying existing threats such as phishing, malware threats, and insider activity. To help organizations stay ahead of AI-enabled threat activity, Microsoft has introduced the [Security Dashboard for AI](http://ai.security.microsoft.com/). The dashboard provides users with a unified view of AI security posture by aggregating security, identity, and data risk across [Microsoft Defender](https://www.microsoft.com/security/business/microsoft-defender), [Microsoft Entra](https://www.microsoft.com/security/business/microsoft-entra), and [Microsoft Purview](https://www.microsoft.com/security/business/microsoft-purview). This allows organizations to understand what AI assets exist in their environment, recognize emerging risk patterns, and prioritize governance and security across AI agents, applications, and platforms. To learn more about the Microsoft Security Dashboard for AI see: [Assess your organization’s AI risk with Microsoft Security Dashboard for AI](https://learn.microsoft.com/security/security-for-ai/security-dashboard-for-ai).

Additionally, [Microsoft Agent 365](https://www.microsoft.com/microsoft-365/blog/2025/11/18/microsoft-agent-365-the-control-plane-for-ai-agents/) serves as a control plane for AI agents in enterprise environments, allowing users to manage, govern, and secure AI agents and workflows while monitoring emerging risks of agentic AI use. Agent 365 supports a growing ecosystem of agents, including Microsoft agents, broader ecosystems of agents such as Adobe and Databricks, and open-source agents published on GitHub.

As the AI-enabled operations conducted by North Korean threat actors vary across tactics, techniques, and procedures (TTPs), the following guidance can help organizations harden their networks against multiple classes of threats.

**Vulnerability and exposure management**

- Use [Microsoft Defender Vulnerability Management](https://learn.microsoft.com/defender-vulnerability-management/defender-vulnerability-management) to identify, assess, remediate, and track vulnerabilities across critical assets. Use the [exposure score](https://learn.microsoft.com/defender-vulnerability-management/tvm-exposure-score#how-to-use-exposure-score-to-reduce-your-vulnerability-exposure) to reduce your vulnerability exposure and the Microsoft Secure Score to identify and remediate security misconfigurations in your environment.
- Use a perimeter scanning tool like [Microsoft Defender External Attack Surface Management](https://learn.microsoft.com/azure/external-attack-surface-management/overview) to understand your organization’s digital footprint and potential attack surface. Targeting web-facing vulnerabilities continues to be one of the most effective attack methods for initial access.
- Ensure any web-facing systems are isolated from the public internet with a secure network boundary and access them with a virtual private network (VPN). If certain servers must be accessible on the public internet, position them behind a [web application firewall (WAF)](https://azure.microsoft.com/products/web-application-firewall/), [reverse proxy](https://microsoft.github.io/reverse-proxy/articles/getting-started.html), or [perimeter network](https://learn.microsoft.com/azure/architecture/reference-architectures/dmz/secure-vnet-dmz) (also known as a DMZ), which can reduce the risk of vulnerability exploitation in some cases.
- Consider automating patching where possible. [Windows Update client policies](https://learn.microsoft.com/windows/deployment/update/waas-manage-updates-wufb) offer automated patching, which can greatly reduce the amount of time IT admins must spend identifying, configuring, and deploying updates.
- To help manage infrastructure distributed across cloud, on-premises, and hybrid networks, use a centralized patching solution like [Azure Update Manager](https://learn.microsoft.com/azure/update-manager/overview).

**Protecting against social engineering and phishing**    

- Educate users about [protecting personal and business information](https://www.microsoft.com/security/business/security-101/what-is-email-security) on social media, filtering unsolicited communication, identifying lures in spear-phishing emails and watering holes, and reporting reconnaissance attempts and other suspicious activity.
- Educate users about [preventing malware infections](https://www.microsoft.com/security/business/security-101/what-is-malware), such as ignoring or deleting unsolicited and unexpected emails or attachments sent through instant messaging applications or social networks.
- [Review the recommended settings](https://learn.microsoft.com/defender-office-365/recommended-settings-for-eop-and-office365) for Exchange Online Protection and Microsoft Defender for Office 365 to ensure your organization has established essential defenses and knows how to monitor and respond to threat activity.
- Invest in user awareness training and phishing simulations. [Attack simulation training](https://learn.microsoft.com/defender-office-365/attack-simulation-training-get-started) in Microsoft Defender for Office 365, which also includes simulating phishing messages in Microsoft Teams, is one approach to running realistic attack scenarios in your organization.
- Enable [Zero-hour auto purge (ZAP)](https://learn.microsoft.com/defender-office-365/zero-hour-auto-purge) in Defender for Office 365 to quarantine sent mail in response to newly acquired threat intelligence and retroactively neutralize malicious phishing, spam, or malware messages that have already been delivered to mailboxes.
- Responders could also manually check for and purge unwanted emails containing URLs and/or Subject fields that are similar, but not identical, to those of known bad messages.
- [Investigate malicious email that was delivered in Microsoft 365](https://learn.microsoft.com/defender-office-365/threat-explorer-investigate-delivered-malicious-email) and use [Threat Explorer](https://security.microsoft.com/threatexplorer) to find and delete phishing emails.
- Turn on [Safe Links](https://learn.microsoft.com/defender-office-365/safe-links-about) and [Safe Attachments](https://learn.microsoft.com/defender-office-365/safe-attachments-about) in Microsoft Defender for Office 365.
- Only allow device code flow where necessary. Microsoft recommends [blocking device code flow wherever possible](https://learn.microsoft.com/entra/identity/conditional-access/policy-block-authentication-flows). Where necessary, configure Microsoft Entra ID’s [device code flow](https://learn.microsoft.com/entra/identity/conditional-access/concept-authentication-flows) in your Conditional Access policies.

**Vetting potential employees**

- Exercise greater scrutiny for employees of staffing companies, since this is the easiest avenue for North Korean workers to infiltrate target companies.
- Check to make sure a potential employee’s social media/professional accounts are not highly similar to the accounts of other individuals. In addition, check that a contact phone number listed on a potential employee’s account is unique and not also used by other accounts.
- Scrutinize resumes and background checks for consistency of names, addresses, and dates. Consider contacting references by phone or video-teleconference rather than email only.
- Search whether a potential employee is employed at multiple companies using the same persona.
- Ensure the potential employee is seen on camera during multiple video telecommunication sessions. If the potential employee reports video and/or microphone issues that prohibit participation, this should be considered a red flag.
- Confirm the potential employee has a digital footprint. This includes a real phone number (not VOIP), a residential address, and social media accounts.

**Defending against malware**

- Turn on [cloud-delivered protection](https://docs.microsoft.com/microsoft-365/security/defender-endpoint/configure-block-at-first-sight-microsoft-defender-antivirus) in Microsoft Defender Antivirus or the equivalent for your antivirus product to cover rapidly evolving attacker tools and techniques. Cloud-based machine learning protections block a majority of new and unknown variants.
- Ensure Microsoft Defender Antivirus definitions are up to date and [real-time protection is turned on](https://learn.microsoft.com/microsoft-365/security/defender-endpoint/configure-real-time-protection-microsoft-defender-antivirus).
- Run [endpoint detection and response (EDR) in block mode](https://learn.microsoft.com/defender-endpoint/edr-in-block-mode) so that Microsoft Defender for Endpoint can block malicious artifacts, even when your non-Microsoft antivirus does not detect the threat or when Microsoft Defender Antivirus is running in passive mode. EDR in block mode works behind the scenes to remediate malicious artifacts that are detected post-breach.
- Configure [investigation and remediation](https://learn.microsoft.com/defender-endpoint/automated-investigations) in full automated mode to let Microsoft Defender for Endpoint take immediate action on alerts to resolve breaches, significantly reducing alert volume.
- Configure [automatic attack disruption](https://learn.microsoft.com/defender-xdr/configure-attack-disruption) in Microsoft Defender XDR. Automatic attack disruption is designed to contain attacks in progress, limit the impact on an organization’s assets, and provide more time for security teams to remediate the attack fully.
- Enable [network protection](https://learn.microsoft.com/defender-endpoint/enable-network-protection) in Microsoft Defender for Endpoint.
- Microsoft Defender XDR customers can turn on [attack surface reduction rules](https://learn.microsoft.com/defender-endpoint/attack-surface-reduction) to prevent several of the infection vectors of this threat. These rules, which can be configured by users with administrator rights, offer significant hardening against targeted attacks. In observed attacks, Microsoft customers who had the following rules turned on could mitigate the attack in the initial stages and prevent hands-on-keyboard activity:

## Microsoft Defender detections

[Microsoft Defender](https://www.microsoft.com/security/business/microsoft-defender) customers can refer to the list of applicable detections below. Microsoft Defender coordinates detection, prevention, investigation, and response across endpoints, identities, email, and apps to provide integrated protection against attacks like the threat discussed in this blog.

| **Tactic** | **Observed activity** | **Microsoft Defender coverage** | 
| Actor-specific alerts | Known threat actor activity | **Microsoft Defender for Endpoint** – Emerald Sleet threat actor activity – Diamond Sleet Actor activity detected – Onyx Sleet activity group – Pearl Sleet actor activity detected – Sapphire Sleet actor activity – Jade Sleet threat actor activity detected – Coral Sleet activity | 
| Reconnaissance | AI-assisted research of target organizations | **Microsoft Defender for Cloud** – Possible AI Tools Reconnaissance Detected – Possible Secret Reconnaissance Detected | 
| Initial access | Sign-in activity; phishing | **Microsoft Defender XDR** – Sign-in activity by a suspected North Korean entity Jasper Sleet **Microsoft Entra ID Protection** – Atypical travelImpossible travel – Microsoft Entra threat intelligence (sign-in) **Microsoft Defender for Office 365** – A potentially malicious URL click was detected – A user clicked through to a potentially malicious URL – Suspicious email sending patterns detected – Email messages containing malicious URL removed after delivery – Email messages removed after delivery – Email reported by user as malware or phish | 
| Execution | Backdoors observed in Sapphire Sleet Rust software compromise | **Microsoft Defender Antivirus** – Trojan:Linux/ProcmacSteal – Trojan:PowerShell/ProcmacSteal – Trojan:MacOS/ProcmacSteal – Trojan:Cargo/ProcmacSteal | 

#### Microsoft Security Copilot

[Microsoft Security Copilot](https://www.microsoft.com/security/business/ai-machine-learning/microsoft-security-copilot) is [embedded in Microsoft Defender](https://learn.microsoft.com/defender-xdr/security-copilot-in-microsoft-365-defender) and provides security teams with AI-powered capabilities to summarize incidents, analyze files and scripts, summarize identities, use guided responses, and generate device summaries, hunting queries, and incident reports.

Customers can also [deploy AI agents](https://learn.microsoft.com/defender-xdr/security-copilot-agents-defender), including the following [Microsoft Security Copilot agents](https://learn.microsoft.com/copilot/security/agents-overview), to perform security tasks efficiently:

- [Threat Intelligence Briefing agent](https://learn.microsoft.com/defender-xdr/threat-intel-briefing-agent-defender)
- [Phishing Triage agent](https://learn.microsoft.com/defender-xdr/phishing-triage-agent)
- [Threat Hunting agent](https://learn.microsoft.com/defender-xdr/advanced-hunting-security-copilot-threat-hunting-agent)
- [Dynamic Threat Detection agent](https://learn.microsoft.com/defender-xdr/dynamic-threat-detection-agent)

Security Copilot is also available as a [standalone experience](https://learn.microsoft.com/copilot/security/experiences-security-copilot) where customers can perform specific security-related tasks, such as incident investigation, user analysis, and vulnerability impact assessment. In addition, Security Copilot offers [developer scenarios](https://learn.microsoft.com/copilot/security/developer/custom-agent-overview) that allow customers to build, test, publish, and integrate AI agents and plugins to meet unique security needs.

#### Threat intelligence reports

Microsoft Defender XDR customers can use the following [threat analytics](https://learn.microsoft.com/defender-xdr/threat-analytics) reports in the Defender portal (requires license for at least one Defender XDR product) to get the most up-to-date information about the activity and techniques discussed in this blog. These reports provide intelligence, protection information, and recommended actions to prevent, mitigate, or respond to associated threats found in customer environments.

Microsoft Security Copilot customers can also use the [Microsoft Security Copilot integration](https://learn.microsoft.com/defender/threat-intelligence/security-copilot-and-defender-threat-intelligence?bc=%2Fsecurity-copilot%2Fbreadcrumb%2Ftoc.json&toc=%2Fsecurity-copilot%2Ftoc.json#turn-on-the-security-copilot-integration-in-defender-ti) in Microsoft Defender Threat Intelligence, either in the Security Copilot standalone portal or in the [embedded experience](https://learn.microsoft.com/defender/threat-intelligence/using-copilot-threat-intelligence-defender-xdr) in the Microsoft Defender portal to get more information about this threat.

#### Learn more

For the latest security research from the Microsoft Threat Intelligence community, check out the [Microsoft Threat Intelligence Blog](https://aka.ms/threatintelblog).

To get notified about new publications and to join discussions on social media, follow us on [LinkedIn](https://www.linkedin.com/showcase/microsoft-threat-intelligence), [X (formerly Twitter)](https://x.com/MsftSecIntel), and [Bluesky](https://bsky.app/profile/threatintel.microsoft.com).

To hear stories and insights from the Microsoft Threat Intelligence community about the ever-evolving threat landscape, listen to the [Microsoft Threat Intelligence podcast](https://thecyberwire.com/podcasts/microsoft-threat-intelligence).
