---
schema: 1
kind: incident
horizon: operational
title: >
  Everest ransomware breaches a Stadler Rail supplier data-exchange platform, demands CHF 10
  million — the Swiss rail manufacturer refuses to pay
headline: >
  Everest reaches Stadler Rail through a supplier's data-exchange platform, not Stadler's own
  perimeter
summary: >
  Stadler Rail, the Swiss rolling-stock manufacturer headquartered in Bussnang (Thurgau),
  disclosed on 2026-07-21 that the Russian-speaking double-extortion group Everest compromised a
  data-exchange platform it shares with a supplier and demanded a CHF 10 million ransom. Stadler
  refused to pay, filed a criminal complaint, and states its own IT and worldwide production were
  unaffected and no security-relevant or personal data was stolen. It is another home-region
  breach reached through a trusted third-party channel rather than the primary victim's network.
discovered_at: "2026-07-22T04:34:31Z"
updated_at: "2026-07-31T04:09:14Z"
event_date: 2026-07-21
run_id: 2026-07-22T0409Z-intel
priority: notable
immediate_action: null
tags:
  - ransomware
  - data-breach
  - supply-chain
  - organized-crime
regions:
  - switzerland
  - europe
  - dach
sectors:
  - transport
  - manufacturing
entities:
  - "actor:everest-ransomware"
  - "incident:stadler-rail-everest-supplier-breach-2026"
techniques:
  - T1199
  - T1078
affected_products: []
cves: []
sources:
  - url: "https://www.swissinfo.ch/ger/cyberkriminelle-greifen-thurgauer-zugbauer-stadler-rail-an/91776656"
    publisher: swissinfo.ch
    date: 2026-07-21
    role: primary
  - url: "https://www.itmagazine.ch/artikel/87645/Ransomware-Attacke_Stadler_Rail_hat_nicht_gezahlt.html"
    publisher: Swiss IT Magazine
    date: 2026-07-21
    role: corroborating
  - url: "https://www.halcyon.ai/threat-group/everest"
    publisher: Halcyon
    date: 2025-11-19
    role: corroborating
  - url: "https://www.technadu.com/everest-hackers-leak-270000-files-reportedly-from-stadler-rail-breach-after-swiss-firm-refuses-to-pay-including-cctv-footage-configurations/632103/"
    publisher: TechNadu
    date: 2026-07-29
    role: primary
  - url: "https://www.stadlerrail.com/en/media/media-releases/cybervorfall"
    publisher: Stadler Rail
    date: 2026-07-21
    role: primary
  - url: "https://www.inside-it.ch/cyberkriminelle-veroeffentlichen-daten-von-stadler-rail-20260730"
    publisher: Inside IT Switzerland
    date: 2026-07-30
    role: corroborating
closed_sources: []
evidence:
  - quote: "Ein von der cyberkriminellen Everest Group gefordertes Lösegeld in Höhe von zehn Millionen Franken bezahlte die Firma laut Mitteilung nicht"
    publisher: swissinfo.ch
  - quote: Die Produktion laufe aktuell weltweit normal weiter
    publisher: swissinfo.ch
  - quote: "According to the threat actor, which was first flagged by threat-intelligence tracker HackManac, the data breach yielded a 201 GB FTP archive holding more than 271,000 files."
    publisher: TechNadu
  - quote: "Everest claims the compromised data touches projects linked to several high-profile operators, including Deutsche Bahn, Merseytravel, Westbahn, and MTR, alongside other unnamed clients. If validated, exposure of engineering documentation and system configurations tied to these operators raises concerns around downstream risk to connected railway infrastructure."
    publisher: TechNadu
  - quote: "Stadler hat durch den Vorfall von Mitte Juli 2026 keine Daten verloren. Der Zugriff auf diese spezifischen, technischen Daten erfolgte über kompromittierte Zugangsdaten einer Datenaustausch-Plattform."
    publisher: Stadler Rail
verification: multi-source
sourcing_note: >
  Incident facts are from Stadler's own public statement (Mitteilung) as relayed by swissinfo.ch
  (Swiss public broadcaster) and Swiss IT Magazine; the Everest attribution rests on the group's
  own claim as reported. Stadler did not name the supplier or the platform, and no
  intrusion-mechanism details were disclosed.
confidence: high
references: []
weekly_section: null
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-07-31T04:09:14Z"
    run_id: 2026-07-31T0409Z-intel
    type: update
    summary: >
      Everest has published data it says came from the data-exchange platform Stadler Rail shares with
      a supplier, turning the CHF 10 million extortion Stadler refused into an actual disclosure
      event. TechNadu, relaying a threat-intelligence tracker's post of Everest's own listing, reports
      a 201 GB archive of more than 271,000 files and says Everest claims the material touches
      projects tied to Deutsche Bahn, Merseytravel, Westbahn and MTR — claims none of those operators
      or Stadler has confirmed, and which no second outlet independently reports. Stadler's own media
      release, first published 21 July and last revised 23 July, still states no security-relevant or
      personal data was taken and does not address the publication at all. The access path is
      unchanged and is the transferable part: compromised credentials for a shared supplier
      data-exchange platform, not Stadler's own perimeter.
    fields:
      - evidence
      - regions
      - sources
      - techniques
      - body
    merged_from: 2026-07-31/everest-publishes-stadler-rail-supplier-archive
migrated_from: null
---

