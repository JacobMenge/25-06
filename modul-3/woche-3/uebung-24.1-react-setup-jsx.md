# React Setup & JSX - Praktische Übung

## Übersicht

Willkommen zu deinem ersten React-Projekt! In dieser Übung lernst du, wie du ein React-Projekt mit Vite aufsetzt und die Grundlagen von JSX verstehst.

In dieser Übung lernst du:
- **Vite** - Das schnelle Build-Tool für moderne Web-Projekte
- **React-Projektstruktur** - Welche Dateien was machen
- **JSX-Syntax** - HTML in JavaScript schreiben
- **Komponenten** - Die Bausteine von React

---

## Inhaltsverzeichnis

| Teil | Thema | Zeitbedarf |
|------|-------|------------|
| **Teil 1** | Was ist Vite? | 5 min (lesen) |
| **Teil 2** | React-Projekt erstellen | 10 min |
| **Teil 3** | Projektstruktur verstehen | 10 min |
| **Teil 4** | JSX-Grundlagen | 15 min |
| **Teil 5** | Erste eigene Komponente | 15 min |
| **Teil 6** | JSX-Ausdrücke & Variablen | 15 min |
| | **Gesamt** | **ca. 70 Minuten** |

---

## Teil 1: Was ist Vite?

### Warum Vite?

**Vite** (französisch für "schnell") ist ein modernes Build-Tool, das die Entwicklung von React-Projekten extrem schnell macht.

```
┌─────────────────────────────────────────────────────────────┐
│                        VITE                                  │
│                                                              │
│  - Blitzschneller Dev-Server (unter 1 Sekunde Start)        │
│  - Hot Module Replacement (HMR) - Änderungen sofort sichtbar│
│  - Optimierter Production Build                              │
│  - Unterstützt React, Vue, Svelte und mehr                  │
│  - Modernes ES-Modules-basiertes Bundling                   │
└─────────────────────────────────────────────────────────────┘
```

### Vite vs. Create React App

| Aspekt | Create React App (alt) | Vite (modern) |
|--------|------------------------|---------------|
| **Start-Zeit** | 20-30 Sekunden | Unter 1 Sekunde |
| **HMR** | Langsamer | Instant |
| **Bundle-Größe** | Größer | Kleiner |
| **Konfiguration** | Versteckt | Transparent |
| **Status** | Nicht mehr empfohlen | Aktuelle Best Practice |

**Fazit:** Vite ist der aktuelle Standard für neue React-Projekte!

---

## Teil 2: React-Projekt erstellen

### Voraussetzungen prüfen

Stelle sicher, dass Node.js installiert ist:

```bash
node --version
```
**Erwartete Ausgabe:** `v20.19+` oder `v22.12+` (ältere Minor-Versionen von Node 20/22 können Probleme machen)

```bash
npm --version
```
**Erwartete Ausgabe:** `10.x.x` oder neuer

### Übung 1: Projekt erstellen

> **Ziel:** Ein neues React-Projekt mit Vite erstellen
> **Zeitbedarf:** ca. 10 Minuten
> **Du bist fertig, wenn:** Der Dev-Server läuft und du die React-Seite im Browser siehst

**Schritt 1:** Öffne das Terminal und navigiere zu deinem Übungsordner.

**Schritt 2:** Erstelle ein neues Projekt mit diesem Befehl:

```bash
npm create vite@latest meine-erste-react-app -- --template react
```

**Was passiert hier?**
- `npm create vite@latest` - Führt den Vite-Projekt-Generator aus
- `meine-erste-react-app` - Name deines Projekts (frei wählbar)
- `--template react` - Verwendet die React-Vorlage (JavaScript, nicht TypeScript)

> **Windows-Hinweis:** Falls du eine Fehlermeldung bekommst, dass das Template nicht erkannt wird, versuche den Befehl in zwei Schritten:
> ```bash
> npm create vite@latest meine-erste-react-app
> ```
> Dann wähle im interaktiven Menü "React" und "JavaScript" aus.

**Schritt 3:** Wechsle in das neue Projektverzeichnis:

```bash
cd meine-erste-react-app
```

**Schritt 4:** Installiere die Abhängigkeiten:

```bash
npm install
```

**Schritt 5:** Starte den Entwicklungsserver:

```bash
npm run dev
```

**Erwartete Ausgabe:**
```
  VITE vX.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
```

**Schritt 6:** Öffne `http://localhost:5173/` im Browser.

