#!/usr/bin/env python3
# Builds work/<run>/findings.S3.yaml and verifies every evidence quote against the extracted source text.
import sys, re, yaml
from pathlib import Path

import os, datetime
END_TS = os.environ.get("END_TS","PENDING")
try:
    DURATION = int((datetime.datetime.fromisoformat(END_TS.replace("Z","+00:00")) - datetime.datetime.fromisoformat("2026-11-25T03:57:53+00:00")).total_seconds())
except Exception:
    DURATION = 0
RUN = "2026-11-25T0356Z-intel"
W = Path("/home/user/ctipilot/work/2026-11-25T0356Z-intel")
EX = W / "s3tmp" / "ex"

SRC = {
 "https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign": "greynoise_cp.md",
 "https://www.securityweek.com/check-point-security-management-servers-hacked-in-ai-assisted-campaign/": "sw_cp.md",
 "https://www.rapid7.com/blog/post/ra-rapid7-analysis-vmware-vcenter-srp-authentication-bypass-to-root-cve-2026-123890": "r7_vcenter.md",
 "https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0009/README.md": "vmsa.md",
 "https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/": "u42_agentic.md",
 "https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/": "reliaquest.md",
 "https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens": "dragos.md",
 "https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/": "openrouter.md",
 "https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html": "hn_openrouter-drops-3-providers-after.md",
 "https://arxiv.org/abs/2611.18126": "arxiv_tpm.md",
 "https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7079.html": "amd7079.md",
 "https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html": "hn_flash-chip-attack-bypasses-tpm-lockout.md",
 "https://depthfirst.com/research/narrow-grants-wide-engines": "depthfirst.md",
 "https://www.postgresql.org/support/security/CVE-2026-116331/": "pg_cve.md",
 "https://thehackernews.com/2026/11/researcher-demonstrates-database-rce.html": "hn_researcher-demonstrates-database-rce.md",
 "https://www.oracle.com/security-alerts/cspunov2026.html": "oracle_nov.md",
 "https://www.okta.com/blog/threat-intelligence/former_shinyhunters_cluster_moves_to_new_inception_site/": "okta_inception.md",
 "https://www.reversinglabs.com/blog/threat-researchers-notebook-sso-vishing-campaign-associated-with-emerging-inception-extortion-group": "rl_inception.md",
 "https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-23-Legal-themed-vishing-activity.txt": "u42_legal.md",
 "https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html": "hn_okta.md",
 "https://research.checkpoint.com/2026/volant-manticore-flying-under-the-radar/": "cpr_volant.md",
}

def ev(quote, attribution, url):
    return {"quote": quote, "attribution": attribution, "source_url": url}

U_GN = "https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign"
U_SW = "https://www.securityweek.com/check-point-security-management-servers-hacked-in-ai-assisted-campaign/"
U_R7 = "https://www.rapid7.com/blog/post/ra-rapid7-analysis-vmware-vcenter-srp-authentication-bypass-to-root-cve-2026-123890"
U_VMSA = "https://github.com/vmware/vcf-security-and-compliance-guidelines/blob/main/security-advisories/vmsa-2026-0009/README.md"
U_U42 = "https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/"
U_RQ = "https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/"
U_DR = "https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens"
U_OR = "https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/"
U_HNOR = "https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html"
U_AX = "https://arxiv.org/abs/2611.18126"
U_AMD = "https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7079.html"
U_HNTPM = "https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html"
U_DF = "https://depthfirst.com/research/narrow-grants-wide-engines"
U_PG = "https://www.postgresql.org/support/security/CVE-2026-116331/"
U_HNDB = "https://thehackernews.com/2026/11/researcher-demonstrates-database-rce.html"
U_ORA = "https://www.oracle.com/security-alerts/cspunov2026.html"
U_OK = "https://www.okta.com/blog/threat-intelligence/former_shinyhunters_cluster_moves_to_new_inception_site/"
U_RL = "https://www.reversinglabs.com/blog/threat-researchers-notebook-sso-vishing-campaign-associated-with-emerging-inception-extortion-group"
U_U42L = "https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-23-Legal-themed-vishing-activity.txt"
U_HNOK = "https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html"
U_CPR = "https://research.checkpoint.com/2026/volant-manticore-flying-under-the-radar/"

items = []

# ---------------------------------------------------------------- 1. GreyNoise GT13
items.append({
 "title": "GreyNoise GT13: an unattributed, probably AI-assisted actor held persistent access to at least 24 Check Point Security Management servers at 22 organisations, government among them, and used a hijacked Rejetto HFS host as its relay",
 "sources": [
  {"url": U_GN, "publisher": "GreyNoise", "date": "2026-11-23", "role": "primary"},
  {"url": U_SW, "publisher": "SecurityWeek", "date": "2026-11-24", "role": "corroborating"},
 ],
 "discovery_trace": "first seen at: securityweek feed sweep (standing major-lab/news sweep, not a slice record), URL https://www.securityweek.com/check-point-security-management-servers-hacked-in-ai-assisted-campaign/ -> primary: GreyNoise, URL https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign (extract). WebSearch for a Check Point vendor statement or a second independent observer found none.",
 "summary": (
  "GreyNoise reports, from its own sensor network and attacker-side artefacts it recovered, an intrusion campaign it tracks as GT13 against Check Point Security Management servers: confirmed activity between 2026-10-17 and 2026-11-02 at no fewer than 22 organisations in sectors that include government, energy, financial services, transportation, mining, engineering and manufacturing, with assets in the UK, Ireland, France, the Netherlands, Greece, Germany, Austria, Bulgaria, Poland, India, Thailand, Vietnam, South Korea, Hong Kong, China, Australia and the United States. "
  "GreyNoise does not attribute GT13 to any tracked group and states it cannot assess motive or nation of origin. "
  "The observed chain started on 2026-10-02 against a Rejetto HFS server (CVE-2026-61500: recovering the V8 Math.random() state from successive loginSrp1 session values to forge a signed admin cookie, marked allow_session_ip_change:true so it works from any exit); the actor then planted an SSH key, turned the host into an operational relay (\"hop\"), ran Nmap, Chisel (reverse proxy), Impacket, Paramiko and at least 30 Python scripts, and from there used a script for CVE-2026-16232 (SmartConsole authentication bypass to Run Script, described as adapted from the Metasploit module) to launch more than 100 management tasks on several Check Point management servers, including copying the firewall database and the Internal CA, minting a certificate and unloading security policies. "
  "On 2026-10-26 a bulk certificate-management task went to 24 compromised management servers across the 22 organisations; it failed, but the returned files let GreyNoise identify and notify victims directly or through government partners. "
  "GreyNoise says it could not determine when or how the actor first reached the Check Point servers (that access pre-dated the HFS compromise), that its visibility ended around 2026-11-02, and that it expects the campaign to be continuing because of the actor's persistent access. "
  "The use of LLMs and agentic systems for scanning, exploitation and tool development is GreyNoise's assessment (\"we believe\", \"we suspect\"), not an observed fact; hands-on-keyboard activity was also seen."
 ),
 "region_nexus": "multi-country, including Austria and Germany; no Swiss victim named by GreyNoise",
 "primary_sector_nexus": "direct (government is one of the sectors GreyNoise names among the victims)",
 "sector": "public-sector",
 "cves": ["CVE-2026-16232", "CVE-2026-61500"],
 "techniques": ["T1190", "T1098.004", "T1572", "T1090.003", "T1046", "T1110.003", "T1105", "T1686"],
 "affected_products": ["Check Point Security Management", "Check Point Multi-Domain Security Management", "Rejetto HFS"],
 "entity_keys": [],
 "new_entities": [
  {"key": "actor:greynoise-gt13", "type": "actor", "name": "GreyNoise Threat 13 (GT13)", "aliases": ["GT13"],
   "summary": "GreyNoise's unattributed cluster designation for an actor with persistent access to at least 24 Check Point Security Management servers at 22 organisations (activity confirmed 2026-10-17 to 2026-11-02), which GreyNoise suspects uses LLM-driven agentic tooling (GreyNoise, 2026-11-23)."}
 ],
 "verification": "SINGLE-SOURCE-OTHER",
 "confidence": "MEDIUM",
 "novelty": "new",
 "suggested_references": ["2026-07-23/check-point-smartconsole-auth-bypass-cve-2026-16232", "2026-07-13/rejetto-hfs-session-forgery-prng-rce-cve-2026-61500"],
 "suggested_priority": "high",
 "suggested_classification": {"reliability": "B", "credibility": 2},
 "sourcing_note": "GreyNoise is the only first-hand observer (honeypot/sensor data plus recovered attacker files); SecurityWeek re-reports it, so this is one independent observation. Both existing entries on the two CVEs (2026-07-23 Check Point, 2026-07-13 Rejetto HFS) carry the vulnerability facts; this item is the actor campaign and must declare them in references[] because the CVEs overlap.",
 "evidence": [
  ev("GreyNoise recently discovered an intrusion campaign targeting Check Point Security Management Servers, with confirmed attack activity between October 17th and November 2nd, 2026, impacting at least 22 distinct organizations globally.", "GreyNoise", U_GN),
  ev("We do not attribute GT13 to any known or publicly tracked threat group at this time.", "GreyNoise", U_GN),
  ev("The GT13 adversary had access to the victim Check Point Security Management Servers before they compromised the HFS server. We could not determine when or how the attacker gained access to those Check Point assets.", "GreyNoise", U_GN),
  ev("copying the firewall database and the Internal CA, minting a new certificate (pivot.p12), and unloading security policies (which would disable the firewall)", "GreyNoise", U_GN),
  ev("Our visibility into this attack activity stopped around November 2nd, 2026, but given the actor’s persistent access to victim Check Point devices, we expect that this intrusion campaign is ongoing.", "GreyNoise", U_GN),
 ],
 "extended_notes": (
  "EXPOSURE (source-supported): Check Point Security Management / Multi-Domain servers; GreyNoise names CVE-2026-16232 as the exploit script used but could not say how the first access happened or which builds were hit, so a patched management server is not shown to be clean. The existing 2026-07-23 entry carries the vendor fixed builds (Jumbo Hotfix Accumulator R82.10 Take 36+, R82 Take 118+, R81.20 Take 158+) and the Trusted Clients prerequisite.\n"
  "DETECTION (telemetry classes): management-server audit/admin logs for Run Script tasks and bulk certificate-management tasks issued from unexpected admin sessions or source addresses, and for security-policy unload events; Gaia/Linux file-integrity on /root/.ssh/authorized_keys and /etc/ld.so.preload (GreyNoise saw a preload error naming /usr/lib/.libproc.so and says it 'may indicate an implant'); outbound ssh/scp from management servers to non-administrator hosts (GreyNoise: each compromised device held the private key matching the public key planted on the hop, and delivered result files to the hop by scp); Chisel client processes; egress from management servers to consumer-VPN exits (GreyNoise: the 99 actor IPs were ExpressVPN egresses or compromised victim Check Point devices).\n"
  "POST-PATCH COMPROMISE CHECK (implication of the observed actions, not a vendor statement): the actor copied the firewall database and the Internal CA, so if a management server shows any of the above, treat its administrator credentials and CA-issued trust as exposed rather than patching and moving on.\n"
  "TRIAGE: CVE-2026-16232 task bursts across many management servers in incrementing-IP order are automation; a single administrator running Run Script from a known management host is normal.\n"
  "HFS leg: Rejetto HFS CVE-2026-61500 is already an entry (2026-07-13); GreyNoise says the HFS server was unpatched.\n"
  "The 'AI-assisted' framing is GreyNoise's suspicion based on timeline foibles and tooling; do not present it as established."
 ),
})

