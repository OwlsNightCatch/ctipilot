# Evidence-quote verification — 2026-08-05T0412Z-intel

Every candidate quote literal-substring-checked (whitespace-normalised) against the
body saved under `work/<run-id>/src-*.txt`, per the Phase 4 evidence rule.

| Source | Quote | Result |
|---|---|---|
| admin.ch (BIT) | "Im Rahmen der Analyse … rund 200 Konten kompromittiert wurden." | HIT |
| admin.ch (BIT) | "Es gibt bislang keine Anzeichen dafür, dass Daten abgeflossen sind." | HIT |
| admin.ch (BIT) | "Am Dienstag, 28. Juli, haben Sicherheitsspezialistinnen … bemerkt." | HIT |
| admin.ch (BIT) | "Der Cyberangriff wurde durch bisher unbekannte Akteure ausgeführt …" | HIT |
| Check Point sk185222 | "An unauthenticated attacker may be able to bypass Management authentication …" | HIT |
| Check Point sk185222 | "This issue was discovered internally, and Check Point has no indication of active exploits." | HIT |
| Check Point sk185222 | "Conditions: Successful exploitation requires network access …" | HIT |
| Apache Tomcat security-11 | "An error in the fix for CVE-2026-29146 allowed the EncryptInterceptor to be bypassed." | HIT (line-wrapped in source; whitespace-normalised) |
| CISA KEV alert | "based on evidence of active exploitation" | HIT (fragment — a link splits the full sentence in the rendered body) |
| CISA KEV alert | "Apache Tomcat Missing Encryption of Sensitive Data Vulnerability" | HIT |
| CISA KEV alert | "IBM Langflow Code Injection Vulnerability" | HIT |
| Unit 42 NOVA | "every model contributed a large set of findings that no other model found" | HIT (S3 returned it capitalised mid-sentence; corrected) |
| Unit 42 NOVA | "The vast majority of the analysis we did using frontier AI models — 92% — …" | HIT |

## Corrections forced by the check

1. **Unit 42 NOVA, headline figure — REJECTED as returned.** S3 returned:
   "In just two months, NOVA analyzed 3,915 open-source software (OSS) projects and
   uncovered 14,090 confirmed vulnerabilities, 99.4% of which were previously unreported."
   The page's sentence does not end there — it continues "… and 40% of them designated as
   high or critical severity." The returned form is a truncation closed with a full stop that
   the source does not carry. Replaced with the fragment that does hit:
   "99.4% of which were previously unreported".
2. **Check Point affected-version list.** S1's summary listed R80.20 among the EoS trains;
   the vendor's `versions` metadata field omits it, but the advisory's own Affected Products
   prose reads "R80, R80.10, R80.20, R80.30, R80.40, R81, R81.10 (all EoS)". The prose is the
   authority and R80.20 is in scope. Fix list covers only R81.20 / R82 / R82.10, so every EoS
   train is affected with no fix — S2 correctly refused to assert this without a primary, and
   the primary (read via the sk data route) confirms it.
3. **Apache Tomcat quote** is line-wrapped in the served HTML; it is a genuine contiguous
   sentence and is quoted whole after whitespace normalisation.

---

## Full re-verification after verification iteration 3

The ledger above covered only the 13 quotes checked during composition. Iteration 3 correctly
observed that the run ships more than that and that three unlisted quotes were not literal
substrings. Every cited primary was therefore fetched and saved under `work/<run-id>/src-*`, and
**all 40 `evidence[]` quotes across the 15 entries were re-tested** by exact substring match after
whitespace normalisation and Unicode punctuation folding.

Result: **40/40 verified.** Defects the sweep found and fixed:

| Entry | Defect | Fix |
|---|---|---|
| hungary-state-treasury | Risky Bulletin sentence truncated before "into an extremely sensitive government system", closed with a period the source lacks | full sentence carried |
| service-worker-aitm | Securelist sentence truncated before "– a limitation that malicious actors take advantage of" | full sentence carried |
| talos-ai-prompt-logs | "Most" recapitalised from mid-sentence; typographic quotes replaced with straight singles | source casing and quote marks restored |
| n-able-n-central | both Sophos quotes recapitalised from mid-sentence | de-capitalised to the source's own text |
| liechtenstein-vwbp | field-list quote spanned two separate block elements, joined by a space the markup does not contain | split into two contiguous `evidence[]` records |

One quote is verbatim modulo formatting and is recorded as such rather than altered: the NCSC-CH
advisory's "Current exploitation status: Actively Exploited" appears in the Security Hub API payload
as markdown (`**Current exploitation status**: Actively Exploited`). The cited URL is the rendered
advisory page, where the emphasis markers are formatting rather than text — the same status HTML tags
have in every other check here.

Method note for future runs: strip tags to the empty string, never to a space. Doing the reverse hides
exactly the block-boundary splice found in the Liechtenstein entry, and doing it correctly is what
surfaced it.
