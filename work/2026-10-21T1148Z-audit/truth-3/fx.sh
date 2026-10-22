#!/bin/bash
# usage: fx.sh <slug> <url> [mode]   mode: extract (default) | url | pdf | jina
cd /home/user/ctipilot || exit 1
slug="$1"; url="$2"; mode="${3:-extract}"
out="work/2026-10-21T1148Z-audit/truth-3/bodies/${slug}.txt"
tmp=$(mktemp)
python3 tools/fetch_source.py "$mode" "$url" > "$tmp" 2> "$tmp.err"
rc=$?
sz=$(wc -c < "$tmp")
ts=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
if [ $rc -eq 0 ] && [ "$sz" -gt 200 ] && ! head -c 400 "$tmp" | grep -qiE "Title: (Page not found|Error 404)|Target URL returned error 404|Not Found"; then
  { echo "$url"; cat "$tmp"; } > "$out"
  printf '%s\t%s\t%s\n' "$url" "ok-$mode-$sz" "$ts" >> work/2026-10-21T1148Z-audit/url-liveness.tsv
  echo "OK $slug $mode bytes=$sz -> $out"
else
  printf '%s\t%s\t%s\n' "$url" "fail-$mode-rc$rc-$sz" "$ts" >> work/2026-10-21T1148Z-audit/url-liveness.tsv
  echo "FAIL $slug $mode rc=$rc bytes=$sz"; head -c 400 "$tmp.err"; head -c 300 "$tmp"
fi
rm -f "$tmp" "$tmp.err"
