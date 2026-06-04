/* ============================================================
   Clair Obscur: Expedition 33 — Tracker  |  app.js
   ============================================================ */

// ── ICONS ────────────────────────────────────────────────────
const ICONS = {
  shield:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>`,
  sword:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="14.5 17.5 3 6 3 3 6 3 17.5 14.5"/><line x1="13" y1="19" x2="19" y2="13"/><line x1="16" y1="16" x2="20" y2="20"/><line x1="19" y1="21" x2="21" y2="19"/></svg>`,
  layers:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>`,
  book:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>`,
  scissors:  `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><line x1="20" y1="4" x2="8.12" y2="15.88"/><line x1="14.47" y1="14.48" x2="20" y2="20"/><line x1="8.12" y1="8.12" x2="12" y2="12"/></svg>`,
  search:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>`,
  mask:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2z"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" y1="9" x2="9.01" y2="9"/><line x1="15" y1="9" x2="15.01" y2="9"/></svg>`,
  zap:       `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>`,
  music:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>`,
  shirt:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.38 3.46L16 2a4 4 0 0 1-8 0L3.62 3.46a2 2 0 0 0-1.34 2.23l.58 3.57a1 1 0 0 0 .99.84H6v10c0 1.1.9 2 2 2h8a2 2 0 0 0 2-2V10h2.15a1 1 0 0 0 .99-.84l.58-3.57a2 2 0 0 0-1.34-2.23z"/></svg>`,
  lock:      `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>`,
  target:    `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>`,
  image:     `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>`,
  map:       `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>`,
  droplet:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>`,
  crosshair: `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="22" y1="12" x2="18" y2="12"/><line x1="6" y1="12" x2="2" y2="12"/><line x1="12" y1="6" x2="12" y2="2"/><line x1="12" y1="22" x2="12" y2="18"/></svg>`,
  extlink:   `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>`,
};

const CHAR_CATEGORIES = new Set(['haircuts', 'outfits', 'weapons', 'monoco-skills']);

// Background image per category
const CAT_IMAGES = {
  'bosses-main':     'assets/images/bg_img_clairobscur_mainbosses.jpg',
  'bosses-optional': 'assets/images/bg_img_clairobscur_optionalbosses.jpg',
  'endless-tower':   'assets/images/bg_img_clairobscur_endlesstower.jpg',
  'journals':        'assets/images/bg_img_clairobscur_journals.jpg',
  'haircuts':        'assets/images/bg_img_clairobscur_haircuts.jpg',
  'lost-gestrals':   'assets/images/bg_img_clairobscur_gestrals.jpg',
  'mimes':           'assets/images/bg_img_clairobscur_mimes.jpg',
  'monoco-skills':   'assets/images/bg_img_clairobscur_monocoskills.jpg',
  'music-records':   'assets/images/bg_img_clairobscur_music.jpg',
  'outfits':         'assets/images/bg_img_clairobscur_outfits.jpg',
  'paint-cages':     'assets/images/bg_img_clairobscur_paintcages.jpg',
  'petanks':         'assets/images/bg_img_clairobscur_petanks.jpg',
  'pictos':          'assets/images/bg_img_clairobscur_pictos.jpg',
  'quests':          'assets/images/bg_img_clairobscur_quests.jpg',
  'tint-upgrades':   'assets/images/bg_img_clairobscur_tintupgrades.jpg',
  'weapons':         'assets/images/bg_img_clairobscur_weapons.jpg',
};
const PICTO_ID  = 'pictos';
const TOWER_ID  = 'endless-tower';

// ── STATE ────────────────────────────────────────────────────
const STATE_KEY = 'co33-tracker-v1';

function defaultState() {
  return { version: 1, completed: {}, pictos: {}, filters: { status: 'all', missable: 'all' } };
}
function loadState() {
  try {
    const raw = localStorage.getItem(STATE_KEY);
    if (raw) return { ...defaultState(), ...JSON.parse(raw) };
  } catch {}
  return defaultState();
}
function saveState() { localStorage.setItem(STATE_KEY, JSON.stringify(state)); }

let state = loadState();

function isCompleted(id) { return !!state.completed[id]; }
function toggleItem(id) {
  state.completed[id] = !state.completed[id];
  if (!state.completed[id]) delete state.completed[id];
  saveState();
}
function getPictoState(id) { return state.pictos[id] || 'none'; }

// ── DATA ─────────────────────────────────────────────────────
let categories = [];
const dataCache = {};

async function loadCategories() {
  const res = await fetch('data/categories.json');
  categories = await res.json();
}
async function loadCategoryData(id) {
  if (dataCache[id]) return dataCache[id];
  const cat = categories.find(c => c.id === id);
  if (!cat) return null;
  const res = await fetch(`data/${cat.file}`);
  dataCache[id] = await res.json();
  return dataCache[id];
}

// ── PROGRESS ─────────────────────────────────────────────────
function computeProgress(catId, items) {
  if (catId === PICTO_ID) {
    const done = items.filter(it => getPictoState(it.id) !== 'none').length;
    return { done, total: items.length, pct: items.length ? Math.round(done / items.length * 100) : 0 };
  }
  if (catId === TOWER_ID) {
    const stages = [...new Set(items.map(it => it.stage))];
    const done = stages.filter(s => items.filter(it => it.stage === s).every(it => isCompleted(it.id))).length;
    return { done, total: stages.length, pct: stages.length ? Math.round(done / stages.length * 100) : 0 };
  }
  const done = items.filter(it => isCompleted(it.id)).length;
  return { done, total: items.length, pct: items.length ? Math.round(done / items.length * 100) : 0 };
}

async function computeOverallProgress() {
  let totalDone = 0, totalAll = 0;
  for (const cat of categories) {
    const data = await loadCategoryData(cat.id);
    if (!data) continue;
    const p = computeProgress(cat.id, data.items);
    totalDone += p.done; totalAll += p.total;
  }
  return { done: totalDone, total: totalAll, pct: totalAll ? Math.round(totalDone / totalAll * 100) : 0 };
}

// ── HOME VIEW ─────────────────────────────────────────────────
async function renderHome() {
  // Overall progress
  const overall = await computeOverallProgress();
  document.getElementById('home-overall-fill').style.width = `${overall.pct}%`;
  document.getElementById('home-overall-pct').textContent  = `${overall.pct}%`;
  document.getElementById('home-overall-label').textContent = `${overall.done} / ${overall.total} completed`;

  // Category cards
  const container = document.getElementById('home-categories');
  container.innerHTML = '';

  for (const cat of categories) {
    const data  = await loadCategoryData(cat.id);
    const items = data ? data.items : [];
    const p     = computeProgress(cat.id, items);

    const card = document.createElement('div');
    card.className = 'home-cat-card';
    card.innerHTML = `
      <div class="home-cat-icon">${ICONS[cat.icon] || ICONS.map}</div>
      <div class="home-cat-info">
        <div class="home-cat-name">${esc(cat.name)}</div>
        <div class="home-cat-bar-row">
          <div class="home-cat-track">
            <div class="home-cat-fill" style="width:${p.pct}%"></div>
          </div>
          <span class="home-cat-count">${p.done} / ${p.total}</span>
        </div>
      </div>
      <div class="home-cat-arrow">›</div>`;
    card.addEventListener('click', () => navigateTo(cat.id));
    container.appendChild(card);
  }
}

// ── ROUTER ───────────────────────────────────────────────────
function navigateTo(catId) {
  window.location.hash = catId ? `#${catId}` : '';
}

