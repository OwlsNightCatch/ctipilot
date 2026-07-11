---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: MuddyWater (Iran / MOIS) Chaos ransomware false-flag + Teams BEC
headline: MuddyWater (Iran / MOIS) Chaos ransomware false-flag + Teams BEC
summary: "Current state: refreshed 2026 campaign documented by Rapid7 (\"Muddying the Tracks\") and corroborated this week by BleepingComputer and SecurityWeek."
discovered_at: "2026-05-04T05:00:34Z"
event_date: null
run_id: 2026-W19-a5788b22
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - ransomware
  - phishing
  - identity
  - iran-nexus
regions:
  - us
  - middle-east
sectors:
  - manufacturing
entities:
  - "actor:muddywater"
cves: []
sources:
  - url: "https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/"
    publisher: Rapid7 — Muddying the Tracks
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/muddywater-hackers-use-chaos-ransomware-as-a-decoy-in-attacks/"
    publisher: BleepingComputer — MuddyWater Chaos decoy
    role: corroborating
  - url: "https://www.securityweek.com/iranian-apt-intrusion-masquerades-as-chaos-ransomware-attack/"
    publisher: SecurityWeek — Iranian APT masquerades as Chaos
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W19.md
---

Current state: refreshed 2026 campaign documented by Rapid7 ("Muddying the Tracks") and corroborated this week by BleepingComputer and SecurityWeek. Per Rapid7 ("Operation Olalampo"), the campaign's observed victimology is construction, manufacturing, and business-services organisations in the U.S. and MENA regions; deploys Chaos ransomware with criminal-group branding to complicate attribution and delay IR triage; uses Microsoft Teams external-chat requests for an interactive screen-sharing helpdesk pretext to harvest credentials and manipulate MFA. Attribution evidence per Rapid7: a "Donald Gay" code-signing certificate, the `moonzonet[.]com` C2 domain, `pythonw.exe` process injection of suspended processes, and the Teams MFA-harvest tradecraft — all consistent with prior MuddyWater (Seedworm) operations attributed to Iran's Ministry of Intelligence and Security ([Rapid7 — Muddying the Tracks: The State-Sponsored Shadow Behind Chaos Ransomware](https://www.rapid7.com/blog/post/tr-muddying-tracks-state-sponsored-shadow-behind-chaos-ransomware/) · [BleepingComputer — MuddyWater hackers use Chaos ransomware as a decoy](https://www.bleepingcomputer.com/news/security/muddywater-hackers-use-chaos-ransomware-as-a-decoy-in-attacks/) · [SecurityWeek — Iranian APT intrusion masquerades as Chaos ransomware attack](https://www.securityweek.com/iranian-apt-intrusion-masquerades-as-chaos-ransomware-attack/)). M-Trends 2026 (§ 6) notes voice phishing surged to the second most prevalent initial-access vector at 11% with IT help-desk impersonation as a primary modality — MuddyWater's Teams variant of that pattern is operationally similar. Outstanding defender question: whether the same false-flag tradecraft expands across additional Chaos-branded incidents now that the attribution is public.
