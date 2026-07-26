---
schema: 1
kind: incident
horizon: operational
title: "ANCPI Romania — DNSC interim report confirms vCenter-to-ESXi ransomware and exfiltration of ~2 million ePayment user records"
headline: "Romania's DNSC supersedes the 'databases not affected' line: the cadastre attack took the virtualization plane and two million payment records"
summary: >
  Romania's national cybersecurity directorate DNSC published an interim technical report on the
  ANCPI national land-registry attack that materially supersedes the agency's earlier "databases
  not affected" assurance. DNSC describes compromise of the authentication servers, entry into
  VMware vCenter, enumeration of all 1,083 virtual machines, deletion of roughly 100 of them and
  ransomware encryption of ESXi hosts — plus exfiltration of approximately two million ePayment
  platform user records (names, e-mail addresses, identifiers and password hashes). The "core
  database intact" claim survives only for the Oracle Exadata database specifically.
discovered_at: "2026-07-26T13:55:00Z"
event_date: "2026-07-22"
run_id: 2026-07-26T1308Z-audit
priority: notable
immediate_action: null
tags: [data-breach, ransomware, hacktivism]
regions: [europe]
sectors: [public-sector]
entities: [actor:bytetobreach, incident:ancpi-romania-cyberattack-2026-07]
techniques: [T1078, T1485, T1486, T1490, T1005]
affected_products: ["VMware vCenter Server", "VMware ESXi"]
cves: []
sources:
  - url: "https://www.go4it.ro/securitate-informatica/raport-dnsc-dupa-atacul-cibernetic-la-cadastru-vulnerabilitati-vechi-si-lipsa-antivirusului-pe-servere-au-expus-datele-a-doua-milioane-de-utilizatori-19280189/"
    publisher: "go4it.ro (relaying the DNSC interim technical report)"
    date: "2026-07-24"
    role: primary
  - url: "https://psnews.ro/raport-dnsc-dupa-incidentul-de-securitate-de-la-ancpi-cum-au-fost-compromise-aplicatiile-critice-ale-statului/"
    publisher: "PS News (relaying the same DNSC report)"
    date: "2026-07-24"
    role: corroborating
  - url: "https://www.go4it.ro/securitate-informatica/seful-dnsc-despre-atacul-cibernetic-de-la-cadastru-putea-fi-prevenit-hackerii-au-exploatat-vulnerabilitati-deja-cunoscute-19279543/"
    publisher: "go4it.ro (DNSC director statement)"
    date: "2026-07-18"
    role: corroborating
closed_sources: []
evidence:
  - quote: "atacatorii au extras aproximativ două milioane de înregistrări privind utilizatori ai platformei de plăți, care conțineau: nume; e-mailuri; identificatori; hash-uri ale parolelor"
    publisher: "PS News (relaying the same DNSC report)"
  - quote: "au compromis serverele de autentificare; au pătruns în VMware vCenter, adică sistemul care administrează întreaga infrastructură virtuală; au enumerat toate cele 1.083 de mașini virtuale; au executat mișcare laterală în rețea; au șters aproximativ 100 de mașini virtuale; au criptat servere ESXi cu ransomware"
    publisher: "PS News (relaying the same DNSC report)"
  - quote: "infrastructura ANCPI nu beneficia de un antivirus instalat pe serverele care rulau aplicațiile principale"
    publisher: "go4it.ro (relaying the DNSC interim technical report)"
  - quote: "nu există indicii că baza de date principală Oracle Exadata ar fi fost compromisă"
    publisher: "go4it.ro (relaying the DNSC interim technical report)"
verification: multi-source
sourcing_note: "The DNSC interim technical report is cited through two independent Romanian outlets that quote it directly rather than through a first-party DNSC page, so source reliability is rated B rather than the A a directly-fetched national-CERT publication would carry."
confidence: high
update_of: 2026-07-21/ancpi-romania-cadastre-databases-not-affected-update
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 1
watchlist_hit: false
actions: []
migrated_from: null
---

