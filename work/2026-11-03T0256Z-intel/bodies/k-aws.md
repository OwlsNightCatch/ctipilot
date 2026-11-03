# extract: served via trafilatura-direct
---
title: CVE-2026-98432 - Linux kernel IPv4 TCP use-after-free Issue
url: https://aws.amazon.com/security/security-bulletins/2026-160-aws/
hostname: amazon.com
sitename: Amazon Web Services, Inc.
date: "2026-11-02"
fingerprint: "152379138cbc3dec"
---
### CVE-2026-98432 - Linux kernel IPv4 TCP use-after-free Issue

**Bulletin ID:** 2026-160-AWS

**Scope:** AWS

**Content Type:** Important (requires attention)

**Publication Date:** 10/30/2026 22:15 PM PDT

**Last Updated Date:** 11/02/2026 15:00 PM PST

### **Summary:**

AWS is aware of [CVE-2026-98432](https://nvd.nist.gov/vuln/detail/CVE-2026-98432), a memory issue in the Linux kernel IPv4 TCP handshake path affecting kernel versions 4.4 and later. Under specific conditions, a remote, unauthenticated third-party could send crafted IPv4 TCP packets that carry IP options to an affected listener. This could result in a kernel crash, disclosure of kernel memory, or memory corruption. Researchers have demonstrated unauthenticated remote code execution against hosts with a Multipath TCP (MPTCP) listener. We have no evidence that this issue has been leveraged at this time. We will update this bulletin as more information becomes available.

### Current Mitigation Status:

**Amazon Linux**

Amazon Linux 2 and Amazon Linux 2023 kernel packages for the resolution of CVE-2026-98432 are available. Customers should update their kernel packages and reboot. Kernel versions kernel-4.14, kernel-5.4, kernel-5.10, kernel-5.15, kernel-6.1, kernel-6.12, & kernel-6.18: Available now.

Advisories: ALAS2-2026-4065, ALAS2KERNEL-5.4-2026-135, ALAS2KERNEL-5.10-2026-137, ALAS2KERNEL-5.15-2026-120, ALAS2023-2026-3365, ALAS2023-2026-3335, ALAS2023-2026-3251.

To update:

| # Amazon Linux 2 sudo yum update kernel && sudo reboot # Amazon Linux 2023 Kernel 6.1 sudo dnf update kernel --releasever=latest && sudo reboot # Amazon Linux 2023 Kernel 6.12 sudo dnf update kernel6.12 --releasever=latest && sudo reboot # Amazon Linux 2023 Kernel 6.18 sudo dnf update kernel6.18 --releasever=latest && sudo reboot | 

Amazon Linux 2023 instances that are locked to a release version must use release 2023.12.20261102 or later to receive the updated kernel.

**Amazon EC2**

Customers running self-managed Linux instances on Amazon EC2 are responsible for updating the kernel on those instances. If you run Amazon Linux, update the kernel package as described above. If you run another Linux distribution, follow your distribution's guidance for applying the fix when it becomes available.

After updating the kernel, a reboot is required for the fix to take effect. A kernel update and reboot is the only complete remediation for this issue.

**AWS Web Application Firewall, Application Load Balancer, Classic Load Balancer, TLS Listeners on Network Load Balancer, Cloud Front, API Gateway**

Customers using the above services do not receive TCP connections from untrusted sources directly when following best practices. AWS is applying updates to the underlying infrastructure of these services and no immediate customer action is required if you are using these services. We still recommend customers update their self-managed instances behind these services within the next 30 days.

**Network Load Balancer (TCP Listeners) and Amazon Global Accelerator**

Network Load Balancer TCP listeners pass client packets, including IP options, to targets. Customers running Linux targets behind Network Load Balancer TCP listeners, or Linux endpoints behind AWS Global Accelerator, should update the kernel on those targets and reboot, or apply the interim steps below until they can.

**Amazon EKS**

Amazon EKS has released updated EKS-optimized Amazon Linux 2023 AMIs ([release v20261031](https://github.com/awslabs/amazon-eks-ami/releases/tag/v20261031)) that address this issue. Customers using managed node groups, self-managed nodes, or Karpenter with these AMIs should update their nodes to v20261031 or later.

Amazon EKS released updated EKS Auto Mode AMIs on October 31, 2026. EKS Auto Mode automatically replaces existing nodes with nodes running the updated AMI, subject to your NodePool disruption budgets. No customer action is required for EKS Auto Mode. EKS Auto Mode AMIs are named in the form "Bottlerocket (EKS Auto, Standard) 2026.10.31". To check which AMI your nodes are running, run the command kubectl get node -o wide and compare the OS-IMAGE column.

Amazon EKS Fargate Pods launched after November 1, 2026, 9:00 AM PST (November 1, 2026, 5:00 PM UTC) run on the patched platform. Amazon EKS replaces pods that were already running within 14 days as part of our routine [security patching cycle](https://docs.aws.amazon.com/eks/latest/userguide/fargate-pod-patching.html).

**Amazon ECS**

Customers running ECS on EC2 should update the kernel on their container instances and reboot, or replace them with instances launched from the latest ECS-optimized AMI ([release 20261031](https://github.com/aws/amazon-ecs-ami/releases/tag/20261031)).

- Fargate: AWS has released a patched platform version. All new tasks launched after November 1, 2026, 9:00 AM PST (November 1, 2026, 5:00 PM UTC) use the patched platform version. Existing tasks are retired per your task retirement settings, or you can replace them sooner as described in [Task retirement and maintenance for AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-maintenance.html).
- ECS Managed Instances: AWS has released an updated AMI, and new instances launched after the same time use the patched AMI. Existing instances are drained 14 days after launch, or earlier to align with your event windows ([Patching in Amazon ECS Managed Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-instances-patching.html)). To update immediately, [drain them manually](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-instance-draining.html).

**Bottlerocket**

The patched Bottlerocket kernel has been released. Updated Bottlerocket AMIs with the patched kernel are expected to be available beginning November 02, 2026. We recommend customers update to the latest Bottlerocket AMI when available.

**AWS Lambda**

Lambda workloads are not affected by this issue. CVE-2026-98432 requires an actor to send a specially crafted network packet to a publicly reachable IPv4 TCP port on an affected host. Lambda functions do not expose public IPv4 TCP ports, so there is no path for an external party to reach your function's execution environment with the type of traffic needed to trigger this issue. No action is required on your part.

As a defense-in-depth measure, we are proactively applying the kernel patch to the Lambda service infrastructure.

**Amazon Lightsail**

Customers running self-managed Linux instances on Amazon Lightsail are responsible for updating the kernel on those instances. If you run Amazon Linux, update the kernel package as described above. If you run another Linux distribution, follow your distribution's guidance for applying the fix when it becomes available.

After updating the kernel, a reboot is required for the fix to take effect. A kernel update and reboot is the only complete remediation for this issue.

**VPC Endpoints (PrivateLink)**

Customers running Linux targets behind AWS PrivateLink endpoint services should update the kernel on those targets and reboot, or apply the interim steps below until they can.

**VPC Lattice**

Customers running Layer 4 (TCP) targets on Linux behind VPC Lattice should update the kernel on those targets and reboot, or apply the interim steps provided below until they can.

**RDS / Aurora**

RDS / Aurora customers need to make sure that the database ports are not exposed to the internet. Additionally, we are deploying mitigations worldwide to prevent exploitation on your database hosts. Long term remediation will be for you to patch your database OS. This patch will be available Tuesday, November 3, 2026.

**Neptune**

Neptune customers need to make sure that the database ports are not exposed to the internet.

**Redshift**

Redshift is taking mitigation actions that are deploying worldwide to prevent leveraging on your cluster hosts. For long term remediation, Redshift Cluster OS patch will be available Monday, November 2, 2026.

**Storage Gateway**

We are expecting an update beginning November 03, 2026. We recommend customers update to the latest version when available.

**AWS Cloud9**

AWS Cloud9 EC2 environments install Amazon Linux and Ubuntu security updates automatically, but an updated kernel takes effect only after the environment restarts. After the update installs, customers should restart each environment's EC2 instance, or stop the environment and start it again. Canonical has not yet released a fixed kernel for Ubuntu. Customers using Ubuntu environments should restart them after the fixed kernel installs. Customers using AWS Cloud9 SSH environments are responsible for updating the kernel on their own servers.

**Amazon GameLift**

Amazon GameLift Servers is releasing updated Amazon Linux 2 and Amazon Linux 2023 AMIs that include the patched kernel. Existing managed EC2 and container fleets continue to use the AMI they were created with. To receive the fix, create a new fleet after the updated AMIs are available and move your game session traffic to it, for example by updating your game session queue destinations or aliases. Recreating the fleet is the only way to make sure every instance has the fix, because fleets launch new instances from the AMI they were created with. We'll update this bulletin when the updated AMIs are available in all Regions. Fleets running Windows are not affected.

Customers using Anywhere fleets manage their own operating system and should update the kernel and reboot, as described for Amazon EC2 above.

Note: The fix is not yet available for Amazon GameLift Servers managed fleets. Fleets you create now will not include the patched kernel. We expect updated AMIs to be available in all Regions by November 04, 2026. We recommend waiting until this bulletin is updated with a confirmation that the fix is available before you create replacement fleets.

**Amazon WorkSpaces**

Amazon WorkSpaces Windows bundles are not affected by this issue. Linux WorkSpaces use affected Linux kernels and should be updated as fixed kernels become available from the applicable operating system vendor.

In the default WorkSpaces configuration, Linux WorkSpaces do not accept inbound connections from outside the WorkSpace, and the default WorkSpaces security group allows no inbound access. Customer impact increases if customers have opened inbound ports to Linux WorkSpaces, such as SSH, or run their own TCP services, especially MPTCP-enabled services.

Amazon WorkSpaces Personal instances with Amazon Linux 2 can receive the fixed Amazon Linux kernel through existing WorkSpaces maintenance mechanisms. Customers should ensure Linux WorkSpaces can reach their operating system update repositories and should restart WorkSpaces after fixed kernels are installed so the updated kernel is active.

Amazon WorkSpaces Applications fleets and image builders with Amazon Linux 2 can receive the fixed Amazon Linux kernel by creating an updated image through the AWS CLI or SDK, or by launching and updating an existing image builder or image, and then creating a new image from that. In both cases, customers should finish by updating their fleets to use the new image.

For third-party Linux distributions such as Ubuntu, Red Hat Enterprise Linux, and Rocky Linux, fixed kernel availability depends on the respective operating system vendor. Customers should monitor their vendor's security advisories and apply updates when available. On Amazon WorkSpaces Personal instances running Ubuntu, installing a fixed kernel may not protect the running WorkSpace until the WorkSpace is restarted, unless the vendor provides an applicable livepatch that is installed and active.

AutoStop WorkSpaces that are stopped are not running and cannot be exploited while stopped; they will need to install updates and restart after they next start or during their maintenance window. Customers who disabled maintenance mode or restrict repository access should verify that updates are being applied.

Newly provisioned Linux WorkSpaces Personal instances install available operating system updates during provisioning. After fixed kernels are available from the relevant OS repository, newly created Linux WorkSpaces should start with the available fixed kernel after provisioning completes.

**AWS Database Migration Service (AWS DMS)**

AWS DMS replication instances, including those that run AWS DMS Serverless replications, do not accept inbound connections from customer networks or the internet, so there is no path for an external party to send them the traffic needed to trigger this issue.

As a defense-in-depth measure, AWS DMS will apply the patched kernel to all replication instances and to AWS DMS Serverless replications. The update will be available in all AWS Regions by November 2, 2026. AWS DMS will apply it during a weekly maintenance window, with a reboot. During the reboot, running tasks pause and resume, and tables still in full load restart. To choose when this happens, change the replication instance's maintenance window.

To get the update sooner, check whether aws dms describe-pending-maintenance-actions lists an os-patch action for your replication instance. If it does, apply it now. This reboots the instance right away:

| aws dms apply-pending-maintenance-action --replication-instance-arn --apply-action os-patch --opt-in-type immediate | 

**Amazon MQ**

Amazon MQ has released an updated host image with the patched kernel for Amazon MQ for RabbitMQ and Amazon MQ for ActiveMQ. Brokers created after November 2, 2026, 12:16 UTC use the patched kernel. Existing brokers are updated automatically during their next scheduled maintenance window, and no customer action is required. To apply the update sooner, change the broker's maintenance window to an earlier time. Rebooting a broker does not apply this update. For more information, see [Scheduling the maintenance window for an Amazon MQ broker](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/maintaining-brokers.html).


### Interim step for customers who cannot update immediately

Disable MPTCP by setting the kernel parameter net.mptcp.enabled=0, or set GODEBUG=multipathtcp=0 for applications built with Go 1.24 or later. This step reduces the conditions for running code on a host, but it does not resolve the issue. Updating the kernel and rebooting resolves the issue.

Customers can disable IP Options to mitigate this with an IP tables rule. An example is provided below:

| iptables -I INPUT 1 -m u32 --u32 '0>>24&0x0f=6:15' -j DROP | 

This rule does not persist across reboots unless saved with your distribution's tooling. Amazon Linux 2023 does not include iptables by default.

**AWS Network Firewall**

AWS Network Firewall customers can mitigate by adding the following stateful rule, which drops IPv4 packets that carry IP options. Use a SID that isn't already used in their rule groups:

| drop ip any any -> any any (msg:"CVE-2026-98432: drop IPv4 packets carrying IP options (IHL > 5)"; ipv4.hdr; bsize:>20; sid:1000001; rev:3;) | 

Your firewall policy must use strict rule order. Give this rule group a lower priority number than your allow rule groups. Traffic that your stateless rules pass skips this rule.

If your policy uses default order, create a new strict-order policy and recreate your stateful rule groups in strict order. Then switch your firewall to the new policy. This changes how all your rules are evaluated and can interrupt existing connections, so test it first and monitor after the change.


As an additional defense-in-depth measure, AWS is applying network-level protections related to this issue. These protections do not replace the recommended mitigations for this issue and we recommend customers continue to apply the guidance in this bulletin.

### **References:**

Please email [aws-security@amazon.com](mailto:aws-security@amazon.com) with any security questions or concerns.
