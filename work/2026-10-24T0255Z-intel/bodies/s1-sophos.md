---
title: Proof-of-concept exploit released for PHP vulnerabilities (CVE-2026-109618, CVE-2026-109619)
author: About the Author
url: https://www.sophos.com/en-us/blog/proof-of-concept-exploit-released-for-php-vulnerabilities-109618-109619
hostname: sophos.com
description: The vulnerabilities have been identified as critical (CVSS score of 9.2)
sitename: SOPHOS
date: "2026-10-21"
fingerprint: b4d8efd32f879506
---
**October 23 19:31 UTC: Full list of Sophos countermeasures**

In response to requests, this update consolidates the Sophos countermeasures that relate the PHP2Shelll vulnerabilities.

SophosLabs has developed the following countermeasures to specifically detect activity associated with this threat.

| Name | ID | Platform | 
| SERVER-WEBAPP PHP serialized integer key collision remote code execution attempt | 67359, 67360, 67375 | Sophos Firewall IPS | 
| PHP2Shell CVE-2026-109618 / CVE-2026-109619 Remote Code Execution Vulnerabilities | 213184, 213185, 213187, 213188, 213189 | Sophos Firewall IPS, Endpoint IPS | 
| VID444662 Unusually Long Filename in HTTP POST Request Body Detected - Inbound (CVE-2026-109618 CVE-2026-109619) - PHP2Shell | 62983 | iSensor | 
| VID444662 PHP Code Injection via Filename Parameter Detected - Inbound (CVE-2026-109618 CVE-2026-109619) - PHP2Shell | 62986 | iSensor | 
| VID444662 PHP RCE via OOM Corruption Attempt Detected - Inbound (CVE-2026-109618) - PHP2Shell | 62988 | iSensor | 

The next table lists additional pre-existing Sophos countermeasures that will likely address post-exploitation activity associated with these vulnerabilities.

| Name | ID | Platform | 
| Webshell Postexploitation Activity | Not applicable | Sophos Protection for Linux | 
| Ingress Tool Transfer | Not applicable | Sophos Protection for Linux | 
| Suspicious Interactive Shell | Not applicable | Sophos Protection for Linux | 
| Advanced Webshell Detection (optional coverage) | Not applicable | Sophos Protection for Linux | 
| Compromised Web Server (optional coverage) | Not applicable | Sophos Protection for Linux | 
| Php-cgi.exe launching suspicious process through IIS | Access\_1b | Sophos Endpoint and Server Protection (Windows) | 
| Malicious child-process activity involving cmd.exe, powershell.exe or certutil.exe in a covered PHP server process chain | Access\_3b | Sophos Endpoint and Server Protection (Windows) | 
| WIN-DET-PERSIST-WEBSHELL-W3WP-SUSP-CHILD-1 | Not applicable | Sophos XDR | 
| WIN-DET-T1190 | Not applicable | Sophos XDR | 
| WIN-CAC-PSH-WEBCLIENT-UPLOAD-1 | Not applicable | Sophos XDR | 
| WIN-DIS-PRC-SUSP-WEB-SERVER-1 | Not applicable | Sophos XDR | 
| WIN-DIS-PRC-SUSP-WEB-SERVER-1-LOW | Not applicable | Sophos XDR | 
| WIN-EXE-PRC-PHP-EXE-IN-SUSPICIOUS-PATH-1 | Not applicable | Sophos XDR | 
| WIN-EXE-PRC-PHP-EXE-IN-SUSPICIOUS-USERS-PATH-1 | Not applicable | Sophos XDR | 
| WIN-EXE-PRC-PHP-EXE-IN-SUSPICIOUS-USERS-PATH-1-HIGH | Not applicable | Sophos XDR | 
| WIN-EXE-PRC-RENAMED-PHP-EXE-1 | Not applicable | Sophos XDR | 
| WIN-PER-PRC-WEBSHELL-SPAWN-SUS-PROCESS-1 | Not applicable | Sophos XDR | 
| UNX-CAC-PRC-PARENT-WGETPHP-DOWNLOAD-1 | Not applicable | Sophos XDR | 
| UNX-CAC-PRC-PHP-REVERSE-SHELL-1 | Not applicable | Sophos XDR | 
| PHP-CGI Remote Code Execution | Not applicable | Taegis/Fusion XDR | 
| PHP-CGI Exploitation | Not applicable | Taegis/Fusion XDR | 
| RESEARCH: PHP-CGI Exploitation 3 | Not applicable | Taegis/Fusion XDR | 
| RESEARCH: PHP-CGI Executes Multiple Discover Commands | Not applicable | Taegis/Fusion XDR | 
| Potential PHP-FPM Exploit Command Line Activity | Not applicable | Taegis/Fusion XDR | 
| RESEARCH: PHP or Java Process Downloading via Wget or Curl | Not applicable | Taegis/Fusion XDR | 
| PHP Web Shell Executing Command | Not applicable | Taegis/Fusion XDR | 
| PHP Web Shell Activity | Not applicable | Taegis/Fusion XDR | 

