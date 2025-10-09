# Übung: Spezielle Berechtigungen, Prozesse & Systemverwaltung
## Praktische Übungen für Ubuntu

---

## Vorbereitung

Öffne ein Terminal in Ubuntu:
- **Tastenkombination:** `Ctrl + Alt + T`
- Oder über das Anwendungsmenü: "Terminal" suchen
- Verwende optional die WSL oder Multipass

**Wichtig:** Für viele Übungen in diesem Kapitel benötigst du `sudo`-Rechte!

---

## Teil 1: Spezielle Berechtigungen (45 Minuten)

### Aufgabe 1.1: Arbeitsverzeichnis erstellen

Erstelle ein Übungsverzeichnis und wechsle hinein:

```bash
mkdir ~/berechtigungen-uebung
cd ~/berechtigungen-uebung
```

**Erklärung:**
- `mkdir` = Make Directory (Verzeichnis erstellen)
- `~` = Dein Home-Verzeichnis
- `cd` = Change Directory (Verzeichnis wechseln)

---

### Aufgabe 1.2: Sticky Bit verstehen und setzen

**Szenario:** Du erstellst ein gemeinsames Verzeichnis, in dem mehrere Benutzer arbeiten sollen, aber jeder darf nur seine eigenen Dateien löschen.

Erstelle das Verzeichnis:

```bash
mkdir shared-folder
ls -ld shared-folder
```

**Erklärung:**
- `ls -ld` = Zeigt Details zum Verzeichnis selbst (nicht zum Inhalt)

Aktuell siehst du etwa: `drwxr-xr-x`

Setze jetzt das Sticky Bit:

```bash
chmod +t shared-folder
ls -ld shared-folder
```

**Was hat sich geändert?**
- Aus `drwxr-xr-x` wird `drwxr-xr-t`
- Das `t` am Ende zeigt das Sticky Bit an

**Alternative: Oktal-Notation**

```bash
chmod 1755 shared-folder
ls -ld shared-folder
```

**Erklärung:**
- `1` vor der normalen Berechtigung = Sticky Bit
- `755` = rwxr-xr-x

**Test durchführen:**

```bash
# Schreibrechte für alle setzen
chmod 1777 shared-folder

# Erste Datei erstellen
echo "Datei von $USER" > shared-folder/meine-datei.txt

# Überprüfe, dass die Datei existiert
ls -l shared-folder/
```

**Wichtiger Hinweis:**
Durch das Sticky Bit kann nun nur der Besitzer der Datei (oder root) diese löschen, selbst wenn alle Schreibrechte haben!

**Prüfe das /tmp Verzeichnis:**

```bash
ls -ld /tmp
```

**Ergebnis:** `drwxrwxrwt` - Das Sticky Bit ist bereits gesetzt!

---

### Aufgabe 1.3: SUID (Set User ID) verstehen

**Szenario:** Ein Programm soll mit den Rechten des Dateibesitzers ausgeführt werden, nicht mit deinen eigenen.

Schaue dir das klassische Beispiel `passwd` an:

```bash
ls -l /usr/bin/passwd
```

**Ausgabe:** `-rwsr-xr-x` - Das `s` bei User zeigt SUID an

**Erklärung:**
- `passwd` muss `/etc/shadow` ändern (nur root darf das)
- Durch SUID läuft `passwd` als root, auch wenn du es startest
- So kannst du dein Passwort ändern, ohne root zu sein!

**Eigenes Beispiel erstellen:**

Erstelle ein einfaches Script:

```bash
cat > mein-script.sh << 'EOF'
#!/bin/bash
echo "Dieses Script läuft als Benutzer: $(whoami)"
echo "Deine tatsächliche Benutzer-ID: $USER"
EOF

chmod +x mein-script.sh
./mein-script.sh
```

**Ergebnis:** Zeigt deinen Benutzernamen

Jetzt SUID setzen (funktioniert nur bei echten Programmen, nicht bei Shell-Scripts aus Sicherheitsgründen):

```bash
chmod u+s mein-script.sh
ls -l mein-script.sh
```

**Ausgabe:** `-rwsr-xr-x` - Das SUID-Bit ist gesetzt

**Alternative: Oktal-Notation**

```bash
chmod 4755 mein-script.sh
```

**Erklärung:**
- `4` vor der normalen Berechtigung = SUID
- `755` = rwxr-xr-x

**Wichtiger Sicherheitshinweis:**
SUID ist ein Sicherheitsrisiko! Setze es nur auf Programme, die es wirklich brauchen.

**Finde alle SUID-Programme im System:**

```bash
find /usr/bin -perm -4000 -type f 2>/dev/null
```

**Erklärung:**
- `find /usr/bin` = Suche in /usr/bin
- `-perm -4000` = Finde Dateien mit SUID-Bit
- `-type f` = Nur Dateien
- `2>/dev/null` = Unterdrücke Fehlermeldungen

---

### Aufgabe 1.4: SGID (Set Group ID) für Teamarbeit

**Szenario:** Du erstellst einen Projekt-Ordner. Alle neuen Dateien sollen automatisch zur Projekt-Gruppe gehören.

Erstelle das Verzeichnis:

```bash
mkdir team-projekt
ls -ld team-projekt
```

**Aktuell:** `drwxr-xr-x`

Setze SGID:

```bash
chmod g+s team-projekt
ls -ld team-projekt
```

**Ergebnis:** `drwxr-sr-x` - Das `s` bei Group zeigt SGID an

**Alternative: Oktal-Notation**

```bash
chmod 2775 team-projekt
```

**Erklärung:**
- `2` vor der normalen Berechtigung = SGID
- `775` = rwxrwxr-x

**Test durchführen:**

```bash
# Erstelle eine Datei im Verzeichnis
touch team-projekt/neue-datei.txt
ls -l team-projekt/
```

**Beobachtung:**
Die Datei erbt die Gruppe des Verzeichnisses!

**Praktisches Beispiel mit Gruppe:**

