---
schema: 1
kind: synthesis
horizon: strategic
weekly_section: weekly-long-running
title: "Open-source supply-chain wave status: a second vendor assesses the escalation at high confidence, the CI trigger that hands over base-repository secrets is named, and two vendors independently attribute the axios compromise to the same DPRK cluster"
headline: "Supply-chain status — cross-vendor DPRK attribution on axios, and pull_request_target named as the CI lever"
summary: >
  Status update on the npm and developer-ecosystem supply-chain wave prior weeklies tracked from install-hook
  evasion through CI/CD trust abuse to poisoned AI-assistant tool configurations. Two developments this week.
  Amazon attributed the September 2025 debug and chalk compromises and the March 2026 axios compromise to a
  DPRK-linked cluster at medium confidence, finding maintainer access came from social engineering rather than
  a platform flaw in every case, and assessing a small March 2025 package compromise as a testing ground for
  what followed. Google's threat-intelligence group independently credits the same actor with the axios
  compromise under its own tracking name, and names the specific CI mechanism another cluster abused: the
  pull_request_target GitHub Actions trigger, used to obtain base-repository secrets and write permissions.
  The transferable levers are concrete — audit that trigger, and impose a release-age cooldown on installs.
discovered_at: "2026-08-02T23:59:00Z"
event_date: "2026-07-30"
run_id: 2026-08-02T2311Z-weekly
priority: notable
immediate_action: null
tags: [supply-chain, nation-state, organized-crime, north-korea-nexus]
regions: [global, europe]
sectors: [technology, public-sector, finance]
entities:
  - actor:sapphire-sleet
  - actor:teampcp
  - campaign:contagious-interview
  - malware:sandworm-mode
techniques: [T1195.002, T1195.001, T1199, T1027, T1105]
affected_products: ["axios (npm)", "GitHub Actions", "npm", "PyPI", "Docker Hub"]
cves: []
sources:
  - url: "https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/"
    publisher: "AWS Security Blog"
    date: "2026-07-29"
    role: primary
  - url: "https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/"
    publisher: "Google Cloud Blog (GTIG)"
    date: "2026-07-30"
    role: primary
  - url: "https://cyberscoop.com/amazon-north-korea-open-source-software-attacks/"
    publisher: "CyberScoop"
    date: "2026-07-29"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Based on analysis of command-and-control (C2) indicators and TTPs, Amazon Threat Intelligence assesses with medium confidence that these campaigns are attributable to the DPRK-linked threat actor tracked as SAPPHIRE SLEET"
    publisher: "AWS Security Blog"
  - quote: "In each case, the threat actor gained access by socially engineering a trusted maintainer of the package, then published a software update containing malicious code."
    publisher: "AWS Security Blog"
  - quote: "This approach is designed to defeat scanners that evaluate packages one by one instead of reasoning about how they interact in a real dependency graph."
    publisher: "AWS Security Blog"
  - quote: "GTIG assesses with high confidence that the growth in very large-scale, open-source supply chain compromise campaigns, including use of worms and iterative compromises in 2025 and early 2026, represent a significant expansion in use of this tactic compared to prior years."
    publisher: "Google Cloud Blog (GTIG)"
  - quote: "UNC6780 (aka \"TeamPCP\") conducted extensive open source supply chain compromises targeting ecosystems like PyPI, npm, and Docker Hub. Initial infection vectors varied across incidents, and included abuse of the pull_request_target GitHub Actions trigger to obtain base repository secrets and write permissions."
    publisher: "Google Cloud Blog (GTIG)"
  - quote: "While the malicious versions of axios were removed from the npm registry within three hours of their release, the scope of the compromise is estimated to be broad, as the package has over 100 million weekly downloads."
    publisher: "Google Cloud Blog (GTIG)"
  - quote: "Setting this value to at least 24 hours (1440 minutes) ensures that freshly published, potentially poisoned packages are quarantined until the broader security community has had time to identify and remove them"
    publisher: "Google Cloud Blog (GTIG)"
verification: multi-source
sourcing_note: >
  Two vendors reached the same attribution independently under different tracking names, which is what makes
  this genuine corroboration rather than republication: Amazon names the cluster SAPPHIRE SLEET / STARDUST
  CHOLLIMA / BlueNoroff and Google credits the axios compromise to UNC1069, already a registered alias on the
  same registry record. Critically, neither primary states that equivalence: GTIG names MIDNIGHT NEPTUNE
  (formerly UNC1069) and never says SAPPHIRE SLEET, and Amazon never says UNC1069. The bridging claim is
  CyberScoop's and is cited inline to CyberScoop at the clause that makes it, which is also the provenance the
  entity registry records. Both vendors hedge, and the hedges are preserved — Amazon states medium confidence explicitly.
  Amazon is cited for the maintainer social-engineering finding, the rehearsal assessment and the
  dependency-graph evasion; GTIG for the scale assessment and the pull_request_target mechanism. Deliberately
  omitted: GTIG's year-on-year percentage growth figure, which is a statistic without an operational decision
  attached, and its account of a cryptocurrency theft whose dollar value carries no defender takeaway for this
  constituency. The first Amazon evidence quote is truncated mid-word in the source extract available to this
  synthesis and is carried only as far as it is verbatim; the alias list is stated in full in the body instead.
  Both premises of the release-age cooldown action — the 24-hour (1440-minute) value and the three-hour axios
  removal window that motivates it — are GTIG's own statements and are quoted and cited rather than asserted.
