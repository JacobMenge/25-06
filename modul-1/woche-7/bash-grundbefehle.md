# Bash Grundbefehle - Referenztabelle

## Absolute Grundlagen

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `pwd` | **P**rint **W**orking **D**irectory - zeigt aktuelles Verzeichnis | `pwd` | Gibt z.B. `/home/username` aus |
| `cd` | **C**hange **D**irectory - wechselt Verzeichnis | `cd /home/user`<br>`cd ..` (eine Ebene hoch)<br>`cd ~` (Home-Verzeichnis) | Ohne Argument geht's zum Home-Verzeichnis |
| `ls` | **L**i**s**t - listet Dateien und Ordner auf | `ls`<br>`ls -l` (detailliert)<br>`ls -la` (mit versteckten Dateien) | `-l` zeigt Berechtigungen, Größe, Datum |
| `echo` | Gibt Text aus | `echo "Hallo Welt"`<br>`echo $HOME` | Sehr nützlich für Scripts und Variablen |
| `clear` | Löscht den Bildschirm | `clear` | Wie Strg+L, macht Terminal übersichtlich |
| `exit` | Beendet die Terminal-Sitzung | `exit` | Schließt das Terminal-Fenster |
| `man` | **Man**ual - zeigt Hilfeseiten an | `man ls` | Mit `q` verlassen, mit `/suchwort` suchen |
| `history` | Zeigt letzte Befehle an | `history` | Mit `!123` Befehl Nr. 123 wiederholen |

## Verzeichnisse und Navigation

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `mkdir` | **M**a**k**e **Dir**ectory - erstellt Verzeichnis | `mkdir neuer_ordner`<br>`mkdir -p pfad/zum/ordner` | `-p` erstellt auch übergeordnete Ordner |
| `rmdir` | **R**e**m**ove **Dir**ectory - löscht leeres Verzeichnis | `rmdir alter_ordner` | Funktioniert nur bei leeren Verzeichnissen |
| `tree` | Zeigt Verzeichnisstruktur als Baum | `tree`<br>`tree -L 2` | `-L 2` begrenzt auf 2 Ebenen (falls installiert) |

## Dateien erstellen, kopieren, verschieben

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `touch` | Erstellt leere Datei oder aktualisiert Zeitstempel | `touch datei.txt` | Wenn Datei existiert: nur Zeitstempel ändern |
| `cp` | **C**o**p**y - kopiert Dateien/Verzeichnisse | `cp quelle.txt ziel.txt`<br>`cp -r ordner1/ ordner2/` | `-r` für **r**ekursiv (ganze Verzeichnisse) |
| `mv` | **M**o**v**e - verschiebt/benennt um | `mv alt.txt neu.txt`<br>`mv datei.txt ordner/` | Kann gleichzeitig verschieben UND umbenennen |
| `rm` | **R**e**m**ove - löscht Dateien/Verzeichnisse | `rm datei.txt`<br>`rm -r ordner/`<br>`rm -rf ordner/` | `-r` rekursiv, `-f` force (ohne Nachfrage) |
| `ln` | Erstellt Links (Verknüpfungen) | `ln -s /pfad/zur/datei link_name` | `-s` für symbolische Links (wie Shortcuts) |

## Dateien finden und durchsuchen

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `find` | Sucht Dateien und Verzeichnisse | `find . -name "*.txt"`<br>`find /home -type f -size +1M` | `.` = hier, `-type f` = nur Dateien, `+1M` = größer 1MB |
| `locate` | Schnelle Dateisuche (falls installiert) | `locate dateiname` | Nutzt Datenbank, mit `updatedb` aktualisieren |
| `which` | Zeigt Pfad zu einem Befehl | `which python`<br>`which ls` | Zeigt wo sich das Programm befindet |
| `file` | Zeigt Dateityp an | `file datei.txt`<br>`file bild.jpg` | Erkennt Dateityp auch ohne Endung |

## Dateien anzeigen und lesen

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `cat` | Zeigt gesamten Dateiinhalt | `cat datei.txt` | **Cat**enate - für kleine Dateien |
| `less` | Zeigt Datei seitenweise (empfohlen!) | `less große_datei.txt` | Pfeiltasten/PgUp/PgDn navigieren, `q` beenden |
| `more` | Wie less, aber einfacher | `more datei.txt` | Nur vorwärts blättern möglich |
| `head` | Zeigt erste Zeilen | `head -10 datei.txt`<br>`head -n 5 datei.txt` | Standard: 10 Zeilen, `-n` für andere Anzahl |
| `tail` | Zeigt letzte Zeilen | `tail -10 datei.txt`<br>`tail -f log.txt` | `-f` **f**ollow für Live-Updates (Log-Dateien) |
| `grep` | Sucht Text in Dateien | `grep "suchwort" datei.txt`<br>`grep -i "Text" *.txt`<br>`grep -r "wort" ordner/` | `-i` ignoriert Groß/Klein, `-r` rekursiv |

