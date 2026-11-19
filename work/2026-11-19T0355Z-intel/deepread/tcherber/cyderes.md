---
title: "Exposing tcherber: VPN Access Brokerage, Custom Malware, & C2 Panel"
author: Howler Cell Research Team
url: https://www.cyderes.com/howler-cell/exposing-tcherber
hostname: cyderes.com
description: Howler Cell uncovers a cyber operation involving VPN access brokerage, custom malware, and live botnet infrastructure targeting enterprises.
sitename: Cyderes.com
date: "2026-11-17"
tags: ['Active Campaign']
fingerprint: "151ce45a46b48e80"
---
When sandbox evasion is enabled, the loader evaluates the host using a cumulative scoring model rather than relying on a single indicator. Systems exposing one logical processor, less than 2 GiB of physical memory, or a disk smaller than approximately 64 GiB each increase the score by one. The loader also enumerates running processes using the Toolhelp API and compares process names against a hardcoded list of analysis tools including **procmon.exe, wireshark.exe, processhacker.exe, x64dbg.exe, ida.exe, and ida64.exe**. Each detected analysis process increases the score by two, making active debugging or monitoring tools significantly more influential than basic hardware characteristics.

Figure 7: Username-based sandbox and analysis-environment detection.



Additional checks inspect sandbox-related environment values and the current username for strings such as **sandbox, virus, malware, and test.** These indicators contribute further points to the same score. Once the accumulated value exceeds two, the loader records the message **“Sandbox detected, exiting”** and terminates. This weighted approach reduces dependence on any single virtualization artifact and instead combines resource characteristics with evidence that the host may be actively used for malware analysis.

#### [In-Memory PE Manual Mapping]

PE payloads handled through the fileless technique are executed with an internal **64-bit PE manual mapper**. The loader validates the MZ and PE\0\0 signatures, parses the PE32+ headers, and extracts key fields such as ImageBase, SizeOfImage, SizeOfHeaders, section metadata, and the entry-point RVA. It then allocates a private PAGE\_EXECUTE\_READWRITE region with VirtualAlloc, copies the PE headers and sections into their expected virtual addresses, and applies base relocations when the image is not loaded at its preferred address.

Figure 8: In-memory PE allocation and copy during manual mapping.


The mapper also resolves dependencies manually by walking the import table, loading required modules with LoadLibraryA, and resolving imported functions through GetProcAddress. Execution is transferred to mapped\_base + AddressOfEntryPoint using CreateThread.

Figure 9: Entry-point execution of the manually mapped PE using CreateThread.


After launching the child process, the loader closes the associated handles, waits approximately five seconds, and attempts to delete the dropped executable from C:\Users\Public. This cleanup routine is intended to reduce the lifetime of the staged payload on disk.

#### HKCU Run-Key Persistence

The loader establishes user-level persistence through HKCU\Software\Microsoft\Windows\CurrentVersion\Run. Rather than calling registry APIs directly, it dynamically builds a reg add command and executes it through cmd /C. The created value is named SecurityHealth, uses the REG\_SZ type, and stores the target executable path; /f is supplied to replace an existing value without prompting. Before constructing the command, the loader also escapes embedded quotation marks in the executable path to preserve valid command-line syntax.

Figure 11: Registry-based persistence


Because the persistence entry is created under HKCU, it does not inherently require administrative privileges and causes the referenced executable to run when the current user signs in. The SecurityHealth value name also resembles legitimate Windows Security terminology, potentially making the autorun entry less conspicuous during casual inspection.

### Stage 3A - Rust Stealer: Credential Theft, Data Collection, and Exfiltration

Following execution of the Rust Loader, the campaign deploys a dedicated Rust-based stealer responsible for collecting credentials, application data, files, system information, and screenshots from the compromised host. Unlike the loader, which focuses on payload staging and execution, this module is designed for victim profiling, information theft, packaging, and exfiltration. It targets multiple data sources, including web browsers, FTP clients, email applications, cryptocurrency wallets, messaging applications, VPN software, gaming-related data, and selected files from directories such as Desktop, Documents, and Downloads.

The stealer also gathers host information and retrieves the victim's public IP address to build a profile of the infected system. Collected information is packaged into archive data before being transmitted to attacker-controlled infrastructure. Reverse engineering identified two exfiltration paths: Telegram-based delivery using configured bot credentials and direct reporting to the Zer0day Framework infrastructure at 93.152.223\[.\]30:5000.

#### Stealer Initialization and Victim Profiling

After execution is transferred to the Rust stealer's main routine, the **malware begins preparing information used to identify and track the compromised host**. It collects the system hostname and retrieves the victim's external IP address through dedicated helper routines. These values are later associated with explicit metadata fields including hostname and external\_ip, while the operating-system field is set to windows.

Figure 13: Victim profiling via hostname and external IP collection.


The resulting victim profile is incorporated into structured metadata used during later reporting and exfiltration. Reverse engineering identified fields including id, hostname, os, external\_ip, ip, zip\_path, and collected\_at, with the collection timestamp formatted using Rust's chrono implementation of RFC3339. Network activity from the sample also showed IP-geolocation requests associated with ipinfo.io, allowing the stealer to associate the victim's public IP with geographic information before constructing its reporting data.

#### Data Packaging and ZIP Creation

After completing the collection phase, the stealer consolidates the harvested information into a ZIP archive for exfiltration. The archive location is retained in the victim metadata through the zip\_path field, while collected\_at records the collection time using an RFC3339-formatted timestamp. Observed network traffic shows the resulting archive staged under the **victim's temporary directory with a victim-specific filename following the pattern \<victim\_id>\_logs.zip**.

Figure 14: ZIP archive exfiltration


The resulting ZIP acts as the primary container for the stolen material. Network capture reveals archive entries corresponding to **browsers, Cookies, and files collected from user directories including Desktop and Documents**. During transmission, the archive is attached to the multipart request as zip\_file with the MIME type application/zip, confirming that the packaged dataset is subsequently transferred through the stealer's exfiltration workflow.

#### Telegram and C2 Exfiltration

The stealer implements **two separate exfiltration paths** for transferring collected information from the compromised host. The first uses the Telegram Bot API, with the bot configuration obtained through BOT\_TOKEN and CHAT\_ID. The malware constructs multipart requests containing chat\_id, document, caption, and parse\_mode fields to upload the collected ZIP archive. The ZIP transmission uses the caption **ZIP logs**, while a separate multipart request uploads the captured screenshot using the photo field and the caption Screenshot. This shows that the archive and screenshot are handled as distinct Telegram uploads.

