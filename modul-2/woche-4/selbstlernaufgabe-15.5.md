# AWS Praxisprojekt: Apache Logfile-Upload zu S3

## Überblick

In diesem Praxisprojekt richtest du einen automatisierten Log-Upload-Service ein. Eine EC2-Instanz mit Apache Webserver sammelt Zugriffslogdateien, die täglich komprimiert und automatisch in einen S3-Bucket hochgeladen werden.

### Was ist das Ziel dieses Projekts?

Stell dir vor, du betreibst einen Webserver in der Cloud. Jeden Tag greifen Hunderte oder Tausende Nutzer auf deine Website zu. Der Webserver schreibt jeden Zugriff in Logdateien - wer hat wann welche Seite besucht? Diese Logs sind wertvoll für:

- **Fehlersuche**: Welche Fehler treten auf?
- **Sicherheit**: Gab es verdächtige Zugriffe?
- **Statistik**: Wie viele Besucher hatte ich?
- **Compliance**: Gesetzliche Aufbewahrungspflichten

**Das Problem**: Wenn dein Server ausfällt oder neu gestartet wird, sind die Logs weg. Außerdem füllen sich die Festplatten mit der Zeit.

**Unsere Lösung**: Wir sichern die Logs automatisch jeden Tag in S3 (AWS Cloud-Speicher), wo sie sicher und langfristig aufbewahrt werden.

### Was lernst du dabei?

**AWS-Dienste:**
- **EC2**: Virtuelle Server in der Cloud mieten und verwalten
- **S3**: Unbegrenzt Dateien speichern (Object Storage)
- **IAM**: Sichere Berechtigungen ohne Passwörter

**Linux-Administration:**
- Webserver-Installation und -Konfiguration
- Bash-Scripting für Automatisierung
- Cron-Jobs für zeitgesteuerte Aufgaben

**Best Practices:**
- Automatisches Backup
- Sichere Cloud-Authentifizierung
- Infrastruktur als Code

### Wie funktioniert es technisch?

**Architektur:**
```
EC2-Instanz (Ubuntu mit Apache)
    ├─> Apache schreibt Logs nach /var/log/apache2/
    │   ├─> access.log (wer hat zugegriffen?)
    │   └─> error.log (welche Fehler gab es?)
    │
    └─> Cron-Job läuft täglich um 23:55 Uhr (UTC)
        ├─> 1. Logs in tar.gz packen (komprimieren)
        ├─> 2. Upload zu S3 mit AWS CLI
        ├─> 3. Alte lokale Archive aufräumen
        └─> Erfolg/Fehler ins Log schreiben

S3-Bucket (Cloud-Speicher)
    └─> logs/
        ├─> apache-logs-2025-10-24.tar.gz
        ├─> apache-logs-2025-10-25.tar.gz
        └─> ... (automatisch gelöscht nach 30 Tagen)
```

**Warum ist das besser als manuelles Backup?**
- Läuft automatisch - du musst nichts tun
- Keine vergessenen Backups
- Logs sind auch bei Server-Ausfall sicher
- Spart Festplattenspeicher auf dem Server
- Skalierbar: Funktioniert für 1 oder 1000 Server

---

## Voraussetzungen

- Zugang zur AWS Sandbox: https://sandboxes.techstarter.de/
- Windows 11 Rechner
- SSH-Client (OpenSSH in PowerShell oder WSL)
- Grundkenntnisse in Bash-Befehlen
- Zeitaufwand: ca. 45-60 Minuten

**Region:** Wir arbeiten in **eu-central-1 (Frankfurt)**

---

## Schritt 1: S3-Bucket erstellen

### Was ist S3?

**S3 (Simple Storage Service)** ist der Cloud-Speicher von AWS. Stell dir S3 vor wie eine riesige Festplatte im Internet, aber viel besser:

- **Unbegrenzte Kapazität**: Du kannst so viele Dateien hochladen, wie du willst
- **Hochverfügbar**: AWS garantiert 99,999999999% (11 Neunen) Haltbarkeit - deine Daten gehen praktisch nie verloren
- **Skalierbar**: Funktioniert für 1 KB bis Petabytes
- **Bezahlung**: Du zahlst nur für den Speicher, den du wirklich nutzt (ca. 0,023 USD pro GB/Monat)

**Wichtige S3-Konzepte:**

1. **Bucket**: Ein Container für Dateien (wie ein Ordner, aber auf höchster Ebene)
   - Jeder Bucket hat einen global eindeutigen Namen
   - Beispiel: `logs-apache-max-847`

2. **Objekt**: Eine Datei im Bucket
   - Kann ein Foto, Video, Log, Backup, etc. sein
   - Hat einen eindeutigen "Key" (Pfad + Dateiname)
   - Beispiel: `logs/apache-logs-2025-10-24.tar.gz`

3. **Region**: Wo deine Daten physisch gespeichert werden
   - Wir nutzen `eu-central-1` (Frankfurt)
   - Daten verlassen die Region nicht (DSGVO-konform)

### Warum privater Bucket?

Wir machen den Bucket **privat**, weil:
- Logs können sensible Daten enthalten (IP-Adressen, User-Agents)
- Nur unser EC2-Server soll darauf zugreifen können
- Öffentlicher Zugriff wäre ein Sicherheitsrisiko

Der Zugriff erfolgt später über die **IAM-Rolle** - sicherer als Passwörter!

### Anleitung

