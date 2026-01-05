# CSS Grundlagen: Styling, Selektoren & Debugging - Praktische Übungen

## Übersicht

In dieser Übung vertiefst du dein Wissen über:
- **CSS als Asset** - CSS als eigener HTTP-Request
- **CSS-Syntax** - Selektoren und Deklarationen
- **Selektoren** - Klassen als Team-Standard
- **Kaskade & Spezifität** - Wer gewinnt?
- **Box Model** - Content, Padding, Border, Margin
- **DevTools-Debugging** - Styles und Computed

Diese Übung baut auf Tag 1 und 2 auf und bereitet dich auf das Freitags-Projekt vor.

---

## Teil 1: CSS als Asset verstehen

### CSS wird separat geladen

Wenn der Browser HTML parst und ein `<link rel="stylesheet">` findet, startet er einen neuen HTTP-Request:

```html
<head>
  <link rel="stylesheet" href="/css/styles.css">
</head>
```

### Im Network Tab sichtbar

| Name | Status | Type | Content-Type |
|------|--------|------|--------------|
| index.html | 200 | document | text/html |
| styles.css | 200 | stylesheet | text/css |

**Häufige Probleme:**
- **404** → Pfad falsch oder Datei fehlt
- **Falscher MIME-Type** → Server-Konfiguration prüfen
- **Cache** → "Änderung nicht sichtbar" → Hard Reload!

### Wissensfrage 1

Deine CSS-Änderungen werden im Browser nicht angezeigt, obwohl du die Datei gespeichert hast. Was sind die ersten zwei Dinge, die du prüfen solltest?

<details>
<summary>Antwort anzeigen</summary>

1. **Hard Reload durchführen:**
   - Windows: `Strg + Shift + R`
   - Mac: `Cmd + Shift + R`
   - Oder: DevTools öffnen → Rechtsklick auf Reload → "Empty Cache and Hard Reload"

2. **Network Tab prüfen:**
   - Wird die CSS-Datei geladen? (Status 200?)
   - Steht "from cache" dabei? → Cache-Problem
   - Content-Type = text/css?

**Pro-Tipp:** Während der Entwicklung im Network Tab "Disable cache" aktivieren (nur bei offenen DevTools aktiv).

</details>

---

## Teil 2: CSS Grundsyntax

### Aufbau einer CSS-Regel

```css
/* Grundaufbau */
selektor {
  eigenschaft: wert;
  eigenschaft: wert;
}

/* Konkretes Beispiel */
.card {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  margin-bottom: 16px;
}
```

### Bestandteile erklärt

| Teil | Bedeutung |
|------|-----------|
| Selektor | Wählt Elemente aus (`.card`) |
| `{ }` | Deklarationsblock |
| Eigenschaft | Was geändert wird (`padding`) |
| Wert | Der konkrete Wert (`20px`) |
| `;` | Trennt Deklarationen |
| `/* */` | Kommentar |

### Wichtige Einheiten

| Einheit | Bedeutung | Beispiel |
|---------|-----------|----------|
| `px` | Pixel (absolut) | `16px` |
| `rem` | Relativ zur Root-Schriftgröße | `1.5rem` |
| `em` | Relativ zur Eltern-Schriftgröße | `1.2em` |
| `%` | Relativ zum Elternelement | `100%` |
| `vh/vw` | Viewport Height/Width | `100vh` |

---

## Teil 3: Übung - Dein erstes Stylesheet

### Aufgabe

Erstelle ein CSS-Stylesheet für deine HTML-Seite von gestern:

1. Erstelle eine neue Datei: `style.css`
2. Binde sie in dein HTML ein
3. Style folgende Elemente:
   - `body`: Hintergrundfarbe, Schriftart
   - `h1`: Textfarbe
   - `p`: Schriftgröße, Zeilenhöhe
   - `a`: Farbe, ohne Unterstreichung bei hover

