---
schema: 1
kind: incident
title: "Microsoft's agent-framework package on PyPI, versions 1.26.1 and 1.26.2 published on 2026-11-17, carried a credential stealer that a .pth startup hook runs every time Python starts, collecting environment secrets and requesting Azure managed-identity, Azure DevOps and GitHub Actions OIDC tokens; both versions were removed and 1.26.0 is the last clean release"
headline: "Microsoft's agent-framework on PyPI carried a Python-startup credential stealer in 1.26.1 and 1.26.2; pin 1.26.0"
summary: >
  Socket and SafeDep report that versions 1.26.1 and 1.26.2 of Microsoft's official agent-framework metapackage were published to PyPI on 2026-11-17, about 33 minutes apart, with a .pth file that runs a credential stealer whenever Python starts, so a pip install in a CI job is enough. It collects environment secrets and credential files and requests Azure managed-identity, Azure DevOps and, in 1.26.2, GitHub Actions OIDC tokens. Both versions were removed from PyPI and 1.26.0 is the last clean release; how the attacker obtained publishing access is not known.
discovered_at: "2026-11-18T05:11:30Z"
updated_at: null
event_date: "2026-11-17"
run_id: 2026-11-18T0356Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, infostealer, cloud]
regions: [global]
sectors: [technology]
entities: ["incident:microsoft-agent-framework-pypi-compromise-2026-11"]
techniques: [T1195.002, T1546.018, T1059.006, T1552.001, T1552.005, T1528, T1567]
affected_products: ["Microsoft Agent Framework"]
cves: []
sources:
  - url: "https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer"
    publisher: "Socket Research Team"
    date: "2026-11-17"
    role: primary
  - url: "https://safedep.io/blog/microsoft-agent-framework-pypi-compromise"
    publisher: "SafeDep"
    date: "2026-11-18"
    role: primary
closed_sources: []
evidence:
  - quote: "On Python startup, the `.pth` file imports a module that launches collection in a background process/thread."
    publisher: "Socket Research Team"
    source_url: "https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer"
  - quote: "The last clean release is 1.26.0."
    publisher: "SafeDep"
    source_url: "https://safedep.io/blog/microsoft-agent-framework-pypi-compromise"
  - quote: "How the attacker got publishing access is not known yet."
    publisher: "SafeDep"
    source_url: "https://safedep.io/blog/microsoft-agent-framework-pypi-compromise"
verification: multi-source
sourcing_note: >
  Socket and SafeDep detected the releases independently and agree on versions and behaviour; SafeDep dates its post 2026-11-18 and gives the publication times. No statement from Microsoft or PyPI was found; PyPI's own listing shows 1.26.0 as the newest version and neither bad release present.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Search lockfiles, requirements files and CI install logs for agent-framework 1.26.1 or 1.26.2 installed since 2026-11-17 20:35 UTC, and on every host or job that ran Python after installing either, treat the environment variables, local credential files, Azure managed-identity and Azure DevOps tokens and, for 1.26.2, GitHub Actions OIDC tokens as stolen and rotate them, then pin agent-framework to 1.26.0 or earlier."
updates: []
migrated_from: null
---

Socket reports that the Microsoft agent-framework PyPI package was compromised on 2026-11-17, in versions 1.26.1 and 1.26.2, both of which install Python startup hooks that collect credentials, environment data and cloud identity tokens and send them to a web endpoint ([Socket, 2026-11-17](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer)). SafeDep, which flagged both releases independently, says the project is Microsoft's official metapackage, published under the microsoft account on PyPI, that 1.26.1 appeared at 20:35 UTC and 1.26.2 at 21:08 UTC, that each is a single wheel where earlier releases shipped a wheel and a source archive, and that both were removed from PyPI and 1.26.0 is the last clean release ([SafeDep, 2026-11-18](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise)). The attacker published 1.26.2 after 1.26.1 was gone, so removing one version did not stop it, and how it obtained publishing access is not known ([SafeDep, 2026-11-18](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise)).

Nothing has to import the package: a .pth file runs on Python startup, imports a module and launches collection in a background process or thread, so a pip install in a CI job is enough ([Socket, 2026-11-17](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer); [SafeDep, 2026-11-18](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise)). 1.26.1 routes through the package's own initializer, while 1.26.2 moves the payload to a new top-level module and restores the legitimate initializer byte for byte, so checking only the initializer misses it ([Socket, 2026-11-17](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer)). The code matches environment variables by substring, such as TOKEN, SECRET, KEY and AZURE, reads other processes' environments and credential files for pip, npm, netrc, git, Docker, Hugging Face and Foundry, and actively requests fresh Azure managed-identity and Azure DevOps tokens, with GitHub Actions OIDC tokens added in 1.26.2; it compresses the result and posts it to a web endpoint and downloads no further code ([Socket, 2026-11-17](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer)). There is no persistent on-disk marker, so fresh process trees can trigger collection again ([Socket, 2026-11-17](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer)).

**Exposure:** any developer machine, CI job or container that installed agent-framework 1.26.1 or 1.26.2 and then ran Python; lockfiles and requirements files show the installed version, and the last clean release is 1.26.0 ([SafeDep, 2026-11-18](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise)).

**Detection:** lockfiles and requirements files naming the two versions, and a .pth file added to site-packages by the package, looked for on disk without starting the environment's Python, because starting it runs the stealer again ([SafeDep, 2026-11-18](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise)); outbound POSTs to a web-hook service from build and developer hosts; because the stealer requests identity tokens, review sign-in and activity logs for the managed identities and federated credentials the environment could use, from the install time onward ([SafeDep, 2026-11-18](https://safedep.io/blog/microsoft-agent-framework-pypi-compromise)).

**Defender takeaway:** remove both versions, rotate every secret and federated identity a host or job could read, and pin agent-framework to a known clean version; Socket advises rotating potentially exposed credentials where either version was installed ([Socket, 2026-11-17](https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer)).
