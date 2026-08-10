**Model:** Opus 5 (`claude-opus-5`)
**Timestamps:** started_at=2026-08-10T05:07:25Z · ended_at=2026-08-10T05:33:02Z · duration_seconds=1537
**Self-telemetry:** urls_checked=44 · webfetch_calls=0 · bridge_fetches=52 · websearch_calls=1

## Verification report — 2026-08-10T0411Z-intel (iteration 1)

Cold read, no prior-iteration deltas. All 40 distinct cited URLs were fetched in this iteration through
`tools/fetch_source.py` (`url`, with `jina` escalation for lore.kernel.org, which serves an Anubis
anti-bot challenge to the direct transport, and `jina … html` for the four Wazuh GHSA pages, the
WordPress GHSA and the two coding-agent GHSAs, whose markdown render drops the sidebar carrying the
CVE ID, severity and version ranges). Every one of the 40 resolved to a specific advisory / article /
commit / release note — **no broken URLs (F1) and no generic/oversight URLs (F2)**. Structured records were additionally pulled for ground truth:
MSRC per-CVE JSON and the 2026-Apr and 2026-Jul CVRF, BSI CSAF WID-SEC-2026-2699, the CISA KEV
catalogue, FIRST EPSS, NVD, OSV, and the GitHub commit API for the Linux fix.

All 34 `evidence[]` quotes were re-checked independently as contiguous substrings after stripping
markup with empty-string replacement. **All 34 verify**, including the four the run record says it
repaired: both Nextgov quotes (present verbatim modulo curly-vs-straight apostrophes), the hedged
Forescout "Although we cannot confirm these particular assets were compromised in this campaign, they
had some interesting characteristics", the 19-of-22 carrier sentence, the four Wazuh advisory quotes
and the three Rapid7 quotes. The quote-fidelity remediation held. Two evidence records nonetheless
carry a wrong *publisher* / wrong inline citation (F3 below) — the strings are genuine, the attribution
is not.

Answers to the four questions the spawn message asked me to press on are in the § Judgements section
at the end.

### Citation does not support the claim

**F3-a — coding-agent-ci-harness-trust-boundary-shared-checkout: CVE-2026-54316 is bound to a different vulnerability.**
The entry says: *"The Anthropic Claude Code Action flaw is CVE-2026-54316, published 2026-06-13 and fixed
in claude-code 2.1.163 ([Anthropic, 2026-06-13](https://github.com/anthropics/claude-code/security/advisories/GHSA-fg94-h982-f3mm))"*
and then supplies its mechanics: *"The Claude Code bypass turned on an ordering mistake in defensive
code: the command-injection validation pipeline strips single-quoted content before inspecting a
command"* and *"The second bypass was an asymmetry in the allowlist itself, where commands classed as
read-only were exempted from path checking"*.
That advisory describes something else entirely — its description reads *"Because the hostname
huggingface.co was pre-approved as a bare hostname for the WebFetch tool, any path on that domain—
including attacker-co[ntrolled]…"*, weakness CWE-183 Permissive List of Allowed Inputs, severity
Moderate 6.0, affected `>= 0.2.54, < 2.1.163`, patched 2.1.163, CVE ID CVE-2026-54316.
Novee's own write-up separates them: *"Three rounds of patch-and-bypass … Three vulnerabilities, three
bounties, and CVE-2026-54316 at the final round"*, and it describes that final round as *"a full API
key walks out through a read-only GET. Reported, fixed, bounty awarded, CVE assigned. The fix was the
obvious right one: huggingface.co is no longer a bare hostname, it's scoped to a docs path"*.
So rounds 1 and 2 — the two mechanisms the entry actually explains — carry **no** CVE. The entry's
whole framing ("Two of the three are history … carry CVEs") understates how much of this research has
no identifier at all, which cuts against its own thesis rather than for it.
*Fix:* attribute CVE-2026-54316 to the huggingface.co WebFetch allowlist round and say the
quote-stripping and read-only-path bypasses were patched without identifiers.

**F3-b — interlock-volatility3-winpmem-credential-theft: Patient Zero was protected.**
Entry: *"and notes that the first compromised host turned out not to be running endpoint protection at
all."* Sophos says the opposite: *"The customer's environment comprises both Sophos-managed servers and
(at the time) Defender-managed endpoints, though it was discovered that not all endpoints were in fact
running protection of any sort. **Patient Zero was a Defender-managed endpoint running Windows 10.**"*
The unprotected-endpoint observation is about the estate, not about the compromised host.
*Fix:* delete the clause or restate it as an estate-level finding.

**F3-c — natjack-nat-trust-assumption-attack-class-two-cves: the Linux fix is explicitly incomplete, and the entry says patching closes the path.**
Entry body: *"A defender who patches to close both CVEs has addressed one of four primitives on two of
many affected implementations"*; rendered action item: *"…patching closes the two CVE'd TCP-hijack paths
but the other three primitives have no fix."*
natjack.io, cited in the same paragraph: *"CVE-2026-63913: Linux Kernel Netfilter (fixing a code flaw
and applying a mitigation for the downstream spoofing attack) applied in Linux kernel 7.1 and higher.
**This is not a complete fix but does increase attack complexity.**"* Its timeline repeats it: *"June 19,
2026: Linux Kernel commits a mitigation for the downstream spoofing attack on behalf of Microsoft for
Azure AKS. This is not a complete fix but does significantly increase attack complexity."*
This is the load-bearing operational sentence of the entry and it is in `actions[]`, so it renders into
the brief's aggregated task list.
*Fix:* describe the Linux change as a partial mitigation that raises attack complexity.

**F3-d — natjack-…: the ephemeral-port-range claim is the researcher's rebuttal, attributed to Microsoft.**
Entry: *"though Microsoft's own characterisation of the proof of concept used in vendor engagement notes
it can cover the entire ephemeral port range in seconds."*
natjack.io: *"July 14, 2026: Microsoft releases a WinNAT patch … and publishes CVE-2026-56181 as moderate
severity with no payment. Microsoft states the moderate severity rating is because \"the attack depends
on ephemeral port allocations\" **(the PoC, however, can target the entire ephemeral port range in a
matter of seconds)**."* The parenthetical is the researcher pushing back on Microsoft's rating; Microsoft's
own characterisation was the mitigating one. The string "ephemeral" does not occur in the MSRC record at all.
*Fix:* attribute to the researcher and, if kept, frame it as a rebuttal of the moderate rating.

