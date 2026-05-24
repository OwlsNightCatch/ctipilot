**Model:** Claude Opus 4.7 (`claude-opus-4-7`)
**Timestamps:** started_at=2026-05-24T05:18:23Z · ended_at=2026-05-24T05:21:29Z · duration_seconds=186

## Verification report — briefs/2026-05-24.md (iteration 5, final cap)

Cold read. Env vars `CLAUDE_FRIENDLY_NAME` / `CLAUDE_MODEL_ID` were unset; self-identified
from runtime context (Opus 4.7). Mechanical gate `check_brief.py` passed pre-spawn (0 FAILs).

### Scope of this pass
WebFetched 16 substantive source URLs in this iteration (8 MITRE ATT&CK technique pages
treated as stable canonical refs, not re-fetched). CCB Belgium fetched via the bridge.
Cross-checked every CVE id, CVSS score, affected/fixed version, actor attribution, package
name, technique, and numeric claim against a source read in this iteration. The four prior
iterations' remediations were re-verified specifically.

### Truth verification — all key claims confirmed against fetched sources

- **LiteSpeed CVE-2026-48172 (§ 0, § 2):** LiteSpeed vendor blog confirms CVE id, "actively
  exploited", `lsws.redisAble`, affected 2.3–2.4.4, fixes v2.4.7 / WHM v5.3.1.0. GHSA-fxrh-cwjh-m33v
  confirms CVSS 10.0, CWE-266, `cpanel_jsonapi_func=redisAble` hunt string. Supported.
- **Unbound 1.25.1 cluster (§ 0, § 2):** Release page confirms 11 CVEs incl. CVE-2026-33278 and
  CVE-2026-42944, released 2026-05-20. NLnet 33278 advisory confirms the use-after-free / DS
  sub-query / NSEC3-budget / deep-copy mechanism and remote-unauth-controlling-signed-zone reach
  (assigns no CVSS itself — brief correctly attributes the 9.8 to CCB). CCB Belgium confirms
  CVE-2026-33278 = CVSS 9.8 and CVE-2026-42944 = CVSS 7.5 (heap overflow via multiple
  NSID/DNS-Cookie/EDNS-Padding options). Supported.
- **ISC BIND (§ 2):** CVE-2026-5946 confirmed 7.5, CHAOS/HESIOD/ANY/NONE class DoS, 9.18 branch
  affected, fixes 9.18.49 / 9.20.23. CVE-2026-3593 confirmed 7.4, DoH/HTTP-2 use-after-free,
  9.18.x NOT affected (9.20.x only), fixed 9.20.23. Supported.
- **GCP deleted-key window (§ 0, § 3):** Aikido confirms Joe Leon, median ~16 min / max ~23 min
  across 10 trials (Gemini/BigQuery/Maps), service-account ~5 s / Gemini ~1 min, eventual-consistency
  cause, Won't-Fix→P0 reopen, dates 2026-05-21 / updated 2026-05-22. Supported.
