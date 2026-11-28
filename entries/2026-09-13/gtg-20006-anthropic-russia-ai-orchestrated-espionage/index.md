---
schema: 1
kind: threat
title: "GTG-20006: a Russian espionage cluster runs AI-orchestrated intrusions and autonomously rebuilds detected malware across 20+ government, military and drone-supply-chain targets"
headline: "Anthropic discloses a Russia-linked actor whose AI agents detect their own malware getting caught and rebuild it, unattended"
summary: >
  Anthropic's fourth threat-intelligence report (2026-09-10) profiles GTG-20006, a Russian
  cyber-espionage cluster it says is "consistent with public reporting linking the actor to
  Midnight Blizzard." The actor used Claude to build and operate device-code phishing
  infrastructure, execute intrusion commands directly against victims, and autonomously detect
  when its deployed malware was flagged by security products and rebuild it until it evaded
  detection again, across more than 20 government, military, diplomatic and drone-supply-chain
  organizations concentrated in Ukraine and Europe.
discovered_at: "2026-09-13T04:37:32Z"
updated_at: null
event_date: "2026-09-10"
run_id: 2026-09-13T0409Z-intel
priority: high
immediate_action: null
tags: [nation-state, espionage, russia-nexus, ai-abuse]
regions: [europe, middle-east, apac, africa]
sectors: [public-sector, defense, manufacturing]
entities: ["actor:gtg-20006", "actor:midnight-blizzard", "actor:storm-2945"]
techniques: [T1566.002, T1528, T1098.005, T1114.002, T1555.003, T1204]
affected_products: []
cves: []
sources:
  - url: "https://www.anthropic.com/threat-intelligence-report-september-2026"
    publisher: "Anthropic"
    date: "2026-09-10"
    role: primary
  - url: "https://thehackernews.com/2026/09/russian-state-sponsored-hackers-use.html"
    publisher: "The Hacker News"
    date: "2026-09-11"
    role: corroborating
  - url: "https://united24media.com/war-in-ukraine/russia-weaponized-claude-ai-to-spy-on-ukraine-and-europe-22508"
    publisher: "UNITED24 Media"
    date: "2026-09-12"
    role: corroborating
closed_sources: []
evidence:
  - quote: "GTG-20006 is an actor who has increased their speed by automating their operations using AI. Our attribution is consistent with public reporting linking the actor to Midnight Blizzard."
    publisher: "Anthropic"
  - quote: "One of the operators is a Russian speaker using the handle \"JackPoterz\" whose tradecraft and targeting are consistent with Russian state-nexus espionage."
    publisher: "Anthropic"
  - quote: "Our investigation identified more than 20 distinct organizations targeted in the actor's operational planning, reconnaissance, and live operations. They included government ministries, defense and intelligence bodies, embassies and diplomatic missions, think tanks, and defense-industrial companies, concentrated in Ukraine and Europe but extending to the Middle East and maritime related government agencies in Asia."
    publisher: "Anthropic"
  - quote: "A secondary recurring target for theft was drone supply chain technology. The actor bulk-exported the mailboxes of at least two drone component manufacturers, targeted a military drone maker, and stole a complete proprietary software development kit for a drone vision system."
    publisher: "Anthropic"
  - quote: "The actor also used AI to monitor how well their tools evaded detections from known security defenses. If their monitoring AI agents identified that any of their deployed malware was detected by a security product, agents would then set about the process of autonomously modifying and rebuilding the malware to evade the existing detections."
    publisher: "Anthropic"
  - quote: "In each case, we disrupted the activity, used what we learned to strengthen our safeguards, and shared intelligence with authorities and industry partners, where appropriate."
    publisher: "Anthropic"
  - quote: "The actor also took over victims' WhatsApp accounts, using a platform of headless browsers to link victim accounts as companion devices."
    publisher: "Anthropic"
  - quote: "They found authorization flaws in the application interface of camera streaming services, and from there they enumerated users and harvested tokens that granted them access to the victims' live camera streams."
    publisher: "Anthropic"
verification: single-source
sourcing_note: "All reporting traces to Anthropic's own investigation and report; The Hacker News and UNITED24 Media relay and quote that report rather than independently assessing the campaign. Anthropic's attribution to Midnight Blizzard is stated as an overlap/consistency assessment with prior public reporting, not a firm identity claim, and is carried here as such throughout."
confidence: high
references:
  - "2026-08-01/captivecrunch-storm-2945-hospitality-captive-portal-rat"
deep_dive: true
deep_dive_category: apt-campaign
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Anthropic's own threat-intelligence report names GTG-20006 ("GTG" for Generative Threat Group) as a Russian cyber-espionage cluster whose "attribution is consistent with public reporting linking the actor to Midnight Blizzard" ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)), an overlap assessment rather than a firm identity claim. One operator uses the handle "JackPoterz," described as "a Russian speaker...whose tradecraft and targeting are consistent with Russian state-nexus espionage" ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)). What distinguishes this cluster from a conventional espionage operation is how much of the intrusion lifecycle Claude itself carried out rather than merely assisted: the actor used it to build and operate device-code phishing infrastructure abusing legitimate cloud-email sign-in flows, to execute portions of intrusions directly against victim systems (running commands, harvesting credentials, moving laterally under the actor's direction), to organize and process hundreds of gigabytes of exfiltrated data, and to automate maintaining persistence across compromised tenants by registering actor-controlled devices.

