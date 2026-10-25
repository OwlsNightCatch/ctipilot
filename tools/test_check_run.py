#!/usr/bin/env python3
"""Stdlib-only offline self-test for the page checks of `tools/check_run.py`.

    python3 tools/test_check_run.py

`quote-literal` and `citation-cve` compare an entry's quotes and CVE ids with
the cited page as `_page_text` normalises it. Each case below is a false
positive an audit hit on a real page; the cases make no network call (the
`citation-cve` case stubs the bridge subprocess and the cache directory).
The `entry-shape` case stubs the committed copy of an entry this fire updated.
"""
from __future__ import annotations

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _load():
    spec = importlib.util.spec_from_file_location("check_run_under_test", _HERE / "check_run.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cr = _load()
sk = cr._quote_skeleton


def test_extract_keeps_literal_angle_brackets():
    # 2026-10-18 audit: an AhnLab quote with "<FIRST 4 digits of UUID>" failed
    # because trafilatura's markdown went through the HTML tag stripper.
    md = "The mutex is named Global\\<FIRST 4 digits of UUID> and created at start."
    assert sk("named Global\\<FIRST 4 digits of UUID> and") in sk(cr._page_text(md, "extract"))


def test_html_still_strips_tags_and_keeps_description_meta():
    page = ('<html><head><meta property="og:description" content="Patch CVE-2026-1234 now &amp; '
            'restart."></head><body><p>Shell <b>only</b></p></body></html>')
    text = cr._page_text(page, "html")
    assert "<b>" not in text and "Shell only" in text
    assert "Patch CVE-2026-1234 now & restart." in text


def test_opens_in_new_window_label_removed():
    page = "<p>A malicious <a href='x'>Artifactory(opens in a new window)</a> plugin was found.</p>"
    assert sk("Artifactory plugin was found") in sk(cr._page_text(page, "html"))
    md = "the [Artifactory (opens in a new tab)](https://example.org) plugin was found"
    assert sk("the Artifactory plugin was found") in sk(cr._page_text(md, "extract"))


def test_cache_header_is_not_page_text():
    raw = "<!-- https://example.org/advisories/CVE-2026-55555 -->\nAn advisory with no id in it."
    for mode in ("extract", "html"):
        assert "cve202655555" not in sk(cr._page_text(raw, mode)), mode


def test_pdf_without_text_is_unreadable():
    image_only = {"content_streams": 0, "chars": 0, "text": "",
                  "notes": "decode: none; no text objects found — this is very likely a scanned "
                           "or image-only PDF"}
    stray = {"content_streams": 2, "chars": 7, "text": "x 1 ? z",
             "notes": "decode: simple; suspiciously little text for a document with text objects"}
    good = {"content_streams": 5, "chars": 900, "text": "CVE-2026-4242 is exploited " * 30,
            "notes": "decode: simple"}
    assert cr._page_text(json.dumps(image_only), "pdf") is None
    assert cr._page_text("<!-- https://e.org/r.pdf -->\n" + json.dumps(stray), "pdf") is None
    assert "cve20264242" in sk(cr._page_text(json.dumps(good), "pdf"))
    assert "plain text" in cr._page_text("plain text of an older cache", "pdf")


def test_bot_challenge_page_is_unreadable():
    # drupal.org answers the container with this wall: its CSS and script text
    # clear the size floor, and both transports return the raw HTML.
    wall = ("<!doctype html>\n<html lang=\"en\"><head>\n<title>Client Challenge</title>\n"
            "<style>#loading-error { font-size: 16px; display: none; }</style></head><body>"
            "<noscript>JavaScript is disabled in your browser.</noscript>"
            "<script>function loadScript(src) { return new Promise(() => {}); }</script>"
            + "<div>A required part of this site couldn't load.</div>" * 20 + "</body></html>")
    for mode in ("html", "extract"):
        assert cr._page_text("<!-- https://www.drupal.org/sa-core-2026-014 -->\n" + wall, mode) is None, mode
    anubis = "<html><head><title>Making sure you&#39;re not a bot!</title></head><body>x</body></html>"
    assert cr._page_text(anubis, "html") is None
    article = "<html><head><title>Drupal core - Critical - SA-CORE-2026-014</title></head><body>" \
              "<p>Field UI allows remote code execution.</p></body></html>"
    assert "fielduiallowsremotecodeexecution" in sk(cr._page_text(article, "html"))


def test_citation_cve_counts_image_only_pdf_as_unreadable():
    tmp = Path(tempfile.mkdtemp(prefix="check-run-test-"))
    saved = (cr.WORK_DIR, subprocess.run, cr.warn, cr.ok)
    warns, oks = [], []
    # Image bytes decoded as text (ANSSI's report before the 10-18 reader fix)
    # clear the size floor, so only the reader's own verdict can mark them.
    junk = "JFIF Exif MM 0 ICC_PROFILE lcms mntrRGB XYZ acsp " * 40
    image_only = json.dumps({"content_streams": 0, "chars": len(junk), "text": junk,
                             "notes": "no text objects found"})

    class Done:
        returncode, stdout, stderr = 0, image_only, ""

    try:
        cr.WORK_DIR = tmp
        cr.subprocess.run = lambda *a, **k: Done()
        cr.warn = lambda label, detail="": warns.append((label, detail))
        cr.ok = lambda label, detail="": oks.append((label, detail))
        entry = {"id": "2026-10-01/example", "updates": [],
                 "body": "ANSSI ties the campaign to CVE-2026-77777 "
                         "([ANSSI, 2026-09-30](https://cert.ssi.gouv.fr/uploads/report.pdf))."}
        cr.check_citation_cves([entry], "2026-10-21T0000Z-audit", skip=False)
        assert not [w for w in warns if w[0] == "citation-cve"], warns
        assert any("not machine-checkable" in d for lbl, d in oks if lbl == "citation-cve"), oks
    finally:
        cr.WORK_DIR, cr.subprocess.run, cr.warn, cr.ok = saved
        shutil.rmtree(tmp, ignore_errors=True)


def test_entry_shape_flags_growth_of_an_updated_entry():
    saved = (cr._committed_entry, cr.warn, cr.ok, cr.fail)
    warns = []
    run = "2026-10-25T1308Z-audit"
    long_main = " ".join(["word"] * 600)
    try:
        cr._committed_entry = lambda eid: ({"headline": "Short"}, " ".join(["word"] * 500))
        cr.warn = lambda label, detail="": warns.append((label, detail))
        cr.ok = cr.fail = lambda label, detail="": None
        grown = {"id": "2026-10-01/grown", "run_id": "2026-10-01T0256Z-intel", "headline": "Short",
                 "body": long_main, "updates": [{"run_id": run, "fields": ["body"]}]}
        cr.check_entry_shape_v417([], [grown], run, enforce=True)
        assert any("grew the main analysis from 500 to 600" in d for _, d in warns), warns
        warns.clear()
        # Shrinking a long entry, or an internal metadata record, never warns.
        cr._committed_entry = lambda eid: ({"headline": "Short"}, " ".join(["word"] * 700))
        cr.check_entry_shape_v417([], [grown], run, enforce=True)
        meta = dict(grown, updates=[{"run_id": run, "fields": ["cves"]}])
        cr.check_entry_shape_v417([], [meta], run, enforce=True)
        assert not [d for _, d in warns if "grew" in d], warns
    finally:
        cr._committed_entry, cr.warn, cr.ok, cr.fail = saved


def main() -> int:
    tests =[v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"  ok   {t.__name__}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"  FAIL {t.__name__}: {exc!r}")
    print(f"{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