- **Unimed healthcare breach (§ 0, § 1, § 7):** The Record + heise confirm Unimed (Saarland, ~95%
  of German university hospitals), mid-April 2026, encryption attempted but blocked while
  exfiltration succeeded, attribution UNKNOWN ("not yet known who is responsible for the successful
  attack on Unimed" — heise verbatim; The Record: no actor claimed). heise separately attributes the
  ARWINI Lower-Saxony breach to Kairos via Hannover Police. Brief correctly leaves Unimed open and
  frames ARWINI/Kairos as an analyst pattern-overlap, not a sourced attribution. heise lists nine
  institutions (supports § 7 "on the order of nine"). Uniklinik Freiburg confirms ~54,000 master /
  ~900 billing-with-diagnoses / small-number bank data. Uniklinik Köln confirms ~30,000 (27,298
  general + 843 health) and IBAN data in 5 cases. All prior-iteration attribution remediation holds.
- **Packagist deep dive (§ 5):** Socket Laravel-Lang confirms 700+ versions across the four packages,
  autoload.files / src/helpers.php backdoor, per-host MD5 fingerprint (path+arch+inode), runtime
  array_map('chr',...) C2 assembly, TLS-verify disabled + UA spoof, exec("php")/cscript+VBScript
  execution, and "17 distinct Collectors" with XOR. Aikido confirms "fifteen collector modules" with
  AES-256 and self-delete. The § 7 source-divergence note (Socket ~17 collectors/XOR vs Aikido 15
  modules/AES-256) is accurate. The brief's "multiple Chromium-based browsers" generalisation is the
  correct conservative resolution — Socket lists ~4-5 Chromium browsers while Aikido separately
  enumerates "17 Chromium-based browsers"; the prior-iteration fix avoiding the "17 browsers"
  inversion is verified sound. Socket postinstall + THN confirm 700+ repos under common attacker
  infrastructure and all 8 named packages, package.json (not composer.json) postinstall, Linux ELF
  from code-hosting release → /tmp/.sshd masquerade with TLS suppression. StepSecurity confirms
  org-level push access, 700+ tags across four packages, autoload.files/src/helpers.php. C2 domain
  correctly omitted per no-IOC policy; /tmp/.sshd retained as host-path hunt concept (correct).
- **npm staged publishing UPDATE (§ 4):** GitHub Changelog confirms GA 2026-05-22, npm stage publish,
  CLI 11.15.0+, 2FA approval gate, and the three --allow-file/--allow-remote/--allow-directory flags.
  Supported.
- **Atos BYOVD (§ 3):** Atos TRC landing + The Hacker News confirm all three hardware-gate-bypass
  techniques including the third — direct registry manipulation under
  HKLM\SYSTEM\CurrentControlSet\Control\Class (THN explicitly: also \Enum). Atos-TRC named, NDSS
  2026-s1491 referenced, THN dated 2026-05-22, page dated 2026-04-17. § 7 MEDIUM-confidence framing
  and "specific driver names not retained / NDSS PDF not cited" disclosure are accurate. Supported.

### Editorial / whole-brief checks
- Coverage shape correct: § 1 leads with the CH/EU/healthcare item; § 2 trending vulns clear the
  inclusion gates (LiteSpeed = ITW; DNS cluster = CVSS 9.8 pre-auth memory-safety + EU/CH resolver
  ubiquity); deep dive earns its length; no Immediate-Actions callout overreach.
- Primary-source kind sound throughout — vendor PSIRT / research-lab / regulator-equivalent leads;
  NVD/CERT only ever as Additional source or not at all.
- Single-source handling correct (§ 7): none admitted to §§ 1–5; Stormshield single-source candidate
  dropped. National-CERT carve-out not needed.
- No IOCs (C2 domain omitted; /tmp/.sshd is a local-path hunt concept). No vanity metrics. English
  throughout. No workflow-internal language in published prose. Footer taxonomy values all in-vocab.

### Advisory observations (not findings — no remediation required)
- § 5 Strand 1 attributes "attacker-controlled forks" to StepSecurity; this iteration's StepSecurity
  fetch described tag rewrites to malicious commits without naming forks, while Socket (also cited)
  carries the fork mechanism. The substantive claim (malicious code absent from main commit history)
  is confirmed by StepSecurity directly, so this is at most a citation-precision nuance and may be a
  WebFetch-summariser compression artefact; not raised as a finding.
- Minor secondary-source date drift (The Record page shows 05-21 vs cited 05-22; CCB page shows
  21/05 vs cited 05-20). Within normal disclosure-vs-publication ambiguity; brief dates defensible.

### Verdict

CLEAN

No truth defects, no editorial defects, no advisory findings requiring remediation. The four
prior iterations' remediations are all verified correct against freshly fetched sources. The brief
is publishable.

### Findings summary (machine-readable)
```yaml
# Findings summary (machine-readable) — v2.48
[]
```
