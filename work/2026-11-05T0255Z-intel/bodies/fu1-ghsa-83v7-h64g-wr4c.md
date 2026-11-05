---
title: CVE-2026-114425 - GitHub Advisory Database
url: https://github.com/advisories/GHSA-83v7-h64g-wr4c
hostname: github.com
description: SEPPmail Secure Email Gateway before 15.1.1 trusts a file...
sitename: GitHub
date: "2026-11-04"
categories: ['advisory:526690']
fingerprint: "8d4474051d90ff6a"
---
## SEPPmail Secure Email Gateway before 15.1.1 trusts a file...

Critical severity
          
            Unreviewed
        
          Published
            Nov 4, 2026 
            to the GitHub Advisory Database
            •
            Updated Nov 4, 2026 

## Description

Published by the [National Vulnerability Database](https://nvd.nist.gov/vuln/detail/CVE-2026-114425)
      Nov 4, 2026 

Published to the GitHub Advisory Database
      Nov 4, 2026 

Last updated
      Nov 4, 2026 

SEPPmail Secure Email Gateway before 15.1.1 trusts a file path supplied in externally provided Large File Transfer attachment metadata. An unauthenticated remote sender can cause the mail-processing worker to disclose, move, or delete an accessible regular file when LFT is enabled and the message reaches an affected secure-mail processing path. The validated workers ran as root.

## References
