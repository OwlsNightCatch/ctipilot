from fu2_lib import *
S = 'agentfw/socket.extract.md'; D = 'agentfw/safedep.extract.md'; DT = 'agentfw/safedep.timeline.txt'
W = 'agentfw/wiz.extract.md'; ST = 'agentfw/stepsecurity.extract.md'; AK = 'agentfw/aikido.extract.md'; OM = 'agentfw/osm.extract.md'
PR = 'agentfw/pypi-releases.txt'
US = 'https://socket.dev/blog/agent-framework-pypi-package-compromised-with-credential-stealer'
UD = 'https://safedep.io/blog/microsoft-agent-framework-pypi-compromise'
UW = 'https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi'
UST = 'https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised'
UAK = 'https://www.aikido.dev/blog/two-malicious-agent-framework-releases-hit-pypi-in-33-minutes'
UOM = 'https://opensourcemalware.com/blog/agent-framework-pypi-compromised'
UPY = 'https://pypi.org/pypi/agent-framework/json'
out = []
A = out.append
A('## 3. AGENT-FRAMEWORK PYPI COMPROMISE (2026-11-17)\n')
A('Sources read in full with `extract` (all `trafilatura-direct`, fetched 2026-11-18 ~04:50-05:05Z): Socket (' + US + '), SafeDep (' + UD + '; its Timeline block is a script-rendered component that `extract` drops, so it was recovered from the raw HTML into `agentfw/safedep.timeline.txt`), and three further independent detectors found by WebSearch: Wiz (' + UW + '), StepSecurity (' + UST + '), Aikido (' + UAK + '), plus OpenSourceMalware (' + UOM + '). PyPI state read from the PyPI JSON API (' + UPY + '). No Microsoft or PyPI statement could be found or read (see 3.8). All IOC material (hashes, endpoint) is deliberately omitted here.\n')

