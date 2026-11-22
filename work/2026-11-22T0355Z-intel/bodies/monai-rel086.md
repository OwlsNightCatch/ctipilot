---
title: Release MONAI Label 0.8.6 · Project-MONAI/MONAILabel
url: https://github.com/Project-MONAI/MONAILabel/releases/tag/0.8.6
hostname: github.com
description: This is a security release. All MONAI Label server deployments should upgrade. pip install -U monailabel==0.8.6 docker pull projectmonai/monailabel:0.8.6 Security Path traversal in datastore uploa...
sitename: GitHub
date: "2026-11-22"
categories: ['repository:351826770']
fingerprint: b9ba7c498e80fa91
---
## Repository navigation

**This is a security release. All MONAI Label server deployments should upgrade.**

```
pip install -U monailabel==0.8.6
docker pull projectmonai/monailabel:0.8.6
```
#### Security

- **Path traversal in datastore upload endpoints** ([CVE-2026-133968](https://www.cve.org/CVERecord?id=CVE-2026-133968), [GHSA-qc22-rmgc-vg94](https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94), critical). `PUT /datastore/image` and `PUT /datastore/label` built the destination path from the image ID and label tag without confining it to the datastore, so a caller could write files anywhere the server process can write. Affects all versions up to and including 0.8.5. Fixed in [#1915](https://github.com/Project-MONAI/MONAILabel/pull/1915).
- **Path traversal in session upload.** `PUT /session/?uncompress=true` extracted uploaded tar archives without checking member names, and session IDs were used as paths without validation. Affects all versions up to and including 0.8.5. Fixed in [#1942](https://github.com/Project-MONAI/MONAILabel/pull/1942).

Authentication is disabled by default (`MONAI_LABEL_AUTH_ENABLE=False`), so both issues were reachable by any client that can connect to the server. Regardless of version:

- Do not expose the MONAI Label server to untrusted networks ([#1940](https://github.com/Project-MONAI/MONAILabel/pull/1940)).
- Enable authentication and grant roles only to trusted users.
- Run the server as an unprivileged user whose write access is limited to the datastore.

If a 0.8.5 or older server was reachable from an untrusted network, review it for unexpected file changes before returning it to service.

#### Added

- OHIF v3 plugin updated to OHIF 3.11; the pip package and Docker image bundle OHIF v3.11.0 ([#1855](https://github.com/Project-MONAI/MONAILabel/pull/1855), [#1942](https://github.com/Project-MONAI/MONAILabel/pull/1942))
- 3D Slicer: option to include the DICOM files in the data exchanged with the server ([#1664](https://github.com/Project-MONAI/MONAILabel/pull/1664))
- Transform to apply the image orientation to click guidance ([#1853](https://github.com/Project-MONAI/MONAILabel/pull/1853))
- CVAT: `cvat_labels_file` option for CSV label definitions with attributes ([#1824](https://github.com/Project-MONAI/MONAILabel/pull/1824))
- XNAT: requests are sent with the configured credentials ([#1838](https://github.com/Project-MONAI/MONAILabel/pull/1838))

#### Changed

- DICOM SEG export uses highdicom instead of pydicom-seg; pydicom upgraded to 3.x ([#1854](https://github.com/Project-MONAI/MONAILabel/pull/1854), [#1879](https://github.com/Project-MONAI/MONAILabel/pull/1879))
- `numpymaxflow` (scribbles / GraphCut) is an optional dependency: `pip install monailabel[scribbles]` ([#1912](https://github.com/Project-MONAI/MONAILabel/pull/1912))
- Docker image is based on Ubuntu 24.04 with Python 3.12; `python` and `monailabel` are provided by `/opt/venv` ([#1942](https://github.com/Project-MONAI/MONAILabel/pull/1942))
- Rejected, corrupt or unsupported session archives return HTTP 400; tar archives containing links or device files are rejected ([#1942](https://github.com/Project-MONAI/MONAILabel/pull/1942))
- Dependency updates, including fixes for open Dependabot alerts ([#1926](https://github.com/Project-MONAI/MONAILabel/pull/1926), [#1941](https://github.com/Project-MONAI/MONAILabel/pull/1941))

#### Fixed

- CVAT: annotation download and task status with the current CVAT API ([#1795](https://github.com/Project-MONAI/MONAILabel/pull/1795), [#1806](https://github.com/Project-MONAI/MONAILabel/pull/1806), [#1832](https://github.com/Project-MONAI/MONAILabel/pull/1832))
- 3D Slicer: connecting to a server given as `IP:PORT` without a protocol ([#1808](https://github.com/Project-MONAI/MONAILabel/pull/1808)); segmentation stays visible in 3D with `sam_3d` ([#1789](https://github.com/Project-MONAI/MONAILabel/pull/1789))
- `monailabel datasets --download` hash check and NIfTI writing with MONAI 1.6 ([#1915](https://github.com/Project-MONAI/MONAILabel/pull/1915))
- The pip package installs correctly with `uv` ([#1943](https://github.com/Project-MONAI/MONAILabel/pull/1943))

#### Removed

- Python 3.9 and 3.10 support. MONAI Label 0.8.6 requires Python 3.11 or newer ([#1941](https://github.com/Project-MONAI/MONAILabel/pull/1941))

**Full Changelog**: `0.8.5...0.8.6`
