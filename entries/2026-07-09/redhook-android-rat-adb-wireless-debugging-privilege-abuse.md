---
schema: 1
kind: threat
horizon: operational
title: "RedHook Android RAT abuses ADB Wireless Debugging to self-grant shell (uid 2000) privileges without an exploit"
headline: "RedHook shows a no-exploit Android privilege path: Accessibility automation silently enables Wireless Debugging for a shell-uid helper"
summary: >
  Group-IB documents an upgraded RedHook Android RAT that, after tricking a victim into granting
  Accessibility, uses UI automation to silently enable Developer Options and ADB Wireless
  Debugging, connects its own ADB client over loopback, and launches a Shizuku-derived helper
  running as shell uid 2000 — granting itself permissions, modifying secure settings and running
  shell commands with no exploit and no user dialogs. Targeting has expanded from Vietnam to
  Indonesia; the technique is directly relevant to MDM/BYOD-managed Android fleets everywhere.
discovered_at: "2026-07-09T12:30:00Z"
event_date: "2026-07-09"
run_id: 2026-07-09T1211Z-intel
priority: notable
immediate_action: null
tags: [mobile, infostealer, phishing, identity]
regions: [apac, global]
sectors: [finance, technology]
entities: [tool:redhook-android-rat]
cves: []
sources:
  - url: "https://www.group-ib.com/blog/redhook-android-rat-upgraded/"
    publisher: "Group-IB"
    date: "2026-07-09"
    role: primary
closed_sources: []
evidence:
  - quote: "This, however, is the first time we have seen it used by a malware to abuse privileges on a victim's device."
    publisher: "Group-IB"
  - quote: "There is no exploit here, \"merely\" turning a debugging interface into a path to shell-level privileges."
    publisher: "Group-IB"
verification: single-source
sourcing_note: "Single-source: Group-IB original malware analysis (a reliable research lab, reliability B); no independent corroboration of the specific upgraded-variant findings was available in-window, so credibility is rated 2 (plausible, uncorroborated). RedHook was first documented by Cyble in July 2025."
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
  - "On MDM/Android-Enterprise-managed fleets, disable Developer Options and USB/Wireless debugging by default (DevicePolicyManager setDebuggingFeaturesAllowed or equivalent restriction) so an app cannot self-enable the ADB path."
  - "Hunt for the abuse pattern: any non-system app programmatically flipping Settings.Global adb_wifi_enabled / enabling Developer Options without an IT-initiated pairing flow, or a non-ADB process binding a loopback (127.0.0.1) ADB connection, is anomalous on a managed device and should alert."
  - "Gate BIND_ACCESSIBILITY_SERVICE to an approved allowlist and treat off-store APKs delivered via 'required setup' walkthroughs on spoofed government/financial sites as the initial-access vector to block."
migrated_from: null
---

Group-IB documents a significantly upgraded variant of RedHook, an Android RAT first described by Cyble in July 2025 and previously focused on Vietnamese banking users ([Group-IB, 2026-07-09](https://www.group-ib.com/blog/redhook-android-rat-upgraded/)). The notable new capability is self-service privilege abuse over ADB Wireless Debugging with no exploit involved. After the victim is socially engineered — via impersonation calls/messages and a fake Play-Store-styled site — into installing the APK and granting Accessibility through a "required setup" walkthrough, the malware uses Accessibility-driven UI automation to silently navigate Settings, enable Developer Options and Wireless Debugging, then embeds its own ADB client to connect to the device's own ADB daemon over the loopback interface (127.0.0.1) — no PC or USB cable needed. It launches a Shizuku-derived privileged helper that runs under shell uid 2000, from which it grants itself runtime permissions, sets `WRITE_SECURE_SETTINGS`, installs/uninstalls apps and executes shell commands with no user-facing confirmation dialogs. Group-IB states plainly that "there is no exploit here" — this is abuse of a legitimate developer feature, the same primitive tools like Shizuku have long used, weaponised for the first time by malware.

Persistence is layered: a 1×1-pixel foreground activity, silent MediaSession audio, a foreground-service WakeLock, two mutually cross-rebinding services (`bindService` with `BIND_AUTO_CREATE`) that resurrect each other, `oom_score_adj` tuning to -1000, `mlock()` memory pinning, and a `BOOT_COMPLETED` receiver that re-establishes Wireless ADB and the helper on every reboot; screen streaming runs over WebSocket with a parallel RTMP stream once shell privileges exist, bypassing the MediaProjection consent dialog. The command set has grown to 53 server-issued commands, APK payloads are hosted on GitHub and AWS S3 for delivery reliability, and OEM-specific UI-automation routines (Google, Huawei, Meizu, Oppo, Samsung, Vivo, Xiaomi) are present but not yet invoked — suggesting planned device-coverage expansion. Mapped for mobile defenders to `T1453 Abuse Accessibility Features`, `T1541 Foreground Persistence`, `T1512 Video Capture`, `T1417 Input Capture`, and — closest available mapping for the shell-uid grab — `T1626 Abuse Elevation Control Mechanism`. **Defender takeaway:** targeting is currently Vietnam and Indonesia, but the ADB-Wireless-Debugging self-enablement technique is device- and region-agnostic and directly transferable to any Android estate; the defensible control surface is MDM policy disabling debugging features and hunting for an app enabling Developer Options or binding a loopback ADB connection outside an IT-initiated flow.
