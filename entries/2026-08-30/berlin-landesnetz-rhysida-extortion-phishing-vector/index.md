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
updated_at: "2026-09-10T05:05:00Z"
event_date: "2026-08-28"
run_id: 2026-08-30T0410Z-intel
priority: high
immediate_action: null
tags: [ransomware, data-breach, phishing, organized-crime]
regions: [dach]
sectors: [public-sector]
entities: ["incident:berlin-landesnetz-compromise-2026-08", "actor:rhysida", "campaign:terminalfix-clickfix-reverse-tunnel-2026"]
techniques: [T1566, T1657, T1567.002]
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
  - url: "https://www.heise.de/news/BSI-warnt-nach-Daten-Leak-vor-erhoehter-Cyber-Bedrohung-11442510.html"
    publisher: "heise online"
    date: "2026-09-05"
    role: corroborating
  - url: "https://www.heise.de/news/Cyberangriff-Berlin-mit-Steuerungseinheit-will-Betroffene-kontaktieren-11442896.html"
    publisher: "heise online"
    date: "2026-09-06"
    role: corroborating
  - url: "https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile"
    publisher: "BSI (Bundesamt für Sicherheit in der Informationstechnik) — BITS-2026-287419-1032, v1.0"
    date: "2026-09-04"
    role: primary
  - url: "https://www.heise.de/news/BSI-erklaert-ersten-Angriffsvektor-auf-Berliner-Behoerden-11444072.html"
    publisher: "heise online (Nico Ernst)"
    date: "2026-09-07"
    role: corroborating
  - url: "https://www.heise.de/news/Gefahr-fuer-die-nationale-Sicherheit-Berliner-Datenleck-schlaegt-hohe-Wellen-11444301.html"
    publisher: "heise online (Stefan Krempl)"
    date: "2026-09-07"
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
  - quote: "In addition, data containing information on critical infrastructure, companies and organizations can, depending on the sensitivity of the data, also increase the threat level. (translated from German)"
    original: "Darüber hinaus können Daten, die Informationen zu kritischen Infrastrukturen, Unternehmen und Organisationen enthalten, je nach Sensibilität der Daten ebenfalls eine Erhöhung der Bedrohungslage bewirken"
    publisher: "BSI spokesperson, via heise online"
    source_url: "https://www.heise.de/news/BSI-warnt-nach-Daten-Leak-vor-erhoehter-Cyber-Bedrohung-11442510.html"
  - quote: "According to Der Tagesspiegel, the data reportedly also includes information on heating plants, fuel depots, backup-power facilities, substations, prisons, waterworks, as well as armaments companies and the Bundeswehr. (translated from German)"
    original: "Dem Tagesspiegel zufolge sollen sich darunter zudem Daten zu Heizkraftwerken, Tanklagern, Notstromanlagen, Umspannwerken, Gefängnissen, Wasserwerken sowie Rüstungsunternehmen und der Bundeswehr befinden."
    publisher: "heise online, citing Der Tagesspiegel"
    source_url: "https://www.heise.de/news/Cyberangriff-Berlin-mit-Steuerungseinheit-will-Betroffene-kontaktieren-11442896.html"
  - quote: "The state of Berlin acted grossly negligently and deliberately failed to comply with classified-information protection requirements. (translated from German)"
    original: "Das Land Berlin hat grob fahrlässig gehandelt und vorsätzlich die Geheimschutz-Vorgaben nicht eingehalten"
    publisher: "Manuel Atug (IT-security expert), via heise online (dpa)"
    source_url: "https://www.heise.de/news/Cyberangriff-Berlin-mit-Steuerungseinheit-will-Betroffene-kontaktieren-11442896.html"
  - quote: "That TerminalFix is the attack vector used by the Rhysida cybergang has been confirmed by the BSI in a Mastodon post. (translated from German)"
    original: "Dass es sich bei der Methode TerminalFix um den von der Cyberbande Rhysida genutzten Angriffsvektor handelt, hat das BSI in einem Beitrag bei Mastodon bestätigt."
    publisher: "heise online (Nico Ernst)"
    source_url: "https://www.heise.de/news/BSI-erklaert-ersten-Angriffsvektor-auf-Berliner-Behoerden-11444072.html"
  - quote: "This makes it clear: the Senate administrations for construction and transport were attacked via TerminalFix. (translated from German)"
    original: "Damit steht fest: Die Senatsverwaltungen für Bauen und Verkehr wurden per TerminalFix attackiert."
    publisher: "heise online (Nico Ernst)"
    source_url: "https://www.heise.de/news/BSI-erklaert-ersten-Angriffsvektor-auf-Berliner-Behoerden-11444072.html"
  - quote: "The Rhysida ransomware and leak site is attributed to the financially motivated group Vice Spider (aka Vice Society, WhiteNefas, White Hekate, DEV-0832, Vanilla Tempest). (translated from German)"
    original: "Die Ransomware und Leak-Seite Rhysida wird der finanziell motivierten Gruppe Vice Spider (aka Vice Society, WhiteNefas, White Hekate, DEV-0832, Vanilla Tempest) zugeordnet."
    publisher: "BSI (Bundesamt für Sicherheit in der Informationstechnik) — BITS-2026-287419-1032, v1.0"
    source_url: "https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile"
  - quote: "This data leak is of grave scope and endangers our national security."
    original: "Dieser Datenabfluss ist von gravierendem Ausmaß und gefährdet unsere nationale Sicherheit"
    publisher: "Roderich Kiesewetter (CDU defense-policy spokesperson), via Süddeutsche Zeitung, relayed by heise online"
    source_url: "https://www.heise.de/news/Gefahr-fuer-die-nationale-Sicherheit-Berliner-Datenleck-schlaegt-hohe-Wellen-11444301.html"
  - quote: "In an internal letter, he cites concerns, according to rbb, about near-unlimited data access, possible disruption to specialised administrative applications, and remaining monitoring risks for staff."
    original: "In einem internen Schreiben verweist er laut dem rbb auf Bedenken rund um einen nahezu unbegrenzten Datenzugriff, mögliche Störungen von Fachverfahren sowie verbleibende Überwachungsrisiken für die Dienstkräfte."
    publisher: "heise online, citing rbb24, on the Lichtenberg district's refusal to deploy CrowdStrike Falcon Agent"
    source_url: "https://www.heise.de/news/Gefahr-fuer-die-nationale-Sicherheit-Berliner-Datenleck-schlaegt-hohe-Wellen-11444301.html"
  - quote: "Berlin's data protection commissioner Meike Kamp and the security agencies advise those potentially affected to exercise increased vigilance. They recommend changing passwords, closely monitoring account activity, and increased scepticism toward phishing emails."
    original: "Die Berliner Datenschutzbeauftragte Meike Kamp sowie die Sicherheitsbehörden raten potenziell Betroffenen zu erhöhter Wachsamkeit. Sie empfehlen das Ändern von Passwörtern, die genaue Kontrolle von Kontoaktivitäten und erhöhte Skepsis gegenüber Phishing-E-Mails."
    publisher: "heise online, citing Berlin's Data Protection Commissioner Meike Kamp"
    source_url: "https://www.heise.de/news/Gefahr-fuer-die-nationale-Sicherheit-Berliner-Datenleck-schlaegt-hohe-Wellen-11444301.html"
