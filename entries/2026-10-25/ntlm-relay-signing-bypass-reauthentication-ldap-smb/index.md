---
schema: 1
kind: research
title: "NTLM relay past required signing: SpecterOps and Blackfield re-authenticate a signed LDAP or SMB session with a relayed victim identity, and Microsoft fixed it in the September and October 2026 updates"
headline: "Required LDAP and SMB signing did not stop NTLM relay: a re-authenticated session kept the attacker's key"
summary: >
  SpecterOps (LDAP, 2026-10-23) and Blackfield (SMB, 2026-10-21) independently show that a domain controller or file server that
  requires signing still accepts a relayed NTLM authentication when the attacker first opens a signed session of its own and then
  re-authenticates it as the victim, so the session keeps a signing key the attacker knows. Microsoft fixed the SMB variant in
  September 2026 and the LDAP variant in the 2026-10-13 cumulative update; SpecterOps reports no reply to its report and
  Blackfield found no CVE for the SMB change; public tooling exists and neither researcher reports use in attacks.
discovered_at: "2026-10-25T03:34:00Z"
updated_at: null
event_date: "2026-10-23"
run_id: 2026-10-25T0256Z-intel
priority: notable
immediate_action: null
tags: [identity, auth-bypass, poc-public, patch-available]
regions: [global]
sectors: []
entities: ["trend:ntlm-relay-signing-bypass-reauthentication-2026-10", "tool:ldap-switcheroo"]
techniques: [T1557, T1557.001, T1187, T1098, T1003.006]
affected_products: ["Microsoft Windows Server"]
cves: []
sources:
  - url: "https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/"
    publisher: "SpecterOps"
    date: "2026-10-23"
    role: primary
  - url: "https://blackfield.ch/blog/defeating-enforced-smb-signing/"
    publisher: "Blackfield"
    date: "2026-10-21"
    role: primary
  - url: "https://support.microsoft.com/en-us/servicing/os/windows-server/2026/10/kb5126646-windows-server-2025-security-update"
    publisher: "Microsoft (KB5126646, Windows Server 2025)"
    date: "2026-10-13"
    role: corroborating
  - url: "https://support.microsoft.com/en-us/servicing/os/windows-server/2026/09/kb5122882-windows-server-2022-security-update"
    publisher: "Microsoft (KB5122882, Windows Server 2022)"
    date: "2026-09-08"
    role: corroborating
closed_sources: []
evidence:
  - quote: "The domain controller we tested against had both LDAP signing and channel binding enforced, and the attack still worked over 389/TCP."
    publisher: "SpecterOps"
    source_url: "https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/"
  - quote: "We independently identified a similar vulnerability in SMB, and Microsoft patched it quietly in September 2026."
    publisher: "SpecterOps"
    source_url: "https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/"
  - quote: "On any host that requires SMB signing, Domain Controllers included, a relayed privileged authentication yields a privileged session that is still signed with the low-privilege key."
    publisher: "Blackfield"
    source_url: "https://blackfield.ch/blog/defeating-enforced-smb-signing/"
  - quote: "I could not find a CVE for this specific change, in Microsoft’s update guide, the KB notes, or public trackers; it reads as silent hardening rather than a tracked fix."
    publisher: "Blackfield"
    source_url: "https://blackfield.ch/blog/defeating-enforced-smb-signing/"
verification: multi-source
sourcing_note: >
  SpecterOps and Blackfield found the re-authentication weakness independently. The patch status rests on their build testing:
  SpecterOps reports no reply to its report to Microsoft, and Blackfield found no CVE or KB note for the SMB change and did not
  trace every build; neither reports use in attacks.
