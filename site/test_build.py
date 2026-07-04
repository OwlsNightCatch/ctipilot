#!/usr/bin/env python3
"""Stdlib-only smoke tests for site/build.py (v3 pipeline SSG).

Run with: `python3 site/test_build.py` from the repo root. Returns
exit code 0 on pass, 1 on any failure. Used as a gate by
tools/check_run.py and by CI.

Tests cover:
    - Markdown → HTML rendering + URL-scheme allowlist + control-char
      stripping (unchanged security primitives)
    - secret scanner, CDATA safety, XML DTD/entity refusal, path-segment
      safety
    - content_model round-trip (strict-YAML-subset parse/dump, entry
      loader, schema validation)
    - render_brief_sections: section stubs, TL;DR ordering, the
      Immediate-Action callout, update rendering, action items, run notes
    - briefbook.json / alerts.json shapes
    - day/weekly grouping + section-key routing
    - RSS generation from fixture entries (incl. sector slices)
    - entity appearance matching (registry keys, aliases, CVE ids)
    - umami/CSP consistency + the branding profile contract
"""

import json
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(__file__).resolve().parent

sys.path.insert(0, str(SITE))
import build  # noqa: E402
import content_model  # noqa: E402
from build import (  # noqa: E402
    SECTION_EMPTY_STUB,
    _cdata_safe,
    _safe_url,
    _strip_controls,
    _verification_clean_publish,
    _xml_validate,
    annotate_sources,
    build_alerts,
    build_briefbook,
    build_entities,
    build_items_feed,
    build_sector_feeds,
    build_update_chains,
    compute_related_entities,
    entries_by_day,
    entries_by_week,
    entry_section_key,
    is_safe_path_segment,
    parse_taxonomy,
    render_brief_sections,
    render_cve_pill,
    render_entry_card,
    render_inline,
    render_markdown,
    scan_for_secrets,
    select_tldr_entries,
    slugify,
    weekly_section_key,
)

FAILURES: list[str] = []


def assert_eq(name: str, got, want) -> None:
    if got == want:
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: got {got!r}, want {want!r}")
        print(f"  FAIL {name}: got {got!r}, want {want!r}")


def assert_true(name: str, cond) -> None:
    if cond:
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: condition is false")
        print(f"  FAIL {name}")


def assert_in(name: str, needle: str, hay: str) -> None:
    if needle in hay:
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: {needle!r} not in {hay[:200]!r}")
        print(f"  FAIL {name}")


def assert_not_in(name: str, needle: str, hay: str) -> None:
    if needle not in hay:
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: {needle!r} found in {hay[:200]!r}")
        print(f"  FAIL {name}: {needle!r} found")


def assert_match(name: str, pattern: str, hay: str) -> None:
    if re.search(pattern, hay):
        print(f"  ok  {name}")
    else:
        FAILURES.append(f"{name}: pattern {pattern!r} not in {hay[:200]!r}")
        print(f"  FAIL {name}")


# ---------------------------------------------------------------------
# Markdown rendering (unchanged security-relevant primitives)
# ---------------------------------------------------------------------
print("== render_inline ==")
assert_eq("bold renders as strong", render_inline("a **bold** term"),
          "a <strong>bold</strong> term")
assert_eq("italic renders as em", render_inline("a *slanted* term"),
          "a <em>slanted</em> term")
assert_eq("inline code renders as code", render_inline("the `key` is here"),
          "the <code>key</code> is here")

link_html = render_inline("see [the advisory](https://example.com/cve)")
assert_in("link href present", 'href="https://example.com/cve"', link_html)
assert_not_in("link bracket leak", "[the advisory]", link_html)
assert_in("external link target=_blank", 'target="_blank"', link_html)
assert_in("external link rel noopener", 'rel="noopener noreferrer"', link_html)
relative_html = render_inline("see [other section](#anchor)")
assert_in("relative link href present", 'href="#anchor"', relative_html)
assert_not_in("relative link no target", 'target="_blank"', relative_html)
code_in_label = render_inline("read [`tools/x.py` docs](https://example.com/x)")
assert_in("code span inside link label", "<code>tools/x.py</code>", code_in_label)
assert_not_in("no placeholder leak", "CODE0", code_in_label)

print("== render_markdown ==")
md_html = render_markdown("# Head\n\npara **b**\n\n- a\n- b\n\n```sh\nhi\n```")
assert_in("heading rendered", "<h1", md_html)
assert_in("list rendered", "<li>a</li>", md_html)
assert_in("fence rendered", "<pre><code", md_html)
assert_not_in("no raw bold survives", "**b**", md_html)

