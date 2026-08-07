---
schema: 1
kind: threat
horizon: operational
title: "UNC6671 kept operating after BlackFile's announced retirement, across four further extortion brands — and its vishing pretext is now an urgent order to enroll a FIDO2 passkey"
headline: "The group behind BlackFile never stopped: GTIG ties four newer extortion brands to one operator whose lure attacks passkey enrolment, not the passkey"
summary: >
  Google Threat Intelligence Group reports that UNC6671 — the actor behind the BlackFile extortion brand, whose
  retirement was announced in May 2026 — continued operating across four further brands (Redact, Pink, Helix,
  Falcon) linked by shared root domains, identical phishing templates and overlapping victim targeting. The
  intrusion chain is unchanged and identity-centric: a call to an employee's personal mobile impersonating the
  IT helpdesk, now sometimes spoofing the real helpdesk number, demanding an urgent FIDO2 passkey or MFA
  re-enrolment, into an adversary-in-the-middle panel that takes credentials and MFA tokens, then scripted bulk
  exfiltration from Microsoft 365 and Okta-fronted SaaS. Targeting narrowed by July 2026 onto financial services,
  private equity, law firms and rating agencies.
discovered_at: "2026-08-07T04:41:00Z"
event_date: "2026-08-06"
run_id: 2026-08-07T0411Z-intel
priority: high
immediate_action: null
tags: [ransomware, organized-crime, phishing, identity, cloud, data-breach]
regions: [global, us, europe]
sectors: [finance, legal-services, healthcare, manufacturing, transport, technology]
entities: ["actor:unc6671", "actor:helix-extortion"]
techniques: [T1598.004, T1566.004, T1684.001, T1557, T1556.006, T1621, T1098.005, T1078.004, T1114.002, T1530, T1213.002, T1070.008, T1090.002, T1657]
affected_products: ["Microsoft 365", "Microsoft Entra ID", "Okta"]
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/"
    publisher: "Google Threat Intelligence Group / Mandiant"
    date: "2026-08-06"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/hedge-fund-cyberattacks-tied-to-blackfile-linked-unc6671-extortion-group/"
    publisher: "BleepingComputer"
    date: "2026-08-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "These overlaps support our assessment that a common group of threat actors are affiliated with the BlackFile, Redact, Pink, Helix, and Falcon extortion brands, although other scenarios such as splintered affiliates or shared Phishing-as-a-Service infrastructure may also be plausible."
    publisher: "Google Threat Intelligence Group / Mandiant"
  - quote: "UNC6671 callers have continued to call targeted employees on their personal mobile numbers, circumventing corporate security controls."
    publisher: "Google Threat Intelligence Group / Mandiant"
  - quote: "In at least some recent cases, the threat actor has spoofed the legitimate helpdesk phone number adding an air of legitimacy."
    publisher: "Google Threat Intelligence Group / Mandiant"
  - quote: "operators systematically deleted password-reset confirmations, secondary security notifications, company-wide security alerts, and any alerts generated during modifications to account security or MFA configurations."
    publisher: "Google Threat Intelligence Group / Mandiant"
  - quote: "In over 53% of tracked cases in this timeframe, final payments averaged $750,000 USD (~10.2 BTC)."
    publisher: "Google Threat Intelligence Group / Mandiant"
  - quote: "These authenticators implement WebAuthn standard to enforce cryptographic origin binding between the authenticator and the specific domains it can authenticate to, rendering lookalike domains and AiTM proxies ineffective."
    publisher: "Google Threat Intelligence Group / Mandiant"
verification: multi-source
sourcing_note: >
  The brand linkage is GTIG's stated assessment, not a confirmed fact: GTIG names splintered affiliates and
  shared phishing-as-a-service infrastructure as plausible alternative explanations, and this entry carries it
  at that strength. The financial-sector victim characterisation is BleepingComputer relaying Reuters and
  Bloomberg; GTIG's own report names no victims. Ransom figures cover 2026-01-07 to 2026-05-12 and are GTIG's blockchain analysis
  of BlackFile-attributed wallets.
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: identity-infra
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Gate new authenticator and passkey enrolment behind out-of-band identity proofing that does not run over the phone channel the request arrives on — this actor's entire initial access depends on an employee completing an enrolment during an unsolicited call, and origin-bound FIDO2 does not defend the enrolment step itself."
migrated_from: null
---

The retirement of a ransomware brand is a press release, not an outcome. Google Threat Intelligence Group reports that UNC6671, the actor behind the BlackFile extortion brand whose shutdown was announced in May 2026, went on operating and diversified across four further extortion fronts — Redact, Pink, Helix and Falcon — with the intrusion tradecraft essentially untouched ([GTIG / Mandiant, 2026-08-06](https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/)). The linkage is an assessment rather than a certainty, and GTIG says so: overlapping victim targeting across brands "support our assessment that a common group of threat actors are affiliated with the BlackFile, Redact, Pink, Helix, and Falcon extortion brands, although other scenarios such as splintered affiliates or shared Phishing-as-a-Service infrastructure may also be plausible" ([GTIG / Mandiant, 2026-08-06](https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/)). The evidentiary basis is infrastructure economics: rather than isolating infrastructure per victim, the operator reuses generic root domains across many targets and appends victim-name subdomains, so one root domain used against a Falcon-extorted organisation was simultaneously used against a Helix-extorted one — and the same phishing templates, identical in code and design, were served from several of those domains at once.

