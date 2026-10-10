---
schema: 1
kind: research
title: "Zimperium: Rokarolla Android banking trojan targets 217 apps with full device takeover"
headline: "Zimperium: Rokarolla Android banking trojan targets 217 apps with full device takeover"
summary: "Zimperium zLabs detailed Rokarolla, a new Android banking trojan distributed via sideloading from sites impersonating TikTok/Chrome, using a dropper that masquerades as Google Play Protect to obtain Accessibility Service permissions (Zimperium zLabs, 2026-06-16)."
discovered_at: "2026-06-17T05:14:31Z"
event_date: 2026-06-16
run_id: 2026-06-17-e102009c
priority: notable
immediate_action: null
tags:
  - mobile
  - infostealer
  - organized-crime
regions:
  - global
  - europe
sectors:
  - finance
entities:
  - "campaign:zimperium-rokarolla-android-banker-217-apps"
cves: []
sources:
  - url: "https://zimperium.com/blog/rokarolla-android-banker-with-complete-device-takeover-capabilities"
    publisher: "Zimperium zLabs, 2026-06-16"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-rokarolla-android-malware-targets-217-banking-crypto-apps/"
    publisher: "BleepingComputer, 2026-06-16"
    role: corroborating
closed_sources: []
evidence: []
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
migrated_from: briefs/2026-06-17.md
---

Zimperium zLabs detailed Rokarolla, a new Android banking trojan distributed via sideloading from sites impersonating TikTok/Chrome, using a dropper that masquerades as Google Play Protect to obtain Accessibility Service permissions ([Zimperium zLabs, 2026-06-16](https://zimperium.com/blog/rokarolla-android-banker-with-complete-device-takeover-capabilities)). It targets 217 banking and crypto apps via a 137-command framework: lifting the lock-screen PIN, intercepting SMS OTPs, rewriting the clipboard to hijack crypto payments, disabling Play Protect, and — distinctively — registering itself as the default call/SMS handler so a bank's warning call or SMS never reaches the victim ([BleepingComputer, 2026-06-16](https://www.bleepingcomputer.com/news/security/new-rokarolla-android-malware-targets-217-banking-crypto-apps/)). A target list of this breadth makes any Android device used for e-banking a plausible victim once an app is sideloaded.

**Why it matters to us:** Rokarolla cannot reach the Play Store; it relies entirely on sideloading. Enforce "Install from Unknown Sources" restrictions via Android Enterprise/MDM on managed devices and MAM containers for BYOD; flag any app that disables Play Protect or requests Accessibility Service immediately after a web-sourced install.
