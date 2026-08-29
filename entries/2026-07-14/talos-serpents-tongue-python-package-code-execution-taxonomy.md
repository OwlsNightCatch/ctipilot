---
schema: 1
kind: research
title: "Cisco Talos maps the full taxonomy of Python-package build-time and import-time code execution (\"The Serpent's Tongue\")"
headline: "Talos catalogues where malicious Python packages execute code across the install lifecycle, including persistent .pth and site-hook footholds"
summary: >
  Cisco Talos published a lifecycle survey of code-execution paths in Python packaging — from setup.py running
  at install time to persistent .pth files, site-hook modules and PYTHONPATH hijacking that fire on every
  subsequent Python invocation — tying the taxonomy to real TeamPCP supply-chain compromises (litellm, lightning).
  It is a reference for supply-chain defenders and a concrete hunt surface for teams running Python build/CI
  pipelines.
discovered_at: "2026-07-14T20:22:57Z"
event_date: "2026-07-14"
run_id: 2026-07-14T2009Z-intel
priority: notable
immediate_action: null
tags: [supply-chain]
regions: [global]
sectors: [public-sector, technology]
entities: [actor:teampcp]
techniques: [T1195.001, T1574.007, T1059.006]
affected_products: ["Python (PyPI package ecosystem)"]
cves: []
sources:
  - url: "https://blog.talosintelligence.com/the-serpents-tongue-luring-the-python-out-of-its-den/"
    publisher: "Cisco Talos"
    date: "2026-07-14"
    role: primary
closed_sources: []
evidence:
  - quote: "executes automatically during installation or download, allowing for the execution of arbitrary code."
    publisher: "Cisco Talos"
  - quote: "they are executed with every invocation of Python, therefore exhibiting a persistent behavior on the victim endpoint."
    publisher: "Cisco Talos"
verification: single-source
sourcing_note: "Single-source technical survey from Cisco Talos (a high-reliability research lab); it is a taxonomy with proof-of-concept demonstrations rather than a new in-the-wild campaign, and it references TeamPCP's already-tracked litellm/lightning compromises as real-world examples."
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
actions: []
migrated_from: null
---

Cisco Talos published a comprehensive technical survey of code-execution paths across the Python packaging lifecycle — repository hosting (PyPI, version-control, custom servers), source (sdist) and wheel distribution formats, and installation into virtual or system-wide environments — split into two classes and assessed for persistence ([Cisco Talos, 2026-07-14](https://blog.talosintelligence.com/the-serpents-tongue-luring-the-python-out-of-its-den/)). Build-hook abuses fire code during installation: `setup.py` executes automatically on install or download, so a malicious command class runs arbitrary code as a transient one-shot. The more consequential class is persistence: a `.pth` path-configuration file dropped into `site-packages` is executed on every subsequent Python invocation, and site-hook modules (`sitecustomize.py`/`usercustomize.py`) and PYTHONPATH hijacking behave the same way — the payload survives well beyond install time. Talos ties the `.pth` technique directly to TeamPCP's supply-chain compromise of the `litellm` package and the import-time `__init__.py` payload to its `lightning` compromise, part of a documented run of TeamPCP supply-chain waves. The piece closes on defensive measures — dependency auditing (pip-audit), hashed lock files, install-time controls and a dependency-cooldown window before adopting newly-published versions.

**Defender takeaway:** for a SOC defending Python build and CI/CD estates, the actionable shift is treating installed-package persistence as a hunt target, not just install-time scanning — a malicious release that plants a `.pth` file or site-hook keeps executing on every interpreter start long after the install event scrolls out of logs. **Triage:** the discriminator is location and lineage — a legitimate `.pth` file points at directories, whereas a weaponised one carries an executable one-liner; in process telemetry, `python`/`pip` writing to `site-packages/*.pth` or spawning network connections during what should be an offline install, and unexpected child processes on `python -m <module>` invocations, separate malicious import/install-time execution from a normal build. Per policy no indicators or rule code are reproduced; the Talos post carries the detection detail.