1. Melde dich in der AWS Console an (https://sandboxes.techstarter.de/)
2. Wechsle oben rechts zur Region **eu-central-1 (Frankfurt)**
3. Suche in der Suchleiste nach **S3** und klicke darauf
4. Klicke auf den Button **Create bucket** (orange)

### Bucket-Konfiguration

**Bucket-Name:** 
- Trage ein: `logs-apache-deinname-123` 
- Ersetze `deinname` durch deinen Vornamen und `123` durch eine Zufallszahl
- Beispiel: `logs-apache-max-847`
- **Wichtig:** Nur Kleinbuchstaben, Ziffern und Bindestriche erlaubt
- Der Name muss global eindeutig sein (wird weltweit nur einmal vergeben)

**Region:**
- Wähle **EU (Frankfurt) eu-central-1**

**Block Public Access:**
- Lasse alle Häkchen gesetzt (Block all public access)
- Wir wollen einen privaten Bucket!

**Bucket Versioning:**
- Lasse auf **Disable** (nicht benötigt)

**Default encryption:**
- Encryption type: **Server-side encryption with Amazon S3 managed keys (SSE-S3)**
- Belasse alle anderen Einstellungen auf Standard

**Optional - Lifecycle Rule (automatisches Löschen alter Logs):**
- Klicke nach dem Erstellen des Buckets auf deinen Bucket
- Gehe zum Tab **Management**
- Klicke **Create lifecycle rule**
- Rule name: `delete-old-logs`
- Rule scope: **Apply to all objects in the bucket**
- Lifecycle rule actions: Wähle **Expire current versions of objects**
- Days after object creation: `30`
- Bestätige mit dem Häkchen bei "I acknowledge..."
- Klicke **Create rule**

**Erklärung:** Logdateien, die älter als 30 Tage sind, werden automatisch gelöscht, um Speicherkosten zu sparen.

5. Klicke ganz unten auf **Create bucket**

### Checkpoint

**Notiere dir:**
- Deinen vollständigen Bucket-Namen: `____________________`

**Wichtig:** Lass den Browser-Tab mit der AWS Console geöffnet, wir brauchen ihn gleich wieder!

---

## Schritt 2: IAM-Rolle für EC2 erstellen

### Was ist IAM und warum brauchen wir Rollen?

**IAM (Identity and Access Management)** regelt, wer was in AWS darf. Stell dir IAM vor wie einen Sicherheitsdienst, der Ausweise und Berechtigungen verwaltet.

### Das Problem: Wie greift EC2 auf S3 zu?

Unser EC2-Server muss Dateien in den S3-Bucket hochladen. Dafür braucht er Berechtigungen. Es gibt **zwei Möglichkeiten**:

**❌ Schlechte Methode: Access Keys (Benutzername + Passwort)**
```bash
aws configure
AWS Access Key ID: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```

**Warum schlecht?**
- Die Keys müssen auf dem Server gespeichert werden (unsicher!)
- Bei Kompromittierung: Angreifer hat vollen Zugriff
- Keys laufen nie ab - müssen manuell rotiert werden
- Schwer zu verwalten bei vielen Servern
- Versehentlich in Git committed? → Sicherheitslücke!

**✅ Gute Methode: IAM-Rolle (temporäre Berechtigungen)**

Die IAM-Rolle funktioniert wie ein Dienstausweis:
- EC2-Instanz bekommt eine "Rolle" zugewiesen
- AWS gibt automatisch temporäre Credentials (erneuern sich stündlich)
- Keine Credentials auf dem Server gespeichert
- Rolle kann nicht gestohlen werden
- Bei Instanz-Terminierung: Zugriff automatisch weg

**Analogie aus dem echten Leben:**
- Access Keys = Haustürschlüssel (kann kopiert/verloren werden)
- IAM-Rolle = Gesichtserkennung (nur du, nicht kopierbar)

### Was ist das Least Privilege Principle?

Wir geben dem Server **nur genau die Rechte, die er braucht** - nicht mehr!

**Unser Server braucht:**
- ✅ Bucket auflisten (`s3:ListBucket`)
- ✅ Dateien hochladen (`s3:PutObject`)

**Unser Server braucht NICHT:**
- ❌ Dateien löschen
- ❌ Bucket löschen
- ❌ Andere Buckets sehen
- ❌ EC2-Instanzen starten

Wenn der Server kompromittiert wird, kann der Angreifer **nur** Dateien in diesen einen Bucket hochladen - sonst nichts!

### Anleitung

**Schritt 2: Add permissions**
- Hier erstellen wir eine eigene Policy
- Klicke oben auf **Create policy** (öffnet sich in neuem Tab)

### Policy erstellen

Im neuen Tab:

1. Klicke auf den Tab **JSON**
2. Lösche den vorhandenen JSON-Code komplett
3. Füge folgenden Code ein (ersetze `<DEIN-BUCKET-NAME>` durch deinen echten Bucket-Namen):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:ListBucket"],
      "Resource": "arn:aws:s3:::<DEIN-BUCKET-NAME>"
    },
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:AbortMultipartUpload"],
      "Resource": "arn:aws:s3:::<DEIN-BUCKET-NAME>/*"
    }
  ]
}
```

**Beispiel:** Wenn dein Bucket `logs-apache-max-847` heißt, dann:
```json
"Resource": "arn:aws:s3:::logs-apache-max-847"
```
und
```json
"Resource": "arn:aws:s3:::logs-apache-max-847/*"
```

**Was bedeutet diese Policy? (Zeile für Zeile erklärt)**

```json
"Effect": "Allow"  →  Erlaube die folgenden Aktionen
```

**Erster Block (Bucket-Ebene):**
```json
"Action": ["s3:ListBucket"]  →  Darf den Inhalt des Buckets auflisten
"Resource": "arn:aws:s3:::logs-apache-max-847"  →  Nur für diesen Bucket
```

**Zweiter Block (Objekt-Ebene):**
```json
"Action": ["s3:PutObject", "s3:AbortMultipartUpload"]  →  Darf Dateien hochladen
"Resource": "arn:aws:s3:::logs-apache-max-847/*"  →  Alle Objekte im Bucket
```

**Warum `/*` am Ende?**
- Ohne `/*`: Berechtigung für den Bucket selbst (Container)
- Mit `/*`: Berechtigung für alle Objekte (Dateien) im Bucket

**Warum `AbortMultipartUpload`?**
- Große Dateien werden in Teilen hochgeladen
- Falls Upload fehlschlägt, muss AWS den Teil-Upload abbrechen können
- Verhindert Speichermüll

4. Klicke **Next**
5. Policy name: `S3-LogUpload-Policy`
6. Description: `Allows EC2 to upload logs to S3 bucket`
7. Klicke **Create policy**
8. Schließe diesen Tab und gehe zurück zum Tab "Create role"

1. Suche in der AWS Console nach **IAM** und klicke darauf
2. Klicke im linken Menü auf **Roles**
3. Klicke auf **Create role**

### Rolle konfigurieren

**Schritt 1: Select trusted entity**
- Trusted entity type: **AWS service**
- Use case: **EC2**
- Klicke **Next**

### Rolle fertigstellen

1. Klicke auf das Refresh-Symbol neben "Create policy"
2. Suche im Suchfeld nach `S3-LogUpload-Policy`
3. Wähle die Policy mit einem Häkchen aus
4. Klicke **Next**

**Schritt 3: Name, review, and create**
- Role name: `EC2-S3-LogUploader`
- Description: `Role for EC2 to upload Apache logs to S3`
- Klicke **Create role**

### Checkpoint

Die IAM-Rolle ist jetzt erstellt! Sie verleiht deiner EC2-Instanz später die Berechtigung, Logs in den S3-Bucket hochzuladen - ganz ohne Access Keys.

---

## Schritt 3: Security Group vorbereiten

### Was ist eine Security Group?

Eine **Security Group** ist eine virtuelle Firewall für deine EC2-Instanz. Sie kontrolliert, welcher Netzwerkverkehr rein und raus darf.

**Analogie aus dem echten Leben:**
Stell dir vor, deine EC2-Instanz ist ein Haus:
- **Security Group** = Türsteher mit Liste
- **Inbound Rules** = Wer darf reinkommen?
- **Outbound Rules** = Wer darf rausgehen?

### Welche Ports brauchen wir?

**Port 22 (SSH):**
- **Wofür?** Damit wir uns per Terminal mit dem Server verbinden können
- **Von wo?** Nur von deiner eigenen IP-Adresse (Sicherheit!)
- **Warum nicht von überall?** Sonst könnten Hacker versuchen, sich einzuloggen

**Port 80 (HTTP):**
- **Wofür?** Damit Browser auf den Apache-Webserver zugreifen können
- **Von wo?** Von überall (das ist ja der Sinn eines Webservers)
- **Nur für Demo:** In Produktion würdest du Port 443 (HTTPS) verwenden

**Was ist mit S3-Verkehr?**
- S3-Zugriff läuft über HTTPS (Port 443 ausgehend)
- Outbound-Regeln erlauben standardmäßig ALLES → kein Problem
- Wir müssen nichts extra konfigurieren

### Anleitung

1. Suche in der AWS Console nach **EC2** und klicke darauf
2. Klicke im linken Menü auf **Security Groups** (unter Network & Security)
3. Klicke **Create security group**

### Security Group konfigurieren

**Basic details:**
- Security group name: `apache-ssh-access`
- Description: `Allow SSH and HTTP access`
- VPC: Lasse die Default VPC ausgewählt

**Inbound rules:**

Klicke **Add rule** für jede Regel:

**Regel 1 - SSH:**
- Type: **SSH**
- Protocol: TCP
- Port range: 22
- Source: **My IP** (wird automatisch deine aktuelle IP eintragen)
- Description: `SSH from my IP`

**Regel 2 - HTTP:**
- Type: **HTTP**
- Protocol: TCP
- Port range: 80
- Source: **Anywhere-IPv4** (0.0.0.0/0)
- Description: `HTTP for testing`

**Outbound rules:**
- Lasse die Standard-Regel (All traffic to 0.0.0.0/0)

4. Klicke **Create security group**

### Checkpoint

Die Security Group ist fertig! Sie wird gleich der EC2-Instanz zugewiesen.

---

## Schritt 4: EC2-Instanz starten

### Was ist EC2?

**EC2 (Elastic Compute Cloud)** ist der virtuelle Server-Dienst von AWS. Statt einen physischen Server zu kaufen und im Rechenzentrum aufzustellen, mietest du einen virtuellen Server in der Cloud.

### Warum Cloud statt eigener Server?

**Traditioneller Weg (eigener Server):**
- Hardware kaufen (1.000-10.000 €)
- Rechenzentrum mieten
- Strom bezahlen (24/7)
- Kühlung einrichten
- Bei Ausfall: manuell austauschen
- Upgrade: neue Hardware kaufen

**Cloud-Weg (EC2):**
- Server in 5 Minuten starten
- Bezahlen nur für Laufzeit (ca. 0,01 € pro Stunde für t2.micro)
- Bei Bedarf größer/kleiner machen
- Bei Ausfall: neue Instanz starten
- Kein Hardware-Management

### Was bedeutet t2.micro?

AWS bietet verschiedene **Instanz-Typen** an. Die Bezeichnung `t2.micro` bedeutet:

- **t2** = Instanz-Familie (T steht für "burstable", also flexibel)
  - Gut für Workloads mit wechselnder Last
  - Wie ein Auto mit Turbo: Normalerweise sparsam, bei Bedarf mehr Power
  
- **micro** = Größe
  - 1 vCPU (virtuelle CPU)
  - 1 GB RAM
  - Reicht für unsere Demo perfekt!

**Andere Größen zum Vergleich:**
- `t2.nano`: 0,5 GB RAM (noch kleiner)
- `t2.small`: 2 GB RAM (doppelt so groß)
- `t2.medium`: 4 GB RAM (4x so groß)
- `m5.large`: 8 GB RAM (andere Familie, mehr Performance)

### Was ist ein AMI (Amazon Machine Image)?

Ein **AMI** ist wie eine Installations-DVD, aber für virtuelle Server:
- Ubuntu, Windows, Amazon Linux, etc.
- Vorinstallierte Software möglich
- Wir nutzen: **Ubuntu Server 22.04 LTS**

**Warum Ubuntu?**
- Weit verbreitet (viel Dokumentation)
- Kostenlos (Open Source)
- **LTS** = Long Term Support (5 Jahre Updates)
- Gute Package-Verwaltung (apt)

### Was ist ein Key Pair?

Der **Key Pair** ist dein Schlüssel zum Server:
- **Privater Schlüssel** (.pem Datei) = nur bei dir
- **Öffentlicher Schlüssel** = auf dem Server

**Wie funktioniert SSH mit Keys?**
1. Du verbindest dich: `ssh -i key.pem ubuntu@server`
2. Server schickt verschlüsselte Challenge
3. Dein privater Key entschlüsselt sie
4. Server prüft: Passt? → Zugang erlaubt!

**Warum keine Passwörter?**
- Passwörter können erraten werden (Brute Force)
- SSH-Keys sind 2048-4096 Bit lang → praktisch unknackbar
- Kein Passwort-Reset nötig

### Anleitung

1. In der EC2-Console, klicke im linken Menü auf **Instances**
2. Klicke **Launch instances**

### Instanz konfigurieren

**Name and tags:**
- Name: `apache-log-server`

**Application and OS Images (Amazon Machine Image):**
- Quick Start: **Ubuntu**
- Wähle **Ubuntu Server 22.04 LTS**
- Architecture: **64-bit (x86)**

**Instance type:**
- Wähle **t2.micro** (Free tier eligible)

**Key pair (login):**
- Klicke **Create new key pair**
  - Key pair name: `apache-log-key`
  - Key pair type: **RSA**
  - Private key file format: **pem** (für OpenSSH/WSL) ODER **ppk** (für PuTTY)
  - Klicke **Create key pair**
- Die Datei wird automatisch heruntergeladen - **speichere sie sicher!**

**Network settings:**
- Klicke **Edit**
- VPC: Lasse Default VPC
- Subnet: No preference
- Auto-assign public IP: **Enable**
- Firewall (security groups): **Select existing security group**
- Wähle die Security Group `apache-ssh-access` aus

**Configure storage:**
- 8 GiB gp3 (Standard ist ausreichend)

**Advanced details:**
- Scrolle nach unten zu **IAM instance profile**
- Wähle **EC2-S3-LogUploader** aus der Dropdown-Liste

**Wichtig:** Falls du die Rolle hier vergisst, kannst du sie später zuweisen über:
EC2 Console → Instanz auswählen → Actions → Security → Modify IAM role

**Summary:**
- Number of instances: **1**

3. Klicke **Launch instance**
4. Klicke auf **View all instances**
5. Warte, bis der Instance State **Running** ist und Status checks **2/2 checks passed** zeigt (dauert ca. 2-3 Minuten)

### Checkpoint

Die Instanz läuft! Du hast gerade einen virtuellen Server in Frankfurt gestartet.

**Notiere dir:**
- Public IPv4 address: `____________________`
- Instance ID (beginnt mit i-): `____________________`

**Verstehe, was passiert ist:**
- AWS hat in Sekundenschnelle einen virtuellen Server erstellt
- Der Server läuft jetzt in einem Amazon-Rechenzentrum in Frankfurt
- Du zahlst ab jetzt ca. 0,01 € pro Stunde (oder kostenlos im Free Tier)
- Der Server hat eine öffentliche IP → ist aus dem Internet erreichbar
- Die IAM-Rolle ist aktiv → Server kann auf S3 zugreifen

**📸 Screenshot 1 einreichen: EC2-Instanz-Details**

Klicke auf deine Instanz und mache einen Screenshot, der Folgendes zeigt:
- Instance State: **Running** (grüner Punkt)
- Public IPv4 address (sichtbar)
- Security groups: **apache-ssh-access**
- IAM role: **EC2-S3-LogUploader**

Dieser Screenshot beweist: Deine Instanz läuft mit der richtigen Konfiguration!

---

## Schritt 5: Mit EC2-Instanz verbinden (SSH)

### Was ist SSH?

**SSH (Secure Shell)** ist ein verschlüsseltes Protokoll, um sich mit einem entfernten Server zu verbinden. Es ist wie eine sichere Fernsteuerung für den Server.

**Was passiert beim SSH-Login?**
1. Dein Computer verbindet sich mit dem Server (Port 22)
2. Server schickt seinen Fingerprint (Identität)
3. Dein privater Key authentifiziert dich
4. Verbindung wird verschlüsselt aufgebaut
5. Du siehst die Terminal-Kommandozeile des Servers

**Warum verschlüsselt?**
- Alle Daten zwischen dir und dem Server sind verschlüsselt
- Niemand kann mitlesen (nicht mal dein ISP)
- Selbst öffentliche WLANs sind sicher

### Option A: PowerShell (Windows)

1. Öffne PowerShell als Administrator
2. Navigiere zum Ordner mit deinem Key:
```powershell
cd Downloads
```

3. Setze die richtigen Berechtigungen für den Key (wichtig!):
```powershell
icacls apache-log-key.pem /inheritance:r
icacls apache-log-key.pem /grant:r "$($env:USERNAME):R"
```

4. Verbinde dich mit der EC2-Instanz (ersetze `<PUBLIC-IP>`):
```powershell
ssh -i apache-log-key.pem ubuntu@<PUBLIC-IP>
```

5. Tippe `yes` wenn du nach "Are you sure you want to continue connecting?" gefragt wirst

### Option B: WSL (Windows Subsystem for Linux)

1. Öffne WSL (Ubuntu)
2. Kopiere den Key von Windows nach WSL:
```bash
cp /mnt/c/Users/<DEIN-USERNAME>/Downloads/apache-log-key.pem ~/
```

3. Setze die richtigen Berechtigungen:
```bash
chmod 400 ~/apache-log-key.pem
```

4. Verbinde dich mit der EC2-Instanz:
```bash
ssh -i ~/apache-log-key.pem ubuntu@<PUBLIC-IP>
```

### Checkpoint

Du solltest jetzt mit der EC2-Instanz verbunden sein und einen Prompt wie diesen sehen:
```
ubuntu@ip-172-31-XX-XX:~$
```

**Was bedeutet dieser Prompt?**
- `ubuntu` = Dein Benutzername auf dem Server
- `ip-172-31-XX-XX` = Hostname des Servers (interne IP)
- `~` = Du bist im Home-Verzeichnis (`/home/ubuntu`)
- `$` = Du bist ein normaler User (nicht root)

**Teste die Verbindung:**
```bash
hostname
whoami
pwd
```

Wenn du diese Ausgaben siehst, hat alles funktioniert!

---

## Schritt 6: Apache und AWS CLI installieren

### Was ist Apache?

**Apache HTTP Server** ist der weltweit meistgenutzte Webserver (seit 1995!). Er nimmt HTTP-Anfragen entgegen und liefert Webseiten aus.

**Wie funktioniert ein Webserver?**
```
Browser          →  HTTP-Request   →  Apache Webserver
(dein PC)           "GET /"            (EC2-Instanz)
                                       ├─> Datei suchen (/var/www/html/index.html)
                                       └─> Log schreiben (/var/log/apache2/access.log)
                ←  HTTP-Response  ←
                   HTML-Seite
```

**Was wird geloggt?**
Jeder Zugriff wird in `access.log` gespeichert:
```
93.184.216.34 - - [24/Oct/2025:15:42:18 +0000] "GET / HTTP/1.1" 200 10918
```

Das bedeutet:
- `93.184.216.34` = IP des Besuchers
- `24/Oct/2025:15:42:18` = Zeitpunkt
- `GET /` = Anfrage zur Startseite
- `200` = Erfolg (HTTP-Statuscode)
- `10918` = Größe der Antwort in Bytes

**Warum sind Logs wichtig?**
- Fehlersuche ("Warum funktioniert X nicht?")
- Sicherheit ("Wurde ich angegriffen?")
- Statistiken ("Wie viele Besucher?")
- Compliance (gesetzliche Aufbewahrungspflicht)

### Was ist die AWS CLI?

Die **AWS CLI (Command Line Interface)** ist ein Tool, um AWS-Dienste per Terminal zu steuern.

**Beispiel-Befehle:**
```bash
aws s3 ls                          # Alle Buckets auflisten
aws s3 cp file.txt s3://bucket/    # Datei hochladen
aws ec2 describe-instances         # EC2-Instanzen anzeigen
```

**Warum CLI statt Console (Browser)?**
- Automatisierung (in Skripten)
- Schneller (keine Klickerei)
- Wiederholbar (exakt reproduzierbar)
- Für Cron-Jobs (läuft ohne Mensch)

### Anleitung

Führe folgende Befehle auf der EC2-Instanz aus (du bist per SSH verbunden):

1. System-Pakete aktualisieren:
```bash
sudo apt update && sudo apt upgrade -y
```

2. Apache und AWS CLI installieren:
```bash
sudo apt install -y apache2 unzip curl
```

3. Apache-Status überprüfen:
```bash
sudo systemctl status apache2
```

Du solltest sehen: `Active: active (running)`

Drücke `q` um den Status zu verlassen.

4. Apache-Version anzeigen:
```bash
apache2 -v
```

5. AWS-CLI Installationspaket herunterladen:
```bash
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
```

6. Archiv entpacken:
```bash
unzip awscliv2.zip
```

7. Installation starten:
```bash
sudo ./aws/install
```

8. AWS CLI Version anzeigen:
```bash
aws --version
```

9. Test: Apache Webserver aufrufen (vom EC2 selbst):
```bash
curl http://localhost
```

Du solltest HTML-Code sehen, der mit `<!DOCTYPE html>` beginnt.

10. Test: Apache Webserver von außen aufrufen
- Öffne einen Browser auf deinem Windows-PC
- Gehe zu: `http://<PUBLIC-IP-DEINER-EC2>`
- Du solltest die Standard-Ubuntu-Apache-Seite sehen

11. Logdateien überprüfen:
```bash
ls -lh /var/log/apache2/
```

Du solltest mindestens diese Dateien sehen:
- `access.log` (Zugriffslogs)
- `error.log` (Fehlerlogs)

12. Ein paar Zugriffe erzeugen (damit wir Logs haben):
```bash
for i in {1..20}; do curl -s http://localhost > /dev/null; done
```

13. Logs anschauen:
```bash
sudo tail -n 10 /var/log/apache2/access.log
```

Du siehst jetzt die letzten 10 Zugriffe mit IP, Zeit, angeforderter Seite und Status-Code!

### Checkpoint

**Verstehe, was du erreicht hast:**
- ✅ Apache Webserver läuft und ist öffentlich erreichbar
- ✅ AWS CLI ist installiert und hat durch die IAM-Rolle automatisch Zugriff auf S3
- ✅ Logdateien werden erstellt und gefüllt
- ✅ Alles bereit für das Backup-Skript!

**📸 Screenshot 2 einreichen: Apache läuft**

Mache **einen Screenshot**, der zwei Dinge zeigt:

**Teil 1 - Terminal:**
Zeige die Ausgabe von:
```bash
apache2 -v
aws --version
sudo systemctl status apache2
```
(Apache-Version, AWS-CLI-Version, Status "active")

**Teil 2 - Browser:**
Öffne einen zweiten Browser-Tab und gehe zu `http://<DEINE-PUBLIC-IP>`
Zeige die Apache-Standard-Seite ("Apache2 Ubuntu Default Page")

**Tipp:** Beide Fenster nebeneinander anordnen oder zwei separate Screenshots machen.

---

## Schritt 7: Upload-Skript erstellen

### Was macht das Skript?

Unser Bash-Skript automatisiert drei Aufgaben:

**1. Archivierung (tar + gzip)**
```bash
tar -czf backup.tar.gz /var/log/apache2/
```
- **tar** = Tape Archive (fasst mehrere Dateien zusammen)
- **-c** = create (neu erstellen)
- **-z** = gzip (komprimieren)
- **-f** = file (Ausgabedatei)

**Warum tar.gz und nicht zip?**
- **tar.gz** = Standard unter Linux
- Bessere Kompression (10-30% kleiner)
- Erhält Datei-Berechtigungen
- Unterstützt große Dateien besser

**2. Upload zu S3**
```bash
aws s3 sync /local/ s3://bucket/
```
- Synchronisiert Ordner mit S3
- Lädt nur neue/geänderte Dateien hoch
- Spart Zeit und Traffic

**3. Aufräumen**
```bash
find /archive/ -mtime +14 -delete
```
- Löscht lokale Archive älter als 14 Tage
- Spart Festplattenspeicher auf EC2
- Archive bleiben in S3 (bis Lifecycle-Regel greift)

### Warum als root ausführen?

```bash
sudo -s
```

Wir wechseln zu root, weil:
- `/var/log/apache2/` gehört root (normale User können nicht lesen)
- Cron-Jobs mit root-Rechten sind einfacher zu konfigurieren
- Skript muss in `/opt/` schreiben (System-Ordner)

**Sicherheitshinweis:** In Produktion würdest du einen Service-User mit minimalen Rechten nutzen. Für unsere Demo ist root ok.

### Anleitung

Alle folgenden Befehle werden als root-User ausgeführt:

1. Wechsle zu root:
```bash
sudo -s
```

Dein Prompt sollte sich ändern zu: `root@ip-...#`

2. Arbeitsordner erstellen:
```bash
mkdir -p /opt/logsync /var/log/apache2-archive
```

3. Skript erstellen (wir erstellen es Schritt für Schritt):
```bash
nano /opt/logsync/upload_apache_logs.sh
```

Der nano-Editor öffnet sich. Füge folgenden Inhalt ein:

**Hinweis:** Die `--exclude` Optionen im tar-Befehl verhindern, dass bereits komprimierte Dateien (z.B. durch logrotate) nochmals gezippt werden. Das spart Platz und Upload-Traffic.

```bash
#!/usr/bin/env bash
set -euo pipefail

# WICHTIG: Trage hier deinen Bucket-Namen ein!
BUCKET="DEIN-BUCKET-NAME"

SRC_DIR="/var/log/apache2"
ARCHIVE_DIR="/var/log/apache2-archive"
STAMP="$(date +%Y-%m-%d)"

# 1) Tagesarchiv erzeugen (inkl. aller aktuellen & rotierten Apache-Logs)
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting log archive creation..."
tar -czf "${ARCHIVE_DIR}/apache-logs-${STAMP}.tar.gz" -C "${SRC_DIR}" .
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Archive created: apache-logs-${STAMP}.tar.gz"

# 2) Nach S3 synchronisieren
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Uploading to S3..."
aws s3 sync "${ARCHIVE_DIR}/" "s3://${BUCKET}/logs/" --only-show-errors
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Upload completed"

# Alternative: Nur die heutige Datei hochladen (statt sync)
# aws s3 cp "${ARCHIVE_DIR}/apache-logs-${STAMP}.tar.gz" "s3://${BUCKET}/logs/"

# 3) Lokale Archive älter als 14 Tage löschen
find "${ARCHIVE_DIR}" -type f -name 'apache-logs-*.tar.gz' -mtime +14 -delete
echo "[$(date '+%Y-%m-%d %H:%M:%S')] Cleanup completed"
```

**WICHTIG:** Ersetze `DEIN-BUCKET-NAME` mit deinem echten Bucket-Namen!

Beispiel: Wenn dein Bucket `logs-apache-max-847` heißt, dann:
```bash
BUCKET="logs-apache-max-847"
```

4. Speichern in nano:
- Drücke `Strg + O` (WriteOut)
- Drücke `Enter` (bestätigen)
- Drücke `Strg + X` (Exit)

5. Skript ausführbar machen:
```bash
chmod +x /opt/logsync/upload_apache_logs.sh
```

6. Überprüfen, ob das Skript ausführbar ist:
```bash
ls -lh /opt/logsync/upload_apache_logs.sh
```

Du solltest sehen: `-rwxr-xr-x` (die `x` bedeuten "executable")

7. Skript-Inhalt anzeigen (zur Kontrolle):
```bash
cat /opt/logsync/upload_apache_logs.sh
```

Überprüfe, ob der Bucket-Name korrekt eingetragen ist!

### Verstehe das Skript (Zeile für Zeile)

Lass uns das Skript durchgehen und jede Zeile verstehen:

```bash
#!/usr/bin/env bash
```
**Shebang:** Sagt dem System "führe dieses Skript mit Bash aus"

```bash
set -euo pipefail
```
**Fehlerbehandlung:**
- `-e` = Exit bei Fehler (stoppt bei erstem Problem)
- `-u` = Exit bei undefined variables (fängt Tippfehler)
- `-o pipefail` = Fehler in Pipes beachten

```bash
BUCKET="logs-apache-max-847"
```
**Konfiguration:** Dein S3-Bucket-Name (WICHTIG: anpassen!)

```bash
STAMP="$(date +%Y-%m-%d)"
```
**Datumsstempel:** Erzeugt Format `2025-10-24`
- Sortierbar (älteste Datei zuerst)
- Eindeutig pro Tag

```bash
tar -czf "${ARCHIVE_DIR}/apache-logs-${STAMP}.tar.gz" \
  -C "${SRC_DIR}" . \
  --exclude='*.gz' \
  --exclude='*.old'
```
**Archivierung:**
- `-C` = Change directory (erst wechseln, dann packen)
- `.` = Alle Dateien im aktuellen Ordner
- `--exclude` = Bereits komprimierte Dateien auslassen

```bash
aws s3 sync "${ARCHIVE_DIR}/" "s3://${BUCKET}/logs/" --only-show-errors
```
**Upload:**
- `sync` = Synchronisiert Ordner
- `--only-show-errors` = Keine Ausgabe bei Erfolg (weniger Log-Müll)

```bash
find "${ARCHIVE_DIR}" -type f -name 'apache-logs-*.tar.gz' -mtime +14 -delete
```
**Cleanup:**
- `find` = Suche Dateien
- `-type f` = Nur normale Dateien (keine Ordner)
- `-name` = Passendes Muster
- `-mtime +14` = Älter als 14 Tage
- `-delete` = Löschen

### Checkpoint

Das Skript ist fertig! Es kann jetzt:
- ✅ Logs archivieren
- ✅ Nach S3 hochladen
- ✅ Alte Archive aufräumen
- ✅ Fehler protokollieren

---

## Schritt 8: Skript manuell testen

Bevor wir den Cron-Job einrichten, testen wir das Skript manuell.

### Anleitung

Du bist immer noch als root angemeldet (Prompt: `root@ip-...#`)

1. Skript ausführen:
```bash
/opt/logsync/upload_apache_logs.sh
```

Du solltest folgende Ausgaben sehen:
```
[2025-10-24 XX:XX:XX] Starting log archive creation...
[2025-10-24 XX:XX:XX] Archive created: apache-logs-2025-10-24.tar.gz
[2025-10-24 XX:XX:XX] Uploading to S3...
[2025-10-24 XX:XX:XX] Upload completed
[2025-10-24 XX:XX:XX] Cleanup completed
```

2. Überprüfe, ob das Archiv erstellt wurde:
```bash
ls -lh /var/log/apache2-archive/
```

Du solltest eine Datei wie `apache-logs-2025-10-24.tar.gz` sehen.

3. Überprüfe die Größe des Archivs:
```bash
du -h /var/log/apache2-archive/apache-logs-*.tar.gz
```

4. Überprüfe den Inhalt des Archivs (ohne es zu entpacken):
```bash
tar -tzf /var/log/apache2-archive/apache-logs-*.tar.gz | head -n 20
```

Du solltest Dateien wie `access.log`, `error.log` etc. sehen.

### Checkpoint

**Perfekt!** Das Skript hat funktioniert. Was ist passiert?

1. ✅ Logs wurden in `.tar.gz` gepackt (10-50% der Originalgröße)
2. ✅ Archiv wurde nach S3 hochgeladen
3. ✅ IAM-Rolle hat funktioniert (keine Access Keys nötig!)
4. ✅ Alles wurde protokolliert

**📸 Screenshot 3 einreichen: Upload erfolgreich**

Mache einen Screenshot, der beweist, dass alles funktioniert hat:

**AWS Console - S3:**
1. Gehe zu S3 → dein Bucket → logs/
2. Du solltest eine Datei sehen: `apache-logs-2025-10-24.tar.gz`
3. Screenshot sollte zeigen:
   - Bucket-Namen
   - Ordner `logs/`
   - Die .tar.gz-Datei
   - Datum und Uhrzeit des Uploads
   - Dateigröße

Dieser Screenshot ist der Beweis: Dein automatisches Backup funktioniert!

---

## Schritt 9: Cron-Job einrichten (Automatisierung)

### Was ist Cron?

**Cron** ist der Standard-Task-Scheduler unter Linux (seit 1970er Jahren!). Er führt Befehle zu bestimmten Zeiten automatisch aus.

**Beispiel-Anwendungen:**
- Tägliches Backup um 23:00 Uhr
- Stündliche Website-Überprüfung
- Wöchentliche Datenbank-Bereinigung
- Monatliche Rechnung generieren

**Wie funktioniert Cron?**
```
Cron-Daemon (im Hintergrund)
    ├─> Prüft jede Minute: "Ist es Zeit für einen Job?"
    ├─> Liest Cron-Dateien in /etc/cron.d/
    └─> Führt fällige Jobs aus
```

### Warum /etc/cron.d/ statt crontab?

Es gibt mehrere Wege, Cron-Jobs zu definieren:

**Methode 1: User-Crontab** (nicht genutzt)
```bash
crontab -e  # Bearbeitet Cron-Jobs für aktuellen User
```
- Nachteil: Läuft als User, nicht als root
- Kann nicht auf /var/log/apache2/ zugreifen

**Methode 2: /etc/cron.d/** (unsere Wahl!) ✅
- System-weite Cron-Jobs
- Kann User angeben (`root`)
- Übersichtlich (eine Datei pro Task)
- Überlebt System-Updates

### Cron-Syntax verstehen

Die Zeitangabe in Cron sieht kryptisch aus, ist aber logisch:

```
┌───────────── Minute (0 - 59)
│ ┌─────────── Stunde (0 - 23)
│ │ ┌───────── Tag des Monats (1 - 31)
│ │ │ ┌─────── Monat (1 - 12)
│ │ │ │ ┌───── Wochentag (0 - 7, 0 und 7 = Sonntag)
│ │ │ │ │
* * * * * Befehl

55 23 * * *   →  Jeden Tag um 23:55 Uhr
0 */2 * * *   →  Alle 2 Stunden
0 0 * * 0     →  Jeden Sonntag um Mitternacht
30 6 1 * *    →  Jeden 1. des Monats um 06:30
```

**Warum 23:55 Uhr?**
- Nachts wenig Traffic → Server-Last gering
- Vor Mitternacht → Logs des aktuellen Tages sind komplett
- Nicht genau Mitternacht → vermeidet "Mitternachts-Rush" (viele Jobs laufen oft um 00:00)

### Anleitung

Du bist immer noch als root auf der EC2-Instanz.

1. Cron-Job-Datei erstellen:
```bash
nano /etc/cron.d/apache-logsync
```

2. Füge folgenden Inhalt ein:
```
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Täglich um 23:55 Uhr (UTC): Logs archivieren und hochladen
55 23 * * * root /opt/logsync/upload_apache_logs.sh >> /var/log/logsync.log 2>&1

