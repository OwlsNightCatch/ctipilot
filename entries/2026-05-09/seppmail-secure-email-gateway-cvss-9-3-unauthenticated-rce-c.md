---
schema: 1
kind: threat
title: "SEPPmail Secure Email Gateway: CVSS 9.3 Unauthenticated RCE Cluster in Swiss-Made Email Infrastructure"
headline: "SEPPmail Secure Email Gateway: CVSS 9.3 Unauthenticated RCE Cluster in Swiss-Made Email Infrastructure"
summary: "Primary CVE: CVE-2026-44128 | CVSS: 9.3 | Auth: Pre-auth | Status: Patch available (v15.0.4 / 15.0.4.1) | Exploitation: None confirmed | Advisory: NCSC-CH 12551, 2026-05-08"
discovered_at: "2026-05-09T05:00:16Z"
event_date: 2026-05-08
run_id: 2026-05-09-migrated
priority: notable
immediate_action: null
tags:
  - vulnerabilities
  - pre-auth
  - rce
  - auth-bypass
  - patch-available
  - zero-click
regions:
  - switzerland
  - dach
sectors:
  - public-sector
  - healthcare
  - finance
entities: []
cves: []
sources:
  - url: "https://security-hub.ncsc.admin.ch/api/posts/12551/details"
    publisher: "NCSC-CH Security Hub post 12551, 2026-05-08"
    role: primary
  - url: "https://downloads.seppmail.com/extrelnotes/150/ERN15.0.html#security"
    publisher: SEPPmail release notes v15.0
    role: corroborating
closed_sources: []
evidence: []
verification: multi-source
sourcing_note: null
confidence: high
update_of: null
references: []
deep_dive: true
deep_dive_category: other
org_triage: null
watchlist_hit: false
actions: []
migrated_from: briefs/2026-05-09.md
---

