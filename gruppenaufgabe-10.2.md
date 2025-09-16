# Mission: Sichere Verbindung aufbauen
## Linux & SSH mit WSL

---

## Die Ausgangssituation

Ihr arbeitet als IT-Team in einem modernen Unternehmen. Eure Aufgabe: Aufbau eines sicheren Kommunikationsnetzwerks zwischen verschiedenen Arbeitsplätzen. 

### Warum nutzen wir WSL?

Wir nutzen WSL, damit wir trotz unseres Windows-Systems mit Linux arbeiten können. Das bereitet uns auf das spätere Arbeiten mit Servern vor, da die meisten Server Linux-basiert sind.

### Was ist SSH und warum ist es wichtig?

**SSH (Secure Shell)** ist das wichtigste Tool für System-Administratoren:
- **Sicherer Remote-Zugriff:** Verschlüsselte Verbindungen zu anderen Computern
- **Dateiübertragung:** Sichere Übertragung von Dateien zwischen Systemen
- **Automatisierung:** Scripts und Befehle remote ausführen

**Euer Ziel:** Bis zum Ende könnt ihr euch sicher zu jedem Computer in eurer Gruppe verbinden!

---

## Gruppenorganisation

### Arbeitsgruppen bilden
- **Bildet 4-6er Gruppen** für die praktische Durchführung
- Jede Person arbeitet an ihrem eigenen Windows 11 PC
- Ihr unterstützt euch gegenseitig bei Problemen
- **Wichtig:** Trotz Gruppenarbeit gibt jeder eine **individuelle Dokumentation** ab

**Tragt in eurer Abgabe eure Gruppenmitglieder ein:**
- Person 1: ________________
- Person 2: ________________
- Person 3: ________________
- Person 4: ________________
- Person 5: ________________ (optional)
- Person 6: ________________ (optional)

---

# Phase 1: Linux-Arbeitsplatz einrichten
*"Erst die Grundlagen - dann die Magie"*

## Schritt 1.1: WSL-Status prüfen

**Was machen wir hier?** Wir checken, ob Linux bereits in Windows verfügbar ist.

```powershell
# PowerShell öffnen und eingeben:
wsl --list --verbose
```

**Was bedeutet das Ergebnis?**
- **"WSL 2" und "Ubuntu" sichtbar** → Perfekt! Weiter zu Schritt 1.3
- **Fehlermeldung oder leer** → WSL muss installiert werden → Schritt 1.2

## Schritt 1.2: WSL installieren (falls nötig)

**Warum als Administrator?** Systemänderungen benötigen erhöhte Rechte.

```powershell
# PowerShell ALS ADMINISTRATOR öffnen:
wsl --install
```

**Was passiert jetzt?**
- Computer startet neu (das ist normal!)
- Ubuntu wird automatisch installiert
- Ihr müsst einen Linux-Benutzernamen und Passwort festlegen

## Schritt 1.3: Linux-System aktualisieren

**Warum aktualisieren?** Wie bei Windows-Updates: Sicherheit und neue Features.

```bash
# WSL-Terminal öffnen und eingeben:
sudo apt update && sudo apt upgrade -y
```

**Was bedeuten diese Befehle?**
- `sudo` = "Als Administrator ausführen" (Super User Do)
- `apt` = Programm-Manager für Linux (wie Microsoft Store)
- `update` = Liste neuer Programme laden
- `upgrade` = Installierte Programme aktualisieren

Das dauert 2-3 Minuten - perfekte Zeit für Fragen!

---

# Phase 2: Netzwerk verstehen und testen
*"Bevor wir bauen, schauen wir uns das Fundament an"*

## Schritt 2.1: IP-Adressen ermitteln

**Was ist eine IP-Adresse?** Wie eine Hausadresse - ohne sie findet euch niemand im Netzwerk.

```powershell
# Windows PowerShell (neues Fenster):
ipconfig | findstr "IPv4"
```

**Notiert eure Windows-IP (z.B. 192.168.1.100):**
- Meine Windows-IP: ________________

```bash
# In WSL:
hostname -I
```

**Notiert eure WSL-IP (z.B. 172.20.10.2):**
- Meine WSL-IP: ________________

**Warum zwei verschiedene IPs?** Windows und WSL sind wie zwei getrennte Computer - jeder braucht seine eigene Adresse.

## Schritt 2.2: Gruppenmitglieder-IPs sammeln