**F3-e — zabka-supplier-account-jira-access-confirmed: the "Zgadujemy" quote is cited to the wrong outlet.**
Entry: *"the outlet's own words are \"Zgadujemy, że atakujący wykorzystał umieszczone w JIRZE informacje
takie jak tokeny/hasła/konta testowe aby dostać się do kolejnych systemów\" … ([Sekurak, 2026-08-03](https://sekurak.pl/potencjalny-wyciek-danych-z-zabki/))"*.
The substring `Zgaduj` occurs in the Niebezpiecznik page and in neither the Sekurak nor the RMF FM page.
The entry's own `evidence[]` record attributes the same quote to Niebezpiecznik, so frontmatter and body
disagree. Since the whole entry is built on keeping the outlet's guess separate from the victim's
confirmation, the attribution has to be exact.
*Fix:* re-point the inline citation to the Niebezpiecznik URL.

**F3-f — linux-bridge-stp-timer-uaf-no-cve-public-exploit: a commit-message sentence attributed to the advisory.**
Entry: *"The advisory identifies the specific omission — \"This check is missing from
br_topology_change_detection() and it is possible to engineer a situation in which the topology change
timer is armed while the bridge is administratively down, resulting in a use-after-free\""*, and the
matching `evidence[]` record carries `publisher: "SSD Secure Disclosure"`.
`br_topology_change_detection` does not appear in the SSD advisory at all — its Root Cause / Vulnerability
Analysis sections name `br_stp_enable_bridge()`, `br_port_state_selection()`, `br_stp_disable_bridge()`,
`br_dev_stop()` and `br_dev_delete()`. The quoted sentence is verbatim from the upstream commit message
at https://github.com/torvalds/linux/commit/2a00517db8de.
*Fix:* change the `evidence[]` publisher to the Linux kernel commit and re-word "The advisory identifies"
to "The upstream fix commit identifies".

**F3-g — linux-bridge-…: the upstream commit is dated 36 days late.**
`sources[]` carries `{url: https://github.com/torvalds/linux/commit/2a00517db8de, publisher: "Linux kernel",
date: "2026-08-05"}` and the body cites it as *"([Linux kernel, 2026-08-05])"*. The GitHub commit API for
`2a00517db8de4be7df3d483b215c5544fb30a191` returns author date `2026-06-29T07:21:17Z` and committer date
`2026-06-30T13:14:35Z`; the commit's own Link trailer is `patch.msgid.link/20260629072117…`. Far past the
one-day rendering tolerance. This also matters editorially: the entry tells readers *"the fix commit
carries no stable-tree marking, so whether any given distribution kernel has taken it could not be
established this run"* — true, but a fix that has been in mainline since 30 June is a materially different
backport question from one landed the same day as the advisory.
*Fix:* date the source 2026-06-30 and carry the six-week gap into the backport paragraph.

