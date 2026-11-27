---
title: "Inside Agentic Offensive Frameworks: Intent IDs"
author: Rami McCarthy; Hila Ramati
url: https://www.wiz.io/blog/agentic-offensive-frameworks-intent-ids-artex-cairn
hostname: wiz.io
description: Intent IDs (iNNNN) from agentic offensive frameworks like ARTEX and Cairn are leaking into victim logs. We break down how these counters work in code, how defenders can use them to pace and deconflict attacker activity, and where the signal breaks down.
sitename: wiz.io
date: "2026-11-25"
tags: ['Research', 'AI', 'Threat Intel']
fingerprint: "6799e29a6711c79f"
language: en
image: https://www.datocms-assets.com/75231/1795602437-agentic-attack_custom.jpeg?fm=webp
pagetype: article
filedate: "2026-11-27"
---
Intent IDs (iNNNN) from agentic offensive frameworks like ARTEX and Cairn are leaking into victim logs. We break down how these counters work in code, how defenders can use them to pace and deconflict attacker activity, and where the signal breaks down.

We want to dissect them as a new form of **harness leak** that flows from agentic offensive frameworks into defender logs.

## What are Intent IDs?

Intent IDs are incrementing counters in common agentic offensive frameworks. They are an internal implementation detail: the harness breaks an attack into discrete sub-goals called "intents" and assigns each one a numeric ID.

When a harness places that ID in its prompts and workspace paths, it bleeds into the attack: when the model creates a file, registers an account, pushes a GitHub workflow, or sets a User-Agent string on a target, it borrows the identifier sitting right in front of it.

