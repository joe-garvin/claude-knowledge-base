import {
  initCommon, dataUrl, fetchJsonOrNull, stageTypeLabel, pad2,
  formatTimeOnly, localZoneAbbrev, jerseyIconSvg, formatDateOnly,
} from './common.js';

const JERSEY_META = {
  gc: { label: 'General classification', jersey: 'Yellow jersey', colorVar: 'var(--jersey-yellow)', cls: 'gc' },
  points: { label: 'Points classification', jersey: 'Green jersey', colorVar: 'var(--jersey-green)', cls: 'points' },
  kom: { label: 'Mountains classification', jersey: 'Polka dot jersey', colorVar: 'var(--jersey-polka)', cls: 'kom' },
  youth: { label: 'Young rider classification', jersey: 'White jersey', colorVar: 'var(--jersey-white)', cls: 'youth' },
};

function todayIso() {
  const d = new Date();
  return `${d.getFullYear()}-${pad2(d.getMonth() + 1)}-${pad2(d.getDate())}`;
}

function renderStatusStrip(race) {
  const el = document.getElementById('status-strip');
  if (!race) {
    el.innerHTML = '<p class="muted">Race data unavailable.</p>';
    return;
  }
  const today = todayIso();
  const isRestDay = (race.rest_days || []).includes(today);
  const stageToday = (race.stages || []).find((s) => s.date === today);
  const raceStarted = today >= race.start_date;
  const raceEnded = today > race.end_date;

  let statusLabel = 'No stage today';
  if (isRestDay) statusLabel = 'Rest day';
  else if (stageToday) statusLabel = `Stage ${stageToday.number} today`;
  else if (!raceStarted) statusLabel = 'Race not yet started';
  else if (raceEnded) statusLabel = 'Race finished';

  const dateLabel = new Intl.DateTimeFormat(undefined, { dateStyle: 'full' }).format(new Date());

  el.innerHTML = `
    <div class="status-strip__item"><strong>${dateLabel}</strong>Today</div>
    <div class="status-strip__item"><strong>${statusLabel}</strong>${isRestDay ? '<span class="badge badge--rest">Rest day</span>' : ''}</div>
    <div class="status-strip__item"><strong>${race.edition} edition</strong>${race.grand_depart} → ${race.finish}</div>
  `;
}

function pickHeroStage(race) {
  const today = todayIso();
  const stages = race.stages || [];
  const todayStage = stages.find((s) => s.date === today);
  if (todayStage) return todayStage;
  const next = stages.find((s) => s.date > today);
  if (next) return next;
  return stages[stages.length - 1] || null;
}

