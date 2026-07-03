---
schema: 1
kind: research
horizon: strategic
weekly_section: weekly-research
title: "Research: the trust chain, not the perimeter, was the week's attack surface"
headline: "Research: the trust chain, not the perimeter, was the week's attack surface"
summary: "The week's research converges on the trust chain, not the perimeter — a \"Developer Credential Economy\" feeding npm worms into AI-coding-agent session hooks, OAuth-grant abuse, and a Browser-in-the-Middle PhaaS (Bluekit) that defeats Device Bound Session Credentials. (daily 06-28, Tenable)"
discovered_at: "2026-06-29T00:21:14Z"
event_date: null
run_id: 2026-W26-b78503e7
priority: high
immediate_action: null
tags:
  - supply-chain
  - identity
  - ai-abuse
  - cloud
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
entities:
  - "campaign:cordyceps-github-actions-pwn-request"
  - "campaign:bluekit-phaas-browser-in-the-middle"
cves: []
sources:
  - url: "https://www.tenable.com/blog/what-the-miasma-campaign-reveals-about-the-new-supply-chain-threat-model-and-the-underground"
    publisher: Tenable — Developer Credential Economy
    role: primary
  - url: "https://www.netcraft.com/blog/bluekit-phishing-as-a-service-threat"
    publisher: Netcraft — Bluekit BitM
    role: corroborating
  - url: "https://www.island.io/blog/badblocker-11-million-users-one-server-call-away-from-compromise"
    publisher: Island — BadBlocker
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
migrated_from: briefs/weekly/2026-W26.md
---

The week's research converges on one structural shift: the productive attack surface in 2026 is the set of trust relationships connecting developer tools, CI/CD pipelines, SaaS integrations, AI coding agents and the browser — not the network perimeter. Tenable's analysis of the Miasma worm frames it as a [**"Developer Credential Economy"**](https://www.tenable.com/blog/what-the-miasma-campaign-reveals-about-the-new-supply-chain-threat-model-and-the-underground): an infostealer harvests a developer credential (a Red Hat GitHub token sat in infostealer logs ~7 weeks before weaponisation), it is brokered underground, then weaponised through npm and — the novel capability — injected into the `SessionStart` hooks of AI coding tools so it runs when a developer opens a repo (Socket enumerates at least five affected tools — Claude Code, GitHub Copilot, Gemini CLI, Cursor, VS Code). The entire kill chain carries no CVE, and SLSA provenance attestations passed registry checks — provenance without content scanning is no defence ([Socket](https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem)).

The same trust-boundary theme runs through the week's other primary research: the Klue/Icarus cascade (a 2022 OAuth grant, § 2); Cordyceps, which found 300+ exploitable `pull_request_target` GitHub Actions misconfigurations leaking main-branch secrets ([Novee Security](https://novee.security/blog/cordyceps/)); Unit 42's malicious-skill payloads bypassing the OpenClaw agent sandbox ([Unit 42](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/)); and Island's "BadBlocker", an 11M-install Chrome ad-blocker one server-side config change away from arbitrary JavaScript on any site, with no extension update or store review ([Island](https://www.island.io/blog/badblocker-11-million-users-one-server-call-away-from-compromise)). On the identity plane, Netcraft documented Bluekit, a Browser-in-the-Middle phishing-as-a-service platform that authenticates the victim into the *attacker's* browser session, defeating Device Bound Session Credentials ([Netcraft](https://www.netcraft.com/blog/bluekit-phishing-as-a-service-threat)) — a reminder that session-binding controls like DBSC do not stop a browser-in-the-middle relaying the live authenticated session. Cisco Talos's [field guide to Windows COM abuse](https://blog.talosintelligence.com/introduction-to-com-usage-by-windows-threats/) (ITaskService, BITS, WMI, DCOM as EDR-evasion primitives) closes the loop on detection: indirect vtable calls hide activity behind legitimate service call stacks. The defender takeaway is uniform — audit OAuth grants and integration service accounts older than 12 months, restrict AI-agent hook configuration to read-only paths, treat CI/CD token scope as a reviewed principal, and don't assume FIDO2 closes the phishing path.
