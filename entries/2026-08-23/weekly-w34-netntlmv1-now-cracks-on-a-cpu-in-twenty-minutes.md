---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "The cost argument for leaving NetNTLMv1 enabled just collapsed — Sophos published a CPU-only rainbow-table pipeline that recovers the NT hash in under 20 minutes on one server, work that previously occupied GPUs for up to eight hours, and released the tool"
headline: "No GPU farm required any more: a captured v1 response resolves to the NT hash inside a lunch break"
summary: >
  Sophos X-Ops published a bitsliced, AVX2-vectorised CPU implementation of NetNTLMv1 rainbow-table
  lookup that reaches about 2.1 billion DES operations per second on a single 64-core EPYC processor,
  roughly fifteen times its own scalar baseline, by eliminating the DES key schedule that accounted
  for 85% of scalar cost. Its stated end-to-end result: the same downgrade lookup that previously
  occupied GPUs for up to eight hours now completes in under 20 minutes on a single server, without
  consuming a GPU cycle. The pipeline runs against the complete NetNTLMv1 DES rainbow table set
  Mandiant published in 2026 — 4,096 files of roughly 2 GB covering the full 56-bit keyspace — and
  Sophos has released its implementation publicly as a dependency-free C toolset. The precondition is
  unchanged and is the only thing standing between a captured response and the account's NT hash: the
  attacker needs a v1 response taken under a static server challenge, which the standard
  forced-authentication tooling can request. Any Active Directory estate still permitting NetNTLMv1
  negotiation for legacy compatibility has been relying, knowingly or not, on an offline-cracking
  cost that no longer exists.
discovered_at: "2026-08-23T23:58:30Z"
event_date: "2026-08-17"
run_id: 2026-08-23T2311Z-weekly
priority: notable
immediate_action: null
tags: [identity, priv-esc, poc-public]
regions: [global, europe]
sectors: [public-sector, energy, water, transport, healthcare, finance, telco]
entities: []
techniques: [T1557.001, T1110.002, T1187]
affected_products: ["Microsoft Windows Server", "Microsoft Active Directory"]
cves: []
sources:
  - url: "https://www.sophos.com/en-us/blog/accelerating-netntlmv1-lookups-without-gpus"
    publisher: "Sophos X-Ops"
    date: "2026-08-17"
    role: primary
closed_sources: []
evidence:
  - quote: "The same downgrade lookup that previously occupied GPUs for up to eight hours now completes in under 20 minutes on a single server, and faster across a small cluster, without consuming a single GPU cycle."
    publisher: "Sophos X-Ops"
  - quote: "Threat actors thrive on the availability of legacy technology that survives long after its security integrity has expired."
    publisher: "Sophos X-Ops"
verification: single-source
sourcing_note: >
  Single-source by nature rather than by omission: this is a lab's own engineering result and
  published benchmark, and there is no second party who has independently measured the same pipeline.
  Sophos X-Ops is an original research publisher (Admiralty B) and the claim is falsifiable — the
  implementation is released publicly and the underlying table set is Mandiant's, both checkable. The
  figures quoted are Sophos's own measurements on its own hardware and are carried as such. Note the
  vantage point: this is a Sophos Red Team publication about its own offensive workflow, and its own
  "what defenders can do" section is a general argument about legacy technology rather than a
  specific configuration recommendation; the disable-negotiation conclusion below is derived from the
  precondition the article itself states, not attributed to Sophos as advice.
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Determine whether NetNTLMv1 negotiation is still permitted anywhere in the domain — check the LAN Manager authentication level policy applied to domain controllers and to any host group carrying a legacy compatibility exception — and where a v1 response can still be produced, treat every account that authenticates through those hosts as having a recoverable NT hash."
migrated_from: null
---

NetNTLMv1 has survived in Active Directory estates for a decade on an implicit cost argument. The protocol encrypts the derived NT hash under 56-bit DES, which is mathematically broken, but recovering a key from a captured response has meant either a large precomputed table set and hours of GPU time or a cracking rig nobody has spare — so a legacy exception for an old appliance, a scanner or an unsupported application has looked like an accepted risk rather than an open door. Sophos X-Ops published the work that removes the cost side of that argument.

