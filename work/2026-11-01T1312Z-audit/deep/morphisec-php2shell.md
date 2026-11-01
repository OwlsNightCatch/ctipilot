# extract: served via trafilatura-direct
---
title: PHP2Shell Is Hitting Windows Servers in the Wild. We Stopped It.
author: Tommy Perniciaro
url: https://www.morphisec.com/blog/php2shell-is-hitting-windows-servers-in-the-wild-we-stopped-it/
hostname: morphisec.com
description: Get expert insights into technology trends, the cybersecurity landscape and new and emerging threats.
sitename: Morphisec Inc.
date: "2026-10-28"
fingerprint: be3929d9e9a6361e
---
# PHP2Shell Is Hitting Windows Servers in the Wild. We Stopped It.

Every public exploit targets Linux. The attacks we blocked were on Windows IIS. For 110 million servers running end-of-life PHP, no patch exists. Here is what we saw, and how AMTD shut it down.

On October 21, the PHP project shipped emergency fixes for two critical memory corruption vulnerabilities in the PHP runtime: CVE-2026-109618 and CVE-2026-109619, collectively known as PHP2Shell. Both carry a CVSS 9.2 rating and allow an unauthenticated attacker to execute arbitrary code on a vulnerable web server with a single HTTP request, before any application code runs.

The security industry responded exactly as expected. Advisories from CISA, Palo Alto, CrowdStrike, Google Cloud, and Cisco all said the same thing: patch immediately.

That advice is correct. It is also, for the majority of affected servers, impossible to follow.

**100 Million Servers Will Never See a Patch**

