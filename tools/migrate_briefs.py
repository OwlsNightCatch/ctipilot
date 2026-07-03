#!/usr/bin/env python3
"""One-shot v2 -> v3 content-model migration tool.

Migrates the v2 monolithic briefs (briefs/YYYY-MM-DD.md, briefs/weekly/
YYYY-Www.md) and v2 state (state/covered_items.json, state/run_log.json,
state/deep_dive_history.json) into the v3 pipeline layout defined by
docs/pipeline.md:

  entries/YYYY-MM-DD/<slug>.md   one entry per footer-bearing v2 item
  entities/registry.yaml         from covered_items.json non-CVE records
  runs/YYYY-MM-DD/<run-id>.md    one run record per v2 run-log entry

The v2 brief parser pieces below are COPIED from site/build.py (not
imported) so this tool stays runnable after build.py is rewritten for v3.
Serialisation and validation go through site/content_model.py - the shared
v3 reference implementation - so migrated output cannot drift from what
the new pipeline consumes.

Usage:
    python3 tools/migrate_briefs.py                  # dry run, summary only
    python3 tools/migrate_briefs.py --write          # write into repo root
    python3 tools/migrate_briefs.py --write --out-root /tmp/somewhere

Kept in the repo for provenance after the one-shot migration ran.
"""

# === IMPORTS / CONSTANTS ===============================================

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "site"))
import content_model  # noqa: E402
from content_model import slugify  # noqa: E402

BRIEFS_DIR = ROOT / "briefs"
WEEKLY_DIR = BRIEFS_DIR / "weekly"
COVERED_ITEMS = ROOT / "state" / "covered_items.json"
RUN_LOG = ROOT / "state" / "run_log.json"
DEEP_DIVE_HISTORY = ROOT / "state" / "deep_dive_history.json"

CVE_RE = re.compile(r"\bCVE-\d{4}-\d{4,7}\b")
LINK_RE = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
FOOTER_LINK_RE = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
PROMPT_VERSION_RE = re.compile(r"\*\*Prompt:\*\*\s*v?([0-9]+\.[0-9]+)", re.IGNORECASE)
DATE_STEM_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WEEK_STEM_RE = re.compile(r"^\d{4}-W\d{2}$")

# covered_items.json type -> registry entity type (docs/pipeline.md).
REGISTRY_TYPE_MAP = {
    "actor": "actor",
    "campaign": "campaign",
    "incident": "incident",
    "tool": "tool",
    "annual-report": "report",
    "vulnerability-trend": "trend",
    "policy": "policy",
}

# Daily v2 section keys that produce entries, and their kind logic
# (applied in entry_kind_for_daily). Order irrelevant; the walk follows
# document order.
DAILY_ENTRY_SECTIONS = (
    "immediate-actions",
    "active-threats",
    "trending-vulnerabilities",
    "research",
    "updates",
    "deep-dive",
)

# Weekly v2 section key -> v3 kind. weekly_section is the v2 key itself.
WEEKLY_KIND_MAP = {
    "weekly-top-stories": "synthesis",
    "weekly-multi-day": "synthesis",
    "weekly-vuln-rollup": "vulnerability",
    "weekly-sector-patterns": "synthesis",
    "weekly-incidents-recap": "incident",
    "weekly-research": "research",
    "weekly-annual-reports": "annual-report",
    "weekly-long-running": "synthesis",
    "weekly-policy": "policy",
}

# National-CERT hosts for verification: single-source-national-cert
# (list copied from tools/check_brief.py / the migration spec).
CERT_HOSTS = (
    "cert.europa.eu", "ncsc.admin.ch", "cisa.gov", "bsi.bund.de",
    "wid.cert-bund.de", "cert.ssi.gouv.fr", "ncsc.gov.uk", "ncsc.nl",
    "cert.at", "cert.pl", "enisa.europa.eu", "ccn-cert.cni.es",
    "acn.gov.it",
)

WARNINGS: list[str] = []


def warn(msg: str) -> None:
    WARNINGS.append(msg)
    print(f"  warning: {msg}")

# === COPIED V2 PARSER: footer ==========================================
# Copied verbatim (minus type annotations' Any import) from site/build.py
# at v2 so the migration tool survives the build.py rewrite.


def host_of(url: str) -> str:
    try:
        import urllib.parse
        h = (urllib.parse.urlparse(url).hostname or "").lower().strip()
        return h.removeprefix("www.")
    except Exception:
        return ""


def parse_closed_source_field(value: str) -> list:
    """Parse the `Closed-source:` footer field (copied from build.py)."""
    records: list = []
    rec_re = re.compile(r'["“]([^"”]+?)["”]\s*\(([^)]*)\)')
    matched_spans: list = []
    for m in rec_re.finditer(value):
        matched_spans.append(m.span())
        title = m.group(1).strip()
        inner = m.group(2).strip()
        rec = {"title": title, "provider": "", "date": "", "tlp": "", "ref": "",
               "raw": m.group(0)}
        for i, part in enumerate(p.strip() for p in inner.split(",")):
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
        records.append(rec)
    leftover = value
    for a, b in sorted(matched_spans, reverse=True):
        leftover = leftover[:a] + leftover[b:]
    leftover = leftover.strip(" ;·")
    if leftover:
        records.append({"title": "", "provider": "", "date": "", "tlp": "",
                        "ref": "", "raw": leftover})
    return records


def parse_footer_line(line: str):
    """Parse a v2 metadata-footer line (copied from build.py).

    Returns dict {sources, tags, regions, sectors, cve, cvss, vector,
    auth, status, evidence, closed_source} or None.
    """
    s = line.strip()
    if not s:
        return None
    while s.startswith(">"):
        s = s[1:].lstrip()
    if not s:
        return None
    m = re.match(r"^[—-]\s*\*\s*(?P<body>.+?)\*\s*$", s)
    if not m:
        return None
    body = m.group("body").strip()
    if not re.search(r"\b(?:Sources?|Tags|Region|Sector|Sectors|CVE|CVSS|Vector|Auth|Status|Additional source|Additional sources|Evidence|Closed-source):", body):
        return None

    links = list(FOOTER_LINK_RE.finditer(body))
    placeholder_map: dict = {}
    body_clean = body
    for idx, lm in enumerate(links):
        ph = f"\x00LINK{idx}\x00"
        placeholder_map[ph] = f"{lm.group(1)}|||{lm.group(2)}"
        body_clean = body_clean.replace(lm.group(0), ph, 1)

    parts = [p.strip() for p in re.split(r"\s+·\s+", body_clean) if p.strip()]
    if not parts:
        return None
    parts[0] = re.sub(r"^Sources?:\s*", "", parts[0]).strip()

    out: dict = {
        "sources": [], "tags": [], "regions": [], "sectors": [],
        "cve": None, "cvss": None, "vector": None, "auth": None,
        "status": [], "evidence": [], "closed_source": [],
    }

    KNOWN_TYPED_KEYS = {
        "tags", "region", "sector", "sectors", "cve", "cvss",
        "vector", "auth", "status", "additional_source", "additional_sources",
        "source", "sources", "evidence", "closed-source", "closed_source",
    }

    def _add_source_from_placeholder(ph: str) -> None:
        if ph not in placeholder_map:
            return
        label, url = placeholder_map[ph].split("|||", 1)
        if any(sx["url"] == url for sx in out["sources"]):
            return
        out["sources"].append({"label": label, "url": url})

    for p in parts:
        key_m = re.match(r"^([A-Za-z][A-Za-z -]*?):\s*(.*)$", p)
        if key_m:
            key = key_m.group(1).strip().lower().replace(" ", "_")
            value = key_m.group(2).strip()
            for ph, val in placeholder_map.items():
                if ph in value:
                    lab, url = val.split("|||", 1)
                    value = value.replace(ph, f"[{lab}]({url})")
            if key in KNOWN_TYPED_KEYS:
                if key in ("additional_source", "additional_sources", "source", "sources"):
                    link_m = re.match(r"^\[([^\]]+)\]\(([^)]+)\)$", value)
                    if link_m and not any(sx["url"] == link_m.group(2) for sx in out["sources"]):
                        out["sources"].append({"label": link_m.group(1), "url": link_m.group(2)})
                elif key == "tags":
                    out["tags"] = [t.strip() for t in value.split(",") if t.strip()]
                elif key == "region":
                    out["regions"] = [t.strip() for t in value.split(",") if t.strip()]
                elif key in ("sector", "sectors"):
                    out["sectors"] = [t.strip() for t in value.split(",") if t.strip()]
                elif key == "cve":
                    out["cve"] = value.strip()
                elif key == "cvss":
                    out["cvss"] = value.strip()
                elif key == "vector":
                    out["vector"] = value.strip()
                elif key == "auth":
                    out["auth"] = value.strip()
                elif key == "status":
                    out["status"] = [t.strip() for t in value.split(",") if t.strip()]
                elif key == "evidence":
                    quote_re = re.compile(
                        r'["“]([^"”]+?)["”]\s*(?:\(\s*(?P<attr>[^)]+?)\s*\))?'
                    )
                    recs: list = []
                    for qm in quote_re.finditer(value):
                        q = qm.group(1).strip()
                        a = (qm.group("attr") or "").strip()
                        if q:
                            recs.append({"quote": q, "attribution": a})
                    out["evidence"] = recs
                elif key in ("closed-source", "closed_source"):
                    out["closed_source"] = parse_closed_source_field(value)
                continue
        for ph in re.findall(r"\x00LINK\d+\x00", p):
            _add_source_from_placeholder(ph)

    has_field = bool(
        out["sources"] or out["tags"] or out["regions"]
        or out["sectors"] or out["cve"] or out["status"]
        or out["closed_source"]
    )
    if not has_field:
        return None
    return out

