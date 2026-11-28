---
schema: 1
kind: threat
title: "FamousSparrow's three-wave intrusion at an Azerbaijani oil and gas company: repeated ProxyNotShell access, Deed RAT behind a two-export LogMeIn Hamachi sideload, and a blocked TernDoor attempt"
headline: "China-nexus FamousSparrow re-entered an Azerbaijani energy firm three times through the same unpatched Exchange server"
summary: "Bitdefender documented an intrusion at an Azerbaijani oil and gas company from late December 2025 to late February 2026 that it attributes with moderate-to-high confidence to the China-nexus FamousSparrow cluster. The attackers came back three times through the same vulnerable on-premises Exchange server (ProxyNotShell), ran Deed RAT through a LogMeIn Hamachi binary whose malicious loader splits its trigger across two exports and a hooked StartServiceCtrlDispatcherW call, attempted TernDoor in a second wave that security software blocked, and moved laterally with a domain administrator account over RDP and Impacket-style tools."
discovered_at: "2026-05-14T05:00:05Z"
event_date: 2026-05-13
run_id: 2026-05-14-e05c6e6e
priority: notable
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
  - cisa-kev
regions:
  - russia-cis
sectors:
  - energy
entities:
  - "actor:famoussparrow"
  - "campaign:famoussparrow-azerbaijan-2026"
  - "malware:deed-rat"
  - "malware:terndoor"
  - "malware:mofu-loader"
techniques: [T1190, T1505.003, T1574.001, T1543.003, T1569.002, T1036.005, T1140, T1027, T1055, T1112, T1071.001, T1078.002, T1021.001, T1059.001, T1105, T1021.002, T1014]
affected_products: ["Microsoft Exchange Server"]
cves:
  - id: CVE-2022-41040
    cvss: "8.8"
    epss: null
    type: ssrf
    vector: zero-click
    auth: post-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: "Exchange Server without the 2022-11-08 security updates"
    fixed: "Exchange Server security updates of 2022-11-08"
  - id: CVE-2022-41082
    cvss: "8.0"
    epss: null
    type: deserialization
    vector: zero-click
    auth: post-auth
    status:
      - exploited
      - cisa-kev
      - patch-available
    affected: "Exchange Server without the 2022-11-08 security updates"
    fixed: "Exchange Server security updates of 2022-11-08"
sources:
  - url: "https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry"
    publisher: "Bitdefender"
    date: "2026-05-13"
    role: primary
  - url: "https://thehackernews.com/2026/05/azerbaijani-energy-firm-hit-by-repeated.html"
    publisher: "The Hacker News"
    date: "2026-05-13"
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41040"
    publisher: "Microsoft Security Response Center"
    date: "2022-09-30"
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082"
    publisher: "Microsoft Security Response Center"
    date: "2022-09-30"
    role: corroborating
  - url: "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    publisher: "CISA KEV catalog"
    date: "2022-09-30"
    role: corroborating
  - url: "https://microsoft.github.io/CSS-Exchange/Diagnostics/HealthChecker/"
    publisher: "Microsoft CSS-Exchange (HealthChecker)"
    date: "2025-10-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "This context does not establish motive. We have N=1 victim and moderate-to-high attribution confidence."
    publisher: Bitdefender
    source_url: "https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry"
  - quote: "the attackers returned to the same vulnerable Exchange server nearly a month after the initial compromise attempt"
    publisher: Bitdefender
    source_url: "https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry"
  - quote: "The attempt was unsuccessful, as the security solution blocked execution before the malware could complete its installation."
    publisher: Bitdefender
    source_url: "https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry"
  - quote: "Legitimate Exchange maintenance workflows rarely write web-accessible script files through the IIS worker process."
    publisher: Bitdefender
    source_url: "https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry"
  - quote: "Yes, the attacker must be authenticated."
    publisher: Microsoft Security Response Center
    source_url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082"
