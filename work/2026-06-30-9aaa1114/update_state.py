import json, sys
TODAY="2026-06-30"
BP=f"briefs/{TODAY}.md"

# ---------- cves_seen.json ----------
with open("state/cves_seen.json") as f: cs=json.load(f)
cves=cs["cves"]
idx={c["id"]:c for c in cves}

def upsert_cve(cid, title, url, new=False):
    if cid in idx:
        idx[cid]["last_seen"]=TODAY
        if title: idx[cid]["title"]=title
        if url: idx[cid]["primary_source_url"]=url
    else:
        rec={"id":cid,"first_seen":TODAY,"last_seen":TODAY,"title":title,"primary_source_url":url}
        cves.append(rec); idx[cid]=rec

upsert_cve("CVE-2026-48558","SimpleHelp RMM OIDC SSO auth bypass — forged-token full Technician session + MFA bypass; now actively exploited (CISA KEV 2026-06-29), Djinn infostealer via TaskWeaver loader (CVSS 10.0)","https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/")
upsert_cve("CVE-2026-55200","libssh2 pre-auth heap OOB write in ssh2_transport_read() (CVSS 9.2) — public PoC released 2026-06-29; no fixed release tagged yet","https://www.vulncheck.com/advisories/libssh2-out-of-bounds-write-via-unchecked-packet-length-in-transport-c")
upsert_cve("CVE-2026-43503","Linux kernel 'DirtyClone' LPE — SKBFL_SHARED_FRAG drop in __pskb_copy_fclone() + IPsec in-place decrypt; JFrog working exploit on Debian/Ubuntu/Fedora (CVSS 8.8)","https://research.jfrog.com/post/dissecting-and-exploiting-linux-lpe-variant-dirtyclone-cve-2026-43503/")
upsert_cve("CVE-2026-54305","n8n Dynamic Credentials EE — missing ownership/scope checks enable cross-tenant OAuth credential hijack/revoke (CVSS 9.9); NCSC-2026-0212","https://github.com/advisories/GHSA-2j5h-858j-5mpf")
upsert_cve("CVE-2026-54307","n8n public API — editor-level users read other users' credentials in shared instances (CVSS 8.5); NCSC-2026-0212","https://github.com/advisories/GHSA-pmqw-72cg-wx85")
upsert_cve("CVE-2026-8037","Progress Kemp LoadMaster pre-auth RCE — uninitialized malloc heap corruption in escape_quotes()/ /accessv2 to root (CVSS 9.8); fixed 7.2.63.2","https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/")
upsert_cve("CVE-2026-33691","Progress Kemp LoadMaster — OWASP CRS whitespace-padding file-upload extension-check bypass (high); same bulletin as CVE-2026-8037","https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/")
upsert_cve("CVE-2026-13165","SzafirHost (Polish gov e-signature client) JAR parser confusion (JarFile vs JarInputStream, CWE-345) — native DLL injection past signature check; fixed v1.2.2","https://cert.pl/en/posts/2026/06/CVE-2026-13165/")

cs["last_updated"]=TODAY
with open("state/cves_seen.json","w") as f: json.dump(cs,f,indent=2,ensure_ascii=False); f.write("\n")
print("cves_seen: now", len(cves), "entries")

# ---------- covered_items.json ----------
with open("state/covered_items.json") as f: ci=json.load(f)
items=ci["items"]
ik={it["key"]:it for it in items}

def appearance(section, delta):
    return {"date":TODAY,"section":section,"brief_path":BP,"delta_summary":delta}

def upsert_item(key, typ, title, url, section, delta):
    if key in ik:
        it=ik[key]
        it["last_covered"]=TODAY
        if url: it["primary_source_url"]=url
        if title: it["title"]=title
        it.setdefault("appearances",[]).append(appearance(section,delta))
    else:
        it={"key":key,"type":typ,"title":title,"first_covered":TODAY,"last_covered":TODAY,
            "primary_source_url":url,"appearances":[appearance(section,delta)]}
        items.append(it); ik[key]=it

# Updates to prior coverage
upsert_item("CVE-2026-48558","cve","SimpleHelp RMM OIDC auth bypass — actively exploited, CISA KEV 2026-06-29, Djinn infostealer (CVSS 10.0)","https://horizon3.ai/attack-research/disclosures/cve-2026-48558-simplehelp-authentication-bypass-iocs/","immediate_actions","Re-surfaced after 06-13 patch disclosure: now actively exploited ITW, added to CISA KEV 2026-06-29, chained to deploy new Djinn infostealer via TaskWeaver loader; CVSS revised to 10.0. Immediate Action callout + § 2 entry.")
upsert_item("CVE-2026-55200","cve","libssh2 pre-auth heap OOB write (CVSS 9.2) — public PoC","https://www.vulncheck.com/advisories/libssh2-out-of-bounds-write-via-unchecked-packet-length-in-transport-c","updates","UPDATE: public PoC scaffold released 2026-06-29; still no tagged fixed release (patch only in mainline since 06-12).")
upsert_item("CVE-2026-43503","cve","Linux kernel DirtyClone LPE (CVSS 8.8) — working exploit","https://research.jfrog.com/post/dissecting-and-exploiting-linux-lpe-variant-dirtyclone-cve-2026-43503/","updates","UPDATE: JFrog published working-exploit write-up confirmed on Debian/Ubuntu/Fedora; mainline fixed, backports rolling.")