# === COPIED V2 PARSER: sections / bullets / parse_brief ================
# Copied from site/build.py at v2. One deliberate addition: the
# ("highest-impact", "weekly-top-stories") keyword, because every real
# weekly uses the heading "Highest-impact events — ..." which build.py's
# v2 keyword list dropped into the `other` bucket.

_SECTION_KEYWORDS: list = [
    ("tl;dr", "tldr"),
    ("immediate action", "immediate-actions"),
    ("active threats", "active-threats"),
    ("trending vulnerabilities", "trending-vulnerabilities"),
    ("notable incidents", "active-threats"),           # legacy
    ("switzerland, europe", "active-threats"),          # legacy
    ("threat-actor", "weekly-research"),
    ("research findings", "weekly-research"),
    ("research & threat", "weekly-research"),
    ("research and threat", "weekly-research"),
    ("research", "research"),
    ("updates to prior coverage", "updates"),
    ("updates on previously covered", "updates"),
    ("previously covered items", "updates"),
    ("deep dive", "deep-dive"),
    ("action items", "action-items"),
    ("verification notes", "verification-notes"),
    ("week at a glance", "weekly-glance"),
    ("top stories", "weekly-top-stories"),
    ("highest-impact", "weekly-top-stories"),           # migration addition
    ("multi-day", "weekly-multi-day"),
    ("vulnerability roll-up", "weekly-vuln-rollup"),
    ("sector & victim", "weekly-sector-patterns"),
    ("incidents & disclosures recap", "weekly-incidents-recap"),
    ("annual", "weekly-annual-reports"),
    ("long-running campaigns", "weekly-long-running"),
    ("policy", "weekly-policy"),
    ("looking ahead", "weekly-looking-ahead"),
    ("verification & coverage", "verification-notes"),
]


def section_key_for(heading: str) -> str:
    h = heading.lower()
    for kw, key in _SECTION_KEYWORDS:
        if kw in h:
            return key
    return "other"


def _is_skippable_trailer(s: str) -> bool:
    t = s.strip()
    if not t:
        return True
    return bool(re.match(r"^(?:-{3,}|\*{3,}|_{3,})$", t))


def _split_trailing_footer(body: str):
    """(parsed footer | None, body without the footer line). Copied."""
    lines = body.splitlines()
    while lines and _is_skippable_trailer(lines[-1]):
        lines.pop()
    if not lines:
        return None, body
    fm = parse_footer_line(lines[-1])
    if fm:
        return fm, "\n".join(lines[:-1]).rstrip()
    for j in range(len(lines) - 2, -1, -1):
        fm = parse_footer_line(lines[j])
        if fm:
            stripped = "\n".join(lines[:j] + lines[j + 1:]).strip("\n")
            return fm, stripped
    return None, body


_BULLET_TOP_RE = re.compile(r"^([-*])\s+(\S.*)$")
_BULLET_INLINE_FOOTER_RE = re.compile(
    r"^(?P<head>.*?)\s+(?P<footer>[—-]\s*\*[^*]+\*)\s*$"
)


def _extract_bullets_with_footers(body_md: str):
    """(preamble_md, [{body_md, footer}]) for all-bullets-with-footers
    sections; (body_md, []) otherwise. Copied from build.py."""
    lines = body_md.replace("\r\n", "\n").split("\n")
    i = 0
    n = len(lines)
    while i < n and not lines[i].strip():
        i += 1
    preamble_lines: list = []
    while i < n and not _BULLET_TOP_RE.match(lines[i]):
        preamble_lines.append(lines[i])
        i += 1
    preamble_md = "\n".join(preamble_lines).strip()
    if i >= n:
        return body_md, []

    bullets: list = []
    while i < n:
        m = _BULLET_TOP_RE.match(lines[i])
        if not m:
            return body_md, []
        bullet_body_lines: list = [m.group(2)]
        i += 1
        while i < n:
            line = lines[i]
            if not line.strip():
                j = i + 1
                while j < n and not lines[j].strip():
                    j += 1
                if j >= n:
                    i = j
                    break
                if _BULLET_TOP_RE.match(lines[j]):
                    i = j
                    break
                if lines[j].startswith("  "):
                    bullet_body_lines.append("")
                    i += 1
                    continue
                i = j
                break
            if _BULLET_TOP_RE.match(line):
                break
            if line.startswith("  "):
                bullet_body_lines.append(line[2:])
                i += 1
                continue
            bullet_body_lines.append(line)
            i += 1

        while bullet_body_lines and not bullet_body_lines[-1].strip():
            bullet_body_lines.pop()

        footer = None
        if bullet_body_lines:
            block_candidate = parse_footer_line(bullet_body_lines[-1])
            if block_candidate:
                footer = block_candidate
                bullet_body_lines.pop()
                while bullet_body_lines and not bullet_body_lines[-1].strip():
                    bullet_body_lines.pop()
        if footer is None and bullet_body_lines:
            last = bullet_body_lines[-1]
            mi = _BULLET_INLINE_FOOTER_RE.match(last)
            if mi:
                inline_candidate = parse_footer_line(mi.group("footer"))
                if inline_candidate:
                    footer = inline_candidate
                    bullet_body_lines[-1] = mi.group("head").rstrip()
                    if not bullet_body_lines[-1]:
                        bullet_body_lines.pop()
        if footer is None:
            return body_md, []
        bullets.append({"body_md": "\n".join(bullet_body_lines).strip(),
                        "footer": footer})
    if not bullets:
        return body_md, []
    return preamble_md, bullets


def parse_brief_v2(path: Path) -> dict:
    """Parse a v2 brief. Replicates site/build.py parse_brief for the
    pieces the migration needs, plus each section's *raw* body (build.py
    discards it after footer-lifting; the migration needs it for the
    Immediate-Action callout, TL;DR bullets and run-record notes)."""
    text = path.read_text(encoding="utf-8")
    name = path.stem
    is_weekly = path.parent.name == "weekly"

    m = re.search(r"^# (.+?)\s*$", text, re.MULTILINE)
    title = m.group(1).strip() if m else name
    pv_match = PROMPT_VERSION_RE.search(text)
    prompt_version = f"v{pv_match.group(1)}" if pv_match else None

    h2_starts: list = []
    for m in re.finditer(r"^## (.+?)\s*$", text, re.MULTILINE):
        h2_starts.append((m.start(), m.group(1).strip()))

    sections: list = []
    for idx, (start, heading) in enumerate(h2_starts):
        end = h2_starts[idx + 1][0] if idx + 1 < len(h2_starts) else len(text)
        body = text[start:end]
        first_nl = body.find("\n")
        body_text = body[first_nl + 1:] if first_nl >= 0 else ""
        skey = section_key_for(heading)

        h3_starts: list = []
        for m3 in re.finditer(r"^### (.+?)\s*$", body_text, re.MULTILINE):
            h3_starts.append((m3.start(), m3.group(1).strip()))
        item_starts = h3_starts
        if not item_starts:
            for m4 in re.finditer(r"^#### (.+?)\s*$", body_text, re.MULTILINE):
                item_starts.append((m4.start(), m4.group(1).strip()))

        items: list = []
        for j, (s_item, item_heading) in enumerate(item_starts):
            e_item = item_starts[j + 1][0] if j + 1 < len(item_starts) else len(body_text)
            item_md = body_text[s_item:e_item].strip()
            first_nl_i = item_md.find("\n")
            item_body = item_md[first_nl_i + 1:] if first_nl_i >= 0 else ""
            item_body = item_body.strip()
            footer, stripped_body = _split_trailing_footer(item_body)
            items.append({
                "heading": item_heading,
                "anchor": slugify(item_heading),
                "body_md": stripped_body,
                "raw_md": item_md,
                "footer": footer,
                "section_key": skey,
            })

        section_footer = None
        section_body_md = body_text
        bullet_items: list = []
        if not items:
            preamble_md, bullet_items = _extract_bullets_with_footers(body_text)
            if bullet_items:
                section_body_md = preamble_md
            else:
                section_footer, section_body_md = _split_trailing_footer(body_text)

        sections.append({
            "heading": heading,
            "key": skey,
            "items": items,
            "raw_body": body_text,
            "body_md": section_body_md,
            "section_footer": section_footer,
            "bullet_items": bullet_items,
        })

    return {
        "name": name,
        "kind": "weekly" if is_weekly else "daily",
        "path": str(path.relative_to(ROOT)),
        "title": title,
        "prompt_version": prompt_version,
        "sections": sections,
        "text": text,
    }

# === TEXT / TIME HELPERS ===============================================


def fmt_ts(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def git_added_ts(path: Path):
    """UTC datetime of the commit that added `path`, or None."""
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--follow", "--format=%aI",
             "--", str(path.relative_to(ROOT))],
            cwd=ROOT, capture_output=True, text=True, timeout=30,
        )
        if out.returncode != 0:
            return None
        lines = [l.strip() for l in out.stdout.splitlines() if l.strip()]
        if not lines:
            return None
        return datetime.fromisoformat(lines[-1]).astimezone(timezone.utc)
    except Exception:
        return None


