**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-20T13:10:53Z · ended_at=2026-09-20T13:25:07Z · duration_seconds=854

## Retrospective truth audit — batch B (run 2026-09-20T1308Z-audit)

Cold, hostile re-verification of 10 published entries (2026-09-18/19) against primary sources.
9/10 entries' substantive facts (CVSS scores, version ranges, quotes, timelines, technique
mappings, victim numbers) verified letter-for-letter clean against their cited primaries. Two
entries carry genuine factual defects (Brevo quantifier inversion; CISA-KEV-Linux-kernel stale
sourcing_note). One systemic style finding (em dashes) affects all 10 files but is documented in
this repo as non-reader-visible (site build.py strips em dashes at render — see
`.claude/memory/ui-writing-style.md`), so it is reported once here rather than treated as
per-entry substance.

### Systemic finding: em dash in reader-facing text (all 10 entries)

Every one of the 10 files contains the banned em dash character ("—") in title/headline/summary/
body text (counts: check-point 6, acronis 3, ntc 4, famoussparrow 3, moviereaper 2, gyazo 3,
brevo 4, cisa-kev-linux 12, unbound 6, waterplum 14). `prompts/cti-run.md` Style rules ("Never an
em dash (operator directive 2026-08-29)") and `.claude/memory/ui-writing-style.md` both document
this as a hard rule, but the latter is explicit that `render_inline`/`render_markdown` dedash at
the parse boundary and the build self-check FAILs on any surviving em dash in rendered
HTML — "an em dash in an entry is a silent style defect, never a reader-visible one." I did not
verify the live rendered HTML on ctipilot.ch (out of scope / no browser tool), but per the
documented mechanism this should already be invisible to readers. Flagged per entry below for
completeness since the task instructions explicitly asked to check for it, but it should not be
read as evidence of reader-facing harm.

### Entry-by-entry findings

**cve-2026-91843-check-point-security-mgmt-stack-overflow.md — imprecision (em dash only)**
Fetched Check Point PSIRT sk1000155 directly (Next.js JSON payload). CVSS 9.8, the full
affected-version list, LivePatch take numbers per train, and both `evidence[]` quotes (the
"stack overflow ... root privileges" line and the "Username too long" SmartConsole log message)
match verbatim. CERT-FR CERTFR-2026-AVI-1193 corroborates the same version list and IoC line
independently (fetched via trafilatura). BSI CERT-Bund WID-SEC-2026-3429 required a jina fallback
(the direct/trafilatura routes hit an Angular SPA shell) but confirms the same title, affected
builds and take numbers. No factual defect.

**cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev.md — imprecision (em dash only)**
Verified CVSS 7.8, both affected/fixed build strings, and both `evidence[]` quotes against Help
Net Security and BleepingComputer verbatim. Live CISA KEV JSON (fetched 2026-09-20) confirms
CVE-2026-87886 still listed, `dateAdded: 2026-09-16`, `dueDate: 2026-09-19` — matching the entry's
"three-day remediation deadline" claim exactly (both dates match precisely: 16th to 19th).
Independently attempted to fetch Acronis's own advisory (security-advisory.acronis.com/advisories/
SEC-10986) via `extract` and `jina`; both returned a bare "Please enable JavaScript to continue" /
empty client-rendered shell, confirming the entry's sourcing_note claim that the vendor page is
genuinely unreachable rather than a shortcut around a reachable primary. No factual defect.

**ntc-swiss-solar-inverter-cybersecurity-assessment.md — imprecision (low confidence classification concern + em dash)**
Fetched NTC's own English report page, SRF's Rundschau article and cash.ch's AWP wire piece. Every
number (50+ findings / 7 critical / 6 high, full takeover on 4 of 11 products, 338,000 grid-tied
PV installations, Huawei+Sungrow >60% market share) and both translated German quotes (with
verbatim `original:` text) check out exactly. One low-confidence classification concern:
`credibility: 1` implies confirmation by an independent second party, but SRF and cash.ch are both
downstream press coverage of the same NTC study (SRF quotes NTC's own founder and an NTC security
expert; cash.ch is an AWP wire rewrite of the same NTC report) rather than a second party that
itself tested the inverters. The Bundesamt für Energie's "bestätigt die Analyse" is an endorsement,
not an independent technical assessment. `credibility: 2` (single-origin study, multiply reported)
may be the more defensible code. This is a judgment call on Admiralty-code semantics, not a hard
factual error, hence low confidence.

