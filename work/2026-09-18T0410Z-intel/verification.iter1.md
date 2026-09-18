**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-18T05:09:54Z · ended_at=2026-09-18T05:19:57Z · duration_seconds=603

## Verification report — 2026-09-18T0410Z-intel (iteration 1)

### Citation does not support the claim

**#1** `ntc-swiss-solar-inverter-cybersecurity-assessment` — the body states "representative of Switzerland's roughly 338,000 grid-connected photovoltaic installations" cited to `[NTC, 2026-09-17](https://en.ntc.swiss/news/cybersecurity-of-photovoltaic-systems)`. I fetched that exact URL (`fetch_source.py extract`) in full; it never states this figure anywhere. The 338,000 figure is stated by the two co-cited outlets instead: cash.ch ("Ende 2025 waren in der Schweiz rund 338'000 netzverbundene Anlagen installiert") and SRF ("338'000 Photovoltaikanlagen sind bereits in Betrieb"). The citation is attached to the wrong co-cited source.

**#2** `ntc-swiss-solar-inverter-cybersecurity-assessment` — "NTC found no evidence of intentionally built-in backdoors" cited to the same NTC URL. That page (full text fetched) does not contain this statement anywhere. It is cash.ch that states this: "Hinweise auf absichtlich eingebaute Hintertüren fand das NTC laut eigenen Angaben nicht." Citation misattributed to NTC's own page instead of cash.ch.

**#3** `ntc-swiss-solar-inverter-cybersecurity-assessment` — "Switzerland's Federal Office of Energy independently confirms NTC's risk assessment, per cash.ch" cited to `[cash.ch, 2026-09-17]`. I fetched cash.ch's full article; it contains no mention of the Federal Office of Energy at all. This claim is stated by SRF instead: "Das Bundesamt für Energie bestätigt die Analyse: Das Risiko eines koordinierten Angriffs könne nicht ausgeschlossen werden." Citation attached to the wrong outlet.

**#4** `gyazo-helpfeel-data-breach-image-upload-rce` — "the 32-character image ID used to construct the access URL" is folded into a sentence cited only to `[Helpfeel Inc., 2026-09-16]`. I fetched Helpfeel's own notice in full; it lists "Image ID (information used to construct the image URL)" but never states the character count. The "32-character" detail is stated by the co-cited The Hacker News article instead: "Every Gyazo capture gets a link built from a 32-character image ID."

**#5** `gyazo-helpfeel-data-breach-image-upload-rce` — "Helpfeel's own public status page described the outage only as 'emergency maintenance' from September 12 through 15" cited to The Hacker News (2026-09-17). I fetched that article in full; it dates the "emergency maintenance" notices specifically to September 14 and September 15 only ("Gyazo's product-updates page said delivery had been suspended for some images 'due to emergency maintenance'" on Sept 14; "a second notice said, 'Some images remain unavailable due to emergency maintenance'" after Sept 15 resumption) — it never states the maintenance framing began on September 12. Helpfeel's own timeline table (also fetched) shows Sept 12 as "completed our initial response measures," not a maintenance notice.

**#6** `brevo-cloudflare-worker-clickfix-supply-chain` (frontmatter + inline citations) — Sansec is dated "2026-09-14" in `sources[]` and in two inline citations (`[Sansec, 2026-09-14]`). I fetched the Sansec article directly: its own byline reads "Published in Threat Research − September 16, 2026" and its extracted metadata gives `date: "2026-09-16"`. This is a 2-day drift between the cited date and the source's own publication date (check 2e).

**#7** `revolut-fake-government-request-kyc-breach`, 2026-09-18 update section — "Revolut had said only that the request 'appeared authentic based on the technical indicators available'" is presented as something Revolut itself said. I fetched TechCrunch and Security Affairs (the entry's original disclosure sources) in full; neither contains this phrase or anything close to it. The actual source is CyberInsider's own paraphrase, not a Revolut quote: "Revolut previously told CyberInsider that the requests came from a legitimate government agency domain and appeared authentic based on the technical indicators available to its staff." CyberInsider is presenting its own reported summary, not a direct Revolut quote — the entry both misattributes the framing (implying Revolut said this, in quotation marks, when CyberInsider's own sentence isn't a Revolut quote either) and (see F5 below) cites no source for the clause at all.

