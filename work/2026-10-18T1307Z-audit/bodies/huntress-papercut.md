---
title: "PaperCut Zero-Day: Active Exploitation and Pre-Auth RCE | Huntress"
author: John Hammond; Andrew Brandt
url: https://www.huntress.com/blog/papercut-actively-exploited
hostname: huntress.com
description: "UPDATED: PaperCut NG and PaperCut MF are under active exploitation. Huntress reproduced a pre-auth RCE chain and shares urgent patching, exposure, and detection guidance."
sitename: Huntress
date: "2026-08-28"
fingerprint: bfa99df8aa0746ca
---
*Acknowledgements: Special thanks to Tanner Filip, Jai Minton, Max Rogers, Ben Nahorney, Lindsey Welch, Susannah Matt, Aaron Deal, Dray Agha, Lindon Wass, Michael Elford, and Craig Sweeney for their contributions to this investigation and writeup.* 

**Update: 9/10/26 @ 12:20 PM ET**

PaperCut has released regular maintenance releases for PaperCut NG and PaperCut MF: 26.0.5, 25.0.13, and 24.1.10. The maintenance releases replace the emergency patch builds 1, 2 and 3. If you installed an emergency patch, PaperCut recommends moving to the appropriate maintenance release.

If you have not yet patched, upgrade now and review the release notes for your product and version before proceeding.

