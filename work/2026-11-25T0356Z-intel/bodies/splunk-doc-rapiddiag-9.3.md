---
title: Using RapidDiag
url: https://help.splunk.com/en/splunk-enterprise/administer/troubleshoot/9.3/contact-splunk-support/using-rapiddiag
hostname: splunk.com
sitename: help.splunk.com
date: "2025-07-04"
fingerprint: ff01fd1443c5052e
language: en
image: https://assets.portal.heretto.com/splunk/25-02-13/splunk-favicon.ico
filedate: "2026-11-25"
---
# Using RapidDiag

The RapidDiag app assists the Splunk Administrator with collecting diagnostic information from one or more Splunk Enterprise instances simultaneously. What makes RapidDiag unique from the `diag` CLI command is the ability to use distributed search to run diagnostic collections across multiple nodes, while leveraging both operating system (OS) provided utilities and Splunk Enterprise tools to collect troubleshooting information.

## When should I use RapidDiag?

RapidDiag offers a way to collect troubleshooting data from OS provided utilities and Splunk Enterprise tools, and place the results into one file. It is designed to ease data collection tasks when working with Splunk Support on troubleshooting your Splunk platform instances.

## What node do I run RapidDiag from?

The RapidDiag app requires distributed search access to other Splunk Enterprise instances. In a typical Splunk Enterprise environment, there are several roles that are configured to search other Splunk Enterprises instances:

- [Monitoring Console](https://docs.splunk.com/Splexicon:Monitoringconsole): The monitoring console is typically configured with search access to the entire Splunk Enterprise deployment. Running a collection from the monitoring console provides access to the search tier, indexers or cluster peers, and management roles such as the cluster manager node.
- [Manager node](https://docs.splunk.com/Splexicon:Managernode): The cluster manager node is configured with search access to the cluster peers. Running a collection from the cluster manager provides access to the cluster peers.
- [Search Head](https://docs.splunk.com/Splexicon:Searchhead): A search head is configured with search access to the indexers or cluster peers. Running a collection from a search head provides access to the indexers or cluster peers.

## How do I access RapidDiag?

The RapidDiag UI is located in the Settings menu, under System > RapidDiag.

The RapidDiag app has several requirements:

- The RapidDiag app is included with Splunk Enterprise 8.1.1 and later.
- The RapidDiag app is available on Linux-based Splunk Enterprise installations only.
- A user must have the `get_diag` capability to access the RapidDiag UI.

### Accessing the internal reference guide

The RapidDiag UI offers a reference guide in product. The Reference Guide tab provides details on folder paths used for common tools, OS tool dependancies, and Linux distribution compatibility. The Reference Guide also includes a dependency checker that verifies the OS utilities used in RapidDiag collections are available on the Splunk platform machines.

### Verify the OS utilities are available

Use the dependency checker on the RapidDiag Reference Guide tab to verify that the OS utilities used in RapidDiag collections are available on your Splunk platform machines.

1. Select a Splunk Enterprise role to run RapidDiag on.
2. Log into SplunkWeb using the Splunk administrator credentials.
3. On the Settings menu, go to System and click RapidDiag.
4. Select the Reference Guide tab, and click Dependency Checker to verify the OS utilities are available on your machines.
       
       Note: The dependency check is also run on any Peer Nodes that are connected to the Splunk Enterprise role where RapidDiag is running.
5. Review the status report:
       
   1. If you receive "No issues with utilities found," the Splunk Enterprise service account was able to access the OS utilities on the machines.
   2. If there are issues with some machines accessing the utilities, a table with the OS utility name and a status will appear. Under each OS utility name, the host machine name and a status message is displayed.

## Using a task template

In RapidDiag, a task template is a series of data collection tasks bundled together and named for their troubleshooting use case. The data collection tasks define the OS utilities and Splunk Enterprise tools used to collect the data. For example, the "File reading" template will generate multiple data collection tasks using the utilities iostat, ps, strace, diag, and others.

A peer node is the Splunk Enterprise instance where you want to perform a data collection task. You must select a peer node before choosing a task template. If the node where you're running RapidDiag is configured to use distributed search across other Splunk Enterprise instances, you can select one or more peer nodes to run a task template on.

### Monitoring a running task

The Task Manager tab in RapidDiag displays the active and historical task collection jobs. Once a collection is finished, you will see the output file path with a custom folder name used to store the data archive on the machine where the collection ran.

When a task collection is run on remote peer nodes, the data is stored on those nodes. RapidDiag does not move or copy the archive files to a central collection point. You must collect the archives from each peer node manually using the output file path reported in the completed task collection.

### A troubleshooting example

Splunk Support has asked you to run the "Indexer health" template on all indexers to assist them in troubleshooting an issue.

1. Select a Splunk Enterprise node to run RapidDiag on. In this case, a search head is ideal as it has distributed search configured to search all of your indexers.
2. Log into SplunkWeb on the search head using the Splunk administrator credentials.
3. On the Settings menu, go to System and click RapidDiag.
4. (Optional) Select the Reference Guide tab, and click Dependency Checker to verify the OS utilities are available on your machines.
5. On the Task Templates tab, select your indexers in the Peer Node dropdown.
6. Choose the "Indexer Health" template. Select "Next."
7. On the Review page, review the settings for the collectors.
8. Select "Start Collecting."
9. On the Task Manager tab, wait for the job status to change from "Collecting" to "Success."
10. Copy the Output File path from the completed collection, and use it to copy the archive files from each indexer to a central location where you'll upload them to a support case.

## Using the command-line interface

The RapidDiag app includes command-line interface (CLI) support and help on single instances only. You can use the CLI to run task templates locally on a Splunk Enterprise instance and upload the outputs to Splunk support cases. You cannot use the RapidDiag CLI for distributed data collection, and there is no support for universal forwarders.

Use the following commands to review the supported settings and optional arguments:

- `splunk cmd rapidDiag -h`
- `splunk cmd rapidDiag upload -h`

When you run `splunk cmd rapidDiag upload`, you can use the optional `--auth` argument to specify your [splunk.com](https://www.splunk.com/) username and password. This argument circumvents the manual login prompt and can be used to automate diag uploads to Splunk support cases.
