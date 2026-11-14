---
schema: 1
kind: research
title: "Bauman University \"Department No. 4\": leaked documents show a GRU training pipeline that places graduates in Sandworm and Fancy Bear units"
headline: "Leaked Bauman University files show GRU officers run a hacking course that places graduates in Sandworm and Fancy Bear"
summary: "An investigation published on 2026-05-07 by a consortium including The Insider, The Guardian, Le Monde, Der Spiegel and VSquare, based on more than 2,000 leaked internal documents, shows that Department No. 4 of Bauman Moscow State Technical University trains hackers and saboteurs under GRU supervision. Between 10 and 15 of its students a year are assigned to GRU units, including Unit 74455 (Sandworm) and Fancy Bear (APT28)."
discovered_at: "2026-05-10T05:00:04Z"
event_date: 2026-05-07
run_id: 2026-05-10-001
priority: routine
immediate_action: null
tags:
  - nation-state
  - espionage
  - russia-nexus
regions:
  - europe
  - global
sectors:
  - public-sector
  - defense
entities:
  - "report:bauman-gru-pipeline-investigation-2026"
  - "actor:sandworm"
  - "actor:apt28"
techniques: []
affected_products: []
cves: []
sources:
  - url: "https://meduza.io/amp/en/feature/2026/05/07/secret-gru-linked-department-at-top-russian-university-trains-hackers-and-saboteurs-investigation-finds"
    publisher: "Meduza (English)"
    date: "2026-05-07"
    role: primary
  - url: "https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference"
    publisher: "The Guardian"
    date: "2026-05-07"
    role: corroborating
  - url: "https://www.lemonde.fr/en/m-le-mag/article/2026/05/07/moscow-s-bauman-university-the-clandestine-school-training-russian-hackers_6753208_117.html"
    publisher: "Le Monde"
    date: "2026-05-07"
    role: corroborating
  - url: "https://www.spiegel.de/ausland/hybrider-krieg-moskau-bildet-in-einem-geheimen-uni-programm-spione-und-hacker-aus-a-2de79023-aa56-4ed6-b5de-d7c222402e63"
    publisher: "Der Spiegel"
    date: "2026-05-07"
    role: corroborating
  - url: "https://www.heise.de/news/Cyberkrieg-Medien-zitieren-Interna-aus-Russlands-Geheimdienstausbildung-11285528.html"
    publisher: "heise online"
    date: "2026-05-07"
    role: corroborating
  - url: "https://vsquare.org/welcome-to-the-gru-university-where-moscow-turns-students-into-spies-and-hackers-bauman-stupakov/"
    publisher: "VSquare"
    date: "2026-05-07"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The journalists reviewed more than two thousand internal documents from the department, including curricula, contracts, promotional materials, and lists of students, graduates, and faculty."
    publisher: "Meduza (English)"
    source_url: "https://meduza.io/amp/en/feature/2026/05/07/secret-gru-linked-department-at-top-russian-university-trains-hackers-and-saboteurs-investigation-finds"
  - quote: "Between 10 and 15 students from the department are assigned to GRU units each year. Some graduates serve in military unit 74455, which belongs to the hacking group Sandworm, responsible in recent years for several of the largest cyberattacks."
    publisher: "Meduza (English)"
    source_url: "https://meduza.io/amp/en/feature/2026/05/07/secret-gru-linked-department-at-top-russian-university-trains-hackers-and-saboteurs-investigation-finds"
  - quote: "The documents indicate that the GRU exerts direct control over the recruitment and grading process – sending its own officers to conduct exams, approve candidates and oversee placements."
    publisher: "The Guardian"
    source_url: "https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference"
  - quote: "Sandworm has been accused by western intelligence agencies of unleashing some of the most destructive cyber-attacks of the past decade including targeting Ukraine’s power grid in 2015, Emmanuel Macron’s French presidential campaign in 2017"
    publisher: "The Guardian"
    source_url: "https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference"
  - quote: "of stealing emails from Emmanuel Macron's team when he was a presidential candidate in early 2017; and, more recently, of targeting institutions involved in"
    publisher: "Le Monde"
    source_url: "https://www.lemonde.fr/en/m-le-mag/article/2026/05/07/moscow-s-bauman-university-the-clandestine-school-training-russian-hackers_6753208_117.html"
  - quote: "the students are also trained to “exploit vulnerabilities” in such systems using the Metasploit software"
    publisher: "VSquare"
    source_url: "https://vsquare.org/welcome-to-the-gru-university-where-moscow-turns-students-into-spies-and-hackers-bauman-stupakov/"
  - quote: "according to the report, the training also includes a one-month training camp that everyone must attend (translated from German)"
    original: "zur Ausbildung gehört dem Bericht zufolge auch ein einmonatiges Trainingscamp, in das alle müssen"
    publisher: "heise online"
    source_url: "https://www.heise.de/news/Cyberkrieg-Medien-zitieren-Interna-aus-Russlands-Geheimdienstausbildung-11285528.html"
verification: multi-source
sourcing_note: >
  One leaked document set examined by a consortium of outlets: the Guardian, Meduza, Le Monde, VSquare and heise (relaying Der Spiegel)
  each report from the same files, so they corroborate the reporting rather than independently confirm the documents. The attributions
  attached to Sandworm and Fancy Bear are the outlets' accounts of western accusations, and they differ on the 2017 Macron campaign breach.
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
migrated_from: briefs/2026-05-10.md
updates:
  - at: "2026-10-21T20:21:31Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The consortium's journalists reviewed more than 2,000 leaked Bauman University documents and
      published an investigation based on them. The outlets attribute the 2017 Macron campaign breach
      differently (Sandworm in the Guardian and Meduza, Fancy Bear in Le Monde), and none of them reports
      continuing 2025 to 2026 APT28 activity against EU government or election targets. VSquare reports
      training with Metasploit against the protected networks of the US Department of Defense.
    fields: [affected_products, body, classification, confidence, entities, evidence, headline, sources, sourcing_note, summary, techniques, title, priority]
