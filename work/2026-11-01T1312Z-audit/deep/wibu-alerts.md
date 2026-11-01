# extract: served via trafilatura-direct
---
title: "Product Alerts: Compatibility, Operation, and Deployment Notices"
author: WIBU-SYSTEMS AG
url: https://www.wibu.com/support/product-alerts.html
hostname: wibu.com
description: Review Wibu product alerts about compatibility, operation, and deployment issues, with official guidance for assessment and mitigation.
sitename: WIBU-SYSTEMS AG
date: "2026-02-09"
fingerprint: "3414363889cbf6c8"
---
# Product Alerts: Compatibility, Operation, and Deployment Notices


Product Alerts provide official notifications about product-related conditions that may affect compatibility, operation, or deployment in specific environments.

These alerts are published to ensure transparency and to support timely assessment and mitigation where required.


**Last updated on: 2026-10-29 5:00 pm CET (CodeMeter License Central PHP Vulnerabilities)**

## Security Advisory: PHP Vulnerabilities (CVE-2026-109618, CVE-2026-109619) in CodeMeter License Central and Extensions

### Overview

The security vulnerabilities **CVE-2026-109618** and **CVE-2026-109619** have been disclosed in the PHP scripting language. Because both the web interface of **CodeMeter License Central** and the associated **CodeMeter License Central Extensions** (WebDepot, Gateways, Portal, Connectors) use PHP components, unpatched systems are affected by these vulnerabilities. **CodeMeter Runtime** as well as **WibuKey** installed locally on end-user systems are **not affected**.

On this page, we provide continuous updates on the remediation status for systems hosted by Wibu Operating Services (WOPS), as well as update availability and instructions for self-hosted on-premises installations.

#### Update History (Change Log of This Advisory)

- **Update 2026-10-29, 5:00 pm CET (New):**
  - **New Version of the [“PHP-Patch Update Installer” (PHP CVE Update Installer)](https://www.wibu.com/support/developer/software-downloads.html#download-273) Available on the Website (since 2026-10-28, 5:30 pm CET):** This new version is applicable to **CodeMeter License Central 5.0.x and 5.1.x** and works just like the previous version, but additionally applies the post-update configuration recommendations to the CodeMeter License Central frontend image as described in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273). If you have already run the previous version of the installer, you can run the installer again to apply these configuration changes.
  - **CodeMeter License Central 5.2.3 Released:** For users of **CodeMeter License Central 5.2.x**, updating to this version—in addition to the changes listed in the Release Notes—automatically applies the post-update configuration recommendations to the CodeMeter License Central frontend image described in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273). Furthermore, the new update installer enables a seamless upgrade of an existing **CodeMeter License Central 5.0.x or 5.1.x installation to version 5.2.3** to keep deployed installations as up to date as possible.
