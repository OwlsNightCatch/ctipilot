---
schema: 1
kind: incident
horizon: operational
title: "UPDATE — Beacon traces the charity-CRM breach to an AWS access key exposed in public JavaScript build artifacts, and dates the whole exfiltration to a 87-minute window"
headline: "The credential that read 1,500 charities' data was not phished or brute-forced — a build pipeline shipped it to the browser"
summary: >
  Beacon, the CRM platform whose breach affecting around 1,500 UK charities this pipeline covered on 2026-08-08,
  published a root-cause update on 2026-08-12 stating the compromised AWS access key was potentially exposed in public
  JavaScript build artifacts. Analysis of the platform's AWS Cost & Usage reports places the malicious activity at
  01:20:16 UTC on 27 July, lasting about one hour and 27 minutes, during which the attacker copied and likely
  downloaded the entire customer database including attachments in readable form — data encrypted at rest in AWS, but
  decrypted by AWS for a holder of valid credentials. Beacon reports the attacker established no persistence, and has
  rotated all AWS-integrated credentials. The exposure class is the transferable part: a live secret compiled into a
  frontend bundle is invisible to secret scanning that only reads source repositories.
discovered_at: "2026-08-14T05:11:00Z"
event_date: "2026-08-12"
run_id: 2026-08-14T0417Z-intel
priority: notable
immediate_action: null
tags:
  - data-breach
  - cloud
  - supply-chain
regions:
  - uk
sectors:
  - public-sector
  - healthcare
entities:
  - incident:beacon-crm-uk-charities-breach-2026-08
techniques:
  - T1552.001
  - T1078.004
  - T1530
affected_products: []
cves: []
sources:
  - url: "https://www.infosecurity-magazine.com/news/exposed-aws-key-data-charities/"
    publisher: "Infosecurity Magazine"
    date: "2026-08-13"
    role: primary
  - url: "https://www.theregister.com/security/2026/08/13/aws-key-exposed-in-javascript-may-have-lit-way-to-beacons-charity-data/5287303"
    publisher: "The Register"
    date: "2026-08-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The software provider said in an August 12 incident update that the access key was potentially exposed in public Javascript build artifacts. This suggests an error was made in the course of software development."
    publisher: "Infosecurity Magazine"
  - quote: "This update confirms… that a copy of the database which holds all Beacon customer data, including attachment files, was made and likely downloaded in a readable format by the threat actor,"
    publisher: "Beacon CTO David Simpson, quoted by The Register"
verification: multi-source
sourcing_note: "Reliability is rated C because both cited outlets are trade press re-reporting a vendor statement rather than originating the assessment, which is how this pipeline rates the primary of the two. Both outlets report the same Beacon incident update of 2026-08-12 — one assessor, two publishers — so corroboration confirms the wording rather than independently establishing the root cause. Beacon itself hedges: the key was 'potentially' exposed this way, and The Register frames it as the leading suspect rather than a settled finding."
confidence: medium
update_of: 2026-08-08/beacon-crm-access-key-breach-uk-charities-hospices
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: C
  credibility: 2
watchlist_hit: false
actions:
  - "Point your secret scanner at the compiled, minified JavaScript your build pipeline actually serves to browsers, not only at the source repository it was built from — Beacon's root-cause update names a public build artifact as the likely source of the AWS key that read its entire customer database, and a repository-only scan would not have seen it."
migrated_from: null
---

**UPDATE (originally covered 2026-08-08):** the earlier entry recorded Beacon describing the compromised access key only as "more sophisticated than a simple compromised username and password", which left the actual failure unstated. Beacon's incident update of 2026-08-12 names it: ["The software provider said in an August 12 incident update that the access key was potentially exposed in public Javascript build artifacts. This suggests an error was made in the course of software development."](https://www.infosecurity-magazine.com/news/exposed-aws-key-data-charities/) The Register frames the same statement as the leading suspect in the July breach and observes that if the key was exposed in public build artifacts it raises the question of why Beacon's development pipeline and code-review controls did not catch it ([The Register, 2026-08-13](https://www.theregister.com/security/2026/08/13/aws-key-exposed-in-javascript-may-have-lit-way-to-beacons-charity-data/5287303)).

**The loss is now stated more strongly, and it is dated precisely.** Beacon's chief technology officer David Simpson wrote that ["This update confirms… that a copy of the database which holds all Beacon customer data, including attachment files, was made and likely downloaded in a readable format by the threat actor,"](https://www.theregister.com/security/2026/08/13/aws-key-exposed-in-javascript-may-have-lit-way-to-beacons-charity-data/5287303) — firmer than the earlier "assume it was taken" advice. The window comes from an unusual forensic source: analysis of Beacon's AWS Cost & Usage reports identified malicious activity beginning at 01:20:16 UTC on 27 July and lasting approximately one hour and 27 minutes, correlating with a sharp increase in data downloads across 27-28 July ([Infosecurity Magazine, 2026-08-13](https://www.infosecurity-magazine.com/news/exposed-aws-key-data-charities/)). The data was encrypted at rest in AWS, but the attacker's credentials were valid, so AWS decrypted it for them on the way out — encryption at rest protects against media theft, not against a working key. Beacon reports detecting no attempt by the attacker to maintain persistence in the environment, has reset all credentials for services and accounts integrated with AWS, and says there is so far no indication the stolen data has been published or otherwise misused. Simpson also cautioned customers that there are things Beacon may never be able to determine about the incident. The UK regulator has reviewed at least one affected charity's case and concluded the charity holds no responsibility for the breach ([Infosecurity Magazine, 2026-08-13](https://www.infosecurity-magazine.com/news/exposed-aws-key-data-charities/)).

**Defender takeaway:** the transferable finding is an exposure class, not a vendor failure. A credential committed to source control is what most organisations scan for; a credential injected into a frontend bundle at build time — through a build-tool environment variable that the bundler inlines, a configuration object serialised into the shipped JavaScript, or a source map published alongside it — never appears in the repository at all and is therefore invisible to repository-only scanning, while being served to every visitor. Two properties make it worse than the repository case: the artifact is public by construction, so there is no window during which the exposure is theoretical, and the credential is often a build-time service identity with more scope than any browser-facing code should hold. The detection point is the deployed asset, and for cloud credentials specifically the provider-side complement is the one Beacon used in hindsight — billing and usage telemetry, which showed the exfiltration as a cost anomaly and is available even where API-level logging is not. **Triage:** a legitimate frontend does carry public identifiers — publishable API keys, client IDs, analytics tokens — so finding key-shaped strings in a bundle is not by itself a finding. The discriminator is whether the credential authenticates to a control plane rather than to a scoped public endpoint: a provider access-key identifier paired with a secret, or any credential whose permissions are not enforced at the service boundary, is a live secret regardless of the fact that it shipped in a file meant for browsers.