def fallback_ts(brief_name: str) -> datetime:
    """Filename-derived fallback: <date>T05:00:00Z; weeklies anchor on the
    Monday of the ISO week (same convention as v2 build.py)."""
    if WEEK_STEM_RE.match(brief_name):
        y, w = int(brief_name[:4]), int(brief_name[6:])
        d = datetime.fromisocalendar(y, w, 1)
        return d.replace(hour=5, tzinfo=timezone.utc)
    y, m, d = (int(x) for x in brief_name.split("-"))
    return datetime(y, m, d, 5, 0, 0, tzinfo=timezone.utc)


def brief_reference_date(brief_name: str) -> str:
    """Editorial date of the brief: the stem for dailies, the ISO-week
    Sunday for weeklies (used for event_date capping and deep-dive
    history lookups)."""
    if WEEK_STEM_RE.match(brief_name):
        y, w = int(brief_name[:4]), int(brief_name[6:])
        return datetime.fromisocalendar(y, w, 7).strftime("%Y-%m-%d")
    return brief_name


def compute_discovered_at(briefs: list) -> dict:
    """brief name -> base UTC datetime.

    Uses the git first-commit timestamp. When several briefs share one
    identical add-timestamp (the repo's history bulk-import commit added
    45 briefs at once) the git moment is meaningless per-brief, so those
    briefs fall back to the filename-derived timestamp."""
    ts_by_name: dict = {}
    count_by_ts: dict = defaultdict(int)
    for b in briefs:
        ts = git_added_ts(ROOT / b["path"])
        ts_by_name[b["name"]] = ts
        if ts is not None:
            count_by_ts[ts] += 1
    out = {}
    for b in briefs:
        ts = ts_by_name[b["name"]]
        if ts is None or count_by_ts[ts] > 1:
            out[b["name"]] = fallback_ts(b["name"])
        else:
            out[b["name"]] = ts
    return out


_INTERNAL_WEEKLY_LINK_RE = re.compile(
    r"\((?:\.{1,2}/)*(?:briefs/)?weekly/(\d{4}-W\d{2})\.md(#[^)\s]*)?\)")
_INTERNAL_DAILY_LINK_RE = re.compile(
    r"\((?:\.{1,2}/)*(?:briefs/)?(\d{4}-\d{2}-\d{2})\.md(#[^)\s]*)?\)")


def rewrite_internal_links(text: str) -> str:
    """briefs/YYYY-MM-DD.md -> /briefs/YYYY-MM-DD/ (also bare / ../ / ./
    variants); briefs/weekly/YYYY-Www.md -> /weekly/YYYY-Www/."""
    text = _INTERNAL_WEEKLY_LINK_RE.sub(
        lambda m: f"(/weekly/{m.group(1)}/{m.group(2) or ''})", text)
    text = _INTERNAL_DAILY_LINK_RE.sub(
        lambda m: f"(/briefs/{m.group(1)}/{m.group(2) or ''})", text)
    return text


_ANY_LINK_RE = re.compile(r"\[([^\]\n]+)\]\(([^)\s]+)\)")


def flatten_links(text: str) -> str:
    """Replace every markdown link with its label text."""
    return _ANY_LINK_RE.sub(lambda m: m.group(1), text)


def strip_md_inline(text: str) -> str:
    """Markdown bold/italic/code/links -> plain text, single line."""
    text = flatten_links(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"\1", text)
    text = text.replace("`", "")
    return re.sub(r"\s+", " ", text).strip()


_SENT_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z“\"(\[])")


def first_sentences(text: str, n: int, cap: int) -> str:
    """Up to `n` complete sentences of `text` that fit in `cap` chars;
    only the first sentence is ever word-boundary-truncated (when it
    alone exceeds the cap) so the result never ends mid-sentence."""
    text = re.sub(r"\s+", " ", text).strip()
    parts = _SENT_SPLIT_RE.split(text)
    out = ""
    for part in parts[:n]:
        candidate = (out + " " + part).strip()
        if out and len(candidate) > cap:
            break
        out = candidate
    if len(out) > cap:
        out = out[:cap].rsplit(" ", 1)[0].rstrip(",;:—- ") + " …"
    return out


def cap_words(text: str, cap: int) -> str:
    if len(text) <= cap:
        return text
    return text[:cap].rsplit(" ", 1)[0].rstrip(",;:—- ")


_TOKEN_RE = re.compile(r"[a-z0-9][a-z0-9.-]{3,}")


def significant_tokens(text: str) -> set:
    return set(_TOKEN_RE.findall(text.lower()))


def first_paragraph(text: str) -> str:
    for chunk in re.split(r"\n\s*\n", text):
        c = chunk.strip()
        if c:
            return c
    return ""


_LABEL_DATE_RE = re.compile(r"\[[^\]\n]*?(\d{4}-\d{2}-\d{2})[^\]\n]*\]\(")


def event_date_from_body(body: str, brief_date: str):
    """Max YYYY-MM-DD found inside inline citation labels, <= brief date."""
    dates = [d for d in _LABEL_DATE_RE.findall(body) if d <= brief_date]
    valid = []
    for d in dates:
        try:
            datetime.strptime(d, "%Y-%m-%d")
            valid.append(d)
        except ValueError:
            continue
    return max(valid) if valid else None


def strip_markers(heading: str) -> str:
    """Item heading -> clean v3 title: drop UPDATE prefixes,
    [SINGLE-SOURCE...] / [CLOSED-SOURCE...] flags, weekly `key:` markers
    and the ANNUAL REPORT prefix; collapse whitespace."""
    t = heading
    t = re.sub(r"`?\[(?:SINGLE-SOURCE|CLOSED-SOURCE)[^\]]*\]`?", "", t)
    t = re.sub(r"^\s*UPDATE\s*[:—–-]\s*", "", t)
    t = re.sub(r"^\s*ANNUAL REPORT\s*[:—–-]\s*", "", t)
    t = re.sub(r"\(`key:\s*[^`)]*`\)", "", t)
    t = t.replace("**", "").replace("`", "")
    return re.sub(r"\s+", " ", t).strip(" —–-·")


def uniq_slug(title: str, used: set, fallback: str) -> str:
    base = slugify(title)[:60].strip("-")
    if not base:
        base = fallback
    slug = base
    n = 2
    while slug in used:
        suffix = f"-{n}"
        slug = base[: 60 - len(suffix)].rstrip("-") + suffix
        n += 1
    used.add(slug)
    return slug

# === A. ENTITY REGISTRY ================================================


def derive_entity_name(title: str) -> str:
    """Short name from a covered-items title: cut at the first ' — ' /
    ' –' / ': ' boundary when that leaves >= 3 chars, else the full
    title; cap 120."""
    for sep in (" — ", " –", ": "):
        idx = title.find(sep)
        if idx >= 3:
            return title[:idx].strip()[:120]
    return title.strip()[:120]


def build_registry() -> list:
    """entities/registry.yaml entity list from covered_items.json non-CVE
    records. Returns the ordered entity dicts (sorted by key)."""
    data = json.loads(COVERED_ITEMS.read_text(encoding="utf-8"))
    by_key: dict = {}
    for it in data.get("items", []):
        old_type = it.get("type")
        if old_type == "cve":
            continue
        new_type = REGISTRY_TYPE_MAP.get(old_type)
        if new_type is None:
            warn(f"registry: unknown covered_items type {old_type!r} "
                 f"({it.get('key')}) — skipped")
            continue
        old_key = it.get("key") or ""
        slug_part = old_key.split(":", 1)[1] if ":" in old_key else old_key
        slug = slugify(slug_part)[:80].strip("-")
        if not slug:
            warn(f"registry: unslugifiable key {old_key!r} — skipped")
            continue
        key = f"{new_type}:{slug}"
        if key in by_key:
            # Merge duplicates — keep the record with the earliest
            # first_covered; extend last-seen knowledge implicitly.
            if (it.get("first_covered") or "9999") < (by_key[key].get("first_covered") or "9999"):
                by_key[key] = it
            continue
        by_key[key] = it

    # Name derivation with collision fallback: validate_registry treats a
    # repeated name (case-insensitive) as an error, and titles like
    # "Cisco Talos: <campaign>" would otherwise all shorten to the vendor
    # name. Colliding groups fall back to the full title; a residual
    # collision gets a key-slug disambiguator.
    keys = sorted(by_key)
    names: dict = {}
    taken: dict = {}
    for key in keys:
        names[key] = derive_entity_name(by_key[key].get("title") or key)
    counts = defaultdict(list)
    for key in keys:
        counts[names[key].strip().lower()].append(key)
    for norm, ks in counts.items():
        if len(ks) <= 1:
            continue
        for key in ks:
            full = re.sub(r"\s+", " ", (by_key[key].get("title") or key)).strip()[:120]
            names[key] = full
    for key in keys:
        norm = names[key].strip().lower()
        if norm in taken:
            names[key] = f"{names[key][:100]} ({key.split(':', 1)[1]})"[:120]
            norm = names[key].strip().lower()
        taken[norm] = key

    entities = []
    for key in keys:
        it = by_key[key]
        entities.append({
            "key": key,
            "type": key.split(":", 1)[0],
            "name": names[key],
            "aliases": [],
            "nexus": None,
            "summary": re.sub(r"\s+", " ", (it.get("title") or "")).strip(),
            "first_seen": it.get("first_covered"),
        })
    return entities

