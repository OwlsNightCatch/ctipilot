---
title: GINA Domains
author: SEPPMAIL AG
url: https://www.seppmail.com/07_mi_17_gd__gina-domains.html
hostname: seppmail.com
description: In this menu, the configuration of the web interface(s) for GINA Webmail technology is carried out.
sitename: seppmail.com
date: "2023-01-01"
tags: ['cell phone', 'GINA Domains', 'GINA password via SMS', 'GINA Satellite', 'GINA Settings', 'GSM modem', 'SMS', 'virtual hosting']
fingerprint: b29cb8114942b3e5
language: de
filedate: "2026-11-26"
---
In this menu, the configuration of the web interface(s) for [GINA Webmail](https://docs.seppmail.com/en/03_wp_02_pap_02_et_04_gina__gina-webmail.html) technology is carried out.


Sections on this page:




List of GINA domains.


The Filter... provides a search function in the column **GINA name** of the following table. The search term is entered as a character string.


| Column | Description | 
|---|---|
| [GINA name](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#d_ginaname) | List of all GINA domains created on the SEPPMAIL Secure E-Mail Gateway. By default, only the "\[default\]" GINA domain exists. | 
| [Hostname](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#d_hostname) | Displays the hostname of the corresponding GINA domain as it is entered in the submenu  [Secure GINA Host](https://docs.seppmail.com/en/07_mi_17_gd_02_cgs__change-gina-settings-for.html#secureginahost). | 
| [Admin](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#d_admin) | Displays the admin email address of the corresponding GINA domain as it is entered in the submenu  [Admin](https://docs.seppmail.com/en/07_mi_17_gd_02_cgs__change-gina-settings-for.html#admin). | 


If only one GINA web interface is required, it is sufficient to adapt the "\[default\]" settings individually.

If several [Managed Domains](https://docs.seppmail.com/en/07_mi_06_ms__mail-system.html#manageddomains) are set-up on the system, the Create new GINA domain function allows additional GINA web interfaces to be configured (see submenu ).


|  | [Attention:](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#d_warning1) With a client-capable installation, it is absolutely necessary to create at least one GINA domain for each customer. | 


This is set up by clicking on the GINA domain to be configured in the column GINA name (see submenu ).


The allocation of the corresponding GINA domain to the respective [Managed domain](https://docs.seppmail.com/en/07_mi_06_ms__mail-system.html#manageddomains) is realised in the section [Bounce templates](https://docs.seppmail.com/en/07_mi_06_ms_04_aemd__add-edit-managed-domain.html#bouncetemplates) of the submenu  in [Mail System](https://docs.seppmail.com/en/07_mi_06_ms__mail-system.html) [Managed Domains](https://docs.seppmail.com/en/07_mi_06_ms__mail-system.html#manageddomains).


|  | [Attention:](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#d_warning2) The "\[default\]" GINA domain must be configured in any case since it serves as basis for additional GINA domains if applicable. Otherwise, sporadic errors of the appliance are to be expected! | 




General settings of the GINA domains.


| Parameters |  | Description | 
|---|---|---|
| [Virtual hosting](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_virtualhosting) |  |  | 
| [Use virtual hosting](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_usevirtualhosting) |  | If several GINA domains are used...  | 
|  | [On for all domains](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_uvh_onforalldomains) | ...a separate FQDN is to be used for each GINA domain. This has the effect that each GINA domain also requires a separate certificate. In this case, the corresponding input field for the individual certificate is displayed in the submenu and/or . | 
|  | [Off for all domains](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_uvh_offforalldomains) | Default setting. ... generally, only one FQDN is used for access. Each additional GINA domain will have a separate folder created for it below this FQDN. By doing so, even when using multiple GINA domains, only one SSL certificate (see menu item [SSL](https://docs.seppmail.com/en/07_mi_08_ssl.html)) is required for access from the Internet. | 
|  | [Use domain settings](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_uvh_usedomainsettings) | ...it can be decided for each GINA domain (see and/or ) which version is desired.  | 
|  [Disable strict SNI check when virtual hosting is enabled](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_disablestrictsnicheckwhenvirtualhostingisenabled) (new in 12.0) |  | By default, this option is inactive. By activating this option, the protection against the incorrect activation of a GINA domain, which was introduced with version 11.1.7, can be prevented (error message "403 Forbidden You don't have permission to access this resource. Reason: The client software did not provide a hostname using Server Name Indication (SNI), which is required to access this server.". Using this option restores the behaviour of version 11.1.6 and older, and it should only be used for a temporary restoration in the event of an error. | 
| [TLS settings](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_tlssettings) |  |  | 
|  [Disallow insecure ciphers](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_disallowinsecureciphers) |  | By default, this option is inactive. Enables access to GINA domains even with older clients/browsers (RC4 active). To make full use of the security potential of the appliance, the action should be activated Depending on this setting, more or fewer ciphers, ciphersuites and curves will be offered below. | 
| [Ciphers, Ciphersuites, Groups](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_ciphersciphersuitesgroups) |  | Here [Ciphers](https://docs.seppmail.com/en/03_wp_04_sec_01_ciphers.html) (for TLSv1.2), Ciphersuites (for TLSv1.3) and Groups (for example with post quantum support like X25519MLKEM768) could be selected. By default, all are selected. (new in 15.1.2) If no Group is selected, the system default is used. | 
| [GINA cleanup settings](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_ginacleanupsettings) |  |  | 
| [Grace period (in days) after which unregistered GINA accounts are automatically removed](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_graceperiodindaysafterwhichunregisteredginaaccountsareautomaticallyremoved) (removed in 15.0.4) |  |  | 
| [Grace period (in days) after which old GINA message metadata is automatically removed. Mails can still be decrypted by recipient if metadata is missing. (set to 0 to disable)](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_graceperiodindaysafterwhicholdginamessagemetadataisautomaticallyremovedmailscanstillbedecryptedbyrecipientifmetadataismissing) (removed in 15.0.4)  |  |  | 
| [Login history retention period (days) (new in 14.0)](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_loginhistoryretentionperiod) |  | The login history is kept for this period. The default setting for this option is 30 days. If empty or zero, the history is stored indefinitely. | 
| [SMS history retention period (days)](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_smshistoryretentionperiod) (new in 14.1) |  | The SMS history is kept for this period. The default setting for this option is 60 days. If empty or zero, the history is stored indefinitely. The SMS history can be queried with the Rest end point /webmail/user/smshistory. | 
| [Mail track](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_mailtrack) |  |  | 
| [Secure track access](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_securetrackaccess) |  | By default, this option is empty and thus deactivated. With this option, additional information is provided via the inserted link in a GINA read confirmation, e.g. which GINA recipient has read the email and when. This function is activated by entering the URL for access to the administration interface of the appliance (see [System](https://docs.seppmail.com/en/07_mi_05_system.html) [Admin GUI](https://docs.seppmail.com/en/07_mi_05_system.html#admingui)).  | 

|  | [Attention:](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#s_uvh_uds_warning1) If an existing system with several GINA domains is subsequently changed to [virtual hosting](https://docs.seppmail.com/en/07_mi_17_gd_02_cgs__change-gina-settings-for.html#sgh_uvh_usevirtualhosting), this is also possible but requires changes under [Secure GINA host](https://docs.seppmail.com/en/07_mi_17_gd_02_cgs__change-gina-settings-for.html#secureginahost) [hostname](https://docs.seppmail.com/en/07_mi_17_gd_02_cgs__change-gina-settings-for.html#sgh_hostname) and/or [Additional hostnames](https://docs.seppmail.com/en/07_mi_17_gd_02_cgs__change-gina-settings-for.html#sgh_uvh_additionalhostnames)). | 

|  | This option is implemented in client-capable systems by means of the setting [Customers](https://docs.seppmail.com/en/07_mi_24_cust__customers.html) [Retention settings](https://docs.seppmail.com/en/07_mi_24_cust_01_cec__create-newedit-settings-for-customer.html#retentionsettings). By now, all systems are client-capable, so this option has been removed. | 


The changes made are saved via the Save button.


(new in 14.0.0)


Storage settings for S3.


| Parameter | Description | 
|---|---|
| [Host](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sts_host) | Only has to be entered for a non-Amazon host. | 
| [API Key](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sts_apikey) | API Key for the S3 connection. | 
| [API Secret](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sts_apisecret) | API Secret for the S3 connection. | 
| [Bucket name](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sts_bucketname)  | The default is seppmail. | 
| [Download chunk size](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sts_downloadchunksize) | Size of chunks used for upload in bytes. The default value is 5242880. | 


With Connectivity and speed test the connection can be tested.

The changes made are saved via the Save button.



Settings for automatically sending passwords via SMS.


|  | [Note:](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp_hint1) For generating the SMS, both an internal service in the network of the customer can be used via a corresponding gateway as well as an external service in the Internet. Access to this service is to be granted (see [Setting Up The Firewall/Router](https://docs.seppmail.com/en/04_com_04_setup-firewall-router.html)). | 


|  | [Note:](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp_hint2) The standard texts of the SMS service can be customised in the language settings for the GINA domain, see (see [Edit translations](https://docs.seppmail.com/en/07_mi_17_gd_02_cgs_02_edit-translations-for-language-x.html#edittranslationfile)). | 


| Parameters |  | Description | 
|---|---|---|
|  |  [Disable](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp__disable) | Default setting. The GINA password delivery via SMS is deactivated | 
|  |  [Use cell phone / GSM modem attached to appliance](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp__usecellphonegsmmodemattachedtoappliance) | If a hardware appliance is used, a mobile phone or GSM modem capable of sending an SMS can be attached to a USB connection of the appliance. Sufficient reception of the mobile phone/GSM modem is to be ensured. | 
|  |  [Use Mail to SMS service](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp__usemailtosmsservice) (configuration below) | Here, the access data for the SMS delivery via a Mail to SMS service is entered. Put together, an email would be created from \<Mail from:> to \<Mail address prefix:>\<mobile number of the password recipient>@\<Gateway domain>  | 
|  |  [Use xml service](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp__usexmlservice) (configuration below) | Here, the access data for the SMS delivery via a XML service is entered. Additionally, the variables provided are displayed. and a configuration example:  | 
|  |  [Use HTTP GET service](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp__usehttpgetservice) (configuration below) | Here, the access data for the SMS delivery via HTTP Get is to be entered. The variables known from the XML configuration are available. Additionally, the configuration example for the Swiss "chrus" service is displayed.  | 
| [Access to GINA send password form:](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp_accesstoginasendpasswordform) |  | Via this option, access to the password delivery link of the appliance is controlled. | 
|  |  [Disabled](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp_atgspf_disabled) | Default setting. This is used to disable the password delivery link. Thus, the latter will not appear in the password email sent to the sender of the email with the initial sending of a GINA email. | 
|  |  [Available via public GUI](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp_atgspf_availableviapublicginagui) | Activates the insertion of the link for the SMS password delivery in the GINA password notification email to the sender. | 
| [Proxy](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp_proxy) |  | Check the option Do not use proxy (ignore settings under System - Advanced) to disable this proxy setting. By default inactive. | 
| [Use UTF](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp_useutfencoding) (new in 15.0.1) |  | Check the option Use UTF-encoding to enable that the data is sent as UTF-8. By default inactive. | 
| Only available if SMS passwords are disabled while some SMS with initials passwords were not delivered yet |  |  | 
| [\[n\] GINA user(s) have not yet received their initial passphrase via SMS. Please select one of the following actions:](https://docs.seppmail.com/en/07_mi_17_gd__gina-domains.html#sp_smsdisabled_ginausershavenotreceivedpwyet)  |  | Available options for handling this problem: •Send remaining sms •Inform respective senders of GINA mails via email •Download CSV file providing relevant sender-receiver data (click download button below) •Do nothing  | 

| Mail to SMS settings |  | 
| Mail from: | Depending on the provider, the email sender address registered for this service with the provider or a freely selectable sender name is to be entered here. | 
| Mail address prefix: \<PREFIXMobile#>@ | Depending on the provider, aside of the recipient’s number, another addition is required which can also be entered here if necessary. This data is provided by the provider of the service. With Deutsche Telekom, for example, this would be 017187654321 | 
| Gateway domain: \<mobile#>@ | Gateway domain for sending SMS. This data is provided by the provider of the service. With Deutsche Telekom, for example, this would be t-d1.sms.de | 

| Server address: | Server address of a service provider. This data is provided by the provider of the service. | 
|---|---|
| xml template | This data is provided by the provider of the service. An example of this can be found further below in this section | 

| Placeholders: |  | 
| $sms: text message | message text to be transmitted. | 
| $number: cell number including country code (+xx...) | Mobile phone number including country code (+xx...)  | 
| $countrycode: country code, e.g "49" | Country code, for example "49" for Germany | 
| $localnumber: cell number without country code | Mobile phone number WITHOUT country code | 

| XML Example: |  | 
| Server: | [https://xml1.aspsms.com](https://xml1.aspsms.com) | 
| String: | \<?xml version="1.0" encoding="UTF-8"?> \<aspsms> \<Userkey>xyz\</Userkey> \<Password>xyz\</Password> \<Originator>Secmail\</Originator> \<FlashingSMS>0\</FlashingSMS> \<Recipient> \<PhoneNumber>00$countrycode$localnumber\</PhoneNumber> \</Recipient> \<MessageData>\<!\[CDATA\[$sms\]\]>\</MessageData> \<Action>SendTextSMS\</Action> \</aspsms>  | 

| Server address: | The SMS provider provides the server for access to the HTTP Get Service. | 
|---|---|
| HTTP Get String | The SMS provider provides the string for access to the HTTP Get Service. | 

| HTTP GET Example: |  | 
| Server: | [https://www.chrus.ch](https://www.chrus.ch) | 
| String: | /mysms/http/send.php?user=xyz&pwd=xyz&from=Secmail&to=$number&msg=$sms | 



The changes made are saved via the Save button.
