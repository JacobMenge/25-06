# AWS S3 Übungen - Schritt für Schritt

Praktische Aufgaben zum Vertiefen deiner S3-Kenntnisse

---

## Voraussetzungen

Bevor du mit diesen Übungen startest, solltest du:

- Das Basis-Tutorial "Statische Website mit AWS S3 hosten" durchgearbeitet haben
- Einen funktionierenden S3 Bucket mit einer einfachen Website haben
- Dich mit den S3-Grundbegriffen (Bucket, Objekt, Policy) auskennen
- Zugriff auf die AWS Console haben

---

## Übersicht der Übungen

Die Übungen sind in drei Level unterteilt:

**Level 1: Grundlagen & Verständnis**
- Übung 1: Ordnerstrukturen anlegen und verstehen
- Übung 2: Objekte kopieren und löschen
- Übung 3: Metadaten und Content-Type anpassen

**Level 2: Zugriff & Sicherheit**
- Übung 4: Private und öffentliche Dateien
- Übung 5: Erweiterte Bucket Policies schreiben

**Level 3: Mini-Projekte**
- Übung 6: Bildergalerie erstellen
- Übung 7: PDF-Downloads einbinden
- Übung 8: Redirects konfigurieren

**Geschätzte Gesamtdauer:** 2-3 Stunden

---

# Level 1: Grundlagen & Verständnis

---

## Übung 1: Ordnerstrukturen anlegen und verstehen

### Lernziel
Du verstehst, wie S3 mit "Ordnern" umgeht und kannst Objekte strukturiert organisieren.

### Hintergrundwissen

**Wichtig zu wissen:** S3 hat eigentlich **keine echten Ordner**!

Was du als "Ordner" siehst, ist nur eine visuelle Darstellung. In Wirklichkeit ist alles ein **Key** (Schlüssel):

- Was aussieht wie: `images/foto1.jpg`
- Ist in Wirklichkeit: Ein Objekt mit dem Key `images/foto1.jpg`
- Der `/` ist Teil des Dateinamens, kein Ordner-Trennzeichen

S3 zeigt es dir der Einfachheit halber als Ordnerstruktur an.

### Aufgabe

Erstelle in deinem Bucket folgende Struktur:

```
mein-bucket/
├── images/
│   ├── logo.png
│   └── header.jpg
├── docs/
│   ├── anleitung.pdf
│   └── readme.txt
└── css/
    └── main.css
```

### Schritt-für-Schritt Anleitung

#### 1.1 Ordner erstellen

1. Öffne deinen S3 Bucket
2. Klicke auf **"Create folder"** / **"Ordner erstellen"**
3. Gib als Namen ein: `images`
4. Klicke auf **"Create folder"**
5. Wiederhole dies für `docs` und `css`

**Hinweis:** Du siehst jetzt drei "Ordner" mit Ordner-Icons!

#### 1.2 Dummy-Dateien vorbereiten

Erstelle auf deinem PC im Ordner `C:\s3-uebungen\` folgende einfache Testdateien:

**logo.png**
- Erstelle ein beliebiges kleines Bild (z.B. in Paint)
- Speichere es als `logo.png`

**header.jpg**
- Erstelle ein weiteres Bild
- Speichere es als `header.jpg`

**anleitung.pdf**
- Erstelle in Word eine einfache Seite mit Text "Test-Dokument"
- Speichere als PDF: `anleitung.pdf`

**readme.txt**
- Erstelle eine Textdatei mit Inhalt: "Dies ist eine Readme-Datei"
- Speichere als `readme.txt`

**main.css**
- Erstelle eine Textdatei mit Inhalt:
```css
body { font-family: Arial; }
```
- Speichere als `main.css`

#### 1.3 Dateien hochladen

1. Klicke auf den Ordner **`images`**
2. Klicke auf **"Upload"**
3. Lade `logo.png` und `header.jpg` hoch
4. Klicke auf **"Upload"**

5. Gehe zurück (klicke auf den Bucket-Namen oben)
6. Klicke auf den Ordner **`docs`**
7. Lade `anleitung.pdf` und `readme.txt` hoch

8. Wiederhole für den Ordner **`css`**
9. Lade `main.css` hoch

#### 1.4 Die Objekt-Keys verstehen

1. Klicke im Bucket auf die Datei `images/logo.png`
2. Schau dir oben die **"Object URL"** an:
```
https://mein-bucket.s3.eu-central-1.amazonaws.com/images/logo.png
```

3. Beachte: Der komplette Pfad `images/logo.png` ist der **Key**

4. Klicke auf **"Properties"** / **"Eigenschaften"**
5. Siehst du den Eintrag **"Key"**? Dort steht: `images/logo.png`

### Ergebnis-Check

- [ ] Du hast 3 "Ordner" erstellt
- [ ] Jeder Ordner enthält mindestens eine Datei
- [ ] Du verstehst, dass der Pfad Teil des Keys ist
- [ ] Du kannst die Objekt-URL eines beliebigen Objekts aufrufen

### Zusatzwissen

**Frage:** Warum macht S3 das so kompliziert?

**Antwort:** S3 ist ein **Objekt-Speicher**, kein Dateisystem. Diese Architektur macht S3:
- Extrem skalierbar (Milliarden von Objekten)
- Schneller bei großen Datenmengen
- Einfacher zu verteilen über mehrere Server

**Praktische Konsequenz:**
- Du kannst keine Ordner "verschieben"
- Du musst Dateien einzeln kopieren, wenn du die Struktur ändern willst

---

## Übung 2: Objekte kopieren und löschen

### Lernziel
Du lernst, wie man Objekte in S3 kopiert, verschiebt und löscht.

### Hintergrundwissen

In S3 gibt es **kein "Verschieben"**. Stattdessen:
1. Kopierst du das Objekt an den neuen Ort
2. Löschst das Original

Das ist wichtig zu verstehen, weil es Auswirkungen hat:
- Kosten: Beide Objekte existieren kurzzeitig doppelt
- Zeit: Bei großen Dateien dauert es länger
- Versionierung: Alte Versionen bleiben (wenn aktiviert)

**Technischer Hintergrund:** Auch wenn du in der Console "Rename" siehst oder Metadaten bearbeitest - intern führt S3 immer ein **Copy-in-Place** durch und löscht das alte Objekt.

### Aufgabe

1. Lade eine neue Datei `test.txt` in deinen Bucket hoch
2. Kopiere sie in den Ordner `docs/`
3. Lösche das Original
4. Erstelle eine Kopie mit anderem Namen

### Schritt-für-Schritt Anleitung

#### 2.1 Testdatei erstellen und hochladen

1. Erstelle auf deinem PC eine Datei `test.txt` mit folgendem Inhalt:
```
Dies ist eine Testdatei für Übung 2.
Version 1
```

2. Gehe zu deinem S3 Bucket
3. Klicke auf **"Upload"**
4. Lade `test.txt` hoch (direkt in den Root des Buckets, nicht in einen Ordner)

#### 2.2 Datei kopieren

1. Wähle die Datei `test.txt` aus (Checkbox anklicken)
2. Klicke auf **"Actions"** → **"Copy"** / **"Kopieren"**
3. Es erscheint eine Bestätigung oben rechts

4. Navigiere zum Ordner **`docs`** (klicke auf den Ordner-Namen)
5. Klicke auf **"Actions"** → **"Paste"** / **"Einfügen"**
6. Im Dialog siehst du die Ziel-Einstellungen
7. Klicke auf **"Paste"** / **"Einfügen"**

**Wichtig:** Die Datei behält ihren ursprünglichen Namen `test.txt`

#### 2.3 Original löschen

1. Gehe zurück zum Bucket-Root (klicke oben auf den Bucket-Namen)
2. Wähle die originale `test.txt` aus (im Root, nicht im docs-Ordner)
3. Klicke auf **"Delete"** / **"Löschen"**
4. Es erscheint ein Bestätigungsdialog
5. Tippe zur Bestätigung `permanently delete` in das Textfeld
6. Klicke **"Delete objects"**

**Wichtig:** AWS will sichergehen, dass du nicht versehentlich löschst!

#### 2.4 Datei "umbenennen" (Copy + Delete)

S3 kann Dateien nicht direkt umbenennen. Du musst eine neue Kopie mit anderem Key erstellen:

1. Gehe zum Ordner **`docs`**
2. Wähle `test.txt` aus
3. Klicke **"Actions"** → **"Copy"**

4. Bleibe im gleichen Ordner oder navigiere dorthin
5. Klicke **"Actions"** → **"Paste"**
6. Im Paste-Dialog unter **"Destination"**:
   - Ändere bei **"Objects"** den Key von `docs/test.txt` zu `docs/test-kopie.txt`
   - Bei mehreren Dateien musst du das Präfix ändern
7. Klicke **"Paste"**

Jetzt hast du beide Dateien: `docs/test.txt` und `docs/test-kopie.txt`

**Alternative:** Manche S3-UIs zeigen auch direkt "Rename" im Actions-Menü - dies führt intern ebenfalls ein Copy + Delete durch.

### Ergebnis-Check

- [ ] Die Datei `test.txt` existiert im Ordner `docs/`
- [ ] Die originale `test.txt` im Root ist gelöscht
- [ ] Du verstehst, warum es kein echtes "Verschieben" gibt
- [ ] Du hast optional eine Kopie mit anderem Namen erstellt

### Vertiefung: Mehrere Dateien auf einmal

**Aufgabe:** Kopiere alle Dateien aus `images/` in einen neuen Ordner `backup-images/`

<details>
<summary>Lösung anzeigen</summary>

1. Erstelle den Ordner `backup-images/`
2. Gehe zum Ordner `images/`
3. Wähle **alle** Dateien aus (Checkbox bei allen Dateien)
4. Klicke **"Actions"** → **"Copy"**
5. Gehe zu `backup-images/`
6. Klicke **"Actions"** → **"Paste"**

</details>

---

## Übung 3: Metadaten und Content-Type anpassen

### Lernziel
Du verstehst, wie S3 Dateitypen erkennt und wie du sie manuell anpassen kannst.

### Hintergrundwissen

Jedes Objekt in S3 hat **Metadaten**. Das sind Informationen **über** die Datei:

**System-Metadaten (von S3 verwaltet):**
- Größe
- Letztes Änderungsdatum
- ETag (Prüfsumme)

**Benutzer-Metadaten (von dir steuerbar):**
- **Content-Type** (MIME-Type) - Sagt dem Browser, wie er die Datei behandeln soll
- Cache-Control
- Eigene Metadaten (z.B. `x-amz-meta-author: Max`)

### Warum ist Content-Type wichtig?

Der **Content-Type** bestimmt, wie dein Browser die Datei interpretiert:

| Datei | Richtiger Content-Type | Falscher Content-Type | Folge |
|-------|------------------------|----------------------|-------|
| style.css | text/css | text/plain | CSS wird nicht angewendet |
| bild.jpg | image/jpeg | text/html | Bild wird als Text angezeigt |
| daten.json | application/json | text/plain | JSON wird nicht geparst |

### Aufgabe

1. Lade eine CSS-Datei mit **falschem** Content-Type hoch
2. Überprüfe, dass sie nicht funktioniert
3. Korrigiere den Content-Type
4. Überprüfe, dass sie jetzt funktioniert

### Schritt-für-Schritt Anleitung

#### 3.1 CSS-Datei vorbereiten

Erstelle eine Datei `test-style.css` auf deinem PC:

```css
body {
    background-color: lightblue;
    font-family: Arial, sans-serif;
    padding: 20px;
}

