---
schema: 1
kind: vulnerability
horizon: strategic
weekly_section: weekly-vuln-rollup
title: "2026-W31 vulnerability status roll-up — twelve CVEs stood at confirmed exploitation, three carry public exploit chains, and a dense critical tail hit management planes, OT, ERP and the AI toolchain"
headline: "W31 CVE trajectory — twelve exploited/KEV, three with public chains, and a critical tail with no fix on five"
summary: >
  Consolidated status of the CVEs this pipeline covered operationally in ISO week 2026-W31, each with its
  trajectory this week set against when it was first covered. Newly exploited or newly KEV-listed this week:
  CVE-2026-16812 (Arista VeloCloud Orchestrator, CVSS 10.0, KEV the day of disclosure), CVE-2025-68686
  (FortiOS SSL-VPN patch bypass), CVE-2026-20316 (Cisco Secure FMC static credential), CVE-2026-16723
  (fastjson 1.x, no patch exists) and CVE-2026-65884 / CVE-2026-65885 (Balbooa Gridbox, 92 planted admin
  accounts observed). Already-exploited items that moved: CVE-2026-16232 gained a published root cause,
  CVE-2026-12569 entered a mass extortion-email phase, CVE-2026-42897 gained a state attribution,
  CVE-2013-4786 gained evidence of in-the-wild abuse, and CVE-2026-39987 was corrected upward to confirmed
  command execution on 11 endpoints. Full per-CVE detail lives in the referenced operational entries; this
  roll-up carries only the week's trajectory.
discovered_at: "2026-08-02T23:54:00Z"
event_date: "2026-07-30"
run_id: 2026-08-02T2311Z-weekly
priority: high
immediate_action: null
tags: [vulnerabilities, actively-exploited, cisa-kev, pre-auth, rce, auth-bypass, no-patch, poc-public, patch-available, ot-ics]
regions: [global, europe]
sectors: [technology, public-sector, energy, water, manufacturing, finance]
entities: []
techniques: [T1190, T1078.001, T1606, T1136.001, T1505.003, T1068, T1211, T1542.001]
affected_products: ["Arista VeloCloud Orchestrator", "Fortinet FortiOS", "Cisco Secure Firewall Management Center", "Check Point Security Management", "Alibaba fastjson", "Langflow", "Balbooa Gridbox for Joomla", "PTC Windchill", "Microsoft Exchange Server", "Citrix NetScaler ADC", "marimo", "JetBrains TeamCity", "VMware vCenter Server", "IBM WebSphere Application Server", "Adobe Campaign Classic", "Phoenix Contact CHARX SEC-3000", "Siemens Desigo CC", "Ruby on Rails Active Storage"]
cves: []
sources:
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/27/cisa-adds-two-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-07-27"
    role: primary
  - url: "https://www.arista.com/en/support/advisories-notices/security-advisory/24364-security-advisory-0144"
    publisher: "Arista Networks (Security Advisory 0144)"
    date: "2026-07-27"
    role: primary
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh"
    publisher: "Cisco PSIRT"
    date: "2026-07-29"
    role: primary
  - url: "https://www.vulncheck.com/blog/state-of-exploitation-1h-2026"
    publisher: "VulnCheck"
    date: "2026-07-28"
    role: primary
  - url: "https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/"
    publisher: "mySites.guru"
    date: "2026-07-29"
    role: primary
  - url: "https://ransom-isac.org/blog/clop-windchill-flexplm-exploitation/"
    publisher: "Ransom-ISAC / eCrime.ch / DEFUSED"
    date: "2026-07-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This issue was discovered externally and is known to be actively exploited."
    publisher: "Arista Networks (Security Advisory 0144)"
  - quote: "In July 2026, the Cisco PSIRT became aware of active exploitation of this vulnerability."
    publisher: "Cisco PSIRT"
  - quote: "With LangFlow, we've seen attackers gain initial access using exploits targeting both CVE-2026-0769 and CVE-2026-5027, harvest credentials, likely for services such as OpenAI and Claude, deploy cryptominers, and attempt lateral movement. Neither of these vulnerabilities have been added to CISA KEV."
    publisher: "VulnCheck"
  - quote: "We have the server access logs showing the exploitation requests arriving, and connected sites where the accounts are already planted. On one connected Joomla site our rogue admin check is holding 92 planted accounts right now"
    publisher: "mySites.guru"
