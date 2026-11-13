# Iteration 3 findings and the remediation applied (for the iteration 4 pass)

1. [F3] signdrop-windows-clfs-authentication-lpe-public-poc-no-patch
   finding: Entry: 'file-creation telemetry for hid.dll in the ink directory, which Cyderes ranks highest because the file does not ship in that directory'. Cyderes: 'Two of these carry the most signal today. A hid.dll creation in the ink dir
   remediation_applied: fixed: Cyderes counts the hid.dll creation, with the Defender signature-update RPC call, among its two highest-signal observables

2. [F3] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws
   finding: (low confidence) Entry: 'Where a logout had occurred, /var/log/httperror.log can hold authentication material (one of the rows), so limit who can read that file and support bundles' cited to CTX697305. The CVE-2026-111348 row only
   remediation_applied: fixed: 'and support bundles' dropped from the Detection line

3. [F4] wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens
   finding: (low confidence) StepSecurity: 'A missing run means the stealer probably ran.' and 'The gap is the most reliable sign that the stealer ran.' The Triage line states the payload ran, dropping the hedge. Fix: 'probably ran' / 'is the
   remediation_applied: fixed: 'the payload probably ran' restores StepSecurity's hedge

4. [F11] darklunnen-group-ib-fortios-super-admin-swiss-scan-list
   finding: Workflow-internal wording ('previous sweep of this publisher') and a store self-reference ('described in earlier entries') in a reader-facing field; sourcing_note should be provenance only.
   remediation_applied: fixed: the workflow-internal and store self-reference wording removed from the sourcing note

5. [F11] cve-2026-111497-brotli-desigo-cc-mitel-openscape-cisco-duo
   finding: The Exposure line lists no Apple device although the headline and Defender takeaway tell readers to install the 2026-11-09 Apple releases (iOS, iPadOS, macOS, watchOS, visionOS, HomeView). Add the Apple releases before the fixed v
   remediation_applied: fixed: the Exposure line now names iPhone, iPad, Mac, Apple Watch and Vision Pro below the 2026-11-09 releases

6. [F11] citrix-netscaler-adc-gateway-ctx697305-28-memory-flaws
   finding: The body sentence that named the seven rows was removed in iteration 2, so no row text identifies them any more; a reader cannot tell which seven bulletin rows were left out of the CVE records. Reword the note or name the rows by 
   remediation_applied: fixed: the sourcing note no longer refers to row text

7. [F11] confluence-dc-cve-2026-90436-apache-axis-remote-api-rce
   finding: (low confidence) Atlassian: 'this setting was turned off by default for new installations starting in Confluence 3.0'. The body keeps 'for new installations'; the summary drops it. Add 'for new installations'.
   remediation_applied: fixed: the summary says off by default for new installations

8. [F11] wfx-phantom-github-actions-ci-secret-stealer-stolen-tokens
   finding: (low confidence) StepSecurity: 'tries to stay in your AWS and Azure accounts after you rotate' and 'designed to outlast credential rotation'; Endor: 'tries to create back doors'. The headline states survival as fact. Hedge ('built
   remediation_applied: fixed: the headline says cloud persistence meant to survive rotation

9. [F11] check-point-php2shell-sk1000302-portal-and-vpn-gateways
   finding: (low confidence) The KEV feed carries dateAdded 2026-10-26 for CVE-2026-109618 and CVE-2026-109619; the source record is dated 2026-10-28 and the record is not cited inline in the body. Date it 2026-10-26 or drop it.
   remediation_applied: fixed: the CISA KEV source record dated 2026-10-26, the feed's dateAdded
