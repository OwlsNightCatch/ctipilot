---
title: Apache HTTP Server 2.4.71 Released
url: https://downloads.apache.org/httpd/Announcement2.4.html
hostname: apache.org
sitename: downloads.apache.org
date: "2026-11-11"
fingerprint: bf5146daede37750
---
November 11, 2026

The Apache Software Foundation and the Apache HTTP Server Project are
   pleased to [announce](https://www.apache.org/dist/httpd/Announcement2.4.html)
   the release of version 2.4.71 of the Apache
   HTTP Server ("Apache").  This version of Apache is our latest GA
   release of Apache HTTPD and is recommended over all previous releases.

We consider this release to be the best version of Apache available, and encourage users of all prior versions to upgrade.

Apache HTTP Server 2.4.71 is available for download from:

Please see the [CHANGES\_2.4](https://downloads.apache.org/CHANGES_2.4) file, linked from the download page, for a
   full list of changes.  A condensed list, [CHANGES\_2.4.71](https://downloads.apache.org/CHANGES_2.4.71) includes only
   those changes introduced since the prior 2.4 release.  A summary of all 
   of the security vulnerabilities addressed in this and earlier releases 
   is available:

This release requires the Apache Portable Runtime (APR), minimum version 1.5.x, and APR-Util, minimum version 1.5.x. Some features may require the 1.6.x version of both APR and APR-Util. The APR libraries must be upgraded for all features of httpd to operate correctly.

When upgrading or installing this version of Apache, please bear in mind that if you intend to use Apache with one of the threaded MPMs (other than the Prefork MPM), you must ensure that any modules you will be using (and the libraries they depend on) are thread-safe.
