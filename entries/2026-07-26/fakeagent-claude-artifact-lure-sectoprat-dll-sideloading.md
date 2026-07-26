---
schema: 1
kind: threat
horizon: operational
title: "FakeAgent — malvertising hosts a fake AI-desktop-app download page on the vendor's own trusted domain, delivering SectopRAT by DLL side-loading"
headline: "A search ad pointed at a legitimate vendor domain: the lure page was a user-created artifact on the platform itself"
summary: >
  Huntress documents a malvertising campaign it names FakeAgent that compromised at least 29
  organisations between 2026-07-21 and 2026-07-22. Search ads for the Claude Desktop app pointed
  at a genuine claude.ai URL, but the destination was a public user-created artifact hosted on
  the platform that imitated the official download page — so the ad, the domain and the TLS
  certificate all looked legitimate. The fake installer reaches execution by side-loading a
  trojanised DLL under a signed third-party binary and delivers SectopRAT, with a second
  persistence chain abusing another signed vendor executable and decrypting its payload through
  a compiled DirectX shader.
discovered_at: "2026-07-26T14:02:00Z"
event_date: "2026-07-22"
run_id: 2026-07-26T1308Z-audit
priority: notable
immediate_action: null
tags: [phishing, infostealer, ai-abuse, organized-crime]
regions: [global]
sectors: [technology]
entities: []
techniques: [T1583.008, T1204.001, T1574.001, T1027.002, T1102.002]
affected_products: []
cves: []
sources:
  - url: "https://www.huntress.com/blog/fakeagent-claude-desktop-malvertising-ends-in-dotnet-rat"
    publisher: "Huntress"
    date: "2026-07-22"
    role: primary
  - url: "https://www.helpnetsecurity.com/2026/07/23/anthropic-claude-artifacts-download-malware/"
    publisher: "Help Net Security"
    date: "2026-07-23"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/fake-claude-app-promoted-by-bing-ads-pushes-sectoprat-malware/"
    publisher: "BleepingComputer"
    date: "2026-07-23"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Between July 21 and July 22, at least 29 organizations fell victim to a malvertising campaign"
    publisher: "Huntress"
  - quote: "By maliciously modifying that function in the DLL, an adversary can achieve execution in the context of a trusted and signed executable"
    publisher: "Huntress"
  - quote: "The malware's decryption routine isn't a typical CPU-based decryption routine: instead, it is a compiled DirectX shader"
    publisher: "Huntress"
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

The interesting part of this campaign is not the payload but the hosting. Huntress reports that between 2026-07-21 and 2026-07-22 "at least 29 organizations fell victim to a malvertising campaign" in which users searching for the Claude Desktop application were served a sponsored result whose link genuinely resolved to `claude.ai` — the vendor's own domain ([Huntress, 2026-07-22](https://www.huntress.com/blog/fakeagent-claude-desktop-malvertising-ends-in-dotnet-rat)). The destination was a public, user-created artifact on the platform, built to imitate the official download page and viewed some 7,100 times before it was removed ([Help Net Security, 2026-07-23](https://www.helpnetsecurity.com/2026/07/23/anthropic-claude-artifacts-download-malware/)). Every control that keys on domain reputation — ad-network vetting, corporate URL allowlists, certificate inspection, the user's own glance at the address bar — reported a trustworthy destination, because the destination genuinely was the vendor's site. Only the onward redirect to attacker infrastructure serving the installer left the trusted domain.

Execution follows a signed-binary side-loading pattern rather than running unsigned attacker code directly. The fake installer drops a repurposed JetBrains Chromium Embedded Framework helper alongside a trojanised `libcef.dll` packed with VMProtect; as Huntress puts it, "By maliciously modifying that function in the DLL, an adversary can achieve execution in the context of a trusted and signed executable" ([Huntress, 2026-07-22](https://www.huntress.com/blog/fakeagent-claude-desktop-malvertising-ends-in-dotnet-rat)). A second persistence chain repeats the trick with an IBM SPSS binary side-loading `tempdir.dll`, adding GPU-based anti-analysis checks and an unusual unpacking step — "The malware's decryption routine isn't a typical CPU-based decryption routine: instead, it is a compiled DirectX shader", which moves the decryption work off the CPU paths that sandboxes and emulators instrument. The delivered payload is SectopRAT, an information stealer and remote-access tool with hands-on-keyboard capability ([BleepingComputer, 2026-07-23](https://www.bleepingcomputer.com/news/security/fake-claude-app-promoted-by-bing-ads-pushes-sectoprat-malware/)); Huntress is the source for what it reaches for and how it is controlled — plaintext strings referencing browser logins, cookies, autofills and credit cards, and command-and-control data stored in the Ethereum blockchain, the takedown-resistant technique known as EtherHiding ([Huntress, 2026-07-22](https://www.huntress.com/blog/fakeagent-claude-desktop-malvertising-ends-in-dotnet-rat)).

**Defender takeaway:** the constituency-relevant lesson is that user-generated-content features on trusted SaaS platforms are now a lure-hosting surface, and domain allowlisting does not distinguish a vendor's product pages from arbitrary user content served under the same hostname. Where an allowlist grants a whole AI or collaboration domain, the practical mitigations are to source desktop-client installers from a managed software catalogue rather than search results, and to treat executable downloads that originate from a shared-content path on a SaaS domain as a distinct case from downloads from that vendor's release infrastructure.

**Triage:** DLL side-loading under signed third-party binaries produces telemetry that looks legitimate at the process level — the signed JetBrains or IBM SPSS executable is genuinely signed, and its presence on a developer or analyst workstation can be entirely normal. The discriminators are location and lineage: the signed helper running from a user-writable download or temporary directory rather than its installed application tree, loading a module of the expected name from that same directory, with no parent installation of the product it belongs to. A browser or installer process as the immediate ancestor, followed by reads of browser credential stores by that process tree, is the sequence worth alerting on; the signed binary alone is not.
