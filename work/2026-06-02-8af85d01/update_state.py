#!/usr/bin/env python3
"""Phase 5 state update for run 2026-06-02-8af85d01."""
import json, pathlib

TODAY = "2026-06-02"
BRIEF = "briefs/2026-06-02.md"
ROOT = pathlib.Path("/home/user/ctipilot")

def load(p):
    return json.loads((ROOT / p).read_text())

def save(p, obj):
    (ROOT / p).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")

# ---------- cves_seen.json ----------
cs = load("state/cves_seen.json")
by_id = {c["id"]: c for c in cs["cves"]}
NEW_CVES = {
    "CVE-2026-8732": ("WP Maps Pro WordPress plugin <=6.1.0 — unauthenticated admin-account creation via disclosed nonce + wp_ajax_nopriv_ handler; actively exploited (CVSS 9.8); fixed 6.1.1",
                      "https://www.bleepingcomputer.com/news/security/wp-maps-pro-bug-exploited-to-create-admin-accounts-on-wordpress-sites/"),
    "CVE-2026-8931": ("Disig Web Signer 2.0.3-2.5.3 — unauthenticated RCE in Slovak eIDAS qualified-signature client (CVSS 4.0 9.4, SK-CERT); fixed 2.5.5",
                      "https://www.disig.sk/en/news/important-update-of-the-web-signer-application/"),
    "CVE-2026-44825": ("Apache Solr 9.4.0-9.10.1/10.0.0 — hardcoded BasicAuth template credentials allow unauthenticated remote admin (CVSS 8.1, BSI WID-SEC-2026-1740); no patch yet, manual workaround",
                       "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1740"),
    "CVE-2026-42251": ("KAMSOFT KS-SOMED healthcare software — hardcoded FTP credentials in update client allow malicious-update injection / supply-chain (CVSS 4.0 8.7, CERT-PL)",
                       "https://cert.pl/en/posts/2026/06/CVE-2026-42251/"),
    "CVE-2025-8088": ("WinRAR path-traversal (referenced as initial-access exploit in Gamaredon GammaPhish/GammaWorm campaign, Sekoia 2026-06-01)",
                      "https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/"),
    "CVE-2024-21182": ("Oracle WebLogic Server T3/IIOP unauthenticated data access (CVSS 7.5); added to CISA KEV 2026-06-01 (out-of-window for citable primary; noted in 2026-06-02 brief Section 7)",
                       "https://www.oracle.com/security-alerts/cpujul2024.html"),
    "CVE-2026-46243": ("CIFSwitch — Linux kernel CIFS/SMB-client LPE to root via forged cifs.spnego key requests (19-year-old bug; RHEL9/SLES15/Mint/Kali); dropped from 2026-06-02 brief as out-of-window + no Section 2 gate",
                       "https://www.bleepingcomputer.com/news/security/new-cifswitch-linux-flaw-gives-root-on-multiple-distributions/"),
}
for cid, (title, url) in NEW_CVES.items():
    if cid in by_id:
        by_id[cid]["last_seen"] = TODAY
    else:
        cs["cves"].append({"first_seen": TODAY, "id": cid, "last_seen": TODAY,
                           "primary_source_url": url, "title": title})
# update existing 41089
if "CVE-2026-41089" in by_id:
    by_id["CVE-2026-41089"]["last_seen"] = TODAY
    by_id["CVE-2026-41089"]["title"] = ("Windows Netlogon stack buffer overflow — unauthenticated remote RCE to SYSTEM on domain controllers (CVSS 9.8, May 2026 Patch Tuesday); active ITW exploitation confirmed by CCB Belgium 2026-06-01")
cs["last_updated"] = TODAY
save("state/cves_seen.json", cs)
print(f"cves_seen: now {len(cs['cves'])} entries")

# ---------- covered_items.json ----------
ci = load("state/covered_items.json")
ci_by_key = {it["key"]: it for it in ci["items"]}

def appearance(section, delta):
    return {"date": TODAY, "section": section, "brief_path": BRIEF, "delta_summary": delta}

def upsert(key, typ, title, url, section, delta):
    if key in ci_by_key:
        it = ci_by_key[key]
        it["last_covered"] = TODAY
        it["appearances"].append(appearance(section, delta))
    else:
        ci["items"].append({"key": key, "type": typ, "title": title,
                            "first_covered": TODAY, "last_covered": TODAY,
                            "primary_source_url": url, "appearances": [appearance(section, delta)]})

