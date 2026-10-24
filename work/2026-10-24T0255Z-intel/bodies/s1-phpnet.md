---
title: "PHP: News Archive - 2026"
url: https://www.php.net/archive/2026.php
hostname: php.net
description: PHP is a popular general-purpose scripting language that powers everything from your blog to the most popular websites in the world.
sitename: Official_Php
date: "2026-10-23"
fingerprint: f4565778bb0454c8
---
## [Informational advisory: Session upload progress](https://www.php.net/archive/2026.php#2026-10-23-1)

We suggest you set `session.upload_progress.enabled=0` until the
        next regular bugfix release, to fully protect from an unlikely RCE vector.
        This setting was already listed as a mitigation in the
        [GHSA-6wmf-4rv5-p3rp](https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp)
        advisory for CVE-2026-109619 published on Oct 21st, 2026. If you applied it
        then, keep it in place and no further action is needed.

The issue can only occur under an unusual combination of configuration and
        application code. An application must set
        `session.serialize_handler` to `php_binary` or
        `php_serialize` in its configuration and then switch it to
        `php` at runtime with `ini_set()` before calling
        `session_start()`. Session upload progress must also still be
        enabled. Applications that never change the serialize handler at runtime can
        keep the feature enabled. Since this setup is unlikely in practice, we are
        handling it in the regular release cycle and will publish a full advisory for
        CVE-2026-115560 with the next release.