**UPDATE (originally covered 2026-07-19):** the picture of the attack on ANCPI, Romania's national cadastre and land-registration agency, has changed substantially. Earlier coverage recorded the agency's own position that its databases were not affected. Romania's national cybersecurity directorate DNSC has since published an interim technical report, relayed with direct quotation by Romanian technology press, that supersedes that framing on the point that matters most: the attackers extracted approximately two million records concerning users of the payment platform, containing names, e-mail addresses, identifiers and password hashes — in the report's Romanian, "atacatorii au extras aproximativ două milioane de înregistrări privind utilizatori ai platformei de plăți, care conțineau: nume; e-mailuri; identificatori; hash-uri ale parolelor" ([PS News, 2026-07-24](https://psnews.ro/raport-dnsc-dupa-incidentul-de-securitate-de-la-ancpi-cum-au-fost-compromise-aplicatiile-critice-ale-statului/)). The "databases not affected" assurance survives only in a much narrower form — DNSC states there is no indication the main Oracle Exadata database was compromised ([go4it.ro, 2026-07-24](https://www.go4it.ro/securitate-informatica/raport-dnsc-dupa-atacul-cibernetic-la-cadastru-vulnerabilitati-vechi-si-lipsa-antivirusului-pe-servere-au-expus-datele-a-doua-milioane-de-utilizatori-19280189/)) — which is a different claim from "no data was taken", since a separate payment-platform datastore demonstrably was.

The intrusion path DNSC describes is the one that makes a virtualized government estate fail all at once. Per the report the attackers compromised the authentication servers, penetrated VMware vCenter — the system administering the entire virtual infrastructure — enumerated all 1,083 virtual machines, executed lateral movement, deleted approximately 100 virtual machines and encrypted ESXi servers with ransomware ([PS News, 2026-07-24](https://psnews.ro/raport-dnsc-dupa-incidentul-de-securitate-de-la-ancpi-cum-au-fost-compromise-aplicatiile-critice-ale-statului/)). Identity compromise first, then the virtualization control plane, then destruction at the hypervisor layer beneath every guest operating system — the per-VM security stack never gets a vote. Source code for the eTerra, GIS, ePayment and security modules was taken from the agency's GitLab as well. DNSC's account of why it worked is unusually blunt for a national authority — the ANCPI infrastructure had no antivirus installed on the servers running its main applications ([go4it.ro, 2026-07-24](https://www.go4it.ro/securitate-informatica/raport-dnsc-dupa-atacul-cibernetic-la-cadastru-vulnerabilitati-vechi-si-lipsa-antivirusului-pe-servere-au-expus-datele-a-doua-milioane-de-utilizatori-19280189/)), alongside known unpatched vulnerabilities and a web-application firewall retaining connection logs for only seven minutes — which is also why the forensic picture is partial. DNSC's director had already assessed on 2026-07-18 that the attack exploited already-known vulnerabilities and could have been prevented ([go4it.ro, 2026-07-18](https://www.go4it.ro/securitate-informatica/seful-dnsc-despre-atacul-cibernetic-de-la-cadastru-putea-fi-prevenit-hackerii-au-exploatat-vulnerabilitati-deja-cunoscute-19279543/)).

**Defender takeaway:** for a European public-sector body running a comparable estate, the transferable lessons are the vCenter blast radius and the log-retention gap, not the victim. An administrative account that can reach vCenter is an account that can delete or encrypt every workload behind it, so vCenter and ESXi management interfaces belong on separate authentication and network paths from general server administration; and a WAF that keeps connection logs for seven minutes cannot answer the only question that matters after an incident. Note also the shape of the disclosure timeline: the victim's early "databases not affected" statement was accurate about one database and misleading about the incident, which is the normal pattern for first-week victim communications and a reason to treat them as provisional.

**Triage:** in vCenter and ESXi audit telemetry, the discriminating sequence is not any single administrative action but the ordering — an authentication from an unusual source or service account, followed by a full inventory enumeration of virtual machines, followed by power-off or delete operations across guests that share no application grouping. Routine administration enumerates inventory constantly and backup tooling touches many VMs, so volume alone is noise; the signal is enumeration by a principal that does not normally perform it, immediately followed by destructive operations spanning unrelated workloads.
