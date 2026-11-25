---
title: Do you show up on Shodan? The risks of internet-exposed OT to local governments
author: David McMillen
url: https://www.ibm.com/think/x-force/shodan-ot-risks-local-government
hostname: ibm.com
description: Discover how Shodan exposes internet-facing OT—including PLCs, Modbus services and remote-access systems—and why local governments must identify and secure these pathways before attackers exploit them.
sitename: Do you show up on Shodan? The risks of internet-exposed OT to local governments
date: "2026-09-02"
tags: ['Cybersecurity', 'Threat management', 'Cyberattacks', 'Cyberthreats']
fingerprint: a718c8d71e47dae4
language: en
image: https://www.ibm.com/content/dam/connectedassets-adobe-cms/worldwide-content/stock-assets/getty/image/photography/4e/03/dsc2112.jpg/_jcr_content/renditions/cq5dam.thumbnail.1280.1280.png
pagetype: website
filedate: "2026-11-25"
---
Discover how Shodan exposes internet-facing OT—including PLCs, Modbus services and remote-access systems—and why local governments must identify and secure these pathways before attackers exploit them.

Published 02 September 2026

Operational Technology (OT) systems that were once isolated are now increasingly exposed and discoverable on the public internet. Industrial organizations and local governments increasingly depend on remote access, cellular communications, internet-connected gateways, vendor support platforms, building-management systems, programmable logic controllers, supervisory control systems and cloud-connected devices. As those technologies become more connected, portions of the operational environment can become visible from the public internet.