---

Department No. 4 of the military training centre at Bauman Moscow State Technical University trains hackers and saboteurs for the GRU, according to a joint investigation by The Insider, The Guardian, Le Monde, Der Spiegel, Frontstory and VSquare whose journalists reviewed more than two thousand internal documents from the department ([Meduza, 2026-05-07](https://meduza.io/amp/en/feature/2026/05/07/secret-gru-linked-department-at-top-russian-university-trains-hackers-and-saboteurs-investigation-finds)); the Guardian names Delfi among the six outlets and says the files cover several years of activity up to 2025 ([The Guardian, 2026-05-07](https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference)). The documents indicate that the GRU sends its own officers to conduct exams, approve candidates and oversee placements ([The Guardian, 2026-05-07](https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference)). A 144-hour course over two semesters, "Defence against technical reconnaissance", teaches password attacks, software vulnerabilities and trojans, and students must carry out practical penetration tests and develop a computer virus to pass ([The Guardian, 2026-05-07](https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference)). Heise, citing Der Spiegel, adds DDoS attacks, the hacking of a test server at the end of the course and a one-month training camp that all students attend ([heise online, 2026-05-07](https://www.heise.de/news/Cyberkrieg-Medien-zitieren-Interna-aus-Russlands-Geheimdienstausbildung-11285528.html)). Students study the protected networks of the US Department of Defense and are trained to exploit vulnerabilities in them with Metasploit ([VSquare, 2026-05-07](https://vsquare.org/welcome-to-the-gru-university-where-moscow-turns-students-into-spies-and-hackers-bauman-stupakov/)).

Between 10 and 15 students from the department are assigned to GRU units each year, some to military unit 74455, which belongs to Sandworm, and others to Fancy Bear ([Meduza, 2026-05-07](https://meduza.io/amp/en/feature/2026/05/07/secret-gru-linked-department-at-top-russian-university-trains-hackers-and-saboteurs-investigation-finds)). The Guardian traces one 2024 graduate to Fancy Bear and another to Unit 74455 in Anapa, and names Viktor Netyksho, a former commander of Fancy Bear's Unit 26165, among the teachers ([The Guardian, 2026-05-07](https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference)). The operations attached to the two units are western accusations, and the outlets differ on one of them: the Guardian says Sandworm has been accused of targeting Ukraine's power grid in 2015 and Emmanuel Macron's 2017 presidential campaign ([The Guardian, 2026-05-07](https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference)), while Le Monde says Fancy Bear (APT28) is accused of stealing emails from Macron's team in early 2017 and, more recently, of targeting institutions involved in organising the Paris 2024 Olympic Games ([Le Monde, 2026-05-07](https://www.lemonde.fr/en/m-le-mag/article/2026/05/07/moscow-s-bauman-university-the-clandestine-school-training-russian-hackers_6753208_117.html)). Heise reports, citing Der Spiegel, that one graduate apparently joined a unit said to be behind the 2017 NotPetya malware ([heise online, 2026-05-07](https://www.heise.de/news/Cyberkrieg-Medien-zitieren-Interna-aus-Russlands-Geheimdienstausbildung-11285528.html)). Bauman is one pipeline among several: the Guardian's source, a former senior Russian defence official, calls it one of a handful of elite universities used to identify gifted students and says another university, Mirea, was even more crucial in training hackers ([The Guardian, 2026-05-07](https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference)).

**Defender takeaway:** no change to detection or patching priorities; the files show Sandworm and Fancy Bear staffed through a supervised university course, and the latest cohort of trainees does not graduate until the end of the 2027 academic year ([The Guardian, 2026-05-07](https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference)).

## Correction — 2026-10-21T20:21:31Z

The consortium's journalists reviewed more than two thousand internal documents from the department and reported on them ([Meduza, 2026-05-07](https://meduza.io/amp/en/feature/2026/05/07/secret-gru-linked-department-at-top-russian-university-trains-hackers-and-saboteurs-investigation-finds)). The outlets attach the 2017 Macron campaign breach to different units: the Guardian lists it among Sandworm's accused operations ([The Guardian, 2026-05-07](https://www.theguardian.com/world/2026/may/07/revealed-russia-top-secret-spy-school-hacking-western-electoral-interference)), while Le Monde accuses Fancy Bear (APT28), whose most recent alleged activity it names is the targeting of institutions organising the Paris 2024 Olympic Games ([Le Monde, 2026-05-07](https://www.lemonde.fr/en/m-le-mag/article/2026/05/07/moscow-s-bauman-university-the-clandestine-school-training-russian-hackers_6753208_117.html)); none of the cited outlets reports continuing 2025 to 2026 APT28 activity against EU government or election targets. The Metasploit training against US Department of Defense networks is VSquare's reporting ([VSquare, 2026-05-07](https://vsquare.org/welcome-to-the-gru-university-where-moscow-turns-students-into-spies-and-hackers-bauman-stupakov/)), and the one-month camp is one all students attend, per heise citing Der Spiegel ([heise online, 2026-05-07](https://www.heise.de/news/Cyberkrieg-Medien-zitieren-Interna-aus-Russlands-Geheimdienstausbildung-11285528.html)).
