Title: 

URL Source: https://lore.kernel.org/linux-nfs/20260817-jean-v1-1-9e356596ab85@kernel.org/raw

Markdown Content:
From mboxrd@z Thu Jan  1 00:00:00 1970
Received: from smtp.kernel.org (aws-us-west-2-korg-mail-alma10-1.taild15c8.ts.net [100.103.45.18])
	(using TLSv1.2 with cipher ECDHE-RSA-AES256-GCM-SHA384 (256/256 bits))
	(No client certificate requested)
	by smtp.subspace.kernel.org (Postfix) with ESMTPS id B5B34285CB9
	for <linux-nfs@vger.kernel.org>; Tue, 18 Aug 2026 00:57:24 +0000 (UTC)
Authentication-Results: smtp.subspace.kernel.org; arc=none smtp.client-ip=100.103.45.18
ARC-Seal:i=1; a=rsa-sha256; d=subspace.kernel.org; s=arc-20240116;
	t=1787014645; cv=none; b=nJ5yx9t8LX46HAY6566ahq3WTD06eAfzOt5Px+LTchpesYERYwh6x8X3T8ogNvq7CzAODuzjSju4JO0Eqcce7EmEwsAiXO8/jLEHMa9E2pJXfhKFGP2JyCL30MX4muaTK+UCGl4YxN2Lrt9TfZig6z/dLaaQj7SsIMAT66t0tbw=
ARC-Message-Signature:i=1; a=rsa-sha256; d=subspace.kernel.org;
	s=arc-20240116; t=1787014645; c=relaxed/simple;
	bh=YX7IDYQSEuNMNGaMVWuZ4dlaHcjM6ysSx6z8k0krXEo=;
	h=From:Date:Subject:MIME-Version:Content-Type:Message-Id:References:
	 In-Reply-To:To:Cc; b=VOQfoYl4mIGYx6PI907nznKTF4V5rlx2oEkl/1EXaHtbT3pt4x7sWiWQro3ucjJF46brmzfAs6z2JuBrgVY4kZOf3nss7DDzNcHOH2OtiLzTXQ5xBYnayMAX2ftqfiV9nED9XPYCZKb/E0ktxFaOetnEY9AJo5WaTbIarscYj7w=
ARC-Authentication-Results:i=1; smtp.subspace.kernel.org; dkim=pass (2048-bit key) header.d=kernel.org header.i=@kernel.org header.b=cfnEY2aN; arc=none smtp.client-ip=100.103.45.18
Authentication-Results: smtp.subspace.kernel.org;
	dkim=pass (2048-bit key) header.d=kernel.org header.i=@kernel.org header.b="cfnEY2aN"
Received: by smtp.kernel.org (Postfix) with ESMTPSA id 0426E1F00A3E;
	Tue, 18 Aug 2026 00:57:23 +0000 (UTC)
DKIM-Signature: v=1; a=rsa-sha256; c=relaxed/relaxed; d=kernel.org;
	s=k20260515; t=1787014644;
	bh=WLxbEmZFy5hmKAFs+8aqxc7E7GtgtScKuaFXqeUcOFs=;
	h=From:Date:Subject:References:In-Reply-To:To:Cc;
	b=cfnEY2aNgFxGBFPss+2Lwc28P3BLyEslK0DDZrBEyThbQ/yhVbdER8/+/y18+9xY5
	 qL1+WsmOfd+1R5AXY8yFQi13/SHA2TdjNLE7yDI9DY+WOaO7WmuuPSYlrZ9x5HMlCC
	 Ueu/upvThxxmH+tTfY1sQjnd9g/vkYuHRz40VXFDeOWTyoTIwBrHZ9Yh3e6uDMc1Ws
	 FBbuu75+lWBgag8xxISF/e+6OWD9fLGM/NE3batEK/SopsAlGt+FeYeb+JzzLuSen5
	 Pc2uT3sx9rpbQyli5X3kc4gvIYTHJzNKQnFvW6/qVdIXVAzXzN0Mbcqk2C6+wJY3QQ
	 GJBBcqeIZlHKg==
From: Chuck Lever <cel@kernel.org>
Date: Mon, 17 Aug 2026 20:57:14 -0400
Subject: [PATCH 1/2] nfsd: preflight SEQUENCE replies before accepting a
 slot
Precedence: bulk
X-Mailing-List: linux-nfs@vger.kernel.org
List-Id: <linux-nfs.vger.kernel.org>
List-Subscribe: <mailto:linux-nfs+subscribe@vger.kernel.org>
List-Unsubscribe: <mailto:linux-nfs+unsubscribe@vger.kernel.org>
MIME-Version: 1.0
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: 8bit
Message-Id: <20260817-jean-v1-1-9e356596ab85@kernel.org>
References: <20260817-jean-v1-0-9e356596ab85@kernel.org>
In-Reply-To: <20260817-jean-v1-0-9e356596ab85@kernel.org>
To: Jeff Layton <jlayton@kernel.org>, NeilBrown <neil@brown.name>, 
 Olga Kornievskaia <okorniev@redhat.com>, Dai Ngo <Dai.Ngo@oracle.com>, 
 Tom Talpey <tom@talpey.com>
Cc: linux-nfs@vger.kernel.org, 
 =?utf-8?q?J=C3=A9r=C3=A9my_Jean?= <Jeremy.Jean@oss.cyber.gouv.fr>, 
 Chuck Lever <cel@kernel.org>
