---
schema: 1
kind: threat
horizon: operational
title: "CHAINDROP reads OIDC tokens out of GitHub Actions runner memory — and its opensearch-js path would have shipped a backdoored package carrying genuine, valid npm provenance"
headline: "Unit 42 finds the npm worm scraping runner process memory for OIDC tokens and building real Sigstore attestations over a backdoored tarball"
summary: >
  Unit 42's analysis of CHAINDROP, the Shai-Hulud npm worm wave covered here on 2026-08-06, adds two
  mechanics that break controls defenders currently rely on. An embedded Python helper opens
  /proc/<pid>/maps and /proc/<pid>/mem on the GitHub Actions Runner.Worker process and searches live memory
  for OIDC tokens and runner secrets, so scanning files and environment variables at rest does not see it.
  A second, single-target path trades a runner OIDC token at npm's trusted-publishing endpoint for a real
  publish credential, injects a typosquatted dependency without touching install scripts, and then signs the
  result through Fulcio and Rekor — producing provenance Unit 42 is explicit is not forged.
discovered_at: "2026-08-08T04:53:00Z"
event_date: "2026-08-06"
run_id: 2026-08-08T0409Z-intel
priority: high
immediate_action: null
tags: [supply-chain, infostealer, cloud]
regions: [global]
sectors: [technology, public-sector, finance, telco]
entities: [campaign:shai-hulud-chaindrop-2026-08]
techniques: [T1195.001, T1552, T1528, T1102.001, T1027]
affected_products: ["npm", "GitHub Actions"]
cves: []
sources:
  - url: "https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/"
    publisher: "Palo Alto Networks Unit 42"
    date: "2026-08-06"
    role: primary
closed_sources: []
evidence:
  - quote: "locates the Runner.Worker process on GitHub Actions runners, opens /proc/<pid>/maps and /proc/<pid>/mem, and searches live process memory for OpenID Connect (OIDC) tokens and runner secrets."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "This is not forged provenance. The attestation says the tarball was built in that repository by that workflow, and that is true."
    publisher: "Palo Alto Networks Unit 42"
  - quote: "Pivot on the Rekor log index and the workflow identity inside the certificate, not on whether the signature checks out."
    publisher: "Palo Alto Networks Unit 42"
verification: single-source
sourcing_note: "Unit 42's own reverse-engineering of the payload; the wave itself is separately corroborated by Elastic Security Labs in the 2026-08-06 entry this updates, but these specific mechanics rest on Unit 42 alone."
confidence: high
update_of: 2026-08-06/chaindrop-shai-hulud-npm-worm-onchain-c2-resolver
references: []
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Stop treating a valid npm provenance attestation as evidence a package is clean; where release pipelines gate on provenance, change the check to pin on the workflow identity inside the Fulcio certificate and the Rekor log index, which is what Unit 42 says still discriminates."
migrated_from: null
---

**UPDATE (originally covered 2026-08-06):** Unit 42 published its own analysis of the CHAINDROP wave on 2026-08-06, and two of its findings change what defenders can rely on rather than adding detail to what they already knew.

The first is credential theft that never touches disk. An embedded Python helper hidden inside an encrypted blob in the payload "locates the `Runner.Worker` process on GitHub Actions runners, opens `/proc/<pid>/maps` and `/proc/<pid>/mem`, and searches live process memory for OpenID Connect (OIDC) tokens and runner secrets" ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). Ephemeral OIDC tokens exist to avoid long-lived secrets sitting in a file or a variable; reading them out of the runner's address space while they are live defeats that design, and any secret-scanning control that inspects files or environment variables at rest sees nothing.

The second is a single-target path that is worse than a forgery. The worm checks three environment variables and only proceeds if it finds itself inside GitHub Actions, in a repository whose name contains `/opensearch-js`, in a workflow whose reference contains `release-drafter.yml`; anywhere else in that project it exits and steals nothing, staying silent in exactly the runs a maintainer is most likely to be reading ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). In that path it asks the runner for an OIDC token scoped to `npm:registry.npmjs.org` and trades it at npm's own trusted-publishing exchange for a real publish credential — the repository's legitimate release identity becomes the attacker's. It then downloads the latest tarball, bumps the patch version and adds a single dependency line typosquatting the project's own scope, never touching install scripts at all, so detections built around preinstall hooks would miss it. Finally it requests a second OIDC token for Sigstore, obtains a Fulcio certificate, builds an in-toto SLSA v1 provenance statement over the tarball's SHA-512 hash, signs it and uploads the entry to the public Rekor transparency log ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)).

Unit 42 is explicit about what that means: "This is not forged provenance. The attestation says the tarball was built in that repository by that workflow, and that is true." Its guidance follows directly — a package having valid npm provenance does not mean the package is clean, only that the tarball came out of the workflow named in the certificate, and if that workflow is running attacker code then valid provenance is what you should expect to see. "Pivot on the Rekor log index and the workflow identity inside the certificate, not on whether the signature checks out" ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)).

Unit 42 states it did not observe this path execute and that it cannot execute anywhere except in that one workflow in that one repository, but that it is fully implemented and reachable from the payload's main entry point ([Unit 42, 2026-08-06](https://unit42.paloaltonetworks.com/chaindrop-npm-worm-analysis/)). The worm also runs a locale gate before any collection, exiting cleanly on a Russian-language host.

**Defender takeaway:** provenance attestation has been the reassuring answer to "how do we know this build is what it claims to be", and it still answers that question correctly — it just turns out that was never the question worth asking once the workflow itself is hostile. **Triage:** on self-hosted runners, a process opening `/proc/<pid>/mem` of the runner worker is not something any legitimate build step does, and it is the cleanest available discriminator; debuggers and profilers that legitimately read process memory are not part of a normal publish workflow and do not target the runner agent itself.