**F3-h — freebsd-ctl-ha-…(DEEP DIVE): "March 2017" is not in the source it is cited to.**
Entry: *"the feature plus the manpage text describing it date back at least to March 2017 ([Calif,
2026-08-06](https://blog.calif.io/p/the-taking-of-freebsd-one-two-three))"*. The Calif post contains no
occurrence of "2017". The fact sits on the other cited source: the FreeBSD commit diff changes
`-.Dd March 29, 2017` to `+.Dd August 4, 2026`.
*Fix:* attach https://cgit.freebsd.org/src/commit/?id=3c8f8432 to that clause.

**F3-i — coding-agent-…: CVE-2026-12537 is attributed to an advisory that says "No known CVE".**
Entry: *"the Google flaw is CVE-2026-12537, published 2026-04-24 and fixed in gemini-cli 0.39.1 and
run-gemini-cli 0.1.22 ([Google, 2026-04-24](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g))"*.
That advisory's CVE ID field reads **"No known CVE"**, and neither the identifier nor the string `0.1.22`
appears anywhere on the page (its own metadata is affected `< 0.39.1` / `< 0.40.0-preview.3`, patched
`0.39.1` / `0.40.0-preview.3`, severity Critical 10.0, published Apr 24 2026).
The mapping is nonetheless correct and verifiable elsewhere: OSV returns
`{"id":"GHSA-wpqr-6v78-jr5g", "aliases":["CVE-2026-12537"]}` with ranges `@google/gemini-cli < 0.39.1` and
`google-github-actions/run-gemini-cli < 0.1.22`, and the CVE record itself is published 2026-06-24.
*Fix:* cite OSV (or the CVE record) for the identifier and the run-gemini-cli boundary, or attribute them
to OSV in the prose.

### Unsupported / hallucinated facts

**F4-a — wazuh-4-14-6-…: CVE-2026-45798's affected range is widened past the vendor advisory.**
Frontmatter: `- id: CVE-2026-45798 … affected: ">= 4.0.0, <= 4.14.5"`. The owning advisory
(GHSA-4fvp-jfc3-qr6r) states `Affected versions >= 4.5.0` / `Patched versions 4.14.6`, and its body is
more cautious again: *"Verified affected: `wazuh-manager` 5.0.0-beta1 (ASan witness against this build) …
the reachability path was not separately verified for 4.x in this submission. The Wazuh security team is
best-positioned to determine the affected range across maintained branches."*
The other three CVE records check out against their own advisory sidebars — CVE-2026-49441 `>= 4.3.0`,
Critical 9.1; CVE-2026-48024 `>= 4.0.0`, Critical 9.1; CVE-2026-44901 `>= 4.0.0`, High 8.4 — and BSI's
CSAF for WID-SEC-2026-2699 lists exactly ten identifiers including all four. The per-CVE provenance work
this run describes is sound; only this one range is wrong.
*Fix:* `affected: ">= 4.5.0, <= 4.14.5"`, and soften the summary's blanket *"Affected from 4.0.0 through
4.14.5"*.

**F4-b — natjack-…: the sourcing note asserts an absence that is not one.**
`sourcing_note:` *"No CVSS is asserted because neither vendor record supplied one this run."* Microsoft's
record for CVE-2026-56181 supplies `baseScore: "8.3"` with
`CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H` — from the same structured API the run record's own
`bridge_uses` block says carried *"the CWE, CVSS, affected-product range and mitigation text for
CVE-2026-33824 and CVE-2026-56181"*. The co-cited Synack page also states *"Severity Range CVSS 7.2 to 9.6"*.
*Fix:* populate `cvss` for CVE-2026-56181 or rewrite the note to explain why the vendor score was not carried.

**F4-c — run record: the action-item count is wrong.**
*"Action-item discipline: 7 action items across 17 entries, with 12 entries carrying none."* Seven entries
carry exactly one action each (coding-agent-ci-harness, rapid7-metasploit, freebsd-ctl-ha, natjack, wazuh,
wordpress-xss2shell, wp2root); 17 − 7 = **10** carry none.
*Fix:* "with 10 entries carrying none".

### Claims missing inline citation

**F5-a — wp2root-…: the KEV listing, the EPSS score and the CVSS have no source in the entry.**
Body: *"CVE-2026-31431 has been on CISA's Known Exploited Vulnerabilities catalogue since 2026-05-01 for
confirmed in-the-wild exploitation, entirely independent of this chain-building exercise, and EPSS scores
it 0.999."* Frontmatter: `cvss: "7.8"`, `epss: "0.999"`, `status: [exploited, cisa-kev, …]`. The action item
repeats it: *"it is KEV-listed, EPSS 0.999"*.
The Calif post contains no occurrence of "CVE", "CISA", "KEV" or "EPSS"; copy.fail contains no "KEV",
"Known Exploited", "EPSS" or CVSS score. Every one of the three facts is **true** — KEV `dateAdded
2026-05-01`; EPSS `0.99907` as of 2026-08-09; NVD baseScore 7.8 — they are simply uncited, and the entry
explicitly presents the KEV status as the new fact *"that neither the original coverage nor the queue note
carried"*, which is exactly the kind of claim that must carry its own link.
*Fix:* cite the KEV/CVE record on that sentence. This also repairs the `sourcing_note`, whose
credibility-1 rationale currently rests on *"independently catalogued by CISA as exploited"* — a
corroboration the entry never cites.

**F5-b — linux-bridge-…: the entire CAP_NET_ADMIN / user-namespace precondition is uncited.**
Summary: *"The precondition is CAP_NET_ADMIN over a bridge device — not network-reachable and not
available to a plain unprivileged process, but obtainable on hosts that permit unprivileged
user-namespace creation."* Body: *"driving the sequence requires CAP_NET_ADMIN over a bridge device,
exercised through netlink link-management operations"*, *"any host permitting unprivileged user-namespace
creation, which hands a plain local user that capability inside a namespace of their own making"*, and
*"That last case is a widely enabled default, and it is why the disclosing competition classified this in
the Linux privilege-escalation category at all."*
Neither `NET_ADMIN` nor `namespace` occurs in the SSD advisory or on the commit page. This paragraph sets
the entry's priority, scopes its risk, and drives the Defender takeaway (*"restricting unprivileged
user-namespace creation is the control that actually removes the reachable path"*). The trailing causal
claim also goes beyond the advisory, which says only *"won second place in the Linux PE category"*.
*Fix:* cite the precondition, or mark it explicitly as the entry's own inference from the exploit's
netlink operations.

**F5-c — forescout-…: the CVE-2017-16740 description has no source.**
Entry: *"referring to CVE-2017-16740, a stack-based buffer overflow in MicroLogix 1400 Series B and C
firmware 21.002 and earlier"*. Forescout names the CVE and nothing else — *"The most prevalent
vulnerability we observed was CVE-2017-16740"* and *"Exploitation would require Modbus TCP to be enabled,
which was not confirmed"*. The strings "stack", "buffer overflow", "Series B" and "21.002" do not occur on
the page. (Everything else in this entry verifies: the 4,407 count, *"The vast majority (65%) are located
in the U.S., followed by Canada (12%) and Spain (3%)"*, the 19-of-22 carrier finding, the separate
*"Approximately 86% (19 of 22) hosts observed in the affected cities were susceptible to this CVE based on
firmware versions"*, *"There is no confirmation of any CVE exploited in this campaign"*, and both CISA
quotes from acting director Nick Andersen.)
*Fix:* cite the Rockwell PSIRT / ICS advisory for the class and firmware boundary, or drop the description.

### Quantifier without source

**F14-a — natjack-…: "four primitives" where the source enumerates five.**
Summary: *"Four primitives are described"*; body: *"vulnerable to at least one of its four primitives"*,
*"the DNS hijack, the port disclosure and the table-exhaustion denial of service have no CVE"*.
natjack.io's "What attacks are possible?" section carries five separately-headed vulnerabilities, each with
its own Vulnerability Description: TCP Hijacking via Downstream Spoofing, **TCP Hijacking via Upstream
Spoofing**, UDP DNS Hijacking, Victim IP and Port Information Disclosure, Denial of Service. The entry
merges the upstream variant into the first ("A coordinated variant adds an attacker-controlled server
upstream") without saying the regrouping is its own.
*Fix:* use five, or state the four-way grouping as the entry's editorial choice.

**F14-b — natjack-…: "eight stable and long-term point releases".**
Entry: *"fixed in 7.1 and backported across eight stable and long-term point releases ([Linux kernel CVE
team, 2026-07-19])"*. The cited announcement lists eight "fixed in" lines **in total**, one of which is
mainline 7.1: 5.10.259, 5.15.210, 6.1.176, 6.6.143, 6.12.93, 6.18.35, 7.0.12, 7.1. That is **seven**
backports plus mainline.
*Fix:* "seven".

**F14-c — zabka-…: "four independent Polish outlets", and an unsourced superlative.**
Body: *"reproduced in near-identical wording across four of them"*; `sourcing_note`: *"reproduced in
near-identical form by four independent Polish outlets"*. The entry cites three (Niebezpiecznik, Sekurak,
RMF FM) and the run's own telemetry lists only those three in `sources_used` — cyberdefence24 was attempted
but not used. Separately, *"Żabka, Poland's largest convenience-store franchise chain"* is a superlative
none of the three cited pages carries (RMF FM says only *"sieć sklepów Żabka"*).
*Fix:* reduce to three or cite the fourth; source or drop the superlative.

### Classification missing / inconsistent

