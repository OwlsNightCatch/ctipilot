---
schema: 1
kind: threat
title: "PolinRider: a North Korea-linked loader reaches developers through force-pushed forged commits in at least 7,609 GitHub repositories, hijacked npm releases and a fake employer's take-home test, and reads its server address from an Ethereum wallet"
headline: "PolinRider: forged backdated commits, npm hijacks and a fake recruiter run a loader at build or folder open"
summary: >
  Apiiro found the PolinRider loader in at least 7,609 GitHub repositories owned by 2,330 accounts, where stolen GitHub access force-pushes a copy of the owner's own commit, with the same author, message and date, plus a loader hidden after hundreds of spaces in a build configuration file. Sonatype found the same loader in 12 hijacked npm releases and JFrog in a fake employer's take-home test and scripted camera check; none relies on an npm install script, the server address is read from an Ethereum wallet, and removing the code does not revoke the access that pushed it.
discovered_at: "2026-11-15T04:26:40Z"
updated_at: null
event_date: "2026-11-09"
run_id: 2026-11-15T0356Z-intel
priority: notable
immediate_action: null
tags: [supply-chain, nation-state, north-korea-nexus, identity]
regions: [global]
sectors: [technology]
entities: ["campaign:polinrider"]
techniques: [T1195.002, T1078, T1566.003, T1585.001, T1583.001, T1204.002, T1059.007, T1102.001, T1105, T1027, T1036, T1071.001]
affected_products: ["GitHub", "npm", "Microsoft Visual Studio Code"]
cves: []
sources:
  - url: "https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits"
    publisher: "Apiiro"
    date: "2026-11-09"
    role: primary
  - url: "https://research.jfrog.com/post/accurasofthire-fake-interview/"
    publisher: "JFrog Security Research"
    date: "2026-11-09"
    role: primary
  - url: "https://www.sonatype.com/blog/polinrider-loader-reappears-in-hijacked-npm-packages"
    publisher: "Sonatype Research"
    date: "2026-11-04"
    role: corroborating
  - url: "https://www.stepsecurity.io/blog/accurasofthire-fake-interview-developer-machines"
    publisher: "StepSecurity"
    date: "2026-11-13"
    role: corroborating
closed_sources: []
evidence:
  - quote: "Apiiro research found the worm, PolinRider, in at least 7,609 GitHub repos owned by 2,330 accounts."
    publisher: "Apiiro"
    source_url: "https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits"
  - quote: "Cloning runs nothing."
    publisher: "Apiiro"
    source_url: "https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits"
  - quote: "Disabling npm install scripts does not address code that runs during module loading or application startup."
    publisher: "Sonatype Research"
    source_url: "https://www.sonatype.com/blog/polinrider-loader-reappears-in-hijacked-npm-packages"
  - quote: "We have found no link between AccuraSoftHire and that intrusion."
    publisher: "JFrog Security Research"
    source_url: "https://research.jfrog.com/post/accurasofthire-fake-interview/"
verification: multi-source
sourcing_note: >
  Apiiro's census, Sonatype's analysis of hijacked npm releases and JFrog's trace of the fake employer are three separate observations of one loader family; the repository counts are Apiiro's alone and Apiiro calls them lower bounds. The North Korea link is the researchers' assessment, based on the fake-interview playbook and shared loader markers, not an authority's attribution, and JFrog found no link between its fake employer and the Binance intrusion it opens with.
confidence: high
references: ["2026-10-10/ghostaction-fake-audit-workflow-git-history-credential-theft"]
deep_dive: false
deep_dive_category: null
org_triage: null
classification:
  reliability: B
  credibility: 2
watchlist_hit: false
actions:
  - "Search every branch of your organisation's and suppliers' GitHub repositories for a semicolon followed by 200 or more spaces in JavaScript, TypeScript and build configuration files, and for .vscode/tasks.json tasks that run node when a folder opens; on any hit, rotate every GitHub and npm token reachable from the developer machines and CI runners that built the repository and review force-pushes, deploy keys, Actions secrets and releases since the infection, because deleting the loader does not revoke the access that pushed it."
