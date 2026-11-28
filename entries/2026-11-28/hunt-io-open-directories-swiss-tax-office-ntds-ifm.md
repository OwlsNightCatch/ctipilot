---
schema: 1
kind: threat
title: "Hunt.io: exposed attacker directories show a crew staging a Swiss tax office's domain-controller database through ntdsutil install-from-media, a Java loader posing as the SQL Server JDBC driver and an exploit kit for edge services; the Swiss victim is unnamed, the access route is not shown and complete transfer is unconfirmed"
headline: "Hunt.io: crew staged a Swiss tax office's AD database via ntdsutil IFM; fake JDBC driver loader; edge exploit kit"
summary: >
  Hunt.io recovered three exposed attacker directories and reports a domain-controller workflow against "a Swiss tax office": a log of ntdsutil install-from-media creation and a script that copies the Active Directory database and registry hives from a controller share to staging, decodes them and requests removal of the media. Complete off-host transfer is not confirmed, the victim is unnamed and the report does not show how access was gained. The kit also holds a Java loader registered as a Microsoft SQL Server JDBC driver, Apollo- and Poseidon-derived implants, a commercial employee-monitoring product used as a command channel and staged exploits for edge services that Hunt.io says show availability, not success; it assesses a financially motivated, Chinese-speaking, Southeast Asia-based crew and names no group.
discovered_at: "2026-11-28T05:01:00Z"
updated_at: null
event_date: "2026-11-25"
run_id: 2026-11-28T0355Z-intel
priority: notable
immediate_action: null
tags: [organized-crime]
regions: [switzerland, us]
sectors: [public-sector]
entities: ["product:microsoft-active-directory"]
techniques: [T1003.003, T1039, T1557.001, T1059.003, T1071.001, T1219]
affected_products: ["Microsoft Active Directory"]
cves: []
sources:
  - url: "https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms"
    publisher: "Hunt.io"
    date: "2026-11-25"
    role: primary
closed_sources: []
evidence:
  - quote: "a Bangladeshi university's Kerberos material exported at scale, and a Swiss tax office's domain database and hives staged off an internal share. Neither is US."
    publisher: "Hunt.io"
    source_url: "https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms"
  - quote: "A log reports ntdsutil install-from-media creation; a script copies the domain database and registry hives from a controller share to staging, XOR-decoding bytes with 0xA5, then requests IFM removal."
    publisher: "Hunt.io"
    source_url: "https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms"
  - quote: "Complete off-host transfer is not independently confirmed."
    publisher: "Hunt.io"
    source_url: "https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms"
  - quote: "University material already contains monitoring access and credentials; the Swiss output begins after execution is available. Neither explains how access was first obtained."
    publisher: "Hunt.io"
    source_url: "https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms"
  - quote: "Their presence establishes availability, not successful operation against any named target."
    publisher: "Hunt.io"
    source_url: "https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms"
  - quote: "We read this as a Chinese-speaking, Southeast Asia-based cybercrime operation running a Russian-authored toolkit."
    publisher: "Hunt.io"
    source_url: "https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms"
verification: single-source
sourcing_note: >
  Hunt.io is the only source and reads the operators' own recovered files; no Swiss authority, the victim or any other outlet corroborates the Swiss material, and two searches for a second source found none. The report calls the victim only "a Swiss tax office": it names no canton, commune or federal body, so the level of government is not stated and the victim could be any of them. Hunt.io says it notified CISA before publishing and does not say whether any Swiss body was told. The attribution is Hunt.io's assessment from language and timezone indicators and it calls it not a validated attribution. The report's internal domain label and addresses for the Swiss environment are deliberately left out here.
confidence: medium
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 3
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Hunt.io recovered the contents of three exposed open directories and, reading the operators' own files, reports a domain-controller workflow against a Swiss tax office: a log records ntdsutil install-from-media creation, and a script copies the domain database and the registry hives from a controller share to a staging area, decodes them with a single-byte XOR and then requests removal of the install-from-media set ([Hunt.io, 2026-11-25](https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms)). Hunt.io says complete off-host transfer is not independently confirmed, that an NTLM-relay run against an internal LDAP service belongs to the same environment, and that the Swiss output begins after code execution was already available, so how the crew first got in is not shown ([Hunt.io, 2026-11-25](https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms)). The report names no canton, commune or federal body, and Hunt.io says it notified CISA before publishing ([Hunt.io, 2026-11-25](https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms)).

The same files hold a Java class registered as a `java.sql.Driver` service provider that poses as Microsoft's SQL Server JDBC driver: its boot routine runs when an application loads the JAR, with no scheduled task needed, and either polls an HTTPS endpoint on TCP 8443 for commands passed to `cmd.exe` or decodes a packed file into an Apollo-derived Windows executable written under the Java temp directory and started from Java ([Hunt.io, 2026-11-25](https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms)). Hunt.io also describes a Poseidon-derived Linux implant behind a server labelled Mythic, a commercial employee-monitoring product whose agents the operators drive with custom clients, and a reconnaissance stage that sends base64-encoded output in chunks inside GET request paths; it says the artifacts show a Poseidon-derived build, which does not establish that it ran on an external victim, and an Apollo derivation with no verified runtime command-and-control configuration ([Hunt.io, 2026-11-25](https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms)). Staged exploits cover edge and remote-access services, among them Citrix NetScaler (CVE-2025-5777), FreePBX (CVE-2025-57819) and PHP2Shell (CVE-2026-109618 and CVE-2026-109619), and Hunt.io states that their presence establishes availability, not successful operation against any named target ([Hunt.io, 2026-11-25](https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms)). Hunt.io reads the operation as a Chinese-speaking, Southeast Asia-based cybercrime crew running a Russian-authored toolkit and ties it to no named group and no state sponsor ([Hunt.io, 2026-11-25](https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms)).

**Exposure:** Active Directory domain controllers and Java application servers that load third-party JARs; Hunt.io's other victims are a US hospital system, a US manufacturer and a Bangladeshi university; law firms and US federal agencies are mainly reconnaissance targets, and one law firm was attacked without success ([Hunt.io, 2026-11-25](https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms)).

**Detection:** on domain controllers, ntdsutil install-from-media creation that no administrator requested, followed by reads of the database and the SYSTEM and SECURITY hive copies from the share by another host and a removal of the media; NTLM relay and coercion activity against domain controllers; on Java application servers, a JAR whose service-provider descriptor names a `com.microsoft.sqlserver.jdbc` class that matches no vendor build, `java` writing an executable under the temp directory and then starting a child process, and HTTPS polling from application servers to TCP 8443; in proxy logs, GET paths carrying long base64 chunks ([Hunt.io, 2026-11-25](https://hunt.io/blog/open-directory-us-hospital-manufacturer-law-firms)).

**Defender takeaway:** hunt domain controllers for install-from-media creation and share-staged copies of the directory database and hives, and enforce SMB signing and LDAP channel binding, which Hunt.io names as the hardening against the relay and coercion tooling; review Java servers for unexpected JDBC providers, and treat the Swiss victim claim as a single-source reading of recovered files until a Swiss body or the victim comments.
