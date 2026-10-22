---
schema: 1
kind: threat
title: "JDownloader website compromise: \"Download Alternative Installer\" and Linux shell installer links pointed to malware on 6 and 7 May 2026"
headline: "JDownloader site hack repointed Windows alternative-installer and Linux shell links to malware on 6 and 7 May 2026"
summary: "Attackers exploited an unpatched flaw in the content management system of jdownloader.org, the site of the free JDownloader download manager, and from about 00:01 UTC on 2026-05-06 until the server was shut down on 2026-05-07 pointed its Windows \"Download Alternative Installer\" links and its Linux shell installer link to malicious files. The Windows files load a Python-based RAT and the Linux installer plants a SUID-root binary and a login-script persistence; anyone who ran one is advised to reinstall the operating system."
discovered_at: "2026-05-10T05:00:02Z"
event_date: 2026-05-06
run_id: 2026-05-10-001
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
regions:
  - europe
  - dach
  - global
sectors:
  - technology
entities:
  - "incident:jdownloader-supply-chain-2026"
techniques: [T1190, T1195.002, T1204.002, T1036.005, T1059.006, T1105, T1036.008, T1548.001, T1546.004, T1027]
affected_products: ["AppWork JDownloader"]
cves: []
sources:
  - url: "https://piunikaweb.com/2026/05/08/jdownloader-website-hacked-malware/"
    publisher: "PiunikaWeb"
    date: "2026-05-08"
    role: primary
  - url: "https://www.cyberkendra.com/2026/05/jdownloader-website-hacked-malicious.html"
    publisher: "CyberKendra"
    date: "2026-05-08"
    role: corroborating
  - url: "https://jdownloader.org/incident_8.5.2026.html"
    publisher: "JDownloader (incident notice)"
    date: "2026-05-07"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/"
    publisher: "BleepingComputer"
    date: "2026-05-09"
    role: corroborating
  - url: "https://securityaffairs.com/191920/malware/official-jdownloader-site-served-malware-to-windows-and-linux-users.html"
    publisher: "Security Affairs"
    date: "2026-05-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Attackers tested their approach on a low-traffic page before changing live installer links."
    publisher: "JDownloader (incident notice)"
    source_url: "https://jdownloader.org/incident_8.5.2026.html"
  - quote: "The attacker did not gain access to the underlying server stack — in particular no access to the host filesystem or broader operating-system-level control beyond CMS-managed web content."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/"
  - quote: "the devs said their website was compromised by attackers exploiting an unpatched vulnerability that allowed them to change website access control lists and content without authentication."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/"
  - quote: "According to Klemenc, the malware acts as a loader that deploys a heavily obfuscated Python-based RAT."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/"
  - quote: "If Digital Signatures shows it was signed by \"AppWork GmbH,\" then it is legitimate. However, if the file is not signed or is by a different name, it should be avoided."
    publisher: "BleepingComputer"
    source_url: "https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/"
  - quote: "Users on the r/jdownloader subreddit reported seeing strange publisher names attached to the infected downloads. These included names like Zipline LLC, The Water Team, and Peace Team."
    publisher: "PiunikaWeb"
    source_url: "https://piunikaweb.com/2026/05/08/jdownloader-website-hacked-malware/"
verification: multi-source
sourcing_note: >
  JDownloader's incident notice carries the timeline, the affected links and the channels it checked; the payload analysis is
  researcher Thomas Klemenc's (Windows) and BleepingComputer's own (Linux), and the publisher names are user reports.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-10.md
updates:
  - at: "2026-10-21T20:33:12Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The malicious links on jdownloader.org were live from about 00:01 UTC on 2026-05-06 until the server
      was shut down on 2026-05-07, not for about 48 hours, and only the Windows "Download Alternative
      Installer" links and the Linux shell installer link were affected. The vendor's notice lists
      checksums of the malicious substitutes, and the check it gives is the AppWork GmbH signature; an
      independent analyst identified the Windows payload as a loader for a Python-based RAT, while the
      Linux installer plants a SUID-root binary and a login-script persistence.
    fields: [affected_products, body, classification, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title]
---

