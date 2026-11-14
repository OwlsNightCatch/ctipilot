---
schema: 1
kind: vulnerability
title: "CVE-2026-109618 / CVE-2026-109619, Xerox AltaLink, EC81xx, VersaLink and WorkCentre printers and Fiery print controllers: AltaLink 82xx and 81xx, EC81xx and VersaLink remediated with PHP 8.2.35, exposure-reducing patches for WorkCentre and the AltaLink C80xx and B80xx models, Fiery patches due 2026-11-09 to 2026-11-23"
headline: "PHP2Shell: Xerox fixes AltaLink 82xx/81xx, EC81xx and VersaLink; WorkCentre gets an interim patch, Fiery due 9-23 Nov"
summary: >
  Xerox's security bulletin XRX26-016, updated on 2026-11-06, marks AltaLink 82xx and 81xx, EC81xx and VersaLink C/B415, C/B625 and C/B620
  as remediated by releases that add PHP 8.2.35 against the PHP flaws CVE-2026-109618 and CVE-2026-109619. WorkCentre 3655, EC7836 and
  EC7856 and the newly listed AltaLink C8030 to C8070, AltaLink B8045 to B8090, EC8036 and EC8056 stay affected with a system software patch
  that Xerox says reduces exposure; Fiery patches are due between 2026-11-09 and 2026-11-23 and the Worldwide Ticketing Tool fix is in
  development. The bulletin gives no statement on exploitation of Xerox devices, and CISA lists both PHP flaws as exploited.
discovered_at: "2026-11-02T04:24:00Z"
updated_at: "2026-11-08T13:57:15Z"
event_date: "2026-10-28"
run_id: 2026-11-02T0256Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, cisa-kev, patch-available]
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
    status: [cisa-kev, patch-available, mitigation-only]
    affected: "Xerox AltaLink 82xx and 81xx and EC81xx before release 123.xxx.006.29800; VersaLink C/B415, C/B625 and C/B620 before release 123.xxx.006.30100; AltaLink C8030/C8035, C8045/C8055 and C8070, AltaLink B8045/B8055 and B8065/B8075/B8090, EC8036 and EC8056; WorkCentre 3655, EC7836 and EC7856; Fiery Digital Front End; Worldwide Ticketing Tool (bulletin XRX26-016 of 2026-11-06)"
    fixed: "AltaLink 82xx, 81xx and EC81xx release 123.xxx.006.29800 and VersaLink C/B415, C/B625 and C/B620 release 123.xxx.006.30100, each adding PHP 8.2.35; WorkCentre 3655, EC7836 and EC7856 (bulletin XRX26-017) and AltaLink C80xx and B80xx, EC8036 and EC8056 (bulletin XRX26-018): a system software patch that reduces exposure, no fix; Fiery patches by 2026-11-09 (FS500 to FS800, Pro included), 2026-11-16 (FS300 to FS400, Pro included) and 2026-11-23 (FS200, Pro included); Worldwide Ticketing Tool fix in development (bulletin of 2026-11-06)"
  - id: CVE-2026-109619
    cvss: null
    epss: null
    type: memory-corruption
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, patch-available, mitigation-only]
    affected: "Xerox AltaLink 82xx and 81xx and EC81xx before release 123.xxx.006.29800; VersaLink C/B415, C/B625 and C/B620 before release 123.xxx.006.30100; AltaLink C8030/C8035, C8045/C8055 and C8070, AltaLink B8045/B8055 and B8065/B8075/B8090, EC8036 and EC8056; WorkCentre 3655, EC7836 and EC7856; Fiery Digital Front End; Worldwide Ticketing Tool (bulletin XRX26-016 of 2026-11-06)"
    fixed: "AltaLink 82xx, 81xx and EC81xx release 123.xxx.006.29800 and VersaLink C/B415, C/B625 and C/B620 release 123.xxx.006.30100, each adding PHP 8.2.35; WorkCentre 3655, EC7836 and EC7856 (bulletin XRX26-017) and AltaLink C80xx and B80xx, EC8036 and EC8056 (bulletin XRX26-018): a system software patch that reduces exposure, no fix; Fiery patches by 2026-11-09 (FS500 to FS800, Pro included), 2026-11-16 (FS300 to FS400, Pro included) and 2026-11-23 (FS200, Pro included); Worldwide Ticketing Tool fix in development (bulletin of 2026-11-06)"
