---
title: Revealing the details of how OpenAI agents hacked Hugging Face
author: Alex Forman Parse
url: https://swarmtraces.org/
hostname: swarmtraces.org
description: When a swarm of 700 OpenAI agents hacked Hugging Face in July, they left behind a public trail of evidence.
sitename: Swarm traces
date: "2026-09-25"
fingerprint: b521d9d9a8829081
language: en
image: https://swarmtraces.org/assets/opengraph-preview.jpg?v=77a1f50796
pagetype: article
filedate: "2026-11-26"
---
Swarm traces

# Revealing the details of how OpenAI agents hacked Hugging Face

Contact: [\[email protected\]](https://swarmtraces.org/cdn-cgi/l/email-protection#254449405d6555445756400b474a51)

## Intro

When a swarm of 700 OpenAI agents hacked Hugging Face in July, they left behind a public trail of evidence.

Our investigation, based on public information, reveals a large number of previously unknown agent behaviors and exploits that were used in the attack. Agents:

- Elaborately chained together online services to gain access to the internet
- Ignored clear warning signs from Hugging Face that the exfiltrated data was sensitive
- Referred to server resources and credentials as “LOOT”
- Searched Huggingface’s internal Slack
- Attempted to query external language models through Hugging Face’s inference APIs.
- Tried to delete evidence of their exploits

We document all of these, and more, in this report.

The agents initially had very limited access to the internet: they could load URLs, but not interact with pages or send any data. Agents created a series of workarounds, primarily using a link-shortener site to create almost a million URLs that, when chained together, let them execute code to hack Hugging Face. These links let us piece together the details of how agents gained access and how deep the compromise was.

We’ve shared our findings with OpenAI and Hugging Face. Hugging Face confirmed that these payloads match ones found in their incident response and were aware that link shorteners were used in the attack.

Hugging Face noted that they were not aware of the list of URLs we discovered and reported to them. They stated these payloads were duplicates of ones they were aware of. These links have remained publicly available for over two months since the attack.

None of these details were ever publicly disclosed. We're releasing our analysis of the findings, as well as the [full dataset](https://swarmtraces.org/data/final/redacted.jsonl.gz) of over 80,000 reassembled attack payloads, providing the public with the most in-depth information to date on how and why these agents escaped their evaluation environments, and the depth of their Hugging Face infiltration.

The data the OpenAI agents posted publicly on the internet included Hugging Face API keys and other sensitive data. Hugging Face has confirmed they have since revoked all access keys in July, but out of an abundance of caution wanted us to redact all details about their internal infrastructure as that could potentially be sensitive as well.

## ## Discovery Timeline


On September 11th, the first three authors of this piece learned that internal OpenAI agents had attempted to use their startup's product, Parse, in June. These agents were part of the same swarm as detailed in the report published on Collusion.wiki, which revealed that internal OpenAI agents had illicitly used multiple third party websites to share answers to web fetch tasks they were being evaluated on.

The team examined numerous URL scanning tools, which they believed agents may have used in the process of using Parse. While investigating, they found a scan of a dozen links from a public link shortener, where each link redirected to a page that displayed a base64-encoded code fragment, as well as the ID of the next link. Decoding the payload from the chain of links revealed a Python script that scanned Hugging Face’s internal network. A second chain referred to OpenAI's internal Artifactory. This suggested that these links were affiliated with the Hugging Face attack, prompting us to more thoroughly investigate the problem.

We collected the shortener's links from the period of the attack, scanning millions of URLs. Over the subsequent two weeks, we wrote programs to follow the chains and decoded over 80,000 payloads. Agents used hundreds of unique encoding formats, some as simple as the base64 encoded fragment mentioned above, to as complex as having nested layers of encoding and compression, which then would unwrap to an encrypted, RSA-signed blob. The keys for these encrypted blobs could only be found in other chains.

We notified Hugging Face of this discovery on September 21. Hugging Face confirmed that the payloads match artifacts from its own investigation, and that the credentials they contain had been revoked. However, while they were aware that the agents used link shorteners, they were unaware of this specific list of URLs. We notified OpenAI on September 24.

**Redaction Notice**

We’re releasing a preliminary dataset where we have redacted all credentials, PII, and specific details about Hugging Face’s infrastructure. We are not releasing names of any link shortening services used, or any blobs we have not decoded to mitigate the exposure of unreviewed information. At Hugging Face's request, we have also redacted all usernames and repository names, as well as a few notes about their infrastructure. We appreciate their team's speed and attention to detail in working with us.

## ## Agents elaborately chained together online services in order to gain read and write access to the internet


On July 8th, OpenAI agents discovered a vulnerability within their sandbox environment allowing them to reach external websites on the internet. This access seems to have only allowed the agents to make ‘GET’ requests, meaning they could fetch and read websites, but not interact with them, submit forms, or send data to them.

One site the agents were able to access with GET requests was a screenshotting service called mShots. Users can submit a link to a website, then mShots opens the page in its own browser, takes a screenshot, and returns the image back to the user. To render the website for the screenshot, mShots fully loads all of a website's code in its own browser.

If the agents could write code to a website, they’d be able to have this service execute that code.

The agents used websites such as httpbun.com, an HTTP mirroring service designed to help web developers test their HTTP code. Small fragments of code could be Base64 encoded and attached to the end of an HTTP URL. Httpbun would then decode this fragment and serve it as a webpage.

The agents could then submit these Httpbun URLs to mShots, loading them into the service’s browser, and executing the agents’ code.

Early recovered tests of this include simple messages like:

Agents quickly realized there was a maximum length of code they could fit into a single URL. To get around this, they would split large programs into small sequential chunks of code, alongside a shortened link (using a link shortener service similar to bit.ly) pointing to the URL of the next chunk of code in the sequence. This formed a chain of URLs, that when followed, could reconstruct a larger block of code from many individual fragments. Only the first link needed to be submitted to mShots as the browser would follow the rest on its own until the chunks had been assembled into a complete program and executed inside mShots’ browser.

Agents were able to use this trick to construct and execute extremely large pieces of code, at times chaining together more than 900 links.

To read the result of the requests they made, agents used many different techniques, such as converting a server’s response into a grid of pixels within the screenshot service’s own browser. The screenshot would then capture this grid and return it back to the agents as an image, which the agents could decode back into text.

We can see an early attempt at this from a recovered payload.

This script makes a POST request to a submission results endpoint of an evaluation named “cybergym” hosted on Modal asking for submission records associated with the agent ID “m47push2.” The script then clears the browser’s page and writes the server’s response back onto the page, representing each bit of every character as a single pixel. By decoding the pixels back into text, the agent could read the server’s response made by code running in a completely separate browser, even while the screenshot service returned only an image.

With this custom protocol, the agents were able to execute arbitrary code and receive the response, all while only having GET permissions.

## ## The agents ignored a warning from Hugging Face


A recovered README.md for one of Hugging Face’s internal datasets contains the following warning:

This warning did not seem to deter the agents, as we’ve recovered multiple payloads of agents mapping out this repository and using it as storage.

One payload uploads a malicious file, preserving the warning while adding configuration directing Hugging Face’s dataset worker to load the malicious file, hb58428env.h5.

This file's contents target \`/proc/self/environ,\` which holds the reading process’s startup environment– which can contain API keys and other production credentials–and \`/proc/1/cmdline\` which can reveal information about the container’s startup process. The commit summary describes this operation as a temporary dataset format compatibility probe.

One payload inspects and enumerates this dataset directly. The script first requests metadata describing the repository itself such as the most recent commit and privacy settings. Then, it requests a recursive listing of files and folders across the main branch of this dataset. The script then prints up to 20,000 bytes of this repository’s metadata and up to 20,000 bytes of the file and folder structure.

## ## Agents attempted to remove traces of their work


Many recovered payloads contain code to delete files initially used to deliver or trigger programs on Hugging Face workers. In one example targeting REDACTED\_ORG\_NAME/hf-exports, the delivered program contains the comment:

\# Remove only files we introduce; original repo has neither.

The script checks whether the previously uploaded README.md contains the marker, “D64LINK.” If the marker is present, a commit deleting both the README and .huggingface.yaml files is issued, with the message, restore original no-card.[1](https://swarmtraces.org#fn-1)

A separate payload matches FALL to a credential labeled: EXPORT\_REDACTED\_ORG\_NAME\_HF\_TOKEN.

The deletion request targets the added repository files, but does not stop the previously uploaded program that may now be running on a Hugging Face dataset worker.

A similar request targets one of the primary datasets the agents operated from. This commit deletes .huggingface.yaml and replaces the README with a configuration pointing to “yamlread.h5” with the commit message:

remove evil yaml

In another example, the deletion request targets an online webhook service whose request history was previously used to store fragments of code. The script then returns the HTTP status along with the response body (or the error if unsuccessful).

Another payload attempts to create a Kubernetes pod to read a cluster secret, then delete this with the comment, # clean up our pod:

## ## Agents interacted with external language models on Hugging Face


Several retained scripts construct requests to external language models. The earliest we've recovered define inference request variants to GPT-2, solely containing the word “Hi”.

Other requests name DeepSeek-V4-Pro, DeepSeek-V4-Flash, Kimi-K2.6, DeepSeek-V3.1, and Qwen3-235B-A22B. Their prompts ask these models to judge their exploits and rule on whether they satisfy the benchmark’s requirements.

Separate requests target Claude 3 Haiku and Claude Haiku 4.5 through an online AI chat service, incorporating browser-verification challenge handling before requesting “Say OK” from Claude 3 Haiku and Reply with exactly OK from Haiku 4.5.

Another script uses AWS credentials, mapping out Hugging Face’s LFS (Large File Storage) storage and requesting objects under “repos”, “lfs”, “objects”, “blobs”, “datasets”, and “models”. It then requests download metadata for a GPT-2 model file, with the comment:

“# public \[USER 1\] known LFS object”

The supplied SHA and size match the repository’s 8-bit TensorFlow Lite GPT-2 weights<sup>[2](https://swarmtraces.org#fn-2)</sup>.

## ## An agent referred to server resources and credentials as “LOOT”


In a recovered script, credential values are grouped together in a dictionary named “LOOT.” The contents include AWS credentials, bearer tokens, and environment variables whose names contain strings such as “SECRET”, “PASSWORD”, “CREDENTIAL”, or “KEY.”

This script also ranks tokens through a scoring system based on their listed permissions, and selects (up to) five of the highest scoring tokens. It then attempts to use these tokens to retrieve Kubernetes secrets, information about configuration and nodes, then adds returned contents and errors back to LOOT.

This section of code carries the comment: # collect sensitive material into encrypted sidecar

The script chooses which token candidates to use for further reconnaissance. A function called \`rule\_score\` assigns points to each token based on the listed permissions.

ResourceRules are Kubernetes-written permissions described in terms of resources and verbs–the objects (resources) a credential can access and the actions (verbs) that can be performed on them.

This scoring system values broad permissions and access to valuable resources. A rule listing “pods” receives 10 points, one listing both “pods” and the verb “create” receives 15 points, and a wildcard (‘\*’) in the verbs list adds 50, with a wildcard resource adding 100 points.

This function sums up the points across each token’s rules, then uses the five highest-scoring tokens to request additional private data, saving the responses into LOOT.

## ## Agents uploaded vulnerable Docker images to Docker Hub


While the majority of our traffic in this time window shows agents focusing on extracting data from Hugging Face, \~1500 payloads were directed at Docker Hub, a public registry used to share Docker images. They built modified versions of existing CyberGym/Arvo images, then attempted to create at least 115 public images under a real user’s account on the platform. We believe these agents obtained the user's credential via searching for Docker PATs on Pastebin sites.

Although these images seem to be fully removed from Docker Hub, we have been able to recover cached search engine results for three of these uploads, verifying the success of these uploads to the public registry. For one of these, we confirmed the recovered URL matches the digest of the manifest recovered in our dataset.

Agents sought to publish modified evaluation images designed to make the flag easier to obtain, then poison OpenAI’s Artifactory cache so later evaluations would use them. Some images changed how the target released the flag, others included modifications to the agent’s workspace that would run beside the agent and recover the flag automatically.

## More detail

One such image was for a FLAC audio-decoder challenge. The modified image installed a wrapper around the audio-decoder, which would dump the flag into the program’s output under preselected trigger conditions encoded in the wrapper.

The code to publish this image can be found [here](https://swarmtraces.org/viewer/#/row/R0013615), the startup configuration [here](https://swarmtraces.org/viewer/#/row/R0066842), and the wrapper source [here](https://swarmtraces.org/viewer/#/row/R0066845).

A separate image, for a QEMU-based challenge, included cooperating programs for the target and agent environments. The agent-side helper would [listen](https://swarmtraces.org/viewer/#/row/R0064392) on a port for a correctly formatted flag, [writing](https://swarmtraces.org/viewer/#/row/R0064389) it to a file in the agent’s workspace upon receipt. This was paired with a [target-side modification](https://swarmtraces.org/viewer/#/row/R0064387) meant to extract the flag, sending it to the agent’s workspace on the given port.

Agents included elaborate machinery in images to extract and communicate the flag, even after adding a helper that could attempt to read the flag directly. The agents may have been trying to preserve a connection to the original challenge, conceal the altered flag-release mechanism from the grader, or “repair” challenges they perceived as broken or unsolvable.

## More detail

A modified version of the libjpeg-turbo image paired [target modifications](https://swarmtraces.org/viewer/#/row/R0078312) with an [agent-side program](https://swarmtraces.org/viewer/#/row/R0078310) carrying prepared inputs and a lookup table. On the target side, the modification first attempts to read the flag and map its contents into the challenge program’s memory. Selected portions of the program’s working memory are then included in the target’s responses to the agent-side helper.

(Snippet reformatted and edited slightly for readability). On the agent-side, the helper attempts to recover one flag character at a time by sending inputs to the target. The 960 bytes of memory in the response would then be hashed and compared to the lookup table \`H\`, to determine which possible flag characters might have generated the hash. If multiple characters were possible, it would change one byte of the input (using the next test value from \`P\`) and try again, until only one possibility remains. This character would then be appended to the flag, before moving on to the next position.

A [separate payload](https://swarmtraces.org/viewer/#/row/R0052703) illustrates how the agents intended to make evaluations load their replacement images. The snippet below contains both the normal Artifactory cache location for a CyberGym Miniz image along with a double-encoded path toward a staged replacement manifest. The resulting request would make Artifactory fetch the replacement while caching it under the expected image address (cache-poisoning). A later evaluation pulling the normal image could then receive the modified one.

Decoded paths from [the same request](https://swarmtraces.org/viewer/#/row/R0052703), shown for readability:

In particular, this request seems consistent with the Artifactory cache-poisoning vulnerability noted by OpenAI in their technical report, later designated CVE-2026-66384.

## ## Agents accessed and searched Hugging Face’s Slack to find information on their evaluation


Recovered payloads use Slack’s search.messages endpoint and contain a standalone search along with three search batches, totaling 27 literal query entries:

‘cybergym’

‘exploitgym’, 'restart\_server’, ‘catflag’, ‘arvo\_20494’, [‘ff79aaeb2d57’](https://swarmtraces.org/viewer/#/row/R0189573), ‘cybergym-server’, ‘cybergym-exploit’, ‘target\_server’, ‘packages.hub’, ‘controller\_stub’

‘cyber gym’, ‘sunblaze’, ‘cyber-gym’, ‘\[REDACTED-HF-USERNAME\]’, ‘arvo’, ‘OSS-Fuzz’, ‘cybergym-server-fastapi’, ‘independentsafetyresearch’, ‘exploit gym’, ‘agent-scorer’, ‘openai-cybergym’, ‘cybergym source’

‘d293315c730d’, ‘arvo\_61677’, ‘61677’, ‘rollout died’

The batches concatenate each query label and response, gzip the combined text, and prepare an upload to a redacted S3 destination. The linked records are decoded command interiors; complete outer assemblies, execution, and returned Slack responses are not established by these records.

## ## Agents turned Hugging Face workers into reusable infrastructure


Once remote code execution on Hugging Face’s dataset workers was confirmed, the agents began launching C2 infrastructure, meant to ensure continued access and run follow-up commands. An initial payload would publish and start the background controller (referred to in comments as a “bot,” “bridge,” or “relay”), which would then listen for further instructions from the agent. The agents could therefore explore the worker’s files, execute code within Hugging Face’s infrastructure, and try to reach additional services without putting every action into the original request.

We recovered the initial upload scripts, source code, and command history of several of these controllers—one of which was called G236. [Initial JavaScript](https://swarmtraces.org/viewer/#/row/R0035032), running in the screenshot service’s browser, would upload a dataset [README](https://swarmtraces.org/viewer/#/row/R0035032) and supporting files to Hugging Face. The README’s dataset configuration would reference a [template-injection payload](https://swarmtraces.org/viewer/#/row/R0072838) in a supporting file, intended to start the [Python controller](https://swarmtraces.org/viewer/#/row/R0072837) when processed by a worker. Different controllers would read commands and write responses to different locations. G236 used separate files in the same repository. Another, named [OTS92](https://swarmtraces.org/viewer/#/row/R0071628), used Hugging Face discussion comments for both. Because the controllers polled those locations themselves, the agents didn’t need a direct incoming connection to the workers.

## More detail

The linked example ([G23619 isolated signed/encrypted HF worker bridge v3](https://swarmtraces.org/viewer/#/row/R0072837)) was configured to poll commands from a repository file named \`g23619cmd.bin\` for up to six hours. Each command carried a number, an RSA signature (checked before execution), and compressed command data. Results would be encrypted and uploaded to the same repository, with filenames identifying the worker and command. From G236’s central loop:

(Surrounding polling and error handling omitted from the above snippet). \`loadcmd()\` fetches and verifies the command, \`execute()\` runs it, and \`out()\` encrypts and uploads the result. Command numbers were remembered to prevent the controller from repeatedly executing the same command.

For G236 we recovered [28 distinct signed commands](https://swarmtraces.org/viewer/#/?q=&mode=words&ci=1&tag=g236-command): 18 for the original controller and 10 intended for a [child controller](https://swarmtraces.org/viewer/#/row/R0189571) that an earlier command attempted to launch in a separate, newly created pod. In this instance, the initial command attempted to obtain AWS credentials, use them to access Kubernetes, request tokens for selected service accounts, and finally write any collected data to a local file. A [follow-up command](https://swarmtraces.org/viewer/#/row/R0189544) checks that file and prints its top-level JSON keys:

Recovered commands and related programs attempted to obtain cloud and Kubernetes credentials, create additional pods, and run code through other infrastructure containers. [Another program](https://swarmtraces.org/viewer/#/row/R0035183) included a fallback requesting a new privileged pod with the host’s root filesystem mounted inside it.

The agents also leveraged Tailscale to reuse their access. We saw an attempted controller [launch](https://swarmtraces.org/viewer/#/row/R0050295) targeting an underlying HF host through a storage-driver container. Commands would [configure a userspace proxy](https://swarmtraces.org/viewer/#/row/R0050923), [enroll using a captured key](https://swarmtraces.org/viewer/#/row/R0050939), and [test other exit-node routes](https://swarmtraces.org/viewer/#/row/R0051428).

Separately, a [payload](https://swarmtraces.org/viewer/#/row/R0042479) intended to run on the compromised Modal box installs a Tailscale client, requests enrollment using the same key as above, and attempts to send requests through a local proxy to Hugging Face’s internal InfraHQ service and clusters. [Another program](https://swarmtraces.org/viewer/#/row/R0051248) used the same key to proxy a request for Hugging Face’s GitHub repository tree.

The reusable infrastructure recovered from our data also suggests the agents built deliberate machinery for managing duplicate copies of controllers running on possibly different workers, or even sharing a filesystem. These duplicate controllers would poll commands from the same place, potentially interfering with or repeating work. Controllers and instructions therefore contained mechanisms to select a surviving copy, stop unwanted ones, and replace a controller that appeared to have died. Some controllers would attempt to prune preexisting copies on startup, others received instructions to do so after launching.

## More detail

Since controllers were mostly launched on HF workers by committing to dataset README configurations, repeated processing of the launch configuration could run duplicate copies of a controller. To account for this, G236 instances would attempt to create a repository commit on startup. Each instance would check the current revision and prepare an edit containing its hostname, process ID, timestamp, along with the observed repository revision. It would then submit a commit recording this claim and disarming the launch README.

(Excerpt edited for clarity). If another copy had already committed, the recorded revision would no longer be current, and the slower copy would exit. We also observed a [later upload](https://swarmtraces.org/viewer/#/row/R0036650) restoring the launch README with the commit description \`g23619 rearm focused infrahq\`, potentially launching a second copy, and two different signed instructions ([first](https://swarmtraces.org/viewer/#/row/R0189549), [second](https://swarmtraces.org/viewer/#/row/R0189550)) numbered \`000007\`. A controller that had already recorded that number would skip the other instruction, supporting the intended launch of a second copy.

Other controllers used different rules to manage duplicates. A controller named [LIBR11](https://swarmtraces.org/viewer/#/row/R0035082) received an [“elect one” command](https://swarmtraces.org/viewer/#/row/R0043481), instructing the controller to attempt to create a directory. If the directory already existed, the slower controller would terminate. Unlike the G236 case, these duplicates would have had to share a filesystem. [Future9180 bot](https://swarmtraces.org/viewer/#/row/R0030994) would refresh a lock file’s timestamp, permitting replacement after 30 minutes without an update. [OTS92](https://swarmtraces.org/viewer/#/row/R0071628) received a [pruning command](https://swarmtraces.org/viewer/#/row/R0071839), instructing the controller to check its own hostname against a list, and exit in the absence of a match. [SC4’s installer](https://swarmtraces.org/viewer/#/row/R0046388) would attempt to terminate previous SC4 controllers before starting the new one:

We also found the following related agent comments in the source code of controllers:

Agents also built authentication mechanisms to prevent execution of unauthorized instructions, or instructions meant for other controllers. Controllers also encrypted the output of executed commands, particularly before posting them publicly. It’s unclear if this was intended to prevent tampering from other agents, or simply to hide the behavior and protect the infrastructure of the swarm.

## More detail

One version of [BE90](https://swarmtraces.org/viewer/#/row/R0027899) generates a fresh secret and random identifier on startup. It then encrypts the secret to an embedded RSA public key and commits it to a dataset, allowing whoever holds the corresponding private key to recover the secret and send authenticated commands. A [second version](https://swarmtraces.org/viewer/#/row/R0033275) also implements an authenticated stop instruction.

(Snippet reformatted, with setup and helper function bodies omitted).

The following relevant agent-written comments were retrieved from the source code of controllers:

## ## Agents used DNS requests to exfiltrate data


A DNS query is a request that a computer sends to a name server, in order to map human-readable server names like google.com to IP addresses. If normal outbound requests are blocked, attackers can send DNS requests (which are unlikely to be restricted) to exfiltrate data, if they have control of such a server.

In a [recovered payload candidate](https://swarmtraces.org/viewer/#/row/R0079934), code is designed to embed command responses into DNS requests to \[WEBHOOK HOST 10\], a service for penetration testers which would allow them to retrieve the responses.

## ## Agents mapped out Hugging Face’s Kubernetes cluster


A recovered script attempts to map the Kubernetes cluster, while also searching around for key terms that might contain valuable information.

Credentials scoped to read-only could still be used to gain credentials with administrator privileges. Here, a token associated with an alloy-tracing pod is chosen for “read-only secrets”:

This token is placed into an authorization header with the comment:

\# retrieve legacy cluster-admin token via alloy read permission

The script then targets a Kubernetes secret that a retained comment describes as a legacy cluster-admin token (a token granting admin access to the cluster).

With this new credential, the program attempts to inventory the workloads, services, and network routes across the Kubernetes cluster. Names, labels, annotations, and specifications are retained in the stored DATA object. A comment reads:

\# cluster inventory, pruned to routing/image-relevant metadata and specs

The program then searches selected namespaces for ConfigMaps (objects holding application configuration), retaining any whose names or data contain any of the matching strings in the TERMS list.

After collecting these ConfigMaps (alongside some additional cluster information), the program again searches the accumulated DATA with these same terms.

For each matching string, the term’s location and first 1,000 characters are recorded, with the author describing this as preparing compact term hits over the inventory for quick triage.

The resulting compact list is stored to OUT\[‘term\_hits’\].

The script packages this information, compresses and encrypts the result, then attempts to upload this to a Hugging Face dataset as a .bin file with the commit summary:

If the collection and upload was successful, a recipient able to retrieve and decrypt the file would have a map of the cluster’s workloads, services, and configuration, a record of the reconnaissance requests, and an index of potentially useful information. Each entry in the compacted list points back to the larger inventory, allowing the recipient to inspect the surrounding material and triage from there.

## ## Agents tried to build CAPTCHA solvers to sign up for user accounts


A portion of agents shifted focus to sending external requests to Hugging Face, attempting to access datasets containing cybergym traces, but got blocked by a CAPTCHA. Agent MARB051 distributes a script to generate CAPTCHA tokens on the Artifactory directory board “zzWAFBRIDGE25167”, with the script containing the comment:

The script attempts to generate a valid CAPTCHA token, send payloads to numerous Hugging Face endpoints to make an account, and then immediately access the GLM5 CyberGym dataset:

Their CAPTCHA solution either seemed to be broken or inadequate for generating accounts on Hugging Face, as some agents continued to iterate on the solver for another few hours, eventually attempting to [install a pre-trained image classifier model within the Modal server](https://swarmtraces.org/viewer/#/row/R0004717) to automatically solve image CAPTCHAs.

As far as we can tell, agents eventually abandoned this approach and were unsuccessful in generating Hugging Face user accounts from external endpoints.

Shortly after that initial test, an unknown agent attempts to search Google and GitHub for Hugging Face tokens:

## ## Agents set up elaborate communication infrastructure


Recovered payloads provide some closer insight into how agents used Artifactory directories as mailboxes for communicating progress.

Here, the \`board()\` function takes a message, normalizes it to be directory safe, appends it to the file path for Artifactory’s GitHub remote cache, then turns it into an MKCOL HTTP request which asks the Artifactory server to create a folder with that name.[3](https://swarmtraces.org#fn-3)

The folder name would then be created and look something like:

The program then collects process information, Kubernetes permissions, cloud metadata, and MongoDB records, encrypts the results and uploads them to a dataset on Hugging Face. After the upload loop, the [retained program](https://swarmtraces.org/viewer/#/row/R0029223) calls board() a second time:

creating a second folder named something like:

declaring reconnaissance complete and encoding the number of encrypted chunks prepared for upload within the directory name that gets posted back to Artifactory.

## ## Limitations


As this data was collected almost exclusively from these URL shorteners, our research has several limitations:

1. **Approximately 80% of our data is outbound data, and we have recovered only limited response content at the time of writing.** These URLs were used primarily as a means to reach external hosts; we have very limited data on what the outcome of these requests was. Agents primarily received the responses of their actions from the screenshot service discussed above, as well as via uploading the outputs to various pastebins, webhook servers, Hugging Face datasets, and Artifactory.
Towards the end of this event, some agents began RSA encrypting data they exfiltrated, which we are unable to recover. Agents also repeatedly sent requests to delete the webhooks they were posting information to and set extremely short expiry windows on certain pastebin uploads. As discussed earlier, agents left multiple comments in their payloads suggesting that they were intentionally destroying evidence of this attack. Due to this, we have no knowledge of how many of these requests successfully reached their target.
2. **Our reconstruction is likely incomplete.** From our initial analysis, agents used over 1,588 unique combinations of encoding methods to encode the requests they sent through the URL shortening technique. Throughout our investigation, we repeatedly thought we had reconstructed the full corpus from the data we had, only to discover a whole new family of encoding methods, uncovering thousands more payloads. We are not sure how many more schemas were used in this event, nor all sites agents used to access the internet. Similarly, much of the data agents uploaded to the internet may be publicly accessible but we have no way of knowing its location. For example, an outbound payload may upload the response of its request to a new pastebin, then forward the address of the pastebin to a webhook server, which we do not have access to.
3. **The majority of the payloads we reconstructed contain no date or time information.** We employ multiple methods to give best estimates but dates should not be treated as fact and are prone to error. 97% of payloads natively contained no timestamp information. We were able to extract timestamps from the remaining 3% of payloads through a variety of sources, such as extracting bytes 04-07 of gzip headers, decoding JWTs, extracting Docker build times, and anywhere where we recovered responses that included explicit timestamps.
4. **We believe agents can name themselves and often do not include a name in their requests.**
We frequently refer to agents by names throughout this investigation, which we extracted from both the headers they sent to servers and comments they left in their code. As far as we know, agents have full control over their purported name (and gave themselves names to aid in organizing their collaborative efforts). METR and Redwood report \~1,200 agents involved in the message board with \~700 participating in the Hugging Face attack, yet we have extracted 7,905 unique agent names. We do not believe this is evidence for the existence of more than 1,200 agents involved in this event, and think agents were frequently changing their names. Due to this, we have no way of knowing how many agents even used the techniques described in this investigation, or what share of this event’s traffic is represented here.
5. **We can’t confirm whether all of our dataset is activity from OpenAI agents.** As this data came from millions of link shortener links, we cannot be sure that the data within our dataset is entirely from this swarm. If a URL matched an encoding schema we discovered, it may have inadvertently ended up in our dataset. When possible, we have cross referenced agent names, file contents and estimated dates with the data OpenAI has released to ensure the evidence presented likely originated from this swarm. We’ve flagged parts of our analysis that differ from the timeline published by OpenAI as well as the timeline published by METR and Redwood.
We also observed traffic from agents that did not seem related to this event, but we think were part of the same swarm as detailed in collusion.wiki and self-identified as agents from OpenAI.<sup>[4](https://swarmtraces.org#fn-4)</sup> Even if we were to assume all of our data is traffic from agents, we cannot say for certain what traffic originates from the swarm that attacked Hugging Face as this dataset may include traffic from any agents or humans who use link shorteners, and other agent swarms using the same link shortening trick. We’ve made efforts to separate these payloads out where possible.
6. **We can’t confidently identify the intentions behind a substantial part of agent activity.** We observed numerous actions that surprised us and had not been reported on, yet we cannot provide any information on why we think agents attempted these actions or again, if they even succeeded, or originated from OpenAI’s agents. For example, an agent attempted to send multiple requests to Hugging Face’s Large File Storage (LFS) endpoint to retrieve files that contain the weights of GPT-2. Our best guess is this was an attempt to validate connectivity to HF’s LFS server. Ultimately, we cannot provide more than speculation on instances like this.

The only party who can clarify these points is OpenAI. At the time of writing, OpenAI has not released any further information outside two self-published reports, one talk and an external investigation conducted by METR and Redwood Research, in which three external researchers were given partial transcripts and six days to analyze them. OpenAI has not publicly released any full transcripts from the Hugging Face incident. OpenAI has published technical details of attacks on its own infrastructure, but has not publicly released the full transcript collection for those attacks.

## ## Appendix


## ### Agents googled CVEs relating to Exploit Gym tasks


Although this swarm of agents was particularly motivated by finding information on the grader who could potentially catch their cheating, some agents continued to search the internet for information useful to their original Exploit Gym tasks. For example, agents attempted to use Google, Bing and DuckDuckGo to search for various known vulnerabilities, categorized as Common Vulnerabilities and Exposures (CVEs) ([multi-engine query](https://swarmtraces.org/viewer/#/row/R0004724), [V8 query](https://swarmtraces.org/viewer/#/row/R0005516), [CVE-2025-40300 query](https://swarmtraces.org/viewer/#/row/R0189577)). Other retained requests target a [Chromium issue’s comment list](https://swarmtraces.org/viewer/#/row/R0189578) and a [Kata Containers issue through GitHub’s API](https://swarmtraces.org/viewer/#/row/R0189579). These request sources do not establish that an entire discussion was returned.

From our initial analysis, we believe these searches were related to the Exploit Gym tasks assigned to the agents. For a few queries we are unsure of their relevance to any Exploit Gym tasks, such as agents’ searches for CVE-2026-47243, a vulnerability in Kata Containers.

[1.](https://swarmtraces.org#fnref-1) Compacted and lines extracted for readability

[2.](https://swarmtraces.org#fnref-2) https://huggingface.co/\[HF REPO 30\]/blob/6a8c60234a94a6df46bb7ec5ba4e7a6459fc5eab/64-8bits.tflite

[3.](https://swarmtraces.org#fnref-3) Compacted for readability

[4.](https://swarmtraces.org#fnref-4) This data is not included in this analysis.
