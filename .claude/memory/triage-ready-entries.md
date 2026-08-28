---
name: Triage-ready entries
description: The actionability shape (behavioral description for humans + triage agents) and its non-obvious footnotes
type: project
---

# Triage-ready entries — the actionability shape

Master rules: `prompts/cti-run.md` Phase 4 § Triage-ready behavioral description (attack flow as observable behavior in vendor-neutral telemetry classes; ATT&CK complete in `techniques[]`, prose readable without T-numbers; `affected_products[]` as official "Vendor Product" strings; `**Triage:**` benign-lookalike discriminator omitted-never-invented). Reference model: the agentic-SOC pattern — the entry store IS a triage knowledge base for alert-matching agents.

Non-obvious footnotes:
- Migrated v2 entries (`migrated_from != null`) are a lower-fidelity tier — never bulk-rewritten; an audit may lift one via an `improvement` record; the provenance flag never changes.
- `cves[].vector` = victim-interaction axis (`zero-click` is valid on a post-auth bug); `auth` = auth axis. Clarified in `site/taxonomy.yaml` after an auditor misread the pair as a taxonomy error.
- The shape is org-agnostic by design — no org-profile value is baked into the triage rules.
