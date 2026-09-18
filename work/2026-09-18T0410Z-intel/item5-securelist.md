---
title: "MovieReaper: Trojan attack via movie torrents, including \"The Odyssey"
author: Konstantin Isakov; Pavel Cheremushkin
url: https://securelist.com/moviereaper-malware-torrent-odyssey-solana/121344/
hostname: securelist.com
description: Kaspersky experts have discovered a new MovieReaper campaign. The multi-stage Trojan spreads through movie torrents, such as "The Odyssey," and uses the Solana blockchain to hide its C2 infrastructure.
sitename: Securelist
date: "2026-09-17"
tags: ['Malware Technologies,shellcode,Torrent']
---
## Introduction

Torrent trackers have long been abused for distributing malicious software, disguised as popular films, games, and other content. Our previous research has shown that cybercriminals repeatedly turn torrents as an initial infection vector, using trojanized cracks and installers to reach a large number of users. Installation guides for pirated software routinely instruct users to disable their antivirus, conditioning them to ignore potential threats they are inviting onto their computers.

During our analysis of malware that leverages blockchain networks for its C2 infrastructure, we have discovered a previously unknown modular, multi-stage framework that we dubbed MovieReaper. This report details the new crimeware campaign that began with the mass infection of users via compromised torrent tracker file storage. We have identified several hundred victims, including both individual users and organizations in a multitude of countries, such as Russia, Türkiye, Japan, Kenya, Uganda, and Colombia, as well as in several European countries like Spain, the Netherlands, Belgium, Germany. We analyze the techniques used to evade detection by security and sandbox solutions, examine the capabilities of the modular framework.

Kaspersky products detect this threat as HEUR:Trojan.Win64.Agent.gen.

## Technical Details

### Background

In mid‑August 2026, during our threat‑hunting efforts, we identified a large‑scale infection campaign involving previously unknown malware disguised as popular movies. The campaign affected both individuals and organizations across multiple countries. Our initial analysis revealed a common factor among the victims: all had used torrent trackers. This finding prompted us to investigate the campaign further and analyze its distribution mechanism, overall scope, and unknown malware implants.

### Initial infection and spreading

Compromised torrent trackers are the primary vector used to distribute malware. During our investigation, we identified multiple user reports describing suspicious files being downloaded instead of the intended content.

For example, a user of a popular movie torrent tracker reported the following case on Reddit:

Further analysis of the attack revealed that the threat actors did not compromise the torrent trackers themselves. Instead, they compromised a widely used public repository of torrent files — `itorrents[.]org`. As a result, torrent trackers that relied on this repository began inadvertently distributing malicious torrent files to their users. This approach is particularly powerful because the threat actors can reach users of multiple tracчkers without compromising each platform individually.

As of the publication date of this report, the archive remains compromised. When a user attempts to download a torrent using a magnet link, the legitimate torrent archive instead returns a different torrent file. This malicious torrent leads to the download of the malware loader. It is used to deploy a framework that we dubbed MovieReaper.

The loader initiates the infection chain, which is illustrated in the diagram below. Each stage of the infection chain is described in detail in the following sections.

### Malware implants

The infection chain consists of several steps, where only the initial one is dropped on the disk before its execution to avoid detection. The malware itself is not heavily obfuscated, apart from the fact that strings are encrypted with a custom stream cipher. Most of the countermeasures were aimed at avoiding detection by AV sandboxes.

#### Step 1: Loader

The most popular initial executable was distributed through torrent trackers under many different names (for example, `the odyssey (2026) [1080p] [webrip] [5.1].exe`), but the file hash (MD5: `A0B13781EDD7CFDAB13D79AFFF3C83C1`) was identical across all downloads. We have seen multiple different loaders, where the executable file disguises itself with a long filename and an icon of some well-known application. Most of the filenames are rather large, presumably, to hide the “.exe” extension at the end.

After the user manually starts the application, it establishes a global mutex to ensure that only one loader is executed at a time. We have seen several variations of a mutex in our samples, which contain a randomly generated string (in example `Global\fnulSktzSqvVLXHU`). Then this executable performs the series of operations in order to avoid detection by the AV sandbox solutions.

While performing those operations, the malware avoids making `LoadLibrary` and `GetProcAddress` calls in order to acquire addresses of required functions. Instead, it searches for loaded libraries by traversing the double-linked list taken from the Ldr field of PEB and then performs manual parsing of loaded DLL to calculate the address of function.

After all the initial checks have passed, this binary prepares to perform network connection to a C2 web-server to download the shellcode, map it into the RWX memory and execute. While doing it, loader decodes `https://deadhub[.]org` domain name and if connection to it has failed, then it uses the IP address `http://193.23.118[.]155` as a fallback and connects to it using plain HTTP. Malware chooses a random group of strings and uses them as a path in the HTTP request to download parts of a shellcode.

Example URLs:

`/cloud/v192.4/ui/sync-status-icons.png`

`/cloud/v192.4/onboarding/welcome-bg.jpg`

`/cloud/v192.4/ui/file-preview-placeholder.png`

`/cloud/v192.4/shared/link-banner.jpg`

While mapping the address space and executing the shellcode, the loader registers a vectored exception handler and rewrites the handler address in memory in order to perform a debug break, which will not crash the program, but instead redirect control-flow into the function that actually makes raw `NtProtectVirtualMemory` syscall (via previously located “0x0F 0x05” syscall instruction inside `ntdll`). Then it calls an undocumented ntdll function EtwpCreateEtwThread, which is a popular alternative to a CreateThread to perform code execution and executes the shellcode.

