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
    from build import parse_footer_line, parse_taxonomy, validate_footer  # type: ignore
    BUILD_IMPORTED = True
except Exception as exc:  # pragma: no cover — fallback path
    BUILD_IMPORTED = False
    _print("WARN", "build-import",
           f"site/build.py unimportable ({exc!s}); falling back to local parsers")

    _FOOTER_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    def parse_footer_line(line: str) -> dict[str, Any] | None:
        s = line.strip()
        m = re.match(r"^[—-]\s*\*\s*Source:\s*(?P<body>.+?)\*\s*$", s)
        if not m:
            return None
        body = m.group("body").strip()
        out: dict[str, Any] = {"sources": [], "tags": [], "regions": [], "sectors": [],
                                "cve": None, "cvss": None, "vector": None,
                                "auth": None, "status": []}
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
            kv = re.match(r"^([A-Za-z][A-Za-z ]*?):\s*(.*)$", p)
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
    ("tl;dr", "tldr"),
    ("immediate action", "immediate-actions"),
    ("active threats", "active-threats"),
    ("active threat", "active-threats"),
    ("trending vulnerabilities", "trending-vulnerabilities"),
    ("research", "research"),
    ("notable incidents", "active-threats"),  # legacy
    ("switzerland, europe", "active-threats"),  # legacy
    ("updates to prior coverage", "updates"),
    ("updates on previously", "updates"),
    ("deep dive", "deep-dive"),
    ("action items", "action-items"),
    ("verification notes", "verification-notes"),
    ("verification & coverage", "verification-notes"),
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


def check_section_h3_coverage(sections: list[dict[str, Any]]) -> None:
    """The three core content sections (active-threats, trending-vulnerabilities,
    research) must each carry ≥1 H3 item. An empty core section is editorial
    drift — a sub-agent failed and the gap was not surfaced as a stub."""
    by_key = sections_by_key(sections)
    for key in REQUIRED_SECTION_KEYS:
        secs = by_key.get(key, [])
        if not secs:
            fail("section-present", f"section '{key}' missing")
            continue
        total = sum(len(s["items"]) for s in secs)
        title = secs[0]["title"]
        if total == 0:
            # Empty is acceptable only if the section explicitly carries an
            # 'intentionally left empty' stub (less-is-more rule from v2.27).
            body = "\n".join(secs[0]["lines"])
            if re.search(r"intentionally left empty|no qualifying items|no item met the bar",
                         body, re.IGNORECASE):
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


def check_h3_footers(sections: list[dict[str, Any]], taxonomy: dict[str, set[str]]) -> None:
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

    by_key = sections_by_key(sections)
    for key in FOOTERED_SECTION_KEYS:
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
                if not footer.get("sources"):
                    no_source.append(tag)
                if not footer.get("tags"):
                    no_tags.append(tag)
                if not footer.get("regions"):
                    no_region.append(tag)
                errs = validate_footer(footer, taxonomy)
                if errs:
                    bad_taxonomy.append(f"{tag}: {errs}")
                # CVE-typed items: every required CVE field must be present.
                if key == "trending-vulnerabilities" and _has_cve_in_heading(it["heading"]):
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


