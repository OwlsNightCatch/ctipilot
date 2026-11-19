---
title: Release and support
url: https://docs.airlock.com/gateway/latest/index/1755485389142.html
hostname: airlock.com
sitename: docs.airlock.com
date: "2024-10-01"
fingerprint: fe3189438d90f7c8
---
# Release and support

## Release lifecycles

Maintenance releases and hotfixes for minor versions will be served for one year after the publication of the next release.

## End-of-support dates (EOS)

Supported releases are covered by the [Airlock support process](https://techzone.ergon.ch/node/1717). That is, customers and partners may open support cases for these versions, and our support team will investigate these issues.

**Support lifecycle for Airlock Gateway minor releases**

| Minor version | Published | End-of-support date | 
|---|---|---|
| 8.6 | 06/2026 | \<one year after the publication of 9.0> | 
| 8.5 | 11/2025 | 06/2027 | 
| 8.4 | 05/2025 | 08/2026<sup>1)</sup> | 
| **No longer supported:** 8.3 | 10/2024 | 05/2026 | 

- <sup>1)</sup>
- Airlock Gateway 8.5 introduces **OpenSSL version 3.5**. Since the current version 3.0.x will only be supported by the OpenSSL project until **August 2026**, the support lifecycle for Gateway 8.4 has been slightly shortened to align with this timeline.

## Supported versions for configuration import

When importing a configuration, Airlock Gateway automatically converts it to the version of the configuration schema used by the current release. Older configurations are supported only for defined earlier releases.

**Range of supported earlier releases**

A release can import configurations that are at most two minor versions older than the oldest still supported version.

Example: Airlock Gateway 8.6.0 still supports version 8.4.x as the oldest supported minor version. Therefore, configurations from version 8.2.x and later can be imported. Configurations from version 8.1.x and earlier cannot be imported.

## Extended support

Ergon offers the possibility to extend the support services beyond the end-of-support date. Airlock Gateway can be extended by a maximum of 6 months. This service is subject to an additional charge. To request a proposal for extended support please contact: [order@airlock.com](mailto:order@airlock.com)

## Update types

To deliver new features, improvements, and security fixes for Airlock Gateway, Ergon provides the following four update types:

- **Major release update**
- Major release updates introduce significant enhancements or architectural changes. Upgrading from any previous release to a new major release requires a **new installation**.
- **Minor release update**
- Minor release updates deliver new features, improvements, and regular bug fixes. Updates from any previous minor release (X.Y) to the subsequent minor release (X.Y+1) are supported. Minor release updates **cannot be uninstalled**. Downgrading to an earlier version requires **reinstallation**.
- **Maintenance update**
- Maintenance updates address stability issues between releases. Maintenance versions will be provided approximately every 3 months for all supported versions. Maintenance updates **cannot be uninstalled**. Downgrading to an earlier version requires **reinstallation**.
- **Hotfix**
- Hotfixes address security issues between releases. Hotfixes will be provided for *exploitable vulnerabilities* for the most recent maintenance releases of supported minor versions. Hotfixes **can be uninstalled** (e.g., from X.Y-HF001 to X.Y).

- Updates can only be installed if they are newer than the currently installed version.
- Compatibility restrictions may apply between specific versions — always review the release notes of your target version before updating.

## Release artifacts

We might provide additional artifacts that can be used with Airlock Gateway. This may comprise documentation, examples, tutorials, etc. Generally, these artifacts are only maintained for the most recent version. Nevertheless, it is at Ergon's discretion to decide which artifacts are also maintained for older versions.

## Airlock semantic versioning

Airlock Gateway versions are expressed as *x.y.z*:

- **x** is the major version.
- **y** is the minor version.
- **z** is the patch version.

This scheme follows the [Airlock semantic versioning](https://semver.org) terminology.

Semantic versioning requires a release to be major whenever it contains breaking changes. We adhere to the following definitions:

- **Breaking change** 
- The term *breaking change* typically refers to a change that falls into one or more of the following categories:
  - Invasive change, potentially requiring manual configuration adjustment (e.g., new regex engine, removal of a deprecated feature)
  - Change in the config REST API with expected high impact on customers
  - Non-backward compatible change in the control API.
  - Change that requires a full reinstallation (e.g., major OS update)
- **Non-breaking change**
- The term *non-breaking change* typically refers to a change that falls into one or more of the following categories:
  - Change in a non-published feature or feature marked as incubating
  - Change due an improved rule or parser that requires only a non-invasive adjustment
  - Change in log structure or metrics, as we provide built-in dashboards
