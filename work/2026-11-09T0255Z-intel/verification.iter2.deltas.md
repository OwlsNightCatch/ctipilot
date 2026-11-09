# Prior-iteration deltas (iteration 2 -> iteration 3)

Iteration 1 deltas were verified clean in iteration 2 (all 14 remediations confirmed).

1. [F3] 2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole
   - finding: (low confidence) The record summary says attempts peaked on 2026-11-06 and were lower by 2026-11-08, but ISC states no trend and the 11-08 count is a partial day.
   - remediation_applied: fixed: the summary now says 713 long-password attempts on 2026-11-06 were the highest of ISC's daily counts, with no trend claim; the section marks the 11-08 count as the day the page was published
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported

2. [F3] 2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole
   - finding: (low confidence) ISC's "quite a few of these login attempts" follows the 2026-11-05 scanner table, but the section widened it to the whole series.
   - remediation_applied: fixed: scoped to the first scanners ISC lists
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported

3. [F3] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: (low confidence) "which are the events to watch" sits under the Wiz citation, which gives no detection guidance.
   - remediation_applied: fixed: the cited clause ends after "billing account"; the watch advice is the entry's own clause after the citation
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported

4. [F14] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: (low confidence) "an account that never used model services" is not what GTIG says; GTIG says the services were not enabled at the time of compromise.
   - remediation_applied: fixed: "accounts with model services not enabled are in scope too, because the actors enabled them"
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported

5. [F5] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: (low confidence) Three consecutive factual sentences in the second paragraph carry no inline link.
   - remediation_applied: fixed: a GTIG citation now follows each sentence
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported

6. [F11] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: Advisory: GTIG also describes secrets taken from cloud secret managers (T1555.006) and codebase cloning for secrets (T1213.003), unmapped.
   - remediation_applied: fixed: both ids added to techniques[] and the second paragraph now names the enumeration of repositories and the secret-manager reads
   - verify_in_this_iteration: re-read the clause against the page; confirm the fix is supported and nothing new is unsupported
