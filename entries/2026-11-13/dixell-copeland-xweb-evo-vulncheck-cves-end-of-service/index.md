---
schema: 1
kind: vulnerability
title: 'Dixell/Copeland XWEB EVO refrigeration supervisors: VulnCheck published 14 CVEs on 2026-11-12, seven scored CVSS 4.0 9.2 to 9.3 (unauthenticated command injection that runs as root, a hard-coded Administrator password, Administrator and root passwords computed from the MAC address and date); Copeland ended support on 2026-03-16 and ships no fixes; no exploitation reported'
headline: 'XWEB EVO refrigeration controllers: 14 CVEs, unauthenticated root RCE and a hard-coded password, no fix will ship'
summary: 'VulnCheck, as CNA, published 14 CVEs on 2026-11-12 for XWEB EVO, the end-of-service Copeland and Dixell web supervisor for refrigeration and cold-chain equipment, seven of them scored CVSS 4.0 9.2 to 9.3: unauthenticated command injection that runs as root, a hard-coded Administrator password, and Administrator and root passwords computed from the device MAC address and date. Copeland ended software support on 2026-03-16 and ships no security fixes, and on 2026-10-14 it told operators to remove all XWEB EVO units from the public internet; no source reports exploitation of these CVEs or ties them to the refrigeration attacks that French and Swiss authorities warn about.'
discovered_at: '2026-11-13T04:02:00Z'
updated_at: null
event_date: '2026-11-12'
run_id: 2026-11-13T0256Z-intel
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - ot-ics
  - pre-auth
  - rce
  - auth-bypass
  - no-patch
regions:
  - global
sectors: []
entities:
  - product:copeland-xweb
  - product:dixell-xweb
  - product:copeland-xweb-evo
techniques:
  - T1190
  - T1078.001
  - T1078
  - T1059.004
  - T1548.001
affected_products:
  - Copeland XWEB EVO
cves:
  - id: CVE-2026-124007
    cvss: 9.2 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
    affected: XWEB EVO before 5.6.2
    fixed: 'none distributed: Copeland ended software support for XWEB EVO on 2026-03-16 and the CNA record names no fixed build'
  - id: CVE-2026-124002
    cvss: 9.3 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
    affected: XWEB EVO 5.2.3 to before 5.7.0
    fixed: 'none distributed: Copeland ended software support for XWEB EVO on 2026-03-16 and the CNA record names no fixed build'
  - id: CVE-2026-124010
    cvss: 9.3 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
    affected: XWEB EVO before 5.6.2
    fixed: 'none distributed: Copeland ended software support for XWEB EVO on 2026-03-16 and the CNA record names no fixed build'
  - id: CVE-2026-124004
    cvss: 9.3 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
    affected: XWEB EVO before 5.6.2
    fixed: 'none distributed: Copeland ended software support for XWEB EVO on 2026-03-16 and the CNA record names no fixed build'
  - id: CVE-2026-124012
    cvss: 9.2 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
    affected: XWEB EVO 5.6.2 to 5.8.8
    fixed: 'none distributed: Copeland ended software support for XWEB EVO on 2026-03-16 and the CNA record names no fixed build'
  - id: CVE-2026-124005
    cvss: 9.2 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
    affected: XWEB EVO 4.3.0 to 5.8.8
    fixed: 'none distributed: Copeland ended software support for XWEB EVO on 2026-03-16 and the CNA record names no fixed build'
  - id: CVE-2026-124006
    cvss: 9.2 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - no-patch
    affected: XWEB EVO through 5.8.8
    fixed: 'none distributed: Copeland ended software support for XWEB EVO on 2026-03-16 and the CNA record names no fixed build'
sources:
  - url: https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-pre-auth-os-command-injection-via-password-field
    publisher: VulnCheck (CNA advisory CVE-2026-124007)
    date: '2026-11-12'
    role: primary
  - url: https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-pre-authentication-os-command-injection-via-username
    publisher: VulnCheck (CNA advisory CVE-2026-124002)
    date: '2026-11-12'
    role: primary
  - url: https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-unauthenticated-command-injection-via-xwconsole-cgi
    publisher: VulnCheck (CNA advisory CVE-2026-124010)
    date: '2026-11-12'
    role: primary
  - url: https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-hardcoded-administrator-backdoor-password
    publisher: VulnCheck (CNA advisory CVE-2026-124004)
    date: '2026-11-12'
    role: primary
  - url: https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-hardcoded-administrator-daily-password-authentication-bypass
    publisher: VulnCheck (CNA advisory CVE-2026-124012)
    date: '2026-11-12'
    role: primary
  - url: https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-predictable-administrator-password-generation
    publisher: VulnCheck (CNA advisory CVE-2026-124005)
    date: '2026-11-12'
    role: primary
  - url: https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-predictable-root-password-generation
    publisher: VulnCheck (CNA advisory CVE-2026-124006)
    date: '2026-11-12'
    role: primary
  - url: https://euvdservices.enisa.europa.eu/api/search?fromDate=2026-11-12&toDate=2026-11-13&vendor=Copeland&size=100
    publisher: ENISA EUVD (VulnCheck records for Copeland)
    date: '2026-11-12'
    role: corroborating
  - url: https://webapps.copeland.com/dixell/Content/Pages/AdvertisingMaterials/ProductNews/XWEB%20EVO%20EoS%20-%20Product_Bulletin_March_2026.pdf
    publisher: Copeland (XWEB EVO end-of-support bulletin)
    date: '2026-03-16'
    role: corroborating
  - url: https://webapps.copeland.com/Dixell/Pages/XWEB300D_500D_500_EVO
    publisher: Copeland (XWEB EVO download page)
    date: '2026-11-13'
    role: corroborating
  - url: https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf
    publisher: Dixell France (Copeland XWEB security recommendations)
    date: '2026-10-14'
    role: corroborating
  - url: https://security-hub.ncsc.admin.ch/#/posts/13054
    publisher: NCSC Switzerland (Cyber Security Hub post 13054)
    date: '2026-11-06'
    role: corroborating
  - url: https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de
    publisher: BACS (warning on refrigeration systems)
    date: '2026-11-10'
    role: corroborating
  - url: https://ransom-isac.org/blog/the-copeland-incident/
    publisher: Ransom-ISAC
    date: '2026-11-06'
    role: corroborating
  - url: https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/
    publisher: CERT-FR (alert CERTFR-2026-ALE-012)
    date: '2026-10-16'
    role: corroborating
