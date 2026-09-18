**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-18T05:26:57Z · ended_at=2026-09-18T05:37:57Z · duration_seconds=660

## Verification report — 2026-09-18T0410Z-intel (iteration 2)

Prior-iteration deltas (all 13, iteration 1 → this pass) verified against current file state and live sources:

1. NTC 338,000-installation figure → cash.ch: confirmed. cash.ch: "Ende 2025 waren in der Schweiz rund 338'000 netzverbundene Anlagen installiert." Correctly re-attributed.
2. NTC "no evidence of intentionally built-in backdoors" → cash.ch: confirmed. cash.ch: "Hinweise auf absichtlich eingebaute Hintertüren fand das NTC laut eigenen Angaben nicht." Correctly re-attributed.
3. NTC Federal Office of Energy confirmation → SRF: confirmed. SRF: "Das Bundesamt für Energie bestätigt die Analyse: Das Risiko eines koordinierten Angriffs könne nicht ausgeschlossen werden." Correctly re-attributed.
4. Gyazo "32-character image ID" → The Hacker News: confirmed. THN: "Every Gyazo capture gets a link built from a 32-character image ID." Correctly re-attributed.
5. Gyazo "emergency maintenance ... September 14 and 15": confirmed against THN's own timeline ("suspended image delivery on September 14 ... 'due to emergency maintenance' ... resumed on September 15 ... 'Some images remain unavailable due to emergency maintenance'"). Corrected range is accurate.
6. Brevo/Sansec publication date → 2026-09-16: confirmed. Sansec page metadata and byline both read "September 16, 2026." All three citations now correct.
7. Revolut "appeared authentic based on the technical indicators available" → CyberInsider: confirmed. CyberInsider: "Revolut previously told CyberInsider that the requests came from a legitimate government agency domain and appeared authentic based on the technical indicators available to its staff." This is CyberInsider's own paraphrase of what Revolut told it — citing it to CyberInsider (not to an implied Revolut quote) is correct.
8. Acronis DirectAdmin removal from the entry body/frontmatter: confirmed — grepped the published entry and found zero occurrences of "DirectAdmin." Help Net Security and BleepingComputer sources both cover only cPanel & WHM and Plesk; remaining claims verified against both (see below). **However, the DirectAdmin removal was incomplete store-wide — see new findings #2 and #3.**
9. Cisco ISE "seven" → "eight" unpatched CVEs on 3.1/3.2: confirmed. CERT-FR CERTFR-2026-AVI-1197 lists exactly eight: CVE-2026-20247, CVE-2026-20282, CVE-2026-20300, CVE-2026-76424, CVE-2026-76425, CVE-2026-76426, CVE-2026-76427, CVE-2026-76428.
10. FamousSparrow 90%-Latin-America / "almost all governmental" reword: confirmed against ESET's own text ("90% of the group's targets registered in our telemetry have been located in the region," separately: "FamousSparrow is extensively targeting governmental organizations in Latin America"). The two facts are now correctly stated as distinct.
11. MovieReaper CreateThread-alternative reword: confirmed. Securelist: "Then it calls an undocumented ntdll function EtwpCreateEtwThread, which is a popular alternative to a CreateThread." Kaspersky's own framing only, correctly stated.
12. Brevo four newly-cited claims (Sansec corroboration, 100k-site estimate, Brevo's SSO-incident silence, BleepingComputer's non-response note): all four now carry citations and all four are supported by the cited pages (Sansec: SSL cert 2026-08-25, Last-Modified matching, "more than 100 thousand" via a publicwww query; BleepingComputer: "Brevo did not respond to BleepingComputer's questions as to whether the SSO incident and the Cloudflare compromise were connected"). Correct.
13. Acronis priority:high reviewed and kept: I independently reach the same conclusion — KEV listing is CISA's own exploitation judgment, the body states the single-customer-report basis plainly, "high" (not "critical") is appropriate given the local/post-auth vector. No change requested.

All 13 prior-iteration fixes hold. This pass also found new defects not previously flagged — a full independent cold read, not a spot-check.

### Unsupported / hallucinated facts

**#1** `brevo-cloudflare-worker-clickfix-supply-chain` — evidence[] record:
> "The plugin also stores a backup copy of the last valid JavaScript URL so it can continue loading malicious code if the remote server becomes unavailable... the plugin contains a hardcoded authentication key that allows attackers to generate a valid login session for a WordPress administrator account without knowing the account password."

