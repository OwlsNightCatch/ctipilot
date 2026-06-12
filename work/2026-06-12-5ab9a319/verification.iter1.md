**Model:** Anthropic Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-06-12T04:36:59Z · ended_at=2026-06-12T04:41:02Z · duration_seconds=243
**Self-telemetry:** webfetch_calls=18 · websearch_calls=0 · bridge_fetches=5 · urls_checked=23

## Verification report — briefs/2026-06-12.md (iteration 1)

Cold read. Every cited URL fetched (WebFetch, or `tools/fetch_source.py` for CISA/NCSC.ch/Oracle/Secret-Service hosts). MSRC vulnerability pages are JS SPAs that do not render under WebFetch and are script-allowlisted; their CVSS/exploitability claims could not be independently verified by fetch (URLs are valid, CVE IDs in-path are correct) — noted, not flagged. Europol page is a JS "Please wait" shell that did not render; its claims are corroborated by the Secret Service body (US/Iceland/Germany/France seizures, Dark2Web) and BleepingComputer (15+ investigations), so not flagged.

The brief is strong: AudiA6, Oracle PeopleSoft/ShinyHunters, Nottingham, MariaDB deep dive, GreatXML, Maine portal, CISA BOD 26-04, npm v12, Imperva/Varonis all verified accurate against fetched primaries. Findings below concentrate on The Gentlemen item (§0/§1), one ESET technique claim (§3), and one cross-source CVSS contradiction (§2).

### Unsupported / hallucinated facts