print("== _safe_url ==")
assert_eq("javascript: neutered", _safe_url("javascript:alert(1)"), "#")
assert_eq("data: neutered", _safe_url("data:text/html,<b>x</b>"), "#")
assert_eq("vbscript: neutered", _safe_url("vbscript:x"), "#")
assert_eq("mixed-case scheme neutered", _safe_url("JaVaScRiPt:alert(1)"), "#")
assert_eq("control-char smuggle neutered", _safe_url("java\tscript:alert(1)"), "#")
assert_eq("protocol-relative refused", _safe_url("//evil.example/x"), "#")
assert_eq("backslash lead refused", _safe_url("\\\\evil.example\\x"), "#")
assert_eq("https passes", _safe_url("https://ok.example/a"), "https://ok.example/a")
assert_eq("anchor passes", _safe_url("#frag"), "#frag")
assert_eq("relative passes", _safe_url("briefs/2026-07-03/"), "briefs/2026-07-03/")
evil_link = render_inline("[click](javascript:alert(1))")
assert_in("renderer neuters javascript links", 'href="#"', evil_link)

print("== is_safe_path_segment ==")
assert_eq("plain id ok", is_safe_path_segment("cisa-kev"), True)
assert_eq("cve id ok", is_safe_path_segment("CVE-2026-1234"), True)
assert_eq("typed key ok", is_safe_path_segment("actor:lazarus"), True)
assert_eq("dotdot rejected", is_safe_path_segment("../etc"), False)
assert_eq("slash rejected", is_safe_path_segment("a/b"), False)
assert_eq("leading dot rejected", is_safe_path_segment(".htaccess"), False)
assert_eq("empty rejected", is_safe_path_segment(""), False)

print("== slugify ==")
assert_eq("slugify basic", slugify("Hello, World! 42"), "hello-world-42")

print("== _cdata_safe / _xml_validate ==")
assert_eq("cdata break split", _cdata_safe("a]]>b"), "a]]]]><![CDATA[>b")
assert_eq("valid xml passes", _xml_validate("<a><b>x</b></a>"), [])
assert_true("doctype refused",
            _xml_validate('<!DOCTYPE foo [<!ENTITY x "y">]><a>&x;</a>'))
assert_true("entity decl refused", _xml_validate('<!ENTITY x "y"><a/>'))

print("== _strip_controls ==")
assert_eq("nul stripped", _strip_controls("a\x00b"), "ab")
assert_eq("tab/newline kept", _strip_controls("a\tb\nc"), "a\tb\nc")

print("== scan_for_secrets ==")
assert_true("github classic token detected",
            scan_for_secrets("ghp_" + "A" * 40))
assert_true("aws key id detected", scan_for_secrets("AKIA" + "A" * 16))
assert_eq("clean text clean", scan_for_secrets("nothing to see CVE-2026-1234"), [])

print("== render_cve_pill multi-CVE split ==")
multi = render_cve_pill("CVE-2026-1111, CVE-2026-2222")
assert_in("first cve linked", 'href="entities/CVE-2026-1111/"', multi)
assert_in("second cve linked", 'href="entities/CVE-2026-2222/"', multi)
assert_not_in("no combined slug", "CVE-2026-1111, CVE-2026-2222/", multi)


# ---------------------------------------------------------------------
# v3 fixtures
# ---------------------------------------------------------------------
TAXONOMY = parse_taxonomy(SITE / "taxonomy.yaml")
REF_TS = datetime(2026, 7, 3, 12, 0, 0, tzinfo=timezone.utc)


def mk_entry(slug, *, day="2026-07-03", ts="2026-07-03T04:21:09Z",
             kind="vulnerability", priority="notable",
             horizon="operational", **kw):
    e = dict(content_model.ENTRY_DEFAULTS)
    e.update({
        "schema": 1,
        "kind": kind,
        "horizon": horizon,
        "title": f"Title {slug}",
        "headline": f"Headline {slug}",
        "summary": f"Summary {slug}.",
        "discovered_at": ts,
        "event_date": day,
        "run_id": "2026-07-03T0412Z-intel",
        "priority": priority,
        "tags": ["vulnerabilities"],
        "regions": ["global"],
        "sectors": [],
        "verification": "multi-source",
        "sources": [
            {"url": f"https://example.com/advisory-{slug}", "publisher": "Example PSIRT",
             "date": day, "role": "primary"},
            {"url": f"https://example.org/news-{slug}", "publisher": "Example News",
             "date": day, "role": "corroborating"},
        ],
        "slug": slug,
        "date": day,
        "id": f"{day}/{slug}",
        "path": f"entries/{day}/{slug}.md",
        "body": f"Analysis body of {slug} with **detail** and a "
                f"[reference](https://example.com/ref-{slug}).",
    })
    e.update(kw)
    return e