closed_sources: []
evidence:
  - quote: End of software support for the XWEB EVO family
    publisher: Copeland (XWEB EVO end-of-support bulletin)
    source_url: https://webapps.copeland.com/dixell/Content/Pages/AdvertisingMaterials/ProductNews/XWEB%20EVO%20EoS%20-%20Product_Bulletin_March_2026.pdf
  - quote: in a single request to obtain a complete admin session and full control over the application.
    publisher: VulnCheck (CNA advisory CVE-2026-124004)
    source_url: https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-hardcoded-administrator-backdoor-password
verification: single-source
sourcing_note: VulnCheck assigned all 14 CVEs and wrote their descriptions and scores; ENISA's database repeats them and is not independent, and Copeland neither confirms nor disputes the cluster in anything read. The only fixed versions in the records are the 5.6.2 and 5.7.0 range limits and no source says where such a build is distributed, while Copeland's download pages list nothing above 5.2.3. The seven records scored below 9.0 are not carried here. XWEB EVO is a different product line from XWEB Pro.
confidence: medium
references:
  - 2026-10-13/danfoss-ak-sm-ak-sc-french-supermarket-refrigeration-attack
  - 2026-08-28/claroty-copeland-xweb-pro-refrigeration-unauth-root-rce
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

VulnCheck, the assigning CNA, describes unauthenticated command injection in XWEB EVO through the password field ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-pre-auth-os-command-injection-via-password-field)) and the username field ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-pre-authentication-os-command-injection-via-username)) of its login and API scripts, and through the sh parameter of the setuid xwconsole.cgi ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-unauthenticated-command-injection-via-xwconsole-cgi)), all reaching root; a hard-coded password for the built-in Administrator account that gives a full session in one request ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-hardcoded-administrator-backdoor-password)); and Administrator and root passwords that can be computed offline from the device MAC address and the date ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-hardcoded-administrator-daily-password-authentication-bypass); [VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-predictable-administrator-password-generation); [VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-predictable-root-password-generation)). The cluster holds 14 records, and the seven scored 9.2 or higher are the ones covered here ([ENISA EUVD, 2026-11-12](https://euvdservices.enisa.europa.eu/api/search?fromDate=2026-11-12&toDate=2026-11-13&vendor=Copeland&size=100)). The records' ranges end before 5.6.2 or 5.7.0 or run through 5.8.8, but Copeland's download pages list EVO packages only up to 5.2.3 of 2018 ([Copeland, 2026-11-13](https://webapps.copeland.com/Dixell/Pages/XWEB300D_500D_500_EVO)), and its bulletin says software support ended on 2026-03-16 with no further firmware or security updates ([Copeland, 2026-03-16](https://webapps.copeland.com/dixell/Content/Pages/AdvertisingMaterials/ProductNews/XWEB%20EVO%20EoS%20-%20Product_Bulletin_March_2026.pdf)), so no source shows where a fixed build can be had.

No source reports exploitation or a public proof of concept for these CVEs, and none ties them to the compromises of Danfoss, Copeland and Dixell controllers. Copeland's bulletin of 2026-10-14, carried in the Dixell France guide that CERT-FR links, acknowledges a vulnerability on an end-of-life generation of XWEB EVO controllers and tells operators to remove all XWEB EVO units from the public internet immediately (translated from French) ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)); NCSC Switzerland says that guidance addresses end-of-service XWEB EVO systems and that the public information does not confirm exploitation of the Danfoss CVEs it lists ([NCSC Switzerland, 2026-11-06](https://security-hub.ncsc.admin.ch/#/posts/13054)), and BACS lists Copeland and Dixell XWEB as potentially affected ([BACS, 2026-11-10](https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de)). The one compromised-unit log read concerns an XWEB Pro, not an EVO ([Ransom-ISAC, 2026-11-06](https://ransom-isac.org/blog/the-copeland-incident/)).

**Exposure:** an XWEB EVO unit, sold until October 2023 ([Copeland, 2026-03-16](https://webapps.copeland.com/dixell/Content/Pages/AdvertisingMaterials/ProductNews/XWEB%20EVO%20EoS%20-%20Product_Bulletin_March_2026.pdf)), whose login page appears when the site's public address is opened from outside the site network, which is the vendor's own test ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)).

**Detection:** no source gives log artefacts for these flaws. After suspected access the vendor's procedure is to review the user list and profiles and the alarm categories, levels and recipients with a test alarm, and to read product temperatures directly in the cabinets because setpoints or alarm thresholds may have changed; CERT-FR says a factory reset removes persistence but leaves an end-of-life unit vulnerable ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf); [CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

**Defender takeaway:** no fix is coming, so keep XWEB EVO units off the internet and reach them only through a VPN, and plan the move to the supported XWEB Pro ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)).
