---
schema: 1
kind: research
title: "SANS ISC: Linux process-name masquerading via prctl(PR_SET_NAME) and how to detect it"
headline: "SANS ISC: Linux process-name masquerading via prctl(PR_SET_NAME) and how to detect it"
summary: "A SANS Internet Storm Center diary (2026-06-24) documents how Linux malware masquerades its process name via prctl(PR_SET_NAME, …), which writes the 15-character comm field in /proc/<pid>/comm — letting a process running ./ps-masquerade appear in ps/top/pgrep as a kernel worker thread such as …"
discovered_at: "2026-06-27T05:17:46Z"
event_date: 2026-06-24
run_id: 2026-06-27-40e791d4
priority: notable
immediate_action: null
tags:
  - espionage
  - china-nexus
regions:
  - global
sectors:
  - technology
entities: []
cves: []
sources:
  - url: "https://isc.sans.edu/diary/33102"
    publisher: SANS Internet Storm Center
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-27.md
---

A SANS Internet Storm Center diary (2026-06-24) documents how Linux malware masquerades its process name via `prctl(PR_SET_NAME, …)`, which writes the 15-character `comm` field in `/proc/<pid>/comm` — letting a process running `./ps-masquerade` appear in `ps`/`top`/`pgrep` as a kernel worker thread such as `[kworker/0:1-events]` ([SANS ISC, 2026-06-24](https://isc.sans.edu/diary/33102)). The detection key is the divergence between `/proc/<pid>/comm` (mutable) and `/proc/<pid>/cmdline` (the original argv, which the kernel will not grow beyond its fixed allocation): a genuine kernel thread has an *empty* `cmdline`, so any process whose `comm` resembles `[kworker/*]`/`[kthreadd]` but whose `cmdline` is non-empty is a high-fidelity hunt artefact. The diary points to eBPF-based tooling (Kunai) that captures the real command line at `exec` time independently of later `comm` mutation, and cites Operation Highland (Velvet Ant, Sygnia) as a real-world user of the technique (`T1036` Masquerading).
**Why it matters to us:** This is a free, immediately deployable hunt for any Linux fleet — and a useful complement to today's § 5 deep dive, where the same audit-blindness of in-memory tampering recurs.
