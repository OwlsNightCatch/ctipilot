---
schema: 1
kind: incident
title: "Dutch IGJ: Clinical Diagnostics labs failed NEN 7510 at the time of the July 2025 Nova breach, which reached data of about 941,000 people through an account without MFA in unmonitored legacy systems"
headline: "Dutch inspectorate finds the hacked cervical-screening lab ran no NEN 7510 audit or periodic risk assessment"
summary: "The Dutch Health and Youth Care Inspectorate (IGJ) found on 2026-05-13 that Clinical Diagnostics LCPL and NMDL in Rijswijk did not meet the statutory NEN 7510 information-security standard during the July 2025 data hack or at a December 2025 inspection visit, citing no independent audit and no periodic risk assessment. According to Computable, attackers used a compromised account without multi-factor authentication in legacy environments that had dropped out of SOC monitoring, and data of about 941,000 people, mostly cervical-cancer screening participants, was viewed or stolen. IGJ cannot impose penalties, the Dutch data protection authority can and is investigating, and IGJ is calling on healthcare providers to prove NEN 7510 compliance, including at the labs they use."
discovered_at: "2026-05-14T05:00:00Z"
event_date: 2026-05-13
run_id: 2026-05-14-e05c6e6e
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - policy
regions:
  - europe
sectors:
  - healthcare
entities:
  - "incident:clinical-diagnostics-nmdl-igj-2026"
  - "actor:nova-raas"
