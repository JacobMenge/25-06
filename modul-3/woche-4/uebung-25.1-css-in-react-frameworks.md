# CSS in React & CSS-Frameworks - Praktische Übung

## Übersicht

Willkommen zu deiner ersten Begegnung mit CSS in der React-Welt! Bisher hast du deine Komponenten entweder gar nicht oder nur mit einfachen CSS-Dateien gestylt. In dieser Übung lernst du, warum CSS in React anders funktioniert als in klassischem HTML, welche Ansätze es gibt und wie CSS-Frameworks dir die Arbeit massiv erleichtern können.

In dieser Übung lernst du:
- **CSS-Ansätze in React** - Inline Styles, CSS-Dateien und CSS Modules im Vergleich
- **Warum CSS-Frameworks?** - Welche Probleme sie lösen und warum du sie brauchst
- **Tailwind CSS** - Utility-First CSS direkt in deinem JSX
- **Ant Design** - Eine fertige Komponenten-Bibliothek für professionelle UIs
- **Weitere kostenlose Frameworks** - Bootstrap, Chakra UI, Material UI und mehr
- **Framework-Auswahl** - Wann welches Framework die richtige Wahl ist

Diese Übung baut auf "24.4 Rendering, Listen & Keys" auf und nutzt CSS-Grundlagen aus Woche 1 (Tag 3 & 4) – stelle sicher, dass du Flexbox und Grid verstanden hast!

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Rückblick** | CSS-Grundlagen in React | 5 min (lesen) |
| **Teil 1** | CSS-Ansätze in React | 20 min |
| **Teil 2** | Warum CSS-Frameworks? | 10 min (lesen) |
| **Teil 3** | Tailwind CSS: Setup & Grundlagen | 25 min |
| **Teil 4** | Tailwind CSS: Responsive & Hover-States | 20 min |
| **Teil 5** | Ant Design: Setup & Grundlagen | 25 min |
| **Teil 6** | Ant Design: Formulare & Layout | 20 min |
| **Teil 7** | Weitere CSS-Frameworks im Überblick | 10 min (lesen) |
| **Teil 8** | Praxis: Profilkarte mit Tailwind | 30 min |
| **Teil 9** | Praxis: Dashboard mit Ant Design | 30 min |
| | **Gesamt** | **ca. 3,5 Stunden** |

### Minimalpfad (wenn du wenig Zeit hast)

**In 60-90 Minuten die wichtigsten Konzepte:**

1. **Teil 1** - CSS-Ansätze in React - *Grundverständnis*
2. **Teil 2** - Warum CSS-Frameworks? - *Motivation verstehen*
3. **Teil 3** - Tailwind CSS: Setup & Grundlagen - *Utility-First kennenlernen*
4. **Teil 5** - Ant Design: Setup & Grundlagen - *Komponenten-Bibliothek kennenlernen*
5. **Teil 8** - Praxis: Profilkarte mit Tailwind - *Alles zusammen*

---

## Voraussetzungen & Setup

**Bevor du startest:**

1. Du hast ein funktionierendes React-Projekt (aus den vorherigen Übungen)
2. Der Dev-Server läuft (`npm run dev`)
3. Du kennst CSS-Grundlagen (Selektoren, Flexbox, Grid) aus Woche 1

Falls du kein Projekt hast, erstelle schnell eines:

```bash
npm create vite@latest css-frameworks-uebung -- --template react
cd css-frameworks-uebung
npm install
npm run dev
```

> **Hinweis:** Für Tailwind CSS und Ant Design werden wir jeweils separate Projekte erstellen. Die Setup-Anleitungen findest du in den jeweiligen Teilen (Teil 3 und Teil 5).

---

## Rückblick: CSS-Grundlagen in React

### Was du schon kennst

In Woche 1 hast du CSS-Grundlagen gelernt:
- **Tag 3:** Selektoren, Box Model, Kaskade & Spezifität
- **Tag 4:** Flexbox, Grid, Responsive Design, Media Queries

### Was sich in React ändert

In klassischem HTML lädst du CSS als separate Datei:

```html
<!-- Klassisch: Eine globale CSS-Datei -->
<link rel="stylesheet" href="styles.css">

<!-- HTML verwendet "class" -->
<div class="card">Inhalt</div>
```

In React importierst du CSS direkt in deine Komponenten – und `class` heißt hier `className`:

```javascript
// React: CSS wird in die Komponente importiert
import './App.css';

// JSX verwendet "className" statt "class"
function App() {
  return <div className="card">Inhalt</div>;
}
```

### Warum `className` statt `class`?

`class` ist ein reserviertes Wort in JavaScript (für Klassen-Definitionen). Deshalb verwendet React `className`. Das ist einer der wenigen Unterschiede zu normalem HTML.

```
┌─────────────────────────────────────────────────────────────┐
│              CSS IN HTML vs CSS IN REACT                    │
│                                                             │
│   HTML (klassisch)              React (modern)              │
│   ────────────────              ──────────────              │
│   <link href="...">            import './App.css'           │
│   class="card"                 className="card"             │
│   style="color: red"          style={{ color: 'red' }}      │
│   Globale CSS-Dateien          Mehrere Ansätze möglich      │
│                                                             │
│   ┌──────────┐                 ┌──────────┐                 │
│   │ HTML     │ ◄── styles.css  │ App.jsx  │ ◄── App.css     │
│   │          │                 │          │ ◄── Inline      │
│   │          │                 │          │ ◄── Modules     │
│   └──────────┘                 └──────────┘                 │
│   Ein Weg                      Mehrere Wege                 │
└─────────────────────────────────────────────────────────────┘
```

**Das Problem:** In React gibt es mehrere Wege, CSS einzusetzen. Jeder hat Vor- und Nachteile. Schauen wir uns die drei wichtigsten Ansätze an!

---

## Teil 1: CSS-Ansätze in React

### Ansatz 1: Inline Styles

In React kannst du Styles direkt als JavaScript-Objekt übergeben:

```javascript
function InlineCard() {
  return (
    <div style={{
      backgroundColor: '#f0f0f0',
      padding: '20px',
      borderRadius: '12px',
      border: '1px solid #ddd'
    }}>
      <h2 style={{ margin: 0, color: '#333' }}>Inline Card</h2>
      <p style={{ color: '#666', marginTop: '8px' }}>
        Styled mit Inline Styles
      </p>
    </div>
  );
}
```

**Wichtige Unterschiede zu HTML-Inline-Styles:**

| HTML | React |
|------|-------|
| `style="background-color: red"` | `style={{ backgroundColor: 'red' }}` |
| String | JavaScript-Objekt |
| `kebab-case` | `camelCase` |
| Werte als Strings | Zahlen für Pixel möglich |

```javascript
// HTML:  font-size        → React: fontSize
// HTML:  background-color → React: backgroundColor
// HTML:  border-radius    → React: borderRadius
// HTML:  margin-top       → React: marginTop

// Zahlen werden automatisch zu Pixeln:
style={{ fontSize: 16 }}    // → "16px"
style={{ fontSize: '2rem' }} // → "2rem" (String für andere Einheiten)
```

**Wann Inline Styles nutzen?**
- Dynamische Styles, die von State oder Props abhängen
- Einzelne, einfache Style-Änderungen

```javascript
//  Gut: Dynamischer Style basierend auf Props
function ProgressBar({ progress }) {
  return (
    <div style={{
      width: `${progress}%`,
      backgroundColor: progress > 80 ? 'green' : 'orange',
      height: '20px',
      borderRadius: '10px'
    }} />
  );
}

//  Schlecht: Komplexe Styles inline
function ComplexCard() {
  return (
    <div style={{
      backgroundColor: '#fff', padding: '20px', borderRadius: '12px',
      boxShadow: '0 4px 6px rgba(0,0,0,0.1)', border: '1px solid #eee',
      maxWidth: '400px', margin: '0 auto', transition: 'all 0.3s'
      // Das wird schnell unübersichtlich!
    }}>
      ...
    </div>
  );
}
```

### Ansatz 2: CSS-Dateien importieren

Der einfachste Ansatz – du erstellst eine `.css`-Datei und importierst sie:

```css
/* src/components/Card.css */
.card {
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 12px;
  border: 1px solid #ddd;
}

.card-title {
  margin: 0;
  color: #333;
}

.card-text {
  color: #666;
  margin-top: 8px;
}
```

```javascript
// src/components/Card.jsx
import './Card.css';  // CSS wird importiert

function Card() {
  return (
    <div className="card">
      <h2 className="card-title">CSS-Datei Card</h2>
      <p className="card-text">Styled mit importierter CSS-Datei</p>
    </div>
  );
}
```

**Das Problem: Globaler Scope!**

Alle importierten CSS-Dateien sind **global** – Klassen können sich gegenseitig überschreiben:

```javascript
// Button.css definiert .button { color: red; }
// NavButton.css definiert auch .button { color: blue; }

// Welche Farbe gewinnt? Das hängt von der Import-Reihenfolge ab!
// → Das führt zu schwer findbaren Bugs!
```

```
┌─────────────────────────────────────────────────────────────┐
│                  DAS SCOPING-PROBLEM                        │
│                                                             │
│  Button.css:     .btn { color: red; }     ──┐               │
│                                             ├── KONFLIKT!   │
│  NavButton.css:  .btn { color: blue; }    ──┘               │
│                                                             │
│  Beide Klassen heißen .btn → Welche gewinnt?                │
│  → Die zuletzt importierte überschreibt die andere!         │
└─────────────────────────────────────────────────────────────┘
```

### Ansatz 3: CSS Modules

CSS Modules lösen das Scoping-Problem. Du erstellst eine Datei mit der Endung `.module.css`:

```css
/* src/components/Card.module.css */
.card {
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 12px;
  border: 1px solid #ddd;
}

.title {
  margin: 0;
  color: #333;
}

.text {
  color: #666;
  margin-top: 8px;
}
```

```javascript
// src/components/Card.jsx
import styles from './Card.module.css';  // Importiert als Objekt!

function Card() {
  return (
    <div className={styles.card}>
      <h2 className={styles.title}>CSS Module Card</h2>
      <p className={styles.text}>Styled mit CSS Modules</p>
    </div>
  );
}
```

**Wie funktioniert das?** Vite wandelt die Klassennamen automatisch um:

```
Dein Code:          .card → styles.card
Im Browser wird:    .card → ._card_x7k2j_1

Jede Komponente bekommt eindeutige Klassennamen!
→ Keine Konflikte mehr!
```

### Vergleichstabelle: CSS-Ansätze in React

| Aspekt | Inline Styles | CSS-Dateien | CSS Modules |
|--------|--------------|-------------|-------------|
| **Syntax** | JavaScript-Objekt | Normales CSS | Normales CSS |
| **Scoping** | Automatisch (per Element) | Global (Konfliktgefahr!) | Automatisch (per Komponente) |
| **Pseudo-Klassen** (`:hover`) | Nicht direkt (nur über State/Events nachbaubar) | Ja | Ja |
| **Media Queries** | Nicht direkt (nur über JS `window.matchMedia` nachbaubar) | Ja | Ja |
| **Dynamische Styles** | Einfach | Umständlich | Umständlich |
| **Wiederverwendbarkeit** | Niedrig | Mittel | Hoch |
| **Empfehlung** | Nur für dynamische Werte | Für kleine Projekte | Für mittlere/große Projekte |

### Übung 1: Drei Wege, eine Card

> **Ziel:** Die drei CSS-Ansätze in React praktisch vergleichen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Du drei identisch aussehende Cards gebaut hast, jede mit einem anderen CSS-Ansatz

Jetzt wendest du die drei Ansätze von oben praktisch an. Erstelle drei Varianten einer einfachen Info-Card, die alle gleich aussehen sollen. Jede Variante bekommt einen eigenen, eindeutigen Dateinamen:

1. `InlineCard.jsx` – mit Inline Styles
2. `CssCard.jsx` + `CssCard.css` – mit importierter CSS-Datei
3. `ModuleCard.jsx` + `ModuleCard.module.css` – mit CSS Modules

**Ziel-Design:**
- Weiße Box mit abgerundeten Ecken (12px) und Schatten
- Padding: 24px
- Titel in dunkelgrau (#333), 20px
- Text in grau (#666), 14px
- Blaue Linie unten (4px, Farbe #3498db)

**Starter-Code für `App.jsx`:**

```javascript
import InlineCard from './components/InlineCard';
import CssCard from './components/CssCard';
import ModuleCard from './components/ModuleCard';

function App() {
  return (
    <div style={{ display: 'flex', gap: '20px', padding: '40px', flexWrap: 'wrap' }}>
      <InlineCard
        title="Inline Styles"
        text="Diese Card verwendet Inline Styles"
      />
      <CssCard
        title="CSS-Datei"
        text="Diese Card verwendet eine importierte CSS-Datei"
      />
      <ModuleCard
        title="CSS Modules"
        text="Diese Card verwendet CSS Modules"
      />
    </div>
  );
}

export default App;
```

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/InlineCard.jsx:**

```javascript
function InlineCard({ title, text }) {
  return (
    <div style={{
      backgroundColor: 'white',
      borderRadius: '12px',
      padding: '24px',
      boxShadow: '0 2px 8px rgba(0,0,0,0.1)',
      borderBottom: '4px solid #3498db',
      width: '280px'
    }}>
      <h3 style={{ margin: 0, color: '#333', fontSize: '20px' }}>
        {title}
      </h3>
      <p style={{ color: '#666', fontSize: '14px', marginTop: '8px' }}>
        {text}
      </p>
    </div>
  );
}

export default InlineCard;
```

**src/components/CssCard.css:**

```css
.css-card {
  background-color: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-bottom: 4px solid #3498db;
  width: 280px;
}

.css-card-title {
  margin: 0;
  color: #333;
  font-size: 20px;
}

.css-card-text {
  color: #666;
  font-size: 14px;
  margin-top: 8px;
}
```

**src/components/CssCard.jsx:**

```javascript
import './CssCard.css';

function CssCard({ title, text }) {
  return (
    <div className="css-card">
      <h3 className="css-card-title">{title}</h3>
      <p className="css-card-text">{text}</p>
    </div>
  );
}

export default CssCard;
```

**src/components/ModuleCard.module.css:**

```css
.card {
  background-color: white;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  border-bottom: 4px solid #3498db;
  width: 280px;
}

.title {
  margin: 0;
  color: #333;
  font-size: 20px;
}

.text {
  color: #666;
  font-size: 14px;
  margin-top: 8px;
}
```

**src/components/ModuleCard.jsx:**

```javascript
import styles from './ModuleCard.module.css';

function ModuleCard({ title, text }) {
  return (
    <div className={styles.card}>
      <h3 className={styles.title}>{title}</h3>
      <p className={styles.text}>{text}</p>
    </div>
  );
}

export default ModuleCard;
```

</details>

### Wissensfrage 1

**Warum kann es problematisch sein, alle CSS-Klassen in globalen CSS-Dateien zu definieren?**

<details>
<summary>Antwort anzeigen</summary>

Globale CSS-Klassen können sich gegenseitig überschreiben, wenn zwei Komponenten denselben Klassennamen verwenden. In einem großen Projekt mit vielen Komponenten ist es schwer, eindeutige Namen zu garantieren. CSS Modules lösen dieses Problem, indem sie Klassennamen automatisch eindeutig machen (z.B. `.card` wird zu `._card_x7k2j_1`). So kann jede Komponente ihre eigenen Klassennamen verwenden, ohne Konflikte befürchten zu müssen.

</details>

---

## Teil 2: Warum CSS-Frameworks?

### Das Problem mit eigenen Styles

Stell dir vor, du baust eine komplette Web-App von Grund auf. Du brauchst:

- Buttons in verschiedenen Varianten (Primary, Secondary, Danger, Disabled...)
- Formulare mit Validierung und Fehlermeldungen
- Responsive Navigation
- Cards, Modals, Tooltips, Tabs, Dropdowns...
- Ein konsistentes Farbschema über die gesamte App
- Responsive Design für jede einzelne Komponente
- Browser-Kompatibilität

**All das von Hand zu bauen dauert Wochen – und ist fehleranfällig.**

```
┌─────────────────────────────────────────────────────────────┐
│                 OHNE CSS-FRAMEWORK                          │
│                                                             │
│  Du musst ALLES selbst bauen:                               │
│                                                             │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │ Buttons  │ │  Forms   │ │  Cards   │ │  Modals  │        │
│  │ 200 LOC  │ │ 500 LOC  │ │ 150 LOC  │ │ 300 LOC  │        │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐        │
│  │  Tables  │ │  Navs    │ │  Tabs    │ │ Tooltips │        │
│  │ 400 LOC  │ │ 350 LOC  │ │ 200 LOC  │ │ 150 LOC  │        │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘        │
│                                                             │
│  = Tausende Zeilen CSS, die DU pflegen musst!               │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                 MIT CSS-FRAMEWORK                           │
│                                                             │
│  ┌─────────────────────────────────────────────────┐        │
│  │           npm install [framework]               │        │
│  │                                                 │        │
│  │  ✓ Buttons    ✓ Forms     ✓ Cards    ✓ Modals  │       │
│  │  ✓ Tables     ✓ Navs     ✓ Tabs     ✓ Tooltips │       │
│  │  ✓ Responsive ✓ Accessible ✓ Getestet          │        │
│  └─────────────────────────────────────────────────┘        │
│                                                             │
│  = Fertig! Du kannst dich auf deine App-Logik               │
│    konzentrieren.                                           │
└─────────────────────────────────────────────────────────────┘
```

### Was CSS-Frameworks dir geben

| Vorteil | Beschreibung |
|---------|-------------|
| **Fertige Bausteine** | Buttons, Cards, Forms, Modals... sofort einsatzbereit |
| **Einheitliches Design** | Alles passt zusammen, konsistente Farben und Abstände |
| **Responsive by Default** | Mobile-First, funktioniert auf allen Bildschirmgrößen |
| **Getestet** | Tausende Entwickler nutzen und testen die Komponenten |
| **Dokumentation** | Ausführliche Docs mit Beispielen und Code-Snippets |
| **Community** | Hilfe bei Problemen, regelmäßige Updates |

### Zwei Arten von CSS-Frameworks

Es gibt zwei grundsätzlich verschiedene Ansätze:

```
┌─────────────────────────────────────────────────────────────┐
│                 UTILITY-FIRST                               │
│                 (z.B. Tailwind CSS)                         │
│                                                             │
│  Du bekommst: Kleine CSS-Klassen (Utilities)                │
│  Du baust:    Deine eigenen Komponenten damit               │
│                                                             │
│  <button className="bg-blue-500 text-white px-4 py-2        │
│                      rounded hover:bg-blue-600">            │
│    Klick mich                                               │
│  </button>                                                  │
│                                                             │
│  → Volle Kontrolle über das Design                          │
│  → Mehr Schreibarbeit pro Element                           │
├─────────────────────────────────────────────────────────────┤
│                 KOMPONENTEN-BIBLIOTHEK                      │
│                 (z.B. Ant Design)                           │
│                                                             │
│  Du bekommst: Fertige React-Komponenten                     │
│  Du nutzt:    Die Komponenten direkt                        │
│                                                             │
│  <Button type="primary" size="large">                       │
│    Klick mich                                               │
│  </Button>                                                  │
│                                                             │
│  → Schnell produktiv, professionelles Design                │
│  → Weniger Kontrolle über Details                           │
└─────────────────────────────────────────────────────────────┘
```

| Aspekt | Utility-First (Tailwind) | Komponenten-Bibliothek (Ant Design) |
|--------|--------------------------|-------------------------------------|
| **Was du bekommst** | CSS-Klassen | Fertige React-Komponenten |
| **Designfreiheit** | Sehr hoch | Eingeschränkt (vordefiniertes Design) |
| **Geschwindigkeit** | Mittel (du baust selbst) | Hoch (fertige Komponenten) |
| **Lernkurve** | Klassen-System lernen | API der Komponenten lernen |
| **Bundle-Größe** | Klein (nur genutzte Klassen) | Größer (Komponenten-Code) |
| **Anpassbarkeit** | Sehr flexibel | Theming möglich, aber begrenzt |
| **Best für** | Eigenes, einzigartiges Design | Business-Apps, Admin-Dashboards |

### Wissensfrage 2

**Was ist der Unterschied zwischen Utility-First (Tailwind) und einer Komponenten-Bibliothek (Ant Design)?**

<details>
<summary>Antwort anzeigen</summary>

**Utility-First (Tailwind CSS):** Du bekommst viele kleine CSS-Klassen (wie `bg-blue-500`, `p-4`, `rounded`), die du direkt im JSX kombinierst, um dein eigenes Design zu bauen. Du hast volle Kontrolle über das Aussehen.

**Komponenten-Bibliothek (Ant Design):** Du bekommst fertige React-Komponenten (wie `<Button>`, `<Card>`, `<Table>`), die bereits gestylt sind und eigene Props haben. Du kannst sie sofort verwenden, hast aber weniger Kontrolle über das genaue Aussehen.

</details>

---

## Teil 3: Tailwind CSS – Setup & Grundlagen

### Was ist Tailwind CSS?

Tailwind CSS ist ein **Utility-First CSS Framework**. Statt eigene CSS-Klassen zu schreiben, verwendest du vorgefertigte Utility-Klassen direkt in deinem HTML/JSX:

```javascript
//  Traditionell: Erst CSS-Klasse definieren, dann verwenden
// .card { padding: 20px; background: white; border-radius: 12px; }
// <div className="card">...</div>

//  Tailwind: Utility-Klassen direkt im JSX
<div className="p-5 bg-white rounded-xl">...</div>
```

**Das Konzept:** Jede CSS-Eigenschaft hat eine eigene Klasse. Du kombinierst diese Klassen, um dein Design zu bauen:

```
┌─────────────────────────────────────────────────────────────┐
│              TAILWIND UTILITY-KLASSEN                       │
│                                                             │
│  CSS-Eigenschaft          Tailwind-Klasse                   │
│  ─────────────────        ───────────────                   │
│  padding: 20px            p-5                               │
│  background: white        bg-white                          │
│  border-radius: 12px      rounded-xl                        │
│  color: #333              text-gray-800                   │
│  font-weight: bold        font-bold                         │
│  display: flex            flex                              │
│  gap: 16px                gap-4                             │
│                                                             │
│  Alles zusammen:                                            │
│  className="p-5 bg-white rounded-xl text-gray-800           │
│             font-bold flex gap-4"                           │
└─────────────────────────────────────────────────────────────┘
```

### Tailwind einrichten (Vite + React)

Erstelle ein neues Projekt mit Tailwind:

```bash
# 1. Neues Projekt erstellen
npm create vite@latest tailwind-uebung -- --template react
cd tailwind-uebung
npm install

# 2. Tailwind installieren
npm install -D tailwindcss @tailwindcss/vite
```

**3. Vite-Konfiguration anpassen** – öffne `vite.config.js`:

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  plugins: [
    react(),
    tailwindcss(),   // Tailwind Plugin hinzufügen
  ],
});
```

> **Hinweis:** Dieses Setup entspricht **Tailwind v4** (Vite-Plugin + `@import "tailwindcss"`). In älteren Guides oder Blogposts siehst du möglicherweise ein anderes Setup mit `tailwind.config.js`, `postcss.config.js` und `@tailwind base; @tailwind components; @tailwind utilities;` – das ist die v3-Variante und **nicht** kompatibel mit diesem Setup. Achte darauf, dass du die v4-Anleitung hier befolgst.

**4. CSS-Datei anpassen** – ersetze den Inhalt von `src/index.css` mit:

```css
/* src/index.css */
@import "tailwindcss";
```

**5. Testen** – ersetze den Inhalt von `src/App.jsx`:

```javascript
function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-xl shadow-lg">
        <h1 className="text-2xl font-bold text-gray-800">
          Tailwind funktioniert!
        </h1>
        <p className="text-gray-600 mt-2">
          Wenn du das hier schön gestylt siehst, ist alles korrekt.
        </p>
      </div>
    </div>
  );
}