### Unsupported / hallucinated facts

**#8** `cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev` — the entry states in `affected_products[]` ("Acronis Backup plugin for DirectAdmin (Linux)"), in `cves[].affected` ("Acronis Backup plugin for DirectAdmin before build 1.2.3.238"), in `cves[].fixed` ("DirectAdmin plugin build 1.2.3.238"), and in the body ("...and plugin for DirectAdmin, all on Linux") that DirectAdmin is a third affected product, cited to Help Net Security. I fetched all three of this entry's listed sources in full: Help Net Security's article names only cPanel & WHM and Plesk; BleepingComputer's article names only cPanel & WHM and Plesk (twice, in its own affected-versions list); and CISA's KEV JSON entry for CVE-2026-87886 (`shortDescription`, fetched live) reads "Acronis Backup plugin for cPanel & WHM and extension for Plesk contains an incorrect default permissions vulnerability" — no DirectAdmin. None of the entry's three cited sources mentions DirectAdmin anywhere; the sourcing_note explicitly claims "every vulnerability-description fact is cited to Help Net Security and BleepingComputer... plus CISA's KEV catalog," which is not true of the DirectAdmin claim. This is a specific product name plus a specific build number with no supporting citation anywhere in the entry.

### Claims missing inline citation

**#9** `brevo-cloudflare-worker-clickfix-supply-chain`, third body paragraph — the two-sentence passage "Sansec independently corroborated the root cause before Brevo's own confirmation, matching Last-Modified timestamps across injected and clean asset versions and finding an SSL certificate for the attacker's infrastructure issued 2026-08-25, pinning the attacker's access to at least that date; Sansec estimates the affected embedded-script exposure reached up to 100,000 sites, a count of pages referencing the compromised script paths rather than a confirmed count of sites whose visitors received the payload. Brevo's post-mortem does not mention a separate SSO-hijacking incident it disclosed on 2026-09-10 that led to a phishing campaign against Trezor customers, and BleepingComputer states Brevo did not respond to its question about whether the two incidents were connected." carries zero inline citations across two full sentences and five distinct factual claims (a specific date, a percentage/count, a named incident, an unanswered-question claim). I confirmed each fact is individually true of the Sansec and BleepingComputer articles I fetched, but the sentence as published has no link at all.

**#10** `revolut-fake-government-request-kyc-breach`, 2026-09-18 update — the clause "(Revolut had said only that the request 'appeared authentic based on the technical indicators available')" carries no inline citation (same clause as F3 finding #7 above).

### Quantifier without source

**#11** `cve-2026-76460-cisco-ise-auth-bypass-root-rce`, 2026-09-18 update section — the entry states "notes ISE 3.1/3.2 will receive no fix at all for **seven** of the disclosed CVEs before their November 2027 end of maintenance," cited to CERT-FR (CERTFR-2026-AVI-1197). I fetched that advisory directly; its text reads: "Cisco indique que les versions 3.2 et 3.1 de Identity Services Engine (ISE) ne seront plus supportées à partir du 30 novembre 2027 et n'ont pas reçu de correctif pour les vulnérabilités CVE-2026-20247, CVE-2026-20282, CVE-2026-20300, CVE-2026-76424, CVE-2026-76425, CVE-2026-76426, CVE-2026-76427 et CVE-2026-76428." That is **eight** distinct CVE ids, not seven. This appears in both the entry's `updates[].summary` and the body's `## Update` section.

**#12** (low confidence) `famoussparrow-sparrowocky-backdoor-latam-gov` — the summary and body state "90% of observed 2025-2026 targeting hit Latin American government entities." I fetched ESET's article in full: the 90% figure is stated as "from mid-2025 and into 2026, 90% of the group's targets registered in our telemetry have been located in the region" — a statement about the *geographic* concentration of all targets, not specifically that 90% of targets were government entities. ESET separately says it observed SparroWocky "deployed against governmental entities" in eight named LatAm countries and that FamousSparrow is "extensively targeting governmental organizations in Latin America," but never states the government-entity share is 90%. The entry's phrasing splices a geographic-concentration statistic onto a sector-composition claim.

