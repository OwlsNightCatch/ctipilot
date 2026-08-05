---
schema: 1
kind: incident
horizon: operational
title: "Switzerland's federal IT provider BIT confirms a SharePoint Server intrusion: ~200 federal user and technical accounts compromised while the July patches were already being installed"
headline: "Swiss federal SharePoint servers breached mid-patching — ~200 accounts taken, servers now being rebuilt"
summary: >
  The Bundesamt für Informatik und Telekommunikation (BIT), which runs the Swiss Confederation's own
  data centres, disclosed on 2026-08-04 that its on-premises Microsoft SharePoint Servers were
  compromised by unknown actors, presumably through the SharePoint flaws Microsoft disclosed in
  mid-July 2026, and that the credentials of roughly 200 accounts — user accounts and technical
  service accounts — were taken. BIT had begun installing the July updates immediately after release;
  staff spotted anomalies on 28 July and confirmed credential compromise on 31 July. Passwords were
  reset, internet access to SharePoint is blocked for non-federal users, and the affected servers are
  being rebuilt from scratch rather than patched in place.
discovered_at: "2026-08-05T04:12:23Z"
event_date: "2026-07-28"
run_id: 2026-08-05T0412Z-intel
priority: high
immediate_action: null
tags: [data-breach, vulnerabilities, identity, actively-exploited]
regions: [switzerland, europe]
sectors: [public-sector]
entities: [incident:foitt-bit-sharepoint-breach-2026-07]
techniques: [T1190, T1078]
affected_products: ["Microsoft SharePoint Server"]
cves: []
sources:
  - url: "https://www.admin.ch/de/newnsb/1CjmpBBHQaMV82PjKEpcL"
    publisher: "Der Bundesrat / Bundesamt für Informatik und Telekommunikation (BIT)"
    date: "2026-08-04"
    role: primary
  - url: "https://therecord.media/swiss-bit-foitt-hacked-possibly-sharepoint-vulnerabilities"
    publisher: "The Record (Recorded Future News)"
    date: "2026-08-04"
    role: corroborating
  - url: "https://www.cisa.gov/news-events/alerts/2026/07/14/cisa-urges-sharepoint-hardening-after-new-exploitations"
    publisher: "CISA"
    date: "2026-07-14"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Im Rahmen der Analyse des Vorfalls wurde festgestellt, dass rund 200 Konten kompromittiert wurden."
    publisher: "Der Bundesrat / Bundesamt für Informatik und Telekommunikation (BIT)"
  - quote: "Der Cyberangriff wurde durch bisher unbekannte Akteure ausgeführt, welche mutmasslich durch die Ausnutzung dieser Schwachstellen in der SharePoint-Software ermöglicht wurde."
    publisher: "Der Bundesrat / Bundesamt für Informatik und Telekommunikation (BIT)"
  - quote: "Am Dienstag, 28. Juli, haben Sicherheitsspezialistinnen und -spezialisten Auffälligkeiten auf den SharePoint-Servern des BIT bemerkt."
    publisher: "Der Bundesrat / Bundesamt für Informatik und Telekommunikation (BIT)"
  - quote: "Es gibt bislang keine Anzeichen dafür, dass Daten abgeflossen sind."
    publisher: "Der Bundesrat / Bundesamt für Informatik und Telekommunikation (BIT)"
verification: multi-source
sourcing_note: "BIT is the disclosing party for its own incident, and every incident-specific fact here — the ~200 accounts, the timeline, the rebuild decision — traces to BIT alone. The Record and CISA supply the wider exploitation wave’s machine-key post-exploitation mechanism, which is context rather than confirmation of this intrusion, so credibility is 2 rather than 1."
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: web-app-rce
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Rotate the ASP.NET machine keys on every on-premises SharePoint farm that was internet-reachable during the July exploitation window, and do it after evicting any resident web shell rather than before — a harvester still on the box simply re-reads the new keys."
  - "Re-authenticate and reset every service and technical account that holds credentials on an exposed SharePoint farm; these are the accounts least likely to be covered by interactive-logon MFA and the ~200 taken at BIT were user and technical accounts alike."
migrated_from: null
---