```

**Wichtig:** Die Uhrzeit ist in **UTC** (koordinierte Weltzeit), da EC2-Instanzen standardmäßig auf UTC laufen.
- 23:55 UTC = 01:55 Uhr deutsche Zeit (im Sommer)
- 23:55 UTC = 00:55 Uhr deutsche Zeit (im Winter)

**Erklärung der Cron-Syntax:**
- `55` = Minute (55)
- `23` = Stunde (23 Uhr)
- `* * *` = jeden Tag, jeden Monat, jeden Wochentag
- `root` = wird als root-User ausgeführt
- `>> /var/log/logsync.log 2>&1` = Ausgabe und Fehler in Logdatei schreiben

**Aktuelle UTC-Zeit anzeigen:**
```bash
date -u
```

3. Speichern in nano:
- Drücke `Strg + O` (WriteOut)
- Drücke `Enter` (bestätigen)
- Drücke `Strg + X` (Exit)

**Wichtig:** Die Datei muss mit einer Leerzeile enden (siehe oben im Code-Block)

4. Cron-Job verifizieren:
```bash
cat /etc/cron.d/apache-logsync
```

5. Überprüfe, dass die Datei mit einer Newline endet:
```bash
tail -c 1 /etc/cron.d/apache-logsync | od -An -tx1
```
Sollte `0a` ausgeben (= Newline vorhanden)

6. Cron-Job-Datei muss die richtigen Berechtigungen haben:
```bash
chmod 644 /etc/cron.d/apache-logsync
ls -l /etc/cron.d/apache-logsync
```
Sollte zeigen: `-rw-r--r--` (= 644 Berechtigungen)

7. Cron-Dienst neu laden (nicht unbedingt nötig, aber sicher ist sicher):
```bash
systemctl restart cron
```

8. Cron-Status überprüfen:
```bash
systemctl status cron
```

Du solltest sehen: `Active: active (running)`

Drücke `q` zum Beenden.

### Cron-Job testen (ohne zu warten)

Da wir nicht bis 23:55 Uhr warten wollen, ändern wir den Cron-Job temporär für einen Test:

1. Aktuelle Uhrzeit anzeigen:
```bash
date
```

Beispiel-Ausgabe: `Fri Oct 24 15:42:30 UTC 2025`

2. Cron-Job anpassen (für Test in 2 Minuten):
```bash
nano /etc/cron.d/apache-logsync
```

Ändere die Zeit-Zeile. Wenn es jetzt z.B. 15:42 Uhr ist, setze:
```
44 15 * * * root /opt/logsync/upload_apache_logs.sh >> /var/log/logsync.log 2>&1
```

(2 Minuten später als aktuelle Uhrzeit)

3. Speichern: `Strg + O` → `Enter` → `Strg + X`

4. Warte 2-3 Minuten

5. Logdatei überprüfen:
```bash
tail -n 50 /var/log/logsync.log
```

Du solltest die Ausgabe deines Skripts sehen mit Zeitstempeln.

6. Prüfe, ob ein neues Archiv erstellt wurde:
```bash
ls -lt /var/log/apache2-archive/ | head -n 5
```

7. Prüfe S3 (du solltest jetzt 2 Dateien haben):
```bash
aws s3 ls s3://DEIN-BUCKET-NAME/logs/
```

### Cron-Job zurück auf 23:55 Uhr setzen

1. Öffne die Cron-Datei wieder:
```bash
nano /etc/cron.d/apache-logsync
```

2. Ändere zurück auf:
```
55 23 * * * root /opt/logsync/upload_apache_logs.sh >> /var/log/logsync.log 2>&1
```

3. Speichern und beenden

### Checkpoint - Der große Moment!

Du hast soeben **vollständige Automatisierung** erreicht! Ab jetzt:

- ✅ Läuft das Backup täglich um 23:55 Uhr (UTC) ohne dein Zutun
- ✅ Logs werden komprimiert und sicher in S3 gespeichert
- ✅ Alte lokale Archive werden automatisch gelöscht
- ✅ Alles wird protokolliert

**📸 Screenshot 4 einreichen: Cron-Job funktioniert**

Zeige in der **S3-Console**, dass der Cron-Job tatsächlich automatisch gelaufen ist:

1. Gehe zu S3 → dein Bucket → logs/
2. Du solltest jetzt **mindestens 2 Dateien** sehen:
   - Eine von deinem manuellen Test (vor Schritt 9)
   - Eine vom automatischen Cron-Job
3. Screenshot sollte zeigen:
   - Beide .tar.gz-Dateien
   - Unterschiedliche Upload-Zeiten (beweist: automatisch!)
   - Dateigröße bei beiden

**Bonus:** Zeige zusätzlich im Terminal:
```bash
sudo tail -n 20 /var/log/logsync.log
```

Du solltest mehrere Einträge mit Zeitstempeln sehen - Beweis für automatische Ausführung!

---

## Schritt 10: Optional - Erweiterte Konzepte

### Mehr Traffic erzeugen

Um mehr Logdaten zu generieren, erzeugen wir zusätzlichen Traffic.

### Optional: Upload-Pfad pro Host trennen

Wenn du mehrere EC2-Instanzen hast, kannst du die Logs pro Server trennen:

1. Öffne das Skript:
```bash
sudo nano /opt/logsync/upload_apache_logs.sh
```

2. Ändere die Zeile mit `aws s3 sync`:
```bash
# Vorher:
aws s3 sync "${ARCHIVE_DIR}/" "s3://${BUCKET}/logs/" --only-show-errors

