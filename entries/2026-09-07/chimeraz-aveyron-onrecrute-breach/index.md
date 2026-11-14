---
schema: 1
kind: incident
title: "ChimeraZ claims France's Département de l'Aveyron employment platform, exposing 20,000+ people's data including 1,499 CVs — a customer account without MFA, an IDOR flaw and a misconfigured Odoo database, per one of two trackers who reviewed the leak"
headline: "ChimeraZ expands beyond its fire-and-rescue targets to a French department's job-seeker platform, exposing CVs and personal data for over 20,000 people"
summary: >
  The criminal-forum handle ChimeraZ — already tracked for a recurring data-theft campaign against
  French departmental fire-and-rescue services (SDIS) — claims to have exfiltrated and published
  data from OnRecrute.EnAveyron.fr, the Département de l'Aveyron's employment platform, exposing
  23,381 records covering 20,316 people plus roughly 1,499 PDF CVs. One of two independent
  reviewers of the leaked files attributes access to a no-MFA customer account combined with an IDOR
  flaw reaching a misconfigured Odoo database; the other declines to confirm any mechanism. No
  statement has been issued by the Département or the platform operator.
discovered_at: "2026-09-07T04:40:00Z"
updated_at: null
event_date: "2026-09-05"
run_id: 2026-09-07T0411Z-intel
priority: notable
immediate_action: null
tags:
  - data-breach
  - organized-crime
  - identity
regions:
  - europe
sectors:
  - public-sector
entities:
  - "actor:chimeraz"
  - "incident:aveyron-onrecrute-chimeraz-breach-2026-09"
techniques:
  - T1078
  - T1190
  - T1213
affected_products:
  - "Odoo"
cves: []
sources:
  - url: "https://frenchbreaches.com/alertes/aveyron-mtp0hyfwss6ietkec1q"
    publisher: "FrenchBreaches"
    date: "2026-09-06"
    role: primary
  - url: "https://www.cyberattaque.org/aveyron-cyberattaque-emplois/"
    publisher: "Cyberattaque.org"
    date: "2026-09-06"
    role: primary
closed_sources: []
evidence:
  - quote: "Selon nos informations, la fuite aurait été rendue possible par la compromission d'un compte client dépourvu de double authentification, combinée à une faille IDOR donnant accès à une base de données Odoo mal configurée. Aucune détection de l'activité malveillante n'aurait eu lieu à ce jour. (translated from French: According to our information, the leak was made possible by the compromise of a client account lacking two-factor authentication, combined with an IDOR flaw granting access to a misconfigured Odoo database. No detection of the malicious activity has reportedly occurred to date.)"
    original: "Selon nos informations, la fuite aurait été rendue possible par la compromission d'un compte client dépourvu de double authentification, combinée à une faille IDOR donnant accès à une base de données Odoo mal configurée. Aucune détection de l'activité malveillante n'aurait eu lieu à ce jour."
    publisher: "FrenchBreaches"
  - quote: "Le hacker ne précise toutefois pas la méthode utilisée pour obtenir ces informations. Rien ne permet à ce stade de déterminer si l'accès provient directement de la plateforme d'emploi, de son extranet ou d'un autre composant de l'écosystème En Aveyron. (translated from French: The hacker does not, however, specify the method used to obtain this information. Nothing at this stage allows us to determine whether the access came directly from the employment platform, its extranet, or another component of the wider En Aveyron ecosystem.)"
    original: "Le hacker ne précise toutefois pas la méthode utilisée pour obtenir ces informations. Rien ne permet à ce stade de déterminer si l'accès provient directement de la plateforme d'emploi, de son extranet ou d'un autre composant de l'écosystème En Aveyron."
    publisher: "Cyberattaque.org"
  - quote: "Le pirate ChimeraZ revendique les données de 20 316 personnes ainsi que près de 1 500 documents PDF, dont des CV contenant de nombreuses informations personnelles et professionnelles. (translated from French: The hacker ChimeraZ claims the data of 20,316 people plus nearly 1,500 PDF documents, including CVs containing extensive personal and professional information.)"
    original: "Le pirate ChimeraZ revendique les données de 20 316 personnes ainsi que près de 1 500 documents PDF, dont des CV contenant de nombreuses informations personnelles et professionnelles."
    publisher: "FrenchBreaches"
