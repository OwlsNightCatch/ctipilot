**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-02T05:51:42Z · ended_at=2026-09-02T06:04:44Z · duration_seconds=782

## Verification report — 2026-09-02T0411Z-intel (iteration 3)

### Prior-iteration deltas — walked and confirmed

All 9 iteration-2 findings were re-checked against a fresh fetch of their cited sources this iteration, independent of the remediation descriptions given:

1. "MiniUpdate" removal — confirmed. Securelist's attribution section says only "Retrograde/MiniFast" throughout; the current entry text says "Retrograde, which overlaps public reporting on the MiniFast family." No residual "MiniUpdate" found in the entry.
2. v1 TCP-port/C2 rewrite — confirmed correct against Securelist: "NodeRabbit binds a TCP listener to 127.0.0.1:48739. This listener acts as a single-instance mechanism... The malware communicates with its command-and-control servers through three API endpoints, choosing from the following Azure-hosted C2 infrastructure addresses." Matches the entry's current wording exactly.
3. Run-record 7-day demotion-window correction — confirmed; the run record now correctly states the 7-day lookback and acknowledges the two 30-day-window `apt-campaign` uses.
4. `state/coverage_backlog.md` work — confirmed genuinely done: `git diff HEAD -- state/coverage_backlog.md` shows the DGFiP/Cybernox and Swiss-Transparency-Register rows moved to `## Struck` with resolution notes, a new 2026-09-02 Krybit/UICC row added to `## Open`, and 2026-09-02-dated notes appended to the Zurich verdict, Siemens S7, OpenShift, Keycloak, Boston Scientific, Insel Gruppe and Ixa Systems rows.
5. "partial corporate-proxy traversal" — confirmed against Securelist: "Variant 2 implements partial corporate proxy support." Matches.
6. Delivery/NodeRabbit/PollCat per-clause citations — confirmed added and, on this iteration's own re-fetch of Securelist, accurate for the overwhelming majority of clauses (two new, distinct fidelity issues in this rewritten prose are reported below under Truth checks — not the same defects iteration 2 found, and not a regression of anything iteration 2 flagged).
7. JFrog classification.credibility 1→2 with sourcing_note — confirmed reasonable: the exploitation-confirmation claim traces to watchTowr, restated verbatim by NCSC-CH ("Additional Sources: x.com/watchtowrcyber... Note: WatchTowr social media post reporting active exploitation"), The Hacker News and SecurityWeek, none of which independently confirms it.
8. Missing `fields[]` entries on JFrog/WatchGuard update records — confirmed fixed; both records' `fields[]` now list every frontmatter key `git diff` shows changed.
9. NodeRabbit proxy-traversal technique-mapping decision (T1090 declined) — independently assessed: reasonable. T1090's canonical ATT&CK definition and its sub-techniques (Internal/External Proxy, Multi-hop, Domain Fronting) describe adversary-operated proxy *infrastructure* for outbound C2 obfuscation, not malware authenticating through a victim's own pre-existing corporate proxy to reach an already-mapped C2 channel (T1071.001). No better-fitting id was found either; declining was the right call.

New, distinct issues surfaced by this iteration's own re-fetch of the same sources are reported below.

### Unsupported / hallucinated facts

**#1.** `2026-09-02/mirage-kitten-noderabbit-pollcat-nodejs-rats` — "**Command and control.** All variants use AES-256-GCM-encrypted JSON over HTTPS (T1573.001, T1071.001) against Azure Websites..." Securelist documents AES-256-GCM encryption only for NodeRabbit ("NodeRabbit serializes each C2 request object as JSON and wraps it with AES-256-GCM"). The PollCat section describes plaintext-legible JSON request/response bodies (e.g. `POST /beacon` with `{"clientId":"<client-id>","type":"poll",...}` and an HTTP 400 response carrying `{"socketId":...}`) and says only "Commands and results are stored as little-endian binary records and carried as Base64 text" — Base64 encoding, not AES-256-GCM encryption, and no source statement that PollCat's transport itself is AES-256-GCM-encrypted. "All variants" overextends a NodeRabbit-specific fact to PollCat, which the paragraph's own placement (between the PollCat section and "Confirmed victims") makes clear it is meant to cover. Fix: scope the AES-256-GCM claim to NodeRabbit only, or cite a specific PollCat encryption detail if one exists in the source (none found on this reading).

