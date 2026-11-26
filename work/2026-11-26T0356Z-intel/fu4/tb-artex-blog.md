---
title: ARTEX Attacks on South Korean Financial Institutions
author: ThreatBook Research Team
url: https://threatbook.io/blog/artex-attacks-south-korean-financial-institutions
hostname: threatbook.io
description: The incident has already caused data breaches at seven South Korean financial institutions, affecting approximately 67,000 individuals.
sitename: ThreatBook
date: "2026-10-09"
categories: ['Threat Research']
tags: ['Threat Research']
fingerprint: "935fa3036010b733"
language: en
image: https://threatbook.io/hubfs/featured-1200x630-v2-1.png
pagetype: article
filedate: "2026-11-26"
---
From September 27 to early October 2026, the internet-facing (peripheral) business systems of multiple South Korean financial institutions were attacked one after another. The attackers used ARTEX together with large language model (LLM)-assisted reconnaissance to exploit authentication and access-control gaps in loan-brokerage query services, employee mobile business-support, and customer-facing business pages, enumerating valid records and stealing personal and credit information. The defining characteristics of this campaign were cross-institution reconnaissance, proxy-IP rotation, and automated collection of business data.\[1\]\[5\]\[9\]

The incident has already caused data breaches at seven South Korean financial institutions, affecting approximately 67,000 individuals. The affected institutions include four commercial banks — Shinhan Bank, KB Kookmin Bank, Hana Bank, and BNK Busan Bank — the savings banks Yegaram and Welcome, and the consumer-finance company Hyundai Capital. The leaked information covers names, phone numbers, addresses, resident registration numbers or encrypted identity tokens, annual income, loan limits, employers, and loan-recruiter profiles, which could be used for targeted fraud and identity impersonation. Woori Bank, NH NongHyup Bank, and other institutions also detected related attack attempts but have not yet reported data breaches.\[9\]\[10\]\[11\]

South Korean regulators have launched on-site investigations, an industry-wide security review, and threat-information sharing. South Korean President Lee Jae-myung ordered a thorough investigation and the development of countermeasures. The principal warning this incident holds for financial institutions is that internet-facing business interfaces must enforce the same identity authentication and per-object authorization as core systems, and that anomaly-query monitoring must cover continuous data-pulling behavior conducted across rotating IPs.\[8\]\[10\]\[12\]

### Key timeline

Time

Key development

September 27, 2026

The internet-facing business systems of Hyundai Capital, KB Kookmin Bank, and Welcome Savings Bank were attacked.

September 28–30

Shinhan Bank and Hana Bank were attacked in succession; Yegaram Savings Bank detected signs of customer-information leakage.

September 30

Shinhan Bank reported the incident to South Korean regulators; the Financial Supervisory Service (FSS) and the Financial Security Institute (FSI) launched on-site investigations.

October 1–3

Shinhan, KB Kookmin, Hana, and BNK Busan banks, along with Yegaram and Welcome savings banks and Hyundai Capital, successively disclosed data breaches; the affected institutions span multiple financial sectors.

October 2

South Korea's Financial Services Commission (FSC) convened an emergency meeting, shared attack information and issued a checklist, requiring financial institutions to inspect their customer-facing business systems.

October 4

President Lee Jae-myung ordered a thorough investigation and the development of countermeasures.

October 6

South Korean financial regulators issued a consumer alert and launched a one-month special response to secondary risks, strengthening anti-fraud monitoring and the protection of affected customers.

As of October 9

Seven South Korean financial institutions had disclosed data breaches; incident investigation, industry security review, and remediation continue.

Timeline sources: \[1\]\[5\]–\[12\].

## Analysis of the leaked data

From late September to early October 2026, four South Korean banks, two savings banks, and one consumer-finance company successively disclosed information leaks caused by external attacks. The primarily affected systems were peripheral ones such as loan queries, employee business support, and corporate-customer services, and the breach victims included not only customers but also employees, outsourced personnel, and loan recruiters. The affected institutions and the scope of data are as follows.\[9\]\[10\]\[11\]

Institution

Disclosed scope of impact

Main leaked information

Systems involved

Shinhan Bank

Approx. 25,700 customers

Names, phone numbers, annual income, estimated loan limits, etc.; an additional 66 cases involving resident registration numbers and 97 cases involving connection information

