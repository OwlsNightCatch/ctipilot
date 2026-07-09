#!/usr/bin/env python3
"""Shared content model for the v3 intelligence pipeline.

The single reference implementation for parsing, serialising and
schema-validating the three v3 content types:

  - entries   (entries/<YYYY-MM-DD>/<slug>.md   — per-finding files)
  - registry  (entities/registry.yaml           — global entity registry)
  - runs      (runs/<YYYY-MM-DD>/<run-id>.md    — per-run records)

Consumed by site/build.py, tools/check_run.py and tools/migrate_briefs.py
so producer and consumers can never drift. Normative contract:
docs/pipeline.md. Stdlib-only — no PyYAML.

The frontmatter format is a strict YAML subset (docs/pipeline.md
§ "Frontmatter — strict YAML subset"): 2-space indentation, block
mappings/lists, `- ` items (scalar or mapping), `>` / `|` block scalars,
inline `[a, b]` lists and `{k: v}` mappings of plain scalars only,
`null`/`true`/`false` literals, full-line comments only.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ENTRIES_DIR = ROOT / "entries"
RUNS_DIR = ROOT / "runs"
REGISTRY_PATH = ROOT / "entities" / "registry.yaml"
TAXONOMY_PATH = ROOT / "site" / "taxonomy.yaml"

# ---------------------------------------------------------------------------
# Controlled structural enums (editorial vocabularies live in site/taxonomy.yaml)
# ---------------------------------------------------------------------------

ENTRY_SCHEMA_VERSION = 1
RUN_SCHEMA_VERSION = 1
REGISTRY_SCHEMA_VERSION = 1

KINDS = (
    "threat",
    "incident",
    "vulnerability",
    "research",
    "annual-report",
    "policy",
    "synthesis",
    "outlook",
)
HORIZONS = ("operational", "strategic")
WEEKLY_SECTIONS = (
    "weekly-top-stories",
    "weekly-multi-day",
    "weekly-vuln-rollup",
    "weekly-sector-patterns",
    "weekly-incidents-recap",
    "weekly-research",
    "weekly-annual-reports",
    "weekly-long-running",
    "weekly-policy",
    "weekly-looking-ahead",
)
# Fallback placement of a strategic entry when weekly_section is unset.
KIND_WEEKLY_SECTION = {
    "threat": "weekly-top-stories",
    "incident": "weekly-incidents-recap",
    "vulnerability": "weekly-vuln-rollup",
    "research": "weekly-research",
    "annual-report": "weekly-annual-reports",
    "policy": "weekly-policy",
    "synthesis": "weekly-multi-day",
    "outlook": "weekly-looking-ahead",
}
PRIORITIES = ("critical", "high", "notable", "routine")
VERIFICATIONS = (
    "multi-source",
    "single-source",
    "single-source-national-cert",
    "single-source-victim",
    "contradicted",
)
CONFIDENCES = ("high", "medium", "low")
RUN_KINDS = ("intel", "weekly")
ENTITY_TYPES = ("actor", "campaign", "malware", "tool", "incident", "report", "trend", "policy")
SOURCE_ROLES = ("primary", "corroborating")

# Which daily-brief render section a kind maps to (operational horizon).
# Orthogonal overrides at render time: update_of -> "updates",
# deep_dive -> "deep-dive". Strategic-only kinds map to None for the
# daily view and are rendered by the weekly structure instead.
KIND_DAILY_SECTION = {
    "threat": "active-threats",
    "incident": "active-threats",
    "vulnerability": "trending-vulnerabilities",
    "research": "research",
    "annual-report": "research",
    "policy": None,
    "synthesis": None,
    "outlook": None,
}

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,59}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
RUN_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9:TZ-]{3,63}$")
ENTITY_KEY_RE = re.compile(
    r"^(actor|campaign|malware|tool|incident|report|trend|policy):[a-z0-9][a-z0-9-]{0,79}$"
)
ENTRY_ID_RE = re.compile(r"^\d{4}-\d{2}-\d{2}/[a-z0-9][a-z0-9-]{0,59}$")
CVE_ID_RE = re.compile(r"^CVE-\d{4}-\d{4,7}$")
# MITRE ATT&CK technique id (entry `techniques[]`) — T#### or T####.###
TECHNIQUE_ID_RE = re.compile(r"^T\d{4}(\.\d{3})?$")


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


# ---------------------------------------------------------------------------
# Strict YAML-subset parser
# ---------------------------------------------------------------------------


class YamlSubsetError(ValueError):
    """Raised when a document steps outside the supported YAML subset."""


_BOOL_NULL = {"null": None, "~": None, "true": True, "false": False}
_INT_RE = re.compile(r"^-?\d+$")
_FLOAT_RE = re.compile(r"^-?\d+\.\d+$")


def _parse_scalar(token: str):
    token = token.strip()
    if token == "":
        return None
    if token.startswith('"') and token.endswith('"') and len(token) >= 2:
        return token[1:-1].replace('\\"', '"')
    if token.startswith("'") and token.endswith("'") and len(token) >= 2:
        return token[1:-1].replace("''", "'")
    low = token.lower()
    if low in _BOOL_NULL:
        return _BOOL_NULL[low]
    if _INT_RE.match(token):
        try:
            return int(token)
        except ValueError:
            return token
    if _FLOAT_RE.match(token):
        try:
            return float(token)
        except ValueError:
            return token
    return token


def _split_inline_items(inner: str) -> list:
    """Split a flow collection body on top-level commas (quote-aware)."""
    items, buf, quote = [], [], None
    for ch in inner:
        if quote:
            buf.append(ch)
            if ch == quote:
                quote = None
            continue
        if ch in ("'", '"'):
            quote = ch
            buf.append(ch)
            continue
        if ch in "[]{}":
            raise YamlSubsetError("nested flow collections are not supported")
        if ch == ",":
            items.append("".join(buf))
            buf = []
            continue
        buf.append(ch)
    tail = "".join(buf).strip()
    if tail or items:
        items.append("".join(buf))
    return [i.strip() for i in items if i.strip() != ""]


def _parse_flow(token: str):
    token = token.strip()
    if token == "[]":
        return []
    if token == "{}":
        return {}
    if token.startswith("[") and token.endswith("]"):
        return [_parse_scalar(i) for i in _split_inline_items(token[1:-1])]
    if token.startswith("{") and token.endswith("}"):
        out = {}
        for item in _split_inline_items(token[1:-1]):
            if ":" not in item:
                raise YamlSubsetError(f"flow mapping item without colon: {item!r}")
            k, _, v = item.partition(":")
            out[k.strip()] = _parse_scalar(v)
        return out
    return None


def _parse_value_token(token: str):
    token = token.strip()
    flow = _parse_flow(token)
    if flow is not None or token in ("[]", "{}"):
        return flow
    return _parse_scalar(token)


class _Lines:
    def __init__(self, text: str):
        self.raw = text.splitlines()
        self.items = []  # (indent, content, lineno)
        for n, line in enumerate(self.raw, start=1):
            if "\t" in line:
                raise YamlSubsetError(f"line {n}: tabs are not allowed")
            stripped = line.strip()
            if stripped == "" or stripped.startswith("#"):
                continue
            indent = len(line) - len(line.lstrip(" "))
            self.items.append((indent, line.strip(), n, line))
        self.pos = 0

    def peek(self):
        return self.items[self.pos] if self.pos < len(self.items) else None

    def next(self):
        item = self.items[self.pos]
        self.pos += 1
        return item


def _collect_block_scalar(lines: _Lines, parent_indent: int, style: str) -> str:
    """Collect a `>` (folded) or `|` (literal) block scalar's raw lines."""
    collected = []
    while True:
        nxt = lines.peek()
        if nxt is None or nxt[0] <= parent_indent:
            break
        indent, _stripped, _n, raw = lines.next()
        collected.append(raw)
    if not collected:
        return ""
    base = min(len(l) - len(l.lstrip(" ")) for l in collected if l.strip())
    body = [l[base:] if len(l) >= base else "" for l in collected]
    if style == "|":
        return "\n".join(body).rstrip("\n")
    # folded: blank line -> newline, otherwise join with single space
    out, para = [], []
    for l in body:
        if l.strip() == "":
            if para:
                out.append(" ".join(para))
                para = []
        else:
            para.append(l.strip())
    if para:
        out.append(" ".join(para))
    return "\n".join(out).strip()


