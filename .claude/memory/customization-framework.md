---
name: Customization framework
description: branding.yaml (site) + org-profile.yaml (lens) carry every org/brand value; rules to not regress
type: project
---

# Customization framework — two configs carry every org value

- `config/branding.yaml` → `site/branding_config.py` → `site/build.py`: site identity, theme tokens, feeds, analytics (`provider: "none"` = off + strips CSP hosts). Shipped config == loader DEFAULTS == byte-identical site (`site/test_build.py` asserts it; keep both in sync).
- `config/org-profile.yaml` → `tools/compose_prompts.py --write`: lens, watchlists, classification/triage schemes, `national_certs` (single-source carve-out; absent = default list, `[]` = disabled), `policy_watch`. Compose targets: `cti-run.md`, `verification.md`, the agent definitions.

Rules to not regress:
- Never reintroduce site-identity literals in `site/build.py` (CLAUDE.md hard rule) or lens phrases in prompt prose outside ORG-PROFILE blocks — write "the profiled constituency (§ Organization profile)".
- For byte-diff comparisons of build changes, build both sides with `PYTHONHASHSEED=0` (pre-existing set-iteration tie jitter, ~30 pages).
- Fork guide: `docs/customization.md`; `site/branding/` is downstream-owned.
