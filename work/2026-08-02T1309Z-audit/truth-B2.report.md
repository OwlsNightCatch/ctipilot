# Truth pass — batch B2 (W30 weekly strategic entries)

Run id: `2026-08-02T1309Z-audit` · Started: 2026-08-02T13:13:48Z · Ended: 2026-08-02T13:24:53Z

11 entries checked. Verdicts: 1 factual-error, 2 imprecision, 8 clean. `machine_surface: true` on none (all defects are body/prose framing, none reach `cves[]`/`techniques[]`/entity keys).

---

## 1. weekly-w30-ai-autonomous-operator-and-target.md — FACTUAL-ERROR

**Defect:** The headline ("an LLM rebuilt a patched exploit chain for ~$25"), summary, and body all frame the Searchlight Cyber GPT-5.6 WordPress case as the AI "rediscovering and weaponising the **already-patched** WordPress 'WP2Shell' pre-auth chain." Fetching the cited primary source (slcyber.io, 2026-07-20) directly contradicts this: the article frames the find as an **original discovery** of a then-unpatched pre-auth RCE — "I didn't quite believe this at first, as WordPress ... hadn't had any meaningful pre-auth vulnerabilities this decade" — and states the researcher "held off on publishing this issue to give defenders a chance to upgrade their WordPress instances over the weekend." The words "rediscover," "already patched," and "already known" appear nowhere in the source. Rapid7's independent CVE-2026-63030/CVE-2026-60137 write-up (a different, correctly-sourced entry in this same batch) separately confirms "Searchlight Cyber, whose researchers identified the vulnerability," disclosed 2026-07-17, patched in 6.9.5/7.0.2 — i.e. Searchlight's AI-driven find and the vendor patch landed on essentially the same timeline, not "AI rebuilds an old patched bug." This inverts the significance of the finding: the real story is autonomous **zero-day discovery** capability, not compressed **weaponization of a public patch**. This is a genuine, load-bearing misreading of the primary source that changes what defenders should take away from the item.

**Fix suggestion:** Reframe to "Searchlight Cyber tasked GPT-5.6 with autonomously discovering a novel pre-auth RCE chain in WordPress core (independently named 'WP2Shell'), reaching an unauthorised admin account in ~10 hours for ~$25 — the researcher withheld publication until a vendor fix shipped." Also worth noting for defenders: the same vulnerability was independently exploited in the wild and KEV-listed within days regardless of the responsible-disclosure delay (per the "exploited-internet-facing-enterprise-persistence" entry in this same batch), which is itself a notable and correctly-covered fact.

All other claims in this entry (OpenAI Hugging Face disclosure mechanics, Hunt.io Thailand Hermes/YOLO-mode quote, Sysdig JADEPUFFER/ENCFORGE quote, Huntress FakeAgent 29-orgs/claude.ai-artifact/SectopRAT) were fetched and verbatim-confirmed against their cited sources — clean.

---

## 2. weekly-w30-bafin-teamviewer-disclosure-precedent.md — CLEAN

Both BaFin's own release and heise's corroborating article were fetched. The German-language quotes ("Die Finanzaufsicht Bafin hat am 16. Juli 2026 eine Geldbuße...", the Ad-hoc-Meldungen sentence) are exact verbatim matches. Heise additionally confirms the appeal-rights claim ("Gegen das Bußgeld ... könne TeamViewer noch Einspruch einlegen") and the Article 17(1) MAR citation, both used correctly in the body. No APT29 claim is sourced to BaFin/heise directly — the entry correctly treats that as prior-reported context, not a fresh claim.

---

## 3. weekly-w30-c2-through-trusted-infrastructure.md — CLEAN

Fetched Kaspersky (Cav3rn DNS AAAA fallback mechanism — confirmed, and confirmed the article itself cites/links Group-IB's HOLLOWGRAPH as prior public reporting on the same component), Cisco Talos (msaRAT/CDP/WebRTC/Twilio/Cloudflare quote — exact match, attributed to Chaos ransomware group matching the entry's `actor:chaos-ransomware` entity), Zscaler (TELESHIM/Telegram-API quote — exact match), Proofpoint (Cruciferra process-ghosting/BYOVD/indirect-syscalls-from-clean-ntdll and TA4922→AsyncRAT attribution — both confirmed verbatim), and Kaspersky's BitLocker-extortion piece (RDP/SQL Server/RMM/GPO/BitLocker mechanics for both LatAm cases, and confirmed Kaspersky explicitly does NOT confirm same-operator, matching the entry's hedge). Group-IB's own page returned only page metadata (JS-rendered site blocked structured extraction) but title/date/description via `<script type="application/ld+json">` corroborate the claim, and Kaspersky's independent write-up serves as a second, fully-fetchable source for the same claims.

