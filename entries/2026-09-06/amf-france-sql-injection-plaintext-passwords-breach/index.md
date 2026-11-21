---
schema: 1
kind: incident
title: >
  Association des maires de France confirms a UNION-based SQL-injection breach exposing 114,000
  records on mayors, municipal councillors and territorial agents — plaintext passwords included
headline: >
  A SQL-injection flaw in France's national mayors' association exposes elected officials'
  contact data and plaintext credentials
summary: >
  The Association des maires de France (AMF), France's national association of more than 34,000
  member municipalities, confirmed on 2026-09-04 that its membership/subscription web application
  at amf.asso.fr had been breached via a UNION-based SQL-injection flaw. The claimed dataset totals
  roughly 114,000 rows covering names, contact details, municipality affiliation, job title and
  subscription data for mayors, elected officials, municipal councillors and territorial agents —
  alongside a separate table of plaintext passwords, stored independent of a properly hashed table.
  AMF has confirmed the breach occurred but not the claimed scope, and has notified France's
  data-protection authority (CNIL) while it is still scoping the incident.
discovered_at: "2026-09-06T04:40:00Z"
updated_at: null
event_date: "2026-09-04"
run_id: 2026-09-06T0409Z-intel
priority: notable
immediate_action: null
tags: [data-breach, sqli, identity]
regions: [europe]
sectors: [public-sector]
entities: ["incident:amf-france-sql-injection-breach-2026-09"]
techniques: [T1190]
affected_products: ["Association des maires de France membership portal (amf.asso.fr)"]
cves: []
sources:
  - url: "https://frenchbreaches.com/alertes/association-des-maires-de-france-mtmsxq04rjndct88z4p"
    publisher: "FrenchBreaches"
    date: "2026-09-04"
    role: primary
  - url: "https://www.clubic.com/actualite-628315-alerte-fuite-de-donnees-l-association-des-maires-de-france-touchee-par-une-cyberattaque.html"
    publisher: "Clubic"
    date: "2026-09-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "A hacker going by the pseudonym \"Alduin\" claimed this attack on a hacker forum, explaining that he exploited a UNION-type SQL injection to access the AMF's database."
    original: "Un hacker dont le pseudonyme est « Alduin » a en effet revendiqué sur un forum de hackers cette attaque, et a expliqué avoir exploité une injection SQL (de type Union) pour accéder à la base de données de l'AMF."
    publisher: "Clubic"
    source_url: "https://www.clubic.com/actualite-628315-alerte-fuite-de-donnees-l-association-des-maires-de-france-touchee-par-une-cyberattaque.html"
  - quote: "The AMF has just confirmed the reality of this cyberattack, and has referred the matter to the CNIL."
    original: "L'AMF vient de confirmer la réalité de cette cyberattaque, et elle a saisi la CNIL de cette question."
    publisher: "Clubic"
    source_url: "https://www.clubic.com/actualite-628315-alerte-fuite-de-donnees-l-association-des-maires-de-france-touchee-par-une-cyberattaque.html"
  - quote: "The analysis of the disclosed material also shows the presence of authentication data in certain tables"
    original: "L’analyse des éléments diffusés montre également la présence de données d’authentification dans certaines tables"
    publisher: "FrenchBreaches"
    source_url: "https://frenchbreaches.com/alertes/association-des-maires-de-france-mtmsxq04rjndct88z4p"
verification: single-source
sourcing_note: >
  FrenchBreaches is the originating technical analysis; Clubic's own reporting names FrenchBreaches
  as its sole source, so the two are one assessor rather than independent corroboration. What lifts
  this above a bare criminal forum claim is that AMF itself confirmed the reality of the
  attack and referred the matter to CNIL, per Clubic's reporting — a victim confirmation, though
  relayed through press rather than a direct AMF statement this entry could independently fetch.
  Credibility is held at 2 accordingly: the underlying technical claim (the UNION-SQLi mechanism,
  the 114,000-row count, the plaintext-password table) traces to one analyst's reading of the
  claimed leak, not to AMF's own technical disclosure.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Audit any communal-association, cantonal-conference or federal member-directory web application for parameterised-query discipline against UNION-based SQL injection, and specifically check whether any legacy credential-storage path retains plaintext passwords alongside — or instead of — a properly hashed table."
