# extract: served via trafilatura-direct
---
title: ValleyRAT is spreading disguised as adware
author: Pavel Bukhtenko
url: https://securelist.com/valleyrat-backdoor-adware/121175/
hostname: securelist.com
description: Threat actors are distributing the ValleyRAT backdoor disguised as adware. We analyze the infection chain, from the malicious installer to the final payload.
sitename: Securelist
date: "2026-08-31"
tags: ['Adware,Backdoor,Malware,Malware Descriptions,Malware Technologies,Silver Fox,Trojan,ValleyRAT']
---
Attackers typically try to pass off malware as legitimate applications or as potentially unwanted programs that users deliberately search for and download, such as cheats or cracks. They often rely on ad and affiliate networks to deliver their creations to victims’ devices. This post examines a less conventional case: a well-known backdoor distributed under the guise of adware. The attackers may have chosen this distribution method because the adware was signed by the developer. On top of that, users often manually add these apps to exclusions, so their useful features don’t get blocked.

Some time ago, a client asked us to analyze a file with the MD5 hash c24e99f9437feacaa63766a3cde3fe3d and add it to our detection database. We initially classified it as adware, but a cursory analysis turned up suspicious network activity, which prompted us to dig deeper. It turned out the sample did far more than serve ads. In fact, its advertising functionality doesn’t even work; instead, it triggers an infection chain that delivers the ValleyRAT backdoor.

## Malicious installer

The file the client shared with us turned out to be an installer that performed different actions depending on the two-letter suffix used in the file name, positioned just before the numeric string.

| **Installer name** | **What it does** | 
| FS_SETUP_DD_173.exe | Installs DingTalk, a workplace collaboration platform | 
| FS_SETUP_GG_173.exe | Installs Google Chrome | 
| FS_SETUP_HY_173.exe | Opens hxxps://meeting[.]tencent[.]com/download/ | 

