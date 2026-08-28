---
name: classification-policy
description: Every entry carries exactly one rating; independence means first-hand observation, not source count
type: project
---

# Classification policy

- Every entry carries exactly one rating. Non-triage kinds: NATO Admiralty `classification: {reliability, credibility}`. Triage kinds carry `org_triage` INSTEAD only while `config/org-profile.yaml` configures a triage scheme — **this deployment configures none, so vulnerability entries carry the Admiralty block too**. Enforcement is version-gated on `prompt_version` (v3.18+ FAIL; pre-3.18 history WARN); `--all` runs the permanent `store-ratings` sweep. The rule text is rendered from the config by `compose_prompts.py` — never hand-edit the rendered blocks.
- **A same-day press write-up of one lab report is NOT a second source.** Independence = first-hand observation, not count — open the second source and ask what it observed itself; if every fact traces back to source one, the entry is `single-source`, credibility 2 (still cite the write-up, just don't count it). Genuine second sources perform their own determination: a KEV listing over a vendor advisory, a CNA's own scoring, a vendor patch announcement over a researcher advisory.
