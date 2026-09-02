---
schema: 1
kind: policy
title: "Swiss federal offices planned to outsource part of the E-ID trust infrastructure to Amazon Web Services; a ministerial veto stopped it in February 2026 on CLOUD Act and digital-sovereignty grounds"
headline: "Bern almost handed a hyperscaler the register that verifies whether a Swiss digital identity is genuine"
summary: >
  Investigative reporting by Republik (2026-09-01), corroborated by heise online and Inside IT
  Switzerland, reveals that Switzerland's Federal Office of Justice and Federal Office of
  Informatics planned in spring 2026 to award Amazon Web Services a contract covering core
  components of the Swiss E-ID's trust infrastructure. Justice Minister Beat Jans vetoed the award
  in mid-February 2026 on digital-sovereignty grounds, with one of the three outlets also tying the
  decision to Amazon's exposure under the US CLOUD Act; the Confederation's existing AWS framework
  contracts give Amazon unilateral rights to change technical terms and only a 90-day
  data-migration window on termination.
discovered_at: "2026-09-02T05:10:00Z"
updated_at: null
event_date: "2026-09-01"
run_id: 2026-09-02T0411Z-intel
priority: notable
immediate_action: null
tags: [cloud, identity]
regions: [switzerland]
sectors: [public-sector]
entities:
  - "policy:swiss-e-id-trust-infrastructure"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://www.republik.ch/2026/09/01/e-id-bundesrat-beat-jans-stoppt-auftrag-an-amazon"
    publisher: "Republik"
    date: "2026-09-01"
    role: primary
  - url: "https://www.heise.de/news/Schweizer-E-ID-Justizminister-Jans-verhindert-geheimen-Amazon-Deal-11437433.html"
    publisher: "heise online (Stefan Krempl)"
    date: "2026-09-01"
    role: corroborating
  - url: "https://www.inside-it.ch/bund-zog-aws-cloud-fuer-e-id-in-betracht-20260901"
    publisher: "Inside IT Switzerland"
    date: "2026-09-01"
    role: corroborating
closed_sources: []
evidence:
  - quote: "An award to Amazon was out of the question. (translated from German)"
    original: "Ein Zuschlag an Amazon komme nicht infrage."
    publisher: "Republik"
  - quote: "It becomes questionable when the state makes itself dependent, for critical infrastructure, on a single commercial provider that can discontinue operations, change terms, or impair availability. (translated from German)"
    original: "Fragwürdig wird es, wenn sich der Staat bei kritischer Infrastruktur von einem einzelnen kommerziellen Anbieter abhängig macht, der den Betrieb einstellen, Bedingungen ändern oder die Verfügbarkeit beeinträchtigen kann."
    publisher: "Republik, quoting Martina Kolpondinos (decentralized-trust-architecture expert)"
  - quote: "If the cloud contract is terminated, the federal administration has only 90 days to withdraw its data before Amazon irrevocably deletes everything. (translated from German)"
    original: "Wenn der Cloud-Vertrag aufgelöst wird, hat die Bundesverwaltung lediglich 90 Tage Zeit, um ihre Daten abzuziehen, bevor Amazon alles unwiderruflich löscht."
    publisher: "Republik"