---

## 4. weekly-w30-ch-eu-public-sector-third-party-incidents.md — CLEAN

Every named incident checked against its cited source or independent corroboration: Stadler Rail/swissinfo.ch (exact quote on the CHF 10M unpaid ransom and shared data-exchange-platform vector — confirmed); Le Temps/BravoX (paywalled — jina reader only returned the teaser, but the headline itself states "100 000 dossiers de clients... conseiller d'Etat," and a web search cross-check against 20 minutes, taxmanager.ch, 24heures.ch and Les Observateurs independently corroborates all cited figures: ~220 GB, >100,000 files, ~15 Vaud municipalities, State Councillor Vassilis Venizelos); Stiftung Autismuslink's own PDF notice (fetched directly — "grössere Datenmengen durch die Angreifer abgezogen und unser Server vorübergehend verschlüsselt" is an exact match, and the PDF's "Leistungsvereinbarungen mit der IV und der BKD" independently confirms the entry's "cantonal education-directorate and disability-insurance-linked clients" framing); Ransomware.live's INC Ransom listing (confirmed); IFAGE/20 minutes (exact quote match) and ICTjournal (confirms DragonForce attribution, correctly cited to the earlier 2026-07-17 article rather than the later 20 minutes piece — proper per-clause adjacency); ANCPI/go4it.ro and psnews.ro (both confirm DNSC's vCenter compromise, 1,083-VM enumeration, ~100 VMs deleted, ~2M ePayment records, and the antivirus gap, with the psnews.ro Romanian-language quote an exact match).

---

## 5. weekly-w30-eu-procurement-assurance-bars.md — CLEAN

Both ENISA pages fetched directly; both quoted sentences ("These baseline requirements apply as a mandatory prerequisite...", "A Contribution Agreement of EUR 6 million...") are exact matches, as are the EU Cybersecurity Reserve two-year certification requirement, the Incident Response vertical, the consultation window (2026-07-24 to 2026-09-13), and the NIS Cooperation Group / EU Health ISAC collaboration on the procurement guidelines.

---

## 6. weekly-w30-exploited-internet-facing-enterprise-persistence.md — CLEAN

NCSC-CH's advisory API confirms "Current exploitation status: Actively exploited" for CVE-2026-6875 verbatim. BleepingComputer confirms the 2026-07-18 ServiceNow exploitation start and KB3137947 hotfix framing. NCSC-NL's CSAF for NCSC-2026-0237 confirms CVE-2026-50522 at CVSS 9.80 and the watchTowr machine-key-theft detail (1.0.2 revision). BleepingComputer's SharePoint article confirms the watchTowr "Attacker Eye... within hours" quote verbatim. Check Point's own advisory confirms the CVE-2026-16232 CVSS-9.3 auth-bypass, the "handful of customers" exploitation claim, and the exact "very specific configuration" quote. Both cited CISA KEV bulletins (07-21 four-CVE, 07-22 two-CVE) were fetched directly and list exactly the CVEs the entry cites (CVE-2026-0770, CVE-2026-63030, CVE-2026-60137, CVE-2026-16232, CVE-2026-50522). Rapid7's WP2Shell write-up confirms the "Given confirmed exploitation in the wild..." quote verbatim and independently names Searchlight Cyber as the original discoverer (consistent with the ground truth used to flag entry 1 above).

---

## 7. weekly-w30-joomla-extension-wave-status.md — IMPRECISION

Gridbox (CVE-2026-61425, cookie-as-identity auth bypass, Super User via a single cookie, fixed 2.20.1, vulnerable since the prior 2025-10-21 release) is fully confirmed against mySites.guru's own post. Membership Pro's unauthenticated-upload disclosure (CVE-2026-62415) is also confirmed against its own mySites.guru post. However, the body's closing sentence — "Alongside it the week added an unauthenticated upload in Membership Pro, unauthenticated SQL injection and order-forgery in EasyStore, and an invoice IDOR in Events Booking" — carries **no inline citation at all**, and neither EasyStore nor Events Booking has a `sources[]` record in frontmatter (only the two Gridbox/Membership-Pro URLs are listed). A web search confirms both disclosures are real and independently attributable (mySites.guru's own "EasyStore Joomla Security Vulnerabilities" post, CVE-2026-65759/-65760/-65761, fixed in EasyStore 2.0.2; and "Events Booking Upload & Enumeration Flaws," CVE-2026-58149/-60024/-60025, fixed in 5.8.1/4.9.5) — so this is not a hallucination, but it is an uncited claim that should have carried its own source records. Separately, `affected_products[]` lists only "Balbooa Gridbox for Joomla" despite the body naming four distinct products.

