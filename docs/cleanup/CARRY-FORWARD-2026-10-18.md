# Carry-forward from the 2026-10-18 audit (reference branch, never auto-merged)

This branch, `cleanup/2026-10-18-carry-forward`, holds the out-of-week repairs the 2026-10-18 quality audit drafted before the operator cut its scope to the trailing week (v4.21). None of it is verified and none of it is on `main`. Its name is outside `claude/**`, so `.github/workflows/auto-merge-claude.yml` never promotes it. It is input for the store cleanup program (`prompts/cleanup-coordinator.md` on `main`), not a branch to merge.

- **Base:** `58416ebf` (main as of 2026-10-18, before the 2026-10-11 audit landed). Diff it with `git diff 58416ebf cleanup/2026-10-18-carry-forward`.
- **The findings themselves** are on `main` and are the authoritative work list: `work/2026-10-18T1307Z-audit/truth-{T1,T2,T4,T5,T6a,T7,T8a,T8b,T9,D1,D2,D3,L}.yaml` (188 out-of-week verdicts: 43 clean, 68 imprecision, 77 factual error), `fetch-worklist.md`, `dup-groups.json`, and the report's § Carry-forward (`docs/audits/2026-10-18-quality-audit.md`).

## Porting rules

1. Every changelog record on this branch carries `run_id: 2026-10-18T1307Z-audit`. That run is published and does not list these entries, so a ported change is re-recorded under the porting fire's own run id with a fresh `at` (never copied verbatim; `check_run.py` resolves record run ids and checks `silent-edit`).
2. Re-verify each ported claim against its source before shipping it, and route it through the porting fire's gate and verifier loop like any other change.
3. Discard a hunk when `main` changed the file since the base, unless the hunk is re-derived on top of `main`.

## What is here

| Class | Files | Status |
|---|---|---|
| Portable: `main` has not touched the file since the base | `2026-05-08/qilin-ransomware-hits-die-linke…`, `2026-05-10/sophos-beagle-backdoor…`, `2026-05-16/gtig-unc6671-blackfile…`, `2026-05-20/microsoft-dcu-disrupts-fox-tempest…`, `2026-05-28/nx-console-tanstack-daemon-tools…`, `2026-10-02/cve-2026-76504-cisco-catalyst-sd-wan…`, `2026-10-02/ftapi-ransomware-the-gentlemen…`, `2026-10-08/ixa-systems-vaud-security-integrator…` | Re-record and port |
| Superseded: duplicate folds the 2026-10-11 audit already did differently on `main` (its survivors differ from these) | the Semantic Kernel, PHP SOAP, Windows Netlogon 41089, Cisco SD-WAN 20182 and 20245, n8n, FortiClient EMS, SimpleHelp 48558 and Cisco ISE 20181/20190 groups (19 files) | Do not port. Re-derive any remaining defect from `main` with the D1–D3 YAMLs |
| Registry | `entities/registry.yaml`: the Eurail incident summary dropped the retracted "Dutch DPA and EDPS are reviewing" claim | Port (re-check the summary against the entry) |
| Tool | `tools/check_run.py` `_page_skeletons`: extract-mode text no longer passes through the HTML tag stripper (keeps literal `<FIRST 4 digits of UUID>`), html mode keeps `meta description`/`og:description` text (Mastodon posts), and "(opens in a new window/tab)" link labels are stripped | Port with a test in `site/test_build.py` or a selftest |

Already on `main` (dropped from this branch): the eight in-week entry fixes, the ATT&CK v20.0 pin, the 2026-09-30T0639Z warning acknowledgment, and the superseded v4.20 prompt drafts.

Delete this branch once the cleanup tracker (`docs/cleanup/STATUS.md` on `main`) marks every row ported or discarded.
