---
schema: 1
kind: threat
title: "k0t: Group-IB and NyxLab describe a probable access broker that mass-exploits FortiWeb and PAN-OS GlobalProtect, brute-forces FortiGate and decrypts stolen FortiGate configurations offline with the default key, with victims later listed by Qilin and The Gentlemen"
headline: "Group-IB: k0t takes edge devices in bulk and decrypts FortiGate configurations offline; enable private-data-encryption"
summary: >
  Group-IB and NyxLab report a campaign by an operator they track as k0t that finds exposed FortiGate, FortiWeb and PAN-OS
  GlobalProtect devices in bulk, exploits FortiWeb CVE-2025-64446 and GlobalProtect CVE-2026-0257 or brute-forces FortiGate logins,
  downloads each FortiGate configuration and decrypts its stored LDAP, Active Directory and administrator secrets offline with the
  default FortiOS key, which cannot be seen on the appliance. Group-IB then sees hands-on Active Directory work, remote-management
  persistence and exfiltration, and victims that later appear on the Qilin and The Gentlemen leak sites; it assesses the operators
  as probable initial-access brokers but says the link to either group is unconfirmed.
discovered_at: "2026-10-22T03:46:00Z"
updated_at: null
event_date: "2026-10-21"
run_id: 2026-10-22T0256Z-intel
priority: notable
immediate_action: null
tags: [organized-crime, ransomware, identity]
regions: [global]
sectors: []
entities: ["actor:k0t", "tool:adaptixc2", "product:fortinet-fortiweb", "product:fortinet-fortigate", "product:meshcentral-meshagent", "incident:fortibleed-fortigate-credential-exposure"]
techniques: [T1190, T1596.005, T1110.001, T1133, T1136.001, T1602.002, T1552.001, T1550.004, T1003.001, T1003.002, T1003.004, T1003.006, T1558.003, T1187, T1068, T1219, T1567.002, T1569.002, T1053.005, T1110.003, T1550.002, T1059.001, T1018, T1046, T1135, T1069.002, T1083, T1518.001, T1078.003]
affected_products: ["Fortinet FortiWeb", "Fortinet FortiGate", "Palo Alto Networks PAN-OS"]
cves:
  - id: CVE-2025-64446
    cvss: "9.8 (CVSS 3.x, Fortinet FG-IR-25-910)"
    epss: null
    type: path-traversal
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "FortiWeb 8.0.0 through 8.0.1, 7.6.0 through 7.6.4, 7.4.0 through 7.4.9, 7.2.0 through 7.2.11 and 7.0.0 through 7.0.11; 6.4 and FortiAppSec Cloud are not affected"
    fixed: "8.0.2, 7.6.5, 7.4.10, 7.2.12, 7.0.12; interim: disable HTTP and HTTPS on internet-facing interfaces"
  - id: CVE-2019-6693
    cvss: "4.3 (CVSS 3.x, Fortinet FG-IR-19-007)"
    epss: null
    type: info-disclosure
    vector: local
    auth: post-auth
    status: [exploited, cisa-kev, mitigation-only]
    affected: "Fortinet FortiOS configuration data encrypted with the default key (Fortinet lists 6.2.0, 6.0.0 through 6.0.6 and 5.6.10 and below); a device keeps using that key until private-data-encryption is enabled"
    fixed: "FortiOS 5.6.11, 6.0.7 and 6.2.1 and later add the private-data-encryption option, disabled by default, which makes FortiOS encrypt with an operator-defined key"
  - id: CVE-2026-0257
    cvss: "7.8 (CVSS-B 4.0, Palo Alto's rating)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "PAN-OS 12.1, 11.2, 11.1, 10.2 and older GlobalProtect portals and gateways with authentication-override cookies and the relevant certificate configuration enabled; Prisma Access 11.2 and 10.2"
    fixed: "12.1.4-h6 or 12.1.7; 11.2.4-h17, 11.2.7-h14, 11.2.10-h7 or 11.2.12; 11.1.4-h33, 11.1.6-h32, 11.1.7-h6, 11.1.10-h25, 11.1.13-h5 or 11.1.15; 10.2.7-h34, 10.2.10-h36, 10.2.13-h21, 10.2.16-h7 or 10.2.18-h6; Prisma Access 11.2.7-h13 and 10.2.10-h36 (upgraded by Palo Alto)"
