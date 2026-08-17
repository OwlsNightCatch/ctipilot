---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "UPDATE — water-sector PLC lockout status: an OT vendor's decade retrospective attributes the Minnesota controller intrusions to a CVE whose own record names a different Rockwell product family, and the campaign still has no CVE and no actor named by any investigating body"
headline: "Water campaign status — the first vendor CVE attribution appeared this week, and it does not match the CVE's own affected-product list"
summary: >
  Status update on the US water-sector PLC lockout campaign a prior weekly consolidated for its European
  exposure. The in-window delta is a sourcing problem rather than a technical one. Dragos published a
  decade-spanning retrospective on 13 August comparing the 2013 Bowman Dam intrusion to the July 2026
  Minnesota campaign, and states the Minnesota controllers were exploitable through a known authentication
  bypass vulnerability, CVE-2021-22681, added to CISA's catalogue in March 2026. The catalogue date checks
  out. The product scope does not: CISA's own ICS advisory for that CVE is titled "Rockwell Automation Logix
  Controllers", describes Studio 5000 Logix Designer using a key to verify Logix controllers, and lists the
  affected products as RSLogix 5000 versions 16 through 20, Studio 5000 Logix Designer version 21 and later,
  and FactoryTalk Security — while the controllers Dragos itself names in the same piece, and that the FBI
  and EPA identified, are MicroLogix 1100 and 1400. No
  investigating body has named a CVE or an actor for these intrusions; the published technique remains
  reachability plus credential control, involving no vulnerability at all.
discovered_at: "2026-08-16T23:59:00Z"
event_date: "2026-08-13"
run_id: 2026-08-16T2315Z-weekly
priority: notable
immediate_action: null
tags: [ot-ics, vulnerabilities, cisa-kev]
regions: [europe, global]
sectors: [water, energy, public-sector]
entities:
  - incident:minnesota-water-utilities-coordinated-cyberattack-2026-07
techniques: [T1078.001, T1133, T1190]
affected_products: ["Rockwell Automation Allen-Bradley MicroLogix 1100", "Rockwell Automation Allen-Bradley MicroLogix 1400", "Rockwell Automation Studio 5000 Logix Designer"]
cves:
  - id: CVE-2021-22681
    cvss: 10.0
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [cisa-kev, no-patch, mitigation-only]
    affected: "Per CISA advisory ICSA-21-056-03: RSLogix 5000 versions 16 through 20, Studio 5000 Logix Designer version 21 and later, and FactoryTalk Security v2.10 and later — the advisory is titled Rockwell Automation Logix Controllers"
    fixed: "No fixed version. CISA records that Rockwell Automation has determined this vulnerability cannot be mitigated with a patch; every remediation in the advisory is a mitigation."
sources:
  - url: "https://www.dragos.com/blog/water-utility-attacks-decade-of-gaps"
    publisher: "Dragos"
    date: "2026-08-13"
    role: primary
  - url: "https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2021/icsa-21-056-03.json"
    publisher: "CISA — ICS advisory ICSA-21-056-03 (CSAF)"
    date: "2021-02-25"
    role: primary
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA Known Exploited Vulnerabilities catalog"
    date: "2026-08-16"
    role: primary
closed_sources: []
evidence:
  - quote: "In Minnesota, it was dozens of PLCs reachable over cellular links, exploitable through a known authentication bypass vulnerability, (CVE-2021-22681) that was first disclosed in 2021 and added to CISA’s Known Exploited Vulnerabilities catalog in March 2026, five years after initial disclosure."
    publisher: "Dragos"
  - quote: "Attackers reached MicroLogix 1100 and 1400 series programmable logic controllers that were directly exposed to the internet through cellular links at water towers and lift stations."
    publisher: "Dragos"
  - quote: "Studio 5000 Logix Designer uses a key to verify Logix controllers are communicating with the affected Rockwell Automation products."
    publisher: "CISA — ICS advisory ICSA-21-056-03"
  - quote: "Successful exploitation of this vulnerability could allow a remote unauthenticated attacker to bypass the verification mechanism and connect with Logix controllers."
    publisher: "CISA — ICS advisory ICSA-21-056-03"
verification: contradicted
sourcing_note: >
  This entry reports a discrepancy rather than resolving it. Dragos's retrospective is the source for the
  CVE attribution; CISA's own ICS advisory for that CVE and the CISA catalogue entry, both fetched
  this run, are the sources for the CVE's own affected-product scope and its catalogue date. The catalogue
  date Dragos gives is correct — CISA added CVE-2021-22681 on 2026-03-05. The product mismatch is stated
  from the primary records and is not an assessment of what happened in Minnesota, which no cited source
  establishes; Dragos has not been asked for comment and may hold information not in the published piece.
  A separate MicroLogix-relevant flaw this pipeline recorded on 10 August, CVE-2017-16740, is not in the
  KEV catalogue and no source claims it was exploited either. Two further discrepancies between the two
  cited sources are stated in the body rather than resolved: the CVSS score (Dragos 9.8, CISA 10.0) and the
  existence of a patch (CISA records that Rockwell determined the flaw cannot be mitigated with one).
