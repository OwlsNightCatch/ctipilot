**Model:** Claude Opus 4.8 (`claude-opus-4-8`)
**Timestamps:** started_at=2026-07-14T13:38:43Z · ended_at=2026-07-14T13:42:51Z · duration_seconds=248

## Verification report — 2026-07-14T1210Z-intel (iteration 5, final)

Cold end-to-end re-read of all three new entries + run record. All sources fetched
this iteration. Iteration-4 delta (F17 ShareFile ATT&CK mapping) re-verified.

### Prior-iteration delta verification (iter-4 F17)
- `progress-sharefile-szc-active-exploitation-confirmed`: `techniques: [T1190]` — CONFIRMED.
  T1505.003 (Web Shell) is gone; T1190 (Exploit Public-Facing Application) is fully
  supported by the entry's own delta body (Shadowserver-confirmed in-the-wild exploitation
  of the pre-auth auth-bypass CVE-2026-2699). Non-empty. Remediation holds.
- All iter-1..3 remediations re-verified cold and hold:
  - ESET F4 (exploitation-primitive over-claim): body line 82 now reads "no complex
    exploitation primitive" + ESP write = privileged local operation, consistent with the
    local/post-auth frontmatter. Holds.
  - ESET F4 (ITW over-attribution): summary + body now passive "no in-the-wild exploitation
    has been reported"; IOC-withholding re-cited to ESET's verbatim wording. Holds.
  - Run-record jargon F11: notes body (§ Verification & coverage notes) is clean; residual
    "main-agent"/"S1/S2" strings are only in operator frontmatter telemetry (bridge_uses,
    iterations[]), which iter-1 explicitly left intact. Holds.
  - AsyncAPI single→multi-source F9: SafeDep independently confirmed this iteration — covers
    the identical incident (same package/version set, 06:58 UTC commit), reports
    "miasma-train-p1", and carries the verbatim "private, parallel build … adopted the
    Miasma brand" quote. Genuine independent corroboration. Holds.
  - AsyncAPI ordinal F14: body line 67 now "a recurring 2026 pattern"; no wave count. Holds.

### Truth gate (F1–F4, F13–F15)
- All inline source URLs fetched and resolve to specific articles/advisories: Wiz blog post,
  SafeDep post, ESET WeLiveSecurity research post, CERT/CC VU#616257, BankInfoSecurity article
  (via jina), The Register article. No 404 / homepage / listing redirects.
- Named entities cross-checked against fetched sources:
  - ESET: CVE-2026-8863 + CVE-2026-10797 present; 11 shims; signature-length-mismatch quote
    verbatim; "present on thousands of systems…" verbatim; dbx 2026-06-09; no CVSS stated
    (frontmatter null — correct). Affected-vendor list matches CERT/CC exactly.
  - CERT/CC: BYOVD quote verbatim; vendor list matches; revised 2026-06-17.
  - AsyncAPI: 37 PRs, PR#2155, 06:58 UTC commit, 07:10 publish, five versions across four
    packages, >3M downloads/wk, "M-RED-TEAM v6.4", import-not-install, IPFS, systemd, HTTP/
    Nostr/Ethereum/libp2p C2, credential-theft targets, "minimal resemblance … Miasma and
    Shai-Hulud", "we are not making any definitive attribution", 2026-05-17 fix unmerged 58d
    — all confirmed against Wiz. No IOCs leaked into the entry (Wiz's IPs/hashes/wallets
    correctly excluded).
  - ShareFile: every evidence quote verbatim in BankInfoSecurity; watchTowr ~30,000→~1,000;
    Liska/Recorded Future/Bluesky Clop hypothesis correctly framed as speculation, not
    attribution. Register corroborates cloud-restored + on-prem-off + no-unauthorized-access.
  - CVSS spot-check: BankInfoSecurity misprints CVE-2026-2699 as "9.9"; entry frontmatter
    uses 9.8, which matches the authoritative NVD/CIRCL score (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/
    S:U/C:H/I:H/A:H). Entry correctly used the authority over the roundup outlier — no defect.
- No hallucinated facts, no analytical-link-as-fact, no unsourced quantifier, no name-collision
  (M-RED-TEAM / Miasma-train-p1 aliases correctly registered on the tool record).

### Editorial gate (F5–F12, F16–F18)
- Primary sources are all vendor-research/coordinated-advisory grade (Wiz, ESET, CERT/CC,
  BankInfoSecurity/Register + vendor status). No NVD/MITRE-only primary. No F6.
- Relevance: AsyncAPI (global supply-chain, transferable CI/CD pwn-request lesson, 3M dl/wk),
  ESET UEFI shim (Secure-Boot bypass across widely-deployed Linux distros + kiosk/diagnostic
  tooling, concrete dbx-enrollment audit lever), ShareFile (actively-exploited edge file-
  transfer, US+DE exposure, direct EU on-prem nexus) all clear the SOC gate. No F7.
- Priority calibration sound: no critical (none clears stop-and-act bar); AsyncAPI+ShareFile
  high; ESET notable (patched five weeks ago, no ITW). No F16.
- Classification codes consistent: all three B/1 — reliability B fits vendor/research primaries;
  credibility 1 fits the two-source corroboration each entry actually shows. No F17.
- actions[]: AsyncAPI one concrete do-now task; ESET one concrete inventory/verify task naming
  real artifacts; ShareFile empty (correct — update whose original actions still stand). No F18.
- Coverage shape: borderline drops (Siemens Opcenter, Swiss Army OpenDesk→weekly, Talos Python
  taxonomy, D1R extortion claim, Lidl breach) are well-reasoned; gaps documented (cert-pl,
  cert-eu quiet, jina 402). No nameable in-window relevant omission. Coverage looks complete.

### Verdict
CLEAN

No truth, editorial, or advisory findings. The three entries and the run-record notes are
sound and complete, all sourcing verified against pages fetched this iteration, and every
prior-iteration remediation holds. Clean to publish.

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable)
[]
```