updates: []
migrated_from: null
---

Apiiro calls PolinRider a North Korea-linked worm and found it in at least 7,609 GitHub repositories owned by 2,330 accounts, mostly developers' own ([Apiiro, 2026-11-09](https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits)). Three routes, none relying on an npm install script. Forged commits: with stolen GitHub access the worm force-pushes a copy of a commit the owner already made, with the same author, message and date, plus a loader hidden after hundreds of spaces in a build configuration file; in 94% of 9,990 injection pushes the copy claims to be more than an hour older than the push, so `git log` shows an old commit under the owner's name. Cloning runs nothing; building the project or running its dev, build or lint scripts loads the file, and in the newest wave opening the folder in VS Code is enough ([Apiiro, 2026-11-09](https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits)). Hijacked npm releases: Sonatype found concealed loaders in 12 releases across 10 hijacked packages with no install or postinstall hook, so disabling install scripts does not help ([Sonatype, 2026-11-04](https://www.sonatype.com/blog/polinrider-loader-reappears-in-hijacked-npm-packages)). A fake employer: JFrog traced AccuraSoftHire, a decoy recruiter with ID-verified LinkedIn recruiters and job ads, whose take-home loads a look-alike npm package and whose scripted camera check fails and hands the candidate a command that installs the same loader ([JFrog, 2026-11-09](https://research.jfrog.com/post/accurasofthire-fake-interview/)); StepSecurity says taking its site down, as had happened by 2026-11-13, does not end the operation ([StepSecurity, 2026-11-13](https://www.stepsecurity.io/blog/accurasofthire-fake-interview-developer-machines)).

The loader reads the latest outbound transaction of a hard-coded Ethereum wallet and decodes two IPv4 addresses from its recipient field ([Apiiro, 2026-11-09](https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits)), then fetches XOR-encoded JavaScript over plain HTTP on port 443, so blocking one server changes nothing; the wallet in the hijacked npm releases also appears in GitGuardian's GhostAction report, which Sonatype says does not establish a shared operator ([Sonatype, 2026-11-04](https://www.sonatype.com/blog/polinrider-loader-reappears-in-hijacked-npm-packages)). Cleanup does not hold: 1,949 repositories were infected again after being publicly listed, and where owners cleaned up the stolen access often still worked; Apiiro counts roughly 2,300 developers reached ([Apiiro, 2026-11-09](https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits)).

**Exposure:** any developer machine, CI runner or coding agent that builds or opens a checkout the worm reached, installs one of the hijacked npm packages, or runs a take-home from an unverified recruiter. Apiiro's checks are a semicolon followed by 200 or more spaces on any branch, a `.vscode/tasks.json` task with `runOn` set to `folderOpen` that runs node, and force-pushes in the GitHub Activity view whose commit is dated days before the push ([Apiiro, 2026-11-09](https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits)).

**Detection:** in process telemetry, a detached node child with no console started from a build script, editor or package entrypoint; in egress telemetry, build hosts and CI runners resolving public blockchain RPC endpoints and then making plain HTTP requests on port 443 to a bare IP address; in GitHub audit telemetry, force-pushes whose replacement commit repeats the replaced commit's author and message ([Apiiro, 2026-11-09](https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits); [Sonatype, 2026-11-04](https://www.sonatype.com/blog/polinrider-loader-reappears-in-hijacked-npm-packages)).

**Triage:** blockchain developers legitimately call public RPC endpoints; the discriminator is a build or lint process in a project with no Web3 purpose doing so and then spawning a detached node child ([Apiiro, 2026-11-09](https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits)).

**Defender takeaway:** treat a machine or runner that built an infected checkout as compromised and rotate what it could reach, because the stolen access, not the file, reinfects; run take-home tests from unknown recruiters only in a throwaway virtual machine with no tokens or keys, and block public blockchain RPC from CI runners ([Apiiro, 2026-11-09](https://apiiro.com/blog/polinrider-north-korea-worm-forged-github-commits); [JFrog, 2026-11-09](https://research.jfrog.com/post/accurasofthire-fake-interview/)).
