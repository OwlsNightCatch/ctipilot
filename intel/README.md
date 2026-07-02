# `intel/` — closed-source intelligence drop folder

This directory is the **hand-off point between an operator-owned feed script
and the autonomous brief routines**. A script (yours — commercial CTI portal
exports, ISAC bulletins, FIU/LE reports, internal advisories) downloads
closed-source documents and commits them here; the next daily (or weekly)
routine fire ingests them via a dedicated intake sub-agent (S5 daily / W3
weekly) and folds qualifying items into the brief with **unlinked
closed-source citations**.

**Most days this directory is empty or absent — that is the normal state.**
The routines detect content, spawn the intake agent only when files exist,
and otherwise skip the whole machinery at zero cost.

## Directory layout

```
intel/
  README.md            ← this file (the only permanent inhabitant)
  2026-07-02/          ← one folder per drop date (UTC, YYYY-MM-DD)
    provider-x-flash-2026-07-02.md
    isac-ch-weekly-27.md
```

The folder date is the **drop date**, not necessarily the document's
publication date (that lives in the front-matter). The routines process every
dated folder inside their gap-derived recency window, so a drop that lands
while a routine was down is picked up by the next fire (self-healing, same
mechanism as brief catch-up).

## File contract

Formats: `.md` or `.txt` (preferred — directly readable by the agents) or
`.json`. PDFs must be converted to text by the feed script before the drop —
the agents do not parse binary formats.

Every file SHOULD open with a front-matter block (the intake agent falls back
to filename + folder date when it is missing, but the citation quality drops):

```markdown
---
title: "Targeting of cantonal e-government portals"
provider: "ISAC-CH weekly bulletin"
date: "2026-07-01"
tlp: "AMBER"
ref: "ISACCH-2026-27"
reliability: "HIGH"
---

Document body — the full text of the closed-source report.
```

- `title` — human-readable document title (becomes the citation title).
- `provider` — who produced the intelligence (becomes the citation
  attribution; also the `Evidence:` quote attribution).
- `date` — the document's publication date (recency decisions anchor here).
- `tlp` — `CLEAR | GREEN | AMBER | AMBER+STRICT | RED`. **Mandatory in
  spirit**: an unmarked file is treated as TLP:CLEAR on a public deployment
  and WARNed. See the TLP gate below.
- `ref` — a stable document id; carried into the brief's citation so a
  reader can request the document through your internal channels.
- `reliability` — optional; defaults to HIGH (see credibility below).

## How the routines treat this content

- **High credibility.** Closed-source documents are treated as
  HIGH-reliability primary sources — the same tier as a national CERT
  advisory. A single closed-source document is sufficient sourcing for an
  item (no two-source requirement), but the item's heading then carries a
  reader-visible `[CLOSED-SOURCE]` marker. Public corroboration is still
  *attempted* (it strengthens the item and can lift a TLP constraint by
  re-anchoring the story in public sources).
- **Unlinked citations.** The brief cites these documents without URLs:
  `Closed-source: "Title" (Provider, YYYY-MM-DD, TLP:CLEAR, ref: ID)` in the
  metadata footer, and `(Provider, YYYY-MM-DD — closed source)` inline at
  the point of claim. Never a fabricated link.
- **TLP gate (hard).** On a `deployment.visibility: public` profile
  (`config/org-profile.yaml`), any citation above TLP:CLEAR **fails the
  commit gate** — the brief publishes to the open internet. Drop
  above-CLEAR material only into private deployments, or expect the intake
  agent to use it strictly as a *lead* it re-anchors in public sources
  without citing or quoting the document.
- **Verifiable.** The intake agent extracts verbatim `Evidence:` quotes from
  the document, and the verification sub-agent `Read`s the referenced file
  to confirm every claim — closed-source items get the same
  anti-hallucination treatment as public ones.

## How to feed it

The routine containers clone the repo fresh from `main` on every fire, so a
drop must be **committed and pushed** to be visible. Two supported paths:

1. **Ride the existing auto-merge chain (recommended).** The feed script
   commits to a branch named `claude/intel-drop-<YYYY-MM-DD>` and pushes;
   `.github/workflows/auto-merge-claude.yml` promotes it to `main`
   automatically and deletes the branch. No extra credentials or workflow
   changes needed beyond push access.
2. **Direct operator push to `main`** where branch protection permits your
   operator credential (the no-direct-push rule binds the Claude routines,
   not your feed script — but path 1 is safer and audit-identical).

Example feed-script tail:

```sh
DATE=$(date -u +%F)
mkdir -p "intel/${DATE}"
cp /path/to/converted-reports/*.md "intel/${DATE}/"
git checkout -b "claude/intel-drop-${DATE}"
git add "intel/${DATE}"
git commit -m "intel: drop ${DATE} ($(ls intel/${DATE} | wc -l) file(s))"
git push origin "claude/intel-drop-${DATE}"
```

**Privacy note.** Files in this directory are part of the repository. A
public repository ⇒ every drop is world-readable regardless of TLP marking —
put only TLP:CLEAR material here. For anything above CLEAR, run the private
deployment (private repo + local site hosting): see
[`docs/private-deployment.md`](../docs/private-deployment.md).
