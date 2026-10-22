---
schema: 1
kind: incident
title: "Foxconn confirms a cyberattack on some North American factories after Nitrogen claims theft of 8 TB of customer project data"
headline: "Foxconn confirms a cyberattack on North American factories; Nitrogen claims 8 TB of Apple, Nvidia and other project data"
summary: "Foxconn confirmed on 2026-05-12 that some of its North American factories suffered a cyberattack and were resuming normal production, after the Nitrogen ransomware group claimed on 2026-05-11 to have stolen 8 TB, more than 11 million files of instructions, project documentation and technical drawings related to Intel, Apple, Google, Dell and Nvidia projects; Foxconn declined to confirm that any customer data was taken. Workers at the Mount Pleasant, Wisconsin plant reported a network outage from 2026-05-01, and Coveware has documented a bug in Nitrogen's ESXi encryptor that leaves files unrecoverable even by the attackers."
discovered_at: "2026-05-13T05:00:00Z"
event_date: 2026-05-12
run_id: 2026-05-13-c148b9a5
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - supply-chain
regions:
  - us
sectors:
  - manufacturing
entities:
  - "incident:foxconn-nitrogen-2026"
  - "actor:nitrogen"
techniques: [T1486]
affected_products: []
cves: []
sources:
  - url: "https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144"
    publisher: "The Register"
    date: "2026-05-12"
    role: primary
  - url: "https://therecord.media/foxconn-confirms-cyberattack-north-american-factories"
    publisher: "The Record"
    date: "2026-05-12"
    role: corroborating
  - url: "https://9to5mac.com/2026/05/12/apple-supplier-foxconn-confirms-ransomware-attack-affected-north-american-factories/"
    publisher: "9to5Mac"
    date: "2026-05-12"
    role: corroborating
  - url: "https://www.coveware.com/blog/2026/2/2/nitrogen-ransomware-esxi-malware-has-a-bug"
    publisher: "Coveware"
    date: "2026-02-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The affected factories are currently resuming normal production"
    publisher: "The Record"
    source_url: "https://therecord.media/foxconn-confirms-cyberattack-north-american-factories"
  - quote: "A spokesperson for the company confirmed the incident but declined to provide specifics on how many factories in North America were impacted."
    publisher: "The Record"
    source_url: "https://therecord.media/foxconn-confirms-cyberattack-north-american-factories"
  - quote: "stolen 8 TB of data comprising more than 11 million files"
    publisher: "The Register"
    source_url: "https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144"
  - quote: "Foxconn declined to confirm that these - or any - customers' information was hoovered up in the digital intrusion."
    publisher: "The Register"
    source_url: "https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144"
  - quote: "Any ESXi encrypted files that are without viable backups, must be analyzed in conjunction with the corresponding malware that encrypted them to ascertain their status."
    publisher: "Coveware"
    source_url: "https://www.coveware.com/blog/2026/2/2/nitrogen-ransomware-esxi-malware-has-a-bug"
verification: multi-source
sourcing_note: >
  Foxconn confirms only that some North American factories suffered a cyberattack; the data-theft figures are Nitrogen's own claim,
  the Mount Pleasant timeline comes from workers quoted by The Cybersec Guru via 9to5Mac, and Coveware's encryptor analysis predates
  this incident.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-13.md
updates:
  - at: "2026-10-21T20:56:23Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Foxconn confirmed only that some North American factories suffered a cyberattack and were resuming
      production, without naming sites or confirming that customer data was taken; the Mount Pleasant
      timeline comes from workers, Houston from AppleInsider, and the state list from The Record's
      description of where Foxconn has factories. Coveware's finding is that a bug in one Nitrogen ESXi
      encryptor leaves files unrecoverable even for the attackers, so recovery depends on checking
      encrypted files against the specific sample, not on the claim that paying never restores VMs.
    fields: [affected_products, body, classification, confidence, evidence, headline, priority, sources, sourcing_note, summary, techniques, title, entities]
---

