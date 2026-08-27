---
name: Customization framework
description: Two-config downstream-fork model — branding.yaml (site) + org-profile.yaml (lens); rules any session must follow when touching identity values
type: project
---

# Customization framework (added 2026-07-02, prompts v2.69)

The deployment is a fork-friendly framework. Two configs carry every
organization-specific value; the static code/prompts are org-neutral.

- `config/branding.yaml` → `site/branding_config.py` → `site/build.py`:
  site name/wordmark, taglines, footer copy, theme-override tokens,
  logos/favicon, chart palettes, RSS feed identity + sector slices, trend
  cohorts, analytics (`provider: "none"` = off switch, also strips the
  Umami hosts from the CSP). **Shipped config == loader DEFAULTS ==
  byte-identical site** — `site/test_build.py` asserts this; keep the two
  in sync when either changes.
- `config/org-profile.yaml` → `tools/compose_prompts.py --write`: lens,
  watchlists, triage, plus (new) `national_certs` (single-source carve-out
  list; absent key = default list, `[]` = disabled) and `policy_watch`
  (weekly W2/§9). Compose targets now include `prompts/verification.md`
  (`org-certs` block); weekly gained `org-policy-watch`.
- `site/branding/` is downstream-owned (logos, fonts, custom.css);
  upstream ships only its README.

## Rules to not regress

- NEVER reintroduce "ctipilot.ch" / colors / umami ids as literals in
  `site/build.py` — everything flows from BRANDING; CLAUDE.md hard rule.
- NEVER write "Swiss / EU public-sector"-style lens phrases into prompt
  prose outside ORG-PROFILE managed blocks — reference "the profiled
  constituency (§ Organization profile)" instead (v2.69 sweep did this;
  worked examples keep Swiss flavor deliberately).
- Findings-schema example fields renamed: `ch_eu_nexus` → `region_nexus`,
  `public_sector_nexus` → `primary_sector_nexus` (compact summary labels
  "Region nexus / Primary-sector nexus").
- The site build has pre-existing run-to-run tie-order jitter (~30 pages,
  PYTHONHASHSEED set-iteration ties in related-entities / delta blocks).
  For byte-diff comparisons of build changes, build both sides with
  `PYTHONHASHSEED=0`.
- Fork guide for operators: `docs/customization.md`.

**2026-08-27 (v4.0):** the weekly routine is retired, so `prompts/weekly-summary.md` is no longer a
compose target; the `org-policy-watch` block now renders into `prompts/cti-run.md` (it tasks the S2
home-region & sector worker). Compose targets: `cti-run.md`, `verification.md`, the three agent
definitions. See [[entry-lifecycle-v4]].