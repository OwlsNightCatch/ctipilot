---
schema: 1
kind: threat
horizon: operational
title: "FSB Centre 16 (Static Tundra) router-hijacking campaign: 19-agency joint advisory, formal Poland energy-grid attribution and first joint EU/UK cyber sanctions"
headline: "19-agency advisory details FSB Centre 16 router hijacking via SNMP and Cisco Smart Install as the UK and EU attribute Poland's Dec-2025 grid sabotage"
summary: >
  A joint Cybersecurity Advisory from 19 agencies across 13 countries (2026-07-13) details how Russian FSB Centre 16 (Static Tundra / Berserk Bear) opportunistically compromises internet-facing routers across energy, government, telecom, finance and healthcare — chiefly by abusing default/weak SNMP community strings and the seven-year-old Cisco Smart Install flaw CVE-2018-0171 (CISA KEV) to exfiltrate device configurations. On the same day the UK and EU formally attributed the destructive 29 Dec 2025 attack on Poland's energy grid to this FSB unit and imposed their first joint cyber-sanctions package. Swiss and European critical-infrastructure operators running Cisco IOS/IOS XE or legacy SNMP on exposed network devices should treat router hygiene as an active-exploitation priority.
discovered_at: "2026-07-13T12:40:00Z"
event_date: "2026-07-13"
run_id: 2026-07-13T1212Z-intel
priority: high
immediate_action: null
tags: [nation-state, espionage, actively-exploited, cisa-kev, wiper, law-enforcement, ot-ics, russia-nexus]
regions: [global, europe]
sectors: [energy, public-sector, telco, finance, healthcare, defense]
entities: [actor:static-tundra, actor:secretblizzard, actor:sandworm, incident:poland-energy-grid-attack-2025-12-29]
techniques: [T1595.001, T1595.002, T1027, T1602.001, T1602.002, T1003, T1583.003, T1090, T1071, T1048, T1584.008, T1588.005, T1190, T1068, T1078, T1601.001, T1485]
affected_products: ["Cisco IOS", "Cisco IOS XE"]
cves:
  - id: CVE-2018-0171
    cvss: "9.8"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "Cisco IOS / IOS XE devices with the Smart Install (SMI) client feature enabled"
    fixed: "Patched by Cisco in 2018; primary mitigation is disabling Smart Install (`no vstack`)"
sources:
  - url: "https://www.ncsc.gov.uk/news/uk-and-allies-urge-critical-sectors-to-improve-defences-against-russian-intelligence-targeting"
    publisher: "NCSC-UK"
    date: "2026-07-13"
    role: primary
  - url: "https://media.defense.gov/2026/Jul/09/2003959498/-1/-1/1/CSA_IMPROVE_ROUTER_HYGIENE.PDF"
    publisher: "NSA / CISA / FBI / DC3 joint Cybersecurity Advisory (19 agencies, 13 countries)"
    date: "2026-07-13"
    role: primary
  - url: "https://www.gov.uk/government/news/uk-and-eu-strike-russian-cyber-networks-with-new-sanctions"
    publisher: "UK Government (FCDO)"
    date: "2026-07-13"
    role: primary
  - url: "https://cert.pl/en/posts/2026/01/incident-report-energy-sector-2025/"
    publisher: "CERT Polska"
    date: "2026-01-30"
    role: primary
  - url: "https://blog.talosintelligence.com/static-tundra/"
    publisher: "Cisco Talos"
    date: "2025-08-20"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/eu-and-uk-hit-russia-with-first-joint-cyber-sanctions-package/"
    publisher: "BleepingComputer"
    date: "2026-07-13"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/sandworm-hackers-linked-to-failed-wiper-attack-on-polands-energy-systems/"
    publisher: "BleepingComputer"
    date: "2026-01-24"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The actors scan for Internet IP ranges with active Simple Network Management Protocol (SNMP) agents that accept common or default community strings for authentication"
    publisher: "NSA / CISA / FBI / DC3 joint Cybersecurity Advisory (19 agencies, 13 countries)"
  - quote: "The UK together with EU member states has also today formally attributed the December 2025 attack on Poland's energy grid to Russia's FSB Centre 16."
    publisher: "NCSC-UK"
  - quote: "This is, however, the first publicly described destructive activity attributed to this activity cluster."
    publisher: "CERT Polska"
  - quote: "This reckless attack failed but could have caused 500,000 citizens to lose electricity in the depths of winter."
    publisher: "UK Government (FCDO)"
