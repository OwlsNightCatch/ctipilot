# Truth pass — batch B4 (retrospective audit)

Run: 2026-08-09T1315Z-audit · Window: 2026-08-02T13:09:58Z → 2026-08-09T13:15:57Z · Batch B4 of 4 (20 entries)

## Summary

18 of 20 entries clean. 2 flagged **imprecision** (no factual-error verdicts) — both are CVSS-authority
discrepancies where the entry's number is a real published score, just not the one from the primary
per-CVE authority, and in one case the entry's own sourcing_note misdescribes what the authoritative
record contains.

## Findings

### 1. `entries/2026-08-08/cve-2026-8037-kemp-loadmaster-kev-confirmed-exploitation.md` — imprecision

The entry's `cves[]` record scores CVE-2026-8037 at CVSS 9.8 with no version disclosed. Fetching the
CVE record directly (`https://cveawg.mitre.org/api/cve/CVE-2026-8037`) shows the **vendor's own CNA
record** (Progress Software) publishes CVSS 3.1 **9.6** with vector
`AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H` — Attack Vector **ADJACENT_NETWORK**. NVD separately republishes
its own "Primary" analyst score of CVSS 3.1 **9.8** with `AV:N` (NETWORK) — confirmed via the NVD 2.0
API — which is where the entry's 9.8 comes from. The entry's own body language ("any appliance that
sat internet-reachable and unpatched... warrants a compromise assessment") reads as if this is a
straightforwardly network-exposed flaw, which is NVD's reading, but the vendor's own scoring treats it
as requiring adjacent-network position. Not a hallucination — both numbers are real, authoritative
publications — but the entry silently picked the non-vendor score without disclosing the vendor's
differing (and lower-severity-by-vector) assessment, which the audit mandate's per-CVE-authority check
(vendor PSIRT over a "roundup") would prefer. Recorded as imprecision, not factual-error.

### 2. `entries/2026-08-08/flowise-three-cves-vendor-sunset-no-fix-coming.md` — imprecision

The entry's `sourcing_note` states: "an earlier summary in this run carried CVE-2026-67622 as CVSS
9.9, which the CNA record contradicts at 8.5, and the authority governs." Fetching VulnCheck's own CVE
record (`https://cveawg.mitre.org/api/cve/CVE-2026-67622`) shows this is not a contradiction: the CNA
record carries **two parallel metrics** — CVSS 4.0 8.5 (HIGH) *and* CVSS 3.1 9.9 (CRITICAL,
`AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:L`) — published by the same assigner. The entry's frontmatter
`cvss: "8.5"` and body text "CVSS 4.0 8.5" are themselves accurate and correctly version-labelled, but
the sourcing_note's framing ("the CNA record contradicts... 8.5... the authority governs") is
inaccurate: the authority publishes both, and the entry silently drops a CRITICAL-tier rating from the
narrative while describing its removal as a correction of an "earlier summary" error. Recorded as
imprecision — a self-correction narrative that misdescribes the source it cites.

## Entries verified clean (18)

All evidence[] quotes checked verbatim against a fetched copy of their cited source; all cves[]
CVSS/CWE values cross-checked against cveawg.mitre.org per-CVE records where the entry carries
structured CVE data; ATT&CK technique ids checked against the pinned `attack/enterprise-attack.json`
(all active, none revoked/deprecated). No hallucinated facts, no broken/generic URLs, no closed_sources
records in this batch (all `closed_sources: []`), no IOCs found.

- `entries/2026-08-07/meta-ai-eval-containment-breach-shared-evaluator-irregular.md` — all Reuters/
  Anthropic quotes verified (Anthropic post fetched directly; Reuters itself is CAPTCHA-blocked on
  every transport tried — WebFetch, jina, and the bridge all failed — so the Reuters-attributed quotes
  were cross-checked against BleepingComputer's relay and an independent web search snippet quoting the
  same Irregular statement with matching wording, including the "a sophisticated cyber action" article
  placement the entry uses).
- `entries/2026-08-07/unc6671-blackfile-multi-brand-passkey-vishing-aitm.md` — all 6 evidence quotes,
  the wallet/BTC figures, and the domain-cadence figures verified verbatim against the GTIG/Mandiant
  post.
- `entries/2026-08-08/zapscape-cve-2026-64561-kvm-shadow-mmu-second-vm-escape.md` — CCB advisory quotes
  and CVSS vectors for both CVE-2026-64561 and CVE-2026-53359 verified verbatim; both CVSS 8.8 scores
  confirmed against cveawg.
- `entries/2026-08-08/ncsc-ch-clickfix-wp2shell-etherhiding-vidar-swiss-websites.md` — German-language
  quotes and the "über 100'000" worldwide figure verified verbatim against the NCSC-CH page.
- `entries/2026-08-08/chaindrop-oidc-runner-memory-theft-valid-slsa-provenance.md` — all Unit 42 quotes,
  the opensearch-js/release-drafter.yml gate, and the Russian-locale exit gate verified against the
  source.
- `entries/2026-08-08/dprk-contagious-interview-blast-radius-flemish-government.md` — the "1,640
  companies across 57 countries" figure, the Flemish government spokesperson quote, the Stykas "up to
  30 companies" quote, and the "700 to 800... really damaging" figure all verified verbatim against
  WIRED directly.
- `entries/2026-08-08/cisco-ios-xe-august-2026-hardening-release-cwe-grouped-cves.md` — all 7 CVEs'
  CVSS scores, CWE classes, and the "input validation... path traversal" and "frontier AI models"
  quotes verified against both cveawg per-CVE records and the rendered advisory table.
- `entries/2026-08-08/cve-2026-65400-macos-screen-sharing-auth-state-bypass.md` — Apple's own CVE
  record (assignerShortName "apple") matches the entry's description and affected-version list
  verbatim; entry correctly attributes the CVSS 7.1 to NCSC-NL since Apple publishes none.
- `entries/2026-08-08/beacon-crm-access-key-breach-uk-charities-hospices.md` — all Beacon CRM quotes
  (backup download, "assume all data", encryption/decryption statement) verified verbatim.
- `entries/2026-08-08/cloudflare-workerd-glue-memory-corruption-sandbox-escape.md` — all Check Point
  Research quotes and the description of all five bugs verified against the source directly.
- `entries/2026-08-08/coding-agent-reverse-tunnel-launchagent-persistence.md` — all Elastic Security
  Labs quotes and the Cursor/permission-bypass side-cases verified against the source directly.
- `entries/2026-08-08/screenconnect-app-store-fake-update-distribution-campaign.md` — LevelBlue quotes,
  installation chain, guest-permission deployment, and AI-assisted-code assessment verified against the
  source directly.
- `entries/2026-08-08/wiz-cloud-threat-highlights-h1-2026-ai-toolchain-exposure.md` — all Wiz Research
  quotes (MCP endpoints, LiteLLM events, supply-chain percentage growth, JINX-0163) verified verbatim.
- `entries/2026-08-08/cpdlc-atn-b1-five-protocol-flaws-no-mitigation-available.md` — all 5 CVEs' CVSS
  scores, CWE classes, and descriptions verified against their individual cveawg per-CVE records
  (icscert assigner); CISA's "unlikely to be exploited outside of a lab setting" and safety-margin
  quotes match the CSAF record fields fetched.
- `entries/2026-08-09/cert-polska-private-apn-pivot-into-ot-chp-plant-shutdown.md` — all three lead
  evidence quotes, the 50,000-resident figure, the incident date, and the Marcin Dudek/DEF CON
  attribution verified against the CERT Polska post directly.
- `entries/2026-08-09/metabase-unauth-sqli-zeroday-exploited-framework-tally.md` — all Metabase blog
  quotes, the six minimum-safe-release version numbers, and the "installations below version 58 are
  not affected" statement verified verbatim against the vendor post.
- `entries/2026-08-09/teamdavid-tobit-22-cves-unauth-mailbox-takeover-dach.md` — all four lead evidence
  quotes and the full disclosure timeline (2025-11-05 through 2026-08-07) verified verbatim against
  InfoGuard Labs; spot-checked 4 of 22 CVE records against cveawg (CVE-2026-54211/54203/54210/54212),
  all consistent, including the entry's own already-disclosed PR:N/description discrepancy on
  CVE-2026-54211.
- `entries/2026-08-09/n-able-n-central-hotfix-2-required-supersedes-hotfix-1.md` — the N-able status
  page quote and the Hacker News Cloudflare Tunnel persistence quote both verified verbatim; CVE-2026-18577
  CVSS 8.2 confirmed against cveawg.

## Notes on method

- Reuters (`www.reuters.com`) is unreachable from this environment on every transport tried this pass
  (WebFetch tool error, jina CAPTCHA block, and the `tools/fetch_source.py url` bridge, which itself
  fell back to jina and hit the same CAPTCHA). Where an entry's only primary-attributed quote came from
  Reuters, it was corroborated via the cited corroborating source (BleepingComputer) and, for one
  disputed phrase, an independent web search snippet reproducing the same quote.
- CISA and NCSC.ch/ncsc.admin.ch URLs were fetched via the `tools/fetch_source.py` bridge per policy,
  never via direct WebFetch.
- CVSS/CWE ground truth for every CVE checked was pulled from `https://cveawg.mitre.org/api/cve/<id>`
  (the CVE Services API — the authoritative CNA record), not from NVD or a roundup post, except where
  used deliberately to characterize a *discrepancy* between NVD and the vendor CNA (Kemp LoadMaster).
- ATT&CK technique ids across all 20 entries were checked in bulk against the pinned
  `attack/enterprise-attack.json` (`attack_version: 19.1`) — all active, none revoked or deprecated.