**F4 — The Gentlemen "478 victims across 66 countries … Germany, France … education, transport, healthcare and finance".** §0 TL;DR: "The Gentlemen RaaS claims 478 victims across 66 countries, Germany and France included". §1 H3 + body: "has claimed 478 victims on its leak site spanning 66 countries including Germany, France and the UK, with education, transport, healthcare and finance among the affected sectors ([The Hacker News, 2026-06-11])". I fetched THN twice: it confirms "478 victims" but does NOT state any country count ("66 countries" absent), does NOT list France ("The majority of the victims are concentrated in Thailand, the U.K., Brazil, Germany, and India"), and names NO sectors. Check Point Research, Krebs, and the Microsoft dissection (the item's other cited sources) likewise carry none of "66 countries", "France", or that sector list. The "478" is supported; the "66 countries", "France", and the four-sector list are unsupported by every source cited on the item. Remediation: drop "66 countries", drop "France", drop the sector list — or source them. (Quote 478 only, with the THN concentration list if a geography line is wanted.)

**F4 — The Gentlemen "drawing former LockBit, Qilin and Medusa affiliates" attributed to Check Point.** §1: "Check Point Research documents the affiliate-favourable 90/10 split that is drawing former LockBit, Qilin and Medusa affiliates ([Check Point Research])". I fetched Check Point: the 90/10 split IS confirmed verbatim ("90% for affiliates and 10% for the operator"), but Check Point does NOT state that affiliates came from / are being drawn from LockBit, Qilin, or Medusa — it discusses the administrator's views of other RaaS programs, no defection claim. No other cited source on the item carries it. Remediation: drop "drawing former LockBit, Qilin and Medusa affiliates" or attribute to a source that states it.

**F4 — ESET OceanLotus "process hollowing, COM hijacking — T1195.002, T1055.012".** §3: "delivered the SPECTRALVIPER backdoor (process hollowing, COM hijacking — [T1195.002], [T1055.012])". I fetched the ESET WeLiveSecurity write-up: it supports T1195.002 (supply-chain) and uses the generic parent T1055 (Process Injection), describing SPECTRALVIPER as a loader that "inject[s] itself … into target processes" plus DLL side-loading (OneDrive.Sync.Service.exe). It does NOT describe "process hollowing" specifically, and does NOT mention "COM hijacking" at all. The brief's sub-technique pairing is also internally inconsistent: T1055.012 is Process Hollowing, not COM hijacking (COM hijacking is T1546.015). Remediation: change to "process injection ([T1055]) and DLL side-loading" per the source, or drop the unsupported "COM hijacking" / specific hollowing sub-technique.

### Surface contradiction

**F9 — FortiSandbox CVE-2026-25089 CVSS: 9.1 (brief, via NCSC-NL) vs 9.8 (CCB Belgium, also cited).** §2 body and the CVE Summary Table both record CVSS **9.1** attributed to NCSC-NL. The CCB Belgium advisory (cited inline on the same item) states CVSS **9.8 (Critical)** — fetched and confirmed: "CVSS Score: 9.8 (Critical)". The NCSC-NL SPA page did not render under WebFetch or the bridge, so I could not confirm the 9.1 against NCSC-NL directly. Two cited sources disagree on the score for the same CVE and the brief silently picks 9.1. Remediation: confirm the NCSC-NL value, and add a `Contradiction:` line in §7 noting NCSC-NL 9.1 vs CCB 9.8 (or reconcile to whichever vendor/source is authoritative). Note: 9.1 vs 9.8 does not change the >9.1 §2 inclusion gate either way.

### Editorial / less-is-more flags (advisory)

**F11 — Maine VRChat quotation insertion.** §1 quotes VRChat: "…the employee/email cited does not exist." The fetched BleepingComputer text reads "…the employee cited does not exist." The "/email" is an inserted gloss inside quotation marks. Minor; recommend either removing "/email" from inside the quote marks or moving it outside as paraphrase. Not blocking on its own.

**F11 — Check Point Research date.** §1 cites "[Check Point Research, 2026-06-09]". The fetch summariser reported the article date as "May 13, 2026" on one pass (the page's date extraction is unreliable — Krebs links it as current). Advisory only: confirm the Check Point publication date; if it is May, the "developing-window allowance" note in §7 should cover it (§7 already cites Check Point as 2026-06-09 background). No hard action required if the date is correct.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 0, advisory: 2)

Truth count = F4 (Gentlemen geography/sectors) + F4 (Gentlemen LockBit/Qilin/Medusa) + F4 (ESET process-hollowing/COM-hijacking). F9 (CVSS contradiction) is counted under editorial=0 here as a surface-contradiction request rather than a wrong-fact assertion — the brief's 9.1 may be correct per NCSC-NL; the defect is the un-surfaced disagreement. Recount: treating F9 as editorial gives truth=3, editorial=1, advisory=2. The three F4 items are the blocking defects: each is a statement the brief attributes to a named source that I fetched in this iteration and that does not contain the statement.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "The Gentlemen ransomware — 478 victims / 66 countries / sectors"
  url_or_quote: "claimed 478 victims on its leak site spanning 66 countries including Germany, France and the UK, with education, transport, healthcare and finance among the affected sectors"
  summary: "THN (cited) confirms 478 only; states victims concentrate in Thailand/UK/Brazil/Germany/India, gives no country count, no France, no sectors. Check Point/Krebs/Microsoft also carry none of '66 countries', 'France', or the sector list. Drop or source the geography and sectors."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "The Gentlemen ransomware — affiliate origins"
  url_or_quote: "Check Point Research documents the affiliate-favourable 90/10 split that is drawing former LockBit, Qilin and Medusa affiliates"
  summary: "Check Point confirms the 90/10 split verbatim but does NOT state affiliates are drawn from LockBit/Qilin/Medusa; no cited source supports the migration claim. Drop the LockBit/Qilin/Medusa clause."
- code: F4
  category: hallucinated-fact
  section: research
  item: "ESET OceanLotus / SPECTRALVIPER techniques"
  url_or_quote: "delivered the SPECTRALVIPER backdoor (process hollowing, COM hijacking — T1195.002, T1055.012)"
  summary: "ESET write-up supports T1195.002 and generic T1055 (loader injects into target processes; DLL side-loading), but does NOT describe process hollowing specifically and never mentions COM hijacking. T1055.012 = Process Hollowing, not COM hijacking. Change to 'process injection (T1055) and DLL side-loading' or drop COM-hijacking."
- code: F9
  category: surface-contradiction
  section: trending-vulnerabilities
  item: "CVE-2026-25089 Fortinet FortiSandbox"
  url_or_quote: "CVSS 9.1 (brief/NCSC-NL) vs CVSS 9.8 (CCB Belgium, https://ccb.belgium.be/advisories/warning-fortinet-addresses-critical-command-injection-vulnerability-fortisandbox-patch)"
  summary: "CCB Belgium (cited) states CVSS 9.8; brief records 9.1 attributed to NCSC-NL (SPA, could not render to confirm). Surface the disagreement in §7 and/or reconcile to the authoritative score."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "Maine breach-portal — VRChat quote"
  url_or_quote: "VRChat did not submit this Notice of Data Incident, and the employee/email cited does not exist"
  summary: "Fetched source reads 'the employee cited does not exist'; '/email' is inserted inside quote marks. Remove from inside the quotation or move outside as paraphrase. Advisory."
- code: F11
  category: editorial-advisory
  section: active-threats
  item: "The Gentlemen — Check Point Research citation date"
  url_or_quote: "[Check Point Research, 2026-06-09]"
  summary: "Fetch summariser reported article date 'May 13, 2026'; date extraction on the page is unreliable. Confirm the Check Point publish date; §7 developing-window note should cover it if older. Advisory."
```