**October 23 15:35 UTC: Note about additional PHP vulnerability and new PHP2Shell countermeasures**

On October 23, PHP released an [informational advisory](https://www.php.net/) disclosing another remote code execution vulnerability ([CVE-2026-115560](https://nvd.nist.gov/vuln/detail/cve-2026-115560)). The advisory states that the issue requires “an unusual combination of configuration and application code” and that [mitigations](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp) published for PHP2Shell vulnerability CVE-2026-109619 also address this threat. Sophos will continue to monitor the vulnerability and will release updated information and additional countermeasures as appropriate.

SophosLabs has also released additional PHP2Shell countermeasures, specifically Sophos Firewall and Endpoint IPS signatures 213184, 213185, 213187, 213188, and 213189.

**October 22 21:21 UTC: Correction and new insights, countermeasures, and indicators**

The previous update (October 22 16:18 UTC) reported that Sophos observed successful exploitation of PHP2Shell in customer environments. Upon further analysis, we are correcting that assessment as Sophos customer telemetry shows scanning and a small number of failed exploitation attempts. As of this update, there is no evidence of a successful compromise due to these vulnerabilities.

The payload, a likely Mirai botnet variant known as Potassium, was not delivered since the exploitation attempt was unsuccessful due to being blocked by Sophos countermeasures. However, analysis of the sample revealed that is an updated and significantly expanded version of the Mirai-derived botnet variant identified in early 2026. The sample displays downloader and network disruption functionality. It resolves a hard-coded, encrypted C2 address; establishes a TCP connection to 134\[.\]199\[.\]154\[.\]64; and sends an HTTP request. It checks for an HTTP 200 response status and verifies that the resulting payload begins with the ELF magic bytes 7F 45 4C 46, indicating that it expects to retrieve a Linux ELF follow-on payload. A resolver function supports IPv4 addresses and hostname resolution, with additional fallback resolution logic that includes hard-coded public DNS servers such as 8.8.8.8, 1.1.1.1, and 1.0.0.1. As with Mirai malware historically, this sample can execute DDoS attacks.

Sophos analysis of the vulnerabilities suggests that developing a successful exploit is not straightforward. The Sophos Adversary Group has been attempting to produce a successful exploit, which is proving challenging even with AI support. The lack of successful exploits in the wild suggests threat actors are also struggling. Security researchers have claimed they have developed successful exploits, but it is possible these only work in lab scenarios rather than real-world environments. Successful exploitation may also require certain dependencies or configurations. Despite the low level of activity, the vulnerabilities remain serious. Given time, threat actors may develop successful exploits. Urgent patching remains the primary recommendation.

The following new Sophos countermeasures relate to this threat:

- Sophos Firewall IPS signatures 67359, 67360, 67375, 2313184, 2313185, 2313187 and 2313188
- Sophos Endpoint IPS signatures 2313184, 2313185, 2313187, 2313188 and 2313189

These join existing Sophos endpoint XDR, Taegis XDR, Windows Behavioral Protection, and Linux Runtime Detection rules.

CTU researchers also associate the additional indicators in the following table with this activity. IP addresses can be allocated. The domains and IP addresses may contain malicious content, so consider the risks before opening them in a browser.

| **Indicator** | **Type** | **Context** | 
| 134\[.\]199\[.\]154\[.\]64 | IP address | C2 server for Potassium, a likely Mirai variant | 
| 117\[.\]55\[.\]202\[.\]115 | IP address | C2 server for Potassium, a likely Mirai variant | 
| hackattackkaboom\[.\]botlesscucks\[.\]st | Domain name | Malware staging server used by PHP2Shell-related payload | 
| hik\[.\]gettingheadfromduckysmom\[.\]st | Domain name | Potassium infrastructure embedded in PHP2Shell-related payload | 

**October 22 16:18 UTC: Sophos observations, exploitation activity, countermeasures, and indicators**

These two vulnerabilities are now widely referred to as “PHP2Shell”. Proof-of-concept exploit code is publicly available, and Sophos threat hunters have identified multiple exploit attempts consistent with PHP2Shell activity and one successful exploitation. While Sophos analysis have concluded that exploitation of these vulnerabilities is viable, successful follow-on remote code execution depends on deployment architecture, PHP version, and configuration. As of this update, Sophos analysts have not observed evidence linking the activity to ransomware deployment, data theft, or supply chain compromise.

In activity observed by Sophos threat hunters, activity originated from IP address 45\[.\]198\[.\]224\[.\]169 and delivered a payload that appears to be a Mirai variant known as Potassium. The traffic included a User-Agent string that referenced scanning activity, a multipart boundary string, and a distinct POST request pattern. The activity resulted in a payload being written to /tmp/nfs and executed as ./nfs php.

The following threat indicators were observed by Sophos analysts.

| Indicator | Type | Context | 
| 45\[.\]198\[.\]224\[.\]169 | IP address | Source of PHP2Shell exploit attempt | 
| 92\[.\]118\[.\]112\[.\]100 | IP address | Hosting payload associated with PHP2Shell exploitation activity | 
| hxxp://92\[.\]118\[.\]112\[.\]100/nfs | URL | Location of payload associated with PHP2Shell exploitation activity | 
| thunder\[.\]godofthunder\[.\]st | Domain name | Contacted by PHP2Shell-related malware sample during sandbox analysis | 
| b61a098fc62a2c2696e196dca78da71a | MD5 hash | Likely Mirai variant downloaded in PHP2Shell exploitation | 
| c472dab4ff7c16782a8037f988d4daa6d4bdb343 | SHA1 hash | Likely Mirai variant downloaded in PHP2Shell exploitation | 
| 0c5486f06620e26e316f4b33f318b0d646d5e1133789331aa2fed012360d1486 | SHA256 hash | Likely Mirai variant downloaded in PHP2Shell exploitation | 
| /tmp/nfs | File path | Location on compromised system where PHP2Shell exploit drops payload | 
| ./nfs php | Command | Used to execute PHP2Shell payload | 
| php2shell-scan/109618 | User-Agent | Observed in PHP2Shell exploit traffic | 
| B7kQpoc618 | String | Multipart boundary observed in PHP2Shell exploit request | 

The following Sophos countermeasures relate to activity associated with PHP2Shell:

- UNX-CAC-PRC-PARENT-WGETPHP-DOWNLOAD-1
- UNX-CAC-PRC-PHP-REVERSE-SHELL-1
- WIN-CAC-PSH-WEBCLIENT-UPLOAD-1
- WIN-DIS-PRC-SUSP-WEB-SERVER-1
- WIN-DIS-PRC-SUSP-WEB-SERVER-1-LOW
- WIN-EXE-PRC-PHP-EXE-IN-SUSPICIOUS-USERS-PATH-1-HIGH
- WIN-PER-PRC-WEBSHELL-SPAWN-SUS-PROCESS-1

**October 21 17:01 UTC: Monitoring for signs of exploitation**

The following behaviors and changes may indicate exploitation of these vulnerabilities:

- Network sessions that last longer than usual (Applications running on the PHP service should have a standard pattern of network connections.)
- Unusual process names (including misspellings of legitimate names), or seemingly legitimate processes in unexpected locations
- Unusual and low-volume inbound traffic from low-reputation infrastructure

**October 21 14:28 UTC: Revised version of the original advisory (published at approximately 12:55 UTC) following PHP’s release of updates and additional details**

## Overview

On October 20, 2026, PHP announced an upcoming security release to address two critical (CVSS score of 9.2) vulnerabilities. Third-party sources [identified](https://cyberplace.social/@GossiTheDog/117474220875882526) the vulnerabilities as [CVE-2026-109618](https://nvd.nist.gov/vuln/detail/cve-2026-109618) and [CVE-2026-109619](https://nvd.nist.gov/vuln/detail/cve-2026-109619). According to [reports](https://www.bleepingcomputer.com/news/security/php-warns-admins-of-two-critical-flaws-emergency-patches-coming-tomorrow/), the issues impact multiple PHP versions and allow for remote code execution.

On October 21, PHP [released](https://www.php.net/archive/2026.php#2026-10-21-5) updated versions to address these issues and stated that “all PHP installations serving web requests” are at risk. A user on the X platform [claims](https://x.com/J4ck3LSyN/status/2112703096443097263) to have created a working proof-of-concept exploit. As of this publication, active exploitation has not been reported in the wild.

## Recommended actions

Counter Threat Unit™ researchers recommend that customers identify potentially vulnerable systems and upgrade as appropriate. In the interim, organizations should consider taking internet-facing PHP-powered systems offline if feasible or putting them behind network-layer authentication (e.g., ZTNA). Additionally, network defenders should evaluate the potential for exploitation in their environment and monitor for suspicious activity. The PHP advisory lists mitigations for organizations who cannot immediately upgrade but notes that updating is the only complete solution.

## Sophos countermeasures

SophosLabs continues to monitor the threat landscape for activity related to these vulnerabilities and will deliver detections and protections as available. An internal [investigation](https://www.sophos.com/en-us/security-advisories/sophos-sa-20261021-php2shell) is also underway to determine if Sophos products or services are affected.
