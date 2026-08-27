---
schema: 1
kind: vulnerability
horizon: operational
title: "Three new PTC Windchill and FlexPLM CVEs land on the product line already under mass extortion — all three unauthenticated and flagged red by the vendor, and only one has a fixed version anyone outside PTC's login wall can find"
headline: "The advisory records carry no version data at all; a national CERT's structured copy yields the one fixed release"
summary: >
  PTC assigned three CVEs against Windchill and FlexPLM on 2026-08-20, relayed by BSI CERT-Bund.
  CVE-2026-77644 (9.3) is an unauthenticated access-control bypass in the Windchill Risk and Reliability
  Enterprise Edition module; CVE-2026-77645 (9.2) is an unauthenticated remote code execution in Windchill
  and FlexPLM that the advisory says may be exploited through deserialization of untrusted data;
  CVE-2026-77646 (7.7) is a server-side request forgery by the same mechanism in Windchill PDMLink and
  FlexPLM. All three need no authentication in PTC's own published vectors, and all three carry its highest
  urgency flag. The remediation picture is the problem: PTC published these as advisory records
  with no structured version data whatsoever, and its own support articles sit behind a login, so the only
  fixed version obtainable is 13.1.0.1 for the access-control flaw, read out of the German CERT's
  structured copy. No source links these three to the extortion campaign already running against this
  product line.
discovered_at: "2026-08-22T05:12:00Z"
event_date: "2026-08-20"
run_id: 2026-08-22T0410Z-intel
priority: high
immediate_action: null
tags: [vulnerabilities, rce, auth-bypass, pre-auth, no-patch]
regions: [global]
sectors: [manufacturing, defense, energy]
entities: []
techniques: [T1190]
affected_products: ["PTC Windchill", "PTC Windchill PDMLink", "PTC Windchill Risk and Reliability", "PTC FlexPLM"]
cves:
  - id: CVE-2026-77644
    cvss: "9.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [patch-available]
    affected: "PTC Windchill Risk and Reliability (WRR) Enterprise Edition below 13.1.0.1"
    fixed: "13.1.0.1"
  - id: CVE-2026-77645
    cvss: "9.2"
    epss: null
    type: rce
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "PTC Windchill and PTC FlexPLM — no version range published in any advisory record reachable this run"
    fixed: "not obtainable this run; PTC's own support article is behind a login wall and the advisory record carries no version data"
  - id: CVE-2026-77646
    cvss: "7.7"
    epss: null
    type: ssrf
    vector: zero-click
    auth: pre-auth
    status: [no-patch]
    affected: "PTC Windchill PDMLink and PTC FlexPLM — no version range published in any advisory record reachable this run"
    fixed: "not obtainable this run; same limitation as CVE-2026-77645"
sources:
  - url: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2963"
    publisher: "BSI CERT-Bund (WID-SEC-2026-2963)"
    date: "2026-08-20"
    role: primary
  - url: "https://github.com/advisories/GHSA-5hvp-9mcx-5245"
    publisher: "GitHub Security Advisory (PTC as numbering authority)"
    date: "2026-08-20"
    role: primary
  - url: "https://github.com/advisories/GHSA-qxmv-9q88-wwmw"
    publisher: "GitHub Security Advisory (PTC as numbering authority)"
    date: "2026-08-20"
    role: primary
  - url: "https://github.com/advisories/GHSA-2698-qwmx-3r6f"
    publisher: "GitHub Security Advisory (PTC as numbering authority)"
    date: "2026-08-20"
    role: primary
closed_sources: []
evidence: []
verification: single-source
sourcing_note: >
  PTC is the numbering authority for all three records and BSI CERT-Bund's structured advisory is what
  relays them to a European constituency, so this is one assessor with two publishers: reliability A,
  credibility 2. `evidence` is empty deliberately rather than by omission. The advisory records could only
  be read this run through a transport that summarises rather than returning raw page text — the advisory
  host refused the direct transport and the reader fallback was credit-exhausted — so no quotation from
  them could be literal-checked as a contiguous verbatim substring, and the body paraphrases instead of
  quoting. The scores, weakness classes and vector strings were read from those records and are reported as
  the vendor's own. Two further limits are stated plainly because they change what a reader can do. First,
  the advisory records carry no structured product or version data at all — an empty affected-versions
  field is PTC's own publication, not a fetch failure, because these were filed as records with no package
  ecosystem to bind a range to; the one fixed version here comes from BSI's structured product tree.
  Second, the CVSS 4.0 vectors carry a provider urgency of red on all three CVEs, which is PTC's own
  supplemental metric across the set rather than an annotation unique to one of them. On the question a
  reader will ask first: no source found this run links any of these three identifiers to the ongoing
  extortion campaign against internet-facing Windchill deployments, which remains anchored to the earlier
  CVE-2026-12569. That is a checked negative, not an assumption. The verification value is single-source
  on the same reasoning: the numbering authority and the relaying national CERT are one assessment with two
  publishers, not two independent assessors.
