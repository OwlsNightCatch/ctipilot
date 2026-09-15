---
schema: 1
kind: vulnerability
title: >
  ShieldBreak — a public proof-of-concept defeats Microsoft's July fix for the RoguePlanet
  Defender flaw, claims 100% reliability where the original was a coin flip, and now covers
  Windows Server 2025
headline: >
  Microsoft has now shipped an engine fix (1.1.26080.3) — and the same researcher claims a
  partial bypass of it
summary: >
  Researcher Nightmare Eclipse published ShieldBreak on 2026-08-11/12, a proof-of-concept the
  researcher describes as a full bypass of the patch Microsoft shipped in July for RoguePlanet
  (CVE-2026-50656), the Microsoft Malware Protection Engine privilege-escalation flaw that yields
  a SYSTEM shell on fully updated Windows. Two properties make it worse than what it replaces: it
  is listed with a 100 percent success rate where RoguePlanet was an unreliable race, and it is
  listed as tested on Windows Server 2025 alongside Windows 11 25H2, where the June exploit did
  not run. Microsoft acknowledged it as CVE-2026-69414 and has since shipped a fix: Malware
  Protection Engine 1.1.26080.3 addresses it, with 1.26070.7 the last affected engine. On
  2026-09-08 the same researcher published ShieldCrash, claiming that fix is incomplete under
  specific conditions; Microsoft has not confirmed that claim.
discovered_at: "2026-08-12T04:47:00Z"
updated_at: "2026-09-13T15:10:00Z"
event_date: 2026-08-12
run_id: 2026-08-12T0411Z-intel
priority: high
immediate_action: null
tags:
  - vulnerabilities
  - priv-esc
  - lpe
  - poc-public
  - patch-available
  - zero-day
  - identity
regions:
  - global
  - europe
  - switzerland
sectors:
  - public-sector
  - energy
  - healthcare
  - finance
  - telco
  - technology
  - water
  - transport
entities:
  - "actor:nightmare-eclipse"
  - "trend:shieldbreak-defender-rogueplanet-patch-bypass-2026-08"
  - "trend:nightmare-eclipse-rogueplanet-defender-toctou-lpe-2026-06"
techniques:
  - T1068
  - T1548
  - T1036.005
  - T1574.001
  - T1218
  - T1053.005
  - T1685
  - T1106
  - T1070.004
  - T1027.007
affected_products:
  - Microsoft Defender Antivirus
  - Microsoft Windows 11
  - Microsoft Windows Server 2025
  - Microsoft Defender
  - Microsoft Malware Protection Engine
  - Microsoft Windows Defender
cves:
  - id: CVE-2026-50656
    cvss: "7.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: >
      Microsoft Malware Protection Engine builds before 1.1.26060.3008 (RoguePlanet, the flaw
      ShieldBreak is described as bypassing)
    fixed: "Engine build 1.1.26060.3008, shipped 2026-07-09 — reported as bypassed by ShieldBreak"
  - id: CVE-2026-69414
    cvss: "7.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status:
      - patch-available
      - poc-public
    affected: >
      Windows 11 24H2 and Windows Server 2025 with Windows Defender in its default configuration,
      fully patched as of the August 2026 updates
    fixed: Microsoft Malware Protection Engine 1.1.26080.3 (last affected engine 1.26070.7)
sources:
  - url: "https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html"
    publisher: Cyber Kendra
    date: 2026-08-12
    role: primary
  - url: "https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026/"
    publisher: Rapid7
    date: 2026-08-11
    role: corroborating
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414"
    publisher: Microsoft Security Response Center
    date: 2026-08-14
    role: primary
  - url: "https://security-hub.ncsc.admin.ch/#/posts/12622"
    publisher: NCSC Switzerland (BACS) — Cyber Security Hub
    date: 2026-08-17
    role: corroborating
  - url: "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1035/"
    publisher: CERT-FR / ANSSI
    date: 2026-08-17
    role: corroborating
  - url: "https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking"
    publisher: LevelBlue SpiderLabs
    date: 2026-08-19
    role: primary
  - url: "https://socradar.io/blog/shieldcrash-poc-microsoft-defender-fix-bypass/"
    publisher: "SOCRadar"
    date: "2026-09-10"
    role: corroborating
