**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-21T06:18:03Z · ended_at=2026-09-21T06:32:09Z · duration_seconds=846

## Verification report — 2026-09-21T0410Z-intel (iteration 5)

Cold pass, no memory of iterations 1-4. Re-fetched all cited primary sources myself via `tools/fetch_source.py extract`. Cross-checked iteration-4's fixes (REF9334 São Paulo dual-framing, NightEagle contrastive-clause removal, Huntress VSS "a few minutes later", Gentlemen VHDX/Responder fixes) against the live sources — all hold up; no regression found. This iteration surfaces new defects not caught by iterations 1-4.

### Unsupported / hallucinated facts

**#1 (F4) — AFPA entry, sourcing_note reliability mismatch.** The entry's own `sourcing_note` states: *"Cyberattaque.org and FrenchBreaches are lower-reliability (C) niche breach-tracking outlets."* `sources/sources.json` registers FrenchBreaches at `"reliability": "B"` (Cyberattaque.org is indeed `"C"`). The sourcing_note misstates FrenchBreaches' registered reliability tier, contradicting the store's own authoritative source record. Fix: correct the sourcing_note to reflect FrenchBreaches = B, Cyberattaque.org = C (they are not both "C").

**#2 (low confidence) (F4) — TraderTraitor entry, `techniques[]` T1566.002 mapping.** `T1566.002` = "Spearphishing Link" (email delivery of a malicious link). Neither the body nor the cited SentinelLabs source describes email or a link as the delivery channel — the source states only "The attacker makes contact with job seekers from the company that is ultimately compromised" and the victim's own timeline shows the lure delivered by cloning a GitHub repo via GitHub Desktop, not by clicking an emailed link. `T1566.003` ("Spearphishing via Service," the standard mapping for DPRK's LinkedIn/social-platform recruiter-outreach pattern) or simply omitting a spearphishing sub-technique may be the more defensible choice; as mapped, T1566.002 names a specific mechanic (email link) the source does not state.

**#3 (low confidence) (F4) — NightEagle entry, "forged payload" embellishment.** Body states Kaspersky's technique was "overwriting and injecting a **forged** payload into the VIEWSTATE framework parameter." Securelist's own text (fetched this iteration) says only: *"extracting the cryptographic keys used by Microsoft Exchange from the ASP.NET configuration, overwriting the VIEWSTATE framework parameter, and injecting **a payload** into it"* — no "forged" qualifier appears anywhere in the source. Minor, but the word implies a specific technical property (a cryptographically forged value) the source does not claim.

### Surface contradiction

**#4 (F9) — Conference-phishing entry, NetSupport Manager persistence mechanism contradicted by Huntress's own fuller write-up.** The entry states NetSupport Manager "carries persistence for all three payloads: a keyboard-filter driver, a Windows service, a Winlogon entry, **a Run key and a self-reinstalling scheduled task**." This wording tracks a direct quote in the entry's cited source (`huntress.com/blog/google-doc-sidebar-malware-mac-windows`, 2026-09-15 — a "Tradecraft Tuesday" webinar recap): *"It's got a keyboard filter driver, a Windows service, a Win logon, a Run key, a scheduled task to reinstall itself…"* (Jon Semon, quoted verbatim). But the recap article itself links to "the full technical details" at `https://www.huntress.com/blog/defcon-phishing-google-doc-malware` (published 2026-08-19, same author team) — the actual technical write-up this campaign was analyzed for. I fetched it: its own persistence description for the identical payload reads: *"NetSupport carries the persistence for all three. It installs a kernel-mode keyboard filter driver at `C:\Windows\system32\drivers\nskbfltr.sys`, registers it as a service under `HKLM\SYSTEM\...\Services\nskbfltr`, modifies Winlogon, and **registers its own COM object**."* — no Run key, no scheduled task anywhere in the detailed technical write-up. The entry silently adopted the informal recap's (looser, spoken) characterization without cross-checking it against the vendor's own more rigorous original reporting of the exact same artifact, and the two accounts disagree on a concrete forensic detail (COM object registration vs. Run key + scheduled task). Per check 9 this needed a `Contradiction:` line, not silent adoption of one account.

### Needs more research