X-Mailer: b4 0.16-dev
X-Developer-Signature: v=1; a=openpgp-sha256; l=3569; i=cel@kernel.org;
 h=from:subject:message-id; bh=Rt8dKfj1pAxjDp2+nDPNhS+eUDPJIvhkGFUr6YM6b7s=;
 b=owEBbQKS/ZANAwAKATNqszNvZn+XAcsmYgBqg63yDvicQ5KXYMbcj9zwSYZWqeVXfZeZCIBoG
 fMFRGFT5LKJAjMEAAEKAB0WIQQosuWwEobfJDzyPv4zarMzb2Z/lwUCaoOt8gAKCRAzarMzb2Z/
 l97dEACwKLfMlZqXEKZ5GGcI9EzbeaILydzaF4VNlLNQhLe0KJLzdg1+zOR67TePMAi8uo3yPoU
 O6X4SJ0bK5w5XO872h4G/Nlvj+xOPVtqQl2bP95AGUBJOLvOmsjIsSJ+XlhjS47pVe2YTPkWqPc
 ufc7o50TeahVRx6IhZCe5ic8Q50jyilZquUBi+IMP6a88cITDaR1S85Thl9bm0dIAP2K8MGt34T
 l23GiDoD78ijfgMIdZKuIZUeHafVmeK00sN3F/yGXID2XRsBSWZ/7NYtxpYFVG1Kslqd0SlCOH1
 A5MWP6YHkrNnDwGCaSrUiyqZV5IABQ7CEgTbOe+/ZPQIFw6bPonNkvA8RWi/daRcsLxBAh2AViQ
 nsr/4oYQTLVYa6ooqHurHd8KEIVFIoMpDQcrtXZAAUOrnNZOzRESjiM8Tq9K8Zi3P0WPwHKen18
 pZdfXRetsRHFOrbkgQzPXsZgsirMp0Nn0+Y5rmo5ViUiYJDArkWpU2p3uRyFwqM3g+LMNrBor1B
 9TtHIYl1hQbQlNBaiFuJzdcvqiIh6VFrwJ03pJF/cZvTkdT82393dGv5E0v7ioqTHgc/A4V7TUd
 10po4aoENopNFrVI6f/NvtI0s61J263K9OOSbj9y6iURSiAx4LqYtIebB575BcmmIARpbB6CYMu
 Vn46aqGbapf07hw==
X-Developer-Key: i=cel@kernel.org; a=openpgp;
 fpr=28B2E5B01286DF243CF23EFE336AB3336F667F97

From: Jérémy Jean <Jeremy.Jean@oss.cyber.gouv.fr>

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

Fixes: 47ee52986472 ("nfsd4: adjust buflen to session channel limit")
Assisted-by: Codex:gpt-5
Signed-off-by: Jérémy Jean <Jeremy.Jean@oss.cyber.gouv.fr>
Signed-off-by: Chuck Lever <cel@kernel.org>
---
 fs/nfsd/nfs4state.c | 19 ++++++++++++++++++-
 1 file changed, 18 insertions(+), 1 deletion(-)

diff --git a/fs/nfsd/nfs4state.c b/fs/nfsd/nfs4state.c
index 1ba97e3f65eb..3fc5bed85bab 100644
--- a/fs/nfsd/nfs4state.c
+++ b/fs/nfsd/nfs4state.c
@@ -5044,6 +5044,7 @@ __be32
 nfsd4_sequence(struct svc_rqst *rqstp, struct nfsd4_compound_state *cstate,
 		union nfsd4_op_u *u)
 {
+	struct nfsd4_compoundargs *args = rqstp->rq_argp;
 	struct nfsd4_sequence *seq = &u->sequence;
 	struct nfsd4_compoundres *resp = rqstp->rq_resp;
 	struct xdr_stream *xdr = resp->xdr;
@@ -5053,6 +5054,7 @@ nfsd4_sequence(struct svc_rqst *rqstp, struct nfsd4_compound_state *cstate,
 	struct nfsd4_conn *conn;
 	__be32 status;
 	int buflen;
+	u32 maxlen, respsize;
 	struct net *net = SVC_NET(rqstp);
 	struct nfsd_net *nn = net_generic(net, nfsd_net_id);
 
@@ -5130,7 +5132,22 @@ nfsd4_sequence(struct svc_rqst *rqstp, struct nfsd4_compound_state *cstate,
 			session->se_fchannel.maxresp_sz;
 	status = (seq->cachethis) ? nfserr_rep_too_big_to_cache :
 				    nfserr_rep_too_big;
-	if (xdr_restrict_buflen(xdr, buflen - rqstp->rq_auth_slack))
+	if (buflen < rqstp->rq_auth_slack)
+		goto out_put_session;
+	maxlen = buflen - rqstp->rq_auth_slack;
+
+	/*
+	 * A SEQUENCE result too large for maxlen never reaches
+	 * nfsd4_encode_sequence(), so cstate.data_offset stays zero and
+	 * the reply cache overruns the slot.
+	 */
+	respsize = nfsd4_max_reply(rqstp, &args->ops[0]);
+	if (!nfsd4_last_compound_op(rqstp))
+		respsize += COMPOUND_ERR_SLACK_SPACE;
+	if (xdr->buf->len + respsize > maxlen)
+		goto out_put_session;
+
+	if (xdr_restrict_buflen(xdr, maxlen))
 		goto out_put_session;
 	svc_reserve_auth(rqstp, buflen);
 

-- 
2.54.0

Links/Buttons:
This page does not seem to contain any buttons/links.
