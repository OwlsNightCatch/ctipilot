---
title: TerminalFix and Lorem Ipsum Loader enable covert tunneling
author: About the Author
url: https://www.sophos.com/en-us/blog/terminalfix-and-lorem-ipsum-loader-enable-covert-tunneling
hostname: sophos.com
description: The activity is linked to a broader campaign that previously used a different delivery mechanism
sitename: SOPHOS
date: "2026-09-30"
---
In August 2026, Sophos analysts began investigating a series of Managed Detection and Response (MDR) cases that involved ClickFix-style lures and resulted in the deployment of a Python-based tunneling implant. Instead of a typical ClickFix lure that instructs victims to open the Run dialog box, these lures direct users to open a Windows Terminal window. This ClickFix variation is known as ‘TerminalFix’.

TerminalFix is not linked to a specific threat group or a single campaign. In 2026, Sophos analysts have observed several malicious campaigns that incorporated these lures (see Figure 1) and resulted in multiple infection chains.

*Figure 1: TerminalFix lures*

While investigating this activity, Sophos analysts identified the deployment of Lorem Ipsum Loader, a shellcode-based loader first [observed](https://www.bluevoyant.com/blog/lorem-ipsum-trojanized-microsoft-teams-installers-multi-stage-loader-backdoor) by BlueVoyant in February 2026. The presence of this malware, combined with the command and control (C2) infrastructure, persistence techniques, and DLL sideloading activity, enabled Sophos analysts to link the TerminalFix intrusions to a broader campaign that has been active since at least March. Sophos analysts track this campaign as STAC4924.

## STAC4924 infection chain

By following the instructions in the TerminalFix lure, victims execute a PowerShell command that downloads a ZIP archive containing a legitimate Windows executable, a malicious DLL, and a batch script (see Figure 2).

*Figure 2: Contents of the downloaded ZIP archive*

The command then executes the batch script, which installs several persistence mechanisms and launches the legitimate LockScreenContentServer.exe binary. The executable loads the malicious dui70.dll file via DLL sideloading. This DLL contains and executes Lorem Ipsum Loader. This loader attempts to evade entropy-based detections by storing shellcode bytes as English words rather than raw binary data. A separate lookup table provides a mapping between those words and the hexadecimal byte values they represent.

Once executed, Lorem Ipsum Loader issues an HTTP request to an attacker-controlled profile hosted on the legitimate Letsdiskuss platform. The loader extracts an encoded string embedded within the profile and decodes it to retrieve the current set of C2 servers. The loader then communicates with the C2 servers using HTTP POST requests that appear to contain JPEG image files (see Figure 3). However, the image files contain encoded data that the malware extracts and decodes to facilitate C2 communications.;

*Figure 3: Sample image passed between the malware and C2 server*

The malware then executes a series of PowerShell commands to conduct reconnaissance, gather information, and establish persistence. It deploys a portable Python runtime to the Users\Public\indigo directory by downloading the legitimate Python embedded package from python.org and extracting it alongside malicious files. The runtime is then used to execute client.py, a custom tunneling implant that establishes an encrypted WebSocket connection to attacker-controlled servers and assigns a unique UUID to identify the compromised host. The resulting tunnel enables the threat actors to relay traffic through the compromised host and access network resources while blending in with legitimate web traffic.

### Two phases, two delivery mechanisms

Analysis of the STAC4924 campaign revealed two distinct phases of activity that employ different delivery mechanisms but share many technical characteristics.

The first phase, observed in March and April, relied on SEO-poisoned websites distributing trojanized Microsoft Teams MSI installers. These installers deployed a multi-stage PowerShell loader that communicated with victim-specific C2 infrastructure and leveraged attacker-controlled profiles hosted on letsdiskuss[.]com as dead-drop resolvers. Sophos analysts observed substantial overlap between this activity and the Lorem Ipsum Loader campaign observed by BlueVoyant.

Beginning in late May, the campaign transitioned from signed MSI installers to TerminalFix lures. The timing of this shift coincided with [Microsoft's takedown](https://www.microsoft.com/en-us/security/blog/2026/05/19/exposing-fox-tempest-a-malware-signing-service-operation/) of the malware-signing service that supplied the fraudulently obtained certificates used by the threat actors. The second phase has continued through September and leverages DLL sideloading, image-based steganography, Active Directory reconnaissance, and a Python reverse-tunnel implant. The tooling and tradecraft observed by Sophos analysts closely align with TerminalFix activity [reported](https://www.microsoft.com/en-us/security/blog/2026/08/28/terminalfix-campaign-deploys-reverse-tunnel-through-multistage-intrusion/) by Microsoft in August.

Sophos analysts assess with [moderate confidence](https://www.sophos.com/confidence-assessment) that the two phases are linked to the same threat group or to closely associated threat actors. The per-victim UUID callback structure and use of letsdiskuss[.]com as a dead-drop resolver were observed across both phases. The DLL sideloading tradecraft also suggests a connection, as it was introduced in the first phase and became the execution core of the second phase. Table 1 lists the sideload pairings that Sophos analysts observed between March and September. In addition, both phases establish persistence through auto-run entries masquerading as legitimate Microsoft or software-update components, often reinforced with scheduled tasks. These overlaps suggest an evolution of the campaign’s delivery mechanism rather than a complete redesign of the post-compromise playbook.

| Legitimate application | Malicious DLL | 
| lockscreencontentserver.exe | dui70.dll | 
| changepk.exe | slc.dll | 
| changepk.exe | faultrep.dll | 
| changepk.exe | sppcext.dll | 
| werfaultsecure.exe | faultrep.dll | 
| ResilientStorageCoordinator.exe (originally WerFaultSecure.exe) | faultrep.dll | 
| embeddedapplauncher.exe | sspicli.dll | 
| embeddedapplauncher.exe | secur32.dll | 
| certenrollctrl.exe | certenroll.dll | 
| phoneactivate.exe | dui70.dll | 
| vdsldr.exe | vdsutil.dll | 
| wuauclt.exe | sspicli.dll | 
| bin.exe | cpulib.dll | 
| sessionmsg.exe | dui70.dll | 
| sessionmsg.exe | duser.dll | 
| net runtime optimization service.exe | mscoree.dll | 
| Microsoft Edge Updates Helper.exe | msvcp140.dll | 
| Microsoft Teams Revo Helper. Exe | msvcp140.dll | 
| wlrmdr.exe | dui70.dll | 

*Table 1: Sideload pairings used in STAC4924 campaign*

## Attribution

BlueVoyant subsequently [attributed](https://www.bluevoyant.com/blog/orem-ipsum-clickfix-rapid-brigantine) Lorem Ipsum Loader to the Rapid Brigantine cybercriminal threat group, which Sophos Counter Threat Unit™ (CTU) researchers track as [GOLD VICTOR](https://www.sophos.com/en-us/threat-profiles/gold-victor) (also known as Vanilla Tempest, DEV-0832, VICE SPIDER, and Vice Society). This group has been linked to the Vice Society and Rhysida ransomware families. The tooling, infrastructure, and shift in delivery mechanisms that Sophos analysts observed in STAC4924 support BlueVoyant’s attribution. However, Sophos analysts have not observed encryption in the STAC4924 campaign.

## Recommendations, countermeasures, and indicators

Organizations should monitor their environments for evidence of infection and remediate as appropriate to limit impact. Additionally, it is important to train employees to recognize ClickFix-style lures as these types of attacks continue to increase and evolve.

The following Sophos countermeasures relate to this threat:

- Evade_28d
- C2_38a
- Evade_61b
- Creds_2d
- Troj/Loader-RV
- Troj/Loader-RW
- Troj/Loader-RN
- Troj/Loader-RT
- ATK/PyTune-B

Due to the large number of threat indicators, the full list is available in the SophosLabs [GitHub repository](https://github.com/sophoslabs/IoCs/blob/master/STAC4924_IOCs.csv).
