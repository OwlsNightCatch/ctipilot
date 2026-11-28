---
title: "Sandboxing AI Coding Agents: nono vs Docker Sandboxes vs Microsandbox vs OpenShell"
url: https://kudelskisecurity.com/research/the-rise-of-offensive-ai-frameworks-when-business-logic-becomes-the-attack-surface
hostname: kudelskisecurity.com
description: Nov 27, 2026 - Kudelski Security Team -
sitename: kudelskisecurity.com
date: "2026-11-27"
fingerprint: "1113c2d862bfd6cd"
language: en
filedate: "2026-11-28"
---
# The Rise of Offensive AI Frameworks: When Business Logic Becomes the Attack Surface

[Find out more](https://kudelskisecurity.com/team-members/kudelski-security-team)

*From the BabidiGhost campaign to a real-world Kudelski Security Incident Response investigation: understanding the industrialization of AI-driven cyberattacks.*

**Kudelski Counter Adversary Unit| Incident Response, Artificial Intelligence**

## Executive Summary

Artificial intelligence is transforming the offensive cybersecurity landscape. Beyond assisting threat actors with phishing, reconnaissance and malicious code generation, AI is increasingly being integrated into offensive frameworks capable of orchestrating complex cyber operations with varying degrees of human supervision.

The emergence of **Offensive AI Frameworks** marks a significant evolution in adversarial capabilities. By combining Large Language Models (LLMs), automated security tools and agentic decision-making, these frameworks enable attackers to explore attack surfaces, interpret application behavior, identify weaknesses and coordinate exploitation at machine speed.

The recently documented **BabidiGhost campaign** illustrates how these capabilities are already being weaponized against European organizations.

A recent investigation conducted by the Kudelski Security Incident Response team provides further evidence of this emerging threat.

In a single night, an attacker targeting a European insurance company:

- Generated approximately three million requests in less than nine hours.
- Identified approximately 30 legitimate customer identities.
- Fraudulently created more than a dozen customer accounts.
- Compromised identity verification and authentication workflows.
- Extracted more than one hundred documents containing sensitive customer information.

No malware was identified, and no compromise of the servers hosting the individual customer portal was observed.

Instead, the attacker exploited weaknesses in application architecture, identity management and business logic.

Based on the correlation of indicators of compromise (IoCs), attack patterns and adversarial behavior with previously documented offensive AI activity, **Kudelski Security assesses with high confidence that an offensive AI framework was leveraged during this intrusion.**

Our investigation highlights a particularly concerning development: the application of AI-powered offensive capabilities to the security assumptions embedded within legitimate business processes.

AI does not need to invent new vulnerabilities to transform the threat landscape. It changes the speed, scale and economics at which existing weaknesses can be discovered, combined and exploited.

## 1. The Emergence of Offensive AI Frameworks

The use of artificial intelligence by threat actors has evolved significantly. Initial applications of generative AI in cybercrime primarily focused on supporting individual tasks, including phishing content generation, malicious script development and technical research.

However, the emergence of agentic AI introduces a different operational model. Rather than relying exclusively on human operators to analyze results and determine subsequent actions, offensive AI frameworks can integrate multiple capabilities within a coordinated environment.

These capabilities include:

- Automated reconnaissance and attack surface discovery.
- Contextual analysis of application behavior.
- Interpretation of technical documentation.
- Identification of security weaknesses.
- Dynamic generation and adaptation of offensive tooling.
- Evaluation of exploitation outcomes.
- Exploration of alternative attack paths.
- Automated data collection.

The fundamental difference is the integration of reasoning and execution within the same operational workflow. Conventional automation typically follows predefined instructions. Agentic offensive frameworks can evaluate the results of previous actions and adapt subsequent activities accordingly.

### From traditional automation to agentic offensive operations

These frameworks are not inherently malicious. Many are developed to support legitimate penetration testing, security research and adversarial simulation. However, their weaponization by threat actors introduces additional challenges for defenders.

### Three dimensions of offensive AI

**Acceleration:** AI-powered tooling can reduce the time between reconnaissance, vulnerability identification and exploitation.

**Democratization:** Operators with limited technical expertise can access offensive capabilities that previously required substantial specialist knowledge.

**Industrialization:** Agentic frameworks can potentially sustain multiple offensive activities simultaneously, reducing the marginal cost of investigating additional targets and attack paths.

Organizations are therefore not necessarily facing entirely new exploitation techniques. They are facing adversaries capable of applying familiar techniques with greater persistence, adaptability and operational efficiency.

## 2. BabidiGhost: Offensive AI in Action

SOCRadar's investigation into **BabidiGhost** describes a French-speaking operator using an AI agent to target European organizations. Evidence recovered from the operator's exposed infrastructure provided visibility into AI-driven offensive activity.

### BabidiGhost campaign at a glance

*Source: SOCRadar Research, November 2026.*

The campaign affected sectors including banking, insurance, payments and public administration. The operator relied heavily on natural-language instructions, delegating technical activities to the AI agent.

Successful intrusions exploited known vulnerabilities, exposed credentials and inadequate access controls. No zero-day exploitation was reported.

### Why BabidiGhost matters

The campaign demonstrates that offensive capability can become partially independent of operator expertise. Historically, the complexity of an intrusion could provide some indication of an adversary's technical capabilities. With offensive AI, that relationship becomes less reliable.

A technically sophisticated attack no longer necessarily implies a technically sophisticated human operator. Threat assessments based exclusively on an operator's historical sophistication may underestimate what that operator can achieve through AI-powered tooling.

## 3. Kudelski Security Incident Response Team: An Offensive AI-Driven Attack Against a European Insurer

### Logic, not malware

Kudelski Security's Incident Response team recently investigated an attack targeting a European insurance company.

In a single night, an attacker created more than a dozen accounts in the names of legitimate customers without possessing their original passwords. The attacker subsequently accessed sensitive personal information, financial details and customer documents.

Our investigation relied on perimeter, application and identity-provider logs, complemented by endpoint threat hunting and threat intelligence correlation.

No evidence of malware deployment or compromise of the servers hosting the individual customer portal was identified. Instead, the attacker leveraged weaknesses within the organization's existing application and identity-management processes.

### The attack in numbers

The volume, diversity and execution speed of the observed activity establish that substantial portions of the attack were automated. However, the most significant finding was not simply the scale of the operation. It was the depth of the attacker's interaction with application-specific functionality and the exploitation of relationships between multiple business processes.

### High-confidence assessment of offensive AI involvement

During the investigation, Kudelski Security identified indicators and behavioral characteristics consistent with previously documented offensive AI framework activity.

Our assessment was based on the convergence of multiple evidence categories:

- Correlated indicators of compromise.
- Infrastructure characteristics.
- Previously documented attack patterns.
- Machine-speed execution.
- Application-specific reconnaissance.
- Automated interaction with complex identity workflows.
- Exploration of multiple security boundaries.
- Chaining of application and identity-management weaknesses.

The assessment is not based exclusively on the speed or volume of requests. Conventional automation can also generate significant attack traffic.

Rather, the combination of technical indicators and adversarial behavior supports our **high-confidence assessment that an offensive AI framework was used during the intrusion.**

The identity of the specific framework and its associated indicators are not disclosed in this publication. The degree of human supervision throughout the operation could not be established.

## 4. When Business Logic Becomes the Attack Surface

Traditional offensive security assessments predominantly focus on identifying known vulnerabilities, insecure configurations and technical implementation flaws.

Business logic vulnerabilities introduce a different challenge. They arise when legitimate application functionality, intended business processes and security assumptions interact in ways that produce unintended outcomes.

The compromise did not result from a single weakness. It resulted from a combination of deficiencies across application lifecycle management, identity verification, customer onboarding and authentication.

### Why traditional vulnerability scanners would have missed much of the attack

Conventional vulnerability scanners are effective at detecting known software vulnerabilities and certain categories of insecure configuration. They are generally less effective at identifying inconsistencies in the trust relationships connecting multiple business processes.

Understanding whether an identity verification requirement is preserved across onboarding, migration and account recovery requires contextual analysis of the application.

This is where offensive AI frameworks introduce a potentially significant change. By combining application analysis with automated execution, these frameworks may reduce the effort required to investigate complex workflows and identify inconsistencies in security enforcement.

An additional identity-provider vulnerability, identified as `GHSA-qqv8-37gw-ww2q`, contributed to the compromise. However, this technical vulnerability was only one component of a broader chain of weaknesses. The business logic deficiencies had already undermined the integrity of the customer identity lifecycle.

The attack surface is no longer limited to vulnerable software. It includes the trust assumptions embedded in every business process.

## 5. Correlating the Kudelski Security Incident Response Team Investigation with BabidiGhost

The BabidiGhost campaign and the incident investigated by Kudelski Security provide complementary perspectives on the operational use of offensive AI frameworks.

The correlation is particularly relevant because both investigations involve European organizations, sensitive customer information and adversaries exploiting existing security weaknesses through highly automated offensive operations.

However, the targeting and exploitation approaches differ. BabidiGhost demonstrated the ability of an AI agent to conduct offensive operations across multiple organizations. Our investigation demonstrates the intensive exploration of a single organization's interconnected application and identity ecosystem.

### Comparative threat analysis

### Horizontal versus vertical offensive scalability

**Horizontal scalability**, demonstrated by BabidiGhost, refers to the ability to investigate and attack numerous organizations within a compressed timeframe.

**Vertical scalability**, demonstrated by our investigation, refers to the ability to extensively investigate the interconnected applications, APIs, identity systems and business processes of an individual organization.

Both approaches benefit from persistent automated execution and reduced dependence on manual investigation. Their convergence creates a threat landscape in which organizations may face both increased attack frequency and deeper exploration of their business-critical processes.

### Shared operational characteristics

#### Machine-speed execution

Both investigations demonstrate that significant offensive activity can be conducted within compressed operational timelines. This reduces the time available for security teams to identify suspicious behavior and contain malicious activity.

#### Existing weaknesses as the primary opportunity

Neither case requires an entirely new category of vulnerability to explain its outcome. Familiar security weaknesses, incomplete access controls and insufficient validation remain significant sources of exposure.

#### Reduced dependence on manual investigation

Offensive AI frameworks can reduce the amount of manual technical analysis required throughout an operation. This potentially allows attackers to dedicate more resources to pursuing objectives rather than performing repetitive technical tasks.

#### Persistent exploration of alternative attack paths

The observed activities extended beyond isolated vulnerability exploitation. They included reconnaissance, repeated security testing and investigation of multiple application or infrastructure components.

#### Sensitive data as an operational outcome

Both investigations resulted in the compromise of sensitive information. For organizations operating in regulated industries, particularly insurance and financial services, this creates exposure extending beyond technical remediation to privacy, regulatory, operational and reputational risks.

## 6. The Industrialization of Offensive Cyber Operations

The most consequential impact of offensive AI may not be the creation of entirely new attack techniques. It may be the reduction in the cost of discovering and exploiting existing weaknesses.

Historically, offensive operations have been constrained by:

- The availability of skilled operators.
- The time required to understand unfamiliar technologies.
- The complexity of developing and maintaining offensive tooling.
- The effort associated with manual reconnaissance.
- The cost of investigating unsuccessful attack paths.
- The operational resources required to sustain multiple attacks.

Offensive AI frameworks can reduce several of these constraints. This changes the economic feasibility of attacking complex enterprise environments.

A weakness that previously required hours or days of manual investigation may become more attractive when portions of the investigative process can be delegated to an AI agent.

An adversary can potentially investigate more targets, explore more application functionality and sustain more unsuccessful attempts before identifying an exploitable weakness.

### The changing economics of offensive security

This creates a growing asymmetry between attackers and defenders. Organizations must maintain consistent security across interconnected components and business processes. Attackers need to identify only a sufficiently exploitable combination of weaknesses. Offensive AI may substantially reduce the cost of searching for that combination.

### The emergence of machine-speed adversarial pressure

In our investigation, the attacker generated approximately three million identification requests within a single night.

The relevant question for defenders is not simply whether their existing security controls can withstand an individual malicious request. It is whether those controls can withstand persistent, distributed and context-sensitive adversarial activity across multiple application components.

Security weaknesses that previously remained undiscovered because of the time and effort required to investigate them may become increasingly exposed.

## 7. What Held: Security Fundamentals Still Matter

An important finding from both the BabidiGhost campaign and our investigation is that offensive AI does not make established security controls obsolete.

### Network perimeter

Direct attempts to access protected application infrastructure were unsuccessful. Network security controls prevented the attacker from establishing meaningful access to the underlying systems.

### Server-side authorization

Attempts to access information belonging to other customer accounts were unsuccessful. The compromised accounts could retrieve only information associated with their respective customer identities.

### Administrative protections

Attempts to obtain privileged administrative access were unsuccessful.

### Application security

Conventional injection attempts did not produce successful exploitation.

The BabidiGhost investigation identified a comparable pattern: effective security controls prevented several attempted intrusions.

The attacker succeeded where security assumptions were not consistently enforced across business processes. It failed where security controls were effectively implemented.

**Offensive AI increases the pressure on security controls. It does not invalidate them.**

## 8. Detection Engineering in the Age of Offensive AI

Detecting offensive AI activity exclusively through framework-specific indicators is unlikely to provide sufficient long-term coverage. Threat actors can modify infrastructure, adopt alternative frameworks and change their execution methods.

Detection engineering should therefore combine threat intelligence with behavioral analytics across application and identity telemetry.

### Recommended detection opportunities

### From technical detection to business-aware detection

An individual application request may appear legitimate. A newly created account may satisfy the application's registration requirements. An authentication session may contain technically valid credentials. However, the sequence of events leading to these outcomes may reveal malicious activity.

Security Operations Centers should increasingly correlate telemetry across:

- Web application firewalls.
- API gateways.
- Application services.
- Identity providers.
- Customer onboarding platforms.
- Account recovery mechanisms.
- Document management systems.

The absence of malware should never be interpreted as evidence that no compromise occurred. In our investigation, application and identity telemetry provided significantly more relevant evidence of the attack than traditional endpoint indicators.

### Behavioral intelligence over framework identification

Framework-specific IoCs remain valuable for threat hunting and investigation. However, their greatest value emerges when correlated with abnormal application behavior and contextual evidence.

The objective is not simply to identify which offensive AI framework an attacker is using. It is to detect the offensive behavior enabled by these frameworks, regardless of their implementation.

### Rethinking detection and response timelines

The observed attack had generated multiple detectable signals well before the data collection phase. These included abnormal application request volumes, extensive authentication failures and suspicious reconnaissance activity. Yet the attack progressed throughout the night.

As offensive operations accelerate, organizations should reassess whether their existing monitoring and response capabilities can interrupt malicious activity before it reaches its operational objective.

The relevant metric is not simply mean time to detect or mean time to respond in isolation. It is whether the combined detection and containment timeline remains shorter than the attacker's time to impact.

## 9. Preparing Organizations for Offensive AI-Driven Threats

### Expand offensive security assessments to business logic

Extend penetration testing and red-team exercises beyond infrastructure vulnerabilities and known CVEs. Assess complete business processes, including identity verification, customer registration, authentication, account recovery and access to sensitive information.

### Adopt continuous adversarial security validation

Periodically reassess critical applications and identity workflows against evolving attacker capabilities. AI-assisted security testing can also help defensive teams identify weaknesses before malicious actors discover them.

### Secure the entire API lifecycle

Maintain an accurate inventory of internet-facing functionality. Ensure that retiring a front-end application includes reviewing and appropriately decommissioning its supporting APIs.

### Validate security control effectiveness

Regularly test whether configured security controls are operational. Particular attention should be given to rate limiting, CAPTCHA, authentication requirements and server-side validation following application or infrastructure changes. A configured security control is not necessarily an effective security control.

### Strengthen identity assurance

Ensure that identity verification requirements remain consistent throughout account creation, migration, authentication and recovery. User-controlled information must never automatically inherit verified status. Authentication tokens must be validated against their signature, issuer, audience and expiration.

### Treat identity migration as a critical attack surface

Identity migrations must preserve existing account activation states and security guarantees. Organizations should specifically assess the security implications of legacy identity platforms interacting with modern identity providers.

### Remediate vulnerable identity infrastructure

Organizations should maintain supported and updated identity-provider software. Where authentication compromise is suspected, remediation should include the investigation and removal of unauthorized authenticators, sessions and tokens. The effectiveness of remediation should be verified against identity-provider records.

### Reduce containment timelines

Machine-speed attacks require organizations to reassess how quickly malicious activity can be detected, investigated and contained. Automated containment mechanisms, supported by appropriate safeguards and human oversight, can help reduce the opportunity for attackers to achieve their objectives.

### Integrate offensive AI intelligence into defensive operations

Threat intelligence concerning offensive AI frameworks should inform threat hunting, detection engineering, incident response and continuous security validation. Organizations should prepare for the operational characteristics of offensive AI rather than concentrating exclusively on individual tools.

## 10. Conclusion: The Threat Is No Longer Theoretical

The BabidiGhost campaign and the incident investigated by Kudelski Security demonstrate that offensive AI is transitioning from an emerging capability into an operational cyber threat.

The significance of this evolution extends beyond the automation of traditional exploitation techniques. Offensive AI frameworks are changing the accessibility, speed and scalability of cyber operations. They can support threat actors in investigating unfamiliar environments, exploring alternative attack paths and exploiting complex relationships between application components.

Our investigation highlights a particularly important dimension of this emerging threat: the exploitation of business logic and identity-management workflows.

The attacker did not need to deploy malware or compromise underlying application servers. Instead, the attack targeted the organization's own processes and the security assumptions connecting them.

The BabidiGhost campaign illustrates the democratization of offensive capabilities across operators. Our investigation illustrates how offensive automation can be directed toward a specific organization and its business-critical workflows.

Together, these findings illustrate the industrialization of offensive cybersecurity.

For defenders, the challenge is not simply to identify and block AI-powered tools. It is to ensure that applications, identities and business processes remain resilient when subjected to persistent, adaptive and highly automated adversarial activity.

Traditional security fundamentals remain essential. Their consistent enforcement and continuous validation are becoming increasingly critical.

**The emerging threat is not just an attacker using AI to exploit a vulnerability. It is an attacker using AI to understand how an organization operates, identify where its security assumptions fail and exploit those failures at machine speed.**

## References

- SOCRadar Research — [BabidiGhost: An AI-Augmented Cybercrime Operation](https://socradar.io/blog/babidighost-ai-augmented-cybercrime/), November 2026.

*Categories: Incident Response, Threat Intelligence, Artificial Intelligence*

*Tags: Offensive AI Frameworks, Agentic AI, BabidiGhost, AI-Driven Cyberattacks, Business Logic Exploitation, Identity Security, Incident Response, Cyber Threat Intelligence*
