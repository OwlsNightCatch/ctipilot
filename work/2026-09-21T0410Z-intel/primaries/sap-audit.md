# extract: served via trafilatura-direct
---
title: "The Sound of Silence: SAP SM49/SM69 and the OS Commands Your SIEM Never Hears"
author: MalBot
url: https://malware.news/t/the-sound-of-silence-sap-sm49-sm69-and-the-os-commands-your-siem-never-hears/125738
hostname: malware.news
description: "The audit blind spot in external OS command executionResponsible-research note. Everything below was performed on a self-owned SAP lab. No third-party or production system was involved. The purpose is defensive: to show exactly where SAP does, and does not, record operating-system command execution, and to give blue teams working detections and remediation. The audit-log screenshots have been redacted to remove the workstation account name and local file paths; the remaining identifiers (vhcaln..."
sitename: Malware Analysis, News and Indicators
date: "2026-09-20"
---
### The audit blind spot in external OS command execution

***Responsible-research note.*** *Everything below was performed on a self-owned SAP lab. No third-party or production system was involved. The purpose is defensive: to show exactly where SAP does, and does not, record operating-system command execution, and to give blue teams working detections and remediation. The audit-log screenshots have been redacted to remove the workstation account name and local file paths; the remaining identifiers (**vhcalnplci,* *NPL,* *npladm) are the public defaults of the free SAP Developer Edition and carry no sensitive information. No IP addresses, credentials, or license keys appear anywhere in this article.*

### Why I went looking

Every SAP hardening checklist says the same thing about external operating-system commands: restrict S_LOG_COM and S_RZL_ADM, and review your SM69 command list. Good advice. But it answers only half the question. The other half — the half nobody seems to write about — is this:

**When an external OS command *does* run, what does SAP actually log, and where?**

I expected the answer to be “the Security Audit Log, in some awkward field.” The real answer is stranger and more useful for defenders: on the most common execution path, the Security Audit Log records **nothing** about the command at all. Whether the command is captured anywhere depends entirely on *how* it was launched. This article is the evidence for that, end to end, on a live system.

**Environment (all findings are scoped to it):** SAP NetWeaver AS ABAP 7.52 SP04 (Developer Edition), kernel 753 patch 400, on openSUSE Leap 15.3, SAP ASE database, auditd 2.8.5. Newer releases or S/4HANA may behave differently and should be re-tested.

### The mechanism, in one diagram

An external command maps a logical name to an OS binary. When it runs, the SAP work process hands off to a helper, sapxpg, which launches the binary as the <sid>adm OS user. The process ancestry at the OS layer is always:

SAP work process  →  sapxpg  →  <the defined binary>

Two properties drive everything that follows:

1. **It runs as** **<sid>adm** — the account that owns the SAP installation, including the profile and audit directories.
2. **The definition and the runtime parameters are separate.** A command can point at a general-purpose binary and allow extra parameters at run time. On this system,**72 of 75** Linux-applicable SAP-delivered commands ship with additional parameters allowed. So the risk lives in the runtime parameter string, not just the stored definition — which is precisely why “review your command list” is not enough, and why you must capture what actually executed.

Here is a command definition in SM69. Note what SAP *does* structure: it records who created the definition and when, in proper fields.

### Step 1 — Proof the command runs as <sid>adm

Running a defined command in SM49 returns the OS output directly. Here the command executed and returned the identity of the process — uid=…(npladm), the SAP OS user. An ABAP dialog user just caused code to run on the host.

That alone is expected behaviour for an authorized user. The security-relevant twist is the next step.

### Step 2 — The definition is not the command

I defined a command pointing at a perfectly ordinary binary, find, and supplied the rest at run time. The runtime parameters used find’s own -exec feature to run a *different* binary, /usr/bin/id. The binary that actually executed appears **nowhere** in the SM69 definition — only in the runtime parameter string.