verification: multi-source
sourcing_note: >
  Bitdefender's incident-response and malware research is the only account of the intrusion, and The Hacker News
  reports it; Bitdefender's attribution is moderate-to-high confidence. Microsoft's advisories and CISA's catalogue carry
  the ProxyNotShell scores, the authentication requirement and the exploitation status, which contradict Bitdefender's
  description of the chain as unauthenticated.
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
migrated_from: briefs/2026-05-14.md
updated_at: null
updates:
  - at: "2026-10-21T20:26:12Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      Bitdefender gives Azerbaijan's European gas role as context that does not establish motive and
      attributes the intrusion to the China-nexus FamousSparrow cluster with moderate-to-high confidence,
      not to Chinese state actors as fact. The sideload is an evolved technique closely matching a Deed
      RAT loader Trend Micro documented for Earth Estries, the second wave's TernDoor installation was
      blocked before it completed, and the re-entries came through the same still-vulnerable Exchange
      server rather than through surviving persistence. Microsoft says ProxyNotShell requires
      authentication, while Bitdefender calls it unauthenticated.
    fields: [affected_products, body, classification, cves, entities, evidence, headline, regions, sources, sourcing_note, summary, tags, techniques, title, priority]
---

**Background.** Bitdefender tracked an intrusion at an Azerbaijani oil and gas company from late December 2025 to late February 2026 and attributes it with moderate-to-high confidence to FamousSparrow, citing substantial overlap with the Earth Estries toolset and tradecraft; earlier public reporting placed the cluster against telecoms, government and technology targets in the United States, Asia-Pacific, the Middle East and South Africa, and this is the first public link to energy targets in the South Caucasus ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). Bitdefender sets the targeting against Azerbaijan's larger role in European gas supply, now reaching 13 European countries, but states that this context does not establish motive ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). The Hacker News notes that FamousSparrow is also tracked as UAT-9244 and overlaps with Earth Estries and Salt Typhoon ([The Hacker News, 2026-05-13](https://thehackernews.com/2026/05/azerbaijani-energy-firm-hit-by-repeated.html)).

**Initial access, three times.** On 2025-12-25 the Exchange IIS worker process `w3wp.exe`, with `MSExchangePowerShellAppPool` on its command line, tried to write a web shell into a publicly accessible directory, which Bitdefender reads as ProxyNotShell exploitation; more web-shell writes followed on 12-26 and 12-29, alongside attempts to execute commands through the same process ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). Bitdefender calls ProxyNotShell (CVE-2022-41040 and CVE-2022-41082) usable by unauthenticated attackers ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)), whereas Microsoft's advisory for CVE-2022-41082 says the attacker must be authenticated and scores both flaws with low privileges required, 8.8 and 8.0 ([MSRC, CVE-2022-41040](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41040); [MSRC, CVE-2022-41082](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082)). Microsoft released fixes on 2022-11-08 ([MSRC, CVE-2022-41082](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082)), and CISA has listed both as known exploited since 2022-09-30 ([CISA KEV catalog, 2022-09-30](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)). After remediation removed malware from at least one system, the attackers came back to the same still-vulnerable Exchange server about a month later, and again at the end of February ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)).

**Wave 1: Deed RAT behind a two-export sideload.** The legitimate LogMeIn Hamachi binary `LMIGuardianSvc.exe`, first run from `C:\TEMP`, sideloaded a malicious loader and was then installed under a path chosen to mimic the legitimate Hamachi install directory, with a service named LogMeIn Hamachi starting it at boot ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). The loader's `Init` export changes memory protection on `StartServiceCtrlDispatcherW` and patches its entry point; when the host later calls `ComMain` and its normal service start-up reaches that API, execution diverts into the loader, which restores the original bytes, decrypts the AES-128-CBC payload and runs shellcode that resolves APIs by hash, RC4-decrypts and LZNT1-decompresses the Deed RAT orchestrator ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)); a sandbox that runs the DLL on its own or invokes a single export sees the malware largely inactive ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). Deed RAT's configuration names system processes such as `SearchIndexer.exe` and `taskhost.exe` as injection targets and a registry key under the Hamachi name for configuration and plugin storage, and it talks HTTPS to domains impersonating security vendors ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). Bitdefender calls the technique an evolved DLL sideload and finds the loader closely matches one Trend Micro documented for Earth Estries, with the same exports and hook-and-restore flow ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)).

