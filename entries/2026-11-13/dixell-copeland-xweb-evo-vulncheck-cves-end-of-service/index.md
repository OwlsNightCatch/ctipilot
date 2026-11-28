---
schema: 1
kind: vulnerability
title: 'Dixell/Copeland XWEB EVO refrigeration supervisors: VulnCheck published 14 CVEs on 2026-11-12, seven scored CVSS 4.0 9.2 to 9.3 (unauthenticated command injection that runs as root, a hard-coded Administrator password, Administrator and root passwords computed from the MAC address and date); VulnCheck sees two of the 14 exploited, the injection flaws are fixed on the current branch and the password flaws will stay unfixed after Copeland ended support on 2026-03-16'
headline: 'XWEB EVO refrigeration controllers: two of 14 flaws exploited, unauthenticated root RCE; password flaws stay unfixed'
summary: 'VulnCheck, as CNA, published 14 CVEs on 2026-11-12 for XWEB EVO, the end-of-service Copeland and Dixell web supervisor for refrigeration and cold-chain equipment, seven of them scored CVSS 4.0 9.2 to 9.3: unauthenticated command injection that runs as root, a hard-coded Administrator password, and Administrator and root passwords computed from the device MAC address and date. VulnCheck''s sensors recorded exploitation of an unauthenticated configuration write (CVE-2026-124014) from 2026-11-12 and root-command probes against CVE-2026-124010 from 2026-11-13, by opportunistic scanners it does not tie to the October refrigeration attacks. The injection flaws are fixed on the current firmware branch, while the password flaws reach the last firmware, 5.8.8, and stay unfixed because Copeland ended software support on 2026-03-16; Copeland tells operators to remove all XWEB EVO units from the public internet.'
discovered_at: '2026-11-13T04:02:00Z'
updated_at: "2026-11-15T14:53:24Z"
event_date: '2026-11-12'
run_id: 2026-11-13T0256Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - ot-ics
  - pre-auth
  - rce
  - auth-bypass
  - actively-exploited
  - patch-available
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
      - patch-available
    affected: XWEB EVO before 5.6.2
    fixed: '5.6.2 or later: VulnCheck says this pre-2021 class is fixed on the current branch (last firmware 5.8.8, end of support), which Copeland distributes through its System Software Update page'
  - id: CVE-2026-124002
    cvss: 9.3 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: XWEB EVO 5.2.3 to before 5.7.0
    fixed: '5.7.0 or later: VulnCheck says this pre-2021 class is fixed on the current branch (last firmware 5.8.8, end of support), which Copeland distributes through its System Software Update page'
  - id: CVE-2026-124010
    cvss: 9.3 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - patch-available
    affected: XWEB EVO before 5.6.2
    fixed: '5.6.2 or later: VulnCheck says this pre-2021 class is fixed on the current branch (last firmware 5.8.8, end of support), which Copeland distributes through its System Software Update page'
  - id: CVE-2026-124004
    cvss: 9.3 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - patch-available
    affected: XWEB EVO before 5.6.2
    fixed: '5.6.2 or later: VulnCheck says this pre-2021 class is fixed on the current branch (last firmware 5.8.8, end of support), which Copeland distributes through its System Software Update page'
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
  - id: CVE-2026-124014
    cvss: 8.8 (CVSS 4.0, VulnCheck CNA)
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - no-patch
    affected: XWEB EVO 4.3.0 through 5.8.8
    fixed: 'none distributed: the CNA record''s range runs through the last firmware, 5.8.8, and Copeland ended software support on 2026-03-16'
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
  - url: https://www.vulncheck.com/blog/copeland-xweb-evo-unauthenticated-root
    publisher: VulnCheck (XWEB EVO disclosure and canary observations)
    date: '2026-11-13'
    role: corroborating
  - url: https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-unauthenticated-configuration-write-via-config-lua
    publisher: VulnCheck (CNA advisory CVE-2026-124014)
    date: '2026-11-12'
    role: corroborating
closed_sources: []
evidence:
  - quote: End of software support for the XWEB EVO family
    publisher: Copeland (XWEB EVO end-of-support bulletin)
    source_url: https://webapps.copeland.com/dixell/Content/Pages/AdvertisingMaterials/ProductNews/XWEB%20EVO%20EoS%20-%20Product_Bulletin_March_2026.pdf
  - quote: in a single request to obtain a complete admin session and full control over the application.
    publisher: VulnCheck (CNA advisory CVE-2026-124004)
    source_url: https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-hardcoded-administrator-backdoor-password
  - quote: Two of them are under active exploitation.
    publisher: VulnCheck (XWEB EVO disclosure and canary observations)
    source_url: https://www.vulncheck.com/blog/copeland-xweb-evo-unauthenticated-root
  - quote: this whole class was removed in the 2021 rewrite, so it is fixed on the current branch but lives on across the legacy fleet that is still most of what is exposed
    publisher: VulnCheck (XWEB EVO disclosure and canary observations)
    source_url: https://www.vulncheck.com/blog/copeland-xweb-evo-unauthenticated-root