**Schritte:**
1. CSS-Datei erstellen
2. Im `<head>` verlinken: `<link rel="stylesheet" href="style.css">`
3. Regeln schreiben
4. Im Network Tab prüfen: Wird CSS geladen?

<details>
<summary>Musterlösung anzeigen</summary>

```css
/* Basis-Styling für die Seite */

/* Body - Grundeinstellungen */
body {
  font-family: Arial, Helvetica, sans-serif;
  background-color: #f5f5f5;
  color: #333333;
  margin: 0;
  padding: 20px;
  line-height: 1.6;
}

/* Überschriften */
h1 {
  color: #1a1a2e;
  font-size: 2.5rem;
  margin-bottom: 10px;
}

h2 {
  color: #16213e;
  font-size: 1.8rem;
  margin-top: 30px;
}

/* Absätze */
p {
  font-size: 1rem;
  line-height: 1.8;
  margin-bottom: 15px;
}

/* Links */
a {
  color: #0066cc;
  text-decoration: none;
}

a:hover {
  color: #004499;
  text-decoration: underline;
}
```

**Im HTML einbinden:**
```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meine Seite</title>
  <link rel="stylesheet" href="style.css">
</head>
```

**Prüfen im Network Tab:**
- Status: 200
- Type: stylesheet
- Content-Type: text/css

</details>

---

## Teil 4: CSS Selektoren

### Die wichtigsten Selektoren

| Typ | Syntax | Beispiel | Trifft auf |
|-----|--------|----------|------------|
| Element | `p` | `p { }` | Alle `<p>` |
| Klasse | `.name` | `.card { }` | `class="card"` |
| ID | `#name` | `#header { }` | `id="header"` |
| Nachfahre | `a b` | `.nav a { }` | `<a>` in `.nav` |
| Multi-Klasse | `.a.b` | `.btn.primary { }` | Beide Klassen |
| Alle Kinder | `a > b` | `ul > li { }` | Direkte Kinder |

### Warum Klassen in Teams bevorzugt werden

**IDs (`#id`):**
- Nur 1x pro Seite erlaubt
- Hohe Spezifität (schwer zu überschreiben)
- Nicht wiederverwendbar

**Klassen (`.class`):**
- Beliebig oft verwendbar
- Mittlere Spezifität
- Kombinierbar (`.btn.large.primary`)
- Explizit im HTML sichtbar

**Element-Selektoren (`p`, `div`):**
- Sehr breit (trifft alle Elemente)
- Niedrige Spezifität
- Für Basis-Styling geeignet

### Wissensfrage 2

Warum solltest du für Styling hauptsächlich Klassen statt IDs verwenden?

<details>
<summary>Antwort anzeigen</summary>

**Klassen sind besser für Styling, weil:**

1. **Wiederverwendbar:** Ein Stil für viele Elemente
   ```html
   <div class="card">...</div>
   <div class="card">...</div>
   <div class="card">...</div>
   ```

2. **Wartbar:** Änderung an einer Stelle wirkt überall
   ```css
   .card {
     background: white;
     border-radius: 8px;
   }
   ```

3. **Kombinierbar:** Mehrere Klassen für Varianten
   ```html
   <button class="btn primary large">Klick mich</button>
   ```

4. **Moderate Spezifität:** Leicht zu überschreiben wenn nötig
   - `.card` = 0-1-0
   - `#header` = 1-0-0 (10x stärker!)

5. **Explizit:** Im HTML sieht man, welcher Stil angewendet wird

**IDs sind besser für:**
- JavaScript (Element finden)
- Formular-Labels (`for="id"`)
- Anker-Links (`href="#section"`)

</details>

---

## Teil 5: Pseudo-Klassen

### Zustände stylen

Pseudo-Klassen wählen Elemente basierend auf ihrem Zustand:

