---
schema: 1
kind: threat
title: "BigBlueButton bbb-web before 3.0.21 and 3.0.23: predictable session tokens, an API checksum bypass and an SSRF (CVE-2026-46351, CVE-2026-46353, CVE-2026-46404)"
headline: "BigBlueButton fixes predictable session tokens, an API checksum bypass and an SSRF in bbb-web (3.0.21, 3.0.23)"
summary: "BigBlueButton published three advisories for bbb-web on 2026-05-13: before 3.0.21 a session user could predict other users' conference session tokens and impersonate them (CVE-2026-46351, CVSS 8.1), and a presentationUploadExternalUrl parameter let any user send valid requests to some API endpoints without a checksum (CVE-2026-46353, 8.1); before 3.0.23 presentation URL validation did not keep requests away from site-local and link-local addresses (CVE-2026-46404, 6.8, high privileges). Germany's BSI summarizes the set as letting a remote, authenticated attacker bypass security measures and disclose confidential information; no source reports exploitation."
discovered_at: "2026-05-19T05:00:01Z"
event_date: 2026-05-13
run_id: 2026-05-19-2505c918
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - auth-bypass
  - info-disclosure
  - patch-available
regions:
  - global
  - dach
sectors:
  - education
entities:
  - "trend:bigbluebutton-bbb-web-three-cves-46351-46353-46404-eu-edu"
techniques: [T1190, T1212]
affected_products: ["BigBlueButton"]
cves:
  - id: CVE-2026-46351
    cvss: "8.1 (CVSS 3.1, GitHub as CNA via ENISA EUVD)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: "bbb-web before 3.0.21"
    fixed: "3.0.21"
  - id: CVE-2026-46353
    cvss: "8.1 (CVSS 3.1, GitHub as CNA via ENISA EUVD)"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: "bbb-web before 3.0.21"
    fixed: "3.0.21"
  - id: CVE-2026-46404
    cvss: "6.8 (CVSS 3.1, GitHub as CNA via ENISA EUVD)"
    epss: null
    type: ssrf
    vector: zero-click
    auth: post-auth
    status:
      - patch-available
    affected: "BigBlueButton before 3.0.23"
    fixed: "3.0.23"
sources:
  - url: "https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h"
    publisher: "BigBlueButton (GHSA-7959-pf2v-xc4h)"
    date: "2026-05-13"
    role: primary
  - url: "https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-43hc-5g2m-cqff"
    publisher: "BigBlueButton (GHSA-43hc-5g2m-cqff)"
    date: "2026-05-13"
    role: primary
  - url: "https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h"
    publisher: "BigBlueButton (GHSA-xqm3-6q7q-4v5h)"
    date: "2026-05-13"
    role: primary
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1568"
    publisher: "BSI (WID-SEC-2026-1568)"
    date: "2026-05-18"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44996"
    publisher: "ENISA EUVD (EUVD-2026-44996)"
    date: "2026-07-16"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44998"
    publisher: "ENISA EUVD (EUVD-2026-44998)"
    date: "2026-07-16"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44997"
    publisher: "ENISA EUVD (EUVD-2026-44997)"
    date: "2026-07-16"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Without the fix it is possible for a user to determine the sesionTokens of other users in the session."
    publisher: BigBlueButton
    source_url: "https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h"
  - quote: "Without this fix it is possible for any user to send valid requests to some endpoints without a checksum."
    publisher: BigBlueButton
    source_url: "https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-43hc-5g2m-cqff"
  - quote: "Private addresses assets may be compromised if the attacker has gained additional access."
    publisher: BigBlueButton
    source_url: "https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h"
  - quote: "A remote, authenticated attacker can exploit several vulnerabilities in BigBlueButton to bypass security measures and disclose confidential information."
    original: "Ein entfernter, authentisierter Angreifer kann mehrere Schwachstellen in BigBlueButton ausnutzen, um Sicherheitsvorkehrungen zu umgehen und vertrauliche Informationen offenzulegen."
    publisher: BSI
    source_url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1568"
verification: multi-source
sourcing_note: >
  BigBlueButton's own advisories describe each flaw and its fix, ENISA's EUVD carries the CVE records GitHub later issued for them with their scores,
  and BSI restates the set for Germany; no source reports exploitation or says where BigBlueButton is deployed.
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
migrated_from: briefs/2026-05-19.md
updates:
  - at: "2026-10-21T20:35:59Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      BigBlueButton published its three bbb-web advisories on 2026-05-13, and BSI's advisory followed on
      2026-05-18; no source names DFN, SWITCH, GÉANT, Swiss cantonal schools or German education
      ministries as BigBlueButton operators. The checksum bypass lets any user send valid requests to some
      endpoints without a checksum, and the SSRF, which needs a high-privilege user, exposes
      private-address assets only if the attacker has gained additional access.
    fields: [actions, affected_products, body, classification, cves, event_date, evidence, headline, priority, regions, sectors, sources, sourcing_note, summary, techniques, title]
