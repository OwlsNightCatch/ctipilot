#!/usr/bin/env python3
"""tools/check_run.py — the v3 mechanical self-check gate.

Replaces tools/check_brief.py for the per-finding entry pipeline
(docs/pipeline.md § "The mechanical gate"). The agent MUST run this script
after writing a run's entries + run record and before the verifier spawn and
before every commit. A non-zero exit is a hard stop on the publishing chain.

Usage:
    python3 tools/check_run.py                     # check the LATEST run (by `started`)
    python3 tools/check_run.py 2026-07-03T0412Z-intel   # check a specific run
    python3 tools/check_run.py --all               # validate the whole content store
    python3 tools/check_run.py --no-build-tests    # skip site/test_build.py
    python3 tools/check_run.py --no-link-check     # skip the live URL check (offline runs)
    python3 tools/check_run.py --root PATH         # resolve entries/runs/registry under PATH
                                                   # (state/sources/taxonomy stay in the repo;
                                                   # used by the self-test fixtures)

Exit codes:
    0   all checks passed (warnings allowed)
    1   one or more FAIL checks
    2   script-level error (no run records, unknown run id, content_model missing)

Scope model:
    A "run scope" is the run record `runs/<date>/<run-id>.md` plus every
    entry whose `run_id` matches. Historical entries and records (other
    run_ids) are loaded as *context* for the dedup / composition checks but are
    not re-validated strictly — EXCEPT in --all mode, where every entry gets
    schema validation and registry cross-checks (but never URL liveness:
    that would hammer hundreds of historical URLs) and run records carrying
    `migrated_from` get only a minimal parse/identity check.

Design rules (carried over from check_brief.py):
    - Stdlib-only. No third-party deps.
    - The parsing/validation layer is `site/content_model.py` — the single
      shared loader for entries, registry and run records — so this gate,
      site/build.py and tools/migrate_briefs.py can never drift on what a
      valid document is. If content_model is missing the script exits 2.
    - Output is line-by-line `PASS / FAIL / WARN  <check>: <detail>` so the
      agent can copy a failure verbatim into the run record's verification
      notes if it commits anyway.
    - The script never modifies any file. It is read-only. The agent fixes
      drift; this script reports it.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "site"
STATE_DIR = ROOT / "state"
SOURCES_JSON = ROOT / "sources" / "sources.json"
TAXONOMY = SITE_DIR / "taxonomy.yaml"
TEST_BUILD = SITE_DIR / "test_build.py"
CHANGELOG = ROOT / "prompts" / "CHANGELOG.md"
WORK_DIR = ROOT / "work"
INTEL_DIR = ROOT / "intel"

# --- Shared content model (the single parser/validator) --------------------

try:
    sys.path.insert(0, str(SITE_DIR))
    import content_model as cm
except Exception as _exc:  # pragma: no cover — hard dependency
    print(f"FATAL: cannot import site/content_model.py ({_exc}) — "
          "check_run.py builds on the shared loader and cannot run without it")
    sys.exit(2)

# --- Severity counters ------------------------------------------------------

FAILS: list[str] = []
WARNS: list[str] = []
PASSES: list[str] = []
ACKED: list[str] = []

# Acknowledged-warning ledger (v3.28 zero-warning discipline). A warning on
# settled, immutable history (a past run record's runaway duration; an
# era-correct confirmation waiver from the 5-cap era) cannot be "fixed"
# without falsifying the record — the weekly quality audit reviews each such
# warning and, when it is genuinely unfixable, acknowledges it here with a
# reason. Acknowledged warnings are reported separately and do not count as
# warnings, so `--all` can be held at zero. Discipline (enforced by prompt,
# reviewed in the audit): only the weekly audit adds entries, never a run
# for its own fresh warnings; `match` must pin the specific run/subject.
ACK_LEDGER_PATH = STATE_DIR / "warning_acknowledgments.json"
_ACK_LEDGER: list[dict] | None = None


def _ack_ledger() -> list[dict]:
    global _ACK_LEDGER
    if _ACK_LEDGER is None:
        _ACK_LEDGER = []
        try:
            data = json.loads(ACK_LEDGER_PATH.read_text(encoding="utf-8"))
            for rec in data.get("acknowledged", []):
                if (isinstance(rec, dict)
                        and str(rec.get("check") or "").strip()
                        and len(str(rec.get("match") or "").strip()) >= 12
                        and str(rec.get("reason") or "").strip()):
                    _ACK_LEDGER.append(rec)
                else:
                    fail("ack-ledger",
                         f"malformed acknowledgment record {rec!r} — needs "
                         "check, match (≥12 chars, pin the specific subject) "
                         "and reason")
        except FileNotFoundError:
            pass
        except Exception as exc:
            fail("ack-ledger",
                 f"{ACK_LEDGER_PATH.name} unreadable/malformed: {exc}")
    return _ACK_LEDGER


def _print(severity: str, label: str, detail: str = "") -> None:
    msg = f"  {severity:<4} {label}" + (f": {detail}" if detail else "")
    print(msg)


def fail(label: str, detail: str = "") -> None:
    FAILS.append(f"{label}: {detail}" if detail else label)
    _print("FAIL", label, detail)


def warn(label: str, detail: str = "") -> None:
    msg = f"{label}: {detail}" if detail else label
    for rec in _ack_ledger():
        if rec["check"] == label and str(rec["match"]) in msg:
            ACKED.append(
                f"{msg}  [acknowledged {rec.get('acknowledged_at', '?')}: "
                f"{rec['reason']}]")
            _print("ACK", label, detail)
            return
    WARNS.append(msg)
    _print("WARN", label, detail)


def ok(label: str, detail: str = "") -> None:
    PASSES.append(label)
    _print("PASS", label, detail)


# --- Ported constants -------------------------------------------------------
# Each block below is copied from tools/check_brief.py (the v2 gate) so this
# file is self-contained — check_brief.py is deleted once the migration
# lands, and importing from it would leave a dangling dependency.

CVE_RE = re.compile(r"CVE-\d{4}-\d{4,7}")

# v2 origin: check_brief.py CHANGELOG_HEAD_RE (~line 2192). The run record's
# `prompt_version` must match the most recent `## N.M —` heading.
CHANGELOG_HEAD_RE = re.compile(r"^##\s+(\d+\.\d+)\s+—", re.MULTILINE)

# v2 origin: check_brief.py BLOCKED_SOURCE_PATTERNS (~line 677).
# Sources that are NEVER acceptable in an entry's `sources[]` list. NVD and
# MITRE per-CVE pages are derived data sheets — the vendor PSIRT advisory or
# research-lab post is the primary disclosing source and must be cited
# instead. NVD/MITRE still appear automatically as "External references" on
# every per-CVE page in the build.
BLOCKED_SOURCE_PATTERNS: list[tuple[str, str, str]] = [
    # (host fragment, path regex, reason)
    ("nvd.nist.gov", r"^/vuln/detail/CVE-",
     "NVD per-CVE pages are derived data sheets — cite the vendor advisory or research blog instead"),
    ("cve.mitre.org", r"^/cgi-bin/cvename\.cgi",
     "MITRE per-CVE pages are derived data sheets — cite the vendor advisory or research blog instead"),
    ("cve.org", r"^/CVERecord",
     "cve.org per-CVE pages are derived data sheets — cite the vendor advisory or research blog instead"),
]

# v2 origin: check_brief.py BLOCKED_LANDING_PATTERNS (~line 690).
# Generic landing / category / index pages — never an acceptable source.
# A source must be a specific article / advisory / blog post / regulator
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

    v2 origin: check_brief.py `_host_path` (~line 720), incl. the carve-out:

    SPA hash-router carve-out: when the actual URL path is empty/root and
    the fragment looks like a route (starts with `/`), treat the fragment
    as the meaningful path. NCSC-CH's Cyber Security Hub is the canonical
    case — `tools/fetch_source.py` synthesises citation URLs of the form
    `https://security-hub.ncsc.admin.ch/#/posts/12551` because that is the
    public, human-readable post page; the JSON-only `/api/posts/.../details`
    endpoint is the fetch URL, not the citation. Without this carve-out the
    homepage regex `^/?$` for `ncsc.admin.ch` flags every Hub citation."""
    try:
        u = urlsplit(url)
        path = u.path or "/"
        if path in ("", "/") and u.fragment.startswith("/"):
            path = u.fragment
        return u.netloc.lower(), path
    except Exception:
        return "", ""


# v2 origin: check_brief.py NEWS_AGGREGATOR_HOSTS (~line 872).
# News-aggregator host allowlist for the "aggregator-only sourcing" warning.
# These are reputable news outlets per `sources.json`, but they aggregate
# primary research and should NOT be the only sources backing an entry. An
# entry whose sources are ≥2 URLs all from this list meets the literal
# two-source bar but lacks any primary disclosure — flag it so the run
# record carries the reduced-confidence framing instead of silently
# accepting.
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
                           # "labs"/"threat-intel" half as primary.
)


def _host_is_aggregator(host: str) -> bool:
    h = (host or "").lower()
    return any(h == a or h.endswith("." + a) for a in NEWS_AGGREGATOR_HOSTS)


# v2 origin: check_brief.py NATIONAL_CERT_HOSTS (~lines 972-981).
# The national-CERT carve-out hosts — the editorial policy treats these as
# primary disclosing parties for their own jurisdiction; a single source
# from this set is `verification: single-source-national-cert`, not plain
# `single-source`.
NATIONAL_CERT_HOSTS: tuple[str, ...] = (
    "ncsc.admin.ch", "ncsc.ch", "govcert.ch",
    "cert.europa.eu", "enisa.europa.eu",
    "bsi.bund.de", "wid.cert-bund.de", "cert.ssi.gouv.fr",
    "ncsc.gov.uk", "ncsc.nl", "advisories.ncsc.nl",
    "cisa.gov", "www.cisa.gov",
    # Joint US advisories are frequently reachable only from a co-sealing
    # agency's host while cisa.gov itself refuses the routine transports.
    # Same disclosing parties, same document — added 2026-08-20 after the
    # five-agency Siemens S7 advisory was retrievable only from the FBI
    # mirror and cert.lv carried an EU member-state authority's own bulletin.
    "ic3.gov", "www.ic3.gov", "media.defense.gov", "nsa.gov", "www.nsa.gov",
    "cert.lv",
    "csirt.gov.it", "agid.gov.it", "acn.gov.it",
    "cert.at", "govcert.gv.at", "cert.pl", "ccn-cert.cni.es",
    "ccb.belgium.be", "safeonweb.be",
    "jpcert.or.jp",
    "cert.gov.ua",
)


def _host_is_national_cert(host: str) -> bool:
    h = (host or "").lower()
    return any(h == c or h.endswith("." + c) for c in NATIONAL_CERT_HOSTS)


# v2 origin: check_brief.py KNOWN_UA_BLOCKED (~line 1208).
# Hosts that reliably 403 the default UA but are otherwise alive — we treat
# 403/429 from these as PASS during the liveness check, since the agent is
# expected to use tools/fetch_source.py for them. A 403 here NEVER demotes
# the entry: the WAF is filtering this check container's UA, not telling us
# the content is gone.
KNOWN_UA_BLOCKED: tuple[str, ...] = (
    "www.cisa.gov", "cisa.gov", "ncsc.admin.ch", "www.ncsc.admin.ch",
    "talosintelligence.com", "blog.talosintelligence.com",
    "csirt-italia.it", "www.csirt-italia.it",
    "prodaft.com", "www.prodaft.com",
    "inside-it.ch", "www.inside-it.ch",
    "ico.org.uk", "www.ico.org.uk",
)

# v2 origin: check_brief.py BRIDGE_REQUIRED_SOURCE_IDS (~lines 1319-1331).
# Bridge-allowlist source-id matchers. Source ids in sources.json are stable
# strings; here we list the substrings that identify a bridge-allowlisted
# source (case-insensitive substring match against the lowered source id).
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

# v2 origin: check_brief.py RICH_FAILURE_REQUIRED_KEYS (~line 1334).
# Required keys in the rich `fetch_failures` entry shape.
RICH_FAILURE_REQUIRED_KEYS = (
    "id", "url_tried", "fetch_method", "status_code",
    "error_class", "attempted_methods", "mitigation_applied",
    "covered_anyway",
)


def _failure_id_is_bridge_allowlisted(sid: str) -> bool:
    """True iff this source id should be fetched via the bridge."""
    s = (sid or "").lower()
    return any(needle in s for needle in BRIDGE_REQUIRED_SOURCE_IDS)


# Taxonomy keys the gate requires (v2 set + cve_types, which the structured
# per-entry cves[] records now reference directly).
TAXONOMY_REQUIRED_KEYS = {
    "themes", "sectors", "regions", "cve_types", "cve_vectors", "cve_auth", "cve_status",
}


# --- Tolerant collectors ----------------------------------------------------
# cm.collect_entries / cm.collect_runs raise on the first malformed file,
# which would turn one bad frontmatter block into an exit-2 crash of the
# whole gate. The gate's job is to REPORT the bad file as a FAIL and keep
# checking everything else — pipeline.md: "check_run.py fails the commit on
# anything the parser rejects".


def collect_entries_tolerant(entries_dir: Path, root: Path) -> tuple[list[dict], list[str]]:
    entries: list[dict] = []
    errors: list[str] = []
    if not entries_dir.is_dir():
        return entries, errors
    for day_dir in sorted(entries_dir.iterdir()):
        if not day_dir.is_dir() or not cm.DATE_RE.match(day_dir.name):
            continue
        for path in sorted(day_dir.glob("*.md")):
            try:
                entries.append(cm.load_entry(path, root=root))
            except Exception as e:  # noqa: BLE001 — every parse error is a finding
                errors.append(f"{day_dir.name}/{path.name}: {e}")
    entries.sort(key=lambda e: (str(e.get("discovered_at") or ""), e["id"]))
    return entries, errors


