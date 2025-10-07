# Übung: Archivierung & Paketverwaltung in Linux
## Praktische Übungen für Ubuntu

---

## Vorbereitung

Öffne ein Terminal in Ubuntu:
- **Tastenkombination:** `Ctrl + Alt + T`
- Oder über das Anwendungsmenü: "Terminal" suchen
- Verwende optional die WSL oder Multipass

---

## Teil 1: Archivierung mit tar (30 Minuten)

### Aufgabe 1.1: Arbeitsverzeichnis erstellen

Erstelle ein Übungsverzeichnis und wechsle hinein:

```bash
mkdir ~/archiv-uebung
cd ~/archiv-uebung
```

**Erklärung:**
- `mkdir` = Make Directory (Verzeichnis erstellen)
- `~` = Dein Home-Verzeichnis
- `cd` = Change Directory (Verzeichnis wechseln)

---

### Aufgabe 1.2: Testdateien erstellen

Erstelle eine Verzeichnisstruktur mit Testdateien:

```bash
mkdir -p projekt/{dokumente,bilder,code}
```

**Erklärung:**
- `-p` = Erstellt auch übergeordnete Verzeichnisse und keine Fehlermeldung, wenn Verzeichnis existiert
- `{dokumente,bilder,code}` = Erstellt drei Unterverzeichnisse auf einmal

Jetzt Dateien erstellen:

```bash
echo "Dies ist eine README-Datei" > projekt/dokumente/readme.txt
echo "Projektbeschreibung hier" > projekt/dokumente/beschreibung.txt
echo "print('Hallo Welt')" > projekt/code/main.py
echo "def test(): pass" > projekt/code/test.py
touch projekt/bilder/logo.png
touch projekt/bilder/banner.jpg
```

**Erklärung:**
- `echo "text" > datei` = Schreibt Text in eine Datei
- `touch datei` = Erstellt eine leere Datei

Überprüfe die Struktur:

```bash
tree projekt/
# Falls tree nicht installiert ist:
ls -R projekt/
```

**Erklärung:**
- `tree` = Zeigt Verzeichnisstruktur als Baum
- `ls -R` = Listet Dateien rekursiv (alle Unterverzeichnisse)

---

### Aufgabe 1.3: Einfaches tar-Archiv erstellen

Erstelle ein unkomprimiertes Archiv:

```bash
tar -cvf projekt.tar projekt/
```

**Erklärung der Optionen:**
- `-c` = **c**reate (Archiv erstellen)
- `-v` = **v**erbose (zeigt Details während der Erstellung)
- `-f` = **f**ile (nächster Parameter ist der Dateiname)

**Was passiert:**
Alle Dateien aus `projekt/` werden in `projekt.tar` gebündelt.

Überprüfe die erstellte Datei:

```bash
ls -lh projekt.tar
```

**Erklärung:**
- `ls -lh` = Liste mit Details, `-h` zeigt Größe in lesbarem Format (KB, MB)

---

### Aufgabe 1.4: Archivinhalt anzeigen

Zeige den Inhalt **ohne** Entpacken:

```bash
tar -tf projekt.tar
```

**Erklärung:**
- `-t` = **t**able/list (Inhalt auflisten)
- `-f` = **f**ile (Archivname folgt)

Mit detaillierten Informationen:

```bash
tar -tvf projekt.tar
```

**Erklärung:**
- `-v` = **v**erbose (zeigt Berechtigungen, Größe, Datum)

---

### Aufgabe 1.5: Komprimiertes Archiv mit gzip erstellen

Erstelle ein komprimiertes Archiv:

```bash
tar -czf projekt.tar.gz projekt/
```

**Erklärung der Optionen:**
- `-c` = **c**reate (erstellen)
- `-z` = Mit g**z**ip komprimieren
- `-f` = **f**ile (Dateiname)

Alternative Schreibweise (gleicher Befehl):

```bash
tar -czvf projekt.tar.gz projekt/
```

**Hinzugefügt:** `-v` für detaillierte Ausgabe

Vergleiche die Dateigröße:

```bash
ls -lh projekt.tar projekt.tar.gz
```

Beobachte den Unterschied in der Dateigröße zwischen unkomprimiert und komprimiert.

---

### Aufgabe 1.6: Komprimiertes Archiv entpacken

Erstelle ein Verzeichnis für die Wiederherstellung:

```bash
mkdir wiederherstellung
cd wiederherstellung
```

Entpacke das Archiv:

```bash
tar -xzf ../projekt.tar.gz
```

**Erklärung:**
- `-x` = e**x**tract (entpacken)
- `-z` = g**z**ip-dekomprimieren
- `-f` = **f**ile (Archivname)
- `../` = Ein Verzeichnis höher

**Moderne Variante** (tar erkennt Kompression automatisch):

```bash
tar -xf ../projekt.tar.gz
```

