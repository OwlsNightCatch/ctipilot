**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-02T04:51:54Z · ended_at=2026-06-02T04:56:01Z · duration_seconds=247
**Self-telemetry:** urls_checked=19 · webfetch_calls=15 · bridge_fetches=1

## Verification report — briefs/2026-06-02.md (iteration 2)

### Prior-iteration delta walk (F3, F13, F9, F11a, F11b)

**F3 (Disig EUVD re-anchor) — VERIFIED CORRECT.** The §2 Disig item now leads with ENISA EUVD EUVD-2026-33648 as the primary Source and the Disig vendor advisory as Additional source. The dropped specifics (slovensko.sk, "primary QTSP in Slovakia", researcher name, eIDAS-legal-binding framing) are absent from the current brief. The Disig vendor advisory page confirms: CVE-2026-8931 implied (the page describes a critical security vulnerability in Web Signer 2.0.3–2.5.3 fixed in 2.5.5, and credits Marek Alakša as discoverer — does NOT name the CVE, CVSS, or SK-CERT, consistent with iter-1's finding). The EUVD page remains SPA-only and unverifiable by any fetch path. The item now correctly attributes the CVE/CVSS/RCE/SK-CERT claims to EUVD, which is the authoritative record even if it cannot be HTML-fetched. Remediation correctly applied; the limitation is inherent to EUVD's SPA architecture and was noted in iter-1.

**F13 (SteppeDriver/UNC5221 attribution) — PARTIALLY REMEDIATED; RESIDUAL DEFECT.** See F1 below. The main agent added a caveat but the framing still attributes to THN a "link" that THN does not assert. THN's article, per my fetch, presents Dragon Weave, SteppeDriver, and UNC5221 as distinct separate actor clusters with no stated connection between them. The brief says "The link to previously documented SteppeDriver and UNC5221 tooling comes from The Hacker News's broader China-nexus roundup" — this implies THN established a tooling connection, but THN made no such connection.

**F9 (Miasma download count) — VERIFIED CORRECT.** Brief now reads "Wiz puts the combined weekly downloads at roughly 80,000, while Aikido counts closer to 117,000." I confirmed: Wiz article says "~80,000 weekly downloads"; Aikido article says "116,991 times per week." Both figures correctly attributed to their sources. Remediation correctly applied.

**F11a (WP Maps Pro BleepingComputer date) — VERIFIED CORRECT.** Footer cites BleepingComputer as primary with date 2026-05-31; the BleepingComputer article is dated May 31, 2026 per my fetch. CVSS 9.8 attributed to The Hacker News in body text — THN confirms CVSS 9.8. Remediation correctly applied.

**F11b (Charter §4 vishing/Entra/Salesforce framing) — VERIFIED CORRECT.** The sentence now reads "As established in prior coverage of the broader ShinyHunters Salesforce campaign, the access pattern is vishing-driven compromise of an employee Microsoft Entra account followed by a Salesforce export." The phrase "As established in prior coverage" correctly signals this claim rests on prior-coverage context, not the cited Security Affairs article. The Security Affairs source does mention Salesforce and vishing, providing partial corroboration. Remediation correctly applied.

---

### Broken / unreachable URLs

No broken or 404 URLs found. All URLs fetched in this iteration resolved. The BSI CERT-Bund advisory page rendered minimal content (SPA/portal architecture) but the URL resolved and the host is the canonical German government advisory system. The EUVD ENISA page and MSRC advisory page both render as SPAs — these are known issues with those platforms, not a defect in the brief.

---

### Analytical-link-as-fact

**F1 — §5 Dragon Weave attribution paragraph: "the link to SteppeDriver and UNC5221 tooling" attributed to THN, but THN asserts no such link.**

Claim quoted: "The link to previously documented **SteppeDriver** and **UNC5221** tooling comes from The Hacker News's broader China-nexus roundup, not from Seqrite's own report ([The Hacker News, 2026-06-01](https://thehackernews.com/2026/06/china-aligned-groups-ramp-up-attacks.html))"

What THN actually says (per my fetch): "The article presents these as distinct threat actors with no explicit connections between Dragon Weave and the other two groups." SteppeDriver is described as "a separate unreported cluster first discovered in 2024." UNC5221 is mentioned separately with the PhiliKit toolkit. Neither is linked to Dragon Weave in THN's text.

The word "link" in the brief implies THN established a tooling connection or overlap between Dragon Weave and SteppeDriver/UNC5221. THN did not. The caveat that follows ("treat that grouping as the secondary source's framing rather than a confirmed attribution") partially mitigates harm, but the opening clause still misrepresents what THN says. The main agent's remediation in iter-1 added the caveat but left the "link...tooling" framing intact.

**Fix:** Replace "The link to previously documented SteppeDriver and UNC5221 tooling comes from The Hacker News's broader China-nexus roundup, not from Seqrite's own report" with: "The Hacker News's broader China-nexus roundup covers SteppeDriver and UNC5221 as separate actor clusters in the same reporting window — these are distinct from Dragon Weave; Seqrite names no group, and no source in this item connects Dragon Weave to either of those clusters."

---

### Claims missing inline citation

**F2 — §0 TL;DR: "netlogon.dll" filename not supported by cited source.**

Claim quoted: "Belgium's national CSIRT (CCB) confirmed in-the-wild exploitation on 1 June against the stack-based buffer overflow in `netlogon.dll` that yields SYSTEM on any domain controller without authentication ([BleepingComputer, 2026-06-01](https://www.bleepingcomputer.com/news/microsoft/critical-windows-netlogon-remote-code-execution-flaw-now-exploited-in-attacks/))"

Per my fetch of BleepingComputer: "The article explicitly states Microsoft described it as 'a stack-based buffer overflow in Windows Netlogon' but does not specifically mention 'netlogon.dll' by filename." The specific DLL filename `netlogon.dll` is not in the cited BleepingComputer article. The MSRC advisory (also cited later in the Immediate Action) is an SPA and could not be content-verified. The Help Net Security article links to an aretiq.ai research page that may name the specific DLL, but that source is not cited in this sentence.

The TL;DR cites only BleepingComputer for this sentence. The filename `netlogon.dll` is unsourced at the point of citation.

**Fix:** Either (a) remove the specific DLL name (`netlogon.dll`) from the TL;DR and say "stack-based buffer overflow in the Windows Netlogon service," consistent with what BleepingComputer says, or (b) add an inline citation to a source that names the DLL explicitly (e.g., the aretiq.ai research URL surfaced in Help Net Security's article).

---

### Verdict

NEEDS_FIXES (truth: 2, editorial: 0, advisory: 0)

- F1 is truth-class (F13 analytical-link-as-fact: the "link to SteppeDriver/UNC5221 tooling" phrase implies a connection THN does not make).
- F2 is truth-class (F5 missing citation: `netlogon.dll` DLL name not in the cited BleepingComputer article).
- Both findings are specific, quoted, and backed by sources fetched in this iteration.
- All five prior-iteration deltas verified: F3 and F13-remediation partially correct (F13 residual now raised as F1 above), F9/F11a/F11b fully resolved.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F13
  category: analytical-link-as-fact
  section: deep-dive
  item: "Operation Dragon Weave — Attribution paragraph"
  url_or_quote: "The link to previously documented SteppeDriver and UNC5221 tooling comes from The Hacker News's broader China-nexus roundup"
  summary: "THN article presents SteppeDriver, UNC5221, and Dragon Weave as distinct separate actors with no stated connection between them. The phrase 'link to...tooling' implies THN asserted a tooling overlap that THN did not assert. Caveat in brief partially mitigates but opening clause misrepresents THN. Fix: rewrite to say THN's roundup covers these as separate clusters, no connection to Dragon Weave established."
- code: F5
  category: missing-citation
  section: tl-dr
  item: "CVE-2026-41089 Windows Netlogon — TL;DR bullet"
  url_or_quote: "stack-based buffer overflow in `netlogon.dll` that yields SYSTEM on any domain controller"
  summary: "The specific DLL filename 'netlogon.dll' is not present in the cited BleepingComputer article (confirmed by fetch). BleepingComputer says only 'stack-based buffer overflow in Windows Netlogon'. Remove the DLL filename or add an inline citation to a source that names it explicitly."
```
