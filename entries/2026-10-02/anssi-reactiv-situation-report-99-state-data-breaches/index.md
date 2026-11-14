---
schema: 1
kind: research
title: 'ANSSI''s REACTIV situation reports on French state data breaches: 99 since 1 August in the first, driven by Metabase CVE-2026-72898, infostealer credentials without MFA, IDOR flaws and supplier rebound, and 64 more in the second, which names the reuse of stolen secrets as the one recurring technique'
headline: 'ANSSI''s second REACTIV report: 64 new breaches, reuse of stolen secrets the one technique; SMS 2FA and IDOR cases'
summary: 'ANSSI''s situation report of 2026-09-30 for its REACTIV operation counts 99 data breaches reported to it by French state services since 2026-08-01, 67 confirmed, and names the recurring causes: mass exploitation of the Metabase SQL injection CVE-2026-72898 (nine ministry instances compromised), infostealer-harvested credentials used on exposed services without a second factor, IDOR flaws, missing or weak MFA, and compromise through a supplier. The figures are provisional. ANSSI''s second report of 2026-11-12 counts 64 new breaches brought to its attention since then, five at ministries or supervised bodies, says all exploit the weaknesses already listed and names the reuse of stolen secrets as the technique.'
discovered_at: '2026-10-02T04:52:00Z'
updated_at: "2026-11-13T04:05:15Z"
event_date: '2026-09-30'
run_id: 2026-10-02T0404Z-intel
priority: notable
immediate_action: null
tags:
  - data-breach
  - identity
  - supply-chain
regions:
  - europe
sectors:
  - public-sector
entities:
  - report:anssi-reactiv-situation-report-2026-09
  - incident:metabase-sqli-zeroday-2026-08
techniques:
  - T1190
  - T1078
  - T1199
affected_products:
  - Metabase
cves: []
sources:
  - url: https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf
    publisher: ANSSI / CERT-FR (CERTFR-2026-CTI-006)
    date: '2026-09-30'
    role: primary
  - url: https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-006/
    publisher: ANSSI / CERT-FR (report page)
    date: '2026-09-30'
    role: primary
  - url: https://next.ink/259353/securite-le-premier-point-de-situation-reactiv-de-lanssi-illustre-lampleur-du-probleme/
    publisher: Next
    date: '2026-10-01'
    role: corroborating
  - url: https://www.cert.cyber.gouv.fr/uploads/CERTFR-2026-CTI-010.pdf
    publisher: ANSSI / CERT-FR (CERTFR-2026-CTI-010)
    date: '2026-11-12'
    role: primary
  - url: https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-010/
    publisher: ANSSI / CERT-FR (CERTFR-2026-CTI-010, report page)
    date: '2026-11-12'
    role: primary
closed_sources: []
evidence:
  - quote: This vulnerability, of the SQL injection type, gives an unauthenticated user access to the database of the Metabase application and administrator rights on the instance. (translated from French)
    original: Cette vulnérabilité, de type injection SQL, permet l’accès à la base de données de l’application Metabase pour un utilisateur non authentifié et l’obtention des droits administrateurs de l’instance
    publisher: Next (quoting the ANSSI report)
    source_url: https://next.ink/259353/securite-le-premier-point-de-situation-reactiv-de-lanssi-illustre-lampleur-du-probleme/
  - quote: This document is a situation report that reflects ongoing investigations and rapidly evolving incidents. (translated from French)
    original: Le présent document est un point de situation qui reflète des travaux d’investigation en cours et des incidents qui évoluent rapidement.
    publisher: ANSSI / CERT-FR (report page)
    source_url: https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-006/
verification: single-source-national-cert
sourcing_note: The report is the French national authority's account of breaches at its own state services; the figures are provisional by the report's own statement, and individual claims by attackers inside it are labelled as claims. The Next article is a press reading of the same document. The second report's PDF splits digits in its text layer, so its headline figures were checked against the rendered pages; its counts are events brought to ANSSI's attention, of which only five concern ministries or supervised bodies, and the two reports' totals are not added.
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
updates:
  - at: "2026-11-13T04:05:15Z"
    run_id: 2026-11-13T0256Z-intel
    type: update
    summary: >
      ANSSI's second REACTIV report of 2026-11-12 counts 64 further breaches, five at ministries, says all
      exploit the weaknesses already listed and names the reuse of stolen secrets as the technique, with
      new cases of an SMS second factor validated by the attacker and IDOR flaws combined with infostealer
      credentials.
    fields: [title, headline, summary, sources, sourcing_note, body]
