#!/bin/bash
# usage: fx.sh <slug> <url-or-arg> [mode words, default extract] [label-url for first line]
cd /home/user/ctipilot || exit 1
slug="$1"; u="$2"; mode="${3:-extract}"; label="${4:-$2}"
out="work/2026-10-21T1148Z-audit/truth-4/bodies/${slug}.txt"
tmp="work/2026-10-21T1148Z-audit/truth-4/bodies/.${slug}.tmp"
python3 tools/fetch_source.py $mode "$u" > "$tmp" 2>&1
rc=$?
{ printf '%s\n' "$label"; cat "$tmp"; } > "$out"
: > "$tmp"
printf '%s\t%s\t%s\n' "$label" "$mode-rc$rc" "$(date -u +%FT%TZ)" >> work/2026-10-21T1148Z-audit/url-liveness.tsv
echo "$slug rc=$rc bytes=$(wc -c < "$out")"
head -c 300 "$out" | tr '\n' ' ' ; echo