```bash
# Überprüfe deine aktuellen Gruppen
groups

# Setze optimale Rechte für Teamarbeit
chmod 2775 team-projekt

# Erstelle mehrere Dateien
touch team-projekt/dokument1.txt
touch team-projekt/dokument2.txt

# Überprüfe die Gruppenbesitzer
ls -l team-projekt/
```

Alle Dateien gehören zur gleichen Gruppe wie das Verzeichnis!

---

### Aufgabe 1.5: Alle speziellen Bits kombinieren

**Zusammenfassung der Oktal-Notation:**

```bash
# Normale Rechte: 755
# Mit Sticky Bit: 1755
# Mit SUID:       4755
# Mit SGID:       2755
```

**Test-Verzeichnis mit allen Bits:**

```bash
mkdir vollstaendig
chmod 7777 vollstaendig
ls -ld vollstaendig
```

**Ergebnis:** `drwsrwsrwt`
- `s` bei User = SUID (4)
- `s` bei Group = SGID (2)
- `t` am Ende = Sticky Bit (1)
- `4 + 2 + 1 = 7`

**Zurücksetzen:**

```bash
chmod 0755 vollstaendig
ls -ld vollstaendig
```

---

### Aufgabe 1.6: Überprüfung mit stat

Der `stat`-Befehl zeigt detaillierte Informationen:

```bash
stat shared-folder
```

**Ausgabe:**
- Access: Zeigt Rechte in Oktal und symbolisch
- Uid: Besitzer
- Gid: Gruppe

**Praktische Anwendung:**

```bash
# Verschiedene Verzeichnisse vergleichen
stat shared-folder team-projekt /tmp | grep Access
```

---

## Teil 2: Prozesse verwalten (45 Minuten)

### Aufgabe 2.1: Prozesse anzeigen mit ps

**Grundlegender Befehl:**

```bash
ps
```

**Erklärung:**
- Zeigt nur DEINE Prozesse in der aktuellen Shell
- Meist zu wenig Information

**Der wichtigste Befehl:**

```bash
ps aux
```

**Erklärung:**
- `a` = Alle Benutzer
- `u` = Detaillierte Informationen (User-Format)
- `x` = Auch Prozesse ohne Terminal

**Ausgabe verstehen:**

```bash
ps aux | head -5
```

**Spalten:**
- `USER` = Wer hat's gestartet?
- `PID` = Prozess-ID (eindeutige Nummer)
- `%CPU` = CPU-Auslastung in Prozent
- `%MEM` = Speicher-Auslastung in Prozent
- `VSZ` = Virtueller Speicher
- `RSS` = Tatsächlich genutzter Speicher
- `STAT` = Status (R=running, S=sleeping, Z=zombie)
- `START` = Startzeit
- `TIME` = CPU-Zeit
- `COMMAND` = Programmname

---

### Aufgabe 2.2: Prozesse filtern

**Suche nach Firefox:**

```bash
ps aux | grep firefox
```

**Erklärung:**
- `|` = Pipe (gibt Ausgabe an nächsten Befehl weiter)
- `grep firefox` = Filtert nach "firefox"

**Suche nach deinen Prozessen:**

```bash
ps aux | grep $USER
```

**Zähle deine Prozesse:**

```bash
ps aux | grep $USER | wc -l
```

**Erklärung:**
- `wc -l` = Zählt Zeilen

**Zeige die 10 speicherhungrigsten Prozesse:**

```bash
ps aux --sort=-%mem | head -10
```

**Zeige die 10 CPU-intensivsten Prozesse:**

```bash
ps aux --sort=-%cpu | head -10
```

---

### Aufgabe 2.3: Live-Überwachung mit top

**Starte top:**

```bash
top
```

**Wichtige Tasten in top:**
- `q` = Beenden (quit)
- `k` = Prozess beenden (kill) - fragt nach PID
- `M` = Nach Speicher sortieren (Shift+M)
- `P` = Nach CPU sortieren (Shift+P) - Standard
- `h` = Hilfe anzeigen
- `1` = Zeige alle CPU-Kerne einzeln

**Was du siehst:**

**Oberer Bereich (Systemübersicht):**
- Uptime = Wie lange läuft das System?
- Load average = Systemlast (1, 5, 15 Minuten)
- Tasks = Anzahl Prozesse
- %Cpu(s) = CPU-Auslastung
- MiB Mem = Speichernutzung

**Unterer Bereich:**
- Liste aller Prozesse, sortiert nach CPU-Nutzung

**Beende top:**
Drücke `q`

---

### Aufgabe 2.4: Bessere Alternative - htop

**Installation:**

```bash
sudo apt update
sudo apt install htop
```

**Starten:**

```bash
htop
```

**Vorteile von htop:**
- Farbige Anzeige
- Maus-Unterstützung
- Übersichtlicher
- Einfacher zu bedienen

**Wichtige Tasten in htop:**
- `F1` = Hilfe
- `F2` = Setup/Einstellungen
- `F3` = Suchen
- `F4` = Filter
- `F5` = Baumansicht (Prozess-Hierarchie)
- `F9` = Prozess beenden
- `F10` oder `q` = Beenden

**Beende htop:**
Drücke `F10` oder `q`

---

### Aufgabe 2.5: Prozesse beenden mit kill

**Starte einen Test-Prozess:**

```bash
sleep 300 &
```

**Erklärung:**
- `sleep 300` = Wartet 300 Sekunden
- `&` = Führt im Hintergrund aus

**Finde die PID:**

```bash
ps aux | grep sleep
```

Notiere die PID (z.B. 12345)

**Sanft beenden:**

```bash
kill 12345
```

**Erklärung:**
- Sendet Signal SIGTERM (15)
- Prozess kann noch aufräumen
- Standard-Signal von `kill`

**Überprüfen:**

```bash
ps aux | grep sleep
```

Der Prozess sollte weg sein.

**Falls der Prozess nicht beendet wird:**

```bash
sleep 300 &
# Notiere PID
kill -9 12345  # Ersetze 12345 mit deiner PID
```

