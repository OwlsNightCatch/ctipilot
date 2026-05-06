/* render.js — view templates for each route.

   Each render fn returns an HTML string. The router puts the result into #view.
   Markdown rendering goes through marked.js + DOMPurify (vendored), with link
   targets set to _blank for outbound publisher URLs.

   No template engine: small surface, easy to audit. The few places that
   inline user-controlled strings always pass through esc()/Search.escapeHtml().
*/

(function () {
  'use strict';

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
     and rel="noopener noreferrer". Catches every link in every rendered
     markdown body regardless of how marked produced it. Runs after the
     sanitizer's attribute-allowlist so we know target/rel are permitted
     (PURIFY_CFG.ADD_ATTR includes them). */
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

  /* Markdown rendering pipeline: marked → DOMPurify.

     The brief content includes inline links and quoted titles whose
     attacker-controlled text comes from third-party publisher pages. Even
     after the agent's verification chain, we treat all of it as untrusted
     by the time it reaches the browser. Defences:
       1. CSP meta tag (index.html) blocks inline scripts at the engine level.
       2. marked is configured with gfm + breaks; we explicitly do not
          enable raw HTML rendering of unsafe tags.
       3. DOMPurify with a restrictive allowlist strips script tags, on*
          handlers, and javascript:/data: in href/src.
  */
  /* Defence in depth — every option here is justified.

     USE_PROFILES.html              base allowlist of safe HTML tags.
     ADD_ATTR target, rel           markdown links opening in new tabs need
                                    these; the afterSanitizeAttributes hook
                                    sets them on every external link.
     FORBID_TAGS                    explicit superset over USE_PROFILES.html
                                    that strips every "executes / parses
                                    code" surface even if a future profile
                                    change loosens defaults.
     FORBID_ATTR                    attributes that have led to historic XSS
                                    even on otherwise-safe tags.
     FORBID_CONTENTS                drop the *text* of these tags too —
                                    avoids the case where DOMPurify keeps
                                    the inner content as inert text but a
                                    downstream regex / unsafe sink could
                                    still find a "javascript:" substring.
     ALLOW_DATA_ATTR false          arbitrary data-* leaks into JS via
                                    dataset; we never need them in briefs.
     ALLOW_UNKNOWN_PROTOCOLS false  belt-and-braces with ALLOWED_URI_REGEXP.
     ALLOWED_URI_REGEXP             only http(s):, mailto:, tel:, in-page
                                    anchor (#…), or relative path.
     SAFE_FOR_TEMPLATES             treats `${…}`-style template syntax as
                                    text everywhere, not interpolation.
     SANITIZE_DOM                   protects against DOM-clobbering via id
                                    or name attributes that shadow globals.
     SANITIZE_NAMED_PROPS           further DOM-clobbering protection on
                                    named-property access.
     KEEP_CONTENT                   default true — keep textual content of
                                    forbidden non-script tags so a stray
                                    <p> wrapped in <iframe> isn't lost.
     IN_PLACE / WHOLE_DOCUMENT      defaults; explicit so a future flip
                                    here would be deliberate.
     RETURN_TRUSTED_TYPE            we ship plain strings; if the page
                                    later opts into Trusted Types, flip
                                    this and add a policy in app.js. */
  const PURIFY_CFG = Object.freeze({
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
    FORBID_CONTENTS: ['style', 'script', 'iframe', 'noscript', 'noembed', 'noframes', 'svg', 'math'],
    ALLOW_DATA_ATTR: false,
    ALLOW_UNKNOWN_PROTOCOLS: false,
    ALLOWED_URI_REGEXP: /^(?:(?:https?|mailto|tel):|#|\/)/i,
    SAFE_FOR_TEMPLATES: true,
    SANITIZE_DOM: true,
    SANITIZE_NAMED_PROPS: true,
    KEEP_CONTENT: true,
    IN_PLACE: false,
    WHOLE_DOCUMENT: false,
    RETURN_TRUSTED_TYPE: false,
  });

  /** Boot-time XSS self-test for the markdown sanitisation pipeline.

     Runs a panel of known XSS vectors through the same marked + DOMPurify
     path that user content takes. After sanitisation, we parse the output
     into a detached document and look for *DOM-level* danger signals:
       - any forbidden tag actually rendered (script, iframe, svg, math,
         object, embed, form, meta, link, base, style, frame…)
       - any attribute starting with on* (event handlers)
       - any href/src/action/formaction/data starting with a dangerous
         scheme (javascript:, data:, vbscript:, file:)

     Substring-on-string checks are deliberately avoided because
     KEEP_CONTENT preserves inert text; a stripped <style> tag's CSS
     becomes harmless text that a regex would still match.

     If any vector survives, runtime markdown rendering is *disabled* and
     md() falls back to plain escaped text. The page stays usable; an
     attacker payload cannot execute. The failure is logged so the
     operator notices on the next visit / inspection. */

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

  /** Inspect sanitiser output as a DOM tree. Returns null if clean,
      otherwise a string describing the first danger signal found. */
  function findDangerInHtml(html) {
    let doc;
    try {
      doc = new DOMParser().parseFromString(`<div>${html}</div>`, 'text/html');
    } catch (_) {
      return 'DOMParser failed';
    }
    const root = doc.body;
    if (!root) return null;
    for (const el of root.querySelectorAll('*')) {
      const tag = (el.tagName || '').toLowerCase();
      if (FORBIDDEN_TAGS_LOWER.has(tag)) return `forbidden tag rendered: <${tag}>`;
      // attributes
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
    if (!window.marked || !window.DOMPurify) return null; // libs not loaded yet
    if (!configureMarked._done) { configureMarked(); configureMarked._done = true; }
    attachExternalLinkHook();
    for (const vec of XSS_VECTORS) {
      let out;
      try {
        out = DOMPurify.sanitize(marked.parse(vec || ''), PURIFY_CFG);
      } catch (e) {
        return `sanitiser threw on vector ${JSON.stringify(vec)}: ${e.message}`;
      }
      const reason = findDangerInHtml(out);
      if (reason) {
        return `vector ${JSON.stringify(vec)} survived: ${reason}; output=${out.slice(0,160)}`;
      }
    }
    return null;
  }

  /** Run the self-test once at module load; result is cached. Falls back
      to plain text rendering if the pipeline is broken. */
  function ensureSafe() {
    if (ensureSafe._ran) return !_renderUnsafe;
    ensureSafe._ran = true;
    const failure = selfTest();
    if (failure) {
      _renderUnsafe = failure;
      // eslint-disable-next-line no-console
      console.error('[CTI Briefs] markdown sanitiser self-test FAILED — falling back to plain text. Detail:', failure);
    }
    return !_renderUnsafe;
  }

  function md(markdown) {
    if (!window.marked || !window.DOMPurify) return esc(markdown);
    if (!configureMarked._done) { configureMarked(); configureMarked._done = true; }
    attachExternalLinkHook();
    if (!ensureSafe()) {
      // Pipeline broken or compromised — render as escaped plain text in <pre>.
      return `<pre class="muted" style="white-space:pre-wrap">${esc(markdown)}</pre>`;
    }
    const html = window.marked.parse(markdown || '');
    return window.DOMPurify.sanitize(html, PURIFY_CFG);
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

  function briefLink(name) {
    return `<a href="#/briefs/${esc(name)}" class="mono">${esc(name)}</a>`;
  }

  function timelineStrip(briefs, current) {
    if (!briefs || !briefs.length) return '';
    return `<div class="timeline-strip" aria-label="Brief appearances">
      ${briefs.map((n) => `<a href="#/briefs/${esc(n)}" class="${n === current ? 'current' : ''}" title="Brief ${esc(n)}">${esc(n)}</a>`).join('')}
    </div>`;
  }

  /* ── home (renders today's / latest daily brief inline) ─────── */

  async function renderHome() {
    const dailies = Store.manifest.filter((b) => b.kind === 'daily');
    const weeklies = Store.manifest.filter((b) => b.kind === 'weekly');
    const today = todayISO();
    const latestDaily = dailies.find((b) => b.name === today) || dailies[0];
    const latestWeekly = weeklies[0];

    if (!latestDaily) {
      return `<div class="empty">
        <h1>No briefs yet</h1>
        <p>The first daily routine run will publish a brief here.</p>
        <p><a href="#/about">About this newsletter →</a></p>
      </div>`;
    }

    const isToday = latestDaily.name === today;
    const banner = `
      <div class="home-banner">
        <div class="home-banner-left">
          <div class="home-banner-eyebrow">${isToday ? "Today's brief" : 'Latest brief'} · <span class="mono">${esc(latestDaily.name)}</span></div>
          <h1 style="margin:0.15rem 0 0">${esc(latestDaily.title)}</h1>
        </div>
        <div class="home-banner-right">
          ${latestWeekly
            ? `<a class="cta-weekly" href="#/briefs/weekly/${esc(latestWeekly.name)}" title="${esc(latestWeekly.title)}">
                <span class="cta-eyebrow">Weekly summary</span>
                <span class="cta-title">${esc(latestWeekly.name)} →</span>
               </a>`
            : `<span class="muted" style="font-size:0.85rem">No weekly summary yet — the first weekly routine will publish one on Sunday.</span>`}
        </div>
      </div>`;

    const briefHtml = await renderBriefBody(latestDaily);

    return `${banner}${briefHtml}${renderHomeFooter(latestDaily)}`;
  }

  function renderHomeFooter(currentBrief) {
    const counts = Store.site && Store.site.counts ? Store.site.counts : {};
    const eng = Store.engagement || {};
    const personal = window.Personal ? Personal.recent(5) : [];
    const top = (eng.by_brief || [])
      .filter((b) => b.name !== currentBrief.name)
      .slice(0, 5);

    const personalHtml = personal.length
      ? `<ul class="entity-list">${personal.map((p) => {
          const b = Store.findBrief(p.name);
          return `<li>
            <span><a class="e-title" href="#/briefs/${esc(p.name)}">${b ? esc(b.title) : esc(p.name)}</a>
              <div class="e-meta"><span class="e-tag">visited ${p.count}×</span><span class="muted">last ${esc(p.last)}</span></div>
            </span>
            <span class="mono muted">${esc(p.name)}</span>
          </li>`;
        }).join('')}</ul>
        <p class="muted" style="font-size:0.75rem;margin:0.4rem 0 0">Stored only on this device — never sent anywhere. <a href="#" data-action="clear-personal">Clear</a></p>`
      : `<p class="muted" style="font-size:0.85rem">Briefs you open on this device will appear here. Stored locally only.</p>`;

    const topHtml = top.length
      ? `<ul class="entity-list">${top.map((t) => {
          const b = Store.findBrief(t.name);
          return `<li>
            <span><a class="e-title" href="#/briefs/${esc(t.name)}">${b ? esc(b.title) : esc(t.name)}</a>
              <div class="e-meta"><span class="e-tag">${esc(t.views_14d || 0)} views</span>${t.uniques_14d ? `<span>${esc(t.uniques_14d)} unique</span>` : ''}</div>
            </span>
            <span class="mono muted">${esc(t.name)}</span>
          </li>`;
        }).join('')}</ul>
        <p class="muted" style="font-size:0.75rem;margin:0.4rem 0 0">Aggregate-only counts from GitHub Pages traffic — no IPs or sessions stored.</p>`
      : `<p class="muted" style="font-size:0.85rem">Aggregate engagement appears here once the daily traffic-sync action has run.</p>`;

    return `
      <section class="home-footer">
        <h2 class="section-head" style="margin-top:2rem">Continue exploring</h2>

        <div class="stat-grid" style="margin-bottom: 1.4rem">
          <div class="stat"><div class="v">${esc(counts.briefs || 0)}</div><div class="l"><a href="#/briefs">All briefs</a></div></div>
          <div class="stat"><div class="v">${esc(counts.cves || 0)}</div><div class="l"><a href="#/cves">CVEs tracked</a></div></div>
          <div class="stat"><div class="v">${esc(counts.topics || 0)}</div><div class="l"><a href="#/topics">Topics</a></div></div>
          <div class="stat"><div class="v">${esc(counts.sources || 0)}</div><div class="l"><a href="#/sources">Sources</a></div></div>
        </div>

        <div class="section-grid">
          <section class="panel section">
            <h2 class="section-head" style="margin-top:0">Top briefs (last 14d)</h2>
            ${topHtml}
          </section>
          <section class="panel section">
            <h2 class="section-head" style="margin-top:0">Your reading history</h2>
            ${personalHtml}
          </section>
        </div>

        <p class="muted" style="font-size:0.78rem; margin-top: 1rem; font-family: var(--mono)">build · ${esc((Store.site && Store.site.built_at) || '—')}${eng.updated_at ? ` · engagement · ${esc(eng.updated_at)}` : ''}</p>
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

  /** Shared body renderer used by home and the brief detail view. */
  async function renderBriefBody(brief) {
    let raw;
    try { raw = await Store.getMarkdown(brief.path); }
    catch (e) { return `<p class="muted">Failed to load <code>${esc(brief.path)}</code>: ${esc(e.message)}</p>`; }

    const body = raw.replace(/^# .+\n+/, '');
    const cves = Store.cvesInBrief(brief.name);
    const topics = Store.topicsInBrief(brief.name);
    const cited = Store.sourcesInBrief(brief.name);
    const sectionsToc = brief.sections.map((s) => `<li><a href="#${esc(s.anchor)}">${esc(s.heading)}</a></li>`).join('');
    const briefViews = (Store.engagement && (Store.engagement.by_brief || []).find((x) => x.name === brief.name)) || null;

    const cveList = cves.length ? `
      <h3>CVEs in this brief</h3>
      <ul style="list-style:none;padding:0;margin:0">
        ${cves.map((c) => `<li style="margin:0.25rem 0"><a href="#/cves/${esc(c.id)}" class="mono">${esc(c.id)}</a>${c.appearances.length > 1 ? ` <span class="badge badge--accent" title="Appears in ${c.appearances.length} briefs">×${c.appearances.length}</span>` : ''}</li>`).join('')}
      </ul>` : '';
    const topicList = topics.length ? `
      <h3>Tracked topics</h3>
      <ul style="list-style:none;padding:0;margin:0">
        ${topics.map((t) => `<li style="margin:0.25rem 0"><a href="#/topics/${encodeURIComponent(t.key)}">${esc(t.title)}</a>${(t.briefs || []).length > 1 ? ` <span class="badge badge--accent" title="Appears in ${t.briefs.length} briefs">×${t.briefs.length}</span>` : ''}</li>`).join('')}
      </ul>` : '';
    const sourceList = cited.length ? `
      <h3>Sources cited</h3>
      <ul style="list-style:none;padding:0;margin:0">
        ${cited.slice(0, 30).map((s) => `<li style="margin:0.25rem 0"><a href="#/sources/${encodeURIComponent(s.id)}">${esc(s.publisher)}</a></li>`).join('')}
        ${cited.length > 30 ? `<li class="muted">+ ${cited.length - 30} more</li>` : ''}
      </ul>` : '';

    return `
      <article class="brief-layout" data-brief="${esc(brief.name)}">
        <div>
          <div class="brief-meta">
            <span><strong>${esc(brief.kind)}</strong></span>
            <span class="mono">${esc(brief.name)}</span>
            ${brief.generated_by ? `<span>${esc(brief.generated_by)}</span>` : ''}
            <span>${esc(brief.items)} item${brief.items === 1 ? '' : 's'}</span>
            ${brief.cves.length ? `<span>${esc(brief.cves.length)} CVE${brief.cves.length === 1 ? '' : 's'}</span>` : ''}
            ${briefViews ? `<span title="GitHub Pages aggregate view count, last 14 days">${esc(briefViews.views_14d || 0)} views (14d)</span>` : ''}
          </div>
          <div class="brief-prose">${md(body)}</div>
        </div>
        <aside class="aside-toc" aria-label="In this brief">
          <h3>On this page</h3>
          <ul>${sectionsToc || '<li class="muted">—</li>'}</ul>
          ${cveList}
          ${topicList}
          ${sourceList}
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
      `}
    `;
  }

  function renderCve(state) {
    const cve = Store.findCve(state.id);
    if (!cve) return notFound(`CVE ${esc(state.id)} not found in any brief.`);

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

        ${cve.primary_source_url ? `
          <p style="margin-top: 0.9rem">
            <span class="muted">Primary source: </span>
            <a href="${attr(cve.primary_source_url)}" target="_blank" rel="noopener noreferrer">${esc(cve.primary_source_url)}</a>
          </p>` : ''}

        <h3 style="margin-top:1.2rem">External references</h3>
        <p>
          <a href="https://nvd.nist.gov/vuln/detail/${esc(cve.id)}" target="_blank" rel="noopener noreferrer">NVD</a> ·
          <a href="https://www.cve.org/CVERecord?id=${esc(cve.id)}" target="_blank" rel="noopener noreferrer">cve.org</a> ·
          <a href="https://www.cisa.gov/known-exploited-vulnerabilities-catalog" target="_blank" rel="noopener noreferrer">CISA KEV</a>
        </p>
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

  /* ── Topics (covered_items) ─────────────────────────────────── */

  function renderTopics(state) {
    const all = Store.topics.items;
    const q = (state.q || '').toLowerCase().trim();
    const filterType = state.filterType || 'all';
    const list = all
      .filter((t) => filterType === 'all' || t.type === filterType)
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
        <span class="chip ${filterType === 'all' ? 'active' : ''}" data-type="all">All</span>
        ${types.map((t) => `<span class="chip ${filterType === t ? 'active' : ''}" data-type="${esc(t)}">${esc(t)}</span>`).join('')}
      </div>

      ${list.length === 0 ? `<div class="empty">No topics match.</div>` : `
        <ul class="entity-list">
          ${list.map((t) => {
            const n = (t.briefs || []).length;
            return `<li>
              <span>
                <a class="e-title" href="#/topics/${encodeURIComponent(t.key)}">${esc(t.title)}</a>
                <div class="e-meta">
                  <span class="e-tag">${esc(t.type)}</span>
                  <span class="mono">${esc(t.key)}</span>
                  <span>last covered ${esc(t.last_covered || '—')}</span>
                  ${n > 1 ? `<span class="badge badge--accent" title="Story unfolds across ${n} briefs">×${n} appearances</span>` : ''}
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

        ${t.primary_source_url ? `
          <p style="margin-top: 0.9rem">
            <span class="muted">Primary source: </span>
            <a href="${attr(t.primary_source_url)}" target="_blank" rel="noopener noreferrer">${esc(t.primary_source_url)}</a>
          </p>` : ''}
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
      <div class="toolbar" style="margin-top:-0.6rem">
        <span class="chip ${filterStatus === 'all' ? 'active' : ''}" data-status="all">All statuses</span>
        ${stats.map((s) => `<span class="chip ${filterStatus === s ? 'active' : ''}" data-status="${esc(s)}">${esc(s)}</span>`).join('')}
      </div>

      ${list.length === 0 ? `<div class="empty">No sources match.</div>` : `
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
          ${typeof s.consecutive_failures === 'number' ? `<span class="e-tag">failures: ${esc(s.consecutive_failures)}</span>` : ''}
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

  /* ── search results page ───────────────────────────────────── */

  function renderSearch(state) {
    const q = state.q || '';
    const results = q ? Search.query(Store.search, q, { limit: 200 }) : [];
    const grouped = { brief: [], cve: [], topic: [], source: [] };
    for (const r of results) (grouped[r.kind] || []).push(r);

    function groupBlock(label, items, anchorRoute) {
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
        <input class="input" id="search-q" type="search" placeholder="Search briefs · CVEs · topics · sources…" value="${attr(q)}" autocomplete="off" spellcheck="false" />
      </div>

      ${q && !results.length ? `<div class="empty">No matches.</div>` : ''}
      ${groupBlock('Briefs',  grouped.brief)}
      ${groupBlock('CVEs',    grouped.cve)}
      ${groupBlock('Topics',  grouped.topic)}
      ${groupBlock('Sources', grouped.source)}
    `;
  }

  /* ── About ──────────────────────────────────────────────────── */

  async function renderAbout() {
    async function safeFetch(path) {
      try { const r = await fetch(path); return r.ok ? await r.text() : ''; }
      catch { return ''; }
    }
    const [readme, architecture, workflow, verification, security, improvements] = await Promise.all([
      safeFetch('docs/README.md'),
      safeFetch('docs/architecture.md'),
      safeFetch('docs/workflow.md'),
      safeFetch('docs/verification.md'),
      safeFetch('docs/security-review.md'),
      safeFetch('docs/improvements.md'),
    ]);

    function block(title, body) {
      if (!body) return '';
      const slug = title.toLowerCase().replace(/[^a-z0-9]+/g, '-');
      return `
        <details class="panel" style="margin-top:1.2rem" id="about-${slug}">
          <summary style="cursor:pointer;font-weight:600;font-size:1.05rem">${esc(title)}</summary>
          <div class="brief-prose" style="margin-top:0.8rem">${md(body)}</div>
        </details>`;
    }

    return `
      <h1>About this newsletter</h1>
      <p class="subtitle">Rendered from the repository's <code>README.md</code> and <code>docs/</code>. The same files govern the agent that writes the briefs — the docs and the runtime are kept in sync.</p>

      <div class="brief-prose">${md(readme)}</div>

      <h2 class="section-head" style="margin-top:2rem">Deeper documentation</h2>
      <p class="muted" style="font-size:0.85rem">Click each section to expand. These render the source files in <code>docs/</code> directly — to edit them, edit those files.</p>
      ${block('Architecture', architecture)}
      ${block('Workflow', workflow)}
      ${block('Verification policy', verification)}
      ${block('Security review (threat model)', security)}
      ${block('Recommended improvements', improvements)}
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
    search: renderSearch,
    about: renderAbout,
    notFound,
    md,
    esc,
    selfTest,                  // exposed for the boot-time check in app.js
    renderUnsafeReason,        // exposed so app.js can render a warning banner
  };
})();