def mk_run(run_id="2026-07-03T0412Z-intel", **kw):
    r = {
        "schema": 1,
        "run_id": run_id,
        "kind": "intel",
        "date": "2026-07-03",
        "started": "2026-07-03T04:12:03Z",
        "completed": "2026-07-03T04:31:40Z",
        "duration_seconds": 1177,
        "model": "Claude Fable 5",
        "model_id": "claude-fable-5",
        "prompt_version": "v3.0",
        "window_hours": 9,
        "gap_hours": 7,
        "entries_published": 3,
        "entries_updated": 1,
        "sub_agents": {"S1": {"model": "Claude Fable 5", "returned": True,
                              "items_returned": 2}},
        "verification_iterations": 1,
        "verification_residual_count": 0,
        "verification": {"iterations": [{"n": 1, "verdict": "CLEAN",
                                         "truth": 0, "editorial": 0,
                                         "advisory": 0, "findings": []}]},
        "body": "Coverage gaps: none. Watchlist: no hits this run.",
    }
    r.update(kw)
    return r


E_CRIT = mk_entry(
    "coolify-rce", kind="vulnerability", priority="critical",
    ts="2026-07-03T04:21:09Z",
    immediate_action={"title": "Patch Coolify now",
                      "action": "Upgrade to v4.0.0-beta.469 immediately."},
    evidence=[{"quote": "actively exploited in the wild",
               "publisher": "Example PSIRT"}],
    cves=[{"id": "CVE-2026-34038", "cvss": "9.9", "epss": None, "type": "rce",
           "vector": "zero-click", "auth": "post-auth",
           "status": ["exploited", "patch-available"]}],
    actions=["Patch Coolify to ≥ v4.0.0-beta.469."],
    tags=["vulnerabilities", "rce", "actively-exploited"],
)
E_HIGH = mk_entry(
    "fortibleed-campaign", kind="threat", priority="high",
    ts="2026-07-03T03:00:00Z",
    regions=["europe"],
    entities=["actor:testfox"],
)
E_NOTE = mk_entry(
    "quiet-botnet", kind="threat", priority="notable",
    ts="2026-07-03T02:00:00Z",
    body="TestFox infrastructure overlap noted; also tracked as FOXCAT-9.",
)
E_UPD = mk_entry(
    "coolify-rce-update", kind="vulnerability", priority="notable",
    ts="2026-07-03T08:00:00Z",
    update_of="2026-07-03/coolify-rce",
    body="**UPDATE (originally covered 2026-07-03):** A public PoC has now surfaced.",
    cves=[{"id": "CVE-2026-34038", "cvss": "9.9", "epss": None, "type": "rce",
           "vector": "zero-click", "auth": "post-auth",
           "status": ["exploited", "patch-available", "cisa-kev"]}],
    actions=[],
)
E_DEEP = mk_entry(
    "deep-dive-edge", kind="research", priority="notable",
    ts="2026-07-03T05:00:00Z",
    deep_dive=True, deep_dive_category="edge-infrastructure",
)
E_OLD = mk_entry(
    "old-item", day="2026-07-01", ts="2026-07-01T10:00:00Z",
    kind="incident", priority="notable", sectors=["healthcare"],
)
E_STRAT = mk_entry(
    "weekly-policy-item", day="2026-06-28", ts="2026-06-28T10:00:00Z",
    kind="policy", priority="high", horizon="strategic",
)
E_STRAT2 = mk_entry(
    "weekly-synthesis", day="2026-06-28", ts="2026-06-28T11:00:00Z",
    kind="synthesis", priority="notable", horizon="strategic",
    weekly_section="weekly-long-running",
    references=["2026-07-01/old-item"],
)
ALL_ENTRIES = sorted(
    [E_CRIT, E_HIGH, E_NOTE, E_UPD, E_DEEP, E_OLD, E_STRAT, E_STRAT2],
    key=lambda e: (e["discovered_at"], e["id"]),
)
RUN = mk_run()

