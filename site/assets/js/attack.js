/* attack.js — the /attack/ matrix's client-side entity overlap.
 *
 * The page is server-rendered: full enterprise matrix (store-wide
 * coverage heat) + per-technique evidence directory. This script adds the
 * ATT&CK-Navigator-style comparison: pick up to N entities (actors,
 * campaigns, malware, incidents, CVEs) from data/attack.json, shade each
 * matrix cell by which of the selection use the technique (or one of its
 * sub-techniques), switch between union / overlap≥2 / common-to-all
 * modes, and export the current selection as a Navigator layer JSON.
 *
 * Progressive enhancement: without JS the heat map, tooltips, anchors and
 * the evidence directory all keep working; the picker stays hidden.
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', init);

  function sitePrefix() {
    var m = document.querySelector('meta[name="cti-site-prefix"]');
    return (m && m.getAttribute('content')) || '';
  }

  function esc(s) {
    return String(s == null ? '' : s)
      .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;').replaceAll("'", '&#39;');
  }

  var MAX_SEL = 8;
  var data = null;          // data/attack.json payload
  var entByKey = {};        // key -> entity record
  var selected = [];        // ordered entity keys (color = index)
  var mode = 'any';         // any | overlap | all
  var cells = [];           // [{el, tid, subs[]}]

  function init() {
    var cfgEl = document.getElementById('attack-config');
    var picker = document.querySelector('[data-attack-picker]');
    if (!cfgEl || !picker) { wireAnchors(); return; }
    var cfg;
    try { cfg = JSON.parse(cfgEl.textContent); } catch (_) { wireAnchors(); return; }
    MAX_SEL = cfg.max_selection || 8;

    document.querySelectorAll('.atk-cell').forEach(function (el) {
      var subs = (el.getAttribute('data-subs') || '').split(',').filter(Boolean);
      cells.push({ el: el, tid: el.getAttribute('data-tid'), subs: subs });
    });
    wireAnchors();

    fetch(sitePrefix() + cfg.data_url, { credentials: 'omit' })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (payload) {
        data = payload;
        (data.entities || []).forEach(function (e) { entByKey[e.key] = e; });
        picker.hidden = false;
        wirePicker(picker);
        restoreFromUrl();
      })
      .catch(function () { /* picker stays hidden; static page remains fully usable */ });
  }

  /* Matrix cells link to the directory's <details> anchors — open the
     target row so a jump never lands on a collapsed element. */
  function wireAnchors() {
    function openHash() {
      var id = decodeURIComponent((location.hash || '').slice(1));
      if (!id) return;
      var el = document.getElementById(id);
      if (el && el.tagName === 'DETAILS') { el.open = true; }
    }
    window.addEventListener('hashchange', openHash);
    openHash();
  }

  // --- selection state -------------------------------------------------

  function techniqueSet(key) {
    var e = entByKey[key];
    return (e && e.techniques) || {};
  }

  /* Does entity `key` use `tid` or any of the cell's sub-techniques? */
  function hits(key, tid, subs) {
    var t = techniqueSet(key);
    if (t[tid]) return true;
    for (var i = 0; i < subs.length; i++) { if (t[subs[i]]) return true; }
    return false;
  }

  function threshold() {
    if (mode === 'all') return selected.length;
    if (mode === 'overlap') return Math.min(2, selected.length);
    return 1;
  }

  /* The single source of truth for "what the matrix shows": every
     parent-technique cell that passes the current mode, with the selected
     entities that hit it (the parent id or any of its sub-techniques).
     A technique listed under several tactics is one matrix technique drawn
     in several columns, so the map is keyed by technique id and both the
     status line and the Navigator export read from it. */
  function passingTechniques() {
    var out = {};
    if (!selected.length) return out;
    var min = threshold();
    cells.forEach(function (c) {
      if (out[c.tid]) return;
      var hitters = selected.filter(function (k) { return hits(k, c.tid, c.subs); });
      if (hitters.length && hitters.length >= min) out[c.tid] = { subs: c.subs, hitters: hitters };
    });
    return out;
  }

  function apply() {
    var passingCells = 0;
    var min = threshold();
    cells.forEach(function (c) {
      var hitters = selected.filter(function (k) { return hits(k, c.tid, c.subs); });
      var dots = c.el.querySelector('[data-dots]');
      if (!selected.length) {
        c.el.classList.remove('atk-cell--ol', 'atk-cell--dim');
        if (dots) dots.innerHTML = '';
        return;
      }
      var pass = hitters.length >= min && hitters.length > 0;
      if (pass) passingCells++;
      c.el.classList.toggle('atk-cell--ol', pass);
      c.el.classList.toggle('atk-cell--dim', !pass);
      if (dots) {
        dots.innerHTML = hitters.map(function (k) {
          var idx = selected.indexOf(k);
          var e = entByKey[k];
          return '<i class="sel-' + idx + '" title="' + esc(e ? e.title : k) + '"></i>';
        }).join('');
      }
    });
    document.querySelectorAll('[data-atk-legend-heat]').forEach(function (el) { el.hidden = !!selected.length; });
    document.querySelectorAll('[data-atk-legend-cmp]').forEach(function (el) { el.hidden = !selected.length; });
    renderStatus(Object.keys(passingTechniques()).length, passingCells);
    if (selected.length < MAX_SEL) note('');
    syncUrl();
  }

  function modeLabel() {
    var n = selected.length;
    if (n === 1) {
      var e = entByKey[selected[0]];
      return 'mapped to ' + (e ? e.title : selected[0]);
    }
    if (mode === 'all') return n === 2 ? 'common to both' : 'common to all ' + n;
    if (mode === 'overlap') return n === 2 ? 'shared by both' : 'shared by at least 2 of the ' + n;
    return n === 2 ? 'used by either' : 'used by at least one of the ' + n;
  }

  function renderStatus(techniques, cellCount) {
    var st = document.querySelector('[data-atk-status]');
    var exp = document.querySelector('[data-atk-export]');
    var clr = document.querySelector('[data-atk-clear]');
    if (exp) exp.hidden = !selected.length;
    if (clr) clr.hidden = !selected.length;
    if (!st) return;
    if (!selected.length) {
      st.textContent = 'No selection · cells show store-wide coverage heat.';
      return;
    }
    var text = selected.length + ' selected · ' + techniques + ' technique' +
      (techniques === 1 ? '' : 's') + ' ' + modeLabel();
    st.textContent = cellCount !== techniques
      ? text + ', in ' + cellCount + ' cells (a technique appears under each of its tactics; ' +
        'sub-techniques roll up into their parent).'
      : text + ' (sub-techniques roll up into their parent cell).';
  }

  /* One short, polite message line under the chips (selection limit). */
  function note(msg) {
    var el = document.querySelector('[data-atk-note]');
    if (!el) return;
    el.textContent = msg;
    el.hidden = !msg;
  }

  function fullMessage() {
    return 'The comparison holds at most ' + MAX_SEL + ' entities. Remove one to add another.';
  }

  // --- picker UI ---------------------------------------------------------

  function wirePicker(picker) {
    var input = picker.querySelector('#atk-q');
    var list = picker.querySelector('[data-atk-suggest]');
    picker.querySelectorAll('[data-atk-mode]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        mode = btn.getAttribute('data-atk-mode');
        picker.querySelectorAll('[data-atk-mode]').forEach(function (b) {
          b.classList.toggle('active', b === btn);
        });
        apply();
      });
    });
    var clr = picker.querySelector('[data-atk-clear]');
    if (clr) clr.addEventListener('click', function () { selected = []; renderChips(); apply(); });
    var exp = picker.querySelector('[data-atk-export]');
    if (exp) exp.addEventListener('click', exportLayer);

    function close() { list.hidden = true; list.innerHTML = ''; }
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      if (q.length < 2) { close(); return; }
      if (selected.length >= MAX_SEL) { close(); note(fullMessage()); return; }
      var out = [];
      for (var i = 0; i < data.entities.length && out.length < 12; i++) {
        var e = data.entities[i];
        if (selected.indexOf(e.key) !== -1) continue;
        var hay = (e.title + ' ' + e.key).toLowerCase();
        if (hay.indexOf(q) !== -1) out.push(e);
      }
      if (!out.length) { close(); return; }
      list.innerHTML = out.map(function (e) {
        return '<li><button type="button" data-atk-add="' + esc(e.key) + '">' +
          '<b>' + esc(e.title) + '</b> <span class="mono">' + esc(e.type) + '</span>' +
          '<span class="muted">' + Object.keys(e.techniques).length + ' techniques</span>' +
          '</button></li>';
      }).join('');
      list.hidden = false;
    });
    list.addEventListener('click', function (ev) {
      var btn = ev.target.closest('[data-atk-add]');
      if (!btn) return;
      add(btn.getAttribute('data-atk-add'));
      input.value = '';
      close();
      input.focus();
    });
    input.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape') close();
      if (ev.key === 'Enter') {
        ev.preventDefault();
        var first = list.querySelector('[data-atk-add]');
        if (first) { add(first.getAttribute('data-atk-add')); input.value = ''; close(); }
      }
    });
    document.addEventListener('click', function (ev) {
      if (!picker.contains(ev.target)) close();
    });
  }

  function add(key) {
    if (!entByKey[key] || selected.indexOf(key) !== -1) return;
    if (selected.length >= MAX_SEL) { note(fullMessage()); return; }
    selected.push(key);
    renderChips();
    apply();
  }

  function remove(key) {
    selected = selected.filter(function (k) { return k !== key; });
    renderChips();
    apply();
  }

  function renderChips() {
    var box = document.querySelector('[data-atk-chips]');
    if (!box) return;
    box.innerHTML = selected.map(function (k, idx) {
      var e = entByKey[k];
      return '<span class="atk-chip sel-' + idx + '">' +
        '<a href="' + sitePrefix() + 'entities/' + encodeURIComponent(k) + '/">' +
        esc(e ? e.title : k) + '</a>' +
        '<span class="mono">' + Object.keys(techniqueSet(k)).length + '</span>' +
        '<button type="button" aria-label="Remove ' + esc(e ? e.title : k) +
        '" data-atk-remove="' + esc(k) + '">✕</button></span>';
    }).join('');
    box.querySelectorAll('[data-atk-remove]').forEach(function (btn) {
      btn.addEventListener('click', function () { remove(btn.getAttribute('data-atk-remove')); });
    });
  }

  // --- URL state ---------------------------------------------------------

  function syncUrl() {
    var p = new URLSearchParams(location.search);
    if (selected.length) p.set('sel', selected.join(',')); else p.delete('sel');
    if (mode !== 'any') p.set('mode', mode); else p.delete('mode');
    var qs = p.toString();
    history.replaceState(null, '', location.pathname + (qs ? '?' + qs : '') + location.hash);
  }

  function restoreFromUrl() {
    var p = new URLSearchParams(location.search);
    var m = p.get('mode');
    if (m === 'overlap' || m === 'all') {
      mode = m;
      document.querySelectorAll('[data-atk-mode]').forEach(function (b) {
        b.classList.toggle('active', b.getAttribute('data-atk-mode') === m);
      });
    }
    var wanted = [];
    (p.get('sel') || '').split(',').filter(Boolean).forEach(function (k) {
      if (entByKey[k] && wanted.indexOf(k) === -1) wanted.push(k);
    });
    selected = wanted.slice(0, MAX_SEL);
    renderChips();
    apply();
    if (wanted.length > MAX_SEL) {
      note('The link named ' + wanted.length + ' entities; the comparison holds at most ' +
        MAX_SEL + ', so the first ' + MAX_SEL + ' are shown.');
    }
  }

  // --- Navigator layer export ---------------------------------------------

  /* The layer carries exactly the techniques the matrix highlights: one
     record per passing parent-technique cell, scored by how many selected
     entities hit that cell (the parent or one of its sub-techniques, the
     same roll-up the matrix applies). The comment names each entity with
     the exact technique ids it maps, so a sub-technique-only overlap stays
     traceable after import. */
  function exportLayer() {
    if (!selected.length || !data) return;
    var passing = passingTechniques();
    var techniques = Object.keys(passing).sort().map(function (tid) {
      var rec = passing[tid];
      var parts = rec.hitters.map(function (k) {
        var e = entByKey[k];
        var t = techniqueSet(k);
        var ids = [tid].concat(rec.subs).filter(function (id) { return t[id]; });
        return (e ? e.title : k) + ' (' + ids.join(', ') + ')';
      });
      return { techniqueID: tid, score: rec.hitters.length, comment: parts.join('; ') };
    });
    var titles = selected.map(function (k) { return entByKey[k] ? entByKey[k].title : k; });
    var layer = {
      name: 'Overlap: ' + titles.join(' + '),
      versions: {
        attack: String(data.attack_version || '').split('.')[0],
        layer: '4.5',
        navigator: '5.1.0'
      },
      domain: 'enterprise-attack',
      description: 'Entity TTP overlap (' + techniques.length + ' techniques ' + modeLabel() +
        ') exported from the coverage matrix. Score = number of selected entities mapping ' +
        'the technique or one of its sub-techniques (sub-techniques roll up into their ' +
        'parent, as on the matrix). Pinned dataset: ATT&CK v' + data.attack_version + '.',
      sorting: 3,
      layout: { layout: 'side', showID: true, showName: true },
      techniques: techniques,
      gradient: { colors: ['#ffe766', '#ff6666'], minValue: 0, maxValue: selected.length },
      metadata: [
        { name: 'entities', value: selected.join(', ') },
        { name: 'mode', value: mode },
        { name: 'attack_version', value: String(data.attack_version || '') }
      ]
    };
    var blob = new Blob([JSON.stringify(layer, null, 1)], { type: 'application/json' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'attack-layer-overlap.json';
    document.body.appendChild(a);
    a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
})();
