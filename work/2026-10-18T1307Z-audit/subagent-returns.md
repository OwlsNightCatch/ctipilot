# Sub-agent returns (compact lines, verbatim)

## T6a
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:13Z · ended_at=2026-10-18T13:49:26Z · duration_seconds=1333 (ended_at read from `date`; the file write was refused, main agent wrote it from the return)
**Entries:** 9 checked · clean 1 · imprecision 6 · factual-error 2
**Claims:** in_scope=445 checked=280 (entries 1–5 row by row; entries 6–9 at passage level against every cited source; the session's auto-mode safety check refused the sub-agent's Bash writes from entry 6 on, so rows and the report file for 6–9 were never written; main agent transcribed 6–9 from the return into truth-T6a.yaml)
**Self-telemetry:** webfetch_calls=14 websearch_calls=2 bridge_fetches=21 urls_checked=70

## T4
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:26:57Z · ended_at=2026-10-18T13:50:03Z · duration_seconds=1386
**Entries:** 14 checked · clean 4 · imprecision 8 · factual-error 2
**Claims:** in_scope=375 checked=375
**Self-telemetry:** webfetch_calls=0 websearch_calls=8 bridge_fetches=126 urls_checked=118
Note: out-of-scope registry defects — incident:eurail-breach-2026 summary keeps the retracted DPA/EDPS review; incident:daemon-tools-supply-chain-2026 says "EU governments targeted", which Kaspersky does not say.

## T7
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:24Z · ended_at=2026-10-18T13:50:43Z · duration_seconds=1399
**Entries:** 14 checked · clean 3 · imprecision 8 · factual-error 3
**Claims:** in_scope=350 checked=350
**Self-telemetry:** webfetch_calls=3 websearch_calls=0 bridge_fetches=~60 urls_checked=~85
Note: Gyazo/Helpfeel notice updated since (suspension 2026-09-24, resumption 2026-09-27), not an entry defect.

## T8b
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:40Z · ended_at=2026-10-18T13:52:56Z · duration_seconds=1516
**Entries:** 10 checked · clean 2 · imprecision 6 · factual-error 2
**Claims:** in_scope=334 checked=334
**Self-telemetry:** webfetch_calls=0 websearch_calls=2 bridge_fetches=40 urls_checked=62
Group: ShinyHunters PeopleSoft campaign / NAIC / FBI claim — same_finding false; NAIC unlinked (link to complete the set).

## T8a
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:32Z · ended_at=2026-10-18T13:53:30Z · duration_seconds=1558
**Entries:** 11 checked · clean 2 · imprecision 7 · factual-error 2
**Claims:** in_scope=363 checked=363
**Self-telemetry:** webfetch_calls=1 websearch_calls=3 bridge_fetches=38 urls_checked=65
Lead (kernel ChangeLogs): fixed versions supported by the kernel CNA records; ChangeLogs carry the fix commit titles but no CVE ids → citation imprecision.
Outside batch: registry BeaverTail described as "an initial loader"; waterplum Correction says it is not a loader.

## T2
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:26:42Z · ended_at=2026-10-18T13:53:41Z · duration_seconds=1619
**Entries:** 18 checked · clean 10 · imprecision 5 · factual-error 3
**Claims:** in_scope=382 checked=382
**Self-telemetry:** webfetch_calls=1 websearch_calls=4 bridge_fetches=75 urls_checked=95 (estimates); one jina call (BLVK PDF)

## G3a
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:28:58Z · ended_at=2026-10-18T13:55:02Z · duration_seconds=1564
**Self-telemetry:** webfetch_calls=0 · websearch_calls=4 · bridge_fetches=135
**Findings:** 21 items (6 non-borderline incl. 1 update_target; 15 borderline; 20 covered posts listed)
**Source ledger:** 29 of 29 attempted
**Candidate sources:** 2 (barracuda-research, island-security-research)
**Coverage gaps:** 9 recipe notes (no real fetch failures)

## T6b
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:19Z · ended_at=2026-10-18T13:55:42Z · duration_seconds=1703
**Entries:** 8 checked · clean 1 · imprecision 6 · factual-error 1
**Claims:** in_scope=302 checked=302
**Self-telemetry:** webfetch_calls=1 websearch_calls=4 bridge_fetches=85 urls_checked=75

## T5
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:07Z · ended_at=2026-10-18T13:55:28Z · duration_seconds=1701
**Entries:** 13 checked · clean 5 · imprecision 8 · factual-error 0
**Claims:** in_scope=375 checked=375
**Self-telemetry:** webfetch_calls=7 websearch_calls=2 bridge_fetches=80 urls_checked=74
Group: CVE-2026-0257 pair = one finding; survivor 2026-05-30/cve-2026-0257-palo-alto-pan-os-globalprotect-pre-auth-authen.
Note: sub-agents shared the main scratchpad; T5 moved to a subfolder after a helper was overwritten (no repo effect).

## T1
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:26:36Z · ended_at=2026-10-18T13:57:02Z · duration_seconds=1826
**Entries:** 16 checked · clean 11 · imprecision 4 · factual-error 1
**Claims:** in_scope=401 checked=401 (14 unreadable: community.citrix.com 403 everywhere; presseportal captcha)
**Self-telemetry:** webfetch_calls=7 websearch_calls=6 bridge_fetches=70 urls_checked=115
Lead (ANSSI CVE-2026-72898): false positive — the ANSSI PDF has no text layer; rendered pages 3-4 carry the id. The citation-cve check reported "does not mention" for an unextractable PDF.

