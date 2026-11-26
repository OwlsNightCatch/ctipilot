---
title: PolinRider Malware Force-Pushed Into AsyncAPI, CircuitVerse and Open Food Facts Pull Requests
author: Owais Shaikh View LinkedIn November
url: https://www.stepsecurity.io/blog/polinrider-malware-open-source-pull-requests
hostname: stepsecurity.io
description: PolinRider malware was force-pushed into AsyncAPI, CircuitVerse and Open Food Facts pull requests and ran in CircuitVerse's release CI. How it works, IOCs, and how to check your projects.
sitename: stepsecurity.io
date: "2026-11-26"
fingerprint: "659431d156e487c1"
language: en
image: https://cdn.prod.website-files.com/673b71f0790aabf30bd30bf8/6b075bead7959b6bbc9f7a33_6b075b4115eed26b7de0812f_polinrider-pull-requests-cover-v4.png
pagetype: website
filedate: "2026-11-26"
---
On November 25, Lukasz Gornicki, a maintainer of AsyncAPI Generator, opened heads-up issues in eight open-source projects, including Meshery, Jitsi Meet, Jaeger, stdlib and PipeCD. The issues reported that the GitHub account `Eternity0207` had pushed an obfuscated malware loader into pull requests and that GitHub had suspended the account. GitHub removed every pull request the account had opened, merged ones included, without telling the projects why.

The account had opened 217 pull requests, and 145 of them were merged. None of the merged pull requests contains the loader: the AsyncAPI maintainer scanned all 145, and maintainers at Jitsi Meet and Floresta confirmed it in their own reviews. The loader arrived on October 19 in rewritten commits force-pushed into pull requests that were still open. At AsyncAPI, each malicious commit stayed on its branch for 30 to 40 minutes before another force-push replaced it, leaving a clean final diff.