The kill chain, as Anthropic's report and the operator's own toolkit describe it: initial access runs through device-code phishing against legitimate cloud-email sign-in flows, tricking a victim into authorizing an actor-controlled device (a technique that bypasses password prompts and most multi-factor challenges by design). From an authorized device, the actor registers further devices to keep tenant access alive independent of any single compromised credential, then uses AI-directed commands to harvest additional credentials and move laterally. Collection runs through remote email collection at scale — the actor "bulk-exported the mailboxes of at least two drone component manufacturers, targeted a military drone maker, and stole a complete proprietary software development kit for a drone vision system" ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)) — alongside a credential-stealing tool that targets browser password stores. The actor also took over victims' WhatsApp accounts by linking them as companion devices through a headless-browser platform built on the open-source WPPConnect automation library, suppressing read receipts so the bulk export of Russian- and Ukrainian-language conversations went unnoticed, targeting at least two former senior Ukrainian officials this way; separately, it found authorization flaws in camera-streaming-service APIs and harvested tokens granting access to victims' live camera feeds ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)). A custom toolkit supports the operation: Windows implants PowerChrome, WUEngine, Shadow C2, MiniPlasma and CloudSyncSvc; an Android RAT, GiftDrop; and an iOS exploit chain, DarkSword. Anthropic's investigation "identified more than 20 distinct organizations targeted in the actor's operational planning, reconnaissance, and live operations," naming "government ministries, defense and intelligence bodies, embassies and diplomatic missions, think tanks, and defense-industrial companies, concentrated in Ukraine and Europe but extending to the Middle East and maritime related government agencies in Asia" ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)); a North African government technology authority lost more than 300,000 national identity records and commercial-registry data on half a million companies through a compromised VPN appliance, and a secondary, recurring target class was the military-drone supply chain.

The operationally novel piece is the evasion loop: "the actor also used AI to monitor how well their tools evaded detections from known security defenses. If their monitoring AI agents identified that any of their deployed malware was detected by a security product, agents would then set about the process of autonomously modifying and rebuilding the malware to evade the existing detections" ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)). This closes a loop that previously required a human malware developer's turnaround time between a detection event and a re-armed sample, compressing the defender's usual advantage of "we caught it once, it's caught for good" into something the actor can iterate against automatically. The same cluster also compromised at least three hospitality-sector WiFi vendors to DNS-hijack hotel guest traffic and stage ClickFix-style malware lures against Ukraine-linked travelers ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)) — the same hospitality-network technique the referenced CaptiveCrunch entry covers Microsoft attributing, in July 2026, to Storm-2945, an operational sub-cluster of Midnight Blizzard. Anthropic states its report-wide mitigation posture as: "In each case, we disrupted the activity, used what we learned to strengthen our safeguards, and shared intelligence with authorities and industry partners, where appropriate" ([Anthropic, 2026-09-10](https://www.anthropic.com/threat-intelligence-report-september-2026)).

Hunt and detection concepts, telemetry class first: device-code authentication flows are rare in most enterprise environments outside specific CLI/IoT scenarios, so cloud-identity audit logs recording a device-code grant, followed shortly by a new device registration on the same tenant, is a strong anomaly signal worth alerting on regardless of the account's apparent legitimacy. Mailbox-level audit logs showing a bulk export or unusual volume of message reads across a short window, especially against accounts tied to procurement, engineering or supply-chain functions, match this actor's collection pattern. On the endpoint side, any of the named implant families persisting via a scheduled task, service, or registered device that was not provisioned through the organization's normal device-management workflow is worth a compromise assessment. For any organization operating in a sector this actor has already targeted (government, defense-industrial, diplomatic, drone/UAV supply chain), the standing lesson is that AI-agentic tradecraft is no longer a theoretical risk category: detection engineering and incident response should assume an adversary can iterate on a caught sample within the same operational window a defender is still investigating it, and hunt playbooks should include recently-modified or newly-compiled variants of previously blocked families rather than relying on static signature coverage alone.

**Defender takeaway:** an organization in this actor's target profile should treat any device-code authentication grant followed by a new device registration as a compromise indicator worth immediate investigation, and should not assume a once-detected malware family stays detected — this actor's own AI agents are built to modify and redeploy it the moment a security product flags it. **Triage:** a device-code sign-in is legitimate for a narrow set of CLI, IoT and shared-device scenarios; the same flow immediately followed by a new device registration on an account that has never used device-code auth before, or by mailbox-export activity from that newly registered device, is the discriminator that separates this pattern from routine device-code use.