export default App;
```

```bash
npm run dev
```

Wenn du eine weiße Box mit Schatten auf grauem Hintergrund siehst, funktioniert Tailwind!

### Die wichtigsten Utility-Klassen

#### Spacing (Abstände)

Tailwind nutzt ein **4px-Raster**: `1` = 4px, `2` = 8px, `4` = 16px, `8` = 32px usw.

| Klasse | CSS | Bedeutung |
|--------|-----|-----------|
| `p-4` | `padding: 16px` | Padding auf allen Seiten |
| `px-4` | `padding-left: 16px; padding-right: 16px` | Padding horizontal |
| `py-2` | `padding-top: 8px; padding-bottom: 8px` | Padding vertikal |
| `pt-4` | `padding-top: 16px` | Padding oben |
| `m-4` | `margin: 16px` | Margin auf allen Seiten |
| `mx-auto` | `margin-left: auto; margin-right: auto` | Horizontal zentrieren |
| `mt-8` | `margin-top: 32px` | Margin oben |
| `gap-4` | `gap: 16px` | Abstand in Flex/Grid |

#### Farben

Tailwind hat ein Farbsystem mit Abstufungen von 50 (hell) bis 950 (dunkel):

```javascript
// Hintergrundfarben
<div className="bg-blue-500">Blau</div>
<div className="bg-red-100">Helles Rot</div>
<div className="bg-gray-900">Fast Schwarz</div>

// Textfarben
<p className="text-blue-500">Blauer Text</p>
<p className="text-gray-600">Grauer Text</p>
<p className="text-white">Weißer Text</p>

// Rahmenfarben
<div className="border border-gray-300">Grauer Rahmen</div>
```

#### Typografie

| Klasse | CSS | Bedeutung |
|--------|-----|-----------|
| `text-sm` | `font-size: 14px` | Klein |
| `text-base` | `font-size: 16px` | Normal |
| `text-lg` | `font-size: 18px` | Groß |
| `text-xl` | `font-size: 20px` | Größer |
| `text-2xl` | `font-size: 24px` | Noch größer |
| `font-bold` | `font-weight: bold` | Fett |
| `font-semibold` | `font-weight: 600` | Halbfett |
| `text-center` | `text-align: center` | Zentriert |

#### Layout

| Klasse | CSS | Bedeutung |
|--------|-----|-----------|
| `flex` | `display: flex` | Flexbox |
| `grid` | `display: grid` | Grid |
| `items-center` | `align-items: center` | Vertikal zentrieren |
| `justify-center` | `justify-content: center` | Horizontal zentrieren |
| `justify-between` | `justify-content: space-between` | Verteilen |
| `flex-col` | `flex-direction: column` | Spalte |
| `grid-cols-3` | `grid-template-columns: repeat(3, 1fr)` | 3 Spalten |
| `w-full` | `width: 100%` | Volle Breite |
| `max-w-md` | `max-width: 28rem` | Maximale Breite |

#### Rahmen & Schatten

| Klasse | CSS | Bedeutung |
|--------|-----|-----------|
| `rounded` | `border-radius: 4px` | Leicht gerundet |
| `rounded-lg` | `border-radius: 8px` | Stärker gerundet |
| `rounded-xl` | `border-radius: 12px` | Stark gerundet |
| `rounded-full` | `border-radius: 9999px` | Komplett rund |
| `border` | `border: 1px solid` | Rahmen |
| `shadow` | `box-shadow: ...` | Kleiner Schatten |
| `shadow-lg` | `box-shadow: ...` | Großer Schatten |

### Vergleich: Traditionelles CSS vs Tailwind

Die gleiche Komponente – einmal mit CSS-Datei, einmal mit Tailwind:

```css
/* Traditionell: Button.css */
.primary-button {
  background-color: #3b82f6;
  color: white;
  padding: 8px 16px;
  border-radius: 8px;
  border: none;
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s;
}

.primary-button:hover {
  background-color: #2563eb;
}
```

```javascript
// Traditionell: Button.jsx
import './Button.css';

