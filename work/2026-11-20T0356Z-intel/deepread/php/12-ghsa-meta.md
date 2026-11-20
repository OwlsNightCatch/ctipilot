## GHSA-qc49-hpvq-g2w6
CVE: CVE-2026-129289 | Severity: Critical | CVSS4: CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | CVSS3: None | CWE: CWE-444, CWE-670 | AI-assisted-report: True
Affected/patched: Affected versions < 8.2.36 >= 8.3.0, < 8.3.37 >= 8.4.0, < 8.4.28 >= 8.5.0, < 8.5.13 Patched versions 8.2.36 8.3.37 8.4.28 8.5.13 Description Summary PHP can fail to discard unread bytes from an HTTP request body before reusing a persistent PHP-FPM or LSAPI con

## GHSA-658j-r8rw-q6mx
CVE: CVE-2026-115560 | Severity: Critical | CVSS4: CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | CVSS3: None | CWE: CWE-20, CWE-502 | AI-assisted-report: False
Affected/patched: Affected versions < 8.2.36 >= 8.3.0, < 8.3.37 >= 8.4.0, < 8.4.28 >= 8.5.0, < 8.5.13 Patched versions 8.2.36 8.3.37 8.4.28 8.5.13 Description Summary PHP's session upload progress feature can write attacker-controlled data using one session serialization format

## GHSA-fm2m-fjf5-v3cp
CVE: CVE-2026-126714 | Severity: Critical | CVSS4: CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | CVSS3: None | CWE: CWE-367, CWE-662 | AI-assisted-report: False
Affected/patched: Affected versions < 8.2.36 >= 8.3.0, < 8.3.37 >= 8.4.0, < 8.4.28 >= 8.5.0, < 8.5.13 Patched versions 8.2.36 8.3.37 8.4.28 8.5.13 Description Summary PHP's file-based session handler can leave a session file containing parts of two different serialized sessions

## GHSA-2fjv-p558-g82m
CVE: CVE-2026-129182 | Severity: Critical | CVSS4: CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | CVSS3: None | CWE: CWE-416, CWE-459 | AI-assisted-report: False
Affected/patched: Affected versions >= 8.5.0, < 8.5.13 Patched versions 8.5.13 Description Summary As part of CVE-2026-109619 ( GHSA-6wmf-4rv5-p3rp ), PHP 8.5.12 fixes a generic use-after-free of the last_fatal_error_backtrace global by clearing it during executor shutdown. Fur

## GHSA-g3vh-838c-65v7
CVE: CVE-2026-129481 | Severity: Critical | CVSS4: CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | CVSS3: None | CWE: CWE-416, CWE-459 | AI-assisted-report: True
Affected/patched: Affected versions >= 8.3.0, < 8.3.37 >= 8.4.0, < 8.4.28 >= 8.5.0, < 8.5.13 Patched versions 8.3.37 8.4.28 8.5.13 Description Summary PHP can retain a pointer to a script filename after session shutdown is interrupted and the request memory has been released. A

## GHSA-8mjj-2r7p-4hg2
CVE: CVE-2026-129474 | Severity: Critical | CVSS4: CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | CVSS3: None | CWE: CWE-416 | AI-assisted-report: True
Affected/patched: Affected versions >= 8.5.0, < 8.5.13 Patched versions 8.5.13 Description Summary PHP can access freed memory when collecting the arguments of a method handled by __call() or __callStatic() for a backtrace. On PHP 8.5 and later, an unauthenticated attacker may 

## GHSA-gr4f-wgx5-jpfv
CVE: CVE-2026-129496 | Severity: Critical | CVSS4: CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | CVSS3: None | CWE: CWE-416, CWE-459 | AI-assisted-report: True
Affected/patched: Affected versions < 8.2.36 >= 8.3.0, < 8.3.37 >= 8.4.0, < 8.4.28 >= 8.5.0, < 8.5.13 Patched versions 8.2.36 8.3.37 8.4.28 8.5.13 Description Summary PHP can retain a reference to a freed timezone cache when a diagnostic is written to a PHP error log file durin

## GHSA-jm4m-qfqx-967m
CVE: CVE-2026-129291 | Severity: High | CVSS4: CVSS:4.0/AV:L/AC:H/AT:P/PR:L/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H | CVSS3: None | CWE: CWE-416 | AI-assisted-report: True
Affected/patched: Affected versions >= 8.1.20, <= 8.1.34 >= 8.2.7, < 8.2.36 >= 8.3.0, < 8.3.37 >= 8.4.0, < 8.4.28 >= 8.5.0, < 8.5.13 Patched versions None 8.2.36 8.3.37 8.4.28 8.5.13 Description Summary PHP-FPM can dispatch an epoll event that refers to a freed worker record wh

## GHSA-5j3f-64r7-f564
CVE: CVE-2026-129538 | Severity: None | CVSS4: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:L/VA:L/SC:N/SI:N/SA:N | CVSS3: None | CWE: CWE-125, CWE-787, CWE-823 | AI-assisted-report: True
Affected/patched: Affected versions < 8.2.36 >= 8.3.0, < 8.3.37 >= 8.4.0, < 8.4.28 >= 8.5.0, < 8.5.13 Patched versions 8.2.36 8.3.37 8.4.28 8.5.13 Description Summary The PHP CGI binary ( php-cgi ) can access memory outside the supplied path information when a web server passes

## GHSA-68fq-fh7h-f8gr
CVE: CVE-2026-128090 | Severity: High | CVSS4: CVSS:4.0/AV:N/AC:L/AT:P/PR:N/UI:P/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N | CVSS3: None | CWE: CWE-347, CWE-757 | AI-assisted-report: False
Affected/patched: Affected versions < 8.2.36 >= 8.3.0, < 8.3.37 >= 8.4.0, < 8.4.28 >= 8.5.0, < 8.5.13 Patched versions 8.2.36 8.3.37 8.4.28 8.5.13 Description Summary An attacker who can modify an OpenSSL-signed Phar archive without changing its trusted public key can make PHP 