confidence: medium
update_of: null
references: ["2026-06-20/ptc-windchill-cve-2026-12569-unauthenticated-java-deserializ"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Upgrade Windchill Risk and Reliability Enterprise Edition to 13.1.0.1, the one fixed version published outside PTC's login wall. For the remote-code-execution and request-forgery flaws, open a support case with PTC to obtain the fixed builds for support articles CS474818 and CS474826 rather than waiting for a public advisory to carry them — there is no version range in the public records to triage against, so an inventory cannot answer whether an instance is affected."
  - "Treat any internet-reachable Windchill or FlexPLM instance as requiring exposure reduction now rather than after the version question is settled: all three are unauthenticated and network-reachable in PTC's own vectors, and this product line already has a mass-extortion campaign running against it on a different flaw."
migrated_from: null
---

PTC assigned three CVEs against Windchill and FlexPLM on 2026-08-20, and BSI CERT-Bund relayed them the same day. All three are network-reachable and need no authentication in PTC's own published vectors. CVE-2026-77644, scored 9.3, is described as a critical access-control bypass in the Windchill Risk and Reliability Enterprise Edition module, classified as missing authentication for a critical function. CVE-2026-77645, scored 9.2, is described as a critical remote code execution in Windchill and FlexPLM which the advisory says may be exploited through the deserialization of untrusted data — though its own weakness classification is improper input validation, with the deserialization mechanism appearing in the description text rather than as a second formal class. CVE-2026-77646, scored 7.7, is a server-side request forgery in Windchill PDMLink and FlexPLM reachable by the same deserialization mechanism ([BSI CERT-Bund, 2026-08-20](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2963); [GitHub Security Advisory, 2026-08-20](https://github.com/advisories/GHSA-5hvp-9mcx-5245)). All three carry a provider urgency of red in PTC's own published vectors.

The remediation gap is the operational story, and it is a publication problem rather than a research one. All three advisory records were filed with no structured product or version data — the affected-versions and patched-versions fields are empty, which is PTC's own choice of record type rather than an artefact of how they were read. PTC's own support articles carry the real build numbers and sit behind an authentication wall. The one exception came from an unexpected direction: BSI CERT-Bund's structured advisory copy binds CVE-2026-77644 to Windchill Risk and Reliability Enterprise Edition below 13.1.0.1 and names 13.1.0.1 as the remediating version ([BSI CERT-Bund, 2026-08-20](https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2963)). For the other two, the German CERT's record references only version-less product identifiers, so there is no public answer to "is my instance affected?" for either the unauthenticated code execution or the request forgery. For an asset owner that is a worse position than a high score: a CVSS 9.2 with no version boundary cannot be triaged, only assumed.

The context a reader will supply themselves needs stating carefully. This pipeline has covered a mass-extortion campaign against internet-exposed Windchill and FlexPLM deployments since late July, including the reverse-engineering of a purpose-built implant found on compromised instances, all of it anchored to a different flaw. A targeted check this run found no source connecting any of these three new identifiers to that campaign, and the campaign's exploited vulnerability remains the earlier one. Three unauthenticated flaws arriving on a product line under active mass exploitation is a reason to move, but it is not evidence that these particular flaws are being used, and this entry does not imply otherwise.

**Defender takeaway:** the sequencing writes itself. Patch the one flaw with a published fixed version, then treat the version gap on the other two as the thing to resolve by contacting the vendor rather than by waiting — a support case naming the two support articles will get build numbers faster than the public record will. In the meantime the control that does not depend on version knowledge is exposure: none of the three needs credentials, so an instance answering from the internet is exposed regardless of which build it runs, and a product-lifecycle-management platform is not a system with a good reason to be internet-reachable in the first place. On detection there is little honest to offer, and the reason is worth naming: with no root cause, no vulnerable endpoint and no version range published, any hunt guidance here would be invented. What is available is the generic post-exploitation surface for this application class, and the store already carries it in specific form from the campaign coverage — application-server processes spawning interpreters or shells, files appearing under the application's own web directories outside a deployment, and database queries arriving with the application's own service identity at times no scheduled job explains.