h1 {
    color: darkblue;
    border-bottom: 3px solid navy;
}
```

#### 3.2 Testseite erstellen

Erstelle eine HTML-Datei `meta-test.html`:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Metadaten Test</title>
    <link rel="stylesheet" href="test-style.css">
</head>
<body>
    <h1>Metadaten-Test</h1>
    <p>Wenn diese Seite einen blauen Hintergrund hat, funktioniert das CSS.</p>
    <p>Wenn nicht, stimmt der Content-Type nicht!</p>
</body>
</html>
```

#### 3.3 CSS-Datei mit falschem Namen hochladen

Um einen falschen Content-Type zu erzwingen, laden wir die CSS-Datei mit falscher Endung hoch:

1. Benenne die Datei `test-style.css` auf deinem PC um in `test-style.txt`
2. Gehe zu deinem S3 Bucket
3. Lade `test-style.txt` hoch
4. Lade auch `meta-test.html` hoch

**Was ist passiert?** S3 erkennt die Datei als `.txt` und setzt automatisch `Content-Type: text/plain` statt `text/css`

#### 3.4 Problem überprüfen

1. Passe die HTML-Datei an, damit sie auf die .txt-Datei verweist:
   - Ändere in `meta-test.html` den Link zu: `<link rel="stylesheet" href="test-style.txt">`
   - Lade die aktualisierte HTML-Datei hoch

2. Gehe zu **"Properties"** Tab deines Buckets
3. Klicke auf **"Static website hosting"**
4. Kopiere deine Website-URL
5. Öffne: `http://deine-url.amazonaws.com/meta-test.html`

**Ergebnis:**
- Die Seite lädt
- Aber: **Kein blauer Hintergrund!**
- Öffne die Browser-Konsole (F12 → Console-Tab)
- Du siehst einen Fehler ähnlich wie: "Resource interpreted as Stylesheet but transferred with MIME type text/plain"

**Cache-Hinweis:** Wenn du Änderungen vornimmst, drücke immer **Strg + F5** (Windows) bzw. **Cmd + Shift + R** (Mac) für einen Hard Refresh, um den Browser-Cache zu umgehen.

#### 3.5 Content-Type korrigieren - Methode 1 (Datei korrekt hochladen)

**Einfachste Lösung:**

1. Lösche `test-style.txt` aus dem Bucket
2. Benenne die Datei auf deinem PC zurück zu `test-style.css`
3. Lade `test-style.css` hoch
4. S3 erkennt jetzt automatisch: `Content-Type: text/css`

5. Passe die HTML-Datei wieder an:
```html
<link rel="stylesheet" href="test-style.css">
```

6. Lade die aktualisierte HTML-Datei hoch

7. Teste die Website erneut (mit Strg + F5 für Hard Refresh)

**Jetzt sollte die Seite einen blauen Hintergrund haben!**

#### 3.6 Content-Type korrigieren - Methode 2 (Metadaten ändern)

**Alternative Lösung ohne erneuten Upload:**

Wenn du die Datei `test-style.txt` behalten möchtest:

1. Klicke im Bucket auf die Datei `test-style.txt`
2. Gehe zum Tab **"Properties"**
3. Scrolle zu **"Metadata"**
4. Klicke auf **"Edit"**
5. Unter **"System-defined metadata"** findest du **"Content-Type"**
6. Ändere den Wert von `text/plain` zu `text/css`
7. Klicke **"Save changes"**

**Hinweis:** Intern führt S3 ein Copy-in-Place durch - das Objekt wird neu geschrieben.

8. Stelle sicher, dass deine HTML-Datei auf `test-style.txt` verlinkt
9. Aktualisiere deine Website (Strg + F5)

**Jetzt sollte es auch funktionieren!**

### Ergebnis-Check

- [ ] Du verstehst, was Content-Type bedeutet
- [ ] Du kannst Metadaten in S3 bearbeiten
- [ ] Du siehst, wie falsche Metadaten zu Problemen führen
- [ ] Die Testseite zeigt einen blauen Hintergrund

