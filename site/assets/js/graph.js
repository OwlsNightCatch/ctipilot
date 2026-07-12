/* graph.js — the /graph/ interactive threat graph (seeded exploration).
 *
 * Renders data/graph.json (all canonical entities + covered CVEs +
 * mapped ATT&CK techniques; curated typed edges + derived edges) as a
 * force-directed canvas — but never all at once: the analyst SEEDS the
 * view by naming one or more nodes, and the surface renders exactly the
 * connected subgraph reachable from those seeds (full component by
 * default, optionally hop-limited). Nothing unconnected is ever drawn,
 * and an empty seed list renders nothing — which keeps layout and
 * drawing fast no matter how large the store grows.
 *
 *   - search → add seed chips (multiple seeds compare components)
 *   - reach control: 1 hop (default) / 2 hops / full connected graph
 *   - double-click a node (or the panel's "expand") → pull that node's
 *     direct neighbours into the view — investigations grow node by
 *     node; nothing outside the grown view is ever drawn, not even
 *     dimmed
 *   - node-type layers (entities / CVEs / techniques) and edge-class
 *     toggles (curated / derived) — these also bound reachability
 *   - click → detail panel (typed relations with their source entries,
 *     neighbours, page links); shift-click a second node → shortest path
 *   - ?focus=<id>[,<id>…][&hops=1|2|all][&to=<id>] deep links (entity
 *     pages link here)
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
  var nodes = [];            // all nodes: {id,kind,type,label,...,x,y,vx,vy,deg,pinned}
  var nodeById = {};
  var edges = [];            // all edges: {s,t,kind,...} with node refs
  var adj = {};              // id -> [{other, edge}]
  var seeds = [];            // node ids the user named — the view roots
  var reach = 1;             // 1 | 2 | Infinity — BFS depth from the seeds
  var expanded = new Set();  // nodes whose direct neighbours were pulled in
  var extra = new Set();     // individually pulled-in nodes (panel jumps)
  var layers = { entity: true, cve: true, technique: false };
  var edgeClasses = { relation: true, derived: true };
  var visN = [], visE = [], visSet = new Set();   // cached visible subgraph
  var selected = null;       // node id
  var pathEnd = null;        // second node id (shift-click)
  var pathIds = null;        // Set of ids on the traced path
  var pathEdgeSet = null;
  var hovered = null;
  var view = { x: 0, y: 0, k: 1 };   // pan/zoom transform
  var canvas, ctx, panel, statusEl, shell, seedBox;
  var dpr = Math.max(1, window.devicePixelRatio || 1);
  var simTimer = null, alpha = 0;
  var colors = {};

  var HINT_DEFAULT = 'Double-click a node to pull in its neighbours · scroll to zoom · ' +
    'drag the canvas to pan · drag a node to pin it · click = details · ' +
    'shift-click a second node = shortest path · Esc = clear.';
  var HINT_EMPTY = 'Nothing is drawn until you pick a starting point — search above, or ' +
    'pick one of the most-connected entities below. The view then shows everything connected to it.';

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
    seedBox = shell.querySelector('[data-graph-seeds]');
    if (!canvas || !canvas.getContext) return;
    ctx = canvas.getContext('2d');
    readColors();
    // The theme toggle stamps data-theme on <html>; re-read the palette
    // and repaint so edges stay visible after a light/dark switch.
    new MutationObserver(function () { readColors(); draw(); })
      .observe(document.documentElement, { attributes: true, attributeFilter: ['data-theme'] });
    var mq = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)');
    if (mq && mq.addEventListener) {
      mq.addEventListener('change', function () { readColors(); draw(); });
    }

    fetch(sitePrefix() + cfg.data_url, { credentials: 'omit' })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return r.json(); })
      .then(function (payload) {
        data = payload; build(); shell.hidden = false; resize(); wire();
        if (!restoreFromUrl()) { refreshVisible(); }
      })
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
    // Edge inks come from the TEXT ramp, not the border ramp — the border
    // color is near-invisible against the page background in dark mode.
    colors.curated = (cs.getPropertyValue('--text-soft') || '').trim() || colors.text;
    colors.edge = colors.muted;
    colors.bg = (cs.getPropertyValue('--bg') || '').trim() || '#fff';
    colors.accent = (cs.getPropertyValue('--accent') || '').trim() || '#2f81f7';
  }

  function build() {
    nodes = (data.nodes || []).map(function (n) {
      return Object.assign({}, n, {
        x: 0, y: 0, vx: 0, vy: 0, deg: 0, pinned: false, placed: false
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
  }

  // ---- visibility: seeded reachability ---------------------------------
  function layerOk(n) { return !!layers[n.kind]; }
  function edgeClassOk(e) {
    return e.kind === 'relation' ? edgeClasses.relation : edgeClasses.derived;
  }
  function traversable(e) { return edgeClassOk(e) && layerOk(e.s) && layerOk(e.t); }

  function refreshVisible() {
    visSet = new Set();
    var rooted = seeds.filter(function (id) { return nodeById[id]; });
    if (rooted.length) {
      // BFS from every seed over traversable edges, bounded by `reach`.
      var depth = {};
      var q = [];
      rooted.forEach(function (id) {
        if (!layerOk(nodeById[id])) {
          // A seed always shows, even if its layer is toggled off …
          layers[nodeById[id].kind] = true;
          var btn = shell.querySelector('[data-graph-layer="' + nodeById[id].kind + '"]');
          if (btn) btn.classList.add('active');
        }
        depth[id] = 0; q.push(id); visSet.add(id);
      });
      while (q.length) {
        var cur = q.shift();
        if (depth[cur] >= reach) continue;
        var neigh = adj[cur] || [];
        for (var i = 0; i < neigh.length; i++) {
          var e = neigh[i];
          if (!traversable(e.edge)) continue;
          var o = e.other.id;
          if (visSet.has(o)) continue;
          visSet.add(o);
          depth[o] = depth[cur] + 1;
          q.push(o);
        }
      }
      // user-driven growth: nodes explicitly pulled in one by one — a
      // deliberate pick always shows, even when its layer is toggled off
      // (the layer toggles govern automatic reachability, not explicit
      // choices).
      extra.forEach(function (id) {
        if (nodeById[id]) visSet.add(id);
      });
      // … and expansions: a visible node's direct neighbours join the
      // view. Insertion order matters (each expansion may make the next
      // expandable node visible), so iterate until stable.
      var grew = true;
      while (grew) {
        grew = false;
        expanded.forEach(function (id) {
          if (!visSet.has(id)) return;
          (adj[id] || []).forEach(function (a) {
            if (!traversable(a.edge)) return;
            if (!visSet.has(a.other.id)) { visSet.add(a.other.id); grew = true; }
          });
        });
      }
    }
    visN = nodes.filter(function (n) { return visSet.has(n.id); });
    // Every edge between two visible nodes draws (visSet membership
    // already encodes the layer rules) — a visible pair must never show
    // without its connection.
    visE = edges.filter(function (e) {
      return visSet.has(e.s.id) && visSet.has(e.t.id) && edgeClassOk(e);
    });
    placeNew();
    if (selected && !visSet.has(selected)) { selected = null; showPanel(null); }
    if (pathIds) {
      var ok = true;
      pathIds.forEach(function (id) { if (!visSet.has(id)) ok = false; });
      if (!ok) { pathEnd = null; pathIds = null; pathEdgeSet = null; }
    }
    renderSeedChips();
    updateStatus();
    layout(true);
  }

  function placeNew() {
    // Deterministic spiral placement for nodes entering the view, highest
    // degree first; already-placed nodes keep their position.
    var golden = Math.PI * (3 - Math.sqrt(5));
    var fresh = visN.filter(function (n) { return !n.placed; });
    fresh.sort(function (a, b) { return b.deg - a.deg || (a.id < b.id ? -1 : 1); });
    var base = visN.length - fresh.length;
    fresh.forEach(function (n, i) {
      var k = base + i + 1;
      var r = 34 * Math.sqrt(k);
      n.x = r * Math.cos(k * golden);
      n.y = r * Math.sin(k * golden);
      n.placed = true;
    });
  }

  function updateStatus() {
    if (!statusEl) return;
    if (!seeds.length) { statusEl.textContent = HINT_EMPTY; return; }
    var reachLabel = reach === Infinity ? 'full connected graph' : reach + ' hop' + (reach === 1 ? '' : 's');
    statusEl.textContent = visN.length + ' node(s) · ' + visE.length + ' edge(s) — ' +
      reachLabel + ' from ' + seeds.map(function (id) {
        return (nodeById[id] || {}).label || id;
      }).join(', ') + '. ' + HINT_DEFAULT;
  }

  function renderSeedChips() {
    if (!seedBox) return;
    if (!seeds.length) { seedBox.innerHTML = '<span class="muted g-seed-empty">no starting point selected</span>'; return; }
    seedBox.innerHTML = seeds.map(function (id) {
      var n = nodeById[id] || { label: id, type: '' };
      return '<span class="g-seed-chip"><span class="e-tag e-tag--' + esc(n.type || 'none') + '">' +
        esc(n.type || '?') + '</span> ' + esc(n.label) +
        ' <button type="button" data-seed-remove="' + esc(id) + '" aria-label="Remove ' + esc(n.label) + '">×</button></span>';
    }).join('');
  }

  // ---- force layout (visible subgraph only) -----------------------------
  function layout(restart) {
    if (restart) alpha = 1;
    if (simTimer) return;
    var step = function () {
      tick();
      draw();
      alpha *= 0.97;
      if (alpha > 0.02 && visN.length) { simTimer = requestAnimationFrame(step); }
      else { simTimer = null; draw(); }
    };
    simTimer = requestAnimationFrame(step);
  }

  function tick() {
    var vn = visN, ve = visE;
    var i, j, n, m, dx, dy, d2, d, f;
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
      n.vx -= n.x * 0.012 * alpha;
      n.vy -= n.y * 0.012 * alpha;
    }
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

    if (!visN.length) {
      ctx.fillStyle = colors.muted;
      ctx.font = '14px ' + '-apple-system, BlinkMacSystemFont, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('Pick a starting point — search above or choose an entity below.', w / 2, h / 2 - 12);
      ctx.font = '12px -apple-system, BlinkMacSystemFont, sans-serif';
      ctx.fillText('The graph then shows everything connected to it — and nothing else.', w / 2, h / 2 + 12);
      ctx.textAlign = 'left';
      return;
    }

    ctx.translate(w / 2 + view.x, h / 2 + view.y);
    ctx.scale(view.k, view.k);

    var focusSet = null;
    if (hovered || selected) {
      focusSet = new Set();
      var fid = hovered || selected;
      focusSet.add(fid);
      (adj[fid] || []).forEach(function (a) {
        if (visSet.has(a.other.id) && edgeClassOk(a.edge)) focusSet.add(a.other.id);
      });
      if (pathIds) pathIds.forEach(function (id) { focusSet.add(id); });
    }

    var ve = visE;
    for (var i = 0; i < ve.length; i++) {
      var e = ve[i];
      var onPath = pathIds && pathEdgeSet && pathEdgeSet.has(e);
      var dimmed = focusSet && !onPath &&
        !(focusSet.has(e.s.id) && focusSet.has(e.t.id));
      ctx.beginPath();
      ctx.moveTo(e.s.x, e.s.y);
      ctx.lineTo(e.t.x, e.t.y);
      if (e.kind === 'relation') {
        ctx.setLineDash([]);
        ctx.strokeStyle = onPath ? colors.accent : colors.curated;
        ctx.lineWidth = (onPath ? 2.4 : 1.4) / view.k;
      } else {
        ctx.setLineDash([4 / view.k, 4 / view.k]);
        ctx.strokeStyle = onPath ? colors.accent : colors.edge;
        ctx.lineWidth = (onPath ? 2.2 : Math.min(2.5, 0.7 + (e.count || 1) * 0.25)) / view.k;
      }
      ctx.globalAlpha = dimmed ? 0.18 : (e.kind === 'relation' ? 0.9 : 0.65);
      ctx.stroke();
      ctx.setLineDash([]);
      if (e.kind === 'relation' && !e.symmetric && !dimmed && view.k > 0.35) {
        drawArrow(e, onPath ? colors.accent : colors.curated);
      }
    }
    ctx.globalAlpha = 1;

    var vn = visN;
    for (i = 0; i < vn.length; i++) {
      var n = vn[i];
      var r = nodeRadius(n);
      var dim = focusSet && !focusSet.has(n.id);
      ctx.beginPath();
      ctx.arc(n.x, n.y, r, 0, Math.PI * 2);
      ctx.fillStyle = colors[n.type] || colors.muted;
      ctx.globalAlpha = dim ? 0.4 : 1;
      ctx.fill();
      if (n.kind === 'cve' && n.exploited) {
        ctx.beginPath();
        ctx.arc(n.x, n.y, r + 2.2 / view.k, 0, Math.PI * 2);
        ctx.strokeStyle = colors.cve;
        ctx.lineWidth = 1.6 / view.k;
        ctx.stroke();
      }
      if (seeds.indexOf(n.id) !== -1) {
        ctx.beginPath();
        ctx.arc(n.x, n.y, r + 5 / view.k, 0, Math.PI * 2);
        ctx.strokeStyle = colors[n.type] || colors.muted;
        ctx.setLineDash([3 / view.k, 3 / view.k]);
        ctx.lineWidth = 1.4 / view.k;
        ctx.stroke();
        ctx.setLineDash([]);
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

    // labels: small views label everything; larger ones label seeds,
    // hovered/selected/path nodes and hubs (more as you zoom in)
    ctx.font = (11 / view.k) + 'px ui-monospace, SFMono-Regular, Menlo, monospace';
    ctx.textBaseline = 'middle';
    for (i = 0; i < vn.length; i++) {
      n = vn[i];
      var show = n.id === hovered || n.id === selected || n.id === pathEnd ||
        seeds.indexOf(n.id) !== -1 ||
        (pathIds && pathIds.has(n.id)) ||
        vn.length <= 40 ||
        (view.k > 1.4) || (n.deg >= 8 && view.k > 0.5);
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
    var best = null, bestD = Infinity;
    for (var i = 0; i < visN.length; i++) {
      var n = visN[i];
      var dx = n.x - p.x, dy = n.y - p.y;
      var r = nodeRadius(n) + 4 / view.k;
      var d2 = dx * dx + dy * dy;
      if (d2 < r * r && d2 < bestD) { best = n; bestD = d2; }
    }
    return best;
  }

  // ---- shortest path ---------------------------------------------------
  function tracePath(a, b) {
    var prev = {}, prevEdge = {}, seen = {}; seen[a] = true;
    var q = [a];
    var visEdgeSet = new Set(visE);
    while (q.length) {
      var cur = q.shift();
      if (cur === b) break;
      var neigh = adj[cur] || [];
      for (var i = 0; i < neigh.length; i++) {
        var o = neigh[i].other.id;
        if (seen[o] || !visEdgeSet.has(neigh[i].edge)) continue;
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
    var conns = (adj[n.id] || []).filter(function (a) { return edgeClassOk(a.edge); });
    // What "expand" would actually add: distinct not-yet-drawn neighbours
    // reachable over traversable edges (layer rules apply to automatic
    // growth) — never a per-edge count.
    var expandable = new Set();
    conns.forEach(function (a) {
      if (!visSet.has(a.other.id) && traversable(a.edge)) expandable.add(a.other.id);
    });
    var hiddenCount = expandable.size;
    var CONN_CAP = 40;
    var rows = conns
      .sort(function (a, b) {
        var ka = a.edge.kind === 'relation' ? 0 : 1;
        var kb = b.edge.kind === 'relation' ? 0 : 1;
        return ka - kb || (b.edge.count || 0) - (a.edge.count || 0);
      })
      .slice(0, CONN_CAP)
      .map(function (a) {
        var off = visSet.has(a.other.id) ? '' :
          ' <span class="muted" title="Not drawn yet — jumping pulls it into the view">(not in view)</span>';
        return '<li><button type="button" class="g-jump" data-jump="' + esc(a.other.id) + '">' +
          esc(a.other.label || a.other.id) + '</button>' + off + ' ' + edgeExplain(a.edge, n.id) + '</li>';
      }).join('');
    var meta = [];
    if (n.type) meta.push('<span class="e-tag e-tag--' + esc(n.type) + '">' + esc(n.type) + '</span>');
    if (n.nexus) meta.push('<span class="badge">' + esc(n.nexus) + '</span>');
    if (n.kind === 'cve' && n.exploited) meta.push('<span class="badge badge--accent">exploited</span>');
    if (n.entries) meta.push('<span class="muted">' + n.entries + ' entr' + (n.entries === 1 ? 'y' : 'ies') + '</span>');
    if (n.first) meta.push('<span class="mono muted">' + esc(n.first) + (n.last && n.last !== n.first ? ' → ' + esc(n.last) : '') + '</span>');
    var isSeed = seeds.indexOf(n.id) !== -1;
    panel.innerHTML =
      '<div class="g-panel-head">' +
      '<strong>' + esc(n.title && n.title !== n.label ? n.label + ' — ' + n.title : n.label) + '</strong>' +
      '<button type="button" class="mini-btn" data-panel-close aria-label="Close">×</button></div>' +
      '<div class="g-panel-meta">' + meta.join(' ') + '</div>' +
      '<div class="g-panel-actions">' +
      '<a class="mini-btn" href="' + pageUrl + '">open page</a> ' +
      (hiddenCount
        ? '<button type="button" class="mini-btn" data-expand="' + esc(n.id) +
          '" title="Pull this node’s direct neighbours into the view">expand +' + hiddenCount + '</button> '
        : '') +
      '<button type="button" class="mini-btn" data-reseed="' + esc(n.id) + '">re-seed here</button> ' +
      (isSeed
        ? '<button type="button" class="mini-btn" data-seed-remove="' + esc(n.id) + '">remove seed</button> '
        : '<button type="button" class="mini-btn" data-seed-add="' + esc(n.id) + '">add as seed</button> ') +
      '<button type="button" class="mini-btn" data-pin="' + esc(n.id) + '">' + (n.pinned ? 'unpin' : 'pin') + '</button>' +
      '</div>' +
      (pathIds && pathEnd
        ? '<p class="muted g-path-note">Path ' + esc(selected) + ' → ' + esc(pathEnd) + ': ' +
          (pathIds.size - 1) + ' hop(s). Esc to clear.</p>'
        : '<p class="muted g-path-note">Shift-click another node to trace the shortest path from here.</p>') +
      '<h4>Connections <span class="muted">(' + conns.length +
      (hiddenCount ? ' · ' + hiddenCount + ' not drawn yet' : '') + ')</span></h4>' +
      '<ul class="g-conn">' + (rows || '<li class="muted">none</li>') +
      (conns.length > CONN_CAP
        ? '<li class="muted">… showing the first ' + CONN_CAP + ' of ' + conns.length +
          ' — the <a href="' + pageUrl + '">entity page</a> lists them all</li>'
        : '') + '</ul>';
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
      if (n) expandNode(n.id);
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
        refreshVisible();
        return;
      }
      t = ev.target.closest('[data-graph-edges]');
      if (t) {
        var c = t.getAttribute('data-graph-edges');
        edgeClasses[c === 'derived' ? 'derived' : 'relation'] =
          !edgeClasses[c === 'derived' ? 'derived' : 'relation'];
        t.classList.toggle('active');
        refreshVisible();
        return;
      }
      t = ev.target.closest('[data-graph-reach]');
      if (t) {
        var r = t.getAttribute('data-graph-reach');
        reach = r === 'all' ? Infinity : parseInt(r, 10);
        shell.querySelectorAll('[data-graph-reach]').forEach(function (b) {
          b.classList.toggle('active', b === t);
        });
        refreshVisible();
        syncUrl();
        return;
      }
      if (ev.target.closest('[data-graph-reset]')) { resetAll(); return; }
      if (ev.target.closest('[data-panel-close]')) { clearSelection(); return; }
      t = ev.target.closest('[data-jump]');
      if (t) { jumpTo(t.getAttribute('data-jump')); return; }
      t = ev.target.closest('[data-expand]');
      if (t) { expandNode(t.getAttribute('data-expand')); return; }
      t = ev.target.closest('[data-reseed]');
      if (t) { reseed(t.getAttribute('data-reseed')); return; }
      t = ev.target.closest('[data-seed-add]');
      if (t) { addSeed(t.getAttribute('data-seed-add')); return; }
      t = ev.target.closest('[data-seed-remove]');
      if (t) { removeSeed(t.getAttribute('data-seed-remove')); return; }
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
      });
      hits.sort(function (a, b) { return b.deg - a.deg; });
      hits = hits.slice(0, 12);
      sug.innerHTML = hits.map(function (n) {
        return '<li><button type="button" data-seed-pick="' + esc(n.id) + '">' +
          '<span class="e-tag e-tag--' + esc(n.type) + '">' + esc(n.type) + '</span> ' +
          esc(n.label) + (n.title && n.title !== n.label ? ' <span class="muted">' + esc(n.title) + '</span>' : '') +
          ' <span class="muted mono">×' + n.deg + '</span></button></li>';
      }).join('');
      sug.hidden = hits.length === 0;
    });
    input.addEventListener('keydown', function (ev) {
      if (ev.key === 'Enter') {
        var first = sug.querySelector('[data-seed-pick]');
        if (first) { pickSeed(first.getAttribute('data-seed-pick')); }
      }
      if (ev.key === 'Escape') { sug.hidden = true; }
    });
    sug.addEventListener('click', function (ev) {
      var b = ev.target.closest('[data-seed-pick]');
      if (b) { pickSeed(b.getAttribute('data-seed-pick')); }
    });
    function pickSeed(id) {
      sug.hidden = true; sug.innerHTML = ''; input.value = '';
      addSeed(id);
      selectNode(id, true);
    }
  }

  // ---- actions ---------------------------------------------------------
  function addSeed(id) {
    if (!nodeById[id]) return;
    if (seeds.indexOf(id) === -1) seeds.push(id);
    refreshVisible();
    syncUrl();
  }

  function removeSeed(id) {
    seeds = seeds.filter(function (s) { return s !== id; });
    refreshVisible();
    syncUrl();
    if (selected) showPanel(nodeById[selected]);
  }

  function reseed(id) {
    if (!nodeById[id]) return;
    seeds = [id];
    expanded.clear();
    extra.clear();
    refreshVisible();
    selectNode(id, true);
  }

  function expandNode(id) {
    if (!nodeById[id]) return;
    expanded.add(id);
    refreshVisible();
    selectNode(id);
  }

  function jumpTo(id) {
    // Neighbour click in the panel: select it; if it is not drawn yet,
    // pull exactly this one node into the view (never its whole
    // neighbourhood — growth stays user-driven, node by node).
    if (!visSet.has(id)) { extra.add(id); refreshVisible(); }
    selectNode(id, true);
  }

  function selectNode(id, center) {
    var n = nodeById[id];
    if (!n) return;
    if (!visSet.has(id)) { extra.add(id); refreshVisible(); }
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
        ' inside the current view (layers/edge classes apply).';
    }
    showPanel(nodeById[selected]);
    syncUrl();
    draw();
  }

  function clearSelection() {
    selected = null;
    pathEnd = null; pathIds = null; pathEdgeSet = null;
    showPanel(null);
    updateStatus();
    syncUrl();
    draw();
  }

  function resetAll() {
    seeds = [];
    expanded.clear();
    extra.clear();
    selected = null; pathEnd = null; pathIds = null; pathEdgeSet = null;
    view = { x: 0, y: 0, k: 1 };
    nodes.forEach(function (n) { n.pinned = false; n.placed = false; });
    showPanel(null);
    refreshVisible();
    syncUrl();
  }

  // ---- URL state -------------------------------------------------------
  function syncUrl() {
    var p = new URLSearchParams();
    if (seeds.length) p.set('focus', seeds.join(','));
    if (selected && pathEnd) p.set('to', pathEnd);
    if (reach !== 1) p.set('hops', reach === Infinity ? 'all' : String(reach));
    var qs = p.toString();
    history.replaceState(null, '', location.pathname + (qs ? '?' + qs : '') + location.hash);
  }

  function restoreFromUrl() {
    var p = new URLSearchParams(location.search);
    var hops = p.get('hops');
    if (hops && /^([12]|all)$/.test(hops)) {
      reach = hops === 'all' ? Infinity : parseInt(hops, 10);
      shell.querySelectorAll('[data-graph-reach]').forEach(function (b) {
        b.classList.toggle('active', b.getAttribute('data-graph-reach') === hops);
      });
    }
    var focus = (p.get('focus') || '').split(',').filter(function (id) { return nodeById[id]; });
    var to = p.get('to');
    if (!focus.length) return false;
    seeds = focus;
    refreshVisible();
    // let the first layout settle briefly before centering
    setTimeout(function () {
      selectNode(focus[0], true);
      if (to && nodeById[to]) setPath(focus[0], to);
    }, 350);
    return true;
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
