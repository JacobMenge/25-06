# Challenge: Sichere Verbindung aufbauen
## Linux & SSH mit WSL - Verteilte Teams Edition

---

## Die Ausgangssituation

Ihr arbeitet als IT-Team in einem modernen Unternehmen. Eure Aufgabe: Aufbau eines sicheren Kommunikationsnetzwerks zwischen verschiedenen Arbeitsplätzen. 

**Besonderheit:** Ihr arbeitet alle von verschiedenen Standorten (zuhause) und müsst euch über das Internet verbinden!

### Warum nutzen wir WSL?

Wir nutzen WSL, damit wir trotz unseres Windows-Systems mit Linux arbeiten können. Das bereitet uns auf das spätere Arbeiten mit Servern vor, da die meisten Server Linux-basiert sind.

### Was ist SSH und warum ist es wichtig?

**SSH (Secure Shell)** ist das wichtigste Tool für System-Administratoren:
- **Sicherer Remote-Zugriff:** Verschlüsselte Verbindungen zu anderen Computern über das Internet
- **Dateiübertragung:** Sichere Übertragung von Dateien zwischen Systemen
- **Automatisierung:** Scripts und Befehle remote ausführen

**Euer Ziel:** Bis zum Ende könnt ihr euch sicher zu jedem Computer in eurer Gruppe verbinden - egal wo auf der Welt ihr seid!

---

## Gruppenorganisation

### Arbeitsgruppen bilden
- **Bildet 4-6er Gruppen** für die praktische Durchführung
- Jede Person arbeitet von ihrem eigenen Standort aus
- Ihr unterstützt euch gegenseitig über Chat/Video bei Problemen
- **Wichtig:** Ihr gebt pro Gruppe mindestens eine Dokumentation ab

**⚠️ Hinweis:** Ihr werdet Router-Einstellungen für das IT-Projekt ändern müssen. Diese Konfigurationen sind sicher und werden nach der Übung wieder rückgängig gemacht.

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

# Phase 2: Netzwerk verstehen - Lokal vs. Global
*"Zwei Welten: Zuhause-Netzwerk und Internet"*

## Schritt 2.1: Lokale IP-Adressen ermitteln

**Was ist eine lokale IP-Adresse?** Wie eine interne Adresse in eurem lokalen Netzwerk - nur in eurem WLAN/LAN gültig.

```powershell
# Windows PowerShell (neues Fenster):
ipconfig | findstr "IPv4"
```

**Notiert eure lokale Windows-IP (z.B. 192.168.1.100):**
- Meine lokale Windows-IP: ________________

```bash
# In WSL:
hostname -I
```

**Notiert eure WSL-IP (z.B. 172.20.10.2):**
- Meine WSL-IP: ________________

## Schritt 2.2: Öffentliche IP-Adresse ermitteln

**Was ist eine öffentliche IP?** Wie eure Adresse im Internet - damit findet euch die ganze Welt!

```bash
# Linux - eure "Internet-Adresse" finden:
curl ifconfig.me
```

**Notiert eure öffentliche IP (z.B. 89.247.123.45):**
- Meine öffentliche IP: ________________

**Tauscht eure öffentlichen IPs in der Gruppe aus:**
- Person 1 öffentliche IP: ________________
- Person 2 öffentliche IP: ________________
- Person 3 öffentliche IP: ________________
- Person 4 öffentliche IP: ________________

## Schritt 2.3: Internet-Verbindungstest

**Warum testen?** Ohne funktionierende Internet-Verbindung wird SSH nicht funktionieren.

```powershell
# Teste Internet-Verbindung
ping google.de

# Teste zu euren Gruppenmitgliedern (öffentliche IPs!)
ping PERSON1-ÖFFENTLICHE-IP
```

**Was bedeuten die Ergebnisse?**
- **"Antwort von..."** = Internet funktioniert!
- **"Zeitüberschreitung"** = Internet-Problem oder die andere Person ist offline

---

# Phase 3: SSH-Server einrichten
*"Jetzt machen wir euren Computer zu einem sicheren Server"*

## Schritt 3.1: SSH-Server installieren

**Was ist ein SSH-Server?** Ein Programm, das sichere Verbindungen aus dem Internet annimmt.

