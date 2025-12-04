# Tag 4: Deployment auf AWS EC2 + Logging

> **Wichtig:** Wir nutzen die Techstarter AWS Sandbox unter https://sandboxes.techstarter.de/ mit einem Budget-Limit von 15€. Alle Ressourcen sollten am Ende aufgeräumt werden!

## Lernziele

**Kernziele (Pflicht):**
* Eine EC2-Instanz in AWS erstellen und konfigurieren
* FastAPI-Anwendung auf einem Linux-Server deployen
* Systemd Service für automatisches Starten einrichten
* Nginx als Reverse Proxy konfigurieren
* API öffentlich über HTTP erreichbar machen

**Bonus-Ziele (Optional):**
* Log-Dateien strukturiert erstellen und verwalten
* Cronjob für automatische S3-Uploads einrichten
* HTTPS mit Let's Encrypt aktivieren
* Monitoring und Backups implementieren

---

## Theorie: Was ist AWS EC2?

### Cloud Computing - Grundlagen

**Was ist Cloud Computing?**

Statt einen physischen Server zu kaufen und in deinem Büro zu betreiben, mietest du Rechenleistung von einem Cloud-Anbieter wie AWS.

**Metapher: Server mieten wie eine Wohnung**
* **Früher (eigener Server):** Du kaufst ein Haus → Hohe Anfangskosten, du kümmerst dich um alles
* **Heute (Cloud):** Du mietest eine Wohnung → Bezahlst nur was du nutzt, Wartung übernimmt der Vermieter

### Was ist EC2?

**EC2 = Elastic Compute Cloud**

EC2 ist der AWS-Service für virtuelle Server (genannt "Instanzen").

**Elastic = Flexibel:**
* Starte Server in Minuten
* Skaliere hoch oder runter je nach Bedarf
* Bezahle nur für die tatsächliche Nutzung

**Was ist eine EC2-Instanz?**
Eine EC2-Instanz ist ein virtueller Computer in der Cloud:
* Hat CPU, RAM, Festplatte (wie ein normaler Computer)
* Läuft auf AWS-Hardware (die du nicht siehst)
* Du hast volle Admin-Rechte über `sudo` (Root-Rechte bei Bedarf)
* Du kannst darauf installieren was du willst

### EC2-Instanz-Typen

AWS bietet verschiedene Instanz-Typen für verschiedene Zwecke:

**t2.micro / t3.micro (Free Tier eligible):**
* 1-2 vCPUs (virtuelle CPUs)
* 1 GB RAM
* Perfekt für kleine Projekte und Lernen
* Im Free Tier je nach Account-Typ kostenlos/rabattiert

**t3.small (kleine Produktion):**
* 2 vCPUs
* 2 GB RAM
* Ca. 15-20€/Monat
* Gut für kleine APIs mit moderatem Traffic

**Für unser Projekt:** Wähle eine Instanz, die in der AWS-Konsole als **"Free tier eligible"** markiert ist (meist t2.micro oder t3.micro)!

### AWS-Regionen

AWS hat Rechenzentren auf der ganzen Welt verteilt (Regionen):

* **eu-central-1** → Frankfurt (Deutschland)
* **eu-west-1** → Irland
* **us-east-1** → Virginia (USA)

**Wichtig:** Wähle eine Region in deiner Nähe für niedrige Latenz!

### Warum EC2 für unsere API?

**Vorteile:**
* Immer verfügbar (24/7)
* Feste IP-Adresse
* Echte Linux-Umgebung
* Professionelles Setup
* Du lernst Production-Deployment

**Nachteile:**
* Kostet Geld (aber Free Tier für 12 Monate)
* Mehr Konfiguration als lokaler Server
* Du musst dich um Updates kümmern

---

## Theorie: Deployment-Architektur

### Wie sieht unsere finale Architektur aus?

```
Internet
   │
   ↓
[AWS Security Group]  ← Firewall
   │
   ↓
[Nginx :80]          ← Reverse Proxy (öffentlich)
   │
   ↓
[FastAPI :8000]      ← Unsere API (intern)
   │
   ↓
[SQLite DB]          ← Datenbank (lokal)
   │
   ↓
[Log-Dateien]        ← Logs
   │
   ↓ (Cronjob)
[S3 Bucket]          ← Log-Archiv
```

**Erklärung der Komponenten:**

**1. Security Group (AWS-Firewall):**
* Kontrolliert welche Ports von außen erreichbar sind
* Wir öffnen nur Port 80 (HTTP) und 22 (SSH)
* Alles andere ist blockiert

**2. Nginx (Reverse Proxy):**
* Nimmt HTTP-Anfragen von außen entgegen (Port 80)
* Leitet sie intern an FastAPI weiter (Port 8000)
* Warum? Nginx ist robuster, kann SSL, Load Balancing, Static Files
* FastAPI läuft nur intern (nicht direkt erreichbar von außen)

**3. FastAPI (unsere Anwendung):**
* Läuft mit Uvicorn auf Port 8000
* Nur von localhost erreichbar
* Managed von Systemd (automatischer Start bei Neustart)

**4. SQLite:**
* Lokale Datenbank-Datei
* Liegt im gleichen Verzeichnis wie die Anwendung

**5. Logs + S3:**
* Logs werden in `/var/log/notes-api/` gespeichert
* Täglich per Cronjob zu S3 hochgeladen
* Alte Logs werden komprimiert

### Warum Nginx statt direkt FastAPI?

**Problem mit direktem FastAPI:**
```
Internet → FastAPI :8000
```

**Nachteile:**
* Port 8000 muss öffentlich sein (unüblich)
* Keine SSL-Unterstützung
* Keine Load Balancing-Möglichkeit
* Keine Static Files (CSS, JS, Bilder)
* Weniger robust bei vielen Anfragen

**Lösung mit Nginx:**
```
Internet → Nginx :80 → FastAPI :8000 (localhost)
```

**Vorteile:**
* Standard Port 80 (HTTP) / 443 (HTTPS)
* SSL/TLS-Terminierung
* Kann mehrere FastAPI-Instanzen verwalten
* Serve Static Files effizient
* Bessere Performance
* Professioneller Standard

**Metapher:** Nginx ist wie ein Empfangschef im Restaurant:
* Nimmt Gäste (Requests) in Empfang
* Leitet sie an den richtigen Koch (FastAPI) weiter
* Der Koch muss nicht mit jedem Gast direkt sprechen

---

## Theorie: Systemd Service

### Was ist Systemd?

Systemd ist der Service-Manager in modernen Linux-Systemen (Ubuntu, Debian, CentOS, etc.).

**Was macht Systemd?**
* Startet Services beim Booten
* Überwacht laufende Services
* Startet Services neu, wenn sie abstürzen
* Verwaltet Logs

**Ohne Systemd:**
```bash
# Du musst manuell starten:
uvicorn main:app

# Server neu gestartet? API ist weg!
# SSH-Verbindung getrennt? API ist weg!
```

**Mit Systemd:**
```bash
# Service wird automatisch gestartet:
sudo systemctl start notes-api

# Bei Server-Neustart: Automatisch wieder da!
# SSH getrennt? Läuft weiter im Hintergrund!
```

### Systemd Unit File

Ein Systemd Service wird mit einem "Unit File" definiert:

```ini
[Unit]
Description=Notes API Service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/notes-api
ExecStart=/home/ubuntu/notes-api/venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

**Erklärung:**
* `[Unit]` → Allgemeine Infos über den Service
* `After=network.target` → Starte erst, wenn Netzwerk verfügbar ist
* `[Service]` → Wie der Service läuft
* `User=ubuntu` → Als welcher User (nicht root!)
* `WorkingDirectory` → Wo liegt die Anwendung
* `ExecStart` → Kommando zum Starten
* `--host 127.0.0.1` → Nur auf localhost hören (nicht von außen erreichbar)
* `--port 8000` → Interner Port für FastAPI
* `Restart=always` → Bei Crash automatisch neu starten
* `[Install]` → Wann beim Boot starten

---

## Theorie: SSH und Sicherheit

### Was ist SSH?

**SSH = Secure Shell**

SSH ist ein verschlüsseltes Protokoll, um sich sicher mit einem entfernten Server zu verbinden.

**Metapher:** SSH ist wie ein verschlüsselter Telefon-Tunnel zu deinem Server:
* Alles was du tippst, ist verschlüsselt
* Niemand kann mithören
* Du authentifizierst dich mit einem Schlüssel (nicht nur Passwort)

**SSH-Verbindung aufbauen:**
```bash
ssh -i mein-key.pem ubuntu@54.93.123.456
     ^              ^       ^
     |              |       └── IP-Adresse der EC2-Instanz
     |              └── Username (ubuntu ist Standard bei Ubuntu AMIs)
     └── Private Key (wie ein digitaler Haustürschlüssel)