Attackers exploited an unpatched vulnerability in the website of JDownloader, a free download manager with millions of users across Windows, macOS and Linux ([CyberKendra, 2026-05-08](https://www.cyberkendra.com/2026/05/jdownloader-website-hacked-malicious.html)), that let them change access control lists and content without authentication ([BleepingComputer, 2026-05-09](https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/)). After a test on a low-traffic page at about 23:55 UTC on 2026-05-05, they repointed the Windows "Download Alternative Installer" links and the Linux shell installer link to unrelated malicious files at about 00:01 UTC on 2026-05-06; the developers were alerted through Reddit on 2026-05-07 and shut the server down that day, and the site returned with verified links on the night of 8 to 9 May ([JDownloader](https://jdownloader.org/incident_8.5.2026.html)). The genuine installer packages were not modified, the changes stayed within the content management system without access to the host file system, and the other installers on the site, the RSA-signed built-in updater and the winget, Flatpak, Snap and Docker channels were not affected ([JDownloader](https://jdownloader.org/incident_8.5.2026.html)). The developers said the malicious Windows installers lacked a valid digital signature ([Security Affairs, 2026-05-10](https://securityaffairs.com/191920/malware/official-jdownloader-site-served-malware-to-windows-and-linux-users.html)), and users reported unfamiliar publisher names such as Zipline LLC, The Water Team and Peace Team ([PiunikaWeb, 2026-05-08](https://piunikaweb.com/2026/05/08/jdownloader-website-hacked-malware/)).

Researcher Thomas Klemenc found the Windows files to be a loader for a heavily obfuscated Python-based RAT that runs Python code delivered from its C2 servers; the Linux installer downloads an archive disguised as an SVG file, installs one of two extracted binaries as a SUID-root binary under /usr/bin, creates a persistence script under /etc/profile.d and launches a Pyarmor-obfuscated payload masquerading as a system daemon ([BleepingComputer, 2026-05-09](https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/)). An ANY.RUN analysis shows an 8-minute delay before the payload activates ([Security Affairs, 2026-05-10](https://securityaffairs.com/191920/malware/official-jdownloader-site-served-malware-to-windows-and-linux-users.html)).

**Exposure:** machines on which an installer downloaded through the "Download Alternative Installer" links or the Linux shell installer link of jdownloader.org on 6 or 7 May 2026 (UTC) was run; downloading without running, other installers from the site, in-app updates and store or package channels are not at risk ([JDownloader](https://jdownloader.org/incident_8.5.2026.html)).

**Detection:** code-signing state in process and file telemetry: a JDownloader installer that is unsigned or signed by anyone other than AppWork GmbH ([JDownloader](https://jdownloader.org/incident_8.5.2026.html)); on Linux hosts that ran the shell installer, a new script under /etc/profile.d and a new SUID-root binary under /usr/bin ([BleepingComputer, 2026-05-09](https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/)).

**Triage:** genuine JDownloader installers are signed by AppWork GmbH; the same installer unsigned or carrying another publisher's name is the substitute ([BleepingComputer, 2026-05-09](https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/)).

**Defender takeaway:** on any machine where a substitute installer ran, reinstall the operating system and change passwords for important accounts from another device, as JDownloader advises ([JDownloader](https://jdownloader.org/incident_8.5.2026.html)); machines that only took in-app or store updates need no action.

## Correction — 2026-10-21T20:33:12Z

The malicious links were live from about 00:01 UTC on 2026-05-06 until the server was shut down on 2026-05-07, and the risk window JDownloader names is 6 to 7 May, not about 48 hours to 8 May ([JDownloader](https://jdownloader.org/incident_8.5.2026.html)). JDownloader's notice lists SHA256 checksums of the malicious substitute installer files ([JDownloader](https://jdownloader.org/incident_8.5.2026.html)), and the check for a downloaded Windows installer is its signature: genuine installers are signed by AppWork GmbH, the substitutes are unsigned or carry another publisher's name ([BleepingComputer, 2026-05-09](https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/)). The Python RAT is researcher Thomas Klemenc's analysis of the Windows files; on Linux the tampered shell installer installs a SUID-root binary under /usr/bin and a persistence script under /etc/profile.d ([BleepingComputer, 2026-05-09](https://www.bleepingcomputer.com/news/security/jdownloader-site-hacked-to-replace-installers-with-python-rat-malware/)), which are the artefacts to look for on Linux hosts rather than Python child processes of a JDownloader parent. Anyone who ran a substitute installer is advised to reinstall the operating system and change important passwords from another device ([JDownloader](https://jdownloader.org/incident_8.5.2026.html)).
