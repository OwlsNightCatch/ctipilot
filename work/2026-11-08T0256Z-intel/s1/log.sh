#!/bin/bash
# usage: log.sh progress <source-id> <attempted|failed> <items>
# usage: log.sh live <url> <status>
W=/home/user/ctipilot/work/2026-11-08T0256Z-intel
if [ "$1" = progress ]; then
  printf '%s %s %s %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$2" "$3" "$4" >> $W/S1.progress
else
  printf '%s\t%s\t%s\n' "$2" "$3" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> $W/url-liveness.tsv
fi
