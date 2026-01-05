# CSS Layout & Responsive - Praktische Übungen

## Übersicht

In dieser Übung vertiefst du dein Wissen über:
- **Flexbox** - Eindimensionales Layout (eine Richtung)
- **CSS Grid** - Zweidimensionales Layout (Zeilen UND Spalten)
- **Responsive Design** - Layouts für alle Bildschirmgrößen
- **Media Queries** - Breakpoints definieren
- **DevTools** - Layout-Debugging mit Responsive Mode

Diese Übung baut auf den vorherigen Tagen auf und bereitet dich auf das Freitags-Projekt vor.

---

## Teil 1: Flexbox vs. Grid - Die richtige Wahl

### Wann was verwenden?

| Flexbox | Grid |
|---------|------|
| **Eindimensional** | **Zweidimensional** |
| Elemente in EINER Richtung | Elemente in Zeilen UND Spalten |
| Row (Zeile) ODER Column (Spalte) | Echtes Raster mit definierten Bahnen |

### Typische Use Cases

**Flexbox:**
- Navigation / Header-Leiste
- Button-Gruppen nebeneinander
- Zentrierung (horizontal & vertikal)
- Elemente mit flexiblen Breiten

**Grid:**
- Kartenraster (3x3, 4x2, etc.)
- 2-Spalten-Layout (Content + Sidebar)
- Dashboard-Layouts
- Foto-Galerien

### Wissensfrage 1

Du möchtest eine Navigation erstellen: Logo links, Menü-Links rechts. Flexbox oder Grid?

<details>
<summary>Antwort anzeigen</summary>

**Flexbox!**

Begründung:
- Es ist ein eindimensionales Layout (eine Zeile)
- `justify-content: space-between` verteilt Logo und Links perfekt
- Flexbox ist ideal für Komponenten wie Navigationen

```css
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

</details>

---

## Teil 2: Flexbox - Die wichtigsten Eigenschaften

### Container-Eigenschaften (Parent)

```css
.container {
  display: flex;           /* Flexbox aktivieren */
  flex-direction: row;     /* row | column */
  justify-content: center; /* Hauptachse */
  align-items: center;     /* Querachse */
  gap: 20px;               /* Abstand zwischen Items */
  flex-wrap: wrap;         /* Items umbrechen erlauben */
}
```

### Visualisierung

**flex-direction:**
```
row (Standard):     [1] [2] [3] →

column:             [1]
                    [2]
                    [3]
                    ↓
```

**justify-content (Hauptachse):**
```
flex-start:    [1][2][3]
center:           [1][2][3]
flex-end:                [1][2][3]
space-between: [1]    [2]    [3]
space-around:   [1]  [2]  [3]
space-evenly:  [1]  [2]  [3]
```

**align-items (Querachse):**
```
flex-start:    [1] [2] [3]    (oben)
center:        [1] [2] [3]    (mitte)
flex-end:      [1] [2] [3]    (unten)
stretch:       [===] [===]    (gestreckt)
```

### Item-Eigenschaften (Children)

```css
.item {
  flex: 1;         /* Item wächst flexibel */
  flex-grow: 1;    /* Wie viel vom freien Platz nehmen */
  flex-shrink: 0;  /* Ob/wie viel schrumpfen */
  flex-basis: auto; /* Ausgangsgröße */
}
```

---

## Teil 3: Übung - Navigation mit Flexbox

### Aufgabe

Erstelle eine responsive Navigation:
1. Logo links
2. Menü-Links rechts
3. Vertikal zentriert
4. Dunkler Hintergrund

**HTML-Struktur:**
```html
<nav class="navbar">
  <div class="logo">DevApp</div>
  <ul class="nav-links">
    <li><a href="#">Home</a></li>
    <li><a href="#">About</a></li>
    <li><a href="#">Contact</a></li>
  </ul>
