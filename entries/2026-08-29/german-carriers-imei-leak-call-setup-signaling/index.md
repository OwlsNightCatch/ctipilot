---
schema: 1
kind: research
title: "German mobile carriers leaked callees' IMEI, device model and OS version to callers during call setup — GSMA confirmed the flaw and warned its 1,000+ member operators worldwide"
headline: "A phone call alone could fingerprint the callee's device and patch level, and GSMA's warning suggests the gap is not Germany-specific"
summary: >
  An investigation by Bayerischer Rundfunk (BR), corroborated by heise, found that Germany's three mobile network
  operators (Deutsche Telekom, Vodafone, Telefónica/O2) forwarded device-identifying data — a callee's full IMEI, or
  smartphone model and OS version — to the calling party during call setup, in certain unspecified network/device
  constellations. The GSMA confirmed the flaw on inquiry and warned its 1,000+ member operators worldwide to review
  their networks; Germany's BfV assessed it as security-relevant, citing near-certain exploitation by foreign
  intelligence services. A parallel April-2026 finding in Norwegian networks suggests the underlying gap is not
  carrier-specific.
discovered_at: "2026-08-29T04:09:36Z"
updated_at: null
event_date: "2026-08-27"
run_id: 2026-08-29T0409Z-intel
priority: high
immediate_action: null
tags: [espionage, identity]
regions: [dach, europe]
sectors: [telco, public-sector]
entities: []
techniques: [T1592.004]
affected_products: []
cves: []
sources:
  - url: "https://www.br.de/nachrichten/deutschland-welt/sicherheitsluecke-mobilfunknetze-verrieten-sensible-handydaten,VTPFtd7"
    publisher: "Bayerischer Rundfunk (BR24)"
    date: "2026-08-27"
    role: primary
  - url: "https://www.heise.de/news/Mobilfunk-IMEI-Kennungen-gelangten-beim-Rufaufbau-unbemerkt-zu-Anrufern-11427013.html"
    publisher: "heise Security"
    date: "2026-08-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "In the networks of Telekom and Telefónica (O2), IMEI numbers reached the caller in several cases."
    original: "In den Netzen von Telekom und Telefónica (O2) gelangten dabei in mehreren Fällen IMEI-Nummern zum Anrufer."
    publisher: "Bayerischer Rundfunk (BR24)"
  - quote: "The Federal Office for the Protection of the Constitution (BfV) assesses the security vulnerability discovered by BR research, on inquiry, as \"security-relevant\"."
    original: "Das Bundesamt für Verfassungsschutz (BfV) wertet die von BR Recherche entdeckte Sicherheitslücke auf Anfrage als \"sicherheitsrelevant\"."
    publisher: "Bayerischer Rundfunk (BR24)"
  - quote: "After BR approached the association with questions, it warned its more than 1,000 member companies, which also include the German network operators."
    original: "Nachdem der BR sich mit Fragen an den Verband gewandt hatte, warnte er seine mehr als 1.000 Mitgliedsunternehmen, wozu auch die deutschen Netzanbieter gehören."
    publisher: "Bayerischer Rundfunk (BR24)"
