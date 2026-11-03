# extract: served via trafilatura-direct
---
title: Progress WS_FTP flaws could allow system compromise
author: Heise Online; Dirk Knop
url: https://www.heise.de/en/news/Progress-WS-FTP-flaws-could-allow-system-compromise-11507793.html
hostname: heise.de
description: Progress reports multiple critical vulnerabilities in WS_FTP. Admins should apply updates promptly.
sitename: Heise Online
date: "2026-11-02"
categories: ['IT']
fingerprint: "92086d5fa9d17e8f"
---
# Progress WS\_FTP flaws could allow system compromise

Progress reports multiple critical vulnerabilities in WS\_FTP. Admins should apply updates promptly.

Numerous vulnerabilities put systems running Progress’s WS\_FTP at risk. The file-transfer software even has a vulnerability with the highest possible severity rating. Admins should update promptly.

Progress [published a security advisory](https://community.progress.com/s/article/WS-FTP-Server-Critical-Security-Alert-Bulletin-September-2026) over the weekend. The most serious vulnerability is insufficient authentication in WS\_FTP Server versions before 2024.0.6 and 2025.0.3 on Windows, which allows unauthenticated attackers on the network to steal sensitive information, including admin credentials ([CVE-2026-84295](https://nvd.nist.gov/vuln/detail/cve-2026-84295), CVSS **10.0**, risk “**critical**”).

The other vulnerabilities, sorted by severity:

- [OS command injection vulnerability in WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-W9JF-9HG2-6MGP) (CVE-2026-90868, CVSS **9.9**, risk “**critical**”)
- [Path traversal vulnerability in WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-P4XX-H8R7-VFH5) (CVE-2026-90866, CVSS **9.1**, risk “**critical**”)
- [Path traversal vulnerability in WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-PP85-J4V2-W38M) (CVE-2026-90864, CVSS **9.1**, risk “**critical**”)
- [Missing authorization in the administrative interface of WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-GPXJ-XCV2-8MHF) (CVE-2026-90863, CVSS **9.1**, risk “**critical**”)
- [OS command injection vulnerability in WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-4V72-8XJ2-5F6X) (CVE-2026-90865, CVSS **9.0**, risk “**critical**”)
- [Improper access control in the Web Admin console of WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-6FMF-7MQV-8MVJ) (CVE-2026-90867, CVSS **8.1**, risk “**high**”)
- [Improper limitation of pathname in the Ad Hoc Transfer component of WS\_FTP Server versions before 2024.0.6 and 2025.0.3](https://github.com/advisories/GHSA-QPHH-2FW4-CG95) (CVE-2026-84294, CVSS **7.7**, risk “**high**”)
- [Termination of the shared SSH service in WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-47X4-GRC2-RH4M) (CVE-2026-90869, CVSS **7.5**, risk “**high**”)
- [Multi-Factor Authentication bypass vulnerability in the SSH component of WS\_FTP Server versions before 2024.0.6 and 2025.0.3](https://github.com/advisories/GHSA-47GC-942J-729J) (CVE-2026-84296, CVSS **6.8**, risk **“medium**”)
- [WS\_FTP Server versions before 2024.0.7 and 2025.0.4 may expose a user’s password](https://github.com/advisories/GHSA-9RPC-QGVP-GFFM) (CVE-2026-90861, CVSS **6.6**, risk “**medium**”)
- [Improper neutralization of directives in dynamically evaluated code in the Manager web console of WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-4F4V-R2RP-777F) (CVE-2026-90872, CVSS **6.6**, risk “**medium**”)
- [Failure to release backend receiver sessions in the Ad Hoc Transfer component of WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-CQ7F-79V2-GG46) (CVE-2026-90870, CVSS **5.3**, risk “**medium**”)
- [Improper limitation of a pathname to a restricted directory in WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-8298-7W39-FVV4) (CVE-2026-90871, CVSS **5.3**, risk “**medium**”)
- [Improper authentication in the Web Transfer Module of WS\_FTP Server versions before 2024.0.7 and 2025.0.4](https://github.com/advisories/GHSA-6JV7-V4X3-VX24) (CVE-2026-90862, CVSS **4.3**, risk “**medium**”)

### Software versions with fixes

Progress describes the WS\_FTP Server 2025 updates in publicly available [release notes](https://docs.progress.com/bundle/wsftp-server-release-notes-2025/page/Whats-New-in-WS_FTP-Server-2025.html). Version 2025.0.4 has been available since Oct. 1 of this year, while version 2024.0.7 for the 2024 branch has been available since the same day.

Cybercriminals favor exploiting vulnerabilities in such file-transfer solutions to steal sensitive data and extort companies. In 2024, for example, [malicious actors exploited a vulnerability in](https://www.heise.de/news/Jetzt-patchen-Progress-MOVEit-Sicherheitsluecken-werden-bereits-angegriffen-9778266.html?from-en=1) [Progress MOVEit Transfer](https://www.heise.de/news/Jetzt-patchen-Progress-MOVEit-Sicherheitsluecken-werden-bereits-angegriffen-9778266.html?from-en=1) . A year earlier, the [Cl0p cybercrime gang stole data from many affected organizations](https://www.heise.de/news/MOVEit-Luecke-Weitere-namhafte-Opfer-der-Cl0p-Cybergang-9202121.html?from-en=1) and demanded ransom payments.

([dmk](mailto:dmk@heise.de))