Shodan provides one way to identify that exposure. This is not a new issue, nor is Shodan an obscure platform. Shodan has been widely known within the cybersecurity community for years as a tool that indexes internet-connected systems and externally exposed services. However, the continued visibility of [operational technology](https://www.ibm.com/think/topics/operational-technology) environments demonstrates that internet exposure remains a persistent and significant security concern worth revisiting. Depending on the device and configuration, those results may reveal open ports, industrial protocols, device manufacturers, software versions, management interfaces, certificates and other information that can help identify an organization’s technology stack.

For operational technology defenders, the primary concern is not that Shodan creates a vulnerability. The concern is that Shodan can reveal an exposure that already exists.

That distinction matters because an attacker can begin reconnaissance without knowing an organization’s name. An adversary can first search for a technology, protocol, product or service and identify its owner afterward. This dynamic is particularly important for local governments, which often operate critical infrastructure with comparatively small IT and cybersecurity staffs.

A small municipality in New York may operate several remotely located wastewater pump stations that must run continuously to prevent sewage overflows. These facilities may rely on aging programmable logic controllers, cellular communications, remote access maintained by outside vendors and industrial equipment that has remained in service for decades.

Every OT owner should ask two questions: Do you show up on Shodan, and if so, what could that visibility reveal about your operational environment?

This paper traces the risk from initial internet discovery to potential operational and physical consequences. It explains how exposed OT assets become actionable intelligence for adversaries, why municipal environments face distinctive challenges, how exposed Modbus services may provide a pathway from reconnaissance to operational disruption, and what defenders can do to identify, prioritize and reduce that exposure.

- **Internet-visible OT infrastructure presents risk beyond the vulnerability of any single exposed device.** External visibility can provide adversaries with reconnaissance data that supports identification of industrial technologies, remote-access infrastructure, vendors, facilities and potential pathways into operational environments.
- **Local governments face elevated exposure risk.** Many municipalities operate critical physical infrastructure while relying on comparatively small technical teams, legacy control systems, third-party integrators, and persistent remote-access arrangements.
- **Externally reachable Modbus/TCP warrants immediate investigation.** Traditional Modbus was designed for trusted industrial environments and generally lacks the authentication, encryption and authorization characteristics expected of modern internet-facing protocols.
- **Remote access represents one of the most significant pathways into modern OT environments.** The highest-risk externally visible asset may not be the PLC itself. Instead, it may be a VPN appliance, cellular gateway, remote-support platform, engineering workstation or vendor-access service that provides a pathway toward the control environment.
- **Effective OT defense requires monitoring beyond conventional malware detection.** Defenders should correlate identity, remote access, industrial protocol activity, controller changes and physical-process behavior to identify malicious activity conducted through otherwise legitimate systems and credentials.

Shodan is fundamentally a visibility and reconnaissance tool. It doesn’t add systems to the internet; instead, it reveals existing online services. The main takeaway is that a system’s presence in a Shodan search indicates it was already accessible. Secondly, this highlights a concerning reality: if a security researcher can locate a system, so too could a malicious actor.

Attackers routinely use automated reconnaissance; they do not have to manually search for individual organizations one at a time. They can identify devices, ports, protocols, software products, and services that match technical characteristics.

The targeting process can therefore begin with technology rather than with a predetermined victim. An adversary might search for industrial gateways, PLC interfaces, remote-access appliances, VPN systems, building-management systems, SCADA interfaces, engineering workstations, cellular routers, remote terminal units, industrial protocols or legacy administrative services. For example, the adversary could search for internet-accessible devices responding on the default Modbus TCP port, narrow the results by geographic area and device characteristics, and only then investigate which municipality or utility operates them.

Once a system is discovered, an attacker can investigate its ownership and add contextual information about the potential target. At that point, internet visibility becomes actionable threat intelligence.

Local governments occupy an unusually difficult cybersecurity position. A municipality may operate infrastructure with consequences comparable to those of a major industrial organization while having only a fraction of the technical and cybersecurity resources.

A town, city, county, or public authority may be responsible for drinking-water and wastewater systems, pumping stations, traffic signals, building automation, emergency facilities, public works operations, physical security, remote telemetry, and flood-control infrastructure. Many of these systems are operationally critical and have remained in service for years or decades. Industrial equipment is often retained far longer than conventional enterprise technology. A functioning controller may remain in operation for twenty years or more because replacement can require engineering changes, process shutdowns, testing, regulatory review, or substantial capital expenditure.

The result is an environment in which legacy technology increasingly coexists with modern connectivity. A PLC that was originally deployed on an isolated network may later become reachable through a cellular modem, remote-access appliance, vendor VPN, firewall rule, or internet-connected gateway. The controller may not have changed, but the threat environment surrounding it has changed substantially.

For municipalities, this risk is compounded by dependence on third parties. A municipality may have one contractor maintaining water controls, another supporting building automation, another managing traffic systems, and another administering network infrastructure. Each relationship can introduce connectivity and privileged access.

A municipality may therefore own the infrastructure without having complete visibility into every technical pathway that leads to it. This gap extends beyond IT: it is an operational-governance problem because remote access can affect the systems that deliver essential public services.

Local-government OT is already being targeted. Recent incidents demonstrate that internet-accessible industrial systems can provide attackers with a path from reconnaissance to operational disruption.

In April 2026, CISA, the FBI, NSA, EPA, DOE, and [US Cyber Command warned](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a) that Iranian-affiliated actors were actively targeting internet-connected PLCs across U.S. critical infrastructure, including government services, water and wastewater, and energy. The campaign caused PLC disruptions, manipulation of HMI and SCADA data, operational disruption, and financial loss. CISA expanded the advisory in July 2026 after observing targeting of Rockwell Automation/Allen-Bradley, Schneider Electric, Siemens, and potentially other PLCs. Investigators observed malicious traffic targeting OT-related ports including 44818, 2222, 102, and 502.

On July 30, 2026, the FBI and EPA [issued a separate warning](https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions) after water and wastewater utilities in at least seven states reported attacks against internet-facing Rockwell Automation/Allen-Bradley MicroLogix 1100 and 1400 PLCs. Attackers changed PLC IP addresses and passwords, disrupting monitoring and control. Reported operational effects included loss of water pressure and flooding. The FBI also noted that similar third-party network configurations across multiple utilities may have allowed attackers to repeat successful techniques against different customers.

In January 2024, attackers [targeted water systems](https://www.texastribune.org/2024/04/19/texas-cyberattacks-russia/) in several small Texas communities. In Muleshoe, attackers caused the municipal water system to overflow before officials shut down the affected system and moved to manual operations. Hale Center reported approximately 37,000 firewall login attempts in four days, while Lockney reported stopping attackers before they reached its water system.

In November 2023, CISA [warned of active exploitation](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a) of Unitronics PLCs used by U.S. water and wastewater systems. The activity was associated with the Iranian IRGC-affiliated CyberAv3ngers operation. The broader federal investigation found that the campaign compromised at least 75 Unitronics devices between November 2023 and January 2024 across multiple critical-infrastructure sectors. Attackers deployed malicious ladder logic to some devices, replacing legitimate controller logic and causing disruptive effects.

These incidents involved different PLC manufacturers and attack techniques, but they demonstrate the same underlying lesson: internet-accessible OT creates opportunity. For local governments, automated reconnaissance does not distinguish between a water system serving 5,000 residents and one serving five million. Attackers are already looking for municipal OT; the urgent questions are what they can see and what they can reach.

One of the most important protocols to evaluate when investigating internet-exposed OT is Modbus. Modbus has been used in industrial environments for decades and remains common across manufacturing, water, wastewater, energy, building systems and other control environments. Modbus/TCP commonly operates over TCP port 502.

Its continued popularity comes partly from its simplicity. That simplicity is also part of its security challenge. Traditional Modbus was developed for trusted industrial environments and was not originally designed for communication across hostile public networks.

Classic implementations generally do not provide the security characteristics that defenders would expect from a modern internet-facing protocol. Traditional Modbus commonly lacks native encryption, strong authentication, message-integrity protection and granular user-level authorization. Those characteristics become particularly important when Modbus is reachable from an untrusted network.

A Modbus device may expose information about an industrial process simply by responding to legitimate protocol requests. Depending on the device and configuration, communication may expose registers or values associated with operational conditions. The concern becomes significantly greater when write functionality is accessible.

Modbus communications can read or modify coils and registers associated with physical processes, including pump status, valve position, motor operation, temperature, pressure, flow, tank level, alarm state, operating mode, and setpoints. The security question is therefore not simply whether TCP port 502 is open, but what physical process the device listening on that port can monitor or control.

If internet-originated communication can reach an industrial controller using Modbus, defenders should immediately determine why that pathway exists, what systems are reachable through it, who depends on it, whether write operations are possible and how the communication is being restricted and monitored. For most organizations, direct internet exposure of Modbus/TCP should be considered a significant security finding until demonstrated otherwise.

Traditional Modbus was designed for trusted industrial environments in which connected systems were presumed to be authorized. That assumption was more defensible when the protocol operated over isolated serial links or tightly restricted control networks. It becomes dangerous when Modbus communication can originate from untrusted or publicly accessible networks.

Traditional Modbus does not inherently verify that a command came from an authorized engineering workstation. An unauthorized system that can reach the device may issue the same technically valid command, and the controller may process it without being able to distinguish the source’s intent or authority.

That is why architecture matters. Security protections must often surround the protocol rather than depend on the protocol itself. Organizations should use segmentation, industrial firewalls, allowlisting, controlled remote-access infrastructure, network monitoring, identity controls and process-aware detection to limit who can communicate with Modbus devices and what those systems are allowed to do.

The assumption that obscurity provides meaningful protection should be retired. Attackers do not need to know the address of a municipal pump station or industrial plant in advance. Internet-scale scanning allows systems to be identified by their technical characteristics.

An adversary can search for an industrial protocol or exposed service and investigate ownership afterward. The targeting process can therefore proceed in reverse: find the technology, identify the device, identify the owner, determine the physical process, enrich the target and identify additional access pathways.

This changes traditional targeting assumptions. The attacker does not always select the victim first. In some cases, the exposed technology identifies the victim for them.

A single exposed industrial service may not initially appear significant. The risk increases when that information is correlated with other sources. An attacker may identify an industrial gateway whose banner reveals a manufacturer. The product family may suggest a particular control architecture. Public records may identify the facility or system integrator. Job postings may mention a specific SCADA platform. Employee profiles may identify automation engineers. A remote-access portal may identify the connectivity technology in use, while previously compromised credentials associated with the organization may provide another potential avenue of attack.

At that point, the attacker is no longer examining an isolated device. The attacker is developing an OT target profile that may include the organization, facility, industrial technology, vendors, remote-access infrastructure, personnel, probable architecture and potential vulnerabilities. External OT exposure must therefore be treated as an intelligence problem as well as an asset-management and vulnerability-management problem.

Shodan and other internet-reconnaissance platforms may represent the beginning, rather than the entirety, of an attack. Exposure discovery can lead to credential abuse, internal reconnaissance, industrial-protocol interaction, controller access and ultimately physical-process impact.

Consider a hypothetical municipality that operates several drinking-water wells and remotely managed pump stations. Each remote facility communicates with a central supervisory system, while a third-party integrator maintains the control environment and periodically provides remote support. One remote site includes a cellular-connected industrial gateway that ultimately provides connectivity to equipment communicating through Modbus/TCP. The system operates normally for years. Then an adversary discovers an externally visible service.

One of the greatest challenges in external attack-surface management is the difference between what an organization believes it exposes and what an external observer can identify. A municipality may believe its internet presence consists primarily of a website, email infrastructure, cloud applications and a VPN. An outside observer may identify considerably more, including a cellular router, industrial gateway, remote-management interface, vendor portal, device fingerprint, certificate metadata or Modbus/TCP service. That difference should be measured, not assumed.

Organizations should manage internet-exposed OT as an ongoing security risk through recurring external assessments, exposure reduction, access controls, network segmentation, monitoring, connection governance and incident preparedness.

- **Perform an outside-in OT exposure assessment**
Inventory what the internet can see, including exposed industrial protocols, remote-access services, gateways, certificates, and management interfaces.
- **Eliminate unnecessary internet exposure**
Investigate any internet-visible Modbus/TCP service, especially TCP/502, and remove direct internet access to PLCs, RTUs, HMIs and engineering workstations wherever possible.
- **Secure remote and vendor access**
Require MFA, unique user accounts, strong logging, and time-limited access for employees, contractors, integrators, and vendors.
- **Segment and restrict OT communications**
Separate OT from enterprise and internet-facing networks. Allow only required communication paths and, where practical, allowlist systems authorized to communicate with controllers.
- **Monitor industrial protocol and process behavior**
Detect new Modbus talkers, unauthorized write operations, controller changes, and commands that do not make sense given actual process conditions.
- **Know every remote path into OT**
Maintain an inventory of remote connections, who owns them, why they exist, what they can reach, and how access can be disabled. If no one can explain a connection, treat that as a finding.
- **Prepare for an OT incident**
Establish escalation procedures involving both cybersecurity and operations teams, and maintain tested backups of controller logic, HMI configurations, engineering projects, and critical network configurations.

The most important lesson from Shodan is that obscurity is no longer a security strategy. Attackers can search for technologies such as Modbus, industrial gateways, remote-access appliances, or exposed PLCs and then determine who owns them. For local governments, this matters because water, wastewater, transportation, buildings, and emergency services often depend on long-lived OT systems supported by small technical teams, contractors, and limited cybersecurity resources.

That is why “Do you show up on Shodan?” should become a routine OT security question. Appearing in Shodan does not prove compromise, but it does prove visibility—and visibility enables reconnaissance and targeting. If an asset is exposed, determine what it is, why it is reachable, who can access it and how that access can be revoked. In OT, the objective is not simply to protect computers; it is to protect the availability, integrity, controllability and safety of the physical processes’ communities depend on every day.

Join security leaders who rely on the Think Newsletter for curated news on AI, cybersecurity, data and automation. Learn fast from expert tutorials and explainers—delivered directly to your inbox twice weekly. See the [IBM Privacy Statement](https://www.ibm.com/privacy).