verification: multi-source
sourcing_note: >
  The original phishing access vector and the Rhysida attribution were sourced only to
  investigative journalism (Der Tagesspiegel, Der Spiegel via heise online); Berlin's Senate
  administration has explicitly declined to name the attacker, citing investigative-tactical
  reasons. Germany's BSI (BITS-2026-287419-1032, 2026-09-04, confirmed via Mastodon the same day)
  now independently confirms both: the intrusion technique matches its own advisory's
  description of the TerminalFix campaign, and Rhysida is attributed to a group BSI tracks as
  Vice Spider — resolving what was previously a media-only attribution into a national-CERT
  technical confirmation. Whether the affected systems were also encrypted, not only exfiltrated,
  remains disputed: BornCity attributes an encryption claim to unnamed "experts", while every
  other cited source, BSI included, describes data theft and extortion without confirming
  encryption. The isolation/disclosure date itself is contradicted across sources and unresolved
  (see the body's Contradiction line): Der Tagesspiegel and rbb24 explicitly date the network
  disconnection to 2026-08-14; Berliner Zeitung dates the attack becoming publicly known to
  the same day without separately dating the disconnection itself. Security Affairs dates both
  the disconnection and Berlin's first public disclosure to 2026-08-17. The 2026-09-07 update's heise source adds a
  fourth account — a retrospective timeline dating isolation to 2026-08-14 (matching the
  German-language reporting) and a separate Senate chancellery press statement to
  2026-08-17 — which is consistent with the German-language sources on the isolation date but
  does not corroborate Security Affairs' claim that isolation itself happened on 2026-08-17.
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
  - at: "2026-09-07T04:47:00Z"
    run_id: 2026-09-07T0411Z-intel
    type: update
    summary: >
      Follow-up reporting establishes for the first time that the published leak extends well
      beyond personnel data: it includes records tied to district heating and power plants, fuel
      depots, backup-power installations, electrical substations, prisons and defense-industrial /
      Bundeswehr-related material. Germany's BSI issued a public warning of an elevated threat
      level from the leak — heightened targeted-phishing risk plus a hack-and-leak risk given
      Berlin's 20 September state election — while assessing the underlying intrusion itself as
      financially motivated. Berlin's government set up a dedicated coordination unit (BSI, BKA
      and the domestic intelligence service BfV jointly reviewing the material) and started a
      risk-based notification process for affected citizens, employees and companies.
    fields: [updated_at, sources, evidence, body]
  - at: "2026-09-08T04:49:00Z"
    run_id: 2026-09-08T0411Z-intel
    type: update
    summary: >
      Germany's BSI officially confirms, for the first time, both the intrusion technique and the
      actor attribution this entry had previously carried only from investigative journalism: the
      compromise matches BSI's own TerminalFix campaign advisory, and Rhysida is attributed to a
      group BSI tracks as Vice Spider (aka Vice Society, WhiteNefas, White Hekate, DEV-0832,
      Vanilla Tempest). BSI's advisory adds that operators staged exfiltration into
      attacker-controlled Azure cloud storage using the vendor's own azcopy tool and separately
      names the malware family LoremIpsumLoader (aka AxolotLoader) as attributed to the same
      group. Confidence moves from medium to high on the strength of this national-CERT technical
      confirmation.
    fields: [updated_at, entities, techniques, sources, evidence, sourcing_note, confidence, classification, body]
  - at: "2026-09-10T05:05:00Z"
    run_id: 2026-09-10T0410Z-intel
    type: update
    summary: >
      The leak's national-security framing sharpens: a CDU defense-policy spokesperson states the
      published dataset includes civil-defense/total-defense emergency plans and barracks
      documents alongside the critical-infrastructure material already recorded, prompting the
      Bundeswehr's own operational command to join BSI's review. Separately, the Berlin district of
      Lichtenberg has refused to deploy CrowdStrike's Falcon Agent on its own servers over
      data-access and monitoring concerns, and Berlin's data protection commissioner has issued
      concrete victim guidance.
    fields: [sources, evidence, body]
