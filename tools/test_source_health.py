#!/usr/bin/env python3
"""Stdlib-only offline self-test for the `source_health.py` walled check.

    python3 tools/test_source_health.py

Makes no network calls: `_content_fetch` is stubbed, so the cases run in a
fresh routine container with no egress budget.

Why this exists: v4.18 gives a `fetch_method: webfetch` record the verdict
`webfetch-only` (handled, action `none`) when the container is walled out of
its host, because the agent-side `WebFetch` tool reads it from outside. The
2026-09-30 audit's verifier showed that the first version counted every shell
marker as a wall, so a 404 or a parked domain on a webfetch record was also
called handled and its `needs-demote` was silenced. These cases pin the split:
a challenge page or a refused transport is a wall, a dead page is not. The
same wall test decides when a documented unreachable `blocked` host
(ssd-disclosure) is a handled coverage gap rather than a recipe to demote.
"""

from __future__ import annotations

import importlib.util
import os
import sys
from datetime import datetime, timezone

_HERE = os.path.dirname(os.path.abspath(__file__))


def _load_module():
    """Import source_health.py by path, it is a script, not a package."""
    path = os.path.join(_HERE, "source_health.py")
    spec = importlib.util.spec_from_file_location("source_health_under_test", path)
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


sh = _load_module()
_NOW = datetime(2026, 9, 30, 12, 0, tzinfo=timezone.utc)
_RECORD = {"id": "example", "fetch_method": "webfetch", "url": "https://example.org/news/"}


def _assess(body: str) -> dict:
    """Run the content check on a stubbed read of `body`."""
    real = sh._content_fetch
    sh._content_fetch = lambda s, timeout: ("extract+direct", body, body, [])
    try:
        return sh._content_assess(dict(_RECORD), timeout=1.0, now=_NOW)
    finally:
        sh._content_fetch = real


def test_marker_sets_are_disjoint_and_complete():
    assert not set(sh._CHALLENGE_MARKERS) & set(sh._DEAD_MARKERS)
    assert set(sh._SHELL_MARKERS) == set(sh._CHALLENGE_MARKERS) | set(sh._DEAD_MARKERS)


def test_blocked_transport_is_walled():
    for cls in ("ua-blocked", "bridge-blocked", "reader-quota"):
        assert sh._walled(cls, []), cls


def test_reachable_without_markers_is_not_walled():
    assert not sh._walled("ok", [])
    assert not sh._walled("ok", None)


def test_challenge_page_is_walled():
    c = _assess("<html><title>Just a moment...</title>Checking your browser before accessing</html>")
    assert c["content_verdict"] == "shell", c
    assert sh._walled("ok", c["content_shell_markers"]), c["content_shell_markers"]


def test_dead_page_is_not_walled():
    c = _assess("<html><h1>404 Not Found</h1>The requested URL was not found.</html>")
    assert c["content_verdict"] == "shell", c
    assert c["content_shell_markers"] == ["404 not found"], c["content_shell_markers"]
    assert not sh._walled("ok", c["content_shell_markers"])


def test_parked_domain_is_not_walled():
    c = _assess("<html>This domain is for sale. Buy this domain today.</html>")
    assert c["content_verdict"] == "shell", c
    assert not sh._walled("ok", c["content_shell_markers"]), c["content_shell_markers"]


def test_documented_blocked_host_wall_is_handled():
    assert "ssd-disclosure" in sh.TRANSPORT_BLOCKED_UNREACHABLE
    c = _assess("<html><title>Robot Challenge Screen</title>sgcaptcha</html>")
    assert c["content_verdict"] == "shell", c
    assert sh._blocked_handled("blocked", "ssd-disclosure", c["content_verdict"], 202,
                               c["content_shell_markers"])
    # With an empty reader pool the direct transports return nothing at all
    # (SiteGround answers HTTP 202 with no readable body): still the known wall.
    assert sh._blocked_handled("blocked", "ssd-disclosure", "unreadable", 202, [])


def test_blocked_handling_needs_listing_and_a_wall():
    assert not sh._blocked_handled("blocked", "not-listed", "shell", 202, ["captcha"])
    assert not sh._blocked_handled("jina", "ssd-disclosure", "shell", 202, ["captcha"])
    assert not sh._blocked_handled("blocked", "ssd-disclosure", "relevant", 200, [])
    assert not sh._blocked_handled("blocked", "ssd-disclosure", "unreadable", 404, [])
    c = _assess("<html><h1>404 Not Found</h1></html>")
    assert not sh._blocked_handled("blocked", "ssd-disclosure", c["content_verdict"], 200,
                                   c["content_shell_markers"])


def test_blocked_record_is_probed_without_the_reader():
    calls = []
    real = sh._run_fetch
    sh._run_fetch = lambda argv, timeout: (calls.append(argv), "")[1]
    try:
        transport, text, _, _ = sh._content_fetch(
            {"id": "ssd-disclosure", "fetch_method": "blocked",
             "url": "https://ssd-disclosure.com/advisories/"}, timeout=1.0)
    finally:
        sh._run_fetch = real
    assert transport == "direct" and not text.strip(), (transport, text)
    assert calls == [["url", "https://ssd-disclosure.com/advisories/", "--direct"]], calls


def main() -> int:
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failed = 0
    for t in tests:
        try:
            t()
        except AssertionError as e:
            failed += 1
            print(f"FAIL {t.__name__}: {e}")
        except Exception as e:  # noqa: BLE001, a crash is a failure too
            failed += 1
            print(f"ERROR {t.__name__}: {type(e).__name__}: {e}")
        else:
            print(f"ok   {t.__name__}")
    print(f"\n{len(tests) - failed}/{len(tests)} passed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
