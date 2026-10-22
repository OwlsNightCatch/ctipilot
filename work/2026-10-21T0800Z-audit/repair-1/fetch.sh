#!/bin/bash
# usage: fetch.sh name url  -> src/name.md (extract)
R=/home/user/ctipilot/work/2026-10-21T0800Z-audit/repair-1
cd /home/user/ctipilot
out="$R/src/$1.md"
python3 tools/fetch_source.py extract "$2" > "$out" 2> "$R/src/$1.err"
echo "$1: rc=$? bytes=$(wc -c < "$out") lines=$(wc -l < "$out")"