</nav>
```

<details>
<summary>Musterlösung anzeigen</summary>

```css
/* Navigation Container */
.navbar {
  display: flex;
  justify-content: space-between;  /* Logo links, Links rechts */
  align-items: center;             /* Vertikal zentriert */
  padding: 1rem 2rem;
  background-color: #1a1a2e;
}

/* Logo */
.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
}

/* Navigation Links Container */
.nav-links {
  display: flex;        /* Auch die Links als Flexbox */
  gap: 30px;            /* Abstand zwischen Links */
  list-style: none;
  margin: 0;
  padding: 0;
}

/* Einzelne Links */
.nav-links a {
  color: white;
  text-decoration: none;
  transition: color 0.2s ease;
}

.nav-links a:hover {
  color: #aaaaaa;
}
```

**Erklärung:**
- `justify-content: space-between` schiebt Logo und Links auseinander
- `align-items: center` zentriert vertikal
- Die `nav-links` sind selbst auch ein Flex-Container mit `gap`

</details>

---

## Teil 4: Übung - Zentrierte Inhalte mit Flexbox

### Aufgabe

Zentriere einen Content-Block horizontal UND vertikal auf der Seite:

**HTML:**
```html
<div class="hero">
  <div class="hero-content">
    <h1>Willkommen</h1>
    <p>Dies ist meine Portfolio-Seite.</p>
    <button>Mehr erfahren</button>
  </div>
</div>
```

**Anforderungen:**
- Der Hero-Bereich soll die volle Viewport-Höhe haben
- Der Inhalt soll exakt in der Mitte sein

<details>
<summary>Musterlösung anzeigen</summary>

```css
.hero {
  /* Volle Viewport-Höhe */
  min-height: 100vh;

  /* Flexbox für Zentrierung */
  display: flex;
  justify-content: center;  /* Horizontal */
  align-items: center;      /* Vertikal */

  /* Optionale Styling */
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  color: white;
  text-align: center;
}

.hero-content {
  max-width: 600px;
  padding: 2rem;
}

.hero h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.hero p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
}

.hero button {
  background-color: #0066cc;
  color: white;
  border: none;
  padding: 1rem 2rem;
  font-size: 1rem;
  cursor: pointer;
  border-radius: 4px;
}
```

**Die magische Kombination für Zentrierung:**
```css
display: flex;
justify-content: center;
align-items: center;
```

</details>

---

## Teil 5: CSS Grid - Die wichtigsten Eigenschaften

### Container-Eigenschaften

```css
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);  /* 3 gleiche Spalten */
  grid-template-rows: auto;                /* Zeilen nach Bedarf */
  gap: 20px;                               /* Abstand */
}
```

### Spalten definieren

```css
/* 3 gleiche Spalten */
grid-template-columns: repeat(3, 1fr);

/* 3 Spalten mit verschiedenen Breiten */
grid-template-columns: 1fr 2fr 1fr;

/* Feste + flexible Spalten */
grid-template-columns: 250px 1fr;

/* Automatische Spalten basierend auf Mindestbreite */
grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
```

### Visualisierung

```
grid-template-columns: repeat(3, 1fr)

┌─────────┬─────────┬─────────┐
│   1fr   │   1fr   │   1fr   │
├─────────┼─────────┼─────────┤
│  Card   │  Card   │  Card   │
└─────────┴─────────┴─────────┘

grid-template-columns: 1fr 2fr 1fr

┌────┬──────────────┬────┐
│1fr │     2fr      │1fr │
└────┴──────────────┴────┘
```

---

## Teil 6: Übung - Kartenraster mit Grid

### Aufgabe

Erstelle ein Kartenraster mit 3 Spalten:

**HTML:**
```html
<section class="cards">
  <div class="card">
    <h3>Projekt 1</h3>
    <p>Beschreibung des ersten Projekts.</p>
  </div>
  <div class="card">
    <h3>Projekt 2</h3>
    <p>Beschreibung des zweiten Projekts.</p>
  </div>
  <div class="card">
    <h3>Projekt 3</h3>
    <p>Beschreibung des dritten Projekts.</p>
  </div>
  <div class="card">
    <h3>Projekt 4</h3>
    <p>Beschreibung des vierten Projekts.</p>
  </div>
  <div class="card">
    <h3>Projekt 5</h3>
    <p>Beschreibung des fünften Projekts.</p>
  </div>
  <div class="card">
    <h3>Projekt 6</h3>
    <p>Beschreibung des sechsten Projekts.</p>
  </div>