sources:
  - url: "https://www.group-ib.com/blog/stray-cat-network-edge/"
    publisher: "Group-IB (with NyxLab)"
    date: "2026-10-21"
    role: primary
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-25-910"
    publisher: "Fortinet PSIRT (FG-IR-25-910, Path confusion vulnerability in GUI)"
    date: "2025-11-14"
    role: corroborating
  - url: "https://fortiguard.fortinet.com/psirt/FG-IR-19-007"
    publisher: "Fortinet PSIRT (FG-IR-19-007, Hardcoded symmetric key in fips.c)"
    date: "2019-11-19"
    role: corroborating
  - url: "https://security.paloaltonetworks.com/CVE-2026-0257"
    publisher: "Palo Alto Networks PSIRT (CVE-2026-0257 advisory)"
    date: "2026-05-13"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.21)"
    date: "2026-10-21"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Large-scale campaign involving vulnerability exploitation and brute-forcing of exposed network devices"
    publisher: "Group-IB (with NyxLab)"
    source_url: "https://www.group-ib.com/blog/stray-cat-network-edge/"
  - quote: "Many victims seen in this campaign have also been observed to be later listed by ransomware groups, Qilin and the Gentlemen, on their Data Leak Sites (DLS)."
    publisher: "Group-IB (with NyxLab)"
    source_url: "https://www.group-ib.com/blog/stray-cat-network-edge/"
  - quote: "Because this decryption is performed against a copy of the configuration held by the operator, it is not detectable on the appliance itself and cannot be prevented by access control alone"
    publisher: "Group-IB (with NyxLab)"
    source_url: "https://www.group-ib.com/blog/stray-cat-network-edge/"
  - quote: "Enable the ‘private-data-encryption’ setting on FortiGate appliances and supply an operator-defined key."
    publisher: "Group-IB (with NyxLab)"
    source_url: "https://www.group-ib.com/blog/stray-cat-network-edge/"
verification: single-source
sourcing_note: >
  Group-IB with NyxLab is the only source for the campaign and its tooling; the three CVEs are independently listed in CISA's
  Known Exploited Vulnerabilities catalog. Group-IB itself calls the link to the Qilin and The Gentlemen operators unconfirmed.
