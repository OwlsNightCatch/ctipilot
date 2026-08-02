**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-02T04:48:56Z · ended_at=2026-08-02T05:01:33Z · duration_seconds=757

## Verification report — 2026-08-02T0409Z-intel (iteration 1)

Cold read. All 10 inline source URLs across the four entries were fetched in this iteration
(direct `WebFetch` + `tools/fetch_source.py url`; the jina rung was not attempted — reader pool
confirmed exhausted). All 10 resolve, all 10 land on specific articles/advisories: no F1, no F2.
Every `evidence[]` quote was checked against the fetched page text and every one is a contiguous
verbatim substring. Dedup: `prior_coverage.json` (121 records) carries no Adform, COLDCARD/Coinkite,
clipper or CCI/chamber record, so the three `new` entries are correctly new; the Rails `update_of`
target exists and the delta is genuine. CISA KEV shows no in-window additions (latest 2026-07-29);
NCSC-CH security-hub's newest post is 2026-07-31T12:06Z, i.e. pre-window. Coverage looks complete
for this weekend window — no F10.

### Citation does not support the claim

**F1 — Adform entry: the vendor notice is credited with facts it does not contain.**
Body, first sentence: *"Adform, an advertising-technology platform headquartered in Copenhagen, has
confirmed that attackers modified `trackpoint-async.js`, the shared JavaScript tracking library it
serves from `s2.adform.net`, into a tool that rewrites cryptocurrency wallet addresses in the
visitor's browser."* — the sentence is uncited and the following sentence terminates the Adform
citation, so the claim reads as the vendor's own confirmation. Frontmatter `summary` repeats it:
*"Adform … confirmed that malicious code was appended to trackpoint-async.js — the tracking library
it serves from s2.adform.net and that customer sites embed across entire websites."*
I fetched `https://site.adform.com/resources/newsroom/security-incident-company-update/` in full.
The notice never uses the string `trackpoint-async.js`, never names `s2.adform.net`, never says
"appended", and never characterises customer deployment. Its technical content is limited to: "The
malicious code was designed to interfere with certain cryptocurrency transactions … by attempting to
replace a cryptocurrency wallet address copied to a user's clipboard", "the code was not designed to
install software … or establish persistence", the 27 July detection/containment, and the cache
advice. The asset identification belongs to the researcher and the press: BleepingComputer —
"Security researcher Kevin Beaumont discovered the malicious activity, saying that it stemmed from
'trackpoint-async.js,' Adform's JavaScript tracking script served from 's2.adform.net'"; The Hacker
News — "The compromised resource is trackpoint-async.js, served from s2.adform[.]net." THN also
qualifies the deployment claim the summary flattens: "Adform's implementation documentation says the
tracking code **can** run on one page, several sections, or unconditionally across an entire website."
Fix: keep "Adform confirmed a compromise of code it serves" attributed to Adform; attribute the file,
the host, the append-at-end-of-library detail and the site-wide deployment property to BC/THN.

