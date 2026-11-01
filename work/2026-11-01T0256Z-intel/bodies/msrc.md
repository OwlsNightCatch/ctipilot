---
title: Microsoft’s response to compromised eMudhra certificate authority keys
author: MSRC
url: https://www.microsoft.com/en-us/msrc/blog/2026/10/microsoft-response-to-compromised-emudhra-certificate-authority-keys
hostname: microsoft.com
sitename: microsoft.com
date: "2026-10-26"
fingerprint: fd57fb967f3e6cc5
---
# Microsoft’s response to compromised eMudhra certificate authority keys

*Update, October 27, 2026: Microsoft has removed the seven affected certificates from the Microsoft Edge trust list. We've also added more detail on why these keys pose a risk and why organizations should be cautious about restoring trust locally. There's also a link to the Microsoft Trusted Root Program announcement.*

Microsoft is responding to an issue involving eight eMudhra intermediate certificate authority (CA) private keys: six associated with TLS and two with code signing. Because these keys could be recovered, they could potentially be used to create certificates or sign content that appeared to come from a trusted CA. The issue arose in eMudhra’s certificate hierarchy; it was not a compromise of Microsoft systems.

## Why this matters

A certificate created with one of these keys would look legitimate to browsers and operating systems, even though eMudhra never authorized it. The six TLS keys could be used to impersonate a website or service and potentially intercept users' communications. The two code-signing keys could be used to make malicious software appear to come from a trusted publisher. Blocking the affected certificate authorities promptly means certificates created with these keys are no longer trusted.

## Immediate protections

On October 20, Microsoft published an update to the Windows Disallowed Certificate Trust List to block the affected certificate authorities.

Microsoft also deployed a separate CRLSet update for Microsoft Edge and WebView2 to block the affected TLS certificates signed by the affected certificate authorities. The Edge and WebView2 update is delivered automatically through the component update mechanism and does not require customers to install a new browser version.

These protections address the identified compromised intermediate keys. They are separate from eMudhra’s revocation of the affected intermediate certificates. They are also separate from Microsoft’s decision about which roots to keep trusting, described below.

## Removing roots from the Windows and Edge trust lists

On October 26, Microsoft released an out-of-band Windows update that removes seven certificates associated with the affected hierarchies: six eMudhra G3 roots and an AAA Certificate Services cross-sign, from the Windows trust list.

On October 27, Microsoft removed the same seven certificates from the Microsoft Edge trust list.

Once the changes reach a device, these certificates will no longer be trusted by default through the respective trust lists. **Removing a root from a trust list is not the same as revoking the known impacted intermediate certificate authorities**. This is a separate trust decision, broader than blocking the identified compromised intermediate keys. Organizations with a specific compatibility need may choose to trust a certificate locally, subject to their own security assessment and policies. They should not restore trust in an affected hierarchy without understanding the associated risk.

This is most important for software that doesn't reliably check revocation or Microsoft's disallowed-certificate list. If that software keeps or restores trust in the removed certificates, certificates associated with the compromised intermediates could still be accepted as valid. Organizations with a specific compatibility need may choose to trust a certificate locally, subject to their own security assessment and policies. Before they do, they should evaluate how their own applications and systems perform these checks.

Microsoft is evaluating the remaining eMudhra roots separately and will sequence any further changes as affected customers transition away from those hierarchies.

## What customers should do

- **Keep updates flowing.** Allow automatic Windows certificate trust updates and Edge component updates to reach your devices.
- **Check disconnected Windows devices.** If you manage Windows devices that don't get automatic updates, make sure your update process delivers the updated Disallowed Certificate Trust List and the upcoming trust-list changes. See [Configure trusted roots and disallowed certificates in Windows | Microsoft Learn](https://learn.microsoft.com/en-us/windows-server/identity/ad-cs/configure-trusted-roots-disallowed-certificates) for details.
- **Review any disconnected Azure devices** running on Virtual Machine Scale Sets (VMSS) or single-instance VMs. Updated images are available in Azure Marketplace, and customers can deploy them to protect against this vulnerability.
- **Replace dependent certificates.** If any of your certificates chain to one of the seven certificates being removed, find those dependencies. Then get replacement certificates or an alternative trusted chain before the changes reach your devices.

Affected customers can find the full list of removed eMudhra certificates and next steps in the Microsoft Trusted Root Program's [October 26, 2026 announcement](https://github.com/TrustedRootProgram/Program-Requirements/blob/main/Announcements.md#october-26-2026).

Microsoft continues to investigate the scope of this issue and will update this post if additional findings or trust changes materially affect customers.