confidence: high
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Confirm that every domain controller has the cumulative update of 2026-10-13 and every Windows server the September 2026 one for its Windows release (SpecterOps names KB5126646, the October update for Windows Server 2025, and KB5122882, the September update for Windows Server 2022; other releases have their own packages), then list the computer accounts whose msDS-AllowedToActOnBehalfOfOtherIdentity or msDS-KeyCredentialLink holds a value nobody set, because patching does not remove what a relay already wrote."
updates: []
migrated_from: null
---
SpecterOps and Blackfield show that NTLM relay to a server that requires signing works again when the attacker first owns a signed session and then re-authenticates it with the victim's identity, so the session keeps the attacker's signing key. For LDAP, the attacker signs a session to a domain controller with valid credentials or, where accepted, an anonymous NTLM context, coerces a victim over SMB, and sends the victim's relayed authentication with a malicious LDAP modification in one SASL record signed with the attacker's key; the controller checks the signature once, switches to the victim's identity and runs the modification with the victim's rights ([SpecterOps, 2026-10-23](https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/)). The tested controller enforced LDAP signing and channel binding and the attack still worked over 389/TCP; the demonstration writes the resource-based constrained delegation attribute, and relaying a domain controller's machine account to another controller leads to DCSync and domain compromise ([SpecterOps, 2026-10-23](https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/)). Blackfield shows the SMB counterpart: a server keeps the original signing key on re-authentication without checking that the identity matches, so on any host that requires SMB signing, domain controllers included, a relayed privileged authentication yields a privileged session still signed with the low-privilege key, provided the attacker can capture or coerce that authentication ([Blackfield, 2026-10-21](https://blackfield.ch/blog/defeating-enforced-smb-signing/)).

SpecterOps reported the LDAP flaw to Microsoft on 2026-10-06, received no response, and says the fix shipped in the 2026-10-13 cumulative update, KB5126646, while the SMB variant was patched quietly in September 2026 (KB5122882) ([SpecterOps, 2026-10-23](https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/)). KB5126646 is the October update for Windows Server 2025 and KB5122882 the September update for Windows Server 2022 ([Microsoft, 2026-10-13](https://support.microsoft.com/en-us/servicing/os/windows-server/2026/10/kb5126646-windows-server-2025-security-update); [Microsoft, 2026-09-08](https://support.microsoft.com/en-us/servicing/os/windows-server/2026/09/kb5122882-windows-server-2022-security-update)), so each release needs its own cumulative update of the month. Blackfield found no CVE or KB note for the SMB change, says similar changes seem to have reached the other supported versions in the following weeks without having traced every build, and warns that one or two end-of-life versions may never receive it ([Blackfield, 2026-10-21](https://blackfield.ch/blog/defeating-enforced-smb-signing/)). Both publish tooling; neither reports use in attacks ([SpecterOps, 2026-10-23](https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/); [Blackfield, 2026-10-21](https://blackfield.ch/blog/defeating-enforced-smb-signing/)).

**Exposure:** Windows Server domain controllers and SMB servers without the September 2026 (SMB) or 2026-10-13 (LDAP) cumulative update of their release; SpecterOps tested Server 2016 domain controllers and above and says every Server 2022 and 2025 domain controller it tested accepted the relay with LDAP signing required ([SpecterOps, 2026-10-23](https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/)). The LDAP variant needs a signed session the attacker controls, a victim coerced to authenticate over SMB and LDAP reachable on 389/TCP ([SpecterOps, 2026-10-23](https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/)).

**Detection:** neither researcher publishes detection guidance. The demonstration ends in an LDAP modification of msDS-AllowedToActOnBehalfOfOtherIdentity on the victim's own computer object, and msDS-KeyCredentialLink (shadow credentials) is the other write ([SpecterOps, 2026-10-23](https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/)), so directory-service change auditing on computer objects for those two attributes is where it surfaces, attributed to the victim's own computer account while the connection comes from the attacker's host. Patching does not remove values a relay already wrote.

**Defender takeaway:** confirm that every domain controller runs the 2026-10-13 cumulative update of its Windows release and every Windows server the September one, because required signing did not stop this relay before them. SpecterOps also advises enforcing LDAP signing and channel binding together, restricting LDAP on 389/TCP where possible and reducing NTLM; Blackfield says SMB signing stays necessary but is not sufficient ([SpecterOps, 2026-10-23](https://specterops.io/blog/2026/10/23/ldap-signing-bypass-ntlm-relay/); [Blackfield, 2026-10-21](https://blackfield.ch/blog/defeating-enforced-smb-signing/)).