Figure 15: Telegram ZIP upload request construction.


In addition to Telegram, the stealer communicates directly with attacker-controlled infrastructure at 93.152.223\[.\]30:5000. The direct channel uses HTTP multipart requests to transmit the victim identifier, serialized metadata, and the collected ZIP archive. Observed traffic confirms a POST /api/stealer/report request containing the multipart fields victim\_id, data, and zip\_file, with the archive transmitted as application/zip. Together, these mechanisms provide the stealer with both Telegram-based delivery and a dedicated framework reporting channel for moving stolen information off the infected system.

#### Victim Registration and Reporting

Before the final reporting workflow, the stealer registers the compromised host with the attacker-controlled infrastructure using an HTTP request to /api/c2/heartbeat. The heartbeat contains a structured victim profile including the generated id, hostname, os, external\_ip, and ip fields. In observed traffic, the victim identifier follows a pattern combining geographic information, the public IP address, and a timestamp, providing the backend with a unique reference for tracking the infected system.

The C2 server responds to the heartbeat with a JSON object indicating whether registration was successful. In the observed session, the response was {"success":true,"command":null}, confirming that the victim profile was accepted by the backend. Although the response structure contains a command field, no command was returned during the captured communication, and the analyzed stealer does not provide sufficient evidence to classify this heartbeat mechanism as an interactive command-execution channel.

#### Browser Credential and Cookie Collection

The stealer targets browser-related information as part of its data-collection routine. Examination of the extracted archive reveals dedicated directories for browsers, Cookies, and Passwords, indicating that browser-derived data, session information, and credential-related artifacts are separated from other collected material before packaging.

The same archive also contains dedicated collection directories for FTP clients, email applications, messaging software, VPN data, cryptocurrency wallets, gaming-related data, and selected files from user directories. This structure demonstrates that browser information forms part of a broader credential- and application-data theft capability.

Overall, the Rust stealer functions as the campaign's primary information-theft component, combining host profiling, credential and application-data collection, file theft, screenshot capture, ZIP-based staging, and multiple exfiltration mechanisms. The use of both Telegram and dedicated Zer0day Framework endpoints provides the operators with separate channels for receiving stolen data while maintaining centralized victim registration and reporting.

### Stage 3B - Rust HVNC Implant

Howler Cell Reverse Engineering Team analyzed the Rust-compiled HVNC module downloaded from the live C2 during an ongoing investigation into the threat actor tcherber. The binary is a 64-bit Windows PE cross-compiled from a Linux build environment using the Rust stable toolchain.

Panic strings throughout the binary leak the build user's home path (/home/tcherber/) and the project's source tree (hvnc/src/implant/implant.rs, hvnc/src/implant/commands.rs), directly tying this artifact to the same handle observed on darkweb forums advertising Initial Access Broker and Malware-as-a-Service offerings.

#### Startup and Configuration

The HVNC module checks whether arguments were passed on the command line. If not, it uses default values embedded in the binary:

- **Build identifier:** J9kzQ2Y0qO
- **Credentials:** Guest$ / Admin@2024
- **C2 address:** 93\[.\]152\[.\]223\[.\]30
- **C2 port:** 5555
- **AES-256-GCM key:** 18a30346a7fdd1b9aba4fd3b46d06c05359d5332bd86e01987af8ae6684fb838

When three or more positional arguments are present, they override the host, port, and encryption key respectively. The key parser enforces exactly 32 bytes from a 64-character hex string and rejects anything else with "key must be 32 bytes".

A separate branch recognizes -s or server as the first argument and enters a standalone HVNC server mode. This analysis covers the implant/client path.

#### Anti-Analysis

Before opening any network connection, the HVNC module runs multiple defensive checks.

#### VM Detection

The HVNC module queries HKLM\HARDWARE\DESCRIPTION\System\BIOS\SystemManufacturer and compares against vmware, virtualbox, xen, microsoft corporation, and virtual. Any match causes a silent exit.

#### AMSI/ETW Patching

The HVNC module resolves AmsiScanBuffer and EtwEventWrite, flips the page protection, writes 0xC3 (RET) over the first byte of each, and restores the original protection. All subsequent operator activity runs with AMSI scanning and ETW event logging disabled.

#### Resource-Based Sandbox Detection

The HVNC module performs three additional environment checks that target the resource constraints typical of automated analysis sandboxes:

- **Physical memory:** Calls GlobalMemoryStatusEx and exits if total physical memory is below 2 GB.
- **Disk size:** Calls GetDiskFreeSpaceExA on C:\ and exits if the total disk capacity is 14 GB or less.
- **Uptime:** Calls GetTickCount and exits if the system has been running for less than roughly 10 minutes.

All three resource checks must meet their respective thresholds before execution proceeds to the C2 connection path. Combined with the VM manufacturer and processor-count checks, these mechanisms form a broader anti-sandbox gate designed to prevent the HVNC module from communicating from suspected analysis environments.

#### C2 Protocol

#### Connection Setup

The HVNC module creates a TCP socket configured with 5s receive timeout, 30s send timeout and connects with a nonblocking connect followed by select for writability. On failure, reconnect timer doubles each attempt, capping at 60 seconds.

After connecting, the HVNC module collects the **computer name, OS product name, architecture (hardcoded as x64), current user, working directory, IP address, and domain or workgroup**, then sends this as an encrypted registration beacon to the C2.

#### Packet Format

All traffic uses a custom protocol and the magic bytes **0x48564e43** (HVNC in ASCII).

The receive path reads the 12-byte outer header first and validates the magic at offset 0x00. It then reads the body length at offset 0x08 and receives the full body. If the body is 27 bytes or shorter, it is treated as a plaintext command frame: trimmed and dispatched directly with no cryptographic processing.

For longer bodies, the first 12 bytes are parsed as a per-packet crypto header containing three DWORDS that seed the GCM nonce and counter state. The authentication tag occupying the final 16 bytes is verified. Once the tag passes, the ciphertext between the crypto header and the tag is decrypted via the AES-256-GCM CTR keystream. The resulting plaintext is trimmed of Unicode whitespace and dispatched to the command router.

#### Command Surface

Commands are encoded as little-endian packed integers and matched via XOR-equality checks, dispatched through a switch on command length. Unmatched text falls through to cmd.exe /c, giving the operator unrestricted shell access.

#### Reconnaissance

