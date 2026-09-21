# extract: served via trafilatura-direct
---
title: NightEagle APT targets Russian organizations
author: Stanislav Larinsky; Kaspersky Security Services
url: https://securelist.com/tr/nighteagle-apt-ghostcontainer-and-tunneling/121323/
hostname: securelist.com
description: Kaspersky GERT experts have uncovered a new campaign by the NightEagle APT, featuring the GhostContainer backdoor and tools hosted on GitHub. The group is also exploiting vulnerabilities in Active Directory and RDP.
sitename: Securelist
date: "2026-09-16"
---
Over the past year, our Global Emergency Response Team (GERT) has investigated several incidents involving the NightEagle group (also tracked as [APT-Q-95)](https://cybersecuritynews.com/nighteagle-apt-exploiting-0-days/). This group has been active since at least 2023 and originally focused on organizations in Asia. We have now identified attacks by the group targeting businesses in Russia. This post examines both known and new tools NightEagle used in its latest campaign.

## Initial access

In most incidents, the attackers used compromised valid credentials to gain access to corporate VPNs. VPN connections originated from IP addresses in the Russian segment linked to Cloudflare WARP tunnels, as well as from IP addresses associated with European virtual infrastructure providers.

## GhostContainer on Microsoft Exchange

Both during the initial access stage and as the attack progressed, the attackers deployed the [GhostContainer backdoor](https://securelist.com/ghostcontainer/116953/#ghostcontainer-the-backdoor) on Microsoft Exchange servers. It incorporates components from several open-source projects, including the Neo-reGeorg tunnel, an exploit for the CVE-2020-0688 vulnerability, and the `GhostWebShell` class from the ysoserial utility. All of these components are publicly available on GitHub.

We were unable to determine the exact method the attackers used to deliver the backdoor to Microsoft Exchange servers. We believe with a high degree of confidence that they applied a [technique already familiar to us](https://securelist.com/ghostcontainer/116953/#stub-c2-parser-and-dispatcher): extracting the cryptographic keys used by Microsoft Exchange from the ASP.NET configuration, overwriting the `VIEWSTATE` framework parameter, and injecting a payload into it, which then launched the GhostContainer backdoor in memory.

The backdoor is a .NET assembly containing three classes that implement its core functionality:

- `Stub` : processes C2 commands delivered to the infected system through the`x-owa-urlpostdata` headers and evades detection by the Antimalware Scan Interface (AMSI) and Windows Event Log mechanisms by overwriting addresses in`amsi.dll` and`ntdll.dll` .
- `App_Web_843e75cf5b63` : accepts the`fakePath` and`fakePageName` parameters and creates virtual paths that redirect requests to the`App_Web_8c9b251fb5b3` class.
- `App_Web_8c9b251fb5b3` : implements network traffic redirection (proxying) and socket forwarding functionality.

Kaspersky products detect the GhostContainer backdoor as Trojan.MSIL.GhostContainer.gen.

## **Traffic redirection**

Once the attackers gain sufficient privileges during an attack, they leverage RDP to move laterally within the internal network segment. To do this, they download and run tools for tunneling and redirecting network traffic.

The attackers used GitHub repositories to host their archived tools. The names of the repositories and archives were disguised to look legitimate:

- https://github[.]com/mirror-js/mirror-js/refs/heads/main/js/js-webpack.zip
- https://github[.]com/mirror-js/mirror-js/refs/heads/main/js/jsonp-pack.zip
- https://github[.]com/browserthemes/resourcepack/releases/download/main/resource-pack.zip

The files contained within the archives were also given names mimicking known legitimate software, though unrelated to the archive names:

- `adobe_32.exe` ;
- `AdobeSync.exe` ;
- `trueconf.exe` ;
- `1cbroker.exe` ;
- `1c-office-plugin.exe` ;
- `trueconf-broker.exe` .

Across the incidents we investigated, we found two tools that the attackers combined for traffic tunneling.

1. Microsoft dev tunnels
 This is a[legitimate Microsoft mechanism](https://learn.microsoft.com/en-us/azure/developer/dev-tunnels/) that allows local web services to be published for internet access on`*.*.devtunnels.ms` domains. The attackers used this tunneling capability to expose port 3389 (RDP) on the compromised system.
2. rdp2tcp
 This is a[publicly available tool](https://github.com/V-E-O/rdp2tcp) for tunneling TCP traffic over an established RDP connection. It includes a server component that runs on the target system and a client component that runs on the attacker’s side.When virtual channels are opened and closed, corresponding events with IDs 132 (channel opened) and 148 (channel closed) are logged in the *Microsoft-Windows-RemoteDesktopServices-RdpCoreTS/Operational.evtx* Windows log. These events contain the names of the channels (such as XPSRD, cliprdr, Microsoft::Windows::RDS::DisplayControl, and others) used by the RemoteFX module, which extends the capabilities of the RDP protocol.When the rdp2tcp tool is used, events with IDs 132 and 148 will contain the channel name rdp2tcp or other random alphanumeric combinations chosen by the attackers.

The combination of Microsoft dev tunnels and rdp2tcp allows the attackers to maintain network access by using legitimate services without opening additional suspicious ports.

The attackers also used the atexec utility from the Impacket toolkit to create scheduled tasks on target systems. These tasks enabled network port forwarding through standard Windows functionality:

| 1 | netsh interface portproxy add v4tov4 listenport=443 connectaddress=10.0.12.101 connectport=445 | 

## Lateral movement

To obtain elevated privileges and move laterally through the network, NightEagle exploited various vulnerabilities in Active Directory. The attackers used previously established tunnels to connect to internal infrastructure systems.

In one incident, they exploited a well-known RDP implementation vulnerability, CVE-2019-0708 (BlueKeep). They used the vulnerable mechanism to create a local account on the system and add it to the Administrators and Remote Desktop Users groups.

The attackers also requested Kerberos tickets with a non-standard combination of flags (`Forwardable`, `Proxiable`, `Renewable`) and attempted to replicate the `Domain-Password` object from the Active Directory database to impersonate the domain controller (a technique known as DCSync) after obtaining an account with sufficient privileges.

Through these methods, the attackers establish persistence in the infrastructure, obtain password hashes for domain accounts, use long-lived Kerberos tickets to gain legitimate access to target resources, and ultimately compromise domain controllers and the victim’s entire Active Directory infrastructure.

## Takeaways

To expand the geographic scope of its targets, NightEagle is updating its methods and adopting new techniques for persistence and lateral movement. Despite the group’s efforts to stay hidden, timely detection of anomalies combined with a comprehensive approach to infrastructure protection can significantly hinder the attackers from achieving their goals. Since the attackers rely on known legitimate tools and infrastructure vulnerabilities, well-configured monitoring can help detect NightEagle’s presence on the network.

## Detection by Kaspersky solutions

Kaspersky solutions reliably identify the malicious activity described above at various stages of the attack. We showed examples above of how [Kaspersky Threat Analysis](https://www.kaspersky.com/enterprise-security/threat-analysis?icid=gl_sl_threat-analysis-lnk_sm-team_ac4d6b2bf27709dd) detects samples of the GhostContainer backdoor and the tunneling utility. This toolkit also includes the analytical solution [Kaspersky Threat Attribution Engine](https://www.kaspersky.com/enterprise-security/threat-analysis?icid=gl_sl_threat-analysis-lnk_sm-team_ac4d6b2bf27709dd#attribution) (KTAE), which helps SOC analysts and incident responders determine which APT groups malware can be attributed to. The solution uses a proprietary comparison method that measures the similarity between analyzed samples of suspicious files and known malicious samples in Kaspersky’s collection.

The backdoor we discovered showed similarity to previously analyzed GhostContainer samples and a connection to the NightEagle APT group:

However, detection scenarios for this kind of attacks are not limited to file analysis. Deploying a backdoor on a target host produces numerous characteristic artifacts, which allow [Kaspersky Endpoint Detection and Response Expert](https://www.kaspersky.com/enterprise-security/endpoint-detection-response-edr?icid=gl_sl_post-kedr-expert_sm-team_29dc1130f3f612f2) to alert users to anomalies in the infrastructure in a timely manner.

This malicious activity is detected by the following rules, available in the repository:

- Initial detection of the malicious signature occurs through the generic_ransomware_related_detection rule, based on EPP module events
- Detection of a malicious DLL’s .NET assembly being loaded via PowerShell: [suspicious_assembly_loading_into_powershell_via_reflection](https://tip.kaspersky.com/landscape/hunts/edr/0735eff9-e580-3ce4-6208-06ba49538902?icid=gl_sl_tip-rule-lnk_sm-team_8178aa5b470c1704)
- Activity of tunneling and traffic redirection tools: [detection_of_access_to_tunnel_domains_dns](https://tip.kaspersky.com/landscape/hunts/edr/0b4c2f8e-6083-5454-40ca-1345bcc9a4ef?icid=gl_sl_tip-rule-lnk_sm-team_0299b6b77b97c610)
- Use of tools from the Impacket toolkit, such as atexec:
  - [impacket_possible_activity](https://tip.kaspersky.com/landscape/hunts/edr/604cdb41-c877-493a-ac68-4074a2ded058?icid=gl_sl_tip-rule-lnk_sm-team_8fc21aa9614b0533)
  - attempt_to_download_hacktool_or_risktool_by_non_browser
  - [credentials_dumping_tools_file_artifacts_creation](https://tip.kaspersky.com/landscape/hunts/edr/3d6cbeda-f5c5-abaa-666a-2e51f164f8fa?icid=gl_sl_tip-rule-lnk_sm-team_af734cd2abbdb1f0)
- Attempts to replicate an Active Directory database object to impersonate a domain controller: [potential_dcsync_via_startupparameters](https://tip.kaspersky.com/landscape/hunts/edr/e66b0d87-26ca-4a55-9f77-3d775175ff94?icid=gl_sl_tip-rule-lnk_sm-team_7eeccaa71488e6e6)

[Kaspersky Anti Targeted Attack (KATA)](https://www.kaspersky.com/enterprise-security/anti-targeted-attack-platform?icid=gl_sl_post-kata_sm-team_839dfa6f6cbc16e1) detects this malicious activity in network traffic. For example, the [Exploit.CVE-2019-0708.TCP.C&C](https://tip.kaspersky.com/landscape/hunts/ndr/48845929?icid=gl_sl_tip-rule-lnk_sm-team_a704e0413cebc855) signature allows detecting attempts to exploit the CVE-2019-0708 (BlueKeep) vulnerability.

Beyond this activity, KATA also detects other NightEagle actions in network traffic, such as the following:

- Traffic redirection and tunneling variations
- Attacks on Active Directory (DCSync, attempts to compromise AD CS, and others)
- Lateral movement across the network

## Indicators of compromise

| 1dcafb7f8448683281106b06dd22409a | AdobeSync.exe | 
| 1f3034b706c78b35d8e34044e68c693a | adobe_32.exe | 
| [3ecd1cd627d0340c92901a478a7caad8](https://opentip.kaspersky.com/3ecd1cd627d0340c92901a478a7caad8/results?icid=gl_sl_tr-post-opentip_sm-team_7e7c7c9f707d4db3&utm_source=SL&utm_medium=SL&utm_campaign=SL)[631fb131a56caf4ca0f287ed73e876ab](https://opentip.kaspersky.com/631fb131a56caf4ca0f287ed73e876ab/results?icid=gl_sl_tr-post-opentip_sm-team_d0e9df37c5eb6eb6&utm_source=SL&utm_medium=SL&utm_campaign=SL) | App_Web_Container_1.dll | 
| [4aa9fb1bf9223dfcdac920759bc7a3c7](https://opentip.kaspersky.com/4aa9fb1bf9223dfcdac920759bc7a3c7/results?icid=gl_sl_tr-post-opentip_sm-team_71d71f6023ccca64&utm_source=SL&utm_medium=SL&utm_campaign=SL) | 1c-office-plugin.exe, 1cbroker.exe, trueconf.exe | 
| https://github[.]com/mirror-js/mirror-js |  | 
| https://github[.]com/browserthemes/resourcepack |  | 

NightEagle targets Russian companies
