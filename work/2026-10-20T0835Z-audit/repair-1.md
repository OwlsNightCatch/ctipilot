# repair-1 report (cleanup wave W1-A, run 2026-10-20T0835Z-audit)

Seven entries recorded (one record each), one declined. Every ground-truth page was re-fetched with `fetch_source.py extract` (CVE record via `url`); bodies saved under `work/2026-10-20T0835Z-audit/repair-1/src/`. Every new evidence quote was `grep -F`-checked against the saved body, and `check_run.py <cache> --page-checks-since 2026-10-20` reports 0 warn (197 quotes verbatim, 92 CVE mentions on their cited page). `check_run.py --all`: 0 fail; the only warnings on these entries are "run_id does not resolve to a run record" (cleared once the run record exists). The run-scoped gate (`--pre-verify`) shows no entry-level finding on these seven; its 3 FAILs are run-record bookkeeping (run-clock, entries_updated / updated_entry_ids).

## 2026-10-02/zammad-cve-2026-102489-102490-exploited-divd-breach
- Record: `update` (non-internal), at 2026-10-20T08:40:20Z, `updated_at` moved. fields: [actions, body, cves, evidence, headline, sources, summary]
- Applied: "6.5 and older receive no security fixes" superseded by Zammad 6.5.5 (2026-10-15), an emergency fix for CVE-2026-102489 in the unsupported 6.5 series, installed only from a new package repository. Restated in headline, summary, cves[CVE-2026-102489].fixed, actions[0], the Defender takeaway and the 2026-10-10 closing sentence. New section notes that the 6.5.5 notes name only CVE-2026-102489 (silent on the root escalation) and that 6.3/6.4 still need upgrading. 7.2.2 confirmed as still the current release. Ground truth: https://zammad.com/en/product/releases/6-5-5

## 2026-10-10/ghostaction-fake-audit-workflow-git-history-credential-theft
- Record: `update` (non-internal), at 2026-10-20T08:42:29Z, `updated_at` moved. fields: [body, evidence, sourcing_note, summary]
- Applied: "the larger figure stays unconfirmed" / "disagrees with the counts elsewhere" replaced with GitGuardian's 2026-10-13 update: more than 30,000 repositories across 3,000 users and orgs, about 1,900 compromised accounts, 3,174 secrets targeted, GitHub blocking the workflow from 2026-10-09 (the 10 and 12 October waves extracted nothing). Summary and sourcing_note revised. GitGuardian is cited with its page date 2026-10-07 (one sources[] record per URL), and the prose names the 13 October update. Ground truth: https://blog.gitguardian.com/ghostaction-github-actions-supply-chain-attack-returns/

