# Prior-iteration deltas (iteration 3 NEEDS_FIXES → iteration 4 post-fix pass)

| finding | entry | remediation applied | verify in this iteration |
|---|---|---|---|
| F4 CVE-2019-6693 "no fix release" | k0t-fortiweb-fortigate-globalprotect-edge-device-campaign | fixed now states FortiOS 5.6.11, 6.0.7 and 6.2.1 and later add private-data-encryption (disabled by default); affected carries Fortinet's list; FG-IR-19-007 added to sources[] and cited in Exposure | against FG-IR-19-007 (bodies/fg-19-007.txt) |
| F8/F11 k0t CVE-2025-64446 and CVE-2026-0257 records | same | affected/fixed filled from FG-IR-25-910 (FortiWeb table, workaround, post-upgrade review) and Palo Alto's CVE-2026-0257 advisory (CVSS-B 7.8, per-branch fixed builds, Prisma Access); "cited sources" wording gone; three vendor sources added and cited in Exposure/Detection; body kept within the word limit by cutting the 70,000-credentials sentence, the forged-header parenthetical, the lockout back-off clause and the victim-geography clause | CVE records against the three pages; cvss for CVE-2025-64446 stays null (the Fortinet page carries none) |
| F11 k0t techniques | same | ten Group-IB-mapped ids added (T1110.003, T1550.002, T1059.001, T1018, T1046, T1135, T1069.002, T1083, T1518.001, T1078.003) | ids active; present in Group-IB's table |
| F4 Cisco "persistent cluster cookies" | cve-2026-76466-cisco-expressway-cluster-unauth-root-rce | summary says "persistent cookies" | wording |
| F3 Cisco takeaway citations | same | the Unified CM and Snort 3 advisories added to the clause | citation |
| F11 Cisco "bar" / "Three hardening releases" | same | "two further hardening releases whose worst classes are exploitable over the network without authentication"; summary says "Hardening releases ship the same day for ..." | wording |
| F11 Cisco affected_products IOS XE spelling | same | "Cisco IOS XE Software" (existing alias of product:cisco-ios-xe, so no new registry key) | sync_products --check ok |
| F3 PHP CVSS cite | php-critical-release-pre-announced-cve-2026-109618-109619 | the 2026-10-20-1 php.net item added to the clause | citation |
| F14 + F11 ARTEX | artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse | "another actor"; stray "(" removed; affected_products uses "Okta"; the duplicate registry key product:okta-workforce-identity removed (created this run, never published) | single Okta key; link renders |
| F11 pipeline wording | pan-os-..., cve-2026-110264-... | "Palo Alto does not say which logs record request bodies"; "GitLab and its detection pages report no public proof of concept" | wording |
| F11 Publica relay attribution | publica-pk-softech-supplier-malware-intrusion-data-outflow | summary splits it: Tamedia (100 GB, ransom; Inside IT relays), authorities' assumed scope (Netzwoche relays) | attribution against the three pages |

Declined: PAN-OS references[] entry for the CVE-2026-0257 entry (low confidence; kept because the product entity overlaps and the dedup gate would otherwise WARN; the 0322 reference stays too); watchTowr FAQ label date (low confidence; rolling page, observation dated 2026-10-21 in its text); OVH envchecker folder and extension name (advisory, declined in iterations 1 to 3, the verifier calls leaving it defensible).