**#2 (low confidence).** `2026-09-02/mirage-kitten-noderabbit-pollcat-nodejs-rats`, Delivery paragraph — "The NodeRabbit archive gives candidates three hours to \"fix the bugs\" in a project..." The quotation marks imply verbatim source language. Securelist's actual text: "The accompanying README instructed the candidate to review the application and fix defects in its frontend." No instance of the phrase "fix the bugs" appears in the fetched article. Fix: drop the quotation marks (this is a fair paraphrase, "fix defects" ≈ "fix the bugs") or replace with the source's own wording if a verbatim quote is wanted.

**#3 (low confidence).** `2026-08-31/watchguard-fireware-ike-vpn-preauth-rce-epm-overflow` — `techniques: [T1190, T1552.001]`. T1552.001 ("Credentials In Files") is placed to cover, among other things, CVE-2026-78174's Dimension session-hijack behavior: a low-privileged admin extracts a Super Administrator's *session token* from an unredacted diagnostic log to impersonate them. The pinned ATT&CK dataset's own definition of T1552.001 is narrower than this: "Adversaries may search local file systems and remote file shares for files containing insecurely stored credentials... configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords" — passwords/embedded credentials in files, not session cookies/tokens harvested from a log. T1550.004 ("Web Session Cookie" — "Adversaries can use stolen session cookies to authenticate to web applications and services... bypasses some multi-factor authentication protocols since the session is already authenticated") is a materially closer match to what WatchGuard's own PSIRT page describes ("harvesting the Super Administrator's session ID and CSRF token from the diagnostic log," "fully impersonate the Super Administrator"). Fix: replace or supplement T1552.001 with T1550.004.

**#4.** `2026-08-04/liechtenstein-vwbp-beneficial-ownership-register-breach` — the 2026-09-02 update record's `summary` and the body's new `## Update — 2026-09-02T04:50:00Z` section both state Switzerland's incoming Transparency Register covers "roughly 600,000 legal entities." The cited source for this section, Inside Paradeplatz (2026-08-31), states "**500'000** tatsächlichen Besitzer" (the Financial Times figure it relays), and the earlier-cited NZZ 2026-08-07 article gives no figure at all in the passage used. No source fetched on this entry states 600,000; the only concrete figure any cited source gives for the Swiss register's population is 500,000. This is a quantifier discrepancy, not a rounding difference (a 20% gap), appearing twice (frontmatter `updates[].summary` and the body section). Fix: change "roughly 600,000" to "roughly 500,000" (or cite whatever source actually supports 600,000, none found on this reading).

### Citation does not support the claim

**#5 (low confidence).** `2026-09-02/swiss-eid-trust-infrastructure-aws-veto-digital-sovereignty` — "Federal Councillor Beat Jans... vetoed the award in mid-February 2026... on the grounds that handing the task to a US hyperscaler subject to the US CLOUD Act would directly contradict the Federal Council's own digital-sovereignty objectives" is cited solely to Republik (2026-09-01). Republik's own text keeps the two facts separate: the CLOUD Act linkage is the journalist's own framing of the political risk ("Jans muss die politische Brisanz des Vorhabens gespürt haben. Das Outsourcing... an einen US-Konzern, der weitreichenden Überwachungsgesetzen wie dem amerikanischen «Cloud Act» unterliegt, wäre... auf viel Unverständnis gestossen"), while the digital-sovereignty veto rationale is attributed to insiders separately ("Eine Vergabe an den amerikanischen Big-Tech-Konzern würde den Plänen des Bundesrats für mehr digitale Souveränität der Schweiz diametral entgegenstehen, wie Insider aus dem Umfeld des Bundesrats bestätigen") with no CLOUD Act mention in that specific insider-sourced clause. The single-source citation to Republik for the merged claim is adjacency-thin; Inside IT Switzerland's paraphrase does merge the two ("Eine Vergabe an einen Konzern, der dem 'US Cloud Act' untersteht, würde den Plänen des Bundesrats für mehr digitale Souveränität... diametral entgegenstehen, hätten Insider... bestätigt") but is not the source cited for this clause. Low confidence because the overall claim is well supported by the totality of the three sources on the entry, just not cleanly by the one cited for this specific sentence. Fix: cite Inside IT alongside Republik for this sentence, or soften to separate the CLOUD Act observation from the sourced insider quote as Republik itself does.

