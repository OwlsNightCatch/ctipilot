**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-09T04:31:26Z · ended_at=2026-10-09T04:47:10Z · duration_seconds=944

## Verification report — 2026-10-09T0255Z-intel (iteration 3)

Scope walked: every one of the 160 ledger claims (all of `claims.changed.iter3.yaml`, every claim of Publica, AA26-281A, Talos and ReliaQuest, and in addition every claim of the other four entries; rows in `verification.iter3.claims.yaml`). Every cited page was fetched this iteration (extract, pdf, cisa-kev, ncsc-csh, the Citrix community RSS feed for the two permalinks every transport blocks, NVD API for per-CVE cross-checks); a claim was marked `ok` only against text read this iteration.

### Prior-iteration deltas (each remediation re-checked against the live source)

1. Publica 'among others' and end-2025 as-of date: correct. watson and Netzwoche both read "Sie versichert unter anderem Mitarbeitende der Bundesverwaltung und des ETH-Bereichs. Ende 2025 zählte sie rund 70'000 ... und 41'600 Rentenbeziehende"; summary, body and action 1 now match. The Exposure line is folded into the body as stated. New nit found in the same paragraph (F3 below).
2. AA26-281A Apache date and MicroScan wording: correct. The S2-032 page's only visible dateline is "modified on Feb 13, 2021"; AA26-281A: "This Python-based web application contains over 1,300 penetration testing scripts".
3. "the advisory names no Swiss victim": correct. All 57 pages (2-58) of the PDF text are present and contain no "Swiss"/"Switzerland"; victims are U.S. sectors plus "Southeast Asia, Africa, and North America".
4. CVE-2023-22894 auth pre-auth: the cves[] value is supported by Strapi's own disclosure (PR:N; "unauthenticated users could exploit"), but the sourcing_note's closing clause is wrong under its natural reading (F9 below).
5. Run-record Updates bullet, Talos CAIRN, ReliaQuest Cairn clause: correct and consistent with the entries (Talos body now names CAIRN; ReliaQuest clause names Gambit's Cairn engine and Talos' CAIRN).
6. Left on purpose, judged: Publica length is at the upper edge of the incident floor but acceptable (advisory, F11 below); 88771 actions[0] vs immediate_action is acceptable (advisory).

### Citation does not support the claim

#1 (F3, minor) `2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow`, body: "the supplier, PK Softech AG of Reinach (BL), says unknown persons used malware ... and that data left its systems". PK Softech's page: "Nach heutigem Kenntnisstand muss davon ausgegangen werden, dass Daten aus unseren Systemen abgeflossen sind." (it must be assumed). watson/Netzwoche: Publica says whether and which data actually left is still unclear. The summary's "The Confederation, Publica and the supplier ... confirmed ... that unknown attackers used malware" credits all three with wording only PK uses (admin.ch says only "Cyberangriff", title "Datenabfluss bestätigt"). Fix: "says it must be assumed that data left its systems".

### Needs more research

#2 (F8, low confidence) `2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop`: after the 2026-10-09T03:54:00Z update, `affected_products: ["Terraform", "macOS"]` omits the Linux and Windows payloads the update documents ("The loader selects payloads for macOS, Linux, and Windows"). Add them (and name `affected_products` in the record's `fields`) or leave if platform names are not wanted for malware targets.

### Surface contradiction

#3 (F9) `2026-10-09/aa26-281a-integrity-tech-microscan-exchange-mail-theft`, sourcing_note: "CISA's catalogue says the Strapi flaw needs access to the admin panel while Strapi's own vector lists no privileges required; the CVE record follows Strapi." The public CVE/NVD record (services.nvd.nist.gov, CVE-2023-22894, fetched this iteration) reads "allows attackers (with access to the admin panel)" with CVSS 3.1 PR:H, the same as CISA; only Strapi's disclosure gives PR:N. "The CVE record follows Strapi" is read by a SOC reader as the public record and is the opposite of what NVD says. Reword: CISA and the NVD record say admin-panel access is needed, Strapi's own disclosure says an unauthenticated attacker can exploit it, and the pre-auth rating follows Strapi (no frontmatter field names in reader-facing text).

### Editorial / less-is-more flags (advisory)