| Command | Behavior | 
|---|---|
| systeminfo | Returns hostname, OS version, domain, user, architecture | 
| domain | Returns AD domain or workgroup | 
| admin | Returns privilege status | 
| ps | Full process listing via snapshot enumeration | 
| kill | Terminates a process by PID | 
| pwd / cd | Navigate filesystem | 
| screenshot | Fresh capture of the real visible desktop, returned as encoded image | 
| clipboard | Reads clipboard contents in Unicode text format | 

#### 

Credential Theft

| Command | Behavior | 
|---|---|
| passwords | Aggregates Chrome + Edge credential reports | 
| chrome\_pass | Chrome-only credential report | 
| edge\_pass | Edge-only credential report | 
| firefox\_pass | Firefox-only credential report | 
| chrome / firefox | Copies entire browser profile directory (cookies, local storage, session tokens, autofill) | 

#### 

Persistence and Escalation

| Command | Behavior | 
|---|---|
| persist | Attempts three persistence legs: writes HKCU\...\CurrentVersion\Run value WindowsUpdate pointing to the implant path creates a scheduled task WindowsUpdate with /SC ONLOGON /RL HIGHEST creates a WMI permanent event subscription (WindowsUpdateFilter / WindowsUpdateConsumer) that triggers at 120-130 seconds uptime. | 
| uac | Writes implant path to ms-settings\shell\open\command, sets DelegateExecute, launches fodhelper.exe, cleans up registry after execution. Returns "UAC bypass triggered" | 
| anydesk | Retrieves AnyDesk credentials/configuration from stored connection data | 

#### 

HVNC Lifecycle

The HVNC capability is built around a hidden Windows desktop named HVNC\_Session. When the operator sends hvnc\_start, the module creates this desktop via CreateDesktopA with GENERIC\_ALL access, falling back to OpenDesktopA if the desktop already exists from a prior session.

On success, a background thread is spawned that continuously captures the hidden desktop through the GDI pipeline (GetDC, CreateCompatibleDC, CreateDIBSection, BitBlt), JPEG-encodes each frame via the Rust image::codecs::jpeg::encoder, and publishes the latest buffer to global state. The operator retrieves frames on demand rather than receiving a continuous stream.

Applications launched on the hidden desktop via hvnc:chrome, hvnc:firefox, or hvnc:explorer are created with CreateProcessA with lpDesktop set to "HVNC\_Session". Because they run under the victim's user context, DPAPI-protected credential stores decrypt transparently, giving the operator full access to authenticated browser sessions.

An important operational distinction exists between the two stop commands. hvnc\_stop halts frame streaming only, leaving the desktop and launched applications alive for later reuse. hvnc:stop performs a full teardown, closing the desktop handle and orphaning any running processes.

| Command | Description | 
|---|---|
| hvnc\_start | Creates HVNC\_Session desktop, sets streaming flag, spawns capture thread. Returns "Streaming already active\n" if already running. | 
| hvnc\_stop | Clears streaming flag only. Desktop and launched apps remain alive. Returns "Desktop streaming stopped\n". | 
| hvnc:stop | Full teardown: clears streaming flag, resets desktop state, closes handle. Returns "HVNC stopped\n". | 
| frame | Returns latest cached JPEG from hidden desktop. No new capture triggered. Returns "NOFRAME\n" if none available. | 
| screenshot | Separate path: fresh capture of the real visible desktop via OpenInputDesktop. Not the hidden desktop. | 
| hvnc:explorer | Launches Explorer on hidden desktop via GetWindowsDirectoryA path. Returns error if HVNC not started. | 
| hvnc:chrome | Launches Chrome on hidden desktop via local appdata path. Returns error if HVNC not started. | 
| hvnc:firefox | Launches Firefox on hidden desktop via program files path. Returns error if HVNC not started. | 
| hvnc\_mouse \<x> \<y> | Binds thread to hidden desktop, repositions cursor via SetCursorPos, and posts WM\_MOUSEMOVE to the hit-tested window; input coordinates scaled from viewer to desktop resolution. | 
| hvnc\_click \<btn> \[down\] | Maps button/state to WM\_LBUTTONDOWN, WM\_RBUTTONUP, etc. PostMessageW primary, SendInput fallback. | 
| hvnc\_key \<vk> \[down\] | Injects virtual key event into hidden desktop's foreground window. | 
| hvnc\_scroll \<delta> | Posts WM\_MOUSEWHEEL with signed delta to foreground window. | 


Overall, the HVNC module transforms the compromise from passive data theft into interactive remote access. Through its encrypted C2 channel, credential-access commands, hidden desktop implementation, browser launching, persistence mechanisms, and remote input controls, the implant gives the operator sustained control over the victim environment while minimizing visible interaction on the primary desktop.

Analysis of the HVNC artifact also exposed shared development evidence that links it to a broader operator arsenal, including ransomware and network-access tooling discussed in the following sections.

## Related Operator Arsenal

### Enigma Encryptor

Howler Cell Reverse Engineering Team analyzed a Rust-compiled ransomware binary recovered during the ongoing investigation into the threat actor tcherber. The sample was identified through its Rust crate dependency paths, which contain the same build user home directory observed in the previously analyzed HVNC implant.

The binary is a 64-bit Windows PE that implements a full-featured ransomware operation: operator-controlled runtime gating through an extensive CLI interface, pre-encryption impact preparation (process killing, service disablement, shadow copy deletion, Defender suppression, Hyper-V shutdown, event log clearing), recursive file collection with configurable exclusions, per-file encryption using ChaCha12 with ECIES-wrapped key metadata, ransom note deployment, multi-vector persistence, a fodhelper.exe UAC bypass, network propagation with remote share targeting, and a watchdog mechanism for resilience.

**No data exfiltration transport was identified**. The network-capable paths support propagation and remote destructive administration only, not victim data upload. The embedded contact address is **Enigma\_1@aol.com**, and encrypted files receive the **.ENIGMA extension**.

#### Operator Controls

The ransomware accepts an extensive set of command-line flags that allow the operator to tailor each deployment to the target environment. These are parsed at the top of the entry function before any destructive action begins.

