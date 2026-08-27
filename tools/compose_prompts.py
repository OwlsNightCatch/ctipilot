#!/usr/bin/env python3
"""Render config/org-profile.yaml into the ORG-PROFILE managed blocks.

The organization profile (org description, sector/region lens, product +
supplier watchlists, vulnerability-triage scheme) is parameterized in
`config/org-profile.yaml`. This script composes those values into managed
marker blocks inside the master prompts and the sub-agent definitions, so
every agent in the workflow sees the same organization context:

    prompts/cti-run.md                    blocks: daily-mission, org-data, org-policy-watch
    prompts/verification.md               blocks: org-certs
    .claude/agents/cti-research.md        blocks: research-mission, research-audience, org-data, org-certs
    .claude/agents/cti-verification.md    blocks: verify-context

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
    # v4.0: the weekly strategic routine (prompts/weekly-summary.md) was
    # retired; its standing policy / regulatory watch moved into the intel
    # run's S2 (home region & sector) domain.
    ("prompts/cti-run.md", ["daily-mission", "org-data", "org-policy-watch"]),
    ("prompts/verification.md", ["org-certs"]),
    (".claude/agents/cti-research.md",
     ["research-mission", "research-audience", "org-data", "org-certs"]),
    (".claude/agents/cti-verification.md", ["verify-context"]),
]

# Upstream defaults for the optional org-profile keys below — used when the
# key is ABSENT from config/org-profile.yaml (an explicit empty list is a
# deliberate "disable" and is honoured as such).
DEFAULT_NATIONAL_CERTS: list[str] = [
    "NCSC-CH", "GovCERT.ch", "CERT-EU", "ENISA", "BSI", "ANSSI/CERT-FR",
    "NCSC-UK", "NCSC-NL", "CISA", "CCN-CERT", "AGID-CSIRT-IT", "CERT.at",
    "CERT-PL",
]
DEFAULT_POLICY_WATCH: list[str] = [
    "NCSC.ch announcements (use `tools/fetch_source.py` — direct WebFetch 403s)",
    "FINMA guidance",
    "EU NIS2 / DORA / CRA developments (transposition steps, implementation deadlines)",
    "OFCOM / BAKOM publications",
    "Council of Europe cybercrime convention items",
    "sanctions and law-enforcement actions affecting publicly-known threat-actor infrastructure",
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

    # classification — how every item is classified. `triage_kinds` lists the
    # entry kinds classified with the vulnerability-triage scheme (org_triage);
    # everything else uses the Admiralty `intel_classification`. Optional
    # section: an absent section keeps the upstream default (triage for
    # `vulnerability`, Admiralty for everything else); empty code lists disable
    # the intelligence-classification requirement entirely.
    cl = profile.get("classification", {})
    if not isinstance(cl, dict):
        raise ProfileError("classification: must be a mapping")
    triage_kinds = cl.get("triage_kinds", ["vulnerability"])
    if not isinstance(triage_kinds, list) or any(
            not isinstance(k, str) or not k.strip() for k in triage_kinds):
        raise ProfileError("classification.triage_kinds: must be a list of non-empty strings")
    triage_kinds = [k.strip() for k in triage_kinds]
    ic = cl.get("intel_classification", {})
    if not isinstance(ic, dict):
        raise ProfileError("classification.intel_classification: must be a mapping")

    def _codes(dim: str) -> list[dict[str, str]]:
        raw = ic.get(dim, [])
        if not isinstance(raw, list):
            raise ProfileError(f"classification.intel_classification.{dim}: must be a list")
        out_codes: list[dict[str, str]] = []
        seen: set[str] = set()
        for i, c in enumerate(raw):
            ctx = f"classification.intel_classification.{dim}[{i}]"
            if not isinstance(c, dict):
                raise ProfileError(f"{ctx}: must be a mapping with code/definition")
            code = _req_str(c, "code", ctx)
            if len(code) > 4:
                raise ProfileError(f"{ctx}.code {code!r}: max 4 chars")
            if code in seen:
                raise ProfileError(f"{ctx}.code {code!r}: duplicate")
            seen.add(code)
            out_codes.append({"code": code, "definition": _req_str(c, "definition", ctx)})
        return out_codes

    rel_codes = _codes("reliability")
    cred_codes = _codes("credibility")
    if bool(rel_codes) != bool(cred_codes):
        raise ProfileError(
            "classification.intel_classification: define BOTH reliability and credibility "
            "codes, or neither (leave both empty to disable intelligence classification)")
    ic_name = str(ic.get("name", "NATO Admiralty code")).strip() or "NATO Admiralty code"
    ic_default = str(ic.get("default", "")).strip()
    if ic_default and rel_codes and cred_codes:
        rset = {c["code"] for c in rel_codes}
        cset = {c["code"] for c in cred_codes}
        if not any(ic_default.startswith(r) and ic_default[len(r):] in cset for r in rset):
            raise ProfileError(
                f"classification.intel_classification.default {ic_default!r} is not a defined "
                "<reliability><credibility> code pair")

    # deployment — optional section; only the publish-polling site URL now.
    # There is no visibility / TLP gate: this pipeline never filters on TLP or
    # a public/private flag (everything readable, including intel/, is fair
    # game to process into entries and reports).
    dep = profile.get("deployment", {})
    if not isinstance(dep, dict):
        raise ProfileError("deployment: must be a mapping")
    if "visibility" in dep:
        raise ProfileError(
            "deployment.visibility is no longer supported — this pipeline does not filter on "
            "TLP or a public/private flag; remove the key from config/org-profile.yaml")
    site_url = str(dep.get("site_url", "https://ctipilot.ch/")).strip()
    if site_url and not re.match(r"^https?://\S+$", site_url):
        raise ProfileError(f"deployment.site_url {site_url!r} must be an http(s) URL or empty")

    # national_certs / policy_watch — optional lists of strings; an absent
    # key keeps the upstream default, an explicit [] disables the feature.
    def _opt_str_list(key: str, default: list[str]) -> list[str]:
        raw = profile.get(key)
        if raw is None:
            return list(default)
        if not isinstance(raw, list) or not all(
                isinstance(x, str) and x.strip() for x in raw):
            raise ProfileError(f"{key}: must be a list of non-empty strings (or omitted)")
        return [x.strip() for x in raw]

    national_certs = _opt_str_list("national_certs", DEFAULT_NATIONAL_CERTS)
    policy_watch = _opt_str_list("policy_watch", DEFAULT_POLICY_WATCH)

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
        "classification": {
            "triage_kinds": triage_kinds,
            "intel_classification": {
                "name": ic_name,
                "default": ic_default,
                "reliability": rel_codes,
                "credibility": cred_codes,
            },
        },
        "deployment": {
            "site_url": site_url,
        },
        "national_certs": national_certs,
        "policy_watch": policy_watch,
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


def _render_mission(profile: dict[str, Any], kind: str = "daily") -> str:
    org = profile["organization"]
    artifact = {
        "daily": "operating the continuous intelligence pipeline",
    }[kind]
    lines = [
        GENERATED_NOTE,
        f"You are a senior cyber threat intelligence officer {artifact} "
        f"for **{org['name']}** — {_flow(org['description'])}. "
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
        return ["**Vulnerability-triage scheme:** none configured — leave "
                "`org_triage: null` everywhere; do not invent a rating. "
                "Vulnerability-kind entries instead carry the Admiralty "
                "`classification` block like every other kind (see § Classification "
                "above) — **no entry ships unrated**; `tools/check_run.py` FAILs a "
                "missing rating."]
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


def _render_classification(profile: dict[str, Any]) -> list[str]:
    """Intelligence-classification (Admiralty) scheme + the triage-kind split.
    Rendered into the org-data block seen by the daily/weekly main agents and
    the research agent. The triage-kind exemption applies only while a
    vulnerability-triage scheme actually exists — with none configured, EVERY
    entry (triage kinds included) carries the Admiralty block, so no entry
    ever ships unrated."""
    cl = profile["classification"]
    ic = cl["intel_classification"]
    triage = cl["triage_kinds"]
    triage_phrase = ", ".join(f"`{k}`" for k in triage) if triage else "none"
    scheme_configured = bool(profile["vulnerability_triage"]["categories"])
    if not ic["reliability"] or not ic["credibility"]:
        return ["**Classification:** intelligence-classification codes are not configured — "
                "leave `classification: null` on every entry (vulnerability-kind entries still "
                "carry `org_triage`)."]
    if scheme_configured and triage:
        head = (f"**Classification — {ic['name']}:** every entry EXCEPT the triage kinds "
                f"({triage_phrase}) carries `classification: {{reliability, credibility}}` in its "
                "frontmatter — a source-reliability LETTER and an information-credibility NUMBER, "
                "assessed independently and rendered together (e.g. `B2`). The triage kinds carry "
                "`org_triage` instead (see the vulnerability-triage scheme below).")
    else:
        head = (f"**Classification — {ic['name']}:** EVERY entry — including the triage kinds "
                f"({triage_phrase}), because no vulnerability-triage scheme is configured — "
                "carries `classification: {reliability, credibility}` in its frontmatter: a "
                "source-reliability LETTER and an information-credibility NUMBER, assessed "
                "independently and rendered together (e.g. `B2`). **No entry ships unrated** — "
                "`tools/check_run.py` FAILs a missing rating.")
    out = [head, ""]
    out.append("_Source reliability — rate the SOURCE (its authority + track record):_")
    out.append("")
    out.append("| Code | Meaning |")
    out.append("|---|---|")
    for c in ic["reliability"]:
        out.append(f"| {c['code']} | {_cell(c['definition'])} |")
    out.append("")
    out.append("_Information credibility — rate the ITEM (its truth given corroboration):_")
    out.append("")
    out.append("| Code | Meaning |")
    out.append("|---|---|")
    for c in ic["credibility"]:
        out.append(f"| {c['code']} | {_cell(c['definition'])} |")
    out.append("")
    out.append("Weight original / primary sources over news and aggregators: a first-party "
               "authority (a national CERT for its own jurisdiction, a vendor PSIRT for its own "
               "product) is A; original research labs and large corroborating outlets are "
               "typically B; sources that mainly re-report are C or lower. The two axes are "
               "independent — a reliable source does NOT by itself make an uncorroborated claim "
               "credible: independent corroboration is what drives the credibility number toward "
               "1, while a single uncorroborated claim from a reliable source is 2, not 1.")
    if ic["default"]:
        out.append("")
        out.append(f"Conservative fallback when an item cannot be assessed further: "
                   f"**{ic['default']}** (state why in the entry's sourcing note).")
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
    dep_line = ("**Deployment · Site URL:** "
                + (dep["site_url"] or "none (site polling disabled)")
                + " — there is NO TLP / public-private gate: everything the agents can read, "
                  "including every file under intel/, is fair game to process into entries and "
                  "reports; nothing is withheld or downgraded on the basis of a TLP marking.")
    lines: list[str] = [GENERATED_NOTE, head, "",
                        f"**Constituency:** {_flow(org['description'])}", "",
                        dep_line, ""]
    lines.extend(_render_products(wl["products"]))
    lines.append("")
    lines.extend(_render_suppliers(wl["suppliers"]))
    lines.append("")
    lines.extend(_render_interests(wl["interests"]))
    lines.append("")
    lines.extend(_render_classification(profile))
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
    certs = profile["national_certs"]
    if certs:
        lines.append("**National-CERT single-source carve-out list:** "
                     + ", ".join(certs)
                     + " — acceptable as a single source when the authority is "
                       "the primary disclosing party for its own jurisdiction "
                       "or an advisory it owns.")
    else:
        lines.append("**National-CERT single-source carve-out:** disabled for "
                     "this deployment — flag every single-source item "
                     "regardless of the source's authority.")
    lines.append("")
    lines.append("**Deployment:** no TLP / public-private gate — every file the agents can "
                 "read (including everything under intel/) is fair game; nothing is withheld, "
                 "downgraded, or flagged on the basis of a TLP marking. Do NOT raise TLP "
                 "findings.")
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
                     "off-audience for severity alone), and such entries must carry "
                     "`watchlist_hit: true` plus the `watchlist` tag. Every truth gate "
                     "applies unchanged. A window dominated by watchlist entries "
                     "(guideline: more than about a third of the threat + vulnerability "
                     "entries) has over-rotated onto the watchlist — flag it (F11) so the "
                     "main agent rebalances.")
    else:
        lines.append("**Watchlists:** none configured — `watchlist_hit: true` and the "
                     "`watchlist` tag should not appear on any entry; flag any use (F16).")
    lines.append("")
    if vt["categories"]:
        lines.append(f"**Org-triage scheme (configured, short name `{org['short_name']}`):**")
        lines.append("")
        lines.extend(_render_triage_table(vt))
        lines.append("")
        default = vt["default_category"] or "none defined"
        lines.append(f"Default category: {default}. Every `vulnerability`-kind entry (and "
                     "any critical-priority CVE-carrying entry) must set frontmatter "
                     "`org_triage: {category, rationale}`. The chosen category must follow "
                     "from facts the entry itself cites (exposure class, auth prerequisite, "
                     "exploitation status, watchlist membership). Missing block, unknown "
                     "category id, or a rationale introducing facts no cited source "
                     "supports → flag F16 (org-triage, editorial).")
    else:
        lines.append("**Org-triage scheme:** none configured — any non-null `org_triage` "
                     "block on an entry is a defect; flag it F16 (org-triage, editorial).")
    lines.append("")
    cl = profile["classification"]
    ic = cl["intel_classification"]
    triage = cl["triage_kinds"]
    if ic["reliability"] and ic["credibility"]:
        rels = ", ".join(c["code"] for c in ic["reliability"])
        creds = ", ".join(c["code"] for c in ic["credibility"])
        tk = ", ".join(f"`{k}`" for k in triage) if triage else "none"
        if vt["categories"] and triage:
            scope_sentence = (
                f"every entry whose kind is NOT a triage kind ({tk}) must carry "
                f"`classification: {{reliability, credibility}}` with reliability ∈ {{{rels}}} "
                f"and credibility ∈ {{{creds}}}; triage-kind entries carry `org_triage` instead "
                "and must NOT carry `classification`. Flag F17 (classification, editorial) when: "
                "the block is missing on a non-triage entry")
        else:
            scope_sentence = (
                f"EVERY entry — including the triage kinds ({tk}), because no vulnerability-"
                f"triage scheme is configured — must carry `classification: {{reliability, "
                f"credibility}}` with reliability ∈ {{{rels}}} and credibility ∈ {{{creds}}}; "
                "no entry ships unrated. Flag F17 (classification, editorial) when: the block "
                "is missing on ANY entry")
        lines.append(
            f"**Classification ({ic['name']}):** " + scope_sentence
            + "; a code is outside the vocabulary; "
            "the reliability letter plainly contradicts the cited source's nature (e.g. `A` on a "
            "lone blog/forum post, or `A` on a source not in the A tier of sources.json); or the "
            "credibility number is inconsistent with the corroboration the entry actually shows "
            "(e.g. `1` on a single uncorroborated source, which should be 2).")
    else:
        lines.append("**Classification:** intelligence-classification codes are not configured — "
                     "no entry should carry a `classification` block; flag any use F17.")
    return "\n".join(lines)


def _render_certs(profile: dict[str, Any]) -> str:
    """`org-certs` block — the national-CERT single-source carve-out list
    (research agent + prompts/verification.md)."""
    certs = profile["national_certs"]
    lines: list[str] = [GENERATED_NOTE]
    if certs:
        lines.append(
            "**National-CERT single-source carve-out list** — a high-reliability "
            "(Admiralty A / B) national CERT / government cybersecurity authority "
            "acting as the primary disclosing party for its own jurisdiction or an "
            "advisory it owns is acceptable as a single source: " + ", ".join(certs) + ". "
            "The list is deployment-configurable (`national_certs` in "
            "config/org-profile.yaml); treat it as the trust bar, illustrative "
            "rather than exhaustive for same-tier authorities."
        )
    else:
        lines.append(
            "**National-CERT single-source carve-out: DISABLED** — "
            "`national_certs` in config/org-profile.yaml is empty; two-source "
            "verification applies to every item without exception."
        )
    return "\n".join(lines)


def _render_policy_watch(profile: dict[str, Any]) -> str:
    """`org-policy-watch` block — the intel run's S2 (home region & sector)
    standing policy / regulatory watch list (v4.0: inherited from the
    retired weekly's W2 domain)."""
    org = profile["organization"]
    items = profile["policy_watch"]
    lines: list[str] = [GENERATED_NOTE]
    if items:
        lines.append(
            f"Standing policy / regulatory watch for {org['name']} "
            f"({org['region_focus']} · {org['sector']}) — S2 sweeps these every run; a "
            "development ships as a `policy` entry only when it changes what the "
            "constituency's defenders are obliged or advised to do (PD-11 c):"
        )
        lines.append("")
        lines.extend(f"- {_flow(t)}" for t in items)
    else:
        lines.append(
            "No standing policy / regulatory watch configured (`policy_watch` "
            "in config/org-profile.yaml is empty) — cover only policy "
            "developments with direct, sourced operational impact on the "
            "constituency."
        )
    return "\n".join(lines)


def render_blocks(profile: dict[str, Any]) -> dict[str, str]:
    return {
        "daily-mission": _render_mission(profile, "daily"),
        "research-mission": _render_research_mission(profile),
        "research-audience": _render_research_audience(profile),
        "org-data": _render_org_data(profile),
        "verify-context": _render_verify_context(profile),
        "org-certs": _render_certs(profile),
        "org-policy-watch": _render_policy_watch(profile),
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
classification:
  triage_kinds:
    - "vulnerability"
  intel_classification:
    name: "NATO Admiralty code"
    default: "C3"
    reliability:
      - code: "A"
        definition: "Completely reliable"
      - code: "B"
        definition: "Usually reliable"
      - code: "C"
        definition: "Fairly reliable"
    credibility:
      - code: "1"
        definition: "Confirmed"
      - code: "2"
        definition: "Probably true"
      - code: "3"
        definition: "Possibly true"
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
    import copy as _copy
    check(profile["deployment"] == {"site_url": "https://ctipilot.ch/"},
          "deployment defaults when section absent (no visibility key)")
    dep_variant = _copy.deepcopy(parsed)
    dep_variant["deployment"] = {"site_url": ""}
    dp = validate_profile(dep_variant, tax)
    check(dp["deployment"]["site_url"] == "", "empty site_url accepted (site polling disabled)")
    dep_bad = _copy.deepcopy(parsed)
    dep_bad["deployment"] = {"visibility": "public"}
    try:
        validate_profile(dep_bad, tax)
        check(False, "deployment.visibility now rejected (TLP/visibility gate removed)")
    except ProfileError:
        check(True, "deployment.visibility now rejected (TLP/visibility gate removed)")

    # classification: parses, orders, and enforces its vocabulary.
    ic_p = profile["classification"]["intel_classification"]
    check([c["code"] for c in ic_p["reliability"]] == ["A", "B", "C"],
          "admiralty reliability codes parsed in order")
    check([c["code"] for c in ic_p["credibility"]] == ["1", "2", "3"],
          "admiralty credibility codes parsed in order")
    check(profile["classification"]["triage_kinds"] == ["vulnerability"], "triage_kinds parsed")
    badcl = _copy.deepcopy(parsed)
    badcl["classification"]["intel_classification"]["default"] = "Z9"
    try:
        validate_profile(badcl, tax)
        check(False, "undefined classification default rejected")
    except ProfileError:
        check(True, "undefined classification default rejected")
    onlyrel = _copy.deepcopy(parsed)
    onlyrel["classification"]["intel_classification"]["credibility"] = []
    try:
        validate_profile(onlyrel, tax)
        check(False, "reliability-without-credibility rejected")
    except ProfileError:
        check(True, "reliability-without-credibility rejected")

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
    check(set(blocks_a) == {"daily-mission", "research-mission",
                            "research-audience", "org-data", "verify-context",
                            "org-certs", "org-policy-watch"},
          "all block names rendered")
    check("NATO Admiralty code" in blocks_a["org-data"], "classification scheme rendered in org-data")
    check("Usually reliable" in blocks_a["org-data"], "reliability code definitions rendered")
    check("Classification (NATO Admiralty code)" in blocks_a["verify-context"],
          "classification verification rendered in verify-context")
    # The triage-kind exemption exists only while a triage scheme does: with
    # a scheme (the fixture) the split rule renders; without one (variant)
    # the no-unrated-entry Admiralty fallback must be spelled out for the
    # composer AND the verifier.
    check("EXCEPT the triage kinds" in blocks_a["org-data"],
          "configured triage scheme renders the org_triage split")
    check("must NOT carry `classification`" in blocks_a["verify-context"],
          "verify-context keeps the split rule when a scheme is configured")
    variant_nts = _copy.deepcopy(parsed)
    variant_nts["vulnerability_triage"] = {"intro": "", "default_category": "",
                                           "categories": []}
    vb_nts = render_blocks(validate_profile(variant_nts, tax))
    check("No entry ships unrated" in vb_nts["org-data"]
          and "including the triage kinds" in vb_nts["org-data"],
          "org-data states the no-scheme Admiralty fallback")
    check("no entry ships unrated" in vb_nts["verify-context"]
          and "missing on ANY entry" in vb_nts["verify-context"],
          "verify-context requires a rating on every entry when no triage scheme exists")
    check("public-private gate" in blocks_a["org-data"] and "TLP:CLEAR" not in blocks_a["org-data"],
          "TLP gate language removed from org-data")

    # 4b. national_certs / policy_watch: absent key → upstream default;
    # explicit values render; explicit [] disables.
    check(profile["national_certs"] == DEFAULT_NATIONAL_CERTS,
          "absent national_certs falls back to upstream default")
    check(profile["policy_watch"] == DEFAULT_POLICY_WATCH,
          "absent policy_watch falls back to upstream default")
    check("NCSC-CH" in blocks_a["org-certs"], "org-certs renders the carve-out list")
    check("FINMA guidance" in blocks_a["org-policy-watch"],
          "org-policy-watch renders the watch list")
    variant = _copy.deepcopy(parsed)
    variant["national_certs"] = ["SingCERT"]
    variant["policy_watch"] = []
    vp = validate_profile(variant, tax)
    vb = render_blocks(vp)
    check("SingCERT" in vb["org-certs"] and "NCSC-CH" not in vb["org-certs"],
          "custom national_certs replaces the default list")
    check("DISABLED" not in vb["org-certs"], "non-empty custom list stays enabled")
    check("No standing policy / regulatory watch configured" in vb["org-policy-watch"],
          "explicit empty policy_watch disables the watch")
    variant2 = _copy.deepcopy(parsed)
    variant2["national_certs"] = []
    vb2 = render_blocks(validate_profile(variant2, tax))
    check("DISABLED" in vb2["org-certs"], "explicit empty national_certs disables carve-out")

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