techniques: [T1078, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging"
    publisher: "IGJ"
    date: "2026-05-13"
    role: primary
  - url: "https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/"
    publisher: "Computable"
    date: "2026-05-13"
    role: corroborating
  - url: "https://www.govinfosecurity.com/dutch-lab-cancer-screening-hack-balloons-to-941000-victims-a-29360"
    publisher: "GovInfoSecurity"
    date: "2025-09-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The investigation shows that the business units of Clinical Diagnostics involved did not meet the standard either at the time of the hack or during an inspection visit in December 2025. (translated from Dutch)"
    original: "Uit het onderzoek blijkt dat de betrokken bedrijfsonderdelen van Clinical Diagnostics zowel op het moment van de hack als tijdens een inspectiebezoek in december 2025 niet voldeden aan de norm."
    publisher: IGJ
    source_url: "https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging"
  - quote: "Working according to this standard could have reduced the likelihood of an information security incident like this and limited the consequences. (translated from Dutch)"
    original: "Het werken volgens deze norm had de kans op een informatiebeveiligingsincident als dit kunnen verkleinen en de gevolgen beperken."
    publisher: IGJ
    source_url: "https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging"
  - quote: "Under the Wabvpz the IGJ cannot impose punitive measures. The AP can do so under the GDPR. (translated from Dutch)"
    original: "Op basis van de Wabvpz kan de IGJ geen bestraffende maatregelen opleggen. De AP kan dat wel op basis van de AVG."
    publisher: IGJ
    source_url: "https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging"
  - quote: "However, no multi-factor authentication turned out to be active on the affected account. (translated from Dutch)"
    original: "Op het getroffen account bleek echter geen multi-factorauthenticatie actief."
    publisher: Computable
    source_url: "https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/"
verification: multi-source
sourcing_note: >
  IGJ's release is the primary for the compliance finding and the enforcement position; the access vector, the
  monitoring gap and IGJ's call on healthcare providers come from Computable's account of the inspection, and the Nova
  attribution and the patient count from 2025 reporting by GovInfoSecurity.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-14.md
updated_at: null
updates:
  - at: "2026-10-21T20:23:07Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      IGJ asked Clinical Diagnostics to demonstrate NEN 7510 compliance at short notice rather than
      demanding certification, the company reports a positive external audit, and IGJ's call on all
      healthcare providers to prove compliance, including at their labs, comes from Computable's account
      of the inspection. No source compares NEN 7510 with Switzerland's EPDG or describes Swiss providers,
      and IGJ says compliance could have reduced the likelihood and limited the consequences of the hack
      rather than calling the breach scale their proximate result. The Nova attribution and the count of
      about 941,000 people come from press reporting, and the lab could not confirm the full extent; a
      Dutch regulatory finding on a breach outside Switzerland moves from high to notable priority.
    fields: [affected_products, body, classification, entities, evidence, headline, priority, sources, sourcing_note, summary, tags, techniques, title]
---

The Dutch Health and Youth Care Inspectorate (IGJ) concluded on 2026-05-13 that the business units Clinical Diagnostics LCPL BV and NMDL BV in Rijswijk "did not meet the standard either at the time of the hack or during an inspection visit in December 2025" (translated from Dutch): among other gaps, no independent audit of information security had been carried out and processing risks had not been mapped periodically, so the company could not determine which data-security measures it needed ([IGJ, 2026-05-13](https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)). The Wabvpz requires organisations working with patient data to meet NEN 7510, and IGJ says working to the norm could have reduced the likelihood of an incident like this and limited its consequences ([IGJ, 2026-05-13](https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)).

Computable reports from the inspection that the company could not establish how the attackers gained access to the compromised user account, which had a 16-character password but no active multi-factor authentication, and that the legacy environments the attackers entered had dropped out of the security operations centre's monitoring through human error, because the SOC wrongly believed them inactive, so anomalous patterns in the logs went unnoticed ([Computable, 2026-05-13](https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/)). Data of about 941,000 people, mostly cervical-cancer screening participants, was viewed or stolen, and Computable reports that the company paid a ransom ([Computable, 2026-05-13](https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/)). The ransomware-as-a-service group Nova had threatened in July 2025 to leak the data, and the screening agency said the lab could not confirm that 941,000 was the full extent ([GovInfoSecurity, 2025-09-03](https://www.govinfosecurity.com/dutch-lab-cancer-screening-hack-balloons-to-941000-victims-a-29360)).

IGJ asked the company to demonstrate NEN 7510 compliance at short notice; under the Wabvpz it cannot impose punitive measures, while the Dutch data protection authority (AP), which is investigating under the GDPR, can, and the company says an external audit came out positive and certification is expected soon ([IGJ, 2026-05-13](https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)). IGJ is using the case to call on healthcare providers to work demonstrably to NEN 7510, with a certificate or an independent assessment, and to check actively that the labs and other third parties they use comply ([Computable, 2026-05-13](https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/)).

**Exposure:** healthcare providers in the Netherlands that process patient data are bound by NEN 7510 under the Wabvpz ([IGJ, 2026-05-13](https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)), and IGJ's supervision will now look at whether they verify their labs and other suppliers ([Computable, 2026-05-13](https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/)).

**Detection:** what hid this intrusion was monitoring coverage, not missing signatures: legacy environments that were still reachable had been dropped from SOC collection as inactive, and the account used had no second factor, so the checks that would have caught it are a reconciliation of SOC log sources against systems still reachable and a review of authentication logs for accounts without multi-factor authentication ([Computable, 2026-05-13](https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/)).

**Defender takeaway:** for any organisation whose sensitive data is processed by a laboratory or other service provider, ask for an independent assessment of that provider's information security, as IGJ now expects of Dutch healthcare providers, and confirm that legacy environments holding the data are either decommissioned or inside monitoring scope ([Computable, 2026-05-13](https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/)).

## Correction — 2026-10-21T20:23:07Z

IGJ asked Clinical Diagnostics to demonstrate NEN 7510 compliance at short notice rather than demanding certification, and the company reports a positive external audit with certification expected soon ([IGJ, 2026-05-13](https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)). IGJ's release speaks of a data hack and an inspection visit in December 2025; it says working to the norm could have reduced the likelihood of such an incident and limited its consequences, not that the breach scale was their proximate result, and it states no relationship to ISO/IEC 27001 ([IGJ, 2026-05-13](https://www.igj.nl/actueel/nieuws/2026/05/13/clinical-diagnostics-voldeed-niet-aan-wettelijke-norm-voor-informatiebeveiliging)). The call on all healthcare providers to prove NEN 7510 compliance, including at the labs they use, is reported by Computable from the inspection ([Computable, 2026-05-13](https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/)). Ransomware by Nova and the figure of 941,000 come from press reporting, and the screening agency said the lab could not confirm that this was the full extent ([GovInfoSecurity, 2025-09-03](https://www.govinfosecurity.com/dutch-lab-cancer-screening-hack-balloons-to-941000-victims-a-29360)).

No cited source compares NEN 7510 with Switzerland's electronic patient record rules or describes the security of Swiss providers; that comparison is removed. Computable's account of the inspection adds the access vector, a compromised account without multi-factor authentication in legacy environments that had dropped out of SOC monitoring ([Computable, 2026-05-13](https://www.computable.nl/2026/05/13/inspectie-vernietigend-over-beveiliging-clinical-diagnostics-na-datahack/)), which is what the detection guidance above now rests on.