---

BigBlueButton, an open-source virtual classroom, published three security advisories for its bbb-web component on 2026-05-13 ([ENISA EUVD-2026-44996](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44996); [BigBlueButton GHSA-7959-pf2v-xc4h, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h); [BigBlueButton GHSA-43hc-5g2m-cqff, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-43hc-5g2m-cqff); [BigBlueButton GHSA-xqm3-6q7q-4v5h, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h)). Before version 3.0.21, bbb-web generated conference session tokens with insufficiently secure randomness, so a user could determine the session tokens of other users in the same session and impersonate them (CVE-2026-46351) ([BigBlueButton GHSA-7959-pf2v-xc4h, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h); [ENISA EUVD-2026-44996](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44996)), and supplying a presentationUploadExternalUrl parameter bypassed checksum validation, so any user could send valid requests to some endpoints without a checksum (CVE-2026-46353) ([BigBlueButton GHSA-43hc-5g2m-cqff, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-43hc-5g2m-cqff); [ENISA EUVD-2026-44998](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44998)). Before 3.0.23, presentation URL validation did not restrict access to site-local and link-local addresses, and the fix also pins resolved IPs when following redirects; BigBlueButton says private-address assets may be compromised if the attacker has gained additional access (CVE-2026-46404) ([BigBlueButton GHSA-xqm3-6q7q-4v5h, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h); [ENISA EUVD-2026-44997](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44997)). The CVSS 3.1 scores in the CVE records are 8.1 for the first two, with low privileges and no user interaction, and 6.8 for the SSRF, with high privileges and a changed scope ([ENISA EUVD-2026-44996](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44996); [ENISA EUVD-2026-44998](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44998); [ENISA EUVD-2026-44997](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44997)). Germany's BSI summarized the set as letting a remote, authenticated attacker bypass security measures and disclose confidential information (translated from German) ([BSI WID-SEC-2026-1568, 2026-05-18](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1568)). No source reports exploitation.

**Exposure:** BigBlueButton servers running bbb-web older than 3.0.21, or older than 3.0.23 for the SSRF; the token flaw needs a user inside the meeting, the checksum bypass any user of the API, and the SSRF a high-privilege user ([ENISA EUVD-2026-44996](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44996); [ENISA EUVD-2026-44998](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44998); [ENISA EUVD-2026-44997](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44997)).

**Detection:** in bbb-web API logs, requests carrying a presentationUploadExternalUrl parameter that reach endpoints without a valid checksum, and joins in which one participant presents another participant's session token; in egress telemetry from the BigBlueButton server, presentation fetches to site-local or link-local addresses ([BigBlueButton GHSA-43hc-5g2m-cqff, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-43hc-5g2m-cqff); [BigBlueButton GHSA-7959-pf2v-xc4h, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h); [BigBlueButton GHSA-xqm3-6q7q-4v5h, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h)).

**Defender takeaway:** upgrade BigBlueButton to 3.0.23 or later, which covers all three flaws; the advisories offer no workaround besides updating ([BigBlueButton GHSA-xqm3-6q7q-4v5h, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h); [BigBlueButton GHSA-7959-pf2v-xc4h, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h)). Organizations without BigBlueButton have no decision to make.

## Correction — 2026-10-21T20:35:59Z

BigBlueButton published the three advisories on 2026-05-13, not 2026-05-17, and BSI's advisory followed on 2026-05-18 ([BigBlueButton GHSA-7959-pf2v-xc4h, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-7959-pf2v-xc4h); [BSI WID-SEC-2026-1568, 2026-05-18](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1568)). No source names the research networks, Swiss cantonal schools or German education ministries said to run BigBlueButton; BSI describes it only as an open-source web-conferencing system ([BSI WID-SEC-2026-1568, 2026-05-18](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1568)). The checksum bypass lets any user send valid requests to some endpoints without a checksum, rather than arbitrary authenticated API calls ([BigBlueButton GHSA-43hc-5g2m-cqff, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-43hc-5g2m-cqff)), and for the SSRF, which needs a high-privilege user, BigBlueButton says only that private-address assets may be compromised if the attacker has gained additional access ([BigBlueButton GHSA-xqm3-6q7q-4v5h, 2026-05-13](https://github.com/bigbluebutton/bigbluebutton/security/advisories/GHSA-xqm3-6q7q-4v5h); [ENISA EUVD-2026-44997](https://euvd.enisa.europa.eu/enisa/eu_vulnerability_database/EUVD-2026-44997)).
