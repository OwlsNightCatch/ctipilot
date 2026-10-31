---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, PHP2Shell in industrial, building and network-access products: Belden NetModule NRSW has no fix and macmon 6.x must move to 7.x, with notices from Schneider Electric, B&R, HMS Networks, Wibu-Systems, Johnson Controls and Oracle"
headline: "PHP2Shell hits NetModule routers with no fix, macmon, Schneider, B&R, HMS, Wibu and Oracle products"
summary: >
  Industrial, building and network-access vendors have published their own notices for the PHP flaws CVE-2026-109618 and CVE-2026-109619,
  which CISA added to its Known Exploited Vulnerabilities catalog on 2026-10-26. Belden says all versions of NetModule NRSW, the router software of the
  Bern-headquartered NetModule AG, are affected with no patched release and advises disabling the web interface; macmon 6.x and 7.x, Schneider Electric
  Security Expert and Control Engineering, B&R APROL, HMS Netbiter, Wibu-Systems CodeMeter License Central and Oracle Secure Backup and
  Solaris 11 carry fixes or remediations at varying stages.
discovered_at: "2026-10-27T03:56:00Z"
updated_at: null
event_date: "2026-10-22"
run_id: 2026-10-27T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, rce, pre-auth, cisa-kev, patch-available, no-patch, ot-ics]
regions: [global, switzerland]
sectors: [transport, manufacturing]
entities: ["tool:php2shell", "product:php", "product:belden-netmodule-nrsw", "product:belden-macmon-nac", "product:schneider-electric-ecostruxure-security-expert", "product:schneider-electric-ecostruxure-control-engineering", "product:proleit-lineoptimize", "product:b-r-aprol", "product:hms-networks-netbiter", "product:wibu-systems-codemeter-license-central", "product:johnson-controls-illustra", "product:johnson-controls-visonic-powermanage", "product:oracle-secure-backup", "product:oracle-solaris"]
techniques: [T1190]
affected_products: ["Belden NetModule NRSW", "Belden macmon NAC", "Schneider Electric EcoStruxure Security Expert", "Schneider Electric EcoStruxure Control Engineering", "ProLeiT LINEoptimize", "B&R APROL", "HMS Networks Netbiter", "Wibu-Systems CodeMeter License Central", "Johnson Controls Illustra", "Johnson Controls Visonic PowerManage", "Oracle Secure Backup", "Oracle Solaris"]
cves:
  - id: CVE-2026-109618
    cvss: "9.8 (CVSS 3.1, as stated by Belden and Oracle)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, no-patch, patch-available, mitigation-only]
    affected: "Belden NetModule NRSW all versions including 5.0.0.104; macmon 6.x and 7.x; Schneider Electric EcoStruxure Security Expert before 1.48.4.0, LINEoptimize and EcoStruxure Control Engineering all versions; B&R APROL up to R 4.4-65; HMS Netbiter firmware up to 3.00.10; Wibu-Systems CodeMeter License Central web interface and extensions; Oracle Secure Backup 19.1.0.0.0 to 19.1.0.1.0 and Oracle Solaris 11"
    fixed: "NRSW: no patched release, web interface to be disabled; macmon 7.x: patch from the service portal, 6.x: upgrade to 7.x; Security Expert 1.48.4.0; LINEoptimize and Control Engineering: remediation through ProLeiT support and Schneider Electric; APROL: patches planned 2026-10-26 and 2026-10-29; Netbiter 3.00.11; CodeMeter License Central 5.2.2 or the patch installer for 5.1.2 and 5.0.x; Oracle patches per its Security Alert Rev 2"
  - id: CVE-2026-109619
    cvss: "9.8 (CVSS 3.1, as stated by Belden)"
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, no-patch, patch-available, mitigation-only]
    affected: "Belden NetModule NRSW all versions including 5.0.0.104; macmon 6.x and 7.x; Schneider Electric EcoStruxure Security Expert before 1.48.4.0, LINEoptimize and EcoStruxure Control Engineering all versions; B&R APROL up to R 4.4-65; HMS Netbiter firmware up to 3.00.10; Wibu-Systems CodeMeter License Central web interface and extensions; Oracle Secure Backup 19.1.0.0.0 to 19.1.0.1.0 and Oracle Solaris 11"
    fixed: "NRSW: no patched release, web interface to be disabled; macmon 7.x: patch from the service portal, 6.x: upgrade to 7.x; Security Expert 1.48.4.0; LINEoptimize and Control Engineering: remediation through ProLeiT support and Schneider Electric; APROL: patches planned 2026-10-26 and 2026-10-29; Netbiter 3.00.11; CodeMeter License Central 5.2.2 or the patch installer for 5.1.2 and 5.0.x; the Oracle patch for CVE-2026-109618 also addresses CVE-2026-109619"
