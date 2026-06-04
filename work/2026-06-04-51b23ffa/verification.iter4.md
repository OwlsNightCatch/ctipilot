**Model:** Claude Sonnet 4.6 (`claude-sonnet-4-6`)
**Timestamps:** started_at=2026-06-04T05:12:17Z · ended_at=2026-06-04T05:17:10Z · duration_seconds=293

## Verification report — briefs/2026-06-04.md (iteration 4)

Cold read by a hostile, technically-fluent Swiss/EU public-sector SOC reader. Even-iteration alt-verifier with Prior-iteration deltas block.

**URLs fetched this iteration:** Sansec (mirasvit-cache-warmer), Ammar Askar (github-token-stealing), GHSA-679G-PP8V-JVG4, SecurityWeek (Kirki/Burst), NCSC-CH Week 22 (via bridge — HTML scaffold returned, no readable body), BleepingComputer Kirki, BleepingComputer Burst Statistics, Imperva (CVE-2026-45247), Cisco PSIRT (cisco-sa-cucm-ssrf-cXPnHcW), US Treasury OFAC (sb0519) (via bridge), Huntress (DesckVB RAT), UpGuard (WFP breach), DutchNews.nl (Dutch hotels), Techzine EU (Dutch hotels), Huntress (NTLM search: leak), oss-security (HTTP/2), Calif/Codex (HTTP/2 Bomb), SecurityWeek (M365 Android), THN (M365 Android), Enclave (FlagLeft), Symantec (stock-exchange espionage), SecurityWeek (stock-exchange espionage). Total: ~22 URLs fetched.

---

### Prior-iteration delta verification

**F4 (Magento exploitation date):** CONFIRMED CLEAN. Brief now states "Sansec discovered the flaw and shipped a detection rule on 24 April under coordinated disclosure (patch 25 May); Imperva has since observed active exploitation campaigns." Sansec source confirms April 24 = discovery date. Imperva source confirms "active exploitation attempts… since disclosure on May 26, 2026." TL;DR now says "CISA KEV-listed and exploitation confirmed by Imperva" — correct and supported. CVE table row shows "Yes (Imperva; CISA KEV)" — correct. No "exploitation from 24 April" language remains.

**F4b (WordPress European targeting):** CONFIRMED CLEAN. Brief now says "under active mass-exploitation" (line 56) with no geographic qualifier. SecurityWeek and both BleepingComputer articles confirm no geographic targeting mentioned. Footer Region changed to "global" — confirmed. No "against European sites" language remains.

**F5 (NCSC hotel phishing targeting):** CONFIRMED CLEAN. Brief now states "NCSC frames the targets as Swiss hotel-booking customers generally; for a federal SOC, staff who book travel through these platforms fall in the same exposed population (analyst inference)." The analyst-inference framing correctly bounds the NCSC's own claim (a general public advisory about WhatsApp hotel-booking phishing) while being transparent about the SOC-specific inference. The NCSC bridge returned HTML scaffold only (no readable body) — consistent with prior iteration's bridge fetch. The meta description confirms NCSC's framing as a general public advisory. No unsourced Swiss-federal-employee targeting claim remains.

**F3 (github.dev mechanism):** CONFIRMED CLEAN. Brief now states "synthetic keyboard events (keydown injection) to drive the editor into silently installing a malicious workspace extension, which then reads and exfiltrates the OAuth token… Askar notes the technique does not rely on bypassing postMessage origin validation." This matches the Askar primary exactly: "synthesizes keyboard events (specifically KeyboardEvent objects via dispatchEvent)… the technique does not rely on bypassing postMessage origin validation." Clean.

**F11a (github.dev patch status):** CONFIRMED CLEAN. Brief now says "Microsoft shipped a fix on 3 June" and heading reads "Microsoft patched 3 June." Tags show "patch-available." Askar blog confirms Microsoft fix on June 3. Clean.

**F11b (MISP version):** CONFIRMED CLEAN. Brief now says "commit 39b3cb15 per the GitHub advisory" only — no version number. GHSA confirms only the commit hash, no version listed. Clean.

