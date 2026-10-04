#!/bin/bash
u="$1"
h=$(echo -n "$u" | md5sum | cut -c1-10)
cd /home/user/ctipilot
python3 tools/fetch_source.py extract "$u" > work/2026-10-04T0405Z-intel/v4/$h.txt 2> work/2026-10-04T0405Z-intel/v4/$h.err
echo "$h $u $(wc -c < work/2026-10-04T0405Z-intel/v4/$h.txt)" >> work/2026-10-04T0405Z-intel/v4/index.txt
