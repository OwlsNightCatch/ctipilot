#!/bin/sh
# usage: quotecheck <file> <quote>
f="$1"; shift
if grep -Fq "$*" "$f"; then echo "PASS  $f :: $*"; else echo "FAIL  $f :: $*"; fi