confidence: medium
references:
  - "2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen"
  - "2026-06-18/fortibleed-73-932-internet-facing-fortigate-devices-exposed"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On every FortiGate (FortiOS 5.6.11, 6.0.7, 6.2.1 or later; check the FortiManager and HA note in Fortinet's FG-IR-19-007 first where it applies), enable private-data-encryption with an operator-defined key, and for any device that was internet-reachable with a brute-forceable administrator login or an unpatched exposed service, treat the LDAP and Active Directory bind and administrator credentials stored in its configuration as known to the attacker and rotate them, bind accounts first."
updates:
  - at: "2026-10-25T13:41:38Z"
    run_id: 2026-10-25T1308Z-audit
    type: improvement
    internal: true
    summary: >
      The CVE records for CVE-2025-64446 and CVE-2019-6693 left the score empty; they now carry Fortinet's
      own CVSS 3 scores from FG-IR-25-910 (9.8) and FG-IR-19-007 (4.3).
    fields: [cves]
migrated_from: null
---

Group-IB and NyxLab describe a campaign by an operator they track as k0t (Group-IB lists CryptoFeel as a potential alias, and Scrooge as a likely collaborator and possible alias) that enumerates internet-facing VPN and firewall appliances in bulk and attacks the product directly, chiefly Fortinet firewalls and Palo Alto GlobalProtect portals ([Group-IB, 2026-10-21](https://www.group-ib.com/blog/stray-cat-network-edge/)). A custom script exploits CVE-2025-64446 against FortiWeb, a relative path traversal that lets an unauthenticated attacker run administrative commands, or brute-forces exposed Fortinet devices as a fallback ([Group-IB, 2026-10-21](https://www.group-ib.com/blog/stray-cat-network-edge/); [CISA KEV, 2026-10-21](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). Against PAN-OS it exploits CVE-2026-0257, the GlobalProtect authentication bypass, with a forged authentication-override cookie ([Group-IB, 2026-10-21](https://www.group-ib.com/blog/stray-cat-network-edge/)). On a compromised FortiGate the tool downloads the configuration and decrypts its secrets locally with the default FortiOS key, the weakness tracked as CVE-2019-6693, recovering LDAP and Active Directory bind and, Group-IB says, administrator credentials, although Fortinet's advisory excludes the administrator's password and says FIPS-CC devices are not impacted; unless private-data-encryption is set, the device falls back to that known key ([Group-IB, 2026-10-21](https://www.group-ib.com/blog/stray-cat-network-edge/); [Fortinet, 2019-11-19](https://fortiguard.fortinet.com/psirt/FG-IR-19-007)).

After access the operators work by hand with NetExec, Impacket, Kerbrute, relayed PetitPotam and Mimikatz, keep access through OpenConnect, MeshCentral agents, AdaptixC2, Atera and AnyDesk, and exfiltrate with Rclone to Wasabi and MEGA ([Group-IB, 2026-10-21](https://www.group-ib.com/blog/stray-cat-network-edge/)). Group-IB sees victim overlap with the Qilin and The Gentlemen leak sites and assesses the operators are probably initial-access brokers, but says no relationship is confirmed, and it found indications of a possible connection with the FortiBleed cluster alongside negligible overlap in the compromised credentials ([Group-IB, 2026-10-21](https://www.group-ib.com/blog/stray-cat-network-edge/)). CISA lists all three CVEs in KEV, with ransomware use marked known for CVE-2026-0257 and CVE-2019-6693 ([CISA KEV, 2026-10-21](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

**Exposure:** internet-reachable FortiGate administrator and VPN logins, FortiWeb up to 8.0.1, 7.6.4, 7.4.9, 7.2.11 or 7.0.11 on its branch ([Fortinet, 2025-11-14](https://fortiguard.fortinet.com/psirt/FG-IR-25-910)), and PAN-OS GlobalProtect portals and gateways below the per-branch fixed builds ([Palo Alto Networks, 2026-05-13](https://security.paloaltonetworks.com/CVE-2026-0257)); every FortiGate except FIPS-CC models is exposed to the offline decryption step once its configuration has been downloaded unless private-data-encryption, available from FortiOS 5.6.11, 6.0.7 and 6.2.1 and off by default, is enabled with an operator-defined key, which Fortinet warns can cause install errors and split-brain on FortiManager-managed or HA FortiGates until FortiManager 6.2.7 and FortiGate 6.2.6, 6.4.4 or 6.6.0 and later ([Group-IB, 2026-10-21](https://www.group-ib.com/blog/stray-cat-network-edge/); [Fortinet, 2019-11-19](https://fortiguard.fortinet.com/psirt/FG-IR-19-007)).

**Detection:** on edge appliances, unexpected local administrator creation, configuration exports, trusted-host changes, repeated authentication failures, lockout-and-retry patterns and administration from unusual source addresses; on directory infrastructure, the NetExec, Impacket and relay pattern against domain controllers; on endpoints, remote-management agents and dual-use tools without an approved owner. The decryption leaves no trace on the appliance, so a patched or cleaned device may already have yielded its secrets ([Group-IB, 2026-10-21](https://www.group-ib.com/blog/stray-cat-network-edge/)). After upgrading FortiWeb, Fortinet advises reviewing configuration and logs for unexpected changes and unauthorised administrator accounts, and until then disabling HTTP and HTTPS on internet-facing interfaces ([Fortinet, 2025-11-14](https://fortiguard.fortinet.com/psirt/FG-IR-25-910)).

**Triage:** OpenConnect, MeshCentral, Atera, AnyDesk and Rclone are legitimate tools, so Group-IB advises judging execution context, installation source, operator account, destination and timing rather than tool names ([Group-IB, 2026-10-21](https://www.group-ib.com/blog/stray-cat-network-edge/)).

**Defender takeaway:** enable private-data-encryption with an operator-defined key on every FortiGate and rotate the directory and administrator secrets stored in any configuration that may have left the device, because patching or rebuilding does not undo a copy already decrypted; Group-IB also advises investigating lockout events and raising the lockout time against brute force ([Group-IB, 2026-10-21](https://www.group-ib.com/blog/stray-cat-network-edge/)).
