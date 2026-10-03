---
schema: 1
kind: annual-report
title: "Rapid7's Q2 2026 quarterly report: high- and critical-severity disclosures doubled year on year to 8,539 while the number newly exploited held flat at 40 — and 62% of what was exploited needed no user interaction at all"
headline: "Rapid7 Q2 2026: disclosure volume doubled, exploitation did not — and missing-authentication disclosures rose 247%"
summary: >
  Rapid7 Labs published its Quarterly Threat Landscape Report for Q2 2026 on 2026-08-18. It counts 8,539 new high-
  and critical-severity CVEs in the quarter against 4,268 in the same quarter a year earlier, while the number of
  vulnerabilities newly observed under exploitation held roughly steady at 40 — its argument being not that
  exploitation exploded but that disclosure volume has outrun what any team can triage. (The report states that
  steadiness without naming a comparison period.) Of the flaws that were
  exploited, 62% required no user interaction, up nine points from 53% a year earlier, and disclosures of
  missing-authentication flaws rose 247% year on year. Qilin led leak-site activity with 263 listed victims, and
  ClickFix, fake-CAPTCHA and social engineering through trusted collaboration platforms together accounted for 31.8%
  of the incidents Rapid7's incident-response team worked.
discovered_at: "2026-08-24T09:14:00Z"
event_date: "2026-08-18"
run_id: 2026-08-24T0410Z-intel
priority: notable
immediate_action: null
tags: [vulnerabilities, actively-exploited, ransomware, phishing, nation-state, ot-ics]
regions: [global, europe]
sectors: [public-sector, healthcare, energy, finance, manufacturing, telco]
entities:
  - report:rapid7-quarterly-threat-landscape-q2-2026
techniques: [T1190, T1204.004, T1566.003, T1133, T1486]
affected_products: []
cves: []
sources:
  - url: "https://www.rapid7.com/blog/post/tr-new-report-ai-threats-q2-2026-ends-traditional-patch-cycles"
    publisher: "Rapid7 Labs"
    date: "2026-08-18"
    role: primary
closed_sources: []
evidence:
  - quote: "There were 8,539 new high- and critical-severity CVEs (CVSS 7.0–10.0) this quarter- double the number reported in the same quarter last year (4,268)."
    publisher: "Rapid7 Labs"
  - quote: "Nearly two-thirds of exploited vulnerabilities this quarter (62%) required no user interaction - no stolen credentials, no phishing victim, no click."
    publisher: "Rapid7 Labs"
verification: single-source
sourcing_note: >
  Single-source: a vendor's own quarterly telemetry report, carried as the vendor's own measurement rather than as an
  independently corroborated fact — the figures are Rapid7's count over Rapid7's data and no second party has
  reproduced them. Composed from the summary post Rapid7 published alongside the report; the full report is gated.
  Reproduced verbatim from the page including its own typographic artefacts (an en dash in the CVSS range, a
  space-less hyphen in "quarter- double").
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
migrated_from: null
---

Rapid7 Labs published its **Quarterly Threat Landscape Report** for Q2 2026 on 2026-08-18 ([Rapid7 Labs, 2026-08-18](https://www.rapid7.com/blog/post/tr-new-report-ai-threats-q2-2026-ends-traditional-patch-cycles)). One pair of numbers carries the argument: "There were 8,539 new high- and critical-severity CVEs (CVSS 7.0–10.0) this quarter- double the number reported in the same quarter last year (4,268)," while the count of vulnerabilities newly observed under exploitation "held roughly steady (40)" — a comparison the report makes without stating the period it is against, in a paragraph whose preceding sentence is year-on-year. Rapid7 is explicit that the finding is not an exploitation surge but a triage-capacity one — disclosure volume is far outstripping what any team can work through.

Three further measurements give that a defensive shape. First, the exploited set has moved further out of the user's hands: "Nearly two-thirds of exploited vulnerabilities this quarter (62%) required no user interaction - no stolen credentials, no phishing victim, no click," up nine points from 53% in Q2 2025 — meaning awareness training and phishing-resistant authentication, whatever else they buy, are addressing a shrinking share of what actually gets exploited. Second, disclosures of **missing-authentication** flaws (CWE-306) rose 247% year on year, which Rapid7 frames as a fast-expanding pool of internet-facing systems requiring no login at all; that is a category where an asset-exposure question answers the risk question directly, without needing a severity score. Third, on the intrusion side, Qilin led ransomware activity with 263 listed victims, the United States remained the most-targeted country, and business services and healthcare were among the hardest-hit sectors — while ClickFix and fake-CAPTCHA campaigns together with social engineering through trusted collaboration platforms such as Microsoft Teams accounted for **31.8%** of the incidents Rapid7's incident-response team worked. Rapid7 also records continued Iranian, North Korean and Russian state-nexus activity against government, finance, healthcare, manufacturing, energy and telecommunications, with Russian campaigns focused on edge infrastructure and Iranian activity including sustained ICS and OT targeting.

Rapid7's own conclusion is a prioritisation argument rather than a patching one: as disclosures keep growing, the organisations that stay ahead will not be the ones patching fastest but the ones that know what they expose, which assets matter most, where an attacker can realistically get in, and how to reduce reachable exposure before it becomes an incident.

**Defender takeaway:** the useful reading for this constituency is that severity-ranked patch queues degrade as disclosure volume grows, and Rapid7's own numbers show why — the quantity to triage doubled while the quantity actually exploited did not move, so the ratio of noise to signal in a CVSS-ordered queue roughly halved. The two findings that translate into a concrete change of method are the 62% no-interaction share and the 247% rise in missing-authentication disclosures: both say that *reachability* discriminates better than severity, and that an accurate inventory of what is internet-facing and what authenticates is the input a triage process needs most. That pairs directly with this store's own finding a day earlier that the exploitation flag itself has become a per-authority opinion — if neither severity nor the exploited flag can be relied on to order the queue, exposure is what is left. Note also what Rapid7's report does not support: it gives no basis for deprioritising user-facing defences, since the 31.8% incident-response share for ClickFix, fake-CAPTCHA and collaboration-platform social engineering is measured on intrusions rather than on vulnerabilities, and those two populations are different things.
