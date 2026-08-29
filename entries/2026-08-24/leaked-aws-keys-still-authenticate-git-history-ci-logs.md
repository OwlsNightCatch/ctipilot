---
schema: 1
kind: research
title: "Truffle Security re-tested 10,616 leaked AWS key pairs and 88% still authenticate — 768 of them give full control of a company account, and none of the measured leak surfaces is the current working tree"
headline: "88% of leaked AWS keys still authenticate, and the measured leak surfaces are Git history, dataset repos, images, registries and CI logs — not the working tree"
summary: >
  Truffle Security re-verified 10,616 leaked AWS key pairs on 2026-08-10, drawn from a scanned population of 64,024
  unique verified pairs across 431,875 public findings surfaced between August 2022 and August 2026, and found 88%
  still authenticate. Crossing ownership against privilege, 768 live keys give full control of a company AWS account
  — 526 root keys plus 242 IAM users holding AdministratorAccess, two non-overlapping sets — and 130 of the live root
  keys sit on organization-management accounts controlling every member account beneath them. The median live key is
  1,831 days old, 86% were never rotated, and 90.5% of the accounts have no budget alert configured. The defender's
  point is where the keys came from: Git history, public dataset repositories, container images, package registries
  and CI logs — so a clean secret scan of the current working tree does not answer the question.
discovered_at: "2026-08-24T09:15:00Z"
event_date: "2026-08-19"
run_id: 2026-08-24T0410Z-intel
priority: notable
immediate_action: null
tags: [cloud, identity, info-disclosure, supply-chain]
regions: [global]
sectors: [public-sector, technology, finance]
entities: []
techniques: [T1552.001, T1078.004, T1580, T1526, T1213.003]
affected_products: ["Amazon Web Services"]
cves: []
sources:
  - url: "https://trufflesecurity.com/blog/leaked-corporate-aws-keys-held-full-admin-rights"
    publisher: "Truffle Security"
    date: "2026-08-19"
    role: primary
closed_sources: []
evidence:
  - quote: "The median live leaked key is five years old and has never been rotated."
    publisher: "Truffle Security"
  - quote: "The two sets do not overlap, so 768 live keys give full control of a company AWS account."
    publisher: "Truffle Security"
  - quote: "90.5% of leaked-key accounts have none."
    publisher: "Truffle Security"
verification: single-source
sourcing_note: >
  Single-source: Truffle Security is the only party to have run this measurement and no second party has reproduced
  it. Carried as the vendor's own measurement over its own scanning corpus. The methodology is stated and bounds the
  claims: re-verification used read-only metadata calls only — a caller-identity check, access-key enumeration,
  policy-name enumeration without reading policy documents, account contact information, organisation description,
  budget data and one cost query per account — with nothing modified and no key material or account identifiers
  published, and Truffle states it is notifying 10,260 of the 10,616 affected key owners ahead of publication. Two
  figures rest on narrower denominators than the headline and are attributed as such in the body: key age, rotation
  and the share created in the last thirty days all come from the 2,903 keys that permitted access-key enumeration
  (0.9% of that subset is ~26 keys, which is what the reported 25 matches — it cannot be read against the 64,024
  population), and the budget-alert share from the accounts with readable budget data. Only one leak surface is
  ranked by the source; the entry infers no ordering among the rest. Date note: the on-page byline reads 19 August 2026 while the raw HTML carries a
  site-build comment dated 21 August; the byline is used.
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
actions:
  - "Scan full Git history, published container image layers, package-registry artefacts and CI job logs for AWS credentials — not just the current working tree — and treat every hit as live until a caller-identity check proves otherwise, because 88% of the keys in this study still authenticated."
migrated_from: null
---

Truffle Security re-verified **10,616 leaked AWS key pairs** on 2026-08-10, a subset with complete credentials drawn from a scanned population of 64,024 unique verified AWS key pairs across 431,875 public findings surfaced between August 2022 and August 2026, and reports that **88% still authenticate** ([Truffle Security, 2026-08-19](https://trufflesecurity.com/blog/leaked-corporate-aws-keys-held-full-admin-rights)). Of the broader population, 10,625 keys (16.6%) were root keys across 9,945 distinct accounts. Within the enumerable subset described below, only 25 keys — 0.9% — were created in the last thirty days, and Truffle's reading of that is blunt: almost none of the population leaked recently, and the count has been building for years.

The privilege picture is what makes it operational. Crossing ownership against privilege, Truffle states: "The two sets do not overlap, so 768 live keys give full control of a company AWS account" — 526 root keys plus 242 IAM users carrying AdministratorAccess, derived from a wider set of 817 business-linked keys, with the remaining 49 scoped below administrator. Separately, **130 of the live root keys sit on organization-management accounts**, which control every member account in the organisation beneath them. Age and hygiene compound it: "The median live leaked key is five years old and has never been rotated" — 1,831 days, measured across the 2,903 keys that permitted access-key enumeration, of which only 13.7% had any newer key alongside the leaked one, with the oldest live key 17.4 years old. On the accounts where budget data was readable, "90.5% of leaked-key accounts have none," and where a budget did exist the median configured limit was $8 — the free-tier guardrail rather than a control. Truffle also found that 929 of 7,590 active IAM users (12%) already carry AWS's own compromised-key quarantine policy, meaning AWS itself detected the exposure and restricted them, and that **112 of those carry the pre-2023 version of that policy** — AWS flagged them at least three years ago and they still authenticate. Spend on the readable set was mostly negligible at a $0.03 median, but with a real tail: 50 accounts spent over $1,000 in the preceding month, nine over $10,000, and the readable set $420,631 in July alone.

The finding a defender should act on is the source distribution, not the counts. Truffle names five measured surfaces — Git history, public dataset repositories, container images, package registries and CI logs — and ranks only one of them: the largest single source is a public machine-learning dataset platform, with 8,482 unique live keys across 3,394 public datasets, whose keys skew most privileged of any source it tracks at 17.9% root. It publishes no ordering among the other four, so none should be inferred. **None of those is the current working tree**, which means the reassurance a team takes from a clean secret scan of `HEAD` is answering a different question from the one that matters: a credential deleted in a later commit is still in the object history, a credential removed in a later image build is still in the published layer, and a credential echoed by a build step is still in the job log long after the pipeline changed.

**Defender takeaway:** for a public-sector or critical-infrastructure estate the transferable action is to move credential scanning from the working tree to the artefact history — full Git history including deleted branches and dangling objects, every published container layer, package-registry artefacts, and CI job logs — and to treat a discovered key as live until a read-only caller-identity check says otherwise, since in this study nearly nine in ten were. Two secondary controls follow from Truffle's own numbers rather than from general practice: a budget alarm on every account is worth setting because 90.5% of the affected accounts had none, and it is often the only signal an organisation would get that a forgotten key is being used; and the presence of AWS's own quarantine policy on an IAM user should be treated as a confirmed-exposure alert to act on rather than a control that has already solved the problem, because 112 accounts in this set have carried that flag for over three years and the key still works. The organisation-management finding is the one that changes blast radius: a root key on the management account of an AWS organisation is not one account's problem, so those accounts deserve verification independently of the rest.
