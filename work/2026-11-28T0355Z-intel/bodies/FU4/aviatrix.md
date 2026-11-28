---
title: "SAP GitHub Breach 2026: AI-Assisted Token Theft & Supply-Chain Risk"
url: https://aviatrix.ai/threat-research-center/sap-confirms-security-incident-after-suspicious-github-activity/
hostname: aviatrix.ai
description: SAP confirmed a 2026 GitHub breach (Project Granite) where attackers stole auth tokens and modified source code using agentic AI tools. Learn the supply-chain risk.
sitename: Aviatrix.ai
date: "2026-11-28"
categories: ['Threat Research']
tags: ['SAP GitHub breach 2026', 'Project Granite SAP', 'supply chain attack 2026', 'credential theft GitHub', 'agentic AI cyberattack', 'authentication token theft', 'SAP source code compromise', 'enterprise software supply chain', 'ARTEX CAIRN PentAGI', 'BSI agentic AI warning', 'zero trust segmentation', 'egress security', 'multicloud visibility', 'NIST CSF supply chain', 'PCI DSS source code integrity']
fingerprint: e503501b4e90be1b
language: en
image: https://images.ctfassets.net/mvxxnmpzvwpe/7LF531v5CcbaanUvNBUPdI/8d32d5096f431dbfa2d3062ddd70fe49/sap-confirms-security-incident-after-suspicious-github-activity.png?w=1200&h=630&fit=fill&fm=jpg&q=85
pagetype: website
filedate: "2026-11-28"
---
## Executive Summary

In November 2026, SAP SE confirmed a security incident tracked internally as 'Project Granite,' in which threat actors breached the company's GitHub environment and stole authentication tokens from SAP employees. Leveraging those credentials—reportedly with assistance from agentic AI tools—the attackers copied and modified SAP source code repositories. SAP, which serves over 300 million subscribers globally and generates more than $40 billion in annual revenue, stated it found no evidence of downstream compromise to customer business data, but declined to clarify whether customers pulling code from affected repositories faced residual risk.

This incident reflects a sharp escalation in supply-chain attacks that weaponize developer credential theft and AI-assisted intrusion tools. Germany's BSI simultaneously warned of agentic AI platforms such as ARTEX, CAIRN, and PentAGI being used in cyberattacks, signaling that AI-augmented threat actors are actively targeting enterprise software pipelines—a trend that raises systemic risk for every downstream SAP customer.

## Why This Matters Now

Agentic AI tools are lowering the barrier for sophisticated supply-chain attacks against major enterprise software vendors. With SAP embedded in critical business processes across thousands of global organizations, source-code tampering or token compromise in its GitHub environment could propagate malicious changes silently to hundreds of thousands of downstream systems—making rapid detection, egress control, and zero-trust segmentation urgent priorities for every SAP customer.

## Attack Path Analysis

Attackers leveraged AI-assisted tools (potentially ARTEX, CAIRN, or PentAGI-class agentic systems) to target SAP employees, stealing authentication tokens that granted access to SAP's GitHub environment where source code was copied and modified. The attackers moved through SAP's developer and CI/CD infrastructure using stolen credentials, established covert command-and-control channels to exfiltrate source code and potentially sensitive tokens at scale, with the ultimate impact being unauthorized modification of enterprise source code and risk of downstream supply chain compromise affecting SAP's 300 million subscribers.

## Kill Chain Progression

This analysis maps confirmed threat intelligence to the full cloud kill chain to show where defensive gaps would emerge as an attack progresses.

### Initial Compromise

#### Description

Attackers, likely aided by agentic AI tooling (consistent with BSI warnings about ARTEX, CAIRN, PentAGI), targeted SAP employees through credential harvesting or phishing campaigns to obtain authentication tokens. The use of AI tools suggests automated, high-velocity reconnaissance and credential targeting against SAP's GitHub-integrated developer workforce. CNSF Cloud Native Security Fabric controls with inline enforcement and real-time inspection could have flagged anomalous AI-driven access patterns at the perimeter before token theft was completed.

## MITRE ATT&CK® Techniques

