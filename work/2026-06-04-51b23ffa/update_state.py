#!/usr/bin/env python3
import json, io

TODAY = "2026-06-04"
BRIEF = "briefs/2026-06-04.md"

def load(p):
    with open(p) as f: return json.load(f)
def save(p, d):
    with open(p, "w") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)
        f.write("\n")

# ---------- cves_seen ----------
cs = load("state/cves_seen.json")
existing = {c["id"] for c in cs["cves"]}
new_cves = [
 ("CVE-2026-49975","HTTP/2 Bomb — HPACK dynamic-table amplification + Slowloris stream-hold memory-exhaustion DoS vs nginx/Apache/IIS/Envoy/Pingora; nginx 1.29.8 & Apache mod_http2 2.0.41 patched, IIS/Envoy/Pingora unpatched at disclosure","https://blog.calif.io/p/codex-discovered-a-hidden-http2-bomb"),
 ("CVE-2026-45247","Mirasvit Full Page Cache Warmer (Magento 2) unauthenticated PHP object-injection RCE via CacheWarmer cookie; CISA KEV 2026-06-03, ITW from 2026-04-24; fix v1.11.12","https://sansec.io/research/mirasvit-cache-warmer-object-injection"),
 ("CVE-2026-8206","Kirki WordPress Freeform Page Builder 6.0.0-6.0.6 unauthenticated password-reset hijack → admin account takeover; actively exploited; fix v6.0.7","https://www.bleepingcomputer.com/news/security/critical-kirki-flaw-exploited-to-hijack-wordpress-admin-accounts/"),
 ("CVE-2026-8181","Burst Statistics WordPress 3.4.0-3.4.1.1 unauthenticated REST auth-bypass (is_mainwp_authenticated) → admin impersonation/rogue admin; actively exploited; fix v3.4.2","https://www.bleepingcomputer.com/news/security/hackers-exploit-auth-bypass-flaw-in-burst-statistics-wordpress-plugin/"),
 ("CVE-2026-20230","Cisco Unified Communications Manager WebDialer unauthenticated SSRF → OS-root file write (SIR Critical); fix 14SU6 / Release 15 COP","https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW"),
 ("CVE-2026-10611","MISP OTP bypass — session established in beforeFilter before OTP when LdapAuth.mixedAuth+require_otp both on; fix commit 39b3cb15 / >=2.5.37","https://github.com/advisories/GHSA-679G-PP8V-JVG4"),
 ("CVE-2026-7312","Progress Sitefinity CMS OData web-services unauthenticated access-control bypass (CVSS 10.0, CWE-284); BSI WID-SEC-2026-1783; fix 15.4.8630","https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1783"),
 ("CVE-2026-7198","Progress Sitefinity CMS OData improper input validation (CVSS 9.8, CWE-20), affects 15.4.8623-15.4.8629; BSI WID-SEC-2026-1783","https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1783"),
 ("CVE-2026-7201","Progress Sitefinity CMS ServiceStack web-services credential exposure (CVSS 8.8, CWE-522); BSI WID-SEC-2026-1783","https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1783"),
 ("CVE-2026-7313","Progress Sitefinity CMS legacy-branch flaw (CVSS 8.7), affects v8.0-13.3; BSI WID-SEC-2026-1783","https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1783"),
 ("CVE-2026-7195","Progress Sitefinity CMS web-services improper input validation (CWE-20); BSI WID-SEC-2026-1783","https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1783"),
 ("CVE-2026-42832","Microsoft Excel for Android OAuth-token theft via setIsDebugMode(true) debug flag left in production (CVSS 7.7); patched 2026-05-12","https://www.securityweek.com/exclusive-how-one-line-of-code-put-billions-of-microsoft-android-app-downloads-at-risk/"),
 ("CVE-2026-41101","Microsoft Word for Android OAuth-token theft via production debug flag (CVSS 7.1); patched 2026-05-12","https://www.securityweek.com/exclusive-how-one-line-of-code-put-billions-of-microsoft-android-app-downloads-at-risk/"),
 ("CVE-2026-41102","Microsoft PowerPoint for Android OAuth-token theft via production debug flag (CVSS 7.1); patched 2026-05-12","https://www.securityweek.com/exclusive-how-one-line-of-code-put-billions-of-microsoft-android-app-downloads-at-risk/"),
 ("CVE-2026-41100","Microsoft 365 Copilot for Android OAuth-token theft via production debug flag (CVSS 4.4); patched 2026-05-12","https://www.securityweek.com/exclusive-how-one-line-of-code-put-billions-of-microsoft-android-app-downloads-at-risk/"),
 ("CVE-2026-33829","Windows Snipping Tool ms-screensketch: URI handler NTLM hash leak — patched April 2026; cited as structural predecessor of unpatched search: URI variant","https://www.huntress.com/blog/unpatched-ntlm-leak-windows-search-uri-handler"),
 ("CVE-2026-9047","Devolutions Server MFA bypass via improper factor-key state handling (DEVO-2026-0013, CVSS 7.5); evaluated 2026-06-04, dropped to §7 (no ITW, below §2 gate)","https://devolutions.net/security/advisories/DEVO-2026-0013/"),
 ("CVE-2026-7325","Devolutions Server LDAP coercion exposing PAM credentials (DEVO-2026-0013, CVSS 7.1); evaluated 2026-06-04, dropped to §7 (no ITW, below §2 gate)","https://devolutions.net/security/advisories/DEVO-2026-0013/"),
]
added=0
for cid,title,url in new_cves:
    if cid in existing: continue
    cs["cves"].append({"first_seen":TODAY,"id":cid,"last_seen":TODAY,"primary_source_url":url,"title":title})
    added+=1