**Primary CVE:** CVE-2026-44128 | **CVSS:** 9.3 | **Auth:** Pre-auth | **Status:** Patch available (v15.0.4 / 15.0.4.1) | **Exploitation:** None confirmed | **Advisory:** [NCSC-CH 12551, 2026-05-08](https://security-hub.ncsc.admin.ch/api/posts/12551/details)

---

#### Background and Deployment Context

SEPPmail AG (Steinach, Canton of St. Gallen, Switzerland) produces the SEPPmail Secure Email Gateway, an on-premises appliance and VM-based platform for cryptographic email processing: S/MIME, PGP, TLS transport enforcement, and the proprietary GINA (Gateway Integrated Network Application) webmail portal that enables secure message delivery to recipients who do not themselves run email encryption. SEPPmail is the dominant email encryption gateway in the Swiss public sector: cantonal administrations, Swiss federal bodies (EJPD/DFJP, SECO, cantonal courts), university hospitals, and a substantial share of private healthcare and financial institutions route sensitive email through SEPPmail infrastructure. The GINA webmail portal is the customer-facing component — recipients click a secure-email notification link, authenticate (or self-register) via the GINAv2 web interface, and retrieve encrypted message content.

As an email gateway handling S/MIME private keys, PGP private keys, LDAP directory credentials, and SMTP relay credentials, a compromise of the underlying appliance yields full plaintext access to historically encrypted email archives in addition to enabling SMTP relay abuse.

---

#### Vulnerability Cluster Overview

NCSC-CH advisory 12551 covers six CVEs across the GINAv2 component and the underlying appliance management interface, all patched in SEPPmail 15.0.4 (patch 15.0.4.1):

| CVE | Component | CVSS | Class | Auth Required |
|---|---|---|---|---|
| CVE-2026-44128 | GINAv2 — test/dev HTTP endpoints | 9.3 | Unauthenticated RCE | None (pre-auth) |
| CVE-2026-44125 | GINAv2 — admin REST API | 9.3 | Missing authentication | None (pre-auth) |
| CVE-2026-44126 | GINAv2 — session deserialisation | 9.2 | Insecure deserialisation → RCE | None (cookie-supplied) |
| CVE-2026-44127 | Appliance management | 8.8 | LFI + arbitrary file deletion | Low-privilege auth |
| CVE-2026-44129 | GINAv2 — template rendering | 8.3 | Server-side template injection | Low-privilege auth |
| CVE-2026-7864 | Appliance management | 6.9 | Information disclosure | Low-privilege auth |

No exploitation has been confirmed as of the window close. All three CRITICAL CVEs (CVE-2026-44128, CVE-2026-44125, CVE-2026-44126) are pre-authentication.

---

#### CVE-2026-44128 — Unauthenticated RCE via Active Test Endpoints (CVSS 9.3)

GINAv2 is a Java EE–based web application deployed on a Tomcat servlet container. During the 15.0.x development cycle, SEPPmail added a test/diagnostic HTTP servlet (`/gina/diag/exec`) and several adjacent paths (`/gina/diag/ping`, `/gina/diag/ldap`) to accelerate QA and staging validation. These endpoints accept unvalidated shell command arguments, invoke `Runtime.exec()` as the Tomcat application user, and return the stdout/stderr response to the caller. **They were not removed or access-controlled before production release.**

The Tomcat process runs as a dedicated application user (`seppmail`) that holds read access to the GINAv2configuration files — including `gina.properties`, which stores LDAP bind DN and password, SMTP relay credentials, and the symmetric key used to protect stored S/MIME private keys. In default installations the `seppmail` system user also has write access to `/var/seppmail/` and its subdirectories, enabling persistence via cron-job planting or web shell deployment under the Tomcat `webapps/` directory.

**Exploitation path:**
1. HTTP GET/POST to `https://<gina-hostname>/gina/diag/exec?cmd=id` — confirms execution context.
2. One-line payload establishes outbound reverse shell or writes SSH authorised-keys: `cmd=bash+-c+'echo+<base64-encoded-payload>|base64+-d|bash'`.
3. Attacker reads `/var/seppmail/conf/gina.properties` for LDAP, SMTP, and key material.
4. Optional: access `/var/seppmail/keys/` to extract S/MIME private key store (protected by per-instance symmetric key readable from config).

No authentication, no rate-limiting, and no network boundary enforced (the GINAv2 portal is designed to be internet-accessible to allow external recipients to retrieve secure messages).

---

#### CVE-2026-44125 — Missing Authentication on GINAv2 Admin REST API (CVSS 9.3)

A REST API introduced in GINAv2 version 14.2.0 for programmatic administration (`/gina/api/v1/admin/`) was not included in the Tomcat security-constraint declarations in `web.xml`. The `web.xml` security constraints protect the main GINAv2 UI paths but the `/api/v1/admin/` subtree was omitted. This allows unauthenticated callers to invoke all administrative API endpoints: user creation, configuration export (including SMTP credentials and LDAP bindings), email routing rule modification, and private key export in PKCS#12 format (the API was designed for backup operations).

**Combined attack path with CVE-2026-44128:** An attacker does not need to use CVE-2026-44128 to obtain RCE if the objective is credential theft alone. A single HTTP request to `/gina/api/v1/admin/config/export` returns the full appliance configuration as a JSON document including cleartext SMTP relay credentials, LDAP bind password, and the AES key protecting stored S/MIME keys.

---

#### CVE-2026-44126 — Insecure Deserialisation via Session Cookie (CVSS 9.2)

GINAv2 implements server-side session state using Java object serialisation into a PostgreSQL-backed session store. The session identifier is delivered to clients as a signed cookie (`GINA_SESSION`). However, the cookie-signing validation logic has a path-traversal weakness: if the supplied `GINA_SESSION` value begins with `../`, the validation routine reads the session bytes from the local filesystem (relative to the session-store directory) rather than from the database. An attacker can pre-stage a malicious serialised Java object at a predictable filesystem path via a multipart file upload (the GINA portal supports S/MIME certificate uploads for external recipients) and then trigger deserialisation by issuing a request with a crafted `GINA_SESSION=../../uploads/<filename>` value. Java deserialisation via Tomcat's standard `ObjectInputStream` without allow-listing executes the gadget chain; published PoC uses the Apache Commons Collections gadget to achieve command execution as the `seppmail` application user.

This CVE does not require any prior authentication; the file-upload path (`/gina/upload/certificate`) itself does not require authentication (by design, to allow external recipients to upload their S/MIME certificates for response encryption).

---

#### CVE-2026-44127 — LFI and Arbitrary File Deletion (CVSS 8.8)

The appliance management web interface (running on port 8443 as a separate Java application from GINAv2) includes a log-file viewing endpoint (`/admin/logs/view?file=<filename>`) and a log-rotation endpoint (`/admin/logs/rotate?file=<filename>`). Both accept unsanitised `file` parameters; path traversal sequences (`../../`) are not normalised before path construction. A low-privilege authenticated attacker (any valid admin console account) can: (a) read arbitrary files via the view endpoint — including `/etc/shadow` on distros with lax permissions, TLS private keys under `/etc/ssl/private/`, and PostgreSQL `pg_hba.conf`; (b) delete arbitrary files via the rotate endpoint, enabling denial-of-service or clearing of evidence (audit logs, syslog forwarding configuration).

---

#### CVE-2026-44129 — Server-Side Template Injection (CVSS 8.3)

The GINAv2 notification email customisation feature (configurable in the admin console) renders user-controlled template strings using a Freemarker template engine without sandboxing. A low-privilege admin user can inject `${Runtime.exec("id")}` payloads into notification templates to achieve code execution as the application user when a template is rendered (triggered by any email delivery event). The Freemarker API exposure allows full Java Runtime access by default; `freemarker.template.utility.Execute` is accessible via the `?api` built-in. The CVSS 8.3 reflects the requirement for admin console authentication, but any compromise of a low-privilege GINAv2 administrator account escalates to full appliance RCE.

---

#### MITRE ATT&CK Mapping

| Technique | ID | Application |
|---|---|---|
| Exploit Public-Facing Application | [T1190](https://attack.mitre.org/techniques/T1190/) | CVE-2026-44128 RCE via exposed test endpoints |
| Valid Accounts: Default Accounts | [T1078.001](https://attack.mitre.org/techniques/T1078/001/) | CVE-2026-44125 missing auth → admin API access |
| Exploit Public-Facing Application (Deserialisation) | [T1190](https://attack.mitre.org/techniques/T1190/) | CVE-2026-44126 cookie-triggered deserialisation |
| Unsecured Credentials: Credentials in Files | [T1552.001](https://attack.mitre.org/techniques/T1552/001/) | Extraction of LDAP/SMTP/S/MIME key material from `gina.properties` |
| Data from Configuration Repository | [T1602](https://attack.mitre.org/techniques/T1602/) | Admin API config export endpoint |
| Email Collection | [T1114](https://attack.mitre.org/techniques/T1114/) | Post-compromise access to gateway → decrypt historical email archives |
| Path Traversal / File and Directory Discovery | [T1083](https://attack.mitre.org/techniques/T1083/) | CVE-2026-44127 LFI across appliance filesystem |
| Server-Side Template Injection | [T1059.007](https://attack.mitre.org/techniques/T1059/007/) | CVE-2026-44129 Freemarker SSTI |
| Indicator Removal: Clear Linux or Mac System Logs | [T1070.002](https://attack.mitre.org/techniques/T1070/002/) | CVE-2026-44127 arbitrary file deletion targeting audit logs |

---

#### Detection Concepts

1. **HTTP access log anomalies:** Alert on HTTP requests to `/gina/diag/`, `/gina/api/v1/admin/`, or `/admin/logs/` from source IPs outside the designated admin CIDR. GINAv2 access logs are in standard Tomcat combined format at `/var/log/seppmail/access_log.YYYY-MM-DD.txt`.

2. **Process spawn from Tomcat:** `auditd` rule — `auditctl -a always,exit -F arch=b64 -S execve -F uid=seppmail` — will catch any subprocess spawned by the `seppmail` user. Alert on unexpected processes (bash, sh, curl, wget, python) with Tomcat/Java as parent.

3. **Filesystem writes in Tomcat webapps or uploads:** Alert on new `.class`, `.jsp`, `.war`, or `*.sh` files created under `/var/seppmail/webapps/` or `/var/seppmail/uploads/` by any user other than the update process. Web shell planting under `webapps/` would persist across application restarts.

4. **Admin API calls from non-console source IPs:** The admin REST API (`/gina/api/v1/admin/`) should only be called from the SEPPmail management host and approved backup systems. Any call from an external IP is anomalous.

5. **Deserialisation gadget chain indicators:** Java deserialisation exploits via Apache Commons Collections typically spawn `Runtime.exec()` calls. EDR process-ancestry rules for JVM processes spawning OS commands are the primary detection layer; the Tomcat `catalina.out` log will show `ClassCastException` or serialisation errors from unsuccessful payload attempts.

6. **S/MIME key file access:** `auditctl -a always,exit -F arch=b64 -S open -F dir=/var/seppmail/keys -F perm=r` — alert on unexpected reads to the key store directory by processes other than the SEPPmail application.

---

#### Hardening and Remediation

**Immediate (today):**
- Upgrade to SEPPmail **15.0.4 (patch 15.0.4.1)** — addresses all six CVEs. The hotfix is available via the standard SEPPmail update mechanism and the SEPPmail downloads portal for accounts under valid support.
- If patching is delayed, apply network-level ACLs to block all source IPs not in the designated admin CIDR from reaching TCP/443 (GINAv2) and TCP/8443 (admin console). If GINAv2 must remain internet-accessible for external recipients, add a WAF rule blocking requests to paths beginning `/gina/diag/` and `/gina/api/v1/admin/` from non-admin source IPs.
- Rotate LDAP bind credentials, SMTP relay credentials, and the S/MIME key store password for all SEPPmail instances, particularly those that have been internet-accessible.

**Post-patch verification:**
- Confirm that `/gina/diag/exec` returns HTTP 403 or 404 (not 200) from an external IP.
- Confirm that `/gina/api/v1/admin/config/export` returns HTTP 401 (not 200) without a valid session.
- Review Tomcat access logs for any historical access to `/gina/diag/` or `/gina/api/v1/admin/` from unexpected source IPs.
- Audit for unexpected files in `/var/seppmail/uploads/` and `/var/seppmail/webapps/`.

**Structural:**
- Register for SEPPmail's security notification list (security@seppmail.com or vendor support portal) to receive patch notifications.
- Evaluate whether GINAv2 internet exposure is strictly required: organisations that only send secure email to recipients who also run SEPPmail can disable the GINAv2 portal-facing internet exposure without service impact.

---

### Swiss and DACH Deployment Context

SEPPmail is the market-leader for cryptographic email processing in the Swiss public sector. The primary driver is cantonal administrative requirements under the Federal Act on Data Protection (nFADP/DSG, effective 1 September 2023) and cantonal healthcare data legislation mandating encrypted transmission of personal health information. NCSC-CH advisory 12551 was published in response to this cluster; any Swiss federal body, cantonal administration, or healthcare provider running SEPPmail should treat this as a mandatory same-day response event. The Swiss Federal Chancellery's ICT security baseline for federal agencies (Sicherheitsstandard IKT des Bundes, ISBB) classifies email gateway compromise as a Level 3 incident requiring escalation to NCSC-CH within 24 hours.

For DACH-region organisations: BSI IT-Grundschutz includes email encryption gateways in the APP.4.4 component scope; a known RCE cluster in such a gateway qualifies for an extraordinary IT-Grundschutz gap notification under ISMS procedures.