```css
/* Maus über Element */
.btn:hover {
  background-color: darkblue;
  cursor: pointer;
}

/* Element hat Fokus (Tastatur) */
.input:focus {
  border-color: blue;
  outline: 2px solid lightblue;
}

/* Element wird geklickt */
.btn:active {
  transform: scale(0.98);
}

/* Besuchter Link */
a:visited {
  color: purple;
}
```

### Wichtige Pseudo-Klassen

| Pseudo-Klasse | Wann aktiv |
|---------------|------------|
| `:hover` | Maus ist über dem Element |
| `:focus` | Element hat Tastatur-Fokus |
| `:active` | Element wird geklickt |
| `:visited` | Link wurde besucht |
| `:first-child` | Erstes Kind-Element |
| `:last-child` | Letztes Kind-Element |
| `:disabled` | Deaktiviertes Formularfeld |

### Übung 2: Interaktive Elemente stylen

**Aufgabe:**

Füge deinem Stylesheet Hover- und Focus-Styles hinzu:

1. Links sollen bei Hover die Farbe wechseln
2. Buttons sollen bei Hover dunkler werden
3. Input-Felder sollen bei Focus einen blauen Rahmen bekommen

<details>
<summary>Musterlösung anzeigen</summary>

```css
/* Links */
a {
  color: #0066cc;
  text-decoration: none;
  transition: color 0.2s ease;
}

a:hover {
  color: #004499;
  text-decoration: underline;
}

a:focus {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

/* Buttons */
button {
  background-color: #0066cc;
  color: white;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

button:hover {
  background-color: #004499;
}

button:active {
  transform: scale(0.98);
}

button:focus {
  outline: 2px solid #004499;
  outline-offset: 2px;
}

/* Input-Felder */
input, textarea {
  border: 2px solid #cccccc;
  padding: 10px;
  font-size: 1rem;
  transition: border-color 0.2s ease;
}

input:focus, textarea:focus {
  border-color: #0066cc;
  outline: none;
}
```

**Wichtig:**
- `transition` sorgt für sanfte Übergänge
- Niemals `outline: none` ohne Alternative (Accessibility!)
- `:focus` ist wichtig für Tastatur-Navigation

</details>

---

## Teil 6: Kaskade & Spezifität

### Die Kaskade: Wer gewinnt?

Wenn mehrere Regeln auf ein Element zutreffen:

**1. Spezifität** (wichtigste)
```css
#header { color: red; }    /* 1-0-0 - gewinnt! */
.header { color: blue; }   /* 0-1-0 */
header { color: green; }   /* 0-0-1 */
```

**2. Reihenfolge** (bei gleicher Spezifität)
```css
.card { color: red; }
.card { color: blue; }  /* gewinnt - kommt später */
```

### Spezifität berechnen

| Selektor | Berechnung | Ergebnis |
|----------|------------|----------|
| `p` | 0-0-1 | 1 |
| `.card` | 0-1-0 | 10 |
| `#header` | 1-0-0 | 100 |
| `.nav .link` | 0-2-0 | 20 |
| `#main .card p` | 1-1-1 | 111 |

**Merke:** ID > Klasse > Element

### Vererbung

**Was vererbt wird:**
- `font-family`
- `color`
- `line-height`
- `text-align`

**Was NICHT vererbt wird:**
- `margin`
- `padding`
- `border`
- `background`

### Wissensfrage 3

Welche Farbe hat der Text?

```css
.container p { color: blue; }
p { color: red; }
```

```html
<div class="container">
  <p>Welche Farbe habe ich?</p>
</div>
```

<details>
<summary>Antwort anzeigen</summary>

**Der Text ist blau!**

Warum?
- `.container p` hat Spezifität 0-1-1 (Klasse + Element)
- `p` hat Spezifität 0-0-1 (nur Element)

0-1-1 > 0-0-1, also gewinnt `.container p`.

Die Reihenfolge im CSS spielt hier keine Rolle, weil die Spezifität unterschiedlich ist.

</details>

---

## Teil 7: Das CSS Box Model

### Jedes Element ist eine Box

