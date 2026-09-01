**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-01T06:23:13Z · ended_at=2026-09-01T06:35:28Z · duration_seconds=735

## Verification report — 2026-09-01T0411Z-intel (iteration 6)

### Prior-iteration deltas — walked and confirmed

1. JFrog CVE-2026-66384 severity fix (F4, iter 5): confirmed against a live fetch of `docs.jfrog.com/releases/docs/jfrog-security-advisories` — the table lists `Medium | CVE-2026-66384 | ... Docker cache path ... | <7.146.35; 7.161.0->7.161.16`. The rewritten sentences ("Medium-severity, KEV-listed CVE-2026-66384", "this critical-severity flaw is the more severe of the two") now match. Fixed correctly.
2. Anthropic title "sessions" fix (F4, iter 5): confirmed — title now reads "...Anthropic mass-revokes sessions compromised via..." consistently with body/summary/headline. See new finding #7 below on a different word in the same clause.
3. ValleyRAT svchost/60-second rewrite (F3, iter 5): confirmed verbatim against Securelist: "The backdoor allocates memory inside the svchost process, injects code into it, and sets PAGE_NOACCESS permissions ... waits 60 seconds, grants read, write, and execute permissions on the page, and resumes the thread." The rewritten Defender-takeaway/Triage sentences ("toggles from no-access to fully executable roughly a minute after code injection") match this exactly and no longer assert an unstated child-process/timing claim. Fixed correctly.
4. Anthropic Triage citation (F5, iter 5): confirmed — the "refilled and then drained" quote is now inline-cited and present in `evidence[]`, verified verbatim against BleepingComputer's article. Fixed correctly.
5. Liechtenstein/transparency-register backlog judgment (F10, iter 5): independently re-searched (see Whole-run checks below) — the underlying reasoning holds up under a fresh check.
6. ValleyRAT T1055/T1055.012 split (F11, iter 5): confirmed both ids are active in the pinned ATT&CK v19.2 dataset, and the split is technically sound — Securelist calls "process hollowing" only for the shellcode-module-loading path ("If the payload is shellcode, the backdoor uses process hollowing with svchost to launch the module"), while the svchost watchdog-injection path is a distinct allocate/PAGE_NOACCESS/wait/RWX sequence Securelist never labels "hollowing." Fixed correctly.

All six prior findings were verified fixed with no regression. Independent cold pass below surfaced new findings.

### Citation does not support the claim

**#1.** `2026-09-01/jfrog-artifactory-cve-2026-82329-default-config-admin-bypass.md` — body states: *"JFrog's summary advisory table names the same six fixed versions but its 'Versions' column displays the 7.111 **and 7.146** branch ranges inconsistently with itself — for 7.111 it prints the fixed version, 7.111.21, as the range's own end rather than the last affected build."* A live fetch of the cited `https://docs.jfrog.com/releases/docs/jfrog-security-advisories` today shows the CVE-2026-82329 detail table as: `7.161.0 > 7.161.19 → 7.161.20` / `7.146.0 > 7.146.36 → 7.146.38` / `7.133.0 > 7.133.28 → 7.133.29` / `7.125.0 > 7.125.19 → 7.125.20` / `7.117.0 > 7.117.27 → 7.117.28` / `7.111.4 > 7.111.21 → 7.111.21`. Only the 7.111 row shows the "fixed version repeated as the affected range's own end" quirk (`7.111.4 > 7.111.21`, fix `7.111.21`); the 7.146 row (`7.146.0 > 7.146.36`, fix `7.146.38`) is internally consistent — 36 ≠ 38, exactly as the entry's own affected/fixed frontmatter states. Naming "7.146" alongside 7.111 as also displaying this inconsistency is not supported by the source as it stands today. This reads as a residual of an earlier, *different* 7.146 defect (iteration 1's fix of a hallucinated 7.146.37) that was never fully reconciled with iteration 4's new 7.111-specific explanation. Fix: drop "and 7.146" from the sentence, or restrict the explanation to 7.111 only.

