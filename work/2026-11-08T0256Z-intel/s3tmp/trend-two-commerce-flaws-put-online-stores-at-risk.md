---
title: "Two Ways In Before the Holiday Rush: Exploited Adobe Commerce Flaws Put Online Stores at Risk | TrendAI (US)"
url: https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/two-commerce-flaws-put-online-stores-at-risk
hostname: trendaisecurity.com
description: Two actively exploited Adobe Commerce and Magento Open Source vulnerabilities (CVE-2026-48356 and CVE-2026-75650) are giving attackers code execution on ecommerce store servers just as holiday shopping season begins. This entry breaks down how each attack works and what store operators should do to patch and check for compromise.
sitename: TrendAI
date: "2026-11-06"
fingerprint: fcce84cbeab0aed4
---
#### Key Takeaways

- Two critical Adobe Commerce and Magento Open Source flaws are being exploited going into the holiday shopping season. One is PolyShell (CVE-2026-48356), a dangerous file upload flaw that the Cybersecurity and Infrastructure Security Agency (CISA) added to Known Exploited Vulnerabilities (KEV) on October 27. The other is StyleSmuggler (CVE-2026-75650), used in September to install a remote access trojan on stores.
- Both give attackers code execution on the store server. From there they can read store secrets, plant web shells and inject card skimmers into checkout.
- Patching closes the door but does not remove an attacker already inside. Stores that were exposed need to be checked for compromise.

Holiday shopping season is probably one of the worst times for ecommerce platforms to get hit. Naturally, the opposite is true for cybercriminals who find the season the perfect time to strike. Over the past few months, flaws in popular ecommerce software Adobe Commerce and Magento Open Source Attacks have moved from disclosure to active exploitation, to the detriment of online stores. PolyShell ( [CVE-2026-48356](https://nvd.nist.gov/vuln/detail/cve-2026-48356) ), a file upload flaw, has now been reported by CISA as under attack. It follows the same track as StyleSmuggler *(* [CVE-2026-75650](https://nvd.nist.gov/vuln/detail/cve-2026-75650) *)*, already linked to a coordinated campaign that planted a remote access trojan on live stores.

Both give attackers a foothold on the store server itself, opening the door to stolen secrets or skimmers straight off the checkout page. While the way in may differ, the outcome is the same. We break down what exploiting these flaws does in this entry.

## **PolyShell (CVE-2026-48356): Polyglot uploads through guest carts**

CVE-2026-48356, which researchers at Sansec have named  [PolyShell](https://sansec.io/research/magento-polyshell) , is an unrestricted upload flaw in Adobe Commerce and Magento Open Source. According to Sansec, attackers can send unauthenticated requests to the guest cart API and attach a disguised image file that also contains PHP code. Because the upload check only verifies the image header, the file is saved on the store server, where it can be run depending on how the web server is configured.

Adobe’s  [bulletin](https://www.adobe.com/trust/security/products/commerce/apsb26-73.html)  rates the flaw Critical and lists its impact as privilege escalation. Sansec describes the flaw as enabling code execution, and attackers have used it to plant backdoors and inject malicious scripts into checkout pages. In March, they  [reported](https://sansec.io/research/polyshell-mass-attack-wave)  a mass attack wave that compromised 471 stores in a single hour.

## **StyleSmuggler (CVE-2026-75650): PSK Agent on stores**

CVE-2026-75650 is a critical unauthenticated server-side template injection (SSTI) vulnerability that leads to remote code execution (RCE)**.** A request to /paypal/transparent/response/ writes attacker PHP into var/report/, and a follow-up GraphQL request with crafted styles values loads and runs it. A 3,313-byte script then finds a writable location and launches PSK Agent, a 10.5 MB obfuscated Go remote access trojan with command execution, host discovery, and SOCKS5 proxying. Some victims also got a 910-line PHP web shell (t4.php placed as zer4.php, including under pub/media/). Compromised stores announce themselves through DNS callbacks that include the victim's hostname.

Imperva  [assesses](https://www.imperva.com/blog/stylesmuggler-exploitation-deploys-psk-agent-rat-against-magento-stores/)  with moderate confidence that the PSK Agent operator is likely Chinese-speaking and found no link to a named threat group. Adobe's hotfix VULN-39341 closes the entry point. Imperva observed a coordinated campaign from September 9 to 13 across Western Europe, North America, and Asia-Pacific.

## **What store operators should do**

Patching is the first crucial step. However, this does not undo damage from an attacker who already got in before the patch. Affected stores need to check their systems for signs they were already compromised, not just update and move on.

Here is a list of what to do:

- Make sure the web server will not run PHP from media and upload directories such as pub/media/.
- Hunt for compromise: unexpected files under pub/media/custom\_options/quote/ and pub/media/, files named zer4.php or t4.php, new files in var/report/, PSK Agent processes, and changes to cron, system, and CMS blocks.
- Check checkout pages for injected scripts, and rotate secrets in app/etc/env.php if the server may have been reached.

## **How TrendAI™ can help**

- **Virtual patching on the network:** TrendAI Vision One™ TippingPoint™ protection for CVE-2026-48356 was released on November 5.
- **Network detection and response:** TrendAI Vision One™ Network Security detects PolyShell upload attempts that exploit CVE-2026-48356.
- **StyleSmuggler (CVE-2026-75650):** TrendAI Vision One™ Endpoint Security, Network Security and TippingPoint™ protection is available.