Loan-progress and simple-query services used by loan brokers

KB Kookmin Bank

119 people, including 99 customers and 20 employees

Names, phone numbers, addresses, some encrypted resident registration numbers, etc.

Employee mobile business-support systems RM Agent and PB Agent

Hana Bank

89 customers

Resident registration numbers, names, addresses, email, phone numbers, employers

Business-support system ODS

BNK Busan Bank

11 outsourced developers

Names, phone numbers, dates of birth, email

Customer-facing web page

Yegaram Savings Bank

Preliminary estimate of approx. 40,000 customers

Names, dates of birth, contact information

Server storing customer information

Welcome Savings Bank

2,370 leaked records, of which 2,299 contain personal information

Corporate online-banking IDs, company names, representatives' names, work phone numbers, mobile numbers, email

Corporate-customer-related services

Hyundai Capital

146 home-loan recruiters

Names, mobile numbers, email, industry registration numbers, internal IDs, and resident registration numbers

Publicly accessible loan-recruiter query page

Separately, public reporting mentions that two P2P lending institutions suffered data leaks, though their names and the specific scope of impact were not specified in the relevant reports.\[9\]

## Attack process and technical analysis

### Phase 1 | Tooling: Deploying an AI-assisted attack environment

The attackers deployed the open-source AI penetration-testing platform ARTEX and combined it with large language models to assist in executing attack tasks. CrowdStrike found ARTEX configuration files, Claude Code session history, and memory files in an open directory controlled by the attackers, and identified a two-server structure consisting of a primary control node and an ARTEX hosting node. The configuration indicates that ARTEX primarily used DeepSeek v4.1-flash as its model backend, and the attackers also used GLM-5.3 and Grok 4.6 in other Claude Code sessions. This environment supported target analysis, tool invocation, and the adjustment of subsequent operations based on execution results, enabling the attackers to continuously handle attack tasks against multiple financial institutions.\[1\]

### Phase 2 | Infrastructure: Sustaining the attack through multi-country IP rotation

The attackers launched access from proxy nodes distributed across multiple countries and regions, and switched IPs to continue their attempts after some sources were blocked. After deduplication, the attack sources comprised 28 IPs spanning 12 countries and regions.\[7\]

Overlapping IPs, similar attack methods, and ARTEX-related artifacts appeared across the attack records of multiple banks, providing the basis for assessing that some of the activity shared a common origin. Shinhan Bank's handling especially illustrates the role of IP rotation: after the bank blocked anomalous sources, the attackers continued to access the relevant services through other IPs, so blocking a single source did not immediately stop the attack.

### Phase 3 | Reconnaissance: Finding access gaps in peripheral business systems

The attacks concentrated on internet-reachable peripheral systems directly associated with customer or staff information, including Shinhan Bank's loan-brokerage query service, KB Kookmin Bank's employee mobile business-support systems RM Agent and PB Agent, Hana Bank's sales-support system ODS, and Hyundai Capital's home-loan recruiter query page. These entry points were simultaneously connected to personnel or customer data, making them high-value targets for cross-institution reconnaissance.\[8\]\[9\]

These systems handle business such as loan-progress queries, employees working outside the office, customer-material processing, and personnel-information queries. The key gap was that, after external requests reached the business interfaces, identity verification, session checks, or query-object authorization failed to adequately restrict the accessible data. The attackers accordingly sought interfaces that could directly return sensitive fields and expanded the scope of their data pull through repeated queries.\[8\]\[9\]

### Phase 4 | Initial breach: Exploiting authentication, session, and access-control gaps

The attackers obtained unauthorized data access through authentication or access-control flaws in the peripheral systems. Typical manifestations include:

- Shinhan Bank: The attackers bypassed the authentication of the loan-brokerage mobile query service in an anomalous manner and accessed loan-application progress and related information, establishing an entry point for subsequent ID enumeration and cross-service queries.\[9\]
- KB Kookmin Bank: The employee mobile business-support systems RM Agent and PB Agent were subjected to anomalous external access, and the information of customers as well as current and former employees was obtained.
- Hana Bank: The ODS system, used by employees to handle customer business materials away from branches, was subjected to anomalous external access, and the identity and contact information of 89 customers was leaked.
- BNK Busan Bank: The customer-facing web page was subjected to anomalous access, exposing the profiles of 11 outsourced developers. Hyundai Capital's loan-recruiter query page exposed the information of 146 recruiters.\[11\]