# ---------------------------------------------------------------- 2. Rapid7 vCenter analysis (update)
items.append({
 "title": "Rapid7's technical analysis of the vCenter directory-service bypass (CVE-2026-123890): root cause, a working chain to root on 8.0.2.00400, and the appliance log trail it leaves",
 "sources": [
  {"url": U_R7, "publisher": "Rapid7", "date": "2026-11-24", "role": "primary"},
  {"url": U_VMSA, "publisher": "Broadcom (VMSA-2026-0009 Q&A)", "date": "2026-11-19", "role": "corroborating"},
 ],
 "discovery_trace": "first seen at: rapid7 feed sweep (standing major-lab sweep, not a slice record), URL https://www.rapid7.com/rss.xml item https://www.rapid7.com/blog/post/ra-rapid7-analysis-vmware-vcenter-srp-authentication-bypass-to-root-cve-2026-123890 -> primary (extract of the Rapid7 post) -> Broadcom VMSA-2026-0009 Q&A on GitHub (fixed-version confirmation)",
 "summary": (
  "Rapid7 published on 2026-11-24 its reproduction of CVE-2026-123890 against vCenter Server Appliance 8.0.2.00400 (build 23929136, Photon OS 4.0) and the root cause. "
  "Three flaws combine: the vmdir SRP verifier helper (Srv_rpc_srp_verifier_get_session_key) returns the session key of a pending login without checking authentication, ownership or the client's proof; the DCE/RPC runtime resolves a context handle from a process-wide table without comparing it to the requesting connection; and the context handles are predictable UUIDv1 values, so two reference verifiers created before and after a target login bound the hidden handle to a short timestamp window (recovered after 5,083 queries in 0.88 s in one run, 17,337 guesses in 8 s in another). "
  "With the key the attacker completes SRP as the SSO administrator without the password, needs only TCP 2012 and the name of an existing SSO principal (the default SSO administrator principal in the PoC), and no administrator has to be online. "
  "Rapid7 then chained the session into the directory database-copy interface to read data.mdb with the STS private signing key, forged an administrator SAML assertion, created a local superAdmin account through the appliance API, enabled SSH and Bash and reached root via sudo (this last stage also needs TCP 443 and 22). "
  "Rapid7 describes a Metasploit module with a check that only requests a key and a run that performs the full chain, but does not state whether the module is public. "
  "It did not diff Broadcom's fix, notes that replacing the predictable UUIDs alone would leave the ownership flaw, and names vCenter 8.0 U3m (VMSA-2026-0009) as the fixed 8.0 release."
 ),
 "region_nexus": "global",
 "primary_sector_nexus": "direct (vCenter is common public-sector virtualisation management; existing entry already covers exploitation by ARMORY CASTLE per GTIG)",
 "sector": "public-sector",
 "cves": ["CVE-2026-123890"],
 "techniques": ["T1190", "T1606.002", "T1136.001", "T1021.004"],
 "affected_products": ["VMware vCenter Server"],
 "entity_keys": [],
 "new_entities": [],
 "verification": "SINGLE-SOURCE-OTHER",
 "confidence": "HIGH",
 "novelty": "update-of:2026-11-20/vmware-vcenter-cve-2026-123890-auth-bypass-exploited-gtig",
 "suggested_update_fields": ["body", "detection"],
 "suggested_priority": "high (existing entry's priority applies; this adds the technical root cause and a log-based hunt)",
 "suggested_classification": {"reliability": "B", "credibility": 2},
 "sourcing_note": "Rapid7's own lab reproduction (a vulnerability-research vendor, not an observer of in-the-wild exploitation); the fixed-version statement is corroborated by Broadcom's Q&A. The exploited-in-the-wild facts stay with the existing entry (GTIG, CISA KEV).",
 "evidence": [
  ev("The vulnerable interface is exposed through DCE/RPC on TCP port 2012.", "Rapid7", U_R7),
  ev("The attacker needs network access to TCP 2012 and the name of an existing SSO principal.", "Rapid7", U_R7),
  ev("Remote DB transfer (/storage/db/vmware-vmdir/data.mdb) granted.", "Rapid7", U_R7),
  ev("Replacing predictable UUIDs alone leaves that ownership problem in place.", "Rapid7", U_R7),
  ev("The vCenter 8.0 fixed version in this advisory is 8.0 U3m.", "Broadcom (VMSA-2026-0009 Q&A)", U_VMSA),
 ],
 "extended_notes": (
  "DELTA vs the existing entry (which already has TCP 2012, GTIG's BONESAW chain, fixed builds and KEV): (1) Rapid7's lab chain shows the same endgame GTIG saw, data.mdb read, STS signing key, forged SAML admin session, local account creation, SSH/Bash enabled, root; (2) root-cause detail (no ownership check on an RPC context handle plus predictable UUIDv1 handles); (3) concrete appliance telemetry to hunt after patching.\n"
  "DETECTION (telemetry classes + anchors from Rapid7's reproduction): network: repeated calls to operation 1 of the SRP helper interface (c7e94609-6ab0-4767-8e92-b6485bff1649) with no RPC authentication verifier and context UUIDs differing mainly in timestamp, between a pending login's bind and its SRP proof, a port-2012 connection alone does not prove exploitation; appliance logs: /var/log/vmware/vmdird/vmdird-syslog.log 'Remote DB transfer (/storage/db/vmware-vmdir/data.mdb) granted' (no caller address, legitimate replication can also trigger it), /var/log/vmware/vapi/endpoint/endpoint-access.log POST /rest/appliance/local-accounts/<name>, PUT /rest/appliance/access/ssh and /shell, /var/log/vmware/applmgmt/applmgmt.log (account created, SSH/Bash enabled; the enable values are DEBUG-level), /var/log/audit/sshinfo.log (rotated) and audit.log (useradd -G superAdmin, sudo -n /bin/bash -i). Rapid7: the forged SAML session is treated as an administrator session, so the identity alone does not distinguish it; the sequence (DB-transfer grant, account creation, SSH enablement, SSH login then sudo) does.\n"
  "POST-PATCH CHECK: a data.mdb transfer grant means the STS private signing key left the appliance (Rapid7: the database contains it); the existing entry's GTIG-sourced guidance on what to rotate applies.\n"
  "Not stated by Rapid7: whether the Metasploit module is public; whether other exposure than TCP 2012 matters for the first stage."
 ),
})

