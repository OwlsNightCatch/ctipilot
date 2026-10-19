---
title: "A Series of Unauthenticated Events: Chained Exploitation of Ivanti Connect Secure Zero-Days"
author: Steven Adair
url: https://www.volexity.com/blog/2026/10/13/a-series-of-unauthenticated-events-chained-exploitation-of-ivanti-connect-secure-zero-days/
hostname: volexity.com
description: Volexity has identified active in-the-wild exploitation of a vulnerability chain allowing unauthenticated remote code execution in Ivanti Connect Secure VPN devices. Ivanti has published an advisory providing upgrade instructions to customers. Systems exhibiting signs of compromise, such as attempts to move laterally originating from the ICS VPN device, should be forensically investigated to ensure no breach has occurred.In the first week of October 2026, Volexity discovered an unknown threat actor, UTA0576, abusing a zero-day exploit chain to compromise a fully patched (at the time, version 22.8R2.4) Ivanti Connect Secure (ICS) VPN appliance. This exploit chain combined an authentication bypass, a remote code execution (RCE), and a privilege escalation vulnerability to achieve unauthenticated root-level code execution. The RCE and authentication bypass vulnerabilities are tracked under CVE-2026-104935.
sitename: Volexity | Memory Forensics, Cybersecurity Threat Intelligence & Incident Response
date: "2026-10-13"
categories: ['Threat Intelligence']
fingerprint: b4b1bd11ef8ad3a1
---
Threat Intelligence

October 13, 2026

*Volexity has identified active in-the-wild exploitation of a vulnerability chain allowing unauthenticated remote code execution in Ivanti Connect Secure VPN devices. Ivanti has [published an advisory](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935) providing upgrade instructions to customers. Systems exhibiting signs of compromise, such as attempts to move laterally originating from the ICS VPN device, should be forensically investigated to ensure no breach has occurred.*

In the first week of October 2026, Volexity discovered an unknown threat actor, UTA0576, abusing a zero-day exploit chain to compromise a fully patched (at the time, version 22.8R2.4) Ivanti Connect Secure (ICS) VPN appliance. This exploit chain combined an authentication bypass, a remote code execution (RCE), and a privilege escalation vulnerability to achieve unauthenticated root-level code execution. The RCE and authentication bypass vulnerabilities are tracked under CVE-2026-104935.

Volexity identified a range of post-exploitation actions undertaken by the threat actor that targeted Active Directory credentials and secrets, including Local Administrator Password Solution (LAPS) passwords and BitLocker recovery keys. Volexity began working closely with Ivanti as soon as it suspected a vulnerability chain.

