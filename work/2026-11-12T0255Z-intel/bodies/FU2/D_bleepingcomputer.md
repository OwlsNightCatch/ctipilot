---
title: eMudhra revokes 8 more CA certificates after private key mishap
author: Lawrence Abrams
url: https://www.bleepingcomputer.com/news/security/emudhra-revokes-8-more-ca-certificates-after-private-key-mishap/
hostname: bleepingcomputer.com
description: Certificate authority eMudhra has revoked eight additional intermediate CA certificates after an investigation into its recent certificate security incident found improper handling of private keys during the certificate-generation process.
sitename: BleepingComputer
date: "2026-11-11"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, Certificate Authority, Certificate Revocation, Certificates, eMudhra,virus removal, malware removal, computer help, technical support']
fingerprint: "7d5fef96341e74d4"
---
Certificate authority eMudhra has revoked eight additional intermediate CA certificates after an investigation into its recent certificate security incident found improper handling of private keys during the certificate-generation process.

The new revocations bring the total number of affected intermediate CA certificates to 16, including eight previously compromised certificates whose private keys were so weak that anyone could recover them almost instantly.

In a [new incident report](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c82) published Tuesday, eMudhra said that both sets of certificates were affected by a custom Python script used to transfer private keys between hardware security modules (HSMs) in April 2025.

HSMs are devices designed to securely generate and store cryptographic keys, preventing sensitive private keys from being exposed outside the hardware.

eMudhra says it developed the script to move certificate authority keys between different HSM vendors at its facilities after delays in obtaining new hardware.

However, the script contained a bug that reduced eight ECDSA private keys to a single byte, making them extremely easy to recover.

The same script also processed eight RSA private keys, which handled sensitive key information in the memory of the computer running the script rather than keeping it protected within the HSM.

While the RSA keys were not weakened like the original eight certificates, eMudhra says it could not demonstrate that it handled them under its certificate security policies.

"A re‑import performed from host process memory is not consistent with the CPS §6.2.6 and the RSA objects are therefore treated as not meeting that requirement," reads the incident report.

Due to this, the company revoked the additional eight RSA intermediate CA certificates on November 7, including certificates used to issue TLS and code-signing certificates.

Some of the affected RSA intermediates had been actively issuing certificates since May 2026, with the last certificate issued on November 3.

eMudhra says the affected customer certificates have also been replaced or migrated.

The investigation also found that an earlier problem in June 2025 could have revealed the flaw more than a year before it was discovered by a security researcher known as "Wayne."

At that time, eMudhra detected certificate revocation lists (CRLs) signed with private keys that did not match the corresponding CA certificates.

The company fixed the issue by signing the revocation lists with the matching keys but did not investigate why the problem occurred.

The new report confirms this was an early warning sign of the faulty key-generation process that went undetected until October 2026.

The investigation also found that eMudhra did not verify the strength of generated private keys or check that the keys used for certification matched those originally created in the HSM.

## Major browsers blocked compromised certificates

As [BleepingComputer previously reported](https://www.bleepingcomputer.com/news/security/mozilla-google-apple-block-compromised-emudhra-ca-certificates/), the incident was first disclosed on October 17, when a security researcher named Wayne discovered that eight eMudhra intermediate CA private keys could be recovered by testing just 256 possible values.

Major browsers and operating systems trusted the compromised certificates, potentially allowing attackers to forge certificates for legitimate websites and intercept encrypted communications.

Mozilla, Google, Apple, and other software vendors subsequently released protections to block the compromised certificates.

Microsoft also [released out-of-band Windows updates](https://www.bleepingcomputer.com/news/microsoft/microsoft-releases-windows-oob-updates-to-distrust-emudhra-certificates/) on October 26 to remove trust in affected eMudhra certificate trust chains on systems that could not receive automatic certificate trust updates.

Following the incident, eMudhra announced that it would exit the publicly trusted TLS certificate business and transition its remaining customers to another provider.

The company says it plans to stop issuing certificates under its remaining G1 hierarchy by November 16.

eMudhra has also commissioned an independent review by KPMG, with findings expected by December 4, to identify improvements to its certificate management and key-generation procedures.

The company says it has not detected any evidence that the compromised keys were used maliciously.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
