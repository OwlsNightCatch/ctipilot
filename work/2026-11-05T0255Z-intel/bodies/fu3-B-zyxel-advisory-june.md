---
title: Zyxel security advisory for stack-based buffer overflow vulnerability in GS1900 series switches | Zyxel Networks
url: https://www.zyxel.com/global/en/support/security-advisories/zyxel-security-advisory-for-stack-based-buffer-overflow-vulnerability-in-gs1900-series-switches-06-16-2026
hostname: zyxel.com
description: "CVE: CVE-2026-7273 Summary Zyxel has released patches for GS1900 series switches affected by a stack-based buffer overflow vulnerability. Users are advised to install them for optimal protection. What is the vulnerability? A stack-based buffer overflow vulnerability in the CGI program of the Zyxel GS1900 series switch firmware could allow a LAN-based, unauthenticated attacker to exploit the flaw and potentially execute OS commands via a crafted HTTP request. What versions are vulnerable—and what should you do? After a thorough investigation, we identified the vulnerable switch firmware versions and released patches for models still within their vulnerability support period, as shown in the table below. Please note that on-market products not listed in the table remain unaffected. Affected model Affected version Patch availability GS1900-8 2.90(AAHH.1)C0 and earlier 2.90(AAHH.2)C0 GS1900-8HP 2.90(AAHI.1)C0 and earlier 2.90(AAHI.2)C0 GS1900-10HP 2.90(AAZI.1)C0 and earlier 2.90(AAZI.2)C0 GS1900-16 2.90(AAHJ.1)C0 and earlier 2.90(AAHJ.2)C0 GS1900-24 2.90(AAHL.1)C0 and earlier 2.90(AAHL.2)C0 GS1900-24E 2.90(AAHK.1)C0 and earlier 2.90(AAHK.2)C0 GS1900-24EP 2.90(ABTO.1)C0 and earlier 2.90(ABTO.2)C0 GS1900-24HPv2 2.90(ABTP.1)C0 and earlier 2.90(ABTP.2)C0 GS1900-48 2.90(AAHN.1)C0 and earlier 2.90(AAHN.2)C0 GS1900-48HPv2 2.90(ABTQ.1)C0 and earlier 2.90(ABTQ.2)C0 Got a question? Please contact your local service rep or visit Zyxel's Community for further information or assistance. Acknowledgment Thanks to Lei Gu, Jun Cao, Zhiqing Rui, Jingzheng Wu, and Tianyue Luo from ISCAS for reporting the issue to us. Revision history 2026-6-16: Initial release"
sitename: Zyxel Networks
date: "2026-06-16"
fingerprint: "22d9a152f496f28d"
---

# Zyxel security advisory for stack-based buffer overflow vulnerability in GS1900 series switches

###### CVE:  [CVE-2026-7273](https://www.cve.org/CVERecord?id=CVE-2026-7273)

###### Summary

Zyxel has released patches for GS1900 series switches affected by a stack-based buffer overflow vulnerability. Users are advised to install them for optimal protection.

###### What is the vulnerability?

A stack-based buffer overflow vulnerability in the CGI program of the Zyxel GS1900 series switch firmware could allow a LAN-based, unauthenticated attacker to exploit the flaw and potentially execute OS commands via a crafted HTTP request.

###### What versions are vulnerable—and what should you do?

After a thorough investigation, we identified the vulnerable switch firmware versions and released patches for models still within their vulnerability support period, as shown in the table below. Please note that on-market products not listed in the table remain unaffected.

| Affected model | Affected version | Patch availability | 
|---|---|---|
| **GS1900-8** | 2.90(AAHH.1)C0 and earlier | 2.90(AAHH.2)C0 | 
| **GS1900-8HP** | 2.90(AAHI.1)C0 and earlier | 2.90(AAHI.2)C0 | 
| **GS1900-10HP** | 2.90(AAZI.1)C0 and earlier | 2.90(AAZI.2)C0 | 
| **GS1900-16** | 2.90(AAHJ.1)C0 and earlier | 2.90(AAHJ.2)C0 | 
| **GS1900-24** | 2.90(AAHL.1)C0 and earlier | 2.90(AAHL.2)C0 | 
| **GS1900-24E** | 2.90(AAHK.1)C0 and earlier | 2.90(AAHK.2)C0 | 
| **GS1900-24EP** | 2.90(ABTO.1)C0 and earlier | 2.90(ABTO.2)C0 | 
| **GS1900-24HPv2** | 2.90(ABTP.1)C0 and earlier | 2.90(ABTP.2)C0 | 
| **GS1900-48** | 2.90(AAHN.1)C0 and earlier | 2.90(AAHN.2)C0 | 
| **GS1900-48HPv2** | 2.90(ABTQ.1)C0 and earlier | 2.90(ABTQ.2)C0 | 

###### Got a question?

Please contact your local service rep or visit Zyxel's [Community](https://community.zyxel.com/en) for further information or assistance.

###### Acknowledgment

Thanks to Lei Gu, Jun Cao, Zhiqing Rui, Jingzheng Wu, and Tianyue Luo from ISCAS for reporting the issue to us.

###### Revision history

2026-6-16: Initial release