> **Hinweis:** Falls Port 5173 bereits belegt ist, wählt Vite automatisch einen anderen Port (z.B. 5174). Schau einfach in der Terminal-Ausgabe nach der korrekten URL.

Du solltest die Vite + React Startseite sehen mit einem animierten Logo und einem Counter-Button!

---

## Teil 3: Projektstruktur verstehen

### Die wichtigsten Dateien

Nach dem Erstellen hast du folgende Struktur:

```
meine-erste-react-app/
├── node_modules/       # Installierte Pakete (nicht anfassen!)
├── public/             # Statische Dateien (Favicon etc.)
├── src/                # DEIN CODE LEBT HIER!
│   ├── App.css         # Styles für App-Komponente
│   ├── App.jsx         # Haupt-Komponente
│   ├── index.css       # Globale Styles
│   └── main.jsx        # Einstiegspunkt der App
├── index.html          # HTML-Grundgerüst
├── package.json        # Projekt-Konfiguration & Abhängigkeiten
└── vite.config.js      # Vite-Konfiguration
```

### Die wichtigsten Dateien erklärt

**`index.html`** - Das HTML-Grundgerüst:
```html
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + React</title>
  </head>
  <body>
    <div id="root"></div>           <!-- Hier wird React eingehängt! -->
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>
```

**`src/main.jsx`** - Der Einstiegspunkt:
```javascript
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

**Was passiert hier?**
1. `createRoot(document.getElementById('root'))` - Verbindet React mit dem `<div id="root">`
2. `.render(<App />)` - Rendert die App-Komponente
3. `<StrictMode>` - Aktiviert zusätzliche Prüfungen (z.B. werden manche Funktionen doppelt aufgerufen, um Probleme zu finden - das ist normal!)

**`src/App.jsx`** - Deine Haupt-Komponente (hier arbeitest du!)

### Wissensfrage 1

Warum heißen React-Dateien `.jsx` und nicht `.js`?

<details>
<summary>Antwort anzeigen</summary>

**JSX = JavaScript + XML**

Die Dateiendung `.jsx` signalisiert, dass die Datei JSX-Syntax enthält - also HTML-ähnlichen Code innerhalb von JavaScript.

```javascript
// Das ist JSX - sieht aus wie HTML, ist aber JavaScript!
const element = <h1>Hallo Welt!</h1>;
```

Technisch funktioniert auch `.js`, aber `.jsx` ist Best Practice weil:
- Editoren bieten besseres Syntax-Highlighting
- Es ist sofort klar, dass die Datei React-Komponenten enthält
- Viele Tools behandeln `.jsx`-Dateien speziell

</details>

---

## Teil 4: JSX-Grundlagen

### Was ist JSX?

JSX ist eine Syntax-Erweiterung für JavaScript, die es dir erlaubt, HTML-ähnlichen Code zu schreiben:

```javascript
// Das ist JSX:
const element = <h1>Hallo Welt!</h1>;
```

**Was passiert im Hintergrund?**
Das Build-Tool (Vite) kompiliert JSX zu JavaScript-Funktionsaufrufen. Du musst das nicht selbst schreiben - es passiert automatisch. Das Konzept ist aber gut zu wissen: JSX ist kein echtes HTML, sondern wird in JavaScript umgewandelt.

> **Info:** Moderne Toolchains nutzen den "New JSX Transform" (Standard seit React 17). Deshalb musst du `import React from 'react'` nicht mehr in jede Datei schreiben - das passiert automatisch.

### Die wichtigsten JSX-Regeln

**Regel 1: Ein Wurzelelement**

JSX muss **immer** ein einzelnes Wurzelelement haben:

```javascript
// FALSCH - Zwei Wurzelelemente
return (
    <h1>Titel</h1>
    <p>Text</p>
);

// RICHTIG - Ein Wrapper-Element
return (
    <div>
        <h1>Titel</h1>
        <p>Text</p>
    </div>
);

// RICHTIG - Fragment (kein extra DOM-Element)
return (
    <>
        <h1>Titel</h1>
        <p>Text</p>
    </>
);
```

**Regel 2: className statt class**

```javascript
// FALSCH - 'class' ist ein reserviertes Wort in JavaScript
<div class="container">

// RICHTIG - 'className' verwenden
<div className="container">
```

**Regel 3: Selbstschließende Tags**

```javascript
// FALSCH in JSX
<img src="bild.jpg">
<input type="text">

// RICHTIG - Selbstschließend mit />
<img src="bild.jpg" />
<input type="text" />
```

**Regel 4: camelCase für Attribute**

```javascript
// HTML:
<div onclick="...">
<label for="name">

