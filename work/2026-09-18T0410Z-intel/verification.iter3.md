**Model:** Sonnet 5 (`claude-sonnet-5`)
**Timestamps:** started_at=2026-09-18T05:43:48Z · ended_at=2026-09-18T05:54:29Z · duration_seconds=641

## Verification report — 2026-09-18T0410Z-intel (iteration 3)

### Prior-iteration (iteration 2) deltas — verified

All eight iteration-2 remediations checked against current file state and the cited sources; all confirmed correct:

1. Brevo evidence[] split (F4) — both records are now genuine contiguous verbatim substrings of the BleepingComputer article (`file.js` plugin quotes checked verbatim against the fetched page). Confirmed fixed.
2. `state/cves_seen.json` CVE-2026-87886 title corrected to name only cPanel & WHM/Plesk — confirmed, no DirectAdmin string anywhere in `state/cves_seen.json`, `entities/registry.yaml`, or the published entry.
3. Orphan `product:acronis-backup-plugin-for-directadmin-linux` registry key — confirmed removed; no entry references it.
4. NTC entry's two previously-uncited sentences — confirmed both now cited: the EU/US-regulatory-response clause and the NTC confidential-disclosure/fix-status clause are supported by the fetched SRF and NTC pages respectively (see new finding below on one sub-clause not fully carried).
5. FamousSparrow PEB_LDR_DATA/LDR_DATA_TABLE_ENTRY technique — confirmed verbatim against ESET's "Host process camouflage for dynamically loaded PEs" section.
6. FamousSparrow → `campaign:famoussparrow-azerbaijan-2026` relations edge — confirmed correctly declined. Read ESET's full SparroWocky article end to end; it never mentions Azerbaijan, an oil & gas operator, or UAT-9244. Adding the edge would have been an F13 analytical-link-as-fact. Agree this is a closed, correct call, not an open finding.
7. NTC Reischuk quote trim — confirmed the retained quote ("Würden die chinesischen Hersteller...") is a faithful, complete, verbatim sentence from the fetched SRF article.
8. BleepingComputer Acronis citation date 2026-09-15 — confirmed against the fetched page's own `date:` metadata (trafilatura: `date: "2026-09-15"`).

Independent full cold pass across all 10 entries follows; new findings below were not part of the iteration-2 delta list.

### Unsupported / hallucinated facts

**#1 (F4).** `cve-2026-20079-cisco-secure-fmc-auth-bypass-root-hotfix` — the new `evidence[]` record added by this run's `## Update — 2026-09-18T05:04:00Z` section:
> "A registered sftunnel peer has incorrect permissions to write an arbitrary file to any location on the device. ... A successful exploit could allow the attacker to write a file to the device that is executed with root privileges. To exploit this vulnerability, the attacker must have valid user credentials on the affected device."

Fetched `cisco-sa-fmc-sftunn-codex-c3O4Jft2` directly. The advisory's actual, contiguous text is:
> "This vulnerability exists because a registered sftunnel peer has incorrect permissions to write an arbitrary file to any location on the device. **An attacker could exploit this vulnerability by hijacking the sftunnel communication connection or being a valid registered sftunnel peer and sending an sftunnel command to write a malicious file to the disk of an affected device.** A successful exploit could allow the attacker to write a file to the device that is executed with root privileges. To exploit this vulnerability, the attacker must have valid user credentials on the affected device."

The `evidence[]` record's `"..."` splices out the bolded middle sentence and presents the remainder as one contiguous quote — exactly the "inserted ellipsis...splice of two sentences" pattern check 4b defines as F4. Fix: either drop the ellipsis and quote only one contiguous span, or split into two separate records.

### Citation does not support the claim

**#2 (F3, high confidence).** `brevo-cloudflare-worker-clickfix-supply-chain` body:
> "Visitors saw a fake Cloudflare human-verification page instructing them to press Win+R, paste and press Enter, a ClickFix lure that ran an attacker-supplied clipboard command to download Windows malware, and did not activate for crawlers, developers or automated scanners ([Sansec, 2026-09-16])."

