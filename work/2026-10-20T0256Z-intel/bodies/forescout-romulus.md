---
title: "ROMULUS: Analysis of a New Multi-Payload ClickFix Delivery Platform - Forescout"
author: Sai Molige; Forescout Research
url: https://www.forescout.com/blog/romulus-analysis-of-a-new-multi-payload-clickfix-delivery-platform/
hostname: forescout.com
description: Threat hunting researchers at Forescout’s Vedere Labs uncover a new multi-payload ClickFix delivery platform. See how it works and how to detect.
sitename: Forescout Technologies, Inc.
date: "2026-10-15"
categories: ['Research & Cyber Alerts']
fingerprint: dd4f8c83e5820256
---
### Key Findings

- While investigating an incident, we found a server hosting a panel called ROMULUS that turned out to be a new multi-payload ClickFix delivery platform.
- ClickFix has become a popular method for malware deployment over the last year and continues to evolve.
- Here, we detail how ROMULUS served malware recently reported in another campaign and how we found a new delivery route that was used to deploy LegionLoader
- We identify six IP addresses running ROMULUS instances and analyze two malware delivered by the platform to uncover new indicators of compromise.
- The identity of the operator behind the platform and common ownership of the malware families are unknown.
- ROMULUS may be a privately operated panel, a commercial cybercriminal delivery service, an affiliate framework, or software that has been copied between operators.

### Mitigation Recommendations

- Detect and hunt for distinctive anomalies: 
  - Long PowerShell scripts executed from `%TEMP%` or using decimal IP notation
  - Silent MSI installation from `%TEMP%`
  - PowerShell launched with `-NoProfile`, `-ep bypass`, or `-w hidden` and a URL in the command line
  - POST requests with content type form-urlencoded whose body is a single base64 blob
- See the Detection and Indicators section for full details and indicators of compromise