**Tauscht eure Windows-IPs aus:**
- Person 1 Windows-IP: ________________
- Person 2 Windows-IP: ________________
- Person 3 Windows-IP: ________________
- Person 4 Windows-IP: ________________

## Schritt 2.3: Netzwerk-Test (WICHTIG!)

**Warum testen wir das?** Ohne funktionierende Grundverbindung wird SSH nicht funktionieren.

```powershell
# Windows PowerShell - testet zu euren Gruppenmitgliedern:
ping PERSON1-WINDOWS-IP
ping PERSON2-WINDOWS-IP
```

**Was bedeuten die Ergebnisse?**
- **"Antwort von..."** = Perfekt! Das Netzwerk funktioniert
- **"Zeitüberschreitung"** = Problem! Seht Troubleshooting unten

### Troubleshooting: Falls Ping nicht funktioniert

**Problem:** Router verhindert Kommunikation zwischen Geräten (häufig in Schul-WLANs)

**Lösung - Hotspot erstellen:**
1. Eine Person: Windows-Einstellungen → Netzwerk → Mobiler Hotspot
2. Hotspot aktivieren, Name und Passwort festlegen
3. Alle anderen verbinden sich mit diesem Hotspot
4. Neue IPs ermitteln und Ping-Test wiederholen

**Dokumentiert euer Ergebnis:**
```
Netzwerk-Test:
- Ping zu Person 1: ✅ / ❌
- Ping zu Person 2: ✅ / ❌
- Hotspot verwendet: Ja / Nein
```

---

# Phase 3: SSH-Server einrichten
*"Jetzt machen wir euren Computer zu einem sicheren Server"*

## Schritt 3.1: SSH-Server installieren

**Was ist ein SSH-Server?** Ein Programm, das sichere Verbindungen von anderen Computern annimmt.

```bash
# SSH-Server installieren
sudo apt install openssh-server -y

# Prüfen ob Installation erfolgreich war
dpkg -l | grep openssh-server
```

**Erfolgreich?** Ihr seht eine Zeile mit "openssh-server".

## Schritt 3.2: SSH konfigurieren

**Warum konfigurieren?** Standardeinstellungen sind nicht optimal für unsere Übung.

```bash
# Backup der Original-Konfiguration (Sicherheit!)
sudo cp /etc/ssh/sshd_config /etc/ssh/sshd_config.backup

# Konfiguration bearbeiten
sudo nano /etc/ssh/sshd_config
```

**Sucht diese Zeilen und ändert sie:**
```bash
# Port 22                    →    Port 2222
# PasswordAuthentication yes →    PasswordAuthentication yes
# PermitRootLogin no         →    PermitRootLogin no
```

**Warum Port 2222?** Port 22 ist oft in Firmen-/Schulnetzwerken blockiert.

**Speichern:** `Strg + O` → Enter → `Strg + X`

## Schritt 3.3: SSH-Server starten

```bash
# SSH-Service starten
sudo service ssh start

# Status prüfen
sudo service ssh status
```

**Erfolg sieht so aus:**
```
Active: active (running)
```

**Falls "failed":** Meist Tippfehler in der Konfiguration. Prüft die Änderungen nochmal.

## Schritt 3.4: Lokaler Test

**Warum zu uns selbst verbinden?** Bevor wir andere erreichen, testen wir ob SSH grundsätzlich funktioniert.

```bash
# Test: Verbindung zu uns selbst
ssh -p 2222 $(whoami)@localhost

# Bei Erfolg seht ihr euren Prompt nochmal
# Trennen mit: exit
```

---

# Phase 4: Windows für SSH öffnen
*"Windows muss lernen, Gäste reinzulassen"*

## Schritt 4.1: Windows Firewall konfigurieren

**Warum?** Windows blockiert standardmäßig alle eingehenden Verbindungen für Sicherheit.

```powershell
# PowerShell ALS ADMINISTRATOR:
netsh advfirewall firewall add rule name="WSL SSH" dir=in action=allow protocol=TCP localport=2222

# Prüfen ob Regel erstellt wurde
netsh advfirewall firewall show rule name="WSL SSH"
```

## Schritt 4.2: Port-Weiterleitung einrichten

**Das Problem:** WSL läuft "versteckt" hinter Windows. Andere Computer sehen nur Windows, nicht WSL.

**Die Lösung:** Eine "Brücke" von Windows zu WSL bauen.

