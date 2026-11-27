#!/bin/bash
h=$1; u=$2
if [[ "$u" == *"api.github.com"* || "$u" == *"euvdservices"* || "$u" == *".json"* || "$u" == *".sh" ]]; then
  python3 /home/user/ctipilot/tools/fetch_source.py url "$u" > pages/$h.txt 2>pages/$h.err
else
  python3 /home/user/ctipilot/tools/fetch_source.py extract "$u" > pages/$h.txt 2>pages/$h.err
fi
echo "$h $u $(wc -c < pages/$h.txt)" >> pages/_done.log