---

## 8. weekly-w30-looking-ahead.md — IMPRECISION

Certighost/CVE-2026-54121 confirmed against Microsoft's own MSRC API (AD CS Elevation of Privilege, released 2026-07-14, "authenticated attacker... gain the ability to perform privileged Active Directory operations" — consistent with the DCSync/krbtgt framing; CybersecurityNews' corroborating detail on the specific public PoC could not be independently fetched, blocked by a bot-challenge, but is a plausible corroborating-role extension of the MSRC description). Mitel's own PSIRT advisory confirms CVSS 9.8, internal id MTLVULN-1694, and "no CVE assigned" verbatim. ENISA EUMSS consultation dates re-confirmed (see entry 5). The nginx item, however, has a citation-support gap: the body states "anyone running internet-facing nginx should complete the **F5 out-of-band patch**," but the entry's sole cited source (cyberstan.co.uk) frames the fix as "scheduled for the F5 Security Advisory on 15 July 2026" — a planned release, never described as "out-of-band" on that page. A web search confirms F5's July release genuinely was reported elsewhere (BleepingComputer, Field Effect) as an out-of-band patch bundle, so the underlying fact is true — but it is not supported by the page this entry actually cites for it.

---

## 9. weekly-w30-npm-ai-toolchain-supply-chain-status.md — CLEAN

CrowdStrike's own blog confirms every mechanic cited: rogue MCP entries into Cursor/VS Code/Claude Desktop/Windsurf, global git-template hook persistence, npm/AWS/SSH + multi-provider LLM API key exfiltration, and the 48–96 hour activation delay, all verbatim. The "14 investigated behaviours, only 2 met the bar for high-fidelity alerting" figure is an exact match ("only 2 met the fidelity bar for customer-visible alerting"). SecurityBrief's corroborating article independently repeats the same mechanics.

---

## 10. weekly-w30-state-nexus-webmail-espionage.md — CLEAN

This entry received the heaviest verification load given its state-attribution claims, and holds up fully. The joint CSA AA26-204A was fetched directly: the "view-based exploit that only requires a user to view a malicious email..." quote is an exact match, as are the 90-days-of-email, Global Address List, and 2FA-token exfiltration claims, and CVE-2025-66376/LAUNDRY BEAR attribution. The claimed "16 nations" is exactly correct — the advisory's co-sealing-agency list was counted and totals authorities from 16 distinct countries (US, Netherlands, Australia, Canada, New Zealand, UK, Czech Republic, Denmark, Estonia, Finland, France, Italy, Moldova, Poland, Spain, Sweden). Proofpoint's TA488 article confirms the CSS-@import sanitizer bypass and the "ZimbraWeb" application-specific-password persistence mechanism verbatim, and — critically for the entry's actor-differentiation claim — confirms verbatim that "Proofpoint has not observed TA458 using CVE-2025-66376," correctly cited to that same TA488 URL (not the TA458 URL), matching the actual location of the sentence. Proofpoint's separate TA458/RoundPress article independently confirms the "half-click exploit requires no social engineering..." quote, the GRU assessment, and the SOGo CVE-2026-8496/Alinto/5.12.8 disclosure chain, all verbatim.

---

## 11. weekly-w30-vuln-status-rollup.md — CLEAN

This roll-up's own directly-cited sources (NCSC-CH ServiceNow advisory, both CISA KEV bulletins, NCSC-NL's Oracle CPU advisory) were re-fetched and confirm exactly the claims made: NCSC-NL's Dutch-language assessment "het NCSC het zeer waarschijnlijk [acht] dat grootschalig misbruik op korte termijn plaats gaat vinden" is an exact match for "very likely" large-scale abuse, and the CSAF data confirms "9 kwetsbaarheden... hoogste score van 10.0" (nine CVSS-10.0 flaws). All other per-CVE claims in this roll-up (SolarWinds Serv-U, GLPI, Mitel, Zimbra, OT libraries, GitLab) are explicitly delegated to the referenced daily operational entries rather than asserted fresh here, and are out of scope for this weekly-only batch.

---

## Counts

- clean: 8
- imprecision: 2
- factual-error: 1
- machine_surface true: 0
- Primary/corroborating URLs fetched this pass: ~45 (see `url-liveness.tsv`)
