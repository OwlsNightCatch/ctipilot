**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-09T04:49:11Z · ended_at=2026-10-09T05:04:50Z · duration_seconds=939

## Verification report — 2026-10-09T0255Z-intel (iteration 4)

Scope walked: the whole ledger, 163 of 163 claims (all 8 of `claims.changed.iter4.yaml`, every claim of Publica, AA26-281A, TraderTraitor and 88771, and every claim of 88779, 107406, Talos and ReliaQuest; no sampling). Rows in `verification.iter4.claims.yaml` (162 ok, 1 F3). Every cited page was fetched this iteration: extract, pdf, cisa-kev, `ncsc-csh recent`, the Citrix community RSS feed and jina for the two community permalinks that answer 403 to extract, and a raw GET for the PK Softech footer, the S2-032 dateline and the ACSC 3 October update. Beyond the ledger I read the registry diff, the backlog diff and the run-record notes, re-listed the NCSC-CH hub and the CISA advisories listing (nothing newer than AA26-281A), and checked the store for duplicates of each new subject.

### Prior-iteration deltas (each remediation re-checked against the live source)

1. Publica F3: correct. PK Softech's page reads "Nach heutigem Kenntnisstand muss davon ausgegangen werden, dass Daten aus unseren Systemen abgeflossen sind" and the entry's summary and body now say "it must be assumed"; the Confederation's part (detected the attack, informed other customers, Federal Prosecutor's Office) is stated separately and matches admin.ch. The new ground clause ("the supplier serves a federal institution and holds its staff's data") is uncited and stronger than the sources (finding #4). The same hedge loss stands in the registry text (finding #1).
2. AA26-281A F9: correct as worded. KEV: "attackers with access to the admin panel"; Strapi's disclosure: PR:N and "unauthenticated users could exploit this vulnerability", fixed in 4.8.0; the note no longer says the CVE record follows Strapi.
3. TraderTraitor F8: partly done. "Microsoft Windows" added and `affected_products` named in the record's `fields`; Linux, equally documented by Zscaler, not added (finding #6).
4. AA26-281A 'among others': correct (advisory: "Flax Typhoon, Ethereal Panda, and Red Juliett, among others"; NCSC UK the same).
5. 88771 actions[0] pointer: correct against CTX697191 (IdP fixed at 14.1-73.46 / 13.1-64.29); the record's `fields` name `actions`; every changed line of `git diff HEAD` is covered by `fields`.
6. Left on purpose, judged: T1199 stays advisory (finding #9); the ReliaQuest clause is not a pure disambiguation, see finding #7.

### Citation does not support the claim

#1 (F3) `entities/registry.yaml`, `incident:pk-softech-publica-cyberattack-2026-09`, summary: "PK Softech and the Confederation confirm data left the supplier's systems". PK Softech: "muss davon ausgegangen werden". The entry was fixed at iteration 3; the registry text (rendered on the entity page) was not. Fix: "the Confederation says data left the supplier's systems; PK Softech says it must be assumed".

#2 (F3, low confidence) AA26-281A body: "Initial access has mostly come since January 2021 from command-line exploit utilities and from a cross-site-scripting payload". Advisory: "primarily through command line utilities ... Additionally ... XSS attacks". Fix: primary versus additional.

### Claims missing inline citation

#4 (F5, low confidence) Publica body, closing clause: "the supplier serves a federal institution and holds its staff's data" is uncited; admin.ch says the extent of Publica data affected is being clarified, Netzwoche "könnten betroffen sein"; no source says the supplier holds it. Suggested: "the supplier's software runs the federal pension fund's administration (Netzwoche), whose insured include federal and ETH staff".

### Needs more research

#5 (F8, low confidence) Publica: admin.ch "Keine anderen Bundesstellen pflegen Geschäftsbeziehungen mit dem Unternehmen" (watson and Netzwoche repeat it) scopes the Exposure and action 2; omitted.

#6 (F8, low confidence) TraderTraitor `affected_products` lacks Linux (Zscaler: "selects payloads for macOS, Linux, and Windows").

### Surface contradiction

#3 (F9, low confidence) Publica title/headline/sourcing_note treat the outflow as settled ("let data leave", "data left", "agree on ... the data outflow"). admin.ch is headlined "Datenabfluss bestätigt"; PK Softech "must be assumed"; Publica's spokesperson (watson, Netzwoche) "Ob und welche Daten ... tatsächlich abgeflossen sind, ist allerdings noch unklar". The body carries only the last; add one contradiction clause and soften the three fields.

### Name-collision unflagged

#7 (F15, low confidence) ReliaQuest: "no source links to other projects of that name, such as the Cairn exploitation engine in Gambit Security's reporting or Talos' CAIRN toolkit". Talos' CAIRN is distinct; for Gambit's Cairn ("autonomous penetration testing engine. It receives target domains and an objective ... runs for hours until it achieves the objective") versus ReliaQuest's ("legitimate open-source orchestration platform for coordinating AI agents", "dispatches AI coding agents against an objective") nothing shows two projects. Say "no source says whether it is the same project as ..." or add a `references[]` link.

### Editorial / less-is-more flags (advisory)

#8 (F11, low confidence) Entity linking: FLATROOF and ROOFDECK (TraderTraitor update now has a second publisher) and the Talos/ESET subjects (FRUITSHELL, PLOTSAFE, HOLLOWCLAD, MANTLEMAZE, MATCHBOIL) have no registry record or key. May be left for the audit.

#9 (F11) Publica T1199: no cited source says the attackers used a trusted relationship; closest non-empty mapping, documented in the run record. May be left.

### Checked and clean (no finding)

Every evidence quote on the new and updated entries is verbatim on its live page (translations of the three German Publica quotes faithful). CVE ids, CVSS and version tables for CVE-2026-107406 (CTX697191), CVE-2026-88779 (CTX697174) and the eight AA26-281A CVEs (Appendix B, KEV 2026.10.08, Apache S2-032, Strapi disclosure) match their per-CVE authority. All five KEV additions of 2026-10-08 are covered; ILIAS, SonicWall SMA1000, FortiMail, Cisco SD-WAN and Atlassian are covered by earlier entries. Priorities hold (Publica routine; 107406, AA26-281A, Talos, ReliaQuest notable; 88779 high unchanged); classification codes agree with sources.json; `verification` values and sourcing notes fit the source counts; changelog contract for the three updated entries holds (`updated_at` mirrors, sections match records, no silent edit, no supersession defect); no IOCs, no em dash outside headings, no workflow vocabulary; run-record notes (KEV sweep, backlog rows and expiries, counts, dispositions, bridge uses) hold on disk. Gate re-run: only the two Phase 6 bookkeeping failures (residual count, completed/duration re-stamp).

Missed angles: none found. The KEV catalogue (2026.10.08) carries only the five AA26-281A additions; the CISA advisories listing has nothing newer than AA26-281A; NCSC-CH hub posts since 2026-10-06 are covered or deliberately dropped; two web searches (exploited zero-days of 8 October; Swiss administration incidents in October) returned nothing in-window. Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 4, advisory: 2). Seven of the nine items are marked low confidence; finding #1 is evidenced and cheap to fix.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: incident
  item: "entities/registry.yaml incident:pk-softech-publica-cyberattack-2026-09 (summary; entity page text, registry addition of this run)"
  url_or_quote: "registry summary: \"PK Softech and the Confederation confirm data left the supplier's systems\" vs https://pksoftech.ch/de/newsreader/Cyberangriff-auf-die-PKSoftechAG: \"Nach heutigem Kenntnisstand muss davon ausgegangen werden, dass Daten aus unseren Systemen abgeflossen sind.\""
  summary: "Same hedge loss the entry itself had at iteration 3 (fixed there, still standing in the registry text readers see on the entity page): PK Softech says only that it must be assumed data left; the Confederation's release is headlined 'Datenabfluss bestätigt'; Publica's spokesperson (watson, Netzwoche) says whether and which data actually left is unclear. Reword to 'the Confederation says data left the supplier's systems; PK Softech says it must be assumed'."
- code: F3
  category: claim-not-supported
  section: threat
  item: "2026-10-09/aa26-281a-integrity-tech-microscan-exchange-mail-theft (claim 8ae5c2f94e, body paragraph 2) (low confidence)"
  url_or_quote: "body: \"Initial access has mostly come since January 2021 from command-line exploit utilities and from a cross-site-scripting payload that overlays a login form\" vs https://www.ic3.gov/CSA/2026/261008.pdf: \"Since at least mid-January 2021, the threat actors have gained access to victim networks and cloud-based services primarily through command line utilities built on exploit codes ... Additionally, the threat actors have used JavaScript and HTML code to execute cross-site scripting (XSS) attacks.\""
  summary: "(low confidence) The advisory makes the command-line exploit utilities the primary access route and XSS an additional one; the sentence puts both under 'mostly' and the January 2021 date. Reword to 'primarily from command-line exploit utilities, and additionally from a cross-site-scripting payload ...'."
- code: F9
  category: surface-contradiction
  section: incident
  item: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow (title, headline, sourcing_note) (low confidence)"
  url_or_quote: "title: \"malware at its administration-software supplier PK Softech let data leave the supplier's systems\"; headline: \"data left\"; sourcing_note: \"The Confederation's release and the supplier's own notice agree on the intrusion and the data outflow\""
  summary: "(low confidence) Sources differ in confidence and the entry picks the strong reading in its most visible fields: admin.ch is headlined 'Datenabfluss bestätigt' and Netzwoche's lead says 'Dabei sind Daten abgeflossen, wie der Bund schreibt'; PK Softech says 'muss davon ausgegangen werden'; Publica's spokesperson (watson, Netzwoche) says 'Ob und welche Daten ... tatsächlich abgeflossen sind, ist allerdings noch unklar'. The body carries only the Netzwoche 'unclear' fact and never says the Confederation's release calls the outflow confirmed. Add a one-clause contradiction line in the body (Confederation: confirmed; PK Softech: must be assumed; Publica: scope unclear) and soften 'agree on ... the data outflow' and the title/headline ('data outflow reported')."
- code: F5
  category: missing-citation
  section: incident
  item: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow (body, closing clause of paragraph 1) (low confidence)"
  url_or_quote: "\"the supplier serves a federal institution and holds its staff's data.\""
  summary: "(low confidence) The ground clause added at iteration 3 is uncited and states more than the sources: admin.ch says the extent of Publica data affected is still being clarified and watson/Netzwoche say Publica data 'könnten betroffen sein' / is unclear; none says the supplier holds the staff data, and 'its staff' is ambiguous (Publica's insured are federal and ETH staff, not Publica's staff). Suggested wording: 'the supplier's software runs the federal pension fund's administration (Netzwoche), whose insured include federal and ETH staff'."
- code: F8
  category: needs-more-research
  section: incident
  item: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow (Exposure scope omitted) (low confidence)"
  url_or_quote: "https://www.admin.ch/de/newnsb/FjG4XOIms04s: \"Keine anderen Bundesstellen pflegen Geschäftsbeziehungen mit dem Unternehmen.\" (watson and Netzwoche repeat it)"
  summary: "(low confidence) The Confederation's statement that no other federal body deals with PK Softech scopes the Exposure for a federal, cantonal and communal readership and bears on action 2 ('If your organisation's ... runs on PK Softech software, ask the supplier'); the entry leaves it out. One clause in paragraph 1 or the Defender takeaway."
- code: F8
  category: needs-more-research
  section: threat
  item: "2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop (affected_products after the 2026-10-09T03:54:00Z update) (low confidence)"
  url_or_quote: "affected_products: [\"Terraform\", \"macOS\", \"Microsoft Windows\"] vs https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver: \"The loader selects payloads for macOS, Linux, and Windows\"; FLATROOF persistence \"a service on Linux\""
  summary: "(low confidence) Iteration 3 asked for the Linux and Windows platforms the update documents; Windows was added, Linux was not. The Update section, summary and record all say macOS, Linux and Windows. Add 'Linux' (convention in the store: \"Linux\" / \"Linux kernel\") or state why it stays out."
- code: F15
  category: name-collision-unflagged
  section: threat
  item: "2026-10-09/reliaquest-llm-agents-spring-batch-tomcat-nashorn-system (Cairn disambiguation clause) (low confidence)"
  url_or_quote: "body: \"a live, unauthenticated Cairn agent-orchestration dashboard (an open-source platform for coordinating AI agents that no source links to other projects of that name, such as the Cairn exploitation engine in Gambit Security's reporting or Talos' CAIRN toolkit)\""
  summary: "(low confidence) Talos' CAIRN is a distinct Cisco toolkit, but 'other projects of that name' also asserts that Gambit's Cairn is a different project, which neither source establishes: Gambit (https://gambit.security/blog-posts/autonomous-ai-agents-online-retailers-25-a-company) says 'Cairn is an autonomous penetration testing engine. It receives target domains and an objective ... then runs for hours until it achieves the objective'; ReliaQuest says Cairn is a 'legitimate open-source orchestration platform for coordinating AI agents' that 'dispatches AI coding agents against an objective'. Both are open-source, objective-driven agent harnesses. Reword to 'no source says whether it is the same project as the Cairn engine in Gambit Security's reporting' (Talos' CAIRN is the clearly separate one) or add the 2026-09-23 Gambit entry to references[]; if the two are one project the entry belongs on tool:cairn-exploitation-engine."
- code: F11
  category: editorial-advisory
  section: threat
  item: "2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop; 2026-10-09/talos-ai-analysis-evasion-instructions-aimed-at-llm-triage (entity linking) (low confidence)"
  url_or_quote: "entities: [\"actor:jade-sleet\"] (TraderTraitor entry); entities: [\"tool:cairn-talos\", \"actor:uac-0099\"] (Talos entry)"
  summary: "Advisory. The subject malware families have no registry record or key: FLATROOF and ROOFDECK (the update now gives them a second publisher, so entity pages cannot aggregate the Zscaler reporting) and FRUITSHELL, PLOTSAFE, HOLLOWCLAD, MANTLEMAZE and MATCHBOIL (the Talos and ESET subjects). The store keys malware subjects elsewhere (for example malware:whipshot on the 88771 entry). May be left for the audit."
- code: F11
  category: editorial-advisory
  section: incident
  item: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow (techniques[] T1199)"
  url_or_quote: "techniques: [T1199]"
  summary: "Advisory, judged as asked: T1199 (Trusted Relationship) describes using a third party's access to reach the target, and no cited source says the attackers did that against Publica or the federal bodies; the sources describe malware on the supplier's own infrastructure and a possible data outflow. Acceptable as the closest non-empty mapping for the gate and the run record says so; may be left."
```
