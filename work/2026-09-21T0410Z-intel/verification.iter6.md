**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-21T06:43:36Z · ended_at=2026-09-21T07:00:22Z · duration_seconds=1006

## Verification report — 2026-09-21T0410Z-intel (iteration 6)

Cold read of all 9 new entries, the run record, and re-fetch of every cited primary source (Talos, Kaspersky Securelist, SentinelLabs, Huntress ×2, Elastic Security Labs, detect.fyi, Clubic, Cyberattaque.org, FrenchBreaches). Walked the prior-iteration deltas (all 5 prior NEEDS_FIXES rounds) against the primaries myself rather than trusting the descriptions; all of them hold on a fresh read, including the conference-phishing entry's twice-revised structure (document/certificate/payload attribution and the macOS zsh/DMG swap), which I verified word-for-word against both the 2026-08-19 primary and the 2026-09-15 recap. New findings below were not raised in iterations 1-5.

### Unsupported / hallucinated facts

**#1 (moderate confidence).** `2026-09-21/afpa-third-party-accommodation-tool-data-extraction` — headline: "AFPA confirms a breach in a vendor-hosted tool after two criminal claims a day apart turn out to be the same incident." The entry's own body states the opposite: "AFPA has not confirmed the IDOR mechanism Cybernox claims, and has not stated whether the two claimed datasets overlap or were extracted from the same source — the two figures must not be summed." None of the three cited sources states the two claims are the same incident either — Clubic explicitly says "aucun élément public n'indique s'ils se recoupent" (no public element indicates whether they overlap), and Cyberattaque.org's own "Les deux revendications concernent-elles les mêmes données ?" section leaves it open. This is check-4b frontmatter-overstates-body: the headline asserts as resolved fact what the entry's own analysis and every cited source leave unresolved. Fix: reword the headline to not assert the two claims are confirmed as one incident (e.g., "...after two criminal claims a day apart point to the same third-party tool").

**#2 (low confidence).** `2026-09-21/ref9334-kremlin-chromium-secure-preferences-hmac-forge` — body: "The main C++ installer resolves NTDLL syscall numbers indirectly, by correlating export names against the .pdata exception-directory RUNTIME_FUNCTION table rather than parsing Nt*/Zw* stubs directly, evading userland EDR hooks." Fetched the Elastic source (`https://www.elastic.co/security-labs/threat-command/malicious-browser-extension-kremlin-banking-malware`): the "Indirect syscalls and SSN resolution from NTDLL" section describes exactly the correlation mechanism quoted, but never states the purpose is "evading userland EDR hooks" — that causal/purpose clause is the entry's own addition, not something this source says for this specific implementation.

**#3 (low confidence).** `2026-09-21/qilin-ai-generated-wiper-locker-scripts-forensic-markers` — frontmatter `affected_products: ["Veeam Backup & Replication"]`. The cited Talos source only ever calls the target "Veeam backups" — evidence quote #2 itself: "a Python script designed to stop, disable, and destroy Veeam backups" — and never names the specific product "Veeam Backup & Replication" (as opposed to Veeam's other products, e.g. Backup for Microsoft 365). The specific product name in `affected_products[]` is not stated by the source.

### Citation does not support the claim

**#4 (low confidence).** `2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft` — body: "...used NetExec plus RustHound (a Rust BloodHound collector) to enumerate Active Directory users, groups, computer accounts, administrative privileges and domain-trust relationships for attack-path analysis," stated as settled fact. Talos's own Phase 2 text (fetched from `blog.talosintelligence.com/ransomware-incidents-in-japan-in-the-first-half-of-2026/`) hedges this exact clause: "They may also have used RustHound/BloodHound-related tools to collect domain users, groups, computers, administrative privileges, and trust relationships..." The entry drops Talos's own "may have" hedge and presents an inferred activity as confirmed.

**#5 (low-moderate confidence).** `2026-09-21/afpa-third-party-accommodation-tool-data-extraction` — body: "...has not stated whether the two claimed datasets overlap or were extracted from the same source — the two figures must not be summed." This specific caution is FrenchBreaches' own statement ("Les deux chiffres ne doivent donc pas être additionnés pour annoncer plus de 2,7 millions de personnes touchées" — fetched from `frenchbreaches.com/alertes/afpa-mu4jbja3w3es4t7j0a8`), but the clause carries no citation at all, and sits between two Cyberattaque.org citations (before and after in the same paragraph) — Cyberattaque.org discusses the overlap question but never states the "must not be summed" caution itself. A citation to FrenchBreaches belongs on this clause.

**#6 (low confidence).** `2026-09-21/afpa-third-party-accommodation-tool-data-extraction` — body: "...while noting the schema's email-address fields were largely empty in the samples it observed ([Cyberattaque.org, 2026-09-15])." Cyberattaque.org's own text (fetched) says: "La structure comporte également des champs prévus pour des adresses e-mail, des seconds numéros de téléphone ou d'autres coordonnées. Dans les échantillons observés, plusieurs de ces champs sont cependant vides" — this states that several fields among *three* categories (email, second phone number, other contact info) were observed empty, without pinning the emptiness specifically to the email field. The entry's specific claim ("email-address fields... largely empty") narrows the source's more ambiguous, three-way statement.

