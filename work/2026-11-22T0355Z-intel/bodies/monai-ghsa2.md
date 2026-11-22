---
title: Path traversal in datastore upload endpoints allows arbitrary file write
author: Ericspod
url: https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94
hostname: github.com
description: Originally reported by @aws-sec-vdp at https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-cxx7-378q-5622 Solved here (https://github.com/Project-MONAI/MONAILabel/pull/1915) and re-r...
sitename: GitHub
date: "2026-11-18"
categories: ['repository:351826770']
fingerprint: "990bdd3dbeb4fac0"
---
  
    Originally reported by [@aws-sec-vdp](https://github.com/aws-sec-vdp) at [https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-cxx7-378q-5622](https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-cxx7-378q-5622)

Solved here ([#1915](https://github.com/Project-MONAI/MONAILabel/pull/1915)) and re-reported to generate CVE in the correct repository.

### Impact

The `PUT /datastore/image` endpoint accepts a caller-controlled `image` query parameter that is used as the image ID without validation. `LocalDatastore.add_image()` appends the file extension to this ID, joins it onto the datastore image directory, and writes the uploaded file to the resulting path with `shutil.copy()`. Because the resolved path is never checked to be inside the datastore, a value such as `../../../tmp/x` writes the uploaded content to any location the MONAI Label process can write to. `LocalDatastore.save_label()` (`PUT /datastore/label`) builds its destination from the image ID and label tag in the same way.

An arbitrary file write can lead to remote code execution (for example by overwriting application code or adding entries to `.ssh/authorized_keys` or cron), or to denial of service by overwriting configuration files.

Authentication is disabled by default (`MONAI_LABEL_AUTH_ENABLE=False`), so in the default configuration any network client that can reach the server can exploit this. With authentication enabled, the `ANNOTATOR` role is sufficient.

This issue was originally reported privately against the MONAI repository (GHSA-cxx7-378q-5622) and is tracked here because the affected code is in MONAI Label.

### Patches

Fixed in [#1915](https://github.com/Project-MONAI/MONAILabel/pull/1915). Both `add_image()` and `save_label()` now resolve the destination (including the label tag directory) and reject any path outside the datastore image/labels directories. The `/datastore/image` endpoint also reduces the image ID to its basename and rejects empty or dot-prefixed IDs with HTTP 400. The fix will be included in the next MONAI Label release.

### Workarounds

Until you can upgrade:

- Enable authentication (`MONAI_LABEL_AUTH_ENABLE=True`) and do not grant the `ANNOTATOR` role to untrusted users.
- Do not expose the MONAI Label server to untrusted networks.
- Run the server as an unprivileged user with write access limited to the datastore directory.

### References

Originally reported by @aws-sec-vdp at https://github.com/Project-MONAI/MONAI/security/advisories/GHSA-cxx7-378q-5622

Solved here (#1915) and re-reported to generate CVE in the correct repository.

## Impact

The

`PUT /datastore/image`endpoint accepts a caller-controlled`image`query parameter that is used as the image ID without validation.`LocalDatastore.add_image()`appends the file extension to this ID, joins it onto the datastore image directory, and writes the uploaded file to the resulting path with`shutil.copy()`. Because the resolved path is never checked to be inside the datastore, a value such as`../../../tmp/x`writes the uploaded content to any location the MONAI Label process can write to.`LocalDatastore.save_label()`(`PUT /datastore/label`) builds its destination from the image ID and label tag in the same way.
An arbitrary file write can lead to remote code execution (for example by overwriting application code or adding entries to

`.ssh/authorized_keys`or cron), or to denial of service by overwriting configuration files.
Authentication is disabled by default (

`MONAI_LABEL_AUTH_ENABLE=False`), so in the default configuration any network client that can reach the server can exploit this. With authentication enabled, the`ANNOTATOR`role is sufficient.
This issue was originally reported privately against the MONAI repository (GHSA-cxx7-378q-5622) and is tracked here because the affected code is in MONAI Label.

## Patches

Fixed in #1915. Both

`add_image()`and`save_label()`now resolve the destination (including the label tag directory) and reject any path outside the datastore image/labels directories. The`/datastore/image`endpoint also reduces the image ID to its basename and rejects empty or dot-prefixed IDs with HTTP 400. The fix will be included in the next MONAI Label release.
## Workarounds

Until you can upgrade:

`MONAI_LABEL_AUTH_ENABLE=True`) and do not grant the`ANNOTATOR`role to untrusted users.
## References
