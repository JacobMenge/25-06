# Pflicht-Assignment: Einfache Portfolio-Webseite (Einzelarbeit)

## Wochenabschluss: Webentwicklung Grundlagen I

### Organisatorische Rahmenbedingungen

Die Abgabe erfolgt bis Montag, 23:59 Uhr. Reiche folgende Dateien ein:


- `index.html` - Deine HTML-Datei
- `style.css` - Dein CSS-Stylesheet
- `README.md` - Kurze Dokumentation (ca. 5-10 Sätze oder Stichpunkte)

Der thematische Umfang dieser Aufgabe erstreckt sich über die Grundlagen der Woche:
- HTML Struktur & Semantik
- CSS Styling & Selektoren
- Einfaches Layout mit Flexbox oder Grid
- Grundlegendes Responsive Design

---

## Abgabe

Packe deine Dateien in einen Ordner und lade ihn hoch:

```
vorname_nachname_woche1/
    index.html
    style.css
    README.md
```

**Hinweis:** Falls kein Ordner-Upload möglich ist, komprimiere den Ordner als ZIP-Datei und lade die ZIP-Datei hoch.

---

## Hinweis zur Nutzung von KI-Tools

**Die Nutzung von KI-Tools (wie ChatGPT, Claude, Copilot) ist erlaubt!**

**Wichtige Bedingungen:**
- Du musst **jeden Code, den eine KI generiert hat, vollständig verstehen**
- Du solltest in der Lage sein, **jede Zeile deines Codes zu erklären**
- Bei Rückfragen musst du erklären können, was der Code macht und warum

**Warum?** KI-Tools sind hilfreiche Werkzeuge, aber das Ziel ist, dass DU die Grundlagen verstehst. Nutze KI als Lernhilfe, nicht als Ersatz für eigenes Verständnis.

**Tipp:** Wenn du KI nutzt, frage sie auch, dir den Code zu erklären!

---

## Zielsetzung der Aufgabe

Mit diesem Assignment zeigst du, dass du die wichtigsten Webentwicklungs-Grundlagen verstanden hast. Es geht darum, eine **einfache, funktionierende Webseite** zu erstellen.

**Wichtig:** Eine einfache, vollständige Seite ist besser als eine komplexe, fehlerhafte Seite!

Du hast die Wahl zwischen zwei Ansätzen.

---

## Weg A: Eigenes Thema (Kreativ)

Erstelle eine einfache Webseite zu einem Thema deiner Wahl.

### Mindestanforderungen:

**HTML:**
- Korrektes HTML5-Grundgerüst
- Mindestens 3 verschiedene Sections
- Eine Navigation
- Ein Kontaktformular mit mindestens 2 Feldern

**CSS:**
- Externes Stylesheet
- Grundlegende Styles (Farben, Schriften, Abstände)
- Entweder Flexbox ODER Grid an mindestens einer Stelle
- Mindestens ein :hover Effekt

### Themen-Ideen:

- **Über mich:** Vorstellung, Hobbys, Kontakt
- **Lieblingsrezept:** Zutaten, Anleitung, Bild
- **Mein Haustier:** Fotos, Infos, Steckbrief
- **Lieblingsserie/Spiel:** Beschreibung, Bewertung, Empfehlung

---

## Weg B: Vorgegebene Aufgabe (Geführt)

Falls du lieber Schritt für Schritt arbeiten möchtest, nutze diese Anleitung.

### Aufgabe: Einfache Portfolio-Seite

Du erstellst eine persönliche "Über mich"-Seite mit drei Bereichen.

**Hinweis:** Wenn du Weg B vollständig umsetzt, erfüllst du automatisch die Flexbox-Anforderung (durch `nav { display: flex; }` und das Formular-Styling).

### Schritt 1: HTML-Grundgerüst erstellen

Erstelle eine Datei `index.html` mit diesem Grundgerüst:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Über mich - Dein Name</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Hier kommt der Inhalt -->
</body>
</html>
```

**Erklärung:**
- `<!DOCTYPE html>` sagt dem Browser: Das ist HTML5
- `<html lang="de">` ist das Wurzelelement, "de" steht für Deutsch
- `<meta charset="UTF-8">` ermöglicht Umlaute (ä, ö, ü)
- `<meta name="viewport">` sorgt für korrekte Darstellung auf Handys
- `<link rel="stylesheet">` verbindet dein CSS

### Schritt 2: Header mit Navigation hinzufügen

Füge im `<body>` hinzu:

```html
<header>
    <h1>Dein Name</h1>
    <nav>
        <a href="#about">Über mich</a>
        <a href="#skills">Skills</a>
        <a href="#contact">Kontakt</a>
    </nav>
