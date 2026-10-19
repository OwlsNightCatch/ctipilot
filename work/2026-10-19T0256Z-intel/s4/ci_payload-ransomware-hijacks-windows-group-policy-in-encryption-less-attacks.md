---
title: PAYLOAD ransomware hijacks Windows Group Policy in encryption-less attacks
author: Bill Mann
url: https://cyberinsider.com/payload-ransomware-hijacks-windows-group-policy-in-encryption-less-attacks/
hostname: cyberinsider.com
description: A PAYLOAD ransomware incident weaponized Microsoft Active Directory Group Policy to disrupt a firms computers without encrypting files.
sitename: CyberInsider
date: "2026-09-22"
categories: ['News', 'Ransomware']
fingerprint: "8489a9dfdcb317c2"
---
A PAYLOAD ransomware incident weaponized Microsoft Active Directory Group Policy to disrupt an organization’s Windows computers without deploying ransomware or encrypting files.

Instead, the attackers used the company’s own administration infrastructure to display ransom notes, change wallpapers, deactivate local administrator accounts, and turn off Windows Firewall across the network.

Kaspersky’s Global Emergency Response Team (GERT) [investigated the attack](https://securelist.com/tr/payload-ransomware-via-group-policy/121335/) after an incident at an unnamed manufacturing organization in the Middle East. Kaspersky researchers Ahmad Zaidi Said and Elsayed Elrefaei said the attackers first accessed the network on April 11 using a compromised domain account through the company’s FortiGate SSL VPN.

By April 13, the intruders had obtained privileges equivalent to a domain administrator and created a malicious Group Policy Object (GPO) named “PAYLOAD.” Group Policy is a legitimate Windows administration feature that allows organizations to centrally configure thousands of computers and user accounts through Active Directory.

Because PAYLOAD was linked at the root of the company’s domain, its settings could reach virtually every domain-joined Windows workstation. The attackers used it to distribute a README-payload.txt ransom note, replace desktop and lock-screen images with payload.jpg, display a ransom message at login, and disable the built-in local administrator account.

A second GPO named “win Firewall Off” disabled Windows Firewall across domain, private, and public profiles.

However, the changes did not appear immediately. Kaspersky found that the malicious policies had reached endpoints on April 13 but remained largely dormant until computers restarted the following day. When employees began rebooting their systems on April 14, the policies took effect across the organization and caused widespread disruption.

The attackers also exfiltrated data from file servers and other systems, and later published the stolen information on the dark web. Kaspersky also found a PAYLOAD ransomware variant targeting ESXi servers, but found no evidence that Windows files were encrypted.

Forensic examination found no malicious Windows executable, persistence mechanism, or active malware process. According to Kaspersky, the attack effectively lived inside Active Directory, allowing it to bypass security monitoring focused primarily on suspicious files and processes.

The incident highlights the risks of attackers gaining control of Group Policy, which previous ransomware operations, including Ryuk, LockBit, and BlackCat, have also abused for network-wide deployment.

Kaspersky recommends that organizations closely monitor the creation and modification of GPOs, particularly policies linked at the domain level, and monitor SYSVOL for unexpected files or configuration changes. Companies should also enforce phishing-resistant MFA for VPN access, restrict who can create and link Group Policies, centrally collect Active Directory audit logs, and protect privileged administrator accounts.

Organizations responding to this type of attack should remove malicious Group Policies from domain controllers before cleaning individual computers, or the compromised policies can be reapplied during the next Group Policy refresh.

## Leave a Reply Cancel reply
