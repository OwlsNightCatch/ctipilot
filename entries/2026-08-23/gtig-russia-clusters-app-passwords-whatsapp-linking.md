---
schema: 1
kind: threat
horizon: operational
title: "Three Russia-nexus espionage clusters compromise European diplomats and academics without malware — by talking targets through app passwords, device-code approvals and WhatsApp device-linking, all of which are legitimate features working as designed"
headline: "No exploit and no payload — the victim approves the attacker's session, or issues a credential the second factor never sees"
summary: >
  Google Threat Intelligence Group published research on 2026-08-20 on three distinct suspected
  Russia-nexus clusters whose primary access method is abuse of legitimate authentication workflows
  rather than malware. UNC6293 talks targets into creating an application-specific password and
  sharing it back, which grants access without ever triggering the second factor. UNC7005 — the
  cluster this store already tracks as Storm-2945 — runs device-code phishing through spoofed
  conference sites that fingerprint the browser to evade automated scanners before showing the code,
  and separately abuses WhatsApp device-linking by generating a genuine link request against a
  victim-supplied phone number, then instructing the victim to approve it; a fake voice call on the
  same page captures microphone and camera through the browser under cover of the call. UNC5976 stands up a cloud
  project per phishing domain and harvests OAuth tokens after a real consent flow. The target set is
  academia, aerospace and defence, governments and think tanks across Europe.
discovered_at: "2026-08-23T05:12:00Z"
event_date: "2026-08-20"
run_id: 2026-08-23T0409Z-intel
priority: high
immediate_action: null
tags: [espionage, nation-state, identity, phishing, cloud, russia-nexus]
regions: [europe, us, global]
sectors: [public-sector, defense, education, technology]
entities: [actor:storm-2945, actor:midnight-blizzard, actor:unc6293, actor:unc5976, malware:headrush, campaign:captivecrunch-storm-2945-hospitality-wifi]
techniques: [T1566.002, T1528, T1556.006, T1123, T1125, T1204.002, T1218.005]
affected_products: ["Google Workspace", "Microsoft Entra ID", "WhatsApp"]
cves: []
sources:
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia"
    publisher: "Google Threat Intelligence Group"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence:
  - quote: "individuals working in academia, aerospace and defense, governments and think tanks across Europe"
    publisher: "Google Threat Intelligence Group"
  - quote: "GTIG assesses with high confidence that these three threat clusters"
    publisher: "Google Threat Intelligence Group"
verification: single-source
sourcing_note: >
  Google Threat Intelligence Group is the sole assessor and its confidence wording is carried as
  stated — high confidence on the Russian nexus of all three clusters, moderate confidence on the
  linkage of two of them to the actor it tracks as ICE RELIC. The cluster GTIG calls UNC7005 is the
  same one this store already tracks as Storm-2945, and GTIG itself ties it to the captive-portal
  activity previously reported by other vendors; the ICE RELIC designation is an existing alias of
  the actor this store tracks as Midnight Blizzard, so both linked entities are already known here
  rather than new. Cluster designations are GTIG's own and are not merged with one another.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Disable application-specific passwords tenant-wide if your identity platform still permits them — they are the one credential class in this research that defeats multi-factor authentication outright, and for most organisations nothing legitimate still depends on them."
  - "Restrict the OAuth device-code authorisation flow by policy to the users and locations that genuinely need it, and alert on device-code grants completed from a different network than the sign-in that requested them."
migrated_from: null
---

