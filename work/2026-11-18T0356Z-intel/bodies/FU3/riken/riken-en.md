---
title: Notice regarding a possible personal information leak affecting Fugaku and RIKYU users following unauthorized access to the supercomputer Fugaku
url: https://www.riken.jp/en/news_pubs/news/2026/20261116_2/index.html
hostname: riken.jp
sitename: riken.jp
date: "2026-11-17"
fingerprint: "8d9a6e1e6b16f39d"
---
Nov. 17, 2026

# Notice regarding a possible personal information leak affecting Fugaku and RIKYU users following unauthorized access to the supercomputer Fugaku

## Overview

On November 13, it was confirmed that a system involved in the operation of the supercomputer Fugaku, operated by the RIKEN Center for Computational Science (R-CCS), was subject to unauthorized access by an external third party on November 12.

An investigation revealed that files stored in users’ home directories on Fugaku, as well as information registered in the user authentication system, were either taken or may have been taken from the system. This information includes users’ names and email addresses, as well as authentication credentials stored by users for connecting to systems or services outside of RIKEN. Up to 4,222 users registered with Fugaku and up to 375 users registered with RIKYU may have been affected.

On November 13, the unauthorized access was confirmed, and RIKEN suspended operations of Fugaku at 4:30 AM on November 14 and blocked access from the outside. We are currently investigating the scope of the impact and the cause, as well as implementing measures to prevent a recurrence.

We deeply apologize for the considerable concern and inconvenience this has caused our users and all other parties involved.

### 1. Timeline

- Maintenance and management of the system in question were outsourced to an external service provider, and after suspicious network traffic was detected on November 12, we promptly coordinated with the provider to begin an investigation.
- At 4:33 PM on November 13, it was confirmed that unauthorized access had taken place.
- At 4:30 AM on November 14, the operations of Fugaku were suspended and external access was suspended.
- At 4:18 PM on November 15, emails were sent to users.

### 2. Results of the Investigation

Investigations revealed that, from November 10 to 13, 2026, an external third party gained unauthorized access to Fugaku’s internal operational network by using a publicly accessible web page displaying Fugaku’s operational status (the dashboard). The exact method that was used to gain unauthorized access is currently under investigation.

- The unauthorized party tampered with multiple internal servers. It was also confirmed that files stored in users’ home directories, as well as information from the user authentication system (names email addresses, and IDs of users) were either taken from the system or may have been taken from the system. The information also included authentication credentials stored by users for connecting to other systems or services.

### 3. Information which was or may have been compromised

- (1)Information registered in the user authentication system (Affected: Up to 4,597 individuals)
  - Names, email addresses, and user IDs for users of Fugaku (up to 4,224 individuals)
  - Name, email for users of the AI for Science supercomputer RIKYU (up to 375 users)
- (2)Files stored in users’ home directories, etc.
  - Authentication credentials stored by users for connecting to other systems or services (such as SSH private keys and access keys)
  - Files stored by users (research data)
At present, there is no evidence that research data or files were exfiltrated. Whether data containing the personal information of third parties was taken is currently under investigation.

Furthermore, we have confirmed that the unauthorized party attempted to connect to other systems using some of the obtained credentials. In cooperation with relevant agencies, we are investigating whether any damage resulted from this, and whether there has been any secondary damage caused by the misuse of users’ credentials.

In addition, we have confirmed that some of the compromised servers were tampered with, including through the installation of malicious programs. We are currently investigating the details of this.

### 4. RIKEN’s response

- RIKEN reported the situation to the Personal Information Protection Commission (November 16 at 5:55 PM), the Ministry of Education, Culture, Sports, Science and Technology (November 13 at 8:59 PM), and the relevant organizations of the HPCI (High Performance Computing Infrastructure) (November 15 at 10:51 AM).
- We suspended the operation of Fugaku and blocked the route used for unauthorized access (November 14 at 4:30 AM).
- We halted all running and queued compute jobs and simultaneously notified affected users (November 15, 4:18 PM).
- We isolated the system used for the unauthorized access (November 13 at 10:07 PM) and replaced the administrative keys (November 14, 8:20 PM).
- We have invalidated the public keys used by all users for login and informed them of the details of the incident. We also requested that they invalidate any authentication credentials stored on Fugaku (November 15 at 4:18 PM).

### 5. Future actions

- We will conduct a thorough investigation into the scope of the impact and the cause. There is no concrete evidence at the present that user research data was taken outside. We will continue to investigate whether personal information of third parties was included in the data.
- We will resume operation of Fugaku after implementing measures to prevent recurrence (including addressing any vulnerabilities in the exploited software), rebuilding the compromised servers, reviewing the network configuration, and implementing state-of-the-art security measures utilizing AI.
- We will review the division of responsibilities for operations and maintenance to ensure that we can more promptly respond to emergencies.
- We will promptly disclose any new findings from the investigation.

### 6. To all users

- For any SSH private key stored on Fugaku, please revoke or remove the corresponding public key from each external service where it is authorized, and generate a new key pair. Please revoke and replace any other stored authentication credentials through the relevant service.
- Please also be wary of suspicious emails claiming to be from Fugaku or RIKEN. RIKEN will never ask you for your password or other personal information via email.

## Inquiries

Inquiries regarding the content of this article:

RIKEN Center for Computational Science (R-CCS)

HPCI Help Desk | helpdesk@hpci-office.jp

Media inquiries:

RIKEN Communications Division

[Contact Form](https://krs1.riken.jp/m/contact_en/)
