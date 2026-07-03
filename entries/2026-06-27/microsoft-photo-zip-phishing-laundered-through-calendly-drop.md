---
schema: 1
kind: threat
horizon: operational
title: "Microsoft: \"Photo ZIP\" phishing laundered through Calendly drops Node.js TonRAT against European hospitality front desks"
headline: "Microsoft: \"Photo ZIP\" phishing laundered through Calendly drops Node.js TonRAT against European hospitality front desks"
summary: "Microsoft Threat Intelligence documented an active, since-April-2026 campaign against hospitality front-desk systems across Europe and Asia (Microsoft Threat Intelligence, 2026-06-25)."
discovered_at: "2026-06-27T05:17:40Z"
event_date: 2026-06-25
run_id: 2026-06-27-40e791d4
priority: notable
immediate_action: null
tags:
  - phishing
  - organized-crime
  - infostealer
regions:
  - europe
  - apac
sectors: []
entities: []
cves: []
sources:
  - url: "https://www.microsoft.com/en-us/security/blog/2026/06/25/photo-zip-campaign-targeting-hospitality-industry-delivers-node-js-implant-persistent-access/"
    publisher: Microsoft Threat Intelligence
    role: primary
  - url: "https://thehackernews.com/2026/06/microsoft-warns-of-photo-zip-phishing.html"
    publisher: The Hacker News
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
migrated_from: briefs/2026-06-27.md
---

Microsoft Threat Intelligence documented an active, since-April-2026 campaign against hospitality front-desk systems across Europe and Asia ([Microsoft Threat Intelligence, 2026-06-25](https://www.microsoft.com/en-us/security/blog/2026/06/25/photo-zip-campaign-targeting-hospitality-industry-delivers-node-js-implant-persistent-access/)). The operators use **authentication laundering** — routing phishing mail through Calendly's SendGrid notification infrastructure and Google/`share.google` redirects so it passes SPF/DKIM/DMARC — before serving `photo-<random>.zip` archives whose `IMG-<random>.png.lnk` shortcuts masquerade as images. Execution runs multi-stage obfuscated PowerShell (BigInt arithmetic decoders that harden wave-over-wave), compiles a .NET DLL on the fly via `csc.exe`/`cvtres.exe` (`T1027.004`), then fetches a Node.js v24.13.0 runtime that executes the **TonRAT** implant. Persistence is the standout: dual `HKCU\Run` (Node component) plus `HKCU\RunOnce` (PE payload in `C:\ProgramData\<random>\`) keys, with the payload re-writing its RunOnce entry after every execution so removing only one key lets the other re-install on next logon. The loader also adds `Add-MpPreference -ExclusionProcess` Defender exclusions for its temp paths. Lures appear in Dutch, Danish and Japanese.
**Why it matters to us:** Swiss and EU hotels/event venues running Windows front-desk systems are in scope. Hunt for `node.exe` spawned from `%LOCALAPPDATA%` running random-named `.js` files, `csc.exe`+`cvtres.exe` sequences outside CI, and new Defender process-exclusions on temp paths — and remember cleanup must remove **both** the `Run` and `RunOnce` keys in the same pass.