migrated_from: null
---

Germany's Berlin state administration is the target of a live extortion attempt following a compromise of its Landesnetz, the shared network serving every Senate department and state agency; Der Tagesspiegel and rbb24 both independently date the two affected departments' disconnection from the network, as a containment measure, to 2026-08-14 (translated from German) ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html); [rbb24, 2026-08-29](https://www.rbb24.de/politik/beitrag/2026/08/berlin-hackerangriff-landesnetz-loesegeld-forderung-erpresser.html)); Berliner Zeitung independently dates the attack becoming publicly known to the same day, stating the departments were disconnected shortly after the incident became known without giving a separate explicit date for the disconnection itself (translated from German) ([Berliner Zeitung, 2026-08-28](https://www.berliner-zeitung.de/article/cyberangriff-auf-berliner-senat-wegner-bestaetigt-erpressungsversuch-10337926)). **Contradiction:** Security Affairs instead states "Berlin first disclosed the compromise on August 17, isolating" the same two departments — dating both the public disclosure and the network isolation itself three days later than the German-language reporting ([Security Affairs, 2026-08-29](https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html)). This entry follows the 2026-08-14 date as the better-corroborated account (two independent German-language outlets against one English-language aggregator) without resolving the discrepancy. Investigative reporting, not an official technical disclosure, is the first to name a mechanism: the attackers apparently gained access to the Landesnetz through an employee's click on a phishing email (translated from German) ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). Forensic investigators found the actual data exfiltration ran between 2026-08-07 and 2026-08-12 ([Security Affairs, 2026-08-29](https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html)), several days before the two affected departments were disconnected.

Der Spiegel reported, citing security-industry sources, that the ransomware group Rhysida is behind the attack ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)), an attribution Berlin's Senate administration has declined to confirm, citing investigative-tactical reasons ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)). Rhysida's own dark-web leak site independently posted an entry titled "Berlin, Germany" on 2026-08-28 claiming 5.79 terabytes of data across roughly 1.44 million files, including personal data on 12,076 individuals, more than 5,000 personnel files, plaintext credentials for internal systems, disciplinary and court records, Bundesrat committee protocols, and vulnerability analyses concerning Berlin's water supply ([Security Affairs, 2026-08-29](https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html)). Rhysida demanded 30 Bitcoin, about EUR 2 million (translated from German) ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)), with a one-week ultimatum running from 2026-08-28 (translated from German) ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)); Berlin's Governing Mayor Kai Wegner and Interior Senator Iris Spranger jointly confirmed the extortion attempt and publicly refused to pay, stating the state of Berlin will not submit to extortion ([Security Affairs, 2026-08-29](https://securityaffairs.com/198064/cyber-crime/rhysida-ransomware-group-targets-berlin-government-ahead-of-vote.html)). Whether the affected systems were also encrypted, not only exfiltrated, is disputed: one outlet attributes to unnamed "experts" the claim that the Rhysida ransomware was the tool used to both encrypt the systems and steal the data (translated from German) ([BornCity, 2026-08-29](https://borncity.com/news/berlin-cyberangriff-rhysida-fordert-2-millionen-euro-fuer-57-tb-daten/)), while every other cited source describes only data theft and extortion without confirming encryption; this entry does not assert that encryption occurred.

CrowdStrike is conducting a forensic investigation across every Senate department and state agency network-wide, an effort Tagesspiegel's sources expect to take several more days ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). The department networks disconnected on 2026-08-14 were reconnected on 2026-08-23, but staff report continuing operational degradation days later, with many now working over private internet connections because the corporate network remains impaired; the same reporting flags that workaround as a new, self-inflicted security exposure ([Der Tagesspiegel, 2026-08-28](https://www.tagesspiegel.de/berlin/notfallplane-und-passworter-erbeutet-wegner-weist-erpresser-ultimatum-zuruck--hacker-fordern-laut-medienbericht-zwei-millionen-euro-15984600.html)). Rhysida has run this extortion pattern against public-sector targets before, including an earlier 2026 claim against the city of Stuttgart (translated from German) ([heise online, 2026-08-29](https://www.heise.de/news/30-Bitcoin-oder-Leak-Ransomware-Bande-erpresst-Berlin-11434325.html)); per the joint CISA/FBI/Multi-State ISAC advisory on the group, current as of its 2025-04-30 update, its initial-access techniques include compromising internal VPN access points using valid credentials at organizations lacking multi-factor authentication, and separately deploying Gootloader malware ([CISA, 2025-04-30](https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-319a)).

**Defender takeaway:** the exposure pattern here, a single employee's phishing click reaching a shared administrative network broad enough to threaten a different department's critical-infrastructure and judiciary holdings, is directly transferable to any DACH shared-network government architecture, including Swiss cantonal and federal administrative networks: segment administrative domains so that one credential or endpoint compromise cannot reach unrelated departments' sensitive holdings, and verify that phishing-resistant multi-factor authentication and out-of-band verification cover every remote-access and VPN path that Rhysida's documented playbook targets.

**Triage:** the confirmed mechanism, a user-driven phishing-email click followed by multi-day bulk data exfiltration, surfaces at the point of delivery in mail-flow and attachment-sandboxing logs, and in network-egress and data-loss-prevention telemetry as a sustained high-volume outbound transfer from a single department's network segment; neither cited source states what executed after the click, so no process-level discriminator is offered here.

## Update — 2026-09-05T04:50:00Z

Rhysida's one-week ultimatum expired on 2026-09-04 at roughly 15:35 local time; the Berlin Senate had publicly committed not to pay, and about an hour after the deadline the group published the full stolen dataset on its darknet leak site, replacing the prior partial "auction" listing ([heise online, 2026-09-04](https://www.heise.de/news/Berliner-Senat-zahlt-nicht-sensible-Daten-jetzt-im-Darknet-11442286.html)). Chaos Computer Club spokesperson Joachim Selzer confirmed the complete dataset — including personnel files and documents Selzer describes seeing directly, such as employment references — is now publicly accessible to anyone. Whether the dataset actually contains the drinking-water vulnerability analyses and administration credentials the group had earlier claimed remains unverified by any party this entry cites: Left-party parliamentary faction leader Tobias Schulze stated the Senate now has the opportunity to check whether the prior assumptions about the leaked data are accurate, and should notify affected individuals and organizations as quickly as possible once it does. No further technical root-cause detail beyond the phishing vector has been disclosed by the Senate.

## Update — 2026-09-06T04:50:00Z

A structural consequence of this incident has now surfaced at the federal level. Asked in a Bundestag inquiry whether, given ongoing severe attacks on states and municipalities, the government would bring forward a constitutional amendment planned earlier by the previous coalition to make the BSI a true central authority for cyber incidents, the Federal Interior Ministry pointed only to the existing constitutional framework ([heise online, 2026-09-03](https://www.heise.de/news/Kehrtwende-bei-Cybersicherheit-Bund-gibt-Plan-fuer-BSI-Grundgesetzaenderung-auf-11440646.html)). Under that framework, the BSI may assist a state in defending against a serious cyberattack only after that state explicitly requests administrative assistance, and durable bilateral cooperation agreements (a precondition the ministry itself confirms do not yet exist with all 16 federal states) still gate faster support; in practice the BSI has repeatedly had to help first and formalise the legal basis afterward ([heise online, 2026-09-03](https://www.heise.de/news/Kehrtwende-bei-Cybersicherheit-Bund-gibt-Plan-fuer-BSI-Grundgesetzaenderung-auf-11440646.html)). The ministry points instead to its 14 existing cooperation agreements, its NIS2-transposition-driven expansion of BSI's powers, and increased staffing and budget as sufficient. Green-faction deputy chair Konstantin von Notz, who filed the inquiry, called the reversal "devastating for Germany's IT security" (translated from German) given the still-unfolding fallout from this exact incident. The tension is directly transferable to any federated cyber-incident-response model, including Switzerland's own federal/cantonal/communal cooperation structure with BACS: a central technical authority's ability to help is gated by a request-and-agreement process rather than by its own capacity to act.

Separately, on the incident itself, the Chaos Computer Club's Joachim Selzer identified specific record types now visible in the fully-published leak beyond the personnel-and-employment-reference material already recorded here: an internal request form for a new mobile phone bearing the requesting employee's handwritten signature, which Selzer noted gives a criminal a usable signature sample ([heise online, 2026-09-04](https://www.heise.de/news/Berliner-Senat-zahlt-nicht-sensible-Daten-jetzt-im-Darknet-11442286.html)).

## Update — 2026-09-07T04:47:00Z

Follow-up reporting establishes for the first time that the scope of the published leak extends well beyond the personal data first identified. Citing Der Tagesspiegel, heise reports the dataset also includes information on district-heating and power plants, fuel depots, backup-power installations, electrical substations, prisons, waterworks, and armaments companies and the Bundeswehr (translated from German) ([heise online, 2026-09-06](https://www.heise.de/news/Cyberangriff-Berlin-mit-Steuerungseinheit-will-Betroffene-kontaktieren-11442896.html)) — a materially broader critical-infrastructure and defense-industrial exposure than the water-supply-vulnerability material Rhysida itself had claimed at disclosure.

Germany's BSI issued a public warning on 2026-09-05 of an elevated threat level stemming from the leak. The agency states data containing information on critical infrastructure, companies and organizations can, depending on its sensitivity, also increase the threat level (translated from German) ([heise online, 2026-09-05](https://www.heise.de/news/BSI-warnt-nach-Daten-Leak-vor-erhoehter-Cyber-Bedrohung-11442510.html)), and separately warns of heightened targeted-phishing risk against anyone who had contact with affected individuals or institutions ([heise online, 2026-09-05](https://www.heise.de/news/BSI-warnt-nach-Daten-Leak-vor-erhoehter-Cyber-Bedrohung-11442510.html)). BSI additionally flags a hack-and-leak risk specific to the political calendar: Berlin holds a state-parliament election on 20 September 2026, and stolen documents can be released or recontextualized at a moment favorable to an attacker ([heise online, 2026-09-05](https://www.heise.de/news/BSI-warnt-nach-Daten-Leak-vor-erhoehter-Cyber-Bedrohung-11442510.html)). BSI assesses the underlying intrusion itself as financially rather than politically motivated ([heise online, 2026-09-05](https://www.heise.de/news/BSI-warnt-nach-Daten-Leak-vor-erhoehter-Cyber-Bedrohung-11442510.html)) — an assessment attributed to BSI, distinct from opposition politicians' own separately reported alarm about the incident's severity.

Berlin's government responded on 2026-09-06 by establishing a dedicated coordination unit ("Steuerungseinheit") in which BSI, the Federal Criminal Police Office (BKA) and the domestic intelligence service (BfV) jointly review and assess the leaked material, and by starting a risk-based notification process to contact affected citizens, employees and companies by letter or email ([heise online, 2026-09-06](https://www.heise.de/news/Cyberangriff-Berlin-mit-Steuerungseinheit-will-Betroffene-kontaktieren-11442896.html)). Independent IT-security expert Manuel Atug separately stated that the state of Berlin acted grossly negligently and deliberately failed to comply with classified-information protection requirements (translated from German), adding that he had already flagged the same security gaps to Berlin's parliamentary interior committee in 2023 and 2025 ([heise online, 2026-09-06](https://www.heise.de/news/Cyberangriff-Berlin-mit-Steuerungseinheit-will-Betroffene-kontaktieren-11442896.html)). **Contradiction:** the heise 2026-09-06 timeline separately dates full network reconnection to 2026-08-24, one day later than the 2026-08-23 date this entry's main analysis attributes to Der Tagesspiegel; both dates are carried without resolving the one-day gap.

The same 2026-09-06 report adds a fourth account of the date sequence: its own retrospective timeline states the two affected Senate departments were isolated from the Landesnetz on 2026-08-14 — matching Der Tagesspiegel and Berliner Zeitung's dating of the isolation, not Security Affairs' 2026-08-17 — and separately states the Senate chancellery's public press statement disclosing the "ICT incident" followed on 2026-08-17 (translated from German) ([heise online, 2026-09-06](https://www.heise.de/news/Cyberangriff-Berlin-mit-Steuerungseinheit-will-Betroffene-kontaktieren-11442896.html)). This distinguishes network isolation (2026-08-14, now three independent accounts) from the Senate's own formal press disclosure (2026-08-17) as two separate events, but Security Affairs' claim that the isolation itself happened on 2026-08-17 remains an unresolved discrepancy with the German-language reporting, not one this update can settle.

## Update — 2026-09-08T04:49:00Z

Germany's BSI published an advisory on 2026-09-04 describing the compromise of an anonymized "state institution" whose technique matches the multi-stage TerminalFix campaign Microsoft documented on 2026-08-28 — the advisory itself never names Berlin ([BSI, BITS-2026-287419-1032, 2026-09-04](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile)). The same day, BSI posted on its official Mastodon account that it was intensively involved in handling the Berlin incident and separately linked to its detailed TerminalFix security notice; heise reports that juxtaposition as confirmation that TerminalFix is specifically the attack vector the Rhysida operators used against Berlin's two affected Senate administrations ([heise online, citing BSI, 2026-09-07](https://www.heise.de/news/BSI-erklaert-ersten-Angriffsvektor-auf-Berliner-Behoerden-11444072.html)) — the first technical confirmation, reported by heise, of both the access vector and the attribution this entry had previously carried only from investigative journalism. BSI attributes the Rhysida ransomware and leak site to a financially motivated group it tracks as Vice Spider, cross-referenced against the aliases Vice Society, WhiteNefas, White Hekate, DEV-0832 and Vanilla Tempest, active since at least mid-2021 and using the Rhysida ransomware and leak site almost exclusively since June 2023 ([BSI, BITS-2026-287419-1032, 2026-09-04](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile)). BSI's advisory adds a detail beyond what Microsoft's original write-up described: reporting organizations told BSI that TerminalFix operators have staged exfiltration into attacker-controlled cloud storage, for example Azure, using the cloud provider's own transfer tooling such as azcopy ([BSI, BITS-2026-287419-1032, 2026-09-04](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile)). BSI further states that incident reports place a malware family it names LoremIpsumLoader (also known as AxolotLoader) within the campaign, and attributes that loader to the same group responsible for Rhysida ([BSI, BITS-2026-287419-1032, 2026-09-04](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile)). BSI assesses the campaign as opportunistic, purely financially motivated cybercrime with no established link to a state or politically motivated actor, and states Rhysida shows no particular regional focus on Germany, concentrating instead on education and healthcare, with public administration a more distant top-five target sector ([BSI, BITS-2026-287419-1032, 2026-09-04](https://www.bsi.bund.de/SharedDocs/Cybersicherheitswarnungen/DE/2026/2026-287419-1032.pdf?__blob=publicationFile)).

## Update — 2026-09-10T05:05:00Z

CDU defense-policy spokesperson Roderich Kiesewetter told Süddeutsche Zeitung "this data leak is of grave scope and endangers our national security" (translated from German), naming civil-defense and total-defense emergency plans and barracks documents as part of the published dataset alongside the critical-infrastructure material already recorded here; Germany's Bundeswehr Operative Führungskommando and the Nationales Cyberabwehrzentrum have joined BSI in reviewing the security fallout ([heise online, citing Süddeutsche Zeitung, 2026-09-07](https://www.heise.de/news/Gefahr-fuer-die-nationale-Sicherheit-Berliner-Datenleck-schlaegt-hohe-Wellen-11444301.html)). Separately, the Berlin district of Lichtenberg has refused to deploy CrowdStrike's Falcon Agent on its own servers: "in an internal letter, he cites concerns, according to rbb, about near-unlimited data access, possible disruption to specialised administrative applications, and remaining monitoring risks for staff" (translated from German), while the district states it has found no evidence of intrusion on its own systems and is demanding the Senate assume full responsibility and cost for the response ([heise online, citing rbb24, 2026-09-07](https://www.heise.de/news/Gefahr-fuer-die-nationale-Sicherheit-Berliner-Datenleck-schlaegt-hohe-Wellen-11444301.html)). Berlin's data protection commissioner Meike Kamp has now issued concrete guidance for potentially affected individuals: "change passwords, closely monitor account activity, and increased scepticism toward phishing emails" (translated from German) ([heise online, citing Meike Kamp, 2026-09-07](https://www.heise.de/news/Gefahr-fuer-die-nationale-Sicherheit-Berliner-Datenleck-schlaegt-hohe-Wellen-11444301.html)).

**Defender takeaway:** the Lichtenberg dispute is a transferable governance lesson for any DACH federated administration, Swiss cantonal/communal architecture included — an incident-response tool that needs broad endpoint data access can itself become a point of inter-departmental conflict when trust in central IT governance is already damaged, so decide the incident-response tooling and data-access model before an incident forces the question under public pressure.
