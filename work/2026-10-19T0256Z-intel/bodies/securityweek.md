---
title: Supermarket Refrigeration Attack Widens to Copeland, Dixell Controllers
author: Eduard Kovacs
url: https://www.securityweek.com/supermarket-refrigeration-attack-widens-to-copeland-dixell-controllers/
hostname: securityweek.com
description: Roughly 700 French supermarkets were hit by the cyberattacks, for which no group has claimed responsibility.
sitename: SecurityWeek
date: "2026-10-15"
categories: ['ICS/OT', 'Incident Response']
fingerprint: "74942316c219ebca"
---
**The cyberattack that disrupted refrigerationat hundreds of French supermarkets this week also affected equipment from Copeland and its Dixell brand, according to France’s national cybersecurity agency ANSSI.**

ANSSI’s CERT-FR first warned on October 12 of numerous compromises involving Danfoss AK-SM and AK-SC series refrigeration controllers. A day later, the agency updated its [alert](https://cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-012/) to include Copeland XWEB and Dixell XWEB systems.

Copeland initially declined to confirm the agency’s findings, but it has since acknowledged a vulnerability. “We are currently working with impacted customers to mitigate the risk,” the company said.

This summer, Claroty detailed [flaws in Danfoss’s AK-SM 800A](https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers), along with [23 vulnerabilities](https://claroty.com/team82/research/chilling-discoveries-unpacking-vulnerabilities-in-copeland-xweb-pro-controllers) in Copeland’s XWEB Pro controller. Copeland patched them in a firmware update.

It is still unclear how the attackers gained access. The CERT-FR alert does not link the compromises to any specific vulnerability, and neither Danfoss nor French authorities have tied the attack to the flaws Claroty disclosed.

Danfoss said most of the affected devices are older AK-SM 800 and AK-SC 355 systems, which have reached end of life and are no longer patched. The vendor stopped supporting the AK-SM 800 in May 2021, and the AK-SC 355 was discontinued in 2016. Some current AK-SM 800A controllers that were running outdated firmware were also affected.

CERT-FR has urged operators of the affected controllers to take them off the internet and restore remote access only through a secure VPN or protected network. Filtering connections by IP address is acceptable only as a temporary emergency measure, the agency said.

For compromised end-of-life devices, a factory reset alone is not enough as the device will remain vulnerable and is likely to be compromised again if it stays exposed.

## Hundreds of supermarkets affected in France

Supermarket chains that have confirmed being affected include Carrefour, Coopérative U, E.Leclerc, Intermarché, and Monoprix.

About 700 of France’s roughly 10,000 supermarkets were affected, Finance Minister Roland Lescure told lawmakers on Tuesday. Earlier reports had put the number at 300-350.

At Intermarché, about 150 stores were affected, according to owner Les Mousquetaires. Refrigeration units there ran at 50 degrees Celsius for six hours, and all the food was discarded. Carrefour said 80 of its stores were impacted.

Coopérative U CEO Dominique Schelcher said 80 of the group’s stores were targeted, but only a minority had to throw away products. Two supermarkets in Alsace reported combined losses of €270,000 ($300,000).

The Paris prosecutor’s office, whose cybercrime unit has opened an investigation, said the attack caused fires in addition to food losses. According to Le Monde, the attackers lengthened defrost cycles from one hour to as many as eight, which delayed alarms.

Investigators are reportedly puzzled by the lack of either a claim of responsibility or a ransom demand, [Reuters](https://www.reuters.com/legal/litigation/investigators-hunt-french-supermarket-fridge-hackers-no-claim-responsibility-2026-10-13/) reported, citing a source familiar with the probe.

Sekoia’s Félix Aimé told Reuters that stores in Spain, Portugal, Poland, Germany, and Belgium were also affected, but did not provide details. The Dutch NCSC said it did not believe a [cyberattack against Ahold Delhaize](https://www.securityweek.com/cyberattack-prompts-ahold-delhaize-to-disconnect-systems/) was connected to the attack on refrigerators.

[Censys counted](https://censys.com/blog/frostbitten-in-france-a-danfoss-storeview-internet-exposure-report/) nearly 3,000 internet-exposed Danfoss StoreView control panels on October 11, more than 1,800 of them in France. By October 14, the French count had dropped to 537, while the number elsewhere barely changed.

Patched and unpatched versions disappeared at roughly the same rate, suggesting that operators are disconnecting the controllers rather than updating them, Censys noted.

The attack has also raised questions about liability. Les Mousquetaires said the refrigeration systems were managed by Danfoss and that it is therefore up to the supplier to file a complaint with the authorities, [Bloomberg reported](https://www.bloomberg.com/news/articles/2026-10-12/french-supermarket-refrigeration-sites-hit-by-cyberattacks).

**Related**: [CenterPoint Energy Data Breach Impacts 1 Million Texans](https://www.securityweek.com/centerpoint-energy-data-breach-impacts-1-million-texans/)

**Related**: [Meta Says Hackers Took Code, Personal Data of 1,500 in GitHub Breach](https://www.securityweek.com/meta-says-hackers-took-code-personal-data-of-1500-in-github-breach/)
