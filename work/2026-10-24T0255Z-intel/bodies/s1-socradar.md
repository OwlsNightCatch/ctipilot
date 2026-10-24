---
title: PHP2Shell Exploit Tooling Found on Exposed Attacker Server
author: ST SOCRadar Threat Intelligence Unit
url: https://socradar.io/blog/php2shell-exploit-tooling-attacker-server/
hostname: socradar.io
description: SOCRadar Threat Intelligence Unit (STRU) researchers found PHP2Shell exploit tooling on an attacker-controlled server whose working directory was exposed..
sitename: SOCRadar
date: "2026-10-22"
categories: ['Cyber Threat Intelligence']
fingerprint: bef9b797af823e8e
---
# PHP2Shell Exploit Tooling Found on Exposed Attacker Server

SOCRadar Threat Intelligence Unit (STRU) researchers found **PHP2Shell** exploit tooling on an attacker-controlled server whose working directory was exposed through an open, unauthenticated directory listing. The files show an operator turning the PHP2Shell vulnerabilities into practical attack tooling: a full remote code execution (RCE) chain built and tested in a lab, plus scripts that screen live websites for the conditions that chain depends on.

The screening reached public websites across Europe, North America, and Asia, including the United Kingdom, Finland, Poland, France, Canada, the United States, and China.

**Key Takeaways**

- **Working exploit chain:** An exposed attacker server held a lab-tested PHP2Shell exploit for PHP 8.4.26 running as Apache mod\_php, the last vulnerable 8.4 release.
- **Live target screening:** Companion scripts checked about 20 public websites for the PHP version, server setup, and session settings the exploit needs.
- **No successful exploitation observed:** None of the screened sites met the exploit’s preconditions, and the operator’s results show no shell access.
- **Configuration matters, patching decides:** Hardened production settings blocked this chain, but only updating to a fixed PHP release removes the risk.