</header>
```

**Erklärung:**
- `<header>` ist der Kopfbereich der Seite
- `<nav>` enthält die Navigation
- `href="#about"` verlinkt zu einem Element mit `id="about"`

### Schritt 3: Hauptinhalt mit Sections hinzufügen

Füge nach dem `</header>` hinzu:

```html
<main>
    <section id="about">
        <h2>Über mich</h2>
        <p>Hallo! Ich bin [Dein Name] und lerne gerade Webentwicklung.</p>
        <p>Schreibe hier 2-3 Sätze über dich.</p>
    </section>

    <section id="skills">
        <h2>Meine Skills</h2>
        <ul>
            <li>HTML</li>
            <li>CSS</li>
            <li>Noch ein Skill</li>
        </ul>
    </section>

    <section id="contact">
        <h2>Kontakt</h2>
        <form action="#" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">E-Mail:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Nachricht:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Absenden</button>
        </form>
    </section>
</main>
```

**Erklärung:**
- `<main>` enthält den Hauptinhalt
- `<section>` teilt den Inhalt in Abschnitte
- `id="about"` ermöglicht das Verlinken von der Navigation
- `<ul>` ist eine Aufzählungsliste, `<li>` sind die Punkte
- `<form>` ist das Formular
- `<label for="name">` verbindet den Text mit dem Eingabefeld (`for` muss zur `id` des Eingabefelds passen)
- `name="..."` wird für die Formularübermittlung benötigt
- `required` macht das Feld zum Pflichtfeld

**Hinweis zum Formular:** Da wir kein Backend haben, wird beim Absenden nichts gespeichert oder gesendet. Es geht hier nur um die HTML-Struktur und das CSS-Styling des Formulars.

### Schritt 4: Footer hinzufügen

Füge nach `</main>` hinzu:

```html
<footer>
    <p>&copy; 2025 Dein Name</p>
</footer>
```

**Erklärung:**
- `<footer>` ist der Fußbereich
- `&copy;` erzeugt das Copyright-Symbol ©

### Schritt 5: CSS-Datei erstellen

Erstelle eine Datei `style.css`:

```css
/* === GRUNDEINSTELLUNGEN === */

/* Box-Sizing für einfachere Größenberechnung */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

/* Body - Grundeinstellungen für die ganze Seite */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f5f5f5;
}
```

**Erklärung:**
- `*` wählt ALLE Elemente aus
- `box-sizing: border-box` macht Größenberechnungen einfacher
- `font-family` legt die Schriftart fest
- `line-height: 1.6` macht Text besser lesbar
- `#333` ist ein dunkles Grau (Hex-Farbcode)

### Schritt 6: Header stylen

Füge in deine CSS-Datei hinzu:

```css
/* === HEADER === */

header {
    background-color: #1a1a2e;
    color: white;
    padding: 20px;
    text-align: center;
}

header h1 {
    margin-bottom: 10px;
}

/* Navigation */
nav {
    display: flex;
    justify-content: center;
    gap: 20px;
}

nav a {
    color: white;
    text-decoration: none;
}

nav a:hover {
    color: #aaaaaa;
}
```

**Erklärung:**
- `display: flex` macht nav zu einem Flex-Container
- `justify-content: center` zentriert die Links
- `gap: 20px` fügt Abstand zwischen den Links ein
- `text-decoration: none` entfernt die Unterstreichung
- `:hover` wird aktiv, wenn die Maus über dem Element ist

### Schritt 7: Sections stylen

```css
/* === SECTIONS === */

section {
    padding: 40px 20px;
    max-width: 800px;
    margin: 0 auto;
}

section h2 {
    margin-bottom: 20px;
    color: #1a1a2e;
}

/* Hintergrund für jede zweite Section */
#skills {
    background-color: #e8e8e8;
}
```

**Erklärung:**
- `padding: 40px 20px` bedeutet: 40px oben/unten, 20px links/rechts
- `max-width: 800px` begrenzt die Breite
- `margin: 0 auto` zentriert den Inhalt horizontal

### Schritt 8: Formular stylen

```css
/* === FORMULAR === */

form {
    display: flex;
    flex-direction: column;
    gap: 15px;
    max-width: 400px;
}

label {
    font-weight: bold;
}

input, textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 16px;
}

input:focus, textarea:focus {
    border-color: #1a1a2e;
    outline: none;
}

textarea {
    height: 100px;
}

button {
    padding: 12px;
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

**Erklärung:**
- `flex-direction: column` stapelt die Elemente untereinander
- `gap: 15px` fügt Abstand zwischen den Formularfeldern ein
- `border-radius: 4px` macht abgerundete Ecken
- `:focus` wird aktiv, wenn das Feld ausgewählt ist
- `cursor: pointer` zeigt eine Hand beim Hover über den Button

### Schritt 9: Footer stylen

```css
/* === FOOTER === */