**#13** (low confidence) `moviereaper-torrent-supply-chain-solana-c2` — the body describes `EtwpCreateEtwThread` as "an ETW-Threat-Intelligence-provider-evading alternative to CreateThread." Kaspersky's article states only that it is "an undocumented ntdll function EtwpCreateEtwThread, which is a popular alternative to a CreateThread to perform code execution" — it does not characterize the function as specifically ETW-TI-evading. The added framing is plausible (the function name suggests ETW involvement) but is not stated by the cited source.

### Editorial / less-is-more flags (advisory)

**#14** `cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev` — priority `high` on a post-auth, local-only privilege escalation whose sole exploitation evidence is Acronis's own single-customer report (the entry itself narrates this caveat twice). The KEV listing and CISA's independent-judgment framing justify inclusion and urgency, but given the constituency's core is public-sector administration rather than hosting-panel/MSP infrastructure, a case could be made for `notable`. Flagging as advisory only — KEV-listed CVEs conventionally clear the `high` bar in this pipeline's established practice, and I found nothing that plainly requires downgrading it.

### Verdict

`NEEDS_FIXES (truth: 11, editorial: 2, advisory: 1)`

Findings #1–#8 are truth-class (F3/F4), #9–#10 are editorial-class (F5), #11–#13 are truth-class (F14), #14 is advisory (F11). Truth count = 8 (F3 #1,#2,#3,#4,#5,#6,#7 = 7, plus F4 #8 = 1) + 3 (F14 #11,#12,#13) = 11. Editorial count = 2 (F5 #9, #10). Advisory = 1 (#14).

Everything else checked out clean: both Check Point sources (sk1000155, CERT-FR AVI-1193) confirm every version/take number, the exact evidence quotes, and the exploitation-status framing; the FamousSparrow entry's 34-id `techniques[]` list was verified against the raw HTML of ESET's own ATT&CK table and matches exactly (all 34 ids present, none invented) — the run record's claimed Phase-4 correction from a 13-id draft holds; MovieReaper's technical chain, victim list and both direct quotes verified verbatim against Securelist; the Brevo post-mortem's timeline, root cause, and both evidence quotes verified verbatim; the two new Cisco FMC advisories (CVE-2026-20324, CVE-2026-20242) verified in full against Cisco's own PSIRT text, including CVSS, ASA/FTD-not-affected, and workaround status; the NCSC-NL CSAF record (fetched via the `ncsc-nl csaf` bridge recipe) verified both translated evidence quotes verbatim; all three updated entries' `git diff` output is purely additive (no silent edits), every changed line is covered by its changelog record's `fields`, and `discovered_at`/`run_id`/path are untouched on all three. No F1 (broken URL), F2 (generic URL), F6 (weak primary), F7 (drop-worthy), F9 (contradiction), F12 (single-source flag), F15 (name collision), F16 (org-triage/priority), F17 (classification), or F18 (action-item) findings. No dedup violations found against `prior_coverage.json` (71 records, no CVE/entity overlap) or `state/cves_seen.json` (neither new CVE present). No missed-angle candidate identified beyond what the run record's own coverage-backlog section already tracks.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "ntc-swiss-solar-inverter-cybersecurity-assessment"
  url_or_quote: "representative of Switzerland's roughly 338,000 grid-connected photovoltaic installations ([NTC, 2026-09-17])"
  summary: "NTC's own page (fetched in full) never states this figure; it is stated by cash.ch and SRF, both co-cited elsewhere in the entry."
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "ntc-swiss-solar-inverter-cybersecurity-assessment"
  url_or_quote: "NTC found no evidence of intentionally built-in backdoors ([NTC, 2026-09-17])"
  summary: "Not stated on the NTC page fetched; stated by cash.ch ('Hinweise auf absichtlich eingebaute Hintertüren fand das NTC laut eigenen Angaben nicht')."
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "ntc-swiss-solar-inverter-cybersecurity-assessment"
  url_or_quote: "Switzerland's Federal Office of Energy independently confirms NTC's risk assessment, per cash.ch ([cash.ch, 2026-09-17])"
  summary: "cash.ch's full text (fetched) never mentions the Federal Office of Energy; the claim is stated by SRF instead ('Das Bundesamt für Energie bestätigt die Analyse...')."
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "gyazo-helpfeel-data-breach-image-upload-rce"
  url_or_quote: "the 32-character image ID used to construct the access URL ([Helpfeel Inc., 2026-09-16])"
  summary: "Helpfeel's own notice never states the character count; The Hacker News states 'a link built from a 32-character image ID.'"
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "gyazo-helpfeel-data-breach-image-upload-rce"
  url_or_quote: "described the outage only as \"emergency maintenance\" from September 12 through 15 ([The Hacker News, 2026-09-17])"
  summary: "The Hacker News dates the 'emergency maintenance' notices to Sept 14 and Sept 15 only; Helpfeel's own timeline shows Sept 12 as 'completed initial response measures,' not a maintenance notice."
