---
title: Remote Command Execution in Google Cloud with Single Directory Deletion
url: https://flatt.tech/research/posts/remote-command-execution-in-google-cloud-with-single-directory-deletion/
hostname: flatt.tech
description: Introduction Hello, I’m RyotaK (@ryotkak ), a security engineer at GMO Flatt Security Inc. A while ago, I participated in the Google Cloud VRP bugSWAT, a live hacking event organized by Google. During this event, I discovered a remote command execution vulnerability in one of Google Cloud’s services. As the vulnerability has now been fixed, I would like to share the technical details in this article. TL;DR Google Cloud has a product called Looker, and this product has a feature to manage Git repositories.
sitename: GMO Flatt Security Research
date: "2026-03-23"
categories: ['posts']
tags: ['Security', 'Race Condition', 'Google Cloud', 'Command Injection', 'Git', 'RCE']
fingerprint: "1fa998dd85a553c1"
---
# Remote Command Execution in Google Cloud with Single Directory Deletion

##### Posted on March 23, 2026 • 9 minutes • 1823 words

## Introduction

Hello, I’m [RyotaK](https://ryotak.net)
 ([@ryotkak](https://twitter.com/ryotkak)
), a security engineer at GMO Flatt Security Inc.

A while ago, I participated in the [Google Cloud VRP bugSWAT,](https://bughunters.google.com/blog/5364401980899328/hardening-google-cloud-insights-from-the-latest-cloud-vrp-bugswat)
 a live hacking event organized by Google.

During this event, I discovered a remote command execution vulnerability in one of Google Cloud’s services. As the vulnerability has now been fixed, I would like to share the technical details in this article.

## TL;DR

Google Cloud has a product called Looker, and this product has a feature to manage Git repositories.

When a user deletes a directory, Looker improperly validates the target directory, making it possible to delete the directory containing the repository itself. Since other Git operations can be performed concurrently, it was possible to trigger Git-related operations during the directory deletion process.

By exploiting this race condition, an attacker could execute arbitrary commands on the Looker server.

While instances were isolated using Kubernetes, misconfigurations in the Looker service account permissions could allow privilege escalation to access other instances within the same Kubernetes cluster.

After reporting the vulnerability to Google, they fixed both the remote command execution vulnerability and the privilege escalation vulnerability.

## About Looker

Looker is a business intelligence (BI) and data analytics platform that is part of Google Cloud. It enables organizations to explore, analyze, and visualize their data through interactive dashboards and reports. Looker connects to various data sources, allowing users to create custom data models and perform analytics.

Looker has two types of the deployment, cloud-hosted and self-hosted. Since I could obtain the self-hosted Looker instance for the Google Cloud VRP bugSWAT event, I focused on reverse engineering the self-hosted Looker.

## Technical Details

### Git Integration in Looker

Looker provides a feature to manage model files called LookML in Git repositories (Looker calls them projects). Users can pull or push changes to Git repositories, and Looker applies the changes accordingly.

To integrate with external Git services, Looker typically uses the JGit library (a pure Java implementation of Git). However, when the remote Git repository is configured over SSH, Looker uses the native Git command-line tool instead of JGit.

It creates the checked-out repository under a specific directory on the Looker server and executes Git commands against that directory.

```
      def self._cli_git_command(working_directory, command_words)
        [...]
              command_with_dir = "cd #{working_directory} && #{command}"
              Looker::Log.log_block_latency(:git, "_cli_git_command: command: #{command_with_dir}") do
                Open3.capture3(command_with_dir)
              end
        [...]
```
In addition to standard Git operations, Looker has a feature to manage files from the Web UI. Users can create, edit, and delete files or directories from the Looker interface.

### Improper Validation in Directory Deletion

When a user deletes a directory, Looker executes the following code:

```
    post("/api/internal/projects/:project_id/delete_dir") do |_project_id|
      [...]
        dir_path_array = body["dir_path_array"]
        @project.delete_dir(dir_path_array)
      [...]
```
```
      def delete_dir(dir_path_array)
        dir_name = dir_path_array.reject(&:empty?).join("/")
        dir_name = validate_dir_name(dir_name)
        dir_path = File.join(path, dir_name)
        [...]
        FileUtils.rm_rf(dir_path)
```
The `validate_dir_name` method ensures that reserved directories cannot be tampered with:

```
      def validate_dir_name(dir_name)
        [...]
        if path_array.include?(Looker::Model::Project::DOT_GIT)
          raise(InvalidFileNameError.new("New path cannot include .git"))
        else
          nil
        end
        File.join(path_array.map do |s|
          Looker::Utils.sanitize_file_or_dir_name(s)
          HellToolJava
        end)
      end
```
Since it’s possible to trick Git into using forged Git configurations if the `.git` directory is corrupted or deleted, the `validate_dir_name` method checks if the directory to be deleted includes `.git` and raises an error if it does.

For example, consider a repository with the following structure:

```
--- .git directory (Can't be controlled by the user) ---
.git/
    HEAD
    config
...
--- worktree (Controllable by the user) ---
HEAD
config
objects/
refs/
```
If the `.git` directory is deleted, the next Git command executed against this repository will fail to find the `.git` directory and will look for Git configurations in the worktree directory instead.

Therefore, if the worktree contains files that resemble the contents of a `.git` directory, Git commands will use those configurations.

For instance, if the following configuration is placed as a `config` file in the worktree and the `.git` directory is deleted, the `fsmonitor` hook will be triggered and the `whoami` command will be executed when running `git status` or similar commands:

```
[core]
        bare = false
        worktree = "."
        fsmonitor = "whoami"
```
Let’s return to the `validate_dir_name` method. It properly checks if the directory to be deleted includes `.git`:

```
      def validate_dir_name(dir_name)
        [...]
        if path_array.include?(Looker::Model::Project::DOT_GIT)
          raise(InvalidFileNameError.new("New path cannot include .git"))
        else
          nil
        end
        File.join(path_array.map do |s|
          Looker::Utils.sanitize_file_or_dir_name(s)
          HellToolJava
        end)
      end
```
However, this check fails to catch the case where `dir_name` is `/`.

After the `validate_dir_name` method returns, the `delete_dir` method constructs the full path to delete by joining the base path and the `dir_name`:

```
      def delete_dir(dir_path_array)
        dir_name = dir_path_array.reject(&:empty?).join("/")
        dir_name = validate_dir_name(dir_name)
        dir_path = File.join(path, dir_name)
        [...]
        FileUtils.rm_rf(dir_path)
```
So, specifying `dir_path_array` as `["/"]` results in `dir_name` being `/`, and the full path to delete becomes the repository directory itself.

That said, even if an attacker can delete the entire repository directory, the attack described above requires forged Git configuration files to be present in the worktree. This means the attack isn’t possible if the entire repository is deleted.

…Or is it?

### Internals of FileUtils.rm\_rf

The `FileUtils.rm_rf` method is a Ruby standard library method that recursively deletes files and directories.

Tracing through its internals reveals the following code:

```
  def remove_entry(path, force = false)
    Entry_.new(path).postorder_traverse do |ent|
      begin
        ent.remove
      rescue
        raise unless force
      end
    end
```
As shown, it uses the `Entry_.postorder_traverse` method to traverse the directory tree in post-order (processing all children of a directory before processing the directory itself).

What happens if we trick Looker into deleting a directory in the repository that contains thousands of files and subdirectories?

Indeed, it takes considerable time to delete all the files and directories. If we can trigger deletion of such a directory after the `.git` directory is deleted but before the entire repository deletion is complete, we still have a chance to execute Git commands against the partially deleted repository.

### Controlling Deletion Order

The `Entry_.postorder_traverse` internally uses the `Dir.children` method to list directory contents, which uses the `readdir` system call to read directory entries.

```
while ((dp = READDIR(dirp->dir, dirp->enc)) != NULL) {
  const char *name = dp->d_name;
  [...]
```
Since the order of entries returned by `readdir` depends on the filesystem implementation and can vary, there’s no guarantee about the order in which files and directories are processed during deletion.

Fortunately from an attacker’s perspective, the entry order returned by `readdir` is somewhat deterministic on ext4 filesystems. This allows attackers to influence the deletion order through careful directory naming.

So, I was able to “spray” directory names as follows to determine which directory name would ensure the `.git` directory is processed first during deletion:

```
.git/
aaa/
aab/
    dir1/
        file1
        file2
        file3
        ...
    dir2/
        file1
        file2
        file3
        ...
    ...
    dir10000/
        ...
aac/
...
ccb/
ccc/
```
By placing many files and directories under a specific directory and measuring the time until the repository becomes unavailable after triggering the deletion, I could find the optimal directory name to have the `.git` directory deleted first, creating a window to trigger Git operations against the partially deleted repository.

### Remote Command Execution

Now that we can control the timing of `.git` directory deletion, we can attempt to execute arbitrary commands on the Looker server.

The attack steps are:

1. Create a Git repository with a worktree containing forged Git configurations to execute arbitrary commands using the `fsmonitor` hook.
2. Create a directory with a random name containing many files and subdirectories, then attempt to delete the repository itself using the `POST /api/internal/projects/:project_id/delete_dir` API.
3. Measure the time until the repository becomes unavailable. If the time is long, return to step 2 (this indicates the `.git` directory wasn’t deleted first).
4. Once the optimal directory name is found, prepare the repository again and continuously hit endpoints that trigger Git operations (e.g., `git status`). In my tests, 1 req/sec was sufficient.
5. Hit the `POST /api/internal/projects/:project_id/delete_dir` API to delete the repository directory. This will delete the `.git` directory first, but completing the deletion of the large directory takes time.
6. At this point, Git operations triggered in step 4 will attempt to use the partially deleted repository, causing the Git configuration from the worktree to be used and executing arbitrary commands.

I used the following Git configuration to test command execution:

```
[core]
        bare = false
        worktree = "."
        fsmonitor = "echo \"$(whoami) $(uname -a)\" > ../output/pwned.model.lkml"
```
Once `git status` is executed during repository deletion, the `whoami` and `uname -a` commands are executed, and the output is written to `../output/pwned.model.lkml`, which is another repository I can access normally.

### Privilege Escalation Against Other Looker Instances

At this point, I asked the Google Cloud team if I could investigate the vulnerability’s impact further, and they kindly granted permission.

Shortly after gaining a reverse shell on the Looker instance, I noticed the instance was isolated in Kubernetes pods, limiting the impact on other Looker instances.

However, upon inspecting the Kubernetes service account credentials mounted at `/var/run/secrets/kubernetes.io/serviceaccount`, I found excessive permissions:

```
{
  "kind": "SelfSubjectAccessReview",
  "apiVersion": "authorization.k8s.io/v1",
  [...]
  "spec": {
    "resourceAttributes": {
      "namespace": "looker",
      "verb": "update",
      "resource": "secrets"
    }
  },
  "status": {
    "allowed": true,
    "reason": "RBAC: allowed by RoleBinding..."
  }
}
```
The Looker service account had permission to update secrets in the `looker` namespace, which was shared across multiple Looker instances.

Since read permission for secrets wasn’t granted, I couldn’t read existing secrets directly, making safe testing difficult. Without read access, I couldn’t back up existing secrets before modification, which meant any updates would be irreversible and could potentially break other Looker instances. This limitation prevented me from demonstrating the full impact without risking production systems.

Therefore, I shared this finding with the Google Cloud team for further investigation.

After investigation, they confirmed it was possible to escalate privileges to access other instances in the same Kubernetes cluster by abusing this permission, and classified the vulnerability as S0.

As of the time of publishing this article, both the remote command execution vulnerability and the privilege escalation vulnerability have been fixed by the Google Cloud team.

## Conclusion

In this article, I shared the technical details of a remote command execution vulnerability in Google Cloud’s Looker product, discovered during the Google Cloud VRP bugSWAT event.

While the vulnerability stemmed from a small validation mistake in directory deletion, proper exploitation made remote command execution possible. This vulnerability highlights the importance of proper input validation—even small mistakes can lead to severe security issues.

I would like to thank the Google Cloud security team for hosting the Google Cloud VRP bugSWAT event and for their quick response and support during the vulnerability disclosure process.

## Shameless Plug

At GMO Flatt Security, we provide top-notch penetration testing for a wide range of targets, including Web, Mobile, Cloud, LLM, and IoT.

[https://flatt.tech/en/professional/penetration\_test](https://flatt.tech/en/professional/penetration_test)

We also developed Takumi, our AI security engineer. Built by world-class offensive security experts, Takumi brings human-level reasoning to application security. Using a hybrid AI-powered SAST/DAST approach, it audits your code and live apps to uncover everything from classic vulnerabilities to logic flaws like broken authentication and authorization — all validated through safe exploit simulations for near-zero false positives.

Based in Japan, we work with clients globally, including industry leaders like Canonical Ltd.

If you’d like to learn more, please contact us at [https://flatt.tech/en](https://flatt.tech/en)