### Phase 5 | Expanding the data pull: Business-ID enumeration and cross-service queries

After entering an accessible query entry point, the attackers identified valid records by repeatedly substituting different business IDs, then used the returned information to expand the scope of collection. The attack path disclosed by Shinhan Bank is relatively complete.\[9\]

Step

Attacker action

Data-acquisition effect

1

Submit different business IDs to the loan-brokerage query service

Identify valid records and customer identifiers from the responses

2

Use the valid identifiers to continue querying associated information

Obtain contact information, income, and loan-related fields

3

Repeat the queries and aggregate the returned results

Form a collection of personal and credit information that can be correlated to specific customers

The effectiveness of the attack depends on whether the server enforces binding checks on identity, privilege, and query object for each request. As long as changing the ID yields another object's data, automated tools can expand a single-record exposure into a bulk breach. Shinhan Bank disclosed that approximately 25,700 customers were affected, and some records also involved resident registration numbers and identity-connection information.\[9\]

### Phase 6 | Data collection and exfiltration: Obtaining information usable for fraud and identity impersonation

The attackers continuously extracted data from the accessible business pages and query interfaces. The data exposed by different institutions was directly related to the business purpose of their affected systems:

- Shinhan Bank primarily involved customer identity, contact information, annual income, and estimated loan limits.
- KB Kookmin Bank and Hana Bank respectively involved the personal profiles of 119 customers and employees, and of 89 customers.
- Yegaram Savings Bank disclosed that approximately 40,000 customers' information might have been affected, with the scope still under verification.
- Welcome Savings Bank leaked approximately 2,370 records, of which 2,299 contained personal information; the number of individuals has not yet been deduplicated.
- Hyundai Capital involved 146 home-loan recruiters, and BNK Busan Bank involved 11 outsourced developers.

The attackers collected and aggregated the sensitive fields returned by business pages and interfaces one record at a time. Such data pulls can be dispersed across a large number of normal HTTP responses, so detection should focus on single-session cross-object queries, ID-change patterns, the volume of sensitive fields returned, and continuous requests from multiple IPs — not merely large-file transfers.\[11\]

### Phase 7 | Monetization intent and secondary risks

Analysis shows that the attackers had queried channels for selling leaked South Korean data and Telegram data-trading groups, reflecting an intent to profit by selling the stolen information. The leaked data could also be used for subsequent fraud: scammers leverage genuine information such as income, loan limits, and employers to gain victims' trust, then impersonate bank staff and, on the pretext of arranging low-interest loans, loan refinancing, or compensation for the breach, induce victims to transfer money or install malicious apps.\[1\]\[6\]\[12\]

### ATT&CK framework and incident TTPs

Tactic

Technique ID

Specific behavioral facts

Resource Development

T1583.003 Acquire Infrastructure: Virtual Private Server

Deployed ARTEX hosting and control nodes and configured proxy resources.\[1\]

Resource Development

T1588.007 Obtain Capabilities: Artificial Intelligence

Used ARTEX and multiple large language models to assist in the analysis, orchestration, and execution of attacks.\[1\]

Reconnaissance

T1595 Active Scanning

Probed the internet-reachable business entry points of multiple financial institutions.\[5\]\[9\]

Initial Access

T1190 Exploit Public-Facing Application

Exploited authentication and access-control gaps in peripheral systems to obtain unauthorized data access.\[8\]\[9\]

Collection

T1119 Automated Collection

Repeatedly requested valid records to obtain personal and credit profiles in bulk; this is a behavioral mapping.\[9\]

Command and Control

T1090 Proxy

Accessed targets through multiple proxy exits to hide the true source and maintain operational continuity.\[1\]\[7\]

Incident-level TTP

Business-object enumeration and correlated queries

Repeatedly changed business IDs to locate valid records, then obtained associated fields; this does not map to operating-system account Discovery.\[9\]

## Remediation recommendations

### Remediation of peripheral entry points and query authorization