function renderSparkline(canvasId, points) {
  const canvas = document.getElementById(canvasId);
  if (!canvas || !window.Chart || !points || !points.length) return;
  new window.Chart(canvas, {
    type: 'line',
    data: {
      labels: points.map((p) => p.km),
      datasets: [{
        data: points.map((p) => p.elevation_m),
        borderColor: '#8a9a5b',
        backgroundColor: 'rgba(138,154,91,0.15)',
        fill: true,
        pointRadius: 0,
        borderWidth: 1.5,
        tension: 0.15,
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { display: false }, tooltip: { enabled: false } },
      scales: {
        x: { display: false },
        y: { display: false },
      },
    },
  });
}

function renderHero(dataRoot, meta, race, watch) {
  const el = document.getElementById('hero-card');
  const stage = pickHeroStage(race);
  if (!stage) {
    el.innerHTML = '<p class="muted">No stage data available.</p>';
    return;
  }
  const w = (watch?.stages || []).find((s) => s.number === stage.number);
  const stageHref = `stages/stage-${pad2(stage.number)}.html`;

  let watchHtml = '';
  if (w) {
    const localStart = formatTimeOnly(w.start_utc);
    const localZone = localZoneAbbrev(w.start_utc);
    const parisStart = formatTimeOnly(w.start_utc, 'Europe/Paris');
    const localFinish = formatTimeOnly(w.est_finish_utc);
    watchHtml = `
      <dl class="hero-card__watch">
        <div><dt>Start (yours)</dt><dd>${localStart} ${localZone}</dd></div>
        <div><dt>Start (Paris)</dt><dd>${parisStart} CEST</dd></div>
        <div><dt>Est. finish (yours)</dt><dd>${localFinish} ${localZone}</dd></div>
      </dl>
    `;
  }

  el.innerHTML = `
    <div>
      <span class="type-badge type-badge--${stage.type}">${stageTypeLabel(stage.type)}</span>
      <span class="muted"> · Stage ${stage.number} · ${formatDateOnly(stage.date, { dateStyle: 'medium' })}</span>
    </div>
    <a class="hero-card__route" href="${stageHref}">${stage.start} → ${stage.finish}</a>
    <div class="hero-card__meta">
      <span>${stage.distance_km} km</span>
      <span>${stage.elevation_gain_m} m elevation</span>
      ${stage.summit_finish ? '<span>Summit finish</span>' : ''}
    </div>
    <div class="chart-wrap" style="height:100px;">
      <canvas id="hero-sparkline"></canvas>
    </div>
    ${watchHtml}
    <p><a href="${stageHref}">Full stage page →</a></p>
  `;
  renderSparkline('hero-sparkline', stage.profile?.points);
}

function renderJerseyCards(standings) {
  const el = document.getElementById('jersey-cards');
  const classifications = standings?.classifications || {};
  el.innerHTML = Object.entries(JERSEY_META).map(([key, m]) => {
    const list = classifications[key] || [];
    const leader = list[0];
    const detail = !leader ? 'Awaiting stage 1'
      : key === 'gc' || key === 'youth'
        ? `${leader.team || ''} · ${leader.gap || '—'}`
        : `${leader.team || ''} · ${leader.points ?? '—'} pts`;
    return `
      <div class="card jersey-card jersey-card--${m.cls}">
        ${jerseyIconSvg(m.colorVar)}
        <div>
          <div class="jersey-card__label">${m.jersey}</div>
          <div class="jersey-card__name">${leader ? leader.rider : '—'}</div>
          <div class="jersey-card__detail">${detail}</div>
        </div>
      </div>
    `;
  }).join('');
}

function renderGcTable(standings) {
  const tbody = document.querySelector('#gc-table tbody');
  const gc = (standings?.classifications?.gc || []).slice(0, 5);
  if (!gc.length) {
    tbody.innerHTML = '<tr><td colspan="4" class="muted">Awaiting stage 1.</td></tr>';
    return;
  }
  tbody.innerHTML = gc.map((r) => `
    <tr>
      <td class="num">${r.rank}</td>
      <td>${r.rider}</td>
      <td>${r.team}</td>
      <td class="num">${r.gap}</td>
    </tr>
  `).join('');
}

async function renderLastResult(dataRoot, meta, race, standings) {
  const el = document.getElementById('last-result-card');
  const asOf = standings?.as_of_stage || 0;
  if (!asOf) {
    el.innerHTML = '<p class="muted">Awaiting the first stage.</p>';
    return;
  }
  const url = dataUrl(dataRoot, `data/results/stage-${pad2(asOf)}.json`, meta);
  const result = await fetchJsonOrNull(url);
  if (!result || !result.completed) {
    el.innerHTML = '<p class="muted">Awaiting the first stage.</p>';
    return;
  }
  const stage = (race?.stages || []).find((s) => s.number === result.stage);
  const top3 = (result.top10 || []).slice(0, 3);
  el.innerHTML = `
    <p class="muted">Stage ${result.stage}${stage ? ` — ${stage.start} → ${stage.finish}` : ''}</p>
    <div class="table-wrap">
      <table>
        <thead><tr><th class="num">Rank</th><th>Rider</th><th>Team</th><th class="num">Gap</th></tr></thead>
        <tbody>
          ${top3.map((r) => `<tr><td class="num">${r.rank}</td><td>${r.rider}</td><td>${r.team}</td><td class="num">${r.gap}</td></tr>`).join('')}
        </tbody>
      </table>
    </div>
    <p><a href="stages/stage-${pad2(result.stage)}.html">Full result →</a></p>
  `;
}

function renderStageStrip(race, standings) {
  const el = document.getElementById('stage-strip');
  const asOf = standings?.as_of_stage || 0;
  el.innerHTML = (race?.stages || []).map((s) => {
    const completed = s.number <= asOf;
    return `
      <a class="stage-strip__cell stage-strip__cell--${s.type}${completed ? ' stage-strip__cell--completed' : ''}"
         href="stages/stage-${pad2(s.number)}.html" title="${s.start} → ${s.finish}">
        <strong>${s.number}</strong>
        <span>${formatDateOnly(s.date, { month: 'short', day: 'numeric' })}</span>
      </a>
    `;
  }).join('');
}

async function main() {
  const { meta, dataRoot } = await initCommon({ rootPath: '', active: 'dashboard' });

  const race = await fetchJsonOrNull(dataUrl(dataRoot, 'data/race.json', meta));
  const standings = await fetchJsonOrNull(dataUrl(dataRoot, 'data/standings.json', meta));
  const watch = await fetchJsonOrNull(dataUrl(dataRoot, 'data/watch.json', meta));

  renderStatusStrip(race);
  if (race) renderHero(dataRoot, meta, race, watch);
  renderJerseyCards(standings);
  renderGcTable(standings);
  await renderLastResult(dataRoot, meta, race, standings);
  renderStageStrip(race, standings);
}

main();