This is the crux for a defender: **you cannot detect this by inspecting command definitions.** Detection depends entirely on capturing the runtime command line. Which brings us to the logging.

### Step 3 — First, prove the audit log is actually recording

A blind test is worthless if you can’t tell “not logged” from “logging was off.” So before every capture I confirmed the Security Audit Log was live by generating a known event and reading it back.

With recording confirmed live, every negative result below is real.

### Step 4 — The dialog path: the log says nothing

I executed the find-with–exec command interactively, inside the confirmed-live audit window, and read the Security Audit Log back for that exact period.

The only trace is a generic *“Transaction SM49 started.”* There is no event for the command, the binary, the parameters, the -exec payload, or the npladm context. A SIEM ingesting this log sees “a user opened SM49” and nothing more.

Re-running it with every audit class enabled and the user filter wide open changes nothing:

### Why the log can’t help here

The Security Audit Log is a fixed-format log: each event is a message ID plus a few positional variable slots. There is no event type for “external command executed,” and no field that carries a command line. Even where SAP *does* structure “what was invoked” — the transaction code for a dialog transaction, the function name for an RFC call — there is simply no equivalent for the OS command. The command has nowhere to go in that schema.

A small illustration from the same day’s log tells the whole story: mistyping a transaction code generated a **Critical** severity audit event, while running an OS command as npladm generated, at most, a routine “transaction started” line. The log treats a typo as more alarming than command execution.

### Step 5 — The RFC path: still silent

External commands can also be invoked as a remote-enabled function over RFC. I created a loopback destination and called the function through it — the command executed successfully.

The Security Audit Log for that window recorded only a generic RFC logon line (AU5), no command and no parameters. There *is* an RFC-function-call audit event (AUK) that names the invoked module — I saw it capture other function calls in the same log — so on a fully-audited RFC path you would expect a Successful RFC call SXPG_COMMAND_EXECUTE. But note what that gives you even at its best: the *function* name, never the OS command or its parameters. Auditability without visibility. In this same-system loopback capture even that event didn’t fire (the SAL held only the logon), but either way the command itself is absent.

### Step 6 — The background path: the one place it is recorded

Here is the reconciliation. This whole project began with a simple question: when an external command *does* get recorded, where does the command actually land? The answer depends entirely on the execution path — and this is the path where it finally shows up.

I ran the identical command as a background job step (SM36).

The **job log** records the command name, the full parameter string, and the command output — as free-text message entries:

There it is: the command, its parameters, and its output, all in message-text fields. But note *where* this lives — the **job log** (TBTC* tables / job-log files), **not** the Security Audit Log. And the Security Audit Log for that same minute? Empty:

Same action, opposite outcome: nearly invisible when run interactively, fully recorded when scheduled — but in a different log, collected through a different pipe. One thing worth flagging for SAP teams: because OS auditd (next section) captures the full command on *every* path, ingesting job logs is useful but not strictly necessary. The job log is the SAP-native option and it catches the background path even where OS-level auditing isn’t in place — but if you collect auditd, you already have the command.

### Step 7 — The only source that always sees it (and why it’s usually blind)

OS-level auditd records the full command on every path, because everything funnels through sapxpg. Here is the verified chain in **native auditd fields** (values trimmed for length):

# sapxpg itself — the parent process

type=SYSCALL … pid=5310 comm=sapxpg exe=/usr/sap/NPL/D00/exe/sapxpg uid=npladm key=sap_xpg

# the command sapxpg runs - full argv; its parent (ppid) is 5310, i.e. sapxpg

type=EXECVE … a0=find a1=/tmp a2=-maxdepth a3=0 a4=-exec a5=/usr/bin/id a6=;

type=SYSCALL … pid=5311 ppid=5310 comm=find exe=/usr/bin/find uid=npladm key=sap_xpg

