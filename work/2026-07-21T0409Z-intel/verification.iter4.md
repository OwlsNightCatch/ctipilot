**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-07-21T05:29:52Z · ended_at=2026-07-21T05:37:30Z · duration_seconds=458

## Verification report — 2026-07-21T0409Z-intel (iteration 4, confirmation pass)

Cold, independent read of all 8 new entries + run record. Did not anchor on iteration 3's CLEAN verdict — fetched every inline/sources[] URL myself, re-derived every evidence[] quote's contiguity against a fresh fetch of the cited page, and cross-checked every CVE/CVSS/entity/date/quantifier against the source actually cited.

### Fetches performed this iteration
- NCSC-CH post 12778 (bridge) — ServiceNow CVE-2026-6875 advisory: confirmed "Current exploitation status: Actively exploited" verbatim, CVSS 9.5, KB3137947 hotfix reference.
- BleepingComputer (ServiceNow ITW) — confirmed Defused attribution, CVE-2026-6875.
- Searchlight Cyber (ServiceNow sandbox-escape original write-up) — confirmed the `eval`/`new Function` sandbox-bypass sentence verbatim.
- Exodus Intelligence (dnsmasq) — confirmed both candidate quotes verbatim ("root cause... unsafe strcpy()"; "length of the string is not checked..."), CVE-2026-2291, fixed versions 2.92rel2/2.93 (2026-05-11), full-RCE vs. NVD's lower framing.
- Sysdig (JADEPUFFER/ENCFORGE) — raw HTML fetched via bridge; confirmed the "doubled down on that bet... a trained AI model" quote verbatim, "same operator with a materially upgraded toolkit" phrase present, "approximately 180" file-extension count, `lockd` on-disk filename, AES-256-CTR/RSA-2048.
- Proofpoint (Cruciferra) — confirmed both evidence quotes verbatim (ntdll stub-pointer sentence; "four campaigns attributed to... TA4922... AsyncRAT"), GoFlyDrv.sys/BYOVD/process-ghosting/ZwQueryVirtualMemory/NtManageHotPatch all present, additional packed families (Agent Tesla, DarkCloud, Formbook, XLoader, Phantom Stealer, Remcos, Snake Keylogger, ValleyRAT, XWorm, zgRAT) match body.
- Group-IB (HOLLOWGRAPH) — raw HTML fetched via bridge; confirmed both evidence quotes verbatim (high-confidence Cavern attribution sentence; "cannot confidently attribute... any previously identified threat actor"), Lyceum/OilRig low-confidence overlap, 2050-05-13 / 22:00–23:00 UTC calendar-event window, IPv6 AAAA DNS-tunneled Entra refresh, 12 infected / ~3 actively communicating, 3 June–9 July 2026 activity window.
- Hugging Face's own disclosure — raw HTML fetched via bridge; confirmed all three evidence quotes are contiguous verbatim substrings (including the parenthetical in quote 1, matching iteration-1's remediation), 17,000+ actions, guardrail-refusal/open-weight-model forensic detail.
- BleepingComputer + SecurityWeek (Hugging Face corroboration) — both independently report the incident.
- Searchlight Cyber (GPT5.6/WP2Shell) — confirmed both evidence quotes verbatim ("Total usage: 50%..."; "...no security researcher could have found and completed this exploit chain in 10 hours without AI" — sentence-initial capitalization of "No" is the only difference, standard quoting convention, not a splice), confirmed the batch-API/oEmbed/`parse_request`-hook mechanism matches the original 2026-07-18 entry's CVE-2026-63030/CVE-2026-60137 chain (this write-up itself doesn't restate the CVE numbers — they're correctly carried via `update_of` from the original entry, not falsely sourced to this article).
- Infosecurity Magazine (×4: Cruciferra, HOLLOWGRAPH, JADEPUFFER, WP2Shell) — each is a dedicated article corroborating the respective primary, not a homepage/listing.
- Digi24 (ANCPI) — confirmed databases-not-affected statement and 22 July Gov Cloud completion date.
- Risky Business News (ANCPI) — confirmed the "wiped systems and backups" quote verbatim.
- KELA Cyber (ByteToBreach profile) — confirmed the Zakaria Mahdjoub/Oran, Algeria attribution quote verbatim, victim sectors/countries, access-method list.
- Confirmed all four `update_of` targets exist as files (2026-07-13 ServiceNow, 2026-07-04 JADEPUFFER, 2026-07-18 WP2Shell, 2026-07-19 ANCPI) and that each update's delta is genuinely new (exploitation-status flip; new ENCFORGE payload; AI-capability angle on an unchanged CVE pair; contradiction + operator profile).
- Confirmed all new/referenced registry entities (`actor:jadepuffer`, `actor:ta4922`, `tool:cruciferra-crypter`, `tool:hollowgraph-malware`, `tool:cavern-c2-framework`, `actor:bytetobreach`, `incident:ancpi-romania-cyberattack-2026-07`, `incident:hugging-face-autonomous-ai-agent-breach-2026-07`) exist, are correctly typed, and relations (`uses`, `variant-of`, `attributed-to`) are sourced to the correct entry ids.
- Confirmed every `techniques[]` id (T1190, T1611, T1486, T1055, T1685, T1027, T1027.002, T1102.002, T1071.004, T1573, T1078.004, T1078, T1485, T1490, T1552) is active (not revoked/deprecated) in the pinned ATT&CK v19.1 dataset and maps to a behavior the body actually describes (T1685 = "Disable or Modify Tools" correctly maps Cruciferra's BYOVD EDR-kill).
- Ran `tools/check_run.py` myself: 35 pass / 1 warn / 1 fail. The FAIL is `verification-confirmation` (expected — this iteration's CLEAN is what resolves it). The WARN is a `dedup` note flagging that HOLLOWGRAPH shares entity `tool:cavern-c2-framework` with the 2026-07-09 Cavern Manticore entry; checked `prior_coverage.json` — the 2026-07-09 entry is about a SysAid-RMM-delivered modular C2 framework generally, while HOLLOWGRAPH is a distinct, newly-analysed implant (Group-IB, new M365-calendar-as-C2 technique, narrow Israeli victimology) correctly linked via a typed `variant-of` relation rather than merged/updated — the non-update decision is substantively correct; the run record's deep-dive-rotation note already carries the rationale even though it doesn't name the WARN explicitly. Not flagged as a numbered finding (verified correct, not a defect).
- Grepped all 8 entries for IOC patterns (IPs, hashes, defanged domains) — none found. Grepped for workflow-internal terms (`sub-agent`, `Phase N`, `spawn`, `main agent`) — none found (one `spawned from an unexpected parent` hit is legitimate process-lineage detection language, not pipeline jargon).
- Reviewed priority calibration: one `high` (ServiceNow exploitation-status flip on an already-patched, already-tracked CVE — correctly not `critical`, since it is neither newly disclosed nor missing a fix), seven `notable`; no entry plainly clears the `critical` bar undetected, none of the `notable` entries plainly clears the `critical` bar either (HOLLOWGRAPH's narrow, non-CH/EU-targeting victimology correctly keeps it at `notable` despite deep-dive treatment).
- Reviewed Admiralty classification codes against `sources/sources.json` reliability letters for every primary (NCSC-CH=A, Exodus=B, Sysdig=B, Proofpoint=B, Group-IB=B, Searchlight=B(untracked but consistent with peer standard-tier research labels), Hugging Face=A as first-party victim disclosure, Digi24=B) — all consistent; credibility numbers (mostly 2, ANCPI at 3 for the explicit contradiction) track the actual corroboration shown.
- Reviewed `actions[]` (4 total across 8 entries per `check_run.py`): each is a concrete, self-contained, non-generic, non-duplicate task derived from this run's own new mechanics (ServiceNow KB3137947 hotfix; dnsmasq version-verification; JADEPUFFER backup-isolation, distinct from the 2026-07-04 entry's Langflow-patch/credential-rotation/egress-filter actions; Hugging Face pre-vetted open-weight forensic model). No F18 violation.

### Editorial / less-is-more flags (advisory)

- **F11** — `2026-07-21/hollowgraph-m365-calendar-graph-api-c2-cavern`: the body's kill-chain paragraph reads "(`techniques[]` records the Graph-API dead-drop as bidirectional web-service C2 and the DNS-tunneled credential refresh as DNS application-layer C2)" — a direct reference to the entry's own frontmatter field name in reader-facing prose. Not a truth defect (the technique mapping itself is correct and well-explained elsewhere in the same paragraph), but it reads as pipeline-schema self-reference rather than natural analyst language. Advisory only; the main agent can leave it or tighten the wording (e.g. drop the `techniques[]` self-reference and just parenthesize the T-ids: "...(T1102.002, T1071.004)").

### Verdict

**CLEAN** — no truth or editorial defects found; one advisory (F11) the main agent may leave. This independently confirms iteration 3's CLEAN under the double-CLEAN publish gate (two consecutive CLEAN verdicts, two different models — Opus iteration 3, Sonnet iteration 4).

### Findings summary (machine-readable)

```yaml
- code: F11
  category: editorial-advisory
  section: identity-infra
  item: "2026-07-21/hollowgraph-m365-calendar-graph-api-c2-cavern"
  url_or_quote: "(`techniques[]` records the Graph-API dead-drop as bidirectional web-service C2 and the DNS-tunneled credential refresh as DNS application-layer C2)"
  summary: "Body prose references the frontmatter field name 'techniques[]' with bracket notation directly to the reader — pipeline-schema self-reference reads as internal jargon rather than natural analyst prose. Not a truth defect; a wording-only advisory the main agent can leave or tighten."
```
