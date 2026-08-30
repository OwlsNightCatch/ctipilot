**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-30T14:03:45Z · ended_at=2026-08-30T14:15:42Z · duration_seconds=717

## Verification report — 2026-08-30T1312Z-audit (iteration 2)

Scope read cold: the run record, the audit report, all 13 changelog-touched entries (full file + `git diff HEAD` for each), the 2 new entries under full normal-gate treatment, `work/2026-08-30T1312Z-audit/truth-B1/B2/B3.yaml` (independently re-aggregated by unique entry), `entities/registry.yaml` (spot checks), `attack/enterprise-attack.json` (technique validity), `sources/sources.json`, `state/cves_seen.json`, `state/coverage_backlog.md`, `prompts/cti-run.md` § Style rules (full re-read), `prompts/CHANGELOG.md`, `tools/kev_window_diff.py --help`, `tools/check_run.py` (frontmatter-yaml wiring), `python3 tools/check_run.py --all`, `python3 site/build.py`, `python3 tools/attack_data.py --check`. Fetched this iteration: NetSPI CVE-2026-21962 blog, SecurityWeek CVE-2026-21962 article, SOCRadar SNOWLIGHT report, Oracle CPU Jan-2026 advisory landing, api.osv.dev records for CVE-2026-60004/GHSA-rcr6-4jqh-j84m, Gitea GHSA advisory (jina, twice), Gitea 1.27.1 release blog, Help Net Security CVE-2026-60004 article, CERT/CC VU#308749 (jina).

### Prior-iteration deltas walked (all confirmed correct except as noted below)