function Button({ children }) {
  return <button className="primary-button">{children}</button>;
}
```

```javascript
// Tailwind: Button.jsx – keine CSS-Datei nötig!
function Button({ children }) {
  return (
    <button className="bg-blue-500 text-white px-4 py-2 rounded-lg
                        font-semibold cursor-pointer transition-colors
                        hover:bg-blue-600">
      {children}
    </button>
  );
}
```

> **Tipp:** Am Anfang fühlt sich Tailwind ungewohnt an – viele Klassen im JSX. Aber du wirst merken: Du wechselst nie wieder zwischen CSS- und JSX-Datei hin und her. Alles ist an einem Ort!

### Übung 2: Hallo Tailwind

> **Ziel:** Erste Erfahrungen mit Tailwind CSS sammeln
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du eine gestylte Card mit Tailwind-Klassen im Browser siehst

Erstelle in deinem Tailwind-Projekt eine Komponente `TailwindCard.jsx`:

**Anforderungen:**
1. Eine Card mit weißem Hintergrund, Schatten und abgerundeten Ecken
2. Ein Titel in dunkelgrau, groß und fett
3. Ein Beschreibungstext in hellem Grau
4. Ein blauer Button mit weißem Text und abgerundeten Ecken
5. Angemessenes Spacing (Padding, Margins)

**Starter-Code:**

```javascript
// src/components/TailwindCard.jsx
function TailwindCard() {
  return (
    // Aufgabe: Füge Tailwind-Klassen hinzu!
    <div className="???">
      <h2 className="???">Meine erste Tailwind Card</h2>
      <p className="???">
        Diese Card wurde komplett mit Tailwind CSS gestylt –
        ohne eine einzige Zeile eigenes CSS!
      </p>
      <button className="???">
        Mehr erfahren
      </button>
    </div>
  );
}

export default TailwindCard;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/TailwindCard.jsx
function TailwindCard() {
  return (
    <div className="bg-white p-6 rounded-xl shadow-lg max-w-sm">
      <h2 className="text-xl font-bold text-gray-800">
        Meine erste Tailwind Card
      </h2>
      <p className="text-gray-600 mt-2">
        Diese Card wurde komplett mit Tailwind CSS gestylt –
        ohne eine einzige Zeile eigenes CSS!
      </p>
      <button className="mt-4 bg-blue-500 text-white px-4 py-2 rounded-lg
                          font-semibold hover:bg-blue-600 transition-colors">
        Mehr erfahren
      </button>
    </div>
  );
}

export default TailwindCard;
```

**src/App.jsx:**

```javascript
import TailwindCard from './components/TailwindCard';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <TailwindCard />
    </div>
  );
}

export default App;
```

</details>

---

## Teil 4: Tailwind CSS – Responsive & Hover-States

### Responsive Design mit Tailwind

Tailwind verwendet einen **Mobile-First** Ansatz. Du schreibst zuerst die Styles für kleine Bildschirme und fügst dann Breakpoint-Prefixes für größere Bildschirme hinzu:

| Prefix | Minimale Breite | Typisches Gerät |
|--------|----------------|-----------------|
| (kein Prefix) | 0px | Smartphone |
| `sm:` | 640px | Großes Smartphone |
| `md:` | 768px | Tablet |
| `lg:` | 1024px | Laptop |
| `xl:` | 1280px | Desktop |
| `2xl:` | 1536px | Großer Desktop |

```javascript
// Mobile: 1 Spalte → Tablet: 2 Spalten → Desktop: 3 Spalten
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <div>Karte 1</div>
  <div>Karte 2</div>
  <div>Karte 3</div>
</div>
```

```
┌─────────────────────────────────────────────────────────────┐
│              RESPONSIVE MIT TAILWIND                        │
│                                                             │
│  Mobile (< 768px)      Tablet (≥ 768px)    Desktop (≥ 1024) │
│  grid-cols-1           md:grid-cols-2       lg:grid-cols-3  │
│                                                             │
│  ┌────────────┐        ┌──────┐ ┌──────┐   ┌────┐┌────┐┌──┐ │
│  │  Karte 1   │        │  K1  │ │  K2  │   │ K1 ││ K2 ││K3│ │
│  ├────────────┤        ├──────┤ ├──────┤   └────┘└────┘└──┘ │
│  │  Karte 2   │        │  K3  │ │      │                    │
│  ├────────────┤        └──────┘ └──────┘                    │
│  │  Karte 3   │                                             │
│  └────────────┘                                             │
└─────────────────────────────────────────────────────────────┘
```

### Hover, Focus & andere States

Tailwind bietet Prefixes für verschiedene Zustände:

```javascript
// Hover-Effekte
<button className="bg-blue-500 hover:bg-blue-600">
  Hover mich
</button>

// Focus-Effekte (z.B. für Tastatur-Navigation)
<input className="border border-gray-300 focus:border-blue-500
                   focus:ring-2 focus:ring-blue-200" />

// Active (während dem Klicken)
<button className="bg-blue-500 active:bg-blue-700">
  Klick mich
</button>

// Disabled
<button className="bg-blue-500 disabled:bg-gray-300 disabled:cursor-not-allowed"
        disabled>
  Nicht klickbar
</button>
```

### Transition & Animation

```javascript
// Sanfte Übergänge
<div className="transition-all duration-300 hover:scale-105 hover:shadow-xl">
  Hover für Animation
</div>

// Nur bestimmte Eigenschaften animieren
<button className="transition-colors duration-200 bg-blue-500 hover:bg-blue-600">
  Farbübergang
</button>
```

### Übung 3: Responsives Produkt-Grid

> **Ziel:** Responsive Layouts und Hover-Effekte mit Tailwind umsetzen
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Dein Produkt-Grid sich an die Bildschirmgröße anpasst und die Cards Hover-Effekte haben

Erstelle ein responsives Produkt-Grid:
- **Mobile:** 1 Spalte
- **Tablet (md):** 2 Spalten
- **Desktop (lg):** 3 Spalten
- Jede Card soll beim Hover leicht nach oben wandern und einen stärkeren Schatten bekommen

**Starter-Code:**

```javascript
// src/components/ProductGrid.jsx
const produkte = [
  { id: 1, name: 'Laptop Pro', preis: 999.99, kategorie: 'Elektronik' },
  { id: 2, name: 'Wireless Kopfhörer', preis: 149.99, kategorie: 'Audio' },
  { id: 3, name: 'Smart Watch', preis: 299.99, kategorie: 'Wearables' },
  { id: 4, name: 'USB-C Hub', preis: 49.99, kategorie: 'Zubehör' },
  { id: 5, name: 'Mechanische Tastatur', preis: 179.99, kategorie: 'Zubehör' },
  { id: 6, name: '4K Monitor', preis: 449.99, kategorie: 'Elektronik' },
];

