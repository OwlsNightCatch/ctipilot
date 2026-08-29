---
schema: 1
kind: threat
title: "ClickLock Stealer — a macOS ClickFix infostealer that force-kills every visible app until the victim types their login password"
headline: "ClickLock: a modular macOS stealer that locks the desktop by killing every app until the user surrenders their password — Europe is the top victim region"
summary: >
  Group-IB has documented ClickLock Stealer, a previously undetected modular macOS infostealer delivered
  via ClickFix social engineering (paste-into-Terminal) that needs no exploit and no elevated privilege.
  Its signature move: on next login, a module kills every visible application every ~210 ms, leaving only
  a fake password dialog on screen — for up to ~83 hours — until the victim types their macOS password
  (validated locally so only the correct one is exfiltrated); a parallel module uses the same coercion to
  force a real Keychain-authorization dialog and steal Chrome's Safe Storage key. More than 50% of the
  ~100 identified victims across 33 countries are in Europe, making this directly relevant to any Swiss or
  European organization issuing macOS endpoints.
discovered_at: "2026-07-19T04:23:31Z"
event_date: "2026-07-16"
run_id: 2026-07-19T0408Z-intel
priority: notable
immediate_action: null
tags: [infostealer, phishing, cryptocrime]
regions: [europe, global]
sectors: []
entities: ["tool:clicklock-stealer"]
techniques: [T1204.004, T1059.004, T1105, T1543.001, T1053.003, T1546.004, T1036.005, T1056.002, T1685, T1564.001, T1555.001, T1555.003, T1552.001, T1119, T1070.004, T1070.006, T1102, T1567]
affected_products: ["Apple macOS"]
cves: []
sources:
  - url: "https://www.group-ib.com/blog/clicklock-stealer-macos-malware/"
    publisher: "Group-IB Threat Intelligence"
    date: "2026-07-16"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/new-clicklock-macos-malware-traps-users-into-revealing-login-password/"
    publisher: "BleepingComputer"
    date: "2026-07-16"
    role: corroborating
  - url: "https://www.forbes.com/sites/daveywinder/2026/07/18/app-killing-mac-malware-triggers-83-hour-password-entry-loop/"
    publisher: "Forbes"
    date: "2026-07-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "On subsequent login, the zsh.txt module activates killing every visible application every 210 milliseconds, leaving only a password dialog on screen until the user is forced to comply."
    publisher: "Group-IB"
  - quote: "If the user enters a password, it is validated against the local directory service via dscl /Local/Default -authonly “$USER” “$PASS” ensuring only the correct password is exfiltrated."
    publisher: "Group-IB"
  - quote: "A ClickLock Stealer operation has already targeted at least 100 victims in 33 countries, with more than 50% from Europe, and has been active for approximately two months, since May 2026."
    publisher: "Group-IB"
  - quote: "Alert on rapid, repeated pkill or killall activity targeting system processes (Finder, Dock, SystemUIServer, NotificationCenter) at sub-second intervals, this behavior is unique to forced-interaction malware and has no legitimate use case."
    publisher: "Group-IB"
verification: multi-source
sourcing_note: "Group-IB is the sole originating research (reliability B, original macOS-malware analysis); BleepingComputer and Forbes re-report Group-IB's findings rather than contribute independent primary analysis, so credibility is rated 2 (a plausible, well-evidenced single-origin research claim, not independently corroborated). No IOCs (compromised-domain names, hashes, Telegram identifiers) are carried per pipeline policy."
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
migrated_from: null
---