```bash
# SSH-Server installieren
sudo apt install openssh-server -y

# Prüfen ob Installation erfolgreich war
dpkg -l | grep openssh-server
```

**Erfolgreich?** Ihr seht eine Zeile mit "openssh-server".

## Schritt 3.2: SSH konfigurieren

**Warum konfigurieren?** Standardeinstellungen sind nicht optimal für Internet-Verbindungen.

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
# MaxAuthTries 6             →    MaxAuthTries 3
# ClientAliveInterval 0      →    ClientAliveInterval 60
```

**Warum diese Änderungen?**
- **Port 2222:** Port 22 ist oft von Internet-Providern blockiert
- **MaxAuthTries 3:** Weniger Angriffs-Versuche erlaubt
- **ClientAliveInterval:** Verbindung bleibt stabil bei schlechtem Internet

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

**Warum zu uns selbst verbinden?** Bevor wir das Internet nutzen, testen wir ob SSH grundsätzlich funktioniert.


powershell:
[Benutzer auf dem server] = Tragt hier den Benutzer eures Servers ein
```powershell
# Test: Verbindung zu uns selbst
ssh [benutzer auf dem server]@localhost

# Bei Erfolg seht ihr euren Prompt nochmal
# Trennen mit: exit
```

---

# Phase 4: Router für Internet-Zugriff konfigurieren
*"Das Tor zur Welt öffnen - Port-Forwarding einrichten"*

## Schritt 4.1: Router-Interface öffnen

**Wichtig:** Stellt sicher, dass ihr Administratorrechte für euren Router habt!

```powershell
# Eure Router-IP finden (Gateway)
ipconfig | findstr "Standard"
```

**Typische Router-Adressen im Browser öffnen:**
- `192.168.1.1` (häufigste)
- `192.168.0.1` 
- `10.0.0.1`
- `fritz.box` (bei Fritzboxen)
- `speedport.ip` (bei Telekom)

## Schritt 4.2: Router-Login

**Login-Daten finden:**
- Aufkleber am Router
- Handbuch des Routers
- Standard-Kombinationen: `admin/admin`, `admin/password`, `admin/(leer)`

**Router-Typ dokumentieren:**
- Mein Router-Typ: ________________ (z.B. Fritzbox 7590)

## Schritt 4.3: Port-Forwarding einrichten

**Sucht nach diesen Menü-Punkten:**
- "Port-Forwarding" / "Port-Weiterleitung"
- "Virtuelle Server" / "Virtual Server"
- "NAT" / "Portfreigabe"
- "Firewall" → "Portfreigabe"

### Für Fritzbox:
```
Internet → Freigaben → Portfreigabe → Gerät für Freigaben hinzufügen
- Gerät: [Euer PC auswählen]  
- Neue Freigabe: Andere Anwendung
- Bezeichnung: SSH-Server
- Protokoll: TCP
- Von Port: 2222
- Bis Port: 2222
- An Computer: [Eure lokale Windows-IP]
```

### Für andere Router:
```
Port-Forwarding Regel erstellen:
- Service Name: SSH-Server
- External Port: 2222
- Internal Port: 2222
- Internal IP: [Eure lokale Windows-IP]
- Protocol: TCP
- Enable: ✅
```

## Schritt 4.4: Windows Firewall konfigurieren

```powershell
# PowerShell ALS ADMINISTRATOR:
netsh advfirewall firewall add rule name="SSH Server Internet" dir=in action=allow protocol=TCP localport=2222

# Prüfen ob Regel erstellt wurde
netsh advfirewall firewall show rule name="SSH Server Internet"
```

## Schritt 4.5: Port-Weiterleitung von Windows zu WSL

```powershell
# Eure WSL-IP nochmal prüfen
wsl hostname -I

# Port-Weiterleitung einrichten (ersetzt durch eure WSL-IP!)
netsh interface portproxy add v4tov4 listenport=2222 listenaddress=0.0.0.0 connectport=2222 connectaddress=EURE-WSL-IP

# Beispiel:
# netsh interface portproxy add v4tov4 listenport=2222 listenaddress=0.0.0.0 connectport=2222 connectaddress=172.20.10.2

