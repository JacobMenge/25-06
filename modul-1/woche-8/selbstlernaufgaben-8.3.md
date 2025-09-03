# Selbstlernaufgaben - Webserver-Grundlagen

Bitte lade deine Ergebnisse bis spätestens **Sonntag um 23:59 Uhr im Google Classroom** zur entsprechenden Aufgabe hoch.

---

## 1. Grundlagenaufgabe - Webserver verstehen

**Deine Aufgabe:**

Beantworte folgende Fragen in **deinen eigenen Worten**:

1. **Webserver-Grundlagen:**
   - Was ist ein Webserver und welche Aufgabe hat er?
   - Beschreibe in 4-5 Stichpunkten, was passiert, wenn du `http://example.com/index.html` aufrufst

2. **Webserver-Aufgaben:**
   Ordne folgende Aufgaben einem Webserver zu (Ja/Nein):
   - HTTP-Requests empfangen: ___
   - E-Mails versenden: ___
   - 404-Fehler anzeigen: ___
   - Dateien aus DocumentRoot laden: ___
   - Excel-Tabellen erstellen: ___

**Formatvorschläge:**
- Kurze, präzise Antworten in Stichpunkten
- PDF oder Word-Dokument

---

## 2. Grundlagenaufgabe - Webserver-Software vergleichen

**Deine Aufgabe:**

Erstelle eine **Vergleichstabelle** mit folgenden Informationen:

| Eigenschaft | Apache | Nginx | IIS |
|------------|---------|-------|-----|
| Entwickelt seit | | | |
| Marktanteil (ca.) | | | |
| Betriebssystem | | | |
| Kosten | | | |
| Hauptstärke | | | |
| Hauptschwäche | | | |

**Entscheidungshilfe:**
Für welchen Webserver würdest du dich in folgenden Szenarien entscheiden? Begründe kurz:

1. **Startup mit hohem Traffic:** Viele Besucher, hauptsächlich statische Inhalte, wenig Budget
   - Wahl: _____ 
   - Begründung: _____

2. **Traditionelles Unternehmen:** Windows-Umgebung, .NET-Anwendungen, IT-Team kennt Microsoft-Produkte
   - Wahl: _____ 
   - Begründung: _____

3. **WordPress-Blog:** PHP-basierte Website, mittlerer Traffic, viele Plugins nötig
   - Wahl: _____ 
   - Begründung: _____

**Formatvorschläge:**
- Tabelle + Begründungen in einem Dokument
- Übersichtliche Struktur mit klaren Antworten

---

## 3. Vertiefungsaufgabe - DocumentRoot verstehen

**Deine Aufgabe:**

**Teil A: URL-zu-Pfad-Mapping**

Gegeben ist ein Webserver mit DocumentRoot: `/var/www/html/`

Vervollständige die Zuordnung:

| URL | Dateipfad auf Server |
|-----|---------------------|
| `http://meinshop.de/` | |
| `http://meinshop.de/produkte.html` | |
| `http://meinshop.de/bilder/logo.png` | |
| `http://meinshop.de/css/style.css` | |
| `http://meinshop.de/kontakt/formular.php` | |

**Teil B: Dateistruktur erstellen**

Zeichne/schreibe die Ordnerstruktur für eine Website mit folgenden URLs:
- `http://beispiel.de/` (Startseite)
- `http://beispiel.de/ueber-uns.html`
- `http://beispiel.de/produkte/kategorie1.html`
- `http://beispiel.de/bilder/header.jpg`
- `http://beispiel.de/downloads/katalog.pdf`

**Teil C: Berechtigungen**

1. Welcher Linux-User sollte Dateien im DocumentRoot besitzen?
2. Welche Berechtigungen (rwx) sollten HTML-Dateien haben?
3. Was passiert, wenn der Webserver-User keine Leserechte auf eine Datei hat?

**Formatvorschläge:**
- Tabellen für URL-Mapping
- Baumstruktur oder Ordnerliste für Dateistruktur
- Kurze Antworten für Berechtigungen

---

## 4. Anwendungsaufgabe - Fehleranalyse und Problemlösung

**Deine Aufgabe:**