**F11c (MISP Evidence quote):** CONFIRMED CLEAN. The Evidence field has been removed from the MISP footer entirely. Clean.

---

### Unsupported / hallucinated facts

**F4 — "WFP took the platform offline on detection" not supported by UpGuard source (§ 1).**
Brief line 31: "WFP took the platform offline on detection."
The UpGuard source (fetched this iteration) contains no mention of the platform being taken offline. The UpGuard article states only that the breach was discovered and the breach date was May 14, 2026. There is no sentence anywhere in the article about WFP taking the application offline, shutting down the registration portal, or suspending operations. The claim is not present in any cited source for this item. The brief asserts an operational response step for a humanitarian data breach that cannot be verified.

---

### Editorial / less-is-more flags (advisory)

**F11 — Envoy patch status stale in § 5 body and § 6 Action Items (advisory).**
Brief line 112 (§ 5): "Microsoft IIS, Envoy and Cloudflare Pingora had no patch available at the time of writing."
Brief line 125 (§ 6): "for IIS, Envoy and Cloudflare Pingora (no patch) disable HTTP/2 at the edge where feasible."
The Calif/Codex blog (fetched this iteration) includes an update: "Jun 3 - Envoy released patches under advisory GHSA-22m2-hvr2-xqc8." The brief is published June 4 — one day after the Envoy patch. The TL;DR (line 9) correctly qualifies "remained unpatched at disclosure" (June 2), which is accurate. However, the § 5 body says "at the time of writing" which is ambiguous for a June 4 publication, and the § 6 Action Item actively recommends workarounds for Envoy as if no patch exists. Defenders running Envoy who read only § 6 would apply workarounds instead of patching. Recommend noting Envoy's June 3 patch in § 5 body and updating the § 6 Envoy guidance from "(no patch)" to "patch available (GHSA-22m2-hvr2-xqc8)."

---

### Coverage gaps / missed angles

**F10 — Envoy GHSA-22m2-hvr2-xqc8 patch not surfaced.**
The Envoy advisory `GHSA-22m2-hvr2-xqc8` is directly linked from the Calif/Codex blog and released June 3. SOC operators running Envoy who read this brief get told there is no patch when one exists. Suggested search: `Envoy CVE-2026-49975 GHSA-22m2-hvr2-xqc8 patch June 2026`.

---

### Everything else verified clean

