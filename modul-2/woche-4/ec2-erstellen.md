# AWS EC2 Instance mit nginx - Praktische Übung

## Schritt-für-Schritt-Anleitung für Windows 11

### Voraussetzungen
- AWS Account (mit aktiviertem Free Tier)
- Windows 11 Rechner mit integriertem SSH-Client
- Internetverbindung
- Browser (Chrome, Firefox, Edge)
- Ca. 60-90 Minuten Zeit

---

## Teil 1: EC2 Instance starten

### 1.1 In die AWS Console einloggen

1. Öffne deinen Browser und gehe zu: https://sandboxes.techstarter.de/
2. Logge dich mit deinem AWS Account ein

### 1.2 Zur EC2-Konsole navigieren

1. Oben in der Suchleiste: Tippe **"EC2"** ein
2. Klicke auf **"EC2"** (mit dem orangenen Logo)
3. Du bist jetzt im EC2 Dashboard

**Wichtig:** Prüfe oben rechts die Region! Wähle am besten **"eu-central-1" (Frankfurt)** aus dem Dropdown-Menü.

### 1.3 Instance starten

1. Klicke auf den orangenen Button **"Launch instance"** (oder "Instance starten")
2. Du siehst jetzt das "Launch an instance" Formular

### 1.4 Name und Tags vergeben

1. Bei **"Name and tags"**: Gib einen Namen ein, z.B. `mein-webserver-test`
2. Die Tags werden automatisch erstellt - das kannst du so lassen

### 1.5 AMI (Betriebssystem) auswählen

1. Scrolle zu **"Application and OS Images (Amazon Machine Image)"**
2. **Wichtig:** Stelle sicher, dass **"Ubuntu"** ausgewählt ist
3. Wähle: **"Ubuntu Server 22.04 LTS (HVM), SSD Volume Type"**
   - **LTS** = Long Term Support (unterstützt bis April 2027)
4. **Prüfe:** Es sollte "Free tier eligible" dabei stehen (grünes Label)
5. Architektur: **"64-bit (x86)"** sollte ausgewählt sein
6. **Alternative:** "Ubuntu Server 24.04 LTS" funktioniert auch (neueste Version)

### 1.6 Instance Type wählen

1. Scrolle zu **"Instance type"**
2. **Wichtig:** Wähle **"t2.micro"** oder **"t3.micro"**
   - Das ist der Free Tier!
   - 1 vCPU, 1 GB RAM
3. Falls ein anderer Type vorausgewählt ist, klicke auf das Dropdown und wähle `t2.micro`

### 1.7 Key Pair erstellen (sehr wichtig!)

1. Scrolle zu **"Key pair (login)"**
2. Klicke auf **"Create new key pair"**
3. Ein Popup öffnet sich:
   - **Key pair name:** `mein-ec2-key` (oder einen Namen deiner Wahl)
   - **Key pair type:** Wähle **"RSA"**
   - **Private key file format:** Wähle **".pem"**
4. Klicke auf **"Create key pair"**

