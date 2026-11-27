---
title: AI Joins the Industrial Attack Workflow
author: Levi Gundert; Chief Security; Intelligence Officer
url: https://www.recordedfuture.com/blog/ai-industrial-attack-workflow
hostname: recordedfuture.com
description: Insikt Group analyzes how GreenJuliett and AI frameworks like ARTEX are accelerating cyberattacks on OT networks.
sitename: recordedfuture.com
date: "2026-11-20"
fingerprint: "979882db7185d65b"
image: https://www.recordedfuture.com/blog/media_1addc3b8faa2fd80b1b3d308daeea7aa9751444e8.jpg?width=1200&format=pjpg&optimize=medium
filedate: "2026-11-27"
---
# AI Joins the Industrial Attack Workflow

On October 11 and 12, 2026, someone changed the defrost settings on refrigeration controllers at more than 700 retail locations in France. This resulted in fires, damaged equipment, and food losses estimated in the tens of millions of euros, highlighting the physical impacts of attacks against operational technology (OT). On November 9, France [attributed the attack](https://diplomatie.gouv.fr/fr/presse-et-ressources/decouvrir-et-informer/actualites/declaration-d-attribution-a-l-iran-de-cyberattaques-visant-la-france) to Shahid Kaveh, a unit of Iran's Islamic Revolutionary Guard Corps Cyber Electronic Command (IRGC-CEC). We track activity that likely belongs to an element of Shahid Kaveh as GreenJuliett.

GreenJuliett (also known as CyberAv3ngers and Bauxite) builds infrastructure aimed at internet-facing PLCs. And while that work continued through at least October 30, despite repeated public reporting on the group, the target set began to widen. Between August and October, we observed GreenJuliett-linked infrastructure scanning, or attempting to exploit, Fortinet FortiGate firewalls, edge devices that protect OT networks, in Bahrain, Israel, Jordan, Kuwait, Saudi Arabia, and Qatar. Our network data suggests the group is also working to add internet-of-things (IoT) and CCTV devices to its list.

While we have not independently tied GreenJuliett infrastructure to the refrigeration attacks, over the past three months, we have seen the group continue to target PLCs (programmable logic controllers), which are similar to the internet-exposed controllers the refrigerators in France used. We have also observed that AI is now part of how they work.

## **From Accounts to Infrastructure**

In October 2024, OpenAI [banned accounts](https://openai.com/index/disrupting-malicious-uses-of-ai-cyberav3ngers) it assessed as belonging to CyberAv3ngers. The operators had used ChatGPT to research default credentials for PLCs, compile lists of electricity companies and common PLCs in Jordan, and draft scripts against industrial protocols (such as Modbus TCP, a control protocol that allows PLCs to communicate quickly on local networks).

However, in 2026, the picture is different. In October, we found a configuration for LiteLLM (an open-source gateway that puts multiple AI models behind a single interface, suggesting a team-sharing model for access), alongside self-hosted chat applications built for Persian-language users, on infrastructure we assessed as likely used by GreenJuliett-linked operators. We also observed servers in the group's anonymization network communicating with infrastructure that hosts Anthropic's Claude.

While we have not confirmed specific instances of misuse in this research, both OpenAI and [Anthropic](https://anthropic.com/threat-intelligence-report-september-2026) have reported publicly on detecting and disrupting misuse by Iranian government operators. AI shortens the time it takes to identify vulnerable device types and write targeting scripts, and GreenJuliett has moved it from individual accounts into its operating environment.

## **AI As Operator**

GreenJuliett uses AI as an assistant. A separate class of tooling makes AI the operator, and it is already deployed at scale.

For example, ARTEX AI is one of eight offensive AI frameworks we track. Material recovered from exposed ARTEX servers shows how the agent works: Nmap, Masscan, and Nuclei for reconnaissance; Hydra and sqlmap for access; Chisel for tunneling. While the toolkit is familiar, the agent has now become the operator: On one server, archived transcripts show the agent issuing roughly 7,000 shell commands, recording more than 1,000 facts as it worked, and filing 54 findings.

As a result, ARTEX’s footprint roughly doubled in 30 days. We observed 1,506 servers running ARTEX on October 21 and 2,978 on November 19, hosted across 58 countries. (These are observed servers, not attacks or confirmed compromises.)

The steps GreenJuliett uses AI to speed up (finding exposed devices, testing credentials, writing scripts) are the steps these frameworks hand to an agent end-to-end, and the frameworks are openly available. The growing availability of ARTEX and other frameworks lowers the barrier for financially motivated and state actors alike to use AI agents to carry out end-to-end attacks. Agents can probe more environments for weaknesses to exploit, increasing the pace and volume of attempts. While the use of AI does not guarantee a successful attack, the machine-scale volume of attempts makes success somewhere more likely.

## **Deny Them the Easy Wins**

- **Take controllers off the internet:** CERT-FR [named](https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012) Copeland XWEB, Danfoss AK-SC and AK-SM, and Dixell XWEB refrigeration controllers in the French attacks. Use Recorded Future’s Attack Surface Intelligence to inventory which of your devices are exposed, then remove any controller that shouldn’t be publicly reachable.
- **Lock down edge devices:** Since the firewall in front of your OT network is now a target on its own, restrict FortiGate management interfaces to known addresses and keep firmware current.
- **Hunt based on GreenJuliett indicators:** The GreenJuliett infrastructure from this research is available to Recorded Future customers. Search your logs for it, going back to at least August.
- **Block the framework servers:** We track servers running ARTEX AI along with seven other AI automation frameworks every day. Alert on connections from them, and block them whenever there is no authorized testing underway. Most operators will use proxies instead of launching attacks directly from offensive AI framework servers, but blocking is worthwhile even for a small percentage of direct-attack servers.

## **The List Changes Every Day**

While none of these are quick fixes, blocking framework services is harder than it sounds. Only about one in six ARTEX servers we observed was present continuously for 30 days, and roughly 90 new ones appear on a typical day. A blocklist updated by hand each week is stale within days.

This is where defense should mirror the adversary's tactics. Choose one action that is high confidence, low consequence, and reversible (blocking inbound connections from a confirmed framework server qualifies) and let an agent take it without waiting for a person. Measure the results, then widen what the agent is allowed to do. We call this “earned autonomy.”

The adversary is handing its workflow to machines one step at a time. Which of your steps would you hand over first?

<sup>®</sup>researchers brief a live audience on the threat actors, tools, and infrastructure they’re tracking, and answer your questions.

[Join the Monthly Briefings →](https://recordedfuture.registration.goldcast.io/series/125d8a70-818e-4347-83d4-447885ba5702?utm_source=website&utm_medium=organic&utm_campaign=fy26-global-webinar-why-rf&utm_content=insikt)

*Insikt Group adheres to responsible disclosure procedures in conducting its research.*

## About Insikt Group<sup>®</sup>

*Recorded Future’s Insikt Group, the company’s threat research division, comprises analysts and security researchers with deep government, law enforcement, military, and intelligence agency experience. Its mission is to produce intelligence that reduces risk for customers, enables tangible outcomes, and prevents business disruption.*

## **Related Resources**

Explore expert insights, reports, and tools to strengthen your cybersecurity strategy.
