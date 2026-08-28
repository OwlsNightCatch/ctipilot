---
schema: 1
kind: vulnerability
horizon: strategic
title: >
  2026-W33 vulnerability status roll-up — eight flaws crossed into confirmed exploitation or the
  federal catalogue this week, two of them within seventy-two hours of their own disclosure,
  against a critical tail led by two unauthenticated CVSS 10.0 flaws in industrial edge devices
headline: >
  W33 CVE trajectory — eight newly exploited or newly catalogued, one exploited with no identifier
  at all, and eight flaws with no fix in existence
summary: >
  Consolidated status of the vulnerabilities covered operationally here in ISO week
  2026-W33, each with its trajectory this week set against when it was first covered. Newly
  confirmed exploited or newly KEV-listed: CVE-2026-20349 (Cisco Secure Firewall ASA/FTD),
  CVE-2026-68820 (Windows AFD.sys, a Lazarus zero-day), CVE-2026-72898 (Metabase, CVSS 10.0),
  CVE-2026-59310 (VMware vCenter), CVE-2026-55040 (Microsoft SharePoint), CVE-2026-65400 (macOS
  Screen Sharing), CVE-2026-58231 (SAP Commerce Cloud) and CVE-2026-71362 (Adobe Commerce).
  CVE-2026-45659 gained a ransomware-campaign-use flag rather than a new exploitation finding.
  Exploited with no identifier: the GeoServer jsonArrayContains SQL injection, which also has no
  patch. The critical tail is led by two unauthenticated CVSS 10.0 flaws on industrial edge
  devices — Siemens SIMATIC IoT2050 Advanced and the Haiwell IoT Cloud HMI Gateway — and by eight
  flaws where no fix exists at all. Full per-flaw detail lives in the referenced operational
  entries; this roll-up carries only the week's trajectory.
discovered_at: "2026-08-16T23:58:00Z"
updated_at: null
event_date: 2026-08-14
run_id: 2026-08-16T2315Z-weekly
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - actively-exploited
  - cisa-kev
  - no-patch
  - ot-ics
  - rce
  - auth-bypass
  - sqli
  - pre-auth
  - patch-available
regions:
  - switzerland
  - europe
  - global
sectors:
  - public-sector
  - energy
  - water
  - finance
  - technology
  - transport
entities: []
techniques:
  - T1190
  - T1068
  - T1078
  - T1499.004
  - T1606
  - T1496
affected_products:
  - Cisco Secure Firewall Adaptive Security Appliance (ASA)
  - Cisco Secure Firewall Threat Defense (FTD)
  - Microsoft Windows 11
  - Metabase
  - VMware vCenter Server
  - Microsoft SharePoint Server Subscription Edition
  - Apple macOS Tahoe
  - SAP Commerce Cloud
  - Adobe Commerce
  - Magento Open Source
  - Siemens SIMATIC IoT2050 Advanced
  - Haiwell IoT Cloud HMI Gateway
  - GeoServer
  - Citrix NetScaler ADC
  - Citrix NetScaler Gateway
  - GeoTools
cves:
  - id: CVE-2026-76904
    cvss: "9.8"
    epss: null
    type: sqli
    vector: zero-click
    auth: pre-auth
    status:
      - exploited
      - patch-available
    affected: >
      GeoTools gt-jdbc-postgis from 35.0 before 35.1, from 34.0 before 34.5, and from 30.5 before 33.6
      — shipped in GeoServer before 3.0.1, 2.28.5 and 2.27.6 respectively
    fixed: "GeoServer 3.0.1, 2.28.5, 2.27.6 (released 2026-08-14), carrying GeoTools 35.1, 34.5 and 33.6"