A('### 3.1 Affected versions, timeline, state on PyPI\n')
A(table([
 ('Socket: compromised on 17 Nov, versions 1.26.1 and 1.26.2', US, S, 'PyPI package was compromised on November 17th, affecting versions 1.26.1 and 1.26.2.'),
 ('SafeDep: official Microsoft metapackage; any environment that installs them', UD, D, 'steal credentials from any environment that installs them.'),
 ('SafeDep: last clean release is 1.26.0', UD, D, 'The last clean release is 1.26.0.'),
 ('SafeDep affected-versions table: 1.26.1 wheel only, malicious, removed', UD, D, 'wheel only, 10,402 bytes'),
 ('SafeDep: status wording', UD, D, 'Malicious, removed from PyPI'),
 ('SafeDep: 1.26.0 is last clean', UD, D, 'Last clean release'),
 ('SafeDep timeline (UTC): 1.26.1 published 20:35; flagged 20:57', UD, DT, '20:35 | agent-framework 1.26.1 published | Malicious | A single wheel, where every earlier release shipped a wheel and an sdist. | 20:57 | SafeDep flags 1.26.1'),
 ('SafeDep timeline: 1.26.2 published 21:08 (1.26.1 already gone); flagged 21:12; 1.26.2 removed after 21:12', UD, DT, '21:08 | agent-framework 1.26.2 published | Malicious | 1.26.1 is gone from PyPI.'),
 ('SafeDep timeline: flagged 21:12', UD, DT, '21:12 | SafeDep flags 1.26.2'),
 ('SafeDep timeline: removal', UD, DT, 'After 21:12 | 1.26.2 removed from PyPI | Removed | 1.26.0 is again the newest version on PyPI.'),
 ('SafeDep: detection latency', UD, D, 'SafeDep flagged version 1.26.1 22 minutes after it was published on 17 November 2026.'),
 ('SafeDep: second release', UD, D, "Once 1.26.1 came off PyPI, 1.26.2 shipped the same stealer under different file names, and SafeDep flagged it 4 minutes after upload."),
 ('StepSecurity: upload and PyPI quarantine times (UTC) for both versions', UST, ST, 'Version 1.26.1 was uploaded at 20:35:20 UTC on November 17 and quarantined at 21:06:16 UTC. Version 1.26.2 followed at 21:08:39 UTC, just 2 minutes 23 seconds after the first quarantine, and was quarantined at 21:16:44 UTC.'),
 ('StepSecurity: PyPI quarantined both releases; attacker still able to publish after the first quarantine', UST, ST, 'PyPI has quarantined both releases, but the attacker demonstrated continued publishing access by uploading 1.26.2 after 1.26.1 was already quarantined.'),
 ('StepSecurity: whether access persists is not established', UST, ST, 'It does not establish whether that access remains available now.'),
 ('Wiz: both unavailable as of 21:30 UTC; 1.26.0 most recent safe', UW, W, 'As of 21:30 UTC, both versions were no longer available on PyPI.'),
 ('Wiz: safe version', UW, W, 'The most recent safe version is 1.26.0.'),
 ('Wiz: legitimate 1.26.0 published 2026-11-12 18:25', UW, W, '| 2026-11-12 18:25 | Legitimate 1.26.0 published (wheel + sdist, alongside agent-framework-core 1.26.0) |'),
 ('Aikido: exposure window for an unpinned install', UAK, AK, 'between 20:35 UTC and roughly 21:20 UTC on Nov 17, 2026'),
 ('Aikido: both removed', UAK, AK, 'Both have been removed from PyPI.'),
 ('OpenSourceMalware: says PyPI quarantined "the Microsoft publisher" (differs from StepSecurity: releases)', UOM, OM, 'PyPI quarantined the Microsoft publisher because unauthorized publishing access is believed to remain active'),
 ('Own check, PyPI JSON API 2026-11-18: latest = 1.26.0; 1.26.1 and 1.26.2 absent from the release list (not merely yanked)', UPY, PR, 'releases 1.26.1 present: False ; 1.26.2 present: False'),
 ('Own check: latest version on PyPI', UPY, PR, 'PROJECT agent-framework | info.version (latest): 1.26.0'),
 ('Own check: metapackage 1.26.0 depends on agent-framework-core[all]==1.26.0; core and foundry show no upload after 2026-11-12 (siblings looked at: core, foundry)', UPY, PR, "requires_dist: ['agent-framework-core[all]==1.26.0']"),
]))
A('')
A('Version table: clean up to and including **1.26.0** (published 2026-11-12 18:25 UTC, wheel + sdist); malicious **1.26.1** (published 2026-11-17 20:35:20 UTC, quarantined 21:06:16 per StepSecurity, wheel only 10,402 bytes) and **1.26.2** (published 21:08:39 UTC, quarantined 21:16:44 per StepSecurity, wheel only 10,449 bytes). Download volume: SafeDep "about 192,000 downloads a month", Aikido "about 190,000 downloads a month", Wiz "about 41,000 downloads a week"; nobody knows how many installs the two bad versions received (SafeDep, OpenSourceMalware).\n')
A(table([
 ('Package size / install count unknown (SafeDep)', UD, D, 'and gets about 192,000 downloads a month. How many installs the two bad versions got is not known yet.'),
 ('Wiz download figure', UW, W, 'The package gets about 41,000 downloads a week.'),
 ('OpenSourceMalware: demand statistics are not victim counts', UOM, OM, "Public download statistics for agent-framework show demand for the project as a whole, but they don't say how many times 1.26.1 or 1.26.2 were installed."),
]))
A('')

