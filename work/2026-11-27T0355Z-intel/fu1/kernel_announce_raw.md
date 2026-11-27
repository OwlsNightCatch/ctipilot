Title: 

URL Source: https://lore.kernel.org/linux-cve-announce/2026111950-CVE-2026-99362-c6f2@gregkh/raw

Markdown Content:
From mboxrd@z Thu Jan  1 00:00:00 1970
Authentication-Results: smtp.subspace.kernel.org; arc=none smtp.remote-ip=100.103.45.18
ARC-Seal: i=1; d=subspace.kernel.org; s=arc20261015; a=rsa-sha256; cv=none;
	t=1795099054;
	b=NbfDw1zVNwdts4ROnXWOhVr+qPddMpu24gQ2evuOcqqXzgv/wMKIG5PXyBH/7fvreJgr
	 a9XXWAIwTagfI/KxZAMkWoFTiQhpLokM+GqTW3jGo2CBpBMCwgU+5Y3CRkQDwK0o54+w5
	 062tqk5ePlmQprw8IBefMUI6cr/jQNgEB+JnCxNvgG78h141MI0BeRyQTSZyNzwvvtaAW
	 77yisGTVnk/drVPrBvBxnrSEoqRzbk6O5+euKMCjSizjB3k9fsYSv8RvE9MgCcx5+rAYp
	 dR5Fmsyv0hVDoDZM2T+Gbv2pHbIPeCqA8R9UYLSM1IMRcsGlYZfnsII0JxZGRc0YwFA==
ARC-Message-Signature: i=1; d=subspace.kernel.org; s=arc20261015;
	a=rsa-sha256; c=relaxed/relaxed; t=1795099054;
	h=Received:DKIM-Signature:From:To:Cc:Subject:Date:Message-ID:X-Mailer:
	 Reply-To:MIME-Version:Lines:X-Developer-Signature:X-Developer-Key:
	 Content-Transfer-Encoding;
	bh=cBbuSXkHtO9lavvvNsCUJsCvBouLy9vQrO32H2gJbl4=;
	b=SryLsEh1e9TJ61SOShWMnCr7wxtOmuqz+GmvQ/4dwwJOBt52nktIHOSU8AOWYs0JshNy
	 WGTyEN/NxCedhtrmq55IDIioinpiyHjQnB2sMEWg3g3eTZ+vbH3/24Byjtlf4xOhz3M+n
	 7uuexvxjJ0o/Vs1sGYme4HREeOxcW6lXkPAvewRvx++rAJb+rPjLc7bgPx0600cWROwzy
	 HjV6GBrWzOgtp0zWHZkCtpiTei3HF3PhUZ9wE+6XZy7oN8v4ObhFomdpQJMuUAOBa2CPE
	 QX19OPkd1EMCKWLM72y/ry52NKC7hkZt1NmxoD8QPmWKAtHyub/zF44DyPhQZrARLVw==
ARC-Authentication-Results: i=1; smtp.subspace.kernel.org; 
	dkim=pass header.d=linuxfoundation.org header.i=@linuxfoundation.org header.a=rsa-sha256 header.s=korg header.b=jeqcWmZn;
	arc=none smtp.remote-ip=100.103.45.18
Received: from smtp.kernel.org (quasi.space.kernel.org [100.103.45.18])
	(using TLSv1.3 with cipher TLS_AES_256_GCM_SHA384 (256/256 bits)
	 key-exchange X25519 server-signature ECDSA (prime256v1))
	(No client certificate requested)
	by smtp.subspace.kernel.org (Postfix) with ESMTPS id 905B1606A335
	for <linux-cve-announce@vger.kernel.org>; Thu, 19 Nov 2026 14:37:34 +0000 (UTC)
Authentication-Results: smtp.subspace.kernel.org;
	dkim=pass (1024-bit key) header.d=linuxfoundation.org header.i=@linuxfoundation.org header.a=rsa-sha256 header.s=korg header.b=jeqcWmZn
Received: by smtp.kernel.org (Postfix) with ESMTPSA id A5CBA1F000C8;
	Thu, 19 Nov 2026 14:37:33 +0000 (UTC)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=linuxfoundation.org;
	s=korg; t=1795099054;
	bh=cBbuSXkHtO9lavvvNsCUJsCvBouLy9vQrO32H2gJbl4=;
	h=From:To:Cc:Subject:Date:Reply-To;
	b=jeqcWmZnZUHtBJq2HC+rGImga9QpuUoHQFqJ3u0Jb3SR7xP5LhJsM9BszCbIeXGAB
	 mqrIvRrGo0j3IPatOR93M+EpYQu4GJBSQqooBY/yiaR7LRgAckn7fhuTDb9dG+Jntw
	 Z1H+9TUbrWW8tP5x5x9imTSeTGQYw45HZzCWc6o4=