PHP runs behind roughly 70% of the web. When the [Qualys Threat Research Unit](https://blog.qualys.com/vulnerabilities-threat-research/2026/10/20/php-announces-critical-security-release-for-two-vulnerabilities%5D) surveyed their customer base of more than 10,000 organizations, they found 167 million PHP package installations. Of those, 110 million (71%) run end-of-life PHP branches (8.1, 8.0, 7.x, 5.x) that will never receive an official vendor patch for PHP2Shell.

The PHP project released fixes for branches 8.2 through 8.5. Everything older gets source-only backports at best, and nothing for branches older than 7.4. Organizations on these versions face a harder choice than “apply the patch.” They need a full PHP version upgrade, which means application compatibility testing, dependency audits, and in many cases, a migration to an entirely new server stack. That work takes weeks or months, not hours.


Five days after disclosure, [OX Security reported](https://www.ox.security/blog/php2shell-day-5-the-panic-hasnt-turned-into-patching/) that 93.6% of the 2.2 million internet-facing PHP instances visible on Shodan were still running vulnerable versions. That number includes the supported branches where a patch exists. For the 110 million on EOL branches, that number is functionally 100%, and it will stay there.

The gap between “patch available” and “patch deployed” is where attackers operate. PHP2Shell makes that gap especially dangerous because exploitation requires no authentication, no vulnerable application code, and no user interaction. A single crafted POST request is enough.

**First Confirmed Windows Exploitation of PHP2Shell**

Most of the public discussion around PHP2Shell has focused on Linux. The original proofs-of-concept target Apache with mod\_php on Linux, and every confirmed exploitation report published to date describes a Linux environment.

The reality on the ground is different.

Morphisec has confirmed that PHP2Shell post-exploitation activity is targeting Windows servers running IIS with PHP-CGI. Our AMTD agent blocked a post-exploitation payload on a customer’s Windows server where the attack followed the now-familiar PHP2Shell chain: the IIS worker process spawned the PHP-CGI handler, which executed a command shell, which launched a packed binary that attempted to establish a reverse shell to an external command-and-control address.


Alt text: PHP2Shell attack chain observed on Windows/IIS: PHP2Shell exploit (T1190) to w3wp.exe spawning php-cgi.exe, to cmd.exe (T1059.003), to packed payload with PEB-walk shellcode (T1027.002), with the reverse shell to attacker C2 blocked by AMTD.

The attacker used shellcode injection through the PEB (Process Environment Block) to resolve and load networking libraries, then attempted to establish a reverse shell to an external server. This is textbook post-exploitation behavior: after gaining code execution through the PHP vulnerability, the attacker staged the next phase of the intrusion on the compromised Windows server.

This matters for two reasons. First, it confirms that PHP2Shell exploitation has moved beyond Linux and beyond proof-of-concept. Windows environments running IIS with php-cgi.exe are actively being targeted. Second, many of these Windows PHP deployments run older, unsupported PHP versions on older Windows Server editions, compounding the patching problem.

**What Happened, and What Morphisec Stopped**

Morphisec’s AMTD technology blocked the attack at the post-exploitation stage. When the attacker’s payload attempted to execute shellcode in memory, the morphed runtime environment caused the malicious code to fail. The shellcode targeted memory structures that AMTD had already relocated, leaving only decoy structures in their original locations. The payload landed on the decoy, failed, and was immediately trapped and logged with full forensic detail.

This is worth understanding precisely. Morphisec did not detect PHP2Shell itself. No endpoint agent can patch a PHP runtime vulnerability. What AMTD did is neutralize the attacker’s ability to do anything useful after exploiting it.

The PHP vulnerability gives the attacker code execution as the web worker process. That code execution is the beginning of the attack, not the end. To move laterally, exfiltrate data, deploy ransomware, or establish persistence, the attacker must execute additional payloads in memory. Those payloads depend on predictable memory layouts: known offsets for Windows API functions, expected locations of the PEB, reliable positions for loaded DLLs.

AMTD removes that predictability. The memory layout the payload expects does not exist. The attack fails deterministically, regardless of whether the shellcode is novel, packed, or obfuscated, and regardless of whether a signature for it exists.

**AMTD as a Compensating Control**

The conventional response to a critical vulnerability follows a predictable sequence: vendor discloses, CISA advises, security teams scramble to inventory and patch, and the organization accepts risk during the window between disclosure and deployment. For supported software with available patches, this window might last days or weeks. For end-of-life software, the window never closes.

AMTD operates independently of this cycle. It does not need to know about CVE-2026-109618 or CVE-2026-109619 to stop an attacker who exploits them. It does not need a signature for the specific shellcode the attacker uses. It does not need a patch for the vulnerable PHP version. It makes the post-exploitation step fail by making the runtime environment unpredictable to the attacker.

For the 110 million PHP installations running end-of-life versions, this distinction is critical. These servers cannot be patched in any practical timeframe. Many run legacy applications that cannot be migrated without significant investment. WAF rules and configuration hardening provide partial mitigation, but PHP’s own advisory states plainly: “there are no complete mitigations; updating is the only safe choice.”

AMTD provides a control that works while the organization plans and executes the upgrade. It does not replace patching. It makes the period between vulnerability disclosure and patch deployment survivable.

**What Organizations Should Do Now**

Hunt for prior compromise. Sophos recommends reviewing activity on exposed PHP servers from August 1, 2026 onward. Look for web server worker processes spawning command shells, unexpected outbound connections, new files in web-accessible directories, and PHP worker crashes or restarts.

**The Broader Lesson**

PHP2Shell is not the first critical vulnerability in a foundational runtime, and it will not be the last. The pattern is always the same: a flaw in something that powers a large share of the internet, a patch that reaches a fraction of affected systems, and a long tail of unpatched installations that remain exposed for months or years.

The security industry’s answer to this pattern has been “patch faster.” That advice is necessary but insufficient. Organizations that depend on legacy systems, embedded runtimes, or software they do not control need a defense that works before the patch arrives and keeps working when the patch never arrives.

AMTD is that defense. Not because it fixes vulnerabilities, but because it breaks the assumptions every post-exploitation payload makes about the environment it is running in. The vulnerability is the door. AMTD makes sure there is nothing useful on the other side.

#### Stay up-to-date

Get the latest resources, news, and threat research delivered to your inbox.
