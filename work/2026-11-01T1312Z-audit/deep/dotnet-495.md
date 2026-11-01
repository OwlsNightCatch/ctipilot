# extract: served via trafilatura-direct
---
title: "Microsoft Security Advisory CVE-2026-114148 | .NET Elevation of Privilege Vulnerability · Issue #495 · dotnet/announcements"
author: Bribrothers
url: https://github.com/dotnet/announcements/issues/495
hostname: github.com
description: Executive summary Microsoft is releasing this security advisory to provide information about a vulnerability in file ownership in Linux .NET tarball distributions, including ASP.NET Core runtime ta...
sitename: GitHub
date: "2026-10-25"
categories: ['issue:6028168078']
fingerprint: ad0a28168f770441
---
## Repository navigation

# Microsoft Security Advisory CVE-2026-114148 | .NET Elevation of Privilege Vulnerability #495

## Description

## Executive summary

Microsoft is releasing this security advisory to provide information about a vulnerability in file ownership in Linux .NET tarball distributions, including ASP.NET Core runtime tarballs, ASP.NET Core targeting-pack tarballs, and source-built .NET tarballs. This advisory also provides guidance on updating affected installations and source-build engineering workflows.

Incorrect ownership of runtime files installed from affected Linux tarballs can allow local elevation of privilege.

## Discussion

