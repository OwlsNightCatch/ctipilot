---
title: PolinRider Moves to Python with an Ethereum Calldata Loader
author: SafeDep Team
url: https://safedep.io/blog/polinrider-python-loader-ethereum-calldata
hostname: safedep.io
description: PolinRider hides a Python loader in utils modules and conftest.py that runs JavaScript stored in Ethereum transactions. 375 repositories, wallets, C2, IOCs.
sitename: SafeDep
date: "2026-11-24"
categories: ['Malware']
tags: ['supply-chain', 'malware', 'github', 'blockchain', 'polinrider', 'python', 'threat-intel']
fingerprint: "99b01390cea48741"
language: en
image: https://safedep.io/_next/static/immutable/media/polinrider-python-loader-ethereum-calldata-banner.1et8uyjopvq1y.png
pagetype: article
filedate: "2026-11-26"
---
# PolinRider Moves to Python with an Ethereum Calldata Loader

On this page

The PolinRider campaign now plants a Python loader in GitHub repositories. The loader hides in a small `utils` package or in `conftest.py`. When Python imports the file, the loader reads the newest transaction that an Ethereum wallet sent to itself. It decodes the input data of that transaction as JavaScript and runs it with Node.js. That JavaScript reads a second wallet to find the command and control (C2) server. It then passes the next stage to a detached `node -i` process. On 24 November 2026, SafeDep found the loader in 375 public repositories that belong to 260 accounts. No package on PyPI or npm carries it. `pytest` runs the loader through `conftest.py`. The planted import lines in application files run the loader only when Python can find the `utils` package. In the three example applications that SafeDep checked, the documented start commands fail with an import error before the loader runs.

