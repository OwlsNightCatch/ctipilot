---
schema: 1
kind: research
horizon: operational
title: "Citizen Lab: a European Parliament spyware-inquiry member was himself infected twice with Pegasus"
headline: "Citizen Lab confirms Pegasus infected a PEGA-Committee MEP via the PWNYOURHOME zero-click chain"
summary: "Citizen Lab forensically confirmed that the iPhone of former MEP Stelios Kouloglou — a member of the European Parliament's PEGA committee investigating commercial-spyware abuse — was infected with NSO Group's Pegasus twice while he served on that committee (Oct 2022 via the PWNYOURHOME zero-click HomeKit→BlastDoor chain, and Mar 2023). The infections are unattributed but overlap a Pegasus operator also targeting Russian/Belarusian-speaking exiles in Europe. For SOCs protecting officials and oversight staff, the actionable surface is proactive mobile forensic triage and enforced device hardening, not endpoint alerting — the chain is zero-click."
discovered_at: "2026-07-03T18:25:00Z"
event_date: 2023-03-07
run_id: 2026-07-03T1809Z-intel
priority: notable
immediate_action: null
tags:
  - espionage
  - mobile
  - zero-click
regions:
  - europe
sectors:
  - public-sector
entities:
  - incident:pegasus-mep-kouloglou-pega-committee-2026
cves: []
sources:
  - url: "https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/"
    publisher: Citizen Lab
    role: primary
  - url: "https://therecord.media/pegasus-spyware-european-parliament-pega-committee-member"
    publisher: The Record (Recorded Future News)
    role: corroborating
closed_sources: []
evidence:
  - quote: "We found with high confidence that his device was successfully infected with Pegasus spyware on or around October 21, 2022, and again on March 6 and 7, 2023."
    publisher: Citizen Lab
  - quote: "PWNYOURHOME appeared to first involve the attacker sending a specially crafted NSKeyedArchive that landed in HomeKit, followed by malicious content that landed in MessagesBlastDoorService."
    publisher: Citizen Lab
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "For officials in oversight, diplomatic, or inquiry roles handling sensitive material: enrol government-issued iPhones in Lockdown Mode (or an MDM-enforced equivalent that disables HomeKit and rich iMessage/attachment parsing) and Apple's at-risk threat-notification program."
  - "Establish proactive mobile forensic triage for high-risk principals — run the Mobile Verification Toolkit (MVT) against iOS sysdiagnose/backup artefacts periodically rather than waiting for an alert; a zero-click chain leaves no phishing artefact to hunt on the endpoint."
migrated_from: null
---

Citizen Lab published a forensic report confirming, with high confidence, that the iPhone of Stelios Kouloglou — a former MEP who sat on the European Parliament's PEGA committee, the inquiry into commercial-spyware abuse — was infected with NSO Group's Pegasus on two occasions, around 21 October 2022 and 6–7 March 2023, while the device ran iOS 15.5 ([Citizen Lab, 2026-07-03](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/)). The 2022 infection used the PWNYOURHOME zero-click chain: a specially crafted `NSKeyedArchive` object landing in the HomeKit daemon, followed by malicious content processed by `MessagesBlastDoorService` (iMessage's sandboxed attachment parser) — a distinct path from earlier NSO chains that abused iMessage directly. Citizen Lab does not attribute the intrusion to any government and explicitly found no indication of Greek-government responsibility, but notes the targeting infrastructure overlaps a previously documented Pegasus campaign against Russian- and Belarusian-speaking exiled journalists and opposition figures in Europe, suggesting a single Pegasus customer with multi-country authorization ([The Record, 2026-07-03](https://therecord.media/pegasus-spyware-european-parliament-pega-committee-member)). Because Kouloglou sat on the committee scrutinising exactly this abuse, the operator would have gained visibility into confidential PEGA deliberations — an EU parliamentary-privilege and confidentiality concern. **Defender takeaway:** PWNYOURHOME is zero-click, so there is no user action or phishing artefact to detect at the endpoint; the realistic defensive surface for parliamentarians, diplomats, and inquiry staff is proactive forensic triage (MVT against iOS sysdiagnose/backups) plus mandated Lockdown Mode / hardened MDM configuration that strips HomeKit and rich-content parsing from official devices. This continues a 2026 pattern of Citizen Lab naming EU institutional targets of mercenary spyware, alongside its earlier Cellebrite/Pivovarov forensic work.
