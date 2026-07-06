import {
  initCommon, dataUrl, fetchJsonOrNull, stageTypeLabel, pad2,
  formatTimeOnly, localZoneAbbrev, formatDateOnly, applyHeroImage,
  kmToMi, mToFt, formatMiles, formatFeet, formatAvgSpeedMph,
} from './common.js';

const stageNumber = Number(document.body.dataset.stage);

function renderHeader(stage, watch) {
  const el = document.getElementById('stage-header');
  if (!stage) {
    el.innerHTML = '<p class="muted">Stage data unavailable.</p>';
    return;
  }
  const dateLabel = formatDateOnly(stage.date, { dateStyle: 'full' });

  let watchHtml = '';
  if (watch) {
    const localStart = formatTimeOnly(watch.start_utc);
    const localZone = localZoneAbbrev(watch.start_utc);
    const parisStart = formatTimeOnly(watch.start_utc, 'Europe/Paris');
    const localFinish = formatTimeOnly(watch.est_finish_utc);
    const parisFinish = formatTimeOnly(watch.est_finish_utc, 'Europe/Paris');
    watchHtml = `
      <dl class="hero-card__watch">
        <div><dt>Start (yours)</dt><dd>${localStart} ${localZone}</dd></div>
        <div><dt>Start (Paris)</dt><dd>${parisStart} CEST</dd></div>
        <div><dt>Est. finish (yours)</dt><dd>${localFinish} ${localZone}</dd></div>
        <div><dt>Est. finish (Paris)</dt><dd>${parisFinish} CEST</dd></div>
      </dl>
    `;
  }

  document.title = `Stage ${stage.number}: ${stage.start} → ${stage.finish} — Tour de France 2026 tracker`;

  el.innerHTML = `
    <p class="stage-header__eyebrow">Stage ${stage.number} · ${dateLabel}</p>
    <h1 class="stage-header__route">${stage.start} → ${stage.finish}</h1>
    <div class="stage-header__meta">
      <span class="type-badge type-badge--${stage.type}">${stageTypeLabel(stage.type)}</span>
      <span>${formatMiles(stage.distance_km)}</span>
      <span>${formatFeet(stage.elevation_gain_m)} elevation</span>
      ${stage.summit_finish ? '<span class="badge">Summit finish</span>' : ''}
    </div>
    ${watchHtml}
  `;
}

function renderPreview(stage) {
  const el = document.getElementById('stage-preview');
  el.textContent = stage?.preview || 'No preview available for this stage yet.';
}

function renderProfileChart(stage) {
  const canvas = document.getElementById('profile-chart');
  if (!stage || !window.Chart) return;
  const points = stage.profile?.points || [];
  const climbs = stage.profile?.climbs || [];

  const annotations = {};
  climbs.forEach((c, i) => {
    // Must use the same km -> mi conversion as the profile points below,
    // or the annotation line drifts out of alignment with the curve.
    const xMi = kmToMi(c.km_mark);
    annotations[`climb-${i}`] = {
      type: 'line',
      xMin: xMi,
      xMax: xMi,
      borderColor: '#c8443a',
      borderWidth: 1,
      borderDash: [4, 3],
      label: {
        display: true,
        content: `${c.name}${c.category ? ` (Cat ${c.category})` : ''}`,
        position: 'start',
        rotation: 90,
        font: { size: 10 },
        backgroundColor: 'rgba(255,255,255,0.92)',
        color: '#1a1a1a',
      },
    };
  });

  new window.Chart(canvas, {
    type: 'line',
    data: {
      datasets: [{
        label: 'Elevation',
        data: points.map((p) => ({ x: kmToMi(p.km), y: mToFt(p.elevation_m) })),
        borderColor: '#0075de',
        backgroundColor: 'rgba(0,117,222,0.10)',
        fill: true,
        pointRadius: 0,
        borderWidth: 1.5,
        tension: 0.2,
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            title: (items) => `${items[0]?.parsed?.x?.toFixed(1) ?? ''} mi`,
            label: (item) => `${Math.round(item.parsed.y).toLocaleString()} ft`,
          },
        },
        annotation: { annotations },
      },
      scales: {
        x: {
          type: 'linear',
          title: { display: true, text: 'Miles' },
          grid: { color: '#e6e6e6' },
        },
        y: {
          title: { display: true, text: 'Elevation (ft)' },
          grid: { color: '#e6e6e6' },
        },
      },
    },
  });
}