Inventory all internet-reachable employee, loan-broker, outsourcing, and business-support systems, assign clear owners, and close unnecessary exposure. Enforce server-side verification of identity, role, and object ownership for every sensitive query; do not return data based solely on a customer ID, a case ID, or front-end login state. Add managed-device, certificate, and multi-factor authentication constraints to employee mobile-office entry points.\[8\]\[12\]

### Cross-IP behavior detection and forensic traceback

Focusing on the period from late September to early October 2026, correlate WAF, reverse-proxy, API-gateway, application, and identity logs. Prioritize searching for the incident-associated IPs, then combine UA, Host, URI, session identifiers, ID sequences, and response fields to determine the actual impact. Aggregate requests from low-rate or rotating IPs by the same business object, session, and operation pattern; preserve the original requests, responses, and access-control configuration as evidence.

### Data-impact and secondary-risk control

Determine the breach scope based on the fields actually returned, the affected objects, and the query time, distinguishing among customers, employees, outsourced personnel, and recruiters, and deduplicate repeated records. Provide affected individuals with query services and anti-fraud guidance, emphasizing in particular that loan and income information may be used to impersonate financial institutions. Share effective indicators and handling results through existing industry channels.\[11\]\[12\]

### IOC application and candidate-asset verification

Use the incident-associated IPs for priority traceback and risk assessment; apply controls to shared proxy and third-party model services in combination with actual business usage. Use tool fingerprints and Team Cymru candidate nodes for hunting, and escalate them to incident-level indicators only after obtaining a direct correlation from victim logs, attack tasks, or trusted industry intelligence. Search the candidate addresses item by item according to the original posts; do not expand the entire network segment they belong to into a blocking target.

## IOCs and detection leads

This section presents, respectively, “incident-associated IPs,” “attacker-side files, services, and accounts,” “tool detection signatures,” and “candidate infrastructure.” Confidence is assessed for the nature of the correlation described in the tables and does not imply that node attribution, real identity, or attack success has been confirmed. Information is current as of October 9, 2026.

Confidence

Basis for assessment

Scope of application

High

Attacker-side files, configuration, or sessions directly support the corresponding correlation

Priority forensics and historical-log searching, handled in combination with current access conditions

Medium-High

Research institutions explicitly identified the proxy activity, or industry attack-IP materials have been publicly transcribed

Prioritize traceback; confirm this institution's risk based on access behavior and impact evidence

Medium

Third-party scan disclosure or tool source-code signatures; used to identify deployment, service, or account correlation

Hunting and cross-verification; not directly equivalent to incident attack assets

Low / To be verified

Self-reported identity or still lacking direct incident correlation

Manual verification, retaining the source and limiting conditions

### Publicly disclosed incident-associated IPs

CrowdStrike disclosed 10, and the 19 IPs released by PLURA come from a list issued by South Korea's Financial Supervisory Service (금감원), officially characterized as the “attacker IPs” of this financial-institution intrusion (the intrusion type labeled as a presumed automated attack leveraging an AI agent); however, the official materials did not mark each IP for whether it used ARTEX, so it cannot be confirmed that every IP used ARTEX. The two lists overlap on 7, totaling 22 after deduplication.\[1\]\[2\]

IP

Nature and basis of correlation

Incident-correlation confidence

ARTEX correlation status

`38.244.50.120`

ARTEX hosting node; directly correlated by configuration and public files

High

Deployment confirmed

`101.53.80.20`

Attack proxy node; attacker-side proxy-activity record

Medium-High

ARTEX-related activity proxy

`205.214.59.31`

Attack proxy node; attacker-side proxy-activity record

Medium-High

ARTEX-related activity proxy

`124.155.252.63`

Attack proxy node; attacker-side proxy-activity record

Medium-High

ARTEX-related activity proxy

`154.201.79.246`

Attack proxy node; attacker-side proxy-activity record

Medium-High

ARTEX-related activity proxy

`23.248.249.90`

Attack proxy node; attacker-side proxy-activity record

Medium-High

ARTEX-related activity proxy

`23.158.220.98`

Attack proxy node; attacker-side proxy-activity record

Medium-High

ARTEX-related activity proxy

`103.248.148.84`

Attack proxy node; attacker-side proxy-activity record

Medium-High

ARTEX-related activity proxy

`203.160.133.172`