## Einfache Textbearbeitung

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `nano` | Einfacher Texteditor (anfängerfreundlich) | `nano datei.txt` | Strg+X zum Speichern/Beenden |
| `vim` / `vi` | Mächtiger Texteditor | `vim datei.txt` | `:q` beenden, `:wq` speichern+beenden |
| `sort` | Sortiert Zeilen | `sort datei.txt`<br>`sort -n zahlen.txt` | `-n` für numerische Sortierung |
| `uniq` | Entfernt doppelte Zeilen | `sort datei.txt | uniq` | Funktioniert nur bei bereits sortierten Zeilen |
| `wc` | **W**ord **C**ount - zählt Zeilen/Wörter/Zeichen | `wc -l datei.txt` (Zeilen)<br>`wc -w datei.txt` (Wörter) | Ohne Option: Zeilen, Wörter, Zeichen |

## Berechtigungen und Besitzer (Sehr wichtig!)

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `sudo` | **S**uper **U**ser **Do** - führt als Administrator aus | `sudo apt update`<br>`sudo rm system_datei` | Fragt nach Passwort, sehr mächtig - Vorsicht! |
| `chmod` | **Ch**ange **Mod**e - ändert Berechtigungen | `chmod +x script.sh`<br>`chmod -w datei.txt`<br>`chmod u+rw,g+r,o-rwx datei.txt` | `+` hinzufügen, `-` entfernen, `=` exakt setzen |
| `chown` | **Ch**ange **Own**er - ändert Besitzer | `sudo chown user:gruppe datei.txt` | Braucht meist sudo-Rechte |
| `ls -l` | Zeigt detaillierte Berechtigungen | `ls -l datei.txt` | rwx rwx rwx = Read Write eXecute |

**Berechtigungen verstehen:**
- `r` = **R**ead (lesen) - Datei lesen/Verzeichnis auflisten
- `w` = **W**rite (schreiben) - Datei ändern/Verzeichnis bearbeiten  
- `x` = e**X**ecute (ausführen) - Datei ausführen/Verzeichnis betreten
- `u` = **U**ser (Besitzer), `g` = **G**roup (Gruppe), `o` = **O**thers (Andere), `a` = **A**ll (Alle)

**Häufige chmod Beispiele:**
- `chmod +x script.sh` - Script ausführbar machen
- `chmod -w datei.txt` - Schreibschutz setzen  
- `chmod u=rw,g=r,o=` - Besitzer: lesen+schreiben, Gruppe: nur lesen, Andere: nichts

## System-Informationen

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `whoami` | Zeigt aktuellen Benutzernamen | `whoami` | "Who am I?" - nützlich in Scripts |
| `date` | Zeigt/setzt Datum und Zeit | `date`<br>`date +"%Y-%m-%d %H:%M"` | `+` für eigenes Format |
| `uptime` | Zeigt Systemlaufzeit und Last | `uptime` | Wie lange läuft das System? |
| `df` | **D**isk **F**ree - zeigt Speicherplatz | `df -h` | `-h` für **h**uman readable (MB, GB) |
| `du` | **D**isk **U**sage - zeigt Verzeichnisgröße | `du -sh ordner/`<br>`du -sh *` | `-s` summary, `-h` human readable |
| `free` | Zeigt Arbeitsspeicher-Nutzung | `free -h` | RAM und Swap-Speicher Übersicht |

## Prozesse verwalten

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `ps` | **P**rocess **S**tatus - zeigt Prozesse | `ps aux`<br>`ps -ef` | `aux` = alle Prozesse aller User |
| `top` | Live-Ansicht der Prozesse | `top` | Drücken Sie `q` zum Beenden |
| `htop` | Interaktiver Prozessmanager (falls installiert) | `htop` | Schönere Alternative zu `top` |
| `kill` | Beendet Prozess über PID | `kill 1234`<br>`kill -9 1234` | `-9` für erzwungenes Beenden (SIGKILL) |
| `killall` | Beendet alle Prozesse eines Namens | `killall firefox` | Vorsicht - beendet ALLE Instanzen |
| `jobs` | Zeigt Hintergrund-Jobs | `jobs` | Nur Jobs der aktuellen Shell |
| `bg` | Setzt Job in Hintergrund | `bg %1` | `%1` = Job Nummer 1 |
| `fg` | Holt Job in Vordergrund | `fg %1` | Gegenteil von `bg` |