**F17-a — forescout-…: credibility 1 is not what the entry shows.**
`classification: {reliability: B, credibility: 1}`. The two primaries carry disjoint facts and corroborate
nothing: the census, geography and both 19-of-22 findings rest solely on Forescout; both CISA quotes rest
solely on Nextgov/FCW. The entry's own note concedes it — *"the figures are attributed to the parties that
produced them"*. The run applies credibility 2 elsewhere on exactly this reasoning (interlock: *"a single
originating assessor with two documents rather than independent corroboration"*; esxi: *"reproduction is not
corroboration, so credibility stays at 2"*).
*Fix:* credibility 2. (Every other classification block in the run checks out, including reliability A on
wazuh/wordpress/freebsd/moucka, where a vendor advisory, a project release, a project source commit and a
DOJ release respectively carry the letter.)

### Action-item discipline

**F18-a — cve-2026-66066-rapid7-…: the action duplicates both predecessor entries.**
`actions[]`: *"Confirm every Rails application accepting untrusted image uploads is on activestorage
7.2.3.2, 8.0.5.1 or 8.1.3.1 — a public Metasploit module now automates recovery of signing material, so
secret_key_base on any host that was exposed and unpatched should be treated as disclosed and rotated."*
2026-07-31/cve-2026-66066-rails-activestorage-libvips-file-read already carries *"Upgrade activestorage to
7.2.3.2, 8.0.5.1 or 8.1.3.1 AND confirm the host's libvips is >= 8.13…"*, and
2026-08-02/cve-2026-66066-rails-attack-chain-public-forensic-tooling already carries *"…rotate
secret_key_base, the master key and every credential reachable through credentials.yml.enc … because the
patch does not invalidate a secret that was already read."* The delta here (a public module now automates
the chain) raises urgency but changes no task.
*Fix:* drop the action — this update is informational — or replace it with a task the delta creates.
The other six actions are clean: each names a specific configuration surface, version boundary or
enumeration derived from its own finding, and 10 entries correctly carry none.

### Missed angles

