# WebFetch transcripts (summariser output, kept for audit; not raw bodies)

WebFetch returns a summary, so quotes taken from it are NOT grep-verifiable against a raw body. Every claim in deepread.yaml that rests only on these notes is tagged `body_file: webfetch-notes.md` and `grep_verified: false`.

## drupal.org/sa-core-2026-019 (WebFetch, 2026-11-26 about 04:38Z)
Confirmed the feed reading: Highly critical 21 of 25; affected "<10.6.23 || >= 11.0.0 <11.3.23 || >=11.4.0 <11.4.14"; CVE-2026-136716; "The page has no separate 'Update' section."; fixed 11.4.14, 11.3.23, 10.6.23; Run update.php; securing installer strongly recommended; Steward covers 019 and 017. Date 2026-November-25.

## drupal.org/sa-core-2026-017 (WebFetch)
Confirmed the feed reading: Highly critical 20 of 25 AC:Complex/A:None/CI:All/II:All/E:Exploit/TD:Uncommon; "Update: the Security Team has received a report this was exploited on live sites as early as 2026-11-19 19:00 UTC."; fixed 11.4.13, 11.3.22, 10.6.22; "Discovered by Anthropic's OSS Scanner, as vulnerability ANT-2026-GMRPK0BU."; If you cannot upgrade immediately: follow the instructions for securing the Drupal installer.

## drupal.org/project/drupal/releases/11.4.14 (WebFetch)
- Release date 25 November 2026, security release of the Drupal 11 series, fixes SA-CORE-2026-019.
- 11.4.x security coverage through April 2027 (summariser statement).
- "This release fixes an issue with the theme registry that was introduced in 11.4.13" (errors such as "Theme hook field not found" in some contributed and custom code, Search API named).
- "Symfony has issued a security update today that is not included in this release" ; "It is recommended that you update Symfony along with this release." ; Twig bumped to 3.31.1.
- The page does not mention install.php, update hooks, .htaccess or settings.php.

## cisa.gov alert 2026-11-24 "CISA Adds Three Known Exploited Vulnerabilities to Catalog" (WebFetch)
Lists CVE-2026-131914 (Idunno AntiCsrf), CVE-2026-132165 (Drupal Core Remote Code Execution Vulnerability), CVE-2026-132224 (Optimizely Web Experimentation). No threat actor named; page carries no due date; cites BOD 26-04.