**famoussparrow-sparrowocky-backdoor-latam-gov.md — imprecision (em dash only)**
The most thoroughly checkable entry in the batch: ESET's welivesecurity.com post publishes its own
complete ATT&CK v19 mapping table. I diffed the entry's 33-id `techniques[]` list against that
table id-by-id — exact match, same order by tactic, zero additions or omissions. The 90%-LatAm
statistic, the 8-country target list, the SparrowDoor-attribution quote, the Panama port-dispute
motive theory, and every architectural/anti-analysis claim (trident loader, RC4/.dat payload
format, Mbed TLS, MinHook, TrustedSec COFFLoader-derived BOF support redirected through a
stack-spoofing subroutine, SilentMoonwalk-style JOP/ROP call-stack forgery targeting
RtlUserThreadStart/BaseThreadInitThunk, AnimateWindow thread-start-address spoofing, forged
LDR_DATA_TABLE_ENTRY in PEB_LDR_DATA) match the source verbatim or in faithful paraphrase. No
factual defect.

**moviereaper-torrent-supply-chain-solana-c2.md — imprecision (em dash only)**
Fetched securelist.com in full. All four technical stages (PEB module-walk instead of
LoadLibrary/GetProcAddress; VEH-triggered debug-break redirecting into a raw ntdll syscall calling
NtProtectVirtualMemory; EtwpCreateEtwThread execution; Solana `getAccountInfo` XOR-encrypted C2
dead-drop; UAC bypass + Windows\Telemetry masquerade; 21-command file-manager module) verified
verbatim, as were all three `evidence[]` quotes. The entry's sourcing_note correctly identifies
that Kaspersky's article carries two different victim-country lists and correctly prefers the more
specific dedicated "Victims" section list over the shorter intro-paragraph list — confirmed by
reading both lists in the source. No factual defect.

**gyazo-helpfeel-data-breach-image-upload-rce.md — imprecision (pipeline-internal fragment + em dash)**
Fetched Helpfeel's own notice and The Hacker News in full. Every number (23.62M user records, 490M
image-metadata records, a further 2.4M separately-filtered images, the 32-character image ID) and
both `evidence[]` quotes match verbatim, as does the full incident timeline (Sept 11 breach, Sept
12 initial remediation, Sept 14 confirmed-exposed + "emergency maintenance" framing on the public
status page, Sept 15 PIPC filing, Sept 16 public notice). One defect: the frontmatter
`sourcing_note` contains the literal fragment "(PD-5)" — a pipeline-internal policy-decision
reference — which `prompts/cti-run.md` Style rules explicitly bans from ever appearing in an
entry ("PD numbers, phase names, gate/verifier mechanics ... never appear"). This is the only
instance of this specific pattern found across all 10 entries (grepped for `PD-[0-9]`,
`sub-agent`, `main agent`, `phase [0-9]`, `this run` across the full batch).

