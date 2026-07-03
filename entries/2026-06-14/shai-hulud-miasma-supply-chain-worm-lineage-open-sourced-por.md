---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-multi-day
title: "Shai-Hulud / Miasma supply-chain worm lineage — open-sourced, ported to PyPI, and a 1,500-package AUR wave"
headline: "Shai-Hulud / Miasma supply-chain worm lineage — open-sourced, ported to PyPI, and a 1,500-package AUR wave"
summary: "The supply-chain-worm family the W23 weekly consolidated under the Miasma/IronWorm banner spent this week proliferating across ecosystems and operators. On 9 June a SANS ISC handler tracked TeamPCP open-sourcing its Mini Shai-Hulud framework, immediately spawning a \"Phantom Gyp\" derivative (SANS ISC; daily 06-09)."
discovered_at: "2026-06-14T23:57:21Z"
event_date: null
run_id: 2026-W24-bd5a7519
priority: notable
immediate_action: null
tags:
  - supply-chain
  - infostealer
  - botnet
regions:
  - global
sectors:
  - technology
entities:
  - "campaign:mini-shai-hulud"
  - "campaign:ironworm"
  - "actor:teampcp"
cves: []
sources:
  - url: "https://www.sonatype.com/blog/atomic-arch-npm-campaign-adds-malicious-dependency"
    publisher: Sonatype — Atomic Arch
    role: primary
  - url: "https://thehackernews.com/2026/06/over-400-arch-linux-aur-packages.html"
    publisher: The Hacker News — AUR wave
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/weekly/2026-W24.md
---

The supply-chain-worm family the W23 weekly consolidated under the Miasma/IronWorm banner spent this week proliferating across ecosystems and operators. On 9 June a SANS ISC handler tracked TeamPCP open-sourcing its Mini Shai-Hulud framework, immediately spawning a "Phantom Gyp" derivative ([SANS ISC](https://isc.sans.edu/diary/33060); [daily 06-09](/briefs/2026-06-09/)). On 10 June the lineage opened a PyPI front dubbed "Hades" — 37 malicious wheels across 19 packages ([The Hacker News](https://thehackernews.com/2026/06/hades-pypi-attack-19-packages-poisoned.html); [daily 06-10](/briefs/2026-06-10/)).

The week's largest wave hit the Arch User Repository. "Atomic Arch" began with roughly 400 orphaned AUR packages adopted and re-pointed to a Rust credential-stealer plus eBPF rootkit ([The Hacker News](https://thehackernews.com/2026/06/over-400-arch-linux-aur-packages.html); [Sonatype](https://www.sonatype.com/blog/atomic-arch-npm-campaign-adds-malicious-dependency); [daily 06-13](/briefs/2026-06-13/)); a second wave around 12 June expanded the count further (tracker estimates range from the 400+ in primary reporting to ~1,500) and swapped some PKGBUILD delivery from npm dependency injection to `bun install js-digest` — active operator iteration against detection. The npm delivery mechanism has been linked by SANS ISC and subsequent reporting to the broader Shai-Hulud supply-chain family. Official Arch core/extra repositories were not affected; only adopted AUR packages. For defenders the through-line is constant: install-time script execution is the kill chain, and `npm`/`bun`/AUR build steps need to be treated as untrusted code execution in CI/CD.