def _parse_block(lines: _Lines, indent: int):
    """Parse a block (mapping or list) whose entries sit at `indent`."""
    first = lines.peek()
    if first is None:
        return None
    if first[1].startswith("- "):
        return _parse_list(lines, indent)
    if first[1] == "-":
        return _parse_list(lines, indent)
    return _parse_mapping(lines, indent)


def _parse_mapping(lines: _Lines, indent: int) -> dict:
    out = {}
    while True:
        nxt = lines.peek()
        if nxt is None or nxt[0] < indent:
            break
        if nxt[0] > indent:
            raise YamlSubsetError(f"line {nxt[2]}: unexpected indentation")
        if nxt[1].startswith("- ") or nxt[1] == "-":
            raise YamlSubsetError(f"line {nxt[2]}: list item inside a mapping block")
        _i, content, n, _raw = lines.next()
        m = re.match(r"^([^:#]+?):(?:\s+(.*))?$", content)
        if not m:
            raise YamlSubsetError(f"line {n}: expected `key: value`, got {content!r}")
        key = m.group(1).strip().strip('"').strip("'")
        rest = (m.group(2) or "").strip()
        if rest == "":
            nxt2 = lines.peek()
            if nxt2 is not None and nxt2[0] > indent:
                out[key] = _parse_block(lines, nxt2[0])
            else:
                out[key] = None
        elif rest in (">", "|", ">-", "|-"):
            out[key] = _collect_block_scalar(lines, indent, rest[0])
        else:
            out[key] = _parse_value_token(rest)
    return out


