#!/bin/bash
name=$1; url=$2
out=/home/user/ctipilot/work/2026-10-11T0256Z-intel/bodies/$name.txt
python3 /home/user/ctipilot/tools/fetch_source.py extract "$url" > "$out" 2>"$out.err"
if [ $(wc -c < "$out") -lt 1500 ]; then sleep 3; python3 /home/user/ctipilot/tools/fetch_source.py extract "$url" > "$out" 2>"$out.err"; fi
echo "$name $(wc -c < $out)"