# New § 2 vulns
upsert_item("CVE-2026-54305","cve","n8n Dynamic Credentials EE cross-tenant OAuth credential hijack (CVSS 9.9)","https://advisories.ncsc.nl/advisory?id=NCSC-2026-0212","trending_vulns","First coverage. Part of NCSC-2026-0212 (18 GHSAs); cross-tenant OAuth credential hijack/revoke; no ITW.")
upsert_item("CVE-2026-54307","cve","n8n public-API cross-user credential access (CVSS 8.5)","https://advisories.ncsc.nl/advisory?id=NCSC-2026-0212","trending_vulns","First coverage. Editor-level credential read via public API in shared instances; NCSC-2026-0212.")
upsert_item("CVE-2026-8037","cve","Progress Kemp LoadMaster pre-auth RCE to root (CVSS 9.8)","https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/","trending_vulns","First coverage. Uninitialized-malloc heap corruption in escape_quotes()//accessv2; watchTowr full mechanics; no ITW; fixed 7.2.63.2.")
upsert_item("CVE-2026-33691","cve","Progress Kemp LoadMaster file-upload extension-check bypass","https://labs.watchtowr.com/enterprise-tech-in-shell-out-progress-kemp-loadmaster-uninitialized-heap-to-pre-auth-rce-cve-2026-8037/","trending_vulns","First coverage (noted). Second bulletin CVE alongside CVE-2026-8037; CRS whitespace-padding bypass.")
upsert_item("CVE-2026-13165","cve","SzafirHost JAR parser-confusion native-DLL injection (Polish gov e-signature client)","https://cert.pl/en/posts/2026/06/CVE-2026-13165/","active_threats","First coverage. CERT Polska disclosure; JarFile vs JarInputStream confusion; EU public-sector eIDAS relevance; fixed v1.2.2.")

# New § 1 items
upsert_item("item:mustang-panda-zohomurk-zoho-workdrive-deaddrop-c2","campaign","Mustang Panda ZOHOMURK — Zoho WorkDrive dead-drop C2 vs government/energy","https://www.acronis.com/en/tru/posts/mustang-panda-targets-indias-government-and-energy-sectors/","active_threats","First coverage. China-nexus; SHARDLOADER/MINIRECON/ZOHOMURK; SaaS-as-C2 moved Dropbox/Drive→Zoho; gov/energy targeting; EU-transferable.")
upsert_item("item:jfrog-vscode-folderopen-task-npm-go-supply-chain-infostealer","campaign","Hijacked npm/Go packages weaponise VS Code folderOpen task autorun → Python infostealer","https://research.jfrog.com/post/hijacked-npm-vscode-tasks-blockchain/","active_threats","First coverage. .vscode/tasks.json runOn:folderOpen autorun bypasses npm v12 lifecycle-script block; blockchain dead-drop (Tron/Aptos); cross-platform stealer.")
upsert_item("item:fox-rothschild-silent-ransom-group-luna-moth-breach","incident","Fox Rothschild law-firm breach by Silent Ransom Group (Luna Moth)","https://databreaches.net/2026/06/29/exclusive-top-100-law-firm-fox-rothschild-suffers-data-breach-and-leak-by-silent-ransom-group/","active_threats","First coverage. SRG/Luna Moth social-engineering data-theft extortion; leak after missed deadline; FBI links to law-firm wave (48 firms listed); class action filed.")

# New § 3 research
upsert_item("item:stegoad-darkspectre-119-edge-extensions-steganography","campaign","StegoAd — 119 Edge extensions hide payloads via steganography (DarkSpectre)","https://microsoftedge.github.io/edgevr/posts/Inside-StegoAd-How-We-Disrupted-a-Massive-Malicious-Extension-Campaign/","research","First coverage. Microsoft disruption; payloads after PNG IEND / WebP / WOFF2; 2.6M installs; China-linked DarkSpectre overlap.")
upsert_item("item:malicious-perplexity-ai-chrome-extension-keystroke-intercept","campaign","Malicious 'Perplexity AI' Chrome extension intercepts address-bar keystrokes","https://www.microsoft.com/en-us/security/blog/2026/06/29/chromium-extension-uses-airelated-branding-redirect-browser-search/","research","First coverage. Abuses chrome search suggest_url override + declarativeNetRequest two-hop redirect to exfil live keystrokes; AI-brand impersonation trend.")

# Deep dive
upsert_item("item:dfir-bumblebee-adaptixc2-akira-seo-poisoning-killchain","incident","Bumblebee → AdaptixC2 → Akira: SEO-poisoning-to-ransomware kill chain (DFIR Report; Swisscom CSIRT parallel intrusion)","https://thedfirreport.com/2026/06/29/from-bing-search-to-ransomware-bumblebee-and-adaptixc2-deliver-akira-3/","deep_dive","Deep dive. Full kill chain: poisoned Bing→trojanized OpManager MSI→Bumblebee DLL-sideload→AdaptixC2→EA accounts via RSAT→NTDS.dit/Veeam→77GB SFTP exfil→Akira via WMI. Swisscom B2B CSIRT observed second intrusion same campaign.")

ci["last_updated"]=TODAY
with open("state/covered_items.json","w") as f: json.dump(ci,f,indent=2,ensure_ascii=False); f.write("\n")
print("covered_items: now", len(items), "items")