closed_sources: []
evidence:
  - quote: "First version of the Microsoft Malware Protection Engine with this vulnerability addressed"
    publisher: Microsoft Security Response Center
    source_url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414"
  - quote: "ShieldCrash does not currently have a separate CVE. Nightmare Eclipse describes the public release as a skeleton PoC that demonstrates privileged file reads. It does not establish arbitrary file writes or SYSTEM-level code execution."
    publisher: "SOCRadar"
    source_url: "https://socradar.io/blog/shieldcrash-poc-microsoft-defender-fix-bypass/"
  - quote: ShieldBreak is listed with a 100 percent success rate.
    publisher: Cyber Kendra
  - quote: "No patch exists for ShieldBreak, and no vendor has reproduced it publicly yet."
    publisher: Cyber Kendra
  - quote: We are working to provide a high quality security update that addresses this vulnerability.
    publisher: Microsoft Security Response Center
  - quote: ShieldBreak is tracked as CVE-2026-69414 by Microsoft
    publisher: NCSC Switzerland (BACS) — Cyber Security Hub
  - quote: "The LevelBlue OpsCTI and THOR teams reviewed and reproduced the complete ShieldBreak exploitation chain with the August 2026 Patch Tuesday updates installed, confirming the PoC functions as described."
    publisher: LevelBlue SpiderLabs
  - quote: ShieldBreak is best detected through behavioral correlation rather than any single static indicator.
    publisher: LevelBlue SpiderLabs
  - quote: ShieldBreak is fully self-contained and runs to full SYSTEM completion from a standard user account on any fully patched Windows 11 24H2 or Windows Server 2025 system with Windows Defender in its default configuration.
    publisher: LevelBlue SpiderLabs
  - quote: "The set of expected MpClient.dll consumers is small. A load by an unrelated process becomes especially significant when followed by runtime resolution of MpManagerOpen, MpScanStart, MpCleanOpen, MpCleanStart, or MpCleanControl."
    publisher: LevelBlue SpiderLabs
verification: multi-source
sourcing_note: >
  Both sources report the researcher's own claims about ShieldBreak rather than independent
  reproduction — Cyber Kendra states explicitly that no vendor has reproduced it publicly, and
  Rapid7 reports the release as part of its Patch Tuesday round-up. The reliability rating
  reflects Rapid7 as the higher-reliability of the two; the credibility number reflects that the
  technical claims (100% success rate, Server 2025 coverage) trace to the researcher and are so
  far uncorroborated by any vendor or independent analysis.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Confirm every Windows endpoint reports Microsoft Malware Protection Engine 1.1.26080.3 or later — the engine version updates on its own cadence and is not covered by the OS patch level, so check it separately; 1.26070.7 is the last affected build."
  - "Hunt for C:\\Windows\\System32\\phoneinfo.dll across the Windows estate now — LevelBlue states the file is not expected to exist natively on supported Windows versions, so an instance on a supported build is either this chain or an unrelated planted DLL, and either warrants investigation."
