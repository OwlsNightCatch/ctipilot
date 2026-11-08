---
title: Chained PHP2Shell Exploit Roots 25 Servers | Dream Research
author: Dream Research
url: https://dreamgroup.com/blog/chained-php2shell-exploit-roots-25-servers
hostname: dreamgroup.com
description: Custom PHP2Shell Exploit Chained with Kernel LPE to Root Versions of Palo Alto Networks PAN-OS Firewalls in the Wild
sitename: Dream Security
date: "2026-10-29"
fingerprint: b5901091fe822181
---
# Chained PHP2Shell Exploit Roots 25 Servers, including US Government Servers

*Updated: October 29, 2026.*

*Since this discovery, the Dream research team has been sharing updates and collaborating on an investigation with Palo Alto Networks, the vendor of the firewall in question. More information is available on the Palo Alto Networks website. Additional details are now included in the post itself.*

*Custom PHP2Shell Exploit Chained with Kernel LPE to Root Versions of Palo Alto Networks PAN-OS Firewalls in the Wild*

On October 25, Dream researchers uncovered artifacts of what appeared to be a Chinese AI-assisted campaign that rooted 25 servers, including systems in a US government-affiliated environment. The attacker combined PHP2Shell with a kernel privilege-escalation exploit to compromise exposed systems.

The affected devices run specific versions of Palo Alto Networks PAN-OS.

The exploited surface is the PAN-OS management web server, which also fronts the GlobalProtect portal. Palo Alto Networks’ Unit 42 has independently verified the attacker’s tooling and results, and Palo Alto Networks is releasing fixed PAN-OS versions across the affected branches.

After rooting the firewalls, the attacker launched attacks against Active Directory. The recovered artifacts confirm credential extraction and directory enumeration.

The operation illustrates how an exposed management interface can become a path into an organization’s identity infrastructure. For government defenders, vulnerability discovery is just the beginning, after which the real challenge extends from identifying vulnerable systems to understanding and containing the access a compromise makes possible.

*The research below was conducted with proactive threat hunting using Dream’s autonomous cyber research product, Hero.*

## Discovery

Dream researchers identified a complete attack operation that included a custom weaponization of the PHP2Shell exploit chain (CVE-2026-109618/CVE-2026-109619) paired with the Fragnesia kernel privilege escalation (CVE-2026-46300), target lists, exploitation logs, and approximately 40 custom post-exploitation scripts.

This included artifacts of a campaign that had rooted 25 PAN-OS firewall and management servers across the United States, Japan, Taiwan, and South Korea. Once rooted, the attacker zeroed in on three specific servers in a US government-affiliated environment.

The discovered artifacts revealed an operation that began with exploit development in a lab environment and ended with persistent access to a US government organization's internal Active Directory domain.

### AI Usage in Attack

We also observed some evidence of AI-assisted tooling in the attack infrastructure:

- Claude Code had been installed
- An AI-powered offensive security platform called aiscan was configured with Chinese LLMs DeepSeek and Kimi
- API keys for the Chinese reconnaissance platform FOFA were present

While we have no direct evidence that the AI tools were specifically used to write the exploit or the post-exploitation scripts, the code structure, commenting style, and consistency across \~40 scripts suggest AI-assisted development. That said, this operation does not appear to be a [fully autonomous nation-state attack](https://dreamgroup.com/blog/inside-a-multi-agent-ai-framework-used-to-compromise-government-entities-in-asia).

## The Exploit: Two Vulnerabilities Chained Into One Request

The attacker developed two separate exploits and chained them together to achieve root access on any internet-facing PAN-OS firewall running a vulnerable build in a single HTTP request without any credentials.

### PHP2Shell (CVE-2026-109618 / CVE-2026-109619) — Remote Code Execution

The implementation we recovered is a custom, non-public build, not a copy of any known public exploit for PHP2Shell. It follows the same underlying concept but appears to have been independently developed and tailored specifically for PAN-OS.

The vulnerability targets PHP's `session.upload_progress` mechanism on the PAN-OS management web server (appweb). PAN-OS uses PHP 8.0.30 with a high memory limit that enables the memory corruption stages of the attack.

The attack works in four orchestrated stages:

- **A1 — Memory Exhaustion (\~383MB):** The attacker floods the server with crafted multipart POST requests, each containing massive filenames and session progress data. This pushes PHP's memory allocator to its limits, forcing the system into a predictable memory layout.
- **B1 — Information Leak:** A second request forges the stale session ID length from A1, forcing an out-of-bounds read. The server's `Set-Cookie` response header carries the leaked pointer value — giving the attacker the base address of `libphp.so` in the running process.
- **A2 — Stale Reference Setup (\~500MB):** Another round of memory pressure initializes a session, leaving `http_session_vars` as a live `zend_reference`, then triggers a second OOM that leaves `mod_data=NULL` — creating a stale reference the attacker can forge in B2.
- **B2 — Code Execution:** The final request forges a PHP HashTable entry in the freed memory region. The forged entry's `pDestructor` callback points to `zif_system` (PHP's `system()` function), and its data points to a shell command string. When PHP's cleanup handler walks the HashTable, it calls the forged destructor — executing arbitrary commands as the `nobody` user.