| Flag | Effect | 
|---|---|
| --no-admin | Skips the admin check and UAC elevation gate entirely | 
| --spread | Enables the network propagation thread | 
| --paths | Seeds explicit local target paths before default enumeration | 
| --no-wallpaper | Suppresses desktop wallpaper modification | 
| --force | Bypasses the already-encrypted guard, re-encrypts .ENIGMA files | 
| --no-notes | Suppresses \_README\_ENIGMA.txt ransom note drops | 
| --no-progress | Suppresses the progress reporting thread | 
| --no-scan | Skips default local and cloud-drive target enumeration | 
| --threads | Sets the encryption worker thread count | 
| --watchdog | Enables the guardian loop with persistence re-staging | 
| --main-pid | Supplies a PID for the watchdog to monitor; exits when that process dies | 
| --no-persist | Skips all persistence installation | 
| --no-antidebug | Skips all anti-VM, anti-sandbox, and debugger checks | 
| --hide | Hides the console window via GetConsoleWindow + ShowWindow | 
| --max-size | Skips files larger than the specified size in megabytes | 
| --logs | Enables operational logging (logs to C:\logs.txt) | 


This level of operator control is consistent with a ransomware builder or affiliate model where the same binary is deployed across different target environments with environment-specific tuning.

#### Execution Flow

The entry function follows a strict sequential order. Understanding this sequence matters because many steps are gated by CLI flags, and the operator can selectively enable or disable entire phases.

- Parse CLI configuration and project values into runtime flags.
- If **--hide** is set, hide the console window.
- If not already elevated and admin checks are enabled, attempt the fodhelper.exe UAC bypass.
- If anti-debug is enabled, run anti-VM, anti-sandbox, and debugger checks. Exit silently on failure.
- If **--watchdog** is set, enter the guardian loop. Otherwise continue.
- If **--spread** is set, launch the network propagation thread.
- Unless **--no-scan** is set, enumerate default local and cloud-drive targets.
- Install autorun persistence (unless **--no-persist**).
- Launch the recovery/defence impairment command batch.
- Kill targeted processes and stop/disable targeted services.
- Select worker thread count and optionally start the progress thread.
- Dispatch work into the encryption pipeline.
- Enter a post-run loop that repeatedly sleeps and re-stages the persistence copy.

#### Anti-Analysis

These checks execute unless --no-antidebug is supplied. Failure on any check routes to a delayed process::exit.

##### Registry, Device, and OEM Probes

The ransomware queries SCSI device identifiers at HARDWARE\DEVICEMAP\Scsi and system information values under SYSTEM\CurrentControlSet\Control\SystemInformation, checking Identifier, SystemManufacturer, and SystemProductName against virtualization vendor strings: **vmware, virtual, vbox, qemu, xen, and kvm**.

##### CPUID Vendor Check

Executes CPUID and compares the vendor string against KVM and VMware.

##### MAC Address Heuristics

Retrieves the first nonzero MAC address and compares against known virtual NIC vendor prefixes.

##### Debugger Detection

Reads PEB->BeingDebugged directly.

#### Sandbox Username and Path Heuristics

Compares the current username, computer name, and executable path against known sandbox indicators: **sandbox, cuckoo, malwareanalysis, virustotal, detectsample**, and common default usernames like **john, mary, admin, user, currentuser**.

This is a significantly more comprehensive anti-analysis suite than the HVNC module, reflecting the higher stakes of a ransomware deployment where sandbox detection is critical to avoiding early detection and signature generation.

#### Pre-Encryption Impact Preparation

Before any file is touched, the ransomware systematically dismantles the victim's ability to recover. This phase executes as a batch of shell commands launched sequentially.

#### Shadow Copy and Recovery Destruction

| Command | Purpose | 
|---|---|
| vssadmin.exe delete shadows /all /quiet | Deletes all VSS shadow copies | 
| wmic shadowcopy delete | Redundant shadow copy deletion via WMI | 
| powershell -NoProfile -Command Get-WmiObject Win32\_ShadowCopy │ ForEach-Object {$\_.Delete()} | Third-path shadow deletion via PowerShell | 
| wmic service where name='vss' call ChangeStartMode Manual | Sets VSS service start mode to Manual, preventing it from auto-starting on reboot; does not stop the currently running service or block immediate snapshot creation. | 
| net start vss | Restarts VSS briefly before deletion | 
| bcdedit /set {default} recoveryenabled no | Disables Windows Recovery Environment | 
| bcdedit /set {default} bootstatuspolicy ignoreallfailures | Prevents automatic repair on boot failure | 
| powershell -NoProfile -Command Disable-ComputerRestore -Drive 'C:\' | Disables System Restore on the C: drive | 

#### 

Defender and Security Suppression

| Command | Purpose | 
|---|---|
| reg add HKLM\SOFTWARE\Policies\Microsoft\Windows Defender /v DisableAntiSpyware /t REG\_DWORD /d 1 /f | Attempts to disable Windows Defender via policy | 
| reg add HKLM\SOFTWARE\Microsoft\Windows Defender\Features /v TamperProtection /t REG\_DWORD /d 0 | Disables Tamper Protection | 

#### 

Event Log Clearing

| Command | Purpose | 
|---|---|
| wevtutil cl application | Clears Application event log | 
| wevtutil cl system | Clears System event log | 
| wevtutil cl security | Clears Security event log | 

#### 

Hyper-V Shutdown

| Command | Purpose | 
|---|---|
| powershell -NoProfile -Command Get-VM │ Where-Object {$\_.State -eq 'Running'} │ Stop-VM -Force | Force-stops all running Hyper-V VMs to unlock their disk files for encryption | 

#### 

Symlink Evaluation

| Command | Purpose | 
|---|---|
| fsutil behavior set SymlinkEvaluation R2L:1 | Enables remote-to-local symlink evaluation | 
| fsutil behavior set SymlinkEvaluation R2R:1 | Enables remote-to-remote symlink evaluation | 


The symlink commands are notable. Enabling remote symlink evaluation allows the encryption engine to follow symlinks that cross network boundaries, potentially reaching files on mapped drives or UNC paths that would otherwise be unreachable through the local filesystem traversal.

The triple redundancy on shadow copy deletion (vssadmin, wmic, PowerShell) reflects operational maturity. If one method is blocked by endpoint protection, the others may succeed.

#### Process Termination

The ransomware kills processes to release file locks before encryption. It uses two parallel methods for each target:

- **taskkill /F /T /IM \<process>** for direct termination and
- **wmic process where name=\<process>.exe delete** as a fallback.

The target list contains 125 entries driven from an embedded table.

#### SQL and Database Processes

