# HTML: Struktur, Semantik & Formulare - Praktische Übungen

## Übersicht

In dieser Übung vertiefst du dein Wissen über:
- **HTML Grundstruktur** - doctype, head, body
- **Semantische Elemente** - header, nav, main, section, footer
- **Links und Pfade** - Relativ, absolut und externe URLs
- **Request-Kaskade** - Wie HTML weitere Requests auslöst
- **Formulare** - Aufbau, Methoden und Debugging

Diese Übung baut auf Tag 1 auf und bereitet dich auf das Freitags-Projekt vor.

---

## Teil 1: HTML Grundstruktur

### Das HTML-Grundgerüst

Jedes HTML-Dokument folgt dieser Struktur:

```html
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine Seite</title>
    <link rel="stylesheet" href="styles.css">
  </head>
  <body>
    <!-- Sichtbarer Inhalt hier -->
  </body>
</html>
```

### Bestandteile erklärt

| Element | Bedeutung |
|---------|-----------|
| `<!DOCTYPE html>` | Aktiviert den Standards-Modus im Browser |
| `<html lang="de">` | Root-Element mit Sprachattribut |
| `<head>` | Meta-Informationen (nicht sichtbar für User) |
| `<meta charset="UTF-8">` | Zeichenkodierung (immer UTF-8!) |
| `<meta name="viewport">` | Mobile-Optimierung |
| `<title>` | Titel im Browser-Tab |
| `<link>` | Lädt externes CSS (= eigener HTTP-Request!) |
| `<body>` | Sichtbarer Seiteninhalt |

### Wissensfrage 1

Warum ist das `<meta charset="UTF-8">` so wichtig und sollte immer als erstes im `<head>` stehen?

<details>
<summary>Antwort anzeigen</summary>

Das `charset="UTF-8"` definiert die **Zeichenkodierung** des Dokuments.

**Warum wichtig:**
- Ohne korrekte Kodierung werden Sonderzeichen (ä, ö, ü, €, etc.) falsch dargestellt
- Der Browser muss die Kodierung kennen, BEVOR er Text parst
- Deshalb muss es ganz am Anfang des `<head>` stehen

**UTF-8** ist der Standard, weil es:
- Alle Zeichen aller Sprachen unterstützt
- Mit ASCII abwärtskompatibel ist
- Im Web der de-facto Standard ist

</details>

---

## Teil 2: Übung - Deine erste HTML-Seite

### Aufgabe

Erstelle eine HTML-Seite mit folgenden Anforderungen:

1. Korrektes HTML5-Grundgerüst
2. Deutscher Sprachcode
3. Sinnvoller Titel
4. Eine Hauptüberschrift `<h1>` mit deinem Namen
5. Einen Absatz `<p>` über dich
6. Eine ungeordnete Liste `<ul>` mit 3 Hobbys

**Schritte:**
1. Erstelle eine neue Datei: `index.html`
2. Schreibe das HTML-Grundgerüst
3. Füge die geforderten Elemente hinzu
4. Öffne die Datei im Browser

<details>
<summary>Musterlösung anzeigen</summary>

```html
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Über mich</title>
  </head>
  <body>
    <h1>Hallo, ich bin Max Mustermann!</h1>

    <p>
      Ich bin Teilnehmer des Webentwicklung-Kurses und lerne
      gerade HTML und CSS. Ich freue mich darauf, meine erste
      eigene Website zu erstellen.
    </p>

    <h2>Meine Hobbys</h2>
    <ul>
      <li>Programmieren</li>
      <li>Musik hören</li>
      <li>Wandern</li>
    </ul>
  </body>
</html>
```

**Wichtige Punkte:**
- `<!DOCTYPE html>` aktiviert den Standardmodus
- `lang="de"` hilft Screenreadern bei der Aussprache
- `<meta charset="UTF-8">` steht ganz am Anfang des `<head>`
- `<meta name="viewport">` sorgt für korrekte Darstellung auf Mobilgeräten

</details>

---