There has been a [proliferation of agentic offensive frameworks](https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks#agentic-offensive-frameworks-4). We reviewed over a hundred open-source offensive harness repositories, and two families stand out for handing the LLM a numeric Intent ID that leaks into target-side artifacts:

1. **The ARTEX family**: ARTEX itself, plus public forks like Pojun (tracking current ARTEX as of `v0.4.99`) and AntiFox (forked from ARTEX `v0.1.1`).
2. **The Cairn family**: Cairn itself and descendants like `sapper-v2` (a reimplementation of Cairn's design).

### ARTEX

ARTEX stores intents, facts, findings, hints, and digests in one PostgreSQL table, exploration\_nodes, backed by a single `BIGSERIAL` sequence. Each installation runs its own counter and never resets it by default.

That design produces three traits defenders see in logs:

1. **Numbers climb across runs and targets**. A fresh campaign driven from a new ARTEX installation might start in the double digits (`i49` through `i63` in Ardor's disclosure). A long-running, busy installation climbs into the tens or hundreds of thousands (`i37257` at Chainstack).
2. **Intent IDs are rarely seen consecutively increasing**. Because facts, findings, hints, and digests draw from the same sequence as intents, consecutive intent numbers are rare.
3. **Facts stay local; intents leak**. Workers see fact IDs as bare integers in their planner snapshots. We checked 539 worker transcripts (\~10,900 shell commands) from an exposed ARTEX instance. Fact IDs appeared only in local scripts and notes (e.g `fact #461`).

In `agent/worker.go`, ARTEX wires the intent ID into three places the model reads on every turn: its working directory (`tasks/<task>/i<N>`), its session name (`exp<N>-worker-i<N>`), and the "意图 id" ("intent id") field in its prompt. Pojun keeps this exact layout. AntiFox goes further: its prompt orders the agent to save its outputs under an `i<id>/` subdirectory.

### Cairn

Cairn separates its counters by object type and leaves a distinct fingerprint.

In `services.py`, Cairn formats Intent IDs as zero-padded three-digit strings (`i%03d`) and gives each object type its own series:

- Intents: i001, i002, i003...
- Facts: f001, f002, f003...
- Hints: h001, h002, h003...
- Projects: proj\_001, proj\_002...

Unlike ARTEX, Cairn resets its counters for every new project. Numbers stay small and run without gaps. On one exposed Cairn host we examined, a single project held every intent from i001 through i292.

Cairn passes `{intent_id}` into its explore prompt as "Current Intent", and the worker reuses it in callbacks, DTD files, webshells, and test accounts.

`sapper-v2` reimplements the same `i%03d`/`f%03d`/`h%03d` per-project scheme.

## Pacing ARTEX Intent IDs

Because an ARTEX installation's sequence increments across runs and targets without resetting by default, plotting Intent IDs against timestamps can offer analysts a pacing signal.

### Linking Across IPs and Incidents

Agentic campaigns often rotate through residential proxy pools, using a new exit IP on nearly every request. Proxy rotation breaks IP-based clustering. Intent IDs cut across that noise: if activity from rotating IPs, or across separate victims, produces Intent IDs climbing at a steady rate over time, those sightings point to one ARTEX installation.

While tracking ARTEX-Harvester, we used rising Intent IDs alongside a distinctive boto3 build and proxy pool overlap to connect activity across more than a dozen organizations.

Intent IDs also survive a move between clouds. In one intrusion the attacker used stolen IAM users in AWS and a service principal in Azure. We found 36 Intent IDs on the AWS side, in SSM command comments and resource names, and 34 on the Azure side, in resource names, tags, and a role assignment description. All of them came from one climbing sequence, linking both to the same run even though the identities have nothing in common.

### Deconflicting Installations

The same sequence behavior works in reverse. Because `exploration_nodes.id` is a single `BIGSERIAL` counter per database, one ARTEX installation will not assign the same Intent ID to two different intents.

This property gives analysts a rough way to separate instances:

- Duplicate IDs across unrelated targets point to separate installations. Two campaigns hitting `i13211` against different victims are running on different ARTEX databases, not the same one. (A single worker will reuse its own ID across multiple requests and artifacts while working a single intent, so duplicates within one engagement are expected.)
- Out-of-order jumps signal a split. If a cluster of activity shows `i37257` on Monday and `i4100` on Tuesday, those requests are not coming from one continuous database sequence.

This deconfliction separates installations, not necessarily operators. One operator can run several ARTEX instances in parallel.

### Gauging Scope from a Single Victim's Logs

Even without cross-victim visibility, the size of the gaps between Intent IDs could indicate whether your are a dedicated target or one of many.

If a single attacker hits your environment with `i14200` at 10:00 and `i15100` an hour later, while your logs show only a handful of probes in between, those missing sequence numbers went somewhere. Some of that gap comes from facts, findings, hints, and digests recorded against your own assets. When a jump dwarfs the activity in your logs, the same ARTEX installation is likely burning through tasks against other targets in parallel: an opportunistic, multi-target run rather than an operator focused solely on you.

These signals are lossy. Intent ID pacing is a corroborating signal, not standalone attribution:

- **The rate of climb is uneven**. Facts, findings, hints, and digests share the sequence, and work against other targets advances the counter between sightings at one victim.
- **Unrelated installations collide in the same numeric ranges**. Fresh deployments all pass through the low hundreds and thousands, so two unrelated operators can produce numbers that look sequential by coincidence.
- **Operators reset or parallelize**. Rebuilding the container, wiping the database, or splitting targets across multiple ARTEX instances breaks the sequence.
- **Cairn resets per project**. Because Cairn restarts at `i001` for every new project, cross-incident pacing applies only to the ARTEX family.

## Intent IDs in the Wild

Across public disclosures, exposed harness directories, and our telemetry, we cataloged hundreds of distinct Intent IDs. A few extremes show how the two designs behave at scale:

- **Highest Intent ID**: `i808807`. Observed in ARTEX activity in November 2026, alongside `pentest-i804759` and `i806173` from the same series. An installation only reaches the 800,000s after churning through intents, facts, and findings across targets without a reset.
- **Lowest Intent ID**: `i001`. The bootstrap intent of a Cairn project recovered from an exposed Cairn host. Cairn's dispatcher creates `i001` automatically as a synthetic root edge connecting origin to the project's initial seed fact (`f001`), before worker intents begin at `i002`.
- **Longest consecutive runs**:
- **Cairn**: `i001` through `i292`. Every intent present in a complete project graph recovered from an exposed Cairn open directory.
- **ARTEX**: `i8920` through `i8923` (four in a row). Seen in `artex-verify-i89xx` User-Agent strings. ARTEX installations rarely string more than a few consecutive Intent IDs together because facts, findings, hints, and digests pull from the same sequence between intents.

## Hunting for Harness Leaks

Intent IDs are noisy on their own, so pair `i<N>` with an anchor before alerting. Good anchors include prefixes like `artex-`, `pentest-`, `probe`, or `canary` in account names, User-Agents, CI workflows, and cloud resources, or leaked run-directory paths such as `tasks/<task>/i<N>` in command-line telemetry. Hits are useful tool markers and pacing clues, but not operator fingerprints.

Where do these leak in logs? Anywhere that the API expects user-provided context, naming, or commentary. We have already observed these IDs in:

**AWS:**

- role session names
- SSM command comments
- bucket, role, user, and policy names
- tags and descriptions
- RDS export task IDs
- KMS key descriptions and aliases
- security-group names and rule descriptions

**Azure and Entra**:

- run-command names
- VM computer names
- app registration names

*Note: for denied calls, the names survive in error messages.*

Key highlights from government leaders, industry experts, and the Wiz FedRAMP team from our November 12th event on modernizing vulnerability management to meet FedRAMP’s new requirements.

Agentic offensive frameworks like ARTEX are driving a surge in cloud intrusions. Wiz Research shares cases from the wild, including both sides of one attack via the operator's leaked logs, an update on Black October, and the detections that catch these noisy, machine-speed attacks.

Get a personalized demo

## Ready to see Wiz in action?

> "Best User Experience I have ever seen, provides full visibility to cloud workloads."

David EstlickCISO

> "Wiz provides a single pane of glass to see what is going on in our cloud environments."

Adam FletcherChief Security Officer

> "We know that if Wiz identifies something as critical, it actually is."

Greg PoniatowskiHead of Threat and Vulnerability Management