**F10-a — Retelit (Italy) / Qilin: the run deferred the most constituency-relevant out-of-window item while publishing three others of the same vintage.**
The run record itself says: *"out-of-window: Retelit (Italy) Qilin compromise reportedly affecting 193
Italian public administrations and Leonardo — primary dated 2026-08-04, updated 2026-08-06 … This is
**relevant and uncovered**, and its absence from the store suggests three prior fires missed it rather than
dropped it."*
Confirmed live this iteration: IrpiMedia's 2026-08-04 investigation
(https://irpimedia.irpi.eu/retelit-operatore-cloud-e-telecomunicazioni-attacco-informatico/) reports ~300 GB
across ~270,000 files exfiltrated from Retelit, an Italian telecommunications and cloud operator whose
customers include Leonardo, three digital-identity providers and ~193 public administrations; compromise
apparently discovered early June 2026, Qilin's claim posted 2026-07-11 with sample files 2026-07-14, and no
company statement nearly two months on — against ACN/CSIRT-ITA's 2026-05-28 national warning on systematic
Qilin campaigns in Italy.
This is a European telco + public-administration + defence-supplier exposure — squarely the profiled
constituency — held back while NatJack, the Novee CI research and the Linux bridge UAF (all 2026-08-05/06,
all further from the constituency core) shipped under the recovered-coverage-gap rationale. The deferral
reason given (*"verify against Retelit's own statement before composing"*) is legitimate in itself, but the
Żabka entry in this very run demonstrates the discipline for exactly this situation: publish what the
victim confirms, attribute the leak-site/journalistic claims to their sources, and say plainly that no
company statement exists.
*Fix:* publish it under the same reasoning, or record in the run notes why this item alone was held.
Suggested query: `Retelit Qilin IrpiMedia 193 pubbliche amministrazioni Leonardo`.

### Judgements on the four questions raised in the spawn message

**1. The recency stretch (NatJack, Novee CI research, Linux bridge STP UAF at event_date 2026-08-06/05).**
The reasoning holds and I would not drop any of the three. Each is a first-time publication of material
verified absent from both the 14-day index and the registry (I re-confirmed: none of `trend:natjack-…`,
`trend:coding-agent-ci-harness-…` or the bridge UAF has prior coverage), each carries an honest
`event_date` outside the window rather than a laundered one, and the run record discloses the stretch and
invites the challenge. The alternative is not "publish it later" — it is "never publish it", because the
window has already passed over it twice. Under a completeness standard that treats a dropped relevant item
as seriously as an included marginal one, publishing is the correct call. Two caveats, neither fatal:
the coding-agent CI entry is the weakest of the three on constituency relevance (two of its three findings
are patched CVEs months old, which the entry states honestly, leaving one architectural lesson), and the
asymmetry with the deferred Retelit item is the real problem with the policy as applied — see F10-a. The
stretch itself is defensible; the selection within it is what I would question.

**2. Quote fidelity.** All 34 `evidence[]` quotes re-verify as contiguous substrings of pages I fetched in
this iteration, including all four the run says it repaired. Specifically: the Forescout hedge is intact
("Although we cannot confirm these particular assets were compromised in this campaign, they had some
interesting characteristics"), both Nextgov quotes are exact modulo curly-vs-straight apostrophes, the four
Wazuh advisory quotes match their own advisories, and the three Rapid7 quotes match (the Metasploit-module
sentence in the body, though not an `evidence[]` record, also verifies verbatim). The FreeBSD manpage quote
reconstructs exactly from the commit diff once the `+` diff prefixes and the `.Sy` roff macro are removed —
I do not treat that as a defect. Two *attribution* defects remain (F3-e Żabka, F3-f Linux bridge): the strings
are genuine, the publisher named is wrong.

**3. Per-fact attribution on the split-sourced entries.** The Moucka entry's discipline is right and I
verified the absences directly: "Snowflake", "multi-factor", "MFA", "Mandiant", "UNC5537", "Judische",
"Waifu" and "Wagenius" all return zero hits in the DOJ release, and every one of them is carried in the
entry as Krebs's. DOJ-attributed figures all check out ($9.5 million actual losses, "at least 100 million
individuals", four counts, sentencing 27 October, two-year mandatory minimum, February–October 2024, "26,
of Kitchener, Ontario"). The Żabka entry's separation of victim statement / seller claim / outlet guess is
likewise correct on substance — the 541,000-ticket and 89-repository figures are attributed to the forum
seller as both Polish outlets present them, and the Jira-to-production mechanism is carried as the outlet's
stated guess. Its only defect is which outlet gets the guess (F3-e).
One genuine attribution gap I did **not** find flagged anywhere: *"Mandiant tracks the cluster behind the
campaign as UNC5537"* appears in the summary and the body with no citation, and neither cited source
mentions Mandiant or UNC5537. I am deliberately **not** raising it as a separate numbered finding because
the same sentence is a store-level entity-linking convention (`entities: [actor:unc5537]`, a registry key
that already exists with aliases Judische/Waifu) rather than a claim the entry invented — but the main
agent should consider adding a Mandiant citation, since as written the entry names a vendor cluster
attribution that no source it cites supports.

**4. The Rapid7 reframing.** Correct, and I could not find a single sentence implying observed attacker
activity. The title says "public Metasploit module and a validated code-execution path"; the headline says
"and states it is not aware of exploitation in the wild"; the summary says "The status change is
weaponisation and automation, not attacker activity"; `status: [poc-public, patch-available]` with no
`exploited` and no `actively-exploited` tag. I independently re-confirmed the underlying claims: the ETR
post carries "As of July 30, 2026, Rapid7 is not aware of exploitation in the wild" and the string
"scanning" occurs in neither post; the technical post carries the reproduction sentence, the JSON-serializer
sentence and the module description verbatim, and links `github.com/rapid7/metasploit-framework/pull/21733`
with an `msf6 > use exploit/multi/http/rails_activestorage_vips_rce` console transcript, which supports
"released" and "public". CVSSv4 9.5 and the three fixed versions match the ETR post. `high` rather than
`critical` is right — nothing here is actively exploited or hour-critical — and the only problem with the
entry is its duplicated action (F18-a).

**5. CVE provenance (asked as question 5).** The four Wazuh identifiers are each correctly bound to their own
advisory — GHSA-3v57→CVE-2026-49441, GHSA-gh4h→CVE-2026-48024, GHSA-8c6v→CVE-2026-44901,
GHSA-4fvp→CVE-2026-45798 — with CVSS 9.1/9.1/8.4/7.5 matching each advisory's own vector string, and all ten
identifiers appear in BSI's CSAF record. No id is paired to the wrong flaw. The one defect is the widened
affected range on CVE-2026-45798 (F10). NatJack's two ids are correctly mapped per platform against the
researcher's explicit statement (*"CVE-2026-56181: Microsoft Windows NAT (affecting Hyper-V in a downstream
spoofing configuration)"* / *"CVE-2026-63913: Linux Kernel Netfilter"*), Microsoft's affected-product list
matches the July CVRF exactly (Windows Server 2025 + Windows 11 24H2/25H2/26H1), and the kernel CVE text
matches the lore announcement verbatim. The coding-agent entry is where CVE provenance breaks down (F3-a, F3-i).
CVE-2026-33824's CWE-415, CVSS 9.8, 2026-04-14 release, exploited=No, publiclyDisclosed=No and the
27-product affected range all match Microsoft's own records; CVE-2026-64638's 8.9 and its 24 branch ranges
(4.7.0–4.7.33 up to 7.0.0–7.0.2, patched from 4.7.34) match the WordPress advisory exactly.

**6. Priority calibration and actions.** Zero `critical` is right — nothing in this batch is
newly-disclosed-and-actively-exploited with an hour-scale clock. The six `high` entries all clear the
TL;DR bar (Wazuh: pre-auth reachable on a self-hosted public-sector SIEM; WordPress: pre-auth chain, Swiss
region; FreeBSD: pre-auth kernel RCE with public exploits and no patch coming; wp2root: a KEV-listed kernel
bug wired to a chain confirmed against Swiss sites; Rails: public module on a pre-auth flaw; Interlock:
a novel, transferable credential-access inversion). I found no under-prioritisation: the Linux bridge UAF
is the only plausible promotion candidate and its capability precondition justifies `notable`. Action
discipline is otherwise good — 7 concrete actions, 10 empty lists, no generic advice, no body restatement
— with the single exception at F18-a and the factual correction needed inside the NatJack action (F3-c).

**Other whole-run checks, all clean:** no IOCs in any entry (the only regex hits are version numbers); no
workflow-internal language in any entry body; English throughout; all 50 `techniques[]` ids resolve to
active, non-revoked techniques in the pinned ATT&CK v19.2 dataset, and T1685.006 "Clear Linux or Mac
System Logs" and the rejection of Group-IB's own T1564.013 ("Bind Mounts") are both correct; every entity
key referenced by every entry exists in the registry; all five `update_of` targets exist and each carries a
genuine delta (I read 2026-08-02/unit42-… and confirmed it records CVE-2026-33824 only as "reverse-shell
callbacks targeting three IKE VPN endpoints", exactly as the ikeext entry says); the deliberate
`actor:akira` shared-entity gate warning is correctly judged a non-update; no `org_triage` block, no
`watchlist_hit: true`, no `watchlist` tag anywhere.

### Verdict

NEEDS_FIXES (truth: 12, editorial: 9, advisory: 0)

Truth: 9 x F3 (citation-does-not-support: F3-a … F3-i) + 3 x F4 (unsupported fact: F4-a … F4-c).
Editorial: 3 x F5 (missing citation: F5-a … F5-c) + 3 x F14 (quantifier: F14-a … F14-c) + F17-a
(classification) + F18-a (action discipline) + F10-a (missed angle). Finding labels use the F-code of
their category with a letter suffix, matching the `code` field of each record in the machine-readable
block below.

Nothing here undermines the run's shape — the recency stretch is defensible, the quote-fidelity repair
held, the split-source attribution discipline is right in substance, the Rapid7 reframing is correct, and
the Wazuh and NatJack CVE-provenance work is sound. The defects cluster in three places: the coding-agent
CI entry's CVE bindings (F3-a, F3-i), the NatJack entry's treatment of the Linux patch and Microsoft's own
words (F3-c, F3-d, F4-b, F14-a), and the Linux bridge entry's source attribution and dates (F3-f, F3-g,
F5-b).

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable)
- code: F3
  category: claim-not-supported
  section: research
  item: "Coding-agent CI harnesses broke on the same trust boundary three different ways"
  url_or_quote: "\"The Anthropic Claude Code Action flaw is CVE-2026-54316, published 2026-06-13 and fixed in claude-code 2.1.163\" ... \"The Claude Code bypass turned on an ordering mistake in defensive code: the command-injection validation pipeline strips single-quoted content before inspecting a command\" / https://github.com/anthropics/claude-code/security/advisories/GHSA-fg94-h982-f3mm"
  summary: "The cited advisory assigns CVE-2026-54316 to a different vulnerability: 'Because the hostname huggingface.co was pre-approved as a bare hostname for the WebFetch tool, any path on that domain...' (CWE-183 Permissive List of Allowed Inputs, CVSS 6.0). Novee's own write-up says 'Three vulnerabilities, three bounties, and CVE-2026-54316 at the final round' and describes the CVE-bearing round as the huggingface.co allowlist exfiltration ('Reported, fixed, bounty awarded, CVE assigned. The fix was the obvious right one: huggingface.co is no longer a bare hostname'). The quote-stripping validator (round 1) and the read-only path exemption (round 2) carry NO CVE. Fix: state that Claude Code produced three vulnerabilities of which only the final round (the huggingface.co WebFetch allowlist bypass) carries CVE-2026-54316, and stop attributing rounds 1-2 mechanics to that identifier."
