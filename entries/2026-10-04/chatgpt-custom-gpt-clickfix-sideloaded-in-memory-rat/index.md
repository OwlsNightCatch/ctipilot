---
schema: 1
kind: threat
title: "A malicious ChatGPT Custom GPT sends users to a Google Sites ClickFix page that installs a sideloaded, in-memory RAT"
headline: "Huntress: a ChatGPT Custom GPT lure feeds a ClickFix chain that ends in a signed-host DLL sideload and a RAT"
summary: >
  Huntress describes a September 2026 campaign in which, in some incidents, a sponsored Google result for "chatgpt" opens an attacker-built
  Custom GPT on chatgpt.com, which sends the visitor to a Google Sites page showing a fake CAPTCHA and a ClickFix
  paste-and-run command. The command installs an MSI that starts a signed Canon application sideloading a malicious DLL,
  which unpacks a RAT with remote desktop, camera and microphone capture and DNS-over-HTTPS command resolution; Huntress
  has responded to at least 40 incidents from the Google Sites domain, two confirmed through a Custom GPT.
discovered_at: "2026-10-04T04:39:00Z"
updated_at: null
event_date: "2026-09-28"
run_id: 2026-10-04T0405Z-intel
priority: notable
immediate_action: null
tags: [phishing, ai-abuse]
regions: [global]
sectors: []
entities: ["campaign:chatgpt-custom-gpt-clickfix-rat-2026-09"]
techniques: [T1583.008, T1204.004, T1059.001, T1218.007, T1105, T1027, T1140, T1553.005, T1070.004, T1574.001, T1036.005, T1620, T1685, T1497, T1547.001, T1053.005, T1113, T1123, T1125]
affected_products: ["Microsoft Windows"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat"
    publisher: "Huntress"
    date: "2026-09-28"
    role: primary
closed_sources: []
evidence:
  - quote: "has responded to at least 40 incidents stemming from the specific Google Sites domain involved in this attack, and confirmed that two of these incidents came through a Custom GPT instance"
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat"
  - quote: "Most ClickFix chains we see are two or three hops: paste a command, download something, run it. This one has eight, and each hop exists to hide the next one."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat"
  - quote: "rules and URL filters that look for a dotted IP address never see one"
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat"
  - quote: "Detections tied to Canon or Stardock names will miss the next swap."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat"
  - quote: "Kill the process first, then remove both."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat"
verification: single-source
sourcing_note: >
  One first-hand source: Huntress's own SOC telemetry and its analysis of samples recovered from affected hosts. No
  independent confirmation was found, and the command-and-control address was not present in any recovered file.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Huntress reports a campaign from late September 2026 in which, in some incidents, victims who searched Google for "chatgpt" got a sponsored result that opened an attacker-built Custom GPT on the genuine chatgpt.com domain. It answers any input with a fake service-availability notice pointing to a "backup domain" on Google Sites, which shows a CAPTCHA and tells the user to paste a command into a terminal. The command fetches a layered, obfuscated script from a host written as a single decimal number, so "rules and URL filters that look for a dotted IP address never see one"; the script installs a hidden MSI with msiexec and deletes itself ([Huntress, 2026-09-28](https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat)).

The MSI presents itself as a printer-configuration reader, launches a legitimately signed Canon application, which loads a patched Canon logging DLL whose imports pull in unsigned DLLs; one XOR-decodes shellcode hidden in a file posing as audio. The shellcode bypasses AMSI, unhooks ntdll, runs anti-VM checks and hosts the .NET runtime, then opens a custom encrypted archive holding a persistence script and the remote access trojan. The script re-creates an HKCU Run value every 150 seconds and a scheduled task of the same name every 875 seconds if either is removed. The RAT offers remote desktop, camera, microphone and audio capture, file search and follow-on payload execution, and resolves its command server through DNS-over-HTTPS to public resolvers, "so they never appear in local DNS logs" ([Huntress, 2026-09-28](https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat)).

Huntress has responded to at least 40 incidents from the Google Sites domain and confirmed two through a Custom GPT. OpenAI took the first GPT down as of 2026-09-25; on 2026-09-27 Huntress found a replacement that swaps the signed host for a Stardock application, hides the loader in a Microsoft NuGet package, strips Mark-of-the-Web from the MSI and pulls a second script that is freshly obfuscated on every request, while the RAT is byte-identical ([Huntress, 2026-09-28](https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat)).

**Exposure:** any Windows endpoint whose user pastes the command; the chain uses no vulnerability, and staff who search for AI assistants are in scope.

**Detection:** process-creation telemetry with parent lineage is the most reliable place. Look for PowerShell launching msiexec on a GUID-named MSI in the user temp folder with silent flags; a signed vendor binary started by msiexec from a fake product folder under the user profile; an unsigned DLL next to the signed executable; and an HKCU Run value and scheduled task sharing one name that return after deletion. In proxy and egress logs, look for a decimal-integer download host and, inferred from the RAT's DNS-over-HTTPS command resolution, DNS-over-HTTPS from a non-browser process. Detections keyed on the Canon or Stardock names will miss the next swap, because the behaviors have so far carried over and the names have not ([Huntress, 2026-09-28](https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat)).

**Triage:** the signed Canon and Stardock host binaries are legitimate (Huntress: do not block globally); the discriminator is the same binary launched by msiexec from a fake product folder under the user profile, beside a same-named Run value and scheduled task that return when deleted ([Huntress, 2026-09-28](https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat)).

**Defender takeaway:** add these process-lineage and persistence patterns as hunts or detections now, keyed on behavior, not on the Canon or Stardock names. On an endpoint that matches, kill the implant process before removing its Run value and scheduled task, or the script restores both ([Huntress, 2026-09-28](https://www.huntress.com/blog/chatgpt-custom-gpts-clickfix-rat)).
