**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-05-29T05:00:37Z · ended_at=2026-05-29T05:05:44Z · duration_seconds=307

## Verification report — briefs/2026-05-29.md (iteration 2)

### Prior-iteration delta verification (v2.53 — iter 2 protocol)

All 12 prior-iteration findings (F3 ×3, F3-Asocks, F4 ×2, F5 ×2, F8, F9, F11 ×2) were walked against fetched sources. Summary:

- **F3 (332+ victims to Check Point)**: RESOLVED. Brief line 143 reads "Check Point counts more than 332 victim organisations on the operator's leak site" — Check Point Research article confirmed to contain "332 published victims in first five months of 2026." Attribution correct.
- **F3 (GPO-spread to Check Point)**: RESOLVED. Brief attributes GPO pathway to "Check Point Research" explicitly. Microsoft article does not mention GPO; Check Point article describes the GPO technique. Correct.
- **F3 (ASR GUID removed, MS Learn cited)**: RESOLVED. GUID `d4f940ab` no longer present. Brief cites `https://learn.microsoft.com/en-us/defender-endpoint/attack-surface-reduction-rules-reference` for the "Block process creations originating from PsExec and WMI commands" rule. Page verified — rule exists, GUID `d1e49aac-8f56-4280-b9ba-993a6d77406c`. Note: GUID `d4f940ab` is for "Block all Office applications from creating child processes" — the removed GUID was incorrect; the brief now correctly names the rule without a GUID.
- **F3 (Asocks framing)**: RESOLVED. Brief frames Asocks as joining "the recent string of disrupted residential-proxy networks — SocksEscort, Aisuru/Kimwolf, FirstVPN, IPIDEA, RapperBot." Risky Business article confirmed with verbatim language: "Asocks joins a list of multiple other botnets disrupted by authorities in recent months, such as SocksEscort, Aisuru/Kimwolf, FirstVPN, IPIDEA, and RapperBot." Framing correct.
- **F4 (BTMOB technical claims trimmed)**: PARTIALLY RESOLVED. "WebSocket port 443" and "GPS geo-filter" removed. However "HTML-injected overlay phishing" and "keylogging" remain. ESET source (fetched this iteration) does not mention these capabilities; The Hacker News (also cited) does confirm "HTML injections for credential theft" and "keylogging functionality." THN is an Additional source, so these claims are technically backed. Not a blocker.
- **F4 (Carnival April 22 removed)**: RESOLVED. Date not present in brief.
- **F5 (Nuclei template cited in § 5)**: RESOLVED. Brief line 152 cites `https://github.com/projectdiscovery/nuclei-templates/blob/main/http/cves/2026/CVE-2026-35616.yaml` inline at the Vulnerable component paragraph. Template fetched and confirmed to send `X-SSL-CLIENT-VERIFY: SUCCESS`. Citation is adequate for the X-SSL-CLIENT-VERIFY claim.
- **F5 (Maine AG URL cited)**: RESOLVED. Maine AG URL cited in TL;DR line 11 and § 1 line 44. Maine AG filing confirmed: 5,995,277 total individuals, breach occurred April 10, 2026, discovered April 14.
- **F8 (8.7M vs 5.99M)**: RESOLVED. Brief line 44 includes the reconciliation sentence; The Register cited as the source for the HIBP 8.7M figure.
- **F9 (GitLab § 7 contradiction)**: RESOLVED. § 7 lines 196-197 contain the contradiction note. GitLab release page confirmed 7 CVEs (including CVE-2026-2710 CVSS 4.3).
- **F11 (editorial advisories)**: Not blockers, carried as-is.

---

### Citation does not support the claim

**F1** — **§ 1 Carnival H3 — "Initial access on 2026-04-14 was social engineering"**

The brief states (line 44): "Initial access on 2026-04-14 was social engineering against a single employee account."

The PR Newswire source (`https://www.prnewswire.com/news-releases/carnival-corporation-notice-of-data-breach-302783524.html`) says: "On April 14, 2026, the company's IT security team *identified* unauthorized activity involving an employee's account, when an unauthorized actor used social engineering to deceive an employee." April 14 is the detection/identification date per Carnival's own notice.

The Maine AG filing (`https://www.maine.gov/agviewer/content/ag/985235c7-cb95-4be2-8792-a1252b4f8318/d6729ef2-7bb3-42d3-abdd-99a1dd8f2415.html`) states the breach *occurred* on **April 10, 2026** and was *discovered* on April 14, 2026.

The brief conflates the discovery date (April 14) with the initial-access date. Per Maine AG, initial access was April 10, not April 14.

**Severity:** F3 (citation does not support claim). The PR Newswire notice — the cited source — explicitly frames April 14 as when the security team *identified* the activity (discovery), not when it happened. The actual initial access date (April 10) is in the Maine AG filing, also cited.

### Surface contradiction

**F2** — **§ 1 Carnival H3 — April 10 vs. April 14 initial access**