updates:
  - at: "2026-08-18T04:45:00Z"
    run_id: 2026-08-18T0410Z-intel
    type: update
    summary: >
      The ShieldBreak proof-of-concept covered here on 2026-08-12, which claims a fully reliable
      bypass of Microsoft's July fix for the RoguePlanet Defender privilege-escalation flaw and had
      drawn no vendor comment at the time, is now tracked as CVE-2026-69414. Microsoft's advisory
      names ShieldBreak explicitly, rates the flaw Important at CVSS 3.1 base 7.8, records it as
      publicly disclosed but not exploited, sets its exploitability assessment to "Exploitation More
      Likely", and states that a security update is still being worked on. Switzerland's NCSC and
      France's CERT-FR both relayed the identifier to their constituencies on 2026-08-17, which is
      what puts a tracking number on an unpatched weakness in a baseline endpoint control across this
      constituency's estate.
    fields:
      - affected_products
      - cves
      - evidence
      - regions
      - sectors
      - sources
      - body
    merged_from: 2026-08-18/cve-2026-69414-shieldbreak-defender-acknowledged-no-fix
  - at: "2026-08-21T06:20:00Z"
    run_id: 2026-08-21T0410Z-intel
    type: update
    summary: >
      LevelBlue SpiderLabs reproduced the complete ShieldBreak chain on Windows 11 24H2 and Windows
      Server 2025 with the August 2026 Patch Tuesday updates already installed, reaching SYSTEM from a
      standard user account against Windows Defender in its default configuration in roughly eight to
      twelve seconds. The published mechanism is the delta: a fake Cloud Files sync provider serves
      benign bait on first read and the malicious DLL on a later read, a shadow NT Object Manager
      namespace supplies two conflicting symbolic links, and Defender's own management library is
      called directly so that its remediation engine — not the attacker — writes the payload into
      System32, where a Windows Error Reporting scheduled task loads it as SYSTEM. Microsoft's record
      still says no fix is available; its only revision on the day of the report was an informational
      CWE addition.
    fields:
      - affected_products
      - cves
      - evidence
      - sources
      - techniques
      - body
    merged_from: 2026-08-21/shieldbreak-cve-2026-69414-reproduced-on-august-patch-level
  - at: "2026-08-24T09:11:00Z"
    run_id: 2026-08-24T0410Z-intel
    type: update
    summary: >
      LevelBlue SpiderLabs published the working mechanism of the unpatched Windows Defender
      privilege-escalation chain this pipeline has tracked as ShieldBreak: a fake Cloud Files sync
      root, two conflicting object-manager symbolic links both named WD_SCAN, an exclusive lock on the
      CLFS transaction log that freezes Defender's clean operation mid-flight, and a symlink swap that
      redirects the in-flight write so Defender's own remediation engine places an attacker-supplied
      phoneinfo.dll into System32 — after which a crafted Windows Error Report triggers the built-in
      QueueReporting task and wermgr.exe loads that DLL as SYSTEM. Roughly eight to twelve seconds,
      standard user to SYSTEM, on fully patched Windows 11 24H2 and Windows Server 2025 with Defender
      in its default configuration. There is still no vendor fix, so detection is the whole available
      control — and the mechanism supplies it, led by the presence of
      C:\Windows\System32\phoneinfo.dll, which LevelBlue states is not expected to exist natively on
      supported Windows versions.
    fields:
      - actions
      - cves
      - evidence
      - tags
      - techniques
      - body
    merged_from: 2026-08-24/shieldbreak-defender-remediation-mechanism-hunting-package
  - at: "2026-09-13T15:10:00Z"
    run_id: 2026-09-13T1307Z-audit
    type: update
    summary: >
      Microsoft has shipped a fix. Its own record for CVE-2026-69414 names Malware Protection
      Engine 1.1.26080.3 as the first version with the vulnerability addressed and 1.26070.7 as the
      last affected, so this entry's standing "no fix available" statement is superseded and the
      frontmatter, headline, summary and action item move with it. Separately, on 2026-09-08 the
      same researcher published ShieldCrash, claiming the fix is incomplete under specific
      conditions; that claim is the researcher's own, relayed by SOCRadar, carries no new CVE, and
      Microsoft has not confirmed it. Surfaced by this audit's coverage re-sweep.
    fields:
      - headline
      - summary
      - tags
      - cves
      - actions
      - sources
      - evidence
      - body
migrated_from: null
---