# Prüfen ob aktiv
netsh interface portproxy show all
```

## Schritt 4.6: Konfiguration testen

```powershell
# Test von außen mit Online-Tool (im Browser):
# https://www.canyouseeme.org
# Port: 2222
# IP wird automatisch erkannt

# Oder mit eigenem Tool:
telnet EURE-ÖFFENTLICHE-IP 2222
```

**Erfolgreich wenn:** "SSH-2.0-OpenSSH" erscheint oder Verbindung wird hergestellt.

---

# Phase 5: Internet-SSH-Verbindungen
*"Der magische Moment - Verbindung über das Internet!"*

## Schritt 5.1: Erste Internet-SSH-Verbindung

**Der Moment der Wahrheit:** Verbindung zu einem Gruppenmitglied über das Internet.

```bash
# Verbindung zu einem Gruppenmitglied (ÖFFENTLICHE IP verwenden!)
ssh -p 2222 gruppenmitglied-benutzername@GRUPPENMITGLIED-ÖFFENTLICHE-IP

# Beispiel:
# ssh -p 2222 anna@89.247.123.45
```

**Was passiert Schritt für Schritt:**
1. **Verbindungs-Aufbau:** "Connecting to..." (kann 5-10 Sekunden dauern)
2. **Sicherheitswarnung:** "The authenticity of host... are you sure?" → `yes` eingeben
3. **Passwort-Abfrage:** Das Linux-Passwort eures Gruppenmitglieds eingeben
4. **Erfolg:** Neuer Prompt zeigt euch, dass ihr "im Internet beim anderen" seid!

## Schritt 5.2: "Wo bin ich?"-Beweis

**Beweist euch selbst, dass ihr wirklich auf dem anderen Computer seid:**

```bash
# Computername anzeigen
hostname

# Internet-IP des Partners prüfen
curl ifconfig.me

# Aktueller Benutzer
whoami

# Welches System und wo?
uname -a && date

# Zurück zum eigenen Computer
exit
```

## Schritt 5.3: Alle Internet-Verbindungen testen

**Testet systematisch zu allen Gruppenmitgliedern:**

```bash
# Schnelltest zu Person 1
ssh -p 2222 person1@PERSON1-ÖFFENTLICHE-IP "hostname && curl -s ifconfig.me && echo ' <- Das bin ich!'" && echo "Internet-Verbindung erfolgreich!"

# Das gleiche für alle anderen...
```

### Internet-Problemlösung

**"Connection refused" oder "Connection timeout":**
1. **Partner prüft Router-Konfiguration:** Port 2222 wirklich weitergeleitet?
2. **Partner prüft SSH-Status:** `sudo service ssh status`
3. **Partner prüft Firewall:** Windows-Regel aktiviert?
4. **Online Port-Check:** https://www.canyouseeme.org

**"Permission denied":**
- Richtigen Linux-Benutzernamen beim Partner erfragen
- Passwort korrekt eingeben (Vorsicht: anderes Tastatur-Layout?)

**"Host key verification failed":**
```bash
# Host-Key zurücksetzen und neu akzeptieren
ssh-keygen -R PARTNER-ÖFFENTLICHE-IP
ssh -p 2222 partner@PARTNER-ÖFFENTLICHE-IP
```

**Dokumentiert eure Internet-Tests:**
```
Internet-SSH-Verbindungstest:
- Zu Person 1 (IP: ___.___.___.__): ✅ / ❌
- Zu Person 2 (IP: ___.___.___.__): ✅ / ❌  
- Zu Person 3 (IP: ___.___.___.__): ✅ / ❌
- Zu Person 4 (IP: ___.___.___.__): ✅ / ❌
```

---

# Phase 6: Internet-Kommunikation wie Profis
*"Echte Administratoren kommunizieren über SSH durchs Internet"*

## Schritt 6.1: Nachrichten über das Internet senden

**Warum über Internet-Terminal kommunizieren?** Server stehen oft in anderen Ländern/Kontinenten.

```bash
# Verbindung zu einem Gruppenmitglied
ssh -p 2222 gruppenmitglied@GRUPPENMITGLIED-ÖFFENTLICHE-IP