### Fragnesia (CVE-2026-46300) — Kernel Privilege Escalation

Getting code execution as `nobody` isn't enough since SELinux confines `httpd_t` from modifying system files. In order to complete the root, the attacker chained in a second exploit: a Linux kernel vulnerability in the XFRM ESP-in-TCP subsystem.

Fragnesia uses page-cache writes to overwrite `/etc/pam.d/su` — replacing its authentication rules with `pam_permit.so` (accept all). Because the PAM file is only 774 bytes, the exploit uses a per-byte splicing variant to write it precisely. After the overwrite, `su root` succeeds without a password.

Both exploits run in a single B2 HTTP request. The total chain — from unauthenticated HTTPS connection to persistent root webshell — completes in under 15 minutes.

## The Lab: Version Profiling at Scale

The exploit is not a single fire-and-forget payload. It requires precise memory offsets that differ between PAN-OS versions — the address of `zval_ptr_dtor`, the address of `zif_system`, HashTable structure sizes, and memory geometry parameters that control the heap layout during each stage.

Among the recovered artifacts, we found 11 JSON version profile files — one for each PAN-OS version that had been tested:

Each profile contains the exact offsets extracted from the `libphp.so` binary of that version — with SHA256 hashes of each library, ELF build IDs, and precise memory geometry parameters (chunk sizes, fill counts, drain counts, spray offsets) tuned through lab testing.

The difference between "calibrated" and "provisional" profiles is notable — calibrated means the attacker tested the exploit against a running VM of that version and confirmed the memory geometry works. Provisional means they calculated offsets from the binary but haven't verified on a live instance.

## The Campaign Funnel: From 19,000 Discovered to 25 Exploited

With the exploit ready and profiles for 9 exploitable versions, the attacker launched a targeting campaign that followed a clear funnel:

### Stage 1: Global Discovery (19,000 targets)

Using FOFA — a Chinese internet asset search engine similar to Shodan — the attacker identified approximately 19,000 internet-facing PAN-OS firewalls worldwide. These were devices with management interfaces exposed to the internet, discoverable through certificate fingerprints and HTTP response signatures.

### Stage 2: Version Fingerprinting (5,000 alive)

A custom version scanner ran with 200 concurrent threads against all 19,000 targets, identifying which devices were actually online and what PAN-OS version they were running. Approximately 5,000 responded with version information.

### Stage 3: Geographic and Version Filtering (240 targets)

From the 5,000 alive devices, the attacker filtered to servers located in only United States, Japan, Taiwan, and South Korea. They then further filtered to versions matching their exploit profiles (the PAN-OS 12.1 and 12.2 branches running PHP 8.0.30). This produced a final target list of 240 firewalls.

Since US, Japan, Taiwan, and South Korea are the four primary strategic adversaries and intelligence targets for Chinese state-aligned cyber operations in the Pacific theater, this indicates potential nation-state adversary efforts.

### Stage 4: Automated Exploitation (24 rooted)

The 240 targets were fed into an automated batch runner that exploited them five at a time, with an 1800-second (30-minute) timeout per target. For each success, the batch:

- Ran the full PHP2Shell + Fragnesia chain
- Planted a 103-byte PHP root webshell in a publicly accessible directory on the firewall (`/unauth/php/change_password.php`)
- Verified root by executing `id` through the webshell
- Logged the target's hostname and IP to a success CSV
- Moved to the next target

At this point, 24 firewalls had been successfully rooted.

### Stage 5: Triage (2 firewalls prioritized)

For 22 of the 24 rooted firewalls, the attacker did nothing beyond planting the webshell. No persistence, no tunnels, no post-exploitation tools. The servers were effectively **owned and parked**, allowing the attacker to return through the webshell at any time.

Two servers seemingly associated with one target progressed beyond this stage. Both appeared to belong to a US government-affiliated environment.

### Stage 6: The Pivot (Shifting from Firewall to Domain)

Among the 24 rooted firewalls, two belonged to a US government-affiliated organization. The running configuration extracted from the first firewall revealed an environment with characteristics suggesting government affiliation: CAC (Common Access Card) authentication, a specific naming prefix, and standardized government-style asset naming. The configuration file contained the organization's complete internal network topology: domain controllers, a central firewall management server, a Keycloak SSO server, a GitLab instance, GlobalProtect VPN gateways, and the Active Directory domain.

The first firewall was rooted on Oct 23 at 18:14 UTC during the automated batch. But it crashed shortly after — likely from the \~900MB of exploit traffic — and never came back online. The attacker monitored it with 240 automated probes over two hours, waiting for it to recover. It didn't. The second firewall, whose certificate data definitively linked it to the target organization, had timed out during the original batch.

Recognizing the organization's value from the first firewall's configuration, the attacker created a separate, dedicated campaign and successfully exploited it on Oct 24 at 10:09 UTC.

Within hours, the attacker:

**Built a persistent tunnel into the internal network.**

An 8-port reverse SSH tunnel connected the compromised firewall back to the operator's infrastructure, forwarding access to:

