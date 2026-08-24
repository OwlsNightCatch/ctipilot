**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-23T05:37:19Z · ended_at=2026-08-23T05:50:06Z · duration_seconds=767
**Self-telemetry:** urls_checked=14 · webfetch_calls=3 · bridge_fetches=6

## Verification report — 2026-08-23T0409Z-intel (iteration 2, delta-verify + cold read past deltas)

Scope: all 11 new entries end-to-end, the run record's frontmatter and § Verification & coverage notes, `work/2026-08-23T0409Z-intel/prior_coverage.json` (128 records), `state/cves_seen.json`, `entities/registry.yaml`, and the pinned `attack/enterprise-attack.json` (v19.2). Re-ran `python3 tools/check_run.py 2026-08-23T0409Z-intel` — still 40 pass · 0 warn · 0 fail after the iteration-1 remediations.

### Part 1 — iteration-1 deltas, verified

All fifteen iteration-1 remediations were checked against the current entry text and, where a source fetch was needed, against a freshly fetched copy of the source (not just the saved iter-1 snapshot).

- **F1** (bare EUVD homepage): fixed on the Entra ID entry (per-record URL, live-checked against the MSRC API and EUVD API this iteration — `baseScore 10.0`, `exploited: No`, revision 1.1 correction text all confirmed verbatim). **Partially fixed on misp-stix** — see new finding F3 below; the URL was corrected to a specific per-record page, but the entry needed three per-CVE EUVD records and only kept one.
- **F2** (blockchain 3-of-4 count): fixed correctly. Re-fetched Red Canary's post and re-derived the count myself: of the four new entrants (GraphSpy, Phexia, CastleRAT, EtherRAT), three use dead-drop resolution (confirmed: *"Three of the threats in our top 10 this month use dead drop resolution as a technique"*) and two of those three (Phexia, EtherRAT) read it from a public blockchain (CastleRAT reads `steamcommunity.com` or attacker domains). The entry's rewritten title/summary/body now state exactly this. `tags[]` also correctly dropped `mobile`.
- **F3** (TrueConf advisory date): fixed — now `2026-08-12`, matching the page's own `dateModified`.
- **F4** (CVE-2021-21551 score/auth): fixed — `cvss: "8.8"`, `auth: post-auth` on both driver CVEs; `sourcing_note` now correctly states the scores are the CNA's, not Talos's (Talos publishes none).
- **F5** (invented "Graph API"/"compromised" detail): fixed. Body now quotes Kaspersky's own wording (*"an account on Microsoft OneDrive cloud storage as their command-and-control (C2) server"*, verified literal against `securelist-headmare-stripped.txt`) and states explicitly that no source says the account was compromised. The detection-concept paragraph was rewritten to "a consumer cloud-storage service" — vendor-neutral, no longer resting on the invented detail.
- **F6** (T1027.002 unsupported): fixed — id removed from rust-crates `techniques[]`; the remaining seven ids all map to described, sourced behaviour (verified against Wiz + Rust Security Response Team text).
- **F7** (poc-public / espionage / mobile tags): fixed on both entries.
- **F8** (unreferenced entity keys): fixed — spot-checked spectre, uat-10147-agentic, blockchain, btr-sys, payload-zurich and rust-crates; every key each entry's `entities_added` registered is now referenced by that entry's own `entities[]`.
- **F9** (run-record miscounts): fixed — re-derived the counts myself from the eleven entries' frontmatter: 5 `high` (btr-sys, gtig-russia, rust-crates, spectre, trueconf) / 6 `notable` (blockchain, entra, martigny, misp-stix, payload-zurich, uat-10147-agentic), 12 actions across 9 entries, 2 with none (martigny, payload-zurich) — the run record's § Priority and action-item calibration now states exactly this.
- **F10 / F11** (BTR.sys quantifiers): fixed — the eighteen-build claim is now framed as a best-effort de-duplicated sample, and the filename length claim was replaced with "a randomised filename". (Worth a note, not a finding: the source article does separately state the randomised-filename pattern as `[a-z]{8}.sys` — line 461 of the saved Check Point text, in the driver-overview section that iteration 1's grep evidently didn't reach — so the removed eight-character detail was in fact source-supported. This is not a regression: the current text is accurate, just more conservative than it needed to be. No fix required.)
- **F12** (uncited CVE-2022-37042): fixed — id dropped, body now carries only Talos's own characterisation, `sourcing_note` updated to match.
- **F13** (em-dash/en-dash quote): fixed — quote shortened to the exactly-matching fragment.
- **F14** (unmapped technique behaviour): fixed — SPECTRE's body now describes process hollowing and APC EarlyBird injection explicitly (line 93); GTIG's body now describes the HTA downloader mechanism (line 75), both verified against the sources.
- **F15** (locale.php mischaracterised as JavaScript): fixed — body now states the extension/directory distinction explicitly.

