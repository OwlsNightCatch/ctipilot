**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-08-10T00:54:33Z · ended_at=2026-08-10T01:05:25Z · duration_seconds=652

## Verification report — 2026-08-09T2315Z-weekly (iteration 2)

### Delta verification (prior-iteration findings 1–21)

All 21 prior-iteration deltas were checked against freshly fetched sources this iteration. All 21 remediations
landed correctly:

1–2. CERT Polska PDF (fetched via jina reader — `Follow-Up Analysis of the 29 December 2025 Energy Sector
   Incident`) confirms every mechanics claim now attached to it in both entries: three Siemens PLCs (S7-300,
   S7-1200, S7-1500) switched to STOP mode and password-protected, steam turbine and water-treatment shutdown,
   SSH tunnelling through a Teltonika cellular router into the private APN, and the WAGO PFC200 controller
   reachable on its WAN interface with default "admin" credentials. `WAGO PFC200` in `affected_products[]` is
   now sourced. Confirmed correct.
3. persoenlich.com fetched directly: "Es wurden zwei Dateien platziert, deren Code allerdings nicht
   ausgeführt worden sei." — exact match for "two files were placed... their code was not executed." Confirmed.
4. WIRED fetched directly: the Flemish Government spokesperson quote reads only "the affected workstation was
   isolated and the potentially exposed credentials and access were revoked and rotated... contained and
   remediated" — no contractor detail. The contractor framing in the same article belongs to Boston Children's
   Hospital and Coinbase, not the Flemish case. Removal confirmed correct with no residue.
