---
title: nginx security advisories
url: https://nginx.org/en/security_advisories.html
hostname: nginx.org
sitename: nginx.org
date: "2010-01-13"
fingerprint: ae04bbf6f9b8af93
---
## nginx security advisories

All nginx security issues should be reported
via one of the methods listed
[here](https://github.com/nginx/nginx/blob/master/SECURITY.md).

Patches are signed using one of the
[PGP public keys](https://nginx.org/pgp_keys.html).

- Buffer overflow when using alias with rewrite
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000162416)
[CVE-2026-15176](https://www.cve.org/CVERecord?id=CVE-2026-15176)
Not vulnerable: 1.31.7+, 1.30.6+
Vulnerable: 0.1.29-1.31.6
- Buffer overflow in script evaluation
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000162607)
[CVE-2026-93479](https://www.cve.org/CVERecord?id=CVE-2026-93479)
Not vulnerable: 1.31.7+, 1.30.6+
Vulnerable: 1.31.2-1.31.6, 1.30.0-1.30.5
- Request body injection in HTTP/3
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000162613)
[CVE-2026-95101](https://www.cve.org/CVERecord?id=CVE-2026-95101)
Not vulnerable: 1.31.7+, 1.30.6+
Vulnerable: 1.25.0-1.31.6
- Session forgery when using TLS session tickets
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000162606)
[CVE-2026-97629](https://www.cve.org/CVERecord?id=CVE-2026-97629)
Not vulnerable: 1.31.7+, 1.30.6+
Vulnerable: 1.23.2-1.31.6
- Use-after-free when using asynchronous file I/O (AIO)
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000162608)
[CVE-2026-97205](https://www.cve.org/CVERecord?id=CVE-2026-97205)
Not vulnerable: 1.31.7+, 1.30.6+
Vulnerable: 0.8.11-1.31.6
- Buffer overflow when using ngx\_http\_v3\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000162604)
[CVE-2026-90439](https://www.cve.org/CVERecord?id=CVE-2026-90439)
Not vulnerable: 1.31.6+, 1.30.5+
Vulnerable: 1.29.2-1.31.5
- Buffer overflow when using map and regex
Severity: **major**
[Advisory](https://my.f5.com/manage/s/article/K000162097)
[CVE-2026-42533](https://www.cve.org/CVERecord?id=CVE-2026-42533)
Not vulnerable: 1.31.3+, 1.30.4+
Vulnerable: 0.9.6-1.31.2
- Memory disclosure when using ngx\_http\_slice\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000162100)
[CVE-2026-60005](https://www.cve.org/CVERecord?id=CVE-2026-60005)
Not vulnerable: 1.31.3+, 1.30.4+
Vulnerable: 1.15.8-1.31.2
- Use-after-free when using ngx\_http\_ssi\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000162098)
[CVE-2026-56434](https://www.cve.org/CVERecord?id=CVE-2026-56434)
Not vulnerable: 1.31.3+, 1.30.4+
Vulnerable: 0.8.11-1.31.2
- Use-after-free in HTTP/3
Severity: **major**
[Advisory](https://my.f5.com/manage/s/article/K000161616)
[CVE-2026-42530](https://www.cve.org/CVERecord?id=CVE-2026-42530)
Not vulnerable: 1.31.2+
Vulnerable: 1.31.0-1.31.1
- Buffer overflow in the ngx\_http\_proxy\_v2\_module and ngx\_http\_grpc\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000161584)
[CVE-2026-42055](https://www.cve.org/CVERecord?id=CVE-2026-42055)
Not vulnerable: 1.31.2+, 1.30.3+
Vulnerable: 1.13.10-1.31.1
- Buffer overread in the ngx\_http\_charset\_module
Severity: low
[Advisory](https://my.f5.com/manage/s/article/K000161585)
[CVE-2026-48142](https://www.cve.org/CVERecord?id=CVE-2026-48142)
Not vulnerable: 1.31.2+, 1.30.3+
Vulnerable: 0.3.50-1.31.1
- Buffer overflow in the ngx\_http\_rewrite\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000161377)
[CVE-2026-9256](https://www.cve.org/CVERecord?id=CVE-2026-9256)
Not vulnerable: 1.31.1+, 1.30.2+
Vulnerable: 0.1.17-1.31.0
- HTTP/2 request injection in the ngx\_http\_proxy\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000161131)
[CVE-2026-42926](https://www.cve.org/CVERecord?id=CVE-2026-42926)
Not vulnerable: 1.31.0+, 1.30.1+
Vulnerable: 1.29.4-1.30.0
- Buffer overflow in the ngx\_http\_rewrite\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000161019)
[CVE-2026-42945](https://www.cve.org/CVERecord?id=CVE-2026-42945)
Not vulnerable: 1.31.0+, 1.30.1+
Vulnerable: 0.6.27-1.30.0
- Buffer overread in the ngx\_http\_scgi\_module and ngx\_http\_uwsgi\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000161027)
[CVE-2026-42946](https://www.cve.org/CVERecord?id=CVE-2026-42946)
Not vulnerable: 1.31.0+, 1.30.1+
Vulnerable: 0.8.42-1.30.0
- Buffer overread in the ngx\_http\_charset\_module
Severity: low
[Advisory](https://my.f5.com/manage/s/article/K000161028)
[CVE-2026-42934](https://www.cve.org/CVERecord?id=CVE-2026-42934)
Not vulnerable: 1.31.0+, 1.30.1+
Vulnerable: 0.3.50-1.30.0
- HTTP/3 address spoofing
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000161068)
[CVE-2026-40460](https://www.cve.org/CVERecord?id=CVE-2026-40460)
Not vulnerable: 1.31.0+, 1.30.1+
Vulnerable: 1.25.0-1.30.0
- resolver use-after-free in OCSP
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000161021)
[CVE-2026-40701](https://www.cve.org/CVERecord?id=CVE-2026-40701)
Not vulnerable: 1.31.0+, 1.30.1+
Vulnerable: 1.19.0-1.30.0
- Buffer overflow in ngx\_http\_dav\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000160382)
[CVE-2026-27654](https://www.cve.org/CVERecord?id=CVE-2026-27654)
Not vulnerable: 1.29.7+, 1.28.3+
Vulnerable: 0.5.13-1.29.6
- Buffer overflow in the ngx\_http\_mp4\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000160364)
[CVE-2026-27784](https://www.cve.org/CVERecord?id=CVE-2026-27784)
Not vulnerable: 1.29.7+, 1.28.3+
Vulnerable: 1.1.19-1.29.6
- Buffer overflow in the ngx\_http\_mp4\_module
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000160366)
[CVE-2026-32647](https://www.cve.org/CVERecord?id=CVE-2026-32647)
Not vulnerable: 1.29.7+, 1.28.3+
Vulnerable: 1.1.19-1.29.6
- NULL pointer dereference while using CRAM-MD5 or APOP
Severity: low
[Advisory](https://my.f5.com/manage/s/article/K000160383)
[CVE-2026-27651](https://www.cve.org/CVERecord?id=CVE-2026-27651)
Not vulnerable: 1.29.7+, 1.28.3+
Vulnerable: 0.5.15-1.29.6
- Injection in auth\_http and XCLIENT
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000160367)
[CVE-2026-28753](https://www.cve.org/CVERecord?id=CVE-2026-28753)
Not vulnerable: 1.29.7+, 1.28.3+
Vulnerable: 0.6.27-1.29.6
- OCSP result bypass in stream
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000160368)
[CVE-2026-28755](https://www.cve.org/CVERecord?id=CVE-2026-28755)
Not vulnerable: 1.29.7+, 1.28.3+
Vulnerable: 1.27.2-1.29.6
- SSL upstream injection
Severity: medium
[Advisory](https://my.f5.com/manage/s/article/K000159824)
[CVE-2026-1642](https://www.cve.org/CVERecord?id=CVE-2026-1642)
Not vulnerable: 1.29.5+, 1.28.2+
Vulnerable: 1.3.0-1.29.4
- Buffer overread in the ngx\_mail\_smtp\_module
Severity: low
[Advisory](https://my.f5.com/manage/s/article/K000152786)
[CVE-2025-53859](https://www.cve.org/CVERecord?id=CVE-2025-53859)
Not vulnerable: 1.29.1+
Vulnerable: 0.7.22-1.29.0
- SSL session reuse vulnerability
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2025/NYEUJX7NCBCGJGXDFVXNMAAMJDFSE45G.html)
[CVE-2025-23419](https://www.cve.org/CVERecord?id=CVE-2025-23419)
Not vulnerable: 1.27.4+, 1.26.3+
Vulnerable: 1.11.4-1.27.3
- Buffer overread in the ngx\_http\_mp4\_module
Severity: low
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2024/UUOCLLONPR6244YQYU65PO5LB7JDYCWM.html)
[CVE-2024-7347](https://www.cve.org/CVERecord?id=CVE-2024-7347)
Not vulnerable: 1.27.1+, 1.26.2+
Vulnerable: 1.5.13-1.27.0
[The patch](https://nginx.org/download/patch.2024.mp4.txt) [pgp](https://nginx.org/download/patch.2024.mp4.txt.asc)
- Buffer overwrite in HTTP/3
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2024/GMY32CSHFH6VFTN76HJNX7WNEX4RLHF6.html)
[CVE-2024-32760](https://www.cve.org/CVERecord?id=CVE-2024-32760)
Not vulnerable: 1.27.0+, 1.26.1+
Vulnerable: 1.25.0-1.25.5, 1.26.0
- Stack overflow and use-after-free in HTTP/3
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2024/GMY32CSHFH6VFTN76HJNX7WNEX4RLHF6.html)
[CVE-2024-31079](https://www.cve.org/CVERecord?id=CVE-2024-31079)
Not vulnerable: 1.27.0+, 1.26.1+
Vulnerable: 1.25.0-1.25.5, 1.26.0
- NULL pointer dereference in HTTP/3
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2024/GMY32CSHFH6VFTN76HJNX7WNEX4RLHF6.html)
[CVE-2024-35200](https://www.cve.org/CVERecord?id=CVE-2024-35200)
Not vulnerable: 1.27.0+, 1.26.1+
Vulnerable: 1.25.0-1.25.5, 1.26.0
- Memory disclosure in HTTP/3
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2024/GMY32CSHFH6VFTN76HJNX7WNEX4RLHF6.html)
[CVE-2024-34161](https://www.cve.org/CVERecord?id=CVE-2024-34161)
Not vulnerable: 1.27.0+, 1.26.1+
Vulnerable: 1.25.0-1.25.5, 1.26.0
- NULL pointer dereference in HTTP/3
Severity: **major**
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2024/NW6MNW34VZ6HDIHH5YFBIJYZJN7FGNAV.html)
[CVE-2024-24989](https://www.cve.org/CVERecord?id=CVE-2024-24989)
Not vulnerable: 1.25.4+
Vulnerable: 1.25.3
- Use-after-free in HTTP/3
Severity: **major**
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2024/NW6MNW34VZ6HDIHH5YFBIJYZJN7FGNAV.html)
[CVE-2024-24990](https://www.cve.org/CVERecord?id=CVE-2024-24990)
Not vulnerable: 1.25.4+
Vulnerable: 1.25.0-1.25.3
- Memory corruption in the ngx\_http\_mp4\_module
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2022/RBRRON6PYBJJM2XIAPQBFBVLR4Q6IHRA.html)
[CVE-2022-41741](https://www.cve.org/CVERecord?id=CVE-2022-41741)
Not vulnerable: 1.23.2+, 1.22.1+
Vulnerable: 1.1.3-1.23.1, 1.0.7-1.0.15
[The patch](https://nginx.org/download/patch.2022.mp4.txt) [pgp](https://nginx.org/download/patch.2022.mp4.txt.asc)
- Memory disclosure in the ngx\_http\_mp4\_module
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2022/RBRRON6PYBJJM2XIAPQBFBVLR4Q6IHRA.html)
[CVE-2022-41742](https://www.cve.org/CVERecord?id=CVE-2022-41742)
Not vulnerable: 1.23.2+, 1.22.1+
Vulnerable: 1.1.3-1.23.1, 1.0.7-1.0.15
[The patch](https://nginx.org/download/patch.2022.mp4.txt) [pgp](https://nginx.org/download/patch.2022.mp4.txt.asc)
- 1-byte memory overwrite in resolver
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2021/000300.html)
[CVE-2021-23017](https://www.cve.org/CVERecord?id=CVE-2021-23017)
Not vulnerable: 1.21.0+, 1.20.1+
Vulnerable: 0.6.18-1.20.0
[The patch](https://nginx.org/download/patch.2021.resolver.txt) [pgp](https://nginx.org/download/patch.2021.resolver.txt.asc)
- Excessive CPU usage in HTTP/2 with small window updates
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2019/000249.html)
[CVE-2019-9511](https://www.cve.org/CVERecord?id=CVE-2019-9511)
Not vulnerable: 1.17.3+, 1.16.1+
Vulnerable: 1.9.5-1.17.2
- Excessive CPU usage in HTTP/2 with priority changes
Severity: low
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2019/000249.html)
[CVE-2019-9513](https://www.cve.org/CVERecord?id=CVE-2019-9513)
Not vulnerable: 1.17.3+, 1.16.1+
Vulnerable: 1.9.5-1.17.2
- Excessive memory usage in HTTP/2 with zero length headers
Severity: low
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2019/000249.html)
[CVE-2019-9516](https://www.cve.org/CVERecord?id=CVE-2019-9516)
Not vulnerable: 1.17.3+, 1.16.1+
Vulnerable: 1.9.5-1.17.2
- Excessive memory usage in HTTP/2
Severity: low
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2018/000220.html)
[CVE-2018-16843](https://www.cve.org/CVERecord?id=CVE-2018-16843)
Not vulnerable: 1.15.6+, 1.14.1+
Vulnerable: 1.9.5-1.15.5
- Excessive CPU usage in HTTP/2
Severity: low
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2018/000220.html)
[CVE-2018-16844](https://www.cve.org/CVERecord?id=CVE-2018-16844)
Not vulnerable: 1.15.6+, 1.14.1+
Vulnerable: 1.9.5-1.15.5
- Memory disclosure in the ngx\_http\_mp4\_module
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2018/000221.html)
[CVE-2018-16845](https://www.cve.org/CVERecord?id=CVE-2018-16845)
Not vulnerable: 1.15.6+, 1.14.1+
Vulnerable: 1.1.3-1.15.5, 1.0.7-1.0.15
[The patch](https://nginx.org/download/patch.2018.mp4.txt) [pgp](https://nginx.org/download/patch.2018.mp4.txt.asc)
- Integer overflow in the range filter
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2017/000200.html)
[CVE-2017-7529](https://www.cve.org/CVERecord?id=CVE-2017-7529)
Not vulnerable: 1.13.3+, 1.12.1+
Vulnerable: 0.5.6-1.13.2
[The patch](https://nginx.org/download/patch.2017.ranges.txt) [pgp](https://nginx.org/download/patch.2017.ranges.txt.asc)
- NULL pointer dereference while writing client request body
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2016/000179.html)
[CVE-2016-4450](https://www.cve.org/CVERecord?id=CVE-2016-4450)
Not vulnerable: 1.11.1+, 1.10.1+
Vulnerable: 1.3.9-1.11.0
[The patch](https://nginx.org/download/patch.2016.write.txt) [pgp](https://nginx.org/download/patch.2016.write.txt.asc) (for 1.9.13-1.11.0)
[The patch](https://nginx.org/download/patch.2016.write2.txt) [pgp](https://nginx.org/download/patch.2016.write2.txt.asc) (for 1.3.9-1.9.12)
- Invalid pointer dereference in resolver
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2016/000169.html)
[CVE-2016-0742](https://www.cve.org/CVERecord?id=CVE-2016-0742)
Not vulnerable: 1.9.10+, 1.8.1+
Vulnerable: 0.6.18-1.9.9
- Use-after-free during CNAME response processing in resolver
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2016/000169.html)
[CVE-2016-0746](https://www.cve.org/CVERecord?id=CVE-2016-0746)
Not vulnerable: 1.9.10+, 1.8.1+
Vulnerable: 0.6.18-1.9.9
- Insufficient limits of CNAME resolution in resolver
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2016/000169.html)
[CVE-2016-0747](https://www.cve.org/CVERecord?id=CVE-2016-0747)
Not vulnerable: 1.9.10+, 1.8.1+
Vulnerable: 0.6.18-1.9.9
- SSL session reuse vulnerability
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2014/000147.html)
[CVE-2014-3616](https://www.cve.org/CVERecord?id=CVE-2014-3616)
Not vulnerable: 1.7.5+, 1.6.2+
Vulnerable: 0.5.6-1.7.4
- STARTTLS command injection
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2014/000144.html)
[CVE-2014-3556](https://www.cve.org/CVERecord?id=CVE-2014-3556)
Not vulnerable: 1.7.4+, 1.6.1+
Vulnerable: 1.5.6-1.7.3
[The patch](https://nginx.org/download/patch.2014.starttls.txt) [pgp](https://nginx.org/download/patch.2014.starttls.txt.asc)
- SPDY heap buffer overflow
Severity: **major**
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2014/000135.html)
[CVE-2014-0133](https://www.cve.org/CVERecord?id=CVE-2014-0133)
Not vulnerable: 1.5.12+, 1.4.7+
Vulnerable: 1.3.15-1.5.11
[The patch](https://nginx.org/download/patch.2014.spdy2.txt) [pgp](https://nginx.org/download/patch.2014.spdy2.txt.asc)
- SPDY memory corruption
Severity: **major**
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2014/000132.html)
[CVE-2014-0088](https://www.cve.org/CVERecord?id=CVE-2014-0088)
Not vulnerable: 1.5.11+
Vulnerable: 1.5.10
[The patch](https://nginx.org/download/patch.2014.spdy.txt) [pgp](https://nginx.org/download/patch.2014.spdy.txt.asc)
- Request line parsing vulnerability
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2013/000125.html)
[CVE-2013-4547](https://www.cve.org/CVERecord?id=CVE-2013-4547)
Not vulnerable: 1.5.7+, 1.4.4+
Vulnerable: 0.8.41-1.5.6
[The patch](https://nginx.org/download/patch.2013.space.txt) [pgp](https://nginx.org/download/patch.2013.space.txt.asc)
- Memory disclosure with specially crafted HTTP backend responses
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2013/000114.html)
[CVE-2013-2070](https://www.cve.org/CVERecord?id=CVE-2013-2070)
Not vulnerable: 1.5.0+, 1.4.1+, 1.2.9+
Vulnerable: 1.1.4-1.2.8, 1.3.9-1.4.0
[The patch](https://nginx.org/download/patch.2013.chunked.txt) [pgp](https://nginx.org/download/patch.2013.chunked.txt.asc) (for 1.3.9-1.4.0)
[The patch](https://nginx.org/download/patch.2013.proxy.txt) [pgp](https://nginx.org/download/patch.2013.proxy.txt.asc) (for 1.1.4-1.2.8)
- Stack-based buffer overflow with specially crafted request
Severity: **major**
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2013/000112.html)
[CVE-2013-2028](https://www.cve.org/CVERecord?id=CVE-2013-2028)
Not vulnerable: 1.5.0+, 1.4.1+
Vulnerable: 1.3.9-1.4.0
[The patch](https://nginx.org/download/patch.2013.chunked.txt) [pgp](https://nginx.org/download/patch.2013.chunked.txt.asc)
- Vulnerabilities with Windows directory aliases
Severity: medium
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2012/000086.html)
[CVE-2011-4963](https://www.cve.org/CVERecord?id=CVE-2011-4963)
Not vulnerable: 1.3.1+, 1.2.1+
Vulnerable: nginx/Windows 0.7.52-1.3.0
- Buffer overflow in the ngx\_http\_mp4\_module
Severity: **major**
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2012/000080.html)
[CVE-2012-2089](https://www.cve.org/CVERecord?id=CVE-2012-2089)
Not vulnerable: 1.1.19+, 1.0.15+
Vulnerable: 1.1.3-1.1.18, 1.0.7-1.0.14
[The patch](https://nginx.org/download/patch.2012.mp4.txt) [pgp](https://nginx.org/download/patch.2012.mp4.txt.asc)
- Memory disclosure with specially crafted backend responses
Severity: **major**
[Advisory](https://mailman.nginx.org/pipermail/nginx-announce/2012/000076.html)
[CVE-2012-1180](https://www.cve.org/CVERecord?id=CVE-2012-1180)
Not vulnerable: 1.1.17+, 1.0.14+
Vulnerable: 0.1.0-1.1.16
[The patch](https://nginx.org/download/patch.2012.memory.txt) [pgp](https://nginx.org/download/patch.2012.memory.txt.asc)
- Buffer overflow in resolver
Severity: medium
[CVE-2011-4315](https://www.cve.org/CVERecord?id=CVE-2011-4315)
Not vulnerable: 1.1.8+, 1.0.10+
Vulnerable: 0.6.18-1.1.7
- Vulnerabilities with invalid UTF-8 sequence on Windows
Severity: **major**
[CVE-2010-2266](https://www.cve.org/CVERecord?id=CVE-2010-2266)
Not vulnerable: 0.8.41+, 0.7.67+
Vulnerable: nginx/Windows 0.7.52-0.8.40
- Vulnerabilities with Windows file default stream
Severity: **major**
[CVE-2010-2263](https://www.cve.org/CVERecord?id=CVE-2010-2263)
Not vulnerable: 0.8.40+, 0.7.66+
Vulnerable: nginx/Windows 0.7.52-0.8.39
- Vulnerabilities with Windows 8.3 filename pseudonyms
Severity: **major**
[CORE-2010-0121](http://www.coresecurity.com/content/filename-pseudonyms-vulnerabilities)
Not vulnerable: 0.8.33+, 0.7.65+
Vulnerable: nginx/Windows 0.7.52-0.8.32
- An error log data are not sanitized
Severity: none
[CVE-2009-4487](https://www.cve.org/CVERecord?id=CVE-2009-4487)
Not vulnerable: none
Vulnerable: all
- The renegotiation vulnerability in SSL protocol
Severity: **major**
[VU#120541](http://www.kb.cert.org/vuls/id/120541) [CVE-2009-3555](https://www.cve.org/CVERecord?id=CVE-2009-3555)
Not vulnerable: 0.8.23+, 0.7.64+
Vulnerable: 0.1.0-0.8.22
[The patch](https://nginx.org/download/patch.cve-2009-3555.txt) [pgp](https://nginx.org/download/patch.cve-2009-3555.txt.asc)
- Directory traversal vulnerability
Severity: minor
[CVE-2009-3898](https://www.cve.org/CVERecord?id=CVE-2009-3898)
Not vulnerable: 0.8.17+, 0.7.63+
Vulnerable: 0.1.0-0.8.16
- Buffer underflow vulnerability
Severity: **major**
[VU#180065](http://www.kb.cert.org/vuls/id/180065) [CVE-2009-2629](https://www.cve.org/CVERecord?id=CVE-2009-2629)
Not vulnerable: 0.8.15+, 0.7.62+, 0.6.39+, 0.5.38+
Vulnerable: 0.1.0-0.8.14
[The patch](https://nginx.org/download/patch.180065.txt) [pgp](https://nginx.org/download/patch.180065.txt.asc)
- Null pointer dereference vulnerability
Severity: **major**
[CVE-2009-3896](https://www.cve.org/CVERecord?id=CVE-2009-3896)
Not vulnerable: 0.8.14+, 0.7.62+, 0.6.39+, 0.5.38+
Vulnerable: 0.1.0-0.8.13
[The patch](https://nginx.org/download/patch.null.pointer.txt) [pgp](https://nginx.org/download/patch.null.pointer.txt.asc)
