---
schema: 1
kind: incident
title: "SoftwareOK: Q-Dir 12.83 to 12.85 and DesktopOK 12.82 and 12.85 installers from the vendor's official site carried a Python remote-access tool, ASEC says the update function may have been affected too, and reinstalling may not remove it"
headline: "SoftwareOK Q-Dir and DesktopOK installers carried a Python RAT; check hashes, reinstalling may not remove it"
summary: >
  AhnLab ASEC reports that Q-Dir 12.83.0.0 to 12.85.0.0 and DesktopOK 12.82.0.0 and 12.85.0.0 installers
  distributed from SoftwareOK's official site were tampered with and install a Python remote-access tool that
  compares running processes with 1,206 security-product names. ASEC says copies updated through the update
  function may be affected, has not found how the files were replaced, and the vendor's pages carry no notice
  as of 2026-11-27.
discovered_at: "2026-11-27T04:41:00Z"
updated_at: null
event_date: "2026-11-25"
run_id: 2026-11-27T0355Z-intel
priority: notable
immediate_action: null
tags: [supply-chain]
regions: [global]
sectors: []
entities: ["incident:softwareok-q-dir-desktopok-tampered-installers-2026-11"]
techniques: [T1195.002, T1204.002, T1036.005, T1105, T1059.006, T1053.005, T1518.001, T1113, T1082, T1041]
affected_products: ["SoftwareOK Q-Dir", "SoftwareOK DesktopOK"]
cves: []
sources:
  - url: "https://asec.ahnlab.com/en/96827/"
    publisher: "AhnLab ASEC"
    date: "2026-11-25"
    role: primary
  - url: "https://www.softwareok.com/?seite=Freeware/Q-Dir/History"
    publisher: "SoftwareOK"
    date: "2026-11-21"
    role: corroborating
  - url: "https://www.softwareok.com/?seite=Freeware/DesktopOK/History"
    publisher: "SoftwareOK"
    date: "2026-11-26"
    role: corroborating
  - url: "https://www.softwareok.com/?Download=Q-Dir"
    publisher: "SoftwareOK"
    date: "2026-11-27"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Evidence indicates that malicious files were generated not only when users downloaded the programs directly from the official download page but also during the update process of previously installed legitimate programs."
    publisher: "AhnLab ASEC"
    source_url: "https://asec.ahnlab.com/en/96827/"
  - quote: "However, simply uninstalling and reinstalling the program may not remove a Python RAT that has already been installed."
    publisher: "AhnLab ASEC"
    source_url: "https://asec.ahnlab.com/en/96827/"
verification: single-source
sourcing_note: "ASEC is the only analyst and the only source for the tampering, the behaviour and the versions; the malware.news copy of the post is an automated relay of it. SoftwareOK's pages are cited only for release dates and for the absence of a notice."
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
  - "Inventory every Windows endpoint that installed or updated Q-Dir or DesktopOK since 2026-10-28, compare each installer's SHA-256 with the value on SoftwareOK's download page, and isolate any host with a bundled Python interpreter under ProgramData or a scheduled task that runs one, treating its credentials as stolen, because ASEC says simply uninstalling and reinstalling the program may not remove a Python RAT already installed."
updates: []
migrated_from: null
---

AhnLab's ASEC reports that Q-Dir 12.83.0.0, 12.84.0.0 and 12.85.0.0 and DesktopOK 12.82.0.0 and 12.85.0.0 were replaced with tampered installers on SoftwareOK's official distribution path, and that the SHA-256 of some files downloaded from the official site did not match the value posted on its download page. ASEC says the evidence indicates malicious files were also generated during the update process of installed copies, a point it later hedges (users of the update function "may have been affected"), and that it has not identified how the files were replaced ([ASEC, 2026-11-25](https://asec.ahnlab.com/en/96827/)).

The tampered installer embeds the genuine, correctly signed Q-Dir or DesktopOK executable and runs it from the public user folder so the program appears to work. It then downloads the legitimate 7-Zip console extractor and a package holding a Python runtime and a remote-access tool, unpacks it under a Microsoft-looking folder in ProgramData and persists through a scheduled task, named to look like Edge, that runs the windowless Python interpreter. The tool runs shell commands and Python code, transfers files, takes screenshots and collects system information, and it compares running processes with a list of 1,206 security-product process names and sends the matches to its server. ASEC does not describe the server protocol, names no malware family or actor, and reads Chinese-language comments in the code only as a hint ([ASEC, 2026-11-25](https://asec.ahnlab.com/en/96827/)).

ASEC gives no distribution window. SoftwareOK's release pages date Q-Dir 12.83 to 4 November, 12.84 to 13 November and 12.85 to 21 November ([SoftwareOK, 2026-11-21](https://www.softwareok.com/?seite=Freeware/Q-Dir/History)) and DesktopOK 12.82 to 28 October and 12.85 to 19 November ([SoftwareOK, 2026-11-26](https://www.softwareok.com/?seite=Freeware/DesktopOK/History)), which bounds only when the listed versions could first have reached users, and its Q-Dir download page carries no notice about tampering as of 2026-11-27 ([SoftwareOK, 2026-11-27](https://www.softwareok.com/?Download=Q-Dir)).

**Exposure:** any Windows endpoint on which the listed versions were installed or updated since 2026-10-28; ASEC adds that other versions installed or updated while the tampered files were distributed may be affected. The installed program is the genuine signed one, so a signature check on it passes; the check that finds the tampering is the installer's SHA-256 against the vendor page.

**Detection:** software-inventory telemetry for the listed versions; in scheduled-task creation and process-creation telemetry, a task running a bundled Python interpreter from under ProgramData and an extractor tool started by an installer; and egress from that interpreter. After removal ASEC says to look for the Python environment, scheduled tasks, related files and external connections.

**Defender takeaway:** treat every host that ran an affected installer or updater as compromised: isolate it, remove the tool and rotate the credentials used on it, because ASEC says uninstalling and reinstalling the utility may not remove the remote-access tool.
