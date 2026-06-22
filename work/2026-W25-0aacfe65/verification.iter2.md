**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-21T23:42:42Z · ended_at=2026-06-21T23:48:41Z · duration_seconds=359

## Verification report — briefs/weekly/2026-W25.md (iteration 2)

**Prior-iteration deltas (iter 1 → iter 2) verification:**

All seven iter-1 remediations verified correct:
- F3 (DORA §7): §7 now reads "roughly one-third had cross-border impact" with the ESA "borderless and interconnected" quote. EBA and EIOPA sources fetched and confirmed — both match. PASS.
- F4 (Check Point §7): The 20.7% EU figure is gone; Switzerland Akira ~31% and Germany #2 (Emsisoft) remain. Check Point source confirms Akira 31% for Switzerland; Emsisoft source confirms "Germany moved into the #2 position." PASS.
- F5 (INC §6): Germany #2 figure absent from §6. PASS.
- F4 (INC §6): No NHS Dumfries & Galloway / Alder Hey victim names in §6; replaced with "non-US targets; healthcare/education/legal sectors." PASS.
- F4 (SocGholish §8): "over 100 servers and 14,971 WordPress sites remediated" — Proofpoint source confirmed: "over 100 servers and domains worldwide" and "14,971 websites were remediated." PASS.
- F14 (Council of Europe §0/§2): §0 reads "a European institution of which Switzerland is a member"; §2 reads "the only named European-institution victim to date per W1's assessment." No bare "first" quantifier remains. PASS.
- F11 (GTIG date §2): Explicit date for the GTIG mention is absent from the inline text and footer. PASS.

---

### Broken / unreachable URLs

No broken / DNS-fail / 404 URLs found across the items tested. All primary sources resolved successfully.

---

### Generic / oversight URLs (replace with specific article)

No generic URL defects found. All cited source URLs land on specific articles or advisories.

---

### Citation does not support the claim

**F1.** §8 SocGholish — "five FakeUpdates-style clusters remain fully operational"

Claim (brief, §8): "five FakeUpdates-style clusters remain fully operational — TA2726, TA2727, ZPHP, ErrTraffic (the ClickFix MaaS in § 6) and LandUpdate808/KongTuke"