# Nachricht mit Standort-Info senden
echo "Grüße aus $(curl -s ipinfo.io/city) von $(whoami) - Internet-SSH funktioniert!" | wall

# IP und Ort anzeigen
echo "Ich bin gerade eingeloggt auf einem Computer in $(curl -s ipinfo.io/city), $(curl -s ipinfo.io/country)"

# Verbindung trennen
exit
```

## Schritt 6.2: Geografische Internet-Analyse

```bash
# Verbindung zu Partnern und deren Standort anzeigen
ssh -p 2222 partner@PARTNER-ÖFFENTLICHE-IP "curl -s ipinfo.io"

# Zeitzonen-Vergleich
ssh -p 2222 partner@PARTNER-ÖFFENTLICHE-IP "date" && echo "Meine Zeit: $(date)"
```

## Schritt 6.3: Professionelle Internet-Nachrichten

```bash
# Tool für schöne Nachrichten installieren
sudo apt install figlet curl -y

# Internet-Erfolg-Nachricht senden
ssh -p 2222 gruppenmitglied@GRUPPENMITGLIED-ÖFFENTLICHE-IP
figlet "Connected!" && echo "Internet-SSH von $(curl -s ipinfo.io/ip) erfolgreich!" | wall
exit
```

---

# Phase 7: Dateien sicher über das Internet übertragen
*"SCP - Datenaustausch zwischen verschiedenen Standorten"*

## Schritt 7.1: Internet-Systeminfo-Datei erstellen

```bash
# Detaillierte System- und Internet-Info erstellen
echo "# Internet-SSH-System-Report
=================================
Lokale Informationen:
- Hostname: $(hostname)
- Lokale IP: $(hostname -I)
- SSH-Port: 2222
- Linux-User: $(whoami)

Internet-Informationen:
- Öffentliche IP: $(curl -s ifconfig.me)
- Standort: $(curl -s ipinfo.io/city), $(curl -s ipinfo.io/region)
- Provider: $(curl -s ipinfo.io/org)
- Land: $(curl -s ipinfo.io/country)

System-Details:
- Betriebssystem: $(uname -a)
- Erstellt: $(date)
- Uptime: $(uptime -p)
=================================
Internet-SSH-Mission erfolgreich!
$(figlet 'CONNECTED')" > internet_system_report.txt

# Inhalt anzeigen
cat internet_system_report.txt
```

## Schritt 7.2: Datei über das Internet übertragen

```bash
# Datei sicher über das Internet zu einem Gruppenmitglied senden
scp -P 2222 internet_system_report.txt gruppenmitglied@GRUPPENMITGLIED-ÖFFENTLICHE-IP:/tmp/

# Prüfen ob über Internet angekommen
ssh -p 2222 gruppenmitglied@GRUPPENMITGLIED-ÖFFENTLICHE-IP "ls -la /tmp/internet_system_report.txt && echo '--- INHALT ---' && cat /tmp/internet_system_report.txt"
```

## Schritt 7.3: Internet-Daten von allen sammeln

```bash
# Reports von allen Gruppenmitgliedern über Internet holen
scp -P 2222 person1@PERSON1-ÖFFENTLICHE-IP:/tmp/internet_system_report.txt ./report_person1.txt
scp -P 2222 person2@PERSON2-ÖFFENTLICHE-IP:/tmp/internet_system_report.txt ./report_person2.txt

# Weltweite Gruppen-Übersicht erstellen
echo "===== GRUPPEN-INTERNET-ÜBERSICHT ====="
echo "Gesammelt am: $(date)"
echo
for file in report_*.txt; do
    echo "=== $(basename $file .txt | cut -d_ -f2) ==="
    grep -A5 "Internet-Informationen:" "$file"
    echo
done
```

---

# Phase 8: Remote-Internet-Administration
*"Systeme weltweit überwachen und verwalten"*

## Schritt 8.1: Weltweites System-Monitoring

```bash
# Eigenes System checken
echo "=== MEIN SYSTEM ($(curl -s ipinfo.io/city)) ==="
free -h && df -h | head -3 && echo "Öffentliche IP: $(curl -s ifconfig.me)"

