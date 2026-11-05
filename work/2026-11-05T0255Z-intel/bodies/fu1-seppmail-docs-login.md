---
title: Login As Administrator
author: SEPPmail GmbH
url: https://www.seppmail.com/04_com_06_bc_01_ns_02_login-as-administrator.html
hostname: seppmail.com
description: All administration options of the SEPPmail Secure E-Mail Gateway are available via a web browser-based configuration interface.
sitename: seppmail.com
date: "2023-01-01"
fingerprint: ab4cf57b9833b55e
---
All administration options of the SEPPmail Secure E-Mail Gateway are available via a web browser-based configuration interface.

In the delivery state, the configuration interface can be reached as follows:


•Hardware Appliance

ovia crossover cable or hub via

LAN1 - [https://192.168.1.60:8443](https://192.168.1.60:8443)

LAN2 - [https://192.168.2.60:8443](https://192.168.2.60:8443)


•virtual and hardware appliances

ofor which the IP address has been changed through the console:

LAN1 - [https://\<Your temporarily](https://%3CYour%20temporarily) assigned IP>:8443


ofor which the IP address was obtained dynamically:

LAN1 - [https://\<dynamic](https://%3Cdynamic) IP>:8443


The default user name is: admin

The default password is: admin


Immediately after successful login, the system switches to the"Change password" screen, where the password for the built-in administrator "admin" must be changed to prevent the use of insecure passwords.


|  | Note: Only by registering the SEPPmail Secure E-Mail Gateway, a temporary, 30-day test licence is obtained, respectively an already existing purchase licence is activated. (see [System Registration](https://docs.seppmail.com/04_com_06_bc_01_ns_05_system-registration.html)). After a successful registration process, the message disappears. No valid license found – Please obtain a valid license. | 


When the configuration interface is opened in the web browser, a warning that the web page is unsafe is issued. The page must still be opened despite this message.


|  | Note: The message usually only appears until a valid SSL certificate has been installed (see the menu item [SSL](https://docs.seppmail.com/07_mi_08_ssl.html)). |
