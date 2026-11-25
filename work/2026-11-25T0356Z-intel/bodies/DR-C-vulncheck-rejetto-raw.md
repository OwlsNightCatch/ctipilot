---
title: Rejetto HFS < 3.2.1 Session Forgery via Predictable Signing Key
url: https://www.vulncheck.com/advisories/rejetto-hfs-session-forgery-via-predictable-signing-key
hostname: vulncheck.com
description: "CVE-2026-61500 | null | Affecting hfs >= 3.0.0, < 3.2.1 | Severity: CRITICAL | CVSS: 9.3"
sitename: VulnCheck
date: "2026-07-13"
fingerprint: a0b9bed3b5dfc5c1
language: en
image: https://www.vulncheck.com/_og/d/c_Advisory,icon_i-mdi-comment-alert,title_~UmVqZXR0byBIRlMgPCAzLjIuMSBTZXNzaW9uIEZvcmdlcnkgdmlhIFByZWRpY3RhYmxlIFNpZ25pbmcgS2V5,date_2026-07-13,headline_Advisories,cves_CVE-2026-61500,props_eyJhZmZlY3RpbmciOlsiaGZzID49IDMuMC4wLCA8IDMuMi4xIl19,severity_CRITICAL,cvss_9.3,p_Ii9hZHZpc29yaWVzL3JlamV0dG8taGZzLXNlc3Npb24tZm9yZ2VyeS12aWEtcHJlZGljdGFibGUtc2lnbmluZy1rZXki,s_yEegaza7Qrxdg32d.png
pagetype: website
filedate: "2026-11-25"
---
Advisories

- Severity
  critical
- Date
- Affecting
  - hfs >= 3.0.0, \< 3.2.1
- CWE
  - CWE-338 Use of Cryptographically Weak Pseudo-Random Number Generator (PRNG)
- CVSS
  9.3
- CVSS V4 Vector
  CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N
- References
- Credit
  Zach Hanley (@hacks\_zach) of Horizon3.ai, in collaboration with Claude and Anthropic Research
- Description
  Rejetto HFS 3.0.0 through 3.2.0 derives its session-cookie signing key from the non-cryptographic Math.random() generator and discloses outputs of the same generator to unauthenticated clients during login. A remote attacker can collect a small number of login responses, reconstruct the generator's state, recover the signing key, and forge a valid administrator session cookie, leading to full administrative access and remote code execution via the server\_code configuration feature.
- VulnCheck KEV
  [This advisory is in the VulnCheck KEV database](https://api.vulncheck.com/v3/index/vulncheck-kev?cve=CVE-2026-61500)

Explore VulnCheck, a next-generation Cyber Threat Intelligence platform, which provides exploit and vulnerability intelligence to help you prioritize and remediate vulnerabilities that matter.

- Vulnerability PrioritizationPrioritize vulnerabilities that matter based on the threat landscape and defer vulnerabilities that don't.
- Early Warning SystemReal-time alerting of changes in the vulnerability landscape so that you can take action before the attacks start.
