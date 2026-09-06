---
schema: 1
kind: research
title: "Amazon attributes the axios, debug and chalk npm compromises to a DPRK-linked cluster with medium confidence, and names a small 2025 package compromise as the rehearsal"
headline: "Amazon Threat Intelligence traces three major npm compromises to one DPRK-linked actor, and describes a payload that only detonates on a specific input"
summary: >
  Amazon's threat-intelligence team published an assessment on 2026-07-29 attributing the September 2025
  compromises of the npm packages debug and chalk and the March 2026 compromise of axios — a library Amazon
  puts at more than 100 million weekly downloads — to a DPRK-linked cluster tracked as SAPPHIRE SLEET,
  STARDUST CHOLLIMA, BlueNoroff, CageyChameleon and Alluring Pisces, explicitly at medium confidence rather
  than as an established fact. In every case maintainer access came from socially engineering a trusted
  maintainer rather than from a platform flaw. Amazon assesses that a small March 2025 compromise of a
  package named typo-crypto was a testing ground for these later operations, and that payload only executed
  when handed one specific input value — a conditional-detonation design that defeats analysis which merely installs and
  observes a package.
discovered_at: "2026-07-30T05:00:00Z"
event_date: "2026-07-29"
run_id: 2026-07-30T0409Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, nation-state, north-korea-nexus, infostealer]
regions: [global]
sectors: [public-sector, finance, technology]
entities: [actor:sapphire-sleet]
techniques: [T1195.002, T1199, T1027, T1105]
affected_products: []
cves: []
sources:
  - url: "https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/"
    publisher: "AWS Security Blog"
    date: "2026-07-29"
    role: primary
  - url: "https://cyberscoop.com/amazon-north-korea-open-source-software-attacks/"
    publisher: "CyberScoop"
    date: "2026-07-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Based on analysis of command-and-control (C2) indicators and TTPs, Amazon Threat Intelligence assesses with medium confidence that these campaigns are attributable to the DPRK-linked threat actor tracked as SAPPHIRE SLEET, STARDUST CHOLLIMA, BlueNoroff, CageyChameleon, and Alluring Pisces."
    publisher: "AWS Security Blog"
  - quote: "In each case, the threat actor gained access by socially engineering a trusted maintainer of the package, then published a software update containing malicious code."
    publisher: "AWS Security Blog"
  - quote: "Based on the limited number of observed downloads, Amazon Threat Intelligence assesses that this campaign was small scale and likely served as a testing ground for the more visible supply chain operations that followed in late 2025 and 2026."
    publisher: "AWS Security Blog"
  - quote: "This approach is designed to defeat scanners that evaluate packages one by one instead of reasoning about how they interact in a real dependency graph."
    publisher: "AWS Security Blog"
  - quote: "When triggered, it downloads a second-stage payload from a hardcoded C2 server, then executes the payload based on the victim's operating system, with behavior tailored for Windows, macOS, or Linux."
    publisher: "AWS Security Blog"
verification: multi-source
sourcing_note: >
  The attribution is Amazon Threat Intelligence's own medium-confidence assessment and is reported here as
  that assessment rather than as established authorship. Amazon states the axios compromise had already been
  publicly attributed to this actor and that the newly-drawn links are to typo-crypto, debug and chalk, so
  the novelty claim here is scoped to those three rather than to the cluster as a whole. CyberScoop's coverage comes from an Amazon media roundtable rather than independent analysis,
  and supplies the additional alias UNC1069 used by researchers generally, which is why that alias is
  sourced to CyberScoop and not to Amazon's own post. Amazon's post gives no affected or fixed version
  numbers for axios, debug or chalk — only compromise timing — so none are stated here; an operator needing
  version precision must go to each package's own advisory. Amazon issues no explicit dependency-audit
  recommendation, so the defensive implication drawn below is attributed to its description of the
  tradecraft rather than presented as its guidance.
confidence: medium
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

