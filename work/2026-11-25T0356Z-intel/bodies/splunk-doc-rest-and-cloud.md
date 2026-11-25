---
title: Access requirements and limitations for the Splunk Cloud Platform REST API
url: https://help.splunk.com/en/splunk-enterprise/leverage-rest-apis/rest-api-tutorials/10.6/rest-api-tutorials/access-requirements-and-limitations-for-the-splunk-cloud-platform-rest-api
hostname: splunk.com
sitename: help.splunk.com
date: "2026-08-25"
fingerprint: "2e014d905aae99c9"
language: en
image: https://assets.portal.heretto.com/splunk/25-02-13/splunk-favicon.ico
filedate: "2026-11-25"
---
# Access requirements and limitations for the Splunk Cloud Platform REST API

After you request access, you can use a limited subset of the Splunk Enterprise REST API endpoints with your Splunk Cloud Platform deployment.

## Accessing the Splunk Cloud Platform REST API

You might need to take extra steps to access your Splunk Cloud Platform deployment using the Splunk REST API and SDKs. If necessary, you can get access with one of the following options:

- Use the Admin Config Service (ACS) API search-api/ipallowlists endpoint to add IP addresses to the search-api allow list. For more information about the search-api/ipallowlists endpoint, see [Configure IP allow lists for Splunk Cloud Platform](https://docs.splunk.com/?resourceId=SplunkCloud_Config_ConfigureIPAllowList).
- Submit a support case requesting access using the [Splunk Support Portal](https://www.splunk.com/en_us/customer-success/support-programs.html). Splunk Support opens port 8089 for REST access. You can specify a range of IP addresses to control who can access the REST API, so make sure your request includes the IP addresses or CIDR ranges that you want access from.

Free trial Splunk Cloud Platform accounts cannot access the REST API.

After you get REST API access, create authentication tokens to use the REST APIs. Tokens are available for both native Splunk authentication and external authentication through either the LDAP or SAML schemes. To learn more about setting up authentication with tokens, see [Set up authentication with tokens](https://docs.splunk.com/?resourceId=Splunk_Security_Setupauthenticationwithtokens) in the *Securing Splunk Enterprise* manual.

Use the following URL for Splunk Cloud Platform deployments:

`https://<deployment-name>.splunkcloud.com:8089`
## Administrative role limitations

The Splunk Cloud Platform administrative role `sc_admin` is restricted from performing the following types of tasks using Splunk Web, the command line interface, or the REST API:

- Modifying configuration of deployment servers, client configuration, and distributed components, such as indexers, search heads, and clustering.
- Restarting a Splunk Cloud Platform deployment
- Executing debug commands
- Installing apps and modifying app configurations

## REST API access limitations

As a Splunk Cloud Platform user, you are restricted to interacting with the search tier only with the REST API. You cannot access other tiers by using the REST API. Splunk Support manages all tiers other than the search tier.

To access endpoints and REST operations, you must authenticate with your username and password.

The following table shows which resource groups are supported in Splunk Cloud Platform:

| Category | Description | 
|---|---|
| [Access control](https://docs.splunk.com/?resourceId=Splunk_RESTREF_RESTaccess) | Authorize and authenticate users. | 
| [Federated Search](https://docs.splunk.com/?resourceId=Splunk_RESTREF_RESTfederated) | Create, update, and delete definitions for federated providers and federated indexes. | 
| [Knowledge](https://docs.splunk.com/?resourceId=Splunk_RESTREF_RESTknowledge) | Define indexed and searched data configurations. | 
| [KV store](https://docs.splunk.com/?resourceId=Splunk_RESTREF_RESTkvstore) | Manage the Key Value store. | 
| [Metrics](https://docs.splunk.com/?resourceId=Splunk_RESTREF_RESTmetrics) | Enumerate metrics. | 
| [Search](https://docs.splunk.com/?resourceId=Splunk_RESTREF_RESTsearch) | Manage searches and search-generated alerts and view objects. |
