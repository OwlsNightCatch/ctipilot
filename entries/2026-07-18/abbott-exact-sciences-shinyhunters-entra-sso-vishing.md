---
schema: 1
kind: incident
horizon: operational
title: >
  Abbott confirms a Cancer Diagnostics cyber incident; ShinyHunters claims a vished Entra SSO
  account and 30M+ records
headline: >
  Abbott confirms unauthorized access to its Cancer Diagnostics (Exact Sciences) systems as
  ShinyHunters claims a helpdesk-vishing to Entra SSO breach
summary: >
  Abbott Laboratories confirmed (2026-07-16) unauthorized access to a limited number of internal
  systems in its Cancer Diagnostics business (the acquired Exact Sciences unit) only. Separately,
  the ShinyHunters extortion group claims the intrusion began with a vishing call that compromised
  a Microsoft Entra ID single-sign-on account, then used it to pull 30M+ records from Entra,
  ServiceNow, SharePoint, Databricks and Coupa — a claim Abbott has neither confirmed nor
  attributed. The confirmed incident plus the same vishing-to-cloud-SSO tradecraft this actor uses
  against SaaS-integrated enterprises makes it relevant to healthcare and any
  SharePoint/Entra-dependent estate.
discovered_at: "2026-07-18T04:35:00Z"
updated_at: "2026-07-31T04:09:14Z"
event_date: 2026-07-16
run_id: 2026-07-18T0409Z-intel
priority: notable
immediate_action: null
tags:
  - data-breach
  - phishing
  - identity
  - cloud
  - organized-crime
regions:
  - global
  - us
  - europe
sectors:
  - healthcare
  - technology
entities:
  - "actor:shinyhunters"
  - "incident:brinks-home-shinyhunters-breach-2026-07"
techniques:
  - T1566.004
  - T1078.004
  - T1530
  - T1598.004
  - T1556.006
  - T1213.002
affected_products:
  - Microsoft Entra ID
  - Okta
  - Salesforce
  - Microsoft 365
  - Microsoft SharePoint
  - ServiceNow
cves: []
sources:
  - url: "https://www.abbott.com/en-us/corpnewsroom/diagnostics-testing/abbott-statement-on-cyber-incident-in-cancer-diagnostics-business"
    publisher: Abbott Laboratories (own statement)
    date: 2026-07-16
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/"
    publisher: BleepingComputer
    date: 2026-07-17
    role: corroborating
  - url: "https://www.medtechdive.com/news/abbott-discloses-cyberattack-on-cancer-diagnostics-business/825529/"
    publisher: MedTech Dive
    date: 2026-07-17
    role: corroborating
  - url: "https://health-isac.org/shiny-hunters-impact-to-health-sector-and-recommended-mitigation-strategies/"
    publisher: Health-ISAC
    date: 2026-07-24
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/health-isac-warns-of-rising-shinyhunters-data-theft-attacks-on-healthcare/"
    publisher: BleepingComputer
    date: 2026-07-29
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/shinyhunters-claims-brinks-home-breach-threatens-to-leak-stolen-data/"
    publisher: BleepingComputer
    date: 2026-07-30
    role: primary
closed_sources: []
evidence:
  - quote: Abbott is investigating a cyber incident in which there was unauthorized access to a limited number of internal systems in our Cancer Diagnostics business only.
    publisher: Abbott Laboratories (own statement)
  - quote: "ShinyHunters claimed it exfiltrated data from Microsoft Entra, ServiceNow, SharePoint, Databricks, and Coupa, including internal documents, contracts, and customer information."
    publisher: BleepingComputer
  - quote: "SSO is the control plane, and ShinyHunters' leverage is created through data theft at cloud scale."
    publisher: Health-ISAC
  - quote: "The advisory does not identify affected healthcare organizations, disclose how many incidents have been observed, or provide a timeframe for the reported increase."
    publisher: BleepingComputer
  - quote: "The intrusion did not impact in any way the company's alarm monitoring and system functionality."
    publisher: BleepingComputer
verification: multi-source
sourcing_note: >
  Abbott's own statement (Admiralty A for its own incident) confirms unauthorized access limited
  to the Cancer Diagnostics business and states legacy Exact Sciences systems are separate from
  Abbott's. The vishing-to-Entra-SSO method, the exfiltrated SaaS platforms and the 30M+ record
  counts are ShinyHunters' own leak-site claims relayed by BleepingComputer — unverified and not
  attributed by Abbott. Credibility rated 3 accordingly: the incident is confirmed, the actor's
  method and scope are a claim.
