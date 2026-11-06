---
title: Residential proxy services found routing traffic through White House network
author: Alex Lekander
url: https://cyberinsider.com/white-house-network-residential-proxy-traffic/
hostname: cyberinsider.com
description: Residential proxy services allowed paying customers to route internet traffic through addresses assigned to the White House network.
sitename: CyberInsider
date: "2026-11-05"
categories: ['News', 'Security']
fingerprint: bf4bf339b02970d1
---
Residential proxy services allowed paying customers to route internet traffic through addresses assigned to the White House network.

The findings raise concerns about unauthorized bandwidth sharing on a sensitive government network.

[Layer3 Intel disclosed the activity](https://layer3intel.com/blog/residential-proxies-white-house-network) on November 4 after researchers spotted it in the company’s newly launched Residential Proxy Observatory. Between October 5 and November 3, its monitoring pipeline recorded exits through six IP addresses on 26 of the 30 days, involving 28 proxy services.

The addresses belong to AS2650, an autonomous system registered to the Executive Office of the President that hosts the White House network. [Residential proxy services](https://cyberinsider.com/50-of-lg-and-samsung-smart-tv-apps-embed-residential-proxies/) let customers relay requests through other people’s devices, making traffic appear to originate from those devices’ internet connections.

Layer3 said it discovered the activity while requesting globally rotating connections from public proxy providers, rather than deliberately targeting the White House. It also checked the addresses against public IP intelligence pages from Spur and Synthient, which classified them as residential proxy exits.

Access required only a subscription to publicly available services costing a few dollars, the researchers said.

### Infatica linked to the activity

Proxy intelligence firm Synthient separately linked activity on AS2650 to multiple installations of Infatica, a residential proxy service often bundled into free desktop and mobile applications.

Developers can integrate proxy software development kits, or SDKs, to earn money by sharing users’ bandwidth. However, the findings do not establish which application introduced the software, whether users knowingly enabled it, or who owned the devices involved.

Around half of Layer3’s observations occurred between 5 p.m. and midnight Eastern time, with almost none in the early morning. The researchers interpreted this as suggesting a device accompanying someone regularly present during evening hours, but their measurements identify network exits rather than individual people or endpoints.

### Potential internal network exposure

Beyond letting strangers generate traffic attributed to a government address, insecure proxy software can expose local systems.

In January, [Synthient documented](https://synthient.com/blog/a-broken-system-fueling-botnets) how the [Kimwolf botnet](https://cyberinsider.com/record-breaking-kimwolf-ddos-botnet-released-new-stealthier-version/) abused residential proxy infrastructure to reach vulnerable Android devices with exposed Android Debug Bridge services. The company assessed that infections had surpassed two million devices.

Layer3 founder Sergiy Usatyuk said the company had not notified anyone about the findings and would withhold the specific addresses because of their sensitivity.

## Leave a Reply Cancel reply