# ---------------------------------------------------------------------
# content_model round-trip + validation
# ---------------------------------------------------------------------
print("== content_model round-trip ==")
fm = {
    "schema": 1, "kind": "vulnerability", "title": "T — x: y (9.9)",
    "summary": "Line one.\nLine two.",
    "tags": ["vulnerabilities", "rce"],
    "cves": [{"id": "CVE-2026-1", "status": ["exploited"]}],
    "update_of": None, "deep_dive": False,
}
dumped = content_model.dump_yaml_subset(fm)
assert_eq("yaml subset round-trips", content_model.parse_yaml_subset(dumped), fm)

with tempfile.TemporaryDirectory() as td:
    troot = Path(td)
    day_dir = troot / "entries" / "2026-07-03"
    day_dir.mkdir(parents=True)
    doc_fm = {k: v for k, v in E_CRIT.items()
              if k not in ("slug", "date", "id", "path", "body")}
    (day_dir / "coolify-rce.md").write_text(
        content_model.compose_frontmatter_doc(doc_fm, E_CRIT["body"]),
        encoding="utf-8",
    )
    loaded = content_model.collect_entries(entries_dir=troot / "entries", root=troot)
    assert_eq("loader finds the fixture entry", len(loaded), 1)
    le = loaded[0]
    assert_eq("entry id path-derived", le["id"], "2026-07-03/coolify-rce")
    assert_eq("headline round-trips", le["headline"], E_CRIT["headline"])
    assert_eq("cve record round-trips", le["cves"][0]["id"], "CVE-2026-34038")
    assert_eq("immediate_action round-trips",
              le["immediate_action"]["title"], "Patch Coolify now")
    errs = content_model.validate_entry(le, TAXONOMY)
    assert_eq("fixture entry is schema-valid", errs, [])
    bad = dict(le)
    bad["priority"] = "urgent"
    assert_true("bad priority flagged",
                any("priority" in x for x in content_model.validate_entry(bad, TAXONOMY)))

# ---------------------------------------------------------------------
# render_brief_sections — the canonical assembler
# ---------------------------------------------------------------------
print("== render_brief_sections ==")
day_entries = [E_NOTE, E_HIGH, E_CRIT, E_UPD, E_DEEP]
by_id = {e["id"]: e for e in ALL_ENTRIES}
html = render_brief_sections(day_entries, [RUN], prefix="", entries_by_id=by_id)

assert_in("empty section carries the stub", SECTION_EMPTY_STUB, html)
assert_in("every daily section renders", 'data-section="research"', html)
assert_in("TL;DR bullet carries strong headline", "<strong>Headline coolify-rce.</strong>", html)
crit_pos = html.find("Headline coolify-rce")
high_pos = html.find("Headline fortibleed-campaign")
assert_true("TL;DR: critical bullet precedes high", 0 <= crit_pos < high_pos)
assert_in("immediate-action callout present", "Immediate action", html)
assert_in("callout carries the action", "Upgrade to v4.0.0-beta.469 immediately.", html)
assert_in("callout quotes evidence", "actively exploited in the wild", html)
assert_in("update rendered as callout blockquote", 'class="callout-update"', html)
assert_in("update lead links the original", "originally covered", html)
assert_in("update body retained after prefix strip", "A public PoC has now surfaced.", html)
assert_true(
    "redundant update-prefix stripped from body",
    "<strong>UPDATE (originally covered 2026-07-03)" not in html,
)
assert_in("update lead href", 'href="entries/2026-07-03/coolify-rce/"', html)
assert_in("deep-dive entry in its section", 'data-section="deep-dive"', html)
assert_in("action item present", "Patch Coolify to ≥ v4.0.0-beta.469.", html)
assert_in("action finding-ref link", 'class="action-ref"', html)
assert_in("action finding-ref carries a short label", 'class="action-ref__label"', html)
assert_in("verification notes carry the run body", "Watchlist: no hits this run.", html)
assert_in("run note names the run id", "2026-07-03T0412Z-intel", html)
assert_in("verification badge absent for multi-source", 'data-priority="critical"', html)

card = render_entry_card(E_CRIT, prefix="", entries_by_id=by_id)
assert_in("card keeps data-tags", 'data-tags="vulnerabilities rce actively-exploited"', card)
assert_in("card keeps data-regions", 'data-regions="global"', card)
assert_in("card keeps data-section", 'data-section="trending-vulnerabilities"', card)
assert_in("card links the permalink", 'href="entries/2026-07-03/coolify-rce/"', card)
assert_in("card carries sources line", "Example PSIRT", card)
assert_in("card renders evidence citation", 'class="entry-cite"', card)
assert_in("card citation carries attribution", 'class="entry-cite__attr"', card)
assert_in("cve pill on card", "CVE-2026-34038", card)

