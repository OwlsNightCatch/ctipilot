# Run 2026-11-07T0256Z-intel — resume notes (main agent)

Started 2026-11-07T02:56:04Z · gap 24.0 h · window 26 h · prompt v4.24 · main model Sonnet 5.5 (claude-sonnet-5-5).
Branch: claude/nifty-gauss-87c6tw (feature branch only; commit atomically in Phase 6; Stop-hook nudges do not override).

## Done
- Phase 0 (prior_coverage 89 records read; registry NOT read whole: 714 KB, grep by key instead; KEV sweep: 1 row CVE-2026-19868 -> N1)
- Phase 1: S1 S2 S3 S4 returned (findings.S*.yaml, ledgers complete 26/19/14/10). Digests: s1-digest.txt, s3-digest.txt; S2/S4 in findings files.
- Phase 2 triage -> triage.json (7 new N1-N7, 6 updates U1-U6, borderline drops listed there, backlog dispositions).
- Phase 4 deep reads delegated: DR1 (N1,N2,U2,U3), DR2 (U4,U5,U6,U1), DR3 (N3,N4,N5,N6,N7) -> deepread.DR{1,2,3}.yaml + bodies/*.md (claims verified grep -F by the agents; re-check quotes before use).

## Decisions
- No deep dive, no critical today. N1 SonicWall = high; N2 Brotli vendor wave notable (references both Brotli base entry and .NET OOB entry); N3 BOSSAI, N4 Kaspersky GERT, N5 Oneconsult notable; N6 Aargau policy routine; N7 TUM incident routine.
- Updates (type update): U1 Danfoss refrigeration (NCSC checklist + Ransom-ISAC XWEB Pro log + Unit 42 exposure), U2 OpenSSH sshole exploitation (Previdian honeypot), U3 WordPress update-window, U4 Cisco ESG Metasploit module for sibling flaw, U5 IoT2050 scope widened (Basic/M.2/SM), U6 ARTEX Storm-3358/Check Point.
- Backlog: ARX row -> struck (unconfirmed at expiry 2026-11-07). ChimeraZ row: Ebikon/Gersau/Meggen/Wil struck as non-incident; Solnet+davos.ch struck below incident floor; ZOHE held until 2026-11-17.
- Source edits to apply in Phase 5 (sources_changed[]): crowdstrike rss_url https://www.crowdstrike.com/en-us/blog/feed/; rapid7-research recipe (feed malformed: url blog + extract); msft-ti raw url shows time datetime; blick-ch feed https://www.blick.ch/news.xml; zimbra feed https://blog.zimbra.com/feed/; synology-security-advisories feed 404 -> bridge recipe url --direct https://www.synology.com/en-us/security/advisory then extract SA page; sonicwall-psirt rss https://psirtapi.global.sonicwall.com/api/v1/feed/rss.xml + vulndetail JSON; qnap newsroom notices under qnap.com/en/security-news; previdian per-CVE pages via extract; ox-security direct feed https://www.ox.security/feed/; inside-it.ch body via url --direct; esentire extract returns boilerplate (WebFetch works); piyolog candidate->active (3 productive sweeps) only if promotion_due agrees (digest lists oss-security promotion_due instead — apply that one). Candidate new sources: layer3intel.com/blog, aargauerpolitik.ch, picus-security-blog. jina pool dead (HTTP 402 on every key) — note in run record.
- Run-record body must carry: borderline-drop lines (from triage.json), backlog dispositions, KEV disposition, essential-coverage (all attempted), coverage gaps (connectwise-trust-center 403, sygnia 403, ico-uk 403, prodaft no dated listing, ag.ch 404, cert.at html 403, apple-security maybe cached).

## Next
1. Wait DR1-3 -> check bodies + quote verification -> read each target entry fully, apply ONE record each (tools/entry_record.py add), write 7 new entries (Read prompts/entry-template.md already done).
2. Phase 5: registry (actor:storm-3358, actor:blacknevas, campaign/incident keys), cves_seen, sources.json, sync_products.py, source_health.py, run record.
3. Phase 5.5 check_run --pre-verify; claim_ledger; Phase 5.7 verifier x>=2; Phase 6 commit/push (re-stamp main.ended_at); Phase 7 poll + publish-status amendment.

## Status update (04:15Z)
- DONE: 7 new entries (entries/2026-11-07/*; Kaspersky slug is now kaspersky-esxi-proxmox-ransomware-monitoring-root-password), 6 changelog records (U1-U6), registry (+5 entities, +11 products via sync_products), cves_seen, sources.json (bookkeeping, recipe fixes, 2 candidates, oss-security promoted, shadowserver/ec-presscorner fixed), backlog (ARX struck, ChimeraZ noted), source_health re-run (0 UNSOLVED), run record written (runs/2026-11-07/2026-11-07T0256Z-intel.md; provisional completed/duration; publish_status pending; verification block to be filled).
- Gate: `check_run.py <id> --pre-verify` = 0 fail, only the 3 expected verification warnings.
- NEXT: Phase 5.7 verifier loop (cti-verification, fresh each iteration; claim ledger: tools/claim_ledger.py <id> --iteration N / --coverage N; double CLEAN needed). Then fill run record verification block (counters), re-run gate WITHOUT --pre-verify, Phase 6 re-stamp main.ended_at + completed/duration, commit (stage specifics; NOT git add -A; include .claude/memory only if touched), sync main, push branch, Phase 7 poll + publish-status amendment.
- Run-record YAML must be dumped with the indented-sequence Dumper and width=100000 (custom parser rejects wrapped scalars / unindented lists).