verification: single-source
sourcing_note: VulnCheck assigned all 14 CVEs and wrote their descriptions and scores; ENISA's database repeats them and is not independent, and Copeland neither confirms nor disputes the cluster in anything read. The exploitation statements are VulnCheck's own canary observations, which no second party has reported. VulnCheck's blog says the pre-2021 injection and backdoor class is fixed on the current branch, while the CNA record for the exploited configuration write CVE-2026-124014 runs through 5.8.8; the record's range is carried. Copeland's public download pages list nothing above 5.2.3, and its guide points to the System Software Update page for the latest build. Of the seven records scored below 9.0, only the exploited CVE-2026-124014 is carried. XWEB EVO is a different product line from XWEB Pro.
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
actions:
  - Find every Dixell or Copeland XWEB EVO supervisor reachable from the internet and put it behind a VPN now; on each unit that was exposed, review its users, alarm settings and setpoints and read cabinet temperatures directly, because VulnCheck sees two of its unauthenticated flaws exploited and the password flaws will never be fixed.
updates:
  - at: "2026-11-15T14:53:24Z"
    run_id: 2026-11-15T1407Z-audit
    type: update
    summary: >
      VulnCheck reports two XWEB EVO flaws exploited by opportunistic scanners: the unauthenticated
      configuration write CVE-2026-124014 (CVSS 4.0 8.8) from 2026-11-12 and root-command probes against
      CVE-2026-124010 from 2026-11-13. It says the injection and backdoor flaws are fixed on the current
      firmware branch, so the unfixed exposure is the pre-2021 fleet plus the predictable-password flaws; its
      blog and its CNA record disagree on whether CVE-2026-124014 reaches 5.8.8.
    fields: [title, headline, summary, priority, tags, cves, sources, evidence, sourcing_note, actions, body]
migrated_from: null
---