def _parse_list(lines: _Lines, indent: int) -> list:
    out = []
    while True:
        nxt = lines.peek()
        if nxt is None or nxt[0] < indent:
            break
        if nxt[0] > indent:
            raise YamlSubsetError(f"line {nxt[2]}: unexpected indentation in list")
        if not (nxt[1].startswith("- ") or nxt[1] == "-"):
            break
        _i, content, n, _raw = lines.next()
        inner = content[1:].strip()  # after the dash
        if inner == "":
            nxt2 = lines.peek()
            if nxt2 is not None and nxt2[0] > indent:
                out.append(_parse_block(lines, nxt2[0]))
            else:
                out.append(None)
            continue
        m = re.match(r"^([^:#]+?):(?:\s+(.*))?$", inner)
        if m and not inner.startswith(("'", '"', "[", "{")):
            # `- key: value` mapping item; continuation keys sit indented
            # deeper than the dash column.
            item = {}
            key = m.group(1).strip().strip('"').strip("'")
            rest = (m.group(2) or "").strip()
            if rest in (">", "|", ">-", "|-"):
                item[key] = _collect_block_scalar(lines, indent + 1, rest[0])
            elif rest == "":
                nxt2 = lines.peek()
                if nxt2 is not None and nxt2[0] > indent + 1:
                    item[key] = _parse_block(lines, nxt2[0])
                else:
                    item[key] = None
            else:
                item[key] = _parse_value_token(rest)
            nxt2 = lines.peek()
            if nxt2 is not None and nxt2[0] > indent and not (
                nxt2[1].startswith("- ") or nxt2[1] == "-"
            ):
                rest_map = _parse_mapping(lines, nxt2[0])
                item.update(rest_map)
            out.append(item)
        else:
            out.append(_parse_value_token(inner))
    return out


def parse_yaml_subset(text: str):
    """Parse a strict-subset YAML document into Python primitives."""
    lines = _Lines(text)
    if lines.peek() is None:
        return {}
    value = _parse_block(lines, lines.peek()[0])
    leftover = lines.peek()
    if leftover is not None:
        raise YamlSubsetError(f"line {leftover[2]}: trailing content outside document")
    return value


# ---------------------------------------------------------------------------
# Serialiser (emits the same subset the parser accepts — round-trip safe)
# ---------------------------------------------------------------------------

_PLAIN_SCALAR_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 _./+()&≤≥§·—–-]*$")


def _needs_quotes(s: str) -> bool:
    if s == "":
        return True
    low = s.lower()
    if low in _BOOL_NULL or _INT_RE.match(s) or _FLOAT_RE.match(s):
        return True
    if s != s.strip():
        return True
    if any(ch in s for ch in (":", "#", '"', "'", "[", "]", "{", "}", ",", "\n")):
        return True
    if s.startswith(("-", ">", "|", "*", "&", "!", "%", "@", "`", "?")):
        return True
    return not _PLAIN_SCALAR_RE.match(s)