**Erklärung:**
- `-9` = Signal SIGKILL
- Erzwingt sofortigen Abbruch
- **Nur als letzte Lösung verwenden!**

---

### Aufgabe 2.6: Mehrere Prozesse beenden mit killall

**Starte mehrere Test-Prozesse:**

```bash
sleep 200 &
sleep 200 &
sleep 200 &
```

**Überprüfe:**

```bash
ps aux | grep sleep
```

Du solltest 3 sleep-Prozesse sehen.

**Beende alle auf einmal:**

```bash
killall sleep
```

**Überprüfe:**

```bash
ps aux | grep sleep
```

Alle sleep-Prozesse sollten weg sein.

**Unterschied:**
- `kill` = Braucht PID (Nummer)
- `killall` = Braucht Programmname

---

### Aufgabe 2.7: Signale verstehen

**Liste aller Signale:**

```bash
kill -l
```

**Die wichtigsten Signale:**

| Signal | Nummer | Bedeutung |
|--------|--------|-----------|
| SIGTERM | 15 | Sanft beenden (Standard) |
| SIGKILL | 9 | Sofort töten (nicht abfangbar) |
| SIGHUP | 1 | Konfiguration neu laden |
| SIGINT | 2 | Abbruch (Ctrl+C) |
| SIGSTOP | 19 | Anhalten |
| SIGCONT | 18 | Fortsetzen |

**Praktisches Beispiel:**

```bash
# Starte einen Prozess
sleep 500 &
PID=$!  # Speichert PID des letzten Hintergrundprozesses

# Verschiedene Signale testen
kill -SIGTERM $PID  # Oder: kill -15 $PID
```

**Mit Namen oder Nummer:**

```bash
sleep 500 &
PID=$!

# Beide Befehle sind identisch:
kill -15 $PID
kill -TERM $PID
```

---

### Aufgabe 2.8: Hintergrundprozesse

**Prozess im Hintergrund starten:**

```bash
sleep 100 &
```

**Erklärung:**
- `&` = Startet Prozess im Hintergrund
- Du bekommst sofort die Shell zurück

**Aktive Hintergrundprozesse anzeigen:**

```bash
jobs
```

**Ausgabe:** `[1]+ Running   sleep 100 &`

**Prozess im Vordergrund starten und dann pausieren:**

```bash
sleep 200
```

Drücke `Ctrl+Z`

**Ausgabe:** `[1]+ Stopped   sleep 200`

**Pausierte Prozesse weiterlaufen lassen:**

```bash
bg
```

**Erklärung:**
- `bg` = background
- Prozess läuft weiter, aber im Hintergrund

**Prozess in den Vordergrund holen:**

```bash
fg
```

**Erklärung:**
- `fg` = foreground
- Prozess blockiert wieder die Shell

Beende mit `Ctrl+C`

**Mehrere Hintergrund-Jobs:**

```bash
sleep 100 &
sleep 200 &
sleep 300 &
jobs
```

**Bestimmten Job in den Vordergrund holen:**

```bash
fg %1  # Holt Job 1
```

**Oder:**

```bash
fg %2  # Holt Job 2
```

---

### Aufgabe 2.9: Prozess-Prioritäten mit nice

**Starte Prozess mit niedriger Priorität:**

```bash
nice -n 10 sleep 500 &
```

**Erklärung:**
- `nice -n 10` = Setzt Nice-Wert auf 10
- Höhere Zahl = niedrigere Priorität
- Bereich: -20 (höchste) bis 19 (niedrigste)
- Standard: 0

**Überprüfe den Nice-Wert:**

```bash
ps -l | grep sleep
```

**Spalte NI zeigt den Nice-Wert:**

**Starte mit hoher Priorität (nur root):**

```bash
sudo nice -n -10 sleep 500 &
```

**Wichtig:**
- Normale Benutzer können nur Priorität verringern (0-19)
- Root kann auch erhöhen (-20 bis 0)

---

### Aufgabe 2.10: Priorität ändern mit renice

**Starte einen Prozess:**

```bash
sleep 600 &
PID=$!
echo "PID: $PID"
```

**Überprüfe aktuelle Priorität:**

```bash
ps -l -p $PID
```

**Ändere Priorität:**

```bash
renice -n 15 -p $PID
```

**Überprüfe erneut:**

```bash
ps -l -p $PID
```

**Priorität für alle eigenen Prozesse ändern:**

```bash
renice -n 10 -u $USER
```

**Wichtig:**
- Normale Benutzer können Priorität nur erhöhen (netter sein)
- Root kann in beide Richtungen ändern

---

## Teil 3: Systemdienste mit systemctl (40 Minuten)

### Aufgabe 3.1: Dienste-Status überprüfen

**Überprüfe SSH-Dienst:**

```bash
systemctl status ssh
```

**Oder auf manchen Systemen:**

```bash
systemctl status sshd
```

**Was du siehst:**
- **Loaded:** Wo ist die Konfigurationsdatei?
- **Active:** Läuft der Dienst? Seit wann?
- **Main PID:** Prozess-ID
- **Tasks:** Anzahl Threads
- **Memory:** Speicherverbrauch
- **Logs:** Letzte Log-Einträge

**Ausgabe verstehen:**

```bash
# Grün = läuft
# Rot = gestoppt oder Fehler
# Gelb = andere Zustände
```

---

### Aufgabe 3.2: Dienst starten und stoppen

**Installation eines Test-Dienstes:**

```bash
sudo apt update
sudo apt install apache2
```

**Status prüfen:**

```bash
systemctl status apache2
```

**Dienst stoppen:**

```bash
sudo systemctl stop apache2
systemctl status apache2
```

**Beobachtung:** Status ist jetzt "inactive (dead)"

**Dienst starten:**

```bash
sudo systemctl start apache2
systemctl status apache2
```

**Beobachtung:** Status ist jetzt "active (running)"

**Dienst neu starten:**

```bash
sudo systemctl restart apache2
```

