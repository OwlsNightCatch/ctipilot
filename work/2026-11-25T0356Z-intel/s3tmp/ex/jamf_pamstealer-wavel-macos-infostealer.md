---
title: New PamStealer variant targets macOS via fake crypto wallet
author: Jamf Threat Labs
url: https://www.jamf.com/blog/pamstealer-wavel-macos-infostealer/
hostname: jamf.com
description: "Jamf Threat Labs breaks down a new PamStealer variant: a fake crypto wallet lure, server-side payload decryption and a Swift-based macOS infostealer."
sitename: Jamfsoftware
date: "2026-09-22"
fingerprint: a558c097e135678d
language: en
image: https://media.jamf.com/images/news/2026/pamstealer-wavel-macos-infostealer.webp?h=400&q=80&w=700
pagetype: website
filedate: "2026-11-25"
---
# PamStealer adapts again: a move to Swift with a server-side decryption chain

Jamf Threat Labs investigates a newer variant of PamStealer, the third known variant of the family, distributed as a fake application installer that uses a purpose-built decryption utility to ensure the payload cannot be recovered without server cooperation.

*By Thijs Xhaflaire*

## Introduction

Following our [July 2026 publication of PamStealer](https://www.jamf.com/blog/pamstealer-macos-infostealer-applescript-rust/), Jamf Threat Labs has continued to monitor and identify additional variants. While our earliest publication documented a compiled JXA dropper distributed as a fake Maccy clipboard manager, the sample analyzed here uses the same compiled JXA outer format but shifts the lure and rebuilds the delivery chain entirely.

What distinguishes this variant from its earlier ones is not what it collects but how it is delivered. Where earlier variants embedded their payload key material directly in the JXA source, it now fetches a purpose-built decryption utility and completes a key exchange with the server before the payload can be unwrapped. Without the server's cooperation, the payload cannot be recovered statically. The second stage has also been rewritten, moving from Rust to Swift, while carrying forward the PAM-based credential validation that gave this family its name.

### Table of contents

## The lure: Wavel, a fake application installer

Victims are lured through `hxxps://wavel[.]app`, a convincing website impersonating a multichain crypto wallet application. The site's "Download for macOS" button retrieves a disk image from `hxxps://y32me8[.]com/Wavel.dmg`. The DMG contains a compiled AppleScript that has no filename but only the `.scpt` extension. Because macOS hides file extensions by default in Finder, the `.scpt` file appears as a generic document to most users. Opening it launches Script Editor, the default handler for `.scpt` files. Upon following the instructions on the screen, an embedded JXA source is executed.

The compiled JXA format used here is identical to the one documented in PamStealer's first variant and in the earlier [Scoppr](https://x.com/MarceloRivero/status/2089510572043739308?s=20) and [Nancy](https://x.com/L0Psec/status/2089737386775265740?s=20) variants of the same family: a binary file beginning with the magic bytes `JsOsaDAS1.001.00`, followed by a binary property list containing the UTF-16BE encoded JXA source. What changed is what that source contains.

In Maccy, Scoppr and Nancy, the JXA source performed RC4 decryption of an embedded payload, made Objective-C framework calls through JXA's bridge to Foundation and NSData, and managed the entire download and staging process. In Wavel, the JXA source contains none of that. It holds a single large base64 string (`_b`, 24,868 characters) and one shell invocation:

The entire JXA layer is now a carrier. When Script Editor executes the file, it decodes the base64 string and pipes the result into `/bin/zsh -s`, where zsh reads and executes the decoded bytes from standard input. The JXA process exits immediately; the zsh dropper continues in the background.

## Stage 1: the zsh dropper and a server-side payload decryption chain

The decoded zsh script has a single function named `daemon_function`, launched in the background before exiting: `daemon_function & ; exit 0`. This causes the running function to be reparented when Script Editor terminates, severing the visible process ancestry and making the origin of subsequent child processes harder to trace in standard process monitoring tools.

`daemon_function` contains all of the dropper's logic: downloading and invoking the decryption utility, performing the key exchange, decrypting and staging the payload bundle, suppressing the background item notification, installing multi-layer persistence, and polling for and uploading the collected archive. The key constants are embedded in the function body:

All temp filenames are suffixed with `$$` (the current PID), so multiple invocations do not collide.

### pkgunpack: a purpose-built ECIES decryption utility

Rather than embedding the payload key in the dropper, this variant delegates decryption to a separate utility that performs a live key exchange with the server on each run. Without server cooperation, the payload cannot be recovered.

Before fetching the payload, the dropper downloads `pkgunpack`, a small Mach-O binary whose sole purpose is cryptographic:

`pkgunpack` is a FAT Mach-O supporting arm64 and x86\_64. It uses X25519 for key exchange (via a statically linked `curve25519_donna`) and AES-256-GCM with SHA-256 from CommonCrypto for the symmetric layers. It exposes two subcommands:

- `genkey`: generates a fresh ephemeral keypair and writes it to disk.
- `decrypt`: performs the full ECIES decryption sequence described below.

The steps following the download are produced by the dropper, not by `pkgunpack` itself: `xattr -cr` removes the quarantine attribute, and `codesign -fs - --deep` applies an ad-hoc signature. The ad-hoc signature is required for Gatekeeper to allow execution of a downloaded unsigned binary without triggering an authorization dialog. Worth noting: these two steps are produced by the dropper script rather than by `pkgunpack` or by any action of the user.

### Ephemeral key generation and a live DEK exchange

The dropper invokes `pkgunpack genkey` to produce a fresh ephemeral keypair for this execution:

It then sends the ephemeral public key and a freshness nonce to the server's key-exchange endpoint:

The server responds with a JSON body containing a `dek_wrap_b64` field: a blob beginning with the magic bytes `SNWK1`, followed by an AES-GCM IV, the encrypted DEK, and an authentication tag.

To recover the DEK, `pkgunpack` performs an X25519 key exchange between the ephemeral private key and a hardcoded server-side public key (`I6VuXPzLJfPEXgVRO5ycNXdMWHWvMAkrLMV6OpEuwDw=`). The resulting shared secret is run through SHA-256 with the domain separator `"sn-dek-wrap-v1"` to derive a key-encryption key, which is then used in an AES-256-GCM decryption to unwrap the DEK.

### Why the payload cannot be decrypted without server cooperation

The server holds the private key that completes the key exchange. Without it, the DEK cannot be recovered and the payload cannot be decrypted. Because a fresh ephemeral keypair is generated on every execution, a captured DEK wrap response cannot be replayed. The encrypted payload is therefore of limited value for static analysis without access to a live C2 session.

The payload envelope uses a parallel format, with the magic bytes `SNP1`:

The `X-Upload-Token` value is stable across all C2 requests for a given build and appears in every curl invocation the dropper makes.

### Payload extraction and staging

After decryption, the plaintext is a `tar.gz` archive. The dropper extracts it into a hidden temp directory:

The archive expands to `Wavel.app`. The dropper then copies the bundle to the permanent install location, renaming it:

The bundle is renamed from `Wavel.app` to `Finder.app` during this copy, while the internal executable retains its original name `r8afup9un0`. The ad-hoc signature and install path masquerade as a system component.

### Suppressing the background item notification

Before registering the LaunchAgent, the dropper suppresses the macOS notification that alerts users when a new background login item is added. It does this by pausing the relevant system processes before the `launchctl bootstrap` call:

After the LaunchAgent is registered, the dropper issues SIGKILL to each paused process in a loop until all three have exited:

This technique was absent from PamStealer earlier variants. Its presence in this variant reflects an awareness of the user-visible alerts.

### Multi-layer persistence repair

After installing the LaunchAgent, the dropper installs three redundant repair mechanisms, each carrying the marker comment `# sysnotif-repair`, so the dropper can detect whether any layer is already in place.

**LaunchAgent (**`com.apple.finder.agent`**).** The primary persistence job masquerades as a system component and runs at login and every 15 seconds thereafter, restarting on crash:

**Repair script (**`~/Library/Application Support/System/.repair-run`**).** A standalone zsh script that checks whether `Finder.app` is present and whether the LaunchAgent is registered. If either is missing, it restores both from a local backup tarball (`.sysnotif-backup.tgz`) stored alongside the installed bundle. The backup allows the repair to complete without any network contact.

**Shell hook (**`~/.zshrc`**).** The following block is appended to `~/.zshrc`, triggering the repair script in the background on every new interactive zsh session:

**Global Git hooks.** The repair script is copied to `~/Library/Application Support/System/.githooks/post-checkout` and `pre-commit`, and `git config --global core.hooksPath` is set to that directory. Any `git checkout` or `git commit` in any repository on the affected system will silently execute the repair script.

## Stage 2: from Rust to Swift based infostealer

The second stage (`r8afup9un0`) is a FAT Mach-O supporting arm64 and x86\_64 and is written in Swift. The first-generation PamStealer second stage was written in Rust, making this a notable toolchain shift while the collection objectives remain the same.

The binary's internal project name is `MacClient`, confirmed by the entry point `_MacClient_main`, the class name `MacClient.AuthPromptWindow` and the string `"MacClient archive: "` in the assembly. Four functions are exported by name: `_MacClient_main` (entry point), `_pam_verify_login` (PAM credential validation), `_kc_grab_storage_item` (keychain retrieval) and `_sqlite_backup_database` (browser database backup). Linked frameworks include AppKit, Security, `libpam.2.dylib` and `libsqlite3.dylib`.

### A dialog for password capture and a fake crash dialog

The binary includes a full AppKit-based decoy user interface implemented in the `AuthPromptWindow` class. The presentation follows a two-step sequence. An window follows with a "macOS wants to make changes" authentication prompt and a password field and a second window replicating the macOS "damaged and can't be opened" dialog, complete with native system icons to make it look legitimate.

The password entered is passed to `_pam_verify_login`, which validates it through the macOS Pluggable Authentication Modules interface using `"login"` as the service name. This is the same PAM-based credential validation approach that gave this family its name, now reimplemented in Swift. The binary also carries a `SONOMA_DISPLAY_NAME` environment variable that appears to control the application name shown in the prompt, though its precise use was not confirmed at the time of analysis.

### Keychain extraction with a two-step unlock

The exported function `_kc_grab_storage_item` uses `_SecItemCopyMatching` from Security.framework to enumerate and retrieve keychain items. Before making those calls, the binary shells out to `/usr/bin/security unlock-keychain` and `set-generic-password-partition-list` to unlock the login keychain and modify its access control list. The `KC_PERSIST_PROMPT` environment variable controls whether the keychain unlock prompt re-appears on subsequent access within the same session.

The login keychain database is also copied directly to the staging directory. The path template `"%s/Library/Keychains/login.keychain-db"` is used to locate it.

### Browser credential theft across seventeen targets

The exported function `_sqlite_backup_database` uses SQLite's built-in backup API to copy browser credential databases directly, without corrupting the source: `_sqlite3_open_v2` opens the source database in read-only mode, `_sqlite3_backup_init`initializes the copy to the staging path, and `_sqlite3_backup_step` and `_sqlite3_backup_finish` transfer and finalize it. The dropper kills browser helper processes before any data collection, which releases the file locks on browser profile databases and allows direct file copy without corruption. The kill command observed during dynamic analysis targeted `pkill -9 -fi 'Google Chrome Helper|Brave Browser Helper|Microsoft Edge Helper|Chromium Helper|Vivaldi Helper|Opera Helper|Firefox Helper'`.

Browser bundle IDs in the binary confirm seventeen targets. The standard Chromium and Firefox families are covered, including all four Chrome release channels (stable, Beta, Dev and Canary), Brave, Edge, Vivaldi, Opera and Opera GX, Chromium, and Firefox. Beyond that baseline the binary also targets Arc, Zen, Waterfox, LibreWolf, Yandex Browser and CocCoc. The inclusion of Arc, Zen and the less common regional and privacy-focused browsers extends the target list noticeably beyond what is typical in commodity macOS stealers.

The `Wavel.app` bundle embeds thirteen per-browser helper applications at `Contents/Resources/Helpers/`, each named `Helper_<Browser>Storage.app` with a `KcHelper` binary at `Contents/MacOS/KcHelper` inside. Analysis confirms that `r8afup9un0` resolves these helpers at runtime using `NSBundle.mainBundle.bundleURL`, appends `Contents/Resources/Helpers` as a path component, then launches each `KcHelper` with a set of environment variables (`KC_PASS`, `KC_STAGING`, `KC_SERVICE`, `KC_ACCOUNT`) that pass the keychain credentials and staging path it needs. Spawning per-browser helper processes allows each helper to present as its corresponding browser application, which can satisfy browser-specific keychain ACL entries without triggering a cross-app authorization prompt.

### System fingerprinting and user file (and photo) collection

System fingerprinting is performed through a series of `system_profiler` subprocesses. The binary collects 21 attributes covering hardware identifiers (hardware UUID, serial number, provisioning UDID, model identifiers, chip, firmware version), software state (system version, kernel version, boot volume, username, computer name, SIP status, secure virtual memory) and display information (GPU core count, Metal support, resolution). System uptime is calculated from `sysctl kern.boottime`.

Beyond credentials and system metadata, this stage also collects the user's profile photo. On macOS, the picture a user sets for their account, the one shown on the login screen and in System Settings, is stored as JPEG data in Open Directory, the local directory service. The binary reads it directly using `dscl` without touching the filesystem path most users would associate with their photo. It's notable that this potentially means a real photograph of the user is exfiltrated alongside the stolen credentials:

The spawned `dscl . -read ... JPEGPhoto` call is uncommon in stealers and in legitimate use.

User files collected include `.zsh_history`, `.zshrc`, `.bash_history` and `.gitconfig`, alongside the avatar image. Dynamic analysis confirmed `.zsh_history` was staged; `.zshrc`, `.bash_history` and `.gitconfig` are present as targets in the binary's string table but have not been present in the sandboxed environment.

Installed applications are enumerated with `lsappinfo list 2>/dev/null | head -200` and running processes with `ps -ax -o pid,comm 2>/dev/null | head -400`.

### Exfiltration: assembling and uploading the archive

After collection, it assembles the staging directory into an archive at a fixed path using `ditto`, which preserves resource forks and extended attributes:

A lock directory (`/tmp/.5ffa071d.zip.lockdir`) prevents concurrent assembly, and the atomic rename ensures the dropper's polling loop does not read a partial archive. During analysis the exfil archive was assembled and uploaded successfully.

The zsh dropper, which is still running from the initial execution, polls `/tmp/.5ffa071d.zip`, waits for three consecutive 2-second stability reads with identical size, validates the archive with `zip -T`, and uploads it with a single PUT request:

The `X-Upload-Token` header carries the same token used for all dropper C2 requests and is a stable IOC across all activity using this build.

## Behavior on an infected host

We detonated the sample in a sandboxed environment and captured the activity through dynamic analysis. The observed execution chain matches the static analysis and fills in the on-disk detail.

The observed execution chain proceeds as follows:

1. Script Editor opens `Wavel.applescript` and executes the JXA source, which spawns `sh`, then `zsh`. The `daemon_function`detaches from Script Editor via `& ; exit 0`.
2. `curl` downloads `pkgunpack` from `wavel.apple03cloudstore[.]com/pkgunpack` using the `X-Upload-Token` header. The file is written to `/tmp/.pkgunpack-<PID>`, the quarantine attribute is stripped, and an ad-hoc signature is applied.
3. `curl` downloads the encrypted payload from `wavel.apple03cloudstore[.]com/4e7a12e1c294f377/CoreUpdate.pkg.enc` to `/tmp/.core-<PID>.enc`.
4. `pkgunpack genkey` writes `/tmp/.eph-<PID>.key` and `/tmp/.eph-<PID>.pub`. The base64-encoded ephemeral public key observed in this execution: `sK2+KZYoZvdLRuLsID7OBopfce4n1fJqjVuML0SEC0Y=`.
5. `curl` POSTs to `/v1/loader/dek` with `{"eph_pub_b64":"sK2+KZYoZvdLRuLsID7OBopfce4n1fJqjVuML0SEC0Y=","nonce":"<ts>-<rand>-<PID>"}`. The server returns a 65-byte DEK wrap blob beginning with `SNWK1`.
6. `pkgunpack decrypt` performs the X25519 key exchange, SHA-256 KDF, DEK unwrap, and AES-256-GCM decryption of the payload to `/tmp/.core-<PID>.tar.gz`.
7. `tar` expands the archive to `/tmp/.upd-<PID>/Wavel.app/`. `BackgroundTaskManagementAgent`; `BTMNotificationAgent` and `NotificationCenter` receive SIGSTOP. `launchctl bootstrap gui/<UID>` registers `com.apple.finder.agent`. SIGKILL loops follow for each paused process.
8. `r8afup9un0` launches via `xpcproxy application.com.local.r8afup9un0.*` under the `com.local.r8afup9un0` sandbox container.
9. `r8afup9un0` spawns `bash` to kill browser helper processes via `pkill -9 -fi 'Google Chrome Helper|...'`, followed by 21 separate `system_profiler` subprocesses and a `dscl . -read /Users/admin JPEGPhoto` call writing to `/tmp/.avatar-<PID>.img`.
10. The staging directory `/tmp/.65486b/2966269/` is populated with `Password`, `Username` and `Mode` (all written atomically via sandbox-mediated rename), `Keychains/login.keychain-db`, `Browsers/`, `Extensions/`, `Wallets/`, `UserFiles/` and `u2whj/`.
11. `ditto -c -k --sequesterRsrc /tmp/.65486b/2966269 /tmp/.5ffa071d.zip.part` assembles the archive, which is renamed to `/tmp/.5ffa071d.zip`.
12. The dropper uploads the archive to `wavel.apple03cloudstore[.]com/v1/asset/1789753519-10913-1182`.

## Conclusion

This variant of PamStealer reflects a deliberate investment in delivery infrastructure. The pkgunpack utility introduces a live key exchange that ties payload decryption to server availability: without C2 cooperation, the second stage cannot be decrypted. That design makes static recovery of the payload significantly harder and shifts part of the operational control to the server operator. On the host, the persistence layer shows the same intent toward durability: four redundant repair mechanisms, two of which fire on routine user activity, combined with a local backup tarball that requires no network contact, make removal meaningfully harder than for families that rely on a single LaunchAgent.

The Swift rewrite of the second stage, retaining PAM-based validation as a named, exported function, is the clearest continuity marker between this variant and its predecessors. Together, these changes illustrate how this family continues to add operational controls over each stage of the attack chain while staying within the boundaries of standard macOS APIs.

Another indicator the threat actors are actively developing PamStealer is a finding posted by [L0psec](https://x.com/L0Psec/status/2099529962080366780?s=20) earlier this month on X that shares some similarities with our analysis and research.

Jamf Threat Labs continues to monitor this activity and track related infrastructure and variants. In Jamf for Mac, customers can configure threat prevention, advanced threat controls and web protection to **Block** and **Report** to help prevent the execution of similar threats.

## Indicators of compromise

Read the latest research from Jamf Threat Labs.
