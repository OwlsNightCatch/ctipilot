# Iteration 2 findings and the remediation applied (for the iteration 3 pass)

Verify each fix in the entry before the cold pass. Declined items carry their rationale; judge them on the cited facts.

1. [F3] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws
   finding: The cited record EUVD-2026-102489 carries only CVE-2026-111345 (Trudesk, aliases CVE-2026-111345 / GHSA-xm42-mhff-286m). The other six collisions are true but sit on records the entry does not cite: CVE-2026-111343 EUVD-2026-10248
   remediation_applied: fixed: the colliding-id sentence removed from the body (the sourcing note keeps the provenance) and the uncited EUVD record dropped from sources[]

2. [F3] wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens
   finding: The 63,000 figure is StepSecurity's ('As of 07:40 UTC on November 12, GitHub search returns more than 63,000 of the attacker's probe pull requests') and sits only on the StepSecurity page; the two citations that close the clause a
   remediation_applied: fixed: StepSecurity cited at the 63,000 clause

3. [F4] confluence-dc-cve-2026-90436-apache-axis-remote-api-rce
   finding: (low confidence) Neither the Atlassian advisory (fetched: 'Advisory Release Date Tue, Nov 9 2026 22:00 PST', no cadence wording) nor BSI WID-SEC-2026-4427 nor the Apache post characterises the advisory as out-of-cycle; no source c
   remediation_applied: fixed: 'out-of-cycle' removed from the summary

4. [F5] cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo
   finding: (low confidence) True (https://support.apple.com/en-us/149717 iOS 18.7.12 lists AirPlay, Bluetooth, CoreUtils x2, MediaRemote, rapportd; https://support.apple.com/en-us/149723 watchOS 26.6.1 lists AirPlay, Bluetooth, CoreUtils x2,
   remediation_applied: fixed: Apple pages 149717 and 149723 added to sources[] and cited

5. [F8] check-point-php2shell-sk1000302-portal-and-vpn-gateways
   finding: (low confidence) Check Point Research states TSGA and TSProxy are modified variants of PhiliKit (ESET: China-nexus UNC5221, Ivanti campaigns), shares code, configuration and cryptographic material with it, uses LightNode VPS and w
   remediation_applied: fixed: the PhiliKit lineage, ESET's UNC5221 association and Check Point Research's attribution caveat added to the update section

6. [F10] coverage
   finding: (low confidence) An exploited (KEV-listed), unauthenticated XXE in Cisco BroadWorks (a web search summary names advisory cisco-sa-bworks-xxe-uwUd7CEt and fix RI.2026.07; not fetched) is in no entry and not in state/cves_seen.json;
   remediation_applied: declined: the 2026-11-10 KEV addition sits outside this run's window and earlier fires borderline-dropped it; left for the audit's KEV sweep

7. [F16] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws
   finding: (low confidence, judgement call) The facts the entry itself cites: vendor impact 'unpredictable behaviour or denial of service', CERT-EU 'Citrix reports no exploitation, and no public proof-of-concept has been confirmed', NCSC-CH 
   remediation_applied: declined with the facts surfaced: priority high kept; the body now states the new monthly Patch-Tuesday-aligned release program (heise, added to sources[])

8. [F11] cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo
   finding: HomeView Software 27.2 (2026-11-12) is in summary, body, sources[] and affected_products but not in cves[CVE-2026-111497].affected or .fixed; no Apple product key (apple-ios, apple-macos, apple-watchos, apple-visionos, apple-homev
   remediation_applied: fixed: HomeView Software 27.2 added to cves[] affected and fixed, and the Apple product keys linked in entities[]

9. [F11] huntress-teams-booking-device-code-phishing-encrypted-kit
   finding: Huntress's ATT&CK table also maps T1557 (callback proxy relaying the victim's authentication and the Cmsi:Cmsi handoff) and T1684.001 (Social Engineering: Impersonation, executive impersonation and Teams/Microsoft branding; id is 
   remediation_applied: fixed: T1557 and T1684.001 added to techniques[]

10. [F11] signdrop-windows-clfs-authentication-lpe-public-poc-no-patch
   finding: Cyderes: 'The real hid.dll (Human Interface Device library) lives in C:\Windows\System32' and the detection row says 'The file does not ship there with Windows'. As written the sentence (and 'because the file does not ship with Wi
   remediation_applied: fixed: 'does not ship in that directory'

11. [F11] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws
   finding: heise is named as a restating source but is not in sources[] and not cited inline; add it (https://www.heise.de/news/Angreifer-koennen-Citrix-NetScaler-ADC-und-NetScaler-Gateway-lahmlegen-11522940.html, 2026-11-12, read this itera
   remediation_applied: fixed: heise added to sources[] and cited

12. [F11] darklunnen-group-ib-fortios-super-admin-swiss-scan-list
   finding: cves[] is empty and no KEV source is cited. CVE-2024-55591 is in KEV (cisa-kev bridge: dateAdded 2025-01-14), so the tag is true, but the entry should cite the KEV record or drop the tag.
   remediation_applied: fixed: the cisa-kev tag removed (the entry carries no CVE record)

13. [F11] confluence-dc-cve-2026-90436-apache-axis-remote-api-rce
   finding: Inference (Atlassian says off by default since 3.0 and that disabling may break scripts, automations and add-ons) presented as exposure fact without the 'inference' label the Detection line carries.
   remediation_applied: fixed: the unlabelled 'likeliest' clause removed from the Exposure line

14. [F11] cve-2026-111497-microsoft-net-oob-update-brotli-sockets-fix
   finding: MSRC's affectedProduct data (api.msrc.microsoft.com/sug/v2.0/en-US/affectedProduct filter cveNumber eq CVE-2026-111497) lists two fixed KBs for Server 2025 (KB5131077 build 26100.33730 and KB5131080 33822) and for Windows 11 24H2/
   remediation_applied: fixed: the earlier Server 2025 and Windows 11 KBs, PowerShell 7.4 to 7.6 and Visual Studio 2017 to 2026 added; '(ESU)' removed; Microsoft PowerShell added to affected_products

15. [F11] cve-2026-119618-apache-httpd-mod-http2-assign-headers-rce
   finding: USN-9090-1 gives the 20.04 fix as 2.4.41-4ubuntu3.23+esm11 (ESM, Ubuntu Pro), which a non-Pro 20.04 host will not receive; the researcher repository the entry cites lists mod_h2 2.0.43 as the fixed standalone release (the Apache p
   remediation_applied: fixed: the Ubuntu 20.04 fix labelled ESM and mod_h2 2.0.43 added from the researcher repository


Also changed since iteration 2 and not a finding: Apache httpd main analysis trimmed to 548 words (Ubuntu ESM wording), the Brotli/Desigo record `fields` now declare `entities`, Microsoft PowerShell registered as a product entity.