Google Threat Intelligence Group published research on 2026-08-20 covering three suspected Russia-nexus espionage clusters that share a method rather than infrastructure: they compromise accounts by driving legitimate authentication features, not by delivering malware ([Google Threat Intelligence Group, 2026-08-20](https://cloud.google.com/blog/topics/threat-intelligence/distinct-clusters-target-individuals-of-interest-to-russia)). The reported target set puts this constituency inside the blast radius directly — *"individuals working in academia, aerospace and defense, governments and think tanks across Europe"*, alongside US academia and think tanks. GTIG assesses with high confidence that all three possess a Russian nexus, and with moderate confidence that two of them are sub-clusters of the actor it tracks as ICE RELIC — the cluster more widely known as Midnight Blizzard — handling initial access.

**Application passwords (UNC6293).** An application-specific password is an account-level passcode issued so that a legacy client can authenticate without going through the second factor. The cluster sends a diplomatic or conference-themed lure — a PDF containing screenshots that walk the target through creating a password under a specific, official-looking name and sharing it back. Nothing is exploited and no code runs; the victim performs the whole operation, and the resulting credential is designed not to prompt for a second factor. Campaigns are deliberately small, typically fewer than five targets at a time. By mid-2026 the cluster had added a variation asking targets to share a verification code or post-login URL after authenticating legitimately to an external provider.

**Device codes and WhatsApp linking (UNC7005, tracked here as Storm-2945, the cluster behind the CaptiveCrunch hospitality-WiFi captive-portal activity).** The device-code flow exists so that input-constrained devices can authenticate: one device shows a short code, the user approves it on another. Phished, it becomes a way to have the victim authorise the attacker's session. This cluster delivers those prompts through emailed links to domains impersonating real conferences — GTIG documents a spoof of a European security forum reusing a template from an earlier embassy-invitation operation — and the pages fingerprint the browser with client-side JavaScript to detect automated scanners and headless browsers, withholding the code entirely until the visitor looks like a real person. That last detail matters operationally: a security team detonating the link in a sandbox may see a benign page.

The WhatsApp technique is the same idea applied to a messaging platform. The page asks for the target's phone number, the attacker's backend uses it to generate a genuine device-linking request, and the resulting code is displayed to the victim with instructions to approve it — linking the attacker's device to the victim's account through the vendor's own supported mechanism. The page then offers a voice call, encrypted chat or file share; if the victim joins the call, browser JavaScript captures microphone and camera through the standard media-capture interface and uploads the recording while the call is presented as having failed.

**OAuth token harvesting (UNC5976).** Assessed as operationally distinct from the other two, this cluster buys file-sharing-themed domains, creates a cloud project for each, and serves a fake file-share login. A target choosing to continue with their existing identity provider is sent through a genuine consent flow and then redirected to the attacker's own cloud-project URL, where a script captures the resulting token. GTIG disrupted the operation by disabling the malicious cloud projects; the cluster stood up at least twelve new domains within roughly three months and began moving hosting elsewhere. It has separately distributed a malicious spreadsheet plugin GTIG names HEADRUSH, observed in April 2026 and leading to an HTML Application downloader — a scripted payload executed through the built-in Windows host binary rather than as a conventional executable — delivered through a domain impersonating a Ukrainian research institute.

Detection concepts, telemetry class first. The unifying property is that **none of this produces endpoint malware telemetry on the way in** — the compromise completes in the identity plane, so that is where it must be caught. In **identity and sign-in telemetry**: creation of an application-specific password, which for most organisations should be a rare or extinct event and is trivially alertable; completion of a device-code authorisation, particularly where the approving session and the resulting access originate from different networks or geographies; and new OAuth consent grants to applications outside an approved inventory. In **mail and web telemetry**, conference-themed invitations linking to newly registered lookalike domains are the delivery pattern, though the browser fingerprinting means automated detonation may return a clean verdict — treat a link that renders differently for a sandbox than for a user as suspicious in itself rather than as a false positive. On the messaging side, the observable is the account's own linked-device list, which is user-visible and rarely inspected.

**Defender takeaway:** every mechanism here is a supported feature behaving correctly, so there is no patch and signature-based controls see nothing. Two of the three are closable by policy rather than detection — application passwords can be disabled outright, and the device-code flow can be restricted to the small set of users and locations that need it. The WhatsApp path is not organisationally controllable where staff use personal accounts for work contact, which makes it an awareness and account-hygiene problem: the linked-device list is the only place the compromise is visible. **Triage:** a legitimate device-code sign-in and a phished one produce the same event type, so the discriminator is correlation rather than the event itself — whether the approval came from the same user, network and time window as a sign-in the user actually initiated, and whether the account subsequently reads mail or files at a rate and breadth that its owner does not.
