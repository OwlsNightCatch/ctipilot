---
schema: 1
kind: vulnerability
horizon: strategic
weekly_section: weekly-vuln-rollup
title: "2026-W32 vulnerability status roll-up — seven CVEs and one unnumbered zero-day stood at confirmed exploitation, five of them newly catalogued this week, against a critical tail concentrated on management planes and on products whose vendors have stopped shipping fixes"
headline: "W32 CVE trajectory — five new KEV listings, two exploited flaws with no catalogue entry, and five products with no fix coming"
summary: >
  Consolidated status of the vulnerabilities this pipeline covered operationally in ISO week 2026-W32, each
  with its trajectory this week set against when it was first covered. Newly confirmed exploited or newly
  KEV-listed: CVE-2026-18556 and CVE-2026-18577 (N-able N-central), CVE-2026-34486 (Apache Tomcat),
  CVE-2026-9198 (IBM Langflow), CVE-2026-63077 (JetBrains TeamCity) and CVE-2026-8037 (Progress Kemp
  LoadMaster). Exploited without a catalogue entry: CVE-2026-71851 (crypto-js) and the unnumbered Metabase
  SQL-injection zero-day. The critical tail is dominated by management planes — Cisco Secure FMC at CVSS 10.0,
  Check Point Security Management, WALLIX Bastion, Veeam ONE — and by five products where no fix exists or
  none is coming. Full per-flaw detail lives in the referenced operational entries.
discovered_at: "2026-08-09T23:45:00Z"
event_date: "2026-08-07"
run_id: 2026-08-09T2315Z-weekly
priority: high
immediate_action: null
tags: [vulnerabilities, actively-exploited, cisa-kev, pre-auth, no-patch, rce, auth-bypass]
regions: [global, europe]
sectors: [public-sector, technology, finance]
entities: []
techniques: [T1190, T1210, T1072, T1078.001]
affected_products:
  - "N-able N-central"
  - "Apache Tomcat"
  - "IBM Langflow"
  - "JetBrains TeamCity"
  - "Progress Kemp LoadMaster"
  - "Cisco Secure Firewall Management Center"
  - "Check Point Security Management Server"
  - "Veeam ONE"
  - "Adobe Campaign Classic"
  - "Red Hat Build of Keycloak"
cves: []
sources:
  - url: "https://www.cisa.gov/news-events/alerts/2026/08/04/cisa-adds-three-known-exploited-vulnerabilities-catalog"
    publisher: "CISA"
    date: "2026-08-04"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/08/05/cisa-adds-one-known-exploited-vulnerability-catalog"
    publisher: "CISA"
    date: "2026-08-05"
    role: primary
  - url: "https://www.cisa.gov/news-events/alerts/2026/08/07/cisa-adds-one-known-exploited-vulnerability-catalog"
    publisher: "CISA"
    date: "2026-08-07"
    role: primary
  - url: "https://status.n-able.com/2026/08/06/n-central-2026-3-hotfix-2-additional-mitigation-for-cve-2026-18577/"
    publisher: "N-able"
    date: "2026-08-06"
    role: primary
  - url: "https://github.com/advisories/GHSA-rg76-677x-56q9"
    publisher: "GitHub Advisory Database"
    date: "2026-08-07"
    role: primary
  - url: "https://www.coinspect.com/blog/ill-bloom-investigation/"
    publisher: "Coinspect Security"
    date: "2026-08-05"
    role: primary
  - url: "https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2"
    publisher: "Cisco PSIRT"
    date: "2026-08-05"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/framework-tally-disclose-metabase-data-theft-attacks/"
    publisher: "BleepingComputer"
    date: "2026-08-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "based on evidence of active exploitation"
    publisher: "CISA"
  - quote: "The vulnerability had existed for more than a decade, making it difficult to determine how widely the vulnerable implementation had spread, and attackers were already exploiting it while our investigation was underway."
    publisher: "Coinspect Security"
  - quote: "This is not a duplicate of our previous communication — Hotfix 2 is required, even if you already applied the earlier hotfix. Hotfix 2 supersedes Hotfix 1 with additional hardening measures to further protect you and your customers."
    publisher: "N-able"
verification: multi-source
sourcing_note: >
  Per-CVE status below is transcribed from each flaw's own owning advisory as recorded in the referenced
  operational entries, never from a roundup; the full per-flaw records (CVSS, vector, affected and fixed
  versions) live in those entries, which is why this roll-up carries no cves[] of its own and states the
  trajectory instead. Check Point publishes no CVSS for CVE-2026-18574 and none is asserted here; the
  WALLIX Bastion authentication bypass and the Metabase zero-day carry no CVE identifier at all.
