// Kleine Wetter-App ohne Framework.
// Idee: Wir haben 3 Zustände (Loading / Error / Success) und rendern danach.

const cityInput = document.getElementById("cityInput");
const loadBtn = document.getElementById("loadBtn");
const output = document.getElementById("output");

// Mini-State (so wenig wie möglich)
let isLoading = false;
let error = null;
let weather = null;

loadBtn.addEventListener("click", () => {
  const city = cityInput.value.trim();
  loadWeather(city);
});

// Optional: Enter-Taste soll auch laden (fühlt sich „normal“ an)
cityInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") loadBtn.click();
});

async function loadWeather(city) {
  // 1) bisschen Eingabe-Check, damit wir keine leeren Requests senden
  if (!city) {
    error = "Bitte eine Stadt eingeben.";
    weather = null;
    render();
    return;
  }

  // 2) Loading-State setzen (damit der Nutzer Feedback bekommt)
  isLoading = true;
  error = null;
  weather = null;
  render();

  try {
    // wttr.in ist super für Demos: keine API-Keys, direkt JSON möglich
    const url = "https://wttr.in/" + encodeURIComponent(city) + "?format=j1";

    const response = await fetch(url);

    // Wichtig: fetch wirft bei 404/500 NICHT automatisch einen Fehler.
    // Deshalb prüfen wir response.ok selbst.
    if (!response.ok) {
      throw new Error("HTTP Fehler: " + response.status);
    }

    const data = await response.json();

    // Aus dem JSON holen wir nur das, was wir wirklich anzeigen wollen.
    // (Sonst wird’s unnötig kompliziert.)
    const current = data.current_condition?.[0];
    if (!current) {
      throw new Error("Keine Wetterdaten gefunden (Format unerwartet).");
    }

    weather = {
      city: data.nearest_area?.[0]?.areaName?.[0]?.value ?? city,
      tempC: current.temp_C,
      feelsC: current.FeelsLikeC,
      desc: current.weatherDesc?.[0]?.value ?? "—",
      humidity: current.humidity,
      windKmh: current.windspeedKmph,
    };
  } catch (e) {
    // Hier landen Netzwerkfehler, unsere eigenen throw Errors, JSON-Probleme, usw.
    error = e.message;
  } finally {
    // 3) Egal ob Erfolg oder Fehler: Loading ist vorbei
    isLoading = false;
    render();
  }
}

function render() {
  loadBtn.disabled = isLoading;

  if (isLoading) {
    output.innerHTML = `<div class="loading">Lade Wetterdaten…</div>`;
    return;
  }

  if (error) {
    output.innerHTML = `
      <div class="error">
        <strong>Fehler:</strong> ${escapeHtml(error)}
        <div class="small">Tipp: Stadtname prüfen oder später nochmal versuchen.</div>
      </div>
    `;
    return;
  }

  if (weather) {
    output.innerHTML = `
      <div class="result">
        <h2 style="margin:0 0 8px;">${escapeHtml(weather.city)}</h2>
        <div><strong>${escapeHtml(weather.desc)}</strong></div>
        <div class="small">
          Temperatur: ${weather.tempC}°C (fühlt sich an wie ${weather.feelsC}°C)<br/>
          Luftfeuchtigkeit: ${weather.humidity}%<br/>
          Wind: ${weather.windKmh} km/h
        </div>
      </div>
    `;
    return;
  }

  // Startzustand
  output.innerHTML = `<div class="small">Gib eine Stadt ein und klicke auf „Laden“.</div>`;
}

// Kleiner Sicherheits-Helper: macht Texte HTML-sicher
function escapeHtml(str) {
  return String(str)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

// Direkt einmal initial rendern
render();