**Was passiert jetzt:**
- Eine Datei `mein-ec2-key.pem` wird automatisch heruntergeladen
- **WICHTIG:** Diese Datei ist dein Schlüssel zum Server!
- Verschiebe die Datei an einen sicheren Ort, z.B. `C:\Users\DeinName\aws-keys\`
- **NICHT umbenennen!** Merke dir den exakten Dateinamen für später

### 1.8 Network Settings (Firewall)

1. Scrolle zu **"Network settings"**
2. Klicke auf **"Edit"** (rechts oben in diesem Bereich)
   - **Hinweis:** Bei manchen ist dieser Bereich schon aufgeklappt - dann einfach weitermachen
3. Bei **"Firewall (security groups)"**: Wähle **"Create security group"**
4. **Security group name:** Lasse den automatischen Namen oder gib ein: `webserver-sg`
5. **Description:** `Webserver Security Group`

**Wichtig - Jetzt die Regeln einstellen:**

6. Du siehst bereits eine Regel für SSH:
   - Type: **SSH**
   - Port: **22**
   - Source type: Ändere zu **"My IP"** (das ist sicherer!)
   - **Hinweis:** Falls du von zu Hause arbeitest und deine IP sich ändert (DSL-Router Neustart), musst du später die Security Group anpassen
   
7. Klicke auf **"Add security group rule"** (um eine zweite Regel hinzuzufügen)
   - Type: Wähle aus dem Dropdown **"HTTP"**
   - Port: **80** (wird automatisch gesetzt)
   - Source type: **"Anywhere"** oder **"0.0.0.0/0"**
   - Beschreibung (optional): `Allow HTTP traffic`

**Warum machen wir das?**
- SSH (Port 22): Damit du dich mit dem Server verbinden kannst
- HTTP (Port 80): Damit später der Webserver erreichbar ist

### 1.9 Storage (Speicher)

1. Scrolle zu **"Configure storage"**
2. Lasse alles auf Standard:
   - **8 GB** (gp3 oder gp2) Root volume
   - Beides (gp2/gp3) ist im Free Tier enthalten
   - gp3 ist neuer und etwas schneller

### 1.10 Advanced Details (überspringen)

- Scrolle einfach weiter, hier musst du nichts ändern

### 1.11 Instance starten!

1. Scrolle ganz nach unten
2. Auf der rechten Seite siehst du eine Zusammenfassung
3. **Prüfe nochmal:**
   - Instance type: **t2.micro**
   - Key pair: **mein-ec2-key** (oder dein gewählter Name)
4. Klicke auf den orangenen Button **"Launch instance"**

5. Du siehst jetzt: **"Successfully initiated launch of instance"**
6. Klicke auf **"View all instances"**

**Herzlichen Glückwunsch!** Deine Instance startet jetzt! 🎉

---

## Teil 2: Auf die Instance per SSH verbinden

### ⚠️ WICHTIG VORAB - Häufigster Fehler vermeiden!

**Bevor du weitermachst:**
1. Prüfe den **exakten Dateinamen** deiner .pem Datei (z.B. `mein-key.pem`)
2. Verwende **immer** diesen exakten Namen in allen Befehlen
3. **Häufiger Fehler:** Datei heißt `ec2-ssh.pem`, aber du schreibst `ssh-ec2.pem` → Das funktioniert nicht!

---

### 2.1 Warten bis die Instance läuft

1. Im EC2 Dashboard unter **"Instances"** siehst du deine Instance
2. **Instance State:** Warte bis dort **"Running"** (grün) steht
3. **Status checks:** Warte bis **"2/2 checks passed"** steht (dauert 1-2 Minuten)

### 2.2 Public IP-Adresse notieren

1. Klicke auf deine Instance (Checkbox links anklicken oder auf die Instance-ID klicken)
2. Unten öffnen sich die **Details**
3. Suche nach **"Public IPv4 address"**
4. Notiere dir diese IP-Adresse, z.B. `3.121.45.189`

### 2.3 SSH-Key vorbereiten (Windows)

**Windows 11 hat SSH bereits integriert!**

1. Öffne den **Windows Explorer**
2. Navigiere zu dem Ordner, wo deine `.pem` Datei liegt (z.B. `C:\Users\DeinName\Downloads\`)
3. **Prüfe den exakten Dateinamen!** Z.B. `mein-ec2-key.pem`
4. Klicke mit der **rechten Maustaste** in den leeren Bereich des Ordners
5. Wähle **"In Terminal öffnen"** (oder "Open in Windows Terminal")
   - Es öffnet sich PowerShell direkt in diesem Ordner

**Wichtig - Key-Berechtigungen setzen:**

6. Im PowerShell-Fenster, tippe die folgenden Befehle **einen nach dem anderen** (ersetze `mein-ec2-key.pem` mit deinem **exakten** Dateinamen):

```powershell
icacls "mein-ec2-key.pem" /reset
```

Drücke Enter, dann:

```powershell
icacls "mein-ec2-key.pem" /inheritance:r
```

Drücke Enter, dann:

```powershell
icacls "mein-ec2-key.pem" /grant:r "$($env:USERNAME):(R)"
```

**Was macht das?**
- `/reset` = Alle bestehenden Berechtigungen entfernen
- `/inheritance:r` = Vererbung von übergeordneten Ordnern entfernen  
- `/grant:r` = NUR dir Leserechte geben
- Linux/AWS verlangt, dass der Key nur von dir lesbar ist

7. **Prüfe die Berechtigungen** (sollte nur dein Username da stehen):

```powershell
icacls "mein-ec2-key.pem"
```

Du solltest sehen: `mein-ec2-key.pem DEIN-PC\dein-username:(R)`

**Falls noch andere Benutzer aufgelistet sind**, wiederhole die Schritte nochmal von Anfang!

### 2.4 SSH-Verbindung herstellen

1. Im gleichen PowerShell-Fenster, tippe (ersetze `mein-ec2-key.pem` mit deinem **exakten** Dateinamen und die IP-Adresse mit deiner eigenen):

```bash
ssh -i mein-ec2-key.pem ubuntu@3.121.45.189
```

**WICHTIG:** Der Dateiname muss **exakt** übereinstimmen!
- Wenn deine Datei `ec2-ssh.pem` heißt, schreibe: `ssh -i ec2-ssh.pem ubuntu@...`
- Wenn deine Datei `ssh-ec2.pem` heißt, schreibe: `ssh -i ssh-ec2.pem ubuntu@...`

**Erklärung des Befehls:**
- `ssh`: Das SSH-Programm
- `-i mein-ec2-key.pem`: Verwende diesen Key
- `ubuntu`: Der Benutzername (bei Ubuntu AMI ist das immer "ubuntu")
- `@3.121.45.189`: Deine Server-IP-Adresse

2. Beim **ersten** Mal verbinden erscheint:
```
The authenticity of host '3.121.45.189' can't be established...
Are you sure you want to continue connecting (yes/no)?
```

3. Tippe **`yes`** und drücke Enter

4. Du solltest jetzt verbunden sein! Du siehst so etwas wie:

```
Welcome to Ubuntu 22.04.3 LTS...
ubuntu@ip-172-31-xx-xx:~$
```

**Du bist jetzt auf deinem Server in der Cloud!** 🎉

---

## Teil 3: nginx installieren

### 3.1 System aktualisieren

1. Im SSH-Terminal, tippe:

```bash
sudo apt update
```

Drücke Enter und warte, bis der Befehl durchgelaufen ist.

**Was macht das?**
- Aktualisiert die Paketliste
- `sudo` = als Administrator ausführen
- `apt` = Paketmanager von Ubuntu

### 3.2 nginx installieren

2. Tippe:

```bash
sudo apt install nginx -y
```

**Was macht das?**
- Installiert den nginx Webserver
- `-y` = automatisch "ja" sagen zu allen Fragen

Die Installation dauert ca. 30 Sekunden.

### 3.3 nginx-Status prüfen

3. Prüfe, ob nginx läuft:

```bash
sudo systemctl status nginx
```

Du solltest sehen: **"active (running)"** in grün.

4. Drücke **`q`** um zurück zum Terminal zu kommen

### 3.4 nginx starten (falls nicht läuft)

Falls nginx nicht läuft, starte ihn:

```bash
sudo systemctl start nginx
```

---

## Teil 4: Im Browser testen

### 4.1 Webserver aufrufen

1. Öffne einen **neuen Tab** in deinem Browser
2. Gib deine **Public IP-Adresse** ein: `http://3.121.45.189`
   - Achte darauf: **http://** (nicht https!)
   - Ersetze die IP mit deiner eigenen IP-Adresse

