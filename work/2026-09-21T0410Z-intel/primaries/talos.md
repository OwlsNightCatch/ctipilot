# extract: served via trafilatura-direct
---
title: "Ransomware incidents in Japan in the first half of 2026: Investigation of The Gentlemen’s infrastructure and evidence of Qilin's AI use"
author: Takahiro Takeda
url: https://blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/
hostname: talosintelligence.com
description: Ransomware incidents in Japan rose 4.7% year over year. The Gentlemen was the most active group, with leak-site listings more than doubling from January to July. Qilin ranked second and appeared to use AI, while SMEs with capital under JPY 1 billion represented 80% of victims.
sitename: Cisco Talos Blog
date: "2026-09-17"
tags: ['ransomware', 'Threat Spotlight', 'Cisco Talos Malware Protection', 'Cisco Talos Network Intrusion Prevention']
---
- Compared with the same period last year, ransomware incidents in Japan increased slightly by approximately 4.7%, indicating that ransomware continues to pose a significant threat.
- In Japan, The Gentlemen was the most active ransomware group in the first half of 2026.
- Attackers continue to primarily target small- and medium-sized enterprises, with organizations capitalized at less than JPY 1 billion accounting for approximately 80% of the total — an increase of around 13% from the previous year.
- The total number of listings on The Gentlemen’s leak site increased from 48 in January to 105 in July, representing approximately a 2.2-fold increase in activity. Additionally, there is a possibility that Russian-speaking individuals are involved in The Gentlemen’s attacks.
- Qilin, which recorded the second-highest number of observed incidents in 2026 after The Gentlemen, is leveraging AI to improve the efficiency of its operations.

## Victimized companies

Figure 1 summarizes ransomware incidents affecting Japanese companies from January to July 2026. According to Cisco Talos research, 90 organizations in Japan were affected by ransomware during this period. Compared with 86 incidents during the same period from January to July last year, this represents a slight increase of approximately 4.7%, indicating that ransomware incidents continue to remain at a high level.

On a monthly basis, there were approximately 13 incidents per month on average. The number of incidents increased in March and April, with April recording the highest number during the period at 19 incidents.

Cases involving overseas offices and subsidiaries accounted for 13.3% of the total. Among these, Taiwan recorded the highest number of incidents, followed by the United States and the Philippines, which recorded the same number of incidents, with multiple cases identified in each country.

The manufacturing sector continued to be the most affected industry, accounting for 34% of incidents, followed by the information and communications sector at 11% and the services sector at 9% (see Figure 2).

In terms of the size of the affected organizations, those with capital of less than JPY 100 million accounted for the largest share at 48%, followed by organizations with capital of JPY 100 million to less than JPY 1 billion at 30%. Combined, organizations with capital of less than JPY 1 billion accounted for 78% of the total, representing an increase of around 13% from 69% in 2025. This suggests that attackers are increasingly focusing their efforts on small- and medium-sized enterprises (see Figure 3).

## Most frequently observed ransomware types in Japan

In Japan, the most frequently observed ransomware group in the first half of 2026 was The Gentlemen, with 14 incidents. This was followed by Qilin, which caused the highest number of incidents last year, and SafePay, which had relatively few confirmed incidents during the same period last year, with seven incidents each.

The Gentlemen and SafePay have increased their activity this year and can be considered emerging ransomware groups that require increased vigilance. Other ransomware groups observed include NightSpire, NetRunner, LockBit 5.0, RansomEXX, Stormous, and AiLock.

Looking at the ransomware groups observed this year, very few of the groups that were active during the same period last year have been observed, highlighting the rapid changes in the ransomware threat landscape.

In the following sections, we examine the most prominent groups during the period, The Gentlemen and Qilin, and provide an overview of The Gentlemen, the tools it uses, attack flow and findings related to its attribution, as well as examining Qilin’s use of AI.

## Overview of The Gentlemen ransomware

