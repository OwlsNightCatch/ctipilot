---
title: Former ShinyHunters-affiliated cluster O-UNC-053 moves to new INCEPTION leak site
url: https://www.okta.com/blog/threat-intelligence/former_shinyhunters_cluster_moves_to_new_inception_site/
hostname: okta.com
description: In November 2026, organizations targeted by cluster O-UNC-053 appeared on a new data leak site branded as INCEPTION, rather than the previous ShinyHunters site.
sitename: Okta
date: "2026-11-23"
tags: ['Threat Intelligence', 'Social Engineering', 'Blog Post', 'Phishing Resistance', 'Phishing']
fingerprint: "491828d3081ae7dc"
language: en
image: https://www.okta.com/content/dam/okta-www/en_us/blog/threat-intelligence/former-shinyhunters-affiliated-cluster-o-unc-053-moves-to-new-inception-leak-site/image3.png
pagetype: website
filedate: "2026-11-25"
---
## Executive Summary

In November 2026, organizations targeted by threat cluster O-UNC-053 began appearing on a new data leak site (DLS) branded as INCEPTION, rather than the previous ShinyHunters DLS that published targets between March-September 2026.

While this threat cluster has changed their brand affiliation, the operators remain active in targeting organizations with voice phishing attacks and account takeovers resulting in data theft and extortion. The key prevention against these attacks remains implementing [phishing-resistant authentication](https://help.okta.com/oie/en-us/content/topics/identity-engine/authenticators/phishing-resistant-auth.htm).

## Threat Analysis

O-UNC-053 has been active since March 2026 and regularly performs multi-stage social engineering and credential harvesting campaigns targeting entities in various sectors, including technology, healthcare, biotechnology, financial services, insurance, entertainment, gaming, retail, transportation, hospitality, and legal industries. The campaigns use voice phishing (vishing) in which callers often impersonate support personnel and attempt to compel targeted users to urgently perform password resets. The operators change themes of phishing domains approximately every 4-6 weeks.

The threat actor has deployed a phishing kit to intercept authentication flows. This infrastructure first harvests the targeted user’s credentials (username and password) and then prompts for various MFA factors to steal SSO credentials. While interacting with targeted users on the phone, the operators socially engineer them into sharing factors like one-time passcodes and approving push notifications. The kit is not capable of bypassing phishing-resistant methods of authentication such as Okta FastPass and FIDO2/WebAuthn passkeys. If successful, the operators gain access to SaaS applications and exfiltrate sensitive data, which is often used to extort targets under the threat of releasing it on a data leak site.

**Infrastructure**

The domains from this cluster’s current campaign are registered predominantly through NICENIC, with Spaceship, Tucows, and NameSilo also being used. The infrastructure uses Cloudflare nameservers, with the phishing sites fronted by Cloudflare (AS13335). WHOIS records use privacy redaction services.

As of November 2026, O-UNC-053 domain names use the following patterns:

- legal-\<target>\[.\]com
- legaldept-\<target>\[.\]com
- \<target>\[.\]legal
- \<target>-legal\[.\]com

The “legal” themed campaign started in late October 2026 and was preceded by campaign themes using similar patterns in the phishing domains, as shown in the appendix. Cloudflare challenges block the current campaign’s domains from scanners, which has prevented deep analysis of the phishing kit(s) in use. The domains are typically registered on or within one day of a campaign starting, with several domains being registered the same day that a vishing call was received.

After an August 2026 peak, O-UNC-053 domain registrations dropped significantly across September and October, before rebounding in November. This pattern may be indicative that the threat actors' operations may have been impacted by the late September 2026 arrests of alleged ShinyHunters members.

When performing account takeovers during the most recent campaign, the threat actor shifted their operational infrastructure and began using Internet Utilities Na LLC (AS19318) in addition to 1337 Services GmbH (AS210558) and Talon Ops LLC (AS399486).

## DLS Affiliation Assessment

Okta Threat Intelligence tracks phishing infrastructure that we attribute to various activity clusters. This infrastructure commonly includes a target name in the phishing domain or in the branding of the phishing kit (e.g. legal-\<target>\[.\]com, as explained above). We subsequently analyze if those targets have data published on data leak sites (DLS).

Throughout our tracking of O-UNC-053 between March and September 2026, we observed the names of targeted entities appear on the ShinyHunters DLS between 1 and 28 days after the phishing infrastructure was registered.

While we are unable to validate if published data is authentic, we assess that the registration of O-UNC-053 infrastructure targeting an organization followed by publication of that organization’s alleged stolen data on the ShinyHunters DLS represented a significant relationship between the two entities. The exact nature of this relationship is unclear, but may have involved an agreement between the operator(s) of the O-UNC-053 cluster and the operator(s) of the ShinyHunters DLS. We assess the operator(s) of the ShinyHunters DLS almost certainly had relationships with multiple intrusion operators, as we observed organizations that were not targeted by O-UNC-053 infrastructure listed on the same data leak site.

From March 2026 through September 2026, we regularly observed organizations targeted by O-UNC-053 infrastructure appearing on the ShinyHunters DLS. In September 2026, law enforcement agencies made two notable arrests of actors allegedly affiliated with the ShinyHunters brand: [Pepijn van der Stap](https://www.cbsnews.com/news/dutch-arrest-shinyhunters-fbi-hack/) on September 15 and [Saif ‌al-Din Khader (“Rey”)](https://www.reuters.com/world/middle-east/key-shinyhunters-hacker-detained-jordan-is-cooperating-sources-say-2026-10-03/) on September 29. Following these arrests, the ShinyHunters DLS [went down](https://www.reuters.com/legal/government/shinyhunters-website-goes-offline-after-fbi-deadline-expires-2026-09-30/), and we did not observe publication of any O-UNC-053 targets on any DLS throughout October and early November 2026 during the period that O-UNC-053 operators were registering new infrastructure. The below timeline depicts these details.

On November 16, 2026, researchers observed the appearance of a new DLS, branded as INCEPTION. The DLS listings included multiple targets for which Okta Threat Intelligence previously observed O-UNC-053 infrastructure registration. Our analysis indicates that O-UNC-053 infrastructure was registered between 6 and 19 days prior to the targets being named on the INCEPTION DLS.

This gap in publishing on any leak site followed by publishing on a new data leak site with a new brand is consistent with prior shifts from Com-affiliated actors. Before and after the change in DLS publication, O-UNC-053 maintained consistent infrastructure and TTPs, leading us to assess that the cluster has very likely changed their brand affiliation. We cannot currently make a high confidence assessment as to whether O-UNC-053 is operating the DLS themselves or is partnering with another extortion actor.

Regardless of the nature of the relationship with the INCEPTION DLS, O-UNC-053 remains active in conducting vishing attacks against targets in an effort to take over accounts, steal data, and extort targets. Organizations should take steps to protect against their ongoing intrusion attempts.

## Recommendations

Okta customers can find the detailed indicators for O-UNC-053 activity [in our Trust Center](https://security.okta.com/product/oktathreatintelligence/former-shinyhunters-affiliated-cluster-o-unc-053-moves-to-new-inception-leak-site).  This portal also includes an [interactive map](https://security.okta.com/product/oktathreatintelligence/mapping-com-linked-activity-clusters-to-data-leak-sites) of intrusion clusters and associated data leak sites.

The following recommendations are specific to Okta customers, and could be adapted for other solutions. 


| **ATT&CK Technique**  | **Tactic**  | **Control Recommendation**  | 
| T1566 Phishing  | Initial Access  | Enroll users in strong authenticators such as [Okta FastPass](https://help.okta.com/oie/en-us/content/topics/identity-engine/devices/fp/fp-main.htm), [passkeys](https://help.okta.com/oie/en-us/content/topics/identity-engine/authenticators/configure-passkeys.htm) or [smart cards](https://help.okta.com/oie/en-us/content/topics/identity-engine/authenticators/smart-card-authenticator.htm) and enforce phishing resistance in policy. Train users to identify indicators of suspicious emails, phishing sites and common social engineering techniques used by attackers. Make it easy for users to report potential issues by configuring [End User Notifications](https://help.okta.com/oie/en-us/Content/Topics/Security/Security_General.htm) and [Suspicious Activity Reporting](https://help.okta.com/en-us/Content/Topics/Security/suspicious-activity-reporting.htm). To identify or investigate possible phishing activity, review application logs (Okta logs, web proxies, email systems, DNS servers, firewalls) for any evidence of communication with suspicious domains listed in the IOC appendix. To take a proactive approach, monitor the domains regularly to see if the contents change. If content hosted on the domain violates copyright or legal marks, consider providing evidence and issuing a takedown request with the domain registrar and/or web hosting provider.  | 
| T1078 Valid Accounts  | Initial Access  | Use Okta authentication policies to restrict access to user accounts based on a range of customer-configurable prerequisites. We recommend administrators restrict access to sensitive applications to devices that are [managed](https://help.okta.com/oie/en-us/Content/Topics/identity-engine/devices/managed-main.htm) by Endpoint Management tools and [protected by endpoint security tools](https://help.okta.com/oie/en-us/Content/Topics/identity-engine/devices/edr-integration-main.htm). For access to less sensitive applications, require registered devices ([using Okta FastPass](https://help.okta.com/oie/en-us/Content/Topics/identity-engine/devices/fp/fp-main.htm)) that [exhibit indicators of basic hygiene](https://help.okta.com/oie/en-us/Content/Topics/identity-engine/devices/device-assurance.htm). Okta Behavior and Risk evaluations can be used to identify requests for access to applications that deviate from previously established patterns of user activity. Policies can be configured to step-up or deny requests using this context.  | 
| T1665 Hide Infrastructure  | Defense Evasion  | Deny or require higher assurance for requests from rarely-used networks. With Okta Network Zones, access can be controlled by location, ASN (Autonomous System Number), IP, and IP-Type (which can identify known anonymizing proxies).  | 

## A note on estimative language

Okta’s Threat Intelligence teams use the following terms to express likelihood or probability as outlined in the US Office of the Director of National Intelligence, Intelligence Community Directive 203 - Analytic Standards.

| Likelihood | Almost no chance | Very unlikely | Unlikely | Roughly even chance | Likely | Very likely | Almost certain(ly) | 
| Probability | Remote | Highly improbable | Improbable | Roughly even odds | Probable | Highly Probable | Nearly Certain | 
| Percentage | 1-5% | 5-20% | 20-45% | 45-55% | 55-80% | 80-95% | 95-99%  | 

*This advisory is provided for informational purposes only, without warranty or liability, does not constitute professional advice, and should not be relied upon to address every aspect of the subject discussed herein. Each customer remains solely responsible for consulting qualified advisors, evaluating its own cybersecurity risks, and selecting and implementing the security practices most appropriate for its specific operational needs.*
