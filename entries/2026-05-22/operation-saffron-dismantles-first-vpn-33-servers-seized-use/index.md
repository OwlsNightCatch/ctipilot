---
schema: 1
kind: threat
title: >
  Operation Saffron dismantles First VPN — 33+ servers seized, user database captured, Switzerland
  named JIT participant; Phobos RaaS infrastructure link confirmed
headline: >
  Operation Saffron dismantles First VPN — 33+ servers seized, user database captured, Switzerland
  named JIT participant; Phobos RaaS infrastructure link
summary: >
  Operation Saffron seizes First VPN — Europol/Eurojust-coordinated takedown of criminal
  anonymisation VPN present in "nearly every major cybercrime investigation"; 33+ servers seized
  across 27 countries (server-host), 5,000+ user accounts captured; Switzerland one of seven JIT
  participants; Phobos RaaS infrastructure link confirmed (Help Net Security, 2026-05-21).
discovered_at: "2026-05-22T05:00:00Z"
updated_at: "2026-07-14T04:45:00Z"
event_date: 2026-05-21
run_id: 2026-05-22-5b90d5a1
priority: high
immediate_action: null
tags:
  - law-enforcement
  - organized-crime
  - ransomware
regions:
  - europe
  - switzerland
  - us
sectors:
  - public-sector
  - finance
  - healthcare
entities:
  - "incident:operation-saffron-first-vpn-takedown-33-servers-27-countri"
techniques:
  - T1090.002
  - T1027.002
affected_products: []
cves: []
sources:
  - url: "https://www.eurojust.europa.eu/news/eurojust-coordinated-investigation-shuts-down-criminal-vpn-network"
    publisher: "Eurojust, 2026-05-21"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/police-seize-first-vpn-service-used-in-ransomware-data-theft-attacks/"
    publisher: "BleepingComputer, 2026-05-21"
    role: corroborating
  - url: "https://www.helpnetsecurity.com/2026/05/21/operation-saffron-first-vpn-takedown/"
    publisher: "Help Net Security, 2026-05-21"
    role: corroborating
  - url: "https://home.treasury.gov/news/press-releases/sb0559"
    publisher: US Department of the Treasury (OFAC)
    date: 2026-07-13
    role: primary
  - url: "https://ofac.treasury.gov/recent-actions/20260713"
    publisher: OFAC Recent Actions
    date: 2026-07-13
    role: primary
  - url: "https://www.fbi.gov/contact-us/field-offices/boston/news/fbi-boston-supports-international-takedown-of-first-vpn-service-used-by-ransomware-actors-to-compromise-businesses-worldwide"
    publisher: FBI Boston Field Office
    date: 2026-06-09
    role: corroborating
closed_sources: []
evidence:
  - quote: "OFAC is designating two individuals and one entity enabling ransomware actors' and other cybercriminals' malign activities, notably ransomware attacks against Americans."
    publisher: US Department of the Treasury (OFAC)
  - quote: cryptors are built specifically to make malware stealthier and more effective by disguising it as harmless files
    publisher: US Department of the Treasury (OFAC)
  - quote: "This takedown was conducted by France's Direction Régionale de la Police Judiciaire Brigade de Lutte Contre la Cybercriminalité (BL2C), and the Dutch National Police, National High Tech Crime Unit (NHTC), with assistance from Ukraine, the United Kingdom, Switzerland, and Luxembourg."
    publisher: FBI Boston Field Office
verification: multi-source
sourcing_note: null
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification: null
watchlist_hit: false
actions: []
updates:
  - at: "2026-07-14T04:45:00Z"
    run_id: 2026-07-14T0409Z-intel
    type: update
    summary: >
      Following the May 2026 Operation Saffron takedown of First VPN Service (1VPNS) — in which
      Switzerland was a joint-investigation-team partner — US Treasury OFAC and the UK FCDO on
      2026-07-13 sanctioned 1VPNS, its administrator Dmytro Rashevskyi, and separately a Belarusian
      cryptor seller, Yegeniy Silayev, whose malware-obfuscation service is a distinct enabling layer
      beneath ransomware payloads. The service infrastructure is already down; the new development is
      the individual designations and the explicit targeting of the cryptor-as-a-service layer.
    fields:
      - evidence
      - regions
      - sectors
      - sources
      - techniques
      - body
    merged_from: 2026-07-14/ofac-uk-sanctions-first-vpn-1vpns-cryptor-seller
migrated_from: briefs/2026-05-22.md
---

