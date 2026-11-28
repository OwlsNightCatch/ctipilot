---
schema: 1
kind: threat
title: "ScreenConnect: Huntress finds 2,223 fake guest sessions named after crypto exchanges on 118 self-hosted servers, enrolled from 2026-11-03 and, in its leading hypothesis, bait for technicians whose clients predate 26.6.5; it saw no malicious use and no overlap with SCKit"
headline: "Huntress: 2,223 crypto-named fake sessions sit on 118 ScreenConnect servers, likely bait for unpatched technicians"
summary: >
  Huntress counted 2,223 unauthorized guest sessions on 118 self-hosted ScreenConnect servers at 109 MSP and organisation accounts, enrolled between 2026-11-03 and 2026-11-13 and named after crypto exchanges; on the 29 servers with complete history an operator revisited every 151 seconds to keep them online. Huntress's leading hypothesis, which it has not observed, is that they are bait for a technician with a client older than 26.6.5 to connect, so that CVE-2026-84869 runs a file on the technician's workstation; it saw no malicious activity from the sessions and found no overlap with the SCKit indicators.
discovered_at: "2026-11-15T04:27:47Z"
updated_at: null
event_date: "2026-11-14"
run_id: 2026-11-15T0356Z-intel
priority: notable
immediate_action: null
tags: [supply-chain]
regions: [global]
sectors: [technology]
entities: ["campaign:screenconnect-crypto-bait-sessions-2026-11", "product:connectwise-screenconnect"]
techniques: [T1219.002, T1036.005]
affected_products: ["ConnectWise ScreenConnect"]
cves: []
sources:
  - url: "https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect"
    publisher: "Huntress"
    date: "2026-11-14"
    role: primary
closed_sources: []
evidence:
  - quote: "As of this writing, we've found 2,223 fake sessions on 118 servers across 109 MSP and organization accounts."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect"
  - quote: "This is our leading hypothesis, but it's important to note that we have not observed the guest sessions being used this way."
    publisher: "Huntress"
    source_url: "https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect"
verification: single-source
sourcing_note: >
  Single source: Huntress is first-hand on the session counts, which come from the ScreenConnect session databases of the servers it protects and could reach, so they are a lower bound; no second party has reported the activity. Huntress states the bait purpose as an unobserved hypothesis and does not rule out other goals. Its post counts 2,223 fake sessions and, elsewhere, 2,408 unauthorized guest sessions, which appear to be different snapshots.
confidence: medium
references: ["2026-09-12/cve-2026-84869-connectwise-screenconnect-worm-file-transfer", "2026-11-12/screenconnect-sckit-toolkit-pushed-to-hundreds-of-endpoints"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On every self-hosted ScreenConnect server your organisation or its IT providers run, list guest sessions with an exchange-and-role name or empty company or site fields, copy App_Data\\Session.db and its WAL file before deleting any, and where a technician connected to one from a client older than 26.6.5, inspect that workstation's ScreenConnect Temp and Startup folders and process history and treat text sent through the session as exposed credentials, because Huntress suspects the sessions are bait for the file-transfer flaw CVE-2026-84869."
updates: []
migrated_from: null
---

Huntress counted 2,223 fake guest sessions on 118 self-hosted ScreenConnect servers across 109 MSP and organisation accounts, enrolled between 2026-11-03 and 2026-11-13: always-online "computers" named after crypto exchanges (an exchange word joined to a role word) with a trading-desktop thumbnail ([Huntress, 2026-11-14](https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect)). An MSP asked about them on 2026-11-12; its own server showed no web shells, suspicious child processes or new accounts, and the first Access installer Huntress examined was publicly downloadable, which ScreenConnect allows without authentication by design, and a guest client needs the server's relay address, which is embedded in that server's guest installer, to register. Huntress saw no malicious activity from the sessions: technicians who opened them mostly stayed under 30 seconds, and in one case a technician used the send-text feature, which ScreenConnect does not log, so Huntress treated it as a possible credential exposure. On 29 servers with complete history the operator revisited every 151 seconds to keep the sessions online ([Huntress, 2026-11-14](https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect)).

Huntress's leading hypothesis, which it has not observed, is bait: a technician who connects with a client older than 26.6.5 would let a malicious guest use the file-transfer flaw CVE-2026-84869 to run a file on the technician's workstation, often the MSP's most privileged machine; it cannot rule out capturing what a technician types, and it found no overlap with the published SCKit indicators ([Huntress, 2026-11-14](https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect)). It considers the public suggestion that the sessions are a malware sandbox detonating installers unlikely.

**Exposure:** a self-hosted ScreenConnect server whose Access guest installer is public or leaked, and every technician host client older than 26.6.5; server session history shows client versions ([Huntress, 2026-11-14](https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect)).

**Detection:** in the server session database, new guest sessions with ClientType 1 (Windows), an empty guest public key, empty company or site fields and crypto-site thumbnails (guest version 25.3.4.9288 is context, not unique on its own); in web or relay logs, many new Access guests from one external address in a short window; on technician workstations, `ScreenConnect.WindowsClient.exe` starting `cmd.exe`, `powershell.exe`, `wscript.exe` or `msiexec.exe` on a file under a Documents Temp folder, which Huntress calls the host-side shape of CVE-2026-84869 exploitation. A fake alone shows reachability, not exposure: compare technician-side with guest-side events ([Huntress, 2026-11-14](https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect)).

**Triage:** a malware-analysis sandbox detonating a ScreenConnect installer also creates guest sessions; per Huntress, a sandbox session sends a key and JPEG screenshots of the analysis VM, while these send no key, reuse seven screenshot families and randomise hardware and OS details ([Huntress, 2026-11-14](https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect)).

**Defender takeaway:** upgrade technician host clients to 26.6.5 or later, keep Access installer links private and rebuild leaked ones, restrict installer and web access where supported, bar technicians from joining sessions they cannot tie to a customer, and move unfamiliar sessions into a group technicians do not browse; in Huntress's hypothesis the target is a technician client below 26.6.5 ([Huntress, 2026-11-14](https://www.huntress.com/blog/fake-crypto-exchange-sessions-screenconnect)).
