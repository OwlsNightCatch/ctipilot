---
schema: 1
kind: research
title: "Oneconsult on the File System Access API: after two clicks a website holds read and write access to folders such as .vscode, .Azure, the public desktop and SMB shares in Chrome and Edge, enough for token theft and persistence without a process on the host"
headline: "Oneconsult: a site granted a folder in Chrome or Edge can steal tokens and plant VS Code and PowerShell persistence"
summary: >
  Oneconsult's analysis of Chromium's Windows blocklist shows that a website granted a folder through the File System Access API after two clicks keeps a handle for as long as the tab is open, and that the blocklist leaves .vscode, .Azure, C:\Users\Public, SMB shares and, after a OneDrive Known Folder Move, the Desktop reachable. The paths it demonstrates are token and .env theft, a fake VS Code extension and PowerShell profile or module backdoors that need the Bypass or Unrestricted execution policy, and a file proxy through the open tab that EDR sees only as browser file activity.
discovered_at: "2026-11-07T04:01:00Z"
updated_at: null
event_date: "2026-11-02"
run_id: 2026-11-07T0256Z-intel
priority: notable
immediate_action: null
tags: [phishing, cloud]
regions: [global]
sectors: []
entities: ["product:microsoft-onedrive"]
techniques: [T1204.001, T1176.002, T1546.013, T1005, T1080, T1552.001]
affected_products: ["Google Chrome", "Microsoft Edge", "Microsoft OneDrive"]
cves: []
sources:
  - url: "https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/"
    publisher: "Oneconsult"
    date: "2026-11-02"
    role: primary
  - url: "https://danieloz147.github.io/2026/07/05/rogue-sandbox-when-the-scan-is-the-payload/"
    publisher: "Daniel Oz (danieloz147)"
    date: "2026-07-05"
    role: corroborating
closed_sources: []
evidence:
  - quote: "after just two user clicks (selecting the folder and granting permission) on the website, a handle to the files is obtained"
    publisher: "Oneconsult"
    source_url: "https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/"
  - quote: "A MotW (Mark of the Web) has no effect on the execution, since Node.js simply does not check the Zone.Identifier Alternate Data Stream (ADS)."
    publisher: "Oneconsult"
    source_url: "https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/"
  - quote: "EDR solutions only detect that Chrome is reading and writing files"
    publisher: "Oneconsult"
    source_url: "https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/"
verification: multi-source
sourcing_note: >
  Oneconsult's results come from its own tests in July 2026 on Windows 11 with Chrome and Edge 150.0.7871.101 and from the public Chromium source; other systems and browser configurations are not covered. Oz's July write-up of the same technique gives no versions, and the two disagree on whether an edit by a site marks an existing file with Mark of the Web.
confidence: medium
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

Oneconsult analyses, from the Chromium source and tests on Windows 11 with Chrome and Edge 150.0.7871.101, what a website can reach through the File System Access API once a user selects a folder and grants permission: the handle stays valid as long as the tab is open and is obtained after just two user clicks ([Oneconsult, 2026-11-02](https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/)). Chrome rejects blocklisted paths, but a path that is not in its table and not an ancestor of a blocked path is allowed, and the kDontBlockChildren rule leaves the subfolders of listed directories selectable; Oneconsult confirmed .vscode, the Azure token cache, C:\Users\Public and SMB shares as accessible ([Oneconsult, 2026-11-02](https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/)).

Oneconsult demonstrates these paths. A site can search a granted folder and take files such as cached Azure tokens and .env files. It can drop a fake VS Code extension into .vscode/extensions, which runs inside the normal code.exe process and is unaffected by Mark of the Web because Node.js does not check the Zone.Identifier stream. It can plant PowerShell profile and module backdoors, which work only with the Bypass or Unrestricted execution policy because the API stamps every written file with ZoneId=3 and RemoteSigned refuses such files. It can drop files on the public desktop, where they appear for all users and trigger a warning that a certain percentage of users acknowledge. And it can run an interactive file proxy through the still-open tab, where EDR sees only the browser reading and writing files ([Oneconsult, 2026-11-02](https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/)). A OneDrive Known Folder Move enabled while Chrome is running leaves a stale blocklist, so the redirected Desktop was writable; Oneconsult notes that the bypass has been reported to Google, which made the issue public, and that Google classed reading a single dragged file from a blocked folder as "not a security issue" ([Oneconsult, 2026-11-02](https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/)).

Daniel Oz's July write-up of the same technique has a website edit a file the user already holds. He says the user-gesture requirement does not prevent phishing, only automatic picker invocation, and that signed or complex files may fail, be blocked or break in a way that prevents execution ([Oz, 2026-07-05](https://danieloz147.github.io/2026/07/05/rogue-sandbox-when-the-scan-is-the-payload/)).

**Exposure:** Windows users of Chrome or Edge, above all developer workstations with VS Code, cached Azure tokens or PowerShell on the Bypass or Unrestricted execution policy, and estates that enable OneDrive Known Folder Move; the attack needs a user to choose a folder and confirm a second prompt ([Oneconsult, 2026-11-02](https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/)).

**Detection:** file-write telemetry for PowerShell profile paths, PowerShell module folders and .vscode\extensions, and changes to the Zone.Identifier stream there, whose ReferrerUrl and HostUrl fields keep the origin of the page that wrote the file ([Oneconsult, 2026-11-02](https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/)). Oz says editing a file does not automatically reclassify it as downloaded, so the stream is a possible marker, not a guaranteed one ([Oz, 2026-07-05](https://danieloz147.github.io/2026/07/05/rogue-sandbox-when-the-scan-is-the-payload/)).

**Triage:** browsers legitimately read and write files for web editors such as Google Docs and VS Code for Web, as Oneconsult notes; the signal is a browser process writing into a persistence location, not the file activity itself.

**Defender takeaway:** restrict file system read and write access with the Chrome Enterprise policies Oneconsult names, FileSystemReadAskForUrls, FileSystemWriteAskForUrls and the respective AskForUrls policies, alert on writes to PowerShell profiles and VS Code extension folders, and treat a website's request to choose a local folder as a social-engineering step ([Oneconsult, 2026-11-02](https://www.oneconsult.com/en/blog/attack-simulation-red-teaming/fsa-api-possible-attacks-using-the-file-system-access-api/)).
