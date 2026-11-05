---
title: ['XenServer']
author: Citrix
url: https://support.citrix.com/external/article/CTX697256/xenserver-security-update-for-multiple-i.html
hostname: citrix.com
description: XenServer Security Update for Multiple Issues
sitename: Citrix
date: "2026-11-03"
fingerprint: edb25c7798b64586
---
**What Customers Should Do** 

We have pushed updates to both the Early Access and Normal update channels of each of XenServer 8.4 and XenServer 9.  We recommend that customers update to the latest version from their chosen channel following the instructions at [https://docs.xenserver.com/us/en/xenserver/8/update.html](https://docs.xenserver.com/us/en/xenserver/8/update.html) or [https://docs.xenserver.com/us/en/xenserver/9/update.html](https://docs.xenserver.com/us/en/xenserver/9/update.html)

We have released updated versions of Workload Balancing and Conversion Manager appliances at [https://www.xenserver.com/downloads](https://www.xenserver.com/downloads).  We recommend that customers update to versions 2026.1.1 or later of Workload Balancing and 2026.2.0 of Conversion Manager.

**What Citrix is Doing** 

We are notifying customers and channel partners about this potential security issue through the publication of this security bulletin on the Citrix Knowledge Center at [https://support.citrix.com/support-home/topic-article-list?trendingCategory=20&trendingTopicName=Security%20Bulletin](https://support.citrix.com/support-home/topic-article-list?trendingCategory=20&trendingTopicName=Security%20Bulletin)

**Obtaining Support on This Issue** 

If you require technical assistance with this issue, please contact Citrix Technical Support. Contact details for Citrix Technical Support are available at [https://www.citrix.com/support](https://www.citrix.com/support)

**Subscribe to Receive Alerts**  

Citrix strongly recommends that all customers subscribe to receive alerts when a security bulletin is created or modified at [https://support.citrix.com/wolken-support/view/aboutsupport/my-support-alerts](https://support.citrix.com/wolken-support/view/aboutsupport/my-support-alerts)

**Reporting Security Vulnerabilities to Citrix** 

Citrix welcomes input regarding the security of its products and considers any and all potential vulnerabilities seriously. For details on our vulnerability response process and guidance on how to report security-related issues to Citrix, please see the following webpage: [https://www.cloud.com/trust-center/support](https://www.cloud.com/trust-center/support)

**Change Log**

| 2026-11-03 | Initial Publication | 

The information on this page is being provided to you on an "AS IS" and "AS-AVAILABLE" basis. The issues described on this page may or may not impact your system(s). Cloud Software Group, Inc. and its subsidiaries (collectively, "Cloud SG") make no representations, warranties, or guarantees as to the information contained herein. ANY AND ALL WARRANTIES, EXPRESS OR IMPLIED, INCLUDING, WITHOUT LIMITATION, INCLUDING, BUT NOT LIMITED TO, IMPLIED WARRANTIES OF MERCHANTABILITY, NON-INFRINGEMENT AND FITNESS FOR A PARTICULAR PURPOSE ARE HEREBY DISCLAIMED. BY ACCESSING THIS PAGE, YOU ACKNOWLEDGE THAT CLOUD SG SHALL IN NO EVENT BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, PUNITIVE, OR CONSEQUENTIAL DAMAGES THAT ARISE OUT OF YOUR USE OR FAILURE TO USE THE INFORMATION CONTAINED HEREIN. Cloud SG reserves the right to change or update the information on this page at any time. We accordingly recommend that you always view the latest version of this page. The information contained herein is being provided to you under the terms of your applicable customer agreement with Cloud SG, and may be used only for the purposes contemplated by such agreement. If you do not have such an agreement with Cloud SG, this information is provided under the cloud.com Terms of Use, and may be used only for the purposes contemplated by such Terms of Use.

**Severity:** Critical

**Description of Problem**  

An issue has been identified that may allow an unauthenticated attacker on the management network to compromise the host and/or any running Workload Balancing (WLB) or Conversion Manager appliances.

This issue has the following identifier:

- CVE-2026-98432

A further issue may allow a privileged user in a guest VM to compromise the host.

This issue has the following identifiers:

- CVE-2026-102703

A further group of issues may allow a malicious unauthenticated attacker on the same network to compromise a network-booting (PXE boot) VM during the initial booting stage or allow the guest VM administrator to bypass the guest VM's secure boot policy.

These issues have the following identifiers:

- CVE-2026-97631

- CVE-2026-45447

- CVE-2024-38797

- CVE-2024-38796

- CVE-2022-36764

- CVE-2022-36763

**Affected Versions**  

All the above issues affect both XenServer 8.4 and XenServer 9. CVE-2026-98432 also affects Workload Balancing (before 2026.1.1) and Conversion Manager (before 2026.2.0).

Feedback

Was this article helpful?

Feedback submitted!

Yes

No
