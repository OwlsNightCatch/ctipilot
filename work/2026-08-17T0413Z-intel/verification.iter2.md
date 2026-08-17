**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-17T04:56:46Z · ended_at=2026-08-17T05:01:35Z · duration_seconds=289

## Verification report — 2026-08-17T0413Z-intel (iteration 2)

### Prior-iteration delta verification (all 5 confirmed correct)

1. **F3 (dates)** — confirmed. `src-3e264b0d.html` (The Hacker News) carries visible dateline "Aug 13, 2026" (no JSON-LD stamp present but dateline is unambiguous) → frontmatter now reads `2026-08-13`, correct. `src-eaed1390.html` (Security Affairs) carries `datePublished":"2026-08-16T07:24:53+00:00"` → frontmatter now reads `2026-08-16`, correct. `src-b47a0561.html` (BleepingComputer, Akira entry) carries `datePublished": "2026-08-13T16:47:02-04:00"` → frontmatter `2026-08-13`, correct. `src-d1d78467.html` (The Register) carries `datePublished":"2026-08-12T13:00:00.000Z"` → frontmatter `2026-08-12`, correct. All four corroborating-source dates now match their own structured stamps / visible datelines.

2. **F3 (chronology inversion)** — confirmed fixed and now accurate against `src-acronis-patchcord.txt` line 383: "Infrastructure pivoting identified an earlier campaign, observed in March 2026, targeting India's energy sector with a different PATCHCORD variant." The entry body now reads "A different PATCHCORD variant appears in what Acronis calls an earlier campaign, observed in March 2026 against India's energy sector … and it carries an anti-analysis suite the Afghan-telecom sample does not" — matches source line 401 ("The only notable difference we found with this variant of PATCHCORD is the inclusion of anti-analysis techniques which were not present in the earlier sample") under the only textually-supportable reading (the document describes exactly two PATCHCORD samples: the Afghan-telecom one, analysed first in the write-up, and the March-2026 energy-sector one; "the earlier sample" can only refer to the Afghan-telecom sample described earlier in the document's own narrative). The registry summary for `malware:patchcord` (entities/registry.yaml:4963) carries the identical corrected framing. No new unsupported claim was introduced by the rewrite.

3. **F11 (T1564.003)** — confirmed. `attack/enterprise-attack.json` lists `T1564.003` as `{"name": "Hidden Window", "deprecated": false, "revoked": false}` — active in the pinned v19.2 dataset. The body genuinely describes the behaviour twice: "PATCHCORD hides its console window" and SHEETCORD's startup script "launches the implant with a hidden window at every logon" — both textually present and both source-supported (`src-acronis-patchcord.txt` lines 154 and 353).

4. **F11 ("named victims")** — confirmed. The sentence now reads "The named targeting is Afghan telecom providers and South Asian government, defence and energy organisations, reached through sector-specific lures" — matches the source's own framing (targeting/lures, not compromised organisations). A full re-read of both entries for other overstated-compromise language found none.

5. **F11 (registry edge)** — confirmed correct. `campaign:operation-xenofiscal-sidecopy` now carries an `attributed-to` edge to `actor:apt36`, sourced to `2026-06-03/operation-xenofiscal-sidecopy-apt36-hits-provincial-treasury`. That entry's own cited primary (Seqrite Labs) states directly "SideCopy (Transparent Tribe / APT36, Pakistan-attributed)" — a stated attribution, correctly typed `attributed-to` rather than `overlaps-with`. This is a materially different (and correct) edge type from the three `overlaps-with` edges this run added from the Acronis PATCHCORD cluster to the same `actor:apt36` key, where Acronis itself states only a moderate-confidence overlap — the registry now correctly carries both relation strengths against the same actor key, sourced to the entry that actually makes each claim.

### Independent cold-read findings

None. Both entries were re-verified end to end against their saved primary captures (`src-huntress-akira.txt`, `src-acronis-patchcord.txt`) independent of the prior iteration's fixes:

- Every timestamp, event ID, registry path, and command string in the Akira entry (03:45/03:52:42 UTC spray→login, ~2h to hands-on, msconfig at 06:29:21 UTC, Kernel-Boot EID 27/Kernel-General EID 12, `reg.exe add …SafeBoot\Network\AnyDesk`, akira.exe at 06:34:29 UTC, System EID 26 cascade, Defender detection at 07:43:50 UTC, reboot-to-normal at 08:10:38 UTC, quarantine at 08:12:28 UTC, WinRAR flag string) is a verbatim or accurately-paraphrased match to `src-huntress-akira.txt`. All four `evidence[]` quotes are exact contiguous substrings of that capture.
- Every technical claim in the PATCHCORD/SHEETCORD/HACKERAI entry (five shortcut locations, `IShellLinkW`/`IPersistFile`, three→six browser widening, `VirtualAlloc`→`VirtualProtect(PAGE_EXECUTE_READ)`→`CreateThread`, Google Sheets API v4 service-account C2, GitHub Gist channel, the March-2026 anti-analysis checklist) matches `src-acronis-patchcord.txt`. All four `evidence[]` quotes are exact contiguous substrings.
- `techniques[]` on both entries maps cleanly to source-described behaviour with no bare/unsupported ids: Akira's `T1688` is the source's own cited ATT&CK id; PATCHCORD's in-memory shellcode execution is correctly `T1620` (Reflective Code Loading, in-process — not `T1055` process injection, since nothing is injected into another process).
- `classification: {reliability: B, credibility: 2}` on both entries matches `sources/sources.json`'s own catalogued reliability for `huntress` and `acronis-tru` (both `B`), and credibility `2` for a single-assessor, multi-republisher item is the org profile's own documented convention for this exact situation.
- `verification: single-source` + `sourcing_note` are present and correctly worded on both entries (F12 n/a).
- `org_triage: null` and `watchlist_hit: false` on both entries are correct — no triage scheme or watchlist is configured for this deployment; `check_run.py`'s own `org-triage` check confirms.
- `actions[]`: the Akira entry's single action is a concrete, self-contained, do-now task derived from this entry's own cited event IDs and registry path — not generic advice, not a restatement of the body's detection guidance (it names the specific registry values and event IDs to sweep for and the triage rule for hits). The PATCHCORD entry's empty `actions: []` is correct — nothing in the entry clears the do-now bar beyond the standing hunting/egress-monitoring guidance already carried in the body. No F18.
- `check_run.py 2026-08-17T0413Z-intel` re-run this iteration: 39 pass · 3 warn · 0 fail, matching the spawn message exactly. The three WARNs are the shared-`actor:akira` dedup confirmations; the run record's verification notes name the correct three prior entries (RUAG ransom-payment review, ESXi shell-obfuscation catalogue, Q2 ransomware weekly roll-up) for all three, and the non-update reasoning (none of the three describes this initial-access route or evasion step) holds up against a read of the actor-key co-occurrence.
- The borderline-drop (CRPx0 RaaS/HaaS brand) reasoning was checked against `src-bitdefender-crpx0.txt`: the source confirms concentrated US/Turkey dental-practice/technology/financial-services victimology with no home-region, coverage-focus, or profiled-sector nexus — the strike is correctly reasoned.
- No IOCs (hashes/IPs) leaked into either entry body; no workflow-internal language in the run record's verification notes.
- Coverage completeness: the run record's `fetch_failures` telemetry (CISA advisories/directives 403, Siemens ProductCERT CSAF 403, ccb-belgium/venarix reader-pool casualties) is transparently logged with mitigation reasoning per source; I found no additional in-window story a plausible search would surface beyond what is already logged as a gap.

### Verdict

CLEAN

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
[]
```
