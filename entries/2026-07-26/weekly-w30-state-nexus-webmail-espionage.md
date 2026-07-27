---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-top-stories
title: "Self-hosted webmail is a standing state-espionage battleground — this week a 16-nation advisory exposed Russia's LAUNDRY BEAR Zimbra zero-click and Proofpoint detailed a separate GRU actor's live 'half-click' zero-day supply across five webmail platforms"
headline: "Two distinct Russian actors read government mail via view-based webmail exploits that need no click — and eviction takes more than patching"
summary: >
  Two independent 2026-W30 disclosures put self-hosted webmail at the centre of Russian state email-espionage, from two distinct actors. A joint advisory (AA26-204A) co-sealed by agencies from 16 nations attributes a sustained campaign against Zimbra Collaboration Suite to LAUNDRY BEAR (Void Blizzard / TA488), abusing the view-based stored-XSS CVE-2025-66376 that fires when a target merely opens a crafted email — and Proofpoint's follow-up unpacked ZimReaper's sanitizer-bypass mechanics and its use of an attacker-created application-specific password for persistence (detailed in the referenced operational entry). Separately, Proofpoint detailed TA458 (ESET's Operation RoundPress), a GRU-assessed actor running a live supply of "half-click" webmail zero-days across Zimbra, mDaemon, Roundcube, Kerio and a newly disclosed SOGo flaw (CVE-2026-8496, patched in 5.12.8). The strategic reality for CH/EU public-sector estates: any internet-reachable self-hosted webmail is standing state-espionage exposure, the exploit needs no click, and eviction requires revoking attacker-created app passwords, not just patching.
discovered_at: "2026-07-26T23:41:00Z"
event_date: 2026-07-25
run_id: 2026-07-26T2309Z-weekly
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - zero-click
  - zero-day
  - actively-exploited
  - identity
  - cisa-kev
regions:
  - europe
  - switzerland
  - global
sectors:
  - public-sector
  - defense
  - energy
  - telco
entities:
  - actor:laundry-bear
  - actor:ta458-roundpress
  - malware:spypress
  - tool:ulej-flowerbed
cves: []
techniques:
  - T1203
  - T1566
  - T1114.002
  - T1539
  - T1556.006
  - T1098
  - T1087.003
affected_products:
  - "Zimbra Collaboration Suite"
  - "SOGo"
sources:
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a"
    publisher: "CISA / NSA / FBI + allied agencies from 16 nations (joint CSA AA26-204A)"
    date: "2026-07-23"
    role: primary
  - url: "https://www.ncsc.gov.uk/news/uk-and-partners-expose-russian-state-supported-actors-for-new-zero-click-phishing-campaign"
    publisher: "NCSC-UK"
    date: "2026-07-23"
    role: primary
  - url: "https://www.proofpoint.com/us/blog/threat-insight/ta488-targets-zimbra-mailservers-half-click-exploits"
    publisher: "Proofpoint Threat Research"
    date: "2026-07-23"
    role: primary
  - url: "https://www.proofpoint.com/us/blog/threat-insight/ta458-roundpress-exploits"
    publisher: "Proofpoint Threat Research"
    date: "2026-07-23"
    role: primary
  - url: "https://unit42.paloaltonetworks.com/russian-webmail-espionage/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-07-23"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Unlike traditional phishing campaigns that persuade a user into taking an action, such as clicking a link or opening a file, LAUNDRY BEAR's latest campaign leverages a view-based exploit that only requires a user to view a malicious email within a vulnerable version of the webmail service."
    publisher: "CISA / NSA / FBI + allied agencies from 16 nations (joint CSA AA26-204A)"
  - quote: "A 'half-click exploit' requires no social engineering, nor does it require a user to click a link or open an attachment. The targeted user must only open the malicious email in their webmail viewer to be compromised."
    publisher: "Proofpoint Threat Research"
  - quote: "Proofpoint has not observed TA458 using CVE-2025-66376, despite the group's regular access to webmail XSS zero-days."
    publisher: "Proofpoint Threat Research"
verification: multi-source
sourcing_note: "LAUNDRY BEAR (Void Blizzard / TA488) and TA458 (Operation RoundPress) are treated as distinct actors — Proofpoint explicitly states it has not observed TA458 using the Zimbra CVE-2025-66376 that the joint advisory attributes to LAUNDRY BEAR. The unifying claim is the shared attack surface (self-hosted webmail) and technique class (view/half-click exploitation), not a shared operator."
confidence: high
update_of: null
references:
  - 2026-07-24/laundry-bear-zimbra-zero-click-cve-2025-66376
  - 2026-07-25/laundry-bear-zimreaper-app-password-persistence
  - 2026-07-25/ta458-roundpress-webmail-zero-days-sogo-cve-2026-8496
  - 2026-07-22/zimbra-10-1-20-snmp-command-injection-rce-plus-stored-xss
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**If you did nothing this week:** any internet-reachable self-hosted webmail server in your estate — Zimbra above all, but also SOGo, Roundcube, mDaemon or Kerio — is exposed to at least one Russian state actor running exploits that compromise a mailbox the instant a targeted user simply opens a message, with no link to click and no attachment to open.

Two independent disclosures made webmail the week's espionage story, and they are two different actors. The 16-nation joint advisory **AA26-204A** attributes a sustained campaign against Zimbra Collaboration Suite to **LAUNDRY BEAR** (also tracked as Void Blizzard / TA488), and describes its distinguishing tradecraft precisely: the campaign "leverages a view-based exploit that only requires a user to view a malicious email within a vulnerable version of the webmail service" ([joint CSA AA26-204A, 2026-07-23](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a)), abusing the stored-XSS **CVE-2025-66376** to steal 90 days of mail, the Global Address List and 2FA codes ([joint CSA AA26-204A, 2026-07-23](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-204a)). Proofpoint's follow-up added the mechanics the advisory omitted, including a CSS-`@import` sanitizer bypass that reassembles an executing `<svg onload="eval(atob('…'))">` and — the part that matters for eviction — the creation of an attacker-controlled application-specific password as a persistence credential separate from the user's own login ([Proofpoint, 2026-07-23](https://www.proofpoint.com/us/blog/threat-insight/ta488-targets-zimbra-mailservers-half-click-exploits)).

The second actor is **TA458** (ESET's Operation RoundPress), which Proofpoint assesses as a likely Russian GRU operation and — importantly — states it "has not observed TA458 using CVE-2025-66376" ([Proofpoint, 2026-07-23](https://www.proofpoint.com/us/blog/threat-insight/ta488-targets-zimbra-mailservers-half-click-exploits)), keeping the two clusters distinct. TA458 instead runs a standing supply of "half-click" webmail zero-days that fire the instant a target opens a message across Zimbra, mDaemon, Roundcube, Kerio and — newly disclosed this week — SOGo, where Proofpoint reported the flaw to Alinto and it "was patched as CVE-2026-8496 in version 5.12.8" ([Proofpoint, 2026-07-23](https://www.proofpoint.com/us/blog/threat-insight/ta458-roundpress-exploits)), each dropping a per-client SpyPress payload to steal credentials, contacts and mail. That the same week also brought a routine Zimbra 10.1.20 release fixing an SNMP command-injection RCE and four stored-XSS bugs underlines how continuously this software surface turns over.

**Defender takeaway:** treat any exposed self-hosted webmail as a live state-espionage target and reason from the shared observable behaviour, not the actor. The exploit executes on message *rendering*, so the telemetry to hunt is server-side script execution in the webmail context and anomalous mailbox operations that follow — bulk message reads, GAL enumeration, and IMAP/SOAP application-password creation — rather than a user click. **Triage:** a legitimate webmail user creating an app password does so interactively from a known session; the espionage pattern is an application-specific password minted via the SOAP/admin API shortly after a crafted inbound message, with no corresponding interactive login — and because such application passwords are credentials separate from the user's own, evicting these actors means enumerating and revoking application-specific passwords on affected mailboxes, not only patching and forcing a password reset. Per-platform patched versions are in the referenced operational entries.