## Teil 3: Semantische HTML-Elemente

### Warum Semantik wichtig ist

Semantische Tags geben dem Inhalt **Bedeutung**, nicht nur Aussehen:

| Element | Bedeutung | Verwendung |
|---------|-----------|------------|
| `<header>` | Kopfbereich | Logo, Navigation, Seitentitel |
| `<nav>` | Navigation | Hauptmenü, Breadcrumbs |
| `<main>` | Hauptinhalt | Zentraler Content (nur 1x pro Seite!) |
| `<section>` | Thematischer Abschnitt | Kapitel, Feature-Bereiche |
| `<article>` | Eigenständiger Inhalt | Blog-Posts, News, Kommentare |
| `<aside>` | Ergänzender Inhalt | Sidebar, verwandte Links |
| `<footer>` | Fußbereich | Copyright, Kontakt, Social Links |

### Vergleich: Ohne vs. Mit Semantik

```html
<!-- NICHT SO (nur divs) -->
<div class="header">
  <div class="nav">...</div>
</div>
<div class="content">
  <div class="sidebar">...</div>
  <div class="main">...</div>
</div>
<div class="footer">...</div>

<!-- BESSER (semantisch) -->
<header>
  <nav>...</nav>
</header>
<main>
  <aside>...</aside>
  <section>...</section>
</main>
<footer>...</footer>
```

### Wissensfrage 2

Warum sollte `<main>` nur einmal pro Seite verwendet werden?

<details>
<summary>Antwort anzeigen</summary>

`<main>` markiert den **Hauptinhalt** der Seite - den Content, der einzigartig für diese Seite ist (nicht Header, Footer, Navigation, die auf jeder Seite gleich sind).

**Gründe für nur 1x:**
- Es gibt nur einen Hauptinhalt pro Seite
- Screenreader können direkt zum Hauptinhalt springen
- Suchmaschinen verstehen, was der wichtigste Content ist
- Es ist semantisch korrekt - eine Seite hat einen Hauptzweck

**Was NICHT in `<main>` gehört:**
- Navigation (`<nav>`)
- Footer (`<footer>`)
- Sidebar (`<aside>` - kann innerhalb oder außerhalb sein)
- Wiederholte Elemente, die auf jeder Seite gleich sind

</details>

---

## Teil 4: Übung - Semantische Struktur

### Aufgabe

Erweitere deine HTML-Seite mit semantischer Struktur:

1. Füge einen `<header>` mit einer `<nav>` hinzu
2. Umschließe deinen Hauptinhalt mit `<main>`
3. Erstelle einen `<footer>` mit Copyright-Info
4. Organisiere deinen Content in sinnvolle `<section>` Elemente

**Hinweise:**
- Die Navigation kann erstmal nur Platzhalter-Links haben (`<a href="#">Link</a>`)
- Denke an die Überschriften-Hierarchie: `<h1>` → `<h2>` → `<h3>` (keine Stufen überspringen!)

<details>
<summary>Musterlösung anzeigen</summary>

```html
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Über mich - Max Mustermann</title>
  </head>
  <body>
    <header>
      <h1>Max Mustermann</h1>
      <nav>
        <ul>
          <li><a href="#ueber-mich">Über mich</a></li>
          <li><a href="#hobbys">Hobbys</a></li>
          <li><a href="#kontakt">Kontakt</a></li>
        </ul>
      </nav>
    </header>

    <main>
      <section id="ueber-mich">
        <h2>Über mich</h2>
        <p>
          Ich bin Teilnehmer des Webentwicklung-Kurses und lerne
          gerade HTML und CSS. Ich freue mich darauf, meine erste
          eigene Website zu erstellen.
        </p>
      </section>

      <section id="hobbys">
        <h2>Meine Hobbys</h2>
        <ul>
          <li>Programmieren</li>
          <li>Musik hören</li>
          <li>Wandern</li>
        </ul>
      </section>

      <section id="kontakt">
        <h2>Kontakt</h2>
        <p>Du erreichst mich unter: max@example.com</p>
      </section>
    </main>

    <footer>
      <p>&copy; 2024 Max Mustermann. Alle Rechte vorbehalten.</p>
    </footer>
  </body>
</html>
```