```

**Wichtig zum Username:**
* Bei **Ubuntu AMIs** ist der Standard-User: `ubuntu`
* Bei Amazon Linux AMIs wäre es: `ec2-user`
* Bei Debian AMIs: `admin`
* Wir nutzen Ubuntu → daher: `ubuntu@...`

### SSH-Keys verstehen

**Asymmetrische Verschlüsselung:**

Beim Erstellen einer EC2-Instanz erzeugt AWS ein Schlüsselpaar:

1. **Private Key** (mein-key.pem)
   * Bleibt bei dir auf dem Laptop
   * Wie ein Haustürschlüssel
   * NIEMALS weitergeben!
   * Permissions: 400 (nur du kannst lesen)

2. **Public Key**
   * Liegt auf der EC2-Instanz
   * Wie ein Türschloss
   * Kann öffentlich sein

**Wie funktioniert es?**
```
Du (mit Private Key) → Server (mit Public Key)
                     ← "Beweise, dass du den Private Key hast!"
                     → [Mathematischer Beweis]
                     ← "OK, du bist authentifiziert!"
```

**Wichtig:**
* Private Key muss Permissions 400 haben:
  ```bash
  chmod 400 mein-key.pem
  ```
* Ohne diesen Key kommst du nicht auf den Server!

---

## Vorbereitung: AWS-Account und Kosten

### AWS Free Tier und Sandbox-Zugang

**Für diesen Kurs nutzen wir die Techstarter AWS Sandbox:**
* Zugang über: https://sandboxes.techstarter.de/
* Budget-Limit: 15€ pro Teilnehmer
* Alle Ressourcen sollten am Ende aufgeräumt werden

**AWS Free Tier (für eigene Accounts):**

AWS bietet ein kostenloses Kontingent für neue Accounts. Die genauen Konditionen hängen vom Account-Erstellungsdatum ab:

**Legacy Free Tier (Accounts vor Juli 2025):**
* 750 Stunden EC2 t2.micro/Monat (12 Monate)
* 5 GB S3 Storage
* 20.000 GET Requests (S3)

**Aktuelles Free Tier:**
* Variiert je nach AWS-Programm
* **Wichtig:** Prüfe im AWS Free Tier Dashboard die aktuellen Limits
* Achte in der EC2-Konsole auf das Label **"Free tier eligible"**

**Das bedeutet für uns:**
* Wähle immer eine Instanz mit "Free tier eligible" Label
* In der Sandbox: Achte auf das 15€-Budget
* Eine kleine Instanz (t2.micro/t3.micro) 24/7 laufen lassen ist normalerweise im Free Tier abgedeckt

**Nach Free Tier (oder außerhalb):**
* t2.micro: ~8-10€/Monat
* t3.micro: ~9-11€/Monat
* S3 Storage: ~0,023€/GB/Monat
* S3 Requests: Vernachlässigbar für kleine Projekte

**Kostenfallen vermeiden:**
* Nur **eine** kleine Instanz (t2/t3.micro)
* Instanz **stoppen** wenn nicht gebraucht (nicht terminate!)
* S3 Buckets regelmäßig aufräumen
* In der Sandbox: Am Ende des Tages alles aufräumen!

### AWS-Account erstellen

Wenn du noch keinen AWS-Account hast:

1. Gehe zu https://aws.amazon.com
2. Klicke auf "Kostenloses Konto erstellen"
3. Folge den Schritten (Kreditkarte erforderlich)
4. Wähle "Basic Support" (kostenlos)

**Sicherheitshinweis:**
* Aktiviere MFA (Multi-Factor Authentication)
* Erstelle einen IAM-User (nicht als Root arbeiten)

---

## Live-Coding Teil 1: EC2-Instanz erstellen

### Schritt 1: In die AWS Console einloggen

1. Öffne https://console.aws.amazon.com
2. Logge dich mit deinen Zugangsdaten ein
3. Wähle die Region **eu-central-1** (Frankfurt)
   * Oben rechts in der Navbar
   * Wichtig: Merke dir diese Region!

### Schritt 2: EC2 Dashboard öffnen

1. Suche nach "EC2" in der Suchleiste
2. Klicke auf "EC2" → Du siehst das EC2 Dashboard
3. Klicke auf **"Launch instance"** (großer oranger Button)

### Schritt 3: Instanz konfigurieren

**Name und Tags:**
```
Name: notes-api-server
```

**Application and OS Images (AMI):**
* Wähle: **Ubuntu Server 24.04 LTS**
* Architecture: **64-bit (x86)**
* Warum Ubuntu? Weit verbreitet, gut dokumentiert, stabil

**Instance Type:**
* Wähle: **t2.micro** oder **t3.micro** (je nachdem was als "Free tier eligible" markiert ist)
* Wichtig: Achte auf das Label **"Free tier eligible"**!
* Beide Typen haben 1 GB RAM und sind für unser Projekt perfekt

**Key Pair (Login):**
* Klicke auf **"Create new key pair"**
* Key pair name: `notes-api-key`
* Key pair type: **RSA**
* Private key format: **.pem** (für Linux/Mac) oder **.ppk** (für PuTTY/Windows)
* Klicke auf **"Create key pair"**
* Die Datei wird automatisch heruntergeladen
* **WICHTIG:** Diese Datei gut aufbewahren! Du kannst sie nicht nochmal herunterladen!

**Network Settings:**
* Klicke auf **"Edit"** (rechts oben)
* **Auto-assign public IP:** Enable (wichtig!)
* **Firewall (Security Groups):**
  * Wähle: **"Create security group"**
  * Security group name: `notes-api-sg`
  * Description: `Security group for notes API`
  
**Inbound Security Group Rules:**

Erstelle 2 Regeln:

**Regel 1: SSH**
* Type: **SSH**
* Port: **22**
* Source: **My IP** (nur deine IP kann sich verbinden)
* Description: `SSH from my IP`

**Regel 2: HTTP**
* Type: **HTTP**
* Port: **80**
* Source: **Anywhere (0.0.0.0/0)**
* Description: `HTTP access for API`

**Warum diese Regeln?**
* SSH (Port 22) → Damit du dich verbinden kannst
* HTTP (Port 80) → Damit die Welt deine API nutzen kann
* Port 8000? Nicht nötig! FastAPI läuft intern, Nginx ist das Gateway

**Configure Storage:**
* 8 GB gp3 (Standard) reicht völlig

### Schritt 4: Instanz starten

1. Klicke rechts auf **"Launch instance"**
2. Warte ca. 1-2 Minuten
3. Klicke auf **"View instances"**
4. Deine Instanz sollte jetzt Status **"Running"** haben

### Schritt 5: Public IP notieren

1. Klicke auf deine Instanz
2. Notiere die **Public IPv4 address**
   * Beispiel: `54.93.123.456`
   * Diese IP brauchst du zum Verbinden!

---

## Live-Coding Teil 2: SSH-Verbindung einrichten

### Schritt 1: Private Key vorbereiten

**Linux/Mac:**

```bash
# Wechsle in den Download-Ordner
cd ~/Downloads

# Verschiebe den Key in ein sicheres Verzeichnis
mkdir -p ~/.ssh
mv notes-api-key.pem ~/.ssh/

# Setze korrekte Permissions (wichtig!)
chmod 400 ~/.ssh/notes-api-key.pem

# Überprüfe die Permissions
ls -la ~/.ssh/notes-api-key.pem
# Sollte zeigen: -r-------- (nur Lesen für dich)
```

**Windows 10/11:**

Windows 10/11 hat OpenSSH meist schon vorinstalliert. Du kannst `.pem` Dateien direkt nutzen!

```powershell
# PowerShell oder CMD öffnen
# Wechsle zum Download-Ordner
cd Downloads

# Key sollte bereits die richtigen Permissions haben
# Wenn nicht, kannst du sie setzen (optional):
# icacls notes-api-key.pem /inheritance:r
# icacls notes-api-key.pem /grant:r "%USERNAME%:R"

# SSH-Verbindung testen (siehe nächsten Schritt)
```

**Alternative für Windows: PuTTY (falls OpenSSH fehlt)**

Falls `ssh` Befehl nicht funktioniert:

1. Lade PuTTY herunter: https://www.putty.org/
2. Lade PuTTYgen herunter (kommt mit PuTTY)
3. Öffne PuTTYgen → Load → Wähle `.pem` Datei
4. Save Private Key → Speichere als `.ppk` Datei
5. Öffne PuTTY:
   * Host Name: `ubuntu@DEINE_PUBLIC_IP`
   * Connection → SSH → Auth → Browse → Wähle `.ppk` Datei
   * Open

**Empfehlung:** Nutze OpenSSH wenn möglich (einfacher!)

**Warum chmod 400?**
* SSH lehnt Keys ab, die von anderen gelesen werden können
* 400 = Nur du kannst lesen, niemand sonst
* Sicherheitsfeature

### Schritt 2: SSH-Verbindung testen

**Linux/Mac:**
```bash
# Verbinde dich mit der EC2-Instanz
ssh -i ~/.ssh/notes-api-key.pem ubuntu@DEINE_PUBLIC_IP