# §0 + §4 — Netlogon (existing)
upsert("CVE-2026-41089", "cve", "Windows Netlogon CVE-2026-41089 RCE",
       "https://www.bleepingcomputer.com/news/microsoft/critical-windows-netlogon-remote-code-execution-flaw-now-exploited-in-attacks/",
       "immediate_actions", "UPDATE: active ITW exploitation confirmed by CCB Belgium 2026-06-01 on the May Patch Tuesday Netlogon RCE; promoted to Immediate Action. Microsoft advisory not yet updated to mark exploited.")
ci_by_key.setdefault("CVE-2026-41089", ci["items"][-1] if ci["items"][-1]["key"]=="CVE-2026-41089" else ci_by_key.get("CVE-2026-41089"))

# §1
upsert("item:spain-national-police-arrest-doxer-incibe-ag-civil-guard", "incident",
       "Spain arrests doxer publishing data on INCIBE/AG/Civil Guard staff (Police-ESP-Doxed)",
       "https://www.bleepingcomputer.com/news/security/spain-arrests-doxer-leaking-sensitive-data-of-govt-employees/",
       "active_threats", "First coverage. National Police arrest (Granada, 27 May) over BreachForums doxing of national-security/cyber-authority staff; OSINT+prior-breach aggregation.")
upsert("CVE-2026-42251", "cve", "KS-SOMED healthcare supply-chain hardcoded FTP creds (CERT-PL)",
       "https://cert.pl/en/posts/2026/06/CVE-2026-42251/",
       "active_threats", "First coverage. CERT-PL discloses hardcoded update-server FTP creds in KAMSOFT KS-SOMED (Polish NFZ healthcare); malicious-update injection risk.")
upsert("campaign:miasma-redhat-npm-supply-chain", "campaign",
       "Miasma worm backdoors 32 @redhat-cloud-services npm packages (TeamPCP / Mini Shai-Hulud variant)",
       "https://www.wiz.io/blog/miasma-supply-chain-attack-targeting-redhat-npm-packages",
       "active_threats", "First coverage. TeamPCP-attributed OIDC trusted-publishing abuse; new Miasma variant adds GCP/Azure cloud-identity collectors. Lineage: Mini Shai-Hulud / Shai-Hulud.")
upsert("item:meta-ai-support-bot-instagram-account-takeover", "incident",
       "Meta AI support chatbot social-engineered into resetting Instagram passwords (pro-Iranian)",
       "https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/",
       "active_threats", "First coverage. AI support agent coaxed into adding attacker email + password reset, bypassing recovery MFA envelope; MFA-enabled accounts unaffected.")

# §2
upsert("CVE-2026-8732", "cve", "WP Maps Pro unauthenticated admin-account creation (actively exploited)",
       "https://www.bleepingcomputer.com/news/security/wp-maps-pro-bug-exploited-to-create-admin-accounts-on-wordpress-sites/",
       "trending_vulns", "First coverage. CVSS 9.8 nonce/nopriv-ajax admin creation; live exploitation per Wordfence; fixed 6.1.1.")
upsert("CVE-2026-8931", "cve", "Disig Web Signer eIDAS qualified-signature client RCE",
       "https://www.disig.sk/en/news/important-update-of-the-web-signer-application/",
       "trending_vulns", "First coverage. CVSS 9.4 RCE in Slovak eIDAS signing client (SK-CERT); fixed 2.5.5.")
upsert("CVE-2026-44825", "cve", "Apache Solr hardcoded BasicAuth template credentials (no patch)",
       "https://wid.cert-bund.de/portal/wid/securityadvisory?name=WID-SEC-2026-1740",
       "trending_vulns", "First coverage. Unauthenticated admin via default template creds; no patch yet, manual workaround (BSI WID-SEC-2026-1740).")

# §3
upsert("campaign:gamaredon-gammaphish-gammaworm", "campaign",
       "Gamaredon GammaPhish/GammaWorm — NTFS-ADS USB+network worm (Sekoia)",
       "https://blog.sekoia.io/fsbs-matryoshka-1-3-gamaredons-gifts-that-keeps-unpacking-gammaphish-and-gammaworm/",
       "research", "First coverage. Sekoia unifies Gamaredon (UAC-0010/FSB) tooling; CVE-2025-8088 WinRAR initial access; ADS hiding + removable-media propagation + legit-service dead-drops.")