function renderClimbsTable(stage) {
  const tbody = document.querySelector('#climbs-table tbody');
  const emptyEl = document.getElementById('climbs-empty');
  const climbs = stage?.profile?.climbs || [];
  if (!climbs.length) {
    document.getElementById('climbs-table').style.display = 'none';
    emptyEl.style.display = 'block';
    return;
  }
  tbody.innerHTML = climbs.map((c) => `
    <tr>
      <td>${c.name}</td>
      <td>${c.category ?? '—'}</td>
      <td class="num">${c.km_mark != null ? kmToMi(c.km_mark).toFixed(1) : '—'}</td>
      <td class="num">${c.length_km != null ? formatMiles(c.length_km) : '—'}</td>
      <td class="num">${c.avg_gradient != null ? `${c.avg_gradient}%` : '—'}</td>
    </tr>
  `).join('');
}

function renderResult(stage, result, highlights) {
  const el = document.getElementById('result-card');
  if (!result || !result.completed) {
    const dateLabel = stage ? formatDateOnly(stage.date, { dateStyle: 'long' }) : '';
    el.innerHTML = `<div class="awaiting-block">Awaiting stage — runs ${dateLabel || 'soon'}.</div>`;
    return;
  }
  const rows = (result.top10 || []).map((r) => `
    <tr>
      <td class="num">${r.rank}</td>
      <td>${r.rider}</td>
      <td>${r.team}</td>
      <td class="num">${r.time}</td>
      <td class="num">${r.gap}</td>
    </tr>
  `).join('');

  const jw = result.jersey_wearers_after || {};
  const jerseyList = [
    ['Yellow', jw.gc],
    ['Green', jw.points],
    ['Polka dot', jw.kom],
    ['White', jw.youth],
  ].filter(([, name]) => name).map(([label, name]) => `<li><strong>${label}:</strong> ${name}</li>`).join('');

  const highlightsHtml = highlights
    ? `<a class="highlights-link" href="${highlights.url}" target="_blank" rel="noopener">
        <span class="highlights-link__icon" aria-hidden="true">▶</span>
        ${highlights.label || 'Watch stage highlights'}
      </a>`
    : '';

  const winnerTime = result.top10?.[0]?.time;
  const avgSpeed = stage ? formatAvgSpeedMph(stage.distance_km, winnerTime) : null;
  const avgSpeedHtml = avgSpeed ? `<p class="result-avg-speed muted">Average speed: <strong>${avgSpeed}</strong></p>` : '';

  el.innerHTML = `
    ${avgSpeedHtml}
    <div class="table-wrap">
      <table>
        <thead><tr><th class="num">Rank</th><th>Rider</th><th>Team</th><th class="num">Time</th><th class="num">Gap</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
    </div>
    ${jerseyList ? `<h3>Jersey wearers after this stage</h3><ul>${jerseyList}</ul>` : ''}
    ${highlightsHtml}
  `;
}

function renderStageNav(race) {
  const el = document.getElementById('stage-nav');
  const prev = stageNumber > 1 ? `<a href="stage-${pad2(stageNumber - 1)}.html">← Stage ${stageNumber - 1}</a>` : '<span></span>';
  const next = stageNumber < 21 ? `<a href="stage-${pad2(stageNumber + 1)}.html">Stage ${stageNumber + 1} →</a>` : '<span></span>';
  el.innerHTML = `${prev}<a href="../overview.html">All stages</a>${next}`;
}

async function main() {
  const { meta, dataRoot } = await initCommon({ rootPath: '../', active: 'stage' });

  const race = await fetchJsonOrNull(dataUrl(dataRoot, 'data/race.json', meta));
  const watchData = await fetchJsonOrNull(dataUrl(dataRoot, 'data/watch.json', meta));
  const result = await fetchJsonOrNull(dataUrl(dataRoot, `data/results/stage-${pad2(stageNumber)}.json`, meta));
  const images = await fetchJsonOrNull(dataUrl(dataRoot, 'data/images.json', meta));
  const highlightsData = await fetchJsonOrNull(dataUrl(dataRoot, 'data/highlights.json', meta));

  const stage = race?.stages?.find((s) => s.number === stageNumber) || null;
  const watch = watchData?.stages?.find((s) => s.number === stageNumber) || null;
  const highlights = highlightsData?.stages?.[stageNumber] || null;

  renderHeader(stage, watch);
  applyHeroImage(document.getElementById('stage-header'), dataRoot, images?.stages?.[stageNumber]);
  renderPreview(stage);
  if (stage) renderProfileChart(stage);
  renderClimbsTable(stage);
  renderResult(stage, result, highlights);
  renderStageNav(race);
}

main();
