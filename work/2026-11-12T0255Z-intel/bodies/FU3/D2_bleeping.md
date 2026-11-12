---
title: Active ScreenConnect attacks breach MSPs, impact dozens of organizations
author: Lawrence Abrams
url: https://www.bleepingcomputer.com/news/security/active-screenconnect-attacks-breach-msps-impact-dozens-of-organizations/
hostname: bleepingcomputer.com
description: ConnectWise is investigating an active malware campaign targeting managed service providers (MSPs) that uses compromised ScreenConnect environments to deploy rogue remote-access clients to customer devices.
sitename: BleepingComputer
date: "2026-11-11"
tags: ['computers, windows, linux, mac, support, tech support, spyware, malware, virus, security, ConnectWise, Huntress Labs, Managed Service Provider, MSP, ScreenConnect,virus removal, malware removal, computer help, technical support']
fingerprint: "8c9fc813e91f8944"
---
*Update 11/11/26: Added additional information from ConnectWise and Huntress.*

ConnectWise is investigating an active malware campaign targeting managed service providers (MSPs) that uses compromised ScreenConnect environments to deploy rogue remote-access clients to customer devices.

As part of its investigation, ConnectWise has disabled five third-party ScreenConnect extensions across approximately 400 partner environments as a precaution, warning that they may be associated with the attacks.

The campaign was first discovered Wednesday by cybersecurity firm Huntress, which says it has identified six compromised MSPs and 286 affected endpoints across 47 organizations, and that the number of victims continues to rise.