Find the latest version for your environment on the [PaperCut product upgrade page](https://www.papercut.com/products/upgrade/).

**Update: 9/1/26 @ 8:15AM ET**

PaperCut has announced [Release 3](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/) for PaperCut NG and PaperCut MF, a third emergency patch that supersedes Release 2, meaning you do not need to install the other two releases first. If you already installed either of the original emergency patches, PaperCut recommends installing Release 3 as well. 

Along with additional hardening and mitigation, Release 3 addresses broken SAML login flows and restores support for using legacy Microsoft SQL Server drivers for external card lookup.

The PaperCut team also published a [behind-the-scenes blog post](https://www.papercut.com/blog/news/behind-the-scenes-august-security-incident/) breaking down how the incident unfolded from their perspective.

**Update: 8/28/26 @ 2:45PM ET**

PaperCut has released a second emergency patch, referred to as Release 2, for PaperCut NG and PaperCut MF. If you already installed the original emergency patch, PaperCut recommends installing Release 2 as well. Organizations should follow PaperCut's [<u>urgent security advisory</u>](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/) for the latest supported builds and installation guidance.

PaperCut has also assigned two CVEs to the vulnerabilities involved in this attack chain:

- CVE-2026-81578 is an improper access control vulnerability in the web management interface that can allow an unauthenticated attacker to modify system configurations.
- CVE-2026-82078 is an unsafe dynamic class-loading vulnerability in the database connection utilities that can be used to execute arbitrary Java bytecode.

Chained together these flaws enable pre-authentication remote code execution in the PaperCut Application Server.

## Background

On August 27, PaperCut published an [<u>urgent security advisory</u>](https://www.papercut.com/kb/Main/security-bulletin-27-aug-2026-urgent-security-advisory/) warning that a vulnerability in their print management software, PaperCut NG and MF, were being exploited in the wild. This vulnerability gives an unauthenticated attacker remote control over PaperCut's trusted configuration, which could be used to execute arbitrary Java code inside the Application Server process.

PaperCut currently treats all NG and MF versions as potentially affected, and has released emergency patches for versions 25 and 26 (version 24 fixes are still in progress). Organizations that have PaperCut NG and MF in their environment should remove public exposure immediately and apply PaperCut's emergency update for versions 25 or 26.

For version 25 on Windows, the emergency builds are:

- PaperCut NG `25.0.12.76497`
- PaperCut MF `25.0.12.76496`

Huntress has seen limited exploitation on two customer environments; post-exploitation activity included base64-encoded commands executed on the targeted server that decoded to commands (`whoami & ver`) that aimed to identify the victim's user account and operating system.

*Figure 1: A sample log entry highlighting a base64-encoded command that was executed on the targeted server. The string decodes to the commands whoami & ver.*

Huntress also reproduced a pre-authentication, remote configuration takeover and a complete remote code execution chain against a stock installation of PaperCut NG `25.0.11.75758`, the previous public version listed in PaperCut's [<u>25.0 release history</u>](https://www.papercut.com/products/ng/release-history/25-0/).

## What is the PaperCut vulnerability?

In unpatched versions of PaperCut NG and PaperCut MF, a specifically crafted request can refer to one page that is rendered for the response, and another page that owns the component or action being executed.

PaperCut's authorization check could trust the rendered page and miss the permissions required by the component behind it. We found that an unauthenticated request could be utilized in this way to make changes to the server configuration. This enables access to sensitive endpoints that can trigger unsafe actions, and ultimately lets an ill-intended actor execute any arbitrary attacked-controlled code.

## Exploitation: Huntress Observations

As of publication on August 27, Huntress has seen two instances of exploitation across our customer base. The exploitation activity that was observed during one of the incidents on August 26 was limited and lasted under two minutes in total.

In the course of the exploitation, the PaperCut server.log file was found to contain artifacts of the threat actor's exploitation attempt. There were multiple instances in the log of the base64-encoded string `d2hvYW1pICYgdmVy`, which decodes to two chained commands - `whoami & ver` - that can identify the user account and the operating system version on Windows computers.

Logs also uncovered a hex-encoded Java .class file that was delivered to the computer in the same way. The command leads to the .class file being dropped into a location relative to the PaperCut server's installation directory, inside of `lib/Udydn.class`.

*Figure 2: The large array of hexadecimal code appears in the PaperCut server's server.log file.*

When extracted from the log file, we were able to decompile the binary data using a tool called Fernflower, which revealed the source code of the .class the threat actors were executing.

*Figure 3: The Java .class file decodes data saved in the relative folder path /data/content/ and can execute it as a command and then delete the files it saves.*

This OS-agnostic .class file, when executed, can run commands under either Linux or Windows systems to profile the system and obtain a directory listing of files stored on the computer. The code wrote out this data to a file named `Udydn.out`, which it writes in a `/data/content/` path relative to the program's installation directory, and deleted afterward.

On the Windows system where this example was captured, which was running version `25.0.10.75465` of the PaperCut software, the malicious code was recovered from the file path `C:\Program Files\PaperCut MF\server\lib\Udydn.class` and another copy was found at `C:\Program Files\PaperCut MF\server\lib\Moo97.class`. Based on the code we found, the `Udydn.out` and `Udydn.cmd` files would have been stored in this same directory structure. They were not recovered from the targeted computer.

*Figure 4: The Udydn.class file deletes logs after it executes commands it extracts, then deletes itself from the filesystem.*

After exploitation, the .class file deletes its own `Udydn.out` file, as well as the server's `server.log` file. The `server.log` file recorded the execution of this code in a log line that contains the string `DB URL: jdbc:derby:memory:pwn` that immediately followed the large encoded data blob's appearance in the log. We observed `/data/internal/derby.log` was not deleted, and it contains one insightful breadcrumb:

`Booting Derby version ... on database directory`

`memory:C:\Program Files\PaperCut MF\server\data\internal\pwn`

A second log entry of booting Derby with this irregular name includes the timestamp just before code execution and acts a very high-confidence indicator of compromise.

In the second incident observed on August 27, the logs revealed another .class file payload, this time with a slightly different base64-encoded command. The base64-encoded string in this incident (`d2hvYW1pICYgdmVyICYgdGFza2xpc3Q=`) decoded to `whoami & ver & tasklist`. Here, attackers were sussing out currently running processes in addition to the account username and Windows version.

This second exploited instance was running PaperCut MF version 24.1.5.71847, and was exploited before Emergency Patch Release 2 was publicly available. While Release 2 now extends coverage to the v24 branch, **47% of the approximately 2,500 PaperCut installations Huntress tracks are running v23 or older**, for which no patch is currently available.

## Proof of Concept

Huntress has recreated a working proof of concept for the exploit chain.

From a remote host, we could trigger pre-authenticated code execution to invoke an observable `charmap.exe` process running as SYSTEM spawned under the `pc-app.exe` PaperCut Application Server.

We are currently in contact with PaperCut to coordinate on vulnerability analysis.

## What Should Impacted Organizations Do?

#### Patch PaperCut NG and MF

If you're potentially impacted by this vulnerability, apply PaperCut's emergency update for your supported version as soon as possible. PaperCut says version 24 fixes are still in progress. Organizations that cannot move to a fixed version should treat network isolation as urgent.

#### Remove Public Exposure

Restrict PaperCut Application Server web access to trusted IP addresses or place it behind a VPN or another controlled administrative path. Review why any PaperCut management interface is reachable from the internet.

#### Preserve Evidence

If the server was publicly exposed, preserve evidence before an upgrade or restart changes it. Prioritize:

- The full PaperCut `server/logs` directory and file metadata
- Current and nondefault PaperCut configuration
- Endpoint process trees where the parent execution originates from `pc-app.exe`
- Reverse-proxy, WAF, firewall, DNS, and network-flow logs
- Recent services, scheduled tasks, autoruns, and file creation on the Application Server

#### Review PaperCut's Investigation Leads

PaperCut recommends looking for:

- Suspicious post-exploitation activity involving `pc-app.exe`
- Missing, unexpectedly truncated, or deleted `server.log` files
- `ERROR No suitable driver found for jdbc:no:x`
- `ERROR DatabaseUtils - Database error looking up cardID: VALUES CAST`

Additional investigation leads include unexpected .class files under `server/lib`, matching `.cmd` or `.out` files under `server/data/content`, changes to external user-lookup configuration, and PaperCut's `pc-app.exe` or Java process spawning command shells or system-discovery utilities. The observed five-character filenames may vary.

Huntress is continuing to investigate this vulnerability and related exploitation; we will update this blog accordingly with any additional findings about post-compromise activity and other relevant developments.
