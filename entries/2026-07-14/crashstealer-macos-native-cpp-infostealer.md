---
schema: 1
kind: threat
horizon: operational
title: "CrashStealer — a native-C++ macOS infostealer using a notarized dropper and local dscl password validation to raid keychain, browsers and wallets"
headline: "CrashStealer: notarized-dropper macOS stealer validates stolen passwords with dscl before harvesting keychain and browser data"
summary: >
  Jamf Threat Labs details CrashStealer, a native-C++ macOS infostealer (distinct from AMOS/MacSync) that reached in-the-wild deployment by early July 2026. A signed, Apple-notarized "Werkbit Setup" dropper clears Gatekeeper and stages an ad-hoc-signed payload impersonating Apple's CrashReporter from a hidden /private/tmp path; the payload prompts for the login password, validates it locally with dscl -authonly, unlocks the keychain, profiles installed EDR tooling, and exfiltrates browser, wallet-extension and keychain data AES-GCM-encrypted over libcurl. Any organisation with a macOS fleet should hunt for the staging artifacts.
discovered_at: "2026-07-14T04:35:00Z"
event_date: 2026-07-13
run_id: 2026-07-14T0409Z-intel
priority: notable
immediate_action: null
tags:
  - infostealer
  - identity
regions:
  - global
sectors: []
entities:
  - "tool:crashstealer"
techniques:
  - T1204.002
  - T1553.001
  - T1140
  - T1105
  - T1543.001
  - T1622
  - T1027
  - T1518.001
  - T1555.001
  - T1555.003
  - T1564.001
  - T1560.001
  - T1041
  - T1070.006
affected_products:
  - "Apple macOS"
cves: []
sources:
  - url: "https://www.jamf.com/blog/crashstealer-macos-infostealer-analysis/"
    publisher: "Jamf Threat Labs"
    date: "2026-07-13"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-crashstealer-malware-poses-as-apple-crash-reporting-tool/"
    publisher: "BleepingComputer"
    date: "2026-07-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Validating the password with dscl -authonly before harvesting lets the operator keep only credentials that actually work"
    publisher: "Jamf Threat Labs"
  - quote: "Patching out that first check is not enough on its own: a second check later in application initialization exits the same way"
    publisher: "Jamf Threat Labs"
verification: multi-source
sourcing_note: "Primary technical analysis is Jamf Threat Labs' own; BleepingComputer relays the same research rather than independently corroborating, so credibility is held at 2."
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
  - "Sweep the macOS fleet for a bundle identifier com.apple.crashreporter executing from a hidden path (/private/tmp/.CrashReporter or ~/Library/Caches) with an ad-hoc (rather than Apple) signature, and for a LaunchAgent whose label impersonates an Apple service — Apple's genuine CrashReporter never runs from those paths."
migrated_from: null
---

Jamf Threat Labs documents **CrashStealer**, a macOS infostealer written in native C++ (around an internal `MacOSData` class) rather than the AppleScript droppers or thin Objective-C wrappers typical of commodity macOS stealers; Jamf first saw a sample on VirusTotal in early May 2026 and observed in-the-wild payload detections by early July, and tracks it as a distinct family rather than a variant of Atomic (AMOS), MacSync or Phexia ([Jamf Threat Labs, 2026-07-13](https://www.jamf.com/blog/crashstealer-macos-infostealer-analysis/); [BleepingComputer, 2026-07-13](https://www.bleepingcomputer.com/news/security/new-crashstealer-malware-poses-as-apple-crash-reporting-tool/)). Initial access is a signed and Apple-**notarized** dropper distributed as a "Werkbit Setup" disk image (both the image and the inner app are signed under a valid Developer ID — which Jamf reported to Apple after confirming it was used to distribute malicious payloads — with hardened runtime enabled) — because it carries a valid notarization ticket it clears Gatekeeper on first launch, so the "right-click → Open" instruction the installer shows is pure social engineering rather than a technical bypass ([Jamf Threat Labs, 2026-07-13](https://www.jamf.com/blog/crashstealer-macos-infostealer-analysis/)). The dropper fetches a first-stage file from a GitHub repository (keeping the opening network hop on a trusted developer domain), decodes a `curl` command, and pulls a shell script delivered as successive Base64 blobs decoded at runtime and piped to `bash`; that script downloads the payload disk image, copies the app into a hidden `/private/tmp/.CrashReporter` directory, strips and re-signs it ad-hoc (`codesign --remove-signature` then `codesign -s - --force --deep`), registers it with Launch Services and launches it ([Jamf Threat Labs, 2026-07-13](https://www.jamf.com/blog/crashstealer-macos-infostealer-analysis/)).

The payload impersonates Apple's crash reporter (bundle identifier `com.apple.crashreporter`, executing from the hidden staging path), clears its own quarantine and last-used-date extended attributes with `xattr -cr`, then presents a native-styled password prompt and validates the entered credential locally with `dscl . -authonly`, looping until a valid password is supplied — so the operator only ever collects credentials that actually authenticate ([Jamf Threat Labs, 2026-07-13](https://www.jamf.com/blog/crashstealer-macos-infostealer-analysis/)). With the validated password it unlocks the login keychain, copies `login.keychain-db` into a hidden `~/.cache` staging root, runs a reconnaissance sweep (`defaults read` for version paired with `du -sh` for on-disk size) against an embedded list skewed toward malware-analysis and EDR tooling to profile the defensive environment, and collects browser data, Chromium/Firefox extensions (including cryptocurrency-wallet extensions) and password-manager material — AES-GCM-encrypting each item into hidden staging files as it is collected (so the loot is never written to disk in the clear), then packaging each staging directory into its own zip archive before exfiltrating over `libcurl`. Persistence is a LaunchAgent registered under an Apple-impersonating label with a second re-signed copy of the binary. Anti-analysis is layered throughout: the binary checks for an attached debugger via `sysctl` process-flag (`P_TRACED`) inspection at two separate points in initialization — so patching out the first check alone does not defeat it — and its C2 address and collection-target list are held as encrypted, runtime-decoded strings behind control-flow-flattening obfuscation rather than in cleartext ([Jamf Threat Labs, 2026-07-13](https://www.jamf.com/blog/crashstealer-macos-infostealer-analysis/)).

**Defender takeaway:** the notarized-dropper-plus-ad-hoc-payload split is the load-bearing tradecraft — the trusted first stage clears Gatekeeper, while the actual stealer is re-signed locally so it never needed valid signing of its own. On endpoints, the high-signal behaviours are process-execution telemetry showing an application bundle launching from a hidden `/private/tmp` path, a GUI process spawning `dscl . -authonly` and `security unlock-keychain`, `codesign` re-signing a bundle at runtime, and a chain of `base64 -d` decodes piped to `bash` from a `curl`-fetched script. **Triage:** Apple's genuine CrashReporter runs from `/System/Library/CoreServices/` and is Apple-signed; a process advertising the `com.apple.crashreporter` bundle identifier that runs from `/private/tmp` or `~/Library/Caches` with an ad-hoc signature, or a `dscl -authonly` invocation parented to a freshly-launched "installer" app, is the discriminator — the legitimate directory-service utility is used routinely by system components but not normally spawned by a user-launched app bundle. Hardening: restrict app execution from user-writable and temporary paths, and treat a Developer-ID-notarized installer that then reaches out to GitHub and a bespoke delivery endpoint as suspicious regardless of its signature.
