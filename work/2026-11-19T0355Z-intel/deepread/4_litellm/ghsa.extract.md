---
title: Sandbox escape in custom-code guardrail
author: Jaydns
url: https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p
hostname: github.com
description: "### Impact The `POST /guardrails/test_custom_code` endpoint runs user-supplied Python inside a hand-rolled sandbox. The sandbox can be escaped using bytecode-level techniques, allowing arbitrary..."
sitename: GitHub
date: "2026-05-07"
categories: ['repository:671269505']
fingerprint: "2bb2dfbb9c60ba80"
---
  
    ### Impact

The `POST /guardrails/test_custom_code` endpoint runs user-supplied Python inside a hand-rolled sandbox. The sandbox can be escaped using bytecode-level techniques, allowing arbitrary code execution in the proxy process — which runs as root in the default Docker image.

**Reaching the endpoint requires a proxy-admin credential** in default configurations.

### Patches

Fixed in **`1.83.11`**. The hand-rolled sandbox has been replaced with `RestrictedPython`. Upgrade to `1.83.11` or later.

### Workarounds

If upgrading is not immediately possible, block `POST /guardrails/test_custom_code` at your reverse proxy or API gateway.

### References

## Impact

The

`POST /guardrails/test_custom_code`endpoint runs user-supplied Python inside a hand-rolled sandbox. The sandbox can be escaped using bytecode-level techniques, allowing arbitrary code execution in the proxy process — which runs as root in the default Docker image.Reaching the endpoint requires a proxy-admin credentialin default configurations.
## Patches

Fixed in

`1.83.11``RestrictedPython`. Upgrade to`1.83.11`or later.
## Workarounds

If upgrading is not immediately possible, block

`POST /guardrails/test_custom_code`at your reverse proxy or API gateway.
## References

`v1.83.10-stable`