**Beachte:**
- `id`-Attribute ermöglichen Navigation zu Abschnitten (`href="#hobbys"`)
- Jede `<section>` hat eine eigene Überschrift
- Die Überschriften-Hierarchie ist korrekt: h1 → h2
- Footer enthält typischerweise Copyright-Info

</details>

---

## Teil 5: Links und Pfade

### Pfadtypen verstehen

| Typ | Beispiel | Erklärung |
|-----|----------|-----------|
| Relativ | `href="styles.css"` | Im gleichen Ordner |
| Relativ (Unterordner) | `href="css/main.css"` | In Unterordner `css/` |
| Relativ (höher) | `href="../images/logo.png"` | Eine Ebene höher, dann in `images/` |
| Absolut (Root) | `href="/styles/main.css"` | Vom Webroot aus |
| Externe URL | `href="https://example.com"` | Volle URL mit Protokoll |

### Wissensfrage 3

Du hast folgende Ordnerstruktur:
```
projekt/
├── index.html
├── css/
│   └── styles.css
└── images/
    └── logo.png
```

Wie verlinkst du von `index.html` aus auf `styles.css` und `logo.png`?

<details>
<summary>Antwort anzeigen</summary>

**Für CSS (im `<head>`):**
```html
<link rel="stylesheet" href="css/styles.css">
```
Oder absolut: `href="/css/styles.css"`

**Für das Bild (im `<body>`):**
```html
<img src="images/logo.png" alt="Logo">
```
Oder absolut: `src="/images/logo.png"`

**Häufiger Deploy-Fehler:**
Lokal funktioniert alles, aber nach dem Deploy brechen die Pfade, weil die Anwendung unter einem Unterpfad läuft (z.B. `/app/`).

**Lösung:** Root-Pfade (`/css/...`) sind oft sicherer als relative Pfade.

</details>

---

## Teil 6: Die Request-Kaskade

### HTML löst weitere Requests aus

Wenn der Browser HTML parst, lädt er automatisch alle referenzierten Ressourcen:

```html
<head>
  <link rel="stylesheet" href="/css/main.css">    <!-- Request 1 -->
  <link rel="stylesheet" href="/css/fonts.css">   <!-- Request 2 -->
</head>
<body>
  <img src="/images/logo.png" alt="Logo">          <!-- Request 3 -->
  <img src="/images/hero.jpg" alt="Hero">          <!-- Request 4 -->
  <script src="/js/app.js"></script>               <!-- Request 5 -->
</body>
```

### Im Network Tab sichtbar

| Name | Status | Type | Size |
|------|--------|------|------|
| index.html | 200 | document | 5 KB |
| main.css | 200 | stylesheet | 12 KB |
| fonts.css | 200 | stylesheet | 3 KB |
| logo.png | 200 | image | 8 KB |
| hero.jpg | **404** | image | - |
| app.js | 200 | script | 45 KB |

**Problem:** `hero.jpg` = 404 → Pfad falsch oder Datei fehlt!

### Übung 3: Request-Kaskade beobachten

**Aufgabe:**

1. Füge deiner HTML-Seite ein CSS-Stylesheet hinzu (erstelle `style.css`)
2. Füge ein Bild ein (finde ein beliebiges Bild oder nutze einen Platzhalter)
3. Öffne die DevTools (F12) → Network Tab
4. Lade die Seite neu
5. Beobachte:
   - Wie viele Requests werden ausgelöst?
   - Welche Typen siehst du?
   - Gibt es 404-Fehler?

<details>
<summary>Hinweise zur Lösung</summary>

**style.css erstellen:**
```css
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 20px;
}

h1 {
  color: #333;
}
```

**In index.html einbinden:**
```html
<head>
  ...
  <link rel="stylesheet" href="style.css">
</head>
```