footer {
    background-color: #1a1a2e;
    color: white;
    text-align: center;
    padding: 20px;
    margin-top: 40px;
}
```

### Schritt 10: Responsive machen (Bonus)

Füge am Ende deiner CSS-Datei hinzu:

```css
/* === RESPONSIVE === */

/* Für Bildschirme kleiner als 600px */
@media (max-width: 600px) {
    nav {
        flex-direction: column;
        gap: 10px;
    }

    section {
        padding: 20px 15px;
    }
}
```

**Erklärung:**
- `@media (max-width: 600px)` aktiviert die Regeln nur bei kleinen Bildschirmen
- Die Navigation wird vertikal statt horizontal
- Die Abstände werden kleiner

**Hinweis:** Dieser Schritt ist optional und gibt Bonuspunkte.

---

## Bewertungsraster (Vereinfacht)

Die Bewertung erfolgt mit insgesamt 100 möglichen Punkten:

### HTML (40 Punkte)

| Kriterium | Punkte |
|-----------|--------|
| Korrektes Grundgerüst (DOCTYPE, head, body) | 10 |
| Semantische Elemente (header, main, section, footer) | 15 |
| Formular mit label, input, button | 15 |

### CSS (40 Punkte)

| Kriterium | Punkte |
|-----------|--------|
| Externes Stylesheet eingebunden | 5 |
| Grundstyling (Farben, Schriften, Abstände) | 15 |
| Flexbox ODER Grid verwendet | 10 |
| Hover-Effekt vorhanden | 10 |

### Qualität (20 Punkte)

| Kriterium | Punkte |
|-----------|--------|
| Seite funktioniert (keine offensichtlichen Fehler) | 10 |
| Code ist lesbar (Einrückung) | 5 |
| README vorhanden | 5 |

### Bonus (bis zu 10 Extra-Punkte)

- Responsive Design mit @media
- Mehrere Hover-Effekte
- Kreative Gestaltung
- Zusätzliche Sections

**Zum Bestehen sind 50 Punkte erforderlich.**

---

## Checkliste vor der Abgabe

### HTML
- [ ] DOCTYPE vorhanden
- [ ] `<meta charset="UTF-8">` im head
- [ ] `<meta name="viewport">` im head
- [ ] Titel gesetzt
- [ ] CSS-Datei verlinkt
- [ ] header, main, footer vorhanden
- [ ] Mindestens 3 sections
- [ ] Formular mit mindestens 2 Feldern

### CSS
- [ ] Datei heißt `style.css`
- [ ] Body hat Grundeinstellungen
- [ ] Farben sind gesetzt
- [ ] Mindestens ein Flexbox oder Grid
- [ ] Mindestens ein :hover Effekt

### Test
- [ ] Seite im Browser öffnen
- [ ] Alle Links funktionieren (springen zu den Sections)
- [ ] Formular sieht gut aus
- [ ] Keine großen Fehler sichtbar

---

## README.md Vorlage

Erstelle eine Datei `README.md` mit folgendem Inhalt (Stichpunkte reichen aus):

```markdown
# Mein Portfolio - [Dein Name]

## Beschreibung
Dies ist meine erste Webseite. Sie enthält Informationen über mich,
meine Skills und ein Kontaktformular.

## Verwendete Techniken
- HTML5 (Semantische Elemente)
- CSS (Flexbox, Hover-Effekte)

## Weg
Ich habe Weg [A/B] gewählt.

## Notizen
[Optional: Was war schwierig? Was hat gut funktioniert?]
```

---

## Hilfreiche Tipps

### Problem: CSS wird nicht geladen
1. Prüfe den Dateinamen (style.css)
2. Prüfe den Pfad im `<link>` Tag
3. Sind beide Dateien im gleichen Ordner?

### Problem: Farben funktionieren nicht
- Hex-Codes brauchen ein `#` davor: `#1a1a2e`
- Schreibfehler prüfen: `backgroud` vs `background`

### Problem: Flexbox funktioniert nicht
- `display: flex` muss auf dem CONTAINER sein
- Die KINDER werden dann angeordnet

### Problem: Formular sieht komisch aus
- Prüfe, ob alle `<label>` Tags korrekt geschlossen sind (`</label>`)
- Prüfe, ob `for` im Label zur `id` im Input passt
- Hinweis: `<input>` ist ein selbstschließendes Element und braucht kein `</input>`

### Problem: Navigation springt nicht zu den Sections
- Prüfe, ob die `id` in der Section mit dem `href` im Link übereinstimmt
- Beispiel: `href="#about"` springt zu `id="about"`

---



## Viel Erfolg!

Diese Aufgabe soll zeigen, dass du die Grundlagen verstanden hast. Es muss nicht perfekt sein! Konzentriere dich darauf, dass die Seite funktioniert und der Code verständlich ist.

Bei Fragen: Frag nach! Das ist keine Schwäche, sondern zeigt, dass du verstehen willst.