# === B. ENTRY FIELD BUILDERS ===========================================


# Legacy v2 sector values that are not in the v3 taxonomy.
_SECTOR_ALIASES = {"government": "public-sector", "insurance": "finance"}


def split_footer_tags(footer: dict, taxonomy: dict):
    """(tags, sectors) — v2 footers occasionally put sector values in the
    Tags field (and vice versa: theme values like `cloud`/`ot-ics` in the
    Sector field); v3 validate_entry rejects both, so values move to the
    vocabulary they belong to. A few legacy sector spellings are aliased;
    anything else unknown is dropped with a warning."""
    tax_sectors = taxonomy.get("sectors", set())
    tax_themes = taxonomy.get("themes", set()) | taxonomy.get("nexus", set())
    tags: list = []
    sectors: list = []
    for s in footer.get("sectors") or []:
        s = _SECTOR_ALIASES.get(s, s)
        if s in tax_sectors:
            if s not in sectors:
                sectors.append(s)
        elif s in tax_themes:
            if s not in tags:
                tags.append(s)
        else:
            warn(f"footer sector {s!r} not in taxonomy — dropped")
    for t in footer.get("tags") or []:
        if t in tax_sectors:
            if t not in sectors:
                sectors.append(t)
        elif t not in tags:
            tags.append(t)
    return tags, sectors


def footer_sources(footer: dict) -> list:
    out = []
    for i, s in enumerate(footer.get("sources") or []):
        out.append({
            "url": s["url"],
            "publisher": s["label"],
            "role": "primary" if i == 0 else "corroborating",
        })
    return out


def footer_closed_sources(footer: dict) -> list:
    out = []
    for cs in footer.get("closed_source") or []:
        if not cs.get("title") or not cs.get("provider"):
            continue  # raw-only fragment; nothing citable
        rec = {"title": cs["title"], "provider": cs["provider"]}
        for k in ("date", "tlp", "ref"):
            if cs.get(k):
                rec[k] = cs[k]
        out.append(rec)
    return out


def footer_evidence(footer: dict, sources: list) -> list:
    out = []
    primary = sources[0]["publisher"] if sources else "primary source"
    for ev in footer.get("evidence") or []:
        out.append({
            "quote": ev["quote"],
            "publisher": ev.get("attribution") or primary,
        })
    return out


def _per_cve_parenthetical(value: str, cve_ids: list):
    """Map '<val> (CVE-X), <val2> (CVE-Y)' -> {cve: val}; None when the
    string is not in that explicit format."""
    pairs = re.findall(r"([^,()]+?)\s*\((CVE-\d{4}-\d{4,7})[^)]*\)", value)
    mapping = {cve: val.strip() for val, cve in pairs if cve in cve_ids}
    return mapping or None


def map_cvss(cvss: str, cve_ids: list) -> dict:
    """Footer CVSS string -> {cve_id: cvss string}. Handles the three v2
    shapes: single value, slash-separated in CVE order, and explicit
    '<score> (CVE-...)' pairs. Unmatched -> 'n/a'."""
    out = {c: "n/a" for c in cve_ids}
    if not cvss:
        return out
    cvss = cvss.strip()
    if len(cve_ids) == 1:
        out[cve_ids[0]] = cvss
        return out
    explicit = _per_cve_parenthetical(cvss, cve_ids)
    if explicit:
        out.update(explicit)
        return out
    parts = [p.strip() for p in cvss.split("/") if p.strip()]
    if len(parts) == len(cve_ids):
        for c, v in zip(cve_ids, parts):
            out[c] = v
    elif len(parts) == 1:
        for c in cve_ids:
            out[c] = parts[0]
    return out


def map_shared_or_scoped(value, cve_ids: list) -> dict:
    """Vector/Auth footer value -> {cve_id: value}; handles per-CVE
    parentheticals, else the shared value applies to every CVE."""
    out = {c: None for c in cve_ids}
    if not value:
        return out
    scoped = _per_cve_parenthetical(value, cve_ids)
    if scoped:
        out.update(scoped)
        return out
    v = value.strip()
    for c in cve_ids:
        out[c] = v
    return out


def build_cves(footer: dict, section_key: str, tags: list,
               taxonomy: dict, ctx: str):
    """(cves records, cve_ids, sourcing_note | None) from a v2 footer."""
    raw = footer.get("cve") or ""
    cve_ids = []
    for c in CVE_RE.findall(raw):
        if c not in cve_ids:
            cve_ids.append(c)
    if not cve_ids:
        return [], [], None

    vectors = map_shared_or_scoped(footer.get("vector"), cve_ids)
    auths = map_shared_or_scoped(footer.get("auth"), cve_ids)
    tax_vec = taxonomy.get("cve_vectors", set())
    tax_auth = taxonomy.get("cve_auth", set())
    for c in cve_ids:
        if vectors[c] not in tax_vec:
            vectors[c] = None
        if auths[c] not in tax_auth:
            auths[c] = None
    incomplete = [c for c in cve_ids if vectors[c] is None or auths[c] is None]

    if incomplete:
        if section_key in ("trending-vulnerabilities", "weekly-vuln-rollup"):
            # v2 enforced Vector/Auth in these sections, so a gap here is
            # a rare formatting slip — default rather than drop.
            for c in incomplete:
                vectors[c] = vectors[c] or "user-interaction"
                auths[c] = auths[c] or "post-auth"
            warn(f"{ctx}: Vector/Auth defaulted for {', '.join(incomplete)} "
                 "(vuln section, incomplete v2 footer)")
        else:
            note = ("migration: CVE fields incomplete in v2 footer "
                    f"({', '.join(cve_ids)})")
            return [], cve_ids, note

    cvss_map = map_cvss(footer.get("cvss") or "", cve_ids)
    tax_status = taxonomy.get("cve_status", set())
    raw_status = [s.strip() for s in (footer.get("status") or []) if s.strip()]
    scoped_status: dict = {c: [] for c in cve_ids}
    unscoped: list = []
    for st in raw_status:
        m = re.match(r"^(.*?)\s*\((CVE-\d{4}-\d{4,7})[^)]*\)$", st)
        if m and m.group(2) in scoped_status:
            val = m.group(1).strip()
            if val in tax_status:
                scoped_status[m.group(2)].append(val)
        elif st in tax_status:
            unscoped.append(st)

    tax_types = taxonomy.get("cve_types", set())
    cve_type = next((t for t in tags if t in tax_types), None)

    records = []
    for c in cve_ids:
        status = scoped_status[c] + [s for s in unscoped if s not in scoped_status[c]]
        if not status:
            if "patch-available" in tags:
                status = ["patch-available"]
            elif "actively-exploited" in tags:
                status = ["exploited"]
            else:
                status = ["patch-available"]
            warn(f"{ctx}: {c} status defaulted to {status[0]} (missing/"
                 "invalid v2 Status)")
        records.append({
            "id": c,
            "cvss": cvss_map[c],
            "epss": None,
            "type": cve_type,
            "vector": vectors[c],
            "auth": auths[c],
            "status": status,
        })
    return records, cve_ids, None


def verification_for(heading: str, sources: list, closed: list) -> str:
    if "SINGLE-SOURCE-NATIONAL-CERT" in heading:
        return "single-source-national-cert"
    if "SINGLE-SOURCE" in heading:
        return "single-source"
    if not sources:
        return "single-source"          # closed-source-only
    if len(sources) >= 2:
        return "multi-source"
    host = host_of(sources[0]["url"])
    if any(host == h or host.endswith("." + h) for h in CERT_HOSTS):
        return "single-source-national-cert"
    return "single-source"


def append_note(entry: dict, note: str) -> None:
    if entry.get("sourcing_note"):
        entry["sourcing_note"] += "; " + note
    else:
        entry["sourcing_note"] = note


def ensure_evidence(entry: dict, ctx: str) -> None:
    """validate_entry requires evidence[] on immediate_action entries and
    on exploited-status CVEs. Pre-Evidence-era v2 items carry none; the
    only honest backfill is a quote from the migrated body itself,
    explicitly attributed to the v2 brief and flagged in sourcing_note."""
    needs = isinstance(entry.get("immediate_action"), dict) or any(
        "exploited" in (c.get("status") or []) for c in entry.get("cves") or []
    )
    if not needs or entry.get("evidence"):
        return
    quote = first_sentences(strip_md_inline(entry["_body"]), 1, 300)
    if not quote:
        quote = entry["title"]
    entry["evidence"] = [{"quote": quote,
                          "publisher": "ctipilot v2 brief (migrated)"}]
    append_note(entry, "migration: evidence backfilled from v2 brief body "
                       "(item predates the Evidence footer field)")
    warn(f"{ctx}: evidence backfilled from v2 body")