# ---------------------------------------------------------------- 3. Unit 42 agentic AI trends
items.append({
 "title": "Unit 42 on agentic AI attackers: more than ten campaigns (July to September 2026), all entered through web shells on vulnerable web applications, with machine-speed command rates and fingerprints defenders can hunt for",
 "sources": [
  {"url": U_U42, "publisher": "Unit 42 (Palo Alto Networks)", "date": "2026-11-24", "role": "primary"},
  {"url": U_RQ, "publisher": "ReliaQuest", "date": "2026-10-07", "role": "corroborating"},
 ],
 "discovery_trace": "first seen at: unit42 feed sweep (standing major-lab sweep, not a slice record), URL https://unit42.paloaltonetworks.com/feed/ item https://unit42.paloaltonetworks.com/autonomous-ai-agent-threat-campaigns/ -> primary (extract) -> ReliaQuest Threat Spotlight, URL https://reliaquest.com/blog/threat-spotlight-how-ai-agents-turned-one-exposed-endpoint-into-a-server-takeover/ (Unit 42's cited infrastructure overlap, read and checked)",
 "summary": (
  "Unit 42 says it tracked more than 10 global campaigns between July and September 2026 in which different attackers pointed autonomous AI agents at victims in government, logistics, hospitality, manufacturing, agriculture and education. "
  "In every campaign the foothold was a web shell dropped through a vulnerable web application, handed to the agent by a human operator; the agent then did reconnaissance, credential harvesting, privilege escalation and lateral movement and reported back in machine-readable output. "
  "Unit 42 reports no novel technique but a different tempo and set of traces: about 800 unique commands in 140 minutes in one case and more than 8,000 over 12 days in another; a median gap between commands of 1.4 s once the agent took over, against 23.9 s in the preceding human phase of a subset; section headers such as ===[Title]=== in shell commands in every campaign; step-by-step reasoning comments inside scripts in more than half; and 40 to 100 unique, victim-tailored Base64 payloads per session with no compiled implant recovered. "
  "Observed behaviours include on-target compilation of public local-privilege exploits after pre-built ones failed (Copy Fail CVE-2026-31431, PwnKit, CVE-2024-1086), a switch from IMDSv1 to IMDSv2 token acquisition on an EC2 instance role, ASPX web shells pushed over SMB to more than 40 locations in 26 minutes, deliberate EDR path exclusion in find commands, enumeration of 16 security scanners, strace against the Defender for Endpoint daemon, and a pivot from the victim's web server to the vendor's self-managed GitLab (credentials found on the compromised host, no GitLab flaw exploited) and to sister organisations. "
  "Unit 42 links one campaign's hard-coded C2 address to a host also running a CyberStrikeAI login page, an overlap ReliaQuest independently documented on the same host in its 2026-10-07 incident, and treats such infrastructure and operator slips (a leaked exploitmasteryai path, code comments in Chinese) as more reliable attribution leads than behaviour."
 ),
 "region_nexus": "global; a US hospitality and gaming victim is described; no Swiss nexus stated",
 "primary_sector_nexus": "direct (government named among the targeted sectors; the entry vector is the web-application tier)",
 "sector": "public-sector",
 "cves": ["CVE-2026-31431"],
 "techniques": ["T1190", "T1505.003", "T1059.004", "T1059.001", "T1047", "T1068", "T1552.005", "T1021.002", "T1110", "T1518.001", "T1580", "T1619"],
 "affected_products": ["Linux kernel (CVE-2026-31431 Copy Fail)", "GitLab (self-managed; credentials exposed on a compromised host, no GitLab flaw exploited)"],
 "entity_keys": ["tool:cyberstrikeai"],
 "new_entities": [],
 "verification": "SINGLE-SOURCE-OTHER",
 "confidence": "MEDIUM",
 "novelty": "new",
 "suggested_references": ["2026-11-17/gtig-ai-threat-tracker-nov-2026-exploit-agent-settings", "2026-11-14/cyberstrikeai-aws-cloudtrail-intrusion-one-source-ip", "2026-11-17/symantec-ai-assisted-retailer-intrusion-orion-rabbitmq"],
 "suggested_priority": "notable",
 "suggested_classification": {"reliability": "B", "credibility": 2},
 "sourcing_note": "The ten-campaign synthesis is Unit 42's own telemetry (one source); the CyberStrikeAI infrastructure overlap is independently corroborated by ReliaQuest (2026-10-07), whose host-level description (a Cairn dashboard on the attack-origin host, a CyberStrikeAI login page and agent console on a second host) is consistent with Unit 42's citation. ReliaQuest's 'Cairn' may or may not be the registry's tool:cairn-exploitation-engine: unresolved, do not link.",
 "evidence": [
  ev("Between July and September 2026, we identified and tracked more than 10 global campaigns in which different attackers deployed autonomous AI agents to enhance their attacks.", "Unit 42", U_U42),
  ev("In every observed campaign the attackers gained their initial foothold through web shells that were deployed via vulnerable web applications.", "Unit 42", U_U42),
  ev("Once an AI operator took command, the median inter-command gap dropped to 1.4 seconds.", "Unit 42", U_U42),
  ev("In every campaign that we observed, AI operators used section headers in shell commands and scripts", "Unit 42", U_U42),
  ev("we did not recover a single compiled backdoor, custom C2 framework, DLL implant or shellcode loader.", "Unit 42", U_U42),
  ev("Title “CyberStrikeAI,” login page", "ReliaQuest", U_RQ),
 ],
 "extended_notes": (
  "EXPOSURE: internet-facing web applications that can be turned into a web-shell foothold; the report names no specific vulnerable product (the entry vectors are not enumerated), so the exposure line is the web-application tier plus self-managed GitLab-style developer tooling reachable with credentials found on a compromised host.\n"
  "DETECTION (behavioural, telemetry-class first): process-creation and shell-history telemetry on web servers for bursts of hundreds of distinct commands with sub-2-second gaps, ===[Title]=== delimiters and explanatory comments inside shell one-liners; web-server-spawned shells piping many unique Base64 blobs (volume and uniqueness, not the encoding itself); find/grep commands that exclude EDR vendor directories, enumeration of security scanners, strace or debugger attach on the EDR daemon (wdavdaemon in the case described); cloud audit records showing an instance role calling IMDS and then enumerating 20 services across eight regions; ASPX/PHP files written to many web roots over SMB in minutes.\n"
  "TRIAGE: human admins also run find and enumeration commands; the discriminator is rate (1.4 s median gap), volume of unique payloads and the delimiters/reasoning comments, not any single command.\n"
  "HARDENING named by the source: GitLab hardening (MFA, sign-in rate limiting, IP restriction, patching); the IMDSv1-to-v2 switch shows on-host code can still get role credentials, so scope instance roles (inference from the observed behaviour).\n"
  "Unit 42 itself says no behavioural marker links activity to a specific model or orchestration framework, and recommends infrastructure and operator-slip correlation for attribution. The product claims (Cortex) are vendor marketing and are not carried."
 ),
})