Fetched `sansec.io/research/brevo-supply-chain-attack` directly: Sansec's own text says only "show the visitor a clickfix overlay (urging the person to prove that they're human by copy-pasting a command)" — it never mentions Win+R, Ctrl+V, Enter, or that the command downloads malware onto a Windows computer. Those specific mechanics are stated only in Brevo's own write-up ("press Win+R, then Ctrl+V, then Enter... ran a command placed on the clipboard by the script, which downloaded malware onto the visitor's Windows computer"), which is not cited in this sentence at all. Only the trailing "did not activate for crawlers, developers or automated scanners" clause is Sansec's. Per check 2(d), the sentence-ending citation is claiming every fact in the sentence; most of it is uncarried by Sansec. Fix: cite Brevo for the Win+R/Ctrl+V/Enter/malware-download clause, Sansec only for the crawler-exemption clause.

**#3 (F3, high confidence).** Same entry, next paragraph:
> "Brevo's post-mortem does not mention a separate SSO-hijacking incident it disclosed on 2026-09-10 that led to a phishing campaign against Trezor customers ([Brevo, 2026-09-17])..."

Fetched `status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up` directly and read it end to end — it contains zero mentions of Trezor, phishing, or the September 10 incident at all (consistent with the entry's own claim that the post-mortem is silent on it). But the Trezor **fact itself** — that the Sept 10 SSO incident "led to a phishing campaign against Trezor customers" — cannot be sourced to Brevo's silent document; it comes from BleepingComputer, which states: "One high-profile victim was cryptocurrency wallet vendor Trezor, which reported on September 11 that phishing attacks reached 347,000 user email addresses." The citation `([Brevo, 2026-09-17])` is attached to a clause containing a fact only BleepingComputer supports. Fix: re-cite the Trezor/phishing-campaign clause to BleepingComputer.

**#4 (F3, high confidence).** `revolut-fake-government-request-kyc-breach`, `## Update — 2026-09-18T05:08:00Z` section and matching `evidence[]` records:
> "Hudson Rock states the hacker gained access to government employee accounts using an infostealer, and after gaining entry to an employee's email, would log in, add a recovery email under their control, begin logging activities, and silently monitor communications ([Hudson Rock, 2026-09-15])."
> "...an anti-forensic technique that let the campaign run for roughly five months, beginning with forged court orders before pivoting to Revolut Bank UAB... ([Hudson Rock, 2026-09-15])."

Fetched the Hudson Rock page via `jina` (direct `extract` returns only an empty LiveChat widget shell, as the run record notes). The full article has two clearly separated parts: (a) "BREAKING: The investigations team at **Duel** has established contact with the hacker..." through direct quotes attributed to "**The Duel Investigations Team**" — this is the section containing the infostealer/recovery-email/logging-activities claim and the five-month/forged-court-orders/Revolut-Bank-UAB narrative; and (b) a separate, clearly headed "## Hudson Rock's Analysis & Intelligence" / "### New Insight from Hudson Rock" section, which contains **only** the pec.interno.it identification, the ~300-compromised-credential database finding, and Hudson Rock's own assessment that the attacker likely didn't infect the employees directly. CyberInsider's own reporting (fetched, `cyberinsider.com/revolut-hackers-used-infostealer-to-hijack-italian-government-emails`) draws the identical distinction: "Duel's investigations team says it established contact with a hacker..." vs. "Hudson Rock's investigation supports the use of compromised Italian government accounts but questions the attacker's account of how they obtained them." Two of the entry's three `evidence[]` records attributed to publisher "Hudson Rock" (the infostealer/recovery-email quote and the ".eml file" quote) are verbatim text from the page, but they are Duel's/the attacker's claims republished on Hudson Rock's blog, not Hudson Rock's own analysis — the entry's own `sourcing_note` already correctly describes this provenance ("the surrounding attacker narrative...originates from the attacker's own account to a third outlet, Duel, relayed via Hudson Rock"), but the body and `evidence[]` publisher fields contradict that same sourcing_note by attributing the Duel/attacker narrative directly to "Hudson Rock" as if Hudson Rock itself made the claim. This inflates the credibility of unverified attacker-relayed claims. Fix: re-attribute the two narrative quotes/clauses to "the attacker, via Duel Investigations Team (relayed by Hudson Rock)" or similar, reserving "Hudson Rock" attribution for the pec.interno.it/300-credential finding only.

**#5 (F3, low confidence).** `ntc-swiss-solar-inverter-cybersecurity-assessment` body:
> "The EU has withdrawn subsidy eligibility for Chinese-inverter projects and the US has declared a grid emergency that can force removal of already-installed sanctioned-country inverters; Switzerland has taken no equivalent step ([SRF, 2026-09-16])."

Fetched SRF's article directly. It states the EU/US measures verbatim-equivalently but never states, in any form, that "Switzerland has taken no equivalent step" — that clause is an inference from the article's overall juxtaposition (the "Trotzdem" framing plus canton Bern's continued Huawei procurement), not a stated fact. Low confidence because the inference is a reasonable synthesis of the article's own framing, but it is presented as a flat fact under a citation that does not carry it verbatim.

**#6 (F3, low confidence).** `gyazo-helpfeel-data-breach-image-upload-rce` body:
> "Gyazo's default access-control model for a 'private' image relies entirely on the image ID staying secret; the leaked IDs directly defeat that model, and Helpfeel confirms the attacker also obtained a list identifying which images were marked private, so it 'cannot rule out' unauthorized viewing of private content ([Helpfeel Inc., 2026-09-16])."

Fetched Helpfeel's own notice directly — it never describes the access-control model as relying on ID secrecy; that specific mechanism claim is stated by The Hacker News, drawing on Gyazo's own help pages ("the ID is long enough that a link 'can't be guessed'... For a capture at the default setting, the link is the only thing protecting it"). The sentence-ending citation is Helpfeel only, but the opening clause's fact is carried by The Hacker News, cited elsewhere in the entry but not here.

**#7 (F3, low confidence).** `cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev` frontmatter: `event_date: "2026-09-15"` while the entry's own primary source (`sources[0]`, role: primary) is Help Net Security dated `2026-09-16`. `event_date` instead matches the corroborating BleepingComputer source's date (2026-09-15). Check 4b requires `event_date` to match the primary source's publication date; here it matches the corroborating one. Likely a defensible editorial choice (BleepingComputer's 2026-09-15 article states Acronis's advisory was updated "today," i.e. the actual disclosure-update date), but it is a literal mismatch against the entry's own designated primary source.

### Claims missing inline citation

**#8 (F5).** `gyazo-helpfeel-data-breach-image-upload-rce`, last sentence of the body: "Helpfeel's other two products, Helpfeel and Cosense, run on separate infrastructure and were not found to have any unauthorized data disclosure." carries no inline citation (the fact is supported by both fetched sources, but the sentence itself is uncited, and the preceding sentence's citation does not extend to it under check 2(d)/3).

**#9 (F5).** `cve-2026-91843-check-point-security-mgmt-stack-overflow`, body and `sourcing_note`: "No source — Check Point's own advisory, BSI CERT-Bund, CERT-FR, or CISA's own SSVC exploitation-decision field (which reads 'none') — reports observed exploitation..." The entry's `sources[]` list contains no CISA source at all (only Check Point, BSI, CERT-FR), and no inline citation is given for the "CISA's own SSVC exploitation-decision field" claim specifically. This is a specific, checkable factual claim about a named CISA data field with zero supporting link.

### Strengthen primary source

**#10 (F6, low confidence).** `cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev` — `sources[0]` (role: primary) is Help Net Security, a journalism outlet, not a vendor PSIRT/research-lab/regulator/victim source per check 6's list. The `sourcing_note` explains Acronis's own advisory page (`security-advisory.acronis.com/advisories/SEC-10986`) is an unreachable client-rendered SPA on every transport tried, which is a legitimate, documented constraint rather than a shortcut — flagging this at low confidence since the letter of check 6 is not met even though the workaround is reasonable and disclosed.

### Quantifier without source

**#11 (F14, low confidence).** `famoussparrow-sparrowocky-backdoor-latam-gov` — summary and body both state "90% of [FamousSparrow's] observed targets were in Latin America... almost all of them governmental entities." Fetched ESET's article in full: it states the 90%-in-Latin-America figure verbatim ("90% of the group's targets registered in our telemetry have been located in the region") but never quantifies the government-sector proportion — its only sector claim is qualitative ("FamousSparrow is extensively targeting governmental organizations in Latin America") and it names governmental entities in eight countries without stating what fraction of the 90% (or of all targets) is governmental. "Almost all of them governmental entities" is the researcher's own inference from the illustrative examples, not an ESET-stated quantifier. Low confidence because the underlying claim (heavy government focus) is well supported qualitatively; the added quantifier ("almost all") is not.

### Verdict

`NEEDS_FIXES (truth: 8, editorial: 3, advisory: 0)`

Coverage note: no additional missed-angle (F10) identified with evidence from this iteration's fetches beyond what the run record's own coverage-backlog section already tracks; I did not find a plausible in-window story the research missed. Findings above are concentrated in citation-adjacency precision (F3/F4) on the newest content (this run's two new update sections on Cisco FMC, Revolut, and the three brand-new incident/vulnerability entries) rather than in relevance or structural defects — the run's coverage shape, priority calibration, classification blocks, and action-item discipline all held up under this cold pass.

### Findings summary (machine-readable)
```yaml
- code: F4
  category: hallucinated-fact
  section: cve-2026-20079-cisco-secure-fmc-auth-bypass-root-hotfix
  item: "CVE-2026-20079 — Cisco Secure FMC (Update 2026-09-18T05:04:00Z, CVE-2026-20324 evidence)"
  url_or_quote: "\"A registered sftunnel peer has incorrect permissions to write an arbitrary file to any location on the device. ... A successful exploit could allow the attacker to write a file to the device that is executed with root privileges. To exploit this vulnerability, the attacker must have valid user credentials on the affected device.\""
  summary: "Ellipsis splices out a full sentence from Cisco's contiguous advisory text (cisco-sa-fmc-sftunn-codex-c3O4Jft2), presenting two non-adjacent sentences as one quote."
- code: F3
  category: claim-not-supported
  section: brevo-cloudflare-worker-clickfix-supply-chain
  item: "Brevo Cloudflare Worker ClickFix supply-chain compromise"
  url_or_quote: "https://sansec.io/research/brevo-supply-chain-attack — cited for 'press Win+R, paste and press Enter... download Windows malware'"
  summary: "Sansec's page never mentions Win+R/Ctrl+V/Enter or malware download; those facts are stated only by Brevo's write-up, not cited in this sentence. Only the crawler-exemption clause is Sansec's."
- code: F3
  category: claim-not-supported
  section: brevo-cloudflare-worker-clickfix-supply-chain
  item: "Brevo Cloudflare Worker ClickFix supply-chain compromise"
  url_or_quote: "https://status.brevo.com/incidents/01M2QBC4EZ24ZACW6SWQYVW8N3/write-up — cited for 'led to a phishing campaign against Trezor customers'"
  summary: "Brevo's write-up never mentions Trezor; the Trezor/phishing-campaign fact is stated only by BleepingComputer (https://www.bleepingcomputer.com/news/security/brevo-supply-chain-attack-injected-clickfix-scripts-on-customer-sites/)."
- code: F3
  category: claim-not-supported
  section: revolut-fake-government-request-kyc-breach
  item: "Revolut fake-government-request KYC breach (Update 2026-09-18T05:08:00Z)"
  url_or_quote: "\"Hudson Rock states the hacker gained access to government employee accounts using an infostealer... [and] Upon receiving a reply to their fraudulent emails, they would immediately download it as a .eml file...\" ([Hudson Rock, 2026-09-15])"
  summary: "These two evidence[] quotes are from 'The Duel Investigations Team' section of the Hudson Rock blog page (the attacker's own account relayed by Duel), not Hudson Rock's own 'New Insight' analysis section (which covers only the pec.interno.it/300-credential finding). CyberInsider's own reporting draws the identical Duel-vs-Hudson-Rock distinction the entry collapses."
- code: F3
  category: claim-not-supported
  section: ntc-swiss-solar-inverter-cybersecurity-assessment
  item: "NTC Swiss solar inverter cybersecurity assessment"
  url_or_quote: "\"Switzerland has taken no equivalent step ([SRF, 2026-09-16])\""
  summary: "(low confidence) SRF's article never states this as a fact; it is an inference from the article's overall framing (EU/US measures vs. canton Bern's continued Huawei procurement)."
- code: F3
  category: claim-not-supported
  section: gyazo-helpfeel-data-breach-image-upload-rce
  item: "Gyazo (Helpfeel) data breach"
  url_or_quote: "\"Gyazo's default access-control model for a 'private' image relies entirely on the image ID staying secret... ([Helpfeel Inc., 2026-09-16])\""
  summary: "(low confidence) Helpfeel's own notice never describes the access-control model; this framing is stated by The Hacker News, drawing on Gyazo's help pages, and is cited elsewhere in the entry but not on this clause."
- code: F3
  category: claim-not-supported
  section: cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev
  item: "CVE-2026-87886 Acronis Backup plugin"
  url_or_quote: "event_date: \"2026-09-15\" vs. sources[0] (primary, Help Net Security) date \"2026-09-16\""
  summary: "(low confidence) event_date matches the corroborating BleepingComputer source's date, not the designated primary source's publication date, per check 4b."
- code: F5
  category: missing-citation
  section: gyazo-helpfeel-data-breach-image-upload-rce
  item: "Gyazo (Helpfeel) data breach"
  url_or_quote: "\"Helpfeel's other two products, Helpfeel and Cosense, run on separate infrastructure and were not found to have any unauthorized data disclosure.\""
  summary: "Final body sentence carries no inline citation."
- code: F5
  category: missing-citation
  section: cve-2026-91843-check-point-security-mgmt-stack-overflow
  item: "CVE-2026-91843 Check Point Security Management stack overflow"
  url_or_quote: "\"...or CISA's own SSVC exploitation-decision field (which reads 'none')...\""
  summary: "No CISA source appears anywhere in sources[]; this specific claim about a named CISA data field has no supporting citation."
- code: F6
  category: strengthen-primary-source
  section: cve-2026-87886-acronis-backup-plugin-lpe-cpanel-kev
  item: "CVE-2026-87886 Acronis Backup plugin"
  url_or_quote: "https://www.helpnetsecurity.com/2026/09/16/acronis-backup-plugin-vulnerability-exploited-cve-2026-87886/ (role: primary)"
  summary: "(low confidence) Primary source is a journalism outlet, not a vendor PSIRT/research-lab/regulator/victim source; Acronis's own advisory (security-advisory.acronis.com/advisories/SEC-10986) is documented as unreachable on every transport tried, a legitimate but unmet constraint against check 6's letter."
- code: F14
  category: quantifier-without-source
  section: famoussparrow-sparrowocky-backdoor-latam-gov
  item: "FamousSparrow SparroWocky backdoor"
  url_or_quote: "\"90% of observed 2025-2026 targeting hit Latin America, almost all of it governmental entities\""
  summary: "(low confidence) ESET states the 90%-in-Latin-America figure verbatim but never quantifies the government-sector proportion as 'almost all'; that quantifier is the researcher's own inference from illustrative examples."
```