1. **Verdict counts (F4, iter1 #1).** Independently re-aggregated `truth-B1.yaml` (15 entries: 5 clean / 4 factual-error / 6 imprecision), `truth-B2.yaml` (15 entries: 5 clean / 6 factual-error / 4 imprecision), `truth-B3.yaml` (14 entries: 9 clean / 1 factual-error / 4 imprecision) by unique entry — totals **19 clean / 11 factual-error / 14 imprecision, 44 entries**, matching the current run record and audit report exactly, with Kaltura correctly folded into the 11 (as the entry the "eleventh" paragraph names, handled via `update`). The "six of the eleven" quotation-drift figure reconciles: doj-fbi-qscan, unisoc-volte, cncmachinerms, kudelski-bismarck, manchester-airports, protection-civile-france = 6; the "two of the eleven" world-changed figure = Kaltura + Zbtlink = 2; "the remaining three" = owncloud (EPSS), claroty-copeland (CVE binding), cve-2026-53362 (auth field) = 3. 6+2+3=11. **Confirmed correct, no residual.**
2. **`cve-2026-53362` fields (F4, iter1 #2).** `git diff HEAD` confirms `fields: [cves, body]`, matching the body-section addition. **Then checked all other 12 changelog records' `fields[]` against their own diffs** (not just this one, per the task): `cve-2026-42897` `[actions, classification]` ✓, `sekoia-consolidates-gamaredon` `[actions, classification, techniques, evidence]` ✓, `endlessdoors-zbtlink` `[summary, body]` ✓, `claroty-copeland` `[cves, sourcing_note, actions, body]` ✓, `cncmachinerms` `[evidence, body]` ✓, `doj-fbi-qscan` `[title, evidence, body]` ✓, `kaltura` `[title, summary, tags, cves, body, updated_at]` ✓, `kudelski-bismarck` `[body]` ✓, `manchester-airports` `[summary, body]` ✓, `owncloud` `[cves, body]` ✓, `protection-civile-france` `[evidence, body]` ✓, `unisoc-volte` `[title, summary, affected_products, body]` ✓. All 13 correct. **Confirmed, no residual.**
3. **Copeland/Protection-Civile summary rewrites (F11, iter1 #4/#3).** Confirmed both rewritten summaries are now clean of the flagged phrases. **However, re-scanning every `sourcing_note` field (a reader-facing field per `cti-run.md` § Style rules' own list) across the WHOLE entry — not just the new changelog records — surfaced a much larger, systemic instance of the identical defect class the run's own report claims is "mostly took, one leak." See F11 findings below: this is not one leak, it is at least nine.**
4. **Declined finding ("sub-agent"/"Phase 0 step 6b" in the run record).** Re-read `prompts/cti-run.md` § Style rules (line 555) directly: the "no internal-policy shorthand" rule explicitly enumerates the fields it binds — "entry title, headline, summary, sourcing_note, body, changelog sections" — and its own text states "selection and mapping rationale belongs in the run record". Line 563 repeats this: "Selection and mapping rationale goes in the run record." **On a plain reading of `cti-run.md` itself, the decline's textual reading holds** — the rule does not name the run record among the fields it binds, and the same passage affirmatively assigns exactly this kind of narration to the run record. I do not disagree with the decline on this specific textual question. Separately (not a disagreement, a flagged tension): my own governing check 12 states the prohibition covers "any entry or in the run-record notes" — broader than `cti-run.md`'s own scope list — so there is an unreconciled inconsistency between the two documents worth a future prompt-editing pass; it does not change my read of what `cti-run.md` itself says.

### Unsupported / hallucinated facts

**#1 (F3, adjacency/splice).** `entries/2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev.md` title: *"KEV-listed after seven months of exploitation against government infrastructure."* This splices two unrelated facts from two different cited sources as one continuous claim. SecurityWeek (fetched this iteration): "the vulnerability has been exploited since January" — CloudSEK's honeypot telemetry, with no sector/target attribution anywhere in the article. SOCRadar (fetched this iteration): the government-domain targeting comes from a *different* dataset — "the artifacts span a six-week operational window" of one exposed operator's staging server, and SOCRadar explicitly does not tie this CVE to any specific intrusion (the entry's own body correctly hedges this point: "SOCRadar does not tie any specific intrusion to this CVE"). The title nonetheless binds the 7-month CloudSEK exploitation window to the 6-week SOCRadar campaign's government-heavy reconnaissance list as if they describe the same exploitation activity — exactly the "count or as-of date spliced from one figure onto another figure's context" pattern this same audit's report names as its own dominant defect class (found in the DOJ/QTFY entry, among others), reproduced here in a brand-new entry this run composed.

**#2 (F4, entity-linking miss).** `entries/2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev.md` `entities: ["product:oracle-weblogic-server", "actor:unc5174", "actor:unc6586", "malware:snowlight"]`. This run's own `entities_added:` list (run record) registers two NEW keys specifically for this entry's subject matter — `product:oracle-http-server` and `product:oracle-weblogic-server-proxy-plug-in` (both `first_seen: 2026-08-30`, no aliases linking them to the generic key) — matching exactly the two components named in `affected_products[]` and `cves[0].affected`. Neither new key is referenced anywhere in the entry's own `entities[]`; instead the entry cites `product:oracle-weblogic-server`, a different, pre-existing, more general product (the backend the flaw only *pivots into*, per the body's own "pivot path into backend WebLogic clusters" framing) which is not itself listed as an affected product. The two keys this run registered are consequently orphaned — no entry links them, defeating the point of registering them.

**#3 (F4, technique contradicted by its own cited source).** `entries/2026-08-30/cve-2026-60004-gitea-diffpatch-git-hook-rce-kev.md` `techniques: [T1190, T1505, T1543, T1496, T1552.001]`. T1543 = "Create or Modify System Process" (systemd/launchd/Windows-service persistence, per the pinned dataset's own definition). The entry's own cited Help Net Security article (fetched this iteration) states explicitly: *"No traces of persistence via cron, systemd, or new SSH keys were found during the investigation."* The entry's body never describes a system-process/service creation or modification anywhere — the described chain is a one-shot RCE via Git-hook installation. T1543 is not merely unsupported, it is affirmatively negated by the entry's own source.

**#4 (low confidence, F4, technique not clearly supported).** `entries/2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev.md` `techniques: [T1190, T1090, T1133]`. T1090 = "Proxy" (an adversary using a connection proxy to disguise C2 traffic, per the pinned dataset's definition). Nothing in the entry or its three cited sources (NetSPI, SecurityWeek, SOCRadar) describes an attacker using a proxy for C2 — the "proxy" in this entry is the *target software component* (WebLogic Server Proxy Plug-in), a different sense of the word entirely. T1133 ("External Remote Services" — VPN/Citrix/VNC-class remote-access gateways) is also a stretch for an HTTP reverse-proxy exploit better covered by T1190 alone; flagged with lower confidence than T1090 since the entry's own framing ("the trusted boundary," "gateway") gives it some argument.

### Surface contradiction

**#5 (F9).** `entries/2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev.md`. SecurityWeek (fetched this iteration): *"The remote code execution flaw, identified as CVE-2026-21962... affects Oracle HTTP Server and the WebLogic Server Proxy plugin."* NetSPI, the entry's own primary (fetched this iteration): describes only "unauthorized read/write access to sensitive data... Potential pivoting into backend WebLogic clusters" — no mention of code execution anywhere in the article. The entry's `cves[0].type: auth-bypass` and its body ("yields unauthorized read and write access... plus a route into the backend WebLogic clusters") silently adopt NetSPI's framing without a `Contradiction:` line disclosing that a second cited source characterises the same flaw as RCE.

### Editorial / less-is-more flags (advisory) — systemic pipeline self-reference in `sourcing_note` (check 12 / § Style rules)

The run's own report (finding 4, "Fix effectiveness") states the 2026-08-28 internals-out-of-reader-text fix is "mostly took, one leak" (the `2026-08-29/servicenow-ai-platform-…` `sourcing_note`). Re-scanning `sourcing_note` — an explicitly reader-facing field per `cti-run.md` line 555's own field list — across the WHOLE scope (not just this run's new sections) finds this is not one leak; it is systemic, present in most of the entries this run itself touched, and freshly introduced in both of this run's own brand-new entries. `cti-run.md` line 563 explicitly names the exact pattern as a defect requiring deletion: *"referencing the production process ('as of this run', 'this run's own re-check' — use the date instead)."*

**#6.** `entries/2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev.md` — `sourcing_note`: *"Recovered by the 2026-08-30 quality audit's coverage re-sweep: the KEV addition of 2026-08-24 fell inside the 2026-08-28 catch-up fire's window and was never surfaced"* and *"The Oracle Critical Patch Update advisory itself was not re-fetched this run."* Both are production-process narration in a brand-new entry.

**#7.** `entries/2026-08-30/cve-2026-60004-gitea-diffpatch-git-hook-rce-kev.md` — `sourcing_note`: *"Recovered by the 2026-08-30 quality audit's coverage re-sweep: the KEV addition of 2026-08-25 fell inside the 2026-08-28 catch-up fire's window and was never surfaced, so this is first coverage."* Same pattern, second brand-new entry.

**#8.** `entries/2026-08-28/cve-2026-53362-linux-kernel-ipv6-udp-fraggap-kev.md` — `sourcing_note`: *"...the 'who/how' of exploitation unstated by any source read this run."*

**#9.** `entries/2026-08-28/claroty-copeland-xweb-pro-refrigeration-unauth-root-rce.md` — `sourcing_note`: *"could not be located or fetched this run"* and *"no individually published identifier or per-flaw detail located this run."*

**#10.** `entries/2026-08-28/cncmachinerms-babadeda-loader-enumtimeformats-shellcode.md` — `sourcing_note`: *"its full technical report is a companion PDF not independently fetched this run."*

**#11.** `entries/2026-08-28/kaltura-mwembed-unauth-rce-file-read-no-patch.md` — `sourcing_note`: *"CERT/CC's own vulnerability-note page... returned a corrupted/binary body on every transport this run."*

**#12.** `entries/2026-08-28/protection-civile-france-eprotec-breach-volunteers.md` — `sourcing_note`: *"Publication date (2026-08-21) predates this run's recency window."*

**#13.** `entries/2026-08-28/unisoc-volte-mpu-isolation-bypass-android-kernel.md` — `sourcing_note`: *"SSD Secure Disclosure's own posts... were unreachable on every transport this run."*

**#14.** `entries/2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen.md` — main analysis BODY (not sourcing_note, not a changelog section — the July-31 `## Update` prose): *"The actor is TA488, which Microsoft tracks as Void Blizzard and which **this pipeline** registers as LAUNDRY BEAR."* An explicit self-reference to the store's own registry naming convention, in reader-facing prose. Pre-existing (not touched by this run's `[actions, classification]` record), but a live defect in a currently-in-scope entry this run re-classified.

None of #6–#14 is confined to this run's own new changelog text (only #6/#7 are literally new prose from this run; #8–#14 predate it), so this is a store-wide pattern this audit's own systemic review (finding 4 of the report) should have caught and did not — its own remediation-effectiveness claim ("one leak") is itself now inaccurate given nine further instances found on a single field-name grep across the 15-entry scope.

### Editorial — action-item discipline

**#15 (low confidence, F18).** `entries/2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev.md` `actions[]`. Action 1 ("Inventory Oracle HTTP Server and WebLogic Server Proxy Plug-in instances... Check deployment manifests and container images as well as installed hosts: the plug-in ships bundled, so it is routinely missed by inventories keyed on WebLogic Server itself.") closely restates the body's own "**Defender takeaway:** find the plug-in, not the server... estates that inventory WebLogic Server by name routinely miss it." Action 2 ("Treat an unpatched, internet-reachable instance as a compromise-assessment candidate rather than a patching ticket... seven months of exposure is the working assumption.") closely restates the body's own "**Exploitation is not new, only the listing is**" paragraph. Both add some concrete specificity (version numbers, DMZ priority) beyond the body's prose, so this is flagged low confidence rather than a clear-cut violation.

### Quantifier / date check

**#16 (low confidence, F3).** `entries/2026-08-30/cve-2026-60004-gitea-diffpatch-git-hook-rce-kev.md`: `cves[0].fixed: "Gitea 1.27.1 (2026-07-28)"`, `sources[0].date: "2026-07-28"` (the Gitea GHSA advisory). Gitea's own official release announcement (`https://blog.gitea.com/release-of-1.27.1/`, fetched this iteration, not cited by the entry) carries dateline `2026-07-27` — one day earlier. Neither of the entry's two cited sources independently states the specific date "2026-07-28" in the text I could extract (the GHSA advisory's metadata sidebar did not render through `extract`/`url`/`jina`; Help Net Security only says "last month"). One day of drift may be a timezone artifact per check 2(e); flagged low confidence since I cannot confirm which date is authoritative from the entry's own citations.

### What I confirmed holds (no defect)

- Verdict-count reconciliation (19/11/14, Kaltura as the 11th via `update`) — independently re-derived, matches exactly (see delta #1 above).
- All 13 changelog records' `fields[]` match their own `git diff HEAD` output (see delta #2).
- `updated_at` moved on exactly Kaltura across all 13 records; `discovered_at`, `run_id`, path untouched on every entry.
- Internal records (`cve-2026-42897`, `sekoia-consolidates-gamaredon`) carry no body section; every non-internal record has its matching `## <Type> — <at>` section.
- Kaltura's `## Update` section verified verbatim against CERT/CC VU#308749 (fetched independently this iteration via jina): "Solution" text and "Date Last Updated: 2026-08-28 19:59 UTC" both match exactly.
- CVE-2026-21962: CVSS 10.0, affected versions (12.2.1.4.0/14.1.1.0.0/14.1.2.0.0 HTTP Server+Proxy; 12.2.1.4.0 IIS plug-in), and both `evidence[]` quotes from NetSPI verified verbatim against the live page; SecurityWeek's two quotes verified verbatim; SOCRadar's UNC5174/UNC6586/SNOWLIGHT attribution and CVE-2026-21962's presence in the toolkit table verified against the live page; both actor/malware registry keys pre-exist (no new-entity gap on those three).
- CVE-2026-60004: both Gitea-advisory `evidence[]` quotes and the Help Net Security quote verified verbatim; CVSS 9.8/CWE-94/fixed-in-1.27.1 independently cross-checked via `api.osv.dev` (not cited by the entry, used here only for my own ground-truth check); the "about 11 seconds" and mining/shell-loader narrative match Help Net Security's article exactly; `product:gitea` registry key exists.
- No IOCs in either new entry or any changelog section. Classification blocks present and plausible on both new entries (B/1 for Oracle given three-source corroboration on different facts; A/1 for Gitea given first-party vendor advisory + independent corroborating outlet).
- `state/coverage_backlog.md`: 11 open rows (5 carried-forward + 6 new dated 2026-08-30), 2 new struck rows (CVE-2026-21962, CVE-2026-60004) dated 2026-08-30 — matches the "2 struck, 11 open" claim exactly.
- `tools/kev_window_diff.py` exists and `--help` runs; `check_frontmatter_yaml_portability` wired at both the `--all` call site (all store entries) and the run-scope call site (run's own entries + own run record).
- Both prompt banners read v4.8; `prompts/CHANGELOG.md` has a matching `## 4.8` head entry.
- `sources/sources.json` carries `symantec-security-com`; `state/cves_seen.json` carries both CVE-2026-21962 and CVE-2026-60004.
- `python3 tools/attack_data.py --check`: local v19.2 == upstream latest v19.2.
- `python3 site/build.py`: single clean summary line, no self-check warnings.
- `python3 tools/check_run.py --all`: 24 pass · 0 warn · 2 fail · 25 acknowledged. The 2 FAILs (`verification_residual_count 0 != final truth+editorial 2` / `residual count 0 on a NEEDS_FIXES final iteration`) are the expected mid-loop state — the run record's `verification.iterations[]` currently ends at n=1 (NEEDS_FIXES, truth=2/editorial=0) and `verification_residual_count` has not yet been updated to reflect that outstanding count, because this iteration's (n=2) verdict has not yet been appended. This resolves once the main agent records this iteration's outcome, exactly as iteration 1 characterised its own analogous mid-loop FAIL. Not a new defect.

### Verdict

`NEEDS_FIXES (truth: 5, editorial: 2, advisory: 11)`

Truth: #1 (F3 title splice), #2 (F4 entity-linking miss), #3 (F4 technique contradicted by source), #4 (F4 technique unsupported, low confidence), #16 (F3 date drift, low confidence).
Editorial: #5 (F9 surface contradiction), #15 (F18 action-item overlap, low confidence).
Advisory: #6–#14 (F11 systemic sourcing_note/body pipeline self-reference, 9 instances).

All four of iteration 1's findings were correctly remediated or, for the one declined, correctly declined on a plain reading of `cti-run.md` itself. The new findings surfaced this iteration are concentrated in the two brand-new entries (which iteration 1's own scope description never mentioned reading) and in a systemic `sourcing_note` self-reference pattern the run's own report believed was reduced to a single known leak.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev"
  url_or_quote: "KEV-listed after seven months of exploitation against government infrastructure"
  summary: "Title splices CloudSEK's 7-month (untargeted) exploitation window with SOCRadar's separate 6-week government-heavy campaign staging-server finding; SOCRadar itself does not tie this CVE to a specific intrusion, and the entry's own body says so, but the title states the compound claim as one fact."
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev"
  url_or_quote: "entities: [\"product:oracle-weblogic-server\", ...]"
  summary: "entities[] omits the two registry keys this very run added (product:oracle-http-server, product:oracle-weblogic-server-proxy-plug-in) for exactly this entry's affected products, using a different, non-affected, pre-existing product key instead; the two new keys are referenced by no entry."
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "2026-08-30/cve-2026-60004-gitea-diffpatch-git-hook-rce-kev"
  url_or_quote: "techniques: [..., T1543, ...]"
  summary: "T1543 (Create or Modify System Process) is contradicted by the entry's own cited Help Net Security article: 'No traces of persistence via cron, systemd, or new SSH keys were found during the investigation.'"
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev"
  url_or_quote: "techniques: [T1190, T1090, T1133]"
  summary: "(low confidence) T1090 (Proxy, a C2-evasion technique) matches no described attacker behavior; the entry's 'proxy' is the vulnerable target software, not an ATT&CK proxying behavior. T1133 is also a stretch given the entry's own web-facing HTTP framing."
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "2026-08-30/cve-2026-60004-gitea-diffpatch-git-hook-rce-kev"
  url_or_quote: "cves[0].fixed: \"Gitea 1.27.1 (2026-07-28)\""
  summary: "(low confidence) Gitea's own release blog (not cited by the entry) is dated 2026-07-27, one day earlier; neither cited source states the specific date 2026-07-28 in extractable text."
- code: F9
  category: surface-contradiction
  section: new-entries
  item: "2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev"
  url_or_quote: "SecurityWeek: \"The remote code execution flaw...\" vs NetSPI (primary): unauthorized read/write access only, no RCE mentioned"
  summary: "Two cited sources characterise the flaw's technical nature differently (RCE vs access-control bypass); the entry silently follows NetSPI's framing with no Contradiction: line."
- code: F18
  category: action-item-discipline
  section: new-entries
  item: "2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev"
  url_or_quote: "\"Inventory Oracle HTTP Server and WebLogic Server Proxy Plug-in instances...\" / \"Treat an unpatched, internet-reachable instance as a compromise-assessment candidate...\""
  summary: "(low confidence) Both actions closely restate the body's own 'Defender takeaway' and 'Exploitation is not new' paragraphs rather than adding a distinct task."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "2026-08-30/cve-2026-21962-oracle-http-server-weblogic-proxy-plugin-kev"
  url_or_quote: "sourcing_note: \"Recovered by the 2026-08-30 quality audit's coverage re-sweep...\" / \"not re-fetched this run\""
  summary: "Production-process self-reference in a reader-facing field, the exact pattern cti-run.md line 563 bans ('as of this run' — use the date instead)."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "2026-08-30/cve-2026-60004-gitea-diffpatch-git-hook-rce-kev"
  url_or_quote: "sourcing_note: \"Recovered by the 2026-08-30 quality audit's coverage re-sweep...\""
  summary: "Same pattern, second brand-new entry."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-08-28/cve-2026-53362-linux-kernel-ipv6-udp-fraggap-kev"
  url_or_quote: "sourcing_note: \"...unstated by any source read this run.\""
  summary: "Same pattern, pre-existing (not introduced by this run's own record)."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-08-28/claroty-copeland-xweb-pro-refrigeration-unauth-root-rce"
  url_or_quote: "sourcing_note: \"could not be located or fetched this run\" / \"located this run\""
  summary: "Same pattern, pre-existing."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-08-28/cncmachinerms-babadeda-loader-enumtimeformats-shellcode"
  url_or_quote: "sourcing_note: \"not independently fetched this run\""
  summary: "Same pattern, pre-existing."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-08-28/kaltura-mwembed-unauth-rce-file-read-no-patch"
  url_or_quote: "sourcing_note: \"...on every transport this run\""
  summary: "Same pattern, pre-existing."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-08-28/protection-civile-france-eprotec-breach-volunteers"
  url_or_quote: "sourcing_note: \"predates this run's recency window\""
  summary: "Same pattern, pre-existing."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-08-28/unisoc-volte-mpu-isolation-bypass-android-kernel"
  url_or_quote: "sourcing_note: \"unreachable on every transport this run\""
  summary: "Same pattern, pre-existing."
- code: F11
  category: editorial-advisory
  section: updated-entries
  item: "2026-05-18/cve-2026-42897-exchange-owa-em-service-auto-mitigation-depen"
  url_or_quote: "body: \"...which this pipeline registers as LAUNDRY BEAR\""
  summary: "Self-reference to the store's own registry naming convention in main-analysis prose (not a changelog section); pre-existing, from the 2026-07-31 update, in an entry this run re-touched for classification."
```
