---
title: "QNAP Security Notice: Plex Media Server Vulnerabilities (Plex2Shell) – Update to 1.43.3.10861 or Later Immediately"
author: QNAP Systems; Inc
url: https://www.qnap.com/en/security-news/2026/qnap-security-notice-plex-media-server-vulnerabilities-plex2shell-update-to-1-43-3-10861-or-later-immediately
hostname: qnap.com
description: Taipei, Taiwan, November 6, 2026 – QNAP® Systems, Inc., a leading innovator in storage, networking, and data protection solutions…
sitename: QNAP Systems, Inc. - Network Attached Storage (NAS)
date: "2026-11-06"
fingerprint: b57fb4529db34b85
---
# QNAP Newsroom

Keep up to date with the latest QNAP news, awards and connect with our team

## QNAP Security Notice: Plex Media Server Vulnerabilities (Plex2Shell) – Update to 1.43.3.10861 or Later Immediately

**Taipei, Taiwan, November 6, 2026 –** QNAP® Systems, Inc., a leading innovator in storage, networking, and data protection solutions, today issued a security notice regarding "Plex2Shell", a set of vulnerabilities in the third-party application Plex Media Server. Plex has confirmed that these vulnerabilities are being actively and widely exploited. Plex Media Server 1.43.3 (1.43.3.10861 and later), which contains the fix, is available in the QNAP App Center. The vulnerabilities reside in Plex Media Server; QNAP operating systems such as QTS and QuTS hero are not themselves affected. QNAP urges all users running Plex Media Server on a QNAP NAS to update immediately and to review their devices as described below.

**About the vulnerabilities**

Plex has disclosed four vulnerabilities in Plex Media Server 1.43.2 and earlier (CVE-2026-96652, CVE-2026-96654, CVE-2026-96655, and CVE-2026-96656), collectively known as "Plex2Shell". Each presents limited risk on its own, but chained together they allow an unauthenticated remote attacker to execute arbitrary code with the privileges of the Plex Media Server process. According to Plex, a public proof of concept was released on October 16, and internet-facing servers that have not been updated have since been subject to widespread attacks; compromised servers have been used to run cryptocurrency miners and proxy software.

**What QNAP has observed**

QNAP has received reports from some users that Plex Media Server on their NAS appears to have been compromised through these vulnerabilities, and QNAP Technical Support is assisting the affected users. The QNAP Product Security Incident Response Team (QNAP PSIRT) has confirmed that the vulnerabilities exist only in Plex Media Server; QTS, QuTS hero, and other QNAP operating systems are not themselves affected.

**Recommended actions**

- **Update now.** Go to App Center > My Apps and update Plex Media Server to 1.43.3 or later, then confirm in Plex Web under Settings > General that the version is 1.43.3.10861 or later. Later Plex releases will also be made available once verified. Do not wait for them – update now.
- **If Plex was reachable from the Internet, treat the NAS as potentially compromised.** If, while running 1.43.2 or earlier, Plex on your NAS could be reached from the Internet (for example, Plex Remote Access was enabled, port 32400 was forwarded, or the port was opened automatically through UPnP or router auto-configuration), updating alone will not remove anything an attacker may have installed. Follow the FAQ to perform a clean reinstall, check for indicators of compromise, and reset your Plex and NAS credentials.
- **Reduce exposure.** If you do not need remote access to Plex, disable Plex Remote Access and do not forward port 32400. If you do need remote access, use a VPN instead. Also make sure QTS or QuTS hero and all installed apps are up to date.

Step-by-step instructions are available in the FAQ: [Plex2Shell: Check and Remediation FAQ for QNAP NAS Users](https://www.qnap.com/go/how-to/faq/article/plex2shell-check-and-remediation-faq-for-qnap-nas-users)

**Need help?**

If you suspect your device has been compromised and would like QNAP to help confirm it, preserve the Plex Logs folder before removing Plex Media Server, then open a case with QNAP Technical Support. QNAP remains in contact with Plex and will update this notice as new information becomes available.

**Related information**

- Plex security announcement (CVE details and exploitation notes): Important Security Update for Plex Media Server v1.43.2 and earlier – [https://forums.plex.tv/t/important-security-update-for-plex-media-server-v1-43-2-and-earlier/942319/3](https://forums.plex.tv/t/important-security-update-for-plex-media-server-v1-43-2-and-earlier/942319/3)
- QNAP Technical Support: [https://service.qnap.com/](https://service.qnap.com/)

### About QNAP

QNAP delivers integrated technology solutions through software innovation, hardware craftsmanship, and in-house manufacturing. With strengths in storage, networking, and smart video surveillance, QNAP also integrates cloud services to enhance data safety, intelligence, and workflow efficiency. We envision the NAS as a core platform unifying high availability, cybersecurity, edge AI, IT/OT resilience, and cloud management—empowering organizations across industries to stay competitive in a rapidly evolving digital world.