function goHome() {
  window.location.hash = '';
}

async function route() {
  const hash = window.location.hash.replace('#', '');
  const isCategory = hash && categories.find(c => c.id === hash);

  document.getElementById('view-home').classList.toggle('hidden', !!isCategory);
  document.getElementById('view-category').classList.toggle('hidden', !isCategory);

  if (isCategory) {
    await showCategoryView(hash);
  } else {
    await renderHome();
  }
}

// ── CATEGORY VIEW ─────────────────────────────────────────────
async function showCategoryView(catId) {
  const cat  = categories.find(c => c.id === catId);
  const data = await loadCategoryData(catId);
  if (!cat || !data) return;

  // Update header title
  document.getElementById('cat-header-title').textContent = cat.name;

  const scroll = document.getElementById('cat-scroll');
  scroll.innerHTML = '';
  scroll.scrollTop = 0;

  // Insert category hero image if available
  const imgPath = CAT_IMAGES[catId];
  if (imgPath) {
    const hero = document.createElement('div');
    hero.className = 'cat-hero';
    hero.style.backgroundImage = `url('${imgPath}')`;
    hero.innerHTML = '<div class="cat-hero-overlay"></div>';
    scroll.appendChild(hero);
  }

  // Render section
  const section = await renderSection(cat);
  if (section) scroll.appendChild(section);

  // Re-apply filters
  applyFilters(section, catId);
}