migrated_from: null
---

ANSSI published the first situation report of its REACTIV operation on 2026-09-30, set up after the Prime Minister asked on 2026-09-01 for a reinforced response capability for state services, including the power to have ministries take urgent measures within tight deadlines ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/cti/CERTFR-2026-CTI-006/)). Since 2026-08-01, 99 data breaches have been reported to ANSSI, 67 of them confirmed and 32 of those still being handled by the agency, and the report says its figures are provisional ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf)). It names the recurring causes: mass exploitation of the Metabase SQL injection CVE-2026-72898 since early August, with nine ministry instances compromised and a fix available since 2026-08-06; credentials stolen by infostealers on personal devices used for work, or taken from earlier breaches, that opened exposed services without a second factor; IDOR flaws, sometimes combined with other weaknesses, that allowed mass document exfiltration; missing or weak MFA, an email second factor counting as weak; compromise by rebound through a supplier that held ministry data; and, less often, missing authorization checks, SQL injection and exposed files ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf)). ANSSI asked all ministries to inventory their Metabase instances and verify they are updated ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf)).

ANSSI's second report, published on 2026-11-12, counts 64 further breaches brought to its attention since 2026-09-30, five of them at ministries or bodies under their supervision, and says they all exploit the weaknesses already listed in September, naming the reuse of stolen secrets to reach ministry applications as the technique, with renewing compromised secrets as the first containment step ([ANSSI, 2026-11-12](https://www.cert.cyber.gouv.fr/uploads/CERTFR-2026-CTI-010.pdf)).

The report's incident summaries show the shape of the losses: a compromised Tchap account of an Education nationale agent was used to read public and private rooms it already had access to and the conversations were exfiltrated; a claimed IDOR data leak on a Service national universel portal would expose 275,000 users and is still under investigation; and the compromise of the subcontractor of the operator of a TRACFIN reporting portal's support module led to exfiltration of the contact data of 136 reporting entities and the content of 213 support requests, after which the administration ended its relationship with that supplier ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf)).

**Exposure:** internet-facing public-sector services where staff or supplier accounts sign in with a password only or an email second factor, portals whose object identifiers are not checked against the caller's authorization, suppliers that hold your data, and any Metabase instance not upgraded since 2026-08-06 ([ANSSI, 2026-09-30](https://www.cert.ssi.gouv.fr/uploads/CERTFR-2026-CTI-006.pdf)).

**Detection:** the report gives no detection guidance of its own; its causes map to authentication logs on exposed services for first-time or unfamiliar logins on accounts without strong MFA, web access logs for sequential identifier enumeration, and access by supplier accounts to your data stores.

**Defender takeaway:** test your own estate against the six causes, in particular which exposed services accept password-only or email-second-factor logins, which portals lack object-level authorization checks and which suppliers hold your data; the report shows breaches at national scale arising from these ordinary weaknesses and one patched flaw, not from new techniques.

## Update — 2026-11-13T04:05:15Z

ANSSI's second REACTIV situation report, published on 2026-11-12, counts 64 new data breaches brought to its attention since the first report of 2026-09-30, five of them at ministries or bodies under their supervision, with a significant fall in breaches detected or claimed at ministry level; it says all of them exploit weaknesses already named in September and gives the reuse of stolen secrets to reach ministry applications as the technique, which lets attackers extract the data legitimately (translated from French) ([ANSSI, 2026-11-12](https://www.cert.cyber.gouv.fr/uploads/CERTFR-2026-CTI-010.pdf)). The new cases it describes: stolen technical accounts reused against a foreign-ministry library portal after a server compromise; an IDOR flaw in the payment API of a public registration portal for the hunting-licence exam, exposing more than a thousand people; an agent's France Travail account compromised with the SMS second factor validated, with the data of more than 60,000 agents and professionals claimed on a forum; and partner-account credentials from infostealers without two-factor authentication, combined with an IDOR flaw on a URL exposing file identifiers, which let attackers extract close to 1.2 million files from the CAF's VACAF service in three days. Education nationale is now put at 25 of 30 académies, with lateral movement over the interministerial network ([ANSSI, 2026-11-12](https://www.cert.cyber.gouv.fr/uploads/CERTFR-2026-CTI-010.pdf)). ANSSI's recommendations are renewing compromised or suspect secrets first, systematic strong authentication, strict control of privileged accounts and tighter filtering to prevent exfiltration ([ANSSI, 2026-11-12](https://www.cert.cyber.gouv.fr/uploads/CERTFR-2026-CTI-010.pdf)).
