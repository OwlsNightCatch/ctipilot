---
schema: 1
kind: threat
title: "The Gentlemen affiliate: an SSL-VPN account without MFA, a Windows Server 2003 host and a dormant local administrator gave Domain Admin in under an hour; the GPO locker most likely lost a replication race, so antivirus was disabled estate-wide but only one host was encrypted (Ransom-ISAC)"
headline: "Ransom-ISAC: Gentlemen affiliate, VPN without MFA to Domain Admin in an hour; GPO locker likely lost a replication race"
summary: >
  Ransom-ISAC's incident-response report describes an early-August 2026 intrusion by a Gentlemen ransomware affiliate that began with an SSL-VPN account without MFA and reached Domain Admin in under an hour, most likely with credentials taken from an end-of-life Windows Server 2003 host that a dormant local administrator account opened, then used a Rust credential harvester and the EtherRAT implant. The locker's GPO disabled antivirus across the estate but the task that runs it most likely never reached clients because of a replication race, so the locker ran on one host; the report names the telemetry at each step. Single source, no victim named.
discovered_at: "2026-11-15T04:28:58Z"
updated_at: null
event_date: "2026-11-13"
run_id: 2026-11-15T0356Z-intel
priority: notable
immediate_action: null
tags: [ransomware, identity]
regions: [global]
sectors: []
entities: ["actor:thegentlemen", "malware:etherrat"]
techniques: [T1133, T1078, T1135, T1558.003, T1110, T1078.003, T1078.002, T1021.006, T1105, T1003, T1555, T1547.001, T1048, T1484.001, T1685, T1685.005, T1486, T1059.001, T1059.007, T1102.001, T1568, T1490]
affected_products: []
cves: []
sources:
  - url: "https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/"
    publisher: "Ransom-ISAC"
    date: "2026-11-13"
    role: primary
closed_sources: []
evidence:
  - quote: "Everything here comes from a single incident response engagement."
    publisher: "Ransom-ISAC"
    source_url: "https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/"
  - quote: "The GPO still turned off the antivirus across the estate, but the locker ran on only one host."
    publisher: "Ransom-ISAC"
    source_url: "https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/"
verification: single-source
sourcing_note: >
  Single source: Ransom-ISAC draws on forensic images of two domain controllers, event logs of 41 hosts and firewall logs from one engagement, and names no victim. The locker wiped the logs of the host it encrypted, so conclusions about that host rest on peer hosts. Ransom-ISAC could not prove how the Domain Admin session was obtained and says the credential was most likely taken from the legacy host; it attributes the locker to The Gentlemen from the ransom-note name, the encrypted-file footer and the file extension, and also saw a claim of responsibility.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Ransom-ISAC reconstructs an early-August 2026 intrusion into a small company by a Gentlemen ransomware affiliate from forensic images of two domain controllers, event logs of 41 hosts and firewall logs ([Ransom-ISAC, 2026-11-13](https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/)). Entry was an SSL-VPN account without MFA that succeeded on the first attempt from an unusual country; neither egress address appears in any earlier failed login, so the credential was most likely held beforehand. Within the hour the actor ran an anonymous SMB sweep, three Kerberoast-style service-ticket requests (the KDC logged an RC4 and DES downgrade against an AES-only account) and hundreds of failed SMB logons against a domain controller, then used a dormant, weak-password local administrator on an end-of-life Windows Server 2003 SQL host that allowed null sessions. A Domain Admin session opened on the domain controller less than an hour after the first login; Ransom-ISAC could not prove how and says the credentials were most likely taken from that host. The actor then pushed a Rust credential harvester, which takes the DPAPI domain backup key, and EtherRAT, a Node.js implant that reads its command address from an Ethereum smart contract and never reached it; data left through the VPN tunnel over about two days of a weekend ([Ransom-ISAC, 2026-11-13](https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/)).

The locker, run on a domain controller in domain-wide mode, built a GPO linked enforced at the domain root and the Domain Controllers container, with eight registry values that disable antivirus and a Preferences scheduled task in SYSVOL. The call that declares the Preferences extension reached a domain controller the GPO had not replicated to, the script suppressed the error and no client read the task: antivirus was off estate-wide but the locker ran on one host, which wiped its logs ([Ransom-ISAC, 2026-11-13](https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/)).

**Exposure:** an SSL-VPN gateway with accounts that lack MFA, and any end-of-life host reachable from the VPN address pool that allows null sessions or keeps dormant local administrators.

**Detection:** in KDC and authentication logs, RC4 or DES advertised against an AES-only account, bursts of SMB logon failures from one client (expired-password answers show valid credentials) and null-session logons with random sixteen-character workstation names followed by a dormant local account's logon on a legacy host; in directory change records, a new GPO linked enforced at the domain root or a Preferences task file written into SYSVOL outside the management console; on servers, a Run value named like a browser updater, `node.exe` fed its script on standard input by a `node.exe` parent, resolution of three or more public Ethereum RPC providers and antivirus preference changes that disable real-time monitoring ([Ransom-ISAC, 2026-11-13](https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/)).

**Triage:** scanners and inventory tools also sweep SMB anonymously and legacy applications use null sessions (the finding is a dormant account logging on right after); developers resolve Ethereum RPC providers, so scope that rule to servers; administrators edit GPOs, so correlate with the change calendar ([Ransom-ISAC, 2026-11-13](https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/)).

**Defender takeaway:** Ransom-ISAC concludes that the actor needed one credential without MFA and one end-of-life server to reach Domain Admin ([Ransom-ISAC, 2026-11-13](https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/)), so MFA on every SSL-VPN account and retiring or isolating the legacy host with its dormant local administrator each remove a link; Ransom-ISAC advises that a GPO of this shape found in a domain be unlinked and deleted, with its Preferences task file, before hosts are cleaned or credentials rotated ([Ransom-ISAC, 2026-11-13](https://ransom-isac.org/blog/the-gentlemen-incident-locked-out/)).
