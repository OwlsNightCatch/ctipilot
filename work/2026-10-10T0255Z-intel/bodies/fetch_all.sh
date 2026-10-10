#!/bin/bash
# Deep-read capture: fetch each will-publish primary to work/<run>/bodies/<name>.txt
# usage: fetch_all.sh [urls.tsv]   (tab-separated: name, method, url)
cd /home/user/ctipilot || exit 1
R=work/2026-10-10T0255Z-intel/bodies
LIST="${1:-$R/urls.tsv}"

fetch_one() {
  local n="$1" m="$2" u="$3"
  if [ "$m" = pdf ]; then
    timeout 150 python3 tools/fetch_source.py pdf "$u" > "$R/$n.txt" 2> "$R/$n.err"
  else
    timeout 150 python3 tools/fetch_source.py extract "$u" > "$R/$n.txt" 2> "$R/$n.err"
  fi
  echo "$n rc=$? bytes=$(wc -c < "$R/$n.txt")"
}

i=0
while IFS=$'\t' read -r n m u; do
  [ -z "$n" ] && continue
  fetch_one "$n" "$m" "$u" &
  i=$((i+1))
  if [ $((i % 6)) -eq 0 ]; then wait; fi
done < "$LIST"
wait
