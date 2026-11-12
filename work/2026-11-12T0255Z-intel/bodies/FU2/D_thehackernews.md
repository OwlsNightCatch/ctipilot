---
title: eMudhra Revokes 8 More CAs It Previously Declared Unaffected by Key Compromise
author: The Hacker News
url: https://thehackernews.com/2026/11/emudhra-revokes-8-more-cas-it.html
hostname: thehackernews.com
description: eMudhra revoked 8 more certificate authorities after finding its Python script exposed RSA private keys to process memory during an HSM transfer.
sitename: The Hacker News
date: "2026-11-11"
categories: ['Article']
fingerprint: a464e5b3343675cc
---
The in-house Python script behind [eMudhra's October key compromise](https://thehackernews.com/2026/10/eight-emudhra-ca-keys-compromised.html) has now cost the company 8 more of its intermediate certificate authorities (CAs), even though it did not weaken their keys.

Each intermediate CA has its own private key, which the company uses to sign the certificates it issues. The 8 intermediate CAs compromised in October had a different problem: a single line in the script cut each of their keys to one byte, the company said this week.

The script also retrieved the RSA keys of the 8 newly revoked CAs from the company's hardware security modules (HSMs). The company says it cannot show that the keys were handled as required by its own rules. It revoked the CAs late last week.

The company had called those CAs unaffected. "The RSA issuers went through a different path as per our assessment of the code and are therefore not impacted," it wrote on Mozilla's bug tracker on October 19.

Of the 8, 6 were for website (TLS) certificates and 2 for code signing. The company had put 4 of them into production in May. Its list names 195 certificates from them, 29 for its own domains.

Both problems began at a key ceremony on April 30, 2025, according to the full [incident report](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c82) the company posted to the same bug tracker this week. That day it generated 16 CA keys on Utimaco HSMs, including the 8 behind the October key compromise.

The keys were meant for Crypto4A HSMs at the company's US and EU sites. Moving keys between HSMs from different vendors is limited, the company says, so its PKI operations team wrote the Python script to wrap each key for transport and unwrap it again.

The round trip that day was a practice run of the transfer, and the source HSM's FIPS-approved mode was switched off for it as an approved exception.

After the round trip, the script read each private key out of the HSM into the ceremony computer's memory and rebuilt the key from that copy. For the 8 ECDSA keys, "a single line in that read‑back truncated the private value to its leading byte," the report says.


The rebuilt key carried a label almost identical to the original's, which allowed the weak copy to be sent for signing and certification.

The Hacker News worked out all 8 keys from their public certificates. The smallest, for EM OV TLS CA - G3C, is 4, and the largest is 237.

Nothing in the ceremony tested the key's strength or checked the certified key against the first generated key. The weak keys still produced valid signatures, and their certificates passed linting and 2 WebTrust audit cycles unnoticed.

The HSMs worked correctly throughout, according to the company, which puts the fault in its own script and process controls.

Invalid CRL signatures in June 2025 were an early sign of the same fault, according to the report. The company fixed them at the time by re-signing the lists with the keys that matched the certificates, which were the weak ones.

According to the report, the 8 RSA keys went through the same read-back step that the company's [earlier response](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c11) had ruled out. Early last week, the company said its earlier answers reflected only what its teams had gathered so far, including which script paths each set of keys took.

The script did not shorten those keys, and every signature still checks against the certified key. But their private parts, such as the private exponent and one of the primes, sat in the memory of a Python process on the ceremony computer.

As a result, the company "cannot positively demonstrate that this key material was in compliance with CPS §6.2.6," its own rule on moving keys into and out of an HSM. Logs and files from that computer cannot reliably show how the material was handled.

The company reached that view in early November, after discussions with browser root programs. The 8 RSA CAs were revoked late last week with the reason code cessationOfOperation, not the CA-compromise code used when the first 8 were revoked on October 18.

Participants in the bug thread have asked why the company chose that code rather than keyCompromise.

Of the 195 certificates in the company's [certificate list](https://bugzilla.mozilla.org/show_bug.cgi?id=2083449#c83), 130 came from EM DV TLS CA - G2C, 63 from EM OV TLS CA - G2C, and 2 from the code-signing CA, EM OV CS CA - G2C.

Besides the company's own domains, the certificates name several universities and colleges, a county, and other organizations. The newest was issued last week, days before the CAs were revoked. All their holders have been moved to new certificates, the company says.

The company says the wrap-and-unwrap process was used only this once, and that its other key ceremonies all created keys in place.

Participants in the bug thread also want the script published, and some have asked how private keys could leave its HSMs at all.

KPMG, which the company hired as an independent reviewer, is due to finish by December 4. The company's inventory of all its CA keys is due November 30.

The company knows of no case of misuse. Anyone holding one of the October keys could have impersonated any website, according to a [disclosure site](https://emudhra.we-have-a-problem.com/) run by Dennis Jackson, who investigated the keys for Mozilla.

Browsers that enforce Certificate Transparency could not have been fooled. Whether anyone used the keys against software that skips that check is not known.

### What emSign Certificate Holders Need to Check

eMudhra, which sells certificates under the emSign brand, is exiting the publicly trusted TLS business following its October 22 [announcement](https://thehackernews.com/2026/10/emudhra-to-exit-global-ssltls-business.html).

Holders can find affected certificates in the company's list or by searching Certificate Transparency logs for the revoked G2C TLS issuers.

All issuance from the company's G1 hierarchy is due to stop before November 16, as the remaining customers, mainly a university federation in North America, move to another provider.

Microsoft will start removing the 10 remaining eMudhra roots, including emSign Root CA - G1, on November 16, according to an update to its [security response post](https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys) earlier this week. Certificates that chain to those roots will then lose default trust in Windows and Edge, and in some of its other products on their own timelines.

According to the Indian company's [phase-out schedule](https://emudhra.com/en/post/certificate-security-incident), Chrome and Firefox will not trust G1 certificates issued after November 16, and Apple will end trust in all G1 certificates, including older ones, on November 30.

macOS 27.2.1, 26.7.3 and 15.8.3 stop bundled command-line tools such as curl and git from accepting the compromised TLS CA certificates, Apple said in a [support note](https://support.apple.com/en-us/149555) earlier this week. They also drop 5 roots, including emSign Root CA - G1, from /etc/ssl/cert.pem, so tools relying on that file may not verify some sites chaining to them.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