# Nachher (mit Hostname):
aws s3 sync "${ARCHIVE_DIR}/" "s3://${BUCKET}/logs/$(hostname)/" --only-show-errors
```

3. Speichern und testen

Jetzt landen die Logs in `s3://dein-bucket/logs/ip-172-31-xx-xx/`

### Mehr Traffic erzeugen

Um mehr Logdaten zu generieren, erzeugen wir zusätzlichen Traffic.

### Anleitung

Auf der EC2-Instanz:

1. Traffic von der EC2-Instanz selbst erzeugen:
```bash
for i in {1..100}; do curl -s http://localhost > /dev/null; echo "Request $i sent"; done
```

2. Überprüfe die Größe der Logdatei:
```bash
ls -lh /var/log/apache2/access.log
```

3. Zeige die letzten 20 Einträge:
```bash
sudo tail -n 20 /var/log/apache2/access.log
```

4. Von deinem Windows-PC aus (PowerShell):
```powershell
1..50 | ForEach-Object { 
    Invoke-WebRequest -Uri "http://<PUBLIC-IP>" -Method GET -UseBasicParsing
    Write-Host "Request $_ completed"
}
```

Ersetze `<PUBLIC-IP>` mit der Public IP deiner EC2-Instanz.

---

## Schritt 11: Optionale Alternativen