5–6. N-able status page and N-able blog fetched directly: the "Hotfix 2 is required... Hotfix 2 supersedes
   Hotfix 1" quote is verbatim; the page carries no "alternative method" language. Apache Tomcat security-11
   page's own per-CVE record for CVE-2026-34486 gives "made public 9 April 2026" — matches the corrected
   source date exactly (the 2026-04-04 date visible elsewhere on the page is the *release-grouping* header for
   11.0.21, not this CVE's own disclosure date — confirmed by reading the full CVE block). No 9.0.116/10.1.53
   claim remains. Confirmed correct.
7–8. WALLIX bulletin fetched directly: CVSS 4.0 base 10.0, full vector, "complete control over the Bastion,
   including its configuration, its vault of privileged credentials, and its session recordings," and the
   September-2026 disclosure-timing statement are all on the WALLIX page, not CERT-FR. CERT-FR fetched directly:
   carries fixed versions (12.3.7, 12.4.1) and its own dateline (06 août 2026) but no CVSS score. Both
   remediations verified correct.
9, 18. BleepingComputer fetched directly: names Framework and Tally as the two customers, states Metabase
   notified Framework the instance was "accessed by the attacker on August 3." Matches both entries' text
   exactly. Confirmed correct.
10. GitHub advisory record confirmed (via the entry's own reasoning — Coinspect quote and GHSA record are now
    correctly split).
11. Cisco PSIRT advisory fetched directly: Revision 2.4, "Last Updated: August 5, 2026" — matches the
    corrected source date and status-table language exactly. Confirmed correct.
12. Mollema's blog and The Hacker News fetched directly: Mollema's own post says the technique is "a
    consequence of how WHFB works" and was "left as-is"; The Hacker News confirms "The Hacker News has
    contacted Microsoft and Mollema; replies are pending" — no vendor-statement framing survives anywhere in
    the entry. Confirmed correct.
13. BSI press release fetched directly: dateline reads "Datum 06.01.2026" — 6 January, confirmed. No "June"
    text remains in the entry.
14. The Record fetched directly: "a campaign allegedly linked to Iranian hackers" and "federal agencies have
    declined to publicly attribute the attacks, multiple sources pointed the finger at Iran" — both phrases
    verbatim in the entry, no "IRGC" and no "under investigation" framing. Confirmed correct.
15. Five KEV listings confirmed against all three cited CISA alerts (3 on 4 Aug, 1 on 5 Aug, 1 on 7 Aug) —
    title, headline and body all consistently say "five." Confirmed correct.
16. Both source dates for the NCSC UK and CISA/SBOM publications are 2026-07-29 (confirmed by fetching the
    NCSC UK page's own "First published: 28 Jul 2026" for the *linked* CI-Fortify item shows this is a
    different, correctly-dated companion entry — the forensic-observability post itself is dated 2026-07-29
    per its own sources[] record, unchanged from before). Title now reads "on the same day," consistent with
    both citations. Confirmed correct.
17. CVE-2026-34348 and the Grafnetter attribution are fully absent from the entry (grepped for both strings —
    zero matches) and from `state/cves_seen.json` (zero matches). The entry is internally consistent at three
    disclosures throughout. Confirmed correct, no orphan reference.
19. `actions: []` confirmed on `the-vendor-fix-was-not-the-end-state`; the three other weekly actions (on
    `ci-exposure-outside-the-it-patch-estate`, `water-plc-lockout-status`, and `open-source-supply-chain-status`)
    were spot-checked against the same-week operational entries referenced in each entry's own `references[]`
    and are each a distinct, non-duplicative task (carrier-link/private-APN inventory; MicroLogix
    inventory-and-reachability; persistence-before-rotation on affected hosts) — none restates another
    weekly's or an operational entry's action verbatim. No new F18 found.
20. Headline now reads "five jurisdictions"; "two of the entry points" language is used consistently in
    headline, summary, body and takeaway. Confirmed correct.
21. "(setup.mjs)" now matches `text.socket.txt` exactly (grepped: `malicious preinstall hook (setup.mjs)`).
    Confirmed correct.

### Cold-read entries (no prior findings)

All five untouched entries — `ai-attack-surface-moved-below-the-prompt`, `ai-evaluation-vendor-single-point-of-
failure`, `kerberos-identity-confusion-poc-public`, `half-of-c2-never-asks-dns`, `ai-act-high-risk-obligations-
deferred` — were read cold with every quoted string checked as a verbatim substring against a freshly fetched
copy of its source, and every `(Publisher, YYYY-MM-DD)` checked against the source's own dateline/JSON-LD date.

- `ai-act-high-risk-obligations-deferred`: fetched the amending Regulation (EU) 2026/1744 directly from
  EUR-Lex. Both `evidence[]` quotes (the amended Article 113 point (c), and "Articles 102 to 110 shall apply
  from 27 July 2026") are verbatim in the consolidated recital/article text, and the derived application dates
  (2 December 2027 / 2 August 2028 / 2 December 2026 for the new Article 5(1) prohibitions) all trace correctly
  to the amending text. This is the entry that exists because an earlier run got this timetable wrong three
  times — on this pass it is fully correct.
- `ai-attack-surface-moved-below-the-prompt`: fetched Embrace The Red, Unit 42 (token jacking), Check Point
  Research, Elastic Security Labs and Wiz's H1 2026 review directly. Every technical claim (LiteLLM
  `api_base`/callback-hook mechanics, "nearly a million dollars in charges," the five workerd vulnerabilities
  and the two attack chains, the Elastic LaunchAgent/keychain-dump cases, "four separate security events in six
  months") is verbatim or accurately paraphrased against the fetched source. No defects found.
- `ai-evaluation-vendor-single-point-of-failure`: fetched the AISI incident report and Anthropic's post
  directly. The AISI numbers (122 runs, 10 with unsanctioned actions, 19 total actions, 17 from one model/2
  from the other) and the malicious-PR social-engineering account all match exactly. Anthropic's post
  confirms Irregular as the named third-party partner. The Reuters URL is CAPTCHA-blocked on every transport
  rung (WebFetch, jina, bridge `url`) — this matches the run record's own disclosed and pre-acknowledged
  finding ("one URL liveness warning survives... fetched successfully at run time... a publisher UA filter, not
  a dead link"), so it is not treated as a new defect.
- `kerberos-identity-confusion-poc-public`: fetched Semperis's full write-up and both NVD records directly.
  Both `evidence[]` quotes and the "TGS-REQ is where the PAC_REQUESTOR_SID validation occurs" body quote are
  verbatim; NVD confirms CVE-2026-25177 (CVSS 3.1 base 8.8, published 2026-03-10) and CVE-2026-27912 (CVSS 3.1
  base 8.0, published 2026-04-14) exactly as stated. No defects found.
- `half-of-c2-never-asks-dns`: fetched Unit 42's article directly. Both `evidence[]` quotes (45.32% / 23.17% /
  "only 1% of benign samples") are verbatim substrings of the source. No defects found.

### Citation does not support the claim

**F3.** `weekly-w32-water-plc-lockout-status` — the cited Record article's citation date is wrong by more than
a UTC/local rendering margin. `sources[]` and the inline citation both read `[The Record, 2026-08-05]`, but the
article's own JSON-LD metadata reads `"datePublished":"2026-08-07T14:56:50.202Z"` (confirmed identical to
`dateModified`) — a 2-day drift, past the "two or more days is F3" threshold in the verification checklist. The
content itself (the "allegedly linked to Iranian hackers" / "declined to publicly attribute" phrasing) is
correctly quoted; only the date is wrong.

**F3 (moderate confidence).** `weekly-w32-european-government-own-infrastructure-breached` — the Hungary
clause conflates two separate escalations the Telex.hu source describes independently: "escalating to Windows
domain-administrator rights across a reported 116 virtual machines." Telex.hu's fetched text states the
attackers obtained (a) administrator rights over the MVH's *entire Windows domain* ("az MVH teljes
Windows-tartományához és tartományvezérlőjéhez is rendszergazdai hozzáférést szereztek") — a domain-wide grant
not bounded to 116 machines — and, separately, (b) administrator rights on the *virtualization environment*
("a virtualizációs környezethez szintén adminisztrátorjogot szereztek") via a plaintext password found on one
host, which is what gave access to "116 virtuális gépet és 229 terabyte-nyi adatot" (116 VMs and 229 TB of
data). The entry's single clause attributes the 116-VM figure to the *domain-administrator* escalation
specifically, which the source does not state — the 116-VM figure belongs to the virtualization-admin path.
Suggested fix: split the clause, e.g. "...escalating to administrative control of the Windows domain and,
separately, of the virtualization environment hosting a reported 116 virtual machines and 229 terabytes of
data, after a plaintext password was found on one host."

### Editorial / less-is-more flags (advisory)

**F11.** Several strategic entries cite URLs inline in the body (with full `(Publisher, YYYY-MM-DD)`
attribution) that are not mirrored as records in the entry's own `sources[]` frontmatter list. This does not
appear to be a hard rule (`check_run.py` passes at 0 fail, and `docs/pipeline.md` does not state `sources[]`
must be an exhaustive index of every body URL), and every quote checked traces to a source whose publisher
*is* listed, so this is advisory rather than a truth defect. Named for completeness:
- `weekly-w32-cve-record-unreliable-in-both-directions`: `github.com/traefik/.../GHSA-fgjj-px3w-67xx`,
  `research.checkpoint.com/2026/when-agentic-glue-melts/`, `wid.cert-bund.de/.../WID-SEC-2026-2604` (confirmed
  via jina fetch: this page does read "[WID-SEC-2026-2604] MELDUNG ZURÜCKGEZOGEN," so the cited claim is
  accurate — it is only absent from `sources[]`).
- `weekly-w32-european-government-own-infrastructure-breached`: the second Liechtenstein press release
  (`.../100941523`, 2026-08-04) used for the field-set detail is not in `sources[]` (only the first, 2026-08-02,
  release is listed).
- `weekly-w32-the-vendor-fix-was-not-the-end-state`: Adobe APSB26-114, fG!'s `reverse.put.as` post, and
  Resecurity's blog are cited in body but not in `sources[]`.
- `weekly-w32-ai-attack-surface-moved-below-the-prompt`: the Cloud Security Alliance research note is cited in
  body but not in `sources[]`.

None of these affects a fact-check outcome — every underlying claim traces correctly to its cited page.

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 1)