verification: multi-source
sourcing_note: >
  Each status claim is attributed to the party that states it, never to the roll-up as a whole. CISA's
  2026-07-27 alert is cited only for the two KEV additions it carries (CVE-2026-16812 and CVE-2025-68686).
  Where an operational entry recorded a KEV listing this synthesis did not itself re-source — the Cisco Secure
  FMC and Check Point additions among them — the exploitation status is carried from the vendor or research
  statement instead, and the KEV claim is left to the referenced entry that sourced it. CVSS values are the
  scores recorded in each referenced entry from the authority that owns the identifier; the Gridbox and
  SP Page Builder figures are the Joomla CNA's CVSS 4.0 scores, and no CVSS is published for CVE-2026-59243.
  Per-CVE metadata is deliberately NOT duplicated into this entry's cves[]: the identifiers, scores, affected
  and fixed versions live on the operational entries that first covered them, which own that surface for the
  dedup index, the per-CVE pages and automated triage matching. This roll-up carries trajectory in its body.
confidence: high
update_of: null
references:
  - 2026-07-28/cve-2026-16812-arista-velocloud-orchestrator-exploited
  - 2026-07-28/cve-2025-68686-fortios-ssl-vpn-symlink-persistence-kev
  - 2026-07-30/cisco-secure-fmc-cve-2026-20316-static-credential-exploited
  - 2026-07-27/cve-2026-16723-fastjson-1x-spring-boot-fat-jar-rce-no-patch
  - 2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave
  - 2026-07-23/check-point-smartconsole-auth-bypass-cve-2026-16232
  - 2026-06-20/ptc-windchill-cve-2026-12569-unauthenticated-java-deserializ
  - 2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen
  - 2026-07-30/cve-2013-4786-exposed-bmc-ipmi-rakp-hash-disclosure
  - 2026-07-31/unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055
  - 2026-07-28/cve-2026-61511-vbulletin-preauth-rce-public-exploit
  - 2026-07-31/cve-2026-66066-rails-activestorage-libvips-file-read
  - 2026-07-30/rufroot-cve-2026-59726-ruflo-mcp-bridge-unauth-rce
  - 2026-07-29/cve-2026-0769-langflow-preauth-eval-rce-exploited-not-in-kev
  - 2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce
  - 2026-07-30/vmware-vmsa-2026-0006-vcenter-auth-bypass-vmxnet3-escape
  - 2026-07-29/cve-2026-59243-airflow-fab-azure-ad-jwt-signature-bypass
  - 2026-07-29/cve-2025-15467-siemens-desigo-cc-cms-overflow-v7-unfixed
  - 2026-08-01/ibm-websphere-cve-2026-14512-14446-preauth-no-fix-pack
  - 2026-08-01/solarwinds-web-help-desk-cve-2026-28323-saml-auth-bypass
  - 2026-08-02/adobe-campaign-classic-apsb26-114-cvss10-unauth-rce
  - 2026-08-02/phoenix-contact-charx-sec-3xxx-unauth-root-no-firmware-yet
  - 2026-08-01/aimy-captcha-joomla-cve-2026-65883-object-injection-rce
  - 2026-08-02/sp-page-builder-cve-2026-65766-preauth-sqli-mail-relay
  - 2026-07-30/hashicorp-terraform-mcp-server-hcsec-2026-23-token-exfil
  - 2026-07-21/hugging-face-autonomous-ai-agent-production-breach
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

