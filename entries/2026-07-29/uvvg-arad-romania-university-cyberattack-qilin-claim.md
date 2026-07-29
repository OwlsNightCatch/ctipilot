---
schema: 1
kind: incident
horizon: operational
title: "Romanian public university UVVG Arad confirms a cyberattack on its IT infrastructure; a Qilin leak-site listing is the only thing linking an actor to it"
headline: "West University Vasile Goldis Arad notifies DNSC, the data-protection authority and prosecutors after an attack on academic and administrative systems"
summary: >
  Universitatea de Vest "Vasile Goldis" din Arad, a Romanian public university, issued a press release on
  2026-07-28 confirming that a recently identified cyberattack affected its IT infrastructure and the
  digital services used in academic and administrative work, that it notified the national cybersecurity
  directorate DNSC, the data-protection authority ANSPDCP and organised-crime prosecutors DIICOT, and
  that technical teams are working with external specialists on gradual restoration. The university does
  not say which systems are unavailable, whether personal data was accessed or exfiltrated, when the
  attack occurred, or who was responsible. Separately, the Qilin ransomware operation listed the
  university on its leak site with an estimated attack date of 2026-07-26 — a claim carried only by a
  leak-site mirror, which none of the Romanian reporting mentions at all.
discovered_at: "2026-07-29T05:50:00Z"
event_date: "2026-07-28"
run_id: 2026-07-29T0408Z-intel
priority: notable
immediate_action: null
tags: [ransomware, data-breach]
regions: [europe]
sectors: [public-sector, education]
entities: [incident:uvvg-arad-cyberattack-2026-07, actor:qilin]
techniques: [T1486]
affected_products: []
cves: []
sources:
  - url: "https://www.aradon.ro/aradon-stirile-judetului-arad/atac-cibernetic-la-uvvg-arad-2225370/"
    publisher: "Aradon.ro"
    date: "2026-07-28"
    role: primary
  - url: "https://www.radioromania.ro/stiri-locale/arad-universitatea-de-vest-tinta-unui-atac-cibernetic-id203468.html"
    publisher: "Radio România"
    date: "2026-07-28"
    role: corroborating
  - url: "https://www.sportarad.ro/2026/07/28/universitatea-de-vest-vasile-goldis-din-arad-ofera-informatii-cu-privire-la-incidentul-de-securitate-cibernetica-ce-a-vizat-infrastructura-it-a-institutiei/"
    publisher: "Sportarad.ro"
    date: "2026-07-28"
    role: corroborating
  - url: "https://www.ransomware.live/id/VW5pdmVyc2l0YXRlYSBkZSBWZXN0IOKAnlZhc2lsZSBHb2xkaciZ4oCdIGRpbiBBcmFkQHFpbGlu"
    publisher: "Ransomware.live (Qilin leak-site mirror)"
    date: "2026-07-26"
    role: corroborating
closed_sources: []
evidence:
  - quote: "recent a fost identificat un atac cibernetic care a afectat infrastructura informatică a universității"
    publisher: "Aradon.ro"
  - quote: "Universitatea nu a precizat, deocamdată, care sunt sistemele indisponibile și nici dacă au fost compromise sau extrase date personale."
    publisher: "Radio România"
  - quote: "Autoritățile urmează să stabilească natura atacului, modul în care agresorii au pătruns în sistemele informatice și amploarea eventualelor prejudicii."
    publisher: "Radio România"
