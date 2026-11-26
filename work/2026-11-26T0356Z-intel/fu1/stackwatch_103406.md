---
title: Juniper Session Smart Conductor OS Command Injection (AutomatedProvisioner) CVE-2026-103406 Published on October 28, 2026
url: https://stack.watch/vuln/CVE-2026-103406/
hostname: stack.watch
sitename: stack.watch
date: "2024-11-01"
fingerprint: "16385f11ad15f6a1"
language: en
filedate: "2026-11-26"
---
# Juniper Session Smart Conductor OS Command Injection (AutomatedProvisioner)

CVE-2026-103406 Published on October 28, 2026

**Session Smart Conductor: An unauthenticated attacker causes arbitrary command execution during key management.**

An Improper Neutralization of Special Elements used in an OS Command vulnerability in the AutomatedProvisioner in Juniper Networks Session Smart Conductor allows a remote attacker to execute arbitrary commands as root via a specially crafted salt minion ID.

### Vulnerability Analysis

CVE-2026-103406 is exploitable with network access, and does not require authorization privileges or user interaction. This vulnerability is considered to have a low attack complexity. The potential impact of an exploit of this vulnerability is considered to be critical as this vulnerability has a high impact to the confidentiality, integrity and availability of this component.

### Weakness Type

#### What is a Shell injection Vulnerability?

The software constructs all or part of an OS command using externally-influenced input from an upstream component, but it does not neutralize or incorrectly neutralizes special elements that could modify the intended OS command when it is sent to a downstream component.

CVE-2026-103406 has been classified to as a Shell injection vulnerability or weakness.

### Affected Versions

Juniper Networks Session Smart Conductor:
- Before 7.0.5 is affected.
- Version 7.1.0 and below 7.1.7 is affected.
- Version 7.2.0 and below 7.2.3 is affected.

### Exploit Probability

EPSS (Exploit Prediction Scoring System) scores estimate the probability that a vulnerability will be exploited in the wild within the next 30 days. The percentile shows you how this score compares to all other vulnerabilities.
