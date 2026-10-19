# Systemic notes (working file)

1. CNA scores nulled by the 2026-09-30 banned-citation repair (commit 3797866): 9 values on 7 entries
   - 2026-07-29/cve-2026-63077-teamcity (9.8), 2026-09-04/chrome-v8 CVE-2026-85046 (8.8), 2026-09-12/jfrog (8.1, 7.5),
     2026-09-19/unbound CVE-2026-82717 (8.4 CVSS4.0), 2026-09-21/nighteagle CVE-2020-0688 (8.8),
     2026-09-23/virtualizor (9.8/9.3, 8.1/9.2, 7.5/8.7)
   - Root cause: PD-2 bans citing the CVE record, and the repair read "fact only on a banned page" as "fact unsupported";
     but cves[].cvss carries no inline citation and PD-2 explicitly allows reading the CVE record to verify a score.
   - Fix: restore via correction records; clarify the rule in cti-run.md Phase 2 item 4 (versioned edit).
2. Main-analysis growth past the 550-word limit through update records' supersession rewrites (12 of 54 new window
   entries now over; e.g. Zammad 526 -> 1048, Danfoss 550 -> 926). The length WARN covers new entries only.
3. 10-01 fire missing (gap 48 h on a daily schedule); 10-02 fire self-healed (window 50 h). Availability signal only.
4. Session safety check refused one truth pass's Bash writes mid-pass (T6a, entries 6-9 transcribed by main agent).
5. Calibration alarm: window high share 15/54 = 28 % (> ~25 %). Draft re-grade against the high bar:
   - fails: 2026-10-16/drupal-sa-core-2026-014 (unexploited, no public exploit, unauthenticated path only via contrib modules = non-default config) -> notable
   - borderline: 2026-10-13/cve-2026-97229-gitlab (unexploited, PoC needs push access to a public project), 2026-10-13/danfoss (retail refrigeration; constituency exposure thin, NCSC.ch rating gives home-region nexus)
   - the rest hold (exploited/KEV with constituency-run products, or actor/supply-chain with Swiss/public-sector nexus)
6. citation-cve page check reports 'does not mention' on an image-only PDF (ANSSI CERTFR-2026-CTI-006) — should be unverifiable, not a mismatch.
7. quote-literal false positives: reader/extract renders links as '[text(opens in a new window)](url)', escapes underscores ('ping\_'), and Mastodon text lives only in og:description — the check should normalise these (D2 lead-only results).
   Root causes in tools/check_run.py _page_skeletons: (a) extract-mode (markdown) text goes through the HTML tag stripper, which deletes literal angle-bracket text such as "<FIRST 4 digits of UUID>" (Kimsuky); (b) accessibility labels "(opens in a new window)" inside link text (OpenAI); (c) Mastodon post text exists only in og:description/description meta tags, which tag stripping discards (CERT-Bund).