verification: multi-source
sourcing_note: "The router-hygiene tradecraft is confirmed by the advisory's 19 authoring and co-sealing agencies across 13 countries. The cluster label for the Poland grid attack is contested across sources: CERT Polska (infrastructure overlap) and the UK/EU attribute it to the Static Tundra / Berserk Bear cluster under FSB Centre 16, while earlier ESET reporting (via BleepingComputer, 2026-01-24) attributed the same DynoWiper attack to the GRU-linked Sandworm cluster, and the EU Council statement separately names FSB Centre 16 as also controlling Turla — i.e. FSB Centre 16 is a parent unit spanning multiple tracked clusters, not a single group."
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: apt-campaign
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions:
  - "Disable Cisco Smart Install (`no vstack`) and confirm CVE-2018-0171 is remediated on every internet-facing IOS/IOS XE device, and alert on inbound SNMP Set-Requests carrying the config-copy OIDs named in the advisory (1.3.6.1.4.1.9.9.96.1.1 Cisco Config Copy; 1.3.6.1.4.1.9.9.96.1.1.1.1.5 Config Copy Server Address) — both are in-use FSB Centre 16 access and config-exfiltration vectors."
migrated_from: null
---

**Background.** The FSB Centre 16 network-device cluster is not new — it has a decade-plus public record under the vendor labels Berserk Bear, Energetic Bear, Crouching Yeti, Dragonfly and Ghost Blizzard, and Cisco Talos profiled it in August 2025 as "Static Tundra," documenting long-term compromise of unpatched and end-of-life network gear for configuration theft and persistent collection ([Cisco Talos, 2025-08-20](https://blog.talosintelligence.com/static-tundra/)). What is new is a same-day trio of actions on 2026-07-13: a much fuller TTP disclosure, a formal government attribution of a destructive attack, and the first coordinated EU/UK cyber-sanctions package.

A joint Cybersecurity Advisory carrying 19 authoring and co-sealing agencies across 13 countries — NSA, CISA, FBI and DC3 (US) alongside the cyber and intelligence authorities of Australia, Canada, New Zealand, the UK, Czech Republic, Denmark, Estonia, Finland, France, Italy, Poland and Sweden — describes FSB Centre 16 opportunistically compromising poorly configured routers across communications, defense industrial base, energy, financial services, government (especially state/local), and healthcare sectors ([NSA/CISA/FBI joint advisory, 2026-07-13](https://media.defense.gov/2026/Jul/09/2003959498/-1/-1/1/CSA_IMPROVE_ROUTER_HYGIENE.PDF); [NCSC-UK, 2026-07-13](https://www.ncsc.gov.uk/news/uk-and-allies-urge-critical-sectors-to-improve-defences-against-russian-intelligence-targeting)). The advisory notes these TTPs overlap with Salt Typhoon activity, so the hardening below counters more than one actor.

The primary access vector is not a novel exploit but weak SNMP hygiene. The actors scan internet IP ranges for SNMP agents that accept common or default community strings, then issue spoofed-source SNMP Set-Requests carrying object identifiers that instruct the device to copy its running configuration to a file (commonly `config.bkp` or `output.txt`) and transfer it, usually over TFTP, to a leased VPS or a compromised FTP server ([joint advisory, 2026-07-13](https://media.defense.gov/2026/Jul/09/2003959498/-1/-1/1/CSA_IMPROVE_ROUTER_HYGIENE.PDF)). The advisory names the exact OIDs abused — `1.3.6.1.4.1.9.9.96.1.1` (Cisco Config Copy) and `1.3.6.1.4.1.9.9.96.1.1.1.1.5` (the destination address for the copied config). A stolen configuration frequently discloses further credentials and additional community strings, feeding lateral movement. Talos's profile records the actor guessing or reusing insecure read-write community strings such as `public` and `anonymous` ([Cisco Talos, 2025-08-20](https://blog.talosintelligence.com/static-tundra/)). Secondarily — "occasionally," per the advisory — the actors exploit known Cisco bugs and the Smart Install (SMI) feature, naming CVE-2018-0171 (the Smart Install pre-auth RCE, in CISA KEV since 2021) and CVE-2008-4128 (end-of-life devices only, no patch). Persistence has historically included the SYNful Knock IOS firmware implant.

**The Poland grid attribution.** On the same day, the UK together with EU member states formally attributed the destructive 29 December 2025 attack on Poland's energy grid to FSB Centre 16 ([NCSC-UK, 2026-07-13](https://www.ncsc.gov.uk/news/uk-and-allies-urge-critical-sectors-to-improve-defences-against-russian-intelligence-targeting)). CERT Polska's own incident report describes coordinated destructive activity against 30-plus wind and photovoltaic grid-connection substations — RTU, HMI and protection-relay firmware damaged or system files deleted — and a combined heat-and-power plant serving roughly half a million people, where wiper malware was blocked by the operator's EDR before detonation; CERT Polska tied the activity to the Static Tundra / Berserk Bear / Ghost Blizzard / Dragonfly cluster via VPS, router and anonymizing-infrastructure overlap and called it "the first publicly described destructive activity attributed to this activity cluster" ([CERT Polska, 2026-01-30](https://cert.pl/en/posts/2026/01/incident-report-energy-sector-2025/)). Note the attribution is contested at the cluster-label level: earlier ESET reporting attributed the same DynoWiper attack to the GRU's Sandworm ([BleepingComputer, 2026-01-24](https://www.bleepingcomputer.com/news/security/sandworm-hackers-linked-to-failed-wiper-attack-on-polands-energy-systems/)), and the EU Council statement names FSB Centre 16 as the parent controlling several groups including Turla — so treat "FSB Centre 16" as an umbrella unit rather than a single team.

The sanctions package is the policy layer: the EU designated 9 individuals and 4 entities and the UK designated 24, covering senior GRU figures, the front company IMPULS accused of recruiting hackers for GRU Unit 29155, Lumma Stealer operators, and the disinformation outlet Rybar LLC ([UK Government, 2026-07-13](https://www.gov.uk/government/news/uk-and-eu-strike-russian-cyber-networks-with-new-sanctions); [BleepingComputer, 2026-07-13](https://www.bleepingcomputer.com/news/security/eu-and-uk-hit-russia-with-first-joint-cyber-sanctions-package/)).

**Detection.** The telemetry classes to prioritise on network gear: network-flow and firewall logs for inbound SNMP Set-Requests (especially with spoofed or unfamiliar source addresses) and for outbound TFTP sessions initiated from a router/switch management interface to non-management destinations; device syslog and AAA/TACACS+ logs for unexpected "config copy" events, new local-account creation, and unexplained drops in logging volume — Talos documents the actor tampering with TACACS+ configuration to blind logging and standing up GRE tunnels to redirect victim traffic ([Cisco Talos, 2025-08-20](https://blog.talosintelligence.com/static-tundra/)); and IDS rules keyed to inbound SNMP Set-Requests carrying the config-copy OIDs above, as the advisory recommends ([joint advisory, 2026-07-13](https://media.defense.gov/2026/Jul/09/2003959498/-1/-1/1/CSA_IMPROVE_ROUTER_HYGIENE.PDF)). Baseline NetFlow for the new GRE tunnel endpoints Talos describes.

**Defender takeaway.** For a Swiss or European CI operator this is a router-hygiene mandate with a live destructive precedent next door. Disable Smart Install where it is not in active use, confirm CVE-2018-0171 is patched, migrate management SNMP to v3 with authPriv and disable SNMPv1/v2c (or, where legacy SNMP is unavoidable, replace every default/weak community string and enforce read-only), restrict all management protocols to known stations via out-of-band ACLs, use Cisco password hashing type 8 (never 0/4/7), and treat the device configuration held in your management system — not the device itself — as the source of truth so a tampered config is detectable.

**Triage:** legitimate network-management stations poll SNMP on a predictable cadence from a known IP set, almost always read-only GET/GET-NEXT. The signal is a *write* (SNMP Set-Request) — particularly one carrying the config-copy OIDs — from a source outside the management range or with an inconsistent/spoofed source address, followed by an outbound TFTP transfer from the device; either alone is weak, the sequence config-write-then-TFTP-egress is the discriminator.