verification: single-source-victim
sourcing_note: >
  The confirmed facts come from the university's own press release about its own incident, which is the
  victim-disclosure carve-out; six Romanian outlets were found running near-identical text and the fullest
  verbatim transcription is cited as primary, with Radio România — the national public broadcaster —
  carried as the highest-reliability relay and the source of the clearest statement of what remains
  unconfirmed. No copy of the statement could be located on the university's own domain despite fetching
  its homepage and news subdomain and running a site-restricted search, so the release appears to have been
  distributed directly to regional outlets rather than published as a page; multiple outlets explicitly
  frame it as a press release. The actor claim and the confirmed incident are two unlinked streams and are
  kept that way: the Qilin attribution rests solely on a leak-site mirror listing, carries no description
  text on the listing itself, and is mentioned by none of the six Romanian articles, which name no actor
  and do not use the word ransomware. The university's statement therefore does not corroborate the Qilin
  claim in any respect. The single ATT&CK mapping describes only the ransomware claim, which is itself
  unconfirmed; no source provides technical detail that would support any further mapping, so none is
  invented. The leak-site mirror is cited as a corroborating source so a reader can see exactly what the
  actor claim rests on; it is a discovery-layer aggregator, not a terminal authority. Reliability is rated B
  rather than A: the load-bearing statement is the university's own, but no first-party copy is verifiable
  and the fullest transcription sits on a regional news portal, with the national broadcaster as the
  strongest relay — the A letter is reserved in this pipeline for first-party authorities publishing
  directly.
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

The university's press release is specific about process and silent about substance. It states that a cyberattack was recently identified which affected the institution's IT infrastructure and the functioning of digital services used in academic and administrative activity, that the competent authorities were notified immediately — naming DNSC, the national cybersecurity directorate; ANSPDCP, the data-protection authority; and DIICOT, the organised-crime and terrorism prosecution directorate — and that technical teams are working with specialists on the gradual resumption of affected services ([Aradon.ro, 2026-07-28](https://www.aradon.ro/aradon-stirile-judetului-arad/atac-cibernetic-la-uvvg-arad-2225370/)). Radio România is direct about the gaps: the university has not specified which systems are unavailable, nor whether personal data was compromised or extracted, and authorities are yet to determine the nature of the attack, how the attackers entered the systems and the scope of any damage, with no timeframe announced for full restoration ([Radio România, 2026-07-28](https://www.radioromania.ro/stiri-locale/arad-universitatea-de-vest-tinta-unui-atac-cibernetic-id203468.html)). The notification of all three authorities at once is itself informative: DIICOT's involvement indicates a criminal referral, and ANSPDCP's indicates the university considered a personal-data breach at least possible, even while declining to confirm one.

The actor question should be read carefully, because the two available pieces of information do not actually touch. The Qilin ransomware operation listed the university on its leak site with an estimated attack date of 2026-07-26, two days before the university's disclosure ([Ransomware.live, 2026-07-26](https://www.ransomware.live/id/VW5pdmVyc2l0YXRlYSBkZSBWZXN0IOKAnlZhc2lsZSBHb2xkaciZ4oCdIGRpbiBBcmFkQHFpbGlu)). That listing is the *only* source for the connection: it carries no description text, and none of the Romanian outlets covering the incident — including the national broadcaster — mentions Qilin, ransomware, or any actor at all. So while the timing is consistent with an unresolved extortion negotiation, which is the ordinary explanation for a victim confirming a "cybersecurity incident" without naming a cause, nothing in the university's statement corroborates the claim, and treating the two as one confirmed story would be assembling an attribution the sources do not make.

**Defender takeaway:** for the Swiss and European public-sector and research estate, the transferable content here is not the technique — none has been disclosed — but the disclosure pattern, and this window has now produced several instances of it. A victim confirms an incident in general terms and refers it to a national CERT, a data-protection regulator and prosecutors simultaneously, while a leak site independently claims the same organisation days earlier; the actor claim precedes and outlives the victim's own account of scope. Two consequences follow for anyone tracking sector incidents. First, an early institutional statement that declines to confirm data exfiltration is not evidence that none occurred — the same pattern in this window's Romanian land-registry and Geneva adult-education cases was later contradicted by a national-CERT report and by published data respectively. Second, a leak-site listing is a lead for monitoring rather than a fact to act on: it justifies watching for a subsequent publication or a regulator notice, not a briefing that names the actor. Higher-education institutions remain a soft segment of the public-sector attack surface — large, federated identity estates with heavy third-party service use and thin out-of-hours coverage — and the practical read-across is to check that your own incident playbook can answer "which systems are unavailable and was personal data accessed" faster than this one currently can.
