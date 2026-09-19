---
schema: 1
kind: threat
title: "A ScreenConnect distribution campaign fronts fake Microsoft Store and App Store update dialogs, and binds each installer to its operator's relay with an embedded key"
headline: "Interactive fake-update modals, cloud-hosted payloads and self-registering RMM installers deployed at guest permission to stay quiet"
summary: >
  LevelBlue's SpiderLabs documents a large-scale ConnectWise ScreenConnect distribution campaign that
  impersonates the Google Meet pre-join screen, the Microsoft Store and the Apple App Store using interactive
  modal dialogs — progress bars and permission prompts — rather than a static phishing page. The chain runs
  batch script to PowerShell to a silent MSI install with UAC elevation, and each installer is
  cryptographically bound by an embedded public key to a specific attacker relay so it self-registers on
  install, deployed at guest-level permission to keep its footprint small. Payloads are hosted on AWS S3 and
  Cloudflare R2 behind anti-automation checks and victim fingerprinting.
discovered_at: "2026-08-08T05:19:00Z"
event_date: "2026-08-07"
run_id: 2026-08-08T0409Z-intel
priority: notable
immediate_action: null
tags: [phishing, infostealer, ai-abuse]
regions: [global]
sectors: [public-sector, healthcare, finance, energy, transport, telco]
entities: [campaign:screenconnect-appstore-phishing-2026-08]
techniques: [T1189, T1204.002, T1219, T1102.002, T1583.006]
affected_products: ["ConnectWise ScreenConnect"]
cves: []
sources:
  - url: "https://www.levelblue.com/blogs/spiderlabs-blog/beyond-fake-updates-from-application-store-themed-phishing-to-large-scale-distribution-of-screenconnect"
    publisher: "LevelBlue SpiderLabs"
    date: "2026-08-07"
    role: primary
closed_sources: []
evidence:
  - quote: "impersonating the Microsoft Store and Apple App Store"
    publisher: "LevelBlue SpiderLabs"
  - quote: "Because each installer is cryptographically bound to its corresponding relay server through the embedded public key, it automatically registers with the attacker's ScreenConnect instance once installed."
    publisher: "LevelBlue SpiderLabs"
verification: single-source
sourcing_note: "LevelBlue SpiderLabs' own campaign tracking; no second research team is cited here for these specific mechanics."
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
actions:
  - "Alert on ScreenConnect client installation where the relay hostname is not one your organisation operates — the campaign's installers self-register to an attacker relay on install, so the relay identity is the discriminator that survives every cosmetic change to the lure."
migrated_from: null
---

LevelBlue's SpiderLabs OpsCTI team is tracking a ScreenConnect distribution campaign whose lure has moved past the static fake-update page. Instead, it "recreates convincing software update and installation alerts by impersonating the Microsoft Store and Apple App Store while reproducing the look and behavior of trusted applications through dynamic modal dialogs and other interactive web elements", also imitating the Google Meet pre-join screen, with progress bars and camera and microphone permission prompts that behave the way the real dialogs do ([LevelBlue SpiderLabs, 2026-08-07](https://www.levelblue.com/blogs/spiderlabs-blog/beyond-fake-updates-from-application-store-themed-phishing-to-large-scale-distribution-of-screenconnect)).

The installation chain is a batch script into PowerShell into an MSI installed silently through `msiexec.exe /quiet` with UAC elevation. The operational detail worth carrying is what happens next: "Because each installer is cryptographically bound to its corresponding relay server through the embedded public key, it automatically registers with the attacker's ScreenConnect instance once installed" ([LevelBlue SpiderLabs, 2026-08-07](https://www.levelblue.com/blogs/spiderlabs-blog/beyond-fake-updates-from-application-store-themed-phishing-to-large-scale-distribution-of-screenconnect)). The agent is deployed at guest-level permission rather than full administrative rights, which keeps its footprint small and its behaviour closer to a legitimate support install.

The delivery infrastructure is built to survive the loss of any single component: thousands of near-identical phishing-framework deployments, payloads hosted on legitimate cloud object storage (AWS S3, Cloudflare R2), anti-automation gating through honeypot form fields, artificial delays and User-Agent filtering to Windows desktop clients only, and full victim fingerprinting — address, geolocation, ISP, browser, timezone, screen resolution — before an installer is served at all. Successful infections notify the operator in real time through the Telegram Bot API. LevelBlue assesses the supporting scripts as AI-assisted on the basis of unusually verbose documentation-style inline comments and emoji markers ([LevelBlue SpiderLabs, 2026-08-07](https://www.levelblue.com/blogs/spiderlabs-blog/beyond-fake-updates-from-application-store-themed-phishing-to-large-scale-distribution-of-screenconnect)).

**Defender takeaway:** blocking ScreenConnect outright is not available to most organisations, because it is a legitimate remote-support product many helpdesks and suppliers use, and the payload here is the genuine signed client rather than a trojanised build. That is what makes the relay binding the useful control: a legitimately deployed client points at a relay your organisation or your managed-service provider operates, and this campaign's clients cannot — the operator's relay is compiled into the installer by key. An allow-list of sanctioned relay hostnames turns an unblockable application into a decidable one.

**Triage:** the benign lookalike is a real support session, and it is common. The discriminators the cited mechanics support, in order of strength: the relay hostname the client registers to; installation at guest-level permission with no corresponding helpdesk ticket; and the process lineage — a browser spawning a batch script or PowerShell that calls `msiexec.exe /quiet`, which is not how a user or an administrator installs remote-support software deliberately. The fingerprinting gate also means an analyst re-visiting the lure URL from a sandbox or a non-Windows client will usually be served a decoy rather than the installer, so failure to reproduce the payload is not evidence the report is wrong.
