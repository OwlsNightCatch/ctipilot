---
schema: 1
kind: incident
horizon: operational
title: "Threema and its Swiss colocation partner were hit by the same adaptive DDoS wave — the attack moved to the hosting layer, and only the self-hosted customers stayed up"
headline: "Swiss messenger Threema loses four hours to a DDoS campaign that also hit its colocation partner; availability only, no access to systems or data"
summary: >
  Threema disclosed on 2026-08-14 that a series of large-scale DDoS attacks over two days targeted both its own
  infrastructure and its Swiss colocation partner Nine, leaving it unclear whether Threema was the primary
  target. The service was unavailable for four hours on the Tuesday evening with intermittent interruptions
  into Wednesday. Threema states availability only was affected, not systems or data, and that customers running
  Threema OnPrem on their own infrastructure were unaffected throughout.
discovered_at: "2026-08-15T04:53:00Z"
event_date: "2026-08-14"
run_id: 2026-08-15T0412Z-intel
priority: notable
immediate_action: null
tags:
  - ddos
regions:
  - switzerland
  - europe
sectors:
  - telco
  - technology
entities:
  - incident:threema-nine-ddos-2026-08
techniques: [T1498]
affected_products:
  - Threema
cves: []
sources:
  - url: "https://threema.com/en/blog/outage-august-2026"
    publisher: Threema GmbH
    date: "2026-08-14"
    role: primary
  - url: "https://cyberinsider.com/threema-messenger-says-ddos-attacks-disrupted-its-service-for-two-days/"
    publisher: CyberInsider
    date: "2026-08-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This week, however, a series of large-scale DDoS attacks targeted Threema and our colocation partner, Nine. It is not entirely clear whether Threema was the primary target or whether the attacks were directed at multiple targets."
    publisher: Threema GmbH
  - quote: "Because organizations using Threema OnPrem rely on their own infrastructure, they were not affected by this wave of attacks and were able to use their Threema OnPrem instances as usual at all times, without any interruptions."
    publisher: Threema GmbH
verification: single-source-victim
sourcing_note: >
  Threema's own disclosure about its own outage is the sole account of the event and the victim-disclosure
  carve-out applies; the corroborating outlet derives its reporting from the same post rather than observing
  independently. No party has attributed the attacks to a named actor, and Threema's reference to state actors
  is a general statement about well-resourced attackers, not an attribution of this incident.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

Threema, the Swiss end-to-end-encrypted messenger, published an account on 2026-08-14 of a two-day disruption: a series of large-scale DDoS attacks targeted Threema and its colocation partner Nine, and Threema states it is not entirely clear whether it was the primary target or whether the attacks were directed at multiple targets ([Threema, 2026-08-14](https://threema.com/en/blog/outage-august-2026)). The service was unavailable on the Tuesday between 19:30 and 23:30 CEST; the attacks resumed on Wednesday morning and produced intermittent brief interruptions until normal operations were restored at 12:23. Threema notes that its status page was initially not updating because of a technical issue unrelated to the attack, and that it took the page offline until that was fixed — a small detail with a wider lesson, since the channel an organisation uses to tell users what is happening shares infrastructure and failure modes with the thing that is failing.

Threema is explicit about what the incident was not: a denial-of-service attack targets only the availability of an online service, not its security, and even a successful one gives attackers no access to systems or data ([Threema, 2026-08-14](https://threema.com/en/blog/outage-august-2026)). It describes the defensive problem as a contest of resources in which sophisticated attackers continuously change their sources and patterns during an attack, producing what it calls a cat-and-mouse game, and notes that even with effective DDoS protection in place, temporary disruption cannot always be prevented when an attacker has considerable technical and financial resources — as, it says, may be the case with state actors. That is a general observation about well-resourced adversaries; Threema does not attribute this incident to one, and no other party has. Threema says it is adding specialised DDoS protection that filters attack traffic upstream of its own infrastructure, and an update on the same post records that protection as now activated in the production environment ([Threema, 2026-08-14](https://threema.com/en/blog/outage-august-2026)).

The transferable point for an operator sits in the two facts Threema puts either side of the outage. The attack reached the colocation partner as well as the service, which means an application-layer mitigation scoped to the service's own edge is not scoped to the whole failure domain — the hosting provider's capacity is a shared dependency, and a tenant is exposed to a volumetric attack aimed at a neighbour. And customers running Threema OnPrem, on their own infrastructure, were unaffected throughout and used their instances without interruption ([Threema, 2026-08-14](https://threema.com/en/blog/outage-august-2026)). For a public-sector body that has adopted a hosted secure-messaging service as its out-of-band or emergency communications channel, that is the operationally relevant sentence: the deployment model, not the protocol, decided who could still talk to each other that evening.

**Defender takeaway:** an out-of-band communications plan is only out-of-band if its dependencies differ from the systems it is meant to back up. Check which of your fallback channels terminate in the same hosting facility or provider as each other, and confirm that the failure of a shared colocation provider does not take the primary channel and its designated fallback down together.
