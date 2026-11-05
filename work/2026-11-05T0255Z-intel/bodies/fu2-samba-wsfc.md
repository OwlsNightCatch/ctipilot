Title: Setting up a Windows failover cluster

URL Source: https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster

Markdown Content:
This page is a draft

## Introduction

Setting up a Windows cluster requires at least three virtual machines and two networks.

These instructions assume KVM and libvirt are used. Windows version is Server 2019.

				+-------------+
				| SMB  Client |
				+-------------+
				       |
				192.168.150.201
				       |
	+---------------------------------------------------------------+
	|			Clients network				|
	+---------------------------------------------------------------+
		|                      |                       |
	 192.168.150.10		192.168.150.21		192.168.150.22
		|                      |                       |
	+---------------+       +------------+          +------------+
	|   AD + iSCSI  |       |   Node 1   |          |   Node 2   |
	| target server |       +------------+          +------------+
	+---------------+              |                       |
                                       |                       |
                                192.168.160.21          192.168.160.22
                                       |                       |
	+---------------------------------------------------------------+
	|		        Cluster network                         |
	+---------------------------------------------------------------+

| VM name | Hostname | IP addresses |
| --- | --- | --- |
| win2k19-fover-ad | fover-ad | 192.168.150.10 |  |
| win2k19-fover-n1 | fover-n1 | 192.168.150.21 | 192.168.160.21 |
| win2k19-fover-n2 | fover-n2 | 192.168.150.22 | 192.168.160.22 |

## Setup libvirt networks

The first step is to create the public and private networks in libvirt. Save the following fragment to a file named `cluster-public.xml`:

<network>
  <name>cluster-public</name>
  <forward mode='nat'>
    <nat>
      <port start='1024' end='65535'/>
    </nat>
  </forward>
  <domain name='cluster-public'/>
  <dns>
    <forwarder domain='fover.net' addr='192.168.150.10'/>
  </dns>
  <ip address='192.168.150.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.150.200' end='192.168.150.250'/>
    </dhcp>
  </ip>
</network>

Save the following fragment to `cluster-private.xml`:

<network>
  <name>cluster-private</name>
  <domain name='fover.net'/>
  <dns>
    <forwarder domain='fover.net' addr='192.168.160.10'/>
  </dns>
  <ip address='192.168.160.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.160.200' end='192.168.160.250'/>
    </dhcp>
  </ip>
</network>

Now define and start the networks:

# virsh net-define cluster-public.xml
# virsh net-define cluster-private.xml
# virsh net-start cluster-public
# virsh net-start cluster-private

## Setup AD virtual machine

After installing the operating system, **set the host name** and **IP addresses**. It is useful to rename the network adapters to know to which network are connected.

|  | Public | Private |
| --- | --- | --- |
| IP Address | 192.168.150.10 | 192.168.160.10 |
| Netmask | 255.255.255.0 | 255.255.255.0 |
| Gateway | 192.168.150.1 |  |
| DNS 1 | 192.168.150.1 |  |
| DNS 2 |  |  |

Proceed to install the **Active Directory Domain Services** and **iSCSI target server** roles:

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_ad_install_roles.png)

Once roles are installed, provision the Active Directory domain following the Wizard:

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_ad_domain_provision.png)

## Setup cluster nodes

In both nodes:

1.    Install the operating system
2.    Set the hostname
3.    Set the IP addresses

|  | fover-n1 | fover-n2 |
| --- | --- | --- |
|  | Public | Private | Public | Private |
| IP Address | 192.168.150.21 | 192.168.160.21 | 192.168.150.22 | 192.168.160.22 |
| Netmask | 255.255.255.0 | 255.255.255.0 | 255.255.255.0 | 255.255.255.0 |
| Gateway | 192.168.150.1 |  | 192.168.150.1 |  |
| DNS 1 | 192.168.150.10 |  | 192.168.150.10 |  |
| DNS 2 |  |  |  |  |
4.   Join the computer to the domain
5.   Install the "File Server" role and the "Failover Clustering" feature. 

## Setup the iSCSI target server

In fover-ad:

1.   Open the Server Manager console and go to "File and Storage Services" -> "iSCSI"
2.   Click TASKS -> New iSCSI virtual disk
3.   Follow the "New iSCSI Virtual Disk Wizard" 
    1.   iSCSI Virtual Disk Location Select C
    2.   iSCSCI Virtual Disk Name Name quorum Description quorum witness disk</il>
    3.   iSCSI Virtual Disk Size 128 MB, Dynamically expanding
    4.   iSCSI target Select New iSCSI target
    5.   Target Name and Access Name fover Description Fover cluster iSCSI target server
    6.   Access Server 
        1.   Click add
        2.   Select Query initiator computer for ID
        3.   Type the node 1 host name (fover-n1.fover.net)
        4.   Click OK
        5.   Click add
        6.   Select Query initiator computer for ID
        7.   Type the node 2 host name (fover-n2.fover.net)
        8.   Click OK

    7.   Enable authentication Do not enable
    8.   Confirm

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_ad_iscsi_target_server.png)