**Lateral movement.** From the first host the attackers opened an RDP session to a second server with a domain administrator account, launched PowerShell, and within minutes the Hamachi-based Deed RAT files appeared there; from that host atexec and smbexec-style utilities consistent with Impacket spread it to a third machine ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)).

**Wave 2: TernDoor, blocked.** About a month after the first wave, a renamed copy of the legitimate `deskband_injector64.exe` in a `ProgramData` subdirectory tried to sideload a malicious `winmm.dll`; the security product blocked execution before installation completed, and registry artefacts showed an attempt to create a kernel-driver service ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). From recovered memory pages Bitdefender identifies a Mofu loader chain and assesses the partially recovered payload as TernDoor ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)).

**Wave 3.** At the end of February the attackers deployed Deed RAT again through the same chain with a modified configuration, the components moved to `C:\Recovery` and new injection targets ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)).

**Exposure:** on-premises Exchange servers without Microsoft's 2022-11-08 ProxyNotShell fixes ([MSRC, CVE-2022-41082](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082)); Bitdefender warns that attackers will keep exploiting unpatched servers until they are patched or taken offline ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). HealthChecker's `-VulnerabilityReport` switch collects the vulnerability state of every Exchange server in an environment ([Microsoft CSS-Exchange, 2025-10-29](https://microsoft.github.io/CSS-Exchange/Diagnostics/HealthChecker/)).

**Detection:** in process and file telemetry on Exchange, `w3wp.exe` writing `.aspx` files to publicly accessible directories under `MSExchangePowerShellAppPool`; in memory and EDR telemetry, changes to the first bytes of commonly hooked APIs such as `StartServiceCtrlDispatcherW` by unsigned code; in service-creation events, a kernel-driver service (Type 1) whose image path is under `ProgramData`, `Temp` or another user-writable directory; in authentication logs, RDP from internal hosts with domain administrator credentials outside maintenance windows, followed by PowerShell and executable downloads; and Impacket atexec or smbexec use ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). The Wave 1 chain also leaves a LogMeIn Hamachi service and `LMIGuardianSvc.exe` on hosts with no sanctioned Hamachi install ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)).

**Triage:** legitimate Exchange maintenance rarely writes web-accessible script files through the IIS worker process, and legitimate applications rarely patch system API entry points, which signed system components or documented security tools do when they must ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)).

**Defender takeaway:** after removing malware from an Exchange-originated intrusion, the decision that ends it is patching the entry point and rotating every domain administrator credential used during the intrusion, since Bitdefender's lesson from this intrusion is that actors re-exploit the same access path until the vulnerability is patched and compromised credentials are rotated; where Exchange cannot be patched at once, segment it so a compromise does not grant domain-wide access ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)).

## Correction — 2026-10-21T20:26:12Z

Bitdefender presents Azerbaijan's expanded gas exports to 13 European countries as context that does not establish motive, and attributes the intrusion with moderate-to-high confidence to FamousSparrow as likely affiliated with the Chinese APT ecosystem ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)); no source states a motive of Chinese state actors. Prior reporting placed the cluster against telecoms, government and technology targets, and Bitdefender cites toolset and tradecraft overlap with Earth Estries rather than shared infrastructure ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). The sideload is what Bitdefender calls an evolved technique: its loader closely matches a Deed RAT loader Trend Micro documented for Earth Estries, and no source calls the Hamachi host new for the cluster or the binary signed ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)).

The second wave's TernDoor installation was blocked by the security product before it completed, and TernDoor is Bitdefender's assessment from recovered memory pages ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). The re-entries came through the same still-vulnerable Exchange server, and Bitdefender's lesson is patching plus rotation of compromised credentials; no surviving web shell or scheduled task is reported, no source describes cumulative updates rolling back fixes, and the persisted loader sat in a path mimicking the legitimate Hamachi install directory, so a hunt that trusts that path misses it ([Bitdefender, 2026-05-13](https://www.bitdefender.com/en-us/blog/businessinsights/famoussparrow-apt-targets-azerbaijani-oil-gas-industry)). Microsoft's advisory says ProxyNotShell requires an authenticated attacker ([MSRC, CVE-2022-41082](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2022-41082)), while Bitdefender describes it as unauthenticated.