def _dump_scalar(value) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)):
        return str(value)
    s = str(value)
    if _needs_quotes(s):
        return '"' + s.replace('"', '\\"') + '"'
    return s


def _dump_block(value, indent: int, out: list) -> None:
    pad = "  " * indent
    if isinstance(value, dict):
        if not value:
            out[-1] += " {}"
            return
        for k, v in value.items():
            if isinstance(v, str) and "\n" in v:
                out.append(f"{pad}{k}: |")
                for line in v.split("\n"):
                    out.append(f"{pad}  {line}" if line else "")
            elif isinstance(v, dict) and v:
                out.append(f"{pad}{k}:")
                _dump_block(v, indent + 1, out)
            elif isinstance(v, list) and v:
                out.append(f"{pad}{k}:")
                _dump_block(v, indent + 1, out)
            elif isinstance(v, list):
                out.append(f"{pad}{k}: []")
            elif isinstance(v, dict):
                out.append(f"{pad}{k}: {{}}")
            else:
                out.append(f"{pad}{k}: {_dump_scalar(v)}")
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, dict) and item:
                keys = list(item.keys())
                first_k = keys[0]
                first_v = item[first_k]
                if isinstance(first_v, (dict, list)) and first_v:
                    out.append(f"{pad}- {first_k}:")
                    _dump_block(first_v, indent + 2, out)
                elif isinstance(first_v, str) and "\n" in first_v:
                    out.append(f"{pad}- {first_k}: |")
                    for line in first_v.split("\n"):
                        out.append(f"{pad}    {line}" if line else "")
                else:
                    if isinstance(first_v, list):
                        out.append(f"{pad}- {first_k}: []")
                    elif isinstance(first_v, dict):
                        out.append(f"{pad}- {first_k}: {{}}")
                    else:
                        out.append(f"{pad}- {first_k}: {_dump_scalar(first_v)}")
                rest = {k: item[k] for k in keys[1:]}
                if rest:
                    _dump_block(rest, indent + 1, out)
            elif isinstance(item, list):
                raise YamlSubsetError("cannot serialise a list nested directly in a list")
            else:
                out.append(f"{pad}- {_dump_scalar(item)}")
    else:
        out.append(f"{pad}{_dump_scalar(value)}")


def dump_yaml_subset(value) -> str:
    """Serialise Python primitives into the strict YAML subset."""
    out: list = []
    _dump_block(value, 0, out)
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Frontmatter documents
# ---------------------------------------------------------------------------

_FM_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.DOTALL)


def split_frontmatter(text: str):
    """Split a document into (frontmatter_text, body). Raises on missing FM."""
    m = _FM_RE.match(text)
    if not m:
        raise YamlSubsetError("document does not start with a `---` frontmatter block")
    return m.group(1), m.group(2).lstrip("\n")


def compose_frontmatter_doc(frontmatter: dict, body: str) -> str:
    """Serialise a frontmatter dict + Markdown body into a document."""
    return "---\n" + dump_yaml_subset(frontmatter) + "---\n\n" + body.strip() + "\n"


# ---------------------------------------------------------------------------
# Taxonomy (same file format as v2 — flat keys with `- value` lists)
# ---------------------------------------------------------------------------


def parse_taxonomy(path: Path = TAXONOMY_PATH) -> dict:
    """Parse site/taxonomy.yaml into {key: set(values)}."""
    tax: dict = {}
    current = None
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        m = re.match(r"^([a-z_]+):\s*$", line)
        if m:
            current = m.group(1)
            tax[current] = set()
            continue
        m = re.match(r"^\s+-\s+(.+)$", line)
        if m and current:
            tax[current].add(m.group(1).strip())
    return tax


# ---------------------------------------------------------------------------
# Entry loading
# ---------------------------------------------------------------------------

ENTRY_DEFAULTS = {
    "horizon": "operational",
    "priority": "notable",
    "immediate_action": None,
    "event_date": None,
    "tags": [],
    "regions": [],
    "sectors": [],
    "entities": [],
    "cves": [],
    "sources": [],
    "closed_sources": [],
    "evidence": [],
    "verification": "multi-source",
    "sourcing_note": None,
    "confidence": "high",
    "update_of": None,
    "references": [],
    "weekly_section": None,
    "deep_dive": False,
    "deep_dive_category": None,
    "org_triage": None,
    "classification": None,
    "watchlist_hit": False,
    "actions": [],
    "migrated_from": None,
}

