---
schema: 1
kind: incident
title: "Berlin's state government confirms an extortion attempt after a phishing click opens the shared Landesnetz; media reporting names Rhysida"
headline: "Berlin confirms extortion after a phishing click reaches the shared state network; media reports name Rhysida"
summary: >
  Germany's Berlin state administration confirmed on 2026-08-28 that it faces an active
  extortion attempt following a compromise of its shared Landesnetz government network first
  disclosed on 2026-08-17; media reporting attributes the attack to the ransomware group
  Rhysida, which separately claimed it on its own leak site. Investigative reporting states
  an employee's phishing-email click opened the network to attackers who exfiltrated 5.7 to
  5.8 terabytes of data, including critical-infrastructure and emergency-planning material,
  before detection; Berlin's government has publicly refused the roughly EUR 2 million ransom
  demand.
discovered_at: "2026-08-30T04:35:00Z"
updated_at: "2026-09-06T04:50:00Z"
event_date: "2026-08-28"
run_id: 2026-08-30T0410Z-intel
priority: high
immediate_action: null
tags: [ransomware, data-breach, phishing, organized-crime]
regions: [dach]
sectors: [public-sector]
entities: ["incident:berlin-landesnetz-compromise-2026-08", "actor:rhysida"]
techniques: [T1566, T1657]
affected_products: []
cves: []
sources:
  - url: "https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html"
    publisher: "Der Tagesspiegel"
    date: "2026-08-28"
    role: primary
  - url: "https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html"
    publisher: "heise online"
    date: "2026-08-29"
    role: primary
  - url: "https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html"
    publisher: "Security Affairs"
    date: "2026-08-29"
    role: corroborating
  - url: "https://www.berliner-zeitung.de/article/cyberangriff-auf-berliner-senat-wegner-bestaetigt-erpressungsversuch-10337926"
    publisher: "Berliner Zeitung"
    date: "2026-08-28"
    role: corroborating
  - url: "https://www.rbb24.de/politik/beitrag/2026/08/berlin-hackerangriff-landesnetz-loesegeld-forderung-erpresser.html"
    publisher: "rbb24 (Rundfunk Berlin-Brandenburg)"
    date: "2026-08-29"
    role: corroborating
  - url: "https://borncity.com/news/berlin-cyberangriff-rhysida-fordert-2-millionen-euro-fuer-57-tb-daten/"
    publisher: "BornCity"
    date: "2026-08-29"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a"
    publisher: "CISA / FBI / Multi-State ISAC"
    date: "2025-04-30"
    role: corroborating
  - url: "https://www.heise.de/news/Berliner-Senat-zahlt-nicht-sensible-Daten-jetzt-im-Darknet-11442286.html"
    publisher: "heise online"
    date: "2026-09-04"
    role: corroborating
  - url: "https://www.heise.de/news/Kehrtwende-bei-Cybersicherheit-Bund-gibt-Plan-fuer-BSI-Grundgesetzaenderung-auf-11440646.html"
    publisher: "heise online"
    date: "2026-09-03"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The attackers apparently gained access to the Landesnetz through an employee's click on a phishing email."
    original: "Zugang zum Landesnetz verschafften sich die Täter offenbar durch den Klick eines Mitarbeiters auf eine Phishing-Mail."
    publisher: "Der Tagesspiegel"
    source_url: "https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html"
  - quote: "“The state of Berlin will not submit to extortion,” Berlin Mayor Kai Wegner and Berlin's interior senator, Iris Spranger, said in a joint statement on Friday, before the ransomware group claimed the attack on their Tor data leak site."
    publisher: "Security Affairs"
    source_url: "https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html"
  - quote: "The ransomware group Rhysida claimed responsibility on its leak site August 28, posting an entry titled simply “Berlin, Germany” and claiming 5.79 terabytes of data across roughly 1.44 million files, with personal information on 12,076 individuals allegedly included."
    publisher: "Security Affairs"
    source_url: "https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html"
  - quote: "Experts identified the ransomware Rhysida as the tool with which the systems were encrypted and the data stolen."
    original: "Experten identifizierten die Ransomware Rhysida als das Werkzeug, mit dem die Systeme verschlüsselt und die Daten entwendet wurden."
    publisher: "BornCity"
    source_url: "https://borncity.com/news/berlin-cyberangriff-rhysida-fordert-2-millionen-euro-fuer-57-tb-daten/"
  - quote: "All files have been uploaded to the publicly accessible area — have fun browsing, data hunters!"
    original: "Alle Dateien wurden im öffentlich zugänglichen Bereich hochgeladen – viel Spaß beim Stöbern, Datenjäger!"
    publisher: "Rhysida leak-site posting, via heise online"
    source_url: "https://www.heise.de/news/Berliner-Senat-zahlt-nicht-sensible-Daten-jetzt-im-Darknet-11442286.html"
  - quote: "Based on what I can see here now, they have put the complete dataset online for everyone to view"
    original: "Nach dem, was ich jetzt hier sehen kann, haben sie den kompletten Datensatz für alle zur Einsicht live gestellt"
    publisher: "Joachim Selzer, Chaos Computer Club spokesperson, via heise online (dpa)"
    source_url: "https://www.heise.de/news/Berliner-Senat-zahlt-nicht-sensible-Daten-jetzt-im-Darknet-11442286.html"
  - quote: "Among the data that is viewable is, for example, the application for a new phone, including the signature of the administrative employee."
    original: "Unter den Daten, die einsehbar sind, ist zum Beispiel der Antrag auf ein neues Handy – samt der Unterschrift des Verwaltungsmitarbeiters."
    publisher: "heise online (dpa)"
    source_url: "https://www.heise.de/news/Berliner-Senat-zahlt-nicht-sensible-Daten-jetzt-im-Darknet-11442286.html"
  - quote: "the ministry points only to the existing constitutional framework."
    original: "vorlegen wird, verweist das Ressort nur auf den bestehenden verfassungsrechtlichen Rahmen."
    publisher: "heise online, citing the Federal Interior Ministry's (BMI) written reply"
    source_url: "https://www.heise.de/news/Kehrtwende-bei-Cybersicherheit-Bund-gibt-Plan-fuer-BSI-Grundgesetzaenderung-auf-11440646.html"
  - quote: "Until now, the BSI has only been constitutionally permitted to assist the states in defending against serious cyberattacks after an explicit request for administrative assistance. In addition, lengthy bilateral agreements had to be concluded, and these still do not exist with all 16 federal states today."
    original: "Bisher durfte das BSI den Ländern bei der Abwehr schwerer Cyberattacken verfassungsrechtlich bedingt erst nach einer expliziten Anforderung von Amtshilfe zur Seite stehen. Zudem mussten langwierige bilaterale Vereinbarungen geschlossen werden – und die existieren bis heute nicht mit allen 16 Bundesländern."
    publisher: "heise online"
    source_url: "https://www.heise.de/news/Kehrtwende-bei-Cybersicherheit-Bund-gibt-Plan-fuer-BSI-Grundgesetzaenderung-auf-11440646.html"