Since UTA0576 deleted evidence of exploitation from Ivanti debug logs and Linux audit logs, forensic analysis was necessary to discover how the ICS VPN appliance had been compromised. Volexity worked with Ivanti to collect memory and disk images of the impacted device along with analyzing core dumps that were generated as a result of exploitation. Volexity leveraged the core dumps and system memory collections with [Volexity Volcano](https://www.volexity.com/products-overview/volcano/) to identify and reconstruct the full exploit chain used by the threat actor. UTA0576 also passed commands and results through the exploit chain’s HTTPS requests rather than a separate command-and-control (C2) channel, with no backdoor or web shell deployed to the compromised device.

On October 5, 2026, Volexity began an investigation into suspected malicious activity at a Network Security Monitoring customer. Initial work identified an ICS VPN appliance as the root cause, and subsequent checks confirmed that the ICS VPN appliance was fully patched (22.8R2.4, Build 19097).

Volexity conducted a thorough forensic investigation and identified a zero-day exploit chain targeting the following vulnerabilities:

- An authentication bypass in ICS welcome.cgi allowing requests to be routed to arbitrary CGI files, including those protected by authentication
- A file write vulnerability in wu.cgi
- A privilege escalation vulnerability in how the ICS dsinvoked broker trusts DSCache configuration data, which enables an attacker to execute commands as root

Volexity discovered that starting on October 3, 2026, UTA0576 repeatedly exploited these vulnerabilities to compromise the ICS VPN appliance and run commands on it. With this access, the threat actor undertook the following post-exploitation actions:

- Extracted credentials stored on the ICS VPN appliance, such as domain credentials used with LDAP
- Dumped and exfiltrated limited Active Directory metadata
- Deployed a custom Kerberos tool capable of [Kerberoast](https://attack.mitre.org/techniques/T1558/003/) attacks and credential testing
- Deployed a custom Python LDAP tool to search Active Directory for LAPS local administrator passwords, BitLocker recovery keys, and password-bearing attributes via a compromised Active Directory service account
- Local DNS and host reconnaissance
- Collected ICS VPN appliance configuration data, including authentication methods
- [Password spraying](https://attack.mitre.org/techniques/T1110/003/)
- Packet capture of LDAP traffic from the compromised ICS VPN appliance
- Inspection of authentication logs to identify valid usernames

The first exploit abused by UTA0576 targets a vulnerability in how the ICS VPN appliance routes requests from front- and back-end processes to a CGI script handler. The following is a high-level overview of how this works:

- The attacker sends a network request to /dana-na/auth/url\_default/welcome.cgi.
  - This script is public and serves a login page for the ICS VPN appliance. These requests are therefore allowed without authentication.
- This network request names a different script in its headers, X-DSCGI-PATH: /home/webserver/htdocs/dana/fb/smb/wu.cgi.
  - This script is not public and executes within a trusted context on the ICS VPN appliance.
- The URL is used to determine whether the request is allowed, while the header path is used to determine the destination of the request. From this, the attacker is able to pass requests to the cgi script.

The RCE portion of the exploitation chain lies in wu.cgi and can be summarized as follows:

- UTA0576 submits a Perl script with a .zip extension to the wu.cgi upload handler.
- The handler calculates the MD5 hash of the filename supplied by the client and writes the uploaded content to /home/runtime/tmp/\<MD5(filename)>.
- Only after writing the file to disk does wu.cgi check whether it is a valid ZIP. The Perl script fails this check, causing the handler to delete it. However, the file exists on disk for a short period before that deletion.
- The attacker exploits this window by sending parallel requests with the header X-DSCGI-PATH: /home/runtime/tmp/\<MD5(filename)>, using the same technique described in the previous step to execute the uploaded script.
- The race condition is between execution and deletion: if an execution request reaches the uploaded script before wu.cgi deletes it, the attacker’s code runs. Sending several execution requests in quick succession increases the likelihood of reaching the file during this window.

During this activity, UTA0576 used this exploit to upload and execute a Perl script, which executes a Bash script that in turn executes a Python script. The Python script is delivered in a Base64-encoded, zlib-compressed format. Once the Python script is decompressed and decoded, it is executed via exec(), meaning the raw script is only ever stored in memory.

Ivanti is tracking both the RCE and authentication bypass components of this chain under CVE-2026-104935. This vulnerability was fixed in patches released on October 13, 2026.

As detailed so far, the exploit chain gives UTA0576 access to code execution in the context of the cgi-server user. The threat actor then chained a separate privilege escalation exploit to gain access to root privileges. This exploit was passed via the in-memory Python script executed by the RCE Perl script. The high-level details of this exploit are outlined below:

- ICS VPN appliances run a privileged background service named dsinvoked, which runs maintenance tasks as root on demand.
- The dsinvoked service looks up which program each task runs in DSCache, a shared ICS configuration store.
- UTA0576 patches the cgi-server process’s in-memory copy of the Ivanti library /home/lib/libdsplibs.so, allowing it to modify DSCache and reconfigure an existing maintenance task to launch the Perl interpreter instead of its legitimate script.
- The exploit code then requests that dsinvoked run the task, supplying a malicious Perl script as the argument; dsinvoked executes the script as root.
- The exploit script checks for successful root-level access by checking whether /etc/shadow is readable.
- After root-level execution has been achieved, UTA0576’s exploit script restores the in-memory DSCache entry to the legitimate, pre-exploitation script and restores the libdsplibs.so library to its pre-exploitation state.
- The exploit code then removes log entries relating to the exploitation from the following targeted Ivanti runtime and Linux audit logs:
  - /home/runtime/dlogs/debuglog
  - /var/log/audit/audit.log

For each command executed by UTA0576, the entire exploit chain is executed. The result of each command is then returned via the HTTP response. Volexity did not identify first-stage malware or web shells that would have enabled the threat actor to execute commands without re-exploiting the ICS VPN appliance.

Ivanti publishes an [Integrity Checker Tool](https://hub.ivanti.com/s/article/KB44859?language=en_US) to identify unexpected file modifications on disk. However, because this exploit chain patches library code in memory only and restores configuration store data, the tool does not detect any modifications. As such, forensic investigation is required to identify evidence of exploitation.

Ivanti is working on a fix for the privilege escalation vulnerability, and it will be included in a future release in the coming weeks.

Through forensic analysis, Volexity identified numerous post-exploitation activities undertaken by UTA0576. Volexity assesses with high confidence that UTA0576 was actively interacting with the results of their commands rather than simply executing a post-exploitation script. This is based on the diversity of approaches and commands executed.

Based on Volexity’s observations, UTA0576 primarily focused on credential theft, data exfiltration, log tampering, and network reconnaissance. Each of these is further detailed in the sections that follow.

UTA0576 gained access to Active Directory and then used this access to run queries and export results to JSON files in /tmp/ for exfiltration. Based on filenames, commands, and cleanup actions, Volexity assesses with high confidence that UTA0576 exfiltrated information that could be queried from the target’s Active Directory.

UTA0576 also used a custom LDAPv3 tool and accompanying malicious Python script, writing them to /tmp/ml.py and /tmp/rq5.py. This authenticated to an internal domain controller via LDAP using the ICS VPN appliance’s Active Directory service account and searched for high-value Active Directory attributes. These included the following:

- Windows Local Administrator Password Solution (LAPS) credentials
- BitLocker recovery information
- Active Directory attributes containing userPassword and unixUserPassword values
- Logon script paths and other user account metadata

The results of this search were written to zlib-compressed, Base64-encoded JSON files stored in /tmp/. These files were exfiltrated via the exploit channel.

Volexity identified a command that executed a packet parsing tool configured to filter for packets on TCP port 389 (commonly used for LDAP). This tool parsed a file stored at /data/.icscap/cap0. Volexity also observed logs showing that UTA0576 exfiltrated raw packet capture file data.

Volexity assesses with high confidence that UTA0576 was attempting to extract credentials from LDAP traffic by inspecting an existing packet capture file on the ICS VPN appliance. UTA0576 first attempted to parse the capture locally, filtering for TCP port 389 traffic, and then attempted to exfiltrate the first 8 KB of the file. It is worth noting that this technique was also recently used by another threat actor, which Volexity tracks as UTA0533, [who obtained root access via zero-day exploitation on SonicWall SMA VPN appliances](https://www.volexity.com/blog/2026/07/17/proxying-to-compromise-sonicwall-secure-mobile-access-0-day-exploitation/).

UTA0576 wrote /data/.icscap/h.py to disk and executed it using /home/venv3/bin/python3.6 during their operation. Analysis of h.py revealed its main functionality is to parse packet captures stored in /data/.icscap/cap\* to harvest plaintext LDAP credentials, HTTP Basic Authentication credentials, and NTLM challenge-response hashes. It prints recovered credentials and password-cracking material to standard output, allowing the attacker to collect authentication data from intercepted network traffic.

UTA0576 wrote a Python implementation of Kerberos to /tmp/mk.py and an accompanying malicious script to /tmp/rr.py. The mk.py script handles basic Kerberos tests, which rr.py used to test credentials. Volexity noted that mk.py also contained [Kerberoast](https://attack.mitre.org/techniques/T1558/003/) functionality that was not used by the rr.py script.

UTA0576 sought to exfiltrate configuration and authentication data used by the compromised ICS VPN appliance. Targeted files and directories included the following:

- /home/etc/pulse/
- /home/etc/
- /home/\*.cfg
- /home/runtime

UTA0576 also sought to parse local authentication logs to steal credentials from the compromised ICS VPN appliance. Volexity observed evidence of the following actions undertaken by the attacker:

- Attempted username extraction from log.events.vc0 with results written to /tmp/pu.txt
- Extensive grep searching for authentication events and logs

UTA0576 exfiltrated the contents of /etc/resolv.conf and ran network resolution for various internal domains belonging to the targeted organization. The threat actor then used a Python helper script, sp\_run.py, to conduct a series of password-spraying attacks against Active Directory accounts. The following files related to this activity were written to /tmp/ and exfiltrated:

- sp\_out.txt
- spray\_hits.json

Volexity’s analysis of UTA0576’s payloads recovered from the ICS VPN appliance identified several anti-forensic capabilities designed to remove evidence of exploitation, conceal privileged execution, and reduce residual artifacts:

- **Log tampering:** The payload selectively removes recent entries from /home/runtime/dlogs/debuglog and /var/log/audit/audit.log. It reads both logs, filters entries within the targeted time window, and truncates and rewrites the files with the remaining records. This preserves older entries while attempting to remove evidence of malicious activity.
- **Payload self-deletion:** The root-stage Perl payload attempts to unlink its own execution file (/home/runtime/tmp/ics-root-run-inband-\*.pl) after execution begins. The preceding Python stage also attempts to delete the script during cleanup.
- **Temporary file cleanup:** The payload removes temporary execution results (/home/runtime/tmp/ics-root-result-inband-\*) and attempts to delete the original CGI source and temporary gate file.
- **Additional script removal:** Recovered commands explicitly delete /tmp/rq5.py and /tmp/rr.py using rm -f after executing the LDAP and Kerberos helper scripts.
- **Privilege-escalation cleanup:** After obtaining root execution, the payload restores the DSCache ScriptUtil/updateOpswatSDK command to /home/bin/updateOpswatSDK.pl, removing the temporary redirection to the Perl interpreter.
- **Memory patch restoration:** The payload restores the modified instruction byte in its own process memory through /proc/self/mem, removing the temporary patch associated with the privilege-escalation mechanism. The on-disk library is not modified.
- **Output suppression:** Background cleanup processes redirect standard input, output, and error streams to /dev/null, reducing visible execution artifacts and error messages.
- **Tool masquerading and capture rotation:** The attacker used a renamed tcpdump executable (/data/.icscap/dsstatmond) and eight rotating packet-capture files. Earlier captured traffic was overwritten as the capture buffer rotated.

The recovered payloads demonstrate deliberate efforts to conceal malicious activity through selective log modification, removal of temporary execution artifacts, and restoration of altered system state. Although these capabilities are confirmed in the recovered code, the extent to which each operation completed successfully on the compromised ICS VPN appliance has not been fully established.

Volexity assesses with low confidence that UTA0576 has criminal, rather than espionage, motivations based on the target of this activity. The host used for this operation, 108.165.147\[.\]64, is an [Evoxt VPS](https://evoxt.com/) and was observed running an OpenVPN server from September 30 to October 7, 2026.

For its investigation, Volexity relied heavily on memory analysis with [Volcano](https://www.volexity.com/products-overview/volcano/) to detect and respond to this zero-day exploitation. Volcano ships with various indicators of compromise (IOCs) that can flag suspicious activity in analyzed evidence, which is summarized on the *Alerts* tab.  The following screenshot, taken directly from Volcano’s *Alerts* tab by a Volexity incident responder during the investigation, immediately shows evidence of attacker activity:

The first two alerts point directly to the network sniffer used by the exploit chain and its operator. The “Linux Socket Filters” indicator reports that dsstatmond (PID 5012) is sniffing network traffic. Given the role and network placement of the ICS VPN appliance, packets that traverse its interfaces contain a significant amount of sensitive information. Network sniffing is a common technique deployed against compromised edge and core networking devices analyzed by Volexity. In fact, the same Volcano IOC also triggers on the well-known [BPFDoor](https://attack.mitre.org/software/S1161/) because its packet sniffer leverages BPF filters.

Pivoting from the “Commands from Hidden Directories” alert brings Volcano Viewer to the process table, as shown below:

The dsstatmond process is running from a directory named .icscap for stealth, which is in fact hidden from normal file system listings. Based on the command-line parameters, the BPF/PCAP filter only records traffic on network ports used by common plaintext protocols, such as LDAP, HTTP, FTP, and telnet. Sniffing on these ports allows for direct capture of sensitive information, such as credentials, administrator commands, and file transfer contents as mentioned earlier.

Volcano also recovers files and file system activity from memory for comprehensive analysis. As shown in the following screenshot, many of the tools and exploit chain components are recoverable from memory, including output JSON files, Python scripts, and the PCAP files created by dsstatmond:

The open file descriptor path /home/root/data/.icscap/cap6 corroborates the process command line value.

These examples provide just a glimpse of how Volcano’s memory analysis capability exposes volatile artifacts – even on edge devices and *especially* when attackers are engaging in anti-forensics tactics.

In this blog post, Volexity outlined three zero-day exploits in Ivanti Connect Secure VPN appliances which, when chained together, grant unauthenticated root-privilege RCE. These exploits affect versions up to 22.8R2.4, Build 19097, which at the time of writing is the latest version. Volexity reported these exploits and their abuse to Ivanti as part of a coordinated disclosure process. Ivanti is releasing a patch for the authentication bypass and RCE vulnerability (CVE-2026-104935) on the October 13, 2026; Ivanti is working on a fix for the privilege escalation vulnerability which will be patched in a future release.

Volexity’s forensic investigation revealed that, immediately after exploiting an ICS VPN appliance, UTA0576 began conducting reconnaissance, stealing credentials, and exfiltrating data. Because the operation was detected and disrupted, the threat actor’s ultimate objectives could not be determined. However, Volexity assesses with high confidence that UTA0576’s actions signaled preparation for lateral movement and a broader compromise of the victim network.

As with many other threat actor operations Volexity has investigated in 2026, Volexity assesses with medium confidence that UTA0576 makes use of large language models (LLMs) for exploit development and post-exploitation activity. This assessment is based on the continuous use of the exploit channel to pass commands to the compromised host (rather than a simpler method such as a web shell), the repeated deployment of highly specific scripts using hardcoded credentials (rather than generic pre-built utilities), and the complexity of the exploit chain.

To generally prevent these attacks, Volexity recommends the following:

- Apply the patches for affected devices [published by Ivanti](https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935).
- Monitor for large numbers of network requests for /dana-na/auth/url\_default/welcome.cgi. Malicious requests will use a header value similar to the following:
  - X-DSCGI-PATH: /home/webserver/htdocs/dana/fb/smb/wu.cgi
  - X-DSCGI-PATH: /home/runtime/tmp/\<MD5(filename)>
- It is likely that threat actors will identify additional paths that can either be used as the URL or header target for this exploit. If possible, monitoring for mismatches between the URL path and X-DSCGI-PATH is advisable.
- Check the /tmp/ directory for evidence of post-exploitation actions.
- If you suspect your device has been compromised, conduct network and memory forensics to identify evidence of exploitation. The Ivanti Integrity Checker may not be able to identify device compromise.
- Upgrade ICS VPN appliances running any of the following versions to the newest version:
  - 25.1.1 and prior
  - 25.1.2
  - 22.8R2.4

Related indicators can be downloaded from the [Volexity GitHub page](https://github.com/volexity/threat-intel/tree/main/2026/2026-10-13%20Ivanti).

**Acknowledgements**
Volexity would like to thank its customer for their close collaboration and for permitting public sharing of investigation details.

Volexity would also like to thank Ivanti for their collaboration in investigating this vulnerability chain and for their efforts to quickly remediate the issues identified.

Volexity also thanks OpenAI for their partnership via the Trusted Access for Cyber (TAC) program. OpenAI’s cyber models have allowed Volexity to drastically reduce its analysis time when it comes to investigating exploits and other incidents of this nature.


If any organization or individual believes they may have been targeted by a similar attack, please feel free to reach out to Volexity via our [**contact form**](https://www.volexity.com/company/contact/). We would be glad to assess any potential targeting and assist in determining if such an attack may have succeeded.

*Volexity’s Threat Intelligence research, such as the content from this blog, is published to customers via its [**Threat Intelligence Service**](https://www.volexity.com/services-overview/threat-intelligence/). The activity described in this blog post was shared with Volexity Threat Intelligence customers in TIB-20261012. Related indicators were available to customers beginning on October 10, 2026.*

*If you are interested in learning more about Volexity’s services, including Threat Intelligence,Network Security Monitoring and Incident Response, or our leading memory forensics solutions, Volexity Surge Collect Pro for memory acquisition and Volexity Volcano for memory analysis, please do not hesitate to contact us.*

- Volexity has identified three zero-day exploits in Ivanti Connect Secure VPN appliances exploited by a previously unknown threat actor that Volexity tracks as UTA0576.
- This exploit chain combines authentication bypass, RCE, and privilege escalation vulnerabilities to grant unauthenticated root-level RCE. The authentication bypass and RCE vulnerabilities are tracked under CVE-2026-104935.
- UTA0576 used this access, without deploying a backdoor or web shell, to conduct post-exploitation actions.
- UTA0576 also incorporated multiple anti-forensics measures to remain undetected by the Ivanti Integrity Checker Tool.
- Forensics and network analysis are required to confirm device compromise.