## 2026-05-18/thorchain-gg20-threshold-signature-scheme-vault-drain-11m-ac (legacy)
- Record: `correction` (non-internal), at 2026-10-20T08:46:34Z. fields: [body, evidence, headline, sources, sourcing_note, summary, title]
- Applied (factual-error): six vaults / about $11M stated as fact. Now one of five vaults and about $10.7M (THORChain Report #1; about $10M in Report #2), with The Record's six vaults and TRM's more than USD 11M attributed to them. https://blog.thorchain.org/thorchain-exploit-report-1
- Applied (imprecision): "GG20 flaw suspected / working theory". Now THORChain's confirmation (2026-05-15) and its post-mortem chain: a multi-prime Paillier key, 864 deliberately failed MTA rounds, and two further tss-lib weaknesses fixed upstream in v2.0.0 and v3.0.0. Main analysis rewritten from both reports. https://blog.thorchain.org/thorchain-exploit-report-2
- Legacy duties: classification already present (B/2, kept). techniques [T1657] kept (active; no other technique is source-supported). Added **Exposure:**, **Detection:**, **Triage:** (honest discriminator from Report #2: one recently admitted validator's disproportionate share of signing failures) and a rewritten **Defender takeaway:**. Source records gained `date` fields (publisher strings cleaned). The 2026-09-30 section's "is the working theory" is put into past tense.

## 2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags (legacy)
- Record: `update` (non-internal), at 2026-10-20T08:49:45Z, `updated_at` added. fields: [actions, body, evidence, headline, sources, summary, techniques, title]
- Applied (factual-error): GitHub disabled both repositories on 2026-05-19, not only maintain-one-comment. Main text fixed and stated in the new section; the 2026-09-30 record summary is append-only and cannot be edited. https://socket.dev/blog/mini-shai-hulud-actions
- Applied (missing development): re-enabled 2026-09-16 with the malicious tags intact; about 15,000 dependents of issues-helper; SafeDep's six newly infected repositories (2026-09-20 to 09-24), whose payload now also commits Claude Code and VS Code hooks; disabled again by 2026-09-25. Exposure windows, Detection (run-history and commit-audit signals), a new **Triage:** line (Socket's runtime and duration discriminator) and the takeaway (pin to a SHA before 2026-05-18) are rewritten. One action added. https://thehackernews.com/2026/09/compromised-github-actions-came-back.html
- Legacy duties: classification present (B/2). techniques plus T1204.002 (hooks run when a developer opens the project; active id). Source records gained `date` fields; evidence[] populated (4 verbatim quotes).

## 2026-07-29/cve-2026-63077-teamcity-onprem-unauth-deserialization-rce
- Record: `correction` (non-internal), at 2026-10-20T08:51:34Z. fields: [actions, body, cves, sourcing_note]
- Applied: cves[0].cvss null to "9.8 (CVSS 3.1, JetBrains as CNA)"; sourcing_note says the blog gives no number while the CNA record scores 9.8. The CVE Services API is a blocked citation, so the score has no inline link; provenance is named in prose, following the sp-page-builder precedent. Read via https://cveawg.mitre.org/api/cve/CVE-2026-63077
- Applied: 2026-08-06 section reworded to "as of 2026-08-06 ... had not been revised", noting the 2026-08-07 pointer and marking "nothing beyond exploitation" as the position at that date. https://blog.jetbrains.com/teamcity/2026/07/cve-2026-63077/
- Applied: actions[1] window is now "unpatched at any point after 2026-07-27", matching the takeaway. https://blog.jetbrains.com/teamcity/2026/08/cve-2026-63077-update/
- Applied (low confidence, confirmed): actions[0] and the Triage hardening sentence now say restrict external access to the server, or VPN / extra layer, as JetBrains advises, instead of closing the agent-polling endpoint separately. Same URL.

## 2026-08-04/liechtenstein-vwbp-beneficial-ownership-register-breach
- Record: `correction` (non-internal), at 2026-10-20T08:53:04Z. fields: [body]
- Applied: the 2026-09-01 section's trailing "as Fabian Schmid told the media" claimed the whole mechanism sentence. It is now split into two cited sentences, and the new section states that NZZ attributes only the no-bulk-query / several-hours point to Schmid; the access mechanism is NZZ's own reporting. The 2026-09-01 record summary is append-only. https://www.nzz.ch/wirtschaft/nach-hackerangriff-in-liechtenstein-wie-sicher-sind-heikle-finanzdaten-beim-bund-ld.10018419
- Declined, already fixed by 2026-10-11T1307Z-audit: Swiss/EU-administered wording (headline, takeaway, 2026-08-05 section); "both registers reach the same client population" (now marked analyst judgement); "500,000 beneficial owners" (now legal entities, cited to NZZ 2025; the 2026-09-02 record summary is append-only); "human and internal rather than telemetry-driven" (removed); the blast-radius causal claim (now the government's own quoted reason plus a marked analyst judgement).

## 2026-09-17/kairos-libercourt-commune-ransomware-confirmed
- No record. Declined, already fixed by 2026-10-11T1307Z-audit: the uncited "three small municipal administrations" count was withdrawn, and the takeaway names Valdemoro and Velilla de San Antonio without a quantifier. (Optional improvement not made: Kairos's 2026-05-29 claim on Commune de Camiers per ransomware.live.)

## 2026-09-17/mandiant-ai-risk-resilience-report-2026
- Record: `correction` (non-internal), at 2026-10-20T08:54:19Z. fields: [body, headline, summary]
- Applied (residual of the case 1 finding): headline "recommended a poisoned package that spread the Shai-Hulud worm" becomes "an attacker used a hijacked AI coding-assistant session to steal OAuth tokens and deploy the Shai-Hulud worm"; the summary's case 1 clause gives the chain as Mandiant states it. https://cloud.google.com/security/resources/ai-risk-and-resilience-2026
- Applied (residual of the citation finding): the Hardening/Hunt lines of cases 1, 2, 3, 4, 5, 6 and 7 and the tail of case 8 now carry the Mandiant citation; each was verified against the report's "Defensive controls" paragraphs. Same URL.
- Declined, already fixed by 2026-10-11T1307Z-audit: case 7 as an observed leak; case 1 body "re-poisoned/revived"; "weaponized" title and summary lead; "production ledger database"; "published 2026-09-15".

## State and registry changes for the main agent
- state/cves_seen.json: bump `last_seen` to 2026-10-20 for CVE-2026-102489 (cves[].fixed moved) and CVE-2026-63077 (cves[].cvss moved). No CVE added or removed. CVE-2026-102490 unchanged.
- entities/registry.yaml:
  - `incident:thorchain-gg20-tss-vault-drain-11m-nine-chains-switzerland`: summary is stale ("roughly $11M across nine chains"). Suggested: "THORChain vault drain of about $10.7M from one of its five vaults (THORChain's count; TRM Labs: more than USD 11M across nine chains), by a newly churned validator exploiting its GG20 threshold-signature implementation (Switzerland-based project)." Key unchanged.
  - `incident:actions-cool-issues-helper-github-action-compromised-53-tag`: add relation `{to: "campaign:mini-shai-hulud", type: part-of, source: "2026-05-20/actions-cool-issues-helper-github-action-compromised-53-tags", note: "Socket places the compromise in the May 2026 Mini Shai-Hulud campaign"}`. Optionally extend its summary with the 2026-09-16 re-enable.
  - No new entity keys.

## Residuals noticed, not fixed (outside the findings)
- Legacy em dashes remain in older text of several of these entries (the gate checks only this fire's sections on updated entries; the site strips them).
- VWBP main text and takeaway still quote German untranslated with English glosses ("Datenkopien ...", "Weitere Angriffe ...", "aus Sicherheitsgründen ..."), against the English-quotation style rule.
- THORChain keeps the retired `update_of: null` key; the gate does not flag it.
- Nothing was unreadable: every ground-truth page extracted cleanly. JetBrains' fixed-issues page does not render CVE-2026-63077, so no citable page carries the 9.8.