### Claims missing inline citation

**#7.** `2026-09-21/afpa-third-party-accommodation-tool-data-extraction` — opening sentence: "AFPA (Agence nationale pour la formation des adultes), France's national public adult vocational-training agency **under the Ministry of Labour**..." None of the entry's three cited sources (Clubic, Cyberattaque.org, FrenchBreaches — all three fetched and checked) mentions a Ministry of Labour affiliation anywhere. The claim is true but appears in no linked source.

### Drop (low relevance / off-audience / duplicate)

**#8 (low confidence, residual note — not a new objection).** `2026-09-21/afpa-third-party-accommodation-tool-data-extraction` — the `sourcing_note`'s "primary-sector criterion, matched directly rather than by analogy" ground is a stretch: check 5's stricter out-of-nexus breach test lists four grounds (global significance, transferable TTP, actor plausibly targeting the constituency, imminent shared threat) and "primary-sector nexus for a foreign agency" is not literally one of them — AFPA is French, not Swiss, and the constituency is defined narrowly as Swiss public-sector. That said, the entry's *second*, independently-stated ground (scale of up to 1.7M people = global significance, plus a transferable third-party-vendor-trust lesson) is sufficient on its own to clear the bar, and this exact point was already raised and engaged with in iterations 1 and 2. Flagging only for completeness per the coverage obligation; no action needed beyond what's already been decided.

### Editorial / less-is-more flags (advisory)

**#9 — treat as a must-fix, not a leave-it advisory (this is a hard-invariant issue, not a style nit).** `2026-09-21/tradertraitor-terraform-lockfile-nostr-dead-drop` — body: "each carry a weaponized `.terraform.lock.hcl` pointing to an attacker-controlled custom Terraform provider registry (`registry.hashicorp-aws[.]com`, `registry.hashicorp-aws[.]io`, `registry.hashicorp-terraform[.]io`)." These are three literal attacker-controlled infrastructure domains (SentinelLabs' own IOC list), defanged with `[.]` notation, printed directly in entry prose. CLAUDE.md's hard rule is explicit: "NEVER put IOCs in an entry. No hashes, no IPs, **no attacker domains**, no YARA/Sigma/Suricata." `check_run.py`'s `_scan_iocs()` only pattern-matches hashes and routable IPv4 addresses — it does not scan for domain names — so this did not trip the mechanical gate and needs a manual fix (state the mechanism — "a custom, attacker-controlled Terraform provider registry" — without naming the specific malicious domains). Note: `api.nostr[.]watch` appearing in the same and a later paragraph is a *legitimate* public Nostr-relay directory the malware calls, not attacker infrastructure, so that one reference is fine as-is.

**#10 (advisory).** `2026-09-21/conference-phishing-rogue-root-ca-mitm-persistence` — body: "NetSupport carries the persistence for all three... a Winlogon modification and its own registered COM object" — a clearly described persistence behavior (COM object registration) with no corresponding id in `techniques[]`. `T1546.015` (Component Object Model Hijacking) is active/non-revoked in the pinned v19.2 dataset and fits.

**#11 (advisory).** `2026-09-21/the-gentlemen-open-directory-vhdx-backup-ntds-theft` — body: "...used NetExec and Impacket to attempt authentication against SMB, LDAP, RDP and **WinRM** across multiple hosts" — WinRM is explicitly named as an attempted lateral-movement authentication target, but `techniques[]` has no `T1021.006` (Windows Remote Management), which is active/non-revoked in the pinned dataset. `T1021.001` (RDP) and `T1021.002` (SMB) are mapped; WinRM is the one left out.

### Verdict

`NEEDS_FIXES (truth: 6, editorial: 2, advisory: 3)`