#4 (F11) Publica: "which makes the supplier relationship the reason this belongs here" is composition-rationale wording; state the ground in the reader's terms. Length: paragraph 1 is three sentences (the third mixes the Netzwoche fact with the ground) plus Detection and Defender takeaway, the upper edge of the incident floor; acceptable for a routine incident with two sourced actions. May be left.
#5 (F11) AA26-281A: body closes the alias list ("Flax Typhoon, Ethereal Panda and Red Juliett"); the advisory and the NCSC UK quote in evidence say "among others". No decision turns on it.
#6 (F11) 88771: actions[0] stops at the 88779 builds while immediate_action carries 14.1-73.46/13.1-64.29; acceptable because the entry is not re-floated and the 88779 and 107406 actions carry the identity-provider task in the aggregated list. Optional one-clause alignment.
#7 (F11) Publica techniques[] T1199 is the closest id, but no source says the attackers used the supplier's access to enter Publica; left on purpose per the run record.
#8 (F11) ReliaQuest Cairn clause names Gambit's and Talos' projects inside a ReliaQuest-cited clause without a citation or `references[]` link (Gambit's "autonomous penetration testing engine ... receives target domains and an objective" and ReliaQuest's objective-driven orchestrator are close). Optional link.

### Checked and clean (no finding)

Relevance, priority (Publica routine; 107406, AA26-281A, Talos, ReliaQuest notable; 88779 high unchanged), classification codes, verification values and sourcing notes, evidence quotes (all verbatim on live pages), changelog contract for the three updated entries (every changed line in `git diff HEAD` is covered by a record `fields` list; sections match record summaries; no supersession defects), zero IOCs, no em dash outside the section headings, no workflow vocabulary, run-record notes (KEV sweep, backlog rows and expiries, counts, dispositions) hold on disk. Gate re-run: only the two Phase 6 bookkeeping items (residual count, completed/duration_seconds re-stamp).

Missed angles: none found. KEV catalog 2026.10.08 carries only the five AA26-281A additions (all covered); NCSC-CH hub posts since 2026-10-07 (Atlassian, ILIAS, SonicWall SMA1000, FortiMail, Cisco SD-WAN) are covered by earlier entries or deliberately dropped; no further in-window critical/high item surfaced from a standard search. Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 2, advisory: 5)

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: incident
  item: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow (claim 440abb4ffb)"
  url_or_quote: "body: \"the supplier, PK Softech AG of Reinach (BL), says unknown persons used malware to reach part of its IT infrastructure and that data left its systems\" vs https://pksoftech.ch/de/newsreader/Cyberangriff-auf-die-PKSoftechAG: \"Nach heutigem Kenntnisstand muss davon ausgegangen werden, dass Daten aus unseren Systemen abgeflossen sind.\""
  summary: "Minor hedge loss: PK Softech writes that it 'must be assumed' data left (watson/Netzwoche: Publica says whether and which data left is still unclear); the body turns the assumption into the supplier's flat statement. The summary's 'The Confederation, Publica and the supplier ... confirmed ... that unknown attackers used malware' likewise credits all three with wording only PK uses. Fix: 'says it must be assumed that data left its systems' (the entry's own evidence quote already has the hedge)."
- code: F9
  category: surface-contradiction
  section: threat
  item: "2026-10-09/aa26-281a-integrity-tech-microscan-exchange-mail-theft (sourcing_note, CVE-2023-22894)"
  url_or_quote: "sourcing_note: \"CISA's catalogue says the Strapi flaw needs access to the admin panel while Strapi's own vector lists no privileges required; the CVE record follows Strapi.\""
  summary: "Conflict is surfaced but the closing clause misleads: the public CVE/NVD record (https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2023-22894, fetched this iteration) says 'allows attackers (with access to the admin panel)' with CVSS 3.1 PR:H, the same reading as CISA; only Strapi's own disclosure gives PR:N / unauthenticated. 'The CVE record follows Strapi' reads as the public CVE record to a SOC reader and is the opposite of what NVD says. Reword to name who says what and that the pre-auth rating follows Strapi's disclosure (no field names), e.g. 'CISA and the NVD record say admin-panel access is needed; Strapi's own disclosure says an unauthenticated attacker can exploit it, and the pre-auth rating follows Strapi.'"
