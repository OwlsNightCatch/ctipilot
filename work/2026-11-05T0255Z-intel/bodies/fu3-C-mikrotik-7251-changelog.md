Title: 

URL Source: https://upgrade.mikrotik.com/routeros/7.25.1/CHANGELOG

Published Time: Tue, 03 Nov 2026 10:23:17 GMT

Markdown Content:
What's new in 7.25.1 (2026-11-02):

*) bridge - fix BPDUs leaking to the wrong dual-connected bond in MLAG (introduced in v7.24);
*) bridge - improve FDB synchronization between MLAG peers when VLANs are added;
*) console - fix custom SSH client login parameters being ignored (introduced in v7.25);
*) dhcpv4-client - fix packet length calculation (introduced in v7.25);
*) dude - fix missing outage times and graph background scaling (introduced in v7.25);
*) fetch - fix HTTP fetch getting stuck in a "bad HTTP response" state;
*) ipsec - fix XFRM interfaces staying down until a reboot;
*) ipv6 - fix from-pool address lifetimes not updating after a prefix renewal (introduced in v7.25);
*) pim - fix IGMP/MLD querier being disabled after upgrade (introduced in v7.25);
*) ptp - fix PTP support on CRS804-4DDQ;
*) routing-filter - fix host matching in address lists with more than 64 ranges;
*) sfp - fix DAC EEPROM corruption when disabling 400G ports on CRS804 and CRS812 switches;
*) ssh - fix packet alignment when SHA-1 is used (introduced in v7.25);
*) system - improve stability (includes CVE-2026-98432);
*) webfig - fix multi-value fields being displayed as empty (introduced in v7.25);
*) wifi - fix virtual interface restart loop when reselect-interval and reselect-time are configured (introduced in v7.25);

Links/Buttons:
This page does not seem to contain any buttons/links.
