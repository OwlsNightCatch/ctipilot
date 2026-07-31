**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-07-31T05:41:09Z · ended_at=2026-07-31T06:02:33Z · duration_seconds=1284
**Self-telemetry:** urls_checked=26 · webfetch_calls=24 · bridge_fetches=26 · websearch_calls=0

## Verification report — 2026-07-31T0409Z-intel (iteration 3)

Cold confirmation pass on the other model. All 11 entries and the run record read end to end; every cited URL in every entry fetched in this iteration (26 distinct source URLs, none 404, none generic/homepage/NVD-per-CVE). Independent authority cross-checks performed against the MITRE CVE 5.2 records for CVE-2026-65884 / CVE-2026-65885 / CVE-2026-3055, the NVD record and FIRST EPSS API for CVE-2026-3055, the MSRC SUG API record for CVE-2026-42897, the CISA KEV catalogue, the NCSC-CH Cyber Security Hub post API, and the Storyblok CMS payload behind the Stadler Rail media release.

The previous iteration's CLEAN does not hold. Four truth-class defects and two editorial defects survive, one of them **introduced by an iteration-1 remediation that rested on a false premise**.

### Citation does not support the claim

**F1 — Stadler Rail media release: wrong publication date, and the "unrevised since publication" claim is contradicted by the very metadata the entry cites.**
Entry: `entries/2026-07-31/everest-publishes-stadler-rail-supplier-archive.md`

The entry states, in three places:
- frontmatter `sources[1].date: "2026-07-23"`
- summary: `"Stadler's own media release, unchanged since 2026-07-23, still states no security-relevant or personal data was taken"`
- body: `"Its media release, which its content-management metadata shows has not been revised since it was published on 2026-07-23, states that Stadler lost no data..."` — cited `([Stadler Rail, 2026-07-23](https://www.stadlerrail.com/en/media/media-releases/cybervorfall))`

And the run record repeats it: `"Stadler's own release — confirmed unrevised since 23 July against its content-management timestamps"`.

I fetched the page via `python3 tools/fetch_source.py url https://www.stadlerrail.com/en/media/media-releases/cybervorfall`. Its Storyblok story object is embedded in the server payload:

```
"story":{"name":"Cybervorfall","created_at":"2026-07-20T14:28:30.804Z",
 "published_at":"2026-07-23T07:35:27.738Z","updated_at":"2026-07-23T07:35:27.751Z",
 "content":{... "date":"2026-07-21 00:00", "lead":"Cyberkriminelle haben sich illegal Zugriff ..."
```
and the story's own record carries `"first_published_at":"2026-07-21T07:57:43.565Z"`. The **visible dateline rendered immediately above the lead paragraph is `21.07.2026`.**

Two defects follow:
- (a) **Citation-date drift of two days.** Check 2(e): the citation date must match the source's own publication date (visible dateline / published_time). The dateline is 21.07.2026 and the content `date` field is `2026-07-21 00:00`; the entry cites 2026-07-23. Two days is F3, not a UTC rendering artifact.
- (b) **The claim is self-contradicting against its own stated evidence.** The release was first published 2026-07-21 (`first_published_at`) and last republished 2026-07-23 (`published_at` / `updated_at`). So it *was* revised — two days after publication. "has not been revised since it was published on 2026-07-23" collapses a revision timestamp into a publication date and then asserts the absence of the revision it is actually reading.

The analytical point the entry builds on this (the statement predates the 29–30 July publication event) survives either way; the stated fact does not. The correct rendering is: first published 21 July, last revised 23 July, unchanged since.

**F2 — "No ransom was paid" is not in the cited source; The Record reports only the UK's standing policy.**
Entry: `entries/2026-07-31/exfilsquad-uk-department-for-education-pnld-breach.md`

Body, first paragraph, whose only citation is `([The Record, 2026-07-30](https://therecord.media/united-kingdom-ransomware-education))`:
> "The NCSC has confirmed it is supporting law enforcement colleagues on the response. **No ransom was paid**, consistent with the UK's standing position for the public sector."