sources:
  - url: "https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/"
    publisher: BleepingComputer
    date: 2026-08-14
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog"
    publisher: CISA
    date: 2026-08-11
    role: primary
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF"
    publisher: Cisco PSIRT
    date: 2026-08-11
    role: primary
  - url: "https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/"
    publisher: Check Point Research
    date: 2026-08-11
    role: primary
  - url: "https://advisories.ncsc.nl/2026/ncsc-2026-0280.html"
    publisher: NCSC-NL (Nationaal Cyber Security Centrum)
    date: 2026-08-12
    role: primary
  - url: "https://advisories.ncsc.nl/2026/ncsc-2026-0302.html"
    publisher: NCSC-NL (Nationaal Cyber Security Centrum)
    date: 2026-08-15
    role: primary
  - url: "https://www.bleepingcomputer.com/news/microsoft/hackers-leverage-new-microsoft-sharepoint-exploit-in-attacks/"
    publisher: BleepingComputer
    date: 2026-08-12
    role: primary
  - url: "https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html"
    publisher: The Hacker News
    date: 2026-08-12
    role: corroborating
  - url: "https://www.securityweek.com/hackers-exploiting-unpatched-geoserver-zero-day/"
    publisher: SecurityWeek
    date: 2026-08-14
    role: primary
  - url: "https://cert-portal.siemens.com/productcert/html/ssa-834709.html"
    publisher: Siemens ProductCERT
    date: 2026-08-11
    role: primary
  - url: "https://sansec.io/research/adobe-commerce-account-takeover-apsb26-92"
    publisher: Sansec Forensics Team
    date: 2026-08-11
    role: primary
  - url: "https://helpx.adobe.com/security/products/magento/apsb26-92.html"
    publisher: Adobe PSIRT
    date: 2026-08-11
    role: primary
  - url: "https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html"
    publisher: GeoServer project (OSGeo)
    date: 2026-08-14
    role: primary
  - url: "https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-2-28-5-released.html"
    publisher: GeoServer project (OSGeo)
    date: 2026-08-14
    role: primary
  - url: "https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-2-27-6-released.html"
    publisher: GeoServer project (OSGeo)
    date: 2026-08-14
    role: primary
  - url: "https://api.osv.dev/v1/vulns/GHSA-mqjf-5f49-2fjh"
    publisher: OSV (mirroring the GeoTools GitHub Security Advisory)
    date: 2026-08-21
    role: primary
closed_sources: []
evidence:
  - quote: "First exploitation attempts against CVE-2026-58231 (unauth RCE in SAP Commerce Cloud, CVSS 10.0) is now hitting our honeypots - 3 days after patch day"
    publisher: "Defused, quoted by BleepingComputer"
  - quote: In al deze gevallen was root toegang verkregen op het getroffen systeem en een Monero crypto miner geplaatst.
    publisher: NCSC-NL
  - quote: "During the intrusion, the threat actor exploited CVE-2026-68820, a zero-day vulnerability in the Microsoft AFD.sys driver, to deploy a new version of FudModule, Lazarus’ kernel-mode rootkit."
    publisher: Check Point Research
  - quote: "GeoServer 3.0.1 is made in conjunction with GeoTools 35.1, and GeoWebCache 2.0.1."
    publisher: GeoServer project (OSGeo)
    url: "https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html"
verification: multi-source
sourcing_note: >
  Each CVE's status is taken from the record that owns it — the vendor PSIRT bulletin, the CISA
  catalogue entry, or the disclosing researcher's own advisory — as recorded in the referenced
  operational entries and re-checked against the fetched sources listed here. Where a status
  change rests on a single observer (Defused's honeypot telemetry for SAP Commerce Cloud and
  SharePoint, QUIRSO's incident-response findings for vCenter, watchTowr's telemetry for
  GeoServer), that observer is named rather than the finding being presented as vendor-confirmed.
  Microsoft does not record CVE-2026-55040 as exploited; the exploitation finding is Defused's.
