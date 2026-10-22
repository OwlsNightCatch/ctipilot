---
schema: 1
kind: threat
title: "BSI lists two authenticated pfSense CE code-execution flaws as critical: CVE-2025-69690 (CE 2.7.2) and CVE-2025-69691 (CE 2.8.0), disputed by Netgate"
headline: "BSI rates two admin-authenticated pfSense CE code-execution flaws critical; Netgate disputes them and plans no patch"
summary: "BSI's advisory WID-SEC-2026-1435 of 2026-05-08 lists CVE-2025-69690 in Netgate pfSense CE 2.7.2 and CVE-2025-69691 in pfSense CE 2.8.0 as critical: both let an authenticated administrator run code as root, through a crafted configuration backup and through the XMLRPC method pfsense.exec_php. The researcher says Netgate acknowledged the reports but will issue no patch, and the CVE records note that the supplier disputes both because the functions are available only to administrators."
discovered_at: "2026-05-11T05:00:00Z"
event_date: 2026-05-08
run_id: 2026-05-11-migrated
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - rce
  - no-patch
  - default-config
regions:
  - dach
  - europe
sectors:
  - public-sector
  - education
  - healthcare
entities: []
techniques: [T1078.001, T1059, T1059.004]
affected_products: ["Netgate pfSense CE"]
cves:
  - id: CVE-2025-69690
    cvss: "9.1"
    epss: null
    type: deserialization
    vector: zero-click
    auth: admin-required
    status:
      - no-patch
      - poc-public
    affected: "pfSense CE 2.7.2"
    fixed: "none (the supplier disputes the vulnerability)"
  - id: CVE-2025-69691
    cvss: "9.9"
    epss: null
    type: rce
    vector: zero-click
    auth: admin-required
    status:
      - no-patch
      - poc-public
    affected: "pfSense CE 2.8.0"
    fixed: "none (the supplier disputes the vulnerability)"
sources:
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1435"
    publisher: "BSI WID-SEC-2026-1435"
    date: "2026-05-08"
    role: primary
  - url: "https://seclists.org/fulldisclosure/2026/Feb/16"
    publisher: "Full Disclosure (Nelson Adhepeau)"
    date: "2026-02-16"
    role: primary
  - url: "https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-1435.json"
    publisher: "BSI WID-SEC-W-2026-1435 (CSAF version)"
    date: "2026-05-08"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2025-209738"
    publisher: "ENISA EUVD (EUVD-2025-209738, CVE-2025-69690)"
    date: "2026-05-08"
    role: corroborating
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2025-209739"
    publisher: "ENISA EUVD (EUVD-2025-209739, CVE-2025-69691)"
    date: "2026-05-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An attacker can exploit several vulnerabilities in Netgate pfSense to execute arbitrary program code with administrator rights. (translated from German)"
    original: "Ein Angreifer kann mehrere Schwachstellen in Netgate pfSense ausnutzen, um beliebigen Programmcode mit Administratorrechten auszuführen."
    publisher: "BSI WID-SEC-W-2026-1435 (CSAF version)"
    source_url: "https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-1435.json"
  - quote: "The vendor was notified on December 2, 2025, acknowledged the reports, and indicated no patches would be issued."
    publisher: "Full Disclosure (Nelson Adhepeau)"
    source_url: "https://seclists.org/fulldisclosure/2026/Feb/16"
  - quote: "post_reboot_commands property, executed through mwexec()"
    publisher: "Full Disclosure (Nelson Adhepeau)"
    source_url: "https://seclists.org/fulldisclosure/2026/Feb/16"
  - quote: "pfsense.exec_php that executes arbitrary PHP code as root"
    publisher: "Full Disclosure (Nelson Adhepeau)"
    source_url: "https://seclists.org/fulldisclosure/2026/Feb/16"
  - quote: "NOTE: the Supplier disputes this because the API call is only available to admins and they are intentionally allowed to execute PHP code."
    publisher: "ENISA EUVD (EUVD-2025-209739, CVE-2025-69691)"
    source_url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2025-209739"
verification: multi-source
sourcing_note: >
  One researcher's disclosure with proof of concept, recorded by BSI and ENISA's EUVD; neither authority published its own analysis
  or mitigation, and Netgate's position is known only from the researcher's account and the supplier's dispute note in the CVE records.
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-11.md
updates:
  - at: "2026-10-21T20:35:05Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      BSI's advisory WID-SEC-2026-1435 lists the two pfSense CE flaws as critical but says nothing about
      patch status or mitigation, so the critical-unpatched framing and the claim that a national
      authority recommends mitigation go. CVE-2025-69690 scores 9.1 in ENISA's EUVD against the
      researcher's 8.8, both flaws need administrator credentials, Netgate's no-patch position comes from
      the researcher, and the supplier disputes both in the CVE records; no source addresses pfSense Plus.
    fields: [affected_products, body, classification, confidence, cves, evidence, headline, priority, sources, sourcing_note, summary, techniques, title]