verification: multi-source
sourcing_note: >
  Two independent breach-tracking outlets (FrenchBreaches, Cyberattaque.org) each state they
  obtained and directly analysed the leaked files rather than merely relaying the forum post, and
  both corroborate the same scope (23,381 records / 20,316 people / ~1,499 PDFs). The access-vector
  claim is single-sourced to FrenchBreaches alone and explicitly contradicted by Cyberattaque.org's
  refusal to confirm any mechanism; both accounts are carried and attributed rather than merged.
  No victim statement exists from the Département de l'Aveyron, the ADAT, or the platform operator.
  Reliability is set to C (fairly reliable) rather than FrenchBreaches' own tracked B: the two
  co-primary trackers contradict each other on the access mechanism and neither is a victim
  statement, so the blended sourcing for this specific item is weaker than FrenchBreaches' general
  track record alone would suggest.
confidence: medium
references:
  - "2026-08-31/france-sdis-fire-rescue-data-leak-campaign"
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

The threat actor ChimeraZ — a criminal-forum handle already tracked for a recurring data-theft campaign against French departmental fire-and-rescue services — claimed on 5 September 2026 to have exfiltrated and published data from OnRecrute.EnAveyron.fr, an employment and CV platform the Département de l'Aveyron operates through its Agence Départementale de l'Attractivité et du Tourisme (ADAT). Two independent breach-tracking outlets, FrenchBreaches and Cyberattaque.org, each state they obtained and personally analysed the leaked files rather than relaying the forum post, and both corroborate the same scope: 23,381 records covering 20,316 people, plus roughly 1,499 PDF documents (~451 MB) — predominantly job-seeker CVs — for a claimed total of ~465 MB ([FrenchBreaches, 2026-09-06](https://frenchbreaches.com/alertes/aveyron-mtp0hyfwss6ietkec1q); [Cyberattaque.org, 2026-09-06](https://www.cyberattaque.org/aveyron-cyberattaque-emplois/)). Exposed fields include names, email addresses, phone numbers, postal codes and communes, plus — within the CVs specifically — dates of birth, driving-licence status, education, employment history and named former employers ([FrenchBreaches, 2026-09-06](https://frenchbreaches.com/alertes/aveyron-mtp0hyfwss6ietkec1q)). Cyberattaque.org notes several candidate profiles were created or updated as recently as August 2026, indicating the exposed data is live production data rather than a stale archive ([Cyberattaque.org, 2026-09-06](https://www.cyberattaque.org/aveyron-cyberattaque-emplois/)).

The two trackers diverge sharply on how access was obtained, and neither account is a victim statement. FrenchBreaches alone reports the mechanism as a compromised customer account lacking multi-factor authentication, combined with an IDOR (Insecure Direct Object Reference) flaw that reached a misconfigured Odoo database from which the data was extracted, and adds that no detection of the malicious activity has occurred to date ([FrenchBreaches, 2026-09-06](https://frenchbreaches.com/alertes/aveyron-mtp0hyfwss6ietkec1q)). Cyberattaque.org, which independently obtained and reviewed the same files, explicitly declines to confirm any mechanism, stating that the hacker did not specify the access method and that nothing in the leak establishes whether access came from the employment platform itself, its extranet, or another component of the wider "En Aveyron" ecosystem ([Cyberattaque.org, 2026-09-06](https://www.cyberattaque.org/aveyron-cyberattaque-emplois/)). No statement has been issued by the Département de l'Aveyron, the ADAT, or the platform operator as of this run.

ChimeraZ is already tracked for the SDIS fire-and-rescue campaign, tied by name to five of seven French departmental fire-and-rescue services (SDIS) hit in an August 2026 wave; an earlier July 2026 wave against five further SDIS was attributed only collectively to three handles including ChimeraZ, with no per-unit breakdown. This incident shows the same forum handle now reaching French departmental administrative services outside that vertical, via a suspected third-party customer-account foothold into a business-application (Odoo) backend rather than the fire-and-rescue-specific access this actor was previously observed using. The pattern — an outsourced business-application backend reachable through a customer account without MFA — is directly transferable to Swiss cantonal and communal administrations running comparable outsourced CRM- or ERP-backed citizen or partner portals.

**Defender takeaway:** any organization that grants partner or third-party accounts access to a business-application backend (Odoo, or a comparable CRM/ERP platform) should confirm MFA is enforced for those accounts specifically, not only for internal staff logins, and should audit object-level authorization checks on any endpoint that a partner account can reach — an IDOR flaw reaching a misconfigured database backend is a low-sophistication, high-yield access path that requires no memory-corruption exploit and leaves the platform's own detection blind if, as claimed here, no anomalous access was flagged.