Discussion for this issue can be found at [dotnet/aspnetcore#70040](https://github.com/dotnet/aspnetcore/discussions/70040)

## CVSS Details

- **Version:** 3.1
- **Severity:** High
- **Score:** 7.8
- **Vector:** `CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H/E:U/RL:O/RC:C`
- **Weakness:** CWE-276 (Incorrect Default Permissions)

## Affected Platforms

- **Platforms:** Linux
- **Architectures:** ARM, ARM64 and x64, as applicable to the affected Linux distribution.

## Affected Products

The affected ASP.NET Core runtime, ASP.NET Core targeting-pack, and source-built .NET Linux tarballs are listed below. The installation and source-build engineering scenarios require different remediation, as described in [How do I fix the issue?](https://github.com#how-fix).

### Microsoft-published ASP.NET Core archives

For Microsoft-published .NET 8 and .NET 9 distributions, only the ASP.NET Core runtime and targeting-pack tarballs are affected. Other Microsoft-published .NET runtime and SDK tarballs are not included in this scope.

| Product | Affected version | Patched version | 
|---|---|---|
| ASP.NET Core 8 regular and composite Linux runtime tarballs | >= 8.0.0, \< 8.0.33 | 8.0.33 | 
| ASP.NET Core 8 Linux targeting-pack tarballs | >= 8.0.0, \< 8.0.33 | 8.0.33 | 
| ASP.NET Core 9 regular and composite Linux runtime tarballs | >= 9.0.0, \< 9.0.22 | 9.0.22 | 
| ASP.NET Core 9 Linux targeting-pack tarballs | >= 9.0.0, \< 9.0.22 | 9.0.22 | 

These products use the archive names `aspnetcore-runtime-{version}-{rid}.tar.gz`, `aspnetcore-runtime-composite-{version}-{rid}.tar.gz`, and `aspnetcore-targeting-pack-{version}-{rid}.tar.gz`, where `{rid}` is `linux-arm`, `linux-arm64`, `linux-x64`, `linux-musl-arm`, `linux-musl-arm64` or `linux-musl-x64`. Runtime tarballs are listed on the [.NET download site](https://dotnet.microsoft.com/download/dotnet); targeting-pack tarballs are distributed through the .NET download CDN.

### Source-built distributions

Every tarball type produced by source-build is affected in the ranges below, not only SDK tarballs. The versions in this table identify the corresponding source-build SDK release.

Source-built tarballs are used in build and engineering workflows, rather than deployed directly to customer installations. Consuming an affected source-build archive does not, by itself, mean that a production shared runtime was installed from that archive.

| Product | Affected version | Patched version | 
|---|---|---|
| Source-built .NET 8 Linux distributions | >= 8.0.100, \< 8.0.133 | 8.0.133 | 
| Source-built .NET 9 Linux distributions | >= 9.0.100, \< 9.0.123 | 9.0.123 | 
| Source-built .NET 10.0.1xx Linux distributions | >= 10.0.100, \<= 10.0.113 | 10.0.114-servicing.26522.126 | 
| Source-built .NET 10.0.4xx Linux distributions | >= 10.0.400, \<= 10.0.402 | 10.0.403-servicing.26523.112 | 
| Source-built .NET 11 preview Linux distributions | >= 11.0.100-preview.1.26104.118, \<= 11.0.100-rc.2.26504.105 | 11.0.100-rc.3.26522.148 | 

## Advisory FAQ

### 

Review whether an installation came from an affected ASP.NET Core runtime or targeting-pack tarball, or whether a build or engineering workflow consumes an affected source-built archive. Check whether extraction preserved numeric ownership and whether the resulting files have the intended ownership. A .NET version number alone does not identify which archive was used or establish the ownership of an installation or build workspace.

The vulnerability can affect installations that preserve numeric file ownership from an affected archive, for example during privileged extraction or ownership-preserving container archive import. A local account that controls the installed files or writable directories may be able to modify files used by a more privileged application.

Restoring ASP.NET Core runtime or targeting-pack NuGet packages does not, by itself, introduce this tarball ownership defect. Applications using a shared runtime installed from an affected tarball can still be affected.

### 

#### Customer-deployed installations

For an installation made from an affected ASP.NET Core runtime or targeting-pack tarball, replace the affected installation with a clean installation from the patched distribution listed in [Affected Products](https://github.com#affected-products). Updating a NuGet reference, downloading a new archive, or extracting over an existing installation does not by itself correct the existing installation.

1. Identify the affected installation directories and the applications, services, scheduled jobs, and container images that use them. Stop affected applications and services before switching installations.
2. Obtain the patched archives appropriate to your distribution, architecture, and required components from the trusted publisher. Verify their checksums against the publisher's trusted release information before extracting them.
3. Install into a **new, empty directory**, not the affected installation tree. For a shared or privileged installation, use a trusted administrator account and an administrator-controlled directory whose parent directories cannot be modified by untrusted accounts. Do not copy binaries, plugins, or other files from the affected tree into the replacement. Install any required side-by-side versions from trusted, fixed distributions.
4. Extract without restoring the archive's user/group ownership. Follow the [manual installation guidance](https://learn.microsoft.com/dotnet/core/install/linux-scripted-manual#manual-install), which uses `--no-same-owner`. For GNU tar, the following example also applies a restrictive write-permission mask:
```
(
    umask 022
    tar -xzf "$PATCHED_ARCHIVE" -C "$NEW_DOTNET_ROOT" \
        --no-same-owner --no-same-permissions
)
```
`PATCHED_ARCHIVE` must identify the verified patched archive, and `NEW_DOTNET_ROOT` must identify the new, empty installation directory. For a shared or privileged installation, run extraction in the trusted administrator context. Confirm that the resulting files, directories, and parent directories are controlled by the intended trusted owner and cannot be modified by untrusted accounts, including through group permissions or access-control lists.
5. Update application and service configuration to use the replacement installation, then restart and verify the applications. Check the actual runtime selected by each application, not only the version reported by an unrelated `dotnet` executable on `PATH`. Ensure that no service, scheduled job, or runtime search path still selects the affected installation. Retire the old tree using your deployment procedures, preserving evidence first if compromise is suspected.
6. Rebuild affected custom container images from trusted inputs using the patched archives and ownership-controlled extraction, and deploy replacement containers. Changing only a running container does not correct the image used to create subsequent containers.

#### Source-build engineering workflows

If a build or engineering workflow consumes an affected source-built tarball, update that input to the patched source-build release listed in [Affected Products](https://github.com#affected-products). Recreate its extracted workspace in a new, trusted directory using ownership-controlled extraction, rather than reusing a tree extracted from the affected archive. The extraction guidance above also applies to these workspaces.

Review downstream runtime or SDK packages and custom images for ownership inherited from the affected archive, and rebuild affected outputs as needed. The customer-installation steps above apply if affected outputs were actually installed or deployed; do not treat the source-build engineering archive itself as a deployed production runtime.

## Other Information

### Reporting Security Issues

If you have found a potential security issue in a supported version of .NET, please report it to the Microsoft Security Response Center (MSRC) via the [MSRC Researcher Portal](https://msrc.microsoft.com/report/vulnerability/new). Further information can be found in the MSRC [Report an Issue FAQ](https://www.microsoft.com/msrc/faqs-report-an-issue).

Security reports made through MSRC may qualify for the Microsoft .NET Bounty. Details of the Microsoft .NET Bounty Program including terms and conditions are at [https://aka.ms/corebounty](https://aka.ms/corebounty).

### Support

You can ask questions about this issue on GitHub in the .NET GitHub organization. The main repos are located at [https://github.com/dotnet/aspnetcore](https://github.com/dotnet/aspnetcore). The Announcements repo ([https://github.com/dotnet/Announcements](https://github.com/dotnet/Announcements)) will contain this bulletin as an issue and will include a link to a discussion issue. You can ask questions in the linked discussion issue.

### Disclaimer

The information provided in this advisory is provided "as is" without warranty of any kind. Microsoft disclaims all warranties, either express or implied, including the warranties of merchantability and fitness for a particular purpose. In no event shall Microsoft Corporation or its suppliers be liable for any damages whatsoever including direct, indirect, incidental, consequential, loss of business profits or special damages, even if Microsoft Corporation or its suppliers have been advised of the possibility of such damages. Some states do not allow the exclusion or limitation of liability for consequential or incidental damages so the foregoing limitation may not apply.

### External Links

### Acknowledgements

- Alen Cheung

### Revisions

V1.0 (10/25/2026): Initial advisory.

## Activity

1. locked and limited conversation to collaboratorson Oct 25, 2026

to join this conversation on GitHub.Already have an account? Sign in to comment