macOS endpoint malware is usually treated as rare and, when it appears, as a stealthy background stealer; **ClickLock Stealer** — documented by Group-IB after a shell script with zero VirusTotal detections was uploaded on 9 June 2026 — inverts both assumptions with an overtly coercive design that forces the victim to hand over their own password, and it is landing disproportionately in Europe ([Group-IB, 2026-07-16](https://www.group-ib.com/blog/clicklock-stealer-macos-malware/)). Group-IB's telemetry counts "at least 100 victims in 33 countries, with more than 50% from Europe," active since roughly May 2026 ([Group-IB, 2026-07-16](https://www.group-ib.com/blog/clicklock-stealer-macos-malware/)). It sits in the same ClickFix-delivered macOS-stealer lineage as AMOS, Poseidon and Banshee but is mechanically distinct in how it obtains credentials — it does not defeat the operating system's protections, it defeats the user.

**Delivery and execution (T1204.004, T1059.004, T1105).** The victim reaches a ClickFix page — a fake Cloudflare "verifying you are not a bot" flow — and is instructed to paste a command into Terminal. That orchestrator shell script disables keyboard interrupts, renders a fake Cloudflare progress-bar animation as cover, and downloads four modules from compromised WordPress infrastructure: a credential stealer, a Keychain stealer, a cross-platform crypto stealer, and a backdoor installer ([Group-IB, 2026-07-16](https://www.group-ib.com/blog/clicklock-stealer-macos-malware/)). Nothing here needs an exploit or elevated privilege — the whole chain runs at the logged-in user's level.

**The coercion mechanism (T1056.002, T1685).** The orchestrator first tries a "soft" approach: a fake macOS password dialog built with `osascript`, styled with a downloaded Apple icon to look genuine. Any password entered is checked locally against the directory service — "validated against the local directory service via `dscl /Local/Default -authonly`… ensuring only the correct password is exfiltrated" — so the operator receives only a working credential ([Group-IB, 2026-07-16](https://www.group-ib.com/blog/clicklock-stealer-macos-malware/)). If the victim cancels, the script installs persistence and exits; on the next login the credential-stealer module "activates killing every visible application every 210 milliseconds, leaving only a password dialog on screen until the user is forced to comply" ([Group-IB, 2026-07-16](https://www.group-ib.com/blog/clicklock-stealer-macos-malware/)). The kill loop deliberately includes Finder, Dock, SystemUIServer, Spotlight, Terminal, all common browsers and — critically — Activity Monitor and Console, so the victim cannot investigate or terminate the malware; the credential loop is configured to run for approximately 83 hours. A parallel Keychain-stealer module uses the identical technique at a ~0.2-second cadence to force approval of a *real* macOS Keychain-authorization prompt, capturing Chrome's Safe Storage AES key (which decrypts the browser's saved passwords and cookies offline). A separate background loop kills `NotificationCenter` for roughly six hours to suppress any Gatekeeper or security alerts.

**Collection and exfiltration (T1555.001, T1555.003, T1552.001, T1119, T1567, T1102).** While the coercion loops run, a data harvester performs a full scan across eight browsers, 31 crypto-wallet browser extensions, seven password-manager extensions, eight desktop wallet applications, blockchain addresses across six chains, the macOS Keychain, shell history and FTP credentials, archives everything into a ZIP, and pushes it to a Telegram bot via the bot API — Telegram serving as a no-infrastructure exfiltration channel with encrypted transport unlikely to be blocked by network filters (Group-IB observed no dedicated command-and-control infrastructure; ongoing remote access comes from the GSocket backdoor below). To widen access, the orchestrator checks whether Terminal holds Full Disk Access and, if not, opens System Settings straight to the Full Disk Access pane with step-by-step instructions to add Terminal, unlocking TCC-protected paths including the Keychain database.

**Persistence and anti-forensics (T1543.001, T1053.003, T1546.004, T1564.001, T1036.005, T1070.004, T1070.006).** The credential and Keychain modules stage into a hidden `~/.cacheb/` directory and install two LaunchAgents so they re-arm on every login even if the victim cancels the dialog, closes Terminal or reboots. The backdoor installer deploys a lightly modified open-source GSocket build — a persistent `gs-netcat` reverse shell disguised as an iCloud process — and, unlike the self-deleting stealer modules, keeps a durable foothold via crontab injection, shell-RC-file modification and a LaunchAgent, phoning its connection secret home over three redundant channels. Every stealer module self-deletes after running and copies file modification times from a default macOS directory onto its artifacts to blunt timeline-based forensics.

**Defender takeaway:** the malware's design gives defenders a narrow but distinctive behavioral window, because the payloads are hosted on clean-reputation compromised domains, the script had zero detections at discovery, and the stealer modules self-delete — signature and reputation controls will largely miss it, so hunt on behavior. The strongest single discriminator is Group-IB's own: "rapid, repeated `pkill` or `killall` activity targeting system processes (Finder, Dock, SystemUIServer, NotificationCenter) at sub-second intervals… has no legitimate use case" ([Group-IB, 2026-07-16](https://www.group-ib.com/blog/clicklock-stealer-macos-malware/)). Layer onto that: `osascript` spawning password dialogs (especially with an icon loaded from an unusual path); `security find-generic-password` invoked from a shell or other non-browser parent; bulk reads of browser-profile directories (Login Data, Cookies, extension storage) followed by outbound connections to the Telegram bot API; LaunchAgent creation by a shell process; and the presence of a `~/.cacheb/` staging directory or unfamiliar plists in `~/Library/LaunchAgents/`. Because initial access is paste-into-Terminal, the highest-value prevention is user-facing — treat any workflow that tells a user to paste a command into Terminal to "verify" themselves as hostile — reinforced by restricting or monitoring Full Disk Access grants to Terminal on managed macOS fleets. **Triage:** a legitimate application querying its own Keychain item does so from the application process itself; a `bash`/shell process requesting Chrome's Safe Storage key, or a burst of process terminations that leaves only a credential prompt on screen, is the malicious pattern — there is no benign administrative task that repeatedly kills Finder, Dock and Activity Monitor every fraction of a second.