#### Step 2: Shellcode

The second stage of this malware performs an HTTPS request to the Solana blockchain at the `/getAccountInfo` endpoint for the `6pnDGAiHgyPdmckM5Qt1YbanGzrX43WLEU159nRaNLDm` account. The data field of the response contains the base64‑encoded address of a second C2, which is encrypted with a static XOR key located within the shellcode itself. To store data in this account, attackers used a simple Solana program (address: `CSiY8bQLBYPdfPWkwipBzH6sijTVQVVsA279JQdvwHtL`).

By using Solana blockchain network as a distribution layer of endpoints for a next stage attackers may increase stability of their campaign and resist takedown efforts of defenders.

The second stage payload communicates with its C2 server strictly through HTTPS via TLS-pinned certificate using nanopb protobuf library as a container for transferred data. The main logic of stage 2 implant contains several initial commands, where the most important is the one that parses the COFF file and loads it to the memory, and executes the `module_init` function from it. It provides a convenient interface for extension of the command list, which leads us to the next stage of the payload.

#### Step 3: UAC Bypass and persistence

Notably, the recovered modules were compiled with symbols, which accelerated reverse engineering.

After receiving the next stage from the second C2 server, the newly loaded module performs several tasks right in the `module_init` function.

Stage 3 performs UAC Bypass and achieves persistence using public techniques, masquerades the original binary as `C:\ProgramData\Microsoft\Windows\Telemetry\msedge.exe`, and restarts itself.

The respawned process starts with the initial loader, but with a special command-line argument, which allows it to skip most of the anti-sandboxing checks and proceed straight to the download of the stage 2. The executable proceeds with the same steps as before, but this time, instead of downloading persistence and UAC bypass module, the new one is downloaded from the second C2 server, because there is a flag being sent to a remote server that indicates whether the implant is running from the Telemetry folder is sent in the beacon, allowing the C2 to distinguish first-run and respawned instances.

#### Step 4: The final implant

The final module (“file manager”) exposes 21 commands that give the operator filesystem access on the victim host. It allows remote operator to download, upload, read files on the system, list and enumerate directories, manipulate files using create, copy, rename, move, delete, chmod, symlink commands, use preview and thumbnail commands to exfiltrate previews of images and files before actually extracting them.

We suspect that other modules may be loaded on-demand by the request of the operator.

## Infrastructure

During this malware campaign, attackers use various commercial hosting providers for their C2 infrastructure (see IoC section for details). Furthermore, as noted above, the campaign leverages the legitimate Solana blockchain via the `api.mainnet.solana.com` RPC endpoint to deliver the address of the second‑stage C2 server to the malware. This approach provides the attackers with decentralized storage for C2 addresses, adding an additional layer of resilience and making it more difficult for defenders to disrupt the campaign by simply blocking the IP addresses of the C2 servers.

## Victims

The observed campaign targeted both individuals and organizations across Europe, Asia, and Africa, with infection attempts identified in countries including Russia, Spain, Germany, Finland, Türkiye, Japan, Nepal, Kenya, Tanzania, Ghana, and others. The targeted organizations span a wide range of sectors, including enterprise, government, IT, consulting, retail, transportation, and agriculture.

## Conclusions

Our research uncovered activity of the same actor, dating back to October 2025. The campaign has evolved over time with the malware authors expanding their arsenal, making the loader harder to detect, although the pattern remains the same: encoded strings, parts of shellcode are downloaded through the plain HTTP protocol, several techniques are used to avoid sandboxes and virtual machines. We will continue monitoring this actor’s activity to catch new potential threats.

The first stage offers the clearest opportunity to disrupt this campaign, as it relies on a single specific domain name and a single IP address to serve the shellcode, meaning that taking down this server would prevent the infection chain further. This includes the second-stage payload, which uses the Solana blockchain network for C2 and is, therefore, more resistant to conventional infrastructure takedowns.

However, this framework’s self-containment, modularity and in-memory execution has its potential to be reused in later campaigns with minimal rework.

## Indicators of compromise

### File hashes

### File paths

%ProgramData%\Microsoft\Windows\Telemetry\msedge.exe

### Mutexes

Global\E4AyDKzvEhe2hgAr

Global\fnulSktzSqvVLXHU

### Domains and IPs

First-stage C2:

[deadhub\[.\]org](https://opentip.kaspersky.com/deadhub.org/results?icid=gl_sl_post-opentip_sm-team_369b95308445984a&utm_source=SL&utm_medium=SL&utm_campaign=SL)

[193.23.118\[.\]155](https://opentip.kaspersky.com/193.23.118.155/results?icid=gl_sl_post-opentip_sm-team_059e95cfa9fc9c9c&utm_source=SL&utm_medium=SL&utm_campaign=SL)

Second-stage C2:

[208.64.33\[.\]90](https://opentip.kaspersky.com/208.64.33.90/results?icid=gl_sl_post-opentip_sm-team_3882023dc2e8d791&utm_source=SL&utm_medium=SL&utm_campaign=SL)

[208.94.246\[.\]53](https://opentip.kaspersky.com/208.94.246.53/results?icid=gl_sl_post-opentip_sm-team_0380ca162178fee7&utm_source=SL&utm_medium=SL&utm_campaign=SL)

The Odyssey and trojans again: MovieReaper attacks users in multiple countries via compromised torrents