### Claims missing inline citation

**#6.** `2026-09-02/swiss-eid-trust-infrastructure-aws-veto-digital-sovereignty`, final paragraph before "Defender takeaway" — "The E-ID's public launch is already delayed from end-2026 to the first half of 2027 for unrelated reasons — open questions on AHV-number lookups, AI-driven deepfake risk to online enrollment, and incompatibility with the EU's own eID system in its first version." No inline citation anywhere in this sentence, despite four distinct facts (delay dates, AHV-number issue, deepfake risk, EU incompatibility). All four are independently confirmed by the fetched Republik article, so this is a sourcing-hygiene gap, not a truth problem: fix by adding `([Republik, 2026-09-01](https://www.republik.ch/2026/09/01/e-id-bundesrat-beat-jans-stoppt-auftrag-an-amazon))` to the sentence.

### Editorial / less-is-more flags (advisory)

**#7 (low confidence).** `2026-09-02/mirage-kitten-noderabbit-pollcat-nodejs-rats` — `T1195.002` (Compromise Software Supply Chain) is mapped to "the malicious code sits in a locally bundled, never-registry-published npm package... imported by the assessment's own project files." The attacker authored the entire fake `TaskFlow`/`RankChallenge-react` project and its bundled package from scratch — there is no real upstream package, pipeline or maintainer being compromised, which is what T1195.002's definition and MITRE's own examples (source-code manipulation, update-mechanism manipulation, replacing compiled releases) describe. This reads closer to plain trojanized-file delivery (already mapped via T1204.002) than a supply-chain compromise. Worth a second look, not a confident F4 given "manipulation of the application source code... prior to receipt by a final consumer" is broad enough to arguably cover it.

**#8.** `2026-09-02/mirage-kitten-noderabbit-pollcat-nodejs-rats`, v3 paragraph — "...and Git post-merge/post-checkout hook injection, scanning up to 20 repositories under common project directories for one to inject into (T1547.001, T1053.005 / T1053.003 on the Linux side)." T1053.005/T1053.003 (Scheduled Task / Cron) are attached at the end of this clause, but the behavior they actually name — v3's own OS-specific persistence table (a daily 10AM Windows/WSL task, a Linux `@reboot` cron entry) — is never narrated anywhere in the entry's prose; only the git-hook mechanism (which the technique ids don't cover) is described in the sentence they're attached to. Bare-attached ids with no matching narrated behavior nearby is the F11 pattern check 10 calls out. Fix: either narrate v3's own scheduled-task/cron persistence explicitly, or move the T1053 ids to sit next to a sentence that describes it.

**#9 (low confidence).** `2026-09-02/dropbox-lenovo-id-sso-account-takeover` — the first `sources[]` record is `role: primary`, `publisher: "Reuters (via Free Malaysia Today)"` — a Malaysian news portal's syndication of a Reuters wire story, not Reuters' own site or a Dropbox/Lenovo statement. The entry already carries a stronger primary in the same array (9to5Mac, which obtained and quotes Dropbox's own breach-notification email directly — closer to a victim/vendor statement). Not a hard violation (the URL is a specific, non-blocked article), but the FMT reprint is a weaker choice than what the entry already has on hand for the lead primary slot.

### Verdict

`NEEDS_FIXES (truth: 6, editorial: 1, advisory: 3)`

Coverage note (check 13): given the dedup context (`prior_coverage.json`, `entities/registry.yaml`) and this run's own telemetry, I did not find an in-window relevant story the run's sources plausibly missed; the backlog handling (Boston Scientific, Insel Gruppe, Ixa Systems re-checks; new Krybit/UICC row) all check out against `state/coverage_backlog.md`'s diff. Coverage looks complete for this window.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "2026-09-02/mirage-kitten-noderabbit-pollcat-nodejs-rats"
  url_or_quote: "All variants use AES-256-GCM-encrypted JSON over HTTPS"
  summary: "Securelist documents AES-256-GCM encryption for NodeRabbit only; PollCat's C2 (POST /beacon JSON body, HTTP 400 response carrying {socketId}) is described only as Base64-carried binary records, with no statement that PollCat's transport is AES-256-GCM-encrypted."