- code: F3
  category: claim-not-supported
  section: threat
  item: "Interlock ran Volatility3 and WinPmem against a live endpoint to harvest credentials"
  url_or_quote: "\"and notes that the first compromised host turned out not to be running endpoint protection at all\" / https://www.sophos.com/en-us/blog/2608-volatility-interlock/"
  summary: "Contradicted by the cited page, which says: 'The customer's environment comprises both Sophos-managed servers and (at the time) Defender-managed endpoints, though it was discovered that not all endpoints were in fact running protection of any sort. Patient Zero was a Defender-managed endpoint running Windows 10.' The unprotected-endpoints observation is about the estate generally; Patient Zero WAS protected. Fix: remove the clause or restate it as 'not all endpoints in the estate were running protection of any sort'."
- code: F3
  category: claim-not-supported
  section: research
  item: "NatJack — sharing a NAT table is a trust relationship nobody declared"
  url_or_quote: "actions[]: \"...patching closes the two CVE'd TCP-hijack paths but the other three primitives have no fix\" and body \"A defender who patches to close both CVEs has addressed one of four primitives\" / https://natjack.io/"
  summary: "natjack.io states the Linux fix is explicitly incomplete: 'CVE-2026-63913: Linux Kernel Netfilter (fixing a code flaw and applying a mitigation for the downstream spoofing attack) applied in Linux kernel 7.1 and higher. This is not a complete fix but does increase attack complexity.' Its timeline repeats it: 'Linux Kernel commits a mitigation for the downstream spoofing attack on behalf of Microsoft for Azure AKS. This is not a complete fix but does significantly increase attack complexity.' The entry (body AND the rendered action item) tells readers patching closes that path. Fix: say the Linux patch is a partial mitigation that raises attack complexity, not a fix."
- code: F3
  category: claim-not-supported
  section: research
  item: "NatJack — sharing a NAT table is a trust relationship nobody declared"
  url_or_quote: "\"though Microsoft's own characterisation of the proof of concept used in vendor engagement notes it can cover the entire ephemeral port range in seconds\" / https://natjack.io/"
  summary: "Attribution inverted. natjack.io's timeline reads: 'Microsoft states the moderate severity rating is because \"the attack depends on ephemeral port allocations\" (the PoC, however, can target the entire ephemeral port range in a matter of seconds).' The parenthetical is the RESEARCHER's rebuttal; Microsoft's characterisation was the opposite (a mitigating factor justifying a moderate rating). Fix: attribute the ephemeral-port-range-in-seconds claim to the researcher and, if kept, note it rebuts Microsoft's moderate rating."
- code: F3
  category: claim-not-supported
  section: incident
  item: "Zabka confirms an external service-provider account reached its ticketing system"
  url_or_quote: "\"the outlet's own words are \\\"Zgadujemy, ze atakujacy wykorzystal umieszczone w JIRZE informacje...\\\" ... ([Sekurak, 2026-08-03](https://sekurak.pl/potencjalny-wyciek-danych-z-zabki/))\""
  summary: "The quote is cited in the body to Sekurak but appears only in Niebezpiecznik (verified: the string 'Zgaduj' occurs in the Niebezpiecznik page and in neither Sekurak nor RMF FM). The entry's own evidence[] record correctly attributes it to Niebezpiecznik, so frontmatter and body disagree. Fix: re-point the inline citation to https://niebezpiecznik.pl/post/zabka-zhackowana-co-wycieklo/."
- code: F3
  category: claim-not-supported
  section: vulnerability
  item: "Linux kernel bridge STP timer use-after-free"
  url_or_quote: "\"The advisory identifies the specific omission — \\\"This check is missing from br_topology_change_detection() and it is possible to engineer a situation in which the topology change timer is armed while the bridge is administratively down, resulting in a use-after-free\\\"\" / evidence[] publisher: \"SSD Secure Disclosure\""
  summary: "That sentence is the upstream commit message, not the SSD advisory. The SSD advisory names br_stp_enable_bridge(), br_port_state_selection(), br_stp_disable_bridge(), br_dev_stop() and br_dev_delete() and never mentions br_topology_change_detection at all. The commit message at https://github.com/torvalds/linux/commit/2a00517db8de carries the quoted text verbatim. Fix: change the evidence[] publisher to the Linux kernel commit and re-word the body from 'The advisory identifies' to 'The upstream fix commit identifies'."
- code: F3
  category: claim-not-supported
  section: vulnerability
  item: "Linux kernel bridge STP timer use-after-free"
  url_or_quote: "sources[]: {url: \"https://github.com/torvalds/linux/commit/2a00517db8de\", publisher: \"Linux kernel\", date: \"2026-08-05\"} and body \"the upstream fix restores the missing guard ([Linux kernel, 2026-08-05])\""
  summary: "The commit is authored 2026-06-29T07:21:17Z and committed 2026-06-30T13:14:35Z (GitHub commit API for 2a00517db8de4be7df3d483b215c5544fb30a191; patch link is patch.msgid.link/20260629...). The cited date is 36 days late — well past the one-day rendering tolerance. Fix: set the source date to 2026-06-30 and note the fix landed in mainline six weeks before the advisory, which is materially useful for the backport question the entry raises."