| Target | Family | 
|---|---|
| sqlservr, sqlwriter, msmdsrv, sqlbrowser, ssms, sqlagent, sqlce, sqllocaldb, sqlps, sqlanywhere, sqlserver, sqlwb, sqladhlp, sqlctr, sqlse, sqlang | Microsoft SQL Server | 
| mysql, mysqld, mysqldump, mysqladmin, mysqlmanager | MySQL | 
| mariadbd, mariadb | MariaDB | 
| postgres, pg\_ctl, pgadmin, psql, pg\_dump, postmaster | PostgreSQL | 
| mongod, mongos, mongo | MongoDB | 
| redis-server, redis-sentinel | Redis | 
| oracle, tnslsnr, oracle.exe, emagent, ocssd, crsd | Oracle | 
| cassandra, elasticsearch, rabbitmq | Other databases | 

#### 

Backup and Virtualization Processes

| Target | Family | 
|---|---|
| vmms, vmsp, vmpvw, vmcompute, vmswitch | Hyper-V | 
| veeam, Veeam.Backup, VeeamAgent, VeeamCrypto, VeeamMount | Veeam | 
| acronis, trueimage, acronisagent, acrocef | Acronis | 
| nbu, bp, VxSvc, netbackup, nbk, nbsvc | Veritas NetBackup | 
| cv, Galaxy, commvault, cvd | Commvault | 
| be, beremote, bengine, bebackup | Backup Exec | 
| carbonite, carboniteagent | Carbonite | 
| arcserve, asbackup, cas | Arcserve | 
| shadowprotect, sp, spagent, sprt | ShadowProtect | 
| dpm, dpma, dpmra | DPM | 

#### 

Cloud Sync and Productivity

| Target | Family | 
|---|---|
| googledrivesync, googledrive, GoogleDriveFS | Google Drive | 
| dropbox, dropboxext | Dropbox | 
| onedrive, OneDriveStandaloneUpdater | OneDrive | 
| icloud, iclouddrive, AppleCloudKit | iCloud | 
| boxsync, boxedit | Box | 
| megasync, MEGA | MEGA | 
| FileCoAuth | Office co-authoring | 
| excel, winword, outlook, powerpnt, msaccess, onenote, mspub, infopath, lync, skype, thunderbird, thebat, outlook32 | Office and email | 
| firefox, chrome, iexplore, edge, opera, brave | Browsers | 
| steam, origin, epicgameslauncher | Gaming | 
| vmware, VirtualBox, vbox, qemu | Desktop virtualization | 


The breadth of the kill list is significant. It targets every major database engine, several distinct backup products, all major cloud sync clients, all common browsers, and the full Microsoft Office suite. **It reflects either direct operational experience with what holds file locks in enterprise environments or a well-maintained shared target list across the ransomware ecosystem**.

#### Service Disablement

A separate service-target table (53 entries, distinct from the process list) drives a three-command sequence for each service:

- net stop \<service> /y
- sc stop \<service>
- sc config \<service> start=disabled

The net stop with /y handles dependency chains. The sc config ensures the service cannot restart after reboot.

| Target Pattern | Family | 
|---|---|
| MSSQLSERVER, SQLSERVERAGENT, SQLWriter, MSSQLFDLauncher, MSSQL$\* | SQL Server | 
| MySQL, MySQL80, MySQL57, MariaDB, PostgreSQL, pgsql, MongoDB, Redis | Other databases | 
| OracleService\*, OracleTNSListener | Oracle | 
| vmms, Hyper-V\* | Hyper-V | 
| Veeam\*, VeeamMountSvc, VeeamAgentSvc | Veeam | 
| Acronis\*, AcrSch2Svc, AcronisAgent | Acronis | 
| NetBackup\*, BP\*, VxSvc | Veritas NetBackup | 
| CommVault\*, CV\* | Commvault | 
| BackupExec\*, BESVC | Backup Exec | 
| DPM\*, DPMLA | DPM | 
| ShadowProtect\*, SP\* | ShadowProtect | 
| GoogeDriveSync (misspell as seen in code), GoogleDriveFS, DbxSvc, DropboxUpdate\*, OneDrive\*, OneSync\*, iCloud\*, Apple\* | Cloud sync | 
| vss, WinDefend, MSEService, McAfee\*, Norton\*, Kaspersky\*, wscsvc, SecurityCenter, MpsSvc, Sense, wuauserv | Security and Windows services | 

Some names overlap deliberately with the process kill list (e.g. vmms). This is intentional duplication across two control paths: one kills the process, the other disables the service to prevent restart.

#### Encryption Scheme

Enigma uses a hybrid encryption model: ChaCha12 for fast symmetric file encryption, with ECIES (Elliptic Curve Integrated Encryption Scheme) to protect the per-file key material so that only the operator's private key can recover it.

For each file, the worker generates two independent random values: a 32-byte ChaCha12 key and a 12-byte nonce, both from BCryptGenRandom. The file body is XORed with the ChaCha12 keystream derived from these values. The key and nonce are then individually wrapped using ECIES against an embedded public key:

- **049fdc6fb7c5bee17a942fc3cc40ff54aedbab6743d22e22fbb135d94ccbe9577ca49aa1c24386bd7720b9cba7cbf40c0ae04237d398f5b87194610f391f91118f**

#### Encrypted File Layout

The encrypted file is structured as a single contiguous stream with no footer. The file begins with the ECIES-wrapped 32-byte ChaCha12 key and is followed by a two-byte || delimiter.

Next comes the ECIES-wrapped 12-byte nonce, followed by another || delimiter. The remainder of the file from that point onward is the ChaCha12-encrypted body, which is the same length as the original plaintext. **The only place where the symmetric key and nonce exist in recoverable form is inside those two ECIES-wrapped header blobs, meaning the operator's private key is the main recovery path**.

#### Exclusions

The engine skips files and paths needed for boot and OS function:

- **Extensions:** .sys, .com, .scr, .inf, .reg
- **Folders:** windows, system32, system, system volume information, efi, boot, perflogs, $recycle.bin, windows.old, recovery, config.msi
- **Filenames:** boot.ini, bootmgr, bcd, desktop.ini, config.sys, autoexec.bat, \_readme\_enigma.txt, thumbs.db, ntuser.dat, pagefile.sys, hiberfil.sys, swapfile.sys

The **--force** flag bypasses the .ENIGMA guard, allowing re-encryption of previously processed files.

#### Ransom Note

When a directory qualifies for encryption and note suppression is not active, the ransomware drops \_README\_ENIGMA.txt containing:

ENIGMA Locker

Your files have been encrypted.

To recover your files, contact us: Enigma\_1@aol.com

Your unique ID: \<ID>

#### Persistence