Überprüfe das Ergebnis:

```bash
ls -R projekt/
```

Gehe zurück ins Hauptverzeichnis:

```bash
cd ..
```

---

### Aufgabe 1.7: Archiv mit Ausschluss erstellen

Erstelle ein Archiv, aber **ohne** bestimmte Dateien:

```bash
tar -czf projekt-ohne-bilder.tar.gz --exclude='*.png' --exclude='*.jpg' projekt/
```

**Erklärung:**
- `--exclude='*.png'` = Schließt alle .png-Dateien aus
- `*` = Platzhalter für beliebige Zeichen

Überprüfe den Inhalt:

```bash
tar -tzf projekt-ohne-bilder.tar.gz
```

Sieh dir an, dass die Bilder-Dateien im Archiv fehlen.

---

### Aufgabe 1.8: Archiv mit Datum im Namen

Erstelle ein Backup mit aktuellem Datum:

```bash
tar -czf projekt-backup-$(date +%Y%m%d).tar.gz projekt/
```

**Erklärung:**
- `$(date +%Y%m%d)` = Fügt aktuelles Datum ein
- `%Y` = Jahr (4-stellig)
- `%m` = Monat (2-stellig)
- `%d` = Tag (2-stellig)

**Beispiel:** `projekt-backup-20250107.tar.gz`

Liste die erstellten Archive auf:

```bash
ls -lh *.tar.gz
```

---

## Teil 2: Kompression verstehen (20 Minuten)

### Aufgabe 2.1: Testdatei erstellen

Erstelle eine größere Testdatei:

```bash
dd if=/dev/zero of=testdatei.txt bs=1M count=10
```

**Erklärung:**
- `dd` = Daten kopieren
- `if=/dev/zero` = Input: Nullen
- `of=testdatei.txt` = Output: Datei
- `bs=1M` = Block Size: 1 Megabyte
- `count=10` = 10 Blöcke = 10 MB

Überprüfe die Größe:

```bash
ls -lh testdatei.txt
```

---

### Aufgabe 2.2: Mit gzip komprimieren

Komprimiere die Datei:

```bash
gzip -k testdatei.txt
```

**Erklärung:**
- `gzip` = GNU zip
- `-k` = **k**eep (Original behalten)
- **Ohne** `-k` würde das Original gelöscht!

**Ergebnis:** `testdatei.txt.gz`

Vergleiche die Größe:

```bash
ls -lh testdatei.txt testdatei.txt.gz
```

---

### Aufgabe 2.3: Mit bzip2 komprimieren

Komprimiere mit bzip2:

```bash
bzip2 -k testdatei.txt
```

**Erklärung:**
- `bzip2` = Bessere Kompression als gzip
- `-k` = Original behalten

**Ergebnis:** `testdatei.txt.bz2`

---

### Aufgabe 2.4: Mit xz komprimieren

Komprimiere mit xz:

```bash
xz -k testdatei.txt
```

**Erklärung:**
- `xz` = Beste Kompression
- `-k` = Original behalten

**Ergebnis:** `testdatei.txt.xz`

---

### Aufgabe 2.5: Kompression vergleichen

Vergleiche alle Versionen:

```bash
ls -lh testdatei.txt*
```

Beobachte die unterschiedlichen Dateigrößen und welches Format am besten komprimiert hat.

---

### Aufgabe 2.6: Dekomprimieren

Dekomprimiere die gzip-Datei:

```bash
gunzip testdatei.txt.gz
```

**Alternative:**

```bash
gzip -d testdatei.txt.gz
```

**Erklärung:**
- `gunzip` = gzip rückgängig machen
- `gzip -d` = **d**ecompress

**Hinweis:** Das .gz-Archiv wird gelöscht, Original wird wiederhergestellt.

---

## Teil 3: ZIP-Archive (15 Minuten)

### Aufgabe 3.1: ZIP-Archiv erstellen

Erstelle ein ZIP-Archiv:

```bash
zip -r projekt.zip projekt/
```

**Erklärung:**
- `zip` = ZIP-Format (Windows-kompatibel)
- `-r` = **r**ekursiv (mit Unterverzeichnissen)

**Hinweis:** Bei zip kommt erst der Archivname, dann die Quelle!

---

### Aufgabe 3.2: ZIP-Inhalt anzeigen

Zeige den Inhalt an:

```bash
unzip -l projekt.zip
```

**Erklärung:**
- `unzip` = ZIP entpacken
- `-l` = **l**ist (nur anzeigen, nicht entpacken)

---

### Aufgabe 3.3: ZIP entpacken

Erstelle ein Testverzeichnis:

```bash
mkdir zip-test
cd zip-test
```

Entpacke das Archiv:

```bash
unzip ../projekt.zip
```

**In spezifisches Verzeichnis entpacken:**