```powershell
# Eure WSL-IP herausfinden (merkt sie euch!)
wsl hostname -I

# Port-Weiterleitung einrichten (ersetzt WSL-IP durch eure echte IP!)
netsh interface portproxy add v4tov4 listenport=2222 listenaddress=0.0.0.0 connectport=2222 connectaddress=EURE-WSL-IP

# Beispiel:
# netsh interface portproxy add v4tov4 listenport=2222 listenaddress=0.0.0.0 connectport=2222 connectaddress=172.20.10.2
```

**Prüfen ob es funktioniert:**
```powershell
netsh interface portproxy show all
```

**Ihr solltet sehen:** `2222` → `eure-wsl-ip:2222`

---

# Phase 5: Erste Verbindungen
*"Der magische Moment - Verbindung zu anderen Computern!"*

## Schritt 5.1: Erste SSH-Verbindung

**Der Moment der Wahrheit:** Verbindung zu einem Gruppenmitglied.

```bash
# Verbindung zu einem Gruppenmitglied (verwendet WINDOWS-IP!)
ssh -p 2222 gruppenmitglied-benutzername@GRUPPENMITGLIED-WINDOWS-IP

# Beispiel:
# ssh -p 2222 anna@192.168.1.101
```

**Was passiert Schritt für Schritt:**
1. **Sicherheitswarnung:** "The authenticity of host... are you sure?" → `yes` eingeben
2. **Passwort-Abfrage:** Das Linux-Passwort eures Gruppenmitglieds eingeben
3. **Erfolg:** Neuer Prompt zeigt euch, dass ihr "drüben" seid!

## Schritt 5.2: "Wo bin ich?"-Beweis

**Beweist euch selbst, dass ihr wirklich auf dem anderen Computer seid:**

```bash
# Computername anzeigen
hostname

# Aktueller Benutzer
whoami

# Welches System?
uname -a

# Zurück zum eigenen Computer
exit
```

## Schritt 5.3: Alle Verbindungen testen

**Testet systematisch zu allen Gruppenmitgliedern:**

```bash
# Schnelltest zu Person 1
ssh -p 2222 person1@PERSON1-IP "hostname && whoami" && echo "Verbindung erfolgreich!"

# Das gleiche für alle anderen...
```

### Problemlösung (falls etwas nicht funktioniert)

**"Connection refused":**
- Partner prüft: `sudo service ssh status`
- Partner startet SSH: `sudo service ssh start`

**"Connection timeout":**
- Ping-Test wiederholen: `ping PARTNER-IP`
- Falls Ping nicht geht: Zurück zu Phase 2 (Hotspot)

**"Permission denied":**
- Richtigen Benutzernamen beim Partner erfragen
- Passwort korrekt eingeben

**Dokumentiert eure Tests:**
```
Verbindungstest-Matrix:
- Zu Person 1: ✅ / ❌
- Zu Person 2: ✅ / ❌  
- Zu Person 3: ✅ / ❌
- Zu Person 4: ✅ / ❌
```

---

# Phase 6: Kommunikation wie Profis
*"Echte Administratoren kommunizieren über das Terminal"*

## Schritt 6.1: Nachrichten senden

**Warum über Terminal kommunizieren?** In Server-Umgebungen gibt es oft keine grafische Oberfläche.

```bash
# Verbindung zu einem Gruppenmitglied
ssh -p 2222 gruppenmitglied@GRUPPENMITGLIED-IP

# Nachricht an alle Benutzer senden
echo "Hallo von $(whoami) - Verbindungstest erfolgreich!" | wall

# Verbindung trennen
exit
```

**Was macht `wall`?** "Write to all" - sendet Nachrichten an alle angemeldeten Benutzer.

## Schritt 6.2: Professionelle Nachrichten

```bash
# Tool für schöne ASCII-Art installieren
sudo apt install figlet -y

# Beeindruckende Nachricht erstellen
ssh -p 2222 gruppenmitglied@GRUPPENMITGLIED-IP
figlet "System OK" | wall
exit
```

---

# Phase 7: Dateien sicher übertragen
*"SCP - Das Werkzeug für sicheren Dateiaustausch"*

## Schritt 7.1: Erste Datei erstellen

**Was ist SCP?** Secure Copy Protocol - kopiert Dateien sicher über SSH.

