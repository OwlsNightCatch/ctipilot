---
title: "1Password Breach Exposes Customer Data, Internal Source Code"
author: Eduard Kovacs
url: https://www.securityweek.com/1password-breach-exposes-customer-data-internal-source-code/
hostname: securityweek.com
description: A hacker used a compromised employee GitHub account to push malicious code and steal customer records, but vaults were not accessed.
sitename: SecurityWeek
date: "2026-11-26"
categories: ['Data Breaches']
tags: ['1Password', 'data breach', 'Featured', 'source code']
fingerprint: bf29f09312223c45
language: en
image: https://www.securityweek.com/wp-content/uploads/2026/11/1password.jpeg
pagetype: article
filedate: "2026-11-28"
---
**Password management and identity security company 1Password revealed on Wednesday that a hacker stole customer information and proprietary source code. 1Password says customer vaults are not affected.**

The company launched an investigation on November 19 after discovering that an employee’s corporate GitHub account may have been compromised.

The attacker used the account to deploy malicious code to backend services and exfiltrate customer records. The compromised customer records include names, email addresses, account identifiers, public cryptographic keys, authentication parameters, account activity times, and non-secret metadata.

In addition, the threat actor obtained source code from private repositories and accessed the company’s CI/CD system, potentially exposing infrastructure credentials.

[According to 1Password](https://1password.com/blog/update-on-nov-2026-security-incident), the hacker also obtained tokens from emails sent to users for account invitations, provisioning, and recovery.

A “small number” of individuals who were undergoing provisioning or recovery during the intrusion have been notified. However, the company noted that the exposed tokens cannot be exploited on their own and there is no evidence that the attacker hijacked user accounts.

A 1Password representative noted on the company’s [community forum](https://www.1password.community/announcements-52/update-on-a-security-incident-involving-1password-s-backend-systems-customer-vaults-were-not-affected-and-all-vault-contents-remain-secure-26259) that the stolen authentication data included Secure Remote Password verifiers derived from user account passwords and Secret Keys. The verifiers cannot be used directly for authentication, and brute-forcing account passwords would require the associated Secret Keys, which 1Password does not store.

1Password highlighted that customer vaults and the cryptographic keys protecting them were not compromised. “We have no evidence that encrypted vaults were downloaded or accessed,” a 1Password community manager said.

The breach also does not impact client applications, browser extensions, and account recovery keys.

It’s unclear how many users are affected and how the hacker gained initial access to the corporate GitHub account.

In response to the intrusion, 1Password disabled the compromised GitHub account, invalidated a stolen token, replaced potentially compromised infrastructure credentials, and restored clean versions of affected services.

The company said its investigation, conducted with independent cybersecurity experts, is still ongoing. Customers do not need to take any action, but have been advised to watch for phishing attacks that could exploit news of the incident.

**Related**: [European Commission Uncovers Data Breach in Cyberattack Investigation](https://www.securityweek.com/european-commission-uncovers-data-breach-in-cyberattack-investigation/)

**Related**: [AI Inference Providers Failed to Detect Hacking and Prompt Theft, Says Dragos](https://www.securityweek.com/ai-inference-providers-failed-to-detect-hacking-and-prompt-theft-says-dragos/)

**Related**: [1.5 Million Impacted by Data Breach at South Korean Electric Company KEPCO](https://www.securityweek.com/1-5-million-impacted-by-data-breach-at-south-korean-electric-company-kepco/)