**#2 (low confidence).** `2026-08-23/payload-zurich-it-provider-hwz-student-data.md` — Update section states as settled fact: *"the ransomware group behind the provider-side intrusion has published data from the breach"*. Inside IT's 2026-08-31 article (`https://www.inside-it.ch/hwz-daten-landen-im-darkweb-20260831`) is paywalled beyond its opening two paragraphs, but its own meta description — part of the same page — hedges: *"Hinter dem Angriff auf einen externen IT-Dienstleister der Hochschule steckt **offenbar** eine Ransomware-Bande. Sie hat Daten veröffentlicht."* ("apparently a ransomware gang" is behind the attack). The entry drops "apparently" and states the ransomware-group attribution as fact. Low confidence because the visible/extractable text is thin (paywall) and the headline itself ("HWZ-Daten landen im Darkweb") does assert publication as fact — only the actor-attribution clause carries the hedge. Fix: soften to "apparently a ransomware group" or attribute the hedge to Inside IT.

### Needs more research

**#3.** `2026-08-29/exchange-mrsproxy-auth-bypass-cve-2026-62911-poc.md` — this run's own changelog record escalated `cves[].auth` from `post-auth` to `pre-auth` and rewrote the body to state *"any Exchange server below the August 2026 build should be treated as exposed to unauthenticated, mailbox-wide access once an attacker can coerce or capture a Negotiate authentication exchange directed at MRSProxy"*, explicitly weighing CERT-Bund/NCSC-NL's "unauthenticated" language over MSRC's own CVSS vector (`PR:L/UI:R`, "authorized attacker"). Following a comment-link from Franky's Web (one of the entry's own cited sources) to a detailed third-party technical write-up — MB VRED, "Analysis of Exchange Server Pre-Auth RCE (CVE-2026-62911)", `https://vred.mbbank.com.vn/p/analysis-of-exchange-server-pre-auth`, dated 2026-08-13 — the actual mechanics are considerably more constrained than the entry's framing suggests: the `/Microsoft.Exchange.MailboxReplicationService.ProxyService` MRSProxy endpoint only accepts connections from an identity holding the Exchange-specific `ms-Exch-EPI-Token-Serialization` right, i.e. an Exchange server machine account; the write-up's own conclusion is *"The attacker sits inside the network, especially inside a domain-joined PC!"*, using a PetitPotam-style MS-EFSR coercion (`EfsRpcEncryptFileSrv`) to force one Exchange server to authenticate to an attacker-controlled path, then relaying that captured hash to a **different** Exchange server's MRSProxy — explicitly *"This one works only for multiple Exchange servers setup because the captured hash cannot be relayed to itself!"* The author's own risk assessment: *"It requires lot of non-realistic conditions to be exploited in the real world ... So, for the defensive guys, don't be panic!"* This is consistent with — and explains — MSRC's own `PR:L/UI:R` scoring that the entry's sourcing_note treats as the outlier to be overridden by the national CERTs' looser "unauthenticated" wording. None of this precondition (domain-network foothold, PetitPotam-class coercion capability, ≥2 Exchange servers in the environment) appears anywhere in the entry, which instead frames the risk as "any Exchange server ... exposed to unauthenticated, mailbox-wide access." This does not mean the entry's underlying facts (CERT-Bund/NCSC-NL do use "unauthenticated" language; the CVSS is 8.0; public exploit code exists) are wrong — but the entry's own weighing of that language against MSRC's vector, absent this technical context, produces a materially broader risk characterization than the mechanism supports. Suggested fix: read the MB VRED write-up (or an equivalent primary technical analysis of the published PoC) and either walk back `auth: pre-auth` to reflect the real precondition, or add a paragraph/Contradiction line explaining that "unauthenticated" in the CERT advisories means "no valid Exchange mailbox credential," not "no network position," and that exploitation needs a domain-joined foothold plus a multi-Exchange-server topology.

**#4 (low confidence).** `2026-09-01/valleyrat-winos4-qn-wallpaper-dll-sideload-defender-kill.md` — the cited Hacker News article states: *"When the logged-in user lacks administrator rights, the malware relaunches itself with `runas` to acquire them."* This privilege-escalation-relevant behavior is not reflected anywhere in the entry's body or `techniques[]`. Minor, but it's exactly the kind of concrete artifact (a `runas` re-launch prompt/event) a Tier 2 responder could hunt for.