# ---------------------------------------------------------------- 4. Dragos canary-token research
items.append({
 "title": "Dragos canary-token research: attackers stole prompts from three AI inference providers for months, marketplace sellers logged them, and Zero Data Retention flags did not hold; OpenRouter dropped three providers",
 "sources": [
  {"url": U_DR, "publisher": "Dragos (HD Moore)", "date": "2026-11-19", "role": "primary"},
  {"url": U_OR, "publisher": "OpenRouter", "date": "2026-11-22", "role": "corroborating"},
  {"url": U_HNOR, "publisher": "The Hacker News", "date": "2026-11-22", "role": "corroborating"},
 ],
 "discovery_trace": "first seen at: hackernews feed, URL https://feeds.feedburner.com/TheHackersNews item https://thehackernews.com/2026/11/openrouter-drops-3-providers-after.html -> primary: Dragos, URL https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens -> corroboration: OpenRouter incident announcement, URL https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers/",
 "summary": (
  "Dragos's research team sent about two million prompts carrying unique canary URLs and AWS credentials to widely used AI services between July and November 2026 and watched where the secrets surfaced. "
  "It reports three findings: data from at least three inference providers was exposed to attackers (the earliest incident from mid-July, none of the three knew until Dragos told them, and in two of the breaches some stolen requests carried the Zero Data Retention flag); resellers on an inference marketplace could read and keep prompts through ordinary request logging, with no exploit needed; and several providers did not honour privacy settings, including a Chinese AI lab whose systems fetched the secret URLs from more than half of the seeded prompts sent to its models (about two-thirds of those flagged ZDR) and U.S. hosts reselling that lab's models that fed the same scraper. "
  "The largest breach saw a couple of hundred AWS keys, each sent once in short late-October windows, tested within hours, used to list S3, search Secrets Manager and Parameter Store, try to enable Bedrock models, create Bedrock API keys and add IAM users, for tens of thousands of AWS API calls. "
  "Dragos says one adversary appears to have compromised two providers at once and on 2026-11-01 added the ARTEX agentic pentest framework, only to confirm already-held keys were live. "
  "OpenRouter confirmed it off-boarded three providers, removed 125 endpoints from ZDR eligibility and notified potentially affected customers, stating the findings show no breach of OpenRouter itself; it lists six provider notices, among them security-incident posts from GMI Cloud and Together, without saying which three were breached."
 ),
 "region_nexus": "global; no Swiss nexus stated",
 "primary_sector_nexus": "indirect (public-sector adoption of LLM gateways and agents; prompts routinely carry credentials and internal data)",
 "sector": "cross-sector",
 "cves": [],
 "techniques": ["T1078.004", "T1619", "T1555.006", "T1136.003", "T1098.001"],
 "affected_products": [],
 "entity_keys": ["tool:artex"],
 "new_entities": [],
 "verification": "MULTI-SOURCE",
 "confidence": "MEDIUM",
 "novelty": "new",
 "lookback": True,
 "suggested_references": ["2026-10-22/artex-storm-0940-agentic-llm-pentest-spraying-oauth-abuse"],
 "suggested_priority": "notable",
 "suggested_classification": {"reliability": "B", "credibility": 2},
 "sourcing_note": "Dragos is the only source for the canary design and the provider findings (its providers are unnamed); OpenRouter, the largest affected router, independently confirms the remediation and that providers were off-boarded, but does not confirm the breach details. The Chinese-lab and Feishu observations are Dragos's own and the lab is unnamed.",
 "evidence": [
  ev("We observed activity indicating that data from at least three AI providers was exposed.", "Dragos", U_DR),
  ev("In the other two breaches, some of the stolen requests were marked as ZDR.", "Dragos", U_DR),
  ev("The earliest incident dates back to the middle of July, and none of the three providers knew about their breach until we notified them.", "Dragos", U_DR),
  ev("Off-boarded three providers from OpenRouter, based on the results of our investigations.", "OpenRouter", U_OR),
  ev("Removed 125 endpoints from Zero Data Retention (ZDR) eligibility.", "OpenRouter", U_OR),
  ev("Two of its user agents, artex-agent and artex-judge-r121, appear in no public indicator list the firm could find and are worth adding to detections.", "The Hacker News", U_HNOR),
 ],
 "extended_notes": (
  "EXPOSURE: any organisation sending prompts, agent context or tool output through a third-party LLM router, reseller marketplace or smaller inference host; Dragos's point is that a privacy flag binds only the first hop and that agents send whatever they can read, credentials included.\n"
  "DETECTION: cloud control-plane audit records (AWS CloudTrail userAgent) for artex-agent and artex-judge-r121 and for Kali- or OrbStack-hosted Boto3/aws-cli clients, with Dragos's caveat that this self-identification is present in only a small fraction of traffic; first use of any AWS key that was ever pasted into a prompt, then S3 listing, Secrets Manager/Parameter Store reads, Bedrock API key creation and IAM user creation; seeded canary credentials in agent context whose first use is an incident (Dragos recommends free Thinkst Canarytokens).\n"
  "HARDENING named by Dragos: choose the upstream provider yourself instead of the router default, verify privacy settings change where requests go, avoid reseller marketplaces, enable provider-side secret filtering (not a panacea), self-host for the most sensitive work.\n"
  "Not carried: which providers were breached (Dragos does not name them); the OpenRouter-listed provider posts were not fetched in this run, so no claim about them beyond their existence on OpenRouter's page."
 ),
})

