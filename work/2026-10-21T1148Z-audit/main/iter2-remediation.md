# Iteration 2 remediation log (main agent)

Ref = i2#n in verification.iter2.findings.yaml. A = applied, D = declined (reason). No further verifier spawn: the wave's budget of 20 is spent.

- i2#1 A: Ivanti record summary replaced with the Ivanti correction text (the TrickMo text had been pasted in by the s1#42 fix).
- i2#2 A: Calypso, "at least mid-2022" cited to Lumen.
- i2#3 A: BWH, "passport" dropped from the body and the record summary (The Register says no payment or bank details).
- i2#4 A: AMD, the frontmatter summary and record summary no longer bind the Windows mitigation to EPYC 7002; Microsoft says the latest Windows builds enable a mitigation for the affected AMD models without naming them (MSRC description re-read through its API).
- i2#5 A: ChromaDB, Hadrian repeats HiddenLayer's name "ChromaToast".
- i2#6 A: Drupal, the Symfony and Twig updates follow SA-CORE-2026-004 (highly recommended whether or not the SQL injection applies, exposure depends on configuration and contributed modules).
- i2#7 A: run record and report recounted: 398 mappings over 170 distinct ids (after i2#9), 23 CVEs added, 40 product entities, 40 summaries, 36 priority moves (after i2#12), three primary URLs.
- i2#8 A: the report's per-entry table regenerated from the final record summaries.
- i2#9 A: GemStuffer, T1567.004 removed (no source mentions a webhook); T1567 stays.
- i2#10 A: ICO, cisa-kev dropped from CVE-2020-1472's status (no KEV source cited in the entry).
- i2#11 A: F5 CVE-2026-41225, verification single-source (F5 is the only assessor).
- i2#12 A: Groupe 3R, high to notable (its takeaway says no patching or detection decision changes).
- i2#13 A: ChromaDB record summary ends on the sourced roles, no narration.
- i2#14 A: Verizon record summary ends on the methodology change, no narration of the source swap or priority.
- i2#15 A: Ivanti sourcing_note, the fetch-failure sentence dropped.
- i2#16 A (pre-existing): GTIG takeaway, AWS keys and GitHub tokens are treated as stolen and the AI API secrets are those GTIG says the LiteLLM compromise could expose.
- Sweep after i2#13/14: three more record summaries narrated pipeline internals and were tightened (West Pharmaceutical "only encryption is mapped", Nextcloud "rather than a high-priority item", Webworm "the ATT&CK mapping follows ESET's own table").
