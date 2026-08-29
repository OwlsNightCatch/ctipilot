---
name: customization-framework
description: branding.yaml (site) + org-profile.yaml (lens) carry every org/brand value; rules to not regress
metadata: 
  node_type: memory
  type: project
  originSessionId: b6284326-dd92-4265-9208-2bb89b1ad9fe
  modified: 2026-08-29T10:16:41.103Z
---

# Customization framework — two configs carry every org value

- `config/branding.yaml` → `site/branding_config.py` → `site/build.py`: site identity, theme tokens, feeds, analytics (`provider: "none"` = off + strips CSP hosts). Shipped config == loader DEFAULTS == byte-identical site (`site/test_build.py` asserts it; keep both in sync). **Exception (2026-08-29, operator directive): `feeds.sector_slices` + `trends.cohorts` have NO in-code default and are excluded from the mirror — the config list is the complete set (empty = none).**
- `config/org-profile.yaml` → `tools/compose_prompts.py --write`: lens, watchlists, classification/triage schemes, `national_certs`, `policy_watch`, `deployment.site_url` — **all three REQUIRED since 2026-08-29 (no in-code default; `[]`/`""` = disabled, absent key = validation error)**. Compose targets: `cti-run.md`, `verification.md`, the agent definitions.

Rules to not regress:
- Never reintroduce site-identity literals in `site/build.py` (CLAUDE.md hard rule) or lens phrases in prompt prose outside ORG-PROFILE blocks — write "the profiled constituency (§ Organization profile)".
- **The shipped profile is a generic EXAMPLE / POC demo** (2026-08-29): org name "Swiss Government Entities" (SGE), empty watchlists, no triage scheme. Never write a concrete organization's name, estate, or affiliation into config, README, prompts, or memory — this repo is public and memory is committed. A lens change is a config edit + `compose_prompts.py --write`, never a code or prompt edit.
- For byte-diff comparisons of build changes, build both sides with `PYTHONHASHSEED=0` (pre-existing set-iteration tie jitter, ~30 pages).
- Fork guide: `docs/customization.md`; `site/branding/` is downstream-owned.