sources:
  - url: "https://assets.belden.com/asset/0e20ea6c-c1f5-4269-b765-e160a2bf4965/PSIRT-10-Critical-PHP-Vulnerabilities-in-macmon-and-NRSW.pdf"
    publisher: "Belden (security advisory PSIRT-10)"
    date: "2026-10-22"
    role: primary
  - url: "https://download.se.com/files?p_Doc_Ref=SESB-2026-295-01&p_enDocType=Security+and+Safety+Notice&p_File_Name=SESB-2026-295-01.pdf"
    publisher: "Schneider Electric (security bulletin SESB-2026-295-01, version 2.0.0)"
    date: "2026-10-26"
    role: primary
  - url: "https://br-cws-assets.de-fra-1.linodeobjects.com/SA26P015-7cd6ca9c.pdf"
    publisher: "B&R (cyber security advisory SA26P015)"
    date: "2026-10-23"
    role: primary
  - url: "https://hmsnetworks.blob.core.windows.net/nlw/docs/default-source/products/cybersecurity/security-advisory/hms-security-advisory-2026-10-22-002---netbiter-and-argos-php-vulnerabilities.pdf"
    publisher: "HMS Networks (security advisory HMSSAR-2026-10-22-002)"
    date: "2026-10-23"
    role: primary
  - url: "https://www.wibu.com/support/product-alerts.html#c61269"
    publisher: "Wibu-Systems (product alert, CodeMeter License Central PHP vulnerabilities)"
    date: "2026-10-23"
    role: primary
  - url: "https://www.oracle.com/security-alerts/alert-cve-2026-109618.html"
    publisher: "Oracle (Security Alert Advisory, Rev 2)"
    date: "2026-10-26"
    role: primary
  - url: "https://www.securityweek.com/industrial-vendors-check-products-for-php2shell-vulnerabilities/"
    publisher: "SecurityWeek"
    date: "2026-10-26"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.26)"
    date: "2026-10-26"
    role: corroborating
  - url: "https://www.belden.com/news/belden-acquires-netmodule-ag"
    publisher: "Belden (acquisition of NetModule AG)"
    date: "2022-03-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "including the latest mainline release 5.0.0.104."
    publisher: "Belden (security advisory PSIRT-10)"
    source_url: "https://assets.belden.com/asset/0e20ea6c-c1f5-4269-b765-e160a2bf4965/PSIRT-10-Critical-PHP-Vulnerabilities-in-macmon-and-NRSW.pdf"
  - quote: "said all versions of its NetModule NRSW are affected, including the latest mainline release, and a patched version has yet to be released."
    publisher: "SecurityWeek (relaying Belden PSIRT-10)"
    source_url: "https://www.securityweek.com/industrial-vendors-check-products-for-php2shell-vulnerabilities/"
  - quote: "Customers can obtain the patched Security Expert version 1.48.4.0 from Schneider’s Customer Care Center"
    publisher: "SecurityWeek (relaying SESB-2026-295-01)"
    source_url: "https://www.securityweek.com/industrial-vendors-check-products-for-php2shell-vulnerabilities/"
  - quote: "said its APROL process control system is affected in versions up to R 4.4-65. Patches were expected on October 26 and October 29."
    publisher: "SecurityWeek (relaying B&R SA26P015)"
    source_url: "https://www.securityweek.com/industrial-vendors-check-products-for-php2shell-vulnerabilities/"
  - quote: "Remote code execution without authentication is possible."
    publisher: "HMS Networks (security advisory HMSSAR-2026-10-22-002)"
    source_url: "https://hmsnetworks.blob.core.windows.net/nlw/docs/default-source/products/cybersecurity/security-advisory/hms-security-advisory-2026-10-22-002---netbiter-and-argos-php-vulnerabilities.pdf"
  - quote: "Rev 2. Added Oracle Secure Backup"
    publisher: "Oracle (Security Alert Advisory, Rev 2)"
    source_url: "https://www.oracle.com/security-alerts/alert-cve-2026-109618.html"
verification: multi-source
sourcing_note: >
  Each vendor's own notice is the first-party source for its products; the flaws themselves are in the PHP runtime and are covered by the
  related PHP, PAN-OS, NetScaler and QNAP entries. The Johnson Controls patches are read through SecurityWeek's summary of the vendor's
  notice. No vendor reports exploitation of its own product; the CISA listing is of the PHP flaws themselves.
confidence: high
references:
  - "2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619"
  - "2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release"
  - "2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27"
  - "2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Disable the web interface of every Belden NetModule NRSW router now, after confirming SSH access to it, with the CLI settings http.status=0 and https.status=0, because no patched NRSW release exists; patch macmon 7.x from the service portal and move macmon 6.x to 7.x, and keep the web interfaces of both off networks that are not trusted."
updates: []
migrated_from: null
---

