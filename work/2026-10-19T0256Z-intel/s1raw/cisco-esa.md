---
title: "Cisco Security Advisory: Cisco Secure Email Gateway Arbitrary File Write Vulnerability"
url: https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp
hostname: cisco.com
description: "A vulnerability in the Advanced Malware Protection (AMP) feature of Cisco Secure Email Gateway could allow an unauthenticated, remote attacker to write arbitrary files on the underlying operating system. This vulnerability is due to improper handling of email attachments when the file reputation service is enabled. An attacker could exploit this vulnerability by sending an email that contains a crafted attachment through an affected device. A successful exploit could allow the attacker to write arbitrary files and execute commands with root privileges on the underlying operating system. Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability. This advisory is available at the following link:https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp For further documentation of improvements and fixes in Cisco Secure Email Gateway, see Cisco Secure Email Gateway and Secure Email and Web Manager Security Hardening Release: September 2026."
sitename: sec.cloudapps.cisco.com
date: "2026-10-14"
fingerprint: ed7359574852a32d
---
# Cisco Security Advisory

# Cisco Secure Email Gateway Arbitrary File Write Vulnerability

[Base 9.8](https://sec.cloudapps.cisco.com/security/center/cvssCalculator.x?version=3.1&vector=CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

**Click Icon to Copy Verbose Score**

CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H/E:X/RL:X/RC:X

- A vulnerability in the Advanced Malware Protection (AMP) feature of Cisco Secure Email Gateway could allow an unauthenticated, remote attacker to write arbitrary files on the underlying operating system. This vulnerability is due to improper handling of email attachments when the file reputation service is enabled. An attacker could exploit this vulnerability by sending an email that contains a crafted attachment through an affected device. A successful exploit could allow the attacker to write arbitrary files and execute commands with *root* privileges on the underlying operating system.
Cisco has released software updates that address this vulnerability. There are no workarounds that address this vulnerability. This advisory is available at the following link:
[https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp)
For further documentation of improvements and fixes in Cisco Secure Email Gateway, see [Cisco Secure Email Gateway and Secure Email and Web Manager Security Hardening Release: September 2026](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm).

- ## Vulnerable Products This vulnerability affects Cisco Secure Email Gateway, both physical and virtual, if it is running a vulnerable release of Cisco AsyncOS Software and both of the following conditions are met: 
  - The File Reputation service, which is part of Cisco AMP, is enabled and assigned to a mail policy.
  - The Content Scanner Tools version is earlier than 25.3.0.5525.
For information about which Cisco software releases are vulnerable, see the [Fixed Software](https://sec.cloudapps.cisco.com#fs) section of this advisory.
**Determine Whether File Reputation service is Enabled**
To determine whether file reputation is enabled, complete the following steps: 
  1. Connect to the product web-based management interface.
  2. Choose **Mail Policies > Incoming Mail Policies > Advanced Malware Protection** or **Mail Policies > Outgoing Mail Policies > Advanced Malware Protection.**
  3. Choose a Mail Policy and inspect the **Enable File Reputation** check box.
If the box is checked, file reputation is enabled. **Determine the Content Scanner Tools Version**
To determine which version of Content Scanner Tools is running, use the **contentscannerstatus** command at the CLI. The following example shows a vulnerable version of Content Scanner Tools:
cisco-esa> **contentscannerstatus**
Component Version Last Updated
Content Scanner Tools 25.2.0.5427.15.5.001 Never updated
## Products Confirmed Not Vulnerable Only products listed in the [Vulnerable Products](https://sec.cloudapps.cisco.com#vp) section of this advisory are known to be affected by this vulnerability.
Cisco has confirmed that this vulnerability does not affect the following Cisco products: 
  - Secure Email and Web Manager
  - Secure Web Appliance


- To confirm any attempted exploitation of this vulnerability, review the *system\_logs* using the following command:
esa-appliance> **grep "System Security" system\_logs** If the device is part of a cluster, review the logs of each cluster device. One of the log messages in the following table may be in the output. See the corresponding Recommended Action column for the next steps. Log Message Recommended Action System Security: Suspected compromise indicator was found. Contact TAC for further recommendations. Compromise detected. Follow the instructions in the [Recommendations](https://sec.cloudapps.cisco.com#Recommendations) section of this Security AdvisorySystem Security: Security scan did not complete. Contact TAC for further recommendations. Contact the Cisco Technical Assistance Center (TAC) for further support. System Security: No compromise indicator was found. No compromise detected. Upgrade to a fixed software release if applicable On Cisco Secure Email Cloud, administrators without CLI access may not be able to independently check the described indicators of compromise. Cisco has directly contacted customers who own Cisco Secure Email Cloud devices on which malicious activity was detected. **Note:** Upon successful exploitation of this vulnerability, attackers may obtain command execution with *root* privileges. With this level of access, attackers may remove or hide evidence of exploitation and indicators of compromise. Cisco strongly recommends that cross-checking the network logs and the firewall logs outside of the impacted device to identify any potential suspicious activity, including but not limited to unexpected uploads that were initiated from the affected device to external IP addresses or downloads from malicious IP addresses.

- There are no workarounds that address this vulnerability.


- Cisco considers any workarounds and mitigations (if applicable) to be temporary solutions until an upgrade to a fixed software release is available. To remediate this vulnerability and avoid future exposure as described in this advisory, Cisco strongly recommends that customers upgrade to the fixed software indicated in this advisory. ### Fixed Releases In the following table, the left column lists Cisco software releases. The right column indicates whether a release is affected by the vulnerability that is described in this advisory and the first release that includes the fix for this vulnerability. Customers are advised to upgrade to an appropriate [fixed software release](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) as indicated in this section.
Cisco AsyncOS Software for Cisco Secure Email Gateway Release First Fixed Release 15.5 15.5.5-014 16.0 Migrate to a fixed release. 16.5 16.5.0-780 Cisco strongly recommends that customers who are running Cisco AsyncOS Software releases earlier than Release 16.5 migrate to Release 16.5.0-780. The fix for this vulnerability is also distributed to all licensed and supported Cisco AsyncOS Software releases through an updated version of the Content Scanner Tools package. Content Scanner Tools versions 25.3.0.5525 and later contain the fix for this vulnerability. ### Update the Content Scanner Tools Updating the Content Scanner Tools does not require a software upgrade or a product restart. Customers who have enabled automatic Content Scanner Tools updates are not required to take any action once the update has been applied. Customers who have disabled automatic updates should apply the Content Scanner Tools update manually. **Manual Update**
To manually update the Content Scanner Tools, use the command **contentscannerupdate** at the CLI, as shown in the following example:
cisco-esa> **contentscannerupdate**
Requesting check for new Content Scanner updates. For instructions on how to verify the current version, see the [Vulnerable Products](https://sec.cloudapps.cisco.com#vp) section of this advisory.
**Automatic Update**
To enable automatic updates, complete the following steps on the web-based management interface: 
  1. Choose **Security Services > Service Updates**.
  2. Click **Edit Update Settings**.
  3. Click the **Automatic Updates** check box.
  4. Click **Submit**.
  5. Choose **Commit Changes** on the top right of the page.
  6. Click **Commit Changes** to confirm the uncommitted changes.
For customers who use Cisco Secure Email Cloud Gateway, no action is required. Cisco has taken actions to protect the infrastructure from this vulnerability, and a fixed version of Content Scanner Tools is already deployed as part of the standard upgrade processes for the environment. The Cisco Product Security Incident Response Team (PSIRT) validates only the affected and fixed release information that is documented in this advisory.

- ### On-Premises Physical Devices If exploitation is suspected on a **physical** appliance, Cisco recommends contacting the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/index.html) for further support. To expedite our investigation into the potential compromise, please ensure that remote access is enabled on the affected appliances. For more guidance, see [FAQ for Remote Access on Cisco ESA/WSA/SMA](https://www.cisco.com/c/en/us/support/docs/security/email-security-appliance/117873-faq-esa-00.html).
### On-Premises Virtual Devices If exploitation is suspected on a **virtual** appliance, Cisco strongly recommends the following actions to restore a device to a secure configuration, when possible:
  1. Maintain forensics information, as described in the incident handling policies of the customer. **Important:** Record forensics information before continuing to any of the following steps. Upgrading a compromised instance will destroy forensic data and logs.
  2. Deploy a new virtual machine running one of the fixed software releases.
  3. Rebuild the product configuration without importing any previous configuration files.
  4. Renew credentials and any cryptographic materials that are installed on the appliance.
  5. Continue to monitor the system for anomalous behavior.
**Note**: Cisco Secure Email Gateway appliances can be part of clusters. SSH key pairs are used for authentication purposes between cluster members. Upon successful exploitation of this vulnerability, private SSH keys used for this communication could be accessed on a compromised appliance. Access to these keys may allow the attacker to compromise other cluster members. For this reason, Cisco strongly recommends restoring to a secure configuration each member of a cluster that contains at least one compromised appliance.
If restoring the appliance is not possible, Cisco recommends contacting the [Cisco TAC](https://www.cisco.com/c/en/us/support/index.html) for further support.
If exploitation is not suspected and the device is running an affected software release, Cisco strongly recommends upgrading to a fixed release. ### Cisco Secure Email Cloud Cisco has conducted a thorough threat intelligence investigation on devices that belong to Cisco Secure Email Cloud. Cisco has directly contacted customers who own Cisco Secure Email Cloud devices where indicators of possible compromise were identified. Cisco is engaged in remediation and recovery operations. Cisco has already deployed mitigations that are within Cisco's management. Additionally, Cisco strongly recommends that customers who have been contacted restore a device to a secure configuration by renewing credentials and any cryptographic materials that are installed on the appliance, when possible. In addition, Cisco strongly recommends restricting access to the appliance and implementing robust access control mechanisms. ### General Recommendations For Hardening
  - Upgrade the appliance to the latest version of Cisco AsyncOS Software.
  - Prevent access from the internet to the appliance. If internet access to the appliance is required, restrict appliance access to only known, trusted hosts on ports and protocols that are included in the user guides.
  - For Cisco Secure Email Gateway, separate mail and management functionality onto individual network interfaces. This reduces the chance of unauthorized users accessing the internal management network. For more information, see the device user guides.
  - Protect Cisco Secure Email Gateway and Cisco Secure Email and Web Manager appliances behind a filtering device such as a firewall, and filter management traffic to and from the appliances while allowing only known, trusted hosts to send traffic to the appliances. Using a two-layer firewall can provide flexibility in network planning so that end users do not connect directly to the outer DMZ. See the Deployment sections of the User Guides for [Cisco Secure Email Gateway](https://www.cisco.com/c/en/us/td/docs/security/esa/esa16-5/user_guide/b_ESA_Admin_Guide_16-5.html) and [Cisco Secure Email and Web Manager](https://www.cisco.com/c/en/us/td/docs/security/security_management/sma/sma16-5/user_guide/b_sma_admin_guide_16_5.html).
  - Regularly monitor log traffic for any unexpected traffic to or from appliances. Logging should be sent to an external server, if possible, and kept for a long enough duration so that post-event investigations can be performed with sufficient log data.
  - Disable HTTP for the main administrator portal.
  - Disable any network services that are not required, including HTTP and FTP. For more information about specific service functionality, see the Cisco Secure Email Gateway and Cisco Secure Email and Web Manager user guides.
  - Use a strong form of end-user authentication to the appliances, such as SAML or Lightweight Directory Access Protocol (LDAP). For more secure methods of authentication, see [Authentication Options for End Users Accessing Spam Management Features](https://www.cisco.com/c/en/us/td/docs/security/esa/esa16-5/user_guide/b_ESA_Admin_Guide_16-5/b_ESA_Admin_Guide_12_1_chapter_0100000.html#con_1623537).
  - Change the default administrator password to a more secure variant. Restrict access to the administrator account by creating user accounts based on necessary access requirements. In addition, create operator accounts for all administrators.
  - Using SSL/TLS, obtain an SSL certificate from a certificate authority (CA) or create a self-signed certificate.
### Useful Resources The following resources can help restore an affected appliance to a secure state. Some of the documents are related to a specific product, but the procedures are mostly interchangeable. If customers have specific questions about a procedure, contact [Cisco TAC](https://www.cisco.com/c/en/us/support/index.html).
To download replacement virtual appliances, see the relevant Cisco Software Download page: The [User Guide for AsyncOS 16.5 for Cisco Secure Email and Web Manager](https://www.cisco.com/c/en/us/td/docs/security/security_management/sma/sma16-5/user_guide/b_sma_admin_guide_16_5.html) provides more information. See the following sections:
  - For information about exporting reporting data from an appliance, see [Working with Reports](https://www.cisco.com/c/en/us/td/docs/security/security_management/sma/sma16-5/user_guide/b_sma_admin_guide_16_5/b_NGSMA_Admin_Guide_chapter_010.html).
  - For information about how to purge messages in the quarantine, see [Spam Quarantine](https://www.cisco.com/c/en/us/td/docs/security/security_management/sma/sma16-5/user_guide/b_sma_admin_guide_16_5/b_NGSMA_Admin_Guide_chapter_0101.html).
  - For additional information, see [Centralizing Policy, Virus, and Outbreak Quarantines](https://www.cisco.com/c/en/us/td/docs/security/esa/esa16-5/user_guide/b_ESA_Admin_Guide_16-5/b_ESA_Admin_Guide_12_1_chapter_0101011.html#con_1158787).

- In October 2026, the Cisco PSIRT became aware of active exploitation of this vulnerability.

- This vulnerability was found during internal security scanning.

- To learn about Cisco security vulnerability disclosure policies and publications, see the [Security Vulnerability Policy](http://www.cisco.com/web/about/security/psirt/security_vulnerability_policy.html). This document also contains instructions for obtaining fixed software and receiving security vulnerability information from Cisco.
For additional information on Cisco's vulnerability management, disclosure cadence, and software patching strategy, see [Cisco's Transition to a Risk-Based Vulnerability Disclosure Model](https://sec.cloudapps.cisco.com/security/center/resources/risk-based-disclosure).

- Version Description Section Status Date 1.0 Initial public release. - Final 2026-OCT-14 [Show Less]

- ### SOFTWARE DOWNLOADS AND TECHNICAL SUPPORT The [Cisco Support and Downloads](https://www.cisco.com/c/en/us/support/index.html) page on Cisco.com provides information about licensing and downloads. This page can also display customer device support coverage for customers who use the My Devices tool. Please note that customers may download only software that was procured from Cisco directly or through a Cisco authorized reseller or partner and for which the license is still valid.
Customers who purchase directly from Cisco but do not hold a Cisco service contract and customers who make purchases through third-party vendors but are unsuccessful in obtaining fixed software through their point of sale should obtain upgrades by contacting the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html). Customers should have the product serial number available and be prepared to provide the URL of this advisory as evidence of entitlement to a free upgrade.
When [considering software upgrades](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes), customers are advised to regularly consult [the advisories](https://www.cisco.com/go/psirt) for the relevant Cisco products to determine exposure and a complete upgrade solution. In all cases, customers should ensure that the devices to be upgraded contain sufficient memory and confirm that current hardware and software configurations will continue to be supported properly by the new release. If the information is not clear, customers are advised to contact the [Cisco Technical Assistance Center (TAC)](https://www.cisco.com/c/en/us/support/web/tsd-cisco-worldwide-contacts.html) or their contracted maintenance providers.
### LEGAL DISCLAIMER DETAILS CISCO DOES NOT MAKE ANY EXPRESS OR IMPLIED GUARANTEES OR WARRANTIES OF ANY KIND, INCLUDING THE WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR USE. WITHOUT LIMITING THE GENERALITY OF THE FOREGOING, CISCO DOES NOT GUARANTEE THE ACCURACY OR COMPLETENESS OF THIS INFORMATION. THIS DOCUMENT IS PROVIDED ON AN "AS IS" BASIS. YOUR USE OF THE INFORMATION ON THE DOCUMENT OR MATERIALS LINKED FROM THE DOCUMENT IS AT YOUR OWN RISK. CISCO RESERVES THE RIGHT TO CHANGE OR UPDATE THIS DOCUMENT AT ANY TIME. Copies or summaries of the information contained in this Security Advisory may lack important information or contain factual errors. Customers are advised to visit the [Cisco Security Advisories](https://www.cisco.com/go/psirt) page for the most recent version of this Security Advisory. The Cisco Product Security Incident Response Team (PSIRT) assesses only the affected and fixed release information that is documented in this advisory. See the [Cisco Security Vulnerability Policy](https://sec.cloudapps.cisco.com/security/center/resources/security_vulnerability_policy.html#fixes) for more information.