Analysiere folgende **Probleme** und finde Lösungen:

**Problem 1: 404 Not Found**
- URL: `http://meinefirma.de/impressum.html`
- DocumentRoot: `/var/www/html/`
- Datei existiert als: `/var/www/html/impressum.htm` (ohne 'l')
- Was ist das Problem? Wie löst man es?

**Problem 2: Keine Berechtigung**
- Datei: `/var/www/html/index.html` 
- Berechtigung: `-rw------- 1 root root index.html`
- Webserver läuft als User: `www-data`
- Was ist das Problem? Wie löst man es?


**Formatvorschläge:**
- Pro Problem: Problemanalyse + Lösungsvorschlag
- Strukturierte Antworten mit Begründung

---

# Bonus-Aufgabe - Apache Webserver installieren und konfigurieren (freiwillig)

**Deine Aufgabe:**

Installiere und konfiguriere einen echten Apache-Webserver auf deinem System. Diese Aufgabe ist herausfordernd, aber sehr lehrreich!

**⚠️ WICHTIGE SICHERHEITSHINWEISE:**
- Diese Aufgabe ist **NUR für Lernzwecke** gedacht
- Verwende **keine echten persönlichen Daten**
- **Öffne den Server NICHT für das Internet** (nur localhost verwenden)
- **Stoppe Apache nach den Experimenten** (siehe Teil G)

---

## **Teil A: Apache installieren (Schritt-für-Schritt)**

### **Für Ubuntu/Debian (Linux):**

**Schritt 1: System aktualisieren**
```bash
sudo apt update
```

**Schritt 2: Apache installieren**
```bash
sudo apt install apache2 -y
```

**Schritt 3: Apache starten**
```bash
# Apache starten
sudo systemctl start apache2

# Status prüfen (sollte "active" zeigen)
sudo systemctl status apache2
```

**Schritt 4: Test im Browser**
- Öffne: `http://localhost`
- Du solltest "Apache2 Ubuntu Default Page" sehen

### **Für Windows:**

**Schritt 1: XAMPP herunterladen**
- Gehe zu https://www.apachefriends.org/
- Lade XAMPP für Windows herunter (aktuelle Version)
- Installiere XAMPP (alle Komponenten außer Apache können abgewählt werden)

**Schritt 2: XAMPP Control Panel starten**
- Starte XAMPP Control Panel **als Administrator**
- Klicke "Start" bei Apache
- Status sollte grün werden

**Schritt 3: Test im Browser**
- Öffne: `http://localhost`
- Du solltest die XAMPP-Willkommensseite sehen

---

## **Teil B: Deine erste eigene Webseite**

### **DocumentRoot-Verzeichnis finden:**

**Linux:** `/var/www/html/`
**Windows:** `C:\xampp\htdocs\`

### **Einfache Webseite erstellen:**

**Linux:**
```bash
# In DocumentRoot wechseln
cd /var/www/html/

# Neue index.html erstellen (überschreibt die Standard-Seite)
sudo nano index.html
```

**Windows:**
- Navigiere zu `C:\xampp\htdocs\`
- Öffne `index.html` mit Notepad++ oder einem anderen Editor

**Inhalt für index.html (kopiere das komplett rein):**
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Mein Apache Server</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 50px auto; 
            padding: 20px;
            background-color: #f8f9fa;
        }
        .header { 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white; 
            padding: 30px; 
            border-radius: 10px; 
            text-align: center;
            margin-bottom: 30px;
        }
        .info-box { 
            background: white; 
            padding: 25px; 
            border-radius: 8px; 
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }
        .nav-list { 
            list-style: none; 
            padding: 0; 
        }
        .nav-list li { 
            margin: 10px 0; 
        }
        .nav-list a { 
            color: #667eea; 
            text-decoration: none; 
            font-weight: bold;
        }
        .nav-list a:hover { 
            text-decoration: underline; 
        }
    </style>
</head>
<body>
    <div class="header">
        <h1> Mein Apache Server läuft!</h1>
        <p>Herzlichen Glückwunsch - du hast Apache erfolgreich installiert!</p>
    </div>
    
    <div class="info-box">
        <h2>Server-Informationen</h2>
        <p><strong>Server:</strong> Apache Webserver</p>
        <p><strong>Aktuelles Datum:</strong> <span id="datum"></span></p>
        <p><strong>Status:</strong> Online und funktionsfähig </p>
    </div>
    
    <div class="info-box">
        <h2>Test-Navigation</h2>
        <ul class="nav-list">
            <li><a href="/">Startseite (diese Seite)</a></li>
            <li><a href="/about.html">Über-uns Seite (erstelle als nächstes)</a></li>
            <li><a href="/test/">Test-Verzeichnis</a></li>
        </ul>
    </div>
    
    <script>
        document.getElementById('datum').textContent = new Date().toLocaleString('de-DE');
    </script>
</body>
</html>
```

