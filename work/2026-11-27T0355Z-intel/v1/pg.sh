#!/bin/bash
# usage: pg.sh <substring of url>
grep -F "$1" urllist.txt | head -1 | cut -f1