cs["cves"].sort(key=lambda c:c["id"])
cs["last_updated"]=TODAY
save("state/cves_seen.json", cs)
print(f"cves_seen: +{added} (total {len(cs['cves'])})")

# ---------- covered_items ----------
ci = load("state/covered_items.json")
def app(section, delta):
    return {"date":TODAY,"section":section,"brief_path":BRIEF,"delta_summary":delta}
items = [
 ("CVE-2026-45247","cve","Mirasvit Cache Warmer (Magento 2) unauth object-injection RCE — CISA KEV","https://sansec.io/research/mirasvit-cache-warmer-object-injection","trending_vulns","First coverage — KEV-added, ITW from April"),
 ("CVE-2026-8206","cve","Kirki WordPress plugin unauth admin takeover (password-reset hijack)","https://www.bleepingcomputer.com/news/security/critical-kirki-flaw-exploited-to-hijack-wordpress-admin-accounts/","trending_vulns","First coverage — actively exploited, paired with CVE-2026-8181"),
 ("CVE-2026-8181","cve","Burst Statistics WordPress plugin unauth REST auth-bypass","https://www.bleepingcomputer.com/news/security/hackers-exploit-auth-bypass-flaw-in-burst-statistics-wordpress-plugin/","trending_vulns","First coverage — actively exploited"),
 ("CVE-2026-20230","cve","Cisco Unified CM unauth SSRF → OS-root file write","https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cucm-ssrf-cXPnHcW","trending_vulns","First coverage — public-sector VoIP"),
 ("CVE-2026-10611","cve","MISP OTP bypass (LDAP mixed-auth + require_otp)","https://github.com/advisories/GHSA-679G-PP8V-JVG4","trending_vulns","First coverage — EU/CH CERT TI platform"),
 ("CVE-2026-7312","cve","Progress Sitefinity CMS OData unauth access-control bypass cluster (5 CVEs)","https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1783","trending_vulns","First coverage — DACH/EU gov CMS, BSI advisory"),
 ("CVE-2026-49975","cve","HTTP/2 Bomb single-connection memory-exhaustion DoS","https://blog.calif.io/p/codex-discovered-a-hidden-http2-bomb","deep_dive","Deep dive — network-stack DoS, IIS/Envoy/Pingora unpatched"),
 ("incident:ncsc-ch-booking-hotel-phishing-2026","incident","NCSC-CH: Booking.com breach feeds WhatsApp hotel-booking phishing (TWINT/bank spoof + booking-channel ATO)","https://www.ncsc.admin.ch/ncsc/en/home/aktuell/im-fokus/2026/wochenrueckblick_22.html","active_threats","First coverage — direct CH nexus"),
 ("incident:dutch-hotels-booking-saas-breach-2026","incident","Shared booking-SaaS breach exposes guests at 100+ Dutch/Belgian/Irish hotels; phishing wave","https://www.dutchnews.nl/2026/06/mass-data-breach-on-over-100-dutch-hotels-hits-guests/","active_threats","First coverage — EU upstream-SaaS supply-chain breach"),
 ("incident:wfp-gaza-sra-breach-2026","incident","UN WFP Palestine Self-Registration breach — ~600k Gaza households' IDs/locations exposed","https://www.upguard.com/news/world-food-programme-data-breach-2026-06-02","active_threats","First coverage — humanitarian, physical-safety risk"),
 ("incident:ofac-nobitex-iran-sanctions-2026","incident","OFAC sanctions Nobitex + 3 Iranian exchanges as IRGC-affiliated ransomware proceeds conduit","https://home.treasury.gov/news/press-releases/sb0519","active_threats","First coverage — sanctions / threat-financing context"),
 ("campaign:desckvb-rat-doubleclick-2026","campaign","DesckVB RAT malspam laundering via Google DoubleClick; AMSI/ETW patching; DACH lures","https://www.huntress.com/blog/malspam-to-deskcvb-rat-delivery-chain-analysis","active_threats","First coverage — DACH-targeted, single-source (Huntress)"),
 ("item:windows-search-uri-ntlm-leak-2026","vulnerability-trend","Unpatched Windows search: URI handler NTLMv2 leak; Microsoft declined to patch","https://www.huntress.com/blog/unpatched-ntlm-leak-windows-search-uri-handler","research","First coverage — forced-auth URI-handler class"),
 ("item:m365-android-debug-flag-oauth-theft-2026","vulnerability-trend","M365 Android debug flag (setIsDebugMode) enables silent OAuth-token theft across 6 apps","https://www.securityweek.com/exclusive-how-one-line-of-code-put-billions-of-microsoft-android-app-downloads-at-risk/","research","First coverage — patched May 2026; BYOD relevance"),
 ("item:github-dev-oauth-token-theft-2026","vulnerability-trend","One-click github.dev webview OAuth-token theft (postMessage origin flaw), unpatched + PoC","https://blog.ammaraskar.com/github-token-stealing/","research","First coverage — full-disclosure, unpatched at publish"),
 ("campaign:stock-exchange-mailbox-espionage-2026","campaign","Symantec: 5-month mailbox espionage vs global stock exchange; Aspose OST stealer, Dropbox/OneDrive exfil","https://www.security.com/threat-intelligence/stock-exchange-espionage","research","First coverage — finance critical infra, unattributed"),
]
by_key={it["key"]:it for it in ci["items"]}
appended=0
for key,typ,title,url,section,delta in items:
    if key in by_key:
        rec=by_key[key]; rec["last_covered"]=TODAY; rec["appearances"].append(app(section,delta))
    else:
        ci["items"].append({"key":key,"type":typ,"title":title,"first_covered":TODAY,"last_covered":TODAY,"primary_source_url":url,"appearances":[app(section,delta)]})
        appended+=1
