/* brief.js — the live rolling brief's client-side windowing.
 *
 * The /brief/ page is server-rendered for the default 24 h window as a
 * run-grouped timeline. This script re-renders that timeline from
 * data/briefbook.json when the reader changes the window (the range
 * <select> or the "Load older findings" button), and re-applies the
 * active chip filters (kept in sync via the `cti:filterchange` event
 * dispatched by app.js). It mirrors the server markup exactly
 * (render_timeline_item / render_run_divider in site/build.py).
 *
 * Progressive enhancement: without JS the page shows the server-rendered
 * 24 h timeline and every link still works.
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', init);

  function sitePrefix() {
    var m = document.querySelector('meta[name="cti-site-prefix"]');
    return (m && m.getAttribute('content')) || '';
  }

  var MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  var PRI_LABEL = { critical: 'CRITICAL', high: 'HIGH', notable: 'NOTABLE', routine: 'ROUTINE' };
  var PRI_CLASS = { critical: 'crit', high: 'pri' };
  var PRI_DOT = { critical: 'var(--crit)', high: 'var(--accent)' };

  function pad(n) { return n < 10 ? '0' + n : '' + n; }
  function stamp(d) { return pad(d.getUTCDate()) + ' ' + MONTHS[d.getUTCMonth()] + ' ' + pad(d.getUTCHours()) + ':' + pad(d.getUTCMinutes()) + 'Z'; }
  function euro(d) { return pad(d.getUTCDate()) + '.' + pad(d.getUTCMonth() + 1) + '.' + d.getUTCFullYear() + ' ' + pad(d.getUTCHours()) + ':' + pad(d.getUTCMinutes()); }
  function esc(s) {
    return String(s == null ? '' : s)
      .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;').replaceAll("'", '&#39;');
  }

  function init() {
    var cfgEl = document.getElementById('brief-config');
    var container = document.querySelector('[data-brief-timeline]');
    if (!cfgEl || !container) return;
    var cfg;
    try { cfg = JSON.parse(cfgEl.textContent); } catch (_) { return; }

    var refTs = new Date(cfg.reference_ts);
    var defaultHours = cfg.default_hours || 24;
    var hours = defaultHours;
    var filterSets = { priority: [], kind: [], tag: [], region: [] };
    var data = null;

    var select = document.querySelector('[data-window-select]');
    var more = document.querySelector('[data-window-more]');
    var endMsg = document.querySelector('[data-window-end]');
    var fromEl = document.querySelector('[data-window-from]');
    var toEl = document.querySelector('[data-window-to]');
    var statusEl = document.querySelector('[data-window-status]');
    var countEl = document.querySelector('[data-window-count]');

    if (toEl) toEl.textContent = euro(refTs);

    function passesFilter(e) {
      var s = filterSets;
      if (s.priority.length && s.priority.indexOf(e.priority) < 0) return false;
      if (s.kind.length && s.kind.indexOf(e.kind) < 0) return false;
      if (s.tag.length && !s.tag.some(function (t) { return (e.tags || []).indexOf(t) >= 0; })) return false;
      if (s.region.length && !s.region.some(function (r) { return (e.regions || []).indexOf(r) >= 0; })) return false;
      return true;
    }

    function relUrl(e) {
      // briefbook url is prefixed for the /brief/ page ("../entries/…/"); strip
      // that and re-apply the live sitePrefix so it resolves anywhere.
      return (e.url || '').replace(/^(\.\.\/)+/, '');
    }

    function runItem(e, isNew) {
      var badges = ['<span class="b ' + (PRI_CLASS[e.priority] || '') + '">' + esc(PRI_LABEL[e.priority] || String(e.priority).toUpperCase()) + '</span>'];
      if (e.cve_label) badges.push('<span class="b cve">' + esc(e.cve_label) + '</span>');
      if (e.exploited) badges.push('<span class="b exp">exploited</span>');
      if (e.update_of) badges.push('<span class="b upd">update</span>');
      var d = e.discovered_at ? new Date(e.discovered_at) : refTs;
      var flag = e.update_of ? '↻ UPD' : (isNew ? 'NEW' : '');
      var flagStyle = e.update_of ? 'color:var(--warn)' : (isNew ? 'color:var(--ok)' : '');
      var prov = ['<div class="prov">'];
      if (e.kind) prov.push('<span>' + esc(e.kind) + '</span>');
      if (e.cve_label) prov.push('<span style="color:var(--info)">' + esc(e.cve_label) + '</span>');
      prov.push('<span>' + esc(stamp(d)) + '</span>');
      if (e.source_count) prov.push('<span>' + e.source_count + ' source' + (e.source_count === 1 ? '' : 's') + '</span>');
      prov.push('<span class="' + esc(e.verification_class || 'p-warn') + '">' + esc(e.verification_label || '') + '</span>');
      prov.push('<span class="refs">open ↗</span></div>');
      return '<div class="tl-item">'
        + '<div class="tl-rail"><span class="tl-node" style="background:' + (PRI_DOT[e.priority] || 'var(--text-muted)') + '"></span>'
        + '<span class="time">' + esc(stamp(d)) + '</span><span class="flag" style="' + flagStyle + '">' + esc(flag) + '</span></div>'
        + '<a class="tl-body" href="' + esc(sitePrefix() + relUrl(e)) + '">'
        + '<div class="badges">' + badges.join('') + '</div>'
        + '<h3>' + esc(e.title || e.id) + '</h3><p>' + esc(e.summary || e.headline || '') + '</p>'
        + prov.join('') + '</a></div>';
    }

    function runDivider(label, gap, count) {
      var n = count + ' finding' + (count === 1 ? '' : 's');
      var g = (gap ? gap + ' · ' : '') + n;
      return '<div class="tl-run"><div class="tl-rail rail-e"><span class="runnode"></span></div>'
        + '<div class="run-h"><span class="rl">' + esc(label) + '</span><span class="rg">· run · ' + esc(g) + '</span></div></div>';
    }

    function render() {
      if (!data) return;
      var since = new Date(refTs.getTime() - hours * 3600000);
      var runsById = {};
      (data.runs || []).forEach(function (r) { if (r.run_id) runsById[r.run_id] = r; });

      var ops = (data.entries || []).filter(function (e) {
        if ((e.horizon || 'operational') !== 'operational') return false;
        var d = e.discovered_at ? new Date(e.discovered_at) : null;
        if (!d || d < since || d > refTs) return false;
        return passesFilter(e);
      });
      ops.sort(function (a, b) {
        var da = a.discovered_at || '', db = b.discovered_at || '';
        if (da !== db) return da < db ? 1 : -1;
        return a.id < b.id ? 1 : -1;
      });

      // has-older ignores active filters (it's a window boundary, not a filter).
      var hasOlder = (data.entries || []).some(function (e) {
        if ((e.horizon || 'operational') !== 'operational') return false;
        var d = e.discovered_at ? new Date(e.discovered_at) : null;
        return d && d < since;
      });

      var groups = [];
      ops.forEach(function (e) {
        var rid = e.run_id || '';
        if (groups.length && groups[groups.length - 1].rid === rid) groups[groups.length - 1].items.push(e);
        else groups.push({ rid: rid, items: [e] });
      });

      var activeCount = filterSets.priority.length + filterSets.kind.length + filterSets.tag.length + filterSets.region.length;
      var html = '';
      if (!ops.length) {
        html = '<div class="section-empty" style="padding:40px 0 0;margin-left:96px;">'
          + 'No findings in this window' + (activeCount ? ' matching the active filters' : '')
          + '. Load older findings to reach further back.</div>';
      } else {
        var prevTs = null;
        groups.forEach(function (g, gi) {
          var r = runsById[g.rid];
          var ts = r && (r.completed || r.started) ? new Date(r.completed || r.started)
            : (g.items[0].discovered_at ? new Date(g.items[0].discovered_at) : refTs);
          var gap = '';
          if (prevTs) {
            var dh = (prevTs.getTime() - ts.getTime()) / 3600000;
            if (dh >= 1) gap = 'gap ' + Math.round(dh) + 'h';
          }
          prevTs = ts;
          html += runDivider(stamp(ts), gap, g.items.length);
          g.items.forEach(function (e) { html += runItem(e, gi === 0); });
        });
      }
      container.innerHTML = html;

      if (fromEl) fromEl.textContent = euro(since);
      if (statusEl) statusEl.textContent = 'last ' + hours + 'h';
      if (countEl) countEl.textContent = String(ops.length);
      if (endMsg) endMsg.hidden = hasOlder;
      if (more) more.hidden = !hasOlder;
    }

    function load() {
      fetch(sitePrefix() + (cfg.briefbook_url || 'data/briefbook.json'))
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (j) { if (j) { data = j; render(); } })
        .catch(function () { /* keep the server-rendered timeline */ });
    }

    if (select) select.addEventListener('change', function () {
      hours = parseInt(select.value, 10) || defaultHours;
      render();
    });
    if (more) more.addEventListener('click', function () {
      hours += 24;
      if (select) {
        var has = Array.prototype.some.call(select.options, function (o) { return parseInt(o.value, 10) === hours; });
        if (has) select.value = String(hours);
      }
      render();
    });

    document.addEventListener('cti:filterchange', function (e) {
      if (e.detail && e.detail.sets) { filterSets = e.detail.sets; if (data) render(); }
    });

    load();
  }
})();
