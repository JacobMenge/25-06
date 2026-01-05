# Schnellreferenz: HTML & CSS

Diese Referenz enthält alle wichtigen Code-Snippets, die du für das Assignment brauchst.

---

## HTML Grundgerüst

Jede HTML-Datei beginnt so:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Seitentitel</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Inhalt hier -->
</body>
</html>
```

**Was bedeutet was?**
| Code | Bedeutung |
|------|-----------|
| `<!DOCTYPE html>` | Sagt dem Browser: "Das ist HTML5" |
| `lang="de"` | Sprache der Seite (für Screenreader) |
| `charset="UTF-8"` | Ermöglicht Umlaute (ä, ö, ü) |
| `viewport` | Korrekte Darstellung auf Handys |
| `<title>` | Text im Browser-Tab |
| `<link rel="stylesheet">` | Verbindet CSS-Datei |

---

## Semantische Struktur

```html
<body>
    <header>
        <h1>Seitenname</h1>
        <nav>
            <!-- Navigation hier -->
        </nav>
    </header>

    <main>
        <section id="bereich1">
            <h2>Überschrift</h2>
            <p>Inhalt...</p>
        </section>

        <section id="bereich2">
            <h2>Überschrift</h2>
            <p>Inhalt...</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Dein Name</p>
    </footer>
</body>
```

**Elemente erklärt:**
| Element | Verwendung |
|---------|------------|
| `<header>` | Kopfbereich mit Logo/Name und Navigation |
| `<nav>` | Navigation/Menü |
| `<main>` | Hauptinhalt (nur 1x pro Seite!) |
| `<section>` | Thematischer Abschnitt |
| `<footer>` | Fußbereich |
| `<h1>` bis `<h6>` | Überschriften (h1 = wichtigste) |
| `<p>` | Absatz/Paragraph |

---

## Navigation erstellen

```html
<nav>
    <a href="#about">Über mich</a>
    <a href="#skills">Skills</a>
    <a href="#contact">Kontakt</a>
</nav>
```

**Wie funktioniert das?**
- `href="#about"` verlinkt zu dem Element mit `id="about"`
- Das `#` bedeutet: "Springe zu dieser ID auf der gleichen Seite"

---

## Listen

**Ungeordnete Liste (Punkte):**
```html
<ul>
    <li>Erster Punkt</li>
    <li>Zweiter Punkt</li>
    <li>Dritter Punkt</li>
</ul>
```

**Geordnete Liste (Zahlen):**
```html
<ol>
    <li>Schritt 1</li>
    <li>Schritt 2</li>
    <li>Schritt 3</li>
</ol>
```

---

## Formular erstellen

```html
<form action="#" method="POST">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">E-Mail:</label>
    <input type="email" id="email" name="email" required>

    <label for="message">Nachricht:</label>
    <textarea id="message" name="message" required></textarea>

    <button type="submit">Absenden</button>
</form>
```

**Wichtige Attribute:**
| Attribut | Bedeutung |
|----------|-----------|
| `action="#"` | Wohin werden die Daten gesendet |
| `method="POST"` | Wie werden die Daten gesendet |
| `for="name"` | Verbindet Label mit Input (gleiche ID) |
| `id="name"` | Eindeutige Kennung (für Label) |
| `name="name"` | Schlüssel für die Daten (WICHTIG!) |
| `required` | Pflichtfeld |
| `type="email"` | Prüft auf gültige E-Mail |

**Verschiedene Input-Typen:**
```html
<input type="text">      <!-- Normaler Text -->
<input type="email">     <!-- E-Mail (wird geprüft) -->
<input type="password">  <!-- Passwort (versteckt) -->
<input type="number">    <!-- Zahlen -->
<textarea></textarea>    <!-- Mehrzeiliger Text -->
```

---

## CSS Grundgerüst

```css
/* Reset - Entfernt Browser-Standardabstände */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* Body - Grundeinstellungen */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f5f5f5;
}
```

**Was bedeutet was?**
| Code | Bedeutung |
|------|-----------|
| `*` | Wählt ALLE Elemente aus |
| `box-sizing: border-box` | Padding zählt zur Breite dazu |
| `margin: 0` | Entfernt Außenabstand |
| `padding: 0` | Entfernt Innenabstand |
| `font-family` | Schriftart |
| `line-height: 1.6` | Zeilenabstand (1.6 = 160%) |
| `color` | Textfarbe |
| `background-color` | Hintergrundfarbe |

---

## Farben in CSS

**Hex-Codes (am häufigsten):**
```css
color: #333333;      /* Dunkelgrau */
color: #000000;      /* Schwarz */
color: #ffffff;      /* Weiß */
color: #1a1a2e;      /* Dunkelblau */
color: #0066cc;      /* Blau */
```

**Benannte Farben:**
```css
color: white;
color: black;
color: red;
color: blue;
```