function ProductGrid() {
  return (
    <div className="max-w-6xl mx-auto p-4">
      <h1 className="???">Unser Sortiment</h1>
      <div className="???">
        {produkte.map(produkt => (
          <div key={produkt.id} className="???">
            {/* Kategorie-Badge */}
            <span className="???">
              {produkt.kategorie}
            </span>
            <h3 className="???">{produkt.name}</h3>
            <p className="???">{produkt.preis.toFixed(2)} €</p>
            <button className="???">In den Warenkorb</button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductGrid;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/ProductGrid.jsx
const produkte = [
  { id: 1, name: 'Laptop Pro', preis: 999.99, kategorie: 'Elektronik' },
  { id: 2, name: 'Wireless Kopfhörer', preis: 149.99, kategorie: 'Audio' },
  { id: 3, name: 'Smart Watch', preis: 299.99, kategorie: 'Wearables' },
  { id: 4, name: 'USB-C Hub', preis: 49.99, kategorie: 'Zubehör' },
  { id: 5, name: 'Mechanische Tastatur', preis: 179.99, kategorie: 'Zubehör' },
  { id: 6, name: '4K Monitor', preis: 449.99, kategorie: 'Elektronik' },
];

function ProductGrid() {
  return (
    <div className="max-w-6xl mx-auto p-4">
      <h1 className="text-3xl font-bold text-gray-800 text-center mb-8">
        Unser Sortiment
      </h1>

      {/* Responsives Grid: 1 → 2 → 3 Spalten */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {produkte.map(produkt => (
          <div
            key={produkt.id}
            className="bg-white p-6 rounded-xl shadow
                       transition-all duration-300
                       hover:-translate-y-1 hover:shadow-xl"
          >
            {/* Kategorie-Badge */}
            <span className="inline-block bg-blue-100 text-blue-800
                             text-xs font-semibold px-3 py-1 rounded-full">
              {produkt.kategorie}
            </span>

            <h3 className="text-lg font-bold text-gray-800 mt-3">
              {produkt.name}
            </h3>

            <p className="text-2xl font-bold text-green-600 mt-2">
              {produkt.preis.toFixed(2)} €
            </p>

            <button className="mt-4 w-full bg-blue-500 text-white py-2
                               rounded-lg font-semibold
                               hover:bg-blue-600 transition-colors">
              In den Warenkorb
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductGrid;
```

**src/App.jsx:**

```javascript
import ProductGrid from './components/ProductGrid';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 py-8">
      <ProductGrid />
    </div>
  );
}

export default App;
```

</details>

---

## Teil 5: Ant Design – Setup & Grundlagen

### Was ist Ant Design?

Ant Design (kurz: antd) ist eine **Komponenten-Bibliothek** für React. Statt einzelne CSS-Klassen zu kombinieren, bekommst du fertige, professionell gestaltete React-Komponenten:

```javascript
// Tailwind: Du baust den Button selbst mit Klassen
<button className="bg-blue-500 text-white px-4 py-2 rounded-lg">
  Klick mich
</button>

// Ant Design: Du verwendest eine fertige Button-Komponente
import { Button } from 'antd';
<Button type="primary" size="large">
  Klick mich
</Button>
```

```
┌─────────────────────────────────────────────────────────────┐
│          TAILWIND vs ANT DESIGN – ARBEITSWEISE              │
│                                                             │
│  Tailwind CSS:                                              │
│  ─────────────                                              │
│  Du bekommst: Utility-Klassen (CSS-Bausteine)               │
│  Du schreibst: <div className="p-4 bg-white rounded-lg">    │
│  Du baust:     Dein eigenes Design zusammen                 │
│                                                             │
│  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐                        │
│  │ p-4  │ │bg-whi│ │round │ │shad  │  ──► Dein Design       │
│  └──────┘ └──────┘ └──────┘ └──────┘                        │
│                                                             │
│  Ant Design:                                                │
│  ───────────                                                │
│  Du bekommst: Fertige React-Komponenten                     │
│  Du schreibst: <Button type="primary">                      │
│  Du nutzt:     Vorgefertigtes, professionelles Design       │
│                                                             │
│  ┌──────────────────────────────────────┐                   │
│  │  <Button type="primary" size="lg">   │  ──► Fertiges     │
│  │      Klick mich                      │      Design!      │
│  │  </Button>                           │                   │
│  └──────────────────────────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

### Ant Design einrichten

```bash
# 1. Neues Projekt erstellen
npm create vite@latest antd-uebung -- --template react
cd antd-uebung
npm install

# 2. Ant Design installieren (das ist alles!)
npm install antd

# 3. Dev-Server starten
npm run dev
```

**Kein extra CSS-Import nötig!** Ant Design 5 lädt Styles automatisch per Komponente (Tree-Shaking).

> **Troubleshooting:** Falls Ant Design-Komponenten ungestylt oder „kaputt" aussehen: Stelle sicher, dass du `antd` Version 5 oder höher installiert hast (`npm list antd`). In älteren Versionen (v4 und früher) musste man CSS manuell importieren (`import 'antd/dist/antd.css'`). Falls trotzdem etwas seltsam aussieht, kann ein CSS-Reset helfen – lösche dazu den Inhalt von `src/App.css` und `src/index.css`, damit keine Vite-Standard-Styles mit Ant Design kollidieren.

### Die wichtigsten Ant Design Komponenten

#### Button

```javascript
import { Button } from 'antd';

function ButtonDemo() {
  return (
    <div>
      {/* Verschiedene Button-Typen */}
      <Button type="primary">Primary</Button>
      <Button>Default</Button>
      <Button type="dashed">Dashed</Button>
      <Button type="text">Text</Button>
      <Button type="link">Link</Button>

      {/* Größen */}
      <Button type="primary" size="large">Groß</Button>
      <Button type="primary" size="middle">Mittel</Button>
      <Button type="primary" size="small">Klein</Button>

      {/* Danger & Disabled */}
      <Button danger>Löschen</Button>
      <Button type="primary" disabled>Deaktiviert</Button>
    </div>
  );
}
```

#### Card

```javascript
import { Card, Button } from 'antd';

function CardDemo() {
  return (
    <Card
      title="Meine Card"
      extra={<a href="#">Mehr</a>}
      style={{ width: 300 }}
    >
      <p>Inhalt der Card</p>
      <p>Noch mehr Inhalt</p>
      <Button type="primary">Aktion</Button>
    </Card>
  );
}
```

#### Typography

```javascript
import { Typography } from 'antd';

const { Title, Text, Paragraph } = Typography;

function TypoDemo() {
  return (
    <div>
      <Title>h1 Überschrift</Title>
      <Title level={2}>h2 Überschrift</Title>
      <Title level={3}>h3 Überschrift</Title>

      <Text>Normaler Text</Text>
      <Text strong>Fetter Text</Text>
      <Text type="secondary">Grauer Text</Text>
      <Text type="success">Grüner Text</Text>
      <Text type="danger">Roter Text</Text>

      <Paragraph>
        Ein ganzer Absatz mit automatischem Styling.
      </Paragraph>
    </div>
  );
}
```

#### Space (Abstände)

```javascript
import { Space, Button } from 'antd';

function SpaceDemo() {
  return (
    // Space verteilt Kinder mit gleichmäßigem Abstand
    <Space size="middle">
      <Button type="primary">Speichern</Button>
      <Button>Abbrechen</Button>
      <Button danger>Löschen</Button>
    </Space>
  );
}
```

#### Input & Select

```javascript
import { Input, Select } from 'antd';

function InputDemo() {
  return (
    <div>
      <Input placeholder="Dein Name" />
      <Input.Password placeholder="Passwort" />
      <Input.TextArea rows={4} placeholder="Nachricht" />

      <Select
        defaultValue="option1"
        style={{ width: 200 }}
        options={[
          { value: 'option1', label: 'Option 1' },
          { value: 'option2', label: 'Option 2' },
          { value: 'option3', label: 'Option 3' },
        ]}
      />
    </div>
  );
}
```

#### Table

```javascript
import { Table } from 'antd';

function TableDemo() {
  // Spalten-Definitionen
  const columns = [
    { title: 'Name', dataIndex: 'name', key: 'name' },
    { title: 'Alter', dataIndex: 'alter', key: 'alter' },
    { title: 'Stadt', dataIndex: 'stadt', key: 'stadt' },
  ];

  // Daten (jede Zeile braucht einen "key")
  const data = [
    { key: '1', name: 'Anna', alter: 28, stadt: 'Berlin' },
    { key: '2', name: 'Max', alter: 34, stadt: 'München' },
    { key: '3', name: 'Lisa', alter: 22, stadt: 'Hamburg' },
  ];

  return <Table columns={columns} dataSource={data} />;
}
```

### Übung 4: Erste Schritte mit Ant Design

> **Ziel:** Ant Design Komponenten importieren und verwenden
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Du eine Seite mit verschiedenen Ant Design Komponenten siehst

Erstelle eine Seite, die verschiedene Ant Design Komponenten zeigt:

1. Ein `Title` mit dem Text "Ant Design Demo"
2. Drei `Card`-Komponenten nebeneinander (mit `Space`)
3. Jede Card mit einem Titel, Text und einem Button
4. Die Buttons sollen verschiedene `type`-Varianten haben

**Starter-Code:**

```javascript
// src/App.jsx
import { Card, Button, Typography, Space } from 'antd';

const { Title, Text } = Typography;

function App() {
  return (
    <div style={{ padding: '40px', maxWidth: '900px', margin: '0 auto' }}>
      {/* Aufgabe 1: Title hinzufügen */}

      {/* Aufgabe 2: Drei Cards mit Space */}
      <Space size="large">
        {/* Card 1: type="primary" Button */}
        {/* Card 2: default Button */}
        {/* Card 3: danger Button */}
      </Space>
    </div>
  );
}

export default App;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/App.jsx
import { Card, Button, Typography, Space } from 'antd';

const { Title, Text } = Typography;

function App() {
  return (
    <div style={{ padding: '40px', maxWidth: '900px', margin: '0 auto' }}>
      <Title>Ant Design Demo</Title>
      <Text type="secondary">
        Verschiedene Ant Design Komponenten auf einen Blick
      </Text>

      <Space size="large" style={{ marginTop: '24px', display: 'flex', flexWrap: 'wrap' }}>
        <Card title="Profil" style={{ width: 260 }}>
          <Text>Verwalte deine persönlichen Daten und Einstellungen.</Text>
          <br /><br />
          <Button type="primary">Profil bearbeiten</Button>
        </Card>

        <Card title="Benachrichtigungen" style={{ width: 260 }}>
          <Text>Du hast 3 neue Nachrichten in deinem Postfach.</Text>
          <br /><br />
          <Button>Nachrichten anzeigen</Button>
        </Card>

        <Card title="Konto" style={{ width: 260 }}>
          <Text>Möchtest du dein Konto wirklich löschen?</Text>
          <br /><br />
          <Button danger>Konto löschen</Button>
        </Card>
      </Space>
    </div>
  );
}

export default App;
```

</details>

### Wissensfrage 3

**Warum importiert man bei Ant Design `{ Button }` statt das gesamte Paket?**

<details>
<summary>Antwort anzeigen</summary>

Durch den gezielten Import einzelner Komponenten (`import { Button } from 'antd'`) wird **Tree-Shaking** ermöglicht: Nur der Code der tatsächlich verwendeten Komponenten wird in die finale App eingebunden. Würde man das gesamte Paket importieren, wäre die Bundle-Größe deutlich größer, da der Code aller Komponenten (Button, Table, Form, Modal, etc.) mitgeladen würde – auch wenn man sie gar nicht braucht.

</details>

---

## Teil 6: Ant Design – Formulare & Layout

### Formulare mit Ant Design

Ant Design bietet ein mächtiges Form-System mit eingebauter Validierung:

```javascript
import { Form, Input, Button, Select, message } from 'antd';

function KontaktFormular() {
  const onFinish = (values) => {
    console.log('Formulardaten:', values);
    message.success('Formular erfolgreich abgeschickt!');
  };

  return (
    <Form
      layout="vertical"
      onFinish={onFinish}
      style={{ maxWidth: '400px' }}
    >
      <Form.Item
        label="Name"
        name="name"
        rules={[{ required: true, message: 'Bitte gib deinen Namen ein!' }]}
      >
        <Input placeholder="Dein Name" />
      </Form.Item>

      <Form.Item
        label="E-Mail"
        name="email"
        rules={[
          { required: true, message: 'Bitte gib deine E-Mail ein!' },
          { type: 'email', message: 'Bitte gib eine gültige E-Mail ein!' }
        ]}
      >
        <Input placeholder="deine@email.de" />
      </Form.Item>

      <Form.Item
        label="Betreff"
        name="betreff"
      >
        <Select
          placeholder="Wähle einen Betreff"
          options={[
            { value: 'frage', label: 'Allgemeine Frage' },
            { value: 'feedback', label: 'Feedback' },
            { value: 'bug', label: 'Fehlermeldung' },
          ]}
        />
      </Form.Item>

      <Form.Item
        label="Nachricht"
        name="nachricht"
        rules={[{ required: true, message: 'Bitte schreibe eine Nachricht!' }]}
      >
        <Input.TextArea rows={4} placeholder="Deine Nachricht..." />
      </Form.Item>

      <Form.Item>
        <Button type="primary" htmlType="submit">
          Absenden
        </Button>
      </Form.Item>
    </Form>
  );
}
```

**Was Form.Item dir abnimmt:**
- Label automatisch über dem Feld
- Validierung beim Absenden
- Fehlermeldungen in Rot unter dem Feld
- Alle Formulardaten als Objekt im `onFinish`-Callback

### Layout mit Ant Design

Ant Design bietet ein eigenes Layout-System:

```javascript
import { Layout, Menu, Typography } from 'antd';

const { Header, Content, Footer, Sider } = Layout;
const { Title } = Typography;

function AppLayout() {
  return (
    <Layout style={{ minHeight: '100vh' }}>
      {/* Seitenleiste */}
      <Sider>
        <div style={{ color: 'white', padding: '16px', fontWeight: 'bold' }}>
          Meine App
        </div>
        <Menu
          theme="dark"
          mode="inline"
          defaultSelectedKeys={['1']}
          items={[
            { key: '1', label: 'Dashboard' },
            { key: '2', label: 'Benutzer' },
            { key: '3', label: 'Einstellungen' },
          ]}
        />
      </Sider>

      <Layout>
        {/* Kopfzeile */}
        <Header style={{ background: '#fff', padding: '0 24px' }}>
          <Title level={4} style={{ margin: '16px 0' }}>Dashboard</Title>
        </Header>

        {/* Hauptinhalt */}
        <Content style={{ margin: '24px', padding: '24px', background: '#fff' }}>
          <p>Hier kommt der Hauptinhalt hin.</p>
        </Content>

        {/* Fußzeile */}
        <Footer style={{ textAlign: 'center' }}>
          Meine App © 2025
        </Footer>
      </Layout>
    </Layout>
  );
}
```

### Row & Col – Das Grid-System

Ant Design verwendet ein **24-Spalten-Grid** (ähnlich wie Bootstrap):

```javascript
import { Row, Col, Card } from 'antd';

function GridDemo() {
  return (
    <Row gutter={[16, 16]}>
      {/* 3 gleich große Spalten: 24 / 3 = 8 */}
      <Col xs={24} sm={12} md={8}>
        <Card title="Spalte 1">Inhalt 1</Card>
      </Col>
      <Col xs={24} sm={12} md={8}>
        <Card title="Spalte 2">Inhalt 2</Card>
      </Col>
      <Col xs={24} sm={24} md={8}>
        <Card title="Spalte 3">Inhalt 3</Card>
      </Col>
    </Row>
  );
}

// xs = Extra-Small (Smartphone)       → 24 = volle Breite
// sm = Small (Tablet Hochformat)      → 12 = halbe Breite
// md = Medium (Tablet Querformat)     → 8  = ein Drittel
```

### Übung 5: Registrierungsformular mit Ant Design

> **Ziel:** Ein Formular mit Ant Design erstellen und Validierung einrichten
> **Zeitbedarf:** ca. 20 Minuten
> **Du bist fertig, wenn:** Dein Formular bei fehlenden Pflichtfeldern Fehlermeldungen anzeigt

Erstelle ein Registrierungsformular mit:

1. **Vorname** (Pflichtfeld)
2. **Nachname** (Pflichtfeld)
3. **E-Mail** (Pflichtfeld, muss gültige E-Mail sein)
4. **Rolle** (Select: "Entwickler", "Designer", "Projektmanager")
5. **Über mich** (TextArea, optional)
6. **Absenden-Button**

**Starter-Code:**

```javascript
// src/components/RegistrationForm.jsx
import { Form, Input, Button, Select, Typography, message } from 'antd';

const { Title } = Typography;

function RegistrationForm() {
  const onFinish = (values) => {
    console.log('Registrierung:', values);
    message.success('Registrierung erfolgreich!');
  };

  return (
    <div style={{ maxWidth: '500px', margin: '40px auto', padding: '24px' }}>
      <Title level={2}>Registrierung</Title>

      <Form layout="vertical" onFinish={onFinish}>
        {/* Aufgabe: Füge die Form.Items hier hinzu */}

      </Form>
    </div>
  );
}

export default RegistrationForm;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/components/RegistrationForm.jsx
import { Form, Input, Button, Select, Typography, message } from 'antd';

const { Title } = Typography;

function RegistrationForm() {
  const onFinish = (values) => {
    console.log('Registrierung:', values);
    message.success('Registrierung erfolgreich!');
  };

  return (
    <div style={{ maxWidth: '500px', margin: '40px auto', padding: '24px' }}>
      <Title level={2}>Registrierung</Title>

      <Form layout="vertical" onFinish={onFinish}>
        <Form.Item
          label="Vorname"
          name="vorname"
          rules={[{ required: true, message: 'Bitte gib deinen Vornamen ein!' }]}
        >
          <Input placeholder="Max" />
        </Form.Item>

        <Form.Item
          label="Nachname"
          name="nachname"
          rules={[{ required: true, message: 'Bitte gib deinen Nachnamen ein!' }]}
        >
          <Input placeholder="Mustermann" />
        </Form.Item>

        <Form.Item
          label="E-Mail"
          name="email"
          rules={[
            { required: true, message: 'Bitte gib deine E-Mail ein!' },
            { type: 'email', message: 'Bitte gib eine gültige E-Mail ein!' }
          ]}
        >
          <Input placeholder="max@beispiel.de" />
        </Form.Item>

        <Form.Item
          label="Rolle"
          name="rolle"
          rules={[{ required: true, message: 'Bitte wähle eine Rolle!' }]}
        >
          <Select
            placeholder="Wähle deine Rolle"
            options={[
              { value: 'entwickler', label: 'Entwickler' },
              { value: 'designer', label: 'Designer' },
              { value: 'projektmanager', label: 'Projektmanager' },
            ]}
          />
        </Form.Item>

        <Form.Item
          label="Über mich"
          name="ueber_mich"
        >
          <Input.TextArea
            rows={3}
            placeholder="Erzähl etwas über dich... (optional)"
          />
        </Form.Item>

        <Form.Item>
          <Button type="primary" htmlType="submit" size="large">
            Registrieren
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}

export default RegistrationForm;
```

</details>

---

## Teil 7: Weitere CSS-Frameworks im Überblick

Neben Tailwind CSS und Ant Design gibt es viele weitere **kostenlose** CSS-Frameworks für React. Hier ein Überblick:

### Bootstrap (react-bootstrap)

**Das bekannteste CSS-Framework der Welt.**

```bash
npm install react-bootstrap bootstrap
```

```javascript
import { Button, Card, Container, Row, Col } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

function BootstrapDemo() {
  return (
    <Container>
      <Row>
        <Col md={4}>
          <Card>
            <Card.Body>
              <Card.Title>Bootstrap Card</Card.Title>
              <Card.Text>Mit React-Bootstrap.</Card.Text>
              <Button variant="primary">Aktion</Button>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
}
```

**Vorteile:** Riesige Community, extrem gut dokumentiert, viele Tutorials online
**Nachteile:** Kann „generisch" aussehen, relativ große Bundle-Größe

### Material UI (MUI)

**Googles Material Design als React-Komponenten.**

```bash
npm install @mui/material @emotion/react @emotion/styled
```

```javascript
import { Button, Card, CardContent, Typography } from '@mui/material';

function MuiDemo() {
  return (
    <Card sx={{ maxWidth: 300 }}>
      <CardContent>
        <Typography variant="h5">MUI Card</Typography>
        <Typography color="text.secondary">
          Mit Material UI gestylt.
        </Typography>
        <Button variant="contained" sx={{ mt: 2 }}>Aktion</Button>
      </CardContent>
    </Card>
  );
}
```

**Vorteile:** Elegantes Design, mächtiges Theming, riesige Komponentenbibliothek
**Nachteile:** Komplexere API, größere Bundle-Größe, steile Lernkurve

### Chakra UI

**Accessibility-first Komponenten für React.**

```bash
npm install @chakra-ui/react
```

```javascript
import { Button, Card, CardBody, Heading, Text, ChakraProvider } from '@chakra-ui/react';

function ChakraDemo() {
  return (
    <ChakraProvider>
      <Card maxW="300px">
        <CardBody>
          <Heading size="md">Chakra Card</Heading>
          <Text mt={2}>Mit Chakra UI gestylt.</Text>
          <Button colorScheme="blue" mt={4}>Aktion</Button>
        </CardBody>
      </Card>
    </ChakraProvider>
  );
}
```

**Vorteile:** Barrierefreiheit eingebaut, intuitive API, gute DX (Developer Experience)
**Nachteile:** Kleinere Community als Bootstrap/MUI, weniger Komponenten

### Bulma

**Reines CSS-Framework – kein JavaScript.**

```bash
npm install bulma
```

```javascript
import 'bulma/css/bulma.min.css';

function BulmaDemo() {
  return (
    <div className="card" style={{ maxWidth: '300px' }}>
      <div className="card-content">
        <p className="title is-5">Bulma Card</p>
        <p className="subtitle is-6">Mit Bulma gestylt.</p>
        <button className="button is-primary">Aktion</button>
      </div>
    </div>
  );
}
```

**Vorteile:** Leichtgewichtig, einfach zu lernen, kein JavaScript nötig
**Nachteile:** Keine React-Komponenten (nur CSS-Klassen), kleinere Community

### DaisyUI

**Tailwind CSS + vorgefertigte Komponentenklassen.**

```bash
npm install -D daisyui@latest
```

```javascript
// DaisyUI baut auf Tailwind auf und fügt semantische Klassen hinzu
function DaisyDemo() {
  return (
    <div className="card w-72 bg-base-100 shadow-xl">
      <div className="card-body">
        <h2 className="card-title">DaisyUI Card</h2>
        <p>Mit DaisyUI gestylt.</p>
        <div className="card-actions justify-end">
          <button className="btn btn-primary">Aktion</button>
        </div>
      </div>
    </div>
  );
}
```

**Vorteile:** Kombiniert Tailwinds Flexibilität mit fertigen Komponenten-Klassen, viele Themes
**Nachteile:** Erfordert Tailwind CSS, eigene Klassennamen zu lernen

### Vergleichstabelle

| Framework | Typ | React-Komponenten | Lernkurve | Bundle-Größe | Beliebtheit |
|-----------|-----|-------------------|-----------|--------------|-------------|
| **Tailwind CSS** | Utility-First | Nein (nur Klassen) | Mittel | Sehr klein | Sehr hoch |
| **Ant Design** | Komponenten | Ja | Mittel | Mittel | Hoch |
| **Bootstrap** | Hybrid | Ja (react-bootstrap) | Niedrig | Mittel | Sehr hoch |
| **Material UI** | Komponenten | Ja | Hoch | Groß | Sehr hoch |
| **Chakra UI** | Komponenten | Ja | Niedrig | Mittel | Mittel |
| **Bulma** | Nur CSS | Nein | Niedrig | Klein | Mittel |
| **DaisyUI** | Utility + Klassen | Nein (Tailwind-basiert) | Niedrig | Sehr klein | Wachsend |

> **Alle genannten Frameworks sind kostenlos und Open Source!**

### Entscheidungshilfe

```
┌─────────────────────────────────────────────────────────────┐
│                WELCHES FRAMEWORK PASST?                     │
│                                                             │
│  Was ist dir wichtig?                                       │
│                                                             │
│  "Volle Kontrolle über das Design"                          │
│   └──► Tailwind CSS (oder DaisyUI für mehr Komfort)         │
│                                                             │
│  "Schnell eine professionelle Business-App bauen"           │
│   └──► Ant Design                                           │
│                                                             │
│  "Das bekannteste, meiste Hilfe online"                     │
│   └──► Bootstrap (react-bootstrap)                          │
│                                                             │
│  "Modernes, elegantes Google-Design"                        │
│   └──► Material UI (MUI)                                    │
│                                                             │
│  "Barrierefreiheit ist mir besonders wichtig"               │
│   └──► Chakra UI                                            │
│                                                             │
│  "So leichtgewichtig wie möglich"                           │
│   └──► Bulma (reines CSS) oder Tailwind CSS                 │
└─────────────────────────────────────────────────────────────┘
```

### Wissensfrage 4

**Nenne zwei Vorteile einer Komponenten-Bibliothek (wie Ant Design) gegenüber einem Utility-First-Framework (wie Tailwind CSS).**

<details>
<summary>Antwort anzeigen</summary>

1. **Schnellere Entwicklung:** Fertige Komponenten wie `<Table>`, `<Form>` oder `<Modal>` können sofort verwendet werden, ohne dass man sie selbst bauen muss.
2. **Eingebaute Funktionalität:** Komponenten wie `<Form>` bringen bereits Validierung, Fehlermeldungen und Event-Handling mit – das müsste man bei Tailwind alles selbst programmieren.

Weitere mögliche Antworten: Konsistentes Design out-of-the-box, weniger Code für komplexe UI-Elemente, professionelles Aussehen ohne Design-Kenntnisse.

</details>

---

## Teil 8: Praxis – Profilkarte mit Tailwind

Zeit, alles Gelernte über Tailwind zusammen anzuwenden!

> **Ziel:** Eine vollständige, responsive Team-Member-Profilkarte mit Tailwind CSS
> **Zeitbedarf:** ca. 30 Minuten
> **Du bist fertig, wenn:** Die Profilkarte responsive ist und Hover-Effekte hat

### Aufgabe: Team-Member-Karte

Erstelle eine Profilkarte für ein Team-Mitglied mit:

1. **Avatar** – Kreis mit Initialen (oder Bild-Platzhalter)
2. **Name & Titel** – Name groß und fett, Titel in Grau
3. **Status** – "Online" (grüner Punkt) oder "Offline" (grauer Punkt)
4. **Skills** – Als Tags/Badges dargestellt
5. **Kontakt-Buttons** – E-Mail und Profil, mit Hover-Effekten
6. **Responsive** – Auf mobil schmal, auf Desktop breiter

**Komponenten-Struktur:**

```
src/
├── components/
│   ├── TeamMember.jsx        # Hauptkomponente
│   ├── Avatar.jsx            # Avatar mit Initialen
│   └── SkillBadge.jsx        # Einzelner Skill-Badge
└── App.jsx
```

**Starter-Code:**

```javascript
// src/App.jsx
import TeamMember from './components/TeamMember';

const teamMembers = [
  {
    id: 1,
    name: 'Anna Schmidt',
    title: 'Frontend Entwicklerin',
    email: 'anna@example.com',
    online: true,
    skills: ['React', 'Tailwind', 'TypeScript'],
  },
  {
    id: 2,
    name: 'Max Weber',
    title: 'Backend Entwickler',
    email: 'max@example.com',
    online: false,
    skills: ['Node.js', 'Python', 'PostgreSQL'],
  },
  {
    id: 3,
    name: 'Lisa Braun',
    title: 'UX Designerin',
    email: 'lisa@example.com',
    online: true,
    skills: ['Figma', 'CSS', 'User Research'],
  },
];

function App() {
  return (
    <div className="min-h-screen bg-gray-100 py-12 px-4">
      <h1 className="text-3xl font-bold text-center text-gray-800 mb-8">
        Unser Team
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6
                      max-w-5xl mx-auto">
        {teamMembers.map(member => (
          <TeamMember key={member.id} member={member} />
        ))}
      </div>
    </div>
  );
}

export default App;
```

<details>
<summary>Musterlösung anzeigen</summary>

**src/components/Avatar.jsx:**

```javascript
function Avatar({ name }) {
  // Initialen aus dem Namen extrahieren
  const initialen = name
    .split(' ')
    .map(teil => teil[0])
    .join('');

  return (
    <div className="w-16 h-16 rounded-full bg-blue-500 flex items-center
                    justify-center text-white text-xl font-bold">
      {initialen}
    </div>
  );
}

export default Avatar;
```

**src/components/SkillBadge.jsx:**

```javascript
function SkillBadge({ skill }) {
  return (
    <span className="inline-block bg-blue-100 text-blue-800 text-xs
                     font-semibold px-3 py-1 rounded-full">
      {skill}
    </span>
  );
}

export default SkillBadge;
```

**src/components/TeamMember.jsx:**

```javascript
import Avatar from './Avatar';
import SkillBadge from './SkillBadge';

function TeamMember({ member }) {
  const { name, title, email, online, skills } = member;

  return (
    <div className="bg-white rounded-xl shadow p-6 transition-all duration-300
                    hover:-translate-y-1 hover:shadow-xl">
      {/* Header: Avatar + Info */}
      <div className="flex items-center gap-4">
        <Avatar name={name} />
        <div>
          <h3 className="text-lg font-bold text-gray-800">{name}</h3>
          <p className="text-sm text-gray-500">{title}</p>
        </div>
      </div>

      {/* Online-Status */}
      <div className="flex items-center gap-2 mt-4">
        <span className={`w-3 h-3 rounded-full ${
          online ? 'bg-green-500' : 'bg-gray-400'
        }`} />
        <span className={`text-sm ${
          online ? 'text-green-600' : 'text-gray-500'
        }`}>
          {online ? 'Online' : 'Offline'}
        </span>
      </div>

      {/* Skills */}
      <div className="flex flex-wrap gap-2 mt-4">
        {skills.map(skill => (
          <SkillBadge key={skill} skill={skill} />
        ))}
      </div>

      {/* Aktions-Buttons */}
      <div className="flex gap-3 mt-6">
        <a
          href={`mailto:${email}`}
          className="flex-1 text-center bg-blue-500 text-white py-2
                     rounded-lg font-semibold hover:bg-blue-600
                     transition-colors text-sm"
        >
          E-Mail
        </a>
        <button className="flex-1 text-center border border-gray-300
                           text-gray-700 py-2 rounded-lg font-semibold
                           hover:bg-gray-50 transition-colors text-sm">
          Profil
        </button>
      </div>
    </div>
  );
}

export default TeamMember;
```

</details>

---

## Teil 9: Praxis – Dashboard mit Ant Design

Jetzt bauen wir ein kleines Dashboard mit Ant Design!

> **Ziel:** Ein professionelles Mini-Dashboard mit Ant Design Komponenten
> **Zeitbedarf:** ca. 30 Minuten
> **Du bist fertig, wenn:** Dein Dashboard Statistiken, eine Tabelle und einen Button zum Hinzufügen zeigt

### Aufgabe: Produkt-Dashboard

Erstelle ein Dashboard mit:

1. **Layout** – Header mit Titel, Content-Bereich
2. **Statistik-Cards** – Gesamtprodukte, Auf Lager, Gesamtwert (mit `Card` + `Statistic`)
3. **Produkt-Tabelle** – mit Name, Kategorie, Preis, Status (mit `Table`)
4. **Suche** – Produkte in der Tabelle filtern (mit `Input.Search`)

**Daten:**

```javascript
const produkte = [
  { key: '1', name: 'Laptop Pro', kategorie: 'Elektronik', preis: 999.99, aufLager: true },
  { key: '2', name: 'Wireless Kopfhörer', kategorie: 'Audio', preis: 149.99, aufLager: true },
  { key: '3', name: 'Smart Watch', kategorie: 'Wearables', preis: 299.99, aufLager: false },
  { key: '4', name: 'USB-C Hub', kategorie: 'Zubehör', preis: 49.99, aufLager: true },
  { key: '5', name: 'Mechanische Tastatur', kategorie: 'Zubehör', preis: 179.99, aufLager: true },
  { key: '6', name: '4K Monitor', kategorie: 'Elektronik', preis: 449.99, aufLager: false },
];
```

**Starter-Code:**

```javascript
// src/App.jsx
import { useState } from 'react';
import { Layout, Typography, Card, Statistic, Table, Input, Row, Col, Tag } from 'antd';

const { Header, Content } = Layout;
const { Title } = Typography;

const alleProdukte = [
  { key: '1', name: 'Laptop Pro', kategorie: 'Elektronik', preis: 999.99, aufLager: true },
  { key: '2', name: 'Wireless Kopfhörer', kategorie: 'Audio', preis: 149.99, aufLager: true },
  { key: '3', name: 'Smart Watch', kategorie: 'Wearables', preis: 299.99, aufLager: false },
  { key: '4', name: 'USB-C Hub', kategorie: 'Zubehör', preis: 49.99, aufLager: true },
  { key: '5', name: 'Mechanische Tastatur', kategorie: 'Zubehör', preis: 179.99, aufLager: true },
  { key: '6', name: '4K Monitor', kategorie: 'Elektronik', preis: 449.99, aufLager: false },
];

function App() {
  const [suchbegriff, setSuchbegriff] = useState('');

  // Aufgabe 1: Filtere Produkte basierend auf dem Suchbegriff
  const gefilterteProdukte = // ???

  // Aufgabe 2: Berechne Statistiken
  const gesamtAnzahl = // ???
  const aufLagerAnzahl = // ???
  const gesamtWert = // ???

  // Aufgabe 3: Definiere die Tabellen-Spalten
  const columns = [
    // ???
  ];

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ background: '#001529', padding: '0 24px', display: 'flex', alignItems: 'center' }}>
        <Title level={3} style={{ color: 'white', margin: 0 }}>
          Produkt-Dashboard
        </Title>
      </Header>

      <Content style={{ padding: '24px', background: '#f0f2f5' }}>
        {/* Aufgabe 4: Statistik-Cards in einer Row */}

        {/* Aufgabe 5: Suchfeld */}

        {/* Aufgabe 6: Produkt-Tabelle */}

      </Content>
    </Layout>
  );
}

export default App;
```

<details>
<summary>Musterlösung anzeigen</summary>

```javascript
// src/App.jsx
import { useState } from 'react';
import { Layout, Typography, Card, Statistic, Table, Input, Row, Col, Tag } from 'antd';

const { Header, Content } = Layout;
const { Title } = Typography;

const alleProdukte = [
  { key: '1', name: 'Laptop Pro', kategorie: 'Elektronik', preis: 999.99, aufLager: true },
  { key: '2', name: 'Wireless Kopfhörer', kategorie: 'Audio', preis: 149.99, aufLager: true },
  { key: '3', name: 'Smart Watch', kategorie: 'Wearables', preis: 299.99, aufLager: false },
  { key: '4', name: 'USB-C Hub', kategorie: 'Zubehör', preis: 49.99, aufLager: true },
  { key: '5', name: 'Mechanische Tastatur', kategorie: 'Zubehör', preis: 179.99, aufLager: true },
  { key: '6', name: '4K Monitor', kategorie: 'Elektronik', preis: 449.99, aufLager: false },
];

function App() {
  const [suchbegriff, setSuchbegriff] = useState('');

  // Produkte filtern
  const gefilterteProdukte = alleProdukte.filter(produkt =>
    produkt.name.toLowerCase().includes(suchbegriff.toLowerCase()) ||
    produkt.kategorie.toLowerCase().includes(suchbegriff.toLowerCase())
  );

  // Statistiken berechnen
  const gesamtAnzahl = alleProdukte.length;
  const aufLagerAnzahl = alleProdukte.filter(p => p.aufLager).length;
  const gesamtWert = alleProdukte
    .reduce((summe, p) => summe + p.preis, 0)
    .toFixed(2);

  // Tabellen-Spalten
  const columns = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
      sorter: (a, b) => a.name.localeCompare(b.name),
    },
    {
      title: 'Kategorie',
      dataIndex: 'kategorie',
      key: 'kategorie',
      render: (kategorie) => <Tag color="blue">{kategorie}</Tag>,
    },
    {
      title: 'Preis',
      dataIndex: 'preis',
      key: 'preis',
      render: (preis) => `${preis.toFixed(2)} €`,
      sorter: (a, b) => a.preis - b.preis,
    },
    {
      title: 'Status',
      dataIndex: 'aufLager',
      key: 'aufLager',
      render: (aufLager) => (
        <Tag color={aufLager ? 'green' : 'red'}>
          {aufLager ? 'Auf Lager' : 'Ausverkauft'}
        </Tag>
      ),
    },
  ];

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{
        background: '#001529',
        padding: '0 24px',
        display: 'flex',
        alignItems: 'center'
      }}>
        <Title level={3} style={{ color: 'white', margin: 0 }}>
          Produkt-Dashboard
        </Title>
      </Header>

      <Content style={{ padding: '24px', background: '#f0f2f5' }}>
        {/* Statistik-Cards */}
        <Row gutter={[16, 16]} style={{ marginBottom: '24px' }}>
          <Col xs={24} sm={8}>
            <Card>
              <Statistic title="Gesamtprodukte" value={gesamtAnzahl} />
            </Card>
          </Col>
          <Col xs={24} sm={8}>
            <Card>
              <Statistic
                title="Auf Lager"
                value={aufLagerAnzahl}
                valueStyle={{ color: '#3f8600' }}
              />
            </Card>
          </Col>
          <Col xs={24} sm={8}>
            <Card>
              <Statistic
                title="Gesamtwert"
                value={gesamtWert}
                suffix="€"
              />
            </Card>
          </Col>
        </Row>

        {/* Suchfeld */}
        <Input.Search
          placeholder="Produkte suchen..."
          value={suchbegriff}
          onChange={(e) => setSuchbegriff(e.target.value)}
          style={{ marginBottom: '16px', maxWidth: '400px' }}
          allowClear
        />

        {/* Produkt-Tabelle */}
        <Card>
          <Table
            columns={columns}
            dataSource={gefilterteProdukte}
            pagination={false}
          />
        </Card>
      </Content>
    </Layout>
  );
}

export default App;
```

</details>

---

## Zusammenfassung

### Was du heute gelernt hast

| Konzept | Beschreibung | Beispiel |
|---------|--------------|----------|
| **Inline Styles** | Style als JS-Objekt | `style={{ color: 'red' }}` |
| **CSS-Dateien** | Globale CSS importieren | `import './App.css'` |
| **CSS Modules** | Scoped CSS per Komponente | `import styles from './X.module.css'` |
| **Tailwind CSS** | Utility-First Framework | `className="bg-blue-500 p-4"` |
| **Responsive (Tailwind)** | Mobile-First Breakpoints | `className="grid md:grid-cols-2"` |
| **Hover (Tailwind)** | State-Prefixes | `className="hover:bg-blue-600"` |
| **Ant Design** | Komponenten-Bibliothek | `<Button type="primary">` |
| **Ant Design Form** | Formulare mit Validierung | `<Form><Form.Item rules={...}>` |
| **Ant Design Table** | Datentabellen | `<Table columns={...} dataSource={...}>` |
| **Framework-Wahl** | Richtige Wahl treffen | Utility-First vs. Komponenten |

### CSS-Ansätze auf einen Blick

```javascript
// 1. Inline Styles – für dynamische Werte
<div style={{ width: `${progress}%` }}>

// 2. CSS-Datei – für einfache, globale Styles
import './App.css';
<div className="card">

// 3. CSS Modules – für scoped Styles (empfohlen!)
import styles from './Card.module.css';
<div className={styles.card}>

// 4. Tailwind CSS – Utility-Klassen direkt im JSX
<div className="bg-white p-4 rounded-xl shadow-lg">

// 5. Ant Design – fertige React-Komponenten
<Card title="Titel"><Button type="primary">Klick</Button></Card>
```

### Entscheidung auf einen Blick

```javascript
// Eigenes, einzigartiges Design?    → Tailwind CSS
// Schnell professionelle App?       → Ant Design oder MUI
// Bekanntestes Framework?           → Bootstrap
// Barrierefreiheit wichtig?         → Chakra UI
// So leicht wie möglich?            → Bulma oder Tailwind
```

---

## Vorbereitung auf morgen

Mit dem Wissen über CSS-Frameworks und Styling in React bist du bestens vorbereitet für:

- **Fortgeschrittene React-Patterns** – Custom Hooks, Context API
- **Vollständige App-Projekte** – Mit professionellem Styling
- **Echte Projekt-Arbeit** – Framework wählen und produktiv einsetzen

> **Tipp:** Wähle für dein nächstes Projekt **ein** Framework und bleibe dabei. Es ist besser, ein Framework gut zu kennen, als fünf nur oberflächlich.

---

## Checkliste

Bevor du mit der nächsten Übung weitermachst, stelle sicher:

- [ ] Du kennst die drei CSS-Ansätze in React (Inline, CSS-Dateien, CSS Modules)
- [ ] Du verstehst, warum CSS-Frameworks die Entwicklung beschleunigen
- [ ] Du kannst Tailwind CSS in einem Vite-Projekt einrichten
- [ ] Du kannst Tailwind-Utility-Klassen für Spacing, Farben und Layout verwenden
- [ ] Du kannst responsive Layouts mit Tailwind-Breakpoints erstellen
- [ ] Du kannst Ant Design installieren und Komponenten importieren
- [ ] Du kannst Ant Design Komponenten (Button, Card, Form, Table) verwenden
- [ ] Du kennst weitere kostenlose CSS-Frameworks und ihre Einsatzgebiete
- [ ] Du kannst einschätzen, wann welches Framework die richtige Wahl ist

**Alles abgehakt?** Du bist bereit für fortgeschrittene React-Patterns und echte Projekt-Arbeit!
