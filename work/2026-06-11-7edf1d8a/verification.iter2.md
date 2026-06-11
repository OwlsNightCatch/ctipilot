**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-11T04:43:00Z · ended_at=2026-06-11T04:46:38Z · duration_seconds=218
**Self-telemetry:** urls_checked=20 · webfetch_calls=14 · bridge_fetches=2

## Verification report — briefs/2026-06-11.md (iteration 2)

### Prior-iteration delta review (F3 / F14 remediation check)

**F3 remediation (RoguePlanet / NCSC-CH 12622):** The GreatXML clause has been removed. The brief now reads: "NCSC-CH GovCERT consolidated this disclosure alongside the researcher's prior 2026 Defender drops — BlueHammer, RedSun, UnDefend, YellowKey and GreenPlasma." BleepingComputer (fetched this iteration) confirms all five names; SecurityWeek also confirms. The NCSC-CH bridge returns a JavaScript SPA shell for posts 12621 and 12622 — neither post's actual content can be retrieved through the bridge or directly. The claim about NCSC-CH listing those five names therefore remains attributed to NCSC-CH 12622 without direct verification; however it is independently supported by two other fetched sources. The NCSC-CH posts are noted as unverifiable in this iteration — not a truth defect given the corroboration.

**F14 remediation (ServiceNow exploitation window):** The brief now says "2–4 June" in both the TL;DR and the § 1 item body. BleepingComputer (fetched) says "Anomalous activity was observed from 2–4 June from a single source IP." The Hacker News (fetched) says "June 2, 2026 (malicious activity commenced)." Both confirm 2–4 June. The action-items section says "2–5 June window" — the additional day represents the patch date (5 June), framed as "first activity through the 5 June patch," which is editorially defensible. No per-tenant request count remains. Both F3 and F14 remediations are correct.

---

### Citation does not support the claim

**F1 — GreenPlasma assigned wrong CVE (§ 1 RoguePlanet item)**

The brief states: "hours after Microsoft patched two of the researcher's earlier disclosures (YellowKey/CVE-2026-45585 and GreenPlasma/CVE-2026-50507) in June Patch Tuesday."

BleepingComputer June 2026 Patch Tuesday article (fetched this iteration) explicitly states: "CVE-2026-45586 is assigned to the 'GreenPlasma' zero-day, a Windows CTFMON privilege escalation vulnerability." The state-summary confirms: CVE-2026-45586 = "Windows CTFMON elevation of privilege, publicly disclosed, June 2026 Patch Tuesday." CVE-2026-50507 is separately defined as "Windows BitLocker physical-access bypass, publicly disclosed, June 2026 Patch Tuesday" — that is the BitLocker bypass, not GreenPlasma. The SecurityWeek RoguePlanet article also lists CVE-2026-45586 among the RoguePlanet-context entities and does not associate CVE-2026-50507 with GreenPlasma.

Correct attribution: GreenPlasma = CVE-2026-45586; CVE-2026-50507 = BitLocker bypass (CVE-2026-50507 is YellowKey's companion, not GreenPlasma's).

Note: YellowKey/CVE-2026-45585 is confirmed correct. Only the GreenPlasma CVE number is wrong.

### BleepingComputer date annotation in § 4 UPDATE

**F2 — Incorrect date annotation on BleepingComputer Netlogon article (§ 4 UPDATE)**

The brief writes: "[BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/microsoft/critical-windows-netlogon-remote-code-execution-flaw-now-exploited-in-attacks/)"

That article's publication date is June 1, 2026 (updated June 2, 2026). The article is about CCB's June 1 warning. It is not a June 10 article. The brief annotates it as 2026-06-10, which is the date of the CERT-EU advisory, not the BleepingComputer article. The correct annotation should be "(BleepingComputer, 2026-06-01)."

This is an editorial annotation error — the URL itself resolves to a valid, relevant article — but the date label misleads readers about recency of the cited source.

---

### Whole-brief checks

**Coverage shape:** § 1 leads with ServiceNow (public-sector CH/EU relevance) and RoguePlanet (universal Windows fleet). § 2 covers CVE-2026-5027 (Langflow, exploited ITW with ~7,000 exposed instances). § 3 research includes Black Lotus Labs JDY botnet and CrowdStrike annual report. § 4 UPDATE on CVE-2026-41089 Netlogon ITW confirmation. § 5 deep dive on ShinyHunters PeopleSoft. Inclusion gates for § 2: CVE-2026-5027 is confirmed exploited ITW (VulnCheck honeypots cited), with CVSS 8.8 and pre-auth path — gate satisfied. CVE-2026-41089 is carried as § 4 update only (not a new § 2 entry) with a summary table cross-reference — appropriate for an update item. Shape is correct.