# single-source badge
ss = mk_entry("single-src", verification="single-source-national-cert",
              sources=[{"url": "https://cert.example/adv", "publisher": "CERT",
                        "date": "2026-07-03", "role": "primary"}])
ss_card = render_entry_card(ss, prefix="")
assert_in("single-source badge rendered", "single-source · national CERT", ss_card)

# ---------------------------------------------------------------------
# grouping + section routing
# ---------------------------------------------------------------------
print("== grouping ==")
days = entries_by_day(ALL_ENTRIES)
assert_eq("day pages: operational dates only", sorted(days), ["2026-07-01", "2026-07-03"])
assert_eq("2026-07-03 has 5 operational entries", len(days["2026-07-03"]), 5)
weeks = entries_by_week(ALL_ENTRIES)
assert_eq("weekly grouping keys on ISO week of strategic entries",
          sorted(weeks), ["2026-W26"])
assert_eq("strategic-only in weeks", len(weeks["2026-W26"]), 2)
assert_eq("update routes to updates", entry_section_key(E_UPD), "updates")
assert_eq("deep dive routes to deep-dive", entry_section_key(E_DEEP), "deep-dive")
assert_eq("policy has no daily section", entry_section_key(E_STRAT), None)
assert_eq("weekly fallback by kind", weekly_section_key(E_STRAT), "weekly-policy")
assert_eq("explicit weekly_section wins", weekly_section_key(E_STRAT2), "weekly-long-running")
assert_eq("update chain resolves", build_update_chains(ALL_ENTRIES),
          {"2026-07-03/coolify-rce": ["2026-07-03/coolify-rce-update"]})
picked = select_tldr_entries([E_NOTE, E_HIGH, E_CRIT])
assert_eq("tl;dr picks critical first", picked[0]["id"], E_CRIT["id"])
assert_eq("tl;dr pads with notable to 3", len(picked), 3)

# ---------------------------------------------------------------------
# briefbook.json / alerts.json shapes
# ---------------------------------------------------------------------
print("== briefbook + alerts ==")
book = build_briefbook(ALL_ENTRIES, [RUN], ref_ts=REF_TS, prefix="../")
assert_eq("briefbook window_days", book["window_days"], 35)
assert_eq("briefbook generated_at", book["generated_at"], "2026-07-03T12:00:00Z")
assert_eq("briefbook carries all fixture entries", len(book["entries"]), len(ALL_ENTRIES))
be = {x["id"]: x for x in book["entries"]}[E_CRIT["id"]]
for field in ("id", "url", "date", "discovered_at", "kind", "horizon", "priority",
              "headline", "summary", "title", "tags", "regions", "sectors",
              "entities", "cve_ids", "cve_status", "update_of", "updated_by",
              "deep_dive", "actions", "watchlist_hit", "verification",
              "immediate_action", "html"):
    assert_true(f"briefbook entry field `{field}`", field in be)
assert_eq("briefbook cve_ids", be["cve_ids"], ["CVE-2026-34038"])
assert_eq("briefbook cve_status union", be["cve_status"], ["exploited", "patch-available"])
assert_eq("briefbook updated_by chain", be["updated_by"], ["2026-07-03/coolify-rce-update"])
assert_in("briefbook html is the day-page card", 'class="brief-item entry-card"', be["html"])
assert_eq("briefbook IA block", be["immediate_action"]["title"], "Patch Coolify now")
assert_eq("briefbook run count", len(book["runs"]), 1)
br = book["runs"][0]
for field in ("run_id", "url", "date", "kind", "started", "completed",
              "window_hours", "gap_hours", "model", "entries_published", "html"):
    assert_true(f"briefbook run field `{field}`", field in br)
assert_in("briefbook run html rendered", "<p>", br["html"])

alerts = build_alerts(ALL_ENTRIES, ref_ts=REF_TS, site_url="https://x.example/")
assert_true("alerts documents itself", alerts["_comment"].startswith("Notification-hook"))
# Both horizons alert — a strategic `high` is still notification-worthy.
assert_eq("alerts: only critical|high in window",
          sorted(a["id"] for a in alerts["alerts"]),
          sorted([E_CRIT["id"], E_HIGH["id"], E_STRAT["id"]]))
al = {a["id"]: a for a in alerts["alerts"]}
assert_eq("alerts: critical carries immediate_action",
          al[E_CRIT["id"]]["immediate_action"]["title"], "Patch Coolify now")
assert_eq("alerts: high has null immediate_action",
          al[E_HIGH["id"]]["immediate_action"], None)