```
┌─────────────────────────────────────────┐
│                 MARGIN                   │
│   ┌─────────────────────────────────┐   │
│   │            BORDER                │   │
│   │   ┌─────────────────────────┐   │   │
│   │   │        PADDING           │   │   │
│   │   │   ┌─────────────────┐   │   │   │
│   │   │   │     CONTENT      │   │   │   │
│   │   │   └─────────────────┘   │   │   │
│   │   └─────────────────────────┘   │   │
│   └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

### Die 4 Bereiche

| Bereich | Bedeutung | Eigenschaft |
|---------|-----------|-------------|
| Content | Der eigentliche Inhalt | `width`, `height` |
| Padding | Innenabstand | `padding` |
| Border | Rahmen | `border` |
| Margin | Außenabstand | `margin` |

### Box Model in CSS

```css
.card {
  /* Content-Größe */
  width: 300px;
  height: 200px;

  /* Padding - Innenabstand */
  padding: 20px;           /* alle Seiten */
  padding: 10px 20px;      /* oben/unten | links/rechts */
  padding: 10px 20px 15px; /* oben | links/rechts | unten */
  padding: 5px 10px 15px 20px; /* oben | rechts | unten | links */

  /* Border - Rahmen */
  border: 2px solid gray;

  /* Margin - Außenabstand */
  margin: 16px;
  margin-bottom: 32px;  /* nur unten */
}
```

### Box-Sizing

**Standardverhalten (`content-box`):**
- `width: 300px` = nur Content-Breite
- Gesamtbreite = 300 + padding + border

**Besseres Verhalten (`border-box`):**
- `width: 300px` = Gesamtbreite inkl. padding + border

```css
/* Best Practice - am Anfang des CSS */
*, *::before, *::after {
  box-sizing: border-box;
}
```

### Übung 3: Box Model anwenden

**Aufgabe:**

Style eine "Card"-Komponente mit Box Model:

1. Feste Breite: 300px
2. Weißer Hintergrund
3. Innenabstand: 20px
4. Grauer Rahmen: 1px solid
5. Abgerundete Ecken: 8px
6. Außenabstand unten: 20px

<details>
<summary>Musterlösung anzeigen</summary>

```css
/* Box-Sizing für alle Elemente */
*, *::before, *::after {
  box-sizing: border-box;
}

/* Card-Komponente */
.card {
  width: 300px;
  background-color: white;
  padding: 20px;
  border: 1px solid #cccccc;
  border-radius: 8px;
  margin-bottom: 20px;
}