## Netzwerk (Grundlagen)

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `ping` | Testet Netzwerkverbindung | `ping google.com`<br>`ping -c 4 8.8.8.8` | `-c 4` = nur 4 Pakete senden |
| `wget` | Lädt Dateien herunter | `wget https://example.com/datei.zip` | Speichert Datei im aktuellen Verzeichnis |
| `curl` | Vielseitiges Datenübertragungstool | `curl -O https://example.com/datei.txt` | `-O` behält ursprünglichen Dateinamen |

## Archive und Komprimierung

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `tar` | **T**ape **Ar**chive - packt/entpackt Dateien | `tar -czf archiv.tar.gz ordner/`<br>`tar -xzf archiv.tar.gz` | **c**reate **z**ip **f**ile / e**x**tract **z**ip **f**ile |
| `zip` | Erstellt ZIP-Archive | `zip -r archiv.zip ordner/` | `-r` für rekursiv (ganze Verzeichnisse) |
| `unzip` | Entpackt ZIP-Archive | `unzip archiv.zip` | Einfacher als tar für ZIP-Dateien |

**TAR-Optionen merken:**
- `c` = **c**reate (erstellen)
- `x` = e**x**tract (entpacken) 
- `z` = g**z**ip (komprimieren)
- `f` = **f**ile (Dateiname folgt)
- `v` = **v**erbose (zeige Details)

## Umgebung und Variablen

| Befehl | Beschreibung | Beispiel | Erklärung |
|--------|--------------|----------|-----------|
| `env` | Zeigt alle Umgebungsvariablen | `env` | Liste aller Environment Variables |
| `export` | Setzt Umgebungsvariable | `export PATH=$PATH:/neuer/pfad` | Macht Variable für alle Programme verfügbar |
| `alias` | Erstellt Befehls-Abkürzungen | `alias ll='ls -la'`<br>`alias ..='cd ..'` | Eigene Kurzbefehle definieren |
| `source` | Führt Script in aktueller Shell aus | `source script.sh`<br>`. script.sh` | Punkt `.` ist Kurzform für `source` |
| `$?` | Exit-Status des letzten Befehls | `ls; echo $?` | 0 = Erfolg, alles andere = Fehler |

## Pipe und Umleitung (Sehr mächtig!)

| Symbol/Befehl | Beschreibung | Beispiel | Erklärung |
|---------------|--------------|----------|-----------|
| `\|` | **Pipe** - Ausgabe weiterleiten | `ls \| grep txt`<br>`cat datei.txt \| sort \| uniq` | Verbindet Befehle miteinander |
| `>` | Umleitung in Datei (überschreibt) | `ls > dateiliste.txt`<br>`echo "neu" > datei.txt` | **Achtung:** Löscht Dateiinhalt zuerst! |
| `>>` | Umleitung in Datei (anhängen) | `echo "mehr text" >> datei.txt` | Hängt am Ende an, löscht nicht |
| `<` | Eingabe aus Datei | `sort < datei.txt` | Datei wird als Eingabe verwendet |
| `2>` | Fehlerausgabe umleiten | `befehl 2> fehler.log` | Nur Fehlermeldungen in Datei |
| `&>` | Alles umleiten (Output + Fehler) | `befehl &> alles.log` | Normale und Fehlerausgabe |

## Kontrollzeichen (Tastenkombinationen)

| Kombination | Beschreibung | Wann verwenden |
|-------------|--------------|----------------|
| `Strg + C` | Beendet aktuellen Befehl | Programm hängt oder läuft zu lange |
| `Strg + Z` | Pausiert Befehl (Hintergrund) | Um Programm später mit `fg` fortzusetzen |
| `Strg + D` | Beendet Eingabe/Terminal | Wie `exit`, oder Ende der Eingabe |
| `Strg + L` | Löscht Bildschirm | Wie `clear` |
| `Strg + R` | Suche in Historie | Tippen Sie Teilbefehl für Suche |
| `Tab` | Auto-Vervollständigung | Spart VIEL Tipparbeit! |
| `↑/↓` | Durch Befehlshistorie blättern | Letzte Befehle wiederholen |

## Wildcards (Platzhalter)

| Symbol | Bedeutung | Beispiel | Was passiert |
|--------|-----------|----------|--------------|
| `*` | Beliebige Anzahl Zeichen | `ls *.txt` | Alle Dateien mit .txt Endung |
| `?` | Genau ein Zeichen | `ls datei?.txt` | datei1.txt, dateiA.txt, etc. |
| `[]` | Eines der Zeichen | `ls datei[123].txt` | datei1.txt, datei2.txt, datei3.txt |
| `{}` | Alternativen | `cp datei.{txt,bak}` | Kopiert datei.txt und datei.bak |
