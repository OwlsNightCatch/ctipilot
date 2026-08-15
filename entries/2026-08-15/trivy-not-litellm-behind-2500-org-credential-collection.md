---
schema: 1
kind: threat
horizon: operational
title: "The '2,500-organisation LiteLLM breach' was mostly not LiteLLM: 95% of the identified victims were collected before the poisoned packages existed, through the Trivy scanner their pipelines pulled unpinned"
headline: "SOCRadar's row-level re-analysis moves the blast radius upstream to a compromised security scanner — which changes what a CI/CD estate has to audit"
summary: >
  SOCRadar re-analysed the exposure dataset behind the widely reported 2,500-organisation LiteLLM supply-chain
  breach and found that 2,085 of the 2,188 identified organisations — 95% — had credential collection that ended
  before the poisoned LiteLLM packages were ever published. The collection tracks the compromise of Aqua
  Security's Trivy scanner instead, whose poisoned release LiteLLM's own CI pulled unpinned. An estate that
  checked only for the LiteLLM package versions has audited the wrong artifact.
discovered_at: "2026-08-15T06:20:00Z"
event_date: "2026-08-13"
run_id: 2026-08-15T0412Z-intel
priority: notable
immediate_action: null
tags:
  - supply-chain
  - organized-crime
  - cloud
  - data-breach
regions:
  - global
  - europe
sectors:
  - technology
  - public-sector
entities:
  - actor:teampcp
techniques: [T1195.002, T1552.001, T1078.004]
affected_products:
  - Aqua Security Trivy
  - LiteLLM
cves: []
sources:
  - url: "https://socradar.io/blog/litellm-supply-chain-attack/"
    publisher: SOCRadar
    date: "2026-08-13"
    role: primary
  - url: "https://www.securityweek.com/trivy-not-litellm-behind-the-2500-org-compromise/"
    publisher: SecurityWeek
    date: "2026-08-14"
    role: corroborating
  - url: "https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/"
    publisher: Aqua Security
    date: "2026-04-01"
    role: primary
  - url: "https://www.docker.com/blog/trivy-supply-chain-compromise-what-docker-hub-users-should-know/"
    publisher: Docker
    date: "2026-03-23"
    role: corroborating
  - url: "https://docs.litellm.ai/blog/security-update-march-2026"
    publisher: "LiteLLM (BerriAI)"
    date: "2026-03-24"
    role: corroborating
  - url: "https://cert.europa.eu/blog/european-commission-cloud-breach-trivy-supply-chain"
    publisher: CERT-EU
    date: "2026-04-02"
    role: corroborating
closed_sources: []
evidence:
  - quote: "For 2,085 organizations, or 95% of the 2,188 that were identified, data collection activity ended before March 24, when the poisoned LiteLLM packages were published to the registry."
    publisher: "SecurityWeek, citing SOCRadar"
  - quote: "March 19, 2026 (~17:43 UTC): The attacker force-pushed 76 of 77 version tags in the aquasecurity/trivy-action repository and all 7 tags in aquasecurity/setup-trivy, redirecting trusted references to malicious commits."
    publisher: Aqua Security
  - quote: "We believe that the compromise originated from the Trivy dependency used in our CI/CD security scanning workflow."
    publisher: "LiteLLM (BerriAI)"
  - quote: "GitHub's release UI displayed \"Immutable\" badges next to each poisoned tag. The attacker may have deliberately published immutable releases after force-pushing, locking in the malicious state. Organizations should not rely solely on the \"Immutable\" indicator. Pinning to full commit SHAs remains the only truly immutable protection."
    publisher: Aqua Security
  - quote: "We assess with high confidence that initial access was obtained through the Trivy supply-chain compromise, which was publicly attributed to a threat actor known as TeamPCP."
    publisher: CERT-EU
verification: multi-source
sourcing_note: >
  The in-window item is SOCRadar's re-analysis of 2026-08-13 and its pickup the following day; the underlying
  compromise is from March 2026 and is carried here as the background the correction rests on, each fact cited
  to the party that states it — the affected vendors' own incident posts for the timeline, and CERT-EU's own
  blog for the European Commission intrusion. No CVE identifier is carried in this entry's metadata: the
  identifier that covers this ecosystem compromise is recorded against a different TeamPCP supply-chain
  incident in this pipeline's own CVE index, and that conflict is logged for reconciliation rather than
  resolved by asserting one reading here.