Cited source: [Proofpoint](https://www.proofpoint.com/us/blog/threat-insight/sayonara-socgholish-operation-endgame-disrupts-major-cybercrime-operation) (fetched this iteration)

Proofpoint's actual text: "The action took down over 100 servers and domains worldwide" and it identifies **seven** still-active clusters: "TA2726, TA2727, ZPHP, ErrTraffic, LandUpdate808 (also known as KongTuke), **GeoTDS, and tdsshop** threat clusters." The brief's count of "five" omits GeoTDS and tdsshop — both named by Proofpoint as remaining operational. The brief's list is incomplete relative to the primary source.

**F2.** §9 EDPB — "a structured ~120-field form across seven sections"

Claim (brief, §9): "The template is a structured ~120-field form across seven sections, designed to replace the current patchwork in which a multi-jurisdiction breach can require navigating up to 27 different national DPA forms."

Cited source: [EDPB](https://www.edpb.europa.eu/news/news/2026/edpb-meets-eu-commissioner-mcgrath-and-adopts-common-data-breach-notification_en) (fetched via bridge this iteration)

The EDPB press release states the template provides "predefined options to choose from" and "guidance on how to fill in the fields" but does **not** mention "~120 fields," "seven sections," or "27 different national DPA forms" anywhere in the retrieved text. The template PDF itself (linked from the press release) returned HTTP 403 and could not be verified. The specific structural details (~120 fields, seven sections, 27 DPA forms) do not appear in the cited source and cannot be confirmed.

**F3.** §9 NCSC-CH — e-vignette campaign

Claim (brief, §9): "a parallel email campaign abuses the Swiss e-vignette motorway scheme ([NCSC-CH, 2026-06-16])"

Cited source: [NCSC-CH Week 24 Wochenrückblick](https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_24.html) (fetched this iteration)

The fetched NCSC-CH page covers the fake Swiss Post QR-code letterbox campaign ("Avis de passage") in detail. The e-vignette motorway scheme is **not mentioned** on the retrieved page. The "Avis de passage" campaign and e-vignette campaign appear to be conflated, or the e-vignette claim is sourced elsewhere but cited to the NCSC-CH URL which doesn't carry it.

---

### Unsupported / hallucinated facts

**F4.** §6 Mastra — "88 minutes"

Claim (brief, §6): "published 140+ malicious `@mastra` packages in 88 minutes"

Cited sources: [Microsoft Security — Mastra](https://www.microsoft.com/en-us/security/blog/2026/06/17/postinstall-payload-inside-mastra-npm-supply-chain-compromise/) (fetched this iteration) and [BleepingComputer](https://www.bleepingcomputer.com/news/security/microsoft-links-mastra-ai-supply-chain-attack-to-north-korean-hackers/) (fetched this iteration)

Microsoft's primary source states the packages were published in a "~20-minute window (01:20 UTC on June 17)." The BleepingComputer secondary does not mention 88 minutes either. Neither cited source uses the "88 minutes" figure; the Microsoft primary says approximately 20 minutes. "88 minutes" appears nowhere in any cited source and contradicts the primary's stated timeline.

**F5.** §2 Klue/Icarus — "Sprout Social" victim

Claim (brief, §2): "the named victim list had grown to include Huntress, Recorded Future, Tanium, Jamf and Sprout Social"

Cited sources: [Klue incident update](https://klue.com/blog/an-update-on-recent-klue-security-incident) (fetched this iteration) and [Huntress](https://www.huntress.com/blog/klue-breach-investigation) (fetched this iteration)

The Klue blog post does not mention Sprout Social or any specific victim names. The Huntress investigation names Huntress, Recorded Future, Tanium, and Jamf as the confirmed victim set — **Sprout Social is not mentioned**. "Sprout Social" does not appear in either cited primary source as a confirmed victim in the Klue/Icarus incident.

---

### Claims missing inline citation

No new F5 findings beyond those surfaced in F2/F3 above (the structural EDPB template details and e-vignette claim are implicitly missing citations since the cited sources don't carry them).

---

### Strengthen primary source

No F6 findings. All CVE-sourced items lead with vendor PSIRT / vendor research-lab sources, not NVD.

---

### Drop (low relevance / off-audience / not weekly content)

No F7 findings. All items either answer "inaction = incident," "cross-day pattern," or "strategic horizon" per W-PD-1.

---

### Needs more research

No F8 findings that would materially change the brief's accuracy or operational value.

---

### Surface contradiction

No new contradictions beyond the existing one documented in §11 (PAN-OS CVE-2026-0257 Impacket detail). That contradiction is already disclosed in §11 Verification & coverage notes.

---

### Missed angles

**F6.** The brief covers Rockwell FLEX I/O CVEs (§3) but does not address the corresponding NCSC-CH advisory cross-referencing these for Swiss OT operators, nor the companion ENISA ICS alert published during the week. A search for "ENISA ICS advisory June 2026 Rockwell" might surface whether ENISA issued guidance that would strengthen the CH/EU nexus already noted.

---

### Editorial / less-is-more flags (advisory)

**F7.** §2 Gentlemen / ESET date: the brief states "On 2026-06-19 ESET published a months-long investigation" but the ESET WeLiveSecurity article is dated "18 Jun 2026." Minor one-day discrepancy, advisory only.

**F8.** §9 NCSC-CH Week 24 item is somewhat thin relative to the other §9 items, covering only a brief paragraph about the physical QR phishing campaign. If e-vignette detail is confirmed via a different NCSC-CH publication or another source, it would strengthen the paragraph.

---

### Single-source items missing [SINGLE-SOURCE] flag

No additional F12 findings. The brief's §11 already documents single-source items: HCRG Care Group, One Medical 8.8 TB figure. National-authority carve-outs are explicitly noted (EDPB, EC/ENISA CRA, NCSC-CH, G7/ANSSI).

---

### Analytical-link-as-fact

No F13 findings. The brief correctly attributes analytical conclusions (Council of Europe "per W1's assessment," NoName attribution to "group's Telegram self-claim," Krebs attribution as "analytical claim, not an indictment").

---

### Quantifier without source

No remaining F14 findings beyond those surfaced above. The iter-1 F14 (Council of Europe "first") was remediated correctly. The "five clusters" issue is classified under F3 (citation does not support claim) since the source names 7 not 5.

---

### Name-collision unflagged

No F15 findings. No name-collision issues identified across the 41 H3 items.

---

### Verdict

NEEDS_FIXES (truth: 4, editorial: 2, advisory: 2)

Truth findings:
- F1: §8 SocGholish five-cluster count — source says 7; brief says 5 (2 omitted)
- F2: §9 EDPB "~120-field form across seven sections / 27 DPA forms" — not in cited source
- F3: §9 NCSC-CH e-vignette claim — not on the cited NCSC-CH page
- F4: §6 Mastra "88 minutes" — contradicts cited Microsoft source (~20 min); neither cited source uses this figure
- F5: §2 "Sprout Social" victim — not in either cited primary source

(Counts: truth includes F1+F2+F3+F4+F5 = 5; editorial = F6 missed angle; advisory = F7 date + F8 thin paragraph)

Revised count: **truth: 5, editorial: 1, advisory: 2**

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: long-running-campaigns
  item: "SocGholish / TA569 — Operation Endgame seized 106 servers"
  url_or_quote: "five FakeUpdates-style clusters remain fully operational — TA2726, TA2727, ZPHP, ErrTraffic (the ClickFix MaaS in § 6) and LandUpdate808/KongTuke"
  summary: "Proofpoint source names 7 still-operational clusters: TA2726, TA2727, ZPHP, ErrTraffic, LandUpdate808/KongTuke, GeoTDS, and tdsshop. Brief omits GeoTDS and tdsshop; count 'five' is incorrect. Fix: update to 'seven' and add GeoTDS and tdsshop to the named list."

- code: F3
  category: claim-not-supported
  section: policy-regulatory-horizon
  item: "EDPB adopts a harmonised GDPR Article 33 breach-notification template"
  url_or_quote: "The template is a structured ~120-field form across seven sections, designed to replace the current patchwork in which a multi-jurisdiction breach can require navigating up to 27 different national DPA forms."
  summary: "The cited EDPB press release does not mention '~120 fields', 'seven sections', or '27 different national DPA forms'. The template PDF (linked from press release) returned 403. These structural details are not supported by the cited source. Fix: remove or replace unsupported structural specifics with what the cited source actually says ('predefined options', 'guidance on how to fill in the fields')."

- code: F3
  category: claim-not-supported
  section: policy-regulatory-horizon
  item: "NCSC-CH — fake Swiss Post 'Avis de passage' QR-code phishing"
  url_or_quote: "a parallel email campaign abuses the Swiss e-vignette motorway scheme ([NCSC-CH, 2026-06-16])"
  summary: "The cited NCSC-CH Week 24 Wochenrückblick page covers the QR-code letterbox phishing campaign but does not mention the e-vignette scheme. Fix: either remove the e-vignette claim or cite a source that carries it."

- code: F4
  category: hallucinated-fact
  section: research-threat-actor-developments
  item: "DPRK Sapphire Sleet escalates npm supply-chain attacks with the Mastra compromise"
  url_or_quote: "published 140+ malicious @mastra packages in 88 minutes"
  summary: "Neither cited source (Microsoft Security blog or BleepingComputer) uses '88 minutes'. Microsoft's primary states '~20-minute window (01:20 UTC on June 17)'. Fix: replace '88 minutes' with '~20 minutes' or 'within a 20-minute window' per the Microsoft primary."

- code: F4
  category: hallucinated-fact
  section: multi-day-campaigns
  item: "Klue / Icarus — one dormant integration credential cascades into multi-tenant Salesforce CRM theft"
  url_or_quote: "the named victim list had grown to include Huntress, Recorded Future, Tanium, Jamf and Sprout Social"
  summary: "Sprout Social does not appear in the Klue blog post or the Huntress investigation report (the two named primary sources). Huntress names Recorded Future, Tanium, and Jamf only. Fix: remove 'Sprout Social' from the victim list or cite a source that confirms it."

- code: F10
  category: missed-angle
  section: vulnerability-rollup
  item: "CVE-2026-0647 et al. — Rockwell Automation FLEX I/O"
  url_or_quote: "Rockwell disclosed five ICS CVEs on 2026-06-16"
  summary: "The brief cites CISA ICS-CERT and NCSC-CH for the Rockwell advisory but does not note whether ENISA published a companion ICS guidance for EU operators during the window. Suggested search: 'ENISA ICS advisory Rockwell FLEX I/O June 2026'."

- code: F11
  category: editorial-advisory
  section: multi-day-campaigns
  item: "The Gentlemen (Storm-2697) — EDR-killer framework documented, OT-adjacent victim claimed, operator named"
  url_or_quote: "On 2026-06-19 ESET published a months-long investigation"
  summary: "ESET WeLiveSecurity article is dated 18 Jun 2026, not 19 Jun 2026. One-day discrepancy. Advisory fix only."

- code: F11
  category: editorial-advisory
  section: policy-regulatory-horizon
  item: "NCSC-CH — fake Swiss Post 'Avis de passage' QR-code phishing"
  url_or_quote: "a parallel email campaign abuses the Swiss e-vignette motorway scheme"
  summary: "If the e-vignette claim is removed (per F3 above), the paragraph should be reviewed for completeness. The NCSC-CH Week 24 content about QR-code phishing stands on its own without the e-vignette detail."
```