BleepingComputer's actual text has these as two separate paragraphs, not contiguous: "The plugin also stores a backup copy of the last valid JavaScript URL so it can continue loading malicious code if the remote server becomes unavailable." — [new paragraph] — "Finally, the plugin contains a hardcoded authentication key that allows attackers to generate a valid login session for a WordPress administrator account without knowing the account password." The evidence quote splices the two sentences with an ellipsis and drops the "Finally, " lead-in, producing a quote that is not a contiguous verbatim substring of the source (check 4b, F4-class per the rules' own example: "an inserted ellipsis, a splice of two sentences... is F4"). Fix: split into two separate evidence records, or requote only the second sentence with "Finally, " restored.

**#2** (moderate confidence) `state/cves_seen.json`, record for `CVE-2026-87886` — title field:
> "Acronis Backup plugin for cPanel & WHM/Plesk/DirectAdmin local privilege escalation via insecure default permissions (CVSS 7.8), CISA KEV-listed 2026-09-16, exploitation basis is a single customer report"

This is the same store-wide CVE index entry created by this run (`first_seen: 2026-09-18`), but its title still names DirectAdmin even though iteration 1's remediation dropped DirectAdmin entirely from `entries/2026-09-18/cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev.md` (title, summary, affected_products[], cves[].affected/fixed, actions[], body — confirmed zero occurrences of "DirectAdmin" in the published entry). The remediation fixed the entry but left this store-wide index record stale and now contradicting the entry it is supposed to summarize. Neither Help Net Security nor BleepingComputer (the entry's only sources) mentions DirectAdmin. A future run's dedup pass reading `cves_seen.json` would see DirectAdmin listed as confirmed-affected for this CVE, which is now false. Fix: update the title to drop "/DirectAdmin".

**#3** (moderate confidence) `entities/registry.yaml` — orphan product key:
```
- key: "product:acronis-backup-plugin-for-directadmin-linux"
  type: product
  name: Acronis Backup plugin for DirectAdmin (Linux)
  aliases: []
  first_seen: 2026-09-18
```
Added by this run (`first_seen: 2026-09-18`) alongside the two products that survived the DirectAdmin remediation (`product:acronis-backup-extension-for-plesk-linux`, `product:acronis-backup-plugin-for-cpanel-whm-linux`). No entry in the store references this key (`grep -rl "acronis-backup-plugin-for-directadmin-linux" entries/` returns nothing), and no cited source supports DirectAdmin being affected. This is the registry-level residue of the same incomplete DirectAdmin cleanup as #2 — a permanent, published entity record for a product no source confirms is vulnerable. Registry keys are permanent per the pipeline's own rules, so this should be actively reconciled (e.g. annotated or removed) rather than left to accumulate.

### Claims missing inline citation

**#4** `ntc-swiss-solar-inverter-cybersecurity-assessment`, second body paragraph, two consecutive sentences with no citation:
> "The EU has withdrawn subsidy eligibility for Chinese-inverter projects and the US has declared a grid emergency that can force removal of already-installed sanctioned-country inverters; Switzerland has taken no equivalent step. NTC deliberately withheld product names and technical exploit detail, reporting findings confidentially to manufacturers, most of whom have already shipped fixes; no CVEs were assigned."

The only citation in that paragraph is attached to the preceding sentence about the canton Bern tender ([Kanton Bern Baudirektion, via SRF, 2026-09-16]) — a different, unrelated fact from the same source. I fetched SRF and confirmed it does support the EU/US claims ("Es gibt keine Fördergelder mehr für Projekte mit Wechselrichtern aus China"; "Präsident Donald Trump hat für das Hochspannungs-Stromnetz den nationalen Notstand ausgerufen... Betreiber sollen sogar gezwungen werden können, bereits verbaute Geräte wieder auszubauen"), and NTC's own page supports the disclosure-practice claims ("The public report deliberately omits product names and technical details," "The findings were reported confidentially to the manufacturers. Most responded quickly..."). The facts are accurate but two sentences carrying six distinct new claims (EU policy, US executive action, Switzerland's non-action, NTC's disclosure method, fix status, no-CVE fact) have zero inline citation of their own. Fix: attach `([SRF, 2026-09-16])` to the first sentence and `([NTC, 2026-09-17])` to the second.

### Needs more research

