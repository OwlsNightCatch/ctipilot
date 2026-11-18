---
title: "COLD RELIC: A Case Study in Impersonation and Compromise | Google Cloud Blog"
author: Google Threat Intelligence Group; Mandiant
url: https://cloud.google.com/blog/topics/threat-intelligence/cold-relic-a-case-study-in-impersonation-and-compromise
hostname: google.com
description: In 2026, Mandiant and GTIG linked a Russia-nexus cyber espionage group, COLD RELIC, to a US organizational compromise, discovering that data stolen in 2025 facilitated the attack.
sitename: Google Cloud Blog
date: "2026-11-17"
tags: ['Threat Intelligence']
fingerprint: "350b8df10137e5e1"
---
# COLD RELIC: A Case Study in Impersonation and Compromise

##### Google Threat Intelligence Group

##### Mandiant

##### Google Threat Intelligence

Visibility and context on the threats that matter most.

[Contact Us & Get a Demo](https://cloud.google.com/security/resources/google-threat-intelligence-demo?utm_source=cgc-blog&utm_medium=blog&utm_campaign=FY25-Q2-global-GCP30649-website-su-dgcsm-GTI-interest)

Written by: Josh Murchie, John Wolfram, Joseph Spero, Peter Ukhanov, Fernando Tomlinson, Jr., Wesley Shields

### Introduction 

Over the past year, Mandiant has responded to a series of linked intrusions demonstrating how Russian cyber espionage group COLD RELIC (formerly tracked as COLDRIVER and UNC4057; also known as Star Blizzard, Callisto, and Gossamer Bear) turns a single cloud compromise into a springboard for ongoing third party compromise and espionage. Most recently, Mandiant investigated a 2026 compromise at a US-based organization where COLD RELIC directly weaponized data, the corporate staff directory, and identities stolen during a late-2025 compromise, which Mandiant also investigated, at a separate US-based organization.

COLD RELIC is a Russian state-sponsored threat group that the [US Department of Justice (DOJ) has assessed](https://www.justice.gov/archives/opa/pr/justice-department-disrupts-russian-intelligence-spear-phishing-efforts) operates within Russia's Federal Security Service (FSB). The group is known for implementing sophisticated phishing and malware campaigns with the aim to gain access to information of strategic or political relevance to the Russian government, as well as to leverage compromised access to target compromised individuals’ broader social and professional networks. Once COLD RELIC compromises a target, it uses stolen emails and data to establish authentic pretexts and impersonate contacts when reaching out to subsequent targets. While COLD RELIC has largely maintained a low profile, yielding minimal public reporting relative to other Russia-nexus threat actors, it has been highly successful at compromising high-value targets (including government officials, defense contractors, and non-governmental organizations (NGOs) across Europe and North America) while maintaining a consistent operational tempo.

While Google Threat Intelligence Group (GTIG) has [tracked and disrupted](https://blog.google/threat-analysis-group/google-tag-coldriver-russian-phishing-malware) COLD RELIC phishing campaigns since 2015, recent Mandiant incident response investigations have uncovered critical new insights into the group’s social engineering and post-compromise tradecraft. We are sharing this end-to-end analysis—along with actionable detection and hardening guidance—to help organizations defend against COLD RELIC’s ongoing use of stolen pretexts, localized residential proxies, and cross-cloud identity abuse. As part of our efforts to thwart this threat actor, we issue [Government-backed attack alerts](https://knowledge.workspace.google.com/admin/reports/government-backed-attack-alerts) when we detect COLD RELIC targeting Google accounts. COLD RELIC remains an active threat; GTIG has observed evidence of new phishing operations as recently as November 2026.

### Threat Detail 

Over more than a decade of tracking COLD RELIC alongside Mandiant incident response investigations, we have observed the group continually refine how it leverages data harvested from one intrusion to enable follow-on operations against downstream targets. In late 2025, COLD RELIC downloaded a large volume of data from a US-based organization, searching for names, email addresses, and email archives, likely to fulfill broader intelligence requirements. In 2026, Mandiant investigated a subsequent COLD RELIC intrusion at a second US-based organization where phishing URL parameters and impersonation pretexts indicated that COLD RELIC likely leveraged contact and relationship context from the first organization to target the second.

One of the hallmarks of COLD RELIC phishing campaigns is the use of a compromised website as the initial link that will redirect the target to the actual phishing domain. This provides COLD RELIC with a layer of misdirection and hides their phishing domains, while also giving them a chance to fingerprint anyone visiting the link to determine if they should be redirected or not. A COLD RELIC phishing link usually contains a parameter on the end of it with a value that is set by the attacker and often indicates a relationship to a previous victim or what the lure is. For example, a URL might look like these (though this is not always the case):

```
https://compromised.example.com/some_path/some_file.php?file=<previous_victim_name>
https://compromised.example.com/some_path/some_file.php?ref=<lure_name>
```
Figure 1: Sample URLs incorporating targeted individuals’ names or lure topics

During Mandiant’s incident response investigation at the second US-based organization, responders identified that COLD RELIC initiated contact over an encrypted messaging app while impersonating an employee from the first victim organization. In parallel, GTIG correlated a COLD RELIC redirector URL from the intrusion that had been submitted to VirusTotal in June 2026, whose query parameter referenced the first victim organization.

### Case Study 1 - Stolen Credentials to Data Exfiltration

During the late-2025 intrusion, GTIG observed COLD RELIC operators compromise the cloud productivity environment of a US-based organization. To gain initial access, COLD RELIC leveraged a residential proxy network in the US located in close geographical proximity to the victim. COLD RELIC authenticated using the stolen credentials of a Super Admin account, in combination with a multi-factor authentication (MFA) push notification fatigue attack. After the victim user accepted an MFA request, COLD RELIC registered a device model previously unseen within the tenant of the victim organization. COLD RELIC leveraged passkeys, MFA backup codes, and rogue MFA devices to retain access throughout the intrusion.

COLD RELIC used the privileges of the compromised Super Admin account to download the contents of the entire organization’s cloud storage drive by both mass sharing files to a COLD RELIC-operated email account and downloading files directly. While operating inside the tenant of the victim organization, COLD RELIC accessed the Admin Console, queried Admin security investigation and email audit logs to check defensive visibility, and viewed, modified, and deleted Alert Center notifications to remove forensic evidence of the initial intrusion. COLD RELIC also exported full employee lists and initiated a domain-wide data export via Google Workspace Customer Takeout using Super Admin privileges. Unlike individual end-user Google Takeout, Customer Takeout is an administrative tenant-wide export tool; these requests are logged in Google Workspace Admin audit logs (`CUSTOMER_TAKEOUT_CREATED`), and administrators can also [disable Google Takeout for users at the organizational level](https://knowledge.workspace.google.com/admin/users/advanced/allow-or-block-google-takeout).

Following mass data theft and antiforensics activities, COLD RELIC maintained access to the victim organization for several months and performed additional activities including:

- Email inbox sync via OAuth to external email clients
- Reauthentication using unrevoked attacker-enrolled passkeys that persisted across password and session resets and bypassed device registration controls
- Targeted cloud drive document access related to credentials, email archives, personnel information, and other documents relevant to COLD RELIC’s intelligence collection requirements

When the threat actor was removed from the victim organization’s infrastructure, GTIG observed COLD RELIC leveraging email accounts impersonating employees of the victim organization. These impersonated accounts were used to target both internal employees and associates within the same professional circles with renewed social engineering attempts.

### Case Study 2 - Leveraging Previous Compromise - Initial Approach

During the second intrusion, COLD RELIC demonstrated competency in navigating multi-cloud environments and federated authentication mechanisms. GTIG observed COLD RELIC operators compromise a Microsoft Entra ID user account of a US-based organization that used Entra ID as its federated single sign-on (SSO) identity provider for Google Workspace. To gain initial access, COLD RELIC impersonated an employee of the organization impacted in Case Study 1 to establish a pretext for communications over a secure messaging app. The threat actor ultimately shared phishing links during the course of the conversation. These phishing links, designed to steal credentials and authentication tokens for Entra ID, redirected the victim to document lures relevant to the ongoing conversation in order to avoid raising suspicion. Upon successful authentication using the stolen credentials, COLD RELIC registered and used a new MFA device in the SSO solution to retain access to the user account throughout the intrusion.

A redacted and abbreviated version of the social engineering conversation is included below (image generated with LLMs):

Figure 2: Redacted, LLM-generated depiction of observed threat actor social engineering engagement

By impersonating someone known in the same professional circles as the new target, COLD RELIC increased their chance of phishing success. Ultimately, in this case, COLD RELIC was able to obtain credentials to the organization and perform bulk download of files accessible in the compromised user’s cloud drive.

### Post-Compromise Activity

After gaining initial access to an organization, COLD RELIC registers rogue MFA devices, passkeys, and MFA backup codes to establish long-term persistence. Once persistence is secured, COLD RELIC conducts aggressive data collection and exfiltration operations, accessing email, chat, and cloud storage repositories. While COLD RELIC's primary objective post-compromise is mass collection and download of files and email archives, it simultaneously performs targeted queries for specific terms of interest. In particular, COLD RELIC searches for credentials, personnel information, email archives (.pst files), and documents related to their collection requirements. Additionally, COLD RELIC seeks out data that can support subsequent spear-phishing operations, including organizational rosters, contact lists, resumes, and event schedules to build convincing pretexts for future targets.

Beyond seeking out data to support subsequent operations, COLD RELIC also appeared to repurpose the account used in Case Study 2 for follow on targeting. After the compromise, the encrypted messaging application used for the initial approach recorded that the threat actor changed their profile name to a completely new person. GTIG believes this new persona was likely used to continue to target other organizations in the same professional circles in a similar manner to both of the cases documented here.

### Outlook and Implications

COLD RELIC’s campaigns demonstrate the convergence of human-centric social engineering and cloud identity abuse. By obtaining access to strategic personnel rosters and operational documents, Russian intelligence services turn legitimate business communications into attack vectors against trusted partners. Their ability to navigate across multiple cloud ecosystems highlights that organizations must defend their entire identity estate holistically. GTIG will continue to track, disrupt, and expose COLD RELIC infrastructure to protect global cloud users.

### Remediation and Hardening

As previously mentioned, GTIG has observed COLD RELIC heavily rely on residential proxy networks in the course of their intrusions. Moreover, the group goes one step further in obfuscating their activities by selecting proxies that geolocate to the same approximate location as their victim users, thereby avoiding impossible travel or other heuristic-based alerting mechanisms. GTIG recommends enriching authentication logs with [residential proxy](https://spur.us/blog/residential-proxy-lateral-movement-risk) and VPN IP reputation feeds, alerting on sudden residential ASN shifts for privileged accounts, and applying conditional access policies to block or detect logons from known proxy networks.

In some cases, the severity and scope of COLD RELIC intrusions were amplified due to users storing credentials and other secrets within their organization’s cloud storage platforms. This enabled COLD RELIC to pivot to additional accounts or services that it would not have otherwise been able to access, including users’ personal accounts which are typically unmonitored by their employers. Organizations can implement cloud storage Data Loss Prevention (DLP) policies, such as [Google Workspace’s Security & Data Protection](https://knowledge.workspace.google.com/admin/security/create-data-protection-rules), to warn or block users attempting to create, upload, or externally share files matching sensitive patterns.

In at least one case, GTIG observed that a victim organization identified the intrusion and attempted to remediate COLD RELIC’s access to their cloud tenant via password resets for impacted accounts. However, because the threat actor hijacked sessions and the victim organization failed to also revoke all existing sessions for the accounts in question, COLD RELIC maintained access. In similar circumstances, such as Business Email Compromise (BEC) intrusions, GTIG recommends organizations revoke all user sessions in addition to forcing password resets for impacted accounts.Organizations should implement the following recommendations:

1. Identity & Multi-Factor Authentication
2. Enforce Phishing-Resistant MFA (FIDO2 / WebAuthn): Replace SMS, voice, and push notifications with hardware security keys (e.g., Titan Security Keys). Hardware keys are bound to the origin URL and cannot be intercepted by AiTM reverse proxies or approved via fatigue attacks.
3. Restrict and Audit Passkey Registrations: Monitor identity logs for passkey registrations and rogue device enrollments, particularly on administrative accounts.
4. Harden MFA Registration: Require existing administrators or out-of-band identity verification to approve new MFA devices or secondary authenticators (such as Microsoft Authenticator or passkeys).
5. Organizations and individuals may consider enrolling in the [Advanced Protection Program](https://landing.google.com/advancedprotection/).
6. Session Management & Incident Response
7. Mandate Session & OAuth Revocation in BEC Playbooks: When remediating suspected account compromise, password changes alone are insufficient. Administrators must immediately revoke all active browser sessions, refresh tokens, and authorized third-party OAuth app permissions across both Google Workspace and Microsoft Entra ID, and remove any unauthorized passkeys, backup codes, or MFA devices.
8. Audit Third-Party OAuth Grants: Continuously review authorized third-party applications in Google Workspace and Microsoft 365, flagging unexpected native desktop email clients (e.g., Thunderbird) or external mail services (e.g., Proton Mail).
9. Network & Infrastructure Controls
10. Detect & Block Residential Proxy Logons: Restrict administrative access from consumer ISPs, VPNs, and known residential proxy ASN ranges (e.g., AS5650, AS20115).
11. Cross-Cloud DLP Policies: Deploy Data Loss Prevention (DLP) rules across cloud storage (Google Drive, OneDrive, SharePoint) to alert on documents containing sensitive terms (e.g., passwords, roster, .pst) or to restrict mass external file-sharing.

### Detections

### Google Security Operations (SecOps)

Google SecOps customers have access to these broad category rules and more under the Mandiant Frontline Threats rule pack. The activity discussed in the blog post is detected in Google SecOps under the rule names:

- Google Workspace Successful MFA Fatigue Attack
- Google Workspace Customer Takeout Initiated
- Google Workspace Alert Center Alert Deletion
- Google Workspace Directory User List Download
- Google Workspace Drive Bulk External or Freemail File Sharing
- Google Workspace Device or Passkey Enrollment Following MFA Fatigue
- Google Workspace OAuth Broad Mail Scope Granted to Unapproved Client
