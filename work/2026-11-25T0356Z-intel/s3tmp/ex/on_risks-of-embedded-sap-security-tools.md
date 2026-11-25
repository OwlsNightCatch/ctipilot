---
title: "The SAP Security Paradox: Insecure Architectures, Risks and Myths of Third-Party SAP-Embedded Solutions"
author: David D'Aprile
url: https://onapsis.com/blog/risks-of-embedded-sap-security-tools/
hostname: onapsis.com
description: Evaluating your SAP security architecture? Uncover the hidden risks of SAP-embedded add-ons and why standalone solutions offer true cyber resilience.
sitename: Onapsis
date: "2026-11-10"
tags: ["David D'Aprile", 'onapsis platform']
fingerprint: f5108c1607a1ce26
language: en
image: https://onapsis.com/wp-content/uploads/blog-wp.jpg
pagetype: article
filedate: "2026-11-25"
---
## Executive Summary:

*When securing mission-critical SAP environments, third-party SAP-embedded security solutions claiming ease of installation and low footprints can be deceiving. More critically, these tools build and run their security logic inside the SAP application technologies they are supposed to protect, paradoxically exposing themselves to known and zero-day SAP vulnerabilities and introducing critical operational risk. Onapsis’ Next Generation Architecture (NGA) delivers the true, isolated, and resilient protection that is needed in the age of AI, while unlocking record-fast time-to-value (TTV) and low total cost of ownership (TCO).* 

## A Foundational Decision for SAP Security

When it comes to evaluating third-party vendors for SAP security, you have a critical decision to make: what is the right architecture, standalone or SAP-embedded?

