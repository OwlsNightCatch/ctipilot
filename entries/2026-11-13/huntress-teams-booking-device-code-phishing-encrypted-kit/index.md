---
schema: 1
kind: threat
title: 'Device-code phishing disguised as a Microsoft Teams meeting booking: Huntress traces an October intrusion from a spear-phish through a Microsoft Safe Links-wrapped Google share link to a scheduler page whose ''Booking Reference'' is the device code, an in-browser decrypted kit that restarts the flow when MFA is required, and a token replayed through a residential proxy'
headline: 'Huntress: device-code phishing posing as a Teams booking skips URL reputation checks; hunt Cmsi:Cmsi sign-ins'
summary: Huntress describes a mid-October 2026 intrusion in which a spear-phish impersonating a company executive led, through a Safe Links-wrapped Google share link that sidestepped URL reputation checks, to a fake Microsoft Teams meeting scheduler whose 'Booking Reference' is a Microsoft device code, with a phishing kit shipped as AES-256-GCM ciphertext that the browser decrypts and a fallback that restarts the device-code session when MFA is required. The account had no MFA enrolled and the captured session was replayed from a residential proxy, showing as a device-code (Cmsi:Cmsi) sign-in followed by programmatic user agents; Huntress names no victim country and no Swiss link.
discovered_at: '2026-11-13T04:07:00Z'
updated_at: null
event_date: '2026-11-12'
run_id: 2026-11-13T0256Z-intel
priority: notable
immediate_action: null
tags:
  - phishing
  - identity
regions:
  - global
sectors: []
entities:
  - product:microsoft-365
techniques:
  - T1566.002
  - T1204.001
  - T1528
  - T1078.004
  - T1027.013
  - T1090
  - T1583.001
  - T1608.005
  - T1550.004
  - T1539
  - T1557
  - T1684.001
affected_products:
  - Microsoft Entra ID
cves: []
sources:
  - url: https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing
    publisher: Huntress
    date: '2026-11-12'
    role: primary
closed_sources: []
evidence:
  - quote: This booking reference is the device code.
    publisher: Huntress
    source_url: https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing
  - quote: To an email scanner or crawler that doesn't run JavaScript, the lure page is just an encrypted blob.
    publisher: Huntress
    source_url: https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing
  - quote: The captured session was replayed from attacker infrastructure; the ASN and region changed inside the same session ID.
    publisher: Huntress
    source_url: https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing
verification: single-source
sourcing_note: Huntress is the only source, reporting first-hand SOC telemetry on one contained incident; it names no victim, country or scale and does not link the case to the device-code campaign in French-speaking Switzerland. Its ATT&CK table says the account had no MFA enrolled, while the kit has an MFA-required fallback; whether the fallback fired in this incident is not stated. Domains, the share-link identifier and other indicators are deliberately not carried.
confidence: medium
references:
  - 2026-11-05/vaud-m365-device-code-phishing-campaign-romandie
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

In mid-October a Huntress SOC saw an employee of a construction company receive a spear-phishing email from a typosquatted domain impersonating another company's senior vice president; the link in the mail was wrapped by Microsoft Safe Links and pointed to a Google share link that redirected server-side to the lure page, so the mail body held the Google link and not the lure domain, which Huntress says sidestepped URL reputation checks for email security ([Huntress, 2026-11-12](https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing)). The page posed as a Microsoft Teams meeting scheduler, and behind it the backend started a Microsoft device-code sign-in; the "Booking Reference" shown to the victim is the device code, which the victim enters in a genuine Microsoft sign-in window ([Huntress, 2026-11-12](https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing)).

The kit is shipped as AES-256-GCM ciphertext that the browser decrypts, so that to an email scanner or crawler that does not run JavaScript the page is an encrypted blob; if Microsoft answers AADSTS50076 or interaction_required because MFA is required, the kit starts a new device-code session and restarts the flow ([Huntress, 2026-11-12](https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing)). After the victim finished, the attacker held a session token and the device-code login (Cmsi:Cmsi) was routed through a residential proxy; the compromised account had no MFA enrolled and was used from an unmanaged device, and Huntress contained the incident before it escalated ([Huntress, 2026-11-12](https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing)).

**Exposure:** a Microsoft 365 tenant that allows the device-code flow for users with no device that needs it, particularly accounts without MFA.

**Detection:** in Entra sign-in logs, a successful device-code authentication shown as Cmsi:Cmsi, programmatic user agents such as python-requests and node afterwards (often only in the non-interactive log), and a change of ASN and region inside the same session ID; in mail and proxy telemetry, a Google share link that redirects to a freshly registered lookalike domain ([Huntress, 2026-11-12](https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing)).

**Triage:** Huntress treats a device-code prompt that follows a link, a booking request or another unexpected interaction as suspicious, and the captured session shows up as a replay from another ASN and region within one session ([Huntress, 2026-11-12](https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing)).

**Defender takeaway:** restrict or monitor device-code authentication where it is not needed, enforce phishing-resistant MFA, and investigate unfamiliar device sign-ins from unmanaged devices, new regions or residential proxy networks ([Huntress, 2026-11-12](https://www.huntress.com/blog/crafty-microsoft-teams-booking-flow-disguises-device-code-phishing)).