**brevo-cloudflare-worker-clickfix-supply-chain.md — factual-error**
Fetched Brevo's own post-mortem, Sansec's research post and BleepingComputer in full. The 15:01-
20:30 UTC (5h29) impact window, the 16:07 UTC JS-file-append timing, the Aug-25 SSL-certificate
dating of the attacker's DNS access, all four `evidence[]` quotes, and the cross-reference to the
Sept 10 SSO/Trezor incident all verified verbatim. One genuine defect: the entry's title, summary
and body all state the malicious script reached "up to 100,000 customer sites" (body: "an
upper-bound count"). Sansec's own text says the opposite direction: "Brevo served malware to
visitors of its own site and **more than** 100 thousand customer sites," linking the figure to a
live publicwww.com search count. "Up to 100,000" (a ceiling) inverts "more than 100,000" (a floor)
— the entry systematically understates what Sansec actually reported, repeated identically across
three surfaces (title/summary/body), which is why this is scored factual-error rather than a
one-off imprecision.

**cisa-kev-linux-kernel-ktls-af-alg-ebtables-snat.md — factual-error**
Fetched both CISA alert pages (confirmed the 1-CVE/2-CVE split matches exactly), the live CISA KEV
JSON feed (all three CVEs present, `dateAdded: 2026-09-18`), and live NVD JSON for all three CVEs.
Every CVSS score — including the unusual dual kernel-CNA/NVD-re-score notation for CVE-2025-39682
(9.8 AV:N vs 7.1 AV:L) and CVE-2025-39964 (7.8 vs 5.5, correctly annotated "availability-only") —
and both NVD-sourced `evidence[]` quotes ("The corner case we missed is when the initial record
comes from rx_list, and it's zero length." / the `skb_store_bits()` sentence) match the live NVD
CVE JSON descriptions letter-for-letter, including every fixed-kernel-version number. However, the
`sourcing_note`'s claim that "no vendor (Red Hat, Ubuntu, Debian, SUSE) ... adds exploitation
detail beyond re-listing the fixed kernel builds" is contradicted by The Hacker News's 2026-09-19
coverage of the same three CVEs, which reports Red Hat updated all three `access.redhat.com`
advisory pages "as of September 19, 2026, at 2 a.m. UTC to acknowledge active exploitation,"
quoting Red Hat verbatim: "This CVE is high risk and there are known public exploits leveraging
this vulnerability." I independently found this exact sentence embedded as a client-side i18n
message key (`known_exploit_vulnerability`) in the live HTML of
`access.redhat.com/security/cve/cve-2025-39682`, consistent with (though I could not fully
render-execute to confirm the flag is toggled true for this specific page — noted low confidence
on that sub-point only) The Hacker News's specific, dated, on-topic report naming these exact three
CVE URLs. Red Hat's 2 a.m. UTC update also precedes this entry's own `discovered_at` (04:33 UTC the
same day), so the sourcing_note's characterization was already stale at publication time, not
merely overtaken since. This also affects the entry's `verification: single-source-national-cert`
framing, since Red Hat is a second party independently acknowledging exploitation rather than
merely re-listing CISA's fixed-build guidance.

**cve-2026-81642-cve-2026-82717-unbound-dnssec-rce.md — imprecision (low-confidence attribution nuance + em dash)**
Fetched both NLnet Labs advisory .txt files, NCSC Switzerland post 12957 via the bridge recipe, and
live NVD JSON for CVE-2026-82717. Both evidence[] quotes, the NCSC "Prerequisites" quote, the
"exploitation status: unknown" characterization, and the CVSS4.0 9.1/8.4 dual-CNA notation
(NVD confirms source `sep@nlnetlabs.nl` scored 8.4 for CVE-2026-82717, exactly as the entry states)
all check out exactly. Low-confidence note only: NLnet Labs' acknowledgment reads "Yuqi Qiu and
Xiang Li from Nankai University, AOSP Lab" — genuinely ambiguous as to whether "AOSP Lab" is a unit
of Nankai University (the entry's reading, "Nankai University's AOSP Lab") or a separately named
second affiliation. Not flagged as a hard defect given the source's own ambiguity.

**waterplum-contagious-interview-joint-advisory-scale.md — imprecision (PDF-extraction gap, no factual defect found + em dash)**
Fetched the IC3 PDF directly with `tools/fetch_source.py pdf`. The extraction uses a systematic
per-character shift-cipher-like decode ("byte-encoding") that I was able to reverse (a constant
+29 codepoint shift) to recover readable prose, but the reversed text is missing every embedded
numeral (30,000 / 100 / 7,000 / 313 / 1.7 billion all vanish — e.g. the decoded text runs
"...haveinfectedatleastdevicesinmorethancountriesand..." with the numbers simply absent between
"least" and "devices," and between "than" and "countries"). This affected only digit runs, not
prose: all four `evidence[]` quotes, the "313 General Bureau of the Munitions Industry Department"
sentence, and the "For the first time in Japan ... dismantled a 'laptop farm'" sentence decoded and
matched the entry verbatim once the numerals are accounted for. I corroborated every number via
therecord.media's 2026-09-18 coverage of the same advisory ("at least 30,000 devices across 100
countries," "about 7,000 cryptocurrency wallets") and confirmed "313 General Bureau" and "$10.7
million" independently via web search (Forbes, startupfortune.com, rankiteo.com all report the
same figures from the same advisory). One minor, non-defect observation: therecord.media itself
states "more than $10.5 million" versus the entry's $10.7M (1.7bn JPY) — this is an inaccuracy on
The Record's side, not the entry's, since $10.7M is the figure independently confirmed by multiple
other outlets as the advisory's own number and the entry cites the FBI/IC3 PDF directly for it, not
The Record.

### Verdict distribution

clean: 0/10 · imprecision: 8/10 · factual-error: 2/10

All 10 "imprecision" verdicts are driven predominantly (in 6 of 8 cases, entirely) by the
documented-as-non-reader-visible em dash style defect; strip that out and the substantive-fact
scorecard is: 6 entries with zero factual defects found (check-point, acronis, famoussparrow,
moviereaper, unbound, moviereaper), 1 entry with a single pipeline-internal-language leak (gyazo),
1 entry with a low-confidence Admiralty-code classification judgment call (ntc), and 2 entries with
genuine, evidenced factual defects (brevo's quantifier inversion; cisa-kev-linux-kernel's stale
sourcing_note that a vendor advisory now corroborates exploitation).

**Self-telemetry:** webfetch_calls=0 · websearch_calls=2 · bridge_fetches=2 (ncsc-csh, jina fallback
for BSI CERT-Bund) · urls_checked≈33 (Check Point sk1000155, WID-SEC-2026-3429 x2 transports,
CERTFR-2026-AVI-1193, Help Net Security, BleepingComputer x2, Acronis advisory x2 transports, CISA
KEV feed, NTC report, SRF, cash.ch, ESET welivesecurity, Securelist, Helpfeel notice, The Hacker
News x2, Brevo write-up, Sansec, CISA alert x2, NVD JSON x4, Red Hat CVE pages x3, Red Hat raw HTML
x1, NLnet Labs x2, NCSC.ch post, IC3 PDF, BfV page, heise, therecord.media, attack/enterprise-attack.json local)