```bash
unzip ../projekt.zip -d /tmp/mein-ziel/
```

**Erklärung:**
- `-d` = **d**irectory (Zielverzeichnis)

Gehe zurück:

```bash
cd ..
```

---

## Teil 4: Paketverwaltung mit apt (40 Minuten)

### Aufgabe 4.1: System aktualisieren

**Schritt 1:** Paketlisten aktualisieren

```bash
sudo apt update
```

**Erklärung:**
- `sudo` = Befehl als Administrator ausführen
- `apt` = Advanced Package Tool
- `update` = Lädt neueste Paketlisten von Repositories

**Was passiert:** Ubuntu prüft, welche Updates verfügbar sind.

**Schritt 2:** Verfügbare Updates anzeigen

```bash
apt list --upgradable
```

**Erklärung:**
- `--upgradable` = Zeigt nur Pakete mit verfügbaren Updates

**Schritt 3:** System aktualisieren

```bash
sudo apt upgrade
```

**Erklärung:**
- `upgrade` = Installiert alle verfügbaren Updates
- Du wirst gefragt, ob du fortfahren möchtest (Y/n)

**Hinweis:** Bei der Übung kannst du mit `n` (nein) antworten, um Zeit zu sparen.

---

### Aufgabe 4.2: Nach Software suchen

Suche nach einem Texteditor:

```bash
apt search text editor
```

**Erklärung:**
- `search` = Durchsucht Paketnamen und Beschreibungen
- Keine sudo-Rechte nötig

**Gezielter suchen:**

```bash
apt search vim
```

---

### Aufgabe 4.3: Paketinformationen anzeigen

Zeige Details zu einem Paket:

```bash
apt show vim
```

**Erklärung:**
- `show` = Zeigt detaillierte Paketinformationen

**Was du siehst:**
- Paketbeschreibung
- Version
- Größe
- Abhängigkeiten
- Quelle (Repository)

---

### Aufgabe 4.4: Software installieren

Installiere einen Texteditor (falls nicht vorhanden):

```bash
sudo apt install vim
```

**Erklärung:**
- `install` = Paket installieren
- apt löst Abhängigkeiten automatisch auf

**Während der Installation siehst du:**
- Welche zusätzlichen Pakete installiert werden
- Wie viel Speicherplatz benötigt wird
- Bestätigung (Y/n)

Überprüfe die Installation:

```bash
vim --version
```

**oder:**

```bash
which vim
```

**Erklärung:**
- `which` = Zeigt den Pfad zur ausführbaren Datei

---

### Aufgabe 4.5: Mehrere Pakete installieren

Installiere mehrere Tools auf einmal:

```bash
sudo apt install tree htop curl
```

**Erklärung:**
- `tree` = Zeigt Verzeichnisstruktur als Baum
- `htop` = Interaktiver Prozess-Monitor
- `curl` = Tool zum Herunterladen von Dateien

**Hinweis:** Paketnamen durch Leerzeichen trennen.

---

### Aufgabe 4.6: Installierte Pakete auflisten

Liste alle installierten Pakete:

```bash
apt list --installed
```

**Zu viele? Filtere sie:**

```bash
apt list --installed | grep vim
```

**Erklärung:**
- `|` = Pipe (gibt Ausgabe an nächsten Befehl weiter)
- `grep vim` = Filtert nach "vim"

**Anzahl installierter Pakete zählen:**

```bash
apt list --installed | wc -l
```

**Erklärung:**
- `wc -l` = **w**ord **c**ount mit `-l` für **l**ines (Zeilen zählen)

---

### Aufgabe 4.7: Paket deinstallieren

Entferne ein Paket:

```bash
sudo apt remove htop
```

**Erklärung:**
- `remove` = Deinstalliert Programm
- Konfigurationsdateien bleiben erhalten

**Vollständig entfernen (mit Konfiguration):**

```bash
sudo apt purge htop
```

**Erklärung:**
- `purge` = Entfernt Programm UND Konfigurationsdateien

---

### Aufgabe 4.8: Nicht mehr benötigte Pakete entfernen

Entferne automatisch installierte, nicht mehr benötigte Pakete:

```bash
sudo apt autoremove
```

**Erklärung:**
- `autoremove` = Entfernt Abhängigkeiten, die nicht mehr gebraucht werden

**Was wird entfernt:**
- Pakete, die als Abhängigkeit installiert wurden
- Die nicht mehr von anderen Paketen benötigt werden

---

### Aufgabe 4.9: Cache bereinigen

Lösche heruntergeladene Paketdateien:

```bash
sudo apt autoclean
```

**Erklärung:**
- `autoclean` = Löscht veraltete .deb-Dateien aus dem Cache

**Gesamten Cache leeren:**

```bash
sudo apt clean
```

**Unterschied:**
- `autoclean` = Nur veraltete Pakete
- `clean` = Alle gecachten Pakete

