---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, Xerox AltaLink, EC81xx, VersaLink and WorkCentre printers and Fiery print controllers: Xerox lists them as affected by the PHP2Shell flaws, with fixes expected on 2026-11-06 and Fiery patches between 2026-11-09 and 2026-11-23"
headline: "PHP2Shell affects Xerox AltaLink and VersaLink printers and Fiery controllers; fixes due 6 to 23 November"
summary: >
  Xerox's security bulletin XRX26-016 (published 2026-10-23, updated 2026-10-28) lists AltaLink, EC81xx, VersaLink C/B415, C/B625 and C/B620,
  WorkCentre 3655, EC7836 and EC7856, the Fiery Digital Front End and the Worldwide Ticketing Tool as affected by the PHP flaws CVE-2026-109618
  and CVE-2026-109619, and no fixed build is out: Xerox expects the AltaLink, EC81xx and VersaLink fixes on 2026-11-06, Fiery patches are due
  between 2026-11-09 and 2026-11-23, and the WorkCentre and Ticketing Tool fixes are in development. The bulletin names no workaround, interface
  or attack on these devices; CISA lists both PHP flaws as exploited.
discovered_at: "2026-11-02T04:24:00Z"
updated_at: null
event_date: "2026-10-28"
run_id: 2026-11-02T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, cisa-kev, no-patch]
regions: [global]
sectors: []
entities: ["tool:php2shell", "product:php", "product:xerox-altalink", "product:xerox-ec81xx", "product:xerox-versalink", "product:xerox-workcentre", "product:fiery-digital-front-end", "product:xerox-worldwide-ticketing-tool"]
techniques: [T1190]
affected_products: ["Xerox AltaLink", "Xerox EC81xx", "Xerox VersaLink", "Xerox WorkCentre", "Fiery Digital Front End", "Xerox Worldwide Ticketing Tool"]
cves:
  - id: CVE-2026-109618
    cvss: null
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, no-patch]
    affected: "Xerox AltaLink and EC81xx; VersaLink C/B415, C/B625 and C/B620; WorkCentre 3655, EC7836 and EC7856; Fiery Digital Front End; Worldwide Ticketing Tool (most current releases evaluated, bulletin XRX26-016 version 4)"
    fixed: "none released as of 2026-10-28: AltaLink, EC81xx and VersaLink fixes expected 2026-11-06; Fiery patches by 2026-11-09 (FS500 to FS800, Pro included), 2026-11-16 (FS300 to FS400, Pro included) and 2026-11-23 (FS200, Pro included); WorkCentre and Worldwide Ticketing Tool fixes in development"
  - id: CVE-2026-109619
    cvss: null
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, no-patch]
    affected: "Xerox AltaLink and EC81xx; VersaLink C/B415, C/B625 and C/B620; WorkCentre 3655, EC7836 and EC7856; Fiery Digital Front End; Worldwide Ticketing Tool (most current releases evaluated, bulletin XRX26-016 version 4)"
    fixed: "none released as of 2026-10-28: AltaLink, EC81xx and VersaLink fixes expected 2026-11-06; Fiery patches by 2026-11-09 (FS500 to FS800, Pro included), 2026-11-16 (FS300 to FS400, Pro included) and 2026-11-23 (FS200, Pro included); WorkCentre and Worldwide Ticketing Tool fixes in development"
sources:
  - url: "https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf"
    publisher: "Xerox (Security Bulletin XRX26-016, version 4)"
    date: "2026-10-28"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.30)"
    date: "2026-10-30"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Xerox is aware of the recently disclosed critical vulnerabilities in the PHP runtime"
    publisher: "Xerox (Security Bulletin XRX26-016, version 4)"
    source_url: "https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf"
  - quote: "Fix being tested. Expected to post to web November 6, 2026."
    publisher: "Xerox (Security Bulletin XRX26-016, version 4)"
    source_url: "https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf"
verification: single-source
sourcing_note: >
  Xerox's own bulletin is the first-party source for its products; it gives no CVSS score, no affected interface or PHP version and no statement
  on exploitation of Xerox devices, and says its review of the remaining products is still underway. The listing of both flaws in CISA's
  Known Exploited Vulnerabilities catalog comes from the catalog and concerns the PHP runtime, not these devices; the pre-authentication, remote nature recorded for the CVEs is CISA's description of the PHP flaws, since Xerox does not say which device interface is reachable.
confidence: high
references:
  - 2026-10-21/php-critical-release-pre-announced-cve-2026-109618-109619
  - 2026-10-22/pan-os-panorama-php2shell-mgmt-interface-no-fixed-release
  - 2026-10-23/netscaler-php2shell-management-gui-fixes-2026-10-27
  - 2026-10-25/qnap-synology-php2shell-qts-quts-hero-fixed-others-unfixed
  - 2026-10-27/php2shell-ot-products-netmodule-nrsw-no-fix-macmon-schneider
  - 2026-10-28/cisco-php2shell-expressway-urwb-duo-access-gateway-fixes
  - 2026-10-28/hpe-clearpass-php2shell-hotfixes-hpesbnw05171
  - 2026-10-29/check-point-php2shell-sk1000302-portal-and-vpn-gateways
  - 2026-10-29/f5-big-ip-php2shell-k000163821-critical-releases
  - 2026-10-29/php2shell-trend-micro-apex-quest-kace-netapp-ontap
  - 2026-10-31/php2shell-broadcom-sepm-carbon-black-app-control-casma
  - 2026-05-15/cve-2026-46300-linux-kernel-local-privilege-escalation-via-x
  - 2026-10-27/camping-care-tcs-camping-data-theft-php-flaw-whatsapp-fraud
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

Xerox's security bulletin XRX26-016, published 2026-10-23 and updated on 2026-10-28, lists Xerox AltaLink and EC81xx products, VersaLink C/B415, C/B625 and C/B620, WorkCentre 3655, EC7836 and EC7856, the Fiery Digital Front End and the Worldwide Ticketing Tool as affected by the PHP flaws CVE-2026-109618 and CVE-2026-109619 ([Xerox, 2026-10-28](https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf)). No fixed build is out: Xerox says the AltaLink, EC81xx and VersaLink fixes are being tested and expected on its website on 2026-11-06, the WorkCentre models and the Ticketing Tool are in development, and Fiery's target patch dates are by 2026-11-09 for FS800, FS700, FS600 and FS500 including the Pro editions, by 2026-11-16 for FS400, FS350 and FS300, and by 2026-11-23 for FS200 ([Xerox, 2026-10-28](https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf)). The bulletin does not name the affected interface or PHP version, offers no workaround and reports no attack on these devices, while CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26 and describes each as allowing unauthenticated remote code execution in PHP ([CISA KEV, 2026-10-30](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

**Exposure:** the models above and the Fiery controllers in FS200 to FS800 releases. Xerox lists as not impacted, among others, Lexmark printer firmware, VersaLink B400 to B615, C400 to C605, C8000, C9000 and the C/B70xx and C/B71xx series, WorkCentre 3335, 3345 and 6515, and the Phaser and PrimeLink models it names, and says the review of its remaining products is still underway ([Xerox, 2026-10-28](https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf)).

**Defender takeaway:** find which of the listed models and Fiery controllers the estate and its print suppliers run, and treat any that untrusted networks can reach as exposed to an exploited flaw class: Xerox names no interim mitigation, so the lever is network reachability until the fixes are installed on release, 2026-11-06 for AltaLink, EC81xx and VersaLink and 2026-11-09 to 2026-11-23 for Fiery ([Xerox, 2026-10-28](https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf)).
