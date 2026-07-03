---
schema: 1
kind: threat
horizon: operational
title: "\"Signal Support\" impersonation phishing harvests cloud-backup recovery keys from high-value users"
headline: "\"Signal Support\" impersonation phishing harvests cloud-backup recovery keys from high-value users"
summary: "A phishing wave is impersonating \"Signal Support\" to trick high-value users into pasting their cloud-backup recovery key into the chat — defeating the end-to-end encryption protecting the historical message archive (TechCrunch, 2026-05-28). Pure social engineering; the lure exploits fear of data loss. Signal never initiates contact and never asks for a recovery key, PIN or registration code."
discovered_at: "2026-05-31T05:00:01Z"
event_date: 2026-05-29
run_id: 2026-05-31-d742bed9
priority: high
immediate_action: null
tags:
  - phishing
  - identity
  - mobile
regions:
  - global
sectors:
  - public-sector
  - media
entities: []
cves: []
sources:
  - url: "https://techcrunch.com/2026/05/28/hackers-are-trying-to-steal-signal-users-backups-in-new-wave-of-phishing-attacks/"
    publisher: TechCrunch
    role: primary
  - url: "https://www.malwarebytes.com/blog/news/2026/05/signal-users-targeted-in-backup-stealing-phishing-attacks"
    publisher: Malwarebytes Labs
    role: corroborating
closed_sources: []
evidence:
  - quote: "A new hacking campaign is trying to trick Signal users to give up their secret recovery key, which can be used to access online backups containing past messages"
    publisher: TechCrunch
  - quote: "Signal says it 'will never reach out' to users first, and will never ask for their registration code, PIN, or recovery key"
    publisher: Malwarebytes
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-31.md
---

A phishing campaign first reported on 2026-05-28 impersonates Signal's support team, warning targets that their cloud-backed chats are "at risk of permanent loss due to a sync issue" and instructing them to retrieve their Signal cloud-backup recovery key from the app and paste it into the conversation ([TechCrunch, 2026-05-28](https://techcrunch.com/2026/05/28/hackers-are-trying-to-steal-signal-users-backups-in-new-wave-of-phishing-attacks/); [Malwarebytes, 2026-05-29](https://www.malwarebytes.com/blog/news/2026/05/signal-users-targeted-in-backup-stealing-phishing-attacks)). Signal cloud backups are end-to-end encrypted with that recovery key: without it, an attacker who separately hijacks the victim's phone number (SIM-swap or SS7 abuse) can intercept only future messages, while the historical archive of conversations, photos and documents stays sealed. Surrendering the key unlocks that archive. The technique is pure social engineering (`T1598` spearphishing for information / `T1566`) with no exploit component; reporting notes targeting consistent with anti-CCP activists, but both outlets stress the lure is reusable by any actor against secure-messaging users — a population heavily represented among government officials, lawyers, journalists and civil-society staff.

**Why it matters to us:** Signal is widely used inside Swiss and European public-sector bodies and by the journalists and civil-society contacts they work with for sensitive communications. The attack bypasses transport encryption entirely by going after the backup key, so MDM and message-content controls do not help. Defender takeaway: brief high-value users that Signal Support never initiates contact and never asks for a recovery key, PIN or registration code; pair this with carrier-side SIM port-freeze / number-lock for principals, since phone-number hijacking is the prerequisite for full account takeover even without the key.
