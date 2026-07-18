**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-18T05:14:39Z · ended_at=2026-07-18T05:22:04Z · duration_seconds=445
**Self-telemetry:** urls_checked=13 · webfetch_calls=2 · bridge_fetches=13

## Verification report — 2026-07-18T0409Z-intel (iteration 3)

Cold read of all 6 new entries + run record. Every inline URL fetched (bridge/WebFetch/NVD/CISA-KEV) or cross-checked against the on-disk deepread extracts; every evidence[] quote checked as a contiguous verbatim substring; every cves[] CVSS pairing checked against its owning authority.

### Citation does not support the claim

**F3 — abbott-exact-sciences-shinyhunters-entra-sso-vishing (truth).**
Claim (body para 2): "A second, separate claim by an actor calling itself 'ShadowByt3$' alleges compromise of an externally facing LabCentral customer portal, from which Abbott says only publicly available reference documentation was taken ([MedTech Dive, 2026-07-17])."
I fetched the cited MedTech Dive article this iteration (WebFetch): it covers only the single Abbott Cancer Diagnostics disclosure (title "Abbott discloses cyberattack on cancer diagnostics business", 2026-07-17) and does **not** mention ShadowByt3$, LabCentral, or "publicly available reference documentation" — it explicitly states Abbott "did not disclose what kind of information was accessed."
The claim is factually accurate but is supported by the entry's OTHER source, BleepingComputer, which I also fetched: it contains "Shadowbyt3$", "attackers breached its LabCentral portal", and verbatim "It houses publicly available technical product reference documents, including operating manuals, troubleshooting checklists and product specifications, and does not contain proprietary/sensitive customer or business information."
Remediation: change the inline citation on that sentence from MedTech Dive to BleepingComputer (already source #2 on the entry). MedTech Dive may remain a general corroborating source for the base incident.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 0)

One misattributed citation. Everything else verified clean (see notes below).

---

### Notes — what was verified and passed

**VMware Avi (CVE-2026-47865):** Broadcom VMSA-2026-0005 deepread confirms 9.8 auth bypass, all seven CVEs + CVSS (47866=8.3, 47867=8.7, 47868=7.8, 47869=8.7, 47870=7.1, 47871=8.8), "no workarounds", NATO NCSC (Filip Waeytens) reporter. Evidence quote verbatim. FIRST vectors confirm 47865 AV:N/PR:N (pre-auth remote). heise corroboration fetched — confirms 9.8 + auth/authorization bypass framing. Priority high defensible (pre-auth 9.8 + no workaround + NATO provenance, no ITW). Classification A/2 correct.

**Siemens ROX II:** Unit 42 deepread confirms 6.8/7.5/9.1 scores and the xz/-f-c-d, gpgv system(), scheduler-cron chain. Both evidence quotes verbatim (Unit 42 line + SSA-081142). Fetched Siemens SSA-081142 directly: quote "Ruggedcom Rox contains an input validation vulnerability in the Scheduler functionality that could allow an authenticated remote attacker to execute arbitrary commands with root privileges" is a contiguous substring; CVSS 9.1 and Publication Date 2026-05-12 confirmed. Classification B/1 (iter1-adjusted) acceptable. Notable priority + OT/CI nexus justify inclusion beyond routine patch cycle.

**SonicWall SMA 1000 (deep-dive, update_of):** Volexity deepread confirms the SSRF→CouchDB/UUID→execRemoveHotfix path-traversal→KNUCKLEBALL/Suo5/ORANGETAIL→tcpdump-LDAP chain and both Volexity quotes ("No valid SMA session cookie was required during this process." and "available evidence suggests the threat actor was less successful moving laterally or gaining access to other systems"). Rapid7 fetched: quote "quickly shifted to lateral movement, pivoting from the compromised appliance directly into the internal corporate network" verbatim, and CVSS 10.0/CVE labels confirmed. NVD confirms 15409=10.0 (PR:N pre-auth) and 15410=7.2 (PR:H post-auth). CISA KEV confirms both CVEs listed (status flags correct). update_of target matches prior coverage (2026-07-14 entry, same CVEs). No IOCs in body. Single concrete do-now action, not padded. The F5/F9 fixes from iter2 (Rapid7-attributed pivot, Volexity divergence surfaced) are present and correct.

**Contagious Interview / OTTERCOOKIE:** Elastic deepread confirms REF9403, community-Slack targeting, SVG-comment steganography, eval()/Check() avoiding atob()/Buffer.from, npm-cache masquerade, 500ms clipboard poll, four-stage payload, NTT-Dec-2024 OTTERCOOKIE lineage + Microsoft ref. Both evidence quotes verbatim including the iter2-fixed "These trojanized repositories at the time of writing have zero detections and are not flagged by any AV vendors". Single-source Elastic correctly flagged; classification B/2 (credibility 2, uncorroborated) correct. No IOCs (domains/hashes kept out of body).

**Abbott:** Abbott own-statement deepread confirms the primary quote verbatim ("unauthorized access to a limited number of internal systems in our Cancer Diagnostics business only"). BleepingComputer fetched: evidence quote #2 verbatim; vishing/Entra-SSO/ServiceNow/SharePoint/Databricks/Coupa, 30M+ rows, July 21 deadline all confirmed; "medical notes and orders" is a fair compression of BC's "22 million client notes ... more than 20 million medical orders". UNC6240 confirmed as registry alias of actor:shinyhunters. Classification B/3 correct (incident confirmed, actor scope a claim). Only defect: the MedTech Dive misattribution above.

**Metro Mondego:** Campeão deepread confirms primary quote verbatim, ransomware type, 6 July date, CNCS/CNPD/criminal-authority notification, passenger-payment-data-unaffected, and the passenger-fraud warning that backs the Triage line. TugaTech fetched: quote "A ação foi reivindicada pelo grupo de cibercriminosos Thegentlemen, que afirma ter conseguido extrair documentação confidencial" verbatim. Storm-2697 confirmed registry alias of actor:thegentlemen. Classification B/2 correct. Clear EU+transport nexus.

**Whole-run:** No IOCs anywhere in bodies. No vanity metrics, English throughout, no workflow-internal language. New registry keys (actor:uta0533, tool:sonicwall-sma-uta0533-toolset, campaign:contagious-interview, tool:ottercookie) all present. Dedup correct (SonicWall as update_of; no CVE/entity duplication with the 14-day index). Borderline drops (FortiSandbox, n8n, EY, Coca-Cola) documented and defensible. Coverage looks complete — no in-window relevant item I can name with a plausible source is missing. The run-record header (iter2 fix "6 = 5 new + 1 update") is correct.

### Findings summary (machine-readable)

```yaml
- code: F3
  category: claim-not-supported
  section: incident
  item: "2026-07-18/abbott-exact-sciences-shinyhunters-entra-sso-vishing"
  url_or_quote: "ShadowByt3$/LabCentral sentence cited to MedTech Dive; that article does not contain the claim — BleepingComputer does"
  summary: "Inline cite points to MedTech Dive, which lacks ShadowByt3$/LabCentral/reference-docs detail; re-cite to BleepingComputer (already source #2)."
```
