---
schema: 1
kind: incident
title: "OVHcloud CLI: release binaries of already-published versions were replaced on 2026-10-19 with a build that steals secrets from disk, uploaded through a developer's GitHub account"
headline: "OVHcloud CLI release binaries carried a secret-stealing build for about 90 minutes; a pinned hash caught it"
summary: >
  OVHcloud says a hacker used a developer's GitHub account to replace the release binaries of its command-line tool for
  versions v0.11.0 to v0.15.0 on 2026-10-19 with a build that steals secrets from disk, available for 1h33 and downloaded about
  250 times; the first replacement was at about 12:47 UTC and OVHcloud deleted the files at 14:21 UTC after a customer's pinned
  SHA-256 failed. Its postmortem traces the account compromise to a poisoned editor extension installed on the developer's personal
  MacBook on 2025-10-20, ties it to the GlassWorm actor through a Solana wallet, and names a missing release-immutability setting as
  the main issue. Anyone who installed or updated the tool from a release asset in that window must rotate every secret on that
  host; the source tag and the Go module were untouched.
discovered_at: "2026-10-20T03:36:20Z"
updated_at: "2026-10-22T03:47:17Z"
event_date: "2026-10-19"
run_id: 2026-10-20T0256Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, cloud]
regions: [global]
sectors: [technology]
entities: ["incident:ovhcloud-cli-release-asset-compromise-2026-10"]
techniques: [T1195.002, T1176.002, T1078.004, T1552.001, T1552.004, T1005, T1041]
affected_products: ["OVHcloud CLI"]
cves: []
sources:
  - url: "https://github.com/ovh/ovhcloud-cli/issues/300"
    publisher: "GitHub issue ovh/ovhcloud-cli #300 (external reporter, with OVHcloud maintainer replies)"
    date: "2026-10-19"
    role: primary
  - url: "https://x.com/olesovhcom/status/2112225308589834260"
    publisher: "Octave Klaba, OVHcloud founder (post on X)"
    date: "2026-10-19"
    role: primary
  - url: "https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool"
    publisher: "OpenSourceMalware"
    date: "2026-10-19"
    role: corroborating
  - url: "https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw"
    publisher: "OVHcloud (security advisory and postmortem)"
    date: "2026-10-20"
    role: primary
closed_sources: []
evidence:
  - quote: "The release assets of v0.13.0, v0.14.0 and v0.15.0 were replaced today"
    publisher: "GitHub issue ovh/ovhcloud-cli #300 (external reporter, with OVHcloud maintainer replies)"
    source_url: "https://github.com/ovh/ovhcloud-cli/issues/300"
  - quote: "All binaries involved have been deleted at 16:21 GMT+2."
    publisher: "GitHub issue ovh/ovhcloud-cli #300 (external reporter, with OVHcloud maintainer replies)"
    source_url: "https://github.com/ovh/ovhcloud-cli/issues/300"
  - quote: "This release is immutable, so the assets attached to it can be trusted."
    publisher: "GitHub issue ovh/ovhcloud-cli #300 (external reporter, with OVHcloud maintainer replies)"
    source_url: "https://github.com/ovh/ovhcloud-cli/issues/300"
  - quote: "The compromised versions are v0.11.0, v0.12.0, v0.13.0, v0.14.0 and v0.15.0. (translated from French)"
    original: "La version compromise est v0.11.0 v0.12.0 v0.13.0 v0.14.0 v0.15.0."
    publisher: "Octave Klaba, OVHcloud founder (post on X)"
    source_url: "https://x.com/olesovhcom/status/2112225308589834260"
  - quote: "The hacker used the GitHub account of one of the developers and added a binary whose job is to retrieve the secrets on the disk. (translated from French)"
    original: "Le hacker a utilisé le compte github d'un des développeurs et a ajouté un binaire dont le job est récupérer les secrets sur le disque."
    publisher: "Octave Klaba, OVHcloud founder (post on X)"
    source_url: "https://x.com/olesovhcom/status/2112225308589834260"
  - quote: "If you are concerned, please change all the secrets on your disk. (translated from French)"
    original: "Si vous êtes concernés, merci de changer tous les secrets sur votre disque."
    publisher: "Octave Klaba, OVHcloud founder (post on X)"
    source_url: "https://x.com/olesovhcom/status/2112225308589834260"
  - quote: "No tag was pushed and no GitHub Actions workflow ran."
    publisher: "OpenSourceMalware"
    source_url: "https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool"
  - quote: "Whether the same actor did both is our inference"
    publisher: "OpenSourceMalware"
    source_url: "https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool"
  - quote: "OVHcloud deleted the replaced binaries before anyone archived them, so we have not analyzed the payload"
    publisher: "OpenSourceMalware"
    source_url: "https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool"
  - quote: "The compromission took place months before when the developer installed the extension"
    publisher: "OVHcloud (security advisory and postmortem)"
    source_url: "https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw"
  - quote: "The main issue was that the GitHub repository was not appropriately configured to ensure release immutability."
    publisher: "OVHcloud (security advisory and postmortem)"
    source_url: "https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw"
  - quote: "Duration of malware availability: 1h33"
    publisher: "OVHcloud (security advisory and postmortem)"
    source_url: "https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw"
