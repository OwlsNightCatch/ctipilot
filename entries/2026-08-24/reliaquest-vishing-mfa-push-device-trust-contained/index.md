---
schema: 1
kind: incident
title: "An MDR vendor denies a circulating compromise claim and publishes what actually happened: a phone-call phishing attempt that got one MFA push approved, and a device-trust policy that made the resulting session useless"
headline: "ReliaQuest denies a compromise claim and documents a vishing call that got one MFA push approved — device-trust binding is what capped it"
summary: >
  ReliaQuest published an account on 2026-08-23 stating that claims it had been compromised or hit by ransomware
  are false, and describing what it says actually happened: an attacker registered a lookalike domain, stood up a
  fake single-sign-on page behind a content delivery network, and cold-called multiple employees while impersonating
  a named member of its own security staff. One employee entered a password and approved the resulting MFA push,
  giving the attacker a brief session on the identity dashboard — which ReliaQuest says was view-only, because a
  device-trust policy blocked every attempt to reach applications from an unmanaged device regardless of a
  successful sign-in. The transferable finding is that control boundary and the log sequence it produces: an
  authentication that succeeds while every downstream authorisation fails on device state.
discovered_at: "2026-08-24T09:17:00Z"
event_date: "2026-08-22"
run_id: 2026-08-24T0410Z-intel
priority: notable
immediate_action: null
tags: [phishing, identity]
regions: [global]
sectors: [technology]
entities:
  - incident:reliaquest-social-engineering-attempt-2026-08
techniques: [T1566.004, T1684.001, T1583.001, T1621, T1078.004]
affected_products: []
cves: []
sources:
  - url: "https://reliaquest.com/blog/threat-spotlight-social-engineering-attempt-against-reliaquest-what-we-found"
    publisher: "ReliaQuest"
    date: "2026-08-23"
    role: primary
closed_sources: []
evidence:
  - quote: "Claims that ReliaQuest was compromised or targeted by ransomware are false."
    publisher: "ReliaQuest"
  - quote: "One teammate entered their password and approved the push notification on their phone."
    publisher: "ReliaQuest"
  - quote: "The extent of the access was view only."
    publisher: "ReliaQuest"
verification: single-source-victim
sourcing_note: >
  Single-source under the victim's-own-disclosure carve-out: every fact here is ReliaQuest's account of its own
  incident, and no independent party has examined it. One limit is deliberate and shaped this entry. A claim that
  ReliaQuest had been compromised was circulating when it published — the article states plainly that such claims
  are false, after setting out its investigation findings rather than as its opening line — but it never describes
  the claim, its origin, its contents or its date, so this entry does not either. Nothing about a leak-site listing, an extortion brand, screenshots or data samples is asserted here,
  because the only source cited would not bear it; the earlier draft of this entry did assert those specifics and
  they were removed. ReliaQuest names no actor for the attempt it describes, so no actor is linked. Note also that
  the attempted enrolment of a new authenticator appears in the article only as an element of the industry playbook
  ReliaQuest says this attempt is consistent with, not as a recorded step of this incident — the body reflects that
  distinction rather than reporting it as an observed action — and `techniques[]` does not map device
  registration for the same reason, because the mapping surface must not assert what the prose de-asserts.
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

ReliaQuest published an account of a security incident on 2026-08-23 ([ReliaQuest, 2026-08-23](https://reliaquest.com/blog/threat-spotlight-social-engineering-attempt-against-reliaquest-what-we-found)). It describes a social-engineering attempt against the company, sets out what its investigation found, and then states flatly that "Claims that ReliaQuest was compromised or targeted by ransomware are false" — so something to that effect was evidently circulating. The article never describes that claim: not where it came from, what it asserted, or what it offered as proof. Neither does this entry. What it does describe is the attempt, and the interesting part is where that attempt stopped.

Per that account, on 22 August 2026 an attacker registered a lookalike domain, stood up a counterfeit single-sign-on page fronted by a content delivery network, and then **cold-called multiple ReliaQuest employees**, each time impersonating a named member of ReliaQuest's own security staff, to steer the target toward the fake page. "One teammate entered their password and approved the push notification on their phone," which handed the attacker a session on the identity dashboard. "The extent of the access was view only." ReliaQuest states the attacker then made further attempts to move from that dashboard into business applications and was consistently denied by security controls — specifically a device-trust policy that blocks any device the organisation does not manage from reaching applications or systems, **regardless of a successful identity-provider sign-in**. Containment terminated the session, expired the compromised password and reset every authentication factor on the account. Its investigation — described as a complete audit of control fidelity, device trust, on-network access and any suspicious subsequent activity in the preceding 48 hours, so a lookback window rather than a statement about how long the work took — found no other identities accessed, no business applications reached, no customer or company data reached beyond that one user's login credentials, and no persistence established.

ReliaQuest then places the episode in a wider pattern rather than claiming novelty for it, and the distinction matters for what a reader should take as observed: the playbook it says this is consistent with across the industry runs an impersonation call, a throwaway lookalike domain registered and burned within the hour, a harvesting page behind a content delivery network, MFA push abuse, and a rapid attempt to enrol a new authenticator. The authenticator-enrolment step is named there, as part of the pattern — the article does not record it as a step the attacker took in this case, and it should not be read as one.

**Defender takeaway:** the transferable lesson is a control boundary, not a technique. Multi-factor authentication did not stop this — it was satisfied, by a real user approving a real push — and what did was treating a successful identity-provider sign-in as necessary but not sufficient, with a separate managed-device requirement in front of every business application. For a public-sector or critical-infrastructure identity estate that is a concrete question to put to its own configuration: after a valid sign-in from an unrecognised device, what is actually reachable? If the answer is "the application portfolio", then push-approval phishing is a full compromise rather than a contained one. The secondary lesson is about the phone as a channel: the impersonation was of a *named internal security staff member*, which is worth carrying into awareness content because it defeats the usual heuristic that internal support never calls out of the blue — this caller had done the homework to sound like a colleague.

**Triage:** the high-fidelity signal in identity-provider audit logs is a *sequence*, not an event: a successful primary authentication and MFA-push approval, followed within the same session by repeated application-access denials keyed to device compliance or device trust. Authentication succeeding while every downstream authorisation fails on device state is a far better phishing indicator than the sign-in alone, because a legitimate user on a managed device does not generate it — and it is a pattern worth building a rule on precisely because it fires on the successful phish rather than on the attempt. Because the harvesting domain in this case was registered and burned inside an hour, domain-age and reputation signals are unlikely to be the thing that catches the next one; the identity-side sequence is.