**Test:** Lade `http://localhost` neu - du solltest jetzt deine eigene Seite sehen!

---

## **Teil C: Weitere Seiten und Struktur erstellen**

### **Schritt 1: About-Seite erstellen**

**Linux:**
```bash
sudo nano /var/www/html/about.html
```

**Windows:**
- Erstelle neue Datei `C:\xampp\htdocs\about.html`

**Inhalt für about.html:**
```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <title>Über uns - Mein Apache Server</title>
</head>
<body style="font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px;">
    <h1>Über diesen Server</h1>
    <p>Dies ist eine Testseite für meinen Apache-Webserver.</p>
    <p>Hier lerne ich, wie Webserver funktionieren!</p>
    <p><a href="/" style="color: #667eea;">&larr; Zurück zur Startseite</a></p>
</body>
</html>
```

### **Schritt 2: Test-Verzeichnis erstellen**

**Linux:**
```bash
# Verzeichnis erstellen
sudo mkdir /var/www/html/test

# Testdateien erstellen
echo "Das ist eine Textdatei" | sudo tee /var/www/html/test/readme.txt
echo "Weitere Testdatei" | sudo tee /var/www/html/test/info.txt
```

**Windows:**
- Erstelle Ordner `C:\xampp\htdocs\test\`
- Erstelle dort zwei Textdateien: `readme.txt` und `info.txt` mit beliebigem Inhalt

### **Tests durchführen:**
- `http://localhost/about.html` → sollte deine About-Seite zeigen
- `http://localhost/test/` → sollte Dateiliste oder Fehler zeigen
- `http://localhost/test/readme.txt` → sollte Textinhalt zeigen

---

## **Teil D: Apache verstehen - Logs und Konfiguration**

### **Apache-Logs anschauen:**

**Linux:**
```bash
# Wer hat was aufgerufen? (Access Log)
sudo tail -10 /var/log/apache2/access.log

# Gab es Fehler? (Error Log)
sudo tail -10 /var/log/apache2/error.log
```

**Windows (XAMPP):**
- Access Log: `C:\xampp\apache\logs\access.log`
- Error Log: `C:\xampp\apache\logs\error.log`
- Öffne diese Dateien mit Notepad

**Was bedeuten die Log-Einträge?**
```
127.0.0.1 - - [03/Sep/2025:15:30:45 +0200] "GET / HTTP/1.1" 200 1234
```
- `127.0.0.1` = IP-Adresse des Besuchers (localhost)
- `GET /` = HTTP-Request für die Startseite
- `200` = Status-Code (200 = OK, 404 = Not Found)
- `1234` = Größe der ausgelieferten Datei in Bytes

### **Wichtige Apache-Konfiguration finden:**

**Linux:**
```bash
# Haupt-Konfigurationsdatei anzeigen
sudo grep -n "DocumentRoot\|Listen\|ServerName" /etc/apache2/sites-enabled/000-default.conf
```

**Windows (XAMPP):**
- Öffne: `C:\xampp\apache\conf\httpd.conf`
- Suche nach diesen Zeilen:
  - `Listen 80` → Apache hört auf Port 80
  - `DocumentRoot "C:/xampp/htdocs"` → Hier liegen die Website-Dateien
  - `ServerName localhost:80` → Server-Name

---

## **Teil E: Experimente und Tests**

### **Experiment 1: 404-Fehler provozieren**
1. Rufe `http://localhost/existiert-nicht.html` auf
2. Was siehst du? → Apache-Fehlerseite
3. Schaue ins Error Log - wurde der Fehler protokolliert?