#### Autorun Registry

The persistence installer writes multiple masqueraded autorun entries to both HKCU and HKLM:

| Registry | Value Name | 
|---|---|
| HKCU\Software\Microsoft\Windows\CurrentVersion\Run HKLM\Software\Microsoft\Windows\CurrentVersion\Run | EnigmaUpdater | 
| HKCU\Software\Microsoft\Windows\CurrentVersion\RunOnce HKLM\Software\Microsoft\Windows\CurrentVersion\RunOnce | WindowsSecurityService | 
| HKCU\Software\Microsoft\Windows\CurrentVersion\Run HKLM\Software\Microsoft\Windows\CurrentVersion\Run | SystemRestoreAgent | 

#### 

Self-Copy Staging

A separate staging function derives a self-copy path for enigma\_guard.exe and copies the current executable. This function is called both during the initial persistence setup and repeatedly from the watchdog loop and the post-encryption persistence re-staging loop.

#### Watchdog

When **--watchdog** is enabled, the ransomware enters a guardian loop that repeatedly calls the self-copy staging function to refresh persistence. If --main-pid is supplied, the loop also monitors the specified PID via OpenProcess and GetExitCodeProcess, exiting when the monitored process terminated. This allows an operator to chain the watchdog to a parent process.

## Offensive Toolkit and Infrastructure

After identifying the /home/tcherber/ build path in the HVNC and Enigma binaries, the Howler Cell team conducted OSINT pivoting on the tcherber identifier across threat intelligence platforms and code repositories. A lookup on the username returned a collection of Go source files comprising a **self-contained offensive toolkit designed for VPN-based initial access, internal network reconnaissance, Active Directory enumeration, and credential validation**. A parallel search for tcherber on darkweb forums surfaced two posts on rehubcom\[.\]pro advertising capabilities that closely match the discovered toolkit.

**A credential database (processed\_config.txt) containing 500+ validated FortiGate VPN credentials and operational logs confirming full network tunnel establishment into multiple victim organizations were recovered alongside the toolkit**.

### Toolkit Inventory

The hunting results contained Ten Go source files with timestamps spanning October 2025 through November 2025, plus configuration and output files generated during active operations in May and June 2026.

### Source Files

| File | Description | 
|---|---|
| Main.go | Main entry point for the Go toolkit, responsible for initializing the application and coordinating execution of the supporting modules. | 
| csicl.go | Orchestrator. Runs the full attack chain in sequence: launches the VPN connection in the background, waits for the tunnel to stabilize, then executes route parsing, LDAP enumeration, and reporting. All UI strings and comments are in Russian. Versioned as v2.2 (DEBUG MODE). | 
| forti\_vpn.go | FortiGate VPN client wrapper using OpenConnect with --protocol=fortinet. Auto-discovers the TLS certificate hash on first connection by sending a dummy hash and parsing the server's rejection. Maintains persistent connectivity with a 30-second reconnect loop. | 
| sonik.go | SonicWall VPN client wrapper using NetExtender. Probes seven URL paths on the target to auto-discover the VPN authentication domain by scraping login page HTML against ten regex patterns. Supports exponential backoff up to 5 minutes. | 
| netexec\_scaner.go | Credential validation and remote execution across Windows hosts. Likely a Go reimplementation of CrackMapExec/NetExec functionality. Outputs validated credentials to smb\_valid.txt. | 
| nxc\_ldap.go | Active Directory and LDAP enumeration. The largest file in the toolkit, indicating thorough AD recon capability (users, groups, domain structure, domain controllers). Outputs to ldap\_valid.txt and ldap\_domains.txt. | 
| smb\_info.go | SMB share and host enumeration. Collects OS versions, share names, and host metadata across target subnets. | 
| nmap.go | Lightweight port scanner for internal network discovery after VPN tunnel establishment. | 
| route\_parser.go | Parses internal network routes and DNS servers obtained from VPN connections. Feeds subnet and gateway information into the recon pipeline. Updated November 19, 2025, indicating continued development. | 
| reporter.go | Aggregates and formats output from all other tools into structured result files for operator review. | 

### 

Credential and Configuration Files

| File | Format | Description | 
|---|---|---|
| processed\_config.txt | ip:port:login:password | Master credential database. 500+ FortiGate VPN entries spanning multiple countries. Contains a mix of default credentials (guest:guest, admin:admin, test:test) and organization-specific passwords, indicating both brute-force harvesting and credential dump sourcing. | 
| input\_vpn.txt | ip:port:login:password | Relay server entries with guest:guest credentials across non-standard ports (44381, 12000, 10443). These are the operator's own proxy infrastructure, not victim targets. | 
| input.txt | ip:port;login;password | SonicWall target list (semicolon-delimited, distinct format from the Fortinet files). | 

### 

Orchestrated Attack Chain

The orchestrator (csicl.go) defines the automated attack sequence. When launched, it executes the following steps without operator intervention:

- Launches **forti\_vpn.go** as a background process with a 20-second stabilization delay.
- Runs **route\_parser.go** to map internal subnets and gateways from the established VPN tunnel.
- Runs **nxc\_ldap.go** for Active Directory enumeration.
- Runs **reporter.go** to aggregate results.
- Checks for output files (smb\_valid.txt, ldap\_valid.txt, smb\_domains.txt, ldap\_domains.txt) and reports completeness.

The remaining tools (nmap.go, netexec\_scaner.go, smb\_info.go, sonik.go) are not called by the orchestrator and are intended for manual use by the operator as needed. **sonik.go serves as an alternate entry point for targets running SonicWall instead of FortiGate**.

## Attribution and Operator Correlation

### Darkweb Forum Correlation

Using the same tcherber search pattern, the Howler Cell threat intelligence team identified two forum posts on rehubcom\[.\]pro whose described capabilities align closely with the toolkit surfaced through our research.

The first post advertises access to Fortiki, Ciski, Citrix (Russian slang for FortiGate, Cisco, and Citrix appliances) obtained through "brute-forcing a custom recording" and an "exploit toolkit." The poster describes an automated FortiGate checker that outputs validated access in a structured format including IP, GEO, login, password, access level, SSH status, LDAP presence, device count, and VPN user count. The poster segments targets by revenue (above/below $10M) and organization type and explicitly excludes CIS targets.