A('### 3.2 Mechanism: the .pth startup hook (behaviour only)\n')
A(table([
 ('Socket: on interpreter start the .pth line imports a module that launches collection in the background', US, S, 'imports a module that launches collection in a background process/thread.'),
 ('SafeDep: nothing has to import the package (a pip install in CI suffices)', UD, D, 'Nothing has to import the package.'),
 ('SafeDep: the host process returns at once; no visible delay', UD, D, 'The host process returns at once, so a test run or build shows no delay.'),
 ('Socket: no persistent on-disk execution marker; fresh process trees re-trigger collection', US, S, 'Fresh process trees can trigger collection again; there is no persistent on-disk execution marker.'),
 ('Wiz: runs on every interpreter start, import not needed', UW, W, 'Python runs `.pth` files on every interpreter start, so the credential stealer runs whenever Python starts in that environment, even if `agent-framework` is never imported.'),
 ('StepSecurity: a detached collector child can outlive its parent; removing the package does not stop it', UST, ST, 'The child can outlive its parent interpreter; survival beyond the job depends on runner cleanup and container or VM teardown.'),
 ('StepSecurity: scope of the hook depends on which site-packages the interpreter processes', UST, ST, 'This does not automatically affect every virtual environment sharing a base interpreter'),
 ('StepSecurity: non-Python steps do not trigger it', UST, ST, 'Non-Python steps do not themselves trigger the hook, although a previously started collector may still be running.'),
 ('Wiz/StepSecurity/Socket agree no second stage', UST, ST, 'The inspected payloads contain no remote-code-loading second stage.'),
 ('Socket: same', US, S, 'The reported payloads do not download or execute additional code.'),
 ('1.26.1 vs 1.26.2: 1.26.2 restores the clean package initializer, so checking only that file misses it', US, S, 'The legitimate package initializer is restored byte-for-byte'),
 ('Wiz: a check on 1.26.1 file names misses 1.26.2', UW, W, 'Searching only for the 1.26.1 file names will miss this version.'),
 ('SafeDep: same point', UD, D, 'A check for 1.26.1’s file names or hashes misses 1.26.2.'),
]))
A('')
A('Behaviour summary for the composer (all from the sources above): 1.26.1 ships a one-line startup file in site-packages plus a module appended to the package initializer; 1.26.2 ships a different startup file plus a new top-level module and leaves the initializer clean. The collector sets a run-once environment marker so child interpreters skip it, forks and detaches on Unix (daemon thread elsewhere), swallows all errors, and makes one HTTPS POST to a public request-capture service (webhook.site) carrying a compressed, base64-encoded JSON document. Both Socket and StepSecurity say it is not encryption.\n')

