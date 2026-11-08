#!/bin/bash
cd /home/user/ctipilot
W=work/2026-11-08T1309Z-audit/deep
while IFS=$'\t' read -r name mode url; do
  ( timeout 180 python3 tools/fetch_source.py $mode "$url" > "$W/$name.txt" 2> "$W/$name.err"; echo "$name $? $(wc -c < $W/$name.txt)" >> $W/fetch.status ) &
  while [ $(jobs -r | wc -l) -ge 8 ]; do sleep 1; done
done < $W/urls.tsv
wait