**Erklärung:**
- `restart` = Stoppen + Starten
- Nützlich nach Konfigurationsänderungen

**Konfiguration neu laden (ohne Neustart):**

```bash
sudo systemctl reload apache2
```

**Erklärung:**
- `reload` = Liest Konfiguration neu ein
- Dienst läuft weiter
- Keine Unterbrechung
- **Nicht alle Dienste unterstützen reload!**

---

### Aufgabe 3.3: Autostart konfigurieren

**Autostart aktivieren:**

```bash
sudo systemctl enable apache2
```

**Erklärung:**
- Dienst startet automatisch beim Booten
- **Startet den Dienst NICHT sofort!**

**Überprüfen:**

```bash
systemctl is-enabled apache2
```

**Ausgabe:** `enabled`

**Autostart deaktivieren:**

```bash
sudo systemctl disable apache2
```

**Überprüfen:**

```bash
systemctl is-enabled apache2
```

**Ausgabe:** `disabled`

**Beides gleichzeitig:**

```bash
sudo systemctl enable --now apache2
```

**Erklärung:**
- Aktiviert Autostart UND startet sofort
- Sehr praktisch!

**Deaktivieren und stoppen:**

```bash
sudo systemctl disable --now apache2
```

---

### Aufgabe 3.4: Unterschied start/enable verstehen

**Wichtige Unterscheidung:**

| Befehl | Bedeutung | Wirkt |
|--------|-----------|-------|
| `start` | Jetzt starten | Sofort |
| `stop` | Jetzt stoppen | Sofort |
| `enable` | Autostart EIN | Nächster Boot |
| `disable` | Autostart AUS | Nächster Boot |

**Test-Szenario:**

```bash
# Dienst ist gestoppt und deaktiviert
sudo systemctl stop apache2
sudo systemctl disable apache2

# Status prüfen
systemctl status apache2    # inactive
systemctl is-enabled apache2  # disabled

# Nur starten (ohne enable)
sudo systemctl start apache2

# Jetzt läuft er
systemctl status apache2    # active

# Aber beim Neustart würde er NICHT starten
systemctl is-enabled apache2  # disabled

# Jetzt enable (ohne start)
sudo systemctl stop apache2
sudo systemctl enable apache2

# Er läuft NICHT
systemctl status apache2    # inactive

# Aber würde beim Neustart starten
systemctl is-enabled apache2  # enabled
```

**Häufiger Fehler:**
"Mein Dienst läuft, aber nach Reboot nicht mehr" → Du hast `enable` vergessen!

---

### Aufgabe 3.5: Alle Dienste auflisten

**Alle geladenen Dienste:**

```bash
systemctl list-units --type=service
```

**Nur laufende Dienste:**

```bash
systemctl list-units --type=service --state=running
```

**Nur fehlgeschlagene Dienste:**

```bash
systemctl list-units --type=service --state=failed
```

**Alle installierten Dienste (auch inaktive):**

```bash
systemctl list-unit-files --type=service
```

**Mit Autostart-Status:**

```bash
systemctl list-unit-files --type=service | grep enabled
```

---

### Aufgabe 3.6: Wichtige Dienste kennenlernen

**SSH-Dienst (Remote-Zugriff):**

```bash
systemctl status ssh      # Debian/Ubuntu
systemctl status sshd     # Red Hat/CentOS
```

**Netzwerk:**

```bash
systemctl status networking  # Ältere Systeme
systemctl status NetworkManager  # Neuere Systeme
```

**Cron (zeitgesteuerte Aufgaben):**

```bash
systemctl status cron   # Debian/Ubuntu
systemctl status crond  # Red Hat/CentOS
```

**Firewall:**

```bash
systemctl status ufw  # Ubuntu
systemctl status firewalld  # Red Hat/CentOS
```

---

### Aufgabe 3.7: Systemd-Logs mit journalctl

**Alle Logs anzeigen:**

```bash
journalctl
```

**Erklärung:**
- Zeigt alle Systemlogs
- Älteste zuerst
- Mit `less`-Ansicht (Space = Seite weiter, q = Beenden)

**Nur letzte 50 Zeilen:**

```bash
journalctl -n 50
```

**Logs live verfolgen:**

```bash
journalctl -f
```

**Erklärung:**
- `-f` = follow (wie `tail -f`)
- Zeigt neue Logs sofort an
- Beenden mit `Ctrl+C`

**Logs für bestimmten Dienst:**

```bash
journalctl -u apache2
```

**Nur Fehler:**

```bash
journalctl -p err
```

**Prioritäten:**
- `emerg` = System unbenutzbar
- `alert` = Sofortige Aktion nötig
- `crit` = Kritisch
- `err` = Fehler
- `warning` = Warnung
- `notice` = Hinweis
- `info` = Information
- `debug` = Debug-Infos

**Logs von heute:**

```bash
journalctl --since today
```

**Logs der letzten Stunde:**

```bash
journalctl --since "1 hour ago"
```

**Logs zwischen zwei Zeitpunkten:**

```bash
journalctl --since "2025-01-01" --until "2025-01-07"
```

---

## Teil 4: Log-Dateien lesen (30 Minuten)

### Aufgabe 4.1: Traditionelle Logs in /var/log

**Übersicht der Log-Verzeichnisse:**

```bash
ls -lh /var/log/
```

**Wichtigste Log-Dateien:**
- `syslog` = Allgemeine Systemmeldungen
- `auth.log` = Authentifizierungs-Logs (Login-Versuche)
- `kern.log` = Kernel-Meldungen
- `dmesg` = Boot-Meldungen und Hardware
- `apache2/` = Webserver-Logs
- `apt/` = Paketmanager-Logs

---

### Aufgabe 4.2: System-Log lesen

**Letzte Zeilen von syslog:**

```bash
sudo tail /var/log/syslog
```

**Erklärung:**
- `tail` = Zeigt letzte 10 Zeilen
- Neueste Einträge zuerst

**Mehr Zeilen:**

```bash
sudo tail -n 50 /var/log/syslog
```

**Live verfolgen:**