A('### 3.3 What it collects and the tokens it requests\n')
A(table([
 ('Socket: environment secrets by substring match, not an allowlist', US, S, 'substring-based matching, not a fixed variable allowlist'),
 ('SafeDep (1.26.1 description): env vars matching 31 substrings, each value capped at 8,000 characters', UD, D, 'whose names contain any of 31 substrings, including'),
 ('SafeDep: credential files up to 60, each under 256 KB (Azure CLI JSON, pip.conf, .npmrc, .netrc, git credentials, Docker config, Hugging Face token, Azure AI Foundry, Azure DevOps agent .credentials)', UD, D, 'up to 60 under 256 KB each.'),
 ('SafeDep: other processes\' environments, up to 300 /proc/PID/environ files; reaches other jobs on shared runners', UD, D, 'On a shared or self-hosted runner, that reaches secrets belonging to other jobs.'),
 ('SafeDep: it also records host context', UD, D, 'It also records the hostname, user, working directory and'),
 ('Socket: it requests fresh tokens, not only copies existing secrets', US, S, 'They actively request fresh Azure managed-identity and CI federation tokens rather than merely copying existing secrets.'),
 ('SafeDep: rotating stored secrets does not cover newly issued tokens', UD, D, 'Rotating stored secrets does not cover those.'),
 ('Wiz: Azure managed-identity tokens for 12 resources from IMDS or the App Service identity endpoint', UW, W, '**Azure managed-identity tokens** from IMDS or the App Service identity endpoint for 12 resources: ARM, Graph, Key Vault, Storage, Cognitive Services, Azure AI/ML, Search, Container Registry, Azure DevOps, and AzureADTokenExchange'),
 ('Wiz: Azure DevOps OIDC token via SYSTEM_ACCESSTOKEN and SYSTEM_OIDCREQUESTURI for api://AzureADTokenExchange', UW, W, '**Azure DevOps OIDC tokens**: if `SYSTEM_ACCESSTOKEN` and `SYSTEM_OIDCREQUESTURI` are set, it requests an OIDC token for `api://AzureADTokenExchange`'),
 ('StepSecurity: Azure DevOps OIDC and managed-identity requests in BOTH versions; GitHub Actions OIDC in 1.26.2 only', UST, ST, '- **GitHub Actions OIDC** (1.26.2 only): uses `ACTIONS_ID_TOKEN_REQUEST_URL` and `ACTIONS_ID_TOKEN_REQUEST_TOKEN` (or the runtime token) to request JWTs for the audiences `api://AzureADTokenExchange` and `https://management.azure.com/`.'),
 ('StepSecurity: GitHub OIDC issuance needs the job permission; Azure exchange needs a federated trust; payload only collects the response', UST, ST, 'GitHub OIDC issuance requires the relevant job permission, normally `id-token: write`.'),
 ('StepSecurity: the payload does not itself perform the Azure exchange; static analysis shows attempts not successes', UST, ST, 'static analysis establishes the attempts, not successful issuance or subsequent cloud access'),
 ('Wiz: where an Entra federated credential trusts the workflow, the OIDC tokens can be exchanged for Azure access', UW, W, 'Where an Entra ID federated credential trusts the workflow, these tokens can be exchanged for Azure access, with no stored secret needed.'),
 ('Wiz: stolen managed-identity / exchanged tokens valid up to 24 hours (Wiz claim)', UW, W, 'Stolen managed-identity and OIDC-exchanged tokens are valid for up to 24 hours.'),
 ('Aikido: Azure DevOps OIDC request lacks a serviceConnectionId so the exchange step may fail depending on the pipeline', UAK, AK, "The request here doesn't pass a `serviceConnectionId`, so this step may fail depending on the pipeline"),
]))
A('')
A('Version differences (a real inconsistency across sources): SafeDep says "The rest of the collector is unchanged" for 1.26.2 and gives 31 substrings / 60 files without a version split; StepSecurity says 35 substrings and up to 80 files for 1.26.2 (31 and 60 for 1.26.1); Wiz says 1.26.2 raised the file cap from 60 to 80 and added GitHub-hosted runner paths; Socket lists the 1.26.2 additions (ACTIONS, OIDC, RUNNER, ARM_).\n')
A(table([
 ('SafeDep: rest of collector unchanged in 1.26.2', UD, D, 'The rest of the collector is unchanged.'),
 ('StepSecurity: 35 substrings in 1.26.2, 31 in 1.26.1', UST, ST, 'any variable whose name contains one of 35 substrings in 1.26.2 (31 in 1.26.1)'),
 ('StepSecurity: up to 80 files in 1.26.2, 60 in 1.26.1', UST, ST, 'up to 80 files (60 in 1.26.1)'),
 ('Wiz: file cap 60 to 80 in 1.26.2', UW, W, 'the file cap rose from 60 to 80.'),
]))
A('')

A('### 3.4 Exfiltration, in behaviour terms\n')
A(table([
 ('Socket: collected JSON is zlib-compressed, base64-encoded and POSTed to the webhook (one request)', US, S, 'Collected JSON is zlib-compressed, base64-encoded, and POSTed to the decoded webhook with'),
 ('StepSecurity: one exfiltration attempt, errors suppressed, no retry', UST, ST, 'Each collector makes one exfiltration attempt, suppresses failures, and has no retry loop.'),
 ('Wiz: the destination is a free-tier anonymous webhook.site bin; at most 50 requests were captured (Wiz states it confirmed this)', UW, W, 'We have confirmed the attackers token was on the free tier, and a maximum of 50 requests were captured.'),
 ('SafeDep: proxy/egress logs showing a POST to the destination identify hosts that sent data', UD, D, 'Proxy and egress logs that show a POST to it mark the hosts that sent data.'),
 ('Wiz: status-code reading for a defender (200 accepted; 410/429 suggests rejected)', UW, W, "A 200 means that host's data was accepted. A 410/429 suggests it was rejected."),
]))
A('')