### Vertiefungsaufgabe

**Aufgabe:** Lade ein Bild (.jpg) als .txt hoch und korrigiere den Content-Type

<details>
<summary>Lösung anzeigen</summary>

1. Benenne `bild.jpg` um in `bild.txt`
2. Lade es in S3 hoch
3. Versuche die Datei über die Objekt-URL zu öffnen - du siehst wirre Zeichen
4. Gehe zu **Properties** → **Metadata** → **Edit**
5. Ändere Content-Type zu `image/jpeg`
6. Öffne die URL erneut - jetzt siehst du das Bild!

</details>

### Häufige Content-Types Übersicht

| Dateityp | Content-Type | Beispiel |
|----------|-------------|----------|
| HTML | text/html | index.html |
| CSS | text/css | style.css |
| JavaScript | application/javascript | script.js |
| JSON | application/json | data.json |
| JPEG-Bild | image/jpeg | foto.jpg |
| PNG-Bild | image/png | logo.png |
| PDF | application/pdf | dokument.pdf |
| Plain Text | text/plain | readme.txt |
| MP4-Video | video/mp4 | video.mp4 |

**Hinweis:** `text/javascript` funktioniert auch, aber `application/javascript` ist der aktuelle Standard.

---

# Level 2: Zugriff & Sicherheit

---

## Übung 4: Private und öffentliche Dateien

### Lernziel
Du verstehst den Unterschied zwischen privaten und öffentlichen Objekten und kannst gezielt steuern, was zugänglich ist.

### Hintergrundwissen

In S3 gibt es verschiedene Ebenen der Zugriffskontrolle:

**1. Bucket-Ebene:**
- "Block Public Access" (alle Objekte betroffen)
- Bucket Policy (JSON-Regeln für den gesamten Bucket)

**2. Objekt-Ebene:**
- Object ACL (Access Control List) - individuelle Objekt-Rechte (veraltet, nicht empfohlen)
- Bucket Policy mit spezifischen Pfaden (empfohlen)

**Der Unterschied:**
- **Öffentlich:** Jeder mit der URL kann die Datei sehen
- **Privat:** Nur authentifizierte AWS-Nutzer mit Berechtigung

**Wichtiger Hinweis:** AWS empfiehlt mittlerweile, Object ACLs zu deaktivieren und stattdessen Bucket Policies zu verwenden. Wir werden daher ausschließlich mit Bucket Policies arbeiten.

---

**WICHTIG: Block Public Access prüfen**

Bevor du mit öffentlichen Policies arbeitest, muss folgende Einstellung korrekt sein:

1. Gehe zu deinem Bucket
2. Klicke auf **"Permissions"** Tab
3. Scrolle zu **"Block public access (bucket settings)"**
4. Klicke **"Edit"**
5. **Deaktiviere** "Block all public access" (Haken entfernen)
6. Bestätige mit "I acknowledge..."
7. Klicke **"Save changes"**

**Ohne diesen Schritt funktionieren öffentliche Bucket Policies nicht!**

---

### Aufgabe

Erstelle zwei Dateien:
1. Eine **öffentliche** Datei über die Bucket Policy
2. Eine **private** Datei (ohne Policy-Eintrag)
3. Teste beide Szenarien

### Schritt-für-Schritt Anleitung

#### 4.1 Testdateien erstellen

Erstelle auf deinem PC zwei Textdateien:

**public-file.txt:**
```
Dies ist eine öffentliche Datei.
Jeder mit der URL kann sie lesen.
```

**private-file.txt:**
```
Dies ist eine private Datei.
Sie sollte nur für autorisierte Nutzer sichtbar sein.
Geheime Info: Passwort123
```

#### 4.2 Ordnerstruktur anlegen

1. Erstelle im Bucket zwei Ordner:
   - `public` - für öffentliche Dateien
   - `private` - für private Dateien

2. Lade `public-file.txt` in den Ordner `public/` hoch
3. Lade `private-file.txt` in den Ordner `private/` hoch

#### 4.3 Bucket Policy anpassen

**Wichtig:** Wenn du noch die Policy aus dem Basis-Tutorial hast, die ALLES öffentlich macht, musst du sie jetzt ändern.

1. Gehe zu **"Permissions"** Tab
2. Scrolle zu **"Bucket policy"**
3. Klicke **"Edit"**

4. Ersetze die Policy durch folgende (die nur `/public/` öffentlich macht):

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForPublicFolder",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::DEIN-BUCKET-NAME/public/*"
        }
    ]
}
```

**Wichtig:** Ersetze `DEIN-BUCKET-NAME` mit deinem echten Bucket-Namen!

5. Klicke **"Save changes"**

#### 4.4 Zugriff testen

**Test-Checkliste:**
- [ ] Block Public Access ist deaktiviert
- [ ] Bucket Policy ist gespeichert
- [ ] JSON-Syntax ist valide (kein Fehler beim Speichern)

**Test 1: Private Datei**

1. Klicke im Bucket auf `private/private-file.txt`
2. Kopiere die **"Object URL"** (nicht die "S3 URI")
3. Öffne diese URL in einem **neuen Inkognito-Fenster** (Strg + Shift + N)

**Ergebnis:**
```xml
<Error>
  <Code>AccessDenied</Code>
  <Message>Access Denied</Message>