# ---------------------------------------------------------------- 5. TU Berlin Hello Again
items.append({
 "title": "'Hello Again': TU Berlin rolls back the firmware TPM's PIN lockout counters from the flash chip, cutting a default 6-digit BitLocker PIN from 19 years to 20 days; AMD confirms a firmware flaw (CVE-2026-43613) and schedules fixes",
 "sources": [
  {"url": U_AX, "publisher": "arXiv (Werling et al., TU Berlin)", "date": "2026-11-13", "role": "primary"},
  {"url": U_AMD, "publisher": "AMD (AMD-SB-7079)", "date": "2026-11-17", "role": "primary"},
  {"url": U_HNTPM, "publisher": "The Hacker News", "date": "2026-11-18", "role": "corroborating"},
 ],
 "discovery_trace": "first seen at: hackernews feed, URL https://feeds.feedburner.com/TheHackersNews item https://thehackernews.com/2026/11/flash-chip-attack-bypasses-tpm-lockout.html -> primary: arXiv 2611.18126, URL https://arxiv.org/abs/2611.18126 -> vendor: AMD-SB-7079, URL https://www.amd.com/en/resources/product-security/bulletin/amd-sb-7079.html (found via WebSearch (\"AMD security bulletin fTPM RPMC ... Hello Again\"), then fetched)",
 "summary": (
  "Researchers at Technische Universitaet Berlin show that the TPM lockout (anti-hammering) state of firmware TPMs on AMD, Intel and Pluton PCs, which is persisted in SPI flash, can be rolled back by someone holding the open machine. "
  "On newer platforms rollback protection is delegated to the flash chip's Replay Protected Monotonic Counters (RPMC); they found that Winbond RPMC flash leaks its HMAC key under voltage glitching (allowing counter forgery), that AMD's NV controller never verifies that an RPMC increment happened so an interposer can suppress it, and that AMD platforms without RPMC flash appear to have no rollback protection at all (reflashing an old image reset the counters on two desktops). "
  "End to end on locked, encrypted laptops they found a four-digit Windows Hello PIN in 40 hours worst case instead of 69 days and, for BitLocker's TPM+PIN pre-boot protector, cut the worst case for a default six-digit PIN from 19 years to 20 days (test PINs found within 236 tries; the BitLocker test took under seven minutes). "
  "AMD's bulletin of 2026-11-17 (CVE-2026-43613, CVSS 4.0 5.1) states that physical attacks are outside its threat model but that RPMC is meant to stop exactly this interposer attack, and schedules firmware mitigations between November 2026 and December 2026 for most Ryzen, Threadripper and EPYC 4004/4005 lines and February 2027 for embedded parts. "
  "The attack needs physical access, board-level hardware and the flash chip; neither the paper nor the vendor notices describe use outside the lab. The researchers advise adding at least two digits to Hello and BitLocker PINs."
 ),
 "region_nexus": "global",
 "primary_sector_nexus": "indirect (managed laptops using BitLocker TPM+PIN or Windows Hello for Business; a lost or seized device is the scenario)",
 "sector": "cross-sector",
 "cves": ["CVE-2026-43613"],
 "techniques": ["T1200", "T1110.001"],
 "affected_products": ["AMD Ryzen processors (AMD-SB-7079 list)", "Windows Hello", "Microsoft BitLocker TPM+PIN", "Winbond RPMC SPI flash"],
 "entity_keys": [],
 "new_entities": [],
 "verification": "MULTI-SOURCE",
 "confidence": "HIGH",
 "novelty": "new",
 "lookback": True,
 "borderline": True,
 "borderline_reason": "Physical-access lab attack with no observed exploitation; included because the hardening lever (a longer pre-boot or Hello PIN on managed laptops) is concrete and cheap, the vendor has confirmed the flaw, and device loss or seizure is a standing risk for public-sector staff. Hold to a short entry or drop if the brief is crowded.",
 "suggested_priority": "notable (low)",
 "suggested_classification": {"reliability": "A", "credibility": 1},
 "sourcing_note": "Academic primary (arXiv) plus the chipmaker's own bulletin confirming the flaw: independent, first-party. Intel's position and the Pluton claim are not established by the cited pages (the researchers expect, but did not show, Pluton-based AMD PCs to be affected).",
 "evidence": [
  ev("We demonstrate this end-to-end on locked, encrypted hardware: our setup finds a 4-digit Windows Hello PIN in 40 hours instead of 69 days.", "arXiv (Werling et al., TU Berlin)", U_AX),
  ev("The same primitive defeats BitLocker's TPM+PIN pre-boot protector, reducing the worst-case time for a default-length 6-digit PIN from 19 years to 20 days.", "arXiv (Werling et al., TU Berlin)", U_AX),
  ev("While attacks requiring physical access to the system are outside of the AMD product security threat model, RPMC is intended to stop this type of interposer attack and AMD plans to release firmware updates to mitigate this issue.", "AMD (AMD-SB-7079)", U_AMD),
  ev("Until updated firmware is available, AMD recommends following security best practices, including maintaining physical control of systems and monitoring for signs of physical tampering.", "AMD (AMD-SB-7079)", U_AMD),
  ev("For now, the researchers advise adding at least two digits to Hello and BitLocker PINs.", "The Hacker News", U_HNTPM),
 ],
 "extended_notes": (
  "EXPOSURE: AMD PCs with the listed Ryzen/Threadripper/EPYC parts (AMD-SB-7079 names AGESA/PI builds per family with target months Nov'26, Dec'26 or Feb'27 for embedded); PCs using Winbond RPMC flash whatever the processor (the researchers say only a new chip design fixes the leaked-key method); some Intel PCs without RPMC-like flash. Per The Hacker News the owner can boot Linux and run the researchers' exposure check (grep over /sys/bus/pci/drivers/ccp/*/rpmc_*) to see whether RPMC flash is present and enabled; missing files do not prove absence.\n"
  "DETECTION: little at the endpoint (a physical attack): chassis-intrusion or tamper telemetry, repeated pre-boot PIN failures that reset, unexplained firmware-setting changes (the researchers slowed the flash link in firmware settings); AMD advises monitoring for signs of physical tampering.\n"
  "DEFENDER TAKEAWAY: lengthen or complexity-raise BitLocker startup PINs and Windows Hello PINs on managed laptops (enhanced alphanumeric PIN where policy allows) and track the AMD firmware drops; a recovered Hello PIN also unlocks device-bound keys and Hello-based SSO per the researchers (claimed, not demonstrated).\n"
  "Not stated: Intel's formal advisory position (search snippet only, not fetched); whether Microsoft changed lockout defaults."
 ),
})

# ---------------------------------------------------------------- 6. Depthfirst database RCE
items.append({
 "title": "Depthfirst: low-privilege SQL roles reach native engine bugs in PostgreSQL (CVE-2026-116331), MySQL (CVE-2026-101786), ClickHouse and, through a two-bug chain it calls unauthenticated, Oracle Database (CVE-2026-114819 CVSS 9.9 with ORDS CVE-2026-91609); all fixed",
 "sources": [
  {"url": U_DF, "publisher": "Depthfirst (Zheng Yu)", "date": "2026-11-18", "role": "primary"},
  {"url": U_PG, "publisher": "PostgreSQL Global Development Group", "date": "2026-11-19", "role": "corroborating"},
  {"url": U_ORA, "publisher": "Oracle (November 2026 Critical Security Patch Update)", "date": "2026-11-17", "role": "corroborating"},
  {"url": U_HNDB, "publisher": "The Hacker News", "date": "2026-11-19", "role": "corroborating"},
 ],
 "discovery_trace": "first seen at: hackernews feed, URL https://feeds.feedburner.com/TheHackersNews item https://thehackernews.com/2026/11/researcher-demonstrates-database-rce.html -> primary: Depthfirst research post, URL https://depthfirst.com/research/narrow-grants-wide-engines -> vendor: PostgreSQL CVE page, URL https://www.postgresql.org/support/security/CVE-2026-116331/ ; Oracle November CSPU, URL https://www.oracle.com/security-alerts/cspunov2026.html (CVE row verified); Oracle October CPU (ORDS row verified) and MySQL October advisory fetched",
 "summary": (
  "Depthfirst researcher Zheng Yu argues that SQL GRANTs gate tables, not the C and C++ engine code a session can still drive, and shows chains from minimal roles to code execution as the database's OS service account. "
  "PostgreSQL CVE-2026-116331 (CVSS 3.x 8.8, fixed 2026-11-12 in 18.7, 17.12, 16.16, 15.20 and 14.25): the min/max aggregate SORTOP shortcut skips FINALFUNC, so a pass-by-value int8 is read as a pass-by-reference pointer; a default login role gets there entirely inside its pg_temp schema through the default TEMPORARY privilege. "
  "MySQL CVE-2026-101786 (Server and Cluster 26.7.0 to 26.7.1, fixed in Oracle's October update, Oracle CVSS 7.2): an out-of-bounds write in windowed BIT_OR counters reached with a prepared statement and a longer-than-prepared BLOB, exploited by an account holding only CREATE TEMPORARY TABLES. "
  "ClickHouse has no CVE: a length wraparound in RowBinary String reading, reachable over HTTP by setting format_binary_max_string_size=0, tested on 26.7.5.10 and fixed in September (26.9 and later, backports 26.8.3.41, 26.7.7.30, 26.6.5.55, 26.3.32.8). "
  "For Oracle, Depthfirst says CVE-2026-114819 (Oracle Text, CVSS 9.9 in Oracle's table, fixed in the November CSPU for 19.3-19.32, 21.3-21.24 and 23.4.0-23.26.3) chains with the Oracle REST Data Services GraphQL flaw CVE-2026-91609 (ORDS 24.2.0 to 26.2.1, fixed in October) so that an attacker who can reach the exposed HTTP endpoint runs commands before any login; Oracle's own table lists neither flaw as exploitable without authentication on its own, and The Hacker News notes the full chains were not independently reproduced. "
  "The Hacker News reports no sign of use in an attack."
 ),
 "region_nexus": "global; databases common in Swiss public-sector line-of-business systems (not source-stated)",
 "primary_sector_nexus": "direct (Oracle Database, PostgreSQL and MySQL are standard public-sector back ends; the Oracle chain is the pre-login claim)",
 "sector": "cross-sector",
 "cves": ["CVE-2026-116331", "CVE-2026-101786", "CVE-2026-114819", "CVE-2026-91609"],
 "techniques": ["T1190", "T1068"],
 "affected_products": ["PostgreSQL", "MySQL Server", "MySQL Cluster", "Oracle Database (Oracle Text)", "Oracle REST Data Services", "ClickHouse"],
 "entity_keys": [],
 "new_entities": [],
 "verification": "MULTI-SOURCE",
 "confidence": "MEDIUM",
 "novelty": "new",
 "lookback": True,
 "suggested_references": ["2026-11-18/oracle-november-2026-cspu-56-unauthenticated-critical-rows"],
 "suggested_priority": "notable",
 "suggested_classification": {"reliability": "B", "credibility": 2},
 "sourcing_note": "Vendor advisories confirm the CVEs, affected ranges and fixes (PostgreSQL page fetched; Oracle November CSPU row and October CPU ORDS row verified; MySQL October advisory row verified). The pre-authentication Oracle chain is the discoverer's claim and is hedged by Oracle's own table (both rows 'No' for exploitable without authentication individually) and by The Hacker News (chains not independently reproduced).",
 "evidence": [
  ev("fixes CVE-2026-114819 (CVSS 9.9), a vulnerability we reported in Oracle AI Database.", "Depthfirst", U_DF),
  ev("Together, the two vulnerabilities allow an unauthenticated attacker with access only to the exposed HTTP endpoint to smuggle a crafted document into the database and execute arbitrary commands as the database’s OS service user.", "Depthfirst", U_DF),
  ev("Versions before PostgreSQL 18.7, 17.12, 16.16, 15.20, and 14.25 are affected.", "PostgreSQL Global Development Group", U_PG),
  ev("On their own, the company rates neither as exploitable without a login.", "The Hacker News", U_HNDB),
  ev("None has been seen in a real attack.", "The Hacker News", U_HNDB),
 ],
 "extended_notes": (
  "EXPOSURE: version checks via SELECT version() (PostgreSQL before 18.7/17.12/16.16/15.20/14.25), MySQL 26.7.0-26.7.1, Oracle Database 19.3-19.32/21.3-21.24/23.4.0-23.26.3 without the November CSPU, ORDS 24.2.0-26.2.1 without the October CPU, ClickHouse older than the backport builds. The Oracle pre-login path needs the ORDS HTTP endpoint reachable.\n"
  "HARDENING named by Depthfirst: revoke the default TEMPORARY privilege from PUBLIC in PostgreSQL and avoid broad CREATE TEMPORARY TABLES ON *.* grants in MySQL and ClickHouse; least-privilege roles do not shrink the native attack surface and do not stop the pre-login Oracle path.\n"
  "DETECTION (derived from the stated mechanisms): database audit logs for CREATE AGGREGATE with SORTOP in pg_temp by application roles, prepared-statement BIT_OR window queries with oversized BLOB parameters, ClickHouse HTTP queries setting format_binary_max_string_size=0, repeated database-engine crashes (memory corruption grooming), and process-creation events where the DB service account (postgres, mysql, clickhouse, oracle) spawns a shell; ORDS GraphQL requests from unexpected sources.\n"
  "S1 may carry the Oracle row (CVE-2026-114819 CVSS 9.9) and the PostgreSQL release separately; merge into one entry if so."
 ),
})

