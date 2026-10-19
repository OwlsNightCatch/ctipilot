---
title: Cl0p ransomware launches new large-scale data theft campaign
author: Amar Ćemanović
url: https://cyberinsider.com/cl0p-ransomware-launches-new-large-scale-data-theft-campaign/
hostname: cyberinsider.com
description: Hackers linked to Cl0p ransomware are exploiting a critical flaw in PTC Windchill and FlexPLM to deploy web shells and steal enterprise data.
sitename: CyberInsider
date: "2026-07-24"
categories: ['Data Breach', 'News', 'Ransomware', 'Security']
fingerprint: a41744d3080de959
---
Hackers believed to be Cl0p ransomware operatives are exploiting a critical flaw in PTC Windchill and FlexPLM to deploy web shells and steal sensitive enterprise data.

While the threat actor has not been identified with absolute certainty, the observed tactics closely match those used in previous data theft campaigns attributed to the Cl0p ransomware gang.

ReliaQuest [reported](https://x.com/ReliaQuestTR/status/2079963221365055890) that it has observed active exploitation of CVE-2026-12569, a critical unsafe deserialization flaw affecting PTC Windchill and PTC FlexPLM. The vulnerability allows unauthenticated remote code execution, enabling attackers to deploy JSP web shells, execute commands, and exfiltrate sensitive product data.

ReliaQuest said the tradecraft closely resembles Cl0p’s previous campaigns targeting enterprise applications that store high-value corporate data.

PTC Windchill and FlexPLM are Product Lifecycle Management (PLM) platforms used to manage products from design through manufacturing. The software is widely deployed across the aerospace, defense, automotive, manufacturing, retail, and medical technology sectors. PTC says its products are used by more than 30,000 organizations worldwide, including over 1,500 FlexPLM customers.

PTC [released patches](https://www.ptc.com/en/about/trust-center/advisory-center/active-advisories/windchill-flexplm-rce-vulnerability) for CVE-2026-12569 on June 17, accompanied by a private advisory urging customers to review their environments for signs of compromise. After warning customers of “heightened threat activity” on June 26, the U.S. Cybersecurity and Infrastructure Security Agency (CISA) added the flaw to its Known Exploited Vulnerabilities (KEV) catalog and ordered federal agencies to secure affected systems within three days.

Previously, the Federal Office for Information Security (BSI) [contacted PTC customers directly](https://www.heise.de/en/news/WTF-Police-responded-on-Saturday-night-due-to-a-zero-day-11221590.html) by phone and email, urging them to apply the updates immediately. Earlier this year, the agency issued similar warnings over another critical Windchill vulnerability, CVE-2026-4681.

The activity fits Cl0p’s long-standing strategy of exploiting zero-day vulnerabilities in widely used enterprise software to steal sensitive data. Previous campaigns targeted Accellion FTA, SolarWinds Serv-U, GoAnywhere MFT, [MOVEit Transfer](https://cyberinsider.com/active-exploitation-of-new-moveit-transfer-auth-bypass-flaw-detected/), [Cleo](https://cyberinsider.com/clop-ransomware-claimed-november-attack-at-blue-yonder/), and, most recently, an [Oracle E-Business Suite](https://cyberinsider.com/clop-ransomware-exploits-oracle-ebs-zero-day-in-data-theft-campaign/) zero-day that compromised numerous organizations, including [The Washington Post](https://cyberinsider.com/washington-post-breach-exposed-financial-data-of-nearly-10k-staff/), [Logitech](https://cyberinsider.com/logitech-customer-data-exposed-in-zero-day-flaw-cyberattack/), and [Estée Lauder](https://cyberinsider.com/estee-lauder-discloses-data-breach-tied-to-oracle-e-business-suite-attacks/).

Rather than relying solely on file encryption, Cl0p primarily extorts victims by threatening to publish stolen data on its leak site, often making it available via BitTorrent if ransom demands are not met.

ReliaQuest urges organizations to apply PTC’s security update (CS473270) immediately and, where possible, restrict Windchill and FlexPLM access behind a VPN or trusted access gateway. If a compromise is suspected, affected servers should be isolated, forensic evidence preserved, exposed credentials rotated, and systems thoroughly investigated before being returned to production.

## Leave a Reply Cancel reply
