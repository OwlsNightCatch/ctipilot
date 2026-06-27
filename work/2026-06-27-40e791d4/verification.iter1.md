**Model:** Anthropic Claude Opus 4.8 (1M context) (`claude-opus-4-8[1m]`)
**Timestamps:** started_at=2026-06-27T04:41:06Z · ended_at=2026-06-27T04:46:41Z · duration_seconds=335
**Self-telemetry:** webfetch_calls=14 websearch_calls=0 bridge_fetches=3 urls_checked=18

## Verification report — briefs/2026-06-27.md (iteration 1)

Cold read. Every Source and Additional-source URL across §§ 0–7 was fetched this run
(WebFetch + bridge for NCSC-CH). Two known-403 hosts could not be content-verified:
inside-it.ch (403 via WebFetch and bridge) and the ENISA EUVD / NCSC-CH SPAs (JS-rendered;
NCSC-CH post 12579 verified via the bridge JSON endpoint). All are corroborating
Additional sources, not sole primaries.

### Citation does not support the claim

**F3 — Amazon Q (§ 3): wrong fixed-version number; readers told to confirm the wrong build.**
The brief states: "Affected: Language Server for AWS < 1.65.0; fixed in 1.69.0 (discovered
2026-04-17, patched 2026-05-12, public 2026-06-26)." The § 3 "Why it matters" repeats:
"confirm the language server is ≥ 1.69.0."
I fetched both cited sources this run:
 - Wiz Research (https://www.wiz.io/blog/amazon-q-vulnerability): "Fixed Version: language
   server 1.65.0"; the page does not mention 1.69.0.
 - The Register (https://www.theregister.com/cyber-crime/2026/06/26/amazon-q-flaw-let-booby-trapped-git-repos-execute-code-swipe-cloud-creds/5263202):
   "We have remediated this issue in language server version 1.65.0" — fixed in 1.65.0, not 1.69.0.
The brief's "< 1.65.0 affected, fixed in 1.69.0" is also internally inconsistent (if affected
is < 1.65.0 then 1.65.0 is the fix). Operational impact: a defender who upgrades only to a
build between 1.65.0 and 1.69.0 is told (wrongly) they are still exposed; conversely the
remediation target should be 1.65.0. Fix the prose and the action item to "fixed in 1.65.0;
confirm ≥ 1.65.0."

### Unsupported / hallucinated facts

**F4 — SANS ISC item (§ 3): "auditd rules on prctl" not in the cited diary.**
The brief states: "The diary recommends `auditd` rules on `prctl` with the `PR_SET_NAME`
argument, and eBPF tooling (Kunai/Falco) ..." I fetched the only cited source
(https://isc.sans.edu/diary/33102). The diary documents the comm/cmdline divergence, the
PR_SET_NAME technique, Kunai (eBPF) detection, and Operation Highland / Velvet Ant (Sygnia);
it does NOT recommend or mention auditd rules on prctl. The eBPF/Kunai half is supported; the
auditd half is not. Either drop the auditd clause or attach a source that recommends it.

**F4 — "The Gentlemen" UPDATE (§ 4, TL;DR, § 6): The Hacker News article cited as 2026-06-26
is actually dated Jun 11, 2026, and carries no in-window delta.**
The brief cites https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html
as "[The Hacker News, 2026-06-26]" in the TL;DR, the § 4 UPDATE, and the § 6 Action-Items
footer. I fetched it twice this run; the byline is "Jun 11, 2026" and the most recent event
it reports is late April 2026 (Rocket.Chat leak) — there is NO 24–26 June development in it.
The 478-victim count and the `--spread` worm capability are both from this June-11 article,
so the UPDATE's framed "in-window delta" ("now claims 478 victims and ships a `--spread`
argument") is two-plus weeks stale, not a fresh 36 h development. The only genuinely
in-window element is the Swiss-targeting claim, whose sole source (inside-it.ch, dated
20260626 in the slug) I could not fetch (403 via WebFetch and via the bridge). Two problems
to fix: (a) correct the THN citation date to 2026-06-11 everywhere it appears; (b) re-justify
the UPDATE's in-window hook — if the only fresh element is the inside-it.ch Swiss-press piece,
the delta is the Swiss-second-most-targeted finding (Check Point Research via inside-it.ch),
not the 478/`--spread` content, and § 7 should record that inside-it.ch could not be
re-fetched this run.

### Analytical-link-as-fact

**F13 — Miasma UPDATE (§ 4): "RevokeAndItGoesKaboom ... ties this wave to the earlier
codfish/semantic-release-action compromise" is asserted as fact but not in either cited source.**
The brief states: "The recurring `RevokeAndItGoesKaboom` dead-drop marker ties this wave to
the earlier `codfish/semantic-release-action` compromise." I fetched both cited sources:
 - Socket (https://socket.dev/blog/miasma-mini-shai-hulud-hits-leoplatform-npm-packages-go-ecosystem):
   mentions the RevokeAndItGoesKaboom marker but makes no codfish/semantic-release-action link.
 - JFrog (https://research.jfrog.com/post/shai-hulud-miasma-alright-lets-see-if-this-works/):
   mentions the marker but "does not connect it to any codfish/semantic-release-action compromise."
Neither cited source asserts the connection the brief states as fact. Either attach a source
that makes the link or soften to "the marker recurs from earlier waves" without the specific
codfish attribution. (Medium confidence — the marker/wave-continuity claim itself is supported;
only the specific codfish tie is unsourced.)

### Surface contradiction

**F9 — STOCKSTAY deep dive (§ 5) publication date: the GTIG primary is dated 2026-06-25, but
the brief uses 2026-06-26 and § 7 inverts which source said what.**
The brief's § 5 says GTIG "published a full technical analysis of STOCKSTAY on 2026-06-26".
The cited primary (https://cloud.google.com/blog/topics/threat-intelligence/stockstay-turla-intelligence-gathering)
is dated June 25, 2026 in its byline. § 7 currently records: "minor publication-date
discrepancy ... one feed cited 2026-06-25, corroborating sources 2026-06-26; the brief uses
2026-06-26." That has the polarity backwards — the GTIG *primary* is 06-25; THN/The Record are
the 06-26 restatements. Low-severity, but the resolution picked the date that disagrees with
the primary. Suggest aligning § 5 to the primary (06-25) or correcting the § 7 note to state
the primary is 06-25.

### Editorial / less-is-more flags (advisory)

**F11 — STOCKTRADER command count (§ 5).** Brief says STOCKTRADER supports "15+ commands";
the GTIG primary enumerates 13 named commands ("13+"). Minor overstatement vs. the primary;
THN may carry 15+ but I did not see it. Consider "13+ commands" to match the primary, or
confirm 15+ against the THN restatement.

**F11 — minor primary-date drift on Miasma (§ 4) and StrikeShark (§ 3) and Canvas lure
languages (§ 1).** Miasma cited 2026-06-26; both Socket and JFrog primaries are 06-25 (wave
itself 06-24). StrikeShark cited 2026-06-26; Securelist primary byline is 24 Jun 2026. Photo-ZIP
lists "Czech" among lure languages; the Microsoft primary mentions Czech in user-account naming,
not explicitly as a lure language. All three are cosmetic and none change the operational claim;
advisory only.

### Confirmations (no action — recorded for the operator)

- Name-collision WARNs both clear: "ShinyHunters" (§ 1) is the attacker in the Computer Weekly
  primary (no defender/tool inversion); "Operation Highland" (§ 3 SANS) is correctly cited as a
  Velvet Ant campaign per the Sygnia reference in the diary. No attacker/defender inversion in
  either.
- Cellebrite (§ 3) in-window hook confirmed as the Citizen Lab *publication* (2026-06-25), event
  is 17 June 2021 — framing is correct.
- DirtyClone (§ 0/§ 2): JFrog states the attack needs CAP_NET_ADMIN; the brief's "reachable by
  any unprivileged user where user namespaces are enabled" is consistent (CAP_NET_ADMIN is
  obtainable in a user namespace) — not a defect.
- pedit COW (§ 2): the Red Hat RHSB primary does not carry tcf_pedit_act()/packet_edit_meme/
  v5.18/v7.1-rc7/"pedit COW", but the cited THN additional source does — claims are sourced.
- Windchill (§ 0/§ 4), SD-WAN chain (§ 4 — verified incl. NCSC-CH post 12579 lastModified
  2026-06-25 / Mandiant report added), Klue (§ 0/§ 4), STOCKSTAY architecture/attribution
  (HIGH confidence, Turla), Signal PSA (§ 0/§ 1), Photo-ZIP/TonRAT (§ 1), StrikeShark (§ 3):
  all named entities (CVEs, actors, versions, dates) trace to a fetched source. No IOCs leaked
  into prose; brief correctly omitted the IPs/hashes present in the THN Windchill source.
- Could not content-verify (403/SPA, all Additional sources only): inside-it.ch (§ 4 Gentlemen),
  ENISA EUVD-2026-37831 (§ 4 Windchill), NCSC-CH SPA front-end (verified via bridge JSON instead).

### Verdict

NEEDS_FIXES (truth: 4, editorial: 1, advisory: 2)

Truth = F3 (claim-not-supported, Amazon Q version), F4-a (auditd unsupported), F4-b (Gentlemen
THN date / stale delta), F13 (codfish analytical link). Editorial = F9 (STOCKSTAY date /
§ 7 inverted). Advisory = the two F11 records. The F3 and F4-b defects are the operationally
material ones (wrong remediation version; an UPDATE whose in-window justification rests on a
two-week-old article).

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: research
  item: "CVE-2026-12957 — Amazon Q Developer MCP auto-load (Wiz)"
  url_or_quote: "fixed in 1.69.0 ... confirm the language server is >= 1.69.0"
  summary: "Wiz and The Register both state fixed in 1.65.0, not 1.69.0; affected <1.65.0 means 1.65.0 is the fix. Wrong remediation version in prose and action item."
- code: F4
  category: hallucinated-fact
  section: research
  item: "SANS ISC prctl(PR_SET_NAME) masquerading [SINGLE-SOURCE]"
  url_or_quote: "The diary recommends auditd rules on prctl with the PR_SET_NAME argument"
  summary: "Cited SANS diary (isc.sans.edu/diary/33102) does not mention auditd rules; it covers comm/cmdline divergence, Kunai/eBPF, Operation Highland only. Drop the auditd clause or source it."
- code: F4
  category: hallucinated-fact
  section: updates
  item: "UPDATE: The Gentlemen ransomware 478 victims / --spread"
  url_or_quote: "[The Hacker News, 2026-06-26](https://thehackernews.com/2026/06/the-gentlemen-ransomware-claims-478.html)"
  summary: "THN article byline is Jun 11, 2026, not 2026-06-26; most recent event is late April 2026. 478/--spread content is stale, not an in-window delta. Correct the date everywhere (TL;DR, S4, S6) and re-base the UPDATE's in-window hook on the inside-it.ch Swiss-targeting finding (which could not be re-fetched this run, 403)."
- code: F13
  category: analytical-link-as-fact
  section: updates
  item: "UPDATE: Miasma / Mini Shai-Hulud npm worm new wave"
  url_or_quote: "The recurring RevokeAndItGoesKaboom dead-drop marker ties this wave to the earlier codfish/semantic-release-action compromise"
  summary: "Neither cited source (Socket, JFrog) connects the RevokeAndItGoesKaboom marker to codfish/semantic-release-action. Marker recurrence is supported; the specific codfish tie is not. Source it or soften."
- code: F9
  category: surface-contradiction
  section: deep-dive
  item: "Deep Dive — Turla STOCKSTAY"
  url_or_quote: "published a full technical analysis of STOCKSTAY on 2026-06-26"
  summary: "GTIG primary byline is June 25, 2026; brief uses 06-26 and S7 note inverts which source carried which date (claims primary=06-26, feed=06-25). Align S5 to 06-25 or fix the S7 note."
- code: F11
  category: editorial-advisory
  section: deep-dive
  item: "STOCKSTAY STOCKTRADER command count"
  url_or_quote: "supporting 15+ commands"
  summary: "GTIG primary enumerates 13 named commands (13+). Minor overstatement; consider 13+ or confirm 15+ in THN."
- code: F11
  category: editorial-advisory
  section: multiple
  item: "Cosmetic primary-date drift (Miasma, StrikeShark) + Photo-ZIP Czech lure"
  url_or_quote: "StrikeShark 2026-06-26 (Securelist=24 Jun); Miasma 2026-06-26 (primaries=06-25); Czech listed as lure language"
  summary: "Cosmetic date/attribution drift vs primaries; no operational claim changes. Advisory only."
```
