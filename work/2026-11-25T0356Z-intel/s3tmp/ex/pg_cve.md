---
title: CVE-2026-116331
url: https://www.postgresql.org/support/security/CVE-2026-116331/
hostname: postgresql.org
sitename: The PostgreSQL Global Development Group
date: "2026-11-19"
fingerprint: ef9aa91795382bd4
language: en
filedate: "2026-11-25"
---
November 19, 2026: [PostgreSQL 19 Released!](https://www.postgresql.org/about/news/postgresql-19-released-3449/)

Type confusion in PostgreSQL min/max aggregate optimization allows an object creator to execute arbitrary code as the operating system user running the database, via a user-defined aggregate whose SORTOP option causes the planner to treat the aggregate's input and result as the same type when they differ. Versions before PostgreSQL 18.7, 17.12, 16.16, 15.20, and 14.25 are affected.

| Affected Version | Fixed In | Fix Published | 
|---|---|---|
| 18 |                         [18.7](https://www.postgresql.org/docs/release/18.7)                     |            [2026-11-12](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/)          | 
| 17 |                         [17.12](https://www.postgresql.org/docs/release/17.12)                     |            [2026-11-12](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/)          | 
| 16 |                         [16.16](https://www.postgresql.org/docs/release/16.16)                     |            [2026-11-12](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/)          | 
| 15 |                         [15.20](https://www.postgresql.org/docs/release/15.20)                     |            [2026-11-12](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/)          | 
| 14 |                         [14.25](https://www.postgresql.org/docs/release/14.25)                     |            [2026-11-12](https://www.postgresql.org/about/news/postgresql-187-1712-1616-1520-1425-and-19-rc-2-released-3442/)          | 

For more information about [PostgreSQL versioning](https://www.postgresql.org/support/versioning/),
  please visit the [versioning page](https://www.postgresql.org/support/versioning/).

| Overall Score | **8.8** | 
|---|---|
| Component | core server | 
| Vector |            [AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H&version=3.0)          | 

If you wish to report a new security vulnerability in PostgreSQL, please
  send an email to
  [security@postgresql.org](mailto:security@postgresql.org).

For reporting non-security bugs, please see the [Report a Bug](https://www.postgresql.org/account/submitbug/) page.