**Wie viel Speicher wurde freigegeben?**

```bash
du -sh /var/cache/apt/archives/
```

**Erklärung:**
- `du` = **d**isk **u**sage (Speichernutzung)
- `-s` = **s**ummary (Gesamtsumme)
- `-h` = **h**uman-readable (lesbar: KB, MB, GB)

---

## Teil 5: Low-Level Paketmanager - dpkg (25 Minuten)

### Aufgabe 5.1: Was ist dpkg?

**dpkg** ist der Low-Level-Paketmanager für Debian/Ubuntu.

**Unterschied zu apt:**
- `apt` = High-Level, löst Abhängigkeiten automatisch, nutzt Repositories
- `dpkg` = Low-Level, arbeitet mit lokalen .deb-Dateien

---

### Aufgabe 5.2: Installierte Pakete mit dpkg auflisten

Liste alle installierten Pakete:

```bash
dpkg -l
```

**Erklärung:**
- `-l` = **l**ist (auflisten)

**Filtere nach bestimmtem Paket:**

```bash
dpkg -l | grep vim
```

---

### Aufgabe 5.3: Paketinformationen anzeigen

Zeige Informationen zu einem installierten Paket:

```bash
dpkg -s vim
```

**Erklärung:**
- `-s` = **s**tatus (Paketinformationen)

**Was du siehst:**
- Paketname
- Version
- Status (installiert oder nicht)
- Beschreibung

---

### Aufgabe 5.4: Paketinhalt anzeigen

Zeige alle Dateien eines Pakets:

```bash
dpkg -L vim
```

**Erklärung:**
- `-L` = **L**ist files (Dateien auflisten)

**Was du siehst:**
- Alle Dateien, die das Paket installiert hat
- Pfade zu Programmdateien, Dokumentation, etc.

---

### Aufgabe 5.5: Welches Paket hat eine Datei installiert?

Finde heraus, welches Paket eine bestimmte Datei installiert hat:

```bash
dpkg -S /usr/bin/vim
```

**Erklärung:**
- `-S` = **S**earch (suchen)
- Gibt Paketname zurück

**Praktisches Beispiel:**

```bash
which python3
dpkg -S $(which python3)
```

---

### Aufgabe 5.6: .deb-Datei herunterladen (ohne Installation)

Lade eine .deb-Datei herunter:

```bash
cd ~/archiv-uebung
apt download tree
```

**Erklärung:**
- `apt download` = Lädt .deb-Datei herunter, installiert aber nicht

**Ergebnis:** Eine Datei wie `tree_X.X.X_amd64.deb`

Liste die Datei auf:

```bash
ls -lh *.deb
```

---

### Aufgabe 5.7: .deb-Dateiinhalt anzeigen (ohne Installation)

Zeige den Inhalt einer .deb-Datei:

```bash
dpkg -c tree*.deb
```

**Erklärung:**
- `-c` = **c**ontents (Inhalt anzeigen)
- `*` = Platzhalter für Versionsnummer

---

### Aufgabe 5.8: .deb-Datei mit dpkg installieren

Installiere die .deb-Datei manuell:

```bash
sudo dpkg -i tree*.deb
```

**Erklärung:**
- `-i` = **i**nstall (installieren)

**Mögliches Problem:** Abhängigkeiten fehlen!

**Lösung - Abhängigkeiten nachinstallieren:**

```bash
sudo apt --fix-broken install
```

**oder kürzer:**

```bash
sudo apt -f install
```

**Erklärung:**
- `-f` = **f**ix (reparieren)
- Installiert fehlende Abhängigkeiten nach

---

### Aufgabe 5.9: Paket mit dpkg entfernen

Entferne das Paket:

```bash
sudo dpkg -r tree
```

**Erklärung:**
- `-r` = **r**emove (entfernen)
- Konfigurationsdateien bleiben erhalten

**Vollständig entfernen:**

```bash
sudo dpkg -P tree
```

**Erklärung:**
- `-P` = **P**urge (bereinigen)
- Entfernt Programm UND Konfiguration

---

## Teil 6: Praktisches Szenario - Website Backup (30 Minuten)

### Szenario

Du betreust eine Website und musst ein vollständiges Backup erstellen, das du später wiederherstellen kannst.

---

### Aufgabe 6.1: Website-Struktur simulieren

Erstelle eine Beispiel-Website-Struktur:

```bash
cd ~/archiv-uebung
mkdir -p website/{html,config,logs,uploads}
```

Erstelle Beispieldateien:

```bash
# HTML-Dateien
echo "<!DOCTYPE html><html><body><h1>Willkommen</h1></body></html>" > website/html/index.html
echo "<html><body><h1>Über uns</h1></body></html>" > website/html/about.html

# Konfiguration
echo "ServerName localhost" > website/config/server.conf
echo "Port 8080" > website/config/port.conf

# Uploads (simulierte hochgeladene Dateien)
touch website/uploads/bild1.jpg
touch website/uploads/dokument.pdf

# Logs (sollten NICHT gesichert werden)
echo "2025-01-07 10:00:00 - Server gestartet" > website/logs/access.log
echo "2025-01-07 10:01:00 - Fehler 404" > website/logs/error.log
```

Überprüfe die Struktur:

```bash
tree website/
```

---

### Aufgabe 6.2: Backup mit Ausschluss erstellen

Erstelle ein Backup **ohne** die Log-Dateien:

```bash
tar -czf website-backup-$(date +%Y%m%d-%H%M).tar.gz \
  --exclude='logs' \
  website/
```

**Erklärung:**
- `$(date +%Y%m%d-%H%M)` = Datum und Uhrzeit im Format: 20250107-1530
- `--exclude='logs'` = Schließt das logs-Verzeichnis aus
- `\` = Zeilenumbruch (Befehl geht in nächster Zeile weiter)

---

### Aufgabe 6.3: Backup überprüfen

Überprüfe den Backup-Inhalt:

```bash
tar -tzf website-backup-*.tar.gz
```

Prüfe:
- Sind alle wichtigen Dateien enthalten?
- Fehlt das logs-Verzeichnis?

**Detaillierte Ansicht:**

```bash
tar -tzvf website-backup-*.tar.gz
```

---

### Aufgabe 6.4: Wiederherstellung simulieren

Simuliere einen Datenverlust:

```bash
# VORSICHT: Löscht das gesamte Verzeichnis!
rm -rf website/
```

**Erklärung:**
- `rm` = remove (löschen)
- `-r` = **r**ecursive (mit Unterverzeichnissen)
- `-f` = **f**orce (keine Rückfragen)

Überprüfe die Löschung:

```bash
ls website/
# Fehler: Verzeichnis existiert nicht mehr
```

---

### Aufgabe 6.5: Backup wiederherstellen

Stelle das Backup wieder her:

```bash
tar -xzf website-backup-*.tar.gz
```

**Erklärung:**
- Entpackt das Archiv im aktuellen Verzeichnis
- Die Struktur wird wiederhergestellt

Überprüfe die Wiederherstellung:

```bash
tree website/
```

Beobachte:
- Alle wichtigen Dateien sind zurück
- Das logs-Verzeichnis fehlt (wie gewünscht)

---

### Aufgabe 6.6: Mehrere Backups verwalten

Erstelle mehrere Backups zu verschiedenen Zeiten:

```bash
# Erstes Backup
tar -czf website-backup-$(date +%Y%m%d-%H%M).tar.gz --exclude='logs' website/

# Warte 1 Minute oder ändere etwas...
echo "Neue Seite" > website/html/news.html

