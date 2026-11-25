---
title: "Days to Zero: How Ransomware and Accelerated Exploitation Are Reshaping SAP Security"
author: Onapsis Research Labs
url: https://onapsis.com/blog/days-to-zero-sap-threat-report-2026/
hostname: onapsis.com
description: Explore the 2026 SAP Threat Report by Onapsis and Recorded Future. Learn how ransomware and AI are actively reshaping enterprise SAP security.
sitename: Onapsis Research Labs
date: "2026-10-29"
tags: ['Onapsis Research Labs']
fingerprint: e54a05f50f54b7a8
language: en
image: https://onapsis.com/wp-content/uploads/blog-recorded-future-report.png
pagetype: article
filedate: "2026-11-25"
---
*Key Insights from the 2026 Onapsis × Recorded Future Threat Report*

## Key Takeaways for Enterprise Leaders

- **•Time-to-Exploit Has Collapsed to 1–3 Days:** The median window between an SAP Security Note release and active public exploitation or proof-of-concept dropped from 489 days in 2021 to 24–72 hours in 2025–2026, rendering traditional quarterly patching obsolete.
- **Underground SAP Activity Doubled (+123% Surge):** Actor-operated channels — underground forums, messaging and leak sites — grew from 419 SAP-relevant  documents in 2023 to 933 in 2025.
- **Ransomware Syndicates Target the ERP Core Directly:** Ransomware interest broadened from 8 distinct groups in 2023 to 26 in 2025, with 30 unique groups appearing in SAP-relevant content across 2023 to H1 2026 (including Qilin, Scattered Spider, LAPSUS$, and ShinyHunters), with groups building custom scripts to terminate SAP services prior to encryption.
- **Stolen SAP Access Reaches a 23x Premium (up to $30K):** Underground listings highlight that high-privilege SAP access listings span $500 to $30,000, with high-value enterprise access at the top of that range on dark web forums – reaching roughly 23x standard enterprise network access (\~$1,300).
- **AI Accelerates Both Defense and Attack Cycles:** AI tools accelerate vendor patch research (\~220 forecast notes in 2026) while simultaneously empowering adversaries to reverse-engineer binaries instantly and target developer CI/CD supply chains (e.g., Mini Shai-Hulud worm / CVE-2026-45321).

## 1. Executive Overview: The Acceleration of SAP Threats

SAP serves as the digital backbone of the global economy, with its customers responsible for approximately 84% of world commerce. That centrality makes business-critical application platforms a primary target for financially motivated extortionists and sophisticated nation-state threat actors alike. According to the joint **[Days to Zero: 2026 SAP Threat Report](https://onapsis.com/threat-research/days-to-zero-sap-onapsis-recorded-future)** by Onapsis Research Labs and [Recorded Future](https://www.recordedfuture.com/), genuine SAP-relevant threat activity more than tripled between 2023 and 2025 – surging 211% from 791 to 2,458 distinct human-origin threat documents.

## 2. The Time-to-Exploit Collapse: 489 Days Down to 24–72 Hours

Historically, enterprise defenders relied on a predictable lag between when SAP released a Security Note and when threat actors could reverse-engineer the patch to build a working exploit. In 2021, the median time from an SAP Security Note release to verified public exploitation or proof-of-concept (PoC) was **489 days**. By 2025–2026, that median window collapsed to **1 to 3 days (24 to 72 hours)**. Across every SAP CVE with verified first-exploitation observations since April 2025, exploitation occurred between 0.3 and 24 days post-disclosure.

This speed compression is driven by the dual-use nature of generative AI and automated binary analysis tools. Onapsis Research Labs uses AI-augmented techniques to surface flaws faster – contributing to a record forecast of \~220 SAP Security Notes in 2026. However, threat actors utilize the exact same AI tools to analyze patch binaries, write automated exploits, and execute mass-scanning campaigns across internet-facing ERP instances within hours of disclosure.

## 3. Ransomware Groups Target the ERP Core Directly

In 2023, SAP-relevant ransomware activity was concentrated to 8 groups. Across 2023 to H1 2026, **30 distinct ransomware and extortion groups** appeared in SAP-relevant content, rising from 8 in 2023 to 26 in 2025 – including Qilin, Scattered Spider, LAPSUS$, ShinyHunters, BianLian, RansomEXX, and Akira. Cybercriminals recognize that encrypting or halting an ERP system delivers maximum financial leverage because downtime halts order-to-cash, manufacturing, and supply chain operations.

For example, the Qilin ransomware group updated its encryptor to explicitly terminate SAP background services before initiating file encryption. In a single 40-day window in early 2026, 11 distinct Qilin leak-site victims had exfiltrated files explicitly labeled ‘SAP’

## 4. Stolen SAP Access Reaches a 23x Dark Web Premium

Underground cybercrime broker pricing reflects the strategic leverage gained when compromising core business systems. While standard administrative access to generic enterprise networks averages \~$1,300, SAP listings span $500 to $30,000, with management-level access to named enterprises at the top of that range on dark web markets:

- U.S. Federal Logistics Agency: High-privilege access bundling SAP supply chain, contract, and procurement records was listed on Telegram for $12,000.
- Israeli Banking Institution: Direct management access to core SAP systems was offered on underground forums for $30,000.
- Egyptian Infrastructure Holding: SAP BusinessObjects administrative panel access for a $1B-$2B enterprise was auctioned for $1,000.

## 5. Action Plan: 3 Steps to Secure Your SAP Landscape

**1. Evolve from Patch Management to Exposure Management:** Quarterly patch cycles are obsolete when time-to-exploit is measured in days. Adopt threat-intelligence-driven risk prioritization – treating HotNews and High-Priority Notes on an emergency cadence while applying virtual compensating controls to lower-priority systems.

**2. Deploy Continuous Application-Layer Threat Detection:** When instant patching is impossible due to business continuity constraints, real-time application monitoring serves as the vital compensating control to catch zero-day exploitation attempts and unauthorized ABAP transports in real time.

**3. Secure the SAP Development Supply Chain:** Extend DevSecOps to custom ABAP code, SAP Joule AI prompts, and cloud build pipelines. Enforce dependency integrity checks and treat build environments with the same security controls as production.