I fetched the page twice, the second time asking for every sentence mentioning ransom payment. The page carries exactly three:
> "The breach was claimed by extortionists calling themselves ExfilSquad who are demanding a ransom in exchange for not releasing the information."
> "As a matter of policy, the British government does not make ransom payments."
> "Although it is not yet law, last year the government moved forward with plans to suffocate the ransomware industry by making it illegal for public sector entities and organizations working within critical national infrastructure to make a payment in response to ransomware attacks."

The article states a **policy**; it never states that no payment was made in this incident, and it explicitly notes the prohibition is "not yet law". The entry converts a standing policy into a reported fact of the case. On an entry whose entire defender takeaway is a discipline about not treating unconfirmed assertions as findings, this is the wrong direction to round.

### Unsupported / hallucinated facts

**F3 — The OctLurk/SilkLurk title, summary and defender takeaway attribute the disk-serial key derivation to *both* families; SilkLurk's loader keys off the computer name.**
Entry: `entries/2026-07-31/octlurk-silklurk-service-dll-plugin-backdoors-government.md`

Title: `"OctLurk and SilkLurk — plugin backdoors whose **loaders** derive half their decryption key from the victim's own **disk serial**, deployed against Central Asian and Syrian government bodies"`
Summary: `"...a malicious loader DLL, which decrypts its payload using two keys — one hard-coded, one derived from the victim machine's C: drive serial number — so each victim's loader is undecodable anywhere else."`
Body: `"Two keys are involved: one is baked into the binary, and the second is derived at runtime from the serial number of the victim's C: drive."`

I pulled the full Securelist page text (`tools/fetch_source.py url https://securelist.com/octlurk-silklurk-backdoors-central-asia/120840/`). The two loaders use **different** machine identifiers:

*OctLurk loader* section, verbatim:
> "The double-XOR decryption uses two distinct multibyte keys: Key 1: hard-coded in the loader Key 2: derived from the serial number of the C: drive"

*SilkLurk loader* section, verbatim:
> "The ServiceProc then calls the routine s_1800078F0_decrypt_and_run_payload. This routine **computes a 32-bit hash (dword) of the victim's computer name.** The dword hash is used by a custom algorithm made up of arithmetic and logical operations to decrypt the hardcoded payload file path."

Kaspersky's own generalisation is the weaker one the entry quotes in `evidence[]`: "use information from the victim's machine to decrypt the payload" — it never says both use the disk serial.

This is not cosmetic, because the entry turns the wrong generalisation into IR guidance:
> "**Defender takeaway:** ... If an incident on a government network turns up a loader of this shape, retrieving the payload requires the volume serial from the specific infected host, so preserving the disk image — not just the extracted binary — is what makes downstream analysis possible at all."

For a SilkLurk loader the analyst needs the **computer name**, which is recoverable from almost any triage artefact and does not require a disk image at all. The deployment chain in the summary has the same problem — the `ServiceMain`-repointing chain (service `NgcCIntSvc`, `ServiceMain` → `RegisterService` in the loader DLL) is OctLurk's; SilkLurk creates service `RmSs` that runs a legitimate binary which side-loads the malicious DLL.

**F4 — The run record's iteration-1 finding asserts the Anthropic report names no independent third-party reviewer. It names one.**
File: `runs/2026-07-31/2026-07-31T0409Z-intel.md`, `verification.iterations[1].findings[]`, code F5:
> "The remediation list did not match the source: it split one item into two, dropped another, and added a third-party review of the incident that the source does not describe — **the only third party named is the evaluation partner running its own investigation, an involved party rather than an independent reviewer.**"

The source says otherwise, verbatim from `https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals` (fetched via the bridge this iteration):
> "We are also in dialogue with **METR, an independent AI evaluation organization, to conduct a third-party review, including access to all transcripts and sampling access to the relevant models.** In the meantime, within the next week, we will release a lightly redacted transcript in which Claude built a malicious PyPI package."

The iteration-1 finding was factually wrong, and the run record publishes the wrong statement as a verified finding. (The remediation it drove is F5 below.)

### Needs more research

**F5 — The Anthropic entry, as remediated, omits the independent third-party review and the transcript-release commitment.**
Entry: `entries/2026-07-31/anthropic-cyber-eval-environment-escape-pypi-package.md`

Current text:
> "Its stated remediation is to expand continuous monitoring of evaluation transcripts for unexpected behaviour, improve its investigation tooling, and conduct more rigorous assurance work with the vendors it relies on; its evaluation partner is separately running its own investigation."

