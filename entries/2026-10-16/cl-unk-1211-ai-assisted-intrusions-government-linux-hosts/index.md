---
schema: 1
kind: threat
title: "CL-UNK-1211: an AI-assisted intrusion set against government Linux web and mail servers persists through PHP auto_prepend_file, steals sudo passwords with a fake prompt and reads mail stores, and tries to pass as a red-team exercise"
headline: "Unit 42: government Linux web and mail hosts hit with PHP prepend persistence, a sudo password trap and mail searches"
summary: >
  Unit 42 reports CL-UNK-1211, a cluster of unknown nation-state or criminal affiliation that between October 2025 and April 2026 targeted government entities and state-affiliated infrastructure, focusing on Linux servers to run reconnaissance and keep persistent access for intelligence collection.
  Its scripts carry AI-style reasoning comments, which Unit 42 reads as LLM-generated code or an AI agent's work; the intrusions used PHP web shells with auto_prepend_file persistence on Plesk hosts, a replaced .bashrc that traps sudo passwords, SUID root shells, searches of mail directories and log cleanup. Unit 42 names no victim or country, does not say how the web shells were first placed, and is the only source.
discovered_at: "2026-10-16T04:21:00Z"
updated_at: null
event_date: "2026-10-15"
run_id: 2026-10-16T0256Z-intel
priority: notable
immediate_action: null
tags: [espionage, ai-abuse]
regions: [global]
sectors: [public-sector]
entities: ["actor:cl-unk-1211", "malware:sysgorat"]
techniques: [T1505.003, T1546.004, T1056, T1552.001, T1552.003, T1068, T1548.001, T1098.004, T1021.004, T1090, T1114.001, T1041, T1567, T1070.003, T1070.006, T1685, T1685.006, T1070.004, T1059.004, T1071.001, T1543.002, T1053.003, T1547.001, T1053.005, T1595.002]
affected_products: ["Plesk", "PHP"]
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-10-15"
    role: primary
closed_sources: []
evidence:
  - quote: "Unit 42 identified a campaign targeting government entities and state-affiliated infrastructure, with observed activity spanning from October 2025–April 2026. We track this activity as CL-UNK-1211."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/"
  - quote: "The attackers targeted official government mail servers to steal emails and facilitate access to external social media accounts."
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/"
  - quote: "They attempted to disguise their activity as a red team operation"
    publisher: "Palo Alto Networks Unit 42"
    source_url: "https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/"
verification: single-source
sourcing_note: >
  Unit 42 is the only source and the only observer; the report names no victim, country or victim count and does not say how the web shells were first placed. The AI-assistance reading is Unit 42's inference from the scripts' style, not a confirmed finding.
confidence: medium
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

Unit 42 reports a campaign it tracks as CL-UNK-1211 (UNK: affiliation undetermined) against government entities and state-affiliated infrastructure between October 2025 and April 2026, concentrating on Linux servers for persistent access and intelligence collection ([Unit 42, 2026-10-15](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/)). It names no victim or country and does not say how the web shells were first placed; the recovered tools include a custom Go scanner for CVE-2025-55182 (React2Shell) ([Unit 42, 2026-10-15](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/)). The scripts carry conversational, step-by-step comments in the style of an AI model, which Unit 42 reads as LLM-generated code or an AI agent's work, an inference rather than a confirmed finding ([Unit 42, 2026-10-15](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/)).

On the hosts, the attackers ran PHP web shells under the php-fpm parent process and rewrote auto_prepend_file in every PHP configuration under /etc/php/ and /opt/plesk/php/, so a planted file runs first ([Unit 42, 2026-10-15](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/)). They replaced a .bashrc with a copy that, in one instance, aliases sudo to a fake password prompt that logs the input, searched configuration and history files for credentials, escalated with LinPEAS and the public PwnKit exploit (CVE-2021-4034), left root-SUID shells under hidden names and injected an SSH key into authorized_keys ([Unit 42, 2026-10-15](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/)). They moved laterally with sshpass and hard-coded credentials and through an MSSQL double hop using xp_cmdshell, and kept access with SysGoRAT, a Go trojan that takes commands over WebSocket, plus the revsocks and pysoxy proxies and GSocket's gs-netcat, which ran from /dev/shm under a fake kernel-thread process name ([Unit 42, 2026-10-15](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/)). On government mail servers they enumerated /var/qmail/mailnames/, counted mails in Maildir folders to pick targets and searched mail headers for social-media messages; they tried to exfiltrate database dumps over netcat and to public file-hosting platforms, to delete authentication, history, mail and system logs and to kill endpoint security processes, timestomped scripts with touch -t, and planted a red-team marker string and a pentest-style password to pass as an authorised exercise ([Unit 42, 2026-10-15](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/)).

**Exposure:** Linux web and mail hosting estates of government or state-affiliated bodies, in particular Plesk-managed PHP stacks and their /var/qmail/mailnames/ mail directories, which the attackers enumerated and searched; the report does not say how the attackers got in ([Unit 42, 2026-10-15](https://unit42.paloaltonetworks.com/ai-campaign-targets-linux-infrastructure/)).

**Detection:** from the described behaviour: file-integrity monitoring on PHP configuration directories for any auto_prepend_file that points outside the application tree; shells or interpreters spawned by php-fpm or web server workers; writes to shell startup files, authorized_keys and any new sudo alias; PHP or web-server access to the mail store; new systemd units, five-minute cron entries and hidden-name SUID-root binaries; outbound WebSocket, GSocket or file-hosting connections from servers; touch -t changes, bursts of deleted history and mail logs, and pkill sequences that name EDR agents.

**Triage:** Plesk or PHP hardening can legitimately set auto_prepend_file and administrators do define sudo aliases; the report supports these discriminators: a prepended file with a vendor-like name outside the application tree, an alias that prompts for and logs the password, a log file named after another product, and red-team marker strings that no change record explains.

**Defender takeaway:** audit every PHP configuration for auto_prepend_file, privileged accounts' startup files for a sudo alias and authorized_keys for unknown keys, and the file system for root-SUID binaries under hidden names; ship authentication, mail and web logs off-host so local log cleanup cannot erase them; patch PwnKit and keep Linux EDR self-protection alerting.