**#5** (moderate confidence) `famoussparrow-sparrowocky-backdoor-latam-gov` — the body describes two of ESET's three named anti-analysis techniques (the SilentMoonwalk call-stack forger, and the MinHook CreateThread hook reporting AnimateWindow as the start address) but omits the third, which ESET describes in comparable technical detail: "before calling the entry point of the loaded PE file, SparroWocky forges and inserts a fake LDR_DATA_TABLE_ENTRY structure in the doubly linked list of the PEB_LDR_DATA structure. This doubly linked list is used by Windows to keep track of loaded modules and is usually monitored by security products." This is itself a genuine behavioral-detection concept (an EDR/hunter can walk PEB_LDR_DATA looking for a forged/inconsistent module entry) at the same technical depth as the two techniques the body does describe, and it is already referenced in this run's own registry summary for `malware:sparrowocky` ("PEB_LDR_DATA forgery") — so the fact was captured during research but dropped from the published body. Fix: add a sentence describing the fake LDR_DATA_TABLE_ENTRY / module-list forgery, ideally folded into the Triage or Defender-takeaway detection guidance.

### Missed angles

**#6** (low confidence) `famoussparrow-sparrowocky-backdoor-latam-gov` — the registry already carries `campaign:famoussparrow-azerbaijan-2026` (first_seen 2026-05-14, aliases: ["UAT-9244"], "FamousSparrow (UAT-9244) three-wave intrusion of an Azerbaijani oil & gas operator"), documenting the same real-world actor this run newly registers as `actor:famoussparrow`. The new actor record carries no `relations[]` edge back to that campaign record, so the registry/graph does not show that the May 2026 Azerbaijan campaign and the September 2026 SparroWocky reporting are the same actor. This is not a name collision (same entity, no disambiguation needed) but a linking gap the registry-maintenance step should close, e.g. a `documented-in` or `related-to` edge from `actor:famoussparrow` to `campaign:famoussparrow-azerbaijan-2026`, sourced to this entry.

### Editorial / less-is-more flags (advisory)

**#7** `ntc-swiss-solar-inverter-cybersecurity-assessment` evidence[] record embeds an editorial annotation inside the quoted text itself rather than as external metadata:
> quote: "If the Chinese manufacturers were to simultaneously switch off all their devices at full power, a collapse of the Swiss power grid would threaten. (translated from German, Raphael Reischuk, NTC founder)"

The `(translated from German, Raphael Reischuk, NTC founder)` parenthetical is not part of the German original and is not itself a translation of anything — it's editorial bookkeeping that has leaked into the `quote:` field, which per the frontmatter contract should be a faithful translation of `original:` only. The content is accurate (verified verbatim against SRF's German text) and the attribution is otherwise correct via the separate `publisher:` field and inline citation; this is a formatting nit, not a truth defect. Advisory only.

**#8** (low confidence) `cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev` — `sources[]` cites the BleepingComputer article with `date: "2026-09-16"`, but the page's own extracted metadata gives `date: "2026-09-15"`. One day of drift may be a timezone/publish-vs-index artifact per the verification rules' own guidance and I cannot rule that out from the fetched metadata alone, so flagging at low confidence rather than as a hard F3.

### Verdict

`NEEDS_FIXES (truth: 3, editorial: 3, advisory: 2)`

All 13 remediations from iteration 1 verified correct and holding. This independent cold pass found three new truth-class defects (one spliced evidence quote in the Brevo entry, and two residual store-wide artifacts — a stale `cves_seen.json` title and an orphan registry product key — both left over from the DirectAdmin removal that fixed the entry itself but not the index/registry that were populated alongside it), one missing-citation defect (NTC), one technical-depth gap (FamousSparrow's third anti-analysis technique), one low-confidence entity-linking gap, and two advisory-level formatting/date-drift notes. Coverage otherwise looks sound: I fetched every primary and corroborating source for all 7 new entries and both new-source changelog updates (Cisco FMC hardening release, Cisco ISE hardening release), cross-checked every named CVE/version/date/quote against the cited page, and found no other broken URLs, no other hallucinated entities, no contradictions, no priority miscalibration, and no `org_triage`/`watchlist` drift (both correctly absent throughout, consistent with this deployment's unconfigured triage/watchlist scheme). `check_run.py` reconfirmed 48 pass · 0 warn · 0 fail during this pass.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: brevo-cloudflare-worker-clickfix-supply-chain
  item: "Brevo: a stolen, hardcoded Cloudflare API key let an attacker inject ClickFix malware and a WordPress backdoor plugin via a CDN-edge Worker"
  url_or_quote: "\"The plugin also stores a backup copy of the last valid JavaScript URL so it can continue loading malicious code if the remote server becomes unavailable... the plugin contains a hardcoded authentication key that allows attackers to generate a valid login session for a WordPress administrator account without knowing the account password.\""
  summary: "Ellipsis splices two non-contiguous BleepingComputer sentences (separated by a 'Finally,'-led paragraph break) into one evidence[] quote; not a contiguous verbatim substring of the source."
