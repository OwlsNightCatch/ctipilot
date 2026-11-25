---
title: Fake Zoom Installer Delivers Overlord RAT on macOS
author: Jamf Threat Labs
url: https://www.jamf.com/blog/fake-zoom-installer-delivers-overlord-rat-macos/
hostname: jamf.com
description: Jamf Threat Labs exposes a macOS malware campaign using a fake Zoom installer to drop the Overlord RAT via a .NET downloader — learn more.
sitename: Jamfsoftware
date: "2026-08-06"
fingerprint: "25fd451d259b1187"
language: en
image: https://media.jamf.com/images/news/2026/threat-labs-blog-mac.webp?h=500&q=80&w=800
pagetype: website
filedate: "2026-11-25"
---
# Fake Zoom installer uses .NET downloader to deliver Overlord RAT on macOS

Jamf Threat Labs uncovers a macOS campaign using a fake Zoom installer to deploy Overlord RAT. Built with .NET, this cross-platform technique simultaneously targets Windows, joining Go- and Rust-based cross-platform malware.

*By: Ferdous Saljooki*

## Introduction

Jamf Threat Labs recently identified a campaign using a fake Zoom installer to deliver a configured build of [Overlord](https://github.com/vxaboveground/Overlord), an open-source remote access framework, hosted on attacker-controlled infrastructure. The downloader is a macOS ARM64 Mach-O binary named `ZoomMeetings`, built as a self-contained .NET 10 single-file application with the .NET runtime bundled inside.

Rather than the Go or Rust we typically see in macOS malware, this downloader uses .NET, whose cross-platform support means the same codebase also targets Windows. Building macOS malware using the .NET framework is fairly uncommon, so naturally this caught our attention. Our curiosity led to a number of interesting finds that we'll share in this blog post.

## Stage 1: the downloader

The malware downloader, found on VirusTotal, was disguised as a Zoom installer called `ZoomMeetings`(`7a2318127cabf28552a8aeed14a8445c8f36fbda5e57d8b122cf6f1c6b51a522`). Its code is obfuscated: method and field names are replaced with sequences like `__o_8ca0ad3ec7b40770` and `__obf_proxy_0`. At the time of analysis it was undetected by static engines on VirusTotal and its initial delivery vector is still under investigation.

As part of .NET's self-contained single-file deployment, the executable bundles all required runtime libraries using the Portable Executable (PE) format. This allows the downloader to run without .NET being pre-installed on the victim's system. Even on macOS, .NET assemblies use the PE format as their container for Intermediate Language bytecode, a platform-agnostic instruction set that the runtime executes. The outer wrapper is a native Mach-O binary that macOS can execute, but inside it contains PE files, the same format used by Windows DLLs. They can be extracted by scanning `ZoomMeetings`for `MZ` magic bytes with valid PE signatures, which located 34 DLLs. The first contained two plaintext strings in its header: `"Zoom Communications, Inc"` and `"Zoom Meetings Installer"`, distinguishing it from the remaining 33, which were standard .NET runtime libraries.

The metadata for the extracted DLL uses values commonly seen in legitimate Zoom installers.

The malicious DLL (`b5f1a21dcd315676a4a9217a40ef830c159121528114c6436e671c2fa5455681`) was decompiled with [ilspycmd](https://github.com/icsharpcode/ILSpy), revealing the obfuscated C# string table.

The downloader decodes each base64 string before XOR'ing with key `0x94` to recover the plaintext using the following logic:

Decoding the string table recovers the attacker's infrastructure, payload URLs and both legitimate Zoom installer URLs.

### Fingerprinting and payload selection

The downloader starts by identifying the operating system and architecture using .NET's `RuntimeInformation` APIs:

Based on the result, it fetches one of three platform-specific payloads from attacker-controlled infrastructure:

The `ts=` parameter is a 6-character random alphanumeric token generated each run:

The server requires the `ts=` token; requests without one return a 401.

### Execution

On macOS, the downloader writes the stage 2 binary to `/tmp/ZoomMeetings` and launches it via a backgrounded `nohup` command, allowing it to avoid termination when the downloader exits.

Concurrently, it fetches the real Zoom installer to maintain the lure. On macOS it downloads the `.pkg`; on Windows the `.exe`:

By the time anything suspicious happens on the machine, Zoom is installed and working.

The downloader prints the following, regardless of whether the payload download succeeded:

A second .NET downloader (`d4cf150d6effeea315f136cdf448e32f4a8daac9e95f46def6a31ba18787dae3`) named `ZoomInstallerFull` was identified on VirusTotal using the same infrastructure. The binary contains an embedded debug path `/Users/ollie/Documents/TheEgg/obj/Release/net10.0/osx-arm64/linked/ZoomInstallerFull.pdb` revealing a developer username (`ollie`) and project name (`TheEgg`). Unlike the obfuscated build, its strings are in plaintext.

## Stage 2: the Overlord agent

The second stage (`2c0bb97632bb9b90ee97be2ac350a557b08d84a7dad1f3ef63ffd83be1ab1f00`) is a Mach-O ARM64 binary hosted on the attacker server as `zoomMacArm` and saved to disk at the path `/tmp/ZoomMeetings`. It is built from the Overlord framework, compiled with garble obfuscation, and carrying a hardcoded C2 server address.

Overlord is publicly available on GitHub, where the author describes it as a cross-platform RAT with agents connecting over encrypted WebSockets.

### Obfuscation

This build is compiled with garble, which Overlord's standard build does not apply. Garble mangles function, type and package names in Go's `pclntab` and obfuscates the `moduledata` structure that tools use to locate it, breaking static analysis tooling. [GoReSym](https://github.com/mandiant/GoReSym), which has specific recovery strategies for garbled binaries, could not resolve a function table on this sample:

Its byte scan surfaced `pclntab` magic candidates, but none could be validated. The mangled source paths are visible in the binary:

### Persistence

Overlord contains a LaunchAgent persistence routine with a plist template embedded in the binary. In our run this routine did not fire: the agent connected to its C2 without writing a LaunchAgent. The framework exposes an `OVERLORD_ENABLE_PERSISTENCE` toggle, so persistence is opt-in rather than automatic.

### C2 configuration

The agent connects to its C2 over a secure WebSocket. In this build the hardcoded default server is `hub.zoom.com[.]kg:5173`. This build defaults `TLSInsecureSkipVerify` to `true`, so certificate validation is disabled.

The framework also ships with a Solana-based C2 resolver that can read server addresses from blockchain transactions instead of a fixed URL. It is disabled by default in this build: the toggle resolves to `false` and no wallet or RPC endpoint is configured. This sample uses the hardcoded WebSocket address above, not Solana.

### Capabilities

The following capabilities are present in the [Overlord framework](https://github.com/vxaboveground/Overlord):

- **Keylogging**: captures keystrokes system-wide via `CGEventTap`
- **Screen capture**: captures the display and streams frames to the operator
- **Audio capture**: captures microphone audio via miniaudio
- **Webcam access**: captures video from the device camera
- **System info**: collects CPU, RAM, battery, macOS version, architecture and admin status
- **Filesystem**: browse, read, write, upload, download, move, rename, delete, chmod and zip
- **Process control**: list, kill, suspend and resume
- **Script execution**: runs commands via bash, python3, ruby, node, perl or PowerShell (`pwsh`)
- **Plugin system**: loads native dylibs or WebAssembly modules from the C2 at runtime
- **Self-update**: replaces the agent binary with a new version from the C2
- **Remote desktop streaming**: streams the desktop to the operator over WebSocket or WebRTC peer-to-peer
- **Persistence**: installs a LaunchAgent; gated by `OVERLORD_ENABLE_PERSISTENCE`
- **Solana C2 resolver**: resolves C2 addresses from Solana blockchain transactions

## Additional sample: `ZoomMeetings (Overlord variant)`

A second binary (`7878031f2bd907e7300133b3e8ce640f3cdcba56686eaca3539d4c22773bc233`) was identified on VirusTotal, also named `ZoomMeetings`, with the same hardcoded C2 (`hub.zoom.com[.]kg:5173`) but a different hash. Dynamic analysis confirmed it is a second Overlord build, differently configured from the first.

Unlike `zoomMacArm`, persistence fired immediately on first run. The binary copies itself to `~/Library/Application Support/Overlord/com.zoom` and installs a LaunchAgent at `~/Library/LaunchAgents/com.zoom.plist` with label `com.zoom`.

On first run, the variant spawns `ioreg -rd1 -c IOPlatformExpertDevice` before connecting to its C2, retrieving the hardware UUID, serial number and model identifier.

## Ongoing similarities

Zoom-based lures and open-source RAT frameworks have featured in multiple macOS campaigns Jamf Threat Labs has tracked. Overlord was also used by UNK\_DeadDrop, a cluster [Proofpoint assesses as likely North Korean](https://www.proofpoint.com/us/blog/threat-insight/dont-fear-repo-unkdeaddrop-phishing-campaign-targets-developers-steal), though no direct overlap has been identified between that activity and this campaign. The Overlord variant observed here shares a LaunchAgent label (`com.zoom`) and plist name (`com.zoom.plist`) with FlexibleFerret, a DPRK-attributed macOS malware family associated with the Contagious Interview campaign and [documented by SentinelOne](https://www.sentinelone.com/blog/macos-flexibleferret-further-variants-of-dprk-malware-family-unearthed/) in February 2025. The use of .NET as a macOS downloader is a technique we had not previously observed in campaigns of this kind. Jamf Threat Labs has noted the similarities but does not currently attribute this malware to a specific threat actor.

## Conclusion

The .NET downloader is the most notable finding in this campaign. Threat actors targeting macOS have previously leveraged cross-platform languages such as Go and Rust to reduce development overhead. .NET now joins that list, with its cross-platform support enabling a single codebase to target both Windows and macOS.

Jamf Threat Labs will continue to monitor this activity. In Jamf for Mac, customers can configure threat prevention, advanced threat controls and web protection to Block and Report to help prevent the execution of similar threats.

## Indicators of compromise

Read the latest research from Jamf Threat Labs.