- **Sansec Magento (CVE-2026-45247):** All claims confirmed — CVSS 9.8, CacheWarmer cookie, unauthenticated, fix v1.11.12, Imperva exploitation since disclosure (~May 26), CISA KEV June 3. Evidence quote verbatim from Sansec.
- **WordPress CVEs (CVE-2026-8206 / CVE-2026-8181):** Kirki versions 6.0.0–6.0.6 confirmed, fix v6.0.7 confirmed, 222+ Wordfence blocks in 24h confirmed. Burst Statistics 3.4.0–3.4.1.1 confirmed, ~7,400 attacks in 24h confirmed, fix v3.4.2 confirmed. No geographic targeting in any source. FooterRegion: global — correct.
- **Cisco PSIRT (CVE-2026-20230):** CVSS 8.6, SSRF with root file-write path, WebDialer disabled by default, Release 14 (pre-14SU6) and 15 (pre-15SU5), PoC public, no ITW confirmed — all confirmed against PSIRT advisory.
- **MISP (CVE-2026-10611):** OTP bypass with LdapAuth.mixedAuth=true + require_otp=true, fix commit 39b3cb15, CVSS 8.2 — confirmed against GHSA.
- **HTTP/2 Bomb (CVE-2026-49975):** All deep-dive claims verified — 880,000+ servers, Envoy 32GB in ~10s, nginx 1.29.8 max_headers fix, Apache mod_http2 v2.0.41, LimitRequestFields ineffective, oss-security post confirms all named mitigations.
- **Huntress NTLM search: leak:** Structural identity to CVE-2026-33829 confirmed, Microsoft Moderate rating / no CVE confirmed, crumb=location: parameter confirmed.
- **M365 Android (CVE-2026-41100/41101/41102/42832):** All CVEs confirmed via THN and Enclave blog. CVSS scores 7.7/7.1/7.1/4.4 confirmed. Teams unaffected confirmed. Fix May 12 cycle confirmed. Excel/Word/PowerPoint/Copilot/Loop/OneNote all confirmed as affected.
- **github.dev OAuth theft:** Synthetic keyboard-event mechanism confirmed. Microsoft June 3 fix confirmed. No CVE assigned (GitHub issue #319593).
- **Symantec stock-exchange espionage:** All named tools confirmed — armsvc.exe, oneservice.exe, Aspose OST stealer, Dropbox + OneDrive exfil, hard-coded Microsoft IPs, FRPC/SharpDecryptPwd/Secretsdump. Oct 2025–Mar 2026 confirmed. No attribution confirmed.
- **DesckVB RAT:** Bestellung_2026.html (German), DoubleClick hop, AMSI/ETW native-API patching all confirmed by Huntress blog.
- **Dutch hotel breach:** 100+ Dutch hotels, Belgium and Ireland reports confirmed by DutchNews and Techzine. Hospecs named. SaaS vendor unnamed (confirmed by both sources — that's accurate).
- **WFP Gaza breach:** 600,000 households, names/IDs/mobile/location, breach May 14, June 2 disclosure, "potentially largest of its kind" — all confirmed by UpGuard.
- **OFAC/Nobitex:** >50% Iranian digital-asset inflows 2025, IRGC-affiliated ransomware, EO 13224/13902, 4 Nobitex principals (Rad, Ali Aghamir, Mohammad Aghamir, Khoee), 3 other exchanges (Wallex, Bitpin, Ramzinex) — all confirmed by Treasury press release body.
- **Dedup:** No recycled prior-coverage items.
- **§ 2 inclusion gates:** CVE-2026-45247 (CISA KEV + ITW) ✓; CVE-2026-8206/8181 (ITW) ✓; CVE-2026-20230 (PoC public, pre-auth, critical-path) ✓; CVE-2026-10611 (EU/CH high-blast-radius) ✓; CVE-2026-49975 (deep dive, pre-auth DoS + 880k servers) ✓.
- **No IOCs, no vanity metrics, English throughout, no workflow language leaked.**
- **Single-source flags:** WFP Gaza [SINGLE-SOURCE] present ✓. DesckVB [SINGLE-SOURCE] present ✓. Both are research-lab/news-source single primaries; § 7 notes them.
- **Style:** taxonomy footers checked — all Tags/Region/Sector values appear within controlled vocabulary scope.

---

### Verdict

NEEDS_FIXES (truth: 1, editorial: 0, advisory: 1)

Truth: F4 (WFP platform-offline claim unsupported by UpGuard source). Advisory: F11 (Envoy patch now available since June 3, § 5 body and § 6 Action Items still say no patch for Envoy). F10 (missed angle — Envoy patch) is informational and does not block publish.

---

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "UN World Food Programme breach — Gaza households [SINGLE-SOURCE]"
  url_or_quote: "WFP took the platform offline on detection"
  summary: "UpGuard source (fetched this iteration) contains no mention of the platform being taken offline. The only cited source for this item is UpGuard, which states the breach date (May 14) and that data was exposed, but never says the platform was shut down or taken offline. Remove or replace with a sourced claim."
- code: F11
  category: editorial-advisory
  section: deep-dive
  item: "HTTP/2 Bomb CVE-2026-49975 — § 5 body and § 6 Action Items Envoy status"
  url_or_quote: "Microsoft IIS, Envoy and Cloudflare Pingora had no patch available at the time of writing / for IIS, Envoy and Cloudflare Pingora (no patch) disable HTTP/2"
  summary: "Envoy released patches on June 3 under GHSA-22m2-hvr2-xqc8 (linked from Calif/Codex blog, fetched this iteration). Brief publishes June 4. TL;DR correctly says 'at disclosure'; § 5 body and § 6 Action Items still describe Envoy as unpatched, which misleads defenders into applying workarounds instead of patching. Recommend noting Envoy June 3 patch in § 5 and updating § 6 Envoy guidance."
```
