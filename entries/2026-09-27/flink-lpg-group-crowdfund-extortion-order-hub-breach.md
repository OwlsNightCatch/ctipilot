---
schema: 1
kind: incident
title: "Flink refuses a corporate ransom after an Order Hub breach, so extortion actor \"LPG Group\" pivots to crowdfund-style individual extortion of at least 10,000 customers"
headline: "A refused corporate ransom becomes 10,000+ individual shakedown emails: an extortion playbook worth recognizing before it recurs"
summary: >
  Quick-commerce grocery delivery service Flink (Germany, also operating in the
  Netherlands) confirmed a breach of an internal order-management system; after
  Flink refused a cryptocurrency ransom, the little-known extortion
  actor "LPG Group" mass-emailed at least 10,000 individual customers directly
  (Flink says employees are being contacted too) with small per-person payment
  demands and a 2 October 2026 deadline; heise reads the 100 ETH total as a sum
  customers are to raise, NL Times as what the company itself would have to pay.
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
techniques: [T1078, T1657]
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
  - url: "https://retail-news.de/flink-datenschutzvorfall-kundendaten-phishing/"
    publisher: "RETAIL-NEWS Deutschland"
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
  - quote: "An unauthorised person gained access to one of the delivery service's internal systems with the help of compromised credentials (translated from German)"
    publisher: "RETAIL-NEWS Deutschland (reporting Flink's customer notification)"
    source_url: "https://retail-news.de/flink-datenschutzvorfall-kundendaten-phishing/"
    original: "gelangte eine unbefugte Person mithilfe kompromittierter Zugangsdaten in eines der internen Systeme des Lieferdienstes"
verification: multi-source
sourcing_note: >
  heise online's own reporting (which includes Flink's on-record statement)
  and NL Times' independent Dutch-market coverage (drawing on an NOS interview
  with a named Northwave researcher) each reached the facts independently
  rather than one relaying the other; both cite the group's ransom emails
  directly. heise and NL Times give no initial-access vector; Flink's own
  customer notification, as seen by RETAIL-NEWS, says compromised credentials
  were used; which credentials, how they were obtained and whether multi-factor
  authentication applied are not stated.
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
updates:
  - at: "2026-10-04T04:44:00Z"
    run_id: 2026-10-04T0405Z-intel
    type: correction
    summary: >
      Flink's own customer notification of 2026-09-25, seen by RETAIL-NEWS, says an unauthorised person reached an
      internal system with compromised credentials, which corrects the earlier statement that no initial-access vector
      had been disclosed. The 10,000 figure now says customers, the two outlets' differing readings of the 100 ETH
      demand are stated, and Flink's more cautious notice on the order details is carried.
    fields: [title, summary, techniques, sources, evidence, sourcing_note, body]
migrated_from: null
---

Flink, a quick-commerce grocery delivery service headquartered in Germany that also operates in the Netherlands and formerly in Austria and France ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data)), confirmed a breach of an internal ordering system used in its "Order Hubs", the small decentralized city warehouses behind its promise of delivery in under thirty minutes ([heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)). Flink's own customer notification, seen by RETAIL-NEWS, says an unauthorized person reached one of its internal systems with compromised credentials ([RETAIL-NEWS, 2026-09-25](https://retail-news.de/flink-datenschutzvorfall-kundendaten-phishing/)); which credentials and how they were obtained is not stated. Flink told heise that the specific Order Hub instance involved has been identified and unauthorized access to it cut off ([heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)). Attackers first approached Flink directly, demanding payment in the cryptocurrency ETH and promising to delete the data if paid. Flink states plainly that it does not negotiate with criminals and did not respond ([heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)).