The second post advertises C2 / Loader Build + FUD crypt for Win or Unix targeting USA, CA, Europe, offering to "reconfigure the build to suit your needs" for a percentage-based fee. This directly maps to the recovered Rust loader's CLI reconfigurability (host, port, key overrides without rebuilding) and the HVNC module's configurable defaults. The mention of "Win or Unix" is consistent with the Rust cross-compilation from Linux to Windows observed in both the HVNC and Enigma binaries.

Both posts share the same Tox contact ID:

- 48B547A7A6195593B9158E4B6160ED0310B2F9AD080992D44EA299878DCCD0551CC7CAD168CD.

### Build Path Evidence

The tcherber identifier appears across multiple build artifacts spanning Rust and Go. The Rust-compiled HVNC module contains panic strings with /home/tcherber. The Enigma ransomware contains Rust crate dependency paths under /home/tcherber/.cargo/registry/src/. The Go-based toolkit contains module paths referencing /home/tcherber/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.25.3.linux-amd64/src/internal/abi/escape.go.

This means all three components (Rust implants, Rust ransomware, Go offensive toolkit) were built on machines where the tcherber user account has development environments configured for Rust and Go. Whether this is a single machine or multiple machines sharing the same username, the build identity is consistent across the entire arsenal.

### Continued Activity: STANDALONE C2 Panel v3

While tracking payloads compiled under the same /home/tcherber/ build path, the Howler Cell team identified an additional Rust-compiled binary named work\_video.exe. Analysis confirmed it is a C2 agent for the STANDALONE C2 PANEL v3, a web-based botnet management platform with an entirely Russian-language interface. The agent calls back to 158\[.\]94\[.\]209\[.\]138, where the panel is hosted openly at hxxps://158\[.\]94\[.\]209\[.\]138\[.\]sslip\[.\]io/ with no authentication gate, exposing the full operator interface to anyone with the URL.

This represents the most current indicator of active operations by the tcherber actor. The panel was live and serving payloads at the time of writing.

### Panel Capabilities

The panel provides six functional modules accessible from the left navigation: Victims, Builder, Cryptor, Delivery, Auto-Load, and Config. Together these form a complete botnet operations pipeline, from agent generation through encryption and delivery to victim management and tasking.

Builder allows the operator to generate agent binaries on demand. The interface accepts a build type (Agent (.exe, native)), a build name/tag (метка), the C2 host and port, and target architecture (x64). A debug build toggle labelled DEBUG BUILD (VERBOSE-ЛОГ НА БОТЕ) enables verbose logging on the bot side.

Cryptor provides FUD (Fully Undetectable) crypting as a self-service tool. Architecture and type are detected automatically). The operator can drag-and-drop any executable, DLL, or shellcode, or select an existing build from the panel. This directly matches the forum post where tcherber advertises "C2 / Loader Build + FUD crypt."

Delivery generates ready-made delivery chains in four variants, each with copy-paste commands for the operator:

| Variant | Method | 
|---|---|
| 1. Short commands (v1.0 agents, ≤60 chars) | curl download to %PUBLIC%, scheduled task creation (schtasks /create /f /tn Upd /tr %PUBLIC%\a.exe /sc hourly), task execution | 
| 2. Certutil (for older systems without curl) | certutil -urlcache -split -f download, direct execution | 
| 3. PowerShell XOR chain | Encoded PowerShell with .cer + XOR 0x5A obfuscation, randomized filenames, AV evasion, and cleanup | 
| 4. Panel-native FILE delivery | For v3.0 bots already checked in: FILE:agent.exe via the terminal, dropped to C:\Users\Public | 

The delivery commands reference hxxp://158\[.\]94\[.\]209\[.\]138/agent.exe as the payload URL, confirming the panel is actively serving agents over HTTP. The scheduled task persistence uses the name Upd with hourly execution, a simple but effective persistence mechanism for maintaining access across reboots.

Figure 26: Delivery Panel



Config sets the public C2 host for file distribution (158.94.209.138) and the agent filename (agent.exe). The distribution note confirms both x64 and x86 variants are served at hxxp://158\[.\]94\[.\]209\[.\]138/agent\[.\]exe.

**Victims** list compromised hosts with hostname, IP, agent version, architecture, build tag, status, and last seen timestamp. At the time of capture, the panel showed 178 bots with the most recent check-in seconds prior. **The hostnames indicate a mix of personal and corporate machines across geographically dispersed environments**. All agents report v3.0-id on x64 with the default build tag. **Clicking into a bot opens a terminal with quick-access recon commands, a file browser for directory traversal, and a persistence check shortcut, giving the operator interactive shell access to every compromised host directly from the panel**.

### Operational Assessment

The STANDALONE C2 Panel represents a shift from the bespoke Rust/Go toolchain analyzed in earlier sections to a managed panel-based operation. The panel's built-in builder, cryptor, and delivery chain generator allow the operator to produce, obfuscate, and deploy agents without touching a compiler. The 178-bot count and the September 2026 build timestamps confirm this is not legacy infrastructure; it is actively growing. The offer1\_build3 tag in the builder suggests builds are being prepared for specific transactions, consistent with the percentage-based MaaS model tcherber advertises on the forums.

The panel being accessible without authentication is either an operational security failure or a deliberate choice to allow affiliates or buyers to access the panel without credential management. Either way, it provides defenders with direct visibility into the actor's current infrastructure, victim count, and operational tempo.

## Operator Profile

The evidence converges on a Russian-speaking operator working as both an Initial Access Broker and a Malware-as-a-Service provider, with operations ongoing as of September 2026.

The linguistic indicators are consistent across every surface. The Go orchestrator (csicl.go) contains all-Russian UI strings, progress messages, and debug output. The forum posts on rehubcom\[.\]pro are written in Russian with native fluency. The STANDALONE C2 Panel interface is entirely in Russian, with labels like "ТИП БИЛДА," "ЛОГ СБОРКИ," "ГОТОВЫЕ БИЛДЫ," "ФАЙЛОВАЯ СИСТЕМА БОТА," and "ДЕТАЛИ БОТА" throughout. The explicit CIS exclusion in the forum post is a hallmark of Russian cybercriminal operations, where attacking CIS countries is avoided both culturally and to reduce domestic law enforcement exposure.

The operational model described in the darkweb forum posts matches the toolkit architecture and the panel capabilities. The automated FortiGate checker maps to forti\_vpn.go + csicl.go + reporter.go. The LDAP, SMB, and device enumeration capabilities map to nxc\_ldap.go, smb\_info.go, and nmap.go. The "development to DA (Domain Admin)" offering maps to the HVNC module's credential theft, UAC bypass, and persistence commands. The "C2 / Loader Build + FUD crypt" offering maps directly to the STANDALONE C2 Panel's Builder and Cryptor modules, which provide exactly this service through a web interface. The offer1\_build3 build tag visible in the panel suggests builds are prepared per transaction, consistent with the percentage-based model advertised on the forums. The credential database (processed\_config.txt) with 500+ FortiGate entries across multiple countries is the product inventory of an access broker operating at scale.

