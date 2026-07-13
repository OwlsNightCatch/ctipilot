---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-sector-patterns
title: Government and public administration across Switzerland and Europe took a broad spread of attacks this week — ransomware, espionage watering-holes, AI-tooled APTs and credential-phishing
headline: CH/EU government under broad attack this week — Latvia forestry ransomware, Swiss cantonal mailbox compromise, e-gov watering-hole, Ghostwriter phishing
summary: 'The constituency''s core sector was hit from several directions in 2026-W28: a ransomware crew breached Latvia''s state forestry operator LVM via a two-year-unpatched service (CERT.LV, an EU/NATO-shared-threat framing); Psychiatrische Dienste Aargau (a Swiss cantonal health authority) had email accounts phished and abused as a spam relay; espionage actors weaponised a citizen-facing e-government complaint portal as a watering hole; Armored Likho hit government and electric-power targets with an AI-generated loader; and UNC1151/Ghostwriter ran real-time 2FA-relay Gmail phishing against officials (CERT Polska). The common thread is not one actor but the breadth of pressure on public-sector identity, exposed services and citizen-facing web.'
discovered_at: '2026-07-12T23:30:00Z'
event_date: 2026-07-10
run_id: 2026-07-12T2309Z-weekly
priority: high
immediate_action: null
tags:
  - data-breach
  - espionage
  - ransomware
  - phishing
regions:
  - switzerland
  - europe
sectors:
  - public-sector
  - energy
entities:
  - incident:cert-lv-lvm-olpha-ransomware-2026
  - incident:pdag-email-phishing-2026
  - actor:bitter
  - actor:armored-likho
  - campaign:frostyneighbor-2026-05-campaign
cves: []
sources:
  - url: https://cert.lv/lv/2026/06/as-latvijas-valsts-mezi-kiberdrosibas-incidents-aktuala-informacija
    publisher: CERT.LV
    role: primary
  - url: https://www.swisscybersecurity.net/news/2026-07-09/psychiatrische-dienste-aargau-werden-opfer-eines-phishing-angriffs
    publisher: SwissCybersecurity.net
    role: primary
  - url: https://www.sentinelone.com/labs/one-target-china-india-espionage-converge-on-pakistani-law-enforcement/
    publisher: SentinelLabs
    role: primary
  - url: https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/
    publisher: Kaspersky Securelist
    role: corroborating
  - url: https://cert.pl/en/posts/2026/06/UNC1151-gmail-campaign/
    publisher: CERT Polska
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: Each strand is separately primary-sourced by a national CERT or a research lab (CERT.LV, SwissCybersecurity.net, SentinelLabs, Kaspersky, CERT Polska); the sector pattern is the synthesis. Reliability B (national-CERT strands are A in their own entries; the aggregate is weighted to the mix), credibility 1.
confidence: high
classification:
  reliability: B
  credibility: 1
update_of: null
references:
  - 2026-07-10/cert-lv-lvm-olpha-ransomware-eu-nato-shared-threat
  - 2026-07-09/pdag-aargau-email-account-compromise-spam-relay
  - 2026-07-10/e-government-portal-watering-hole-cms-implant-espionage
  - 2026-07-11/armored-likho-busysnake-ai-generated-loader-python-stealer
  - 2026-07-09/unc1151-ghostwriter-gmail-realtime-2fa-phishing
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
---
Government and public administration — the profiled constituency's core — absorbed an unusually broad spread of activity in 2026-W28, notable less for any single incident than for how many different attack classes landed on the sector in one week.

On the **ransomware** front, CERT.LV disclosed that a crew breached Latvijas Valsts Meži (LVM), Latvia's state forestry operator, through a service left unpatched for roughly two years, and framed it explicitly as an EU/NATO-shared-threat matter for a state-owned critical operator ([CERT.LV, 2026-06](https://cert.lv/lv/2026/06/as-latvijas-valsts-mezi-kiberdrosibas-incidents-aktuala-informacija)). In Switzerland, **Psychiatrische Dienste Aargau (PDAG)**, a cantonal health authority, had staff email accounts compromised via phishing and abused to relay spam — a low-sophistication but high-frequency pattern against public-sector mailboxes ([SwissCybersecurity.net, 2026-07-09](https://www.swisscybersecurity.net/news/2026-07-09/psychiatrische-dienste-aargau-werden-opfer-eines-phishing-angriffs)). On the **espionage** axis, SentinelLabs documented converging China- and India-nexus operations weaponising a citizen-facing e-government complaint portal as a watering hole with a CMS implant ([SentinelLabs, 2026-07-10](https://www.sentinelone.com/labs/one-target-china-india-espionage-converge-on-pakistani-law-enforcement/)); Kaspersky profiled **Armored Likho** hitting government and electric-power targets with an AI-generated loader and the BusySnake stealer ([Kaspersky Securelist, 2026-07-11](https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/)); and CERT Polska tracked **UNC1151/Ghostwriter** moving to Gmail with real-time 2FA-relay phishing against officials ([CERT Polska, 2026-06](https://cert.pl/en/posts/2026/06/UNC1151-gmail-campaign/)).

**Why this is a sector pattern for the constituency:** two of the five strands carry a direct home-region or EU-critical-operator nexus (a Swiss cantonal authority and a Latvian state operator); the e-government watering-hole targeted a Pakistani law-enforcement programme (EU-funded but with no direct European victim nexus) and is carried for its transferable technique, while the remaining two are actors whose targeting profile — government and energy — matches the constituency. The exposed surfaces recur: unpatched internet-facing services, public-sector email identity, and citizen-facing web applications.

**Defender takeaway:** the week's public-sector lesson is coverage of the unglamorous basics — an authoritative patch SLA for internet-facing services (the LVM two-year gap is the cautionary case), phishing-resistant MFA on staff mail to break both spam-relay abuse and 2FA-relay phishing, and integrity monitoring on citizen-facing CMS platforms that make natural watering holes. **Triage:** a compromised public-sector mailbox used as a relay shows a sudden outbound-volume spike and sends to external recipients with no prior correspondence; a watering-hole CMS implant shows unexpected file writes to web-root and template/plugin directories outside a deployment window.
