#!/bin/bash
# usage: fx.sh <slug> <mode> <url>   mode: extract|url|pdf|jina
cd /home/user/ctipilot
slug=$1; mode=$2; url=$3
out=work/2026-10-21T1148Z-audit/truth-1/bodies/$slug.txt
tmp=$(mktemp)
timeout 120 python3 tools/fetch_source.py $mode "$url" > $tmp 2>$tmp.err
rc=$?
n=$(wc -c < $tmp)
{ echo "$url"; cat $tmp; } > $out
printf '%s\t%s\t%s\n' "$url" "$mode rc=$rc bytes=$n" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> work/2026-10-21T1148Z-audit/url-liveness.tsv
echo "$slug $mode rc=$rc bytes=$n $(head -c 200 $tmp.err | tr '\n' ' ')"
rm -f $tmp $tmp.err