</Error>
```

Das ist korrekt! Die Datei ist privat.

**Test 2: Öffentliche Datei**

1. Klicke auf `public/public-file.txt`
2. Kopiere die Object URL
3. Öffne sie im Inkognito-Fenster

**Ergebnis:**
```
Dies ist eine öffentliche Datei.
Jeder mit der URL kann sie lesen.
```

Perfekt! Die Datei ist öffentlich zugänglich.

### Ergebnis-Check

- [ ] Block Public Access ist deaktiviert
- [ ] Dateien in `/public/` sind öffentlich zugänglich
- [ ] Dateien in `/private/` sind nicht zugänglich
- [ ] Du verstehst, wie Bucket Policies Zugriff steuern
- [ ] Du hast beide Szenarien erfolgreich getestet

### Zusatzwissen: Object ACLs vs. Bucket Policies

**Object ACLs (veraltet):**
- Pro Datei einzeln konfigurierbar
- Kompliziert bei vielen Dateien
- AWS empfiehlt, sie zu deaktivieren

**Bucket Policies (empfohlen):**
- Zentrale Verwaltung
- Regelbasiert (z.B. nach Pfaden)
- Besser skalierbar
- Mehr Kontrolle

**Best Practice:** Nutze ausschließlich Bucket Policies für die Zugriffskontrolle.

---

## Übung 5: Erweiterte Bucket Policies schreiben

### Lernziel
Du lernst, granulare Bucket Policies zu schreiben, die nur bestimmte Bereiche deines Buckets öffentlich machen.

### Hintergrundwissen

Im Basis-Tutorial hast du vielleicht eine Policy geschrieben, die **alles** öffentlich macht:

```json
"Resource": "arn:aws:s3:::mein-bucket/*"
```

Das `/*` am Ende bedeutet: **Alle Objekte im Bucket**.

**Aber:** Was, wenn du nur einen Teil öffentlich machen willst?

**Lösung:** Nutze spezifische Pfad-Präfixe in der Resource-Angabe.

---

**WICHTIG: Präfixe und Wildcards**

Die Wildcard `*` matcht **alles**, auch Unterordner:
- `/*.html` matcht auch `unterordner/datei.html`
- Für präzise Kontrolle: Nutze Ordner-Präfixe wie `/public/*`

---

### Aufgabe

Erstelle eine Bucket Policy, die:
1. Nur Dateien im Ordner `/public/` öffentlich macht
2. Dateien im Ordner `/downloads/` ebenfalls öffentlich macht
3. Alle anderen Dateien privat lässt

### Schritt-für-Schritt Anleitung

#### 5.1 Ordnerstruktur vorbereiten

1. Erstelle im Bucket drei Ordner (falls noch nicht vorhanden):
   - `public`
   - `downloads`
   - `internal`

2. Erstelle auf deinem PC verschiedene Testdateien:

**public-info.txt:**
```
Öffentliche Information
```

**download-datei.txt:**
```
Herunterladbare Datei
```

**internal-doc.txt:**
```
Internes Dokument - Vertraulich
```

3. Lade die Dateien in die entsprechenden Ordner:
   - `public-info.txt` → in `/public/`
   - `download-datei.txt` → in `/downloads/`
   - `internal-doc.txt` → in `/internal/`

#### 5.2 Multi-Path Bucket Policy erstellen

1. Gehe zu **"Permissions"** Tab
2. Scrolle zu **"Bucket policy"**
3. Klicke **"Edit"**

4. Verwende folgende Policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForPublicFolder",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::DEIN-BUCKET-NAME/public/*"
        },
        {
            "Sid": "PublicReadForDownloadsFolder",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::DEIN-BUCKET-NAME/downloads/*"
        }
    ]
}
```

**Wichtig:** Ersetze `DEIN-BUCKET-NAME` zweimal mit deinem echten Bucket-Namen!

#### 5.3 Policy-Syntax verstehen

**Die Änderungen im Detail:**

**Zwei separate Statements:**
- Statement 1: Macht `/public/*` öffentlich
- Statement 2: Macht `/downloads/*` öffentlich
- Alles andere (wie `/internal/*`) bleibt privat

**Jedes Statement hat:**
- `Sid`: Eindeutiger Name (zur Identifikation)
- `Effect`: "Allow" = Erlauben
- `Principal`: "*" = Für alle
- `Action`: "s3:GetObject" = Lesen erlaubt
- `Resource`: Welche Objekte betroffen sind

#### 5.4 Policy speichern und testen

1. Klicke **"Save changes"**

**Test-Checkliste vor dem Testen:**
- [ ] Block Public Access ist deaktiviert
- [ ] Bucket Policy ist gespeichert (JSON valide)
- [ ] Browser-Cache geleert (Strg + F5)

2. **Test 1: Öffentliche Ordner**
   - Kopiere die Object URL von `public/public-info.txt`
   - Öffne sie im Inkognito-Fenster
   - **Erwartet:** Datei ist sichtbar
   
   - Kopiere die Object URL von `downloads/download-datei.txt`
   - Öffne sie im Inkognito-Fenster
   - **Erwartet:** Datei ist sichtbar

3. **Test 2: Privater Ordner**
   - Kopiere die Object URL von `internal/internal-doc.txt`
   - Öffne sie im Inkognito-Fenster
   - **Erwartet:** "Access Denied"

Perfekt! Die Policy funktioniert wie gewünscht.

### Ergebnis-Check

- [ ] Dateien in `/public/` sind öffentlich
- [ ] Dateien in `/downloads/` sind öffentlich
- [ ] Dateien in `/internal/` sind privat
- [ ] Du verstehst das Multi-Statement Konzept
- [ ] Du kannst die Policy auf andere Ordner erweitern

### Vertiefung: Condition-basierte Policies

Für fortgeschrittene Szenarien kannst du Bedingungen hinzufügen:

**Beispiel: Nur HTTPS-Zugriff erlauben**

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadOnlyOverHTTPS",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::DEIN-BUCKET-NAME/public/*",
            "Condition": {
                "Bool": {
                    "aws:SecureTransport": "true"
                }
            }
        }
    ]
}
```

Dies erzwingt, dass Zugriffe nur über HTTPS (nicht HTTP) erfolgen.

**Hinweis:** Der S3-Website-Endpoint liefert nur HTTP aus. Für HTTPS brauchst du CloudFront + ACM-Zertifikat.

### Policy Best Practices

1. **Principle of Least Privilege:** Gib nur die Rechte, die wirklich nötig sind
2. **Strukturierte Ordner:** Nutze eine klare Ordnerstruktur
3. **Aussagekräftige Sids:** Benenne Statements klar (z.B. "PublicReadForBlogImages")
4. **Dokumentation:** Kommentiere komplexe Policies (außerhalb der JSON)
5. **Testen:** Teste immer im Inkognito-Modus

---

# Level 3: Mini-Projekte

---

## Übung 6: Mini-Bildergalerie erstellen

### Lernziel
Du erstellst eine funktionale Bildergalerie, die Bilder aus S3 lädt und verstehst, wie S3 als CDN für statische Assets funktioniert.

### Hintergrundwissen

S3 eignet sich perfekt als **Content Delivery** für:
- Bilder
- Videos
- Downloads
- JavaScript-Bibliotheken

**Vorteile:**
- Trennung von Code und Assets
- Skalierbar (unbegrenzt viele Bilder)
- Schnell (S3 ist global verteilt)
- Kostengünstig

**Wichtiger Hinweis zu HTTPS:**
Der S3-Website-Endpoint (`http://bucket.s3-website.region.amazonaws.com`) liefert nur **HTTP** aus, nicht HTTPS. Für HTTPS brauchst du CloudFront als CDN + ein ACM-Zertifikat. Das ist ein fortgeschrittenes Thema für später.

### Aufgabe

Erstelle eine Bildergalerie-Website mit:
- Mindestens 4 Bildern
- Responsive Design (funktioniert auf Handy + Desktop)
- Hover-Effekte
- Beschreibungen zu jedem Bild

### Schritt-für-Schritt Anleitung

#### 6.1 Ordnerstruktur planen

Um Wildcard-Probleme mit `/*.html` zu vermeiden, nutzen wir eine saubere Struktur:

**Empfohlene Struktur:**
```
mein-bucket/
└── public/
    ├── gallery.html
    ├── gallery.css
    └── gallery/
        ├── galerie-01.jpg
        ├── galerie-02.jpg
        ├── galerie-03.jpg
        └── galerie-04.jpg
```

Alles liegt unter `/public/` - so reicht eine einfache Policy.

#### 6.2 Bilder vorbereiten

1. Suche 4-6 Bilder (z.B. von [Unsplash](https://unsplash.com/) oder eigene Fotos)
2. Benenne sie sinnvoll um:
   - `galerie-01.jpg`
   - `galerie-02.jpg`
   - `galerie-03.jpg`
   - `galerie-04.jpg`

**Wichtig:** Optimiere die Bildgröße (max. 1920px Breite, um Ladezeiten zu minimieren)

3. Erstelle im Bucket:
   - Den Ordner `public`
   - Darin den Unterordner `gallery`

4. Lade alle Bilder in den Ordner `public/gallery/` hoch

#### 6.3 HTML-Galerie erstellen

Erstelle eine Datei `gallery.html` auf deinem PC:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meine S3 Bildergalerie</title>
    <link rel="stylesheet" href="gallery.css">
</head>
<body>
    <header>
        <h1>Meine Bildergalerie</h1>
        <p>Alle Bilder werden aus AWS S3 geladen</p>
    </header>

    <div class="gallery">
        <div class="gallery-item">
            <img src="gallery/galerie-01.jpg" alt="Bild 1" loading="lazy">
            <div class="caption">
                <h3>Sonnenuntergang</h3>
                <p>Ein wunderschöner Sonnenuntergang am Meer</p>
            </div>
        </div>

        <div class="gallery-item">
            <img src="gallery/galerie-02.jpg" alt="Bild 2" loading="lazy">
            <div class="caption">
                <h3>Berge</h3>
                <p>Majestätische Berglandschaft</p>
            </div>
        </div>

        <div class="gallery-item">
            <img src="gallery/galerie-03.jpg" alt="Bild 3" loading="lazy">
            <div class="caption">
                <h3>Stadt</h3>
                <p>Moderne Stadtarchitektur</p>
            </div>
        </div>

        <div class="gallery-item">
            <img src="gallery/galerie-04.jpg" alt="Bild 4" loading="lazy">
            <div class="caption">
                <h3>Natur</h3>
                <p>Grüne Wälder und Natur</p>
            </div>
        </div>
    </div>

    <footer>
        <p>&copy; 2025 - Gehostet auf AWS S3</p>
    </footer>
</body>
</html>
```

**Hinweis:** Das `loading="lazy"` Attribut sorgt dafür, dass Bilder erst geladen werden, wenn sie sichtbar werden - Performance-Optimierung!

#### 6.4 CSS für die Galerie

Erstelle eine Datei `gallery.css` auf deinem PC:

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    padding: 20px;
}

header {
    text-align: center;
    color: white;
    margin-bottom: 40px;
    padding: 30px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

header p {
    font-size: 1.1em;
    opacity: 0.9;
}

.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.gallery-item {
    background: white;
    border-radius: 15px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.gallery-item:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.4);
}

.gallery-item img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    display: block;
}

.caption {
    padding: 20px;
}

.caption h3 {
    color: #333;
    margin-bottom: 10px;
    font-size: 1.3em;
}

.caption p {
    color: #666;
    line-height: 1.6;
}

footer {
    text-align: center;
    color: white;
    margin-top: 50px;
    padding: 20px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

/* Responsive Design */
@media (max-width: 768px) {
    header h1 {
        font-size: 2em;
    }
    
    .gallery {
        grid-template-columns: 1fr;
        gap: 20px;
    }
}
```

#### 6.5 Dateien hochladen

1. Lade `gallery.html` in den Ordner `public/` hoch
2. Lade `gallery.css` in den Ordner `public/` hoch
3. Stelle sicher, dass die Bilder in `public/gallery/` liegen

#### 6.6 Bucket Policy für /public/*

Verwende diese einfache, robuste Policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForPublicFolder",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::DEIN-BUCKET-NAME/public/*"
        }
    ]
}
```