# Beispiel:
ssh -i ~/.ssh/notes-api-key.pem ubuntu@54.93.123.456
```

**Windows (PowerShell/CMD):**
```powershell
# Verbinde dich mit der EC2-Instanz
ssh -i C:\Users\DEINNAME\Downloads\notes-api-key.pem ubuntu@DEINE_PUBLIC_IP

# Beispiel:
ssh -i C:\Users\Max\Downloads\notes-api-key.pem ubuntu@54.93.123.456

# Hinweis: Passe den Pfad an deinen Benutzernamen und Speicherort an
```

**Was passiert beim ersten Mal?**
```
The authenticity of host '54.93.123.456' can't be established.
ECDSA key fingerprint is SHA256:abc123...
Are you sure you want to continue connecting (yes/no)?
```

* Tippe: **yes** und Enter
* Das ist normal beim ersten Verbinden
* Der Server-Fingerprint wird gespeichert

**Wenn alles funktioniert:**
```
Welcome to Ubuntu 24.04 LTS
...
ubuntu@ip-172-31-x-x:~$
```

**Du bist jetzt auf dem Server!**

### Troubleshooting SSH

**Problem: "Permission denied (publickey)"**
```bash
# Überprüfe Permissions
ls -la ~/.ssh/notes-api-key.pem

# Sollte sein: -r--------
# Falls nicht:
chmod 400 ~/.ssh/notes-api-key.pem
```

**Problem: "Connection refused"**
* Ist die Instanz "Running"?
* Ist die IP-Adresse korrekt?
* Security Group: Ist SSH (Port 22) erlaubt von deiner IP?

**Problem: "Connection timeout"**
* Ist die Security Group korrekt?
* Ist "Auto-assign public IP" aktiviert?

---

## Live-Coding Teil 3: Server vorbereiten

Jetzt bist du auf dem Server verbunden. Lass uns die Umgebung vorbereiten.

### Schritt 1: System aktualisieren

```bash
# Paketlisten aktualisieren
sudo apt update

# Installierte Pakete upgraden
sudo apt upgrade -y

# Dauer: 1-2 Minuten
```

**Was macht das?**
* `apt update` → Lädt Liste der verfügbaren Pakete
* `apt upgrade` → Installiert Updates für alle Pakete
* `-y` → Beantwortet alle Fragen automatisch mit "ja"

### Schritt 2: Benötigte Software installieren

```bash
# Python 3.12 und pip
sudo apt install -y python3 python3-pip python3-venv

# Git für Code-Management
sudo apt install -y git

# Nginx als Reverse Proxy
sudo apt install -y nginx

# AWS CLI für S3-Zugriff (wird später gebraucht)
sudo apt install -y awscli

# Überprüfe die Installationen
python3 --version    # Sollte Python 3.12.x zeigen
pip3 --version       # Sollte pip zeigen
nginx -v             # Sollte nginx Version zeigen
git --version        # Sollte git Version zeigen
aws --version        # Sollte aws-cli Version zeigen
```

### Schritt 3: Projektverzeichnis erstellen

```bash
# Erstelle Projektordner
mkdir -p ~/notes-api
cd ~/notes-api

# Überprüfe, wo du bist
pwd
# Sollte zeigen: /home/ubuntu/notes-api
```

### Schritt 4: Code auf den Server bringen

**Option A: Code manuell erstellen (einfacher für Lernen)**

```bash
# Erstelle main.py
nano main.py
```

**Kopiere den gesamten Code aus Tag 3 main.py hinein:**
* Strg+Shift+V zum Einfügen
* Strg+X zum Beenden
* Y zum Speichern
* Enter

```bash
# Erstelle db.py
nano db.py
```

**Kopiere den gesamten Code aus Tag 3 db.py hinein:**
* Gleicher Prozess

**Option B: Code via Git (professioneller)**

Wenn dein Code in einem Git-Repository ist:

```bash
# Klone dein Repository
git clone https://github.com/DEIN_USERNAME/notes-api.git
cd notes-api
```

### Schritt 5: Virtual Environment erstellen

```bash
# Erstelle venv
python3 -m venv venv

# Aktiviere venv
source venv/bin/activate

# Prompt sollte jetzt (venv) zeigen
```

### Schritt 6: Dependencies installieren

```bash
# Installiere FastAPI und Uvicorn
pip install fastapi uvicorn

# Überprüfe die Installation
pip list | grep fastapi
pip list | grep uvicorn
```

### Schritt 7: API testen (lokal auf Server)

```bash
# Starte die API (Test) - nur lokal erreichbar
uvicorn main:app --host 127.0.0.1 --port 8000

# Sollte zeigen:
# INFO:     Started server process
# INFO:     Uvicorn running on http://127.0.0.1:8000
```

**In einem neuen Terminal auf deinem Laptop:**
```bash
# Teste von außen (ersetze IP)
curl http://DEINE_PUBLIC_IP:8000

# PROBLEM: Connection refused!
```

**Warum funktioniert es nicht?**
* Port 8000 ist nicht in der Security Group!
* FastAPI läuft nur auf 127.0.0.1 (localhost) - nicht von außen erreichbar
* Das ist genau was wir wollen - Nginx ist das Gateway!

**Zurück auf dem Server:**
```bash
# Stoppe Uvicorn
Strg+C

# Test lokal auf dem Server
curl http://localhost:8000

# Sollte jetzt die API-Response zeigen!
```

---

## Live-Coding Teil 4: Systemd Service einrichten

Jetzt machen wir die API zu einem richtigen Service, der automatisch startet.

### Schritt 1: Service-Datei erstellen

```bash
# Erstelle Service-Datei
sudo nano /etc/systemd/system/notes-api.service
```

**Füge folgenden Inhalt ein:**

```ini
[Unit]
Description=Notes API Service
After=network.target
# Starte den Service erst, wenn das Netzwerk bereit ist

[Service]
# Als welcher User soll der Service laufen
User=ubuntu
# Arbeitsverzeichnis
WorkingDirectory=/home/ubuntu/notes-api
# Kommando zum Starten (mit venv!)
# Wichtig: --host 127.0.0.1 → nur lokal, Nginx ist das Gateway
ExecStart=/home/ubuntu/notes-api/venv/bin/uvicorn main:app --host 127.0.0.1 --port 8000
# Bei Crash automatisch neu starten
Restart=always
# Warte 3 Sekunden vor Neustart
RestartSec=3
# Standard Output und Error in Systemd Journal
StandardOutput=journal
StandardError=journal

[Install]
# Starte beim Booten
WantedBy=multi-user.target
```

**Speichern:** Strg+X, dann Y, dann Enter

**Erklärung der wichtigsten Teile:**

* `After=network.target` → Warte auf Netzwerk
* `User=ubuntu` → Nicht als root laufen (Sicherheit!)
* `WorkingDirectory` → Wo liegt die Anwendung
* `ExecStart` → Voller Pfad zum uvicorn im venv
* `Restart=always` → Bei Crash neu starten
* `RestartSec=3` → 3 Sekunden Pause zwischen Restarts
* `WantedBy=multi-user.target` → Beim Boot starten

### Schritt 2: Service aktivieren und starten

```bash
# Systemd neu laden (neue Service-Datei erkennen)
sudo systemctl daemon-reload

# Service aktivieren (beim Boot starten)
sudo systemctl enable notes-api

# Service jetzt starten
sudo systemctl start notes-api

# Status überprüfen
sudo systemctl status notes-api
```

**Erwartete Ausgabe:**
```
● notes-api.service - Notes API Service
     Loaded: loaded (/etc/systemd/system/notes-api.service; enabled)
     Active: active (running) since ...
   Main PID: 1234 (uvicorn)
```

**Wichtige Status-Werte:**
* `loaded` → Service-Datei wurde gelesen
* `enabled` → Startet beim Booten
* `active (running)` → Läuft gerade
* Grüner Punkt ● → Alles gut!

### Schritt 3: Logs ansehen

```bash
# Letzte 50 Zeilen der Logs
sudo journalctl -u notes-api -n 50

# Logs live verfolgen (wie tail -f)
sudo journalctl -u notes-api -f

# Zum Beenden: Strg+C
```

### Schritt 4: Service-Befehle (wichtig!)

```bash
# Service starten
sudo systemctl start notes-api

# Service stoppen
sudo systemctl stop notes-api