### Alternative ohne AWS CLI (nur AWS Console)

Falls die AWS CLI Probleme macht, kannst du Dateien auch manuell hochladen.

### Variante A: Einfacherer Upload-Befehl (nur heutige Datei)

Wenn du das Skript vereinfachen möchtest, kannst du statt `aws s3 sync` auch `aws s3 cp` verwenden:

1. Öffne das Skript:
```bash
sudo nano /opt/logsync/upload_apache_logs.sh
```

2. Ersetze die Zeile mit `aws s3 sync` durch:
```bash
# Nur die heutige Datei hochladen (einfacher zu verstehen)
aws s3 cp "${ARCHIVE_DIR}/apache-logs-${STAMP}.tar.gz" "s3://${BUCKET}/logs/"
```

**Unterschied:**
- `sync`: Lädt alle Dateien im Ordner hoch, die noch nicht in S3 sind
- `cp`: Lädt nur diese eine Datei hoch

**Vorteil von sync:** Falls ein Upload mal fehlschlägt, wird die Datei beim nächsten Mal nachgeholt.

### Variante B: Manueller Upload über AWS Console

### Anleitung

1. Auf der EC2-Instanz das Archiv erstellen (ohne Upload):
```bash
sudo tar -czf /tmp/apache-logs-manual.tar.gz -C /var/log/apache2 .
```