```bash
sudo tail -f /var/log/syslog
```

**Beenden:** `Ctrl+C`

**Nach bestimmtem Wort suchen:**

```bash
sudo grep "error" /var/log/syslog
```

**Groß-/Kleinschreibung ignorieren:**

```bash
sudo grep -i "error" /var/log/syslog
```

---

### Aufgabe 4.3: Authentifizierungs-Logs

**Login-Versuche anzeigen:**

```bash
sudo tail /var/log/auth.log
```

**Erfolgreiche Logins:**

```bash
sudo grep "Accepted" /var/log/auth.log
```

**Fehlgeschlagene Login-Versuche:**

```bash
sudo grep "Failed" /var/log/auth.log
```

**sudo-Befehle anzeigen:**

```bash
sudo grep "sudo" /var/log/auth.log
```

**SSH-Verbindungen:**

```bash
sudo grep "sshd" /var/log/auth.log
```

---

### Aufgabe 4.4: Kernel-Meldungen mit dmesg

**Alle Kernel-Meldungen:**

```bash
dmesg
```

**Mit Zeitstempel:**

```bash
dmesg -T
```

**Letzte 20 Zeilen:**

```bash
dmesg | tail -20
```

**Nach Fehler suchen:**

```bash
dmesg | grep -i error
```

**USB-Geräte:**

```bash
dmesg | grep -i usb
```

**Live-Ansicht:**

```bash
dmesg -w
```

**Beenden:** `Ctrl+C`

---

### Aufgabe 4.5: Logs filtern und analysieren

**Häufigste Fehler finden:**

```bash
sudo grep -i error /var/log/syslog | cut -d' ' -f5- | sort | uniq -c | sort -rn | head -10
```

**Erklärung:**
- `grep -i error` = Finde Fehler
- `cut -d' ' -f5-` = Schneide Datum/Zeit weg
- `sort` = Sortiere
- `uniq -c` = Zähle gleiche Zeilen
- `sort -rn` = Sortiere numerisch, absteigend
- `head -10` = Zeige Top 10

**Zeitbasierte Filterung:**

```bash
sudo grep "Jan  7" /var/log/syslog
```

**Mehrere Log-Dateien durchsuchen:**

```bash
sudo grep -r "error" /var/log/*.log
```

---

## Teil 5: Cron - Aufgaben automatisieren (40 Minuten)

### Aufgabe 5.1: Crontab verstehen

**Syntax:**

```
* * * * * befehl
│ │ │ │ │
│ │ │ │ └─ Wochentag (0-7, 0 und 7 = Sonntag)
│ │ │ └─── Monat (1-12)
│ │ └───── Tag (1-31)
│ └─────── Stunde (0-23)
└───────── Minute (0-59)
```

**Beispiele:**

| Zeitplan | Cron-Syntax | Bedeutung |
|----------|-------------|-----------|
| Jeden Tag 3 Uhr | `0 3 * * *` | Täglich um 3:00 |
| Jede volle Stunde | `0 * * * *` | Stündlich |
| Alle 15 Minuten | `*/15 * * * *` | Viertelstündlich |
| Montags 8 Uhr | `0 8 * * 1` | Jede Woche |
| Ersten jeden Monats | `0 0 1 * *` | Monatlich |
| Werktags 9 Uhr | `0 9 * * 1-5` | Mo-Fr |

---

### Aufgabe 5.2: Ersten Cronjob erstellen

**Cronjob-Editor öffnen:**

```bash
crontab -e
```

**Beim ersten Mal:** System fragt nach bevorzugtem Editor (nano empfohlen für Anfänger)

**Erstelle ein Test-Script:**

```bash
cat > ~/cronjob-test.sh << 'EOF'
#!/bin/bash
echo "Cronjob ausgeführt am $(date)" >> ~/cron-log.txt
EOF

chmod +x ~/cronjob-test.sh
```

**Füge in crontab ein:**

```
*/1 * * * * ~/cronjob-test.sh
```

**Erklärung:**
- `*/1` = Jede Minute
- Führt das Script jede Minute aus

**Speichern:**
- In nano: `Ctrl+O`, Enter, `Ctrl+X`
- In vim: `Esc`, `:wq`, Enter

**Überprüfen:**

```bash
crontab -l
```

**Warte 2 Minuten und prüfe:**

```bash
cat ~/cron-log.txt
```

Du solltest mindestens 2 Einträge sehen!

---

### Aufgabe 5.3: Praktische Cronjobs

**Tägliches Backup um 3 Uhr:**

```bash
crontab -e
```

Füge hinzu:

```
0 3 * * * tar -czf ~/backup-$(date +\%Y\%m\%d).tar.gz ~/dokumente/
```

**Erklärung:**
- `\%` = Escapes das % für cron
- Erstellt täglich um 3 Uhr ein Backup

**Alte Dateien aufräumen (monatlich):**

```
0 2 1 * * find ~/downloads/ -type f -mtime +30 -delete
```

**Erklärung:**
- `0 2 1 * *` = Ersten jeden Monats um 2 Uhr
- `-mtime +30` = Älter als 30 Tage
- `-delete` = Löschen

**System-Check alle 15 Minuten:**

```
*/15 * * * * systemctl is-active apache2 || systemctl start apache2
```

**Erklärung:**
- Prüft alle 15 Minuten, ob Apache läuft
- Startet ihn neu, falls gestoppt

**Wöchentlicher Report (Montags 8 Uhr):**

```
0 8 * * 1 df -h > ~/speicher-report-$(date +\%Y\%m\%d).txt
```

---

### Aufgabe 5.4: Cronjob mit Log-Ausgabe

**Problem:** Cron-Ausgaben gehen oft verloren

**Lösung:** Umleitung in Log-Datei

```bash
crontab -e
```

Füge hinzu:

```
*/5 * * * * ~/mein-script.sh >> ~/cron-output.log 2>&1
```

**Erklärung:**
- `>>` = Anhängen (nicht überschreiben)
- `2>&1` = Fehler auch in die Datei umleiten