The engineering is straightforward and is the point. A scalar CPU implementation reaches about 144 million DES operations per second on a 64-core EPYC, which puts a single precompute at about 45 minutes and spends most of that time in the DES key schedule rather than in encryption. Bitslicing treats a CPU register as parallel one-bit lanes instead of one value, turning each DES S-box into a small Boolean gate network; widening the slice from a 64-bit word to a 256-bit AVX2 vector quadruples the parallelism to 256 simultaneous DES operations; and because a rainbow chain derives its keys deterministically, the key schedule can be replaced by a precomputed wiring map — which matters because, as Sophos puts it, the key schedule was 85% of the scalar cost. The result is about 2.1 billion DES operations per second on a single 64-core EPYC, roughly fifteen times the scalar baseline, and a precompute that drops from about 45 minutes to about three ([Sophos X-Ops, 2026-08-17](https://www.sophos.com/en-us/blog/accelerating-netntlmv1-lookups-without-gpus)).

The end-to-end figure is the one to carry into a risk conversation: "The same downgrade lookup that previously occupied GPUs for up to eight hours now completes in under 20 minutes on a single server, and faster across a small cluster, without consuming a single GPU cycle" ([Sophos X-Ops, 2026-08-17](https://www.sophos.com/en-us/blog/accelerating-netntlmv1-lookups-without-gpus)). The table set it runs against is not new either — Sophos states that in 2026 Mandiant published a complete NetNTLMv1 DES rainbow table set for the fixed-challenge scenario, 4,096 files of roughly 2 GB each covering the full 2^56 keyspace at about 9 TB total — so the precomputation is a public good the attacker does not have to fund. Sophos has released its own implementation publicly as a dependency-free C toolset. Nothing in the chain now requires specialist hardware or a specialist budget.

Sophos is equally clear about what still gates it, and this is the half a defender can act on: the attacker needs a captured v1 response taken under a static server challenge. The article names the standard forced-authentication tooling flags used to request that downgrade, and notes plainly that sometimes it works and sometimes it does not — where it does not, the GPUs remain the fallback. That precondition is the whole control surface. An estate that does not negotiate NetNTLMv1 produces no response for the pipeline to consume; an estate that does produces one for every coerced or poisoned authentication its hosts answer.

Its closing observation generalises past this protocol: "Threat actors thrive on the availability of legacy technology that survives long after its security integrity has expired" ([Sophos X-Ops, 2026-08-17](https://www.sophos.com/en-us/blog/accelerating-netntlmv1-lookups-without-gpus)).

**Defender takeaway:** the horizon shift here is a re-pricing, not a new attack, and it lands on a specific class of decision that European public-sector and industrial estates make routinely — the legacy authentication exception granted for one old system and never revisited. The mechanics of the article settle the risk question on their own: if a host in your domain will negotiate NetNTLMv1, then any of the ordinary forced-authentication techniques that reach it — name-resolution poisoning on a local segment, a coerced SMB or HTTP authentication from a machine account — yields a response, and that response now resolves to the account's NT hash in commodity server time regardless of how long or complex the password is. Password policy is not a mitigating factor for this and never was; the cracking cost was, and it is gone. Two things are worth doing this week and both are inventory rather than engineering: establish whether v1 negotiation is permitted anywhere in the domain at all, and — because the exception is usually granted per host group rather than domain-wide — establish which accounts authenticate *through* those hosts, since it is their hashes that are recoverable, not the legacy appliance's. **Triage:** there is no attack telemetry to key on here, because the expensive half of the attack happens offline on the attacker's own hardware and produces nothing observable in the victim estate. The only detectable moment is the capture — an authentication negotiated down to v1, or the forced-authentication step that provoked it — which is exactly why removing the ability to negotiate is a better control than watching for the consequence.
