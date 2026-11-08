---
title: TrendAI™ Research Helps Disrupt Botnet of More Than 1.3 Million Pre-Infected Set-Top Boxes
url: https://www.trendaisecurity.com/en-us/resources-insights/trendai-security-blog/trendaitm-research-helps-disrupt-android-tv-botnet-of-more-than-13-million-pre-infected-devices
hostname: trendaisecurity.com
description: TrendAI™ Research supplied intelligence over several months that helped disrupt a botnet of more than 1.3 million pre-infected set-top boxes. We look at how the operation worked, its impact, and what the disruption means for defenders.
sitename: TrendAI
date: "2026-11-02"
fingerprint: "7735ac51f839b181"
---
#### Key Takeaways

- A disruption of the control infrastructure behind more than 1.3 million Android devices, such as TV set-top-boxes and projectors. The boxes came with pre-installed “x.cpe” management agent that used obfuscation techniques to evade pre-release security tests. Once the devices were activated, it pulled in unwanted software and enrolled the devices in residential proxy networks, ad fraud networks, peer-to-peer content delivery networks (PCDNs), and other “gray” infrastructure without their owners’ consent.
- Google has implemented changes to its existing review process to better safeguard against similar activity in the future.
- Access through the infected TV set-top boxes was sold as residential proxy and AI gateway services. Each box relayed third-party traffic through its owner’s home internet connection, and the operation reported more than 3.8 million distinct home and mobile IP addresses over four months.
- Residential proxies let criminals look like ordinary local customers. Traffic from a real household IP address passes IP reputation and geolocation checks that banks, retailers and online services rely on.
- Owners cannot remove the implant themselves. It runs as a system app signed with the manufacturer’s key, so cleanup needs vendor action, platform protection or replacement of the device.
- Google permanently banned the company, along with any of its future subsidiaries or affiliates, from building and selling certified Android devices or supplying software to other certified vendors.

Millions of home TV boxes could be opening homes and offices to malicious actors. More than a million Android TV set-top boxes were pre-infected to do exactly that, in an operation TrendAI™ Research helped disrupt.

Last week, action was taken against the infrastructure that controlled this global fleet of TV set-top boxes, projectors, and other Android devices. TrendAI™ Research supplied intelligence on this botnet infrastructure over several months, fueling the operation. As part of the disruption, Google also permanently banned the manufacturer, along with any of its future subsidiaries or affiliates, from building and selling certified Android devices or supplying software to other certified vendors. The fleet was managed through a pre-installed initial agent called “x.cpe” and a monetization module known as com.abc.nexus. The module has many versions , and each can pull different payloads that let the operator make money from pay-per-bandwidth services such as Traffmonetizer, Grass, and Honeygain.

