---
schema: 1
kind: research
title: "Sophos: \"Beagle\" backdoor distributed via fake Claude AI site using DonutLoader + DLL sideloading on a signed G DATA AV updater"
headline: "Sophos: \"Beagle\" backdoor distributed via fake Claude AI site using DonutLoader + DLL sideloading on a signed G DATA AV updater"
summary: "Sophos X-Ops (cluster STAC4713) published a write-up on 2026-05-07 of a malvertising campaign using the counterfeit claude-pro[.]com site to distribute a previously-undocumented Windows backdoor named Beagle (Sophos X-Ops, 2026-05-07 · Malwarebytes, 2026-04-10 (earlier wave))."
discovered_at: "2026-05-10T05:00:06Z"
event_date: 2026-05-07
run_id: 2026-05-10-001
priority: notable
immediate_action: null
tags:
  - phishing
  - infostealer
regions:
  - global
sectors:
  - technology
entities:
  - "tool:beagle-fake-claude-stac4713-2026"
cves: []
sources:
  - url: "https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor"
    publisher: "Sophos X-Ops, 2026-05-07"
    role: primary
  - url: "https://www.malwarebytes.com/blog/scams/2026/04/fake-claude-site-installs-malware-that-gives-attackers-access-to-your-computer"
    publisher: "Malwarebytes, 2026-04-10"
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
migrated_from: briefs/2026-05-10.md
---

Sophos X-Ops (cluster STAC4713) published a write-up on 2026-05-07 of a malvertising campaign using the counterfeit `claude-pro[.]com` site to distribute a previously-undocumented Windows backdoor named **Beagle** ([Sophos X-Ops, 2026-05-07](https://www.sophos.com/en-us/blog/donuts-and-beagles-fake-claude-site-spreads-backdoor) · [Malwarebytes, 2026-04-10 (earlier wave)](https://www.malwarebytes.com/blog/scams/2026/04/fake-claude-site-installs-malware-that-gives-attackers-access-to-your-computer)). The chain delivers a 505 MB ZIP archive containing a malicious MSI that sideloads an attacker-controlled DLL alongside a *legitimate, signed G DATA antivirus updater executable* ([T1574.002 DLL Side-Loading](https://attack.mitre.org/techniques/T1574/002/)). The first-stage [DonutLoader](https://attack.mitre.org/software/S1042/) shellcode then fetches and injects Beagle into memory. Beagle communicates with `license.claude-pro[.]com` over TCP/443 and UDP/8080 with AES-encrypted payloads; supported commands are `cmd`, `upload`, `download`, `ls`. Sophos notes TTP similarity with PlugX operators (BRONZE PRESIDENT / Dragon Breath clusters) but explicitly does not confirm attribution. The campaign's distribution infrastructure was established March 2026 with samples observed in February, April and May.

The targeting class is the operationally important part: counterfeit AI-tooling sites lure *technical users* — developers, ML engineers, IT admins — who often hold privileged access to source code, cloud environments, and secrets. Defenders should treat AI-tool installer downloads as a high-risk software class and require allow-listed sources (anthropic.com, claude.ai, OS package managers) rather than ad-hoc web search results.