verification: multi-source
sourcing_note: >
  The phishing access vector and the Rhysida attribution are both sourced to investigative
  journalism (Der Tagesspiegel, Der Spiegel via heise online), not an official BSI or Senate
  technical disclosure; Berlin's Senate administration has explicitly declined to name the
  attacker, citing investigative-tactical reasons. Whether the affected systems were also
  encrypted, not only exfiltrated, is disputed: BornCity attributes an encryption claim to
  unnamed "experts", while every other cited source describes only data theft and extortion.
  Security Affairs states Berlin first disclosed the compromise on 2026-08-17; Berliner
  Zeitung, Der Tagesspiegel and rbb24 all independently state the compromise became public
  and the affected departments were disconnected on 2026-08-14. This entry follows the
  three-source consensus date.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates:
  - at: "2026-09-05T04:50:00Z"
    run_id: 2026-09-05T0409Z-intel
    type: update
    summary: >
      Rhysida's ultimatum lapsed on 2026-09-04 after Berlin's Senate refused to pay; the group
      then published the full stolen dataset on its darknet leak site, replacing its prior
      partial "auction" listing. Chaos Computer Club spokesperson Joachim Selzer confirmed the
      complete dataset is now publicly accessible to anyone, but whether it actually contains the
      drinking-water vulnerability analyses and administration credentials the group had earlier
      claimed remains what the Senate itself must still verify, per a state-parliament faction
      leader's own account.
    fields: [updated_at, sources, evidence, body]
  - at: "2026-09-06T04:50:00Z"
    run_id: 2026-09-06T0409Z-intel
    type: update
    summary: >
      Germany's federal government has quietly abandoned a plan set by the previous coalition to amend the
      Basic Law so the BSI could act as a true central authority for state- and municipal-level
      cyber incidents, per the Interior Ministry's own written Bundestag reply: a structural gap
      in federated cyber-incident response the fallout from this exact incident has now surfaced.
      Separately, the Chaos Computer Club identifies specific exposed record types (personnel
      matters, employment references, a handwritten signature on an internal device-request form)
      in the now fully-published leak.
    fields: [updated_at, sources, evidence, body]
