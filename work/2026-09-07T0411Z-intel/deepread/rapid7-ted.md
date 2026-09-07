# extract: served via trafilatura-direct
---
title: "DPRK APTs: Ted backdoor and curlRAT target South Korean media and automotive sectors"
author: Rapid
url: https://www.rapid7.com/blog/post/tr-dprk-apts-ted-backdoor-curlrat-target-south-korean-media-automotive-sectors/
hostname: rapid7.com
description: A new Linux toolkit, identified by Rapid7 Labs, has been targeting organizations across South Korea’s automotive and media industries with minimal detection. This previously undocumented framework, enabled threat actors to execute remote commands on compromised servers, inject malicious scripts into web traffic, perform credential harvesting, and engage in long-term surveillance.
sitename: Rapid7
date: "2026-09-03"
categories: ['Threat Research']
tags: ['cybersecurity company,managed detection and response,exposure management,managed security solutions,vulnerability management,exposure assessment platform']
---
## Overview

A new Linux toolkit, identified by Rapid7 Labs, has been targeting organizations across South Korea’s automotive and media industries with minimal detection. The campaign made use of a HAProxy instance named “ted backdoor”, alongside trojanized versions of crond, agetty, atd, sshd, and polkitd. This previously undocumented framework enabled threat actors to execute remote commands on compromised servers, inject malicious scripts into web traffic, perform credential harvesting, and engage in long-term surveillance.

The standout feature of this toolkit is its depth of integration with the target environment. The ted backdoor is compiled as part of the victim’s existing HAProxy version 2.8.12. It uses its native filter API, internal memory pools, event scheduler, and process management infrastructure to intercept traffic and hide from monitoring, while genuine load balancing traffic operates as expected.

Operating alongside this are an SSH keylogger, a curl-based RAT, and a stager. The RAT maintains a watchdog thread dedicated to tracking HAProxy’s health, and reporting it back to the operator’s infrastructure. The earliest uploads on VirusTotal date back to mid-2025 and the involved HAProxy 2.8.12-0fdb194 was released on 22 November 2024, establishing this as the earliest possible compilation date for this build.

