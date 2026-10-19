---
title: Thousands of refrigerator devices remain exposed following French cyberattack
author: David Jones
url: https://www.cybersecuritydive.com/news/thousands-refrigerator-devices-exposed-french-cyberattack/833117/
hostname: cybersecuritydive.com
description: The investigation points to a much wider risk for industrial systems across the globe.
sitename: Cybersecurity Dive
date: "2026-10-15"
fingerprint: c509180ace93ebc6
---
Days after a cyberattack targeting French supermarket refrigerators, thousands of controllers across the globe are visible online and at risk of compromise.

Hundreds of grocery stores in France were targeted in a sophisticated attack, in which hackers gained access to programmable controllers that regulate commercial refrigeration systems.

Hackers were able to manipulate controls inside the refrigerators, causing systems to overheat – and in some cases catch fire – leading to millions of dollars in damage.

Hackers targeted vulnerabilities in Danfoss AK-SM, Danfoss AK-SC, Copeland xweb and Dixell xweb controllers, according to ANSSI, France’s national cybersecurity agency.

About 350 instances of the Danfoss AK-SM 800A remained exposed as of Wednesday, down from more than 550 earlier this week, according to researchers from [Shadowserver Foundation](https://dashboard.shadowserver.org/statistics/iot-devices/time-series/?date_range=7&vendor=danfoss&model=ak-sm+800a&model=sm800a&limit=100&group_by=geo&stacking=stacked&auto_update=on). On Thursday, researchers said 1,173 [Copeland XWEB Pro and Evo](https://dashboard.shadowserver.org/statistics/iot-devices/time-series/?date_range=7&vendor=pulse+secure&limit=100&group_by=geo&stacking=stacked&auto_update=on) instances remain exposed to the internet.

A [report released Wednesday](https://url.us.m.mimecastprotect.com/s/GdtRCG6Y9jf2wVrznFKfmGsB7tod?domain=censys.com/) by Censys shows more than 2,900 hosts using the Danfoss StoreView panel are visible online. A separate report from [Security Scorecard](https://securityscorecard.com/blog/hackers-turned-supermarket-refrigerators-into-heaters/) shows over 5,200 StoreView instances visible across more than 4,600 public IP addresses.

### Security afterthought

Security researchers say the problems begin in the design of these systems, where security is not a top priority.

“People who design systems, people who build systems, they usually believe that people will be well behaved,” Aleksandr Yampolskiy, co-founder and CEO of Security Scorecard, told Cybersecurity Dive. “But hackers are not well behaved.”

High-severity vulnerabilities in Danfoss controllers were publicly disclosed in an August report by Claroty, a firm that specializes in industrial cybersecurity. Researchers found high-severity flaws in the web management interface of Danfoss systems that could allow an attacker to take control of a device.

The vulnerabilities were tracked as [CVE-2025-41451](https://nvd.nist.gov/vuln/detail/cve-2025-41451) and [CVE-2025-41452](https://nvd.nist.gov/vuln/detail/cve-2025-41452). Researchers originally alerted Danfoss to the flaws in 2025 before releasing the report under a coordinated disclosure process. The manufacturer patched the flaws and issued additional guidance.

The attacks impacted hundreds of supermarkets across multiple chains, including Carrefour, Monoprix, Cooperative U and Intermarche.

A spokesperson for Copeland confirmed that a vulnerability was found in discontinued end-of-life controllers. The company is actively working with impacted customers to mitigate the risk.

French authorities are continuing to investigate the attack and working with various industries to implement remediation and prevention measures. They said further attacks remain a strong possibility, and they are particularly focused on large retailers.

“The complex system that delivers our food is fragile but often doesn’t receive the attention it deserves,” said John Hultquist, chief analyst at Google Threat Intelligence Group. “We must treat this supply chain as the critical infrastructure it is.”

*Editor’s note: Updates with additional information from Shadowserver Foundation.*