ENTRY_REQUIRED = ("schema", "kind", "title", "headline", "summary", "discovered_at", "run_id")


def load_entry(path: Path, root: Path = ROOT) -> dict:
    """Load one entry file into a dict: frontmatter fields + id/date/slug/path/body."""
    text = path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(text)
    fm = parse_yaml_subset(fm_text)
    if not isinstance(fm, dict):
        raise YamlSubsetError(f"{path}: frontmatter is not a mapping")
    entry = dict(ENTRY_DEFAULTS)
    entry.update(fm)
    entry["slug"] = path.stem
    entry["date"] = path.parent.name
    entry["id"] = f"{entry['date']}/{entry['slug']}"
    entry["path"] = str(path.relative_to(root)) if path.is_relative_to(root) else str(path)
    entry["body"] = body
    return entry


def collect_entries(entries_dir: Path = ENTRIES_DIR, root: Path = ROOT) -> list:
    """Load every entry, sorted by (discovered_at, id) ascending."""
    entries = []
    if not entries_dir.is_dir():
        return entries
    for day_dir in sorted(entries_dir.iterdir()):
        if not day_dir.is_dir() or not DATE_RE.match(day_dir.name):
            continue
        for path in sorted(day_dir.glob("*.md")):
            entries.append(load_entry(path, root=root))
    entries.sort(key=lambda e: (str(e.get("discovered_at") or ""), e["id"]))
    return entries


def entries_in_window(entries: list, since: datetime, until: datetime | None = None) -> list:
    """Filter entries whose discovered_at falls in [since, until)."""
    out = []
    for e in entries:
        ts = parse_ts(e.get("discovered_at"))
        if ts is None:
            continue
        if ts >= since and (until is None or ts < until):
            out.append(e)
    return out


def parse_ts(value) -> datetime | None:
    if not value or not isinstance(value, str):
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


def classification_code(entry: dict) -> str:
    """Render an entry's intelligence classification as a single token, e.g.
    reliability `B` + credibility `2` -> ``B2``. Empty string when the entry
    carries no `classification` block (vulnerability-kind entries use
    `org_triage` instead)."""
    c = entry.get("classification")
    if not isinstance(c, dict):
        return ""
    rel = str(c.get("reliability") or "").strip()
    cred = str(c.get("credibility") if c.get("credibility") is not None else "").strip()
    return f"{rel}{cred}"


# ---------------------------------------------------------------------------
# Registry loading
# ---------------------------------------------------------------------------


def load_registry(path: Path = REGISTRY_PATH) -> dict:
    """Load entities/registry.yaml → {key: entity-dict}."""
    if not path.exists():
        return {}
    doc = parse_yaml_subset(path.read_text(encoding="utf-8"))
    if not isinstance(doc, dict):
        raise YamlSubsetError(f"{path}: registry document is not a mapping")
    out = {}
    for ent in doc.get("entities") or []:
        if isinstance(ent, dict) and ent.get("key"):
            out[ent["key"]] = ent
    return out


# ---------------------------------------------------------------------------
# Run-record loading
# ---------------------------------------------------------------------------


def load_run_record(path: Path, root: Path = ROOT) -> dict:
    text = path.read_text(encoding="utf-8")
    fm_text, body = split_frontmatter(text)
    fm = parse_yaml_subset(fm_text)
    if not isinstance(fm, dict):
        raise YamlSubsetError(f"{path}: run-record frontmatter is not a mapping")
    fm["body"] = body
    fm["date_dir"] = path.parent.name
    fm["path"] = str(path.relative_to(root)) if path.is_relative_to(root) else str(path)
    if not fm.get("run_id"):
        fm["run_id"] = path.stem
    return fm


def collect_runs(runs_dir: Path = RUNS_DIR, root: Path = ROOT) -> list:
    """Load every run record, sorted by (started, run_id) ascending."""
    runs = []
    if not runs_dir.is_dir():
        return runs
    for day_dir in sorted(runs_dir.iterdir()):
        if not day_dir.is_dir() or not DATE_RE.match(day_dir.name):
            continue
        for path in sorted(day_dir.glob("*.md")):
            runs.append(load_run_record(path, root=root))
    runs.sort(key=lambda r: (str(r.get("started") or ""), str(r.get("run_id"))))
    return runs