upsert("campaign:wordpress-steam-profile-c2-unicode-steganography", "campaign",
       "WordPress malware abuses Steam profile comments as Unicode-steganography C2 (GoDaddy)",
       "https://www.godaddy.com/resources/news/malware-targeting-wordpress-abuses-steam-community-profiles",
       "research", "First coverage. ~2,000 sites; invisible-Unicode-encoded C2 URLs in Steam Community profiles; cookie-auth PHP backdoor.")

# §4 — ShinyHunters Charter (existing key)
upsert("item:shinyhunters-charter-spectrum-listing-42m-claim", "incident",
       "ShinyHunters Charter Communications breach",
       "https://securityaffairs.com/192907/uncategorized/shinyhunters-leaks-charter-communications-data-potentially-impacting-5-million-customers.html",
       "updates", "UPDATE: ShinyHunters published the dataset after ransom refusal (30 May); HIBP ingested 4.9M unique emails + ~85k internal employee-directory records. Charter says no CPNI exfiltrated.")

# §5 — Dragon Weave deep dive
upsert("campaign:operation-dragon-weave", "campaign",
       "Operation Dragon Weave — China-nexus espionage (Czech/Taiwan) with Azure Blob dead-drop C2",
       "https://www.seqrite.com/blog/operation-dragon-weave-uncovering-a-china-linked-campaign-targeting-czech-republic-and-taiwan-using-azure-cloud-c2/",
       "deep_dive", "First coverage + deep dive. RUSTCLOAK Rust dropper -> DLL side-load -> AZUREVEIL (AdaptixC2) with Azure Blob Storage dead-drop C2; Seqrite links overlaps to SteppeDriver/UNC5221.")

ci["last_updated"] = TODAY
save("state/covered_items.json", ci)
print(f"covered_items: now {len(ci['items'])} entries")

# ---------- deep_dive_history.json ----------
dh = load("state/deep_dive_history.json")
dh["entries"].append({"date": TODAY, "category": "apt-campaign",
                      "title": "Operation Dragon Weave — China-nexus espionage vs Czech/Taiwan government with Azure Blob Storage dead-drop C2 (RUSTCLOAK -> AZUREVEIL/AdaptixC2)",
                      "primary_cve": None, "brief_path": BRIEF})
dh["entries"] = dh["entries"][-30:]
dh["last_updated"] = TODAY
save("state/deep_dive_history.json", dh)
print(f"deep_dive_history: now {len(dh['entries'])} entries")

# ---------- sources/sources.json ----------
sj = load("sources/sources.json")
src_by_id = {s["id"]: s for s in sj["sources"]}
USED_TODAY = ["bleepingcomputer", "wiz-blog", "hackernews", "krebs", "sekoia",
              "securityaffairs", "troyhunt", "helpnetsecurity", "securityweek",
              "heise-sec", "cert-pl", "bsi-de", "enisa", "ccb-belgium", "infosec-magazine"]
for sid in USED_TODAY:
    s = src_by_id.get(sid)
    if not s:
        continue
    s["last_successful_fetch"] = TODAY
    if "consecutive_failures" in s:
        s["consecutive_failures"] = 0
    if "consecutive_fetch_failures" in s:
        s["consecutive_fetch_failures"] = 0
    if "consecutive_quiet_periods" in s:
        s["consecutive_quiet_periods"] = 0
# ccb-belgium note (contributed again -> progressing toward promotion)
if "ccb-belgium" in src_by_id:
    src_by_id["ccb-belgium"]["notes"] += " | 2026-06-02: contributed corroborating content (CVE-2026-41089 exploitation confirmation)."
# add new candidate seqrite-labs (one per run)
if "seqrite-labs" not in src_by_id:
    sj["sources"].append({
        "id": "seqrite-labs",
        "publisher": "Seqrite Labs (Quick Heal Technologies research arm)",
        "url": "https://www.seqrite.com/blog/",
        "category": ["research"],
        "reliability": "MEDIUM",
        "language": ["en"],
        "status": "candidate",
        "fetch_method": "webfetch",
        "last_successful_fetch": TODAY,
        "consecutive_failures": 0,
        "notes": "First-to-publish original research on Operation Dragon Weave (China-nexus espionage vs Czech Republic + Taiwan, Azure Blob dead-drop C2) — primary used for the 2026-06-02 deep dive. Fills an India/APAC + EU-targeting research gap. Candidate — promote to active after 3 runs with content contribution."
    })
save("sources/sources.json", sj)
print(f"sources: now {len(sj['sources'])} entries; seqrite-labs added as candidate")
print("STATE UPDATE COMPLETE")