Attack proxy node; attacker-side proxy-activity record

Medium-High

ARTEX-related activity proxy

`209.209.85.38`

Attack proxy node; attacker-side proxy-activity record

Medium-High

ARTEX-related activity proxy

`129.212.181.253`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`134.185.91.25`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`64.20.39.190`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`129.212.181.23`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`74.82.60.23`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`34.175.107.233`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`18.183.215.124`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`104.28.162.188`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`104.28.164.188`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`104.28.164.196`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`104.28.166.183`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

`104.28.155.179`

Attack IP listed in regulatory materials; specific node role to be verified

Medium-High

Not confirmed per IP

### Attacker-side file, service, and account leads

Indicator

Nature and scope of correlation

Confidence

Source

`38.244.50.120:18899`

Public-file access service on the ARTEX node

High / node correlation

\[1\]

`http://38.244.50.120:18899/.claude/CLAUDE.md`

The prompt file records another Hong Kong control-node address and is an infrastructure connection point

High / file correlation

\[1\]

`/.claude/CLAUDE.md`

File path assisting retrieval, judged in combination with host and file content

Medium / auxiliary signature

\[1\]

`xcai.pro`

Suspected third-party LLM API proxy/resale service providing DeepSeek access; search by service-usage leads

Medium / service correlation

\[1\]

`@YY520CN`

Telegram identifier appearing in attacker-side sessions and reused in other target-research records

Medium / account correlation; Low / real identity

\[1\]\[6\]

`YY`

Alias filled in when a resume was generated in a session; manual identity cross-verification

Low / identity lead

\[1\]\[6\]

`17820191556`

Phone number filled in during a session; manual identity cross-verification, not treated as a confirmed malicious communication number

Low / identity lead

\[1\]\[6\]

### ARTEX tool detection signatures

The following UA and installation signatures mainly come from PLURA's analysis of the public source code and are used to identify the tool or suspicious automated requests.\[3\]

User-Agent

Purpose

Tool identification / incident correlation

Source

`artex-enrich/1.0`

Web-asset information collection

Medium / to be verified

\[2\]\[3\]

`Mozilla/5.0 (spa-api-recon)`

Static analysis of HTML and JavaScript

Medium / to be verified

\[2\]\[3\]

`Mozilla/5.0 (spa-api-recon spider)`

Web traversal and collection of links and forms

Medium / to be verified

\[2\]\[3\]

Installation or management signature

Meaning and search scope

Tool identification / incident correlation

Source

`artex_token`

ARTEX management browser Cookie/Local Storage authentication key; not a fixed attack Cookie on victim websites

Medium / to be verified

\[3\]

`artex-selfupdate`

Tool-update communication; not a fixed attack UA directed at victim financial systems

Medium / to be verified

\[3\]

`ARTEX — Autonomous Penetration Testing Console`

Management console title

Medium / to be verified

\[3\]

`LLM-driven autonomous penetration-testing system console`

Management console description

Medium / to be verified

\[3\]

`autumn27/artex`

Tool container image

Medium / to be verified

\[3\]

### Team Cymru candidate scanned infrastructure

Team Cymru Research filtered out 52 server IPs that deploy ARTEX and use sub2api, new-api, or grok2api to provide AI relay services. Existing public evidence cannot confirm that these IPs participated in this attack on South Korean financial institutions, so they are listed as pivoting candidate assets with a confidence of “Medium.”\[4\]

Candidate IP

Original-post deployment tag

Deployment / incident-correlation confidence

`38.11.173.1`

ARTEX + sub2api

Medium / to be verified

`38.11.173.5`

ARTEX + sub2api

Medium / to be verified

`38.11.173.10`

ARTEX + sub2api

Medium / to be verified

`38.11.173.14`

ARTEX + sub2api

Medium / to be verified

`38.11.173.19`

ARTEX + sub2api

Medium / to be verified

`38.11.173.23`

ARTEX + sub2api

Medium / to be verified

`38.11.173.28`

ARTEX + sub2api

Medium / to be verified

`38.11.173.32`

ARTEX + sub2api

Medium / to be verified

`38.11.173.37`

ARTEX + sub2api

Medium / to be verified

`38.11.173.41`

ARTEX + sub2api

Medium / to be verified