Foxconn said some of its factories in North America suffered a cyberattack, that its cybersecurity team activated its response mechanism to keep production and delivery going and that the affected factories were resuming normal production; a spokesperson declined to say how many factories were hit ([The Record, 2026-05-12](https://therecord.media/foxconn-confirms-cyberattack-north-american-factories)), and Foxconn declined to confirm that any customer's information was taken ([The Register, 2026-05-12](https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144)). The Nitrogen ransomware gang took credit on Monday 2026-05-11 ([The Record, 2026-05-12](https://therecord.media/foxconn-confirms-cyberattack-north-american-factories)), claiming 8 TB of data comprising more than 11 million files, with confidential instructions, internal project documentation and technical drawings related to projects at Intel, Apple, Google, Dell and Nvidia, among others ([The Register, 2026-05-12](https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144)). Workers at the Mount Pleasant, Wisconsin campus reported a network collapse from Friday 2026-05-01, according to The Cybersec Guru as quoted by 9to5Mac, and AppleInsider reports that a Houston, Texas facility also appears to have been affected ([9to5Mac, 2026-05-12](https://9to5mac.com/2026/05/12/apple-supplier-foxconn-confirms-ransomware-attack-affected-north-american-factories/)). Nitrogen's ransomware is believed to have been created with a builder based on the defunct Conti ransomware, and Barracuda describes the group as first observed in 2023 ([The Record, 2026-05-12](https://therecord.media/foxconn-confirms-cyberattack-north-american-factories)); Coveware found that a coding mistake in Nitrogen's ESXi encryptor overwrites four bytes of the public key, so files are encrypted with a corrupted key that nobody, the attackers included, can decrypt ([Coveware, 2026-02-02](https://www.coveware.com/blog/2026/2/2/nitrogen-ransomware-esxi-malware-has-a-bug)).

**Exposure:** Foxconn's customers, whose project documentation Nitrogen claims to hold, although Foxconn has not confirmed that any customer data was taken ([The Register, 2026-05-12](https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144)).

**Defender takeaway:** after a Nitrogen encryption of ESXi hosts, analyse the encrypted files against the specific encryptor sample before relying on a decryptor, since the encryptor Coveware examined leaves files without viable backups unrecoverable ([Coveware, 2026-02-02](https://www.coveware.com/blog/2026/2/2/nitrogen-ransomware-esxi-malware-has-a-bug)); no access vector is public, so the incident changes no patching or detection decision.

## Correction — 2026-10-21T20:56:23Z

Foxconn's statement confirms that some of its North American factories suffered a cyberattack and are resuming normal production; it does not name sites, a start time or how long production stopped, and Foxconn declined to say how many factories were hit or to confirm that customer data was taken ([The Record, 2026-05-12](https://therecord.media/foxconn-confirms-cyberattack-north-american-factories); [The Register, 2026-05-12](https://www.theregister.com/cyber-crime/2026/05/12/foxconn-confirms-cyberattack-after-nitrogen-claims-apple-nvidia-data-theft/5239144)). Wisconsin, Ohio, Texas, Virginia, Indiana and several sites in Mexico are where Foxconn has factories, and Foxconn declined to say how many were impacted ([The Record, 2026-05-12](https://therecord.media/foxconn-confirms-cyberattack-north-american-factories)); the Mount Pleasant outage from 2026-05-01 comes from workers quoted by The Cybersec Guru, and Houston from AppleInsider ([9to5Mac, 2026-05-12](https://9to5mac.com/2026/05/12/apple-supplier-foxconn-confirms-ransomware-attack-affected-north-american-factories/)). Coveware's finding concerns Nitrogen's ESXi encryptor, whose bug leaves files unrecoverable even for the attackers, and its advice is to analyse encrypted files against the specific malware sample before assuming they can or cannot be recovered ([Coveware, 2026-02-02](https://www.coveware.com/blog/2026/2/2/nitrogen-ransomware-esxi-malware-has-a-bug)).
