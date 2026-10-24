---
schema: 1
kind: threat
title: "Armored Likho: new APT hits government and electric-power targets with an AI-generated loader and the Python 'BusySnake' stealer"
headline: "Kaspersky names Armored Likho — spear-phishing into an LLM-written loader chain that stages a full Python runtime and a PyArmor-protected stealer"
summary: >
  Kaspersky documented (2026-07-03) Armored Likho (aka Eagle Werewolf), a previously unknown APT
  targeting government agencies and the electric-power sector across Russia, Brazil and Kazakhstan.
  Spear-phishing delivers an NSIS dropper or a ZDI-CAN-25373 LNK lure whose loader — assessed as
  LLM-generated — stages a bundled Python 3.12 runtime and the PyArmor-protected BusySnake Stealer
  from rotating GitHub repositories. Campaign active at publication; concrete low-noise hunt pivots
  exist. Published as an audit-recovered item: the primary fell inside the 2026-07-07 scheduler
  outage's backfill blind spot.
discovered_at: "2026-07-11T17:40:00Z"
event_date: "2026-07-03"
run_id: 2026-07-11T1435Z-audit
priority: notable
immediate_action: null
tags: [espionage, phishing, infostealer, ai-abuse]
regions: [russia-cis, latam]
sectors: [public-sector, energy]
entities: [actor:armored-likho, malware:busysnake-stealer]
techniques: [T1566.001, T1204.002, T1027, T1055, T1053.005, T1059.001, T1059.006, T1608.001, T1555.003, T1539, T1115, T1113, T1005, T1572, T1219]
affected_products: []
cves: []
sources:
  - url: "https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/"
    publisher: "Kaspersky Securelist"
    date: "2026-07-03"
    role: primary
closed_sources: []
evidence:
  - quote: "This targeted campaign focuses heavily on government agencies and the electric power sector. The geographical footprint of these attacks spans Russia, Brazil, and Kazakhstan, establishing the group as a global threat actor."
    publisher: "Kaspersky Securelist"
  - quote: "This coding style is highly uncharacteristic of human-developed malware. It strongly indicates that the group is leveraging LLMs to generate their malicious payloads."
    publisher: "Kaspersky Securelist"
verification: single-source
sourcing_note: "Single-source: Kaspersky is the sole publisher at time of writing (research-lab primary with full technical analysis; no independent corroboration found in-window). Kaspersky's attribution of the campaign to a single new group, and the Eagle Werewolf overlap, are the vendor's own assessments — the alias is flagged by Kaspersky itself as based on circumstantial evidence."
confidence: medium
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
migrated_from: null
---

Kaspersky's threat-monitoring team published a full analysis of a previously unknown APT it dubs Armored Likho (also tracked, on circumstantial evidence, as Eagle Werewolf), which mixes financially motivated campaigns against individuals with targeted espionage against organizations — the current campaign, still active at publication, concentrates on government agencies and electric-power-sector organizations in Russia, Brazil and Kazakhstan ([Kaspersky Securelist, 2026-07-03](https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/)). Initial access is spear-phishing with government-notice and social-program themes carrying archive attachments. One variant drops an NSIS self-extracting dropper that shows a decoy "psychological test" survey, writes a legitimate `pnx.exe` to a temp directory and injects loader code into its process memory; the other abuses the ZDI-CAN-25373 Windows shortcut-display weakness — whitespace/line-break padding that hides the LNK's real command line from the user — to launch obfuscated PowerShell. Both paths converge on a loader that Kaspersky assesses was written by an LLM (verbose comments and bullet-point emojis "highly uncharacteristic of human-developed malware") — a concrete case of AI-generated first-stage tooling blurring the actor's TTP fingerprint and complicating attribution ([Kaspersky Securelist, 2026-07-03](https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/)).

The loader pulls its payload packages from attacker-controlled GitHub repositories whose contents and names rotate automatically, then stages everything under `%APPDATA%\WindowsHelper`: a bundled Python 3.12 interpreter, `get-pip.py` for dependency installation, and the primary payload `module.pyw` — BusySnake Stealer, a Python infostealer obfuscated with PyArmor Pro 9.2.0 that decrypts each function's bytecode only at call time and re-encrypts it afterward. Persistence is a VBScript launcher (`run.vbs`) registered as a scheduled task re-executing the payload every five minutes; a companion `wh_selfdelete.vbs` wipes the initial loader. On tasking from its C2, the stealer harvests Chromium credentials via DPAPI and Firefox credentials via `PK11SDR_Decrypt`, steals browser cookies (in one command variant by installing a browser extension), scrapes the clipboard and local files for 64-character hex keys and `otpauth://` OTP seeds, inventories and exfiltrates user documents under 5 MB, captures screenshots, packages Telegram `tdata` session stores after force-killing `telegram.exe`, hunts cryptocurrency-wallet JSON files, opens a reverse-SSH tunnel with a C2-supplied key, and abuses RustDesk — downloading it if absent, or restarting it to make the user re-enter their ID/password while screenshotting the credentials ([Kaspersky Securelist, 2026-07-03](https://securelist.com/tr/armored-likho-apt-with-busysnake-stealer/120292/)).

**Defender takeaway:** the chain is long but noisy in telemetry classes most estates already collect. In process-creation telemetry, alert on script interpreters or unknown binaries spawning a bundled/user-writable Python interpreter (`python.exe`/`pythonw.exe` executing from `%APPDATA%`), on `.pyw` files registered in scheduled tasks, and on `wscript.exe` launching from `%APPDATA%\WindowsHelper`-style working directories; in network telemetry, surface hosts fetching archives from GitHub release repositories outside development context, and outbound SSH from hosts with no SSH business. **Triage:** developer machines legitimately run user-installed Python — the discriminators are the scheduled-task-driven five-minute re-execution cadence, the interpreter living under `%APPDATA%` rather than a managed install path, and RustDesk (re)starts the user did not initiate; any one alone is weak, the combination is the signal. For the profiled constituency this is transferable tradecraft knowledge, not an active home-region threat — no Swiss or EU targeting is reported.

*Provenance note: this entry was published by the 2026-07-11 full-store quality audit, which found the item had fallen into the 2026-07-07 scheduler outage's backfill blind spot (research-blog publications do not route through the KEV/CERT catch-up paths the backfill run swept — pipeline fix shipped as prompts v3.21).*