A('### 3.5 Provenance and cause (what is and is not known)\n')
A(table([
 ('SafeDep: how the attacker got publishing access is not known', UD, D, 'How the attacker got publishing access is not known yet.'),
 ('StepSecurity: initial access vector, account/credential and uploader identity not established', UST, ST, "The available evidence does not establish the initial access vector, the specific account or credential used, or the uploader's identity."),
 ('Wiz: root cause unconfirmed', UW, W, "The root cause hasn't been confirmed."),
 ('Wiz: no matching release tag; main branch does not contain the malicious code', UW, W, "and the main branch doesn't contain the malicious code."),
 ('Wiz: 1.26.1 was wheel only (clean releases ship wheel + sdist)', UW, W, '1.26.1 was a wheel only'),
 ('StepSecurity: both bad wheels shipped without a provenance attestation; absence alone does not identify the upload mechanism', UST, ST, 'and had no published provenance attestation.'),
 ('SafeDep: the clean 1.26.0 also has no attestation, so consumers could not tell the uploads apart', UD, D, 'PyPI has no attestation for 1.26.0 either'),
 ('SafeDep: second Microsoft PyPI package with rogue releases in six months (durabletask, stolen API token, May); no evidence of a link', UD, D, 'The payloads and infrastructure share nothing, so there is no evidence the two incidents are linked.'),
 ('OpenSourceMalware: "account compromise is likely" (its assessment)', UOM, OM, 'an account compromise is likely'),
 ('StepSecurity: satellite packages checked had no uploads after 12 Nov (not a blanket finding)', UST, ST, 'had no uploads after November 12 at the time of that check.'),
]))
A('')

A('### 3.6 Telemetry a defender checks (as the sources state it)\n')
A(table([
 ('SafeDep: look for the versions in lockfiles and requirement files', UD, D, 'Look for the versions in lockfiles and requirement files.'),
 ('SafeDep: look for either startup file on machines/images/runners WITHOUT starting that environment\'s Python (starting it re-runs the stealer)', UD, D, 'On machines, images and runners, look for either startup file without starting the environment’s Python. Starting it would run the stealer again.'),
 ('SafeDep: treat everything reachable from an environment that installed either version as exposed', UD, D, 'Treat every secret reachable from an environment that installed either version as exposed.'),
 ('SafeDep: review sign-in and activity logs of managed identities and federated credentials from install time onward', UD, D, 'Review sign-in and activity logs for the managed identities and federated credentials that environment could use, from the install time onward.'),
 ('SafeDep: rotation does not undo tokens already issued', UD, D, 'Rotation does not undo the tokens it had issued.'),
 ('StepSecurity: removing the package alone does not terminate a detached payload process nor establish credentials are safe', UST, ST, 'Removing the package alone does not terminate a detached payload process or establish that credentials are safe.'),
 ('StepSecurity: rotating static secrets does not necessarily invalidate already-issued identity tokens', UST, ST, 'rotating static secrets does not necessarily invalidate already-issued identity tokens'),
 ('Wiz: check proxy and DNS logs and treat a 200 from the capture service as data accepted', UW, W, "A 200 means that host's data was accepted. A 410/429 suggests it was rejected."),
 ('Wiz: for workflows that installed 1.26.2 with id-token: write, treat GitHub OIDC tokens (both audiences) as exposed', UW, W, 'treat GitHub OIDC tokens for `api://AzureADTokenExchange` and https://management.azure.com/ as exposed. Review the Entra ID federated credentials that trust those repositories and workflows'),
 ('Socket: avoid the versions; remove and rotate', US, S, 'Avoid installing either version; if installed, remove them and rotate potentially exposed credentials.'),
 ('SafeDep: pin to the clean version with hashes and hold newer releases until Microsoft confirms clean', UD, D, 'and hold off on any newer release until Microsoft confirms it is clean.'),
]))
A('')

