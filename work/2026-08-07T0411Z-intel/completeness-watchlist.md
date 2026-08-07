# Phase 2 completeness sweep — items handed off or dropped by sub-agents
(built as returns arrive; every line resolved before composition)

## From S1 (returned 04:28:45Z, 1 item)
- [ ] Sonatype "Flooding Dropper" npm campaign, 846+ malicious packages — S1 says out of its CVE/advisory scope, explicitly left for S3/S4. CHECK S3/S4 returns; if neither carries it, decide directly.
- [ ] WordPress 7.0.3 / CVE-2026-64638 (pre-auth XSS -> potential RCE, 11 fixes) — S1 dropped: needs victim click, no ITW exploitation, forced auto-update release. Re-examine against the WP2Shell precedent.
- [ ] Cisco Catalyst SD-WAN hardening release CVE-2026-20303/-20304/-20310/-20312/-20313 — dropped: internally found, auth-required, no exploitation. Likely correct.
- [ ] CERT-FR Cisco multi-product bundle (CIMC arg-injection etc.) — dropped, same profile. Likely correct.
- [ ] Oracle off-cycle PeopleSoft alert CVE-2026-35273 — dropped as stale (page metadata dates to June). Verify the date claim if it resurfaces.
- [ ] KEV additions: S1 reports NO in-window KEV addition. Spot-check `cisa-kev` directly in Phase 2 (allowed once all Phase 1 agents have returned) — a missed KEV addition is the single highest-cost false negative this pipeline has.

## From S3 (returned 04:29:14Z, 4 items)
Items returned: UNC6671/BlackFile rebrand (GTIG); macOS ClickFix server-side fingerprinting gate (Microsoft TI); fake-Zoom .NET downloader -> Overlord RAT (Jamf); AI Token Jacking (Unit 42).
- [x] Sonatype "Flooding Dropper" npm campaign — S3 did NOT pick it up. STILL OPEN: check S4, else decide directly.
- [ ] S3 dropped: Zimperium "Flying Eagle" Android RAT (rehash of a 2026-07-28 hunt.io primary, no in-window delta) — defensible.
- [ ] S3 dropped: two CrowdStrike AI-agent posts (architecture/benchmark, no attacker behaviour) — defensible.
- [ ] S3 dropped: Recorded Future "Emerging Threats to Neurotechnology" (strategic framing, not tradecraft) — defensible; also strategic horizon belongs to the weekly.
- [ ] S3 dropped: Unit 42 + Microsoft ChainDrop write-ups — corroborating sources on the already-published 2026-08-06 CHAINDROP entry, no material delta. Defensible.

### Dedup resolutions already made
- actor:unc6671 prior entries are 2026-05-16, 2026-05-25 and 2026-07-10 — ALL outside the 14-day window, so the GTIG post is a NEW entry, not an update_of. Use `references[]` to orient. PD-10 background paragraph not triggered (prior reporting ~2.5 months, not >6).
- campaign:clickfix-macos-2026 has no in-window entry -> new entry, not an update.
- hunt-io is ALREADY a tracked source (status=candidate, lsf 2026-07-30). S3's candidate proposal is a DUPLICATE — do not add it. Record that S3 pivoted to hunt.io content this run (counts toward its promotion evidence).

## From S2 (returned 04:33:06Z, 2 items)
Items returned: Keycloak 7 CVEs via CERT-FR CERTFR-2026-AVI-0976 (all 7 CVE ids NEW to the store); BIT/FOITT SharePoint CVE narrowing (borderline).
- [ ] **Meta AI sandbox-escape story** — S2 surfaced it via Swiss trade press and pushed it to S3 as out-of-S2-scope; S3 did NOT return it. OPEN cross-domain gap. The store already runs a thread on AI evaluation-containment failures (Hugging Face 07-30/07-31, Anthropic 07-31, UK AISI 08-05) — a fourth vendor would be a genuine delta. RESOLVE before composing.
- [x] BIT/FOITT SharePoint CVE narrowing -> **borderline-drop**. Both named CVEs (CVE-2026-56164, CVE-2026-50522) are ALREADY in state/cves_seen.json from the W30 on-prem SharePoint wave; the narrowing is explicitly hedged press inference ("It remains unclear whether either vulnerability was used"), and the existing 2026-08-05 entry already directs exposed-SharePoint operators to a compromise assessment plus machine-key rotation. No change to what the reader does in the next 7 days.
- [ ] S2 found NO third Swiss/EU SharePoint victim and NO European water/OT development despite targeted searches — both were explicit spawn tasks. Negative results, recorded as such.
- [ ] prodaft: 3rd consecutive non-contribution, root-caused as a STALE JINA CACHE (HTTP 200 throughout, page metadata frozen at "Wed, 08 Jul 2026", Next.js SPA so the reader is the only route). Not a transport failure, not a demotion. -> sources_changed[] note.
- [ ] ENISA CVE-programme announcement (NCIA + AISLE join as CNAs under the ENISA Root, 2026-08-06) — dropped as policy/administrative with no SOC action. Defensible; policy horizon also belongs to the weekly.
- [ ] dcod-ch items (FINMA post-quantum survey; Zurich Yutong bus remote-disable) — dropped as late rehashes of stale events (2026-07-09 circular; Nov 2025 Norway/Denmark disclosure). Defensible.
- [ ] netzwoche Liechtenstein follow-up (2026-08-06, names 2 of the 4 already-reported offline systems) — dropped as too thin a delta over the 08-04/08-05 entries. Defensible.

### Dedup resolutions
- Keycloak prior entries are 2026-05-21, 2026-06-07, 2026-06-28, 2026-06-29 — all outside the 14-day window, and all 7 new CVE ids are absent from state/cves_seen.json -> NEW entry, not update_of. This is the "stream of independent disclosures from one project" case, not one story recurring.