`38.11.173.46`

ARTEX + sub2api

Medium / to be verified

`38.11.173.50`

ARTEX + sub2api

Medium / to be verified

`38.11.173.59`

ARTEX + sub2api

Medium / to be verified

`38.11.173.68`

ARTEX + sub2api

Medium / to be verified

`38.11.173.77`

ARTEX + sub2api

Medium / to be verified

`38.11.173.86`

ARTEX + sub2api

Medium / to be verified

`38.11.173.95`

ARTEX + sub2api

Medium / to be verified

`38.11.173.104`

ARTEX + sub2api

Medium / to be verified

`38.11.173.108`

ARTEX + sub2api

Medium / to be verified

`38.11.173.113`

ARTEX + sub2api

Medium / to be verified

`38.11.173.117`

ARTEX + sub2api

Medium / to be verified

`38.11.173.122`

ARTEX + sub2api

Medium / to be verified

`38.11.221.9`

ARTEX + sub2api

Medium / to be verified

`38.11.221.18`

ARTEX + sub2api

Medium / to be verified

`38.11.221.27`

ARTEX + sub2api

Medium / to be verified

`38.11.221.36`

ARTEX + sub2api

Medium / to be verified

`38.11.221.45`

ARTEX + sub2api

Medium / to be verified

`38.11.221.49`

ARTEX + sub2api

Medium / to be verified

`38.11.221.54`

ARTEX + sub2api

Medium / to be verified

`38.11.221.58`

ARTEX + sub2api

Medium / to be verified

`38.11.221.63`

ARTEX + sub2api

Medium / to be verified

`38.11.221.72`

ARTEX + sub2api

Medium / to be verified

`38.11.221.76`

ARTEX + sub2api

Medium / to be verified

`38.11.221.81`

ARTEX + sub2api

Medium / to be verified

`38.11.221.85`

ARTEX + sub2api

Medium / to be verified

`38.11.221.90`

ARTEX + sub2api

Medium / to be verified

`38.11.221.94`

ARTEX + sub2api

Medium / to be verified

`38.11.221.103`

ARTEX + sub2api

Medium / to be verified

`38.11.221.112`

ARTEX + sub2api

Medium / to be verified

`38.11.221.121`

ARTEX + sub2api

Medium / to be verified

`198.46.198.206`

ARTEX + sub2api, vps

Medium / to be verified

`173.254.220.78`

ARTEX + sub2api, vps

Medium / to be verified

`47.253.69.182`

ARTEX + sub2api

Medium / to be verified

`47.82.118.105`

ARTEX + sub2api

Medium / to be verified

`103.117.121.13`

ARTEX + sub2api, socks

Medium / to be verified

`198.200.59.86`

ARTEX + sub2api

Medium / to be verified

`14.103.211.223`

ARTEX + new-api

Medium / to be verified

`103.116.247.42`

ARTEX + new-api

Medium / to be verified

`81.71.120.246`

ARTEX + new-api

Medium / to be verified

`154.12.94.223`

ARTEX + grok2api

Medium / to be verified

`192.236.166.73`

ARTEX + grok2api, cyberstrikeai, mythic, scopesentry, vps

Medium / to be verified

`149.104.24.91`

ARTEX + sub2api, cyberstrikeai, arl, risknet, vps

Medium / to be verified

## References

Materials verified as of October 9, 2026. The numbers in the body and IOC tables correspond to the links below; the two PLURA articles use their current revised content.

**\[5\]** Herald Economy, Interview with South Korea's Financial Security Institute on ARTEX Artifacts, Shared IPs, and Common-Origin Activity, 2026-10-03 [https://mbiz.heraldcorp.com/article/10892496](https://mbiz.heraldcorp.com/article/10892496)

**\[11\]** Aju Press, Welcome Savings Bank and Hyundai Capital Retrospectively Discovered the Attack, with Record Counts and Timing, 2026-10-07 [https://m.ajupress.com/view/20261007084870471](https://m.ajupress.com/view/20261007084870471)

**\[12\]** Financial Services Commission of South Korea, Briefing from the October 4 Emergency Inspection Meeting for the Entire Financial Sector, published 2026-10-06 [https://fsc.go.kr/no010101/87876](https://fsc.go.kr/no010101/87876)
