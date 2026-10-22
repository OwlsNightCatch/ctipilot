#!/bin/bash
# usage: fx.sh <name> <extract|url|pdf> <URL>
cd /home/user/ctipilot
name="$1"; mode="$2"; u="$3"
out=work/2026-10-21T1149Z-audit/truth-T1/$name.txt
python3 tools/fetch_source.py "$mode" "$u" > "$out" 2> "$out.err"
rc=$?
sz=$(wc -c < "$out")
echo "rc=$rc bytes=$sz $name"
if [ $rc -eq 0 ] && [ "$sz" -gt 200 ]; then
  printf '%s\t%s\t%s\n' "$u" "200" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> work/2026-10-21T1149Z-audit/url-liveness.tsv
else
  head -c 300 "$out.err"
fi