**Vorteil:** Alle Dateien unter `/public/` sind zugänglich, egal ob HTML, CSS oder Bilder. Keine Wildcard-Probleme mit Unterordnern.

#### 6.7 Testen

**Test-Checkliste:**
- [ ] Block Public Access ist deaktiviert
- [ ] Bucket Policy `public/*` ist gesetzt
- [ ] Static Website Hosting ist aktiviert
- [ ] Index document ist `index.html` (aus dem Basis-Tutorial)

1. Öffne deine Website-URL:
```
http://dein-bucket.s3-website.eu-central-1.amazonaws.com/public/gallery.html
```

2. Falls du einen anderen Index haben möchtest, kannst du auch in Static Website Hosting den Index auf `public/gallery.html` setzen

Du solltest jetzt eine schöne Bildergalerie sehen!

**Cache-Hinweis:** Wenn Änderungen nicht sichtbar sind, drücke **Strg + F5** für einen Hard Refresh.

### Ergebnis-Check

- [ ] Alle Bilder werden korrekt angezeigt
- [ ] Das Design ist responsive (teste auf dem Handy oder verkleinere das Browserfenster)
- [ ] Hover-Effekte funktionieren (Karten heben sich beim Überfahren)
- [ ] Die Galerie lädt schnell (dank lazy loading)

### Vertiefung: Cache-Control für bessere Performance

Du kannst Metadaten setzen, damit Browser Bilder cachen:

1. Wähle alle Bilder in `public/gallery/` aus
2. Actions → Edit metadata
3. Füge hinzu: **Cache-Control** = `public, max-age=31536000`

Dies sagt dem Browser: "Cache dieses Bild 1 Jahr lang"

**Testweise beim Entwickeln:** Setze `Cache-Control: no-cache` um sofortige Änderungen zu sehen.

---

## Übung 7: PDF-Downloads einbinden

### Lernziel
Du lernst, wie du Download-Links für PDFs und andere Dateien erstellst und verstehst den Unterschied zwischen Inline-Anzeige und Download.

### Hintergrundwissen

Wenn ein Nutzer auf eine Datei klickt, gibt es zwei Möglichkeiten:

**1. Inline-Anzeige (im Browser):**
- Browser zeigt die Datei direkt an
- Standard bei PDFs, Bildern, Videos
- HTTP-Header: `Content-Disposition: inline`

**2. Download:**
- Browser lädt die Datei herunter
- Datei wird nicht im Browser geöffnet
- HTTP-Header: `Content-Disposition: attachment`

Du kannst das über S3-Metadaten steuern!

### Aufgabe

Erstelle eine Download-Seite mit:
- 3 PDFs
- 1 PDF wird im Browser angezeigt (inline)
- 2 PDFs werden direkt heruntergeladen (attachment)
- Übersichtliche Darstellung mit Beschreibungen

### Schritt-für-Schritt Anleitung

#### 7.1 Ordnerstruktur

Wir nutzen wieder die `/public/` Struktur:

```
public/
├── downloads.html
├── downloads.css
└── downloads/
    ├── anleitung.pdf
    ├── formular.pdf
    └── bericht.pdf
```

#### 7.2 PDF-Dateien vorbereiten

Du benötigst 3 einfache PDF-Dateien. Du kannst:
- Eigene PDFs verwenden
- In Word/LibreOffice simple Dokumente erstellen und als PDF speichern

Benenne sie:
- `anleitung.pdf` (wird im Browser angezeigt)
- `formular.pdf` (wird heruntergeladen)
- `bericht.pdf` (wird heruntergeladen)

#### 7.3 Dateien hochladen

1. Erstelle im Bucket den Ordner `public/downloads`
2. Lade alle 3 PDFs in den Ordner `public/downloads/` hoch

#### 7.4 Metadaten für Download-PDFs setzen

Für die Dateien, die heruntergeladen werden sollen:

**Für formular.pdf:**
1. Klicke im Bucket auf `public/downloads/formular.pdf`
2. Gehe zum Tab **"Properties"**
3. Scrolle zu **"Metadata"**
4. Klicke **"Edit"**
5. Klicke **"Add metadata"**
6. Wähle **"Type"**: System defined
7. Wähle **"Key"**: Content-Disposition
8. Gib als **"Value"** ein: `attachment; filename="formular.pdf"`
9. Klicke **"Save changes"**

**Für bericht.pdf:**
Wiederhole die gleichen Schritte mit:
- Value: `attachment; filename="bericht.pdf"`

**Für anleitung.pdf:**
Lass die Metadaten unverändert (Standard ist inline-Anzeige)

**Was bewirkt das?**
- Mit `Content-Disposition: attachment` wird der Browser die Datei herunterladen
- Ohne diese Einstellung (oder mit `inline`) zeigt der Browser die Datei an

**Browser-Unterschied:** Manche Browser (besonders Chrome) zeigen PDFs trotz `attachment` im integrierten PDF-Viewer an. Das Verhalten kann variieren.

#### 7.5 Download-Seite erstellen

Erstelle `downloads.html` auf deinem PC:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Downloads</title>
    <link rel="stylesheet" href="downloads.css">