- **Update 2026-10-27, 6:00 pm CET:**
  - **New Version of the [“PHP Patch Manual”](https://www.wibu.com/support/developer/software-downloads.html#download-273) Available on the Website:**
    - The updated manual adds dedicated chapters for each specific **CodeMeter License Central version (5.2, 5.1, 5.0)** deployed by operators, as well as for the **4.x versions**, providing detailed step-by-step instructions on what actions to take in each case.
    - It also includes the recommended restart along with the specific criteria operators can use afterwards to identify whether the patch was applied successfully.
- **Update 2026-10-27, 9:30 am CET:**
  - **WOPS Hosting (Downstream Systems & Containers – Completed):** Updates for all downstream systems and containers have been completed. In individual cases, customers have been contacted directly for clarification.
  - **CodeMeter License Central 5.2 (5.2.2) and 4.x:** In addition to applying the update from the registry (for 5.2.2) or the operating system patches via Ubuntu Pro (for 4.x), we **strongly recommend** applying the `php.ini` configuration described in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273). This implements a restrictive configuration, rules out an unlikely residual attack vector (CVE-2026-115560) until the next regular PHP release in accordance with a recent [PHP project advisory](https://www.php.net/archive/2026.php#2026-10-23-1), and preventively makes the exploitation of future vulnerabilities more difficult.
  - **CodeMeter License Central 5.0:** Unified the fixed target version designation to **5.0.1** (consistent with the Security Advisory).
- **Update 2026-10-23, 7:00 pm CEST:**
  - **WOPS Hosting (Downstream Systems & Containers):** All hosted 5.x systems have been updated. For 4.x, all systems that can be patched automatically have been updated; individual cases are currently being clarified.
  - The patch installer for **CodeMeter License Central 5.1.2 and 5.0.1** is now available for download from the Wibu-Systems website as the [**“PHP-Patch Update Installer”**](https://www.wibu.com/support/developer/software-downloads.html#download-273), along with the accompanying [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273).
  - Operating system updates via **Ubuntu Pro** for **CodeMeter License Central 4.x (On-Premises)** have been successfully tested and are now officially **approved and released**.
- **Update 2026-10-23, 2:30 pm CEST: CodeMeter License Central 5.2.2** has been released and is available for download from the registry.
- **Update 2026-10-23, 2:00 pm CEST: WebDepot 24.09g** as well as **CodeMeter License Portal 25.09a and 26.09a** are available on the Wibu-Systems website; the CodeMeter License Portal versions are also available via Harbor. Status update for CodeMeter License Central 5.2.2, 5.1.2, and 5.0.1. Clarification on WOPS infrastructure systems (including standard Gateways and WebDepots) and maintenance windows.
- **Initial Publication 2026-10-22, 4:30 pm CET:** Initial publication of the security advisory. Infrastructure systems operated by WOPS have been fully patched; initial overview and mitigation guidance for on-premises systems provided.

### 1. Status for Systems Hosted by Wibu-Systems (WOPS)

For customers whose systems are operated by Wibu Operating Services (WOPS), Wibu-Systems handles all necessary remediation steps:

- **Infrastructure Systems Including Standard Gateways and WebDepots (Completed):** All affected infrastructure systems—including all WOPS-provided Gateways and WebDepots without customer-specific customizations—have already been updated via patches from the operating system vendors and are no longer affected by CVE-2026-109618 and CVE-2026-109619.
- **Downstream Systems & Containers (Completed):** All hosted systems running version **5.x** as well as all automatically patchable systems running version **4.x** have been updated. In individual cases, customers have been contacted directly for clarification.
- **Note on Service Availability During Updates:** In many cases, applying these updates will cause **no service interruptions at all**. Where a brief interruption does occur, it typically lasts only around 5 minutes (and up to a maximum of 30 minutes). Please understand that, for organizational reasons, any such brief maintenance windows cannot be announced or scheduled in advance.
- **Customer-Specific Customizations:** Customized WebDepots, Gateways, Portals, and Connectors are automatically included by WOPS as part of this maintenance. Should your cooperation or approval be required in individual cases, our team will contact you directly.

### 2. Required Actions and Remediation Strategy for On-Premises Systems (Self-Hosted)

For self-hosted systems, it is the responsibility of the respective operator to apply the necessary security updates. The procedure depends on the deployed architecture and product version.

**Important Note on Risk Mitigation for CodeMeter License Central:**

Operating CodeMeter License Central behind a **reverse proxy with client certificate authentication (mTLS)** significantly minimizes the attack surface, as unauthenticated requests are rejected before reaching the PHP components.

#### Version Overview (Continuously Updated)

| Product / Component | Architecture / Base | Remediation Strategy / Action | Status / Availability | 
|---|---|---|---|
| **CodeMeter License Central 5.2** | Containerized (Docker / Kubernetes) | Update to version **5.2.3** (in addition to the PHP security update and the changes listed in the Release Notes, this automatically applies the post-update configuration recommendations to the frontend image described in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273); if remaining on **5.2.2**, manual adjustment of `php.ini` according to the manual is strongly recommended). | **5.2.3 available** (as well as 5.2.2; download from registry; [updated Manual on website](https://www.wibu.com/support/developer/software-downloads.html#download-273); *Updated 2026-10-29, 5:00 pm CET*) | 
| **CodeMeter License Central 5.1** | Containerized (Docker / Kubernetes) | Run the new version of the [**“PHP-Patch Update Installer”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) (pulls the new container images for version **5.1.2** and additionally applies the post-update configuration recommendations to the frontend image as described in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273); can be re-run if the previous installer was already executed). **Alternatively:** Seamless upgrade to **5.2.3** using the new update installer. | **5.1.2 / 5.2.3 available** ([updated Installer & Manual on website](https://www.wibu.com/support/developer/software-downloads.html#download-273); *Updated 2026-10-29, 5:00 pm CET*) | 
| **CodeMeter License Central 5.0** | Containerized (Docker) | Run the new version of the [**“PHP-Patch Update Installer”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) for version **5.0.1** (additionally applies the post-update configuration recommendations to the frontend image as described in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273); can be re-run if the previous installer was already executed). **Alternatively:** Seamless upgrade to **5.2.3** using the new update installer *(starting with version 5.1, a separate license is required)*. | **5.0.1 / 5.2.3 available** ([updated Installer & Manual on website](https://www.wibu.com/support/developer/software-downloads.html#download-273); *Updated 2026-10-29, 5:00 pm CET*) | 
| **CodeMeter License Central 4.x** | Classic VM Installation (Ubuntu) – *Internet & Desktop Edition* | 1. Operating system patches via paid **Ubuntu Pro Support (ESM)** plus **strongly recommended** adjustment of `php.ini`, restart, and verification according to the updated [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273). 2. **Alternatively:** Upgrade / migration to CodeMeter License Central **5.0 / 5.2** *(starting with version 5.1, a separate license via Sales is required)*. | **Approved & Released** (Ubuntu Pro successfully tested and released; [updated Manual on website](https://www.wibu.com/support/developer/software-downloads.html#download-273); *Updated 2026-10-27, 6:00 pm CET*) | 
| **Extensions – Containerized / Packages** (WebDepot, CodeMeter License Portal) | Containerized / Download | Provision of patched versions **WebDepot 24.09g** and **CodeMeter License Portal 25.09a and 26.09a**. | **Available now** (on the Wibu-Systems website; CodeMeter License Portal versions are also available via **Harbor**) | 
| **Extensions – ZIP Package** (Self-hosted on custom server) | Custom web server / PHP runtime environment | Update to a patched PHP version (or WebDepot 24.09g / License Portal 25.09a, 26.09a). Optional upgrade to **PHP 8.2 to 8.4** (Note: **PHP 8.5 is not supported**). Custom extensions must be verified for compatibility. | To be performed by the operator | 

### 3. Detailed Information by Version

#### CodeMeter License Central (General Mitigation & Updated Tools)

- **Minimizing the Attack Surface:** Operating CodeMeter License Central behind a reverse proxy with enabled client certificate verification significantly reduces the attack surface. We strongly recommend using this protection mechanism.
- **Strongly Recommended `php.ini` Hardening (Automated in 5.2.3 and New Update Installer):** We **strongly recommend** applying the `php.ini` configuration (including `session.upload_progress.enabled=0`) described in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) across all installations. In line with a recent [PHP project advisory](https://www.php.net/archive/2026.php#2026-10-23-1), this fully rules out an unlikely residual attack vector (CVE-2026-115560) until the next regular PHP bugfix release and also serves as a restrictive configuration to make exploiting future vulnerabilities more difficult. When updating to **CodeMeter License Central 5.2.3** or using the new version of the [**“PHP-Patch Update Installer”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) (available since 2026-10-28, 5:30 pm CET for 5.0.x and 5.1.x), these post-update configuration recommendations on the CodeMeter License Central frontend image are applied **automatically**.
- **Updated [“PHP Patch Manual”](https://www.wibu.com/support/developer/software-downloads.html#download-273):** The manual includes dedicated chapters for each deployed CodeMeter License Central version (**5.2, 5.1, 5.0, and 4.x**) with detailed step-by-step instructions, the recommended restart, and the specific information operators can use afterwards to verify whether the patch was applied successfully.

#### CodeMeter License Central 5.2 (Updated 2026-10-29, 5:00 pm CET)

- **Target Version: 5.2.3** (or at least **5.2.2**)
- **Status: Available** for download from the registry (updated [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) on the website).
- **Procedure:** We have released **CodeMeter License Central 5.2.3**. For users of CodeMeter License Central 5.2.x, updating to 5.2.3—in addition to the changes mentioned in the Release Notes—automatically applies the post-update configuration recommendations to the CodeMeter License Central frontend image as described in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273). If you are running version **5.2.2** and do not yet update to 5.2.3, we strongly recommend manually applying the `php.ini` hardening, performing the recommended restart, and verifying the patch as described in the “PHP Patch Manual”.

#### CodeMeter License Central 5.1 (Updated 2026-10-29, 5:00 pm CET)

- **Target Version: 5.1.2** (or direct upgrade to **5.2.3**)
- **Status: Available** via the new version of the [**“PHP-Patch Update Installer”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) (since 2026-10-28, 5:30 pm CET) and the updated [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) on the website.
- **Procedure:**
  - **Patch to 5.1.2 Including Automated Frontend Configuration:** A new version of the [**“PHP-Patch Update Installer”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) has been available since 2026-10-28, 5:30 pm CET. This version works just like the previous one (pulling the new container images for 5.1.2), but additionally applies the post-update configuration recommendations to the CodeMeter License Central frontend image as described in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273). **Note:** If you have already run the previous version of the installer, you can simply run the new installer again to obtain the configuration changes.
  - **Seamless Upgrade to 5.2.3:** In addition, the new update installer enables a seamless upgrade of an existing CodeMeter License Central 5.1.x installation directly to version **5.2.3** to keep deployed systems as up to date as possible.

#### CodeMeter License Central 5.0 (Updated 2026-10-29, 5:00 pm CET)

- **Target Version: 5.0.1** (or direct upgrade to **5.2.3**)
- **Status: Available** via the new version of the [**“PHP-Patch Update Installer”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) (since 2026-10-28, 5:30 pm CET) and the updated [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) on the website.
- **Procedure:**
  - **Patch to 5.0.1 Including Automated Frontend Configuration:** A new version of the [**“PHP-Patch Update Installer”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) has been available since 2026-10-28, 5:30 pm CET. This version works just like the previous one, but additionally applies the post-update configuration recommendations to the CodeMeter License Central frontend image as described in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273). **Note:** If you have already run the previous version of the installer, you can run the new installer a second time to obtain the configuration changes.
  - **Seamless Upgrade to 5.2.3:** Furthermore, the new update installer enables a seamless upgrade of an existing CodeMeter License Central 5.0.x installation to version **5.2.3** to keep existing installations as up to date as possible *(Note: Starting with version 5.1, a separate license is required for operation, which can be obtained through our sales team at [sales(at)wibu.com](mailto:sales@wibu.com))*.

#### CodeMeter License Central 4.x (VM Environments: Internet Edition & Desktop Edition – Updated 2026-10-27, 6:00 pm CET)

- **Status: Approved & Released** (Ubuntu Pro successfully tested and released; updated [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) with dedicated 4.x chapter available).
- **Risk Assessment – Desktop Edition vs. Internet Edition:** CodeMeter License Central 4.x was offered as an *Internet Edition* and a *Desktop Edition*. Because the **Desktop Edition** must not be connected to the internet when operated as intended, it is only exposed to potential attacks originating from within the internal corporate network. Nevertheless, we recommend updating or migrating internally operated systems promptly.
- **Procedure:** Operators of classic 4.x VM installations have two approved options:
  - **Option 1 – Operating System Patch via Ubuntu Pro (Approved & Released) & Strongly Recommended `php.ini` Hardening:** Because standard support for the underlying older Ubuntu version has expired, PHP security updates are provided by the OS vendor through the paid **Ubuntu Pro Support (Expanded Security Maintenance / ESM)** program. Wibu-Systems has successfully tested and officially approved Ubuntu Pro for CodeMeter License Central 4.x on-premises installations. In addition, we **strongly recommend** applying the `php.ini` hardening to fully rule out any residual attack vector and make the exploitation of future vulnerabilities more difficult. The updated [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) available on our website includes a dedicated chapter for 4.x versions with detailed step-by-step instructions, the recommended restart, and the criteria you can use afterwards to verify whether the patch was successful.
  - **Option 2 – Upgrade to Version 5.0 / 5.2:** Alternatively, you can upgrade or migrate your installation to the newer, containerized technology of CodeMeter License Central (**5.0 / 5.2**). **Important Licensing Note:** Starting with version **5.1** (including 5.2), a separate license is required for operation, which can be obtained through our sales team ([sales(at)wibu.com](mailto:sales@wibu.com)).

#### CodeMeter License Central Extensions (On-Premises)

- **Available Updates (Website & Harbor):**
  - **WebDepot 24.09g** as well as **CodeMeter License Portal 25.09a and 26.09a** are now available on the Wibu-Systems website.
  - The updated versions of **CodeMeter License Portal (25.09a and 26.09a)** are also available via **Harbor**.
- **Extensions as ZIP Archive (Operated on a Custom Server):**
  - **PHP Security Update:** Update the PHP installation on your server to a version in which CVE-2026-109618 and CVE-2026-109619 are resolved, and apply the `php.ini` hardening recommended in the [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273).
  - **Supported PHP Versions:** Optionally, you can upgrade to **PHP 8.2 through 8.4** as part of this maintenance.
  - **Important Restriction:** CodeMeter License Central Extensions are **not compatible with PHP 8.5** and will not run on PHP 8.5.
  - **Compatibility Verification:** If you have implemented custom extensions or modifications, you must verify their compatibility with your target PHP version prior to rollout.

### 4. Frequently Asked Questions (FAQ)

#### General & WOPS Operations

**Q: (Updated 2026-10-27, 9:30 am CET) My CodeMeter License Central is hosted by Wibu-Systems (WOPS). Do I need to take any action?**

A: No. Our Wibu Operating Services (WOPS) department has completed the updates for both the primary infrastructure systems—including all provided standard Gateways and WebDepots without customer-specific customizations—and all downstream systems and containers. All hosted **5.x** systems as well as all automatically patchable **4.x** systems have been updated; in individual cases, customers have been contacted directly for clarification.

**Q: Will the maintenance work performed by WOPS cause any downtime for my hosted systems?**

A: In many cases, applying the updates will cause **no interruptions at all**. Where a brief interruption does occur, it typically lasts only around 5 minutes (and up to a maximum of 30 minutes). For organizational reasons, any such short maintenance windows cannot be announced or scheduled in advance.

**Q: We use a customized WebDepot or Gateway hosted by WOPS. Will these systems be updated as well?**

A: Yes. Customer-specific customizations are automatically included in the update process by WOPS. If any coordination or clarification is needed in your specific case, WOPS will contact you directly.

**Q: Which components of CodeMeter License Central are specifically affected?**

A: Only server-side components that use PHP are affected: the CodeMeter License Central web interface and the PHP-based extensions (CodeMeter License Central Extensions: WebDepot, Gateways, Portal, and Connectors).

**Q: Are the CodeMeter Runtime or WibuKey installed on end-user computers also affected by these vulnerabilities?**

A: No. Neither CodeMeter Runtime nor WibuKey contain any PHP components, and neither is affected by CVE-2026-109618 or CVE-2026-109619. Therefore, no updates to CodeMeter Runtime or WibuKey are required for your end users in connection with this advisory.

#### On-Premises Operations (Self-Hosted)

**Q: How can I minimize the attack surface of my CodeMeter License Central installation immediately and in general?**

A: Operating CodeMeter License Central behind a reverse proxy with client certificate authentication (mTLS) significantly reduces the attack surface, ensuring that only authenticated peers can reach the web interface or endpoints.

**Q: We operate the Extensions (e.g., WebDepot or Gateways) on our own web server using the provided ZIP package. What do we need to consider?**

A: Apply the latest PHP security update provided by your operating system or distribution vendor. Optionally, you can update to **PHP 8.2 through 8.4**. Please note the following mandatory requirements:

1. The Extensions **do not run on PHP 8.5**.
2. Any custom extensions or modifications must be tested for compatibility with the new PHP version beforehand.

**Q: Which updated versions are available for WebDepot and CodeMeter License Portal, and where can I get them?**

A: **WebDepot 24.09g** as well as **CodeMeter License Portal 25.09a and 26.09a** are now available on the Wibu-Systems website. In addition, the CodeMeter License Portal versions (25.09a and 26.09a) are available via **Harbor**.

**Q: (Updated 2026-10-29, 5:00 pm CET) We run CodeMeter License Central 5.x in our own on-premises environment. When and how do we receive the fixes?**

A: Fixes and version-specific step-by-step instructions in the updated [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) are available for all 5.x version lines:

- **Version 5.2 (5.2.3 or 5.2.2):** The newly released version **5.2.3** is available in the Wibu Registry and, in addition to the changes listed in the Release Notes, automatically applies the post-update configuration recommendations to the CodeMeter License Central frontend image described in the “PHP Patch Manual”. (If you remain on version 5.2.2, we strongly recommend manually applying the `php.ini` hardening described in the “PHP Patch Manual”.)
- **Version 5.1 (5.1.2) and 5.0 (5.0.1):** Since 2026-10-28, 5:30 pm CET, a new version of the [**“PHP-Patch Update Installer”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) has been available for download on the Wibu-Systems website together with the updated [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273). This version pulls the new container images and additionally applies the post-update configuration recommendations to the frontend image described in the “PHP Patch Manual”. If you have already run the previous version of the installer, you can simply run the new installer again to obtain the configuration changes. Furthermore, the new update installer enables a seamless upgrade of an existing CodeMeter License Central 5.0.x or 5.1.x installation directly to version **5.2.3** *(Note: Starting with version 5.1, a separate license is required)*.

**Q: (Updated 2026-10-27, 6:00 pm CET) We still operate CodeMeter License Central 4.x as a virtual machine (VM). Why is Ubuntu Pro required, and what is the current approval status?**

A: Version 4.x VM installations are based on an older Ubuntu version for which regular standard support by Canonical has ended. Security updates for PHP on these versions are delivered by the OS vendor exclusively through the paid *Ubuntu Pro* (Expanded Security Maintenance) program. Wibu-Systems has successfully tested and officially **approved and released** the Ubuntu Pro updates for CodeMeter License Central 4.x (On-Premises). In addition, we **strongly recommend** applying the `php.ini` hardening. The updated [**“PHP Patch Manual”**](https://www.wibu.com/support/developer/software-downloads.html#download-273) includes a dedicated chapter for 4.x versions with step-by-step instructions, the recommended restart, and the criteria to identify afterwards whether the patch was successful. Alternatively, we recommend upgrading or migrating to the containerized technology of CodeMeter License Central (5.0 / 5.2). Please note that upgrading to version 5.1 or 5.2 requires a separate license, which can be obtained through our sales team.

**Q: We use the CodeMeter License Central 4.x Desktop Edition. What is the risk level for this edition?**

A: By design, the 4.x Desktop Edition must not be accessible from the internet. Provided this requirement is met, the system cannot be attacked externally and is only exposed to potential attacks from within the internal corporate network. While this lowers the immediate risk compared to an Internet Edition, we still recommend updating the system using the now-approved Ubuntu Pro patches (including the strongly recommended `php.ini` hardening described in the “PHP Patch Manual”) or migrating to a current version.

**Q: Who can I contact if I need assistance updating my on-premises installation?**

A: If you have any questions or require assistance, please contact our support team at [support(at)wibu.com](mailto:support@wibu.com).

## Archive

*Last updated on: 2026-02-11 4:00 pm CET (Adjustment regarding KB5077181)*

Windows update KB5074105 and KB5077181 modify multiple Windows components, rendering a mechanism used by AxProtector for Windows to obfuscate certain function calls incompatible.

Under specific protection configurations, protected applications may fail during startup or operation.

Below you will find answers to frequently asked questions for both end users of protected software and developers providing protected applications. If your question is not covered here, please contact our [technical support](https://www.wibu.com/support/customer.html) team.

## Frequently Asked Questions

**Q: My purchased, licensed software hasn't worked correctly since the last Windows update. What can I do?**

**A:** First, check whether either of the Windows updates KB5074105 or KB5077181 is installed on your system. If so, contact the software vendor or check whether an updated version is available that is compatible with these Windows updates.

**Q: My purchased software has not worked correctly since the last Windows update, but I urgently need to use it. What else can I do?**

**A:** You will need to wait for an updated version from the software vendor. At present, there is no general workaround – no system or application setting can bypass this issue.

**Q: My purchased software still runs on a Windows 10 system. Does the error occur there too?**

**A:** Both Windows updates apply only to Windows 11. Older operating systems don't receive these changes, so no error occurs, and no action is needed.

## Frequently Asked Questions for Software Manufacturers Protecting Apps with AxProtector Windows (up to and including Version 11.70c)

**Q: *(New 2026-02-11)* The initial information referred only to KB5074105, and later also to KB5077181. What is the difference between them?**

**A:** Microsoft first released the optional update KB5074105, in which the incompatibility was initially identified. On February 10, 2026, Microsoft then released the security update KB5077181, which includes update KB5074105. With regard to the incompatibility, both updates have the same impact. The available remediation options are identical.

**Issue Diagnosis**

**Q: How can I determine if my software is affected?**

**A:** To be certain, test your software thoroughly. Install Windows Update KB5077181 on a Windows 11 system, launch your software, and test functionality. If it crashes, you're likely affected.

**Q:** *(New 2026-02-09)* My software consists of .NET assemblies and runs on Windows. Is my software affected as well?

**A:** As a rule, .NET assemblies are protected with AxProtector .NET. This product uses a different technical approach, and such applications are therefore typically not affected. In some cases, however, individual .NET assemblies may additionally have been protected with AxProtector Windows. As a precaution, you should verify whether your protection configuration uses AxProtector Windows (axprotector.exe) for .NET assemblies and test your application on Windows 11 with Windows update KB5077181installed.

For distinction:

AxProtector Windows (axprotector.exe) uses wbc files (*.wbc) for configuration; AxProtector .NET (axprotectornet.exe) uses XML files (*.xml) for configuration or, in newer versions, \*WibuCpsConf.

**Q: *(New 2026-02-09)* My software was encrypted with AxProtector NC or AxProtector CTP. Is my software also affected?**

**A:** No, software that was encrypted with AxProtector NC or CTP is not affected.

**Q: I've found protection options in a wbc file or log file. How can I check if my software is affected?**

**A:** Look for the -caa option in the file. The number that follows represents the sum of *Advanced Protection Schemes* (1, 2, 4, 8). Methods with the value 2 and 8 may trigger the issue. If the value is -caa1, -caa4, or -caa5, your software is unaffected by this compatibility issue.

**Q: Based on the Advanced Protection Methods value, my software is affected. But tests with KB5074105 or KB5077181 installed work fine. Is that possible?**

**A:** The compatibility issue doesn't occur in every case. Wibu-Systems investigations show it only happens if your protected component's (EXE or DLL) import table includes Microsoft APIs identifiable by module names starting with "api-ms," e.g., api-ms-win-crt-runtime.dll.

**Q: The encryption log shows "Warning: Static code modification does not have any effect to the current executable!". Does this mean no compatibility issue?**

**A:** Unfortunately not. This output from the encryption process wasn't reliable; it indicates modification couldn't be applied to certain functions, but doesn't guarantee it wasn't applied at all.

**Problem Resolution**

**Q: *(Updated 2026-02-09)* My software is affected by the KB5074105/KB5077181 compatibility issue. What can I do to provide users with a working app again?**

**A:** There are currently two options:

1. Repair the protected files (recommended): Please refer to the detailed instructions below.

2. Re-encrypt the original source file.

Re-encrypt your software using the same AxProtector version as the original release to avoid side effects from other changes. Key difference: Use a -caa value excluding 2 and 8, e.g., -caa5. In the AxProtector GUI, uncheck *Static Code Modification*. Test the new version and distribute it.

If you already used AxProtector 11.70 or later, switch to 11.70d (in CodeMeter SDK 8.40d), which supports *Static Code Modification* and *Extended Static Modification* without issues.

**Q: Why doesn't Wibu-Systems provide a new CodeMeter Runtime version to fix this?**

**A:** It's not technically feasible. Changes to loading Microsoft API functions are deeply embedded in the protected app, unrelated to CodeMeter Runtime and unfixable from within the app.

**Q: Is there really no way to make the protected software work at the user end without a new version?**

**A:** Since KB5077181 is a security update, uninst   alling it is generally not recommended. Users may, at their own risk, delay installing the security update for a limited period. It can be assumed that future security updates will either require KB5077181 or incorporate the same incompatibility.

*(New 2026-02-09)* Using the AxRepairKB5074105 Repair Tool

**Q: How does the AxRepairKB5074105 tool work?**

**A:** The AxRepairKB5074105 tool modifies a section of code located outside the protected areas of the binary so that the problematic code path is no longer executed. The protection of the application remains intact. This achieves the same result as re-encrypting with the current AxProtector version 11.70d.

**Q: What other effects does using the AxRepairKB5074105 tool have?**

**A:** Because the application is modified, the Authenticode signature typically used to sign the application becomes invalid. After applying the repair, you must reapply the Authenticode signature.

**Q: *(New 2026-02-11)* Is the AxRepairKB5074105 tool also applicable to Windows update KB5077181?**

**A:** KB5077181 incorporates KB5074105. In terms of the compatibility issue, it is therefore irrelevant which of the two Windows updates is installed. The same applies to remediation using AxRepairKB5074105. An application repaired with AxRepairKB5074105 will operate on Windows 11 with either KB5074105 or KB5077181 installed. This is expected to apply to future security updates as well.

**Q: How exactly is the AxRepairKB5074105 tool used?**

**A:** AxRepairKB5074105 has a single parameter: the file name of the EXE or DLL to be repaired. First, the tool checks whether it can repair the specified file. If this is the case, you are asked whether the repair should be performed. If you answer with “y”es, a backup copy is created in the same folder with the extension .wibu\_bak, and the file is modified in place.

**Q: Can multiple files be repaired at once?**

**A:** If you specify a directory instead of a single file name as the argument, all EXEs and DLLs in that directory will be checked, and – after confirmation – the files for which the repair is applicable will be backed up and repaired.

**Q:  Can the tool also be run without explicit confirmation?**

**A:** You can preempt the confirmation with an appropriate call. For example:

echo y | AxRepairKB5074105.exe "C:\Program Files\MyTool\ "

**Q: How do my users receive the repaired files?**

**A:** Before distribution, you should reapply the Microsoft Authenticode signature to the files. You can then distribute them using your usual update mechanisms, for example via newly generated installation packages.

**Q: Where can I find the AxRepairKB5074105 tool?**

**A:** The AxRepairKB5074105 tool is available for software developers in the [developer download area](https://www.wibu.com/support/developer/software-downloads.html#AxProtector_Developer_Download) under “AxProtector Windows”. Please log in using your existing credentials.

**Miscellaneous**

**Q: How will Wibu-Systems prevent this in the future?**

**A:** The AxProtectors within the CodeMeter Protection Suite are being gradually transitioned to new technology. NC variants minimize modifications to the binary file and shift API calls, licensing, and security checks to the CodeMeter Protection Suite Runtime (CPSRT), a library that is part of CodeMeter Runtime or can be distributed separately. This allows certain system incompatibilities to be resolved in the future through CPSRT updates. It also facilitates the replacement of third-party libraries following security incidents (CVEs) and supports compliance with the Cyber Resilience Act (CRA). The NC variant of AxProtector Windows will be released in Q2 2026 with version 11.80 (CodeMeter SDK 9.00).