verification: multi-source
sourcing_note: "Two independent journalistic assessors (Bayerischer Rundfunk's original investigation and heise's corroborating report) plus on-the-record confirmation from the GSMA and Germany's BfV. Neither source names the precise signaling layer carrying the leaked data — recorded as an open question, not invented."
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Bayerischer Rundfunk (BR) published an investigation, corroborated the same window by heise, that found Germany's
three mobile network operators — Deutsche Telekom, Vodafone and Telefónica/O2 — forwarded device-identifying data to
the calling party during call setup, before the callee ever answered
([BR24, 2026-08-27](https://www.br.de/nachrichten/deutschland-welt/sicherheitsluecke-mobilfunknetze-verrieten-sensible-handydaten,VTPFtd7)).
Across more than 70 test calls, Telekom's and O2's networks in several cases forwarded the callee's full 15-digit
IMEI — confirmed by Wireshark packet captures of the call-setup traffic — and Telekom's and Vodafone's networks
separately exposed the callee's smartphone model and operating-system version, specific enough to reveal whether a
target device was missing a given security update
([BR24, 2026-08-27](https://www.br.de/nachrichten/deutschland-welt/sicherheitsluecke-mobilfunknetze-verrieten-sensible-handydaten,VTPFtd7);
[heise Security, 2026-08-27](https://www.heise.de/news/Mobilfunk-IMEI-Kennungen-gelangten-beim-Rufaufbau-unbemerkt-zu-Anrufern-11427013.html)).
The leak occurred only in certain unspecified network/device constellations rather than on every call, and BR could
not establish since when the gap existed; BR notified the three operators in late June 2026, after which Vodafone
said it had "further narrowed" transmitted call data, Telekom said in mid-August it would adjust its network, and
Telefónica said it had implemented technical measures — all three state they otherwise meet international industry
standards ([BR24, 2026-08-27](https://www.br.de/nachrichten/deutschland-welt/sicherheitsluecke-mobilfunknetze-verrieten-sensible-handydaten,VTPFtd7)).

The GSMA confirmed the flaw on inquiry and, per a nine-page briefing BR obtained, warned its 1,000+ member operators
worldwide to review their networks and filter unnecessarily transmitted call-setup information — an implicit
acknowledgment that the same signaling gap plausibly extends beyond Germany's three carriers to any GSMA member
network ([BR24, 2026-08-27](https://www.br.de/nachrichten/deutschland-welt/sicherheitsluecke-mobilfunknetze-verrieten-sensible-handydaten,VTPFtd7)).
Germany's domestic security service (BfV) assessed the flaw as security-relevant, stating that given cyberattacks
against mobile devices by state-affiliated actors already on record, it is "near-certain" that foreign intelligence
services use such information for their own purposes
([BR24, 2026-08-27](https://www.br.de/nachrichten/deutschland-welt/sicherheitsluecke-mobilfunknetze-verrieten-sensible-handydaten,VTPFtd7)).
A scenario in the Bundeswehr's own magazine "Y" illustrates the mechanism: correlating a soldier's IMEI between a
domestic posting and a later deployment abroad — its example is a training ground in Lithuania — could put that
individual "in a spy's focus"; the Federal Ministry of Defense separately told BR that intelligence services can use
such device identifiers to build movement profiles and identify individuals
([BR24, 2026-08-27](https://www.br.de/nachrichten/deutschland-welt/sicherheitsluecke-mobilfunknetze-verrieten-sensible-handydaten,VTPFtd7)).
HPI mobile-security researcher Jiska Classen called it a serious flaw enabling mass profile-building and said it
shows how poorly such carrier systems are tested
([BR24, 2026-08-27](https://www.br.de/nachrichten/deutschland-welt/sicherheitsluecke-mobilfunknetze-verrieten-sensible-handydaten,VTPFtd7)).
SRLabs founder Karsten Nohl, asked by heise to elaborate, added that device-model exposure also enables more
targeted attacks and IMEI cloning, while stating he sees no dramatic security impact in the finding on its own
([heise Security, 2026-08-27](https://www.heise.de/news/Mobilfunk-IMEI-Kennungen-gelangten-beim-Rufaufbau-unbemerkt-zu-Anrufern-11427013.html)).
BR notes the finding parallels an April-2026 discovery of a similar flaw in Norwegian networks by Mnemonic researcher
Harrison Sand, who shared his methodology with BR — suggesting the underlying signaling gap is not specific to any
one carrier or country
([BR24, 2026-08-27](https://www.br.de/nachrichten/deutschland-welt/sicherheitsluecke-mobilfunknetze-verrieten-sensible-handydaten,VTPFtd7)).

Neither BR nor heise names the precise signaling layer — an SS7 interconnect field, a Diameter/IMS parameter, or a
VoLTE SIP header — carrying the leaked data; this is recorded as an unresolved open question, not an invented
mechanism. Detection concept for a telco SOC or network-security team: audit outbound call-setup signaling at the
interconnect boundary for device-identifying parameters (IMEI, UE capability/OS-version fields) reaching the
calling party or a foreign network, consistent with GSMA and IETF guidance (RFC 7254, RFC 7255) that such fields be
anonymized or stripped before leaving the home network
([heise Security, 2026-08-27](https://www.heise.de/news/Mobilfunk-IMEI-Kennungen-gelangten-beim-Rufaufbau-unbemerkt-zu-Anrufern-11427013.html)).
Hardening lever: filter or strip unnecessary device-identifying call-setup parameters at the network edge, per the
GSMA's own briefing recommendation.
**Defender takeaway:** for public-sector mobile fleets whose personnel travel internationally — defense, diplomatic,
law-enforcement — call-based device fingerprinting is a tracking vector independent of the SIM, and roaming exposes
it to a foreign operator by design; this is a policy/procurement question (does the fleet's home carrier still leak
this after the fixes described here) as much as a technical one. Swiss carriers (Swisscom, Sunrise, Salt) were not
tested by BR; whether they carry the same gap is unconfirmed and worth a direct inquiry given the GSMA's broad
member warning.