Source A (PR Newswire, also cited): "On April 14, 2026, the company's IT security team identified unauthorized activity involving an employee's account." — frames April 14 as discovery.

Source B (Maine AG filing, also cited): Breach date: April 10, 2026; Discovery date: April 14, 2026.

The brief currently says "Initial access on 2026-04-14 was social engineering" which picks April 14 but labels it as "initial access" rather than "discovery." The two cited sources agree that April 14 is the discovery date, not the initial-access date. Brief should say "discovered 2026-04-14; breach occurred 2026-04-10 per Maine AG filing" or drop the date and say "social engineering against a single employee account" without a date.

This is the same finding as F1 above — filing both as F3 (citation claim mismatch) and F9 (contradiction between sources creating a misleading claim) to surface the remediation path clearly.

### Needs more research

**F3** — **§ 3 Grandoreiro + BTMOB — BTMOB Iberian-banking framing not in cited sources**

The brief (line 132-134) says: "BTMOB is the parallel Android-targeting half of the same Iberian-banking pressure wave."

Sources checked:
- ESET WeLiveSecurity (`https://www.welivesecurity.com/en/malware/btmob-stealthy-rat-burrowing-deep-android-devices/`, fetched this iteration): Geographic focus is **Argentina, Brazil, Latin America**. "Campaigns impersonating Argentine tax and customs authorities." No mention of Spain or Portugal.
- WatchGuard Secplicity (`https://www.watchguard.com/wgrd-security-hub/secplicity-blog/grandoreiro-malware-campaign-targets-europe-and-latin-america`, fetched this iteration): Does not mention BTMOB at all.
- The Hacker News (`https://thehackernews.com/2026/05/grandoreiro-malware-and-btmob-rat.html`, fetched this iteration): Notes BTMOB targets "mobile users in Brazil" and says "No mention of BTMOB targeting Iberian banks specifically."

The "Iberian-banking pressure wave" framing is an analytical connection the brief makes that no cited source asserts. This is not technically F13 (analytical-link-as-fact) because the BTMOB item is hedged as "parallel" — but the framing could mislead Swiss/EU defenders into thinking BTMOB is a Spain/Portugal threat when the sources indicate Latin American targeting. Recommend softening "Iberian-banking pressure wave" to "Latin American banking pressure wave, with Grandoreiro extending into Portugal and Spain" or remove the BTMOB-as-Iberian-parallel framing.

**Advisory severity** (F8-class): The claim isn't factually wrong in a way that harms defenders, but the geographic characterisation is unsupported by the ESET source.

### Analytical-link-as-fact

No new F13 findings. The BTMOB framing is better characterized as F8 (needs more precision) than F13 (asserted connection that no source makes), because the brief uses "parallel" as a hedge and Grandoreiro *is* Iberian-targeting per WatchGuard.

### Verdict

NEEDS_FIXES (truth: 1, editorial: 1, advisory: 0)

- **F1/F3-class (truth):** "Initial access on 2026-04-14" in § 1 Carnival H3 and TL;DR is contradicted by the cited Maine AG source which shows April 10 as breach date and April 14 as discovery. The brief conflates the two dates.
- **F2/F9-class (editorial):** Contradiction between PR Newswire (frames April 14 as identification) and Maine AG (April 10 breach / April 14 discovery) should be surfaced in § 7 per the brief's own contradiction-logging policy.
- **F3/F8-class (editorial):** BTMOB "Iberian-banking pressure wave" not supported by ESET or WatchGuard sources; ESET focuses on Argentina/Brazil.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3
  category: claim-not-supported
  section: active-threats
  item: "Carnival Corporation — ShinyHunters breach"
  url_or_quote: "Initial access on 2026-04-14 was social engineering against a single employee account"
  summary: "PR Newswire frames April 14 as discovery date ('IT security team identified unauthorized activity'); Maine AG filing says breach occurred April 10, discovered April 14. Brief labels April 14 as 'initial access' but both cited sources indicate it is the discovery date."
- code: F9
  category: surface-contradiction
  section: active-threats
  item: "Carnival Corporation — ShinyHunters breach"
  url_or_quote: "Initial access on 2026-04-14 was social engineering"
  summary: "Source A (PR Newswire): April 14 = discovery date. Source B (Maine AG filing): April 10 = breach date, April 14 = discovery date. Brief silently picks April 14 and labels it initial-access without surfacing the discrepancy. Recommend: change to 'social engineering gained access on 2026-04-10; discovered 2026-04-14 per Maine AG filing' or add § 7 contradiction entry."
- code: F8
  category: needs-more-research
  section: research
  item: "Grandoreiro + BTMOB — § 3 H3"
  url_or_quote: "BTMOB is the parallel Android-targeting half of the same Iberian-banking pressure wave"
  summary: "ESET source focuses on Argentina/Brazil/Latin America; WatchGuard does not mention BTMOB; THN says BTMOB targets Brazil. No cited source frames BTMOB as part of an Iberian-banking campaign. Soften framing or source explicitly."
```