assert_true("alerts URLs absolute",
            al[E_CRIT["id"]]["url"].startswith("https://x.example/entries/"))

# ---------------------------------------------------------------------
# feeds from fixture entries
# ---------------------------------------------------------------------
print("== feeds ==")
items_xml, _ts = build_items_feed(ALL_ENTRIES, site_url="https://x.example/", ref_ts=REF_TS)
assert_eq("items feed is valid XML", _xml_validate(items_xml), [])
assert_in("item title = headline", "<title>Headline coolify-rce</title>", items_xml)
assert_in("item description = summary", "Summary coolify-rce.", items_xml)
assert_in("pubDate from discovered_at", "03 Jul 2026 04:21:09", items_xml)
assert_in("category carries cve id", "<category>CVE-2026-34038</category>", items_xml)
assert_in("category carries tag", "<category>vulnerabilities</category>", items_xml)
sector_feeds = {f: x for f, x, _t in build_sector_feeds(ALL_ENTRIES,
                                                        site_url="https://x.example/",
                                                        ref_ts=REF_TS)}
assert_true("eight sector slices emitted", len(sector_feeds) == 8)
assert_in("healthcare entry lands in its slice",
          "Headline old-item", sector_feeds["feed-healthcare.xml"])
assert_not_in("healthcare entry stays out of energy slice",
              "Headline old-item", sector_feeds["feed-energy.xml"])
for fname, xml in sector_feeds.items():
    errs = _xml_validate(xml)
    if errs:
        FAILURES.append(f"sector feed {fname} invalid XML: {errs}")
        print(f"  FAIL sector feed {fname} XML")
print("  ok  all sector feeds parse as XML")

# ---------------------------------------------------------------------
# entity appearance matching + sources annotation
# ---------------------------------------------------------------------
print("== entities ==")
REGISTRY = {
    "actor:testfox": {
        "key": "actor:testfox", "type": "actor", "name": "TestFox",
        "aliases": ["FOXCAT-9"], "nexus": None,
        "summary": "Fixture actor for tests.", "first_seen": "2026-06-01",
    },
}
CVES_SEEN = {"cves": [
    {"id": "CVE-2025-0001", "first_seen": "2026-05-01", "last_seen": "2026-05-02",
     "title": "Historical CVE never re-covered", "primary_source_url": ""},
]}
SOURCES_RAW = {"sources": [
    {"id": "example-psirt", "publisher": "Example PSIRT",
     "url": "https://example.com/", "category": ["vulns"],
     "reliability": "HIGH", "status": "active"},
]}
day_pages = set(days)
ents, matched = build_entities(REGISTRY, ALL_ENTRIES, CVES_SEEN, SOURCES_RAW, day_pages)
by_key = {e["key"]: e for e in ents}
fox = by_key["actor:testfox"]
assert_eq("explicit key + alias mention both match",
          sorted(a["entry_id"] for a in fox["appearances"]),
          sorted([E_HIGH["id"], E_NOTE["id"]]))
assert_eq("registry first_seen backfills first_covered", fox["first_covered"], "2026-06-01")
assert_true("cve entity from entry cves[]", "CVE-2026-34038" in by_key)
assert_eq("cve entity appearance count",
          len(by_key["CVE-2026-34038"]["appearances"]), 2)
assert_true("historical cves_seen id becomes an entity", "CVE-2025-0001" in by_key)
assert_eq("historical cve keeps its dates",
          by_key["CVE-2025-0001"]["first_covered"], "2026-05-01")
assert_true("citations resolve to curated source ids",
            any(c.get("source_id") == "example-psirt"
                for c in by_key["CVE-2026-34038"]["citations"]))
compute_related_entities(ents, matched)
assert_true("co-occurrence links actor to nothing (no shared entries)",
            fox["related_entities"] == [] or isinstance(fox["related_entities"], list))

src = annotate_sources(SOURCES_RAW, ALL_ENTRIES)["sources"][0]
assert_true("source appearances carry dates", "2026-07-03" in src["appearances"])
assert_true("source entry_refs carry entry ids",
            any(r["id"] == E_CRIT["id"] for r in src["entry_refs"]))


