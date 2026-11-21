---
schema: 1
kind: annual-report
title: "Elastic threats, etc. report, November 2026: signed AI assistants as execution parents, RMM agents as the payload, paste-and-run infostealers and legacy-protocol identity abuse"
headline: "Elastic quarterly report: intrusions run through signed AI assistants, RMM agents and ROPC sign-ins"
summary: >
  Elastic Security Threat Command's quarterly report of 2026-11-04, on confirmed intrusions and research from 2026-04-04 to 2026-09-08,
  documents attackers operating through trusted software: Claude Code and the ChatGPT desktop app as parents of tunnelling and keychain
  theft, 23 confirmed RMM abuse findings led by ScreenConnect, paste-and-run infostealer delivery, and identity abuse through the ROPC grant,
  which Conditional Access does not evaluate, and device-code phishing that ends in a registered device and a primary refresh token.
discovered_at: "2026-11-08T14:20:00Z"
updated_at: null
event_date: "2026-11-04"
run_id: 2026-11-08T1309Z-audit
priority: notable
immediate_action: null
tags: [ai-abuse, infostealer, identity, cloud]
regions: [global]
sectors: []
entities: ["report:elastic-threats-etc-2026-11"]
techniques: [T1059.001, T1572, T1555.001, T1543.001, T1219, T1204.004, T1055.012, T1190, T1505.003, T1078.004, T1098.005]
affected_products: []
cves: []
sources:
  - url: "https://www.elastic.co/pdf/elastic-threats-etc-elastic-security-threat-command-nov-2026.pdf"
    publisher: "Elastic Security Threat Command (threats, etc. report, November 2026)"
    date: "2026-11-04"
    role: primary
  - url: "https://www.elastic.co/security-labs/reports/threats-etc-report-november-2026-trouble-with-trust"
    publisher: "Elastic Security Labs (report summary)"
    date: "2026-11-04"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Out of 23 confirmed RMM abuse findings this quarter, ScreenConnect was the product named most often."
    publisher: "Elastic Security Labs (report summary)"
    source_url: "https://www.elastic.co/security-labs/reports/threats-etc-report-november-2026-trouble-with-trust"
  - quote: "RMM abuse is an inventory problem before it is a detection problem"
    publisher: "Elastic Security Threat Command (threats, etc. report, November 2026)"
    source_url: "https://www.elastic.co/pdf/elastic-threats-etc-elastic-security-threat-command-nov-2026.pdf"
verification: single-source
sourcing_note: >
  Elastic's report is its own account of intrusions it confirmed and research it ran, with no second observer. Its window ends on
  2026-09-08, so several cases predate the report by months.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions: []
updates: []
migrated_from: null
---

Elastic Security Threat Command's November 2026 threats, etc. report covers activity it observed between 2026-04-04 and 2026-09-08 and says its counts are observations, not market share or a count of victims ([Elastic Security Threat Command, 2026-11-04](https://www.elastic.co/pdf/elastic-threats-etc-elastic-security-threat-command-nov-2026.pdf)). Its thread is intrusions run through signed, legitimate products: remote monitoring agents, AI coding assistants and Microsoft first-party clients ([Elastic Security Labs, 2026-11-04](https://www.elastic.co/security-labs/reports/threats-etc-report-november-2026-trouble-with-trust)).

On Windows an operator drove Claude Code through its VS Code extension over RDP to stage tooling and reach a self-hosted GitLab instance through a SOCKS5 proxy tunnel; Elastic's rules fired on PowerShell children of claude.exe and repeated curl.exe calls with --socks5-hostname against port 1080. On macOS the ChatGPT desktop application acted as a shell command proxy for a zsh pipeline that ran security dump-keychain against the login keychain, and in two coding-agent cases a session started with permission-bypass flags stood up a Cloudflare quick tunnel and installed LaunchAgent persistence ([Elastic Security Threat Command, 2026-11-04](https://www.elastic.co/pdf/elastic-threats-etc-elastic-security-threat-command-nov-2026.pdf)).

Of 23 confirmed RMM abuse findings, ScreenConnect was named most often ([Elastic Security Labs, 2026-11-04](https://www.elastic.co/security-labs/reports/threats-etc-report-november-2026-trouble-with-trust)). In the SILENTCONNECT chain a CAPTCHA page framed as a digital invitation drops a VBS script from Cloudflare r2.dev storage and ends in a silent ScreenConnect install whose client runs as a Windows service and beacons to the attacker's server on TCP 8041. In TOLLBOOTH an actor tracked as REF3927 entered a misconfigured IIS server through ViewState deserialization with publicly leaked ASP.NET machine keys, deployed a Godzilla-forked web shell and, when account creation failed, installed GotoHTTP as fallback access over ports 80 and 443 ([Elastic Security Threat Command, 2026-11-04](https://www.elastic.co/pdf/elastic-threats-etc-elastic-security-threat-command-nov-2026.pdf)).

A compromised university account reached Azure Resource Manager over the ROPC grant from an anonymized address known to be malicious; every successful attempt returned a token, and Conditional Access was bypassed because ROPC never traverses the surface the policy governs. A Kali365 device-code compromise ended with a registered device and a primary refresh token ([Elastic Security Threat Command, 2026-11-04](https://www.elastic.co/pdf/elastic-threats-etc-elastic-security-threat-command-nov-2026.pdf)).

**Exposure:** endpoints where AI coding assistants or desktop AI clients may run shell commands, endpoints that can install RMM agents the organisation does not use, Entra tenants that still accept the ROPC grant or device-code sign-in, and IIS servers whose ASP.NET machine keys have been published.

**Detection:** in process lineage, PowerShell, curl with --socks5-hostname or security dump-keychain under claude.exe or the ChatGPT desktop app; a ScreenConnect client beaconing to an unknown host on TCP 8041 or an RMM process hollowing MSBuild.exe; in Entra sign-in logs, successful ROPC sign-ins with BAV2RPOC user agents from anonymized hosting addresses, and a device registration followed by a primary refresh token after a device-code sign-in ([Elastic Security Threat Command, 2026-11-04](https://www.elastic.co/pdf/elastic-threats-etc-elastic-security-threat-command-nov-2026.pdf)).

**Triage:** Elastic says the same primitive is often both normal product behavior and confirmed theft, so judge an AI-assistant child process by its outcome (a proxy tunnel, a keychain read), not by the signed parent ([Elastic Security Threat Command, 2026-11-04](https://www.elastic.co/pdf/elastic-threats-etc-elastic-security-threat-command-nov-2026.pdf)).

**Defender takeaway:** Elastic calls RMM abuse an inventory problem before a detection problem: knowing which agents the organisation pays for turns every other vendor name into a high-confidence alert ([Elastic Security Threat Command, 2026-11-04](https://www.elastic.co/pdf/elastic-threats-etc-elastic-security-threat-command-nov-2026.pdf)). In Entra, a tenant that still allows ROPC has a sign-in path its Conditional Access policies never evaluate.