## Setup the iSCSI initiators

In each node:

1.   Open the Server Manager
2.   Click Tools -> iSCSI initiator
3.   It will ask to start the service, click yes
4.   In the "Targets" tab, type "fover-ad.fover.net" and click Quick Connect
5.   In the "Volumes and Devices" tab, click Auto Configure
6.   Click OK

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_node_iscsi_initiator.png)

## Initialize the quorum disk

In one of the nodes:

1.   Open the Server Manager
2.   Go to File and Storage Services -> Disks
3.   Right click the 128MB disk, select bring online
4.   Right click the 128MB disk, select Initialize
5.   Right click the 128MB disk, select New Volume
6.   Follow the "New Volume Wizard", do not assign a letter

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_node_quorum_disk.png)

## Create the cluster

1.   Open the Server Manager
2.   Go to Tools -> Failover Cluster Manager
3.   In the right column, click Validate Configuration
4.   Follow the Validate Configuration Wizard 
    1.   Select Servers Type the name of the first node, fover-n1.fover.net and click add Type the name of the second node, fover-n2.fover.net and click add
    2.   Testing options Select Run all tests
    3.   Check the results Everything should succeed, you may get a warning if the nodes do not have the same updates installed
    4.   Select the "Create the cluster now using the validated nodes" and click finish

5.   Follow the "Create Cluster Wizard" 
    1.   Access point for administering the cluster Type a name for the cluster: "cluster"Type an address associated to the cluster name: "192.168.150.30"
    2.   Confirmation page Select "Add all elegible storage to the cluster"
    3.   Confirm

Check the Quorum is properly configured. You should see the 128MB disk assigned to "Disk Witness in Quorum"

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_node_disk_witness.png)

A new computer account "cluster" will be created in AD, and a new A record added to the DNS zone. This new computer account needs permission to create and modify computer objects in the AD computers organizational unit. To grant this permission:

1.   In fover-ad, open the Active Directory Users and Computers management tool
2.   Click View, enable Advanced features
3.   Expand the domain, right click in the "Computers" OU and select Properties
4.   Select the Security tab, click add
5.   Click "Object Types", Select Computers, click OK
6.   Type "cluster", click OK
7.   Click cluster, and grant "Write, Create all child objects and Delete all child objects"
8.   Click OK

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_ad_grant_permissions.png)

## Create the clustered file server

### Create a new iSCSI disk for the file server

1.   In AD, open the Server Manager
2.   Go to File and Storage Services -> iSCSI
3.   Click Tasks -> New iSCSI virtual disk
4.   Follow the New iSCSI Virtual Disk Wizard: 
    1.   iSCSI Virtual Disk Location Click Select by volume and select C:
    2.   iSCSCI Virtual Disk Name Name: fs Description: Disk for file server role
    3.   iSCSI Virtual Disk Size 2 GB, Dynamically expanding
    4.   iSCSI Target Select Existing iSCSI target and select 'fover'
    5.   Click create

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_ad_fs_disk.png)

### Initialize the iSCSI disk

1.   In one of the nodes, open Server Manager
2.   Go to Tools -> iSCSI Initiator
3.   Go to the Volumes and Devices tab and click Auto Configure
4.   The new disk will appear in the list. Click OK to close the iSCSI initiator
5.   Go to "File and Storage Services" -> Disks
6.   If the new disk does not appear, click Tasks -> Refresh
7.   Right click the 2GB Disk, Bring online
8.   Right click the 2GB Disk, Initialize
9.   Right click the 2GB Disk, New Volume
10.   Follow the "New Volume Wizard", assign a drive letter

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_ad_fs_volume.png)

### Add the iSCSI disk to the cluster storage

1.   In one of the nodes, open the Failover Cluster Manager
2.   In the left column, expand the cluster, expand Storage and select Disks
3.   In the right column, click Add Disk
4.   Select the disk and click OK
5.   The disk is listed as "Available Storage"

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_node_fs_disk_assigned.png)

### Create the role

1.   In one of the nodes, open the Failover Cluster Manager
2.   In the left column, expand the cluster and select Roles
3.   In the right column, click "Configure Role"
4.   Follow the "High Availabiliry wizard" 
    1.   Select Role Select "File Server"
    2.   File Server Type Select "File Server for general use"
    3.   Client Access Point Name: fs IP Address: 192.168.150.31
    4.   Select Storage Select the disk
    5.   Confirm

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_node_fs_role.png)

