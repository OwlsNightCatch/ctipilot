---
schema: 1
kind: threat
title: "GreyNoise GT13: an unattributed actor that GreyNoise believes used LLM tooling held persistent access to at least 24 Check Point Security Management servers at 22 organisations, government among them, using CVE-2026-16232 and a Rejetto HFS relay hijacked through CVE-2026-61500"
headline: "GT13 holds Check Point management servers at 22 organisations; patching does not evict it, check audit logs"
summary: >
  GreyNoise reports that an actor it tracks as GT13 had persistent access to at least 24 Check Point Security Management servers at 22 organisations in 17 named countries and territories (Switzerland is not among them), government among seven sectors, with confirmed activity from 2026-10-17 to 2026-11-02. The actor used a script for the SmartConsole authentication bypass CVE-2026-16232, which Check Point confirms and which has been fixed since July, to launch more than 100 management tasks that copied the firewall database and the internal certificate authority. GreyNoise does not know how the actor first got in or who it is, and expects the campaign to be ongoing.
discovered_at: "2026-11-25T04:38:00Z"
updated_at: null
event_date: "2026-11-23"
run_id: 2026-11-25T0356Z-intel
priority: high
immediate_action: null
tags: [ai-abuse, actively-exploited, auth-bypass]
regions: [global]
sectors: [public-sector, finance, energy, transport, manufacturing]
entities: [actor:gt13, product:check-point-security-management-server, product:check-point-smartconsole, product:rejetto-hfs]
techniques: [T1190, T1606.001, T1098.004, T1572, T1046, T1110.003, T1090.003, T1584.004, T1686.002, T1105, T1059.006]
affected_products: ["Check Point Security Management Server", "Rejetto HFS"]
cves:
  - id: CVE-2026-16232
    cvss: "9.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, cisa-kev, poc-public, patch-available]
    affected: "Security Management and Multi-Domain Security Management R82.10, R82, R81.20 (R81.10 and R81 end of support), with Trusted Clients unrestricted"
    fixed: "Jumbo Hotfix Accumulator: R82.10 from Take 36, R82 from Take 118, R81.20 from Take 158"
  - id: CVE-2026-61500
    cvss: "9.3"
    epss: null
    type: auth-bypass
    vector: zero-click
    auth: pre-auth
    status: [exploited, patch-available]
    affected: "Rejetto HFS 3.0.0 to below 3.2.1"
    fixed: "3.2.1"
sources:
  - url: "https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign"
    publisher: "GreyNoise"
    date: "2026-11-23"
    role: primary
  - url: "https://www.bleepingcomputer.com/news/security/hackers-compromise-check-point-servers-in-22-organizations/"
    publisher: "BleepingComputer"
    date: "2026-11-24"
    role: corroborating
  - url: "https://support.checkpoint.com/results/sk/sk185169"
    publisher: "Check Point"
    date: "2026-09-24"
    role: corroborating
  - url: "https://www.vulncheck.com/advisories/rejetto-hfs-session-forgery-via-predictable-signing-key"
    publisher: "VulnCheck"
    date: "2026-07-13"
    role: corroborating
  - url: "https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-check-point-smartconsole-authentication-bypass-cve-2026-16232/"
    publisher: "Check Point"
    date: "2026-07-22"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Over the Chisel tunnel, and by using a script for CVE-2026-16232 (Check Point SmartConsole auth bypass to Run Script), the actor launched over 100 management tasks on multiple Check Point Management Servers."
    publisher: "GreyNoise"
    source_url: "https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign"
  - quote: "leading us to believe this exploitation was indeed CVE-2026-61500 for session forgery, which was not patched on this server."
    publisher: "GreyNoise"
    source_url: "https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign"
  - quote: "We are aware of the activity outlined by the GreyNoise article. The attackers used CVE-2026-16232, a SmartConsole authentication bypass vulnerability that Check Point publicly disclosed in July 2026, with a note that exploitation had been observed in the wild."
    publisher: "Check Point (statement quoted by BleepingComputer)"
    source_url: "https://www.bleepingcomputer.com/news/security/hackers-compromise-check-point-servers-in-22-organizations/"