def make_entry(*, brief: dict, section_key: str, heading: str, body_md: str,
               footer: dict, kind: str, horizon: str, taxonomy: dict,
               weekly_section=None) -> dict:
    """Assemble one v3 entry dict (frontmatter fields + private `_` keys
    consumed by later passes and stripped before emit)."""
    ctx = f"{brief['name']}/{heading[:50]}"
    title = strip_markers(heading)
    tags, sectors = split_footer_tags(footer, taxonomy)
    sources = footer_sources(footer)
    closed = footer_closed_sources(footer)
    cves, cve_ids, cve_note = build_cves(footer, section_key, tags, taxonomy, ctx)

    if not tags:
        fallback = {"vulnerability": ["vulnerabilities"],
                    "incident": ["data-breach"]}.get(kind, ["vulnerabilities"])
        tags = list(fallback)
        warn(f"{ctx}: empty v2 Tags — fell back to {tags}")
    regions = list(footer.get("regions") or [])
    if not regions:
        regions = ["global"]
        warn(f"{ctx}: empty v2 Region — fell back to ['global']")

    body = rewrite_internal_links(body_md).strip()
    if not body:
        body = title
        warn(f"{ctx}: empty item body — used the title")

    entry = {
        "schema": 1,
        "kind": kind,
        "horizon": horizon,
        "title": title,
        "headline": cap_words(title, 160),
        "summary": None,                      # filled by TL;DR pass / fallback
        "discovered_at": None,                # filled by the per-brief pass
        "event_date": event_date_from_body(
            body, brief_reference_date(brief["name"])),
        "run_id": None,                       # filled by the per-brief pass
        "priority": "notable",
        "immediate_action": None,
        "tags": tags,
        "regions": regions,
        "sectors": sectors,
        "entities": [],
        "cves": cves,
        "sources": sources,
        "closed_sources": closed,
        "evidence": footer_evidence(footer, sources),
        "verification": verification_for(heading, sources, closed),
        "sourcing_note": None,
        "confidence": "high",
        "update_of": None,
        "references": [],
        "deep_dive": False,
        "deep_dive_category": None,
        "org_triage": None,
        "watchlist_hit": "watchlist" in (footer.get("tags") or []),
        "actions": [],
        "migrated_from": brief["path"],
        # -- private migration state (stripped on emit) --
        "_body": body,
        "_cve_ids": cve_ids,
        "_anchor": slugify(heading),
        "_brief": brief["name"],
        "_section_key": section_key,
        "_heading": heading,
    }
    if weekly_section is not None:
        entry["weekly_section"] = weekly_section
    if cve_note:
        append_note(entry, cve_note)
    if not sources and not closed:
        warn(f"{ctx}: footer has neither sources nor closed-source citations")
    return entry


def finish_summary(entry: dict) -> None:
    if entry.get("summary"):
        return
    summary = first_sentences(flatten_links(first_paragraph(entry["_body"])),
                              2, 320)
    entry["summary"] = strip_md_inline(summary) or entry["headline"]

# === B. DAILY BRIEF MIGRATION ==========================================


def entry_kind_for_daily(section_key: str, heading: str, footer: dict) -> str:
    tags = footer.get("tags") or []
    if section_key == "active-threats":
        return "incident" if "data-breach" in tags else "threat"
    if section_key == "trending-vulnerabilities":
        return "vulnerability"
    if section_key == "research":
        return "annual-report" if re.search(r"annual report", heading, re.I) else "research"
    if section_key in ("updates", "immediate-actions"):
        if footer.get("cve"):
            return "vulnerability"
        return "incident" if "data-breach" in tags else "threat"
    if section_key == "deep-dive":
        return "vulnerability" if footer.get("cve") else "threat"
    return "threat"


def strip_blockquote(text: str) -> str:
    """Remove one level of `> ` blockquote prefix from every line
    (§ 4 Updates items are fully blockquoted in v2)."""
    out = []
    for line in text.splitlines():
        if line.startswith("> "):
            out.append(line[2:])
        elif line.strip() == ">":
            out.append("")
        elif line.startswith(">"):
            out.append(line[1:].lstrip())
        else:
            out.append(line)
    return "\n".join(out)


def migrate_deep_dive(brief: dict, section: dict, taxonomy: dict,
                      dd_cat: dict):
    """The whole § 5 Deep Dive becomes ONE entry: its H3s (if any) are
    narrative sub-headings, and the single metadata footer sits either at
    the section tail or under the last sub-heading."""
    raw = section["raw_body"].rstrip()
    footer, body = _split_trailing_footer(raw)
    if not footer:
        if re.search(r"no item met the deep-dive bar", raw, re.I):
            return None  # intentional empty-section placeholder
        first = strip_md_inline(first_paragraph(raw))[:90]
        warn(f"{brief['name']}: deep-dive section has no metadata footer "
             f"(pre-footer prompt era) — skipped ({first!r})")
        return None
    kind = "vulnerability" if footer.get("cve") else "threat"
    entry = make_entry(
        brief=brief, section_key="deep-dive", heading=section["heading"],
        body_md=body, footer=footer, kind=kind, horizon="operational",
        taxonomy=taxonomy)
    dd_title = re.sub(r"^\s*(?:§\s*)?\d+[.)]?\s*[—–-]?\s*", "", section["heading"])
    dd_title = re.sub(r"^Deep Dive\s*[—–:-]\s*", "", dd_title, flags=re.I)
    dd_title = strip_markers(dd_title)
    if dd_title and dd_title.lower() != "deep dive":
        entry["title"] = dd_title
        entry["headline"] = cap_words(dd_title, 160)
    entry["deep_dive"] = True
    entry["deep_dive_category"] = dd_cat.get(brief["name"], "other")
    return entry


def parse_callout(raw_tldr_body: str):
    """Extract the § 0 `> **Immediate Action — ...**` blockquote callout:
    {title, action, body, footer, cves} or None."""
    lines = raw_tldr_body.splitlines()
    start = None
    for i, l in enumerate(lines):
        if l.lstrip().startswith("> **Immediate Action"):
            start = i
            break
    if start is None:
        return None
    end = start
    while end < len(lines) and lines[end].lstrip().startswith(">"):
        end += 1
    block_lines = lines[start:end]

    footer = None
    body_lines = []
    for l in block_lines:
        f = parse_footer_line(l)
        if f and footer is None:
            footer = f
            continue
        body_lines.append(strip_blockquote(l))
    body = "\n".join(body_lines).strip()

    m = re.search(r"\*\*Immediate Action\s*[—–:-]?\s*(.+?)\*\*", body, re.S)
    if not m:
        return None
    title = re.sub(r"\s+", " ", m.group(1)).strip().rstrip(".")
    rest = body[m.end():].strip()
    action = first_sentences(strip_md_inline(rest), 3, 600)
    if not action:
        action = strip_md_inline(title)
    cves = []
    for c in CVE_RE.findall("\n".join(block_lines)):
        if c not in cves:
            cves.append(c)
    return {"title": title, "action": action, "body": rest,
            "footer": footer, "cves": cves}


def apply_callout(callout: dict, entries: list, brief: dict,
                  taxonomy: dict):
    """Attach the Immediate-Action callout to the same-brief entry that
    shares a CVE (priority: critical + immediate_action), or return a new
    standalone critical entry when nothing matches."""
    ia = {"title": callout["title"], "action": callout["action"]}
    ccves = set(callout["cves"])
    target, best = None, 0
    for e in entries:
        n = len(ccves & set(e["_cve_ids"]))
        if n > best:
            target, best = e, n
    if target is not None:
        target["priority"] = "critical"
        target["immediate_action"] = ia
        if not target["evidence"] and callout["footer"]:
            target["evidence"] = footer_evidence(
                callout["footer"], target["sources"])
        return None

    footer = callout["footer"]
    if footer is None:
        # No structured footer on the callout: synthesise sources from
        # its inline citations so the standalone entry stays verifiable.
        srcs = []
        seen = set()
        for lm in LINK_RE.finditer(callout["body"]):
            if lm.group(2) in seen:
                continue
            seen.add(lm.group(2))
            srcs.append({"label": lm.group(1).strip(), "url": lm.group(2)})
        footer = {"sources": srcs, "tags": [], "regions": [], "sectors": [],
                  "cve": ", ".join(callout["cves"]) or None, "cvss": None,
                  "vector": None, "auth": None, "status": [],
                  "evidence": [], "closed_source": []}
        warn(f"{brief['name']}: Immediate-Action callout has no footer — "
             "sources synthesised from inline links")
    kind = "vulnerability" if footer.get("cve") else "threat"
    entry = make_entry(
        brief=brief, section_key="immediate-actions",
        heading=callout["title"], body_md=callout["body"], footer=footer,
        kind=kind, horizon="operational", taxonomy=taxonomy)
    entry["priority"] = "critical"
    entry["immediate_action"] = ia
    return entry


def parse_tldr_bullets(raw_body: str) -> list:
    """Top-level `- ` bullets of the § 0 TL;DR / weekly glance section
    (blockquote callout lines excluded, aggregate footers dropped)."""
    bullets: list = []
    cur = None
    for line in raw_body.splitlines():
        if line.lstrip().startswith(">"):
            continue
        m = _BULLET_TOP_RE.match(line)
        if m:
            if cur:
                bullets.append(cur)
            cur = m.group(2)
        elif cur is not None and line.strip() and not line.startswith("#"):
            cur += " " + line.strip()
        elif cur is not None and not line.strip():
            bullets.append(cur)
            cur = None
    if cur:
        bullets.append(cur)
    return [b for b in bullets if not parse_footer_line(b)]


