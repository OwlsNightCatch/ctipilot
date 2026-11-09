# Prior-iteration deltas (iteration 3 -> iteration 4)

Iterations 1 and 2 remediations were confirmed; iteration 3 confirmed all six iteration-2 remediations.

1. [F3] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: (low confidence) The summary credits the enabling of model services to the stolen tokens; GTIG names the tokens as initial access and credits the enabling to abuse of access keys.
   - remediation_applied: fixed: the summary says the tokens gave initial access and the actors then enabled the services
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported

2. [F3] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: (low confidence) "12 customers" and "failed ListFoundationModels calls" drop Datadog's "12 organizations" and "in the majority of instances".
   - remediation_applied: fixed: "12 organizations in 30 days, mostly as failed ListFoundationModels calls across several regions"
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported

3. [F4] 2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole
   - finding: (low confidence) "no source publishes an indicator beyond that" is no longer literally true, since ISC lists scanner addresses and an all-A password pattern.
   - remediation_applied: fixed: "no source publishes a further log indicator" (scanner addresses are not carried); the main analysis stays at 549 words
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported

4. [F4] 2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole
   - finding: (low confidence) The sourcing note credits OX Security with the mechanism, the `*` condition and the Alpine fixed-package table, which Alpine's own advisory carries.
   - remediation_applied: fixed: OX Security is named as the source of the CVSS score only; Alpine's advisory is named for the mechanism, the condition and the fixed-package table (read in this iteration)
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported

5. [F11] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: Advisory: T1548.005 (token-creation privileges used to mint temporary credentials for high-privilege service accounts) is unmapped.
   - remediation_applied: fixed: T1548.005 added to techniques[]
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported

6. [F11] 2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole
   - finding: Advisory: the clause "writing of the first scanners, its author expects" is garbled.
   - remediation_applied: fixed: "after listing the first scanners, its author expects"
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported
