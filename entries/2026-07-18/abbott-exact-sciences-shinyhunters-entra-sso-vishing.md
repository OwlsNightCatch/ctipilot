---
schema: 1
kind: incident
horizon: operational
title: "Abbott confirms a Cancer Diagnostics cyber incident; ShinyHunters claims a vished Entra SSO account and 30M+ records"
headline: "Abbott confirms unauthorized access to its Cancer Diagnostics (Exact Sciences) systems as ShinyHunters claims a helpdesk-vishing to Entra SSO breach"
summary: >
  Abbott Laboratories confirmed (2026-07-16) unauthorized access to a limited number of internal
  systems in its Cancer Diagnostics business (the acquired Exact Sciences unit) only. Separately, the
  ShinyHunters extortion group claims the intrusion began with a vishing call that compromised a
  Microsoft Entra ID single-sign-on account, then used it to pull 30M+ records from Entra, ServiceNow,
  SharePoint, Databricks and Coupa — a claim Abbott has neither confirmed nor attributed. The confirmed
  incident plus the same vishing-to-cloud-SSO tradecraft this actor uses against SaaS-integrated
  enterprises makes it relevant to healthcare and any SharePoint/Entra-dependent estate.
discovered_at: "2026-07-18T04:35:00Z"
event_date: "2026-07-16"
run_id: 2026-07-18T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, phishing, identity, cloud]
regions: [global, us]
sectors: [healthcare]
entities: ["actor:shinyhunters"]
techniques: [T1566.004, T1078.004, T1530]
affected_products: []
cves: []
sources:
  - url: "https://www.abbott.com/en-us/corpnewsroom/diagnostics-testing/abbott-statement-on-cyber-incident-in-cancer-diagnostics-business"
    publisher: "Abbott Laboratories (own statement)"
    date: "2026-07-16"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/"
    publisher: "BleepingComputer"
    date: "2026-07-17"
    role: corroborating
  - url: "https://www.medtechdive.com/news/abbott-discloses-cyberattack-on-cancer-diagnostics-business/825529/"
    publisher: "MedTech Dive"
    date: "2026-07-17"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Abbott is investigating a cyber incident in which there was unauthorized access to a limited number of internal systems in our Cancer Diagnostics business only."
    publisher: "Abbott Laboratories (own statement)"
  - quote: "ShinyHunters claimed it exfiltrated data from Microsoft Entra, ServiceNow, SharePoint, Databricks, and Coupa, including internal documents, contracts, and customer information."
    publisher: "BleepingComputer"
verification: multi-source
sourcing_note: "Abbott's own statement (Admiralty A for its own incident) confirms unauthorized access limited to the Cancer Diagnostics business and states legacy Exact Sciences systems are separate from Abbott's. The vishing-to-Entra-SSO method, the exfiltrated SaaS platforms and the 30M+ record counts are ShinyHunters' own leak-site claims relayed by BleepingComputer — unverified and not attributed by Abbott. Credibility rated 3 accordingly: the incident is confirmed, the actor's method and scope are a claim."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 3
watchlist_hit: false
actions: []
migrated_from: null
---

Abbott Laboratories is investigating a cyber incident and states there was "unauthorized access to a limited number of internal systems in our Cancer Diagnostics business only," adding that there is "no impact to any other Abbott businesses, sites or systems" and that the legacy Exact Sciences systems (Exact Sciences was folded into Abbott's diagnostics business in a 2026 acquisition) remain separate from Abbott's core infrastructure ([Abbott, 2026-07-16](https://www.abbott.com/en-us/corpnewsroom/diagnostics-testing/abbott-statement-on-cyber-incident-in-cancer-diagnostics-business)). Abbott has not named an actor, confirmed a method, or disclosed what kind of information was accessed ([MedTech Dive, 2026-07-17](https://www.medtechdive.com/news/abbott-discloses-cyberattack-on-cancer-diagnostics-business/825529/)).

The **ShinyHunters** extortion group (registry-tracked, alias UNC6240) claims responsibility, saying the intrusion began with a vishing (voice-phishing) attack targeting several Abbott employees that compromised a Microsoft Entra ID single-sign-on account, which was then used to "exfiltrate data from Microsoft Entra, ServiceNow, SharePoint, Databricks, and Coupa" — the actor's leak-site posting claims more than 30 million customer records, medical notes and orders, and set a leak deadline it later pushed to 21 July ([BleepingComputer, 2026-07-17](https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/)). A second, separate claim by an actor calling itself "ShadowByt3\$" alleges compromise of an externally facing LabCentral portal, which BleepingComputer reports houses publicly available technical product reference documents and does not contain proprietary or sensitive customer or business information ([BleepingComputer, 2026-07-17](https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/)). The record counts and the specific SaaS platforms are the actor's unverified claim, not Abbott's confirmation.

**Defender takeaway:** the transferable signal is the actor's method, not the victim's name — the same vishing-to-cloud-SSO tradecraft ShinyHunters/UNC6240 has used against SaaS-integrated enterprises, now aimed at a large healthcare/diagnostics estate's Entra/ServiceNow/SharePoint/Databricks/Coupa stack, which mirrors the SharePoint-and-Entra default across Swiss and EU public-sector tenants. **Triage:** distinguish a legitimate help-desk-assisted MFA or device re-enrollment from a vished account takeover — the discriminators are an MFA-method change or new-device registration on an account immediately preceding a spike in bulk SaaS data-export activity, and Entra sign-in anomalies (unfamiliar device, unusual ISP/ASN, impossible travel) on the account in the hours before large read/export operations against ServiceNow, SharePoint, Databricks or Coupa.