**Bild einfügen (Platzhalter):**
```html
<img src="https://via.placeholder.com/300x200" alt="Platzhalterbild">
```

**Im Network Tab siehst du:**
1. `index.html` (document)
2. `style.css` (stylesheet)
3. `300x200` (image) - der Platzhalter

**Debug-Tipps:**
- "Preserve log" aktivieren
- Nach "Type" filtern (Doc, CSS, Img, JS)
- Klick auf "Initiator" zeigt, welches HTML-Element den Request auslöste

</details>

---

## Teil 7: Formulare - Aus Input wird HTTP-Request

### Formular-Grundlagen

Formulare senden Benutzereingaben an den Server. Jeder Submit = ein neuer HTTP-Request!

```html
<form action="/api/submit" method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required>

  <label for="email">E-Mail:</label>
  <input type="email" id="email" name="email" required>

  <label for="message">Nachricht:</label>
  <textarea id="message" name="message"></textarea>

  <button type="submit">Absenden</button>
</form>
```

### Die 3 wichtigsten Attribute

| Attribut | Bedeutung | Beispiel |
|----------|-----------|----------|
| `action` | Wohin? Die Ziel-URL | `action="/api/submit"` |
| `method` | Wie? GET oder POST | `method="POST"` |
| `name` | Was? Der Schlüssel für jeden Wert | `name="email"` |

### Wissensfrage 4

Was passiert, wenn du das `name`-Attribut bei einem Input-Feld vergisst?

<details>
<summary>Antwort anzeigen</summary>

**Das Feld wird NICHT übertragen!**

Ohne `name="..."` weiß der Browser nicht, unter welchem Schlüssel er den Wert senden soll. Der Server empfängt die Daten dann nicht.

**Beispiel:**
```html
<!-- FALSCH - wird nicht übertragen -->
<input type="text" id="username" placeholder="Username">

<!-- RICHTIG - wird übertragen -->
<input type="text" id="username" name="username" placeholder="Username">
```

**Im Network Tab:**
Bei "Form Data" oder "Payload" fehlt das Feld ohne `name`-Attribut komplett.

Dies ist einer der **häufigsten Formular-Fehler**!

</details>

---

## Teil 8: GET vs. POST

### Unterschiede

| Aspekt | GET | POST |
|--------|-----|------|
| Daten übertragen | In der URL (Query String) | Im Request Body |
| Sichtbarkeit | In Adressleiste sichtbar | Nicht in URL sichtbar |
| Bookmarkbar | Ja | Nein |
| Längenbeschränkung | ~2000 Zeichen | Keine |
| Caching | Wird gecacht | Wird nicht gecacht |
| Verwendung | Suchformulare, Filter | Datenänderungen, Login |

### Wann was verwenden?

**GET verwenden für:**
- Suchformulare
- Filter/Sortierung
- Alles, was man bookmarken möchte

**POST verwenden für:**
- Login-Formulare
- Registrierung
- Datenänderungen (Erstellen, Bearbeiten, Löschen)
- Sensible Daten (mit HTTPS!)

### Im Network Tab prüfen

- **GET:** Schaut auf "Query String Parameters" (in der URL)
- **POST:** Schaut auf "Form Data" oder "Payload" Tab (im Request Body)

---

## Teil 9: Übung - Kontaktformular erstellen

### Aufgabe

Erstelle ein Kontaktformular mit folgenden Feldern:

1. Name (Textfeld, Pflichtfeld)
2. E-Mail (E-Mail-Feld, Pflichtfeld)
3. Betreff (Textfeld)
4. Nachricht (Textarea, Pflichtfeld)
5. Newsletter-Abo (Checkbox)
6. Absenden-Button

**Anforderungen:**
- Verwende `method="POST"`
- Setze `action="#"` (wir haben keinen Server)
- Alle Felder brauchen `name`, `id` und zugehöriges `<label>`
- Pflichtfelder mit `required` markieren

<details>
<summary>Musterlösung anzeigen</summary>

