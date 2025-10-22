# Statische Website mit AWS S3 hosten - Die Basics

Eine Schritt-für-Schritt-Anleitung für Anfänger

---

## Was ist AWS S3?

**Amazon S3 (Simple Storage Service)** ist ein Cloud-Speicher von AWS. Stell dir S3 vor wie eine riesige Festplatte in der Cloud, auf der du Dateien ablegen kannst. Diese Dateien werden in sogenannten **Buckets** (Containern) organisiert.

### Warum S3 für Websites?

- Extrem skalierbar (funktioniert bei 10 oder 10 Millionen Besuchern)
- Sehr günstig (oft unter 1€ pro Monat)
- Kein Server nötig
- Hohe Verfügbarkeit

### Was kannst du hosten?

S3 eignet sich für **statische Websites**, also Seiten aus:
- HTML
- CSS
- JavaScript
- Bilder, Videos, PDFs

**Nicht möglich:** Serverseitige Sprachen wie PHP, Python oder Datenbanken.

---

## Schritt 1: Deine Website-Dateien vorbereiten

Erstelle auf deinem Windows 11 PC einen Ordner, z.B. `C:\meine-website\` und lege dort folgende Dateien an:

### index.html
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine S3 Website</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <h1>Willkommen auf meiner S3-Website!</h1>
    </header>
    <main>
        <p>Diese Seite wird direkt aus einem Amazon S3 Bucket ausgeliefert.</p>
    </main>
    <footer>
        <p>&copy; 2025 - Gehostet auf AWS S3</p>
    </footer>
</body>
</html>
```

### error.html
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Fehler 404</title>
</head>
<body>
    <h1>Seite nicht gefunden</h1>
    <p>Die angeforderte Seite existiert leider nicht.</p>
    <a href="index.html">Zurück zur Startseite</a>
</body>
</html>
```

### style.css
```css
body {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f0f0f0;
}

header {
    background-color: #232f3e;
    color: white;
    padding: 20px;
    border-radius: 5px;
}