confidence: high
update_of: 2026-07-26/weekly-w30-npm-ai-toolchain-supply-chain-status
references:
  - 2026-07-30/amazon-dprk-attribution-npm-typo-crypto-rehearsal
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Audit every GitHub Actions workflow in your organisation that uses the pull_request_target trigger and confirm none exposes base-repository secrets or write permissions to code from a fork — this is the specific mechanism GTIG names UNC6780 as having abused across npm, PyPI and Docker Hub, and a workflow using that trigger runs with the base repository's privileges by design rather than by misconfiguration."
  - "Set a minimum release-age cooldown of at least 24 hours on npm and pnpm installs across CI and developer environments, so a freshly-published malicious version is quarantined during the window in which these compromises are typically caught and pulled — the malicious axios versions were removed from the registry within about three hours of release."
migrated_from: null
---

**UPDATE (originally covered 2026-07-26):** the prior weekly tracked this wave's front edge moving into the AI coding assistant's own trust configuration. This week the wave gained something it had lacked — independent cross-vendor agreement on who is running a significant part of it, and a named CI mechanism defenders can go and check.

Amazon published an attribution assessment covering three of the ecosystem's most consequential compromises, stating that "based on analysis of command-and-control (C2) indicators and TTPs, Amazon Threat Intelligence assesses with medium confidence that these campaigns are attributable to the DPRK-linked threat actor tracked as SAPPHIRE SLEET" — a cluster it also names as STARDUST CHOLLIMA, BlueNoroff, CageyChameleon and Alluring Pisces ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)). The access mechanism is consistent and is not a platform weakness: "in each case, the threat actor gained access by socially engineering a trusted maintainer of the package, then published a software update containing malicious code." ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)). Amazon also assesses that a small March 2025 compromise served as a testing ground for the more visible operations that followed ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)), and identifies an evasion design that has direct implications for how organisations scan: the payload "is designed to defeat scanners that evaluate packages one by one instead of reasoning about how they interact in a real dependency graph" ([AWS Security Blog, 2026-07-29](https://aws.amazon.com/blogs/security/amazon-identifies-north-korean-hacker-group-behind-open-source-supply-chain-attacks/)).

Google's threat-intelligence group published defender-facing guidance a day later and reached the same attribution independently, attributing the activity to an actor it now calls MIDNIGHT NEPTUNE, formerly known as UNC1069 ([Google Cloud Blog, 2026-07-30](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/)). Neither vendor states the equivalence itself; the reporting on Amazon's briefing does, recording that "security researchers track the group under several names, including UNC1069, Sapphire Sleet and Stardust Chollima" ([CyberScoop, 2026-07-29](https://cyberscoop.com/amazon-north-korea-open-source-software-attacks/)) — which is what makes this two vendors looking rather than one vendor being repeated. Its own assessment of the trend is unhedged on direction: "GTIG assesses with high confidence that the growth in very large-scale, open-source supply chain compromise campaigns, including use of worms and iterative compromises in 2025 and early 2026, represent a significant expansion in use of this tactic compared to prior years." ([Google Cloud Blog, 2026-07-30](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/)).

The most immediately actionable content is a named CI mechanism belonging to a different cluster: "UNC6780 (aka \"TeamPCP\") conducted extensive open source supply chain compromises targeting ecosystems like PyPI, npm, and Docker Hub. Initial infection vectors varied across incidents, and included abuse of the pull_request_target GitHub Actions trigger to obtain base repository secrets and write permissions." ([Google Cloud Blog, 2026-07-30](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/)). That trigger is worth singling out because it is not a misconfiguration in the usual sense — `pull_request_target` runs workflow code in the context of the base repository, with its secrets, deliberately, so a workflow that checks out or executes anything from the incoming fork hands those secrets to whoever opened the pull request. It is a design that behaves exactly as documented and is very easy to use wrongly.

**Defender takeaway:** the through-line from the prior weeklies holds — the initial-access objective is the maintainer, the pipeline and the developer's own toolchain rather than the registry — but this week adds two things a Swiss or European public-sector build estate can act on directly rather than track. The first is the CI trigger above. The second is a change in how package scanning has to work: if payloads are split so that no single package looks malicious in isolation, per-package scanning returns clean by design, and the control that still functions is time — a release-age cooldown that keeps a brand-new version out of builds during the hours in which these compromises are typically noticed and pulled. GTIG names the specific control and the specific value: "setting this value to at least 24 hours (1440 minutes) ensures that freshly published, potentially poisoned packages are quarantined until the broader security community has had time to identify and remove them" ([Google Cloud Blog, 2026-07-30](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/)). The axios case is the argument for it: "while the malicious versions of axios were removed from the npm registry within three hours of their release, the scope of the compromise is estimated to be broad, as the package has over 100 million weekly downloads" ([Google Cloud Blog, 2026-07-30](https://cloud.google.com/blog/topics/threat-intelligence/mitigation-guidance-for-supply-chain-compromise/)) — fast removal did not help, because the pull volume in those three hours was enormous.
