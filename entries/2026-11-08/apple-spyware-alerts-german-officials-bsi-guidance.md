---
schema: 1
kind: policy
title: "Apple's mercenary-spyware threat notifications of late October reached Bundestag members and federal-government staff in Germany; BSI tells recipients to treat the iPhone as possibly compromised, update, keep Lockdown Mode on and consider replacing the device; no actor or vector is public"
headline: "Apple spyware alerts reached German MPs and ministry staff; BSI: assume the iPhone may be compromised"
summary: >
  Apple has sent a new round of mercenary-spyware threat notifications to users in 99 countries since 2026-10-29, and Germany's BSI says Bundestag members and other public figures are among the
  recipients; the digital minister said members of the federal government were also warned. BSI tells recipients to assume the device may be compromised, to update iOS at once unless a forensic
  analysis is intended, to keep Lockdown Mode on permanently and to consider replacing the device where the risk looks high; neither Apple nor BSI names an actor, a spyware vendor or an infection vector.
discovered_at: "2026-11-08T03:29:00Z"
updated_at: null
event_date: "2026-10-29"
run_id: 2026-11-08T0256Z-intel
priority: notable
immediate_action: null
tags: [mobile, policy]
regions: [dach, europe]
sectors: [public-sector]
entities: ["campaign:apple-mercenary-spyware-threat-notifications-2026-10"]
techniques: []
affected_products: ["Apple iOS"]
cves: []
sources:
  - url: "https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Buero/Apple_Mercenary-Spyware/apple_mercenary-spyware_node.html"
    publisher: "BSI (Bedrohungsbenachrichtigungen von Apple zu Mercenary Spyware, translated from German)"
    date: "2026-11-02"
    role: primary
  - url: "https://therecord.media/apple-warns-users-99-countries-mercenary-spyware"
    publisher: "The Record"
    date: "2026-11-02"
    role: corroborating
  - url: "https://therecord.media/german-officials-among-apple-spyware-warning-recipients"
    publisher: "The Record"
    date: "2026-11-03"
    role: corroborating
  - url: "https://www.euronews.com/2026/11/02/german-mps-and-ministers-warned-iphones-have-been-targeted-by-spyware"
    publisher: "Euronews"
    date: "2026-11-02"
    role: corroborating
  - url: "https://support.apple.com/en-us/102174"
    publisher: "Apple Support (About Apple threat notifications)"
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Apple has begun sending a new round of threat notifications to victims of suspected mercenary spyware attacks located in nearly 100 countries"
    publisher: "The Record"
    source_url: "https://therecord.media/apple-warns-users-99-countries-mercenary-spyware"
  - quote: "Apple threat notifications never ask the user to click any links, open files, install apps or profiles, or provide an Apple Account password or verification code by email or on the phone."
    publisher: "Apple Support"
    source_url: "https://support.apple.com/en-us/102174"
verification: multi-source
sourcing_note: >
  BSI is the primary source for the German recipients and the guidance; The Record and Euronews relay the notification text, the minister's statement and Der Spiegel's report of ministry staff and
  journalists among the recipients. No source lists the 99 countries, so Swiss recipients are neither confirmed nor excluded, and whether any notified device was infected is unknown to BSI. BSI's public page says
  to treat the device as possibly compromised and to consider replacing it where the risk is rated high, while The Record, relaying the digital minister on BSI's letter to members, says recipients were told to assume
  infection and replace the device immediately.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Apple has sent a new round of threat notifications to suspected mercenary-spyware targets in 99 countries, according to a notification screenshot posted by the researcher Costin Raiu, who says he verified several victims' notices ([The Record, 2026-11-02](https://therecord.media/apple-warns-users-99-countries-mercenary-spyware)). Germany's BSI says several Bundestag members and other public figures have received it since 2026-10-29, that it does not know whether the alerts mean actual compromise or only attempted attacks, and that it wrote to the members on 2026-10-30 (translated from German) ([BSI, 2026-11-02](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Buero/Apple_Mercenary-Spyware/apple_mercenary-spyware_node.html)). Germany's digital minister confirmed that members of the federal government were also warned ([Euronews, 2026-11-02](https://www.euronews.com/2026/11/02/german-mps-and-ministers-warned-iphones-have-been-targeted-by-spyware)), and The Record, citing Der Spiegel, reports that staff of federal ministries, lawmakers and journalists travelling with the Chancellor in Asia were among the recipients ([The Record, 2026-11-03](https://therecord.media/german-officials-among-apple-spyware-warning-recipients)). Apple attributes nothing to any actor or region ([Apple, 2026-08-13](https://support.apple.com/en-us/102174)), and neither Apple nor BSI has named a spyware vendor or an infection vector. BSI notes that mercenary spyware is generally assumed to infect devices without any action by the user, for example through a prepared message that need not be opened, and that a compromised device exposes messages including those in encrypted messengers, calls, contacts, calendar, location, camera and microphone ([BSI, 2026-11-02](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Buero/Apple_Mercenary-Spyware/apple_mercenary-spyware_node.html)).

BSI's guidance for a recipient: assume the device may be compromised; update the operating system at once unless a forensic analysis is intended; keep Lockdown Mode on permanently, also on a new device, noting that it hampers new attacks but does not remove an existing infection; where the risk looks high, consider replacing the device, resetting every account used on it and changing the phone number; then set a new device passcode, change the Apple Account and mail passwords, re-enrol authenticator apps instead of transferring them, enable Signal's registration lock and WhatsApp's two-step verification with new PINs, remove linked devices nobody recognises, and report the notification to BSI's service centre ([BSI, 2026-11-02](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Buero/Apple_Mercenary-Spyware/apple_mercenary-spyware_node.html)).

**Exposure:** Apple sends these notifications to individuals it judges to have been individually targeted, "likely because of who they are or what they do", and names politicians and diplomats among the usual targets ([Apple, 2026-08-13](https://support.apple.com/en-us/102174)); a recipient confirms authenticity on the lock screen, in Settings, in the e-mail to the Apple Account address and in the banner at account.apple.com after signing in ([Apple, 2026-08-13](https://support.apple.com/en-us/102174)).

**Detection:** Apple relies solely on its own threat intelligence and says it cannot say what causes a notification ([Apple, 2026-08-13](https://support.apple.com/en-us/102174)), and BSI's guidance names no artefact to check, so the organisational signal is a recipient reporting the notification; unusual device behaviour such as frequent crashes or fast battery drain is the only on-device hint BSI mentions ([BSI, 2026-11-02](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Buero/Apple_Mercenary-Spyware/apple_mercenary-spyware_node.html)).

**Triage:** a genuine notification never asks to click a link, open a file, install an app or profile, or give a password or verification code; a message that does is a phishing imitation, and the recipient should open account.apple.com directly in the browser instead ([Apple, 2026-08-13](https://support.apple.com/en-us/102174)).

**Defender takeaway:** give people who are plausible targets the authenticity check above and a named internal reporting path, and keep a replace-device-and-reset-accounts procedure that follows BSI's order; a recipient updates iOS at once unless a forensic analysis is intended, considers Lockdown Mode and keeps it on permanently once enabled, and considers replacing the device where the risk is rated high, treating it as possibly compromised until then.
