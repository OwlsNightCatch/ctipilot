#!/usr/bin/env python3
import json, datetime

TODAY = "2026-05-24"
BRIEF = "briefs/2026-05-24.md"
RUN_ID = "2026-05-24-f1fd8070"

def load(p): return json.load(open(p))
def save(p, d): json.dump(d, open(p, "w"), indent=2, ensure_ascii=False); open(p,"a").write("\n")

# ---------- covered_items.json ----------
ci = load("state/covered_items.json")
items = ci["items"]
by_key = {it["key"]: it for it in items}

def upsert(key, typ, title, url, section, delta):
    rec = by_key.get(key)
    app = {"date": TODAY, "section": section, "brief_path": BRIEF, "delta_summary": delta}
    if rec:
        rec["last_covered"] = TODAY
        rec.setdefault("appearances", []).append(app)
        if url: rec["primary_source_url"] = url
    else:
        rec = {"key": key, "type": typ, "title": title, "first_covered": TODAY,
               "last_covered": TODAY, "primary_source_url": url, "appearances": [app]}
        items.append(rec); by_key[key] = rec

upsert("incident:unimed-kairos-german-hospitals-2026", "incident",
       "Kairos exfiltrates ~97,600+ patient records from six German university hospitals via billing processor Unimed",
       "https://therecord.media/hackers-steal-patient-billing-data-german-hospitals",
       "active_threats", "First coverage: Unimed billing-processor breach, GDPR Art.9 data; Kairos attribution per Hannover Police (heise), unclaimed per The Record")
upsert("CVE-2026-48172", "cve",
       "LiteSpeed User-End cPanel plugin lsws.redisAble privilege escalation to root (CVSS 10.0, actively exploited)",
       "https://blog.litespeedtech.com/2026/05/21/security-update-for-litespeed-cpanel-plugin/",
       "trending_vulns", "First coverage: CVSS 4.0=10.0 priv-esc, ITW exploited, patched plugin v2.4.7/WHM 5.3.1.0")
upsert("CVE-2026-33278", "cve",
       "NLnet Labs Unbound DNSSEC validator use-after-free (CVSS 9.8, pre-auth potential RCE), fixed 1.25.1",
       "https://nlnetlabs.nl/projects/unbound/security-advisories/",
       "trending_vulns", "First coverage: headline of Unbound 1.25.1 11-CVE release; no ITW/PoC")
upsert("CVE-2026-42944", "cve",
       "NLnet Labs Unbound heap overflow via NSID/Cookie/EDNS-Padding options (CVSS 8.6, default-config), fixed 1.25.1",
       "https://nlnetlabs.nl/projects/unbound/security-advisories/",
       "trending_vulns", "First coverage: default-config heap overflow in Unbound 1.25.1 cluster")
upsert("CVE-2026-3593", "cve",
       "ISC BIND 9 DoH/HTTP-2 use-after-free (CVSS 7.4), fixed 9.20.23",
       "https://kb.isc.org/docs/cve-2026-3593",
       "trending_vulns", "First coverage: BIND DoH UAF, 9.20.x only")
upsert("CVE-2026-5946", "cve",
       "ISC BIND 9 non-Internet CLASS DoS crashing named (CVSS 7.5), fixed 9.18.49/9.20.23",
       "https://kb.isc.org/docs/cve-2026-5946",
       "trending_vulns", "First coverage: single-query DoS affecting widely-deployed 9.18 branch")
upsert("item:google-cloud-api-key-deletion-delay-2026", "vulnerability-trend",
       "Deleted Google Cloud API keys keep authenticating up to 23 minutes (GCP IAM eventual consistency)",
       "https://www.aikido.dev/blog/google-api-keys-deletion",
       "research", "First coverage: Aikido finding; key revocation not immediate containment; Google reopened as P0")
upsert("item:atos-byovd-hardware-gate-bypass-2026", "vulnerability-trend",
       "Atos TRC: hardware-gated Windows drivers made BYOVD-exploitable in software (PnP AddDevice / filter restacking / registry)",
       "https://atos.net/en/lp/cybershield/anatomy-of-access-windows-device-objects-from-a-security-perspective",
       "research", "First coverage: expands LOLDrivers attack surface; surfaced by in-window THN reporting (NDSS 2026)")
upsert("tool:npm-staged-publishing-2fa", "tool",
       "npm 2FA-gated staged publishing GA + install-source restriction flags (supply-chain hardening)",
       "https://github.blog/changelog/2026-05-22-staged-publishing-and-new-install-time-controls-for-npm/",
       "updates", "Defensive response to Megalodon/mini-shai-hulud npm waves; --allow-remote/--allow-directory/--allow-file controls")
upsert("campaign:packagist-laravel-lang-supply-chain-2026", "campaign",
       "Packagist supply-chain wave: Laravel-Lang autoloader backdoor + 8-package cross-ecosystem postinstall strand",
       "https://socket.dev/blog/laravel-lang-compromise",
       "deep_dive", "Deep dive: distinct from npm/Shai-Hulud; autoload.files RCE + package.json postinstall Linux implant; 700+ repos")

