---
schema: 1
kind: research
horizon: operational
title: "Jamf Threat Labs documents \"PamStealer\": a macOS infostealer that validates the victim's password via the PAM API before exfiltrating it"
headline: "**PamStealer** impersonates the Maccy clipboard app and confirms a stolen macOS password through pam_authenticate before sending it"
summary: >
  Jamf Threat Labs detailed PamStealer, a two-stage macOS infostealer distributed
  from a typosquatted site impersonating the Maccy clipboard manager. A JXA
  AppleScript downloader stages an arm64 Rust Mach-O that masquerades as Finder,
  validates the victim's typed login password through the macOS PAM API
  (pam_start/pam_authenticate/pam_end) before harvesting it, and steals Keychain,
  browser and clipboard data. macOS-managing teams should tighten Gatekeeper,
  Full Disk Access grants and PAM-abuse detection.
discovered_at: "2026-07-04T06:24:38Z"
event_date: "2026-07-02"
run_id: 2026-07-04T0609Z-intel
priority: notable
immediate_action: null
tags: [infostealer, identity, phishing]
regions: [global]
sectors: []
entities: [tool:pamstealer]
cves: []
sources:
  - url: "https://www.jamf.com/blog/pamstealer-macos-infostealer-applescript-rust/"
    publisher: "Jamf Threat Labs"
    date: "2026-07-02"
    role: primary
  - url: "https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html"
    publisher: "The Hacker News"
    date: "2026-07-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Rather than relying on shell commands such as curl or zsh, the AppleScript executes a self-contained JavaScript for Automation (JXA) downloader that retrieves and stages the payload using native Objective-C APIs."
    publisher: "Jamf Threat Labs"
  - quote: "The result is a quieter routine that keeps only a verified password, and one fewer process chain for defenders to detect on."
    publisher: "Jamf Threat Labs"
verification: single-source
sourcing_note: >
  Single first-hand observer: Jamf Threat Labs vendor research. The Hacker News
  (2026-07-03) is a rewrite of that primary and adds no independent first-hand
  observation, so this is single-source in substance under
  prompts/verification.md (rewrites of one report are one source).
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions:
  - "Enforce Gatekeeper and notarization policy so unsigned or ad-hoc-signed applications launched from a mounted disk image cannot run; block AppleScript execution from quarantined/mounted images via an EDR script-control policy."
  - "Alert on pam_authenticate invoked by any process other than loginwindow, sudo or su in the macOS Unified Log — legitimate password validation does not originate from a downloaded binary."
  - "Restrict Full Disk Access grants by MDM policy and alert on new TCC.db entries for unrecognized bundle IDs, since the malware social-engineers the user into granting FDA."
migrated_from: null
---

Jamf Threat Labs published an analysis of **PamStealer**, a two-stage macOS infostealer served from a typosquatted domain impersonating the legitimate Maccy clipboard-manager app ([Jamf Threat Labs, 2026-07-02](https://www.jamf.com/blog/pamstealer-macos-infostealer-applescript-rust/)). The first stage is a compiled AppleScript delivered on a disk image that, rather than shelling out to `curl`/`zsh`, runs a self-contained JavaScript for Automation (JXA) downloader against native `NSURLSession` APIs (`T1059.007`) and fingerprints the host — CPU architecture, locale, keyboard layout, timezone — excluding Russian/Belarusian/Kazakh locales before proceeding (`T1497.001`) ([Jamf Threat Labs, 2026-07-02](https://www.jamf.com/blog/pamstealer-macos-infostealer-applescript-rust/)). The second stage is an arm64 Rust Mach-O masquerading as Finder (`T1036.005`).

The behaviour that names the family is its credential handling: PamStealer validates the victim's typed login password through the macOS Pluggable Authentication Modules API — `pam_start`, `pam_authenticate`, `pam_end` — and re-prompts if validation fails, so only a confirmed-correct password is ever exfiltrated. Jamf notes the operational payoff: "the result is a quieter routine that keeps only a verified password, and one fewer process chain for defenders to detect on" ([Jamf Threat Labs, 2026-07-02](https://www.jamf.com/blog/pamstealer-macos-infostealer-applescript-rust/)). It runtime-loads Security.framework to pull browser-stored credentials and Keychain data (`T1555.001`, `T1555.003`), reads the clipboard via `pbpaste` (`T1115`), and persists through both the modern ServiceManagement API and legacy shared-file-list APIs (`T1547`); exfiltration uses an encrypted HTTPS channel and the user is social-engineered into granting Full Disk Access ([Jamf Threat Labs, 2026-07-02](https://www.jamf.com/blog/pamstealer-macos-infostealer-applescript-rust/)), a chain corroborated in secondary reporting ([The Hacker News, 2026-07-03](https://thehackernews.com/2026/07/pamstealer-uses-fake-maccy-sites-and.html)).

**Defender takeaway:** the PAM-validation step is both the family's tell and a durable detection opportunity — `pam_authenticate` invoked by anything other than `loginwindow`/`sudo`/`su` is anomalous and surfaces in the Unified Log. Pair that with alerts on new LaunchAgent/ServiceManagement registrations by unsigned or ad-hoc-signed binaries shortly after a disk-image mount from Downloads, and on new TCC.db Full Disk Access entries for unrecognized bundle IDs. Gatekeeper/notarization enforcement blocks the unsigned second stage from launching at all.