confidence: medium
update_of: 2026-08-09/weekly-w32-water-plc-lockout-status
references:
  - 2026-08-10/forescout-rockwell-plc-exposure-census-cellular-carrier-path
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-08-09):** the prior weekly recorded the water-sector PLC lockout campaign in a state that had held since it began — a device family European operators could inventory, an operational effect on real utilities, and an attribution that no US authority would make. This week produced the campaign's first vendor attribution to a specific vulnerability, and it does not survive a check against that vulnerability's own record.

Dragos published a decade-spanning retrospective on 13 August setting the 2013 Bowman Dam intrusion against the July 2026 Minnesota campaign. Its description of the target is consistent with everything published before: "Attackers reached MicroLogix 1100 and 1400 series programmable logic controllers that were directly exposed to the internet through cellular links at water towers and lift stations." The new claim is the mechanism: "In Minnesota, it was dozens of PLCs reachable over cellular links, exploitable through a known authentication bypass vulnerability, (CVE-2021-22681) that was first disclosed in 2021 and added to CISA's Known Exploited Vulnerabilities catalog in March 2026, five years after initial disclosure" ([Dragos, 2026-08-13](https://www.dragos.com/blog/water-utility-attacks-decade-of-gaps)). Half of that checks out: CISA added CVE-2021-22681 to the catalogue on 5 March 2026 ([CISA Known Exploited Vulnerabilities catalog, 2026-08-16](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)).

The product scope does not. CISA's own ICS advisory for that CVE is titled "Rockwell Automation Logix Controllers", and states that "Studio 5000 Logix Designer uses a key to verify Logix controllers are communicating with the affected Rockwell Automation products", with successful exploitation allowing "a remote unauthenticated attacker to bypass the verification mechanism and connect with Logix controllers". The products it lists as affected are RSLogix 5000 versions 16 through 20, Studio 5000 Logix Designer version 21 and later, and FactoryTalk Security version 2.10 and later ([CISA ICS advisory ICSA-21-056-03, 2021-02-25](https://raw.githubusercontent.com/cisagov/CSAF/develop/csaf_files/OT/white/2021/icsa-21-056-03.json)). MicroLogix appears nowhere in it, and the flaw concerns a key used by Rockwell's Logix engineering software to verify Logix controllers — a different product line and a different mechanism from the MicroLogix 1100 and 1400 units Dragos names two paragraphs earlier. CISA's catalogue summary frames it the same way, around Studio 5000 Logix Designer and Logix controllers. The same advisory records a second divergence from Dragos's account that is worth stating given this entry's subject: Dragos gives the flaw a CVSS score of 9.8, while CISA's advisory reads "A CVSS v3 base score of 10.0 has been calculated". This entry carries CISA's 10.0, and notes that the advisory also records that Rockwell "has determined this vulnerability cannot be mitigated with a patch" — so a reader who took the retrospective's framing and went looking for a patch to apply would find none. What the FBI and EPA have published about Minnesota, and what this pipeline recorded from that reporting, describes no vulnerability at all: attackers reached internet-exposed controllers, changed their IP addresses and passwords, and locked operators out — reachability plus credential control.

**Defender takeaway:** the operational consequence for a European water or wastewater operator is that this campaign still gives you nothing to patch, and a vendor claim that it does should not redirect the work. The controls that address the published technique are architectural — whether any controller answers on a routable address, whether the cellular or carrier-provided path is treated as untrusted, and whether default or weak credentials survive on management interfaces — and none of them are a patch cycle. The wider point is a sourcing habit worth applying generally: a CVE identifier in a vendor narrative is a claim like any other, and it is cheap to check against the CVE's own affected-product list. Here the check takes one page load and changes the conclusion, and the same check applied to an internal inventory would prevent an operator from concluding their MicroLogix estate is covered because they patched something else. This pipeline separately recorded a genuinely MicroLogix-relevant flaw, CVE-2017-16740, present in firmware on 19 of 22 devices one census found in campaign-targeted cities — that one is not in the KEV catalogue, and no source claims it was exploited either.

**Triage:** unchanged from prior coverage, because the technique is unchanged. The observables for this campaign are administrative rather than exploit-shaped: a controller-mode or configuration change with no corresponding maintenance window, a management session to a field device originating from outside the engineering workstation subnet — particularly from the carrier-side of a cellular router rather than from the operator's own network — and credential or network-configuration changes on a controller that the engineering team cannot attribute to a change record. Legitimate remote maintenance produces the same protocol events, which is why origin and change-record correlation, not the event type, is what separates them.