Standalone solutions (like the Onapsis Platform) are deployed as a side car to SAP systems, running their security logic “outside” your SAP platform. On the other hand, [SAP-embedded third-party tools](https://onapsis.com/why-onapsis/onapsis-vs-other-sap-security-tools/), commonly developed in ABAP/UI5, run their logic inside one of your productive SAP applications (such as S/4HANA, SAP GRC or Solution Manager), or in a dedicated SAP NetWeaver system.

From a general perspective, each architecture has its own strengths and weaknesses. Compared to standalone products, installing SAP-embedded solutions is a known process for SAP Basis administrators and they have a familiar look-and-feel to the other SAP tools they use every day. However, when considering you would be deploying this product to protect your business-critical SAP systems from damaging cyber attacks, the downsides of SAP-embedded architectures become strikingly clear.

## The Fundamental Flaws of SAP-Embedded Security Solutions: Vulnerable to SAP Attacks By Design & Operational Risks

### Exposed to the Very Threats They Claim to Protect You Against

> “As a CISO and CTO, I’ve designed, developed and operated numerous industry-leading cybersecurity products. The architecture is where everything starts. Designing a security control that is vulnerable to the same threats it’s supposed to protect is a fundamental architectural flaw. Having isolation is a key requirement, even more in the age of AI.”
>
> – **Gerhard Eschelbeck, CISO at Kodiak, former CISO at Google, former CTO at Qualys & Sophos, and more.**

> “As an SAP expert with 30+ years of experience managing mission-critical SAP environments, it’s obvious to me that having an SAP security product running inside your SAP systems and developed in ABAP is a terrible idea. You need as much separation as possible, so your security engine is not affected by SAP vulnerabilities. This is a non-negotiable architectural requirement, that was one of JYSK’s requirements, when choosing a SAP Security solution back in 2019”
>
> – **Frank Folsach Olsen, Senior Technology Architect – SAP Platform at JYSK**

SAP-embedded third party security solutions are developed in ABAP/UI5 and run directly inside the customer’s SAP NetWeaver application stack. Paradoxically, this renders them exposed, by design, to the very same SAP vulnerabilities that they claim to protect you against.

During every monthly [SAP Security Patch Day](https://onapsis.com/blog-category/sap-patch-day/), whenever a new SAP zero-day is exploited in the wild, or the moment an SAP Basis administrator inadvertently changes a security setting to an insecure value or grants high privileges to a system user, the SAP-embedded security tool can become immediately exposed to compromise in tandem with the host SAP system it runs on, rendering it ineffective or worse.

Threat actors, and AI agents, know this. In real-world scenarios, these solutions would be the first target in their kill chain.

### Illustrative Attack Sequence

At best, the compromised security tool is hosted on a dedicated SAP system with no business data. In this scenario, the attack “only” blinds your defenses, which remains a massive problem. At worst, and alarmingly this is the deployment model many SAP-embedded vendors recommend, the tool runs directly inside your S/4HANA or production system. This means a tool compromise instantly exposes your crown-jewel data and core processes.

### Operational & Stability Risks in Production SAP Landscapes

Beyond the inherent insecurity of the architectural design itself, deploying and running third-party code directly into production SAP application servers can also introduce severe operational risk: a flawed software update to the security tool can destabilize production SAP application servers. Just as a kernel-level update failure can crash an operating system, a bad update or performance issue in an embedded SAP security tool that runs complex logic and processing on top of your S/4HANA system has the potential to take down core enterprise processes and halt business operations.

## Debunking the “No Infrastructure” and “Low Footprint” Myths

Several SAP-embedded add-on vendors claim to have a “zero infrastructure footprint”. However, a closer look at their underlying deployment model reveals substantial hidden complexity and maintenance costs that inflate the overall total cost of ownership for an enterprise.

SAP-embedded tools typically require a central “controller” system, used for the security tool’s management functions and hosting its security logic, and a set of “agents”, which are deployed on each target SAP application being monitored.

**The Controller Dilemma**: With SAP-embedded architectures, organizations are forced to choose between two very risky options when deciding how to deploy the controller:

- **Inside an existing SAP system**: Many vendors paradoxically suggest hosting the controller on S/4HANA, SAP GRC, or SAP Solution Manager. As explained previously, this exposes vital business systems to direct compromise, additional internal threat vectors from users in those systems, and risks operational disruption if a security tool update fails.

- **On a dedicated SAP system**: To avoid risking business disruption, organizations must spin up a full, dedicated SAP system solely to run the security controller component. This requires provisioning, licensing, and maintaining *five* separate layers: virtual machine + operating system + database + SAP NetWeaver + controller. This results in an additional, complex infrastructure footprint and incremental licensing costs, completely counter to their “no infrastructure” marketing claims. *Hint: with Onapsis NGA, you have even less layers to manage than this, and no hidden licensing costs.* 

**The Agent Sprawl**: On top of the controller challenges, while many vendors claim to be “agentless”, they in fact require installing, configuring, and maintaining agents (typically in the form of SAP transports/add-ons) in every target SAP system in your landscape. Maintaining individual agents across hundreds of SAP systems is an additional burden of maintenance for teams and increases total cost of ownership.

**The Bottom-Line:** when SAP-embedded vendors say they have “no infrastructure” or “low footprint”, they are in fact only talking about the simplicity of option to deploy the controller inside one of your productive SAP systems (which is truly simple, but also a terrible idea in conflict with basic cybersecurity best practices). If you push back on this architecture, your only option is dedicated infrastructure with an SAP system for it, which not only is still exposed to SAP-attacks but also requires a higher footprint compared to Onapsis NGA (see below).

## The Onapsis Solution: Next Generation Architecture (NGA)

Ultimately, to avoid introducing unnecessary risk into your SAP security programs and productive environments, it’s imperative that your security remains external to the SAP environment. Quite simply, this is a well-known best practice in the cybersecurity industry, adopted by all reputable vendors: the security decision logic of a security product should be, as much as technically possible, outside of the target environments it protects.

The [**Onapsis Platform**](https://onapsis.com/platform/), powered by the new **Next Generation Architecture (NGA)** released in mid-2026, was engineered from the ground up to adhere to these enterprise security standards while still providing unmatched time to value and low total cost of ownership (TCO).

This new platform is delivered as a lightweight virtual machine that can be rapidly deployed as infrastructure-as-code (IaC) across all major cloud providers and on-premises for full data control. Through a highly-optimized internal orchestration framework, the platform can monitor hundreds of SAP systems from a single virtual machine. If needed, customers can deploy connectors in remote locations or segregated networks, providing enterprise-ready, secure scalability for global organizations with distributed SAP environments and high-security requirements.

Compared to the legacy Onapsis architecture, NGA represents a radical reduction in TCO, time to value (TTV), footprint and overhead. Customers using NGA have been able to provision the platform in minutes and experience upwards of 80% footprint reduction and 70%+ cost savings in infrastructure compared to the legacy Onapsis architecture.

When compared to SAP-embedded solutions installed on a dedicated SAP system, the TTV and TCO are also far superior with NGA: SAP-embedded tools force you to license, provision and maintain a dedicated virtual machine, operating system, database, and SAP NetWeaver environment just to run the controller; with NGA, you only need to provision the Onapsis Platform virtual machine image, which is self-contained and automatically updated.

## Side-by-Side Comparison: Onapsis Platform Standalone Next Generation Architecture vs. SAP-Embedded Security Tools

| **Architectural Dimension** | **Onapsis Platform Next Generation Architecture (NGA)** | **Embedded SAP Security Add-On Architecture** | 
|---|---|---|
| Endorsed by SAP | **Yes**. The Onapsis Platform is the only SAP cybersecurity solution [endorsed by SAP](https://onapsis.com/why-onapsis/why-sap-endorses-onapsis/). | **No**. Only basic SAP integration certifications. | 
| Deployment Model | Standalone Unified Virtual Appliance (IaC). | Embedded SAP Add-On / Transport. | 
| Console | All self-contained in a single Unified Appliance for all products (Assess, Defend, Control). | Requires installation on a productive or dedicated SAP system, creating exposure and adding hidden costs and complexity. | 
| Security Console Exposed to SAP Vulnerabilities | **Not Exposed:** Due to its completely decoupled, standalone deployment, Onapsis’ security console is unaffected by SAP NetWeaver, ABAP, or UI5 zero-days or flaws. | **Inherently Exposed:** Susceptible to the exact same SAP flaws and vulnerabilities it claims to protect you from. | 
| Production System Risk | **Low Risk:** Operates externally; risk of crashing or destabilizing production SAP systems is low by design. | **High Risk:** Bad transport updates or code issues can disrupt the host SAP system. | 
| Setup & Administration | **Easy, 15-20 Minute Setup:** Modern IaC architecture with web installer. From bare metal to platform provisioned in 15-20 minutes. The virtual appliance internal layers are automatically updated without requiring separate licensing and maintenance by your teams. | **Easy for Riskiest Model, Harder for Dedicated:** Controller installs easily through an SAP add-on in a productive SAP system (highest-risk model). Dedicated option requires new virtual machine, OS, database and SAP NetWeaver component being provisioned. | 
| Works Out of the Box? | **Yes:** Preconfigured with test cases, modules, policies, and crawl-walk-run rulesets, recommended by the [Onapsis Research Labs](https://onapsis.com/threat-research/onapsis-research-labs/) and designed to accelerate time-to-value for new deployments. | **Requires Tuning:** Add-ons may deploy quickly, but software generally requires significant tuning and noise reduction afterwards. | 
| RISE with SAP Compatible | **Full:** Compatibility across  all products ([Assess](https://onapsis.com/platform/assess/), [Defend](https://onapsis.com/platform/defend/), [Control](https://onapsis.com/platform/control/)), including HANA database security (both Runtime and Enterprise licenses). | **Partial:** Limited capabilities for HANA assessments and no HANA security monitoring / threat detection capabilities. | 

## Conclusion: Architectural Isolation for SAP Security is Simply Non-Negotiable

When safeguarding your organization’s financial records, supply chain logic, and crown-jewel SAP data, choosing the right architecture for your SAP security solution really matters.

SAP-embedded add-on tools offer surface-level convenience for SAP Basis administrators at the expense of fundamental security principles, leaving your SAP security layer vulnerable to SAP exploits and increasing operational disruption risk. Furthermore, despite claims of “no infrastructure” or “low footprint”, the reality is very different in real-world implementations and when compared against the modern Onapsis Platform architecture.

With **Onapsis Next Generation Architecture (NGA)**, enterprise organizations achieve true domain separation and resiliency, and full alignment with cybersecurity best practices, all delivered through a lightweight virtual appliance that reduces infrastructure TCO and delivers lightning-fast time to value (TTV).

## Frequently Asked Questions

### What is the key difference between embedded SAP add-on security and a standalone architecture?

An embedded add-on runs natively inside the SAP application stack, sharing the SAP system’s runtime environment. Because it’s developed in ABAP/UI5 and runs inside SAP systems, it is completely susceptible to any SAP vulnerability affecting its host SAP system, including critical vulnerabilities such as [OVERPASS](https://onapsis.com/blog/sap-overpass-remediation/), [ICMAD](https://onapsis.com/threat-research/icmad/), new SAP zero-days, and privileged SAP system users.

In contrast, a standalone architecture like Onapsis Next Generation Architecture (NGA) operates in an isolated, hardened environment outside the SAP stack, maintaining strict domain separation and remaining unaffected by underlying SAP vulnerabilities.

### Does an SAP-embedded tool eliminate infrastructure costs? They claim they “do not require external infrastructure” to run, is this true?

The short answer is no, if you care about security. SAP-embedded tools force you to choose between two bad options: either you host the controller on one of your existing SAP systems, which saves you one virtual machine but introduces significant vulnerability and operational risk, or you deploy it on a dedicated SAP system, which not only requires a virtual machine, but also an operating system, a database, an SAP NetWeaver installation, and the tool itself – all of which you need to license maintain yourself. This is completely counter to their claims of “not requiring external infrastructure”.

In both cases, Onapsis NGA is both more secure and requires a lighter footprint, with no hidden licensing and maintenance costs.

### I had heard from an SAP-embedded vendor that Onapsis has a “heavy footprint” and “high TCO”. Is that true?

It used to, but not anymore. While the Onapsis Platform has always had a more secure architecture than SAP-embedded alternatives, its legacy architecture required a console and sensor virtual machines that increased with the number of SAP systems in a customer environment. For organizations with hundreds of systems, this in fact resulted in an increased operational footprint and complexity in the past.

Now, through the new NGA architecture released mid 2026, Onapsis eliminated the need for sensor virtual machines (and even agents in the target systems), and optimized the base platform through a highly-efficient containerized platform and infrastructure-as-code (IaC) deployment. Compared to the legacy Onapsis architecture, NGA represents a radical reduction in TCO, Time-to-Value, footprint and overhead.This provides customers with the most secure *and* lightest architecture for SAP security in the market.

Customers using NGA have been able to provision the platform in hours and experience upwards of 80% footprint reduction and 70%+ cost savings in infrastructure compared to the legacy Onapsis architecture.

### Why isn’t Onapsis vulnerable to SAP attacks?

SAP-embedded solutions running inside SAP systems are inherently exposed to SAP vulnerabilities, as well as to attacks from privileged users of the host SAP environment they run on. The Onapsis Platform console is not developed in ABAP/UI5, and does not run inside an SAP system, limiting its exposure to SAP-based attacks.

While advanced threat actors could potentially compromise the target SAP systems and manipulate the API functions that are used by Onapsis to extract security-relevant data, impairing or manipulating the results visible to the platform, this is a threat scenario that also affects SAP-embedded architectures. Onapsis has implemented several measures in its architecture to limit the potential impact of these scenarios.

Every security product may itself become vulnerable to zero-days or novel exploitation techniques. However, the paradox of SAP-embedded tools is that they are affected *by the very same SAP vulnerabilities they are designed to prevent/detect. Attackers don’t need to find a separate attack; they just use the same SAP vulnerability in sequence*.

### How can I trust that the Onapsis Platform NGA virtual appliance is secure? I’ve heard SAP-embedded vendors claim that this would “expand the attack surface”?

Onapsis was founded by cybersecurity professionals and has invested from day one in industry-leading secure development lifecycle practices and cybersecurity controls. Our solution architecture follows the same principles used by the world’s leading cybersecurity providers, which separate the security logic, as much as technically possible, from the assets they protect.

Conceptually, any new component introduced in an environment expands the attack surface. This is exactly the same case (and worse) with SAP-embedded vendors that run on dedicated SAP systems, as they require more infrastructure than Onapsis and they shift all its management to customers.

Onapsis takes security very seriously, and can back this claim with proof of significantly higher third-party validation than any other SAP security vendor in the market. We’re proud to be certified for SOC 1/SOC 2 Type II, ISO/IEC 27001:2022 (ISMS), ISO 20243:2018 (O-TTPS), TISAX Level 3 (AL3), and more, and to be the only SAP cybersecurity solution endorsed by SAP. Learn more about how we operate securely in our [Trust Center](https://onapsis.com/trust-center/).
