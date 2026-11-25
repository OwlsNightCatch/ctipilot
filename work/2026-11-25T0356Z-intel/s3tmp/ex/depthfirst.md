---
title: "Narrow Grants, Wide Engines: Reaching Native Database Attack Surface from Minimal SQL Roles"
author: Zheng Yu
url: https://depthfirst.com/research/narrow-grants-wide-engines
hostname: depthfirst.com
description: How minimally privileged SQL roles can reach native database engine vulnerabilities, with PostgreSQL and MySQL exploit chains and a reproduced ClickHouse vulnerability.
sitename: Depthfirst
date: "2026-11-18"
fingerprint: "27b9983f259e2250"
language: en
image: https://depthfirst.com/uploads/narrow-grants-wide-engines/cover.png
pagetype: article
filedate: "2026-11-25"
---
# Narrow Grants, Wide Engines: Reaching Native Database Attack Surface from Minimal SQL Roles

## Overview

Database access controls are usually modeled as a hard security boundary: if an application or tenant connects under a low-privilege role, it should only be able to read or modify the schemas and tables explicitly granted to it. From an offensive security perspective, however, SQL authorization only restricts logical objects. The practical strength of that boundary still depends on the memory safety and logic correctness of every C and C++ subsystem reachable from permitted SQL statements. Even heavily locked-down accounts can exercise query optimizers, stateful aggregate evaluators, prepared-statement resolvers, and binary wire-protocol parsers. A single memory corruption bug in any of those paths collapses the SQL privilege model into arbitrary command execution under the database’s OS service account.

