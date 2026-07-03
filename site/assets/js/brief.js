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

  function init() {
    var root = document.getElementById('brief-sections');
    var controls = document.querySelector('[data-brief-controls]');
    CFG = readConfig();
    if (!root || !controls || !CFG) return;

    var chips = controls.querySelectorAll('[data-window-hours]');
    var sinceInput = controls.querySelector('[data-window-since]');

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var hours = parseInt(chip.getAttribute('data-window-hours'), 10);
        if (!(hours > 0)) return;
        if (sinceInput) sinceInput.value = '';
        setActiveChip(chips, chip);
        applyWindow({ hours: hours });
      });
    });

    if (sinceInput) {
      sinceInput.addEventListener('change', function () {
        var v = sinceInput.value; // YYYY-MM-DD from the date input
        if (!/^\d{4}-\d{2}-\d{2}$/.test(v)) return;
        setActiveChip(chips, null);
        applyWindow({ since: v });
      });
    }

    // ?hours=N / ?since=YYYY-MM-DD on load.
    var params = new URLSearchParams(window.location.search);
    var pHours = parseInt(params.get('hours') || '', 10);
    var pSince = params.get('since') || '';
    if (/^\d{4}-\d{2}-\d{2}$/.test(pSince)) {
      if (sinceInput) sinceInput.value = pSince;
      setActiveChip(chips, null);
      applyWindow({ since: pSince }, { replaceUrl: false });
    } else if (pHours > 0 && pHours !== CFG.default_hours) {
      chips.forEach(function (c) {
        if (parseInt(c.getAttribute('data-window-hours'), 10) === pHours) {
          setActiveChip(chips, c);
        }
      });
      applyWindow({ hours: pHours }, { replaceUrl: false });
    }
  }

  function setActiveChip(chips, active) {
    chips.forEach(function (c) { c.classList.toggle('active', c === active); });
  }

  function applyWindow(win, opts) {
    opts = opts || {};
    ensureBook().then(function (book) {
      renderWindow(book, win);
      if (opts.replaceUrl !== false && window.history && history.replaceState) {
        var q = win.since ? ('?since=' + encodeURIComponent(win.since))
                          : ('?hours=' + win.hours);
        history.replaceState(null, '', q);
      }
    }).catch(function () {
      var status = document.querySelector('[data-window-status]');
      if (status) status.textContent = 'could not load the entry book — showing the default window';
    });
  }

  // ── window filter ───────────────────────────────────────────────────

  function parseTs(s) {
    var t = Date.parse(s || '');
    return isNaN(t) ? null : t;
  }

  function windowBounds(win) {
    if (win.since) {
      return { since: Date.parse(win.since + 'T00:00:00Z'), label: 'since ' + win.since + ' (UTC)' };
    }
    return {
      since: Date.now() - win.hours * 3600 * 1000,
      label: 'from the last ' + win.hours + ' h'
    };
  }

  function inWindow(book, bounds) {
    var out = [];
    (book.entries || []).forEach(function (e) {
      var ts = parseTs(e.discovered_at);
      if (ts !== null && ts >= bounds.since) out.push(e);
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
      var headline = (e.headline || e.title || e.id).replace(/\.+$/, '');
      li.appendChild(el('strong', null, headline + '.'));
      li.appendChild(document.createTextNode(' ' + (e.summary || '') + ' '));
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
    var a = el('a', null, (e.headline || e.title || e.id) + ' →');
    a.setAttribute('href', e.url);
    p.appendChild(a);
    body.appendChild(p);
    if (ia.evidence_quote) {
      var bq = el('blockquote', 'entry-evidence');
      var qp = el('p', null, '“' + ia.evidence_quote + '”');
      if (ia.evidence_publisher) {
        qp.appendChild(document.createTextNode(' '));
        qp.appendChild(el('cite', null, '— ' + ia.evidence_publisher));
      }
      bq.appendChild(qp);
      body.appendChild(bq);
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
        (row.entry.headline || row.entry.title || row.entry.id) + ' →');
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

  // ── render ───────────────────────────────────────────────────────────

  function renderWindow(book, win) {
    var root = document.getElementById('brief-sections');
    if (!root) return;
    var bounds = windowBounds(win);
    var entries = inWindow(book, bounds);
    var ops = entries.filter(function (e) { return (e.horizon || 'operational') === 'operational'; });
    var runs = (book.runs || []).filter(function (r) {
      var ts = parseTs(r.completed || r.started);
      return ts !== null && ts >= bounds.since;
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
      status.textContent = 'showing ' + ops.length
        + (ops.length === 1 ? ' entry ' : ' entries ') + bounds.label;
    }
  }
})();
