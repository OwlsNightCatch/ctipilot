---
title: An interesting route to domain admin- iSCSI | Pen Test Partners
author: PTP Admin
url: https://www.pentestpartners.com/security-blog/an-interesting-route-to-domain-admin-iscsi/
hostname: pentestpartners.com
description: On a recent test, none of the common tricks for getting a foothold onto the Windows network were working. Machines were patched, responder.py wasn’t delivering the goods, and no common passwords were in use. We needed to go deeper. A full port scan of one host had shown that port 3260 – iSCSI – was […]
sitename: Pen Test Partners
date: "2016-05-18"
categories: ['How Tos']
fingerprint: ff19d810cd2047e0
---
On a recent test, none of the common tricks for getting a foothold onto the Windows network were working. Machines were patched, responder.py wasn’t delivering the goods, and no common passwords were in use. We needed to go deeper.

A full port scan of one host had shown that port 3260 – iSCSI – was open. Nmap’s scripting engine has a script – [iscsi-info](https://nmap.org/nsedoc/scripts/iscsi-info.html) – which indicated that a number of iSCSI targets were available and required no authentication. I’d never needed to exploit this before as there had always been an easier route to domain admin.

*One or more of the iSCSI (Internet Small Computer Systems Interface) targets on the remote host are configured not to use an authentication mechanism, potentially allowing unauthorized access to the targets.*

I’ve seen this a couple of times before, but never had to try and actively exploit it. Being able to connect over iSCSI should allow us to mount the drives inside, and have full access to the filesystem inside.

First, we need to replicate what the tool is telling us. Google tells us that [iSCSI Initiator](https://help.ubuntu.com/lts/serverguide/iscsi-initiator.html) should allow us to both view and connect to the iSCSI service. This is installed as part of the open-iscsi package.

192.168.10.10:3260,-1 iqn.2008-08.com.starwindsoftware:san1-helpdesk

We’ve already identified the machine helpdesk on the network, and it looks to be running a number of potentially interesting (but secure) services. Access to the filesystem of this would be helpful, and the name of the iSCSI target suggests it may be related.

It’s probably worth pointing out that these operations are risky – we’re mounting a file system backing an important server. In the actual test, the connection was made to a secondary SAN to reduce risk.

Next, we need to connect to iSCSI:

Logging in to \[iface: default, target: iqn.2008-08.com.starwindsoftware:san1-helpdesk, portal: 192.168.10.10,3260\] (multiple)

Login to \[iface: default, target: iqn.2008-08.com.starwindsoftware:san1-helpdesk, portal: 192.168.10.10,3260\] successful.

Running fdisk will show that we now have an additional device:

Units: sectors of 1 \* 512 = 512 bytes

Sector size (logical/physical): 512 bytes / 4096 bytes

I/O size (minimum/optimal): 4096 bytes / 4096 bytes

Disklabel type: gpt

Disk identifier: E45844BF-AE06-42A5-8E73-D6598DF2A86EDevice Start End Sectors Size Type

/dev/sdb1 2048 314572766 314570719 150G unknown

Attempting to mount this doesn’t work, but it does tell us that it is a VMFS file system. This is used by VMWare ESXi, so it’s likely the SAN is providing the storage for virtual machines.

Installing the package vmfs-tools will allow us to mount this file system:

root@kalibrate:\~# vmfs-fuse /dev/sdb1 /mnt/i\_helpdesk

Looking inside the mount, there are the files for a Virtual Machine, including the .vmdk that holds the file system:

Helpdesk-1ab837b8.hlog Helpdesk.nvram Helpdesk.vmx\~ vmware-11.log vmware-9.log

Helpdesk-ctk.vmdk Helpdesk.vmdk Helpdesk.vmxf vmware-12.log vmware.log

Helpdesk-d1cf6655.vswp Helpdesk.vmsd Helpdesk.vmx.lck vmware-13.log vmx-Helpdesk-3520030293-1.vswp

Helpdesk-flat.vmdk Helpdesk.vmx vmware-10.log vmware-14.log

.vmdk files are just raw disk images, so we can use kpartx to read the partition table and create devices for each one it finds:

add map loop0p1 (254:0): 0 716800 linear /dev/loop0 2048

add map loop0p2 (254:1): 0 250937344 linear /dev/loop0 718848

The second one of these is the NTFS C: drive. We mount this read-only:

root@kalibrate:\~# mount -o ro /dev/mapper/loop0p2 /mnt/v\_helpdesk/

And now we have access to the C:\ drive of the helpdesk machine.

There are a number of different paths we can take at this point. Firstly, let’s dump the local password hashes for the machine from the registry hives:

Administrator:500:\*\*\*REDACTED\*\*\*:::

This goes straight into a password cracker to see if we can get the local admin password. The problem with this method is that a good password is unlikely to be found quickly, and in this case, they had chosen a good password.

But better than a hash would be passwords in the plain. During initial scans, it could be seen that the helpdesk machine was running [Lansweeper](http://www.lansweeper.com/). This is a network monitoring tool. One thing it does is allow you to enter credentials so that it can login to remote machines to perform checks. By necessity, the credentials have to be stored in a way that allows them to be read. This means they aren’t hashed – they are encrypted. That means we can decrypt them.

It just so happens that someone has already looked into Lansweeper and found that this [encryption isn’t great.](http://blog.gosecure.ca/2016/04/21/your-credentials-at-risk-with-lansweeper-5/)

Prodding around the filesystem, we find the database backing Lansweeper. It’s a SQL Server Compact database stored in Program Files. According to the Internet, this should have the encrypted credentials in the table tsysconfig or tsyscredentials.

Trying to open the lansweeper.sdf file in [LINQPad](https://www.linqpad.net/) tells us the database is corrupt and needs repairing. I’ve seen this before – it seems to happen when you copy the database whilst it is open elsewhere. The [sqlcmdce tool](https://sqlcecmd.codeplex.com/) allows us to repair it, but only using the option repairdelete. This may lose data in the process of repairing the file.

Now viewing the database works, but the tables holding credentials appear empty:

As a last ditch attempt, I try strings on the file. Piping this into grep and looking for administrator quickly shows what look like encrypted values.

We pass that into the [Lansweeper Password Recovery Tool](https://github.com/GoSecure/LansweeperPasswordRecovery) to decrypt the values, and voila, we have a domain admin password in clear text:

Not a conventional route to domain admin, and could have failed at numerous points.

What would our recommendations here be?

- Run iSCSI on an entirely segregated network, ideally on totally discrete switches and cabling. This is best practice for any form of SAN traffic.
- If this isn’t possible use iSCSI authentication, VLANS or IPSEC to secure communications.
- Segregate management and non-essentials services from end-user desktop networks. If port 3260 could not be routed from the machine I was on to the server, this attack would have failed.
- Appreciate the risks of storing credentials in applications, and protect machines running these applications appropriately.
- Setup a domain account for use in monitoring tools, set a strong password, and reduce permissions as far as is possible.