# Internet-Partner-System checken
echo -e "\n=== PARTNER-SYSTEM ÜBER INTERNET ==="
ssh -p 2222 partner@PARTNER-ÖFFENTLICHE-IP 'echo "Standort: $(curl -s ipinfo.io/city)" && free -h && df -h | head -3 && echo "Öffentliche IP: $(curl -s ifconfig.me)"'
```

## Schritt 8.2: Internet-Monitoring-Dashboard

```bash
# Professionelle Tools für Internet-Admin installieren
sudo apt install htop neofetch speedtest-cli -y

# Internet-Geschwindigkeit testen
speedtest-cli --simple

# Schöne System-Übersicht mit Internet-Info
neofetch

# Bei Partnern über Internet ausführen
ssh -p 2222 partner@PARTNER-ÖFFENTLICHE-IP 'neofetch && echo "Internet-Speed:" && speedtest-cli --simple'
```

## Schritt 8.3: Live Internet-Monitoring

```bash
# Live-Internet-Monitoring beim Partner
ssh -p 2222 partner@PARTNER-ÖFFENTLICHE-IP htop

# Internet-Latenz kontinuierlich messen
ping -c 10 PARTNER-ÖFFENTLICHE-IP
```

---

# Phase 9: Maximale Sicherheit mit SSH-Keys über Internet
*"Keine Passwörter über das Internet - Kryptographie für Profis!"*

## Schritt 9.1: Internet-SSH-Keys verstehen

**Warum SSH-Keys bei Internet-Verbindungen kritisch sind:**
- **Internet-Sicherheit:** Passwörter können abgefangen werden
- **Automatisierung:** Scripts ohne Passwort-Eingabe möglich
- **Compliance:** Viele Unternehmen verlangen schlüsselbasierte Authentifizierung

## Schritt 9.2: Hochsichere Key-Paare generieren

```bash
# Hochsicheres RSA-4096-Schlüsselpaar für Internet-Nutzung
ssh-keygen -t rsa -b 4096 -C "internet-admin-$(whoami)@$(hostname)-$(date +%Y%m%d)"

# Sicheren Speicherort wählen (Enter für Standard)
# Passphrase für Extra-Sicherheit (optional, aber empfohlen für Internet)
```

## Schritt 9.3: Public Keys über Internet übertragen

```bash
# Automatische Übertragung zu einem Internet-Partner
ssh-copy-id -p 2222 person1@PERSON1-ÖFFENTLICHE-IP

# Manuelle Übertragung (falls automatisch nicht funktioniert):
scp -P 2222 ~/.ssh/id_rsa.pub person1@PERSON1-ÖFFENTLICHE-IP:/tmp/
ssh -p 2222 person1@PERSON1-ÖFFENTLICHE-IP
mkdir -p ~/.ssh
cat /tmp/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
exit
```

## Schritt 9.4: Passwortlose Internet-Verbindungen testen

```bash
# Test: Jetzt ohne Passwort über Internet einloggen!
ssh -p 2222 person1@PERSON1-ÖFFENTLICHE-IP

# Magie! Keine Passwort-Abfrage mehr - direkt über Internet verbunden!
hostname && curl -s ifconfig.me
exit
```

## Schritt 9.5: Internet-SSH-Konfiguration optimieren

```bash
# SSH-Config für komfortable Internet-Verbindungen
nano ~/.ssh/config
```

**Inhalt für Internet-Verbindungen:**
```bash
Host person1-internet
    HostName PERSON1-ÖFFENTLICHE-IP
    User person1-benutzername
    Port 2222
    ServerAliveInterval 60
    ServerAliveCountMax 3
    TCPKeepAlive yes

Host person2-internet
    HostName PERSON2-ÖFFENTLICHE-IP
    User person2-benutzername
    Port 2222
    ServerAliveInterval 60
    ServerAliveCountMax 3
    TCPKeepAlive yes