Also re-confirmed, independently, everything iteration 1 said it verified and the spawn message asked me to re-test: all evidence quotes I re-checked (BTR.sys x5, SPECTRE x5, rust-crates x7, blockchain x5, all exact literal contiguous substrings of saved/freshly-fetched source text); the T1562.001→T1685 substitution (confirmed against the pinned dataset: T1685 active, T1562.001 `revoked: true, revoked_by: T1685`); all 45 unique technique ids across the eleven entries resolve and are active/non-revoked in the pinned v19.2 dataset; zero CVE overlap between this run's 8 CVEs and both `prior_coverage.json` (128 records) and `state/cves_seen.json`; the Martigny-Combe vector attribution and all its French quotes (re-fetched the newspaper article directly via curl past the same paywall shell that blocks a plain fetch, and the commune's PDF — every figure checks out: 450 recipients, ~300 emails, "Ce sont des mails à caractère confidentiel, contenant parfois des données sensibles", the year-long dark-net watch, the OFCS/cantonal/police notifications); the HWZ/Payload entry's German quote, data-class list, 490 GB figure and eight-domain count (re-fetched Inside Paradeplatz and the ransomware.live listing directly); priority calibration (5 high / 6 notable / 0 critical is right for this window — no item clears the stop-and-act-now bar); and action-item discipline (all twelve actions are concrete and self-contained, no generic advice, no restated detection guidance, no duplicates).

I did **not** find a coverage gap I could name a plausible in-window source for, beyond what the run record already discloses for cisa-advisories/cisa-directives.

### Part 2 — read past the deltas: new findings

### Citation does not support the claim

**F3 — misp-stix: a single EUVD record is cited to support EPSS/exploitation facts about three different CVEs, but the cited page documents only one of them.**

`entries/2026-08-23/misp-stix-import-trust-boundary-dos-parser-state.md` carries exactly one ENISA EUVD source record:

```yaml
  - url: "https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-63881"
    publisher: "ENISA EU Vulnerability Database"
    date: "2026-08-21"
    role: corroborating
```

and cites it inline for a claim about all three CVEs in the entry: *"None of the three is reported as exploited, and EPSS sits below 0.4% for all of them ([ENISA EU Vulnerability Database, 2026-08-21](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-63881))."*