// JSX:
<div onClick={...}>
<label htmlFor="name">
```

### Übung 2: App.jsx verstehen und anpassen

> **Ziel:** Die Standard-App verstehen und erste Änderungen machen
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Du den Titel und Text der App geändert hast

**Aufgabe:**

1. Öffne `src/App.jsx` in deinem Editor
2. Lies den Code und verstehe die Struktur
3. Ersetze den gesamten Inhalt mit diesem vereinfachten Code:

```javascript
import './App.css'

function App() {
  return (
    <div className="app">
      <h1>Meine erste React-App</h1>
      <p>Willkommen zu React!</p>
    </div>
  )
}

export default App
```

4. Speichere und beobachte wie der Browser automatisch aktualisiert wird (Hot Module Replacement!)

5. Experimentiere: Ändere den Text und beobachte die sofortige Aktualisierung.

---

## Teil 5: Erste eigene Komponente

### Was ist eine Komponente?

Eine **Komponente** ist eine wiederverwendbare UI-Einheit. In React ist eine Komponente einfach eine Funktion, die JSX zurückgibt:

```javascript
// Eine einfache Komponente
function Greeting() {
  return <h1>Hallo!</h1>;
}

// Als Arrow Function (auch üblich)
const Greeting = () => {
  return <h1>Hallo!</h1>;
};
```

### Komponenten-Regeln

1. **Name beginnt mit Großbuchstaben** - `Greeting`, nicht `greeting`
2. **Gibt JSX zurück** - Das ist die UI der Komponente
3. **Kann Props empfangen** - Daten von außen (kommt später)

### Übung 3: Eigene Komponente erstellen

> **Ziel:** Eine eigene Komponente erstellen und verwenden
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Deine Greeting-Komponente in der App angezeigt wird

**Schritt 1:** Erstelle eine neue Datei `src/Greeting.jsx`:

```javascript
function Greeting() {
  return (
    <div className="greeting">
      <h2>Willkommen!</h2>
      <p>Schön, dass du hier bist.</p>
    </div>
  );
}

export default Greeting;
```

**Schritt 2:** Importiere und verwende die Komponente in `src/App.jsx`:

```javascript
import './App.css'
import Greeting from './Greeting'

function App() {
  return (
    <div className="app">
      <h1>Meine erste React-App</h1>
      <Greeting />
      <Greeting />
      <Greeting />
    </div>
  )
}

export default App
```

**Schritt 3:** Speichere und beobachte das Ergebnis im Browser.

Du siehst jetzt dreimal die Greeting-Komponente! Das zeigt die **Wiederverwendbarkeit** von Komponenten.

### Wissensfrage 2

Warum müssen Komponenten-Namen mit einem Großbuchstaben beginnen?

<details>
<summary>Antwort anzeigen</summary>

React unterscheidet zwischen HTML-Elementen und Komponenten anhand der Groß-/Kleinschreibung:

```javascript
// Kleinbuchstabe = HTML-Element
<div>     → Wird zu einem echten <div>
<span>    → Wird zu einem echten <span>

// Großbuchstabe = React-Komponente
<Greeting /> → React sucht nach einer Komponente namens Greeting
<MyButton /> → React sucht nach einer Komponente namens MyButton
```

Wenn du `<greeting />` schreibst, denkt React, es sei ein unbekanntes HTML-Element!

</details>

---

## Teil 6: JSX-Ausdrücke & Variablen

### JavaScript in JSX einbetten

Mit **geschweiften Klammern `{}`** kannst du JavaScript-Ausdrücke in JSX einbetten:

```javascript
function App() {
  const name = "Max";
  const age = 25;

  return (
    <div>
      <h1>Hallo {name}!</h1>
      <p>Du bist {age} Jahre alt.</p>
      <p>Nächstes Jahr bist du {age + 1}.</p>
    </div>
  );
}
```

### Was kann in {} stehen?

```javascript
// Variablen
{name}

// Berechnungen
{price * quantity}

// Funktionsaufrufe
{formatDate(today)}

// Ternary Operator
{isLoggedIn ? "Willkommen" : "Bitte einloggen"}

// Array-Methoden
{items.map(item => <li>{item}</li>)}

