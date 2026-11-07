---
schema: 1
kind: threat
title: "Phishing lures sent as ICS calendar invites land in Outlook and Gmail calendars without a click and stay after the email is deleted; EvilTokens used them for Microsoft 365 device-code phishing"
headline: "Calendar-invite phishing spreads: Outlook and Gmail add the lure on their own and keep it after the email is deleted"
summary: >
  Netcraft reports that phishing lures delivered as ICS calendar files, adopted by widespread campaigns of the EvilTokens
  Microsoft 365 token-stealing kit, are now spreading to low-effort scams. Outlook with Exchange Online (desktop, web and
  mobile) and Gmail with Google Calendar add such an invite to the calendar automatically as tentative and keep it after
  the email is deleted, so purging the message leaves the lure in place. EvilTokens invites posed as meetings, alerts or
  voicemail and led to a device-code page that has the victim authorise an attacker's device through OAuth; Sublime
  Security, quoted by The Guardian, reports exponential growth in calendar phishing.
discovered_at: "2026-10-19T21:15:00Z"
updated_at: null
event_date: "2026-10-16"
run_id: 2026-10-18T1307Z-audit
priority: notable
immediate_action: null
tags: [phishing, identity]
regions: [global]
sectors: [public-sector, technology]
entities: ["tool:eviltokens", "product:microsoft-outlook", "product:microsoft-exchange-online", "product:google-calendar", "product:microsoft-365", "product:google-workspace"]
techniques: [T1566.001, T1204.001, T1528]
affected_products: ["Microsoft Outlook", "Microsoft Exchange Online", "Google Calendar"]
cves: []
sources:
  - url: "https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way"
    publisher: "Netcraft"
    date: "2026-10-16"
    role: primary
  - url: "https://www.theguardian.com/money/2026/oct/11/calendar-phishing-scam-meeting-renewal-google-microsoft-paypal"
    publisher: "The Guardian"
    date: "2026-10-11"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Threat actors are using ICS calendar invite files to bypass email security filters and often achieve persistence in targets’ calendars even after the original email is deleted."
    publisher: "Netcraft"
    source_url: "https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way"
  - quote: "Security teams may wish to review their default email client settings to ensure that employees who should not expect invites from outside of the organization would not have those automatically added to their calendars."
    publisher: "Netcraft"
    source_url: "https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way"
  - quote: "Calendar apps, such as Google Calendar, can add invitations automatically without users even accepting them"
    publisher: "The Guardian"
    source_url: "https://www.theguardian.com/money/2026/oct/11/calendar-phishing-scam-meeting-renewal-google-microsoft-paypal"
verification: multi-source
sourcing_note: >
  Netcraft's own collection is the source for the technique, the client behaviour matrix and the EvilTokens link; The
  Guardian independently quotes Sublime Security and Cofense on the same lure type and its growth. No source gives
  victim counts, and the fake Microsoft, Google and PayPal campaigns The Guardian describes are not confirmed to be
  EvilTokens.
confidence: medium
references:
  - 2026-07-10/m365-conditional-access-gaps-railway-lshiy-campaigns
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

Netcraft reports that attackers send phishing lures as ICS calendar files because the "text/calendar" type is treated as low risk by major email clients, and that the mail client's normal invite handling then places the lure in the victim's calendar with no user interaction, often keeping it there after the original email is deleted ([Netcraft, 2026-10-16](https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way)). In Netcraft's client table, Outlook desktop, Outlook on the web and Outlook Mobile with Exchange Online and Gmail with Google Calendar add the event automatically, mark it tentative and keep it after the email is deleted, Apple Calendar connected to Exchange Online often does the same, and Apple Mail with iCloud does not add it ([Netcraft, 2026-10-16](https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way)).

Campaigns using the EvilTokens toolkit, which steals Microsoft 365 tokens, used ICS invites disguised as meetings, alerts or voicemail notifications; the link leads to a page that gives the user a device code and tells them to enter it on Microsoft's device authorization page, which grants an attacker's device access to the account through OAuth ([Netcraft, 2026-10-16](https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way)). Netcraft now also sees smaller scams carrying ordinary phishing content inside ICS files ([Netcraft, 2026-10-16](https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way)). Sublime Security reports "exponential growth" in calendar phishing, with lures such as voicemail notices, payment receipts and renewal warnings that link to fake Microsoft, Google or PayPal logins or give a phone number, and Cofense says some senders use legitimate platforms such as Zoom to send the invitations, so filtering those platforms would also block real meetings ([The Guardian, 2026-10-11](https://www.theguardian.com/money/2026/oct/11/calendar-phishing-scam-meeting-renewal-google-microsoft-paypal)).

**Exposure:** users of Outlook with Exchange Online and of Gmail with Google Calendar, whose clients add external invites to the calendar on their own ([Netcraft, 2026-10-16](https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way)).

**Detection:** Netcraft names no telemetry; from the delivery path it describes, the traces are inbound external messages carrying a calendar part or ICS attachment in mail-flow logs, tentative events from external organizers the user never accepted in calendar audit logs, and, for the EvilTokens variant, a device-code sign-in to the account shortly after such an event ([Netcraft, 2026-10-16](https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way)). When responding to a reported phish of this kind, remove the calendar entry as well as the email, because the entry persists after the email is deleted ([Netcraft, 2026-10-16](https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way)).

**Defender takeaway:** treat email-attached invites as part of the phishing attack surface: review whether the mail client settings add invites from outside the organization automatically for staff who do not expect them, and extend phishing guidance and purge procedures to calendar entries for those who do ([Netcraft, 2026-10-16](https://www.netcraft.com/blog/how-attackers-get-into-your-calendar-the-easy-way)).