- code: F3
  category: claim-not-supported
  section: vulnerability
  item: "FreeBSD CTL HA — three independent pre-authentication remote kernel-code-execution primitives (DEEP DIVE)"
  url_or_quote: "\"the feature plus the manpage text describing it date back at least to March 2017 ([Calif, 2026-08-06](https://blog.calif.io/p/the-taking-of-freebsd-one-two-three))\""
  summary: "The Calif post contains no occurrence of '2017' anywhere. The supporting fact is on the OTHER cited source: the FreeBSD commit diff shows the ctl.4 manpage date line changing '-.Dd March 29, 2017' to '+.Dd August 4, 2026'. Classic adjacency defect. Fix: attach the FreeBSD commit citation (https://cgit.freebsd.org/src/commit/?id=3c8f8432) to that clause."
- code: F3
  category: claim-not-supported
  section: research
  item: "Coding-agent CI harnesses broke on the same trust boundary three different ways"
  url_or_quote: "\"the Google flaw is CVE-2026-12537, published 2026-04-24 and fixed in gemini-cli 0.39.1 and run-gemini-cli 0.1.22 ([Google, 2026-04-24](https://github.com/google-github-actions/run-gemini-cli/security/advisories/GHSA-wpqr-6v78-jr5g))\""
  summary: "The cited GHSA's CVE ID field reads 'No known CVE' and its text never carries the identifier or the string 0.1.22. The mapping is real but lives elsewhere: OSV records GHSA-wpqr-6v78-jr5g with aliases ['CVE-2026-12537'] and ranges @google/gemini-cli < 0.39.1 and google-github-actions/run-gemini-cli < 0.1.22 (https://api.osv.dev/v1/vulns/GHSA-wpqr-6v78-jr5g). Fix: add the OSV/CVE record as a source for the identifier, or attribute the id to OSV rather than to the Google advisory."
- code: F4
  category: hallucinated-fact
  section: vulnerability
  item: "Wazuh 4.14.6 — two cluster-protocol paths to root, a DAPI deserialization RCE, and a pre-auth stack overflow"
  url_or_quote: "cves[] CVE-2026-45798: affected: \">= 4.0.0, <= 4.14.5\" / https://github.com/wazuh/wazuh/security/advisories/GHSA-4fvp-jfc3-qr6r"
  summary: "The owning advisory's own metadata reads 'Affected versions >= 4.5.0 / Patched versions 4.14.6', and its body is more cautious still: 'Verified affected: wazuh-manager 5.0.0-beta1 ... the reachability path was not separately verified for 4.x in this submission.' The entry widens the range to >= 4.0.0. (The other three records check out: 49441 >= 4.3.0 / 9.1, 48024 >= 4.0.0 / 9.1, 44901 >= 4.0.0 / 8.4, all patched 4.14.6; all four ids read off their own advisory sidebars and all ten appear in BSI's CSAF for WID-SEC-2026-2699.) Fix: set affected to '>= 4.5.0, <= 4.14.5' and soften the summary's blanket 'Affected from 4.0.0 through 4.14.5'."
- code: F4
  category: hallucinated-fact
  section: research
  item: "NatJack — sharing a NAT table is a trust relationship nobody declared"
  url_or_quote: "sourcing_note: \"No CVSS is asserted because neither vendor record supplied one this run.\""
  summary: "False, and contradicted by the run's own telemetry. The MSRC record for CVE-2026-56181 supplies baseScore 8.3 with vector CVSS:3.1/AV:A/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H (severity 'Moderate'), retrievable from the same structured API the run record's bridge_uses block says it used ('the structured API and CVRF records carried the CWE, CVSS, affected-product range and mitigation text for ... CVE-2026-56181'). The co-cited Synack page additionally states 'Severity Range CVSS 7.2 to 9.6'. Fix: either populate cvss for CVE-2026-56181 from Microsoft or rewrite the sourcing note to say why the vendor score was deliberately not carried."
- code: F4
  category: hallucinated-fact
  section: run-record
  item: "runs/2026-08-10/2026-08-10T0411Z-intel.md § Verification & coverage notes"
  url_or_quote: "\"Action-item discipline: 7 action items across 17 entries, with 12 entries carrying none.\""
  summary: "Ten entries carry no action, not twelve. Seven entries each carry exactly one action (coding-agent-ci-harness, rapid7-metasploit, freebsd-ctl-ha, natjack, wazuh, wordpress-xss2shell, wp2root); 17 - 7 = 10. Fix: change 'with 12 entries carrying none' to 'with 10 entries carrying none'."
- code: F5
  category: missing-citation
  section: vulnerability
  item: "UPDATE — wp2root turns the WP2Shell foothold into fileless native root"
  url_or_quote: "\"CVE-2026-31431 has been on CISA's Known Exploited Vulnerabilities catalogue since 2026-05-01 for confirmed in-the-wild exploitation ... and EPSS scores it 0.999.\" plus cves[] cvss: \"7.8\", epss: \"0.999\", status: [exploited, cisa-kev, ...]"
  summary: "Neither cited source supports any of it: the Calif wp2root post contains no occurrence of 'CVE', 'KEV', 'CISA' or 'EPSS'; copy.fail contains no 'KEV', 'Known Exploited', 'EPSS' or CVSS score. All three facts are TRUE (KEV dateAdded 2026-05-01 for CVE-2026-31431; EPSS 0.99907 as of 2026-08-09; NVD baseScore 7.8) — they are simply uncited, and the entry explicitly presents the KEV status as new information ('The fact that changes the risk calculation, and that neither the original coverage nor the queue note carried'). It is also the stated basis for the action item. Fix: add a KEV/CVE-record citation on that sentence; doing so also repairs the sourcing_note's credibility-1 rationale, which currently rests on an uncited CISA corroboration."
- code: F5
  category: missing-citation
  section: vulnerability
  item: "Linux kernel bridge STP timer use-after-free"
  url_or_quote: "\"driving the sequence requires CAP_NET_ADMIN over a bridge device, exercised through netlink link-management operations\" ... \"any host permitting unprivileged user-namespace creation, which hands a plain local user that capability inside a namespace of their own making\" (also asserted in summary and Defender takeaway)"
  summary: "Neither 'NET_ADMIN' nor 'namespace' appears anywhere in the SSD advisory or in the upstream commit page. The whole precondition paragraph — which sets the entry's priority, scopes its risk and drives the Defender takeaway ('restricting unprivileged user-namespace creation is the control that actually removes the reachable path') — is uncited. The trailing causal claim 'it is why the disclosing competition classified this in the Linux privilege-escalation category at all' also goes beyond the advisory, which says only 'won second place in the Linux PE category'. Fix: cite a source for the capability precondition or mark it explicitly as the entry's own inference."