confidence: medium
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 3
watchlist_hit: false
actions: []
updates:
  - at: "2026-07-31T04:09:14Z"
    run_id: 2026-07-31T0409Z-intel
    type: update
    summary: >
      Health-ISAC issued a sector advisory on 2026-07-24 formalising the chain ShinyHunters runs
      against healthcare: voice phishing aimed at helpdesk staff, an MFA or password reset or device
      re-enrolment performed without out-of-band identity proofing, takeover of the Entra, Okta or
      Google SSO account, then pivoting into connected SaaS platforms and bulk-exfiltrating data as
      pure extortion leverage with no encryption. Its framing is that SSO is the control plane and
      should be locked down like a domain controller, and it explicitly cautions that not every
      data-theft claim has been verified, directing defenders at the attack pattern rather than the
      victim count. Brinks Home confirmed an intrusion detected on 2026-07-20 in which alarm
      monitoring was unaffected; ShinyHunters separately claims it began with an Entra voice-phishing
      call, a claim the company has not confirmed.
    fields:
      - affected_products
      - entities
      - evidence
      - regions
      - sectors
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-07-31/health-isac-shinyhunters-sso-tier0-advisory-brinks-home
migrated_from: null
---

Abbott Laboratories is investigating a cyber incident and states there was "unauthorized access to a limited number of internal systems in our Cancer Diagnostics business only," adding that there is "no impact to any other Abbott businesses, sites or systems" and that the legacy Exact Sciences systems (Exact Sciences was folded into Abbott's diagnostics business in a 2026 acquisition) remain separate from Abbott's core infrastructure ([Abbott, 2026-07-16](https://www.abbott.com/en-us/corpnewsroom/diagnostics-testing/abbott-statement-on-cyber-incident-in-cancer-diagnostics-business)). Abbott has not named an actor, confirmed a method, or disclosed what kind of information was accessed ([MedTech Dive, 2026-07-17](https://www.medtechdive.com/news/abbott-discloses-cyberattack-on-cancer-diagnostics-business/825529/)).

The **ShinyHunters** extortion group (registry-tracked, alias UNC6240) claims responsibility, saying the intrusion began with a vishing (voice-phishing) attack targeting several Abbott employees that compromised a Microsoft Entra ID single-sign-on account, which was then used to "exfiltrate data from Microsoft Entra, ServiceNow, SharePoint, Databricks, and Coupa" — the actor's leak-site posting claims more than 30 million customer records, medical notes and orders, and set a leak deadline it later pushed to 21 July ([BleepingComputer, 2026-07-17](https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/)). A second, separate claim by an actor calling itself "ShadowByt3\$" alleges compromise of an externally facing LabCentral portal, which BleepingComputer reports houses publicly available technical product reference documents and does not contain proprietary or sensitive customer or business information ([BleepingComputer, 2026-07-17](https://www.bleepingcomputer.com/news/security/abbott-laboratories-probes-two-cyber-incidents-amid-extortion-claims/)). The record counts and the specific SaaS platforms are the actor's unverified claim, not Abbott's confirmation.

**Defender takeaway:** the transferable signal is the actor's method, not the victim's name — the same vishing-to-cloud-SSO tradecraft ShinyHunters/UNC6240 has used against SaaS-integrated enterprises, now aimed at a large healthcare/diagnostics estate's Entra/ServiceNow/SharePoint/Databricks/Coupa stack, which mirrors the SharePoint-and-Entra default across Swiss and EU public-sector tenants. **Triage:** distinguish a legitimate help-desk-assisted MFA or device re-enrollment from a vished account takeover — the discriminators are an MFA-method change or new-device registration on an account immediately preceding a spike in bulk SaaS data-export activity, and Entra sign-in anomalies (unfamiliar device, unusual ISP/ASN, impossible travel) on the account in the hours before large read/export operations against ServiceNow, SharePoint, Databricks or Coupa.

## Update — 2026-07-31T04:09:14Z

Prior coverage tracked this actor's vishing-to-Entra-SSO tradecraft through the Abbott and Ernst & Young incidents as individual cases. The delta is that a sector body has now written the chain down as a pattern with a mitigation timeline attached, and that a fresh confirmed intrusion shows the same entry point ([BleepingComputer, 2026-07-29](https://www.bleepingcomputer.com/news/security/health-isac-warns-of-rising-shinyhunters-data-theft-attacks-on-healthcare/)).

Health-ISAC's advisory describes the chain end to end: voice phishing directed at helpdesk staff, leading to a password reset, MFA reset or device re-enrolment carried out without out-of-band identity proofing, giving the caller a legitimate Entra, Okta or Google SSO session; from there the operators pivot into the connected SaaS estate — Salesforce, Microsoft 365, SharePoint, ServiceNow, Teams — and exfiltrate in bulk. There is no encryption stage; the stolen data is the entire extortion instrument. Its own summary of why this works is the line worth quoting to a steering committee: SSO is the control plane, and the leverage comes from data theft at cloud scale. It recommends treating Entra, Okta and equivalent identity infrastructure as Tier 0, locked down the way a domain controller is, with a 30-to-60-day action list covering phishing-resistant MFA for high-risk users, hardened helpdesk reset procedures with verified callback, a conditional-access baseline blocking legacy authentication, SaaS-exfiltration detection on bulk downloads, API anomalies and OAuth-consent changes, and a tested token- and session-revocation playbook ([Health-ISAC, 2026-07-24](https://health-isac.org/shiny-hunters-impact-to-health-sector-and-recommended-mitigation-strategies/)).

Two things about how the advisory is written are as informative as its content. It names no victims at all — BleepingComputer states directly that it does not identify affected organisations, disclose how many incidents have been observed, or give a timeframe for the increase, and the medtech and healthcare companies frequently listed alongside it come from BleepingComputer's own earlier reporting rather than from the advisory. And Health-ISAC cautions that not every data-theft claim has been verified, directing defenders at the attack pattern rather than at any specific tally. For a sector body facing an actor whose business model is publicising claims, declining to repeat the claims is a deliberate and defensible choice.

The fresh case landed the following day. Brinks Home confirmed, through its chief executive, that it detected an intrusion on 2026-07-20, engaged forensic experts, and that the intrusion did not affect its alarm monitoring or system functionality in any way; its own incident FAQ says it has not yet confirmed exactly what information was involved or whose ([BleepingComputer, 2026-07-30](https://www.bleepingcomputer.com/news/security/shinyhunters-claims-brinks-home-breach-threatens-to-leak-stolen-data/)). ShinyHunters claims the breach began on 13 July with a call convincing an employee to complete a Microsoft Entra authentication or registration process, and claims specific volumes of Salesforce, employee and support-chat data; BleepingComputer reports two different Salesforce record counts in the same article without reconciling them, and states it has not reviewed the data and could not verify the claims. The mechanism the actor describes matches the pattern the advisory documents, which is the reason to note it — the numbers are not established and are not treated here as though they were.

**Detection.** Everything useful sits in identity telemetry, and the shape is a sequence rather than an event. The trigger is a helpdesk-initiated credential or authenticator change — a password reset, an MFA method reset, or a new device registered against an existing account. What turns it into an incident is what follows within minutes to hours: a first successful sign-in for that account from a device, network or geography with no history, then enumeration and bulk retrieval against connected SaaS applications — large report exports, unusual API query volume against customer-record objects, new OAuth consent grants. Instrument the join between the reset event and the next sign-in, because either half alone is ordinary.

**Triage:** a locked-out user calling the helpdesk and having their MFA reset is one of the most common legitimate identity events in any organisation, and it looks identical to this attack up to the moment the reset completes. The discriminator is not in the endpoint or the network — it is whether identity was proven out of band, by a callback to a number already on record rather than a number the caller supplied, and whether the sign-in that follows the reset comes from anywhere the account has been before. Where the helpdesk's own process logs that verification step, the absence of it on a given ticket is the highest-fidelity signal available.

**Defender takeaway:** the technique needs no vulnerability, no malware and no endpoint foothold, so patch state and EDR coverage are irrelevant to it — which is exactly why an advisory aimed at the sector puts identity infrastructure in the same tier as a domain controller. For Swiss and European healthcare and public-sector estates running the same Entra-plus-SaaS pattern, the honest self-assessment question is narrow: can your helpdesk reset an executive's MFA today on the strength of a convincing phone call, and if so, is that reset event visible to your SOC within minutes rather than at the next audit.
