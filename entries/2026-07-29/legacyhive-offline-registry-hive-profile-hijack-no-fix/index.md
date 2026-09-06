---
schema: 1
kind: research
title: >
  LegacyHive: a public Windows technique that redirects a profile's Local AppData into the NT
  Object Manager namespace via offline hive edits, reproduced on fully patched systems
headline: >
  LevelBlue reproduces Nightmare Eclipse's latest Windows PoC on a July-2026-patched build — no
  CVE, no fix, and the abuse uses only legitimate APIs
summary: >
  LevelBlue SpiderLabs published a full analysis on 2026-07-27 of LegacyHive, the latest public
  Windows proof-of-concept from the Nightmare Eclipse disclosure persona. It is not a software
  vulnerability: the chain edits a helper account's ntuser.dat offline through Microsoft's own
  Registry Offline API, repoints the User Shell Folders Local AppData value into an
  attacker-created NT Object Manager namespace, uses a batch opportunistic lock on UsrClass.dat to
  pause until profile initialisation reaches the right moment, then forces a profile load via
  CreateProcessWithLogonW with LOGON_WITH_PROFILE — aliasing into a third account's profile data
  without ever holding that account's credentials. LevelBlue reproduced the whole chain on fully
  patched Windows with July 2026 updates installed and reports no Microsoft mitigation for this
  class of abuse. It is strictly post-compromise: the attacker needs a low-privileged session plus
  a separate helper account's credentials.
discovered_at: "2026-07-29T05:40:00Z"
updated_at: "2026-08-12T04:47:30Z"
event_date: 2026-07-27
run_id: 2026-07-29T0408Z-intel
priority: notable
immediate_action: null
tags:
  - priv-esc
  - no-patch
  - poc-public
  - identity
  - vulnerabilities
  - lpe
  - patch-available
regions:
  - global
  - europe
sectors:
  - public-sector
  - finance
  - healthcare
  - energy
  - telco
  - technology
entities:
  - "actor:nightmare-eclipse"
  - "trend:nightmare-eclipse-legacyhive-profile-registry-hijack-2026-07"
techniques:
  - T1112
  - T1078
  - T1574
  - T1068
  - T1548
affected_products:
  - Microsoft Windows
cves:
  - id: CVE-2026-62832
    cvss: "7.8"
    epss: null
    type: priv-esc
    vector: local
    auth: post-auth
    status:
      - poc-public
      - patch-available
    affected: >
      Windows User Profile Service — the supported Windows range covered by the August 2026 cumulative
      update; Microsoft records the flaw as publicly disclosed and not exploited
    fixed: August 2026 Patch Tuesday cumulative update (released 2026-08-11)
sources:
  - url: "https://www.levelblue.com/blogs/spiderlabs-blog/legacyhive-hunting-windows-profile-initialization-abuse-through-offline-registry-manipulation"
    publisher: LevelBlue SpiderLabs
    date: 2026-07-27
    role: primary
  - url: "https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62832"
    publisher: Microsoft Security Response Center
    date: 2026-08-11
    role: primary
  - url: "https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026/"
    publisher: Rapid7
    date: 2026-08-11
    role: corroborating
  - url: "https://0patch.com/blog/micropatches-available-for-legacyhive-windows-user-profile-service-elevation-of-p"
    publisher: 0patch (ACROS Security)
    date: 2026-07-20
    role: corroborating
