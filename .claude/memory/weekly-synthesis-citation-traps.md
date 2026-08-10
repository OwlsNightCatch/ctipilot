# Weekly synthesis — the citation traps that only appear when you compose from entries

The weekly re-frames facts it did not fetch. Iteration 1 of the 2026-W32 verifier found 17 truth
defects and **every one was a sourcing defect, not a content defect** — the analysis was right, the
citation was pointed at the wrong page. Five reusable shapes:

1. **Blog post vs. the PDF underneath it.** CERT Polska's incident write-up carries the narrative;
   the linked PDF report carries the mechanics (device names, protocols, credentials). The operational
   entry cited both; the weekly inherited only the blog URL and attached PDF-only facts to it.
   **Check which of a source's two artefacts actually carries the clause.**
2. **Vendor blog URLs mutate in place.** `n-able.com/blog/n-central-security-update-august-2-2026`
   now serves an *August 6* update; the August 2 quote is simply gone. A quote verified when the
   operational entry was written can fail days later at the same URL. Re-fetch before re-quoting, and
   take the source date from the page's current metadata, not from the slug.
3. **Slugs are not datelines.** `Presse2026/260601_NIS2_BSI-Portal.html` reads as 1 June to an
   English eye; the page's own `Datum` field says `06.01.2026` = **6 January** (DD.MM.YYYY). The
   internal contradiction gave it away — a portal opened in June cannot have 11,388 registrations
   recorded in March. **When a date is load-bearing, read the dateline field, never the URL.**
4. **National-CERT relays carry less than the vendor bulletin.** CERT-FR's WALLIX advisory has the
   affected/fixed versions and nothing else — no CVSS, no "unauthenticated", no scope. Attributing the
   vendor's own severity and scope to the relay is the single most repeatable F3 in this pipeline.
   Cite the relay for what the relay adds (that it reached the constituency, and when).
5. **Two facts, one clause.** Telex.hu describes a Windows domain-admin escalation *and*, separately,
   a virtualisation-environment compromise with a VM count. Merging them into one clause invents a
   claim neither source makes. Same shape as the CVE-labelled-clause rule: one citation per clause.

**Sub-agent figures are candidates, not facts.** Three numbers a research agent attributed to Socket
(package count, poisoned-version count, mean detection latency) were absent from the fetched body.
`grep -F` every number against the saved text before it reaches an entry.

**Drop rather than half-source.** A sentence naming a researcher and a CVE that no fetched source
connects is not fixable by adding a plausible link — the W32 passkey entry lost its fourth disclosure
and was retitled and renamed instead. That is the cheap outcome; a half-sourced attribution is not.

**Gate contradiction to reconcile (open):** `prompts/weekly-summary.md` Phase 4 says
`weekly-vuln-rollup` entries carry per-CVE `cves[]`, but `check_run.py`'s cross-run dedup FAILs any
non-update entry sharing CVE ids with the last 14 days — which a roll-up does by definition. Three
consecutive weeklies have resolved it the same way: per-CVE trajectory as a **body table**, `cves: []`
in frontmatter. Either the prompt or the check should say so.