**Confirmed exploited or newly KEV-listed this week.** Five items crossed into confirmed exploitation for the first time. Arista's on-prem VeloCloud Orchestrator flaw CVE-2026-16812 arrived already exploited — "this issue was discovered externally and is known to be actively exploited" ([Arista Networks, 2026-07-27](https://www.arista.com/en/support/advisories-notices/security-advisory/24364-security-advisory-0144)) — and was KEV-listed the same day alongside FortiOS CVE-2025-68686 ([CISA, 2026-07-27](https://www.cisa.gov/news-events/alerts/2026/07/27/cisa-adds-two-known-exploited-vulnerabilities-catalog)). Cisco Secure FMC CVE-2026-20316 followed two days later, with Cisco stating that "in July 2026, the Cisco PSIRT became aware of active exploitation of this vulnerability" ([Cisco PSIRT, 2026-07-29](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-fmc-static-cred-BET3Cjh)). The Balbooa Gridbox pair CVE-2026-65884 and CVE-2026-65885 are the week's only items with server-log-level exploitation evidence: "we have the server access logs showing the exploitation requests arriving, and connected sites where the accounts are already planted. On one connected Joomla site our rogue admin check is holding 92 planted accounts right now" ([mySites.guru, 2026-07-29](https://mysites.guru/blog/gridbox-23-critical-vulnerabilities/)). And fastjson CVE-2026-16723 is exploited with no patch that can ever arrive on the 1.x line.

**Already-exploited items whose status moved.** Five CVEs the store already carried as exploited changed in ways that alter defender work rather than merely accumulating coverage. CVE-2026-16232 (Check Point Security Management) gained a published root cause and a confirmed default-configuration precondition. CVE-2026-12569 (PTC Windchill / FlexPLM) moved from exploitation into a mass extortion-email phase, with the significant detail that "as of 22 July, Cl0p ransomware has not begun listing victims of this latest campaign on their dark web data leak site or has publicly claimed credit for this latest campaign" ([Ransom-ISAC, 2026-07-22](https://ransom-isac.org/blog/clop-windchill-flexplm-exploitation/)) — placing affected organisations between exfiltration and publication. CVE-2026-42897 (Exchange OWA), KEV-listed back in May, gained a state-actor attribution and a named browser-resident implant. CVE-2013-4786 moved from a known design weakness to documented in-the-wild abuse of server management planes. And CVE-2026-39987 (marimo) was corrected upward: this pipeline's own 2026-08-02 correction records Unit 42 confirming command execution on 11 notebook endpoints, not merely attempted, which the earlier entry had omitted.

**Public exploit chain or full mechanics, no confirmed in-the-wild abuse.** Three items are a disclosure away from exploitation rather than a discovery away. CVE-2026-61511 (vBulletin) had working exploit code published four weeks after the patch. CVE-2026-66066 (Rails Active Storage) lost its embargo four weeks early because researchers reconstructed the chain independently, and Rails shipped forensic tooling in the same move. CVE-2026-59726 (Ruflo, CVSS 10.0) had the single unauthenticated request that reaches code execution published with the advisory, and its poisoned agent-memory effect survives a patched redeploy.

**Exploited but absent from KEV.** CVE-2026-0769 (Langflow) sits in a category of its own this week and is the reason a KEV-only process was insufficient: VulnCheck reports observed exploitation and states plainly that "neither of these vulnerabilities have been added to CISA KEV" ([VulnCheck, 2026-07-28](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026)), while ZDI documents no fixed version at all.

**Critical-but-unexploited tail requiring scheduled action.** JetBrains TeamCity On-Premises CVE-2026-63077 (CVSS 9.8, every on-prem version ever shipped). VMware VMSA-2026-0006 — CVE-2026-59309 and CVE-2026-59310 both CVSS 9.8 and pre-authentication against vCenter, plus the VMXNET3 guest-to-host escape CVE-2026-47876, with no workaround for any of the five. Apache Airflow's FAB provider CVE-2026-59243, where no party has published a CVSS. Siemens Desigo CC CVE-2025-15467 with the V7 family unfixable, alongside Mendix Runtime CVE-2026-7891. IBM WebSphere CVE-2026-14512, CVE-2026-14446 and CVE-2026-14528, on interim APARs until fix packs targeted for 3Q2026. SolarWinds Web Help Desk CVE-2026-28323 and CVE-2026-28299. Adobe Campaign Classic CVE-2026-48449 (CVSS 10.0 unauthenticated code execution) and CVE-2026-48448, affecting on-premise and hybrid deployments only. Phoenix Contact CHARX SEC-3xxx, twenty CVEs with firmware 1.9.1 unreleased at disclosure. The Joomla extension batch CVE-2026-65883, CVE-2026-65766, CVE-2026-65879, CVE-2026-65877, CVE-2026-65878 and CVE-2026-65876. HashiCorp terraform-mcp-server CVE-2026-14869, CVE-2026-16496 and CVE-2026-16498. And nine JFrog Artifactory Self-Managed CVEs whose chained critical scenario depends on Anonymous Access being enabled.
