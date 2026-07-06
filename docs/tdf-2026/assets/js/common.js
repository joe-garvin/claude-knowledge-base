// Shared front-end logic: data fetching, cache-busting, header/nav,
// local-timezone timestamp rendering, client-side staleness banner,
// and graceful handling of missing per-stage result files.

const STALE_HOURS = 26;

const STAGE_TYPE_LABELS = {
  flat: 'Flat',
  hilly: 'Hilly',
  mountain: 'Mountain',
  individual_time_trial: 'Individual time trial',
  team_time_trial: 'Team time trial',
};

export function stageTypeLabel(type) {
  return STAGE_TYPE_LABELS[type] || type;
}

export function pad2(n) {
  return String(n).padStart(2, '0');
}

// Display-layer unit conversion. All of data/*.json stays in metric — the
// canonical unit system professional cycling is measured and reported in,
// which every scraper source (letour.fr, PCS, Wikipedia) will always hand
// back regardless of this site's display preference. Converting only here,
// at render time, means every future scrape renders in imperial for free,
// with no per-source conversion logic to keep in sync.
const KM_TO_MI = 0.621371;
const M_TO_FT = 3.28084;

export function kmToMi(km) {
  return km * KM_TO_MI;
}

export function mToFt(m) {
  return m * M_TO_FT;
}

/** e.g. formatMiles(19.6) -> "12.2 mi" */
export function formatMiles(km, decimals = 1) {
  if (km == null) return '—';
  return `${kmToMi(km).toFixed(decimals)} mi`;
}

/** e.g. formatFeet(200) -> "656 ft" */
export function formatFeet(m) {
  if (m == null) return '—';
  return `${Math.round(mToFt(m)).toLocaleString()} ft`;
}

/** "21:47" (M:SS) or "3:40:01" (H:MM:SS) -> total seconds, or null. */
export function parseDurationToSeconds(timeStr) {
  if (!timeStr) return null;
  const parts = timeStr.split(':').map(Number);
  if (parts.some((p) => Number.isNaN(p))) return null;
  if (parts.length === 3) return parts[0] * 3600 + parts[1] * 60 + parts[2];
  if (parts.length === 2) return parts[0] * 60 + parts[1];
  return null;
}

/**
 * The stage winner's average speed: distance divided by their elapsed
 * time — not an average across the field. This is what "stage average
 * speed" always means in cycling reporting; callers should pass the
 * winner's (rank 1) time specifically. Returns e.g. "28.5 mph", or null
 * if either input is missing/unparseable (never renders a bogus number).
 */
export function formatAvgSpeedMph(distanceKm, timeStr) {
  const seconds = parseDurationToSeconds(timeStr);
  if (!seconds || !distanceKm) return null;
  const hours = seconds / 3600;
  const mph = kmToMi(distanceKm) / hours;
  return `${mph.toFixed(1)} mph`;
}

/**
 * Fetch meta.json with cache: 'no-store' so the freshness check always
 * sees the latest snapshot, never a browser- or CDN-cached copy.
 */
export async function loadMeta(dataRoot) {
  const res = await fetch(`${dataRoot}data/meta.json`, { cache: 'no-store' });
  if (!res.ok) throw new Error(`meta.json fetch failed: ${res.status}`);
  return res.json();
}

/**
 * Build a cache-busted URL for any other data file, keyed off meta's
 * last_updated so a new snapshot always invalidates the old cached copy.
 */
export function dataUrl(dataRoot, path, meta) {
  const v = encodeURIComponent(meta?.last_updated || '');
  return `${dataRoot}${path}?v=${v}`;
}

/**
 * Fetch a JSON data file and return null on any failure (404, network
 * error, bad JSON) instead of throwing, so callers can render a clean
 * "awaiting" state rather than letting a rejection propagate.
 */
export async function fetchJsonOrNull(url, options) {
  try {
    const res = await fetch(url, options);
    if (!res.ok) return null;
    return await res.json();
  } catch (err) {
    return null;
  }
}

export function isStale(meta) {
  if (!meta) return true;
  if (meta.scrape_status && meta.scrape_status !== 'ok') return true;
  const updated = new Date(meta.last_updated);
  if (Number.isNaN(updated.getTime())) return true;
  const ageHours = (Date.now() - updated.getTime()) / (1000 * 60 * 60);
  return ageHours > STALE_HOURS;
}