verification: single-source
sourcing_note: >
  Republik is the sole investigator (its own reporting cites a direct confirmation from the Federal
  Office of Justice and unnamed insiders close to the Federal Council). heise online and Inside IT
  Switzerland both explicitly frame their coverage as relaying Republik's disclosure ("wie das
  Magazin Republik enthüllt") rather than independently corroborating the underlying facts, so this
  is one assessor with two syndicating publishers, not multi-source confirmation.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Republik's investigation, published 2026-09-01, reveals that Switzerland's Federal Office of Justice (Bundesamt für Justiz) and Federal Office of Informatics and Telecommunications (BIT) planned in spring 2026 to award Amazon Web Services a contract covering core components of the Swiss E-ID's "Vertrauensinfrastruktur" — the trust infrastructure that confirms whether a digital identity is genuine and whether a requesting organization is authorized to verify it ([Republik, 2026-09-01](https://www.republik.ch/2026/09/01/e-id-bundesrat-beat-jans-stoppt-auftrag-an-amazon)). The scope covered the Basisregister, which anonymously tracks whether a given E-ID is still valid, and the publicly queryable Vertrauensregister listing every authorized issuer and verifier — from federal, cantonal and communal authorities to private organizations such as banks. AWS was favored chiefly for its around-the-clock data-centre availability, which officials wanted as a fallback given delays in the Confederation's own planned government cloud; the Federal Office of Justice confirmed to Republik that "im Rahmen der Projektarbeiten wurden aus technischer Sicht sämtliche Optionen geprüft" (all options were reviewed from a technical standpoint as part of the project work, translated from German) ([Republik, 2026-09-01](https://www.republik.ch/2026/09/01/e-id-bundesrat-beat-jans-stoppt-auftrag-an-amazon)).

Federal Councillor Beat Jans, the SP minister responsible for approving major federal IT procurements, vetoed the award in mid-February 2026: "an award to Amazon was out of the question," per Republik's sources close to the Federal Council, because handing the task to the American company would directly contradict the Federal Council's own objectives for greater Swiss digital sovereignty ([Republik, 2026-09-01](https://www.republik.ch/2026/09/01/e-id-bundesrat-beat-jans-stoppt-auftrag-an-amazon)). The specific legal exposure behind that reasoning, per Inside IT's own relay of the same insider sourcing, is that Amazon as a US company is subject to the US CLOUD Act ([Inside IT Switzerland, 2026-09-01](https://www.inside-it.ch/bund-zog-aws-cloud-fuer-e-id-in-betracht-20260901)); Republik's and heise's own reporting present the CLOUD Act point as their own explanatory framing rather than folding it into the insider-confirmed statement, so the sourcing on whether Jans's own confirmed rationale explicitly named the CLOUD Act, or only digital sovereignty in general, is not fully consistent across the three outlets. Republik's review of the Confederation's existing 2021 AWS framework contract — obtained after the outlet won a Federal Administrative Court case for disclosure — found a standardized commercial template rather than terms negotiated for state use: Amazon reserves the unilateral right to change the technical basis of the service, liability for outages is minimal, and on contract termination the administration has only 90 days to migrate all its data before Amazon irrevocably deletes it ([Republik, 2026-09-01](https://www.republik.ch/2026/09/01/e-id-bundesrat-beat-jans-stoppt-auftrag-an-amazon)). An expert in decentralized trust architectures quoted by Republik frames the underlying risk independent of the vendor's home jurisdiction: "it becomes questionable when the state makes itself dependent, for critical infrastructure, on a single commercial provider that can discontinue operations, change terms, or impair availability" (translated from German) ([Republik, 2026-09-01](https://www.republik.ch/2026/09/01/e-id-bundesrat-beat-jans-stoppt-auftrag-an-amazon)).

The E-ID's public launch is already delayed from end-2026 to the first half of 2027 for unrelated reasons — open questions on AHV-number lookups, AI-driven deepfake risk to online enrollment, and incompatibility with the EU's own eID system in its first version ([Republik, 2026-09-01](https://www.republik.ch/2026/09/01/e-id-bundesrat-beat-jans-stoppt-auftrag-an-amazon)).

**Defender takeaway:** the transferable lesson is the contract-risk pattern, not the E-ID case specifically. Any public-sector body evaluating a hyperscaler framework contract for infrastructure that verifies identity, authorization or trust should check for the same three terms Republik found: unilateral rights for the vendor to change technical conditions, minimal liability caps on outages, and a short data-exit window on termination. A 90-day migration deadline is not workable for infrastructure whose failure mode is "citizens and businesses can no longer prove who they are."
