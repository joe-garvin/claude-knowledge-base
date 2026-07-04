import { initCommon, dataUrl, fetchJsonOrNull, stageTypeLabel, pad2, formatDateOnly, applyHeroImage } from './common.js';

// Kept in sync with the --type-* custom properties in site.css.
const TYPE_COLORS = {
  flat: '#1aae39',
  hilly: '#dd5b00',
  mountain: '#c8443a',
  individual_time_trial: '#2a9d99',
  team_time_trial: '#2a9d99',
};

function renderSubtitle(race) {
  const el = document.getElementById('race-subtitle');
  if (!race) {
    el.textContent = 'Race data unavailable.';
    return;
  }
  const start = formatDateOnly(race.start_date, { dateStyle: 'long' });
  const end = formatDateOnly(race.end_date, { dateStyle: 'long' });
  el.textContent = `${race.edition} edition · ${race.grand_depart} → ${race.finish} · ${start} – ${end}`;
}

function renderTotals(race) {
  const el = document.getElementById('totals-grid');
  if (!race) return;
  const t = race.totals;
  const typeCounts = {};
  race.stages.forEach((s) => { typeCounts[s.type] = (typeCounts[s.type] || 0) + 1; });
  const items = [
    ['Stages', t.stages],
    ['Distance', `${t.distance_km.toLocaleString()} km`],
    ['Elevation gain', `${t.elevation_gain_m.toLocaleString()} m`],
    ['Rest days', race.rest_days.length],
    ['Mountain stages', typeCounts.mountain || 0],
    ['Flat stages', typeCounts.flat || 0],
    ['Hilly stages', typeCounts.hilly || 0],
    ['Time trials', (typeCounts.individual_time_trial || 0) + (typeCounts.team_time_trial || 0)],
  ];
  el.innerHTML = items.map(([label, value]) => `
    <div class="card totals-grid__item">
      <strong>${value}</strong>
      <span>${label}</span>
    </div>
  `).join('');
}

function renderElevationChart(race) {
  if (!race || !window.Chart) return;
  const canvas = document.getElementById('elevation-chart');
  new window.Chart(canvas, {
    type: 'bar',
    data: {
      labels: race.stages.map((s) => `S${s.number}`),
      datasets: [{
        data: race.stages.map((s) => s.elevation_gain_m),
        backgroundColor: race.stages.map((s) => TYPE_COLORS[s.type] || '#928c7d'),
        borderRadius: 2,
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            title: (items) => {
              const s = race.stages[items[0].dataIndex];
              return `Stage ${s.number}: ${s.start} → ${s.finish}`;
            },
            label: (item) => `${item.raw} m elevation gain — ${stageTypeLabel(race.stages[item.dataIndex].type)}`,
          },
        },
      },
      scales: {
        x: { grid: { display: false } },
        y: { grid: { color: '#e6e6e6' }, title: { display: true, text: 'metres' } },
      },
    },
  });
}

function renderGcHistoryChart(standings) {
  const canvas = document.getElementById('gc-history-chart');
  const emptyEl = document.getElementById('gc-history-empty');
  const history = standings?.history?.gc_leader_by_stage || [];
  if (!history.length || !window.Chart) {
    canvas.closest('.chart-wrap').style.display = 'none';
    emptyEl.style.display = 'block';
    return;
  }
  emptyEl.style.display = 'none';
  const riders = [...new Set(history.map((h) => h.rider))];
  new window.Chart(canvas, {
    type: 'line',
    data: {
      labels: history.map((h) => `Stage ${h.stage}`),
      datasets: [{
        data: history.map((h) => riders.indexOf(h.rider)),
        stepped: true,
        borderColor: '#e8b800',
        borderWidth: 2,
        pointRadius: 3,
        pointBackgroundColor: '#e8b800',
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: (item) => history[item.dataIndex].rider } },
      },
      scales: {
        y: {
          ticks: { callback: (v) => riders[v] || '' },
          reverse: true,
        },
      },
    },
  });
}

function renderRouteSchematic(race) {
  const el = document.getElementById('route-schematic');
  if (!race) return;
  const items = [];
  race.stages.forEach((s) => {
    items.push(`<div class="route-schematic__item">Stage ${s.number} — ${s.start} → ${s.finish} <span class="faint">(${s.distance_km} km)</span></div>`);
    if (race.rest_days.includes(nextDay(s.date))) {
      items.push(`<div class="route-schematic__item route-schematic__item--rest">Rest day</div>`);
    }
  });
  el.innerHTML = items.join('');
}

function nextDay(dateStr) {
  const d = new Date(`${dateStr}T00:00:00Z`);
  d.setUTCDate(d.getUTCDate() + 1);
  return d.toISOString().slice(0, 10);
}

function renderStageTable(race) {
  const tbody = document.querySelector('#stage-table tbody');
  if (!race) return;
  tbody.innerHTML = race.stages.map((s) => `
    <tr onclick="location.href='stages/stage-${pad2(s.number)}.html'" style="cursor:pointer;">
      <td class="num">${s.number}</td>
      <td>${formatDateOnly(s.date, { month: 'short', day: 'numeric' })}</td>
      <td><a href="stages/stage-${pad2(s.number)}.html">${s.start} → ${s.finish}</a></td>
      <td><span class="type-badge type-badge--${s.type}">${stageTypeLabel(s.type)}</span></td>
      <td class="num">${s.distance_km} km</td>
      <td class="num">${s.elevation_gain_m} m</td>
      <td>${s.summit_finish ? 'Yes' : ''}</td>
    </tr>
  `).join('');
}

async function main() {
  const { meta, dataRoot } = await initCommon({ rootPath: '', active: 'overview' });
  const race = await fetchJsonOrNull(dataUrl(dataRoot, 'data/race.json', meta));
  const standings = await fetchJsonOrNull(dataUrl(dataRoot, 'data/standings.json', meta));
  const images = await fetchJsonOrNull(dataUrl(dataRoot, 'data/images.json', meta));

  renderSubtitle(race);
  applyHeroImage(document.querySelector('.page-hero'), dataRoot, images?.overview);
  renderTotals(race);
  renderElevationChart(race);
  renderGcHistoryChart(standings);
  renderRouteSchematic(race);
  renderStageTable(race);
}

main();
