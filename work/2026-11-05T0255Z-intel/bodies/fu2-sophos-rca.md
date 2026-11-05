---
title: "INC-2026-002: Developer Job Lure Repository Leads to Malware Execution on a Sophos Employee Mac"
url: https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002
hostname: sophos.com
sitename: SOPHOS
date: "2025-11-25"
tags: ['MDR, cyber, incident, managed, detect, endpoint, firewall, network, email, phishing, next gen, www.sophos.com']
fingerprint: a5d8a491483b1382
---
# INC-2026-002: Developer Job Lure Repository Leads to Malware Execution on a Sophos Employee Mac

## Overview

On 15 September 2026, an industry partner informed Sophos, through established intelligence-sharing channels, that they believed that a Sophos employee’s corporate macOS device had been compromised. The Sophos internal incident detection and response (IDR) team opened an incident the same day. The investigation confirmed that on 14 September 2026 the employee had cloned a public code repository presented as a job interview coding assignment and opened it as a workspace in Visual Studio Code (VS Code).

The repository contained a weaponized VS Code workspace settings file that replaced the editor’s integrated terminal profile. When a terminal opened in the workspace, the modified profile silently downloaded and ran a multi-stage payload. SophosLabs identified the payload as the [BeaverTail loader](https://malpedia.caad.fkie.fraunhofer.de/details/js.beavertail) followed by the [InvisibleFerret backdoor](https://attack.mitre.org/software/S1245/): an in-memory remote access tool (RAT) able to steal browser-stored credentials, keychain data, SSH keys, and cryptocurrency-wallet data, and to exfiltrate the process environment to the threat actor.

The Sophos Endpoint agent was installed on the employee’s device but was not functional. Its core services were not running, so the agent was not receiving updates, not enforcing protection and not reporting to the Sophos Central management console. SophosLabs confirmed that a functioning agent would have blocked the chain at the first dropped file, and that the delivery domain was already on the Sophos block list.

Containment began on the day of the report. Corporate sessions were revoked, the password was reset, and the device was moved to a non-compliant device management group to block access to corporate resources. A third-party application (OAuth) authorization that had survived the session revocation was identified and revoked. The in-memory implant was terminated when the device was rebooted on 15 September; no persistence mechanism was found. A sweep of the whole estate for the confirmed indicators found no other affected hosts. Follow-on work found a small population of other corporate devices that were compliant in identity and device management, but which were not reporting to the corporate management console. That population is being remediated, and the macOS device build and compliance processes have been changed to close the onboarding gap that let the agent be skipped or registered outside the corporate console.

## Impact

The impact of this incident was limited to a single internal Sophos macOS endpoint and the associated user account. No Sophos products or services, customers, customer data, or customer-facing systems were affected.

The malware ran in memory on the device for about 26 hours, from its execution on 14 September until the device was rebooted on 15 September. Analysis of the environment infected by the malicious process found no cloud access keys, personal access tokens, or passwords. The residual exposure from that process was assessed as the user’s ssh-agent session. The user confirmed that only personal SSH keys were in use and that they had been revoked, and that no corporate system was reached over SSH during the exposure window.

On 15 September, a third-party application authorization linked to the user’s source code platform account was used to make 27 read requests against two internal Sophos source code repositories. The requests came from a network address not previously associated with the user and were treated as unauthorized. The authorization was revoked on 16 September, and no further use of it was observed.

The following were explicitly confirmed during the investigation:

- No other host in the Sophos estate matched the confirmed indicators (no co-victims).
- No persistence mechanism was installed on the affected device.
- No cloud platform activity was recorded for the user’s identity or for the network addresses associated with the incident.
- No mailbox forwarding or inbox rule changes were made to the user’s account.
- No Sophos product, service, or customer environment was accessed.

## Timeline

All times are in UTC. Rows are mapped across the incident response lifecycle: detection and analysis, containment, eradication and recovery, and post-incident activity.

| Time (UTC) | Event | Actor | 
|---|---|---|
| 11 Jun 2026 | The Sophos Endpoint agent on the affected device was last seen in Sophos Central. After this date the agent stopped functioning and reporting | Undetermined | 
| 10–11 Sep 2026 | Browser identity telemetry recorded the employee’s corporate password being entered on a public source code platform’s sign-in page, including during a third-party ‘sign in with’ authorization for a coding practice website | User (Sophos employee) | 
| 14 Sep 2026 15:17:59 | A repository presented as a job interview coding assignment was cloned to the device and opened as a VS Code workspace | User (Sophos employee) | 
| 14 Sep 2026 15:19:31 | The weaponized workspace settings ran when a terminal opened. The first- and second-stage payload files were written to the user’s profile | Threat actor | 
| 14 Sep 2026 15:24:33 | VS Code was granted Full Disk Access, which gave its child processes, including the malicious ones, broad filesystem access | User (Sophos employee) | 
| 14 Sep 2026 15:36:11 | A package manager dependency install ran from the payload directory, confirming live code execution. From this point the final-stage backdoor ran in memory | Threat actor | 
| 15 Sep 2026 13:37 | An industry partner reported the probable compromise through intelligence-sharing channels. An incident was opened, and it was established that the device was not reporting to Sophos Central | Industry partner / IDR (Detection & Analysis) | 
| 15 Sep 2026 (afternoon) | Active sign-in sessions were revoked and the password was reset. The device was moved to the non-compliant device management group | IT / IDR (Containment) | 
| 15 Sep 2026 (afternoon) | A third-party application authorization that survived the session revocation was used for 27 read requests against two internal source code repositories | Undetermined | 
| 15 Sep 2026 18:05 | The device was rebooted, ending the in-memory implant. No persistence mechanism was found | User (Sophos employee) | 
| 15–16 Sep 2026 | SophosLabs completed analysis of the three-stage chain (BeaverTail loader, InvisibleFerret backdoor). An estate-wide indicator sweep found no other affected hosts | SophosLabs / IDR (Detection & Analysis) | 
| 16 Sep 2026 14:52 | The third-party application authorization was revoked and the user’s source code organization access was removed | IT / IDR (Containment) | 
| 16–17 Sep 2026 | Forensic collection from the device confirmed execution of the payload and recovered the malware source. The credential exposure scope was narrowed, and a review of cloud platform logs found no activity linked to the user’s identity or to the network addresses associated with the incident | IDR (Detection & Analysis) | 
| 17–22 Sep 2026 | Endpoint engineering analyzed the agent’s state on the device and confirmed that the agent’s core services were not running. A fleet-wide review began for other devices that were compliant but not reporting | Endpoint engineering / IDR (Post-incident) | 
| 24 Sep 2026 | A fresh Sophos Endpoint agent was installed. The device reported to Sophos Central and was isolated pending return. A replacement device was issued, and the incident was closed | IT / IDR (Eradication & Recovery) |