Amazon's threat-intelligence team published an attribution assessment on 2026-07-29 linking three separate npm package compromises to one actor. The load-bearing sentence carries its own hedge, and it should be read with the hedge intact: "based on analysis of command-and-control (C2) indicators and TTPs, Amazon Threat Intelligence assesses with medium confidence that these campaigns are attributable to the DPRK-linked threat actor tracked as SAPPHIRE SLEET, STARDUST CHOLLIMA, BlueNoroff, CageyChameleon, and Alluring Pisces" ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)). CyberScoop notes that researchers also track this cluster as UNC1069 ([CyberScoop, 2026-07-29](https://cyberscoop.com/amazon-north-korea-open-source-software-attacks/)). Medium confidence is not attribution-by-consensus. Amazon is also precise about which part is new: it states that "while the axios compromise has been publicly attributed to this DPRK-linked threat actor, the typo-crypto, debug, and chalk incidents haven't previously been connected to it" ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)). For a defender the actor label changes little, but the tradecraft description below changes something real.

The compromises run from March 2025 to March 2026 and escalate in blast radius: debug and chalk in September 2025, then axios in March 2026, which Amazon describes as one of the most widely used JavaScript libraries at more than 100 million weekly downloads ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)). None of them involved breaking the registry. In Amazon's words, "in each case, the threat actor gained access by socially engineering a trusted maintainer of the package, then published a software update containing malicious code" ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)) — the trust chain held exactly as designed and delivered the malicious version, which is why provenance and signing controls do not help here.

The genuinely new element is the rehearsal. Amazon points at a March 2025 compromise of a package named typo-crypto, into which the actor committed a trojanised file that masqueraded as the unrelated legitimate core-js package, and assesses that "based on the limited number of observed downloads... this campaign was small scale and likely served as a testing ground for the more visible supply chain operations that followed in late 2025 and 2026" ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)). That is a patience pattern worth internalising: a package with negligible download counts is not necessarily a failed attack, it may be where the maintainer-social-engineering approach and the payload were refined before being pointed at something with a hundred million weekly installs.

Two mechanics from that rehearsal payload matter for anyone who triages suspicious dependencies. First, detonation was conditional on input rather than on time or environment: the trojanised file executed only when it received a hash input beginning with one specific literal value, and only then downloaded an operating-system-appropriate second stage, with behaviour tailored separately for Windows, macOS and Linux ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)). A package like that installs and runs cleanly in any sandbox that does not happen to feed it the trigger value, so "we installed it and nothing happened" is not a clean result. Second, the payload combined file-based persistence with payload rotation and layered obfuscation — base64-encoded text over an XOR cipher under a fixed key ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)) — so a static scan of the shipped file yields little without unwrapping those layers.

Amazon separately describes a shift in how these operations are structured, observing that attackers increasingly split one malicious workflow across several individually unremarkable packages, and that "this approach is designed to defeat scanners that evaluate packages one by one instead of reasoning about how they interact in a real dependency graph" ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)). Amazon frames that as an observation rather than advice, but the implication for a review process is direct: a per-package verdict is the wrong unit of analysis when the malicious behaviour only exists once the pieces are resolved together.

**Defender takeaway:** the actor label is the least useful part of this report. What carries over is that a dependency compromise can arrive through a legitimate maintainer and a legitimate release, sit dormant unless given a specific input, and distribute its logic across packages that each look fine alone — so dynamic analysis that observes an install without exercising the code, and review that scores packages individually, are both weaker than their output suggests.

**Triage:** a benign minified or bundled dependency also carries base64 blobs and unreadable code, so obfuscation alone does not separate the two. The discriminators are behavioural and structural: a code path that stays inert unless a caller supplies a particular argument value, a second-stage fetch whose destination differs by host operating system, and persistence written outside the package's own installation tree. A dependency that reaches the network at all during a build or test run, when its documented function does not require it, is the anomaly worth pulling.