## T3
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:26:49Z · ended_at=2026-10-18T13:57:17Z · duration_seconds=1828
**Entries:** 20 checked · clean 14 · imprecision 5 · factual-error 1
**Claims:** in_scope=457 checked=457 (443 ok, 9 F3, 5 unreadable)
**Self-telemetry:** webfetch_calls=4 websearch_calls=1 bridge_fetches=87 urls_checked=80 (jina fallback used for BeyondTrust + Wordfence)
Leads: Bricksforge Previdian quote and Exchange banner quotes were verbatim at publication; pages rewritten since — noted and left.

## T9
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:48Z · ended_at=2026-10-18T13:59:42Z · duration_seconds=1914
**Entries:** 14 checked · clean 3 · imprecision 8 · factual-error 3
**Claims:** in_scope=423 checked=423 (1 unreadable: community.citrix.com)
**Self-telemetry:** webfetch_calls=2 websearch_calls=7 bridge_fetches=35 urls_checked=92
Leads: Kiteworks CVE-2026-54154 clause mis-bound (id lives in GHSA-5xhq-9wq3-rvj6); Bitget page revised since capture (quote true when captured, now stale; "pending a fix" stale).

## D2
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:28:13Z · ended_at=2026-10-18T14:02:31Z · duration_seconds=2058
**Entries:** 14 checked · clean 0 · imprecision 0 · factual-error 14 (plus 4 lead-only records: 3 clean, 1 imprecision)
**Claims:** in_scope=278 checked=278 (149 ok, 70 F4, 23 F3, 14 F13, 12 F14, 10 F5)
**Self-telemetry:** webfetch_calls=2 websearch_calls=4 bridge_fetches=85 urls_checked=55
Groups: PHP SOAP same (survivor ...soap-glob); SD-WAN two findings (20182 survivor 2b cve-2026-20182-...-pre; 20245 survivor 2c ...actively-exploi); n8n same (survivor multi-CVE); FortiClient EMS same (survivor ...actively-exploited-to-push-ek); SimpleHelp same (survivor 06-30); Cisco ISE same (survivor cve-2026-20181-cve-2026-20190-...).
Lead-only: three quote-literal WARNs are extraction artefacts (link rendering, og:description meta, escaped underscore); Japan Digital Agency nippon.com source now 404 (quotes verbatim in the Wayback copy).

## D1
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:27:59Z · ended_at=2026-10-18T14:03:57Z · duration_seconds=2158
**Entries:** 17 checked · clean 0 · imprecision 0 · factual-error 17
**Claims:** in_scope=336 checked=336
**Self-telemetry:** webfetch_calls=2 websearch_calls=6 bridge_fetches=100 urls_checked=64

## G2
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:28:51Z · ended_at=2026-10-18T14:08:43Z · duration_seconds=2392
**Self-telemetry:** webfetch_calls=1 · websearch_calls=36 · bridge_fetches≈215
**Findings:** 17 items (7 not borderline, 10 borderline; 51 evidence quotes literal-checked against work/<run-id>/G2-bodies/)
**Source ledger:** 33 of 33 attempted
**Candidate sources:** 2 (imy-se-news, caf-fr-presse); recommends promoting piyolog
**Coverage gaps:** 13 recipe notes (inside-it-ch, heise-sec, borncity feeds reach back only 4-10 days; OAG/fedpol media listings unroutable)
**Watchlist sweep:** duty=none
Beyond Gravity: nothing material changed; hold condition unmet; expiry 2026-10-20 stands.

## G3b
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:29:01Z · ended_at=2026-10-18T14:09:54Z · duration_seconds=2453
**Self-telemetry:** webfetch_calls=5 · websearch_calls=12 · bridge_fetches≈190
**Findings:** 30 items (9 clear the bar, 21 borderline incl. 5 update_target candidates; 18 covered posts listed)
**Source ledger:** 30 of 30 attempted (6 with zero in-window posts)
**Candidate sources:** 4 (Barracuda Research, Checkmarx Zero, Report URI blog, XBOW Labs)
**Coverage gaps:** 9 recipe reports (socradar sitemap; msft-secblog feed stopped 2026-10-08; swisspost-cybersecurity marketing only; redcanary feed frozen 2026-08-20)
**Watchlist sweep:** duty=none

## D3
**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-18T13:28:24Z · ended_at=2026-10-18T14:12:27Z · duration_seconds=2643
**Entries:** 16 checked · clean 0 · imprecision 4 · factual-error 12
**Claims:** in_scope=373 checked=373 (ok 291, F3 9, F4 62, F5 5, F13 2, F14 1, unreadable 3)
**Self-telemetry:** webfetch_calls=7 websearch_calls=11 bridge_fetches=105 urls_checked=80 (last two estimates)
Note: batch L reused D3's helper in the shared scratchpad and appended 3 rows to truth-D3.claims.yaml; D3 cleaned its file and saved them to truth-L.claims.recovered-from-D3.yaml.