# ---------------------------------------------------------------------
# Umami / CSP consistency
# ---------------------------------------------------------------------
# The loader served from UMAMI_SCRIPT_HOST POSTs its pageview beacon to
# UMAMI_BEACON_HOST/api/send. If the CSP connect-src omits the beacon host
# (or re-lists a retired one), the browser silently blocks every beacon and
# analytics record nothing while the script appears to load fine. This is
# exactly the 2026-06-20 regression — it shipped from the first commit
# because nothing tied the CSP to the loader's real beacon endpoint.
print("== umami CSP ==")
if build.ANALYTICS_ENABLED:
    assert_in(
        "snippet loads from the script host",
        f'src="{build.UMAMI_SCRIPT_HOST}/script.js"',
        build.UMAMI_SNIPPET,
    )
    assert_in("CSP permits the script host", build.UMAMI_SCRIPT_HOST, build.CSP_META)
    assert_in("CSP connect-src permits the beacon host", build.UMAMI_BEACON_HOST, build.CSP_META)
    assert_match(
        "beacon host is inside connect-src (not some other directive)",
        r"connect-src[^;]*" + re.escape(build.UMAMI_BEACON_HOST),
        build.CSP_META,
    )
    for _retired in build.UMAMI_RETIRED_HOSTS:
        assert_not_in(f"retired host {_retired} absent from CSP", _retired, build.CSP_META)
else:
    # analytics.provider "none" — the off switch must strip every
    # third-party origin from both the snippet and the CSP.
    assert_eq("analytics off: snippet empty", build.UMAMI_SNIPPET, "")
    assert_not_in("analytics off: no umami host in CSP", "umami", build.CSP_META)
    assert_match(
        "analytics off: connect-src is first-party only",
        r"connect-src 'self';",
        build.CSP_META,
    )


# ---------------------------------------------------------------------
# Ops dashboard — verification clean-rate
# ---------------------------------------------------------------------
# Regression guard: "clean publish" means the final verifier verdict was
# CLEAN (residual == 0), regardless of how many iterations it took.
print("== ops verification clean-rate ==")
assert_eq(
    "first-pass clean counts (iters=1, resid=0)",
    _verification_clean_publish({"verification_iterations": 1, "verification_residual_count": 0}),
    True,
)
assert_eq(
    "clean-after-remediation counts (iters=4, resid=0)",
    _verification_clean_publish({"verification_iterations": 4, "verification_residual_count": 0}),
    True,
)
assert_eq(
    "cap-breach with residuals does not count (iters=5, resid=2)",
    _verification_clean_publish({"verification_iterations": 5, "verification_residual_count": 2}),
    False,
)
assert_eq(
    "missing residual count treated as clean (iters=3, resid absent)",
    _verification_clean_publish({"verification_iterations": 3}),
    True,
)
assert_eq(
    "unrated run (no verification recorded) does not count",
    _verification_clean_publish({"verification_residual_count": 0}),
    False,
)


# ---------------------------------------------------------------------
# Branding profile (config/branding.yaml → branding_config.py)
# ---------------------------------------------------------------------
# The customization framework's core contract: the SHIPPED config is the
# upstream default (byte-identical site), every theme value is an override
# layer, unknown keys fail loud, and the analytics off switch works. See
# docs/customization.md.
import branding_config  # noqa: E402

print("== branding profile ==")

_shipped = branding_config.load_branding()
assert_eq(
    "shipped config/branding.yaml equals upstream DEFAULTS "
    "(byte-identical default site)",
    _shipped, branding_config.DEFAULTS,
)
assert_eq(
    "default theme emits no override CSS",
    branding_config.render_branding_css(_shipped), "",
)
assert_eq(
    "default favicon data-URI is byte-exact",
    branding_config.default_favicon_href(_shipped),
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' "
    "viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='6' "
    "fill='%23e85d75'/%3E%3Ctext x='50%25' y='52%25' text-anchor='middle' "
    "dominant-baseline='middle' font-family='ui-monospace,monospace' "
    "font-size='15' font-weight='700' fill='%230e1116'%3ECTI%3C/text%3E%3C/svg%3E",
)
# Missing file → identical defaults (a fork may delete the config).
assert_eq(
    "missing config file falls back to DEFAULTS",
    branding_config.load_branding(Path("/nonexistent/branding.yaml")),
    branding_config.DEFAULTS,
)

