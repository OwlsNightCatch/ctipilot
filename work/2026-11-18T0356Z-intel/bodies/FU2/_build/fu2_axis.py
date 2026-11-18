from fu2_lib import *
AX = 'axis/axis-cve-2026-119618.normalized.txt'
AXRAW = 'axis/axis-cve-2026-119618.pdf.txt'
REG = 'axis/axis-help-advisories.extract.md'
CF = 'axis/certfr-avi-1549.extract.md'; CFR = 'axis/certfr-avi-1549.rawtext.txt'
AP = 'axis/apache-vulns24.extract.md'
FL = 'axis/axis-os-1211-release-flyer.normalized.txt'
UAX = 'https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf'
UREG = 'https://help.axis.com/en-us/security-advisories'
UCF = 'https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1549/'
UAP = 'https://httpd.apache.org/security/vulnerabilities_24.html'
UFL = 'https://www.axis.com/dam/public/permalink/274172/axis-os-1211-release-flyer-en-US_274172.pdf'
out = []
A = out.append
A('## 5. AXIS OS and Apache mod_http2 (CVE-2026-119618)\n')
A('Primary: ' + UAX + ' (one-page PDF; read with `python3 tools/fetch_source.py pdf` on 2026-11-18 ~04:50Z: "2024 chars from 5/27 streams", per-font ToUnicode decode, text-layer PDF, no OCR needed). The extractor emits one text run per line and splits tokens around hyphens and "://", so the saved raw text (`axis/axis-cve-2026-119618.pdf.txt`) is unreadable as prose; passages below are quoted from a whitespace-normalized copy (`axis/axis-cve-2026-119618.normalized.txt`: lines joined, split hyphens and punctuation re-attached, no word changed). A copy saved through `url --direct` could not be parsed by `pdftotext` (flate stream errors) and was discarded, so `fetch_source.py pdf` is the only working reader found; `pdfinfo` on that copy showed creator "Microsoft Word for Microsoft 365", created Mon Nov 16 07:20:54 2026 UTC, 1 page. Axis\'s own registry page: ' + UREG + ' (extract; page date 2026-11-17).\n')
A('### 5.1 What the Axis PDF says\n')
A(table([
 ('Advisory title, date, version', UAX, AX, 'Security Advisory CVE-2026-119618 – 2026-11-16 (v1.0)'),
 ('Affected products, solutions and services: one line; NO tracks, branches or fixed versions are enumerated', UAX, AX, 'Affected products, solutions, and services • AXIS OS 6.50.5.10 or higher'),
 ('Root cause attribution: the Apache project fixed it in httpd 2.4.71 on 11 Nov 2026', UAX, AX, 'The Apache Software Foundation released Apache HTTP Server 2.4.71 on November 11, 2026, fixing CVE-2026-119618,'),
 ('CVSS Axis gives (9.8 Critical), impact, auth state ("administrator-access" is the PDF text; the hyphen may be a line-break artefact)', UAX, AX, 'a CVSS 9.8 Critical remote code execution vulnerability that would allow an unauthenticated attacker to gain administrator-access to the Axis network device.'),
 ('Exploitation and public exploits (Axis\' knowledge only)', UAX, AX, 'To Axis’ knowledge, no known exploits exist publicly as of today and Axis is not aware that this has been exploited in its network products.'),
 ('Planned service release: all affected AXIS OS tracks, "within the next couple of weeks", exact timelines to follow', UAX, AX, 'Axis is working on a service release for all affected AXIS OS tracks within the next couple of weeks, more accurate timelines will be provided in time.'),
 ('Release-note wording Axis announces', UAX, AX, 'The release notes will state the following: Updated Apache to version 2.4.71 to increase overall cybersecurity.'),
 ('Devices outside the tracks but still supported', UAX, AX, 'Axis devices not included in these tracks and still under support will receive a patch according to their planned maintenance and release schedule.'),
 ('Update recommendation', UAX, AX, 'It is recommended to update the Axis device software.'),
 ('Workaround, introduction (verbatim)', UAX, AX, 'As an immediate workaround, configure the Axis device as below to prevent the vulnerability exploitation. Once an update has been provided, this setting can be reverted again.'),
 ('Workaround, setting 1 (device parameter via param.cgi; the PDF text layer shows "HTTP(S) :// <DEVICE-IP> /axis-cgi/..." with spaces)', UAX, AX, '/axis-cgi/param.cgi?action=update&System.HTTP2.AllowH2=no'),
 ('Workaround, setting 2', UAX, AX, '/axis-cgi/param.cgi?action=update&System.HTTP2.AllowH2c=no'),
 ('Bulk deployment', UAX, AX, 'Use Axis Device Manager or any other device configuration tool to mass-deploy this configuration accordingly.'),
 ('Contact', UAX, AX, 'For further assistance and questions, please contact Axis Technical Support.'),
]))
A('')
A('Not in the PDF (confirmed by reading all of `axis/axis-cve-2026-119618.normalized.txt`): any mention of mod_http2, "HTTP/2" prose, the device web interface, a list of AXIS OS tracks or release numbers, a fixed AXIS OS version, an LTS-track list, authentication/privilege wording beyond "unauthenticated", an exploit-prerequisite statement, or the CVSS vector. The only HTTP/2 references are the two parameter names in the workaround (System.HTTP2.AllowH2 and System.HTTP2.AllowH2c).\n')
A('### 5.2 Axis registry, CERT-FR and the Apache primary\n')
A(table([
 ('Axis registry row for AXIS OS: 9.8 Critical, Affected = Yes; "patched by upgrading to Apache version 2.4.71"; no released AXIS OS version listed (page date 2026-11-17)', UREG, REG, 'The vulnerability is patched by upgrading to Apache version 2.4.71. For an immediate workaround follow the mitigation steps in the security advisory.'),
 ('Registry row cells', UREG, REG, '9.8 (Critical) | Yes | [Axis Security Advisory](https://www.axis.com/dam/public/permalink/294609/cve-2026-119618pdf-en-US_294609.pdf)'),
 ('Registry page date', UREG, REG, 'date: "2026-11-17"'),
 ('CERT-FR (CERTFR-2026-AVI-1549; initial version 17 November 2026): affected = all versions from 6.50.5.10', UCF, CF, '- Axis OS toutes versions à partir de 6.50.5.10'),
 ('CERT-FR: Axis says a fix will be available within a few weeks', UCF, CF, "Axis déclare qu'un correctif sera disponible d'ici quelques semaines."),
 ('CERT-FR: a workaround is provided', UCF, CF, 'Une mesure de contournement est fournie.'),
 ('CERT-FR: risk = remote arbitrary code execution', UCF, CF, '- Exécution de code arbitraire à distance'),
 ('CERT-FR revision history (only initial version, 17 Nov 2026)', UCF, CFR, '17 novembre 2026\nVersion initiale'),
 ('Apache httpd security page: CVE-2026-119618 is mod_http2 assign_headers heap corruption and RCE, rated critical', UAP, AP, '(critical):mod\\_http2: heap corruption and RCE in assign\\_headers'),
 ('Apache: affected httpd 2.4.55 through 2.4.70; mod_h2 2.0.8 through 2.0.42', UAP, AP, 'can lead to RCE. This issue affects Apache HTTP Server: from 2.4.55 through 2.4.70. Affected releases of mod\\_h2 from GitHub: from 2.0.8 through 2.0.42.'),
 ('Apache: fixed in 2.4.71, released 2026-11-11; finders Anthropic\'s OSS Scanner and Google Cloud VR', UAP, AP, 'Update 2.4.71 released 2026-11-11 Affects 2.4.55 through 2.4.70'),
 ('Apache: finder credit', UAP, AP, "finder: Anthropic's OSS Scanner, as vulnerability ANT-2026-MAPKT6MZ"),
 ('Context: AXIS OS 12.11 (active track) release flyer says Apache was updated to 2.4.67 there (inside the Apache-affected 2.4.55-2.4.70 range)', UFL, FL, 'Apache has been updated to version 2.4.67 and curl has been updated to version 8.20.'),
 ('Context: Axis explains tracks: active track and LTS tracks (a new LTS track every two years, maintained five years)', UFL, FL, 'An LTS track has a fixed feature set, and a new track is issued every two years and maintained for five years.'),
]))
A('')
A('### 5.3 Version table\n')
A('| item | value | source |')
A('|---|---|---|')
A('| Affected AXIS OS | "AXIS OS 6.50.5.10 or higher" (CERT-FR: "toutes versions à partir de 6.50.5.10"); tracks not enumerated | Axis PDF; CERT-FR |')
A('| Underlying component | Apache HTTP Server 2.4.55 through 2.4.70 affected, mod_http2 `assign_headers()`; fixed 2.4.71 (2026-11-11) | Apache |')
A('| Axis CVSS | 9.8 Critical (Axis states the number; no vector in the PDF) | Axis PDF; registry |')
A('| Fixed AXIS OS | none released as of 2026-11-18 ~05:00Z: "working on a service release for all affected AXIS OS tracks within the next couple of weeks" (dated 2026-11-16) | Axis PDF; registry lists no released version |')
A('| Devices outside those tracks, still supported | patch "according to their planned maintenance and release schedule" | Axis PDF |')
A('| Workaround | System.HTTP2.AllowH2=no and System.HTTP2.AllowH2c=no via /axis-cgi/param.cgi?action=update; revert after update | Axis PDF |')
A('')
A('### 5.4 Contradictions with the first pass (item 13) and open gaps\n')
A('- CONFIRMED: 6.50.5.10 or higher; Apache 2.4.71 of 2026-11-11; "CVSS 9.8" stated by Axis; unauthenticated, administrator access; "To Axis\' knowledge, no known exploits exist publicly ... not aware that this has been exploited"; service release for all affected tracks "within the next couple of weeks"; "more accurate timelines will be provided in time"; release-note wording; devices outside the tracks; workaround parameters and Axis Device Manager bulk deployment; CERT-FR AVI-1549 (initial version 17 November 2026).')
A('- NOT SUPPORTED BY THE PAGE: the first pass summary says "Axis phrases the advisory as an HTTP/2 flaw reachable on the device web interface". The Axis PDF never says "HTTP/2 flaw" or "web interface"; it says only that Apache fixed CVE-2026-119618 and gives two HTTP2 device parameters as the workaround. The mod_http2 attribution is the Apache project\'s (Apache page above); the inference that the workaround disables the vulnerable path is the analyst\'s.')
A('- WORDING: the first pass title says "calls for a service release within weeks"; the PDF says Axis "is working on a service release ... within the next couple of weeks". It is a plan, not a date, and the PDF says more accurate timelines will follow. "Axis has no fixed release yet" is true as of the PDF and the registry (no released version listed, checked 2026-11-18).')
A('- WORDING: "no exploitation known to Axis" is accurate but note the two limbs: "no known exploits exist publicly" (about public exploit code) and "Axis is not aware that this has been exploited in its network products". Neither is a statement about Apache httpd generally; the store entry for the Apache issue holds that.')
A('- OPEN: the AXIS OS tracks and release numbers affected; the AXIS OS release carrying Apache 2.4.71; whether PoC code for CVE-2026-119618 exists (the Axis statement is as of 2026-11-16; the Apache and distribution coverage is in the existing store entry, not re-read here); Axis\'s later timeline update. The Axis PDF has no revision after v1.0 and the registry shows no released version.')
A('- The Axis registry also lists other Apache-related rows (CVE-2026-49975 and CVE-2026-48913, patched by upgrading to Apache 2.4.68), i.e. Axis handles Apache CVEs by bundling a newer Apache in a service release, consistent with the release-note wording above.\n')
SECTION = '\n'.join(out)