2. Archiv herunterladen mit SCP (von deinem Windows-PC):

**PowerShell:**
```powershell
scp -i apache-log-key.pem ubuntu@<PUBLIC-IP>:/tmp/apache-logs-manual.tar.gz ./
```

**WSL:**
```bash
scp -i ~/apache-log-key.pem ubuntu@<PUBLIC-IP>:/tmp/apache-logs-manual.tar.gz ~/
```

3. In AWS Console:
   - Gehe zu S3 → dein Bucket → logs/
   - Klicke **Upload**
   - Klicke **Add files**
   - Wähle `apache-logs-manual.tar.gz`
   - Klicke **Upload**

Diese Methode funktioniert immer, ist aber nicht automatisiert.

---

## Schritt 12: IAM-Rolle testen (Mini-Challenge)

Teste, ob die IAM-Berechtigungen wirklich eingeschränkt sind.

### Was lernen wir hier?

Diese Tests zeigen dir, dass **Least Privilege** wirklich funktioniert:
- Dein Server kann nur auf SEINEN Bucket zugreifen
- Nicht auf andere Buckets
- Nicht auf andere AWS-Services

Das ist wichtig für Sicherheit: Bei einer Kompromittierung ist der Schaden begrenzt!

### Test 1: Policy entfernen und testen