---

BSI listed two Netgate pfSense Community Edition (CE) vulnerabilities in its advisory WID-SEC-2026-1435, released on 2026-05-08 (22:00 UTC on 2026-05-07), with severity critical: an attacker can exploit them to execute arbitrary code with administrator rights ([BSI WID-SEC-W-2026-1435](https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-1435.json)). Both come from a researcher's Full Disclosure post of 2026-02-16 ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16)). CVE-2025-69690 affects pfSense CE 2.7.2: the configuration restore mechanism calls unserialize() on user-controlled data, so a crafted backup file carrying a serialized PHP object injects commands through its post_reboot_commands property, and they run through mwexec() as root ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16)). CVE-2025-69691 affects pfSense CE 2.8.0: the XMLRPC API method pfsense.exec_php runs arbitrary PHP code as root ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16)). The researcher scores them 8.8 and 9.9 under CVSS 3.1 ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16)), and ENISA's EUVD records 9.1 and 9.9 ([EUVD-2025-209738](https://euvd.enisa.europa.eu/vulnerability/EUVD-2025-209738); [EUVD-2025-209739](https://euvd.enisa.europa.eu/vulnerability/EUVD-2025-209739)).

According to the researcher, Netgate was notified on 2025-12-02, acknowledged the reports, classified both as expected behaviour for authenticated administrators and indicated that no patches would be issued ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16)); the CVE records note that the supplier disputes them because the functions are only available to administrators, who are intentionally allowed to execute PHP code ([EUVD-2025-209739](https://euvd.enisa.europa.eu/vulnerability/EUVD-2025-209739)). BSI's advisory names only pfSense CE 2.7.2 and CE 2.8.0 and references a public proof of concept ([BSI WID-SEC-W-2026-1435](https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-1435.json)).

**Exposure:** pfSense CE 2.7.2 (CVE-2025-69690) and CE 2.8.0 (CVE-2025-69691) ([BSI WID-SEC-W-2026-1435](https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-1435.json)), for anyone who can log in as administrator; the researcher notes the XMLRPC endpoint is enabled by default over HTTPS with Basic Authentication and that default administrator credentials are widely deployed ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16)).

**Detection:** firewall web and XMLRPC access logs: calls to the pfsense.exec_php method and configuration restores nobody scheduled, both made with administrator credentials ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16)).

**Defender takeaway:** no patch is coming, so the decision is about the precondition: replace default administrator credentials and keep the management interface and XMLRPC off networks an attacker can reach; with that in place the flaws give nothing beyond what an administrator can already do, which is the supplier's position ([EUVD-2025-209739](https://euvd.enisa.europa.eu/vulnerability/EUVD-2025-209739)).

## Correction — 2026-10-21T20:35:05Z

BSI's advisory states only that an attacker can exploit the flaws to run arbitrary code with administrator rights, rates them critical and names pfSense CE 2.7.2 and CE 2.8.0 ([BSI WID-SEC-W-2026-1435](https://wid.cert-bund.de/.well-known/csaf/white/2026/wid-sec-w-2026-1435.json)); it carries no patch status and no mitigation, so it does not mark the CE build as unpatched or recommend a mitigation. CVE-2025-69691 needs an authenticated administrator, not any Basic Auth credentials; the researcher adds that the endpoint is enabled by default and default administrator credentials are widely deployed ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16)). ENISA's EUVD scores CVE-2025-69690 at 9.1, against the researcher's 8.8 ([EUVD-2025-209738](https://euvd.enisa.europa.eu/vulnerability/EUVD-2025-209738)). Netgate's refusal to patch is reported by the researcher ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16)), the CVE records mark both flaws as disputed by the supplier because the functions are admin-only ([EUVD-2025-209739](https://euvd.enisa.europa.eu/vulnerability/EUVD-2025-209739)), and no cited source says whether pfSense Plus is affected. The researcher's post gives no file to audit for persistence, so the check is the firewall's own access logs for pfsense.exec_php calls and unplanned configuration restores ([Full Disclosure, 2026-02-16](https://seclists.org/fulldisclosure/2026/Feb/16)).
