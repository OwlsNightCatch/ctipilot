# extract: served via trafilatura-direct
---
title: How Attackers Abuse VSS, and How Huntress Detects It | Huntress
author: Shivangi Pandey; Matt Anderson
url: https://www.huntress.com/blog/vss-abuse-explained
hostname: huntress.com
description: Attackers exploit Volume Shadow Copy for credential theft and ransomware defense evasion. See how Huntress spots the difference from routine IT activity.
sitename: Huntress
date: "2026-09-14"
---
In our [__last post__](https://www.huntress.com/blog/microsoft-vss-limits-and-best-practices), we walked through what Microsoft's Volume Shadow Copy Service (VSS) actually does under the hood, and where it starts to buckle: the 64TB volume ceiling, the Copy-on-Write performance tax, the Windows lock-in, and the hard truth that a snapshot is not a recovery plan.

We ended on a warning: modern ransomware explicitly targets local shadow copies to stop you from rolling back. That's not a footnote. It's a core part of how ransomware operations operate today, and it's exactly the kind of behavior a detection and response program should be built around.

So this time, we're looking at VSS from the other side of the fence: what it looks like when an attacker actually touches it, and why "something deleted a shadow copy" is one of the least useful sentences you can put in a security alert.

## DIFFERENT Ways Attackers Use VSS

Most people think of [__VSS abuse__](https://www.huntress.com/blog/nightmare-eclipse-intrusion) as an attacker deleting the shadow copies right before detonating ransomware, making it hard for the victim to restore from a local backup. That's real, and it's common. In the MITRE ATT&CK Framework, this falls under [**__Inhibit System Recovery__**](https://attack.mitre.org/techniques/T1490/), specifically, preventing recovery. It's often just one step in a longer pre-encryption sequence, not the whole attack.

But deletion isn't the only play. Attackers also *create* shadow copies for an entirely different reason: credential access. Rather than running credential-dumping tools directly against a live, monitored system, an attacker can spin up a shadow copy and quietly pull the NTDS.dit file (the Active Directory database) out of it. Extracting secrets from a static file copied from a shadow copy is easier to hide than running extraction commands on a live command line, which is exactly why it's an attractive technique.

There's a third, quieter category…attackers manipulating shadow copy sizes and configuration as part of the same general tradecraft, rather than outright creating or deleting them.

VSS activity in a threat actor's hands can mean destruction, theft, or manipulation. For this reason, any detection strategy has to account for all three.

## Why "It Deleted a Shadow Copy" Isn't a Good Alert

Here's the catch: deleting or creating shadow copies is *also* completely normal behavior. Plenty of RMM tools and backup agents clean up old shadow copies on a regular schedule as part of basic disk hygiene. If a detection fired on every single deletion or creation event, security teams would drown in noise almost instantly, and the real attacks would get lost in it.

That means the raw event is nearly worthless as a signal on its own. What actually matters is everything happening *around* it.

## What Huntress Looks For

Huntress runs detections that monitor volume shadow copy activity on endpoints, but these detections aren't built to fire on deletion or creation events alone. They're built to fire on that event *plus* the context around it. Broadly, that context-gathering breaks down along the two abuse paths we described above.

Huntress [__ransomware detections__](https://www.huntress.com/use-cases/ransomware) look at how the deletion occurred, not just that it occurred. VSSAdmin is the most common way to delete shadow copies, but it's not the only one, and detections must account for other services and binaries that can quietly accomplish the same thing. 

A shadow copy being created isn't inherently suspicious; plenty of legitimate backup and RMM tools do it constantly. How do we decide if the credential access path being shown is suspicious? First, we look for creation paired with signs of lateral movement. And then we'll check for signs of credential harvesting before or after the activity. Coupled together, those signals bubble a routine-looking event up to "worth reporting" fast.

None of this works on a single event. Huntress correlates events over a time window rather than judging any single action in isolation. Lateral movement, followed by shadow copy activity, followed by credential-harvesting commands, is a materially different story than any one of those three things happening alone. That correlation, more than any single rule, is what lets Huntress tell "an admin's cleanup script ran" apart from "an attacker just took a step toward encrypting or stealing from this environment."

## What This Looks Like

It starts with a queue of completed signals. Several of them share the same rule family, shadow copy deletion or creation via VSSAdmin.

Two of those are deletions that turned out to be routine once reviewed. The third, a **shadow copy creation**, is the one worth zooming in on.

On its own, "a shadow copy was created" tells you almost nothing; it's one of the most common legitimate operations on a Windows host. What made this one worth a second look was the investigation that followed, which reconstructed the full sequence of events around it.

Laid out in order, the sequence reads like this: PsExec was used to spawn SYSTEM-level command shell processes on a domain controller. From there, the attacker enumerated active Remote Desktop sessions, then ran `vssadmin create shadow`, a technique commonly used to pull credentials out of the NTDS.dit database without touching it directly. A few minutes later, the attacker tried to cover their tracks by deleting the shadow copies they'd just created; that attempt was blocked and flagged by endpoint antivirus. Around the same time window, DNS enumeration commands and reconnaissance against at least one additional host also appeared, evidence of lateral movement rather than a single isolated action.

None of these steps alone would necessarily justify an alert. A shadow copy creation, by itself, is unremarkable. PsExec shows up in plenty of legitimate admin workflows. Even a blocked deletion attempt could be a false positive in isolation. It's the full context of the event, the credential-access attempts, a follow-up deletion attempt, and lateral movement to another host, all within one tight window, that makes this worth an analyst's time.

## Don't Trust the Shadow Alone

Volume shadow copies were never meant to be a security control; they're a Windows plumbing feature that happens to sit in the blast radius of most ransomware and credential-theft playbooks. Watching them closely is worthwhile. Treating every deletion or creation as an incident is not, and treating silence on that front as safety is worse. The same lesson from our last post applies here in a different shape: a snapshot doesn't protect you by existing, and a rule doesn't protect you by firing. Both need something more deliberate wrapped around them to be worth anything.

That's what 24/7 human review paired with correlation across process lineage, tooling, and time is for. [__See how Huntress keeps watch on the parts of your environment that attackers count on you to overlook.__](https://www.huntress.com/demo-tour)