These actions are most likely designed to divert the user’s attention away from the sample’s malicious functionality. Regardless of the file name, the installer deploys a modified Chinese desktop wallpaper management tool called QN Wallpaper (hxxps://qnwallpaper[.]keansoft[.]cn/) and adds it to the registry’s autorun entries.

The original version of QN Wallpaper is genuine adware: on installation, it delivers bundled partner apps to the device and then displays ad banners to the user. In this case, however, the attackers use it to carry out [DLL sideloading](https://encyclopedia.kaspersky.com/glossary/dll-sideloading/), a technique that allows malicious code to run under the guise of a signed process by way of a malicious DLL.

The QN Wallpaper modules, along with the malicious components, are unpacked to C:\Program Files\QNWallpaper\5.4.0.1662\<random string of letters and digits>. The following files are saved in that directory:

| **File name** | **MD5** | **Purpose** | 
| 1.zip | 7ad1e3ef4e6d9d636c9e7e967733850e | Archive containing the adware files QnWallpeper.exe and QnwPlayer.exe, along with the modules needed to run them | 
| 7z.dll | 96b4c1d0683dce22bd3223e1e40689c1 | 7z archiver library | 
| 7z.exe | 9b86d3ab6cef15c633933fbbeab39c0a | Archiver | 
| chrome_elf.dll | edfdc30cbd85879776b8f735ea7de1f1 | Library used to launch Electron-based applications | 
| libcef.dll | 07ddbbe2c71c45577a7a4fbcdba0df91 | Malicious library | 
| PeLoader | 48826d5ca845979d2e6ebd66dc1aae90 | File containing the encrypted backdoor | 
| QnWallpaper.exe | 6c158c0f8e029342192d4f0d72e102b7 | Adware module | 
| QnwPlayer.exe | 9a71d6a41cd258b9e89cdc5fc224de73 | Adware module | 
| <random string of letters and digits>Nedca.exe | c24e99f9437feacaa63766a3cde3fe3d | Malicious installer copy | 

After unpacking, the installer uses the DisableAntiSpyware registry key to disable Windows Defender and then launches QnWallpaper.exe.

## DLL Sideloading via libcef.dll

QnWallpaper.exe has dependencies in libcef.dll, so this library gets loaded when the process starts. QnWallpaper.exe also launches QnwPlayer.exe, which likewise calls libcef.dll.

QnWallpaper and QnwPlayer won’t actually function correctly, because the functions exported from libcef.dll are put into an infinite sleep. However, in case that sleep is ever interrupted, the attackers have implemented a function that loads all the necessary functions from the original library into memory, provided it can locate that library on the system.

The malicious functionality in libcef.dll is invoked by a call to DllMain, which runs automatically when the library is loaded. That said, alongside the original exports, the library also contains a function named RunDLL, which likewise initiates execution of the malicious code. QnWallpaper never calls this function. We suspect the attackers intended to invoke it manually via rundll32 or planned to use a separate executable for this purpose, one that wasn’t included in the package downloaded by the sample.

### Running the malicious code

When the library is loaded, code runs that ensures QnWallpaper.exe persists at startup: it adds a file extension association and drops a file with the corresponding extension in C:\Documents and Settings\<username>\Start Menu\Programs\Startup\.

This is followed by a chain of wrapper functions whose main job is to call the next one. Execution eventually reaches the function that contains the actual malicious code. For convenience, we’ll refer to it as mw_entry.

Inside mw_entry, the malware checks two things:

- Whether the current user belongs to the Administrators group
- Which process the DLL is running inside

If the user isn’t a member of the Administrators group, the program attempts to obtain administrator privileges by using the runas utility.

Once it has administrator privileges, the malicious code determines which process the DLL has been loaded into, and selects the payload accordingly:

- If the library is running inside QnWallpaper.exe, the payload is loaded from the PeLoader file.
- If the library is running inside QnwPlayer.exe, the payload is loaded from libcef.dll resources.

Both payloads are AES-encrypted DLLs that contain the ValleyRAT backdoor. The only difference between them is their configuration, specifically, the C2 server addresses. After decryption, libcef.dll checks the magic signatures in the resulting PE file’s headers to confirm the sample is valid. If this check fails, the library releases its resources and takes no further action.

If the headers check out, libcef.dll loads the payload into the process’s memory space and hands control over to the backdoor by calling DllMain.

## ValleyRAT

ValleyRAT begins its operation by parsing its configuration, which consists of key:value pairs concatenated into a single string. To obfuscate this configuration, the attackers wrote the string in reverse.

During parsing, the backdoor restores the correct character order and reads the key values one by one. The set of keys is the same regardless of which process the backdoor is running in.

Some of the configuration fields are listed below:

| **Key** | **Description** | 
| p? | C2 server IP address | 
| o? | C2 server port | 
| t? | Protocol (1: TCP, 0: UDP) | 
| dd | Sleep duration before executing the main code | 
| cl | Sleep duration after receiving the corresponding command from the server | 
| bz | Configuration creation date | 
| bh | Whether to mark the current process as critical (so that terminating it triggers a blue screen of death) Possible values: 1: yes, 0: no | 
| ll | Whether to check for running security/traffic-analysis tools/processes (1: check, 0: do not check) | 
| sh | Whether to inject code into svchost that will restart the malicious process (1: inject, 0: do not inject) | 

The backdoor uses several techniques to protect its process. Some are configuration-dependent, while others are always applied:

- Injecting code into svchost to restart the process: a configurable option. The backdoor allocates memory inside the svchost process, injects code into it, and sets PAGE_NOACCESS permissions on the memory page containing the injected data. It then creates a suspended thread, waits 60 seconds, grants read, write, and execute permissions on the page, and resumes the thread.
The function injected into the process has a single job: restart the backdoor if its execution is interrupted for any reason.
- Marking its own process as critical (so that terminating it triggers a blue screen of death): a configurable option.
- Restarting on an unhandled exception. This protection mechanism is always active, regardless of the backdoor’s configuration.

The backdoor also has spyware functionality. While running, it tracks keystrokes and the currently focused window by using functions from the DirectInput8 library. It also captures clipboard contents. All collected data is saved to a file on disk.

If the ll key in the configuration is set to 1, ValleyRAT periodically checks for active windows belonging to applications that could be used to analyze processes or traffic. Window enumeration is done via the EnumWindows function, using the following callback:

After completing these checks, the backdoor collects system information, including:

- Host name
- Host IP addresses
- User idle time
- Detailed Windows version information (ProductName, EditionId, DisplayVersion)
- Number of CPU cores
- Free disk space
- Graphics adapter
- Currently focused window and its title
- System bitness
- Language settings
- Path to the system directory

On command, the backdoor can perform the actions typical of this malware category:

- Rebooting the computer
- Shutting down the computer
- Taking a screenshot
- Wiping logs
- Updating its C2 addresses
- Downloading additional modules
- Sending keylogger logs along with clipboard contents

Let’s take a closer look at the module-loading functionality. Upon receiving the corresponding command with a link from its operator, the backdoor downloads the file at that link and executes it. The download can come from either the C2 server or a third-party address.

Additional modules can take the form of purpose-built dynamic libraries or shellcode. If the payload is shellcode, the backdoor uses [process hollowing](https://attack.mitre.org/techniques/T1055/012/) with svchost to launch the module.

If the module is a dynamic library, the backdoor loads the PE file into its own process, calls DllMain, and searches for a Main function among the exported functions. Once Main has been called, the library is unloaded from memory.

## Targets and attribution

Over the course of 2026, we detected the ValleyRAT backdoor and its associated malware more than 100,000 times, with more than 1500 unique users affected, primarily in China and India.

This attack geography, combined with the use of the ValleyRAT backdoor, points to [Silver Fox](https://securelist.com/tr/silver-fox-tax-notification-campaign/120038/), a known operator of this malware family, as the likely group behind the campaign.

## Conclusion

This case is a clear example of how adware and affiliate networks can turn out to be far more dangerous than they appear. ValleyRAT is a sophisticated backdoor capable of collecting sensitive data such as keystrokes and clipboard contents, taking screenshots, and delivering additional malicious modules. The attackers exploited a well-known adware application to run the backdoor under the guise of a signed process, which complicates detection.

Motivated by both cyberespionage and financial gain, Silver Fox targets organizations across multiple countries. To stay protected, organizations should keep [employee cybersecurity awareness](https://www.kaspersky.com/enterprise-security/security-awareness?icid=gl_sl_lnk-security-awareness_sm-team_df95e80a3921c34d) up to date and enforce clear policies on the use of third-party software on work devices.

For individual users, we recommend avoiding the installation of software with a questionable reputation, and, even more importantly, never adding such software to your security solutions’ exclusion lists.

## IoC

### MD5

[07ddbbe2c71c45577a7a4fbcdba0df91](https://opentip.kaspersky.com/07ddbbe2c71c45577a7a4fbcdba0df91/?utm_source=sl&utm_medium=sl&utm_campaign=sl&icid=gl_sl_opentip-lnk_sm-team_69ac286c8b13b8c7)

[c24e99f9437feacaa63766a3cde3fe3d](https://opentip.kaspersky.com/c24e99f9437feacaa63766a3cde3fe3d/?utm_source=sl&utm_medium=sl&utm_campaign=sl&icid=gl_sl_opentip-lnk_sm-team_7e0f4f63d22c73d4)

[8a626d844943da3456b044f38deae3a2](https://opentip.kaspersky.com/8a626d844943da3456b044f38deae3a2/?utm_source=sl&utm_medium=sl&utm_campaign=sl&icid=gl_sl_opentip-lnk_sm-team_8d2ab9db1a993061)

ValleyRAT masquerading as adware
