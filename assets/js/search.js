/* search.js — minimal weighted token-prefix search across the unified index.

   Scoring favors:
       - exact id matches (CVE-2026-31431 etc.)
       - title matches over hint matches
       - prefix matches over substring matches
   Multi-token queries AND-combine token matches. Empty query returns top-N
   most-recent briefs.
*/

(function () {
  'use strict';

  /** Normalize text for indexing/matching. Lowercase + collapse separators. */
  function norm(s) {
    return (s || '').toLowerCase().replace(/[ \s]+/g, ' ').trim();
  }

  /** Split a query into tokens. CVE ids stay intact; everything else splits on whitespace + punctuation. */
  function tokens(q) {
    const out = [];
    const cveRe = /cve-\d{4}-\d{4,7}/gi;
    let s = q;
    let m;
    while ((m = cveRe.exec(q)) !== null) {
      out.push(m[0].toLowerCase());
    }
    s = q.replace(cveRe, ' ').toLowerCase();
    s.split(/[^a-z0-9]+/).forEach((t) => {
      if (t && t.length >= 2) out.push(t);
    });
    return out;
  }

  /** Score a single entry against a token. Returns 0 when no match. */
  function scoreEntry(entry, token) {
    const titleN = norm(entry.title);
    const hintN  = norm(entry.hint);
    const idN    = norm(entry.id);
    let score = 0;

    if (idN === token)            score += 100;
    else if (idN.startsWith(token)) score += 60;
    else if (idN.includes(token))   score += 25;

    if (titleN === token)             score += 80;
    else if (titleN.startsWith(token)) score += 40;
    else {
      // Word-prefix match within title
      const words = titleN.split(' ');
      if (words.some((w) => w.startsWith(token))) score += 20;
      else if (titleN.includes(token)) score += 10;
    }

    if (hintN.includes(token)) score += 4;

    if (Array.isArray(entry.tags)) {
      for (const t of entry.tags) {
        if (norm(t) === token) { score += 12; break; }
        if (norm(t).startsWith(token)) { score += 6; break; }
      }
    }

    return score;
  }

  /** Run a query against an index. */
  function query(index, q, opts) {
    opts = opts || {};
    const limit = opts.limit || 50;
    const kindBoost = opts.kindBoost || {};
    const toks = tokens(q || '');

    if (!toks.length) return [];

    const out = [];
    for (const entry of index) {
      let total = 0;
      let allMatched = true;
      for (const t of toks) {
        const s = scoreEntry(entry, t);
        if (!s) { allMatched = false; break; }
        total += s;
      }
      if (allMatched) {
        total += (kindBoost[entry.kind] || 0);
        out.push({ entry, score: total });
      }
    }

    out.sort((a, b) => b.score - a.score || a.entry.title.localeCompare(b.entry.title));
    return out.slice(0, limit).map((r) => r.entry);
  }

  /** Highlight all token occurrences in text with <mark> tags. Plain-text in, HTML out. */
  function highlight(text, q) {
    if (!q) return escapeHtml(text);
    const toks = tokens(q).filter((t) => t.length >= 2);
    if (!toks.length) return escapeHtml(text);
    let html = escapeHtml(text);
    // Sort longest first so substrings don't pre-empt the longer match.
    toks.sort((a, b) => b.length - a.length);
    for (const t of toks) {
      const re = new RegExp('(' + escapeRegex(t) + ')', 'gi');
      html = html.replace(re, '<mark>$1</mark>');
    }
    return html;
  }

  function escapeHtml(s) {
    return String(s)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#39;');
  }
  function escapeRegex(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

  window.Search = { query, highlight, escapeHtml, tokens };
})();