**F2 — Rails entry: the released artifacts are "agent skills", not "scripts".**
Body: *"plus two scripts, one that works out whether an application was ever vulnerable and over what
period, and one that searches Active Storage data for the crafted files and reconstructs what was read
if it finds any"*. I read the cited thread through the Discourse topic JSON. The source says: "The
`kr2s-was-i-vulnerable` **agent skill** works out whether your application was ever vulnerable, and if
it was, over what period of time. The `kr2s-was-i-exploited` **agent skill** searches your Active
Storage data for the crafted files, and works out what was read if it finds any." The rest of the
entry's clause tracks the source almost word-for-word, which makes the substitution of "scripts" a
material misdescription of what the reader is being told to run — an agent skill is a set of
instructions for an AI coding agent, not an executable. `actions[]` inherits it ("Run the published
kr2s-was-i-vulnerable and kr2s-was-i-exploited checks"). Related and cheap to fix in the same edit:
the entry never names the repository the source identifies, `rails/rails-forensics-CVE-2026-66066`,
which is what would make the action self-contained.

### Unsupported / hallucinated facts

**F3 — CCI Nice entry: "with no vulnerability involved" is asserted, not sourced, and contradicts the
entry's own framing.**
Headline: *"A French public-law chamber of commerce confirms bulk candidate-data exports from a
hijacked admin account, with no vulnerability involved"*; body: *"no software flaw was exploited and no
tooling was deployed"*. Cyberattaque.org (fetched in full) says the opposite about what is known: "La
méthode ayant permis de prendre le contrôle du compte n'est pas précisée. Un mot de passe volé, une
campagne de phishing, la réutilisation d'identifiants ou le détournement d'une session peuvent conduire
à ce type de compromission." Session hijacking is itself frequently a software-flaw outcome, so the
negative cannot be inferred; FrenchBreaches adds nothing on the vector. The entry's own paragraph three
gets this right — "How the account was taken over is explicitly not stated" — so the headline and the
detection-paragraph clause are the outliers. Supported claim: the *post-authentication* activity used
the platform's own legitimate export functions; the takeover vector is undisclosed.

**F4 — Rails entry: the summary drops the libvips precondition and over-scopes the exposed population.**
Frontmatter `summary`: *"Any Rails application still on an unpatched activestorage that accepted image
uploads is now exposed to a fully public chain"*; the body's takeaway repeats the shape ("an application
that was internet-reachable and accepting image uploads during its vulnerable window is a key-rotation
candidate"). The cited GHSA-xr9x-r78c-5hrm (fetched) conditions the flaw on the variant processor:
affected applications are those that use "libvips for Active Storage image processing … 
`config.active_storage.variant_processor = :vips`" *and* accept untrusted image uploads. This entry's
own predecessor (2026-07-31) carried the precondition explicitly and recorded Ethiack's statement that
ImageMagick-configured applications are "outside this vector entirely". As written, the update tells
ImageMagick shops to treat themselves as key-rotation candidates. Fix: restore the libvips qualifier
in the summary (and in the takeaway sentence).

**F5 — COLDCARD entry: `techniques: [T1552.004, …]` maps a behaviour the entry does not describe.**
T1552.004 (Unsecured Credentials: Private Keys) covers an adversary searching a compromised system for
insecurely stored private-key material. Nothing in this entry describes host access: the mechanism, per
cited Block Engineering, is offline reconstruction of a deterministic PRNG stream — "An attacker who
can determine or sufficiently constrain the device UID, timer state and RNG-call history can reproduce
the fallback stream offline. A wallet xpub, address or generated public key provides a
candidate-validation oracle" — plus, per CryptoTimes, on-chain sweeping. T1110 (Brute Force, active in
the pinned dataset) is the behaviour the body actually describes; T1657 is correct as-is and the entry
would still satisfy the non-empty-`techniques[]` rule with T1657 + T1110.

### Quantifier without source

**F6 — COLDCARD entry: "the largest disclosed hardware-random-number-generator compromise on record".**
First body paragraph, no citation attached. I read all three cited sources this iteration: Coinkite's
backgrounder makes no comparative claim of any kind; Block Engineering's advisory makes none (and
explicitly limits itself — "This analysis is the opinion of Block, and based on our internal research");
CryptoTimes reports only the Galaxy figures (1,367.05 BTC / $88.6M / 4,585 addresses / third wave) with
no superlative. A keyword sweep over the fetched source text for "largest"/"biggest"/"unprecedented"
returns only a Bitcoin glossary blurb and a headline about the *largest wallets* being hit first. This
is load-bearing rather than decorative: the superlative is one of the two legs on which the entry's
opening paragraph — and the run record's borderline-include argument — justifies carrying an
out-of-nexus consumer-device story. Either attribute it or re-ground the inclusion on what is sourced
(confirmed, still-escalating mass exploitation with a firm figure, plus the transferable
firmware-assurance lesson, which is genuinely strong on its own).

### Editorial / less-is-more flags (advisory)

**F7 — Adform `actions[]` scoping window contradicts the entry's own posture.** The action says "for any
that carried it between 2026-07-26 and 2026-07-27", while the body says defenders "should not resolve
them in Adform's favour by default" and the run record says "a defender sizing exposure should assume
the longer window until the company reconciles the two." A team working the aggregated § Action Items
list without reading the body under-scopes its search. Consider the researcher's ~1-week window with the
2026-07-26 23:29 GMT archived sample as the documented floor.

**F8 — Run-record notes leak a sub-agent identifier.** "S3 confirmed the boundary by reading publication
timestamps directly on two candidates rather than trusting date-only summaries." Published prose should
not carry workflow-internal labels; the same fact reads fine in the passive.

**F9 — Run-record notes invoke a carve-out that does not exist.** "The Rails update rests on the
framework's own security team announcing a change to its own advisory — the first-party carve-out."
`prompts/verification.md` defines exactly two carve-outs (national-CERT, victim-own-disclosure), and the
entry's own `sourcing_note` says so correctly: "This is a first-party maintainer statement rather than
one of the named carve-outs, so it is graded single-source." Align the run record to the entry.

**F10 — Registry summary asserts an exploitation start date.**
`incident:coldcard-rng-fallback-seed-theft-2026` carries "Exploitation began 2026-07-30". No cited
source dates the start; Block published on 2026-07-30 "because active exploitation is under way" and
root-caused it "Following reports from COLDCARD users", which places thefts earlier. Suggest
"confirmed under way by 2026-07-30".

### What I checked and found clean (so the next iteration need not redo it)