We [recently reported](https://www.forescout.com/blog/from-clickfix-to-c2-comparative-analysis-of-two-malware-loaders/) how cybercriminals use ClickFix to deliver malware loaders that are then leveraged to deploy final payloads such as RATs or ransomware on victim machines.

On September 28, [Huntress](https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat) reported a campaign that adds a new link to that common attack chain: threat actors abused ChatGPT’s Custom GPTs that were programmed to present to victims links to pages serving the ClickFix lures that are then used to deliver loaders.

The server hosting the ClickFix script in that campaign was `96.62.224[.]81` and the trojanized software used to sideload malware included a Canon application (`ISOSimple.msi`) and Stardock DeElevation (`IconEdit2Turb.msi`).

While investigating an independent incident, we noticed the exact same malware being delivered via another server, `86.109.75[.]7`. Beyond that, the new server hosted a panel called ROMULUS. Investigating that panel, we identified a new multi-payload shared ClickFix delivery platform. Here, we detail how ROMULUS was used in two delivery chains:

- The same Stardock DeElevation sideloading package reported by Huntress was observed on another server running ROMULUS.
- A separate chain delivering the LegionLoader malware. This second route served a PowerShell script that reached out to `orbitflownetwork[.]lol` to download a nested encrypted 7z file with an artificially inflated executable. That executable was identified as [LegionLoader](https://malpedia.caad.fkie.fraunhofer.de/details/win.satacom), a malware loader that has been active since 2019 and is also known as CurlyGate, RobotDropper and Satacom.

The identity of the operator behind the platform and common ownership of the final malware families are unknown. ROMULUS may be a privately operated panel, a commercial cybercriminal delivery service, an affiliate framework, or software that has been copied between operators. Notably, we have no evidence that this panel is related to the RomulusLoader reported by [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/ta4922-suspected-chinese-crime-group-going-global) as being used by the Silver Fox threat actor earlier this year.

## ROMULUS Delivery Infrastructure

By pivoting on VirusTotal (`entity:url title:"Romulus" path:"/login"`) and Shodan (`http.title:"Romulus"`), we identified six IP addresses exposing the same dark-themed authentication frontend with the ROMULUS name and shield icon shown below:

- `62.224[.]81` (originally reported by Huntress as part of the Custom GPT campaign)
- `109.75[.]7` (involved in the incident we analyzed independently)
- `240.151[.]223`
- `94.145[.]224`
- `152.224[.]118`
- `27.248[.]127`

All have a login page with a JavaScript that POSTs the supplied username and password to `/api/login`, stores a returned token, and redirects successful logins to `/`.

Additionally, `86.109.75[.]7` exposed a page `/stats.htm` with the same ROMULUS theme. That page showed statistics for “unique installs” and “all runs” including a live counter, a 14-day timeline, a history log, and a country breakdown. Those statistics could allow operators to compare campaign reach and execution over time.

Beyond these pages, ROMULUS exposes two relevant endpoints:

- `/s/<token>` downloads a PowerShell staging script that prepares the victim and decides what to fetch next
- `/app/<same-token>` downloads a trojanized MSI installer carrying a malware loader

The tokens are all 12-character hexadecimal and may be used to represent a victim, campaign, assignment, or delivery job. The table below lists the tokens we observed on `86.109.75[.]7`.

| **Token** | **Observed Routes** | 
|---|---|
| `6c67e0336a7b` | `/s/6c67e0336a7b à PowerShell staging script à orbitflownetwork[.]lol` | 
| `19481b28bd67` | `/s/19481b28bd67 à PowerShell staging script` `/app/19481b28bd67/IconEdit2Turb.msi` | 
| `60f9f0dbd64c` | `/app/60f9f0dbd64c/FreePhotoSlideShowDesktop_signed.msi` | 
| `40152518488f` | `/app/40152518488f/235235.msi` | 
| `2c56afb54013` | `/app/2c56afb54013/overlay.msi` | 

We can group these tokens into three categories:

- `19481b28bd67` serves the Stardock DeElevation delivery chain that we detail below in the ‘Route A’ section. That chain is exactly the same as reported by Huntress on another server `62.224[.]81/s/50d6565cf39e`.
- `6c67e0336a7b` uses the same PowerShell staging mechanism but an entirely different payload route. That script does not request an MSI file from a matching `/app/` Instead, it reaches out to `orbitflownetwork[.]lol` and downloads an encrypted archive chain that we detail below in the ‘Route B’ section.
- The other tokens point to other MSI files which we have not analyzed.

The variety of routes – including or not MSI files – shows that ROMULUS is a reusable delivery backend rather than a single hard-coded malware server. There are many other tokens and MSI files reported on VirusTotal, which reinforce this conclusion and show that ROMULUS is being actively used at scale.

The figure below depicts the different servers and routes we have observed.

## Payload Routing and Malware Delivery

We recovered two PowerShell staging scripts from `86.109.75[.]7/s/6c67e0336a7b` and `86.109.75[.]7/s/19481b28bd67`. They are both heavily obfuscated and generated from the same template, which is evidenced by common scaffolding.

Each script saves its own path to `$env:__ST` using `$MyInvocation.MyCommand.Path`, reconstructs code from a large array of integers using a sample-specific key, and executes the reconstructed text with `[scriptblock]::Create`. The reconstructed text is an inner layer that uses the same obfuscation technique for selected strings. The numerical keys, variable names, and payload-specific code change per script, while the overall control flow is similar. Both scripts also delete themselves before exiting.

Here, we explore the two routes observed, including the differences in the staging scripts and remainder of the chain in each case.

### Route A: Stardock DeElevation

The `19481b28bd67` staging script creates a `.NET WebClient` with a `Chrome/131` user-agent and a TLSv1.2 connection to download the trojanized `hxxp://1450003207/app/19481b28bd67/IconEdit2Turb.msi`. In that URL, `1450003207` is decimal IPv4 notation for `86.109.75[.]7`.

The script retries the download up to three times with short randomized delays, writes the downloaded installer to `%TEMP%` with a GUID-prefixed filename, runs `Unblock-File`, then starts `msiexec.exe` with `/i`, `/qn`, and `/norestart` before deleting itself.

The downloaded MSI has a creation timestamp of 25 September 2026, identifies itself as “`Stardock Smart DeElevation Tool`“, targets x64 systems and installs on `%LOCALAPPDATA%\Programs\Stardock Smart DeElevation Tool\`. The installer contains a `WixShellExec` custom action that launches `DeElevate64.exe` after installation.

`DeElevate64.exe` is the legitimate host file used to load further malware and is one of the seven components present in the MSI file, described in the table below.

| **Component** | **Role** | **SHA256** | 
|---|---|---|
| `DeElevate64.exe` | Legitimate Stardock host | `22869e3326fe1de011cd500e666769027126c5c440b76837baf55139f30094e4` | 
| `DeElevator64.dll` | Patched sideloaded DLL | `0457414c4504b70115798eee9c8384a8bf9e793461ffb2e0661a6dcc6ed4809f` | 
| `I++u.dll` | Malicious loader | `3cd1484cc5bf10e22d79784beba58a75d7b126c46efb5e1a85d6aab884447621` | 
| `senddmp.resources.dll` | Helper module | `b59a21a8d4c0c11a9ecbbdbe2a2938499c99c5ebb210c9c6db9683c7ad19f4c4` | 
| `res.dll` | Helper module | `a27cafb84876a3374ef4aba1062345def6cd0b029eaf8e0dc44fa24fc943f3c6` | 
| `Build.dat` | ZIP-style loader container | `d3fda1e6cf886fd530bf62e2d16c39ad23ed12a2c933fc211f1f4876ceaa033e` | 
| `execute_engine_disconnect.raw` | Encrypted payload storage | `d5acf44658f0dce90bd160f15d8e07a96938c81661d87dc7e9cb0107863bfb90` | 

Upon execution, `DeElevate64.exe` imports `DeElevator64.dll` from its application directory. The packaged `DeElevator64.dll` is patched to introduce a dependency on `I++u.dll`, which moves execution to the malicious loader that uses the remaining files in the MSI package. The remaining loader stages are exactly the same as [described by Huntress](https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat).

### Route B: LegionLoader

The `6c67e0336a7b` staging script uses a different delivery mechanism, depicted in the image below.

The staging script hides the PowerShell console through dynamically defined `GetConsoleWindow`, `ShowWindow`, and `MoveWindow` calls, then downloads `orbitflownetwork[.]lol/dl/J8QkZUVJgV.7z` and the legitimate `7zr.exe` utility from GitHub.

The script verifies the 7z signature on the downloaded archive, checks that the downloaded `7zr.exe` begins with an MZ header and exceeds a minimum size, then uses `7zr.exe` to extract the password-protected `J8QkZUVJgV.7z` file using password `iQQaQ7Yo41rbZ` – hardcoded in the script – without displaying a console window.

The use of the legitimate 7-Zip binary avoids embedding an archive library in the loader and makes the extraction step look like an administrative task unless the full process lineage is considered. Encrypting the 7z header hides the file names and contents from file scanners.

Once extracted, `J8QkZUVJgV.7z` reveals another encrypted 7z file (`CarJqRHyOtBu3mI.7z`) and a 20-byte text file containing a password for its extraction (`RkfZvXZt6XtfuoZsHfSr`). After extraction, `CarJqRHyOtBu3mI.7z` reveals five high-entropy .bin files and a random-name executable with 882,716,672 bytes, as summarized in the table below.

| **Layer** | **How Access Is Obtained** | **Result** | 
|---|---|---|
| J8QkZUVJgV.7z | Password iQQaQ7Yo41rbZ is hardcoded in the PowerShell | 20-byte password file + CarJqRHyOtBu3mI.7z | 
| CarJqRHyOtBu3mI.7z | Password RkfZvXZt6XtfuoZsHfSr is read from the extracted text file | Five .bin files + 882,716,672-byte EXE | 
| Executable carrier | No archive password; unpacking occurs inside the PE | AES-encrypted shellcode, then the final LegionLoader PE | 

The five `.bin` files have a fixed-size high-entropy layout that suggests encrypted or chunked content. However, no known container structure emerged from RC4, AES, XOR, or BabaDeda-style storage tests, and the files were never referenced in the final PE. They may be decoys, padding, or ancillary resources used by a code path we did not trace, but that does not affect the full communication between LegionLoader and C2.

The large size of the single EXE file is artificial. That executable is a valid x64 PE, but approximately 881.7 MB belongs to the raw .reloc section. The PE relocation directory describes only 108 bytes of actual relocation data, while most of the oversized section is a repeating 16-byte value. This repetitive padding compresses extremely well, so the attacker can distribute an archive under 1 MB that expands to a file large enough to exceed upload limits, sandbox budgets, or static-analysis thresholds.

The meaningful code and encrypted payload data are near the beginning of the file. This 2 MB prefix retained the PE headers, code, configuration, cryptographic material, and two packed stages:

- Stage 1 uses the Windows CryptoAPI with a `PROV_RSA_AES` provider and a plaintext key blob for `CALG_AES_256` to decrypt an embedded buffer, remove `PKCS#7` padding, and reverse the entire plaintext buffer, which contains stage 2.
- Stage 2 is position-independent shellcode that contains a second decryptor and custom image loader. The shellcode repeats the AES-256-CBC and byte-reversal sequence, then manually maps the resulting 475,648-byte PE (which we call stage 3) by allocating memory, resolving imports, applying relocations, and invoking its entry point.

| **Stage** | **Size** | **SHA256** | **Purpose** | 
|---|---|---|---|
| Stage 1 outer carrier | 882,716,672 B | `1f403ac059f172e99968ce96bd0ef1bd1981070b454e3e5d75a71368c3c8762a` | Inflated PE; decrypts Stage 2 | 
| Stage 2 shellcode | 542,356 B | `4e0941d243c0b16e9019e4f9c5eb0f6e6630af4d44d9677611917450bb2e696e` | Second decryptor and manual PE loader | 
| Stage 3 PE | 475,648 B | `2e3d378d6a842af2404dfcd1dcbfc0df84b01b799b2c8270ddbfe5eb18837762` | LegionLoader | 

## LegionLoader Analysis

The final PE (stage 3) exposes a LegionLoader configuration that is similar to what was  [reported by other researchers](https://asec.ahnlab.com/en/95374/):

- `smashshape[.]com` is the C2 server, with endpoints `/nfront.php` and `/nback.php`. The former is used for registration and command retrieval, while the latter is used to report results.
- Chrome Local State key handling is used to retrieve keys and collect sensitive information stored on the Chrome browser of victims.
- A distinctive RC4/Base64 message framing that we discuss below.

Messages are sent via WinHTTP with declared `Content-Type: application/x-www-form-urlencoded`. However, instead of `key=value` form fields, the request body contains one string generated as follows. The client serializes a compact binary object, encrypts it with a 31-byte RC4 key recovered from the stage 3 PE, and base64-encodes the result. Responses are decoded in the opposite direction. The same framing is used for registration, commands, and result traffic.

Each decoded message starts with a 32-bit little-endian field count. Every field then contains an identifier, a type, a length, and a raw value. All observed fields used type ‘4’ regardless of the type of underlying value (string, raw bytes, integers, Booleans).

The stage 3 PE contains a field identification table with 98 entries. We could assign specific roles to the nine entries shown in the table below.

| **Field ID** | **Observed role** | **Direction** | 
|---|---|---|
| `0x44EFF14D` | Windows version string | Client → server | 
| `0x23811AAC` | 8-character machine ID | Client → server | 
| `0x34585126` | 4-byte build/campaign value; semantics unresolved | Client → server | 
| `0x998012F2` | String registration flag | Client → server | 
| `0xA17BA684` | Boolean registration flag | Client → server | 
| `0x6976C50E` | Primary command/value/result field | Both | 
| `0x19BD28E4` | Raw 16-byte key accompanying a download | Server → client | 
| `0xB7117366` | PowerShell command string | Server → client | 
| `0xFB5E2CDB` | Secondary parameter; tentative | Server → client | 

We divided these messages into the following phases:

- **Registration and host identity.** Upon registration, the client reports to the server the first five values shown in the field ID table above. Most are self-explanatory, but the machine ID is relevant. That ID is derived from the system volume serial by applying CRC32 five times in succession and formatting the final value as uppercase hexadecimal. This identifier is stable across repeat executions on the same installation and gives the C2 backend a compact way to identify returning systems.
- **Tasking and payload handling.** Tasking is field-driven rather than a fixed command packet. The overloaded `0x6976C50E` field can carry control text, such as sleep, a download directive, a URL, or result text, depending on context. A separate field (`0xB7117366`) carries PowerShell code to be executed. When the server instructs the client to retrieve an encrypted payload, field `0x19BD28E4` supplies a raw 16-byte runtime key. The downloaded data is then processed through a separate two-layer RC4 path, first with the runtime key and then with a fixed 16-byte key embedded in the client. This downstream decryption path is distinct from the 31-byte key used to protect the C2 messages themselves.

Results are reported to `/nback.php` using the same serializer and RC4/Base64 framing.

## Detection and Indicators

The table below lists threat detection opportunities ordered from infrastructure to execution and C2. Web fingerprinting and token hunting are useful before a host is compromised. Script and process telemetry cover the ClickFix and staging phases. File and image-load telemetry catch the two payload routes after a download. Network detections for LegionLoader require HTTP visibility or TLS interception while the field IDs and RC4 framing are most useful during packet or sandbox analysis.

| **Technique / Stage** | **Artifact** | **Detection Opportunity** | 
|---|---|---|
| ClickFix / PowerShell | Hidden or bypassed PowerShell with URL | Monitor PowerShell launched with `-NoProfile`, `-ep bypass`, or `-w hidden` and a URL in the command line. Where available, review RunMRU and browser-to-PowerShell process ancestry. | 
| PowerShell obfuscation | `$env:__ST, [scriptblock]::Create`, large negative-integer arrays | Use event 4104 to match the structure rather than sample-specific variable names or keys. Long scripts executed from `%TEMP%` are more suspicious. | 
| Decimal IP notation | `1450003207` `1614733393` | Search command lines and script logs for  `http(s)://` followed by 8-10 decimal digits. Network telemetry will show the equivalent dotted IP, allowing correlation. | 
| Archive route | PowerShell downloads `7zr.exe` and performs two passworded extractions | Correlate PowerShell → `7zr.exe` with -p and -y, followed by launching a new random-name executable from the extraction directory. | 
| PE inflation | \~842 MB PE, \~881.7 MB .reloc, tiny relocation directory | Flag very large executables written to user-writable paths and inspect files skipped by sandbox or scanner size limits. A very large `.reloc` with little actual relocation data is a strong anomaly. | 
| MSI route | PowerShell → `msiexec /i ... /qn /norestart` | Correlate silent MSI installation from %TEMP% with Unblock-File and subsequent EXE execution. | 
| DLL sideload | `DeElevate64.exe` `DeElevator64.dll` `I++u.dll` | Track module loads from `%LOCALAPPDATA%\Programs\Stardock Smart DeElevation Tool\` and compare DLL hashes against legitimate Stardock inventory. | 
| LegionLoader C2 | POST `/nfront.php` or `/nback.php` with base64 body | With HTTP or TLS-inspection visibility, alert on the path and a form-urlencoded POST whose body is a single base64 blob. With decrypted bodies, confirm known field IDs after RC4/Base64 decoding. | 
| Browser access | Non-browser reads Chrome Local State | Use EDR file-read telemetry or a targeted SACL to identify non-browser access to Chrome Local State shortly after a ClickFix chain. | 

### MITRE ATT&CK Summary

| **Technique** | **Observed Behavior** | 
|---|---|
| T1204.004 Malicious Copy and Paste | ClickFix PowerShell execution | 
| T1059.001 PowerShell | Stagers and C2-issued commands | 
| T1105 Ingress Tool Transfer | MSI, 7z, 7zr.exe, and payload downloads | 
| T1027.010 Command Obfuscation | Integer-array and split-string obfuscation | 
| T1027.001 Binary Padding | 842 MB PE via oversized .reloc | 
| T1027.013 Encrypted/Encoded File | Passworded archives, AES stages, RC4/Base64 C2 | 
| T1140 Deobfuscate/Decode Files or Information | AES-CBC with byte reversal; RC4 | 
| T1218.007 Msiexec | Silent MSI install on ROMULUS Stardock route | 
| T1574.002 DLL Side-Loading | DeElevate64.exe loads patched DeElevator64.dll | 
| T1518.001 Security Software Discovery | Security Center product queries | 
| T1555.003 Credentials from Web Browsers | Chrome os\_crypt / encrypted\_key handling | 

### Indicators of Compromise

| **Indicator** | **Context** | 
|---|---|
| `96.62.224[.]81 / 1614733393` | Huntress-documented ClickFix delivery node. ROMULUS frontend observed | 
| `86.109.75[.]7 / 1450003207` | ROMULUS node serving the Stardock-based package and LegionLoader | 
| `hxxp://86.109.75[.]7/s/19481b28bd67` | Stage route paired with the Stardock-based IconEdit2Turb.msi | 
| `hxxp://86.109.75[.]7/app/19481b28bd67/IconEdit2Turb.msi` | `IconEdit2Turb.msi` | 
| `hxxp://86.109.75[.]7/s/6c67e0336a7b` | Stage route leading to `LegionLoader` | 
| `orbitflownetwork[.]lol` | Archive delivery for `/dl/J8QkZUVJgV.7z` | 
| `smashshape[.]com` | `LegionLoader C2`; `/nfront.php` and `/nback.php` | 
| `novatrafficcore[.]lol/AsFJfTQYDTkpOg6K` | Earlier observed stager URL. Direct ROMULUS link unconfirmed | 
| `151.240.151[.]223` | ROMULUS host not individually analyzed | 
| `23.94.145[.]224` | ROMULUS host not individually analyzed | 
| `93.152.224[.]118` | ROMULUS host not individually analyzed | 
| `2.27.248[.]127` | ROMULUS host not individually analyzed | 
| `91a22cf3154944897cbcaffc7d20d4596e972d280ee134197d41d8d8eefb0fe2` | ROMULUS Route A Stardock MSI: `IconEdit2Turb.msi` | 
| `22869e3326fe1de011cd500e666769027126c5c440b76837baf55139f30094e4` | `DeElevate64.exe` | 
| `0457414c4504b70115798eee9c8384a8bf9e793461ffb2e0661a6dcc6ed4809f` | `DeElevator64.dll` | 
| `3cd1484cc5bf10e22d79784beba58a75d7b126c46efb5e1a85d6aab884447621` | `I++u.dll` | 
| `d3fda1e6cf886fd530bf62e2d16c39ad23ed12a2c933fc211f1f4876ceaa033e` | `Build.dat` | 
| `d5acf44658f0dce90bd160f15d8e07a96938c81661d87dc7e9cb0107863bfb90` | `execute_engine_disconnect.raw` | 
| `62ca523863337ac5d6b1c4d9ae262d1b2eb7dd9ca764b702ef719c84b2437a39` | Route B staging script | 
| `6147d56b5e35d6435d83adb49908c40a97520a0c3379121104816e37cbd1df28` | Route A staging script | 
| `3b074d6f9bc399fbb1362aeb6ffe1e02013f10e8fa095fc2b3381d8cec270435` | `J8QkZUVJgV.7z` | 
| `4e2955f5f5861a51c07fe386d782a3872cfe1c9e750295daa94626f2bd97d84a` | `CarJqRHyOtBu3mI.7z` | 
| `1f403ac059f172e99968ce96bd0ef1bd1981070b454e3e5d75a71368c3c8762a` | Inflated 842 MiB carrier | 
| `4e0941d243c0b16e9019e4f9c5eb0f6e6630af4d44d9677611917450bb2e696e` | Stage 2 shellcode | 
| `2e3d378d6a842af2404dfcd1dcbfc0df84b01b799b2c8270ddbfe5eb18837762` | Stage 3 LegionLoader PE |