**Test:**

Erstelle Script:

```bash
cat > ~/mein-script.sh << 'EOF'
#!/bin/bash
echo "Script gestartet: $(date)"
echo "Aktuelle Prozesse: $(ps aux | wc -l)"
EOF

chmod +x ~/mein-script.sh
```

Füge in crontab ein:

```
*/2 * * * * ~/mein-script.sh >> ~/cron-output.log 2>&1
```

**Warte 4 Minuten und prüfe:**

```bash
cat ~/cron-output.log
```

---

### Aufgabe 5.5: Cronjob-Verwaltung

**Alle Cronjobs anzeigen:**

```bash
crontab -l
```

**Cronjob bearbeiten:**

```bash
crontab -e
```

**ALLE Cronjobs löschen:**

```bash
crontab -r
```

**VORSICHT:** Löscht ohne Rückfrage!

**Sicherer: Backup vor dem Löschen:**

```bash
crontab -l > ~/crontab-backup.txt
crontab -r
```

**Wiederherstellen:**

```bash
crontab ~/crontab-backup.txt
```

---

### Aufgabe 5.6: Cron-Verzeichnisse

**Alternative zu crontab:** Fertige Verzeichnisse

```bash
ls -lh /etc/cron.*
```

**Verzeichnisse:**
- `/etc/cron.hourly/` = Stündlich
- `/etc/cron.daily/` = Täglich
- `/etc/cron.weekly/` = Wöchentlich
- `/etc/cron.monthly/` = Monatlich

**Script in Verzeichnis legen:**

```bash
sudo nano /etc/cron.daily/mein-backup
```

Inhalt:

```bash
#!/bin/bash
tar -czf /backup/daily-$(date +%Y%m%d).tar.gz /home/
```

**Ausführbar machen:**

```bash
sudo chmod +x /etc/cron.daily/mein-backup
```

**Testen (sofort ausführen):**

```bash
sudo run-parts --test /etc/cron.daily
```

**Vorteile:**
- Einfacher als crontab-Syntax
- Übersichtlich

**Nachteile:**
- Keine exakte Zeitsteuerung
- Feste Intervalle

---

### Aufgabe 5.7: Cronjob debuggen

**Problem:** Cronjob funktioniert nicht

**Häufige Fehler:**

1. **Script nicht ausführbar**

```bash
chmod +x ~/mein-script.sh
```

2. **Falsche Pfade**

```bash
# FALSCH in crontab:
./mein-script.sh

# RICHTIG in crontab:
/home/username/mein-script.sh
```

3. **Keine Ausgabe sichtbar**

```bash
# Immer Logs schreiben:
*/5 * * * * ~/script.sh >> ~/log.txt 2>&1
```

4. **Umgebungsvariablen fehlen**

```bash
# Pfade im Script setzen:
#!/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
export PATH
```

**Cron-Logs prüfen:**

```bash
sudo grep CRON /var/log/syslog
```

**Test: Cronjob sofort ausführen**

Nicht möglich, aber zum Testen:

```bash
# Setze Cronjob auf nächste Minute
date  # Aktuelle Zeit
crontab -e
# Setze: 15 14 * * * ~/script.sh  (eine Minute in der Zukunft)
```

---

## Teil 6: Kombinierte Übung - Systemüberwachung (45 Minuten)

### Aufgabe 6.1: Monitoring-Script erstellen

**Szenario:** Erstelle ein Script, das regelmäßig das System überwacht.

Erstelle das Script:

```bash
cat > ~/system-monitor.sh << 'EOF'
#!/bin/bash

# Log-Datei
LOGFILE=~/system-monitor.log
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Separator
echo "==================== $DATE ====================" >> $LOGFILE

# CPU-Auslastung
echo "=== CPU Load ===" >> $LOGFILE
uptime >> $LOGFILE

# Speicher
echo "=== Memory ===" >> $LOGFILE
free -h >> $LOGFILE

# Festplatten
echo "=== Disk Usage ===" >> $LOGFILE
df -h >> $LOGFILE

# Top 5 CPU-Prozesse
echo "=== Top 5 CPU Processes ===" >> $LOGFILE
ps aux --sort=-%cpu | head -6 >> $LOGFILE

# Top 5 Memory-Prozesse
echo "=== Top 5 Memory Processes ===" >> $LOGFILE
ps aux --sort=-%mem | head -6 >> $LOGFILE

# Wichtige Dienste
echo "=== Service Status ===" >> $LOGFILE
systemctl is-active ssh >> $LOGFILE
systemctl is-active cron >> $LOGFILE

echo "" >> $LOGFILE
EOF

chmod +x ~/system-monitor.sh
```

**Test:**

```bash
~/system-monitor.sh
cat ~/system-monitor.log
```

---

### Aufgabe 6.2: Automatische Überwachung mit Cron

**Füge Cronjob hinzu:**

```bash
crontab -e
```

Füge ein:

```
*/30 * * * * ~/system-monitor.sh
```

**Erklärung:**
- Läuft alle 30 Minuten
- Schreibt in Log-Datei

**Warte 30 Minuten und prüfe:**

```bash
cat ~/system-monitor.log
```

---

### Aufgabe 6.3: Alarme bei hoher Last

**Erweitertes Monitoring-Script:**

```bash
cat > ~/system-alert.sh << 'EOF'
#!/bin/bash

# Schwellenwerte
CPU_THRESHOLD=80
MEM_THRESHOLD=80

# Aktuelle Werte
CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
MEM_USAGE=$(free | grep Mem | awk '{print int($3/$2 * 100)}')

# Log-Datei
LOGFILE=~/system-alerts.log
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Prüfe CPU
if (( $(echo "$CPU_USAGE > $CPU_THRESHOLD" | bc -l) )); then
    echo "$DATE - WARNING: High CPU usage: ${CPU_USAGE}%" >> $LOGFILE
fi

# Prüfe Speicher
if [ $MEM_USAGE -gt $MEM_THRESHOLD ]; then
    echo "$DATE - WARNING: High Memory usage: ${MEM_USAGE}%" >> $LOGFILE
fi
EOF

chmod +x ~/system-alert.sh
```

