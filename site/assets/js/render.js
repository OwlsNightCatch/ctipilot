/* render.js — view templates for each route.

   Each render fn returns an HTML string. The router puts the result into
   #view. Markdown rendering goes through marked.js + DOMPurify (vendored),
   with a Trusted Types policy wrapping the assignment so the strict CSP
   require-trusted-types-for 'script' directive is satisfied.

   No template engine: small surface, easy to audit. Inline strings come
   either from JSON Store data (sanitised at parse) or the brief markdown
   (sanitised through marked + DOMPurify); plain string interpolation
   passes through esc()/Search.escapeHtml().
*/

(function () {
  'use strict';

  /** Identity wrapper kept for callers — Trusted Types enforcement was
      removed when Umami was added to the page (Umami doesn't declare a
      TT policy and is rejected by `require-trusted-types-for 'script'`).
      DOMPurify still sanitises every markdown body before assignment. */
  function trustHtml(html) {
    return html;
  }

  /* ── markdown configuration ─────────────────────────────────── */

  function configureMarked() {
    if (!window.marked) return;
    const renderer = new marked.Renderer();
    // Heading anchors so we can target sections from a TOC.
    renderer.heading = function (text, level, raw) {
      const slug = String(raw)
        .toLowerCase()
        .replace(/[^a-z0-9]+/g, '-')
        .replace(/(^-+|-+$)/g, '');
      return `<h${level} id="${slug}">${text}</h${level}>`;
    };
    marked.use({ renderer, gfm: true, breaks: false });
  }

  /* DOMPurify hook: any external <a href="https?://..."> gets target="_blank"
     and rel="noopener noreferrer". */
  function attachExternalLinkHook() {
    if (!window.DOMPurify || attachExternalLinkHook._done) return;
    DOMPurify.addHook('afterSanitizeAttributes', (node) => {
      if (node.tagName !== 'A') return;
      const href = node.getAttribute('href') || '';
      if (/^https?:\/\//i.test(href)) {
        node.setAttribute('target', '_blank');
        node.setAttribute('rel', 'noopener noreferrer');
      }
    });
    attachExternalLinkHook._done = true;
  }

  /* Defence in depth — see notes in the previous version of this file
     for the rationale of every flag. */
  const PURIFY_CFG = {
    USE_PROFILES: { html: true },
    ADD_ATTR: ['target', 'rel'],
    FORBID_TAGS: [
      'style', 'iframe', 'form', 'meta', 'link', 'embed', 'object', 'base',
      'svg', 'math', 'noscript', 'noembed', 'noframes', 'plaintext', 'xmp',
      'frame', 'frameset', 'applet', 'audio', 'video', 'source', 'track',
      'portal', 'annotation-xml',
    ],
    FORBID_ATTR: [
      'srcdoc', 'srcset', 'formaction', 'xlink:href', 'autofocus',
      'background', 'ping', 'http-equiv', 'manifest',
    ],
    ALLOW_DATA_ATTR: false,
    ALLOW_UNKNOWN_PROTOCOLS: false,
    ALLOWED_URI_REGEXP: /^(?:(?:https?|mailto|tel):|#|\/)/i,
  };

  const XSS_VECTORS = Object.freeze([
    '<script>alert(1)</script>',
    '<img src=x onerror=alert(1)>',
    '[link](javascript:alert(1))',
    '[link](data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTwvc2NyaXB0Pg==)',
    '[link](vbscript:msgbox(1))',
    '<iframe src="javascript:alert(1)"></iframe>',
    '<a href="" onmouseover="alert(1)">x</a>',
    '<svg onload=alert(1)>',
    '<svg><script>alert(1)</script></svg>',
    '<math href="javascript:alert(1)">x</math>',
    '<details ontoggle=alert(1) open>x</details>',
    '<form action="javascript:alert(1)"><input type=submit></form>',
    '<base href="https://evil.example/">',
    '<style>body{background:url(javascript:alert(1))}</style>',
    '<META http-equiv="refresh" content="0;url=javascript:alert(1)">',
    '<link rel=import href="https://evil.example/x.html">',
    '<object data="javascript:alert(1)"></object>',
    '<embed src="javascript:alert(1)">',
    '<scr<script>ipt>alert(1)</script>',
    '<a href="javascript&#58;alert(1)">x</a>',
    '<a href="java\nscript:alert(1)">x</a>',
    '<a href="JaVaScRiPt:alert(1)">x</a>',
    '<img src=`x` onerror=alert(1)>',
    '<body onload=alert(1)>',
    '<input autofocus onfocus=alert(1)>',
    '"><script>alert(1)</script>',
    '<a href="#" onclick="alert(1)">x</a>',
    '<a href="https://example.com/" target="_blank" onmouseenter="alert(1)">x</a>',
  ]);

  const FORBIDDEN_TAGS_LOWER = new Set([
    'script','iframe','form','meta','link','embed','object','base','svg','math',
    'style','noscript','noembed','noframes','plaintext','xmp','frame','frameset',
    'applet','portal','annotation-xml','body','html','head','title',
  ]);
  const DANGEROUS_URI = /^\s*(?:javascript|data|vbscript|file):/i;

  /** Walks the sanitiser output as a DocumentFragment, looking for any
      forbidden tag, event-handler attribute, dangerous URI scheme, or
      inline style. Returns null when clean.

      Uses DOMPurify.sanitize a second time with RETURN_DOM_FRAGMENT to
      get a DocumentFragment without ever assigning a string to
      innerHTML — necessary under our strict
      `require-trusted-types-for 'script'` CSP, where DOMParser and
      innerHTML otherwise refuse plain strings. */
  function findDangerInHtml(html) {
    let frag;
    try {
      // Apply the same restrictive PURIFY_CFG used at runtime, plus
      // RETURN_DOM_FRAGMENT so we walk the actual node tree without
      // assigning any string to innerHTML (which the strict CSP forbids).
      frag = window.DOMPurify.sanitize(html, Object.assign({}, PURIFY_CFG, { RETURN_DOM_FRAGMENT: true }));
    } catch (_) {
      return 'sanitiser RETURN_DOM_FRAGMENT failed';
    }
    if (!frag) return null;
    for (const el of frag.querySelectorAll('*')) {
      const tag = (el.tagName || '').toLowerCase();
      if (FORBIDDEN_TAGS_LOWER.has(tag)) return `forbidden tag rendered: <${tag}>`;
      for (const a of Array.from(el.attributes || [])) {
        if (/^on/i.test(a.name)) return `event handler attr: ${a.name}`;
        if ((a.name === 'href' || a.name === 'src' || a.name === 'action'
             || a.name === 'formaction' || a.name === 'data') && DANGEROUS_URI.test(a.value)) {
          return `dangerous URI in ${a.name}: ${a.value.slice(0, 80)}`;
        }
        if (a.name === 'style') return `inline style attr present`;
      }
    }
    return null;
  }

  let _renderUnsafe = false;
  function renderUnsafeReason() { return _renderUnsafe; }

  function selfTest() {
    if (!window.marked || !window.DOMPurify) return null;
    if (!configureMarked._done) { configureMarked(); configureMarked._done = true; }
    attachExternalLinkHook();
    for (const vec of XSS_VECTORS) {
      let html;
      try {
        html = String(marked.parse(vec || ''));
      } catch (e) {
        return `marked threw on vector ${JSON.stringify(vec)}: ${e.message}`;
      }
      const reason = findDangerInHtml(html);
      if (reason) {
        return `vector ${JSON.stringify(vec)} survived: ${reason}`;
      }
    }
    return null;
  }

  function ensureSafe() {
    if (ensureSafe._ran) return !_renderUnsafe;
    ensureSafe._ran = true;
    const failure = selfTest();
    if (failure) {
      _renderUnsafe = failure;
      console.error('[CTI Briefs] markdown sanitiser self-test FAILED — falling back to plain text. Detail:', failure);
    }
    return !_renderUnsafe;
  }

  function md(markdown) {
    if (!window.marked || !window.DOMPurify) return esc(markdown);
    if (!configureMarked._done) { configureMarked(); configureMarked._done = true; }
    attachExternalLinkHook();
    if (!ensureSafe()) {
      return `<pre class="muted" style="white-space:pre-wrap">${esc(markdown)}</pre>`;
    }
    const html = window.marked.parse(markdown || '');
    return String(window.DOMPurify.sanitize(html, PURIFY_CFG));
  }

  function esc(s) {
    return String(s == null ? '' : s)
      .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;').replaceAll("'", '&#39;');
  }

  function attr(s) { return esc(s); }

  function fmtDate(d) {
    if (!d) return '';
    if (/^\d{4}-W\d{2}$/.test(d)) return 'Week ' + d.slice(5);
    if (/^\d{4}-\d{2}-\d{2}$/.test(d)) return d;
    return d;
  }

  function reliabilityBadge(r) {
    const cls = r === 'HIGH' ? 'badge--high' : r === 'MEDIUM' ? 'badge--med' : 'badge--low';
    return `<span class="badge ${cls}">${esc(r)}</span>`;
  }

  function statusBadge(s) {
    if (s === 'active') return `<span class="badge badge--high">active</span>`;
    if (s === 'candidate') return `<span class="badge badge--med">candidate</span>`;
    if (s === 'demoted') return `<span class="badge badge--low">demoted</span>`;
    return `<span class="badge">${esc(s)}</span>`;
  }

  /** Build a CISA KEV catalog URL filtered to one CVE. The plain
      `/known-exploited-vulnerabilities-catalog` URL lands on the full
      catalog with no filter; passing the search params drops the user
      directly on the matching row. If the CVE is not in KEV, the page
      simply shows "no results" — still a useful confirmation. */
  function cisaKevSearchUrl(cveId) {
    const id = encodeURIComponent(String(cveId || ''));
    return (
      'https://www.cisa.gov/known-exploited-vulnerabilities-catalog' +
      '?search=' + id +
      '&field_date_added_wrapper=all' +
      '&field_cve=' +
      '&sort_by=field_date_added' +
      '&items_per_page=20' +
      '&url='
    );
  }

  function timelineStrip(briefs, current) {
    if (!briefs || !briefs.length) return '';
    return `<div class="timeline-strip" aria-label="Brief appearances">
      ${briefs.map((n) => `<a href="#/briefs/${esc(n)}" class="${n === current ? 'current' : ''}" title="Brief ${esc(n)}">${esc(n)}</a>`).join('')}
    </div>`;
  }

  /* ── home (preview of latest brief) ───────────────────────────── */

  async function renderHome() {
    const latestDaily = Store.manifest.find((b) => b.kind === 'daily');
    if (!latestDaily) {
      return `<div class="empty">
        <h1>No briefs yet</h1>
        <p>The first daily routine run will publish a brief here.</p>
        <p><a href="#/about">About this newsletter →</a></p>
      </div>`;
    }
    const latestWeekly = Store.manifest.find((b) => b.kind === 'weekly');
    const isToday = latestDaily.name === todayISO();
    const banner = renderHomeBanner(latestDaily, latestWeekly, isToday);
    const preview = renderTldrPreview(latestDaily);
    const footer = renderHomeFooter();
    return `${banner}${preview}${footer}`;
  }

  function renderHomeBanner(brief, latestWeekly, isToday) {
    return `
      <div class="home-banner">
        <div class="home-banner-left">
          <div class="home-banner-eyebrow">${isToday ? "Today's brief" : 'Latest brief'} · <span class="mono">${esc(brief.name)}</span></div>
          <h1>${esc(brief.title)}</h1>
        </div>
        <div class="home-banner-right">
          <a class="cta" href="#/briefs/${esc(brief.name)}">Read the full brief →</a>
          ${latestWeekly
            ? `<a class="cta cta--secondary" href="#/briefs/weekly/${esc(latestWeekly.name)}" title="${esc(latestWeekly.title)}">Weekly · ${esc(latestWeekly.name)}</a>`
            : ''}
        </div>
      </div>`;
  }

  function renderTldrPreview(brief) {
    const items = (brief.tldr || []).slice(0, 5);
    const body = items.length
      ? `<ul>${items.map((line) => `<li>${md(line).replace(/^<p>|<\/p>$/g, '')}</li>`).join('')}</ul>`
      : `<p class="muted">No TL;DR bullets in this brief.</p>`;
    return `
      <section class="preview-tldr">
        <h2>TL;DR — ${esc(brief.name)}</h2>
        ${body}
        <div class="preview-tldr-cta">
          <a class="cta" href="#/briefs/${esc(brief.name)}">Read the full brief →</a>
          <a class="cta cta--secondary" href="#/briefs">All briefs</a>
        </div>
      </section>
    `;
  }

  function renderHomeFooter() {
    const counts = Store.site && Store.site.counts ? Store.site.counts : {};
    return `
      <section class="home-footer">
        <h2 class="section-head" style="margin-top:1.5rem">Continue exploring</h2>
        <div class="stat-grid" style="margin-bottom: 1rem">
          <div class="stat"><div class="v">${esc(counts.briefs || 0)}</div><div class="l"><a href="#/briefs">All briefs</a></div></div>
          <div class="stat"><div class="v">${esc(counts.cves || 0)}</div><div class="l"><a href="#/cves">CVEs tracked</a></div></div>
          <div class="stat"><div class="v">${esc(counts.topics || 0)}</div><div class="l"><a href="#/topics">Topics</a></div></div>
          <div class="stat"><div class="v">${esc(counts.sources || 0)}</div><div class="l"><a href="#/sources">Sources</a></div></div>
        </div>
        <p class="muted" style="font-size:0.78rem; margin-top: 1rem; font-family: var(--mono)">build · ${esc((Store.site && Store.site.built_at) || '—')}</p>
      </section>
    `;
  }

  function todayISO() {
    const d = new Date();
    const yr = d.getUTCFullYear();
    const mo = String(d.getUTCMonth() + 1).padStart(2, '0');
    const da = String(d.getUTCDate()).padStart(2, '0');
    return `${yr}-${mo}-${da}`;
  }

  /** Shared body renderer used by the brief detail view. */
  async function renderBriefBody(brief) {
    let raw;
    try { raw = await Store.getMarkdown(brief.path); }
    catch (e) { return `<p class="muted">Failed to load <code>${esc(brief.path)}</code>: ${esc(e.message)}</p>`; }

    const body = raw.replace(/^# .+\n+/, '');
    const cves = Store.cvesInBrief(brief.name);
    const topics = Store.topicsInBrief(brief.name);
    const cited = Store.sourcesInBrief(brief.name);

    // TOC — sections only by default, plus collapsible References sub-sections.
    const sectionsToc = (brief.sections || [])
      .map((s) => `<li><a href="#${esc(s.anchor)}">${esc(s.heading)}</a></li>`)
      .join('');

    const refsBlock = (cves.length || topics.length || cited.length)
      ? `<details>
          <summary>References (${cves.length + topics.length + Math.min(cited.length, 30)})</summary>
          <ul>
            ${cves.map((c) => `<li><a href="#/cves/${esc(c.id)}" class="mono">${esc(c.id)}</a>${c.appearances.length > 1 ? ` <span class="badge badge--accent" title="Appears in ${c.appearances.length} briefs">×${c.appearances.length}</span>` : ''}</li>`).join('')}
            ${topics.map((t) => `<li><a href="#/topics/${encodeURIComponent(t.key)}">${esc(t.title)}</a></li>`).join('')}
            ${cited.slice(0, 30).map((s) => `<li><a href="#/sources/${encodeURIComponent(s.id)}">${esc(s.publisher)}</a></li>`).join('')}
            ${cited.length > 30 ? `<li class="muted">+ ${cited.length - 30} more sources</li>` : ''}
          </ul>
        </details>`
      : '';

    const tocHtml = `
      <h3>On this page</h3>
      <ul class="toc-sections">${sectionsToc || '<li class="muted">—</li>'}</ul>
      ${refsBlock}
    `;

    // Cited footer — sits below the brief body, replaces the old in-sidebar lists.
    const citedFooter = (cves.length || topics.length || cited.length) ? `
      <footer class="brief-cited">
        ${cves.length ? `<section>
          <h3>CVEs in this brief (${cves.length})</h3>
          <ul>${cves.map((c) => `<li><a href="#/cves/${esc(c.id)}" class="mono">${esc(c.id)}</a>${c.appearances.length > 1 ? ` <span class="badge badge--accent" title="Appears in ${c.appearances.length} briefs">×${c.appearances.length}</span>` : ''}</li>`).join('')}</ul>
        </section>` : ''}
        ${topics.length ? `<section>
          <h3>Tracked topics (${topics.length})</h3>
          <ul>${topics.map((t) => `<li><a href="#/topics/${encodeURIComponent(t.key)}">${esc(t.title)}</a>${(t.briefs || []).length > 1 ? ` <span class="badge badge--accent" title="Appears in ${t.briefs.length} briefs">×${t.briefs.length}</span>` : ''}</li>`).join('')}</ul>
        </section>` : ''}
        ${cited.length ? `<section>
          <h3>Sources cited (${cited.length})</h3>
          <ul>${cited.slice(0, 60).map((s) => `<li><a href="#/sources/${encodeURIComponent(s.id)}">${esc(s.publisher)}</a></li>`).join('')}${cited.length > 60 ? `<li class="muted">+ ${cited.length - 60} more</li>` : ''}</ul>
        </section>` : ''}
      </footer>` : '';

    const promptBadge = brief.prompt_version
      ? `<a class="badge badge--accent" href="#/about?at=changelog" title="Editorial-policy version that produced this brief">prompt v${esc(brief.prompt_version)}</a>`
      : '';

    return `
      <article class="brief-layout" data-brief="${esc(brief.name)}">
        <div>
          <div class="brief-meta">
            <span><strong>${esc(brief.kind)}</strong></span>
            <span class="mono">${esc(brief.name)}</span>
            ${brief.generated_by ? `<span>${esc(brief.generated_by)}</span>` : ''}
            ${promptBadge}
            <span>${esc(brief.items)} item${brief.items === 1 ? '' : 's'}</span>
            ${brief.cves.length ? `<span>${esc(brief.cves.length)} CVE${brief.cves.length === 1 ? '' : 's'}</span>` : ''}
            <span class="meta-actions">
              <button type="button" data-action="share" data-brief="${esc(brief.name)}" title="Copy permalink">Copy link</button>
              <a href="${esc(brief.path)}" target="_blank" rel="noopener noreferrer" title="View raw Markdown on GitHub Pages">Raw .md</a>
            </span>
          </div>
          <details class="toc-mobile">
            <summary>On this page</summary>
            <div class="toc-mobile-body aside-toc">${tocHtml}</div>
          </details>
          <div class="brief-prose">${md(body)}</div>
          ${citedFooter}
        </div>
        <aside class="aside-toc aside-toc--desktop" aria-label="In this brief">
          ${tocHtml}
        </aside>
      </article>
    `;
  }

  /* ── briefs index ───────────────────────────────────────────── */

  function renderBriefs(state) {
    const m = Store.manifest;
    const filterKind = state.filterKind || 'all';
    const search = state.q || '';

    const list = m.filter((b) => filterKind === 'all' || b.kind === filterKind)
      .filter((b) => {
        if (!search) return true;
        const q = search.toLowerCase();
        return b.title.toLowerCase().includes(q) ||
               b.name.toLowerCase().includes(q) ||
               b.tldr.some((t) => t.toLowerCase().includes(q)) ||
               b.cves.some((c) => c.toLowerCase().includes(q));
      });

    const grouped = groupByMonth(list);

    return `
      <h1>Briefs</h1>
      <p class="subtitle">${m.length} brief${m.length === 1 ? '' : 's'}, newest first. Each brief is a Markdown file under <code>briefs/</code>; click through for the full text.</p>

      <div class="toolbar">
        <input class="input" id="briefs-q" type="search" placeholder="Filter by title, CVE, or TL;DR…" value="${attr(search)}" autocomplete="off" spellcheck="false" />
        <span class="chip ${filterKind === 'all' ? 'active' : ''}" data-kind="all">All</span>
        <span class="chip ${filterKind === 'daily' ? 'active' : ''}" data-kind="daily">Daily</span>
        <span class="chip ${filterKind === 'weekly' ? 'active' : ''}" data-kind="weekly">Weekly</span>
        <a class="chip" href="feed.xml" target="_blank" rel="noopener noreferrer" title="RSS feed">RSS</a>
      </div>

      ${list.length === 0
        ? `<div class="empty">No briefs match the current filters.</div>`
        : grouped.map(({ key, label, items }) => `
          <section style="margin-top: 1.4rem">
            <h2 class="section-head">${esc(label)}</h2>
            <ul class="entity-list">
              ${items.map((b) => `
                <li>
                  <span>
                    <a class="e-title" href="#/briefs/${esc(b.name)}">${esc(b.title)}</a>
                    <div class="e-meta">
                      <span class="e-tag">${esc(b.kind)}</span>
                      <span>${esc(b.items)} item${b.items === 1 ? '' : 's'}</span>
                      ${b.cves.length ? `<span>${esc(b.cves.length)} CVE${b.cves.length === 1 ? '' : 's'}</span>` : ''}
                      ${b.tldr.length ? `<span>${esc(b.tldr.length)} TL;DR bullet${b.tldr.length === 1 ? '' : 's'}</span>` : ''}
                    </div>
                  </span>
                  <span class="mono muted">${esc(b.name)}</span>
                </li>
              `).join('')}
            </ul>
          </section>
        `).join('')
      }
    `;
  }

  function groupByMonth(briefs) {
    const groups = new Map();
    for (const b of briefs) {
      let key, label;
      if (b.kind === 'weekly') { key = 'weekly'; label = 'Weekly summaries'; }
      else {
        key = b.name.slice(0, 7);
        const dt = new Date(b.name + 'T00:00:00Z');
        label = isNaN(dt.getTime()) ? key : dt.toLocaleString('en-US', { month: 'long', year: 'numeric', timeZone: 'UTC' });
      }
      if (!groups.has(key)) groups.set(key, { key, label, items: [] });
      groups.get(key).items.push(b);
    }
    return Array.from(groups.values());
  }

  /* ── single brief ───────────────────────────────────────────── */

  async function renderBrief(state) {
    const brief = Store.findBrief(state.name);
    if (!brief) return notFound(`Brief ${esc(state.name)} not found.`);
    return `<h1>${esc(brief.title)}</h1>${await renderBriefBody(brief)}`;
  }

  /* ── CVEs ───────────────────────────────────────────────────── */

  function renderCves(state) {
    const all = Store.cves.cves;
    const q = (state.q || '').toLowerCase().trim();
    const list = !q ? all : all.filter((c) =>
      c.id.toLowerCase().includes(q) ||
      (c.title || '').toLowerCase().includes(q) ||
      (c.appearances || []).some((b) => b.includes(q))
    );

    return `
      <h1>CVEs</h1>
      <p class="subtitle">${all.length} CVE${all.length === 1 ? '' : 's'} referenced across all briefs. Click an ID for the full appearance trail.</p>

      <div class="toolbar">
        <input class="input" id="cves-q" type="search" placeholder="Filter by CVE id, title, or brief date…" value="${attr(state.q || '')}" autocomplete="off" spellcheck="false" />
      </div>

      ${list.length === 0 ? `<div class="empty">No CVEs match.</div>` : `
        <div class="data-wrap">
          <table class="data">
            <thead>
              <tr><th>CVE</th><th>Title</th><th>First seen</th><th>Last seen</th><th>Appears in</th></tr>
            </thead>
            <tbody>
              ${list.map((c) => `
                <tr>
                  <td class="cve-id"><a href="#/cves/${esc(c.id)}">${esc(c.id)}</a></td>
                  <td>${esc(c.title || '')}</td>
                  <td class="mono muted">${esc(c.first_seen || '')}</td>
                  <td class="mono muted">${esc(c.last_seen || '')}</td>
                  <td>${(c.appearances || []).map((n) => `<a href="#/briefs/${esc(n)}" class="mono" style="margin-right:0.4rem">${esc(n)}</a>`).join('')}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      `}
    `;
  }

  function renderCve(state) {
    const cve = Store.findCve(state.id);
    if (!cve) return notFound(`CVE ${esc(state.id)} not found in any brief.`);

    const citations = Array.isArray(cve.citations) ? cve.citations : [];

    // Group citations by host so the reader sees one row per publisher.
    // Within a host, multiple URLs (different articles from the same
    // outlet) appear as a comma-separated list.
    const grouped = new Map();
    for (const cite of citations) {
      const key = cite.host || cite.url;
      if (!grouped.has(key)) grouped.set(key, []);
      grouped.get(key).push(cite);
    }
    // Stable order: publisher hosts alphabetically, with the primary
    // source's host first when present.
    const primaryHost = cve.primary_source_url ? hostOf(cve.primary_source_url) : '';
    const sortedHosts = Array.from(grouped.keys()).sort((a, b) => {
      if (a === primaryHost) return -1;
      if (b === primaryHost) return 1;
      return a.localeCompare(b);
    });

    // Flatten the grouped structure into one row per citation, with the
    // host name as the primary clickable action — opens the actual article
    // URL in a new tab — and a muted secondary link to the source's
    // `#/sources/<id>` page when known. One-click pivot to new
    // information, which is the whole point of the CVE detail page.
    const citationsBlock = citations.length === 0 ? '' : `
      <h3 style="margin-top:1.2rem">All cited sources for this CVE (${citations.length})</h3>
      <ul class="cite-list">
        ${sortedHosts.map((h) => {
          const list = grouped.get(h);
          const sourceId = list.find((c) => c.source_id)?.source_id;
          const isPrimary = h === primaryHost;
          return list.map((c) => {
            const briefSet = Array.from(new Set(c.briefs || [])).sort().reverse();
            return `<li class="cite">
              <a class="cite-link" href="${attr(c.url)}" target="_blank" rel="noopener noreferrer" title="Open ${attr(c.url)} in a new tab">
                <span class="cite-host">${esc(h)}</span>
                ${isPrimary ? `<span class="badge badge--accent" title="Primary source recorded by the agent">primary</span>` : ''}
                <span class="cite-label">${esc(c.label || c.url)}</span>
                <span class="cite-url muted">${esc(c.url)}</span>
              </a>
              <div class="cite-meta muted">
                ${sourceId ? `<a href="#/sources/${encodeURIComponent(sourceId)}" title="Source profile in this site">source profile</a> · ` : ''}
                cited in ${briefSet.map((n) => `<a href="#/briefs/${esc(n)}" class="mono">${esc(n)}</a>`).join(', ')}
              </div>
            </li>`;
          }).join('');
        }).join('')}
      </ul>
    `;

    return `
      <h1 class="mono">${esc(cve.id)}</h1>
      <p class="subtitle">${esc(cve.title || 'No title recorded.')}</p>

      <div class="panel">
        <div class="row" style="justify-content:space-between">
          <div>
            <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">First seen</div>
            <div class="mono">${esc(cve.first_seen || '—')}</div>
          </div>
          <div>
            <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">Last seen</div>
            <div class="mono">${esc(cve.last_seen || '—')}</div>
          </div>
          <div>
            <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">Appearances</div>
            <div class="mono">${(cve.appearances || []).length}</div>
          </div>
        </div>

        <h3 style="margin-top:1.2rem">External references</h3>
        <p>
          <a href="https://nvd.nist.gov/vuln/detail/${esc(cve.id)}" target="_blank" rel="noopener noreferrer">NVD</a> ·
          <a href="https://www.cve.org/CVERecord?id=${esc(cve.id)}" target="_blank" rel="noopener noreferrer">cve.org</a> ·
          <a href="${cisaKevSearchUrl(cve.id)}" target="_blank" rel="noopener noreferrer" title="CISA KEV catalog filtered to this CVE">CISA KEV</a>
        </p>

        ${citationsBlock}
      </div>

      <h2 class="section-head" style="margin-top:1.5rem">Brief appearances</h2>
      ${(cve.appearances || []).length === 0
        ? `<p class="muted">No briefs reference this CVE yet.</p>`
        : `<ul class="entity-list">${
          cve.appearances.map((n) => {
            const b = Store.findBrief(n);
            return `<li>
              <span>
                <a class="e-title" href="#/briefs/${esc(n)}">${b ? esc(b.title) : esc(n)}</a>
                ${b ? `<div class="e-meta"><span class="e-tag">${esc(b.kind)}</span><span>${esc(b.items)} items</span></div>` : ''}
              </span>
              <span class="mono muted">${esc(n)}</span>
            </li>`;
          }).join('')
        }</ul>`}
    `;
  }

  function hostOf(url) {
    try { return new URL(url).hostname.toLowerCase().replace(/^www\./, ''); }
    catch (_) { return ''; }
  }

  /* ── Topics (covered_items) ─────────────────────────────────── */

  function renderTopics(state) {
    const all = Store.topics.items;
    const q = (state.q || '').toLowerCase().trim();
    const filterType = state.filterType || 'all';
    const filterFlag = state.filterFlag || 'all';
    const list = all
      .filter((t) => filterType === 'all' || t.type === filterType)
      .filter((t) => {
        if (filterFlag === 'all') return true;
        if (filterFlag === 'multi') return !(t.flags || []).some((f) => f.startsWith('SINGLE-SOURCE'));
        return (t.flags || []).includes(filterFlag);
      })
      .filter((t) => !q ||
        t.title.toLowerCase().includes(q) ||
        t.key.toLowerCase().includes(q) ||
        t.type.toLowerCase().includes(q));

    const types = Array.from(new Set(all.map((t) => t.type))).sort();

    return `
      <h1>Topics</h1>
      <p class="subtitle">CVEs, actors, campaigns, incidents, tools, and annual reports tracked across briefs. The badge marks items covered in more than one brief — these are the "stories that unfolded".</p>

      <div class="toolbar">
        <input class="input" id="topics-q" type="search" placeholder="Filter topics…" value="${attr(state.q || '')}" autocomplete="off" spellcheck="false" />
        <span class="chip ${filterType === 'all' ? 'active' : ''}" data-type="all">All types</span>
        ${types.map((t) => `<span class="chip ${filterType === t ? 'active' : ''}" data-type="${esc(t)}">${esc(t)}</span>`).join('')}
      </div>
      <div class="toolbar" style="margin-top:-0.5rem">
        <span class="chip ${filterFlag === 'all' ? 'active' : ''}" data-flag="all">All verification</span>
        <span class="chip ${filterFlag === 'multi' ? 'active' : ''}" data-flag="multi" title="Items where two-source verification held (no single-source flag)">Corroborated</span>
        <span class="chip ${filterFlag === 'SINGLE-SOURCE' ? 'active' : ''}" data-flag="SINGLE-SOURCE">Single-source (any)</span>
        <span class="chip ${filterFlag === 'SINGLE-SOURCE-NATIONAL-CERT' ? 'active' : ''}" data-flag="SINGLE-SOURCE-NATIONAL-CERT">National-CERT only</span>
        <span class="chip ${filterFlag === 'SINGLE-SOURCE-OTHER' ? 'active' : ''}" data-flag="SINGLE-SOURCE-OTHER">Other single-source</span>
      </div>

      ${list.length === 0 ? `<div class="empty">No topics match.</div>` : `
        <ul class="entity-list">
          ${list.map((t) => {
            const n = (t.briefs || []).length;
            const flagBadges = (t.flags || []).map((f) => `<span class="badge badge--low" title="Verification flag">${esc(f)}</span>`).join(' ');
            return `<li>
              <span>
                <a class="e-title" href="#/topics/${encodeURIComponent(t.key)}">${esc(t.title)}</a>
                <div class="e-meta">
                  <span class="e-tag">${esc(t.type)}</span>
                  <span class="mono">${esc(t.key)}</span>
                  <span>last covered ${esc(t.last_covered || '—')}</span>
                  ${n > 1 ? `<span class="badge badge--accent" title="Story unfolds across ${n} briefs">×${n} appearances</span>` : ''}
                  ${flagBadges}
                </div>
              </span>
              <span>
                ${(t.briefs || []).slice(0, 5).map((b) => `<a href="#/briefs/${esc(b)}" class="mono" style="margin-left:0.35rem">${esc(b)}</a>`).join('')}
              </span>
            </li>`;
          }).join('')}
        </ul>
      `}
    `;
  }

  function renderTopic(state) {
    const t = Store.findTopic(state.key);
    if (!t) return notFound(`Topic <code>${esc(state.key)}</code> not found.`);

    const apps = (t.appearances || []).slice().sort((a, b) => (b.date || '').localeCompare(a.date || ''));
    const citations = Array.isArray(t.citations) ? t.citations : [];

    // Same per-citation layout as the CVE detail page — the entire row
    // is a one-click pivot to the source article.
    const grouped = new Map();
    for (const cite of citations) {
      const key = cite.host || cite.url;
      if (!grouped.has(key)) grouped.set(key, []);
      grouped.get(key).push(cite);
    }
    const primaryHost = t.primary_source_url ? hostOf(t.primary_source_url) : '';
    const sortedHosts = Array.from(grouped.keys()).sort((a, b) => {
      if (a === primaryHost) return -1;
      if (b === primaryHost) return 1;
      return a.localeCompare(b);
    });
    const citationsBlock = citations.length === 0 ? '' : `
      <h3 style="margin-top:1.2rem">All cited sources for this topic (${citations.length})</h3>
      <ul class="cite-list">
        ${sortedHosts.map((h) => {
          const list = grouped.get(h);
          const sourceId = list.find((c) => c.source_id)?.source_id;
          const isPrimary = h === primaryHost;
          return list.map((c) => {
            const briefSet = Array.from(new Set(c.briefs || [])).sort().reverse();
            return `<li class="cite">
              <a class="cite-link" href="${attr(c.url)}" target="_blank" rel="noopener noreferrer" title="Open ${attr(c.url)} in a new tab">
                <span class="cite-host">${esc(h)}</span>
                ${isPrimary ? `<span class="badge badge--accent" title="Primary source recorded by the agent">primary</span>` : ''}
                <span class="cite-label">${esc(c.label || c.url)}</span>
                <span class="cite-url muted">${esc(c.url)}</span>
              </a>
              <div class="cite-meta muted">
                ${sourceId ? `<a href="#/sources/${encodeURIComponent(sourceId)}" title="Source profile in this site">source profile</a> · ` : ''}
                cited in ${briefSet.map((n) => `<a href="#/briefs/${esc(n)}" class="mono">${esc(n)}</a>`).join(', ')}
              </div>
            </li>`;
          }).join('');
        }).join('')}
      </ul>
    `;

    return `
      <h1>${esc(t.title)}</h1>
      <p class="subtitle"><span class="badge badge--accent">${esc(t.type)}</span> · <span class="mono">${esc(t.key)}</span></p>

      <div class="panel">
        <div class="row" style="justify-content:space-between">
          <div>
            <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">First covered</div>
            <div class="mono">${esc(t.first_covered || '—')}</div>
          </div>
          <div>
            <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">Last covered</div>
            <div class="mono">${esc(t.last_covered || '—')}</div>
          </div>
          <div>
            <div class="muted" style="font-size:0.78rem;text-transform:uppercase;letter-spacing:0.06em">Appearances</div>
            <div class="mono">${esc(apps.length)}</div>
          </div>
        </div>

        ${citationsBlock}
      </div>

      <h2 class="section-head" style="margin-top:1.5rem">Story timeline</h2>
      ${apps.length === 0
        ? `<p class="muted">No recorded appearances.</p>`
        : `<ol class="entity-list" style="list-style:none">
          ${apps.map((a) => {
            const m = (a.brief_path || '').match(/(\d{4}-\d{2}-\d{2}|\d{4}-W\d{2})/);
            const name = m ? m[1] : '';
            const b = name ? Store.findBrief(name) : null;
            return `<li>
              <span>
                <span class="mono" style="margin-right:0.6rem">${esc(a.date || name || '')}</span>
                <a href="#/briefs/${esc(name)}">${b ? esc(b.title) : esc(name || '?')}</a>
                <div class="e-meta" style="margin-top:0.2rem">
                  <span class="e-tag">${esc(a.section || '—')}</span>
                  ${a.delta_summary ? `<span class="muted">${esc(a.delta_summary)}</span>` : ''}
                </div>
              </span>
            </li>`;
          }).join('')}
        </ol>`}
    `;
  }

  /* ── Sources ────────────────────────────────────────────────── */

  function renderSources(state) {
    const all = Store.sources.sources;
    const q = (state.q || '').toLowerCase().trim();
    const filterCat = state.filterCat || 'all';
    const filterStatus = state.filterStatus || 'all';
    const list = all
      .filter((s) => filterCat === 'all' || (s.category || []).includes(filterCat))
      .filter((s) => filterStatus === 'all' || s.status === filterStatus)
      .filter((s) => !q ||
        s.publisher.toLowerCase().includes(q) ||
        s.id.toLowerCase().includes(q) ||
        (s.notes || '').toLowerCase().includes(q) ||
        (s.url || '').toLowerCase().includes(q));

    const cats = Array.from(new Set(all.flatMap((s) => s.category || []))).sort();
    const stats = Array.from(new Set(all.map((s) => s.status))).sort();

    return `
      <h1>Sources</h1>
      <p class="subtitle">${all.length} curated source${all.length === 1 ? '' : 's'}. Each source can be searched and shows the briefs that have cited it.</p>

      <div class="toolbar">
        <input class="input" id="sources-q" type="search" placeholder="Filter by name, id, notes, URL…" value="${attr(state.q || '')}" autocomplete="off" spellcheck="false" />
        <span class="chip ${filterCat === 'all' ? 'active' : ''}" data-cat="all">All categories</span>
        ${cats.map((c) => `<span class="chip ${filterCat === c ? 'active' : ''}" data-cat="${esc(c)}">${esc(c)}</span>`).join('')}
      </div>
      <div class="toolbar" style="margin-top:-0.5rem">
        <span class="chip ${filterStatus === 'all' ? 'active' : ''}" data-status="all">All statuses</span>
        ${stats.map((s) => `<span class="chip ${filterStatus === s ? 'active' : ''}" data-status="${esc(s)}">${esc(s)}</span>`).join('')}
      </div>

      ${list.length === 0 ? `<div class="empty">No sources match.</div>` : `
        <div class="data-wrap">
          <table class="data">
            <thead>
              <tr><th>Publisher</th><th>Reliability</th><th>Status</th><th>Categories</th><th>Cited in</th></tr>
            </thead>
            <tbody>
              ${list.map((s) => `
                <tr>
                  <td>
                    <a href="#/sources/${encodeURIComponent(s.id)}"><strong>${esc(s.publisher)}</strong></a>
                    <div class="muted mono" style="font-size:0.75rem">${esc(s.id)}</div>
                  </td>
                  <td>${reliabilityBadge(s.reliability)}</td>
                  <td>${statusBadge(s.status)}</td>
                  <td><div class="e-meta">${(s.category || []).map((c) => `<span class="e-tag">${esc(c)}</span>`).join('')}</div></td>
                  <td>${(s.appearances || []).slice(0, 6).map((n) => `<a href="#/briefs/${esc(n)}" class="mono" style="margin-right:0.3rem">${esc(n)}</a>`).join('')}${(s.appearances || []).length > 6 ? ` <span class="muted">+${s.appearances.length - 6}</span>` : ''}</td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      `}
    `;
  }

  function renderSource(state) {
    const s = Store.findSource(state.id);
    if (!s) return notFound(`Source <code>${esc(state.id)}</code> not found.`);

    return `
      <h1>${esc(s.publisher)}</h1>
      <p class="subtitle"><span class="mono">${esc(s.id)}</span> · ${reliabilityBadge(s.reliability)} · ${statusBadge(s.status)}</p>

      <div class="panel">
        <p><a href="${attr(s.url)}" target="_blank" rel="noopener noreferrer">${esc(s.url)}</a></p>
        <div class="e-meta" style="margin-top:0.4rem">
          ${(s.category || []).map((c) => `<span class="e-tag">${esc(c)}</span>`).join('')}
          ${(s.language || []).map((c) => `<span class="e-tag">lang: ${esc(c)}</span>`).join('')}
          ${typeof s.consecutive_fetch_failures === 'number' ? `<span class="e-tag">fetch failures: ${esc(s.consecutive_fetch_failures)}</span>` : (typeof s.consecutive_failures === 'number' ? `<span class="e-tag">failures: ${esc(s.consecutive_failures)}</span>` : '')}
          ${typeof s.consecutive_quiet_periods === 'number' ? `<span class="e-tag">quiet periods: ${esc(s.consecutive_quiet_periods)}</span>` : ''}
          <span class="e-tag">last fetch: ${esc(s.last_successful_fetch || 'never')}</span>
        </div>
        ${s.notes ? `<p class="muted" style="margin-top: 0.7rem">${esc(s.notes)}</p>` : ''}
      </div>

      <h2 class="section-head" style="margin-top:1.5rem">Cited in ${(s.appearances || []).length} brief${(s.appearances || []).length === 1 ? '' : 's'}</h2>
      ${(s.appearances || []).length === 0 ? `<p class="muted">Not cited in any brief yet.</p>` : `
        <ul class="entity-list">
          ${s.appearances.map((n) => {
            const b = Store.findBrief(n);
            return `<li>
              <span>
                <a class="e-title" href="#/briefs/${esc(n)}">${b ? esc(b.title) : esc(n)}</a>
                ${b ? `<div class="e-meta"><span class="e-tag">${esc(b.kind)}</span><span>${esc(b.items)} items</span></div>` : ''}
              </span>
              <span class="mono muted">${esc(n)}</span>
            </li>`;
          }).join('')}
        </ul>
      `}
    `;
  }

  /* ── Operations dashboard (uses state/run_log.json) ────────── */

  async function renderOps() {
    let runLog = null;
    try {
      const res = await fetch('data/run_log.json');
      if (res.ok) runLog = await res.json();
    } catch (_) {}

    const runs = (runLog && Array.isArray(runLog.runs)) ? runLog.runs.slice().reverse() : [];

    const sources = Store.sources.sources || [];
    const today = new Date();
    const lastFetchByDays = sources.map((s) => {
      const lf = s.last_successful_fetch;
      if (!lf || !/^\d{4}-\d{2}-\d{2}$/.test(lf)) return { id: s.id, publisher: s.publisher, days: Infinity, status: s.status };
      const dt = new Date(lf + 'T00:00:00Z');
      const days = Math.round((today - dt) / 86400000);
      return { id: s.id, publisher: s.publisher, days, status: s.status, last: lf };
    }).filter((s) => s.status === 'active').sort((a, b) => b.days - a.days);

    const stale = lastFetchByDays.filter((s) => s.days > 7);

    return `
      <h1>Operations</h1>
      <p class="subtitle">Run log and source-rotation health. Sourced from <code>state/run_log.json</code> (per-run sub-agent allocation) and <code>sources/sources.json</code> (last-successful-fetch timestamps).</p>

      <h2 class="section-head">Recent runs</h2>
      ${runs.length === 0 ? `
        <div class="empty">
          <p>No <code>state/run_log.json</code> yet.</p>
          <p class="muted">The agent populates this file at the end of every run (Phase 5). The first scheduled run after this prompt change will create it.</p>
        </div>
      ` : `
        <div class="data-wrap">
          <table class="data">
            <thead>
              <tr><th>Date</th><th>Model</th><th>S1</th><th>S2</th><th>S3</th><th>S4</th><th>Failures</th><th>Items</th><th>Deep dive</th></tr>
            </thead>
            <tbody>
              ${runs.slice(0, 30).map((r) => {
                const sa = r.sub_agents || {};
                const fmt = (k) => {
                  const a = sa[k];
                  if (!a) return '<span class="muted">—</span>';
                  if (a.returned === false) return '<span class="badge badge--low">stalled</span>';
                  return `${esc(a.items_returned ?? 0)} <span class="muted">(${esc((a.sources_used || []).length)}/${esc((a.sources_attempted || []).length)} src)</span>`;
                };
                const failures = (r.fetch_failures || []).length;
                return `<tr>
                  <td class="mono"><a href="#/briefs/${esc(r.date)}">${esc(r.date)}</a></td>
                  <td class="mono muted">${esc(r.model || '')}</td>
                  <td>${fmt('S1')}</td>
                  <td>${fmt('S2')}</td>
                  <td>${fmt('S3')}</td>
                  <td>${fmt('S4')}</td>
                  <td>${failures > 0 ? `<span class="badge badge--med">${esc(failures)}</span>` : '<span class="muted">0</span>'}</td>
                  <td>${esc(r.items_published ?? '')}</td>
                  <td class="mono muted">${esc(r.deep_dive || '—')}</td>
                </tr>`;
              }).join('')}
            </tbody>
          </table>
        </div>
      `}

      <h2 class="section-head" style="margin-top:1.8rem">Stale active sources (>7 days since last successful fetch)</h2>
      ${stale.length === 0 ? `<p class="muted">No active source has been silent for more than a week.</p>` : `
        <ul class="entity-list">
          ${stale.map((s) => `<li>
            <span>
              <a class="e-title" href="#/sources/${encodeURIComponent(s.id)}">${esc(s.publisher)}</a>
              <div class="e-meta">
                <span class="e-tag">${esc(s.days === Infinity ? 'never fetched' : s.days + ' days')}</span>
                ${s.last ? `<span class="muted">last: ${esc(s.last)}</span>` : ''}
              </div>
            </span>
            <span class="mono muted">${esc(s.id)}</span>
          </li>`).join('')}
        </ul>
      `}

      <p class="muted" style="font-size:0.78rem; margin-top:1rem">
        See <a href="#/about?at=architecture">Architecture</a> for how the run log is produced.
      </p>
    `;
  }

  /* ── search results page ───────────────────────────────────── */

  function renderSearch(state) {
    const q = state.q || '';
    const results = q ? Search.query(Store.search, q, { limit: 200 }) : [];
    const grouped = { brief: [], section: [], cve: [], topic: [], source: [] };
    for (const r of results) (grouped[r.kind] || (grouped[r.kind] = [])).push(r);

    function groupBlock(label, items) {
      if (!items.length) return '';
      return `
        <section style="margin-top:1.2rem">
          <h2 class="section-head">${esc(label)} <span class="muted" style="font-size:0.78rem">${items.length}</span></h2>
          <ul class="entity-list">
            ${items.map((r) => `<li>
              <span>
                <a class="e-title" href="${attr(r.route)}">${Search.highlight(r.title, q)}</a>
                <div class="e-meta">
                  <span class="e-tag">${esc(r.kind)}</span>
                  ${r.hint ? `<span>${Search.highlight(r.hint, q)}</span>` : ''}
                </div>
              </span>
            </li>`).join('')}
          </ul>
        </section>`;
    }

    return `
      <h1>Search</h1>
      <p class="subtitle">${q ? `${results.length} result${results.length === 1 ? '' : 's'} for `+ '<code>'+esc(q)+'</code>' : 'Type a query in the top search bar, or below.'}</p>

      <div class="toolbar">
        <input class="input" id="search-q" type="search" placeholder="Search briefs · sections · CVEs · topics · sources…" value="${attr(q)}" autocomplete="off" spellcheck="false" />
      </div>

      ${q && !results.length ? `<div class="empty">No matches.</div>` : ''}
      ${groupBlock('Briefs',   grouped.brief)}
      ${groupBlock('Sections', grouped.section)}
      ${groupBlock('CVEs',     grouped.cve)}
      ${groupBlock('Topics',   grouped.topic)}
      ${groupBlock('Sources',  grouped.source)}
    `;
  }

  /* ── About ──────────────────────────────────────────────────── */

  async function renderAbout() {
    async function safeFetch(path) {
      try { const r = await fetch(path); return r.ok ? await r.text() : ''; }
      catch { return ''; }
    }
    const [readme, architecture, workflow, verification, security, routine, improvements, changelog] = await Promise.all([
      safeFetch('docs/README.md'),
      safeFetch('docs/architecture.md'),
      safeFetch('docs/workflow.md'),
      safeFetch('docs/verification.md'),
      safeFetch('docs/security-review.md'),
      safeFetch('docs/routine-setup.md'),
      safeFetch('docs/improvements.md'),
      safeFetch('docs/CHANGELOG.md'),
    ]);

    function block(title, body, slug, opts) {
      if (!body) return '';
      const open = (opts && opts.open) ? ' open' : '';
      const id = slug || title.toLowerCase().replace(/[^a-z0-9]+/g, '-');
      return `
        <details class="panel" style="margin-top:1.2rem" id="about-${id}"${open}>
          <summary style="cursor:pointer;font-weight:600;font-size:1.05rem">${esc(title)}</summary>
          <div class="brief-prose" style="margin-top:0.8rem">${md(body)}</div>
        </details>`;
    }

    const analytics = `
This site uses **Umami Cloud** to record aggregate visitor counts so the
operator can see whether the newsletter is being read. Umami is a
privacy-by-design alternative to mainstream analytics products:

- **No cookies** are set on your device.
- **No fingerprinting** — Umami does not build a per-visitor profile across sites.
- **No personal data** is collected. The aggregate fields are page URL,
  referrer host, country (from IP, then the IP is discarded), and a
  daily-rotated hash that lets Umami count "unique visitors today"
  without persisting an identifier.
- **Honours \`navigator.doNotTrack\`** — when DNT or Global Privacy Control
  is set, the tracker is a complete no-op.
- **Search-string parameters are excluded** from collection
  (\`data-exclude-search="true"\`).

The script is loaded from \`https://cloud.umami.is/script.js\`. The site's
strict Content Security Policy allows only \`'self'\` and
\`https://cloud.umami.is\` for both \`script-src\` and \`connect-src\`
— no other third-party origin can run code or receive data from this
page. The site's website ID is public (it is in the page source) and is
\`abe09860-85be-4b06-8383-002f2e598061\`.

Umami's privacy policy: <https://umami.is/privacy>. To opt out
completely, enable Do Not Track in your browser; the script self-disables.
You can also block it at the network layer — \`cloud.umami.is\` — without
breaking the site.

The agent's editorial decisions are **not** influenced by Umami. The
brief prompt has no input from this signal. It exists for the operator,
not for the writer.`;

    return `
      <h1>About this newsletter</h1>
      <p class="subtitle">This page is the project's main README rendered in-place — the same file at <code>README.md</code> in the repository. The deeper documents under <code>docs/</code> are surfaced below as collapsible sections.</p>

      <div class="brief-prose">${md(readme)}</div>

      <h2 class="section-head" style="margin-top:2rem">Deeper documentation</h2>
      <p class="muted" style="font-size:0.85rem">Click each section to expand. These render the source files in <code>docs/</code> directly — to edit them, edit those files in the repository.</p>
      ${block('Architecture', architecture, 'architecture')}
      ${block('Workflow', workflow, 'workflow')}
      ${block('Verification policy', verification, 'verification')}
      ${block('Routine setup', routine, 'routine-setup')}
      ${block('Security review (threat model)', security, 'security-review')}
      ${block('Analytics & privacy', analytics, 'analytics')}
      ${block('Recommended improvements', improvements, 'improvements')}
      ${block('Editorial-policy CHANGELOG', changelog, 'changelog')}
    `;
  }

  /* ── Not found ─────────────────────────────────────────────── */

  function notFound(msg) {
    return `<div class="empty">
      <h1>Not found</h1>
      <p>${msg || 'No content for this URL.'}</p>
      <p><a href="#/">← back home</a></p>
    </div>`;
  }

  window.Render = {
    home: renderHome,
    briefs: renderBriefs,
    brief: renderBrief,
    cves: renderCves,
    cve: renderCve,
    topics: renderTopics,
    topic: renderTopic,
    sources: renderSources,
    source: renderSource,
    ops: renderOps,
    search: renderSearch,
    about: renderAbout,
    notFound,
    md,
    esc,
    selfTest,
    renderUnsafeReason,
    trustHtml,
  };
})();
