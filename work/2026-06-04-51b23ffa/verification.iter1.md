**Model:** Claude Opus 4.8 (`claude-opus-4-8`) — env vars CLAUDE_FRIENDLY_NAME / CLAUDE_MODEL_ID were unset; identified from runtime context.
**Timestamps:** started_at=2026-06-04T04:39:37Z · ended_at=2026-06-04T04:44:15Z · duration_seconds=278

## Verification report — briefs/2026-06-04.md (iteration 1)

Read cold as a hostile Swiss/EU public-sector SOC reader. Fetched every Source URL and the priority Additional sources. 18 URLs checked via WebFetch + bridge + 1 corroborating WebSearch. Two truth-class misdescriptions and one unsupported single-source fact found; one primary-source-strength gap; one advisory accuracy flag. Most of the brief is well-sourced and the entity/CVE/version cross-checks pass.

### Citation does not support the claim

**F3a — Sitefinity CVE-2026-7312 is misdescribed (truth-class).**
Brief (§ 2, line 71): "**CVE-2026-7312 (CVSS 10.0, CWE-284)** lets a remote anonymous attacker bypass access controls on the OData web-services endpoint (affects 14.0–15.4 pre-15.4.8630)".
Independently confirmed via NVD mirror https://cve.threatint.eu/CVE/CVE-2026-7312 and the Progress vendor advisory surfaced in search: CVE-2026-7312 is **CWE-522 Insufficiently Protected Credentials**, and it "allows a remote unauthenticated attacker to obtain plain-text credentials used to connect to the Sitefinity Insight service" — NOT an access-control bypass. Crucially, "**Successful exploitation requires active integration with Sitefinity Insight and non-default site configuration**" — a precondition that materially lowers real-world exposure and is absent from the brief. The brief states the wrong CWE (284 vs 522), the wrong mechanism (access-control bypass vs credential disclosure), and omits the exploitation precondition. The BSI German quote cited ("Sicherheitsmaßnahmen zu umgehen") is generic and does not license the CWE-284/access-control-bypass framing. Note the brief separately and correctly describes CVE-2026-7201 as "credential exposure via ServiceStack," suggesting the credential-disclosure nature was mis-assigned away from the headline 10.0 CVE.

**F3b — Windows `search:` URI handler: wrong severity tier (truth-class).**
Brief (§ 3, line 89): "Microsoft declined a CVE or fix, citing an **\"Important\"-only severity that misses its servicing bar**."
Fetched https://www.huntress.com/blog/unpatched-ntlm-leak-windows-search-uri-handler (title "When 'Moderate' Means 'Sometimes'", 2026-06-02). The page states the bug is rated **Moderate**, and that Microsoft's bar is "only **Important and Critical** severity cases meet our bar for servicing." The brief's phrasing implies the bug is rated "Important" and that Important misses the bar — the inverse of the source (an Important rating WOULD meet Microsoft's bar; the bug is Moderate). Severity tier is misstated. (Minor adjacent: brief dates Huntress 2026-06-03; page is 2026-06-02.)

### Unsupported / hallucinated facts

**F4 — WFP "Telegram on 31 May" notification not in the only cited source (truth-class; SINGLE-SOURCE item).**
Brief (§ 1, line 31): "WFP took the platform offline, **notified affected individuals via Telegram on 31 May**, and reports no other regional operation was affected."
Fetched the sole Source https://www.upguard.com/news/world-food-programme-data-breach-2026-06-02 — it confirms 600,000 Gaza households, 14 May breach date, names/ID/mobile/location, "largest breach of its kind to date," no actor identified, undisclosed vector. It does **NOT** mention a Telegram notification on 31 May, nor the "no other regional operation affected" claim. This item carries [SINGLE-SOURCE], so an unsupported specific is higher-risk. § 7 says "WFP spokesperson quotes corroborated via search" but the Telegram-31-May detail is not in the cited page; either add a source that carries it or drop the specific.

### Strengthen primary source

**F6 — Sitefinity: Progress vendor advisory exists and should replace/augment the BSI sole-primary.**
§ 7 (line 148) states "BSI CERT-Bund WID-SEC-2026-1783 for Sitefinity (Progress vendor advisory not reachable in-run)." A WebSearch surfaced the specific Progress vendor advisory: https://community.progress.com/s/article/Sitefinity-Security-Advisory-for-Addressing-Security-Vulnerabilities-CVE-2026-7312-CVE-2026-7198-CVE-2026-7195-CVE-2026-7201-CVE-2026-7313-May-2026 (it has a TLS cert-not-yet-valid error from my fetch host, but it is a real, specific PSIRT advisory URL, not a listing). This is the authoritative primary and carries the correct CWE/precondition that would fix F3a. The brief currently rests its headline 10.0 CVE entirely on a JS-rendered BSI portal page whose body cannot be fetched by the bridge or WebFetch (returns only "Warn- und Informationsdienst" shell), so the German "Evidence" quote and the five-CVE/CVSS/version specifics are not independently verifiable from a fetched source — promoting the Progress advisory resolves both the sourcing and the accuracy gap.

### Editorial / less-is-more flags (advisory)

