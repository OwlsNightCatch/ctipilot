---
title: Mitel MiCollab Zero-Day Vulnerability Let Attackers Bypass Authentication
author: Tushar Subhra Dutta
url: https://cybersecuritynews.com/mitel-micollab-zero-day-vulnerability/
hostname: cybersecuritynews.com
description: Security researchers have uncovered a critical zero-day vulnerability in Mitel MiCollab, a popular unified communications solution.
sitename: Cyber Security News
date: "2024-12-05"
categories: ['Cyber Security News']
fingerprint: "8c135d55eb175bdf"
---
Security researchers have uncovered a critical zero-day vulnerability in Mitel MiCollab, a popular unified communications solution.

The flaw, which remains unpatched, allows attackers to perform arbitrary file reads on the server’s filesystem, potentially compromising sensitive information and system security.

The zero-day vulnerability, discovered by researchers at watchTowr, affects the ‘ReconcileWizard’ servlet in MiCollab.

By exploiting this flaw, attackers can [bypass authentication](https://cybersecuritynews.com/sap-hackers-bypass-authentication/) and access sensitive system files, such as ‘/etc/ passwd’, which contains crucial information about user accounts.

Cybersecurity analysts at watchtower Labs [discovered](https://labs.watchtowr.com/where-theres-smoke-theres-fire-mitel-micollab-cve-2024-35286-cve-2024-41713-and-an-0day/) that this vulnerability is particularly alarming as it doesn’t require authentication to exploit, significantly increasing the risk to organizations using affected versions of MiCollab.

The researchers reported the issue to Mitel on August 26, 2024, but as of December 5, 2024, no patch has been released.

**Free Webinar on Best Practices for API vulnerability & Penetration Testing:  [Free Registration](https://webinars.indusface.com/72-hours-to-audit-ready-api-security-a-proven-framework/register?utm_source=gbhackers-side-banner&utm_campaign=2024-dec-webinar-api-security&utm_medium=referral)**

## **Technical Analysis**

While the newly discovered zero-day doesn’t yet have a CVE identifier, it follows two recently patched vulnerabilities in MiCollab:

1. CVE-2024-35286: An SQL injection flaw fixed on May 23, 2024
2. CVE-2024-41713: An authentication bypass issue addressed on October 9, 2024

The latter, CVE-2024-41713, carries a critical CVSS score of 9.8, highlighting the severe nature of security issues affecting the platform.

As Mitel has not yet released a patch for the [zero-day vulnerability](https://cybersecuritynews.com/tp-link-archer-zero-day-vulnerability/), organizations using MiCollab are advised to implement immediate mitigations:

- Restrict access to the MiCollab server to trusted IP ranges or internal networks
- Implement firewall rules to prevent unauthorized external access
- Monitor logs for suspicious activity targeting the ReconcileWizard servlet
- Watch for unexpected access to sensitive files or configuration data
- If possible, disable or restrict access to the ReconcileWizard servlet

This incident underscores the ongoing security challenges faced by enterprise collaboration platforms. It also highlights the importance of prompt vulnerability disclosure and patching by vendors.

Mitel has stated plans to patch the [vulnerability](https://cybersecuritynews.com/category/vulnerability/) in the first week of December 2024. However, until a fix is released and applied, MiCollab users remain at risk.

**Update: 19/12/2024:** The vulnerability listed as “critical” (CVE-2024-41713) has been patched. The file read exposure referenced in the article carries a “low” severity level and is substantially mitigated by MiCollab 9.8 SP2 (9.8.2.12).

“Our top priority is to ensure the reliability and security of the solutions we offer our customers. We recently became aware of vulnerabilities relating to MiCollab and have published recommended actions, including software updates, to mitigate risks. We strongly encourage customers to apply all available security updates as they become available.” Mitel reached out to Cyber Security News.

Organizations are strongly encouraged to implement the recommended mitigations and stay vigilant for any signs of exploitation attempts.

`Analyse Real-World Malware & Phishing Attacks With ANY.RUN -` [Get up to 3 Free Licenses](https://app.any.run/plans?utm_source=csn&utm_medium=article&utm_campaign=phishing_attacks&utm_content=plans&utm_term=051224)
