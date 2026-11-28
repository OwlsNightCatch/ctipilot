---
title: Attacker obtains 1Password customer data via hijacked GitHub account
author: Michaël Aussems
url: https://itdaily.com/news/security/github-account-hijacked-1password/
hostname: itdaily.com
description: An attacker hijacked the GitHub account of a 1Password employee and obtained account data. The vaults remained out of reach.
sitename: ITdaily
date: "2026-11-26"
categories: ['Security']
tags: ['1Password', 'data breach', 'GitHub']
fingerprint: d31f49106e2364d
language: en
image: https://itdaily.com/wp-content/uploads/2021/04/1Password-scaled.jpg
pagetype: article
filedate: "2026-11-28"
---
**An attacker gained access to the GitHub account of a 1Password employee and obtained account data from a portion of users. The contents of the vaults remained out of reach.**

1Password has fallen victim to a cyberattack after an attacker was able to hijack the GitHub account of a 1Password employee. [1Password](https://1password.com/blog/update-on-nov-2026-security-incident) began an investigation on 19 November 2026 into indications that an attacker had taken over an employee’s corporate [GitHub account](https://itdaily.be/nieuws/beveiliging/dropbox-hack/). Through that account, the attacker gained access to source code.

The attacker also placed malicious code on the company’s backend services. That code downloaded administrative data about customers.

## Which data was affected

The hacker retrieved account records from a portion of users. [These include names](https://itdaily.com/blogs/security/what-happens-after-a-hack/), email addresses, account and user identifiers, the time of account creation and the last login. Public keys and parameters of the Secure Remote Password protocol were also included. According to 1Password, nobody can use these to gain access to an account.

In addition, certain emails for invitations, provisioning and account recovery contained tokens. A small number of users were in such a procedure at that time and have been notified personally. A token only grants access in combination with a login via [single sign-on](https://itdaily.be/nieuws/beveiliging/1password-meldt-veiligheidsincident-link-met-recente-inbraak-bij-okta/) or a six-digit code sent to the registered email address.

The attacker also copied source code from private repositories and gained access to the CI/CD system. That system contains secrets for the infrastructure. 1Password had all credentials that may have been exposed renewed and says that the services and product security are not affected.

## Action taken

The company disabled the affected GitHub account, revoked the stolen token and removed the access the attacker had created. All internal credentials that may have been exposed have been renewed or revoked. The codes in invitation and recovery emails are going from six digits to ten alphanumeric characters, which makes brute force attempts practically impossible.

1Password also tightened controls on GitHub, CI/CD and endpoints and added detections for this type of attack. Internally, the company found no evidence of accounts taken over via the exposed tokens. Independent cybersecurity experts are reviewing the approach.

## Stay alert

1Password advises users to be wary of [phishing via unexpected emails](https://itdaily.com/news/security/1password-increases-security-against-phishing/), text messages or phone calls that refer to 1Password, invitations or account recovery. The company never asks for the account password or the Secret Key. Users are best advised to enter those only in the official app or on the official website, after opening it themselves or typing in the address themselves. That is good advice for everything important on the internet: never click on links, but always go to the relevant website, service or app yourself. That way you avoid falling for phishing almost automatically.
