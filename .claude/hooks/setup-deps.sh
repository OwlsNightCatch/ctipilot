#!/usr/bin/env bash
# .claude/hooks/setup-deps.sh — SessionStart hook
#
# Ensure python dependencies the fetch bridge relies on are present in this
# container. Routine fires run in a fresh, ephemeral container cloned from
# main, so anything pip-installed is gone by the next fire — this hook
# reinstalls it idempotently at session start.
#
# Currently: trafilatura (https://github.com/adbar/trafilatura) — the
# standard capture/extraction layer for `tools/fetch_source.py extract`
# (operator directive 2026-08-24: capture websites with trafilatura, keep
# the metered jina reader strictly last-resort, avoid WebFetch summaries).
#
# Best-effort: failures are logged to stderr but never block the session —
# fetch_source.py degrades gracefully when the module is absent.

set -u

if python3 -c "import trafilatura" 2>/dev/null; then
    exit 0
fi

echo "[setup-deps] installing trafilatura (first run in this container)…" >&2
pip install --quiet --timeout 120 --retries 3 trafilatura >&2 || {
    echo "[setup-deps] trafilatura install failed — fetch_source.py falls back to direct/jina" >&2
    exit 0
}
echo "[setup-deps] trafilatura $(python3 -c 'import trafilatura;print(trafilatura.__version__)') ready" >&2
