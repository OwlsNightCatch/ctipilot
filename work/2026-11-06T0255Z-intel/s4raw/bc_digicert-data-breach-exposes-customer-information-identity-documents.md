---
title: DigiCert data breach exposes customer information, identity documents
author: Lawrence Abrams
url: https://www.bleepingcomputer.com/news/security/digicert-data-breach-exposes-customer-information-identity-documents/
hostname: bleepingcomputer.com
description: DigiCert warns it suffered a data breach after a server migration mistakenly exposed an internal business system to the internet, allowing unauthorized access to customer information and identity documents.
sitename: BleepingComputer
date: "2026-11-05"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Data Breach, DigiCert, Identity Documents, MFA, Passport,virus removal, malware removal, computer help, technical support']
fingerprint: "6f5fbd8b1d17b7c4"
---
DigiCert warns it suffered a data breach after a server migration mistakenly exposed an internal business system to the internet, allowing unauthorized access to customer information and identity documents.

The certificate authority says the breach affected a small portion of its archived customer data, including names, business email addresses, phone numbers, and business addresses.

For some people, the exposed records also contained personal identification documents, such as driver's licenses, passports, and utility bills.

DigiCert has begun sending data breach notifications to affected customers, with cloud architect Fabian Bader sharing a copy of the notification on X.

"Thanks @digicert that your data leak was 'limited' to only my full PII data and potentially any verification documents I submitted for my certificate," [Bader wrote](https://x.com/fabian_bader/status/2118079207171568065).

In the notification, DigiCert said it was still reviewing identification documents to determine those who were affected and would notify them once the review was complete.

"The information involved was limited to names, business email addresses, phone numbers, and business address shared with DigiCert and, if provided, may have included an identification document such as a driver’s license, passport, utility bill or other document with name and address," the data breach notification reads.

An [incident report](https://bugzilla.mozilla.org/show_bug.cgi?id=2084460#c2) on Mozilla's Bugzilla platform explains that a February 2025 server migration mistakenly exposed an internal business system to the internet that was previously only accessible via VPN.

The exposed system contained a self-registration feature intended for other applications, allowing external users to create accounts.

Although these accounts weren't assigned to any particular application, an authorization flaw let them access archived customer information in read-only mode.

DigiCert first discovered unauthorized accounts on the exposed system in June 2026, but initially determined they couldn't access customer information because they weren't assigned to an application.

The company subsequently received a report through its managed security research program warning that external users could create accounts on the system.

DigiCert deployed security fixes to restrict access to the system and address the authorization flaw, but did not realize at the time that archived data had been accessed.

It wasn't until October 19 that a further investigation confirmed an unauthorized account had accessed customer information between June 27 and July 2, 2026.

"The incident was initially handled as an account-creation issue rather than a data-access event," DigiCert acknowledged in its report.

DigiCert says the unauthorized account had read-only access and could not modify records, approve certificate validations, or issue certificates.

The company has now restricted access to the affected system, disabled self-registration, and added additional access controls.

DigiCert says its certificate authority services, CertCentral, and DigiCert ONE platforms were not compromised, and that customer login credentials and issued certificates remain secure.

BleepingComputer has contacted DigiCert to ask further questions about the incident, including how many people were impacted, and will update the story if we get a response.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
