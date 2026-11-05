---
title: CVE-2026-114424 - GitHub Advisory Database
url: https://github.com/advisories/GHSA-3C43-M234-72QW
hostname: github.com
description: SEPPmail Secure Email Gateway before 15.1.1 can evaluate...
sitename: GitHub
date: "2026-11-04"
categories: ['advisory:526691']
fingerprint: "8f4474055d80da6a"
---
## SEPPmail Secure Email Gateway before 15.1.1 can evaluate...

Critical severity
          
            Unreviewed
        
          Published
            Nov 4, 2026 
            to the GitHub Advisory Database
            •
            Updated Nov 4, 2026 

## Description

Published by the [National Vulnerability Database](https://nvd.nist.gov/vuln/detail/CVE-2026-114424)
      Nov 4, 2026 

Published to the GitHub Advisory Database
      Nov 4, 2026 

Last updated
      Nov 4, 2026 

SEPPmail Secure Email Gateway before 15.1.1 can evaluate attacker-influenced replacement text as Perl code in sender or recipient replacement rules. An unauthenticated remote sender can execute operating-system commands in the mail-processing worker context when an active rule uses message-derived replacement data and its search condition matches. The validated worker context was root.

## References