def collect_runs_tolerant(runs_dir: Path, root: Path) -> tuple[list[dict], list[str]]:
    runs: list[dict] = []
    errors: list[str] = []
    if not runs_dir.is_dir():
        return runs, errors
    for day_dir in sorted(runs_dir.iterdir()):
        if not day_dir.is_dir() or not cm.DATE_RE.match(day_dir.name):
            continue
        for path in sorted(day_dir.glob("*.md")):
            try:
                runs.append(cm.load_run_record(path, root=root))
            except Exception as e:  # noqa: BLE001
                errors.append(f"{day_dir.name}/{path.name}: {e}")
    runs.sort(key=lambda r: (str(r.get("started") or ""), str(r.get("run_id"))))
    return runs, errors


# --- Store-level checks (always run) ----------------------------------------


def check_state_json_valid() -> dict[str, Any]:
    """`state/cves_seen.json` and `sources/sources.json` must parse (they are
    live inputs to cve-sync / sources-schema); `state/source_health.json` is
    parse-if-present (the weekly GH Action creates it — WARN when missing).
    Returns {filename: parsed_or_None}. The v2 covered_items / run_log /
    deep_dive_history files are retired in v3 (coverage and telemetry are
    derived from entries/ and runs/)."""
    parsed: dict[str, Any] = {}
    required = [STATE_DIR / "cves_seen.json", SOURCES_JSON]
    optional = [STATE_DIR / "source_health.json"]
    for p in required:
        rel = p.relative_to(ROOT)
        if not p.exists():
            fail("json-parse", f"{rel} missing")
            parsed[p.name] = None
            continue
        try:
            parsed[p.name] = json.loads(p.read_text(encoding="utf-8"))
            ok("json-parse", str(rel))
        except json.JSONDecodeError as e:
            fail("json-parse", f"{rel}: {e}")
            parsed[p.name] = None
    for p in optional:
        rel = p.relative_to(ROOT)
        if not p.exists():
            warn("json-parse", f"{rel} not present (created by the weekly source-health action)")
            parsed[p.name] = None
            continue
        try:
            parsed[p.name] = json.loads(p.read_text(encoding="utf-8"))
            ok("json-parse", str(rel))
        except json.JSONDecodeError as e:
            fail("json-parse", f"{rel}: {e}")
            parsed[p.name] = None
    return parsed


def check_taxonomy_loadable() -> dict[str, set]:
    if not TAXONOMY.exists():
        fail("taxonomy", f"{TAXONOMY.relative_to(ROOT)} missing")
        return {}
    try:
        tax = cm.parse_taxonomy(TAXONOMY)
    except Exception as e:  # noqa: BLE001
        fail("taxonomy", f"unparseable: {e}")
        return {}
    if not tax:
        fail("taxonomy", "no entries parsed")
        return {}
    missing = TAXONOMY_REQUIRED_KEYS - set(tax.keys())
    if missing:
        fail("taxonomy", f"missing keys: {sorted(missing)}")
    else:
        ok("taxonomy", f"{sum(len(v) for v in tax.values())} terms across {len(tax)} keys")
    return tax


def check_registry(registry_path: Path, entries: list | None = None) -> dict[str, dict]:
    """entities/registry.yaml loads and passes content_model.validate_registry
    (key format, type/prefix match, name+summary present, alias-collision
    detection, typed-relation vocabulary/endpoint constraints/canonical
    targets/duplicate edges/source-entry resolution). Every error is a FAIL —
    a broken registry breaks every entry's `entities:` resolution, the entity
    pages, and the threat graph downstream. Advisory layer: a curated edge
    whose source entry references neither endpoint in its `entities[]` WARNs
    (legal — the establishing entry may predate an endpoint's registration —
    but worth an operator's glance)."""
    rel = Path(*registry_path.parts[-2:])  # entities/registry.yaml, root-agnostic
    if not registry_path.exists():
        # A store with zero entities is legitimate on day one; entries that
        # reference entity keys will FAIL entry-schema instead.
        warn("registry", f"{rel} missing — every entries[].entities value will fail to resolve")
        return {}
    try:
        registry = cm.load_registry(registry_path)
    except Exception as e:  # noqa: BLE001
        fail("registry", f"{rel} unparseable: {e}")
        return {}
    entry_ids = {e["id"] for e in entries} if entries is not None else None
    errs = cm.validate_registry(registry, entry_ids=entry_ids)
    if errs:
        for e in errs:
            fail("registry", e)
    else:
        edges = cm.registry_relations(registry)
        ok("registry", f"{len(registry)} entit{'y' if len(registry) == 1 else 'ies'}, "
                       f"{len(edges)} curated relation(s), keys/aliases consistent")
    if entries is not None:
        by_id = {e["id"]: e for e in entries}

        # Generic words that carry no identity in an entity name — a match on
        # these alone never counts as a mention.
        _generic = {"breach", "ransomware", "incident", "campaign", "attack",
                    "data", "cloud", "leak", "site", "listing", "group",
                    "wave", "the", "and", "confirms", "corporate", "false",
                    "flag", "report", "analysis", "advisory", "disclosure"}

        def _mentions(en: dict, key: str, keys: set) -> bool:
            """Explicit entities[] key, or the entity's name/aliases appear in
            the entry text — full-label match, or ≥ half of the name's
            distinctive tokens (story-entities carry descriptive names that
            rarely appear verbatim)."""
            if key in keys:
                return True
            ent = registry.get(key) or {}
            raw = (str(en.get("title") or "") + " " + str(en.get("headline") or "")
                   + " " + str(en.get("body") or ""))
            hay = raw.lower()
            words = set(re.findall(r"[a-z0-9]+", hay))
            for label in [ent.get("name") or ""] + list(ent.get("aliases") or []):
                low = label.lower().strip()
                if len(low) >= 4 and re.search(
                        r"(?<![a-z0-9])" + re.escape(low) + r"(?![a-z0-9])", hay):
                    return True
                # short all-caps acronyms ("INC", "CRA") — case-sensitive
                if 2 <= len(label.strip()) <= 3 and re.fullmatch(
                        r"[A-Z0-9]+", label.strip()) and re.search(
                        r"(?<![A-Za-z0-9])" + re.escape(label.strip())
                        + r"(?![A-Za-z0-9])", raw):
                    return True
                # per-label distinctive-token coverage (≥ half)
                tokens = {t for t in re.findall(r"[a-z0-9]+", low)
                          if len(t) >= 4 and t not in _generic}
                if tokens and len(tokens & words) * 2 >= len(tokens):
                    return True
            return False

        for edge in cm.registry_relations(registry):
            src = edge.get("source")
            en = by_id.get(src) if isinstance(src, str) else None
            if en is None:
                continue  # missing/unresolvable source already FAILed above
            keys = {cm.resolve_entity_key(registry, k) for k in en.get("entities") or []}
            missing = [k for k in (edge["subject"], edge["object"])
                       if not _mentions(en, k, keys)]
            if missing:
                warn("registry-relations",
                     f"{edge['subject']} -[{edge['type']}]-> {edge['object']}: "
                     f"source entry {src} neither keys nor names {', '.join(missing)} "
                     "— confirm the entry actually establishes this edge")
    return registry