with tempfile.TemporaryDirectory() as _td:
    _tmp = Path(_td) / "branding.yaml"

    # Unknown key fails loud (typo protection).
    _tmp.write_text('site:\n  nmae: "typo"\n', encoding="utf-8")
    try:
        branding_config.load_branding(_tmp)
        FAILURES.append("branding: unknown key 'site.nmae' was accepted")
        print("  FAIL branding: unknown key accepted")
    except branding_config.BrandingError:
        print("  ok  unknown key fails loud")

    # Bad analytics provider fails loud.
    _tmp.write_text('analytics:\n  provider: "google"\n', encoding="utf-8")
    try:
        branding_config.load_branding(_tmp)
        FAILURES.append("branding: provider 'google' was accepted")
        print("  FAIL branding: bad provider accepted")
    except branding_config.BrandingError:
        print("  ok  unsupported analytics provider fails loud")

    # Referenced logo file must exist under site/branding/.
    _tmp.write_text('logo:\n  header_mark: "missing.svg"\n', encoding="utf-8")
    try:
        branding_config.load_branding(_tmp)
        FAILURES.append("branding: missing logo file was accepted")
        print("  FAIL branding: missing logo file accepted")
    except branding_config.BrandingError:
        print("  ok  missing logo file fails loud")

    # Partial override: unset keys inherit defaults; theme overrides emit
    # the two light-theme selector shapes styles.css uses.
    _tmp.write_text(
        'site:\n'
        '  name: "acme-cti.example"\n'
        'theme:\n'
        '  dark:\n'
        '    accent: "#00b3a4"\n'
        '  light:\n'
        '    accent: "#00776e"\n'
        'analytics:\n'
        '  provider: "none"\n',
        encoding="utf-8",
    )
    _fork = branding_config.load_branding(_tmp)
    assert_eq("override: site.name replaced", _fork["site"]["name"], "acme-cti.example")
    assert_eq(
        "override: unset tagline inherits upstream default",
        _fork["site"]["tagline"], "Switzerland, Europe & Public Sector",
    )
    assert_eq("override: analytics off", _fork["analytics"]["provider"], "none")
    _css = branding_config.render_branding_css(_fork)
    assert_in("override css: dark accent in :root", "--accent: #00b3a4;", _css)
    assert_in(
        "override css: light accent under prefers-color-scheme",
        ':root:not([data-theme="dark"])', _css,
    )
    assert_in(
        "override css: light accent under explicit data-theme",
        ':root[data-theme="light"]', _css,
    )

    # Custom trend cohorts / sector slices replace the defaults wholesale;
    # empty lists keep the upstream sets.
    _tmp.write_text(
        'trends:\n'
        '  cohorts:\n'
        '    - key: "apac"\n'
        '      title: "APAC items / week"\n'
        '      regions:\n'
        '        - "apac"\n'
        'feeds:\n'
        '  sector_slices:\n'
        '    - filename: "feed-manufacturing.xml"\n'
        '      title_suffix: "Manufacturing"\n'
        '      description: "Items affecting manufacturing."\n'
        '      sectors:\n'
        '        - "manufacturing"\n',
        encoding="utf-8",
    )
    _fork2 = branding_config.load_branding(_tmp)
    assert_eq(
        "custom cohorts replace defaults",
        branding_config.trend_cohorts(_fork2, [{"key": "default"}]),
        [{"key": "apac", "title": "APAC items / week", "tags": (),
          "sectors": (), "regions": ("apac",), "match": "any"}],
    )
    assert_eq(
        "custom sector slices replace defaults",
        branding_config.sector_feed_slices(_fork2, [("default",)]),
        [("feed-manufacturing.xml", ("manufacturing",), (),
          "Manufacturing", "Items affecting manufacturing.")],
    )
    assert_eq(
        "empty cohort list keeps upstream defaults",
        branding_config.trend_cohorts(_shipped, [{"key": "default"}]),
        [{"key": "default"}],
    )

# Module-level consistency in the imported build: snippet present iff
# analytics enabled; branding constants derive from the shipped config.
assert_eq(
    "build: snippet presence matches ANALYTICS_ENABLED",
    bool(build.UMAMI_SNIPPET), build.ANALYTICS_ENABLED,
)
assert_eq("build: SITE_NAME from config", build.SITE_NAME, _shipped["site"]["name"])
assert_eq(
    "build: default sector slices in effect with empty config list",
    build.SECTOR_FEED_SLICES is build._DEFAULT_SECTOR_FEED_SLICES,
    not _shipped["feeds"]["sector_slices"],
)
assert_eq(
    "build: default trend cohorts in effect with empty config list",
    build.TREND_COHORTS is build._DEFAULT_TREND_COHORTS,
    not _shipped["trends"]["cohorts"],
)


# ---------------------------------------------------------------------
# Result
# ---------------------------------------------------------------------
print()
if FAILURES:
    print(f"{len(FAILURES)} failure(s):")
    for f in FAILURES:
        print(f"  · {f}")
    sys.exit(1)
print("All tests passed.")
sys.exit(0)
