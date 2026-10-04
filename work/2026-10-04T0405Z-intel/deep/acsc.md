---
title: Critical vulnerabilities in Citrix NetScaler ADC and Citrix NetScaler Gateway products
author: The Australian Government; Canberra
url: https://www.cyber.gov.au/about-us/view-all-content/alerts-and-advisories/critical-vulnerabilities-in-citrix-netscaler-adc-and-citrix-netscaler-gateway-products
hostname: cyber.gov.au
description: Alert for organisations to implement a high-priority patch addressing new vulnerabilities, under active exploitation in Citrix NetScaler ADC and Citrix NetScaler Gateway products.
sitename: Cyber.gov.au
date: "2026-09-28"
---
This alert is relevant to all Australian organisations who operate Citrix NetScaler ADC and Citrix NetScaler Gateway products.

## Update 3 October 2026

Citrix has published guidance about a newly identified issue affecting NetScaler ADC and NetScaler Gateway deployments that use SAML authentication.

A remote attacker exploiting the issue may induce system crashes, denial of service and potential exploitation.

ASD’s ACSC is aware of impacts to Australian organisations.

Organisations using NetScaler SAML authentication should review their configurations, monitor for unusual activity, and follow [Citrix advice](https://community.citrix.com/techzone-blogs/110_security-updates/security-update-guidance-for-netscaler-saml-authentication-deployments/).

Organisations impacted by this issue are also encouraged to contact Citrix support and report to ASD’s ACSC.

This issue is understood to be separate from the vulnerabilities outlined below [CVE-2026-88771 and CVE-2026-88772].

## Update 30 September 2026

Since publishing the alert on 28 September 2026, the Australian Signals Directorate's Australian Cyber Security Centre (ASD’s ACSC) has received reports from Australian organisations confirming exploitation. ASD's ACSC recommends reviewing for evidence of compromise since at least 4 September 2026. Citrix has made indicators of compromise available through NetScaler Console and published additional guidance in their recent publication, Security Bulletin for CVE-2026-88771 through CVE-2026-88778.

## Background

Citrix has released [8 new vulnerabilities](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096&articleURL=Citrix_NetScaler_ADC_and_Citrix_NetScaler_Gateway_Security_Bulletin_for_CVE_2026_88771_CVE_2026_88772_CVE_2026_88773_CVE_2026_88774_CVE_2026_88775_CVE_2026_88776_CVE_2026_88777_and_CVE_2026_88778) in Citrix NetScaler ADC and Citrix NetScaler Gateway products.

ASD's ACSC understands that at least 2 of these vulnerabilities (CVE-2026-88771 and CVE-2026-88772) have been under active exploitation globally prior to a patch becoming available. ASD’s ACSC has not yet received reports of confirmed exploitation in Australia.

CVE-2026-88771 is a Remote Code Execution vulnerability, which can allow an unauthenticated attacker to execute arbitrary commands. All configurations of Citrix NetScaler ADC and Citrix NetScaler Gateway are affected and are vulnerable to exploitation against this CVE.

The remaining 7 vulnerabilities require certain configurations to be in place for the device to be vulnerable to exploitation. Citrix has provided instructions for customers to check to see if their device is vulnerable to each of the other 7 CVEs.

## Mitigation advice

ASD's ACSC recommends that organisations operating vulnerable Citrix products, review details of the [vulnerabilities released by the vendor](https://support.citrix.com/support-home/kbsearch/article?articleNumber=CTX697096&articleURL=Citrix_NetScaler_ADC_and_Citrix_NetScaler_Gateway_Security_Bulletin_for_CVE_2026_88771_CVE_2026_88772_CVE_2026_88773_CVE_2026_88774_CVE_2026_88775_CVE_2026_88776_CVE_2026_88777_and_CVE_2026_88778) and install the security update.

Organisations should consider internal security assessments and business plans, in determining how to effectively prioritise the implementation of this security update.

In addition to applying the security update, organisations should review the pre-condition requirements for each of the CVEs to understand where they may have been vulnerable to exploitation.

ASD's ACSC recommends reviewing device logging for any suspicious activity, which is consistent with the kinds of attacks enabled by each of the CVE’s where the pre-conditions for exploitation have been met.

## Where to get help

Organisations that have been impacted, suspect impact or require advice and assistance can contact us via [1300 CYBER1 (1300 292 371)](<tel:1300 292 371>)
