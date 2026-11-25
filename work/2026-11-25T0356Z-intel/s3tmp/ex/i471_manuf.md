---
title: "Aerospace To Chemicals: Why Manufacturers Are Easy Targets for Access Brokers"
url: https://www.intel471.com/blog/aerospace-to-chemicals-why-manufacturers-are-easy-targets-for-access-brokers
hostname: intel471.com
description: Manufacturing was the most targeted sector for ransomware and data extortion from January to October 2026, with 1,379 claims, or 16.8% of all victims…
sitename: Intel 471
date: "2026-11-18"
tags: ['intel471', 'security', 'research', 'threat intelligence']
fingerprint: "41032130f06f7f9"
language: en
image: https://www.intel471.com/api/og?id=842d9c79-6b1d-4c34-81d6-0b61e3d12236&type=blog
pagetype: article
filedate: "2026-11-25"
---
# Aerospace To Chemicals: Why Manufacturers Are Easy Targets for Access Brokers

Manufacturing was the most targeted sector for ransomware and data extortion from January to October 2026, with 1,379 claims, or 16.8% of all victims Intel 471 tracked. The cause has less to do with what manufacturers build than with how attackers get in. They buy access designed to work against many organizations at once, and the connections between manufacturers let that access reach well beyond the first victim.

#### **Why do attackers go after manufacturers, whatever they make?**

Because most access brokers aren’t choosing manufacturers at all. They go after whatever is exposed. Initial access brokers (IABs) specialize in compromising networks through brute-force attacks, stolen credentials, vulnerability exploits and social engineering, then sell that foothold to ransomware and data extortion groups so the buyers can skip the intrusion and focus on negotiating the extortion. From January to October 2026, IABs offered access affecting 172 manufacturing entities, about 10% of all accesses offered worldwide.

What stands out is how those offers were packaged. In our new report, [*From Aerospace to Assembly Lines: How Cybercriminals Are Targeting Manufacturing Supply Chains*](https://www.intel471.com/resources/whitepapers/from-aerospace-to-assembly-lines-how-cybercriminals-are-targeting-manufacturing-supply-chains), we found that 66.8% of the access we observed was wholesale, meaning it involved multiple targets rather than one named company. The report explains why that matters: “Once an actor develops an effective exploitation method, the actor can apply that method to additional exposed systems without conducting a separate, extensive reconnaissance effort against each organization.”

Wholesale versus specified access offers targeting manufacturers, January to October 2026. Source: Intel 471.

A broker who finds a weakness in a widely used technology can sweep up every organization running it. Whether a company builds jet components, car parts or specialty chemicals matters far less to that broker than whether the door is open. Perimeter remote access was behind most of the listings we examined, with VPN services alone accounting for 28.5% of cases. These are the same tools manufacturers rely on to keep plants, vendors and offices connected, which is why they keep turning up.

#### **What does that mean for your risk?**

It means the usual assumptions about who gets targeted don’t hold up well. A manufacturer with no household name and no reason to expect attention can be just as attractive as a global brand, because the cost of getting in is nearly the same and the pressure to pay is high. When a stopped production line can cost millions of dollars per day, and customers are waiting on parts, a ransom demand can look like the cheaper option. Attackers know that, and many pair the threat of downtime with the threat of leaking proprietary designs.

That pressure is the point of the whole market. Access is bought because it leads somewhere valuable, and in manufacturing, where uptime and intellectual property are both on the line, it usually does.

#### **Your supplier’s breach can become your problem**

The second half of the story is what happens after the first foothold. Manufacturers depend on one another for components, engineering work and maintenance, and attackers have noticed that the weakest link in that chain is often not the company they ultimately want.

In May 2026, an actor advertised a dataset allegedly stolen from an Asia-based electronics manufacturer containing highly sensitive details from its customer, a US-based automaker. The actor offered to sell hundreds of files and gigabytes of information revealing the automaker’s production-grade CAD schematics and board layouts, sourcing details, and diagnostics documentation that together gave deep insight into how key electronic systems in the vehicle are built, tested, and protected.

Nobody had to breach the automaker. The design files were sitting one tier up, with a supplier whose exposure became the customer’s. The same risk applies in every industry we examined. An engineering contractor, a component maker or a logistics partner can hold the information an attacker needs to pressure a much larger company.

For a supplier, this means your customers’ data is part of what makes you a target. For an OEM, it means your security posture extends to every vendor with a connection to your network or your designs.

#### **What manufacturers can act on today**

A few conclusions hold regardless of size or sector:

- Treat every internet-facing remote access point, including VPNs, remote desktop services and file transfer servers, as a door someone is already testing. Prioritize patching and monitoring there first.
- Enforce multifactor authentication on every external vendor access pathway.
- Segment corporate IT from plant floor systems, especially where legacy controllers can’t be patched.
- Include suppliers and contractors in your threat model, since their exposure can become yours.

#### **What the report adds**

The full report shows how it plays out in practice. It examines how Qilin, The Gentlemen and Akira operate against manufacturers, including what leaked internal chats reveal about how one group goes after backups and hypervisors. It includes real-world cases across aerospace and defense, automotive, industrial products and chemicals, and it breaks down victim claims by industry and revenue along with the entry points IABs advertise most often.

Download the full report to see how threat actors are targeting manufacturing and where your organization may be exposed.
