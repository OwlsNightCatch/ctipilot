---
schema: 1
kind: incident
title: "CERT Polska: a second Polish CHP plant was shut down on 29 December 2025 through the distribution operator's private APN — the first real-world use of that path into an OT network"
headline: "A mobile-carrier private APN, shared by a wind farm and a heat plant, carried an attacker from a substation firewall to the turbine controls"
summary: >
  CERT Polska published a follow-up forensic report on 2026-08-08 disclosing a second, previously
  undisclosed victim of the 29 December 2025 attacks on Poland's energy sector: a smaller combined
  heat and power plant supplying heat to about 50,000 residents, where three Siemens PLCs were
  switched to STOP mode and password-locked, shutting down a steam turbine and the process-water
  treatment system. The attacker reached it from an already-compromised wind-farm substation by
  tunnelling over SSH through a cellular router into the distribution system operator's private APN,
  a mobile network shared by both sites, and then into a WAGO PFC200 controller whose WAN-side web
  interface answered on factory credentials. CERT Polska assesses this is the first observed
  real-world use of a private APN as the path into an OT network, and states the enabling
  misconfiguration — arbitrary device-to-device communication inside the APN — is common in Poland
  and believed widely deployed elsewhere.
discovered_at: "2026-08-09T04:42:00Z"
event_date: "2025-12-29"
run_id: 2026-08-09T0412Z-intel
priority: high
immediate_action: null
tags: [ot-ics, default-config]
regions: [europe]
sectors: [energy]
entities: [incident:poland-energy-grid-attack-2025-12-29]
techniques: [T1133, T1078, T1078.001, T1046, T1021.004, T1572, T1531, T1561.002, T1070]
affected_products: ["Fortinet FortiGate", "Teltonika RUTX50", "WAGO PFC200", "Siemens SIMATIC S7-300", "Siemens SIMATIC S7-1200", "Siemens SIMATIC S7-1500"]
cves: []
sources:
  - url: "https://cert.pl/en/posts/2026/08/incident-follow-up-report-energy-sector-2025/"
    publisher: "CERT Polska (NASK)"
    date: "2026-08-08"
    role: primary
  - url: "https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf"
    publisher: "CERT Polska (NASK)"
    date: "2026-08-08"
    role: primary
closed_sources: []
evidence:
  - quote: "To the best of our knowledge, the use of a private APN to gain access to the OT network was the first instance of this attack vector being observed in a real-world cyberattack."
    publisher: "CERT Polska (NASK)"
  - quote: "The attack was made possible, among other factors, by a misconfiguration that allowed arbitrary devices within the private APN network to communicate with one another."
    publisher: "CERT Polska (NASK)"
  - quote: "Surveys conducted among organizations using similar solutions indicated that this configuration was commonly encountered in Poland."
    publisher: "CERT Polska (NASK)"
verification: single-source-national-cert
sourcing_note: >
  Single-source under the national-CERT carve-out: CERT Polska is the national CSIRT investigating an
  incident in its own jurisdiction and is the primary disclosing party for its own forensic findings.
  The report makes no actor attribution — it is a technical account only — and does not address the
  contested cluster labelling attached to the wider December 2025 campaign.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: ot-ics
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Audit the client-isolation setting on every private APN your OT estate reaches, and enable it: this intrusion crossed from a wind-farm substation to an unrelated heat plant only because arbitrary devices inside the operator's private APN could open connections to each other."
  - "Enumerate what answers on the APN-facing interface of each device connected to that APN and close or re-credential its administrative services — the pivot device here was a WAGO PFC200 whose WAN-side web interface was reachable from the APN on default 'admin' credentials, and SSH was then turned on through that interface."
migrated_from: null
---

CERT Polska published a follow-up analysis on 2026-08-08 of the coordinated 29 December 2025 attacks on Poland's energy sector, adding a victim its January report did not carry: a smaller combined heat and power plant supplying heat to roughly 50,000 residents, whose industrial control systems came under attack at about 07:00 that morning ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). The analysis took more than three months, which is why the case was held back from the initial report published on 30 January 2026 ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). The head of CERT Polska, Marcin Dudek, presented the case at DEF CON in parallel with publication ([CERT Polska, 2026-08-08](https://cert.pl/en/posts/2026/08/incident-follow-up-report-energy-sector-2025/)). The report carries no actor attribution.

The finding that generalises beyond Poland is the access path. Substations that connect renewable generation to the distribution grid commonly carry cellular routers whose SIM cards sit in a private APN — a carrier-operated private mobile network the distribution system operator uses to reach the remote terminal unit at each site, in this case over DNP3.0 ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). The operator's requirements covered the serial path to the RTU but said nothing about the router's own administrative interface, so the Teltonika RUTX50 at the compromised wind farm sat with its serial link to the RTU on one interface and an Ethernet link into a VLAN behind the already-compromised central firewall on the other ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). CERT Polska states this is the first instance it knows of in which a private APN was the route into an OT network, made possible by a configuration that let arbitrary devices inside the APN talk to one another — a configuration its surveys found common in Poland and which it believes is widely deployed in other countries ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)).