VulnCheck, the assigning CNA, describes unauthenticated command injection in XWEB EVO through the password field ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-pre-auth-os-command-injection-via-password-field)) and the username field ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-pre-authentication-os-command-injection-via-username)) of its login and API scripts, and through the sh parameter of the setuid xwconsole.cgi ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-unauthenticated-command-injection-via-xwconsole-cgi)), all reaching root; a hard-coded password for the built-in Administrator account that gives a full session in one request ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-hardcoded-administrator-backdoor-password)); and Administrator and root passwords that can be computed offline from the device MAC address and the date ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-hardcoded-administrator-daily-password-authentication-bypass); [VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-predictable-administrator-password-generation); [VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-predictable-root-password-generation)). The cluster holds 14 records, and the seven scored 9.2 or higher are the ones covered here ([ENISA EUVD, 2026-11-12](https://euvdservices.enisa.europa.eu/api/search?fromDate=2026-11-12&toDate=2026-11-13&vendor=Copeland&size=100)). VulnCheck says the injection and backdoor-password flaws belong to the pre-2021 builds and are fixed on the current branch, while the predictable-password flaws reach the last firmware, 5.8.8 ([VulnCheck, 2026-11-13](https://www.vulncheck.com/blog/copeland-xweb-evo-unauthenticated-root)). Copeland's bulletin says software support ended on 2026-03-16 with no further firmware or security updates ([Copeland, 2026-03-16](https://webapps.copeland.com/dixell/Content/Pages/AdvertisingMaterials/ProductNews/XWEB%20EVO%20EoS%20-%20Product_Bulletin_March_2026.pdf)), so those will stay unfixed; its public download pages list EVO packages only up to 5.2.3 of 2018 ([Copeland, 2026-11-13](https://webapps.copeland.com/Dixell/Pages/XWEB300D_500D_500_EVO)).

VulnCheck's canary sensors recorded in-the-wild exploitation of the unauthenticated configuration-file write CVE-2026-124014 (CVSS 4.0 8.8, XWEB EVO 4.3.0 through 5.8.8) from 2026-11-12 22:00 UTC and four root-command probes against CVE-2026-124010 from 2026-11-13 03:41 UTC, from two opportunistic scanners it does not tie to the October refrigeration campaign ([VulnCheck, 2026-11-13](https://www.vulncheck.com/blog/copeland-xweb-evo-unauthenticated-root); [VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-unauthenticated-configuration-write-via-config-lua)). Copeland's bulletin of 2026-10-14, carried in the Dixell France guide that CERT-FR links, acknowledges a vulnerability on an end-of-life generation of XWEB EVO controllers and tells operators to remove all XWEB EVO units from the public internet immediately (translated from French) ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)); NCSC Switzerland says that guidance addresses end-of-service XWEB EVO systems and that the public information does not confirm exploitation of the Danfoss CVEs it lists ([NCSC Switzerland, 2026-11-06](https://security-hub.ncsc.admin.ch/#/posts/13054)), and BACS lists Copeland and Dixell XWEB as potentially affected ([BACS, 2026-11-10](https://www.bacs.admin.ch/de/warnung-kuehlanlagen-de)). The one compromised-unit log read concerns an XWEB Pro, not an EVO ([Ransom-ISAC, 2026-11-06](https://ransom-isac.org/blog/the-copeland-incident/)).

**Exposure:** an XWEB EVO unit, sold until October 2023 ([Copeland, 2026-03-16](https://webapps.copeland.com/dixell/Content/Pages/AdvertisingMaterials/ProductNews/XWEB%20EVO%20EoS%20-%20Product_Bulletin_March_2026.pdf)), whose login page appears when the site's public address is opened from outside the site network, which is the vendor's own test ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)).

**Detection:** in web or proxy access logs in front of the supervisor, an unauthenticated POST to config.lua or an unauthenticated GET to /cgi-bin/xwconsole.cgi with an sh parameter is VulnCheck's request-level signal ([VulnCheck, 2026-11-13](https://www.vulncheck.com/blog/copeland-xweb-evo-unauthenticated-root)). After suspected access the vendor's procedure is to review the user list and profiles and the alarm categories, levels and recipients with a test alarm, and to read product temperatures directly in the cabinets because setpoints or alarm thresholds may have changed; CERT-FR says a factory reset removes persistence but leaves an end-of-life unit vulnerable ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf); [CERT-FR, 2026-10-16](https://www.cert.ssi.gouv.fr/alerte/CERTFR-2026-ALE-012/)).

**Defender takeaway:** VulnCheck sees two flaws exploited ([VulnCheck, 2026-11-13](https://www.vulncheck.com/blog/copeland-xweb-evo-unauthenticated-root)) and the password flaws will never be fixed, so keep XWEB EVO units off the internet and reach them only through a VPN, install the latest build from Copeland's update page on any pre-2021 unit, and plan the move to the supported XWEB Pro ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)).

## Update — 2026-11-15T14:53:24Z

VulnCheck's canary sensors recorded in-the-wild exploitation of CVE-2026-124014, an unauthenticated write of the system configuration file through config.lua that affects XWEB EVO 4.3.0 through 5.8.8 (CVSS 4.0 8.8), from 2026-11-12 22:00 UTC, and four probes running a root command through CVE-2026-124010 from 2026-11-13 03:41 UTC; it added both to its own exploited-vulnerabilities list and reads both sources as opportunistic scanners, not the October refrigeration campaign ([VulnCheck, 2026-11-13](https://www.vulncheck.com/blog/copeland-xweb-evo-unauthenticated-root); [VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-unauthenticated-configuration-write-via-config-lua)). The same disclosure says the injection and backdoor-password class was removed in the 2021 rewrite and is fixed on the current branch, so the unfixed exposure is the pre-2021 fleet plus the predictable-password flaws, which reach the last firmware ([VulnCheck, 2026-11-13](https://www.vulncheck.com/blog/copeland-xweb-evo-unauthenticated-root)). For CVE-2026-124014 the two VulnCheck sources differ: the blog lists it with the pre-2021 class, while the CNA record gives XWEB EVO 4.3.0 through 5.8.8 as affected ([VulnCheck, 2026-11-12](https://www.vulncheck.com/advisories/dixell-copeland-xweb-evo-unauthenticated-configuration-write-via-config-lua)). Copeland's guide tells operators to install the latest build for their model from its System Software Update page while they migrate (translated from French) ([Dixell France, 2026-10-14](https://dixell.fr/wp-content/uploads/2026/10/Recommandations-pour-une-utilisation-securisee-des-superviseurs-XWEB-v1.0.pdf)).