**Mit Transparenz (RGBA):**
```css
background-color: rgba(0, 0, 0, 0.5);  /* 50% transparentes Schwarz */
```

---

## Abstände (Padding & Margin)

```css
/* Alle Seiten gleich */
padding: 20px;
margin: 20px;

/* Oben/Unten und Links/Rechts */
padding: 20px 40px;  /* 20px oben/unten, 40px links/rechts */

/* Alle 4 Seiten einzeln (Uhrzeigersinn) */
padding: 10px 20px 30px 40px;  /* oben, rechts, unten, links */

/* Einzelne Seiten */
margin-top: 20px;
margin-bottom: 20px;
margin-left: 10px;
margin-right: 10px;
```

**Merkhilfe:** `margin: oben rechts unten links` = Uhrzeigersinn (TRouBLe = Top Right Bottom Left)

---

## Flexbox (für Navigation)

```css
nav {
    display: flex;
    justify-content: center;
    gap: 20px;
}
```

**Was bedeutet was?**
| Code | Bedeutung |
|------|-----------|
| `display: flex` | Macht Element zum Flex-Container |
| `justify-content: center` | Zentriert horizontal |
| `justify-content: space-between` | Verteilt mit Abstand (Logo links, Links rechts) |
| `align-items: center` | Zentriert vertikal |
| `gap: 20px` | Abstand zwischen Elementen |
| `flex-direction: column` | Untereinander statt nebeneinander |

**Beispiel: Logo links, Navigation rechts:**
```css
header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
```

---

## Links stylen

```css
a {
    color: #0066cc;
    text-decoration: none;  /* Entfernt Unterstreichung */
}

a:hover {
    color: #004499;
    text-decoration: underline;  /* Unterstreichung bei Hover */
}
```

---

## Buttons stylen

```css
button {
    padding: 12px 24px;
    background-color: #1a1a2e;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background-color: #333;
}
```

---

## Formular-Elemente stylen

```css
/* Labels */
label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}

/* Inputs und Textareas */
input, textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
    margin-bottom: 15px;
}

/* Bei Fokus */
input:focus, textarea:focus {
    border-color: #1a1a2e;
    outline: none;
}
```

---

## Responsive Design (Media Query)

```css
/* Standard (für Desktop) */
nav {
    display: flex;
    gap: 20px;
}

/* Für Bildschirme kleiner als 600px (Handy) */
@media (max-width: 600px) {
    nav {
        flex-direction: column;
        gap: 10px;
    }
}
```

**Erklärung:**
- Alles VOR `@media` gilt immer
- Alles IN `@media` gilt nur bei kleinen Bildschirmen
- `max-width: 600px` = "wenn Bildschirm maximal 600px breit ist"

---

## Häufige Fehler und Lösungen

### CSS wird nicht geladen
```html
<!-- Prüfe den Link im head -->
<link rel="stylesheet" href="style.css">
```
- Dateiname korrekt? `style.css` (nicht `Style.css` oder `styles.css`)
- Beide Dateien im gleichen Ordner?

### Umlaute werden falsch angezeigt
```html
<!-- Muss ganz oben im head stehen! -->
<meta charset="UTF-8">
```

### Formular sendet keine Daten
```html
<!-- Fehlt das name-Attribut? -->
<input type="text" name="username">  <!-- name ist wichtig! -->
```

### Flexbox funktioniert nicht
```css
/* display: flex muss auf dem CONTAINER sein! */
.container {
    display: flex;  /* Container */
}
.child {
    /* Die Kinder werden automatisch angeordnet */
}
```

### Hover funktioniert nicht
```css
/* Doppelpunkt vor hover, nicht vergessen! */
a:hover {  /* Richtig */
    color: red;
}
```

---

## Vollständiges Mini-Beispiel

### HTML (index.html)
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine Seite</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Willkommen!</h1>
        <nav>
            <a href="#about">Über mich</a>
            <a href="#contact">Kontakt</a>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>Über mich</h2>
            <p>Hallo, ich bin Max.</p>
        </section>

        <section id="contact">
            <h2>Kontakt</h2>
            <form action="#" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <button type="submit">Senden</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2024 Max</p>
    </footer>
</body>
</html>
```

### CSS (style.css)
```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

header {
    background: #1a1a2e;
    color: white;
    padding: 20px;
    text-align: center;
}

nav {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 10px;
}

nav a {
    color: white;
    text-decoration: none;
}

nav a:hover {
    color: #aaa;
}

section {
    padding: 40px 20px;
    max-width: 600px;
    margin: 0 auto;
}

input {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
}

button {
    padding: 10px 20px;
    background: #1a1a2e;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background: #333;
}

footer {
    background: #1a1a2e;
    color: white;
    text-align: center;
    padding: 20px;
}
```

---

Diese Referenz enthält alles, was du für das Assignment brauchst. Bei Fragen: Frag nach!