The Gentlemen ransomware group has been active since around July 2025. Although it is a relatively new group, it has been expanding its operations through a Ransomware-as-a-Service (RaaS) model and has already caused significant damage to organizations worldwide. The group uses a double-extortion strategy, encrypting victims’ data while also threatening to publish stolen information unless a ransom is paid.

Figure 6 shows the monthly number of listings on The Gentlemen data leak site worldwide. From January to July 2026, the number of listings shows an overall upward trend despite some month-to-month fluctuations. The number increased sharply from 48 in January to 87 in February. From March through May, it remained relatively stable at around 70 – 74 listings per month.

In June, however, the number exceeded 100 for the first time, reaching 108, and remained high at 105 in July. In particular, the figures for June and July were notably higher than those in the preceding months, indicating that listing activity has intensified compared with the beginning of the year. Compared with 48 listings in January, the 105 listings recorded in July represent an increase to approximately 2.2 times the January level.

By industry, manufacturing accounted for the largest share at 21%, followed by professional, scientific, and technical services at 16%, and wholesale trade at 13%. These three industries clearly stood out in terms of the number of incidents.

Among the remaining industries, retail trade accounted for 6%, while construction and health care/social assistance each accounted for 5%, showing a substantial gap from the top three. Incidents were also observed across a wide range of other industries, including information, finance and insurance, transportation and warehousing, and educational services.

Overall, while the activity is not concentrated exclusively in any single industry, manufacturing; professional, scientific, and technical services; and wholesale trade are particularly prominent in terms of the number of observed cases.

## Investigation of The Gentlemen’s open directory infrastructure