</section>
```

**Anforderungen:**
- 3 gleichmäßige Spalten
- 20px Abstand zwischen den Karten
- Auf Mobile: 1 Spalte

<details>
<summary>Musterlösung anzeigen</summary>

```css
/* Kartenraster */
.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  padding: 2rem;
}

/* Responsive: 1 Spalte auf Mobile */
@media (max-width: 768px) {
  .cards {
    grid-template-columns: 1fr;
  }
}

/* Optional: 2 Spalten auf Tablet */
@media (max-width: 1024px) and (min-width: 769px) {
  .cards {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* Einzelne Karte */
.card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card h3 {
  margin-top: 0;
  color: #1a1a2e;
}

.card p {
  color: #666666;
  margin-bottom: 0;
}
```

**Erklärung:**
- `repeat(3, 1fr)` = 3 gleiche Spalten
- `gap: 20px` = Abstand zwischen allen Karten
- `@media` = Breakpoint für Responsive

</details>

---

## Teil 7: Responsive Design Grundprinzipien

### Die 3 Säulen

**1. Viewport Meta (im HTML `<head>`):**
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
→ Sagt dem Browser: Skaliere nicht herunter, nutze die echte Gerätebreite

**2. Breakpoints (Media Queries):**
```css
/* Mobile First: Standard ist Mobile */
.container {
  padding: 1rem;
}

/* Ab 768px: Tablet */
@media (min-width: 768px) {
  .container {
    padding: 2rem;
  }
}

/* Ab 1024px: Desktop */
@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

**3. Relative Einheiten:**
```css
/* Statt fixer Breiten */
width: 500px;  /* ❌ Kann überlaufen */

/* Besser: relative Werte */
width: 100%;
max-width: 500px;  /* ✓ Flexibel mit Maximum */
```

### Häufige Breakpoints

| Breakpoint | Beschreibung |
|------------|--------------|
| 480px | Kleine Smartphones |
| 768px | Tablets / große Phones |
| 1024px | Laptops |
| 1200px | Desktop |
| 1440px | Große Bildschirme |

**Pro-Tipp:** Starte mit 1-2 Breakpoints. Mehr sind selten nötig!

---

## Teil 8: Wissensfrage

Du siehst horizontales Scrollen auf einem Smartphone. Was sind die drei häufigsten Ursachen?

<details>
<summary>Antwort anzeigen</summary>

**Die 3 häufigsten Ursachen für horizontales Scrollen:**

1. **Feste Breiten:**
   ```css
   /* Problem */
   .container { width: 1000px; }

   /* Lösung */
   .container {
     width: 100%;
     max-width: 1000px;
   }
   ```

2. **Fehlendes `flex-wrap`:**
   ```css
   /* Problem - Items brechen nicht um */
   .flex-container { display: flex; }

   /* Lösung */
   .flex-container {
     display: flex;
     flex-wrap: wrap;
   }
   ```

3. **Bilder ohne `max-width`:**
   ```css
   /* Problem - Bild ist breiter als Viewport */
   img { width: 800px; }

   /* Lösung */
   img {
     max-width: 100%;
     height: auto;
   }
   ```

**Debug-Tipp:** DevTools → Responsive Mode → Element inspizieren, das über den Rand ragt

</details>

---

## Teil 9: Übung - Responsive Layout

### Aufgabe

Erstelle ein vollständiges responsives Layout:

**Desktop (> 768px):**
- Navigation: Logo links, Links rechts
- Hero-Bereich: Zentriert
- Cards: 3 Spalten

**Mobile (< 768px):**
- Navigation: Logo oben, Links darunter
- Hero-Bereich: Volle Breite
- Cards: 1 Spalte

<details>
<summary>Musterlösung anzeigen</summary>

```css
/* ==================
   Responsive Layout
   Mobile First Approach
   ================== */

/* Reset */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Segoe UI', Arial, sans-serif;
  line-height: 1.6;
  color: #333;
}

/* ==================
   Navigation
   ================== */

.navbar {
  background-color: #1a1a2e;
  padding: 1rem;
}

/* Mobile: Logo oben, Links darunter */
.navbar {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
}

.nav-links {
  display: flex;
  gap: 1rem;
  list-style: none;
}

.nav-links a {
  color: white;
  text-decoration: none;
}

/* Desktop: Logo links, Links rechts */
@media (min-width: 768px) {
  .navbar {
    flex-direction: row;
    justify-content: space-between;
    padding: 1rem 2rem;
  }
}

/* ==================
   Hero Section
   ================== */

.hero {
  min-height: 50vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 2rem 1rem;
  background: linear-gradient(135deg, #1a1a2e, #16213e);
  color: white;
}

.hero-content {
  max-width: 100%;
}

.hero h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

@media (min-width: 768px) {
  .hero {
    min-height: 70vh;
  }

  .hero-content {
    max-width: 600px;
  }

  .hero h1 {
    font-size: 3rem;
  }
}

/* ==================
   Cards Section
   ================== */

.cards {
  padding: 2rem 1rem;
  display: grid;
  grid-template-columns: 1fr;  /* Mobile: 1 Spalte */
  gap: 1rem;
}

@media (min-width: 768px) {
  .cards {
    grid-template-columns: repeat(3, 1fr);  /* Desktop: 3 Spalten */
    gap: 2rem;
    padding: 3rem 2rem;
  }
}

.card {
  background-color: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* ==================
   Footer
   ================== */

footer {
  background-color: #1a1a2e;
  color: white;
  text-align: center;
  padding: 1.5rem;
}
```

**HTML-Struktur:**
```html
<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Responsive Layout</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <nav class="navbar">
    <div class="logo">DevApp</div>
    <ul class="nav-links">
      <li><a href="#">Home</a></li>
      <li><a href="#">About</a></li>
      <li><a href="#">Contact</a></li>
    </ul>
  </nav>

  <section class="hero">
    <div class="hero-content">
      <h1>Willkommen</h1>
      <p>Dies ist meine Portfolio-Seite.</p>
    </div>
  </section>

  <section class="cards">
    <div class="card">
      <h3>Projekt 1</h3>
      <p>Beschreibung</p>
    </div>
    <div class="card">
      <h3>Projekt 2</h3>
      <p>Beschreibung</p>
    </div>
    <div class="card">
      <h3>Projekt 3</h3>
      <p>Beschreibung</p>
    </div>
  </section>

  <footer>
    <p>&copy; 2024 DevApp</p>
  </footer>
</body>
</html>
```

</details>

---

## Teil 10: DevTools für Layout-Debugging

### Responsive Mode

**Aktivieren:** `Ctrl+Shift+M` (Windows) / `Cmd+Shift+M` (Mac)

**Features:**
- Verschiedene Geräte simulieren
- Eigene Viewport-Größen eingeben
- Breakpoints testen
- Touch-Events simulieren

### Flex/Grid Overlays

In Chrome und Firefox:
1. Element mit Flexbox/Grid inspizieren
2. Im Styles-Panel auf `flex` oder `grid` Badge klicken
3. Overlay zeigt die Layout-Struktur

### Übung 5: Layout debuggen

**Aufgabe:**

1. Öffne dein responsives Layout im Browser
2. Öffne DevTools → Responsive Mode (Ctrl+Shift+M)
3. Teste verschiedene Bildschirmbreiten:
   - 320px (kleines Smartphone)
   - 768px (Tablet)
   - 1200px (Desktop)
4. Prüfe: Gibt es horizontales Scrollen?
5. Finde ein Flex- oder Grid-Element und aktiviere das Overlay

<details>
<summary>Hinweise zur Lösung</summary>

**So testest du Breakpoints:**

1. Im Responsive Mode die Breite langsam ziehen
2. Beobachte, wo das Layout "springt" (Breakpoints)
3. Prüfe, ob alle Übergänge sauber sind

**Horizontales Scrollen finden:**
- Auf sehr schmale Breite (320px) gehen
- Horizontal scrollen → Welches Element ragt über?
- Element inspizieren → Box Model prüfen

**Flex/Grid Overlay aktivieren:**
- Element mit `display: flex` oder `display: grid` auswählen
- Im Styles-Panel erscheint ein `flex`/`grid` Badge
- Klick zeigt farbiges Overlay mit:
  - Spalten/Zeilen
  - Gaps
  - Item-Positionen

</details>

---

## Teil 11: Häufige Layout-Fehler

### Problem: Layout bricht nach Deploy

**Mögliche Ursachen:**

| Ursache | Symptom | Lösung |
|---------|---------|--------|
| Falscher Pfad | CSS 404 | Pfade prüfen |
| Cache | Alte Version | Hard Reload |
| Build/Minification | Anderer Dateiname | Build-Output prüfen |
| Missing Viewport | Zu klein auf Mobile | `<meta viewport>` prüfen |

### Diagnose-Workflow

1. **Network Tab:** Wird CSS geladen? Status 200?
2. **Vergleich:** Lokal vs. Produktion - identisch?
3. **Cache:** Hard Reload, dann erneut testen
4. **Responsive Mode:** Bei welcher Breite bricht es?

---

## Zusammenfassung

### Was du gelernt hast:

| Thema | Key Takeaway |
|-------|--------------|
| Flexbox | Für eindimensionale Layouts (Navigation, Buttons) |
| Grid | Für zweidimensionale Layouts (Kartenraster) |
| justify-content | Verteilung auf Hauptachse |
| align-items | Ausrichtung auf Querachse |
| Media Queries | Breakpoints für Responsive |
| Relative Einheiten | %, rem, max-width statt fixe px |
| DevTools | Responsive Mode, Flex/Grid Overlays |

### Faustregel

```
Flexbox = Eine Richtung (Zeile ODER Spalte)
Grid = Zwei Richtungen (Zeilen UND Spalten)
```

### Vorbereitung auf morgen

Morgen ist **Freitag - Mini-Projekt Tag!**

Du wirst alles zusammenbringen:
- HTTP-Wissen (Tag 1)
- HTML-Struktur (Tag 2)
- CSS-Styling (Tag 3)
- Layout & Responsive (Tag 4)

...zu einem vollständigen Portfolio-Projekt!

---

## Bonus: Flexbox vs. Grid Cheatsheet

<details>
<summary>Schnellreferenz anzeigen</summary>

### Flexbox

```css
/* Container */
.flex-container {
  display: flex;
  flex-direction: row | column;
  justify-content: flex-start | center | flex-end | space-between | space-around;
  align-items: flex-start | center | flex-end | stretch;
  gap: 20px;
  flex-wrap: wrap;
}

/* Items */
.flex-item {
  flex: 1;            /* Wächst gleichmäßig */
  flex: 0 0 200px;    /* Feste Breite, kein Schrumpfen */
  align-self: center; /* Einzelnes Item ausrichten */
}
```

### Grid

```css
/* Container */
.grid-container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-columns: 200px 1fr 200px;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

/* Items */
.grid-item {
  grid-column: span 2;     /* 2 Spalten breit */
  grid-row: span 2;        /* 2 Zeilen hoch */
}
```

### Media Queries

```css
/* Mobile First */
.container {
  padding: 1rem;
}

/* Tablet */
@media (min-width: 768px) {
  .container {
    padding: 2rem;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .container {
    max-width: 1200px;
    margin: 0 auto;
  }
}
```

</details>