# Zweites Backup
tar -czf website-backup-$(date +%Y%m%d-%H%M).tar.gz --exclude='logs' website/
```

Liste alle Backups auf:

```bash
ls -lht website-backup-*.tar.gz
```

**Erklärung:**
- `-t` = Sortiert nach Zeit (neueste zuerst)

---

## Teil 7: Fortgeschrittene apt-Befehle (15 Minuten)

### Aufgabe 7.1: Simulation (ohne Installation)

Simuliere eine Installation:

```bash
apt install -s nginx
```

**Erklärung:**
- `-s` = **s**imulate (simulieren)
- Zeigt, was passieren würde, ohne es zu installieren

Nützlich um zu sehen:
- Welche Abhängigkeiten installiert würden
- Wie viel Speicher benötigt wird

---

### Aufgabe 7.2: Abhängigkeiten anzeigen

Zeige Abhängigkeiten eines Pakets:

```bash
apt depends vim
```

**Erklärung:**
- `depends` = Zeigt, was das Paket benötigt

**Umgekehrt - Was braucht dieses Paket:**

```bash
apt rdepends vim
```

**Erklärung:**
- `rdepends` = **r**everse depends (umgekehrte Abhängigkeiten)
- Zeigt, welche Pakete VIM benötigen

---

### Aufgabe 7.3: Paketdatei lokalisieren

Finde heraus, woher ein Paket kommt:

```bash
apt policy vim
```

**Erklärung:**
- `policy` = Zeigt Repository-Informationen
- Zeigt installierte und verfügbare Versionen

---

### Aufgabe 7.4: Nach Dateien in Paketen suchen

Installiere erst das Suchtool:

```bash
sudo apt install apt-file
sudo apt-file update
```

Suche, welches Paket eine bestimmte Datei bereitstellt:

```bash
apt-file search /usr/bin/python3
```

**Erklärung:**
- `apt-file` = Durchsucht Paketinhalte
- Findet Pakete, die eine bestimmte Datei installieren würden

---

## Vertiefung: Übersicht aller Paketmanager (Theorie)

In dieser Übung hast du hauptsächlich mit **apt** und **dpkg** gearbeitet, da du Ubuntu verwendest. In der Linux-Welt gibt es jedoch verschiedene Paketmanager, je nach Distribution.

### High-Level vs. Low-Level Paketmanager

**High-Level Paketmanager:**
- Lösen Abhängigkeiten automatisch
- Greifen auf Repositories (Online-Paketquellen) zu
- Verwalten Updates zentral
- Beispiele: apt, dnf, yum, zypper, pacman

**Low-Level Paketmanager:**
- Arbeiten mit lokalen Paketdateien
- Lösen KEINE Abhängigkeiten automatisch
- Basis für High-Level-Manager
- Beispiele: dpkg, rpm

---

### apt (Advanced Package Tool)

**Verwendet in:** Debian, Ubuntu, Linux Mint, Kali Linux, Pop!_OS

**Paketformat:** `.deb`

**Wichtigste Befehle:**
```bash
sudo apt update              # Paketlisten aktualisieren
sudo apt upgrade             # System aktualisieren
sudo apt install paket       # Paket installieren
sudo apt remove paket        # Paket entfernen
apt search suchbegriff       # Paket suchen
apt show paket               # Paketinfo anzeigen
```

**Eigenschaften:**
- Sehr benutzerfreundlich
- Farbige, übersichtliche Ausgabe
- Automatische Fortschrittsbalken
- Kombiniert Funktionen von apt-get und apt-cache

**Repository-Konfiguration:**
- Hauptdatei: `/etc/apt/sources.list`
- Zusätzliche: `/etc/apt/sources.list.d/`

---

### dpkg (Debian Package Manager)

**Verwendet in:** Debian, Ubuntu, Linux Mint (als Basis für apt)

**Paketformat:** `.deb`

**Wichtigste Befehle:**
```bash
sudo dpkg -i paket.deb       # .deb-Datei installieren
sudo dpkg -r paket           # Paket entfernen
dpkg -l                      # Installierte Pakete auflisten
dpkg -L paket                # Paketinhalt anzeigen
dpkg -S /pfad/datei          # Welches Paket hat Datei installiert?
```

**Eigenschaften:**
- Basis-Paketmanager von Debian/Ubuntu
- Arbeitet nur mit lokalen .deb-Dateien
- Löst keine Abhängigkeiten automatisch
- apt baut auf dpkg auf

**Wann verwenden:**
- Bei manuell heruntergeladenen .deb-Dateien
- Zur Paket-Inspektion
- In Skripten für detaillierte Paket-Operationen

---

### dnf (Dandified YUM)

**Verwendet in:** Fedora (ab 22), RHEL 8+, CentOS 8+, Rocky Linux, AlmaLinux

**Paketformat:** `.rpm`

**Wichtigste Befehle:**
```bash
sudo dnf check-update        # Nach Updates suchen
sudo dnf upgrade             # System aktualisieren
sudo dnf install paket       # Paket installieren
sudo dnf remove paket        # Paket entfernen
dnf search suchbegriff       # Paket suchen
dnf info paket               # Paketinfo anzeigen
```

**Eigenschaften:**
- Nachfolger von yum (moderner und schneller)
- Bessere Abhängigkeitsauflösung als yum
- Unterstützt Plugin-System
- Gruppenverwaltung von Paketen

**Repository-Konfiguration:**
- Verzeichnis: `/etc/yum.repos.d/`

---

### yum (Yellowdog Updater Modified)

**Verwendet in:** RHEL 7 und älter, CentOS 7 und älter, ältere Fedora-Versionen

**Paketformat:** `.rpm`

**Wichtigste Befehle:**
```bash
sudo yum update              # System aktualisieren
sudo yum install paket       # Paket installieren
sudo yum remove paket        # Paket entfernen
yum search suchbegriff       # Paket suchen
```

**Eigenschaften:**
- Vorgänger von dnf
- Langsamer als dnf
- Viele ältere Systeme nutzen es noch
- API-kompatibel mit dnf

**Status heute:**
- Auf neueren Systemen ist `yum` oft nur ein Alias für `dnf`
- Wichtig für Linux Essentials, da noch verbreitet

---

### rpm (Red Hat Package Manager)

**Verwendet in:** RHEL, Fedora, CentOS, openSUSE (als Basis für dnf/yum/zypper)

**Paketformat:** `.rpm`

**Wichtigste Befehle:**
```bash
sudo rpm -i paket.rpm        # .rpm-Datei installieren
sudo rpm -e paket            # Paket entfernen
rpm -qa                      # Alle installierten Pakete
rpm -qi paket                # Paketinfo anzeigen
rpm -ql paket                # Paketinhalt auflisten
```

**Eigenschaften:**
- Basis-Paketmanager für Red Hat-basierte Systeme
- Arbeitet nur mit lokalen .rpm-Dateien
- Löst keine Abhängigkeiten automatisch
- dnf und yum bauen auf rpm auf

**Wann verwenden:**
- Bei manuell heruntergeladenen .rpm-Dateien
- Zur Paket-Inspektion
- Wenn kein Netzwerkzugriff verfügbar ist

---

### zypper

**Verwendet in:** openSUSE, SUSE Linux Enterprise

**Paketformat:** `.rpm`

**Wichtigste Befehle:**
```bash
sudo zypper refresh          # Repositories aktualisieren
sudo zypper update           # System aktualisieren
sudo zypper install paket    # Paket installieren
sudo zypper remove paket     # Paket entfernen
zypper search suchbegriff    # Paket suchen
```

**Eigenschaften:**
- Sehr schnell und effizient
- Hervorragende Abhängigkeitsauflösung
- Unterstützt Rollback von Installationen
- Integration mit SUSE-spezifischen Tools

---

### pacman

**Verwendet in:** Arch Linux, Manjaro, EndeavourOS

**Paketformat:** `.pkg.tar.zst`

**Wichtigste Befehle:**
```bash
sudo pacman -Syu             # System aktualisieren
sudo pacman -S paket         # Paket installieren
sudo pacman -R paket         # Paket entfernen
pacman -Ss suchbegriff       # Paket suchen
pacman -Si paket             # Paketinfo anzeigen
```

**Eigenschaften:**
- Sehr schnell und minimalistisch
- Rolling Release Modell (immer neueste Software)
- AUR (Arch User Repository) für Community-Pakete
- Kompakte, effiziente Syntax

---

### snap

**Verwendet in:** Distributionsunabhängig (Ubuntu, Fedora, etc.)

**Paketformat:** Snap-Pakete (Container)

**Wichtigste Befehle:**
```bash
sudo snap install paket      # Paket installieren
sudo snap remove paket       # Paket entfernen
snap find suchbegriff        # Paket suchen
snap list                    # Installierte Snaps
```

**Eigenschaften:**
- Distributionsunabhängig
- Automatische Updates
- Sandboxed (isoliert vom System)
- Größere Paketgröße (bringt alle Abhängigkeiten mit)

**Vorteile:**
- Eine Installation funktioniert auf allen Distributionen
- Immer neueste Software-Version
- Erhöhte Sicherheit durch Isolation

**Nachteile:**
- Größere Pakete
- Langsamerer Start
- Mehr Speicherverbrauch

---

### flatpak

**Verwendet in:** Distributionsunabhängig (Fedora, Ubuntu, etc.)

**Paketformat:** Flatpak-Pakete (Container)

**Wichtigste Befehle:**
```bash
flatpak install paket        # Paket installieren
flatpak uninstall paket      # Paket entfernen
flatpak search suchbegriff   # Paket suchen
flatpak list                 # Installierte Flatpaks
```

**Eigenschaften:**
- Ähnlich wie snap
- Fokus auf Desktop-Anwendungen
- Flathub als zentrale Repository
- Sandboxing für Sicherheit

---

### Befehlsvergleich: apt vs. dnf vs. pacman

| Aktion | apt (Debian/Ubuntu) | dnf (Fedora/RHEL) | pacman (Arch) |
|--------|---------------------|-------------------|---------------|
| Paketlisten aktualisieren | `sudo apt update` | `sudo dnf check-update` | `sudo pacman -Sy` |
| System aktualisieren | `sudo apt upgrade` | `sudo dnf upgrade` | `sudo pacman -Syu` |
| Paket installieren | `sudo apt install PKG` | `sudo dnf install PKG` | `sudo pacman -S PKG` |
| Paket entfernen | `sudo apt remove PKG` | `sudo dnf remove PKG` | `sudo pacman -R PKG` |
| Paket suchen | `apt search TERM` | `dnf search TERM` | `pacman -Ss TERM` |
| Paketinfo anzeigen | `apt show PKG` | `dnf info PKG` | `pacman -Si PKG` |
| Installierte Pakete | `apt list --installed` | `dnf list installed` | `pacman -Q` |
| Aufräumen | `sudo apt autoremove` | `sudo dnf autoremove` | `sudo pacman -Sc` |

---

### Welchen Paketmanager sollte ich lernen?

**Für Linux Essentials wichtig:**
1. **apt** (am weitesten verbreitet - Ubuntu, Debian, Mint)
2. **dnf** (Red Hat Enterprise, Fedora)
3. **yum** (ältere RHEL-Systeme)
4. **dpkg** (Grundlagen)
5. **rpm** (Grundlagen)

**In der Praxis:**
- **Ubuntu/Debian-Welt:** apt ist Standard
- **Enterprise/Server:** dnf/yum (Red Hat, CentOS)
- **Desktop:** Oft zusätzlich snap oder flatpak
- **Arch-Nutzer:** pacman

**Empfehlung:**
Konzentriere dich auf **apt** (hast du in dieser Übung getan) und verstehe die Grundkonzepte. Die Konzepte sind bei allen Paketmanagern ähnlich - nur die Befehle unterscheiden sich leicht.

---

## Zusammenfassung

### Was hast du gelernt?

**Archivierung:**
- tar-Archive erstellen und entpacken
- Kompression mit gzip, bzip2, xz
- ZIP-Archive für Windows-Kompatibilität
- Ausschluss von Dateien beim Archivieren
- Backups mit Zeitstempel

**Paketverwaltung:**
- System mit apt aktualisieren
- Software suchen, installieren und entfernen
- Paketinformationen anzeigen
- Abhängigkeiten verstehen
- Low-Level-Manager dpkg verwenden
- Lokale .deb-Dateien installieren

**Praktische Fähigkeiten:**
- Website-Backup erstellen
- Backups mit Ausschlüssen
- Wiederherstellung durchführen

### Wichtigste Befehle für Linux Essentials

**Archivierung:**
```bash
tar -czf archiv.tar.gz ordner/    # Archiv erstellen mit gzip
tar -xzf archiv.tar.gz            # Archiv entpacken
tar -tzf archiv.tar.gz            # Inhalt anzeigen
zip -r archiv.zip ordner/         # ZIP erstellen
unzip archiv.zip                  # ZIP entpacken
```

**Paketverwaltung mit apt:**
```bash
sudo apt update                   # Paketlisten aktualisieren
sudo apt upgrade                  # System aktualisieren
sudo apt install paket            # Paket installieren
sudo apt remove paket             # Paket entfernen
apt search begriff                # Paket suchen
apt show paket                    # Paketinfo
```

**Paketverwaltung mit dpkg:**
```bash
sudo dpkg -i paket.deb           # .deb installieren
dpkg -l                          # Installierte Pakete
dpkg -L paket                    # Paketinhalt
dpkg -S /pfad/datei              # Paket für Datei finden
```

---

## Weiterführende Übungen (Optional)

### Übung 1: Automatisches Backup-Script

Erstelle ein Bash-Script `backup.sh`:

```bash
#!/bin/bash
# Backup-Script für wichtige Verzeichnisse