- **URLs (10/10 fetched, live, specific):** discuss.rubyonrails.org/t/…/91441; github.com/rails/rails
  GHSA-xr9x-r78c-5hrm; site.adform.com/…/security-incident-company-update/;
  thehackernews.com/2026/08/hackers-poison-adform-script-to-swap.html;
  bleepingcomputer.com/…/online-ad-firm-adforms-script-compromised-to-steal-cryptocurrency/;
  cyberattaque.org/cci-nice-…/; frenchbreaches.com/alertes/…-ms9972qijqoesdq8cu;
  blog.coinkite.com/entropy-technical-backgrounder/;
  cryptotimes.io/2026/08/02/coldcard-hack-tops-88-6m-…/;
  engineering.block.xyz/blog/predictable-rng-fallback-and-32-bit-reseed-in-coldcard-firmware.
- **Every `evidence[]` quote** (10 across four entries) is a contiguous verbatim substring of the page
  cited, including both French quotes and the three Coinkite quotes.
- **Adform contradictions (main-agent focus 1):** both are stated accurately and neither is silently
  resolved. Duration — Adform's "may have affected individuals who visited a website using the affected
  Adform technology on 27 July 2026" vs Beaumont's week vs BC's "oldest sample … Archive.org snapshot on
  July 26, taken at 23:29:03 GMT" vs THN's "The public timeline is unresolved." all verified verbatim.
  Egress — Adform's "no evidence … Technical analysis indicates that such transmission may have been
  possible" vs THN's "The first payload's request is built to send a page hostname and path to the
  outside server; whether it reached the operator is not established by the sample" — the entry's hedge
  matches THN's exactly. (Optional, not a finding: BC additionally reports Beaumont observing *other*
  Adform-hosted scripts sending "the victim's IP address, referring website, and URL path", which cuts
  harder against Adform's denial; the entry's narrower framing is defensible because BC attributes it to
  other scripts, not the analysed sample.)
- **COLDCARD AI framing (focus 2):** correct and carefully hedged — "we have to assume that someone used
  AI to review previous versions of our firmware and stumbled upon this issue" and "it did not find this
  bug or anything serious" are both verbatim, the headline says "the vendor assumes", and the body closes
  with "No source establishes how the flaw was actually found." No F13.
- **CCI grading (focus 3):** `verification: single-source` + a `sourcing_note` naming the shared
  underlying notification is correct — both trackers reproduce the chamber's notification (FrenchBreaches
  independently fetched; same 18 July date, same field list). Classification C/2 fits. No F12. The
  undisclosed vector is stated as missing in the body (the headline is the exception — F3 above).
- **Rails update (focus 4):** genuine delta (embargo abandoned, forensics repo, in-window Discourse
  reply); no recap beyond one deliberate "nothing changed" version sentence. The Discourse paragraph is
  handled correctly: samsaffron's 2026-08-01 reply says verbatim "We have also noticed an increase in
  this style of attack at Discourse. We use ImageMagick at the moment with a list of allowed coders, but
  are porting over to vips", the Landlock description matches ("stop running image processing libraries
  in processes that have high levels of permission"; "it only needs to write to 1 spot not have global
  write to the entire filesystem"), and the entry's distinction between the attack *class* and this CVE
  is exactly what the source supports.
- **Priority (focus 5):** calibrated. Rails `high` (public chain + PoC on a CVSS 9.5 pre-auth read in a
  default configuration, patch out, no confirmed ITW) and Adform `high` (EU supplier compromise reaching
  any constituent's public site visitors) both clear the TL;DR bar without clearing the critical bar;
  COLDCARD and CCI `notable` are right. No `critical` is correct — nothing here is hour-scale.
- **Completeness (focus 6):** I agree with both drops. EU AI Act Art. 50 is real and in-window but
  carries no detect/hunt/block action — weekly policy lens is right. The CEN/CENELEC extortion claim is
  leak-site-only with no victim statement — the fake-news gate applies. No missed angle found: KEV has no
  in-window additions, NCSC-CH's newest post predates the window, and every THN "top stories" item
  (SharePoint CVE-2026-50522, Certighost, fastjson, GitLab, Hermes/Thai finance ministry) is already in
  prior coverage.
- **Frontmatter hygiene:** no `watchlist_hit: true`, no `watchlist` tag, `org_triage: null` everywhere
  (no scheme configured) — no F16. All four `classification` blocks present and in-vocabulary; A/2, A/1,
  C/2, A/1 are each consistent with the sourcing shown — no F17. No IOCs (the THN IP and the attacker
  addresses were correctly withheld), no vanity metrics beyond the Adform footprint figures, which are
  quoted with THN's own "describe the platform, not this incident" caveat. All `techniques[]` ids are
  active in the pinned dataset (F5 is a semantic mismatch, not a validity problem).

### Verdict

NEEDS_FIXES (truth: 6, editorial: 0, advisory: 4)

### Findings summary (machine-readable)

See `work/2026-08-02T0409Z-intel/verification.iter1.findings.yaml` (same payload, unfenced).