closed_sources: []
evidence:
  - quote: "As released, it requires control of a low-privileged account and the credentials of a separate helper account, making it more useful as a post-compromise capability than as a standalone attack. According to the disclosure, these limitations were intentionally introduced before publication to discourage immediate abuse."
    publisher: LevelBlue SpiderLabs
  - quote: "the registry modification itself is legitimate. LegacyHive uses valid registry structures, valid APIs, and a valid registry value type. The abuse happens because Local AppData no longer points to the user's normal profile directory. Instead, it points into the attacker-controlled Object Manager namespace."
    publisher: LevelBlue SpiderLabs
  - quote: "For EDR platforms with visibility into native Windows APIs, the strongest signals are user-mode invocations of NtCreateDirectoryObjectEx and NtCreateSymbolicLinkObject. These functions are rarely used outside system components, debugging tools, or specialized research utilities. Seeing both from the same process should immediately warrant investigation."
    publisher: LevelBlue SpiderLabs
  - quote: "LevelBlue OpsIntel CTI and Threat Operations and Research (THOR) teams reviewed and reproduced the complete LegacyHive exploitation chain on fully patched Windows systems with the July 2026 Patch Tuesday updates installed, confirming the PoC functions as described."
    publisher: LevelBlue SpiderLabs
  - quote: "Improper link resolution before file access ('link following') in Windows User Profile Service allows an authorized attacker to elevate privileges locally."
    publisher: Microsoft Security Response Center
  - quote: "the advisory is a solid match for Nightmare Eclipse’s description of LegacyHive"
    publisher: Rapid7
verification: single-source
sourcing_note: >
  Single-source: LevelBlue SpiderLabs' own analysis and independent reproduction of a publicly
  released proof-of-concept. Recency disclosure — the primary published 2026-07-27T14:07:50Z,
  roughly 38 hours before this run began and therefore outside its 26-hour window; it is carried
  on the developing-story allowance because the preceding fire did not surface it and because a
  working, unpatched technique against current Windows builds is not something to defer, with
  `event_date` recording the true publication date. The ATT&CK mapping is deliberately imprecise
  and flagged as such: Modify Registry covers the offline hive edit and Valid Accounts the
  helper-credential prerequisite, but no existing enterprise sub-technique describes profile-hive
  path redirection through Object Manager symbolic links, so the parent Hijack Execution Flow is
  used as the closest available category rather than asserting a sub-technique that does not fit.
  The proof-of-concept's own command-line arguments, the specific namespace path and LevelBlue's
  hunting-rule syntax are omitted. The `vulnerabilities` theme tag is deliberately absent: the
  source is explicit that this is not a software vulnerability, and carrying that tag would tell
  an automated consumer the opposite of what the body says. `priv-esc` is kept because the
  technique does cross an account boundary the attacker holds no credentials for, which is the
  capability on offer, even though it is not escalation from a standing start.
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
updates:
  - at: "2026-08-12T04:47:30Z"
    run_id: 2026-08-12T0411Z-intel
    type: update
    summary: >
      The LegacyHive proof-of-concept covered here on 2026-07-29, reproduced on fully patched Windows
      and described at the time as having no Microsoft mitigation, appears to be fixed. Microsoft's
      August Patch Tuesday shipped CVE-2026-62832, an improper-link-resolution elevation-of-privilege
      flaw in the Windows User Profile Service rated CVSS 7.8, publicly disclosed before the patch and
      assessed "Exploitation More Likely". Rapid7 assesses the advisory is a solid match for the
      researcher's description of LegacyHive; Microsoft's record does not name the technique, so the
      identification is Rapid7's judgement rather than a vendor confirmation.
    fields:
      - cves
      - evidence
      - regions
      - sectors
      - sources
      - tags
      - techniques
      - body
    merged_from: 2026-08-12/cve-2026-62832-legacyhive-user-profile-service-patched
migrated_from: null
---