A('### 3.7 Microsoft and PyPI response\n')
A('- PyPI: quarantine of both releases (StepSecurity with timestamps; Wiz "no longer available" by ~21:30Z; SafeDep "removed"); the project page and JSON API show 1.26.0 as the only 1.26 release and latest as of 2026-11-18 ~05:00Z (own check above). OpenSourceMalware alone says the "Microsoft publisher" was quarantined and publishing access is "believed" to remain; StepSecurity says that whether access persists is not established.')
A('- Microsoft: NO statement found. WebSearch (three queries including "Microsoft spokesperson") found no Microsoft or PyPI statement. The microsoft/agent-framework GitHub repository, its security advisories and issues could not be read from this session (GitHub is proxied: `url`, `extract`, `WebFetch` all returned HTTP 404 for github.com/microsoft/agent-framework and its API; `gh` access not enabled), so absence of a GitHub advisory is unverified. Wiz states (not Microsoft) that there is no python-1.26.1 tag or release in the microsoft/agent-framework repository (3.5 table).')
A('- No fixed or newer clean release: PyPI latest is still 1.26.0; no 1.26.3 exists on PyPI (JSON API); SafeDep advises waiting for Microsoft to confirm any newer release.\n')

A('### 3.8 Contradictions with the first pass (item 11) and open gaps\n')
A('- CONFIRMED: affected 1.26.1 and 1.26.2 only; removed from PyPI; 1.26.0 last clean; .pth mechanism; SafeDep flagged 1.26.1 22 minutes after publication and 1.26.2 4 minutes after upload; collects env vars, credential files, /proc environments; requests Azure DevOps federation, managed-identity and (1.26.2) GitHub OIDC tokens; webhook.site exfiltration; about 192,000 downloads a month (SafeDep); durabletask precedent; no Microsoft statement.')
A('- INACCURATE/INCOMPLETE as worded: "collects environment variables matching about 31 name substrings, up to 60 credential files" is the 1.26.1 profile. For 1.26.2, StepSecurity and Wiz give 35 substrings and up to 80 files (SafeDep says the collector is otherwise unchanged and does not split the numbers). Report both versions or say "31 to 35 substrings, 60 to 80 files depending on version (StepSecurity)".')
A('- INACCURATE/INCOMPLETE: the first pass says both versions are "removed"; the more precise state (StepSecurity) is PyPI quarantine at 21:06:16Z (1.26.1) and 21:16:44Z (1.26.2), and 1.26.2 was uploaded 2 min 23 s after the first quarantine. That ordering is the strongest sign the publishing path was still under attacker control.')
A('- ADDED: Wiz, StepSecurity and Aikido are further independent detectors; the first pass named only Socket and SafeDep. Socket published 2026-11-17 (extract metadata date 2026-11-17); SafeDep carries a 2026-11-18 date (page metadata `datePublished 2026-11-18T00:00:00Z`) but its timeline is all 2026-11-17 UTC.')
A('- OPEN: Microsoft and PyPI own statements; GitHub repo/advisory state (unreadable from this session); whether agent-framework siblings (core, foundry, openai, redis, postgres, purview, tools) stayed clean beyond the two spot checks (own PyPI JSON: core and foundry no upload after 2026-11-12; StepSecurity: five other satellites checked no uploads after 2026-11-12); install count; root cause; whether publishing access persists.')
A('- Not a vendor statement, so do not write "Microsoft confirmed": none of the above is Microsoft speaking.\n')
SECTION = '\n'.join(out)