sources:
  - url: "https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf"
    publisher: "Xerox (Security Bulletin XRX26-016, version of 2026-10-28)"
    date: "2026-10-28"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog (version 2026.10.30)"
    date: "2026-10-30"
    role: corroborating
  - url: "https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v5.pdf"
    publisher: "Xerox (Security Bulletin XRX26-016, version of 2026-11-03)"
    date: "2026-11-03"
    role: primary
  - url: "https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf"
    publisher: "Xerox (Security Bulletin XRX26-016, version of 2026-11-06)"
    date: "2026-11-06"
    role: primary
closed_sources: []
evidence:
  - quote: "Xerox is aware of the recently disclosed critical vulnerabilities in the PHP runtime"
    publisher: "Xerox (Security Bulletin XRX26-016, version of 2026-10-28)"
    source_url: "https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf"
  - quote: "Fix being tested. Expected to post to web November 6, 2026."
    publisher: "Xerox (Security Bulletin XRX26-016, version of 2026-10-28)"
    source_url: "https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf"
  - quote: "The vulnerable PHP component is used by a limited number of pages in the device’s Embedded Web Server."
    publisher: "Xerox (Security Bulletin XRX26-016, version of 2026-11-03)"
    source_url: "https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v5.pdf"
  - quote: "Disabling HTTP/HTTPS also disables the Embedded Web Server and any features that depend on it."
    publisher: "Xerox (Security Bulletin XRX26-016, version of 2026-11-03)"
    source_url: "https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v5.pdf"
verification: single-source
sourcing_note: >
  Xerox's own bulletin is the first-party source for its products; it gives no CVSS score, names PHP 8.2.35 as the runtime in its remediating releases, says the vulnerable PHP component
  is used by a limited number of pages in the embedded web server of AltaLink, EC81xx, VersaLink and WorkCentre devices, gives no statement on
  exploitation of Xerox devices, and says its review of the remaining products is still underway. The listing of both flaws in CISA's Known Exploited
  Vulnerabilities catalog comes from the catalog and concerns the PHP runtime, not these devices; the pre-authentication, remote nature recorded
  for the CVEs is CISA's description of the PHP flaws, since Xerox does not state an authentication requirement.
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
actions:
  - "Install release 123.xxx.006.29800 on every Xerox AltaLink 82xx, 81xx and EC81xx and release 123.xxx.006.30100 on every VersaLink C/B415, C/B625 and C/B620; apply Xerox's exposure-reducing system software patch to WorkCentre 3655, EC7836 and EC7856 (XRX26-017) and to AltaLink C80xx and B80xx, EC8036 and EC8056 (XRX26-018), and keep the web interface of those models reachable only from trusted networks or management hosts until Xerox ships a fix."
updates:
  - at: "2026-11-05T03:51:20Z"
    run_id: 2026-11-05T0255Z-intel
    type: update
    summary: >
      Xerox's bulletin of 2026-11-03 adds two interim measures for AltaLink, EC81xx, VersaLink and
      WorkCentre devices, restricting the web interface to trusted networks or management hosts or
      disabling HTTP/HTTPS, and says the vulnerable PHP component serves a limited number of pages of the
      embedded web server; fix dates are unchanged.
    fields: [summary, cves, sources, evidence, sourcing_note, actions, body]
  - at: "2026-11-08T13:57:15Z"
    run_id: 2026-11-08T1309Z-audit
    type: update
    summary: >
      Xerox's bulletin of 2026-11-06 marks AltaLink 82xx and 81xx, EC81xx and VersaLink C/B415, C/B625 and
      C/B620 as remediated by releases adding PHP 8.2.35, gives WorkCentre 3655, EC7836 and EC7856 and
      newly listed AltaLink C80xx and B80xx models an exposure-reducing patch, and keeps the Fiery dates
      of 9 to 23 November.
    fields: [actions, body, cves, headline, sources, sourcing_note, summary, tags, title]
migrated_from: null
---

