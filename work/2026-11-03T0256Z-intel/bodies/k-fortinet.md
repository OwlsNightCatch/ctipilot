# extract: served via trafilatura-direct
---
title: PSIRT | FortiGuard Labs
url: https://fortiguard.fortinet.com/psirt/FG-IR-26-188
hostname: fortinet.com
description: "None"
sitename: FortiGuard Labs
date: "2026-11-02"
fingerprint: a36349579ebe8ed5
---
# Linux kernel RCE CVE-2026-98432

## Summary

CVE-2026-98432:

ipv4: free inet\_opt and ireq\_opt after an RCU grace period tcp\_v4\_syn\_recv\_sock() transfers ownership of ireq->ireq\_opt to the child socket (newinet->inet\_opt) without copying it. Another cpu can concurrently process a retransmitted SYN for the same request socket, and send a SYNACK from tcp\_check\_req(). tcp\_v4\_send\_synack() and inet\_csk\_route\_req() read ireq->ireq\_opt under rcu\_read\_lock() only, and ip\_build\_and\_send\_pkt() and ip\_options\_build() then read opt->optlen twice. Note that the SYNACK timer itself is not an issue: it holds a reference on its request socket, and inet\_csk\_reqsk\_queue\_drop() calls timer\_delete\_sync() before the child can be freed. Since commit 079096f103fa ("tcp/dccp: install syn\_recv requests into ehash table"), request sockets are processed without holding the listener lock, so nothing prevents the child socket from being freed while the SYNACK is still being built. TCP child sockets do not have SOCK\_RCU\_FREE, and inet\_sock\_destruct() frees inet\_opt with a plain kfree(), leading to a use-after-free in ip\_options\_build(). A similar issue exists with request socket migration (net.ipv4.tcp\_migrate\_req=1, or a BPF\_SK\_REUSEPORT\_SELECT\_OR\_MIGRATE program). reqsk\_timer\_handler() clones the request socket with inet\_reqsk\_clone(), so that the old request socket and its clone share the same ireq\_opt, then reqsk\_migrate\_reset() clears the pointer in the old one. Another cpu holding a reference on the old request socket can still be using these options (sending a SYNACK, or creating a child in tcp\_v4\_syn\_recv\_sock()) when the clone is freed, and tcp\_v4\_reqsk\_destructor() also uses a plain kfree(). Readers already use RCU, and other paths replacing inet\_opt (do\_ip\_setsockopt(), cipso\_v4\_sock\_setattr()...) already use kfree\_rcu(). Use kfree\_rcu() in inet\_sock\_destruct() and tcp\_v4\_reqsk\_destructor() as well. IPv6 is not affected by the first issue, because tcp\_v6\_syn\_recv\_sock() duplicates the options. tcp\_v6\_reqsk\_destructor() has the same migration issue with ipv6\_opt, which is only set by CALIPSO. This will be addressed in a separate patch.

###### Fortinet is currently investigating the impact of the CVE over Fortinet Products.

#### Products under investigation:

FortiADC Manager

FortiAIOps

FortiAnalyzer-BigData

FortiAppSec Cloud

FortiCASB

FortiCNAPP

FortiCamera Cloud

FortiConverter

FortiDDoS

FortiDDoS-F

FortiDAST

FortiDevSec

FortiEDR

FortiEdge Cloud

FortiExtender

FortiFone

FortiGate Cloud

FortiMail

FortiMail Cloud

FortiMonitor

FortiNAC

FortiNAC-F

FortiNDR

FortiNDR Cloud

FortiPAM

FortiPortal

FortiRecon

FortiRecorder

FortiSIEM

FortiSandbox PaaS

FortiSASE

FortiSIEM Cloud

FortiSwitch

FortiSwitch NMS

FortiTelemetry

FortiVoice

FortiWeb Manager

FortiZTP

FortiOS

FortiAP

FortiProxy

FortiSwitch Manager

FortiManager 

FortiAnalyzer 

FortiManager Cloud

FortiAnalyzer Cloud

FortiAP-U

FortiClient EMS

FortiAuthenticator

FortiWeb

FortiSOAR

FortiSOAR SaaS

FortiPresence

FortiADC

FortiCamera

FortiClient Cloud

FortiSOAR

FortiDeceptor

FortiVoice UC

FortiSandbox

## Virtual Patch

No
## Timeline

2026-11-02: Initial publication