# ---------------------------------------------------------------------------
# Schema validation (structural — URL liveness / dedup / budgets live in
# tools/check_run.py; this layer is what site/build.py also enforces)
# ---------------------------------------------------------------------------


def _is_str(v) -> bool:
    return isinstance(v, str) and v.strip() != ""


def _is_str_list(v) -> bool:
    return isinstance(v, list) and all(isinstance(i, str) for i in v)


def validate_entry(entry: dict, taxonomy: dict, registry_keys=None) -> list:
    """Return a list of human-readable schema errors (empty = valid)."""
    errs = []
    eid = entry.get("id", "<unknown>")

    def err(msg):
        errs.append(f"{eid}: {msg}")

    if entry.get("schema") != ENTRY_SCHEMA_VERSION:
        err(f"schema must be {ENTRY_SCHEMA_VERSION}")
    for field in ENTRY_REQUIRED:
        if field == "schema":
            continue
        if not _is_str(entry.get(field)) and not isinstance(entry.get(field), int):
            err(f"required field `{field}` missing or empty")
    if entry.get("kind") not in KINDS:
        err(f"kind {entry.get('kind')!r} not in {KINDS}")
    if entry.get("horizon") not in HORIZONS:
        err(f"horizon {entry.get('horizon')!r} not in {HORIZONS}")
    if entry.get("priority") not in PRIORITIES:
        err(f"priority {entry.get('priority')!r} not in {PRIORITIES}")
    if entry.get("verification") not in VERIFICATIONS:
        err(f"verification {entry.get('verification')!r} not in {VERIFICATIONS}")
    if entry.get("confidence") not in CONFIDENCES:
        err(f"confidence {entry.get('confidence')!r} not in {CONFIDENCES}")

    slug = entry.get("slug", "")
    if not SLUG_RE.match(slug or ""):
        err(f"slug {slug!r} must match {SLUG_RE.pattern}")
    if not DATE_RE.match(entry.get("date") or ""):
        err("folder date is not YYYY-MM-DD")
    ts = parse_ts(entry.get("discovered_at"))
    if ts is None:
        err("discovered_at is not a UTC ISO 8601 `YYYY-MM-DDTHH:MM:SSZ` timestamp")
    elif entry.get("date") and ts.strftime("%Y-%m-%d") != entry["date"]:
        err(f"folder date {entry['date']} != discovered_at date {ts.strftime('%Y-%m-%d')}")
    if entry.get("event_date") is not None and not DATE_RE.match(str(entry["event_date"])):
        err("event_date must be YYYY-MM-DD or null")

    headline = entry.get("headline") or ""
    if len(headline) > 160:
        err(f"headline is {len(headline)} chars (max 160)")

    # priority <-> immediate_action consistency
    ia = entry.get("immediate_action")
    if entry.get("priority") == "critical" and not isinstance(ia, dict):
        err("priority critical requires an immediate_action block")
    if isinstance(ia, dict):
        if entry.get("priority") != "critical":
            err("immediate_action present but priority is not critical")
        if not _is_str(ia.get("title")) or not _is_str(ia.get("action")):
            err("immediate_action requires `title` and `action`")

    # taxonomy-controlled vocab
    themes = taxonomy.get("themes", set()) | taxonomy.get("nexus", set())
    for t in entry.get("tags") or []:
        if t not in themes:
            err(f"tag {t!r} not in taxonomy themes/nexus")
    if not entry.get("tags"):
        err("at least one tag required")
    for r in entry.get("regions") or []:
        if r not in taxonomy.get("regions", set()):
            err(f"region {r!r} not in taxonomy regions")
    if not entry.get("regions"):
        err("at least one region required")
    for s in entry.get("sectors") or []:
        if s not in taxonomy.get("sectors", set()):
            err(f"sector {s!r} not in taxonomy sectors")

    # entities
    for key in entry.get("entities") or []:
        if not isinstance(key, str) or not ENTITY_KEY_RE.match(key):
            err(f"entity key {key!r} is not `<type>:<slug>`")
        elif registry_keys is not None and key not in registry_keys:
            err(f"entity key {key!r} not present in entities/registry.yaml")

    # machine-readable triage layer (optional fields; strict when present)
    for t in entry.get("techniques") or []:
        if not isinstance(t, str) or not TECHNIQUE_ID_RE.match(t):
            err(f"techniques value {t!r} is not an ATT&CK technique id (T#### or T####.###)")
    for p in entry.get("affected_products") or []:
        if not _is_str(p):
            err(f"affected_products value {p!r} is not a non-empty string")

    # CVE records
    for cve in entry.get("cves") or []:
        if not isinstance(cve, dict):
            err(f"cves[] item is not a mapping: {cve!r}")
            continue
        cid = cve.get("id") or ""
        if not CVE_ID_RE.match(str(cid)):
            err(f"cve id {cid!r} is not CVE-YYYY-NNNN…")
        if cve.get("type") is not None and cve.get("type") not in taxonomy.get("cve_types", set()):
            err(f"{cid}: cve type {cve.get('type')!r} not in taxonomy cve_types")
        if cve.get("vector") not in taxonomy.get("cve_vectors", set()):
            err(f"{cid}: vector {cve.get('vector')!r} not in taxonomy cve_vectors")
        if cve.get("auth") not in taxonomy.get("cve_auth", set()):
            err(f"{cid}: auth {cve.get('auth')!r} not in taxonomy cve_auth")
        status = cve.get("status")
        if not isinstance(status, list) or not status:
            err(f"{cid}: status must be a non-empty list")
        else:
            for st in status:
                if st not in taxonomy.get("cve_status", set()):
                    err(f"{cid}: status {st!r} not in taxonomy cve_status")

    # sources
    sources = entry.get("sources") or []
    closed = entry.get("closed_sources") or []
    if not sources and not closed:
        err("entry has neither sources nor closed_sources")
    for i, s in enumerate(sources):
        if not isinstance(s, dict):
            err(f"sources[{i}] is not a mapping")
            continue
        url = s.get("url") or ""
        if not isinstance(url, str) or not url.startswith(("http://", "https://")):
            err(f"sources[{i}].url {url!r} is not an http(s) URL")
        if not _is_str(s.get("publisher")):
            err(f"sources[{i}].publisher missing")
        if s.get("role") not in SOURCE_ROLES:
            err(f"sources[{i}].role {s.get('role')!r} not in {SOURCE_ROLES}")
    if sources and sources[0].get("role") != "primary":
        err("first source must have role: primary")
    for i, c in enumerate(closed):
        if not isinstance(c, dict) or not _is_str(c.get("title")) or not _is_str(c.get("provider")):
            err(f"closed_sources[{i}] requires title + provider")
        # No TLP validation or gating: this pipeline never filters on TLP.
        # Everything the agents can read (including intel/) is fair game; a
        # `tlp` key on a legacy drop is an ignored provenance annotation.

    # single-source consistency
    if len(sources) <= 1 and not closed and entry.get("verification") == "multi-source":
        err("verification: multi-source with fewer than 2 sources")

    # evidence
    for i, ev in enumerate(entry.get("evidence") or []):
        if not isinstance(ev, dict) or not _is_str(ev.get("quote")) or not _is_str(ev.get("publisher")):
            err(f"evidence[{i}] requires quote + publisher")
    needs_evidence = isinstance(ia, dict) or any(
        isinstance(c, dict) and "exploited" in (c.get("status") or [])
        for c in entry.get("cves") or []
    )
    if needs_evidence and not entry.get("evidence"):
        err("evidence[] required (immediate_action or exploited-status CVE)")

    # update / reference links
    upd = entry.get("update_of")
    if upd is not None and not ENTRY_ID_RE.match(str(upd)):
        err(f"update_of {upd!r} is not an entry id (YYYY-MM-DD/slug)")
    for ref in entry.get("references") or []:
        if not ENTRY_ID_RE.match(str(ref)):
            err(f"references value {ref!r} is not an entry id")

    if entry.get("deep_dive") and not _is_str(entry.get("deep_dive_category")):
        err("deep_dive: true requires deep_dive_category")

    ws = entry.get("weekly_section")
    if ws is not None:
        if ws not in WEEKLY_SECTIONS:
            err(f"weekly_section {ws!r} not in {WEEKLY_SECTIONS}")
        if entry.get("horizon") != "strategic":
            err("weekly_section is only valid on horizon: strategic entries")

    ot = entry.get("org_triage")
    if ot is not None and (not isinstance(ot, dict) or not _is_str(ot.get("category"))):
        err("org_triage must be null or {category, rationale}")

    # classification — structural only (reliability letter + credibility
    # number). Which entry kinds require it and the code vocabulary itself are
    # config-driven and enforced by tools/check_run.py against the org profile
    # (the same split as org_triage), so this layer stays profile-agnostic.
    cls = entry.get("classification")
    if cls is not None:
        if not isinstance(cls, dict):
            err("classification must be null or {reliability, credibility}")
        else:
            if not _is_str(cls.get("reliability")):
                err("classification.reliability missing (source-reliability code)")
            cred = cls.get("credibility")
            if not (_is_str(cred) or isinstance(cred, int)):
                err("classification.credibility missing (information-credibility code)")

    for i, a in enumerate(entry.get("actions") or []):
        if not _is_str(a):
            err(f"actions[{i}] must be a non-empty string")

    if not _is_str(entry.get("body")):
        err("entry body is empty")
    return errs