```bash
# Wichtige "Konfigurationsdatei" erstellen
echo "# System-Konfiguration
Hostname: $(hostname)
IP-Adresse: $(hostname -I)
SSH-Port: 2222
Status: Aktiv
Administrator: $(whoami)
Erstellt: $(date)" > system_config.txt

# Inhalt anzeigen
cat system_config.txt
```

## Schritt 7.2: Datei übertragen

```bash
# Datei sicher zu einem Gruppenmitglied senden
scp -P 2222 system_config.txt gruppenmitglied@GRUPPENMITGLIED-IP:/tmp/

# Prüfen ob angekommen
ssh -p 2222 gruppenmitglied@GRUPPENMITGLIED-IP "ls -la /tmp/system_config.txt"
```

**Warum funktioniert das?** SCP nutzt SSH - da SSH funktioniert, funktioniert auch SCP!

## Schritt 7.3: Dateien sammeln

```bash
# Konfigurationen von allen Gruppenmitgliedern holen
scp -P 2222 person1@PERSON1-IP:/tmp/system_config.txt ./config_person1.txt
scp -P 2222 person2@PERSON2-IP:/tmp/system_config.txt ./config_person2.txt

# Alle Konfigurationen vergleichen
echo "=== MEINE KONFIGURATION ==="
cat system_config.txt
echo -e "\n=== PERSON 1 KONFIGURATION ==="
cat config_person1.txt
```

---

# Phase 8: Remote-Administration
*"Systeme aus der Ferne überwachen und verwalten"*

## Schritt 8.1: System-Monitoring

**Was machen echte Administratoren?** Sie überwachen viele Server gleichzeitig von ihrem Arbeitsplatz aus.

```bash
# Lokales System checken
echo "=== MEIN SYSTEM ==="
free -h && df -h | head -3 && uptime

# Remote-System checken
echo -e "\n=== PARTNER-SYSTEM ==="
ssh -p 2222 partner@PARTNER-IP 'free -h && df -h | head -3 && uptime'
```

## Schritt 8.2: Monitoring-Tools installieren

```bash
# Professionelle Tools installieren
sudo apt install htop neofetch -y

# Schöne Systemanzeige
neofetch

# Beim Partner remote ausführen
ssh -p 2222 partner@PARTNER-IP neofetch
```

## Schritt 8.3: Live-Monitoring

```bash
# Live-Prozess-Monitor beim Partner
ssh -p 2222 partner@PARTNER-IP htop

# Navigation: Pfeiltasten bewegen, 'q' für beenden
```

---

# Phase 9: Sicherheit erhöhen mit SSH-Keys
*"Keine Passwörter mehr - wir nutzen Kryptographie!"*

## Schritt 9.1: SSH-Keys verstehen

**Warum SSH-Keys statt Passwörter?**
- **Sicherer:** 4096-Bit-Verschlüsselung vs. 8-stelliges Passwort
- **Praktischer:** Kein Passwort-Tippen mehr
- **Professioneller:** Standard in der IT-Industrie

**Wie funktioniert es?**
- **Private Key:** Bleibt geheim bei euch (wie euer Hausschlüssel)
- **Public Key:** Wird zu anderen übertragen (wie ein Türschloss)

## Schritt 9.2: Key-Paar generieren

```bash
# RSA-Schlüsselpaar erstellen
ssh-keygen -t rsa -b 4096 -C "admin-$(whoami)"

# Bei allen Fragen einfach Enter drücken (Standardwerte)
```

**Was passiert?** Zwei Dateien werden erstellt:
- `~/.ssh/id_rsa` → Private Key (GEHEIM!)
- `~/.ssh/id_rsa.pub` → Public Key (darf geteilt werden)

## Schritt 9.3: Public Key übertragen

```bash
# Automatische Übertragung zu einem Gruppenmitglied
ssh-copy-id -p 2222 person1@PERSON1-IP

# Test: Jetzt ohne Passwort einloggen!
ssh -p 2222 person1@PERSON1-IP
```

**Magie!** Keine Passwort-Abfrage mehr - ihr seid direkt drin!

## Schritt 9.4: Komfortable SSH-Konfiguration

```bash
# SSH-Config für einfache Verbindungen erstellen
nano ~/.ssh/config
```

**Inhalt:**
```bash
Host person1
    HostName PERSON1-WINDOWS-IP
    User person1-benutzername
    Port 2222

Host person2
    HostName PERSON2-WINDOWS-IP
    User person2-benutzername
    Port 2222
```

**Jetzt super einfach:**
```bash
# Statt: ssh -p 2222 person1@192.168.1.101
# Einfach: 
ssh person1
```