confidence: high
update_of: null
references:
  - 2026-08-03/cve-2026-18577-n-able-n-central-auth-bypass-exploited
  - 2026-08-05/n-able-n-central-post-exploitation-rmm-tunnel-driver
  - 2026-08-09/n-able-n-central-hotfix-2-required-supersedes-hotfix-1
  - 2026-08-05/cve-2026-34486-tomcat-encryptinterceptor-fail-open-kev
  - 2026-08-05/cve-2026-9198-langflow-auto-login-validate-code-kev
  - 2026-08-06/cve-2026-63077-teamcity-kev-confirmed-exploited
  - 2026-08-08/cve-2026-8037-kemp-loadmaster-kev-confirmed-exploitation
  - 2026-08-09/cryptojs-cve-2026-71851-weak-entropy-exploited
  - 2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally
  - 2026-08-04/cve-2026-20079-cisco-secure-fmc-auth-bypass-root-hotfix
  - 2026-08-05/check-point-cve-2026-18574-management-auth-bypass
  - 2026-08-09/wallix-bastion-rest-api-unauth-admin-cvss10
  - 2026-08-06/veeam-service-provider-console-veeam-one-ten-cves
  - 2026-08-07/adobe-campaign-classic-apsb26-120-second-wave-unauth-rce
  - 2026-08-07/keycloak-saml-broker-signature-bypass-cve-2026-16443
  - 2026-08-08/zapscape-cve-2026-64561-kvm-shadow-mmu-second-vm-escape
  - 2026-08-06/endlessdoors-zbtlink-router-factory-shipped-root-backdoor
  - 2026-08-08/cpdlc-atn-b1-five-protocol-flaws-no-mitigation-available
  - 2026-08-09/thermo-fisher-genetic-analyzer-correction-patch-exists
  - 2026-08-03/gladinet-centrestack-hardcoded-key-token-forgery
  - 2026-08-08/flowise-three-cves-vendor-sunset-no-fix-coming
  - 2026-08-09/teamdavid-tobit-22-cves-unauth-mailbox-takeover-dach
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

This roll-up carries only each vulnerability's trajectory across ISO week 2026-W32; the mechanics, exploitation detail and defender guidance live in the referenced operational entries.

