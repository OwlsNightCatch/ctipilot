---
title: Secure Splunk Enterprise services with pass4SymmKey
url: https://help.splunk.com/en/splunk-enterprise/administer/manage-users-and-security/10.6/secure-distributed-and-clustered-splunk-environments/secure-splunk-enterprise-services-with-pass4symmkey
hostname: splunk.com
sitename: help.splunk.com
date: "2026-09-09"
fingerprint: "33c9dddc40e583c8"
language: en
image: https://assets.portal.heretto.com/splunk/25-02-13/splunk-favicon.ico
filedate: "2026-11-25"
---
# Secure Splunk Enterprise services with pass4SymmKey

Splunk provides a security key that lets various components of your Splunk Enterprise deployment authenticate securely with one another. This security key, known as the pass4SymmKey, can increase security between:

- Search head and indexer cluster managers and nodes
- Deployment servers and clients
- License managers and peers

You can use a pass4SymmKey in addition to using TLS certificates to secure communications between various Splunk Enterprise instances and services. TLS certificates provide authentication between the Splunk daemon, while the pass4SymmKey provides for authentication between individual Splunk services on the instances.

When you set up specific services on two or more Splunk Enterprise instances, you assign the same pass4SymmKey to each instance to enable the authentication between those services. In some cases, you can set the key using Splunk Web. You can always configure the key using the server.conf configuration file.

Pass4SymmKeys control authentication between services on Splunk platform instances. They do not manage user access to any instance.

## General procedure for configuring a pass4SymmKey

Depending on the Splunk Enterprise services you want to secure, you can use Splunk Web or the server.conf configuration file to set a pass4SymmKey.

You can set a single pass4SymmKey for all services, or set different pass4SymmKeys for individual services, as defined within various stanzas of the server.conf configuration file, which controls how Splunk platform services use pass4SymmKey. The following table shows the services which can be protected using a pass4SymmKey, and where in the server.conf file you can configure them.

| Splunk service | Server.conf stanza | Splunk Web configurable? | 
|---|---|---|
| Deployment clients and servers | `[deployment]` | No | 
| Indexer clusters | `[clustering]` | Yes | 
| Search head clustering, including search head deployer | `[shclustering]` | No | 
| All other services, including licensing | `[general]` | Depends | 

To configure a pass4SymmKey for some Splunk Enterprise services, you can specify it as part of the service setup workflow. For example, when you configure an indexer cluster, it provides an option to set a "Security key". This is the pass4SymmKey for the indexer cluster service.

When you specify a pass4SymmKey, it must be at least the number of characters in length as specified by the `pass4SymmKey_minLength` setting, which you can also configure in the server.conf file, and which currently has a default of 12. If you set a key with a length that is shorter than this, the Splunk platform advises you to specify a pass4SymmKey that meets the length requirement in the splunkd.log log file.

In setup workflows that don't include an option to enter a pass4SymmKey, you can edit the server.conf configuration file to specify one or more pass4SymmKeys depending on the services on which you want to enable secure authentication.

Instances or instance service types must share the same pass4SymmKey to authenticate with one another. If they don't share the same key, they won't be able to authenticate. For example, all nodes of a search head cluster must share the same key, as must all license managers and peers, or deployment servers and clients. The pass4SymmKey for each service type can be different, meaning that you can have one key for all search head clusters, another for indexer clusters, and so on.

1. On the instance where you want to enable authentication with pass4SymmKey, open the $SPLUNK\_HOME/etc/system/local/server.conf file for editing.
2. Depending on the type of Splunk platform service where you want to enable authentication, specify a stanza where you want to set the pass4SymmKey.
3. Under the stanza, add the pass4SymmKey by providing a value for the `pass4SymmKey` setting:
       
       CODE`pass4SymmKey = mypassword123`
4. (Optional) If you want to set a different pass4SymmKey for other Splunk Platform services, repeat Steps 2 and 3 for those services.
5. Save the server.conf file and close it.
6. Restart Splunk Enterprise.

Repeat this procedure on all other instance types that offer the same type of service. For example, you must perform this procedure on:

- All indexer cluster nodes
- All deployment servers and clients
- All search head cluster members and the search head deployer
- All license managers and peers

## Configure pass4SymmKey for search head clustering

Configure pass4SymmKey as you deploy the search head cluster. For the specific procedure on deploying a search head cluster, see [Deploy a search head cluster](https://help.splunk.com/?resourceId=Splunk_DistSearch_SHCdeploymentoverview) in *Distributed Search*.

For details on configuring pass4SymmKey on a search head cluster, including how to set it after you deploy the cluster, see [Set a security key for the search head cluster](https://help.splunk.com/?resourceId=Splunk_DistSearch_Setsecretkey).

## Configure pass4SymmKey for indexer clustering

Configure pass4SymmKey as you you deploy the indexer cluster, while enabling the manager node. See [Enable the indexer cluster manager node](https://help.splunk.com/?resourceId=Splunk_Indexer_Enablethemanagernode) in the *Managing Indexers and Clusters of Indexers Manual*.

For more details on setting pass4SymmKey on an indexer cluster, see [Configure the security key](https://help.splunk.com/?resourceId=Splunk_Indexer_Enableclustersindetail) in the *Managing Indexers and Clusters of Indexers Manual*.

## How apps encrypt the pass4SymmKey

When you specify pass4SymmKey in clear-text for an app directory on a Splunk platform instance, for example in the `etc/apps/myapp/default/server.conf` file, the software writes an obfuscated version of the key to the local file when you restart the instance. In this example, the software writes the obfuscated key to `system/local/server.conf`. Configuration files in the default directory are generally read-only, and the software writes the information to the local file, which is editable.

Placing a password directly into the local directory of an app (for example: `etc/apps/myapp/local/server.conf`), replaces it with the encrypted version.

When you use the `curl` web data transfer tool to view a configuration file or a `splunkd` endpoint, the pass4SymmKey appears encrypted. If the configuration location is read-only, Splunk software likewise writes to the local directory.

## Use the OpenSSL utilities to generate a random passphrase for pass4SymmKey

You can use the OpenSSL utilities that come with Splunk software to generate a passphrase that you can use with the pass4SymmKey setting.

For the strongest security, select a passphrase that is at least 12 characters long and isn't in a dictionary of known bad passphrases, like `abc123`, `password`, `qwerty`, `admin`, and so on. The OpenSSL utility that comes with Splunk software lets you randomly generate a passphrase that you can then use to configure pass4SymmKey with on all nodes of your Splunk deployment.

1. On a Splunk platform instance, open a shell prompt.
2. Change to the `$SPLUNK_HOME/bin` directory.
3. Run the following command to generate a random 12-character passphrase:
       CODE`splunk cmd openssl rand -base64 9`
4. Copy the output of the command to your clipboard.
5. For all machines where you want to use the new passphrase:
       
   1. Open the `$SPLUNK_HOME/etc/system/local/server.conf` file for editing.
   2. Under the stanza that represents the service you want to protect with a pass4SymmKey, add `pass4SymmKey = <new passphrase that you just generated>`
   3. Save the server.conf file and close it.
   4. Restart Splunk software.