From: Greg Kroah-Hartman <gregkh@linuxfoundation.org>
To: linux-cve-announce@vger.kernel.org
Cc: Greg Kroah-Hartman <gregkh@kernel.org>
Subject: CVE-2026-99362: nfsd: preflight SEQUENCE replies before accepting a slot
Date: Thu, 19 Nov 2026 15:24:20 +0100
Message-ID: <2026111950-CVE-2026-99362-c6f2@gregkh>
X-Mailer: git-send-email 2.56.0
Reply-To: <cve@kernel.org>, <linux-kernel@vger.kernel.org>
X-Mailing-List: linux-cve-announce@vger.kernel.org
List-Id: <linux-cve-announce.vger.kernel.org>
List-Post: <mailto:linux-cve-announce@vger.kernel.org>
List-Help: <mailto:linux-cve-announce+help@vger.kernel.org>
List-Subscribe: <mailto:linux-cve-announce+subscribe@vger.kernel.org>
List-Unsubscribe: <mailto:linux-cve-announce+unsubscribe@vger.kernel.org>
List-Owner: <mailto:linux-cve-announce+owner@vger.kernel.org>
Precedence: list
MIME-Version: 1.0
X-Developer-Signature: v=1; a=openpgp-sha256; l=3808; i=gregkh@linuxfoundation.org; h=from:subject:message-id; bh=DANAWNTCH570Ec0AAXF1T285HZ2pMKLZPndEKBvXypY=; b=owGbwMvMwCRo6H6F97bub03G02pJDFn/2cpCJ73kn/PNOd5hleq8JXFhGw9d4PygzXB41d1Jr 507qu+rd8SwMAgyMciKKbJ82cZzdH/FIUUvQ9vTMHNYmUCGMHBxCsBEVFYwTA9s+Hjl4ee51qHT 6tV8Y8Tqsta4Miy4usB5gWi0n8GU2ZoZeyLal03ckPwTAA==
X-Developer-Key: i=gregkh@linuxfoundation.org; a=openpgp; fpr=F4B60CC5BF78C2214A313DCB3147D40DDB2DFB29
Content-Transfer-Encoding: 8bit

From: Greg Kroah-Hartman <gregkh@kernel.org>

Description
===========

In the Linux kernel, the following vulnerability has been resolved:

nfsd: preflight SEQUENCE replies before accepting a slot

nfsd4_sequence() narrows the reply buffer to the session's cached
reply limit before it accepts the slot seqid. A client may negotiate
ca_maxresponsesize_cached down to NFSD_MIN_HDR_SEQ_SZ, and
nfsd4_alloc_slot() then gives every slot a zero-length sl_data[]. A
COMPOUND tag can fill that narrowed buffer until it holds the
SEQUENCE opcode but not the status word that follows.
nfsd4_encode_operation() returns without running
nfsd4_encode_sequence(), so cstate.data_offset stays zero. It leaves
op->status at nfs_ok as well, so the COMPOUND is treated as having
succeeded.

nfsd4_store_cache_entry() declines to cache a lone SEQUENCE that
returned an error. That test reads the status the operation
reported, so it passes here. The copy starts at offset zero and
takes the whole reply, RPC and COMPOUND headers included, into the
zero-length sl_data[]. The COMPOUND tag is copied along with it, so
the client picks most of the bytes written past the end of the slot:

  BUG: KASAN: slab-out-of-bounds in read_bytes_from_xdr_buf+0x1bc/0x390
  Write of size 80 at addr ffff888003a549cd by task kunit_try_catch/24
   __asan_memcpy+0x38/0x60
   read_bytes_from_xdr_buf+0x1bc/0x390
   nfsd4_sequence_done+0x5b0/0x810
   nfs4svc_encode_compoundres+0x1bf/0x240

Check that the fixed-size SEQUENCE result, plus room for a following
operation's error status, fits the negotiated limit before narrowing
the buffer and consuming the slot seqid. The slot and its reply
cache are left unchanged, as RFC 8881 Section 2.10.6.1.2 requires of
an error returned from SEQUENCE.

The Linux kernel CVE team has assigned CVE-2026-99362 to this issue.

Affected and fixed versions
===========================

	Issue introduced in 3.16 with commit 47ee52986472dba068e8223cbaf1b65d74238781 and fixed in 6.12.117 with commit 1a5a227bca6a8a9f9d31230697aeb84c62a21da6
	Issue introduced in 3.16 with commit 47ee52986472dba068e8223cbaf1b65d74238781 and fixed in 6.18.61 with commit 37fc2ec211630360e9aefcaaec8730db964645f2
	Issue introduced in 3.16 with commit 47ee52986472dba068e8223cbaf1b65d74238781 and fixed in 7.3.2 with commit ed98b0c57e5e84290c5b35428144ab26778905f3
	Issue introduced in 3.16 with commit 47ee52986472dba068e8223cbaf1b65d74238781 and fixed in 7.4-rc1 with commit 35ff1a7a7e3835c3e974bc5c45d335897564ceae

Please see https://www.kernel.org for a full list of currently supported
kernel versions by the kernel community.

Unaffected versions might change over time as fixes are backported to
older supported kernel versions.  The official CVE entry at
	https://cve.org/CVERecord/?id=CVE-2026-99362
will be updated if fixes are backported, please check that for the most
up to date information about this issue.

Affected files
==============

The file(s) affected by this issue are:
	fs/nfsd/nfs4state.c

Mitigation
==========

The Linux kernel CVE team recommends that you update to the latest
stable kernel version for this, and many other bugfixes.  Individual
changes are never tested alone, but rather are part of a larger kernel
release.  Cherry-picking individual commits is not recommended or
supported by the Linux kernel community at all.  If however, updating to
the latest release is impossible, the individual changes to resolve this
issue can be found at these commits:
	https://git.kernel.org/stable/c/1a5a227bca6a8a9f9d31230697aeb84c62a21da6
	https://git.kernel.org/stable/c/37fc2ec211630360e9aefcaaec8730db964645f2
	https://git.kernel.org/stable/c/ed98b0c57e5e84290c5b35428144ab26778905f3
	https://git.kernel.org/stable/c/35ff1a7a7e3835c3e974bc5c45d335897564ceae

Links/Buttons:
This page does not seem to contain any buttons/links.
