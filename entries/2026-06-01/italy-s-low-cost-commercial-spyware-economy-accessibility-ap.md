---
schema: 1
kind: threat
horizon: operational
title: "Italy's low-cost commercial spyware economy: Accessibility-API abuse as the cheap alternative to zero-days"
headline: "Italy's low-cost commercial spyware economy: Accessibility-API abuse as the cheap alternative to zero-days"
summary: "Deep dive: Italy's low-cost commercial spyware economy — Morpheus (IPS Intelligence) abuses the Android Accessibility API, overlay permissions and ADB to self-grant rights and kill mobile AV, no zero-day required; sibling tool Spyrtacus (SIO) leans on DexGuard obfuscation. EU law-enforcement is the named customer base (EDRi, 2026-05-28)."
discovered_at: "2026-06-01T05:00:03Z"
event_date: 2026-05-28
run_id: 2026-06-01-7f55e064
priority: high
immediate_action: null
tags:
  - espionage
  - mobile
  - eu-nexus
regions:
  - europe
sectors:
  - public-sector
  - media
entities:
  - "campaign:italy-low-cost-commercial-spyware-morpheus-spyrtacus"
cves: []
sources:
  - url: "https://edri.org/our-work/inside-italys-low-cost-spyware-economy/"
    publisher: "EDRi — Inside Italy's low-cost spyware economy"
    role: primary
  - url: "https://osservatorionessuno.org/blog/2026/04/morpheus-a-new-spyware-linked-to-ips-intelligence/"
    publisher: Osservatorio Nessuno — Morpheus technical analysis
    role: corroborating
  - url: "https://osservatorionessuno.org/blog/2026/04/italian-spyware-maker-sio-still-developing-and-distributing-spyrtacus/"
    publisher: Osservatorio Nessuno — Spyrtacus / SIO analysis
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: mobile
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-01.md
---

**Background.** The commercial-spyware conversation in Europe has been dominated by high-tier zero-click vendors — NSO Group's Pegasus and, in Italy specifically, Paragon Solutions' Graphite, whose contract with Italian intelligence agencies was terminated after public disclosure earlier in the Paragon scandal. European Digital Rights (EDRi) and the Italian NGO Osservatorio Nessuno have now documented the layer beneath that headline market: a domestic, low-cost Android-trojan industry that achieves persistent surveillance without any exploit at all ([EDRi, 2026-05-28](https://edri.org/our-work/inside-italys-low-cost-spyware-economy/)). The technical analyses of the two named tools — Morpheus and Spyrtacus — were published by Osservatorio Nessuno in April 2026 and resurfaced in late-May 2026 regional reporting; this deep dive is built on those primary investigations.

**The two tools and who builds them.** Morpheus (version `2025.3.0` analysed) is linked to IPS Intelligence (IPS Public Security S.p.A.) ([Osservatorio Nessuno — Morpheus, 2026-04-23](https://osservatorionessuno.org/blog/2026/04/morpheus-a-new-spyware-linked-to-ips-intelligence/)); Spyrtacus is actively developed by SIO S.p.A. and, per Osservatorio Nessuno's separate analysis, relies on DexGuard obfuscation and an `InMemoryDexClassLoader` loading stage rather than Morpheus's Accessibility-driven approach ([Osservatorio Nessuno — Spyrtacus, 2026-04-09](https://osservatorionessuno.org/blog/2026/04/italian-spyware-maker-sio-still-developing-and-distributing-spyrtacus/)). Both are Android implants delivered by social engineering — fake carrier-update SMS or impersonated apps requiring only a user-initiated install — rather than by a zero-day, which is precisely why they are cheap and why they evade the assumption that "no exploit, no compromise."

**Mechanics — privilege without a vulnerability.** The infection chain is an abuse chain, not an exploit chain. Morpheus uses a two-stage model that leans on three legitimate Android subsystems: the Accessibility Services API, overlay permissions (`SYSTEM_ALERT_WINDOW`), and Android Debug Bridge (ADB). Once a user grants Accessibility — the single consent the whole chain hinges on — the implant programmatically self-grants further dangerous permissions and drives the UI, an elevation-by-design pattern mapped to [`T1626 Abuse Elevation Control Mechanism`](https://attack.mitre.org/techniques/T1626/) and [`T1516 Input Injection`](https://attack.mitre.org/techniques/T1516/). Concretely, Morpheus spoofs a biometric-prompt overlay on top of WhatsApp's account-linking screen to pair an attacker device (capturing the linked session), records audio and video, and — notably for hunt teams — disables the camera and microphone privacy indicators by issuing `device_config` settings via ADB, and actively terminates installed mobile-AV products (Bitdefender, Sophos, Avast, AVG, Malwarebytes) to protect itself ([Osservatorio Nessuno — Morpheus, 2026-04-23](https://osservatorionessuno.org/blog/2026/04/morpheus-a-new-spyware-linked-to-ips-intelligence/)). The AV-killing and indicator-suppression are the behaviours most amenable to detection, because they are loud relative to the otherwise-quiet permission abuse.

**Scale and the oversight gap — why this is a public-sector story.** EDRi reports that Italian prosecutors authorised roughly 5,200 trojan-based interceptions in 2024 alone — a volume far exceeding any other EU member state — at a per-day cost of a few euros, with no centralised oversight: authorisation is local to individual judges, and targets cannot determine which vendor's tool was used or whether authorisation was proper, while EU internal-market rules let these vendors operate across member states with little friction ([EDRi, 2026-05-28](https://edri.org/our-work/inside-italys-low-cost-spyware-economy/)). EDRi calls for an EU-wide ban on the commercial-spyware trade backed by binding transparency obligations ([EDRi, 2026-05-28](https://edri.org/our-work/inside-italys-low-cost-spyware-economy/)). For a Swiss/EU public-sector SOC the relevance is twofold: officials, journalists and civil-society contacts are within the documented target class, and the delivery method works against any managed Android fleet because side-loaded APKs (delivered via carrier cooperation or direct messaging) bypass the Play-Store-sourcing assumption that Play Protect enforces.

**Detection and hardening for managed Android fleets (no IOCs).** The defensible controls are MDM- and MTD-centric, anchored on the consent the implant cannot avoid asking for:
- Alert on any **Accessibility Service grant to an APK not on the approved-app list** and quarantine the device — this is the chokepoint of the whole chain.
- Treat **termination of a registered Mobile Threat Defence / mobile-AV agent within ~30 s of a new APK install** as a high-confidence indicator (Morpheus's AV-killing).
- Alert on **`SYSTEM_ALERT_WINDOW` overlay activity from a non-Play-sourced APK**, especially overlays on messaging apps (the WhatsApp biometric-prompt spoof).
- **Disable ADB over network** (`adb tcpip`) via MDM policy, and enforce **Android Enterprise Fully Managed Device** mode so users cannot side-load APKs at all; keep Play Protect enabled and non-killable (Google's March 2026 Play Protect update restricts Accessibility abuse for side-loaded apps).
- On the regulatory side, Swiss agencies procuring interception tooling should note the Swiss FADP/`Datenschutzgesetz` and `Informationssicherheitsgesetz` exposure the Italian oversight failure illustrates.

The strategic point for defenders: the cheap end of the commercial-spyware market has industrialised *permission abuse* as a substitute for exploit development, which moves the detection burden off "patch the zero-day" and onto "govern Accessibility/overlay/ADB consent on the fleet" — a control surface most Android MDM deployments do not yet alert on.