```

**Jetzt super einfach über Internet:**
```bash
# Statt: ssh -p 2222 person1@89.247.123.45
# Einfach:
ssh person1-internet
```

---

# Phase 10: Internet-Abschluss-Challenge
*"Zeigt was ihr über Internet-Administration gelernt habt!"*

## Challenge: Weltweites Gruppen-Monitoring-System

```bash
# Internet-Monitoring-Script erstellen
nano ~/internet_group_monitor.sh
```

**Script-Inhalt:**
```bash
#!/bin/bash
echo "===== INTERNET-GRUPPEN-NETZWERK-MONITOR ====="
echo "Gestartet: $(date)"
echo "Von: $(curl -s ipinfo.io/city), $(curl -s ipinfo.io/country)"
echo

echo "LOKALES SYSTEM:"
echo "- Hostname: $(hostname)"
echo "- Öffentliche IP: $(curl -s ifconfig.me)"
echo "- Standort: $(curl -s ipinfo.io/city)"
echo "- Speicher frei: $(free -h | grep Mem | awk '{print $7}')"
echo "- Internet-Speed: $(speedtest-cli --simple | grep Download)"
echo

if [ "$1" ]; then
    echo "INTERNET-REMOTE-SYSTEM: $1"
    start_time=$(date +%s)
    ssh "$1" "
        echo '- Hostname:' \$(hostname)
        echo '- Öffentliche IP:' \$(curl -s ifconfig.me)
        echo '- Standort:' \$(curl -s ipinfo.io/city), \$(curl -s ipinfo.io/country)
        echo '- Speicher frei:' \$(free -h | grep Mem | awk '{print \$7}')
        echo '- Lokale Zeit:' \$(date)
    "
    end_time=$(date +%s)
    latency=$((end_time - start_time))
    echo "- Verbindungszeit: ${latency} Sekunden"
fi

echo
echo "Internet-Ping-Tests:"
ping -c 3 google.de | tail -1
echo "===== INTERNET-MONITORING ABGESCHLOSSEN ====="
```

```bash
# Script ausführbar machen und testen
chmod +x ~/internet_group_monitor.sh

# Mit Internet-Partner testen
./internet_group_monitor.sh person1-internet
```

---

# Abschlussdokumentation

## Internet-SSH-Mission-Report (Vorschlag)

```bash
# Euren Internet-Abschlussbericht erstellen
nano ~/internet_ssh_mission_report.txt
```

**Template:**
```
===============================================
 INTERNET-SSH-NETZWERK MISSION - ABSCHLUSSBERICHT
===============================================

NAME: [Euer Name]
DATUM: $(date)
STANDORT: $(curl -s ipinfo.io/city), $(curl -s ipinfo.io/country)
GRUPPE: [Gruppenmitglieder auflisten]

TECHNISCHE INTERNET-DATEN:
- Meine lokale Windows-IP: ____________
- Meine WSL-IP: ____________  
- Meine öffentliche IP: ____________
- SSH-Port verwendet: 2222
- Router-Typ: ____________
- Internet-Provider: $(curl -s ipinfo.io/org)

ERFOLGREICHE INTERNET-VERBINDUNGEN:
[ ] Zu Person 1: Name _____, Öffentliche IP _____, Standort _____
[ ] Zu Person 2: Name _____, Öffentliche IP _____, Standort _____
[ ] Zu Person 3: Name _____, Öffentliche IP _____, Standort _____
[ ] Zu Person 4: Name _____, Öffentliche IP _____, Standort _____

DURCHGEFÜHRTE INTERNET-AUFGABEN:
[ ] WSL eingerichtet
[ ] SSH-Server für Internet konfiguriert
[ ] Router Port-Forwarding eingerichtet
[ ] Windows Firewall für Internet geöffnet
[ ] Internet-SSH-Verbindungen getestet
[ ] Nachrichten über Internet ausgetauscht
[ ] Dateien über Internet übertragen (SCP)
[ ] SSH-Keys für Internet-Sicherheit verwendet
[ ] Internet-Remote-Monitoring durchgeführt
[ ] Internet-Monitoring-Script entwickelt

NEUE INTERNET-SKILLS GELERNT:
1. Netzwerk-Konzepte:
   - Lokale vs. öffentliche IP-Adressen
   - Port-Forwarding im Router
   - NAT-Traversal
   - Internet-SSH-Sicherheit

2. Router-Administration:
   - Router-Interface bedienen
   - Port-Weiterleitungen konfigurieren
   - Firewall-Regeln erstellen