def apply_tldr_pass(entries: list, bullets: list) -> None:
    """§ 0 bullet -> entry matching: shared CVE id first, else >= 6 shared
    significant tokens. A matched entry takes the bullet text as its
    summary and priority high (critical stays critical)."""
    taken = set()
    for b in bullets:
        plain = strip_md_inline(b)
        bcves = set(CVE_RE.findall(b))
        target = None
        if bcves:
            for e in entries:
                if id(e) in taken:
                    continue
                if bcves & set(e["_cve_ids"]):
                    target = e
                    break
        if target is None:
            btok = significant_tokens(plain)
            best, bestn = None, 0
            for e in entries:
                if id(e) in taken:
                    continue
                etok = significant_tokens(
                    e["title"] + " " + first_paragraph(e["_body"]))
                n = len(btok & etok)
                if n >= 6 and n > bestn:
                    best, bestn = e, n
            target = best
        if target is None:
            continue
        taken.add(id(target))
        target["summary"] = plain
        if target["priority"] != "critical":
            target["priority"] = "high"


def simple_bullets(body: str) -> list:
    """Plain top-level bullet extraction for § 6 sections whose bullets
    don't all carry footers. Returns [{text, ctx_cves}]: footer-shaped
    lines are dropped, and CVE ids from the preceding non-bullet group
    header (the 05-09-era checklist shape) carry onto its sub-bullets."""
    bullets: list = []
    cur = None
    ctx_cves: list = []
    for line in body.splitlines():
        if parse_footer_line(line):
            continue
        m = _BULLET_TOP_RE.match(line)
        if m:
            if cur:
                bullets.append({"text": cur.strip(), "ctx_cves": ctx_cves})
            cur = m.group(2)
        elif cur is not None:
            if line.strip():
                cur += " " + line.strip()
            else:
                bullets.append({"text": cur.strip(), "ctx_cves": ctx_cves})
                cur = None
        elif line.strip() and not _is_skippable_trailer(line):
            # Non-bullet prose between bullet groups — a new group header.
            ctx_cves = CVE_RE.findall(line)
    if cur:
        bullets.append({"text": cur.strip(), "ctx_cves": ctx_cves})
    return bullets


def apply_actions_pass(brief: dict, entries: list) -> list:
    """§ 6 Action Items -> per-entry actions[] via anchor-slug match, then
    CVE match. Returns the unmatched bullets (for the run-record body)."""
    section = next((s for s in brief["sections"]
                    if s["key"] == "action-items"), None)
    if section is None:
        return []
    if section["bullet_items"]:
        bullets = [{"text": b["body_md"], "ctx_cves": []}
                   for b in section["bullet_items"]]
    else:
        bullets = simple_bullets(section["body_md"])
    unmatched = []
    for b in bullets:
        b_one = re.sub(r"\s+", " ", b["text"]).strip()
        if not b_one:
            continue
        target = None
        for a in re.findall(r"\]\(#([^)\s]+)\)", b_one):
            target = next((e for e in entries if e["_anchor"] == a), None)
            if target:
                break
        if target is None:
            bcves = set(CVE_RE.findall(b_one)) or set(b["ctx_cves"])
            if bcves:
                target = next((e for e in entries
                               if bcves & set(e["_cve_ids"])), None)
        text = re.sub(r"\[([^\]]+)\]\(#[^)]*\)", r"\1", b_one).strip()
        if target is not None:
            target["actions"].append(text)
        else:
            unmatched.append(text)
    return unmatched


def migrate_daily(brief: dict, taxonomy: dict, dd_cat: dict):
    """One v2 daily brief -> (entries, unmatched_action_items)."""
    entries: list = []
    tldr_raw = ""
    for section in brief["sections"]:
        key = section["key"]
        if key == "tldr":
            tldr_raw = section["raw_body"]
            continue
        if key == "deep-dive":
            e = migrate_deep_dive(brief, section, taxonomy, dd_cat)
            if e:
                entries.append(e)
            continue
        if key not in DAILY_ENTRY_SECTIONS:
            continue
        for item in section["items"]:
            if not item["footer"]:
                warn(f"{brief['name']}: footerless item skipped in {key}: "
                     f"{item['heading'][:70]!r}")
                continue
            body = item["body_md"]
            if key == "updates":
                body = strip_blockquote(body)
            kind = entry_kind_for_daily(key, item["heading"], item["footer"])
            entries.append(make_entry(
                brief=brief, section_key=key, heading=item["heading"],
                body_md=body, footer=item["footer"], kind=kind,
                horizon="operational", taxonomy=taxonomy))

    callout = parse_callout(tldr_raw) if tldr_raw else None
    if callout:
        standalone = apply_callout(callout, entries, brief, taxonomy)
        if standalone is not None:
            entries.append(standalone)
    apply_tldr_pass(entries, parse_tldr_bullets(tldr_raw))
    unmatched = apply_actions_pass(brief, entries)
    return entries, unmatched

# === B. WEEKLY BRIEF MIGRATION =========================================


def migrate_looking_ahead(brief: dict, section: dict, taxonomy: dict):
    """§ Looking ahead (footerless bullet list) -> ONE `outlook` entry.
    Sources are the section's inline links (first = primary); tags come
    from a taxonomy-theme scan of the body (fallback: vulnerabilities)."""
    raw = section["raw_body"].strip()
    srcs = []
    seen = set()
    for lm in LINK_RE.finditer(raw):
        if lm.group(2) in seen:
            continue
        seen.add(lm.group(2))
        srcs.append({"label": lm.group(1).strip(), "url": lm.group(2)})
    if not srcs:
        warn(f"{brief['name']}: looking-ahead section has no inline "
             "sources — outlook entry skipped")
        return None

    low = raw.lower()
    themes = taxonomy.get("themes", set()) | taxonomy.get("nexus", set())
    hits = []
    for t in sorted(themes):
        if re.search(rf"(?<![a-z0-9-]){re.escape(t)}(?![a-z0-9-])", low):
            hits.append(t)
    hits.sort(key=lambda t: low.find(t))
    tags = hits[:6] or ["vulnerabilities"]

    footer = {"sources": srcs, "tags": tags, "regions": ["global"],
              "sectors": [], "cve": None, "cvss": None, "vector": None,
              "auth": None, "status": [], "evidence": [],
              "closed_source": []}
    entry = make_entry(
        brief=brief, section_key="weekly-looking-ahead",
        heading=f"Looking ahead — {brief['name']}", body_md=raw,
        footer=footer, kind="outlook", horizon="strategic",
        taxonomy=taxonomy, weekly_section="weekly-looking-ahead")
    # The section preamble is boilerplate ("A focused, justified list…");
    # the first bullet is the actual signal — use it as the summary.
    bullets = parse_tldr_bullets(raw)
    if bullets:
        entry["summary"] = first_sentences(strip_md_inline(bullets[0]), 2, 320)
    return entry


def migrate_weekly(brief: dict, taxonomy: dict):
    """One v2 weekly summary -> (entries, [])."""
    entries: list = []
    glance_raw = ""
    for section in brief["sections"]:
        key = section["key"]
        if key == "weekly-glance":
            glance_raw = section["raw_body"]
            continue
        if key == "weekly-looking-ahead":
            e = migrate_looking_ahead(brief, section, taxonomy)
            if e:
                entries.append(e)
            continue
        kind = WEEKLY_KIND_MAP.get(key)
        if kind is None:
            continue
        for item in section["items"]:
            if not item["footer"]:
                warn(f"{brief['name']}: footerless item skipped in {key}: "
                     f"{item['heading'][:70]!r}")
                continue
            entries.append(make_entry(
                brief=brief, section_key=key, heading=item["heading"],
                body_md=item["body_md"], footer=item["footer"], kind=kind,
                horizon="strategic", taxonomy=taxonomy, weekly_section=key))
    apply_tldr_pass(entries, parse_tldr_bullets(glance_raw))
    return entries, []

# === B. CROSS-ENTRY PASSES (entities, update_of) =======================


def finalize_entries(entries: list, base_ts: datetime, run_id: str,
                     used_slugs: dict) -> None:
    """Assign discovered_at (+index seconds, never crossing midnight),
    run_id, summaries, evidence backfill, and day-unique slugs/ids."""
    folder = base_ts.strftime("%Y-%m-%d")
    for idx, e in enumerate(entries):
        ts = base_ts + timedelta(seconds=idx)
        if ts.strftime("%Y-%m-%d") != folder:
            ts = base_ts  # never cross midnight; keep the folder date
        e["discovered_at"] = fmt_ts(ts)
        e["run_id"] = run_id
        finish_summary(e)
        ensure_evidence(e, f"{e['_brief']}/{e['title'][:40]}")
        slug = uniq_slug(e["title"], used_slugs[folder], f"item-{idx + 1}")
        e["_slug"] = slug
        e["_date"] = folder
        e["_id"] = f"{folder}/{slug}"


_ORIG_COVERED_RE = re.compile(r"originally covered (\d{4}-\d{2}-\d{2})")