ci["last_updated"]=TODAY
save("state/covered_items.json", ci)
print(f"covered_items: +{appended} (total {len(ci['items'])})")

# ---------- deep_dive_history ----------
dd = load("state/deep_dive_history.json")
dd["entries"].append({"date":TODAY,"category":"network-stack-rce","title":"HTTP/2 Bomb (CVE-2026-49975) — single-connection HPACK+Slowloris memory-exhaustion DoS across major web servers","primary_cve":"CVE-2026-49975","brief_path":BRIEF})
dd["entries"]=dd["entries"][-30:]
dd["last_updated"]=TODAY
save("state/deep_dive_history.json", dd)
print(f"deep_dive_history: appended (total {len(dd['entries'])})")

# ---------- sources bookkeeping + 1 candidate ----------
src = load("sources/sources.json")
contrib = {"ncsc-ch-focus","ncsc-ch-security-hub","ncsc-ch-incidents","heise-sec","bsi-de","cisco-psirt",
           "huntress","securityweek","bleepingcomputer","hackernews","us-treasury-ofac","risky-biz-news",
           "malwarebytes","sans-isc"}
touched=0
ids_present={s["id"] for s in src["sources"]}
for s in src["sources"]:
    if s["id"] in contrib and s.get("status")=="active":
        s["last_successful_fetch"]=TODAY
        if "consecutive_quiet_periods" in s: s["consecutive_quiet_periods"]=0
        if "consecutive_fetch_failures" in s: s["consecutive_fetch_failures"]=0
        if "consecutive_failures" in s: s["consecutive_failures"]=0
        touched+=1
# one new candidate
if "calif-codex" not in ids_present:
    src["sources"].append({
        "id":"calif-codex",
        "publisher":"Calif / Codex security research (blog.calif.io)",
        "url":"https://blog.calif.io",
        "category":["research"],
        "reliability":"MEDIUM",
        "language":["en"],
        "status":"candidate",
        "fetch_method":"webfetch",
        "last_successful_fetch":TODAY,
        "consecutive_failures":0,
        "notes":f"{TODAY}: discovered as primary author of HTTP/2 Bomb CVE-2026-49975 (deep dive {BRIEF}). AI-assisted vulnerability discovery, high technical depth. Candidate — promote to active after 3 runs with content contribution."
    })
    cand=1
else:
    cand=0
src["last_updated"]=TODAY
save("sources/sources.json", src)
print(f"sources: touched {touched} active; candidates added {cand}")