# Service neu starten
sudo systemctl restart notes-api

# Status anzeigen
sudo systemctl status notes-api

# Beim Boot aktivieren
sudo systemctl enable notes-api

# Beim Boot deaktivieren
sudo systemctl disable notes-api
```

### Schritt 5: Service testen

```bash
# API lokal testen
curl http://localhost:8000

# Sollte die API-Response zeigen

# Server neu starten (Test ob Service beim Boot startet)
sudo reboot
```

**Was passiert beim reboot?**
* SSH-Verbindung wird getrennt
* Server startet neu (1-2 Minuten)
* Service sollte automatisch starten

```bash
# Warte 2 Minuten, dann neu verbinden
ssh -i ~/.ssh/notes-api-key.pem ubuntu@DEINE_PUBLIC_IP

# Status überprüfen
sudo systemctl status notes-api
# Sollte "active (running)" zeigen!
```

---

## Live-Coding Teil 5: Nginx als Reverse Proxy

Jetzt machen wir die API über Port 80 erreichbar.

### Schritt 1: Nginx-Konfiguration erstellen

```bash
# Erstelle Konfigurationsdatei
sudo nano /etc/nginx/sites-available/notes-api
```

**Füge folgenden Inhalt ein:**

```nginx
# Upstream-Definition: Wo läuft die FastAPI?
upstream notes_api {
    server localhost:8000;
}

server {
    # Lausche auf Port 80 (HTTP)
    listen 80;
    
    # Server-Name (ersetze mit deiner IP oder Domain)
    server_name _;
    
    # Maximale Größe für Uploads
    client_max_body_size 10M;
    
    # Logs
    access_log /var/log/nginx/notes-api-access.log;
    error_log /var/log/nginx/notes-api-error.log;
    
    # Alle Requests an FastAPI weiterleiten
    location / {
        # Proxy-Headers setzen
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # An FastAPI weiterleiten
        proxy_pass http://notes_api;
        
        # Timeouts
        proxy_connect_timeout 300;
        proxy_send_timeout 300;
        proxy_read_timeout 300;
    }
}
```

**Speichern:** Strg+X, dann Y, dann Enter

**Erklärung der Konfiguration:**

**Upstream-Block:**
```nginx
upstream notes_api {
    server localhost:8000;
}
```
* Definiert, wo die FastAPI läuft
* `localhost:8000` → Intern auf dem Server
* Kann später mehrere Server haben (Load Balancing)

**Server-Block:**
```nginx
listen 80;
server_name _;
```
* `listen 80` → Lausche auf HTTP-Port 80
* `server_name _` → Akzeptiere alle Hostnamen (für IP-Zugriff)
* **Wichtig:** `_` ist ein Wildcard - funktioniert für den Zugriff per IP-Adresse
* Später kann hier eine Domain stehen: `server_name api.example.com;` (siehe HTTPS-Übung)
* **Für IP-Zugriff bleibt `server_name _;` korrekt - nicht ändern!**

**Proxy-Headers:**
```nginx
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
```
* Wichtig! FastAPI muss wissen, wer der echte Client ist
* Ohne diese Headers sieht FastAPI immer nur `127.0.0.1` (localhost)
* `X-Real-IP` → Echte IP des Clients
* `X-Forwarded-For` → Komplette Proxy-Chain

**Logs:**
```nginx
access_log /var/log/nginx/notes-api-access.log;
error_log /var/log/nginx/notes-api-error.log;
```
* Separate Log-Dateien für unsere API
* Access Log → Alle Requests
* Error Log → Nur Fehler

### Schritt 2: Nginx-Konfiguration aktivieren

```bash
# Erstelle Symlink (aktiviert die Konfiguration)
# Falls Symlink schon existiert, wird er ersetzt
sudo ln -sf /etc/nginx/sites-available/notes-api /etc/nginx/sites-enabled/

# Lösche die Default-Konfiguration (optional, aber empfohlen)
sudo rm -f /etc/nginx/sites-enabled/default

# Überprüfe die Nginx-Konfiguration auf Fehler
sudo nginx -t

# Erwartete Ausgabe:
# nginx: configuration file /etc/nginx/nginx.conf syntax is ok
# nginx: configuration file /etc/nginx/nginx.conf test is successful
```

**Was macht `-sf` beim ln Befehl?**
* `-s` = symbolic link (Symlink erstellen)
* `-f` = force (überschreibe falls existiert - verhindert Fehler bei Wiederholung)

**Was macht `-f` beim rm Befehl?**
* `-f` = force (kein Fehler falls Datei nicht existiert)

**Was bedeutet der Symlink?**
* `sites-available/` → Alle verfügbaren Konfigurationen
* `sites-enabled/` → Nur aktive Konfigurationen
* Nginx lädt nur Dateien aus `sites-enabled/`
* Symlink = Verknüpfung (wie ein Shortcut)

### Schritt 3: Nginx neu starten

```bash
# Nginx neu laden (ohne Downtime)
sudo systemctl reload nginx

# Oder: Nginx neu starten
sudo systemctl restart nginx

# Status überprüfen
sudo systemctl status nginx
```

**Expected Output:**
```
● nginx.service - A high performance web server
     Active: active (running)
```

### Schritt 4: Von außen testen

**Auf deinem Laptop (nicht auf dem Server):**

```bash
# HTTP-Request von deinem Laptop
curl http://DEINE_PUBLIC_IP

# Sollte jetzt die API-Response zeigen!

# Oder im Browser:
# http://DEINE_PUBLIC_IP
```

**Im Browser öffnen:**
```
http://DEINE_PUBLIC_IP
http://DEINE_PUBLIC_IP/docs    ← Swagger UI
http://DEINE_PUBLIC_IP/notes
```

**🎉 Glückwunsch! Deine API ist jetzt öffentlich erreichbar!**

### Schritt 5: Nginx-Logs ansehen

```bash
# Access Log (alle Requests)
sudo tail -f /var/log/nginx/notes-api-access.log

# Error Log (nur Fehler)
sudo tail -f /var/log/nginx/notes-api-error.log

# Zum Beenden: Strg+C
```

---

## Bonus: Logging und S3-Upload

Jetzt implementieren wir professionelles Logging mit automatischem Upload zu S3.

### Theorie: Warum Logs wichtig sind

**Was sind Logs?**
* Aufzeichnungen von Ereignissen in der Anwendung
* Requests, Fehler, Warnungen, Informationen
* Unverzichtbar für Debugging und Monitoring

**Problem ohne strukturiertes Logging:**
* `print()` Statements verschwinden
* Keine Historie
* Schwer nachzuvollziehen, was passiert ist

**Lösung: Strukturiertes Logging**
* Logs in Dateien schreiben
* Rotation (alte Logs archivieren)
* Zentrales Backup (S3)

### Schritt 1: S3-Bucket erstellen

**In der AWS Console:**

1. Suche nach "S3" in der Suchleiste
2. Klicke auf **"Create bucket"**
3. **Bucket name:** `notes-api-logs-DEINE-INITIALEN-ZAHL`
   * Beispiel: `notes-api-logs-js-2025`
   * Muss global eindeutig sein!
4. **Region:** eu-central-1 (Frankfurt)
5. **Block all public access:** AKTIVIERT (wichtig!)
6. Klicke auf **"Create bucket"**

### Schritt 2: IAM-Rolle für EC2 erstellen

Die EC2-Instanz braucht Berechtigungen, um zu S3 zu schreiben.

**In der AWS Console:**

1. Gehe zu **IAM** (Identity and Access Management)
2. Links: **Roles** → **Create role**
3. **Trusted entity type:** AWS service
4. **Use case:** EC2 → **Next**
5. **Permissions policies:** Suche nach `AmazonS3FullAccess`
   * Für Production: Erstelle eine eingeschränktere Policy!
   * Für Lernen: FullAccess ist ok
6. **Next**
7. **Role name:** `EC2-S3-Access-Role`
8. **Create role**

**Rolle an EC2-Instanz anhängen:**

1. Gehe zu **EC2** → **Instances**
2. Wähle deine Instanz
3. **Actions** → **Security** → **Modify IAM role**
4. Wähle: `EC2-S3-Access-Role`
5. **Update IAM role**

**Wichtig:** Es kann 1-2 Minuten dauern bis die Rolle aktiv wird!

**Auf dem Server testen (SSH):**

```bash
# Teste ob AWS CLI funktioniert
aws --version
# Sollte Version anzeigen

# Teste ob IAM-Rolle greift
aws sts get-caller-identity

# Sollte zeigen:
# {
#     "UserId": "AROAXXXXXXXXX:i-xxxxxxxxx",
#     "Account": "123456789012",
#     "Arn": "arn:aws:sts::123456789012:assumed-role/EC2-S3-Access-Role/i-xxxxx"
# }