### Steal Application Access Token

### Unsecured Credentials: Credentials In Files

### Supply Chain Compromise: Compromise Hardware Supply Chain

### Compromise Accounts: Email Accounts

### Data Manipulation: Stored Data Manipulation

### Data from Information Repositories: Code Repositories

### Obtain Capabilities: Tool

### Valid Accounts

## Potential Compliance Exposure

Mapping incident impact across multiple compliance frameworks.

### NIS2 Directive – Cybersecurity Risk Management Measures

Control ID: Article 21 – Security of Network and Information Systems

### DORA (Digital Operational Resilience Act) – ICT Security and Access Control

Control ID: Article 9 – ICT Security Policies, Procedures, Protocols and Tools

### CISA Zero Trust Maturity Model 2.0 – Identity and Credential Lifecycle Management

Control ID: Identity Pillar – Credential Management and Least Privilege Access

### ISO/IEC 27001:2022 – Privileged Account and Repository Access Controls

Control ID: Annex A 8.2 – Privileged Access Rights; Annex A 8.9 – Configuration Management

### GDPR (General Data Protection Regulation) – Technical Security Measures and Breach Notification

Control ID: Article 32 – Security of Processing; Article 33 – Notification of Personal Data Breach

### PCI DSS 4.0 – Software Integrity and Authentication Token Security

Control ID: Requirement 6.3 – Security of Software and Source Code; Requirement 8.6 – Authentication Management

## Sector Implications

Industry-specific impact of the vulnerabilities, including operational, regulatory, and cloud security risks.

##### Information Technology/IT

SAP's GitHub credential theft and source code tampering directly exposes IT organizations relying on SAP integrations, risking supply-chain compromise, lateral movement, and unauthorized exfiltration of enterprise pipeline data.

##### Computer Software/Engineering

Authentication token theft enabling SAP source code modification threatens software engineering firms using SAP repositories, with AI-assisted attacks bypassing egress controls and zero trust segmentation across hybrid cloud environments.

##### Financial Services

As major SAP ERP consumers, financial services firms face elevated supply-chain risk; stolen tokens and modified code could undermine PCI 4.0 and NIST 800-53 compliance controls governing transaction integrity and data-in-transit encryption.

##### Government Administration

Government agencies running SAP platforms face critical exposure from AI-driven credential theft; BSI's concurrent warning amplifies ZTMM and NIST CSF compliance urgency given risks of undetected lateral movement within sovereign infrastructure.

## Sources

