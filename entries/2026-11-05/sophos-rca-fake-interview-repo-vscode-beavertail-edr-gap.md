---
schema: 1
kind: incident
title: "Sophos's own root-cause analysis of a developer-targeted intrusion: a fake job-interview repository's VS Code workspace settings ran BeaverTail and InvisibleFerret on a Mac whose endpoint agent had not reported since 11 June, and a third-party OAuth authorization outlived the session revocation"
headline: "Sophos RCA: fake interview repo ran BeaverTail via VS Code settings; dead EDR agent, OAuth grant survived revocation"
summary: >
  Sophos discloses, as the victim, that on 2026-09-14 an employee cloned a repository presented as a job-interview coding assignment and opened it
  as a trusted VS Code workspace; its settings replaced the terminal profile, so opening a terminal downloaded and ran the BeaverTail loader and
  the in-memory InvisibleFerret backdoor on a Mac whose Sophos Endpoint agent had not reported since 2026-06-11. A third-party OAuth authorization
  on the employee's code-platform account survived the session revocation and read two internal repositories 27 times; Sophos found no other host
  and no customer impact.
discovered_at: "2026-11-05T03:57:00Z"
updated_at: null
event_date: "2026-09-14"
run_id: 2026-11-05T0255Z-intel
priority: notable
immediate_action: null
tags: [nation-state, infostealer, identity]
regions: [global]
sectors: [technology]
nexus: []
entities: ["incident:sophos-inc-2026-002-developer-job-lure-2026-09", "campaign:contagious-interview", "malware:beavertail", "malware:invisibleferret", "product:microsoft-visual-studio-code"]
techniques: [T1204, T1059.004, T1105, T1059.007, T1071.001, T1041, T1555.001, T1555.003, T1552.004, T1550.001, T1213.003]
affected_products: ["Microsoft Visual Studio Code"]
cves: []
sources:
  - url: "https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002"
    publisher: "Sophos (root-cause analysis INC-2026-002)"
    date: "2026-11-04"
    role: primary
  - url: "https://www.sophos.com/en-us/blog/fake-coding-test-reaches-security-company"
    publisher: "Sophos (blog)"
    date: "2026-11-04"
    role: primary
closed_sources: []
evidence:
  - quote: "The repository contained a weaponized VS Code workspace settings file that replaced the editor’s integrated terminal profile. When a terminal opened in the workspace, the modified profile silently downloaded and ran a multi-stage payload."
    publisher: "Sophos (root-cause analysis INC-2026-002)"
    source_url: "https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002"
  - quote: "The Sophos Endpoint agent was installed on the employee’s device but was not functional."
    publisher: "Sophos (root-cause analysis INC-2026-002)"
    source_url: "https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002"
verification: single-source-victim
sourcing_note: >
  Sophos is the victim and the only source: its root-cause analysis carries the timeline and the lessons, and its blog adds the tradecraft match.
  The analysis page is undated; the timeline dates are the analysis's own. Sophos says the actual actions on the device could not be fully recovered.
confidence: high
references:
  - 2026-11-04/binance-theft-fake-recruiter-ai-tool-pivot-deploy-token
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

On 2026-09-14 a Sophos employee cloned a public repository presented as a job-interview coding assignment and opened it as a workspace in VS Code; a weaponized workspace settings file replaced the editor's integrated terminal profile with a command that downloads and runs a remote script in a loop, delivery relied on the user opening the workspace as trusted, and no exploit or vulnerability was involved ([Sophos RCA, 2026-11-04](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)). Opening a terminal was enough: a shell script fetched a JavaScript component and a package manifest into a hidden directory in the user profile, a package-manager install ran, the JavaScript ran under Node.js and the final-stage backdoor lived in memory only, with no persistence found ([Sophos RCA, 2026-11-04](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)). SophosLabs identified the BeaverTail loader followed by the InvisibleFerret backdoor, able to steal browser-stored credentials, keychain data and SSH keys, and the JavaScript stage sent the process environment to an attacker web endpoint on a cloud application-hosting service ([Sophos RCA, 2026-11-04](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)).

Two gaps lengthened the exposure. The Sophos Endpoint agent was installed but its core services were not running, so it enforced nothing and reported nothing; the device was last seen in Sophos Central on 2026-06-11, the cause is still under investigation, and SophosLabs says a working agent would have blocked the chain at the first dropped file ([Sophos RCA, 2026-11-04](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)). A third-party application authorization on the employee's source-code platform account survived the session revocation and password reset of 2026-09-15 and made 27 read requests against two internal repositories from an address new to the user until it was revoked on 2026-09-16; Sophos found no other host, no cloud activity and no customer impact ([Sophos RCA, 2026-11-04](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)). The analysis names no group; Sophos CTU says the technique matches the tradecraft of NICKEL ALLEY, which it describes as running the Contagious Interview campaign of fake companies, fake recruiters and malicious code repositories ([Sophos blog, 2026-11-04](https://www.sophos.com/en-us/blog/fake-coding-test-reaches-security-company)).

**Exposure:** developer workstations whose users clone and open repositories from outside parties, recruitment pretexts included, in an editor that trusts the workspace; and any managed device that is compliant in identity and device management but does not report to the endpoint console, as Sophos's fleet review found ([Sophos RCA, 2026-11-04](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)).

**Detection:** in macOS process lineage, the code editor's integrated terminal launching a download-and-run command that a cloned workspace's settings define, followed by a hidden directory in the user profile and a package-manager install run from it ([Sophos RCA, 2026-11-04](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)). In identity telemetry, a device that still signs in but does not report to the endpoint console is a coverage gap; a third-party authorization reading repositories from an address new to the user is the second signal ([Sophos blog, 2026-11-04](https://www.sophos.com/en-us/blog/fake-coding-test-reaches-security-company); [Sophos RCA, 2026-11-04](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)).

**Triage:** a terminal profile normally launches a shell executable; this one launched a command that downloads and runs a remote script in a loop; it came from the settings of a freshly cloned repository ([Sophos RCA, 2026-11-04](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)).

**Defender takeaway:** treat a coding assignment or repository from a recruiter or interviewer as untrusted code, because here the compromise needed only a trusted workspace and an opened terminal. Sophos's lasting controls are to require the endpoint agent for device compliance, to monitor for managed devices that stop reporting, and to revoke application authorizations as part of credential containment, not only sessions and passwords ([Sophos RCA, 2026-11-04](https://www.sophos.com/en-us/trust/root-cause-analyses/inc-2026-002)).