- code: F5
  category: missing-citation
  section: threat
  item: "UPDATE — the water-campaign exposure gets counted"
  url_or_quote: "\"referring to CVE-2017-16740, a stack-based buffer overflow in MicroLogix 1400 Series B and C firmware 21.002 and earlier\""
  summary: "The Forescout post names the CVE and nothing more — the strings 'stack', 'buffer overflow', 'Series B' and '21.002' do not occur on the page (it says only 'The most prevalent vulnerability we observed was CVE-2017-16740' and 'Exploitation would require Modbus TCP to be enabled, which was not confirmed'). The vulnerability class and firmware boundary need their own citation (Rockwell PSIRT or the ICS advisory)."
- code: F14
  category: quantifier-without-source
  section: research
  item: "NatJack — sharing a NAT table is a trust relationship nobody declared"
  url_or_quote: "\"Four primitives are described\" / \"every evaluated NAT implementation vulnerable to at least one of its four primitives\" / \"the DNS hijack, the port disclosure and the table-exhaustion denial of service have no CVE\""
  summary: "natjack.io's 'What attacks are possible?' section enumerates FIVE named vulnerabilities, each with its own Vulnerability Description: TCP Hijacking via Downstream Spoofing, TCP Hijacking via Upstream Spoofing, UDP DNS Hijacking, Victim IP and Port Information Disclosure, Denial of Service. The entry silently merges upstream spoofing into the downstream primitive as 'a coordinated variant' and then counts to four throughout. Fix: use the source's count of five, or state explicitly that the four-way grouping is the entry's own."
- code: F14
  category: quantifier-without-source
  section: research
  item: "NatJack — sharing a NAT table is a trust relationship nobody declared"
  url_or_quote: "\"fixed in 7.1 and backported across eight stable and long-term point releases ([Linux kernel CVE team, 2026-07-19])\""
  summary: "The cited announcement lists eight 'fixed in' lines TOTAL, of which 7.1 is mainline: 5.10.259, 5.15.210, 6.1.176, 6.6.143, 6.12.93, 6.18.35, 7.0.12, and 7.1. That is seven stable/LTS point releases plus mainline, not 'eight ... point releases' in addition to 7.1. Fix: say seven."
- code: F14
  category: quantifier-without-source
  section: incident
  item: "Zabka confirms an external service-provider account reached its ticketing system"
  url_or_quote: "\"reproduced in near-identical wording across four of them\" and sourcing_note \"reproduced in near-identical form by four independent Polish outlets\"; also \"Zabka, Poland's largest convenience-store franchise chain\""
  summary: "The entry cites three outlets (Niebezpiecznik, Sekurak, RMF FM) and the run's own telemetry records only those three as used (cyberdefence24 was attempted but is not in sources_used), so the count of four is unverifiable from the entry's own citations. Separately, none of the three cited pages supports the superlative 'Poland's largest convenience-store franchise chain' (RMF FM says only 'siec sklepow Zabka'). Fix: reduce the count to three or cite the fourth outlet; drop or source the superlative."
- code: F17
  category: classification
  section: threat
  item: "UPDATE — the water-campaign exposure gets counted"
  url_or_quote: "classification: {reliability: B, credibility: 1}"
  summary: "Credibility 1 ('confirmed by other sources') is not what the entry shows. The two primaries carry disjoint facts and corroborate nothing: the 4,407-device census, the 65/12/3 geography, the 19-of-22 carrier finding and the 19-of-22 CVE-2017-16740 finding rest solely on Forescout; the two CISA quotes rest solely on Nextgov/FCW. The entry's own sourcing_note says as much ('the figures are attributed to the parties that produced them'). Compare the run's own convention on interlock and esxi, where a single assessor sets credibility 2. Fix: credibility 2."
- code: F18
  category: action-item-discipline
  section: vulnerability
  item: "UPDATE — CVE-2026-66066 (Rails Active Storage) now has a public Metasploit module"
  url_or_quote: "actions[]: \"Confirm every Rails application accepting untrusted image uploads is on activestorage 7.2.3.2, 8.0.5.1 or 8.1.3.1 — a public Metasploit module now automates recovery of signing material, so secret_key_base on any host that was exposed and unpatched should be treated as disclosed and rotated.\""
  summary: "Duplicates actions already carried by both in-window predecessor entries. 2026-07-31/cve-2026-66066-rails-activestorage-libvips-file-read already says 'Upgrade activestorage to 7.2.3.2, 8.0.5.1 or 8.1.3.1 ...' and 2026-08-02/cve-2026-66066-rails-attack-chain-public-forensic-tooling already says '... rotate secret_key_base, the master key and every credential reachable through credentials.yml.enc ... because the patch does not invalidate a secret that was already read.' This entry's delta (a public module now automates the chain) raises urgency but does not change the task. Fix: drop the action, or replace it with a task the delta actually creates."
- code: F10
  category: missed-angle
  section: coverage
  item: "Retelit (Italy) / Qilin — 300 GB exfiltrated, ~193 public administrations and Leonardo among affected customers"
  url_or_quote: "run record: \"out-of-window: Retelit (Italy) Qilin compromise reportedly affecting 193 Italian public administrations and Leonardo — primary dated 2026-08-04, updated 2026-08-06 ... This is relevant and uncovered\""
  summary: "The run published three items dated 2026-08-05/06 as 'recovered coverage gaps' while deferring to the backlog the one out-of-window item its own notes call 'relevant and uncovered' — and the deferred item is the most constituency-relevant of the four: a European telecommunications and cloud operator, Qilin extortion, with ~193 Italian public administrations, three digital-identity providers and Leonardo among its customers, against an ACN/CSIRT-ITA national Qilin warning. Confirmed live this run: IrpiMedia's investigation of 2026-08-04 (https://irpimedia.irpi.eu/retelit-operatore-cloud-e-telecomunicazioni-attacco-informatico/) reports ~300 GB across ~270,000 files, discovery in early June 2026, Qilin's claim on 2026-07-11 and sample publication on 2026-07-14, with no company statement. Fix: either publish it under the same recovered-gap reasoning, applying the seller-claim-versus-confirmed-fact discipline the Zabka entry demonstrates, or record in the run notes why this item alone was held while three others of the same vintage shipped. Suggested query: Retelit Qilin IrpiMedia 193 pubbliche amministrazioni Leonardo."
```