- code: F8
  category: needs-more-research
  section: threat
  item: "2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop (affected_products after the 2026-10-09T03:54:00Z update) (low confidence)"
  url_or_quote: "affected_products: [\"Terraform\", \"macOS\"] vs Zscaler (https://www.zscaler.com/blogs/security-research/suspected-tradertraitor-group-uses-trojanized-terraform-provider-deliver): \"The loader selects payloads for macOS, Linux, and Windows according to the operating system and CPU architecture.\""
  summary: "(low confidence) The update documents Linux and Windows payloads and the Update section says so, but affected_products (not named in the record's fields) still lists only Terraform and macOS, so the entry is not found from a Linux or Windows product view. Add the platforms the update documents (and name affected_products in the record's fields) or leave as is if platform names are not wanted for malware targets."
- code: F11
  category: editorial-advisory
  section: incident
  item: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow (transfer-ground wording and length)"
  url_or_quote: "\"no access vector, actor or ransom demand is public, which makes the supplier relationship the reason this belongs here.\""
  summary: "Advisory. 'the reason this belongs here' is a composition-rationale phrase aimed at the pipeline, not the reader; state the ground in the reader's terms (supplier to the Confederation's pension fund, federal and ETH staff data). Length: paragraph 1 is three sentences (the third mixes the Netzwoche fact with the ground) plus Detection and Defender takeaway; judged acceptable for a routine incident that carries two sourced actions, but it is the upper edge of the incident floor ('at most two sentences plus its transfer ground'). May be left."
- code: F11
  category: editorial-advisory
  section: threat
  item: "2026-10-09/aa26-281a-integrity-tech-microscan-exchange-mail-theft (alias list closed)"
  url_or_quote: "body: \"use tactics consistent with Flax Typhoon, Ethereal Panda and Red Juliett\" vs AA26-281A: \"Flax Typhoon, Ethereal Panda, and Red Juliett, among others\""
  summary: "Advisory. The advisory (and the NCSC UK sentence the entry quotes in evidence) leaves the alias list open with 'among others'; the body closes it. No decision turns on it. May be left."
- code: F11
  category: editorial-advisory
  section: vulnerabilities
  item: "2026-09-28/cve-2026-88771-citrix-netscaler-preauth-rce-zero-day-kev (actions[0] vs immediate_action)"
  url_or_quote: "actions[0]: \"(a SAML-configured appliance needs the later builds named for CVE-2026-88779)\" vs immediate_action: \"... and to 14.1-73.46+ or 13.1-64.29+ where it is an identity provider (CVE-2026-107406)\""
  summary: "Advisory, judged acceptable. Inside this entry actions[0] stops at the 88779 builds while immediate_action carries the .46/.29 builds; the entry is not re-floated (improvement record) and the 88779 and 107406 actions carry the identity-provider task in the aggregated list, so nothing is lost. If cheap, add 'identity providers then need 14.1-73.46 or 13.1-64.29' to actions[0] for consistency. May be left."
- code: F11
  category: editorial-advisory
  section: incident
  item: "2026-10-09/publica-pk-softech-supplier-malware-intrusion-data-outflow (techniques[] T1199)"
  url_or_quote: "techniques: [T1199]"
  summary: "Advisory, left on purpose per the run record. T1199 (Trusted Relationship) describes using a third party's access to reach the target; no cited source says the attackers used PK Softech's access to enter Publica or federal networks. Closest available id for a non-empty mapping; may be left."
- code: F11
  category: editorial-advisory
  section: threat
  item: "2026-10-09/reliaquest-llm-agents-spring-batch-tomcat-nashorn-system (Cairn disambiguation clause)"
  url_or_quote: "\"...an open-source platform for coordinating AI agents that no source links to other projects of that name, such as the Cairn exploitation engine in Gambit Security's reporting or Talos' CAIRN toolkit...\""
  summary: "Advisory. The parenthetical sits inside a ReliaQuest-cited clause but names Gambit's and Talos' projects without a citation; neither is on the ReliaQuest page. Gambit's description (autonomous engine that takes a target domain and an objective, open-source harness) and ReliaQuest's (objective-driven agent orchestration control plane) are close enough that a reader may want the link: consider adding the 2026-09-23 Gambit entry to references[] or citing its source. May be left."
```