3. Linux-Internet-Tools:
   - ssh über Internet
   - scp für Internet-Dateitransfer
   - curl für IP/Standort-Abfragen
   - speedtest-cli für Internet-Geschwindigkeit

INTERNET-PROBLEME UND LÖSUNGEN:
- Problem 1: [Router-Konfiguration] → Lösung: [Port-Forwarding richtig eingestellt]
- Problem 2: [Firewall blockiert] → Lösung: [Windows-Regel hinzugefügt]
- Problem 3: [Verbindungs-Timeout] → Lösung: [SSH-Konfiguration optimiert]

PRAKTISCHE INTERNET-ANWENDUNGEN:
- Homelab-Server von unterwegs verwalten
- Raspberry Pi-Projekte remote steuern
- Website-Server administrieren
- IoT-Geräte überwachen
- Cloud-Server-Management
- Backup-Systeme kontrollieren

SICHERHEITS-ERKENNTNISSE:
- Router-Sicherheit ist kritisch
- SSH-Keys sind sicherer als Passwörter
- Firewall-Konfiguration essentiell
- Monitoring für Angriffs-Erkennung

BEWERTUNG (1-10):
- Technische Schwierigkeit: ___
- Internet-Komplexität: ___
- Interesse/Spaßfaktor: ___
- Praktischer Nutzen: ___
- Sicherheits-Bewusstsein: ___

FAZIT:
[Freie Bewertung der Internet-SSH-Mission - was habt ihr gelernt?
Wie fühlt es sich an, Computer über das Internet zu verwalten?]

===============================================
```

---

# Anhang: Wichtige Hinweise für Internet-SSH

## Nach PC-/Router-Neustart

**Router-Neustart checken:**
```bash
# Öffentliche IP prüfen (ändert sich manchmal)
curl ifconfig.me

# Port-Forwarding im Router prüfen
# (Browser → Router-Interface → Port-Weiterleitungen)
```

**PC-Neustart wiederholen:**
```bash
# WSL: SSH-Service starten
sudo service ssh start

# Windows: Port-Forwarding neu einrichten (WSL-IP ändert sich!)
wsl hostname -I
netsh interface portproxy show all
# Falls leer: netsh interface portproxy add... (siehe Phase 4.5)
```

## Internet-SSH Sicherheitstipps

**⚠️ Wichtige Sicherheitsregeln:**
- SSH-Port nach der Übung wieder schließen (Router-Konfiguration entfernen)
- Starke Passwörter verwenden
- SSH-Keys mit Passphrase schützen
- Regelmäßig SSH-Logs checken: `sudo journalctl -u ssh`
- Nur vertrauenswürdigen Personen Zugang gewähren

**Port-Forwarding nach Übung rückgängig machen:**
```
Router-Interface → Port-Weiterleitungen → SSH-Regel löschen
```

## Internet-SSH Spickzettel

```bash
# Wichtigste Internet-SSH-Befehle
ssh -p 2222 user@öffentliche-ip          # Internet-Verbindung
scp -P 2222 file.txt user@ip:/path/      # Internet-Dateitransfer
ssh user@ip "command"                     # Internet-Remote-Befehl
curl ifconfig.me                         # Öffentliche IP anzeigen
curl ipinfo.io                           # Standort-Info abrufen
speedtest-cli                            # Internet-Geschwindigkeit

# Router-Konfiguration
192.168.1.1                              # Router-Interface
Port-Forwarding: extern 2222 → intern 2222

# Troubleshooting
ping öffentliche-ip                      # Erreichbarkeit testen
telnet öffentliche-ip 2222              # Port-Test
nmap -p 2222 öffentliche-ip             # Port-Scan
```

---

Ihr habt erfolgreich ein sicheres SSH-Netzwerk über das Internet aufgebaut. Ihr könnt jetzt:
- Computer weltweit sicher verwalten
- Dateien verschlüsselt über Internet übertragen  
- Router professionell konfigurieren
- Netzwerk-Sicherheit einschätzen
- Wie echte System-Administratoren arbeiten

**Das ist der Grundstein für:**
- Server-Administration
- Cloud-Computing
- DevOps-Engineering  
- Cybersecurity
- Network-Engineering