function formatLocal(isoString) {
  const d = new Date(isoString);
  if (Number.isNaN(d.getTime())) return { local: '—', paris: '—' };
  const local = new Intl.DateTimeFormat(undefined, {
    dateStyle: 'medium',
    timeStyle: 'short',
  }).format(d);
  const paris = new Intl.DateTimeFormat('en-GB', {
    dateStyle: 'medium',
    timeStyle: 'short',
    timeZone: 'Europe/Paris',
  }).format(d);
  return { local, paris };
}

/**
 * Format a date-only string ("YYYY-MM-DD", a race day rather than an
 * instant) so the calendar date shown always matches the stored value,
 * regardless of the viewer's timezone. Plain `new Date("2026-07-04")`
 * parses as UTC midnight, which renders as "Jul 3" for anyone west of
 * UTC if formatted in the local zone — this pins the format to UTC
 * instead so date-only values never shift by the viewer's offset.
 */
export function formatDateOnly(dateStr, opts = {}) {
  const d = new Date(`${dateStr}T00:00:00Z`);
  if (Number.isNaN(d.getTime())) return '—';
  return new Intl.DateTimeFormat(undefined, { ...opts, timeZone: 'UTC' }).format(d);
}

export function formatTimeOnly(isoString, timeZone) {
  const d = new Date(isoString);
  if (Number.isNaN(d.getTime())) return '—';
  const opts = { timeStyle: 'short' };
  if (timeZone) opts.timeZone = timeZone;
  return new Intl.DateTimeFormat(undefined, opts).format(d);
}

export function localZoneAbbrev(isoString) {
  const d = new Date(isoString);
  if (Number.isNaN(d.getTime())) return '';
  const parts = new Intl.DateTimeFormat(undefined, {
    timeZoneName: 'short',
    hour: 'numeric',
  }).formatToParts(d);
  const tz = parts.find((p) => p.type === 'timeZoneName');
  return tz ? tz.value : '';
}

function renderUpdatedLine(container, meta) {
  if (!container) return;
  if (!meta) {
    container.textContent = 'Last updated: unknown';
    return;
  }
  const { local, paris } = formatLocal(meta.last_updated);
  container.textContent = `Last updated ${local}`;
  container.title = `${paris} Europe/Paris time`;
}

function renderStaleBanner(container, meta) {
  if (!container) return;
  if (isStale(meta)) {
    const reason = meta && meta.scrape_status !== 'ok'
      ? `the last scrape reported "${meta.scrape_status}"`
      : 'the last successful update was more than 26 hours ago';
    container.textContent = `Showing the last known good data — ${reason}. This page will refresh automatically once a fresh scrape lands.`;
    container.classList.add('is-visible');
  } else {
    container.classList.remove('is-visible');
  }
}

const NAV_ITEMS = [
  { key: 'home', label: 'Home', file: 'overview.html' },
  { key: 'dashboard', label: 'Dashboard', file: 'index.html' },
];

/**
 * Wire the Stages menu as a click-to-toggle panel. Hover menus with a
 * gap between trigger and panel collapse before the cursor can reach a
 * link; and a right-anchored popover clips off-screen on narrow viewports.
 * Instead the menu is a full-width panel that drops in-flow under the
 * header — robust on desktop and touch alike, never clipping — and closes
 * on outside-click, Escape (returning focus to the button), or link choice.
 */
function wireStagesDropdown(container) {
  const btn = container.querySelector('.site-nav__stages-btn');
  const panel = container.querySelector('.site-nav__panel');
  if (!btn || !panel) return;

  const close = () => { container.classList.remove('stages-open'); btn.setAttribute('aria-expanded', 'false'); };
  const open = () => { container.classList.add('stages-open'); btn.setAttribute('aria-expanded', 'true'); };

  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    container.classList.contains('stages-open') ? close() : open();
  });
  document.addEventListener('click', (e) => {
    if (!container.classList.contains('stages-open')) return;
    if (!panel.contains(e.target) && e.target !== btn) close();
  });
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && container.classList.contains('stages-open')) { close(); btn.focus(); }
  });
  panel.addEventListener('click', () => close());
}