**#5 (low confidence).** Same entry — Securelist states the backdoor has three process-protection techniques, of which two are configuration-gated (`bh` critical-process flag, `sh` svchost watchdog) and a third is unconditional: *"Restarting on an unhandled exception. This protection mechanism is always active, regardless of the backdoor's configuration."* The entry's runtime-protections paragraph enumerates only the two configurable ones plus window-enumeration (`ll`, also configurable) and states "each can be switched on or off independently" — true for the three it lists, but the omission of the always-on exception-handler restart means the entry's account of the backdoor's resilience techniques is incomplete.

### Missed angles

**#6.** `entities/registry.yaml` already carries `incident:silver-fox-arrests-china-2026` (first_seen 2026-06-18): *"China arrests 67 operators of the Silver Fox (Winos/ValleyRAT) cybercrime operation."* This is exactly the dedup-context signal check 13 asks verifiers to use, and it is directly relevant to the new `actor:silver-fox` / ValleyRAT entry, which reports Kaspersky's *"over 100,000 [ValleyRAT] detections ... across all of 2026"* — spanning both before and after the June arrests. The entry doesn't address whether this specific QN Wallpaper campaign reflects the same operators continuing after a partial law-enforcement disruption, a rebuilt cell, or an unrelated affiliate using the same malware family — a one-sentence note connecting the two would close a real analytical gap the registry itself already flags (the run record separately logs this as an unlinked registry orphan, but that's a bookkeeping note about the incident record, not about the new entry's own analysis missing the connection). Suggested search: "Silver Fox ValleyRAT arrests 2026 resume operations" / a follow-up on China's Silver Fox prosecution status.

### Quantifier without source

**#7 (low confidence).** `2026-09-01/anthropic-claude-session-hijack-infostealers.md` title: *"Anthropic **mass-revokes** sessions compromised via ..."* None of the three cited sources characterizes the scale as "mass." Dark Reading explicitly says *"Anthropic proactively signed an **unknown number** of users out of Claude."* BleepingComputer and Help Net Security both describe action taken against "affected users"/"some Claude users" with no scale claim at all. "Mass-revokes" implies a large/bulk-scale action; the actual scale is stated by the entry's own best source as unknown. The same "mass-revoked" phrasing was also carried into the new `entities/registry.yaml` record for `campaign:claude-session-hijack-infostealers-2026`, so the fix should be applied in both places if accepted.

### Whole-run checks

- **Liechtenstein/transparency-register backlog row** — independently re-searched this iteration (WebSearch + fetch of `exxpress.at`, a story not in the main agent's own search trail). Exxpress.at (Austrian outlet, 2026-08-31) carries the same facts as domain-b.com (VSV letter dated 24 August, Federal Council's 1 October go-ahead) and explicitly attributes the letter to *"dem Schreiben vom 24. August, das der Nachrichtenagentur Reuters vorlag"* ("the letter... which Reuters had seen") — meaning this is Reuters wire content propagating through multiple secondary sites (cryptobriefing.com, thenews.com.pk, globalbankingandfinance.com, world-today-news.com, brinztech.com, coindesk.cc, exxpress.at all carry near-identical phrasing), none of which is an independently-reported Swiss-domestic outlet, and no live reuters.com URL for the underlying wire item was found. This **confirms** rather than undermines the coverage_backlog.md row's own judgment: the story is real and widely echoed, but every fetchable copy traces to the same paywalled/inaccessible wire origin, with no independent Swiss-domestic corroboration. The decision not to compose a changelog record is sound. (Not a defect — recorded per the assignment's instruction to confirm this reasoning.)
- **check_run.py** re-run this iteration: 46 pass · 1 warn (`aggregator-only`, Anthropic entry, expected/documented) · 1 fail (`run-clock`, expected — re-stamped in Phase 6). Matches the confirmation given in the spawn message exactly.
- **Coverage shape**: no additional missing in-window item found beyond what the run record's own "Coverage gap" note already discloses (the four stories that fell through the back-to-back-window gap). No entry in this run looks like it should have been dropped for relevance; no entry looks like it should have been a changelog record on an existing entry that wasn't already handled that way (checked all three new entries and all four CVE/entity keys against `prior_coverage.json` and `state/cves_seen.json` — no overlap found beyond the JFrog CVE-2026-66384 cross-reference already correctly declared in `references[]`).
- **Style discipline**: no IOCs, no vanity metrics, no workflow-internal language found in any of the seven entries or the run-record notes.
- **Self-identification**: per the harness-injected system-prompt line quoted verbatim above.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 4, advisory: 0)

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: new-entries
  item: "CVE-2026-82329 — JFrog Artifactory default-config admin bypass"
  url_or_quote: "its \"Versions\" column displays the 7.111 and 7.146 branch ranges inconsistently with itself"
  summary: "JFrog's live advisory table (docs.jfrog.com/releases/docs/jfrog-security-advisories) shows only the 7.111 row as inconsistent (7.111.4 > 7.111.21, fix 7.111.21); the 7.146 row (7.146.0 > 7.146.36, fix 7.146.38) is internally consistent. Naming 7.146 as also inconsistent is unsupported — residual phrasing from an earlier, different 7.146 fix."