Those three commitments are verbatim-faithful to the report's "How we're responding" close ("expanding our continuous monitoring of evaluation transcripts for unexpected behavior, improving our investigation tooling, and conducting more rigorous assurance work with the vendors we rely on") — but the sentence's second clause now reads as if the only outside look at this incident is by the involved evaluation partner. The report separately commits to (a) the METR independent third-party review with access to *all* transcripts and sampling access to the models, and (b) publishing a lightly redacted transcript of the PyPI incident within a week.

On the one entry in this run about this pipeline's own model vendor, where the run record explicitly promises the disclosure is "reported exactly as the source states it", dropping the independent-review commitment is the wrong omission in either direction: it is the single most decision-relevant line for a reader weighing how much to trust a self-disclosure, and it was removed by a remediation resting on the false premise in F4. Restore both commitments (naming METR and the transcript release), and drop the "involved party rather than independent reviewer" framing from the run record.

**F6 — The Rails entry tells the reader no proof-of-concept is public; Rapid7, a cited source, says public exploit code already exists.**
Entry: `entries/2026-07-31/cve-2026-66066-rails-activestorage-libvips-file-read.md`

Summary: `"No exploitation is reported and the discoverers are withholding the chain until 2026-08-28, while warning that the patch diffs make reconstruction fast."`
Body: `"No in-the-wild exploitation was reported as of 2026-07-30, and both reporting teams — Ethiack and GMO Flatt Security, who found it independently — are withholding proof-of-concept code and the full chain until no later than 2026-08-28."`

Rapid7 (`https://www.rapid7.com/blog/post/etr-kindarails2shell-cve-2026-66066-...`), which the entry cites as a `role: primary` source, carries both halves of the exploitation picture. I re-fetched it asking for verbatim sentences:
> "As of July 30, 2026, Rapid7 is not aware of exploitation in the wild."
> "**Public code claiming to exploit CVE-2026-66066 exists, but it is unclear how closely it corresponds to the full attack chain reported privately to Rails.**"

The entry takes the first sentence and pairs it with the (true, separately-sourced) fact that the *discoverers* are withholding their PoC. The composite reads as "nothing public exists yet", which is the opposite of what the cited page says and materially changes the urgency an operator assigns to a pre-auth arbitrary-file-read on a default Rails configuration. One clause carrying Rapid7's hedged wording fixes it.

### Editorial / less-is-more flags (advisory)

**F7 — Unit 42 n8n enumeration figure understated.** Entry: `unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055.md` — "against n8n it **enumerated tens of thousands of instances**, sampled about a hundred, probed roughly forty, found three candidates". Unit 42 verbatim: "FOFA confirmed n8n as a high-value target: 647,017 instances globally; 25,209 in China." "Tens of thousands" is defensible against the China slice (the autonomous campaigns "targeted Chinese domestic infrastructure indiscriminately", per the same report), so this is not a truth defect — but the entry's own defender takeaway leans on n8n being "exactly the kind of self-hosted workflow and AI-orchestration software that spreads through research and public-sector environments without going through an asset inventory", and the source's global figure is an order of magnitude larger. Main agent may leave.

**F8 — "never executed" is firmer than the source.** Same entry: "a cloned PAN-OS exploit was non-functional and never executed". Unit 42 verbatim: "The cloned code is non-functional with placeholder values that cannot achieve code execution. **No evidence of modification or execution was found.**" "No evidence of execution" is not "never executed". Small, and the non-functionality claim is fully supported. Main agent may leave.

**F9 — Denominator qualifier dropped from the 141,006 figure.** Entry: `anthropic-cyber-eval-environment-escape-pypi-package.md` — "The scale of the review matters for calibrating the finding. Anthropic examined 141,006 cybersecurity-evaluation runs". Source verbatim: "After reviewing 141,006 evaluation runs **where Claude could have obtained internet access**, we identified three incidents". Since the entry uses the number explicitly to calibrate, the qualifier is load-bearing: the reviewed population was the internet-reachable subset, not all cyber-eval runs.

### What I checked and found clean

Recorded so the main agent does not re-litigate settled ground:

- **Every cited URL resolves to a specific article/advisory.** 26/26. No 404, no homepage, no listing index, no NVD/MITRE per-CVE page as a source. `inside-it.ch` returns HTTP 403 to both the bridge and the reader (the run record documents this transport failure honestly); it is a block, not a dead URL, and I did not treat it as F1.
- **Per-clause attribution.** Swept every inline citation against the clause it terminates. The deliberate splits hold: the Gridbox three-fix-attempt narrative sits on mySites.guru and the release/verification clauses on Balbooa (verified — Balbooa's page carries "Prior to the public release of Gridbox 2.20.2, the updated build was provided to the reporting researcher for independent verification", "If you added custom .htaccess rules ... to block the recent attacks on Gridbox endpoints, remove them", and "Given the recent increase in automated attacks"); the Analog Devices thread splits correctly three ways (delisting → BleepingComputer "While the reason for this is unknown, it is common for threat actors to delist companies when ransom negotiations begin"; intrusion and materiality → the 8-K Item 8.01 text verbatim; the record count as the group's allegation → CyberInsider's "The group alleges it stole approximately 570,000 customer records"); the NetScaler CVE record splits correctly from the Unit 42 campaign narrative.
- **Version and identifier precision in the four vulnerability entries.** CVE-2026-3055 affected/fixed ranges match the NetScaler CNA record exactly (`14.1 <66.59`, `13.1 <62.23`, `13.1 FIPS and NDcPP <37.262`) — iteration 1's off-by-one correction is right, with no regression. EPSS 0.78 matches the FIRST API (`0.783370000`, date 2026-07-30). CVSS 9.8 is NVD's v3.1 primary and is what Unit 42 states (the CNA's own CVSS 4.0 is 9.3; the entry's sourcing_note does not claim the score came from the CVE record, so this is not a defect). CVE-2026-65884 = 10.0 / `exploitMaturity: ATTACKED` / `providerUrgency: Red` / affected `1.0.0-2.20.1`, and CVE-2026-65885 = 9.4 with the same metrics — both verified against the Joomla CNA records, including the CISA ADP SSVC `"Exploitation":"none"` contradiction the entry's sourcing_note surfaces. CVE-2026-42897 = MSRC baseScore 8.1, `"exploited":"Yes"`, `"latestSoftwareRelease":"Exploitation Detected"`, vector `CVSS:3.1/.../E:F/RL:O/RC:C` (the "functional-exploit temporal metric" the sourcing_note claims), KEV `dateAdded 2026-05-15` — all correct. Rails fixed versions and the libvips 8.13 floor match the advisory.
- **Attacker claims vs confirmed facts.** The Stadler, ExfilSquad, Brinks Home and Everest material keeps attacker assertions attributed throughout, in `headline` and `summary` as well as the body. TechNadu's two evidence quotes are verbatim and contiguous; TechNadu's own "if validated" hedge is preserved; the four named rail operators are never asserted. The Brinks Home entry correctly reports BleepingComputer's two unreconciled Salesforce counts (4.9 M in the lede, 1.1 M in the body) without adopting either.
- **The Health-ISAC attribution correction is right.** A full-text check of the advisory confirms it names no victim organisation at all; BleepingComputer states "BleepingComputer is aware of recent ShinyHunters attacks at healthcare and medtech companies, including Medtronic, DentaQuest, iRhythm, and OneMedical" — its own prior reporting, exactly as the entry attributes it.
- **All 21 `evidence[]` quotes** checked as contiguous verbatim substrings of a page I fetched, including the German Stadler quote and the Exchange blog's italicised "Installing the July 2026 update _does not_ automatically remove already applied CVE-2026-42897 mitigations."
- **The 16-nation advisory date (2026-07-23)** is correct: AA26-204A is day-of-year 204 of 2026 = 23 July, and the CISA page confirms the identifier and subject.
- **Prior coverage / update targets.** `update_of` targets verified against `prior_coverage.json`: the Elastic entry correctly points at `2026-07-30/hugging-face-openai-artifactory-zero-day-escape-vector` and its "tracked since 2026-07-21" claim matches the earliest record (`2026-07-21/hugging-face-autonomous-ai-agent-production-breach`); Gridbox → `2026-07-26/joomla-gridbox-cookie-forged-super-user-auth-bypass-wave`; Stadler → `2026-07-22/...`; Health-ISAC → `2026-07-18/abbott-exact-sciences-shinyhunters-entra-sso-vishing`. The two deliberate non-update decisions the gate flagged are correctly reasoned. No recycled coverage shipped as new.
- **Relevance, priority, deep dive.** No entry fails the gate. Both out-of-nexus malware entries name their transferable ground in the body's own words ("The victimology is out of scope for this constituency; the loader design and the plugin architecture are the reason the entry is here"; "places the targeting outside this constituency; three deliberate design decisions in the malware are what transfer"), and the Anthropic entry clears on global-significance plus a named transferable control (independently tested egress containment). The absence of any `critical` is right: the Exchange CVE is a two-month-old KEV item with a mid-July patch, so the delta is attribution and remediation mechanics, not an hour-scale action. The deep dive earns its length — every section carries source-backed mechanics, not narrative padding.
- **`techniques[]`, `actions[]`, classification, style.** No empty `techniques[]` on any threat/incident/vulnerability entry; every mapped id has a matching described behaviour, and the Elastic set matches Elastic's own ATT&CK links one for one. Seven entries carry `actions: []` correctly; the four that carry actions have 1–2 each, all concrete and derived from the finding's own mechanics — no F18. Every entry carries a `classification` block in vocabulary, no `org_triage`, no `watchlist_hit: true`, no `watchlist` tag. Zero IOCs (the Gridbox account-naming pattern and the Kaspersky C2/file-path artefacts are correctly generalised or omitted). No workflow-internal language in any entry or in the run-record notes.
- **Coverage completeness.** No gap I can name a plausible in-window source for. The eight logged borderline drops each carry a defensible reason, the coverage-gap list accounts for the quiet sources, and the run's sweep across the window (two national-CERT-carried critical disclosures, an actively-exploited state-actor campaign, a confirmed-exploited extension flaw, three first-party malware/campaign analyses, four incidents) leaves no obvious pivot unworked. Coverage looks complete.

### Verdict

NEEDS_FIXES (truth: 4, editorial: 2, advisory: 3)

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: incidents
  item: "2026-07-31/everest-publishes-stadler-rail-supplier-archive"
  url_or_quote: "https://www.stadlerrail.com/en/media/media-releases/cybervorfall — entry: \"which its content-management metadata shows has not been revised since it was published on 2026-07-23\""
  summary: "The release's visible dateline is 21.07.2026 and its Storyblok record carries first_published_at 2026-07-21T07:57:43Z and content date 2026-07-21; published_at/updated_at 2026-07-23T07:35:27Z is a REVISION two days after publication. Citation date is two days off the source's own dateline (F3 under check 2e), and the 'unrevised since publication' claim is contradicted by the same metadata. Fix sources[1].date to 2026-07-21, and reword summary + body to 'first published 21 July, last revised 23 July, unchanged since'. The run record's verification note ('confirmed unrevised since 23 July against its content-management timestamps') needs the same correction."
- code: F3
  category: claim-not-supported
  section: incidents
  item: "2026-07-31/exfilsquad-uk-department-for-education-pnld-breach"
  url_or_quote: "https://therecord.media/united-kingdom-ransomware-education — entry: \"No ransom was paid, consistent with the UK's standing position for the public sector.\""
  summary: "The Record states only policy, never a fact of this case: 'As a matter of policy, the British government does not make ransom payments' and 'Although it is not yet law, last year the government moved forward with plans ... making it illegal for public sector entities ... to make a payment'. It also reports the extortionists 'are demanding a ransom'. Reword to the policy statement the source carries, or drop the clause."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "2026-07-31/octlurk-silklurk-service-dll-plugin-backdoors-government"
  url_or_quote: "title: \"OctLurk and SilkLurk — plugin backdoors whose loaders derive half their decryption key from the victim's own disk serial\""
  summary: "Securelist assigns the C: drive serial to the OctLurk loader only ('Key 2: derived from the serial number of the C: drive'); the SilkLurk loader 'computes a 32-bit hash (dword) of the victim's computer name'. Title, summary and body generalise the disk-serial derivation to both families, and the Defender takeaway turns it into IR guidance ('retrieving the payload requires the volume serial from the specific infected host, so preserving the disk image ... is what makes downstream analysis possible at all') that is wrong for SilkLurk. The summary's ServiceMain-repointing chain is likewise OctLurk-specific (service NgcCIntSvc); SilkLurk creates service RmSs and side-loads via a legitimate binary. Scope the key-derivation and deployment claims per family."
- code: F4
  category: hallucinated-fact
  section: run-record
  item: "runs/2026-07-31/2026-07-31T0409Z-intel.md — verification.iterations[1].findings[] code F5"
  url_or_quote: "\"the only third party named is the evaluation partner running its own investigation, an involved party rather than an independent reviewer\""
  summary: "False. The Anthropic report states: 'We are also in dialogue with METR, an independent AI evaluation organization, to conduct a third-party review, including access to all transcripts and sampling access to the relevant models.' The iteration-1 finding recorded in the run record is wrong and drove the remediation flagged in the next finding. Correct or annotate the logged finding."
- code: F8
  category: needs-more-research
  section: incidents
  item: "2026-07-31/anthropic-cyber-eval-environment-escape-pypi-package"
  url_or_quote: "\"Its stated remediation is to expand continuous monitoring ... ; its evaluation partner is separately running its own investigation.\""
  summary: "The three commitments quoted are verbatim-faithful to the report's closing paragraph, but the entry drops two source-stated accountability commitments: the METR independent third-party review with access to all transcripts and sampling access to the models, and the release of a lightly redacted transcript of the PyPI incident 'within the next week'. On the entry about this pipeline's own model vendor, where the run record promises the disclosure is reported exactly as stated, the independent-review commitment is the most decision-relevant line for a reader weighing a self-disclosure. It was removed by the remediation built on the false premise in the preceding finding. Restore both, naming METR."
- code: F8
  category: needs-more-research
  section: trending-vulnerabilities
  item: "2026-07-31/cve-2026-66066-rails-activestorage-libvips-file-read"
  url_or_quote: "https://www.rapid7.com/blog/post/etr-kindarails2shell-cve-2026-66066-critical-arbitrary-file-read-and-possible-remote-code-execution-in-ruby-on-rails"
  summary: "Rapid7, cited as role: primary, states verbatim: 'Public code claiming to exploit CVE-2026-66066 exists, but it is unclear how closely it corresponds to the full attack chain reported privately to Rails.' The entry carries only the companion sentence ('As of July 30, 2026, Rapid7 is not aware of exploitation in the wild') and pairs it with the discoverers withholding their own PoC, so summary and body together tell the reader nothing public exists. Add Rapid7's hedged clause — it changes the urgency on a pre-auth arbitrary-file-read in a default Rails configuration."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "2026-07-31/unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055"
  url_or_quote: "\"against n8n it enumerated tens of thousands of instances\""
  summary: "Unit 42 verbatim: 'FOFA confirmed n8n as a high-value target: 647,017 instances globally; 25,209 in China.' Defensible against the China slice given the report says the autonomous campaigns 'targeted Chinese domestic infrastructure indiscriminately', so not a truth defect — but the entry's own defender takeaway leans on n8n's spread through research and public-sector environments, and the global figure is an order of magnitude larger. Advisory; main agent may leave."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "2026-07-31/unit42-autonomous-deepseek-hermes-netscaler-cve-2026-3055"
  url_or_quote: "\"a cloned PAN-OS exploit was non-functional and never executed\""
  summary: "Unit 42 verbatim: 'The cloned code is non-functional with placeholder values that cannot achieve code execution. No evidence of modification or execution was found.' 'No evidence of execution' is firmer than 'never executed'. The non-functionality half is fully supported. Advisory; main agent may leave."
- code: F11
  category: editorial-advisory
  section: incidents
  item: "2026-07-31/anthropic-cyber-eval-environment-escape-pypi-package"
  url_or_quote: "\"Anthropic examined 141,006 cybersecurity-evaluation runs\""
  summary: "Source verbatim: 'After reviewing 141,006 evaluation runs where Claude could have obtained internet access, we identified three incidents'. The entry drops the qualifier while explicitly using the figure to calibrate scale ('The scale of the review matters for calibrating the finding'), so the denominator reads as all cyber-eval runs rather than the internet-reachable subset. Advisory."
```
