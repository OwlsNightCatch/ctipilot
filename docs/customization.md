# Customization & downstream forks

This repository is a **framework**: an autonomous CTI pipeline whose
intelligence lens, visual identity, analytics, and publishing surface are all
parameterized. The upstream deployment (ctipilot.ch, Swiss federal SOC lens)
is just the default parameter set. A downstream fork customizes **only the
files listed below** and keeps merging upstream — new features, prompt
improvements, build/site upgrades — without touching its customizations.

## The two-config model

| Config | Owns | Consumed by |
|---|---|---|
| [`config/org-profile.yaml`](../config/org-profile.yaml) | The **intelligence lens**: org name, sector, home region, constituency, audience register, product/supplier watchlists, org-triage scheme, the NATO Admiralty classification scheme + triage-kind split, national-CERT carve-out list, policy/regulatory watch, deployment site URL | `tools/compose_prompts.py` → rendered into the `ORG-PROFILE` managed blocks of the intel-run master prompt (`prompts/cti-run.md` — mission, org data, and the `org-policy-watch` block that tasks the S2 worker), `prompts/verification.md`, and all three agent definitions. `site/build.py` additionally reads the `classification:` block at build time so the rating badges, tooltips and the entry-detail assessment panel always describe the same scheme the agents were instructed to assess (NATO doctrine fallback when the profile is absent) |
| [`config/branding.yaml`](../config/branding.yaml) | The **published site**: name, wordmark, taglines, footer copy, logos, favicon, theme colors, fonts, chart palettes, RSS feed identity, sector feed slices, trend cohorts, analytics | `site/build.py` (via `site/branding_config.py`) at build time |

Plus one asset directory:

| Directory | Owns |
|---|---|
| [`site/branding/`](../site/branding/README.md) | Logo/favicon files, self-hosted fonts, free-form `custom.css` — upstream ships only a README here, so it never conflicts |

**The contract:** every value has an upstream default equal to the current
ctipilot.ch deployment. An absent key (or empty string / empty list, where
documented) means "inherit upstream". The default configs build a
**byte-identical** site and compose byte-identical prompts — customization is
strictly opt-in, per value.

## Downstream-owned vs upstream-owned files

A fork edits ONLY these (the "downstream-owned" set):

- `config/org-profile.yaml` — your org, sector, region, watchlists, triage,
  trusted CERTs, policy watch.
- `config/branding.yaml` — your name, colors, fonts, logos, feeds, analytics.
- `site/branding/*` — your logo/favicon/font files and `custom.css`.
- `CNAME` — your custom domain (or delete it for `<org>.github.io/<repo>`).
- `README.md` — rendered at `/about/`; rewrite it for your deployment.
- `.claude/memory/` — accumulates your deployment's operational memory.

Everything else — `prompts/`, `.claude/agents/`, `site/build.py`,
`site/assets/`, `tools/`, `docs/`, `.github/workflows/` — is
**upstream-owned**: never hand-edit it in a fork (the `ORG-PROFILE` managed
blocks inside prompts/agents are regenerated from your config by
`python3 tools/compose_prompts.py --write`; the compose-profile workflow
does this on push). That separation is what makes upstream merges clean.

### Merging upstream

```bash
git remote add upstream https://github.com/OwlsNightCatch/ctipilot.git
git fetch upstream
git merge upstream/main
python3 tools/compose_prompts.py --write   # re-render managed blocks with YOUR profile
python3 site/build.py && python3 site/test_build.py
```

Conflicts can only arise in the downstream-owned set, and there only when
upstream changes the same file — which for `config/*.yaml` means a schema
addition (rare, and always additive with a documented default: take both
sides, keep your values). The content store (`entries/`, `entities/`,
`runs/`) plus `state/*` and `sources/*` evolve independently per deployment
and are not part of the customization surface — a fork's intelligence is
its own.

## Recipes

### Corporate rebrand (colors, fonts, logos)

1. `config/branding.yaml` → `site:` — set `name`, `wordmark_strong` /
   `wordmark_accent`, `tagline`, `lede`, `meta_description`,
   `footer_tagline`, `footer_lede`, `copyright_note`, `url`, `github_repo`.
2. `theme:` — set any subset of the ~25 documented tokens (dark + light
   palettes, radii, font stacks). Empty = inherit the upstream design. The
   build emits `assets/css/branding.css` after `styles.css`, so your values
   win without editing any upstream CSS.
3. Drop `logo.svg` / `favicon.svg` into `site/branding/` and reference them
   under `logo:`. The default favicon is generated from `favicon_text` /
   `favicon_bg` / `favicon_fg` if you only want a color/initials swap.