- [SAP confirms security incident after suspicious GitHub activity](https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/)https://www.bleepingcomputer.com/news/security/sap-confirms-security-incident-after-suspicious-github-activity/Verified
- [BSI Warning on Agentic AI Cyberattack Tools (ARTEX, CAIRN, PentAGI)](https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2026/261126_agentische-KI.html)https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2026/261126\_agentische-KI.htmlVerified
- [SAP Corporate Information and Company Overview](https://www.sap.com/about/company.html)https://www.sap.com/about/company.htmlVerified
- [Der Spiegel: SAP Cyberattack Report - Project Granite](https://www.spiegel.de/netzwelt/sap-wird-opfer-von-hackerangriff-a-6648b5ce-5d74-48dc-86ea-9469705bb91d)https://www.spiegel.de/netzwelt/sap-wird-opfer-von-hackerangriff-a-6648b5ce-5d74-48dc-86ea-9469705bb91dVerified
- [Italy and Switzerland warn of autonomous AI-driven cyberattacks](https://www.bleepingcomputer.com/news/security/italy-and-switzerland-warn-of-autonomous-ai-driven-cyberattacks/)https://www.bleepingcomputer.com/news/security/italy-and-switzerland-warn-of-autonomous-ai-driven-cyberattacks/Verified

## Frequently Asked Questions

### Cloud Native Security Fabric Mitigations and ControlsCNSF

Based on the attack progression modeled above, these are the defensive controls that would constrain each stage.

Aviatrix Zero Trust CNSF is directly relevant to this incident because attackers moved through SAP's developer and CI/CD infrastructure using stolen tokens, exploiting the absence of identity-aware segmentation and controlled egress. Had Zero Trust controls been in place, the attacker's reachability across repositories and their ability to exfiltrate source code at scale would likely have been meaningfully constrained.

Control: Cloud Native Security Fabric (CNSF)

Mitigation: Inline enforcement and real-time traffic inspection could have flagged the high-frequency, anomalous access patterns associated with AI-driven credential targeting before token theft was completed, reducing the attacker's ability to silently complete the initial access phase undetected.

Control: Zero Trust Segmentation

Mitigation: Identity-based segmentation policies enforcing least-privilege access at the repository namespace level could have constrained the scope of what a compromised token was permitted to reach, reducing the blast radius even after a token was successfully stolen.

Control: East-West Traffic Security

Mitigation: East-west enforcement monitoring workload-to-workload and service-to-service flows within SAP's cloud-hosted developer infrastructure could have detected anomalous inter-repository access patterns and unexpected API calls between internal systems, likely reducing how far the attacker could pivot before triggering an alert.

Control: Multicloud Visibility & Control

Mitigation: Centralized traffic observability across SAP's cloud-hosted developer infrastructure would likely have identified the high-frequency, repetitive GitHub API call patterns and suspicious automation behavior indicative of attacker-controlled tooling operating within the environment.

Control: Egress Security & Policy Enforcement

Mitigation: Outbound traffic policy enforcement with FQDN filtering could have blocked or generated high-confidence alerts on unauthorized bulk data transfers leaving SAP's developer environment to external destinations, likely reducing the volume of source code successfully exfiltrated.

Had prior Zero Trust controls constrained token scope, limited lateral repository access, and enforced egress policy, the attacker's ability to reach and modify production source code at scale would likely have been reduced, narrowing the set of repositories exposed to unauthorized modification.

### Impact at a Glance

#### Affected Business Functions

- Enterprise Software Development and Source Code Integrity
- Software Update and Patch Distribution Pipeline
- Customer Trust and SaaS Platform Security Assurance
- Internal Developer Authentication and Identity Management

Estimated downtime: 3 days

Estimated loss: N/A

Authentication tokens belonging to SAP employees were reportedly stolen and used to access and potentially modify SAP source code repositories on GitHub. While SAP stated no customer business data was confirmed as accessed, the exposure of proprietary enterprise source code at this scale poses severe risks: (1) insertion of malicious backdoors into SAP software products used by over 300 million subscribers globally, (2) theft of intellectual property representing decades of enterprise ERP, CRM, and SCM development, (3) potential downstream supply-chain compromise if modified code was distributed to customers via software updates before detection. The scope of modified source code and the number of repositories affected has not been publicly disclosed. Financial loss is currently listed as $0 due to no confirmed customer breach, but potential downstream liability and remediation costs for a vendor of SAP's scale could reach hundreds of millions of dollars.

### Recommended Actions

### Key Takeaways & Next Steps

- • Apply Zero Trust Segmentation with identity-based policy and least-privilege namespace enforcement on all developer tooling, GitHub integrations, and CI/CD pipelines so that compromised authentication tokens are constrained to minimal repository scopes and cannot traverse the full source code estate.
- • Deploy Egress Security and Policy Enforcement with FQDN filtering and outbound traffic controls on all developer workstations and cloud-hosted build environments to detect and block unauthorized bulk code transfers or repository cloning to external destinations.
- • Enable Multicloud Visibility and Control with centralized traffic observability and anomaly detection tuned to identify suspicious automation patterns, high-velocity GitHub API calls, and anomalous control-plane interactions consistent with agentic AI-assisted attacker tooling.
- • Implement Encrypted Traffic inspection controls (HPE) on data-in-transit paths from developer environments to external endpoints to ensure exfiltration via encrypted covert channels can be detected and blocked before source code or embedded secrets leave the organization.
- • Deploy Cloud Native Security Fabric (CNSF) inline enforcement with real-time inspection at the developer environment perimeter to detect AI-driven credential harvesting and token theft activity early in the kill chain, reducing dwell time before authentication tokens are leveraged for repository access.
