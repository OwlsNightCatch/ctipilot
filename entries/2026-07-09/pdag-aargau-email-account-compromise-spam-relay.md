---
schema: 1
kind: incident
horizon: operational
title: "Psychiatrische Dienste Aargau (PDAG) email accounts compromised via phishing and abused to relay spam"
headline: "Swiss cantonal psychiatric provider PDAG discloses phishing-driven takeover of staff mailboxes used to send outbound spam/phishing"
summary: >
  Psychiatrische Dienste Aargau AG (PDAG), a Swiss cantonal psychiatric-care provider,
  disclosed that unauthorised parties gained access to individual @pdag.ch email accounts and
  abused them to send spam/phishing to external recipients. PDAG locked the affected accounts,
  reset passwords for all employees, and notified cantonal and national authorities; by its
  current assessment there is no indication patient data was accessed or exfiltrated.
discovered_at: "2026-07-09T12:28:00Z"
event_date: "2026-07-08"
run_id: 2026-07-09T1211Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity]
regions: [switzerland]
sectors: [healthcare, public-sector]
entities: [incident:pdag-email-phishing-2026]
cves: []
sources:
  - url: "https://www.swisscybersecurity.net/news/2026-07-09/psychiatrische-dienste-aargau-werden-opfer-eines-phishing-angriffs"
    publisher: "SwissCybersecurity.net"
    date: "2026-07-09"
    role: primary
  - url: "https://www.inside-it.ch/cyberangriff-auf-psychiatrische-dienste-aargau-20260708"
    publisher: "Inside IT Switzerland"
    date: "2026-07-08"
    role: corroborating
closed_sources: []
evidence: []
verification: single-source-victim
sourcing_note: "Single-source-victim carve-out: both outlets carry PDAG's own disclosure; the inside-it.ch article (its stable permalink for the item surfaced in the outlet's own RSS feed) is anti-bot-403 to direct fetch and the reader proxy, so it corroborates only the fact and date of the incident — the substance comes from the SwissCybersecurity.net primary. No technical root-cause detail (initial-access vector, MFA state, OAuth-consent vs credential phishing) was disclosed by PDAG or either outlet — flagged as a gap, not inferred. Confidence medium accordingly."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions:
  - "Any Swiss public-sector or health body operating an @<domain>.ch mail estate should implement per-mailbox outbound-volume anomaly detection: a legitimate mailbox suddenly sending bulk external mail is an earlier and stronger compromise signal than waiting for external abuse reports."
  - "Monitor DMARC/DKIM alignment reporting for your own domain to catch when it starts being used as a relay (authenticated sending from compromised accounts) rather than merely spoofed, and enforce MFA plus conditional-access on all mailboxes."
migrated_from: null
---

Psychiatrische Dienste Aargau AG (PDAG), a Swiss cantonal psychiatric-care provider, disclosed that unauthorised parties gained access to individual `@pdag.ch` email accounts and abused them to send spam and phishing messages to external recipients ([SwissCybersecurity.net, 2026-07-09](https://www.swisscybersecurity.net/news/2026-07-09/psychiatrische-dienste-aargau-werden-opfer-eines-phishing-angriffs); [Inside IT, 2026-07-08](https://www.inside-it.ch/cyberangriff-auf-psychiatrische-dienste-aargau-20260708)). On discovery, PDAG locked the affected accounts immediately, reset passwords for all employees as a precaution, notified the competent cantonal and national authorities, and engaged internal and external IT-security experts plus its external ICT service provider to analyse and harden. By its current assessment the incident is limited to account misuse for outbound spam/phishing, with no indication that patient data was accessed or exfiltrated; the organisation is warning recipients about suspicious mail purporting to come from its domain.

No technical root cause — the initial-access vector into the mailboxes, whether MFA was enforced, or whether the takeover was via credential phishing or an OAuth consent grant — was disclosed, so the mechanism is unknown rather than assumed. The pattern maps to `T1566 Phishing` for the initial access and `T1586.002 Compromise Accounts: Email Accounts` for the takeover and downstream abuse. **Defender takeaway:** this is a minor incident in impact (no data breach confirmed) but a directly relevant one for the Swiss public/health sector — the containment (mass lockout plus all-staff reset) was correct, and the detection lesson it underlines for any organisation with a cantonal or federal `.ch` mail presence is that per-mailbox outbound anomaly detection and DMARC-alignment monitoring catch a compromised-legitimate-sender case that inbound-only phishing controls do not.
