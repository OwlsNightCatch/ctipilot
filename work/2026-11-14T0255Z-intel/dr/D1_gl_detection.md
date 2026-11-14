---
schema: 1
offering: [self-managed]
tier: [free, premium, ultimate]
log_sources: [gitaly, sidekiq]
cves:
  - id: CVE-2026-105437
    ranges_source: patch-release
    affected:
      - {from: "16.2", before: "19.3.8"}
      - {from: "19.4", before: "19.4.6"}
      - {from: "19.5", before: "19.5.4"}
    fixed_in: ["19.3.8", "19.4.6", "19.5.4"]
    advisory_url: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-4-released/
    last_verified: "2026-11-12"
    note: "The CVE record lists Git versions, not GitLab versions; the GitLab ranges come from the patch release. Self-compiled installs must also patch the Git at git.bin_path (Git 2.56.1 or later, or a distro-patched build)."
primary: true
sample_source: mixed
scenarios: [compromised-instance]
cicd_techniques: [cicd.initial_access.systems_with_unpatched_vulnerabilities]
---

# About

This detection watches for a `git merge-tree` child process ended by a memory fault. It fires when the `error` field of a Gitaly event contains `merge-tree: signal:` followed by anything other than `killed` or `terminated`, for example `merge-tree: signal: segmentation fault`. A fallback rule reads the same text from `exception.message` of the failed Sidekiq job.

Gitaly runs `git merge-tree` when GitLab checks whether a merge request can be merged or lists its conflicts. CVE-2026-105437 is a heap-based buffer overflow in Git, rated critical, that is reachable in that step by any user who can create a project and open a merge request. The out-of-bounds heap writes can be used to execute arbitrary commands in the Gitaly environment. Events appear in the Gitaly log (`/var/log/gitlab/gitaly/current`) and the Sidekiq log (`/var/log/gitlab/sidekiq/current`) and can be forwarded to a SIEM with your log shipper.

This rule is for self-managed GitLab CE and EE instances on an affected version: 16.2 and later before 19.3.8, 19.4 before 19.4.6, and 19.5 before 19.5.4. GitLab.com and GitLab Dedicated are already patched. Retire it once the instance runs a fixed version and the patched Git is confirmed. The threshold is one event, because a healthy `git merge-tree` never ends with a memory fault and normal merge conflicts are reported without a signal. The rule sees the crash, a side effect of a failed attempt, and not the flaw itself. A hit is strong evidence of an attempt; a clean result does not prove that the flaw was not used.

## Understanding The Threat

### Technical Details/Impact

