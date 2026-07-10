---
name: classification-policy
description: "v3.18: every entry carries exactly one rating — the triage-kind exemption exists only while a triage scheme is configured"
metadata:
  node_type: memory
  type: project
---

# Classification policy (v3.18) — no entry ships unrated

- **Every entry carries exactly one rating, never zero.** Non-triage kinds always carry the NATO Admiralty `classification: {reliability, credibility}`. Triage kinds (`vulnerability` by default) carry `org_triage` INSTEAD only while `config/org-profile.yaml` `vulnerability_triage.categories` is non-empty; **this deployment configures no scheme, so vulnerability entries carry the Admiralty block too**. The pre-3.18 exemption made every vulnerability entry ship with NEITHER rating (894/894 `org_triage: null`, vuln entries `classification: null`) — the operator directive 2026-07-10 closed that hole.
- **Enforcement is version-gated on the run record's `prompt_version`:** `check_run.py` FAILs a missing rating (and an empty behavior-kind `techniques[]`) on v3.18+ runs; pre-3.18 records keep WARN (immutable history stays green). Out-of-vocab codes FAIL at any version. `--all` runs a `store-ratings` sweep (org-triage + classification + attack-mapping with enforce=True over every v3.18+ run's entries) — the permanent "everything is classified" guarantee.
- **The rule text is rendered, not written:** `compose_prompts.py` `_render_classification`/`_render_triage`/`_render_verify_context` emit the deployment-resolved rule (split vs. fallback) into the org-data blocks of both master prompts + the research agent, and into the verifier context (F17 scope). Adding a triage scheme to the config and running `--write` restores the org_triage split automatically — never hand-edit the rendered blocks.
- Site side: unrated legacy entries simply show no badge; every v3.18+ entry shows `NATO <code>` (or the org-triage badge) on every card — see [[design-system]] v3.2.