No F1/F2 (every cited URL resolved to a specific article/advisory and was fetched successfully this iteration — Talos, Securelist, SentinelLabs, Huntress ×2, Elastic, detect.fyi, Clubic, Cyberattaque.org, FrenchBreaches). No F6 (every entry's primary is a vendor research-lab post or a direct victim/AFP quotation via mainstream journalism; SAP entry correctly downgraded to reliability F with a disclosed single-blogger sourcing_note). No F9 surface contradictions beyond what's already disclosed (the REF9334 São Paulo-hours / late-night-hours split is correctly attributed to two different sections of the same source, not silently resolved). No F12 gaps (`verification`/`sourcing_note` correctly disclose single-source status on 8 of 9 entries; AFPA is correctly `multi-source`). No F16/F17 gaps found — `org_triage: null` and `watchlist_hit: false` on every entry, classification blocks present and internally consistent on all 9 (reliability letters checked against `sources/sources.json`: talos/kaspersky-securelist/sentinellabs/huntress/elastic-seclabs all registered B, matching; SAP's detect.fyi correctly F). No F18 (all `actions: []`, which is healthy per policy). No new F10 missed-angle found — I could not name a specific plausible in-window story the run's own telemetry or the dedup context surfaced that was dropped; the run record's borderline-drops and coverage-gaps sections are consistent with what I could verify.

Everything the prior five iterations fixed holds on this independent re-read, including the conference-phishing entry's certificate/document/payload attribution (Norwegian cert → ClickOnce Google-API-Connector path; Discord cert → second-document DocSend installer; Lenovo cert → third, on the rogue-CA payload) and the macOS zsh-vs-DMG payload swap (zsh path unconfirmed/redirect-loop; DMG path delivers the confirmed AMOS stealer + LaunchDaemon backdoor) — both checked against the 2026-08-19 primary directly, not just the recap.

### Findings summary (machine-readable)

```yaml
- code: F4
  category: hallucinated-fact
  section: entries
  item: "afpa-third-party-accommodation-tool-data-extraction"
  url_or_quote: "headline: \"AFPA confirms a breach in a vendor-hosted tool after two criminal claims a day apart turn out to be the same incident\""
  summary: "Body states the opposite (\"has not stated whether the two claimed datasets overlap\"); no cited source confirms the two claims are the same incident."
- code: F4
  category: hallucinated-fact
  section: entries
  item: "ref9334-kremlin-chromium-secure-preferences-hmac-forge"
  url_or_quote: "\"...rather than parsing Nt*/Zw* stubs directly, evading userland EDR hooks.\""
  summary: "(low confidence) Elastic's source describes the syscall-resolution mechanism but never states the EDR-hook-evasion purpose for this implementation."
- code: F4
  category: hallucinated-fact
  section: entries
  item: "qilin-ai-generated-wiper-locker-scripts-forensic-markers"
  url_or_quote: "affected_products: [\"Veeam Backup & Replication\"]"
  summary: "(low confidence) Talos's source only ever says \"Veeam backups\" generically; the specific product name is not stated."
- code: F3
  category: claim-not-supported
  section: entries
  item: "the-gentlemen-open-directory-vhdx-backup-ntds-theft"
  url_or_quote: "\"used NetExec plus RustHound... to enumerate Active Directory users, groups, computer accounts, administrative privileges and domain-trust relationships\""
  summary: "(low confidence) Talos hedges this as \"may also have used\"; the entry drops the hedge and states it as fact."
- code: F3
  category: claim-not-supported
  section: entries
  item: "afpa-third-party-accommodation-tool-data-extraction"
  url_or_quote: "\"the two figures must not be summed\""
  summary: "This caution is FrenchBreaches' own statement, uncited; sits between two Cyberattaque.org citations that don't state it."
- code: F3
  category: claim-not-supported
  section: entries
  item: "afpa-third-party-accommodation-tool-data-extraction"
  url_or_quote: "\"the schema's email-address fields were largely empty in the samples it observed\""
  summary: "(low confidence) Cyberattaque.org's text says several fields among email/second-phone/other-contact were empty, without pinning it specifically to email."
- code: F5
  category: missing-citation
  section: entries
  item: "afpa-third-party-accommodation-tool-data-extraction"
  url_or_quote: "\"France's national public adult vocational-training agency under the Ministry of Labour\""
  summary: "No cited source (Clubic, Cyberattaque.org, FrenchBreaches) mentions a Ministry of Labour affiliation."
- code: F7
  category: drop
  section: entries
  item: "afpa-third-party-accommodation-tool-data-extraction"
  url_or_quote: "sourcing_note: \"it is itself a national public-sector agency (the profile's primary-sector criterion, matched directly rather than by analogy)\""
  summary: "(low confidence, residual note) primary-sector nexus for a foreign agency is not one of check 5's four out-of-nexus breach grounds; the entry's independent scale+transferable-lesson ground already clears the bar, so no action needed — flagged only for completeness."
- code: F11
  category: editorial-advisory
  section: entries
  item: "tradertraitor-terraform-lockfile-nostr-dead-drop"
  url_or_quote: "registry.hashicorp-aws[.]com, registry.hashicorp-aws[.]io, registry.hashicorp-terraform[.]io"
  summary: "Hard-invariant violation, not a leave-it advisory: three attacker-controlled domains printed in entry prose, violating \"NEVER put IOCs in an entry... no attacker domains\"; check_run.py's IOC scan only checks hashes/IPv4 and did not catch this."
- code: F11
  category: editorial-advisory
  section: entries
  item: "conference-phishing-rogue-root-ca-mitm-persistence"
  url_or_quote: "\"...a Winlogon modification and its own registered COM object\""
  summary: "Described COM-object persistence behavior has no techniques[] id; T1546.015 (COM Hijacking) is active in the pinned dataset and fits."
- code: F11
  category: editorial-advisory
  section: entries
  item: "the-gentlemen-open-directory-vhdx-backup-ntds-theft"
  url_or_quote: "\"attempt authentication against SMB, LDAP, RDP and WinRM across multiple hosts\""
  summary: "WinRM is explicitly named but techniques[] has no T1021.006 (Windows Remote Management), active in the pinned dataset; RDP/SMB subtechniques are mapped, WinRM is not."
```