main {
    background-color: white;
    padding: 20px;
    margin-top: 20px;
    border-radius: 5px;
}
```

---

## Schritt 2: Bei AWS anmelden

1. Öffne https://sandboxes.techstarter.de/
2. Melde dich mit deinen AWS Sandbox-Zugangsdaten an
3. Stelle sicher, dass du in der richtigen Region bist (oben rechts, z.B. "EU-Central-1 - Frankfurt")

---

## Schritt 3: S3 Bucket erstellen

### 3.1 S3 Service öffnen
- Gib oben in der Suchleiste "S3" ein
- Klicke auf "S3" unter Services

### 3.2 Neuen Bucket erstellen
- Klicke auf den Button **"Bucket erstellen"** (oder "Create bucket")

### 3.3 Bucket konfigurieren

**Bucket-Name:**
- Wähle einen eindeutigen Namen, z.B. `meine-website-2025-test`
- **Wichtig:** Der Name muss weltweit einzigartig sein
- Nur Kleinbuchstaben, Zahlen und Bindestriche erlaubt

**Region:**
- Wähle die Region, die dir geografisch am nächsten ist
- Für Deutschland: "EU (Frankfurt) eu-central-1"

**Block Public Access:**
- **SEHR WICHTIG:** Entferne das Häkchen bei **"Block all public access"**
- Setze das Häkchen bei der Bestätigung: "I acknowledge that..."
- Ohne diesen Schritt kann niemand deine Website sehen!

**Alle anderen Einstellungen:**
- Kannst du bei den Standardwerten lassen

### 3.4 Bucket erstellen
- Klicke auf **"Bucket erstellen"**

Dein Bucket erscheint jetzt in der Liste!

---

## Schritt 4: Dateien hochladen

### 4.1 Bucket öffnen
- Klicke auf den Namen deines Buckets

### 4.2 Dateien hochladen
- Klicke auf **"Upload"** / **"Hochladen"**
- Klicke auf **"Add files"** / **"Dateien hinzufügen"**
- Wähle alle deine Website-Dateien aus (index.html, error.html, style.css)
- Oder ziehe sie per Drag & Drop ins Browser-Fenster

### 4.3 Upload abschließen
- Scrolle nach unten
- Klicke auf **"Upload"**
- Warte, bis alle Dateien hochgeladen sind
- Klicke auf **"Close"**

Du siehst jetzt alle deine Dateien im Bucket!

---

## Schritt 5: Static Website Hosting aktivieren

### 5.1 Properties Tab öffnen
- Stelle sicher, dass du in deinem Bucket bist
- Klicke oben auf den Tab **"Properties"** / **"Eigenschaften"**

### 5.2 Static Website Hosting konfigurieren
- Scrolle ganz nach unten zu **"Static website hosting"**
- Klicke auf **"Edit"** / **"Bearbeiten"**

### 5.3 Einstellungen vornehmen
- Wähle **"Enable"** / **"Aktivieren"**
- Hosting type: **"Host a static website"**
- Index document: `index.html`
- Error document: `error.html`

### 5.4 Speichern
- Klicke auf **"Save changes"**

### 5.5 Website-URL notieren
Im Abschnitt "Static website hosting" siehst du jetzt eine URL wie:
```
http://meine-website-2025-test.s3-website.eu-central-1.amazonaws.com
```

**Kopiere diese URL** - das ist deine Website-Adresse!

⚠️ **Aber Achtung:** Wenn du sie jetzt aufrufst, bekommst du einen Fehler. Wir müssen noch den öffentlichen Zugriff erlauben!

---

## Schritt 6: Öffentlichen Zugriff erlauben (Bucket Policy)

Eine **Bucket Policy** ist eine Regel, die bestimmt, wer auf deinen Bucket zugreifen darf. Wir erstellen jetzt eine Policy, die jedem erlaubt, deine Dateien zu lesen.

### 6.1 Permissions Tab öffnen
- Klicke oben auf **"Permissions"** / **"Berechtigungen"**

### 6.2 Bucket Policy bearbeiten
- Scrolle zu **"Bucket policy"**
- Klicke auf **"Edit"** / **"Bearbeiten"**

### 6.3 Policy einfügen
Füge folgenden JSON-Code ein und **ersetze `DEIN-BUCKET-NAME`** mit deinem echten Bucket-Namen:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::DEIN-BUCKET-NAME/*"
        }
    ]
}
```