def resolve_updates(entries: list, entries_by_brief: dict) -> None:
    """§ 4 UPDATE entries -> update_of pointing at the original entry
    (CVE intersection first, then >= 3 shared title tokens). Requires
    chronological processing so the target brief is already migrated."""
    for e in entries:
        if e["_section_key"] != "updates":
            continue
        m = _ORIG_COVERED_RE.search(e["_body"])
        if not m:
            append_note(e, "migration: update target unresolved (no "
                           "originally-covered date in v2 body)")
            warn(f"{e['_brief']}/{e['title'][:40]}: update without an "
                 "originally-covered date")
            continue
        date = m.group(1)
        cands = entries_by_brief.get(date, [])
        target = None
        # CVE match first — footer CVE ids plus ids named in the titles
        # (updates on no-CVE campaigns often name the CVE only there).
        ecves = set(e["_cve_ids"]) | set(CVE_RE.findall(e["title"]))
        if ecves:
            target = next(
                (c for c in cands
                 if ecves & (set(c["_cve_ids"]) | set(CVE_RE.findall(c["title"])))),
                None)
        if target is None:
            def toks(text):
                t = significant_tokens(text)
                return t | {p for w in t for p in w.split("-")
                            if len(p) > 3 and not p.isdigit()}
            ttok = toks(e["title"])
            # >= 3 shared title tokens, best match. Unexpanded tokens
            # only — hyphen expansion would triple-count one shared
            # concept ("supply-chain" -> supply, chain) into a match.
            best, bestn = None, 0
            for c in cands:
                n = len(significant_tokens(e["title"])
                        & significant_tokens(c["title"]))
                if n >= 3 and n > bestn:
                    best, bestn = c, n
            target = best
            if target is None:
                # Anchored fallbacks. The anchor must be a shared *title*
                # token that appears with an uppercase letter in the
                # update's title — a proper noun (FortiBleed, Klue,
                # YellowKey), not prose vocabulary ("leaked", "operator")
                # and not a ubiquitous vendor/platform name, which would
                # link unrelated stories about the same vendor.
                stop = {"microsoft", "google", "apple", "cisco", "oracle",
                        "ivanti", "fortinet", "vmware", "adobe", "linux",
                        "windows", "android", "apache", "github", "gitlab",
                        "amazon", "chrome", "firefox", "mozilla", "citrix",
                        "salesforce", "cisa", "ncsc", "storm"}

                def anchored(c):
                    for t in ttok & toks(c["title"]):
                        if t.startswith("cve-") or t.isdigit() or t in stop:
                            continue
                        m2 = re.search(re.escape(t), e["title"], re.I)
                        if m2 and any(ch.isupper() for ch in m2.group(0)):
                            return True
                    return False

                def best_of(pairs):
                    scored = sorted(pairs, key=lambda p: -p[0])
                    return scored[0][1] if scored else None

                target = best_of([
                    (len(ttok & toks(c["title"])), c) for c in cands
                    if len(ttok & toks(c["title"])) >= 2 and anchored(c)])
                if target is None:
                    target = best_of([
                        (len(ttok & toks(c["title"] + " "
                                         + first_paragraph(c["_body"]))), c)
                        for c in cands
                        if len(ttok & toks(c["title"] + " "
                                           + first_paragraph(c["_body"]))) >= 3
                        and anchored(c)])
        if target is None:
            append_note(e, "migration: update target unresolved "
                           f"(originally covered {date})")
            warn(f"{e['_brief']}/{e['title'][:40]}: update target "
                 f"unresolved (originally covered {date})")
        else:
            e["update_of"] = target["_id"]


def link_entities(entries: list, registry_entities: list) -> None:
    """Scan title+body for registry entity names (case-insensitive,
    whole-word, len >= 4, longest names first, cap 8 per entry)."""
    patterns = []
    for ent in registry_entities:
        for nm in [ent["name"]] + list(ent.get("aliases") or []):
            if len(nm) < 4:
                continue
            rx = re.compile(
                rf"(?<![A-Za-z0-9]){re.escape(nm)}(?![A-Za-z0-9])", re.I)
            patterns.append((len(nm), nm.lower(), rx, ent["key"]))
    patterns.sort(key=lambda p: (-p[0], p[1]))
    for e in entries:
        hay = e["title"] + "\n" + e["_body"]
        low = hay.lower()
        found: list = []
        for _ln, nm_low, rx, key in patterns:
            if len(found) >= 8:
                break
            if key in found:
                continue
            if nm_low in low and rx.search(hay):
                found.append(key)
        e["entities"] = found

# === C. RUN RECORDS ====================================================

# v2 run-log fields consumed into computed v3 fields (everything else is
# copied through verbatim — extra keys are allowed on run records).
_RUN_HANDLED_KEYS = {
    "run_id", "date", "kind", "started", "completed", "duration_seconds",
    "model", "model_id", "prompt_version", "gap_hours", "window_hours",
    "sub_agents", "fetch_failures", "bridge_uses", "sources_changed",
    "verification", "verification_iterations", "verification_residual_count",
    "items_dropped_by_verification", "deep_dive",
}


def map_run_kind(v2_kind) -> str:
    if v2_kind in (None, "daily"):
        return "intel"
    if v2_kind == "weekly":
        return "weekly"
    return "intel"  # e.g. the one manual 'audit' session


def run_date_of(run: dict) -> str:
    d = str(run.get("date") or "")
    if DATE_STEM_RE.match(d):
        return d
    started = str(run.get("started") or "")
    if re.match(r"^\d{4}-\d{2}-\d{2}T", started):
        warn(f"run {run.get('run_id')}: invalid date {d!r} — derived "
             f"{started[:10]} from `started`")
        return started[:10]
    warn(f"run {run.get('run_id')}: no usable date")
    return d


def match_runs_to_briefs(runs: list, briefs: list) -> dict:
    """brief name -> v2 run dict. Dailies match daily-kind runs by date
    (last by `started` when several); weeklies match weekly-kind runs by
    iso_week / run_id prefix. Non-brief kinds (audit) never match."""
    out: dict = {}
    for b in briefs:
        if b["kind"] == "daily":
            cands = [r for r in runs
                     if r.get("kind") in (None, "daily")
                     and run_date_of(r) == b["name"]]
        else:
            cands = [r for r in runs if r.get("kind") == "weekly"
                     and (r.get("iso_week") == b["name"]
                          or str(r.get("run_id", "")).startswith(b["name"]))]
        if cands:
            cands.sort(key=lambda r: str(r.get("started") or ""))
            out[b["name"]] = cands[-1]
    return out


def _run_body(brief: dict | None, notes_md: str, unmatched: list) -> str:
    parts = []
    if notes_md.strip():
        parts.append(rewrite_internal_links(notes_md).strip())
    if unmatched:
        parts.append("### Unmatched action items (migrated)\n\n"
                     + "\n".join(f"- {a}" for a in unmatched))
    if brief is not None:
        parts.append(f"_Migrated from {brief['path']} (v2)._")
    else:
        parts.append("_No brief matched this run in migration._")
    return "\n\n".join(parts)


def _brief_counters(entries: list):
    published = len(entries)
    updated = sum(1 for e in entries if e.get("update_of"))
    dd = next((e["_id"] for e in entries if e.get("deep_dive")), None)
    return published, updated, dd


def build_run_records(runs: list, briefs: list, run_for_brief: dict,
                      entries_by_brief: dict, notes_by_brief: dict,
                      unmatched_by_brief: dict, base_ts: dict) -> list:
    """All v3 run records: one per v2 run-log entry, plus synthetic
    `<date>-migrated` records for briefs that have no matching run.
    Returns [{fm, body, date, run_id}]."""
    records = []
    brief_by_name = {b["name"]: b for b in briefs}
    brief_for_run = {id(r): n for n, r in run_for_brief.items()}

    for run in runs:
        rid = str(run.get("run_id"))
        date = run_date_of(run)
        matched_name = brief_for_run.get(id(run))
        brief = brief_by_name.get(matched_name) if matched_name else None
        entries = entries_by_brief.get(matched_name, []) if matched_name else []
        published, updated, dd = _brief_counters(entries)

        fm = {
            "schema": 1,
            "run_id": rid,
            "kind": map_run_kind(run.get("kind")),
            "date": date,
            "started": run.get("started"),
            "completed": run.get("completed"),
            "duration_seconds": run.get("duration_seconds"),
            "model": run.get("model"),
            "model_id": run.get("model_id"),
            "prompt_version": run.get("prompt_version"),
        }
        for k in ("window_hours", "gap_hours"):
            if k in run:
                fm[k] = run[k]
        fm["entries_published"] = published
        fm["entries_updated"] = updated
        fm["deep_dive"] = dd
        fm["sub_agents"] = run.get("sub_agents") or {}
        fm["fetch_failures"] = run.get("fetch_failures") or []
        if "bridge_uses" in run:
            fm["bridge_uses"] = run.get("bridge_uses") or []
        if "sources_changed" in run:
            fm["sources_changed"] = run.get("sources_changed") or []
        fm["entities_added"] = []
        fm["entries_dropped_by_verification"] = (
            run.get("items_dropped_by_verification") or 0)
        fm["verification_iterations"] = run.get("verification_iterations") or 0
        fm["verification_residual_count"] = (
            run.get("verification_residual_count") or 0)
        if run.get("verification") is not None:
            fm["verification"] = run["verification"]
        # v2 fields carried through verbatim; names that clash with a
        # computed v3 field get a v2_ prefix.
        if run.get("kind") not in (None, "daily", "weekly"):
            fm["v2_kind"] = run["kind"]
        if isinstance(run.get("deep_dive"), str) and run["deep_dive"]:
            fm["v2_deep_dive"] = run["deep_dive"]
        for k in sorted(run.keys()):
            if k in _RUN_HANDLED_KEYS or k in fm:
                continue
            fm[k] = run[k]
        fm["migrated_from"] = "state/run_log.json"

        if brief is not None:
            body = _run_body(brief, notes_by_brief.get(matched_name, ""),
                             unmatched_by_brief.get(matched_name, []))
        else:
            body = _run_body(None, "", [])
        records.append({"fm": fm, "body": body, "date": date, "run_id": rid})

    # Synthetic records for briefs with no v2 run-log entry.
    for b in briefs:
        if b["name"] in run_for_brief:
            continue
        ts = fmt_ts(base_ts[b["name"]])
        entries = entries_by_brief.get(b["name"], [])
        published, updated, dd = _brief_counters(entries)
        date = base_ts[b["name"]].strftime("%Y-%m-%d")
        rid = f"{b['name']}-migrated"
        fm = {
            "schema": 1,
            "run_id": rid,
            "kind": "intel" if b["kind"] == "daily" else "weekly",
            "date": date,
            "started": ts,
            "completed": ts,
            "duration_seconds": 0,
            "model": "unknown",
            "model_id": "unknown",
            "prompt_version": b.get("prompt_version") or "v2.x",
            "entries_published": published,
            "entries_updated": updated,
            "deep_dive": dd,
            "sub_agents": {},
            "fetch_failures": [],
            "entities_added": [],
            "entries_dropped_by_verification": 0,
            "verification_iterations": 0,
            "verification_residual_count": 0,
            "migrated_from": b["path"],
        }
        body = _run_body(b, notes_by_brief.get(b["name"], ""),
                         unmatched_by_brief.get(b["name"], []))
        records.append({"fm": fm, "body": body, "date": date, "run_id": rid})
        warn(f"{b['name']}: no v2 run-log entry — synthetic run record "
             f"{rid} created")
    return records

