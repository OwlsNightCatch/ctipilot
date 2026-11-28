---
title: NGINX2ROOT Impact Statement
url: https://www.veeam.com/kb4976?ck=1700057206377
hostname: veeam.com
description: Five nginx vulnerabilities known as nginx2root affect Veeam Software Appliance, Veeam Infrastructure Appliance, and other Veeam components. This article lists the affected products and the mitigation for each.
sitename: Veeam Software
date: "2026-11-20"
categories: ['Veeam Knowledge Base']
fingerprint: "6aa704bd7d4b960"
language: en
image: https://www.veeam.com/content/dam/veeam/en/public/images/og-images/meta_banner_kb.png?ck=1700057206377
pagetype: website
filedate: "2026-11-28"
---
# NGINX2ROOT Impact Statement

| KB ID: | 4976 | 
| Product: | Veeam Backup & Replication Veeam Software Appliance Veeam Data Cloud *for AWS* Veeam Data Cloud *for Salesforce* Veeam Data Cloud *for Microsoft Azure* Veeam Backup *for Salesforce* Veeam Plug-In *for AWS* Veeam Plug-In for *Microsoft Azure* Veeam Plug-In *for Google Cloud* | 
| Published: | 2026-11-20 | 
| Last Modified: | 2026-11-25 | 

Veeam is investigating these vulnerabilities and will update this article as new information becomes available.

## Summary

nginx2root is the common name for five memory corruption vulnerabilities in nginx: CVE-2026-123007, CVE-2026-123633, CVE-2026-121810, CVE-2026-123634, and CVE-2026-113425. They affect the HTTP/2 module, the HTTP/3 module, the DNS resolver, and the mail proxy, and can be triggered remotely. Combined with a Linux kernel vulnerability, they can lead to root access.

Windows-based installations of Veeam Backup & Replication and Veeam Backup Enterprise Manager do not use nginx and are not affected. Veeam Software Appliance and Veeam Infrastructure Appliance include nginx and are listed in the following table.

Whether a Veeam component is affected depends on the nginx build it includes and the nginx features its configuration enables. The following table lists the status and the required action for each product.