- code: F4
  category: hallucinated-fact
  section: cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev
  item: "state/cves_seen.json record for CVE-2026-87886"
  url_or_quote: "\"Acronis Backup plugin for cPanel & WHM/Plesk/DirectAdmin local privilege escalation...\""
  summary: "(moderate confidence) Store-wide CVE index title still names DirectAdmin even though iteration 1 removed DirectAdmin entirely from the published entry (no source supports it); stale and now contradicts the entry it summarizes."
- code: F4
  category: hallucinated-fact
  section: cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev
  item: "entities/registry.yaml: product:acronis-backup-plugin-for-directadmin-linux"
  url_or_quote: "first_seen: 2026-09-18, name: Acronis Backup plugin for DirectAdmin (Linux)"
  summary: "(moderate confidence) Orphan registry product key added by this run but referenced by no entry after the DirectAdmin removal; no cited source supports DirectAdmin being affected. Registry-level residue of the same incomplete cleanup as the cves_seen.json title."
- code: F5
  category: missing-citation
  section: ntc-swiss-solar-inverter-cybersecurity-assessment
  item: "NTC finds default passwords, fleet-wide shared credentials and unauthenticated grid-feed shutoff across Swiss solar inverters"
  url_or_quote: "\"The EU has withdrawn subsidy eligibility for Chinese-inverter projects and the US has declared a grid emergency that can force removal of already-installed sanctioned-country inverters; Switzerland has taken no equivalent step. NTC deliberately withheld product names and technical exploit detail, reporting findings confidentially to manufacturers, most of whom have already shipped fixes; no CVEs were assigned.\""
  summary: "Two sentences with six distinct new claims carry no inline citation; nearest citation in the paragraph covers an unrelated fact. Confirmed both sentences are supported by SRF and NTC's own page respectively, but uncited in the entry."
- code: F8
  category: needs-more-research
  section: famoussparrow-sparrowocky-backdoor-latam-gov
  item: "FamousSparrow retires SparrowDoor for SparroWocky"
  url_or_quote: "ESET: \"SparroWocky forges and inserts a fake LDR_DATA_TABLE_ENTRY structure in the doubly linked list of the PEB_LDR_DATA structure. This doubly linked list is used by Windows to keep track of loaded modules and is usually monitored by security products.\""
  summary: "(moderate confidence) Body describes 2 of ESET's 3 named anti-analysis techniques; the PEB_LDR_DATA/module-list forgery technique (a genuine detection concept, already referenced in this run's own registry summary) is dropped from the body."
- code: F10
  category: missed-angle
  section: famoussparrow-sparrowocky-backdoor-latam-gov
  item: "actor:famoussparrow (new registry entity)"
  url_or_quote: "campaign:famoussparrow-azerbaijan-2026 (first_seen 2026-05-14, alias UAT-9244) already documents the same actor"
  summary: "(low confidence) No relations[] edge links the newly-created actor:famoussparrow entity back to the pre-existing campaign:famoussparrow-azerbaijan-2026 record for the same actor; suggested fix: add a documented-in/related-to edge. Suggested query to confirm scope: search registry for other FamousSparrow/UAT-9244 records."
- code: F11
  category: editorial-advisory
  section: ntc-swiss-solar-inverter-cybersecurity-assessment
  item: "evidence[] quote for Raphael Reischuk"
  url_or_quote: "\"...a collapse of the Swiss power grid would threaten. (translated from German, Raphael Reischuk, NTC founder)\""
  summary: "Editorial annotation leaked inside the quote: field itself rather than kept as external metadata; content and attribution are both accurate, formatting only."
- code: F11
  category: editorial-advisory
  section: cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev
  item: "sources[] BleepingComputer citation"
  url_or_quote: "date: \"2026-09-16\" cited; page metadata reads date: \"2026-09-15\""
  summary: "(low confidence) One-day date drift on the BleepingComputer source; may be a timezone/publish-index artifact per the verification rules' own carve-out, not flagged as a hard F3."
```
