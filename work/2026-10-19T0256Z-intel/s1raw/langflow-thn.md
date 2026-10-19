---
title: Langflow's Critical Authenticated RCE Flaw Targeted in 1,423 Honeypot Exploit Attempts
author: The Hacker News
url: https://thehackernews.com/2026/10/langflows-critical-authenticated-rce.html
hostname: thehackernews.com
description: Honeypots logged 1,423 attempts to exploit a critical Langflow flaw that lets authenticated users execute server commands.
sitename: The Hacker News
date: "2026-10-15"
categories: ['Article']
fingerprint: fb3995b1fb34b6b3
---
Threat actors are exploiting a critical security flaw in Langflow, according to an [alert](https://previdian.com/CVE-2026-105740#telemetry) from Previdian.

Langflow is an open-source platform that allows developers to build artificial intelligence (AI) applications and agentic workflows. In February 2025, DataStax, the parent company of Langflow, was [acquired](https://www.langflow.org/blog/big-news-for-langflow/) by IBM.

The vulnerability in question is **CVE-2026-105740** (CVSS score: 9.9), a case of authenticated remote code execution impacting versions prior to 1.9.0.

"Any authenticated Langflow user can achieve Remote Code Execution (RCE) on the server by adding an MCP server with the 'stdio' transport," reads an advisory [released](https://github.com/langflow-ai/langflow/security/advisories/GHSA-7w94-79vh-5mr2) last month.

"The user-supplied command field is passed directly to bash -c "exec {command}" with zero validation, no allowlisting, and no sandboxing. The command executes immediately when the server list is fetched. Additionally, the env field allows arbitrary environment variable injection (e.g., LD\_PRELOAD, PATH override)."

The crux of the vulnerability is that Langflow accepts a user-provided command without restricting it to approved executables. This, in turn, can lead to shell execution.


In a hypothetical attack scenario, a bad actor can exploit the flaw in the following fashion -

- Login as a regular, non-admin user.
- Add a malicious MCP server by sending a crafted HTTP POST request to "/api/v2/mcp/servers/{server\_name}" with a command field containing a malicious payload (e.g., a reverse shell).
- The server accepts and stores the attacker-supplied "command" without any validation.
- Trigger the flaw by fetching the MCP server list via an HTTP GET "/api/v2/mcp/servers?action\_count=true" request, causing the command to execute.
- Achieve code execution.

"Any authenticated Langflow user (including non-admin accounts) can execute arbitrary OS commands on the server with the privileges of the Langflow process," Langflow warned.

Successful exploitation can result in full server compromise, environment variable injection, facilitate lateral movement, and the deployment of a persistent backdoor, as the malicious MCP server configuration persists and re-executes every time the server list is loaded.

"Unlike custom component code which is visible in the flow editor, MCP server configs are stored in project settings and are not visible during normal flow review," Langflow said.

Data from Previdian shows that 1,423 exploitation attempts have been recorded against its honeypot sensors since September 19, 2026, from 27 unique attacker IP addresses located in Belgium, China, Germany, Hong Kong, Japan, Nigeria, the Philippines, Russia, Seychelles, Singapore, South Korea, Taiwan, Tanzania, the U.S., and Vietnam.

The exploitation efforts ramped up starting October 11, 2026, when 333 attempts were registered. As of writing, 66 attempts have been observed on October 15, 2026.

"We've investigated how attackers are authenticating, as this vulnerability requires authentication," Ryan Dewhurst, founder and CEO of Previdian, told The Hacker News.

"In one observed sequence, attackers checked the Langflow version, attempted /api/v1/auto\_login (which returned 403 as it was disabled in our honeypot), and then successfully authenticated using a common username and password. They immediately used the resulting bearer token to access the vulnerable MCP server configuration endpoint."

Some of the captured payloads include -

- Attempts to extract environment variables and sensitive Langflow configurations, including LANGFLOW\_SECRET\_KEY and LANGFLOW\_SUPERUSER\_PASSWORD, and transmit them to 146.70.211\[.\]112:18764.
- Docker commands attempting to access the host filesystem and read the contents of "/etc/passwd."
- Command execution probes using id, whoami, and other simple commands.

A significant chunk of the activity originates from the IP address "192.255.229\[.\]92," which has been observed attempting to extract environment variables. Data from GreyNoise and Previdian [shows](https://viz.greynoise.io/ips/192.255.229.92) that the IP address has engaged in generic brute-force attacks, as well as exploiting other flaws in Flowise ([CVE-2026-69255](https://github.com/FlowiseAI/Flowise/security/advisories/GHSA-vmv7-4m6c-3cg5)) and Langflow ([CVE-2026-55255](https://thehackernews.com/2026/07/cisa-adds-4-actively-exploited-adobe.html), [CVE-2026-9198](https://thehackernews.com/2026/08/cisa-flags-langflow-rce-tomcat-and-n.html), and [CVE-2026-0768](https://thehackernews.com/2026/09/attackers-exploit-critical-langflow-and.html)).

The targeting of multiple Langflow vulnerabilities points to an unknown threat actor systematically targeting exposed instances. Their end goals are currently unclear.

"We recommend upgrading Langflow to a patched version, disabling auto-login, enforcing strong and unique passwords, and reviewing authentication logs and requests to /api/v2/mcp/servers/ for suspicious activity," Dewhurst said.

Last month, Langflow addressed another critical operating system command injection vulnerability ([CVE-2026-105697](https://github.com/langflow-ai/langflow/security/advisories/GHSA-w794-rj3p-xv45), CVSS score: 9.9) that could also result in arbitrary code execution through MCP stdio server configuration. It has been patched in Langflow version 1.10.3.

If immediate patching is not an option, it's advised to set LANGFLOW\_AUTO\_LOGIN=false, avoid exposing Langflow directly to untrusted networks, and grant Langflow accounts to trusted users.

### Update

The total number of exploitation attempts has jumped to 1,706 and now originates from 28 unique IP addresses. On October 15, 2026, a total of 316 attempts were recorded.

[Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ),
