#!/usr/bin/env python3
"""Phase 5 state update for 2026-05-23 brief."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TODAY = "2026-05-23"
BRIEF = "briefs/2026-05-23.md"


def load(p): return json.loads(Path(p).read_text())
def save(p, data):
    Path(p).write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


# --- covered_items.json ---------------------------------------------------
ci = load(ROOT / "state/covered_items.json")

new_items = [
    # § 1 Active Threats — 6 items
    {
        "key": "item:nl-fiod-stark-industries-worktitans-mirhosting-800-servers-eu-sanctions-arrest",
        "type": "incident",
        "title": "Netherlands FIOD arrests two over EU sanctions evasion for Stark Industries / WorkTitans bulletproof hosting; 800 servers seized; NoName057(16) DDoS infrastructure dismantled",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://www.fiod.nl/fiod-houdt-twee-verdachten-aan-wegens-overtreding-sanctiewetgeving/",
        "appearances": [{
            "date": TODAY, "section": "active_threats", "brief_path": BRIEF,
            "delta_summary": "First criminal enforcement of EU CFSP cyber sanctions against a bulletproof hoster. WorkTitans B.V. director Youssef Z. (57) and MIRhosting founder Andrey N. (39) arrested 2026-05-18; FIOD raided 5 locations including Dronten and Schiphol-Rijk data centres; 800 servers seized. Stark Industries Solutions Ltd had migrated ASN from AS44477 to AS209847 (WorkTitans) and rebranded to THE.Hosting after EU sanctions in May 2025. NoName057(16) DDoS operations against EU and Swiss public-sector targets ran on this infrastructure."
        }]
    },
    {
        "key": "item:kimwolf-dort-jacob-butler-ddos-botnet-arrest-ottawa-aisuru-variant",
        "type": "incident",
        "title": "Kimwolf / 'Dort' DDoS-for-hire operator (Jacob Butler, 23, Ottawa) arrested; AISURU variant; 30+ Tbps peak; >25,000 attack commands; DoD-range targeting",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://krebsonsecurity.com/2026/05/alleged-kimwolf-botmaster-dort-arrested-charged-in-u-s-and-canada/",
        "appearances": [{
            "date": TODAY, "section": "active_threats", "brief_path": BRIEF,
            "delta_summary": "Ontario Provincial Police arrest 2026-05-19; U.S. DoJ unsealed complaint District of Alaska 2026-05-22. Butler operated Kimwolf — variant of AISURU — infecting digital photo frames, webcams via default credentials and known CVEs. >25,000 DDoS commands, 30–31.4 Tbps peak. Coordinated C2 takedown 2026-03-19 dismantled Kimwolf alongside AISURU/JackSkid/Mossad. Also conducted DDoS+swatting against researchers including Synthient's Ben Brundage. Up to 10 years on the U.S. federal charge."
        }]
    },
    {
        "key": "item:megalodon-mass-github-cicd-backdoor-5561-repos-sysdiag-optimize-build",
        "type": "campaign",
        "title": "Megalodon mass-poisoned 5,561 GitHub repos in 6-hour window; SysDiag + Optimize-Build workflows exfiltrate cloud credentials, SSH keys, OIDC tokens",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://safedep.io/megalodon-mass-github-repo-backdooring-ci-workflows/",
        "appearances": [{
            "date": TODAY, "section": "active_threats", "brief_path": BRIEF,
            "delta_summary": "Automated attacker pushed 5,718 commits to 5,561 GitHub repos between 11:36–17:48 UTC on 2026-05-18 using forged committers (build-bot/auto-ci/ci-bot/pipeline-bot) with hardcoded 2001-09-17 timestamp. SysDiag variant runs on push/pull_request; Optimize-Build creates dormant workflow_dispatch backdoors. 111-line base64 bash payload harvests AWS/GCP/Azure creds, SSH keys, GitHub OIDC tokens. npm @tiledesk/tiledesk-server 2.18.6–2.18.12 affected."
        }]
    },
    {
        "key": "item:fbi-psa260521-kali365-phaas-oauth-device-code-m365-mfa-bypass",
        "type": "campaign",
        "title": "FBI PSA260521 warns on Kali365 — Telegram-distributed PhaaS exploiting OAuth device-code flow for persistent M365 token capture bypassing MFA",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://www.theregister.com/cyber-crime/2026/05/22/fbi-warns-of-kali365-as-device-code-phishing-soars/5245024",
        "appearances": [{
            "date": TODAY, "section": "active_threats", "brief_path": BRIEF,
            "delta_summary": "FBI IC3 PSA260521 (2026-05-21) on Kali365 — observed since April 2026. Lures impersonate Adobe Acrobat Sign/DocuSign/SharePoint with device codes for legitimate login.microsoftonline.com/common/oauth2/deviceauth page. Attacker-registered device receives access+refresh tokens. Secondary AiTM proxies session cookies. $250/month or $2,000/year per tenant; AI-generated lures in 14 languages. FBI explicitly names government and critical-infrastructure targets. T1111, T1528. EvilTokens listed as competing PhaaS."
        }]
    },
    {
        "key": "item:rhysida-claims-stuttgart-municipal-data-5btc-city-denies-confirmed-incident",
        "type": "incident",
        "title": "Rhysida claims Landeshauptstadt Stuttgart (Baden-Württemberg state capital) municipal-data theft for 5 BTC; city denies confirmed incident",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://www.heise.de/en/news/Cyber-gang-Rhysida-claims-data-theft-from-Stuttgart-city-11301876.html",
        "appearances": [{
            "date": TODAY, "section": "active_threats", "brief_path": BRIEF,
            "delta_summary": "Rhysida listed Stuttgart (~600,000 residents) on dark-web leak site 2026-05-19; 5 BTC demand (~€333,000). Heavily downscaled previews of scanned invoices and faxes. City statement: 'no indications of a cyber incident at this time'. Data-exfiltration-only claim; no encryption of operational systems. Confidence MEDIUM — leak-site corroboration only, no victim statement."
        }]
    },
    {
        "key": "item:anssi-certfr-2026-avi-0635-spip-4-4-15-security-policy-bypass-fr-public-admin",
        "type": "vulnerability-trend",
        "title": "ANSSI / CERT-FR CERTFR-2026-AVI-0635 on SPIP < 4.4.15 security-policy bypass; dominant French public-administration CMS, EU/CH Francophone government deployment",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://www.cert.ssi.gouv.fr/avis/CERTFR-2026-AVI-0635/",
        "appearances": [{
            "date": TODAY, "section": "active_threats", "brief_path": BRIEF,
            "delta_summary": "ANSSI/CERT-FR advisory 2026-05-22 on SPIP < 4.4.15 security-policy bypass. SPIP 4.4.15 released same day. No CVE assigned. SPIP is predominant CMS in French public administration, Romandie cantonal/communal sites, Belgian Francophone government. Follow-on to 4.4.14 (CERTFR-2026-AVI-0564, 2026-05-12) which fixed multiple RCEs. Auth/ACL bypass classification typical for CERT-FR."
        }]
    },
    # § 3 Research — 4 items
    {
        "key": "actor:screening-serpens-unc1549-smoke-sandstorm-nimbus-manticore-iran-apt",
        "type": "actor",
        "title": "Screening Serpens (UNC1549 / Smoke Sandstorm / Nimbus Manticore) — Iranian APT operationalising AppDomainManager hijacking; six new RAT variants MiniUpdate/MiniJunk V2 deployed Feb–Apr 2026",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://unit42.paloaltonetworks.com/tracking-iran-apt-screening-serpens/",
        "appearances": [{
            "date": TODAY, "section": "research", "brief_path": BRIEF,
            "delta_summary": "Unit 42 documents (2026-05-22) operations Feb–Apr 2026 timed to U.S.–Israeli Middle East conflict onset 2026-02-28. AppDomainManager hijacking (T1574.014) + DLL sideloading (T1574.001) with weaponised .runtimeconfig.json silently disabling ETW tracing and strong-name validation before RAT executes. MiniUpdate three variants (Mar–Apr 2026); MiniJunk V2 three variants (Feb–Mar 2026, IT professional tracked since late 2025). Targets US/Israel/UAE plus two further ME entities. Sectors: aerospace, defence, telecom."
        }]
    },
    {
        "key": "campaign:roadtools-weaponised-by-midnight-blizzard-curious-serpens-uta0355-entra-id",
        "type": "campaign",
        "title": "ROADtools weaponised by Midnight Blizzard (APT29), Curious Serpens (APT33) and UTA0355 for Entra ID device registration, token theft and tenant enumeration",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://unit42.paloaltonetworks.com/roadtools-cloud-attacks/",
        "appearances": [{
            "date": TODAY, "section": "research", "brief_path": BRIEF,
            "delta_summary": "Unit 42 (2026-05-22) documents three named clusters operationalising open-source Python ROADtools framework. Chain: credential compromise → roadtx registers attacker-controlled device → Primary Refresh Token persistence → roadrecon enumerates users/groups/service principals/OAuth via Microsoft Graph. T1098.005, T1550, T1087, T1556.006. EU diplomatic-tenant targeting pattern direct. Detection: Entra Add device events from unfamiliar device names; roadtx user-agent in sign-in logs; bulk Graph GET calls. Hardening: Conditional Access token-protection (token binding); restrict device registration to compliant/hybrid-joined."
        }]
    },
    {
        "key": "annual-report:rapid7-q1-2026-threat-landscape-report-vulnerability-exploitation-top-iav",
        "type": "annual-report",
        "title": "Rapid7 Q1 2026 Threat Landscape Report — vulnerability exploitation overtakes social engineering as top initial-access vector (38% vs 24%); KEV median time 8.5→5.0 days",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://www.rapid7.com/blog/post/tr-q1-2026-threat-landscape-report-geopolitics-ransomware/",
        "appearances": [{
            "date": TODAY, "section": "research", "brief_path": BRIEF,
            "delta_summary": "Rapid7 Labs Q1 2026 report (2026-05-21) covering Jan–Mar 2026 IR data. Vulnerability exploitation 38% IAV (first time top); social engineering 24%. >50% of exploited vulns zero-click network-facing. KEV median time disclosure-to-listing dropped from 8.5d to 5.0d. SQL injection top exploited class. RMM tool abuse 22.9%; ClickFix 18.8%. Ransomware leaders: Qilin 357 posts, The Gentlemen 206, Akira 174. Iranian/Russian/Chinese geopolitical layer; BPFDoor, ModeloRAT mentioned. PD-9 dedicated treatment."
        }]
    },
    {
        "key": "annual-report:checkpoint-research-ai-threat-landscape-march-april-2026-mexico-nine-agencies-eviltokens",
        "type": "annual-report",
        "title": "Check Point Research March-April 2026 AI Threat Landscape Digest — single operator runs two AI platforms in parallel to breach nine Mexican government agencies; EvilTokens jailbreak-as-a-service",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://blog.checkpoint.com/research/ai-attacks-are-no-longer-experimental-key-findings-from-the-march-april-2026-ai-threat-landscape/",
        "appearances": [{
            "date": TODAY, "section": "research", "brief_path": BRIEF,
            "delta_summary": "CPR digest (2026-05-22) flags AI crossing from experimental to operational. Centrepiece (Gambit Security primary): single unknown operator compromised 9 Mexican government agencies (tax records, civil registry, patient files, electoral) Dec 2025–Feb 2026 using two commercial AI platforms in parallel, >5,000 AI-executed commands. Persistence via AI client startup-config modification. EvilTokens commercial jailbreak-as-a-service platform packaging AI-driven phishing. Stolen Anthropic/OpenAI/Groq/Mistral API keys now high-value criminal targets. PD-9 dedicated treatment."
        }]
    },
    # § 5 Deep Dive
    {
        "key": "CVE-2026-46333",
        "type": "cve",
        "title": "CVE-2026-46333 ssh-keysign-pwn — 9-year ptrace race in Linux kernel __ptrace_may_access() (since v4.10-rc1, Nov 2016); four public Qualys exploits read /etc/shadow, exfiltrate SSH host keys, give root on default major distros",
        "first_covered": TODAY,
        "last_covered": TODAY,
        "primary_source_url": "https://blog.qualys.com/vulnerabilities-threat-research/2026/05/20/cve-2026-46333-local-root-privilege-escalation-and-credential-disclosure-in-the-linux-kernel-ptrace-path",
        "appearances": [{
            "date": TODAY, "section": "deep_dive", "brief_path": BRIEF,
            "delta_summary": "Qualys TRU disclosure 2026-05-20. TOCTOU race in __ptrace_may_access() in kernel/ptrace.c since v4.10-rc1 (Nov 2016). Combined with pidfd_getfd() (v5.6-rc1) for fd-duplication primitive. Four working public exploits: chage→/etc/shadow read, ssh-keysign→SSH host key exfil, pkexec→root cmd, accounts-daemon→root cmd via D-Bus. CVSS 5.5 NVD; HIGH per Qualys. Confirmed on Debian 13, Ubuntu 24.04/26.04, Fedora 43/44. No ITW reported. Patches upstream 2026-05-14; distro packages from Debian/Fedora/RHEL/Ubuntu/SUSE/AlmaLinux/CloudLinux. Mitigation: kernel.yama.ptrace_scope=2. T1068, T1552.004."
        }]
    },
]

# Append all new items
ci["items"].extend(new_items)

# Update existing items with new appearances
def add_appearance(key, section, delta_summary):
    for it in ci["items"]:
        if it["key"] == key:
            it["last_covered"] = TODAY
            it["appearances"].append({
                "date": TODAY, "section": section,
                "brief_path": BRIEF, "delta_summary": delta_summary
            })
            return True
    return False

# Drupal CVE-2026-9082 — UPDATE in §4 and Immediate Action in §0
add_appearance(
    "item:drupal-sa-core-2026-004-cve-2026-9082-sql-injection-postgres",
    "immediate_actions",
    "§ 0 Immediate Action: pre-auth SQL injection now actively exploited (CISA KEV-listed 2026-05-22). Patch to 10.4.10/10.5.10/10.6.9/11.1.10/11.2.12/11.3.10 today on PostgreSQL backends; MySQL/MariaDB/SQLite unaffected — backend swap is the temporary control if patch slips."
)
add_appearance(
    "item:drupal-sa-core-2026-004-cve-2026-9082-sql-injection-postgres",
    "updates",
    "§ 4 UPDATE delta: CISA KEV addition 2026-05-22; Drupal SA-CORE-2026-004 updated same day to confirm ITW exploitation; Imperva measured 15,000+ attempts against ~6,000 sites in 65 countries; NCSC-CH Security Hub post 12584 flipped to 'Actively exploited' 2026-05-22T13:52Z; Searchlight Cyber published technical analysis showing JSON-encoded array values surviving into SQL placeholder name on case-insensitive IN operator path through Condition::compile() / ConditionAggregate::compile()."
)

# Ghostwriter / FrostyNeighbor — UPDATE in §4 with new OYSTER* implant chain
add_appearance(
    "frostyneighbor-2026-05-campaign",
    "updates",
    "§ 4 UPDATE delta: CERT-UA#10340 documents new OYSTERFRESH → OYSTERBLUES → OYSTERSHUCK implant chain via Prometheus learning-platform PDF-and-ZIP lures targeting Ukrainian government. Distinct from prior PicassoLoader toolset. T1027 obfuscation + T1547.001 Registry Run + T1059.007 JS via eval(); final Cobalt Strike. CERT-UA recommends blocking wscript.exe execution for standard user accounts."
)

ci["last_updated"] = TODAY
save(ROOT / "state/covered_items.json", ci)
print(f"covered_items.json: +{len(new_items)} new items, 2 updates")


# --- cves_seen.json -------------------------------------------------------
cs = load(ROOT / "state/cves_seen.json")

# Bump CVE-2026-9082 last_seen
for c in cs["cves"]:
    if c["id"] == "CVE-2026-9082":
        c["last_seen"] = TODAY
        c["title"] = "Drupal core highly-critical pre-auth SQL injection in database abstraction API on PostgreSQL backends; CISA KEV-listed 2026-05-22 (SA-CORE-2026-004)"
        break

# Add CVE-2026-46333
existing_ids = {c["id"] for c in cs["cves"]}
if "CVE-2026-46333" not in existing_ids:
    cs["cves"].append({
        "first_seen": TODAY,
        "id": "CVE-2026-46333",
        "last_seen": TODAY,
        "primary_source_url": "https://blog.qualys.com/vulnerabilities-threat-research/2026/05/20/cve-2026-46333-local-root-privilege-escalation-and-credential-disclosure-in-the-linux-kernel-ptrace-path",
        "title": "ssh-keysign-pwn — 9-year ptrace race in Linux kernel __ptrace_may_access() reaches root + SSH host-key exfiltration; four public Qualys exploits on default major distros"
    })

# Sort
cs["cves"].sort(key=lambda x: x["id"])
cs["last_updated"] = TODAY
save(ROOT / "state/cves_seen.json", cs)
print(f"cves_seen.json: bumped CVE-2026-9082, added CVE-2026-46333")


# --- deep_dive_history.json ----------------------------------------------
dd = load(ROOT / "state/deep_dive_history.json")
dd["entries"].append({
    "date": TODAY,
    "category": "linux-lpe",
    "title": "CVE-2026-46333 ssh-keysign-pwn — 9-year ptrace race in Linux kernel __ptrace_may_access() (v4.10-rc1+) reaches root and SSH host keys; four public Qualys exploits",
    "primary_cve": "CVE-2026-46333",
    "brief_path": BRIEF,
})
# Cap at 30 most recent
dd["entries"] = dd["entries"][-30:]
dd["last_updated"] = TODAY
save(ROOT / "state/deep_dive_history.json", dd)
print(f"deep_dive_history.json: appended {TODAY} linux-lpe entry")
