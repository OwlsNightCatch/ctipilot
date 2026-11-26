---
title: "Cold Chain Attack: Unpatched Danfoss Controllers Exploited"
author: TDR Team
url: https://www.sekoia.com/blog/the-cold-chain-on-fire-unpatched-danfoss-controllers-exploited
hostname: sekoia.com
description: Sekoia TDR analyzes attacks on exposed Danfoss controllers in European supermarkets, with honeypot findings and attribution to an Iran-linked unit.
sitename: "The cold chain on fire: Unpatched Danfoss controllers exploited"
date: "2026-11-10"
fingerprint: "3110829102e9d5e0"
language: en
image: https://cdn.prod.website-files.com/69b190e7f47e4c44b0ee07d8/6af3344206c86a787d5bb897_blog-the-cold-chain-on-fire-unpatched-danfoss-controllers-exploited-img-cover%20(1).webp
pagetype: website
filedate: "2026-11-26"
---
## Context

Between 11 and 13 October 2026, **hundreds of supermarkets across France**, including stores operated by Intermarché and Coopérative U running unpatched Danfoss refrigeration control systems **were affected by a large-scale cyberattack**. According to directors of impacted retailers, the potential financial impact could reach tens of millions of euros, through food spoilage and business interruption, while images of discarded goods drew significant public backlash.

More recently, during the night between 1-2 November, a **second wave of attacks** impacted refrigeration systems across around **a dozen European countries**, including Belgium, the Netherlands, Germany and Sweden, with the same modus operandi and final impact: food spoilage and business interruption. The same night, cold rooms at three sites of the French Blood Establishment were reprogrammed to reach 110°C before staff intervened.

This blogpost is a follow-up investigation based on a private Sekoia report prepared on 13–14 October 2026 and shared with our clients and partners on 15 October 2026. It incorporates **observations from the second wave of attacks**, data collected through Sekoia honeypots, and our analysis of the exploitation techniques targeting exposed Danfoss controllers.

It also reviews the alleged **NoName057(16) / Z-Pentest claim,** a claim Sekoia assesses with doubts - see dedicated part below. Finally, it discusses the available attribution hypotheses and outlines the security measures that can help reduce the risk to exposed refrigeration and other industrial control systems.

## Sekoia observations

### Impacts

Following Sekoia assessment and despite its impact, these two attack campaigns weren't sophisticated. The main issue exploited by the threat actor was the **direct exposure of unpatched Danfoss controllers** to the public Internet. Most of the instances were running outdated firmware prone to multiple vulnerabilities, such as those [disclosed in August by Team82 of Claroty](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers).

During these attacks, the threat actor automatically modified **temperature settings**, **defrost cycles**, and **alarm thresholds** to evade detection by maintenance personnel for several hours. The threat actor didn't exploit any code execution flaw, which **prevented further damage** against the controllers, such as wiping their file system.

According to multiple sources, the threat actor **reversed the temperature settings** of the refrigeration systems, increasing them from 50° to 80°, which reportedly caused a fire in at least one instance.

Following the first campaign, we wanted to know the impact of the campaign. Sekoia observed via Censys more than 2,700 Danfoss systems exposed worldwide as of October 11, including approximately 1,700 in France. By 4:00 p.m. on October 12, roughly **half of the previously exposed French systems were no longer publicly accessible**. This initially raised concerns about the possibility that the controllers had been wiped. However, closed-source intelligence indicated to Sekoia that only the refrigeration control system parameters were modified.

Therefore, the decline in publicly accessible devices may instead **be attributable to remediation efforts** undertaken by the victims. At least one victim, identified through its WHOIS records and associated with more than 70 Danfoss instances that had gone offline, confirmed to trusted journalists in contact with Sekoia that it had been affected by the attack campaign.

**Sekoia reached out to its trusted contacts** to determine whether they had observed any reconnaissance activity or signs of the attack campaign against these IP addresses.

After sharing the list of the 70 Danfoss instances known as compromised, along with the ports associated with Danfoss web interfaces, a **trusted partner provided us with several IP addresses linked to this attack campaign**, covering activities ranging from initial device reconnaissance to the attacks themselves.