# ---------------------------------------------------------------- 7. INCEPTION / O-UNC-053 (borderline)
items.append({
 "title": "Okta, ReversingLabs and Unit 42 on O-UNC-053: the vishing cluster formerly tied to the ShinyHunters leak site now publishes under INCEPTION, using legal-themed lookalike domains and an SSO kit that cannot defeat passkeys",
 "sources": [
  {"url": U_OK, "publisher": "Okta Threat Intelligence", "date": "2026-11-23", "role": "primary"},
  {"url": U_RL, "publisher": "ReversingLabs", "date": "2026-11-23", "role": "corroborating"},
  {"url": U_U42L, "publisher": "Unit 42 (timely threat intel note)", "date": "2026-11-23", "role": "corroborating"},
  {"url": U_HNOK, "publisher": "The Hacker News", "date": "2026-11-24", "role": "corroborating"},
 ],
 "discovery_trace": "first seen at: hackernews feed, URL https://feeds.feedburner.com/TheHackersNews item https://thehackernews.com/2026/11/okta-links-shinyhunters-associated.html -> primary: Okta Threat Intelligence, URL https://www.okta.com/blog/threat-intelligence/former_shinyhunters_cluster_moves_to_new_inception_site/ -> corroboration: ReversingLabs, URL https://www.reversinglabs.com/blog/threat-researchers-notebook-sso-vishing-campaign-associated-with-emerging-inception-extortion-group ; Unit 42 timely-threat-intel note, URL https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-23-Legal-themed-vishing-activity.txt",
 "summary": (
  "Okta Threat Intelligence reports that organisations targeted by its cluster O-UNC-053, active since March 2026, began appearing on 2026-11-16 on a new leak site branded INCEPTION instead of the ShinyHunters site that published its targets between March and September, which went offline after arrests of alleged ShinyHunters members. "
  "The cluster runs voice-phishing calls in which callers, often posing as support staff, press users to reset passwords; a web phishing kit then harvests the username and password and prompts for the one-time code or push approval, and Okta says the kit cannot bypass phishing-resistant authentication such as Okta FastPass or FIDO2/WebAuthn passkeys. "
  "Since late October the lookalike domains follow legal-<target>.com, legaldept-<target>.com, <target>.legal and <target>-legal.com patterns, are registered on or within a day of a campaign (some the day of the call), sit behind Cloudflare and rotate theme every four to six weeks. "
  "ReversingLabs analysed 21 domains, found a filtered kit that tailors pages to a target's Okta or NetIQ tenant while redirecting other visitors to the real sign-in, and notes the domains carry no MX, DKIM or DMARC records; Unit 42 counted more than 70 such domains since October. "
  "Okta assesses the cluster \"very likely\" changed brand and says it cannot rate with high confidence whether it runs the leak site or partners with another extortion actor; INCEPTION publicly denies any ShinyHunters link, and the seven victims it lists (US companies) are unverified claims. No public-sector victim is named by any source."
 ),
 "region_nexus": "US-centred victim list; no Swiss or European public-sector nexus stated",
 "primary_sector_nexus": "indirect (technique transferable to any Okta/NetIQ-style SSO helpdesk-reset workflow)",
 "sector": "cross-sector",
 "cves": [],
 "techniques": ["T1566.004", "T1111", "T1078", "T1665"],
 "affected_products": ["Okta", "NetIQ"],
 "entity_keys": ["actor:shinyhunters"],
 "new_entities": [
  {"key": "actor:o-unc-053", "type": "actor", "name": "O-UNC-053", "aliases": ["INCEPTION (leak-site brand)"],
   "summary": "Okta Threat Intelligence's designation for a vishing and SSO-phishing cluster active since March 2026 whose targets were listed on the ShinyHunters leak site until September 2026 and on the INCEPTION leak site from 2026-11-16 (Okta, 2026-11-23)."}
 ],
 "relation_suggestions": [
  {"subject": "actor:o-unc-053", "object": "actor:shinyhunters", "basis": "Okta assesses a significant relationship: targets of the cluster's infrastructure appeared on the ShinyHunters leak site, nature unclear; INCEPTION denies any ShinyHunters affiliation (Okta, 2026-11-23). Use overlaps-with at most."}
 ],
 "verification": "MULTI-SOURCE",
 "confidence": "MEDIUM",
 "novelty": "new",
 "borderline": True,
 "borderline_reason": "No public-sector or Swiss victim and the leak-site claims are unverified; included for the transferable helpdesk-vishing/SSO-relay technique, the phishing-resistant-MFA lever and the domain-pattern monitoring idea. Drop if the brief already carries comparable vishing items.",
 "suggested_priority": "low",
 "suggested_classification": {"reliability": "B", "credibility": 2},
 "sourcing_note": "Three independent analysts (Okta, ReversingLabs, Unit 42) agree on the domain pattern and tailored SSO kit; the ShinyHunters link is Okta's assessment and INCEPTION's denial is on record. Victim names on the leak site are claims.",
 "evidence": [
  ev("While this threat cluster has changed their brand affiliation, the operators remain active in targeting organizations with voice phishing attacks and account takeovers resulting in data theft and extortion.", "Okta Threat Intelligence", U_OK),
  ev("The kit is not capable of bypassing phishing-resistant methods of authentication such as Okta FastPass and FIDO2/WebAuthn passkeys.", "Okta Threat Intelligence", U_OK),
  ev("We cannot currently make a high confidence assessment as to whether O-UNC-053 is operating the DLS themselves or is partnering with another extortion actor.", "Okta Threat Intelligence", U_OK),
  ev("These listings represent unverified claims made by the adversary rather than independently confirmed breaches.", "ReversingLabs", U_RL),
  ev("We analyzed more than 70 observed domains", "Unit 42", U_U42L),
 ],
 "extended_notes": (
  "DETECTION: IdP sign-in logs for a successful password plus OTP/push from a new device or ASN shortly after a password reset request or helpdesk contact; brand-protection or certificate-transparency monitoring for newly registered legal-<yourorg>.com, legaldept-<yourorg>.com, <yourorg>.legal and <yourorg>-legal.com; DNS/proxy hits on those patterns. Domains have no mail records, so mail gateways will not see them (vishing, not email, delivers the link).\n"
  "HARDENING: enforce phishing-resistant authenticators (passkeys, FIDO2, FastPass) and remove OTP and push fallbacks (a kit can downgrade to them); verified-callback procedure for helpdesk resets; restrict sensitive applications to managed devices (Okta's recommendation).\n"
  "Okta's recommendations are Okta-specific and 'could be adapted for other solutions'."
 ),
})

