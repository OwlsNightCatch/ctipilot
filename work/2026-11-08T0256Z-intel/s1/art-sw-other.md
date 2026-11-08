---
title: "In Other News: Trezor Implant, LLMJacking Bills Hit $1M, SAP Flaws Weaponized Within Days"
author: SecurityWeek News
url: https://www.securityweek.com/in-other-news-trezor-implant-llmjacking-bills-hit-1m-sap-flaws-weaponized-within-days/
hostname: securityweek.com
description: "Noteworthy stories that might have slipped under the radar: Synology warns about NAS ransomware attacks, Flowise ‘hello’ attacks, Chainalysis breach impact expands."
sitename: SecurityWeek
date: "2026-11-06"
categories: ['Artificial Intelligence']
fingerprint: "3e3231590c8ff7c9"
---
**SecurityWeek’s weekly cybersecurity news roundupoffers a concise overview of important developments that may not receive full standalone coverage yet remain relevant to the broader threat landscape.**

This curated summary highlights key stories across vulnerability disclosures, emerging attack methods, policy updates, industry reports, and other noteworthy events to help readers stay well-informed about the evolving cybersecurity environment.

**Here are this week’s highlights:** 

**Anthropic adds security center, admin controls to Claude Enterprise**

Anthropic has rolled out [additional security and administration capabilities](https://claude.com/resources/articles/claude-enterprise-security-updates) for Claude Enterprise, including a security center (in beta) that checks an organization’s Claude configuration for chat, Cowork and Claude Code against settings Anthropic recommends. Inference hooks, now generally available, route prompts and tool calls to an organization’s existing data loss prevention and security tools for inspection, while a centralized console (also in beta) lets companies handle single sign-on, SCIM and other settings across all their Claude organizations from one place.

**Fake OpenAI and SpaceX event invites phish Microsoft and Google accounts**

Push Security has documented a [phishing campaign](https://pushsecurity.com/blog/ai-themed-fake-event-campaign-analysis) built around fake registration pages for OpenAI, SpaceX and Anthropic events, which dangle rewards such as three months of ChatGPT Pro or Grok Heavy to get marketing employees to sign in with their work accounts. The Microsoft option launches a device code phishing flow run through the Kali365 phishing-as-a-service platform. Push links the operator, with medium-high confidence, to earlier fake Zoom event pages and says the campaign relies on Google and Zapier short links, Cloudflare challenges and domains swapped out every few weeks to avoid detection.

**Chainalysis breach also exposed password hashes and tokens**

Chainalysis has [widened](https://www.chainalysis.com/blog/security-incident-october-30/) its breach disclosure, saying it discovered on November 2 that names, usernames, password hashes and live tokens for all its users had been exposed, after [initially reporting](https://www.securityweek.com/chainalysis-discloses-data-breach-following-ai-driven-cyberattack/) that only non-sensitive data was accessed. The company has since taken several products offline, including its KYT transaction monitoring service after detecting abnormal activity, and is reaching out to customers whose KYT accounts show signs of unauthorized access.

**Google hands Agent Substrate, gVisor to CNCF for sandboxing AI agents**

Google is [donating](https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html) Agent Substrate, an open source orchestration layer on top of Kubernetes for running large numbers of isolated AI agent sessions, and gVisor, its open source application kernel, to the Cloud Native Computing Foundation (CNCF) as Sandbox projects. When an agent goes idle, Agent Substrate saves its state to storage and can bring it back in under 500 milliseconds. gVisor handles system calls in user space so that untrusted, AI-generated code doesn’t interact directly with the host kernel. According to Google, placing both projects under the CNCF gives the community a shared, vendor-neutral base for agent infrastructure that can run on any Kubernetes cluster meeting conformance standards.

**‘Hello’ messages hide Chinese-language attack framework targeting Flowise**

Era researchers have detailed [Greeter](https://era.security/blog/greeter-flowise-ai-infrastructure-attack), a Chinese-language exploitation framework that bombarded Flowise honeypots with thousands of chat messages reading only “hello” while abusing an old code injection flaw (CVE-2024-58351) to execute commands. The framework mapped the host, queried cloud metadata services, searched for SSH keys and other credentials, tried to set up persistence, and tested whether it could run payloads from memory. Era counted 4,372 Flowise instances exposed online, and of those whose version it could identify, 703 lacked authentication and 46 appeared to share the vulnerable setup used in its honeypots.

**LLM Mixers turn hijacked enterprise AI access into underground business**

Mandiant says it [investigated several LLMJacking cases](https://cloud.google.com/blog/topics/threat-intelligence/llmjacking-monetizing-compromised-cloud-models) this year in which attackers took over companies’ access to AI models, generating fraudulent bills of more than $100,000 in a day and as much as $1 million in total at some organizations. Initial access mainly came from stolen or exposed cloud credentials and API keys, and in one intrusion the attackers exploited a LiteLLM vulnerability (CVE-2026-40217) to upgrade ordinary keys to full admin credentials. Google Threat Intelligence Group also found hijacked access being sold through so-called LLM Mixers, including the Jet Night token routing service, which it believes uses stolen keys to offer unlimited plans with claimed frontier model access for around $60 a month.

**CryptoBilis-sold Trezor allegedly fitted with seed-stealing implant**

Trezor is telling customers who bought its hardware wallets from CryptoBilis since March 2026 to transfer their funds to a freshly created wallet with a new seed, after a buyer reported [finding an implant inside a Trezor Safe 5](https://trezor.io/blog/news/implant-reported-in-a-trezor-sold-by-cryptobilis) purchased from the former Southeast Asian reseller, which also sold Ledger devices that were found to have been [tampered with](https://www.securityweek.com/86-million-crypto-heist-linked-to-ledger-signer-hardware-implant/). According to the report, which Trezor has not yet verified, an added circuit board fitted with a cellular module and antenna captures the recovery phrase displayed on screen and transmits it over a mobile network whenever the device is connected. No stolen funds have been reported.

**Harvard alumni and donor data from 2025 breach added to HIBP**

[Have I Been Pwned](https://haveibeenpwned.com/Breach/Harvard) has loaded roughly 851,000 unique email addresses from Harvard University’s November 2025 [breach](https://www.securityweek.com/alumni-student-and-staff-information-stolen-from-harvard-university/), an incident subsequently tied to a ShinyHunters extortion bid. The records come from Harvard’s alumni and fundraising systems and contain detailed profiles of donors, alumni and parents, as well as some faculty, staff and students, including names, contact details, birth dates and places, employers, ethnicities, marital statuses and donation histories.

**SAP exploitation window shrinks to days as ransomware interest grows**

Onapsis and Recorded Future [report](https://go.onapsis.com/threat-report/days-to-zero-sap-onapsis-recorded-future-2026) that for [SAP vulnerabilities](https://www.securityweek.com/topics/sap) patched in 2025 and 2026, the median gap between a security note’s release and the first verified exploitation or public proof-of-concept was one to three days, down from 489 days for flaws patched in 2021. Ransomware and extortion groups showing up in SAP-related content grew from 8 in 2023 to 26 in 2025, and SAP CVEs with confirmed in-the-wild exploitation or public proof-of-concept code doubled from 9 to 18 between the end of 2023 and mid-2026. The study, drawing on over 1.2 million threat intelligence events, also tracked underground listings for SAP access priced from $500 to $30,000.

**Synology flaw patched in 2024 now exploited in ransomware attacks**

[Synology warns](https://www.synology.com/en-global/company/news/article/C3RB3R/Synology%20urges%20users%20to%20update%20DSM%20following%20ransomware%20attacks%20on%20outdated%20DSM%20versions) that attackers are abusing a vulnerability fixed in December 2024 to hit devices still running outdated DSM releases, with the goal of encrypting data and extorting victims. The company has not identified the specific flaw beyond pointing to its [Synology-SA-24:20](https://www.synology.com/zh-tw/security/advisory/Synology_SA_24_20) advisory. Synology recommends that anyone on a vulnerable release update DSM right away and turn on automatic updates.

**Alleged Nomad Bridge exploiter appears in US court after extradition**

Alexander Gurevich, a 49-year-old Israeli national now known as Alexander Block, [appeared in a US court](https://www.justice.gov/opa/pr/israeli-national-extradited-face-charges-stealing-nearly-3m-virtual-currency-heist) for the first time on October 30, a day after Israel extradited him to face charges that he [exploited the Nomad Bridge](https://www.securityweek.com/nearly-200-million-stolen-cryptocurrency-bridge-nomad/) smart contract in August 2022 to take virtual currency worth roughly $2.89 million. According to the indictment, he swapped the stolen WBTC and WETH for other cryptocurrencies and spread them across multiple addresses to obscure their origin. The money laundering charge alone carries a maximum of 20 years in prison.

**Related**: [In Other News: Anthropic Breach Dispute, UEFI Flaw Hits Most Servers, Cloudflare AI Data Leak](https://www.securityweek.com/in-other-news-anthropic-breach-dispute-uefi-flaw-hits-most-servers-cloudflare-ai-data-leak/)