updates: []
migrated_from: null
---

France's Association des maires de France (AMF), the national association representing more than 34,000 member municipalities, confirmed on 2026-09-04 that its membership and subscription database at amf.asso.fr had been breached ([Clubic, 2026-09-04](https://www.clubic.com/actualite-628315-alerte-fuite-de-donnees-l-association-des-maires-de-france-touchee-par-une-cyberattaque.html); [FrenchBreaches, 2026-09-04](https://frenchbreaches.com/alertes/association-des-maires-de-france-mtmsxq04rjndct88z4p)). An attacker using the handle "Alduin" claimed on a hacking forum to have exploited a UNION-type SQL-injection flaw against the amf.asso.fr web application to pull data from multiple database tables ([FrenchBreaches, 2026-09-04](https://frenchbreaches.com/alertes/association-des-maires-de-france-mtmsxq04rjndct88z4p)). The claimed dataset totals roughly 114,000 entries — a single person can appear in multiple rows — covering names, municipality or intercommunality affiliation, job title, subscription type and dates ([Clubic, 2026-09-04](https://www.clubic.com/actualite-628315-alerte-fuite-de-donnees-l-association-des-maires-de-france-touchee-par-une-cyberattaque.html)), and, per FrenchBreaches' own file analysis, professional and personal email addresses and internal identifiers tied to mayors, elected officials, municipal councillors, directors general of services and other territorial agents ([FrenchBreaches, 2026-09-04](https://frenchbreaches.com/alertes/association-des-maires-de-france-mtmsxq04rjndct88z4p)). That same analysis found authentication data present across two distinct tables: bcrypt password hashes in one, and a separate table holding passwords stored in plaintext ([FrenchBreaches, 2026-09-04](https://frenchbreaches.com/alertes/association-des-maires-de-france-mtmsxq04rjndct88z4p)) — the source does not state whether the two tables cover the same account population, but the plaintext table alone is a basic-hygiene failure regardless: any account whose credentials landed in it had its password exposed in fully recoverable form. AMF has confirmed the incident and referred it to France's data-protection authority (CNIL) ([Clubic, 2026-09-04](https://www.clubic.com/actualite-628315-alerte-fuite-de-donnees-l-association-des-maires-de-france-touchee-par-une-cyberattaque.html)); FrenchBreaches reports AMF is still scoping the leak's extent and says affected individuals will be notified once its internal audit concludes ([FrenchBreaches, 2026-09-04](https://frenchbreaches.com/alertes/association-des-maires-de-france-mtmsxq04rjndct88z4p)). No patch, remediation timeline, or web-application-firewall/input-validation fix has been publicly stated by AMF as of this writing.

A UNION-based SQL injection against a membership or subscription portal is a textbook input-validation gap on a public-facing form or query parameter — the specific field or endpoint has not been named publicly. The combined dataset (identity, function, municipality data alongside a separate plaintext-credential table) enables both targeted spear-phishing of named mayors and directors general and credential-stuffing against any other portal where an affected individual reused a password exposed in the plaintext table.

**Defender takeaway:** this is a direct functional analogue to any body that aggregates contact and subscription data across many communes — a cantonal association of municipalities, a communal-administration federation, or an equivalent body in the constituency's own federal/cantonal/communal structure. Two concrete checks follow from this incident's own mechanics: audit member-directory or subscription-portal web applications for parameterised-query discipline against UNION-based injection specifically, since that is the stated technique; and check whether any legacy credential-storage path retains plaintext passwords alongside a hashed table, since that is what turned a data-exposure incident into a full credential-theft incident here. Neither check is generic advice — both are what this specific breach's own mechanics demand.

**Triage:** no source describes what executed after the SQL injection succeeded, so no process-level or endpoint discriminator is offered here; the observable is at the web-application layer — database-query logs or a web-application firewall showing UNION SELECT patterns against the affected application's parameters, and unusually large result-set exports from a member-facing query endpoint that normally returns single-record lookups.