- code: F3
  category: claim-not-supported
  section: updated-entries
  item: "brevo-cloudflare-worker-clickfix-supply-chain"
  url_or_quote: "sources[] and inline citations date Sansec as 2026-09-14"
  summary: "Sansec's own article byline and metadata read 'September 16, 2026' / date: 2026-09-16 — a 2-day drift from the cited date (check 2e)."
- code: F3
  category: claim-not-supported
  section: updated-entries
  item: "revolut-fake-government-request-kyc-breach"
  url_or_quote: "Revolut had said only that the request \"appeared authentic based on the technical indicators available\""
  summary: "TechCrunch and Security Affairs (the original disclosure sources) contain no such phrase; it is CyberInsider's own paraphrase ('appeared authentic based on the technical indicators available to its staff'), not a Revolut quote, and misattributed as something Revolut itself said."
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev"
  url_or_quote: "Acronis Backup plugin for DirectAdmin (Linux) / before build 1.2.3.238 / fixed build 1.2.3.238"
  summary: "None of the entry's three cited sources (Help Net Security, BleepingComputer, CISA KEV JSON — all fetched in full) mentions DirectAdmin; the sourcing_note's claim that every fact traces to these three sources is false for this detail."
- code: F14
  category: quantifier-without-source
  section: updated-entries
  item: "cve-2026-76460-cisco-ise-auth-bypass-root-rce"
  url_or_quote: "seven of the disclosed CVEs [unpatched on ISE 3.1/3.2]"
  summary: "CERT-FR CERTFR-2026-AVI-1197 (fetched) lists eight CVE ids without a fix for 3.1/3.2: CVE-2026-20247, -20282, -20300, -76424, -76425, -76426, -76427, -76428."
- code: F14
  category: quantifier-without-source
  section: new-entries
  item: "famoussparrow-sparrowocky-backdoor-latam-gov"
  url_or_quote: "90% of observed 2025-2026 targeting hit Latin American government entities"
  summary: "(low confidence) ESET's 90% figure describes geographic concentration of all targets in the region, not specifically that 90% were government entities."
- code: F14
  category: quantifier-without-source
  section: new-entries
  item: "moviereaper-torrent-supply-chain-solana-c2"
  url_or_quote: "an ETW-Threat-Intelligence-provider-evading alternative to CreateThread"
  summary: "(low confidence) Kaspersky calls EtwpCreateEtwThread 'a popular alternative to a CreateThread' without characterizing it as ETW-TI-evading specifically."
- code: F5
  category: missing-citation
  section: updated-entries
  item: "brevo-cloudflare-worker-clickfix-supply-chain"
  url_or_quote: "Sansec independently corroborated the root cause... Sansec estimates the affected embedded-script exposure reached up to 100,000 sites... Brevo's post-mortem does not mention a separate SSO-hijacking incident... BleepingComputer states Brevo did not respond..."
  summary: "Two full sentences, five distinct factual claims, zero inline citations."
- code: F5
  category: missing-citation
  section: updated-entries
  item: "revolut-fake-government-request-kyc-breach"
  url_or_quote: "(Revolut had said only that the request \"appeared authentic based on the technical indicators available\")"
  summary: "No inline citation on this clause at all (same clause as the F3 misattribution finding above)."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev"
  url_or_quote: "priority: high"
  summary: "Post-auth, local-only priv-esc with exploitation resting solely on Acronis's own single-customer report; KEV listing justifies inclusion but the org-relevance case for `high` over `notable` is thinner than most high items this run."
```
