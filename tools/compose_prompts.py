#!/usr/bin/env python3
"""Render config/org-profile.yaml into the ORG-PROFILE managed blocks.

The organization profile (org description, sector/region lens, product +
supplier watchlists, vulnerability-triage scheme) is parameterized in
`config/org-profile.yaml`. This script composes those values into managed
marker blocks inside the master prompts and the sub-agent definitions, so
every agent in the workflow sees the same organization context:

    prompts/daily-cti-brief.md            blocks: daily-mission, org-data
    prompts/weekly-summary.md             blocks: weekly-mission, org-data
    .claude/agents/cti-research.md        blocks: research-mission, org-data
    .claude/agents/cti-verification.md    blocks: verify-context
    .claude/agents/cti-verification-alt.md blocks: verify-context

Managed block shape (content between the markers is REPLACED on --write):

    <!-- ORG-PROFILE:BEGIN <name> -->
    ...generated content...
    <!-- ORG-PROFILE:END <name> -->

Modes:
    --check     exit 0 when every target's blocks match the config,
                exit 3 on drift (CI signal), exit 2 on invalid config.
    --write     regenerate every block in place.
    --dump      print the parsed profile as JSON (consumed by
                tools/check_brief.py's profile-aware checks).
    --selftest  run the embedded parser/renderer round-trip tests.

Stdlib-only by design (same constraint as site/build.py and the other
tools/ scripts — the routine container guarantees nothing beyond stdlib).
The YAML parser below intentionally supports only the strict subset the
profile uses (documented at the top of config/org-profile.yaml): 2-space
indents, nested mappings, lists of scalars or mappings, block scalars
(`key: |`), quoted/plain scalars, `[]` empty lists, full-line comments.
Anything outside the subset is a hard parse error — fail loud, not subtle.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "org-profile.yaml"
TAXONOMY_PATH = ROOT / "site" / "taxonomy.yaml"

BEGIN_RE = re.compile(r"^<!--\s*ORG-PROFILE:BEGIN\s+(?P<name>[a-z-]+)\s*-->\s*$")
END_RE = re.compile(r"^<!--\s*ORG-PROFILE:END\s+(?P<name>[a-z-]+)\s*-->\s*$")

# Target files and the block names each MUST contain.
TARGETS: list[tuple[str, list[str]]] = [
    ("prompts/daily-cti-brief.md", ["daily-mission", "org-data"]),
    ("prompts/weekly-summary.md", ["weekly-mission", "org-data"]),
    (".claude/agents/cti-research.md",
     ["research-mission", "research-audience", "org-data"]),
    (".claude/agents/cti-verification.md", ["verify-context"]),
    (".claude/agents/cti-verification-alt.md", ["verify-context"]),
]

ALLOWED_EXPOSURE = {"internet-facing", "internal", "endpoint", "cloud-saas", "ot"}
ALLOWED_CRITICALITY = {"high", "medium", "low"}
CATEGORY_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]{0,15}$")


class ProfileError(Exception):
    """Config invalid — parse error or schema violation."""


# ---------------------------------------------------------------------------
# Strict-subset YAML parser
# ---------------------------------------------------------------------------

def _strip_scalar(raw: str) -> str:
    s = raw.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ("'", '"'):
        return s[1:-1]
    return s


def parse_yaml_subset(text: str, *, source: str = "<string>") -> dict[str, Any]:
    """Parse the documented YAML subset into dicts/lists/strings.

    Raises ProfileError with a line number on anything outside the subset.
    """
    # Pre-scan: materialize (lineno, indent, content) for parseable lines,
    # but keep raw lines addressable for block scalars (which must preserve
    # blank lines and `#` characters verbatim).
    raw_lines = text.splitlines()

    if any("\t" in ln for ln in raw_lines):
        bad = next(i for i, ln in enumerate(raw_lines, 1) if "\t" in ln)
        raise ProfileError(f"{source}:{bad}: tabs are not allowed (use 2-space indents)")

    def is_skippable(ln: str) -> bool:
        s = ln.strip()
        return not s or s.startswith("#")

    def indent_of(ln: str) -> int:
        return len(ln) - len(ln.lstrip(" "))

    def read_block_scalar(start_idx: int, key_indent: int) -> tuple[str, int]:
        """Collect the block-scalar body following a `key: |` line at
        raw_lines[start_idx]. Returns (text, next_idx)."""
        body: list[str] = []
        i = start_idx + 1
        content_indent: int | None = None
        while i < len(raw_lines):
            ln = raw_lines[i]
            if not ln.strip():
                body.append("")
                i += 1
                continue
            ind = indent_of(ln)
            if ind <= key_indent:
                break
            if content_indent is None:
                content_indent = ind
            if ind < content_indent:
                raise ProfileError(
                    f"{source}:{i + 1}: block-scalar line dedents below its first line")
            body.append(ln[content_indent:])
            i += 1
        # Trim trailing blank lines (YAML clip semantics, close enough).
        while body and not body[-1]:
            body.pop()
        return "\n".join(body), i

    def parse_mapping(idx: int, indent: int) -> tuple[dict[str, Any], int]:
        out: dict[str, Any] = {}
        i = idx
        while i < len(raw_lines):
            ln = raw_lines[i]
            if is_skippable(ln):
                i += 1
                continue
            ind = indent_of(ln)
            if ind < indent:
                break
            if ind > indent:
                raise ProfileError(
                    f"{source}:{i + 1}: unexpected indent (expected {indent} spaces)")
            m = re.match(r"^(?P<key>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*(?P<val>.*)$",
                         ln.strip())
            if not m:
                raise ProfileError(
                    f"{source}:{i + 1}: expected `key: value` mapping entry, got {ln.strip()!r}")
            key, val = m.group("key"), m.group("val").strip()
            if key in out:
                raise ProfileError(f"{source}:{i + 1}: duplicate key {key!r}")
            if val == "|":
                out[key], i = read_block_scalar(i, ind)
            elif val == "[]":
                out[key] = []
                i += 1
            elif val == "":
                # Nested block: mapping or list, decided by the next
                # non-skippable, deeper-indented line.
                j = i + 1
                while j < len(raw_lines) and is_skippable(raw_lines[j]):
                    j += 1
                if j >= len(raw_lines) or indent_of(raw_lines[j]) <= ind:
                    raise ProfileError(
                        f"{source}:{i + 1}: key {key!r} has no value "
                        "(use `[]`, `\"\"`, or an indented block)")
                child_indent = indent_of(raw_lines[j])
                if raw_lines[j].lstrip().startswith("- "):
                    out[key], i = parse_list(j, child_indent)
                else:
                    out[key], i = parse_mapping(j, child_indent)
            else:
                out[key] = _strip_scalar(val)
                i += 1
        return out, i

    def parse_list(idx: int, indent: int) -> tuple[list[Any], int]:
        out: list[Any] = []
        i = idx
        while i < len(raw_lines):
            ln = raw_lines[i]
            if is_skippable(ln):
                i += 1
                continue
            ind = indent_of(ln)
            if ind < indent:
                break
            stripped = ln.strip()
            if ind == indent and stripped.startswith("- "):
                item_body = stripped[2:].strip()
                m = re.match(r"^(?P<key>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*(?P<val>.*)$",
                             item_body)
                if m:
                    # Mapping item. The first key rides on the `- ` line and
                    # sits (visually) at indent+2; any further keys of the
                    # same item follow at exactly indent+2.
                    key, val = m.group("key"), m.group("val").strip()
                    key_indent = indent + 2
                    item: dict[str, Any] = {}
                    if val == "|":
                        item[key], i = read_block_scalar(i, key_indent)
                    elif val == "[]":
                        item[key] = []
                        i += 1
                    elif val == "":
                        raise ProfileError(
                            f"{source}:{i + 1}: nested block as the first key of a "
                            "list item is not supported — put a scalar first")
                    else:
                        item[key] = _strip_scalar(val)
                        i += 1
                    j = i
                    while j < len(raw_lines) and is_skippable(raw_lines[j]):
                        j += 1
                    if (j < len(raw_lines)
                            and indent_of(raw_lines[j]) == key_indent
                            and not raw_lines[j].lstrip().startswith("- ")):
                        rest, i = parse_mapping(j, key_indent)
                        dup = set(rest) & set(item)
                        if dup:
                            raise ProfileError(
                                f"{source}:{j + 1}: duplicate key(s) in list item: "
                                f"{sorted(dup)}")
                        item.update(rest)
                    out.append(item)
                else:
                    out.append(_strip_scalar(item_body))
                    i += 1
            elif ind == indent:
                raise ProfileError(
                    f"{source}:{i + 1}: expected `- ` list item, got {stripped!r}")
            else:
                raise ProfileError(
                    f"{source}:{i + 1}: unexpected indent inside list")
        return out, i

    result, next_idx = parse_mapping(0, 0)
    # Anything left non-skippable means the top-level walk stopped early.
    for k in range(next_idx, len(raw_lines)):
        if not is_skippable(raw_lines[k]):
            raise ProfileError(f"{source}:{k + 1}: unparsed trailing content")
    return result


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def _parse_taxonomy(path: Path) -> dict[str, set[str]]:
    """Same flat `key -> {values}` reader as site/build.py parse_taxonomy."""
    out: dict[str, set[str]] = {}
    if not path.exists():
        return out
    cur: str | None = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^([a-z_][a-z0-9_]*)\s*:\s*$", line)
        if m:
            cur = m.group(1)
            out[cur] = set()
            continue
        m = re.match(r"^\s+-\s+(.+?)\s*$", line)
        if m and cur is not None:
            out[cur].add(m.group(1).strip().strip('"').strip("'"))
    return out


def _req_str(d: dict[str, Any], key: str, ctx: str, *, allow_empty: bool = False) -> str:
    v = d.get(key)
    if not isinstance(v, str) or (not allow_empty and not v.strip()):
        raise ProfileError(f"{ctx}: {key!r} must be a non-empty string")
    return v.strip() if not allow_empty else (v.strip() if isinstance(v, str) else "")


def validate_profile(profile: dict[str, Any],
                     taxonomy: dict[str, set[str]] | None = None) -> dict[str, Any]:
    """Schema-validate the parsed profile; return a normalized copy."""
    if taxonomy is None:
        taxonomy = _parse_taxonomy(TAXONOMY_PATH)
    sectors = taxonomy.get("sectors", set())
    regions = taxonomy.get("regions", set())

    if str(profile.get("profile_version", "")) != "1":
        raise ProfileError("profile_version must be 1")

    org = profile.get("organization")
    if not isinstance(org, dict):
        raise ProfileError("organization: must be a mapping")
    norm_org = {
        "name": _req_str(org, "name", "organization"),
        "short_name": _req_str(org, "short_name", "organization"),
        "sector": _req_str(org, "sector", "organization"),
        "additional_sectors": org.get("additional_sectors", []),
        "region_focus": _req_str(org, "region_focus", "organization"),
        "home_region": _req_str(org, "home_region", "organization"),
        "description": _req_str(org, "description", "organization"),
        "audience": _req_str(org, "audience", "organization"),
    }
    if not re.match(r"^[A-Za-z0-9][A-Za-z0-9 ._-]{0,23}$", norm_org["short_name"]):
        raise ProfileError("organization.short_name: max 24 chars, alphanumeric/space/._-")
    if sectors and norm_org["sector"] not in sectors:
        raise ProfileError(
            f"organization.sector {norm_org['sector']!r} is not a site/taxonomy.yaml sectors value")
    if not isinstance(norm_org["additional_sectors"], list) or any(
            not isinstance(s, str) for s in norm_org["additional_sectors"]):
        raise ProfileError("organization.additional_sectors: must be a list of strings")
    for s in norm_org["additional_sectors"]:
        if sectors and s not in sectors:
            raise ProfileError(
                f"organization.additional_sectors value {s!r} is not a taxonomy sectors value")
    if regions and norm_org["home_region"] not in regions:
        raise ProfileError(
            f"organization.home_region {norm_org['home_region']!r} is not a taxonomy regions value")

    wl = profile.get("watchlist")
    if not isinstance(wl, dict):
        raise ProfileError("watchlist: must be a mapping (use `[]` for empty lists)")
    products = wl.get("products", [])
    suppliers = wl.get("suppliers", [])
    interests = wl.get("interests", [])
    if not isinstance(products, list) or not isinstance(suppliers, list) \
            or not isinstance(interests, list):
        raise ProfileError("watchlist.products/suppliers/interests: must be lists")
    norm_products = []
    for i, p in enumerate(products):
        ctx = f"watchlist.products[{i}]"
        if not isinstance(p, dict):
            raise ProfileError(f"{ctx}: must be a mapping with name/vendor/exposure/criticality")
        exposure = _req_str(p, "exposure", ctx)
        criticality = _req_str(p, "criticality", ctx)
        if exposure not in ALLOWED_EXPOSURE:
            raise ProfileError(f"{ctx}.exposure {exposure!r} not in {sorted(ALLOWED_EXPOSURE)}")
        if criticality not in ALLOWED_CRITICALITY:
            raise ProfileError(f"{ctx}.criticality {criticality!r} not in {sorted(ALLOWED_CRITICALITY)}")
        norm_products.append({
            "name": _req_str(p, "name", ctx),
            "vendor": _req_str(p, "vendor", ctx),
            "exposure": exposure,
            "criticality": criticality,
            "notes": str(p.get("notes", "")).strip(),
        })
    norm_suppliers = []
    for i, s in enumerate(suppliers):
        ctx = f"watchlist.suppliers[{i}]"
        if not isinstance(s, dict):
            raise ProfileError(f"{ctx}: must be a mapping with name/relationship/criticality")
        criticality = _req_str(s, "criticality", ctx)
        if criticality not in ALLOWED_CRITICALITY:
            raise ProfileError(f"{ctx}.criticality {criticality!r} not in {sorted(ALLOWED_CRITICALITY)}")
        norm_suppliers.append({
            "name": _req_str(s, "name", ctx),
            "relationship": _req_str(s, "relationship", ctx),
            "criticality": criticality,
            "notes": str(s.get("notes", "")).strip(),
        })
    for i, topic in enumerate(interests):
        if not isinstance(topic, str) or not topic.strip():
            raise ProfileError(f"watchlist.interests[{i}]: must be a non-empty string")

    vt = profile.get("vulnerability_triage")
    if not isinstance(vt, dict):
        raise ProfileError("vulnerability_triage: must be a mapping")
    categories = vt.get("categories", [])
    if not isinstance(categories, list):
        raise ProfileError("vulnerability_triage.categories: must be a list")
    norm_categories = []
    seen_ids: set[str] = set()
    for i, c in enumerate(categories):
        ctx = f"vulnerability_triage.categories[{i}]"
        if not isinstance(c, dict):
            raise ProfileError(f"{ctx}: must be a mapping with id/name/criteria/response")
        cid = _req_str(c, "id", ctx)
        if not CATEGORY_ID_RE.match(cid):
            raise ProfileError(f"{ctx}.id {cid!r}: max 16 chars, alphanumeric + '-'")
        if cid in seen_ids:
            raise ProfileError(f"{ctx}.id {cid!r}: duplicate category id")
        seen_ids.add(cid)
        norm_categories.append({
            "id": cid,
            "name": _req_str(c, "name", ctx),
            "criteria": _req_str(c, "criteria", ctx),
            "response": _req_str(c, "response", ctx),
        })
    default_category = str(vt.get("default_category", "")).strip()
    if norm_categories and default_category and default_category not in seen_ids:
        raise ProfileError(
            f"vulnerability_triage.default_category {default_category!r} is not a defined category id")
    if not norm_categories:
        default_category = ""

    # deployment (v2.66) — optional section; defaults preserve the historic
    # public GitHub-Pages deployment.
    dep = profile.get("deployment", {})
    if not isinstance(dep, dict):
        raise ProfileError("deployment: must be a mapping")
    visibility = str(dep.get("visibility", "public")).strip().lower()
    if visibility not in {"public", "private"}:
        raise ProfileError(f"deployment.visibility {visibility!r} must be public or private")
    site_url = str(dep.get("site_url", "https://ctipilot.ch/")).strip()
    if site_url and not re.match(r"^https?://\S+$", site_url):
        raise ProfileError(f"deployment.site_url {site_url!r} must be an http(s) URL or empty")

    return {
        "profile_version": 1,
        "organization": norm_org,
        "watchlist": {
            "products": norm_products,
            "suppliers": norm_suppliers,
            "interests": [t.strip() for t in interests],
        },
        "vulnerability_triage": {
            "intro": str(vt.get("intro", "")).strip(),
            "default_category": default_category,
            "categories": norm_categories,
        },
        "deployment": {
            "visibility": visibility,
            "site_url": site_url,
        },
    }


def load_profile(path: Path = CONFIG_PATH) -> dict[str, Any]:
    if not path.exists():
        raise ProfileError(f"config not found at {path}")
    parsed = parse_yaml_subset(path.read_text(encoding="utf-8"), source=str(path))
    return validate_profile(parsed)


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

GENERATED_NOTE = ("<!-- GENERATED from config/org-profile.yaml — do not edit by hand; "
                  "edit the config and run: python3 tools/compose_prompts.py --write -->")


def _flow(text: str) -> str:
    """Fold a block scalar into one line."""
    return re.sub(r"\s+", " ", text).strip()


def _cell(text: str) -> str:
    """Make a string safe inside a Markdown table cell."""
    return _flow(text).replace("|", "\\|") or "—"


def _sector_phrase(org: dict[str, Any]) -> str:
    phrase = f"**{org['sector']}**"
    if org["additional_sectors"]:
        phrase += " (additional sectors: " + ", ".join(org["additional_sectors"]) + ")"
    return phrase


def _render_mission(profile: dict[str, Any], kind: str) -> str:
    org = profile["organization"]
    artifact = {"daily": "daily brief", "weekly": "**weekly summary**"}[kind]
    lines = [
        GENERATED_NOTE,
        f"You are a senior cyber threat intelligence officer producing a {artifact} "
        f"on cyber threats relevant to **{org['name']}** — {_flow(org['description'])}. "
        f"Coverage focus: **{org['region_focus']}**, primary sector lens {_sector_phrase(org)}. "
        "The general threat landscape for this focus ALWAYS comes first; the organization "
        "watchlists (§ Organization profile & watchlists) sharpen relevance on top of it — "
        "they never replace it.",
        "",
        f"**Audience:** {_flow(org['audience'])}",
    ]
    return "\n".join(lines)


def _render_research_mission(profile: dict[str, Any]) -> str:
    org = profile["organization"]
    return "\n".join([
        GENERATED_NOTE,
        f"You are part of a defensive cyber-intelligence workflow for **{org['name']}** — "
        f"defending {_flow(org['description'])}. Coverage focus: **{org['region_focus']}**, "
        f"primary sector lens {_sector_phrase(org)}. Surface what is publicly known so "
        "defenders can build awareness and prioritise their own work. Output is for "
        "awareness — **no IOCs, no rule code, no operational attack details, no vanity "
        "metrics**.",
    ])


def _render_research_audience(profile: dict[str, Any]) -> str:
    org = profile["organization"]
    return "\n".join([
        GENERATED_NOTE,
        f"{_flow(org['audience'])} Surface-level talking points are filler — every item "
        "must give enough specificity to reason about detection, hunt, and hardening "
        "(vulnerable component / file / function / RPC interface, prerequisites, technique "
        "class with MITRE ATT&CK IDs, affected and patched versions, observed exploitation "
        "status).",
    ])


def _render_products(products: list[dict[str, Any]]) -> list[str]:
    if not products:
        return ["**Product watchlist:** none configured — the product sweep is a no-op; "
                "general coverage rules apply unchanged."]
    out = [f"**Product watchlist ({len(products)} entries):**", "",
           "| Product | Vendor | Exposure | Criticality | Notes |",
           "|---|---|---|---|---|"]
    for p in products:
        out.append(f"| {_cell(p['name'])} | {_cell(p['vendor'])} | {p['exposure']} "
                   f"| {p['criticality']} | {_cell(p['notes'])} |")
    return out


def _render_suppliers(suppliers: list[dict[str, Any]]) -> list[str]:
    if not suppliers:
        return ["**Supplier / third-party watchlist:** none configured — the supplier "
                "sweep is a no-op; general coverage rules apply unchanged."]
    out = [f"**Supplier / third-party watchlist ({len(suppliers)} entries):**", "",
           "| Supplier | Relationship | Criticality | Notes |",
           "|---|---|---|---|"]
    for s in suppliers:
        out.append(f"| {_cell(s['name'])} | {_cell(s['relationship'])} "
                   f"| {s['criticality']} | {_cell(s['notes'])} |")
    return out


def _render_interests(interests: list[str]) -> list[str]:
    if not interests:
        return ["**Standing intelligence interests:** none configured."]
    out = ["**Standing intelligence interests:**", ""]
    out.extend(f"- {_flow(t)}" for t in interests)
    return out


def _render_triage_table(vt: dict[str, Any]) -> list[str]:
    out = ["| Id | Name | Criteria | Response target |", "|---|---|---|---|"]
    for c in vt["categories"]:
        out.append(f"| {c['id']} | {_cell(c['name'])} | {_cell(c['criteria'])} "
                   f"| {_cell(c['response'])} |")
    return out


def _render_triage(profile: dict[str, Any]) -> list[str]:
    vt = profile["vulnerability_triage"]
    org = profile["organization"]
    if not vt["categories"]:
        return ["**Vulnerability-triage scheme:** none configured — omit the "
                "`**Org triage**` line everywhere; do not invent a rating."]
    out = [f"**Vulnerability-triage scheme ({org['short_name']}):**"
           + (f" {_flow(vt['intro'])}" if vt["intro"] else ""), ""]
    out.extend(_render_triage_table(vt))
    out.append("")
    if vt["default_category"]:
        out.append(f"Default category when no criteria clearly match: **{vt['default_category']}** "
                   "(state why the specific criteria did not match).")
    else:
        out.append("No default category is defined — when no criteria clearly match, pick "
                   "the closest by criteria and say so in the triage clause.")
    return out


def _render_org_data(profile: dict[str, Any]) -> str:
    org = profile["organization"]
    wl = profile["watchlist"]
    head = (f"**Organization:** {org['name']} ({org['short_name']}) · "
            f"**Primary sector:** {org['sector']}")
    if org["additional_sectors"]:
        head += " · **Additional sectors:** " + ", ".join(org["additional_sectors"])
    head += (f" · **Home region:** {org['home_region']} · "
             f"**Coverage focus:** {org['region_focus']}")
    dep = profile["deployment"]
    dep_line = (f"**Deployment:** {dep['visibility']} · **Site URL:** "
                + (dep["site_url"] or "none (site polling disabled)"))
    if dep["visibility"] == "public":
        dep_line += (" — the brief publishes to the OPEN INTERNET: closed-source "
                     "content above TLP:CLEAR must NEVER appear in it "
                     "(`check_brief.py` FAILs the commit).")
    else:
        dep_line += (" — private deployment: closed-source content up to the "
                     "drop file's TLP marking may be cited (unlinked).")
    lines: list[str] = [GENERATED_NOTE, head, "",
                        f"**Constituency:** {_flow(org['description'])}", "",
                        dep_line, ""]
    lines.extend(_render_products(wl["products"]))
    lines.append("")
    lines.extend(_render_suppliers(wl["suppliers"]))
    lines.append("")
    lines.extend(_render_interests(wl["interests"]))
    lines.append("")
    lines.extend(_render_triage(profile))
    return "\n".join(lines)


def _render_verify_context(profile: dict[str, Any]) -> str:
    org = profile["organization"]
    wl = profile["watchlist"]
    vt = profile["vulnerability_triage"]
    lines: list[str] = [GENERATED_NOTE]
    head = (f"**Organization served:** {org['name']} ({org['short_name']}) · "
            f"**Primary sector:** {org['sector']}")
    if org["additional_sectors"]:
        head += " · **Additional sectors:** " + ", ".join(org["additional_sectors"])
    head += (f" · **Home region:** {org['home_region']} · "
             f"**Coverage focus:** {org['region_focus']}")
    lines.append(head)
    lines.append("")
    lines.append(f"**Constituency:** {_flow(org['description'])}")
    lines.append("")
    lines.append(f"**Audience:** {_flow(org['audience'])}")
    lines.append("")
    dep = profile["deployment"]
    if dep["visibility"] == "public":
        lines.append("**Deployment:** public — the brief publishes to the open "
                     "internet. Any closed-source citation marked above TLP:CLEAR "
                     "is a defect the mechanical gate also FAILs; flag it F7 "
                     "(drop) with the TLP violation named.")
    else:
        lines.append("**Deployment:** private — closed-source citations up to the "
                     "referenced drop file's TLP marking are acceptable. Verify "
                     "each citation's TLP against the file's front-matter.")
    lines.append("")
    if wl["products"] or wl["suppliers"] or wl["interests"]:
        prods = ", ".join(f"{p['name']} ({p['vendor']})" for p in wl["products"]) or "none"
        supps = ", ".join(f"{s['name']} ({s['relationship']})" for s in wl["suppliers"]) or "none"
        ints = "; ".join(_flow(t) for t in wl["interests"]) or "none"
        lines.append(f"**Watchlisted products:** {prods}")
        lines.append(f"**Watchlisted suppliers:** {supps}")
        lines.append(f"**Standing interests:** {ints}")
        lines.append("")
        lines.append("A watchlist match justifies inclusion at moderate severity (the "
                     "relevance bar is deliberately lower for these — do not flag them as "
                     "off-audience for severity alone), and such items must carry the "
                     "`watchlist` tag in their footer `Tags:`. Every truth gate applies "
                     "unchanged. A brief dominated by watchlist items (guideline: more than "
                     "about a third of the § 1 + § 2 items) has over-rotated onto the "
                     "watchlist — flag it (F11) so the main agent rebalances.")
    else:
        lines.append("**Watchlists:** none configured — the `watchlist` footer tag should "
                     "not appear in this brief; flag any use of it (F16).")
    lines.append("")
    if vt["categories"]:
        lines.append(f"**Org-triage scheme (configured, short name `{org['short_name']}`):**")
        lines.append("")
        lines.extend(_render_triage_table(vt))
        lines.append("")
        default = vt["default_category"] or "none defined"
        lines.append(f"Default category: {default}. Every CVE-typed item in the daily § 0 "
                     "Immediate Action callout, § 2 Trending Vulnerabilities, and a CVE-typed "
                     "§ 5 deep dive (weekly: § 3 Vulnerability roll-up) must end its body with "
                     f"`**Org triage ({org['short_name']}):** <id> — <name>. <clause>` "
                     "immediately before the metadata footer. The chosen category must follow "
                     "from facts the item itself cites (exposure class, auth prerequisite, "
                     "exploitation status, watchlist membership). Missing line, unknown "
                     "category id, or a triage clause introducing facts no cited source "
                     "supports → flag F16 (org-triage, editorial).")
    else:
        lines.append("**Org-triage scheme:** none configured — any `**Org triage**` line "
                     "in the brief is a defect; flag it F16 (org-triage, editorial).")
    return "\n".join(lines)


def render_blocks(profile: dict[str, Any]) -> dict[str, str]:
    return {
        "daily-mission": _render_mission(profile, "daily"),
        "weekly-mission": _render_mission(profile, "weekly"),
        "research-mission": _render_research_mission(profile),
        "research-audience": _render_research_audience(profile),
        "org-data": _render_org_data(profile),
        "verify-context": _render_verify_context(profile),
    }


# ---------------------------------------------------------------------------
# Managed-block replacement
# ---------------------------------------------------------------------------

def replace_blocks(text: str, blocks: dict[str, str], *,
                   required: list[str], source: str) -> tuple[str, list[str]]:
    """Replace the content of every ORG-PROFILE block in `text`.

    Returns (new_text, names_replaced). Raises ProfileError on structural
    problems: unknown block name, nested/unterminated blocks, or a required
    block missing from the file.
    """
    out_lines: list[str] = []
    replaced: list[str] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        m = BEGIN_RE.match(lines[i])
        if not m:
            if END_RE.match(lines[i]):
                raise ProfileError(f"{source}:{i + 1}: ORG-PROFILE:END without a BEGIN")
            out_lines.append(lines[i])
            i += 1
            continue
        name = m.group("name")
        if name not in blocks:
            raise ProfileError(f"{source}:{i + 1}: unknown ORG-PROFILE block {name!r}")
        # Find the matching END marker.
        j = i + 1
        end_idx: int | None = None
        while j < len(lines):
            if BEGIN_RE.match(lines[j]):
                raise ProfileError(
                    f"{source}:{j + 1}: nested ORG-PROFILE:BEGIN inside block {name!r}")
            em = END_RE.match(lines[j])
            if em:
                if em.group("name") != name:
                    raise ProfileError(
                        f"{source}:{j + 1}: ORG-PROFILE:END name mismatch "
                        f"(expected {name!r}, got {em.group('name')!r})")
                end_idx = j
                break
            j += 1
        if end_idx is None:
            raise ProfileError(f"{source}:{i + 1}: unterminated ORG-PROFILE block {name!r}")
        out_lines.append(lines[i])                       # BEGIN marker
        out_lines.extend(blocks[name].splitlines())      # fresh content
        out_lines.append(lines[end_idx])                 # END marker
        replaced.append(name)
        i = end_idx + 1

    missing = [n for n in required if n not in replaced]
    if missing:
        raise ProfileError(f"{source}: required ORG-PROFILE block(s) missing: {missing}")

    new_text = "\n".join(out_lines)
    if text.endswith("\n"):
        new_text += "\n"
    return new_text, replaced


def compose(write: bool) -> tuple[bool, list[str]]:
    """Compose every target. Returns (in_sync, messages)."""
    profile = load_profile()
    blocks = render_blocks(profile)
    messages: list[str] = []
    in_sync = True
    for rel, required in TARGETS:
        path = ROOT / rel
        if not path.exists():
            raise ProfileError(f"target file missing: {rel}")
        old = path.read_text(encoding="utf-8")
        new, _ = replace_blocks(old, blocks, required=required, source=rel)
        if new != old:
            in_sync = False
            if write:
                path.write_text(new, encoding="utf-8")
                messages.append(f"composed: {rel}")
            else:
                messages.append(f"drift: {rel} (managed blocks do not match the config)")
        else:
            messages.append(f"in-sync: {rel}")
    return in_sync, messages


# ---------------------------------------------------------------------------
# Selftest
# ---------------------------------------------------------------------------

_SELFTEST_YAML = """\
profile_version: 1
organization:
  name: "Test Org"
  short_name: "TST"
  sector: "finance"
  additional_sectors:
    - "energy"
  region_focus: "DACH"
  home_region: "dach"
  description: |
    a test constituency spanning
    two lines
  audience: |
    test readers