confidence: high
references:
  - 2026-08-12/cve-2026-20349-cisco-asa-ftd-ssl-vpn-dos-exploited
  - 2026-08-12/lazarus-operation-dream-job-cve-2026-68820-afd-fudmodule
  - 2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally
  - 2026-07-30/vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape
  - 2026-07-14/microsoft-july-2026-patch-tuesday-two-exploited-zero-days
  - 2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass
  - 2026-08-12/sap-august-2026-cve-2026-58231-commerce-cloud-data-hub-rce
  - 2026-08-16/cve-2026-71362-adobe-commerce-customer-account-takeover
  - 2026-07-02/cve-2026-45659-microsoft-sharepoint-server-authenticated-des
  - 2026-08-13/cve-2026-58115-simatic-iot2050-node-red-unauth-root
  - 2026-08-15/cve-2026-19188-haiwell-hmi-gateway-unauth-root-rce
  - 2026-08-15/geoserver-jsonarraycontains-unauth-sqli-zeroday-exploited
  - 2026-07-01/cve-2026-8451-citrix-netscaler-adc-gateway-pre-auth-saml-mem
  - 2026-08-12/shieldbreak-defender-rogueplanet-patch-bypass-no-fix
  - 2026-08-10/wazuh-4-14-6-cluster-root-rce-preauth-authd-overflow
  - 2026-08-10/wordpress-core-xss2shell-cve-2026-64638-preauth-xss-to-rce
  - 2026-08-10/freebsd-ctl-ha-three-preauth-kernel-rce-primitives-port-999
  - 2026-08-15/fortiweb-radius-wildcard-bypass-fortimanager-fgfm
  - 2026-08-08/flowise-three-cves-vendor-sunset-no-fix-coming
  - 2026-08-10/natjack-nat-trust-assumption-attack-class-two-cves
  - 2026-08-16/weekly-w33-looking-ahead
  - 2026-08-16/weekly-w33-disclosure-to-exploitation-interval-collapsed
weekly_section: weekly-vuln-rollup
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "If a GeoServer estate was triaged off the 2026-W33 weekly, re-triage it: upgrade to GeoServer 3.0.1, 2.28.5 or 2.27.6 on the matching branch rather than relying on network isolation, and disregard any internal note recording this flaw as having no vendor fix."
updates:
  - at: "2026-08-24T10:00:00Z"
    run_id: 2026-08-24T0902Z-audit
    type: correction
    summary: >
      Three 2026-W33 weekly entries published 2026-08-16T23:5xZ stated that the actively exploited
      jsonArrayContains SQL injection in GeoServer had no CVE and no vendor patch, and one of them
      told readers that removing query endpoints from the public internet was the whole remediation.
      OSGeo had released GeoServer 3.0.1, 2.28.5 and 2.27.6 on 2026-08-14 — two days before those
      entries published — carrying the GeoTools 35.1, 34.5 and 33.6 fixes for exactly this flaw. The
      flaw now also has an identifier, CVE-2026-76904, assigned when the advisory published on
      2026-08-21. The correct remediation is and was to upgrade. The pipeline's own operational
      coverage caught up on 2026-08-18, but the weekly entries are immutable and still carry the wrong
      instruction, which is what this entry exists to fix.
    fields:
      - actions
      - affected_products
      - cves
      - evidence
      - references
      - sectors
      - sources
      - tags
      - body
    merged_from: 2026-08-24/correction-geoserver-w33-no-vendor-fix-claim-patch-existed
  - at: "2026-08-28T15:00:00Z"
    run_id: 2026-08-28T1500Z-audit
    type: improvement
    internal: true
    summary: >
      v4.2 migration: updated_at recomputed under the new float rule (only type: update 
      records move updated_at; corrections/improvements no longer re-float the entry).
    fields: [summary, updated_at, body]
migrated_from: null
---