Switzerland's Bundesamt für Informatik und Telekommunikation — the federal IT service provider that operates the Confederation's own data centres — disclosed on 2026-08-04 that attackers reached its on-premises SharePoint Servers and took the credentials of roughly 200 accounts ([Der Bundesrat / BIT, 2026-08-04](https://www.admin.ch/de/newnsb/1CjmpBBHQaMV82PjKEpcL)). BIT names the actors as previously unknown and states the intrusion was *"mutmasslich"* — presumably — enabled by exploitation of the SharePoint flaws Microsoft disclosed in mid-July 2026; no source names a specific CVE for this intrusion, and none should be inferred. Both user accounts and technical service accounts were affected, passwords were reset immediately, and BIT states there is no indication that anything beyond those credentials was exfiltrated ([Der Bundesrat / BIT, 2026-08-04](https://www.admin.ch/de/newnsb/1CjmpBBHQaMV82PjKEpcL)).

**The timeline is the operationally interesting part, and it is uncomfortable.** BIT began installing the July security updates immediately after Microsoft released them. Security staff nonetheless noticed anomalies on the SharePoint servers on Tuesday 28 July, blocked internet access to SharePoint and closed the vulnerabilities once the suspicion was confirmed, and only during forensics on Friday 31 July established that account credentials had been compromised ([Der Bundesrat / BIT, 2026-08-04](https://www.admin.ch/de/newnsb/1CjmpBBHQaMV82PjKEpcL)). A patch programme that started on time still left a window in which an internet-facing farm was reachable and exploitable, and the compromise of credentials was confirmed three days after the anomaly itself. For any organisation measuring its own exposure by "we patched promptly", that gap is the lesson: promptness is measured against the attacker's start, not the vendor's release.

**Why a rebuild rather than a patch.** BIT is reinstalling the affected servers from scratch as a precaution and keeping internet access to SharePoint closed for non-federal users until that work completes, while federal staff keep internal access through alternative routes. The reason that is proportionate is visible in the wider wave: The Record reports that in this exploitation campaign attackers were extracting machine keys from Microsoft's Internet Information Services ([The Record, 2026-08-04](https://therecord.media/swiss-bit-foitt-hacked-possibly-sharepoint-vulnerabilities)), and CISA describes the same behaviour — stealing IIS machine keys and performing deserialization techniques to gain persistence and deploy malware ([CISA, 2026-07-14](https://www.cisa.gov/news-events/alerts/2026/07/14/cisa-urges-sharepoint-hardening-after-new-exploitations)). Machine keys sign and encrypt ASP.NET ViewState and session material, so an attacker holding them can mint tokens a fully updated server still accepts. Neither source states that this specific mechanism was used against BIT, and BIT does not describe post-exploitation activity — but it is the reason patching alone does not close out this class of intrusion, and rebuilding does.

**The credentials are the live risk, not the documents.** BIT notes that confidential information and specially protected personal data are not permitted on the SharePoint platform by federal policy, which bounds the data-exposure question. It does not bound the identity question: roughly 200 valid federal accounts, including technical accounts, are exactly the material an intruder converts into onward access elsewhere in the estate. Technical and service accounts are the sharper end of that — they typically authenticate non-interactively, are excluded from interactive-logon MFA, often carry broader-than-necessary rights, and their password rotation is frequently coupled to application configuration rather than to an identity lifecycle.

Detection concepts, telemetry class first. In web and application access logs on SharePoint front-ends, unauthenticated POSTs to SharePoint administrative endpoints are the exploitation attempt itself; CISA names AMSI signature classes for the ToolPane authentication-bypass and sign-out request-body patterns, and an AMSI hit on a SharePoint web application is the cheapest positive signal available ([CISA, 2026-07-14](https://www.cisa.gov/news-events/alerts/2026/07/14/cisa-urges-sharepoint-hardening-after-new-exploitations)). In process-creation telemetry with parent lineage, any child process under the IIS worker hosting a SharePoint application pool — a script interpreter, an encoded command line, a certificate or key utility — is anomalous on a healthy SharePoint server. In file and configuration telemetry, reads or exports of ASP.NET machine-key material outside a documented farm operation are the persistence step. In authentication telemetry after remediation, successful sessions carrying valid but unexpected tokens, and technical accounts authenticating from source hosts or at times inconsistent with their automation pattern, are what a forged-token or credential-reuse follow-on looks like. In egress telemetry, a collaboration server initiating outbound connections is worth a look on its own — a document server is a destination, not usually a client.

**Triage:** farm maintenance, Microsoft update installers and backup agents also spawn child processes under IIS-adjacent service accounts and also read farm configuration, so the child-process signal alone is noisy. The discriminators the cited guidance supports are whether the activity falls inside a scheduled maintenance window, whether the parent is the SharePoint timer or administration service rather than the internet-facing application-pool worker, whether the binary is signed and in its expected path, and whether a technical account is being used from more than the one source host it should ever appear on.

**Defender takeaway:** for on-premises SharePoint the order matters and it is not the intuitive one — patch, then hunt for and remediate intrusion artifacts, and rotate the machine keys last. CISA states it directly: before rotating IIS machine keys, hunt for and remediate any intrusion artifacts, including machine-key harvesters ([CISA, 2026-07-14](https://www.cisa.gov/news-events/alerts/2026/07/14/cisa-urges-sharepoint-hardening-after-new-exploitations)). Rotating first simply hands the new keys to whatever is still resident. CISA additionally names enabling AMSI integration for every SharePoint web application, in Full Mode for request-body scanning where the farm can carry it. Swiss operators have one further reference point here: BIT states it met its reporting deadline to the Bundesamt für Cybersicherheit and the Staatssekretariat für Sicherheitspolitik under the Informationssicherheitsgesetz, and then went beyond the duty by pushing the incident's technical indicators to Swiss critical-infrastructure operators through the BACS platform ([Der Bundesrat / BIT, 2026-08-04](https://www.admin.ch/de/newnsb/1CjmpBBHQaMV82PjKEpcL)). That is the federal reporting chain working as designed, and it is a usable model for cantonal bodies and CI operators mapping their own obligations.