**Test:**

```bash
~/system-alert.sh
cat ~/system-alerts.log
```

**In Cron einfügen:**

```bash
crontab -e
```

Füge hinzu:

```
*/10 * * * * ~/system-alert.sh
```

---

### Aufgabe 6.4: Apache-Watchdog

**Script erstellt, das Apache überwacht und bei Bedarf neu startet:**

```bash
cat > ~/apache-watchdog.sh << 'EOF'
#!/bin/bash

LOGFILE=~/apache-watchdog.log
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Prüfe ob Apache läuft
if ! systemctl is-active --quiet apache2; then
    echo "$DATE - Apache is down! Restarting..." >> $LOGFILE
    sudo systemctl start apache2
    
    if systemctl is-active --quiet apache2; then
        echo "$DATE - Apache successfully restarted" >> $LOGFILE
    else
        echo "$DATE - ERROR: Failed to restart Apache!" >> $LOGFILE
    fi
else
    echo "$DATE - Apache is running fine" >> $LOGFILE
fi
EOF

chmod +x ~/apache-watchdog.sh
```

**Sudo-Rechte für Script:**

```bash
sudo visudo
```

Füge am Ende hinzu (ersetze `username` mit deinem Benutzernamen):

```
username ALL=(ALL) NOPASSWD: /bin/systemctl start apache2
username ALL=(ALL) NOPASSWD: /bin/systemctl status apache2
```

**Test:**

```bash
# Stoppe Apache
sudo systemctl stop apache2

# Führe Watchdog aus
~/apache-watchdog.sh

# Prüfe Log
cat ~/apache-watchdog.log
```

**In Cron einfügen:**

```bash
crontab -e
```

```
*/5 * * * * ~/apache-watchdog.sh
```

---

## Teil 7: Prozess-Verwaltung Praxis (30 Minuten)

### Aufgabe 7.1: Zombie-Prozesse verstehen

**Was ist ein Zombie?**
- Prozess ist beendet, aber noch in Prozesstabelle
- Wartet darauf, dass Elternprozess den Exit-Status abholt
- Status: `Z` in `ps`

**Zombie-Prozesse finden:**

```bash
ps aux | grep 'Z'
```

**Bessere Methode:**

```bash
ps aux | awk '$8=="Z" {print}'
```

**Zombie-Anzahl:**

```bash
ps aux | awk '$8=="Z"' | wc -l
```

**Zombies "töten":**
- Zombies können NICHT getötet werden!
- Man muss den Elternprozess beenden
- Oder warten, bis Elternprozess aufräumt

**Elternprozess eines Zombies finden:**

```bash
ps -o ppid= -p <ZOMBIE_PID>
```

---

### Aufgabe 7.2: Prozess-Hierarchie visualisieren

**Mit pstree:**

```bash
sudo apt install psmisc
pstree
```

**Mit PIDs:**

```bash
pstree -p
```

**Nur deine Prozesse:**

```bash
pstree $USER
```

**Bestimmten Prozess und seine Kinder:**

```bash
pstree -p <PID>
```

---

### Aufgabe 7.3: Ressourcen-intensive Prozesse identifizieren

**Top 10 nach CPU:**

```bash
ps aux --sort=-%cpu | head -11
```

**Top 10 nach Speicher:**

```bash
ps aux --sort=-%mem | head -11
```

**Prozesse mit mehr als 5% CPU:**

```bash
ps aux | awk '$3 > 5.0 {print}'
```

**Speicherfresser (über 100MB):**

```bash
ps aux | awk '$6 > 100000 {print}'
```

---

### Aufgabe 7.4: Prozess-Informationen detailliert

**Detaillierte Info zu einem Prozess:**

```bash
ps -fp <PID>
```

**Alle offenen Dateien eines Prozesses:**

```bash
sudo lsof -p <PID>
```

**Prozess-Umgebungsvariablen:**

```bash
cat /proc/<PID>/environ | tr '\0' '\n'
```

**Prozess-Kommandozeile:**

```bash
cat /proc/<PID>/cmdline
```

---

## Zusammenfassung

### Was hast du gelernt?

**Spezielle Berechtigungen:**
- Sticky Bit (`chmod +t` oder `1xxx`) - Nur Besitzer darf löschen
- SUID (`chmod u+s` oder `4xxx`) - Ausführen als Dateibesitzer
- SGID (`chmod g+s` oder `2xxx`) - Gruppe vererben

**Prozess-Verwaltung:**
- `ps aux` - Alle Prozesse anzeigen
- `top` / `htop` - Live-Überwachung
- `kill` / `killall` - Prozesse beenden
- Signale: 15 (TERM) = sanft, 9 (KILL) = sofort
- Hintergrund: `&`, `bg`, `fg`, `jobs`
- Priorität: `nice`, `renice`

**Systemdienste:**
- `systemctl start/stop/restart` - Dienst steuern (jetzt)
- `systemctl enable/disable` - Autostart (beim Boot)
- `systemctl status` - Status prüfen
- `systemctl is-active` - Läuft er?
- `systemctl is-enabled` - Startet beim Boot?

**Logs:**
- `journalctl` - Systemd-Logs
- `/var/log/syslog` - System-Logs
- `/var/log/auth.log` - Login-Versuche
- `dmesg` - Kernel/Hardware-Meldungen

**Cron:**
- `crontab -e` - Cronjobs bearbeiten
- `crontab -l` - Cronjobs anzeigen
- Syntax: `Minute Stunde Tag Monat Wochentag Befehl`
- Verzeichnisse: `/etc/cron.daily/` etc.

### Wichtigste Befehle

**Berechtigungen:**
```bash
chmod +t verzeichnis/          # Sticky Bit
chmod u+s datei               # SUID
chmod g+s verzeichnis/        # SGID
chmod 1755 verzeichnis/       # Oktal
```