1. In AWS Console → IAM → Roles → EC2-S3-LogUploader
2. Unter Permissions, wähle die Policy und klicke **Remove**
3. Auf EC2-Instanz, führe aus:
```bash
sudo /opt/logsync/upload_apache_logs.sh
```

Erwartetes Ergebnis: Fehler `AccessDenied`

4. Policy wieder hinzufügen in IAM Console
5. Warte 1-2 Minuten
6. Skript erneut ausführen - sollte jetzt funktionieren

### Test 2: Anderen Bucket zugreifen

Versuche auf einen Bucket zuzugreifen, für den du keine Berechtigung hast:

```bash
aws s3 ls s3://aws-logs/
```

Erwartetes Ergebnis: `An error occurred (AccessDenied)`

Das zeigt, dass deine Rolle wirklich nur Zugriff auf deinen spezifischen Bucket hat (Least Privilege Principle).

**Perfekt!** Diese Fehlermeldung ist eigentlich ein **Erfolg** - sie beweist, dass die Sicherheit funktioniert!

---

## Schritt 13: CloudWatch Logs (Optional - Fortgeschritten)

Richte CloudWatch Logs ein, um die Logs auch in AWS CloudWatch zu streamen.

### Anleitung

1. CloudWatch Agent installieren:
```bash
wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
sudo dpkg -i amazon-cloudwatch-agent.deb
```

2. Konfigurationsdatei erstellen:
```bash
sudo nano /opt/aws/amazon-cloudwatch-agent/etc/config.json
```

Inhalt:
```json
{
  "logs": {
    "logs_collected": {
      "files": {
        "collect_list": [
          {
            "file_path": "/var/log/apache2/access.log",
            "log_group_name": "/aws/ec2/apache-logs",
            "log_stream_name": "{instance_id}-access"
          }
        ]
      }
    }
  }
}
```

3. Agent starten:
```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
  -a fetch-config \
  -m ec2 \
  -s \
  -c file:/opt/aws/amazon-cloudwatch-agent/etc/config.json
```

4. In AWS Console → CloudWatch → Logs → Log groups
   - Du solltest `/aws/ec2/apache-logs` sehen

Dies erfordert zusätzliche IAM-Berechtigungen (CloudWatchAgentServerPolicy).

---

## Troubleshooting

### Problem: SSH-Verbindung schlägt fehl

**Symptom:** `Connection refused` oder `Connection timed out`

**Lösungen:**
1. Überprüfe, ob die Instanz läuft (Instance State: Running)
2. Überprüfe die Security Group: Port 22 muss für deine IP geöffnet sein
3. Überprüfe, ob du die richtige Public IP verwendest
4. Überprüfe die Key-Berechtigungen (siehe Schritt 5)

### Problem: AWS CLI funktioniert nicht auf EC2

**Symptom:** `aws: command not found`

**Lösung:**
```bash
sudo apt update
sudo apt install -y awscli
aws --version
```

### Problem: 403 AccessDenied beim S3-Upload

**Symptom:** `An error occurred (403) when calling the PutObject operation: Access Denied`

**Lösungen:**
1. Überprüfe, ob die IAM-Rolle der EC2-Instanz zugewiesen ist
   - EC2 Console → Instanz auswählen → Actions → Security → Modify IAM role
2. Überprüfe den Bucket-Namen im Skript (Tippfehler?)
3. Überprüfe die IAM-Policy: ARN muss korrekt sein
4. Warte 1-2 Minuten nach Policy-Änderungen (Propagation)

### Problem: Cron-Job läuft nicht

**Symptom:** Keine neuen Dateien in S3, keine Einträge in `/var/log/logsync.log`

**Lösungen:**
1. Überprüfe Cron-Status:
```bash
systemctl status cron
```

2. Überprüfe Syntax der Cron-Datei:
```bash
cat /etc/cron.d/apache-logsync
```

3. Überprüfe Berechtigungen:
```bash
ls -l /etc/cron.d/apache-logsync
```
Sollte sein: `-rw-r--r--`

4. Manuell testen:
```bash
sudo /opt/logsync/upload_apache_logs.sh
```

5. Cron-Logs prüfen:
```bash
sudo grep CRON /var/log/syslog | tail -n 20
```

### Problem: Skript schlägt fehl mit "command not found"

**Symptom:** `/opt/logsync/upload_apache_logs.sh: line X: aws: command not found`

**Lösung:**
Der PATH in der Cron-Datei muss korrekt sein:
```bash
sudo nano /etc/cron.d/apache-logsync
```