</head>
<body>
    <div class="container">
        <header>
            <h1>Download-Center</h1>
            <p>Alle Dokumente werden sicher auf AWS S3 gehostet</p>
        </header>

        <div class="downloads">
            <!-- PDF zum Anzeigen -->
            <div class="download-card">
                <div class="icon">PDF</div>
                <div class="info">
                    <h2>Anleitung</h2>
                    <p>Wichtige Bedienungsanleitung</p>
                    <span class="tag view">Ansicht im Browser</span>
                </div>
                <div class="actions">
                    <a href="downloads/anleitung.pdf" target="_blank" class="btn btn-view">
                        Ansehen
                    </a>
                </div>
            </div>

            <!-- PDFs zum Download -->
            <div class="download-card">
                <div class="icon">PDF</div>
                <div class="info">
                    <h2>Formular</h2>
                    <p>Ausfüllbares Antragsformular</p>
                    <span class="tag download">Download</span>
                </div>
                <div class="actions">
                    <a href="downloads/formular.pdf" class="btn btn-download">
                        Herunterladen
                    </a>
                </div>
            </div>

            <div class="download-card">
                <div class="icon">PDF</div>
                <div class="info">
                    <h2>Jahresbericht</h2>
                    <p>Geschäftsbericht 2024</p>
                    <span class="tag download">Download</span>
                </div>
                <div class="actions">
                    <a href="downloads/bericht.pdf" class="btn btn-download">
                        Herunterladen
                    </a>
                </div>
            </div>
        </div>

        <div class="info-box">
            <h3>Hinweis</h3>
            <p><strong>Ansicht im Browser:</strong> PDFs werden direkt im Browser-Fenster angezeigt.</p>
            <p><strong>Download:</strong> PDFs werden automatisch auf deinen Computer heruntergeladen.</p>
            <p><em>Hinweis: Das Verhalten kann je nach Browser variieren. Chrome zeigt PDFs oft im integrierten Viewer an.</em></p>
        </div>
    </div>
</body>
</html>
```

#### 7.6 CSS für Download-Seite

Erstelle `downloads.css` auf deinem PC:

```css
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #3a6186 0%, #89253e 100%);
    min-height: 100vh;
    padding: 20px;
}

.container {
    max-width: 900px;
    margin: 0 auto;
}

