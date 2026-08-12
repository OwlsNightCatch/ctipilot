---
schema: 1
kind: threat
horizon: operational
title: "UPDATE — the N-central exploitation has an actor and a payload: Microsoft assesses Storm-1175 is behind it, deploying a new ransomware strain called StormEncryptor from the day the flaw was disclosed"
headline: "The RMM auth-bypass chain tracked here since 3 August is now attributed to a China-linked ransomware actor with a new encryptor"
summary: >
  Microsoft Threat Intelligence reported over the weekend of 2026-08-08/09 that Storm-1175 — a
  financially motivated, China-linked actor previously known for high-velocity Medusa ransomware
  campaigns — began deploying a previously undocumented strain, StormEncryptor, on 2 August, and is
  likely exploiting CVE-2026-18577 in N-able N-central to do it. Microsoft has not formally confirmed
  the access vector; what it notes is that the deployments began the same day the flaw was disclosed.
  Huntress found more than half of reachable cloud-hosted N-central servers across its partner base
  still unpatched, and 28.6% of self-hosted instances.
discovered_at: "2026-08-12T04:48:00Z"
event_date: "2026-08-10"
run_id: 2026-08-12T0411Z-intel
priority: high
immediate_action: null
tags: [ransomware, supply-chain, actively-exploited, auth-bypass, cisa-kev, organized-crime]
regions: [global, europe]
sectors: [technology, public-sector, healthcare, finance]
nexus: [china-nexus]
entities:
  - actor:storm-1175
  - malware:stormencryptor
techniques: [T1190, T1219, T1486, T1072]
affected_products: ["N-able N-central"]
cves:
  - id: CVE-2026-18577
    cvss: null
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, patch-available]
    affected: "N-able N-central self-hosted instances below the Hotfix 2 build; see the vendor's own advisories for the per-build detail already covered in the prior entries"
    fixed: "N-central 2026.3 Hotfix 2 (build 2026.3.1.10)"
sources:
  - url: "https://therecord.media/china-hackers-ransomware-microsoft"
    publisher: "The Record (Recorded Future News)"
    date: "2026-08-10"
    role: primary
  - url: "https://www.microsoft.com/en-us/security/blog/2026/04/06/storm-1175-focuses-gaze-on-vulnerable-web-facing-assets-in-high-tempo-medusa-ransomware-operations/"
    publisher: "Microsoft Threat Intelligence"
    date: "2026-04-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "the Storm-1175 group began deploying a new ransomware strain on August 2 called StormEncryptor"
    publisher: "The Record (Recorded Future News)"
  - quote: "Microsoft has not formally confirmed the access vector, but noted that StormEncryptor deployments began the same day the flaw was disclosed."
    publisher: "The Record (Recorded Future News)"
verification: single-source
sourcing_note: >
  Microsoft Threat Intelligence is the originating assessor for the load-bearing claim — Storm-1175
  deploying StormEncryptor, likely via CVE-2026-18577 — and this entry is composed from The Record's
  reporting of it because no Microsoft publication on that activity was reachable in this run. Other
  outlets carried the same Microsoft assessment on the same day, which makes them additional
  publishers of one assessment rather than independent corroboration — hence single-source. Microsoft's
  own April 2026 profile is cited only for the actor's prior tradecraft and tempo, which it states
  first-hand; the China attribution is The Record's and is not made in that profile. The primary reporting is dated 2026-08-10, just outside this run's 26 h window; it is
  carried under the developing-story allowance as an update to an incident this pipeline has tracked
  since 2026-08-03 and which the vendor states is still active.
confidence: medium
update_of: 2026-08-09/n-able-n-central-hotfix-2-required-supersedes-hotfix-1
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

**UPDATE (originally covered 2026-08-03, most recently 2026-08-09):** the N-able N-central authentication-bypass chain this pipeline has tracked through two hotfixes now has an assessed actor and a named payload. Microsoft Threat Intelligence reported that "the Storm-1175 group began deploying a new ransomware strain on August 2 called StormEncryptor", and that the group is likely exploiting CVE-2026-18577 in N-central to obtain access ([The Record, 2026-08-10](https://therecord.media/china-hackers-ransomware-microsoft)). The hedge is Microsoft's own and matters: "Microsoft has not formally confirmed the access vector, but noted that StormEncryptor deployments began the same day the flaw was disclosed" ([The Record, 2026-08-10](https://therecord.media/china-hackers-ransomware-microsoft)). The same-day correlation is the evidence; a confirmed vector is not yet on the record.

The Record describes the actor as financially motivated and linked to China, and its prior activity is why the attribution changes a defender's calculus rather than just labelling it ([The Record, 2026-08-10](https://therecord.media/china-hackers-ransomware-microsoft)). Microsoft's own April 2026 profile of the group — which does not itself make a China attribution — describes high-tempo Medusa ransomware operations against vulnerable web-facing assets, and records the group moving from initial access to data exfiltration and ransomware deployment often within a few days and in some cases within 24 hours ([Microsoft Threat Intelligence, 2026-04-06](https://www.microsoft.com/en-us/security/blog/2026/04/06/storm-1175-focuses-gaze-on-vulnerable-web-facing-assets-in-high-tempo-medusa-ransomware-operations/)). Its earlier Medusa victims were healthcare, professional services and finance organisations in Australia, Britain and the United States; StormEncryptor is the departure from that tooling ([The Record, 2026-08-10](https://therecord.media/china-hackers-ransomware-microsoft)). Note what those sectors and countries describe: the group's *previous* victim set, not confirmed victims of this campaign, for which no count has been disclosed.

Two facts sharpen the exposure picture for anyone whose managed service provider runs N-central. N-able states it detected the original flaw in a zero-day attack on 31 July, though it is unclear whether the actor behind that first intrusion was Storm-1175 — the initial patch was bypassed, forcing an emergency hotfix on 2 August and a second on 6 August with the warning that the first was not enough. And the patch gap is wide: after the fixes were available, Huntress found more than half of reachable N-central cloud servers across its partner base still unpatched, with 28.6% of self-hosted instances exposed ([The Record, 2026-08-10](https://therecord.media/china-hackers-ransomware-microsoft)). Huntress went as far as suggesting that anyone running N-central in a higher-risk environment where exposure cannot meaningfully be reduced may need to consider turning the tool off, while cautioning that doing so costs central visibility, patching and remote access when they may be needed most.

The structural point is the one this constituency should carry: a single compromised RMM server is a gateway to every endpoint it manages, so one breach at one provider cascades across its whole client base. The Record draws the direct comparison to the 2021 Kaseya intrusion, where REvil compromised around 60 direct customers and subsequently hit roughly 1,500 downstream businesses, and to the 2024 ScreenConnect attacks — in which Microsoft says Storm-1175 was among the actors targeting the product ([The Record, 2026-08-10](https://therecord.media/china-hackers-ransomware-microsoft)).

**Defender takeaway:** for a public-sector body that outsources endpoint management, the exposure is the provider's patch state, not its own — the question to put to the MSP is which N-central build it is running and when Hotfix 2 was applied, because the answer determines whether the estate's endpoints were reachable from a server an unauthenticated attacker could take. No new action ships with this update: the remediation is unchanged from the 2026-08-09 entry (Hotfix 2, build 2026.3.1.10, plus a compromise assessment rather than an upgrade alone), and this delta changes who was doing it and what they dropped, not what to do about it.
