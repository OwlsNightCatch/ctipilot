# extract: served via trafilatura-direct
---
title: Synology_SA_26_13 | Synology Inc.
author: Synology Inc
url: https://www.synology.com/
hostname: synology.com
description: Synology Product Security Advisory
sitename: Synology Inc.
date: "2026-09-18"
fingerprint: "9400879e4bbf8e70"
---
# Synology-SA-26:13 DSM

Publish Time: UTC+8

Last Updated: UTC+8

- Severity
- Critical

- Status
- Resolved

**Abstract**

Synology has released a security update for the DSM to address multiple vulnerabilities :

- CVE-2026-13684, CVE-2026-13639, and CVE-2026-13635 allow remote attackers to read or write arbitrary files, conduct denial-of-service attacks, or obtain non-sensitive information.
- CVE-2026-13673, CVE-2026-6205, and CVE-2026-13666 allow remote authenticated users to read or write arbitrary files, write limited files when a victim clicks a sharing URL, and conduct denial-of-service attacks.
- CVE-2026-13623 and CVE-2026-13683 allow remote authenticated users with administrator privileges to read or write limited files or obtain non-sensitive information.

Please refer to the 'Affected Products' table for the corresponding updates.

**Affected Products**

| Product | Severity | Fixed Release Availability | 
|---|---|---|
| DSM 7.4 | Critical | Upgrade to 7.4-90075 or above. | 
| DSM 7.3 | Critical | Upgrade to 7.3.2-86009-4 or above. | 
| DSM 7.2.2 | Critical | Upgrade to 7.2.2-72806-9 or above. | 
| DSM 7.2.1 | Critical | Upgrade to 7.2.1-69057-12 or above. | 

**Mitigation**

None

**Detail**

- CVE-2026-13684 
  - Severity: Critical
  - CVSS3 Base Score: 9.8
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
  - [CWE-116: Improper Encoding or Escaping of Output](https://cwe.mitre.org/data/definitions/116.html)
  - An improper encoding or escaping of output vulnerability in SCGI in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2-72806-9, 7.3.2-86009-4 and 7.4-90075 allows remote attackers to read or write arbitrary files and conduct denial-of-service attacks.
- CVE-2026-13639 
  - Severity: Critical
  - CVSS3 Base Score: 9.8
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)
  - [CWE-331: Insufficient Entropy](https://cwe.mitre.org/data/definitions/331.html)
  - An insufficient entropy vulnerability in login logic in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2-72806-9, 7.3.2-86009-4 and 7.4-90075 allows remote attackers to read or write arbitrary files and conduct denial-of-service attacks.
- CVE-2026-13673 
  - Severity: Important
  - CVSS3 Base Score: 8.8
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H)
  - [CWE-732: Incorrect Permission Assignment for Critical Resource](https://cwe.mitre.org/data/definitions/732.html)
  - An incorrect permission assignment for critical resource vulnerability in LDAP API in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2-72806-9, 7.3.2-86009-4 and 7.4-90075 allows remote authenticated users to read or write arbitrary files and conduct denial-of-service attacks.
- CVE-2026-6205 
  - Severity: Important
  - CVSS3 Base Score: 8.1
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:H](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:H/A:H)
  - [CWE-73: External Control of File Name or Path](https://cwe.mitre.org/data/definitions/73.html)
  - An external control of file name or path vulnerability in Upload API in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2-72806-9, 7.3.2-86009-4 and 7.4-90075 allows remote authenticated users to write arbitrary files and conduct denial-of-service attacks.
- CVE-2026-13635 
  - Severity: Moderate
  - CVSS3 Base Score: 5.3
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N)
  - [CWE-116: Improper Encoding or Escaping of Output](https://cwe.mitre.org/data/definitions/116.html)
  - An improper encoding or escaping of output vulnerability in Auth API in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2-72806-9, 7.3.2-86009-4 and 7.4-90075 allows remote attackers to obtain non-sensitive information.
- CVE-2026-13623 
  - Severity: Moderate
  - CVSS3 Base Score: 4.8
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:C/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:R/S:C/C:L/I:L/A:N)
  - [CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')](https://cwe.mitre.org/data/definitions/79.html)
  - An improper neutralization of input during web page generation ('Cross-site Scripting') vulnerability in Theme API in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2-72806-9, 7.3.2-86009-4 and 7.4-90075 allows remote authenticated users with administrator privileges to read or write limited files.
- CVE-2026-13666 
  - Severity: Low
  - CVSS3 Base Score: 3.5
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:U/C:N/I:L/A:N)
  - [CWE-93: Improper Neutralization of CRLF Sequences ('CRLF Injection')](https://cwe.mitre.org/data/definitions/93.html)
  - An improper neutralization of CRLF sequences ('CRLF Injection') vulnerability in Sharing API in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2-72806-9, 7.3.2-86009-4 and 7.4-90075 allows remote authenticated users to write limited files when a victim clicks a sharing URL.
- CVE-2026-13683 
  - Severity: Low
  - CVSS3 Base Score: 2.7
  - CVSS3 Vector: [CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:U/C:L/I:N/A:N)
  - [CWE-89: Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')](https://cwe.mitre.org/data/definitions/89.html)
  - An improper neutralization of special elements used in an SQL command ('SQL Injection') vulnerability in EventScheduler API in Synology DiskStation Manager (DSM) before 7.2.1-69057-12, 7.2.2-72806-9, 7.3.2-86009-4 and 7.4-90075 allows remote authenticated users with administrator privileges to obtain non-sensitive information.

**Acknowledgement**

- Lam Jun Rong (https://jro.sg)
- DungNBN (@greengrass19000) from Viettel Cyber Security Research Lab (@vcslab) working with Scamman from Trung Tâm Săn Lỗi Lậu Hải Ngoại
- Uky
- Juhyeop Lee (STEALIEN INC.) https://www.stealien.com
- Brendan O'Rourke
- WinD39 from Viettel Cyber Security (https://www.linkedin.com/in/dinh-vu-17922227a/)

**Revision**

| Revision | Date | Description | 
|---|---|---|
| 1 | 2026-09-18 |  |
