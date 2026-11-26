---
title: Enable Ports on the Firewall
url: https://uat.juniper.net/documentation/us/en/software/session-smart-router/docs/config_firewall_ports
hostname: juniper.net
description: SSR software requires that the following ports be enabled on your firewall to allow connectivity and proper operation.
sitename: uat.juniper.net
date: "2026-01-01"
fingerprint: afa94158d4530084
language: en
filedate: "2026-11-26"
---
# Enable Ports on the Firewall

SSR software requires that the following ports be enabled on your firewall to allow connectivity and proper operation.

### SSR to a Conductor[](https://www.juniper.net/documentation/us/en/software/session-smart-router/docs/config_firewall_ports/index.html#ssr-to-a-conductor)

Enable the following on your firewall for SSR to Conductor connectivity:

- \[Conductor IP address\]
- Port 930/TCP
- Port 4505/TCP
- Port 4506/TCP

### SSR to SSR[](https://www.juniper.net/documentation/us/en/software/session-smart-router/docs/config_firewall_ports/index.html#ssr-to-ssr)

Enable the following on your firewall for SSR to SSR connectivity:

- \[SSR IP address\]
- Port 1280/UDP
- Ports 1280 and 1283/TCP
- Ports in the range 16,384-65,534 TCP/UDP
- rp.cloud.threatseeker.com on port 443/TCP; this is required for Web Filtering

For detailed information about different communication channels between nodes within a router, between peering routers, and between routers and their conductor, see [Intra- and Inter-System Communication](https://www.juniper.net/documentation/us/en/software/session-smart-router/docs/concepts_machine_communication)

### Conductor and Router to the SSR Software Repository[](https://www.juniper.net/documentation/us/en/software/session-smart-router/docs/config_firewall_ports/index.html#conductor-and-router-to-the-ssr-software-repository)

The conductor and routers retrieve SSR software (ISOs, installer packages, RPMs, and plugins) from the Juniper software repository during installation and upgrades. If your deployment requires that external IP addresses are locked down (no internet access), enable the following on your firewall to allow the conductor and routers access to the HPE/Juniper SSR software repository:

- software.128technology.com
- Port 443/TCP

In deployments where the routers managed by a conductor do not have internet access, you can configure the conductor as a software repository (or proxy) for those routers. In this case only the conductor requires outbound access to `software.128technology.com`. For more information, see [Upgrade the SSR Conductor](https://www.juniper.net/documentation/us/en/software/session-smart-router/docs/conductor_upgrade).

### SSR to the Mist Cloud[](https://www.juniper.net/documentation/us/en/software/session-smart-router/docs/config_firewall_ports/index.html#ssr-to-the-mist-cloud)

For the most up to date SSR to Mist Cloud connectivity information, see [Juniper Mist Firewall Ports and IP Addresses for Firewall Configuration](https://networkingdocs.hpe.com/documentation/us/en/software/mist/mist-management/topics/ref/firewall-ports-to-open.html).

| Service Type | Global 01 | Global 02 | Global 03 | Global 04 | Global 05 | EMEA 01 | EMEA 02 | EMEA 03 | EMEA 04 | APAC 01 | APAC 03 | 
|---|---|---|---|---|---|---|---|---|---|---|---|
| SSR | ep-terminator.mistsys.net (TCP 443) portal.mist.com (TCP 443) redirect.mist.com (TCP 443) software.128technology.com (TCP 443) rp.cloud.threatseeker.com (TCP 443) | ep-terminator.mistsys.net (TCP 443) ep-terminator.gc1.mist.com (TCP 443) portal.gc1.mist.com (TCP 443) redirect.mist.com (TCP 443) | ep-terminator.mistsys.net (TCP 443) ep-terminator.ac2.mist.com (TCP 443) portal.ac2.mist.com (TCP 443) redirect.mist.com (TCP 443) | ep-terminator.mistsys.net (TCP 443) ep-terminator.gc2.mist.com (TCP 443) portal.gc2.mist.com (TCP443) redirect.mist.com (TCP 443) | ep-terminator.mistsys.net (TCP 443) ep-terminator.gc4.mist.com (TCP 443) portal.gc4.mist.com (TCP443) redirect.mist.com (TCP 443) software.128technology.com (TCP 443) rp.cloud.threatseeker.com (TCP 443) | ep-terminator.mistsys.net (TCP 443) ep-terminator.eu.mist.com (TCP 443) portal.eu.mist.com (TCP 443) redirect.mist.com (TCP 443) | ep-terminator.mistsys.net (TCP 443) ep-terminator.gc3.mist.com (TCP 443) portal.gc3.mist.com (TCP 443) redirect.mist.com (TCP 443) software.128technology.com (TCP 443) rp.cloud.threatseeker.com (TCP 443) | ep-terminator.mistsys.net (TCP 443) ep-terminator.ac6.mist.com (TCP 443) portal.ac6.mist.com (TCP 443) redirect.mist.com (TCP 443) software.128technology.com (TCP 443) rp.cloud.threatseeker.com (TCP 443) | ep-terminator.mistsys.net (TCP 443) ep-terminator.gc6.mist.com (TCP 443) portal.gc6.mist.com (TCP 443) redirect.mist.com (TCP 443) software.128technology.com (TCP 443) rp.cloud.threatseeker.com (TCP 443) | ep-terminator.mistsys.net (TCP 443) ep-terminator.ac5.mist.com (TCP 443) portal.ac5.mist.com (TCP 443) redirect.mist.com (TCP 443) software.128technology.com (TCP 443) rp.cloud.threatseeker.com (TCP 443) | ep-terminator.mistsys.net (TCP 443) ep-terminator.gc7.mist.com (TCP 443) portal.gc7.mist.com (TCP 443) redirect.mist.com (TCP 443) software.128technology.com (TCP 443) rp.cloud.threatseeker.com (TCP 443) | 

### Connect Directly to the Mist Cloud[](https://www.juniper.net/documentation/us/en/software/session-smart-router/docs/config_firewall_ports/index.html#connect-directly-to-the-mist-cloud)

| Service Type | Global 01 | Global 02 | Global 03 | Global 04 | Europe 01 | APAC 01 | 
|---|---|---|---|---|---|---|
| Admin Portal | manage.mist.com/signin.html api-ws.mist.com api.mist.com(TCP 443) | manage.gc1.mist.com api-ws.gc1.mist.com api.gc1.mist.com(TCP 443) | manage.ac2.mist.com api-ws.ac2.mist.com api.ac2.mist.com(TCP 443) | manage.gc2.mist.com (TCP 443) api-ws.gc2.mist.com (TCP 443) | manage.eu.mist.com api-ws.eu.mist.com api.eu.mist.com(TCP 443) | manage.ac5.mist.com (TCP 443) api-ws.ac5.mist.com (TCP 443) api.ac5.mist.com (TCP 443) | 
| Guest Wi-Fi Portal | portal.mist.com (TCP 443) | portal.gc1.mist.com (TCP 443) | portal.ac2.mist.com (TCP 443) | portal.gc2.mist.com (TCP 443) | portal.eu.mist.com (TCP 443) | portal.ac5.mist.com (TCP 443) | 
| Webhooks Source IP Addresses | 54.193.71.17 54.215.237.20 | 34.94.120.8 35.236.34.24 35.236.92.224 | 34.231.34.177 54.235.187.11 18.233.33.230 | 34.152.4.85 35.203.21.42 34.152.7.156 | 3.122.172.223 3.121.19.146 3.120.167.1 | 54.206.226.168 13.238.77.6 54.79.134.226 |
