---
title: "Mitigating OVERPASS (CVE-2026-44756): A Critical SAP Kernel Vulnerability"
author: JP Perez-Etchegoyen
url: https://onapsis.com/blog/sap-overpass-remediation/
hostname: onapsis.com
description: Remediate OVERPASS (CVE-2026-44756), a critical pre-authentication SAP kernel vulnerability reachable over several SAP communication protocols. Read the step-by-step guide.
sitename: Onapsis Research Labs
date: "2026-09-21"
tags: ['JP Perez-Etchegoyen', 'CVE-2026-44756', 'Onapsis Research Labs', 'OVERPASS', 'sap exploits', 'SAP Extended Passport', 'SAP GUI', 'SAP vulnerabilities', 'SAP zero-day vulnerability']
fingerprint: a5b819968eb9eda8
language: en
image: https://onapsis.com/wp-content/uploads/blog-overpass.png
pagetype: article
filedate: "2026-11-25"
---
The Onapsis Research Labs goes over a threat advisory on the newly released SAPMAP Exploitation Toolkit containing the latest threat insights and protection guidance. This toolkit contains multiple exploits and offensive security capabilities for SAP systems, including proof-of-concept (PoC) exploits for critical vulnerabilities OVERPASS and S4GET (which Onapsis discovered and helped SAP patch just weeks ago). [Watch the on demand webinar here](https://onapsis.com/resources/webinars/onapsis-research-labs-threat-advisory/).

This threat briefing with the Onapsis Research Labs and SAP reviews September’s 2026 Patch Day and the critical vulnerabilities that were released. Our threat intelligence experts provide guidance to organizations on the latest patches released by SAP, including the critical vulnerabilities CVE-2026-44756 and CVE-2026-58240. [Watch the on demand session here](https://onapsis.com/resources/webinars/sept-patch-day-26-vulns/)

CVSS Score: 10.0 (Critical) | Risk Level: Critical, Immediate Action Required

[Onapsis Research Labs](https://onapsis.com/threat-research/onapsis-research-labs/) identified and responsibly disclosed to SAP a critical flaw in the SAP kernel’s processing of the Extended Passport (EPP), the standard SAP tracing structure that clients attach to their requests. Because EPP processing is shared kernel code used by more than one protocol, the flaw is reachable from the Internet-facing web layer, from the SAP GUI layer every end user connects to, and from the RFC layer that links SAP systems to one another.

Tracked as CVE-2026-44756 and named OVERPASS by the Onapsis Research Labs, the vulnerability:

- Is exploitable remotely and without authentication;
- Is rated Critical, at the maximum possible CVSS score (10.0);
- Exists by default in a wide range of SAP technology components;
- Allows remote attackers to run arbitrary operating system commands on the SAP host with SAP administrative privileges, resulting in full compromise of the underlying SAP business data and processes;
- It is reachable through several SAP components and several communication protocols, none of them requiring credentials, so no single network control can fully mitigate risk.

SAP released Security Note 3747649 addressing this vulnerability during the [September SAP Patch Day](https://onapsis.com/blog/sap-security-patch-day-september-2026/). A single kernel patch closes all exploitation vectors. Onapsis strongly recommends that all organizations treat patching as an emergency priority. SAP responded swiftly to this disclosure, reflecting a strong commitment to protecting the SAP ecosystem.

As of publication, Onapsis Research Labs has not observed active in-the-wild exploitation. Onapsis continues to monitor the global SAP threat landscape and will deliver in-product updates and threat insights (including indicators of compromise) to clients if malicious activity occurs. This advisory will be updated with any new observations.

*The Onapsis Research Labs adhere to a strict set of responsible disclosure practices. Consequently, this post will intentionally omit technical exploitation details at this time and is solely focused on helping SAP customers assess exposure and support prompt risk remediation actions.*

## Understanding the OVERPASS Risk

The Extended Passport (EPP) is a standard SAP tracing feature. According to SAP’s documentation, it “*enables you to analyze call sequences within distributed system landscapes*”, letting administrators correlate log traces and error messages and perform end-to-end tracing across integrated SAP and non-SAP systems. Three characteristics of EPP, all documented publicly by SAP, explain why a flaw in its processing is so serious:

- It is created when a new user session is opened. Processing therefore happens at the very start of a connection, before the session is authenticated.
- It is transported by communication protocols such as RFC and HTTP, and is always sent forward from client to server. The data originates with the client, and more than one protocol carries it.
- Between ABAP systems, it is implemented by default, so the affected functionality is active without any configuration by the customer.

OVERPASS is a flaw in the SAP kernel code that processes this structure. A specially-crafted request sent to an affected system can be abused to take control of the receiving process and, from there, run operating system commands on the host.

The reason no password stops this is timing. Because EPP is processed as the session opens, every SAP control that decides who may do what, including user locks, roles, authorization objects and logon policies, is evaluated later than the point where the flaw is reached. None of them is in the attacker’s way.

Reference: [SAP Help Portal, Extended Passport (EPP)](https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/89a03e5e5908448cbe7cce3ddcf214b5.html) and [Using the Extended Passport,](https://help.sap.com/docs/ABAP_PLATFORM_NEW/753088fc00704d0a80e7fbd6803c8adb/888809f4e0c14b9db3be6ceb4b7ccb2a.html) ABAP Platform documentation.

### Multiple Access Vectors: One Flaw, Several Routes

Because EPP processing is shared kernel code, the same defect is reachable through entirely separate parts of the system, over different protocols, and in each case without authentication. Onapsis has confirmed at least three access vectors:

- **The web layer.** The SAP Internet Communication Manager and the SAP Web Dispatcher process an Extended Passport supplied with a web request. This is the HTTP(s)  tier that powers SAP Fiori, the SAP WebGUI, web services and API-based integrations, and the one organizations commonly publish to the Internet to enable public-facing SAP services.
- **The SAP GUI layer.** The SAP Dispatcher, the component of the SAP application server that accepts user connections, processes an Extended Passport supplied over the SAP GUI protocol. Every classic SAP GUI logon goes through it.
- **The RFC layer.** SAP systems exchange an Extended Passport while establishing a Remote Function Call connection, the mechanism SAP systems use to talk to one another and the basis of many third-party and custom integrations.

These are not different vulnerabilities. There are several routes to the same defect, which is why SAP addresses all of them with a single CVE and a single Security Note. It also means no route can be dismissed because another has been handled: a system hardened at the web tier is still reachable over the SAP GUI and RFC layers, and so on for each. Restricting any one protocol can be helpful to narrow exposure, but only the patch closes all of them.

## The Impact of Code Execution on the SAP Host

The affected components run under the operating system account that owns the SAP installation, so code execution under it is equivalent to owning the SAP system outright. An attacker can read the SAP secure store to recover database credentials, password hashes and all housed business data; read the live session data of users logged on at that moment; extract stored credentials to move laterally into every other SAP system that trusts the compromised one; and write freely to application data, system configuration and the SAP binaries themselves. This enables:

- **Sabotage**: deploying ransomware, forcing system shutdowns, corrupting database-level data, and planting persistent backdoors in the SAP kernel.
- **Espionage**: exfiltrating business records, financial data, human resources files, customer master data, and intellectual property.
- **Fraud**: creating privileged users, altering financial records, changing vendor bank account numbers, and processing fraudulent payments.
- **Regulatory risk**: triggering mandatory reportable security incidents for organizations subject to SOX, NIS2, GDPR, HIPAA, or PCI-DSS.

## Affected SAP NetWeaver Products and Components

The affected code is part of the SAP kernel, the foundation underpinning the majority of SAP’s business software, so anything running on that kernel inherits the flaw. The footprint extends across SAP S/4HANA, SAP ERP and the SAP Business Suite (ECC), SAP NetWeaver Application Server ABAP, the SAP Web Dispatcher, SAP BW/4HANA, SAP Enterprise Portal, SAP PI/PO, SAP Solution Manager, and the many other solutions built on the same kernel. For most SAP customers, the correct starting assumption is that at least some systems are in scope until proven otherwise.

### The Internet-Facing Risk

The web tier is, by design, what organizations expose when they make SAP functionality available online. Fiori launchpads, the WebGUI, self-service portals, B2B and B2C applications and machine-to-machine APIs all flow through it, often published to the Internet so that employees, partners and customers can reach SAP from anywhere. A pre-authentication flaw in that tier gives a remote attacker a direct path to high-value production systems without first breaching the network perimeter.

A targeted search using high-fidelity fingerprints identifies more than 10,000 unique Internet-facing IP addresses presenting an SAP web interface reachable from the public Internet, and that figure is conservative. It counts only HTTP-reachable systems and materially undercounts the SAP Web Dispatcher, which proxies its backend and returns no distinguishing SAP banner on its root path, making it structurally hard for Internet-wide scanners to attribute. Exposure is globally distributed, concentrating in the United States, Germany, India and China across both on-premises networks and the major cloud providers.

### The Internal Risk: The Unavoidable SAP GUI Layer

The second route changes the calculation for systems never published online at all. Direct Internet exposure of the SAP Dispatcher is fortunately uncommon, but it is routinely reachable across the internal network because every SAP GUI user needs it. It is habitually permitted through the firewalls placed in front of SAP systems, and it cannot be closed without breaking the end-user logons the business depends on.

Any attacker who already has a foothold on the internal network, whether through a phished workstation, a compromised VPN session or an exposed jump host, is therefore already in position. This is why an SAP application does not need to be Internet-connected for OVERPASS to be a concern: a system with no web presence whatsoever is still exposed through the layer its own users log on to every morning. No architectural change closes this off. Only the patch does.

### Historical Context: Echoes of ICMAD

Security teams will recognize the pattern. OVERPASS mirrors the 2022 ICMAD vulnerabilities, which also resided in shared SAP kernel code and also carried a CVSS score of 10.0. ICMAD demonstrated that critical flaws in shared kernel components have an enormous blast radius, and OVERPASS extends the lesson. The radius here is not confined to the web tier. History also shows attackers can reverse-engineer SAP patches within 72 hours, as with RECON (CVE-2020-6287), and that window keeps shrinking now with AI-assisted tooling. The 2025 mass exploitation of CVE-2025-31324, named by [Mandiant’s 2026 M-Trends](https://onapsis.com/blog/mandiant-m-trends-2026-sap-target/) report as the most exploited vulnerability of the year, showed what happens when a critical pre-authentication SAP flaw is weaponized before defenders can respond. That is the outcome our coordinated disclosure partnership with SAP exists to prevent.

### How to Determine Exposure to OVERPASS

The vulnerable code is in a shared SAP kernel source, so SAP Security Note 3747649 is the authoritative source describing which builds are affected. Check your kernel release and patch level against that note first. Beyond that check, treat a system as in scope if any of the following is true:

- It runs SAP software built on the SAP NetWeaver kernel, which covers the overwhelming majority of SAP customers.
- Its web tier is reachable from the Internet, including Internet-facing Fiori, WebGUI and web service or API endpoints, or it hosts externally published Enterprise Portals, PI/PO systems, or B2B and B2C applications.
- Its SAP Dispatcher is reachable from anything broader than a controlled population of SAP GUI clients, including the general corporate network, partner or extranet segments, or third-party managed networks. In most estates, this is true of every system.
- It is a development, test or sandbox system holding a copy of production data, which are frequently less tightly segmented than the systems they were copied from, or has RFC interfaces to higher-tier systems
- It is an older or decommissioned system still online and listening, even if nobody has logged into it for years.

The three routes have very different exposure profiles. The web route affects the subset of systems published online; the SAP GUI route affects essentially every SAP NetWeaver Application Server ABAP system because that access is open to users by design. An exposure review looking only at Internet-facing systems will substantially understate the affected population, and one scoped to a single SAP component will miss systems entirely. Scope the review by kernel patch level, which is what the Security Note is written against, rather than by which services a system happens to expose.

## OVERPASS Remediation Guide and Prioritization

Applying SAP Security Note 3747649 is the definitive fix and the only measure that fully mitigates the vulnerability. A single kernel patch closes every one of the described access routes. Onapsis recommends the following prioritized actions:

1. **Assess and identify**. Build an accurate exposure inventory covering every SAP system, including forgotten, shadow and non-production systems. Record each one’s kernel release and patch level against SAP Security Note 3747649, and capture which networks can reach each system, because that determines the order of everything below.
2. **Patch Internet-facing systems first**. Begin with any SAP system whose web tier is exposed to the Internet. These are reachable by anyone, which makes them the highest-risk population regardless of how well the rest of the estate is segmented.
3. **Patch internal systems next**, and do not treat them as optional. Because the SAP GUI route is open on every application server by design, the internal population is both larger and more uniformly exposed than the Internet-facing one. These systems are second in sequence, not second in importance.
4. **Reduce reachability** where your architecture allows. Front SAP GUI access with SAProuter or dedicated jump hosts, and keep web access behind a Web Dispatcher. Treat this as hardening that lowers exposure for the next issue, not as a substitute for the patch.
5. **Monitor for exploitation attempts**. Ensure you have visibility into your SAP application layer so that attempts to exploit this vulnerability can be detected and investigated while the rollout is in progress.

SAP has released an FAQ SAP Note [\[3776034\] “FAQ Note for SAP Security Note 3747649](https://me.sap.com/notes/3776034)” with additional information and documented specific workarounds to prevent exploitation over HTTP traffic in note [3756304](https://me.sap.com/notes/3756304).

One point is worth stating plainly: SAP authorizations and Segregation of Duties (SoD) controls will not help. The vulnerable code runs before any authentication step, so locking users, tightening roles, enforcing password policies or restricting transaction access has no effect on this attack path. If you cannot patch promptly because of operational constraints, use compensating controls to actively monitor for exploitation and indicators of compromise until the patch is applied.

## Automating SAP Vulnerability Management and Threat Detection for OVERPASS

The Onapsis Research Labs identifies and responsibly discloses critical vulnerabilities in business-critical applications. This proprietary threat intelligence directly powers the automated [SAP exposure management](https://onapsis.com/solutions/vulnerability-management/) and [threat detection capabilities](https://onapsis.com/solutions/threat-detection-response/) within the Onapsis Platform. As the only SAP-Endorsed application security solution, Onapsis maintains a coordinated disclosure partnership with the SAP Product Security Response Team. This collaboration delivers measurable protection to the global SAP ecosystem, evidenced by:

- The discovery and remediation of over 1,000 zero-day vulnerabilities in SAP business applications.
- The delivery of pre-patch threat intelligence to secure organizations against emerging exploits like OVERPASS.
- Continuous recognition on the official [SAP Security Researcher Acknowledgments page](https://support.sap.com/en/my-support/knowledge-base/security-notes-news/credits-for-security-researchers.html?isu_page=1).

### Protected BEFORE the Patch

Because the Onapsis Research Labs discovered the vulnerabilities, the intelligence and detection content required to protect against them were developed and delivered to customers as part of the coordinated disclosure process, providing Onapsis customers with zero-day coverage prior to the patch being available.

Onapsis Defend was equipped to detect attempts to exploit the issues at the SAP application layer, and the Onapsis Research Labs leveraged its Global Threat Intelligence Network to monitor the global SAP threat landscape for any early signs of malicious activity.

### Supported AFTER the Patch

Once SAP released the Security Note 3747649 for OVERPASS, Onapsis customers moved immediately from awareness to action across the platform:

- [Onapsis Assess](https://onapsis.com/platform/assess/) automatically identifies which SAP systems are affected through actionable SAP threat intelligence feeds, prioritizes the associated SAP Security Note within the broader patch backlog, and validates that the fix has been correctly and completely applied.
- [Onapsis Defend](https://onapsis.com/platform/defend/) provides continuous SAP application-layer monitoring, so that attempts to exploit the OVERPASS vulnerability can be detected and investigated in real time.
- The Onapsis Research Labs continue to track exploitation activity, indicators, and attacker behavior in the wild, feeding updated intelligence back into detection content and Threat Dispatches for customers, so protection keeps pace with the evolving threat.

Together, this coverage turns a high-pressure, all-hands patching event into a guided, measurable process taking customers from zero-day protection before the patch, through prioritized remediation, to ongoing assurance that the fix holds and that exploitation attempts are seen. This is what it means for a security vendor to inform and keep SAP customers well ahead of the threat: robust protection before the patch is released, expert guidance through remediation when a patch is released, and continuous monitoring of the threat long after Patch Tuesday has come and gone to ensure customers remain protected.

## Next Steps for Securing Your SAP Landscape

OVERPASS (CVE-2026-44756) is a maximum-severity, pre-authenticated vulnerability in shared SAP kernel code, reachable both from the Internet-facing web layer, from the SAP GUI layer every end user connects to, and from the RFC layer that links SAP systems to one another.. Its outcome is not disruption but full compromise: arbitrary operating system commands executed as the account that owns the SAP system, and from there the database, the business data and the trust relationships to every connected SAP system.

Apply the SAP Security Note 3747649 now, prioritizing your Internet-facing systems, and [reach out to the Onapsis team](https://onapsis.com/company/contact-us/) if you need assistance in understanding your exposure to accelerate remediation across your SAP landscape.

Existing Onapsis customers are already supported through Assess and Defend. Organizations that are not yet customers can request an SAP Threat Intelligence Briefing with the Onapsis Research Labs to understand their exposure to OVERPASS and other critical risks.

*Onapsis Research Labs reported these vulnerabilities to SAP through coordinated disclosure. In line with that process, technical details that could aid exploitation are intentionally not included in this post.*
