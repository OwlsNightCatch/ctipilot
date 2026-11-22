---
title: Rapid7
author: Christopher Granleese
url: https://www.rapid7.com/blog/post/pt-metasploit-wrap-up-breaking-zimbra-s-identity-boundaries/
hostname: rapid7.com
description: This release we have three pull requests from jburgess-r7 building out coverage for the identity-boundary issues detailed in Rapid7's Breaking Zimbra Identity Boundaries, Part One research. First up is a new shared mixin, Msf::Exploit::Remote::HTTP::Zimbra, which gives every current and future Zimbra module a common foundation for account/admin SOAP authentication, canonical identity resolution, mailbox-server lookup, and version parsing, allowing future modules to stay focused on the vulnerability instead of re-implementing Zimbra's SOAP plumbing. Built on top of that mixin are two new modules targeting CVEs from the same research track.
sitename: Rapid7
date: "2026-11-20"
categories: ['Metasploit']
tags: ['cybersecurity company,managed detection and response,exposure management,managed security solutions,vulnerability management,exposure assessment platform']
fingerprint: ba330954cce4aec5
---
This release we have three pull requests from [jburgess-r7](https://github.com/jburgess-r7) building out coverage for the identity-boundary issues detailed in Rapid7's [Breaking Zimbra Identity Boundaries, Part One](https://www.rapid7.com/blog/post/ve-breaking-zimbra-identity-boundaries-part-1/) research.

First up is a new shared mixin, [Msf::Exploit::Remote::HTTP::Zimbra](https://github.com/rapid7/metasploit-framework/pull/22091), which gives every current and future Zimbra module a common foundation for account/admin SOAP authentication, canonical identity resolution, mailbox-server lookup, and version parsing, allowing future modules to stay focused on the vulnerability instead of re-implementing Zimbra's SOAP plumbing.

Built on top of that mixin are two new modules targeting CVEs from the same research track:

**CVE-2026-73571** ([#22080](https://github.com/rapid7/metasploit-framework/pull/22080)) It's an authorization bypass in Zimbra's SaveDraftRequest handling that lets an ordinary authenticated user send mail as another local mailbox without a delegation grant, landing a message in the victim's own Sent folder in the process.

**CVE-2026-93637** ([#22070](https://github.com/rapid7/metasploit-framework/pull/22070)) Is a rate-limit bypass in Zimbra's Network Edition GraphQL authentication endpoint, which lets credential-stuffing attempts skip the source-IP lockout counter that normally protects the SOAP login path.

Both modules were validated against live Zimbra 10.1.16 Network Edition instances. Super cool contributions from our very own [jburgess-r7](https://github.com/jburgess-r7).

## New module content (6)

### Zimbra SaveDraftRequest Email Impersonation

Authors: Ayoub Nabil Boubagrat and Crypto-Cat

Type: Auxiliary

Pull request: [#22080](https://github.com/rapid7/metasploit-framework/pull/22080) contributed by [jburgess-r7](https://github.com/jburgess-r7)

Path: admin/http/zimbra\_email\_impersonation

CVE reference: [CVE-2026-73571](https://www.rapid7.com/db/vulnerabilities/cve-2026-73571/)

Description: Adds an auxiliary module for CVE-2026-73571, allowing an authenticated user to send email as another local mailbox on Zimbra 10.1.16. The module supports optional Inbox delivery verification.

### Zimbra GraphQL Authentication Rate Limit Bypass

Author: Crypto-Cat

Type: Auxiliary

Pull request: [#22070](https://github.com/rapid7/metasploit-framework/pull/22070) contributed by [jburgess-r7](https://github.com/jburgess-r7)

Path: scanner/http/zimbra\_graphql\_brute

CVE reference: [CVE-2026-93637](https://www.rapid7.com/db/vulnerabilities/cve-2026-93637/)

Description: This adds an auxiliary scanner for CVE-2026-93637 that tests Zimbra Network Edition authentication through GraphQL batches. The module supports configurable batches, safe stopping controls, and storage of verified credentials.

### BeyondTrust Remote Support MRS Origin Validation File Upload

Author: jheysel

Type: Exploit

Pull request: [#22083](https://github.com/rapid7/metasploit-framework/pull/22083) contributed by [jheysel-r7](https://github.com/jheysel-r7)

Path: linux/http/beyondtrust\_rs\_mrs\_file\_upload

CVE reference: [CVE-2026-102764](https://www.rapid7.com/db/vulnerabilities/cve-2026-102764/)

Description: Adds an exploit module for an origin validation vulnerability in Beyond Trust Remote Support which allows for unauthenticated file upload resulting in RCE. The vulnerability is tracked as CVE-2026-102764.

### Openfire Deleted Administrator Account Authentication Bypass RCE

Authors: Admin9961, Jatin Mannepalli, h00die-gr3y [\[email protected\]](https://www.rapid7.com/cdn-cgi/l/email-protection#fc94cccc989599d29b8ecf85bc9b919d9590d29f9391), and xRogue

Type: Exploit

Pull request: [#22043](https://github.com/rapid7/metasploit-framework/pull/22043) contributed by [mjatin2007](https://github.com/mjatin2007)

Path: multi/http/openfire\_deleted\_admin\_rce\_cve\_2024\_25420

CVE reference: [CVE-2024-25420](https://www.rapid7.com/db/vulnerabilities/cve-2024-25420/)

Description: Adds exploit module for CVE-2024-25420, an vulnerability in Ignite Realtime Openfire before 4.8.1 that allows a remote attacker to escalate privileges via the admin.authorizedJIDs system property component.

### Cisco Secure Email Gateway AMP Arbitrary File Write RCE

Author: sfewer-r7

Type: Exploit

Pull request: [#22028](https://github.com/rapid7/metasploit-framework/pull/22028) contributed by [sfewer-r7](https://github.com/sfewer-r7)

Path: unix/smtp/cisco\_secure\_email\_gateway\_amp\_file\_write\_rce

CVE reference: [CVE-2026-76519](https://www.rapid7.com/db/vulnerabilities/cve-2026-76519/)

Description: Adds a new exploit module for CVE-2026-76519 an unauth RCE in Cisco Secure Email Gateway which was disclosed last month by the vendor and reported as being exploited in-the-wild. The vulnerability is a file write in the Advanced Malware Protection (AMP) File Reputation feature. When processing a TAR file which contains a PAX archive, we can force an existing file to be overwritten. The module overwrites an existing script /data/bin/core\_watch.sh with a Metasploit payload. This script file is executed every 5 minutes by a cron job, giving us RCE with root privs.

### Cisco Secure Email Gateway ECS Message-ID SQL Injection RCE

Author: sfewer-r7

Type: Exploit

Pull request: [#22024](https://github.com/rapid7/metasploit-framework/pull/22024) contributed by [sfewer-r7](https://github.com/sfewer-r7)

Path: unix/smtp/cisco\_secure\_email\_gateway\_ecs\_sqli\_rce

CVE reference: [CVE-2026-76461](https://www.rapid7.com/db/vulnerabilities/cve-2026-76461/)

Description: This adds an exploit module for an unauthenticated SQL injection in the Cisco Secure Email Gateway (SEG) Email Cloud Scanner (ECS) URL-retrospective message database. We believe this is CVE-2026-76461 being tracked as, which was reported as being exploited in-the-wild last month as a zero-day.

## Enhancements and features (2)

- [#22055](https://github.com/rapid7/metasploit-framework/pull/22055) from [kx7m2qd](https://github.com/kx7m2qd) - Improve ADSelfService Plus check result clarity.
- [#22091](https://github.com/rapid7/metasploit-framework/pull/22091) from [jburgess-r7](https://github.com/jburgess-r7) - This adds a shared Zimbra SOAP support for account and administrator authentication, account discovery, and version retrieval. Zimbra modules can now reuse consistent token routing, response validation, and error handling.

## Bugs fixed (24)

- [#21879](https://github.com/rapid7/metasploit-framework/pull/21879) from [JothamB](https://github.com/JothamB) - Fixes a crash in the exploits/windows/local/unquoted\_service\_path module.
- [#21931](https://github.com/rapid7/metasploit-framework/pull/21931) from [Pushpenderrathore](https://github.com/Pushpenderrathore) - Improves the performance of Malleable profiles in versions of Ruby older than or equal to version 3.1.
- [#21948](https://github.com/rapid7/metasploit-framework/pull/21948) from [s-r-e-e-r-a-j](https://github.com/s-r-e-e-r-a-j) - Fixes a crash when running Metasploit with Apktool 3.x.
- [#21968](https://github.com/rapid7/metasploit-framework/pull/21968) from [pauljccode](https://github.com/pauljccode) - Fixes a crash when running Android payload generation.
- [#21986](https://github.com/rapid7/metasploit-framework/pull/21986) from [Aaditya1273](https://github.com/Aaditya1273) - Fixed OptArray normalization so accepted values that differ only by capitalization are canonicalized and deduplicated correctly.
- [#21991](https://github.com/rapid7/metasploit-framework/pull/21991) from [pauljccode](https://github.com/pauljccode) - Fixes intermittent UDP receive failures when routing traffic through a Quectel modem session.
- [#22026](https://github.com/rapid7/metasploit-framework/pull/22026) from [kx7m2qd](https://github.com/kx7m2qd) - Fixes a warning message when running the SNMP login scanner module.
- [#22062](https://github.com/rapid7/metasploit-framework/pull/22062) from [Yeagerist0](https://github.com/Yeagerist0) - Fix dlink\_dir\_645\_password\_extractor crashing after it extracts credentials.
- [#22063](https://github.com/rapid7/metasploit-framework/pull/22063) from [Yeagerist0](https://github.com/Yeagerist0) - Fixes NoMethodError in auxiliary/scanner/misc/oki\_scanner.
- [#22074](https://github.com/rapid7/metasploit-framework/pull/22074) from [bc-idpotat](https://github.com/bc-idpotat) - Skip invalid SPNs during LDAP enumeration.
- [#22075](https://github.com/rapid7/metasploit-framework/pull/22075) from [Yeagerist0](https://github.com/Yeagerist0) - Removes duplicate target prefix from vnc\_login module output.
- [#22076](https://github.com/rapid7/metasploit-framework/pull/22076) from [Yeagerist0](https://github.com/Yeagerist0) - Removes duplicate target prefix from rsh\_login and rlogin\_login module output.
- [#22078](https://github.com/rapid7/metasploit-framework/pull/22078) from [Yeagerist0](https://github.com/Yeagerist0) - Fixes auxiliary/scanner/http/coldfusion\_locale\_traversal ignoring FINGERPRINT when FILE is set.
- [#22079](https://github.com/rapid7/metasploit-framework/pull/22079) from [Yeagerist0](https://github.com/Yeagerist0) - Fixes a crash when running the xorcom\_completepbx\_diagnostics\_file\_read module.
- [#22087](https://github.com/rapid7/metasploit-framework/pull/22087) from [Yeagerist0](https://github.com/Yeagerist0) - Reject invalid bytes in the binary encoding checker.
- [#22105](https://github.com/rapid7/metasploit-framework/pull/22105) from [dwelch-r7](https://github.com/dwelch-r7) - Updates the msfdb bootstrap capabilities when creating and securing a created PostgreSQL database.
- [#22107](https://github.com/rapid7/metasploit-framework/pull/22107) from [jankesec](https://github.com/jankesec) - Removes duplicate peer:port prefixes from several scanners.
- [#22108](https://github.com/rapid7/metasploit-framework/pull/22108) from [jankesec](https://github.com/jankesec) - Removes duplicate peer:port prefixes from several scanners.
- [#22111](https://github.com/rapid7/metasploit-framework/pull/22111) from [cgranleese-r7](https://github.com/cgranleese-r7) - Adds additional validation to Metasploit's hardware bridge support.
- [#22116](https://github.com/rapid7/metasploit-framework/pull/22116) from [Army-R](https://github.com/Army-R) - Updates the post/windows/manage/enable\_rdp module's error handling.
- [#22128](https://github.com/rapid7/metasploit-framework/pull/22128) from [sjanusz-r7](https://github.com/sjanusz-r7) - Fixes false positives reported by the check method for auxiliary/gather/solarwinds\_webhelpdesk\_backdoor.
- [#22142](https://github.com/rapid7/metasploit-framework/pull/22142) from [Yeagerist0](https://github.com/Yeagerist0) - Fixes Msf::RPC::JSON::Request rejecting valid JSON-RPC responses as InvalidResponse when symbolize\_names: false is used.
- [#22143](https://github.com/rapid7/metasploit-framework/pull/22143) from [urvalkheni](https://github.com/urvalkheni) - Fixes a crash when running the pihole\_domains\_api\_exec module when a token is not found.
- [#22151](https://github.com/rapid7/metasploit-framework/pull/22151) from [sjanusz-r7](https://github.com/sjanusz-r7) - Fixes a false positive result in the auxiliary/scanner/http/litellm\_proxy\_sqli vulnerability detection check.

## Documentation added (1)

- [#21937](https://github.com/rapid7/metasploit-framework/pull/21937) from [satanonsteroids2024-zzz](https://github.com/satanonsteroids2024-zzz) - Updates the msfvenom help menu documentation.

You can always find more documentation on our docsite at [docs.metasploit.com](https://docs.metasploit.com/).

## Get it

As always, you can update to the latest Metasploit Framework with msfupdate and you can get more details on the changes since the last blog post from GitHub:

If you are a git user, you can clone the [Metasploit Framework repo](https://github.com/rapid7/metasploit-framework) (master branch) for the latest. To install fresh without using git, you can use the open-source-only [Nightly Installers](https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers) or the commercial edition [Metasploit Pro](https://www.rapid7.com/products/metasploit/download/)