function updateCategoryProgress(catId) {
  const section = document.querySelector('.category-section');
  if (!section) return;
  const data = dataCache[catId];
  if (!data) return;
  const p = computeProgress(catId, data.items);
  const fill = section.querySelector('.progress-fill');
  const pct  = section.querySelector('.progress-pct');
  const cnt  = section.querySelector('.cat-count');
  if (fill) fill.style.width = `${p.pct}%`;
  if (pct)  pct.textContent = `${p.pct}%`;
  if (cnt)  cnt.textContent = `${p.done} / ${p.total}`;
}

// ── EXPORT ───────────────────────────────────────────────────
function exportProgress() {
  const date = new Date().toISOString().slice(0, 10);
  const blob = new Blob([JSON.stringify(state, null, 2)], { type: 'application/json' });
  const url  = URL.createObjectURL(blob);
  const a    = document.createElement('a');
  a.href = url; a.download = `clairobscur-progress-${date}.json`; a.click();
  URL.revokeObjectURL(url);
}

// ── HELPERS ───────────────────────────────────────────────────
function esc(str) {
  return String(str || '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function ignBtn(url, label = 'IGN Walkthrough') {
  if (!url) return '';
  return `<a class="btn-ign" href="${esc(url)}" target="_blank" rel="noopener" onclick="event.stopPropagation()">${ICONS.extlink} ${label}</a>`;
}
function ignSmBtn(url) {
  if (!url) return '';
  return `<a class="btn-ign-sm" href="${esc(url)}" target="_blank" rel="noopener" onclick="event.stopPropagation()" aria-label="IGN">${ICONS.extlink}</a>`;
}
function badges(item) {
  let out = '';
  if (item.missable) out += `<span class="badge badge-warn">⚠ Missable</span>`;
  if (item.act)      out += `<span class="badge badge-warn">Act ${item.act}</span>`;
  return out ? `<div class="item-badges">${out}</div>` : '';
}
function missBlock(item) {
  if (!item.missable && !item.act) return '';
  let msg = '';
  if (item.missable && item.act) msg = `⚠ Missable — only available in Act ${item.act}.`;
  else if (item.missable)        msg = `⚠ Missable — can be permanently missed.`;
  else if (item.act)             msg = `⚠ Only available in Act ${item.act}.`;
  return `<div class="miss-block">${msg}</div>`;
}
function rewardsHtml(rewardsStr) {
  if (!rewardsStr) return '';
  const parts = rewardsStr.split(/[-\n]/).map(s => s.trim()).filter(Boolean);
  if (!parts.length) return '';
  return `<div class="rewards-row">${parts.map(r => `<span class="reward-chip"><span class="rdot todo"></span>${esc(r)}</span>`).join('')}</div>`;
}

// ── ITEM RENDERERS ─────────────────────────────────────────────
function renderStandardItem(item, catId) {
  const done = isCompleted(item.id);
  const el   = document.createElement('div');
  el.className = `item${done ? ' completed' : ''}`;
  el.dataset.id  = item.id;
  el.dataset.cat = catId;

  let detailFields = '';
  const gridParts = [];
  if (item.location)    gridParts.push(`<div><div class="detail-label">Location</div><div class="detail-value hi">${esc(item.location)}</div></div>`);
  if (item.act)         gridParts.push(`<div><div class="detail-label">Act</div><div class="detail-value hi">Act ${item.act}</div></div>`);
  if (item.damage_type) gridParts.push(`<div><div class="detail-label">Damage Type</div><div class="detail-value hi">${esc(item.damage_type)}</div></div>`);
  if (item.max_damage)  gridParts.push(`<div><div class="detail-label">Max Damage</div><div class="detail-value hi">${esc(item.max_damage)}</div></div>`);
  if (item.scaling)     gridParts.push(`<div><div class="detail-label">Scaling</div><div class="detail-value hi">${esc(item.scaling)}</div></div>`);
  if (gridParts.length) detailFields += `<div class="detail-grid">${gridParts.join('')}</div>`;

  const howField = item.how_to_find || item.how_to_complete || item.description || item.enemy_location || '';
  if (howField) {
    const label = item.enemy_location ? 'Enemy Location' : (item.how_to_complete ? 'How to Complete' : 'How to Find');
    detailFields += `<div class="detail-sep"></div><div class="detail-label">${label}</div><div class="detail-value">${esc(howField)}</div>`;
  }
  if (item.passives)  detailFields += `<div class="detail-sep"></div><div class="detail-label">Passives</div><div class="detail-value">${esc(item.passives)}</div>`;
  if (item.rewards)   detailFields += `<div class="detail-sep"></div><div class="detail-label">Rewards</div>${rewardsHtml(item.rewards)}`;
  detailFields += missBlock(item);
  detailFields += ignBtn(item.ign_url);

  const displayName = item.name || item.location || '—';
  const displaySub  = item.name ? (item.location || '') : (item.how_to_find ? item.how_to_find.slice(0, 60) + (item.how_to_find.length > 60 ? '…' : '') : '');

  el.innerHTML = `
    <div class="item-row">
      <div class="toggle ${done ? 'on' : ''}" data-toggle="${item.id}">${done ? '✓' : '○'}</div>
      <div class="item-info">
        <div class="item-name">${esc(displayName)}</div>
        ${displaySub ? `<div class="item-sub">${esc(displaySub)}</div>` : ''}
      </div>
      ${badges(item)}
      ${ignSmBtn(item.ign_url)}
      <div class="expand-arrow">▾</div>
    </div>
    <div class="item-detail">${detailFields}</div>`;

  el.querySelector('[data-toggle]').addEventListener('click', e => {
    e.stopPropagation();
    toggleItem(item.id);
    const btn = el.querySelector('[data-toggle]');
    const nowDone = isCompleted(item.id);
    btn.className = `toggle ${nowDone ? 'on' : ''}`;
    btn.textContent = nowDone ? '✓' : '○';
    el.classList.toggle('completed', nowDone);
    updateCategoryProgress(catId);
    refreshHomeIfVisible();
  });

  el.addEventListener('click', () => toggleExpand(el));
  return el;
}

function renderPictoItem(item) {
  const st = getPictoState(item.id);
  const el = document.createElement('div');
  el.className = `item${st !== 'none' ? ' completed' : ''}`;
  el.dataset.id  = item.id;
  el.dataset.cat = PICTO_ID;

  const detailFields = `
    <div class="detail-grid">
      <div><div class="detail-label">Effect</div><div class="detail-value">${esc(item.effect)}</div></div>
      <div><div class="detail-label">Lumina Cost</div><div class="detail-value hi">${esc(item.lumina_cost)} pts</div></div>
    </div>
    <div class="detail-sep"></div>
    <div class="detail-label">Location</div><div class="detail-value hi">${esc(item.location)}</div>
    ${item.how_to_find ? `<div class="detail-sep"></div><div class="detail-label">How to Find</div><div class="detail-value">${esc(item.how_to_find)}</div>` : ''}
    ${missBlock(item)}
    ${ignBtn(item.ign_url, 'IGN Reference')}`;

  el.innerHTML = `
    <div class="item-row">
      <div class="toggle-group">
        <div class="toggle-p ${st === 'collected' || st === 'lumina' ? 'collected' : ''}" data-picto-c="${item.id}">${st === 'collected' || st === 'lumina' ? '✓' : '○'}</div>
        <div class="toggle-p ${st === 'lumina' ? 'lumina' : ''}" data-picto-l="${item.id}">${st === 'lumina' ? '★' : 'L'}</div>
      </div>
      <div class="item-info">
        <div class="item-name">${esc(item.name)}</div>
        <div class="item-sub">${esc(item.location)}</div>
      </div>
      ${item.missable ? `<div class="item-badges"><span class="badge badge-warn">⚠</span></div>` : ''}
      ${ignSmBtn(item.ign_url)}
      <div class="expand-arrow">▾</div>
    </div>
    <div class="item-detail">${detailFields}</div>`;

  el.querySelector('[data-picto-c]').addEventListener('click', e => {
    e.stopPropagation();
    const cur = getPictoState(item.id);
    if (cur === 'none')      state.pictos[item.id] = 'collected';
    else if (cur === 'collected') state.pictos[item.id] = 'lumina';
    else                     delete state.pictos[item.id];
    saveState();
    refreshPictoItem(el, item);
    updateCategoryProgress(PICTO_ID);
    refreshHomeIfVisible();
  });

  el.querySelector('[data-picto-l]').addEventListener('click', e => {
    e.stopPropagation();
    const cur = getPictoState(item.id);
    if (cur === 'lumina')    state.pictos[item.id] = 'collected';
    else if (cur === 'collected') state.pictos[item.id] = 'lumina';
    else                     state.pictos[item.id] = 'collected';
    saveState();
    refreshPictoItem(el, item);
    updateCategoryProgress(PICTO_ID);
    refreshHomeIfVisible();
  });

  el.addEventListener('click', () => toggleExpand(el));
  return el;
}

function renderTowerStageGroup(stage, trials) {
  const allDone = trials.every(t => isCompleted(t.id));
  const el = document.createElement('div');
  el.className = `item stage-row${allDone ? ' completed' : ''}`;

  const trialsHtml = trials.map(t => `
    <div>
      <div class="detail-label">Trial ${t.trial} — Enemies</div>
      <div class="detail-value">${esc(t.enemies)}</div>
      ${t.rewards ? `<div class="detail-label" style="margin-top:6px">Rewards</div><div class="detail-value">${esc(t.rewards)}</div>` : ''}
    </div>`).join('<div class="detail-sep"></div>');

  el.innerHTML = `
    <div class="item-row">
      <div class="stage-toggle ${allDone ? 'on' : ''}" data-stage="${stage}">${allDone ? '✓' : '○'}</div>
      <div class="item-info">
        <div class="stage-num">Stage ${stage}</div>
        <div class="item-sub">${trials.map(t => `Trial ${t.trial}: ${t.enemies.split(',')[0]}…`).join(' · ')}</div>
      </div>
      <div class="expand-arrow">▾</div>
    </div>
    <div class="item-detail">${trialsHtml}</div>`;

  el.querySelector('[data-stage]').addEventListener('click', e => {
    e.stopPropagation();
    const newVal = !allDone;
    trials.forEach(t => { if (newVal) state.completed[t.id] = true; else delete state.completed[t.id]; });
    saveState();
    const newEl = renderTowerStageGroup(stage, trials);
    el.replaceWith(newEl);
    updateCategoryProgress(TOWER_ID);
    refreshHomeIfVisible();
  });

  el.addEventListener('click', () => toggleExpand(el));
  return el;
}

// ── EXPAND ───────────────────────────────────────────────────
function toggleExpand(el) {
  const isOpen = el.classList.contains('expanded');
  document.querySelectorAll('.item.expanded').forEach(e => e.classList.remove('expanded'));
  if (!isOpen) el.classList.add('expanded');
}

// ── REFRESH HOME PROGRESS (when on home view) ─────────────────
async function refreshHomeIfVisible() {
  const homeVisible = !document.getElementById('view-home').classList.contains('hidden');
  if (!homeVisible) return;
  const overall = await computeOverallProgress();
  document.getElementById('home-overall-fill').style.width = `${overall.pct}%`;
  document.getElementById('home-overall-pct').textContent  = `${overall.pct}%`;
  document.getElementById('home-overall-label').textContent = `${overall.done} / ${overall.total} completed`;
  // Update category card counts
  document.querySelectorAll('.home-cat-card').forEach((card, i) => {
    const cat  = categories[i];
    if (!cat) return;
    const data = dataCache[cat.id];
    if (!data) return;
    const p = computeProgress(cat.id, data.items);
    const fill  = card.querySelector('.home-cat-fill');
    const count = card.querySelector('.home-cat-count');
    if (fill)  fill.style.width = `${p.pct}%`;
    if (count) count.textContent = `${p.done} / ${p.total}`;
  });
}

// ── SECTION RENDERER ──────────────────────────────────────────
async function renderSection(cat) {
  const data  = await loadCategoryData(cat.id);
  if (!data) return null;
  const items = data.items;
  const p     = computeProgress(cat.id, items);

  const section = document.createElement('section');
  section.className = 'category-section';

  section.innerHTML = `
    <div class="category-header">
      <div class="cat-rule-l"></div>
      <div class="cat-title">${esc(cat.name)}</div>
      <div class="cat-rule-r"></div>
      <div class="cat-count">${p.done} / ${p.total}</div>
    </div>
    <div class="progress-row">
      <div class="progress-track"><div class="progress-fill" style="width:${p.pct}%"></div></div>
      <div class="progress-pct">${p.pct}%</div>
    </div>
    <div class="items-container"></div>`;

  const container = section.querySelector('.items-container');

  if (cat.id === TOWER_ID) {
    const stageMap = {};
    items.forEach(it => { if (!stageMap[it.stage]) stageMap[it.stage] = []; stageMap[it.stage].push(it); });
    Object.keys(stageMap).sort((a,b) => +a - +b).forEach(s => container.appendChild(renderTowerStageGroup(+s, stageMap[s])));
  } else if (cat.id === PICTO_ID) {
    items.forEach(item => container.appendChild(renderPictoItem(item)));
  } else if (CHAR_CATEGORIES.has(cat.id)) {
    const chars = [...new Set(items.map(it => it.character).filter(Boolean))];
    const hasFilterTabs = true; // all character categories use filter tabs

    // Jump links only for categories without filter tabs
    if (chars.length > 1 && !hasFilterTabs) {
      const jumps = document.createElement('div');
      jumps.className = 'char-jumps';
      chars.forEach(ch => {
        const btn = document.createElement('button');
        btn.className = 'char-jump-btn';
        btn.textContent = ch;
        // Use scrollIntoView instead of href to avoid triggering the hash router
        btn.addEventListener('click', () => {
          const target = document.getElementById(`char-${cat.id}-${ch.replace(/\s+/g,'-')}`);
          if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
        jumps.appendChild(btn);
      });
      section.querySelector('.progress-row').insertAdjacentElement('afterend', jumps);
    }
    if (chars.length > 1) {
      const tabs = document.createElement('div');
      tabs.className = 'char-filter-tabs';
      const allTab = document.createElement('button');
      allTab.className = 'char-tab active'; allTab.textContent = 'All'; allTab.dataset.char = 'all';
      tabs.appendChild(allTab);
      chars.forEach(ch => {
        const tab = document.createElement('button');
        tab.className = 'char-tab'; tab.textContent = ch; tab.dataset.char = ch;
        tabs.appendChild(tab);
      });
      tabs.addEventListener('click', e => {
        const btn = e.target.closest('.char-tab');
        if (!btn) return;
        tabs.querySelectorAll('.char-tab').forEach(t => t.classList.remove('active'));
        btn.classList.add('active');
        const sel = btn.dataset.char;
        container.querySelectorAll('.char-subheader').forEach(h => { h.style.display = (sel === 'all' || h.dataset.char === sel) ? '' : 'none'; });
        container.querySelectorAll('.item').forEach(el => { el.style.display = (sel === 'all' || el.dataset.char === sel) ? '' : 'none'; });
      });
      const jumpsEl = section.querySelector('.char-jumps');
      (jumpsEl || section.querySelector('.progress-row')).insertAdjacentElement('afterend', tabs);
    }
    chars.forEach(ch => {
      const sub = document.createElement('div');
      sub.className = 'char-subheader';
      sub.id = `char-${cat.id}-${ch.replace(/\s+/g,'-')}`;
      sub.dataset.char = ch;
      sub.textContent = ch;
      container.appendChild(sub);
      items.filter(it => it.character === ch).forEach(item => {
        const el = renderStandardItem(item, cat.id);
        el.dataset.char = ch;
        container.appendChild(el);
      });
    });
  } else {
    items.forEach(item => container.appendChild(renderStandardItem(item, cat.id)));
  }

  return section;
}

// ── FILTERS ───────────────────────────────────────────────────
function itemPassesFilter(item, catId) {
  const { status, missable } = state.filters;
  if (missable === 'only' && !item.missable) return false;
  if (status === 'done') {
    return catId === PICTO_ID ? getPictoState(item.id) !== 'none' : isCompleted(item.id);
  }
  if (status === 'remaining') {
    return catId === PICTO_ID ? getPictoState(item.id) === 'none' : !isCompleted(item.id);
  }
  return true;
}

function applyFilters(section, catId) {
  if (!section) return;
  section.querySelectorAll('.item').forEach(el => {
    const id   = el.dataset.id;
    const data = dataCache[catId];
    if (!data || !id) return;
    const item = data.items.find(it => it.id === id);
    if (!item) return;
    el.classList.toggle('hidden', !itemPassesFilter(item, catId));
  });
}

function initFilterPanel() {
  const panel = document.getElementById('filter-panel');
  panel.querySelectorAll('.pill').forEach(pill => {
    pill.addEventListener('click', () => {
      const key = pill.dataset.filter;
      panel.querySelectorAll(`.pill[data-filter="${key}"]`).forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      state.filters[key] = pill.dataset.value;
      saveState();
      const hash = window.location.hash.replace('#', '');
      const section = document.querySelector('.category-section');
      if (section && hash) applyFilters(section, hash);
    });
  });
  // Restore saved filter pills
  Object.entries(state.filters).forEach(([key, val]) => {
    const pill = panel.querySelector(`.pill[data-filter="${key}"][data-value="${val}"]`);
    if (pill) {
      panel.querySelectorAll(`.pill[data-filter="${key}"]`).forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
    }
  });
}

function refreshPictoItem(el, item) {
  const st   = getPictoState(item.id);
  const cBtn = el.querySelector('[data-picto-c]');
  const lBtn = el.querySelector('[data-picto-l]');
  if (cBtn) { cBtn.className = `toggle-p ${st === 'collected' || st === 'lumina' ? 'collected' : ''}`; cBtn.textContent = (st === 'collected' || st === 'lumina') ? '✓' : '○'; }
  if (lBtn) { lBtn.className = `toggle-p ${st === 'lumina' ? 'lumina' : ''}`; lBtn.textContent = st === 'lumina' ? '★' : 'L'; }
  el.classList.toggle('completed', st !== 'none');
}

// ── BOOT ──────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', async () => {
  await loadCategories();

  // Back button
  document.getElementById('btn-back').addEventListener('click', goHome);

  // Filter toggle
  document.getElementById('btn-filter').addEventListener('click', () => {
    document.getElementById('filter-panel').classList.toggle('open');
  });

  // Export
  document.getElementById('btn-export').addEventListener('click', exportProgress);

  // Filter pills
  initFilterPanel();

  // Hash routing
  window.addEventListener('hashchange', route);
  await route();
});