---

# Phase 10: Abschluss-Challenge
*"Zeigt was ihr gelernt habt!"*

## Challenge: Gruppen-Monitoring-System

**Entwickelt gemeinsam ein Monitoring-Script:**

```bash
# Script erstellen
nano ~/group_monitor.sh
```

**Script-Inhalt:**
```bash
#!/bin/bash
echo "===== GRUPPEN-NETZWERK-MONITOR ====="
echo "Gestartet: $(date)"
echo

echo "LOKALES SYSTEM:"
echo "- Hostname: $(hostname)"
echo "- Speicher frei: $(free -h | grep Mem | awk '{print $7}')"
echo "- Uptime: $(uptime -p)"
echo

if [ "$1" ]; then
    echo "REMOTE-SYSTEM: $1"
    ssh "$1" "
        echo '- Hostname:' $(hostname)
        echo '- Speicher frei:' $(free -h | grep Mem | awk '{print $7}')
        echo '- Uptime:' $(uptime -p)
    "
fi

echo "===== MONITORING ABGESCHLOSSEN ====="
```

```bash
# Script ausführbar machen
chmod +x ~/group_monitor.sh

# Testen
./group_monitor.sh person1
```

---

# Individuelle Dokumentation erstellen

## Abschlussbericht

**Erstellt euren persönlichen Bericht:**

```bash
nano ~/abschlussbericht_$(whoami).txt
```

**Template:**
```
===============================================
    SSH-NETZWERK MISSION - ABSCHLUSSBERICHT
===============================================

NAME: [Euer Name]
DATUM: $(date)
GRUPPE: [Gruppenmitglieder auflisten]

TECHNISCHE DATEN:
- Meine Windows-IP: ____________
- Meine WSL-IP: ____________
- SSH-Port verwendet: 2222

ERFOLGREICHE VERBINDUNGEN:
[ ] Zu Person 1: Name _____, IP _____
[ ] Zu Person 2: Name _____, IP _____
[ ] Zu Person 3: Name _____, IP _____
[ ] Zu Person 4: Name _____, IP _____

DURCHGEFÜHRTE AUFGABEN:
[ ] WSL eingerichtet
[ ] SSH-Server konfiguriert
[ ] Windows Firewall geöffnet
[ ] Port-Forwarding eingerichtet
[ ] SSH-Verbindungen getestet
[ ] Nachrichten ausgetauscht
[ ] Dateien übertragen (SCP)
[ ] SSH-Keys verwendet
[ ] Remote-Monitoring durchgeführt
[ ] Monitoring-Script entwickelt

NEUE SKILLS GELERNT:
1. Linux-Befehle:
   - ssh: [Erklärung]
   - scp: [Erklärung]
   - sudo: [Erklärung]

2. Netzwerk-Konzepte:
   - IP-Adressen: [Erklärung]
   - SSH-Protokoll: [Erklärung]
   - Port-Forwarding: [Erklärung]

PROBLEME UND LÖSUNGEN:
- Problem 1: [Beschreibung] → Lösung: [Beschreibung]
- Problem 2: [Beschreibung] → Lösung: [Beschreibung]

PRAKTISCHE ANWENDUNGEN:
Wo könnte ich SSH verwenden?
- Im Studium: [Beispiele]
- Im Beruf: [Beispiele]
- Hobby-Projekte: [Beispiele]

BEWERTUNG (1-10):
- Schwierigkeit: ___
- Interesse: ___
- Praktischer Nutzen: ___

FAZIT:
[Freie Bewertung der Mission]

===============================================
```

---

# Anhang: Wichtige Hinweise

## Nach PC-Neustart

**Falls euer PC neu startet, müsst ihr diese Schritte wiederholen:**

1. **WSL:** SSH-Service starten: `sudo service ssh start`
2. **Windows:** Port-Forwarding neu einrichten (WSL-IP ändert sich!)
3. **Test:** SSH-Verbindungen erneut testen

## Spickzettel für die Zukunft

```bash
# Wichtigste SSH-Befehle
ssh -p 2222 user@host              # Verbindung aufbauen
scp -P 2222 file.txt user@host:/   # Datei übertragen
ssh user@host "command"            # Remote-Befehl ausführen
ssh-keygen -t rsa -b 4096          # SSH-Keys generieren
ssh-copy-id user@host              # Public Key übertragen
```

---