4. Corporate webfont: put the `.woff2` files in `site/branding/fonts/`,
   declare `@font-face` in `site/branding/custom.css`, name the family in
   `theme.fonts.sans` — the CSP already allows same-origin fonts and blocks
   third-party font CDNs by design.
5. `charts:` — chart palettes and accent fills for the Ops/Trends SVGs.
6. Verify: `python3 site/build.py && python3 site/test_build.py`, then open
   `site/_site/index.html`.

### Turn analytics off (or point at your own instance)

```yaml
analytics:
  provider: "none"
```

removes the Umami snippet from every page **and** every third-party origin
from the Content-Security-Policy (the build's self-check then asserts zero
analytics tags). To keep Umami but use your own instance, set `website_id`,
`script_host`, and `beacon_host` under `analytics.umami:` — script host and
beacon host are different origins on Umami Cloud; read the maintainer note
in [docs/analytics.md](analytics.md) before changing the beacon host.

### Change the intelligence lens (org / sector / region)

Everything lives in `config/org-profile.yaml`:

- `organization:` — name, short name, sector + additional sectors (values
  from `site/taxonomy.yaml`), home region, region focus, constituency
  description, audience register.
- `watchlist:` — your estate products, suppliers, standing interests.
- `vulnerability_triage:` — your patch-priority scheme; every vulnerability
  entry then carries a structured `org_triage: {category, rationale}`
  frontmatter block in your scheme.
- `national_certs:` — which national CERTs / government authorities your
  deployment trusts as single sources for their own disclosures. Omit the
  key for the upstream default list; `[]` disables the carve-out entirely.
- `policy_watch:` — the regulators and directives whose changes alter your
  obligations (drives the intel run's S2 home-region & sector sweep; a
  regulatory action with a transferable obligation publishes as a `policy`
  entry).

Then `python3 tools/compose_prompts.py --write` (CI does it too). The
static prompt prose is org-neutral by design — it always defers to these
managed blocks, so a lens change is a config change, never a prompt edit.

Site-side lens knobs live in `config/branding.yaml`: `feeds.sector_slices`
(which per-sector RSS feeds exist) and `trends.cohorts` (which /trends/
tiles are tracked). `site/taxonomy.yaml` is the controlled vocabulary both
draw from; extend it if your sector/region isn't represented.

### Custom domain / hosting

- Public GitHub Pages: put your domain in `CNAME`, set `site.url` in
  `config/branding.yaml` and `deployment.site_url` in
  `config/org-profile.yaml` (the first drives canonical URLs/feeds, the
  second the routine's publish-verification poll).
- Org-internal hosting: see [docs/private-deployment.md](private-deployment.md)
  and set `site_url: ""` (skips the public site poll). There is no TLP /
  visibility flag — the pipeline processes everything it can read regardless;
  privacy is a function of where you host and whether the repo is private.
- Note `.github/workflows/*` restrict runs to the upstream org
  (`if: github.repository_owner == ...` guards) — adjust that guard once in
  your fork, or run the equivalent commands from your own CI.

## What deliberately stays fixed

Hard invariants are not customization surface (see CLAUDE.md § Self-evolution):
the AI-content transparency via run records, the no-IOC rule, two-source
verification (the carve-out *list* is yours to set; the mechanism is not),
English output, the feature-branch publishing chain, the mechanical gate
(`tools/check_run.py` exit 0), the verification sub-agent loop, the entry
lifecycle (one living entry per finding — every change a dated `updates[]`
changelog record, never a silent edit, never a second entry), the entity
registry as the single entity namespace, volume discipline, and memory
commits. Weakening them in
a fork is possible — it's your repo — but nothing in the config schema
encourages it, and upstream merges will not respect the weakening.

## Known remaining upstream-flavored strings (by design)

- `README.md` and `docs/*.md` describe the upstream deployment and are
  rendered under `/about/` — a fork rewrites README.md (downstream-owned)
  and may hide or replace the docs pages via `custom.css` or its own docs.
- Worked examples inside prompts/agents (e.g. the ISAC-CH closed-source
  drop fixture) keep their Swiss flavor: they document formats, not lens.
- `tools/fetch_source.py` bridge recipes target hosts that 403 generic
  clients (CISA, NCSC.ch, NCSC-NL, SEC EDGAR) — they are source tooling,
  useful to any deployment, not branding. Its SEC EDGAR User-Agent picks up
  your `site.name` automatically.
- `site/assets/js/theme.js` stores the theme choice under the localStorage
  key `cti.briefs.theme` — invisible to readers; left stable so existing
  visitors keep their preference across a rebrand.