Together, the agent and module turned common living-room devices into exit nodes for  [residential proxy services](https://www.trendaisecurity.com/en-us/resources-insights/deep-research/the-rise-of-residential-proxies-and-its-impact-on-cyber-risk-exposure-management)  or ad-fraud clickers, or nodes within a PCDN network. PCDNs are common in China. They use the spare bandwidth of home devices to deliver content such as video streams, and they pay device owners for the traffic. This made money for the operator, while device owners remained unaware.

TrendAI™ Research measured the operation between June and October 2026. Our telemetry counted 1,472,554 infected devices across 206 models in more than 170 countries. Counts differ slightly between partners depending on when each snapshot was taken and what each could see, so the joint figure is more than 1.3 million. The operator scheduled its proxy and ad fraud modules onto about 1.33 million of them.

The operation sits in the same ecosystem as BADBOX 2.0, which was previously  [disrupted in March 2025](https://humansecurity.com/learn/blog/satori-disrupting-badbox-2) . Kaspersky has also  [linked](https://securelist.com/android-head-unit-malware/121106/)  the com.abc.nexus component to the IPMoyu actor.

## How the operation worked

The devices shipped with firmware from a Shenzhen-based original equipment manufacturer and original design manufacturer (OEM/ODM) that builds Android devices such as TV set-top boxes for many white-label brands. The firmware carried a pre-installed management agent that presented itself as a standard remote-management client and used obfuscation techniques to evade pre-release security tests. The agent pulled updates from a GitHub page as designed, but it also connected to a Message Queuing Telemetry Transport (MQTT) server that gave the operator full remote control of each box. This allowed the operator to install and remove apps silently, change settings, and push updates.  Google has subsequently implemented changes to its existing review process to better safeguard against similar activity in the future.

One of the agent’s payloads was the com.abc.nexus module, which was renamed in the most recent updates. The com.abc.nexus module ran with system privileges and enrolled each box in several revenue streams. Over time we observed several monetization schemes, as listed here:

- A residential proxy service that resold the household’s internet connection
- Two commercial bandwidth-sharing programs, joined without any consent screen
- An ad module that generated fraudulent ad impressions

Figure 2 summarizes the evolution of com.abc.nexus over time.

Once the modules were deployed, the operator could switch them on and off per device from a central console via an MQTT command. Some of the later versions added anti-analysis protection and removed competing malware from the box, which protected the operator’s hold on the device.

One TV box could therefore earn money in several ways, at times even simultaneously, while its owner saw only a working streaming device showing their favorite TV show.

### Scale of the operation

Table 1 gives the metrics we have observed from June 3 to October 1, 2026. Collection was intermittent, so every figure is a lower bound on the true fleet.

| Measure | Value | 
|---|---|
| Device models | 206 | 
| Devices scheduled for proxy and ad fraud modules | About 1.33 million | 
| Distinct residential exit IP addresses | 3,849,226 | 
| Residential IPs available on a single day | Average 182,025, peak 366,562 | 
| Control messages captured | 2,360,663,001 | 

As Table 1 shows, the operator actively monetized about nine in ten of the devices it controlled. On a typical day the proxy product offered about 180,000 real household IP addresses. The operator pushed the com.abc.nexus payload to only some devices running the x.cpe agent, using a channel setting to choose which ones. This was controlled through a channel setting.

Devices reported from more than 170 countries, with Malaysia, Brazil, Iraq, Mexico and Taiwan recording the most devices. The United States, Germany, the United Kingdom, Australia and Canada each had from about 26,000 through 42,000 devices. Exit addresses belonged overwhelmingly to consumer broadband and mobile providers, the defining property of a residential proxy product.

### What this means for defenders

Traffic from these devices arrives from the same networks as an organization’s real customers and employees working from home. Blocklists of data-center ranges would not and did not catch this traffic. If the devices were part of an organizational network, the attacker could gain access to the internal network as well. The devices also collected detailed information about the environment, including Wi-Fi details (as seen in Figure 5) and Bluetooth settings.

The operator could also run shell commands directly on the devices, as shown in Figure 6.

## Notable functionality deployed on the devices

We observed several notable payloads deployed on controlled devices over time. These included residential proxy components, click fraud modules, bandwidth-sharing software development kits (SDKs), and other pay-for-traffic monetization components. In this section we review some of these payloads and the threat each one poses.

As we mentioned earlier, com.abc.nexus was observed over time to be bundled with multiple components. These include modules for ADMOYU (residential proxy), LinkfogService (which collects lw\_\* named binaries), PPService (pproxy), Appsalt (Honeygain SDK), TraffMonetizer bandwidth-sharing SDK, com.vs.grass (grass\[.\]io SDK), DevourService (ad fraud), and others.

#### LinkFog PCDN and AI gateways

LinkFog and DianxinCloud are PCDN services that pay users for distributed traffic. Like other pay-for-traffic companies, they are not necessarily malicious themselves. The abuse lies in how the operator enrolled devices without their owners’ consent. DianxinCloud also has an interface called DianxinAI which is a load-balanced AI API access platform. DianxinAI spreads the traffic across bandwidth that sell to it.

In some observed scenarios, DianxinCloud components were pushed to devices without user consent.

#### How attackers use the residential proxy fleet

Residential proxy fleet (ADMOYU) is a growing problem. It enables attackers to access networks from specific residential IPs. Once operators have access, these IP addresses in many ways, none of which requires the buyer to compromise a device. A buyer simply rents access. The risk lands wherever an organization trusts an IP address to show who and where a user is, such as login screening, payment fraud checks, ad billing, and geo-restricted services.

#### Attacker signs in from a household IP address to pass fraud screening

An attacker who rents an exit node gets a home broadband address in the victim’s own country and region. In this fleet, those addresses sat on consumer providers such as Comcast, Charter and AT&T in the U.S., Virgin Media in the U.K., and Vodafone in Germany. HUMAN  [reported](https://www.humansecurity.com/company/satori-threat-intelligence/badbox-2-0/)  that buyers of a related BADBOX proxy service used such access for account takeover and fake account creation.

#### Attacker bills advertisers for ad impressions from infected TV boxes

The operator scheduled its ad fraud module into about 1.33 million devices. Each box generated ad impressions from a real home connection, which ad verification treats as genuine audience.

#### Attackers inherit a foothold inside a million homes and offices

The operator could install and remove apps silently and run commands on the boxes. We observed silent install commands reaching more than 187,000, based on download counts. We also saw a script that turned off Google Play Protect on a large number of devices. Owners lose control of the device, and nothing on the connected screen would even hint it.

#### Why the exposure persists and where it stops

Each scenario exploits a decision that works as its owner intended. Buyers want cheap streaming boxes, white-label brands want cheap firmware, and online services trust residential addresses because most of their customers use them.

We observed the control infrastructure, the scheduled modules, and the residential exit pool. We did not observe any specific buyer of this fleet’s proxy capacity, and nothing here should be read as evidence that nation-state actors used this fleet.

## How the disruption worked

The operation of the infrastructure depended on a small number of central servers for initial bootstrap and MQTT configuration. The operation depended on two central servers. One stored configuration details and told devices how to connect . The other was the MQTT server. The removal of these servers cut the operator off from the devices, although the implant remains on each box.

A disruption raises the operator’s costs and does not remove the implant from devices that have already been sold. Unfortunately, operators of this kind have rebuilt on new infrastructure before.

## Recommendations

Compromised devices and botnets remain a staple threat, and this operation shows that a device can arrive already compromised. Organizations and individual users should take care with the devices they bring into their networks, offices, and homes. We recommend the following:

- Take care when buying low-cost Android devices, as many can contain unwanted payloads.Consumers should avoid unbranded or uncertified Android TV boxes and apps that pay for shared bandwidth.
- Online services and fraud teams should stop relying on IP reputation alone. TrendAITM Research’s  [residential proxy research](https://www.trendaisecurity.com/en/resources-insights/deep-research/the-rise-of-residential-proxies-and-its-impact-on-cyber-risk-exposure-management) recommends logging network fingerprints such as JA4T on internet-facing systems. It advises combining those fingerprints with behavioral signals, such as repeated failed logins, before acting on them. AI-powered security platforms and solutions like TrendAI Vision One™ Cyber Risk Exposure Management (CREM) offer promising techniques for identifying connections that originate from residential proxies. These techniques can help defenders differentiate between legitimate use of residential IP addresses by the owners and abuse of these same IP addresses by criminal users of residential proxy providers.
- Organizations with remote staff should treat unmanaged consumer devices on home networks as part of their exposure and keep corporate access behind managed endpoints.
- Operators of cameras, sensors and other telemetry should register what they expose to the internet, including systems run by suppliers. They should also monitor for scraping of those endpoints from residential addresses, as TrendAI™ Research’s report on  [external attack](https://www.trendaisecurity.com/en/resources-insights/deep-research/rethinking-the-external-attack-surface-managing-the-growing-risk-of-open-cyber-physical-data)  recommends.
- Retailers and marketplaces that sell white-label TV boxes should require certified firmware from their suppliers.

 [TrendAI Vision One™ Endpoint Security](https://www.trendaisecurity.com/en/platform/endpoint-security)  can be an enterprise’s additional layer of defense in the case of successful malicious use of residential proxies. This all-in-one endpoint protection with native threat detection and response, proactive risk mitigation, and centralized visibility streamlines operations and enhances an organization’s IT security posture. This solution extends protection to other security layers and integrates with third party solutions, meeting the security teams at whatever stage of the security journey they are on, giving them full visibility and critical insights into their IT and OT infrastructure.

## Indicators of Compromise (IoCs)

The full list of IoCs for this case is available  [here](https://cdn.sanity.io/media-libraries/mllBRzE9QpZ8/files/containers/3LJYKf8Lby5yBg0LGiZUfN8eFtd/trendai-research-helps-disrupt-android-tv-botnet-ioc.txt) .
