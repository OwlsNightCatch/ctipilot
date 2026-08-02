# Running findings ledger — 2026-08-02T1309Z-audit

## Truth passes

### B2 — W30 weekly strategic (11 entries) — RETURNED
8 clean / 11 · 1 factual-error · 2 imprecision · 0 machine-surface.

**FE-1 (candidate `update_of` correction).** `weekly-w30-ai-autonomous-operator-and-target`
frames the Searchlight Cyber GPT-5.6 experiment as the model "rediscovering and weaponising the
already-patched" WordPress WP2Shell pre-auth chain. The cited source's own title is
*"Exploit brokers pay $500,000 for a WordPress RCE — I found one with GPT-5.6"*, and per the
verifier the post describes an **original discovery of an unpatched flaw**, with Searchlight
withholding publication to let defenders upgrade.

Store-internal corroboration that the framing is wrong: the 2026-07-18 entry
`wordpress-core-wp2shell-preauth-rce-chain-cve-2026-63030` calls Searchlight Cyber the
**"Discoverer"** of CVE-2026-63030 / CVE-2026-60137. So the AI's find is what produced the
07-17 out-of-band patch — not a rebuild of someone else's patched bug.

Origin is **not** the weekly: the error entered at `2026-07-21/gpt56-autonomous-wordpress-wp2shell-exploit-chain`
(title, headline, summary and body all say "rediscovers … the already-patched … chain"), and the
weekly inherited the framing. This inverts the capability claim in the direction that matters —
"AI rebuilt a known exploit" is routine, "AI autonomously discovered a novel pre-auth RCE in
WordPress core" is the qualitatively new capability the entry set out to assess.
→ **needs a main-agent primary re-fetch before anything ships** (deferred: Phase 1/2 sweeps still running).

**IMP-1.** `weekly-w30-joomla-extension-wave-status` — three vulnerability claims
(EasyStore unauthenticated SQLi + order-forgery, Events Booking invoice IDOR) carry no inline
citation and neither product appears in `sources[]`; `affected_products[]` lists only Balbooa
Gridbox though the body discusses four products. Facts are real (mySites.guru published both
disclosures) — the citation link is missing. *Missing-citation / attribution class.*

**IMP-2.** `weekly-w30-looking-ahead` — "complete the F5 out-of-band patch" is cited to
cyberstan.co.uk, which calls the fix "scheduled for the F5 Security Advisory on 15 July 2026"
and never says out-of-band. Underlying fact true, carried by an uncited source.
*Per-fact attribution / adjacency class — the exact defect v3.29 mechanised against.*

### B1 — 20 entries — running
### B3 — 20 entries — running
### B4 — 20 entries — running

## Coverage re-sweeps
### G1 vulnerabilities — running
### G2 incidents + watch items — running
### G3 research-blog listing sweeps — running

## Systemic (main context) — see systemic-notes.md
1. Backup weekly burned 2.3 h and 8 verifier iterations before the Phase 6 sync revealed the
   primary had already published W30 — the duplicate-week guard runs at Phase 0 only.
2. The verifier's editorial discipline checks are dormant: 1 F16 (mis-coded) and 1 F18 across
   ~40 July/August fires, while `high` share went 22.4 % → 41.0 % and actions/entry 0.48 → 0.87.
3. Five clusters from the previous audit's watch item were never registered — **fixed this fire**.
4. `state/source_health.json` carries three stale `needs-demote` orders from a snapshot taken
   during the reader-pool outage — re-probe once the sweeps return.
5. Two open `verification-confirmation` WARNs on immutable records.