**#5 (F8) — Conference-phishing entry is sourced to a recap of month-old research; the richer original primary was never fetched or cited.** The entry's sole source is `https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows` (dated 2026-09-15), which is explicitly framed in its own text as a "Tradecraft Tuesday" webinar-highlights recap: *"Read their blog for full technical details"* linking to `https://www.huntress.com/blog/defcon-phishing-google-doc-malware`. I fetched that linked article: dated **2026-08-19** — over a month before this run's window — authored by the same Huntress team, and it already contains every substantive fact in this entry: the same `@HartmansDoeke` CoinDesk-persona X-DM lure, the same Google-Doc-with-Apps-Script-sidebar, the same macOS AMOS/ClickFix chain, the same Windows ClickOnce/Norwegian-certificate route, the same second DocSend document with the Discord certificate, the same NetSupport Manager / TLS-proxy / Ledger-implant three-payload set, and the same self-signed rogue CA impersonating "Google Trust Services CN=WR3." This is check 8's "months-old news as new" pattern: a campaign fully disclosed 33 days before the entry's `event_date` (2026-09-15, taken from the recap's own publish date) is presented as this run's fresh, `priority: high` finding, sourced only to a talk-show-style recap rather than to (or alongside) the actual primary technical report. Fix: either re-source to the 2026-08-19 write-up as the primary (with the 2026-09-15 recap as corroborating, if it adds anything beyond quotes), explicitly disclose the finding's actual age, and reconsider whether `priority: high` (a "renders at the top of the 24h window" bar) is warranted for month-old research — or drop it as stale/non-novel for this window.

**#6 (low confidence) (F8) — NightEagle entry, unsupported technical elaboration.** Body states dev-tunnels and rdp2tcp avoid opening new ports "because both mechanisms ride on already-permitted **outbound HTTPS** and an existing RDP session." Kaspersky's article (fetched this iteration) never states the dev-tunnels traffic rides HTTPS specifically — it only says dev tunnels "allows local web services to be published for internet access." Plausible general knowledge about how Microsoft Dev Tunnels works, but not something the cited source states, and check 3 requires an inline citation for such added technical claims.

### Editorial / less-is-more flags (advisory)

**#7 (low confidence) (F11) — Huntress VSS entry, `techniques[]` T1018 mapping.** `T1018` = "Remote System Discovery" (discovering other hosts on a network). Mapped presumably to "the attacker enumerated active Remote Desktop sessions" — but T1018's own definition is about discovering remote *systems*, not enumerating active *sessions* on the local host, which is closer to account/session-discovery techniques (e.g. T1033/T1049 family) than to T1018. Debatable; flagging for the main agent's judgment rather than asserting it is wrong.

### Claims missing inline citation / adjacency

**#8 (F3) — AFPA entry, joint citation overclaims one of two co-cited sources.** Body: *"independent sample review by Cyberattaque.org and FrenchBreaches additionally found full dates of birth, internal identifiers, a 'partner' field (one observed value, 'LHEA,' suggesting a partner-feed origin), **email addresses and nationality**, spanning records created or modified from 2006 through 2026"* — cited to both `[Cyberattaque.org, 2026-09-15]` and `[FrenchBreaches, 2026-09-19]` jointly. I fetched both pages this iteration. Cyberattaque.org's own text never mentions nationality at all, and on email addresses states the opposite of "found": *"La structure comporte également des champs prévus pour des adresses e-mail... Dans les échantillons observés, plusieurs de ces champs sont cependant vides"* ("The structure also includes fields provided for email addresses... in the observed samples, however, several of these fields are empty"). Only FrenchBreaches' own bullet list ("des nationalités... des adresses e-mail") actually supports both facts. The joint citation vouches for Cyberattaque.org supporting a clause it does not (and on email, arguably contradicts). Fix: attribute "email addresses and nationality" to FrenchBreaches only, or note the two trackers' samples differed on whether email fields were populated.

### Verdict

`NEEDS_FIXES (truth: 4, editorial: 3, advisory: 1)`

