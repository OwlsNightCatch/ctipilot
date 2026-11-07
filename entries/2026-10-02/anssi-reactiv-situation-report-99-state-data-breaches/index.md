---
schema: 1
kind: research
title: "ANSSI's first REACTIV situation report: 99 data breaches reported against French state services since 1 August, driven by Metabase CVE-2026-72898, infostealer credentials without MFA, IDOR flaws and supplier rebound"
headline: "France's national authority names six causes behind two months of state data breaches, common to public-sector portals"
summary: >
  ANSSI's situation report of 2026-09-30 for its REACTIV operation counts 99 data breaches reported to it by French state
  services since 2026-08-01, 67 confirmed, and names the recurring causes: mass exploitation of the Metabase SQL
  injection CVE-2026-72898 (nine ministry instances compromised), infostealer-harvested credentials used on exposed
  services without a second factor, IDOR flaws, missing or weak MFA, and compromise through a supplier. The figures are
  provisional.
discovered_at: "2026-10-02T04:52:00Z"
updated_at: null
event_date: "2026-09-30"
run_id: 2026-10-02T0404Z-intel
priority: notable
immediate_action: null
tags: [data-breach, identity, supply-chain]
regions: [europe]
sectors: [public-sector]
entities: ["report:anssi-reactiv-situation-report-2026-09", "incident:metabase-sqli-zeroday-2026-08"]
techniques: [T1190, T1078, T1199]
affected_products: ["Metabase"]
cves: []
sources:
  - url: "https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf"
    publisher: "ANSSI / CERT-FR (CERTFR-2026-CTI-006)"
    date: "2026-09-30"
    role: primary
  - url: "https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-006/"
    publisher: "ANSSI / CERT-FR (report page)"
    date: "2026-09-30"
    role: primary
  - url: "https://next.ink/259353/securite-le-premier-point-de-situation-reactiv-de-lanssi-illustre-lampleur-du-probleme/"
    publisher: "Next"
    date: "2026-10-01"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This vulnerability, of the SQL injection type, gives an unauthenticated user access to the database of the Metabase application and administrator rights on the instance. (translated from French)"
    original: "Cette vulnérabilité, de type injection SQL, permet l’accès à la base de données de l’application Metabase pour un utilisateur non authentifié et l’obtention des droits administrateurs de l’instance"
    publisher: "Next (quoting the ANSSI report)"
    source_url: "https://next.ink/259353/securite-le-premier-point-de-situation-reactiv-de-lanssi-illustre-lampleur-du-probleme/"
  - quote: "This document is a situation report that reflects ongoing investigations and rapidly evolving incidents. (translated from French)"
    original: "Le présent document est un point de situation qui reflète des travaux d’investigation en cours et des incidents qui évoluent rapidement."
    publisher: "ANSSI / CERT-FR (report page)"
    source_url: "https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-006/"
verification: single-source-national-cert
sourcing_note: >
  The report is the French national authority's account of breaches at its own state services; the figures are
  provisional by the report's own statement, and individual claims by attackers inside it are labelled as claims. The
  Next article is a press reading of the same document.
confidence: high
references:
  - 2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally
  - 2026-08-15/france-dgfip-tax-authority-credential-intrusion
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

ANSSI published the first situation report of its REACTIV operation on 2026-09-30, set up after the Prime Minister asked on 2026-09-01 for a reinforced response capability for state services, including the power to have ministries take urgent measures within tight deadlines ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-006/)). Since 2026-08-01, 99 data breaches have been reported to ANSSI, 67 of them confirmed and 32 of those still being handled by the agency, and the report says its figures are provisional ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf)). It names the recurring causes: mass exploitation of the Metabase SQL injection CVE-2026-72898 since early August, with nine ministry instances compromised and a fix available since 2026-08-06; credentials stolen by infostealers on personal devices used for work, or taken from earlier breaches, that opened exposed services without a second factor; IDOR flaws, sometimes combined with other weaknesses, that allowed mass document exfiltration; missing or weak MFA, an email second factor counting as weak; compromise by rebound through a supplier that held ministry data; and, less often, missing authorization checks, SQL injection and exposed files ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf)). ANSSI asked all ministries to inventory their Metabase instances and verify they are updated ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf)).

The report's incident summaries show the shape of the losses: a compromised Tchap account of an Education nationale agent was used to read public and private rooms it already had access to and the conversations were exfiltrated; a claimed IDOR data leak on a Service national universel portal would expose 275,000 users and is still under investigation; and the compromise of the subcontractor of the operator of a TRACFIN reporting portal's support module led to exfiltration of the contact data of 136 reporting entities and the content of 213 support requests, after which the administration ended its relationship with that supplier ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf)).

**Exposure:** internet-facing public-sector services where staff or supplier accounts sign in with a password only or an email second factor, portals whose object identifiers are not checked against the caller's authorization, suppliers that hold your data, and any Metabase instance not upgraded since 2026-08-06 ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf)).

**Detection:** the report gives no detection guidance of its own; its causes map to authentication logs on exposed services for first-time or unfamiliar logins on accounts without strong MFA, web access logs for sequential identifier enumeration, and access by supplier accounts to your data stores.

**Defender takeaway:** test your own estate against the six causes, in particular which exposed services accept password-only or email-second-factor logins, which portals lack object-level authorization checks and which suppliers hold your data; the report shows breaches at national scale arising from these ordinary weaknesses and one patched flaw, not from new techniques.