I re-derived the EUVD id-to-CVE mapping from the saved `body.euvd-recent.json` (and this matches iteration 1's own F1 table, which the remediation evidently used for the *frontmatter* `cves[]` EPSS values but not for the *sources[]*/inline citation):

| CVE | Its own EUVD record | Its own EPSS | The one URL actually cited in this entry |
|---|---|---|---|
| CVE-2026-77710 | EUVD-2026-63850 | 0.29 | not cited anywhere in this entry |
| CVE-2026-77755 | **EUVD-2026-63881** | 0.30 | **this is the one cited** |
| CVE-2026-77761 | EUVD-2026-63883 | 0.37 | not cited anywhere in this entry |

The frontmatter `cves[]` block itself has the right EPSS values per CVE (0.29 / 0.30 / 0.37) — those are correct, and correctly distinct from each other. But the only citation a reader of the *body* can follow (EUVD-2026-63881) is CVE-2026-77755's record. It does not carry CVE-2026-77710's or CVE-2026-77761's EPSS or exploitation status at all — those live on two other EUVD pages that this entry never links. This is exactly the adjacency-check failure the verification contract calls out by name (check 2d): a trailing citation claiming facts about three items when it only speaks for one. The fact stated ("EPSS sits below 0.4% for all of them") happens to be true of all three CVEs, but the *citation* given does not establish that for two of the three — a reader clicking through gets confirmation for one CVE and nothing for the other two.

Fix: either add the two missing per-CVE EUVD source records (`EUVD-2026-63850` for CVE-2026-77710, `EUVD-2026-63883` for CVE-2026-77761) as additional `corroborating` entries and cite all three inline, or rephrase the sentence to cite only the claim the single record supports and attribute the other two EPSS/exploitation facts to the OSV-hosted MISP advisories already listed as `role: primary` (which do carry the CVE-specific text, just not the EPSS number).

### Editorial / less-is-more flags (advisory)

**F11 — entities linked in frontmatter but never named in the body prose, across three entries.**

Registry linkage is technically correct in all three cases (right key, right entity), so this is advisory rather than a hallucination, but it degrades the entity pages / `/graph/` surface a reader would land on from that link, because the entry gives them no textual anchor for why they arrived there:

- `gtig-russia-clusters-app-passwords-whatsapp-linking.md` — `entities: […, actor:midnight-blizzard, …, campaign:captivecrunch-storm-2945-hospitality-wifi]`. The body names "ICE RELIC" (line 67) but never says "Midnight Blizzard" — the ICE RELIC = Midnight Blizzard equivalence is stated only in the frontmatter `sourcing_note`, which a reader of the rendered entry does not see. The CaptiveCrunch campaign link is even less anchored: it is not mentioned anywhere in the body, only in the `sourcing_note` (*"GTIG itself ties it to the captive-portal activity previously reported by other vendors"*) — I re-fetched the GTIG source and confirmed the connection is real (*"UNC7005 in particular is tied to the hospitality captive portal redirects reported on by Reliaquest and Microsoft"*), so the link is correct, just unexplained on the page itself.
- `uat-10147-agentic-ai-exploitation-oob-confirmation.md` — `entities: [actor:uat-10147, tool:pentestgpt, tool:deepaudit]`. The body describes both tools functionally (*"a source-code vulnerability-scanning framework"*, *"an AI-driven penetration-testing tool used to scan web servers and run proof-of-concept exploits"*, line 82) but never uses the names PentestGPT or DeepAudit, even though Talos's own article names both explicitly (confirmed in `talos-agentic-text.txt`: *"they utilize DeepAudit for source code vulnerability scanning"*, *"installing the PentestGPT framework on their C2 server"*). A reader landing on `/entities/tool:pentestgpt/` from this entry has to take the registry's word for which paragraph is about it.

Not raised against `trueconf`'s PhantomHook/PhantomReact, which follows the same pattern (named in Kaspersky's AV verdicts, described but not named in the body) but is defensible there because the body explicitly states there are "two distinct backdoors" and describes each — the reader isn't left to guess which paragraph maps to which entity the way they are for the two cases above.

### Verdict

**NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)**

The run is in materially better shape than iteration 1 found it: every one of the fifteen prior findings landed correctly (fourteen fully, one — F1 on misp-stix — only partially, which is what F3 above re-raises), no remediation introduced a regression I could find, and the two hard editorial calls from iteration 1 (Berlin non-publication, Swiss provider naming restraint) both re-confirmed correct on independent re-reading. The residual blocker is narrow and mechanical: three of misp-stix's per-CVE facts are carried on one citation that only supports one of them. Fixing it is the same shape of fix iteration 1 already applied to the Entra ID entry on the same source family — add the two missing per-record URLs.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "2026-08-23/misp-stix-import-trust-boundary-dos-parser-state"
  url_or_quote: "None of the three is reported as exploited, and EPSS sits below 0.4% for all of them ([ENISA EU Vulnerability Database, 2026-08-21](https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-63881))"
  summary: "The entry's only EUVD source record (EUVD-2026-63881) is CVE-2026-77755's own per-record page (EPSS 0.30). It is cited inline to support an EPSS/exploitation claim about all three CVEs in the entry, but CVE-2026-77710 (EUVD-2026-63850, EPSS 0.29) and CVE-2026-77761 (EUVD-2026-63883, EPSS 0.37) each have their own distinct EUVD record, neither of which is cited anywhere in the entry. The frontmatter cves[] EPSS values are correct per-CVE; only the body citation and the sources[] list are incomplete. Add the two missing per-record URLs (matching the fix already applied to the Entra ID entry in this same run for the identical defect class) or narrow the inline claim to what the one cited record supports."
- code: F11
  category: editorial-advisory
  section: threat-landscape
  item: "2026-08-23/gtig-russia-clusters-app-passwords-whatsapp-linking + 2026-08-23/uat-10147-agentic-ai-exploitation-oob-confirmation"
  url_or_quote: "entities: [..., actor:midnight-blizzard, ..., campaign:captivecrunch-storm-2945-hospitality-wifi] / entities: [..., tool:pentestgpt, tool:deepaudit]"
  summary: "Four registry keys are correctly linked (right entity, right alias) but never named in the body prose the reader actually sees: Midnight Blizzard (body only says ICE RELIC; the alias equivalence is stated only in sourcing_note), the CaptiveCrunch campaign (mentioned only in sourcing_note, not in the body at all), and PentestGPT/DeepAudit (both described functionally but not named, even though the cited Talos article names both). Advisory only — the links are correct, just unanchored on the rendered page."
```