3. **Du solltest die nginx Willkommensseite sehen!**
   - Große Überschrift: "Welcome to nginx!"

**Glückwunsch! Dein Webserver läuft!** 🎉

---

## Teil 5: Eigene Webseite erstellen (Bonus)

### 5.1 HTML-Datei erstellen

Zurück im SSH-Terminal:

1. Erstelle eine neue HTML-Datei:

```bash
sudo nano /var/www/html/index.html
```

2. Der `nano` Editor öffnet sich. Lösche den alten Inhalt (mit Pfeiltasten navigieren und `Backspace`/`Entf` zum Löschen)

3. Kopiere folgenden HTML-Code rein:

```html
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mein AWS Webserver</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
        }
        h1 {
            font-size: 3em;
            margin-bottom: 20px;
        }
        p {
            font-size: 1.2em;
        }
        .box {
            background: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>🚀 Mein erster AWS Server!</h1>
        <p>Dieser Webserver läuft auf einer EC2 Instance in der AWS Cloud.</p>
        <p>Betrieben mit Ubuntu 22.04 und nginx.</p>
        <p><strong>Es funktioniert! 🎉</strong></p>
    </div>
</body>
</html>
```

4. Speichern:
   - Drücke **`Strg + O`** (der Buchstabe O)
   - Drücke **`Enter`** zum Bestätigen
   - Drücke **`Strg + X`** zum Beenden

