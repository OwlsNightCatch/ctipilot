/* graph.js — the /graph/ interactive threat graph.
 *
 * Renders data/graph.json (all canonical entities + covered CVEs +
 * mapped ATT&CK techniques; curated typed edges + derived edges) as a
 * force-directed canvas an analyst can investigate:
 *
 *   - pan / zoom / drag-to-pin nodes
 *   - node-type layers (entities / CVEs / techniques) and edge-class
 *     toggles (curated / derived)
 *   - search with jump-to-node
 *   - click → detail panel (summary line, typed relations with their
 *     source entries, direct neighbours, page links)
 *   - shift-click a second node → shortest-path trace between the two
 *   - double-click → isolate a node's neighbourhood (depth 2)
 *   - ?focus=<id> deep link (entity pages link here)
 *
 * Progressive enhancement: without JS the page's most-connected
 * directory and the per-entity relationship lists carry the same data.
 * Self-contained (strict CSP): no external libraries.
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

  // ---- state ----------------------------------------------------------
  var data = null;
  var nodes = [];            // render nodes: {id,kind,type,label,...,x,y,vx,vy,deg,pinned}
  var nodeById = {};
  var edges = [];            // render edges: {s,t,kind,...} with node refs
  var adj = {};              // id -> [{other, edge}]
  var layers = { entity: true, cve: true, technique: false };
  var edgeClasses = { relation: true, derived: true };
  var selected = null;       // node id
  var pathEnd = null;        // second node id (shift-click)
  var pathIds = null;        // Set of ids on the traced path
  var isolated = null;       // Set of visible ids when isolating, else null
  var hovered = null;
  var view = { x: 0, y: 0, k: 1 };   // pan/zoom transform
  var canvas, ctx, panel, statusEl, shell;
  var dpr = Math.max(1, window.devicePixelRatio || 1);
  var simTimer = null, alpha = 0;
  var colors = {};

  var TYPE_COLOR_VARS = {
    actor: '--g-actor', campaign: '--g-campaign', malware: '--g-malware',
    tool: '--g-tool', incident: '--g-incident', report: '--g-report',
    trend: '--g-trend', policy: '--g-policy', cve: '--g-cve',
    technique: '--g-technique'
  };
  var TYPE_FALLBACK = {
    actor: '#e5534b', campaign: '#e09b13', malware: '#b83db8', tool: '#9a6ee2',
    incident: '#2f81f7', report: '#6e7781', trend: '#1a7f37', policy: '#0d7d8c',
    cve: '#cf222e', technique: '#57606a'
  };

  function init() {
    shell = document.querySelector('[data-graph-shell]');
    var cfgEl = document.getElementById('graph-config');
    if (!shell || !cfgEl) return;
    var cfg;
    try { cfg = JSON.parse(cfgEl.textContent); } catch (e) { return; }
    canvas = shell.querySelector('[data-graph-canvas]');
    panel = shell.querySelector('[data-graph-panel]');
    statusEl = shell.querySelector('[data-graph-status]');
    if (!canvas || !canvas.getContext) return;
    ctx = canvas.getContext('2d');
    readColors();

    fetch(sitePrefix() + cfg.data_url, { credentials: 'omit' })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (payload) { data = payload; build(); shell.hidden = false; resize(); layout(true); wire(); restoreFromUrl(); })
      .catch(function (err) {
        if (statusEl) statusEl.textContent = 'Could not load the graph dataset (' + err.message + ') — the directory below still works.';
        shell.hidden = false;
      });
  }

  function readColors() {
    var cs = getComputedStyle(document.documentElement);
    Object.keys(TYPE_COLOR_VARS).forEach(function (t) {
      var v = cs.getPropertyValue(TYPE_COLOR_VARS[t]).trim();
      colors[t] = v || TYPE_FALLBACK[t];
    });
    colors.text = (cs.getPropertyValue('--text') || '').trim() || '#333';
    colors.muted = (cs.getPropertyValue('--text-muted') || '').trim() || '#888';
    colors.edge = (cs.getPropertyValue('--border') || '').trim() || '#c8c8c8';
    colors.bg = (cs.getPropertyValue('--bg') || '').trim() || '#fff';
    colors.accent = (cs.getPropertyValue('--accent') || '').trim() || '#2f81f7';
  }

  function build() {
    nodes = (data.nodes || []).map(function (n) {
      return Object.assign({}, n, {
        x: 0, y: 0, vx: 0, vy: 0, deg: 0, pinned: false
      });
    });
    nodeById = {};
    nodes.forEach(function (n) { nodeById[n.id] = n; });
    edges = [];
    adj = {};
    (data.edges || []).forEach(function (e) {
      var s = nodeById[e.source], t = nodeById[e.target];
      if (!s || !t) return;
      var re = Object.assign({}, e, { s: s, t: t });
      edges.push(re);
      (adj[s.id] = adj[s.id] || []).push({ other: t, edge: re });
      (adj[t.id] = adj[t.id] || []).push({ other: s, edge: re });
      if (e.kind !== 'technique') { s.deg++; t.deg++; }
    });
    // deterministic initial spiral placement (stable across loads)
    var golden = Math.PI * (3 - Math.sqrt(5));
    nodes
      .slice()
      .sort(function (a, b) { return b.deg - a.deg || (a.id < b.id ? -1 : 1); })
      .forEach(function (n, i) {
        var r = 40 * Math.sqrt(i + 1);
        n.x = r * Math.cos(i * golden);
        n.y = r * Math.sin(i * golden);
      });
  }

  // ---- visibility -----------------------------------------------------
  function nodeVisible(n) {
    if (!layers[n.kind]) return false;
    if (isolated && !isolated.has(n.id)) return false;
    return true;
  }
  function edgeVisible(e) {
    if (!nodeVisible(e.s) || !nodeVisible(e.t)) return false;
    if (e.kind === 'relation') return edgeClasses.relation;
    return edgeClasses.derived;
  }
  function visibleNodes() { return nodes.filter(nodeVisible); }
  function visibleEdges() { return edges.filter(edgeVisible); }

  // ---- force layout ---------------------------------------------------
  function layout(restart) {
    if (restart) alpha = 1;
    if (simTimer) return;
    var step = function () {
      var vn = visibleNodes(), ve = visibleEdges();
      tick(vn, ve);
      draw();
      alpha *= 0.985;
      if (alpha > 0.02) { simTimer = requestAnimationFrame(step); }
      else { simTimer = null; draw(); }
    };
    simTimer = requestAnimationFrame(step);
  }

  function tick(vn, ve) {
    var i, j, n, m, dx, dy, d2, d, f;
    // repulsion on a coarse grid (Barnes-Hut-ish bucketing)
    var CELL = 160;
    var grid = {};
    for (i = 0; i < vn.length; i++) {
      n = vn[i];
      var gk = Math.floor(n.x / CELL) + ':' + Math.floor(n.y / CELL);
      (grid[gk] = grid[gk] || []).push(n);
    }
    var K = 2600 * alpha;
    for (i = 0; i < vn.length; i++) {
      n = vn[i];
      var gx = Math.floor(n.x / CELL), gy = Math.floor(n.y / CELL);
      for (var ox = -1; ox <= 1; ox++) {
        for (var oy = -1; oy <= 1; oy++) {
          var bucket = grid[(gx + ox) + ':' + (gy + oy)];
          if (!bucket) continue;
          for (j = 0; j < bucket.length; j++) {
            m = bucket[j];
            if (m === n) continue;
            dx = n.x - m.x; dy = n.y - m.y;
            d2 = dx * dx + dy * dy;
            if (d2 < 1) { d2 = 1; dx = (Math.random() - 0.5); dy = (Math.random() - 0.5); }
            if (d2 > CELL * CELL * 2.25) continue;
            f = K / d2;
            n.vx += dx * f; n.vy += dy * f;
          }
        }
      }
      // gravity toward origin
      n.vx -= n.x * 0.012 * alpha;
      n.vy -= n.y * 0.012 * alpha;
    }
    // springs
    var LINK = 120;
    for (i = 0; i < ve.length; i++) {
      var e = ve[i];
      dx = e.t.x - e.s.x; dy = e.t.y - e.s.y;
      d = Math.sqrt(dx * dx + dy * dy) || 1;
      var target = e.kind === 'relation' ? LINK * 0.8 : LINK * 1.25;
      f = (d - target) / d * 0.06 * alpha * (e.kind === 'relation' ? 2 : 1);
      var fx = dx * f, fy = dy * f;
      e.s.vx += fx; e.s.vy += fy;
      e.t.vx -= fx; e.t.vy -= fy;
    }
    for (i = 0; i < vn.length; i++) {
      n = vn[i];
      if (n.pinned || n === dragNode) { n.vx = 0; n.vy = 0; continue; }
      n.x += Math.max(-30, Math.min(30, n.vx));
      n.y += Math.max(-30, Math.min(30, n.vy));
      n.vx *= 0.6; n.vy *= 0.6;
    }
  }

  // ---- rendering ------------------------------------------------------
  function nodeRadius(n) {
    var base = n.kind === 'technique' ? 3.5 : 4.5;
    return base + Math.min(14, Math.sqrt((n.entries || 0) + n.deg) * 1.6);
  }

  function draw() {
    if (!ctx) return;
    var w = canvas.width / dpr, h = canvas.height / dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    ctx.clearRect(0, 0, w, h);
    ctx.translate(w / 2 + view.x, h / 2 + view.y);
    ctx.scale(view.k, view.k);

    var focusSet = null;
    if (hovered || selected) {
      focusSet = new Set();
      var fid = hovered || selected;
      focusSet.add(fid);
      (adj[fid] || []).forEach(function (a) { if (edgeVisible(a.edge)) focusSet.add(a.other.id); });
      if (pathIds) pathIds.forEach(function (id) { focusSet.add(id); });
    }

    var ve = visibleEdges();
    for (var i = 0; i < ve.length; i++) {
      var e = ve[i];
      var onPath = pathIds && pathIds.has(e.s.id) && pathIds.has(e.t.id) &&
        pathEdgeSet && pathEdgeSet.has(e);
      var dimmed = focusSet && !onPath &&
        !(focusSet.has(e.s.id) && focusSet.has(e.t.id));
      ctx.beginPath();
      ctx.moveTo(e.s.x, e.s.y);
      ctx.lineTo(e.t.x, e.t.y);
      if (e.kind === 'relation') {
        ctx.setLineDash([]);
        ctx.strokeStyle = onPath ? colors.accent : colors.muted;
        ctx.lineWidth = (onPath ? 2.4 : 1.4) / view.k;
      } else {
        ctx.setLineDash([4 / view.k, 4 / view.k]);
        ctx.strokeStyle = onPath ? colors.accent : colors.edge;
        ctx.lineWidth = (onPath ? 2.2 : Math.min(2.5, 0.5 + (e.count || 1) * 0.25)) / view.k;
      }
      ctx.globalAlpha = dimmed ? 0.08 : (e.kind === 'relation' ? 0.85 : 0.5);
      ctx.stroke();
      ctx.setLineDash([]);
      // arrowhead on directed curated edges
      if (e.kind === 'relation' && !e.symmetric && !dimmed && view.k > 0.35) {
        drawArrow(e, onPath ? colors.accent : colors.muted);
      }
    }
    ctx.globalAlpha = 1;

    var vn = visibleNodes();
    for (i = 0; i < vn.length; i++) {
      var n = vn[i];
      var r = nodeRadius(n);
      var dim = focusSet && !focusSet.has(n.id);
      ctx.beginPath();
      ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
      ctx.fillStyle = colors[n.type] || colors.muted;
      ctx.globalAlpha = dim ? 0.15 : 1;
      ctx.fill();
      if (n.kind === 'cve' && n.exploited) {
        ctx.beginPath();
        ctx.arc(n.x, n.y, r + 2.2 / view.k, 0, Math.PI * 2);
        ctx.strokeStyle = colors.cve;
        ctx.lineWidth = 1.6 / view.k;
        ctx.stroke();
      }
      if (n.id === selected || n.id === pathEnd) {
        ctx.beginPath();
        ctx.arc(n.x, n.y, r + 3.5 / view.k, 0, Math.PI * 2);
        ctx.strokeStyle = colors.accent;
        ctx.lineWidth = 2 / view.k;
        ctx.stroke();
      }
      if (n.pinned && !dim) {
        ctx.beginPath();
        ctx.arc(n.x, n.y, 1.6 / view.k, 0, Math.PI * 2);
        ctx.fillStyle = colors.bg;
        ctx.fill();
      }
    }
    ctx.globalAlpha = 1;

    // labels: hovered/selected/path always; high-degree when zoomed in
    ctx.font = (11 / view.k) + 'px ui-monospace, SFMono-Regular, Menlo, monospace';
    ctx.textBaseline = 'middle';
    for (i = 0; i < vn.length; i++) {
      n = vn[i];
      var show = n.id === hovered || n.id === selected || n.id === pathEnd ||
        (pathIds && pathIds.has(n.id)) ||
        (view.k > 1.4) || (n.deg >= 8 && view.k > 0.5) ||
        (isolated && isolated.size <= 40);
      if (!show) continue;
      if (focusSet && !focusSet.has(n.id)) continue;
      var label = n.label || n.id;
      if (label.length > 34) label = label.slice(0, 32) + '…';
      var x = n.x + nodeRadius(n) + 4 / view.k;
      ctx.lineWidth = 3 / view.k;
      ctx.strokeStyle = colors.bg;
      ctx.strokeText(label, x, n.y);
      ctx.fillStyle = colors.text;
      ctx.fillText(label, x, n.y);
    }
  }

  function drawArrow(e, color) {
    var dx = e.t.x - e.s.x, dy = e.t.y - e.s.y;
    var d = Math.sqrt(dx * dx + dy * dy) || 1;
    var ux = dx / d, uy = dy / d;
    var tipX = e.t.x - ux * (nodeRadius(e.t) + 2), tipY = e.t.y - uy * (nodeRadius(e.t) + 2);
    var size = 6 / view.k;
    ctx.beginPath();
    ctx.moveTo(tipX, tipY);
    ctx.lineTo(tipX - ux * size - uy * size * 0.5, tipY - uy * size + ux * size * 0.5);
    ctx.lineTo(tipX - ux * size + uy * size * 0.5, tipY - uy * size - ux * size * 0.5);
    ctx.closePath();
    ctx.fillStyle = color;
    ctx.fill();
  }

  // ---- hit testing / coordinates --------------------------------------
  function toWorld(px, py) {
    var w = canvas.width / dpr, h = canvas.height / dpr;
    return {
      x: (px - w / 2 - view.x) / view.k,
      y: (py - h / 2 - view.y) / view.k
    };
  }

  function nodeAt(px, py) {
    var p = toWorld(px, py);
    var vn = visibleNodes();
    var best = null, bestD = Infinity;
    for (var i = 0; i < vn.length; i++) {
      var n = vn[i];
      var dx = n.x - p.x, dy = n.y - p.y;
      var r = nodeRadius(n) + 4 / view.k;
      var d2 = dx * dx + dy * dy;
      if (d2 < r * r && d2 < bestD) { best = n; bestD = d2; }
    }
    return best;
  }

  // ---- shortest path ---------------------------------------------------
  var pathEdgeSet = null;

  function tracePath(a, b) {
    // BFS over visible edges
    var prev = {}, prevEdge = {}, seen = {}; seen[a] = true;
    var q = [a];
    while (q.length) {
      var cur = q.shift();
      if (cur === b) break;
      var neigh = adj[cur] || [];
      for (var i = 0; i < neigh.length; i++) {
        var o = neigh[i].other.id;
        if (seen[o] || !edgeVisible(neigh[i].edge)) continue;
        seen[o] = true;
        prev[o] = cur; prevEdge[o] = neigh[i].edge;
        q.push(o);
      }
    }
    if (!seen[b]) return null;
    var ids = new Set([b]), edgeSet = new Set();
    var cur2 = b;
    while (cur2 !== a) {
      edgeSet.add(prevEdge[cur2]);
      cur2 = prev[cur2];
      ids.add(cur2);
    }
    return { ids: ids, edges: edgeSet };
  }

  // ---- detail panel ----------------------------------------------------
  function edgeExplain(e, fromId) {
    var pfx = sitePrefix();
    if (e.kind === 'relation') {
      var outgoing = e.s.id === fromId;
      var reading = e.symmetric ? e.label : (outgoing ? e.label : e.inverse);
      var entry = e.entry ? ' · <a class="mono" href="' + pfx + 'entries/' + esc(e.entry) +
        '/" title="Establishing entry">' + esc(e.entry.split('/')[0]) + '</a>' : '';
      var note = e.note ? '<div class="muted">' + esc(e.note) + '</div>' : '';
      return '<span class="g-rel">' + esc(reading) + '</span>' + entry + note;
    }
    var n = e.count || (e.entries || []).length || 1;
    var what = e.kind === 'cve' ? 'carried by' : 'co-occurs in';
    var links = (e.entries || []).slice(0, 3).map(function (id) {
      return '<a class="mono" href="' + pfx + 'entries/' + esc(id) + '/">' + esc(id.split('/')[0]) + '</a>';
    }).join(', ');
    if (e.kind === 'technique') { what = 'mapped in'; }
    return '<span class="g-rel g-rel--derived">' + what + ' ' + n +
      ' entr' + (n === 1 ? 'y' : 'ies') + '</span>' + (links ? ' · ' + links : '');
  }

  function showPanel(n) {
    if (!panel) return;
    if (!n) { panel.hidden = true; panel.innerHTML = ''; return; }
    var pfx = sitePrefix();
    var pageUrl = n.kind === 'technique'
      ? pfx + 'attack/#' + encodeURIComponent(n.id)
      : pfx + 'entities/' + encodeURIComponent(n.id) + '/';
    var rows = (adj[n.id] || [])
      .filter(function (a) { return edgeVisible(a.edge); })
      .sort(function (a, b) {
        var ka = a.edge.kind === 'relation' ? 0 : 1;
        var kb = b.edge.kind === 'relation' ? 0 : 1;
        return ka - kb || (b.edge.count || 0) - (a.edge.count || 0);
      })
      .slice(0, 40)
      .map(function (a) {
        return '<li><button type="button" class="g-jump" data-jump="' + esc(a.other.id) + '">' +
          esc(a.other.label || a.other.id) + '</button> ' + edgeExplain(a.edge, n.id) + '</li>';
      }).join('');
    var meta = [];
    if (n.type) meta.push('<span class="e-tag e-tag--' + esc(n.type) + '">' + esc(n.type) + '</span>');
    if (n.nexus) meta.push('<span class="badge">' + esc(n.nexus) + '</span>');
    if (n.kind === 'cve' && n.exploited) meta.push('<span class="badge badge--accent">exploited</span>');
    if (n.entries) meta.push('<span class="muted">' + n.entries + ' entr' + (n.entries === 1 ? 'y' : 'ies') + '</span>');
    if (n.first) meta.push('<span class="mono muted">' + esc(n.first) + (n.last && n.last !== n.first ? ' → ' + esc(n.last) : '') + '</span>');
    panel.innerHTML =
      '<div class="g-panel-head">' +
      '<strong>' + esc(n.title && n.title !== n.label ? n.label + ' — ' + n.title : n.label) + '</strong>' +
      '<button type="button" class="mini-btn" data-panel-close aria-label="Close">×</button></div>' +
      '<div class="g-panel-meta">' + meta.join(' ') + '</div>' +
      '<div class="g-panel-actions">' +
      '<a class="mini-btn" href="' + pageUrl + '">open page</a> ' +
      '<button type="button" class="mini-btn" data-isolate="' + esc(n.id) + '">isolate</button> ' +
      '<button type="button" class="mini-btn" data-pin="' + esc(n.id) + '">' + (n.pinned ? 'unpin' : 'pin') + '</button>' +
      '</div>' +
      (pathIds && pathEnd
        ? '<p class="muted g-path-note">Path ' + esc(selected) + ' → ' + esc(pathEnd) + ': ' +
          (pathIds.size - 1) + ' hop(s). Esc to clear.</p>'
        : '<p class="muted g-path-note">Shift-click another node to trace the shortest path from here.</p>') +
      '<h4>Connections</h4><ul class="g-conn">' + (rows || '<li class="muted">none visible</li>') + '</ul>';
    panel.hidden = false;
  }

  // ---- interactions ----------------------------------------------------
  var dragNode = null, panning = false, lastPos = null, moved = false;

  function wire() {
    window.addEventListener('resize', function () { resize(); draw(); });

    canvas.addEventListener('pointerdown', function (ev) {
      canvas.setPointerCapture(ev.pointerId);
      var n = nodeAt(ev.offsetX, ev.offsetY);
      moved = false;
      lastPos = { x: ev.offsetX, y: ev.offsetY };
      if (n) { dragNode = n; } else { panning = true; }
    });
    canvas.addEventListener('pointermove', function (ev) {
      if (dragNode) {
        var p = toWorld(ev.offsetX, ev.offsetY);
        dragNode.x = p.x; dragNode.y = p.y;
        moved = true;
        alpha = Math.max(alpha, 0.12);
        layout(false);
        return;
      }
      if (panning && lastPos) {
        view.x += ev.offsetX - lastPos.x;
        view.y += ev.offsetY - lastPos.y;
        lastPos = { x: ev.offsetX, y: ev.offsetY };
        moved = true;
        draw();
        return;
      }
      var h = nodeAt(ev.offsetX, ev.offsetY);
      var hid = h ? h.id : null;
      if (hid !== hovered) {
        hovered = hid;
        canvas.style.cursor = h ? 'pointer' : 'grab';
        draw();
      }
    });
    canvas.addEventListener('pointerup', function (ev) {
      if (dragNode && moved) { dragNode.pinned = true; }
      var wasDrag = moved;
      var n = dragNode || (wasDrag ? null : nodeAt(ev.offsetX, ev.offsetY));
      dragNode = null; panning = false; lastPos = null;
      if (wasDrag || !n) { if (!n && !wasDrag) { clearSelection(); } return; }
      if (ev.shiftKey && selected && selected !== n.id) {
        setPath(selected, n.id);
      } else {
        selectNode(n.id);
      }
    });
    canvas.addEventListener('dblclick', function (ev) {
      var n = nodeAt(ev.offsetX, ev.offsetY);
      if (n) isolate(n.id);
    });
    canvas.addEventListener('wheel', function (ev) {
      ev.preventDefault();
      var factor = Math.exp(-ev.deltaY * 0.0012);
      var w = canvas.width / dpr, h = canvas.height / dpr;
      var mx = ev.offsetX - w / 2, my = ev.offsetY - h / 2;
      view.x = mx - (mx - view.x) * factor;
      view.y = my - (my - view.y) * factor;
      view.k = Math.max(0.08, Math.min(6, view.k * factor));
      draw();
    }, { passive: false });

    document.addEventListener('keydown', function (ev) {
      if (ev.key === 'Escape') { clearSelection(); }
    });

    shell.addEventListener('click', function (ev) {
      var t = ev.target.closest('[data-graph-layer]');
      if (t) {
        var l = t.getAttribute('data-graph-layer');
        layers[l] = !layers[l];
        t.classList.toggle('active', layers[l]);
        layout(true);
        return;
      }
      t = ev.target.closest('[data-graph-edges]');
      if (t) {
        var c = t.getAttribute('data-graph-edges');
        edgeClasses[c === 'derived' ? 'derived' : 'relation'] =
          !edgeClasses[c === 'derived' ? 'derived' : 'relation'];
        t.classList.toggle('active');
        draw();
        return;
      }
      if (ev.target.closest('[data-graph-reset]')) { resetAll(); return; }
      if (ev.target.closest('[data-panel-close]')) { clearSelection(); return; }
      t = ev.target.closest('[data-jump]');
      if (t) { selectNode(t.getAttribute('data-jump'), true); return; }
      t = ev.target.closest('[data-isolate]');
      if (t) { isolate(t.getAttribute('data-isolate')); return; }
      t = ev.target.closest('[data-pin]');
      if (t) {
        var n = nodeById[t.getAttribute('data-pin')];
        if (n) { n.pinned = !n.pinned; showPanel(n); draw(); }
        return;
      }
    });

    wireSearch();
  }

  function wireSearch() {
    var input = document.getElementById('graph-q');
    var sug = shell.querySelector('[data-graph-suggest]');
    if (!input || !sug) return;
    input.addEventListener('input', function () {
      var q = input.value.trim().toLowerCase();
      if (q.length < 2) { sug.hidden = true; sug.innerHTML = ''; return; }
      var hits = nodes.filter(function (n) {
        return (n.label || '').toLowerCase().indexOf(q) !== -1 ||
          (n.title || '').toLowerCase().indexOf(q) !== -1 ||
          n.id.toLowerCase().indexOf(q) !== -1;
      }).slice(0, 12);
      sug.innerHTML = hits.map(function (n) {
        return '<li><button type="button" data-jump="' + esc(n.id) + '">' +
          '<span class="e-tag e-tag--' + esc(n.type) + '">' + esc(n.type) + '</span> ' +
          esc(n.label) + (n.title && n.title !== n.label ? ' <span class="muted">' + esc(n.title) + '</span>' : '') +
          '</button></li>';
      }).join('');
      sug.hidden = hits.length === 0;
    });
    input.addEventListener('keydown', function (ev) {
      if (ev.key === 'Enter') {
        var first = sug.querySelector('[data-jump]');
        if (first) { selectNode(first.getAttribute('data-jump'), true); sug.hidden = true; }
      }
    });
    sug.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-jump]');
      if (b) { selectNode(b.getAttribute('data-jump'), true); sug.hidden = true; input.value = ''; }
    });
  }

  // ---- actions ---------------------------------------------------------
  function selectNode(id, center) {
    var n = nodeById[id];
    if (!n) return;
    if (!layers[n.kind]) {
      layers[n.kind] = true;
      var btn = shell.querySelector('[data-graph-layer="' + n.kind + '"]');
      if (btn) btn.classList.add('active');
      layout(true);
    }
    if (isolated && !isolated.has(id)) isolated = null;
    selected = id;
    pathEnd = null; pathIds = null; pathEdgeSet = null;
    showPanel(n);
    if (center) {
      view.x = -n.x * view.k;
      view.y = -n.y * view.k;
      if (view.k < 0.6) view.k = 0.9;
    }
    syncUrl();
    draw();
  }

  function setPath(a, b) {
    var res = tracePath(a, b);
    pathEnd = b;
    if (res) {
      pathIds = res.ids; pathEdgeSet = res.edges;
      if (statusEl) statusEl.textContent =
        'Shortest path: ' + (nodeById[a].label) + ' → ' + (nodeById[b].label) + ' = ' +
        (res.ids.size - 1) + ' hop(s). Every hop is an evidence-backed edge — click nodes along it for details. Esc to clear.';
    } else {
      pathIds = null; pathEdgeSet = null;
      if (statusEl) statusEl.textContent =
        'No path between ' + (nodeById[a].label) + ' and ' + (nodeById[b].label) +
        ' with the current layers/edge classes.';
    }
    showPanel(nodeById[selected]);
    syncUrl();
    draw();
  }

  function isolate(id) {
    var keep = new Set([id]);
    (adj[id] || []).forEach(function (a) {
      if (!edgeVisible(a.edge)) return;
      keep.add(a.other.id);
      (adj[a.other.id] || []).forEach(function (b) {
        if (edgeVisible(b.edge)) keep.add(b.other.id);
      });
    });
    isolated = keep;
    selectNode(id, true);
    if (statusEl) statusEl.textContent =
      'Isolated ' + (nodeById[id].label) + ' + neighbourhood (depth 2, ' +
      keep.size + ' nodes). Reset to restore the full graph.';
    layout(true);
  }

  function clearSelection() {
    selected = null;
    pathEnd = null; pathIds = null; pathEdgeSet = null;
    showPanel(null);
    syncUrl();
    draw();
  }

  function resetAll() {
    isolated = null;
    selected = null; pathEnd = null; pathIds = null; pathEdgeSet = null;
    view = { x: 0, y: 0, k: 1 };
    nodes.forEach(function (n) { n.pinned = false; });
    showPanel(null);
    syncUrl();
    layout(true);
  }

  // ---- URL state -------------------------------------------------------
  function syncUrl() {
    var p = new URLSearchParams();
    if (selected) p.set('focus', selected);
    if (selected && pathEnd) p.set('to', pathEnd);
    var qs = p.toString();
    history.replaceState(null, '', location.pathname + (qs ? '?' + qs : '') + location.hash);
  }

  function restoreFromUrl() {
    var p = new URLSearchParams(location.search);
    var focus = p.get('focus');
    var to = p.get('to');
    if (focus && nodeById[focus]) {
      // let the first layout settle briefly before centering
      setTimeout(function () {
        selectNode(focus, true);
        if (to && nodeById[to]) setPath(focus, to);
      }, 350);
    }
  }

  function resize() {
    var rect = canvas.parentElement.getBoundingClientRect();
    var w = Math.max(320, rect.width);
    var h = Math.max(420, Math.min(720, window.innerHeight - 260));
    canvas.style.width = w + 'px';
    canvas.style.height = h + 'px';
    canvas.width = Math.round(w * dpr);
    canvas.height = Math.round(h * dpr);
  }
})();