A coordinated international law enforcement action on 2026-05-19–20 took down First VPN, a Russian-language criminal anonymisation service established in 2014 and systematically marketed on cybercrime forums as a no-log, law-enforcement-resistant tool ([Eurojust, 2026-05-21](https://www.eurojust.europa.eu/news/eurojust-coordinated-investigation-shuts-down-criminal-vpn-network)). Europol stated the service "appeared in almost every major cybercrime investigation the agency supported" ([BleepingComputer, 2026-05-21](https://www.bleepingcomputer.com/news/security/police-seize-first-vpn-service-used-in-ransomware-data-theft-attacks/)). Led by French and Dutch investigators through a Eurojust joint investigation team established in November 2023, the operation seized more than 33 servers distributed across 27 countries (server-host count); 16 nations participated through Europol's Joint Cybercrime Action Taskforce; 7 nations sat on the Eurojust-led JIT, including Switzerland, France, Netherlands, Luxembourg, Romania, Ukraine, and the UK — signalling fedpol/GovCERT.ch operational involvement. Law enforcement arrested the administrator in Ukraine, captured the full user database (over 5,000 accounts) and cryptographic connection records, and generated 83 intelligence packages covering 506 users distributed to partner agencies; Help Net Security reporting confirms the captured data links to the Phobos ransomware-as-a-service operation and broader ransomware, fraud, and data theft investigations ([Help Net Security, 2026-05-21](https://www.helpnetsecurity.com/2026/05/21/operation-saffron-first-vpn-takedown/)). The primary domains (1vpns.com, 1vpns.net, 1vpns.org) and associated .onion mirrors were seized. Historical network flows to those domains in proxy or firewall logs now constitute potential investigative leads flowing through Europol sharing channels; Phobos affiliates have repeatedly targeted EU public-sector and healthcare organisations.

## Update — 2026-07-14T04:45:00Z

The May 2026 Operation Saffron takedown of First VPN Service (1VPNS) — the Russian-language, no-log criminal anonymisation service in which Switzerland sat on the Eurojust joint investigation team — has now drawn coordinated sanctions. On 2026-07-13 the US Treasury's Office of Foreign Assets Control, in an action coordinated with the UK's Foreign, Commonwealth & Development Office, designated 1VPNS and its administrator **Dmytro Rashevskyi** (who used false identities including "Maksim Sorin" and "Roman Chabanenko" to buy infrastructure from providers that would otherwise have refused him), and separately a Belarusian national, **Yegeniy Silayev**, who sells "cryptors" ([US Treasury, 2026-07-13](https://home.treasury.gov/news/press-releases/sb0559)). Treasury frames cryptors as tools "built specifically to make malware stealthier and more effective by disguising it as harmless files" ([US Treasury, 2026-07-13](https://home.treasury.gov/news/press-releases/sb0559)) — designating the obfuscation-service vendor as a distinct enabling layer beneath the ransomware payload and the affiliate, not just the anonymisation infrastructure. The designations were made under Executive Order 13694 as amended; the FBI confirms the underlying takedown was led by France's BL2C and the Dutch NHTC "with assistance from Ukraine, the United Kingdom, Switzerland, and Luxembourg," and that at least 25 ransomware groups, including Avaddon, used the service for reconnaissance and intrusions ([FBI Boston, 2026-06-09](https://www.fbi.gov/contact-us/field-offices/boston/news/fbi-boston-supports-international-takedown-of-first-vpn-service-used-by-ransomware-actors-to-compromise-businesses-worldwide)).

Treasury describes the concrete abuse pattern: ransomware groups purchased 1VPNS infrastructure and used it "to hide the origins of their attacks, deploy malware, and manage exfiltrated data" — an external commercial VPN used as an anonymising relay in front of the operators' own reconnaissance, delivery and exfiltration traffic ([US Treasury, 2026-07-13](https://home.treasury.gov/news/press-releases/sb0559)).

**Defender takeaway:** the operational picture is unchanged from May — the infrastructure is seized and historical flows to the 1vpns domains remain investigative leads through Europol channels — but the sanctions extend the disruption to the *cryptor-as-a-service* layer, a reminder that malware-obfuscation vendors are now first-class law-enforcement targets in their own right, distinct from the ransomware operators who buy from them. For finance-sector entities in the constituency the designations carry a routine SDN-screening obligation; there is no new host- or network-level defender action, and the US remediation framing does not change the operational priority of any control.