- code: F3
  category: claim-not-supported
  section: updated-entries
  item: "2026-08-23/payload-zurich-it-provider-hwz-student-data.md"
  url_or_quote: "the ransomware group behind the provider-side intrusion has published data from the breach"
  summary: "(low confidence) Inside IT's own meta description hedges the ransomware-gang attribution with 'offenbar' (apparently); the entry states it as settled fact. Body is paywalled beyond two paragraphs so this rests on the page's own title/meta text."
- code: F8
  category: needs-more-research
  section: updated-entries
  item: "CVE-2026-62911 — Microsoft Exchange Server MRSProxy"
  url_or_quote: "any Exchange server below the August 2026 build should be treated as exposed to unauthenticated, mailbox-wide access once an attacker can coerce or capture a Negotiate authentication exchange"
  summary: "A detailed third-party technical analysis (MB VRED, vred.mbbank.com.vn, linked from a comment on the entry's own cited Franky's Web source) shows exploitation requires a domain-joined internal foothold, PetitPotam-style MS-EFSR coercion, and a minimum of two Exchange servers (captured machine-account hash must relay to a DIFFERENT server) — consistent with MSRC's own PR:L/UI:R vector that this run's changelog record overrode based on CERT-Bund/NCSC-NL's looser 'unauthenticated' wording. The entry's pre-auth/broad-exposure framing does not reflect this precondition."
- code: F8
  category: needs-more-research
  section: new-entries
  item: "ValleyRAT (Winos 4.0) via re-signed QN Wallpaper"
  url_or_quote: "the malware relaunches itself with runas to acquire them"
  summary: "(low confidence) The Hacker News (cited corroborating source) documents a runas UAC-elevation relaunch behavior not reflected in the entry's body or techniques[]."
- code: F8
  category: needs-more-research
  section: new-entries
  item: "ValleyRAT (Winos 4.0) via re-signed QN Wallpaper"
  url_or_quote: "Restarting on an unhandled exception. This protection mechanism is always active, regardless of the backdoor's configuration."
  summary: "(low confidence) Securelist documents a third, always-on process-resilience technique alongside the two configuration-gated ones the entry describes; omitted from the entry's runtime-protections account."
- code: F10
  category: missed-angle
  section: new-entries
  item: "ValleyRAT (Winos 4.0) / actor:silver-fox"
  url_or_quote: "China arrests 67 operators of the Silver Fox (Winos/ValleyRAT) cybercrime operation. (entities/registry.yaml, incident:silver-fox-arrests-china-2026, first_seen 2026-06-18)"
  summary: "The entry doesn't connect Kaspersky's 2026-wide 100,000+ ValleyRAT detection count to the existing registry record of China's June 2026 arrest of 67 Silver Fox operators — a directly relevant dedup-context fact about the same actor/malware family. Suggested search: 'Silver Fox ValleyRAT arrests 2026 resume operations'."
- code: F14
  category: quantifier-without-source
  section: new-entries
  item: "Anthropic Claude session-hijacking via commodity infostealers"
  url_or_quote: "Anthropic mass-revokes sessions compromised via Vidar, LummaC2, StealC, RedLine, Acreed and AMOS"
  summary: "(low confidence) No cited source characterizes the scale as 'mass'; Dark Reading explicitly says Anthropic signed out 'an unknown number' of users. Same phrasing was also carried into the new campaign:claude-session-hijack-infostealers-2026 registry record."
```
