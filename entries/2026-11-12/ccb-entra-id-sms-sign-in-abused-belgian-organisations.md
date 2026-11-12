---
schema: 1
kind: threat
title: "Belgium's CCB warns that attackers abused Microsoft Entra ID SMS first-factor sign-in (phone number and one-time code, no password) to compromise several Belgian organisations; turning off 'Use for sign-in' is the priority step"
headline: "CCB: attackers signed in to Entra ID with an SMS code alone; turn off SMS first-factor sign-in"
summary: >
  Belgium's Centre for Cybersecurity warned on 2026-11-10 that a trusted partner observed successful attacks against multiple Belgian organisations in which attackers abused Microsoft Entra ID SMS first-factor sign-in, where a phone number and a one-time code replace the password. The warning gives no victim count, actor, date range or attack chain and says nothing on how the codes were obtained; the CCB's priority step is to find who uses SMS sign-in, give them an alternative and disable it.
discovered_at: "2026-11-12T04:03:00Z"
updated_at: null
event_date: "2026-11-10"
run_id: 2026-11-12T0255Z-intel
priority: notable
immediate_action: null
tags: [identity, cloud]
regions: [europe]
sectors: []
entities: []
techniques: [T1078.004]
affected_products: ["Microsoft Entra ID"]
cves: []
sources:
  - url: "https://ccb.belgium.be/advisories/warning-multiple-belgian-organisations-compromised-through-sms-sign-disable-sms-first"
    publisher: "Centre for Cybersecurity Belgium (CCB)"
    date: "2026-11-10"
    role: primary
  - url: "https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-sms-signin"
    publisher: "Microsoft Learn"
    date: "2026-10-30"
    role: corroborating
  - url: "https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement"
    publisher: "Microsoft Learn"
    date: "2026-09-23"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Check which users actually use SMS sign-in, give them an alternative and disable it as soon as possible"
    publisher: "Centre for Cybersecurity Belgium (CCB)"
    source_url: "https://ccb.belgium.be/advisories/warning-multiple-belgian-organisations-compromised-through-sms-sign-disable-sms-first"
  - quote: "Look for successful SMS-based sign-ins, phone number or method changes, unusual locations or devices, and follow-on activity such as mailbox rules or app consents."
    publisher: "Centre for Cybersecurity Belgium (CCB)"
    source_url: "https://ccb.belgium.be/advisories/warning-multiple-belgian-organisations-compromised-through-sms-sign-disable-sms-first"
verification: single-source-national-cert
sourcing_note: "The attack observation is the CCB's own statement, relayed from an unnamed trusted partner, and no other source reports the Belgian attacks; searches in English, Dutch and French found no independent coverage. The CCB names no victim count, sector, actor, chain or date range. The Microsoft Learn pages corroborate the method and its retirement dates, not the attacks."
confidence: medium
references:
  - 2026-11-05/vaud-m365-device-code-phishing-campaign-romandie
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "In every Microsoft Entra tenant you run or manage for others, open the Authentication methods policy for SMS, list who is enabled and who actually signs in with SMS using the Authentication methods activity report, and turn off 'Use for sign-in' (labelled 'Enable first factor sign-in' in Microsoft's how-to) for everyone who has an alternative; where it must stay for frontline workers, restrict it to that group and monitor it, because the CCB reports successful attacks against it."
updates: []
migrated_from: null
---

The Belgian Centre for Cybersecurity (CCB) warned on 2026-11-10 that a trusted partner had observed successful attacks against multiple Belgian organisations in which attackers abused Microsoft Entra ID SMS as a first factor, the sign-in mode in which a phone number and a one-time code replace the password ([CCB, 2026-11-10](https://ccb.belgium.be/advisories/warning-multiple-belgian-organisations-compromised-through-sms-sign-disable-sms-first)). The warning gives no victim count, sector, actor, date range or attack chain, and it does not say how the codes were obtained; its only statement on the factor itself is that SMS and voice can be phished, intercepted or SIM-swapped ([CCB, 2026-11-10](https://ccb.belgium.be/advisories/warning-multiple-belgian-organisations-compromised-through-sms-sign-disable-sms-first)). No other source reports the Belgian attacks. Microsoft describes the method as designed for frontline workers, advises enabling it only for them, and says it is different from SMS as a multifactor method, which needs a username and password ([Microsoft Learn, 2026-10-30](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-sms-signin)). Microsoft is disabling first-factor sign-in in tenants with no such traffic in the previous 30 days ([Microsoft Learn, 2026-10-30](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-sms-signin)) and retires its own SMS and voice delivery on 2027-02-01 for all users except Global Administrators and external users, who follow on 2027-07-01; a customer-configured telephony provider can keep the methods working ([Microsoft Learn, 2026-09-23](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement)).

**Exposure:** an Entra tenant whose SMS authentication method policy has first-factor sign-in turned on for any user or group; the CCB's path is Authentication methods, SMS, "Use for sign-in", and the Authentication methods activity report shows who actually uses it ([CCB, 2026-11-10](https://ccb.belgium.be/advisories/warning-multiple-belgian-organisations-compromised-through-sms-sign-disable-sms-first)). Microsoft's how-to calls the same setting "Enable first factor sign-in" and says that leaving it unchecked limits SMS to multifactor authentication and self-service password reset ([Microsoft Learn, 2026-10-30](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-sms-signin)).

**Detection:** in Entra sign-in logs, look for successful sign-ins that used SMS as the authentication method; in audit logs, for phone-number or authentication-method changes; then for unusual locations or devices and follow-on mailbox rules or application consents, reviewing as far back as log retention allows ([CCB, 2026-11-10](https://ccb.belgium.be/advisories/warning-multiple-belgian-organisations-compromised-through-sms-sign-disable-sms-first)).

**Defender takeaway:** disable SMS first-factor sign-in now for everyone who has an alternative and restrict it to the smallest group where it must stay, as the CCB advises; remove SMS and voice for privileged accounts only after each has a working phishing-resistant method, and avoid a blind switch-off, which can lock users out or leave them with a password alone ([CCB, 2026-11-10](https://ccb.belgium.be/advisories/warning-multiple-belgian-organisations-compromised-through-sms-sign-disable-sms-first)). Microsoft's own clearing reaches only tenants with no first-factor SMS sign-in traffic in the previous 30 days ([Microsoft Learn, 2026-10-30](https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-sms-signin)), so a tenant that uses the method stays exposed until it acts.
