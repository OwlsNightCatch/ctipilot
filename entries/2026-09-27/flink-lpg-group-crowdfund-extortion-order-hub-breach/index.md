---
schema: 1
kind: incident
title: "Flink refuses a corporate ransom after an Order Hub breach, so extortion actor \"LPG Group\" pivots to crowdfund-style individual extortion of at least 10,000 customers and employees"
headline: "A refused corporate ransom becomes 10,000+ individual shakedown emails: an extortion playbook worth recognizing before it recurs"
summary: >
  Quick-commerce grocery delivery service Flink (Germany, also operating in the
  Netherlands) confirmed a breach of an internal order-management system; after
  Flink refused a cryptocurrency ransom, the previously undocumented extortion
  actor "LPG Group" mass-emailed at least 10,000 individual customers and
  employees directly, demanding small per-person payments toward a collective
  threshold and threatening to sell all data if it is not met by 2 October 2026.
discovered_at: "2026-09-27T04:32:00Z"
updated_at: null
event_date: "2026-09-25"
run_id: 2026-09-27T0404Z-intel
priority: notable
immediate_action: null
tags: [data-breach, organized-crime, phishing]
regions: [europe, dach]
sectors: [retail]
entities: ["actor:lpg-group"]
techniques: [T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html"
    publisher: "heise online"
    date: "2026-09-26"
    role: primary
  - url: "https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data"
    publisher: "NL Times"
    date: "2026-09-25"
    role: corroborating
closed_sources: []
evidence:
  - quote: "If not, the data would, literally, be \"sold on the deep web.\" The extortionists have thus turned to a kind of criminal crowdfunding against a company unwilling to pay. (translated from German)"
    publisher: "heise online"
    source_url: "https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html"
    original: "Wenn nicht, würden die Daten, so wörtlich „im deep web verkauft“. Die Erpresser haben sich also bei einem zahlungsunwilligen Unternehmen auf eine Art kriminelles Crowdfunding verlegt."
  - quote: "But I haven't seen individual consumers being approached before"
    publisher: "Pim Takkenberg, Northwave, via NL Times"
    source_url: "https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data"
  - quote: "As a matter of principle, Flink does not make contact with criminals and does not conduct negotiations with them. (translated from German)"
    publisher: "Flink, quoted by heise online"
    source_url: "https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html"
    original: "Flink tritt grundsätzlich nicht mit Kriminellen in Kontakt und führt keine Verhandlungen mit ihnen."
verification: multi-source
sourcing_note: >
  heise online's own reporting (which includes Flink's on-record statement)
  and NL Times' independent Dutch-market coverage (drawing on an NOS interview
  with a named Northwave researcher) each reached the facts independently
  rather than one relaying the other; both cite the group's ransom emails
  directly. No party has disclosed the initial-access vector into the Order
  Hub system, so this entry maps only the extortion mechanic, not an entry
  technique.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Flink, a quick-commerce grocery delivery service headquartered in Germany and also operating in the Netherlands (formerly in Austria and France), confirmed a breach of one of its internal "Order Hub" ordering systems, the decentralized, city-level warehouse software that lets the service promise delivery in under thirty minutes ([heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)). The company has not disclosed the initial-access vector; it says the specific Order Hub instance involved has been identified and unauthorized access to it cut off. Attackers first approached Flink directly, demanding payment in the cryptocurrency ETH and promising to delete the data if paid. Flink states plainly that it does not negotiate with criminals and did not respond ([heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)).

The extortion actor behind the breach, self-named "LPG Group" and previously undocumented, claims to have obtained personal information on a million Flink customers and 13,000 workers; Flink has not confirmed that figure, though NL Times notes one million would represent roughly two-thirds of the customer base the company reported in June ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data)). Rather than walk away after Flink's refusal to pay a corporate ransom, the group pivoted to mass-emailing individuals directly. At least 10,000 customers and employees in the Netherlands received ransom notes (heise reports Germany was also targeted, though the scale there is unclear), each demanding a small payment of 0.005 ETH (NL Times: the equivalent of EUR 11.80) toward a collective target of 100 ETH, which NL Times puts at just shy of EUR 237,300 and heise at roughly EUR 230,000, a discrepancy the two outlets' independent exchange-rate snapshots do not resolve, with a promise to delete each payer's data once the collective goal is met and a threat to sell everything if it is not, by a 2 October 2026 deadline ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data); [heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)). The emails address recipients by name from a spoofed, Flink-resembling sender, which the outlets note makes them more convincing than a generic mass-phishing blast. Exfiltrated data is limited to names, postal codes/delivery addresses, email addresses, phone numbers and, in some cases, delivery notes such as floor or apartment details; Flink states passwords, payment card details and bank data were not affected ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data); [heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)).

Cybersecurity researcher Pim Takkenberg of Northwave called the crowdfunding-style extortion attempt exceptional, noting that ShinyHunters had previously extorted Dutch higher-education institutions that were clients of a hacked software system. "But I haven't seen individual consumers being approached before," Takkenberg told Dutch broadcaster NOS ([Pim Takkenberg, Northwave, via NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data)). Abuse reporting to the group's mail provider curtailed the flood of messages, and only around 150 customers had proactively contacted Flink's support line as of reporting, leaving the true scale of contacted individuals, particularly in Germany, unclear. Flink has notified Berlin's data protection authority and police in both Germany and the Netherlands, and retained external IT forensics; heise's own coverage notes the company has not, contrary to an earlier report, engaged Germany's BSI ([heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)).

**Defender takeaway:** the operational lesson is for breach-response and communications teams, not for a specific technical control. A refusal to pay a corporate-level ransom no longer ends an extortion attempt when the actor holds individually identifiable customer or employee records: expect a pivot to direct, per-person pressure using a spoofed sender resembling the breached organization, and prepare customer-facing guidance (do not reply, do not pay, report to the organization and to law enforcement) before an incident, not during one. A collective-threshold "crowdfunding" structure, rather than per-victim ransom demands, is itself worth watching for as this technique's next evolution; treat any wave of individually-addressed extortion emails referencing a real breach as corroboration of that breach's scope, not as unrelated spam.