migrated_from: null
---

Germany's Berlin state administration is the target of a live extortion attempt following a compromise of its Landesnetz, the shared network serving every Senate department and state agency; the attack became public knowledge on 2026-08-14 (translated from German) ([Berliner Zeitung, 2026-08-28](https://www.berliner-zeitung.de/article/cyberangriff-auf-berliner-senat-wegner-bestaetigt-erpressungsversuch-10337926)), the same day the two affected departments were disconnected from the network as a containment measure ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). Investigative reporting, not an official technical disclosure, is the first to name a mechanism: the attackers apparently gained access to the Landesnetz through an employee's click on a phishing email (translated from German) ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). Forensic investigators found the actual data exfiltration ran between 2026-08-07 and 2026-08-12 ([Security Affairs, 2026-08-29](https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html)), several days before the two affected departments were disconnected.

Der Spiegel reported, citing security-industry sources, that the ransomware group Rhysida is behind the attack ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)), an attribution Berlin's Senate administration has declined to confirm, citing investigative-tactical reasons ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)). Rhysida's own dark-web leak site independently posted an entry titled "Berlin, Germany" on 2026-08-28 claiming 5.79 terabytes of data across roughly 1.44 million files, including personal data on 12,076 individuals, more than 5,000 personnel files, plaintext credentials for internal systems, disciplinary and court records, Bundesrat committee protocols, and vulnerability analyses concerning Berlin's water supply ([Security Affairs, 2026-08-29](https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html)). Rhysida demanded 30 Bitcoin, about EUR 2 million (translated from German) ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)), with a one-week ultimatum running from 2026-08-28 (translated from German) ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)); Berlin's Governing Mayor Kai Wegner and Interior Senator Iris Spranger jointly confirmed the extortion attempt and publicly refused to pay, stating the state of Berlin will not submit to extortion ([Security Affairs, 2026-08-29](https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html)). Whether the affected systems were also encrypted, not only exfiltrated, is disputed: one outlet attributes to unnamed "experts" the claim that the Rhysida ransomware was the tool used to both encrypt the systems and steal the data (translated from German) ([BornCity, 2026-08-29](https://borncity.com/news/berlin-cyberangriff-rhysida-fordert-2-millionen-euro-fuer-57-tb-daten/)), while every other cited source describes only data theft and extortion without confirming encryption; this entry does not assert that encryption occurred.

CrowdStrike is conducting a forensic investigation across every Senate department and state agency network-wide, an effort Tagesspiegel's sources expect to take several more days ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). The department networks disconnected on 2026-08-14 were reconnected on 2026-08-23, but staff report continuing operational degradation days later, with many now working over private internet connections because the corporate network remains impaired; the same reporting flags that workaround as a new, self-inflicted security exposure ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). Rhysida has run this extortion pattern against public-sector targets before, including an earlier 2026 claim against the city of Stuttgart (translated from German) ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)); per the joint CISA/FBI/Multi-State ISAC advisory on the group, current as of its 2025-04-30 update, its initial-access techniques include compromising internal VPN access points using valid credentials at organizations lacking multi-factor authentication, and separately deploying Gootloader malware ([CISA, 2025-04-30](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a)).

**Defender takeaway:** the exposure pattern here, a single employee's phishing click reaching a shared administrative network broad enough to threaten a different department's critical-infrastructure and judiciary holdings, is directly transferable to any DACH shared-network government architecture, including Swiss cantonal and federal administrative networks: segment administrative domains so that one credential or endpoint compromise cannot reach unrelated departments' sensitive holdings, and verify that phishing-resistant multi-factor authentication and out-of-band verification cover every remote-access and VPN path that Rhysida's documented playbook targets.

**Triage:** the confirmed mechanism, a user-driven phishing-email click followed by multi-day bulk data exfiltration, surfaces at the point of delivery in mail-flow and attachment-sandboxing logs, and in network-egress and data-loss-prevention telemetry as a sustained high-volume outbound transfer from a single department's network segment; neither cited source states what executed after the click, so no process-level discriminator is offered here.

## Update — 2026-09-05T04:50:00Z

Rhysida's one-week ultimatum expired on 2026-09-04 at roughly 15:35 local time; the Berlin Senate had publicly committed not to pay, and about an hour after the deadline the group published the full stolen dataset on its darknet leak site, replacing the prior partial "auction" listing ([heise online, 2026-09-04](https://www.heise.de/news/Berliner-Senat-zahlt-nicht-sensible-Daten-jetzt-im-Darknet-11442286.html)). Chaos Computer Club spokesperson Joachim Selzer confirmed the complete dataset — including personnel files and documents Selzer describes seeing directly, such as employment references — is now publicly accessible to anyone. Whether the dataset actually contains the drinking-water vulnerability analyses and administration credentials the group had earlier claimed remains unverified by any party this entry cites: Left-party parliamentary faction leader Tobias Schulze stated the Senate now has the opportunity to check whether the prior assumptions about the leaked data are accurate, and should notify affected individuals and organizations as quickly as possible once it does. No further technical root-cause detail beyond the phishing vector has been disclosed by the Senate.

## Update — 2026-09-06T04:50:00Z

A structural consequence of this incident has now surfaced at the federal level. Asked in a Bundestag inquiry whether, given ongoing severe attacks on states and municipalities, the government would bring forward a constitutional amendment planned earlier by the previous coalition to make the BSI a true central authority for cyber incidents, the Federal Interior Ministry pointed only to the existing constitutional framework ([heise online, 2026-09-03](https://www.heise.de/news/Kehrtwende-bei-Cybersicherheit-Bund-gibt-Plan-fuer-BSI-Grundgesetzaenderung-auf-11440646.html)). Under that framework, the BSI may assist a state in defending against a serious cyberattack only after that state explicitly requests administrative assistance, and durable bilateral cooperation agreements (a precondition the ministry itself confirms do not yet exist with all 16 federal states) still gate faster support; in practice the BSI has repeatedly had to help first and formalise the legal basis afterward ([heise online, 2026-09-03](https://www.heise.de/news/Kehrtwende-bei-Cybersicherheit-Bund-gibt-Plan-fuer-BSI-Grundgesetzaenderung-auf-11440646.html)). The ministry points instead to its 14 existing cooperation agreements, its NIS2-transposition-driven expansion of BSI's powers, and increased staffing and budget as sufficient. Green-faction deputy chair Konstantin von Notz, who filed the inquiry, called the reversal "devastating for Germany's IT security" (translated from German) given the still-unfolding fallout from this exact incident. The tension is directly transferable to any federated cyber-incident-response model, including Switzerland's own federal/cantonal/communal cooperation structure with BACS: a central technical authority's ability to help is gated by a request-and-agreement process rather than by its own capacity to act.

Separately, on the incident itself, the Chaos Computer Club's Joachim Selzer identified specific record types now visible in the fully-published leak beyond the personnel-and-employment-reference material already recorded here: an internal request form for a new mobile phone bearing the requesting employee's handwritten signature, which Selzer noted gives a criminal a usable signature sample ([heise online, 2026-09-04](https://www.heise.de/news/Berliner-Senat-zahlt-nicht-sensible-Daten-jetzt-im-Darknet-11442286.html)).
