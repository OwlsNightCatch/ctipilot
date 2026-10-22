---
schema: 1
kind: research
title: "Cisco Talos: the \"demo.pdb\" BadIIS variant is commodity IIS-module malware for SEO fraud, likely sold among Chinese-speaking crime groups and built by the author \"lwxat\""
headline: "Cisco Talos: commodity \"demo.pdb\" BadIIS module for SEO fraud survives IIS restarts through a hidden backup copy"
summary: "Cisco Talos reported on 2026-05-19 that a BadIIS variant marked by \"demo.pdb\" strings, seen since 2024 mainly in the Asia-Pacific region and in a few cases in South Africa, Europe and North America, is commodity malware likely sold or shared among Chinese-speaking cybercrime groups, configured with a recovered builder for visitor redirection, crawler reverse proxying, content hijacking and backlink injection. Its installers register the malicious DLL in the IIS server module list, run as services impersonating Windows ones and keep a hidden backup copy that restores it on every IIS restart; Talos ties development since at least September 2021 to the alias \"lwxat\"."
discovered_at: "2026-05-20T05:00:10Z"
event_date: 2026-05-19
run_id: 2026-05-20-a0f7b07f
priority: notable
immediate_action: null
tags:
  - organized-crime
  - cryptocrime
regions:
  - apac
  - global
sectors:
  - technology
  - media
entities:
  - "campaign:cisco-talos-badiis-demo-pdb-maas-isapi-backdoor-lwxat-dragon"
techniques: [T1505.004, T1565.002, T1543.003, T1036.004, T1027, T1059.003, T1105, T1071.001]
affected_products: ["Microsoft IIS"]
cves: []
sources:
  - url: "https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/"
    publisher: "Cisco Talos"
    date: "2026-05-19"
    role: primary
closed_sources: []
evidence:
  - quote: "Based on the recovered builder and PDB strings, Talos assesses with moderate confidence that this \"demo.pdb\" variant is commodity malware, likely sold privately or shared within underground markets."
    publisher: Cisco Talos
    source_url: "https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/"
  - quote: "This ensures that the malicious BadIIS is automatically restored and launched every time the compromised IIS server is restarted."
    publisher: Cisco Talos
    source_url: "https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/"
  - quote: "Talos assesses with moderate-to-high confidence that the string \"lwxat\" is the author's alias or handle."
    publisher: Cisco Talos
    source_url: "https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/"
verification: single-source
sourcing_note: >
  A single Cisco Talos research post on its own investigations and recovered tooling; other vendors track BadIIS variants, but this ecosystem analysis
  and the "lwxat" attribution are Talos's alone, and Talos does not say how the servers were first compromised.
confidence: high
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
migrated_from: briefs/2026-05-20.md
updates:
  - at: "2026-10-21T20:44:17Z"
    run_id: 2026-10-21T1148Z-audit
    type: correction
    summary: >
      The demo.pdb BadIIS variant is a native IIS module registered in the server module list
      (globalModules and modules), not an ISAPI filter or extension loaded from web.config, and a hidden
      backup copy restores it on each IIS restart. Talos contrasts it with the BadIIS variants of
      DragonRank and UAT-8099 rather than placing it in their activity, and finds it difficult to
      attribute the attacks to a single actor; the lwxat alias rests on the builder's authentication
      string, a configuration parameter and a custom user agent. Talos does not describe how the IIS
      servers were first compromised.
    fields: [affected_products, body, classification, entities, event_date, evidence, headline, sources, sourcing_note, summary, techniques, title]
---

Since 2024 Talos has investigated attacks, mainly in the Asia-Pacific region and a few in South Africa, Europe and North America, that use a BadIIS variant marked by "demo.pdb" strings, which it assesses with moderate confidence is commodity malware sold privately or shared among several Chinese-speaking cybercrime groups under a malware-as-a-service model ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)). The BadIIS variants of the DragonRank and UAT-8099 groups Talos documented before relied on hardcoded C2 and statically compiled payloads, whereas this variant is configured with a recovered builder that injects parameters for JavaScript redirection of visitors to illicit sites, reverse proxying of illicit content to search-engine crawlers, site-wide content hijacking and backlink injection, and that encodes the C2 address with single-byte XOR ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)). Service-based installers from the same author impersonate Windows services such as Winlogin, FaxService or AudiosService, authenticate to a C2 server, download further payloads, hide their command lines with custom Base64 and register the BadIIS DLL in the globalModules and modules sections of the IIS configuration, and the latest copies the DLL to a hidden backup location so it is restored every time IIS restarts ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)). Talos ties development from at least September 2021 to January 2026, including a build to bypass Norton, to the alias "lwxat" with moderate-to-high confidence, from the builder's authentication string, a configuration parameter and a custom user agent seen in samples ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)). Talos does not describe how the attackers first gain access to the IIS servers.

**Exposure:** internet-facing Microsoft IIS servers that have already been compromised by means Talos does not describe; the victims it observed are mostly in the Asia-Pacific region ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)).

**Detection:** in the IIS server configuration, unknown native modules in the globalModules and modules sections; in the file system, a second copy of the module DLL in a hidden backup location; in service telemetry, new services named like Windows components that run command lines altering the IIS module list ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)). Deleting the DLL alone does not clean the server, because the backup copy returns it at the next IIS restart ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)).

**Defender takeaway:** operators of internet-facing IIS servers should check the server-level module list for modules they did not install; on a finding, remove the backup copy and the impersonating service along with the module, or BadIIS comes back at the next restart ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)).

## Correction — 2026-10-21T20:44:17Z

The variant is not an ISAPI filter or extension: its installers register the malicious DLL in the globalModules and modules sections of the IIS configuration at server level, and the latest one keeps a hidden backup copy that restores it every time IIS restarts, so the place to look is the server module list and the backup location ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)). Talos does not place it in DragonRank or UAT-8099 activity; it contrasts it with those groups' BadIIS variants, which used hardcoded C2 and static payloads, assesses it as commodity malware likely sold or shared among several Chinese-speaking cybercrime groups, and says the attacks are difficult to attribute to a single actor ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)). The "lwxat" alias rests on the builder's authentication string, a configuration parameter and a custom user agent, and Talos does not say how attackers first reach the IIS servers ([Cisco Talos, 2026-05-19](https://blog.talosintelligence.com/from-pdb-strings-to-maas-tracking-a-commodity-badiis-ecosystem/)).
