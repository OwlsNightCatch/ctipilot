#!/bin/bash
# usage: fx.sh <slug> <mode:extract|url|pdf|jina> <URL>
cd /home/user/ctipilot
slug="$1"; mode="$2"; url="$3"
out=work/2026-10-21T1148Z-audit/truth-2/bodies/$slug.txt
tmp=$(mktemp)
python3 tools/fetch_source.py $mode "$url" > "$tmp" 2> "$tmp.err"
rc=$?
sz=$(wc -c < "$tmp")
{ echo "$url"; cat "$tmp"; } > "$out"
printf '%s\t%s\t%s\n' "$url" "rc=$rc;bytes=$sz;mode=$mode" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> work/2026-10-21T1148Z-audit/url-liveness.tsv
echo "rc=$rc bytes=$sz -> $out"; head -c 300 "$tmp.err"
rm -f "$tmp" "$tmp.err"