Talos identified open directory infrastructure believed to have been used by a threat actor associated with The Gentlemen. During our investigation, we observed numerous tools used to support ransomware operations. Our investigation found ransomware targeting ESXi and Windows environments linked to The Gentlemen. We also identified [RustHound](https://github.com/g0h4n/RustHound-CE), a cross-platform Rust-based tool used to collect Active Directory (AD) information required for attack path analysis with BloodHound; exploit code targeting CVE-2025-2479, a SQL injection vulnerability that can allow unauthorized manipulation of databases; the adversary-in-the-middle (AitM) tool [Responder](https://github.com/lgandx/Responder); [impacket-partial-mic](https://github.com/decoder-it/impacket-partial-mic), which can be used for NTLM authentication relay attacks; [Ligolo-ng](https://github.com/Nicocha30/ligolo-ng), which establishes tunnels into compromised networks and enables access to internal networks from external systems; the tunneling tool [chisel](https://github.com/jpillora/chisel); the remote desktop tool AnyDesk; and the file transfer tool Rclone.

Figure 8 illustrates the attack flow inferred from the commands recorded in .bash_history.

In Phase 1, the actor uses VPN software and tools such as Chisel and Ligolo to establish network routes and turn its server into an attack platform. The actor then repeatedly installs and configures reconnaissance tools such as nmap and masscan, along with BloodHound, NetExec, Responder, and Impacket for targeting AD environments, all within the same command history.

Once the attack platform had been established, the threat actor proceeded to Phase 2: target reconnaissance. They appear to have used Masscan and Nmap to assess publicly exposed hosts, VPN-related ports, web services, SMB, and other active services in order to understand the external and internal network structure. Upon gaining access to the internal network, they used NetExec to enumerate SMB shares, host information, LDAP, and computer information in Active Directory. They may also have used RustHound/BloodHound-related tools to collect domain users, groups, computers, administrative privileges, and trust relationships, with the aim of identifying paths that could be used for lateral movement and privilege escalation.

Following target selection, during Phase 3, we observed the actor downloading and executing Proofs of concept, reconnaissance scripts, and attack tools associated with known vulnerabilities against publicly exposed web services and administrative interfaces. Specifically, the actor attempted to exploit CVE-2025-24799, an unauthenticated SQL injection vulnerability in GLPI, using both a PoC and sqlmap to retrieve user information from the database. The actor also used a scanner targeting cPanel/WHM and downloaded and executed a PoC to test for authentication bypass vulnerabilities.

In Phase 4, the threat actor leveraged the information obtained in Phase 3 to expand the operation into the internal network and Active Directory environment. The actor appears to have collected and validated credentials used within the target environment in an attempt to gain access to multiple hosts and services.

The command history shows the installation and execution of tools targeting Windows authentication and Active Directory, including Responder, NTLM relay-related tools, Impacket, and NetExec. We also observed traces suggesting the exploitation of CVE-2020-1472 (Zerologon) and the vulnerabilities associated with MS17-010.

In Phase 5, the threat actor not only investigated the internal network but also used compromised access paths and credentials to move incrementally toward more critical hosts. The actor used VPN, Chisel, Ligolo-ng, SSH, and Proxychains to establish communication paths from the attacker-controlled server into the target organization’s internal network. They then used NetExec and Impacket to attempt authentication to services such as SMB, LDAP, RDP, and WinRM, seeking access to multiple hosts and attempting lateral movement. This activity indicates an effort to reach critical servers and Active Directory management infrastructure within the internal network.

In Phase 6, involving information collection and exfiltration, the threat actor mounted a backup share via CIFS at /mnt/Backup and inspected the Windows file system within VHDX backups. The command history records the installation of libguestfs-tools, qemu-utils, and nbd-client, the creation of directories such as /mnt/vhdx, and the copying of ntds.dit, SAM, and SYSTEM. The actor then used Impacket’s secretsdump.py to extract credentials and password hashes from the collected ntds.dit and SAM files, saving the results as “ntds.txt” and “SAM.txt”. We also identified traces indicating that the VHDX files were compressed with zstd and transferred to cloud storage services such as Wasabi using rclone. The attackers initially attempted the transfer using the default settings and subsequently reconfigured and reran the process to improve transfer speed and communication stability. The VHDX file was split into 256MiB chunks, with up to 16 files uploaded concurrently to reduce the overall upload time. Detailed progress reporting, connection timeouts, retries following transfer failures, and logging to a file were also specified. This suggests that the attackers were deliberately focused on exfiltrating large volumes of data and intended to maintain and monitor the transfer process.

Following the completion of an operation or at the end of each work phase, the threat actor deleted credential dumps, scan results, Responder-related files, pivoting tools, and temporary files stored on the attacker-controlled server. As shown in Figure 11, the command history contains evidence of deletion activities such as the following:

In addition, as shown in Figure 12, we found that The Gentlemen uses the open-source AdaptixC2 framework for command-and-control (C2) operations.

AdaptixC2 is a C2 post-exploitation framework designed for penetration testing and red team operations. However, The Gentlemen may be using it in real-world attacks.

The tool can also be extended through agents, listeners, and scripts. In addition, it supports multiple communication protocols, including HTTP/S, DNS/DoH, and SMB, making it adaptable to various network environments. Due to this flexibility, AdaptixC2 can be useful not only for legitimate red team operations but also for malicious actors.

## Attribution

Among these traces, we discovered a Bash script. The tool itself is relatively simple, periodically sending ping requests to a specified IP address and logging whether the host is reachable. However, we identified Russian-language comments within the script.

Additionally, the contents of the .bash_history file left in the attacker’s environment contained “црщфьш” (whoami), “ды” (ls), “шз ф” (ip a), “сдуфк” (clear), and “уше” (exit). This suggests that the attacker may have been using a Russian keyboard layout, indicating the possibility that a Russian-speaking individual was involved in the attack. As The Gentlemen is suspected to be led by individuals based in Russia, this further supports the connection to the group.

## Indications of generative AI use found in Qilin’s open directory

When we investigated the environment affected by the Qilin attack, Talos identified several characteristics in Python scripts found in an open directory used by Qilin that suggest, with medium-to-high confidence, that scripts may have been generated using AI.

Figure 16 shows part of a Python script named “deadman.py”. This tool deploys destructive actions to multiple machines in a Windows/Active Directory environment at a specified time and centrally manages their status.

The do_gpo function shown in Figure 16 uses an AD Group Policy Object (GPO) to deploy the wiper broadly across Windows machines within the domain. This function uses Active Directory Group Policy Objects (GPOs) to deploy a wiper across Windows endpoints within the domain. The code also contains comments such as # Stage wipe payload to SYSVOL, # Stage startup script, and # Create GPO via PowerShell on DC, suggesting that an LLM may have structured the overall process as a workflow: (1) Stage the payload → (2) Stage the startup script → (3) Create the GPO.

Figure 17 shows an excerpt from “veeam_kill.py”, a Python script designed to stop, disable, and destroy Veeam backups. As shown in Figures 17 and 18, the main() function clearly divides the overall process into four stages, labeled “Step 1” through “Step 4,” with comments and progress logs provided at a consistent level of detail for each step.

We also identified traces of code that appears to have been generated by an LLM in “deploy_locker.py”, a script used to distribute and execute ransomware across multiple endpoints. As shown in Figure 19, the script begins with documentation-style text describing the tool’s purpose, prerequisites, and usage examples, a format commonly seen when an LLM generates code from a given specification. In addition, as observed in the code discussed above, the script also contains comments that explain the processing flow step by step.

As shown in Figure 20, a portion of the “.bash_history” file also contains a history of commands used to inspect the contents of a directory associated with a tool named llm_chatbot, which appears to be related to LLM-based generation.

## Measures to prevent intrusions

Our investigation found that vulnerabilities and misconfigurations in VPNs, remote access environments, and network devices were prominent initial access vectors. Talos also identified multiple cases in which threat actors gained access to internal networks by abusing stolen credentials or legitimate accounts. Therefore, managing internet-accessible devices and services and protecting credentials remain top priorities.

First, organizations should regularly inventory internet-accessible devices and services, including VPNs and remote desktop services. Unused devices and functions should be disabled, vulnerability advisories should be monitored continuously, and security patches should be applied promptly. Devices that are no longer supported should also be replaced in a planned manner. Restricting access to management interfaces by source IP address and minimizing the externally accessible attack surface are also effective measures.

To prevent the abuse of credentials, organizations should implement multi-factor authentication (MFA) for VPNs, cloud services, remote desktop services, and administrative accounts. Shared accounts and accounts that have not been used for extended periods should also be reviewed, while accounts used for routine work should be separated from those used for administrative tasks. Administrative privileges should be limited to the minimum necessary. Monitoring logins from unusual locations or at unusual times, as well as suspicious account creation, can also help detect the misuse of credentials at an early stage.

Because incidents involving third-party vendors, subsidiaries, and cloud environments were also observed, access controls should extend beyond the organization’s own environment to cover external organizations and services. Access granted to vendors and other third parties should be limited to the minimum necessary and restricted to a defined period. Organizations should also enforce multifactor authentication and retain connection logs to reduce the risk of intrusion through third-party environments. Subsidiaries and overseas locations should be encouraged to manage vulnerabilities and accounts according to the same standards as the headquarters.

Meanwhile, there were also cases in which the initial access vector could not be determined. In addition to implementing preventive measures, organizations should establish processes for retaining the records required for post-incident investigations. To limit the spread of an attack, it is also effective to use EDR and other security tools to monitor activities such as suspicious remote access, the acquisition of administrative privileges, the disabling of backup functions, and large-scale file modifications.

Our investigation indicates that combining vulnerability management for internet-facing assets, credential protection, and access controls that extend to third-party vendors can provide effective protection. Rather than focusing solely on preventing every intrusion, organizations should also establish systems that enable them to detect attacks at an early stage and limit the impact if an intrusion occurs.

## Coverage

The following SNORT® rules (SIDs) detect and block this threat:

- Snort 2: 1:67111
- Snort 3: 7:29

### Integrated Coverage

##### Network Security

                    [Cisco Talos
Network Intrusion Prevention](https://blog.talosintelligence.com/category/cisco-talos-network-intrusion-prevention)
                

Network Intrusion Prevention

##### Malware Defense

                            [Cisco Talos
Malware Protection](https://blog.talosintelligence.com/category/cisco-talos-malware-protection)
                        

Malware Protection
