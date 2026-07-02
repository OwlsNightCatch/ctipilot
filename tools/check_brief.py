#!/usr/bin/env python3
"""tools/check_brief.py — Phase 5.5 self-check gate (institutionalised).

The agent MUST run this script after Phase 5 (state update) and before Phase 6
(commit + push). The script consolidates every consistency check the prompt
once described inline, plus the build-side smoke tests. A non-zero exit is a
hard stop on the publishing chain.

Usage:
    python3 tools/check_brief.py                  # checks today's brief
    python3 tools/check_brief.py 2026-05-08       # checks brief for that date
    python3 tools/check_brief.py briefs/2026-05-08.md
    python3 tools/check_brief.py --no-build-tests # skip site/test_build.py

Exit codes:
    0   all checks passed (warnings allowed)
    1   one or more FAIL checks
    2   script-level error (brief missing, taxonomy missing, etc.)

Design rules:
    - Stdlib-only. No third-party deps.
    - Importable: site/build.py supplies the footer parser + taxonomy loader,
      so this script and the build agree on parsing rules. If site/build.py
      fails to import, the script falls back to its own minimal parsers and
      logs a WARN — the run still completes.
    - Output is line-by-line `PASS / FAIL / WARN  <check>: <detail>` so the
      agent can copy the failure verbatim into § 8 if it commits anyway.
    - The script never modifies any file. It is read-only. The agent fixes
      drift; this script reports it.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
BRIEFS_DIR = ROOT / "briefs"
STATE_DIR = ROOT / "state"
SOURCES_DIR = ROOT / "sources"
SITE_DIR = ROOT / "site"
TAXONOMY = SITE_DIR / "taxonomy.yaml"
TEST_BUILD = SITE_DIR / "test_build.py"

# --- Severity counters ----------------------------------------------------

FAILS: list[str] = []
WARNS: list[str] = []
PASSES: list[str] = []


def _print(severity: str, label: str, detail: str = "") -> None:
    msg = f"  {severity:<4} {label}" + (f": {detail}" if detail else "")
    print(msg)


def fail(label: str, detail: str = "") -> None:
    FAILS.append(f"{label}: {detail}" if detail else label)
    _print("FAIL", label, detail)


def warn(label: str, detail: str = "") -> None:
    WARNS.append(f"{label}: {detail}" if detail else label)
    _print("WARN", label, detail)


def ok(label: str, detail: str = "") -> None:
    PASSES.append(label)
    _print("PASS", label, detail)


# --- Optional: import build.py so checks share the same parser ------------

try:
    sys.path.insert(0, str(SITE_DIR))
    from build import parse_footer_line, parse_taxonomy, slugify, validate_footer  # type: ignore
    BUILD_IMPORTED = True
except Exception as exc:  # pragma: no cover — fallback path
    BUILD_IMPORTED = False
    _print("WARN", "build-import",
           f"site/build.py unimportable ({exc!s}); falling back to local parsers")

    def slugify(text: str) -> str:
        text = text.lower()
        text = re.sub(r"[^a-z0-9]+", "-", text)
        text = re.sub(r"-+", "-", text)
        return text.strip("-")

    _FOOTER_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def parse_footer_line(line: str) -> dict[str, Any] | None:
        s = line.strip()
        m = re.match(r"^[—-]\s*\*\s*Source:\s*(?P<body>.+?)\*\s*$", s)
        if not m:
            return None
        body = m.group("body").strip()
        out: dict[str, Any] = {"sources": [], "tags": [], "regions": [], "sectors": [],
                                "cve": None, "cvss": None, "vector": None,
                                "auth": None, "status": [], "evidence": [],
                                "closed_source": []}
        # Replace links with placeholders so we don't trip on `· Source:` text.
        links = list(_FOOTER_LINK_RE.finditer(body))
        ph_map: dict[str, str] = {}
        body_clean = body
        for i, lm in enumerate(links):
            ph = f"\x00LINK{i}\x00"
            ph_map[ph] = f"{lm.group(1)}|||{lm.group(2)}"
            body_clean = body_clean.replace(lm.group(0), ph, 1)
        parts = [p.strip() for p in re.split(r"\s+·\s+", body_clean) if p.strip()]
        if not parts:
            return None
        first = parts[0]
        m_link = re.search(r"\x00LINK\d+\x00", first)
        if m_link:
            label, url = ph_map[m_link.group(0)].split("|||", 1)
            out["sources"].append({"label": label, "url": url})
        for p in parts[1:]:
            kv = re.match(r"^([A-Za-z][A-Za-z -]*?):\s*(.*)$", p)
            if not kv:
                continue
            k = kv.group(1).strip().lower().replace(" ", "_")
            v = kv.group(2).strip()
            for ph, val in ph_map.items():
                if ph in v:
                    lab, url = val.split("|||", 1)
                    v = v.replace(ph, f"[{lab}]({url})")
            if k in ("additional_source", "additional_sources"):
                lm2 = re.match(r"^\[([^\]]+)\]\(([^)]+)\)$", v)
                if lm2:
                    out["sources"].append({"label": lm2.group(1), "url": lm2.group(2)})
            elif k == "tags":
                out["tags"] = [t.strip() for t in v.split(",") if t.strip()]
            elif k == "region":
                out["regions"] = [t.strip() for t in v.split(",") if t.strip()]
            elif k in ("sector", "sectors"):
                out["sectors"] = [t.strip() for t in v.split(",") if t.strip()]
            elif k == "cve":
                out["cve"] = v.strip()
            elif k == "cvss":
                out["cvss"] = v.strip()
            elif k == "vector":
                out["vector"] = v.strip()
            elif k == "auth":
                out["auth"] = v.strip()
            elif k == "status":
                out["status"] = [t.strip() for t in v.split(",") if t.strip()]
            elif k == "evidence":
                # v2.58 — match the build-side Evidence parser.
                quote_re = re.compile(r'["“]([^"”]+?)["”]\s*(?:\(\s*(?P<attr>[^)]+?)\s*\))?')
                recs: list[dict[str, str]] = []
                for qm in quote_re.finditer(v):
                    qtext = qm.group(1).strip()
                    qattr = (qm.group("attr") or "").strip()
                    if qtext:
                        recs.append({"quote": qtext, "attribution": qattr})
                out["evidence"] = recs
            elif k in ("closed-source", "closed_source"):
                # v2.66 — mirror of site/build.py parse_closed_source_field.
                cs_recs: list[dict[str, str]] = []
                for cm in re.finditer(r'["“]([^"”]+?)["”]\s*\(([^)]*)\)', v):
                    rec = {"title": cm.group(1).strip(), "provider": "", "date": "",
                           "tlp": "", "ref": "", "raw": cm.group(0)}
                    for i, part in enumerate(x.strip() for x in cm.group(2).split(",")):
                        if not part:
                            continue
                        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", part):
                            rec["date"] = part
                        elif part.upper().startswith("TLP:"):
                            rec["tlp"] = part[4:].strip().upper()
                        elif part.lower().startswith("ref:"):
                            rec["ref"] = part[4:].strip()
                        elif i == 0 or not rec["provider"]:
                            rec["provider"] = part
                    cs_recs.append(rec)
                out["closed_source"] = cs_recs
        return out

    def parse_taxonomy(path: Path) -> dict[str, set[str]]:
        if not path.exists():
            return {}
        out: dict[str, set[str]] = {}
        cur: str | None = None
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.rstrip()
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            m = re.match(r"^([a-z_][a-z0-9_]*)\s*:\s*$", line)
            if m:
                cur = m.group(1); out[cur] = set(); continue
            m = re.match(r"^\s+-\s+(.+?)\s*$", line)
            if m and cur is not None:
                out[cur].add(m.group(1).strip().strip('"').strip("'"))
        return out

    def validate_footer(footer: dict[str, Any], taxonomy: dict[str, set[str]]) -> list[str]:
        errs: list[str] = []
        themes = taxonomy.get("themes", set()) | taxonomy.get("nexus", set())
        sectors = taxonomy.get("sectors", set())
        regions = taxonomy.get("regions", set())
        cve_vec = taxonomy.get("cve_vectors", set())
        cve_auth_v = taxonomy.get("cve_auth", set())
        cve_status_v = taxonomy.get("cve_status", set())
        for t in footer.get("tags", []):
            if t and t not in themes and t not in sectors:
                errs.append(f"unknown tag: {t}")
        for r in footer.get("regions", []):
            if r and r not in regions:
                errs.append(f"unknown region: {r}")
        if footer.get("vector") and footer["vector"] not in cve_vec:
            errs.append(f"unknown CVE vector: {footer['vector']}")
        if footer.get("auth") and footer["auth"] not in cve_auth_v:
            errs.append(f"unknown CVE auth: {footer['auth']}")
        for s in footer.get("status", []):
            if s and s not in cve_status_v:
                errs.append(f"unknown CVE status: {s}")
        return errs


# --- Brief decomposition --------------------------------------------------

# Headings: `## § 4 — Trending Vulnerabilities`, `## 4. Trending Vulnerabilities`,
# `## Trending Vulnerabilities` are all valid. We capture the title and assign
# a canonical section key so checks don't depend on the agent's numbering.
H2_RE = re.compile(r"^##\s+(?:§?\s*\d+\s*[.—-]\s+)?(?P<title>.+?)\s*$")
H3_RE = re.compile(r"^###\s+(?P<title>.+?)\s*$")
H4_RE = re.compile(r"^####\s+(?P<title>.+?)\s*$")
INLINE_LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}")

# Map heading-title keywords (lower-cased) → canonical section key. Mirrors
# site/build.py `_SECTION_KEYWORDS` so the script and the renderer agree on
# what each heading means.
_SECTION_KEYWORDS: list[tuple[str, str]] = [
    # Daily-prompt sections.
    ("tl;dr", "tldr"),
    ("immediate action", "immediate-actions"),
    ("active threats", "active-threats"),
    ("active threat", "active-threats"),
    ("trending vulnerabilities", "trending-vulnerabilities"),
    # Weekly research/threat-actor section — must precede the bare "research"
    # key below so a weekly "Research findings & threat-actor developments"
    # heading maps to weekly-research, not the daily `research` slug.
    ("threat-actor", "weekly-research"),
    ("research findings", "weekly-research"),
    ("research & threat", "weekly-research"),
    ("research and threat", "weekly-research"),
    ("research", "research"),
    ("notable incidents", "active-threats"),  # legacy daily
    ("switzerland, europe", "active-threats"),  # legacy daily
    ("updates to prior coverage", "updates"),
    ("updates on previously", "updates"),
    ("deep dive", "deep-dive"),
    ("action items", "action-items"),
    ("verification notes", "verification-notes"),
    ("verification & coverage", "verification-notes"),
    # Weekly-prompt sections (the daily/weekly distinction comes from the
    # brief filename — YYYY-MM-DD.md vs YYYY-Www.md). The keys mirror
    # site/taxonomy.yaml's `sections` list.
    ("week at a glance", "weekly-glance"),
    ("highest-impact events", "weekly-top-stories"),
    ("highest impact events", "weekly-top-stories"),
    ("top stories", "weekly-top-stories"),
    ("multi-day", "weekly-multi-day"),
    ("vulnerability roll-up", "weekly-vuln-rollup"),
    ("sector & victim", "weekly-sector-patterns"),
    ("sector and victim", "weekly-sector-patterns"),
    ("incidents & disclosures recap", "weekly-incidents-recap"),
    ("annual / periodic", "weekly-annual-reports"),
    ("annual /", "weekly-annual-reports"),
    ("annual ", "weekly-annual-reports"),
    ("long-running campaigns", "weekly-long-running"),
    ("policy & regulatory", "weekly-policy"),
    ("policy and regulatory", "weekly-policy"),
    ("looking ahead", "weekly-looking-ahead"),
]


def section_key_for(title: str) -> str:
    t = title.strip().lower()
    for kw, key in _SECTION_KEYWORDS:
        if kw in t:
            return key
    return "other"


def split_sections(text: str) -> list[dict[str, Any]]:
    """Returns an ordered list of sections, each:
        {title, key, ord, lines, items}

    where `key` is the canonical section key (`active-threats`, `trending-
    vulnerabilities`, etc.) and `items` is a list of H3/H4 blocks with
    {heading, body, footer_line, footer (parsed)}.

    Returns a list (not a dict) so callers can iterate without depending on
    the agent's chosen § numbering scheme — § 0–8 vs § 1–9 vs unnumbered all
    work.
    """
    sections: list[dict[str, Any]] = []
    cur: dict[str, Any] | None = None
    cur_lines: list[str] = []
    for line in text.splitlines():
        m2 = H2_RE.match(line)
        if m2:
            if cur is not None:
                cur["lines"] = cur_lines
                sections.append(cur)
            cur = {"title": m2.group("title"), "key": section_key_for(m2.group("title")),
                   "ord": len(sections), "lines": [], "items": []}
            cur_lines = []
            continue
        cur_lines.append(line)
    if cur is not None:
        cur["lines"] = cur_lines
        sections.append(cur)

    # Extract H3 + H4 items per section. H4 (subordinate detail blocks) often
    # also carry footers in upstream briefs.
    for sec in sections:
        items: list[dict[str, Any]] = []
        cur_item: dict[str, Any] | None = None
        for line in sec["lines"]:
            m = H3_RE.match(line) or H4_RE.match(line)
            if m:
                if cur_item is not None:
                    items.append(cur_item)
                cur_item = {"heading": m.group("title"), "level": 3 if line.startswith("### ") else 4, "body": []}
                continue
            if cur_item is not None:
                cur_item["body"].append(line)
        if cur_item is not None:
            items.append(cur_item)

        # Identify each item's footer. Walk from the end skipping blanks and
        # Markdown thematic-break separators (`---`, `***`, `___`). Return
        # the first line that parses as a footer; if we hit substantive
        # content (a paragraph, list, table row) before finding one, the
        # item has no footer.
        SEPARATOR_RE = re.compile(r"^\s*([-*_])\1{2,}\s*$")
        for it in items:
            footer_line: str | None = None
            footer_idx = -1
            for i in range(len(it["body"]) - 1, -1, -1):
                ln = it["body"][i].rstrip()
                if not ln.strip():
                    continue
                if SEPARATOR_RE.match(ln):
                    continue
                stripped = re.sub(r"^>\s+", "", ln).strip()
                parsed = parse_footer_line(stripped)
                if parsed is not None:
                    footer_line = stripped
                    footer_idx = i
                break
            it["footer_line"] = footer_line
            it["footer_idx"] = footer_idx
            it["footer"] = parse_footer_line(footer_line) if footer_line else None
        sec["items"] = items

    return sections


def sections_by_key(sections: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    """Group sections by canonical key — multiple sections can in principle
    share a key (e.g. legacy briefs split CH/EU into its own H2)."""
    out: dict[str, list[dict[str, Any]]] = {}
    for sec in sections:
        out.setdefault(sec["key"], []).append(sec)
    return out


# --- Individual checks ----------------------------------------------------

STATE_FILES = [
    STATE_DIR / "covered_items.json",
    STATE_DIR / "cves_seen.json",
    STATE_DIR / "deep_dive_history.json",
    STATE_DIR / "run_log.json",
    SOURCES_DIR / "sources.json",
]


def check_state_json_valid() -> dict[str, Any]:
    """Every state file we expect to find must parse as JSON. Returns a dict
    of {filename: parsed_or_None}."""
    parsed: dict[str, Any] = {}
    for p in STATE_FILES:
        rel = p.relative_to(ROOT)
        if not p.exists():
            # `deep_dive_history.json` and `run_log.json` are the only ones the
            # agent may legitimately create on first ever run. After that they
            # must exist.
            if p.name in ("deep_dive_history.json", "run_log.json"):
                warn("json-parse", f"{rel} not present (first-run-allowed)")
                parsed[p.name] = None
                continue
            fail("json-parse", f"{rel} missing")
            parsed[p.name] = None
            continue
        try:
            parsed[p.name] = json.loads(p.read_text(encoding="utf-8"))
            ok("json-parse", str(rel))
        except json.JSONDecodeError as e:
            fail("json-parse", f"{rel}: {e}")
            parsed[p.name] = None
    return parsed


def check_taxonomy_loadable() -> dict[str, set[str]]:
    if not TAXONOMY.exists():
        fail("taxonomy", f"{TAXONOMY.relative_to(ROOT)} missing")
        return {}
    tax = parse_taxonomy(TAXONOMY)
    if not tax:
        fail("taxonomy", "no entries parsed")
        return {}
    expected_keys = {"themes", "sectors", "regions", "cve_vectors", "cve_auth", "cve_status"}
    missing = expected_keys - set(tax.keys())
    if missing:
        fail("taxonomy", f"missing keys: {sorted(missing)}")
    else:
        ok("taxonomy", f"{sum(len(v) for v in tax.values())} terms across {len(tax)} keys")
    return tax


def check_cve_sync(brief_text: str, cves_seen: dict[str, Any] | None) -> set[str]:
    """Every CVE referenced in the brief must appear in cves_seen.json."""
    brief_cves = set(CVE_RE.findall(brief_text))
    if not brief_cves:
        ok("cve-sync", "no CVEs in brief")
        return set()
    if not cves_seen:
        fail("cve-sync", "cves_seen.json unavailable for comparison")
        return brief_cves
    seen_ids = {c["id"] for c in (cves_seen.get("cves") or []) if isinstance(c, dict)}
    missing = sorted(brief_cves - seen_ids)
    if missing:
        fail("cve-sync", f"missing from cves_seen.json: {missing}")
    else:
        ok("cve-sync", f"all {len(brief_cves)} CVEs in brief are in cves_seen.json")
    return brief_cves


REQUIRED_SECTION_KEYS = ("active-threats", "trending-vulnerabilities", "research")
FOOTERED_SECTION_KEYS = (
    "immediate-actions", "active-threats", "trending-vulnerabilities",
    "research", "updates", "deep-dive", "action-items",
)

# Weekly-brief equivalents — the weekly does not have the daily's three core
# sections (active-threats / trending-vulnerabilities / research) but has its
# own required scaffolding.
WEEKLY_REQUIRED_SECTION_KEYS = (
    "weekly-top-stories", "weekly-multi-day", "weekly-vuln-rollup",
    "weekly-incidents-recap",
)
WEEKLY_FOOTERED_SECTION_KEYS = (
    "weekly-top-stories", "weekly-multi-day", "weekly-vuln-rollup",
    "weekly-sector-patterns", "weekly-incidents-recap", "weekly-research",
    "weekly-annual-reports", "weekly-long-running", "weekly-policy",
)


def check_section_h3_coverage(sections: list[dict[str, Any]],
                                *, kind: str = "daily") -> None:
    """For daily briefs: active-threats / trending-vulnerabilities / research
    must each carry ≥1 H3 item. For weekly briefs: weekly-top-stories /
    weekly-multi-day / weekly-vuln-rollup / weekly-incidents-recap. An empty
    required section is editorial drift — a sub-agent failed and the gap was
    not surfaced as a stub.

    The weekly's "Highest-impact events" (weekly-top-stories) section is
    legitimately empty if no item from the week qualified as an "if you did
    nothing this would be ongoing" candidate — but this must be stated
    explicitly in the body."""
    keys = WEEKLY_REQUIRED_SECTION_KEYS if kind == "weekly" else REQUIRED_SECTION_KEYS
    by_key = sections_by_key(sections)
    for key in keys:
        secs = by_key.get(key, [])
        if not secs:
            fail("section-present", f"section '{key}' missing")
            continue
        total = sum(len(s["items"]) for s in secs)
        title = secs[0]["title"]
        if total == 0:
            body = "\n".join(secs[0]["lines"])
            if re.search(
                r"intentionally left empty|no qualifying items|no item met the bar|"
                r"no item .{0,40}continued to be operationally critical|"
                r"no inaction-=-incident",
                body, re.IGNORECASE,
            ):
                ok("section-h3", f"'{title}' ({key}): empty with explicit stub")
            else:
                warn("section-h3", f"'{title}' ({key}): no H3 items and no empty-stub marker")
        else:
            ok("section-h3", f"'{title}' ({key}): {total} item(s)")


def check_updates_citations(sections: list[dict[str, Any]]) -> None:
    """Every UPDATE block (whether under H3 or as a `> **UPDATE` blockquote) must
    have at least one inline [label](url) citation."""
    by_key = sections_by_key(sections)
    secs = by_key.get("updates", [])
    if not secs:
        warn("updates-citations", "no updates section found")
        return

    bad: list[str] = []
    update_count = 0
    has_no_updates_marker = False

    for sec in secs:
        # H3 items (UPDATE-style or other) → must carry inline links.
        for it in sec["items"]:
            update_count += 1
            body_text = "\n".join(it["body"])
            if not INLINE_LINK_RE.search(body_text):
                bad.append(f"H3 '{it['heading'][:60]}'")
        # Plus blockquoted `> **UPDATE` legacy form.
        block = "\n".join(sec["lines"])
        bq_updates = re.split(r"^>\s*\*\*UPDATE\b", block, flags=re.MULTILINE)
        for u in bq_updates[1:]:
            update_count += 1
            if not INLINE_LINK_RE.search(u):
                preamble = u.strip().splitlines()[0][:80] if u.strip() else "(empty)"
                bad.append(f"BQ '{preamble}'")
        if re.search(r"no updates this run|intentionally left empty|no qualifying updates",
                     block, re.IGNORECASE):
            has_no_updates_marker = True

    if bad:
        fail("updates-citations", f"UPDATE without inline citation: {bad}")
    elif update_count == 0:
        if has_no_updates_marker:
            ok("updates-citations", "updates: explicit no-updates marker present")
        else:
            warn("updates-citations", "updates section has no items and no no-updates marker")
    else:
        ok("updates-citations", f"updates: {update_count} block(s), all cited")


def _has_cve_in_heading(heading: str) -> bool:
    return bool(CVE_RE.search(heading))


def check_h3_footers(sections: list[dict[str, Any]], taxonomy: dict[str, set[str]],
                       *, kind: str = "daily") -> None:
    """Every H3 in immediate-actions / active-threats / trending-vulnerabilities /
    research / updates / deep-dive / action-items must end with a v2 metadata footer.
    Every footer must have Source + Tags + Region. CVE entries in
    trending-vulnerabilities additionally carry CVE + Vector + Auth + Status."""
    missing: list[str] = []
    no_source: list[str] = []
    no_tags: list[str] = []
    no_region: list[str] = []
    bad_taxonomy: list[str] = []
    cve_field_missing: list[str] = []

    keys = WEEKLY_FOOTERED_SECTION_KEYS if kind == "weekly" else FOOTERED_SECTION_KEYS
    by_key = sections_by_key(sections)
    for key in keys:
        for sec in by_key.get(key, []):
            for it in sec["items"]:
                if it.get("level") == 4:
                    # H4 sub-blocks are detail; the parent H3's footer is the
                    # canonical one. The build supports H4 footers too but
                    # presence is not required.
                    continue
                tag = f"'{sec['title'][:30]}' › '{it['heading'][:60]}'"
                if not it.get("footer"):
                    missing.append(tag)
                    continue
                footer = it["footer"]
                if not footer.get("sources") and not footer.get("closed_source"):
                    no_source.append(tag)
                if not footer.get("tags"):
                    no_tags.append(tag)
                if not footer.get("regions"):
                    no_region.append(tag)
                errs = validate_footer(footer, taxonomy)
                if errs:
                    bad_taxonomy.append(f"{tag}: {errs}")
                # CVE-typed items: every required CVE field must be present.
                # Daily: only the dedicated CVE section (trending-vulnerabilities).
                # Weekly: the equivalent (weekly-vuln-rollup).
                cve_section = (
                    "weekly-vuln-rollup" if kind == "weekly" else "trending-vulnerabilities"
                )
                if key == cve_section and _has_cve_in_heading(it["heading"]):
                    if not footer.get("cve"):
                        cve_field_missing.append(f"{tag}: missing CVE field")
                    if not footer.get("vector"):
                        cve_field_missing.append(f"{tag}: missing Vector")
                    if not footer.get("auth"):
                        cve_field_missing.append(f"{tag}: missing Auth")
                    if not footer.get("status"):
                        cve_field_missing.append(f"{tag}: missing Status")

    if missing:
        fail("footer-presence", f"items without v2 footer: {missing}")
    else:
        ok("footer-presence", "every H3 in footered sections has a v2 footer")
    if no_source:
        fail("footer-source", f"items without Source: {no_source}")
    else:
        ok("footer-source", "every footer has ≥1 Source link")
    if no_tags:
        fail("footer-tags", f"items without Tags: {no_tags}")
    else:
        ok("footer-tags", "every footer has Tags")
    if no_region:
        fail("footer-region", f"items without Region: {no_region}")
    else:
        ok("footer-region", "every footer has Region")
    if bad_taxonomy:
        fail("footer-taxonomy", f"non-taxonomy values: {bad_taxonomy}")
    else:
        ok("footer-taxonomy", "every footer value is in site/taxonomy.yaml")
    if cve_field_missing:
        fail("cve-footer-fields", f"CVE entries missing required fields: {cve_field_missing}")
    else:
        ok("cve-footer-fields", "CVE entries carry CVE/Vector/Auth/Status")


def check_multi_cve_footers(sections: list[dict[str, Any]], *, kind: str = "daily") -> None:
    """When a footer's CVE field is comma-separated (multi-CVE entry), CVSS
    must either be a single value (shared) or carry per-CVE breakdown using
    `/` or `(CVE-...)` syntax. Same for Vector / Auth — flag if multi-CVE and
    a single value claims to apply to all without explicit markup."""
    by_key = sections_by_key(sections)
    soft_warns: list[str] = []
    if kind == "weekly":
        target_keys = (
            "weekly-vuln-rollup", "weekly-top-stories", "weekly-multi-day",
            "weekly-incidents-recap",
        )
    else:
        target_keys = ("trending-vulnerabilities", "active-threats", "deep-dive", "immediate-actions")
    for key in target_keys:
        for sec in by_key.get(key, []):
            for it in sec["items"]:
                footer = it.get("footer")
                if not footer or not footer.get("cve"):
                    continue
                cve_field = footer["cve"]
                cves = [c.strip() for c in cve_field.split(",") if c.strip()]
                if len(cves) <= 1:
                    continue
                # Multi-CVE entry — check CVSS expression.
                cvss = (footer.get("cvss") or "").strip()
                if cvss and cvss.lower() != "n/a":
                    has_breakdown = ("/" in cvss) or ("(" in cvss)
                    if not has_breakdown:
                        soft_warns.append(
                            f"'{it['heading'][:60]}': {len(cves)} CVEs but single CVSS "
                            f"'{cvss}' — clarify per-CVE (e.g. '9.1 / 7.2' or '9.1 (CVE-…), 7.2 (CVE-…)')"
                        )
    if soft_warns:
        for w in soft_warns:
            warn("multi-cve-cvss", w)
    else:
        ok("multi-cve-cvss", "multi-CVE entries either single CVSS or carry per-CVE breakdown")


# Sources that are NEVER acceptable in a footer's `Source:` list (per v2.28
# editorial rule). NVD and MITRE per-CVE pages are derived data sheets — the
# vendor PSIRT advisory or research-lab post is the primary disclosing source
# and must be cited instead. NVD/MITRE still appear automatically as
# "External references" on every per-CVE page in the build.
BLOCKED_SOURCE_PATTERNS: list[tuple[str, str, str]] = [
    # (host fragment, path regex, reason)
    ("nvd.nist.gov", r"^/vuln/detail/CVE-",
     "NVD per-CVE pages are derived data sheets — cite the vendor advisory or research blog instead"),
    ("cve.mitre.org", r"^/cgi-bin/cvename\.cgi",
     "MITRE per-CVE pages are derived data sheets — cite the vendor advisory or research blog instead"),
    ("cve.org", r"^/CVERecord",
     "cve.org per-CVE pages are derived data sheets — cite the vendor advisory or research blog instead"),
]

# Generic landing / category / index pages — never an acceptable Source.
# A "Source" must be a specific article / advisory / blog post / regulator
# filing. Generic landings rot, get reorganised, and don't pin the claim.
BLOCKED_LANDING_PATTERNS: list[tuple[str, str, str]] = [
    ("heise.de", r"^/?$", "Heise homepage is not a source — link the specific article URL"),
    ("heise.de", r"^/news/?$", "Heise news landing is not a source — link the specific article URL"),
    ("heise.de", r"^/security/?$", "Heise Security category is not a source — link the specific article URL"),
    ("nos.nl", r"^/artikel/?$", "NOS article namespace landing is not a source — link the specific article URL"),
    ("nos.nl", r"^/?$", "NOS homepage is not a source — link the specific article URL"),
    ("bleepingcomputer.com", r"^/?$", "BleepingComputer homepage is not a source"),
    ("bleepingcomputer.com", r"^/news/?$", "BleepingComputer news landing is not a source"),
    ("therecord.media", r"^/?$", "The Record homepage is not a source"),
    ("securelist.com", r"^/?$", "Securelist homepage is not a source"),
    ("krebsonsecurity.com", r"^/?$", "Krebs on Security homepage is not a source"),
    ("thehackernews.com", r"^/?$", "The Hacker News homepage is not a source"),
    ("cisa.gov", r"^/news-events/?$", "CISA news-events landing is not a source — link the specific advisory"),
    ("cisa.gov", r"^/known-exploited-vulnerabilities-catalog/?$",
     "CISA KEV catalog root is not a source — link the per-CVE advisory or vendor PSIRT"),
    ("cert.ssi.gouv.fr", r"^/avis/?$", "CERT-FR advisories index is not a source — link the specific avis ID"),
    ("cert.ssi.gouv.fr", r"^/actualite/?$", "CERT-FR actualité index is not a source — link the specific actualité"),
    ("cert.europa.eu", r"^/publications/?$", "CERT-EU publications index is not a source"),
    ("ncsc.admin.ch", r"^/?$", "NCSC.ch homepage is not a source — link the specific advisory"),
    ("ncsc.admin.ch", r"^/ncsc/[a-z]{2}/home(\.html)?/?$",
     "NCSC.ch home page is not a source — link the specific advisory detail page"),
    ("dragos.com", r"^/year-in-review/?$",
     "Dragos year-in-review landing is not a source — link the specific article or PDF"),
    ("abw.gov.pl", r"^/pl/cyberbezpieczenstwo/?$",
     "ABW cybersecurity category landing is not a source — link the specific advisory"),
    ("surf.nl", r"^/?$", "SURF homepage is not a source"),
    ("ico.org.uk", r"^/?$", "UK ICO homepage is not a source"),
]


def _host_path(url: str) -> tuple[str, str]:
    """Return (lowercased host, path-or-'/') for a URL. Tolerates malformed
    input by returning empty strings.

    SPA hash-router carve-out: when the actual URL path is empty/root and
    the fragment looks like a route (starts with `/`), treat the fragment
    as the meaningful path. NCSC-CH's Cyber Security Hub is the canonical
    case — `tools/fetch_source.py` synthesises citation URLs of the form
    `https://security-hub.ncsc.admin.ch/#/posts/12551` because that is the
    public, human-readable post page; the JSON-only `/api/posts/.../details`
    endpoint is the fetch URL, not the citation. Without this carve-out the
    homepage regex `^/?$` for `ncsc.admin.ch` flags every Hub citation."""
    try:
        from urllib.parse import urlsplit
        u = urlsplit(url)
        path = u.path or "/"
        if path in ("", "/") and u.fragment.startswith("/"):
            path = u.fragment
        return u.netloc.lower(), path
    except Exception:
        return "", ""


def check_blocked_source_patterns(sections: list[dict[str, Any]],
                                    *, kind: str = "daily") -> None:
    """Hard FAIL when any footer's `Source:` list contains a URL matching a
    known-bad pattern: NVD/MITRE/cve.org per-CVE pages (always derived,
    never the disclosing party) or generic landing / category / index URLs
    that point at navigation, not content."""
    blocked: list[str] = []
    if kind == "weekly":
        target_keys = WEEKLY_FOOTERED_SECTION_KEYS
    else:
        target_keys = (
            "active-threats", "trending-vulnerabilities", "research",
            "deep-dive", "updates", "immediate-actions", "action-items",
        )
    for sec in sections:
        if sec["key"] not in target_keys:
            continue
        for it in sec["items"]:
            footer = it.get("footer") or {}
            for src in footer.get("sources") or []:
                url = src.get("url", "")
                host, path = _host_path(url)
                matched = False
                for h_frag, p_re, reason in BLOCKED_SOURCE_PATTERNS:
                    if h_frag in host and re.search(p_re, path):
                        blocked.append(f"'{it['heading'][:60]}' cites {url} — {reason}")
                        matched = True
                        break
                if matched:
                    continue
                for h_frag, p_re, reason in BLOCKED_LANDING_PATTERNS:
                    if h_frag in host and re.search(p_re, path):
                        blocked.append(f"'{it['heading'][:60]}' cites {url} — {reason}")
                        break
    if blocked:
        for b in blocked:
            fail("blocked-source", b)
    else:
        ok("blocked-source", "no Source URL matches a known-bad pattern (NVD / landing / index)")


def check_primary_source_quality(sections: list[dict[str, Any]],
                                   *, kind: str = "daily") -> None:
    """Soft-warn when an item's first source is a national CERT/NCSC. The
    editorial rule (v2.28) is: prefer vendor advisories / blogs / research-lab
    posts as primary. CERTs belong as `Additional source:` unless the item
    has no other reachable primary. (NVD/MITRE/cve.org per-CVE pages are
    handled by `blocked-source` above as a hard FAIL.)"""
    CERT_HOSTS = (
        "cert.ssi.gouv.fr", "cisa.gov", "ncsc.admin.ch", "ncsc.ch", "govcert.ch",
        "ncsc.gov.uk", "ncsc.nl", "bsi.bund.de", "cert.europa.eu", "enisa.europa.eu",
        "csirt.gov.it", "agid.gov.it", "cert.at", "cert.pl", "ccn-cert.cni.es",
    )
    if kind == "weekly":
        target_keys = (
            "weekly-top-stories", "weekly-multi-day", "weekly-vuln-rollup",
            "weekly-research", "weekly-annual-reports", "weekly-long-running",
        )
    else:
        target_keys = ("active-threats", "trending-vulnerabilities", "research", "deep-dive")
    soft: list[str] = []
    for sec in sections:
        if sec["key"] not in target_keys:
            continue
        for it in sec["items"]:
            footer = it.get("footer") or {}
            sources = footer.get("sources") or []
            if not sources:
                continue
            primary_url = (sources[0].get("url") or "").lower()
            host = primary_url.split("//", 1)[-1].split("/", 1)[0]
            if any(h in host for h in CERT_HOSTS) and len(sources) == 1:
                soft.append(
                    f"'{it['heading'][:60]}': only source is CERT/NCSC ({host}) — "
                    "look for the original vendor advisory or research blog"
                )
    if soft:
        for w in soft:
            warn("primary-source-quality", w)
    else:
        ok("primary-source-quality", "no item leans on CERT/NCSC as sole primary source")


def _load_url_liveness_ledger() -> dict[str, str]:
    """v2.47 URL-liveness cache. Sub-agents append to `work/<run-id>/url-liveness.tsv`
    a tab-separated `<url>\\t<status>\\t<fetched_at>` line for every Source URL
    they successfully fetched in-run. We sweep every `work/*/url-liveness.tsv`
    (most recent wins on duplicate URLs) and return `{url: status}` for any
    entry whose status starts with `2` (i.e. 2xx). The live HEAD/GET check
    skips URLs in this dict — the sub-agent has already proved them live, so
    re-fetching them only generates SSL-cert / anti-bot 403 noise on URLs the
    agent has already verified live.

    The cache is conservative: it only short-circuits on positive (2xx)
    cached entries. Cached non-2xx outcomes do NOT short-circuit; the live
    check runs and decides for itself. This keeps the gate strictly stronger
    than (or equal to) the no-cache version.
    """
    cached: dict[str, tuple[str, str]] = {}  # url -> (status, fetched_at)
    work_dir = ROOT / "work"
    if not work_dir.exists():
        return {}
    for ledger in sorted(work_dir.glob("*/url-liveness.tsv")):
        try:
            for raw in ledger.read_text(encoding="utf-8", errors="replace").splitlines():
                parts = raw.rstrip().split("\t")
                if len(parts) < 2:
                    continue
                url, status = parts[0].strip(), parts[1].strip()
                fetched_at = parts[2].strip() if len(parts) > 2 else ""
                if not url or not status:
                    continue
                # Most-recent wins (sorted glob order is filesystem order; we
                # also key on fetched_at if present).
                prev = cached.get(url)
                if prev is None or (fetched_at and fetched_at > prev[1]):
                    cached[url] = (status, fetched_at)
        except Exception:
            continue
    # Only honour 2xx cached statuses.
    return {u: st for u, (st, _) in cached.items() if st.startswith("2")}


# v2.47 — News-aggregator host allowlist for the "aggregator-only sourcing"
# warning. These are reputable news outlets per `sources.json`, but they
# aggregate primary research and should NOT be the only sources backing an
# item. An item whose Source field is ≥2 URLs all from this list meets the
# literal two-source bar but lacks any primary disclosure — flag it so § 7
# carries the reduced-confidence framing instead of silently accepting.
NEWS_AGGREGATOR_HOSTS: tuple[str, ...] = (
    "bleepingcomputer.com",
    "thehackernews.com",
    "feeds.feedburner.com",   # hackernews + akamai feedburner namespace
    "securityaffairs.com",
    "securityweek.com",
    "helpnetsecurity.com",
    "therecord.media",
    "cyberscoop.com",
    "darkreading.com",
    "infosecurity-magazine.com",
    "risky.biz",
    "news.risky.biz",
    "krebsonsecurity.com",
    "schneier.com",
    "techcrunch.com",
    "techzine.eu",
    "dutchnews.nl",
    "heise.de",        # news side; their advisory pages are different
    "inside-it.ch",
    "ictjournal.ch",
    "blick.ch",
    "ictjournal.fr",
    "lemondeinformatique.fr",
    "le-monde.fr",
    "lemonde.fr",
    "theguardian.com",
    "spiegel.de",
    "meduza.io",
    "piunikaweb.com",
    "cyberkendra.com",
    "malwarebytes.com",   # they also publish their own research; treat the
                           # "blog/news" half as aggregator and the
                           # "labs"/"threat-intel" half as primary — see the
                           # _is_primary_path carve-out below.
)


def _host_is_aggregator(host: str) -> bool:
    h = (host or "").lower()
    return any(h == a or h.endswith("." + a) for a in NEWS_AGGREGATOR_HOSTS)


def check_aggregator_only_sourcing(sections: list[dict[str, Any]],
                                     *, kind: str = "daily") -> None:
    """v2.47 (§ 2.4): an item whose Source field has ≥2 URLs all matching the
    news-aggregator allowlist meets the literal two-source bar but lacks any
    primary disclosure (vendor PSIRT advisory, research-lab post, regulator
    filing, victim statement). Flag it so § 7 carries the reduced-confidence
    framing instead of silently accepting. Items in § 4 Updates legitimately
    rely on news-aggregator sourcing for the *delta* part of an UPDATE, so
    they are excluded.
    """
    if kind == "weekly":
        target_keys = (
            "weekly-top-stories", "weekly-multi-day", "weekly-vuln-rollup",
            "weekly-incidents-recap", "weekly-research",
        )
    else:
        target_keys = ("active-threats", "trending-vulnerabilities", "research")
    flagged: list[str] = []
    for sec in sections:
        if sec["key"] not in target_keys:
            continue
        for it in sec["items"]:
            footer = it.get("footer") or {}
            sources = footer.get("sources") or []
            if len(sources) < 2:
                continue
            hosts = [_host_path(s.get("url", ""))[0] for s in sources]
            if all(_host_is_aggregator(h) for h in hosts if h):
                flagged.append(
                    f"'{it['heading'][:60]}' has {len(sources)} sources, all from "
                    f"news-aggregator hosts ({sorted(set(hosts))[:3]}). "
                    f"§ 7 should carry `reduced confidence — only aggregator sources` "
                    f"or the item should be re-pivoted to a vendor / research-lab / regulator primary."
                )
    if flagged:
        for w in flagged:
            warn("aggregator-only-sourcing", w)
    else:
        ok("aggregator-only-sourcing",
           "no item leans on news-aggregator hosts as its only sources")


def check_single_source_flag(sections: list[dict[str, Any]],
                               *, kind: str = "daily") -> None:
    """v2.47 (§ 2.5 mechanical complement to the verifier's F12): an item
    whose Source field has exactly 1 URL, where the host is NOT one of the
    national-CERT carve-out hosts, must carry the `[SINGLE-SOURCE]` marker
    (or the related `SINGLE-SOURCE-OTHER` / `SINGLE-SOURCE-NATIONAL-CERT`
    variant) in its heading. Without the marker the reader doesn't see the
    softer guarantee.

    The national-CERT carve-out hosts are the same set the editorial policy
    treats as primary disclosing parties for their own jurisdiction; they
    are single-source acceptable without the explicit reader-visible flag,
    though the verifier's F12 still asks for an explicit § 7 / § 10 line
    naming the carve-out.
    """
    NATIONAL_CERT_HOSTS = (
        "ncsc.admin.ch", "ncsc.ch", "govcert.ch",
        "cert.europa.eu", "enisa.europa.eu",
        "bsi.bund.de", "wid.cert-bund.de", "cert.ssi.gouv.fr",
        "ncsc.gov.uk", "ncsc.nl", "advisories.ncsc.nl",
        "cisa.gov", "www.cisa.gov",
        "csirt.gov.it", "agid.gov.it", "acn.gov.it",
        "cert.at", "govcert.gv.at", "cert.pl", "ccn-cert.cni.es",
        "jpcert.or.jp",
    )
    if kind == "weekly":
        target_keys = (
            "weekly-top-stories", "weekly-multi-day", "weekly-vuln-rollup",
            "weekly-research", "weekly-annual-reports", "weekly-long-running", "weekly-policy",
        )
    else:
        target_keys = ("active-threats", "trending-vulnerabilities", "research")
    flagged: list[str] = []
    for sec in sections:
        if sec["key"] not in target_keys:
            continue
        for it in sec["items"]:
            footer = it.get("footer") or {}
            sources = footer.get("sources") or []
            if len(sources) != 1:
                continue
            if footer.get("closed_source"):
                # v2.66 — a closed-source citation is HIGH-credibility
                # corroboration; one URL + one closed-source ref is not a
                # single-source item.
                continue
            host = _host_path(sources[0].get("url", ""))[0]
            heading = it.get("heading") or ""
            heading_has_flag = bool(re.search(r"\[SINGLE-SOURCE", heading, re.IGNORECASE))
            if heading_has_flag:
                continue
            if any(host == h or host.endswith("." + h) for h in NATIONAL_CERT_HOSTS):
                # National-CERT carve-out — single-source acceptable without
                # the explicit flag. The verifier's F12 still asks for a § 7
                # line naming the carve-out, but no script-side WARN here.
                continue
            flagged.append(
                f"'{it['heading'][:60]}' has exactly 1 Source ({host}) and the "
                f"heading lacks `[SINGLE-SOURCE]`. Add the flag to the heading and "
                f"name the source explicitly in § 7 (or carve-out applies if a national CERT)."
            )
    if flagged:
        for w in flagged:
            warn("single-source-flag", w)
    else:
        ok("single-source-flag",
           "every single-source item carries [SINGLE-SOURCE] in its heading or qualifies for the national-CERT carve-out")


_TLDR_DEADLINE_RE = re.compile(
    r"(?:CISA\s+)?KEV\s+deadline|remediation\s+deadline|federal\s+remediation|CISA\s+deadline",
    re.IGNORECASE,
)
_TLDR_EXPLOITATION_RE = re.compile(
    r"exploit(?:ed|ation|ing)|in[\s-]?the[\s-]?wild|\bITW\b|active(?:ly)?|"
    r"victim|impacted|exposed|targeting|breach",
    re.IGNORECASE,
)


def check_tldr_deadline_lead(sections: list[dict[str, Any]]) -> None:
    """v2.47 (§ 2.3) — PD-13 enforcement at the bullet level. A TL;DR bullet
    that leads with US-only KEV-deadline framing without naming the actual
    urgent driver (active exploitation, victim class, exposure magnitude,
    attack class) is the editorial regression PD-13 was added to prevent.

    Read literally: the *first ~120 characters* of every TL;DR bullet must
    name the operational driver, not the compliance deadline. Bullets that
    mention the KEV deadline elsewhere in their body are fine — the test is
    "what does the reader see in the lead 120 chars".
    """
    by_key = sections_by_key(sections)
    tldr_secs = by_key.get("tldr", [])
    if not tldr_secs:
        ok("tldr-deadline-lead", "no TL;DR section to check")
        return
    flagged: list[str] = []
    bullet_re = re.compile(r"^\s*[-*]\s+(?P<body>.+?)$", re.MULTILINE)
    for sec in tldr_secs:
        body = "\n".join(sec.get("lines", []))
        for m in bullet_re.finditer(body):
            bullet = m.group("body").strip()
            lead = bullet[:160]
            if not _TLDR_DEADLINE_RE.search(lead):
                continue
            if _TLDR_EXPLOITATION_RE.search(lead):
                continue
            preview = bullet[:90].replace("**", "")
            flagged.append(
                f"TL;DR bullet leads with KEV/remediation deadline framing "
                f"without naming exploitation / victim / exposure: {preview!r}. "
                f"PD-13: deadline is US-only compliance signal, not the urgent driver."
            )
    if flagged:
        for w in flagged:
            warn("tldr-deadline-lead", w)
    else:
        ok("tldr-deadline-lead",
           "no TL;DR bullet leads with deadline framing without exploitation context")


def check_source_urls_resolve(sections: list[dict[str, Any]],
                                *, skip: bool, timeout: float = 10.0) -> None:
    """Live HEAD/GET every Source URL in every footer; FAIL on 404. Catches
    fabricated-URL drift the v2.27 verifier was designed to find — duplicating
    it here so the operator gets a green/red answer locally without spawning
    a sub-agent. Use `--no-link-check` for offline runs.

    v2.47 URL-liveness cache: any URL the sub-agents successfully fetched
    in-run (recorded in `work/<run-id>/url-liveness.tsv` as a 2xx entry) is
    trusted and skipped — the sub-agent has already proved it live."""
    if skip:
        warn("source-urls", "skipped (--no-link-check)")
        return

    import ipaddress
    import urllib.request
    import urllib.error
    import socket
    import ssl

    # Defence in depth: even though check_brief.py is run by the operator
    # (not from the public web), refuse redirects that would land us on a
    # loopback / link-local / private / cloud-metadata host. Otherwise an
    # allowlisted publisher whose CMS is compromised — or a typo in a
    # brief — could pivot the operator's local URL-liveness check into a
    # request against `http://127.0.0.1:8080/` or
    # `http://169.254.169.254/latest/meta-data/`. Liveness must not
    # become an SSRF foothold.
    def _ip_is_blocked_local(addr: str) -> bool:
        try:
            ip = ipaddress.ip_address(addr)
        except ValueError:
            return True
        return bool(
            ip.is_loopback or ip.is_link_local or ip.is_private
            or ip.is_multicast or ip.is_reserved or ip.is_unspecified
        )

    def _host_is_blocked(host: str) -> bool:
        try:
            infos = socket.getaddrinfo(host, None, socket.AF_UNSPEC, socket.SOCK_STREAM)
        except socket.gaierror:
            return True
        return any(_ip_is_blocked_local(s[4][0]) for s in infos)

    class _SafeRedirectHandler(urllib.request.HTTPRedirectHandler):
        max_redirections = 5

        def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[override]
            from urllib.parse import urlparse as _up
            parsed = _up(newurl)
            scheme = (parsed.scheme or "").lower()
            host = (parsed.hostname or "").lower()
            if scheme not in ("http", "https"):
                raise urllib.error.HTTPError(
                    newurl, code, f"redirect refused: scheme {scheme!r}",
                    headers, fp,
                )
            if not host or _host_is_blocked(host):
                raise urllib.error.HTTPError(
                    newurl, code, f"redirect refused: host {host!r} resolves to disallowed address",
                    headers, fp,
                )
            return super().redirect_request(req, fp, code, msg, headers, newurl)

    _safe_opener = urllib.request.build_opener(_SafeRedirectHandler())

    urls: dict[str, list[str]] = {}
    for sec in sections:
        for it in sec["items"]:
            footer = it.get("footer") or {}
            for src in footer.get("sources") or []:
                u = src.get("url", "")
                if u.startswith("http://") or u.startswith("https://"):
                    urls.setdefault(u, []).append(f"'{sec['title'][:30]}' › '{it['heading'][:50]}'")

    if not urls:
        ok("source-urls", "no http(s) source URLs to check")
        return

    # v2.47 URL-liveness cache — sub-agents that successfully fetched a URL
    # in-run record it as 2xx in `work/<run-id>/url-liveness.tsv`. Trust those
    # entries and skip the live HEAD/GET; the agent has already proved them
    # live. This kills SSL-cert / anti-bot 403 noise on URLs the agent has
    # already verified live, without weakening the gate (cached non-2xx
    # outcomes do NOT short-circuit, and uncached URLs still go through the
    # full live check).
    cached_2xx = _load_url_liveness_ledger()
    cache_hits = [u for u in urls.keys() if u in cached_2xx]
    if cache_hits:
        for u in cache_hits:
            urls.pop(u, None)
        ok(
            "source-urls-cache",
            f"trusted {len(cache_hits)} URL(s) from sub-agent in-run url-liveness ledger "
            f"(work/<run-id>/url-liveness.tsv); live re-fetch skipped for those URLs",
        )

    if not urls:
        ok("source-urls", f"all source URLs trusted via in-run liveness ledger "
           f"({len(cache_hits)} cached, 0 re-fetched)")
        return

    # Pre-flight: probe a single high-availability host. If the SSL handshake
    # fails because the local Python has no CA trust store (a common macOS
    # footgun where `python3` is the system one without certifi), we emit a
    # single WARN and skip the rest — running 50 of these only to produce 50
    # identical CERTIFICATE_VERIFY_FAILED lines is noise. CI (Linux + bundled
    # certifi) is unaffected.
    try:
        probe = urllib.request.Request(
            "https://www.google.com/",
            headers={"User-Agent": "check_brief.py probe"},
            method="HEAD",
        )
        _safe_opener.open(probe, timeout=5).close()
    except Exception as e:
        msg = str(e)
        if "CERTIFICATE_VERIFY_FAILED" in msg or "SSL" in msg:
            warn("source-urls",
                 "local Python has no CA bundle (SSL: CERTIFICATE_VERIFY_FAILED on https probe) — "
                 "skipping live URL check; CI runs unaffected. Pass --no-link-check to silence locally.")
            return
        # Any other pre-flight failure: keep going — the per-URL loop will
        # surface real errors.

    # Hosts that reliably 403 the default UA but are otherwise alive — we
    # treat 403/429 from these as PASS, since the agent is expected to use
    # tools/fetch_source.py for them. The unmitigated-403 problem is checked
    # separately via run_log.json.
    KNOWN_UA_BLOCKED = (
        "www.cisa.gov", "cisa.gov", "ncsc.admin.ch", "www.ncsc.admin.ch",
        "talosintelligence.com", "blog.talosintelligence.com",
        "csirt-italia.it", "www.csirt-italia.it",
        "prodaft.com", "www.prodaft.com",
        "inside-it.ch", "www.inside-it.ch",
        "ico.org.uk", "www.ico.org.uk",
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
    }

    def _check_one(url: str) -> tuple[int | None, str]:
        # Pre-flight: refuse if the initial host already resolves to a
        # blocked address. The redirect handler covers the post-301 path.
        try:
            from urllib.parse import urlparse as _up
            parsed = _up(url)
            host0 = (parsed.hostname or "").lower()
            if not host0 or _host_is_blocked(host0):
                return None, "host blocked (loopback/link-local/private)"
        except Exception:
            pass
        for method in ("HEAD", "GET"):
            try:
                req = urllib.request.Request(url, headers=headers, method=method)
                with _safe_opener.open(req, timeout=timeout) as resp:
                    # Drain a small bounded chunk so the connection closes
                    # cleanly; we only want the status code.
                    try:
                        resp.read(64 * 1024)
                    except Exception:
                        pass
                    return resp.status, ""
            except urllib.error.HTTPError as e:
                if e.code in (405, 501) and method == "HEAD":
                    continue  # retry with GET
                return e.code, ""
            except (urllib.error.URLError, socket.timeout, ConnectionError, Exception) as e:
                return None, str(e)[:80]
        return None, "exhausted methods"

    bad_404: list[tuple[str, list[str]]] = []
    other_errors: list[tuple[str, int | None, str, list[str]]] = []
    ua_blocked: list[str] = []
    checked = 0
    print(f"  ... checking {len(urls)} URL(s) ...")
    for url in sorted(urls.keys()):
        checked += 1
        host, _ = _host_path(url)
        status, err = _check_one(url)
        if status == 200:
            continue
        if status in (403, 429) and host in KNOWN_UA_BLOCKED:
            ua_blocked.append(url)
            continue
        if status == 404:
            bad_404.append((url, urls[url]))
        else:
            other_errors.append((url, status, err, urls[url]))

    # 404s remain per-URL FAILs — these are the actionable editorial
    # signal the brief-composition LLM should act on (rewrite citation
    # or drop the item).
    if bad_404:
        for u, cited_in in bad_404:
            preview = cited_in[:2]
            more = f" + {len(cited_in) - 2} more" if len(cited_in) > 2 else ""
            fail("source-urls",
                 f"{u} returns 404 — cited in: {preview}{more}")
    # Everything else (403/429 from non-allowlisted hosts, 5xx, network
    # errors, timeouts) is transient — the host's WAF filters this
    # check container's UA, the upstream is having a moment, the proxy
    # stalled. The agent already fetched these at run time via
    # WebFetch / fetch_source.py, so the LLM has no actionable leverage
    # here. Aggregate into one summary WARN with a status breakdown +
    # a few examples — operators still see the pattern (e.g. "this
    # host always 403s us") but the brief-composition LLM doesn't drown
    # in 30 identical warnings of the same shape.
    if other_errors:
        by_status: dict[str, list[tuple[str, list[str]]]] = {}
        for u, status, err, cited_in in other_errors:
            label = f"HTTP {status}" if status else "network/SSL"
            by_status.setdefault(label, []).append((u, cited_in))
        breakdown = ", ".join(
            f"{len(v)}× {k}"
            for k, v in sorted(by_status.items(), key=lambda kv: (-len(kv[1]), kv[0]))
        )
        first_few = [u for u, _, _, _ in other_errors[:3]]
        warn("source-urls",
             f"{len(other_errors)} URL(s) returned non-200 from this check "
             f"({breakdown}) — transient: UA filter / 5xx / timeout / proxy. "
             f"The agent already fetched these at run time. "
             f"Sample: {', '.join(first_few)}")
    if ua_blocked:
        ok("source-urls",
           f"{len(ua_blocked)} URL(s) on UA-blocked hosts (CISA/NCSC.ch/etc.) — handled by fetch_source.py check")
    if not bad_404 and not other_errors:
        ok("source-urls", f"all {checked} source URL(s) returned HTTP 200 (or UA-blocked allowlisted)")


# v2.48 — full bridge-allowlist source-id matchers. Source ids in
# sources.json are stable strings; here we list the substrings that
# identify a bridge-allowlisted source (case-insensitive substring match
# against the lowered source id).
BRIDGE_REQUIRED_SOURCE_IDS = frozenset({
    "cisa-kev", "cisa-advisories", "cisa-news", "cisa-directives",
    "ncsc-ch-security-hub", "ncsc-ch-incidents", "ncsc-ch-focus",
    "enisa-euvd",
    "bsi-de", "wid.cert-bund.de", "cert-bund",
    "advisories-ncsc-nl", "ncsc-nl",
    "anssi-fr", "cert.ssi.gouv.fr",
    "cert-eu", "cert-pl", "ncsc-uk",
    "databreaches-net", "ico-uk",
    "nccgroup", "ncc-research",
    "dragos", "sygnia", "ccn-cert-es", "ccn-cert",
    "talos", "prodaft", "inside-it-ch", "acn", "csirt-acn-it",
})

# v2.48 — required keys in the rich `fetch_failures` entry shape.
RICH_FAILURE_REQUIRED_KEYS = (
    "id", "url_tried", "fetch_method", "status_code",
    "error_class", "attempted_methods", "mitigation_applied",
    "covered_anyway",
)


def _failure_id_is_bridge_allowlisted(sid: str) -> bool:
    """True iff this source id should be fetched via the bridge."""
    s = (sid or "").lower()
    return any(needle in s for needle in BRIDGE_REQUIRED_SOURCE_IDS)


def check_fetch_source_for_known_403(brief_text: str,
                                      run_log: dict[str, Any] | None,
                                      brief_date: str) -> None:
    """CISA + NCSC.ch + every bridge-allowlisted host (v2.48 expanded) must
    be fetched via `tools/fetch_source.py`. Phase 5.5 surfaces three signals:

    1. **Bridge-required FAIL** (`fetch-failure-bridge-required`) — a
       fetch_failures entry whose `id` matches a bridge-allowlisted source
       AND whose `attempted_methods` does NOT contain a `bridge:*` method.
       The agent went direct on a host where the bridge was the right
       first move.
    2. **Legacy 403 FAIL** — preserved for back-compat with v2.47-shape
       entries (`{id, code: "403"}` without `attempted_methods`): a 403/429
       on a known-403 source id is treated as unhandled.
    3. **Rich-shape WARN** (`fetch-failure-detail`) — entry missing one of
       the v2.48 required keys → flag for upgrade. Legacy entries pass via
       a back-compat path; new entries that drop a required key fail this.
    """
    KNOWN_403_HOSTS = ("www.cisa.gov", "cisa.gov", "ncsc.admin.ch", "ncsc.ch")

    cited_hosts: set[str] = set()
    for m in INLINE_LINK_RE.finditer(brief_text):
        url = m.group(1)
        host = url.split("//", 1)[-1].split("/", 1)[0]
        for k in KNOWN_403_HOSTS:
            if k in host:
                cited_hosts.add(k)
                break

    if not run_log:
        if cited_hosts:
            warn("fetch-source-403", f"brief cites {sorted(cited_hosts)}; cannot verify fetch_source.py was used (run_log unavailable)")
        else:
            ok("fetch-source-403", "no CISA/NCSC.ch URLs cited; nothing to verify")
        return

    today_runs = [r for r in (run_log.get("runs") or []) if r.get("date") == brief_date]
    if not today_runs:
        warn("fetch-source-403", f"no run_log entry for {brief_date}; cannot verify")
        return
    rec = today_runs[-1]
    failures = rec.get("fetch_failures") or []

    # ── 1. Legacy 403 unhandled-on-known-host check ──────────────────────
    # Back-compat: legacy v2.43–v2.47 entries used `{id, code|status, note:
    # "handled via bridge fetch_source.py; ..."}`. The `note` substring is
    # the legacy mitigation marker. v2.48 entries use the rich shape with
    # `attempted_methods` instead — we accept either as proof the bridge
    # was used.
    LEGACY_HANDLED_RE = re.compile(
        r"handled\s+via|bridge|fetch[_-]?source\.py|mitigated|recovered",
        re.IGNORECASE,
    )
    unhandled_legacy: list[str] = []
    for f in failures:
        if not isinstance(f, dict):
            continue
        sid = (f.get("id") or "").lower()
        code = str(f.get("code") or f.get("status_code") or f.get("status") or "")
        attempted = [m for m in (f.get("attempted_methods") or []) if isinstance(m, str)]
        note = f.get("note") or ""
        # Treat as handled if (a) attempted_methods carries a bridge:* call,
        # OR (b) the legacy `note` explicitly says it was handled / bridged.
        bridge_handled = (
            any(m.startswith("bridge:") for m in attempted)
            or bool(LEGACY_HANDLED_RE.search(note))
        )
        if (
            code in ("403", "429")
            and not bridge_handled
            and any(k.replace(".", "-") in sid or k.split(".")[0] in sid for k in KNOWN_403_HOSTS)
        ):
            unhandled_legacy.append(f"{sid} ({code})")
    if unhandled_legacy:
        fail("fetch-source-403",
             f"403/429 on known-403 hosts (CISA/NCSC.ch) not mitigated via tools/fetch_source.py: {unhandled_legacy}")
    elif cited_hosts:
        ok("fetch-source-403", "CISA/NCSC.ch cited and no unhandled 403/429 in run_log")
    else:
        ok("fetch-source-403", "no CISA/NCSC.ch URLs cited; nothing to verify")

    # ── 2. v2.48 — bridge-required FAIL across the FULL allowlist ────────
    bridge_skipped: list[str] = []
    for f in failures:
        if not isinstance(f, dict):
            continue
        sid = (f.get("id") or "").lower()
        if not _failure_id_is_bridge_allowlisted(sid):
            continue
        attempted = [m for m in (f.get("attempted_methods") or []) if isinstance(m, str)]
        if not attempted:
            # Legacy entry — treated by the legacy path above; don't double-flag.
            continue
        if not any(m.startswith("bridge:") for m in attempted):
            bridge_skipped.append(
                f"{sid} (attempted_methods={attempted}, no bridge:* present)"
            )
    if bridge_skipped:
        fail(
            "fetch-failure-bridge-required",
            f"v2.48: bridge subcommand not attempted for bridge-allowlisted source(s): {bridge_skipped}. "
            "These hosts must be fetched via `python3 tools/fetch_source.py …` first; see "
            "prompts/daily-cti-brief.md § Reinforced rules ¶2 for the per-source subcommand table.",
        )
    elif failures:
        ok("fetch-failure-bridge-required",
           f"every fetch_failures entry on the bridge allowlist used a bridge:* method")

    # ── 3. v2.48 — rich-shape detail WARN ────────────────────────────────
    thin_entries: list[str] = []
    for f in failures:
        if not isinstance(f, dict):
            thin_entries.append("non-dict entry")
            continue
        # Legacy {id, code} entries are back-compat — flag once per run.
        is_legacy = "code" in f and "url_tried" not in f and "attempted_methods" not in f
        if is_legacy:
            thin_entries.append(f"legacy {{id, code}} for {f.get('id', '?')}")
            continue
        missing = [k for k in RICH_FAILURE_REQUIRED_KEYS if k not in f]
        if missing:
            thin_entries.append(f"{f.get('id', '?')} missing {missing}")
    if thin_entries:
        warn(
            "fetch-failure-detail",
            f"v2.48: {len(thin_entries)} fetch_failures entr{'y' if len(thin_entries) == 1 else 'ies'} "
            f"missing rich-shape detail (sample: {thin_entries[:3]}). "
            "The Ops dashboard renders these as yellow 'needs-detail' rows. "
            "Sub-agents must include url_tried, fetch_method, status_code, error_class, attempted_methods, "
            "mitigation_applied, covered_anyway — see .claude/agents/cti-research.md § fetch_failures.",
        )
    elif failures:
        ok("fetch-failure-detail",
           f"all {len(failures)} fetch_failures entr{'y' if len(failures) == 1 else 'ies'} carry the v2.48 rich shape")


def check_covered_items_appearances(brief_date: str,
                                     sections: list[dict[str, Any]],
                                     covered: dict[str, Any] | None) -> None:
    """Heuristic signal: H3 count in core sections (active-threats / trending-
    vulns / research) should roughly match appearances for `brief_date`.
    Difference >1 → WARN (some H3s legitimately group multiple records)."""
    if not covered:
        warn("covered-items", "covered_items.json unavailable")
        return
    by_key = sections_by_key(sections)
    h3_count = sum(len(s["items"]) for k in REQUIRED_SECTION_KEYS for s in by_key.get(k, []))
    appearances = 0
    target_sections = {"active_threats", "trending_vulns", "research",
                       "active_breaking", "ch_eu", "gov_public"}
    for it in (covered.get("items") or []):
        for app in (it.get("appearances") or []):
            if app.get("date") == brief_date and app.get("section") in target_sections:
                appearances += 1
                break
    # Heuristic: flag only when coverage has SIGNIFICANTLY lagged (less
    # than 40% of H3 items got a covered_items.json appearance for
    # today). The legacy "diff > 1" rule fired on every well-formed
    # brief because not every H3 is meant to be a long-running tracked
    # item — § 4 Research items, § 6 Action Items, and synthetic Deep
    # Dives routinely don't carry topic-state records and shouldn't.
    # Today's gold-standard 2026-05-10 brief has 8 H3s and 4
    # appearances (50% coverage); raising the threshold lets that be
    # the new "good" baseline so the brief-composition LLM doesn't
    # waste an editorial cycle chasing a non-issue.
    if h3_count == 0:
        ok("covered-items", "no H3 in core sections (empty-day brief)")
    elif appearances < max(1, h3_count * 0.4):
        warn("covered-items",
             f"H3 in core sections = {h3_count}; appearances on {brief_date} = "
             f"{appearances} ({appearances / max(h3_count, 1):.0%} coverage; "
             f"expected ≥ 40%). state/covered_items.json may have lagged this run.")
    else:
        ok("covered-items",
           f"H3/appearances within tolerance ({h3_count} vs {appearances}; "
           f"{appearances / max(h3_count, 1):.0%} coverage)")


def check_run_log_for_today(brief_date: str, run_log: dict[str, Any] | None,
                              *, kind: str = "daily", iso_week: str | None = None) -> None:
    """`state/run_log.json` is the Ops dashboard's data source. A sparse record
    leaves the dashboard with `—` cells and hides source-rotation health.

    Required for today's run:
      - top-level `date`, `model`, `sub_agents`, `fetch_failures`,
        `items_published`, `deep_dive`, `verification_iterations`,
        `verification_residual_count`
      - per-sub-agent allocation block: `sources_attempted`, `sources_used`,
        `items_returned`, `returned`
    """
    if run_log is None:
        warn("run-log", "state/run_log.json missing (first run only — fail next run)")
        return
    runs = run_log.get("runs") or []

    # Pick this run: prefer kind-specific match (weekly entries should carry
    # iso_week == this week + kind == "weekly"); fall back to date match for
    # legacy records.
    matching = []
    for r in runs:
        if kind == "weekly":
            if r.get("kind") == "weekly" and (
                (iso_week and r.get("iso_week") == iso_week)
                or r.get("date") == brief_date
            ):
                matching.append(r)
        else:
            if r.get("kind", "daily") == "daily" and r.get("date") == brief_date:
                matching.append(r)
    if not matching:
        # Fall back to any run record matching the date (helps during the
        # daily/weekly schema transition).
        matching = [r for r in runs if r.get("date") == brief_date]
    if not matching:
        ident = iso_week if kind == "weekly" else brief_date
        fail("run-log",
             f"no {kind} entry for {ident} in run_log.json — Ops dashboard will not show this run")
        return
    rec = matching[-1]

    # Required top-level keys. Daily and weekly share most of the schema but
    # diverge on a couple of fields (`deep_dive` is daily-only; `iso_week` /
    # `kind` are weekly-only). v2.47: `run_id` added — deterministic id used
    # for idempotent retry (Phase 5 refuses to append a duplicate).
    if kind == "weekly":
        required = {
            "run_id", "date", "iso_week", "kind", "model", "sub_agents", "fetch_failures",
            "items_published", "verification_iterations", "verification_residual_count",
        }
    else:
        required = {
            "run_id", "date", "model", "sub_agents", "fetch_failures", "items_published",
            "deep_dive", "verification_iterations", "verification_residual_count",
        }
    missing = required - set(rec.keys())
    # `run_id` is the only newly-required field as of v2.47 — older records
    # from v2.46 and earlier still parse, but the WARN flags them so the
    # operator notices the schema gap. The fields list above keeps `run_id`
    # in the required set so any *new* record without it FAILs.
    if missing == {"run_id"}:
        warn("run-log-fields",
             "run_id missing on this run record (v2.47+ requirement; older records grandfathered)")
    elif missing:
        fail("run-log-fields", f"record missing keys: {sorted(missing)}")
    else:
        ok("run-log-fields", "run_log record has every required top-level key")

    # v2.47 idempotent retry: no two runs[] entries may share the same run_id.
    # The deterministic id (computed in Phase 0 step 0 as
    # `<date|iso-week>-<sha8 of brief_path|started_minute>`) makes a true
    # retry within the same minute compute the same id; Phase 5 must update
    # the existing record in place rather than append a duplicate.
    rid = rec.get("run_id")
    if isinstance(rid, str) and rid:
        dupes = [r for r in runs if r.get("run_id") == rid]
        if len(dupes) > 1:
            fail(
                "run-log-run-id-dup",
                f"run_id {rid!r} appears {len(dupes)}× in runs[] — Phase 5 should "
                "update in place when run_id already exists, not append a duplicate",
            )
        else:
            ok("run-log-run-id-dup", f"run_id {rid} is unique in runs[] (idempotent retry honoured)")

    # Sub-agent allocation block.
    sa = rec.get("sub_agents") or {}
    incomplete: list[str] = []
    empty_alloc: list[str] = []
    sub_agent_keys = ("W1", "W2") if kind == "weekly" else ("S1", "S2", "S3", "S4")
    for k in sub_agent_keys:
        a = sa.get(k)
        if not a or not isinstance(a, dict):
            incomplete.append(f"{k}: missing")
            continue
        if "returned" not in a:
            incomplete.append(f"{k}: missing 'returned' flag")
        if a.get("returned", True):
            for f in ("sources_attempted", "sources_used", "items_returned"):
                if f not in a:
                    incomplete.append(f"{k}: missing '{f}'")
            if isinstance(a.get("sources_attempted"), list) and not a["sources_attempted"]:
                empty_alloc.append(f"{k}: sources_attempted is empty (Ops dashboard renders 0/0)")
    # v2.66 — the conditional closed-source intake agent (S5 daily / W3
    # weekly) only runs when intel/<date>/ had files; validate its record
    # shape when present, never require it.
    intake_key = "W3" if kind == "weekly" else "S5"
    a = sa.get(intake_key)
    if isinstance(a, dict):
        for f in ("returned", "items_returned"):
            if f not in a:
                incomplete.append(f"{intake_key}: missing '{f}' (intake record present but partial)")
    if incomplete:
        fail("run-log-subagents", f"sub-agent records incomplete: {incomplete}")
    else:
        n = len(sub_agent_keys)
        extra = f" + {intake_key} intake" if isinstance(a, dict) else ""
        ok("run-log-subagents", f"all {n} sub-agent allocation record(s) present ({', '.join(sub_agent_keys)}){extra}")
    if empty_alloc:
        warn("run-log-subagents", f"sub-agents with empty source allocation: {empty_alloc}")

    # fetch_failures must be a list (empty allowed).
    if not isinstance(rec.get("fetch_failures"), list):
        fail("run-log-failures", "fetch_failures must be a list (use [] when none)")
    else:
        ok("run-log-failures", f"fetch_failures recorded ({len(rec['fetch_failures'])})")

    if rec.get("items_published") in (None, ""):
        fail("run-log-items", "items_published not recorded")
    else:
        ok("run-log-items", f"items_published = {rec.get('items_published')}")

    # Verification sub-agent loop fields (Phase 5.7 daily / Phase 4.7 weekly).
    vi = rec.get("verification_iterations")
    vr = rec.get("verification_residual_count")
    if not isinstance(vi, int) or vi < 1:
        fail("run-log-verification", f"verification_iterations should be ≥ 1 (got {vi!r})")
    elif vi > 5:
        warn("run-log-verification", f"verification_iterations = {vi} exceeds the v2.46 cap of 5")
    else:
        ok("run-log-verification", f"verification_iterations = {vi}")

    # v2.47 corrected residual semantics: `verification_residual_count` is
    # `(final_iter.truth + final_iter.editorial)` when the FINAL iteration's
    # verdict is `NEEDS_FIXES` (cap reached without CLEAN); `0` when the
    # final verdict is `CLEAN`. F11 advisory excluded — F11 alone never
    # blocks CLEAN. Counting it 0 on a NEEDS_FIXES final iteration silently
    # absorbs an editorial-quality drift the gatekeeper was supposed to
    # catch — the cap-breach signal below catches that drift.
    expected_vr = None
    final_iter = None
    vblock_for_vr = rec.get("verification") if isinstance(rec.get("verification"), dict) else None
    if vblock_for_vr and isinstance(vblock_for_vr.get("iterations"), list) and vblock_for_vr["iterations"]:
        final_iter = vblock_for_vr["iterations"][-1]
        if isinstance(final_iter, dict):
            verdict = (final_iter.get("verdict") or "").strip().upper()
            t = final_iter.get("truth") if isinstance(final_iter.get("truth"), int) else 0
            e = final_iter.get("editorial") if isinstance(final_iter.get("editorial"), int) else 0
            if verdict == "CLEAN":
                expected_vr = 0
            elif verdict == "NEEDS_FIXES":
                expected_vr = t + e
    if not isinstance(vr, int) or vr < 0:
        fail("run-log-verification-residual",
             f"verification_residual_count should be ≥ 0 (got {vr!r})")
    elif expected_vr is not None and vr != expected_vr:
        # v2.47: cross-check against the per-iteration block. The legacy
        # "every NEEDS_FIXES final iteration silently records 0" pattern
        # this catches.
        fail(
            "run-log-verification-residual",
            f"verification_residual_count = {vr} but final-iteration "
            f"verdict + truth/editorial implies {expected_vr} "
            f"(v2.47 derived = (truth + editorial) of the final iteration "
            f"if NEEDS_FIXES, else 0; F11 advisory excluded)",
        )
    elif vr > 0:
        warn("run-log-verification-residual",
             f"verification_residual_count = {vr} — published with unresolved findings")
    else:
        ok("run-log-verification-residual", f"verification_residual_count = 0 (clean publish)")

    # v2.47 cap-breach yellow signal — distinct from the residual-count
    # check above. A NEEDS_FIXES final iteration is a regression even when
    # the residual count is correctly recorded. Surfaces to the Ops
    # dashboard so the operator notices the pattern.
    if final_iter and isinstance(final_iter, dict):
        verdict = (final_iter.get("verdict") or "").strip().upper()
        if verdict == "NEEDS_FIXES":
            t = final_iter.get("truth") if isinstance(final_iter.get("truth"), int) else 0
            e = final_iter.get("editorial") if isinstance(final_iter.get("editorial"), int) else 0
            a = final_iter.get("advisory") if isinstance(final_iter.get("advisory"), int) else 0
            warn(
                "cap-breach",
                f"verifier final iteration ({final_iter.get('n', vi)}) returned NEEDS_FIXES "
                f"(truth={t}, editorial={e}, advisory={a}) — brief published at the cap-breach "
                f"safety valve, not on a CLEAN verdict. Surface to the Ops dashboard's 7-day "
                f"rolling cap-breach count.",
            )
            # v2.48 — cap-breach iteration MUST carry per-finding detail
            # so the operator can debug WHAT was unresolved. Legacy
            # iterations (v2.43-v2.47) didn't record this; warn so the
            # next run captures it. Today's run with no findings[] on
            # a NEEDS_FIXES iteration is the highest-priority drift to
            # fix because the dashboard otherwise shows truth=4
            # editorial=3 advisory=3 with zero context.
            findings = final_iter.get("findings")
            if not isinstance(findings, list) or not findings:
                warn(
                    "verification-finding-detail",
                    f"v2.48: cap-breach iteration {final_iter.get('n', vi)} has empty / missing "
                    "findings[] — the Ops dashboard cannot render WHAT the verifier flagged. "
                    "The verifier's `### Findings summary (machine-readable)` YAML block must "
                    "be parsed into iteration.findings[] (one record per F-finding). See "
                    ".claude/agents/cti-verification.md § Findings summary.",
                )
            else:
                ok(
                    "verification-finding-detail",
                    f"cap-breach iteration {final_iter.get('n', vi)} carries {len(findings)} per-finding record(s)",
                )

    # v2.58 — commit-gate when verifier is still in flight. The premature-commit
    # failure mode from the 2026-05-15 run was: the routine spawned the
    # verifier, a stop-hook fired before the verifier returned, the main
    # agent set `verification.final_verdict: "pending"` (or PENDING), then
    # committed. F1 (the dangerous Datadog inversion) lived on `main` for
    # several minutes before the corrective commit landed. This check
    # refuses the commit until the verifier outcome is recorded.
    pending_states = {"pending", "in-flight", "in_flight", "running", "unknown", ""}
    fv = (vblock_for_vr or {}).get("final_verdict") if isinstance(vblock_for_vr, dict) else None
    if isinstance(fv, str) and fv.strip().lower() in pending_states:
        fail(
            "verification-final-verdict-set",
            f"verification.final_verdict = {fv!r} — the verifier has not finished. "
            f"Wait for the verification sub-agent to return and record its verdict "
            f"(CLEAN | NEEDS_FIXES) before committing. If the verifier hard-failed "
            f"or timed out past 30 min, record `final_verdict: \"timeout\"` with a "
            f"§ 7 / § 10 Verification Notes line — never commit on a verdict the "
            f"gatekeeper has not actually rendered.",
        )
    elif isinstance(fv, str) and fv.strip():
        ok("verification-final-verdict-set", f"verification.final_verdict = {fv!r}")
    elif vblock_for_vr and isinstance(vblock_for_vr.get("iterations"), list) and vblock_for_vr["iterations"]:
        # Block exists with iterations but no final_verdict field — accept on
        # the basis of the final iteration's verdict, since older v2.43–v2.52
        # records may not carry the top-level field.
        ok("verification-final-verdict-set",
           "verification.final_verdict not explicitly set; final iteration's verdict is authoritative")

    # Per-agent model surface (v2.43+). Main agent records its own model;
    # every sub-agent that returned should record the model it self-identified
    # with. WARN (not FAIL) on missing fields so older runs from v2.42 still
    # pass validation.
    main_model = rec.get("model")
    main_model_id = rec.get("model_id")
    if isinstance(main_model, str) and main_model and main_model.lower() != "unknown":
        ok("run-log-model", f"main-agent model = {main_model}"
           + (f" ({main_model_id})" if main_model_id else ""))
    elif main_model:
        warn("run-log-model", f"main-agent model = {main_model!r} (consider naming the actual model)")
    else:
        warn("run-log-model", "main-agent model not recorded")

    missing_subagent_models: list[str] = []
    for k in sub_agent_keys:
        a = sa.get(k)
        if not isinstance(a, dict) or a.get("returned") is False:
            continue
        m = a.get("model")
        if not isinstance(m, str) or not m.strip():
            missing_subagent_models.append(k)
    if missing_subagent_models:
        warn("run-log-subagent-models",
             f"sub-agents missing self-reported model: {missing_subagent_models} "
             "(v2.43+ — set to 'unknown' if the **Model:** line was absent)")
    else:
        ok("run-log-subagent-models", "every returning sub-agent has a recorded model")

    # Per-iteration verification block (v2.43+).
    vblock = rec.get("verification")
    if isinstance(vblock, dict) and isinstance(vblock.get("iterations"), list) and vblock["iterations"]:
        per_iter = vblock["iterations"]
        # Sanity-check shape — each iteration carries n, model, verdict.
        broken = [i for i, it in enumerate(per_iter, start=1)
                  if not isinstance(it, dict) or "model" not in it or "verdict" not in it]
        if broken:
            warn("run-log-verification-iterations",
                 f"per-iteration records incomplete at positions {broken}")
        else:
            ok("run-log-verification-iterations",
               f"verification.iterations[] populated ({len(per_iter)} record(s))")
        # Iterations count should match the legacy scalar where both are present.
        if isinstance(vi, int) and vi != len(per_iter):
            warn("run-log-verification-iterations",
                 f"verification_iterations ({vi}) != len(verification.iterations) ({len(per_iter)})")
    else:
        warn("run-log-verification-iterations",
             "verification.iterations[] not populated (v2.43+ — record per-iteration model + verdict)")

    # Wall-clock timing — drives the duration sparkline on the dashboard.
    started = rec.get("started")
    completed = rec.get("completed")
    dur = rec.get("duration_seconds")
    if isinstance(dur, (int, float)) and dur > 0:
        ok("run-log-duration", f"duration_seconds = {int(dur)}")
    else:
        warn("run-log-duration",
             "duration_seconds missing or 0 — Ops dashboard duration sparkline will be empty")
    if started and completed:
        ok("run-log-timestamps", "started + completed timestamps recorded")
    else:
        warn("run-log-timestamps", "started/completed timestamps not both recorded")


def check_essential_coverage(brief_date: str, run_log: dict[str, Any] | None,
                              sources_data: dict[str, Any] | None,
                              *, kind: str = "daily") -> None:
    """v2.67 — every active `tier: essential` source (national CERTs / NCSC /
    CISA / ENISA-class authorities) must be *attempted* on every daily run.
    Reads the union of today's `sub_agents[*].sources_attempted`. WARN, not
    FAIL — the brief must publish regardless; the gap is disclosed and the
    next run's rotation self-heals. Weekly runs are exempt (the guarantee is
    a daily property; W1/W2 slices are horizon-scoped)."""
    if kind == "weekly":
        ok("essential-coverage", "n/a for weekly runs (daily-coverage guarantee)")
        return
    if not sources_data or not run_log:
        warn("essential-coverage", "sources.json or run_log.json unavailable")
        return
    essential = {s["id"] for s in sources_data.get("sources", [])
                 if s.get("tier") == "essential" and s.get("status") == "active"}
    if not essential:
        warn("essential-coverage", "no active `tier: essential` sources defined in sources.json")
        return
    recs = [r for r in (run_log.get("runs") or [])
            if r.get("date") == brief_date and r.get("kind", "daily") == "daily"]
    if not recs:
        warn("essential-coverage", f"no daily run_log record for {brief_date}")
        return
    attempted: set[str] = set()
    for a in (recs[-1].get("sub_agents") or {}).values():
        if isinstance(a, dict):
            attempted |= set(a.get("sources_attempted") or [])
    missed = sorted(essential - attempted)
    if missed:
        warn("essential-coverage",
             f"{len(missed)} essential source(s) not attempted this run — a daily run "
             f"must query every national-CERT/NCSC/CISA/ENISA-class source: {missed} "
             "(disclose in § 7; the allocation step must include ALL essential sources)")
    else:
        ok("essential-coverage",
           f"all {len(essential)} essential sources attempted this run")


def check_sources_touched_today(brief_date: str, sources_data: dict[str, Any] | None) -> None:
    """At least one source must have `last_successful_fetch == brief_date`.
    Otherwise the Ops dashboard's stale-sources panel cannot move and the
    rotation invariant has clearly been skipped."""
    if not sources_data:
        warn("sources-touched", "sources.json unavailable")
        return
    src_list = sources_data.get("sources") or []
    if not src_list:
        warn("sources-touched", "sources.json contains no sources")
        return
    fetched_today = [s.get("id") for s in src_list if s.get("last_successful_fetch") == brief_date]
    if not fetched_today:
        fail("sources-touched",
             f"no source has last_successful_fetch == {brief_date} — "
             "Phase 5 source-bookkeeping was not done")
    else:
        ok("sources-touched",
           f"{len(fetched_today)} source(s) fetched today (sample: {fetched_today[:5]})")


def check_sources_schema(sources_data: dict[str, Any] | None) -> None:
    """Validate the shape of every entry in `sources/sources.json`.

    The autonomous source-add path (Phase 5 § sources/sources.json — autonomous
    lifecycle) has previously produced shape drift that built fine *until* the
    static-site deploy ran and `site/build.py` crashed on the malformed entry.
    The 2026-05-15 regression: `"category": "research"` (string) where every
    other entry has `["research"]` (list) — `build.py` iterates `category` and
    treats each character as a category tag, then the gh-pages deploy fails.

    Catch it at the gate. Strict on fields whose drift breaks the build or
    contract; advisory (WARN) on fields that the build tolerates but that
    indicate the autonomous prompt under-specified the shape.
    """
    if not sources_data:
        warn("sources-schema", "sources.json unavailable (json-parse failed)")
        return
    if not isinstance(sources_data, dict):
        fail("sources-schema", f"top-level must be object, got {type(sources_data).__name__}")
        return

    # Top-level controlled vocabularies — sources reference these by key.
    valid_categories: set[str] = set((sources_data.get("categories") or {}).keys())
    valid_statuses: set[str] = set((sources_data.get("statuses") or {}).keys())
    valid_reliability: set[str] = set((sources_data.get("reliability_tiers") or {}).keys())
    valid_fetch_methods: set[str] = set((sources_data.get("fetch_methods") or {}).keys())

    missing_top = [
        k for k in ("schema_version", "categories", "reliability_tiers",
                    "statuses", "fetch_methods", "sources")
        if k not in sources_data
    ]
    if missing_top:
        fail("sources-schema", f"missing top-level key(s): {missing_top}")
        return  # later checks would all cascade

    if not valid_categories:
        fail("sources-schema", "top-level `categories` is empty — cannot validate per-source `category`")
        return

    src_list = sources_data.get("sources")
    if not isinstance(src_list, list):
        fail("sources-schema", f"`sources` must be a list, got {type(src_list).__name__}")
        return

    errors: list[str] = []
    warnings_: list[str] = []
    seen_ids: dict[str, int] = {}

    for idx, s in enumerate(src_list):
        # Identify the entry in error messages — prefer `id`, fall back to
        # array index.
        if not isinstance(s, dict):
            errors.append(f"#{idx}: entry must be object, got {type(s).__name__}")
            continue
        sid = s.get("id")
        tag = f"#{idx}" if not isinstance(sid, str) or not sid else sid

        # --- id (required, unique, non-empty string) ---
        if not isinstance(sid, str) or not sid:
            errors.append(f"{tag}: missing or non-string `id`")
        else:
            if sid in seen_ids:
                errors.append(f"{tag}: duplicate `id` (also at index {seen_ids[sid]})")
            else:
                seen_ids[sid] = idx

        # --- url (required, http/https string) ---
        url = s.get("url")
        if not isinstance(url, str) or not url:
            errors.append(f"{tag}: missing or non-string `url`")
        elif not (url.startswith("http://") or url.startswith("https://")):
            errors.append(f"{tag}: `url` must start with http:// or https:// (got {url!r})")

        # --- category (required, list[str], every value in vocabulary) ---
        cat = s.get("category")
        if cat is None:
            errors.append(f"{tag}: missing `category` (required — must be a list of strings)")
        elif not isinstance(cat, list):
            # ★ The specific drift the 2026-05-15 deploy regression hit.
            errors.append(
                f"{tag}: `category` must be a list (got {type(cat).__name__}={cat!r}) — "
                f"e.g. [\"research\"] not \"research\""
            )
        elif not cat:
            errors.append(f"{tag}: `category` must contain at least one value")
        else:
            for c in cat:
                if not isinstance(c, str):
                    errors.append(f"{tag}: `category` entry must be string (got {type(c).__name__}={c!r})")
                elif c not in valid_categories:
                    errors.append(
                        f"{tag}: unknown category {c!r} — must be one of "
                        f"{sorted(valid_categories)}"
                    )

        # --- status (required, in vocabulary) ---
        status = s.get("status")
        if not isinstance(status, str) or not status:
            errors.append(f"{tag}: missing or non-string `status`")
        elif status not in valid_statuses:
            errors.append(
                f"{tag}: unknown status {status!r} — must be one of {sorted(valid_statuses)}"
            )

        # --- publisher (required string) ---
        # The build renders `s.get("publisher") or s["id"]`. If a source uses
        # `name` instead (one historical drift), the build falls back to the
        # raw id and the source becomes harder to recognise. Require
        # `publisher`; surface `name`-only entries explicitly.
        publisher = s.get("publisher")
        if not isinstance(publisher, str) or not publisher:
            if isinstance(s.get("name"), str) and s.get("name"):
                errors.append(
                    f"{tag}: uses `name` instead of `publisher` — rename the field "
                    "(the build only reads `publisher`, falling back to `id`)"
                )
            else:
                errors.append(f"{tag}: missing or non-string `publisher`")

        # --- notes (required string, append-only audit trail) ---
        notes = s.get("notes")
        if not isinstance(notes, str):
            errors.append(f"{tag}: missing or non-string `notes`")

        # --- Status-dependent requirements ---
        # `active` and `demoted` sources participate in rotation and bookkeeping;
        # the autonomous prompt promises specific counters and metadata for them.
        # `candidate` sources are newly proposed and may legitimately lack some
        # of these on first append — warn instead of fail so the one-new-
        # candidate-per-run path stays smooth, but flag for next-run promotion.
        is_in_rotation = status in {"active", "demoted"}
        is_candidate = status == "candidate"

        reliability = s.get("reliability")
        if is_in_rotation:
            if not isinstance(reliability, str) or not reliability:
                errors.append(f"{tag}: status={status!r} requires `reliability`")
            elif reliability not in valid_reliability:
                errors.append(
                    f"{tag}: unknown reliability {reliability!r} — must be one of "
                    f"{sorted(valid_reliability)}"
                )
        elif reliability is not None:
            # Candidates may carry a provisional reliability — validate the
            # vocabulary if present.
            if not isinstance(reliability, str) or reliability not in valid_reliability:
                errors.append(
                    f"{tag}: unknown reliability {reliability!r} — must be one of "
                    f"{sorted(valid_reliability)}"
                )

        # --- tier (v2.67 — required on in-rotation sources; drives the daily
        #     essential-coverage guarantee + staleness rotation) ---
        valid_tiers = set((sources_data.get("tiers") or {}).keys()) or {"essential", "standard"}
        tier = s.get("tier")
        if is_in_rotation:
            if not isinstance(tier, str) or not tier:
                errors.append(f"{tag}: status={status!r} requires `tier` "
                              f"(one of {sorted(valid_tiers)})")
            elif tier not in valid_tiers:
                errors.append(f"{tag}: unknown tier {tier!r} — must be one of {sorted(valid_tiers)}")
        elif tier is not None and tier not in valid_tiers:
            errors.append(f"{tag}: unknown tier {tier!r} — must be one of {sorted(valid_tiers)}")

        fetch_method = s.get("fetch_method")
        if is_in_rotation:
            if not isinstance(fetch_method, str) or not fetch_method:
                errors.append(f"{tag}: status={status!r} requires `fetch_method`")
            elif fetch_method not in valid_fetch_methods:
                errors.append(
                    f"{tag}: unknown fetch_method {fetch_method!r} — must be one of "
                    f"{sorted(valid_fetch_methods)}"
                )
        elif fetch_method is not None:
            if not isinstance(fetch_method, str) or fetch_method not in valid_fetch_methods:
                errors.append(
                    f"{tag}: unknown fetch_method {fetch_method!r} — must be one of "
                    f"{sorted(valid_fetch_methods)}"
                )

        language = s.get("language")
        if is_in_rotation:
            if not isinstance(language, list) or not language:
                errors.append(f"{tag}: status={status!r} requires `language` as non-empty list[str]")
            else:
                for lang in language:
                    if not isinstance(lang, str) or not lang:
                        errors.append(f"{tag}: `language` entry must be non-empty string (got {lang!r})")
        elif language is not None and not isinstance(language, list):
            errors.append(f"{tag}: `language` must be a list (got {type(language).__name__})")

        cf = s.get("consecutive_failures")
        if cf is not None and not isinstance(cf, int):
            errors.append(f"{tag}: `consecutive_failures` must be int (got {type(cf).__name__}={cf!r})")

        lsf = s.get("last_successful_fetch")
        if lsf is not None and not (isinstance(lsf, str) and (lsf == "" or re.match(r"^\d{4}-\d{2}-\d{2}$", lsf))):
            errors.append(
                f"{tag}: `last_successful_fetch` must be YYYY-MM-DD or null (got {lsf!r})"
            )

        # --- Advisory: candidates ought to carry the same metadata so they
        # can be promoted without a second drift round. ---
        if is_candidate:
            missing_advisory = [
                k for k in ("publisher", "reliability", "language", "fetch_method")
                if not s.get(k)
            ]
            if missing_advisory:
                warnings_.append(
                    f"{tag}: candidate missing recommended field(s) {missing_advisory} — "
                    "fill these now so promotion to active doesn't need a follow-up edit"
                )

    if errors:
        # Surface up to 12 lines so the agent sees the full picture without
        # overwhelming the summary. Most schema drift cascades — fixing the
        # first error often clears later ones.
        head = errors[:12]
        more = f" (+{len(errors) - 12} more)" if len(errors) > 12 else ""
        fail("sources-schema",
             f"{len(errors)} schema error(s) in sources/sources.json{more}: "
             + "; ".join(head))
    else:
        ok("sources-schema",
           f"{len(src_list)} source(s) — shapes valid, vocab values in range")

    # Warnings flow through `warn()` so they appear in the standard summary.
    for w in warnings_:
        warn("sources-schema-advisory", w)


def check_test_build(skip: bool) -> None:
    """Run site/test_build.py (the build-side smoke tests). Failure here means
    the brief will not render correctly even if its own metadata is clean."""
    if skip:
        warn("test-build", "skipped (--no-build-tests)")
        return
    if not TEST_BUILD.exists():
        warn("test-build", f"{TEST_BUILD.relative_to(ROOT)} missing")
        return
    try:
        proc = subprocess.run(
            [sys.executable, str(TEST_BUILD)],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
            timeout=120,
        )
    except subprocess.TimeoutExpired:
        fail("test-build", "site/test_build.py timed out after 120s")
        return
    if proc.returncode == 0:
        ok("test-build", "site/test_build.py passed")
    else:
        tail = (proc.stdout or "").splitlines()[-20:] + (proc.stderr or "").splitlines()[-10:]
        fail("test-build", "site/test_build.py failed; tail:\n        " +
             "\n        ".join(tail))


def check_ai_notice(brief_text: str) -> None:
    """Hard invariant 1: every brief carries the AI-generated content notice.

    The v2.43 prompt also requires the notice to enumerate sub-agent models —
    we WARN (not FAIL) when the sub-agent enumeration is missing so older
    briefs from v2.42 and earlier still pass."""
    if "AI-generated content" in brief_text and "no human review" in brief_text:
        ok("ai-notice", "AI-generated content notice present")
    else:
        fail("ai-notice", "missing 'AI-generated content — no human review' notice")
        return

    # Sub-agent model surface (v2.43+). The blockquote should mention
    # "sub-agents" and the metadata line should carry "**Sub-agents:**".
    has_blockquote_subagents = bool(re.search(r"sub-agents?\s*\(", brief_text, re.IGNORECASE))
    has_metadata_subagents = "**Sub-agents:**" in brief_text
    if has_blockquote_subagents and has_metadata_subagents:
        ok("ai-notice-subagents", "sub-agent models enumerated in notice and Generated-by line")
    else:
        missing = []
        if not has_blockquote_subagents:
            missing.append("blockquote sub-agent enumeration")
        if not has_metadata_subagents:
            missing.append("**Sub-agents:** metadata field")
        warn("ai-notice-subagents",
             f"v2.43+ surface missing: {', '.join(missing)} (older briefs ok)")


def check_no_iocs(brief_text: str) -> None:
    """Hard invariant 4: no IOCs. Heuristic scan. The agent is still the line
    of defence — this catches the easy cases.

    Patterns checked:
      - SHA-256 / SHA-1 / MD5 hashes (32+ contiguous hex chars).
      - Routable IPv4 addresses (excluding RFC 5737 / 1918 / loopback /
        link-local / broadcast). **Skips version-string contexts** —
        product versions like `12.6.1.1` look like IPs but are not IOCs.
    """
    findings: list[str] = []

    # Hash patterns. 32-char MD5 false-positives are real (Git long SHAs are
    # 40, but mid-text 32-char hex strings can show up in vendor advisory
    # IDs); we still flag them, the agent confirms.
    sha256 = re.findall(r"\b[a-fA-F0-9]{64}\b", brief_text)
    sha1 = re.findall(r"(?<![a-fA-F0-9])[a-fA-F0-9]{40}(?![a-fA-F0-9])", brief_text)
    md5 = re.findall(r"(?<![a-fA-F0-9])[a-fA-F0-9]{32}(?![a-fA-F0-9])", brief_text)
    if sha256:
        findings.append(f"SHA-256 hash(es): {sha256[:3]}")
    if sha1:
        findings.append(f"SHA-1 hash(es): {sha1[:3]}")
    if md5:
        findings.append(f"MD5 hash(es): {md5[:3]}")

    # IPv4 — but skip version-string contexts. A "routable IP" surrounded by
    # words like "version", "branch", "patch", "fixed", "EPMM", or appearing
    # inside a `<` / `≥` / `>=` / `/` separator pattern is almost always a
    # version, not an indicator.
    ipv4_re = re.compile(
        r"\b(?:(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\b"
    )

    def _is_doc_or_private(ip: str) -> bool:
        a = [int(x) for x in ip.split(".")]
        if (a[0], a[1], a[2]) in ((192, 0, 2), (198, 51, 100), (203, 0, 113)):
            return True
        if a[0] in (0, 10, 127):
            return True
        if a[0] == 192 and a[1] == 168:
            return True
        if a[0] == 172 and 16 <= a[1] <= 31:
            return True
        if a[0] == 169 and a[1] == 254:
            return True
        if ip == "255.255.255.255":
            return True
        return False

    VERSION_CONTEXT_RE = re.compile(
        r"(?i)\b(version|versions?|patched|fixed|fix|firmware|build|release|"
        r"branch|prior\s+to|before|earlier\s+than|≥|>=|<=|≤|EPMM|EPMS|EPSS|patch)\b"
    )

    flagged: list[tuple[str, str]] = []
    for m in ipv4_re.finditer(brief_text):
        ip = m.group(0)
        if _is_doc_or_private(ip):
            continue
        # Look at the surrounding 80-char window for version-string cues.
        start = max(0, m.start() - 80)
        end = min(len(brief_text), m.end() + 80)
        window = brief_text[start:end]
        if VERSION_CONTEXT_RE.search(window):
            continue
        # Inside a Markdown table cell or paren list of versions ('| 12.6.1.1 |',
        # '< 12.6.1.1 / 12.7.0.1', etc.) — skip if the immediate neighbours are
        # other version-like dotted numbers.
        if re.search(r"[\d.]+\s*[/,]\s*$", brief_text[start:m.start()]) \
           or re.search(r"^\s*[/,]\s*[\d.]+", brief_text[m.end():end]):
            continue
        flagged.append((ip, window.strip()[:120]))
    if flagged:
        findings.append(f"routable IPv4 address(es): {[ip for ip, _ in flagged[:3]]}")

    if findings:
        fail("ioc-scan", "; ".join(findings) + " — confirm none are IOCs before publishing")
    else:
        ok("ioc-scan", "no obvious IOC patterns detected (version-string false positives skipped)")


# --- v2.57 Tier 2 pre-verifier mechanical checks --------------------------
#
# These four checks land in v2.57 to catch defect classes that previously
# burned verifier-iteration budget on mechanical issues. Each addresses a
# specific failure mode from the 2026-05-15 cap-breach run; see
# prompts/CHANGELOG.md entry v2.57 for the operator-facing rationale.

# Matches `[text](#anchor-slug)` references with a `#`-prefixed href. Used by
# check_anchor_resolution() to scan only intra-document anchor links and skip
# external `http(s)://` URLs that other checks (source-urls) already validate.
ANCHOR_LINK_RE = re.compile(r"\[(?P<text>[^\]]+)\]\(#(?P<slug>[^)]+)\)")

# Matches the raw heading text after `##`, `###`, or `####`. Unlike H2_RE
# (which strips the leading number prefix to derive canonical section keys),
# this captures the full post-prefix string because site/build.py slugifies
# the entire heading line — so `## 5. Deep Dive — …` becomes the slug
# `5-deep-dive-…`, not just `deep-dive-…`.
HEADING_RAW_RE = re.compile(r"^(?P<hashes>#{2,4})\s+(?P<title>.+?)\s*$")


def check_anchor_resolution(brief_text: str) -> None:
    """Every [text](#slug) in the brief must resolve to an H2/H3/H4 in the brief.

    The 2026-05-15 cap-breach run found 5 broken anchor links in § 6 Action
    Items: a stale slug from an iter-2 heading rename plus four `--` vs `-`
    mismatches against the build's slugify (which collapses runs of
    non-alphanumerics to a single hyphen). Mechanically detectable — should
    never burn a verifier iteration. FAIL severity.

    Slugs are computed using the same `slugify` function the static site
    uses (imported from site/build.py at module load, with local fallback),
    so a passing check guarantees a working link in the rendered HTML.
    """
    slugs: set[str] = set()
    for line in brief_text.splitlines():
        m = HEADING_RAW_RE.match(line)
        if m:
            slugs.add(slugify(m.group("title")))

    broken: list[tuple[str, str]] = []
    total = 0
    for m in ANCHOR_LINK_RE.finditer(brief_text):
        total += 1
        slug = m.group("slug").strip()
        # Tolerate trailing slashes that some Markdown renderers emit.
        slug_norm = slug.rstrip("/")
        if slug_norm not in slugs:
            broken.append((m.group("text"), slug))

    if broken:
        examples = "; ".join(f"'{t}' → #{s}" for t, s in broken[:5])
        more = f" (+{len(broken) - 5} more)" if len(broken) > 5 else ""
        fail("anchor-resolution",
             f"{len(broken)} of {total} internal anchor link(s) do not resolve to an H2/H3/H4 slug in the brief: {examples}{more}")
    elif total == 0:
        ok("anchor-resolution", "no internal anchor links to verify")
    else:
        ok("anchor-resolution", f"all {total} internal anchor link(s) resolve to valid H2/H3/H4 slugs")


# Patterns that surface quantifier claims to the verifier. Each category
# corresponds to a class of unsupported-quantifier defect the verifier
# caught in the 2026-05-15 run (BitLocker "five unpatched", "first time
# ESET has documented", "10 additional clusters"). Detection only —
# the operator and the next verifier iteration use the WARN list as a
# focus signal, not a hard-stop. Tier 1 (evidence binding, deferred)
# will convert this to a FAIL once each claim is required to carry an
# in-source verbatim quote.
_QUANTIFIER_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("absolute-claim",
     re.compile(r"\b(?:first time|never before|the only|only known|the first ever|sole)\b", re.I)),
    ("numeric-status",
     re.compile(
         r"\b(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten)\s+"
         r"(?:unpatched|active|confirmed|distinct|named|separate|known)\s+\w+",
         re.I)),
    ("cluster-count",
     re.compile(r"\b\d+\+?\s+(?:additional |new |separate |opportunistic |distinct )?clusters?\b", re.I)),
    ("at-least-count",
     re.compile(r"\b(?:at least|exactly|precisely)\s+\d+\b", re.I)),
]

# Sections where quantifier-flagging would surface noise rather than signal:
# §0 TL;DR (echoes body content), §7 Verification Notes (quotes the brief's
# own quantifiers when documenting drops).
_QUANTIFIER_SKIP_SECTIONS = {"tldr", "verification-notes"}


def check_quantifier_evidence(sections: list[dict[str, Any]]) -> None:
    """Surface quantifier claims for verifier corroboration. WARN severity.

    Pure detection in v2.57 — false positives expected. The output gives the
    verifier (and the next iteration's spawn message) a focused list of claims
    to cross-check against cited sources. Tier 1 evidence-binding will
    upgrade this to FAIL when each claim must carry a verbatim source quote.
    """
    flagged: list[tuple[str, str, str, str]] = []
    for sec in sections:
        if sec["key"] in _QUANTIFIER_SKIP_SECTIONS:
            continue
        for item in sec.get("items", []):
            body_text = "\n".join(item.get("body", []))
            for cat, pat in _QUANTIFIER_PATTERNS:
                for m in pat.finditer(body_text):
                    s, e = m.span()
                    snippet = body_text[max(0, s - 25):min(len(body_text), e + 25)]
                    snippet = re.sub(r"\s+", " ", snippet).strip()
                    flagged.append((sec["key"], item["heading"][:60], cat, snippet))

    if flagged:
        examples = "; ".join(
            f"{cat} in '{h}…': '…{snip}…'" for _, h, cat, snip in flagged[:5]
        )
        more = f" (+{len(flagged) - 5} more)" if len(flagged) > 5 else ""
        warn("quantifier-evidence",
             f"{len(flagged)} quantifier claim(s) detected — verifier should corroborate against cited sources: {examples}{more}")
    else:
        ok("quantifier-evidence", "no quantifier-heuristic matches")


# Regional/sector phrases in TL;DR prose that should be supported by the
# corresponding body footer's Region: / Sector: taxonomy values. v2.52 ships
# a narrow Switzerland/Europe set — the 2026-05-15 failure mode. Other
# regions are reserved for future iteration once historical-brief
# calibration confirms the noise floor.
_TLDR_SWISS_RE = re.compile(r"\b(?:Swiss|Switzerland|CH/|/CH|EU/CH|CH government|federal Swiss)\b", re.I)
_TLDR_EU_RE = re.compile(r"\b(?:European|EU |EU\.|EU/)\b")


def check_tldr_body_drift(sections: list[dict[str, Any]]) -> None:
    """Flag TL;DR bullets whose regional phrasing diverges from the body
    footer's Region: taxonomy values for the same CVE.

    The 2026-05-15 iter-1 finding F4 was: TL;DR said "EU/CH government and
    education" but body footer was `Region: europe` (no switzerland). The
    existing footer-taxonomy check validates taxonomy legality but not
    TL;DR/body consistency. WARN severity.

    Initial scope: switzerland and europe drift on CVE-keyed bullets. Other
    region/sector classes can be added once the noise floor is calibrated.
    """
    by_key = sections_by_key(sections)
    tldr_secs = by_key.get("tldr", [])
    if not tldr_secs:
        ok("tldr-body-drift", "no TL;DR section to check")
        return

    cve_to_footer: dict[str, dict[str, Any]] = {}
    for sec in sections:
        if sec["key"] in {"tldr", "verification-notes"}:
            continue
        for item in sec.get("items", []):
            footer = item.get("footer")
            if not footer:
                continue
            heading_and_body = item["heading"] + "\n" + "\n".join(item.get("body", []))
            for cve in CVE_RE.findall(heading_and_body):
                cve_to_footer.setdefault(cve, footer)

    flagged: list[tuple[str, str, str]] = []
    for sec in tldr_secs:
        for line in sec.get("lines", []):
            s = line.strip()
            if not (s.startswith("- ") or s.startswith("* ")):
                continue
            cves_in_bullet = list(dict.fromkeys(CVE_RE.findall(s)))
            if not cves_in_bullet:
                continue
            swiss_in_tldr = bool(_TLDR_SWISS_RE.search(s))
            eu_in_tldr = bool(_TLDR_EU_RE.search(s))
            for cve in cves_in_bullet:
                footer = cve_to_footer.get(cve)
                if footer is None:
                    continue
                regions = {r.strip().lower() for r in footer.get("regions", [])}
                if swiss_in_tldr and "switzerland" not in regions:
                    flagged.append((
                        cve,
                        "TL;DR mentions Swiss/Switzerland",
                        f"body footer Region: {', '.join(footer.get('regions', [])) or '(empty)'}",
                    ))
                if eu_in_tldr and "europe" not in regions and "global" not in regions:
                    flagged.append((
                        cve,
                        "TL;DR mentions European/EU",
                        f"body footer Region: {', '.join(footer.get('regions', [])) or '(empty)'}",
                    ))

    if flagged:
        examples = "; ".join(f"{cve}: {claim} but {got}" for cve, claim, got in flagged[:5])
        more = f" (+{len(flagged) - 5} more)" if len(flagged) > 5 else ""
        warn("tldr-body-drift",
             f"{len(flagged)} TL;DR/body region drift item(s): {examples}{more}")
    else:
        ok("tldr-body-drift", "TL;DR regional phrasing consistent with body footers")


# Disambiguation phrases that exempt an H3 from the name-collision check.
# When an item shares a name with prior coverage and the body contains one of
# these phrases, the main agent has registered the collision explicitly and
# no WARN is needed.
_DISAMBIGUATION_PHRASES = (
    "named for",
    "no relation to",
    "not to be confused with",
    "same name as",
    "unrelated to the",
    "different from the",
    "shares the name",
    "naming collision",
    "namesake",
)


def check_evidence_shape(sections: list[dict[str, Any]]) -> None:
    """Validate the optional v2.58 `Evidence:` footer field on every item.

    Source-quote binding (Tier 1, v2.58) lets each H3 carry an inline
    `Evidence:` field in its footer — verbatim quotes from cited sources,
    each followed by `(Publisher)` to bind it back to one of the listed
    Sources. This check is shape-only and gentle by design:

    - Items without an `Evidence:` field PASS silently (rollout).
    - Items with an `Evidence:` field whose parsed `evidence: []` list is
      empty (e.g. `Evidence: ` with no quotes or unparseable content) get
      a single FAIL — the field is present but malformed.
    - Items with quotes whose `attribution` does not match any of the
      item's Source publisher labels get a WARN — the attribution should
      bind the quote to a source the brief itself cites, otherwise the
      link from quote to fetched source is lost.

    Content correctness (does the source actually say the quote?) is a
    verifier concern (F4 / F13–F15), not a mechanical concern. The future
    `--strict-evidence` mode would re-fetch each Source URL and substring-
    match the quote, but that adds 5–10 min to the gate and is reserved
    for a follow-up bump.
    """
    malformed: list[tuple[str, str]] = []
    unbound: list[tuple[str, str, str]] = []
    items_with_evidence = 0

    for sec in sections:
        if sec["key"] in {"tldr", "verification-notes"}:
            continue
        for item in sec.get("items", []):
            footer = item.get("footer")
            if not footer:
                continue
            footer_line = item.get("footer_line") or ""
            has_evidence_field = bool(re.search(r"\bEvidence:", footer_line))
            evidence = footer.get("evidence") or []
            if has_evidence_field:
                items_with_evidence += 1
            if has_evidence_field and not evidence:
                malformed.append((sec["key"], item["heading"][:60]))
                continue
            if not evidence:
                continue
            publisher_labels = {
                (s.get("label") or "").strip().lower()
                for s in (footer.get("sources") or [])
                if s.get("label")
            }
            # v2.66 — closed-source providers are valid Evidence attributions.
            publisher_labels |= {
                (cs.get("provider") or "").strip().lower()
                for cs in (footer.get("closed_source") or [])
                if cs.get("provider")
            }
            for rec in evidence:
                attr = (rec.get("attribution") or "").strip().lower()
                if not attr:
                    # Quote with no attribution — flag as unbound. The
                    # attribution is what binds the quote to a Source.
                    unbound.append((sec["key"], item["heading"][:60],
                                    f"quote {rec['quote'][:40]!r} has no attribution"))
                    continue
                # Match if the attribution substring appears in any
                # publisher label (covers "Talos" → "Cisco Talos, 2026-05-14").
                if not any(attr in lbl or lbl in attr for lbl in publisher_labels):
                    unbound.append((
                        sec["key"], item["heading"][:60],
                        f"attribution {rec['attribution']!r} not in any Source publisher label",
                    ))

    if malformed:
        names = "; ".join(f"'{h}' ({k})" for k, h in malformed[:5])
        more = f" (+{len(malformed) - 5} more)" if len(malformed) > 5 else ""
        fail("evidence-shape",
             f"{len(malformed)} item(s) have an `Evidence:` field but no parseable quotes "
             f"(expected `Evidence: \"quote 1\" (Publisher A); \"quote 2\" (Publisher B)`): {names}{more}")
    if unbound:
        names = "; ".join(f"{k}/{h}: {reason}" for k, h, reason in unbound[:5])
        more = f" (+{len(unbound) - 5} more)" if len(unbound) > 5 else ""
        warn("evidence-binding",
             f"{len(unbound)} quote(s) in Evidence fields not bound to a listed Source publisher: {names}{more}")
    if not malformed and not unbound:
        if items_with_evidence:
            ok("evidence-shape",
               f"all {items_with_evidence} item(s) with `Evidence:` carry parseable, bound quotes")
        else:
            ok("evidence-shape",
               "no items carry `Evidence:` field yet (v2.58 rollout — optional)")


def check_profile_sync() -> None:
    """v2.65 — WARN when the ORG-PROFILE managed blocks in the prompts have
    drifted from config/org-profile.yaml (the run then executed against a
    stale composition). WARN-only by design: drift is fixable for the *next*
    run, not retroactively, and the brief must never be blocked on it. The
    compose-profile GitHub Action is the loud enforcement point."""
    script = ROOT / "tools" / "compose_prompts.py"
    cfg = ROOT / "config" / "org-profile.yaml"
    if not script.exists() or not cfg.exists():
        ok("profile-sync", "org-profile composition not present — n/a")
        return
    try:
        proc = subprocess.run(
            [sys.executable, str(script), "--check", "--quiet"],
            capture_output=True, text=True, timeout=120,
        )
    except Exception as e:  # noqa: BLE001 — never let this check crash the gate
        warn("profile-sync", f"compose_prompts --check failed to run: {e}")
        return
    if proc.returncode == 0:
        ok("profile-sync", "ORG-PROFILE blocks in sync with config/org-profile.yaml")
    elif proc.returncode == 3:
        warn("profile-sync",
             "ORG-PROFILE blocks drifted from config/org-profile.yaml — this run "
             "loaded a stale composition; run `python3 tools/compose_prompts.py "
             "--write` and commit the composed prompts alongside this brief")
    elif proc.returncode == 2:
        warn("profile-sync",
             "config/org-profile.yaml is invalid (compose_prompts --check exit 2): "
             + (proc.stderr or "").strip()[:200])
    else:
        warn("profile-sync", f"compose_prompts --check unexpected exit {proc.returncode}")


def _load_org_profile() -> dict[str, Any] | None:
    """Parsed org profile via `compose_prompts.py --dump`, or None when the
    composition is absent/invalid (callers degrade to n/a — never FAIL)."""
    script = ROOT / "tools" / "compose_prompts.py"
    cfg = ROOT / "config" / "org-profile.yaml"
    if not script.exists() or not cfg.exists():
        return None
    try:
        proc = subprocess.run(
            [sys.executable, str(script), "--dump"],
            capture_output=True, text=True, timeout=60,
        )
        if proc.returncode != 0:
            return None
        return json.loads(proc.stdout)
    except Exception:  # noqa: BLE001
        return None


def _footer_status_exploited(footer: dict[str, Any]) -> bool:
    # Handles both plain `exploited` and per-CVE-scoped `exploited (CVE-…)`.
    return any(str(s).strip().lower().startswith("exploited")
               for s in (footer.get("status") or []))


def check_evidence_presence(sections: list[dict[str, Any]], *, kind: str = "daily") -> None:
    """v2.65 — Evidence-escalation presence check (WARN, not FAIL).

    The prompts require the `Evidence:` footer field on: the daily § 0
    Immediate Action callout and every daily § 1 / § 2 item whose Status
    includes `exploited`; every weekly § 1 item; and every weekly § 3 item
    whose Status includes `exploited`. Quotes come from the sub-agents'
    findings YAMLs — the fix is cheap, so the prompt instructs the main
    agent to clear this WARN before the Phase 5.7 / 4.7 verifier spawn."""
    missing: list[tuple[str, str]] = []
    checked = 0
    for sec in sections:
        key = sec["key"]
        for item in sec.get("items", []):
            footer = item.get("footer")
            if not footer:
                continue
            if kind == "weekly":
                required = (key == "weekly-top-stories"
                            or (key == "weekly-vuln-rollup"
                                and _footer_status_exploited(footer)))
            else:
                required = (key == "immediate-actions"
                            or (key in {"active-threats", "trending-vulnerabilities"}
                                and _footer_status_exploited(footer)))
            if not required:
                continue
            checked += 1
            if not (footer.get("evidence") or []):
                missing.append((key, item["heading"][:60]))
    if missing:
        names = "; ".join(f"'{h}' ({k})" for k, h in missing[:5])
        more = f" (+{len(missing) - 5} more)" if len(missing) > 5 else ""
        warn("evidence-presence",
             f"{len(missing)} item(s) require an `Evidence:` field (v2.65 escalation: "
             f"exploited-status / highest-trust items) but carry none: {names}{more} — "
             "populate from the findings YAML `evidence` records before the verifier spawn")
    else:
        ok("evidence-presence",
           f"all {checked} evidence-required item(s) carry an `Evidence:` field"
           if checked else "no evidence-required items in this brief")


_TLP_PUBLIC_ALLOWED = {"", "CLEAR"}          # markings publishable on a public deployment
_TLP_KNOWN = {"CLEAR", "GREEN", "AMBER", "AMBER+STRICT", "RED"}


def check_closed_source(sections: list[dict[str, Any]], *, kind: str = "daily") -> None:
    """v2.66 — closed-source citation hygiene + TLP-vs-deployment gate.

    Closed-source citations (`Closed-source: "Title" (Provider, date, TLP:X,
    ref: ID)`) reference documents dropped under intel/<YYYY-MM-DD>/ by the
    operator's feed script. Checks:
      - TLP gate (FAIL): on a `deployment.visibility: public` profile, any
        closed-source citation marked above TLP:CLEAR fails the commit —
        the brief publishes to the open internet. An unmarked citation
        WARNs (assumed CLEAR, but the drop file should say so).
      - ref-file existence (WARN): a `ref:`/title should trace to a file
        under intel/ — a citation referencing nothing on disk is
        unverifiable for the cold-reader verifier and the operator.
      - reader-visible flag (WARN): an item sourced ONLY from closed
        sources (no public URL) must carry `[CLOSED-SOURCE]` in its
        heading so the reader sees the different verifiability guarantee.
    """
    profile = _load_org_profile()
    visibility = ((profile or {}).get("deployment") or {}).get("visibility", "public")
    intel_root = ROOT / "intel"
    intel_files = {p.name for p in intel_root.glob("*/*")} if intel_root.exists() else set()

    tlp_fails: list[str] = []
    tlp_unmarked: list[str] = []
    missing_refs: list[str] = []
    missing_flag: list[str] = []
    total = 0
    for sec in sections:
        for it in sec.get("items", []):
            footer = it.get("footer") or {}
            cs_list = footer.get("closed_source") or []
            if not cs_list:
                continue
            tag = f"'{it['heading'][:60]}' ({sec['key']})"
            total += len(cs_list)
            for cs in cs_list:
                tlp = (cs.get("tlp") or "").upper()
                if visibility == "public":
                    if tlp and tlp not in _TLP_PUBLIC_ALLOWED:
                        tlp_fails.append(f"{tag}: TLP:{tlp}")
                    elif not tlp:
                        tlp_unmarked.append(tag)
                if intel_files:
                    ref = cs.get("ref") or ""
                    if not any(ref and ref in name for name in intel_files) \
                            and not any((cs.get("title") or "zzz").lower()[:24]
                                        in name.lower() for name in intel_files):
                        missing_refs.append(f"{tag}: ref {ref or cs.get('title', '')!r}")
                elif cs.get("ref"):
                    missing_refs.append(f"{tag}: intel/ directory absent but ref cited")
            if not (footer.get("sources") or []) \
                    and "[CLOSED-SOURCE]" not in (it.get("heading") or "").upper():
                missing_flag.append(tag)

    if tlp_fails:
        fail("closed-source-tlp",
             f"{len(tlp_fails)} closed-source citation(s) above TLP:CLEAR on a PUBLIC "
             f"deployment — remove the item or re-anchor it in public sources: "
             + "; ".join(tlp_fails[:5]))
    elif tlp_unmarked:
        warn("closed-source-tlp",
             f"{len(tlp_unmarked)} closed-source citation(s) without a TLP marking on a "
             f"public deployment (assumed CLEAR — mark the drop file): "
             + "; ".join(tlp_unmarked[:5]))
    if missing_refs:
        warn("closed-source-ref",
             f"{len(missing_refs)} closed-source citation(s) not traceable to a file "
             f"under intel/: " + "; ".join(missing_refs[:5]))
    if missing_flag:
        warn("closed-source-flag",
             f"{len(missing_flag)} item(s) sourced only from closed sources without a "
             f"[CLOSED-SOURCE] heading marker: " + "; ".join(missing_flag[:5]))
    if not (tlp_fails or tlp_unmarked or missing_refs or missing_flag):
        ok("closed-source",
           f"{total} closed-source citation(s), all hygienic" if total
           else "no closed-source citations in this brief")


_ORG_TRIAGE_RE = re.compile(r"^\*\*Org triage \([^)]*\):\*\*\s*([A-Za-z0-9-]+)", re.M)


def check_org_triage(sections: list[dict[str, Any]], *, kind: str = "daily") -> None:
    """v2.65 — org-triage line presence + category-id validity (WARN, not FAIL).

    When config/org-profile.yaml defines vulnerability-triage categories,
    every CVE-typed item in the daily § 2 (weekly § 3) must end its body with
    a `**Org triage (<short_name>):** <id> — …` line whose id is a defined
    category. When no scheme is configured, any Org-triage line is drift.
    Criteria *consistency* (does the category follow from the cited facts?)
    is the verifier's F16 concern — this check is mechanical only."""
    profile = _load_org_profile()
    if profile is None:
        ok("org-triage", "org profile not available — n/a")
        return
    cats = {c["id"] for c in profile["vulnerability_triage"]["categories"]}
    target_key = "weekly-vuln-rollup" if kind == "weekly" else "trending-vulnerabilities"
    problems: list[tuple[str, str, str]] = []
    found = 0
    for sec in sections:
        for item in sec.get("items", []):
            body = "\n".join(item.get("body") or [])
            m = _ORG_TRIAGE_RE.search(body)
            footer = item.get("footer") or {}
            if not cats:
                if m:
                    problems.append((sec["key"], item["heading"][:60],
                                     "Org-triage line present but the profile defines no scheme"))
                continue
            if m:
                found += 1
                if m.group(1) not in cats:
                    problems.append((sec["key"], item["heading"][:60],
                                     f"unknown triage category {m.group(1)!r} "
                                     f"(defined: {sorted(cats)})"))
            elif sec["key"] == target_key and footer.get("cve"):
                problems.append((sec["key"], item["heading"][:60],
                                 "CVE-typed item missing the Org-triage line"))
    if problems:
        names = "; ".join(f"{k}/'{h}': {reason}" for k, h, reason in problems[:5])
        more = f" (+{len(problems) - 5} more)" if len(problems) > 5 else ""
        warn("org-triage", f"{len(problems)} org-triage issue(s): {names}{more}")
    elif not cats:
        ok("org-triage", "no triage scheme configured and no Org-triage lines present")
    else:
        ok("org-triage",
           f"{found} Org-triage line(s) present, all category ids valid")


def check_name_collision(sections: list[dict[str, Any]]) -> None:
    """Flag H3 items that name an entity from prior coverage without
    explicit disambiguation.

    The 2026-05-15 iter-1 F1 (Datadog Shai-Hulud inversion) happened because
    "Shai-Hulud" appeared in prior coverage as the attacker worm and in
    today's § 4 UPDATE as the Datadog tool — without the main agent
    registering the collision. WARN severity; the verifier treats flagged
    items as priority cross-check candidates.

    Reads `name_collision_candidates` from the run's prior_coverage.json
    (the most recent file under work/*/). UPDATE-prefixed H3 items are
    exempt (they link back explicitly), and items containing one of the
    `_DISAMBIGUATION_PHRASES` are exempt (explicit registration).
    """
    candidates_file = None
    for cand in sorted((ROOT / "work").glob("*/prior_coverage.json"), reverse=True):
        candidates_file = cand
        break
    if candidates_file is None:
        ok("name-collision", "no prior_coverage.json found — skipping")
        return

    try:
        prior = json.loads(candidates_file.read_text(encoding="utf-8"))
    except Exception as e:
        warn("name-collision", f"could not parse {candidates_file.relative_to(ROOT)}: {e}")
        return

    candidates = prior.get("name_collision_candidates")
    if not candidates:
        ok("name-collision",
           f"no name_collision_candidates emitted in {candidates_file.relative_to(ROOT)} "
           f"(re-run tools/build_prior_coverage.py to populate; older files lack this field)")
        return

    # Pre-compile a single OR-regex for fast scanning. Anchored on word
    # boundaries so partial-substring noise is suppressed.
    safe_candidates = [re.escape(c) for c in candidates if c]
    if not safe_candidates:
        ok("name-collision", "candidate list empty after sanitisation")
        return
    candidate_re = re.compile(r"\b(?:" + "|".join(safe_candidates) + r")\b")

    flagged: list[tuple[str, str]] = []
    for sec in sections:
        if sec["key"] in {"verification-notes", "tldr"}:
            continue
        for item in sec.get("items", []):
            heading = item["heading"]
            if heading.lstrip().upper().startswith("UPDATE:"):
                continue
            body_lc = " ".join(item.get("body", [])).lower()
            if any(p in body_lc for p in _DISAMBIGUATION_PHRASES):
                continue
            scan_text = heading + "\n" + " ".join(item.get("body", []))
            m = candidate_re.search(scan_text)
            if m:
                flagged.append((heading[:60], m.group(0)))

    if flagged:
        examples = "; ".join(f"'{h}…' shares name '{c}' with prior coverage" for h, c in flagged[:5])
        more = f" (+{len(flagged) - 5} more)" if len(flagged) > 5 else ""
        warn("name-collision",
             f"{len(flagged)} H3 item(s) name an entity from prior coverage without explicit "
             f"disambiguation (verifier should cross-check for attacker/defender inversion): {examples}{more}")
    else:
        ok("name-collision",
           f"no naming collisions detected ({len(candidates)} prior-coverage candidate(s) checked)")


# --- Driver ----------------------------------------------------------------

def resolve_brief_path(arg: str | None) -> Path:
    """Accepts a YYYY-MM-DD (daily) or YYYY-Www (weekly) string, a path, or
    None (→ today's daily). Weekly briefs live under `briefs/weekly/`."""
    if arg is None:
        today = datetime.now(timezone.utc).date().isoformat()
        return BRIEFS_DIR / f"{today}.md"
    if arg.endswith(".md"):
        p = Path(arg)
        return p if p.is_absolute() else (ROOT / arg)
    if re.match(r"^\d{4}-\d{2}-\d{2}$", arg):
        return BRIEFS_DIR / f"{arg}.md"
    if re.match(r"^\d{4}-W\d{2}$", arg):
        return BRIEFS_DIR / "weekly" / f"{arg}.md"
    raise SystemExit(f"could not interpret brief argument: {arg!r}")


def detect_brief_kind(brief_path: Path) -> tuple[str, str, str | None]:
    """Returns (kind, brief_date, iso_week_or_None).

    kind: "daily" if the filename matches YYYY-MM-DD; "weekly" if it matches
    YYYY-Www (and the brief lives under `briefs/weekly/`). Anything else is
    a fatal misuse — the caller raises.
    """
    stem = brief_path.stem
    if re.match(r"^\d{4}-\d{2}-\d{2}$", stem):
        return ("daily", stem, None)
    if re.match(r"^\d{4}-W\d{2}$", stem):
        # Weekly brief — the per-record `date` in run_log.json is the publish
        # date, which we don't know from the filename alone. Use today's UTC
        # date as the comparison anchor and let the run_log check do
        # iso_week-based matching first.
        today = datetime.now(timezone.utc).date().isoformat()
        return ("weekly", today, stem)
    raise SystemExit(f"brief filename does not parse as daily (YYYY-MM-DD) or weekly (YYYY-Www): {stem}")


def run_checks(brief_path: Path, *, skip_build_tests: bool, skip_link_check: bool) -> int:
    print(f"check_brief.py — {brief_path.relative_to(ROOT) if brief_path.is_absolute() else brief_path}\n")

    if not brief_path.exists():
        print(f"FATAL: brief file not found at {brief_path}")
        return 2
    brief_text = brief_path.read_text(encoding="utf-8")
    try:
        kind, brief_date, iso_week = detect_brief_kind(brief_path)
    except SystemExit as e:
        print(f"FATAL: {e}")
        return 2
    print(f"detected kind: {kind}" + (f" · iso_week: {iso_week}" if iso_week else "") + "\n")

    print(f"== state files ==")
    parsed = check_state_json_valid()
    cves_seen = parsed.get("cves_seen.json")
    covered = parsed.get("covered_items.json")
    run_log = parsed.get("run_log.json")
    sources_data = parsed.get("sources.json")

    print(f"\n== taxonomy ==")
    taxonomy = check_taxonomy_loadable()

    print(f"\n== brief structure ==")
    sections = split_sections(brief_text)
    check_section_h3_coverage(sections, kind=kind)

    print(f"\n== AI-content notice ==")
    check_ai_notice(brief_text)

    print(f"\n== IOC scan ==")
    check_no_iocs(brief_text)

    print(f"\n== CVE sync ==")
    check_cve_sync(brief_text, cves_seen)

    if kind == "daily":
        print(f"\n== UPDATE citations ==")
        check_updates_citations(sections)
    else:
        # Weekly briefs do not carry an "Updates to Prior Coverage" section in
        # the same form — § 7 (Long-running campaigns) is the equivalent and
        # uses regular H3 + footer rather than UPDATE blockquotes.
        ok("updates-citations", "n/a for weekly brief (long-running campaigns covered as H3 in § 7)")

    print(f"\n== H3 footers ==")
    check_h3_footers(sections, taxonomy, kind=kind)

    print(f"\n== multi-CVE footer hygiene ==")
    check_multi_cve_footers(sections, kind=kind)

    print(f"\n== blocked source patterns (NVD per-CVE / generic landings / indexes) ==")
    check_blocked_source_patterns(sections, kind=kind)

    print(f"\n== internal anchor links (v2.57) ==")
    check_anchor_resolution(brief_text)

    print(f"\n== primary-source quality ==")
    check_primary_source_quality(sections, kind=kind)

    print(f"\n== aggregator-only sourcing (v2.47) ==")
    check_aggregator_only_sourcing(sections, kind=kind)

    print(f"\n== single-source flag (v2.47) ==")
    check_single_source_flag(sections, kind=kind)

    if kind == "daily":
        print(f"\n== TL;DR deadline-lead (v2.47) ==")
        check_tldr_deadline_lead(sections)

        print(f"\n== TL;DR / body region drift (v2.57) ==")
        check_tldr_body_drift(sections)

    print(f"\n== quantifier-evidence heuristic (v2.57) ==")
    check_quantifier_evidence(sections)

    print(f"\n== name-collision pre-check (v2.57) ==")
    check_name_collision(sections)

    print(f"\n== Evidence-field shape (v2.58) ==")
    check_evidence_shape(sections)

    print(f"\n== Evidence-field presence on exploited-status items (v2.65) ==")
    check_evidence_presence(sections, kind=kind)

    print(f"\n== org-profile composition sync (v2.65) ==")
    check_profile_sync()

    print(f"\n== org-triage lines (v2.65) ==")
    check_org_triage(sections, kind=kind)

    print(f"\n== closed-source citations (v2.66) ==")
    check_closed_source(sections, kind=kind)

    print(f"\n== source URL liveness (HEAD/GET every Source link) ==")
    check_source_urls_resolve(sections, skip=skip_link_check)

    print(f"\n== fetch_source.py for known-403 hosts ==")
    check_fetch_source_for_known_403(brief_text, run_log, brief_date)

    if kind == "daily":
        print(f"\n== covered_items.json appearances ==")
        check_covered_items_appearances(brief_date, sections, covered)

    print(f"\n== run_log.json (Ops dashboard data) ==")
    check_run_log_for_today(brief_date, run_log, kind=kind, iso_week=iso_week)

    print(f"\n== sources.json bookkeeping ==")
    check_sources_touched_today(brief_date, sources_data)

    print(f"\n== essential-source coverage (v2.67) ==")
    check_essential_coverage(brief_date, run_log, sources_data, kind=kind)

    print(f"\n== sources.json schema (shape + controlled-vocab) ==")
    check_sources_schema(sources_data)

    print(f"\n== build-side smoke tests ==")
    check_test_build(skip_build_tests)

    print()
    print(f"summary: {len(PASSES)} pass · {len(WARNS)} warn · {len(FAILS)} fail")
    if FAILS:
        print("\nFAILURES:")
        for f in FAILS:
            print(f"  - {f}")
    if WARNS:
        print("\nWARNINGS (not blocking):")
        for w in WARNS:
            print(f"  - {w}")
    return 1 if FAILS else 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("brief", nargs="?", default=None,
                   help="YYYY-MM-DD or path to a brief; defaults to today")
    p.add_argument("--no-build-tests", action="store_true",
                   help="skip running site/test_build.py")
    p.add_argument("--no-link-check", action="store_true",
                   help="skip the live HEAD/GET check on every Source URL (offline runs)")
    args = p.parse_args()
    return run_checks(
        resolve_brief_path(args.brief),
        skip_build_tests=args.no_build_tests,
        skip_link_check=args.no_link_check,
    )


if __name__ == "__main__":
    sys.exit(main())
