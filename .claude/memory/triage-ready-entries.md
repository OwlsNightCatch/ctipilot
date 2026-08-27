---
name: Triage-ready entries (v3.13 actionability shape)
description: Why entries must be matchable by alert-triage agents and humans holding an alert; the fields and body lines that carry it
type: project
---

# Triage-ready entries — the v3.13 actionability shape

**Origin (2026-07-09):** operator directive to make the pipeline's output "world-class threat intelligence" that both humans and AI triage agents can act on — the reference model is the agentic-SOC pattern (Elastic InfoSec's published pipeline: enrichment workflow → initial-triage agent → specialized forensics agents → final-review agent, all matching alerts against a threat-knowledge base). The ctipilot entry store IS such a knowledge base; entries must let a consumer holding a suspicious alert answer *"is this that attack?"*.

## What the shape is (master rules: `prompts/cti-run.md` Phase 4 § Triage-ready behavioral description)

1. **Attack flow as observable behavior** — attacker steps in order, each tied to a telemetry class named vendor-neutrally (process lineage, auth/session events, web/app access logs, DNS/egress, cloud control-plane audit, mail flow, persistence artifacts); platform-native anchors (Windows event IDs, paths) as examples only; never rule code or query syntax.
2. **ATT&CK in metadata, prose only where essential** (v3.17 inverted the old "woven" rule) — `techniques[]` frontmatter is the canonical, complete mapping surface (active ids per the pinned `attack/enterprise-attack.json`); the body describes each behavior in plain language and must read complete without T-numbers; inline ids only where they earn their place (deep-dive kill chains, mapping-as-the-finding); bare ID lists remain a defect. Full conventions: [attack-layer.md](attack-layer.md).
3. **`affected_products[]`** — official "Vendor Product" strings so an alert/asset-inventory name is a field lookup, not full-text search.
4. **`**Triage:**` line** (threat/incident/research kinds; vulnerability entries fold it into the Detection clause) — benign lookalike + discriminator (path, parent, signing, account type, destination class, sequence, volume). **Omit rather than invent** — must derive mechanically from the cited mechanism (PD-1; an invented discriminator is F4).

## Why-lines worth keeping

- The 2026-07-09 audits found: 80 distinct ATT&CK IDs across the store, ALL prose-only (not retrievable); FP-disambiguation present only in the best entries; F4 (148×, mostly ellipsis-spliced evidence quotes) and F3 (167×, facts attributed to the wrong co-cited source) the top truth defects — v3.13 added the contiguous-quote and per-fact-attribution compose rules for exactly these.
- **Migrated v2 entries (`migrated_from != null`) are a lower-fidelity tier** — placeholder evidence, empty entities/actions/techniques. The tail is never bulk-rewritten — let consumers filter on the field (documented in `docs/pipeline.md`); since v4.0 an audit may lift an individual migrated entry through an `improvement` changelog record ([[entry-lifecycle-v4]]), and the provenance flag itself never changes.
- `cves[].vector` semantics trip readers: `vector` = victim-interaction axis (`zero-click` ok on a post-auth bug), `auth` = auth axis. Clarified in `site/taxonomy.yaml` comment 2026-07-09 after an auditor misread Coolify's `zero-click`+`post-auth` as a taxonomy error.
- Everything above is org-agnostic by design — no org-profile value is baked into the triage-ready rules, so the shape survives re-parameterization via `config/org-profile.yaml`.