According to our partner, **this first campaign targeted mostly devices located in France**, and the threat actor began conducting reconnaissance more than a week before launching the attack campaign against French targets.

### Honeypots

On Monday the 12th, we deployed four honeypots of **Danfoss 800A** web interfaces in France and the Netherlands. The following day, one of these honeypots received **unauthenticated HTTP requests** attempting to enumerate System Manager units and their associated IP addresses via the **read\_units** action, as shown below.

It is worth noting that these requests may allow a threat actor to retrieve **valuable information** about the controller, such as the **identity** and the **location** of the store where it is installed, provided that this information is included in the controller's configuration.

Over the following weeks, we observed multiple requests targeting the **xml.cgi** endpoint from 26 unique IP addresses. These requests ranged from reconnaissance activities using the **read\_units** or **read\_date\_time** actions to **password-spraying attempts** targeting the Supervisor and admin accounts with the password "12345".

Following a quiet period from October 26 to 31, **we observed exploitation attempts on November 1, potentially linked to the second** wave of attacks, as shown below.

### Exploitation attempts

#### Code of the day, the first suspect.

Following the first attack campaign, widespread speculation emerged online suggesting that this campaign may have exploited **CVE-2025-41450**, also known as the "code of the day" vulnerability and disclosed by the cybersecurity firm [Claroty](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers).

This vulnerability compares the first five chars of the password XML attribute against a digit code generated from the current date. If these chars match the generated code, authentication is bypassed even without providing a valid username, **granting full access to the device's API endpoints**.

Although **we could not confirm** whether this vulnerability was exploited during the first campaign, the requests made to the **read\_date\_time** action in our honeypot logs may be linked to the exploitation prelude of CVE-2025-41450, as threat actors would need to determine each system date before attempting to exploit it.

Although we observed several requests targeting the **read\_date\_time** action in our honeypots between October 19 and 25, 2026, no corresponding attack campaign has been confirmed through publicly available sources. As a result, we cannot determine whether these requests originated from malicious threat actors or security researchers simply actively probing internet-exposed Danfoss instances.

#### Possible exploitation linked to the second wave.

The only confirmed exploitation attempt we observed targeted four of our honeypots on November 1, between 10:00 p.m. and 10:30 p.m., **during the second campaign's timeframe**. During this attempt, a threat actor tried to exploit a **non-public vulnerability** aimed at renaming a user account from the IP addresses `178.83.226[.]215` and `37.16.75[.]128`. Although the request was blocked, its characteristics led us to suspect that it may have been part of a more complex exploit chain.

The following day, equipped with **GLM 5.3** and Danfoss firmware images downloaded from the company's website, we set out to understand the purpose of this request and determine whether it might fit into a broader exploit chain.

Within minutes, the model confirmed that the captured request can allow a threat actor to rename any user account simply by providing its numerical identifier, without any authentication. In the exploit observed in the wild, the threat actor targeted user ID 1, an account with full administrative privileges.

Why is this request important? Because the threat actor needs to know the account's login - as a primitive -  to **reset its password through a second unauthenticated request**, which was not captured because the first request was blocked. Since the login name can change, the attacker must first set it to a known value to ensure the password-reset exploit works reliably.

With the knowledge of one of these vulnerabilities, a list of IP addresses associated with Internet-exposed Danfoss devices, and HAR files capturing configuration changes performed during a browsing session of a Danfoss web interface, **a threat actor could leverage an LLM to develop a reliable exploit code capable of enabling a large-scale attack changing parameters of hundreds controllers within minutes**.

### Attribution to Iran’s Islamic Revolutionary Guard Corps