verification: multi-source
sourcing_note: >
  The replacement is shown by an external reporter's capture on GitHub, by OVHcloud's advisory and maintainer replies and by its
  founder's statement on X, and OpenSourceMalware's reconstruction from GitHub's server-side data agrees with it; the payload
  description and the root cause are OVHcloud's alone, since the replaced files were deleted before anyone archived them and
  OpenSourceMalware has not analysed the payload. The reporter checked v0.13.0 to v0.15.0 and OVHcloud lists v0.11.0 to v0.15.0,
  which OpenSourceMalware reads as the same pass. The GlassWorm link rests on a Solana wallet that OVHcloud and OpenSourceMalware
  tie to the actor, and OVHcloud names no actor beyond that.
confidence: high
references:
  - "2026-05-28/crowdstrike-google-and-shadowserver-simultaneously-sever-all"
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: A
  credibility: 2
watchlist_hit: false
actions:
  - "Find every workstation, build agent and container image build that installed or updated the OVHcloud CLI from a release asset (install script, Homebrew cask, direct download or a CI step fetching the release tarball) between 12:47 and 14:21 UTC on 2026-10-19, and rotate every secret readable on each of those hosts before installing v0.16.0 or later."
updates:
  - at: "2026-10-22T03:47:17Z"
    run_id: 2026-10-22T0256Z-intel
    type: update
    summary: >
      OVHcloud's postmortem traces the account compromise to a poisoned editor extension installed on a
      developer's personal MacBook on 2025-10-20, ties it to the GlassWorm actor through a Solana wallet,
      describes a stealer that reads AI-agent data stores and cloud and developer credentials and
      exfiltrates through Solana RPC calls, and names a missing release-immutability setting as the main
      issue; the malicious assets were online for 1h33 and downloaded about 250 times.
    fields: [body, evidence, sources, sourcing_note, summary, techniques]
migrated_from: null
---