ci["last_updated"] = TODAY
save("state/covered_items.json", ci)
print("covered_items: total", len(items))

# ---------- cves_seen.json ----------
cs = load("state/cves_seen.json")
cves = cs["cves"]
idx = {c["id"]: c for c in cves}
def add_cve(cid, title, url, note=None):
    if cid in idx:
        idx[cid]["last_seen"] = TODAY
        if url: idx[cid]["primary_source_url"] = url
    else:
        rec = {"first_seen": TODAY, "id": cid, "last_seen": TODAY,
               "primary_source_url": url, "title": title}
        cves.append(rec); idx[cid] = rec

add_cve("CVE-2026-48172", "LiteSpeed User-End cPanel plugin lsws.redisAble priv-esc to root (CVSS 10.0, ITW)", "https://blog.litespeedtech.com/2026/05/21/security-update-for-litespeed-cpanel-plugin/")
add_cve("CVE-2026-33278", "NLnet Labs Unbound DNSSEC validator UAF (CVSS 9.8), fixed 1.25.1", "https://nlnetlabs.nl/projects/unbound/security-advisories/")
add_cve("CVE-2026-42944", "NLnet Labs Unbound heap overflow, default-config (CVSS 8.6), fixed 1.25.1", "https://nlnetlabs.nl/projects/unbound/security-advisories/")
add_cve("CVE-2026-3593", "ISC BIND 9 DoH use-after-free (CVSS 7.4), fixed 9.20.23", "https://kb.isc.org/docs/cve-2026-3593")
add_cve("CVE-2026-5946", "ISC BIND 9 non-Internet CLASS DoS (CVSS 7.5), fixed 9.18.49/9.20.23", "https://kb.isc.org/docs/cve-2026-5946")
add_cve("CVE-2026-9256", "NGINX ngx_http_rewrite_module heap overflow (medium); dropped from §2, mentioned in §7", "https://nginx.org/en/security_advisories.html")
add_cve("CVE-2025-9086", "Stormshield SNS remote DoS (CERTFR-2026-AVI-0631); dropped from §2, mentioned in §7", "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0631/")
add_cve("CVE-2026-42945", None, None)  # bump last_seen only
cs["last_updated"] = TODAY
save("state/cves_seen.json", cs)
print("cves_seen: total", len(cves))

# ---------- deep_dive_history.json ----------
dd = load("state/deep_dive_history.json")
dd["entries"].append({
    "date": TODAY,
    "category": "supply-chain",
    "title": "Packagist supply-chain wave — Laravel-Lang autoloader backdoor and the cross-ecosystem postinstall strand",
    "primary_cve": None,
    "brief_path": BRIEF,
})
dd["entries"] = dd["entries"][-30:]
dd["last_updated"] = TODAY
save("state/deep_dive_history.json", dd)
print("deep_dive_history: total", len(dd["entries"]))

# ---------- sources/sources.json ----------
sj = load("sources/sources.json")
srcs = sj["sources"]
sidx = {s["id"]: s for s in srcs}
# bump fetched+contributing tracked sources
for sid in ["therecord","heise-sec","hackernews","helpnetsecurity","cert-eu","ncsc-ch-security-hub","anssi-fr","edpb"]:
    s = sidx.get(sid)
    if s:
        s["last_successful_fetch"] = TODAY
        if "consecutive_failures" in s: s["consecutive_failures"] = 0
        if "consecutive_fetch_failures" in s: s["consecutive_fetch_failures"] = 0
for sid in ["therecord","heise-sec","hackernews","helpnetsecurity"]:
    s = sidx.get(sid)
    if s:
        s["last_covered_in_brief"] = TODAY
        if "consecutive_quiet_periods" in s: s["consecutive_quiet_periods"] = 0
# add ccb-belgium candidate
if "ccb-belgium" not in sidx:
    srcs.append({
        "id": "ccb-belgium",
        "publisher": "Centre for Cybersecurity Belgium (CCB)",
        "url": "https://ccb.belgium.be/advisories",
        "category": ["ch-eu", "gov", "vulns"],
        "reliability": "MEDIUM",
        "language": ["en", "nl", "fr"],
        "status": "candidate",
        "fetch_method": "webfetch",
        "last_successful_fetch": TODAY,
        "consecutive_failures": 0,
        "notes": "Belgian national cybersecurity authority; publishes EN advisories on EU-relevant CVEs. Discovered 2026-05-24 via its corroborating Unbound 1.25.1 advisory (CVE-2026-33278 et al.) which carried technical detail beyond the NLnet Labs primary. Candidate — promote to active after 3 runs with content contribution.",
    })
sj["last_updated"] = TODAY
save("sources/sources.json", sj)
print("sources: total", len(srcs), "ccb-belgium added")
