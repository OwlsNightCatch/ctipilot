---
title: "Warning: Multiple Belgian organisations compromised through SMS sign-in, disable SMS as a first factor now!"
url: https://ccb.belgium.be/advisories/warning-multiple-belgian-organisations-compromised-through-sms-sign-disable-sms-first
hostname: belgium.be
sitename: ccb.belgium.be
date: "2026-11-10"
fingerprint: a889671b1f56a7f3
---
Initiatives for

As the national authority for Cybersecurity the CCB has developed several initiatives for specific publics which are presented here.

Other information and services of the government:
                                                                
                  [www.belgium.be
                  (opens in a new tab)](https://www.belgium.be/en)
                

Image

Published : 10/11/2026

**Last update:** 10/11/2026

**Affected software:**

- Microsoft Entra ID (formerly Azure AD): SMS and voice authentication for sign-in, MFA and self-service password reset
- Other identity platforms and portals that allow SMS or voice as a first factor

**Type:** Misconfiguration

A trusted partner observed successful attacks against multiple Belgian organisations in which attackers abused Microsoft authentication with SMS as the *first* factor (phone number + one-time code, no password).

SMS and voice can be phished, intercepted or SIM-swapped, whether used as a first or a second factor. Microsoft will stop delivering SMS and voice codes in Entra ID from **1 February 2027** for most users, and from **1 July 2027** for Global Administrators and external users.

Do not switch off SMS and voice authentication blindly: users can be locked out, or left with password-only sign-in.

1. **Assess impact first.** Identify which users, groups, applications and processes rely on SMS or voice: SMS sign-in, MFA, self-service password reset, break-glass accounts, frontline or shared-device workers, external users and third-party systems. For Microsoft Entra ID, use the [Entra SMS and voice usage analyzer](https://github.com/microsoft/entra-sms-voice-usage-analyzer) for policy scope, and the Authentication methods activity report for actual usage.
2. **SMS as first factor: act with priority.** This is what attackers are abusing. Check which users actually use SMS sign-in, give them an alternative and disable it as soon as possible (in Entra: `Authentication methods → SMS → turn off "Use for sign-in"`). Until then, restrict it to the smallest possible group and monitor it closely.
3. **Remove SMS and voice from privileged accounts**, after confirming each one has a working phishing-resistant method.
4. **Deploy and test alternatives.** Roll out phishing-resistant MFA (passkeys / FIDO2), with a pilot group first. Validate sign-in, password reset, recovery and help-desk procedures before any wider rollout.
5. **Communicate, then phase out.** Inform users in advance, disable SMS and voice for MFA and password reset in phases, and monitor for lockouts and help-desk calls. Guidance: [Microsoft's SMS and voice retirement guidance](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement).
6. **Hunt.** If SMS sign-in was enabled, review sign-in and audit logs as far back as retention allows. Look for successful SMS-based sign-ins, phone number or method changes, unusual locations or devices, and follow-on activity such as mailbox rules or app consents.
7. **Report** incidents to the CCB via [the incident report form](https://ccb.belgium.be/cert/report-incident). NIS2 entities: mind your notification deadlines.