# ---------------------------------------------------------------- 8. Volant Manticore (borderline)
items.append({
 "title": "Check Point Research: Volant Manticore, an Iran-nexus group of probable former MuddyWater operators, uses the IPFS-based KuboShell and the Homa framework against Cyprus telecoms, airlines and government, and Saudi healthcare",
 "sources": [
  {"url": U_CPR, "publisher": "Check Point Research", "date": "2026-11-24", "role": "primary"},
 ],
 "discovery_trace": "first seen at: checkpoint-research feed sweep (standing major-lab sweep, not a slice record), URL https://research.checkpoint.com/feed/ item https://research.checkpoint.com/2026/volant-manticore-flying-under-the-radar/ ; relayed by The Hacker News (feed item https://thehackernews.com/2026/11/iran-aligned-volant-manticore-uses-ipfs.html, not fetched) -> primary (extract)",
 "summary": (
  "Check Point Research describes a previously undocumented Iran-nexus cluster, Volant Manticore, tracing back to September 2025, after a fake CV delivering the KuboShell backdoor reached a Cyprus-based airline in July 2026. "
  "KuboShell is a 64-bit Windows backdoor that uses the Pinata IPFS pinning service for command and control (a MAC-address-named command file polled every 60 seconds, results returned only if the command writes to a file) and is a guardrail stage that profiles the host before a multi-stage PowerShell and JScript chain loads the Homa framework, whose client is a JavaScript reimplementation of MuddyWater's older MuddyC2Go client. "
  "Alongside the implants the group delivers RMM tools (MeshCentral, then NetLock RMM, and an N-able RMM installer) in lure archives and runs credential-harvesting pages, including an ADFS-style sign-in mimic; the operators' test machines carried Fortinet SSL VPN adapters, which Check Point reads as possible VPN access into victim networks. "
  "A January 2026 macro-laden Word lure likely aimed at a Cypriot government entity used a VBA backdoor with HTTP C2; since September 2026 the group pivoted to Saudi targets, particularly healthcare, with broader and rushed phishing. "
  "Check Point assesses with high confidence an Iran nexus, medium confidence a historical MOIS link, and with medium confidence that the cluster is a separate group of former MuddyWater operators rather than a MuddyWater subgroup, explicitly weighing six alternative hypotheses; it warns that treating the group as MuddyWater creates blind spots."
 ),
 "region_nexus": "Cyprus (EU) and Saudi Arabia; no Swiss nexus",
 "primary_sector_nexus": "indirect (government, telecom and airline targeting in an EU member state; transferable RMM-via-lure and IPFS-C2 techniques)",
 "sector": "cross-sector",
 "cves": [],
 "techniques": ["T1566.002", "T1219", "T1102.002", "T1059.001", "T1059.007"],
 "affected_products": [],
 "entity_keys": ["actor:muddywater"],
 "new_entities": [
  {"key": "actor:volant-manticore", "type": "actor", "name": "Volant Manticore", "aliases": [],
   "summary": "Iran-nexus espionage cluster named by Check Point Research (2026-11-24): KuboShell (IPFS/Pinata C2) and the Homa framework against Cyprus telecoms, airlines and government and Saudi healthcare; assessed with medium confidence as a separate group of former MuddyWater operators."},
  {"key": "tool:kuboshell", "type": "tool", "name": "KuboShell", "aliases": [],
   "summary": "Windows backdoor using the Pinata IPFS pinning service for command and control, a first-stage guardrail before the Homa framework (Check Point Research, 2026-11-24)."},
  {"key": "tool:homa-framework", "type": "tool", "name": "Homa Framework", "aliases": ["Homa"],
   "summary": "Multi-stage post-compromise framework whose JScript client reimplements MuddyWater's MuddyC2Go client; used by Volant Manticore (Check Point Research, 2026-11-24)."}
 ],
 "relation_suggestions": [
  {"subject": "actor:volant-manticore", "object": "actor:muddywater", "basis": "Check Point assesses with medium confidence that Volant Manticore is a separate group composed of former MuddyWater operators, while tooling overlaps (MuddyC2Go reimplementation) exist; use overlaps-with, not an alias (Check Point Research, 2026-11-24)."},
  {"subject": "actor:volant-manticore", "object": "tool:kuboshell", "basis": "Check Point: the group uses KuboShell as its first-stage backdoor (Check Point Research, 2026-11-24)."}
 ],
 "verification": "SINGLE-SOURCE-OTHER",
 "confidence": "MEDIUM",
 "novelty": "new",
 "borderline": True,
 "borderline_reason": "Regional Iran-nexus espionage (Cyprus, Saudi Arabia) with no Swiss or Swiss-neighbour public-sector nexus; kept only as a borderline for the RMM-in-lure-archive and IPFS/Pinata-API C2 behaviours. The Hacker News relays it, so the main agent can drop it without losing a unique source.",
 "suggested_priority": "low",
 "suggested_classification": {"reliability": "B", "credibility": 2},
 "sourcing_note": "Check Point Research is the only analyst; attribution is graded (high Iran nexus, medium MOIS and ex-MuddyWater) with competing hypotheses laid out in the primary. HN relay not fetched.",
 "evidence": [
  ev("KuboShell is a 64-bit Windows backdoor that uses the InterPlanetary File System (IPFS) for command-and-control (C2) communication.", "Check Point Research", U_CPR),
  ev("The downloaded text is passed to PowerShell in a hidden window.", "Check Point Research", U_CPR),
  ev("we assess with medium confidence that Volant Manticore is a separate, independent group composed of former MuddyWater operators", "Check Point Research", U_CPR),
 ],
 "extended_notes": (
  "DETECTION (behaviour): outbound API calls to a commercial IPFS pinning service (Pinata) and its public gateway from workstations, followed by hidden-window PowerShell; files named <MAC>.log/.txt written under C:\\Users\\Public; installs of RMM agents (NetLock, MeshCentral, N-able) from archives downloaded from file-sharing hosts after a CV or seminar lure; PowerShell using Add-Type with the JScript language and a loop (Homa second stage).\n"
  "No IOCs carried. Triage: IT-sanctioned RMM installs are common; the discriminator is a user-launched installer from a downloaded archive with a lure-themed filename and an RMM tenant that is not the organisation's."
 ),
})