watchlist:
  products:
    - name: "Windows Server"
      vendor: "Microsoft"
      exposure: "internal"
      criticality: "high"
      notes: "pipe | in notes"
    - name: "FortiGate"
      vendor: "Fortinet"
      exposure: "internet-facing"
      criticality: "high"
  suppliers:
    - name: "Example AG"
      relationship: "MSP"
      criticality: "medium"
      notes: ""
  interests:
    - "test topic"
vulnerability_triage:
  intro: |
    Test intro.
  default_category: "P2"
  categories:
    - id: "P1"
      name: "Emergency"
      criteria: |
        exploited AND internet-facing
      response: "24h"
    - id: "P2"
      name: "Scheduled"
      criteria: "everything else"
      response: "patch window"
"""


def selftest() -> int:
    failures: list[str] = []

    def check(cond: bool, label: str) -> None:
        if cond:
            print(f"  ok: {label}")
        else:
            failures.append(label)
            print(f"  FAIL: {label}")

    # 1. Parser round-trip on the embedded fixture.
    parsed = parse_yaml_subset(_SELFTEST_YAML, source="<selftest>")
    check(parsed["organization"]["name"] == "Test Org", "scalar with quotes")
    check(parsed["organization"]["description"] == "a test constituency spanning\ntwo lines",
          "block scalar")
    check(parsed["watchlist"]["products"][0]["notes"] == "pipe | in notes",
          "list-of-mappings first item")
    check(parsed["watchlist"]["products"][1]["vendor"] == "Fortinet",
          "list-of-mappings second item")
    check(parsed["watchlist"]["interests"] == ["test topic"], "list of scalars")
    check(parsed["vulnerability_triage"]["categories"][0]["criteria"]
          == "exploited AND internet-facing", "block scalar inside list item")

    # 2. Validation of the fixture against a synthetic taxonomy.
    tax = {"sectors": {"finance", "energy"}, "regions": {"dach"}}
    profile = validate_profile(parsed, tax)
    check(profile["vulnerability_triage"]["default_category"] == "P2", "triage default")
    check(profile["deployment"] == {"visibility": "public",
                                    "site_url": "https://ctipilot.ch/"},
          "deployment defaults when section absent")
    import copy as _copy
    dep_variant = _copy.deepcopy(parsed)
    dep_variant["deployment"] = {"visibility": "private", "site_url": ""}
    dp = validate_profile(dep_variant, tax)
    check(dp["deployment"]["visibility"] == "private" and dp["deployment"]["site_url"] == "",
          "private deployment with empty site_url accepted")
    dep_bad = _copy.deepcopy(parsed)
    dep_bad["deployment"] = {"visibility": "internal"}
    try:
        validate_profile(dep_bad, tax)
        check(False, "invalid deployment.visibility rejected")
    except ProfileError:
        check(True, "invalid deployment.visibility rejected")

    # 3. Validation failures fail loud.
    import copy
    bad = copy.deepcopy(parsed)
    bad["watchlist"]["products"][0]["exposure"] = "bogus"
    try:
        validate_profile(bad, tax)
        check(False, "invalid exposure rejected")
    except ProfileError:
        check(True, "invalid exposure rejected")
    bad2 = copy.deepcopy(parsed)
    bad2["organization"]["sector"] = "not-a-sector"
    try:
        validate_profile(bad2, tax)
        check(False, "invalid sector rejected")
    except ProfileError:
        check(True, "invalid sector rejected")

    # 4. Rendering is deterministic and escapes table cells.
    blocks_a = render_blocks(profile)
    blocks_b = render_blocks(profile)
    check(blocks_a == blocks_b, "rendering deterministic")
    check("pipe \\| in notes" in blocks_a["org-data"], "table-cell pipe escaped")
    check(set(blocks_a) == {"daily-mission", "weekly-mission", "research-mission",
                            "research-audience", "org-data", "verify-context"},
          "all block names rendered")

    # 5. Block replacement: idempotent, preserves surroundings, catches drift.
    doc = ("before\n"
           "<!-- ORG-PROFILE:BEGIN org-data -->\n"
           "stale\n"
           "<!-- ORG-PROFILE:END org-data -->\n"
           "after\n")
    new, replaced = replace_blocks(doc, blocks_a, required=["org-data"], source="<doc>")
    check(replaced == ["org-data"], "block replaced")
    check(new.startswith("before\n") and new.endswith("after\n"), "surroundings preserved")
    new2, _ = replace_blocks(new, blocks_a, required=["org-data"], source="<doc>")
    check(new2 == new, "replacement idempotent")
    try:
        replace_blocks("no markers\n", blocks_a, required=["org-data"], source="<doc>")
        check(False, "missing required block rejected")
    except ProfileError:
        check(True, "missing required block rejected")
    try:
        replace_blocks("<!-- ORG-PROFILE:BEGIN org-data -->\nx\n", blocks_a,
                       required=["org-data"], source="<doc>")
        check(False, "unterminated block rejected")
    except ProfileError:
        check(True, "unterminated block rejected")

    # 6. The real config parses, validates, and renders.
    real = load_profile()
    render_blocks(real)
    check(True, "config/org-profile.yaml parses + validates + renders")

    print(f"\nselftest: {'PASS' if not failures else 'FAIL'} "
          f"({len(failures)} failure(s))")
    return 0 if not failures else 1


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true",
                      help="verify managed blocks match the config (exit 3 on drift)")
    mode.add_argument("--write", action="store_true",
                      help="regenerate managed blocks in place")
    mode.add_argument("--dump", action="store_true",
                      help="print the parsed profile as JSON")
    mode.add_argument("--get", metavar="DOTTED.KEY",
                      help="print one profile value (e.g. deployment.site_url)")
    mode.add_argument("--selftest", action="store_true",
                      help="run embedded parser/renderer tests")
    p.add_argument("--quiet", action="store_true", help="suppress per-file messages")
    args = p.parse_args()

    if args.selftest:
        return selftest()

    try:
        if args.dump:
            print(json.dumps(load_profile(), indent=2, ensure_ascii=False))
            return 0
        if args.get:
            node: Any = load_profile()
            for part in args.get.split("."):
                if not isinstance(node, dict) or part not in node:
                    print(f"compose_prompts: ERROR: unknown key {args.get!r}", file=sys.stderr)
                    return 2
                node = node[part]
            print(node if isinstance(node, str) else json.dumps(node, ensure_ascii=False))
            return 0
        in_sync, messages = compose(write=args.write)
    except ProfileError as e:
        print(f"compose_prompts: ERROR: {e}", file=sys.stderr)
        return 2
    if not args.quiet:
        for msg in messages:
            print(msg)
    if args.write:
        return 0
    if not in_sync:
        print("compose_prompts: DRIFT — run `python3 tools/compose_prompts.py --write` "
              "and commit the result", file=sys.stderr)
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