# Wenn Fehler "Unable to locate credentials":
# → IAM-Rolle ist noch nicht aktiv, warte 1-2 Minuten

# Teste S3-Zugriff
aws s3 ls
# Sollte deine Buckets auflisten
```

### Schritt 3: Logging in der Anwendung aktivieren

**Auf dem Server:**

```bash
cd ~/notes-api
```

**Erstelle eine neue Datei `logger_config.py`:**

```bash
nano logger_config.py
```

**Füge ein:**

```python
"""
Logging-Konfiguration für Notes API
"""
import logging
from logging.handlers import RotatingFileHandler
import os

# Log-Verzeichnis erstellen
LOG_DIR = "/var/log/notes-api"
os.makedirs(LOG_DIR, exist_ok=True)

def setup_logger():
    """
    Richtet den Logger ein mit File Handler und Rotation.
    
    Returns:
        logging.Logger: Konfigurierter Logger
    """
    logger = logging.getLogger("notes-api")
    logger.setLevel(logging.INFO)
    
    # Verhindere Handler-Duplikate (wichtig bei mehrfachem Aufruf)
    if logger.handlers:
        return logger
    
    # Format für Log-Nachrichten
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # File Handler mit Rotation
    # Wenn Datei 10MB erreicht, neue Datei erstellen
    # Behalte max. 5 Backup-Dateien
    file_handler = RotatingFileHandler(
        f"{LOG_DIR}/api.log",
        maxBytes=10*1024*1024,  # 10 MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # Console Handler (zusätzlich)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger
```

**Speichern:** Strg+X, Y, Enter

### Schritt 4: Logger in main.py einbinden

**Bearbeite `main.py`:**

```bash
nano main.py
```

**Am Anfang hinzufügen (nach den anderen Imports):**

```python
from logger_config import setup_logger

# Logger initialisieren
logger = setup_logger()
```

**In den Endpoints Logging hinzufügen:**

```python
@app.get("/notes")
def get_notes(
    limit: int = Query(100, ge=1, le=100),
    search: Optional[str] = Query(None, min_length=2)
):
    """Alle Notizen abrufen mit Logging."""
    logger.info(f"GET /notes - limit={limit}, search={'***' if search else 'None'}")
    notes = db.get_all_notes(limit=limit, search=search)
    logger.info(f"Returning {len(notes)} notes")
    return notes

@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    """Neue Notiz erstellen mit Logging."""
    logger.info(f"POST /notes - Creating note (len={len(note.text)})")
    new_id = db.create_note(note.text)
    
    if new_id is None:
        logger.error("Failed to create note")
        raise HTTPException(500, "Fehler beim Erstellen der Notiz")
    
    logger.info(f"Created note with ID: {new_id}")
    return {"id": new_id, "text": note.text}

# Füge Logging zu allen anderen Endpoints hinzu...
```

**Wichtig zum Logging:**
* Logge **Länge** statt Inhalt (`len={len(note.text)}`) → Datenschutz!
* Maskiere Suchbegriffe (`'***' if search else 'None'`) → Keine sensiblen Daten im Log
* Logge IDs, Counts, Status → Gut für Debugging ohne Privacy-Risiko

**Speichern:** Strg+X, Y, Enter

### Schritt 5: Log-Verzeichnis vorbereiten (WICHTIG - vor Service-Start!)

```bash
# Log-Verzeichnis erstellen
sudo mkdir -p /var/log/notes-api

# Besitzer auf ubuntu setzen
sudo chown ubuntu:ubuntu /var/log/notes-api

# Berechtigungen setzen
sudo chmod 755 /var/log/notes-api

# Überprüfen
ls -ld /var/log/notes-api
# Sollte zeigen: drwxr-xr-x ... ubuntu ubuntu ... /var/log/notes-api
```

**Warum JETZT?**
* RotatingFileHandler braucht Schreibrechte auf das Verzeichnis
* Wenn das Verzeichnis nicht existiert oder falsche Rechte hat → Service startet nicht
* Besser jetzt vorbereiten, bevor wir den Service starten!

### Schritt 6: Service neu starten

```bash
# Service neu starten (neue Logging-Konfiguration laden)
sudo systemctl restart notes-api

# Status überprüfen
sudo systemctl status notes-api

# Logs ansehen
sudo tail -f /var/log/notes-api/api.log
```

**Teste die API:**
```bash
# Erstelle ein paar Requests
curl http://localhost:8000/notes
curl -X POST http://localhost:8000/notes \
  -H "Content-Type: application/json" \
  -d '{"text": "Test Notiz"}'
```

**Logs sollten jetzt erscheinen!**

### Schritt 7: S3-Upload-Script erstellen

**Erstelle ein Script für S3-Upload:**

```bash
nano ~/notes-api/upload-logs-to-s3.sh
```

**Füge ein (ersetze BUCKET_NAME):**

```bash
#!/bin/bash
# Script zum Hochladen von Logs zu S3

# Konfiguration
LOG_DIR="/var/log/notes-api"
S3_BUCKET="notes-api-logs-js-2025"  # ERSETZE MIT DEINEM BUCKET!
DATE=$(date +%Y-%m-%d)

# Wechsle in Log-Verzeichnis (mit Fehler-Check)
cd "$LOG_DIR" || exit 1

# Prüfe ob Log-Dateien existieren
if ! ls *.log 1> /dev/null 2>&1; then
    echo "Keine Log-Dateien gefunden. Überspringe Upload."
    exit 0
fi

# Log-Datei komprimieren
tar -czf "api-logs-${DATE}.tar.gz" *.log

# Zu S3 hochladen
aws s3 cp "api-logs-${DATE}.tar.gz" "s3://${S3_BUCKET}/logs/"

# Alte komprimierte Datei löschen
rm "api-logs-${DATE}.tar.gz"

# Optional: Alte Log-Dateien rotieren
find "$LOG_DIR" -name "*.log.*" -mtime +7 -delete

echo "Logs erfolgreich zu S3 hochgeladen: s3://${S3_BUCKET}/logs/api-logs-${DATE}.tar.gz"
```

**Speichern:** Strg+X, Y, Enter

**Script ausführbar machen:**

```bash
chmod +x ~/notes-api/upload-logs-to-s3.sh
```

**Testen:**

```bash
# Script manuell ausführen
~/notes-api/upload-logs-to-s3.sh

# Sollte ausgeben:
# Logs erfolgreich zu S3 hochgeladen...
```

**In S3 überprüfen:**
* Gehe zur AWS Console → S3
* Öffne deinen Bucket
* Im Ordner `logs/` sollte jetzt eine .tar.gz Datei sein!

### Schritt 8: Cronjob für automatischen Upload

**Öffne Crontab:**

```bash
crontab -e

# Beim ersten Mal: Wähle Editor (nano ist einfacher als vim)
# Wähle: 1 (nano)
```

**Füge am Ende hinzu:**

```bash
# Logs täglich um 3 Uhr morgens zu S3 hochladen
0 3 * * * /home/ubuntu/notes-api/upload-logs-to-s3.sh >> /var/log/notes-api/s3-upload.log 2>&1
```

**Speichern:** Strg+X, Y, Enter

**Erklärung des Cronjobs:**

```
0 3 * * *  → Zeitpunkt
│ │ │ │ │
│ │ │ │ └─── Wochentag (0-7, 0 und 7 = Sonntag)
│ │ │ └───── Monat (1-12)
│ │ └─────── Tag (1-31)
│ └───────── Stunde (0-23)
└─────────── Minute (0-59)

0 3 * * *  = Jeden Tag um 3:00 Uhr morgens
```

**Weitere Beispiele:**
```bash
# Jede Stunde
0 * * * * /pfad/zum/script.sh

# Jeden Montag um 9:00
0 9 * * 1 /pfad/zum/script.sh

# Jeden Monatsersten um Mitternacht
0 0 1 * * /pfad/zum/script.sh
```

**Cronjobs auflisten:**

```bash
crontab -l
```

**Testen (nicht 3 Uhr warten!):**

```bash
# Führe Script direkt aus
~/notes-api/upload-logs-to-s3.sh

# Überprüfe Upload-Log
cat /var/log/notes-api/s3-upload.log
```

---

## Mini-Aufgabe

**Aufgabe:** Erstelle einen Health-Check-Endpoint, der auch die Anzahl der Logs-Dateien zurückgibt.

**Anforderungen:**
* Endpoint: `GET /health`
* Response soll enthalten:
  * API-Status
  * Anzahl der Notizen
  * Anzahl der Log-Dateien in `/var/log/notes-api/`

<details>
<summary>Lösung anzeigen</summary>

**In main.py:**

```python
import os
from datetime import datetime

@app.get("/health")
def health():
    """
    Health-Check mit System-Informationen.
    """
    # Anzahl der Notizen
    notes_count = db.get_notes_count()
    
    # Anzahl der Log-Dateien
    log_dir = "/var/log/notes-api"
    try:
        log_files = [f for f in os.listdir(log_dir) if f.endswith('.log')]
        log_count = len(log_files)
    except Exception:
        log_count = 0
    
    return {
        "status": "ok",
        "notes_count": notes_count,
        "log_files_count": log_count,
        "timestamp": datetime.now().isoformat()
    }
```

**Testen:**
```bash
curl http://localhost:8000/health
```

**Erwartete Antwort:**
```json
{
  "status": "ok",
  "notes_count": 5,
  "log_files_count": 2,
  "timestamp": "2025-01-15T10:30:00"
}
```

</details>

---

## Übungen für Tag 4

### Übung 1: Umgebungsvariablen verwenden

**Problem:** S3-Bucket-Name ist hardcoded im Script.

**Aufgabe:** Verwende Umgebungsvariablen für:
* S3-Bucket-Name
* AWS-Region
* Log-Retention-Days

<details>
<summary>Lösung anzeigen</summary>

**Erstelle `.env` Datei:**

```bash
nano ~/notes-api/.env
```

**Inhalt:**
```bash
S3_BUCKET=notes-api-logs-js-2025
AWS_REGION=eu-central-1
LOG_RETENTION_DAYS=7
```

**In upload-logs-to-s3.sh:**

```bash
#!/bin/bash

# Lade Umgebungsvariablen (absoluter Pfad für Cron!)
source /home/ubuntu/notes-api/.env

LOG_DIR="/var/log/notes-api"
DATE=$(date +%Y-%m-%d)

cd $LOG_DIR
tar -czf api-logs-${DATE}.tar.gz *.log

# Verwende Variablen
aws s3 cp api-logs-${DATE}.tar.gz s3://${S3_BUCKET}/logs/ --region ${AWS_REGION}

rm api-logs-${DATE}.tar.gz

# Verwende LOG_RETENTION_DAYS
find $LOG_DIR -name "*.log.*" -mtime +${LOG_RETENTION_DAYS} -delete

echo "Logs uploaded to s3://${S3_BUCKET}/logs/"
```

**Wichtig:** 
* Absoluter Pfad `/home/ubuntu/...` statt `~/...`
* In Cronjobs funktioniert `~` oft nicht zuverlässig
* Besser immer volle Pfade in Scripts die per Cron laufen!

**Vorteile:**
* Einfacher zu konfigurieren
* Keine hardcoded Werte
* Wiederverwendbar auf anderen Servern

</details>

---

### Übung 2: HTTPS mit Let's Encrypt (Bonus)

**Aufgabe:** Aktiviere HTTPS für deine API mit einem kostenlosen SSL-Zertifikat.

**Voraussetzung:** Du brauchst eine eigene Domain
* Domain kann bei beliebigem Registrar gekauft werden (z.B. Namecheap, GoDaddy, Ionos)
* Günstige Domains oft ab ~1€/Jahr verfügbar
* **Hinweis:** Kostenlose Domain-Anbieter sind oft unzuverlässig - besser kleine Investition
* Für Testzwecke: Manche Anbieter haben Free Trials

<details>
<summary>Hintergrundwissen</summary>

**Warum HTTPS?**
* Verschlüsselte Kommunikation
* Browser zeigen "Sicher" an
* SEO-Vorteil
* Vertrauen der Nutzer

**Was ist Let's Encrypt?**
* Kostenlose SSL-Zertifikate
* Automatische Erneuerung
* Von allen Browsern akzeptiert

**Certbot:**
* Tool zum Einrichten von Let's Encrypt
* Automatisiert den gesamten Prozess

</details>

<details>
<summary>Lösung anzeigen</summary>

**Schritt 1: Domain einrichten**

1. Registriere/kaufe eine Domain bei einem Registrar deiner Wahl
2. Gehe zum DNS-Management deines Providers
3. Erstelle einen A-Record:
   * Type: A
   * Name: @ (für root domain) oder api (für Subdomain)
   * Value: DEINE_EC2_IP
   * TTL: 3600 (oder lasse den Standard)
4. Warte 5-15 Minuten bis DNS propagiert ist

**Schritt 2: Certbot installieren**

```bash
# Snapd installieren (falls nicht vorhanden)
sudo apt install snapd

# Certbot installieren
sudo snap install --classic certbot

# Symlink erstellen
sudo ln -s /snap/bin/certbot /usr/bin/certbot
```

**Schritt 3: Nginx-Konfiguration anpassen**

```bash
sudo nano /etc/nginx/sites-available/notes-api
```

**Ändere `server_name`:**
```nginx
server {
    listen 80;
    server_name deine-domain.com;  # ERSETZE MIT DEINER DOMAIN
    # Rest bleibt gleich
}
```

**Schritt 4: Zertifikat erstellen**

```bash
# Certbot mit Nginx-Plugin
sudo certbot --nginx -d deine-domain.com

# Folge den Anweisungen:
# - Email eingeben
# - Bedingungen akzeptieren
# - Redirect auf HTTPS? JA
```

**Certbot macht automatisch:**
* Erstellt SSL-Zertifikat
* Passt Nginx-Konfiguration an
* Erstellt Cronjob für Auto-Renewal

**Schritt 5: Testen**

```bash
# Im Browser öffnen
https://deine-domain.com
https://deine-domain.com/docs
```

**Du solltest jetzt ein grünes Schloss sehen!**

**Security Group anpassen:**
* Gehe zu AWS Console → EC2 → Security Groups
* Füge Regel hinzu:
  * Type: HTTPS
  * Port: 443
  * Source: Anywhere (0.0.0.0/0)

</details>

---

### Übung 3: Monitoring mit simple Health-Check

**Aufgabe:** Implementiere einen einfachen Monitoring-Mechanismus.

<details>
<summary>Lösung anzeigen</summary>

**Erstelle ein Monitoring-Script:**

```bash
nano ~/notes-api/health-check.sh
```

**Inhalt:**

```bash
#!/bin/bash
# Einfacher Health-Check

API_URL="http://localhost:8000/health"
LOG_FILE="/var/log/notes-api/health-check.log"

# Aktuelles Datum
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Health-Check durchführen
RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" $API_URL)

if [ $RESPONSE -eq 200 ]; then
    echo "$DATE - OK - API is healthy (HTTP $RESPONSE)" >> $LOG_FILE
else
    echo "$DATE - ERROR - API is down (HTTP $RESPONSE)" >> $LOG_FILE
    
    # Optional: Service neu starten
    # sudo systemctl restart notes-api
    
    # Optional: Email senden
    # echo "API is down!" | mail -s "Alert: API Down" deine@email.com
fi
```

**Ausführbar machen:**
```bash
chmod +x ~/notes-api/health-check.sh
```

**Cronjob hinzufügen (alle 5 Minuten):**
```bash
crontab -e
```

**Füge hinzu:**
```bash
# Health-Check alle 5 Minuten
*/5 * * * * /home/ubuntu/notes-api/health-check.sh
```

**Logs ansehen:**
```bash
tail -f /var/log/notes-api/health-check.log
```

</details>

---

### Übung 4 (Bonus): Database Backup zu S3

**Aufgabe:** Erstelle ein Script, das die SQLite-Datenbank täglich zu S3 sichert.

<details>
<summary>Lösung anzeigen</summary>

**Schritt 1: SQLite CLI installieren (falls nicht vorhanden)**

```bash
# SQLite3 CLI installieren
sudo apt install -y sqlite3

# Überprüfen
sqlite3 --version
# Sollte Version anzeigen, z.B. 3.37.2
```

**Schritt 2: Backup-Script erstellen**

**Erstelle Backup-Script:**

```bash
nano ~/notes-api/backup-db-to-s3.sh
```

**Inhalt:**

```bash
#!/bin/bash
# Datenbank-Backup zu S3

DB_PATH="/home/ubuntu/notes-api/notes.db"
BACKUP_DIR="/tmp/db-backups"
S3_BUCKET="notes-api-logs-js-2025"  # DEIN BUCKET
DATE=$(date +%Y-%m-%d)

# Backup-Verzeichnis erstellen
mkdir -p $BACKUP_DIR

# SQLite-Datenbank exportieren (sauber)
sqlite3 $DB_PATH ".backup '$BACKUP_DIR/notes-${DATE}.db'"

# Komprimieren
cd $BACKUP_DIR
gzip notes-${DATE}.db

# Zu S3 hochladen
aws s3 cp notes-${DATE}.db.gz s3://${S3_BUCKET}/backups/

# Lokales Backup löschen
rm notes-${DATE}.db.gz

# Alte Backups in S3 löschen (älter als 30 Tage)
# aws s3 ls s3://${S3_BUCKET}/backups/ | ... (komplexer)

echo "Backup erfolgreich: s3://${S3_BUCKET}/backups/notes-${DATE}.db.gz"
```

**Ausführbar machen:**
```bash
chmod +x ~/notes-api/backup-db-to-s3.sh
```

**Cronjob hinzufügen (täglich um 2 Uhr):**
```bash
crontab -e
```

**Füge hinzu:**
```bash
# Database Backup täglich um 2:00
0 2 * * * /home/ubuntu/notes-api/backup-db-to-s3.sh >> /var/log/notes-api/backup.log 2>&1
```

**Testen:**
```bash
~/notes-api/backup-db-to-s3.sh

# In S3 überprüfen
aws s3 ls s3://DEIN-BUCKET/backups/
```

</details>

---

## Zusammenfassung Tag 4

**Was haben wir gelernt?**

### Kernziele (Pflicht) 

Diese Ziele machen die API produktiv erreichbar:

**AWS EC2:**
* EC2-Instanz erstellen und konfigurieren
* Security Groups (Firewall) einrichten
* SSH-Verbindung mit Key-Pair
* Public IP und Netzwerk-Grundlagen
* Instanztypen verstehen (t2.micro/t3.micro)

**Server-Setup:**
* Ubuntu-Server aktualisieren
* Python, Nginx, AWS CLI installieren
* Virtual Environment erstellen
* Code auf Server deployen

**Systemd Service:**
* Service-Datei erstellen
* Service aktivieren und starten
* Automatisches Starten beim Boot
* Logs mit journalctl ansehen
* FastAPI auf localhost (127.0.0.1) binden

**Nginx Reverse Proxy:**
* Nginx-Konfiguration schreiben
* Upstream-Block verstehen
* Proxy-Headers setzen
* API über Port 80 erreichbar machen
* Defense in Depth (Nginx als Gateway)

**Ergebnis:** API ist öffentlich über `http://DEINE_IP/docs` erreichbar! 🎉

---

### Bonus-Ziele (Optional) ⭐

Diese erweitern das Setup um Production-Features:

**Logging:**
* Python Logging-Modul nutzen
* RotatingFileHandler für Log-Rotation
* Logs in Dateien schreiben
* Handler-Duplikate vermeiden

**S3 und Automatisierung:**
* S3-Bucket erstellen
* IAM-Rolle für EC2 einrichten
* Shell-Script für S3-Upload
* Cronjobs einrichten
* Automatische Log-Archivierung

**HTTPS (Übung 2):**
* Domain einrichten
* Let's Encrypt Zertifikat
* HTTPS aktivieren

**Monitoring und Backups (Übungen 3+4):**
* Health-Check Endpoint
* Database Backups zu S3
* Umgebungsvariablen

---

### Best Practices
* Nicht als root laufen
* Security Groups restriktiv konfigurieren
* Private Keys sicher verwahren
* Logs rotieren und archivieren
* Automatisierung mit Cronjobs

---

## Troubleshooting Guide

### Problem: SSH Connection refused

**Symptom:**
```bash
ssh: connect to host 54.93.123.456 port 22: Connection refused
```

**Lösungen:**
1. Ist die Instanz "Running"? (AWS Console überprüfen)
2. Security Group: Port 22 offen für deine IP?
3. Ist "Auto-assign public IP" aktiviert?
4. Firewall auf deinem Laptop blockiert SSH?

### Problem: API nicht erreichbar

**Symptom:**
```bash
curl http://DEINE_IP
# Connection refused
```

**Lösungen:**

1. **Ist der Service running?**
   ```bash
   sudo systemctl status notes-api
   # Sollte "active (running)" zeigen
   ```

2. **Läuft Nginx?**
   ```bash
   sudo systemctl status nginx
   ```

3. **Security Group: Port 80 offen?**
   * AWS Console → EC2 → Security Groups
   * Inbound Rules: HTTP (80) auf 0.0.0.0/0?

4. **Nginx-Logs überprüfen:**
   ```bash
   sudo tail -f /var/log/nginx/notes-api-error.log
   ```

5. **API-Logs überprüfen:**
   ```bash
   sudo journalctl -u notes-api -f
   ```

### Problem: S3-Upload schlägt fehl

**Symptom:**
```bash
upload failed: Unable to locate credentials
```

**Lösungen:**

1. **IAM-Rolle angehängt?**
   * AWS Console → EC2 → Instanz → Security → IAM role
   * Sollte eine Rolle anzeigen

2. **AWS CLI konfiguriert?**
   ```bash
   # Test ob Credentials funktionieren
   aws s3 ls
   ```

3. **Bucket-Name korrekt?**
   ```bash
   # Liste alle Buckets
   aws s3 ls
   ```

### Problem: Cronjob läuft nicht

**Symptom:**
```bash
crontab -l
# Cronjob ist da, aber Script läuft nicht
```

**Lösungen:**

1. **Script ausführbar?**
   ```bash
   ls -la ~/notes-api/upload-logs-to-s3.sh
   # Sollte -rwxr-xr-x zeigen (x = executable)
   
   # Falls nicht:
   chmod +x ~/notes-api/upload-logs-to-s3.sh
   ```

2. **Absolute Pfade verwenden:**
   ```bash
   # Im Cronjob immer volle Pfade:
   0 3 * * * /home/ubuntu/notes-api/upload-logs-to-s3.sh
   # NICHT: ~/notes-api/upload-logs-to-s3.sh
   ```

3. **Output umleiten:**
   ```bash
   # Füge am Ende hinzu:
   0 3 * * * /home/ubuntu/notes-api/upload-logs-to-s3.sh >> /tmp/cron.log 2>&1
   
   # Dann logs ansehen:
   cat /tmp/cron.log
   ```

4. **Cron-Mail überprüfen:**
   ```bash
   sudo tail /var/mail/ubuntu
   ```

---

## Checkliste Tag 4

### Kernziele (Pflicht) 

**AWS Setup:**
- [ ] AWS Sandbox-Zugang funktioniert (https://sandboxes.techstarter.de/)
- [ ] EC2-Instanz erstellt (t2.micro oder t3.micro, Free tier eligible)
- [ ] Security Group konfiguriert (SSH Port 22 + HTTP Port 80)
- [ ] Private Key (.pem) heruntergeladen und gesichert
- [ ] SSH-Verbindung funktioniert

**Server-Konfiguration:**
- [ ] System aktualisiert (apt update && upgrade)
- [ ] Python, pip, venv installiert
- [ ] Nginx installiert
- [ ] AWS CLI installiert
- [ ] Git installiert (optional)
- [ ] Code auf Server kopiert
- [ ] Virtual Environment erstellt
- [ ] Dependencies installiert (FastAPI, Uvicorn)

**Systemd Service:**
- [ ] Service-Datei erstellt (mit --host 127.0.0.1)
- [ ] Service aktiviert und gestartet
- [ ] Service läuft (systemctl status zeigt "active running")
- [ ] Service überlebt Neustart (getestet mit sudo reboot)

**Nginx Reverse Proxy:**
- [ ] Nginx-Konfiguration erstellt
- [ ] Konfiguration aktiviert (Symlink)
- [ ] Nginx-Config getestet (nginx -t)
- [ ] Nginx neu geladen
- [ ] API erreichbar von außen: `http://DEINE_IP/docs`
- [ ] Swagger UI funktioniert

** Wenn alle obigen Punkte vorhanden sind: Kernziel erreicht!**

---

### Bonus-Ziele (Optional) ⭐

**Logging (Bonus):**
- [ ] Logger-Konfiguration erstellt (logger_config.py)
- [ ] Log-Verzeichnis vorbereitet (/var/log/notes-api)
- [ ] Handler-Duplikate Check eingebaut
- [ ] Logging in Endpoints eingebaut
- [ ] Logs werden geschrieben und rotiert

**S3 und Backup (Bonus):**
- [ ] S3-Bucket erstellt
- [ ] IAM-Rolle erstellt und an EC2 angehängt
- [ ] AWS CLI Credentials getestet (aws sts get-caller-identity)
- [ ] Upload-Script erstellt (mit Guard für fehlende Logs)
- [ ] Upload-Script funktioniert
- [ ] Cronjob eingerichtet
- [ ] Automatischer Upload funktioniert

**Übungen (Bonus):**
- [ ] Umgebungsvariablen (.env) implementiert
- [ ] HTTPS mit Let's Encrypt (wenn Domain vorhanden)
- [ ] Health-Check Monitoring
- [ ] Database Backup zu S3

---

## Ausblick auf Tag 5

Morgen könnten wir folgende Themen behandeln:

**Mögliche Themen:**
* **CI/CD:** GitHub Actions für automatisches Deployment
* **Docker:** Anwendung containerisieren
* **Monitoring:** Grafana + Prometheus für Metriken
* **Testing:** Automatische Tests mit pytest
* **Datenbank:** Migration von SQLite zu PostgreSQL
* **Advanced:** Load Balancing mit mehreren EC2-Instanzen

---

## Kosten-Übersicht und Aufräumen

### Was kostet was?

**Für diesen Kurs (Techstarter Sandbox):**
* Budget-Limit: 15€ pro Teilnehmer
* **Wichtig:** Kosten variieren nach Region, Nutzung und Zeitraum
* Eine kleine Instanz (t2.micro/t3.micro) verbraucht typisch einige Euro pro Woche bei 24/7 Betrieb
* S3 Storage und Transfers sind bei unserem Umfang meist unter 1€
* **Am besten:** Beobachte im Sandbox-Dashboard dein Budget und räume täglich auf!
* **WICHTIG:** Am Ende des Tages/Projekts aufräumen (siehe unten)!

**Eigene AWS Accounts (Free Tier):**

Die Free Tier Konditionen variieren je nach Account-Erstellungsdatum:

**Legacy Free Tier (Accounts vor Juli 2025):**
* 750 Stunden EC2 t2.micro/Monat (12 Monate)
* 5 GB S3 Storage
* 15 GB Datenübertragung aus EC2

**Aktuelles Free Tier:**
* Konditionen variieren - prüfe im AWS Free Tier Dashboard
* Achte auf "Free tier eligible" Labels
* Oft ähnliche oder bessere Konditionen

**Nach Free Tier (oder außerhalb):**
* t2.micro: ~8-10€/Monat
* t3.micro: ~9-11€/Monat  
* S3 Storage: ~0,023€/GB/Monat
* S3 Requests: Vernachlässigbar für kleine Projekte

**Kosten sparen:**

**In der Techstarter Sandbox:**
* Instanz **terminate** nach dem Training (nicht stop!)
* Auch gestoppte Instanzen verbrauchen Budget durch EBS Storage
* S3 Buckets komplett leeren und löschen
* Siehe detaillierte Aufräum-Anleitung weiter unten

**Eigener AWS Account:**
* Instanz **stoppen** wenn du später weitermachen willst (nicht terminate!)
* Bei "Stop" bezahlst du nur EBS Storage (~0,80€/Monat für 8GB)
* S3-Lifecycle-Policies für alte Logs einrichten
* Elastic IPs freigeben wenn nicht genutzt

### Ressourcen aufräumen (wichtig für Sandbox!)

**Wenn du in der Techstarter Sandbox arbeitest:**

Am Ende des Trainings/Tages solltest du aufräumen, um Budget zu sparen:

1. **EC2-Instanz TERMINATE (löschen):**
   ```bash
   # In AWS Console:
   EC2 → Instances → Instanz auswählen → Instance State → Terminate
   ```
   * **Warum terminate?** Sandbox hat Budget-Limit (15€)
   * Selbst gestoppte Instanzen kosten durch EBS Storage (~0,80€/Monat)
   * **WARNUNG:** Alle Daten sind weg! Vorher wichtige Daten sichern!

2. **S3-Bucket aufräumen:**
   ```bash
   # Alle Objekte löschen
   aws s3 rm s3://DEIN-BUCKET --recursive
   
   # Bucket löschen
   aws s3 rb s3://DEIN-BUCKET
   ```
   * S3 Storage kostet auch wenn wenig - besser komplett leeren

3. **Elastic IPs freigeben** (falls du eine reserviert hast):
   * EC2 → Elastic IPs → Adresse auswählen → Release
   * Ungenutzte Elastic IPs kosten Geld!

4. **Security Group löschen** (optional, falls selbst erstellt):
   * EC2 → Security Groups → `notes-api-sg` auswählen → Delete
   * Nur möglich wenn keine Instanz mehr damit verbunden ist

5. **IAM Role aufräumen** (optional):
   * IAM → Roles → `EC2-S3-Access-Role` → Delete
   * Vorsicht: Nur löschen wenn du sie selbst erstellt hast!
   * Manche Sandboxes erlauben das Löschen von Roles nicht

6. **Key Pair löschen** (optional):
   * EC2 → Key Pairs → `notes-api-key` auswählen → Delete
   * Nur die AWS-seitige Registrierung, deine lokale .pem-Datei bleibt

**Minimale Aufräum-Checkliste für Sandbox:**
-  EC2-Instanz terminieren
-  S3-Bucket leeren und löschen
-  Elastic IPs freigeben (falls vorhanden)
-  Security Group löschen (wenn möglich)
-  IAM Role löschen (wenn selbst erstellt und erlaubt)

**Wenn du in deinem eigenen AWS Account arbeitest:**

Hier kannst du die Instanz stoppen statt löschen, wenn du später weitermachen willst:

1. **EC2-Instanz STOPPEN (nicht löschen!):**
   ```bash
   # In AWS Console:
   EC2 → Instances → Instanz auswählen → Instance State → Stop
   ```
   * Bei "Stop" bleiben alle Daten erhalten
   * Du zahlst nur für EBS Storage (~0,80€/Monat für 8GB)
   * Kannst sie jederzeit wieder starten
   * Public IP ändert sich beim Neustart (außer du nutzt Elastic IP)

2. **EC2-Instanz LÖSCHEN (nur wenn sicher!):**
   ```bash
   # In AWS Console:
   EC2 → Instances → Instanz auswählen → Instance State → Terminate
   ```
   * **WARNUNG:** Alle Daten sind weg!
   * Kann nicht rückgängig gemacht werden!
   * Nur wenn du das Projekt nicht mehr brauchst

3. **S3-Bucket aufräumen:**
   ```bash
   # Alle Objekte löschen
   aws s3 rm s3://DEIN-BUCKET --recursive
   
   # Bucket löschen
   aws s3 rb s3://DEIN-BUCKET
   ```

**Zusammenfassung:**
* **Sandbox:** Terminate + S3 löschen (Budget schonen)
* **Eigener Account:** Stop (weitermachen) oder Terminate (beenden)

---

## Finale Projekt-Struktur

**Auf dem Server:**

```
/home/ubuntu/notes-api/
├── venv/                      # Virtual Environment
├── main.py                    # FastAPI Anwendung
├── db.py                      # Datenbank-Modul
├── logger_config.py           # Logging-Konfiguration
├── notes.db                   # SQLite-Datenbank
├── upload-logs-to-s3.sh       # S3-Upload-Script
├── backup-db-to-s3.sh         # Backup-Script (Bonus)
└── health-check.sh            # Monitoring-Script (Bonus)

/etc/systemd/system/
└── notes-api.service          # Systemd Service

/etc/nginx/sites-available/
└── notes-api                  # Nginx-Konfiguration

/var/log/notes-api/
├── api.log                    # Anwendungs-Logs
├── api.log.1                  # Rotierte Logs
├── s3-upload.log              # S3-Upload-Logs
└── health-check.log           # Health-Check-Logs
```

**In AWS:**

```
EC2:
└── notes-api-server (t2.micro)
    ├── Security Group (SSH + HTTP)
    └── IAM Role (S3 Access)

S3:
└── notes-api-logs-XXXX/
    ├── logs/
    │   ├── api-logs-2025-01-15.tar.gz
    │   └── api-logs-2025-01-16.tar.gz
    └── backups/ (optional)
        ├── notes-2025-01-15.db.gz
        └── notes-2025-01-16.db.gz
```

---

## Best Practices Zusammenfassung

**Sicherheit:**
* Nie als root arbeiten
* Private Keys mit chmod 400
* Security Groups restriktiv
* Regelmäßige Updates (apt upgrade)
* IAM-Rollen statt Access Keys

**Monitoring:**
* Logs strukturiert schreiben
* Health-Check-Endpoint
* Automatisches Monitoring
* Alerts bei Problemen

**Automatisierung:**
* Cronjobs für wiederkehrende Aufgaben
* Automatische Backups
* Log-Rotation
* S3-Archivierung

**Deployment:**
* Systemd für Services
* Nginx als Reverse Proxy
* Nie direkt auf Port 8000 exponieren
* Virtual Environment nutzen

**Dokumentation:**
* Alle Scripts dokumentieren
* Konfigurationen kommentieren
* README.md erstellen
* Deployment-Schritte festhalten

---

** Glückwunsch! Du hast eine vollständige Production-Umgebung aufgesetzt!**

**Deine API ist jetzt:**
*  Öffentlich erreichbar
*  Automatisch startend
*  Professionell geloggt
*  Automatisch gesichert
*  Produktionsreif!

**Bei Fragen meldet euch bei Patrick oder mir. Viel Erfolg!**