"Our SOC is working an active campaign that started around 17:47 UTC today targeting cloud-hosted ScreenConnect instances," Huntress posted to [Reddit](https://www.reddit.com/r/msp/comments/1xts3f2/active_malware_campaign_abusing_screenconnect/).

"We are currently tracking 6 compromised MSPs and 286+ endpoints, and those numbers are climbing. ConnectWise is engaged and working this with us."

ScreenConnect is a remote access and support platform used by MSPs and IT teams to remotely manage and troubleshoot customer devices.

According to Huntress, attackers are using ScreenConnect's Run Command functionality to deploy rogue ScreenConnect clients on managed endpoints, providing remote access outside of the legitimate MSP's ScreenConnect environment.

The researchers also warned of a potentially more dangerous technique in which attackers can compromise an MSP technician's workstation when they initiate a ScreenConnect session with an infected customer device.

Spike Brandt, Principal Threat Intelligence Incident Commander at Huntress, told BleepingComputer that the activity appears to involve abusing legitimate functionality rather than exploiting a software vulnerability.

"This appears to be abuse of legitimate functionality, aided using custom-built tooling that is, in some cases, compiled on the fly on the victim’s computer," Brandt told BleepingComputer.

"We have no information about how a “patient zero” computer or machine would have initiated this attack."

Huntress said it began receiving alerts when rogue ScreenConnect clients appeared on monitored endpoints and subsequently retrieved attacker scripts that were still accessible to analyze how the attacks worked.

However, the precise mechanism allowing malware to spread from an infected endpoint to a technician's workstation has not been publicly explained.

## ConnectWise disables third-party extensions

In a [security advisory](https://www.connectwise.com/company/trust/advisories) published Wednesday night, ConnectWise confirmed unauthorized access to ScreenConnect partner accounts and the installation of unauthorized remote-access software in customer environments.

As part of its investigation, the company discovered five independent third-party extensions that may be associated with the attacks and disabled them across approximately 400 partner environments as a precaution.

ScreenConnect extensions are installed through its built-in Extensions marketplace via the ScreenConnect administration interface.

The extensions are:

- Labtech Plus
- RMM Plus
- RMM+
- RMM Plus Password Link
- RMM+ Password Link

"Our initial assessment leads us to suspect the threat actor deployed additional remote-access software through independent 3rd party extensions that partners may have added to their environments," ConnectWise said.

The company stressed that having these extensions installed does not necessarily mean that a network was compromised and that the attacks remain under investigation.

"Disabling these 3rd party extensions is a precautionary containment measure. It does not establish that unauthorized software, persistence mechanisms, or access already present on affected devices has been removed," explained ConnectWise

While ConnectWise has disabled the extensions in affected cloud-hosted environments, it warned that on-premises ScreenConnect customers must disable them manually, as the company cannot do so from their end.

Partners were also instructed not to re-enable or reinstall the extensions until further guidance is available.

ConnectWise warned that disabling the extensions does not remove malicious software, persistence mechanisms, or unauthorized access that attackers may have already established on compromised endpoints.

The company advised partners to review authentication logs, extension installation records, administrative activity, Run Command history, and Toolbox records for suspicious activity.

It also urged technicians to avoid initiating interactive ScreenConnect sessions with potentially compromised devices and instead use separate security tools to investigate.

ConnectWise also said it has received reports of technician workstations being compromised during interactive ScreenConnect sessions, but these reports are still being confirmed.

The company added that it has no reason to believe partners that have not deployed the five identified extensions are impacted by this incident, but encouraged all partners to remain on heightened alert.

Huntress has not determined how the attackers are gaining access to affected MSP environments, but says its current telemetry points to compromised credentials or hijacked operator sessions.

Huntress also warned that sequential identifiers used by the attackers suggest additional MSPs may have been previously compromised.

"Sequential attacker-assigned tags suggest other MSPs may have been compromised earlier, so ScreenConnect users should check their Run Command history even if they haven’t received alerts," Huntress told BleepingComputer.

Huntress also shared indicators of compromise (IOCs) to help organizations identify malicious activity, including rogue ScreenConnect client IDs and infrastructure used by the attackers.

The indicators include:

- **Attacker relay:** `185.99.255[.]28` (hostname: screen)
- **C2 domains:** `newnewnew.gotdns[.]org`, `soxnewwork.homedns[.]org`
- **Possible additional C2:** `cdn007-digitaldownloads[.]com`
- **Secondary C2:** `sc.payproofkit[.]com` (`155.94.150[.]39`, hostname: WIN-FB5CKHMU4E1)
- **Stager:** `hxxps://ns.mo7sen[.]dev/EadF.php?p=4`
- **Rogue ScreenConnect client IDs:** `2588ef5c15954b10`, `ed630cc2c873b091`
- **Installer pattern:** `/Bin/ScreenConnect.ClientSetup.msi?...&c=Exploited<N>`
- **Attacker name:** `Addmin`
- **Files:** `Panel-Lateral.ps1`, `runnew.cmd`, `ToolboxRelayUploader.exe`, `Run-Lateral-Full.bat`

The researchers are urging MSPs to review their environments for signs of compromise and avoid initiating interactive ScreenConnect sessions with potentially infected endpoints.

Huntress also told BleepingComputer that its researchers have contacted ConnectWise, the VPS provider hosting the attacker's infrastructure, cloud providers whose dynamic DNS services were used in the attacks, and the broader MSP community.

## Earlier malware activity linked to rogue ScreenConnect identifier

BleepingComputer found an earlier malicious batch script that references one of the rogue ScreenConnect client IDs listed by Huntress, suggesting that the ID was used in malicious activity months before the current attacks were disclosed.

The script, named `SSA-2026-STATEMENT-15518787.bat` ([VirusTotal](https://www.virustotal.com/gui/file/60142ea5daebbf94a2dec4009f673d9822a2fd796ac55478be1edea3136ef4bb/)), appears to impersonate a Social Security Administration statement and was first uploaded to VirusTotal on July 25, 2026.

The batch file attempts to add Microsoft Defender exclusions and creates persistence through the Windows Startup folder and the Run registry key.

It then contacts `amexsafekeyupdate.com` to retrieve installation commands for two separate installers.

VirusTotal sandbox activity associated with the sample includes downloads of ScreenConnect MSI installers from `cdn007-digitaldownloads[.]com` and `cyberrexdesign.screenconnect[.]com`, with `cdn007-digitaldownloads[.]com` also listed by Huntress as a possible C2 domain.

After launching the second installer, the script uses PowerShell to search running processes and Windows services for `ed630cc2c873b091`, one of the rogue ScreenConnect client IDs identified by Huntress.

If the identifier is found, the script considers the installation successful and sends a notification to the attackers through Telegram.

The earlier script also appears designed for a different distribution campaign, with its Social Security-themed filename suggesting it may have been used in phishing attacks.

Asked about the earlier activity, Huntress declined to comment on the specific July incident but said it has observed a significant increase in attacks using legitimate remote monitoring and management (RMM) software as an initial payload in 2026.

The relationship between the July malware activity and the current ScreenConnect attacks remains unclear.

## [Uncover email threats your existing defenses may miss.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

Adaptive Security's AI agents analyze email intent, context, and behavior to uncover phishing, business email compromise, and invoice fraud.

See what's getting through with a 14-day read-only scan of Microsoft 365 or Google Workspace, with no MX changes.

[Start your free email security scan.](https://www.adaptivesecurity.com/lp/nb/email-scan?utm_source=display_network&utm_medium=paid_display&utm_campaign=2026_NA_Q4_Bleepingcomputer_Inadunit_October2026_scan&utm_id=701Rd00000sqmWCIAY)

## Post a Comment Community Rules

## You need to login in order to post a comment

Not a member yet? Register Now
