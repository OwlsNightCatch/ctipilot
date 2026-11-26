---
title: "1Password customer data stolen after employee GitHub account breach"
author: Lawrence Abrams
url: https://www.bleepingcomputer.com/news/security/1password-customer-data-stolen-after-employee-github-account-breach/
hostname: bleepingcomputer.com
description: "1Password has disclosed a data breach after a an employee's corporate GitHub account was hacked and used to deploy malicious code to the company's backend services to steal customer data."
sitename: BleepingComputer
date: "2026-11-25"
tags: ['computers', 'windows', 'linux', 'mac', 'support', 'tech support', 'spyware', 'malware', 'virus', 'security', '1Password', 'Data Breach', 'GitHub', 'Password Manager', 'Security Breach', 'virus removal', 'malware removal', 'computer help', 'technical support']
fingerprint: bf3dd89b10737445
language: en
image: https://www.bleepstatic.com/content/hl-images/2023/10/23/1Password_binary.jpg
pagetype: article
filedate: "2026-11-26"
---
1Password has disclosed a data breach after an employee's corporate GitHub account was hacked and used to deploy malicious code to the company's backend services to steal customer data.

The company says customer password vaults and the encryption keys protecting them were not compromised in the attack.

In a [security incident disclosure](https://1password.com/blog/update-on-nov-2026-security-incident) published today, 1Password says it began investigating the breach on November 19 after detecting indications that an employee's GitHub account had been compromised.

The attacker used the account to access private source code repositories and inject malicious code into backend services that downloaded customer account records.

The stolen data includes:

- Customer names and email addresses
- Account and user IDs
- Account creation and last sign-in timestamps
- Public cryptographic keys
- Secure Remote Password (SRP) protocol parameters
- Invitation, provisioning, and account recovery tokens
- Other internal account metadata

The attacker also stole internal company source code and accessed its continuous integration and continuous delivery (CI/CD) environment, potentially exposing internal infrastructure credentials.

Among the stolen customer data were tokens embedded in links that 1Password emailed to users to accept account provisioning invitations or recover their accounts.

However, 1Password says these tokens cannot be used on their own to access customer accounts, as completing the invitation or recovery process requires either single sign-on (SSO) authentication or a six-digit verification code sent to the user's registered email address.

The company says only a small number of users were affected and have been individually notified.

As a precaution against brute-force attacks, 1Password has strengthened these verification codes from six numeric digits to ten alphanumeric characters.

The company says it has now disabled the compromised GitHub account, revoked the stolen token, restored clean versions of affected services, and rotated or revoked potentially exposed infrastructure credentials.

1Password has also hired independent cybersecurity experts to validate its remediation efforts and says it has found no internal evidence of customer account takeovers.

The company is not requiring customers to change their account passwords or Secret Keys but warns them to watch for unexpected invitations, account recovery requests, and other potential phishing attempts.

While customer vaults were not compromised in the attack, the stolen data is valuable to threat actors as it provides a list of known 1Password users who could be targeted in phishing campaigns.

Threat actors could send emails impersonating 1Password, using the breach as a lure to trick customers into disclosing their account passwords, Secret Keys, or recovery verification codes.

Customers should be particularly wary of emails claiming they need to secure their accounts in response to the breach, reset their passwords, or verify their account information.

Rather than clicking on links in these emails, customers should access their accounts directly through the 1Password website or app and never share their passwords, Secret Keys, or verification codes with anyone.

BleepingComputer contacted 1Password with questions about the attack but has not yet received a response.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