VPN connection logs recovered alongside the Go toolkit confirm the tools were actively used against multiple victim organizations, with full root-level network tunnels established and sustained across multi-hour sessions between May and June 2026. The STANDALONE C2 Panel with 178 active bots and September 2026 build timestamps confirms the operator has not slowed down but rather expanded into managed panel-based operations alongside the bespoke Rust and Go toolchain.

## Conclusion

The tcherber investigation demonstrates how a single leaked build path can unravel an entire operational ecosystem. A Rust binary containing /home/tcherber/ in its panic strings expanded into a broader picture of the actor’s infrastructure, tooling, business model, and ongoing operations spanning Rust and Go tooling across multiple C2 platforms.

The campaign's architecture reflects a mature operator who has invested in automation and repeatability. The VPN tools run unattended through an orchestrator. The HVNC implant and Enigma ransomware accept runtime configuration for per-target tuning. The STANDALONE C2 Panel removes the need to compile payloads manually. This is a production pipeline built to service multiple operations and potentially multiple customers simultaneously.

The attribution chain exists because Rust's panic infrastructure embeds full filesystem paths by default. A single build hygiene step, stripping panic paths, would have significantly complicated this investigation.

Additionally, **all recovered Rust payloads (loader, stealer, HVNC, and Enigma) were compiled with the same Rust toolchain version (v1.95.0) under the same /home/tcherber/ build path**, indicating a consistent build environment across the entire arsenal rather than independently developed tools that happen to share a username.

**As of this writing, the actor's infrastructure remains active**. The STANDALONE C2 Panel continues to serve payloads, accept bot check-ins, and generate new builds. Defenders should treat the indicators in this report as current and actionable and prioritize VPN credential audits across FortiGate and SonicWall appliances.

## Indicators of Compromise

### File Hashes

| SHA-256 | Filename | Description | 
|---|---|---|
| 6bddf59e2a5065255cfc90d2e2e66e3bfd4a7 cbf4e0b6341b4da93b574cc4f53 | setup.exe | Stage 1: Fake Windows Update installer | 
| 6aef80514237808dfe25621a8912422d20a841 4bc2054008a119e541166821b5 | setup.ps1 | Stage 1: PowerShell staging script | 
| 7cb59abaa268ac66461447773d46bb0b0e5e 2568e35e1a8f1d07ac2ec57f67a6 | svchost.exe | Stage 2: Rust loader | 
| d0f0734d4e31ec126da43a46896d0cd761 e5532c0c385db6226cc5a6927d7722 | stealer.exe | Stage 3A: Rust stealer | 
| 278762dfc0f743216a475919bdc9ecc59735bc c247bba5b7b468fc475407ec6a | hvnc.exe | Stage 3B: Rust HVNC implant | 
| 859802972787164683cd78d796b9581ffde1 bcee2a708eb20b14f3a8fb276599 | work\_video.exe | STANDALONE C2 Panel v3 agent | 
| abd43578b135df61f49844087af0b372ae10b 2f27721ad6ba09710760ab0b240 | Enigma ransomware binary | Enigma encryptor (ChaCha12 + ECIES) | 
| fc4755e346c9f2fe11f4ba6546f3e8bd3b8711e fbcf2e417307ea9671a93d0f3 | agent.exe | STANDALONE C2 Panel builder output | 
| fad8f76afec90c888b4a739539deae250320fd4 9c34ef8458833b356ea9b7767 | Stealer | Zer0day Stealer variant | 
| f9964a8d9d01052d9bebe057deadd7ce9d794 e8296e2a72229f8ae4aa62ae224 | Dropper | Rust dropper variant | 
| 178f890f62db90738b11300dd27253724 0b1c8a599d2ebeccdea01654811fed0 | HVNC | HVNC PowerShell-related | 

### 

Network Indicators

| Indicator | Description | 
|---|---|
| 93.152.223\[.\]30:5000 | Primary C2 (loader, stealer, HVNC payload delivery) | 
| 93.152.220\[.\]87:5000 | Additional c2 | 
| 93.152.223\[.\]30:5555 | HVNC module hardcoded default C2 port | 
| 158.94.209\[.\]138 | STANDALONE C2 Panel v3 | 
| hxxps://158.94.209\[.\]138\[.\]sslip\[.\]io/ | STANDALONE C2 Panel web interface | 
| hxxp://158.94.209\[.\]138/agent\[.\]exe | Panel payload distribution URL | 

## 

MITRE ATT&CK Mapping

- **T1204 User Execution**
  - T1204.002 Malicious File
- **T1059 Command and Scripting Interpreter**
  - T1059.001 PowerShell
  - T1059.003 Windows Command Shell
- **T1140 Deobfuscate/Decode Files or Information**
- **T1620 Reflective Code Loading**
- **T1562 Impair Defenses**
  - T1562.001 Disable or Modify Tools
  - T1562.002 Disable Windows Event Logging
- **T1497 Virtualization/Sandbox Evasion**
  - T1497.001 System Checks
- **T1547 Boot or Logon Autostart Execution**
  - T1547.001 Registry Run Keys / Startup Folder
- **T1053 Scheduled Task/Job**
  - T1053.005 Scheduled Task
- **T1546 Event Triggered Execution**
  - T1546.003 Windows Management Instrumentation Event Subscription
- **T1548 Abuse Elevation Control Mechanism**
  - T1548.002 Bypass User Account Control
- **T1555 Credentials from Password Stores**
  - T1555.003 Credentials from Web Browsers
- **T1115 Clipboard Data**
- **T1113 Screen Capture**
- **T1057 Process Discovery**
- **T1082 System Information Discovery**
- **T1021 Remote Services**
  - T1021.005 VNC
- **T1133 External Remote Services**
- **T1078 Valid Accounts**
  - T1078.001 Default Accounts
- **T1486 Data Encrypted for Impact**
- **T1490 Inhibit System Recovery**
- **T1489 Service Stop**
- **T1041 Exfiltration Over C2 Channel**
- **T1567 Exfiltration Over Web Service**
  - T1567.004 Exfiltration Over Webhook
