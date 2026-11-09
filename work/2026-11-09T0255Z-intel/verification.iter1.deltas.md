# Prior-iteration deltas (iteration 1 -> iteration 2)

1. [F3] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: Triage line broadens GTIG's "calls to disable logging by non-IaC principals" to any change to model invocation logging.
   - remediation_applied: fixed: the Triage line and the Detection clause now say a call that disables model invocation logging
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

2. [F14] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: "Other actors harvested LLM API keys from public GitHub repositories" is one actor in GTIG.
   - remediation_applied: fixed: "One actor ... another ..."
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

3. [F3] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: (low confidence) GTIG does not say LiteLLM gateways reachable from the internet are in scope.
   - remediation_applied: fixed: the Exposure line keeps internet-reachable model endpoints only; the body states what GTIG says about the LiteLLM gateway
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

4. [F3] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: (low confidence) The claim that revoking a key leaves the persistence in place is the entry's inference under a GTIG citation.
   - remediation_applied: fixed: the sentence cites GTIG for the persistence and the review step is the entry's own advice ("so review those after revoking a stolen key")
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

5. [F4] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: (low confidence) "Abuse stays invisible" is overstated and conflicts with the Detection line; GTIG gives default-off only for Google Cloud Data Access logs.
   - remediation_applied: fixed: the takeaway now says inference calls go unseen where model-call logging is not on by default
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

6. [F3] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: (low confidence) sourcing_note understates Datadog's evidence base (two scripts, 12 customer organizations).
   - remediation_applied: fixed: sourcing_note names the frontend code of one platform, two validation scripts and probing at 12 customer organizations
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

7. [F11] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: sourcing_note carries a composition-rationale sentence about a flaw the body never describes.
   - remediation_applied: fixed: the sentence was removed and the body describes the LiteLLM exploitation without the CVE id; the run record carries a Contradiction line on the id
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

8. [F8] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: The body drops behaviors GTIG describes for LiteLLM, Ollama and service-account rotation while affected_products carries them.
   - remediation_applied: fixed: added the LiteLLM /key/regenerate exploitation, the Ollama probing and the rotated service accounts; GPU provisioning not added (the analysis is at its 550-word bound)
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

9. [F3] 2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole
   - finding: (low confidence) The hosting and telecom spread was attached to the whole 11-03 to 11-08 series, but ISC's breakdown covers 2026-11-05 only.
   - remediation_applied: fixed: scoped to the scanners ISC lists for 2026-11-05
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

10. [F3] 2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole
   - finding: (low confidence) "so the counts show attempts, not success" is the entry's inference under the ISC citation, and the 11-03 and 11-04 counts were left unexplained.
   - remediation_applied: fixed: ISC's 255-character limit and its expectation of successful honeypot logins are stated as ISC's; the series starts at 2026-11-05
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

11. [F3] 2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole
   - finding: (low confidence, pre-existing) The Previdian source is dated 2026-11-07, the page's publication date is 2026-11-05.
   - remediation_applied: fixed: the sources[] date and both inline labels now follow the page's publication date; "as read on" stays in the prose
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

12. [F11] 2026-11-06/cve-2026-123158-openssh-musl-no-pam-password-bypass-sshole
   - finding: The saved Previdian page (read today) shows 20 attempts, 13 addresses and 9 countries, the entry still shows 15, 10 and 8.
   - remediation_applied: fixed: the section and the summary carry the refreshed counter
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

13. [F11] 2026-11-09/llmjacking-stolen-cloud-keys-enable-model-services-resale
   - finding: The Datadog evidence quote ("Attackers use similar tactics...") is meaningless without the sentence before it.
   - remediation_applied: fixed: replaced by the quote on the Bedrock access check
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim

14. [F11] run record
   - finding: (low confidence) The discovery-path note and sources_used misstate how the item was found.
   - remediation_applied: fixed: the note describes the trade-press lead then the pivot to the GTIG post; the source bookkeeping is explained in the notes
   - verify_in_this_iteration: re-read the cited clause/field against the page and confirm the fix is supported and introduced no new unsupported claim