**Style / no IOCs:** IP address "51.159.98.241" does not appear in the brief text (it was in BleepingComputer's article but not carried into the brief). No SHA hashes, attacker domains, or rule code. No workflow-internal language. Clean.

**Dedup check:** CVE-2026-41089 was in 2026-W23 weekly as "disclosure-only coverage." The § 4 UPDATE is appropriate as a delta (now ITW-confirmed). ShinyHunters PeopleSoft — not in any prior daily brief. ServiceNow — not in prior coverage. RoguePlanet — not in prior coverage (Nightmare Eclipse was covered as a CVE list under 2026-05 but RoguePlanet itself is new). EDPB template — not covered previously. Black Lotus Labs JDY — not covered previously. CrowdStrike report — not covered previously. No recycled items found.

**Single-source items:** CrowdStrike § 3 entry correctly carries `[SINGLE-SOURCE]` in the heading and a § 7 note flagging the axios element as single-source vendor. The § 3 item itself covers a periodic report — PD-9 treatment. No unflagged single-source items detected beyond what's already flagged.

**F15 / Name-collision check:** The brief does not use any of the known name-collision candidates from the prior week (Shai-Hulud, etc.). No name-collision issue detected.

**F13 / Analytical-link-as-fact check:** No unsourced connections asserted as cited. The ShinyHunters deep dive appropriately frames the gadget-chain claims as "attacker-asserted rather than vendor-confirmed." The CCB/CERT-EU Netlogon attribution is directly sourced.

**F14 / Quantifier-without-source check:** "roughly 7,000 instances are internet-exposed" — confirmed: BleepingComputer Langflow article says "~7,000 publicly exposed instances" and source cites Censys. "more than doubled from roughly 650 bots in January 2024 to over 1,500" — Lumen Black Lotus Labs article confirms "expanded from 650 to over 1,500." "100+ organisations across ~300 instances" — BleepingComputer PeopleSoft article confirms "300 instances across over 100 organizations." "more than 58%" — CrowdStrike report confirms "58% state-sponsored intrusions." "47% of state-sponsored hands-on-keyboard activity" — CrowdStrike report confirms "47% of DPRK state-sponsored manual operations (FAMOUS CHOLLIMA)." All major quantifiers are sourced.

**JDY scanning spike timing:** The brief says "scanning of Fortinet devices spiked within hours of the public disclosure of CVE-2026-35616." Lumen Black Lotus Labs article says the spike date was "April 2-5, 2026" for CVE-2026-35616. The brief's "within hours" framing appears to be an editorial characterisation not directly quoted from the Lumen source, which describes the spike as occurring within days of disclosure, not explicitly "within hours." However, the Lumen source does describe it as a "sub-24-hour" pattern in the context of a "rapid vulnerability exploitation" report. The "hours" language is the brief's synthesis, not a quoted stat. This is borderline — the source establishes rapid weaponisation but "within hours" is not a verbatim claim. Borderline F11 (editorial advisory), not a truth defect.

**Missed angles (F10):**
The ServiceNow item notes "activity was from a single source IP" — this is mentioned in the BleepingComputer source as IP 51.159.98.241 (a French hosting provider). Attribution/actor behind the activity is not explored in the brief; given ServiceNow's "likely researchers" framing this is an open question worth noting for defenders but not a gap that must be addressed.

---

### Verdict

The single significant truth defect is the wrong CVE assigned to GreenPlasma (CVE-2026-50507 in the brief; correct is CVE-2026-45586). The date annotation error on the BleepingComputer Netlogon article (2026-06-10 versus actual 2026-06-01) is an editorial annotation error. All prior-iteration remediations (F3 and F14) are confirmed correct.

**NEEDS_FIXES (truth: 1, editorial: 1, advisory: 0)**

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "RoguePlanet Microsoft Defender zero-day"
  url_or_quote: "YellowKey/CVE-2026-45585 and GreenPlasma/CVE-2026-50507"
  summary: "GreenPlasma is CVE-2026-45586 (Windows CTFMON priv-esc), not CVE-2026-50507 (which is the BitLocker bypass). BleepingComputer June 2026 Patch Tuesday article explicitly assigns CVE-2026-45586 to GreenPlasma. Correct the CVE number for GreenPlasma in the RoguePlanet item body."
- code: F11
  category: editorial-advisory
  section: updates
  item: "UPDATE: Windows Netlogon RCE CVE-2026-41089"
  url_or_quote: "[BleepingComputer, 2026-06-10](https://www.bleepingcomputer.com/news/microsoft/critical-windows-netlogon-remote-code-execution-flaw-now-exploited-in-attacks/)"
  summary: "Date annotation '2026-06-10' is incorrect — the BleepingComputer article was published June 1, 2026 (updated June 2). Should be annotated '(BleepingComputer, 2026-06-01)' to avoid misleading readers about recency of the cited source."
```