# === D. VALIDATION / EMIT / MAIN =======================================

ENTRY_KEY_ORDER = (
    "schema", "kind", "horizon", "weekly_section", "title", "headline",
    "summary", "discovered_at", "event_date", "run_id", "priority",
    "immediate_action", "tags", "regions", "sectors", "entities", "cves",
    "sources", "closed_sources", "evidence", "verification",
    "sourcing_note", "confidence", "update_of", "references", "deep_dive",
    "deep_dive_category", "org_triage", "watchlist_hit", "actions",
    "migrated_from",
)


def entry_frontmatter(e: dict) -> dict:
    fm = {}
    for k in ENTRY_KEY_ORDER:
        if k == "weekly_section" and "weekly_section" not in e:
            continue
        fm[k] = e.get(k)
    return fm


def entry_validation_view(e: dict) -> dict:
    view = dict(content_model.ENTRY_DEFAULTS)
    view.update(entry_frontmatter(e))
    view["slug"] = e["_slug"]
    view["date"] = e["_date"]
    view["id"] = e["_id"]
    view["body"] = e["_body"]
    return view


def validate_all(all_entries: list, registry_map: dict, taxonomy: dict,
                 run_records: list):
    """(entry+registry errors, run-record schema-complete count)."""
    errors = []
    registry_keys = set(registry_map)
    for e in all_entries:
        errors.extend(content_model.validate_entry(
            entry_validation_view(e), taxonomy, registry_keys))
    errors.extend(content_model.validate_registry(registry_map))
    complete = 0
    for r in run_records:
        view = dict(r["fm"])
        view["body"] = r["body"]
        view["date_dir"] = r["date"]
        if not content_model.validate_run_record(view):
            complete += 1
    return errors, complete


def emit_all(all_entries: list, registry_entities: list, run_records: list,
             out_root: Path) -> None:
    for e in all_entries:
        path = out_root / "entries" / e["_date"] / f"{e['_slug']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content_model.compose_frontmatter_doc(
            entry_frontmatter(e), e["_body"]), encoding="utf-8")
    reg_path = out_root / "entities" / "registry.yaml"
    reg_path.parent.mkdir(parents=True, exist_ok=True)
    reg_path.write_text(content_model.dump_yaml_subset(
        {"schema": 1, "entities": registry_entities}), encoding="utf-8")
    for r in run_records:
        path = out_root / "runs" / r["date"] / f"{r['run_id']}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content_model.compose_frontmatter_doc(
            r["fm"], r["body"]), encoding="utf-8")


def reverify_from_disk(out_root: Path, taxonomy: dict):
    """--write self-check: re-load everything through content_model's own
    loaders from the out-root and re-validate."""
    errors = []
    registry = content_model.load_registry(out_root / "entities" / "registry.yaml")
    errors.extend(content_model.validate_registry(registry))
    entries = content_model.collect_entries(out_root / "entries", root=out_root)
    for e in entries:
        errors.extend(content_model.validate_entry(e, taxonomy, set(registry)))
    runs = content_model.collect_runs(out_root / "runs", root=out_root)
    complete = sum(1 for r in runs
                   if not content_model.validate_run_record(r))
    return entries, registry, runs, complete, errors


def migrate(write: bool, out_root: Path) -> int:
    taxonomy = content_model.parse_taxonomy()
    registry_entities = build_registry()
    registry_map = {e["key"]: e for e in registry_entities}

    dd_hist = json.loads(DEEP_DIVE_HISTORY.read_text(encoding="utf-8"))
    dd_cat = {e.get("date"): (e.get("category") or "other")
              for e in dd_hist.get("entries", [])}

    daily_paths = sorted(p for p in BRIEFS_DIR.glob("*.md")
                         if DATE_STEM_RE.match(p.stem))
    weekly_paths = sorted(p for p in WEEKLY_DIR.glob("*.md")
                          if WEEK_STEM_RE.match(p.stem))
    briefs = ([parse_brief_v2(p) for p in daily_paths]
              + [parse_brief_v2(p) for p in weekly_paths])
    base_ts = compute_discovered_at(briefs)
    runs = json.loads(RUN_LOG.read_text(encoding="utf-8")).get("runs", [])
    run_for_brief = match_runs_to_briefs(runs, briefs)

    used_slugs: dict = defaultdict(set)
    entries_by_brief: dict = {}
    notes_by_brief: dict = {}
    unmatched_by_brief: dict = {}
    stats = []

    for brief in briefs:  # dailies chronologically, then weeklies
        run = run_for_brief.get(brief["name"])
        rid = str(run["run_id"]) if run else f"{brief['name']}-migrated"
        if brief["kind"] == "daily":
            entries, unmatched = migrate_daily(brief, taxonomy, dd_cat)
        else:
            entries, unmatched = migrate_weekly(brief, taxonomy)
        finalize_entries(entries, base_ts[brief["name"]], rid, used_slugs)
        if brief["kind"] == "daily":
            resolve_updates(entries, entries_by_brief)
        entries_by_brief[brief["name"]] = entries
        unmatched_by_brief[brief["name"]] = unmatched
        notes = next((s["raw_body"] for s in brief["sections"]
                      if s["key"] == "verification-notes"), "")
        notes_by_brief[brief["name"]] = notes.strip()
        kinds = defaultdict(int)
        for e in entries:
            kinds[e["kind"]] += 1
        stats.append((brief["name"], len(entries),
                      " ".join(f"{k}={v}" for k, v in sorted(kinds.items())),
                      len(unmatched)))

    all_entries = [e for b in briefs for e in entries_by_brief[b["name"]]]
    link_entities(all_entries, registry_entities)
    run_records = build_run_records(
        runs, briefs, run_for_brief, entries_by_brief, notes_by_brief,
        unmatched_by_brief, base_ts)

    errors, complete_runs = validate_all(
        all_entries, registry_map, taxonomy, run_records)

    print()
    print(f"{'brief':<12} {'entries':>7}  kinds (unmatched actions)")
    for name, n, kinds, unm in stats:
        extra = f" (unmatched-actions={unm})" if unm else ""
        print(f"{name:<12} {n:>7}  {kinds}{extra}")
    print()
    print(f"briefs: {len(briefs)}  entries: {len(all_entries)}  "
          f"entities: {len(registry_entities)}  "
          f"run-records: {len(run_records)} "
          f"(schema-complete: {complete_runs}, "
          f"sparse-migrated: {len(run_records) - complete_runs})")
    print(f"warnings: {len(WARNINGS)}")

    if errors:
        print(f"\nvalidation errors ({len(errors)}):")
        for err in errors[:50]:
            print(f"  ERROR: {err}")
        if len(errors) > 50:
            print(f"  ... and {len(errors) - 50} more")

    if not write:
        print(f"\n(dry run — nothing written; --write targets {out_root})")
        print(f"migration: entries={len(all_entries)} "
              f"runs={len(run_records)} entities={len(registry_entities)} "
              f"validation-errors={len(errors)}")
        return 1 if errors else 0

    emit_all(all_entries, registry_entities, run_records, out_root)
    entries2, registry2, runs2, complete2, errors2 = reverify_from_disk(
        out_root, taxonomy)
    print(f"\nwrote to {out_root}: entries={len(entries2)} "
          f"entities={len(registry2)} run-records={len(runs2)} "
          f"(schema-complete: {complete2})")
    all_errors = errors + errors2
    if errors2:
        print(f"re-load validation errors ({len(errors2)}):")
        for err in errors2[:50]:
            print(f"  ERROR: {err}")
    print(f"migration: entries={len(entries2)} runs={len(runs2)} "
          f"entities={len(registry2)} validation-errors={len(all_errors)}")
    return 1 if all_errors else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="One-shot v2 -> v3 content migration (see docs/pipeline.md)")
    ap.add_argument("--write", action="store_true",
                    help="write entries/, entities/, runs/ (default: dry run)")
    ap.add_argument("--out-root", type=Path, default=ROOT,
                    help="target root for --write (default: repo root)")
    args = ap.parse_args(argv)
    return migrate(args.write, args.out_root.resolve())


if __name__ == "__main__":
    sys.exit(main())