Note the native form: auditd records a numeric parent PID (ppid), not a parent name. In this capture the child shows ppid=5310; to know that 5310 is sapxpg, you correlate it with sapxpg’s own execve record, where pid=5310. Those PIDs are per-execution and will differ on your system, it’s the correlation by PID that matters, not the value. Some tools do that matching for you — Sysmon for Linux, Auditbeat/Elastic, or an EDR — and hand you a ready-made ParentImage field. So the detection comes in two flavours: the process_creation rules use that friendly ParentImage field (so they need one of those tools), and the raw-auditd rules read auditd’s own fields directly (a0, comm, exe) with no extra tooling. Whichever you use, you get what the SAP logs never give you: the command, its arguments, the user it ran as, and the sapxpg parent. Yet three things make auditd blind in practice:

1. **Often off — but verify on your build.** On SUSE/SLES the audit policy may ship with -a task,never active. That filter is evaluated when a task is created and gives new tasks no audit context, which suppresses their execve records. On many builds the line ships*commented out* , in which case execve is simply off because no execve rule is present — not because anything is suppressing it. Either way you record nothing until you check. Verify with auditctl -l and grep task,never /etc/audit/rules.d/*.rules (the canonical form is task,never; never,task is also accepted).*
2. ***Lost on reboot.** A runtime auditctl rule, and a runtime removal of task,never, don’t persist; on restart augenrules reloads /etc/audit/rules.d/ and undoes both. “Set up once” quietly becomes “not auditing” again unless you persist it in rules.d.*
3. ***Noisy without a filter.** A bare execve rule captures every process on the host — the SAP Host Agent’s monitoring alone spawns dozens continuously as uid=root. The real discriminator is **parent** **sapxpg**: that monitoring noise is *not* a sapxpg child. Should you also require uid=<sid>adm to trim root noise? Don’t. The Host Agent ships its own sapxpg at a different path (/usr/sap/hostctrl/exe/sapxpg, same basename as the work-process one under /usr/sap/<SID>/…/exe/), and Host-Agent-driven external commands there are **run as** **root**. I tested the dialog, RFC and background paths, not that one, so treat it as verify-on-your-build. It’s exactly why the rule matches ParentImage|endswith: ‘sapxpg’ rather than a full path: endswith catches **both** sapxpg binaries, and leaving the uid filter off means a root-running Host-Agent execution isn’t missed. Omitting the uid filter is strictly the safer choice.*

*An honest limit to state plainly: auditd tells you *what* ran but not *which SAP user* triggered it (every SAP-spawned command is uid=<sid>adm), while the SAL knows the SAP user but not the command. Neither source alone gives the full sentence — but you can bridge them by **time-correlation**: join the SAL’s SAP-user-plus-timestamp record with the auditd execve (uid=<sid>adm plus timestamp) in a tight window. The SAL anchor differs by path: the dialog path’s Transaction SM49 started, or the RFC path’s AUK RFC-call event. The background path needs no bridge at all — the job log already carries both the user and the command. It is imperfect for the interactive paths — SAP reuses work-process PIDs, so the window has to be narrow — but it is the only route to the whole sentence: *this SAP user ran this OS command as* *<sid>adm at this time.**

*A practical aside: you don’t have to wrestle with raw auditd. **Sysmon for Linux**, an **EDR agent** (Elastic Defend, CrowdStrike, Microsoft Defender for Endpoint on Linux), or **eBPF tooling** (Falco, Tetragon) all emit process-creation events carrying the parent image and command line the detection rules key on — and they sidestep the task,never and reboot-persistence problems above. Raw auditd proves the point here; in production most teams will collect this through Sysmon-for-Linux or their EDR. And when you do stay on auditd, persist the rule in /etc/audit/rules.d/ and load it with augenrules --load rather than runtime auditctl, which is lost on reboot.*

### *The whole picture, on one page*

*Same command, three execution paths, five log sources.  = command/arguments recorded; ✘ = not recorded.*


### Detection

So what do you actually detect on? The detections come in two tiers.

The **alert** is the higher-fidelity rule: a sapxpg child whose command line carries injection gadgets (-exec, an interpreter, shell meta characters) — that’s the one to page on, at high. The **visibility** rule matches *any* child of sapxpg, so the command and its runtime arguments arrive in a single event on every execution path; because it also fires on every legitimate external command, it runs at medium as a hunting and baselining signal.

Alongside those, there’s a native-auditd variant for raw-auditd pipelines — keying on a0, comm, and exe directly instead of a normalized ParentImage — and a job-log rule for the background path. Each one is written against the actual log records captured here, with negative cases to keep false positives down.

Deliberately, there is no Security Audit Log rule for the execution: there is nothing to key on. The only SAL-side signal worth collecting is the RFC-function-call event (AUK), and it names the function (SXPG_COMMAND_EXECUTE), not the command.

### Remediation (impact-ordered)

1. ***Fix and persist the OS audit policy.** First check whether task,never is active (auditctl -l; grep task,never /etc/audit/rules.d/* .rules) and remove it if so. Add a persistent execve rule under /etc/audit/rules.d/, run augenrules --load, and confirm auditctl -l shows the rule with no task,never. Runtime auditctl changes don’t survive a reboot — persist them in rules.d. This is the only source that sees the argument vector on every path.
2. **Collect OS auditd; job logs are optional.** OS auditd captures the full command on every path, so it is the source to ingest. Job logs are a useful SAP-native addition — they catch the background path even without OS-level auditing — but not strictly necessary if you already collect auditd. Either way, don’t rely on the Security Audit Log for this behaviour.
3. **Restrict execution, not just definitions.** Hold S_LOG_COM and S_RZL_ADM tightly and review SAP_ALL. Cover the other invocation paths too:**S_RFC** for the RFC route (the SXPG_* function group), and the background-job objects**S_BTCH_JOB** /**S_BTCH_ADM** for who can schedule the SM36 external-command step. Because most shipped commands already allow runtime parameters, restricting*execution* matters more than curating the list.
4. **Protect on-host log integrity.** The run-as account owns the audit and profile directories, so enable audit-log integrity protection and forward logs off-host promptly.
5. **Monitor definition changes** as defense-in-depth — secondary, since the technique uses shipped commands plus runtime parameters.
6. **Stay current** and review the relevant SAP security notes for the external-command area.

### The sound of silence

The headline isn’t “SAP doesn’t log this.” It’s sharper: **auditability is not the same as visibility.** For external OS command execution, the command lands in a message field only in the job log (and only when scheduled), in structured fields only in OS auditd (and only when auditing is correctly configured and persisted), and nowhere at all in the Security Audit Log. Which log you collect, and how the command was run, decides whether you ever hear it.

If you run SAP: collect OS auditd (job logs optional), deploy the detections, and stop treating the Security Audit Log as your sole record of host-level activity.

*Performed on a self-owned lab for defensive research. Audit-log screenshots redacted for the workstation account; the identifiers shown are SAP Developer Edition defaults.*

[The Sound of Silence: SAP SM49/SM69 and the OS Commands Your SIEM Never Hears](https://detect.fyi/the-sound-of-silence-sap-sm49-sm69-and-the-os-commands-your-siem-never-hears-e408848cb6e2) was originally published in [Detect FYI](https://detect.fyi) on Medium, where people are continuing the conversation by highlighting and responding to this story.

## Introduction to Malware Binary Triage (IMBT) Course

Looking to level up your skills? Get **10% off** using coupon code: **MWNEWS10** for any flavor.

[Enroll Now and Save 10%: Coupon Code MWNEWS10](https://training.invokere.com/link/QHLuD5/MWNEWS10?url=https%3A%2F%2Ftraining.invokere.com)

*Note: Affiliate link – your enrollment helps support this platform at no extra cost to you.*