Erste Zeilen müssen sein:
```
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

### Problem: Bucket-Name enthält Tippfehler

**Lösung:**
```bash
sudo nano /opt/logsync/upload_apache_logs.sh
```

Korrigiere die BUCKET-Variable und speichere.

### Problem: Apache-Logs sind leer

**Lösung:**
Traffic erzeugen:
```bash
for i in {1..50}; do curl -s http://localhost > /dev/null; done
```

---

## Projekt-Aufräumen (nach Abschluss)

Wenn du das Projekt abgeschlossen hast und die Ressourcen nicht mehr benötigst:

### EC2-Instanz terminieren

1. EC2 Console → Instances
2. Wähle deine Instanz aus
3. Instance state → Terminate instance
4. Bestätige mit "Terminate"

**ACHTUNG:** Alle Daten auf der Instanz gehen verloren!

### S3-Bucket aufräumen

**Option 1: Bucket leeren (behalten)**
1. S3 Console → dein Bucket → logs/
2. Wähle alle Dateien aus
3. Delete

**Option 2: Bucket komplett löschen**
1. S3 Console → dein Bucket
2. Empty bucket (alle Objekte löschen)
3. Dann: Delete bucket

### IAM-Rolle und Policy (optional behalten)

Diese können für zukünftige Projekte wiederverwendet werden.

Zum Löschen:
1. IAM Console → Roles → EC2-S3-LogUploader → Delete
2. IAM Console → Policies → S3-LogUpload-Policy → Delete

### Security Group (optional behalten)

Kann wiederverwendet werden.

Zum Löschen:
1. EC2 Console → Security Groups
2. Wähle `apache-ssh-access`
3. Actions → Delete security groups

---

## Zusammenfassung und Reflexion

### Was hast du erreicht?

Herzlichen Glückwunsch! Du hast ein vollständig automatisiertes Cloud-Backup-System gebaut. Das ist keine triviale Leistung - viele Unternehmen nutzen genau diese Architektur in Produktion!

**Konkret hast du:**

 **Infrastructure as Code (IaC) verstanden**
- Manuelle Klicks in AWS Console
- In der Praxis: Terraform, CloudFormation
- Reproduzierbar und dokumentiert

 **Cloud-Computing genutzt**
- EC2: Virtuelle Server on-demand
- S3: Unbegrenzter Cloud-Speicher
- Pay-as-you-go statt große Investition

 **Sicherheits-Best-Practices angewendet**
- IAM-Rollen statt Access Keys
- Least Privilege Principle
- Verschlüsselung at rest (SSE-S3)
- Security Groups als Firewall

 **Linux-Administration gelernt**
- Package Management (apt)
- Service Management (systemd)
- Bash Scripting
- Cron Jobs

 **Automatisierung implementiert**
- Zeitgesteuerte Aufgaben
- Fehlerbehandlung
- Logging für Debugging

### Was würde in Produktion anders sein?

Diese Demo ist didaktisch vereinfacht. In einem echten Produktions-Setup würdest du ergänzen:

**Sicherheit:**
-  HTTPS (Port 443) statt HTTP (Port 80)
-  SSL-Zertifikat (Let's Encrypt oder AWS Certificate Manager)
-  Private Subnet für EC2 (nicht direkt im Internet)
-  Bastion Host für SSH-Zugriff
-  Service-User statt root
-  KMS-Verschlüsselung für S3 (statt SSE-S3)
-  MFA für AWS Console

**Verfügbarkeit:**
-  Multi-AZ Deployment (mehrere Rechenzentren)
-  Auto Scaling Group (automatisch mehr/weniger Server)
-  Load Balancer (verteilt Traffic)
-  CloudWatch Alarms (Benachrichtigung bei Problemen)
-  Echtzeit-Log-Streaming

**Monitoring:**
-  CloudWatch Dashboards
-  SNS für Alerts (E-Mail/SMS)
-  Log-Analyse mit CloudWatch Insights
-  Prometheus + Grafana für Metriken

**Automatisierung:**
-  Infrastructure as Code (Terraform)
-  CI/CD Pipeline (GitHub Actions, GitLab CI)
-  Automated Testing
-  Blue-Green Deployment

**Backup:**
-  Cross-Region Replication (Disaster Recovery)
-  S3 Versioning (Schutz vor versehentlichem Löschen)
-  S3 Glacier für Langzeitarchivierung (günstiger)
-  Backup-Tests (regelmäßig Restore prüfen!)


---

## Checkliste für diese Selbstlernaufgabe

### Grundlagen verstanden
- [ ] Ich verstehe, was S3 ist und wie Object Storage funktioniert
- [ ] Ich verstehe den Unterschied zwischen IAM-Rollen und Access Keys
- [ ] Ich verstehe, was EC2 ist und wie virtuelle Server funktionieren
- [ ] Ich verstehe, was Security Groups machen

### AWS-Ressourcen erstellt
- [ ] S3-Bucket erstellt (privat, verschlüsselt)
- [ ] IAM-Rolle mit Policy erstellt (Least Privilege)
- [ ] Security Group konfiguriert (SSH + HTTP)
- [ ] EC2-Instanz gestartet mit korrekter IAM-Rolle

### Linux-Administration
- [ ] SSH-Verbindung hergestellt
- [ ] Apache Webserver installiert und getestet
- [ ] AWS CLI installiert und getestet
- [ ] Bash-Skript erstellt und verstanden
- [ ] Cron-Job eingerichtet

### Automatisierung funktioniert
- [ ] Skript manuell erfolgreich getestet
- [ ] Upload in S3 verifiziert
- [ ] Cron-Job läuft automatisch
- [ ] Logs werden protokolliert

### Screenshots eingereicht
- [ ] **Screenshot 1:** EC2-Instanz läuft mit korrekter Konfiguration
- [ ] **Screenshot 2:** Apache läuft + AWS CLI installiert
- [ ] **Screenshot 3:** Erste erfolgreiche S3-Upload nach manuellem Test
- [ ] **Screenshot 4:** Mindestens 2 Dateien in S3 (automatischer Cron-Job läuft)

### Bonuspunkte (Optional)
- [ ] IAM-Rolle getestet (AccessDenied bei anderem Bucket)
- [ ] Upload-Pfad pro Host getrennt (hostname im Pfad)
- [ ] Mehr Traffic generiert
- [ ] Lifecycle Rule in S3 konfiguriert
- [ ] CloudWatch Logs eingerichtet

---

## Häufig gestellte Fragen (FAQ)

**Q: Muss ich die EC2-Instanz laufen lassen?**
A: Nur solange du das Projekt testest. Danach solltest du sie terminieren, um Kosten zu vermeiden.

**Q: Wie lange dauert es, bis der Cron-Job läuft?**
A: Cron überprüft jede Minute, ob Jobs anstehen. Dein Job läuft dann zu der konfigurierten Zeit (23:55 Uhr).

**Q: Was passiert, wenn der Upload fehlschlägt?**
A: Der Fehler wird in `/var/log/logsync.log` protokolliert. Das Archiv bleibt auf der EC2-Instanz und wird beim nächsten erfolgreichen Lauf hochgeladen.

**Q: Kann ich mehrere EC2-Instanzen denselben Bucket verwenden lassen?**
A: Ja! Ändere im Skript den Upload-Pfad zu: `s3://${BUCKET}/logs/$(hostname)/` - so sind die Logs pro Server getrennt.

**Q: Wie viel kostet das?**
A: Mit t2.micro (Free Tier) und geringen Datenmengen: praktisch kostenlos für 12 Monate (Free Tier). Danach: wenige Cent pro Monat.

**Q: Kann ich andere Logs auch hochladen?**
A: Ja! Passe einfach die Variable `SRC_DIR` im Skript an, z.B. `/var/log/nginx/` für Nginx.

**Q: Was ist der Unterschied zwischen `aws s3 sync` und `aws s3 cp`?**
A: 
- `sync` lädt nur neue/geänderte Dateien hoch (effizienter, vergleicht Größe und Zeitstempel)
- `cp` lädt die angegebene Datei immer hoch, auch wenn sie bereits existiert
- Für dieses Projekt: `sync` ist besser, weil mehrere Archive im Ordner liegen
- Alternative: Wenn du nur die heutige Datei hochladen willst, reicht `cp` (siehe Kommentar im Skript)

---

**Ende der Anleitung**

Bei Fragen oder Problemen, nutze die Troubleshooting-Sektion oder schreibt mir bei Slack!