verification: single-source
sourcing_note: "GreyNoise is the only first-hand observer of the campaign. Check Point's reply, quoted by BleepingComputer on 2026-11-25, confirms only that CVE-2026-16232 was used and does not confirm the victim count, persistence or the relay. CVE-2026-16232's 9.3 is Check Point's own score. GreyNoise's belief that the actor used LLM and agentic tooling is its own assessment; BleepingComputer's reading that the activity resembled cyberespionage is the outlet's, not GreyNoise's."
confidence: medium
references:
  - 2026-07-23/check-point-smartconsole-auth-bypass-cve-2026-16232
  - 2026-07-13/rejetto-hfs-session-forgery-prng-rce-cve-2026-61500
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "On every Check Point Security Management and Multi-Domain Security Management server, confirm the Jumbo Hotfix Accumulator is installed (R82.10 from Take 36, R82 from Take 118, R81.20 from Take 158), limit Trusted Clients to named administrator addresses, then search the Audit Logs View for \"Authentication method: Password based application token\" and for any unrecognised administrator name or source address; on a hit, treat the server as compromised, check /etc/ld.so.preload and unfamiliar SSH private keys and treat the firewall database, the internal CA and stored credentials as stolen, because GreyNoise saw the actor copy them from multiple servers and a patch does not evict that access."
updates: []
migrated_from: null
---

GreyNoise reports an intrusion campaign it tracks as GT13 against Check Point Security Management servers: at least 22 organisations and 24 servers, confirmed activity against the Check Point servers from 2026-10-17 to 2026-11-02 and the actor's relay observed from 2026-10-02, victims in 17 named countries and territories (Germany, Austria and France among them, Switzerland not named) and sectors including government, financial services, energy and transportation ([GreyNoise, 2026-11-23](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign)). GreyNoise could not determine when or how the actor first reached the Check Point servers, only that it did so before compromising the Rejetto HFS server it used as a relay; it does not attribute GT13, cannot judge motive and believes that the actor used LLM and agentic tooling ([GreyNoise, 2026-11-23](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign)).

The actor ran a script for the SmartConsole authentication bypass CVE-2026-16232, purportedly adapted from the Metasploit module, to launch more than 100 management tasks, among them copying the firewall database and the internal certificate authority, minting a certificate and unloading security policies, which would disable the firewall ([GreyNoise, 2026-11-23](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign)). Check Point confirmed the use of CVE-2026-16232 and called the flaw and its protections not new ([BleepingComputer, 2026-11-24](https://www.bleepingcomputer.com/news/security/hackers-compromise-check-point-servers-in-22-organizations/)); the fixes are Jumbo Hotfix Accumulator R82.10 from Take 36, R82 from Take 118 and R81.20 from Take 158, and exploitation needs internet access to the management server with no restriction on Trusted Clients ([Check Point, 2026-09-24](https://support.checkpoint.com/results/sk/sk185169)); Check Point's disclosure table scores the flaw 9.3 and lists exploitation against a handful of customers with a specific configuration ([Check Point, 2026-07-22](https://blog.checkpoint.com/security/security-advisory-action-required-active-exploitation-of-check-point-smartconsole-authentication-bypass-cve-2026-16232/)). The relay was taken over by forging an HFS session cookie after recovering the signing key from login responses (CVE-2026-61500, HFS 3.0.0 to below 3.2.1) ([GreyNoise, 2026-11-23](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign); [VulnCheck, 2026-07-13](https://www.vulncheck.com/advisories/rejetto-hfs-session-forgery-via-predictable-signing-key)).

The actor planted an SSH key on its relay, and GreyNoise concludes from scp deliveries that each compromised device holds the matching private key; it also ran Nmap and a Chisel reverse proxy, used at least 30 Python scripts with victim-themed credential lists, and probed NetScaler, Ivanti Connect Secure, vCenter, Exchange, Oracle TNS assets and domain controllers without any stated success. A bulk certificate task to 24 servers failed on each; GreyNoise notified victims directly or through government partners and expects the campaign to be ongoing ([GreyNoise, 2026-11-23](https://www.greynoise.io/blog/check-point-security-management-servers-intrusion-campaign)).

**Exposure:** any Check Point Security Management or Multi-Domain Security Management server on R82.10, R82, R81.20 or an unsupported earlier train, below the fixed Jumbo Hotfix Accumulator, whose Trusted Clients list was unrestricted, reached from the internet or from a compromised internal host.

**Detection:** in management-server audit logs, SmartConsole sessions authenticated by "Password based application token", which Check Point says to treat as suspicious and check for an unrecognised administrator name or address ([Check Point, 2026-09-24](https://support.checkpoint.com/results/sk/sk185169)); script-run, certificate-management and policy-unload events; outbound SSH or scp from management servers to the relay and other non-administrator hosts; unfamiliar SSH private keys and a registration in /etc/ld.so.preload, which GreyNoise says may indicate an implant; tunnelling-tool process creation. A server patched later still needs this check, reaching back to at least early October, since the actor held persistent access and copied the internal CA.

**Defender takeaway:** install the fixed Jumbo Hotfix Accumulator and restrict Trusted Clients now, then treat any server with an unexplained application-token login as a compromised management plane: review policy changes and rebuild trust where the internal CA or stored credentials left.