Iteration-4's specific fixes (REF9334 dual-framing São Paulo/late-night quote, NightEagle contrastive-clause removal, Huntress VSS "a few minutes later," Gentlemen VHDX-file/Responder corrections) were independently re-verified against the live primaries this iteration and all hold up — no regression. This iteration's new findings center on the AFPA entry's source-attribution precision (#1, #8) and the conference-phishing entry's reliance on a recap of month-old research without cross-checking the fuller original write-up it explicitly links to (#4, #5) — the latter is the most consequential finding of this pass: it changes both the entry's sourcing (a richer, more authoritative primary exists and was never fetched) and its editorial framing (this is not fresh news). The remaining items (#2, #3, #6, #7) are lower-confidence ATT&CK-mapping and word-choice nits offered for completeness per the coverage obligation.

No new missed-angle (F10) or dedup (F7) findings beyond what's already noted in the run record's own borderline-drops; entity-registry links (actor:cybernox, actor:xmetah, incident:afpa-third-party-accommodation-tool-data-extraction-2026-09, actor:thegentlemen, actor:qilin) were checked against `entities/registry.yaml` and are correctly keyed with no unmerged duplicates or alias misses found.

### Findings summary (machine-readable)
```yaml
- code: F4
  category: hallucinated-fact
  section: incident
  item: "2026-09-21/afpa-third-party-accommodation-tool-data-extraction"
  url_or_quote: "\"Cyberattaque.org and FrenchBreaches are lower-reliability (C) niche breach-tracking outlets.\""
  summary: "sources/sources.json registers FrenchBreaches at reliability B, not C; the sourcing_note misstates the store's own authoritative source rating for FrenchBreaches (Cyberattaque.org is correctly C)."
- code: F4
  category: hallucinated-fact
  section: threat
  item: "2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop"
  url_or_quote: "techniques[]: T1566.002"
  summary: "(low confidence) T1566.002 = Spearphishing Link (email + malicious link); neither the body nor SentinelLabs' article describes email or a link as the delivery channel — the article says only \"the attacker makes contact with job seekers\" and the victim timeline shows the lure delivered via a cloned GitHub repo, not a clicked link."
- code: F4
  category: hallucinated-fact
  section: threat
  item: "2026-09-21/nighteagle-apt-q-95-ghostcontainer-devtunnels-rdp2tcp-dcsync"
  url_or_quote: "\"overwriting and injecting a forged payload into the VIEWSTATE framework parameter\""
  summary: "(low confidence) Securelist's own text says only \"injecting a payload\" — no \"forged\" qualifier appears in the cited source."
- code: F9
  category: surface-contradiction
  section: threat
  item: "2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence"
  url_or_quote: "\"a keyboard-filter driver, a Windows service, a Winlogon entry, a Run key and a self-reinstalling scheduled task\""
  summary: "Entry follows the cited recap's spoken-quote characterization of NetSupport Manager's persistence; Huntress's own fuller technical write-up (huntress.com/blog/defcon-phishing-google-doc-malware, 2026-08-19, linked from the cited recap as \"full technical details\") instead states it \"registers its own COM object\" with no Run key or scheduled task mentioned — a genuine discrepancy between two same-publisher accounts of the identical artifact, adopted silently rather than flagged."
- code: F8
  category: needs-more-research
  section: threat
  item: "2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence"
  url_or_quote: "https://www.huntress.com/blog/google-doc-sidebar-malware-mac-windows"
  summary: "Sole cited source is a 'Tradecraft Tuesday' webinar recap that explicitly links to \"full technical details\" at https://www.huntress.com/blog/defcon-phishing-google-doc-malware, published 2026-08-19 (33 days before this entry's event_date) by the same authors, already containing every fact in this entry (same X-DM lure, same Google Doc sidebar, same macOS/Windows chains, same rogue CA). Check-8 months-old-news-as-new pattern; the richer original primary was never fetched or cited, and priority:high should be reconsidered given the finding's actual age."
- code: F8
  category: needs-more-research
  section: threat
  item: "2026-09-21/nighteagle-apt-q-95-ghostcontainer-devtunnels-rdp2tcp-dcsync"
  url_or_quote: "\"because both mechanisms ride on already-permitted outbound HTTPS and an existing RDP session\""
  summary: "(low confidence) Kaspersky's article never states the dev-tunnels traffic rides HTTPS specifically; plausible general knowledge but an added technical claim beyond the cited source with no citation."
- code: F11
  category: editorial-advisory
  section: research
  item: "2026-09-21/huntress-vss-abuse-detection-correlation-ntds-shadow-copy"
  url_or_quote: "techniques[]: T1018"
  summary: "(low confidence) T1018 = Remote System Discovery (discovering other hosts), mapped presumably to \"enumerated active Remote Desktop sessions\" (session/account discovery on the local host) — a debatable fit; flagging for judgment rather than asserting it is wrong."
- code: F3
  category: claim-not-supported
  section: incident
  item: "2026-09-21/afpa-third-party-accommodation-tool-data-extraction"
  url_or_quote: "\"additionally found full dates of birth, internal identifiers, a 'partner' field ..., email addresses and nationality, spanning records created or modified from 2006 through 2026 ([Cyberattaque.org, 2026-09-15]; [FrenchBreaches, 2026-09-19])\""
  summary: "Cyberattaque.org's own article never mentions nationality, and on email addresses says the opposite of \"found\" (fields present in the schema but observed empty in their samples: \"plusieurs de ces champs sont cependant vides\"); only FrenchBreaches supports both facts. Joint citation overclaims Cyberattaque.org's coverage."
```
