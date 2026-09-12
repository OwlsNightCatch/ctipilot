---
schema: 1
kind: threat
title: "\"Ransom Busters\" emails ransomware victims before their incident is public, offering to delete the stolen data for a fee — and the tooling says it is the same affiliate who took it"
headline: "The tell is the timing: a recovery offer that arrives while the intrusion is still private is foreknowledge, not marketing"
summary: >
  GuidePoint Security's research team documents an entity calling itself Ransom Busters that emails ransomware
  victims at their own domain, asking for the CEO or IT leadership, claiming years of unauthorised access to
  criminal infrastructure and offering to return stolen files and delete the attackers' copies for
  $20,000-$60,000. The anomaly that gives it away is timing: the outreach arrives before the intrusion is public
  knowledge. Across two responses GuidePoint found the same reconnaissance scanner, the same cloud-exfiltration
  utility, the same remote-management tool installed by script, a local backdoor account with an identical fixed
  password and an identical attacker workstation name — an operator-level match recurring across incidents
  attributed to DragonForce, Settra and Anubis. GuidePoint assesses with moderate confidence this is one
  affiliate working across those programmes and diverting payments from them; Coveware independently confirmed
  responding to at least one incident with contact from the same party.
discovered_at: "2026-08-20T04:52:00Z"
event_date: "2026-08-18"
run_id: 2026-08-20T0409Z-intel
priority: notable
immediate_action: null
tags: [ransomware, organized-crime, phishing]
regions: [global]
sectors: []
entities: [actor:ransom-busters, actor:dragonforce, actor:settra, actor:anubis-raas]
techniques: [T1046, T1567.002, T1219, T1059.001, T1136.001, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.guidepointsecurity.com/blog/beware-ransom-busters/"
    publisher: "GuidePoint Security (GRIT)"
    date: "2026-08-18"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/rogue-ransomware-affiliate-ransom-busters-poses-as-recovery-firm/"
    publisher: "BleepingComputer"
    date: "2026-08-19"
    role: corroborating
closed_sources: []
evidence:
  - quote: "GRIT assesses with moderate confidence that “Ransom Busters” is not a bona fide third-party victim services firm, but rather a single ransomware affiliate with employment across multiple RaaS operations, using their affiliate access to divert ransom payment discussions away from the original ransomware operation."
    publisher: "GuidePoint Security (GRIT)"
  - quote: "We observed this behavior while responding to incidents from threat groups including DragonForce, Settra and Anubis."
    publisher: "GuidePoint Security (GRIT)"
verification: multi-source
sourcing_note: >
  The identity conclusion is explicitly an assessment at moderate confidence, and this entry carries it as one.
  The observed facts beneath it — the outreach pattern, the sums demanded, the artefact overlap across incidents
  — are reported by GuidePoint as directly observed during its own incident response. GuidePoint did not verify
  the actor's claim to have compromised any ransomware operation's administrative panel; it observed only that
  the actor could demonstrate knowledge of the same stolen dataset the affiliate held. BleepingComputer supplies
  independent corroboration from a second incident-response firm, Coveware, which responded to at least one
  incident involving contact from the same party. Neither source names a victim, a sector or a region, and
  neither reports any victim having paid Ransom Busters.
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

An entity styling itself Ransom Busters has been emailing organisations in the middle of a ransomware incident, writing to addresses at the victim's own domain and asking to be put in touch with the chief executive or IT leadership ([GuidePoint Security, 2026-08-18](https://www.guidepointsecurity.com/blog/beware-ransom-busters/)). It presents itself as a project that assists victims of cyberattacks, claims to have held unauthorised access to criminal groups' servers for more than three years, says it has found the victim's stolen data on one of those servers, and offers to return the files, destroy the attackers' backups and — because it claims access to the operation's key storage — help restore encrypted data. The fee is $20,000 to $60,000 to delete the stolen data from the ransomware group's servers.

The property that separates this from ordinary ambulance-chasing is when it arrives. GuidePoint notes that legitimate recovery-service solicitation generally follows an attack becoming public knowledge; this outreach lands before the incident is publicly known at all, which means the sender knew about an intrusion nobody had disclosed ([GuidePoint Security, 2026-08-18](https://www.guidepointsecurity.com/blog/beware-ransom-busters/)). Responding to two of these incidents, GuidePoint's teams found the same set of artefacts in both victim environments: one network-scanning utility used for internal reconnaissance, one cloud-object-storage command-line tool used to move data out to attacker-controlled cloud storage, one remote-monitoring-and-management tool installed through a PowerShell script as a secondary access channel, a locally created backdoor account whose password was identical in both intrusions, and an identical attacker-controlled workstation name appearing in both. GuidePoint weighed and rejected the obvious innocent explanation — a standardised affiliate playbook or a shared virtual-machine image distributed inside one programme — because the same overlap recurred across incidents belonging to *different* ransomware operations, which makes it a fingerprint of an operator rather than of a programme. On that basis it assesses with moderate confidence that Ransom Busters is a single affiliate employed across several operations, using affiliate-level access to divert ransom negotiations away from the operation it is working for, and states it observed the behaviour while responding to incidents involving DragonForce, Settra and Anubis ([GuidePoint Security, 2026-08-18](https://www.guidepointsecurity.com/blog/beware-ransom-busters/)).

A second incident-response firm has seen the same thing independently. Coveware confirmed to BleepingComputer that it responded to at least one incident involving contact from the same group or individual, and its senior director of incident response drew the same distinction — that what makes this different from a routine recovery-service pitch is the approach to a victim whose incident was not yet public ([BleepingComputer, 2026-08-19](https://www.bleepingcomputer.com/news/security/rogue-ransomware-affiliate-ransom-busters-poses-as-recovery-firm/)). No victim is reported to have paid Ransom Busters; in one incident the victim paid the underlying ransomware operator instead.

**Defender takeaway:** during a ransomware incident, unsolicited inbound contact is part of the incident and belongs in the evidence, not in the inbox of whoever received it. A message offering to recover or delete data for a fee, arriving before anything is public, is a claim of foreknowledge that only a participant can honestly make — so it should be preserved, routed to the incident lead and treated as adversarial communication, not evaluated as a vendor proposal by an executive acting alone. Paying it buys nothing that can be verified: GuidePoint's own guidance is that no criminal party's promise to delete stolen data can be relied on, and retention for later re-extortion is a documented pattern. **Triage:** legitimate recovery and negotiation firms are retained *by* the victim, normally through counsel or an existing incident-response contract, and they approach victims — if at all — only once an incident is public; the discriminators are the direction of first contact, the pre-disclosure timing, and a claim of standing access to the attacker's own infrastructure, which no lawful firm would advertise. For hunt teams, GuidePoint's reasoning is reusable in its own right: the co-occurrence of an internal network scanner, a cloud-storage exfiltration utility, a script-installed remote-management agent and a freshly created local account across two nominally unrelated ransomware cases is a signal that the same operator worked both, whatever brand claimed the victims.