**Newly exploited or newly catalogued this week.** Two flaws crossed into exploitation within seventy-two hours of their own disclosure and are treated at length in this week's lead entry, alongside a third whose exploit was rebuilt from the patch diff in four hours but whose confirmed exploitation followed six days later: CVE-2026-58231 in the SAP Commerce Cloud Data Hub Adapter, where Defused recorded the first honeypot hits three days after SAP's patch day and stated the flaw had no public proof-of-concept ([BleepingComputer, 2026-08-14](https://www.bleepingcomputer.com/news/security/max-severity-sap-commerce-cloud-flaw-now-targeted-in-attacks/)) and NCSC-NL published a national advisory recording active scanning ([NCSC-NL, 2026-08-15](https://advisories.ncsc.nl/2026/ncsc-2026-0302.html)); CVE-2026-55040 in SharePoint Server, where Rapid7's proof-of-concept was being replayed against honeypots the morning after publication, against a population of over 8,500 internet-reachable servers ([BleepingComputer, 2026-08-12](https://www.bleepingcomputer.com/news/microsoft/hackers-leverage-new-microsoft-sharepoint-exploit-in-attacks/)); and CVE-2026-65400 in the macOS Screen Sharing daemon, which NCSC-NL revised to record active abuse on internet-reachable port-5900 systems where "In al deze gevallen was root toegang verkregen op het getroffen systeem en een Monero crypto miner geplaatst" ([NCSC-NL, 2026-08-12](https://advisories.ncsc.nl/2026/ncsc-2026-0280.html)).

Five more moved on the exploitation axis on their own timelines. **CVE-2026-20349** is the week's clearest edge item: Cisco disclosed it on 11 August stating its PSIRT had become aware of active exploitation that month, with one crafted HTTP request to the Remote Access SSL VPN reloading the device, no workaround and only per-train hot fixes ([Cisco PSIRT, 2026-08-11](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-vpn-dos-dzv4mQFF)); CISA added it the same day ([CISA, 2026-08-11](https://www.cisa.gov/news-events/alerts/2026/08/11/cisa-adds-three-known-exploited-vulnerabilities-catalog)). **CVE-2026-68820** was fixed in August's Microsoft updates as an exploitation-detected flaw, and Check Point's analysis records that "During the intrusion, the threat actor exploited CVE-2026-68820, a zero-day vulnerability in the Microsoft AFD.sys driver, to deploy a new version of FudModule, Lazarus' kernel-mode rootkit" ([Check Point Research, 2026-08-11](https://research.checkpoint.com/2026/shattering-the-dream-when-a-job-offer-becomes-a-zero-day-attack/)). **CVE-2026-72898** is the Metabase zero-day covered here on 9 August when no identifier existed: it now carries CVSS 10.0 and entered the KEV catalogue on 11 August, which matters because a flaw with no CVE was invisible to every scanner and SBOM pipeline in the estate. **CVE-2026-59310** in the VMware vCenter Syslog server, reported unexploited at disclosure on 29 July, was found by QUIRSO to have 361 unique victim IP addresses across 47 countries with first attacker contact on 3 August, concentrated in Germany, the United States, Turkey, Iran and France ([The Hacker News, 2026-08-12](https://thehackernews.com/2026/08/attackers-exploit-vmware-vcenter.html)). **CVE-2026-71362** in Adobe Commerce is an unauthenticated customer-account takeover which Adobe's own bulletin records as needing no authentication, privileges or user interaction, and while stating in the same bulletin that it is not aware of any exploits in the wild ([Adobe PSIRT, 2026-08-11](https://helpx.adobe.com/security/products/magento/apsb26-92.html)); the exploitation signal is a forensics vendor's, which reviewed the patch and reports its own web application firewall already blocking attempts ([Sansec Forensics Team, 2026-08-11](https://sansec.io/research/adobe-commerce-account-takeover-apsb26-92)).

One entry on this list is a status refinement rather than a new finding, and the distinction matters for planning: **CVE-2026-45659** in SharePoint has been catalogued as exploited since 1 July and gained the catalogue's "Known" ransomware-campaign-use flag this week. Nothing about its exploitation changed; what changed is the expected outcome for an unpatched farm, which moves from data access toward encryption and extortion — a recovery-planning input, not a patch-priority one, since the fix has been available since May.

**Exploited with no identifier, and unpatched.** The GeoServer `jsonArrayContains` SQL injection is the week's hardest case for any CVE-keyed process: disclosed by a researcher on 12 August with no CVE assigned and no vendor patch available, it drew "hundreds of attempts originating from a small number of source IP addresses" within hours per watchTowr ([SecurityWeek, 2026-08-14](https://www.securityweek.com/hackers-exploiting-unpatched-geoserver-zero-day/)). GeoServer underpins public-sector geoportals and INSPIRE spatial-data services across Europe, and Switzerland's NCSC issued its own advisory on 14 August; with no patch, exposure reduction is the entire remediation.

**The critical tail.** Two unauthenticated CVSS 10.0 flaws landed on industrial edge devices and neither is reported exploited. Siemens ProductCERT disclosed CVE-2026-58115, where SIMATIC IoT2050 Advanced devices running Industrial OS with Node-RED installed do not enforce authentication on the Node-RED HTTP interface, exposing programming nodes capable of running system commands as root ([Siemens ProductCERT, 2026-08-11](https://cert-portal.siemens.com/productcert/html/ssa-834709.html)); CISA's ICS advisory for CVE-2026-19188 covers a command injection in the Haiwell IoT Cloud HMI Gateway's diagnostic ping endpoint reaching root without credentials, in a product CISA reports deployed in energy, critical manufacturing and water and wastewater and assesses automatable. Alongside them, this week's disclosures left eight flaws with no fix in existence: the ShieldBreak bypass of Microsoft's July Defender fix, the three FreeBSD CTL HA pre-authentication kernel primitives behind TCP/999, the GeoServer injection, and three of the five NatJack NAT primitives. The NetScaler pair is the week's most consequential reclassification rather than a new flaw — watchTowr's published chain shows CVE-2026-8452 reaching a pre-authentication root shell rather than the availability issue its public description suggested, and NCSC-CH has carried the sibling CVE-2026-8451 as actively exploited with a public proof-of-concept since 3 July.

## Correction — 2026-08-24T10:00:00Z

The correction is to a remediation instruction, so it is worth stating before the reasoning. GeoServer's actively exploited `jsonArrayContains` SQL injection had a vendor fix at the time the 2026-W33 weekly published, and the weekly said it did not.

OSGeo released three versions on 2026-08-14, each announced separately and each paired with the GeoTools release carrying the fix: 3.0.1, which "is made in conjunction with GeoTools 35.1, and GeoWebCache 2.0.1" ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-3-0-1-released.html)); 2.28.5, made in conjunction with GeoTools 34.5 ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-2-28-5-released.html)); and 2.27.6, made in conjunction with GeoTools 33.6 ([GeoServer project, 2026-08-14](https://geoserver.org/announcements/vulnerability/2026/08/14/geoserver-2-27-6-released.html)). The advisory's structured record gives the three fixed ranges precisely: the `org.geotools.jdbc:gt-jdbc-postgis` module is affected from 35.0 before 35.1, from 34.0 before 34.5, and from 30.5 before 33.6, and the flaw now carries the identifier CVE-2026-76904, assigned when the advisory published on 2026-08-21 ([OSV, 2026-08-21](https://api.osv.dev/v1/vulns/GHSA-mqjf-5f49-2fjh)). Three W33 entries — the vulnerability status roll-up, the outlook, and the disclosure-to-exploitation piece — each recorded the flaw as having no CVE and no vendor patch, and the outlook went further, telling readers that until OSGeo shipped something, taking query endpoints off the public internet was the remediation.

Two things went wrong, and only one of them is about GeoServer. The reporting the weekly relied on was a 2026-08-14 news article headlined around an unpatched zero-day, published the same day as the vendor's release and therefore already stale as it went out; and the national advisory the weekly also cited did not append the fixed-version links until 2026-08-17, the day after the weekly. So both of the weekly's sources said "no patch" while the vendor's own release channel said otherwise. Nobody checked the release channel. A claim that no fix exists is a negative claim with an expiry date, and the only source that can carry it is the party that would ship the fix.

There is a second, still-live trap in the advisory itself: its human-readable patch summary names a different set of GeoTools versions than its own structured ranges and its linked release tags. A defender following the prose upgrades to versions that are not the fixes. Take the versions from the vendor's release announcements or the advisory's machine-readable ranges, both cited above.

**Defender takeaway:** if this flaw was triaged off the W33 weekly, the estate was probably given a network-isolation instruction when an upgrade was available, and the isolation may since have been relaxed on the belief that nothing more could be done. Re-triage on version numbers. More generally, the store's operational coverage corrected itself on 2026-08-18 and the strategic surface did not, so a reader who works from the weekly and a reader who works from the daily entries were told different things for a week — when a status roll-up and a later operational entry disagree, the more recent entry and the vendor's own release page win.