confidence: high
update_of: null
references:
  - 2026-08-06/litellm-callback-hook-post-inference-tool-call-forgery
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions:
  - "Re-scope any audit that was closed on the question 'did we install litellm 1.82.7 or 1.82.8 on 24 March': check instead whether CI workflows referenced aquasecurity/trivy-action or aquasecurity/setup-trivy by mutable version tag rather than a full commit SHA in the second half of March 2026, and whether any host pulled the aquasec/trivy image tags 0.69.4, 0.69.5, 0.69.6 or latest between 19 March 18:24 UTC and 23 March 01:36 UTC per Docker's own stated window. Treat credentials reachable from those runners as exposed."
migrated_from: null
---

The widely reported figure — more than 2,500 organisations compromised through poisoned LiteLLM packages — turns out to describe the wrong artifact for almost all of them. SOCRadar re-analysed the exposure dataset row by row and found that "For 2,085 organizations, or 95% of the 2,188 that were identified, data collection activity ended before March 24, when the poisoned LiteLLM packages were published to the registry" ([SecurityWeek, 2026-08-14](https://www.securityweek.com/trivy-not-litellm-behind-the-2500-org-compromise/) · [SOCRadar, 2026-08-13](https://socradar.io/blog/litellm-supply-chain-attack/)). Collection that stops before the malicious packages exist cannot have come from them. SOCRadar times the start against the upstream event instead: the earliest collection record sits eighteen minutes after the poisoned Trivy build published, activity surged while malicious Trivy images were live on Docker Hub, and it closed once the registry quarantined the LiteLLM packages ([SecurityWeek, 2026-08-14](https://www.securityweek.com/trivy-not-litellm-behind-the-2500-org-compromise/)).

The upstream compromise is documented by the vendor itself. Aqua Security's incident advisory records that on 19 March "The attacker force-pushed 76 of 77 version tags in the aquasecurity/trivy-action repository and all 7 tags in aquasecurity/setup-trivy, redirecting trusted references to malicious commits", publishing a malicious Trivy build at the same time ([Aqua Security, 2026-04-01](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/)). LiteLLM's own maintainers state the connection plainly: "We believe that the compromise originated from the Trivy dependency used in our CI/CD security scanning workflow" ([LiteLLM, 2026-03-24](https://docs.litellm.ai/blog/security-update-march-2026)). A security scanner is an unusually good place to put credential-stealing code, because it is a tool organisations deliberately run inside their build systems with access to the material they are scanning.

One detail from Aqua's write-up deserves to outlive this incident. The poisoned tags carried GitHub's "Immutable" badge: "The attacker may have deliberately published immutable releases after force-pushing, locking in the malicious state. Organizations should not rely solely on the 'Immutable' indicator. Pinning to full commit SHAs remains the only truly immutable protection" ([Aqua Security, 2026-04-01](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/)). A control that displayed as satisfied while being subverted is worse than an absent one, because it ends the review.

What the correction is worth to this constituency is visible in one of the confirmed victims. CERT-EU assesses "with high confidence that initial access was obtained through the Trivy supply-chain compromise, which was publicly attributed to a threat actor known as TeamPCP", in an intrusion into a European Commission cloud account from which "A significant volume of data (about 91.7 GB compressed) was exfiltrated ... including personal data such as names, email addresses, and email content" ([CERT-EU, 2026-04-02](https://cert.europa.eu/blog/european-commission-cloud-breach-trivy-supply-chain)). That is an EU institution reached through a build-pipeline dependency, not through a package a developer chose to install.

**Defender takeaway:** the operational cost of a misattributed root cause is a closed audit. An organisation that asked "did we install the bad LiteLLM version in that forty-minute window" almost certainly answered no and moved on — while the artifact that actually collected credentials was a scanner its pipelines pulled by mutable tag, over several days. Docker states the exposure window for its images and the specific tags involved ([Docker, 2026-03-23](https://www.docker.com/blog/trivy-supply-chain-compromise-what-docker-hub-users-should-know/)); the durable lesson is that a build dependency referenced by tag is a dependency someone else can change after you approved it.

**Triage:** a security scanner reaching out during a build is normal behaviour, so egress from the runner is not by itself the discriminator. What separates this from a healthy pipeline is the pairing of a scanner invocation with credential-store and environment reads it has no reason to make, and outbound traffic to a destination that is not the scanner's own update or vulnerability-database endpoint — with the reference in the workflow file being a mutable tag rather than a commit SHA as the precondition that made it possible.