BACKUP_DIR=~/backups
DATUM=$(date +%Y%m%d-%H%M)

# Backup-Verzeichnis erstellen
mkdir -p $BACKUP_DIR

# Backup erstellen
tar -czf $BACKUP_DIR/backup-$DATUM.tar.gz \
  --exclude='*.log' \
  --exclude='*.tmp' \
  ~/dokumente/ \
  ~/bilder/

echo "Backup erstellt: backup-$DATUM.tar.gz"
```

Mache es ausführbar und führe es aus:
```bash
chmod +x backup.sh
./backup.sh
```

---

### Übung 2: Paket-Liste für Neuinstallation

Erstelle eine Liste installierter Pakete:

```bash
dpkg --get-selections > meine-pakete.txt
```

Sieh dir die Liste an:

```bash
less meine-pakete.txt
```

Bei einer Neuinstallation kannst du diese wiederherstellen:

```bash
sudo dpkg --set-selections < meine-pakete.txt
sudo apt-get dselect-upgrade
```

---

## Prüfungsvorbereitung Linux Essentials

### Typische Prüfungsfragen zu diesem Thema:

**Archivierung:**
1. Welcher Befehl erstellt ein komprimiertes tar-Archiv? - `tar -czf`
2. Welche Option zeigt den Inhalt eines Archivs? - `-t`
3. Was ist der Unterschied zwischen .tar.gz und .tgz? - Keine, identisch
4. Welches Kompressionsformat hat die beste Kompression? - xz

**Paketverwaltung:**
1. Welcher Befehl aktualisiert die Paketlisten? - `apt update`
2. Was ist der Unterschied zwischen `remove` und `purge`? - purge löscht auch Konfiguration
3. Welches Paketformat verwendet Ubuntu? - .deb
4. Was ist der Unterschied zwischen apt und dpkg? - apt = High-Level, dpkg = Low-Level
5. Welcher Befehl zeigt Abhängigkeiten? - `apt depends` oder `apt show`

---

## Hilfreiche Ressourcen

**Dokumentation:**
- `man tar` = tar-Handbuch
- `man apt` = apt-Handbuch  
- `man dpkg` = dpkg-Handbuch

**Online:**
- Ubuntu Documentation: https://help.ubuntu.com
- Debian Wiki: https://wiki.debian.org
- GNU tar Manual: https://www.gnu.org/software/tar/manual/

---

**Ende der Übung - Viel Erfolg bei der Prüfung!**