function renderHeader(container, { rootPath, active }) {
  if (!container) return;

  const stageLinks = [];
  for (let n = 1; n <= 21; n++) {
    const file = `stage-${pad2(n)}.html`;
    const href = rootPath === '' ? `stages/${file}` : file;
    stageLinks.push(`<a role="menuitem" href="${href}">Stage ${n}</a>`);
  }

  const navLinks = NAV_ITEMS.map((item) => {
    const href = `${rootPath}${item.file}`;
    const current = active === item.key ? ' aria-current="page"' : '';
    return `<a href="${href}"${current}>${item.label}</a>`;
  }).join('');

  container.innerHTML = `
    <div class="site-header__inner">
      <a class="site-title" href="${rootPath}index.html">Tour de France 2026 <span class="site-title__sub">— Joe's tracker</span></a>
      <nav class="site-nav" aria-label="Primary">
        ${navLinks}
        <button type="button" class="site-nav__stages-btn${active === 'stage' ? ' is-active' : ''}"
          aria-haspopup="true" aria-expanded="false" aria-controls="stages-menu">
          Stages <span class="site-nav__caret" aria-hidden="true">▾</span>
        </button>
      </nav>
    </div>
    <div class="site-nav__panel" id="stages-menu" role="menu">
      <div class="site-nav__panel-inner">${stageLinks.join('')}</div>
    </div>
  `;

  wireStagesDropdown(container);
}

/**
 * Shared page bootstrap: renders the header/nav, loads meta.json,
 * renders the updated timestamp + stale banner, and returns
 * { meta, dataRoot } for the page-specific renderer to use.
 *
 * @param {Object} opts
 * @param {''|'../'} opts.rootPath - prefix to reach the site root from this page
 * @param {'dashboard'|'overview'|'stage'} opts.active - which nav item to mark current
 */
export async function initCommon({ rootPath, active }) {
  const headerEl = document.getElementById('site-header');
  renderHeader(headerEl, { rootPath, active });

  const staleBannerEl = document.getElementById('stale-banner');
  const updatedEls = document.querySelectorAll('[data-updated-line]');

  let meta = null;
  try {
    meta = await loadMeta(rootPath);
  } catch (err) {
    meta = null;
  }

  updatedEls.forEach((el) => renderUpdatedLine(el, meta));
  renderStaleBanner(staleBannerEl, meta);

  return { meta, dataRoot: rootPath };
}

/**
 * Apply a hero photograph to an indigo hero band (dashboard hero card,
 * stage header, or overview title band). A dark indigo scrim is layered
 * over the image so white text stays legible, and a small credit caption
 * is appended for attribution.
 *
 * The image is preloaded first; it is only applied on successful load, so
 * a missing or broken image leaves the CSS solid-indigo fallback in place
 * — the hero never breaks (same principle as the stale-data fallback).
 *
 * @param {HTMLElement} el - the hero element (.hero-card / .stage-header / .page-hero)
 * @param {''|'../'} rootPath - prefix to reach the site root from this page
 * @param {{image:string, alt?:string, credit?:string, credit_url?:string}} img
 */
export function applyHeroImage(el, rootPath, img) {
  if (!el || !img || !img.image) return;
  const url = `${rootPath}${img.image}`;
  const scrim = 'linear-gradient(180deg, rgba(20,27,72,0.34) 0%, rgba(17,22,58,0.72) 74%, rgba(14,19,50,0.86) 100%)';
  const pre = new Image();
  pre.onload = () => {
    el.style.backgroundImage = `${scrim}, url("${url}")`;
    el.style.backgroundSize = 'cover';
    el.style.backgroundPosition = 'center';
    el.classList.add('has-photo');
    if (img.credit && !el.querySelector('.hero-credit')) {
      const hasLink = Boolean(img.credit_url);
      const credit = document.createElement(hasLink ? 'a' : 'span');
      credit.className = 'hero-credit';
      credit.textContent = `📷 ${img.credit}`;
      if (hasLink) {
        credit.href = img.credit_url;
        credit.target = '_blank';
        credit.rel = 'noopener';
      }
      el.appendChild(credit);
    }
  };
  pre.src = url;
}

/** Small inline jersey icon, colored per classification. */
export function jerseyIconSvg(colorVar) {
  return `
    <svg viewBox="0 0 40 40" class="jersey-card__icon" role="img" aria-hidden="true">
      <path d="M12 4 L4 12 L9 17 L12 14 L12 36 L28 36 L28 14 L31 17 L36 12 L28 4 L24 8 L16 8 Z"
        fill="${colorVar}" stroke="var(--color-text)" stroke-width="1" stroke-opacity="0.15" />
    </svg>
  `;
}