- Domain controllers (LDAP, LDAPS, RDP)
- The internal firewall management server
- GlobalProtect VPN infrastructure
- A SOCKS5 proxy for arbitrary internal network access

The tunnel was wrapped in a systemd service and an `rc.local` boot hook, both launching scripts from `/usr/local/lib/.panops/` — it survives reboots and automatically reconnects.

**Exploited the management server through the tunnel.** At 11:35 UTC, less than 90 minutes after rooting the second firewall, the attacker used the newly gained server access and the same PHP2Shell + Fragnesia chain against a third government server - the internal firewall management server that was only reachable through the tunnel. This server centrally manages all of the organization's firewalls. Compromising it gave the attacker access to every managed firewall's configuration, credentials, and network settings. This brought the total number of servers exploited to 25.

**Launched an AD attack campaign from the management server.** Because the management server already had LDAP connectivity to Active Directory (it needs it to authenticate VPN users), the attacker used it as their launch platform for domain attacks:

- Decrypted the LDAP service account password — the device config stores it encrypted, but with root access the attacker has the master key. They extracted it in plaintext and hardcoded it into every subsequent script.
- Enumerated every user and group in the domain via LDAP queries.
- Sprayed passwords against every user account using organization-themed passwords. The domain had `lockoutThreshold=0` — meaning no account lockout, allowing unlimited spray attempts.
- Attempted to create backdoor AD accounts — both a user account (tried in every OU) and a machine account (exploiting the default `MachineAccountQuota` setting).
- Analyzed AD ACL chains for privilege escalation paths.
- Attempted SAML signing key extraction from the Keycloak IdP configuration.
- Probed Keycloak SSO for authentication bypass.

The attack results — whether the password spray found valid credentials, whether the backdoor accounts were created, whether SAML keys were extracted — stayed on the management server's local filesystem and were not among the artifacts we recovered. This means we cannot determine the full extent of the compromise.

### Management Server → Active Directory

## What the Attacker Has Now

From the recovered artifacts, we can confirm the attacker possesses:

- Persistent remote access to the organization's internal network via a boot-surviving reverse tunnel and SOCKS proxy — likely still active
- Root webshells on two firewalls and the firewall management server — likely still active
- The full Active Directory user and group listing — a complete organizational blueprint
- Decrypted LDAP service account credentials — enabling direct AD queries at any time
- Private keys harvested from the PAN-OS firewall filesystem — HA replication keys, SSL/TLS certificate keys, and device authentication keys
- Complete network topology — every IP, hostname, subnet, server role, and VPN gateway
- SAML IdP configuration with weak security settings (`validate-idp-certificate: no`)
- 22 additional parked firewalls across the US, Japan, Taiwan, and South Korea — ready for exploitation at any time

What we cannot determine is whether the password spray, backdoor account creation, or SAML key extraction succeeded. If any of these attacks worked, the compromise extends far beyond the perimeter firewalls into the organization's identity infrastructure.

## Attribution Indicators

We do not attribute this activity to a named threat actor. Palo Alto Networks’ Unit 42 tracks this activity as CL-UNK-1280 and attributes it to a Chinese-speaking attacker in the UTC+8 time zone. However, multiple indicators point to a Chinese-nexus operation:

## Conclusion

This operation demonstrates a level of preparation and capability that sets it apart from opportunistic exploitation. The attacker invested significant effort into vulnerability research — obtaining PAN-OS firmware, decrypting it, extracting PHP libraries, building precise memory profiles for 9 different software versions, and calibrating exploit geometry through lab testing. The exploitation itself was automated and efficient: 240 targets attempted in a single batch, with version-specific profiles selected automatically.

There was a clear-cut focus on government targets.

The attacker scanned 19,000 firewalls, rooted 24, and immediately identified the two that mattered. Within hours of compromising a US government-affiliated firewall, they had tunneled into the internal network, compromised a third server using the same PHP2Shell exploit, and launched a full Active Directory attack campaign — all through a chain that started with a single unauthenticated HTTPS request to a management interface that should never have been exposed to the internet.

The 22 other rooted firewalls remain parked with active webshells. The persistent tunnel into the US government organization is likely still running. And the attacker still has 19,000 fingerprinted targets they can revisit as they develop profiles for additional PAN-OS versions. Palo Alto Networks device telemetry shows continued exploitation attempts against exposed PAN-OS devices.

See the [Palo Alto Networks website](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/) for full guidance and indicators of compromise.

## Closing the Gap Between Discovery and Defense

For governments and critical infrastructure, finding a vulnerability is only the beginning. Defenders need to identify exposed systems, establish what attackers can exploit, and act before a foothold becomes a wider compromise.

Dream addresses that challenge through two complementary cyberdefense platforms:

- **Sphere scales national cyber defense.** It maps exposure, prioritizes risks, and detects and responds to attacks across government networks, tailored to each nation’s threats and infrastructure.
- **Hero scales cyber research.** Its autonomous research agents help experts investigate threats, discover and validate vulnerabilities—including in software without source code—and develop remediation guidance and patches. This is the tool that was used by Dream researchers to conduct the investigation detailed in this post.

Together, they connect deeper investigation with defense across the national attack surface.
