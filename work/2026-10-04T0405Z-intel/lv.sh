#!/bin/bash
# usage: lv.sh URL [status]
printf '%s\t%s\t%s\n' "$1" "${2:-200}" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" >> /home/user/ctipilot/work/2026-10-04T0405Z-intel/url-liveness.tsv