def check_multi_cve_footers(sections: list[dict[str, Any]]) -> None:
    """When a footer's CVE field is comma-separated (multi-CVE entry), CVSS
    must either be a single value (shared) or carry per-CVE breakdown using
    `/` or `(CVE-...)` syntax. Same for Vector / Auth — flag if multi-CVE and
    a single value claims to apply to all without explicit markup."""
    by_key = sections_by_key(sections)
    soft_warns: list[str] = []
    for key in ("trending-vulnerabilities", "active-threats", "deep-dive", "immediate-actions"):
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
    input by returning empty strings."""
    try:
        from urllib.parse import urlsplit
        u = urlsplit(url)
        return u.netloc.lower(), u.path or "/"
    except Exception:
        return "", ""


def check_blocked_source_patterns(sections: list[dict[str, Any]]) -> None:
    """Hard FAIL when any footer's `Source:` list contains a URL matching a
    known-bad pattern: NVD/MITRE/cve.org per-CVE pages (always derived,
    never the disclosing party) or generic landing / category / index URLs
    that point at navigation, not content."""
    blocked: list[str] = []
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


def check_primary_source_quality(sections: list[dict[str, Any]]) -> None:
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
    soft: list[str] = []
    for sec in sections:
        if sec["key"] not in ("active-threats", "trending-vulnerabilities", "research", "deep-dive"):
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


def check_source_urls_resolve(sections: list[dict[str, Any]],
                                *, skip: bool, timeout: float = 10.0) -> None:
    """Live HEAD/GET every Source URL in every footer; FAIL on 404. Catches
    fabricated-URL drift the v2.27 verifier was designed to find — duplicating
    it here so the operator gets a green/red answer locally without spawning
    a sub-agent. Use `--no-link-check` for offline runs."""
    if skip:
        warn("source-urls", "skipped (--no-link-check)")
        return

    import urllib.request
    import urllib.error
    import socket
    import ssl

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
        urllib.request.urlopen(probe, timeout=5).close()
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
        for method in ("HEAD", "GET"):
            try:
                req = urllib.request.Request(url, headers=headers, method=method)
                with urllib.request.urlopen(req, timeout=timeout) as resp:
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

    if bad_404:
        for u, cited_in in bad_404:
            preview = cited_in[:2]
            more = f" + {len(cited_in) - 2} more" if len(cited_in) > 2 else ""
            fail("source-urls",
                 f"{u} returns 404 — cited in: {preview}{more}")
    if other_errors:
        for u, status, err, cited_in in other_errors:
            warn("source-urls",
                 f"{u}: status={status} err={err!r} — cited in: {cited_in[:2]}")
    if ua_blocked:
        ok("source-urls",
           f"{len(ua_blocked)} URL(s) on UA-blocked hosts (CISA/NCSC.ch/etc.) — handled by fetch_source.py check")
    if not bad_404 and not other_errors:
        ok("source-urls", f"all {checked} source URL(s) returned HTTP 200 (or UA-blocked allowlisted)")


def check_fetch_source_for_known_403(brief_text: str,
                                      run_log: dict[str, Any] | None,
                                      brief_date: str) -> None:
    """CISA + NCSC.ch (and a handful of other known-403 publishers) must be
    fetched via `tools/fetch_source.py`. The Bash invocations live in the run
    log's `tool_calls` if the agent recorded them, but at minimum: if the
    brief mentions a CISA / NCSC.ch URL and the run record reports a 403 for
    that source without a fetch_source.py mitigation, warn the operator."""
    KNOWN_403_HOSTS = ("www.cisa.gov", "cisa.gov", "ncsc.admin.ch", "ncsc.ch")

    cited_hosts: set[str] = set()
    for m in INLINE_LINK_RE.finditer(brief_text):
        url = m.group(1)
        host = url.split("//", 1)[-1].split("/", 1)[0]
        for k in KNOWN_403_HOSTS:
            if k in host:
                cited_hosts.add(k)
                break

    # Any 403 in fetch_failures whose id maps to a known-403 host is a
    # transport problem the agent should have handled with fetch_source.py.
    if not run_log:
        if cited_hosts:
            warn("fetch-source-403", f"brief cites {sorted(cited_hosts)}; cannot verify fetch_source.py was used (run_log unavailable)")
        else:
            ok("fetch-source-403", "no CISA/NCSC.ch URLs cited; nothing to verify")
        return

    # Check today's run for unhandled 403s on known-403 hosts.
    today_runs = [r for r in (run_log.get("runs") or []) if r.get("date") == brief_date]
    if not today_runs:
        warn("fetch-source-403", f"no run_log entry for {brief_date}; cannot verify")
        return
    rec = today_runs[-1]
    failures = rec.get("fetch_failures") or []
    unhandled: list[str] = []
    for f in failures:
        sid = (f.get("id") or "").lower()
        code = str(f.get("code") or "")
        if code in ("403", "429") and any(k.replace(".", "-") in sid or k.split(".")[0] in sid
                                             for k in KNOWN_403_HOSTS):
            unhandled.append(f"{sid} ({code})")
    if unhandled:
        fail("fetch-source-403",
             f"403/429 on known-403 hosts not mitigated via tools/fetch_source.py: {unhandled}")
    elif cited_hosts:
        ok("fetch-source-403", f"CISA/NCSC.ch cited and no unhandled 403/429 in run_log")
    else:
        ok("fetch-source-403", "no CISA/NCSC.ch URLs cited; nothing to verify")


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
    diff = abs(h3_count - appearances)
    if diff > 1:
        warn("covered-items",
             f"H3 in core sections = {h3_count}; appearances on {brief_date} = {appearances}")
    else:
        ok("covered-items",
           f"H3/appearances match within tolerance ({h3_count} vs {appearances})")


def check_run_log_for_today(brief_date: str, run_log: dict[str, Any] | None) -> None:
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
    today_runs = [r for r in runs if r.get("date") == brief_date]
    if not today_runs:
        fail("run-log", f"no entry for {brief_date} in run_log.json — Ops dashboard will not show this run")
        return
    rec = today_runs[-1]

    # Required top-level keys (matches the v2.27+ schema).
    required = {
        "date", "model", "sub_agents", "fetch_failures", "items_published",
        "deep_dive", "verification_iterations", "verification_residual_count",
    }
    missing = required - set(rec.keys())
    if missing:
        fail("run-log-fields", f"{brief_date} record missing keys: {sorted(missing)}")
    else:
        ok("run-log-fields", f"{brief_date} record has every required top-level key")

    # Sub-agent allocation block.
    sa = rec.get("sub_agents") or {}
    incomplete: list[str] = []
    empty_alloc: list[str] = []
    for k in ("S1", "S2", "S3", "S4"):
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
    if incomplete:
        fail("run-log-subagents", f"sub-agent records incomplete: {incomplete}")
    else:
        ok("run-log-subagents", "all four sub-agent allocation records present")
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

    # Verification sub-agent loop fields (Phase 4.5).
    vi = rec.get("verification_iterations")
    vr = rec.get("verification_residual_count")
    if not isinstance(vi, int) or vi < 1:
        fail("run-log-verification", f"verification_iterations should be ≥ 1 (got {vi!r})")
    elif vi > 3:
        warn("run-log-verification", f"verification_iterations = {vi} exceeds the v2.27 cap of 3")
    else:
        ok("run-log-verification", f"verification_iterations = {vi}")
    if not isinstance(vr, int) or vr < 0:
        fail("run-log-verification-residual", f"verification_residual_count should be ≥ 0 (got {vr!r})")
    elif vr > 0:
        warn("run-log-verification-residual",
             f"verification_residual_count = {vr} — published with unresolved findings")
    else:
        ok("run-log-verification-residual", f"verification_residual_count = 0 (clean publish)")


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
    """Hard invariant 1: every brief carries the AI-generated content notice."""
    if "AI-generated content" in brief_text and "no human review" in brief_text:
        ok("ai-notice", "AI-generated content notice present")
    else:
        fail("ai-notice", "missing 'AI-generated content — no human review' notice")


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


# --- Driver ----------------------------------------------------------------

def resolve_brief_path(arg: str | None) -> Path:
    """Accepts a YYYY-MM-DD string, a path, or None (→ today)."""
    if arg is None:
        today = datetime.now(timezone.utc).date().isoformat()
        return BRIEFS_DIR / f"{today}.md"
    if arg.endswith(".md"):
        p = Path(arg)
        return p if p.is_absolute() else (ROOT / arg)
    if re.match(r"^\d{4}-\d{2}-\d{2}$", arg):
        return BRIEFS_DIR / f"{arg}.md"
    raise SystemExit(f"could not interpret brief argument: {arg!r}")


def run_checks(brief_path: Path, *, skip_build_tests: bool, skip_link_check: bool) -> int:
    print(f"check_brief.py — {brief_path.relative_to(ROOT) if brief_path.is_absolute() else brief_path}\n")

    if not brief_path.exists():
        print(f"FATAL: brief file not found at {brief_path}")
        return 2
    brief_text = brief_path.read_text(encoding="utf-8")
    brief_date = brief_path.stem  # YYYY-MM-DD
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", brief_date):
        print(f"FATAL: brief filename does not parse as YYYY-MM-DD: {brief_date}")
        return 2

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
    check_section_h3_coverage(sections)

    print(f"\n== AI-content notice ==")
    check_ai_notice(brief_text)

    print(f"\n== IOC scan ==")
    check_no_iocs(brief_text)

    print(f"\n== CVE sync ==")
    check_cve_sync(brief_text, cves_seen)

    print(f"\n== UPDATE citations ==")
    check_updates_citations(sections)

    print(f"\n== H3 footers ==")
    check_h3_footers(sections, taxonomy)

    print(f"\n== multi-CVE footer hygiene ==")
    check_multi_cve_footers(sections)

    print(f"\n== blocked source patterns (NVD per-CVE / generic landings / indexes) ==")
    check_blocked_source_patterns(sections)

    print(f"\n== primary-source quality ==")
    check_primary_source_quality(sections)

    print(f"\n== source URL liveness (HEAD/GET every Source link) ==")
    check_source_urls_resolve(sections, skip=skip_link_check)

    print(f"\n== fetch_source.py for known-403 hosts ==")
    check_fetch_source_for_known_403(brief_text, run_log, brief_date)

    print(f"\n== covered_items.json appearances ==")
    check_covered_items_appearances(brief_date, sections, covered)

    print(f"\n== run_log.json (Ops dashboard data) ==")
    check_run_log_for_today(brief_date, run_log)

    print(f"\n== sources.json bookkeeping ==")
    check_sources_touched_today(brief_date, sources_data)

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