- code: F4
  category: hallucinated-fact
  section: new-entries
  item: "2026-09-02/mirage-kitten-noderabbit-pollcat-nodejs-rats"
  url_or_quote: "gives candidates three hours to \"fix the bugs\" in a project"
  summary: "(low confidence) Quotation marks imply a verbatim source quote; Securelist's actual text is 'review the application and fix defects in its frontend' — the phrase 'fix the bugs' does not appear in the source."
- code: F4
  category: hallucinated-fact
  section: updated-entries
  item: "2026-08-31/watchguard-fireware-ike-vpn-preauth-rce-epm-overflow"
  url_or_quote: "techniques: [T1190, T1552.001]"
  summary: "(low confidence) T1552.001 (Credentials In Files, per the pinned ATT&CK dataset: passwords/embedded credentials in files) is a weak fit for CVE-2026-78174's session-token-theft-from-log behavior; T1550.004 (Web Session Cookie) is a materially closer match to WatchGuard PSIRT's own description of harvesting a session ID/CSRF token from a diagnostic log to impersonate an administrator."
- code: F4
  category: hallucinated-fact
  section: updated-entries
  item: "2026-08-04/liechtenstein-vwbp-beneficial-ownership-register-breach"
  url_or_quote: "roughly 600,000 legal entities"
  summary: "Cited source Inside Paradeplatz (2026-08-31) states the Swiss Transparency Register covers 'rund 500'000' beneficial owners (relaying the FT's figure); no fetched source on the entry supports 600,000. Appears in both the 2026-09-02 update record's summary and its body section."
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "2026-09-02/swiss-eid-trust-infrastructure-aws-veto-digital-sovereignty"
  url_or_quote: "vetoed the award ... on the grounds that handing the task to a US hyperscaler subject to the US CLOUD Act would directly contradict the Federal Council's own digital-sovereignty objectives"
  summary: "(low confidence) Cited solely to Republik, whose own text keeps the CLOUD Act observation (journalist's framing) and the digital-sovereignty veto rationale (insider-sourced quote) separate, with no CLOUD Act mention in the insider-sourced clause; Inside IT's paraphrase merges the two but is not cited for this sentence."
- code: F5
  category: missing-citation
  section: new-entries
  item: "2026-09-02/swiss-eid-trust-infrastructure-aws-veto-digital-sovereignty"
  url_or_quote: "The E-ID's public launch is already delayed from end-2026 to the first half of 2027 for unrelated reasons — open questions on AHV-number lookups, AI-driven deepfake risk to online enrollment, and incompatibility with the EU's own eID system in its first version."
  summary: "Zero inline citation on a sentence carrying four distinct facts, all independently confirmed by the entry's own already-cited Republik source."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "2026-09-02/mirage-kitten-noderabbit-pollcat-nodejs-rats"
  url_or_quote: "T1195.002 mapped to the locally-bundled, never-registry-published npm package"
  summary: "(low confidence) The attacker authored the entire fake project and its bundled package from scratch; no real upstream package/pipeline is compromised, so T1195.002 (Compromise Software Supply Chain) is a stretch versus plain trojanized-file delivery (T1204.002, already mapped)."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "2026-09-02/mirage-kitten-noderabbit-pollcat-nodejs-rats"
  url_or_quote: "(T1547.001, T1053.005 / T1053.003 on the Linux side)"
  summary: "T1053.005/T1053.003 are bare-attached to the Git-hook-injection clause; the scheduled-task/cron behavior they actually name (v3's own daily-task/cron persistence table) is never narrated in the entry's prose."
- code: F11
  category: editorial-advisory
  section: new-entries
  item: "2026-09-02/dropbox-lenovo-id-sso-account-takeover"
  url_or_quote: "publisher: \"Reuters (via Free Malaysia Today)\", role: primary"
  summary: "(low confidence) A Malaysian syndication of a Reuters wire story is a weaker primary choice than the entry's own 9to5Mac source, which obtained Dropbox's actual breach-notification email directly."
```
