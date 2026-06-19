const API_BASE = "http://127.0.0.1:8000";

async function loadChart() {
  const res = await fetch(`${API_BASE}/api/stats`);
  const data = await res.json();
  const stats = data.stats;

  const labels = stats.map(s => s.date);
  const indiaCounts = stats.map(s => s.india_count);
  const globalCounts = stats.map(s => s.global_count);

  const ctx = document.getElementById("newsChart").getContext("2d");
  new Chart(ctx, {
    type: "line",
    data: {
      labels: labels,
      datasets: [
        {
          label: "India News",
          data: indiaCounts,
          borderColor: "#ff6600",
          backgroundColor: "rgba(255,102,0,0.1)",
          fill: true,
          tension: 0.4
        },
        {
          label: "Global News",
          data: globalCounts,
          borderColor: "#0066cc",
          backgroundColor: "rgba(0,102,204,0.1)",
          fill: true,
          tension: 0.4
        }
      ]
    },
    options: {
      responsive: true,
      plugins: {
        legend: { position: "top" }
      },
      scales: {
        y: { beginAtZero: true }
      }
    }
  });
}

async function loadSummary() {
  const res = await fetch(`${API_BASE}/api/summary`);
  const data = await res.json();

  document.getElementById("summary-date").textContent = `Date: ${data.date}`;
  document.getElementById("summary-text").textContent = data.summary;
  document.getElementById("overview-text").textContent = data.overview;
}

loadChart();
loadSummary();