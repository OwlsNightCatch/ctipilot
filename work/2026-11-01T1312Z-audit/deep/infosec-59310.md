# extract: served via trafilatura-direct
---
title: vCenter Flaw Exploited Just Five Days After Disclosure
author: Alessandro Mascellino
url: https://www.infosecurity-magazine.com/news/vcenter-cve-2026-59310-exploited/
hostname: infosecurity-magazine.com
description: Attackers exploited a critical-severity vCenter flaw five days after Broadcom disclosed it
sitename: Infosecurity Magazine
date: "2026-08-13"
fingerprint: bcb5e1d19b23d78b
---
A critical-severity VMware vCenter vulnerability has been exploited within five days of disclosure by Broadcom, with attackers deploying an open-source reverse shell to hold access to compromised systems.

The treat research team at German firm Quirso discovered the campaign during an incident response engagement and [published its findings](https://medium.com/@quirso_de/active-exploitation-of-cve-2026-59310-361-victim-ips-across-47-countries-9783187cc6ff) on August 10.

The digital forensics company assessed a suspected advanced persistent threat (APT) actor was responsible, counting 361 victim IP addresses across 47 countries while cautioning that an IP address does not necessarily correspond to a single organization.

The vulnerability, CVE-2026-59310, is acritical directory traversal flaw in the vCenter Syslog server rated CVSS 9.8. Broadcom said an unauthenticated attacker with network access to vCenter can exploit it to execute arbitrary code, turning a service built to collect logs into a route into the operating system.

[Read more on VMware attacks: Play Ransomware Expands to Target VMware ESXi Environments](https://www.infosecurity-magazine.com/news/play-ransomware-target-vmware-esxi/)

## **Five Days From Advisory to Compromise**

Broadcom published [advisory relating to the flaw](http://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/38017) on July 29, stating in an accompanying FAQ that it had not observed exploitation. It revised the advisory on August 3 to add 8.0 U2f express patches.

Quirso's team said they first observed compromised systems contacting attacker infrastructure on August 3. The following day brought 151 further victim IPs, and by August 5 roughly 95% of the 361 total had appeared. Germany, the United States, Turkey, Iran and France accounted for 185 of them.

While the attacker may have had prior knowledge of the flaw, Quirso said the strong correlation between disclosure and exploitation points to the advisory as the campaign's starting point.

## **Two Clocks to Manage**

For persistence the actor deployed reverse\_ssh, an open-source SSH-based reverse shell framework built for penetration testing.

Because it dials outward rather than accepting inbound connections, it can bypass controls designed to block unsolicited inbound access. QUIRSO stressed that its presence alone is not proof of compromise.

Jason Soroko, senior fellow at certificate lifecycle management (CLM) provider Sectigo, said patching would not resolve the incident by itself. "There are therefore two clocks to manage," he said, one for closing the vulnerability and one for evicting anyone who entered before the patch.

Broadcom has not published a workaround. Fixed vCenter releases are 9.1.0.0300, 9.0.2.0100, and 8.0 U3k or 8.0 U2f depending on the deployed branch, and address both critical vCenter flaws in the advisory, the exploited directory traversal and an authentication bypass in VMware Directory Service.