5. Aktualisiere deinen Browser (F5) - du siehst jetzt deine eigene Seite!

---

## Teil 6: Instance stoppen (WICHTIG!)

### 6.1 SSH-Verbindung beenden

Im Terminal:

```bash
exit
```

Du bist jetzt wieder auf deinem lokalen Windows-Computer.

### 6.2 Instance in AWS stoppen

1. Zurück in der **AWS Console** → **EC2** → **Instances**
2. Wähle deine Instance aus (Checkbox anklicken)
3. Oben rechts: Klicke auf **"Instance state"**
4. Wähle **"Stop instance"**
5. Im Popup: Klicke auf **"Stop"**

**Warum stoppen?**
- Gestoppte Instances verbrauchen keine Compute-Stunden
- Du bleibst im Free Tier (750h/Monat für ALLE deine Instances zusammen)
- Deine Daten bleiben erhalten!
- **Wichtig:** Wenn du 2 Instances gleichzeitig laufen lässt, verbrauchst du 2h pro Stunde!

**NICHT terminate wählen!** Das würde alles unwiderruflich löschen.

---

## Teil 7: Instance später wieder starten

Wenn du später weitermachen willst:

1. In **EC2** → **Instances**
2. Instance auswählen
3. **"Instance state"** → **"Start instance"**
4. Warte bis **"Running"**
5. **Wichtig:** Die Public IP hat sich geändert!
6. Notiere die neue IP
7. Verbinde dich mit SSH mit der **neuen IP-Adresse**

---

## Troubleshooting - Häufige Probleme

### Problem 1: "Permission denied" oder "Bad permissions" beim SSH

**Symptom:** 
```
WARNING: UNPROTECTED PRIVATE KEY FILE!
Permissions for 'datei.pem' are too open.
Bad permissions. Try removing permissions for user: ...
```

**Lösung 1 - Key-Berechtigungen richtig setzen:**

Öffne PowerShell im Ordner der .pem Datei und führe diese Befehle aus:

```powershell
icacls "dein-key.pem" /reset
icacls "dein-key.pem" /inheritance:r
icacls "dein-key.pem" /grant:r "$($env:USERNAME):(R)"
```

**Prüfe danach:**
```powershell
icacls "dein-key.pem"
```

Es sollte **nur** dein Username aufgelistet sein, z.B.:
```
dein-key.pem PC\dein-username:(R)
```

**Falls immer noch andere Benutzer da sind:**

```powershell
# Alle Berechtigungen entfernen
icacls "dein-key.pem" /inheritance:d
$acl = Get-Acl "dein-key.pem"
$acl.SetAccessRuleProtection($true,$false)
$acl.Access | ForEach-Object { $acl.RemoveAccessRule($_) }
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule($env:USERNAME,"Read","Allow")
$acl.SetAccessRule($rule)
Set-Acl "dein-key.pem" $acl
```

**Lösung 2 - Häufiger Fehler: Falscher Dateiname!**

Prüfe, ob der Dateiname im SSH-Befehl **exakt** mit der Datei übereinstimmt:
- Datei heißt `ec2-ssh.pem` aber du tippst `ssh -i ssh-ec2.pem` → **FALSCH!**
- Verwende den exakten Namen: `ssh -i ec2-ssh.pem ubuntu@...`

### Problem 2: "Connection timed out"

