---
schema: 1
kind: threat
title: "Velvet Ant \"Operation Highland\": subverting the Linux authentication stack for a decade"
headline: "Velvet Ant \"Operation Highland\": subverting the Linux authentication stack for a decade"
summary: "China-nexus Velvet Ant lived inside an air-gapped network for ~10 years by trojanising the Linux login stack itself — nine backdoored pam_unix.so variants and a credential-logging sshd, invisible to EDR. Today's deep dive is a binary-integrity hunt playbook for any Linux fleet (The Hacker News, 2026-06-12)."
discovered_at: "2026-06-13T05:00:09Z"
event_date: 2026-06-12
run_id: 2026-06-13-40b26572
priority: high
immediate_action: null
tags:
  - nation-state
  - espionage
  - china-nexus
  - identity
regions:
  - global
sectors:
  - public-sector
  - finance
  - manufacturing
entities:
  - "campaign:velvet-ant-operation-highland-2026"
cves: []
sources:
  - url: "https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html"
    publisher: The Hacker News
    role: primary
  - url: "https://www.sygnia.co/blog/operation-highland-velvet-ant/"
    publisher: Sygnia — Operation Highland
    role: corroborating
  - url: "https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/"
    publisher: Sygnia — Velvet Ant prior reporting
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: apt-campaign
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-06-13.md
---

**Background.** Velvet Ant is a China-nexus espionage actor Sygnia has tracked across several long-dwell intrusions, most prominently a multi-year campaign that abused legacy Cisco Nexus switch persistence and F5 BIG-IP appliances as internal footholds to survive repeated eradication attempts ([Sygnia — Velvet Ant prior reporting](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/)). The throughline across those engagements is patience and a preference for living in places defenders rarely image or hash-verify: network gear, load balancers, and now the host authentication layer. Operation Highland extends that pattern from network appliances to the Linux login path itself.

Sygnia's Operation Highland report, relayed in detail by The Hacker News on 12 June, describes Velvet Ant maintaining covert access to an **air-gapped network for nearly a decade**, with the earliest traces around 2016 ([The Hacker News, 2026-06-12](https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html); [Sygnia — Operation Highland](https://www.sygnia.co/blog/operation-highland-velvet-ant/)). Because the target network had no direct internet connectivity, the group first compromised internet-facing perimeter hosts and engineered a deliberate multi-stage path inward — there was no single exploit, just abuse of trusted administration once inside.

The core of the operation is subversion of the components that decide who may log in. Velvet Ant deployed **nine distinct compiled variants of `pam_unix.so`** — the primary PAM password module — across hosts. Some variants accept a hard-coded magic password that grants access as any user while leaving normal authentication intact; others silently write the real credentials typed by legitimate users to disk for later harvesting (`T1556.003` — [Modify Authentication Process: Pluggable Authentication Modules](https://attack.mitre.org/techniques/T1556/003/)). In parallel, the `sshd`/`ssh` binaries were replaced with backdoored copies that log every username, password and command, and carry an attacker flag to suppress that logging during the operators' own sessions (`T1554` — [Compromise Host Software Binary](https://attack.mitre.org/techniques/T1554/)). Harvested credentials then enable ordinary-looking authenticated movement (`T1078` — [Valid Accounts](https://attack.mitre.org/techniques/T1078/); `T1021.004` — [Remote Services: SSH](https://attack.mitre.org/techniques/T1021/004/)), and the trojanised modules are placed at their legitimate paths under `/lib/security/` and `/usr/sbin/` so nothing looks out of place (`T1036.005` — [Masquerading: Match Legitimate Name or Location](https://attack.mitre.org/techniques/T1036/005/)).

The defensive lesson is the part worth internalising: **this class of compromise is invisible to the telemetry most SOCs rely on.** A backdoored `pam_unix.so` produces no failed-login events, spawns no anomalous child process, and drops no second-stage userland implant for EDR to catch — the malice lives inside a trusted system library behaving normally for everyone except the attacker. Password resets and standard IR containment do not evict it, because the authentication decision itself is owned by the adversary. Detection therefore has to move to **filesystem and binary integrity** rather than behaviour:

- Verify the on-disk `pam_unix.so`, `sshd` and `ssh` binaries against authoritative package-manager checksums — `rpm -V openssh-server` / `dpkg --verify openssh-server` on every Linux host, and a hash comparison of `/lib/security/pam_unix.so` (and the distro's PAM module directory) against the package-provided value. Any mismatch or unexpected modification timestamp on these files is a triage trigger, not a curiosity.
- Deploy file-integrity monitoring (AIDE, Tripwire, or equivalent) on the authentication components specifically, and put OS auth-stack changes under separate change management so a legitimate update is distinguishable from tampering. On Linux endpoints with file-creation telemetry (Sysmon for Linux EID 11), alert on modification of `/lib/security/pam_unix.so` and `/usr/sbin/sshd`.
- Threat-hunt the credential-harvesting side effect: look for successful SSH logins that coincide with unusual source IPs or off-hours timing, and remember that PAM-module replacement will *not* generate failed-login noise to anchor on. Hunt for unexpected credential-log files left in world-writable or dot-prefixed locations.

Hardening that removes or shrinks the attack path: immutable OS partitions or `dm-verity` for high-value isolated systems so authentication binaries cannot be silently rewritten; FIM in detect-and-block mode on the auth stack; and, for genuinely air-gapped networks, outbound filtering on the internet-facing pivot hosts the actor needs to stage the multi-step path inward. The strategic takeaway for a public-sector SOC: your Linux fleet's `pam_unix.so` and `sshd` are as much a crown-jewel integrity target as your domain controllers, and almost certainly far less monitored.