**Beispiel mit echtem Namen:**
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::meine-website-2025-test/*"
        }
    ]
}
```

### Was bedeutet diese Policy?

- `"Effect": "Allow"` → Wir erlauben etwas
- `"Principal": "*"` → Für jeden (das * bedeutet "alle")
- `"Action": "s3:GetObject"` → Die Aktion ist das Lesen von Dateien
- `"Resource": "arn:aws:s3:::..."` → Gilt für alle Dateien in deinem Bucket

### 6.4 Speichern
- Klicke auf **"Save changes"**

Du siehst jetzt die Warnung **"Publicly accessible"** - das ist richtig so! Es bedeutet, dass deine Website jetzt öffentlich zugänglich ist.

---

## Schritt 7: Deine Website testen

### 7.1 Website-URL aufrufen
- Gehe zurück zum **"Properties"** Tab
- Scrolle zu "Static website hosting"
- Klicke auf die **Bucket website endpoint** URL

### 🎉 Geschafft!

Deine Website sollte jetzt im Browser erscheinen!

### 7.2 Funktionen testen
- Rufe eine nicht existierende Seite auf (z.B. füge `/test.html` an die URL) → Du solltest deine error.html sehen
- Prüfe, ob das CSS korrekt geladen wird

---

## Schritt 8: Website aktualisieren

Wenn du später Änderungen vornehmen möchtest:

### 8.1 Dateien lokal bearbeiten
- Ändere deine HTML, CSS oder andere Dateien auf deinem PC

### 8.2 Erneut hochladen
- Gehe in deinen S3 Bucket
- Klicke auf **"Upload"**
- Lade die geänderten Dateien hoch
- S3 überschreibt automatisch Dateien mit gleichem Namen

### 8.3 Änderungen ansehen
- Rufe deine Website-URL auf
- Drücke `Strg + F5` für einen Hard Refresh (löscht Browser-Cache)

---

## Wichtige Begriffe erklärt

### Bucket
Ein Container (wie ein Ordner) in S3, in dem du Dateien speicherst.

### Objekt
So nennt S3 Dateien. Jedes Objekt hat einen Namen (Key) und Inhalt (Value).

### ARN (Amazon Resource Name)
Die eindeutige Kennung für AWS-Ressourcen:
```
arn:aws:s3:::meine-website-2025-test
```

### Static Website Hosting
Ein S3-Feature, das deinen Bucket wie einen einfachen Webserver funktionieren lässt.

### Bucket Policy
Eine JSON-Regel, die festlegt, wer auf deinen Bucket zugreifen darf.

---

## Häufige Probleme und Lösungen

### Problem: 403 Forbidden Error

**Mögliche Ursachen:**
- "Block all public access" ist noch aktiviert
- Bucket Policy fehlt oder ist falsch

**Lösung:**
1. Gehe zu Permissions → "Block public access settings"
2. Stelle sicher, dass "Block all public access" **AUS** ist
3. Prüfe deine Bucket Policy (siehe Schritt 6)
4. Stelle sicher, dass der Bucket-Name in der Policy korrekt ist

### Problem: 404 Error

**Mögliche Ursachen:**
- Die Datei index.html existiert nicht
- Tippfehler im Dateinamen

**Lösung:**
1. Prüfe, ob `index.html` wirklich im Bucket liegt
2. Achte auf Groß-/Kleinschreibung (index.html ≠ Index.html)
3. Prüfe die Static Website Hosting Konfiguration

### Problem: CSS wird nicht geladen

**Mögliche Ursachen:**
- Falscher Pfad in der HTML-Datei
- Tippfehler im Dateinamen

**Lösung:**
1. Nutze relative Pfade: `<link rel="stylesheet" href="style.css">`
2. Nicht: `<link rel="stylesheet" href="/style.css">`
3. Prüfe Dateinamen auf Tippfehler
4. Öffne die Browser-Konsole (F12) um Fehler zu sehen

### Problem: Änderungen sind nicht sichtbar

**Ursache:** Browser-Cache

**Lösung:**
- Drücke `Strg + Shift + R` für einen Hard Refresh
- Oder öffne die Seite im Inkognito-Modus
- Oder lösche den Browser-Cache

---

## Was kosten S3-Websites?

S3 berechnet:

- **Speicherplatz:** ca. 0,023 € pro GB/Monat (Frankfurt Region)
- **Requests:** ca. 0,0004 € pro 1000 Anfragen
- **Datenübertragung:** Erste 100 GB/Monat kostenlos, danach ca. 0,09 €/GB

**Beispiel:** Eine kleine Website mit 50 MB Größe und 1000 Besuchern pro Monat kostet weniger als 1 € pro Monat!

---

## Sicherheits-Tipps

1. **Keine sensiblen Daten hochladen**
   - Keine Passwörter, API-Keys oder persönliche Daten
   - Alles in S3 ist öffentlich, wenn du die Bucket Policy gesetzt hast

2. **Bucket Policy minimalistisch halten**
   - Gib nur die Rechte, die wirklich nötig sind
   - Für eine Website reicht `GetObject` (Lesen)

3. **Bucket-Namen klug wählen**
   - Keine sensiblen Informationen im Namen
   - Später kannst du eine eigene Domain verbinden

---

## Zusammenfassung: Was du gelernt hast

Was AWS S3 ist und wie es funktioniert  
Wie du einen S3 Bucket erstellst  
Wie du Dateien hochlädst  
Wie du Static Website Hosting aktivierst  
Wie du mit einer Bucket Policy öffentlichen Zugriff erlaubst  
Wie du deine Website testest und aktualisierst  
Die wichtigsten S3-Begriffe  

---


## Wichtige Links

- [AWS S3 Dokumentation](https://docs.aws.amazon.com/s3/)
- [AWS Free Tier](https://aws.amazon.com/de/free/) - Info über kostenlose Nutzung
- [AWS Support](https://console.aws.amazon.com/support/)

---

**Viel Erfolg mit deiner ersten S3-Website! **

Bei Fragen oder Problemen kannst du jederzeit nachfragen :)