**F11 — Burst Statistics affected-range and function-name drift.**
§ 2 (line 56): "**CVE-2026-8181 — Burst Statistics (all versions below 3.4.2)**" and "`is_mainwp_authenticated()` mis-validates HTTP Basic Auth application passwords."
The cited https://www.bleepingcomputer.com/news/security/hackers-exploit-auth-bypass-flaw-in-burst-statistics-wordpress-plugin/ gives vulnerable versions **3.4.0 and 3.4.1** (SecurityWeek: 3.4.0–3.4.1.1) and names the function **`wp_authenticate_application_password()`** (WP_Error/null treated as success), not `is_mainwp_authenticated()`. "All versions below 3.4.2" overstates the range (implies 1.x/2.x/early 3.x are affected). The `is_mainwp_authenticated()` name does not appear in the BleepingComputer source; the MainWP angle has partial basis (heise, not fetched in this pass) but the specific function name is not traceable to a cited+fetched source. Advisory: tighten the affected-version string to "3.4.0–3.4.1.1" and either source the function name or generalise it.

### Verdict

NEEDS_FIXES (truth: 3, editorial: 1, advisory: 1)

Findings F3a, F3b, F4 are truth-class (statements no cited+fetched source supports, or that contradict the cited source). F6 is editorial (primary-source strength + verifiability gap). F11 is advisory (accuracy tightening). Everything else verified clean: NCSC-CH hotel phishing (both variants + April Booking.com leak confirmed), Dutch hotels (DutchNews + Techzine), OFAC/Nobitex (all four exchanges + EO 13224/13902 + IRGC-ransomware confirmed), Mirasvit/Magento (Sansec + Imperva, KEV, ITW 24 Apr, 1.11.12, verbatim quote), Kirki (CVE-2026-8206, 500k, handle_forgot_password, 222+ blocked, v6.0.7, Patchstack), Cisco CUCM (CVE-2026-20230, 8.6/Critical, root-write quote verbatim, 14SU6/15 COP), MISP (CVE-2026-10611, beforeFilter/OTP, commit 39b3cb15 — note GHSA lists patched version "Unknown", so the "≥2.5.37" attribution to GHSA is loose but the commit is correct), Enclave M365 Android (six CVEs mapped correctly to products, 12 May fix), Ammar Askar github.dev, Symantec stock-exchange espionage (all tools/dates), Huntress DesckVB, HTTP/2 Bomb deep dive (Calif + oss-security verbatim quotes, nginx 1.29.8/max_headers, Apache mod_http2 v2.0.41, IIS/Envoy/Pingora no-patch). One thing to optionally surface: the Calif post now lists "Envoy 1.37.2 patches released June 3 (under validation)" whereas the brief's "no patch" claim is correctly sourced to oss-security as-of-disclosure — not a defect, the brief sourced it to the right place, but a Contradiction line is optional. § 2 inclusion gates honoured; CH/EU lead-ordering in § 1 correct.

### Findings summary (machine-readable)

```yaml
# Findings summary (machine-readable) — v2.48
- code: F3a
  category: claim-not-supported
  section: trending-vulnerabilities
  item: "CVE-2026-7312 — Progress Sitefinity CMS"
  url_or_quote: "Brief: 'CVE-2026-7312 (CVSS 10.0, CWE-284) lets a remote anonymous attacker bypass access controls on the OData web-services endpoint'"
  summary: "Actual (NVD https://cve.threatint.eu/CVE/CVE-2026-7312 + Progress advisory): CWE-522 Insufficiently Protected Credentials; allows obtaining plain-text Sitefinity Insight credentials, NOT access-control bypass; requires active Insight integration + non-default config (precondition omitted). Wrong CWE, wrong mechanism, missing precondition."
- code: F3b
  category: claim-not-supported
  section: research
  item: "Windows search: URI handler NTLMv2 leak — Huntress"
  url_or_quote: "Brief: 'citing an \"Important\"-only severity that misses its servicing bar'"
  summary: "Source https://www.huntress.com/blog/unpatched-ntlm-leak-windows-search-uri-handler rates the bug Moderate; Microsoft bar is 'Important and Critical meet our bar'. Brief inverts the tier — Important would meet the bar; bug is Moderate."
- code: F4
  category: hallucinated-fact
  section: active-threats
  item: "UN World Food Programme breach [SINGLE-SOURCE]"
  url_or_quote: "Brief: 'notified affected individuals via Telegram on 31 May, and reports no other regional operation was affected'"
  summary: "Sole cited source https://www.upguard.com/news/world-food-programme-data-breach-2026-06-02 does not mention a 31 May Telegram notification nor 'no other regional operation affected'. Add a source carrying it or drop the specific."
- code: F6
  category: strengthen-primary-source
  section: trending-vulnerabilities
  item: "CVE-2026-7312 cluster — Progress Sitefinity"
  url_or_quote: "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1783 (BSI sole primary; JS-rendered, body not fetchable)"
  summary: "Progress vendor PSIRT advisory exists and is the authoritative primary: https://community.progress.com/s/article/Sitefinity-Security-Advisory-for-Addressing-Security-Vulnerabilities-CVE-2026-7312-CVE-2026-7198-CVE-2026-7195-CVE-2026-7201-CVE-2026-7313-May-2026 . Promote it; it carries the correct CWE/precondition that fixes F3a. BSI portal body is not independently verifiable (returns shell only)."
- code: F11
  category: editorial-advisory
  section: trending-vulnerabilities
  item: "CVE-2026-8181 — Burst Statistics WordPress plugin"
  url_or_quote: "Brief: 'all versions below 3.4.2'; function 'is_mainwp_authenticated()'"
  summary: "Cited BleepingComputer gives vulnerable versions 3.4.0/3.4.1 (SecurityWeek: 3.4.0-3.4.1.1) and names function wp_authenticate_application_password(); 'all versions below 3.4.2' overstates range and 'is_mainwp_authenticated()' is not in the cited+fetched source. Tighten version string; source or generalise the function name."
```