### **Experiment 2: Verschiedene Dateitypen testen**
Erstelle verschiedene Dateien und teste sie:

**Linux:**
```bash
# PDF-ähnliche Datei (nur zum Testen)
echo "Das ist eine Test-PDF" | sudo tee /var/www/html/test.pdf

# Bild-Datei (nur Text, aber mit .jpg-Endung)
echo "Fake JPG content" | sudo tee /var/www/html/bild.jpg
```

**Tests:**
- `http://localhost/test.pdf` → Was passiert? Download oder Anzeige?
- `http://localhost/bild.jpg` → Wie reagiert der Browser?

### **Experiment 3: Berechtigungen testen (nur Linux)**
```bash
# Datei mit falschen Berechtigungen erstellen
echo "Geheimer Inhalt" | sudo tee /var/www/html/geheim.html
sudo chmod 000 /var/www/html/geheim.html

# Test: http://localhost/geheim.html
# Erwartung: 403 Forbidden Error

# Reparieren:
sudo chmod 644 /var/www/html/geheim.html
```

---

## **Teil F: Reflexion und Dokumentation**

Beantworte diese Fragen nach deinen Experimenten (es reicht auch, wenn du nur darüber nachdenkst und nicht alles dokumentierst):

### **1. Installation und Setup:**
- Welches System hast du verwendet? (Linux/Windows)
- Welche Schritte waren nötig?
- Gab es Probleme oder Fehlermeldungen?

### **2. DocumentRoot-Verständnis:**
- Wo ist dein DocumentRoot-Verzeichnis?
- Teste: `http://localhost/test/readme.txt` → welcher Dateipfad auf dem Server?
- Was passiert, wenn eine Datei nicht existiert?

### **3. Apache-Verhalten:**
- Welche HTTP-Status-Codes hast du gesehen? (200, 404, 403?)
- Was steht in den Apache-Logs nach deinen Tests?
- Wie schnell lädt Apache deine Seiten?

### **4. Sicherheitsaspekte:**
- Was passiert bei falschen Dateiberechtigungen?
- Werden alle Dateien im DocumentRoot öffentlich zugänglich?
- Warum sollte man Apache nicht dauerhaft laufen lassen?

---

## **Teil G: Aufräumen (wichtig!)**

**Apache stoppen:**

**Linux:**
```bash
sudo systemctl stop apache2
# Prüfen: sudo systemctl status apache2 → sollte "inactive" zeigen
```

**Windows:**
- XAMPP Control Panel → "Stop" bei Apache klicken

**Komplett deinstallieren (optional):**

**Linux:**
```bash
sudo apt remove apache2 -y
sudo apt autoremove -y
```

**Windows:**
- XAMPP über Windows-Systemsteuerung deinstallieren

---

## **Häufige Probleme und Lösungen**

### **Problem: "Port 80 is already in use"**
**Ursache:** Ein anderer Webserver läuft bereits

**Lösung Linux:**
```bash
# Prüfen, was Port 80 verwendet
sudo lsof -i :80
# Falls ein anderer Service läuft, stoppen oder anderen Port verwenden
```

**Lösung Windows:**
- IIS (Internet Information Services) deaktivieren
- Oder in XAMPP einen anderen Port verwenden (z.B. 8080)

### **Problem: "Permission denied" (Linux)**
**Ursache:** Falsche Dateiberechtigungen

**Lösung:**
```bash
sudo chown -R www-data:www-data /var/www/html/
sudo chmod -R 644 /var/www/html/*.html
```

### **Problem: Apache startet nicht (Linux)**
**Diagnose:**
```bash
sudo systemctl status apache2
sudo journalctl -u apache2 --no-pager --lines 20
```

### **Problem: XAMPP startet nicht (Windows)**
**Lösungen:**
- XAMPP als Administrator starten
- Antivirus-Software temporär deaktivieren
- Windows Firewall-Einstellungen prüfen

---

**Formatvorschläge für deine Dokumentation:**
- Screenshots der wichtigsten Schritte zb das was im browser angezeigt wird