/* Optional: Schatten für mehr Tiefe */
.card {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
```

**HTML:**
```html
<div class="card">
  <h3>Kartenüberschrift</h3>
  <p>Dies ist der Inhalt meiner Karte.</p>
</div>
```

</details>

---

## Teil 8: CSS in DevTools debuggen

### Elements → Styles

Zeigt alle CSS-Regeln, die auf das ausgewählte Element zutreffen:

- **Durchgestrichen** = überschrieben (von spezifischerer Regel)
- **Grau** = nicht aktiv (Browser-Default)
- **Checkbox** = Regel ein/ausschalten
- **Wert klicken** = live bearbeiten!

### Elements → Computed

Zeigt den finalen, berechneten Wert jeder Property:

- Der "wahre" Wert nach Kaskade & Vererbung
- Box Model Visualisierung
- Filter nach Property-Name
- Klick zeigt Ursprungsregel

### Debug-Workflow

1. **Element auswählen:** Rechtsklick → "Untersuchen"
2. **Styles prüfen:** Welche Regeln greifen?
3. **Durchgestrichenes:** Was wird überschrieben?
4. **Computed:** Was ist der finale Wert?
5. **Live bearbeiten:** Änderungen testen

### Übung 4: CSS in DevTools analysieren

**Aufgabe:**

1. Öffne deine HTML-Seite im Browser
2. Rechtsklick auf ein Element → "Untersuchen"
3. Beantworte:
   - Welche CSS-Regeln treffen auf dieses Element zu?
   - Gibt es durchgestrichene Styles?
   - Was sind die berechneten Werte für `padding` und `margin`?

<details>
<summary>Hinweise zur Lösung</summary>

**So gehst du vor:**

1. **Styles Tab:**
   - Zeigt alle Regeln sortiert nach Spezifität
   - Oberste Regeln haben höchste Spezifität
   - Durchgestrichenes wird von etwas Spezifischerem überschrieben

2. **Computed Tab:**
   - Box Model Visualisierung (blau=content, grün=padding, gelb=border, orange=margin)
   - Klick auf einen Wert zeigt die Ursprungsregel
   - Filter: Tippe z.B. "margin" um nur Margin-Werte zu sehen

3. **Live bearbeiten:**
   - Klick auf einen Wert und ändere ihn
   - Drücke ↑/↓ um Zahlen zu ändern
   - Checkbox deaktiviert/aktiviert eine Regel

**Wichtig:** Änderungen in DevTools sind temporär - beim Reload sind sie weg!

</details>

---

## Teil 9: Fehlerfall - CSS wirkt nicht

### Diagnose-Checkliste

| Schritt | Prüfung | Problem |
|---------|---------|---------|
| 1 | Network Tab: CSS lädt? | 404 = Pfad falsch |
| 2 | Response Headers: Content-Type? | Falscher MIME-Type |
| 3 | Styles: Regel sichtbar? | Selektor passt nicht |
| 4 | Styles: Durchgestrichen? | Spezifität/Reihenfolge |
| 5 | Hard Reload | Cache-Problem |

### Schnell-Check

**Seite komplett ungestylt?**
→ CSS wird nicht geladen (Network Tab prüfen)

**Nur ein Stil fehlt?**
→ Wahrscheinlich überschrieben (Styles Tab prüfen)

### Wissensfrage 4

Du hast eine CSS-Regel geschrieben, aber sie wird im Styles-Tab durchgestrichen angezeigt. Was ist passiert und wie löst du das Problem?

<details>
<summary>Antwort anzeigen</summary>

**Was passiert ist:**
Eine andere Regel mit höherer Spezifität (oder gleicher Spezifität aber später im Code) überschreibt deine Regel.

**Wie du es löst:**

1. **Schau dir an, welche Regel gewinnt:**
   - Im Styles Tab steht die gewinnende Regel darüber

2. **Erhöhe die Spezifität deiner Regel:**
   ```css
   /* Vorher: wird überschrieben */
   .card { color: blue; }

   /* Nachher: spezifischer */
   .container .card { color: blue; }
   ```

3. **Oder: Ändere die Reihenfolge:**
   - Deine Regel muss nach der überschreibenden kommen

4. **Notbremse (vermeiden!):**
   ```css
   .card { color: blue !important; }
   ```
   Nur als letzte Option - macht Debugging schwieriger!

**Best Practice:** Konsistente Spezifität im Projekt (z.B. immer eine Klasse, nie IDs für Styling)

</details>

---

## Teil 10: Farben und Typografie

### Farben in CSS

```css
/* Benannte Farben */
color: red;
color: darkblue;

/* Hex-Werte */
color: #FF0000;     /* Rot */
color: #333333;     /* Dunkelgrau */
color: #fff;        /* Weiß (Kurzform) */

/* RGB/RGBA */
color: rgb(255, 0, 0);       /* Rot */
color: rgba(0, 0, 0, 0.5);   /* Schwarz, 50% transparent */

/* HSL */
color: hsl(0, 100%, 50%);    /* Rot */
```

### Typografie

```css
/* Schriftart */
font-family: Arial, Helvetica, sans-serif;

/* Schriftgröße */
font-size: 16px;
font-size: 1rem;

/* Schriftstärke */
font-weight: normal;  /* 400 */
font-weight: bold;    /* 700 */
font-weight: 600;     /* Semibold */

/* Zeilenhöhe */
line-height: 1.6;

/* Textausrichtung */
text-align: left;
text-align: center;
text-align: right;

/* Textdekoration */
text-decoration: none;
text-decoration: underline;
```

---

## Zusammenfassung

### Was du gelernt hast:

| Thema | Key Takeaway |
|-------|--------------|
| CSS als Asset | Eigener Request, im Network Tab prüfen |
| Syntax | Selektor { eigenschaft: wert; } |
| Selektoren | Klassen für Styling, IDs für JS |
| Pseudo-Klassen | :hover, :focus für Interaktivität |
| Kaskade | Höhere Spezifität gewinnt |
| Box Model | Content → Padding → Border → Margin |
| DevTools | Styles (Regeln) vs Computed (Ergebnis) |

### Vorbereitung auf morgen

Morgen lernst du **CSS Layout & Responsive**:
- Flexbox für eindimensionale Layouts
- Grid für zweidimensionale Layouts
- Media Queries für Responsive Design
- DevTools Responsive Mode

---

## Bonus: Vollständiges Stylesheet

<details>
<summary>Komplettes Beispiel-Stylesheet anzeigen</summary>

```css
/* ==================
   CSS Grundlagen
   Vollständiges Beispiel
   ================== */

/* Box-Sizing Reset */
*, *::before, *::after {
  box-sizing: border-box;
}

/* Body - Grundeinstellungen */
body {
  font-family: 'Segoe UI', Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #333333;
  background-color: #f8f9fa;
  margin: 0;
  padding: 0;
}

/* Überschriften */
h1, h2, h3, h4, h5, h6 {
  margin-top: 0;
  margin-bottom: 0.5em;
  color: #1a1a2e;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }

/* Absätze */
p {
  margin-top: 0;
  margin-bottom: 1rem;
}

/* Links */
a {
  color: #0066cc;
  text-decoration: none;
  transition: color 0.2s ease;
}

a:hover {
  color: #004499;
  text-decoration: underline;
}

a:focus {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

/* Listen */
ul, ol {
  padding-left: 2rem;
  margin-bottom: 1rem;
}

li {
  margin-bottom: 0.5rem;
}

/* Header */
header {
  background-color: #1a1a2e;
  color: white;
  padding: 1rem 2rem;
}

header h1 {
  color: white;
  margin: 0;
}

/* Navigation */
nav ul {
  list-style: none;
  padding: 0;
  margin: 1rem 0 0 0;
}

nav li {
  display: inline-block;
  margin-right: 1rem;
}

nav a {
  color: white;
}

nav a:hover {
  color: #cccccc;
}

/* Main Content */
main {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

/* Sections */
section {
  margin-bottom: 2rem;
}

/* Cards */
.card {
  background-color: white;
  border: 1px solid #dddddd;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1rem;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* Buttons */
button, .btn {
  display: inline-block;
  background-color: #0066cc;
  color: white;
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s ease;
}

button:hover, .btn:hover {
  background-color: #004499;
}

button:focus, .btn:focus {
  outline: 2px solid #004499;
  outline-offset: 2px;
}

/* Formulare */
form {
  max-width: 500px;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

input, textarea, select {
  width: 100%;
  padding: 0.75rem;
  border: 2px solid #cccccc;
  border-radius: 4px;
  font-size: 1rem;
  margin-bottom: 1rem;
  transition: border-color 0.2s ease;
}

input:focus, textarea:focus, select:focus {
  border-color: #0066cc;
  outline: none;
}

/* Footer */
footer {
  background-color: #1a1a2e;
  color: white;
  padding: 1.5rem 2rem;
  text-align: center;
  margin-top: 2rem;
}

footer p {
  margin: 0;
}
```

Dieses Stylesheet baut auf den Übungen auf und wird morgen mit Layout-Techniken erweitert!

</details>