def validate_registry(registry: dict) -> list:
    """Validate the loaded registry ({key: entity}); returns error list."""
    errs = []
    seen_names: dict = {}
    for key, ent in registry.items():
        if not ENTITY_KEY_RE.match(key):
            errs.append(f"registry key {key!r} is not `<type>:<kebab-slug>`")
            continue
        etype = key.split(":", 1)[0]
        if ent.get("type") != etype:
            errs.append(f"{key}: type {ent.get('type')!r} does not match key prefix")
        if not _is_str(ent.get("name")):
            errs.append(f"{key}: name missing")
        if not _is_str(ent.get("summary")):
            errs.append(f"{key}: summary missing")
        aliases = ent.get("aliases")
        if aliases is not None and not _is_str_list(aliases):
            errs.append(f"{key}: aliases must be a list of strings")
        for label in [ent.get("name")] + list(aliases or []):
            if not isinstance(label, str):
                continue
            norm = label.strip().lower()
            if norm in seen_names and seen_names[norm] != key:
                errs.append(
                    f"{key}: name/alias {label!r} collides with {seen_names[norm]}"
                )
            seen_names.setdefault(norm, key)
    return errs


RUN_REQUIRED = ("schema", "run_id", "kind", "date", "started", "completed", "prompt_version")


def validate_run_record(run: dict) -> list:
    errs = []
    rid = run.get("run_id", "<unknown>")

    def err(msg):
        errs.append(f"run {rid}: {msg}")

    if run.get("schema") != RUN_SCHEMA_VERSION:
        err(f"schema must be {RUN_SCHEMA_VERSION}")
    for field in RUN_REQUIRED:
        if field == "schema":
            continue
        if not _is_str(str(run.get(field) or "")):
            err(f"required field `{field}` missing")
    if run.get("kind") not in RUN_KINDS:
        err(f"kind {run.get('kind')!r} not in {RUN_KINDS}")
    if not DATE_RE.match(str(run.get("date") or "")):
        err("date is not YYYY-MM-DD")
    if run.get("date_dir") and run.get("date") and run["date_dir"] != run["date"]:
        err(f"folder date {run['date_dir']} != date {run['date']}")
    for f in ("entries_published", "entries_updated", "verification_iterations",
              "verification_residual_count"):
        if not isinstance(run.get(f), int):
            err(f"`{f}` must be an integer")
    subs = run.get("sub_agents")
    if not isinstance(subs, dict) or not subs:
        err("sub_agents block missing or empty")
    ver = run.get("verification")
    iters = (ver or {}).get("iterations") if isinstance(ver, dict) else None
    if not isinstance(iters, list) or not iters:
        err("verification.iterations missing or empty")
    else:
        final = iters[-1]
        verdict = (final or {}).get("verdict")
        if verdict not in ("CLEAN", "NEEDS_FIXES"):
            err(f"final verification verdict {verdict!r} must be CLEAN or NEEDS_FIXES")
        residual = run.get("verification_residual_count")
        if isinstance(residual, int) and verdict == "NEEDS_FIXES":
            expect = int(final.get("truth") or 0) + int(final.get("editorial") or 0)
            if residual != expect:
                err(
                    f"verification_residual_count {residual} != final truth+editorial {expect}"
                )
            if residual == 0 and expect != 0:
                err("residual count 0 on a NEEDS_FIXES final iteration")
        if isinstance(residual, int) and verdict == "CLEAN" and residual != 0:
            err("verification_residual_count must be 0 when final verdict is CLEAN")
    if not _is_str(run.get("body")):
        err("run record body (verification & coverage notes) is empty")
    return errs