The toolkit is attributed with medium confidence to DPRK APTs, given that the attacks Rapid7 observed were targeting South Korean media and automotive sectors, likely aiming at long-term espionage, the usage of simple xor-based encryption, custom substitution cipher, and the list of C2s hardcoded is associated to APT37 by [ThreatFox](https://threatfox.abuse.ch/browse/tag/RicochetChollima/) and [maltrail](https://github.com/stamparm/maltrail/blob/master/trails/static/malware/apt_37.txt). Analysis shows that the ted backdoor could be part of a broader framework covering nginx backdoor as well. The ted plugin registers a custom HAProxy filter that hooks the HTTP parser to inspect and log high-value traffic, steal session cookies, and perform a client IP selection to decide whether to inject custom scripts in the webpage being rendered.

## Technical analysis

Rapid7 researchers revealed that the toolkit was used in campaigns targeting South Korean automotive and media sectors likely dating back to early 2025. The number of trojanized binaries and functionalities found suggest the scope could be long-term cyber espionage and surveillance. However, gathered evidence does not suffice to establish a timeline nor how the initial access was performed.

At the time of analysis, both victims were running an edge webserver with ports 80, 443, and 25 exposed. Port 443 hosted the Groupware login portal and port 25 exposed a mail server. Either surface represents a plausible initial access vector consistent with documented Kimsuky tradecraft. Since the beginning of 2026 [Kimsuky](https://www.enki.co.kr/en/media-center/blog/analysis-of-kimsuky-s-attack-on-a-south-korean-groupware-vendor-using-a-new-gomir-family-variant) has been observed exploiting RCE vulnerabilities in externally accessible mail servers to compromise South Korean groupware vendors, while Groupware web portals represent the kind of exposed authenticated application that DPRK-nexus actors have repeatedly targeted for credential harvesting and exploitation. The specific entry point and any associated CVE remain unconfirmed pending further forensic evidence.

The scenario shown in Figure 1 assumes the initial access is obtained by exploitation of CVEs related to the Groupware portal.


*Figure 1: Attack chain partially reconstructed*

⠀

The threat actor begins by exploiting a vulnerability in the Groupware login portal running on the edge webserver, gaining an initial foothold in the DMZ. From there, they establish persistence and harvest credentials from the compromised edge host (e.g. SSH keylogger), which also doubles as a staging server hosting the trojanized system ELFs.

With a foothold on the edge, the attacker pivots inward and drops the stager onto internal servers. The stager checks for the presence of either crond or HAProxy, and only then deploys CurlRAT retrieving it either from its data section or the edge webserver.

In parallel, ted backdoor is dropped onto the HAProxy load balancer. Once active,it establishes its own C2 channel to the external operator infrastructure, enabling data exfiltration, command execution, and script injection. On the victim side, the compromised load balancer silently redirects or serves malicious content to selected clients browsing through it, completing the watering-hole loop.

### SSH keylogger

4bb923eb040aa13ca8fd409c31ee4729c60ddff32e350efe1c5a4a9168a065f5 intercepts legitimate users' plaintext passwords and saves them to an encrypted log file under /var/lib/sshd/c8c68e629bba773a10ac80012d10bf19.

*Figure 2: hardcoded master passwords in userauth_passwd()*

⠀

After checking that entered credentials are not equal to TA’s master passwords, userauth_passwd() proceeds to encrypt them using a custom substitution cipher recurring throughout the toolkit and base64 encoding.

*Figure 3: Substitution cipher used to encrypt credentials*

⠀

Pivoting from the above cipher, instances of polkitd, crond, agetty and atd binaries were identified using a similar encryption algorithm. Crond binaries were found to be delivered by a stager.

### CurlRAT Stager

The stager 5db1b6d52faf60b4f32d6fd0c7c938e4d05d29a14c32ded4a9668357c08b6a91 starts by decrypting its configuration strings using a 1-byte XOR, then verifies root privileges and profiles the OS checking system hostname, OS distribution and version IDs, kernel release and version numbers and CPU architecture to select the correct payload to drop. It decrypts the trojanized crond binary in memory, overwrites the system's legitimate daemon, and restarts the service. As shown below, only if HAProxy or cron are running on the system will it proceed to drop the backdoored crond.

*Figure 4: Stager configuration*

⠀

Checking for HAProxy presence is done as the binary, named by TA as ted backdoor. It also has RAT capabilities and plays a major role in the campaigns described. The embedded crond versions supported are CentOS 7.7, 7.8, 7.9 and Ubuntu 22.04 and after installing the backdoor, timestomping ensures the crond binary gets the same creation timestamp of /usr/bin/ssh. The stager ends by filtering out keywords such as tmp, wget cron and crond from Linux system logs using a staging file named /tmp/jasper-log, likely to blend in as the JSP (JavaServer Pages) engine in old Apache Tomcat versions, erasing any traces of the installation. The logs affected by the selective erasure are /root/.bash_history and the following under /var/log: messages, audit/audit.log, cmd.log, secure, syslog, auth.log.

09739441ed4599bac2f8159028f772f71e4b25c8badfff95574e56d7384f3dbe and fea1bc36632c71e5a839803469ef60ac47595d36b2c50934ac109ade6df06e61 are a different variant of the stager that fetches backdoored binaries from a compromised victim’s server without embedding any payloads.

### CurlRAT

The Ubuntu version is analyzed below, though CentOS samples follow the same logic except for the filepath used to hide config/staging files.

As for the stager, feeea9d0bf6ae7396d28271baa51ae50df5169ce5d32a516865856f91abc50b3 starts by decrypting configuration strings using a 1-byte XOR key (0x58).

*Figure 5: curlRAT configuration*

⠀

The main logic added to crond is executed via two threads. The first thread runs the start_routine function that creates the staging directory snapd under /var/lib, where it attempts to load the victim ID from /var/lib/snapd/g580. If network failures were previously recorded, it reaches out to a secondary domain – img.darklights.store – authenticating with api_token/ecd427ea8330a4ff73618483e00b9b41 and setting the User-token header to the victim ID to fetch updated configuration under /tmp/nimon.unix-docbase.8564479396043450766-db6fb4443bc, where it’s then copied into /var/lib/snapd/g105.

To decrypt the configuration, the first byte of the file initializes the seed of a feedback xor based cipher. Each poll cycle, a config file is fetched from the C2 server over HTTPS (falling back to HTTP on failure) using libcurl, with the victim token embedded in the User-token header. The fetched config is parsed for three single-character delimiters — **!** terminates the credential field, **#** marks the payload section, and ***** separates arguments — after which the credential field is compared against the local victim token.

If authentication succeeds, a single-character mode byte (ASCII **'0'** through **'5'**) preceding the delimiter “#” selects one of six handler routines via a jump table. Payloads embedded in the config are decoded through a two-stage pipeline: standard Base64 decoding followed by a rolling cumulative XOR cipher keyed from the decoded header. The C2 task handler sleeps for 43,200 seconds (12 hours) between polls by default, but the operator can activate a fast-poll mode by setting a flag, reducing the interval to 30 seconds. A retry loop calls the handler up to six times per cycle with five-second intervals, failing fast if the first attempt does not succeed. The table below shows the C2 commands accepted.

| Mode | Function | Description | 
|---|---|---|
| 0 | cmd execution | Base64 + XOR-decodes a command list from the config, executes each line via popen with stderr redirected to stdout, saves output into a 1 MB buffer, and sends the result back. | 
| 1 | config write | Decodes and writes a new config payload to disk, validates it, and sets the polling interval and fast-poll flag. If the validation fails, the C2 resets to img.monderhouse.space | 
| 2 | staged payload drop | Issues an authenticated HTTP POST to the C2 host with a task path as the body, streams the response to a temporary file, decompresses and moves it to the final drop path, unlinking the temp. | 
| 3 | reverse shell | Closes all file descriptors above 2, calls setuid(0) and setreuid(0, 0), forcing both its real and effective user IDs to root, and connects out before handing off to the shell dispatcher. | 
| 4 | beacon | Populates a 10 KB system-info structure and transmits it as a check-in beacon. | 
| 5 | PTY shell | A full interactive PTY shell, the payload consists of an ip:port. | 

Modes 0–2 and 4 use libcurl-based HTTP/HTTPS, hence the name curlRAT. All modes use Base64+XOR encoding/decoding applied to the payload. The victim ID is obtained by concatenating "cron_3.0pl1-137ubuntu3", system hostname, ipv4 address, and the hardware/OS UUID (read from /sys/class/dmi/id/product_uuid), then applying MD5 hash and converting it to uppercase.

The layer of encryption used for all C2 interactions consists of a feedback xor cipher using an initial random seed (modulo 240 + 10, 0<=seed<=249) and then applying Base64 encoding. The malware encapsulates the encrypted and encoded payload, the service name, and the telemetry type into a formatted application/x-www-form-urlencoded HTTP POST body (name=%s&value=%s&type=%d) which is sent to the C2 and authenticated using an hardcoded API token, including the victim ID in the User-token header.

The second thread acts as the HAProxy watchdog. Before entering the monitoring loop, it checks for the presence of the file /usr/lib/libvirtlog.so.0 to ensure the target is running in a virtualized environment, otherwise it sleeps 6 minutes and aborts. Then it accesses the MD5 victim ID under /var/lib/snapd/g580 to check if the node is active and compromised. Every hour the watchdog reads the pid at /var/run/haproxy.pid and monitors the status of HAProxy by polling /proc/pid. The status can be one of the following codes:

- 0 (Started): Process transitioned from stopped to running
- 1 (Stopped): Process is no longer active in the kernel process table
- 2 (Restarted): PID file timestamp modified, and a new PID is detected
- 3 (Reloaded): PID file timestamp modified, but the PID remained identical

The status is then sent to the C2 endpoint “writeservice_info” using the custom crypto layer and the telemetry type set to 0 (Figure 6).

*Figure 6: writeinfo_service monitoring HAProxy status*

⠀

The CentOS versions of curlRAT contain the same functionalities, except that functions are masqueraded as atd_ routines to blend in during static analysis.

*Figure 7: The two threads running curlRAT logic*

⠀

Below is the table summarizing the main RAT components.

| Capability Group | Functions Identified | 
|---|---|
| Reverse Shell / PTY | atd_reverse_try_root, atd_reverse_create_conn, atd_reverse_is_alive, atd_reverse_open_pty, atd_reverse_cleanup_tty, atd_reverse_open_term, atd_reverse_handle_sigs, atd_reverse_close_inherited_sockets | 
| C2 & Network Comms | atd_http_request, atd_response, atd_request, atd_download_to_file, atd_download_config, atd_encrypt_url, atd_decrypt_url, atd_check_haproxy, atd_write_callback | 
| Host Profiling & Recon | atd_get_hostname_info, atd_check_info, atd_get_ip_info, atd_get_system_info, atd_get_version_info, atd_get_machine_info, atd_get_service_info, atd_create_id, atd_get_id | 
| Command Execution & Crypto | atd_run_shell, atd_run_cmd, atd_run_module, atd_base64_encode, atd_base64_decode, atd_md5 | 

Earlier version of the RAT hardcode C2 without using XOR encryption (Figure 8).

*Figure 8: Default configuration curlRAT 8f30b57928934ae67478d0e690c91d046e35a638da098d02922a4a88a0fdb66c*

⠀

The atd_get_info() is a recon routine likely used to decide which binary trojanized next to ensure persistence on the node. It collects the service name of the compromised machine and sends it to the C2 via the atd_response routine together with Ipv4 address, OS version, and the list of services and listening port (Figure 9).

*Figure 9: Recon module output sent to the C2*

⠀

MODE, DELAY and SERVER_URL are parsed from the config file discussed previously. During the campaign observed by Rapid7, the RAT acts as a framework and constitutes the codebase to edit legitimate system daemons. Other trojanized instances found are agetty and polkitd, where we identified a similar pattern lacking the HAProxy monitor: the creation of a thread to run curlRAT, reaching to img.worksongo.store and img.socialteams.store respectively.

atd_encrypt_url and atd_decrypt_url leverages the substitution cipher “E1x0X3f2R5w4g7u6D968kAeCdBPEpDhGJF4IiHHKzJvMtLlOnNcQmPNSjR2UFTUWOVTYIXZZ5aWcQbbeqd7gYf3i8hykGjCmsl9oonrqSp0sVrauKtLwAvBy1xMz=.#,+/--__" shared with the ssh keylogger.

### Ted backdoor

The TA recompiled the HAProxy build 2.8.12 72e70936f0dbe459142a1d867617c35f8d0cce5d18c6a49e1090a2a5adc8e558 (18MB) to include a custom plugin (named ted_plugin) leaving debug strings naming the backdoor.

*Figure 10: ted_plugin compiled as part of the source code*

⠀

Figure 10 shows that the plugin was directly compiled with the rest of HAProxy source code and hooks directly the built-in HTTP parser relying on internal HAProxy structure for searching HTTP request headers. The custom filter defined to capture traffic is loaded via the ted_load_filter_config routine.

*Figure 11: my_filter_config struct*

⠀

The routine reads the implant's operational configuration from ~/cache/haproxy-1000.cache. Each field is decrypted in two layers: first ngx_decode applies a chained XOR seeded by the file's first byte; then ngx_decrypt_script applies a monoalphabetic substitution whose 67-entry mapping table is built at startup in ted_init_util from “E1x0X3f2R5w4g7u6D968kAeCdBPEpDhGJF4IiHHKzJvMtLlOnNcQmPNSjR2UFTUWOVTYIXZZ5aWcQbbeqd7gYf3i8hykGjCmsl9oonrqSp0sVrauKtLwAvBy1xMz=.#,+/--__" , and held in the ted_dec_dict uthash table keyed by Jenkins hash for O(1) lookup. The config carries the operating mode, all targeting regexes, every script rule with its payload paths and filenames, and the allowed operator keys. IP-based access control lists are loaded from haproxy-1001.cache and haproxy-1002.cache via the same decryption scheme. In other ted backdoor samples, the my_filter_config struct includes regexes to capture cookies as well.

After loading its configuration, it sets up signal handling via ted_register_reload_signal_handler() and saves its C2 pipe under HAPROXY_MWORKER_PP_READ and HAPROXY_MWORKER_PP_WRITE environmental variables to survive reloads and restarts, saving child process activity via ted_extra_log().

Below is the list of functions defined by the ted_plugin:

| Capability | ted_* routines | 
|---|---|
| HTTP interception and traffic hooking | ted_flt_register_ops2, ted_http_headers_for_htx, ted_chn_analyze_for_htx_constprop_0, ted_chn_analyze_for_htx_constprop_0_cold, ted_http_payload, ted_find_value_from_header_ist | 
| C2 and task execution | ted_pipe_master_thread, ted_pipe_worker_thread, ted_task_for_response, ted_alloc_task_context | 
| IPC and pipes | ted_init_main_pipe, ted_create_pipe_file, ted_create_multi_pipe_file, ted_make_pipe_name | 
| Configuration and rules engine | ted_load_filter_config, ted_reload_filter_config, ted_free_filter_config, ted_load_ip_set | 
| In-memory data structures | ted_set_add, ted_set_contains, ted_set_clean, ted_set_add_string, ted_set_contains_string, ted_set_clean_string | 
| Logging, file I/O | ted_extra_log, ted_save_capture_log2, ted_write_fd, ted_build_correct_path | 
| Initialization and persistence | ted_init_util, ted_register_reload_signal_handler, ted_regex_free | 

The HAProxy trace_ops struct is copied into my_filter_ops, and contains a hooked tracing method.

*Figure 12: my_filter_ops containing hooked methods*

⠀

trace_chn_start_analyze() is hooked via ted_chn_analyze_for_htx_constprop_0() that parses the HTX buffer — the memory region where HAProxy stores parsed, SSL-decrypted HTTP request. If an incoming request matches the endpoint "/favorite_list_2x_m500_ico.jpg" (Figure 13), the malware drops into a Command & Control mode, setting the field flag to 1 in the ted_rep_state structure that tracks the response state.

⠀

*Figure 13: Dropping into C2 mode*

⠀

First, it reaches into HAProxy's internal counters to decrement active connection stats, referencing fields from the proxy struct via hardcoded 2.8.12 offsets to clear any trace left: the per-backend beconn/feconn and the global actconn, then 64-bit fields within be_counters (cum_conn, cum_req, bytes_in, bytes_out) guarded against underflow, and 32-bit peak metrics (sps_max, conn_max, cps_max) decremented only when exactly 1. Secondly, it parses a custom hardcoded 14-byte header to obtain the payload length, then creates FIFO pipes via ted_make_pipe_name and ted_create_multi_pipe_file keyed on HAProxy's connection ID under /tmp (e.g. /tmp/t[ID]_w.pipe). If HAProxy is running in master-worker mode (MODE_MWORKER, bit 0x80), the connection ID is written to the pp_w2m pipe so the master process runs the dispatcher; otherwise a detached thread runs ted_pipe_worker_thread locally (Figure 13).

The HTX walk filters on block type 4, which is HTX_BLK_DATA, and writes each block straight into fdPipe with write(). Any short write aborts and closes the pipe. Afterwards to_forward, output, buf.head and buf.data on the request channel are all zeroed. That tells HAProxy there is nothing left to forward, so the attacker's command body never reaches a backend server. The C2 request terminates at the load balancer, and no backend ever logs it.

The C2 dispatcher logic is resumed in the table below.

| Command | Description | 
|---|---|
| Opcode '0' (0x30) | Beacon: returns a version banner including build ID (24112201), HAProxy version (2.8.12-0fdb194), master-worker mode status, and chroot path. | 
| Opcode '1' (0x31) | File upload: resolves path via ted_build_correct_path, writes file content via fopen(path, "wb"), and replies 1. Used to upload payload files for the injection path. | 
| Opcode '2' (0x32) | File download: reads a path, stats it, writes the 8-byte size, and streams the contents back with EAGAIN handling. | 
| Opcode '3' (0x33) | Command execution: executes commands via popen; merges stdout/stderr, appends " 2>&1", and streams output back XOR-encrypted. | 
| Opcode '9' (0x39) | Config update: writes new config to ~/cache/haproxy-1000.cache.bak, re-encrypts using chained XOR, validates via ted_load_filter_config, and renames over the active config file if successful. | 

All five handlers write the same “HTTP/1.0 200 OK” header with Content-Type: text/html into the read pipe before the body. That's what the response task then relays out via send() on the raw socket, which is why the traffic looks like an ordinary HTTP response on the wire despite never passing through HAProxy's response path. Output back to the operator uses a rolling XOR cipher where each plaintext block is the key used to encrypt the next block with a random 1-byte seed.

If the initial endpoint check does not match "/favorite_list_2x_m500_ico.jpg" and the filter is in capture mode, then traffic is selectively logged and victims are identified based on the capturelist_set field within the my_filter_config struct (Figure 11), containing the list of targeted IPs and subnets. It uses regular expressions to filter the incoming HTTP traffic, waiting for high-value requests (like a user hitting a /login endpoint or an admin panel).

When a victim's request matches the attacker's filters, the backdoor goes to work.

It extracts the victim's source IP, the requested Host, the Referer, and the User-Agent formatting the data in a single-line record using exclamation marks as separators**.**

*Figure 14: Real-time capturing of selected HTTP headers matching specific regexes*

⠀

The execution flow continues based on conf->action; zero means passive logging only, non-zero starts the injection path. A request then has to clear four conditions. It needs a User-Agent, and if agent_pattern is configured that regex has to match. Second, the code scans the User-Agent for the bytes x,6,4, it selects between the two payload paths the matched rule retrieving them ted_script_config struct (path_32 at offset 0x18 and path_64 at 0x20). Third, the script rule list is walked until one ted_script_config entry's URL and referer regexes both match, with a null referer counting as an automatic pass. Thus the operator catches a victim arriving at a specific page from a specific referrer, rather than spraying at everyone hitting a URL.


⠀

*Figure 15: Custom ted structure defined to inject malicious code in the page, and store regex rules and the connection context*

⠀

Fourth, the implant parses Accept**-**Language splitting on ; and =, pulling four operator-controlled fields: mrt for the 64-byte uid credential, msc for an 8-byte status, mst for an 8-byte score, and a fourth keyword read from off_355407 for a 1024-byte info blob. Parsing is order-independent and any subset can appear. If mrt yields a key, it must exist in allow_id_set, and that credential overrides IP filtering entirely, letting the operator reach the requested page from anywhere. It also upgrades the log record to the *-prefixed format carrying uid**,** status, score, and info. With no key, the fallback is IP-based: action == 1 requires whitelist membership, action == 2 requires blacklist absence, both checked twice, once with the final octet zeroed for /24 subnet matching and once for the exact host. 

Once all checks are cleared the chosen file is opened, stored in the per-connection ted_rep_state as fpAppend and nTotal, alongside a script_conf back-reference to the matched rule. The replace byte at offset 0x00 of that rule sets flag to 4 when zero and 2 when non-zero, distinguishing appending content from substituting it. Finally the code sets its filter flag and increments nb_rsp_data_filters or nb_req_data_filters on the stream, which is HAProxy's documented opt-in for body access– this time reusing the internal structure of the load balancer to inject code into the page at delivery time.

*Figure 16: Hooking the HTTP response*

⠀

Once a victim is marked for injection, two callbacks finish the job on the way out. ted_http_headers_for_htx runs first, and only when the data is on the response side, a state block is initialized during the request, and the transaction flag is set. It rechecks the response against the rule that matched earlier, testing Content-Type and the status line, so a payload is delivered only when the reply is a document worth modifying. It then reshapes the response to fit the incoming file: sets Content-Type, adds a Content-Disposition filename if the rule has one, writes the new body length into the custom length header, deletes Accept-Ranges so the client cannot request byte ranges and spot the size mismatch, and forces the status to 200 OK if it was anything else.

ted_http_payload performs the swap. For each body chunk, it takes only as much as the payload file has left, reads that slice from disk, decrypts it with ngx_decrypt_script, and substitutes it through HAProxy's own body-editing calls. When the replacement changes the body length, the code shifts every remaining filter's offset by the difference, so nothing downstream sees an inconsistency. With the rewritten length header and range support stripped, the size change leaves no trace.

trace_http_end handles the leftover bytes. The previous callback can only overwrite bytes that already exist in the response, so when the payload is larger than the original body there is a remainder with nowhere to go. This function runs at the end of the response and appends it. It checks that the state block is in an injection mode, that the headers were already rewritten, and that fewer bytes have been delivered than the payload holds. If so, it measures the free space left in the response buffer, reads exactly that much from the payload file, decrypts it with ngx_decrypt_script, and appends it as a new data block, bumping the channel's output count to match.

The result is that a payload of any size can be delivered across as many passes as it takes, using HAProxy's own scheduler to drive the process.

To ensure persistence, curlRAT is integrated and hidden as libc routines.

*Figure 17: ted backdoor including curlRAT configuration a8bfab4de81a1acb04aacdf757346946b0f5e30f0c9f402004016d0e425119c7*

⠀

## Attacker infrastructure

The observed infrastructure follows a consistent pattern: Domains are registered under low-cost commodity TLDs — .store, .space, .site, .autos — and use subdomain schemes mimicking image-serving CDN endpoints (img.) They then blend payload delivery traffic into normal web browsing. The naming convention across suggests a shared registration workflow rather than ad-hoc infrastructure. The img.responsive.pstatic.autos mimics Naver's pstatic.net static content domain, a South Korean web platform, which combined with the watering-hole delivery model adopted by the ted backdoor is consistent with targeting of Korean-speaking users.

## Attribution

At the time of the analysis, compromised servers had exposed the Groupware login portal on port 443, which is heavily present in Korean enterprise environments. The targeting of regional software (Groupware), mimicking Naver's static content domain, usage of simple xor and substitution ciphers and the watering-hole model already documented in the [Operation Code on Toast](<https://image.ahnlab.com/atip/content/file/20241126/(ENG%20ver)Operation%20Code%20on%20Toast(full).pdf>) (APT37) and [Operation Synchole](https://securelist.com/operation-synchole-watering-hole-attacks-by-lazarus/116326/) (Lazarus), allows medium confidence attribution to DPRK APT. The list of C2s hardcoded is associated with APT37 by [ThreatFox](https://threatfox.abuse.ch/browse/tag/RicochetChollima/) and [maltrail](https://github.com/stamparm/maltrail/blob/master/trails/static/malware/apt_37.txt).

The campaign's timeline and delivery mechanism overlap with Operation SyncHole, a concurrent Lazarus campaign documented by Kaspersky running from November 2024 through February 2025, in which Lazarus compromised South Korean media sites to redirect visitors to pages serving malicious JavaScript payloads. APT37 and Lazarus Group are distinct North Korean state-sponsored threat clusters assessed by [Mandiant](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-cyber-structure-alignment-2023) to operate under different DPRK agencies — APT37 under the Ministry of State Security, Lazarus under the Reconnaissance General Bureau — though both conduct cyber espionage targeting South Korean entities. Lazarus has been observed to deploy backdoored [open-source](https://ics-cert.kaspersky.com/publications/reports/2023/09/25/apt-and-financial-attacks-on-industrial-organizations-in-h1-2023/#korean-speaking-activity) programs to deliver malware and use feedback XOR + base64 to interact with the C2 by [Kaspersky](https://securelist.com/lazarus-andariel-mistakes-and-easyrat/110119/). As of July 2026, similar suspected initial access has been reported by [ENKI WhiteHat](https://www.enki.co.kr/en/media-center/blog/analysis-of-kimsuky-s-attack-on-a-south-korean-groupware-vendor-using-a-new-gomir-family-variant), suggesting that if a vulnerability in South Korean mail appliances exists, the exploitation could still be ongoing and leveraged by DPRK APTs.

Further evidence is necessary to make a more definitive assessment. Moreover, the presence of ngx_* prefixed routines within the ted backdoor suggest code reused from an nginx backdoor. The ngx_* prefixed routines were observed during the latest [Funnull](https://blog.xlab.qianxin.com/funnull-resurfaces-exposing-ringh23-arsenal-and-maccms-supply-chain-attacks/) campaign, where (similar to our case) a custom nginx filter was registered to hook HTTP traffic, and simple XOR encryption was applied to the configuration file. However, other than a similar naming convention, no significant code-level overlaps exist to support a stronger linkage.

## Conclusion

ted backdoor and curlRAT were designed to persist during long-term espionage operations with the ability to steal cookie sessions, credentials, redirect selected users, conduct drive-by download attacks, and hide evidence of the tampered page to a specific range of IPs to evade detection. Defenders should treat any edge component managing user traffic, SSL, or runtime modules with the same strict security standards as their main application servers. Relying on the component's own logs is not enough; securing these systems requires independent network correlation, memory behavioral analysis, and binary integrity checks.

## MITRE ATT&CK techniques

| **Tactic** | **Technique** | **Detail** | **Component** | 
|---|---|---|---|
| Initial access | [T1190] Exploit public-facing application | HAProxy filter API abused as injection point; watering-hole payload delivery via compromised load balancer | ted backdoor | 
| Execution | [T1059.004] Unix shell | popen() used for one-shot command execution per opcode '3'; PTY shell spawned per opcode '5'; reverse shell per opcode '3' in CurlRAT | ted backdoor, CurlRAT | 
| Execution | [T1106] Native API | pthread_create / pthread_detach for detached shell threads; HAProxy pool_alloc / task_wakeup for async response scheduling | ted backdoor | 
| Persistence | [T1574.006] Hijack execution flow: dynamic linker | Implant loaded as HAProxy shared library filter at process start; persistent across HAProxy restarts | ted backdoor | 
| Persistence | [T1543] Create or modify system process | Legitimate crond binary overwritten in-place; service restarted; timestomping to match /usr/bin/ssh creation time | Stager, CurlRAT | 
| Privilege escalation | [T1548] Abuse elevation control mechanism | setuid(0) / setreuid(0,0) called before reverse shell daemonisation; stager verifies root before payload drop | Stager, CurlRAT | 
| Defence evasion | [T1036.005] Masquerade: match legitimate name | crond, polkitd, agetty, atd binary names used; CentOS variant masquerades functions as atd_ routines in static analysis | Stager, CurlRAT | 
| Defence evasion | [T1070.002] Clear Linux logs | Selective keyword erasure (tmp, wget, cron, crond) from bash_history, messages, audit.log, secure, syslog, auth.log via /tmp/jasper-log staging file | Stager | 
| Defence evasion | [T1070.006] Timestomp | Backdoored crond given same creation timestamp as /usr/bin/ssh post-install | Stager | 
| Defence evasion | [T1562.006] Disable or modify OS logging | HAProxy connection counters (beconn, feconn, actconn, cum_conn, cum_req, bytes_in, bytes_out, sps_max, conn_max, cps_max) atomically scrubbed via hardcoded struct offsets | ted backdoor | 
| Defence evasion | [T1027] Obfuscated files or information | Config files encrypted with chained XOR + monoalphabetic substitution; payload scripts encrypted with substitution cipher; C2 comms protected with feedback XOR + Base64 | Stager, CurlRAT, ted backdoor | 
| Defence evasion | [T1497.001] Virtualisation/sandbox evasion | CurlRAT watchdog checks /usr/lib/libvirtlog.so.0 before activating; aborts if not in virtualized environment | CurlRAT | 
| Defence evasion | [T1480] Execution guardrails | Stager deploys only if HAProxy or cron are detected; CurlRAT validates victim token before handler dispatch; ted blacklists known scanner IPs | Stager, CurlRAT, ted backdoor | 
| Credential access | [T1556.003] Modify authentication process: pluggable authentication modules | SSH keylogger intercepts plaintext passwords; credentials saved to encrypted log at /var/lib/sshd/c8c68e629bba773a10ac80012d10bf19 | CurlRAT | 
| Credential access | [T1539] Steal web session cookie | Passive capture engine intercepts HTTP sessions; harvests Source IP, Host, URL, Referer, User-Agent, Accept-Language key via regex-gated filters | ted backdoor | 
| Discovery | [T1082] System information discovery | Stager profiles hostname, OS distro, version, kernel release, CPU arch to select payload; CurlRAT beacon transmits 10KB system-info structure | Stager, CurlRAT | 
| Discovery | [T1057] Process discovery | CurlRAT watchdog polls /proc/haproxy.pid hourly; tracks started/stopped/restarted/reloaded states; reports via writeservice_info endpoint | CurlRAT | 
| Collection | [T1185] Browser session hijacking | Response body replaced or appended with decrypted payload script via HAProxy data filter callbacks; Content-Type, Content-Length, Content-Disposition rewritten; 200 OK forced; Accept-Ranges stripped | ted backdoor | 
| Collection | [T1119] Automated collection | Passive capture logs timestamped records per matched request; expanded * records written when Accept-Language mrt key present | ted backdoor | 
| C2 | [T1071.001] Application layer protocol: web protocols | ted C2 tunnelled as HTTP through load balancer; CurlRAT polls C2 over HTTPS with libcurl fallback to HTTP; all payloads as application/x-www-form-urlencoded POST | CurlRAT, ted backdoor | 
| C2 | [T1132.001] Data encoding: standard encoding | All CurlRAT C2 payloads Base64-encoded after feedback XOR; ted pipe protocol uses raw bytes with rolling XOR session key | CurlRAT, ted backdoor | 
| C2 | [T1102] Web service | CurlRAT falls back to secondary C2 img.monderhouse.space on config validation failure; img.darklights.store used as backup config host | CurlRAT | 
| C2 | [T1572] Protocol tunnelling | Interactive shell tunnelled through HAProxy HTTP pipeline via named FIFOs; response exfiltrated via raw send() on TCP socket bypassing HAProxy logging | ted backdoor | 
| C2 | [T1568] Dynamic resolution | CurlRAT victim ID derived from hostname + IP + hardware UUID + cron version string, MD5'd and uppercased; used as User-token header in all C2 requests | CurlRAT | 
| Exfiltration | [T1041] Exfiltration over C2 channel | SSH credentials exfiltrated via CurlRAT C2; session capture logs written by ted; CurlRAT mode 0 streams command output back over same channel | Stager, CurlRAT, ted backdoor, SSH keylogger | 
| Exfiltration | [T1560] Archive collected data | SSH keylogger output encrypted with substitution cipher before writing; CurlRAT applies feedback XOR + Base64 to all outbound data | CurlRAT, SSH keylogger | 

## Indicators of compromise (IOCs)

### CurlRAT Stager

5db1b6d52faf60b4f32d6fd0c7c938e4d05d29a14c32ded4a9668357c08b6a91

09739441ed4599bac2f8159028f772f71e4b25c8badfff95574e56d7384f3dbe

fea1bc36632c71e5a839803469ef60ac47595d36b2c50934ac109ade6df06e61

### CurlRAT

83f7d565b0465546027052b597af46eae3a199e7a91fcc2ab936341147349130

7007a78d50a993cb174c685eba96eb442c9507e38fd9d8e5dffc712f613ec110

6cf1b5e92a9c0756f597a5ddefb38eba32961c52efac7ab2a0aa52c639a8fc53

ed72f4cd8d467b5c5d95ae6aeca4aaeea14d79565d379c1ca5871a714727be16

feeea9d0bf6ae7396d28271baa51ae50df5169ce5d32a516865856f91abc50b3

6cf1b5e92a9c0756f597a5ddefb38eba32961c52efac7ab2a0aa52c639a8fc53

d53c760c23b4405eb04ad0f20ead375440344b3bdf1fb7854ed12e40d155eabe - cronie

2f02b09d61d432134e994ad671258f523bbf289ae6091fd4eae192c60bd51b6f - agetty

8f30b57928934ae67478d0e690c91d046e35a638da098d02922a4a88a0fdb66c - atd

a1d8af3a6acb731f07f72040eccb3450c1c83d40e29f736c2a63d35388660be4 - polkitd

12810854c8b2c391b23e2e18b013e873d0369b0637aa3cf993136c07188ba3b8

009a1e2d7a582a24e50cf2ffc2a005482c8e38f22bf5ed416053855f8d054e1e

### SSH keylogger

4bb923eb040aa13ca8fd409c31ee4729c60ddff32e350efe1c5a4a9168a065f5

### Ted backdoor

94630b96f628c96a6bff7904b40ffc9ad67c86f8a4ff6080c3b524831c93f402

72e70936f0dbe459142a1d867617c35f8d0cce5d18c6a49e1090a2a5adc8e558

a8bfab4de81a1acb04aacdf757346946b0f5e30f0c9f402004016d0e425119c7

### C2

img.monderhouse.space

img.smartnords.site

img.darklights.store

img.responsive.pstatic.autos

img.socialteams.store

img.worksongo.store