**Mögliche Ursachen:**
- Falsche Security Group? Prüfe, ob Port 22 (SSH) offen ist
- **Deine IP hat sich geändert?** Wenn du "My IP" in der Security Group gewählt hast und deine Internet-IP sich geändert hat (z.B. nach Router-Neustart):
  - Gehe zu **EC2** → **Security Groups**
  - Wähle deine Security Group
  - **Inbound rules** → **Edit inbound rules**
  - Bei der SSH Regel: Ändere die IP oder wähle erneut "My IP"
  - **Save rules**
- Falsche IP-Adresse?
- Instance läuft noch nicht? (Status muss "Running" sein)

### Problem 3: Webseite nicht erreichbar

**Checkliste:**
1. Ist nginx installiert und gestartet? → `sudo systemctl status nginx`
2. Ist Port 80 in der Security Group offen?
3. Verwendest du `http://` (nicht `https://`)?
4. Richtige IP-Adresse?

### Problem 4: "ssh: command not found" (Windows)

**Lösung:** SSH sollte in Windows 11 dabei sein. Falls nicht:

1. **Einstellungen** öffnen
2. **Apps** → **Optionale Features**
3. **Feature hinzufügen** klicken
4. **"OpenSSH Client"** suchen und installieren

---

### TIPP: Alternative - CMD statt PowerShell verwenden

Falls du lieber die klassische Eingabeaufforderung (CMD) verwenden willst:

1. Im Explorer: Klicke in die Adresszeile des Ordners
2. Tippe `cmd` und drücke Enter
3. Verwende diese Befehle (mit Anführungszeichen!):

```cmd
icacls "mein-ec2-key.pem" /reset
icacls "mein-ec2-key.pem" /inheritance:r
icacls "mein-ec2-key.pem" /grant:r "%username%:(R)"
```

4. Dann SSH wie gewohnt:
```cmd
ssh -i mein-ec2-key.pem ubuntu@DEINE-IP
```

---

## Zusammenfassung - Was du gelernt hast

EC2 Instance erstellen  
Instance Types (Free Tier t2.micro)  
SSH Key Pairs erstellen und nutzen  
Security Groups konfigurieren  
SSH-Verbindung von Windows  
Software auf Linux installieren (nginx)  
Webserver betreiben  
Instance stoppen (Kosten sparen!)  

**Free Tier Reminder:**
- 750 Stunden EC2 t2.micro/t3.micro pro Monat (für 12 Monate ab Registrierung)
- 30 GB EBS Storage
- Das gilt für ALLE deine Instances zusammen
- Nach 12 Monaten oder bei Überschreitung: Normale Kosten (~9€/Monat für eine t2.micro 24/7)  

---

## Wichtige Kommandos zum Merken

**SSH verbinden:**
```bash
ssh -i mein-ec2-key.pem ubuntu@DEINE-IP-ADRESSE
```

**System aktualisieren:**
```bash
sudo apt update
```

**Software installieren:**
```bash
sudo apt install PAKETNAME -y
```

**Service-Status prüfen:**
```bash
sudo systemctl status nginx
```

**Service starten:**
```bash
sudo systemctl start nginx
```

**Datei bearbeiten:**
```bash
sudo nano /pfad/zur/datei
```

**SSH beenden:**
```bash
exit
```

---

## Aufräumen nach der Übung

Wenn du ganz fertig bist und die Instance nicht mehr brauchst:

1. **Entweder:** Instance **stoppen** (Daten bleiben erhalten)
2. **Oder:** Instance **terminieren** (alles wird gelöscht)

**Zum Terminieren:**
1. Instance auswählen
2. **"Instance state"** → **"Terminate instance"**
3. Bestätigen

**Achtung:** Terminated = unwiderruflich gelöscht!

---

## BONUS: Kosten überwachen

**Sehr wichtig!** Richte Billing Alerts ein:

1. In der AWS Console: Suche nach **"Billing"**
2. Gehe zu **"Billing Preferences"**
3. Aktiviere: **"Receive Free Tier Usage Alerts"**
4. Gib deine E-Mail ein
5. Aktiviere: **"Receive Billing Alerts"**

So bekommst du eine Warnung, bevor Kosten entstehen!

**Free Tier Nutzung prüfen:**
1. AWS Console → **"Billing"**
2. Links: **"Free Tier"**
3. Hier siehst du deine Nutzung (z.B. "300 of 750 hours used")

