---
title: Protecting Chrome and Android Users from Compromised eMudhra Intermediate CA Certificates
author: Chrome; Android Security Teams
url: https://blog.google/security/protecting-chrome-and-android-users-from-compromised-emudhra-intermediate-ca-certificates/
hostname: blog.google
description: The Chrome Root Program received a report from a security researcher regarding the compromise of private keys associated with eight eMudhra subordinate Certification Aut…
sitename: Google
date: "2026-10-20"
tags: ['None', 'Android Security,Chrome Security']
fingerprint: ec51acb1611f7142
---
Chrome Security

# Protecting Chrome and Android Users from Compromised eMudhra Intermediate CA Certificates

*Update (November 4, 2026): To proactively safeguard Chrome’s users, and preserve the integrity of the Chrome Root Store, TLS server authentication certificates validating to CN=emSign Root CA - G1, OU=emSign PKI, O=eMudhra Technologies Limited, C=IN whose earliest Signed Certificate Timestamp (SCT) is dated after November 16, 2026 11:59:59 PM UTC, will no longer be trusted by default in Chrome 153 and higher. TLS server authentication certificates validating to the above root whose earliest SCT is on or before November 16, 2026 11:59:59 PM UTC, will be unaffected by this change. See more here.*

On Saturday, October 17, 2026, at 18:05 UTC, the Chrome Root Program received a report from a security researcher regarding the compromise of private keys associated with eight eMudhra subordinate Certification Authority (CA) certificates. The private keys for these certificates were generated with insufficient randomness (i.e., weak cryptographic entropy), enabling anyone to forge trusted HTTPS certificates to impersonate any website against clients that have not yet removed trust in those CAs.

At 19:45 UTC, Chrome completed corroborating the findings and landed a [CRLSet](https://www.chromium.org/Home/chromium-security/crlsets/) update blocking the Subject Public Key Info (SPKI) hashes of the affected intermediate CAs. Because this CRLSet update blocks by SPKI, Chrome users were immediately protected against all certificates sharing those keys, without requiring a browser update or restart. Android devices and Googlebooks received an equivalent update through Google Play Services around 22:00 UTC on Monday. While the majority of Android devices have already received this update, users can also trigger an immediate update by restarting their device.

Because no TLS certificates chaining to these six intermediate CAs were logged to Certificate Transparency (CT) before our blocking action, no fraudulent certificates issued by these CAs could have been used against CT-enforcing clients. This includes Chrome, which enforces CT for all publicly trusted certificates by default. This also includes Android applications that target the latest SDK version or have otherwise opted in to CT enforcement.

Following the initial block, the Chrome Root Program also took several additional steps to protect the broader ecosystem:

- We have reviewed and confirmed that no other keys included in our root stores share the same failure mode with weak entropy.
- Following our initial block, we have been coordinating with other browser vendors, root store operators, and software maintainers to support ecosystem-wide remediation.
- We have worked to ensure that CT logs have been updated to reject certificates chaining to these compromised CAs to prevent risk to the CT ecosystem.

To support other consumers of the Chrome Root Store that do not consume CRLSet updates, we have also removed [emSign ECC Root CA - G3](https://chromium.googlesource.com/chromium/src/+/5a6a4e78597add03dd32bc233e03f3145cd99b65/net/data/ssl/chrome_root_store/root_store.textproto#279) (the root certificate that signed the compromised CA certificates) from the Chrome Root Store. Some legitimate certificates chaining to this root will cease to function in Chrome as a result, and eMudhra has committed to working with impacted subscribers to migrate customers off of the impacted root. This root removal is expected to be released for all devices [relying](https://chromium.googlesource.com/chromium/src/+/main/net/data/ssl/chrome_root_store/faq.md#When-did-these-features-land) on the Chrome Root Store Tuesday morning, October 27, 2026 PDT, and sooner on prerelease channels like Chrome Canary and Chrome Beta. **To avoid breakage, website operators with certificates chaining to emSign ECC Root CA - G3 must immediately acquire and install a new TLS certificate from another PKI hierarchy included in the Chrome Root Store.**

Inclusion in the Chrome Root Store requires that a CA Owner continuously demonstrate the technical competence and operational rigor necessary to protect Chrome users. Due to the seriousness of this incident, the Chrome Root Program is closely investigating the ongoing inclusion of eMudhra's remaining CA certificates in the Chrome Root Store and will share further updates in public forums (e.g., the [Common CA Database Public list](https://groups.google.com/a/ccadb.org/g/public)) as our evaluation progresses.