Jay Maier of Rising Sun Solutions (GitHub [`jaym2026`(opens in new tab)](https://github.com/jaym2026)) first reported the loader on 24 November 2026 in [issue #96 of `meSingh/polinrider-scanner`(opens in new tab)](https://github.com/meSingh/polinrider-scanner/issues/96). The report names the wallet, the loader file and the wallet that funded it. This post confirms that report, measures the spread on GitHub, decodes the JavaScript on the chain, and names the current C2 server. It continues the September post [PolinRider Switches to Ethereum C2 in 30+ Repositories](https://safedep.io/blog/polinrider-ethereum-c2-github-repositories).

## Key findings

- The loader is 58 lines of Python. It reads wallet `0x3b1574417524c11a7403c4b232CAcBb320CceBC6` through the public Ethplorer API and an Ethereum RPC node. The payload is in the input data of a transaction, not in an IP address in the `to` field as in the September samples.
- GitHub code search returns the exact loader in 375 files in 375 repositories under 260 accounts. 370 of these repositories had a push in November 2026. Most are small personal projects, with 189 stars in total.
- The wallet sent 8 transactions to itself from 24 October to 11 November 2026. The newest one holds a 31 KB JavaScript stage with the campaign marker `A9-10502`.
- That stage reads a second wallet, `0x1eEf0849EDa15d87f64e51C73C8442Cf3c8bCEF3`, with the same method as the `0xa322` wallet in the September post. The wallet points to the C2 server `95.135.181[.]84` from 12 November 2026.
- The stage writes the next stage to the standard input of a detached `node -i` process. The code does not appear in the process command line.
- Two repositories hold the loader in a commit whose message says that it removes the malware. Another commit carries dates from September 2025, more than a year before the first transaction of the wallet.

## The loader

The loader below is `conftest.py` at the root of [`Mizero-eloi/alu_regex-data-extraction-MizeroEloi@82a87bb9`(opens in new tab)](https://github.com/Mizero-eloi/alu_regex-data-extraction-MizeroEloi/blob/82a87bb90b3eca941b913f5699fa54b8d1551b52/conftest.py). The same 58 lines are in every repository in this post:

The loader asks Ethplorer for the last 100 transactions of the wallet, with the public API key `freekey`. It takes the first transaction that the wallet sent, which is the newest one. It gets the full transaction from `ethereum.publicnode.com`, decodes the input data from hex to text, writes it to a temporary `.js` file, and runs `node` on it. The outer `try` hides every error, so a project without Node.js shows nothing. The `subprocess.run` call stops `node` after 20 seconds. The JavaScript stage therefore starts its next step in a detached process that outlives the loader.

The loader uses only the standard library. It needs no dependency, so a scan of `requirements.txt` or a lockfile does not show it. Ethplorer and PublicNode run shared public services. A request to them alone does not mean an infection.

The loader exists in two encodings. 355 files have LF line endings (git blob `0302eeba`, SHA-256 `45f1e5c4...f53a`). 20 files have CRLF line endings (git blob `e9e0e433`, SHA-256 `adf94e02...1f91`). The code is the same.

## Where the loader hides

The loader file has a name that looks like part of an HTTP client. GitHub code search for the wallet address returned these 375 loader files:

| File name | Files | 
|---|---|
| `session.py` | 183 | 
| `transport.py` | 65 | 
| `clients.py` | 46 | 
| `http_session.py` | 45 | 
| `net.py` | 24 | 
| `conftest.py` | 12 | 

363 files are in a planted package. 307 of these packages are a `utils` folder inside the project, 30 are a `utils` folder at the repository root, and 26 are in another folder such as `lib`, `helpers`, `common` or `shared`. In the example repositories, the planted `utils` folder has six files: `__init__.py`, `clients.py`, `http_session.py`, `net.py`, `session.py` and `transport.py`. One of them holds the loader and the others are empty. In [`wakaflorien/cst-research-api`(opens in new tab)](https://github.com/wakaflorien/cst-research-api/blob/1eb312a41fa7fc932471e05443295b7cce56d865/core/utils/net.py) the loader is `net.py`. In [`dedev-llc/rpr`(opens in new tab)](https://github.com/dedev-llc/rpr/blob/efd5f17c52b057450c7aac7d6644fa57873a9077/src/rpr/utils/session.py) it is `session.py`.

The attacker also adds five import lines to a start file of the project. This is the Django Asynchronous Server Gateway Interface (ASGI) file of `cst-research-api`:

The same five lines are at the top of [`app/main.py`(opens in new tab)](https://github.com/Moderato-CMaaS/python-rag-api/blob/9b708c02e24131d55bc008305ac6ddcc67ac9250/app/main.py) in the FastAPI project `Moderato-CMaaS/python-rag-api` and of [`src/rpr/cli.py`(opens in new tab)](https://github.com/dedev-llc/rpr/blob/efd5f17c52b057450c7aac7d6644fa57873a9077/src/rpr/cli.py) in the `rpr` command line tool. GitHub code search finds 194 files that import `utils.net`, `utils.clients` and `utils.http_session` together. In the first 100 results, the most common are `main.py` (42) and `app.py` (20).

The other 12 loaders are `conftest.py` files. `pytest` imports every `conftest.py` that it finds while it collects tests, so these need no import line.

## What runs the loader

The issue report and other early reports say that a start of the application runs the loader. The import lines are there, but they work only when Python can find a top-level package named `utils`. In most repositories, the `utils` package is inside an application folder, not at the repository root. SafeDep rebuilt the layout of each example with stub modules that print a line instead of the loader, and ran the start commands from the repository root:

| Repository | Loader | Command | Result | 
|---|---|---|---|
| `Mizero-eloi/alu_regex-data-extraction-MizeroEloi` | `conftest.py` at the root | `pytest` | Runs | 
| `dedev-llc/rpr` | `src/rpr/utils/session.py` | `python src/rpr/cli.py` | Runs | 
| `dedev-llc/rpr` | `src/rpr/utils/session.py` | `rpr` or `python -m rpr` | Does not run `ModuleNotFoundError: No module named 'utils'` | 
| `Moderato-CMaaS/python-rag-api` | `app/utils/session.py` | `uvicorn app.main:app` (from the README) | Does not run `ModuleNotFoundError: No module named 'utils'` | 
| `wakaflorien/cst-research-api` | `core/utils/net.py` | An ASGI server that loads `core.asgi` | Does not run `ModuleNotFoundError: No module named 'utils'` | 

The loader runs when Python starts a script from the folder that holds `utils`, or when that folder is the working directory. It also runs in the 30 repositories with `utils` at the root, because Python finds the package from the project root. Where the import fails, the application does not start. A developer who reads the error `No module named 'utils'` and fixes the import path also starts the loader.

SafeDep did not check every one of the 375 repositories for a working import path. A `conftest.py` loader runs every time `pytest` runs in that folder.

## The JavaScript stored on Ethereum

The wallet `0x3b15...ceBC6` received 0.000542 ETH from `0x6e82b409a357be8d8e88e7d4fcb588ded3de104f` on 24 October 2026 at 05:53 UTC. Seven minutes later it sent its first transaction to itself. All transactions from the wallet go to the wallet, and each one stores data in the input field:

| Time (UTC) | Transaction | Input | Content | 
|---|---|---|---|
| 2026-10-24 06:00 | `0x2866240b` | 3 bytes | Test | 
| 2026-10-24 06:40 | `0x4b824345` | 29,557 bytes | Not valid UTF-8, the loader cannot decode it | 
| 2026-10-25 05:47 | `0x43ce178a` | 29,529 bytes | JavaScript build 1 | 
| 2026-10-28 09:12 | `0x80bc5752` | 29,755 bytes | JavaScript build 2 | 
| 2026-10-28 10:15 | `0x7fe11f4d` | 30,738 bytes | JavaScript build 3 | 
| 2026-10-28 13:11 | `0xf4357b87` | 30,738 bytes | Build 3 again | 
| 2026-11-01 06:28 | `0x09d11256` | 30,738 bytes | Build 3 again | 
| 2026-11-11 16:35 | `0x474097c1` | 31,134 bytes | JavaScript build 4, the newest on 24 November 2026 | 

The same wallet `0x6e82b409` sent 0.0014 ETH at 13:11 UTC on 28 October, three blocks before the second copy of build 3. The wallet has sent nothing since 11 November.

Build 4 starts with `var bx = '-10502';`. A table of hex strings follows, each XOR-encoded with `0x87`, and then a small function that expands a dictionary-compressed body. SafeDep decoded the three layers statically. The result is 474 lines of readable JavaScript with descriptive names. The snippets below come from that output. The other three builds use a different obfuscator, and SafeDep did not decode them.

The stage sets the marker and names the wallet that it reads:

This is the method of the `0xa322` wallet in [the September post](https://safedep.io/blog/polinrider-ethereum-c2-github-repositories). The stage reads the Ethereum block at the last multiple of 1,000 and the blocks around it, and looks for a transaction from the wallet. If it finds none, it searches by transaction count, and then it asks the Blockscout API. The first 8 bytes of the `to` address are two IPv4 addresses. The last 12 bytes are the ASCII text `helloipbot!!`. This is the newest heartbeat of the wallet:

The stage then gets two scripts from the first IP address, as plain HTTP on port 443. Each response is XOR-encoded with a fixed key:

The paths, the keys, the `Sec-V` header and the global variables `_H`, `_H2`, `_t_s` and `_t_u` are the same as in the September samples. The `/0x/cls` script runs twice, once with `eval` in the current process and once in a new process. The `/0x/ls` script runs only in a new process. The new process is where this build differs:

The stage starts `node -i`, the interactive Node.js shell, as a detached process with no window. It waits for the `>`  prompt and then writes the code to the standard input of the shell. The oxc sample in the September post passed its next stage to `node -e` as a command line argument, where a process listing shows it. With `node -i`, a process listing shows only `node -i`. The detached process also survives the 20-second limit of the Python loader.

SafeDep did not connect to the C2 server, so the content of `/0x/cls` and `/0x/ls` for this chain is not known. In the chain that the September post followed to the end, the later stages installed a stealer that took environment secrets, browser passwords, cookies and wallet data.

## Wallet and C2 timeline

The wallet `0x1eEf0849EDa15d87f64e51C73C8442Cf3c8bCEF3` sent 366 heartbeats from 4 September to 24 November 2026. Each heartbeat sends zero ETH to an address that holds the C2 IP address twice. The history shows five C2 servers:

| Active (UTC) | C2 | Heartbeats | 
|---|---|---|
| 2026-09-04 to 2026-09-12 | `166.88.134[.]75` | 61 | 
| 2026-10-14 to 2026-10-16 | `103.179.143[.]219` | 28 | 
| 2026-10-14, 04:52 | `23.27.13[.]72` | 1 | 
| 2026-10-16 to 2026-11-12 | `95.135.181[.]151` | 194 | 
| 2026-11-12, 23:44 to 2026-11-24 | `95.135.181[.]84` | 82 | 

The wallet sent nothing from 12 September to 14 October. On 14 October it pointed to `23.27.13[.]72` for one heartbeat, between two runs of `103.179.143[.]219`. The current server, `95.135.181[.]84`, is in the same /24 network as the server before it.

## Forged dates and reinfected repositories

Earlier PolinRider waves rewrote existing commits with forged author and committer data and then force-pushed them. The Python wave shows the same pattern:

- The `conftest.py` loader in `Mizero-eloi/alu_regex-data-extraction-MizeroEloi` is in commit `82a87bb9`, “\[feat\]: Added the test extractors”. Its author and committer dates are 26 September 2025. The wallet that the loader reads made its first transaction on 24 October 2026, and GitHub records the last push to the repository on 16 November 2026.
- In `wakaflorien/cst-research-api`, the loader is in commit [`1eb312a4`(opens in new tab)](https://github.com/wakaflorien/cst-research-api/blob/1eb312a41fa7fc932471e05443295b7cce56d865/core/utils/net.py), “fix: remove PolinRider malware (FixFlow)”. The committer date is 12 October 2026, 12 days before the first transaction of the wallet.
- In `dedev-llc/rpr`, the loader is in commit [`efd5f17c`(opens in new tab)](https://github.com/dedev-llc/rpr/blob/efd5f17c52b057450c7aac7d6644fa57873a9077/src/rpr/utils/session.py), “Remove injected malware from forced pushes”, dated 3 November 2026.

In two repositories, the owner removed an earlier PolinRider infection, and the newest commit still holds the Python loader. The commit dates do not show when the loader arrived. An attacker who controls a developer’s machine or token sets them to any value. A clean-up that does not also clean the machine that pushes to the repository does not hold.

## Am I affected?

The loader is in source repositories, not in packages. A dependency scan does not find it. Search your projects and clones for the wallet and the loader calls:

A hit in the second command alone needs a check by hand, because a project can have its own `utils` package. Check also the git history of each project, because a clean-up commit can leave the loader in place:

Some commands run the loader in a project that holds it: `pytest`, a script next to the planted `utils` folder, or the application from that folder. If you ran one of them on a computer with Node.js, treat the computer as compromised:

- Rotate the secrets in the shell environment of that computer, and the passwords and session cookies saved in its browsers.
- Move funds out of any wallet extension or wallet file on that computer.
- Look for a `node -i` process that has no terminal, and for connections to `95.135.181[.]84` on port 443 or 80.
- On the network, look for a Python process that calls `api.ethplorer.io` and then `ethereum.publicnode.com`, followed by a `node` process that calls an Ethereum RPC endpoint or `eth.blockscout.com` and then a raw IP address.

If you own an infected repository, delete the planted package, the import lines and the `conftest.py` loader. Then clean the computers that push to the repository, and replace their GitHub tokens and SSH keys. A repository gets infected again while those computers stay infected.

## Infected repositories

All 375 repositories below held the loader on their default branch on 24 November 2026. Each link points to the loader file at the commit in the GitHub search index. A link can return 404 later if the owner removes the history.

| Row | Repository | Loader file | Evidence (file at commit) | 
|---|---|---|---|
| 1 | 20020109tharindu/ML\_Final\_Project | preprocessing/utils/session.py | https://github.com/20020109tharindu/ML\_Final\_Project/blob/92559ff0c631a96fa1592e9f591d7c80cfd9a209/preprocessing/utils/session.py | 
| 2 | aacif-bashir/PythonCourse | Project\_01/utils/session.py | https://github.com/aacif-bashir/PythonCourse/blob/a4ac9897ddd17708e4c5e01afd4b2dfe4f42a8d4/Project\_01/utils/session.py | 
| 3 | aamir-786/Python-Projects | python program/utils/session.py | https://github.com/aamir-786/Python-Projects/blob/1d74fc0f89de034451ccddf5893988632701a2d0/python program/utils/session.py | 
| 4 | aayush2724/XBot | backend/xbot/utils/http\_session.py | https://github.com/aayush2724/XBot/blob/1c198a8c8ee50ffb0406c1ccecfc5612634466c1/backend/xbot/utils/http\_session.py | 
| 5 | abdulfatiransari/linkedin-agent-backend | api/utils/session.py | https://github.com/abdulfatiransari/linkedin-agent-backend/blob/54b86d0240de5b91c72abc1782eb67fe109eb32f/api/utils/session.py | 
| 6 | Abdullah-Abid-03/AWS-Projects | AWS Project 3a - AWS Cost Optimization Pipeline/utils/session.py | https://github.com/Abdullah-Abid-03/AWS-Projects/blob/6bb4684dd52fd95a03868a46a5e3a56c03a6760a/AWS Project 3a - AWS Cost Optimization Pipeline/utils/session.py | 
| 7 | Abdullah-Abid-03/Chai-PostHiv-Django | Chai\_Django\_Proj/utils/transport.py | https://github.com/Abdullah-Abid-03/Chai-PostHiv-Django/blob/103e00e4079c42c8230e9c75bacd4c2f384aa325/Chai\_Django\_Proj/utils/transport.py | 
| 8 | Abdullah-Abid-03/Cloud-Data-Engineering-Projects | Project 1/utils/transport.py | https://github.com/Abdullah-Abid-03/Cloud-Data-Engineering-Projects/blob/e5bda9a01e8db67ea9b0712d59a45a4a543ab07d/Project 1/utils/transport.py | 
| 9 | Abdullah-Abid-03/DevOps-Projs | Project - 01/Sample\_Flask\_app/utils/transport.py | https://github.com/Abdullah-Abid-03/DevOps-Projs/blob/262831f7891708bab6d1247d0d59a5e7a667e7ec/Project - 01/Sample\_Flask\_app/utils/transport.py | 
| 10 | AbdullahAslam1207/DevopsA2 | booking/utils/session.py | https://github.com/AbdullahAslam1207/DevopsA2/blob/4ffa20c0c7076c178d00cc0d0d64768721aceab8/booking/utils/session.py | 
| 11 | AbdullahAslam1207/Twilio\_VoiceBot | utils/clients.py | https://github.com/AbdullahAslam1207/Twilio\_VoiceBot/blob/19cae66adbdbd597155c7693364056edd3774baa/utils/clients.py | 
| 12 | AbdullahAslam1207/VOX\_JOBS\_AI | conftest.py | https://github.com/AbdullahAslam1207/VOX\_JOBS\_AI/blob/000faa948ba9e7e600b9573f0f03be3ab08c7e43/conftest.py | 
| 13 | Abdullahx888/Secure-chat-assignment | app/common/session.py | https://github.com/Abdullahx888/Secure-chat-assignment/blob/3af648950330feb43e6ffffc886be4a2bd26e717/app/common/session.py | 
| 14 | achiniEsandi/ExploringDataScience | ScikitLearn/utils/transport.py | https://github.com/achiniEsandi/ExploringDataScience/blob/36fd8cf36798f0039daf694c05c74e93e31816b6/ScikitLearn/utils/transport.py | 
| 15 | AdeelAhmedQureshi/VideoDiscovery | Backend/app/utils/session.py | https://github.com/AdeelAhmedQureshi/VideoDiscovery/blob/01cca117dc72f304fd922755359028cc61e084d0/Backend/app/utils/session.py | 
| 16 | Admonk20/twitter-sports-bot | utils/clients.py | https://github.com/Admonk20/twitter-sports-bot/blob/63983a07b25b79885bef1b313b930f7f64895ef1/utils/clients.py | 
| 17 | AdnanAftab1/deepseek-api | DeepSeekAPI/DeepSeekChat/utils/http\_session.py | https://github.com/AdnanAftab1/deepseek-api/blob/273c16fff16c89f646263c0818590fb26cbeb7f7/DeepSeekAPI/DeepSeekChat/utils/http\_session.py | 
| 18 | aframson/scrap-wallmart | utils/session.py | https://github.com/aframson/scrap-wallmart/blob/a6cdd03931d2e90838d906c84a036ec22521a5c2/utils/session.py | 
| 19 | Afzal-Iqbal/agentsdk | utils/session.py | https://github.com/Afzal-Iqbal/agentsdk/blob/95de1bda395bd9a5bd874c449ba991847a58dd8e/utils/session.py | 
| 20 | Afzal-Iqbal/django-learning | simosaLearning/utils/session.py | https://github.com/Afzal-Iqbal/django-learning/blob/098399485b48fe5e93f91425ca9b8e3b7e2d803b/simosaLearning/utils/session.py | 

## Indicators of compromise

| Row | Indicator | Type | Context | 
|---|---|---|---|
| 1 | 0x3b1574417524c11a7403c4b232CAcBb320CceBC6 | Ethereum wallet | Dead drop read by the Python loader. The input of its newest self-sent transaction is the JavaScript stage | 
| 2 | 0x6e82b409a357be8d8e88e7d4fcb588ded3de104f | Ethereum wallet | Funded 0x3b15 on 2026-10-24 and 2026-10-28 | 
| 3 | 0x1eEf0849EDa15d87f64e51C73C8442Cf3c8bCEF3 | Ethereum wallet | Operator wallet read by the JavaScript stage. The to address of each heartbeat holds the C2 IP address | 
| 4 | 95.135.181.84 | IP address | C2 from 2026-11-12, current on 2026-11-24. Plain HTTP on port 443 | 
| 5 | 95.135.181.151 | IP address | C2 from 2026-10-16 to 2026-11-12 | 
| 6 | 103.179.143.219 | IP address | C2 from 2026-10-14 to 2026-10-16 | 
| 7 | 23.27.13.72 | IP address | C2 on 2026-10-14, one heartbeat | 
| 8 | 166.88.134.75 | IP address | C2 from 2026-09-04 to 2026-09-12 | 
| 9 | http://95.135.181.84:443/0x/cls | URL | Next stage, XOR key q4FZkxX{!h,Sr3=@, run with eval and in a detached node -i | 
| 10 | http://95.135.181.84:443/0x/ls | URL | Boot stage, XOR key y-p\_>d$0B&@^1aQk, run in a detached node -i | 
| 11 | 45f1e5c405d1253b0014a17619581d31e1b94fdca8733519d84b9795a460f53a | SHA-256 | Python loader, LF line endings (git blob 0302eeba, 1,585 bytes) | 
| 12 | adf94e02b0dea9efbf0c02c522fd39d7b833adc41067e747c3eb0843e36a1f91 | SHA-256 | Python loader, CRLF line endings (git blob e9e0e433, 1,642 bytes) | 
| 13 | 0302eeba73c5e1b9717b60e6c07de110349cb4e9 | Git blob | Python loader, LF line endings | 
| 14 | e9e0e43379fbb8297d0b2d57b57b4ab94217d7e4 | Git blob | Python loader, CRLF line endings | 
| 15 | 0x474097c1e7162d858090b798e37ec7342cef00c44c8c71f1b8cdd755b6f75db7 | Ethereum transaction | Newest self-sent transaction of 0x3b15 (2026-11-11). Its input is the JavaScript stage that runs today | 
| 16 | 623daf99f3bba7ac590025b46d7d7e3fc8d8917629548d3c6e28cfb5aa1b6328 | SHA-256 | JavaScript stage in transaction 0x474097c1 (31,134 bytes) | 
| 17 | 0x09d11256e2ea5a8125a4d69ce953400c71a4106164493ef79a2fffbb5c44efa2 | Ethereum transaction | Self-sent payload transaction, 2026-11-01 | 
| 18 | 0xf4357b87bb0742d027728a20d303eef7103612f9c3d3684394908cffcf8858d3 | Ethereum transaction | Self-sent payload transaction, 2026-10-28 13:11 UTC | 
| 19 | 0x7fe11f4de256ad59d7b112fb107348672449f977b492da954f2dc18151806f3b | Ethereum transaction | Self-sent payload transaction, 2026-10-28 10:15 UTC | 
| 20 | 65408e27530326d501d481955300fa8e3ef2fffc0b7b07ffa29747b7337e0f17 | SHA-256 | JavaScript stage stored in the three transactions above (30,738 bytes) | 

## Related reading

- [PolinRider Switches to Ethereum C2 in 30+ Repositories](https://safedep.io/blog/polinrider-ethereum-c2-github-repositories) documents the `0xa322` wallet, the `helloipbot!!` heartbeat and the later stages.
- [Configuration Files That Run Code](https://safedep.io/blog/config-files-that-run-code) explains how files that tools load by name, such as `conftest.py`, run code without an explicit command.
- [Malicious pull requests threat model](https://safedep.io/blog/malicious-pull-requests-threat-model) describes how a pull request can run code on reviewer computers and CI systems.

- supply-chain
- malware
- github
- blockchain
- polinrider
- python
- threat-intel