The pseudonymous researcher Nightmare Eclipse published ShieldBreak, a proof-of-concept described as defeating the patch Microsoft shipped five weeks earlier for a Windows Defender privilege-escalation flaw ([Cyber Kendra, 2026-08-12](https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)). Rapid7 places the drop late on Patch Tuesday itself, continuing what it describes as a pattern of the past few months ([Rapid7, 2026-08-11](https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026/)). Rapid7, covering the same release in its Patch Tuesday analysis, records the researcher describing ShieldBreak as a full patch bypass for RoguePlanet — the entry in the same series that Microsoft patched as CVE-2026-50656 in July, a month after its public disclosure — and notes that both are elevation-of-privilege-to-SYSTEM vulnerabilities in Defender ([Rapid7, 2026-08-11](https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026/)).

Two claims are what make this worth acting on rather than filing. RoguePlanet was a race condition whose reliability varied sharply between machines — the researcher called it hit or miss in June — while "ShieldBreak is listed with a 100 percent success rate". And where the June exploit did not run on Windows Server because standard users cannot mount ISO images there, ShieldBreak is listed as tested on Windows Server 2025 alongside Windows 11 25H2 and the Canary channel ([Cyber Kendra, 2026-08-12](https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)). Both of those are the researcher's own claims: Cyber Kendra states that "No patch exists for ShieldBreak, and no vendor has reproduced it publicly yet", and that Microsoft had not commented at publication — both true when written on 2026-08-12 and both since overtaken: Microsoft acknowledged the flaw as CVE-2026-69414 two days later and has since shipped an engine fix (2026-09-13 update below). Treat the reliability figure and the server coverage as unverified until someone reproduces them — but treat the existence of working exploit code as established, because that is what the release consists of.

The target is the Microsoft Malware Protection Engine, the scanner behind Defender, which runs as SYSTEM; RoguePlanet abused improper link resolution before file access to spawn a SYSTEM shell on fully updated machines, was rated Important at CVSS 7.8, and was fixed in engine build 1.1.26060.3008 on 2026-07-09. Analysts who dissected RoguePlanet in June described an attack chain built on NTFS junctions, opportunistic locks and the Windows Error Reporting `QueueReporting` scheduled task, which Cyber Kendra reads as suggesting ShieldBreak reworks the same plumbing rather than opening a new front ([Cyber Kendra, 2026-08-12](https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)) — that is an inference in the reporting, not a stated finding, and no technical analysis of ShieldBreak itself has been published.

The reason a local privilege-escalation PoC from this particular persona deserves more than a backlog ticket is the track record the same reporting sets out: of the previously disclosed flaws in the series, three — BlueHammer (CVE-2026-33825), RedSun (CVE-2026-41091) and UnDefend (CVE-2026-45498) — were exploited in real-world intrusions before fixes landed and all three ended up in CISA's Known Exploited Vulnerabilities catalog ([Cyber Kendra, 2026-08-12](https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)). This is also the second time a fix in this class has fallen: Microsoft hardened Defender's internal file-handling APIs in mid-May and RoguePlanet was rewritten to defeat that.

