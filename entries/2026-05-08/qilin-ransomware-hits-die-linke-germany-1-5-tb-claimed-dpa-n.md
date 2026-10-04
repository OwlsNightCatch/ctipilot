---
schema: 1
kind: incident
title: "Qilin claims a ransomware attack on the German party Die Linke; the party has not confirmed data theft"
headline: "Die Linke took its infrastructure offline after a suspected Qilin attack; Qilin listed the party on its leak site without samples"
summary: "Die Linke disclosed on 2026-03-27 that it had taken its infrastructure offline after a suspected ransomware attack it attributes to Qilin. Qilin listed the party on its leak site on 2026-04-01 without publishing samples. The party says its member database was not affected and that it cannot assess whether the attackers' aim of publishing internal data will succeed or has already occurred, and Heise reported that which internal data was compromised had not yet been definitively clarified."
discovered_at: "2026-05-08T05:00:04Z"
event_date: 2026-03-26
run_id: 2026-05-08-migrated
priority: routine
immediate_action: null
tags:
  - ransomware
  - data-breach
regions:
  - europe
  - dach
sectors: []
entities:
  - "incident:die-linke-qilin-2026"
  - "actor:qilin"
techniques: [T1486]
cves: []
sources:
  - url: "https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/"
    publisher: "Die Linke (statement by federal managing director Janis Ehling, German)"
    date: "2026-03-27"
    role: primary
  - url: "https://www.heise.de/en/news/Qilin-Left-Party-reports-Russian-ransomware-attack-11227232.html"
    publisher: "Heise Online"
    date: "2026-03-27"
    role: corroborating
  - url: "https://www.bleepingcomputer.com/news/security/die-linke-german-political-party-confirms-data-stolen-by-qilin-ransomware/"
    publisher: "BleepingComputer"
    date: "2026-04-03"
    role: corroborating
  - url: "https://therecord.media/hackers-threaten-to-leak-german-political-party-data"
    publisher: "The Record"
    date: "2026-04-06"
    role: corroborating
closed_sources: []
evidence:
  - quote: "it has not yet been definitively clarified which internal data has been compromised"
    publisher: "Heise Online"
verification: multi-source
sourcing_note: "The party's own statement of 2026-03-27 (German, paraphrased in translation) is the primary source for the party-side facts. Heise quotes the party's federal managing director directly, and BleepingComputer and The Record report the leak-site listing and the party's statement. Qilin's leak-site claim is the gang's own and unverified."
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
migrated_from: briefs/2026-05-08.md
updates:
  - at: "2026-09-30T07:12:38Z"
    run_id: 2026-09-30T0639Z-audit
    type: correction
    summary: >
      Die Linke did not confirm in April that Qilin encrypted and exfiltrated its systems, and no
      reachable source carries a 1.5 TB claim or a notification to the state data protection
      authority. The party disclosed the attack on 2026-03-27 and has not confirmed data theft. It
      says its member database was not affected and that it cannot assess whether the attackers' aim
      of publishing internal data will succeed or has already occurred, and Heise reported that
      which internal data was compromised had not yet been clarified. The facts now follow the
      party's own statement, Heise, BleepingComputer and The Record, and the priority moves from
      notable to routine because the sources give no access vector.
    fields: [title, headline, summary, event_date, priority, techniques, sources, evidence, verification, classification, body, sourcing_note, confidence]
---

Die Linke detected a cyberattack on its IT network on Thursday, 26 March 2026, took parts of its IT infrastructure offline as a precaution and filed a criminal complaint. In a statement the next day it said it had indications of a ransomware attack by the Qilin group and that its member database was not affected ([Die Linke, 2026-03-27](https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/)). Heise reported that it had not yet been definitively clarified which internal data had been compromised ([Heise Online, 2026-03-27](https://www.heise.de/en/news/Qilin-Left-Party-reports-Russian-ransomware-attack-11227232.html)). Qilin added the party to its leak site on 2026-04-01 without publishing data samples ([BleepingComputer, 2026-04-03](https://www.bleepingcomputer.com/news/security/die-linke-german-political-party-confirms-data-stolen-by-qilin-ransomware/)). **Contradiction:** BleepingComputer's headline says the party confirmed the data theft, while its own text says the party stopped short of confirming a data breach ([BleepingComputer, 2026-04-03](https://www.bleepingcomputer.com/news/security/die-linke-german-political-party-confirms-data-stolen-by-qilin-ransomware/)). The party says the attackers aim to publish sensitive internal data and personal information of headquarters staff, and that it cannot assess whether or to what extent this will succeed or has already happened ([Die Linke, 2026-03-27](https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/)).

The sources give no access vector, so the transferable ground is the target class: German political parties have been targeted by cyberattacks before ([The Record, 2026-04-06](https://therecord.media/hackers-threaten-to-leak-german-political-party-data)), and Die Linke describes ransomware attacks as often part of hybrid warfare and this one as aimed at weakening democratic structures ([Die Linke, 2026-03-27](https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/)).

## Correction — 2026-09-30T07:12:38Z

The earlier text said the party confirmed in April 2026 that its data was encrypted and exfiltrated, that Qilin claimed 1.5 TB, and that the state data protection authority was notified. Die Linke disclosed the attack on 2026-03-27 ([Heise Online, 2026-03-27](https://www.heise.de/en/news/Qilin-Left-Party-reports-Russian-ransomware-attack-11227232.html)), Qilin listed it on 2026-04-01 without samples ([BleepingComputer, 2026-04-03](https://www.bleepingcomputer.com/news/security/die-linke-german-political-party-confirms-data-stolen-by-qilin-ransomware/)), Heise reported that which internal data was compromised had not yet been definitively clarified ([Heise Online, 2026-03-27](https://www.heise.de/en/news/Qilin-Left-Party-reports-Russian-ransomware-attack-11227232.html)), and the party says it cannot assess whether the attackers' aim of publishing internal data will succeed or has already occurred ([Die Linke, 2026-03-27](https://www.die-linke.de/start/presse/detail/news/cyberangriff-auf-die-partei-die-linke/)). The 1.5 TB and notification claims appear in no reachable source and are removed.