On 9 November 2026, **French authorities** [**attributed the operation to Iran’s Islamic Revolutionary Guard Corps**](https://cert.cyber.gouv.fr/uploads/CERTFR-2026-CTI-009.pdf), specifically the unit “**Shahid Kaveh**”, linked to the Islamic Revolutionary Guard Corps Cyber Electronic Command (IRGC-CEC). This unit is most known under the persona they use, the most known is CyberAveng3rs (aka Soldiers of Solomon, Mr. Soul, Cyber Isnaad Front).

The group is notably known for its attack on U.S. water and wastewater critical infrastructure. In late 2023, they gained prominence by compromising internet-exposed Unitronics PLCs at the Municipal Water Authority of Aliquippa. In 2026, the group escalated operations by exploiting Rockwell Automation vulnerabilities to deploy custom ICS malware, culminating in a July 2026 coordinated disruption of over 30 Minnesota water systems.

This attribution is **consistent with one of our attribution hypothesis** we detailed on a private report sent on 15 October 2026 to our clients and partners:

> Iran-nexus threat actors have a well-documented track record of **targeting Internet-facing industrial control systems**. In late 2023, US authorities [attributed](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a) attacks on domestic water utilities to CyberAv3ngers, a group affiliated with Iran's Islamic Revolutionary Guard Corps, which compromised exposed Unitronics controllers by exploiting default credentials. **‍**

> **Previous precedents involve Danfoss controller targeted in Israel and in the USA, both geopolitical adversaries of Iran**.  In 2022, approximately [40 Israeli supermarkets](https://www.danfoss.com/en/service-and-support/articles/dcs/tech-insider-october-2025/#tab-relevant-for-all-categories) operating Danfoss controllers were compromised. More recently, in late August 2026, at least [six US military bases in mainland USA](https://signalandsilence.substack.com/p/i-think-someone-hacked-the-commissary) were impacted by refrigeration failures, with freezers forced into defrost mode in the same way observed in France. While neither incident was formerly attributed to Iran, both **target profiles closely align with the strategic priorities of Iranian offensive cyber operations**, although no technical indicators currently link this incident to that cluster.

> The geopolitical context also offers a plausible motive: France’s [deployment of troops](https://www.lemonde.fr/en/international/article/2026/09/26/france-sending-military-resources-to-saudi-arabia-brings-discreet-defense-ties-into-spotlight_6757983_4.html) and air-defence systems to the Yanbu oil terminal in Saudi Arabia, announced on 24 September 2026, could be perceived by Tehran as direct support to an adversary.

#### What about the NoName057(16) / Z-Pentest (opportunistic) claim?

Sekoia assesses the claim by NoName057(16) and Z-Pentest as unsubstantiated, given NoName057(16)’s documented history of misleading claims of responsibility. NoName057(16) is primarily associated with DDoS operations against Ukrainian and European entities, rather than ICS intrusions or physical sabotage. The credentials released are characteristic of aggregated infostealer logs rather than a database exfiltration.

## Conclusion

The October and November incidents demonstrate how Internet-exposed and insufficiently secured industrial control systems (ICS) can enable disruptive attacks with significant operational and economic consequences, without requiring highly sophisticated tradecraft.

Unauthenticated vulnerabilities, outdated firmware, insufficient network segmentation and exposed administration interfaces created conditions in which threat actors could remotely alter refrigeration parameters across multiple sites.

Our investigation also illustrates how **generative AI (LLM) can lower the barrier to entry for attacks on small-size ICS, IOTs and building automation systems**. By combining publicly available firmware and exposed devices, an attacker may be able to analyse undocumented functionality, find bugs, and **develop reliable exploits much faster than before**. This increases the risk not only of targeted hybrid operations, but also of opportunistic campaigns and copycat activities.

Operators should remove refrigeration controllers and other ICS devices from direct Internet exposure, restrict remote administration through secure access mechanisms, replace default credentials, apply available firmware updates and monitor authentication and configuration changes. Responsibility for these measures is often distributed across asset owners, integrators, maintenance providers and equipment vendors, but **this division of responsibility should not result in persistent exposure**.

Available evidence shows similarities in the timing, the infrastructure, the targeting and observed tradecraft across the October and November waves, suggesting that they **may have been conducted by the same threat actor**.

**Sekoia’s TDR team will continue monitoring the exposed refrigeration ecosystem and operating honeypots that replicate the observed controller configurations to detect and analyse renewed reconnaissance or exploitation activity.**