Our main FAQ blog, [PHP2Shell (CVE-2026-109618 and CVE-2026-109619)](https://socradar.io/blog/php2shell-cve-2026-109618-cve-2026-109619/), covers the flaws, fixed versions, and remediation. To see whether a specific site still needs that fix, SOCRadar’s free [PHP2Shell Checker](https://socradar.io/free-tools/php2shell-checker) flags its exposure in seconds, with no signup, agent, or exploitation.

## How Did SOCRadar Find the Server?

The data comes from SOCRadar’s own platform. The server was one of the exposed hosts captured through **SOCRadar Threat Hunting**, and every file analyzed here was collected passively from its open directory listing.

## What the Exposed Server Held

### A Lab-Built PHP2Shell Exploit Chain

The central file, **aslr\_exploit.py**, is a Python exploit the operator labels a “one-click” PHP2Shell exploit for PHP 8.4.26 under Apache mod\_php. It works entirely over ordinary HTTP requests in three broad steps: it recycles the target’s PHP worker, leaks memory addresses through the session cookie to defeat address space layout randomization (ASLR), and then abuses PHP’s session upload progress handling to run a shell command.

The script ships with two calibration profiles, one for the official PHP 8.4.26 Apache container image and one for a custom lab build, and it defaults to a local target. That points to an operator who has tested the chain against containers they control.

### What Conditions Does the Exploit Need?

The chain depends on a debug-style setup that hardened production servers rarely use:

- **Visible errors:** PHP errors displayed to visitors.
- **Weak session settings:** Session upload progress on and session strict mode off.
- **Tight resource limits:** A very low memory limit and a single Apache worker.

Even when those conditions are met, the payload can run only a very short command, so a real attack would need a second-stage script. The mod\_php focus matches PHP’s own advisory, which rates mod\_php deployments as the highest risk.

## How Did the Operator Screen Live Websites?

Three companion scripts take the work from the lab to real websites. All of them send traffic through a rotating proxy pool hosted on the same server, switching proxies between targets.

### Fingerprinting PHP Versions and Server Setups

The first script, **php2shell\_fp.py**, works through a list of about 20 websites. It reads each site’s PHP version from the X-Powered-By and Server headers and guesses whether the site runs mod\_php based on how those headers appear together. It then sends a small multipart request with an upload-progress field and a random session ID to see whether the site echoes the session back.

### Probing for Exploit Preconditions

The second script, **deep\_probe.py**, examines 11 of those sites more closely. It requests a page designed to trigger a PHP warning to see whether errors are shown, and tries six common phpinfo paths to read settings such as the memory limit and upload progress state. It also tests 11 common parameters for file inclusion and sends an upload with a unique **MARKER\_** filename to test session injection.

### What Do the Results Show?

The saved results cover those 11 sites, which include a university, nonprofits, and small businesses across Europe, North America, and Asia. Six ran PHP 8.4 releases older than the fix, four of them on 8.4.26 itself, while the rest reported 8.3, 8.2, or end-of-life 5.6. None displayed errors, exposed a phpinfo page, revealed a file inclusion flaw, or echoed the test session, so none met the exploit’s preconditions.

**This finding concerns the operator’s PHP2Shell tooling specifically.** Other files on the same server point to unrelated intrusion activity against financial and Web3 targets.

### WordPress Follow-Up Reconnaissance

A third script, **wp\_attack.py**, turns to five of the WordPress sites. It enumerates users through the REST API and author redirects, checks for about two dozen popular plugins, lists XML-RPC methods and tests pingback, and looks for exposed debug logs.

## Assessment

- **Target CVE:** We assess with moderate confidence that the tooling targets CVE-2026-109618, based on its use of the session upload progress path and its focus on PHP 8.4.26.
- **Capability:** The operator shows strong exploit development skills, but as of October 22, 2026, we have seen no evidence of shell access on any screened site.
- **Attribution and motivation:** The operator remains unattributed. Other files on the same server target cryptocurrency and Web3 platforms, which points to financial motivation.

## The Operator’s Wider Toolset

PHP2Shell is one part of a broader operation here. As previously mentioned, other tools recovered from the same server show an operator working well beyond PHP exploitation:

- **Secret harvesting:** Pulling API keys and backend URLs out of websites’ client-side JavaScript.
- **Endpoint sweeping:** Testing web and API routes, including admin paths, for unauthenticated access.
- **Proxy rotation:** A pool of rotating proxies to spread traffic and evade rate limits and blocking.

Related artifacts on the server additionally point to web-archive reconnaissance and automated CAPTCHA solving. Taken together, the toolset points to a financially motivated actor focused on cryptocurrency and Web3 targets. This activity is separate from the PHP2Shell screening.

## What Should Defenders Do?

- **Update PHP:** Move to 8.5.12, 8.4.27, 8.3.36, or 8.2.35. Hardened settings stopped this chain, but they will not stop every variant.
- **Block and hunt the server:** Block 206.188.197\[.\]105 at the perimeter and search web and proxy logs for past connections.
- **Look for screening traffic:** Flag multipart POST requests with a PHP\_SESSION\_UPLOAD\_PROGRESS field from unfamiliar sources, especially uploads named **MARKER\_** followed by eight hex characters.
- **Harden until patched:** Keep display\_errors off, set session.use\_strict\_mode=1, disable session.upload\_progress.enabled, and remove any public phpinfo pages.
- **Stop advertising versions:** Set expose\_php=Off so the X-Powered-By header no longer reveals the PHP version scanners look for.

## Indicators of Compromise

| **Type** | **Value** | **Role** | 
|---|---|---|
| IPv4 | 206.188.197\[.\]105 | Attacker staging and operations server | 
| IPv4:Port | 206.188.197\[.\]105:9999 | Exposed operator working directory (HTTP directory listing) | 
| IPv4:Port | 206.188.197\[.\]105:8899 | Rotating proxy pool endpoint | 
| IPv4:Port | 206.188.197\[.\]105:8888 | Out-of-band interaction listener | 
| Upload filename | MARKER\_\[8 hex characters\].txt | Session injection screening probe | 
| Session ID prefix | fprint, dp | Upload-progress screening probes | 

## MITRE ATT&CK Mapping

| **Tactic** | **Technique** | **ID** | **Observed Behavior** | 
|---|---|---|---|
| Resource Development | Develop Capabilities: Exploits | [T1587.004](https://attack.mitre.org/techniques/T1587/004/) | Built and lab-tested a PHP2Shell RCE chain | 
| Reconnaissance | Gather Victim Host Information: Software | [T1592.002](https://attack.mitre.org/techniques/T1592/002/) | Read PHP and server versions from response headers | 
| Reconnaissance | Active Scanning: Vulnerability Scanning | [T1595.002](https://attack.mitre.org/techniques/T1595/002/) | Probed sites for upload-progress behavior, exposed errors, phpinfo pages, and file inclusion | 
| Command and Control | Proxy | [T1090](https://attack.mitre.org/techniques/T1090/) | Routed screening traffic through a rotating proxy pool | 
| Initial Access | Exploit Public-Facing Application | [T1190](https://attack.mitre.org/techniques/T1190/) | Exploit built for internet-facing mod\_php servers; no successful use observed |