The extortion actor behind the breach, self-named "LPG Group" and described by NL Times and heise as little-known ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data); [heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)), claims to have obtained personal information on a million Flink customers and 13,000 workers; Flink has not confirmed that figure, though NL Times notes one million would represent roughly two-thirds of the customer base the company reported in June ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data)). Rather than walk away after Flink's refusal to pay a corporate ransom, the group pivoted to mass-emailing individuals directly. At least 10,000 customers in the Netherlands received ransom notes (heise reports Germany was also targeted, though the scale there is unclear), and Flink says employees are being contacted directly too, each note demanding a small payment of 0.005 ETH (NL Times: the equivalent of EUR 11.80) toward a total of 100 ETH, which NL Times puts at just shy of EUR 237,300 and heise at roughly EUR 230,000, a discrepancy the two outlets' independent exchange-rate snapshots do not resolve. The outlets frame the 100 ETH differently: heise reads it as the sum customers are to raise, with the data deleted if it is reached and sold on the deep web if not, while NL Times reports the group saying it will delete all user data if the company itself pays 100 ETH; a 2 October 2026 deadline was mentioned ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data); [heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)). The emails address recipients by name from a spoofed, Flink-resembling sender, which heise says may leave recipients easily unsettled ([heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)). Flink says the copied data is limited to names, postal codes/delivery addresses, email addresses, phone numbers and, in individual cases, delivery notes such as floor or apartment details, and that passwords, payment card details and bank data were not affected ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data); [heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)). Flink's own customer notice of 2026-09-25 was more cautious: it said such data could have reached the attacker and that there was no concrete indication that the additional order details, such as floor, doorbell name and delivery notes, had actually been accessed ([RETAIL-NEWS, 2026-09-25](https://retail-news.de/flink-datenschutzvorfall-kundendaten-phishing/)).

Cybersecurity researcher Pim Takkenberg of Northwave called the crowdfunding-style extortion attempt exceptional, noting that ShinyHunters had previously extorted Dutch higher-education institutions that were clients of a hacked software system. "But I haven't seen individual consumers being approached before," Takkenberg told Dutch broadcaster NOS ([Pim Takkenberg, Northwave, via NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data)). Abuse reporting to the group's mail provider curtailed the flood of messages, and only around 150 customers had proactively contacted Flink's support line as of reporting, leaving the true scale of contacted individuals, particularly in Germany, unclear. Flink has notified Berlin's data protection authority and retained external IT forensics; heise's own coverage notes the company has not, contrary to an earlier report, engaged Germany's BSI ([heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)). It has filed reports with police in Germany and the Netherlands ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data)).

**Defender takeaway:** the operational lesson is for breach-response and communications teams, not for a specific technical control. A refusal to pay a corporate-level ransom no longer ends an extortion attempt when the actor holds individually identifiable customer or employee records: expect a pivot to direct, per-person pressure using a spoofed sender resembling the breached organization, and prepare customer-facing guidance (do not reply, do not pay, report to the organization and to law enforcement) before an incident, not during one. A collective-threshold "crowdfunding" structure, rather than per-victim ransom demands, is itself worth watching for as this technique's next evolution; treat any wave of individually-addressed extortion emails referencing a real breach as corroboration of that breach's scope, not as unrelated spam.

## Correction — 2026-10-04T04:44:00Z

Flink's own customer notification of 2026-09-25, which RETAIL-NEWS saw, says an unauthorized person reached one of the delivery service's internal systems with compromised credentials ([RETAIL-NEWS, 2026-09-25](https://retail-news.de/flink-datenschutzvorfall-kundendaten-phishing/)). Which credentials were used, how they were obtained and whether multi-factor authentication applied are not stated. heise reports the 10,000 ransom notes for customers ([heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)), and Flink says employees are also being contacted directly ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data)). The outlets read the 100 ETH differently: heise as the sum customers are to raise ([heise online, 2026-09-26](https://www.heise.de/news/Kunden-und-Mitarbeiter-von-Lieferdienst-Flink-werden-erpresst-11467086.html)), NL Times as what the group says the company itself would have to pay for all user data to be deleted ([NL Times, 2026-09-25](https://nltimes.nl/2026/09/25/individuals-sent-ransom-notes-cybercriminals-steal-flink-customer-worker-data)). Flink's customer notice was more cautious about data scope: it said there was no concrete indication that the additional order details had been accessed ([RETAIL-NEWS, 2026-09-25](https://retail-news.de/flink-datenschutzvorfall-kundendaten-phishing/)).