LevelBlue is explicit that LegacyHive is not a traditional vulnerability — like the rest of the Nightmare Eclipse series it explores a corner of Windows rather than introducing a bug, in this case profile initialisation and registry hive loading ([LevelBlue SpiderLabs, 2026-07-27](https://www.levelblue.com/blogs/spiderlabs-blog/legacyhive-hunting-windows-profile-initialization-abuse-through-offline-registry-manipulation)). The chain runs in seven steps and every one uses documented, legitimate machinery. It first creates a directory hierarchy inside the NT Object Manager namespace via `NtCreateDirectoryObjectEx` called from user mode, which LevelBlue notes is itself unusual because normal applications almost never create Object Manager namespaces after system initialisation, then builds native Object Manager symbolic links inside it with `NtCreateSymbolicLinkObject` — not Windows shortcuts or NTFS junctions — to form the redirection layer ([LevelBlue SpiderLabs, 2026-07-27](https://www.levelblue.com/blogs/spiderlabs-blog/legacyhive-hunting-windows-profile-initialization-abuse-through-offline-registry-manipulation)). It then opens a helper account's `ntuser.dat` directly and edits it offline through Microsoft's Registry Offline API, replacing the Local AppData value under `Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders` with the redirected namespace path, before saving the hive back over the original ([LevelBlue SpiderLabs, 2026-07-27](https://www.levelblue.com/blogs/spiderlabs-blog/legacyhive-hunting-windows-profile-initialization-abuse-through-offline-registry-manipulation)).

The timing step is what makes it reliable rather than racy. Instead of retrying until it wins, the exploit takes a batch opportunistic lock on `UsrClass.dat`, which pauses execution until profile initialisation reaches the expected point — LevelBlue's framing is that the exploit does not fight the Windows startup process but uses Windows' own synchronisation features to control it ([LevelBlue SpiderLabs, 2026-07-27](https://www.levelblue.com/blogs/spiderlabs-blog/legacyhive-hunting-windows-profile-initialization-abuse-through-offline-registry-manipulation)). It then launches a process as the helper user via `CreateProcessWithLogonW` with `LOGON_WITH_PROFILE` — the point being not execution but forcing a normal profile load that consumes the tampered hive — and validates success through `RegOpenUserClassesRoot`. Cleanup removes temporary files but leaves the modified registry configuration and namespace redirection in place, so the persistence lives in on-disk state rather than in a process or scheduled task ([LevelBlue SpiderLabs, 2026-07-27](https://www.levelblue.com/blogs/spiderlabs-blog/legacyhive-hunting-windows-profile-initialization-abuse-through-offline-registry-manipulation)).

Two facts bound how much this should worry a defender, in opposite directions. Downward: the released proof-of-concept requires the attacker to control a low-privileged account *and* hold valid credentials for a separate helper account on the same machine, which LevelBlue says makes it more useful as a post-compromise capability than a standalone attack, and notes those limitations were intentionally introduced before publication to discourage immediate abuse ([LevelBlue SpiderLabs, 2026-07-27](https://www.levelblue.com/blogs/spiderlabs-blog/legacyhive-hunting-windows-profile-initialization-abuse-through-offline-registry-manipulation)). This is not remote, not pre-authentication, and not privilege escalation from nothing. Upward: what the attacker does *not* need is the credentials of the account whose profile data they end up reaching — that is the whole point of the technique — and LevelBlue's teams reproduced the complete chain on fully patched Windows with July 2026 updates installed, with no Microsoft mitigation existing for this class of abuse ([LevelBlue SpiderLabs, 2026-07-27](https://www.levelblue.com/blogs/spiderlabs-blog/legacyhive-hunting-windows-profile-initialization-abuse-through-offline-registry-manipulation)). LevelBlue also cautions that the published code demonstrates the technique rather than exhausting it, and expects variants to change how profile loading is triggered or which hives are targeted while relying on the same building blocks.

**Defender takeaway:** because there is nothing to patch, this converts entirely into a detection and credential-hygiene problem, and the strongest available signal is an unusually clean one. LevelBlue names user-mode invocation of `NtCreateDirectoryObjectEx` and `NtCreateSymbolicLinkObject` as rare outside system components, debugging tools and research utilities, and says seeing both from the same process should immediately warrant investigation ([LevelBlue SpiderLabs, 2026-07-27](https://www.levelblue.com/blogs/spiderlabs-blog/legacyhive-hunting-windows-profile-initialization-abuse-through-offline-registry-manipulation)). Two further telemetry classes are worth wiring up: file-access events showing `ntuser.dat` or `UsrClass.dat` being read or written outside their canonical per-profile locations, which is detectable independently of what the hive contains; and the per-user Volatile Environment registry key, where a `%LOCALAPPDATA%` value resolving into a kernel namespace rather than a filesystem path is a durable forensic artifact of a successful hijack. On the credential side, the prerequisite is the lever: the technique needs a second local account's password, so reducing how many accounts hold reusable local credentials with cross-account logon rights removes the precondition rather than the capability.

**Triage:** every individual operation here is legitimate — offline hive editing, an oplock on a profile hive, a logon-with-profile process launch — and LevelBlue's explicit position is that each is legitimate in isolation while observing them together in a short window is highly unusual and well suited to behavioural correlation. Note specifically that the target executable carries no discriminating value: LevelBlue demonstrates the PoC's `notepad.exe` is trivially substitutable, so detection must anchor on the calling pattern — a cross-account `CreateProcessWithLogonW` using `LOGON_WITH_PROFILE`, routed through the seclogon service — rather than on any process name.

## Update — 2026-08-12T04:47:30Z

The entry on LegacyHive — the Nightmare Eclipse Windows proof-of-concept that LevelBlue reproduced on a fully patched July-2026 build — recorded that the vendor offered no mitigation for that class of abuse. Microsoft's August Patch Tuesday appears to have closed it. CVE-2026-62832 is described in Microsoft's own record as "Improper link resolution before file access ('link following') in Windows User Profile Service allows an authorized attacker to elevate privileges locally", scored CVSS 3.1 7.8 (`AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H`), rated Important, recorded as publicly disclosed before the fix, not exploited, and assessed as "Exploitation More Likely" ([MSRC, 2026-08-11](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62832)).

Microsoft does not name LegacyHive, and the identification is worth attributing precisely rather than assuming. Rapid7 states that between the public disclosure and the advisory FAQ — which describes an authenticated attacker who has credentials for another account and loads another user's registry hive — "the advisory is a solid match for Nightmare Eclipse's description of LegacyHive" ([Rapid7, 2026-08-11](https://www.rapid7.com/blog/post/em-patch-tuesday-august-2026/)). That is an assessment by a third party, not a vendor mapping, which is why this entry carries it as such.

The independent detail that makes the match credible comes from the unofficial patch that preceded the official one. 0patch analysed the flaw in July and describes it in the same terms: the vulnerability lies in the Windows User Profile Service, where a time-of-check-to-time-of-use condition lets a local attacker use a symbolic link to confuse the service into loading any user's registry hive instead of the requesting user's, ending up mounted in the attacker's own registry space with read/write permissions. Its root cause, per 0patch, is an access-check fallback: when the service can open the hive file with full access it mounts it under the requesting user's identity using `NtLoadKey3`, which supports impersonation, but when it cannot, it falls back to the older `NtLoadKeyEx` without impersonation — so the hive loads with full access as Local System. The consequence 0patch names is the same one the original entry described from the attacker's side: read the target user's stored secrets, or replace paths to trusted executables and DLLs so they run the next time that user logs in ([0patch, 2026-07-20](https://0patch.com/blog/micropatches-available-for-legacyhive-windows-user-profile-service-elevation-of-p)).

For anyone who acted on the July coverage, the practical delta is short. The prerequisite is unchanged and still limits the blast radius — the attacker needs a local session plus credentials for a separate account, so this is a post-compromise escalation step rather than an entry point. The August cumulative update supersedes the 0patch micropatch as the remediation, and estates that deployed the community patch were covered in the interval. No action item ships with this entry: the fix arrives inside the ordinary Patch Tuesday cycle, and the entry exists to correct the record on the earlier "no fix available" framing rather than to open new work.