| **Product** | **Affected** | **Notes** | 
| Veeam Software Appliance 13.1 | Yes | Affected by CVE-2026-123007 and CVE-2026-123633. [Install the latest security updates through Veeam Updater](https://www.veeam.com/kb4976#appliances). | 
| Windows-based Veeam Backup & Replication 13.1 | No | nginx is not used. | 
| Veeam Backup Enterprise Manager 13.1 on Linux | No | HTTP/2 is not enabled. | 
| Veeam Backup Enterprise Manager 13.1 on Windows | No | nginx is not used. | 
| Workers deployed by Veeam Plug-Ins for hypervisors | No | The affected nginx features are not used. | 
| Veeam Infrastructure Appliance 13.1 | Yes | Affected by CVE-2026-123007 and CVE-2026-123633. [Install the latest security updates through Veeam Updater](https://www.veeam.com/kb4976#appliances). | 
| Veeam Plug-In *for AWS*, Veeam Plug-In *for Google Cloud*, and Veeam Plug-In for *Microsoft Azure* appliances | Yes | [Install all available security updates through Veeam Updater](https://www.veeam.com/kb4976#cloud). | 
| Veeam Data Cloud *for Salesforce*, Veeam Data Cloud *for Microsoft Azure*, and Veeam Data Cloud *for AWS* | Yes | Veeam manages these services. [No customer action required](https://www.veeam.com/kb4976#vdc). | 
| Veeam Backup *for Salesforce* 3.2.1 | Yes | Affected by CVE-2026-123007 and CVE-2026-123633. [Install the operating system vendor update or disable HTTP/2](https://www.veeam.com/kb4976#vbsf). | 

## Solution

#### **Veeam Software Appliance and Veeam Infrastructure Appliance**

Veeam Software Appliance and Veeam Infrastructure Appliance 13.1 include an nginx build with HTTP/2 enabled on a listener that proxies requests to a backend, so CVE-2026-123007 and CVE-2026-123633 apply. The remaining vulnerabilities do not apply to the appliance configuration.

Since November 25, 2026, an update that contains the fix has been available in the Veeam repository for Veeam Software Appliance and Veeam Infrastructure Appliance 13.1 (). To remediate the vulnerabilities, install the latest security updates through **nginx-1.20.1-22.8.el9\_6\_ciq.3**[Veeam Updater](https://helpcenter.veeam.com/docs/vbr/userguide/update_appliance_check_updates.html?ver=13).

Veeam Updater checks the repository every 12 hours. With the default update configuration, mandatory updates are installed automatically on the nearest Sunday at 14:00, based on the time zone of the backup server. If the update does not appear on the **Updates** tab, it may already be installed. To confirm, check the **History** tab in the Veeam Host Management console. For details, see [Veeam Backup & Replication User Guide: Viewing Update History](https://helpcenter.veeam.com/docs/vbr/userguide/update_appliance_view_history.html).

Appliances that use a local mirror of the Veeam repository receive the update after the mirror is synchronized.

To install the update without waiting for automatic installation, perform the following steps:

1. [Log in to the Veeam Host Management console](https://helpcenter.veeam.com/docs/vbr/userguide/hmc_access.html) on the backup server.
2. In the management pane, click **Updates** > **Check for updates**.
3. On the **Updates** tab, select the available updates, then click **Install Updates Now** and confirm the operation.
4. If a backup infrastructure component uses a custom update configuration, repeat these steps in the Veeam Host Management console of that component.

Until the update is installed, restrict access to TCP port 443 on the appliances to trusted networks. HTTP/2 cannot be disabled on these appliances because Veeam components depend on it.

For more information, see [Veeam Backup & Replication User Guide: Configuring Updates](https://helpcenter.veeam.com/docs/vbr/userguide/update_appliance_configure_updates.html) and [Installing Updates](https://helpcenter.veeam.com/docs/vbr/userguide/update_appliance_install_updates.html).

#### **Public Cloud Appliances**

The Veeam Plug-In *for AWS*, Veeam Plug-In *for Google Cloud*, and Veeam Plug-In for *Microsoft Azure* appliances run Ubuntu 22.04 LTS and use the nginx package provided by Ubuntu. The patched nginx package () is installed with the security updates offered through **1.18.0-6ubuntu14.23**[Veeam Updater](https://helpcenter.veeam.com/docs/vbr/userguide/aws_updates_check.html). Worker instances do not include nginx and are not affected.

To remediate the vulnerabilities, install all available security updates through Veeam Updater.

#### **Veeam Data Cloud**

Veeam manages the infrastructure of Veeam Data Cloud *for Salesforce*, Veeam Data Cloud *for Microsoft Azure*, and Veeam Data Cloud *for AWS*, and is responsible for applying security updates to these services. No customer action is required.

#### **Veeam Backup *for Salesforce***

Veeam Backup *for Salesforce* 3.2.1 uses the nginx package provided by the operating system of the server where it is installed, and generates the nginx configuration. That configuration enables HTTP/2 on a listener that proxies requests to a backend, so CVE-2026-123007 and CVE-2026-123633 apply. The remaining vulnerabilities do not apply to this configuration.

Veeam does not manage the operating system or the nginx package on customer-deployed Veeam Backup *for Salesforce* servers. Customers managing these servers are advised to review the advisory from the operating system vendor and install the nginx update when it is available.

Until the nginx update is installed, HTTP/2 can be disabled to remediate the vulnerabilities:

1. On the Veeam Backup *for Salesforce* server, open the following file: /etc/nginx/sites-available/vbsf-frontend.conf
2. Remove the **http2**
parameter from the **listen**
directive for port 443. Change: listen 443 ssl http2; to: listen 443 ssl;
3. Save the file, then check the nginx configuration and restart the nginx service:

If this KB article did not resolve your issue or you need further assistance with Veeam software, please create a [Veeam Support Case.](https://www.veeam.com/kb1771)

To submit feedback regarding this article, please click this link: [Send Article Feedback](https://www.veeam.com/kb4976?ad=in-text-link#kb_request_form)
 

To report a typo on this page, highlight the typo with your mouse and press CTRL + Enter.