def check_sources_schema(sources_data: dict[str, Any] | None) -> None:
    """Validate the shape of every entry in `sources/sources.json`.

    v2 origin: check_brief.py check_sources_schema (~lines 1902-2132),
    ported essentially verbatim.

    The autonomous source-add path has previously produced shape drift that
    built fine *until* the static-site deploy ran and `site/build.py`
    crashed on the malformed entry. The 2026-05-15 regression:
    `"category": "research"` (string) where every other entry has
    `["research"]` (list) — `build.py` iterates `category` and treats each
    character as a category tag, then the gh-pages deploy fails.

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
    valid_reliability: set[str] = set((sources_data.get("reliability_codes") or {}).keys())
    valid_fetch_methods: set[str] = set((sources_data.get("fetch_methods") or {}).keys())

    missing_top = [
        k for k in ("schema_version", "categories", "reliability_codes",
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

        # --- tier (required on in-rotation sources; drives the daily
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


def _load_org_profile() -> dict[str, Any] | None:
    """Parsed org profile via `compose_prompts.py --dump`, or None when the
    composition is absent/invalid (the org-triage / classification checks
    degrade to n/a when the profile can't be read).

    v2 origin: check_brief.py _load_org_profile (~line 2665)."""
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


# --- Run-scope checks --------------------------------------------------------


def check_run_record(run: dict[str, Any] | None, run_id: str, content_root: Path,
                     pre_verify: bool = False) -> None:
    """The run record `runs/<date>/<run-id>.md` exists and passes
    content_model.validate_run_record (identity, timestamps, counters,
    sub_agents block, verification iterations + residual arithmetic,
    non-empty verification-notes body).

    With `pre_verify=True` (the gate run BEFORE Phase 5.7 has spawned any
    verifier), verification-block completeness errors are downgraded to
    WARN: `verification.iterations` cannot be populated before the first
    verifier iteration returns, and demanding it here would either block
    the run or — worse — invite a fabricated verification block. Every
    other error stays a FAIL. The plain (no-flag) invocation between fix
    iterations and before commit re-enforces the full contract."""
    if run is None:
        fail("run-record",
             f"runs/<date>/{run_id}.md missing — entries reference run_id {run_id!r} "
             "but no run record was written (the record is mandatory even for an empty run)")
        return
    ok("run-record", f"{run.get('path', run_id)} present")
    errs = cm.validate_run_record(run)
    if errs:
        for e in errs:
            if pre_verify and "verification" in e:
                warn("run-record(pre-verify)",
                     f"{e} — expected before Phase 5.7; populated by the verifier loop "
                     "(FAILs without --pre-verify)")
            else:
                fail("run-record", e)
        if pre_verify and all("verification" in e for e in errs):
            ok("run-record", "record passes validate_run_record apart from the "
               "pre-verification block (expected at this stage)")
    else:
        ok("run-record", "record passes content_model.validate_run_record")
    dur = run.get("duration_seconds")
    if isinstance(dur, (int, float)) and dur > RUNAWAY_RUN_SECONDS:
        warn("run-record",
             f"duration_seconds={int(dur)} (~{dur / 3600:.1f} h) exceeds the "
             f"{RUNAWAY_RUN_SECONDS // 3600} h runaway threshold — a single intel fire "
             "should finish well inside an hour or two; a stalled/overrun run delays "
             "publication and lets later scheduled fires overtake it (observed "
             "2026-07-09T2009Z: 11.2 h, published 11 h late). Surface the cause in "
             "the run record and to the operator")


def check_verification_confirmation(run: dict[str, Any], pre_verify: bool = False,
                                    store_mode: bool = False) -> None:
    """v3.23 double-CLEAN gate: a run whose final verifier verdict is CLEAN
    must show the previous iteration also CLEAN, on a different model — the
    rotation's independent second model agreeing is what turns one model's
    CLEAN into a publish decision. Unconfirmed final CLEAN → FAIL pre-commit
    unless the record explains it (`verification.confirmation_waived`, or a
    first CLEAN landing exactly at the iteration cap → WARN). A same-model
    confirmation WARNs (legitimate only as a recorded spawn-failure
    exception, e.g. 2026-06-05's classifier-blocked Opus spawns).
    NEEDS_FIXES finals are the early-exit / cap fail-open path with residuals
    and are out of scope for the double-CLEAN gate — but the rotation itself
    is checked on every chain regardless of verdict (v3.31: 2026-08-06 ran
    all five iterations on `cti-verification` because every alternate spawn
    was classifier-blocked, and because its final verdict was NEEDS_FIXES no
    check saw it). `store_mode` (--all) downgrades FAIL to WARN — published
    records are immutable history."""
    v = _prompt_version_tuple(run.get("prompt_version"))
    if v is None or v < DOUBLE_CLEAN_FROM:
        if not store_mode:
            ok("verification-confirmation",
               "pre-v3.23 run — double-CLEAN gate not yet in force (informational)")
        return
    rid = run.get("run_id")
    ver = run.get("verification") if isinstance(run.get("verification"), dict) else {}
    iters = [i for i in (ver.get("iterations") or []) if isinstance(i, dict)] \
        if isinstance(ver.get("iterations"), list) else []
    # The waiver's canonical home is `verification.confirmation_waived`; one
    # record (2026-08-06T0411Z-intel) wrote it at the top level instead, which
    # would have hidden a fully-documented fail-open from this check had that
    # run converged to CLEAN. Honour both placements, and nudge fresh runs to
    # the canonical one rather than punishing immutable history.
    waived = str(ver.get("confirmation_waived")
                 or run.get("verification_confirmation_waived") or "").strip()
    if (not ver.get("confirmation_waived")) and run.get("verification_confirmation_waived") \
            and not store_mode:
        warn("verification-confirmation",
             f"{rid}: confirmation waiver recorded at top level as "
             "`verification_confirmation_waived` — the canonical key is "
             "`verification.confirmation_waived` (honoured here, but move it)")
    if not iters:
        if pre_verify and not store_mode:
            ok("verification-confirmation",
               "no iterations yet (--pre-verify) — populated by the Phase 5.7 loop")
        # a missing/empty block on the plain invocation is validate_run_record's FAIL
        return

    def _ident(it: dict[str, Any]) -> str:
        return (str(it.get("subagent_type") or "").strip()
                or str(it.get("model_id") or "").strip()
                or str(it.get("model") or "").strip())

    # Rotation integrity across the WHOLE chain — hard invariant #11 says
    # consecutive iterations never run the same definition, and that holds on
    # every publish path, not only on the CLEAN one. A recorded waiver (the
    # classifier-blocked-spawn exception) is what makes a collapsed rotation
    # acceptable, so it silences this.
    pairs = [(a, b) for a, b in zip(iters, iters[1:])
             if _ident(a) and _ident(a) == _ident(b)]
    if pairs and not waived:
        names = ", ".join(f"{a.get('iteration', '?')}+{b.get('iteration', '?')}" for a, b in pairs[:4])
        emit = warn if store_mode else fail
        emit("verification-rotation",
             f"{rid}: {len(pairs)} consecutive same-definition iteration pair(s) "
             f"({names}) on {_ident(pairs[0][0])} — the rotation must alternate "
             "`cti-verification` / `cti-verification-alt` so consecutive passes run on "
             "different models. Legitimate only as a recorded spawn-failure exception: "
             "set verification.confirmation_waived with the reason")
    elif pairs:
        ok("verification-rotation",
           f"{len(pairs)} same-definition iteration pair(s) — explained by the recorded "
           "confirmation waiver")
    elif not store_mode:
        ok("verification-rotation",
           f"rotation alternated across all {len(iters)} iteration(s)")

    final = iters[-1]
    if final.get("verdict") != "CLEAN":
        if not store_mode:
            ok("verification-confirmation",
               "final verdict NEEDS_FIXES — early-exit / fail-open path with residuals; "
               "the double-CLEAN gate governs only CLEAN publishes")
        return
    prev = iters[-2] if len(iters) >= 2 else None
    if prev is None or prev.get("verdict") != "CLEAN":
        if waived:
            warn("verification-confirmation",
                 f"{rid}: final CLEAN is unconfirmed — confirmation waived: {waived!r} "
                 "(recorded fail-open)")
        elif len(iters) >= (VERIFIER_ITERATION_CAP if v >= CAP_EIGHT_FROM
                            else VERIFIER_ITERATION_CAP_PRE_V327):
            cap = (VERIFIER_ITERATION_CAP if v >= CAP_EIGHT_FROM
                   else VERIFIER_ITERATION_CAP_PRE_V327)
            warn("verification-confirmation",
                 f"{rid}: first CLEAN landed at the {cap}-iteration cap "
                 "with no room for the other-model confirmation pass — fail-open; set "
                 "verification.confirmation_waived with the reason")
        else:
            emit = warn if store_mode else fail
            emit("verification-confirmation",
                 f"{rid}: final verdict CLEAN is unconfirmed — iteration "
                 f"{final.get('n')} is the only CLEAN in the chain. A CLEAN publish "
                 "requires two consecutive CLEAN verdicts on two different models "
                 "(Phase 5.7 decision rules 1–2): spawn the other-model confirmation "
                 "pass, or record why it was impossible in "
                 "verification.confirmation_waived")
        return

    ia, ib = _ident(prev), _ident(final)
    if ia and ib and ia == ib:
        warn("verification-confirmation",
             f"{rid}: confirming iterations {prev.get('n')} + {final.get('n')} both ran "
             f"{ia} — the confirmation pass must run on a different model (rotation); "
             "acceptable only as a recorded exception (other-model spawn blocked after "
             "a retry) noted in the run record")
    elif not store_mode:
        ok("verification-confirmation",
           f"confirmed CLEAN — iterations {prev.get('n')} + {final.get('n')} both CLEAN "
           f"on {ia or '?'} + {ib or '?'}")


def check_prompt_version(run: dict[str, Any], content_root: Path) -> None:
    """The run record's `prompt_version` must match the most recent
    `## N.M —` heading in prompts/CHANGELOG.md.

    v2 origin: check_brief.py check_prompt_version (~line 2195) — the safety
    net for the versioning rule: a prompt edit must ship the banner bump and
    the CHANGELOG entry in the same commit; a mismatch here means one of the
    two was skipped. Severity depends on when the check runs: FAIL while the
    run record is still uncommitted (the normal pre-commit gate — this is
    the moment the mismatch must be fixed); WARN on a record that is already
    committed clean, whose version legitimately trails a changelog that
    moved on after publication."""
    pv = str(run.get("prompt_version") or "").strip()
    if not pv:
        warn("prompt-version", "run record carries no prompt_version "
             "(validate_run_record flags the missing field)")
        return
    badge = pv.lstrip("vV")
    if not CHANGELOG.exists():
        warn("prompt-version", "prompts/CHANGELOG.md not found — cannot cross-check prompt_version")
        return
    m = CHANGELOG_HEAD_RE.search(CHANGELOG.read_text(encoding="utf-8"))
    if not m:
        warn("prompt-version", "no `## N.M —` heading found in prompts/CHANGELOG.md")
        return
    latest = m.group(1)
    if badge == latest:
        ok("prompt-version", f"prompt_version v{badge} matches the CHANGELOG's most recent entry")
        return

    # Mismatch — decide severity from whether this is the pre-commit gate.
    rec_path = content_root / run.get("path", "") if run.get("path") else None
    pre_commit: bool | None = None
    if rec_path is not None:
        try:
            proc = subprocess.run(
                ["git", "status", "--porcelain", "--", str(rec_path)],
                capture_output=True, text=True, cwd=ROOT, timeout=15)
            pre_commit = bool(proc.stdout.strip()) if proc.returncode == 0 else None
        except Exception:
            pre_commit = None
    if pre_commit is None:  # git unavailable / fixture root — fall back to a date heuristic
        pre_commit = str(run.get("date") or "") == datetime.now(timezone.utc).date().isoformat()

    if pre_commit:
        fail("prompt-version",
             f"run record prompt_version v{badge} != CHANGELOG latest v{latest} — the prompt "
             f"banner bump and the CHANGELOG entry must ship in the same commit as the prompt "
             f"edit (versioning rule)")
    else:
        warn("prompt-version",
             f"run record prompt_version v{badge} trails CHANGELOG latest v{latest} "
             f"(record already committed; the changelog moved on after publication — informational)")


def check_run_counters(run: dict[str, Any], run_entries: list[dict]) -> None:
    """The record's self-reported counters must equal what is actually on
    disk: `entries_published` == entry files carrying this run_id,
    `entries_updated` == those with update_of set, and a non-null
    `deep_dive` must name a deep_dive: true entry from this run. Counter
    drift means the record was written before composition finished (or an
    entry was added/dropped after the record) — the Ops dashboard and the
    rolling-24 h composition report both key on these numbers."""
    actual_pub = len(run_entries)
    actual_upd = len([e for e in run_entries if e.get("update_of")])
    pub = run.get("entries_published")
    upd = run.get("entries_updated")
    if pub == actual_pub:
        ok("run-counters", f"entries_published = {pub} matches {actual_pub} entry file(s) on disk")
    else:
        fail("run-counters",
             f"entries_published = {pub!r} but {actual_pub} entry file(s) carry run_id "
             f"{run.get('run_id')!r}")
    if upd == actual_upd:
        ok("run-counters", f"entries_updated = {upd} matches {actual_upd} update entr{'y' if actual_upd == 1 else 'ies'}")
    else:
        fail("run-counters",
             f"entries_updated = {upd!r} but {actual_upd} of this run's entries have update_of set")
    dd = run.get("deep_dive")
    if dd is None:
        ok("run-counters", "deep_dive: null (no deep-dive entry claimed)")
    else:
        match = [e for e in run_entries if e["id"] == dd and e.get("deep_dive") is True]
        if match:
            ok("run-counters", f"deep_dive {dd} resolves to a deep_dive: true entry of this run")
        else:
            fail("run-counters",
                 f"deep_dive = {dd!r} does not resolve to an entry of this run with deep_dive: true")


def check_entry_schema(run_entries: list[dict], taxonomy: dict, registry_keys) -> None:
    """Every entry of the run passes content_model.validate_entry: required
    fields, structural enums, taxonomy vocabulary, folder-date ==
    discovered_at date, priority ⇔ immediate_action, per-CVE records,
    source shape, evidence presence on exploited/immediate-action entries,
    entity-key resolution against the registry, non-empty body."""
    if not run_entries:
        ok("entry-schema", "run published no entries (empty run — record-only is a healthy outcome)")
        return
    n_errs = 0
    for entry in run_entries:
        for e in cm.validate_entry(entry, taxonomy, registry_keys):
            fail("entry-schema", e)
            n_errs += 1
    if not n_errs:
        ok("entry-schema", f"all {len(run_entries)} entr{'y' if len(run_entries) == 1 else 'ies'} pass validate_entry")


def check_entry_run_binding(run: dict[str, Any], run_entries: list[dict]) -> None:
    """Every entry's discovered_at must sit inside the run's wall-clock
    envelope: [started − 5 min, completed + 12 h]. The lower slack absorbs
    clock skew between the record and the first verified finding; the upper
    slack allows a long compose/verify tail (the record's `completed` may be
    written before the final publish phase). Outside the envelope → WARN,
    not FAIL: a wrong-but-plausible timestamp is an editorial defect, and
    backdating is already blocked by folder-date == discovered_at."""
    started = cm.parse_ts(run.get("started"))
    completed = cm.parse_ts(run.get("completed"))
    if started is None or completed is None:
        warn("entry-run-binding",
             "run started/completed unparseable — cannot bind entry timestamps to the run window")
        return
    lo = started - timedelta(minutes=5)
    hi = completed + timedelta(hours=12)
    outside: list[str] = []
    for e in run_entries:
        ts = cm.parse_ts(e.get("discovered_at"))
        if ts is None:
            continue  # entry-schema already fails the unparseable timestamp
        if not (lo <= ts <= hi):
            outside.append(f"{e['id']} discovered_at {e.get('discovered_at')}")
    if outside:
        warn("entry-run-binding",
             f"{len(outside)} entr{'y' if len(outside) == 1 else 'ies'} outside "
             f"[{lo.strftime('%Y-%m-%dT%H:%M:%SZ')}, {hi.strftime('%Y-%m-%dT%H:%M:%SZ')}]: "
             + "; ".join(outside[:5]))
    else:
        ok("entry-run-binding",
           f"all {len(run_entries)} discovered_at timestamps inside the run window (−5 min / +12 h slack)")


def _entry_cve_ids(entry: dict) -> set[str]:
    return {str(c.get("id")) for c in (entry.get("cves") or [])
            if isinstance(c, dict) and c.get("id")}


def _update_chain_ids(entry: dict, entries_by_id: dict[str, dict]) -> set[str]:
    """Entry ids reachable from `entry` via update_of (up to 20 hops).
    Used to exempt an entry's own coverage lineage from the dedup scan."""
    seen: set[str] = set()
    cur = entry.get("update_of")
    hops = 0
    while cur and cur not in seen and hops < 20:
        seen.add(str(cur))
        nxt = entries_by_id.get(str(cur))
        cur = nxt.get("update_of") if nxt else None
        hops += 1
    return seen


def check_dedup(run: dict[str, Any], run_entries: list[dict],
                all_entries: list[dict], entries_by_id: dict[str, dict],
                registry: dict[str, Any] | None = None) -> None:
    """Cross-run dedup — the mechanical stage-4 of the pipeline's dedup
    ladder (docs/pipeline.md § Dedup across runs). For each NON-update entry
    of this run: FAIL when any of its cves[].id appears in ANY entry from
    the prior 14 days by folder date (including earlier runs the same day,
    excluding this run's own entries and the entry's update_of lineage);
    WARN when one of its entity keys appears on a non-update prior entry —
    forcing the update_of decision to be explicit. For UPDATE entries: FAIL
    when update_of does not resolve to an existing entry file, and FAIL when
    it points at an entry with a LATER discovered_at (an update cannot
    predate its original)."""
    run_id = run.get("run_id")
    run_date_s = str(run.get("date") or "")
    try:
        run_date = date.fromisoformat(run_date_s)
    except ValueError:
        warn("dedup", f"run date {run_date_s!r} unparseable — dedup window skipped")
        return
    window_start = (run_date - timedelta(days=14)).isoformat()
    prior = [e for e in all_entries
             if e.get("run_id") != run_id and window_start <= e["date"] <= run_date_s]

    cve_hits: list[str] = []
    entity_hits: list[str] = []
    update_fails: list[str] = []
    for e in run_entries:
        upd = e.get("update_of")
        if upd:
            target = entries_by_id.get(str(upd))
            if target is None:
                update_fails.append(
                    f"{e['id']}: update_of {upd!r} does not resolve to an existing entry file")
                continue
            t_ts = cm.parse_ts(target.get("discovered_at"))
            e_ts = cm.parse_ts(e.get("discovered_at"))
            if t_ts is not None and e_ts is not None and t_ts > e_ts:
                update_fails.append(
                    f"{e['id']}: update_of {upd} has LATER discovered_at "
                    f"({target.get('discovered_at')}) than the update itself ({e.get('discovered_at')})")
            continue  # update entries are exempt from the overlap scan — the link IS the dedup
        chain = _update_chain_ids(e, entries_by_id)
        e_cves = _entry_cve_ids(e)
        # Resolve merged_into tombstones so an old entry's key and its
        # canonical successor still register as the same entity.
        reg = registry or {}
        e_ents = {cm.resolve_entity_key(reg, str(k)) for k in (e.get("entities") or []) if k}
        # A weekly strategic entry synthesises the operational entries it lists in
        # references[] — sharing their entity keys is the design, not drift, so the
        # declared reference IS the dedup for those pairs (same logic as update_of
        # above). CVE-level overlap is still reported: per-CVE metadata belongs to
        # the operational entry that owns it and must not be duplicated upward.
        e_refs = set()
        if str(e.get("horizon") or "") == "strategic":
            e_refs = {str(r) for r in (e.get("references") or []) if r}
        for p in prior:
            if p["id"] in chain:
                continue
            overlap = e_cves & _entry_cve_ids(p)
            if overlap:
                cve_hits.append(
                    f"{e['id']}: CVE(s) {sorted(overlap)} already covered by {p['id']} — "
                    f"ship as update_of with a genuine delta, or drop")
            if not p.get("update_of") and p["id"] not in e_refs:
                ent_overlap = e_ents & {cm.resolve_entity_key(reg, str(k))
                                        for k in (p.get("entities") or []) if k}
                if ent_overlap:
                    entity_hits.append(
                        f"{e['id']}: entity {sorted(ent_overlap)} also on {p['id']} — "
                        f"confirm the non-update decision was deliberate (material new story, not a delta)")
    for h in update_fails:
        fail("dedup", h)
    for h in cve_hits:
        fail("dedup", h)
    for h in entity_hits:
        warn("dedup", h)
    if not (cve_hits or entity_hits or update_fails):
        ok("dedup",
           f"no CVE/entity overlap with {len(prior)} prior entr{'y' if len(prior) == 1 else 'ies'} "
           f"in the 14-day window; all update_of targets resolve in order")


def check_update_targets(scope_entries: list[dict], entries_by_id: dict[str, dict]) -> None:
    """update_of chains must terminate — no cycles, no >20-hop runaways.
    A cycle would make the render-time 'originally covered' walk loop
    forever; 20 hops on one story means the ≤1-consolidated-update-per-week
    rule has collapsed."""
    bad: list[str] = []
    checked = 0
    for e in scope_entries:
        if not e.get("update_of"):
            continue
        checked += 1
        seen = {e["id"]}
        cur = str(e.get("update_of"))
        hops = 0
        while cur:
            if cur in seen:
                bad.append(f"{e['id']}: update_of chain cycles at {cur}")
                break
            seen.add(cur)
            hops += 1
            if hops >= 20:
                bad.append(f"{e['id']}: update_of chain exceeds 20 hops (runaway or cycle)")
                break
            nxt = entries_by_id.get(cur)
            if nxt is None:
                break  # unresolved target — check_dedup / --all resolution reports it
            cur = str(nxt.get("update_of")) if nxt.get("update_of") else ""
    if bad:
        for b in bad:
            fail("update-target", b)
    else:
        ok("update-target",
           f"{checked} update chain(s) acyclic and bounded" if checked
           else "no update entries in scope")


def report_rolling_composition(run: dict[str, Any], all_entries: list[dict]) -> None:
    """Relevance discipline (docs/pipeline.md § Relevance discipline): entry
    volume follows the strict relevance/actionability gate, NOT a numeric
    target or ceiling. There is intentionally no count that fails or warns
    here — how many entries a window carries is decided entirely by how much
    of its signal clears PD-11, and more runs must not mean more content
    (dedup enforces that, checked separately in check_dedup).

    This function is purely informational: it reports the rolling-24 h
    composition (operational count, deep dives on the run's UTC date,
    criticals in the window) so the operator can see the shape of the window
    at a glance. `priority: critical` and deep-dive rarity are governed by
    their own qualitative bars in the prompt, not by a count here."""
    completed = cm.parse_ts(run.get("completed"))
    if completed is None:
        ok("composition", "run completed timestamp unparseable — composition report skipped")
        return
    lo = completed - timedelta(hours=24)
    window: list[dict] = []
    for e in all_entries:
        ts = cm.parse_ts(e.get("discovered_at"))
        if ts is not None and lo < ts <= completed:
            window.append(e)
    operational = [e for e in window if (e.get("horizon") or "operational") == "operational"]
    dd_today = [e for e in all_entries
                if e.get("deep_dive") is True and e.get("date") == run.get("date")]
    critical = [e for e in window if e.get("priority") == "critical"]
    ok("composition",
       f"rolling-24h composition (informational, not gated): {len(operational)} operational, "
       f"{len(dd_today)} deep-dive on {run.get('date')}, {len(critical)} critical")

    # Two editorial-discipline rates the verifier's F16 (priority calibration)
    # and F18 (action-item discipline) are asked to judge with no reference
    # point (v3.31, from the 2026-08-02 audit's recommendation 4 — the cheap,
    # informational half of it). These are OBSERVATIONS, never gates: hard
    # invariant #20 forbids governing entry volume or composition by a number,
    # and nothing here fails, warns or caps anything. The trailing-28d rate is
    # the baseline the current window is reported against, so a drift is
    # visible to the operator without anyone having to recompute it.
    def _rates(rows: list[dict]) -> tuple[int, float, float, float]:
        ops = [e for e in rows if (e.get("horizon") or "operational") == "operational"]
        if not ops:
            return 0, 0.0, 0.0, 0.0
        highs = sum(1 for e in ops if e.get("priority") == "high")
        acts = [len(e.get("actions") or []) for e in ops]
        return (len(ops), 100.0 * highs / len(ops), sum(acts) / len(ops),
                100.0 * sum(1 for a in acts if a == 0) / len(ops))

    base_lo = completed - timedelta(days=28)
    baseline = [e for e in all_entries
                if (ts := cm.parse_ts(e.get("discovered_at"))) is not None
                and base_lo < ts <= completed]
    n_w, high_w, act_w, empty_w = _rates(window)
    n_b, high_b, act_b, empty_b = _rates(baseline)
    ok("composition",
       f"editorial rates (informational, not gated): 24h high-share {high_w:.0f}% "
       f"(28d {high_b:.0f}%) · actions/operational-entry {act_w:.2f} (28d {act_b:.2f}) · "
       f"entries with no action {empty_w:.0f}% (28d {empty_b:.0f}%) · n={n_w}/{n_b}")


def _scan_iocs(text: str) -> list[str]:
    """Return IOC findings for one text blob.

    v2 origin: check_brief.py check_no_iocs (~lines 2245-2323), refactored
    to a per-entry helper. Patterns checked:
      - SHA-256 / SHA-1 / MD5 hashes (32+ contiguous hex chars).
      - Routable IPv4 addresses (excluding RFC 5737 / 1918 / loopback /
        link-local / broadcast). **Skips version-string contexts** —
        product versions like `12.6.1.1` look like IPs but are not IOCs.
    """
    findings: list[str] = []

    # Hash patterns. 32-char MD5 false-positives are real (Git long SHAs are
    # 40, but mid-text 32-char hex strings can show up in vendor advisory
    # IDs); we still flag them, the agent confirms.
    sha256 = re.findall(r"\b[a-fA-F0-9]{64}\b", text)
    sha1 = re.findall(r"(?<![a-fA-F0-9])[a-fA-F0-9]{40}(?![a-fA-F0-9])", text)
    md5 = re.findall(r"(?<![a-fA-F0-9])[a-fA-F0-9]{32}(?![a-fA-F0-9])", text)
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

    version_context_re = re.compile(
        r"(?i)\b(version|versions?|patched|fixed|fix|firmware|build|release|"
        r"branch|prior\s+to|before|earlier\s+than|≥|>=|<=|≤|EPMM|EPMS|EPSS|patch)\b"
    )

    flagged: list[str] = []
    for m in ipv4_re.finditer(text):
        ip = m.group(0)
        if _is_doc_or_private(ip):
            continue
        # Skip longer dotted-integer identifiers (SNMP/MIB OIDs such as
        # 1.3.6.1.4.1.9.9.96.1.1, and multi-part version strings): a real
        # IPv4 address is exactly four groups, so a match that continues
        # with another `.<digit>` immediately before or after is part of a
        # longer numeric identifier, not an address. Real routable IOCs are
        # four groups bounded by a non-(dot+digit) neighbour and stay flagged.
        before = text[max(0, m.start() - 1):m.start()]
        after = text[m.end():m.end() + 2]
        if before == "." or re.match(r"\.\d", after):
            continue
        # Look at the surrounding 80-char window for version-string cues.
        start = max(0, m.start() - 80)
        end = min(len(text), m.end() + 80)
        window = text[start:end]
        if version_context_re.search(window):
            continue
        # Inside a Markdown table cell or paren list of versions ('| 12.6.1.1 |',
        # '< 12.6.1.1 / 12.7.0.1', etc.) — skip if the immediate neighbours are
        # other version-like dotted numbers.
        if re.search(r"[\d.]+\s*[/,]\s*$", text[start:m.start()]) \
           or re.search(r"^\s*[/,]\s*[\d.]+", text[m.end():end]):
            continue
        flagged.append(ip)
    if flagged:
        findings.append(f"routable IPv4 address(es): {flagged[:3]}")
    return findings


def check_no_iocs(run_entries: list[dict]) -> None:
    """Hard invariant: no IOCs. Heuristic scan over each entry's body +
    headline + summary (title is a headline subset in practice but scanned
    via headline). The agent is still the line of defence — this catches
    the easy cases."""
    hit = False
    for e in run_entries:
        blob = "\n".join(str(e.get(k) or "") for k in ("headline", "summary", "body"))
        findings = _scan_iocs(blob)
        if findings:
            hit = True
            fail("ioc-scan", f"{e['id']}: " + "; ".join(findings)
                 + " — confirm none are IOCs before publishing")
    if not hit:
        ok("ioc-scan",
           "no obvious IOC patterns detected (version-string false positives skipped)")


def check_blocked_sources(run_entries: list[dict]) -> None:
    """Hard FAIL when any entry's sources[].url matches a known-bad pattern:
    NVD/MITRE/cve.org per-CVE pages (always derived, never the disclosing
    party) or generic landing / category / index URLs that point at
    navigation, not content. v2 origin: check_blocked_source_patterns."""
    blocked: list[str] = []
    for e in run_entries:
        for src in e.get("sources") or []:
            if not isinstance(src, dict):
                continue
            url = src.get("url", "") or ""
            host, path = _host_path(url)
            matched = False
            for h_frag, p_re, reason in BLOCKED_SOURCE_PATTERNS:
                if h_frag in host and re.search(p_re, path):
                    blocked.append(f"{e['id']} cites {url} — {reason}")
                    matched = True
                    break
            if matched:
                continue
            for h_frag, p_re, reason in BLOCKED_LANDING_PATTERNS:
                if h_frag in host and re.search(p_re, path):
                    blocked.append(f"{e['id']} cites {url} — {reason}")
                    break
    if blocked:
        for b in blocked:
            fail("blocked-source", b)
    else:
        ok("blocked-source", "no source URL matches a known-bad pattern (NVD / landing / index)")


def _load_url_liveness_ledger() -> dict[str, str]:
    """URL-liveness cache. Sub-agents append to `work/<run-id>/url-liveness.tsv`
    a tab-separated `<url>\\t<status>\\t<fetched_at>` line for every source URL
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

    v2 origin: check_brief.py _load_url_liveness_ledger (~line 826)."""
    cached: dict[str, tuple[str, str]] = {}  # url -> (status, fetched_at)
    if not WORK_DIR.exists():
        return {}
    for ledger in sorted(WORK_DIR.glob("*/url-liveness.tsv")):
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


def check_source_urls_resolve(run_entries: list[dict], *, skip: bool,
                              timeout: float = 10.0) -> None:
    """Live HEAD/GET every source URL of THIS RUN's entries; FAIL on 404.
    Catches fabricated-URL drift the verifier was designed to find —
    duplicating it here so the operator gets a green/red answer locally
    without spawning a sub-agent. Use `--no-link-check` for offline runs.
    Entries carrying `migrated_from` are skipped entirely — their URLs were
    validated when the v2 brief published and historical link rot is not
    this run's defect.

    v2 origin: check_brief.py check_source_urls_resolve (~lines 1078-1312),
    including the SSRF defences and the pre-flight CA probe."""
    if skip:
        warn("source-urls", "skipped (--no-link-check)")
        return

    import ipaddress
    import socket
    import urllib.error
    import urllib.request

    # Defence in depth: even though check_run.py is run by the operator
    # (not from the public web), refuse redirects that would land us on a
    # loopback / link-local / private / cloud-metadata host. Otherwise an
    # allowlisted publisher whose CMS is compromised — or a typo in an
    # entry — could pivot the operator's local URL-liveness check into a
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
    migrated_skipped = 0
    for e in run_entries:
        if e.get("migrated_from"):
            migrated_skipped += 1
            continue
        for src in e.get("sources") or []:
            if not isinstance(src, dict):
                continue
            u = src.get("url", "") or ""
            if u.startswith("http://") or u.startswith("https://"):
                urls.setdefault(u, []).append(e["id"])
    if migrated_skipped:
        ok("source-urls",
           f"{migrated_skipped} migrated entr{'y' if migrated_skipped == 1 else 'ies'} skipped "
           "(v2-validated at original publication)")

    if not urls:
        ok("source-urls", "no http(s) source URLs to check")
        return

    # URL-liveness cache — sub-agents that successfully fetched a URL
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
            headers={"User-Agent": "check_run.py probe"},
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
    # signal the composing agent should act on (rewrite citation or drop
    # the entry).
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
    # WebFetch / fetch_source.py, so there is no actionable leverage
    # here. Aggregate into one summary WARN with a status breakdown +
    # a few examples — operators still see the pattern (e.g. "this
    # host always 403s us") but the composing agent doesn't drown in 30
    # identical warnings of the same shape.
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
           f"{len(ua_blocked)} URL(s) on UA-blocked hosts (CISA/NCSC.ch/etc.) — "
           "403 from these never demotes; they are fetched via tools/fetch_source.py")
    if not bad_404 and not other_errors:
        ok("source-urls", f"all {checked} source URL(s) returned HTTP 200 (or UA-blocked allowlisted)")


def check_evidence_binding(run_entries: list[dict]) -> None:
    """Every evidence[] quote's `publisher` should bind back to one of the
    entry's sources[].publisher or closed_sources[].provider (case-
    insensitive substring either way, so 'Talos' binds to 'Cisco Talos').
    WARN — the shape itself (quote + publisher present) is validate_entry's
    concern; content correctness (does the source actually say the quote?)
    stays with the verifier's F13-F15. v2 origin: check_evidence_shape's
    binding half (~line 2540)."""
    unbound: list[str] = []
    bound = 0
    for e in run_entries:
        pubs = {str(s.get("publisher") or "").strip().lower()
                for s in (e.get("sources") or []) if isinstance(s, dict)}
        pubs |= {str(c.get("provider") or "").strip().lower()
                 for c in (e.get("closed_sources") or []) if isinstance(c, dict)}
        pubs.discard("")
        for ev in e.get("evidence") or []:
            if not isinstance(ev, dict):
                continue
            p = str(ev.get("publisher") or "").strip().lower()
            if not p:
                continue  # missing publisher is an entry-schema FAIL already
            if any(p in lbl or lbl in p for lbl in pubs):
                bound += 1
            else:
                unbound.append(
                    f"{e['id']}: evidence publisher {ev.get('publisher')!r} matches no "
                    f"sources[].publisher / closed_sources[].provider")
    if unbound:
        for u in unbound[:8]:
            warn("evidence-binding", u)
        if len(unbound) > 8:
            warn("evidence-binding", f"(+{len(unbound) - 8} more unbound quotes)")
    else:
        ok("evidence-binding",
           f"all {bound} evidence quote(s) bind to a listed publisher" if bound
           else "no evidence quotes in this run's entries")


def check_single_source_flags(run_entries: list[dict]) -> None:
    """Consistency between the `verification:` value and the national-CERT
    carve-out (v2 origin: check_single_source_flag ~line 957 — the v2
    heading marker `[SINGLE-SOURCE]` is now the structured field, so the
    mechanical residue is host/value agreement):
      - `single-source` on exactly one source whose host IS a national CERT
        → the entry almost certainly wants `single-source-national-cert`
        (the carve-out is a *stronger* guarantee and renders differently);
      - `single-source-national-cert` whose (first) source host is NOT a
        national-CERT host → the carve-out is claimed but unearned.
    The impossible combination (multi-source with < 2 sources) is a
    validate_entry FAIL and not re-checked here."""
    flagged: list[str] = []
    for e in run_entries:
        sources = [s for s in (e.get("sources") or []) if isinstance(s, dict)]
        ver = e.get("verification")
        host = _host_path(sources[0].get("url", ""))[0] if sources else ""
        if ver == "single-source" and len(sources) == 1 and not e.get("closed_sources") \
                and _host_is_national_cert(host):
            flagged.append(
                f"{e['id']}: verification: single-source but the sole source host ({host}) is a "
                f"national-CERT host — should this be single-source-national-cert?")
        if ver == "single-source-national-cert" and sources and not _host_is_national_cert(host):
            flagged.append(
                f"{e['id']}: verification: single-source-national-cert but source host ({host}) "
                f"is not on the national-CERT carve-out list")
    if flagged:
        for f_ in flagged:
            warn("single-source-flag", f_)
    else:
        ok("single-source-flag",
           "verification values consistent with the national-CERT carve-out list")


def check_aggregator_only(run_entries: list[dict]) -> None:
    """An entry with ≥2 sources all from news-aggregator hosts meets the
    literal two-source bar but lacks any primary disclosure (vendor PSIRT,
    research-lab post, regulator filing, victim statement). WARN so the run
    record carries the reduced-confidence framing instead of silently
    accepting. v2 origin: check_aggregator_only_sourcing (~line 915)."""
    flagged: list[str] = []
    for e in run_entries:
        sources = [s for s in (e.get("sources") or []) if isinstance(s, dict)]
        if len(sources) < 2:
            continue
        hosts = [_host_path(s.get("url", ""))[0] for s in sources]
        if hosts and all(_host_is_aggregator(h) for h in hosts if h):
            flagged.append(
                f"{e['id']}: {len(sources)} sources, all news-aggregator hosts "
                f"({sorted(set(hosts))[:3]}) — re-pivot to a vendor / research-lab / regulator "
                f"primary, or note reduced confidence in the run record")
    if flagged:
        for f_ in flagged:
            warn("aggregator-only", f_)
    else:
        ok("aggregator-only", "no entry leans on news-aggregator hosts as its only sources")


# Action-item discipline (prompts/CHANGELOG.md § 3.19): actions[] is the
# do-now surface feeding the rendered brief's aggregated § Action Items —
# only concrete, finding-derived, start-now tasks; empty is the normal case.
# Mechanical residue of the editorial bar (the verifier's F18 owns the
# judgment calls): list-length and canonical generic-advice phrases. WARN
# severity — genericity is not machine-decidable, so the gate never blocks
# on it. Applied to v3.19+ runs only (entries are immutable; earlier records
# predate the bar).
ACTIONS_DISCIPLINE_FROM = (3, 19)

# Lowercase substrings that mark canonical generic advice — true independently
# of any specific finding, so never an action item (cti-run.md Phase 4
# § actions[] rule 2). Deliberately short and unambiguous: this list flags
# the textbook phrases, not every weak action.
GENERIC_ACTION_PHRASES = (
    "enable mfa",
    "enable multi-factor",
    "patch regularly",
    "apply patches regularly",
    "keep systems up to date",
    "keep software up to date",
    "raise awareness",
    "user awareness",
    "security awareness training",
    "monitor for suspicious activity",
    "stay vigilant",
    "follow best practices",
    "review your security posture",
    "ensure backups",
    "defense in depth",
)


def check_actions_discipline(run_entries: list[dict], run: dict[str, Any] | None) -> None:
    """actions[] hygiene for v3.19+ runs: WARN on a padded list (> 3 actions
    on one entry — near-certain body restatement per the Phase 4 do-now bar),
    on canonical generic-advice phrases, and on the same action string shipped
    verbatim by two entries of the run (the brief's § Action Items is a union
    — the reader sees the duplicate). Empty actions[] is always fine."""
    v = _prompt_version_tuple((run or {}).get("prompt_version"))
    if v is None or v < ACTIONS_DISCIPLINE_FROM:
        ok("action-items", "pre-v3.19 run — do-now bar not yet in force (informational)")
        return
    flagged: list[str] = []
    seen: dict[str, str] = {}
    total = 0
    for e in run_entries:
        actions = [a.strip() for a in (e.get("actions") or [])
                   if isinstance(a, str) and a.strip()]
        total += len(actions)
        if len(actions) > 3:
            flagged.append(
                f"{e['id']}: {len(actions)} action items — the do-now bar (cti-run.md "
                f"Phase 4 § actions[]) makes >3 near-certain body restatement; keep the "
                f"genuine start-now tasks, fold the rest into the body")
        for a in actions:
            low = a.lower()
            for phrase in GENERIC_ACTION_PHRASES:
                if phrase in low:
                    flagged.append(
                        f"{e['id']}: action {a[:80]!r} contains generic-advice phrase "
                        f"{phrase!r} — an action true independently of this finding is "
                        f"body content at best, never an action item")
                    break
            if a in seen and seen[a] != e["id"]:
                flagged.append(
                    f"{e['id']}: action duplicated verbatim from {seen[a]} — the rendered "
                    f"§ Action Items is a union over the window; state it once")
            seen.setdefault(a, e["id"])
    if flagged:
        for f_ in flagged:
            warn("action-items", f_)
    else:
        ok("action-items",
           f"{total} action item{'s' if total != 1 else ''} across "
           f"{len(run_entries)} entr{'y' if len(run_entries) == 1 else 'ies'} — "
           "no padded list, no generic-advice phrase, no verbatim duplicate")


def check_closed_sources(run_entries: list[dict], profile: dict[str, Any] | None) -> None:
    """closed_sources[] traceability hygiene. There is NO TLP gate: this
    pipeline never filters on TLP or a public/private flag — every file under
    intel/ is fair game to process. The one remaining concern is that a cited
    closed source should trace to a file under intel/<date>/ so the
    cold-reader verifier and the operator can find the referenced document
    (WARN — a citation referencing nothing on disk is unverifiable)."""
    intel_files = {p.name for p in INTEL_DIR.glob("*/*")} if INTEL_DIR.exists() else set()

    missing_refs: list[str] = []
    total = 0
    for e in run_entries:
        for cs in e.get("closed_sources") or []:
            if not isinstance(cs, dict):
                continue
            total += 1
            tag = f"{e['id']}: \"{str(cs.get('title') or '')[:40]}\""
            ref = str(cs.get("ref") or "")
            if intel_files:
                if not any(ref and ref in name for name in intel_files) \
                        and not any((str(cs.get("title") or "zzz")).lower()[:24]
                                    in name.lower() for name in intel_files):
                    missing_refs.append(f"{tag} ref {ref or cs.get('title', '')!r}")
            elif ref:
                missing_refs.append(f"{tag}: intel/ directory absent but ref cited")

    if missing_refs:
        warn("closed-source",
             f"{len(missing_refs)} closed-source citation(s) not traceable to a file "
             f"under intel/: " + "; ".join(missing_refs[:5]))
    else:
        ok("closed-source",
           f"{total} closed-source citation(s), all traceable to intel/" if total
           else "no closed-source citations in this run's entries")


def check_cve_sync(scope_entries: list[dict], cves_seen: dict[str, Any] | None,
                   *, scope_label: str = "run") -> None:
    """Every CVE this scope's entries carry — structured cves[].id AND any
    `CVE-YYYY-NNNN…` string in an entry BODY (catches body-only CVEs the
    structured records missed) — must exist in state/cves_seen.json. The
    flat index is the dedup/rotation memory; an unsynced CVE silently
    re-qualifies as 'new' on the next run. v2 origin: check_cve_sync."""
    all_ids: dict[str, list[str]] = {}
    for e in scope_entries:
        ids = _entry_cve_ids(e) | set(CVE_RE.findall(str(e.get("body") or "")))
        for cid in ids:
            all_ids.setdefault(cid, []).append(e["id"])
    if not all_ids:
        ok("cve-sync", f"no CVEs in {scope_label} entries")
        return
    if not cves_seen:
        fail("cve-sync", "state/cves_seen.json unavailable for comparison")
        return
    seen_ids = {c["id"] for c in (cves_seen.get("cves") or []) if isinstance(c, dict)}
    missing = sorted(set(all_ids) - seen_ids)
    if missing:
        detail = "; ".join(f"{cid} (in {all_ids[cid][:2]})" for cid in missing[:8])
        more = f" (+{len(missing) - 8} more)" if len(missing) > 8 else ""
        fail("cve-sync", f"missing from cves_seen.json: {detail}{more}")
    else:
        ok("cve-sync", f"all {len(all_ids)} CVE(s) in {scope_label} entries are in cves_seen.json")


def _triage_kinds(profile: dict[str, Any] | None) -> set[str]:
    """The entry kinds classified with the vulnerability-triage scheme
    (org_triage) rather than the Admiralty intel classification. Config-driven
    (`classification.triage_kinds`); defaults to {vulnerability}."""
    cl = (profile or {}).get("classification") or {}
    tk = cl.get("triage_kinds")
    if isinstance(tk, list) and tk:
        return {str(k) for k in tk}
    return {"vulnerability"}


def _triage_scheme_configured(profile: dict[str, Any] | None) -> bool:
    """Whether the org profile defines vulnerability-triage categories. The
    triage-kind exemption from the Admiralty classification applies ONLY
    while a scheme exists — with none configured, triage kinds carry the
    Admiralty block like every other kind (v3.18: no entry ships unrated)."""
    vt = (profile or {}).get("vulnerability_triage") or {}
    return any(isinstance(c, dict) and c.get("id") for c in (vt.get("categories") or []))


# Rating + ATT&CK-mapping completeness became MANDATORY (FAIL, not WARN) for
# entries composed from prompt v3.18 on (prompts/CHANGELOG.md § 3.18).
# Entries are immutable, so records from earlier prompt versions keep the
# old WARN severity — history stays green, the future is gated.
RATING_ENFORCED_FROM = (3, 18)
# v3.21+: unknown/revoked/deprecated ATT&CK ids in a NEW run's techniques[]
# are a FAIL at gate time — the pinned dataset is on disk when the entry is
# composed, so shipping a dead id is a composition defect, not drift. Store
# mode stays WARN: history is immutable, and a *later* pin update revoking a
# previously-active id (the legitimate case) must never turn --all red.
MAPPING_IDS_STRICT_FROM = (3, 21)
# v3.14 added Phase 7 publish-status telemetry to the run record. A v3.14+
# record still carrying no publish_status a day later means the Phase 7
# amendment never landed — the operator cannot tell from state whether the
# run actually reached the site (observed: 2026-07-09T1211Z-intel).
PUBLISH_TELEMETRY_FROM = (3, 14)
# v3.23+: the Phase 5.7 publish gate for a CLEAN outcome is DOUBLE-CLEAN —
# the final two verifier iterations both return CLEAN, on two different
# models (the opus/sonnet rotation supplies the diversity). A single
# unconfirmed CLEAN publishes only as a recorded fail-open: a first CLEAN
# landing exactly at the iteration cap, or an explicit
# `verification.confirmation_waived` reason (watchdog overrun, other-model
# spawn blocked).
DOUBLE_CLEAN_FROM = (3, 23)
# v3.27 raised the Phase 5.7 cap 5 → 8 (operator directive 2026-07-18): the
# double-CLEAN confirmation gate was churning into the 5-cap fail-open in
# roughly half the runs; 8 gives the CLEAN chain room to converge. Records
# from before v3.27 legitimately capped at 5 — the "first CLEAN landed at
# the cap" waiver check resolves the cap per record's prompt_version.
CAP_EIGHT_FROM = (3, 27)
VERIFIER_ITERATION_CAP = 8
VERIFIER_ITERATION_CAP_PRE_V327 = 5
# A single intel fire should complete well inside an hour or two; the
# 2026-07-09T2009Z run silently ran 11.2 h wall-clock (container stall /
# overrun into the next scheduled fire). Surface it — never a FAIL, the
# record itself is the forensic evidence.
RUNAWAY_RUN_SECONDS = 3 * 3600
# v3.32: `completed` / `duration_seconds` must cover the WHOLE fire. Through
# v3.31 the prompt stamped `work/<run-id>/main.ended_at` in Phase 5, i.e.
# before the mechanical gate and before the Phase 5.7 verifier loop, and the
# record's `completed` was read from that stamp — so every run's recorded
# duration understated its true wall clock by the length of its verifier
# loop and publishing chain. The majority of stored records have a
# `completed` that precedes one of their own children's `ended_at`, by up
# to 125 min
# (2026-08-04T0411Z-intel), and 2026-08-10T0411Z-intel recorded 3103 s
# (~52 min) for a fire its own notes place at ~2 h 55 m. The consequence is
# not cosmetic: RUNAWAY_RUN_SECONDS above is checked against exactly this
# number, so the ~3 h wall-clock watchdog had no machine-auditable signal
# that could see an overrun. Enforced from the prompt version that moves the
# stamp into Phase 6; earlier records are pre-rule history and are not
# reported (they would add ~100 warnings the audit could only acknowledge;
# the exact count moves with the denominator, which is why none is asserted).
COMPLETION_COVERS_RUN_FROM = (3, 32)

# ATT&CK completeness by kind: these kinds inherently describe attacker
# behavior (a campaign, an intrusion, an exploitable vulnerability's access
# vector), so an empty `techniques[]` is a composition defect, never a
# judgment call. Research/annual-report usually map but may legitimately
# carry no TTP content (statistics, governance) → WARN. Strategic kinds
# (policy, synthesis, outlook) may map nothing at all.
ATTACK_REQUIRED_KINDS = {"threat", "incident", "vulnerability"}
ATTACK_EXPECTED_KINDS = {"research", "annual-report"}

_PV_RE = re.compile(r"^v?(\d+)\.(\d+)")


def _prompt_version_tuple(pv: Any) -> tuple[int, int] | None:
    """`v3.18` / `3.18(.x)` → (3, 18); None when unparseable."""
    m = _PV_RE.match(str(pv or "").strip())
    return (int(m.group(1)), int(m.group(2))) if m else None


def _rating_enforced(run: dict[str, Any] | None) -> bool:
    """True when this run's prompt version is subject to the v3.18 hard
    gates (missing rating / missing behavior-kind ATT&CK mapping → FAIL)."""
    if run is None:
        return False
    v = _prompt_version_tuple(run.get("prompt_version"))
    return v is not None and v >= RATING_ENFORCED_FROM


def _parse_iso_utc(value: Any) -> datetime | None:
    """`2026-07-09T20:09:30Z` → aware datetime; None when unparseable."""
    try:
        return datetime.fromisoformat(str(value or "").replace("Z", "+00:00"))
    except ValueError:
        return None


def _mapping_ids_strict(run: dict[str, Any] | None) -> bool:
    """True when this run's prompt version is subject to the v3.21 hard
    gate: dead (unknown / revoked / deprecated) ATT&CK ids in techniques[]
    FAIL at gate time instead of WARNing."""
    if run is None:
        return False
    v = _prompt_version_tuple(run.get("prompt_version"))
    return v is not None and v >= MAPPING_IDS_STRICT_FROM


def check_completion_covers_run(run: dict[str, Any], store_mode: bool = False) -> None:
    """v3.32: the record's `completed` must postdate everything the fire did.

    `completed` / `duration_seconds` are the run's only machine-auditable
    wall-clock figures — the runaway watchdog checks one, the Ops dashboard
    renders both, and every quality audit reads them to answer "did any fire
    overrun?". They are trustworthy only if the stamp is taken after the
    last thing the run does. Through v3.31 it was taken in Phase 5, before
    the gate and before the Phase 5.7 loop, so a record could and did claim
    to have finished two hours before its own final verifier iteration
    returned. This check makes that shape impossible to ship again: any
    child timestamp the record itself carries — a verifier iteration's
    `ended_at`, a sub-agent's `ended_at` — that is later than `completed`
    means the stamp was taken too early.

    Scoped to records from COMPLETION_COVERS_RUN_FROM onward: earlier
    records are immutable pre-rule history, and reporting them would emit
    ~100 warnings whose only available resolution is the acknowledgment
    ledger. `store_mode` (--all) downgrades FAIL to WARN, as elsewhere —
    a published record cannot be re-stamped.
    """
    v = _prompt_version_tuple(run.get("prompt_version"))
    if v is None or v < COMPLETION_COVERS_RUN_FROM:
        if not store_mode:
            ok("run-completion",
               "pre-v%d.%d run — the completion-covers-run rule is not yet in "
               "force for this record (informational)" % COMPLETION_COVERS_RUN_FROM)
        return

    rid = run.get("run_id")
    completed = _parse_iso_utc(run.get("completed"))
    if completed is None:
        # validate_run_record already FAILs a missing/unparseable completed.
        return

    later: list[tuple[str, Any]] = []
    ver = run.get("verification") if isinstance(run.get("verification"), dict) else {}
    iters = ver.get("iterations") if isinstance(ver.get("iterations"), list) else []
    for idx, it in enumerate(iters, start=1):
        if not isinstance(it, dict):
            continue
        ended = _parse_iso_utc(it.get("ended_at"))
        if ended is not None and ended > completed:
            n = it.get("n", it.get("iteration", idx))
            later.append((f"verification iteration {n}", it.get("ended_at")))
    subs = run.get("sub_agents") if isinstance(run.get("sub_agents"), dict) else {}
    for name, sa in subs.items():
        if not isinstance(sa, dict):
            continue
        ended = _parse_iso_utc(sa.get("ended_at"))
        if ended is not None and ended > completed:
            later.append((f"sub_agent {name}", sa.get("ended_at")))

    if not later:
        if not store_mode:   # one line per record would drown --all
            ok("run-completion",
               f"completed={run.get('completed')} postdates every recorded "
               f"sub-agent and verifier timestamp")
        return

    worst = max(later, key=lambda p: _parse_iso_utc(p[1]) or completed)
    skew = ((_parse_iso_utc(worst[1]) or completed) - completed).total_seconds() / 60
    msg = (f"{rid}: completed={run.get('completed')} precedes {len(later)} of the "
           f"record's own child timestamps — latest is {worst[0]} at {worst[1]}, "
           f"{skew:.0f} min later. `completed` and `duration_seconds` must be "
           f"stamped in Phase 6 immediately before the commit, after the verifier "
           f"loop, not from a Phase 5 `main.ended_at`. An understated duration "
           f"blinds the {RUNAWAY_RUN_SECONDS // 3600} h wall-clock watchdog, which "
           f"is checked against exactly this number")
    (warn if store_mode else fail)("run-completion", msg)


def check_attack_dataset() -> dict[str, Any]:
    """attack/enterprise-attack.json is present and passes the
    tools/attack_data.py invariants. FAIL when missing or broken — the
    pinned ATT&CK release is what entity TTP sections, the /attack/ matrix
    and the technique-id checks below all render and validate against
    (contract: attack/README.md). Always resolved in the repo, like
    state/ and sources/ — never under --root."""
    rel = "attack/enterprise-attack.json"
    path = ROOT / "attack" / "enterprise-attack.json"
    if not path.exists():
        fail("attack-dataset",
             f"{rel} missing — run `python3 tools/attack_data.py --update`")
        return {}
    try:
        ds = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        fail("attack-dataset", f"{rel} unparseable: {e}")
        return {}
    try:
        tools_dir = str(ROOT / "tools")
        if tools_dir not in sys.path:
            sys.path.insert(0, tools_dir)
        import attack_data
        errs = attack_data.selftest(ds)
    except Exception as e:  # noqa: BLE001
        errs = [f"cannot run tools/attack_data.py invariants: {e}"]
    if errs:
        for e in errs[:20]:
            fail("attack-dataset", e)
        if len(errs) > 20:
            fail("attack-dataset", f"… and {len(errs) - 20} more invariant violations")
        return {}
    c = ds.get("counts") or {}
    ok("attack-dataset",
       f"ATT&CK v{ds.get('attack_version')} · {c.get('techniques_active')} active "
       f"techniques · {c.get('tactics')} tactics")
    return ds


def check_attack_mapping(scope_entries: list[dict], attack: dict[str, Any],
                         *, store_mode: bool = False, enforce: bool = False,
                         strict_ids: bool = False) -> None:
    """Entry technique ids vs the pinned ATT&CK release, plus mapping
    COMPLETENESS. Id *format* is already a FAIL in entry schema; here:

      - `techniques[]` id unknown to the pin → WARN (typo, or the pin is
        older than the id — run `tools/attack_data.py --check`); FAIL on
        v3.21+ run scope (`strict_ids`) — the pin is on disk at compose
        time, so a new entry shipping a dead id is a composition defect
      - id revoked/deprecated upstream → WARN (forward pointer to
        survivor); FAIL on v3.21+ run scope (`strict_ids`)
      - run scope only: the body names ATT&CK ids in prose but
        `techniques[]` is empty / incomplete → WARN (the machine retrieval
        layer is missing its mirror; prompts v3.17+ compose frontmatter-first)
      - run scope only: a behavior-kind entry (ATTACK_REQUIRED_KINDS) with
        an EMPTY `techniques[]` → FAIL under `enforce` (v3.18: threat /
        incident / vulnerability entries always support at least the access
        or exploitation vector — an empty mapping is a composition defect),
        WARN on pre-v3.18 records; research/annual-report empty → WARN.

    In --all/store mode only the frontmatter-id checks run here: legacy
    entries are immutable and carry prose-only mappings by design (the site
    derives them). Store-wide completeness for v3.18+ runs is enforced by
    check_store_ratings."""
    techniques = attack.get("techniques") or {}
    if not techniques:
        warn("attack-mapping", "skipped — no usable ATT&CK dataset (see attack-dataset)")
        return
    version = attack.get("attack_version")
    n_issues = 0
    n_mapped = 0
    for e in scope_entries:
        eid = e.get("id", "<unknown>")
        fm = [t for t in (e.get("techniques") or []) if isinstance(t, str)]
        if fm:
            n_mapped += 1
        id_report = fail if strict_ids else warn
        for t in fm:
            rec = techniques.get(t)
            if rec is None:
                n_issues += 1
                id_report("attack-mapping",
                          f"{eid}: techniques[] id {t} unknown to pinned ATT&CK v{version} — "
                          "typo, or the pin is stale (python3 tools/attack_data.py --check)")
            elif rec.get("revoked"):
                n_issues += 1
                fwd = rec.get("revoked_by")
                id_report("attack-mapping",
                          f"{eid}: techniques[] id {t} is revoked upstream"
                          + (f" — superseded by {fwd}; reference the surviving id" if fwd else ""))
            elif rec.get("deprecated"):
                n_issues += 1
                id_report("attack-mapping", f"{eid}: techniques[] id {t} is deprecated upstream")
        if store_mode:
            continue
        kind = str(e.get("kind") or "")
        if not fm and kind in ATTACK_REQUIRED_KINDS:
            n_issues += 1
            msg = (f"{eid}: {kind} entry with empty techniques[] — attacker-behavior "
                   "kinds always support at least one mapping (the access or "
                   "exploitation vector); map every technique the sources support")
            (fail if enforce else warn)("attack-mapping", msg)
        elif not fm and kind in ATTACK_EXPECTED_KINDS:
            n_issues += 1
            warn("attack-mapping",
                 f"{eid}: {kind} entry with empty techniques[] — map the described "
                 "tradecraft unless the piece genuinely carries no TTP content")
        prose = sorted({
            m for m in cm.PROSE_TECHNIQUE_RE.findall(e.get("body") or "")
            if m in techniques
        })
        if prose and not fm:
            n_issues += 1
            head = ", ".join(prose[:5]) + (" …" if len(prose) > 5 else "")
            warn("attack-mapping",
                 f"{eid}: body names {len(prose)} ATT&CK id(s) ({head}) but techniques[] "
                 "is empty — mirror every mapped behavior into the frontmatter "
                 "(machine retrieval layer)")
        else:
            missing = [t for t in prose if t not in set(fm)]
            if fm and missing:
                n_issues += 1
                warn("attack-mapping",
                     f"{eid}: prose ids missing from techniques[]: {', '.join(missing[:8])}")
    if not n_issues:
        scope_word = "entries" if len(scope_entries) != 1 else "entry"
        ok("attack-mapping",
           f"{len(scope_entries)} {scope_word} consistent with pinned ATT&CK v{version} "
           f"({n_mapped} carrying techniques[])")


def check_org_triage(run_entries: list[dict], profile: dict[str, Any] | None,
                     *, enforce: bool = False) -> None:
    """org_triage consistency with the profiled triage scheme. When the org
    profile defines vulnerability_triage categories, every triage-kind entry
    of this run MUST carry org_triage with a defined category id — FAIL under
    `enforce` (v3.18: no entry ships unrated), WARN on pre-v3.18 records.
    When no scheme is configured, any non-null org_triage is drift (WARN) and
    the rating duty moves to check_classification (triage kinds then carry
    the Admiralty block). Criteria *consistency* (does the category follow
    from the cited facts?) is the verifier's F16 concern — this check is
    mechanical only."""
    if profile is None:
        ok("org-triage", "org profile not available — n/a")
        return
    vt = profile.get("vulnerability_triage") or {}
    cats = {c.get("id") for c in (vt.get("categories") or []) if isinstance(c, dict) and c.get("id")}
    triage_kinds = _triage_kinds(profile)
    problems: list[str] = []
    found = 0
    for e in run_entries:
        ot = e.get("org_triage")
        if not cats:
            if ot is not None:
                problems.append(f"{e['id']}: org_triage present but the profile defines no scheme")
            continue
        if e.get("kind") in triage_kinds:
            if not isinstance(ot, dict):
                problems.append(f"{e['id']}: {e.get('kind')} (triage-kind) entry missing org_triage")
            elif ot.get("category") not in cats:
                problems.append(
                    f"{e['id']}: unknown triage category {ot.get('category')!r} "
                    f"(defined: {sorted(cats)})")
            else:
                found += 1
    if problems:
        # A missing/unknown rating on a scheme-configured deployment is a
        # hard defect from v3.18; scheme-less drift stays a WARN either way.
        sev = fail if (enforce and cats) else warn
        for p in problems[:8]:
            sev("org-triage", p)
        if len(problems) > 8:
            sev("org-triage", f"(+{len(problems) - 8} more)")
    elif not cats:
        ok("org-triage", "no triage scheme configured and no org_triage values present "
                         "(triage kinds carry the Admiralty classification instead)")
    else:
        ok("org-triage", f"{found} org_triage block(s), all category ids valid")


def check_classification(run_entries: list[dict], profile: dict[str, Any] | None,
                         *, enforce: bool = False) -> None:
    """Intelligence-classification (NATO Admiralty) consistency with the
    profile's configured scheme.

    Which entries MUST carry the block: every non-triage kind always; the
    triage kinds too when NO vulnerability-triage scheme is configured
    (v3.18 — the triage-kind exemption exists only while a triage scheme
    does, so no entry ever ships unrated). A missing block on a required
    entry is a FAIL under `enforce` (v3.18+ runs) and a WARN on earlier
    records — historical pre-scheme entries are immutable and stay green.
    An out-of-vocabulary reliability/credibility code is always a FAIL (a
    real defect on a fresh entry). Whether the letter fits the source and
    the number fits the corroboration is the verifier's F17 concern — this
    is mechanical only."""
    if profile is None:
        ok("classification", "org profile not available — n/a")
        return
    cl = profile.get("classification") or {}
    ic = cl.get("intel_classification") or {}
    triage_kinds = _triage_kinds(profile)
    triage_scheme = _triage_scheme_configured(profile)
    rel_codes = {str(c.get("code")) for c in (ic.get("reliability") or []) if isinstance(c, dict)}
    cred_codes = {str(c.get("code")) for c in (ic.get("credibility") or []) if isinstance(c, dict)}
    configured = bool(rel_codes and cred_codes)
    fails: list[str] = []
    missing: list[str] = []
    warns: list[str] = []
    found = 0
    for e in run_entries:
        cls = e.get("classification")
        kind = e.get("kind")
        if not configured:
            if cls is not None:
                warns.append(f"{e['id']}: classification present but no intel-classification scheme is configured")
            continue
        if kind in triage_kinds and triage_scheme:
            # A configured triage scheme owns these kinds (org_triage).
            if cls is not None:
                warns.append(f"{e['id']}: {kind} (triage-kind) entry carries classification — triage kinds use org_triage, not the Admiralty code")
            continue
        if not isinstance(cls, dict):
            hint = (" (no triage scheme is configured, so triage kinds carry the "
                    "Admiralty block too — no entry ships unrated)"
                    if kind in triage_kinds else "")
            missing.append(f"{e['id']}: {kind} entry missing classification "
                           f"(Admiralty reliability + credibility){hint}")
            continue
        rel = str(cls.get("reliability") or "")
        cred = str(cls.get("credibility") if cls.get("credibility") is not None else "")
        bad = False
        if rel not in rel_codes:
            fails.append(f"{e['id']}: reliability {rel!r} not in {sorted(rel_codes)}")
            bad = True
        if cred not in cred_codes:
            fails.append(f"{e['id']}: credibility {cred!r} not in {sorted(cred_codes)}")
            bad = True
        if not bad:
            found += 1
        # Credibility 1 MEANS "corroborated by other independent sources".
        # An entry that simultaneously declares itself single-source is
        # contradicting its own frontmatter — mechanical, not judgment, and
        # therefore the gate's job rather than an expensive verifier
        # iteration's (v3.31; two of this window's seven F17 findings were
        # exactly this shape, e.g. 2026-08-05).
        if str(cls.get("credibility")) == "1" and str(e.get("verification") or "").startswith("single-source"):
            fails.append(
                f"{e['id']}: credibility 1 (\"corroborated by other independent sources\") "
                f"contradicts verification: {e.get('verification')!r} — a single "
                "uncorroborated claim from a reliable source is credibility 2. "
                "Independence means a second party that observed or assessed, not a "
                "second publisher of the same assessment")
    for p in fails:
        fail("classification", p)
    missing_sev = fail if enforce else warn
    for p in missing[:8]:
        missing_sev("classification", p)
    if len(missing) > 8:
        missing_sev("classification", f"(+{len(missing) - 8} more)")
    for p in warns[:8]:
        warn("classification", p)
    if len(warns) > 8:
        warn("classification", f"(+{len(warns) - 8} more)")
    if not fails and not missing and not warns:
        if not configured:
            ok("classification", "no intel-classification scheme configured and no classification values present")
        else:
            ok("classification", f"{found} entr{'y' if found == 1 else 'ies'} carry a valid Admiralty classification")


def check_store_ratings(entries: list[dict], runs: list[dict],
                        profile: dict[str, Any] | None,
                        attack: dict[str, Any]) -> None:
    """--all: every entry belonging to a v3.18+ run must carry its rating
    (the Admiralty classification, or org_triage per the profile's
    triage-kind split) and, on behavior kinds, a non-empty ATT&CK mapping.
    Pre-v3.18 entries are immutable history and stay green — this sweep is
    what keeps `--all` permanently guarding every future report."""
    enforced = {str(r.get("run_id")) for r in runs if _rating_enforced(r)}
    scoped = [e for e in entries if str(e.get("run_id") or "") in enforced]
    v = f"v{RATING_ENFORCED_FROM[0]}.{RATING_ENFORCED_FROM[1]}"
    if not scoped:
        ok("store-ratings", f"no entries from {v}+ runs yet — nothing to enforce")
        return
    ok("store-ratings",
       f"{len(scoped)} entr{'y' if len(scoped) == 1 else 'ies'} from "
       f"{len(enforced)} {v}+ run(s) under the always-rated / always-mapped gate")
    check_org_triage(scoped, profile, enforce=True)
    check_classification(scoped, profile, enforce=True)
    check_attack_mapping(scoped, attack, enforce=True)


def check_sources_touched(run: dict[str, Any], sources_data: dict[str, Any] | None) -> None:
    """At least one source must have `last_successful_fetch == run.date`.
    Otherwise the Ops dashboard's stale-sources panel cannot move and the
    rotation bookkeeping has clearly been skipped. Skipped for migrated
    runs — the v2 bookkeeping for their date is history, not this commit.
    v2 origin: check_sources_touched_today."""
    if run.get("migrated_from"):
        ok("sources-touched", "n/a (migrated run record)")
        return
    if not sources_data:
        warn("sources-touched", "sources.json unavailable")
        return
    src_list = sources_data.get("sources") or []
    if not src_list:
        warn("sources-touched", "sources.json contains no sources")
        return
    run_date = str(run.get("date") or "")
    fetched = [s.get("id") for s in src_list if s.get("last_successful_fetch") == run_date]
    if not fetched:
        fail("sources-touched",
             f"no source has last_successful_fetch == {run_date} — "
             "the run's source-bookkeeping phase was not done")
    else:
        ok("sources-touched",
           f"{len(fetched)} source(s) fetched on {run_date} (sample: {fetched[:5]})")


def check_essential_coverage(run: dict[str, Any], sources_data: dict[str, Any] | None) -> None:
    """Every active `tier: essential` source (national CERTs / NCSC / CISA /
    ENISA-class authorities) must be *attempted* on every intel run. Reads
    the union of the record's `sub_agents[*].sources_attempted`. WARN, not
    FAIL — the run must publish regardless; the gap is disclosed and the
    next run's rotation self-heals. Weekly runs are exempt (the guarantee is
    an intel-cadence property; W1/W2 slices are horizon-scoped). Skipped for
    migrated records and records without sub_agents telemetry.
    v2 origin: check_essential_coverage (~lines 1841-1878)."""
    if run.get("migrated_from"):
        ok("essential-coverage", "n/a (migrated run record)")
        return
    if run.get("kind") in ("weekly", "audit"):
        ok("essential-coverage",
           f"n/a for {run.get('kind')} runs (intel-cadence coverage guarantee; "
           "audit sub-agents are retrospective passes, not source slices)")
        return
    subs = run.get("sub_agents")
    if not isinstance(subs, dict) or not subs:
        ok("essential-coverage",
           "skipped — no sub_agents telemetry on this record (run-record check flags the gap)")
        return
    if not sources_data:
        warn("essential-coverage", "sources.json unavailable")
        return
    essential = {s["id"] for s in sources_data.get("sources", [])
                 if s.get("tier") == "essential" and s.get("status") == "active"}
    if not essential:
        warn("essential-coverage", "no active `tier: essential` sources defined in sources.json")
        return
    attempted: set[str] = set()
    for a in subs.values():
        if isinstance(a, dict):
            attempted |= set(a.get("sources_attempted") or [])
    missed = sorted(essential - attempted)
    if missed:
        warn("essential-coverage",
             f"{len(missed)} essential source(s) not attempted this run — an intel run "
             f"must query every national-CERT/NCSC/CISA/ENISA-class source: {missed} "
             "(disclose in the run-record notes; the allocation step must include ALL essential sources)")
    else:
        ok("essential-coverage",
           f"all {len(essential)} essential sources attempted this run")


def check_fetch_failures(run: dict[str, Any]) -> None:
    """The record's fetch_failures[] rich-shape checks (v2 origin:
    check_fetch_source_for_known_403 ~lines 1347-1480, parts 2-3):

    1. **Bridge-required FAIL** (`fetch-failure-bridge-required`) — an entry
       whose `id` matches a bridge-allowlisted source AND whose
       `attempted_methods` contains no `bridge:*` method: the agent went
       direct on a host where `tools/fetch_source.py` was the right first
       move.
    2. **Rich-shape WARN** (`fetch-failure-detail`) — an entry missing one
       of the required rich-shape keys; the Ops dashboard renders these as
       yellow 'needs-detail' rows. Legacy `{id, code}` entries flag here
       too (back-compat shape from migrated v2 records)."""
    failures = run.get("fetch_failures")
    if failures is None:
        failures = []
    if not isinstance(failures, list):
        warn("fetch-failure-detail",
             f"fetch_failures must be a list (got {type(failures).__name__}) — use [] when none")
        return

    bridge_skipped: list[str] = []
    for f_ in failures:
        if not isinstance(f_, dict):
            continue
        sid = str(f_.get("id") or "").lower()
        if not _failure_id_is_bridge_allowlisted(sid):
            continue
        attempted = [m for m in (f_.get("attempted_methods") or []) if isinstance(m, str)]
        if not attempted:
            # Legacy entry — no attempted_methods to judge; the rich-shape
            # WARN below flags it for upgrade instead of double-failing.
            continue
        if not any(m.startswith("bridge:") for m in attempted):
            bridge_skipped.append(
                f"{sid} (attempted_methods={attempted}, no bridge:* present)")
    if bridge_skipped:
        fail(
            "fetch-failure-bridge-required",
            f"bridge subcommand not attempted for bridge-allowlisted source(s): {bridge_skipped}. "
            "These hosts must be fetched via `python3 tools/fetch_source.py …` first; see the "
            "run prompt's per-source subcommand table.",
        )
    elif failures:
        ok("fetch-failure-bridge-required",
           "every fetch_failures entry on the bridge allowlist used a bridge:* method")

    thin_entries: list[str] = []
    for f_ in failures:
        if not isinstance(f_, dict):
            thin_entries.append("non-dict entry")
            continue
        # Legacy {id, code} entries are back-compat — flag once per run.
        is_legacy = "code" in f_ and "url_tried" not in f_ and "attempted_methods" not in f_
        if is_legacy:
            thin_entries.append(f"legacy {{id, code}} for {f_.get('id', '?')}")
            continue
        missing = [k for k in RICH_FAILURE_REQUIRED_KEYS if k not in f_]
        if missing:
            thin_entries.append(f"{f_.get('id', '?')} missing {missing}")
    if thin_entries:
        warn(
            "fetch-failure-detail",
            f"{len(thin_entries)} fetch_failures entr{'y' if len(thin_entries) == 1 else 'ies'} "
            f"missing rich-shape detail (sample: {thin_entries[:3]}). "
            "Sub-agents must include url_tried, fetch_method, status_code, error_class, "
            "attempted_methods, mitigation_applied, covered_anyway — see "
            ".claude/agents/cti-research.md § fetch_failures.",
        )
    elif failures:
        ok("fetch-failure-detail",
           f"all {len(failures)} fetch_failures entr{'y' if len(failures) == 1 else 'ies'} carry the rich shape")
    else:
        ok("fetch-failure-detail", "no fetch failures recorded")


# Signatures that indicate site/test_build.py crashed while importing (the
# site rewrite may be mid-flight) rather than a test assertion failing.
_IMPORT_CRASH_SIGNATURES = (
    "ImportError", "ModuleNotFoundError", "SyntaxError", "cannot import name",
)


def check_test_build(skip: bool) -> None:
    """Run site/test_build.py (the build-side smoke tests). Failure here
    means the entries will not render correctly even if their own metadata
    is clean. A missing script or an import-time crash is a WARN, not a
    FAIL — during the v3 site rewrite the test module may legitimately be
    absent or transitional, and the gate must not block the content
    pipeline on the renderer's construction site. A real assertion failure
    stays a FAIL. v2 origin: check_test_build."""
    if skip:
        warn("test-build", "skipped (--no-build-tests)")
        return
    if not TEST_BUILD.exists():
        warn("test-build", f"{TEST_BUILD.relative_to(ROOT)} missing (site rewrite in flight?)")
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
        return
    combined = (proc.stderr or "") + (proc.stdout or "")
    if any(sig in combined for sig in _IMPORT_CRASH_SIGNATURES):
        tail = combined.strip().splitlines()[-5:]
        warn("test-build",
             "site/test_build.py crashed at import (site rewrite in flight?) — "
             "not treated as a content failure; tail:\n        " + "\n        ".join(tail))
        return
    tail = (proc.stdout or "").splitlines()[-20:] + (proc.stderr or "").splitlines()[-10:]
    fail("test-build", "site/test_build.py failed; tail:\n        " +
         "\n        ".join(tail))


# --- --all mode (whole-store validation) -------------------------------------


def check_entry_id_uniqueness(entries: list[dict]) -> None:
    """Entry ids are path-derived (YYYY-MM-DD/slug) so the filesystem makes
    duplicates structurally hard — this guards the residual cases (a
    tolerant-collector bug, case-folding filesystems, future non-path id
    sources) so downstream update_of/references links stay unambiguous."""
    seen: dict[str, int] = {}
    dupes: list[str] = []
    for e in entries:
        seen[e["id"]] = seen.get(e["id"], 0) + 1
    dupes = [i for i, n in seen.items() if n > 1]
    if dupes:
        fail("entry-ids", f"duplicate entry id(s): {dupes[:5]}")
    else:
        ok("entry-ids", f"{len(seen)} entry id(s) unique")


def check_references_resolve(entries: list[dict], entries_by_id: dict[str, dict]) -> None:
    """--all: every update_of and references[] value must resolve to an
    existing entry file (globally). Per-run mode covers update_of via the
    dedup check; this is the store-wide sweep.

    Severity follows commit state (same pattern as check_prompt_version): a
    dangling link on an UNCOMMITTED (new/modified) entry FAILs — this is the
    moment it must be fixed, the target was mistyped or never written. A
    dangling link on an already-committed entry WARNs: entries are immutable
    once committed, so a historical dangling link is normally unrepairable in
    place, and a permanent FAIL would keep `--all` red forever — training the
    operator to ignore it and masking NEW failures. The WARN keeps the defect
    visible without poisoning the exit code. (The four 2026-05/06 dangling
    links from the v2->v3 migration were repaired on 2026-07-09 by a one-time
    operator-authorized immutability exception — frontmatter `update_of`
    repointed to the surviving migrated targets, bodies untouched; see
    .claude/memory/entry-immutability-exceptions.md.)"""
    dirty: set[str] | None = None
    try:
        proc = subprocess.run(
            ["git", "status", "--porcelain", "--", "entries/"],
            capture_output=True, text=True, cwd=ROOT, timeout=15)
        if proc.returncode == 0:
            dirty = {ln[3:].strip().strip('"') for ln in proc.stdout.splitlines() if ln.strip()}
    except Exception:
        dirty = None  # git unavailable (fixture root) → conservative: treat all as uncommitted
    entry_rel = lambda e: f"entries/{e.get('id', '')}.md"  # noqa: E731 — id is YYYY-MM-DD/slug

    bad_new: list[str] = []
    bad_old: list[str] = []
    for e in entries:
        problems = []
        upd = e.get("update_of")
        if upd and str(upd) not in entries_by_id:
            problems.append(f"{e['id']}: update_of {upd!r} does not resolve")
        for ref in e.get("references") or []:
            if str(ref) not in entries_by_id:
                problems.append(f"{e['id']}: references value {ref!r} does not resolve")
        if not problems:
            continue
        committed = dirty is not None and entry_rel(e) not in dirty
        (bad_old if committed else bad_new).extend(problems)
    for b in bad_new[:12]:
        fail("references", b)
    if len(bad_new) > 12:
        fail("references", f"(+{len(bad_new) - 12} more unresolved links on uncommitted entries)")
    for b in bad_old[:12]:
        warn("references", b + " — committed/immutable, grandfathered (WARN, not FAIL)")
    if len(bad_old) > 12:
        warn("references", f"(+{len(bad_old) - 12} more grandfathered unresolved links)")
    if not bad_new and not bad_old:
        ok("references", "all update_of / references links resolve to existing entries")


def check_all_run_records(runs: list[dict]) -> None:
    """--all: strict validate_run_record on every record EXCEPT those
    carrying `migrated_from` — migrated v2 records predate the v3 telemetry
    contract (sub_agents shape, verification arithmetic) and get only a
    minimal identity check: the file parsed (the tolerant collector already
    failed it otherwise) and run_id / date / kind are present."""
    n_err = 0
    n_migrated = 0
    now = datetime.now(timezone.utc)
    for r in runs:
        if r.get("migrated_from"):
            n_migrated += 1
            missing = [f for f in ("run_id", "date", "kind") if not r.get(f)]
            if missing:
                n_err += 1
                fail("run-record", f"{r.get('path', r.get('run_id'))}: migrated record missing {missing}")
            continue
        for e in cm.validate_run_record(r):
            n_err += 1
            fail("run-record", e)
        # Phase 7 follow-through: a v3.14+ record still carrying no
        # publish_status a day after it started means the publish-status
        # amendment never landed — the operator cannot tell from state
        # whether the run reached the site (observed: 2026-07-09T1211Z).
        v = _prompt_version_tuple(r.get("prompt_version"))
        if (v is not None and v >= PUBLISH_TELEMETRY_FROM
                and not r.get("publish_status")):
            started = _parse_iso_utc(r.get("started"))
            if started is not None and (now - started).total_seconds() > 86400:
                warn("run-record",
                     f"{r.get('run_id')}: no publish_status >24 h after the run "
                     "started — the Phase 7 publish-status amendment never landed; "
                     "verify the run reached main and the site, then amend the record")
        dur = r.get("duration_seconds")
        if isinstance(dur, (int, float)) and dur > RUNAWAY_RUN_SECONDS:
            warn("run-record",
                 f"{r.get('run_id')}: duration_seconds={int(dur)} (~{dur / 3600:.1f} h) "
                 "exceeded the runaway threshold — see the per-run watchdog note")
        # v3.23+ double-CLEAN gate, store severity (immutable history → WARN)
        check_verification_confirmation(r, store_mode=True)
        # v3.32+ completion-covers-run, store severity (immutable → WARN)
        check_completion_covers_run(r, store_mode=True)
    if not n_err:
        ok("run-record",
           f"{len(runs)} run record(s) valid ({n_migrated} migrated, identity-checked only)")


def run_all_checks(entries: list[dict], runs: list[dict], taxonomy: dict,
                   registry: dict, parsed_state: dict[str, Any],
                   *, skip_build_tests: bool) -> None:
    """--all mode body: whole-store validation. No URL liveness (hundreds of
    historical URLs — link rot on old entries is not a commit defect), no
    rolling-24 h composition report, no per-run dedup/counter cross-checks."""
    entries_by_id = {e["id"]: e for e in entries}
    registry_keys = set(registry.keys())

    print("\n== all: entry-id uniqueness ==")
    check_entry_id_uniqueness(entries)

    print("\n== all: entry schema (incl. folder-date == discovered_at, registry refs) ==")
    n_err = 0
    for e in entries:
        for err in cm.validate_entry(e, taxonomy, registry_keys):
            fail("entry-schema", err)
            n_err += 1
    if not n_err:
        ok("entry-schema", f"all {len(entries)} entr{'y' if len(entries) == 1 else 'ies'} pass validate_entry")

    print("\n== all: update_of / references resolution + cycles ==")
    check_references_resolve(entries, entries_by_id)
    check_update_targets(entries, entries_by_id)

    print("\n== all: CVE sync ==")
    check_cve_sync(entries, parsed_state.get("cves_seen.json"), scope_label="store")

    print("\n== all: ATT&CK dataset + techniques[] ids ==")
    attack_ds = check_attack_dataset()
    # v3.18+ entries get the full (completeness-enforcing) pass below;
    # legacy entries get the id-drift pass only.
    enforced_run_ids = {str(r.get("run_id")) for r in runs if _rating_enforced(r)}
    legacy_entries = [e for e in entries
                      if str(e.get("run_id") or "") not in enforced_run_ids]
    check_attack_mapping(legacy_entries, attack_ds, store_mode=True)

    print("\n== all: rating + mapping completeness (always-classified gate) ==")
    check_store_ratings(entries, runs, _load_org_profile(), attack_ds)

    print("\n== all: run records ==")
    check_all_run_records(runs)

    print("\n== build-side smoke tests ==")
    check_test_build(skip_build_tests)


# --- Driver ------------------------------------------------------------------


def run_checks(run_arg: str | None, *, all_mode: bool, skip_build_tests: bool,
               skip_link_check: bool, content_root: Path,
               pre_verify: bool = False) -> int:
    entries_dir = content_root / "entries"
    runs_dir = content_root / "runs"
    registry_path = content_root / "entities" / "registry.yaml"

    scope = "--all (whole content store)" if all_mode else (run_arg or "latest run")
    print(f"check_run.py — scope: {scope}")
    if content_root != ROOT:
        print(f"content root: {content_root} (state/sources/taxonomy from {ROOT})")
    print()

    # -- store-level checks (always) --
    print("== store: state / sources JSON ==")
    parsed_state = check_state_json_valid()
    sources_data = parsed_state.get("sources.json")

    print("\n== store: taxonomy ==")
    taxonomy = check_taxonomy_loadable()

    print("\n== store: sources.json schema (shape + controlled-vocab) ==")
    check_sources_schema(sources_data)

    print("\n== store: content parse ==")
    entries, entry_errors = collect_entries_tolerant(entries_dir, content_root)
    runs, run_errors = collect_runs_tolerant(runs_dir, content_root)

    # Registry after content parse: relation source-entry resolution needs
    # the entry-id set.
    print("\n== store: entity registry ==")
    registry = check_registry(registry_path, entries)
    for err in entry_errors:
        fail("entry-parse", f"entries/{err}")
    for err in run_errors:
        fail("run-parse", f"runs/{err}")
    if not entry_errors and not run_errors:
        ok("store-parse", f"{len(entries)} entry file(s) + {len(runs)} run record(s) parse cleanly")

    if all_mode:
        run_all_checks(entries, runs, taxonomy, registry, parsed_state,
                       skip_build_tests=skip_build_tests)
        return _summary()

    # -- run-scope selection --
    run: dict[str, Any] | None = None
    if run_arg is None:
        if not runs:
            print("\nFATAL: no run records found under runs/ — nothing to check "
                  "(after the first v3 run fires, the latest record is selected automatically)")
            return 2
        run = runs[-1]  # collect_runs_tolerant sorts by (started, run_id) ascending
    else:
        for r in runs:
            if r.get("run_id") == run_arg:
                run = r
        if run is None and not any(e.get("run_id") == run_arg for e in entries):
            print(f"\nFATAL: run id {run_arg!r} matches no run record and no entry — "
                  "check the id (runs/<date>/<run-id>.md)")
            return 2

    run_id = str(run.get("run_id")) if run is not None else str(run_arg)
    run_entries = [e for e in entries if e.get("run_id") == run_id]
    entries_by_id = {e["id"]: e for e in entries}
    print(f"\nrun scope: {run_id} · {len(run_entries)} entr{'y' if len(run_entries) == 1 else 'ies'}\n")

    print("== run record ==")
    check_run_record(run, run_id, content_root, pre_verify=pre_verify)

    if run is not None:
        print("\n== verification double-CLEAN (v3.23 gate) ==")
        check_verification_confirmation(run, pre_verify=pre_verify)

        print("\n== completion timestamp covers the whole fire (v3.32) ==")
        check_completion_covers_run(run)

        print("\n== prompt-version vs CHANGELOG ==")
        check_prompt_version(run, content_root)

        print("\n== run counters vs disk ==")
        check_run_counters(run, run_entries)

    print("\n== entry schema ==")
    check_entry_schema(run_entries, taxonomy, set(registry.keys()))

    if run is not None:
        print("\n== entry ↔ run time binding ==")
        check_entry_run_binding(run, run_entries)

        print("\n== cross-run dedup (14-day window) ==")
        check_dedup(run, run_entries, entries, entries_by_id, registry)

    print("\n== update-chain integrity ==")
    check_update_targets(run_entries, entries_by_id)

    if run is not None:
        print("\n== rolling-24h composition (informational) ==")
        report_rolling_composition(run, entries)

    print("\n== IOC scan ==")
    check_no_iocs(run_entries)

    print("\n== blocked source patterns (NVD per-CVE / generic landings / indexes) ==")
    check_blocked_sources(run_entries)

    print("\n== evidence binding ==")
    check_evidence_binding(run_entries)

    print("\n== single-source / national-CERT consistency ==")
    check_single_source_flags(run_entries)

    print("\n== aggregator-only sourcing ==")
    check_aggregator_only(run_entries)

    print("\n== action-item discipline (do-now bar) ==")
    check_actions_discipline(run_entries, run)

    profile = _load_org_profile()
    print("\n== closed-source citations (traceability, no TLP gate) ==")
    check_closed_sources(run_entries, profile)

    # From prompt v3.18, a missing rating or a missing behavior-kind ATT&CK
    # mapping is a hard gate failure; earlier records keep WARN severity.
    enforce_ratings = _rating_enforced(run)

    print("\n== org-triage ==")
    check_org_triage(run_entries, profile, enforce=enforce_ratings)

    print("\n== classification (NATO Admiralty) ==")
    check_classification(run_entries, profile, enforce=enforce_ratings)

    print("\n== CVE sync ==")
    check_cve_sync(run_entries, parsed_state.get("cves_seen.json"))

    print("\n== ATT&CK dataset + technique mapping ==")
    attack_ds = check_attack_dataset()
    check_attack_mapping(run_entries, attack_ds, enforce=enforce_ratings,
                         strict_ids=_mapping_ids_strict(run))

    if run is not None:
        print("\n== sources.json bookkeeping ==")
        check_sources_touched(run, sources_data)

        print("\n== essential-source coverage ==")
        check_essential_coverage(run, sources_data)

        print("\n== fetch failures (rich shape + bridge allowlist) ==")
        check_fetch_failures(run)

    print("\n== source URL liveness (HEAD/GET every source link of this run) ==")
    check_source_urls_resolve(run_entries, skip=skip_link_check)

    print("\n== build-side smoke tests ==")
    check_test_build(skip_build_tests)

    return _summary()


def _summary() -> int:
    print()
    acked = f" · {len(ACKED)} acknowledged" if ACKED else ""
    print(f"summary: {len(PASSES)} pass · {len(WARNS)} warn · "
          f"{len(FAILS)} fail{acked}")
    if FAILS:
        print("\nFAILURES:")
        for f_ in FAILS:
            print(f"  - {f_}")
    if WARNS:
        print("\nWARNINGS (not blocking, but the zero-warning discipline "
              "applies — fix what this run caused before commit; the weekly "
              "audit sweeps the rest to zero):")
        for w in WARNS:
            print(f"  - {w}")
    if ACKED:
        print("\nACKNOWLEDGED (settled history per "
              "state/warning_acknowledgments.json — reviewed by the weekly "
              "audit, not counted as warnings):")
        for a in ACKED:
            print(f"  - {a}")
    return 1 if FAILS else 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("run_id", nargs="?", default=None,
                   help="run id (e.g. 2026-07-03T0412Z-intel); defaults to the latest "
                        "run record by `started`")
    p.add_argument("--all", action="store_true",
                   help="validate the whole content store (every entry + registry + every "
                        "run record; skips liveness, composition report and per-run strict "
                        "checks on migrated records)")
    p.add_argument("--no-build-tests", action="store_true",
                   help="skip running site/test_build.py")
    p.add_argument("--no-link-check", action="store_true",
                   help="skip the live HEAD/GET check on every source URL (offline runs)")
    p.add_argument("--root", default=None, metavar="PATH",
                   help="resolve entries/, runs/ and entities/registry.yaml under PATH "
                        "instead of the repo root (self-test fixtures); state, sources, "
                        "taxonomy, prompts, work/ and intel/ always resolve in the repo")
    p.add_argument("--pre-verify", action="store_true",
                   help="Phase 5.5 gate run BEFORE the first Phase 5.7 verifier spawn: "
                        "verification-block completeness errors on the run record "
                        "(empty verification.iterations, missing verdict/residual) are "
                        "WARNs instead of FAILs — they can only be populated by the "
                        "verifier loop. Never use between fix iterations or before "
                        "commit; the plain invocation enforces the full contract there")
    args = p.parse_args()
    if args.all and args.run_id:
        print("FATAL: --all and an explicit run id are mutually exclusive")
        return 2
    if args.all and args.pre_verify:
        print("FATAL: --pre-verify applies to a single run's pre-Phase-5.7 gate, not --all")
        return 2
    content_root = Path(args.root).resolve() if args.root else ROOT
    return run_checks(
        args.run_id,
        all_mode=args.all,
        skip_build_tests=args.no_build_tests,
        skip_link_check=args.no_link_check,
        content_root=content_root,
        pre_verify=args.pre_verify,
    )


if __name__ == "__main__":
    sys.exit(main())
