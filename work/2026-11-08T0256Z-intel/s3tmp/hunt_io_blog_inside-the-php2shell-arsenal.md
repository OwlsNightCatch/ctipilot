---
title: "Inside the PHP2Shell Arsenal: A Complete Dissection of a PAN-OS Mass-Exploitation Open Directory"
url: https://hunt.io/blog/inside-the-php2shell-arsenal
hostname: hunt.io
description: An exposed open directory revealed a full PAN-OS attack toolkit that chained PHP RCE with a kernel LPE to root 25 Palo Alto firewalls across the US and Korea.
sitename: Hunt Intelligence
date: "2026-11-03"
fingerprint: b5d1d8952ce992c4
---
Inside the PHP2Shell Arsenal: A Complete Dissection of a PAN-OS Mass-Exploitation Open Directory

Published on

In our previous research, [Hunting Leaked PHP2Shell RCE Across Open Directories](https://hunt.io/blog/php2shell-cve-2026-109618-109619-open-directories) examined the exposure of **CVE-2026-109618** and **CVE-2026-109619**, uncovering attacker tooling and early exploitation attempts. We followed up in [PHP2Shell One Week Later: Honeypot Shells on the Web, a Path to Root on Palo Alto Firewalls](https://hunt.io/blog/php2shell-honeypot-shells-root-palo-alto-firewalls), documenting confirmed honeypot activity and production compromises involving Palo Alto firewalls. Building on these findings, this post breaks down the Palo Alto exploitation.

Our [AttackCapture™](https://hunt.io/features/attackcapture) platform identified an open directory at [130.94.67\[.\]235:8080](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.67.235:8080) containing a fully operational **PAN-OS exploitation toolkit**. The analysis reveals an entire campaign lifecycle including internet-wide reconnaissance of **19,182 management portals**, a chained PHP memory corruption and kernel-level privilege escalation exploit, **25 confirmed root compromises** across major US and South Korean organizations including lateral pivots to Panorama and managed firewall infrastructure, and a deep post-exploitation playbook targeting Active Directory, GlobalProtect VPN, and Keycloak SSO infrastructure.

Here is what we found inside.

## Key Takeaways

- A four-stage exploit chain achieves root-level access on PAN-OS firewalls through a single unauthenticated HTTP request, combining PHP **session.upload\_progress** memory corruption with the **Fragnesia kernel LPE (CVE-2026-46300)**.
- The exploitation logs across document root access on **25 appliances (18 US, 6 South Korea, 1 internal pivot)**, including lateral movement to a Panorama management server and a managed next-generation firewall within the same enterprise.
- FOFA-based internet-wide reconnaissance of **19,182 PAN-OS management portals**, version-calibrated target lists, reverse SSH tunnel infrastructure, SOCKS5 proxy pivots, AD/LDAP reconnaissance, **GlobalProtect authentication bypass (CVE-2026-0257)**, and automated persistence and recovery scripts.
- The operator deployed a multi-agent AI penetration testing platform (aiscan) powered by **DeepSeek v4-pro**, **DeepSeek v4-flash**, and **Kimi k3**.
- A 4.6 MB session log captures the aiscan AI (DeepSeek v4-pro) autonomously reading 22 offensive playbooks, downloading 17 security tools, and verifying operational readiness in under nine minutes. Anthropic's Claude Code was also installed on the same VPS, though the capture shows no evidence it was used in the attack.
- Automated health monitoring, crash recovery scripts, and multi-layer boot persistence (systemd, rc.local, preserved health endpoints) indicate a sustained campaign designed to survive appliance reboots and firmware updates.

## Discovery: The Open Directory

On October 24, 2026, our platform flagged an open HTTP file server on port 8080 at [130.94.67\[.\]235](https://portal.hunt.io/ip/130.94.67.235). The host resolves to [AS154177](https://portal.hunt.io/asn/AS154177) (LIGHT NODE LIMITED), a Tokyo-based VPS provider. Services were observed on ports 22 (SSH), 80, 443, and 8080, with the file server exposing the root home directory of a Linux system containing the operator's complete working environment.

The exposed [open directory](https://hunt.io/glossary/open-directories) at [130.94.67\[.\]235:8080](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.67.235:8080) includes over 80 Python scripts, shell scripts, and configuration files, along with binary tools, CSV datasets containing the results of internet-wide scanning campaigns, exploitation logs, and Active Directory reconnaissance output.

Our analysis exposes the full operational infrastructure, including the reconnaissance pipeline, version-calibrated exploitation batches, post-exploitation tooling for lateral movement and persistence, and authentication bypass utilities for **GlobalProtect VPN**.

It also contains a complete AI-powered offensive security platform (aiscan) with a 4.6 MB session log that captures a DeepSeek large language model autonomously reading **22 offensive skill files**, downloading **17 security tools**, and preparing for AI-driven penetration testing, alongside a separate installation of **Anthropic's Claude Code** on the same VPS.

## The Exploit Chain: From HTTP Request to Root Shell

The toolkit's central component is a **four-stage exploit chain** that achieves root-level command execution on **PAN-OS appliances** through a single unauthenticated interaction with the management interface. No credentials, no authentication tokens, and no prior access are required. The operator's own documentation (a detailed **README.md** included in the toolkit) describes the route with precision.

The chain operates as follows.

### Stage 1: PHP Memory Corruption (RCE as nobody)

The initial entry point exploits a heap corruption vulnerability in PHP's **session.upload\_progress** handler as exposed through PAN-OS's management web interface. The core exploit logic resides in **panos\_rce\_poc.py**, which orchestrates the entire four-stage chain from a single invocation.

Our analysis confirms three auxiliary scripts found in the open directory linked with the primary exploit. The **precon.py** script performs pre-exploitation reconnaissance to fingerprint the target's PAN-OS and PHP versions before taking any destructive action. The **prce.py** encapsulates the PHP RCE primitives used during the memory corruption sequence, and **p121.py** is a compatibility front-end that adapts the exploit for PAN-OS 12.1.x-specific memory layouts and offsets.

These **four** scripts implement the following sequence of HTTP requests that manipulate PHP's internal memory structures:

1. **The warm-up phase** primes the PHP process memory layout through controlled allocations.
2. **A1 (OOM trigger)** forces an out-of-memory condition that induces a use-after-free on internal zend\_reference structures.
3. **B1 (pointer leak)** extracts the base address of libphp from the server's Set-Cookie response header, defeating ASLR.
4. **A2 (stale reference)** crafts a dangling zend\_reference pointing to attacker-controlled memory.
5. **B2 (command execution)** constructs a fake HashTable with its pDestructor field set to the address of zif\_system, causing PHP's internal cleanup to execute an arbitrary shell command.

The resulting command execution runs as the **nobody user** within the httpd\_t SELinux context. This alone provides limited access, but the chain doesn't stop there.

### Stage 2: Fragnesia Kernel LPE (CVE-2026-46300)

The privilege escalation stage exploits [Fragnesia (CVE-2026-46300)](https://portal.hunt.io/vulnerability/cve/CVE-2026-46300), a Linux kernel vulnerability in the **XFRM** subsystem's page-cache handling. This stage is implemented by **two dedicated payloads** in the open directory. The **pfrag.py** contains the Fragnesia kernel exploit variant and webshell dropper, and the **fpatch.py** handles the PAM configuration patching logic.

The patched PAM configuration replaces the authentication module with **pam\_permit.so**, which allows any user to invoke **su** without a password. The unmodified **setuid /usr/bin/su** binary then runs within the same B2 HTTP request, elevating the operator from nobody to root.

### Stage 3: Root Relay Installation

With root access, the exploit automatically replaces the existing unauthenticated **change\_password.php** file with a root-capable command relay that executes commands as root. The original PHP file and PAM configuration are backed up, while the unmodified **health.php** endpoint is preserved to maintain the B2 re-exploitation path. No additional ports, daemons, or cron jobs are introduced.

### Stage 4: Verification and Persistence

Once the relay is in place, **three** additional scripts from the open directory handle verification and long-term persistence. The first script, **install\_persist.sh**, is the primary persistence installer that creates a systemd service unit (**pan-ops-init.service**) and an **/etc/rc.local** hook containing the marker string PANOPSHELL, ensuring the operator's access survives reboots. The second script **persist.sh** acts as a lightweight check that verifies the PANOPSHELL marker is present in the boot chain.

The third script, **verify2.sh**, validates the relay, PAM patch, and persistence. A clean **pam\_permit** configuration is written to disk to preserve the relay across PHP restarts. The PAM patch and su invocation must occur within the same B2 request to prevent subsequent memory-intensive exploitation from evicting the patch before it is flushed to disk.

### Version Matrix

The toolkit contains hardcoded memory offsets for specific PAN-OS and PHP version combinations. The operator's README documents the following version matrix, which maps PAN-OS releases to the PHP runtime they ship and the corresponding exploitation offsets:

| PAN-OS Version | PHP Version | Calibration Status | 
|---|---|---|
| 12.1.4 | 8.0.30 | Calibrated | 
| 12.1.9 | 8.0.30 | Provisional | 
| 12.1.10 | 8.0.30 | Provisional | 
| 12.2.3 | 8.0.30 | Provisional | 
| 12.2.4 | 8.0.30 | Provisional | 
| 11.1.6 | 7.4.33 | Unsupported (PHP 7.4) | 

The "**provisional**" designation indicates that the operator identified shared memory offsets between certain PAN-OS builds. The toolkit explicitly states that PAN-OS 11.1.6 is unsupported because its PHP 7.4.33 runtime uses different internal structures that have not been calibrated. Exploitation is restricted to the 12.x branch running PHP 8.0.30.

## The Campaign Pipeline: From 19,182 Targets to 25 Roots

The open directory contains a complete set of **CSV files** that document the operator's systematic approach to target identification and exploitation. This data shows how a mass-exploitation campaign progresses from internet-wide scanning through selective targeting to confirmed compromise.

### Phase 1: Internet-Wide Reconnaissance

The file **paloalto\_all.csv** contains 19,182 rows representing the results of a FOFA-based scan for exposed PAN-OS management interfaces across the public internet. The scan returned results from **95 countries**, with the following distribution among the top 15:

### Phase 2: Version Fingerprinting

The operator's batch scanning tool (**batch\_scan.py**) was run against all 19,182 hosts with **200 concurrent workers** and a 10-second timeout. The results were triaged into **three** categories:

The total count of hosts running exploitable 12.x firmware was **631**, representing approximately 13.7% of all versioned hosts and just 3.3% of the original reconnaissance set.

### Phase 3: Targeted Exploitation

From the **631 exploitable hosts**, the operator further filtered to a batch of **240 targets** concentrated in **four** countries: the United States (219), China (9), South Korea (6), and Japan (6).

The exploitation batch runner then attempted the full **four-stage chain** against each host, with results logged to individual per-target log files.

#### Exploitation Results

The 25 confirmed root compromises are recorded across four separate CSV files within the open directory, each corresponding to a different exploitation phase or target class.

| File | Records | Description | 
|---|---|---|
| **ok.csv** | 21 | Primary internet-facing exploitation batch | 
| **success2.csv** | 2 | Secondary exploitation round targeting US cloud-hosted appliances | 
| **pano\_ok.csv** | 1 | Panorama management server reached via internal reverse tunnel | 
| **mpnf\_success.csv** | 1 | Managed next-generation firewall (MPNF) within the same enterprise | 

The compromised appliances were hosted on networks operated by major cloud providers (**Microsoft Azure, Amazon Web Services, Oracle Cloud**), telecom carriers (**Korea Telecom, SK Broadband**), and colocation and network providers (**Zayo Bandwidth, Equinix**). These providers were not breached. The rooted devices are customer-run PAN-OS firewalls deployed on their networks. Separately, one of the 25 compromises was a managed firewall instance inside a US defense-sector organization. Individual exploitation attempts averaged between **6 and 13 minutes** per target, as recorded in the batch\_elapsed field of the success logs.

The analysis of the CSV shows 25 rows that contain the full command output confirming **uid=0(root)** and the kernel version string. We have mapped the victim countries and exploited versions in the graph below.

## Post-Exploitation: Deep Enterprise Compromise

The open directory reveals that on at least one compromised host, the operator moved well beyond initial root access into a sustained, multi-week intrusion focused on a US defense-sector organization. The post-exploitation toolkit points to careful planning and a clear objective: establish persistent, covert access to the internal enterprise network through the compromised firewall.

### Persistence Mechanisms

The script **install\_persist.sh** installs boot-durable persistence that survives appliance reboots. It operates in three layers:

**Layer 1: Payload staging**. SSH keys, a SOCKS5 proxy script, and tunneling scripts are copied from the ephemeral **/dev/shm** staging area to a hidden directory on the persistent root filesystem at **/usr/local/lib/.panops**, with restrictive permissions (mode 700 for the directory, 600 for the private key).

**Layer 2: Systemd service**. A systemd unit named **pan-ops-init.service** is created and enabled under the **multi-user.target**. The unit is typed as oneshot with RemainAfterExit=yes, described innocuously as "PAN-os Operations Init (post-boot management bridge)". On boot, it spawns the SOCKS5 proxy and reverse SSH tunnel loops.

**Layer 3: rc.local fallback**. As a belt-and-braces measure, a hook is appended to **/etc/rc.d/rc.local** with the marker string PANOPSHELL, ensuring the persistence survives even if systemd unit loading is disrupted during a firmware update. The script checks for the marker before appending to avoid duplicate entries.

```
grep -q PANOPSHELL /etc/rc.d/rc.local 2>/dev/null ||
  printf '\n# PANOPSHELL\n/bin/sh /usr/local/lib/.panops/start.sh >/dev/null 2>&1\n'
  >> /etc/rc.d/rc.local
chmod 755 /etc/rc.d/rc.local
```
                Copy
### Reverse SSH Tunneling and SOCKS5 Proxy

The tunneling infrastructure creates a bidirectional bridge between the compromised firewall's internal network and the operator's VPS. The script **tun.sh** establishes persistent reverse SSH tunnels that map **eight internal network services** to localhost ports on the VPS at 130.94.67\[.\]235:

The tunnel mapping reveals the operator's specific targets within the compromised network: the Active Directory domain controller (LDAP on port 389, LDAPS on port 636, and RDP on port 3389), **two** internal SSH servers, an internal HTTPS application, and the GlobalProtect VPN gateway. The SOCKS5 tunnel on port 10700 provides a general-purpose proxy that gives the operator arbitrary access to the entire 10.100.0.0/16 internal network range from their VPS.

The SOCKS5 proxy itself (**socks.py**) is a minimal, threaded implementation supporting CONNECT operations only, designed to be started with setsid so it survives the PHP relay request that launches it. A supervisor script (**socksloop.sh**) monitors the proxy and restarts it automatically if it crashes or reaches its one-hour timeout.

```
#!/bin/sh
# supervisor: keep the SOCKS5 server alive on 127.0.0.1:10700
while :; do
  echo "$(date -u) socks start" >> /tmp/socksloop.log
  timeout 3600 python3 /dev/shm/.socks.py 10700 >> /tmp/socks.log 2>&1
  echo "$(date -u) socks exit $?" >> /tmp/socksloop.log
  sleep 3
done
```
                Copy
### Active Directory Reconnaissance

The directory contains multiple AD reconnaissance scripts of increasing sophistication. The primary tool (**adacl.py**) performs LDAP-based enumeration of the target domain, querying for users, groups, group memberships, computer objects, and access control lists (ACLs). The script was served to compromised firewalls directly from the VPS HTTP server on port 8080, as confirmed by the recovery automation in **watch\_recover.sh**:

The AD tooling also includes **ldtest.py** (LDAP connection testing), **miner.py** (data extraction), **keys1.py** (SSH key harvesting), and **secrets2.py** (credential extraction from PAN-OS configuration).

The file **spray.py** implements a password spraying attack against authentication endpoints discovered during the reconnaissance phase. The operator appears to have targeted both LDAP bind authentication and Keycloak SSO token endpoints, attempting common passwords across enumerated user accounts.

#### Panorama Pivot

The script **deploy.sh** provides a file transfer mechanism that moves payloads from the VPS to other compromised hosts through the root relay. It ships files via base64-encoded POST chunks, using the compromised **change\_password.php** relay as a command transport.

**Note**: The target in the discovered script is a second compromised host identified in the CSV data as a Panorama management appliance, indicating the operator expanded from a single firewall compromise to the centralized management platform.

## Operational Verification and Cleanup

The operator was disciplined about cleanup. The script **verify2.sh** performs a comprehensive post-installation check: confirming the systemd unit is enabled and active, verifying payload files are present in **/usr/local/lib/.panops**, checking that tunnel and proxy worker processes are running, and auditing /dev/shm and /tmp for residual artifacts.

The cleanup script **finalize.sh** takes an additional step: it kills all running workers, stops the systemd unit, then restarts it, proving that the persistence mechanism correctly survives a clean restart cycle. After verification, it removes approximately 30 staged scripts from **/dev/shm** while preserving the persistence payload on the root filesystem. The cleanup script **clean3.sh** performs a separate sweep of scratch files and verifies that PAN-OS native shared-memory files remain intact.

## GlobalProtect Authentication Bypass (CVE-2026-0257)

Beyond the PAN-OS exploitation chain, the open directory contains forge\_cookie.py, a standalone tool that exploits [CVE-2026-0257](https://portal.hunt.io/vulnerability/cve/CVE-2026-0257) to forge GlobalProtect authentication override cookies. The tool requires no credentials and no prior access to the target.

Its technique:

1. Connect to the target over TLS and extract the CA certificate from the handshake (forcing TLS 1.2 so the Certificate message is sent in plaintext).
2. Extract the public key from the certificate.
3. Encrypt a forged authentication cookie for a specified username using RSA public-key padding.
4. Submit the forged cookie to the GlobalProtect gateway and portal endpoints to bypass authentication entirely.

The presence of this tool alongside the PAN-OS RCE chain indicates the operator maintained a toolkit for multiple Palo Alto Networks attack vectors. Once inside the network via the firewall exploit, the GlobalProtect bypass provides an alternative persistence and access mechanism through the organization's VPN infrastructure, which would survive the firewall being reimaged or patched.

Figure 17. Proof-of-concept exploit for CVE-2026-0257 targeting Palo Alto GlobalProtect. Extracts TLS public keys (unauthenticated), forges RSA-encrypted authentication override cookies, and tests gateway/portal endpoints. Uses cryptography library, network sockets, and plaintext TLS handshake parsing for full chain retrieval.
## Keycloak SSO and SAML Reconnaissance

A cluster of scripts in the open directory targets Keycloak SSO and SAML authentication infrastructure. The reconnaissance script **recon2.sh** performs Certificate Transparency log enumeration via **crt.sh** to discover subdomain names associated with the target organization, then resolves them via DNS and probes for Keycloak endpoints:

Additional Keycloak-focused scripts include **kc.sh**, **kc2.sh**, **kc3.sh** (endpoint enumeration and probing), **kctok.sh** (token acquisition attempts), **kcv.sh** (version detection), and **kcout.py** (output processing). The SAML scripts (**saml1.py**, **saml2.py**, **samldbg.py**, **samlfind.sh**) suggest the operator was also investigating SAML-based single sign-on integration with GlobalProtect.

## Internal Network Reconnaissance and Lateral Movement

Beyond the initial AD enumeration, the open directory contains a suite of tools specifically designed to map and move through the compromised organization's internal network. These scripts were executed on the rooted PAN-OS appliance itself, using the firewall's privileged position on the network boundary to reach hosts in the internal 10.100.0.0/16 range.

### Internal TCP Scanning

The script **scan.py** implements a multithreaded TCP port scanner designed to run from the compromised appliance using only Python standard library modules. It targets internal subnets with a curated list of **36 ports** spanning common enterprise services:

Companion scripts **scan2.py** and **scan3.py** expand this approach to additional subnets. The script dcports.py performs a focused port scan of the domain controller at 10.100.x.x, specifically targeting AD-relevant ports (LDAP, Kerberos, SMB, WinRM, RDP) to confirm service availability before launching more targeted attacks.

### SSH Credential Spraying Against Internal Hosts

The script **vssh.py** implements targeted SSH authentication attempts against internal hosts reached through the reverse tunnel. The script uses the Paramiko library to attempt connections with harvested SSH keys and a curated list of usernames and passwords targeting PAN-OS service accounts, VMware infrastructure accounts, and common administrative credentials. Target hosts are accessed through the reverse tunnel ports (127.0.0.1:2201 and 127.0.0.1:2202), corresponding to the two internal hosts mapped in **tun.sh**.

### On-Box Reconnaissance

The script **recon3.py** performs reconnaissance directly from the compromised firewall, combining SSH banner fingerprinting of internal hosts, SSH key and credential harvesting, and a targeted LDAP bind test against the domain controller using credentials extracted from the PAN-OS configuration. The script probes seven internal IP addresses for SSH service banners and validates LDAP credentials against the domain controller's LDAPS endpoint.

### Configuration Mining

The operator developed multiple scripts to systematically extract intelligence from PAN-OS configuration files on compromised appliances:

- **cfggrep.py** parses the merged running configuration XML to extract GlobalProtect gateway settings, tunnel interface definitions, User-ID agent configurations, internal address objects (including NAS, ESXi, vCenter references), static routes, and IPsec tunnel peers.
- **gp1.py** specifically targets GlobalProtect authentication override settings, client authentication profiles, certificate profiles, and portal/gateway entries, mapping the organization's VPN authentication architecture.
- **exfil.py** performs a comprehensive extraction of pivot-enabling material from the running configuration: HA SSH private keys (PAN-OS roots high-availability over SSH), device certificates with encrypted passphrases, LDAP bind credentials (decrypted in the configuration), address object inventories, and admin account definitions.
- **secrets2.py** and **secrectx.py** extract additional credential material from the appliance.
- **keys1.py** harvests SSH keys stored on the appliance for use in lateral movement.
- **blobs.py** processes encrypted configuration blobs.

Figure 20. Configuration extraction targets from exfil.py. The operator's own comments describe the extraction as enabling the move from "root on one firewall" to "inside the AD segment."

The output file **miner.out.gz** contains 14,806 lines of structured data extracted from **Panorama** saved configurations, including LDAP bind credentials, SAML/Keycloak endpoints, internal IP address inventories, managed device serial numbers, device groups, and firewall rules targeting domain controller subnets. Its presence on the VPS confirms that configuration extractions were completed and exfiltrated across multiple compromised hosts.

| Extraction Category | Items Found | Key Intelligence Value | 
|---|---|---|
| Configuration Files Parsed | 3 files | merged-running-config (941 KB), candidate-snapshot (19.8 MB), ha-remote-rc (568 KB) | 
| LDAP Server Profiles | 9 profiles | Bind DN/passwords for the target's internal AD domain, server addresses on port 636 (LDAPS) | 
| Authentication Profiles | 7 profiles | Auth methods mapped to user groups and access policies | 
| SAML IdP Entries | 4 entries | Keycloak SSO endpoints for two of the organization's SSO realms | 
| Secret Fields (encrypted) | 3 fields | LDAP bind password, 2 cryptographic keys (AQ==-prefixed PAN-OS encryption) | 
| Secret Fields (plaintext) | 22 fields | Key exchange algorithms, master-key settings, rekey intervals | 
| Certificate/Key Paths | 15 paths | Content certs, trusted root CA list (153 KB), internal certificates (18 KB) | 
| Internal Subnets | 25 unique /24s | 10.0.0/8, 172.16.0/12, 192.168.0/16 ranges across 5 major blocks | 
| Panorama-Managed Devices | 6 devices | Firewall fleet managed by the compromised Panorama instance | 
| GlobalProtect Gateways | 2 gateways | two GlobalProtect gateways (hostnames redacted) | 

The operator's own comments in **exfil.py** note that "the earlier copy on our controller got overwritten by another target," indicating the surviving file represents only the last of several extraction runs.

## AI-Assisted Offensive Tooling

The open directory contains extensive evidence that the operator integrated multiple AI systems into the attack infrastructure, not merely as coding assistants but as autonomous agents capable of reading offensive playbooks, downloading security tools, and preparing for AI-driven penetration testing. The session logs, database schemas, and configuration files provide a detailed record of how AI was deployed on this VPS.

### Timeline: AI Deployment on the VPS

The server's bash history reveals a clear sequence of AI tool installation on October 8, 2026. The operator first attempted to run claude (not yet installed), then installed npm via apt, and used it to install **Claude Code** (Anthropic's AI coding assistant) globally:

The configuration file **.claude.json** records the first launch of Claude Code at **08:48:10 UTC** on October 8, 2026 (version 2.1.293). Twelve minutes later, at **09:00:47 UTC**, the aiscan platform opened its first AI session using **DeepSeek v4-pro** as the primary model. The entire AI initialization sequence, from first session to full tool readiness, completed in **under nine minutes (09:00 to 09:09 UTC)**.

### The aiscan Platform: Multi-Agent Architecture

The aiscan directory contains a full installation of an AI-powered offensive security platform built around a multi-agent architecture. The core binary (**aiscan-full**) provides a web interface that was exposed on port 23522. Its configuration file (**aiscan.yaml**) reveals three AI backend providers and a **FOFA reconnaissance key**:

The platform's session logs reveal a multi-agent architecture designed for autonomous penetration testing. The AI reads structured "skill" files that define distinct agent roles:

Figure 24. The aiscan multi-agent penetration testing architecture as described in the platform's skill files.
The three agent roles operate as follows. The **pentest-coordinator** receives a target company or root domain, bootstraps an asset inventory, divides work into shards, and dispatches each shard to a **pentest-worker**. Workers execute autonomously: they scan their assigned shard using the platform's built-in tools, write findings to a central hub, and asynchronously dispatch any high-severity results to the **rce-verify** subagent. The rce-verify agent performs single-finding RCE verification, restricted to id/whoami proof and read-only operations. An **IOA** (Inter-Operator Async) message bus enables multi-agent collaboration across the system.

### Built-in Offensive Tool Suite

The aiscan platform provides a library of pseudo-commands (built-in wrappers around security tools) alongside an arsenal package manager for installing external binaries. The session logs show the AI systematically downloading and initializing **17 external tools** on October 8, all within a **two-minute window (17:05 to 17:07 UTC+8)**:

| Category | Tool | Type | Function | 
|---|---|---|---|
| Built-in pseudo-commands | gogo | Scanner | Host and service discovery | 
|  | spray | Scanner | Web probing and HTTP fingerprinting | 
|  | zombie | Scanner | Weak credential checking | 
|  | neutron | Scanner | Template-based POC execution (83 templates) | 
| Built-in recon | proton | Scanner | Secrets and sensitive data scanning | 
|  | passive | OSINT | FOFA/Shodan/Censys aggregated recon | 
|  | katana/playwright | Crawler | Web crawling and headless browser verification | 
| Infrastructure | arsenal | Utility | Security tool package manager | 
|  | cyberhub | Utility | Fingerprint-to-POC mapping database | 
|  | tmux | Utility | Session manager for concurrent operations | 
|  | proxy | Utility | Proxy node management for anonymized scanning | 
| Arsenal-installed (17 tools) | nuclei v3.11.1 | Scanner | Template-based vulnerability scanner | 
|  | httpx v1.12.0 | Probe | HTTP probing and technology detection | 
|  | subfinder v2.17.0 | Recon | Passive subdomain enumeration | 
|  | naabu v2.6.1 | Scanner | Port scanning | 
|  | + 13 more | Various | dnsx, katana, uncover, interactsh-client, shuffledns, alterx, cloudlist, mapcidr, tlsx, asnmap, proxify, urlfinder, notify | 

### Session Logs: The AI Reading Its Own Playbooks

The most revealing file is the 4.6 MB session log (**session-20261008-170047.789537789.jsonl**), which contains 15,080 event lines documenting a complete AI conversation with **3 turns and 448 discrete events**. The log shows, step by step, how an AI agent prepared itself for offensive security operations.

**Turn 1** (09:01 UTC, 66 events): The operator's English-language prompt, "you read my skill.md and so on," instructed the DeepSeek v4-pro model to internalize its offensive playbooks. The AI's reasoning chain (4,002 characters) shows it methodically planning which files to read. It then executed 22 glob and read tool calls, ingesting the full set of skill files: aiscan (ASM/pentest toolkit), pentest-coordinator (orchestration), pentest-worker (autonomous execution), rce-verify (RCE validation), report (OKF-style output), ioa-finding (vulnerability publishing), plus playbooks for every scanner (scan, gogo, spray, zombie, neutron, proton) and utility (arsenal, cyberhub, tmux, proxy, passive, katana, playwright, ioa). The AI's text response confirmed it understood its role hierarchy and verification standards:

**Turn 2** (09:05 UTC, 264 events): The operator switched to **Chinese**: "下载所有必要的工具及相关资源。" ("Download all necessary tools and related resources.") The AI's reasoning chain expanded to 15,027 characters as it analyzed all 22 arsenal tools, decided which to install (skipping gogo, spray, and zombie as built-in pseudo-commands, and iom as a C2 implant framework "not needed for ASM/pentest work"), and executed 55 bash tool calls to download and install 17 external security binaries. The arsenal manifest records all 17 installations completing between 17:05:34 and 17:07:44 UTC+8, a span of just over two minutes.

**Turn 3** (09:09 UTC, 117 events): A second **Chinese** prompt: "初始化所有工具，并确保它们可用。" ("Initialize all tools and ensure they are available.") The AI produced its longest reasoning chain (29,877 characters), systematically verifying every installed binary, building massdns from source as a dependency for shuffledns, testing all pseudo-commands, verifying that the FOFA-backed passive recon returned live results, confirming uncover/subfinder provider configurations, and running functional smoke tests on every core tool. The AI confirmed **83 built-in neutron templates** were operational and that nuclei had its full template library available.

### Database Schema: Purpose-Built for AI-Driven Penetration Testing

The platform's SQLite database (**aiscan-web.db**) contains 11 tables that reveal the system's intended operational workflow. The schema itself documents the platform's full capability:

| Table | Rows | Purpose | Key Columns | 
|---|---|---|---|
| chat\_sessions | 1 | AI conversation sessions | title, agent\_name, status | 
| chat\_aop\_events | 448 | All AI agent operation events | turn\_id, emitter, event\_json | 
| aop\_request\_journal | 4 | API request/response log | method (OpenSession, RunTurn) | 
| scans | 0 | Scan task tracking | target, mode, verify, sniper, deep, status | 
| pentest\_assets | 0 | Discovered asset inventory | type, value, source, parent\_id | 
| pentest\_findings | 0 | Vulnerability findings | severity, source\_tool, verified | 
| pentest\_rce\_results | 0 | RCE verification outcomes | target, vector, proof, privilege, status | 
| sco\_nodes | 0 | Security Context Objects | cstx\_type, data | 
| sco\_observations | 0 | Observation linkage | operation\_id, observed\_at | 

## Monitoring and Automated Recovery

The operator maintained automated monitoring to detect when compromised appliances went offline (due to reboots, firmware updates, or network changes) and to re-establish access automatically when they returned. The script **mon.sh** polls the root relay's health endpoint every 20 seconds for up to 80 minutes:

The companion script **watch\_recover.sh**, shown earlier, extends this concept: when the firewall comes back online and confirms root access, it automatically re-deploys the AD reconnaissance tooling without operator intervention. This level of automation indicates a sustained, multi-week campaign rather than an opportunistic one-time exploitation.

## Mitigation and Defensive Recommendations

- **Restrict Management Access**: Limit PAN-OS management interfaces to dedicated management networks or authorized administrator IPs. Never expose them directly to the internet.
- **Apply Security Patches**: Promptly install PAN-OS security updates and hotfixes, prioritizing vulnerabilities exploited in the campaign.
- **Monitor Persistence Artifacts**: Audit for unauthorized services, SSH keys, PAM changes, modified PHP files, and suspicious files in /usr/local/lib/.panops/ and /dev/shm/.
- **Detect Outbound Tunnels**: Monitor unusual outbound SSH connections from firewalls, reverse SSH tunnels, and SOCKS5 proxies on port 10700.
- **Strengthen Network Segmentation**: Restrict firewall access to internal systems, including domain controllers and VPN infrastructure. Rotate stored LDAP credentials and shared SSH keys.
- **Harden GlobalProtect and SSO**: Patch authentication vulnerabilities, enforce MFA, review SAML trust relationships, and monitor VPN logins for suspicious activity.
- **Prepare for AI-Driven Threats**: Strengthen continuous attack surface monitoring, accelerate patching, and use threat intelligence to detect emerging AI-assisted attacks.

## MITRE ATT&CK Matrix

The following table maps the techniques observed in this campaign to the MITRE ATT&CK framework for Enterprise.

| Tactic | Technique | ID | Evidence from Open Directory | 
|---|---|---|---|
| Reconnaissance | Active Scanning: Vulnerability Scanning | T1595.002 | FOFA-based scan of 19,182 PAN-OS management portals (paloalto\_all.csv). | 
|  | Gather Victim Host Information: Client Configurations | T1592.004 | Version fingerprinting via precon.py before exploitation. | 
|  | Search Open Technical Databases | T1596 | Certificate Transparency log enumeration (recon2.sh), DNS reconnaissance (dns1.py), FOFA API queries via aiscan. | 
| Resource Development | Acquire Infrastructure: Virtual Private Server | T1583.003 | VPS at 130.94.67\[.\]235 (AS154177, LIGHT NODE LIMITED, Tokyo) hosting payloads and receiving tunnels. | 
|  | Develop Capabilities: Exploits | T1587.001 | Custom PAN-OS exploit chain (panos\_rce\_poc.py), Fragnesia variant (pfrag.py), cookie forging tool (forge\_cookie.py). | 
|  | Obtain Capabilities: Tool | T1588.002 | Aiscan AI offensive platform, iox tunneling utility, ProjectDiscovery suite (nuclei, httpx, subfinder, etc.), Claude Code. | 
| Initial Access | Exploit Public-Facing Application | T1190 | PHP session.upload\_progress heap corruption on PAN-OS management interface via panos\_rce\_poc.py. | 
| Execution | Command and Scripting Interpreter: Unix Shell | T1059.004 | Shell commands executed through the change\_password.php root relay (su -c ... root). | 
|  | Command and Scripting Interpreter: Python | T1059.006 | Python-based exploit scripts (panos\_rce\_poc.py, pfrag.py, fpatch.py, scan.py, vssh.py). | 
| Persistence | Server Software Component: Web Shell | T1505.003 | change\_password.php replaced with root-capable command relay. | 
|  | Create or Modify System Process: Systemd Service | T1543.002 | pan-ops-init.service installed by install\_persist.sh. | 
|  | Boot or Logon Initialization Scripts: RC Scripts | T1037.004 | /etc/rc.local hook with PANOPSHELL marker via install\_persist.sh. | 
| Privilege Escalation | Exploitation for Privilege Escalation | T1068 | Fragnesia kernel LPE (CVE-2026-46300) via pfrag.py and fpatch.py; patches /etc/pam.d/su to pam\_permit.so. | 
| Defense Evasion | Masquerading: Match Legitimate Name or Location | T1036.005 | Webshell placed in legitimate PAN-OS PHP path; persistence directory named .panops to blend with PAN-OS files. | 
|  | Obfuscated Files or Information | T1027 | Base64-encoded tool transfer via deploy.sh chunk uploads; staging in volatile /dev/shm/. | 
| Credential Access | Unsecured Credentials: Credentials in Files | T1552.001 | PAN-OS running-config extraction via exfil.py (LDAP bind passwords, HA SSH keys, RADIUS secrets). | 
|  | Brute Force: Password Spraying | T1110.003 | SSH credential spraying against internal hosts via vssh.py through reverse tunnels. | 
|  | Forge Web Credentials: Web Cookies | T1606.001 | GlobalProtect authentication-override cookie forging (CVE-2026-0257) via forge\_cookie.py. | 
| Discovery | Remote System Discovery | T1018 | Internal TCP scanning of 10.100.0.0/16 via scan.py. | 
|  | Account Discovery: Domain Account | T1087.002 | AD/LDAP enumeration via adacl.py deployed through reverse tunnels. | 
|  | Network Service Discovery | T1046 | Port scanning of internal hosts from compromised firewall; service fingerprinting via gogo. | 
|  | Domain Trust Discovery | T1482 | SAML and Keycloak SSO probing scripts; GlobalProtect authentication profile enumeration. | 
| Lateral Movement | Remote Services: SSH | T1021.004 | SSH credential spraying via vssh.py against internal hosts through SOCKS5 pivot. | 
|  | Remote Services: Remote Desktop Protocol | T1021.001 | RDP access to internal hosts tunneled through reverse SSH infrastructure (tun.sh). | 
| Collection | Data from Local System | T1005 | PAN-OS configuration mining via exfil.py; extraction of HA pairs, LDAP configs, address objects. | 
| Command and Control | Protocol Tunneling | T1572 | Reverse SSH tunnels (tun.sh) from compromised firewalls to VPS on 8 ports. | 
|  | Proxy: Internal Proxy | T1090.001 | SOCKS5 proxy (socks.py) on localhost:10700 supervised by socksloop.sh. | 
|  | Ingress Tool Transfer | T1105 | Base64-chunked payload delivery via deploy.sh; tools served from VPS port 8080. | 

## Indicator of Compromise (IOC) table

| Indicator | Type | Description | 
|---|---|---|
| 130.94.67\[.\]235 | IPv4 | VPS hosting an open directory and receiving reverse SSH tunnels. AS154177 (LIGHT NODE LIMITED), Tokyo, Japan. | 
| :8080 | Port | HTTP file server on the VPS serving payloads to compromised hosts. | 
| :23522 | Port | aiscan AI offensive platform web interface on the VPS. | 
| /usr/local/lib/.panops/ | Path | Persistence payload directory on compromised PAN-OS appliances. | 
| pan-ops-init.service | Systemd Unit | Boot persistence service described as "PAN-os Operations Init." | 
| PANOPSHELL | String | Marker string in /etc/rc.d/rc.local identifying the persistence hook. | 
| change\_password.php | Relay | Default webshell relay location (replaces legitimate PAN-OS file). | 
| /dev/shm/.p2/ | Path | Staging directory for SSH keys and proxy scripts before persistence install. | 
| /dev/shm/.socks.py | Path | SOCKS5 proxy script in shared memory during staging. | 
| /dev/shm/.a/a.py | Path | AD reconnaissance tool staging location on compromised hosts. | 
| socksloop.sh | Filename | SOCKS5 supervisor loop script. | 
| tun.sh / tun2.sh | Filename | Reverse SSH tunnel persistence scripts (primary and secondary). | 
| adacl.py | Filename | Active Directory ACL reconnaissance tool served from VPS port 8080. | 
| aiscan-full | Binary | AI-powered offensive security scanning platform (134 MB). | 
| gogo / gogod.b64 | Binary | Compiled Go network discovery tool (4.3 MB) and base64-encoded variant. | 
| iox | Binary | Open-source tunneling utility (EddieIvan01/iox v0.4). | 
| CVE-2026-46300 | CVE | Fragnesia Linux kernel XFRM page-cache LPE used for privilege escalation. | 
| CVE-2026-0257 | CVE | GlobalProtect authentication override cookie forging vulnerability. | 

## Conclusion

The exposed directory documents the full lifecycle of a PAN-OS exploitation campaign, from reconnaissance of **19,182 internet-facing management portals** to root access, persistence, and enterprise-wide lateral movement. The chained exploitation of PHP and kernel-level vulnerabilities, including the adaptation of the **Fragnesia** exploit to smaller patch files, took deliberate engineering effort. Multiple persistence mechanisms, automated recovery scripts, and configuration-mining tools reveal a deliberate strategy for maintaining access and expanding from compromised firewalls into internal networks.

The aiscan multi-agent framework, driven by DeepSeek v4-pro and Kimi k3, shows AI being used to automate reconnaissance, vulnerability validation, and exploitation workflows. Anthropic's Claude Code was also installed on the VPS, but the capture shows no evidence it was used in the exploitation. The campaign's 25 confirmed root compromises, GlobalProtect authentication bypass, Active Directory enumeration, and access to additional enterprise firewalls show how far a single unpatched management interface can take an attacker.

[Track this PAN-OS campaign across IOCs and infrastructureOne VPS held the whole open directory, from the FOFA scan lists to the reverse SSH tunnels. Start free and pivot across the host, its certificates and the tooling it served to catch the next box before it lands in a blocklist.Start hunting now](https://hunt.io/get-started)

In our previous research, [Hunting Leaked PHP2Shell RCE Across Open Directories](https://hunt.io/blog/php2shell-cve-2026-109618-109619-open-directories) examined the exposure of **CVE-2026-109618** and **CVE-2026-109619**, uncovering attacker tooling and early exploitation attempts. We followed up in [PHP2Shell One Week Later: Honeypot Shells on the Web, a Path to Root on Palo Alto Firewalls](https://hunt.io/blog/php2shell-honeypot-shells-root-palo-alto-firewalls), documenting confirmed honeypot activity and production compromises involving Palo Alto firewalls. Building on these findings, this post breaks down the Palo Alto exploitation.

Our [AttackCapture™](https://hunt.io/features/attackcapture) platform identified an open directory at [130.94.67\[.\]235:8080](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.67.235:8080) containing a fully operational **PAN-OS exploitation toolkit**. The analysis reveals an entire campaign lifecycle including internet-wide reconnaissance of **19,182 management portals**, a chained PHP memory corruption and kernel-level privilege escalation exploit, **25 confirmed root compromises** across major US and South Korean organizations including lateral pivots to Panorama and managed firewall infrastructure, and a deep post-exploitation playbook targeting Active Directory, GlobalProtect VPN, and Keycloak SSO infrastructure.

Here is what we found inside.

## Key Takeaways

- A four-stage exploit chain achieves root-level access on PAN-OS firewalls through a single unauthenticated HTTP request, combining PHP **session.upload\_progress** memory corruption with the **Fragnesia kernel LPE (CVE-2026-46300)**.
- The exploitation logs across document root access on **25 appliances (18 US, 6 South Korea, 1 internal pivot)**, including lateral movement to a Panorama management server and a managed next-generation firewall within the same enterprise.
- FOFA-based internet-wide reconnaissance of **19,182 PAN-OS management portals**, version-calibrated target lists, reverse SSH tunnel infrastructure, SOCKS5 proxy pivots, AD/LDAP reconnaissance, **GlobalProtect authentication bypass (CVE-2026-0257)**, and automated persistence and recovery scripts.
- The operator deployed a multi-agent AI penetration testing platform (aiscan) powered by **DeepSeek v4-pro**, **DeepSeek v4-flash**, and **Kimi k3**.
- A 4.6 MB session log captures the aiscan AI (DeepSeek v4-pro) autonomously reading 22 offensive playbooks, downloading 17 security tools, and verifying operational readiness in under nine minutes. Anthropic's Claude Code was also installed on the same VPS, though the capture shows no evidence it was used in the attack.
- Automated health monitoring, crash recovery scripts, and multi-layer boot persistence (systemd, rc.local, preserved health endpoints) indicate a sustained campaign designed to survive appliance reboots and firmware updates.

## Discovery: The Open Directory

On October 24, 2026, our platform flagged an open HTTP file server on port 8080 at [130.94.67\[.\]235](https://portal.hunt.io/ip/130.94.67.235). The host resolves to [AS154177](https://portal.hunt.io/asn/AS154177) (LIGHT NODE LIMITED), a Tokyo-based VPS provider. Services were observed on ports 22 (SSH), 80, 443, and 8080, with the file server exposing the root home directory of a Linux system containing the operator's complete working environment.

The exposed [open directory](https://hunt.io/glossary/open-directories) at [130.94.67\[.\]235:8080](https://portal.hunt.io/attackcapture/filemanager?host=http://130.94.67.235:8080) includes over 80 Python scripts, shell scripts, and configuration files, along with binary tools, CSV datasets containing the results of internet-wide scanning campaigns, exploitation logs, and Active Directory reconnaissance output.

Our analysis exposes the full operational infrastructure, including the reconnaissance pipeline, version-calibrated exploitation batches, post-exploitation tooling for lateral movement and persistence, and authentication bypass utilities for **GlobalProtect VPN**.

It also contains a complete AI-powered offensive security platform (aiscan) with a 4.6 MB session log that captures a DeepSeek large language model autonomously reading **22 offensive skill files**, downloading **17 security tools**, and preparing for AI-driven penetration testing, alongside a separate installation of **Anthropic's Claude Code** on the same VPS.

## The Exploit Chain: From HTTP Request to Root Shell

The toolkit's central component is a **four-stage exploit chain** that achieves root-level command execution on **PAN-OS appliances** through a single unauthenticated interaction with the management interface. No credentials, no authentication tokens, and no prior access are required. The operator's own documentation (a detailed **README.md** included in the toolkit) describes the route with precision.

The chain operates as follows.

### Stage 1: PHP Memory Corruption (RCE as nobody)

The initial entry point exploits a heap corruption vulnerability in PHP's **session.upload\_progress** handler as exposed through PAN-OS's management web interface. The core exploit logic resides in **panos\_rce\_poc.py**, which orchestrates the entire four-stage chain from a single invocation.

Our analysis confirms three auxiliary scripts found in the open directory linked with the primary exploit. The **precon.py** script performs pre-exploitation reconnaissance to fingerprint the target's PAN-OS and PHP versions before taking any destructive action. The **prce.py** encapsulates the PHP RCE primitives used during the memory corruption sequence, and **p121.py** is a compatibility front-end that adapts the exploit for PAN-OS 12.1.x-specific memory layouts and offsets.

These **four** scripts implement the following sequence of HTTP requests that manipulate PHP's internal memory structures:

1. **The warm-up phase** primes the PHP process memory layout through controlled allocations.
2. **A1 (OOM trigger)** forces an out-of-memory condition that induces a use-after-free on internal zend\_reference structures.
3. **B1 (pointer leak)** extracts the base address of libphp from the server's Set-Cookie response header, defeating ASLR.
4. **A2 (stale reference)** crafts a dangling zend\_reference pointing to attacker-controlled memory.
5. **B2 (command execution)** constructs a fake HashTable with its pDestructor field set to the address of zif\_system, causing PHP's internal cleanup to execute an arbitrary shell command.

The resulting command execution runs as the **nobody user** within the httpd\_t SELinux context. This alone provides limited access, but the chain doesn't stop there.

### Stage 2: Fragnesia Kernel LPE (CVE-2026-46300)

The privilege escalation stage exploits [Fragnesia (CVE-2026-46300)](https://portal.hunt.io/vulnerability/cve/CVE-2026-46300), a Linux kernel vulnerability in the **XFRM** subsystem's page-cache handling. This stage is implemented by **two dedicated payloads** in the open directory. The **pfrag.py** contains the Fragnesia kernel exploit variant and webshell dropper, and the **fpatch.py** handles the PAM configuration patching logic.

The patched PAM configuration replaces the authentication module with **pam\_permit.so**, which allows any user to invoke **su** without a password. The unmodified **setuid /usr/bin/su** binary then runs within the same B2 HTTP request, elevating the operator from nobody to root.

### Stage 3: Root Relay Installation

With root access, the exploit automatically replaces the existing unauthenticated **change\_password.php** file with a root-capable command relay that executes commands as root. The original PHP file and PAM configuration are backed up, while the unmodified **health.php** endpoint is preserved to maintain the B2 re-exploitation path. No additional ports, daemons, or cron jobs are introduced.

### Stage 4: Verification and Persistence

Once the relay is in place, **three** additional scripts from the open directory handle verification and long-term persistence. The first script, **install\_persist.sh**, is the primary persistence installer that creates a systemd service unit (**pan-ops-init.service**) and an **/etc/rc.local** hook containing the marker string PANOPSHELL, ensuring the operator's access survives reboots. The second script **persist.sh** acts as a lightweight check that verifies the PANOPSHELL marker is present in the boot chain.

The third script, **verify2.sh**, validates the relay, PAM patch, and persistence. A clean **pam\_permit** configuration is written to disk to preserve the relay across PHP restarts. The PAM patch and su invocation must occur within the same B2 request to prevent subsequent memory-intensive exploitation from evicting the patch before it is flushed to disk.

### Version Matrix

The toolkit contains hardcoded memory offsets for specific PAN-OS and PHP version combinations. The operator's README documents the following version matrix, which maps PAN-OS releases to the PHP runtime they ship and the corresponding exploitation offsets:

| PAN-OS Version | PHP Version | Calibration Status | 
|---|---|---|
| 12.1.4 | 8.0.30 | Calibrated | 
| 12.1.9 | 8.0.30 | Provisional | 
| 12.1.10 | 8.0.30 | Provisional | 
| 12.2.3 | 8.0.30 | Provisional | 
| 12.2.4 | 8.0.30 | Provisional | 
| 11.1.6 | 7.4.33 | Unsupported (PHP 7.4) | 

The "**provisional**" designation indicates that the operator identified shared memory offsets between certain PAN-OS builds. The toolkit explicitly states that PAN-OS 11.1.6 is unsupported because its PHP 7.4.33 runtime uses different internal structures that have not been calibrated. Exploitation is restricted to the 12.x branch running PHP 8.0.30.

## The Campaign Pipeline: From 19,182 Targets to 25 Roots

The open directory contains a complete set of **CSV files** that document the operator's systematic approach to target identification and exploitation. This data shows how a mass-exploitation campaign progresses from internet-wide scanning through selective targeting to confirmed compromise.

### Phase 1: Internet-Wide Reconnaissance

The file **paloalto\_all.csv** contains 19,182 rows representing the results of a FOFA-based scan for exposed PAN-OS management interfaces across the public internet. The scan returned results from **95 countries**, with the following distribution among the top 15:

### Phase 2: Version Fingerprinting

The operator's batch scanning tool (**batch\_scan.py**) was run against all 19,182 hosts with **200 concurrent workers** and a 10-second timeout. The results were triaged into **three** categories:

The total count of hosts running exploitable 12.x firmware was **631**, representing approximately 13.7% of all versioned hosts and just 3.3% of the original reconnaissance set.

### Phase 3: Targeted Exploitation

From the **631 exploitable hosts**, the operator further filtered to a batch of **240 targets** concentrated in **four** countries: the United States (219), China (9), South Korea (6), and Japan (6).

The exploitation batch runner then attempted the full **four-stage chain** against each host, with results logged to individual per-target log files.

#### Exploitation Results

The 25 confirmed root compromises are recorded across four separate CSV files within the open directory, each corresponding to a different exploitation phase or target class.

| File | Records | Description | 
|---|---|---|
| **ok.csv** | 21 | Primary internet-facing exploitation batch | 
| **success2.csv** | 2 | Secondary exploitation round targeting US cloud-hosted appliances | 
| **pano\_ok.csv** | 1 | Panorama management server reached via internal reverse tunnel | 
| **mpnf\_success.csv** | 1 | Managed next-generation firewall (MPNF) within the same enterprise | 

The compromised appliances were hosted on networks operated by major cloud providers (**Microsoft Azure, Amazon Web Services, Oracle Cloud**), telecom carriers (**Korea Telecom, SK Broadband**), and colocation and network providers (**Zayo Bandwidth, Equinix**). These providers were not breached. The rooted devices are customer-run PAN-OS firewalls deployed on their networks. Separately, one of the 25 compromises was a managed firewall instance inside a US defense-sector organization. Individual exploitation attempts averaged between **6 and 13 minutes** per target, as recorded in the batch\_elapsed field of the success logs.

The analysis of the CSV shows 25 rows that contain the full command output confirming **uid=0(root)** and the kernel version string. We have mapped the victim countries and exploited versions in the graph below.

## Post-Exploitation: Deep Enterprise Compromise

The open directory reveals that on at least one compromised host, the operator moved well beyond initial root access into a sustained, multi-week intrusion focused on a US defense-sector organization. The post-exploitation toolkit points to careful planning and a clear objective: establish persistent, covert access to the internal enterprise network through the compromised firewall.

### Persistence Mechanisms

The script **install\_persist.sh** installs boot-durable persistence that survives appliance reboots. It operates in three layers:

**Layer 1: Payload staging**. SSH keys, a SOCKS5 proxy script, and tunneling scripts are copied from the ephemeral **/dev/shm** staging area to a hidden directory on the persistent root filesystem at **/usr/local/lib/.panops**, with restrictive permissions (mode 700 for the directory, 600 for the private key).

**Layer 2: Systemd service**. A systemd unit named **pan-ops-init.service** is created and enabled under the **multi-user.target**. The unit is typed as oneshot with RemainAfterExit=yes, described innocuously as "PAN-os Operations Init (post-boot management bridge)". On boot, it spawns the SOCKS5 proxy and reverse SSH tunnel loops.

**Layer 3: rc.local fallback**. As a belt-and-braces measure, a hook is appended to **/etc/rc.d/rc.local** with the marker string PANOPSHELL, ensuring the persistence survives even if systemd unit loading is disrupted during a firmware update. The script checks for the marker before appending to avoid duplicate entries.

```
grep -q PANOPSHELL /etc/rc.d/rc.local 2>/dev/null ||
  printf '\n# PANOPSHELL\n/bin/sh /usr/local/lib/.panops/start.sh >/dev/null 2>&1\n'
  >> /etc/rc.d/rc.local
chmod 755 /etc/rc.d/rc.local
```
                Copy
### Reverse SSH Tunneling and SOCKS5 Proxy

The tunneling infrastructure creates a bidirectional bridge between the compromised firewall's internal network and the operator's VPS. The script **tun.sh** establishes persistent reverse SSH tunnels that map **eight internal network services** to localhost ports on the VPS at 130.94.67\[.\]235:

The tunnel mapping reveals the operator's specific targets within the compromised network: the Active Directory domain controller (LDAP on port 389, LDAPS on port 636, and RDP on port 3389), **two** internal SSH servers, an internal HTTPS application, and the GlobalProtect VPN gateway. The SOCKS5 tunnel on port 10700 provides a general-purpose proxy that gives the operator arbitrary access to the entire 10.100.0.0/16 internal network range from their VPS.

The SOCKS5 proxy itself (**socks.py**) is a minimal, threaded implementation supporting CONNECT operations only, designed to be started with setsid so it survives the PHP relay request that launches it. A supervisor script (**socksloop.sh**) monitors the proxy and restarts it automatically if it crashes or reaches its one-hour timeout.

```
#!/bin/sh
# supervisor: keep the SOCKS5 server alive on 127.0.0.1:10700
while :; do
  echo "$(date -u) socks start" >> /tmp/socksloop.log
  timeout 3600 python3 /dev/shm/.socks.py 10700 >> /tmp/socks.log 2>&1
  echo "$(date -u) socks exit $?" >> /tmp/socksloop.log
  sleep 3
done
```
                Copy
### Active Directory Reconnaissance

The directory contains multiple AD reconnaissance scripts of increasing sophistication. The primary tool (**adacl.py**) performs LDAP-based enumeration of the target domain, querying for users, groups, group memberships, computer objects, and access control lists (ACLs). The script was served to compromised firewalls directly from the VPS HTTP server on port 8080, as confirmed by the recovery automation in **watch\_recover.sh**:

The AD tooling also includes **ldtest.py** (LDAP connection testing), **miner.py** (data extraction), **keys1.py** (SSH key harvesting), and **secrets2.py** (credential extraction from PAN-OS configuration).

The file **spray.py** implements a password spraying attack against authentication endpoints discovered during the reconnaissance phase. The operator appears to have targeted both LDAP bind authentication and Keycloak SSO token endpoints, attempting common passwords across enumerated user accounts.

#### Panorama Pivot

The script **deploy.sh** provides a file transfer mechanism that moves payloads from the VPS to other compromised hosts through the root relay. It ships files via base64-encoded POST chunks, using the compromised **change\_password.php** relay as a command transport.

**Note**: The target in the discovered script is a second compromised host identified in the CSV data as a Panorama management appliance, indicating the operator expanded from a single firewall compromise to the centralized management platform.

## Operational Verification and Cleanup

The operator was disciplined about cleanup. The script **verify2.sh** performs a comprehensive post-installation check: confirming the systemd unit is enabled and active, verifying payload files are present in **/usr/local/lib/.panops**, checking that tunnel and proxy worker processes are running, and auditing /dev/shm and /tmp for residual artifacts.

The cleanup script **finalize.sh** takes an additional step: it kills all running workers, stops the systemd unit, then restarts it, proving that the persistence mechanism correctly survives a clean restart cycle. After verification, it removes approximately 30 staged scripts from **/dev/shm** while preserving the persistence payload on the root filesystem. The cleanup script **clean3.sh** performs a separate sweep of scratch files and verifies that PAN-OS native shared-memory files remain intact.

## GlobalProtect Authentication Bypass (CVE-2026-0257)

Beyond the PAN-OS exploitation chain, the open directory contains forge\_cookie.py, a standalone tool that exploits [CVE-2026-0257](https://portal.hunt.io/vulnerability/cve/CVE-2026-0257) to forge GlobalProtect authentication override cookies. The tool requires no credentials and no prior access to the target.

Its technique:

1. Connect to the target over TLS and extract the CA certificate from the handshake (forcing TLS 1.2 so the Certificate message is sent in plaintext).
2. Extract the public key from the certificate.
3. Encrypt a forged authentication cookie for a specified username using RSA public-key padding.
4. Submit the forged cookie to the GlobalProtect gateway and portal endpoints to bypass authentication entirely.

The presence of this tool alongside the PAN-OS RCE chain indicates the operator maintained a toolkit for multiple Palo Alto Networks attack vectors. Once inside the network via the firewall exploit, the GlobalProtect bypass provides an alternative persistence and access mechanism through the organization's VPN infrastructure, which would survive the firewall being reimaged or patched.

Figure 17. Proof-of-concept exploit for CVE-2026-0257 targeting Palo Alto GlobalProtect. Extracts TLS public keys (unauthenticated), forges RSA-encrypted authentication override cookies, and tests gateway/portal endpoints. Uses cryptography library, network sockets, and plaintext TLS handshake parsing for full chain retrieval.
## Keycloak SSO and SAML Reconnaissance

A cluster of scripts in the open directory targets Keycloak SSO and SAML authentication infrastructure. The reconnaissance script **recon2.sh** performs Certificate Transparency log enumeration via **crt.sh** to discover subdomain names associated with the target organization, then resolves them via DNS and probes for Keycloak endpoints:

Additional Keycloak-focused scripts include **kc.sh**, **kc2.sh**, **kc3.sh** (endpoint enumeration and probing), **kctok.sh** (token acquisition attempts), **kcv.sh** (version detection), and **kcout.py** (output processing). The SAML scripts (**saml1.py**, **saml2.py**, **samldbg.py**, **samlfind.sh**) suggest the operator was also investigating SAML-based single sign-on integration with GlobalProtect.

## Internal Network Reconnaissance and Lateral Movement

Beyond the initial AD enumeration, the open directory contains a suite of tools specifically designed to map and move through the compromised organization's internal network. These scripts were executed on the rooted PAN-OS appliance itself, using the firewall's privileged position on the network boundary to reach hosts in the internal 10.100.0.0/16 range.

### Internal TCP Scanning

The script **scan.py** implements a multithreaded TCP port scanner designed to run from the compromised appliance using only Python standard library modules. It targets internal subnets with a curated list of **36 ports** spanning common enterprise services:

Companion scripts **scan2.py** and **scan3.py** expand this approach to additional subnets. The script dcports.py performs a focused port scan of the domain controller at 10.100.x.x, specifically targeting AD-relevant ports (LDAP, Kerberos, SMB, WinRM, RDP) to confirm service availability before launching more targeted attacks.

### SSH Credential Spraying Against Internal Hosts

The script **vssh.py** implements targeted SSH authentication attempts against internal hosts reached through the reverse tunnel. The script uses the Paramiko library to attempt connections with harvested SSH keys and a curated list of usernames and passwords targeting PAN-OS service accounts, VMware infrastructure accounts, and common administrative credentials. Target hosts are accessed through the reverse tunnel ports (127.0.0.1:2201 and 127.0.0.1:2202), corresponding to the two internal hosts mapped in **tun.sh**.

### On-Box Reconnaissance

The script **recon3.py** performs reconnaissance directly from the compromised firewall, combining SSH banner fingerprinting of internal hosts, SSH key and credential harvesting, and a targeted LDAP bind test against the domain controller using credentials extracted from the PAN-OS configuration. The script probes seven internal IP addresses for SSH service banners and validates LDAP credentials against the domain controller's LDAPS endpoint.

### Configuration Mining

The operator developed multiple scripts to systematically extract intelligence from PAN-OS configuration files on compromised appliances:

- **cfggrep.py** parses the merged running configuration XML to extract GlobalProtect gateway settings, tunnel interface definitions, User-ID agent configurations, internal address objects (including NAS, ESXi, vCenter references), static routes, and IPsec tunnel peers.
- **gp1.py** specifically targets GlobalProtect authentication override settings, client authentication profiles, certificate profiles, and portal/gateway entries, mapping the organization's VPN authentication architecture.
- **exfil.py** performs a comprehensive extraction of pivot-enabling material from the running configuration: HA SSH private keys (PAN-OS roots high-availability over SSH), device certificates with encrypted passphrases, LDAP bind credentials (decrypted in the configuration), address object inventories, and admin account definitions.
- **secrets2.py** and **secrectx.py** extract additional credential material from the appliance.
- **keys1.py** harvests SSH keys stored on the appliance for use in lateral movement.
- **blobs.py** processes encrypted configuration blobs.

Figure 20. Configuration extraction targets from exfil.py. The operator's own comments describe the extraction as enabling the move from "root on one firewall" to "inside the AD segment."

The output file **miner.out.gz** contains 14,806 lines of structured data extracted from **Panorama** saved configurations, including LDAP bind credentials, SAML/Keycloak endpoints, internal IP address inventories, managed device serial numbers, device groups, and firewall rules targeting domain controller subnets. Its presence on the VPS confirms that configuration extractions were completed and exfiltrated across multiple compromised hosts.

| Extraction Category | Items Found | Key Intelligence Value | 
|---|---|---|
| Configuration Files Parsed | 3 files | merged-running-config (941 KB), candidate-snapshot (19.8 MB), ha-remote-rc (568 KB) | 
| LDAP Server Profiles | 9 profiles | Bind DN/passwords for the target's internal AD domain, server addresses on port 636 (LDAPS) | 
| Authentication Profiles | 7 profiles | Auth methods mapped to user groups and access policies | 
| SAML IdP Entries | 4 entries | Keycloak SSO endpoints for two of the organization's SSO realms | 
| Secret Fields (encrypted) | 3 fields | LDAP bind password, 2 cryptographic keys (AQ==-prefixed PAN-OS encryption) | 
| Secret Fields (plaintext) | 22 fields | Key exchange algorithms, master-key settings, rekey intervals | 
| Certificate/Key Paths | 15 paths | Content certs, trusted root CA list (153 KB), internal certificates (18 KB) | 
| Internal Subnets | 25 unique /24s | 10.0.0/8, 172.16.0/12, 192.168.0/16 ranges across 5 major blocks | 
| Panorama-Managed Devices | 6 devices | Firewall fleet managed by the compromised Panorama instance | 
| GlobalProtect Gateways | 2 gateways | two GlobalProtect gateways (hostnames redacted) | 

The operator's own comments in **exfil.py** note that "the earlier copy on our controller got overwritten by another target," indicating the surviving file represents only the last of several extraction runs.

## AI-Assisted Offensive Tooling

The open directory contains extensive evidence that the operator integrated multiple AI systems into the attack infrastructure, not merely as coding assistants but as autonomous agents capable of reading offensive playbooks, downloading security tools, and preparing for AI-driven penetration testing. The session logs, database schemas, and configuration files provide a detailed record of how AI was deployed on this VPS.

### Timeline: AI Deployment on the VPS

The server's bash history reveals a clear sequence of AI tool installation on October 8, 2026. The operator first attempted to run claude (not yet installed), then installed npm via apt, and used it to install **Claude Code** (Anthropic's AI coding assistant) globally:

The configuration file **.claude.json** records the first launch of Claude Code at **08:48:10 UTC** on October 8, 2026 (version 2.1.293). Twelve minutes later, at **09:00:47 UTC**, the aiscan platform opened its first AI session using **DeepSeek v4-pro** as the primary model. The entire AI initialization sequence, from first session to full tool readiness, completed in **under nine minutes (09:00 to 09:09 UTC)**.

### The aiscan Platform: Multi-Agent Architecture

The aiscan directory contains a full installation of an AI-powered offensive security platform built around a multi-agent architecture. The core binary (**aiscan-full**) provides a web interface that was exposed on port 23522. Its configuration file (**aiscan.yaml**) reveals three AI backend providers and a **FOFA reconnaissance key**:

The platform's session logs reveal a multi-agent architecture designed for autonomous penetration testing. The AI reads structured "skill" files that define distinct agent roles:

Figure 24. The aiscan multi-agent penetration testing architecture as described in the platform's skill files.
The three agent roles operate as follows. The **pentest-coordinator** receives a target company or root domain, bootstraps an asset inventory, divides work into shards, and dispatches each shard to a **pentest-worker**. Workers execute autonomously: they scan their assigned shard using the platform's built-in tools, write findings to a central hub, and asynchronously dispatch any high-severity results to the **rce-verify** subagent. The rce-verify agent performs single-finding RCE verification, restricted to id/whoami proof and read-only operations. An **IOA** (Inter-Operator Async) message bus enables multi-agent collaboration across the system.

### Built-in Offensive Tool Suite

The aiscan platform provides a library of pseudo-commands (built-in wrappers around security tools) alongside an arsenal package manager for installing external binaries. The session logs show the AI systematically downloading and initializing **17 external tools** on October 8, all within a **two-minute window (17:05 to 17:07 UTC+8)**:

| Category | Tool | Type | Function | 
|---|---|---|---|
| Built-in pseudo-commands | gogo | Scanner | Host and service discovery | 
|  | spray | Scanner | Web probing and HTTP fingerprinting | 
|  | zombie | Scanner | Weak credential checking | 
|  | neutron | Scanner | Template-based POC execution (83 templates) | 
| Built-in recon | proton | Scanner | Secrets and sensitive data scanning | 
|  | passive | OSINT | FOFA/Shodan/Censys aggregated recon | 
|  | katana/playwright | Crawler | Web crawling and headless browser verification | 
| Infrastructure | arsenal | Utility | Security tool package manager | 
|  | cyberhub | Utility | Fingerprint-to-POC mapping database | 
|  | tmux | Utility | Session manager for concurrent operations | 
|  | proxy | Utility | Proxy node management for anonymized scanning | 
| Arsenal-installed (17 tools) | nuclei v3.11.1 | Scanner | Template-based vulnerability scanner | 
|  | httpx v1.12.0 | Probe | HTTP probing and technology detection | 
|  | subfinder v2.17.0 | Recon | Passive subdomain enumeration | 
|  | naabu v2.6.1 | Scanner | Port scanning | 
|  | + 13 more | Various | dnsx, katana, uncover, interactsh-client, shuffledns, alterx, cloudlist, mapcidr, tlsx, asnmap, proxify, urlfinder, notify | 

### Session Logs: The AI Reading Its Own Playbooks

The most revealing file is the 4.6 MB session log (**session-20261008-170047.789537789.jsonl**), which contains 15,080 event lines documenting a complete AI conversation with **3 turns and 448 discrete events**. The log shows, step by step, how an AI agent prepared itself for offensive security operations.

**Turn 1** (09:01 UTC, 66 events): The operator's English-language prompt, "you read my skill.md and so on," instructed the DeepSeek v4-pro model to internalize its offensive playbooks. The AI's reasoning chain (4,002 characters) shows it methodically planning which files to read. It then executed 22 glob and read tool calls, ingesting the full set of skill files: aiscan (ASM/pentest toolkit), pentest-coordinator (orchestration), pentest-worker (autonomous execution), rce-verify (RCE validation), report (OKF-style output), ioa-finding (vulnerability publishing), plus playbooks for every scanner (scan, gogo, spray, zombie, neutron, proton) and utility (arsenal, cyberhub, tmux, proxy, passive, katana, playwright, ioa). The AI's text response confirmed it understood its role hierarchy and verification standards:

**Turn 2** (09:05 UTC, 264 events): The operator switched to **Chinese**: "下载所有必要的工具及相关资源。" ("Download all necessary tools and related resources.") The AI's reasoning chain expanded to 15,027 characters as it analyzed all 22 arsenal tools, decided which to install (skipping gogo, spray, and zombie as built-in pseudo-commands, and iom as a C2 implant framework "not needed for ASM/pentest work"), and executed 55 bash tool calls to download and install 17 external security binaries. The arsenal manifest records all 17 installations completing between 17:05:34 and 17:07:44 UTC+8, a span of just over two minutes.

**Turn 3** (09:09 UTC, 117 events): A second **Chinese** prompt: "初始化所有工具，并确保它们可用。" ("Initialize all tools and ensure they are available.") The AI produced its longest reasoning chain (29,877 characters), systematically verifying every installed binary, building massdns from source as a dependency for shuffledns, testing all pseudo-commands, verifying that the FOFA-backed passive recon returned live results, confirming uncover/subfinder provider configurations, and running functional smoke tests on every core tool. The AI confirmed **83 built-in neutron templates** were operational and that nuclei had its full template library available.

### Database Schema: Purpose-Built for AI-Driven Penetration Testing

The platform's SQLite database (**aiscan-web.db**) contains 11 tables that reveal the system's intended operational workflow. The schema itself documents the platform's full capability:

| Table | Rows | Purpose | Key Columns | 
|---|---|---|---|
| chat\_sessions | 1 | AI conversation sessions | title, agent\_name, status | 
| chat\_aop\_events | 448 | All AI agent operation events | turn\_id, emitter, event\_json | 
| aop\_request\_journal | 4 | API request/response log | method (OpenSession, RunTurn) | 
| scans | 0 | Scan task tracking | target, mode, verify, sniper, deep, status | 
| pentest\_assets | 0 | Discovered asset inventory | type, value, source, parent\_id | 
| pentest\_findings | 0 | Vulnerability findings | severity, source\_tool, verified | 
| pentest\_rce\_results | 0 | RCE verification outcomes | target, vector, proof, privilege, status | 
| sco\_nodes | 0 | Security Context Objects | cstx\_type, data | 
| sco\_observations | 0 | Observation linkage | operation\_id, observed\_at | 

## Monitoring and Automated Recovery

The operator maintained automated monitoring to detect when compromised appliances went offline (due to reboots, firmware updates, or network changes) and to re-establish access automatically when they returned. The script **mon.sh** polls the root relay's health endpoint every 20 seconds for up to 80 minutes:

The companion script **watch\_recover.sh**, shown earlier, extends this concept: when the firewall comes back online and confirms root access, it automatically re-deploys the AD reconnaissance tooling without operator intervention. This level of automation indicates a sustained, multi-week campaign rather than an opportunistic one-time exploitation.

## Mitigation and Defensive Recommendations

- **Restrict Management Access**: Limit PAN-OS management interfaces to dedicated management networks or authorized administrator IPs. Never expose them directly to the internet.
- **Apply Security Patches**: Promptly install PAN-OS security updates and hotfixes, prioritizing vulnerabilities exploited in the campaign.
- **Monitor Persistence Artifacts**: Audit for unauthorized services, SSH keys, PAM changes, modified PHP files, and suspicious files in /usr/local/lib/.panops/ and /dev/shm/.
- **Detect Outbound Tunnels**: Monitor unusual outbound SSH connections from firewalls, reverse SSH tunnels, and SOCKS5 proxies on port 10700.
- **Strengthen Network Segmentation**: Restrict firewall access to internal systems, including domain controllers and VPN infrastructure. Rotate stored LDAP credentials and shared SSH keys.
- **Harden GlobalProtect and SSO**: Patch authentication vulnerabilities, enforce MFA, review SAML trust relationships, and monitor VPN logins for suspicious activity.
- **Prepare for AI-Driven Threats**: Strengthen continuous attack surface monitoring, accelerate patching, and use threat intelligence to detect emerging AI-assisted attacks.

## MITRE ATT&CK Matrix

The following table maps the techniques observed in this campaign to the MITRE ATT&CK framework for Enterprise.

| Tactic | Technique | ID | Evidence from Open Directory | 
|---|---|---|---|
| Reconnaissance | Active Scanning: Vulnerability Scanning | T1595.002 | FOFA-based scan of 19,182 PAN-OS management portals (paloalto\_all.csv). | 
|  | Gather Victim Host Information: Client Configurations | T1592.004 | Version fingerprinting via precon.py before exploitation. | 
|  | Search Open Technical Databases | T1596 | Certificate Transparency log enumeration (recon2.sh), DNS reconnaissance (dns1.py), FOFA API queries via aiscan. | 
| Resource Development | Acquire Infrastructure: Virtual Private Server | T1583.003 | VPS at 130.94.67\[.\]235 (AS154177, LIGHT NODE LIMITED, Tokyo) hosting payloads and receiving tunnels. | 
|  | Develop Capabilities: Exploits | T1587.001 | Custom PAN-OS exploit chain (panos\_rce\_poc.py), Fragnesia variant (pfrag.py), cookie forging tool (forge\_cookie.py). | 
|  | Obtain Capabilities: Tool | T1588.002 | Aiscan AI offensive platform, iox tunneling utility, ProjectDiscovery suite (nuclei, httpx, subfinder, etc.), Claude Code. | 
| Initial Access | Exploit Public-Facing Application | T1190 | PHP session.upload\_progress heap corruption on PAN-OS management interface via panos\_rce\_poc.py. | 
| Execution | Command and Scripting Interpreter: Unix Shell | T1059.004 | Shell commands executed through the change\_password.php root relay (su -c ... root). | 
|  | Command and Scripting Interpreter: Python | T1059.006 | Python-based exploit scripts (panos\_rce\_poc.py, pfrag.py, fpatch.py, scan.py, vssh.py). | 
| Persistence | Server Software Component: Web Shell | T1505.003 | change\_password.php replaced with root-capable command relay. | 
|  | Create or Modify System Process: Systemd Service | T1543.002 | pan-ops-init.service installed by install\_persist.sh. | 
|  | Boot or Logon Initialization Scripts: RC Scripts | T1037.004 | /etc/rc.local hook with PANOPSHELL marker via install\_persist.sh. | 
| Privilege Escalation | Exploitation for Privilege Escalation | T1068 | Fragnesia kernel LPE (CVE-2026-46300) via pfrag.py and fpatch.py; patches /etc/pam.d/su to pam\_permit.so. | 
| Defense Evasion | Masquerading: Match Legitimate Name or Location | T1036.005 | Webshell placed in legitimate PAN-OS PHP path; persistence directory named .panops to blend with PAN-OS files. | 
|  | Obfuscated Files or Information | T1027 | Base64-encoded tool transfer via deploy.sh chunk uploads; staging in volatile /dev/shm/. | 
| Credential Access | Unsecured Credentials: Credentials in Files | T1552.001 | PAN-OS running-config extraction via exfil.py (LDAP bind passwords, HA SSH keys, RADIUS secrets). | 
|  | Brute Force: Password Spraying | T1110.003 | SSH credential spraying against internal hosts via vssh.py through reverse tunnels. | 
|  | Forge Web Credentials: Web Cookies | T1606.001 | GlobalProtect authentication-override cookie forging (CVE-2026-0257) via forge\_cookie.py. | 
| Discovery | Remote System Discovery | T1018 | Internal TCP scanning of 10.100.0.0/16 via scan.py. | 
|  | Account Discovery: Domain Account | T1087.002 | AD/LDAP enumeration via adacl.py deployed through reverse tunnels. | 
|  | Network Service Discovery | T1046 | Port scanning of internal hosts from compromised firewall; service fingerprinting via gogo. | 
|  | Domain Trust Discovery | T1482 | SAML and Keycloak SSO probing scripts; GlobalProtect authentication profile enumeration. | 
| Lateral Movement | Remote Services: SSH | T1021.004 | SSH credential spraying via vssh.py against internal hosts through SOCKS5 pivot. | 
|  | Remote Services: Remote Desktop Protocol | T1021.001 | RDP access to internal hosts tunneled through reverse SSH infrastructure (tun.sh). | 
| Collection | Data from Local System | T1005 | PAN-OS configuration mining via exfil.py; extraction of HA pairs, LDAP configs, address objects. | 
| Command and Control | Protocol Tunneling | T1572 | Reverse SSH tunnels (tun.sh) from compromised firewalls to VPS on 8 ports. | 
|  | Proxy: Internal Proxy | T1090.001 | SOCKS5 proxy (socks.py) on localhost:10700 supervised by socksloop.sh. | 
|  | Ingress Tool Transfer | T1105 | Base64-chunked payload delivery via deploy.sh; tools served from VPS port 8080. | 

## Indicator of Compromise (IOC) table

| Indicator | Type | Description | 
|---|---|---|
| 130.94.67\[.\]235 | IPv4 | VPS hosting an open directory and receiving reverse SSH tunnels. AS154177 (LIGHT NODE LIMITED), Tokyo, Japan. | 
| :8080 | Port | HTTP file server on the VPS serving payloads to compromised hosts. | 
| :23522 | Port | aiscan AI offensive platform web interface on the VPS. | 
| /usr/local/lib/.panops/ | Path | Persistence payload directory on compromised PAN-OS appliances. | 
| pan-ops-init.service | Systemd Unit | Boot persistence service described as "PAN-os Operations Init." | 
| PANOPSHELL | String | Marker string in /etc/rc.d/rc.local identifying the persistence hook. | 
| change\_password.php | Relay | Default webshell relay location (replaces legitimate PAN-OS file). | 
| /dev/shm/.p2/ | Path | Staging directory for SSH keys and proxy scripts before persistence install. | 
| /dev/shm/.socks.py | Path | SOCKS5 proxy script in shared memory during staging. | 
| /dev/shm/.a/a.py | Path | AD reconnaissance tool staging location on compromised hosts. | 
| socksloop.sh | Filename | SOCKS5 supervisor loop script. | 
| tun.sh / tun2.sh | Filename | Reverse SSH tunnel persistence scripts (primary and secondary). | 
| adacl.py | Filename | Active Directory ACL reconnaissance tool served from VPS port 8080. | 
| aiscan-full | Binary | AI-powered offensive security scanning platform (134 MB). | 
| gogo / gogod.b64 | Binary | Compiled Go network discovery tool (4.3 MB) and base64-encoded variant. | 
| iox | Binary | Open-source tunneling utility (EddieIvan01/iox v0.4). | 
| CVE-2026-46300 | CVE | Fragnesia Linux kernel XFRM page-cache LPE used for privilege escalation. | 
| CVE-2026-0257 | CVE | GlobalProtect authentication override cookie forging vulnerability. | 

## Conclusion

The exposed directory documents the full lifecycle of a PAN-OS exploitation campaign, from reconnaissance of **19,182 internet-facing management portals** to root access, persistence, and enterprise-wide lateral movement. The chained exploitation of PHP and kernel-level vulnerabilities, including the adaptation of the **Fragnesia** exploit to smaller patch files, took deliberate engineering effort. Multiple persistence mechanisms, automated recovery scripts, and configuration-mining tools reveal a deliberate strategy for maintaining access and expanding from compromised firewalls into internal networks.

The aiscan multi-agent framework, driven by DeepSeek v4-pro and Kimi k3, shows AI being used to automate reconnaissance, vulnerability validation, and exploitation workflows. Anthropic's Claude Code was also installed on the VPS, but the capture shows no evidence it was used in the exploitation. The campaign's 25 confirmed root compromises, GlobalProtect authentication bypass, Active Directory enumeration, and access to additional enterprise firewalls show how far a single unpatched management interface can take an attacker.

[Track this PAN-OS campaign across IOCs and infrastructureOne VPS held the whole open directory, from the FOFA scan lists to the reverse SSH tunnels. Start free and pivot across the host, its certificates and the tooling it served to catch the next box before it lands in a blocklist.Start hunting now](https://hunt.io/get-started)

Related Posts

Related Posts

Related Posts