1.   In one of the nodes, open the Failover Cluster Manager
2.   In the left column, expand the cluster and select Roles
3.   Click the File Server (fs), and in the right column click "Add File Share"
4.   Follow the "New Share Wizard" 
    1.   Select Profile Select "SMB Share - Quick"
    2.   Share Location Select by Volume, and select E: (The letter assigned to the volume created in previous steps)
    3.   Share Name Name: share1
    4.   Other Settings Enable Continous availability
    5.   Permissions Click Customize permissions and grant Domain Users write access to the share
    6.   Confirm

[](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_node_fs_share.png)

Links/Buttons:
- [Jump to content](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#bodyContent)
- [Main Page](https://wiki.samba.org/index.php/Main_Page)
- [User Documentation](https://wiki.samba.org/index.php/User_Documentation)
- [Developer Documentation](https://wiki.samba.org/index.php/Developer_Documentation)
- [Categories](https://wiki.samba.org/index.php/Special:Categories)
- [Current Events](https://wiki.samba.org/index.php/SambaWiki:Current_events)
- [Recent Changes](https://wiki.samba.org/index.php/Special:RecentChanges)
- [Random Page](https://wiki.samba.org/index.php/Special:Random)
- [Report Samba Bug](https://wiki.samba.org/index.php/Bug_Reporting)
- [Report Doc Bug](https://wiki.samba.org/index.php/Reporting_a_Bug_in_the_Samba_Documentation)
- [Search](https://wiki.samba.org/index.php/Special:Search)
- [Create account](https://wiki.samba.org/index.php?title=Special:CreateAccount&returnto=Setting+up+a+Windows+failover+cluster)
- [Log in](https://wiki.samba.org/index.php?title=Special:UserLogin&returnto=Setting+up+a+Windows+failover+cluster)
- [Beginning](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#)
- [1 Introduction](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Introduction)
- [2 Setup libvirt networks](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Setup_libvirt_networks)
- [3 Setup AD virtual machine](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Setup_AD_virtual_machine)
- [4 Setup cluster nodes](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Setup_cluster_nodes)
- [5 Setup the iSCSI target server](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Setup_the_iSCSI_target_server)
- [6 Setup the iSCSI initiators](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Setup_the_iSCSI_initiators)
- [7 Initialize the quorum disk](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Initialize_the_quorum_disk)
- [8 Create the cluster](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Create_the_cluster)
- [9 Create the clustered file server](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Create_the_clustered_file_server)
- [9.1 Create a new iSCSI disk for the file server](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Create_a_new_iSCSI_disk_for_the_file_server)
- [9.2 Initialize the iSCSI disk](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Initialize_the_iSCSI_disk)
- [9.3 Add the iSCSI disk to the cluster storage](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Add_the_iSCSI_disk_to_the_cluster_storage)
- [9.4 Create the role](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Create_the_role)
- [9.5 Create a high available share](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster#Create_a_high_available_share)
- [Page](https://wiki.samba.org/index.php/Setting_up_a_Windows_failover_cluster)
- [Discussion](https://wiki.samba.org/index.php?title=Talk:Setting_up_a_Windows_failover_cluster&action=edit&redlink=1)
- [View source](https://wiki.samba.org/index.php?title=Setting_up_a_Windows_failover_cluster&action=edit)
- [View history](https://wiki.samba.org/index.php?title=Setting_up_a_Windows_failover_cluster&action=history)
- [What links here](https://wiki.samba.org/index.php/Special:WhatLinksHere/Setting_up_a_Windows_failover_cluster)
- [Related changes](https://wiki.samba.org/index.php/Special:RecentChangesLinked/Setting_up_a_Windows_failover_cluster)
- [Special pages](https://wiki.samba.org/index.php/Special:SpecialPages)
- [Permanent link](https://wiki.samba.org/index.php?title=Setting_up_a_Windows_failover_cluster&oldid=17218)
- [Page information](https://wiki.samba.org/index.php?title=Setting_up_a_Windows_failover_cluster&action=info)
- [](https://wiki.samba.org/index.php/File:Setting_up_a_Windows_failover_cluster_node_fs_share.png)
- [CC-BY](https://wiki.samba.org/index.php/License)
- [Privacy policy](https://wiki.samba.org/index.php/SambaWiki:Privacy_policy)
- [About SambaWiki](https://wiki.samba.org/index.php/SambaWiki:About)
- [Disclaimers](https://wiki.samba.org/index.php/SambaWiki:General_disclaimer)