Industrial, building and network-access vendors have published their own notices for the PHP runtime flaws CVE-2026-109618 and CVE-2026-109619, which CISA lists as exploited since 2026-10-26 ([CISA KEV, 2026-10-26](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). Belden says all versions of NetModule NRSW, including the latest mainline release 5.0.0.104, are affected and that no patched release exists; until one ships it advises disabling the web interface after confirming SSH access, with the CLI settings http.status=0 and https.status=0 ([Belden, 2026-10-22](https://assets.belden.com/asset/0e20ea6c-c1f5-4269-b765-e160a2bf4965/PSIRT-10-Critical-PHP-Vulnerabilities-in-macmon-and-NRSW.pdf)). NetModule AG is headquartered in Bern, Switzerland ([Belden, 2022-03-14](https://www.belden.com/news/belden-acquires-netmodule-ag)). Belden's macmon 6.x and 7.x use PHP in the web interface: a patch for 7.x is in the service portal, 6.x must move to 7.x, and the HTTPS web interface and guest portal must not be reachable from the internet unprotected ([Belden, 2026-10-22](https://assets.belden.com/asset/0e20ea6c-c1f5-4269-b765-e160a2bf4965/PSIRT-10-Critical-PHP-Vulnerabilities-in-macmon-and-NRSW.pdf)).

Schneider Electric lists EcoStruxure Security Expert (fixed in 1.48.4.0), ProLeiT LINEoptimize (remediation through ProLeiT support) and EcoStruxure Control Engineering, where its revision of 2026-10-26 gives an automatic update if the hosting virtual machine can reach the debian.org and sury.org repositories and a Schneider patch otherwise ([Schneider Electric, 2026-10-26](https://download.se.com/files?p_Doc_Ref=SESB-2026-295-01&p_enDocType=Security+and+Safety+Notice&p_File_Name=SESB-2026-295-01.pdf); [SecurityWeek, 2026-10-26](https://www.securityweek.com/industrial-vendors-check-products-for-php2shell-vulnerabilities/)). B&R says APROL up to R 4.4-65 is affected, with patches planned for 2026-10-26 and 2026-10-29 ([B&R, 2026-10-23](https://br-cws-assets.de-fra-1.linodeobjects.com/SA26P015-7cd6ca9c.pdf)). HMS Networks says Netbiter firmware up to 3.00.10 can be exploited from the LAN or the USB port and that 3.00.11 fixes it ([HMS Networks, 2026-10-23](https://hmsnetworks.blob.core.windows.net/nlw/docs/default-source/products/cybersecurity/security-advisory/hms-security-advisory-2026-10-22-002---netbiter-and-argos-php-vulnerabilities.pdf)). Wibu-Systems lists the web interface of CodeMeter License Central and its extensions, with 5.2.2 released and a patch installer for 5.1.2 and 5.0.x ([Wibu-Systems, 2026-10-23](https://www.wibu.com/support/product-alerts.html#c61269)). Johnson Controls has released patches for several Illustra product lines and fixed Visonic PowerManage in 5.0.45 ([SecurityWeek, 2026-10-26](https://www.securityweek.com/industrial-vendors-check-products-for-php2shell-vulnerabilities/)). Oracle's Security Alert, revised on 2026-10-26, patches Oracle Secure Backup 19.1.0.0.0 to 19.1.0.1.0, Oracle Solaris 11 and eight Oracle Communications products for CVE-2026-109618 (CVSS 3.1 9.8) and says it will extend the alert as more patches become available ([Oracle, 2026-10-26](https://www.oracle.com/security-alerts/alert-cve-2026-109618.html)).

**Exposure:** a NetModule router running NRSW, a macmon server, or any other listed product whose web interface answers from a network that is not a trusted administrative one; the vendors name the web interface as the affected component ([Belden, 2026-10-22](https://assets.belden.com/asset/0e20ea6c-c1f5-4269-b765-e160a2bf4965/PSIRT-10-Critical-PHP-Vulnerabilities-in-macmon-and-NRSW.pdf); [HMS Networks, 2026-10-23](https://hmsnetworks.blob.core.windows.net/nlw/docs/default-source/products/cybersecurity/security-advisory/hms-security-advisory-2026-10-22-002---netbiter-and-argos-php-vulnerabilities.pdf)).

**Defender takeaway:** disable the web interface of every NetModule NRSW router now, since no fixed release exists, and keep the web interfaces of the other listed products off untrusted networks until their patches are installed; install the vendor fix wherever one is listed, such as the macmon 7.x patch ([Belden, 2026-10-22](https://assets.belden.com/asset/0e20ea6c-c1f5-4269-b765-e160a2bf4965/PSIRT-10-Critical-PHP-Vulnerabilities-in-macmon-and-NRSW.pdf)), Security Expert version 1.48.4.0 ([Schneider Electric, 2026-10-26](https://download.se.com/files?p_Doc_Ref=SESB-2026-295-01&p_enDocType=Security+and+Safety+Notice&p_File_Name=SESB-2026-295-01.pdf)), Netbiter 3.00.11 ([HMS Networks, 2026-10-23](https://hmsnetworks.blob.core.windows.net/nlw/docs/default-source/products/cybersecurity/security-advisory/hms-security-advisory-2026-10-22-002---netbiter-and-argos-php-vulnerabilities.pdf)) and CodeMeter License Central 5.2.2 ([Wibu-Systems, 2026-10-23](https://www.wibu.com/support/product-alerts.html#c61269)).