[Oracle’s November security update](https://www.oracle.com/security-alerts/cspunov2026.html) fixes CVE-2026-114819 (CVSS 9.9), a vulnerability we reported in Oracle AI Database. It chains directly with [CVE-2026-91609](https://www.oracle.com/security-alerts/cpuoct2026.html), a flaw in Oracle’s GraphQL interface that we disclosed in October. Together, the two vulnerabilities allow an unauthenticated attacker with access only to the exposed HTTP endpoint to smuggle a crafted document into the database and execute arbitrary commands as the database’s OS service user.

To see whether this exposure was specific to Oracle, we audited what native engine code remains reachable to minimally privileged accounts in PostgreSQL and MySQL, identifying full RCE chains in both. Together, Oracle, MySQL, and PostgreSQL hold three of the top four spots in the November 2026 [DB-Engines ranking](https://db-engines.com/en/ranking), and their role models underpin major multi-tenant and production environments. PostgreSQL sits beneath managed offerings including Amazon RDS, Neon, and Supabase, while MySQL backs core production workloads at organizations such as [GitHub](https://github.blog/engineering/infrastructure/partitioning-githubs-relational-databases-scale/) and [Shopify](https://shopify.engineering/scaling-inventory-reservations).

Across the bugs we found in Oracle AI Database, PostgreSQL, and MySQL, alongside recent vulnerabilities reported by others, the underlying dynamic is consistent. Restrictive SQL grants leave a surprisingly broad native attack surface intact, and the session-local features left open to unprivileged roles (such as temporary schemas, temporary tables, and bound parameters) double as reliable building blocks for heap grooming, ASLR bypasses, and control-flow hijacking (In Oracle’s case, the chain reaches vulnerable engine code before login even occurs). Because Oracle AI Database is closed-source, this post walks through the root causes, exploit primitives, and privilege requirements using our PostgreSQL and MySQL chains together with a reproduced vulnerability in ClickHouse.

## PostgreSQL: From Default Login Role to RCE

### Root cause: `SORTOP` optimization skips `FINALFUNC`

PostgreSQL allows users to define custom aggregate functions modeled on built-ins like `SUM` and `MAX`. Each aggregate specifies a **transition function** (`SFUNC`), which folds incoming row values one by one into a running state (`STYPE`), and an optional **final function** (`FINALFUNC`), which converts the finished state into the aggregate’s declared output type. For instance, an aggregate might accept integers, track the maximum integer seen so far in its state, and convert that integer to `text` at the end: given inputs `3`, `8`, and `5`, the transition state finishes at `8` and the final function returns `"8"`.

Scanning an entire table through `SFUNC` is wasteful if an aggregate behaves like `MIN` or `MAX` over an indexed column. To let user-defined aggregates opt into the same planner fast path, PostgreSQL supports a `SORTOP` parameter on [`CREATE AGGREGATE`](https://www.postgresql.org/docs/18/sql-createaggregate.html), declaring that the aggregate’s output corresponds to the extremal input value ordered by that operator. When a query shape qualifies and a compatible B-tree index exists, the planner rewrites the aggregate into an index lookup that fetches the extremal tuple directly. `SORTOP` is strictly opportunistic: if no suitable index is available or the query is ineligible for the rewrite, execution falls back to running `SFUNC` across the input rows followed by `FINALFUNC`.

The bug in [CVE-2026-116331](https://www.postgresql.org/support/security/CVE-2026-116331/) is that [this planner shortcut](https://github.com/postgres/postgres/commit/0eba29495584b72ce9d3ee8b754b48d964b7222c) failed to account for `FINALFUNC` changing the result’s return type. In the integer-to-text example above, the normal execution path invokes `FINALFUNC` and hands the caller a `text` datum (`"8"`). The `SORTOP` index path skips `FINALFUNC` altogether and returns the raw indexed integer `8`, while the outer expression evaluator still expects `text`. On 64-bit builds, PostgreSQL passes fixed-width `int8` values directly by value inside an 8-byte `Datum`, whereas variable-length types such as `text` and `bytea` are passed by reference as pointers. Skipping `FINALFUNC` causes PostgreSQL to interpret raw integer bits from the index as a pointer to `text`, yielding a clean pass-by-value / pass-by-reference type confusion.

### Exploitation: Building infoleak and `fakeobj` primitives in `pg_temp`

At first glance, turning this planner bug into an exploit from an unprivileged session looks difficult. Triggering the fast path requires an indexed table populated with attacker-chosen values, as well as permission to create custom functions and an aggregate. A default role (here meaning a freshly created PostgreSQL login role with zero additional grants) has no write permissions on existing application tables and cannot create objects in public on hardened setups.

What bridges the gap is PostgreSQL’s session-local temporary schema. Out of the box, a default login role [inherits TEMPORARY privilege on the database](https://www.postgresql.org/docs/18/ddl-priv.html). Inside pg\_temp, the role can create temporary tables, populate them with arbitrary values, build B-tree indexes over them, and define helper functions and custom aggregates without ever touching an application schema. The setup below triggers the confusion entirely inside pg\_temp (function bodies and payload constants omitted):

```
-- Every object lives in the role's temporary schema.
CREATE TEMP TABLE t (v int8);
CREATE INDEX ON t (v);
INSERT INTO t VALUES (...);              -- attacker-chosen value
CREATE FUNCTION pg_temp.keep_max(int8, int8) RETURNS int8 ...;
CREATE FUNCTION pg_temp.as_text(int8)        RETURNS text ...;
CREATE AGGREGATE pg_temp.confused(int8) (
  SFUNC     = pg_temp.keep_max,
  STYPE     = int8,
  FINALFUNC = pg_temp.as_text,   -- declares a text result
  SORTOP    = '>'                -- enables the index shortcut
);
SELECT pg_temp.confused(v) FROM t;  -- index path returns int8; caller reads text
```
Because the role can instantiate this pattern repeatedly across arbitrary type pairs on 64-bit PostgreSQL, a single bug provides every primitive needed for a reliable, multi-stage exploit:

1. **Heap pointer leak (`bytea` confused as `int8`):** By indexing a `bytea` column (whose `Datum` holds a 64-bit heap pointer) under an aggregate whose `FINALFUNC` declares `int8`, the index shortcut returns the raw `bytea` pointer directly to the SQL client as a 64-bit integer. This gives an immediate `addrof`-style leak of attacker-controlled heap data.
2. **Bounded memory read and ASLR bypass (`int8` confused as pointer):** Reversing the type mismatch makes PostgreSQL dereference an attacker-chosen `int8` value as a pointer, providing bounded reads around arbitrary addresses. Probing near the leaked heap buffer reveals a code pointer into the `postgres` binary, defeating PIE/ASLR. Repeating the `bytea`-to-`int8` leak then pinpoints the heap address of the final fake object payload.
3. **Control-flow hijack via expanded objects (`int8` confused as `text`):** For the final stage, the attacker stores the 64-bit address of crafted payload bytes in an indexed `int8` column and confuses the output into `text`. PostgreSQL’s variable-length representation supports in-memory [**expanded objects**](https://www.postgresql.org/docs/18/xtypes.html), headed by an `ExpandedObjectHeader` containing a method-table pointer (`eoh_methods`). Passing the forged `text` datum to `length()` triggers an indirect call through `eohptr->eoh_methods->get_flat_size(eohptr)`. Since both `eohptr` and `eoh_methods` reside in attacker-controlled memory, the call pivots into a short instruction sequence that invokes `system()`.

This chain highlights why reachable subsystem breadth matters just as much as the initial bug. `TEMPORARY` access doesn’t merely allow a default role to reach the buggy `SORTOP` planner path; it gives the attacker on-demand tables, B-tree indexes, polymorphic `Datum` conversions to defeat ASLR, and built-in expression sinks like `length()`, all with zero access to application data.

## MySQL: Out-of-Bounds Bit-Counter Increments

### Root cause: Prepare-time sizing vs. execution-time length

[CVE-2026-101786](https://dev.mysql.com/community/security/advisories/2026-10-20/) is an out-of-bounds write in MySQL’s windowed `BIT_OR` aggregates. Unlike a standard `GROUP BY` bitwise aggregate, a sliding window has to subtract a row’s bits as it leaves the frame. MySQL handles this by maintaining an array of 64-bit counters on the session memory arena, allocating one counter per input bit.

When a prepared statement such as `SELECT BIT_OR(?) OVER (...)` uses a parameter whose concrete type is not yet known at prepare time, [`Item_sum_bit::resolve_type()`](https://github.com/mysql/mysql-server/blob/mysql-26.7.0/sql/item_sum.cc) assumes a 511-byte binary `VARCHAR` and allocates 4,088 counters (32,704 bytes). At execution time, however, the client can bind a longer `BLOB` value. `Item_sum_bit::add_bits()` looped over the actual runtime length without re-checking the 511-byte limit; its only array-bounds check was a debug `assert` compiled out of release builds.

The [upstream patch](https://github.com/mysql/mysql-server/commit/21e41643ce19a75d54923278e6f47dd1a1379e12) rejects oversized values at runtime before updating the counters:

```
buff_length = s1->length();
if (m_is_window_function && !m_is_xor &&
    buff_length > m_digit_cnt_card / 8) {
  my_error(ER_INVALID_BITWISE_AGGREGATE_OPERANDS_SIZE,
           MYF(0), func_name());
  return true;
}
```
### Exploitation: Shaping the arena and nudging cleanup pointers

Without that check, binding a 512-byte parameter causes the final byte to index counters 4,088 through 4,095, eight 64-bit slots (64 bytes) past the end of the allocation. Each set bit in that 512th byte adds `1` to its corresponding slot per row evaluated in the window. Rather than an arbitrary 64-byte overwrite, the bug gives a selective, repeatable 64-bit increment primitive whose total offset equals the number of rows processed.

Ordinary session features turn that constrained increment into reliable code execution on the official MySQL 26.7.0 image:

1. **Arena layout control:** Setting `query_alloc_block_size = 65536` for the session places the counter array directly in front of an internal expression node (`Item_ref`), lining up one of the eight out-of-bounds slots with its `next_free` teardown pointer.
2. **Exact pointer increment via temporary tables:** Using `CREATE TEMPORARY TABLES ON *.*`, the session creates a temporary table, fills it with 184 rows via a recursive CTE, and runs the prepared window query over it. Processing 184 rows advances `next_free` by 184 bytes so that it points at the bound parameter object instead.
3. **Teardown hijack:** When the statement finishes and cleans up its expression list, MySQL follows the shifted `next_free` pointer into the 512-byte parameter buffer, treats the attacker-controlled bytes as a C++ object, and dispatches a virtual call. Pivoting the stack into that buffer lets a short ROP chain resolve `system()` from the GOT and execute commands as the `mysql` service account.

The tested user held only `CREATE TEMPORARY TABLES ON *.*` and needed no `SELECT` access to any existing application table.

## ClickHouse: Length Wraparound in `RowBinary`

### Root cause: Unchecked length addition without a size limit

In ClickHouse’s [`RowBinary`](https://clickhouse.com/docs/reference/formats/RowBinary/RowBinary) format, a `String` value is sent as a variable-length integer followed by its raw bytes. As rows arrive, the [string deserializer](https://github.com/ClickHouse/ClickHouse/blob/v26.7.5.10-stable/src/DataTypes/Serializations/SerializationString.cpp) appends each string into a flat byte vector, calculating the new buffer size by adding the declared string length to the vector’s existing size:

```
UInt64 size = 0;
readVarUInt(size, istr);
if (settings.binary.max_binary_string_size &&
    size > settings.binary.max_binary_string_size)
    throw Exception(...);
size_t old_chars_size = data.size();
size_t offset = old_chars_size + size;
offsets.push_back(offset);
try {
    data.resize(offset);
    istr.readStrict(reinterpret_cast<char *>(&data[offset - size]), size);
} catch (...) {
    offsets.pop_back();
    data.resize_assume_reserved(old_chars_size);
    throw;
}
```
Normally, the `format_binary_max_string_size` setting rejects absurdly large lengths up front. However, an unprivileged HTTP caller can pass `format_binary_max_string_size=0` in the query string under the default configuration, disabling that policy check and exposing the unchecked `old_chars_size + size` addition.

If the first row writes 64 bytes (`old_chars_size == 64`) and the second row declares a length of `UINT64_MAX`, 64-bit unsigned addition wraps `offset = 64 + UINT64_MAX` around to `63`, while `offset - size` wraps back to `64`. Calling `data.resize(63)` shrinks the vector’s logical length by one byte without freeing or reallocating its backing heap buffer. The subsequent read then starts writing at offset 64, copying every remaining byte from the HTTP request body (6,144 controlled bytes in our PoC) past the buffer into adjacent heap memory before hitting end-of-stream and throwing a short-read exception. By the time the `catch` block restores the vector’s metadata, the surrounding heap has already been overwritten.

### Exploitation: `Memory` table grooming and virtual call hijack

To exploit the overflow on ClickHouse 26.7.5.10, our PoC first creates a temporary `Memory` table and inserts crafted rows to groom the heap, then triggers the wrapped write through `INSERT INTO FUNCTION null('a String') FORMAT RowBinary` with `format_binary_max_string_size=0`. The 6,144-byte overflow plants forged vtable pointers and command strings into neighboring C++ objects so that a later virtual call redirects into `system()` under the `clickhouse` service account. Using an account granted only `CREATE TEMPORARY TABLE ON *.*`, our exploit obtained an interactive shell as the `clickhouse` service account.

## Takeaways: SQL Grants vs. Reachable Engine Code

Looking across Oracle, PostgreSQL, MySQL, and ClickHouse, SQL `GRANT`s do what they were designed to do—gate access to persistent schemas and tables, while barely narrowing how much of the underlying C and C++ engine a session can exercise. Unlike an OS syscall filter that can wall off entire kernel subsystems, a database session allowed to run queries still drives planner shortcuts, sliding-window state machines, and binary wire deserializers directly.

Just as important for exploit development, scratch privileges that look harmless from a data-access standpoint (`TEMPORARY` granted to `PUBLIC` by default in PostgreSQL, or `CREATE TEMPORARY TABLES` in MySQL and ClickHouse) hand an attacker everything needed to turn subtle memory corruption bugs into code execution without touching production tables. Revoking default `TEMPORARY` privileges in PostgreSQL or avoiding broad `CREATE TEMPORARY TABLES ON *.*` grants when applications do not need them raises the bar against post-authentication exploits, though pre-login paths like our Oracle chain bypass SQL role checks altogether. Least-privilege roles are still essential for isolating data under normal operation, but a short output from `SHOW GRANTS` does not mean a small native attack surface.
