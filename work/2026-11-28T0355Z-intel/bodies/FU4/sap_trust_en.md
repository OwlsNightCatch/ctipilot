---
title: Report a Security Issue | SAP Security Management
url: https://www.sap.com/about/trust-center/security/incident-management.html
hostname: sap.com
description: SAP is committed to identifying and addressing every security issue that affects our software and cloud solutions. Learn how to report a potential security issue.
sitename: SAP
date: "2026-10-21"
tags: ['security incident', 'security vulnerability', 'security risk']
fingerprint: ac120c900cb4634f
language: en
image: http://www.sap.com/dam/application/shared/logos/sap_logo_rgb_onwhite_0300_0300.png.adapt.png/1656382976488.png
pagetype: website
filedate: "2026-11-28"
---
# Security issue management


## Public Statement for CVE-2026-109618 and CVE-2026-109619

As of October 26th, 2026, SAP has no evidence of exploitation due to CVE-2026-109618 and CVE-2026-109619 (critical remote code execution vulnerabilities in PHP's memory-limit handling) across its products and services portfolio. PHP is not a core language in SAP's enterprise technology stack. Based on the analysis conducted to date, PHP involvement has only been identified in the following products and services:

- For SAP BTP, Cloud Foundry Runtime is not affected at the platform level. PHP is available through the community php\_buildpack. A patched version of the buildpack (v5.1.4), containing PHP [versions](https://github.com/cloudfoundry/php-buildpack/releases/tag/v5.1.4) , was released on October 21, 2026. SAP strongly recommends that customers redeploy their PHP Cloud Foundry applications and verify that buildpack version v5.1.4 has been applied.
- SAP BTP, Kyma Runtime is not affected at the platform level. As a Kubernetes-based runtime, SAP does not operate a PHP runtime as part of the platform. Customers running PHP containers are encouraged to update their container images to PHP 8.2.35, 8.3.36, 8.4.27, or 8.5.12, as applicable.
- For on-premise environments, customers operating PHP in these environments are encouraged to review the [official CISA advisory](https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching) and apply the recommended remediation actions, prioritizing internet-facing systems.
- If the SAP Product is not mentioned above, there is no known impact.

SAP remains committed to the security and integrity of its services. For SAP Customers and Partners, please refer to KBA [3841665](https://me.sap.com/notes/3841665/E).

## Report a security issue

SAP is continuously working on improving our security processes. Report a potential security issue using one of the options below.

We secure your business with strong infrastructure protection, continuous 24/7 monitoring, rapid incident response, and built-in disaster recovery. We enforce strict access controls, follow secure development practices, and maintain global certifications such as ISO 27001 and SOC reports. We provide transparency into policies, certifications, and monthly security patches through our Trust Center. While SAP protects the platform, customers manage user access and configuration under a shared responsibility model—working together to keep systems secure.

### SAP customers

Report a customer security issue to find a solution and get real-time support from an expert.

### Non-customers

Security researchers and other non-SAP customers can report any security vulnerability they discover in SAP products (whether on-premises or in the cloud) or on SAP-owned domains (such as the SAP Help Portal) to ensure responsible disclosure.

Security vulnerabilities that are reported will be acknowledged in our SAP Bug Bounty Program hall of fame.

### Disclosure guidelines

Include the following details in the report, as applicable: issue category, affected product version with support package and patch level, necessary pre- and post-conditions for the exploit to work, description with proof of concept or exploit code, and impact of the issue if exploited.

##### Invitation-only SAP Bug Bounty Program

See more information, including list of participating products.

[View SAP Bug Bounty Program](https://bugcrowd.com/engagements/sap-private-invite)

##### Resources for SAP customers and partners

SAP customers and partners with a valid SAP user ID can visit My Trust Center, an area within SAP Support Portal that extends the public offering by granting access to SAP security policies, frameworks, subprocessors lists, and more.

[Login to My Trust Center](https://support.sap.com/en/my-support/trust-center.html)

##### SAP security notes

The SAP for Me portal is the central access point for customers and partners providing detailed information about their product portfolios including a list of all security notes.

[View all SAP security notes](https://me.sap.com/app/securitynotes)

## SAP Security Patch Day

### Fix vulnerabilities discovered in SAP products

Review notes from our monthly SAP Security Patch Day to learn about vulnerabilities discovered in SAP products and patches to protect your SAP landscape.

### Acknowledging our security researchers

Learn about the security researchers who help us identify and solve vulnerabilities so that we can help maintain the safety of our customers and partners.