The chain ran as follows. Every compromised wind-farm substation in the original wave — more than 30 grid connection points — used a FortiGate as both VPN concentrator and firewall, with the VPN interface reachable from the internet and accepting accounts defined on the device itself without multi-factor authentication; the attacker held administrative privileges on the device and likely used them to obtain a VPN account with reach across all network segments ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). From inside, the attacker logged into the Teltonika router over SSH repeatedly during December 2025 and tunnelled from it into the private APN; how the router password was obtained could not be determined, and whether a flaw in the device was used is likewise unresolved ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). From 18 December the attacker scanned the APN for VNC and HTTP services and for the S7 and Modbus industrial protocols, and found a WAGO PFC200 controller exposing a web administration interface on its WAN side, reachable from the APN and still on the default credentials for the `admin` account; SSH was not enabled on that interface by default, and the sequence in the carrier's logs indicates the attacker enabled it through the web interface before tunnelling onward into the heat plant's OT network, to which the controller had connectivity for both the SCADA systems and the segments holding process-control devices ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)).

Reconnaissance inside the plant ran from 18 to 25 December. Repeated attempts to reach the firewall's LAN-side web interface using the account names `admin`, `user` and a username belonging to the company that deploys telecontrol systems at renewable sites all failed, and were retried three days later without success ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). On Sunday 21 December, eight days before the attack, the attacker scanned for S7 on 102/TCP, Modbus on 502/TCP, CODESYS on 11740/TCP and RTSP on 554/TCP alongside RDP, VNC and web services — and in one subnet the scan began at the address of the SCADA system itself, which CERT Polska reads as evidence of earlier reconnaissance having already identified the high-value targets ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). On Christmas Day the attacker established successful S7 connections to three Siemens PLCs, most plausibly to prepare the destructive step ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)).

On 29 December activity inside the plant network ran from about 05:30 to about 10:10, meaning the operator's recovery work beginning around 07:30 started while the attacker was still present ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). The first action after tunnelling through the WAGO controller was to open the SCADA server's web interface, then reach an S7-300 over the S7 protocol, repeating the sequence against an S7-1200 and an S7-1500 ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). According to statements from plant personnel the PLCs were switched to STOP mode and protected with a password blocking both operating-state changes and control-logic modification, shutting down the steam turbine and the process-water treatment system and interrupting cogeneration; prompt operator response held it to a short outage with no interruption to customer heat or electricity supply ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). The attacker also reconfigured seven Moxa serial device servers and three Moxa switches — factory reset, password changed, addresses moved to unreachable values such as 127.0.0.1 — and the timing of the HTTP requests supports a high-confidence assessment that this was automated ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). Connections to two ABB ACS variable frequency drives were observed with no determinable effect, and attempts against Schneider Electric ATV 6xx drives failed because the attacker targeted 80/TCP while those interfaces listened elsewhere ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)).

Two recovery lessons sit in the anti-forensics. The attacker corrupted the partition table of the WAGO controller used as the gateway, and the operator's own factory reset did not repair it, leaving the device unbootable and its logs unrecoverable; the Teltonika router was factory-reset about thirty minutes after the last plant activity and its address set to 127.0.0.1, and the FortiGate was factory-reset last of all, destroying the logs from the initial entry point ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). The investigation only recovered router evidence because RutOS versions before 7.07 keep the event database through a factory reset ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). On the plant side, restoring the Siemens controllers to factory settings and reloading logic backups shortened the outage but deleted the controllers' own logs, and Siemens ProductCERT confirmed they could not be recovered ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)).

**Defender takeaway:** a private APN is not a private network in the sense operators tend to assume — it is a shared layer-3 segment with other subscribers' devices on it, and CERT Polska's recommendations treat it accordingly: audit the APN configuration and enable client isolation between end devices, treat the APN as untrusted from the OT side with segmentation and traffic control at least equal to a corporate WAN boundary (and equal to the internet where the organisation cannot verify its configuration), allowlist only the connections the business function requires between the OT network and the APN gateway device, monitor that traffic for deviation from the expected communication profile, centralise logging on the gateway devices, minimise administrative services reachable from the APN, change default credentials on everything connected to it, and pull private APNs into penetration-test and architecture-review scope ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)). For hunting, the useful telemetry classes are the carrier-side and device-side session records rather than anything on a corporate endpoint: administrative logins on cellular routers and controller web interfaces, SSH sessions originating from a router's APN-facing interface where none should exist, scans for industrial protocol ports sourced from inside the APN rather than the engineering network, and PLC run-state transitions outside a maintenance window.

**Triage:** an engineering contractor doing legitimate remote maintenance also logs into a cellular router and reaches PLCs over S7, so neither event alone separates the two. The discriminators here are direction and sequence — the session enters from the APN side of a device whose administrative interface was never meant to face it, port scanning precedes the PLC access by days, and the run-state change is followed within minutes by configuration writes to unrelated serial servers and switches. This plant's operators initially read the shutdown as contractor error during scheduled maintenance and reported it for information only; CERT Polska opened an investigation anyway because it knew of similar events, which is what turned an unexplained failure into a confirmed intrusion ([CERT Polska, 2026-08-08](https://cert.pl/uploads/docs/CERT_Polska_Energy_Sector_Incident_Follow_up_Report_2025.pdf)).