```html
<section id="kontakt">
  <h2>Kontaktformular</h2>

  <form action="#" method="POST">
    <div>
      <label for="name">Name: *</label>
      <input
        type="text"
        id="name"
        name="name"
        placeholder="Dein Name"
        required
      >
    </div>

    <div>
      <label for="email">E-Mail: *</label>
      <input
        type="email"
        id="email"
        name="email"
        placeholder="deine@email.de"
        required
      >
    </div>

    <div>
      <label for="betreff">Betreff:</label>
      <input
        type="text"
        id="betreff"
        name="betreff"
        placeholder="Worum geht es?"
      >
    </div>

    <div>
      <label for="nachricht">Nachricht: *</label>
      <textarea
        id="nachricht"
        name="nachricht"
        rows="5"
        placeholder="Deine Nachricht..."
        required
      ></textarea>
    </div>

    <div>
      <input
        type="checkbox"
        id="newsletter"
        name="newsletter"
        value="ja"
      >
      <label for="newsletter">Newsletter abonnieren</label>
    </div>

    <button type="submit">Nachricht senden</button>
  </form>
</section>
```

**Wichtige Punkte:**
- `type="email"` validiert automatisch E-Mail-Format
- `required` macht das Feld zum Pflichtfeld
- `placeholder` gibt einen Hinweis im leeren Feld
- `rows="5"` bei Textarea definiert die Höhe
- Bei Checkbox: `value` bestimmt, was gesendet wird

</details>

---

## Teil 10: Formular-Debugging

### Debug-Checkliste

Wenn ein Formular nicht funktioniert:

1. **Request finden:** Nach Submit im Network Tab den neuen Request suchen
2. **Methode prüfen:** GET oder POST? Stimmt mit `method` überein?
3. **URL/Action prüfen:** Geht der Request an die richtige URL?
4. **Payload prüfen:** Unter "Form Data" - sind alle Felder da?
5. **Response lesen:** Was antwortet der Server?

### Typische Fehler

| Fehler | Ursache | Lösung |
|--------|---------|--------|
| Feld fehlt in Payload | `name`-Attribut fehlt | `name="fieldname"` hinzufügen |
| 404 bei Submit | Falsche `action`-URL | URL korrigieren |
| 405 Method Not Allowed | Falsche `method` | GET ↔ POST prüfen |
| Button tut nichts | `type="submit"` fehlt | `type="submit"` hinzufügen |

### Übung 4: Formular im Network Tab analysieren

**Aufgabe:**

1. Öffne dein Kontaktformular im Browser
2. Öffne DevTools → Network Tab
3. Fülle das Formular aus und klicke "Absenden"
4. Finde den Form-Request und beantworte:
   - Welche Methode wird verwendet?
   - Welche Daten werden übertragen?
   - Welchen Status Code erhältst du?

<details>
<summary>Hinweise zur Lösung</summary>

**So findest du den Request:**
1. Network Tab öffnen
2. "Preserve log" aktivieren
3. Formular absenden
4. Nach dem neuesten Request suchen (wird rot markiert, wenn Fehler)

**Was du siehst:**
- **Methode:** POST (steht in der Request-Zeile)
- **Form Data:** Alle Felder mit ihren Werten
  ```
  name: Max Mustermann
  email: max@example.de
  betreff: Anfrage
  nachricht: Hallo, ich habe eine Frage...
  newsletter: ja
  ```
- **Status:** Wahrscheinlich ein Fehler (wir haben keinen Server)

**Hinweis:** Da wir `action="#"` verwenden, wird die aktuelle Seite neu geladen. Bei einem echten Server würde die Anfrage verarbeitet.

</details>

---

## Teil 11: Formular-Elemente im Überblick

### Input-Typen