Xerox's security bulletin XRX26-016, published 2026-10-23 and updated on 2026-11-06, marks AltaLink 82xx and 81xx and EC81xx as remediated by release 123.xxx.006.29800 and VersaLink C/B415, C/B625 and C/B620 by release 123.xxx.006.30100, each of which adds PHP 8.2.35 with the fixes for the PHP flaws CVE-2026-109618 and CVE-2026-109619 ([Xerox, 2026-11-06](https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf)). WorkCentre 3655, EC7836 and EC7856 and the newly listed AltaLink C8030/C8035, C8045/C8055 and C8070, AltaLink B8045/B8055 and B8065/B8075/B8090, EC8036 and EC8056 stay affected, each with a system software patch that Xerox says reduces exposure (bulletins XRX26-017 and XRX26-018) ([Xerox, 2026-11-06](https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf)). Fiery's target patch dates are by 2026-11-09 for FS800, FS700, FS600 and FS500, by 2026-11-16 for FS400, FS350 and FS300, and by 2026-11-23 for FS200, each including the Pro editions, and the Worldwide Ticketing Tool fix is in development ([Xerox, 2026-11-06](https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf)). For the affected AltaLink, EC81xx, VersaLink and WorkCentre devices Xerox says the vulnerable PHP component is used by a limited number of pages in the embedded web server and names two interim measures: restricting the web interface to trusted networks or management hosts, and disabling HTTP/HTTPS, which also disables the embedded web server and all authentication, authorization and accounting solutions, and cannot be re-enabled remotely ([Xerox, 2026-11-06](https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf)). The bulletin gives no statement on exploitation of Xerox devices, while CISA added both PHP flaws to its Known Exploited Vulnerabilities catalog on 2026-10-26 and describes each as allowing unauthenticated remote code execution in PHP ([CISA KEV, 2026-10-30](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

**Exposure:** the models above before their remediating release, the patched-but-unfixed models, and the Fiery controllers in FS200 to FS800 releases; on AltaLink, EC81xx, VersaLink and WorkCentre the affected component sits behind the embedded web server's HTTP/HTTPS interface, so that interface is the surface to restrict. Xerox lists as not impacted, among others, Lexmark printer firmware, VersaLink B400, B405, B600, B605, B610, B615, C400, C405, C500, C505, C600 and C605, C8000, C9000 and the C/B70xx and C/B71xx series, WorkCentre 3335, 3345 and 6515, and the Phaser and PrimeLink models it names, and says its review of other products is still underway ([Xerox, 2026-11-06](https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf)).

**Defender takeaway:** install the remediating releases on AltaLink 82xx and 81xx, EC81xx and VersaLink now; on WorkCentre 3655, EC7836 and EC7856 and the AltaLink C80xx and B80xx models apply Xerox's exposure-reducing patch and keep the web interface restricted to trusted networks or management hosts until a fix ships, and, as Xerox names no interim measure for the Fiery controllers or the Ticketing Tool, treat network reachability as their lever until the Fiery patches land between 2026-11-09 and 2026-11-23 ([Xerox, 2026-11-06](https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf)). Xerox warns not to disable HTTP/HTTPS on a device that runs an AAA solution or is managed remotely, because recovery requires manual action at each device ([Xerox, 2026-11-06](https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf)).

## Update — 2026-11-05T03:51:20Z

Xerox revised bulletin XRX26-016 on 2026-11-03 and added a mitigation section for AltaLink, EC81xx, VersaLink and WorkCentre devices, which the version of 2026-10-28 did not carry ([Xerox, 2026-11-03](https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v5.pdf); [Xerox, 2026-10-28](https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v4.pdf)). It says the vulnerable PHP component is used by a limited number of pages in the device's embedded web server, and that until the fix is installed customers can restrict the web interface (HTTP/HTTPS) to trusted networks or management hosts, for example with a firewall or segmentation, or disable HTTP/HTTPS if remote web administration is not required, which also disables the embedded web server and the features that depend on it ([Xerox, 2026-11-03](https://securitydocs.business.xerox.com/wp-content/uploads/2026/10/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v5.pdf)). The section does not cover the Fiery Digital Front End or the Worldwide Ticketing Tool, and the affected table and the fix dates are unchanged.

## Update — 2026-11-08T13:57:15Z

Xerox updated bulletin XRX26-016 on 2026-11-06: AltaLink 82xx and 81xx and EC81xx (release 123.xxx.006.29800) and VersaLink C/B415, C/B625 and C/B620 (release 123.xxx.006.30100) are remediated by releases that add PHP 8.2.35 ([Xerox, 2026-11-06](https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf)). WorkCentre 3655, EC7836 and EC7856 stay affected but now have a system software patch that Xerox says reduces exposure (bulletin XRX26-017), and the bulletin newly lists AltaLink C8030/C8035, C8045/C8055 and C8070, AltaLink B8045/B8055 and B8065/B8075/B8090, EC8036 and EC8056 as affected, with the same kind of patch (bulletin XRX26-018) ([Xerox, 2026-11-06](https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf)). It now also warns that HTTP/HTTPS, once disabled, cannot be re-enabled remotely and should not be disabled on a device that runs an AAA solution or is managed remotely ([Xerox, 2026-11-06](https://securitydocs.business.xerox.com/wp-content/uploads/2026/11/Xerox-Security-Bulletin-XRX26-016-for-PHP2Shell-Vulnerabilities-CVE-2026-109618-and-CVE-2026-109619-v6.pdf)). The Fiery target dates are unchanged.