**Prozesse:**
```bash
ps aux                        # Alle Prozesse
ps aux | grep programm        # Filtern
top                           # Live-Ansicht
htop                          # Bessere Alternative
kill PID                      # Sanft beenden
kill -9 PID                   # Erzwingen
killall programm              # Nach Name beenden
nice -n 10 befehl            # Mit Priorität starten
renice -n 5 -p PID           # Priorität ändern
```

**Dienste:**
```bash
systemctl status dienst       # Status prüfen
systemctl start dienst        # Starten
systemctl stop dienst         # Stoppen
systemctl restart dienst      # Neustarten
systemctl enable dienst       # Autostart ein
systemctl disable dienst      # Autostart aus
systemctl enable --now dienst # Beides gleichzeitig
```

**Logs:**
```bash
journalctl                    # Alle Logs
journalctl -u dienst         # Logs eines Dienstes
journalctl -f                # Live verfolgen
journalctl --since today     # Von heute
tail -f /var/log/syslog      # Syslog live
dmesg -T                     # Kernel-Logs
```

**Cron:**
```bash
crontab -e                   # Bearbeiten
crontab -l                   # Anzeigen
crontab -r                   # Löschen (VORSICHT!)
```

---

## Weiterführende Übungen (Optional)

### Übung 1: System-Health-Dashboard

Erstelle ein Script, das ein übersichtliches System-Dashboard erstellt:

```bash
cat > ~/dashboard.sh << 'EOF'
#!/bin/bash

clear
echo "================================"
echo "    SYSTEM HEALTH DASHBOARD"
echo "================================"
echo ""
echo "=== Zeit ==="
date
echo ""
echo "=== Uptime ==="
uptime
echo ""
echo "=== CPU Load (1, 5, 15 min) ==="
cat /proc/loadavg | awk '{print $1, $2, $3}'
echo ""
echo "=== Memory Usage ==="
free -h | grep Mem | awk '{print "Used: " $3 " / Total: " $2}'
echo ""
echo "=== Disk Usage ==="
df -h / | tail -1 | awk '{print "Used: " $3 " / Total: " $2 " (" $5 " used)"}'
echo ""
echo "=== Top 5 CPU Processes ==="
ps aux --sort=-%cpu | head -6 | tail -5 | awk '{print $11, "-", $3"%"}'
echo ""
echo "=== Failed Services ==="
systemctl list-units --failed
echo ""
EOF

chmod +x ~/dashboard.sh
```

---

### Übung 2: Automatische Log-Rotation

Erstelle ein Script, das alte Logs archiviert:

```bash
cat > ~/log-rotation.sh << 'EOF'
#!/bin/bash

LOGDIR=~/logs
ARCHIVEDIR=~/logs/archive
DAYS_TO_KEEP=7

# Erstelle Verzeichnisse
mkdir -p $ARCHIVEDIR

# Finde alte Logs
find $LOGDIR -maxdepth 1 -name "*.log" -mtime +$DAYS_TO_KEEP -type f | while read logfile; do
    # Komprimiere und verschiebe
    gzip "$logfile"
    mv "${logfile}.gz" "$ARCHIVEDIR/"
    echo "Archived: $(basename $logfile)"
done
EOF

chmod +x ~/log-rotation.sh
```

---

### Übung 3: Prozess-Killer bei hoher Last

Erstelle ein Script, das automatisch ressourcen-intensive Prozesse beendet:

```bash
cat > ~/process-killer.sh << 'EOF'
#!/bin/bash

CPU_LIMIT=90
MEMORY_LIMIT=90

# Finde Prozesse über CPU-Limit
ps aux --sort=-%cpu | awk -v limit=$CPU_LIMIT '$3 > limit && NR>1 {print $2, $11, $3"%"}' | while read pid cmd cpu; do
    echo "Killing high CPU process: $cmd (PID: $pid, CPU: $cpu)"
    kill $pid
done

# Finde Prozesse über Memory-Limit
ps aux --sort=-%mem | awk -v limit=$MEMORY_LIMIT '$4 > limit && NR>1 {print $2, $11, $4"%"}' | while read pid cmd mem; do
    echo "Killing high Memory process: $cmd (PID: $pid, MEM: $mem)"
    kill $pid
done
EOF

chmod +x ~/process-killer.sh
```

**VORSICHT:** Nutze dieses Script mit Bedacht!

---

## Prüfungsvorbereitung Linux Essentials

### Typische Prüfungsfragen zu diesem Thema:

**Spezielle Berechtigungen:**
1. Was bedeutet das `t` in `drwxrwxrwt`? - Sticky Bit
2. Welche Oktal-Notation für Sticky Bit? - 1
3. Wofür steht SUID? - Set User ID
4. Beispiel für SUID? - `/usr/bin/passwd`
5. Was macht SGID auf Verzeichnissen? - Vererbt Gruppe

**Prozesse:**
1. Befehl für alle Prozesse? - `ps aux`
2. PID 1 ist immer? - Init-System (systemd)
3. Unterschied `kill` vs `killall`? - PID vs Name
4. Signal 9 bedeutet? - SIGKILL (sofort töten)
5. Signal 15 bedeutet? - SIGTERM (sanft beenden)

**Systemdienste:**
1. Dienst starten? - `systemctl start`
2. Autostart aktivieren? - `systemctl enable`
3. Unterschied `start` vs `enable`? - Jetzt vs Boot
4. Dienst-Status prüfen? - `systemctl status`

**Cron:**
1. Cronjob bearbeiten? - `crontab -e`
2. Was bedeutet `*/5 * * * *`? - Alle 5 Minuten
3. Was bedeutet `0 3 * * *`? - Täglich 3 Uhr
4. Wann läuft `/etc/cron.daily/`? - Täglich

---

## Hilfreiche Ressourcen

**Dokumentation:**
- `man systemctl` = systemd-Dokumentation
- `man crontab` = Cron-Dokumentation
- `man ps` = Prozess-Dokumentation
- `man chmod` = Berechtigungen

