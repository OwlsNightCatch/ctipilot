/* brief.js — dynamic window logic for /brief/ (v3 pipeline).
 *
 * The page ships with the default 24 h window fully server-rendered, so
 * everything below is progressive enhancement: window chips (6/12/24/48/
 * 72 h), a "since date" input, and URL params (?hours=N / ?since=DATE).
 * On first control use (or on load when a URL param is present) the
 * script fetches data/briefbook.json ONCE and re-assembles the same
 * section structure client-side. Entries carry server-pre-rendered card
 * HTML — the client does pure grouping + concatenation, NO Markdown
 * parsing. Grouping constants come from the #brief-config JSON data
 * island (type application/json — never executed, CSP-safe).
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', init);

  function sitePrefix() {
    var m = document.querySelector('meta[name="cti-site-prefix"]');
    return (m && m.getAttribute('content')) || '';
  }

  var CFG = null;
  var bookPromise = null;

  function readConfig() {
    var el = document.getElementById('brief-config');
    if (!el) return null;
    try { return JSON.parse(el.textContent); } catch (_) { return null; }
  }

  function ensureBook() {
    if (bookPromise) return bookPromise;
    bookPromise = fetch(sitePrefix() + (CFG.briefbook_url || 'data/briefbook.json'))
      .then(function (r) {
        if (!r.ok) throw new Error('http ' + r.status);
        return r.json();
      });
    return bookPromise;
  }

  // DOM handles, resolved in init().
  var chips = null, fromInput = null, toInput = null, applyBtn = null;
  var HOUR_MS = 3600 * 1000;

  function init() {
    var root = document.getElementById('brief-sections');
    var controls = document.querySelector('[data-brief-controls]');
    CFG = readConfig();
    if (!root || !controls || !CFG) return;

    chips = controls.querySelectorAll('[data-window-hours]');
    fromInput = controls.querySelector('[data-window-from]');
    toInput = controls.querySelector('[data-window-to]');
    applyBtn = controls.querySelector('[data-window-apply]');

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var hours = parseInt(chip.getAttribute('data-window-hours'), 10);
        if (!(hours > 0)) return;
        setActiveChip(chips, chip);
        applyWindow({ hours: hours });
      });
    });

    if (applyBtn) applyBtn.addEventListener('click', applyCustomRange);
    [fromInput, toInput].forEach(function (inp) {
      if (!inp) return;
      inp.addEventListener('change', applyCustomRange);
      inp.addEventListener('keydown', function (e) {
        if (e.key === 'Enter') { e.preventDefault(); applyCustomRange(); }
      });
    });

    // ?hours=N  or  ?from=DD.MM.YYYY HH:MM&to=DD.MM.YYYY HH:MM  on load.
    var params = new URLSearchParams(window.location.search);
    var pHours = parseInt(params.get('hours') || '', 10);
    var pFrom = parseEU(params.get('from')), pTo = parseEU(params.get('to'));
    if (pFrom != null && pTo != null) {
      setActiveChip(chips, null);
      applyWindow({ from: pFrom, to: pTo }, { replaceUrl: false });
      return;
    }
    if (pHours > 0) {
      var matched = null;
      chips.forEach(function (c) {
        if (parseInt(c.getAttribute('data-window-hours'), 10) === pHours) matched = c;
      });
      setActiveChip(chips, matched);
      applyWindow({ hours: pHours }, { replaceUrl: false });
      return;
    }

    // No params: the server rendered [ref − default_hours, ref]. Normalise
    // the From/To boxes to that reference range without a fetch. If the
    // visitor's real clock has moved materially past the build's reference
    // moment, re-render the default against real "now" so the range shown
    // is honest (this is the only case that triggers the briefbook fetch
    // on load).
    var refMs = parseTs(CFG.reference_ts || CFG.generated_at);
    var dh = CFG.default_hours || 24;
    if (refMs != null) fillBoxes(refMs - dh * HOUR_MS, refMs);
    if (refMs != null && (Date.now() - refMs) > HOUR_MS) {
      applyWindow({ hours: dh }, { replaceUrl: false });
    }
  }

  function setActiveChip(chips, active) {
    chips.forEach(function (c) { c.classList.toggle('active', c === active); });
  }

  function markInvalid(inp, bad) {
    if (!inp) return;
    inp.classList.toggle('is-invalid', !!bad);
    if (bad) inp.setAttribute('aria-invalid', 'true');
    else inp.removeAttribute('aria-invalid');
  }

  function applyCustomRange() {
    var fMs = parseEU(fromInput && fromInput.value);
    var tMs = parseEU(toInput && toInput.value);
    markInvalid(fromInput, fMs == null);
    markInvalid(toInput, tMs == null);
    if (fMs == null || tMs == null) return;
    if (fMs > tMs) { var s = fMs; fMs = tMs; tMs = s; } // tolerate reversed entry
    setActiveChip(chips, null);
    applyWindow({ from: fMs, to: tMs });
  }

  function applyWindow(win, opts) {
    opts = opts || {};
    ensureBook().then(function (book) {
      var bounds = renderWindow(book, win);
      fillBoxes(bounds.since, bounds.until);
      if (opts.replaceUrl !== false && window.history && history.replaceState) {
        var q = win.hours
          ? ('?hours=' + win.hours)
          : ('?from=' + encodeURIComponent(fmtEU(bounds.since)) +
             '&to=' + encodeURIComponent(fmtEU(bounds.until)));
        history.replaceState(null, '', q);
      }
    }).catch(function () {
      var status = document.querySelector('[data-window-status]');
      if (status) status.textContent = 'could not load the entry book — showing the default window';
    });
  }

  // ── date helpers (European DD.MM.YYYY HH:MM, interpreted as UTC) ─────

  function pad2(n) { return (n < 10 ? '0' : '') + n; }

  function fmtEU(ms) {
    var d = new Date(ms);
    return pad2(d.getUTCDate()) + '.' + pad2(d.getUTCMonth() + 1) + '.' + d.getUTCFullYear() +
      ' ' + pad2(d.getUTCHours()) + ':' + pad2(d.getUTCMinutes());
  }

  // Parse "DD.MM.YYYY", "DD.MM.YYYY HH:MM" (also tolerates / or - separators
  // and a T between date and time). Returns a UTC epoch-ms, or null.
  function parseEU(s) {
    if (!s) return null;
    var m = String(s).trim().match(
      /^(\d{1,2})[.\/-](\d{1,2})[.\/-](\d{4})(?:[ T,]+(\d{1,2}):(\d{2}))?$/);
    if (!m) return null;
    var day = +m[1], mon = +m[2], yr = +m[3];
    var hr = m[4] != null ? +m[4] : 0, mi = m[5] != null ? +m[5] : 0;
    if (mon < 1 || mon > 12 || day < 1 || day > 31 || hr > 23 || mi > 59) return null;
    var ms = Date.UTC(yr, mon - 1, day, hr, mi, 0, 0);
    var d = new Date(ms); // reject overflow like 31.02.2026
    if (d.getUTCFullYear() !== yr || d.getUTCMonth() !== mon - 1 || d.getUTCDate() !== day) return null;
    return ms;
  }

  function fillBoxes(sinceMs, untilMs) {
    if (fromInput) { fromInput.value = fmtEU(sinceMs); markInvalid(fromInput, false); }
    if (toInput) { toInput.value = fmtEU(untilMs); markInvalid(toInput, false); }
  }

  // ── window filter ───────────────────────────────────────────────────

  function parseTs(s) {
    var t = Date.parse(s || '');
    return isNaN(t) ? null : t;
  }

  // Absolute [since, until] epoch-ms bounds. Presets are measured back from
  // the visitor's real clock; an explicit range uses the parsed boxes.
  function windowBounds(win) {
    var until, since, hours = null;
    if (win.from != null && win.to != null) {
      since = win.from; until = win.to;
    } else {
      hours = win.hours || (CFG.default_hours || 24);
      until = Date.now();
      since = until - hours * HOUR_MS;
    }
    return {
      since: since, until: until, hours: hours,
      label: fmtEU(since) + ' → ' + fmtEU(until) + ' UTC'
    };
  }

  function inWindow(book, bounds) {
    var out = [];
    (book.entries || []).forEach(function (e) {
      var ts = parseTs(e.discovered_at);
      if (ts !== null && ts >= bounds.since && ts <= bounds.until) out.push(e);
    });
    return out;
  }

  // ── grouping (mirrors build.py render_brief_sections) ───────────────

  function lensHit(e) {
    var lens = CFG.lens_regions || [];
    return (e.regions || []).some(function (r) { return lens.indexOf(r) >= 0; });
  }

  function prioRank(e) {
    var pr = CFG.priority_rank || {};
    var v = pr[e.priority];
    return typeof v === 'number' ? v : 2;
  }

  function sortEntries(list) {
    return list.slice().sort(function (a, b) {
      var la = lensHit(a) ? 0 : 1, lb = lensHit(b) ? 0 : 1;
      if (la !== lb) return la - lb;
      var pa = prioRank(a), pb = prioRank(b);
      if (pa !== pb) return pa - pb;
      var ta = a.discovered_at || '', tb = b.discovered_at || '';
      if (ta !== tb) return ta < tb ? 1 : -1; // newest first
      return (a.id || '') < (b.id || '') ? -1 : 1;
    });
  }

  function byRecency(list) {
    return list.slice().sort(function (a, b) {
      var ta = a.discovered_at || '', tb = b.discovered_at || '';
      if (ta !== tb) return ta < tb ? 1 : -1;
      return (a.id || '') < (b.id || '') ? -1 : 1;
    });
  }

  function sectionKeyOf(e) {
    if (e.update_of) return 'updates';
    if (e.deep_dive) return 'deep-dive';
    return (CFG.kind_section || {})[e.kind] || null;
  }

  function selectTldr(ops) {
    var recent = byRecency(ops);
    var crit = recent.filter(function (e) { return e.priority === 'critical'; });
    var high = recent.filter(function (e) { return e.priority === 'high'; });
    var picked = crit.concat(high);
    if (picked.length < 3) {
      var notable = recent.filter(function (e) { return e.priority === 'notable'; });
      picked = picked.concat(notable.slice(0, 3 - picked.length));
    }
    return picked.slice(0, 6);
  }

  // ── DOM builders (textContent only — no HTML string interpolation) ──

  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }

  // Migrated v2 headlines/summaries can carry literal Markdown emphasis
  // markers. We render text via textContent (no HTML), so just strip the
  // markers — this is cosmetic cleanup, not Markdown parsing.
  function plainText(s) {
    return String(s == null ? '' : s)
      .replace(/\*\*([^*]+)\*\*/g, '$1')
      .replace(/(^|\s)\*([^*\n]+)\*(?=[\s.,;:]|$)/g, '$1$2');
  }

  function emptyStub() {
    var p = el('p', 'muted section-empty');
    p.appendChild(el('em', null, CFG.empty_stub || 'No qualifying items in window — this section is intentionally left empty.'));
    return p;
  }

  function sectionShell(sec) {
    var section = el('section', 'brief-section');
    section.setAttribute('data-section', sec.key);
    section.id = sec.anchor;
    var h2 = el('h2');
    var a = el('a', 'section-anchor', sec.title);
    a.setAttribute('href', '#' + sec.anchor);
    h2.appendChild(a);
    section.appendChild(h2);
    var body = el('div', 'brief-section__body');
    body.id = sec.anchor + '-body';
    section.appendChild(body);
    return { section: section, body: body };
  }

  function tldrList(picked) {
    if (!picked.length) return emptyStub();
    var ul = el('ul');
    picked.forEach(function (e) {
      var li = el('li');
      var headline = plainText(e.headline || e.title || e.id).replace(/\.+$/, '');
      li.appendChild(el('strong', null, headline + '.'));
      li.appendChild(document.createTextNode(' ' + plainText(e.summary || '') + ' '));
      var a = el('a', null, '→');
      a.setAttribute('href', e.url);
      li.appendChild(a);
      ul.appendChild(li);
    });
    return ul;
  }

  function immediateActionCallout(e) {
    var ia = e.immediate_action || {};
    var aside = el('aside', 'callout callout--action immediate-action');
    aside.setAttribute('role', 'note');
    aside.setAttribute('data-entry-id', e.id);
    aside.appendChild(el('span', 'callout__label', 'Immediate action'));
    var body = el('div', 'callout__body');
    var p = el('p');
    p.appendChild(el('strong', null, ia.title || ''));
    p.appendChild(document.createTextNode(' — ' + (ia.action || '') + ' '));
    var a = el('a', null, plainText(e.headline || e.title || e.id) + ' →');
    a.setAttribute('href', e.url);
    p.appendChild(a);
    body.appendChild(p);
    if (ia.evidence_quote) {
      var fig = el('figure', 'entry-cite entry-cite--inline');
      fig.appendChild(el('p', 'entry-cite__quote', ia.evidence_quote));
      if (ia.evidence_publisher) {
        fig.appendChild(el('figcaption', 'entry-cite__attr', ia.evidence_publisher));
      }
      body.appendChild(fig);
    }
    aside.appendChild(body);
    return aside;
  }

  function actionItemsList(ops) {
    var rows = [];
    sortEntries(ops).forEach(function (e) {
      (e.actions || []).forEach(function (act) {
        if (typeof act !== 'string' || !act.trim()) return;
        rows.push({ entry: e, action: act.trim() });
      });
    });
    if (!rows.length) return emptyStub();
    var ul = el('ul', 'action-list');
    rows.forEach(function (row) {
      var li = el('li', 'action-list__item');
      li.setAttribute('data-entry-id', row.entry.id);
      var body = el('div', 'action-list__body', row.action + ' ');
      var a = el('a', 'action-list__ref',
        plainText(row.entry.headline || row.entry.title || row.entry.id) + ' →');
      a.setAttribute('href', row.entry.url);
      body.appendChild(a);
      li.appendChild(body);
      ul.appendChild(li);
    });
    return ul;
  }

  function runNote(run) {
    var div = el('div', 'run-note');
    div.setAttribute('data-run-id', run.run_id || '?');
    var h3 = el('h3', 'run-note__head');
    h3.appendChild(el('span', 'mono', run.run_id || '?'));
    var bits = [];
    if (run.model) bits.push(run.model);
    if (typeof run.window_hours === 'number') bits.push('window ' + run.window_hours + ' h');
    if (typeof run.entries_published === 'number') {
      bits.push(run.entries_published + (run.entries_published === 1 ? ' entry published' : ' entries published'));
    }
    if (bits.length) h3.appendChild(el('span', 'muted', ' — ' + bits.join(' · ')));
    div.appendChild(h3);
    var body = el('div', 'run-note__body');
    // run.html is server-rendered, sanitised HTML from our own build.
    body.insertAdjacentHTML('beforeend', run.html || '');
    div.appendChild(body);
    return div;
  }

  // ── chrome sync (meta banner counts + aside filter chips) ────────────

  function setAll(sel, text) {
    document.querySelectorAll(sel).forEach(function (n) { n.textContent = text; });
  }

  function uniqueSorted(list, key) {
    var set = {};
    list.forEach(function (e) {
      (e[key] || []).forEach(function (v) { set[v] = true; });
    });
    return Object.keys(set).sort();
  }

  function buildChip(facetAttr, v) {
    var b = el('button', 'filter-chip');
    b.type = 'button';
    b.setAttribute(facetAttr, v);
    b.setAttribute('aria-pressed', 'true');
    b.setAttribute('title', 'Toggle ' + v);
    b.textContent = v;
    return b;
  }

  function buildFilterGroup(label, facetAttr, values) {
    var d = el('details', 'filter-group');
    d.open = true;
    var s = el('summary', null, label + ' ');
    var count = el('span', 'filter-count');
    count.appendChild(el('span', 'muted', '(' + values.length + ')'));
    s.appendChild(count);
    d.appendChild(s);
    var row = el('div', 'filter-chip-row');
    values.forEach(function (v) { row.appendChild(buildChip(facetAttr, v)); });
    d.appendChild(row);
    return d;
  }

  // Rebuild the aside Tags/Regions chips so they match the entries the
  // new window actually shows, then hand filtering back to filter.min.js.
  function rebuildFilters(ops) {
    var tags = uniqueSorted(ops, 'tags');
    var regions = uniqueSorted(ops, 'regions');
    document.querySelectorAll('[data-filter="brief"] .toc-filters').forEach(function (host) {
      host.textContent = '';
      if (tags.length) host.appendChild(buildFilterGroup('Tags', 'data-filter-tag', tags));
      if (regions.length) host.appendChild(buildFilterGroup('Regions', 'data-filter-region', regions));
      var reset = el('button', 'filter-reset', 'Reset filters');
      reset.type = 'button';
      reset.setAttribute('data-action', 'clear-filters');
      reset.hidden = true;
      host.appendChild(reset);
      var status = el('p', 'filter-status');
      status.setAttribute('data-role', 'filter-status');
      status.hidden = true;
      host.appendChild(status);
    });
    if (window.CTIBrief && typeof window.CTIBrief.rebind === 'function') {
      window.CTIBrief.rebind();
    }
  }

  function updateMeta(ops, win) {
    setAll('[data-window-entries]', String(ops.length));
    setAll('[data-window-cves]', String(uniqueSorted(ops, 'cve_ids').length));
    var label = win.hours ? ('last ' + win.hours + ' h') : 'custom range';
    setAll('[data-window-label]', label);
  }

  // ── render ───────────────────────────────────────────────────────────

  function renderWindow(book, win) {
    var bounds = windowBounds(win);
    var root = document.getElementById('brief-sections');
    if (!root) return bounds;
    var entries = inWindow(book, bounds);
    var ops = entries.filter(function (e) { return (e.horizon || 'operational') === 'operational'; });
    var runs = (book.runs || []).filter(function (r) {
      var ts = parseTs(r.completed || r.started);
      return ts !== null && ts >= bounds.since && ts <= bounds.until;
    });

    // group
    var buckets = {};
    ops.forEach(function (e) {
      var k = sectionKeyOf(e);
      if (!k) return;
      (buckets[k] = buckets[k] || []).push(e);
    });
    Object.keys(buckets).forEach(function (k) { buckets[k] = sortEntries(buckets[k]); });

    var picked = selectTldr(ops);
    var criticals = sortEntries(ops.filter(function (e) { return e.priority === 'critical'; }));

    var frag = document.createDocumentFragment();
    (CFG.sections || []).forEach(function (sec) {
      var shell = sectionShell(sec);
      if (sec.key === 'tldr') {
        shell.body.appendChild(tldrList(picked));
        criticals.forEach(function (e) {
          if (e.immediate_action) shell.body.appendChild(immediateActionCallout(e));
        });
      } else if (sec.key === 'action-items') {
        shell.body.appendChild(actionItemsList(ops));
      } else if (sec.key === 'verification-notes') {
        if (runs.length) {
          runs.forEach(function (r) { shell.body.appendChild(runNote(r)); });
        } else {
          shell.body.appendChild(emptyStub());
        }
      } else {
        var list = buckets[sec.key] || [];
        if (list.length) {
          list.forEach(function (e) {
            // e.html is the server-rendered card — grouping + concatenation only.
            shell.body.insertAdjacentHTML('beforeend', e.html || '');
          });
        } else {
          shell.body.appendChild(emptyStub());
        }
      }
      frag.appendChild(shell.section);
    });

    root.textContent = '';
    root.appendChild(frag);

    var status = document.querySelector('[data-window-status]');
    if (status) {
      status.textContent = 'Showing ' + ops.length
        + (ops.length === 1 ? ' entry · ' : ' entries · ') + bounds.label;
    }

    updateMeta(ops, win);
    rebuildFilters(ops);
    return bounds;
  }
})();