**This paragraph describes the position at disclosure, when no fix existed; Microsoft has since shipped one — see the 2026-09-13 update below, and patch first.** At the time, compensating controls rather than patching were the available lever. The one the reporting names as strongest for this bug class is application allowlisting — ThreatLocker found it blocked RoguePlanet by default ([Cyber Kendra, 2026-08-12](https://www.cyberkendra.com/2026/08/shieldbreak-poc-bypasses-microsofts.html)). Detection concepts follow the RoguePlanet chain rather than ShieldBreak's unpublished internals, so they are hypotheses to hunt with rather than confirmed signatures for this variant: in filesystem and process telemetry, reparse-point or junction creation by a standard-user process inside a path the Defender engine subsequently touches, and unexpected execution lineage from the Windows Error Reporting scheduled task, are the observable steps that chain described. Because the escalation ends in a SYSTEM process spawned by an engine that legitimately runs as SYSTEM all day, the parent-process shape alone will not separate this from routine scanning activity — the preceding filesystem manipulation by an unprivileged account is where the discriminator lives.

## Update — 2026-08-18T04:45:00Z

The original entry recorded that no patch existed, no vendor had publicly reproduced the ShieldBreak proof-of-concept, and Microsoft had not commented. Two of those three have changed. Microsoft published an advisory on 2026-08-14 that names the technique directly — the vulnerability is described as an elevation of privilege in the Microsoft Malware Protection Engine in Microsoft Defender publicly referred to as "ShieldBreak" — and assigned it CVE-2026-69414 ([Microsoft, 2026-08-14](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)). The third has not: on the fix, Microsoft states only that "We are working to provide a high quality security update that addresses this vulnerability."

The vendor's own calibration is the useful part of the delta. Microsoft rates the flaw Important with a CVSS 3.1 base score of 7.8 for a local, low-privilege, no-interaction elevation, records it as publicly disclosed, records exploitation as not detected, and sets its exploitability assessment to "Exploitation More Likely" ([Microsoft, 2026-08-14](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)). That combination — publicly available exploit code, a vendor expectation of exploitation, and no update — is the shape that justifies attention outside the normal patch cycle, and it is a materially different footing from a researcher's unverified GitHub claim.

The relay is what brought it into this constituency's field of view. Switzerland's NCSC amended its rolling Nightmare Eclipse advisory on 2026-08-17 to record that "ShieldBreak is tracked as CVE-2026-69414 by Microsoft" ([NCSC-CH, 2026-08-17](https://security-hub.ncsc.admin.ch/#/posts/12622)), and CERT-FR issued advisory CERTFR-2026-AVI-1035 the same day, listing the Microsoft Malware Protection Engine among affected systems alongside an unrelated, already-patched PowerShell flaw ([CERT-FR, 2026-08-17](https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-1035/)). CERT-FR's bulletin carries its standard instruction to consult the vendor advisory for fixes; for this CVE that advisory has none to offer, which is worth knowing before an operator treats the bulletin as a patchable item.

**Detection, telemetry class first.** No new behavioural detail was published with the CVE, so nothing here supersedes what the original entry carried. The durable anchor remains process-creation telemetry with parent lineage: the Malware Protection Engine has no legitimate reason to be the parent of an interactive shell or an unexpected child process, so any such process tree rooted at the engine is the signal irrespective of which variant produced it. **Triage:** the engine's own remediation work — quarantine, deletion, signature updates — runs inside the service rather than by launching command interpreters, so a shell parented to it does not have a benign counterpart; the discriminator is the parent-child relationship itself, not the child's command line.

**Defender takeaway:** the actionable change is administrative rather than technical. An estate now has an identifier to track this against, which means it can be carried in a vulnerability register, matched by a scanner once detection logic exists, and closed out when the update ships — none of which was possible against an unnumbered proof-of-concept. Nothing to patch yet, and no reason to raise urgency beyond that: exploitation is not observed, the prerequisite is code already running as a local user, and the compensating control named in the earlier coverage is unchanged. Watch the CVE record for the update Microsoft says is coming.

## Update — 2026-08-21T06:20:00Z

This pipeline recorded CVE-2026-69414 three days ago as acknowledged by Microsoft, rated 7.8, publicly disclosed, assessed "Exploitation More Likely", with a security update still being worked on. Two things have changed and neither is a fix.

**It works on the current patch level, and that is now independently established.** "The LevelBlue OpsCTI and THOR teams reviewed and reproduced the complete ShieldBreak exploitation chain with the August 2026 Patch Tuesday updates installed, confirming the PoC functions as described" ([LevelBlue SpiderLabs, 2026-08-19](https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking)). LevelBlue reports the chain running to SYSTEM from a standard user account on Windows 11 24H2 and Windows Server 2025 with Defender in its default configuration, self-contained and needing no arguments, completing in roughly eight to twelve seconds on an idle system. Queried directly, Microsoft's own record for the CVE shows its most recent revision dated the same day as that report, and the change it describes is the addition of a CWE classification, informational only ([MSRC, 2026-08-19](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414)) — exploitation still recorded as no, the exploitability assessment unchanged, and the temporal metrics still recording proof-of-concept code available with no official fix.

**The mechanism, which is the substance of the delta.** The prior entry had the identifier and Microsoft's rating but not how the chain works. LevelBlue reconstructs it in seven stages, and the elegant part is that the attacker never writes to System32 — Defender does.

The exploit first raises its own process and thread priority to improve its odds in a later race, then registers a **fake Cloud Files sync provider** rooted at a working directory it creates, and creates a placeholder file so Windows treats it as a cloud-resident object not yet downloaded. Its hydration callback is two-faced by design: the **first** read returns a benign archive, which is what Defender detects; a **later** read returns the malicious DLL, which is what ends up on disk. Next it resolves native object-manager routines out of `ntdll.dll` and builds a shadow namespace containing two conflicting symbolic links under the same name — one pointing at the working directory, one at a transaction-log path — giving it a redirection layer that sits above the filesystem. It then loads Defender's own management library directly and resolves that library's scan and clean functions to open Defender's RPC interface, scan the placeholder through the shadow path, and — once Defender has flagged the bait archive — start Defender's **own remediation operation** against it. A time-of-check-to-time-of-use race, held open with an exclusive lock on a transaction-log file while the symbolic link is swapped underneath, redirects that remediation so Defender's clean engine writes the attacker's DLL into System32. Execution as SYSTEM then comes from a Windows Error Reporting scheduled task loading that DLL through the error-reporting host process.

LevelBlue also places the disclosing persona in a lineage of prior proof-of-concept releases and notes a functional improvement over the immediately preceding one: where the earlier LegacyHive technique needed a helper-account logon to trigger its final stage, ShieldBreak is fully self-contained.

**Triage:** LevelBlue's own framing is the right instruction — "ShieldBreak is best detected through behavioral correlation rather than any single static indicator", because every component is a legitimate Windows capability. The highest-value single signal is a module load: Defender's management library being loaded by a process outside the small, stable set of Defender's own binaries, especially when that same process then resolves Defender's scan and clean entry points at runtime. Around it, two more composites: an unapproved process registering a cloud sync root and creating a placeholder, then immediately moving into object-manager and Defender API activity; and a standard-user process taking an exclusive lock on a transaction-log file. Each is weak alone — legitimate sync agents register sync roots, and Defender's own processes load its library all day — so the sequence and the identity of the calling process are what separate them. The final stage is the most conventional: a DLL appearing in System32 followed by the error-reporting scheduled task being run on demand, with the payload cleaned up afterwards.

**Defender takeaway:** there is still nothing to patch, so the change for a defender is that detection content is now writable against a documented chain — and that content should key on the Defender-library load by an unexpected process, not on the exploit's filenames, which are proof-of-concept artefacts. The wider pattern is worth naming: this abuses Defender's *remediation* machinery rather than a memory-safety bug, making the product's own privileged clean-up path the write primitive. That argues for treating the endpoint-protection stack's own privileged components as an attack surface to monitor in their own right, rather than purely as a control to rely on.

## Update — 2026-08-24T09:11:00Z

The entry this one updates recorded that Microsoft had acknowledged ShieldBreak as CVE-2026-69414, rated it 7.8, assessed it "Exploitation More Likely", and stated a security update was still being worked on — with no published mechanism and therefore nothing to detect on. LevelBlue SpiderLabs has now published the mechanism and, with it, a hunting package ([LevelBlue SpiderLabs, 2026-08-19](https://www.levelblue.com/blogs/spiderlabs-blog/cloud-sync-root-registrationshieldbreak-hunting-windows-defender-remediation-abuse-and-cloud-files-hijacking)). That is the whole delta, and at the time it mattered because no fix existed: detection was then the only control a defender had. (Microsoft has since shipped an engine fix — see the 2026-09-13 update below.)

The chain turns Windows Defender's own remediation path into the write primitive. The proof-of-concept registers its working directory as a **Cloud Files sync root**, self-identifying as a sync provider with a hardcoded provider GUID and creating a placeholder file. It then creates two directories beneath the object manager's `\BaseNamedObjects\Restricted\` namespace and, inside them, **two conflicting symbolic links both named `WD_SCAN`** — one initially resolving to the working directory holding the placeholder, the other to a path used by the Common Log File System. It opens Defender's interface directly, resolving the management, scanning and clean functions out of `MpClient.dll` at runtime, and asks Defender to scan the placeholder through a `\\.\globalroot\...\WD_SCAN\` path. A background thread watches for the CLFS transaction log that Defender's clean operation creates, and the instant it appears takes an **exclusive lock** on it — freezing Defender mid-transaction. With the operation held open, the proof-of-concept deletes the shadow `WD_SCAN` link and recreates it pointing at `\??\UNC\127.0.0.1\C$\Windows\System32\phoneinfo.dll`, so the already-in-flight path resolves somewhere new without any NTFS junction being involved; it then restarts Cloud Files hydration with the file size set to the DLL's rather than the original's, so the hydration callback supplies the attacker's bytes while Defender's clean engine performs the write. Because `MsMpEng.exe` is the process that writes the file, the write itself looks expected — which LevelBlue flags as a triage detail that must be correlated rather than dismissed. The proof-of-concept then maps the resulting DLL as an executable image to stop remediation removing it, crafts a Windows Error Report into the report queue, and triggers the **built-in `QueueReporting` scheduled task through the Task Scheduler COM interface method `ITaskService::Run()`**; that task runs as SYSTEM, so the signed Windows error-reporting binary `wermgr.exe` processes the report and loads `phoneinfo.dll` with SYSTEM privileges — a trusted system binary acting as the proxy that executes the attacker's code, which is how the payload runs without the attacker ever launching a process of their own. LevelBlue states the whole sequence takes approximately eight to twelve seconds on an unloaded system, and that it "is fully self-contained and runs to full SYSTEM completion from a standard user account on any fully patched Windows 11 24H2 or Windows Server 2025 system with Windows Defender in its default configuration."

Detection, in the report's own framing, "is best detected through behavioral correlation rather than any single static indicator" — but one static indicator is close to free. LevelBlue identifies **`C:\Windows\System32\phoneinfo.dll`** as the strongest single indicator in the chain and states the file **is not expected to exist natively on supported Windows versions** — so its creation warrants a high-priority look regardless of the process that wrote it. (The hedge is the source's own and is worth keeping: "not expected on supported versions" is what it will bear, not a guarantee about every Windows build ever shipped.) Beyond that, and led by telemetry class: in image- and module-load telemetry, `MpClient.dll` loaded by a process that is not one of Defender's own small set of expected consumers — the report names `MsMpEng.exe`, `MpCmdRun.exe`, `NisSrv.exe`, `ConfigSecurityPolicy.exe` and `MpSigStub.exe` — is the compound signal, and LevelBlue is specific about what makes it load-bearing: "The set of expected MpClient.dll consumers is small. A load by an unrelated process becomes especially significant when followed by runtime resolution of MpManagerOpen, MpScanStart, MpCleanOpen, MpCleanStart, or MpCleanControl." The same telemetry should surface `wermgr.exe` loading `phoneinfo.dll`. In scheduled-task audit records, the `QueueReporting` task being started programmatically through the Task Scheduler COM interface is the execution step. In registry or filter telemetry, a sync-root registration call issued by a process that is not a cloud-sync client is the setup step. And in named-pipe telemetry this specific proof-of-concept creates a pipe with a hardcoded name, with a SYSTEM-integrity process then connecting to a pipe a normal user created — though that name is an artefact of this build rather than of the technique.

**Triage:** every individual event here has a benign twin, which is why the sequence is the detection. `MsMpEng.exe` writing into System32 is normal remediation behaviour; a cloud-sync provider registering a sync root is normal on a machine running OneDrive or a similar client; `wermgr.exe` running as SYSTEM off a scheduled task is normal error reporting. The discriminators are the process identities and the ordering: a sync-root registration from something that is not a sync client, `MpClient.dll` resolved by a non-Defender process followed by that specific clean-function set, and a `QueueReporting` run driven through COM rather than by the ordinary error-reporting trigger — with the whole chain completing inside roughly ten seconds. Hardening was the awkward part while the flaw was unpatched: because the abused component is Defender itself in its default configuration, there was no configuration change to apply, and the vulnerable-driver blocklist and application-control policies have nothing third-party to key on. Microsoft has since shipped an engine fix, so updating the Defender engine is now the primary control — see the 2026-09-13 update below.

## Update — 2026-09-13T15:10:00Z

**Microsoft has shipped a fix, and this entry's standing "no fix available" status was stale.** Microsoft's own record for CVE-2026-69414 now carries a remediation boundary in its structured fields: "Last version of the Microsoft Malware Protection Engine affected by this vulnerability" reads 1.26070.7, and "First version of the Microsoft Malware Protection Engine with this vulnerability addressed" reads **1.1.26080.3** ([Microsoft MSRC](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-69414), latest revision 2026-09-03). The record's CVSS vector carries `RL:O` — an official fix — against the `E:P` proof-of-concept maturity it already had. The practical point for a defender is that **the Defender engine version updates on its own cadence and is not the same thing as the OS patch level**, so an estate that is fully current on Windows Update is not thereby on engine 1.1.26080.3; check the engine version explicitly. That replaces detection-as-the-only-control, which is what this entry has told readers since 2026-08-12.

**The same researcher now claims the fix is incomplete — as their own claim, not a confirmed one.** On 2026-09-08 Nightmare Eclipse published ShieldCrash, described in the researcher's own repository as a partial rather than total bypass: "Microsoft has failed to properly patch ShieldBreak CVE-2026-69414, under specific conditions it is still possible to trigger the exact same problem that was caused by ShieldBreak. While Microsoft fixed several things to prevent re-exploiting the issue, they missed a spot where ShieldBreak can still be exploited" ([Nightmare Eclipse, 2026-09-08](https://github.com/MSNightmare/ShieldCrash)). What is published is explicitly unfinished and narrower than the original: SOCRadar records that "ShieldCrash does not currently have a separate CVE. Nightmare Eclipse describes the public release as a skeleton PoC that demonstrates privileged file reads. It does not establish arbitrary file writes or SYSTEM-level code execution" ([SOCRadar, 2026-09-10](https://socradar.io/blog/shieldcrash-poc-microsoft-defender-fix-bypass/)), and that "Microsoft has not publicly confirmed the reported bypass" ([SOCRadar, 2026-09-10](https://socradar.io/blog/shieldcrash-poc-microsoft-defender-fix-bypass/)). Microsoft's record predates the ShieldCrash release by five days and acknowledges no bypass. SOCRadar also states there is no confirmed in-the-wild exploitation of ShieldCrash.

**Defender takeaway:** patch to engine 1.1.26080.3 or later and verify it as an engine version, not an OS build — that is now a real control where previously there was none. Do not retire the detection package in the 2026-08-24 update on the strength of the patch: the researcher who wrote the original working exploit says the fix leaves a reachable path, the claim is unrefuted as well as unconfirmed, and the hunting signals above key on the abuse of Defender's own remediation path rather than on any particular build. Arbitrary file read as SYSTEM is materially less severe than the original's full SYSTEM execution, so the residual risk after patching is lower than the pre-patch position, not equal to it.