| Typ | Verwendung | Beispiel |
|-----|------------|----------|
| `text` | Einzeiliger Text | Name, Adresse |
| `email` | E-Mail mit Validierung | E-Mail-Adresse |
| `password` | Passwort (versteckt) | Login |
| `number` | Zahlen mit Spinner | Alter, Menge |
| `tel` | Telefonnummer | Telefon |
| `url` | URL mit Validierung | Website |
| `date` | Datumsauswahl | Geburtsdatum |
| `checkbox` | Ja/Nein Option | Newsletter, AGB |
| `radio` | Eine aus mehreren | Geschlecht, Zahlungsart |

### Weitere Formular-Elemente

```html
<!-- Mehrzeiliger Text -->
<textarea name="message" rows="5"></textarea>

<!-- Dropdown-Auswahl -->
<select name="country">
  <option value="">Bitte wählen</option>
  <option value="de">Deutschland</option>
  <option value="at">Österreich</option>
  <option value="ch">Schweiz</option>
</select>

<!-- Button -->
<button type="submit">Absenden</button>
```

### Wichtige Attribute

| Attribut | Bedeutung | Beispiel |
|----------|-----------|----------|
| `required` | Pflichtfeld | `<input required>` |
| `placeholder` | Hinweistext | `placeholder="Dein Name"` |
| `disabled` | Deaktiviert | `<input disabled>` |
| `readonly` | Nur lesbar | `<input readonly>` |
| `pattern` | Regex-Validierung | `pattern="[0-9]{5}"` |
| `min`/`max` | Wertebereich | `min="0" max="100"` |

---

## Zusammenfassung

### Was du gelernt hast:

| Thema | Key Takeaway |
|-------|--------------|
| HTML-Grundstruktur | doctype, head (Meta), body (Content) |
| Semantische Elemente | header, nav, main, section, footer für Bedeutung |
| Pfade | Relativ vs. absolut - Deploy-Fallen vermeiden |
| Request-Kaskade | HTML löst weitere Requests aus (CSS, Bilder, JS) |
| Formulare | action, method, name - die 3 essentiellen Attribute |
| Form-Debugging | Network Tab → Form Data prüfen |

### Vorbereitung auf morgen

Morgen lernst du **CSS Grundlagen**:
- CSS als eigener Request
- Selektoren und Klassen
- Kaskade und Spezifität
- Das Box Model
- Debugging in DevTools

Deine HTML-Struktur von heute wird morgen gestylt!

---

## Bonus: Komplette Seitenstruktur

Hier ist eine vollständige HTML-Seite mit allem, was du heute gelernt hast:

<details>
<summary>Vollständige Beispielseite anzeigen</summary>

```html
<!DOCTYPE html>
<html lang="de">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine Portfolio-Seite</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <header>
      <h1>Max Mustermann</h1>
      <nav>
        <ul>
          <li><a href="#about">Über mich</a></li>
          <li><a href="#skills">Skills</a></li>
          <li><a href="#contact">Kontakt</a></li>
        </ul>
      </nav>
    </header>

    <main>
      <section id="about">
        <h2>Über mich</h2>
        <p>
          Willkommen auf meiner Portfolio-Seite! Ich bin ein angehender
          Webentwickler und lerne gerade HTML, CSS und JavaScript.
        </p>
      </section>

      <section id="skills">
        <h2>Meine Skills</h2>
        <ul>
          <li>HTML5</li>
          <li>CSS3</li>
          <li>JavaScript (in Arbeit)</li>
        </ul>
      </section>

      <section id="contact">
        <h2>Kontakt</h2>
        <form action="#" method="POST">
          <div>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
          </div>
          <div>
            <label for="email">E-Mail:</label>
            <input type="email" id="email" name="email" required>
          </div>
          <div>
            <label for="message">Nachricht:</label>
            <textarea id="message" name="message" required></textarea>
          </div>
          <button type="submit">Absenden</button>
        </form>
      </section>
    </main>

    <footer>
      <p>&copy; 2024 Max Mustermann</p>
    </footer>
  </body>
</html>
```

Diese Struktur wirst du morgen mit CSS stylen und am Freitag zu einem vollständigen Projekt ausbauen!

</details>