Stadler Rail disclosed on 2026-07-21 that unauthorised parties gained access, in mid-July, to a **data-exchange platform Stadler uses with an (unnamed) supplier**, and that the Everest ransomware/extortion group claimed the intrusion and demanded a **CHF 10 million** ransom ([swissinfo.ch, 2026-07-21](https://www.swissinfo.ch/ger/cyberkriminelle-greifen-thurgauer-zugbauer-stadler-rail-an/91776656)). Stadler states it does not pay ransoms under any circumstances, has filed a criminal complaint with Thurgau cantonal police, and reports that its own IT systems were unharmed, no security-relevant or personal data was stolen, and worldwide rail-vehicle production and in-service fleets are unaffected — the accessed information belonged to the supplier and is described as not security-relevant ([Swiss IT Magazine, 2026-07-21](https://www.itmagazine.ch/artikel/87645/Ransomware-Attacke_Stadler_Rail_hat_nicht_gezahlt.html)).

Everest is a Russian-speaking, closed-group double-extortion operation that emerged in December 2020, with a code-level connection to the BlackByte ransomware family; it has run hybrid Initial Access Broker services since November 2021 and a corporate-insider recruitment programme offering cash/profit-sharing since October 2023, and its documented infection vectors are internet-exposed RDP without MFA, vulnerable VPN endpoints, and credentials bought from other brokers ([Halcyon, 2025-11-19](https://www.halcyon.ai/threat-group/everest)). Per the same profile the group claimed, in October 2025, attacks on critical infrastructure including a European national electricity transmission operator, aviation systems affecting multiple European airports (Heathrow, Brussels and Berlin), and telecommunications networks — recurring targeting of the European critical-infrastructure and transport space, though those victim claims are the group's own leak-site assertions and are unconfirmed by the named organisations.

**Defender takeaway:** the operationally important fact for peers is the vector, not the victim — a well-resourced extortion actor reached a Swiss transport manufacturer's supplier-side data without touching Stadler's own network, by compromising a B2B data-exchange integration. This is the same trusted-relationship pattern (mapped as T1199) behind several recent home-region incidents. Treat supplier and partner data-exchange platforms as part of your own attack surface in third-party risk reviews, and note that Stadler's refusal-to-pay posture only holds because its own systems and backups were intact — the exposure that mattered here sat in a shared platform outside its direct control.

## Update — 2026-07-31T04:09:14Z

The earlier entry recorded Everest compromising a data-exchange platform Stadler Rail shares with a supplier, a CHF 10 million demand, and Stadler's refusal to pay. The extortion has now moved to its next stage: Everest has published the data ([Inside IT Switzerland, 2026-07-30](https://www.inside-it.ch/cyberkriminelle-veroeffentlichen-daten-von-stadler-rail-20260730)). What is new beyond that fact is a claim about who else is in the archive, and it needs handling with care.

TechNadu reports a 201 GB archive holding more than 271,000 files, attributing the figures to the actor itself via a threat-intelligence tracker that flagged the listing, with the content described as railway software, CCTV footage, engineering documentation and configuration files. It further reports that Everest claims the data touches projects linked to Deutsche Bahn, Merseytravel, Westbahn and MTR, and appends its own conditional — "if validated," exposure of engineering documentation and system configurations tied to these operators would raise downstream risk to connected railway infrastructure ([TechNadu, 2026-07-29](https://www.technadu.com/everest-hackers-leak-270000-files-reportedly-from-stadler-rail-breach-after-swiss-firm-refuses-to-pay-including-cctv-footage-configurations/632103/)). That hedge is the correct reading. These are an extortion group's assertions about the value of what it stole, relayed through one outlet, and none of the four named operators has confirmed anything. TechNadu also notes the odd operational detail that Everest claimed the attack but did not list Stadler on its leak site, so the archive appears to have been dropped outside the group's normal publication channel.

Stadler's own position has not moved. Its media release, first published on 21 July and last revised on 23 July according to its content-management metadata, states that Stadler lost no data in the mid-July 2026 incident and that access to the specific technical data involved was obtained through compromised credentials for a data-exchange platform; it records the CHF 10 million demand, the refusal to pay, and a criminal complaint filed with the Thurgau cantonal police ([Stadler Rail, 2026-07-21](https://www.stadlerrail.com/en/media/media-releases/cybervorfall)). The release does not confirm, deny or acknowledge the publication event — it predates it. So the current state is a victim statement scoped to "no security-relevant or personal data" standing beside an attacker claim of a 201 GB archive naming four third-party operators, with nothing yet reconciling them.

That gap is the pattern worth flagging rather than the file count. Two Swiss and European public-sector incidents this month followed the same arc — an early, narrow "not affected" characterisation, followed by a leak or an authority report that contradicted it. This one has not reached that point, and it may not; Stadler's statement may hold up entirely. But an early scoping statement issued before an attacker publishes is a hypothesis about what was taken, and it is being treated by readers as a finding.

**Defender takeaway:** for anyone in the rail supply chain, the actionable question is not whether Everest's operator list is accurate but whether you would be able to answer it about yourself. The access path here was credentials to a shared supplier data-exchange platform, so the exposure any given partner carries is the set of engineering documents and configuration files it has ever placed on that platform — which is knowable from the platform's own records without waiting for the archive to be analysed. Organisations that exchange design or configuration data with manufacturers through third-party portals should be pulling their own upload inventories now rather than watching for their name in coverage. The same trusted-relationship path — valid credentials on a partner's channel rather than a breach of the victim's perimeter — also drove the ransomware intrusion Kaspersky documented this week, and it does not show up in perimeter telemetry at all.