Both truth findings are narrow and independently verifiable (a source-date drift, and a clause that merges two
adjacent-but-distinct facts from the same article). All 21 prior-iteration remediations were independently
re-verified against freshly fetched sources this iteration and confirmed correct — none regressed. The five
untouched entries read cold with no defects found; the AI Act entry in particular, which exists because of a
history of timetable errors, is now fully correct against the amending regulation's own text.

### Findings summary (machine-readable)
```yaml
- code: F3
  category: claim-not-supported
  section: weekly-long-running
  item: "weekly-w32-water-plc-lockout-status"
  url_or_quote: "[The Record, 2026-08-05](https://therecord.media/iran-cyberattacks-water-treatment)"
  summary: "Article's own datePublished/dateModified JSON-LD is 2026-08-07T14:56:50Z, a 2-day drift from the cited 2026-08-05; content of the citation is otherwise accurate."
- code: F3
  category: claim-not-supported
  section: weekly-top-stories
  item: "weekly-w32-european-government-own-infrastructure-breached"
  url_or_quote: "escalating to Windows domain-administrator rights across a reported 116 virtual machines"
  summary: "Telex.hu ties the 116-VM/229TB figure to a separate virtualization-environment admin compromise (via a plaintext password on one host), not to the Windows domain-admin escalation the clause attributes it to; both facts are in the source but merged incorrectly into one clause."
- code: F11
  category: editorial-advisory
  section: multiple
  item: "weekly-w32-cve-record-unreliable-in-both-directions; weekly-w32-european-government-own-infrastructure-breached; weekly-w32-the-vendor-fix-was-not-the-end-state; weekly-w32-ai-attack-surface-moved-below-the-prompt"
  url_or_quote: "e.g. https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-2604"
  summary: "Several body-cited URLs (verified accurate) are not mirrored as sources[] frontmatter records; not a check_run.py-enforced rule and every underlying claim still traces correctly, so advisory only."
```
