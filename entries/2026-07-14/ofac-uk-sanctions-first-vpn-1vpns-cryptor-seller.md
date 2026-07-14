---
schema: 1
kind: incident
horizon: operational
title: "US and UK sanction First VPN Service (1VPNS), its administrator and a Belarusian cryptor seller — the sanctions follow-through on the Swiss-assisted Operation Saffron takedown"
headline: "OFAC and the UK sanction the 1VPNS bulletproof-VPN admin and a cryptor seller after the Swiss-backed First VPN takedown"
summary: >
  Following the May 2026 Operation Saffron takedown of First VPN Service (1VPNS) — in which Switzerland was a joint-investigation-team partner — US Treasury OFAC and the UK FCDO on 2026-07-13 sanctioned 1VPNS, its administrator Dmytro Rashevskyi, and separately a Belarusian cryptor seller, Yegeniy Silayev, whose malware-obfuscation service is a distinct enabling layer beneath ransomware payloads. The service infrastructure is already down; the new development is the individual designations and the explicit targeting of the cryptor-as-a-service layer.
discovered_at: "2026-07-14T04:45:00Z"
event_date: 2026-07-13
run_id: 2026-07-14T0409Z-intel
priority: notable
immediate_action: null
tags:
  - law-enforcement
  - ransomware
  - organized-crime
regions:
  - us
  - europe
  - switzerland
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
  - url: "https://home.treasury.gov/news/press-releases/sb0559"
    publisher: "US Department of the Treasury (OFAC)"
    date: "2026-07-13"
    role: primary
  - url: "https://ofac.treasury.gov/recent-actions/20260713"
    publisher: "OFAC Recent Actions"
    date: "2026-07-13"
    role: primary
  - url: "https://www.fbi.gov/contact-us/field-offices/boston/news/fbi-boston-supports-international-takedown-of-first-vpn-service-used-by-ransomware-actors-to-compromise-businesses-worldwide"
    publisher: "FBI Boston Field Office"
    date: "2026-06-09"
    role: corroborating
closed_sources: []
evidence:
  - quote: "OFAC is designating two individuals and one entity enabling ransomware actors' and other cybercriminals' malign activities, notably ransomware attacks against Americans."
    publisher: "US Department of the Treasury (OFAC)"
  - quote: "cryptors are built specifically to make malware stealthier and more effective by disguising it as harmless files"
    publisher: "US Department of the Treasury (OFAC)"
  - quote: "This takedown was conducted by France's Direction Régionale de la Police Judiciaire Brigade de Lutte Contre la Cybercriminalité (BL2C), and the Dutch National Police, National High Tech Crime Unit (NHTC), with assistance from Ukraine, the United Kingdom, Switzerland, and Luxembourg."
    publisher: "FBI Boston Field Office"
verification: multi-source
sourcing_note: "First-party government sources (US Treasury OFAC and the FBI); the FBI FLASH (ic3.gov) referenced by both was not used for TTP specifics because its fetched text could not be verified verbatim this run."
confidence: high
update_of: 2026-05-22/operation-saffron-dismantles-first-vpn-33-servers-seized-use
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-05-22):** The May 2026 Operation Saffron takedown of First VPN Service (1VPNS) — the Russian-language, no-log criminal anonymisation service in which Switzerland sat on the Eurojust joint investigation team — has now drawn coordinated sanctions. On 2026-07-13 the US Treasury's Office of Foreign Assets Control, in an action coordinated with the UK's Foreign, Commonwealth & Development Office, designated 1VPNS and its administrator **Dmytro Rashevskyi** (who used false identities including "Maksim Sorin" and "Roman Chabanenko" to buy infrastructure from providers that would otherwise have refused him), and separately a Belarusian national, **Yegeniy Silayev**, who sells "cryptors" ([US Treasury, 2026-07-13](https://home.treasury.gov/news/press-releases/sb0559)). Treasury frames cryptors as tools "built specifically to make malware stealthier and more effective by disguising it as harmless files" ([US Treasury, 2026-07-13](https://home.treasury.gov/news/press-releases/sb0559)) — designating the obfuscation-service vendor as a distinct enabling layer beneath the ransomware payload and the affiliate, not just the anonymisation infrastructure. The designations were made under Executive Order 13694 as amended; the FBI confirms the underlying takedown was led by France's BL2C and the Dutch NHTC "with assistance from Ukraine, the United Kingdom, Switzerland, and Luxembourg," and that at least 25 ransomware groups, including Avaddon, used the service for reconnaissance and intrusions ([FBI Boston, 2026-06-09](https://www.fbi.gov/contact-us/field-offices/boston/news/fbi-boston-supports-international-takedown-of-first-vpn-service-used-by-ransomware-actors-to-compromise-businesses-worldwide)).

Treasury describes the concrete abuse pattern: ransomware groups purchased 1VPNS infrastructure and used it "to hide the origins of their attacks, deploy malware, and manage exfiltrated data" — an external commercial VPN used as an anonymising relay in front of the operators' own reconnaissance, delivery and exfiltration traffic ([US Treasury, 2026-07-13](https://home.treasury.gov/news/press-releases/sb0559)).

**Defender takeaway:** the operational picture is unchanged from May — the infrastructure is seized and historical flows to the 1vpns domains remain investigative leads through Europol channels — but the sanctions extend the disruption to the *cryptor-as-a-service* layer, a reminder that malware-obfuscation vendors are now first-class law-enforcement targets in their own right, distinct from the ransomware operators who buy from them. For finance-sector entities in the constituency the designations carry a routine SDN-screening obligation; there is no new host- or network-level defender action, and the US remediation framing does not change the operational priority of any control.
