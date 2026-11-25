---
title: Music.app Race Conditions Enabled a macOS TCC Bypass
author: Jamf Threat Labs
url: https://www.jamf.com/blog/music-app-race-conditions-tcc-bypass/
hostname: jamf.com
description: Jamf Threat Labs found two symlink race conditions in Apple's Music.app that could replace the TCC database. Learn how they worked and why patching matters.
sitename: Jamfsoftware
date: "2026-11-18"
fingerprint: "9537dddebeb7538d"
language: en
image: https://media.jamf.com/images/news/2026/music-app-race-conditions-tcc-bypass.webp?h=400&q=80&w=700
pagetype: website
filedate: "2026-11-25"
---
# What happens when TCC gets bypassed? A look at Music.app race conditions

Jamf Threat Labs investigates now-patched vulnerabilities that allowed attackers to bypass macOS privacy controls.

**Author: Hu Ke**


Jamf Threat Labs discovered two symbolic link race conditions in Apple’s Music.app. On affected versions of macOS, an attacker could chain these vulnerabilities to replace the user’s Transparency, Consent and Control (TCC) database and gain unauthorized access to protected data.

**Both vulnerabilities are now patched.** Apple’s initial mitigation, released in macOS Sonoma 14.4 as **CVE-2024-23285**, reduced the maximum impact but left the underlying race conditions unresolved. The remaining issue has now been fixed in the latest macOS 27 Golden Gate under **CVE-2026-86933**. With both issues resolved, we can share a high-level account of the research and its implications for enterprise Mac security.

## TCC and the boundaries of user consent

TCC helps users control which applications can access sensitive information and capabilities on their Mac. The privacy protections expanded in the macOS Mojave era made permission prompts an increasingly familiar part of using macOS. These controls require applications to obtain consent for protected access, such as using the camera or microphone. Apple continued expanding these protections in subsequent releases. [Apple’s overview of macOS security](https://developer.apple.com/videos/play/wwdc2019/701/) describes this progression.

For example, an application requesting access to files on the Desktop may trigger a permission prompt. Behind that prompt, macOS must enforce the user’s decision across the operations that applications perform. [Apple’s platform security documentation](https://support.apple.com/en-hk/guide/security/secddd1d86a6/web) explains these file-access controls.

Consistent enforcement is difficult. Researchers have found multiple ways to bypass TCC over the years, revealing gaps between intended permissions and actual application behavior. Apple responds to these findings with security updates that strengthen the operating system. This research illustrates why that process sometimes requires both an initial mitigation and further work to address the underlying problem.

## From discovery to full resolution

The research and remediation progressed through several stages:

- **Discovery and reporting**: During routine analysis of application crash dumps, Jamf Threat Labs identified two Music.app bugs and determined that they could be chained to bypass TCC. We reported the findings to Apple.
- **2024 — Partial mitigation**: Apple addressed CVE-2024-23285 in macOS Sonoma 14.4 with improved symlink handling. Its advisory described the impact as: “An app may be able to create symlinks to protected regions of the disk.” This mitigation reduced the maximum impact of our findings but did not fully resolve the underlying issue. [Apple’s Sonoma 14.4 security advisory](https://support.apple.com/en-us/120895) documents the update.
- **Following the initial fix**: Apple’s initial fix reduced the impact of the vulnerabilities. However, symlink race conditions can affect several ways an application handles files, so fixing one operation does not necessarily fix the others. Our understanding is that Apple addressed this by strengthening sandbox protections, which limits what affected processes can access. The complexity of this work helps explain the longer timeline and reflects Apple’s ongoing efforts to protect user privacy. We waited until the remaining issue was resolved before sharing the technical details.
- **2026 — Final resolution**: The remaining issue has now been fixed in the latest macOS under CVE-2026-86933. Both vulnerabilities are resolved, allowing us to disclose this research.

## How Music.app’s file operations created an opening

A symbolic link, or symlink, points to another location in the filesystem. A race condition can arise when a path changes between the time an application examines it and the time the application performs an operation using it. If that change is not handled safely, an operation intended for one location can affect another.

Our research identified race conditions in two Music.app workflows: saved application state cleanup and media import. Combined, these vulnerabilities could let an attacker replace the user’s TCC database with one containing permissions chosen by the attacker.

### Saved application state cleanup

Music.app uses a saved application state directory as part of restoring and maintaining its application state. During launch, it performs cleanup operations that delete files from that directory.

A symlink race condition in this process could allow an attacker to redirect deletion toward a protected location. In the original exploit chain, that made it possible to delete the real TCC database at `~/Library/Application Support/com.apple.TCC/TCC.db`.

### Media import and copying

The second race condition involved Music.app’s media import path. Music.app uses MP3 metadata to organize imported media under `~/Music/Music/Media.localized/` and uses `clonefile()` to copy files into that structure.

A symlink race condition in this workflow allowed an attacker to redirect the copy operation. Combined with the deletion vulnerability, it enabled the attacker to place a controlled database where the legitimate TCC database had been.

The chain required precise timing after a single Music.app launch. The security consequence came from combining the two operations: deleting the legitimate database and replacing it with one that the attacker has built with their own custom permissions.

## Why control of TCC.db matters

The TCC database records permissions used to govern access to protected resources. Its integrity is therefore essential to enforcing user consent.

Replacing that database gives an attacker control over the permission decisions it contains. In the original chain, this enabled a full TCC bypass, exposing all TCC-protected data to unauthorized access. The impact extended beyond an individual file operation: the attacker could undermine the mechanism responsible for deciding whether access should be allowed.

Our video demonstration illustrates how the vulnerabilities could affect access to protected files on an affected macOS version. It also highlights the importance of Apple’s ongoing work to strengthen macOS privacy protections and safeguard user data.

## Stronger protection through defense in depth

TCC remains an important part of macOS security. These findings show how vulnerabilities in ordinary application workflows can undermine a broader privacy boundary and why resolving the underlying issue matters even after an initial mitigation reduces its impact.

Both vulnerabilities are now patched. Enterprise Mac administrators should ensure their fleets receive the macOS updates containing the fixes and treat timely patching as part of a layered security strategy. Permission controls, endpoint protection, and the ability to detect and respond to malicious activity all contribute to that defense.

Read the latest research from Jamf Threat Labs.
