---
schema: 1
kind: research
title: "An independent researcher's lab test finds SAP's Security Audit Log carries no event for OS command execution via SM49/SM69 or RFC — only OS-level auditd sees the command on every path"
headline: "A SAP transaction that runs arbitrary OS commands leaves almost nothing in the log SAP itself designed to audit it"
summary: >
  An independent researcher's self-owned SAP NetWeaver AS ABAP lab test finds that SAP's Security
  Audit Log records no event type for OS-level external command execution launched through
  transactions SM49/SM69 or over RFC — a structural schema gap rather than a misconfiguration. Only
  OS-level auditd, correlated against the sapxpg parent-process chain, sees the full command line on
  every path; the researcher supplies concrete detection rules and the time-correlation method needed
  to bridge auditd's OS-account visibility with the SAP-user identity the audit log alone carries.
discovered_at: "2026-09-21T04:47:00Z"
updated_at: null
event_date: "2026-09-20"
run_id: 2026-09-21T0410Z-intel
priority: routine
immediate_action: null
tags:
  - identity
regions:
  - global
sectors:
  - public-sector
entities: []
techniques:
  - T1059
affected_products: ["SAP NetWeaver AS ABAP"]
cves: []
sources:
  - url: "https://detect.fyi/the-sound-of-silence-sap-sm49-sm69-and-the-os-commands-your-siem-never-hears-e408848cb6e2"
    publisher: "Detect FYI (author Rohan Taluja)"
    date: "2026-09-20"
    role: primary
  - url: "https://malware.news/t/the-sound-of-silence-sap-sm49-sm69-and-the-os-commands-your-siem-never-hears/125738"
    publisher: "Malware.news (full-text syndication of the same article)"
    date: "2026-09-20"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The only trace is a generic “Transaction SM49 started.” There is no event for the command, the binary, the parameters, the -exec payload, or the npladm context. A SIEM ingesting this log sees \"a user opened SM49\" and nothing more."
    publisher: "Detect FYI"
    source_url: "https://detect.fyi/the-sound-of-silence-sap-sm49-sm69-and-the-os-commands-your-siem-never-hears-e408848cb6e2"
  - quote: "auditd tells you what ran but not which SAP user triggered it (every SAP-spawned command is uid=<sid>adm), while the SAL knows the SAP user but not the command."
    publisher: "Detect FYI"
    source_url: "https://detect.fyi/the-sound-of-silence-sap-sm49-sm69-and-the-os-commands-your-siem-never-hears-e408848cb6e2"
verification: single-source
sourcing_note: >
  This is an individual practitioner's self-published research (a self-described "responsible-research
  note" on a self-owned SAP Developer Edition lab), not a named vendor or lab with an established CTI
  track record — reliability is rated F (no track record to evaluate) rather than the B/C typical of a
  research lab, independent of the content's internal consistency. The true primary, detect.fyi, 403'd
  on every transport on first attempt but was reached directly via the jina reader on a later attempt the
  same day; its content is identical to the malware.news syndication mirror cited alongside it. No second
  independent research source corroborates this finding.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: F
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

An independent researcher, publishing on Detect FYI / Medium and syndicated in full via malware.news, demonstrates on a self-owned SAP NetWeaver AS ABAP 7.52 lab that SAP's Security Audit Log (SAL) carries no event type or field for OS-level "external command" execution launched via transactions SM49/SM69 or over RFC — a structural gap in the log's schema, not a misconfiguration that can be turned on ([Detect FYI, 2026-09-20](https://detect.fyi/the-sound-of-silence-sap-sm49-sm69-and-the-os-commands-your-siem-never-hears-e408848cb6e2)). External commands run through the `sapxpg` helper process as the `<sid>adm` OS-owner account, and the researcher found that most Linux-applicable SAP-delivered command definitions accept additional runtime parameters, so the binary actually executed at runtime can differ entirely from the one an administrator defined — demonstrated by using a `find`-with-`-exec` command definition to run `/usr/bin/id` instead of its intended target. On the interactive SM49 path, the SAL records only a generic "Transaction SM49 started" event, with no command, binary or parameter data, even with every audit class enabled. On the RFC path, the SAL at best records an "RFC call" event naming only the invoked function module (`SXPG_COMMAND_EXECUTE`), never the command or its arguments. Only the background-job path (SM36) records the full command and its output, and it does so in the job log rather than the Security Audit Log.

OS-level `auditd` is the only source that sees the full argument vector on every path, via the `sapxpg` parent-process chain (SAP work process → `sapxpg` → target binary) — but the researcher flags three practical failure modes: the `-a task,never` audit rule, which some SUSE/SLES builds ship active and others omit entirely, silently suppresses `execve` auditing for new tasks; runtime `auditctl` changes do not survive reboot unless persisted under `/etc/audit/rules.d/`; and a bare `execve` rule is noisy unless filtered on a `ParentImage` ending in `sapxpg`, since that name matches both the SAP work-process binary and the SAP Host Agent's own `sapxpg` (the latter running as root). Because the SAL always knows the SAP user but never the command, and `auditd` always knows the command but only the OS account, the researcher recommends bridging the two by time-correlating the SAL's SAP-user timestamp — or, on the background path, simply reading the self-sufficient job log — against the `auditd` `execve` record within a tight window to reconstruct the full "this SAP user ran this OS command as `<sid>adm`" statement.

**Defender takeaway:** any organization running on-premises SAP with external OS commands enabled should confirm `auditd` is capturing `execve` events with a `ParentImage` filter on `sapxpg` (not a bare rule, and not suppressed by `-a task,never`), persist that rule under `/etc/audit/rules.d/` so it survives reboot, and build the SAL-to-auditd time-correlation join described above rather than relying on the Security Audit Log alone — which, on the interactive and RFC paths, cannot answer "what command ran," only "that someone opened SM49."

**Triage:** a `sapxpg` child process running a benign, expected command is routine SAP operation and not itself a signal. The researcher's recommended discriminator is content-based: a high-severity alert on any `sapxpg`-child command line carrying injection gadgets (`-exec`, an interpreter invocation, shell metacharacters) versus a lower-severity baseline rule matching any `sapxpg` child regardless of content, to establish what normal looks like in a given environment before tuning the higher-severity rule.