Git sizes a merge result in one pass and writes it in a second. In the affected versions the size is a signed 32-bit integer ([CWE-190](https://cwe.mitre.org/data/definitions/190.html)), so a large enough result wraps to a small value, Git allocates that, and the second pass writes past it ([CWE-122](https://cwe.mitre.org/data/definitions/122.html)). The repository controls both the size and the content.

On GitLab, a user pushes the prepared branches to a project they own and opens a merge request. `MergeRequestMergeabilityCheckWorker` asks Gitaly for `UserMergeToRef` and the merge request page asks for `ListConflictFiles`; both run the bundled `git merge-tree`. No administrator or second user is involved.

In a lab reproduction on GitLab CE 19.4.1, opening one merge request left this within a second and a half:

| Log | What it recorded | Sigma rule |
|---|---|---|
| Gitaly | Three error events with the signal text in `error`: one `UserMergeToRef` and two `ListConflictFiles`, one called from the web process and one from Sidekiq. | Yes |
| Sidekiq | One failed `MergeRequestMergeabilityCheckWorker` job with the same text in `exception.message`. The retry 21 seconds later finished normally. | Yes |
| Kernel log | One `git[<pid>]: segfault ... in libc.so.6` line for each Git child process. | No, corroboration |
| Workhorse, NGINX | The push only, with status 200. | No |
| `production_json.log`, `api_json.log`, `exceptions_json.log` | No event with the crash text in the files that were collected. | No |

`production_json.log` can also record the crash, as a 500 with `Gitlab::Git::CommandError`, when someone loads a page that lists conflicts, such as the merge request diffs page. That was seen in a development environment only, so it is in the Raw Log Query and not in a Sigma rule.

The signal varies: `segmentation fault` was captured on Linux, `bus error` was seen on macOS, and `aborted` is expected but was not captured. The rules match any signal except `killed` and `terminated`, which mean that Gitaly or a memory limit stopped the child.

What the rules do not cover:

- An attempt that does not fault. A working attempt is silent, so the crashes are the failed ones.
- An attempt stopped by a memory limit (`signal: killed`). The Raw Log Query has a broader search that includes it.
- A memory fault in a Git command other than `merge-tree`.
- Versions other than 19.4.1. The rules depend on the wording of Gitaly's error text, which was captured on 19.4.1 only.
- GitLab.com and GitLab Dedicated, where these logs are not available to customers.

### Business Impact

- Arbitrary command execution in the Gitaly environment, as the `git` operating system user, by any authenticated user who can create a project.
- Read and write access to every repository stored on that Gitaly node.
- Failed mergeability checks and merge request pages for the affected project while the attempts run.
- Regulatory, contractual and reputational exposure following a breach.

## Logs

The primary signal is in the Gitaly log: `/var/log/gitlab/gitaly/current` on a Linux package (Omnibus) install, the standard output of the `gitaly` container on Helm. The fields are `error` (the signal text), `grpc.method` (`UserMergeToRef` or `ListConflictFiles`), `grpc.request.glProjectPath` and `grpc.request.glRepository` (the project), `target_ref` (`refs/merge-requests/<iid>/merge`, on `UserMergeToRef` only), `caller_id` and `correlation_id`.

The fallback signal is in the Sidekiq log: `/var/log/gitlab/sidekiq/current` on a Linux package install, the standard output of the `sidekiq` container on Helm, `log/sidekiq.log` on a source install. The failed job carries `class`, `job_status` `fail`, `exception.class`, `exception.message`, `args` (the merge request id) and the `correlation_id` of its Gitaly events.

- Many installations do not ship these two logs by default; check that yours does. No tier or add-on is required.
- The crash events carry no user name. The user is found through the project and the merge request (see Response).
- The project path is chosen by the user who created the project.
- Gitaly writes `error` as a plain string. A pipeline whose schema treats `error` as an object, such as the Elastic Common Schema, renames it or fails to index it, so check which field holds the text in your SIEM.

### Sample Event Logs

<details>
<summary>Gitaly UserMergeToRef: the mergeability check's merge-tree child ended by a segmentation fault (lab capture on 19.4.1, sanitised) [match: GitLab Gitaly git merge-tree child process crash (CVE-2026-105437)]</summary>

```json
{"caller_id":"MergeRequestMergeabilityCheckWorker","component":"gitaly.UnaryServerInterceptor","correlation_id":"5c1d0f4a9b7e4d21a6f3c8e2b47d9a10","error":"merge-tree: signal: segmentation fault","grpc.meta.auth_version":"v2","grpc.meta.client_name":"gitlab-sidekiq","grpc.meta.method_operation":"mutator","grpc.meta.method_scope":"repository","grpc.meta.method_type":"unary","grpc.method":"UserMergeToRef","grpc.request.deadline":"2026-11-10T18:49:54.151","grpc.request.fullMethod":"/gitaly.OperationService/UserMergeToRef","grpc.request.glProjectPath":"example-group/example-project","grpc.request.glRepository":"project-42","grpc.request.repoPath":"@hashed/73/47/73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049.git","grpc.request.repoStorage":"default","grpc.service":"gitaly.OperationService","grpc.start_time":"2026-11-10T12:49:54.151","level":"error","msg":"unable to create merge commit","pid":2685,"source_sha":"8f2b6c1d4e7a9035b6c8d1e2f3a4b5c6d7e8f901","span.kind":"server","system":"grpc","target_ref":"refs/merge-requests/7/merge","target_sha":"1a2b3c4d5e6f708192a3b4c5d6e7f8091a2b3c4d","time":"2026-11-10T12:49:54.476Z"}
```

</details>

<details>
<summary>Gitaly ListConflictFiles: the conflict listing of the same job ended the same way (lab capture on 19.4.1, sanitised) [match: GitLab Gitaly git merge-tree child process crash (CVE-2026-105437)]</summary>

```json
{"caller_id":"MergeRequestMergeabilityCheckWorker","command.count":3,"command.cpu_time_ms":314,"command.inblock":0,"command.majflt":0,"command.maxrssanon_bytes":210690048,"command.minflt":2697,"command.oublock":0,"command.real_time_ms":316,"command.spawn_token_fork_ms":0,"command.system_time_ms":42,"command.user_time_ms":272,"component":"gitaly.StreamServerInterceptor","correlation_id":"5c1d0f4a9b7e4d21a6f3c8e2b47d9a10","error":"couldn't find conflict: merge-tree: signal: segmentation fault","error_metadata":{"exit_status":-1},"grpc.code":"Internal","grpc.meta.auth_version":"v2","grpc.meta.client_name":"gitlab-sidekiq","grpc.meta.method_operation":"accessor","grpc.meta.method_scope":"repository","grpc.meta.method_type":"server_stream","grpc.method":"ListConflictFiles","grpc.request.deadline":"2026-11-10T18:49:54.812","grpc.request.fullMethod":"/gitaly.ConflictsService/ListConflictFiles","grpc.request.glProjectPath":"example-group/example-project","grpc.request.glRepository":"project-42","grpc.request.payload_bytes":209,"grpc.request.repoPath":"@hashed/73/47/73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049.git","grpc.request.repoStorage":"default","grpc.response.payload_bytes":0,"grpc.service":"gitaly.ConflictsService","grpc.start_time":"2026-11-10T12:49:54.812","grpc.time_ms":318.872,"level":"error","msg":"finished streaming call with code Internal","pid":2685,"span.kind":"server","system":"grpc","time":"2026-11-10T12:49:55.131Z"}
```

</details>

<details>
<summary>Sidekiq: the mergeability check job failed with the Gitaly error (lab capture on 19.4.1, sanitised and trimmed: database and Redis counters removed, backtrace cut to five frames) [match: GitLab Sidekiq job failed on a git merge-tree crash (CVE-2026-105437)]</summary>

```json
{"severity":"WARN","time":"2026-11-10T12:49:55.141Z","retry":3,"queue":"default","args":["7"],"class":"MergeRequestMergeabilityCheckWorker","jid":"3fa1c27d9e5b40c8a1d6e2f7","created_at":"2026-11-10T12:49:53.882Z","meta.feature_category":"code_review_workflow","correlation_id":"5c1d0f4a9b7e4d21a6f3c8e2b47d9a10","meta.caller_id":"NewMergeRequestWorker","meta.root_caller_id":"NewMergeRequestWorker","enqueued_at":"2026-11-10T12:49:53.894Z","pid":1789,"message":"MergeRequestMergeabilityCheckWorker JID-3fa1c27d9e5b40c8a1d6e2f7: fail: 1.242561 sec","job_status":"fail","gitaly_calls":3,"gitaly_duration_s":0.695939,"worker_id":"sidekiq_0","duration_s":1.242561,"completed_at":"2026-11-10T12:49:55.140Z","exception.class":"GRPC::Internal","exception.message":"13:couldn't find conflict: merge-tree: signal: segmentation fault. debug_error_string:{INTERNAL:couldn't find conflict: merge-tree: signal: segmentation fault}","exception.backtrace":["lib/gitlab/gitaly_client/conflicts_service.rb:35:in `any?'","lib/gitlab/gitaly_client/conflicts_service.rb:35:in `conflicts?'","lib/gitlab/git/repository.rb:1157:in `can_be_merged?'","app/services/merge_requests/mergeability_check_service.rb:48:in `execute'","app/workers/merge_request_mergeability_check_worker.rb:28:in `perform'"]}
```

</details>

<details>
<summary>Gitaly UserMergeToRef: the closing event of the same call, which reports the failed merge without the signal (lab capture, sanitised) [no-match]</summary>

```json
{"caller_id":"MergeRequestMergeabilityCheckWorker","command.count":5,"command.cpu_time_ms":314,"command.inblock":0,"command.majflt":0,"command.maxrssanon_bytes":210898944,"command.minflt":3436,"command.oublock":16,"command.real_time_ms":320,"command.spawn_token_fork_ms":0,"command.system_time_ms":45,"command.user_time_ms":269,"component":"gitaly.UnaryServerInterceptor","correlation_id":"5c1d0f4a9b7e4d21a6f3c8e2b47d9a10","error":"Failed to create merge commit for source_sha 8f2b6c1d4e7a9035b6c8d1e2f3a4b5c6d7e8f901 and target_sha 1a2b3c4d5e6f708192a3b4c5d6e7f8091a2b3c4d at refs/merge-requests/7/merge","grpc.code":"FailedPrecondition","grpc.meta.auth_version":"v2","grpc.meta.client_name":"gitlab-sidekiq","grpc.meta.method_operation":"mutator","grpc.meta.method_scope":"repository","grpc.meta.method_type":"unary","grpc.method":"UserMergeToRef","grpc.request.deadline":"2026-11-10T18:49:54.151","grpc.request.fullMethod":"/gitaly.OperationService/UserMergeToRef","grpc.request.glProjectPath":"example-group/example-project","grpc.request.glRepository":"project-42","grpc.request.payload_bytes":396,"grpc.request.repoPath":"@hashed/73/47/73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049.git","grpc.request.repoStorage":"default","grpc.response.payload_bytes":0,"grpc.service":"gitaly.OperationService","grpc.start_time":"2026-11-10T12:49:54.151","grpc.time_ms":329.092,"level":"warning","msg":"finished unary call with code FailedPrecondition","pid":2685,"span.kind":"server","system":"grpc","time":"2026-11-10T12:49:54.481Z"}
```

</details>

<details>
<summary>Gitaly ListConflictFiles: merge-tree child killed by Gitaly at the call deadline (constructed from the captured event) [no-match]</summary>

```json
{"caller_id":"MergeRequestMergeabilityCheckWorker","command.count":3,"command.cpu_time_ms":314,"command.inblock":0,"command.majflt":0,"command.maxrssanon_bytes":210690048,"command.minflt":2697,"command.oublock":0,"command.real_time_ms":30011,"command.spawn_token_fork_ms":0,"command.system_time_ms":42,"command.user_time_ms":272,"component":"gitaly.StreamServerInterceptor","correlation_id":"b7e4d2195c1d0f4aa6f3c8e2b47d9a22","error":"couldn't find conflict: merge-tree: signal: killed","error_metadata":{"exit_status":-1},"grpc.code":"Internal","grpc.meta.auth_version":"v2","grpc.meta.client_name":"gitlab-sidekiq","grpc.meta.method_operation":"accessor","grpc.meta.method_scope":"repository","grpc.meta.method_type":"server_stream","grpc.method":"ListConflictFiles","grpc.request.deadline":"2026-11-10T13:05:12.401","grpc.request.fullMethod":"/gitaly.ConflictsService/ListConflictFiles","grpc.request.glProjectPath":"example-group/example-project","grpc.request.glRepository":"project-42","grpc.request.payload_bytes":209,"grpc.request.repoPath":"@hashed/73/47/73475cb40a568e8da8a045ced110137e159f890ac4da883b6b17dc651b3a8049.git","grpc.request.repoStorage":"default","grpc.response.payload_bytes":0,"grpc.service":"gitaly.ConflictsService","grpc.start_time":"2026-11-10T13:04:42.401","grpc.time_ms":30017.224,"level":"error","msg":"finished streaming call with code Internal","pid":2685,"span.kind":"server","system":"grpc","time":"2026-11-10T13:05:12.418Z"}
```

</details>

<details>
<summary>Sidekiq: the retry of the same job finished normally (lab capture, sanitised and trimmed) [no-match]</summary>

```json
{"severity":"INFO","time":"2026-11-10T12:50:16.574Z","retry":3,"queue":"default","args":["7"],"class":"MergeRequestMergeabilityCheckWorker","jid":"3fa1c27d9e5b40c8a1d6e2f7","created_at":"2026-11-10T12:49:53.882Z","meta.feature_category":"code_review_workflow","correlation_id":"5c1d0f4a9b7e4d21a6f3c8e2b47d9a10","meta.caller_id":"NewMergeRequestWorker","meta.root_caller_id":"NewMergeRequestWorker","enqueued_at":"2026-11-10T12:50:16.540Z","retry_count":0,"pid":1789,"message":"MergeRequestMergeabilityCheckWorker JID-3fa1c27d9e5b40c8a1d6e2f7: done: 0.033145 sec","job_status":"done","worker_id":"sidekiq_0","duration_s":0.033145,"completed_at":"2026-11-10T12:50:16.574Z"}
```

</details>

## Detection

_TLDR Detections are written in [Sigma](https://sigmahq.io/) format_

There are two rules, one for each log, and each stands on its own. The Gitaly rule is primary; the Sidekiq rule is a fallback at a lower level that reports the same event. Both match `merge-tree: signal:` and exclude `killed` and `terminated`. The gRPC method, status code and calling worker are in `fields` for triage and are not conditions, because the same crash is logged under two methods, with and without a status code. One opened merge request produces several events, so group alerts by `grpc.request.glRepository` or `correlation_id`. If your pipeline stores events under a prefix, adjust the field names.

```yaml
title: GitLab Gitaly git merge-tree child process crash (CVE-2026-105437)
id: 0fb0abe0-6c89-4106-bfa2-b8d78212cdc7
status: experimental
description: Detects a Gitaly event where a git merge-tree child process was ended by a memory fault, such as a segmentation fault, on self-managed GitLab instances. This is the crash left by a failed attempt to exploit the Git heap buffer overflow CVE-2026-105437. An attempt that does not crash is not seen.
references:
    - https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-4-released/
    - https://cwe.mitre.org/data/definitions/122.html
    - https://cwe.mitre.org/data/definitions/190.html
    - https://docs.gitlab.com/administration/logs/#gitaly-logs
author: signals-engineering@gitlab.com
date: 2026-11-10
tags:
    - attack.initial_access
    - attack.execution
    - attack.impact
    - attack.t1190
    - attack.t1499.004
    - cve.2026-105437
    - gitlab.selfmanaged
logsource:
    product: gitlab
    service: gitaly
    category: application
detection:
    selection:
        error|contains: 'merge-tree: signal: '
    filter_stopped_from_outside:
        error|contains:
            - 'merge-tree: signal: killed'
            - 'merge-tree: signal: terminated'
    condition: selection and not filter_stopped_from_outside
fields:
    - time
    - error
    - grpc.method
    - grpc.code
    - grpc.request.glProjectPath
    - grpc.request.glRepository
    - grpc.request.repoStorage
    - target_ref
    - caller_id
    - grpc.meta.client_name
    - correlation_id
falsepositives:
    - A Git defect that crashes merge-tree on an ordinary repository. The same project then crashes on every check. Still report it.
    - Failing memory or storage on the Gitaly node. Other Git commands and other projects crash too.
    - Events replayed from a backup or test log. Confirm that the host and the timestamp are live.
level: critical
---
title: GitLab Sidekiq job failed on a git merge-tree crash (CVE-2026-105437)
id: 6e8990ae-0943-4d4c-b6e8-5f6e75b59488
status: experimental
description: Detects a Sidekiq job that failed because a git merge-tree child process was ended by a memory fault, on self-managed GitLab instances. Fallback for the Gitaly rule (CVE-2026-105437) where the Gitaly log is not collected; it reports the same event.
references:
    - https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-4-released/
    - https://cwe.mitre.org/data/definitions/122.html
    - https://cwe.mitre.org/data/definitions/190.html
    - https://docs.gitlab.com/administration/logs/#sidekiq-logs
author: signals-engineering@gitlab.com
date: 2026-11-10
tags:
    - attack.initial_access
    - attack.execution
    - attack.impact
    - attack.t1190
    - attack.t1499.004
    - cve.2026-105437
    - gitlab.selfmanaged
logsource:
    product: gitlab
    service: sidekiq
    category: application
detection:
    selection:
        exception.message|contains: 'merge-tree: signal: '
    filter_stopped_from_outside:
        exception.message|contains:
            - 'merge-tree: signal: killed'
            - 'merge-tree: signal: terminated'
    condition: selection and not filter_stopped_from_outside
fields:
    - time
    - class
    - job_status
    - exception.class
    - exception.message
    - args
    - jid
    - meta.caller_id
    - correlation_id
falsepositives:
    - The same causes as for the Gitaly rule. Tell them apart in the Gitaly and kernel logs.
    - Events replayed from a backup or test log. Confirm that the host and the timestamp are live.
level: high
```

### Raw Log Query

For a self-managed instance without a SIEM. Paths are for a Linux package install; `zgrep` reads current and rotated files. Run searches 1, 3 and 5 on the Gitaly nodes and 2 and 4 on the Sidekiq and Rails nodes.

```bash
GITALY=/var/log/gitlab/gitaly
SIDEKIQ=/var/log/gitlab/sidekiq
RAILS=/var/log/gitlab/gitlab-rails

# 1. Gitaly: merge-tree child ended by a memory fault (the Sigma rule)
zgrep -h 'merge-tree: signal: ' "$GITALY"/* | grep -vE 'merge-tree: signal: (killed|terminated)'

# 2. Sidekiq: the job that failed because of it (the second Sigma rule)
zgrep -h 'merge-tree: signal: ' "$SIDEKIQ"/* | grep -vE 'merge-tree: signal: (killed|terminated)'

# 3. Kernel log of the Gitaly node (the host or Kubernetes node; optional). One line for each crashed Git child:
#    git[8258]: segfault at 55a8037ed000 ... error 6 in libc.so.6[...]
dmesg -T | grep -E 'git\[[0-9]+\]: segfault'
journalctl -k --since '-7 days' | grep -E 'git\[[0-9]+\]: (segfault|trap|general protection)'

# 4. Rails: a web request that hit the same crash (500 with the Gitaly error text)
zgrep -h 'merge-tree: signal: ' "$RAILS"/production_json.log* "$RAILS"/exceptions_json.log*

# 5. Broader: every merge-tree child ended by any signal, including killed, counted by project
zgrep -h 'merge-tree: signal: ' "$GITALY"/* \
  | grep -o '"grpc.request.glProjectPath":"[^"]*"' | sort | uniq -c | sort -rn
```

### Atomic Test

`git merge-tree` cannot be made to fault safely, so this test checks the pipeline and not the vulnerability: it writes one synthetic event with the same `error` text into the Gitaly log of a test instance. It does not involve Git or any GitLab request.

#### Warnings

- Run only on a non-production instance.
- Do not reproduce a real crash with a prepared repository. That is live exploitation and corrupts memory on the Gitaly node.
- Tell your detection team first, and remove the synthetic line afterwards.

#### Test Steps

Append a synthetic event to the Gitaly log on the test instance:

```bash
NOW=$(date -u +%Y-%m-%dT%H:%M:%S.000Z)
printf '%s\n' '{"level":"error","msg":"ATOMIC-TEST synthetic marker","error":"merge-tree: signal: segmentation fault","grpc.method":"UserMergeToRef","grpc.request.glProjectPath":"example-group/atomic-test","grpc.request.glRepository":"project-0","correlation_id":"atomic-test","time":"'"$NOW"'"}' \
  >> /var/log/gitlab/gitaly/current
```

Confirm that the line is in the log:

```bash
grep 'ATOMIC-TEST' /var/log/gitlab/gitaly/current | tail -1
```

The line must produce one `GitLab Gitaly git merge-tree child process crash` alert.

To test the Sidekiq rule, append a line with `"exception.message":"13:couldn't find conflict: merge-tree: signal: segmentation fault."` and the same marker to `/var/log/gitlab/sidekiq/current`. It must produce one `GitLab Sidekiq job failed on a git merge-tree crash` alert.

The rules themselves were checked against the captured crash events under Sample Event Logs.

#### Cleanup

- Remove the synthetic `ATOMIC-TEST` lines from the logs, and from any downstream index if your SIEM allows it.
- Annotate or close the test alerts.
- Document all actions taken.

## Response

Follow your organization's documented incident response procedures. Treat a hit as an attempt at remote code execution on the Gitaly node until shown otherwise. Take these steps in order:

1. Initial Assessment
   - Read `error`: `segmentation fault`, `bus error` or `aborted` after `merge-tree: signal:` is a memory fault in the Git child process.
   - From the Gitaly event take `grpc.request.glProjectPath`, `grpc.request.glRepository` (`project-<id>`), `correlation_id` and, on `UserMergeToRef`, `target_ref` (`refs/merge-requests/<iid>/merge` names the merge request). From the Sidekiq event take `args` (the merge request id) and `correlation_id`.
   - Count the hits for that project. Events within two seconds are one opened merge request. Crashes spread over minutes or hours, each after a merge request was opened or reopened, are repeated attempts.

2. Investigation
   - Find the user from the request that created the merge request, which carries `username`, `user_id` and `remote_ip`. The lab capture did not include this request, so confirm the field values on your own instance.
     - `production_json.log`: a `POST` with `controller` `Projects::MergeRequests::CreationsController` whose `path` starts with the project path.
     - `api_json.log`: a `POST` whose `path` is `/api/v4/projects/<id>/merge_requests`, with `<id>` from `grpc.request.glRepository`.
   - Search both logs for that `username` and `remote_ip`: when the account and the project were created, and what else they did.
   - If you have access to the kernel log of the Gitaly node, confirm one `git[<pid>]: segfault` line for each event at the same second. A clean kernel log does not clear the node.
   - Look at the repository without merging it. A `.gitattributes` file in the target branch that sets `conflict-marker-size` to an unusually large value supports a true positive; an ordinary repository does not set it.
   - Look at what the user did to the project before the first hit: pushes, uploads and other requests from the same `username` in `production_json.log` and `api_json.log`.
   - Hunt on the Gitaly node for the attempt that did not crash. The overflow gives a write as the `git` user, so anything that user can write is in scope. Start with these places; the list is not complete:
     - a file named `rc`, or any other new file, in the `.ssh` directory of the `git` user (`/var/opt/gitlab/.ssh/` on a Linux package install);
     - files or two-character directories directly under `/var/opt/gitlab/gitaly/` that are not part of Gitaly;
     - processes started by `sshd` as `git` that are not `gitlab-shell`;
     - new cron entries or outbound connections for the `git` user.

3. Containment
   - Block the account and revoke its tokens and SSH keys. Close the merge request, which stops further mergeability checks, and make the project inaccessible. Keep a copy of the bare repository as evidence before you delete anything.
   - Preserve the Gitaly, Sidekiq, Rails and kernel logs of the window before any restart.
   - If you find any sign of code execution, treat the instance and every repository on that Gitaly node as compromised: rotate the secrets in `gitlab-secrets.json`, CI/CD variables, runner tokens and access tokens.

4. Prevention
   - Upgrade to 19.5.4, 19.4.6 or 19.3.8, or later. The fix is a patch to Git, and the official Linux packages and container images include it. These versions have no new migrations.
   - On a self-compiled installation, also rebuild the Git embedded in Gitaly and the Git at `git.bin_path`, or upgrade a distribution Git to 2.56.1 or later. The patch release post has the steps.
   - Until then, limit who can create projects and sign up, where your use of the instance allows it.
   - Ship the Gitaly and Sidekiq logs to your SIEM, and the kernel log of the Gitaly nodes if you can.
   - Group repeat alerts for the same `grpc.request.glRepository` within an hour, so that one opened merge request is one alert and repeated attempts stay visible as a count.

### References

- [GitLab Critical Patch Release: 19.5.4, 19.4.6, 19.3.8](https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-5-4-released/)
- [CWE-122: Heap-based Buffer Overflow](https://cwe.mitre.org/data/definitions/122.html)
- [CWE-190: Integer Overflow or Wraparound](https://cwe.mitre.org/data/definitions/190.html)
- [GitLab Gitaly logs](https://docs.gitlab.com/administration/logs/#gitaly-logs)
- [GitLab Sidekiq logs](https://docs.gitlab.com/administration/logs/#sidekiq-logs)
- [Git attributes: conflict-marker-size](https://git-scm.com/docs/gitattributes#_conflict_marker_size)
- [MITRE ATT&CK T1190: Exploit Public-Facing Application](https://attack.mitre.org/techniques/T1190)
- [MITRE ATT&CK T1499.004: Application or System Exploitation](https://attack.mitre.org/techniques/T1499/004)