**The lure is the important change, and it inverts the standard advice.** The pretext is an urgent helpdesk mandate to enable FIDO2 passkeys or update MFA enrolment, delivered by a caller who reaches the employee on their personal mobile — GTIG records that "UNC6671 callers have continued to call targeted employees on their personal mobile numbers, circumventing corporate security controls", and that "in at least some recent cases, the threat actor has spoofed the legitimate helpdesk phone number adding an air of legitimacy" ([GTIG / Mandiant, 2026-08-06](https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/)). Root domains pair authentication vocabulary — passkey, mfa, sso — with a verb, so the destination reads as an enrolment portal. GTIG's own hardening guidance names phishing-resistant authenticators as the durable control, because "these authenticators implement WebAuthn standard to enforce cryptographic origin binding between the authenticator and the specific domains it can authenticate to, rendering lookalike domains and AiTM proxies ineffective" ([GTIG / Mandiant, 2026-08-06](https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/)). The operational catch is that origin binding protects an authenticator that already exists; this actor attacks the moment one is *created*. A defender who has deployed passkeys and considers the identity problem closed has hardened the authentication step and left the enrolment step as the way in.

Post-compromise, the chain is deliberately quiet. With session persistence established, the operator uses compromised mailboxes to trigger password resets on non-SSO enterprise applications, then blinds the victim: GTIG records that "operators systematically deleted password-reset confirmations, secondary security notifications, company-wide security alerts, and any alerts generated during modifications to account security or MFA configurations" ([GTIG / Mandiant, 2026-08-06](https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/)). Exfiltration is scripted rather than hands-on-keyboard, pulling data from Microsoft 365 and other SaaS stores at machine rates. GTIG characterises the operation as data-theft extortion throughout and no cited source describes an encryption stage; the leverage on the evidence published is publication.

Targeting has moved deliberately upmarket. Between April and May 2026 the domains were aimed broadly at large enterprises in manufacturing, real estate, healthcare and insurance; in June the focus shifted to technology, transportation and hospitality; and "by July 2026, the target profile narrowed to focus on the financial and legal sectors, with observed infrastructure directed at private equity firms, law firms, and financial rating agencies" ([GTIG / Mandiant, 2026-08-06](https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/)) — organisations holding merger, capital-deployment and litigation material, which is leverage rather than data. Operational tempo rose with it, to "an accelerated cadence of approximately one domain every 1.6 days" across June and July against one every 2.2 days in the preceding two months ([GTIG / Mandiant, 2026-08-06](https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/)). BleepingComputer, relaying Reuters and Bloomberg, reports that recent targets in this financial-sector phase include several large US hedge funds and private-equity firms; GTIG names no victims itself ([BleepingComputer, 2026-08-06](https://www.bleepingcomputer.com/news/security/hedge-fund-cyberattacks-tied-to-blackfile-linked-unc6671-extortion-group/)).

The economics explain why announced retirements mean nothing. GTIG reviewed 18 BlackFile Bitcoin wallet addresses receiving 141.65 BTC — roughly $10.69 million at transaction time — between 2026-01-07 and 2026-05-12, with payments continuing past the 2026-05-11 shutdown notice and significant cash-out events in late April and early May. Initial demands run from $1 million to upwards of $3 million, negotiated down by 50% to 75%, and "in over 53% of tracked cases in this timeframe, final payments averaged $750,000 USD (~10.2 BTC)" ([GTIG / Mandiant, 2026-08-06](https://cloud.google.com/blog/topics/threat-intelligence/unc6671-targets-financial-services-and-enterprise-cloud-environments/)). GTIG's read is that the multi-brand structure most likely compartmentalises operations, hides total breach volume and isolates negotiation fallout — which is why brand-based tracking misleads and TTP-based tracking does not.

**Defender takeaway:** treat identity-provider enrolment as a privileged operation with its own out-of-band proofing, because every control this actor defeats sits downstream of enrolment. GTIG's detection guidance is directly implementable and telemetry-class first: in identity-provider audit records, look for MFA or passkey registration events immediately preceded by authentication failures or abandoned push challenges — the residue of a caller walking a victim through a re-enrolment after the original factor failed; and in SaaS unified audit telemetry, treat file-access events with the same criticality as file-download events when the user-agent string identifies a scripting library or when access volume exceeds human browsing rates, since this actor's exfiltration is scripted. Session controls that force re-authentication at least daily, device-bound session credentials or IP session binding, restriction of authentication to known network zones, and conditional-access alerting on sign-ins from commercial VPN and residential-proxy ranges each remove part of the post-AiTM window. **Triage:** legitimate self-service MFA re-enrolment produces the same registration event as this attack, so the registration alone is not the signal — the discriminators are a preceding failed or abandoned challenge, an enrolment the service desk has no ticket for, and, downstream, bulk SaaS reads from the same principal within a short window; any one of these is weak on its own, and the sequence is what distinguishes an intrusion from an employee replacing a lost phone.
