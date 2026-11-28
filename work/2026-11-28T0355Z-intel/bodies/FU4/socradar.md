---
title: "SAP Security Incident: GitHub Tokens and Source Code"
author: Yağmur Ernalbant
url: https://socradar.io/blog/sap-security-incident-github-tokens-source-code/
hostname: socradar.io
description: SAP confirmed suspicious activity after reports of stolen employee GitHub tokens and altered source code. What is confirmed, what is not, and what to do.
sitename: SOCRadar
date: "2026-11-27"
categories: ['Cyber News']
tags: ['SAP security incident', 'SAP source code', 'GitHub tokens']
fingerprint: d02161f8e4276c9
language: en
image: https://socradar.io/wp-content/uploads/2026/11/sap-security-incident-github-tokens-source-code.jpg
pagetype: article
filedate: "2026-11-28"
---
# SAP Security Incident: Stolen GitHub Tokens and Source Code Risk

SAP has confirmed that it identified suspicious activity and took immediate measures, after media reports on November 26 said attackers had stolen authentication tokens belonging to SAP employees and used them to access and alter source code on GitHub. The company says its investigation has so far found **no evidence of unauthorized access to customers’ business data**.

An internal SAP letter to employees placed the suspicious activity on GitHub. SAP has not commented on the token theft reports, named the repositories involved or said whether any modified code reached software that customers run. No [threat actor](https://socradar.io/glossary/threat-actors/) has been named, and there is no public claim of responsibility.

## What Happened?

The incident became public on November 26, 2026, through media reports citing unnamed sources and internal communications. They made three main claims:

- **Token theft:** Attackers obtained authentication tokens belonging to SAP employees, which serve as digital access keys
- **Code tampering:** The tokens could be used to access and alter SAP source code on GitHub, and one report said code was also copied
- **Internal response:** SAP tracked the incident internally as **“Project Granite,”** and it was described inside the company as an **“active security incident”**

The reports also said the attackers may have used AI systems, and one cited internal sources describing possible use of agentic AI. SAP has not confirmed these details.

## How Did SAP Respond?

SAP replied the same evening in a [statement](https://www.t-online.de/finanzen/boerse/ticker/sap-haben-verdaechtige-aktivitaeten-identifiziert-spiegel-hackerangriff/0DBAF4002F9BA733/) to a press agency. It said it had identified suspicious activity, had immediately taken the necessary measures to protect customers and keep its services secure, and had so far found no indication of unauthorized access to customer business data. It added that its security measures are continuously being developed.

Immediate measures include restricting access to GitHub, stopping automated processes and replacing signing keys. SAP has not commented on these steps publicly, and it did not confirm the description of the event as a hacking attack.

## What Does the Internal Letter Add?

Press agency [reporting](https://www.ariva.de/news/roundup-sap-haben-verdaechtige-aktivitaeten-identifiziert-12222183) on an internal SAP letter, sent to employees a few days before the statement, adds two details. The letter said the suspicious activity was found within GitHub, and it asked employees to check whether they needed to take security steps, such as changing their access credentials.

As of November 27, 2026, the claims break down as follows:

| **Claim** | **Status** | 
|---|---|
| SAP identified suspicious activity and took immediate measures | Confirmed by SAP | 
| No evidence of access to customer business data | Confirmed by SAP, based on the investigation so far | 
| Suspicious activity was found within GitHub | Stated in an internal SAP letter seen by a press agency | 
| Employee authentication tokens were stolen | Reported by media citing unnamed sources; not confirmed by SAP | 
| Source code on GitHub was accessed and altered, and reportedly copied | Reported by media citing unnamed sources; not confirmed by SAP | 
| AI was used in the attack | Suggested in media reports; not confirmed by SAP | 
| Affected repositories, products or code branches | Not disclosed | 
| Threat actor | Not identified; no public claim of responsibility | 

The customer data assurance is narrower than it may sound. It covers business data held for customers and says nothing about source code, internal credentials or the integrity of software built from the affected repositories.

## Why Does Altered Code Matter More Than Copied Code?

SAP publishes a large amount of code on GitHub, from open-source projects to SDKs, tools and libraries used by developers building on its platforms. SAP has not said whether the reported activity touched public repositories, private ones or both, and the answer makes a real difference to the risk.

Copied code is mainly an intellectual property and reconnaissance problem. Private source lets an attacker study products offline for weaknesses, though it does not hand over access to customer systems by itself.

Altered code is a supply chain question. If an attacker can commit changes with a legitimate employee’s token, those changes carry that employee’s identity and may pass casual review. The key unknown is whether any modification was caught before it moved into a build, a package release or a deployed service. SAP has not said, and there is no public indication so far that tampered code reached customers.

## SAP’s Developer Ecosystem Was Targeted Earlier This Year

In April, SAP’s developer tooling was hit by a separate supply chain attack. On April 29, 2026, malicious versions of four SAP-related npm packages **(mbt, @cap-js/db-service, @cap-js/postgres and @cap-js/sqlite)** were published in the [Mini Shai-Hulud](https://socradar.io/blog/sap-mini-shai-hulud-supply-chain-attack/) campaign. The [malware](https://socradar.io/glossary/malware/) stole developer secrets, including GitHub and npm tokens and CI/CD credentials, and used them to spread further. Researchers assessed that [TeamPCP](https://socradar.io/blog/dark-web-profile-teampcp/) was likely behind it.

SAP’s FAQ on that attack named its CAP and MTA components as affected and advised users to rotate all secrets reachable from compromised systems, including GitHub and npm tokens. SAP’s statement on the November incident does not mention that campaign.

This week, [1Password](https://socradar.io/blog/1password-breach-employee-github-account/) also disclosed a breach that began with a compromised employee GitHub account.

## What Should SAP Customers and Developers Do Now?

SAP has not published customer guidance for this incident. Until it does, these general precautions apply to teams that build on SAP software and open-source components:

- **Follow official channels:** Watch SAP’s Trust Center and Security Notes for any advisory tied to this incident
- **Pin and verify SAP open-source dependencies:** Use exact versions of SAP packages from npm, Maven and GitHub, and check release history for unexpected versions
- **Review recent upstream changes:** Teams that build on SAP open-source code should look for unusual commits or releases in the repositories they consume over the past several weeks
- **Harden your own GitHub access:** Prefer short-lived, fine-grained tokens, enforce SSO and [phishing](https://socradar.io/glossary/phishing/)-resistant MFA for developers and remove unused personal access tokens
- **Audit token activity:** Review GitHub organization audit logs for actions by unfamiliar tokens or from unusual locations
- **Expect incident-themed phishing:** Treat emails that reference the SAP incident and push account “verification” or patches outside normal channels as suspicious

## Which Questions Are Still Open?

SAP’s investigation is ongoing, and the answers that matter most for customers have not been published: whether and how tokens were stolen, which repositories and products were affected, whether the repositories were public or private, when the activity started and was detected, and whether any altered code entered a release.

Any of these could shift the incident from an internal code exposure to a supply chain event, so the next SAP update deserves close attention.

## Keep Watch on Vendor Incidents With SOCRadar

When a core business software vendor confirms suspicious activity but shares few details, teams need to follow the vendor’s disclosures and watch for any sign of stolen material being traded:

- **[Supply Chain Intelligence](https://socradar.io/products/supply-chain-intelligence/)****:** Flags security incidents at vendors in your technology stack, such as SAP, so you can assess exposure as new details are disclosed
- **[Dark Web Monitoring](https://socradar.io/products/dark-web-monitoring/)****:** Watches [underground forums](https://socradar.io/blog/top-5-underground-hacker-forums-that-are-accessible-via-your-web-browsers-such-as-google-chrome-firefox-and-internet-explorer/) and leak channels for SAP source code, credentials or data offered for sale or leaked
- **[Brand Protection](https://socradar.io/products/brand-protection/)****:** Detects lookalike domains and phishing pages that use the SAP incident as a lure against your users

As SAP’s investigation continues, SOCRadar keeps the vendor picture and underground activity in view so teams can act as soon as the risk becomes clearer.