doc = {
 "domain": "S3",
 "run_id": RUN,
 "model": "Sonnet 5.5",
 "model_id": "claude-sonnet-5-5",
 "started_at": "2026-11-25T03:57:53Z",
 "ended_at": END_TS,
 "duration_seconds": DURATION,
 "self_telemetry": {"webfetch_calls": 4, "websearch_calls": 8, "bridge_fetches": 109},
 "items": items,
 "dropped_leads": [
  {"lead": "Bitdefender EggStreme variant (Philippine government, via The Hacker News 2026-11-18)", "reason": "China-nexus espionage on Philippine government, no Swiss or European nexus, primary not fetched"},
  {"lead": "Push Security: DOM-mirroring AiTM taxonomy (2026-11-18), GoodGuys fake expert-interview AiTM (2026-11-20), tech-support-scam RMM detections (2026-11-23)", "reason": "vendor taxonomy and telemetry shares with no new defender lever beyond passkeys and RMM allow-listing already covered; considered borderline, dropped to keep the brief sound"},
  {"lead": "Huntress ClickFix 'Buffet' (2026-11-23) and RMM 2 AM MSP story (2026-11-19)", "reason": "webinar recap and customer case study; ScreenConnect/timeroasting items already in the store"},
  {"lead": "Jamf Music.app TCC bypass (CVE-2026-86933, 2026-11-18)", "reason": "patched macOS-only local bypass, no exploitation"},
  {"lead": "Intel 471 manufacturing access-broker post (2026-11-18)", "reason": "manufacturing-sector statistics, no public-sector nexus"},
  {"lead": "Onapsis AI-in-SAP guide (2026-11-24) and automated patch validation post (2026-11-20)", "reason": "product marketing"},
  {"lead": "Unit 42 NGINX HTTP/2 UAF CVE-2026-123633 (2026-11-24 23:00) and HN VMware vCenter 'another 9.8 auth bypass', WHMCS SQLi, GnuPG GPGME (S1 territory)", "reason": "vulnerability items for S1; nginx2root and vCenter are already entries; the new vCenter VMSA (VMSA-2026-0010/0011 per Broadcom's Q&A) was not researched here"},
  {"lead": "CERT-In AI-assisted payment-fraud advisory CIAD-2026-0062 (via HN 2026-11-23)", "reason": "India financial sector, no nexus; primary not fetched"},
  {"lead": "SecurityWeek: European Commission data breach, CIA unclassified system breach (2026-11-24)", "reason": "incident disclosures for S4"},
 ],
 "candidate_sources": [
  {"id": "dragos-research-blog", "publisher": "Dragos (blog, HD Moore research series)", "url": "https://www.dragos.com/blog/", "category": "research",
   "why": "The new HD Moore research series (IT, LLM and xOT topics) produced the canary-token AI-inference study (2026-11-19) that no covered source had; the post extracts cleanly. Feed/listing recipe not yet probed."},
  {"id": "okta-threat-intelligence", "publisher": "Okta Threat Intelligence (blog)", "url": "https://www.okta.com/blog/threat-intelligence/", "category": "research",
   "why": "First-party tracking of vishing and SSO-phishing clusters (O-UNC-053, O-UNC-066) with the original assessment of the INCEPTION leak-site rebrand (2026-11-23); the post extracts cleanly. Feed/listing recipe not yet probed."},
 ],
 "coverage_gaps": [
  {"source_id": "reversinglabs-blog", "reason": "Not a gap: the candidate record contributed one corroborating citation this run (2026-11-23 SSO-vishing/INCEPTION post, read with extract); counts toward its three-run promotion bar. Existing sources greynoise and depthfirst were each the primary for one item here (GT13, database research); both are already active records."},
  {"source_id": "msft-ti", "reason": "Not in this slice; the Threat Intelligence topic page lists posts up to 2026-11-17 and the blog feed up to 2026-11-20; nothing in the 26 h window."},
  {"source_id": "mandiant-gtig", "reason": "Quiet: feed newest 2026-11-19 (ARMORY CASTLE vSphere, already covered by the vCenter entry); WebFetch of the listing shows no post beyond those in the feed; the listing carries no dates."},
  {"source_id": "hackernews", "reason": "Feed cap is 50 items (back to 2026-11-18 17:58); the horizon is 2026-11-18 02:00. The monthly archive https://thehackernews.com/2026/11/ was read to close most of the gap; the archive shows about 25 posts and is not strictly date-ordered, so a few items from 2026-11-18 02:00 to 17:58 may be unseen."},
  {"source_id": "push-security", "reason": "Recipe confirmed again: extract gives an undated list, WebFetch with a title/date/href prompt returned dates (listing covers about 10 posts per 100k characters; the page is 195k characters)."},
  {"source_id": "nau-ch", "reason": "Recipe works (url https://www.nau.ch/news/digital then extract per article); the listing is mostly consumer tech and the cyber items in the horizon (PHP site shutdowns in Lower Saxony 2026-11-20) are not Swiss."},
  {"source_id": "jamf-threat-labs", "reason": "Recipe confirmed: `url` on the category page returns /blog/<slug>/ links, `extract` per post gives a reliable date; only 2026-11-18 Music.app TCC post in the lookback."},
 ],
 "source_ledger": [
  {"id": "aws-security-blog", "tier": "standard", "attempted": True, "transport": "feed (direct)", "horizon_hours": 168, "in_horizon_items": 15, "returned": 0, "note": "15 posts in horizon, all product and compliance posts except 2026-11-20 Cairn zero-day post, already covered by monai-label-path-traversal entry"},
  {"id": "cloudflare-cf1", "tier": "standard", "attempted": True, "transport": "feed (direct)", "horizon_hours": 168, "in_horizon_items": 0, "returned": 0, "note": "newest feed item 2026-10-29"},
  {"id": "hackernews", "tier": "standard", "attempted": True, "transport": "feed + monthly archive url + extract per post", "horizon_hours": 168, "in_horizon_items": 52, "returned": 4, "note": "leads to Dragos canary-token research, TU Berlin TPM paper, Depthfirst database research and Okta/INCEPTION; each traced to its primary"},
  {"id": "huntress", "tier": "standard", "attempted": True, "transport": "feed + WebFetch listing + extract", "horizon_hours": 168, "in_horizon_items": 7, "returned": 0, "note": "ClickFix recap, MSP RMM case study, EU hosting, resilience essays; timeroasting already covered"},
  {"id": "ibm-xforce", "tier": "standard", "attempted": True, "transport": "bridge url + extract", "horizon_hours": 168, "in_horizon_items": 0, "returned": 0, "note": "six posts on the hub, newest 2026-10-19"},
  {"id": "intel471", "tier": "standard", "attempted": True, "transport": "feed (direct)", "horizon_hours": 168, "in_horizon_items": 1, "returned": 0, "note": "2026-11-18 manufacturing access-broker statistics post, no public-sector nexus"},
  {"id": "iverify-blog", "tier": "standard", "attempted": True, "transport": "bridge url --direct + extract per post", "horizon_hours": 168, "in_horizon_items": 1, "returned": 0, "note": "2026-11-23 BYOD minimum-OS post is product guidance; 2026-11-17 DarkSword post is outside the lookback"},
  {"id": "jamf-threat-labs", "tier": "standard", "attempted": True, "transport": "bridge url + extract per post", "horizon_hours": 168, "in_horizon_items": 1, "returned": 0, "note": "2026-11-18 Music.app TCC bypass, patched, no exploitation"},
  {"id": "mandiant-gtig", "tier": "standard", "attempted": True, "transport": "feed + WebFetch listing", "horizon_hours": 168, "in_horizon_items": 1, "returned": 0, "note": "2026-11-19 ARMORY CASTLE vSphere already covered by the vCenter entry"},
  {"id": "nau-ch", "tier": "standard", "attempted": True, "transport": "bridge url + extract", "horizon_hours": 168, "in_horizon_items": 0, "returned": 0, "note": "no Swiss cyber item in the lookback on /news/digital"},
  {"id": "onapsis", "tier": "standard", "attempted": True, "transport": "bridge url + extract per post", "horizon_hours": 168, "in_horizon_items": 2, "returned": 0, "note": "2026-11-20 and 2026-11-24 posts are product marketing"},
  {"id": "push-security", "tier": "standard", "attempted": True, "transport": "bridge url + WebFetch (dated listing) + extract", "horizon_hours": 168, "in_horizon_items": 3, "returned": 0, "note": "DOM-mirroring taxonomy, GoodGuys teardown, tech-support-scam stats considered and dropped"},
 ],
}

# ------------------------------------------------------------ verify quotes
def norm(s):
    s = s.replace("\\", "")
    s = re.sub(r"\s+", " ", s)
    return s.strip()

bad = 0
cache = {}
for it in items:
    for e in it.get("evidence", []):
        f = SRC.get(e["source_url"])
        if not f:
            print("NO SOURCE FILE", e["source_url"]); bad += 1; continue
        t = cache.setdefault(f, norm((EX / f).read_text(encoding="utf-8", errors="ignore")))
        if norm(e["quote"]) not in t:
            print("QUOTE NOT FOUND:", f, "|", e["quote"][:110]); bad += 1
print("quote failures:", bad)

out = W / "findings.S3.yaml"
if "--write" in sys.argv:
    out.write_text(yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")
    print("written", out)