header {
    text-align: center;
    color: white;
    margin-bottom: 40px;
    padding: 40px 20px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

header h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

header p {
    font-size: 1.1em;
    opacity: 0.9;
}

.downloads {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.download-card {
    background: white;
    border-radius: 15px;
    padding: 30px;
    display: flex;
    align-items: center;
    gap: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    transition: transform 0.3s ease;
}

.download-card:hover {
    transform: translateX(10px);
}

.download-card .icon {
    font-size: 1.2em;
    font-weight: bold;
    min-width: 80px;
    height: 80px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 10px;
    text-align: center;
}

.download-card .info {
    flex: 1;
}

.download-card h2 {
    color: #333;
    margin-bottom: 8px;
}

.download-card p {
    color: #666;
    margin-bottom: 12px;
}

.tag {
    display: inline-block;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 0.85em;
    font-weight: 600;
}

.tag.view {
    background: #e3f2fd;
    color: #1976d2;
}

.tag.download {
    background: #fce4ec;
    color: #c2185b;
}

.btn {
    display: inline-block;
    padding: 12px 30px;
    border-radius: 25px;
    text-decoration: none;
    font-weight: bold;
    transition: all 0.3s ease;
}

.btn-view {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
}

.btn-view:hover {
    background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    transform: scale(1.05);
}

.btn-download {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
}

.btn-download:hover {
    background: linear-gradient(135deg, #f5576c 0%, #f093fb 100%);
    transform: scale(1.05);
}

.info-box {
    margin-top: 40px;
    background: rgba(255, 255, 255, 0.95);
    padding: 30px;
    border-radius: 15px;
    border-left: 5px solid #667eea;
}

.info-box h3 {
    color: #333;
    margin-bottom: 15px;
}

.info-box p {
    color: #666;
    line-height: 1.8;
    margin-bottom: 10px;
}

/* Responsive */
@media (max-width: 768px) {
    .download-card {
        flex-direction: column;
        text-align: center;
    }
    
    .download-card .icon {
        min-width: auto;
    }
    
    header h1 {
        font-size: 2em;
    }
}
```

#### 7.7 Dateien hochladen

1. Lade `downloads.html` in den Ordner `public/` hoch
2. Lade `downloads.css` in den Ordner `public/` hoch

#### 7.8 Bucket Policy prüfen

Stelle sicher, dass deine Policy `/public/*` abdeckt:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadForPublicFolder",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::DEIN-BUCKET-NAME/public/*"
        }
    ]
}
```

#### 7.9 Testen

1. Öffne: `http://dein-bucket.s3-website.eu-central-1.amazonaws.com/public/downloads.html`

2. **Teste das Verhalten:**
   - Klicke auf "Ansehen" bei der Anleitung
     - **Erwartet:** PDF öffnet sich im Browser-Tab
   - Klicke auf "Herunterladen" bei Formular
     - **Erwartet:** Download startet (Browser-abhängig)
   - Klicke auf "Herunterladen" bei Bericht
     - **Erwartet:** Download startet (Browser-abhängig)

### Ergebnis-Check

- [ ] Die Download-Seite wird korrekt angezeigt
- [ ] Ein PDF zeigt unterschiedliches Verhalten (inline vs. download)
- [ ] Du verstehst den Unterschied zwischen inline und attachment
- [ ] Die Metadaten sind korrekt gesetzt

### Troubleshooting

**Problem: Alle PDFs werden heruntergeladen**
- Prüfe, ob `anleitung.pdf` die `Content-Disposition` Metadata **nicht** hat
- Standardverhalten sollte inline sein

**Problem: PDFs werden angezeigt statt heruntergeladen**
- Prüfe die `Content-Disposition` Metadaten bei formular.pdf und bericht.pdf
- Stelle sicher, dass der Wert exakt `attachment; filename="dateiname.pdf"` ist
- Beachte: Chrome/Edge zeigen PDFs oft im integrierten Viewer - teste in Firefox

---

## Übung 8: Redirects konfigurieren

### Lernziel
Du lernst, wie du Weiterleitungen in S3 konfigurierst, um alte URLs umzuleiten oder eine saubere URL-Struktur zu schaffen.

### Hintergrundwissen

**Redirects** sind Weiterleitungen von einer URL zu einer anderen. Typische Anwendungsfälle:

- Alte URLs umleiten nach Website-Redesign
- Von `alt.html` zu `neu.html` weiterleiten
- Kurze URLs zu langen URLs (z.B. `/info` zu `/about.html`)
- 404-Fehler zu einer benutzerfreundlichen Seite umleiten

**Redirect-Typen:**
- **301 (Permanent):** "Diese Seite ist dauerhaft umgezogen" - gut für SEO
- **302 (Temporary):** "Diese Seite ist vorübergehend woanders"

**Wie funktioniert es in S3?**
S3 Static Website Hosting unterstützt Redirect Rules im **XML-Format** (nicht JSON!).

**Wichtig:** Redirects funktionieren nur über die Website-Endpoint-URL:
- Funktioniert: `http://bucket.s3-website.region.amazonaws.com/`
- Funktioniert NICHT: `http://bucket.s3.region.amazonaws.com/`

### Aufgabe

Konfiguriere folgende Redirects:
1. `/alt.html` leitet zu `/about.html` weiter
2. Eine Custom 404-Fehlerseite für nicht existierende URLs

### Schritt-für-Schritt Anleitung

#### 8.1 Test-Seiten erstellen

Erstelle folgende Dateien auf deinem PC:

**alt.html** (wird als Redirect-Quelle dienen):
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Alte Seite</title>
</head>
<body>
    <h1>Diese Seite sollte nie sichtbar sein</h1>
    <p>Du solltest automatisch weitergeleitet werden zu "Über uns".</p>
</body>
</html>
```

**about.html** (Redirect-Ziel):
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Über uns</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: #f5f5f5;
        }
        .card {
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        h1 { color: #333; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Über uns</h1>
        <p>Willkommen auf unserer Über-Uns-Seite!</p>
        <p>Diese Seite wurde erfolgreich über einen 301-Redirect geladen.</p>
    </div>
</body>
</html>
```

**404-custom.html** (Custom Error-Seite):
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Seite nicht gefunden</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0;
        }
        .error-box {
            background: white;
            padding: 50px;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            max-width: 500px;
        }
        .error-box h1 {
            font-size: 6em;
            margin: 0;
            color: #667eea;
        }
        .error-box h2 {
            color: #333;
            margin: 20px 0;
        }
        .error-box p {
            color: #666;
            line-height: 1.6;
            margin-bottom: 30px;
        }
        .btn {
            display: inline-block;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 40px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: bold;
            transition: transform 0.3s ease;
        }
        .btn:hover {
            transform: scale(1.05);
        }
    </style>
</head>
<body>
    <div class="error-box">
        <h1>404</h1>
        <h2>Seite nicht gefunden</h2>
        <p>Die angeforderte Seite existiert leider nicht oder wurde verschoben.</p>
        <a href="index.html" class="btn">Zur Startseite</a>
    </div>
</body>
</html>
```

#### 8.2 Dateien hochladen

**Option A: In /public/ (empfohlen für einheitliche Struktur)**
1. Lade alle drei Dateien in den Ordner `public/` hoch:
   - `public/alt.html`
   - `public/about.html`
   - `public/404-custom.html`

**Option B: Im Root (wenn du das so möchtest)**
1. Lade die Dateien direkt in den Bucket-Root hoch

**Wichtig:** Beide Optionen funktionieren, aber achte darauf, dass die Dateien in deiner Bucket Policy öffentlich sind!

2. Stelle sicher, dass auch `index.html` existiert (aus dem ersten Tutorial)

#### 8.3 Custom Error Document konfigurieren

1. Gehe zu **"Properties"** Tab
2. Scrolle zu **"Static website hosting"**
3. Klicke **"Edit"**

4. Bei **"Index document"** sollte stehen: `index.html` (oder `public/index.html`)
5. Bei **"Error document"** trage ein:
   - Wenn in `/public/`: `public/404-custom.html`
   - Wenn im Root: `404-custom.html`

**Wichtig:** Der Pfad muss zum tatsächlichen Speicherort passen!

#### 8.4 Redirect Rules konfigurieren

**Wichtig:** S3 Redirect Rules verwenden **XML-Format**, nicht JSON!

1. Im gleichen "Static website hosting" Edit-Dialog
2. Scrolle zu **"Redirection rules - optional"**
3. Füge folgende XML-Regeln ein:

**Wenn Dateien in /public/ liegen:**
```xml
<RoutingRules>
    <RoutingRule>
        <Condition>
            <KeyPrefixEquals>public/alt.html</KeyPrefixEquals>
        </Condition>
        <Redirect>
            <ReplaceKeyWith>public/about.html</ReplaceKeyWith>
            <HttpRedirectCode>301</HttpRedirectCode>
        </Redirect>
    </RoutingRule>
</RoutingRules>
```

**Wenn Dateien im Root liegen:**
```xml
<RoutingRules>
    <RoutingRule>
        <Condition>
            <KeyPrefixEquals>alt.html</KeyPrefixEquals>
        </Condition>
        <Redirect>
            <ReplaceKeyWith>about.html</ReplaceKeyWith>
            <HttpRedirectCode>301</HttpRedirectCode>
        </Redirect>
    </RoutingRule>
</RoutingRules>
```

4. Klicke **"Save changes"**

**Was macht diese Regel?**
- Wenn jemand `alt.html` (bzw. `public/alt.html`) aufruft
- Wird er zu `about.html` (bzw. `public/about.html`) weitergeleitet
- Mit HTTP-Status-Code 301 (permanente Weiterleitung)

#### 8.5 Redirects testen

**Test-Checkliste:**
- [ ] Block Public Access ist deaktiviert
- [ ] Bucket Policy deckt die Dateien ab
- [ ] Static Website Hosting ist aktiviert
- [ ] XML-Syntax ist korrekt (keine Fehler beim Speichern)

**Test 1: alt.html Redirect**

1. Öffne:
   - Wenn in `/public/`: `http://dein-bucket.s3-website.eu-central-1.amazonaws.com/public/alt.html`
   - Wenn im Root: `http://dein-bucket.s3-website.eu-central-1.amazonaws.com/alt.html`

2. **Erwartet:** Du wirst automatisch zu `about.html` weitergeleitet

3. **Browser-Tools prüfen:**
   - Öffne F12 → Network-Tab
   - Lade die Seite neu
   - Klicke auf die Anfrage zu `alt.html`
   - Siehst du Status: **301 Moved Permanently**

**Cache-Hinweis:** Wenn der Redirect nicht funktioniert:
- Drücke **Strg + F5** für Hard Refresh
- Teste im Inkognito-Modus
- Prüfe, ob du die Website-Endpoint-URL verwendest (nicht die normale S3-URL)

**Test 2: 404 Custom Error**

1. Öffne eine nicht existierende URL:
```
http://dein-bucket.s3-website.eu-central-1.amazonaws.com/gibts-nicht.html
```

2. **Erwartet:** Du siehst die schöne Custom 404-Seite mit dem großen "404"

### Ergebnis-Check

- [ ] `alt.html` leitet zu `about.html` weiter (301)
- [ ] Nicht existierende Seiten zeigen die Custom 404-Seite
- [ ] Du verstehst die XML-Syntax für Redirects
- [ ] Du siehst den Redirect im Browser-Network-Tab

### Vertiefung: Erweiterte Redirect-Regeln

**Redirect mit Pfad-Präfix:**

Alle Seiten unter `/old/` nach `/new/` umleiten:

```xml
<RoutingRule>
    <Condition>
        <KeyPrefixEquals>old/</KeyPrefixEquals>
    </Condition>
    <Redirect>
        <ReplaceKeyPrefixWith>new/</ReplaceKeyPrefixWith>
        <HttpRedirectCode>301</HttpRedirectCode>
    </Redirect>
</RoutingRule>
```

**Redirect zu externer Domain:**

```xml
<RoutingRule>
    <Condition>
        <KeyPrefixEquals>extern</KeyPrefixEquals>
    </Condition>
    <Redirect>
        <HostName>www.example.com</HostName>
        <Protocol>https</Protocol>
        <HttpRedirectCode>302</HttpRedirectCode>
    </Redirect>
</RoutingRule>
```

**Mehrere Redirect Rules kombinieren:**

```xml
<RoutingRules>
    <RoutingRule>
        <!-- Regel 1: alt.html → about.html -->
        <Condition>
            <KeyPrefixEquals>alt.html</KeyPrefixEquals>
        </Condition>
        <Redirect>
            <ReplaceKeyWith>about.html</ReplaceKeyWith>
            <HttpRedirectCode>301</HttpRedirectCode>
        </Redirect>
    </RoutingRule>
    <RoutingRule>
        <!-- Regel 2: /old/ → /new/ -->
        <Condition>
            <KeyPrefixEquals>old/</KeyPrefixEquals>
        </Condition>
        <Redirect>
            <ReplaceKeyPrefixWith>new/</ReplaceKeyPrefixWith>
            <HttpRedirectCode>301</HttpRedirectCode>
        </Redirect>
    </RoutingRule>
</RoutingRules>
```

### Wichtige Hinweise zu Redirects

**Format beachten:**
- S3 nutzt **XML** für Redirect Rules, nicht JSON
- Die Struktur muss exakt stimmen
- Nutze einen XML-Validator bei Problemen (z.B. xmlvalidation.com)

**Nur Website Endpoint:**
- Redirects funktionieren nur über die Website-Endpoint-URL:
  - Funktioniert: `http://bucket.s3-website.region.amazonaws.com/`
  - Funktioniert NICHT: `http://bucket.s3.region.amazonaws.com/`

**Testing:**
- Nutze den Browser-Network-Tab (F12) um Redirects zu sehen
- Teste im Inkognito-Modus um Cache-Probleme zu vermeiden
- Drücke Strg + F5 für Hard Refresh

**Cache-Control beim Testen:**
Wenn du viele Änderungen an Redirects machst:
- Setze testweise Cache-Control: no-cache als Metadatum
- Oder arbeite konsequent im Inkognito-Modus

### Redirect Best Practices

1. **301 für permanente Änderungen:** Suchmaschinen übertragen das Ranking
2. **302 für temporäre Änderungen:** Alte URL bleibt relevant
3. **Redirect-Chains vermeiden:** Nicht A → B → C, sondern direkt A → C
4. **Dokumentation:** Halte eine Liste aller Redirects
5. **Testing:** Teste alle Redirects nach Änderungen

---

## Zusammenfassung

### Was du gelernt hast

**Level 1: Grundlagen**
- Wie S3 mit "Ordnern" umgeht (Keys mit `/`)
- Objekte kopieren, löschen (kein echtes Verschieben, intern Copy + Delete)
- Metadaten und Content-Type verstehen und ändern

**Level 2: Sicherheit**
- Block Public Access deaktivieren (Voraussetzung für öffentliche Policies)
- Unterschied zwischen privaten und öffentlichen Dateien
- Bucket Policies mit Pfad-Präfixen schreiben
- Best Practices für Zugriffskontrolle

**Level 3: Projekte**
- Responsive Bildergalerie mit S3-Assets erstellen
- Download-Seite mit PDF-Handling (inline vs. attachment)
- Redirects (XML-Format!) und Custom Error-Pages konfigurieren
- /public/* Ordnerstruktur für saubere Policies

---

## Nächste Schritte

Du bist jetzt bereit für fortgeschrittenere Themen:

**Performance:**
- CloudFront CDN für schnellere Auslieferung weltweit
- CloudFront für HTTPS (Website-Endpoint bietet nur HTTP)
- Image-Optimierung (WebP, responsive images)
- Browser-Caching mit Cache-Control konfigurieren

**Erweiterte Sicherheit:**
- IAM-Policies für granulare Bucket-Zugriffe
- S3 Versioning aktivieren (Wiederherstellung von Dateien)
- Server-Side Encryption (SSE)

**Custom Domain:**
- Eigene Domain mit Route 53 verbinden
- SSL/TLS-Zertifikat mit Certificate Manager
- HTTPS für deine S3-Website über CloudFront

**Professionelle Features:**
- S3 Lifecycle Policies (automatisches Archivieren)
- S3 Event Notifications (Lambda-Trigger)
- Cross-Region Replication

---

## Häufige Probleme und Lösungen

### Problem: "Access Denied" trotz öffentlicher Policy

**Lösung:**
1. **Prüfe Block Public Access:** Permissions → Block public access settings
   - "Block all public access" muss **deaktiviert** sein
2. Bucket Policy Syntax überprüfen:
   - Kommas, Klammern korrekt?
   - ARN stimmt mit Bucket-Namen überein?
   - Resource-Pfad passt zum Objekt-Key?
3. Teste URL im Inkognito-Modus
4. Verwende die richtige URL (Object URL, nicht S3 URI)

### Problem: Redirects funktionieren nicht

**Lösung:**
1. Prüfe, ob "Static Website Hosting" aktiviert ist
2. **Nutze die Website-Endpoint-URL**, nicht die normale S3-URL
   - Richtig: `http://bucket.s3-website.region.amazonaws.com/`
   - Falsch: `http://bucket.s3.region.amazonaws.com/`
3. XML-Syntax mit einem Validator prüfen (z.B. xmlvalidation.com)
4. Browser-Cache leeren (Strg + F5) oder Inkognito-Modus nutzen
5. Prüfe, ob die Keys in den Redirect Rules mit den tatsächlichen Datei-Pfaden übereinstimmen

### Problem: Bilder werden nicht angezeigt

**Lösung:**
1. Prüfe Pfade (Groß-/Kleinschreibung beachten!)
2. Stelle sicher, dass Bilder in der Bucket Policy öffentlich sind
3. Browser-Cache leeren (Strg + F5)
4. Object URL direkt im Browser testen
5. Browser-Konsole öffnen (F12) - zeigt Ladefehler an

### Problem: CSS/JS wird nicht geladen

**Lösung:**
1. Prüfe Content-Type der Dateien (Properties → Metadata)
   - CSS sollte `text/css` sein
   - JS sollte `application/javascript` sein
2. Relative Pfade in HTML nutzen (nicht absolute mit `/`)
3. Browser-Konsole (F12) zeigt Fehler an
4. Hard Refresh (Strg + F5)

### Problem: PDFs laden nicht herunter

**Lösung:**
1. Prüfe `Content-Disposition` Metadaten (Properties → Metadata)
2. Stelle sicher, dass der Wert `attachment; filename="dateiname.pdf"` enthält
3. Browser-Verhalten kann variieren:
   - Chrome/Edge zeigen PDFs oft im integrierten Viewer
   - Firefox respektiert `attachment` besser
4. Teste in verschiedenen Browsern

### Problem: Änderungen sind nicht sichtbar

**Ursache:** Browser-Cache oder CloudFront-Cache (falls verwendet)

**Lösung:**
1. **Hard Refresh:** Strg + Shift + R (Windows) oder Cmd + Shift + R (Mac)
2. Öffne die Seite im **Inkognito-Modus**
3. Lösche den Browser-Cache komplett
4. Setze testweise Cache-Control: no-cache als Metadatum
5. Warte 1-2 Minuten (S3 Eventual Consistency)

---

## Test-Checkliste für öffentliche Inhalte

Verwende diese Checkliste **vor jedem Test** von öffentlichen Inhalten:

**Bucket-Einstellungen:**
- [ ] Permissions → Block public access: **deaktiviert**
- [ ] Bucket policy gespeichert und JSON valide
- [ ] Resource-ARN stimmt mit Bucket-Namen überein

**Static Website Hosting:**
- [ ] Static website hosting: **aktiviert**
- [ ] Index document gesetzt
- [ ] Error document gesetzt (optional)
- [ ] Website-Endpoint-URL notiert

**Testing:**
- [ ] Test im **Inkognito-Fenster**
- [ ] Verwende **Website-Endpoint-URL** (für Redirects)
- [ ] Browser-Cache geleert (**Strg + F5**)
- [ ] Browser-Konsole geöffnet (F12) um Fehler zu sehen

---

## Cache-Management beim Entwickeln

**Problem:** Änderungen an HTML/CSS/JS sind oft nicht sofort sichtbar.

**Lösungen während der Entwicklung:**

1. **Browser-Cache umgehen:**
   - Hard Refresh: Strg + F5 (Windows) / Cmd + Shift + R (Mac)
   - Inkognito-Modus verwenden

2. **S3 Cache-Control setzen:**
   - Während Entwicklung: `Cache-Control: no-cache, no-store, must-revalidate`
   - Für Produktion: `Cache-Control: public, max-age=31536000` (1 Jahr)

3. **So setzt du Cache-Control:**
   - Wähle Dateien aus
   - Actions → Edit metadata
   - Add metadata → Cache-Control
   - Value: `no-cache` (zum Testen) oder `public, max-age=31536000` (Produktion)

---

## Ressourcen und Links

**AWS-Dokumentation:**
- [S3 Static Website Hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
- [S3 Redirect Rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-page-redirect.html)
- [S3 Bucket Policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html)

**Tools:**
- [JSON Validator](https://jsonlint.com/) - Prüfe deine Bucket Policies
- [XML Validator](https://www.xmlvalidation.com/) - Prüfe Redirect Rules
- [Unsplash](https://unsplash.com/) - Kostenlose Bilder für Projekte

---

**Glückwunsch! Du hast alle Übungen abgeschlossen!**

Bei Fragen oder Problemen kannst du jederzeit nachfragen. Viel Erfolg mit deinen eigenen S3-Projekten!