OVHcloud's founder says a hacker used the GitHub account of one of its developers to add to the official command-line tool's releases a binary whose job is to retrieve secrets from the disk, that versions v0.11.0 to v0.15.0 are compromised, and that v0.10.0 and v0.16.0 are clean ([Octave Klaba, 2026-10-19](https://x.com/olesovhcom/status/2112225308589834260)). A user whose CI pins a SHA-256 reported on GitHub that the assets of v0.13.0 to v0.15.0 were replaced between about 12:47 and 13:12 UTC, weeks after publication, by an uploader who is not a public member of the ovh organisation, with a local build of a later commit that has uncommitted changes and no release version flag, while the v0.15.0 tag and the Go module proxy still point at the original commit ([GitHub issue #300, 2026-10-19](https://github.com/ovh/ovhcloud-cli/issues/300)). An OVHcloud maintainer replied that all the binaries involved were deleted at 16:21 (GMT+2) and that v0.16.0, with a signed tag, is an immutable release ([GitHub issue #300, 2026-10-19](https://github.com/ovh/ovhcloud-cli/issues/300)). OpenSourceMalware, working from GitHub's server-side records, says no tag was pushed and no release workflow ran, ties the same account's earlier force-pushes carrying a hidden loader (from 2026-03-05) to the GlassWorm campaign while saying that whether the same actor did both is its inference, notes that the project's release tooling replaces existing assets as normal behaviour, and says it has not analysed the payload because the files were deleted before anyone archived them ([OpenSourceMalware, 2026-10-19](https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool)). OVHcloud's advisory gives the root cause: the account belongs to a developer who installed the editor extension color-picker-universal 2.8.91 on a personal MacBook on 2025-10-20, and the releases were replaced with stolen keys, not from that laptop; the malicious assets were online for 1h33 and downloaded about 250 times ([OVHcloud, 2026-10-20](https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw)). Whether any secret was stolen is not public.

**Exposure:** OVHcloud says only users who installed or updated the tool between 14:47 and 16:21 (UTC+2) on 2026-10-19, which is 12:47 to 14:21 UTC, are affected, and that a v0.11.0 to v0.15.0 download from before that day is not ([OVHcloud, 2026-10-20](https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw)); OpenSourceMalware reads the channels as macOS, Linux (x86_64, arm64) or Windows (x86_64) through the install script, the Homebrew cask, a direct download of a v0.11.0 to v0.15.0 asset or a CI step that fetches the release tarball, and says go install, builds from source and the vendor's Docker image were not affected ([OpenSourceMalware, 2026-10-19](https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool)).

**Detection:** an archive whose SHA-256 differs from the original release's for an unchanged version number, which is how the reporter caught it; release-API records of weeks-old assets replaced by an uploader who is not the original publisher; and, on a retained binary, build metadata showing a modified working tree and no release version ([GitHub issue #300, 2026-10-19](https://github.com/ovh/ovhcloud-cli/issues/300)). OVHcloud says each run of the malicious binary leaves a working folder named envchecker followed by digits in the temporary directory and never deletes it, so its presence on a host that ran the tool shows exposure; the stealer reads the databases and histories of AI coding assistants and agents (VS Code, Cursor, Continue, Sourcegraph Cody, OpenCode, Hermes, Claude) as well as cloud, Kubernetes, Terraform, npm, SSH and Git credentials, and exfiltrates through Solana RPC calls and an upload endpoint ([OVHcloud, 2026-10-20](https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw)). Deleting the binary does not undo a run: OVHcloud says to change all the secrets on the disk ([Octave Klaba, 2026-10-19](https://x.com/olesovhcom/status/2112225308589834260)).

**Triage:** a replaced asset alone is not proof, since the project's release tooling replaces assets routinely; the discriminators are an uploader who is not the original publisher, a modified-tree build without the release version, and a digest that changed without a version bump ([OpenSourceMalware, 2026-10-19](https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool); [GitHub issue #300, 2026-10-19](https://github.com/ovh/ovhcloud-cli/issues/300)).

**Defender takeaway:** a host that installed or updated the tool from a release asset between 12:47 and 14:21 UTC on 2026-10-19, the window as OpenSourceMalware reads it ([OpenSourceMalware, 2026-10-19](https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool)), needs its secrets rotated, not just the binary removed ([Octave Klaba, 2026-10-19](https://x.com/olesovhcom/status/2112225308589834260)), and then v0.16.0 or later ([GitHub issue #300, 2026-10-19](https://github.com/ovh/ovhcloud-cli/issues/300)); pinning release digests or building from the source tag, as the reporter did, is the durable lever against a swapped asset on a mutable release.

## Update — 2026-10-22T03:47:17Z

OVHcloud published its advisory and postmortem. It says the compromised account belongs to a developer who installed the editor extension color-picker-universal 2.8.91 on a personal MacBook on 2025-10-20; the extension queries a Solana wallet that OVHcloud says belongs to the GlassWorm actor, a persistent Node.js service was registered on the laptop, and several personal repositories of the account were compromised in March 2026. The release replacement was made with stolen keys, not from that laptop, and OVHcloud says neither the developer's OVHcloud laptop nor its internal CI/CD was compromised as far as it knows ([OVHcloud, 2026-10-20](https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw)). OpenSourceMalware reads the same account as already compromised for seven months, which is its assessment, and says that the same actor made both steps is its inference ([OpenSourceMalware, 2026-10-19](https://opensourcemalware.com/blog/glassworm-hacks-ovh-clouds-cli-tool)).

OVHcloud describes the payload as the original CLI recompiled with embedded stealer code that copies a list of credential files and AI-agent data stores into a temporary folder named envchecker, archives them and exfiltrates through Solana RPC calls and an upload endpoint; the malicious assets were online for 1h33 and downloaded about 250 times ([OVHcloud, 2026-10-20](https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw)). It names the missing release-immutability setting as the main issue, says it allows developers to attach personal GitHub accounts to the organisation, and reports that it enabled immutable releases on every repository, suspended the account, reviewed write access and repository logs without finding another compromise, and published v0.16.0 with a signed tag as the clean release ([OVHcloud, 2026-10-20](https://github.com/ovh/ovhcloud-cli/security/advisories/GHSA-862f-55f5-vmvw)).