We decoded the payload from all three projects. It is the PolinRider loader. PolinRider is a malware family that hides JavaScript in build configuration files and fake font files, steals credentials from developer machines, and uses them to push itself into more repositories. This loader reads its server address from Ethereum wallet `0x1eef0849eda15d87f64e51c73c8442cf3c8bcef3`, the wallet of the HuntRole fake recruiter that we tied to the [AccuraSoftHire fake interview campaign](https://www.stepsecurity.io/blog/accurasofthire-fake-interview-developer-machines). The wallet posted a server address again on November 25.

### At a glance

- **What happened:** on October 19, 2026, rewritten commits carrying a hidden malware loader were force-pushed from the `Eternity0207` account into open pull requests at AsyncAPI Generator, CircuitVerse and Open Food Facts. The commits are unsigned and use a different committer name than the account's usual signed commits.
- **Malware:** PolinRider. One 16,674-byte loader, hidden in `api.js`, appended to `jest.config.js` and `postcss.config.js`, and in a fake font file started by a hidden VS Code task.
- **Where it ran:** CircuitVerse's pull request workflows, including the release workflow that builds the desktop app for Windows, Linux and macOS. The maintainers confirmed the loader ran and deleted the 40 installers the workflow published. Open Food Facts' CI also ran on the poisoned commits. AsyncAPI's CI did not, because fork pull request workflows there need a maintainer's approval.
- **Merged:** none of the account's 145 merged pull requests contains the loader.
- **Server address:** read from Ethereum wallet `0x1eef…cef3`, which has named five servers since September 4. The current one is 95.135.181.84, last posted at 18:30 UTC on November 25.
- **Scale:** GitHub code search returns 2,776 `package.json` files with the same `node api.js &&` hook. 576 of the 622 repositories we checked carry the loader, across 311 accounts. The decoded copies read either this wallet or the AccuraSoftHire campaign's wallet.

## Timeline

| Date (UTC) | Event | 
|---|---|
| Sep 4, 2026 | Wallet `0x1eef…cef3` posts its first server address, 166.88.134.75 | 
| Oct 16 | The wallet switches to 95.135.181.151 | 
| Oct 19, 01:39 to 02:08 | Malicious commit `a891829` sits on AsyncAPI Generator pull request #2277. The same wave reaches CircuitVerse and Open Food Facts pull requests. | 
| Oct 19, 05:31 to 06:12 | Malicious commit `0e2d800` sits on AsyncAPI Generator pull request #2278. A second wave reaches CircuitVerse and Open Food Facts. | 
| Oct 19 | CircuitVerse's pull request workflows, including the desktop release build, run on the poisoned commits without approval. Open Food Facts' CI runs on them too. | 
| Nov 12 | The wallet switches to 95.135.181.84 | 
| Nov 24 | The AsyncAPI maintainer publishes a payload analysis | 
| Nov 25 | GitHub suspends the account and removes its pull requests. Heads-up issues go to eight projects. CircuitVerse confirms the loader ran in its CI and deletes 40 installers. Open Food Facts rotates a secret. | 
| Nov 25, 18:30 | The wallet posts 95.135.181.84 again | 

## How the Malware Got Into the Pull Requests

At AsyncAPI, each malicious commit reused the message and date of a clean, signed commit from the same pull request. All the malicious commits are unsigned and use a different committer name from the account's usual commits.

**Code pushed off-screen.** `api.js` is a single line: 315 tab characters, then the obfuscated loader. In GitHub's diff view the added line looks empty. An automated AI reviewer flagged it on the AsyncAPI pull request within four minutes. In `jest.config.js` and `postcss.config.js`, the loader sits on the same line as the file's last statement, after the closing `};` and roughly 300 more tabs.

**Build scripts that run it first.** The `build` and `dev` scripts in `package.json` gained a prefix:

```
"build": "node api.js && turbo build",
"dev": "node api.js && turbo dev",
```
The prefix kept each project's real command (`vite build` at Open Food Facts, `node scripts/multi-build.js` at CircuitVerse). Open Food Facts' package is an ES module, so its `api.js` starts with an extra `createRequire` line that gives the loader Node's `require`.

**A hidden task that runs when the folder is opened.** The CircuitVerse commits carried PolinRider's full kit:

- `.vscode/tasks.json` with a hidden task labelled `eslint-check` that runs `node ./public/fonts/fa-solid.lkf` when the folder is opened, with its terminal panel hidden
- `.vscode/settings.json` that turns on automatic tasks and hides the terminal
- `public/fonts/fa-solid.lkf`, a text file of obfuscated JavaScript named like a font, next to a copied Font Awesome kit
- `public/fonts/README.md`, a decoy that describes fonts for a "Blockchain Explorer" application
- `.gitignore` lines that hide `temp_auto_push.bat` and `branch_structure.json`, and removal of the lines that kept `.vscode/` out of git

`temp_auto_push.bat` is the script PolinRider drops on infected Windows machines to amend a repository's latest commit with the payload, keep the original message and dates, and force-push the result. `branch_structure.json`, a list of local branches written by the same tool, was committed by mistake in the AsyncAPI and Open Food Facts pull requests.

Other PolinRider victims have reported on the OpenSourceMalware PolinRider tracker that the malware rewrites repositories on the infected machine, and that a GitHub token stolen from VS Code's sign-in was used to clone every repository the victim could reach and force-push rewritten commits.

### Three ways the loader runs

| Trigger | What starts it | 
|---|---|
| `npm run build` or `npm run dev` | The `node api.js &&` prefix in `package.json` | 
| Running tests or a build that loads a config file | Jest loads `jest.config.js` when tests run. The build loads `postcss.config.js` in Open Food Facts. | 
| Opening the folder in VS Code | The hidden `folderOpen` task, if automatic tasks are allowed | 

None of these uses an npm install script, so blocking `preinstall` and `postinstall` scripts does not stop them.

## What Happened in Each Project's CI

All three projects received the poisoned commits through fork pull requests. For `pull_request` workflows from a fork, GitHub passes no repository secrets and limits `GITHUB_TOKEN` to read access, and no project has reported stolen secrets. Those limits do not stop the code from running or from connecting to the internet.

| Project | Pull requests with the payload | Did CI run it? | What followed | 
|---|---|---|---|
| AsyncAPI Generator | 2 | No. Fork pull request workflows need a maintainer's approval, and none was given. | Nothing ran | 
| CircuitVerse (cv-frontend-vue) | 10 | Yes, with no approval step. The maintainers confirmed the loader ran in the desktop build. | The release workflow built the desktop app on four runners and uploaded the results. The maintainers deleted 40 installers and opened a fix so fork pull requests no longer publish builds. | 
| Open Food Facts (openfoodfacts-explorer) | 4 | The CI workflow, which includes `pnpm build`, ran on each poisoned commit. All four runs failed. | The maintainers rotated a secret | 

CircuitVerse's maintainers wrote that the fork pull requests were able to "publish 40 infected installers through our CI." The loader ran on the runners that compiled the Windows, Linux and macOS installers, and its downloaded stages run as background processes that outlive the build step. The installers stayed downloadable from the workflow runs' artifact pages until the maintainers deleted them on November 25, more than a month later.

## What the Loader Does

We decoded the payloads statically with the AsyncAPI maintainer's published decoders. All four files (two `api.js` variants, `postcss.config.js` and the fake font) decode to the same 16,674-byte script, which:

1. **Finds the newest transaction from the wallet.** It asks public Ethereum services (1rpc.io, drpc.org, publicnode.com, blastapi.io, or a service named in `$ETH_RPC_URL`) for recent blocks, and falls back to Blockscout's API.
2. **Reads two IP addresses from the transaction.** The transaction is sent to an address that isn't a real account. Its first 8 bytes are two IPv4 addresses, in practice the same one twice, followed by the text `helloipbot!!`.
3. **Downloads the next stage.** It requests `http://<ip>:443/0x/cls`, plain HTTP on the HTTPS port, decodes the response with a fixed XOR key, and runs it inside the current process and as a separate background `node` process that keeps running after the build or test command exits.
4. **Downloads a second stage** from `http://<ip>:443/0x/ls` and starts it as another background process.

Victims who analysed infected machines report on the OpenSourceMalware tracker that the later stages read saved passwords and keys from browsers and the macOS keychain, modify editor app bundles so the loader restarts, and use the developer's GitHub access to push the loader into more repositories.

## The Wallet Is Still Posting Servers

The loader checks only a few blocks. It rounds the current block number down to the nearest multiple of 1,000 and fetches six blocks: that block, the ones either side of it, and the same three around the previous multiple of 1,000. Ethereum adds a block about every 12 seconds, so a multiple of 1,000 comes about every 3 hours 20 minutes. If those six blocks hold nothing from the wallet, the loader falls back to a slower search.

The operator posts on that schedule. 344 of the wallet's 377 transactions are within one block of a multiple of 1,000, the median gap between them is 200 minutes, and all 377 cost 0.026 ETH in fees. Decoded, the history is:

| Server address | First posted (UTC) | Last posted (UTC) | Transactions | 
|---|---|---|---|
| 166.88.134.75 | Sep 4, 05:18 | Sep 12, 11:21 | 61 | 
| 103.179.143.219 | Oct 14, 01:52 | Oct 16, 02:07 | 28 | 
| 23.27.13.72 | Oct 14, 04:52 | Oct 14, 04:52 | 1 | 
| 95.135.181.151 | Oct 16, 05:00 | Nov 12, 22:57 | 194 | 
| 95.135.181.84 | Nov 12, 23:44 | Nov 25, 18:30 | 93 | 

Data as of November 25, 20:22 UTC. On October 19, when the pull requests were poisoned, the wallet pointed to 95.135.181.151.

The wallet is public, so each new server address can be read as soon as it is posted. Blocking build-time calls to the Ethereum services stops the loader before it gets an address. Blocking one server IP does not.

### The same operator as the fake interviews

On November 24 we [updated our AccuraSoftHire post](https://www.stepsecurity.io/blog/accurasofthire-fake-interview-developer-machines) with HuntRole, a second fake recruiter whose coding test was a VS Code extension. That extension's loader reads this same wallet. The wallet received 0.06 ETH on November 11 from `0xf97062cb1b6ffa18b88e9faea373ed288a87ecd0`, which also funded the AccuraSoftHire wallet, and 12 of the infected repositories in the next section carry an `api.js` that reads the AccuraSoftHire wallet directly. The fake interviews and these repository infections share an operator.

## Not One Account

`Eternity0207` is one of hundreds of infected accounts. GitHub code search returns 2,776 `package.json` files containing `node api.js &&`. The search API returns at most 1,000 results; 715 of them came back, in 622 repositories. We fetched the `api.js` next to each manifest on November 25, without running anything:

- **576 repositories** carry the loader: one very long line of obfuscated code after hundreds of tabs or spaces. They belong to 311 GitHub accounts, 30 of them organizations. Many copies open with a small fake `api` module so the file looks ordinary.
- 5 have the build hook and an `api.js` without the loader: three hold only the fake `api` module, and two are empty.
- 41 have no `api.js` next to the manifest.

We decoded the copies in 402 of the 576 repositories: 390 read wallet `0x1eef…cef3`, and 12 read `0xa322e5f3d311d3080e6f0121063e9adc2490ef1a`, the AccuraSoftHire wallet. All 576 repositories were last pushed in October or November 2026.

Most are personal projects. Their owners' pull requests to other projects can carry the same rewritten commits, as `Eternity0207`'s did.

## Am I Affected?

**If your project received pull requests from `Eternity0207`:** the pull request pages are gone, but merged commits are still in your history under the account's name. Check any CI logs from October for runs on the account's pull request branches that ran `node api.js`, and ask reviewers whether they checked out those branches.

**For any repository**, these commands only read:

```
# Build scripts that run a file first
grep -rnE '"(build|dev|start|test)":[[:space:]]*"node (api\.js|init) &&' --include=package.json .
# Code hidden after long runs of tabs or spaces
grep -rlE '(^|[;})])[[:blank:]]{100,}[^[:blank:]]' --include='*.js' --include='*.mjs' --include='*.cjs' .
# PolinRider's folder-open task, fake fonts and tool files
grep -rl '"runOn": *"folderOpen"' --include=tasks.json .
find . -path '*/fonts/*' \( -name '*.lkf' -o -name '*.lfk' -o -name '*.orc' -o -name '*.llf' \)
git log --all --oneline -- branch_structure.json temp_auto_push.bat
```
**On a machine that ran a build from one of these branches**, look for background `node -e` processes whose command line sets `global['_V']` or `global['_H']`:

`ps -axww -o pid,ppid,lstart,command | grep -E "_t_s|_H2|global\['r'\]=require" | grep -v grep`
A match means the machine is compromised. Note the process ID and command line, then rotate GitHub, npm, SSH and cloud credentials from a clean machine.

**In CI**, look for build or test steps that called the Ethereum services listed in the indicators below, or plain HTTP to port 443 on the server addresses.

## What to Change

1. **Require approval before workflows run on fork pull requests.** In the repository's Actions settings, under the controls for workflows from forks, choose "Require approval for all external contributors". Requiring approval kept AsyncAPI's CI from running the payload. The first-time-contributor options would not have stopped this account, which already had merged pull requests in CircuitVerse and Open Food Facts.
2. **Don't publish artifacts from fork pull requests.** Build them if you need the check, but upload installers and packages only from your own branches and releases. CircuitVerse's fix does this.
3. **Treat a force-push after review as a new pull request.** Turn on the branch protection rule "Require approval of the most recent reviewable push", and read the pull request timeline for `force-pushed` events, not only the final diff.
4. **Check what a diff hides.** Very long lines, an added line that looks empty, new `node <file> &&` prefixes in `package.json` scripts, and changes to `jest.config.js`, `postcss.config.js` or `.vscode/` need a closer look.
5. **Watch for unsigned commits from a contributor who usually signs.** Every malicious commit here was unsigned, with a different committer name.
6. **Keep VS Code's Restricted Mode on for code you haven't reviewed.** Restricted Mode doesn't run workspace tasks, so a `folderOpen` task in a pull request branch won't fire when you open it.

## How StepSecurity Helps

This table maps each part of the attack to the StepSecurity feature that covers it:

| Where it shows up | StepSecurity feature | What it does | 
|---|---|---|
| Loader committed to a repository or a pull request branch | Malicious Files for GitHub | Scans every file version in git history and names the commit that added a flagged file | 
| Loader running in a CI build | Harden-Runner | Flags or blocks unexpected outbound connections from the build | 
| Folder-open task on a developer's machine | Dev Machine Guard: Suspicious Files | Flags editor files that run code when a project is opened | 
| Credentials on an infected machine | Dev Machine Guard: Credentials | Shows which credentials are stored on each machine, so you know what to rotate | 

### 1. Malicious Files for GitHub: find the loader in your history

Malicious Files for GitHub checks every file version in a repository's git history against detection rules that StepSecurity maintains, and each finding names the commit that added the file. Its PolinRider rules flag files from this attack, such as the loader appended to build and test configuration files.

The infected commits keep their original dates and can look years old. After a rule is added, rescan repository history to find them.

### 2. Harden-Runner: stop the loader from finding its server

Harden-Runner monitors network traffic from each step of a GitHub Actions job. A build step that calls `1rpc.io`, `eth.drpc.org` or `ethereum-rpc.publicnode.com`, then fetches from a bare IP address on port 443 over plain HTTP, stands out against the job's normal traffic. With an egress block policy, the call to the Ethereum service is blocked and the loader never gets a server address.

### 3. Dev Machine Guard: check the machines that opened these branches

Opening one of these branches in VS Code with automatic tasks allowed runs the loader without any build. Suspicious Files in Dev Machine Guard scans enrolled developer machines for files flagged by rules StepSecurity maintains, including `.vscode/tasks.json` files set to run when a folder opens. Each finding shows the device, the file path and the campaign.

On an affected machine, Credentials in Dev Machine Guard shows which credentials are stored there, including which are in plaintext. Rotate GitHub tokens first: PolinRider uses them to push itself into more repositories.

## Indicators of Compromise

| Type | Indicator | Notes | 
|---|---|---|
| Ethereum wallet | `0x1eef0849eda15d87f64e51c73c8442cf3c8bcef3` | Publishes the server address | 
| Server IPs | `95.135.181.84` | Current, since Nov 12 | 
|  | `95.135.181.151` | Oct 16 to Nov 12, active on Oct 19 | 
|  | `103.179.143.219`, `23.27.13.72`, `166.88.134.75` | Earlier | 
| URL paths | `/0x/cls`, `/0x/ls` on port 443, plain HTTP |  | 
| HTTP headers | `Sec-V: A8-&&`, `Sec-V: A8-8113`, `X-Payload-B64` |  | 
| Ethereum services called | `1rpc.io/eth`, `eth.drpc.org`, `ethereum-rpc.publicnode.com`, `eth-mainnet.public.blastapi.io`, `eth.blockscout.com/api` | Legitimate services; suspicious when called from a build or test step | 
| Build markers | `global['!'] = '8-&&'`, `global['!'] = '8-8113'` |  | 
| Files | `api.js` with `node api.js &&` in `package.json`; `public/fonts/fa-solid.lkf` or `.lfk`; `.vscode/tasks.json` task `eslint-check`; `branch_structure.json`; `temp_auto_push.bat` in `.gitignore` |  | 
| SHA-256 | `b02a81974810532fff8f76903e09b20431857bfaff00f2473421f4a4fb8162b5` | `api.js`, AsyncAPI and CircuitVerse | 
|  | `41a69ba3946396d2d1c15f2e43be705f0793e8773dee0f3dda89a541d31c00d9` | `api.js`, Open Food Facts (ES module variant) | 
|  | `3ae470cabb9412bf5f0e64e1f71b458e14eb10b19070845597d5b8230b27d552` | `public/fonts/fa-solid.lkf`, CircuitVerse | 
| Malicious commits | `0e2d8001ae47ec85b75295585ff982f2e8f65527`, `a89182973f350b1500ab4bedb1faa5a3928fb810` | asyncapi/generator | 
|  | `c3d3f36443c98c6ee8473a87deeb1e4ce8a81bee`, `05e3ffbbfcdf5ab9e8f31b9313e46bef3ae35d6a` (and 8 more) | CircuitVerse/cv-frontend-vue | 
|  | `a6569a93cf547382dfe69cd126c846f6af4e7df9`, `edb26d5a44e40a9e3266ee8a83a0b2902fd93b6d`, `91557f66b31c5ab0b5bb95895cb1d2717524b0b1`, `86016a03178a2314cdb0bfbbc14dc6db5d6efa6b` | openfoodfacts/openfoodfacts-explorer | 

## References

- Lukasz Gornicki (AsyncAPI): [incident index](https://gist.github.com/derberg/0b4b21fb0a33148c3a13ef3211414b33), [payload analysis and decoders](https://gist.github.com/derberg/1d438e1c3f08d43e41b25bb77aa3f0eb), [CircuitVerse and Open Food Facts](https://gist.github.com/derberg/56e1d0ea296c221e7e6d7a7e387e7157), [all pull requests from the account](https://gist.github.com/derberg/21cda01d35b60877e7db707143487b1e)
- CircuitVerse: [issue #1586](https://github.com/CircuitVerse/cv-frontend-vue/issues/1586), [fix pull request #1591](https://github.com/CircuitVerse/cv-frontend-vue/pull/1591)
- Open Food Facts: [issue #2267](https://github.com/openfoodfacts/openfoodfacts-explorer/issues/2267)
- Heads-up issues: [Meshery](https://github.com/meshery/meshery/issues/24312), [Jitsi Meet](https://github.com/jitsi/jitsi-meet/issues/18486), [stdlib](https://github.com/stdlib-js/stdlib/issues/16819), [Jaeger](https://github.com/jaegertracing/jaeger/issues/10279), [PipeCD](https://github.com/pipe-cd/pipecd/issues/7667), [Floresta](https://github.com/getfloresta/Floresta/issues/1514)
- OpenSourceMalware PolinRider tracker: [issue #12](https://github.com/OpenSourceMalware/PolinRider/issues/12), [issue #13](https://github.com/OpenSourceMalware/PolinRider/issues/13), [issue #15](https://github.com/OpenSourceMalware/PolinRider/issues/15)
- StepSecurity: [The Take-Home Test That Runs on Your Work Laptop: Inside the AccuraSoftHire Fake Interview Campaign](https://www.stepsecurity.io/blog/accurasofthire-fake-interview-developer-machines)
- GitHub Docs: [Approving workflow runs from forks](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/approve-runs-from-forks), [Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository)
- Wallet on Blockscout: [0x1eef0849eda15d87f64e51c73c8442cf3c8bcef3](https://eth.blockscout.com/address/0x1eef0849eda15d87f64e51c73c8442cf3c8bcef3)
