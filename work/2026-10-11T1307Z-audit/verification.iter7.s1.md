**Model:** Sonnet 5.5 (`claude-sonnet-5-5`)
**Timestamps:** started_at=2026-10-19T18:09:14Z · ended_at=2026-10-19T18:38:22Z · duration_seconds=1748

## Verification report — 2026-10-11T1307Z-audit (iteration 7, slice s1)

Scope: 27 entries (all existing; the NeedyMantis entry is in another slice), each read whole including every dated section, and all 234 ledger claims answered (233 ok, 1 F3; `claims.iter7.s1.yaml` fully covered, the 6 claims changed since iteration 6 included). Every cited page was read this pass: cached gate bodies for most, `extract` / `pdf` / `ncsc-csh post` / `cisa-kev` / raw `url` (GitHub advisory CVSS panels, Rapid7 and ABC JSON-LD dates, KEV records, FIRST EPSS, the WID portal list API) for the rest, WebFetch for the two cisa.gov pages (ED 26-03 and the 2026-08-05 KEV alert). Unreadable: the old cyber.gov.au alert address (WebFetch 503; only the run-record summary for the OpenAI/Medicare internal record says it answers 404, no reader-facing text depends on it) and the WID portal detail JSON (the SPA text was read through jina). All evidence-quote originals and quotes were searched against the cited bodies with a normalising script; the misses are markdown-link or footnote-marker artifacts, one trailing comma/period, and quotes with no source_url (CISA alert), none a content difference.

### Delta walk (iteration-6 findings on this slice, 11 items)

- OpenAI/Medicare F11 (ACSC page now dated 25 Sep 2026): decline holds. Cyber Daily (2026-09-24) says "a 24 September alert", and the live page shows "Published 25 Sep 2026"; one day, no contradiction in substance.
- Acronis F9: applied and correct. The advisory record says published 2026-09-17T13:30:00Z; Help Net Security (2026-09-16) says "published on Tuesday" (2026-09-15); BleepingComputer (2026-09-15) already quotes the advisory.
- Liechtenstein F9: applied and correct. The Record: "gained access ... for two days beginning on July 29"; government release: "in der Nacht auf den 30. Juli".
- Liechtenstein F11 ("Defender takeaway (updated)"): decline does not remove the check-4c(h) pattern; re-raised as advisory (#3).
- LiteLLM F3: applied and correct. The table row's Source cell now cites the KEV catalog (dateAdded 2026-06-08) beside GHSA (CVSS 8.7, affected 1.74.2 to < 1.83.7).
- LiteLLM F11 (affected_products): still absent; re-raised as advisory (#4, low confidence).
- Exchange F5: applied. The detection concept is marked "in analyst judgement" and rests on MB VRED's coercion/relay description.
- Exchange F11 (sourcing_note): still about seven sentences; re-raised as advisory (#5).
- Kairos F11: applied. The record summary no longer cites an uncited Ransomware.live count; Ransomware.live page: "Discovered 2026-09-02 14:25 UTC".
- Conference F9: applied and correct. Write-up lists COM object, recap lists Run key and reinstalling scheduled task.
- Conference F11: decline rationale does not match the title literally; re-raised as advisory (#6, low confidence).

### Citation does not support the claim
- #1 F3 TeamCity (`cve-2026-63077-teamcity-onprem-unauth-deserialization-rce.md`), Detection paragraph, claim c7a209d351: "the date shown for such an agent is not the attempt time, so the log timestamps are what date an attempt". JetBrains follow-up of 2026-08-07: "Please note that the date shown for an unauthorized agent does not necessarily indicate when the exploit attempt occurred. Instead, you should rely on the timestamps of the relevant log messages when determining when an attempt may have taken place." The entry drops the hedge; write "is not necessarily the attempt time". (https://blog.jetbrains.com/teamcity/2026/08/cve-2026-63077-update/)

### Editorial / less-is-more flags (advisory)
- #2 F11 Em dashes in reader-facing text: nginx (title, headline, body), LiteLLM (title, headline, summary, body), Liechtenstein (summary, body), Exchange (title, body), JFrog (title, headline), Acronis (title). Left as render-stripped style by the audit; advisory.
- #3 F11 Liechtenstein: "**Defender takeaway (updated):**" in the 2026-09-02 section sits beside a current main takeaway and addresses the Swiss register, a different finding.
- #4 F11 (low confidence) LiteLLM: no `affected_products` and no `cves[].affected`; product pages and triage agents key on them.
- #5 F11 Exchange: sourcing_note is about seven sentences, argues the pre-auth rating and says "see body" twice; the standard is two sentences of provenance.
- #6 F11 (low confidence) Conference phishing: Correction closes "so the entry no longer presents the campaign as conference-targeted", while the title still reads "reported against conference attendees"; sourcing_note is three sentences and refers to "the text".
- #7 F11 (low confidence) Everest Forms takeaway: "ran an affected version after April"; Wordfence dates exploitation from 2026-04-13, so "since 13 April".
- #8 F11 (low confidence) TeamCity: sectors [public-sector, finance, telco, technology] are named by no cited page.

### Checks that came back clean
CVSS per authority: GLPI (seven GHSA CVSS 4.0 panels 5.1/7.1/7.0/7.0/5.9/8.4/8.4 match cves[]), LiteLLM GHSA 8.7, JFrog (High, no numeric; fixed builds table; Wiz corrected list), Kiteworks (eight GHSA records: 10.0, 9.8 x3, 9.4, 9.3, 7.2, 7.2 with the affected bounds and PR:H / UI:R flags), Cisco 10.0 with the Validator revision 2.0 of 2026-06-16, Acronis 7.8, Exchange 8.0 (PR:L/UI:R), Everest Forms 9.8, nginx 9.2 (NCSC-CH, depthfirst; nginx.org medium). KEV dates match the live catalog (CVE-2026-20182 05-14, -42271 06-08, -63077 08-05 with ransomware Known and forensicTriage Yes, -42016/-42018 09-11, -87886 09-16, -86950 09-29 with forensicTriage No, -35273 06-12, CVE-2019-18935 2021-11-03 with ransomware Known). EPSS: Dirty Frag 0.9324/0.9286 (FIRST 2026-09-04), CoreGraphics 0.01242 (FIRST 2026-10-10..12). Internal records (relabels on G7, voicemail and week-23, TVP date correction, ACSC URL move, KEV/BC wording attribution): each frontmatter or body change is source-supported and carries no new reader-facing information. Record summaries match their sections on all 27 entries. Registry keys all resolve and no key is a tombstone; every references[] id exists; classification blocks present and in vocabulary on all 27; org_triage null and watchlist false everywhere; single-source flags carry a plain sourcing_note where required. Priorities: considered and left JFrog critical (exploited chain with a dropped backdoor, KEV-listed), Cisco critical, Kiteworks high (unauthenticated chain to root at a vendor with Swiss-authority customers; no exploitation stated), Dirty Frag high, CoreGraphics high. Missed angles: none evidenced for this slice.

### Verdict
NEEDS_FIXES (truth: 1, editorial: 0, advisory: 7)

The single truth finding is a dropped hedge in one clause. The advisory items may be left, except that #3 and #6 are the delta re-raises whose decline rationales do not hold literally.

### Findings summary (machine-readable)
See `work/2026-10-11T1307Z-audit/verification.iter7.s1.findings.yaml`.