**Crossed into confirmed exploitation this week.** CISA added three flaws to its Known Exploited Vulnerabilities catalogue on 4 August — the N-able N-central authentication bypass CVE-2026-18556, the Apache Tomcat EncryptInterceptor bypass CVE-2026-34486 and the IBM Langflow code-injection path CVE-2026-9198 ([CISA, 2026-08-04](https://www.cisa.gov/news-events/alerts/2026/08/04/cisa-adds-three-known-exploited-vulnerabilities-catalog)) — followed by the JetBrains TeamCity deserialization flaw CVE-2026-63077 on 5 August ([CISA, 2026-08-05](https://www.cisa.gov/news-events/alerts/2026/08/05/cisa-adds-one-known-exploited-vulnerability-catalog)) and the Progress Kemp LoadMaster command injection CVE-2026-8037 on 7 August ([CISA, 2026-08-07](https://www.cisa.gov/news-events/alerts/2026/08/07/cisa-adds-one-known-exploited-vulnerability-catalog)). Three of those five are status changes on ground this pipeline had already covered as unexploited: TeamCity was patch-available on 29 July with JetBrains recording no known exploitation, LoadMaster's only observed activity on 2 July was attempts eSentire reported as unsuccessful, and the Tomcat listing arrived months after the exploitation itself. Each of the three therefore converts an upgrade task into a compromise-assessment task for any instance that was internet-reachable during its window. The Langflow listing is the third confirmed-exploited pre-authentication path in that one product inside three weeks, which turns the question from patching a CVE into removing the product's internet exposure.

**Exploited without a catalogue entry.** Two of the week's confirmed-exploited flaws are invisible to a KEV-driven process. Coinspect traced an active wallet-drain campaign to a weak pseudo-random generator, stating that "attackers were already exploiting it while our investigation was underway" ([Coinspect Security, 2026-08-05](https://www.coinspect.com/blog/ill-bloom-investigation/)); the advisory record identifies the affected code as crypto-js before 4.0.0 under CVE-2026-71851 ([GitHub Advisory Database, 2026-08-07](https://github.com/advisories/GHSA-rg76-677x-56q9)). The identifier exists but the flaw is not catalogued as exploited, and the scope rule is what makes it broad — any application that used the function to produce a key, token, session identifier or reset code inherits the weakness, and no upgrade repairs a secret already generated. The Metabase SQL-injection zero-day has no CVE identifier at all, and two customers — the laptop maker Framework and the form builder Tally — have confirmed data was taken from their instances on 3 August ([BleepingComputer, 2026-08-07](https://www.bleepingcomputer.com/news/security/framework-tally-disclose-metabase-data-theft-attacks/)).

**The critical tail: management planes, and vendors who have stopped.** The unexploited-but-severe set concentrates on the planes that administer everything else — Cisco Secure Firewall Management Center at CVSS 10.0, unpatched for five months before per-train hot fixes arrived, with an accompanying compromise check the vendor has repeatedly revised — the advisory stood at version 2.4, last updated 5 August, when checked at the close of the week ([Cisco PSIRT, 2026-08-05](https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-onprem-fmc-authbypass-5JPp45V2)); Check Point Security Management, taking its fourth CVE on that surface in roughly two weeks and its second authentication bypass, with seven end-of-support trains listed as affected and no fix on offer; WALLIX Bastion, whose REST API hands full product-administrator control of a privileged-access vault to an unauthenticated caller at CVSS 4.0 base 10.0, with the reporting researchers stating they intend to publish full technical details in September 2026; and Veeam ONE's CVE-2026-64633, an unauthenticated CVSS 10.0 remote code execution on the agent host, sitting over the backup estate ransomware operators attack before they encrypt. Alongside them, five products have no fix to apply and will not get one: the Zbtlink routers shipping a factory-installed root backdoor whose remedy is replacement, the CPDLC air-traffic data link whose flaws are properties of the standard, Flowise's three new CVEs landing days after its vendor announced a wind-down, Tobit TeamDavid's 22 CVEs naming no fixed release against roughly 12,000 internet-facing instances, and Check Point's end-of-support trains.

### Status table

Trajectory only — affected and fixed versions, CVSS and exploitation mechanics live in each referenced entry.

| CVE | Product | Status at close of 2026-W32 | Change this week |
|---|---|---|---|
| CVE-2026-18556 | N-able N-central | exploited · KEV | KEV-listed 2026-08-04; the fix build named at first coverage was superseded on 2026-08-06 |
| CVE-2026-18577 | N-able N-central | exploited | the alternative path N-able's earlier fix did not mitigate; Hotfix 2 required even where Hotfix 1 was applied |
| CVE-2026-34486 | Apache Tomcat | exploited · KEV | KEV-listed 2026-08-04, months after the observed exploitation |
| CVE-2026-9198 | IBM Langflow | exploited · KEV | KEV-listed 2026-08-04 — third confirmed-exploited pre-auth path in this product in three weeks |
| CVE-2026-63077 | JetBrains TeamCity | exploited · KEV | KEV-listed 2026-08-05; was patch-available with no known exploitation at first coverage on 2026-07-29 |
| CVE-2026-8037 | Progress Kemp LoadMaster | exploited · KEV · public PoC | KEV-listed 2026-08-07; first covered 2026-07-02 when observed attempts were reported unsuccessful |
| CVE-2026-71851 | crypto-js | exploited, not catalogued | exploitation confirmed during the discloser's own investigation; no upgrade repairs a secret already generated |
| *(no CVE assigned)* | Metabase | exploited, not catalogued | unauthenticated SQL-injection zero-day, exploited from 2026-08-03; two customers confirmed data theft |
| CVE-2026-20079 | Cisco Secure FMC | patch available | per-train hot fixes after five months unpatched; the advisory carrying the compromise check stood at version 2.4, last updated 2026-08-05 |
| CVE-2026-18574 | Check Point Security Management | patch available · no patch for EoS trains | fourth CVE on this management surface in roughly two weeks; seven end-of-support trains affected with no fix |
| *(no CVE assigned)* | WALLIX Bastion | patch available | CVSS 4.0 base 10.0 unauthenticated administrative takeover; full technical details due September 2026 |
| CVE-2026-64633 | Veeam ONE | patch available | unauthenticated CVSS 10.0 code execution on the agent host, one of ten flaws across the backup management and monitoring planes |
| CVE-2026-48331 | Adobe Campaign Classic | patch available | one of three unauthenticated CVSS 10.0 paths whose affected build is the release shipped five days earlier as the previous fix |
| CVE-2026-16443 | Keycloak | patch available | SAML response signature validation silently disabled on a metadata-import edge case |
| CVE-2026-64561 | Linux KVM | public PoC · patch available | second guest-to-host escape in the shadow MMU; Belgium's CCB rates it patch-immediately |
| CVE-2026-66747 | Zbtlink routers | no patch | factory-shipped root backdoor; the discloser's remedy is device replacement and it did not notify the vendor |
| CVE-2025-71409 | CPDLC over ATN-B1 | no patch | a property of the standard; CISA records remediation as none-available |
| CVE-2026-17583 | Applied Biosystems analyzers | patch available | **corrected upward** — patched software exists for five product lines; this pipeline's first coverage wrongly reported none |

**Corrected this week.** The Thermo Fisher genetic-analyzer integrity flaw CVE-2026-17583 was reported here on 5 August as having no vendor fix; the cited advisory in fact names patched software for five product lines, with only three end-of-life instrument families left without an update. Separately, a July weekly's claim that ten CVEs across four product classes were all KEV-listed was wrong for two of them — the Progress ShareFile chain CVE-2026-2699 and CVE-2026-2701 have never been added. Both corrections shipped as their own entries and are reflected in the records above.