// NICHT: Statements wie if, for, while
// Diese brauchen andere Lösungen
```

### Übung 4: Dynamische Inhalte

> **Ziel:** JavaScript-Variablen in JSX verwenden
> **Zeitbedarf:** ca. 15 Minuten
> **Du bist fertig, wenn:** Deine Profilkarte dynamische Daten anzeigt

**Aufgabe:**

Erstelle eine neue Datei `src/ProfileCard.jsx`:

```javascript
function ProfileCard() {
  // Daten
  const name = "Max Mustermann";
  const role = "Frontend Developer";
  const skills = ["React", "JavaScript", "CSS"];
  const isAvailable = true;

  return (
    <div className="profile-card">
      <h2>{name}</h2>
      <p className="role">{role}</p>

      {/* Status mit Ternary Operator */}
      <p className="status">
        Status: {isAvailable ? "Verfügbar" : "Beschäftigt"}
      </p>

      {/* Skills als Liste */}
      <h3>Skills:</h3>
      <ul>
        {skills.map((skill) => (
          <li key={skill}>{skill}</li>
        ))}
      </ul>
    </div>
  );
}

export default ProfileCard;
```

> **Hinweis zum `key`:** Der `key` muss eindeutig sein. Hier funktioniert `key={skill}`, weil alle Skills unterschiedlich sind. Bei doppelten Werten würdest du den Index nutzen: `key={index}` (als zweiter Parameter von map).

Verwende die Komponente in `App.jsx`:

```javascript
import './App.css'
import Greeting from './Greeting'
import ProfileCard from './ProfileCard'

function App() {
  return (
    <div className="app">
      <h1>Meine erste React-App</h1>
      <Greeting />
      <ProfileCard />
    </div>
  )
}

export default App
```

**Bonus:** Ändere die Daten in `ProfileCard.jsx` und beobachte die Änderungen!

---

## Zusammenfassung

### Was du heute gelernt hast

| Thema | Was du jetzt kannst |
|-------|---------------------|
| **Vite** | Ein React-Projekt mit Vite erstellen und starten |
| **Projektstruktur** | Die wichtigsten Dateien verstehen |
| **JSX** | HTML-ähnlichen Code in JavaScript schreiben |
| **Komponenten** | Eigene UI-Bausteine erstellen |
| **Ausdrücke** | JavaScript-Variablen in JSX einbetten |

### Die wichtigsten Befehle

```bash
# Neues Projekt erstellen
npm create vite@latest projektname -- --template react

# In Projektordner wechseln
cd projektname

# Abhängigkeiten installieren
npm install

# Dev-Server starten
npm run dev

# Für Production bauen
npm run build
```

### JSX-Regeln auf einen Blick

```javascript
// 1. Ein Wurzelelement (oder Fragment <>)
return (
  <div>...</div>
);

// 2. className statt class
<div className="container">

// 3. Selbstschließende Tags
<img src="..." />

// 4. camelCase für Events
<button onClick={...}>

// 5. JavaScript in {}
<h1>Hallo {name}!</h1>
```

---

## Troubleshooting

**Browser zeigt weiße Seite / Fehler "Failed to load"**
- Prüfe, ob alle Dateien korrekt benannt sind (`App.jsx`, nicht `app.jsx`)
- Prüfe die Import-Pfade (z.B. `./Greeting` nicht `./greeting`)
- Schau in die Browser-Konsole (F12) für Fehlermeldungen

**Terminal zeigt "Port already in use"**
- Vite wählt automatisch einen anderen Port - schau in die Ausgabe
- Oder beende andere laufende Dev-Server

**Änderungen werden nicht angezeigt**
- Speichere die Datei (Strg+S / Cmd+S)
- Prüfe, ob der Dev-Server noch läuft
- Bei hartnäckigen Problemen: Dev-Server neu starten (Strg+C, dann `npm run dev`)

**Windows: Projekt lässt sich nicht erstellen / hängt**
- Prüfe, ob dein Projektpfad Leerzeichen oder Sonderzeichen enthält
- Lege das Projekt testweise in einen einfachen Pfad (z.B. `C:\dev\mein-projekt`)
- Alternative: Nutze WSL (Windows Subsystem for Linux)

---

## Checkliste

Bevor du mit der nächsten Übung weitermachst, stelle sicher:

- [ ] Du kannst ein React-Projekt mit Vite erstellen
- [ ] Du verstehst die Projektstruktur (index.html, main.jsx, App.jsx)
- [ ] Du kennst die JSX-Grundregeln (className, selbstschließende Tags, ein Wurzelelement)
- [ ] Du kannst eigene Komponenten erstellen und exportieren
- [ ] Du kannst Komponenten importieren und verwenden
- [ ] Du kannst JavaScript-Ausdrücke in JSX mit {} einbetten

**Alles abgehakt?** Du bist bereit für Props & State!
