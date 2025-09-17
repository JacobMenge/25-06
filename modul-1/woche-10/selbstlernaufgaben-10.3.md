# Linux Praxis Challenge: grep & vim
*Für Windows 11 mit WSL (Windows Subsystem for Linux)*

---

## Überblick der Challenge

In dieser Challenge lernst du zwei der mächtigsten Werkzeuge in Linux kennen: **grep** für die Textsuche und **vim** für die Textbearbeitung. Diese Tools sind auf jedem Linux-System verfügbar und werden täglich von Systemadministratoren und Entwicklern verwendet.

**Warum diese beiden Tools?**
- grep hilft dir, in großen Dateien und Logfiles schnell relevante Informationen zu finden
- vim ist ein universeller Editor, der auf jedem Server verfügbar ist
- Beide Tools ergänzen sich perfekt: grep zum Analysieren, vim zum Bearbeiten

**Aufbau der Challenge:**
1. Teil 1: grep - Textsuche und Filterung (Verpflichtend/Grundlagen)
2. Teil 2: vim - Textbearbeitung und Navigation (Verpflichtend/Grundlagen)
3. Teil 3: Kombination beider Tools in realistischen Szenarien (Freiwillig)

---

## Teil 1: grep - Mächtiger Text-Sucher

### Einführung in grep

Das Kommando `grep` steht für "Global Regular Expression Print" und ist eines der wichtigsten Werkzeuge für die Textanalyse in Linux. Du kannst damit in Dateien nach bestimmten Mustern suchen, Logdateien analysieren oder große Datenmengen filtern.

**Grundsyntax:**
```
grep [Optionen] "Suchmuster" datei(en)
```

### Die wichtigsten grep-Optionen

**Basis-Optionen:**
- `grep "text" datei.txt` - Sucht nach "text" in der Datei
- `grep -i "text" datei.txt` - Ignoriert Groß-/Kleinschreibung (case insensitive)
- `grep -n "text" datei.txt` - Zeigt Zeilennummern mit an
- `grep -v "text" datei.txt` - Invertiert die Suche (zeigt Zeilen OHNE "text")
- `grep -c "text" datei.txt` - Zählt nur die Anzahl der Treffer

**Erweiterte Optionen:**
- `grep -r "text" verzeichnis/` - Rekursive Suche in allen Dateien eines Verzeichnisses
- `grep -A 3 "text" datei.txt` - Zeigt 3 Zeilen NACH dem Treffer (After)
- `grep -B 3 "text" datei.txt` - Zeigt 3 Zeilen VOR dem Treffer (Before)  
- `grep -C 3 "text" datei.txt` - Zeigt 3 Zeilen Kontext (Context - davor und danach)

**Warum sind diese Optionen so wichtig?**
- `-i`: In der Praxis suchst du oft nach Wörtern, ohne dir über Groß-/Kleinschreibung Gedanken zu machen
- `-n`: Zeilennummern helfen beim späteren Bearbeiten der Datei mit vim
- `-v`: Perfekt um "alles außer X" zu finden (z.B. alle Zeilen ohne INFO-Meldungen)
- `-A`, `-B`, `-C`: Bei Fehlern brauchst du oft den Kontext, um zu verstehen, was passiert ist

**Praktische Anwendung:**
grep wird hauptsächlich verwendet für:
- Analyse von Logdateien (Fehlersuche)
- Durchsuchen von Konfigurationsdateien
- Filtern von Kommando-Ausgaben
- Code-Reviews und Debugging

### Reguläre Ausdrücke verstehen und verwenden

**Was sind reguläre Ausdrücke?**
Reguläre Ausdrücke (RegEx) sind Muster, die beschreiben, welche Zeichenketten du suchst. Stell dir vor, du suchst nicht nur nach dem exakten Wort "Fehler", sondern nach allem, was mit "Fehl" beginnt.

**Die wichtigsten Symbole:**

**Positionsmarker:**
- `^` = Zeilenanfang (Caret = "Dach")
- `$` = Zeilenende (Dollar)

```bash
# Beispiele:
grep "^ERROR" datei.txt    # Zeilen die mit ERROR beginnen
grep "txt$" datei.txt      # Zeilen die mit txt enden
grep "^$" datei.txt        # Leere Zeilen finden
```

**Platzhalter:**
- `.` = Ein beliebiges Zeichen (außer Zeilenumbruch)
- `*` = Null oder mehr Wiederholungen des vorherigen Zeichens
- `.*` = Beliebig viele beliebige Zeichen (sehr häufig verwendet!)

```bash
# Beispiele:
grep "t.xt" datei.txt      # Findet: text, test, txt, t9xt, etc.
grep "ab*c" datei.txt      # Findet: ac, abc, abbc, abbbc, etc.
grep "Fehler.*Code" datei.txt  # Findet: "Fehler beim Code", "Fehler 404 Code"
```

**Zeichenklassen:**
- `[abc]` = Eines der Zeichen a, b oder c
- `[a-z]` = Ein Kleinbuchstabe
- `[0-9]` = Eine Ziffer
- `[A-Z]` = Ein Großbuchstabe

```bash
# Beispiele:
grep "[0-9]" datei.txt     # Zeilen mit mindestens einer Ziffer
grep "^[A-Z]" datei.txt    # Zeilen die mit Großbuchstaben beginnen
grep "[aeiou]" datei.txt   # Zeilen mit Vokalen
```

**Erweiterte RegEx (mit -E Option):**
- `+` = Ein oder mehr Wiederholungen
- `?` = Null oder eine Wiederholung
- `{n}` = Genau n Wiederholungen
- `{n,m}` = Zwischen n und m Wiederholungen
- `|` = ODER (Alternative)

```bash
# Beispiele:
grep -E "[0-9]+" datei.txt        # Eine oder mehr Ziffern
grep -E "colou?r" datei.txt       # Findet: color oder colour
grep -E "[0-9]{4}" datei.txt      # Genau 4 Ziffern (z.B. Jahreszahlen)
grep -E "(fehler|error)" datei.txt # Findet: fehler oder error
```

**Praktische RegEx-Beispiele:**
```bash
# E-Mail-Adressen finden:
grep -E "[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}" kontakte.txt

# IP-Adressen finden:
grep -E "[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" datei.txt

# Datum im Format DD.MM.YYYY:
grep -E "[0-9]{2}\.[0-9]{2}\.[0-9]{4}" datei.txt

# Telefonnummern:
grep -E "[0-9]{4}-[0-9]{6}" kontakte.txt
```

**Wichtige Escape-Zeichen:**
Manche Zeichen haben in RegEx besondere Bedeutung. Um sie wörtlich zu suchen, musst du sie "escapen":

```bash
grep "\." datei.txt        # Sucht nach einem echten Punkt
grep "\$" datei.txt        # Sucht nach einem Dollar-Zeichen
grep "\[" datei.txt        # Sucht nach einer eckigen Klammer
```

---

### Aufgabe 1: grep Grundlagen

Erstelle zuerst eine Arbeitsumgebung und Testdateien:

```bash
cd ~
mkdir grep_vim_challenge
cd grep_vim_challenge
```

**Erstelle eine Logdatei zum Üben:**

```bash
cat > server.log << 'EOF'
2024-01-15 10:30:22 INFO: Server gestartet auf Port 8080
2024-01-15 10:30:25 INFO: Datenbankverbindung hergestellt
2024-01-15 10:32:10 WARNING: Langsame Antwortzeit auf /api/users
2024-01-15 10:35:45 ERROR: Verbindungsfehler zur Datenbank
2024-01-15 10:36:00 INFO: Datenbankverbindung wiederhergestellt  
2024-01-15 10:38:22 ERROR: 404 Fehler bei /api/products
2024-01-15 10:40:15 INFO: Backup-Prozess gestartet
2024-01-15 10:42:30 WARNING: Speicherplatz wird knapp (85% belegt)
2024-01-15 10:45:10 ERROR: Backup fehlgeschlagen
2024-01-15 10:46:00 INFO: Backup erfolgreich abgeschlossen
EOF
```

**Erstelle eine Konfigurationsdatei:**

```bash
cat > config.txt << 'EOF'
# Server Konfiguration
server_port=8080
database_host=localhost
database_port=5432
debug_mode=true
log_level=INFO
max_connections=100
timeout=30
backup_enabled=true
backup_time=02:00
admin_email=admin@beispiel.de
EOF
```

**Jetzt führe folgende grep-Befehle aus und beobachte die Ergebnisse:**

1. **Einfache Suchen:**
```bash
grep "ERROR" server.log
grep "INFO" server.log
grep "database" config.txt
```

2. **Optionen testen:**
```bash
grep -i "error" server.log      # Was passiert hier im Vergleich zum ersten Befehl?
grep -n "WARNING" server.log    # Warum sind die Zeilennummern nützlich?
grep -c "INFO" server.log       # Nur die Anzahl - wann ist das praktisch?
grep -v "INFO" server.log       # Zeigt alles AUSSER INFO - sehr mächtig!
```

3. **Kontext anzeigen - der Schlüssel zur Fehleranalyse:**
```bash
grep -A 2 "ERROR" server.log    # Zeigt was NACH dem Fehler passierte
grep -B 1 "WARNING" server.log  # Zeigt was VOR der Warnung war
grep -C 1 "Backup" server.log   # Zeigt den kompletten Kontext
```

**Warum ist Kontext so wichtig?**
In echten Logdateien siehst du oft erst durch den Kontext, was wirklich passiert ist. Ein ERROR allein sagt dir: "Etwas ist schief gelaufen". Mit Kontext siehst du: "Was passierte davor?" und "Wurde es behoben?"

**Fragen zur Aufgabe 1:**
1. Wie viele ERROR-Einträge gibt es in der server.log? (Verwende die passende grep-Option)
2. Was zeigt `grep -v "INFO" server.log` an und warum ist das in der Praxis nützlich?
3. Erkläre den Unterschied zwischen `grep "database" config.txt` und `grep -i "database" config.txt`

**Screenshot-Aufgabe 1:**
Mache einen Screenshot der Ausgabe von: `grep -n -C 1 "ERROR" server.log`

---

### Aufgabe 2: grep mit regulären Ausdrücken

Erweitere deine Testumgebung um weitere Dateien:

**Erstelle eine Kontaktdatei:**

```bash
cat > kontakte.txt << 'EOF'
Max Mustermann max.mustermann@firma.de 0123-456789
Anna Schmidt anna.schmidt@example.com 0987-654321
Peter Weber p.weber@test.org 0555-123456
Lisa Müller lisa.mueller@firma.de 0444-987654
Tom Brown tom.brown@company.com 0333-555777
Sarah Johnson sarah@beispiel.de 0222-111333
EOF
```

**Erstelle eine Datei mit strukturierten Daten:**

```bash
cat > bestellungen.txt << 'EOF'
Bestellnummer: ORD-2024-001
Kundennummer: KND-12345
Datum: 15.01.2024
Betrag: 299,99 EUR
Status: abgeschlossen

Bestellnummer: ORD-2024-002  
Kundennummer: KND-67890
Datum: 16.01.2024
Betrag: 1.450,00 EUR
Status: in Bearbeitung

Bestellnummer: ORD-2024-003
Kundennummer: KND-11111
Datum: 17.01.2024
Betrag: 75,50 EUR
Status: storniert
EOF
```

**Teste nun reguläre Ausdrücke mit grep:**

1. **Zeilenanfang und -ende - Struktur verstehen:**
```bash
grep "^Max" kontakte.txt        # Nur Zeilen die mit "Max" beginnen
grep "\.de" kontakte.txt       # Nur Zeilen mit ".de" (Backslash wichtig!)
grep "^Betrag:" bestellungen.txt # Nur Betrag-Zeilen finden
```

**Wichtiger Hinweis:** Der Punkt (.) hat in RegEx eine besondere Bedeutung (beliebiges Zeichen). Um einen echten Punkt zu suchen, musst du `\.` schreiben!

2. **Muster mit Platzhaltern verstehen:**
```bash
grep "0.*-.*" kontakte.txt      # Telefonnummern (beginnt mit 0, enthält Bindestriche)
grep "ORD-202.-..." bestellungen.txt # Bestellnummern 2024 (. = beliebiges Zeichen)
```

3. **Erweiterte Muster (benötigt -E Option):**
```bash
grep -E "[0-9]{4}" bestellungen.txt          # Genau 4 Ziffern (Jahreszahlen)
grep -E "\.de|\.com" kontakte.txt            # .de ODER .com Adressen
grep -E "Status: (abgeschlossen|storniert)" bestellungen.txt # Bestimmte Status
```

4. **Praktische RegEx-Übungen:**
```bash
# Alle E-Mail-Adressen finden:
grep -E "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}" kontakte.txt

# Alle Telefonnummern mit genau 4 Ziffern nach dem Bindestrich:
grep -E "[0-9]{4}-[0-9]{6}" kontakte.txt

# Alle Beträge über 1000 Euro (vereinfacht):
grep -E "1\.[0-9]{3}," bestellungen.txt
```

5. **Kombinierte Suchen mit Pipes:**
```bash
grep "firma" kontakte.txt | grep -v "Mustermann"  # Firma-E-Mails aber nicht Mustermann
grep "ORD" bestellungen.txt | grep -E "(001|003)" # Nur bestimmte Bestellnummern
```

**RegEx Debugging-Tipps:**
- Teste RegEx immer schrittweise: Beginne einfach und erweitere
- Verwende `grep -E` für erweiterte Funktionen
- Der Backslash `\` ist dein Freund für Sonderzeichen
- Bei Problemen: Erst ohne RegEx testen, dann erweitern

**Fragen zur Aufgabe 2:**
1. Was passiert, wenn du den Backslash vor dem Punkt weglässt? Vergleiche `grep "\.de" kontakte.txt` mit `grep ".de" kontakte.txt`
2. Wie findest du mit grep alle Zeilen, die NICHT mit einer Zahl beginnen?
3. Erkläre die Bedeutung von `^` und `$` in regulären Ausdrücken
4. Warum brauchst du `-E` für `{4}` aber nicht für `^` oder `$`?

**Screenshot-Aufgabe 2:**
Screenshot von: `grep -E "\.de|\.com" kontakte.txt` und `grep "^Betrag:" bestellungen.txt`

---

## Teil 2: vim - Der mächtige Text-Editor

### Einführung in vim

vim (Vi IMproved) ist einer der mächtigsten und am weitesten verbreiteten Texteditoren in der Linux-Welt. Obwohl er anfangs gewöhnungsbedürftig erscheint, wirst du nach dem Erlernen der Grundlagen extrem produktiv damit arbeiten können.

**Das Besondere an vim:** Er arbeitet mit verschiedenen "Modi", die unterschiedliche Funktionen haben.

### Die vim-Modi verstehen (Das Herzstück von vim!)

**Warum Modi?** Stell dir vor, du hättest zwei verschiedene Tastaturen: Eine zum Schreiben und eine für Befehle. Das ist die Grundidee von vim - verschiedene Modi für verschiedene Aufgaben.

**Normal-Modus (Standard):**
- Du startest IMMER in diesem Modus
- Hier führst du Befehle aus (navigieren, kopieren, löschen)
- Zurück gelangst du IMMER mit der ESC-Taste
- **Merkhilfe:** Wenn du unsicher bist, drücke ESC - du bist dann sicher im Normal-Modus

**Insert-Modus (Eingabe):**
- In diesem Modus schreibst du tatsächlich Text
- Verschiedene Wege hineinzugelangen: `i`, `a`, `o`
- Unten im Editor steht "-- INSERT --"
- **Wichtig:** Navigationstasten funktionieren hier anders!

**Command-Modus (Befehle):**
- Für vim-Befehle wie speichern, beenden, suchen
- Erreichst du durch Eingabe von `:` (erscheint unten)
- Befehle mit Enter bestätigen

**Visueller Modus (Auswahl):**
- Zum Markieren von Text
- Erreichst du mit `v` (zeichenweise) oder `V` (zeilenweise)
- Markierter Text wird hervorgehoben

### Modi-Wechsel verstehen (Kritisch für den Erfolg!)

```
Normal-Modus (Start)
    ↓ i,a,o
Insert-Modus ←→ ESC ←→ Normal-Modus
    ↓ :                  ↓ v,V
Command-Modus ←→ ESC   Visueller-Modus
```

**Häufige Anfängerfehler vermeiden:**
- **Problem:** Du drückst Tasten, aber es passiert nicht das, was du erwartest
- **Lösung:** Drücke ESC und versuche es erneut
- **Problem:** Du willst speichern, aber `:w` schreibt sich in den Text
- **Lösung:** Du bist im Insert-Modus - drücke ESC, dann `:w`

### Wichtige vim-Befehle

**vim starten und beenden:**
- `vim dateiname.txt` - Öffnet oder erstellt eine Datei
- `:q` - Beenden (nur wenn keine Änderungen)
- `:q!` - Beenden ohne speichern (Änderungen verwerfen)
- `:w` - Speichern
- `:wq` - Speichern und beenden (am häufigsten verwendet)

**Navigation im Normal-Modus:**
- `h` `j` `k` `l` - Links, runter, hoch, rechts (Alternative zu Pfeiltasten)
- `w` - Zum nächsten Wort springen
- `b` - Zum vorherigen Wort springen (back)
- `0` - Zum Zeilenanfang
- `$` - Zum Zeilenende
- `gg` - Zum Dateianfang
- `G` - Zum Dateiende
- `10G` - Zu Zeile 10 springen

**Warum hjkl statt Pfeiltasten?**
- Deine Hände bleiben in der Grundposition
- Deutlich schneller bei häufiger Nutzung
- Auf manchen Servern funktionieren Pfeiltasten nicht richtig

**In den Insert-Modus wechseln:**
- `i` - Insert vor dem Cursor (am häufigsten)
- `a` - Append nach dem Cursor
- `o` - Neue Zeile unter der aktuellen öffnen
- `O` - Neue Zeile über der aktuellen öffnen

**Text bearbeiten (im Normal-Modus):**
- `x` - Zeichen unter dem Cursor löschen
- `dd` - Ganze Zeile löschen
- `yy` - Ganze Zeile kopieren (yank)
- `p` - Kopierten/gelöschten Text einfügen (paste)
- `u` - Letzte Aktion rückgängig machen (undo)
- `Ctrl+r` - Rückgängig gemachte Aktion wiederholen (redo)

**Suchen und Ersetzen:**
- `/suchtext` - Suche nach "suchtext" (mit Enter bestätigen)
- `n` - Zum nächsten Treffer springen
- `N` - Zum vorherigen Treffer springen
- `:s/alt/neu/` - Ersetze "alt" durch "neu" in aktueller Zeile
- `:%s/alt/neu/g` - Ersetze "alt" durch "neu" in der ganzen Datei

**Warum vim lernen?**
- Auf jedem Linux-System verfügbar
- Sehr effizient bei der Textbearbeitung
- Keine Maus erforderlich
- Mächtige Funktionen für Programmierung und Administration
- Einmal gelernt, überall einsetzbar

---

### Aufgabe 3: vim Grundlagen - Modi-Training

**Starte vim und verstehe die Modi:**

```bash
cd ~/grep_vim_challenge
vim erste_uebung.txt
```

Du siehst jetzt das vim-Interface. Unten sollten Tilden (~) stehen, die leere Zeilen anzeigen.

**Modi-Training - Folge dieser Schritt-für-Schritt Anleitung:**

**Schritt 1: Verstehe den Normal-Modus**
- Du bist jetzt im Normal-Modus
- Drücke ein paar Buchstaben (z.B. 'a', 'b', 'c')
- **Beobachtung:** Die Buchstaben werden NICHT eingefügt, sondern führen Befehle aus

**Schritt 2: Wechsle bewusst in den Insert-Modus**
- Drücke `i`
- Unten sollte jetzt "-- INSERT --" stehen
- **Das ist der visuelle Beweis, dass du im Insert-Modus bist!**

**Schritt 3: Schreibe Text**
```
Das ist meine erste vim-Übung.
Ich lerne die verschiedenen Modi kennen.
Normal-Modus für Befehle und Navigation.
Insert-Modus zum Schreiben von Text.
Command-Modus für vim-Befehle.
```

**Schritt 4: Modi-Wechsel trainieren**
- Drücke ESC (zurück zum Normal-Modus)
- Die "-- INSERT --" Anzeige verschwindet
- Drücke `i` (wieder in Insert-Modus)
- Die "-- INSERT --" Anzeige erscheint wieder
- Drücke wieder ESC

**Wichtige Regel:** Immer wenn du unsicher bist, drücke ESC!

**Schritt 5: Navigation im Normal-Modus**
- Stelle sicher, dass du im Normal-Modus bist (ESC drücken)
- Bewege dich mit `h` `j` `k` `l` durch den Text
- Probiere `w` für Wortsprünge
- Teste `0` für Zeilenanfang, `$` für Zeilenende
- `gg` für Dateianfang, `G` für Dateiende

**Schritt 6: Command-Modus testen**
- Drücke `:w` (dann Enter) - speichert die Datei
- vim zeigt an: "erste_uebung.txt" [New] 5L, xxC written

**Schritt 7: Beende vim**
- Drücke `:q` (dann Enter)

**Modi-Verständnis-Test:**
Führe diesen Test durch, um sicherzustellen, dass du die Modi verstehst:

```bash
vim modi_test.txt
```

1. Schreibe: "Ich bin im Insert-Modus" (vergiss nicht `i` zu drücken!)
2. Drücke ESC
3. Navigiere mit `j` `k` `h` `l` (du bist im Normal-Modus)
4. Drücke `:w` und Enter (Command-Modus)
5. Drücke `i` und schreibe: "Wieder im Insert-Modus"
6. Drücke ESC, dann `:wq` und Enter

**Fragen zur Aufgabe 3:**
1. In welchem Modus startet vim standardmäßig?
2. Wie kommst du von jedem beliebigen Modus zurück zum Normal-Modus?
3. Was ist der Unterschied zwischen `:q` und `:q!`?
4. Woran erkennst du visuell, dass du im Insert-Modus bist?

**Screenshot-Aufgabe 3:**
Öffne die Datei erneut mit `vim erste_uebung.txt` und mache einen Screenshot vom vim-Interface mit deinem Text.

---

### Aufgabe 4: vim Text-Bearbeitung

Öffne eine neue Datei für Bearbeitungsübungen:

```bash
vim textbearbeitung.txt
```

**Erstelle folgenden Inhalt (vergiss nicht, mit `i` in den Insert-Modus zu wechseln):**

```
Linux ist ein tolles Betriebssystem.
vim ist ein mächtiger Editor.
grep ist perfekt für Textsuche.
Diese Zeile hat einen Fehllr.
Windows ist auch okay.
Aber Linux ist besser.
Diese Zeile wird gelöscht.
Das ist eine wichtige Zeile.
```

**Jetzt im Normal-Modus (ESC drücken) verschiedene Bearbeitungen ausführen:**

**1. Ganze Zeile löschen (dd-Befehl verstehen):**
- Navigiere zu "Diese Zeile wird gelöscht." (mit `j` `k` oder Pfeiltasten)
- **Wichtig:** Stelle sicher, dass du im Normal-Modus bist
- Drücke `dd`
- Die ganze Zeile wird gelöscht und in den "Puffer" kopiert

**2. Einzelnes Zeichen korrigieren (x-Befehl):**
- Navigiere zum Wort "Fehllr" in Zeile 4
- Positioniere den Cursor auf das zusätzliche "l" (mit `h` `l`)
- Drücke `x`
- Der Buchstabe wird gelöscht

**3. Text am Zeilenende hinzufügen (A-Befehl verstehen):**
- Gehe zur Zeile "vim ist ein mächtiger Editor."
- Drücke `A` (springt automatisch ans Zeilenende UND wechselt in Insert-Modus)
- Schreibe: " und sehr effizient"
- Drücke ESC

**Unterschied zwischen `a` und `A`:**
- `a` = append nach dem Cursor an aktueller Position
- `A` = append am Ende der Zeile (sehr praktisch!)

**4. Neue Zeile erstellen (o-Befehl verstehen):**
- Gehe zu "Linux ist ein tolles Betriebssystem."
- Drücke `o` (öffnet neue Zeile darunter UND wechselt in Insert-Modus)
- Schreibe: "Es ist kostenlos und quelloffen."
- Drücke ESC

**Unterschied zwischen `o` und `O`:**
- `o` = neue Zeile UNTER der aktuellen
- `O` = neue Zeile ÜBER der aktuellen

**5. Zeile kopieren und einfügen (yy und p verstehen):**
- Gehe zu "Aber Linux ist besser."
- Drücke `yy` (kopiert die ganze Zeile in den "Puffer")
- Drücke `p` (fügt die Zeile unter der aktuellen ein)
- **Ergebnis:** Die Zeile erscheint doppelt

**6. Undo und Redo trainieren:**
- Drücke `u` (macht die letzte Aktion rückgängig)
- Drücke `Ctrl+r` (wiederholt die rückgängig gemachte Aktion)
- Teste dies mehrmals mit verschiedenen Aktionen

**7. Speichere die Änderungen:**
- Drücke `:w`

**Warum sind diese Befehle so mächtig?**
- `dd`, `yy`, `p` arbeiten mit einem unsichtbaren "Puffer"
- Du kannst komplexe Bearbeitungen mit wenigen Tastenanschlägen durchführen
- Keine Maus erforderlich - viel schneller!

**Fragen zur Aufgabe 4:**
1. Was passiert, wenn du `dd` drückst und danach sofort `u`?
2. Welcher Unterschied besteht zwischen `i` und `a` beim Wechsel in den Insert-Modus?
3. Erkläre, was `yy` macht und warum das praktisch ist
4. Warum ist `A` oft praktischer als `a`?

**Screenshot-Aufgabe 4:**
Screenshot der fertig bearbeiteten Datei in vim.

---

### Aufgabe 5: vim Suchen und Ersetzen

Öffne eine neue Datei für Such- und Ersetzungsübungen:

```bash
vim suchtest.txt
```

**Erstelle folgenden Inhalt:**

```
Der Server läuft auf Port 8080.
Die Datenbank verwendet Port 5432.
Der Webserver nutzt auch Port 8080.
FTP läuft auf Port 21.
SSH verwendet Port 22.
Der neue Service braucht Port 8080.
Port 443 ist für HTTPS reserviert.
Alle Port-Konfigurationen sind wichtig.
```

**Teste Such- und Ersetzungsfunktionen:**

**1. Einfache Suche verstehen:**
- Drücke `/Port` (dann Enter)
- vim springt zum ersten Vorkommen von "Port"
- **Beobachte:** Das gefundene Wort wird hervorgehoben
- Drücke `n` für den nächsten Treffer
- Drücke `N` für den vorherigen Treffer
- **Tipp:** Mit `/` suchst du vorwärts, mit `?` rückwärts

**2. Text in einer Zeile ersetzen:**
- Gehe zur ersten Zeile (mit `gg`)
- Drücke `:s/8080/9090/` (dann Enter)
- Nur in der aktuellen Zeile wird 8080 durch 9090 ersetzt
- **Beobachte:** Nur das erste Vorkommen in der Zeile wird ersetzt

**3. Alle Vorkommen in einer Zeile ersetzen:**
- Falls mehrere 8080 in einer Zeile stehen würden:
- `:s/8080/9090/g` (das `g` steht für "global" = alle in der Zeile)

**4. Text in der ganzen Datei ersetzen:**
- Drücke `:1` (gehe zu Zeile 1)
- Drücke `:%s/Port/PORT/g` (dann Enter)
- Alle Vorkommen von "Port" werden zu "PORT"
- **Aufschlüsselung:** `%` = ganze Datei, `s` = substitute, `g` = global

**5. Änderungen rückgängig machen:**
- Drücke `u` mehrmals, um die Änderungen rückgängig zu machen

**6. Ersetzen mit Bestätigung (sehr wichtig in der Praxis!):**
- Drücke `:%s/Port/PORT/gc` (dann Enter)
- vim fragt bei jedem Treffer:
  - `y` = yes (ersetzen)
  - `n` = no (nicht ersetzen)
  - `a` = all (alle restlichen ersetzen)
  - `q` = quit (abbrechen)
  - `l` = last (dieses ersetzen und aufhören)

**Such- und Ersetzungs-Cheatsheet:**
```
/text           - Suche vorwärts nach "text"
?text           - Suche rückwärts nach "text"
n               - Nächster Treffer
N               - Vorheriger Treffer
:s/alt/neu/     - Ersetze in aktueller Zeile (erstes Vorkommen)
:s/alt/neu/g    - Ersetze in aktueller Zeile (alle Vorkommen)
:%s/alt/neu/g   - Ersetze in ganzer Datei (alle Vorkommen)
:%s/alt/neu/gc  - Ersetze in ganzer Datei (mit Bestätigung)
```

**Fragen zur Aufgabe 5:**
1. Was ist der Unterschied zwischen `:s/alt/neu/` und `:%s/alt/neu/g`?
2. Wozu dient das `c` in `:%s/alt/neu/gc`?
3. Wie findest du das nächste Vorkommen nach einer Suche mit `/suchtext`?
4. Warum ist die Bestätigungsfunktion (`c`) in der Praxis so wichtig?

**Screenshot-Aufgabe 5:**
Screenshot während einer aktiven Suche (wenn vim ein gefundenes Wort hervorhebt).

---

## Teil 3: grep und vim in der Praxis kombinieren

### Warum grep und vim zusammengehören

In der echten Systemadministration verwendest du beide Tools im Tandem:
1. **grep** analysiert große Datenmengen und findet interessante Stellen
2. **vim** bearbeitet dann gezielt die gefundenen Probleme
3. **grep** überprüft deine Änderungen

**Typischer Workflow:**
```
grep "ERROR" logfile.txt → Fehler identifizieren
vim logfile.txt → zur entsprechenden Zeile springen und umgebenden Code analysieren
vim configfile.txt → Konfiguration anpassen
grep "ERROR" logfile.txt → überprüfen, ob Fehler behoben
```

### Aufgabe 6: Realistische Log-Analyse

Jetzt wendest du beide Tools in einem realistischen Szenario an. Erstelle eine umfangreichere Logdatei:

```bash
cat > system_log.txt << 'EOF'
2024-01-15 08:00:01 INFO: System gestartet
2024-01-15 08:00:05 INFO: Netzwerkinterface eth0 aktiviert  
2024-01-15 08:00:10 WARNING: Festplatte /dev/sda1 90% voll
2024-01-15 08:15:22 ERROR: Dienst apache2 nicht erreichbar
2024-01-15 08:15:25 INFO: Neustart von apache2 initiiert
2024-01-15 08:15:30 INFO: apache2 erfolgreich gestartet
2024-01-15 08:30:45 WARNING: Hohe CPU-Last: 95%
2024-01-15 08:31:10 INFO: CPU-Last normalisiert: 45%
2024-01-15 09:00:15 ERROR: Datenbankverbindung unterbrochen
2024-01-15 09:00:20 INFO: Datenbank-Reconnect erfolgreich
2024-01-15 09:15:33 WARNING: Arbeitsspeicher 85% belegt
2024-01-15 09:30:44 ERROR: Backup-Prozess fehlgeschlagen
2024-01-15 09:31:00 INFO: Manueller Backup-Start
2024-01-15 09:45:15 INFO: Backup erfolgreich abgeschlossen
EOF
```

**Schritt 1: Analyse mit grep (Probleme identifizieren)**

**1. Finde alle kritischen Fehler:**
```bash
grep "ERROR" system_log.txt
```
**Warum wichtig:** Diese Zeilen zeigen dir, wo Systeme ausgefallen sind.

**2. Zeige Fehler mit Kontext:**
```bash
grep -C 2 "ERROR" system_log.txt
```
**Warum wichtig:** Du siehst, was vor und nach dem Fehler passierte - oft entscheidend für die Ursachenanalyse.

**3. Analysiere Warnings (potentielle Probleme):**
```bash
grep "WARNING" system_log.txt
```

**4. Speichere alle Fehler in eine separate Datei:**
```bash
grep "ERROR" system_log.txt > fehler_liste.txt
```
**Warum wichtig:** Du kannst die Fehler separat dokumentieren und bearbeiten.

**5. Zähle verschiedene Log-Level:**
```bash
echo "=== SYSTEM LOG STATISTIK ==="
echo "ERROR-Meldungen: $(grep -c "ERROR" system_log.txt)"
echo "WARNING-Meldungen: $(grep -c "WARNING" system_log.txt)"
echo "INFO-Meldungen: $(grep -c "INFO" system_log.txt)"
```

**6. Finde zeitliche Patterns:**
```bash
grep "08:15" system_log.txt  # Was passierte um 8:15?
grep "09:.*ERROR" system_log.txt  # Alle Errors um 9 Uhr
```

**Schritt 2: Dokumentation mit vim (Probleme dokumentieren)**

**1. Öffne die Fehlerliste zur Bearbeitung:**
```bash
vim fehler_liste.txt
```

**2. Füge eine strukturierte Analyse hinzu:**
- Gehe ans Ende der Datei mit `G`
- Drücke `o` für eine neue Zeile
- Wechsle in den Insert-Modus und schreibe:

```
FEHLERANALYSE:
==============
Identifizierte Probleme:

1. apache2 Ausfall (08:15:22)
   - Symptom: Dienst nicht erreichbar
   - Lösung: Automatischer Neustart erfolgreich
   - Status: BEHOBEN
   - Empfehlung: Überwachung verstärken

2. Datenbankverbindung (09:00:15)
   - Symptom: Verbindung unterbrochen
   - Lösung: Automatischer Reconnect
   - Status: BEHOBEN
   - Empfehlung: Verbindungsstabilität prüfen

3. Backup-Prozess (09:30:44)
   - Symptom: Automatischer Backup fehlgeschlagen
   - Lösung: Manueller Start erfolgreich
   - Status: BEHOBEN
   - Empfehlung: Backup-Script überprüfen

KRITIKALITÄT:
- Alle Probleme wurden automatisch oder manuell behoben
- Backup-Problem erfordert Aufmerksamkeit
- System grundsätzlich stabil
```

**3. Speichere und beende:**
- ESC drücken
- `:wq` eingeben

**Schritt 3: Zusammenfassender Bericht (grep + vim Kombination)**

Erstelle einen umfassenden Bericht mit beiden Tools:

```bash
# Erstelle automatisch Statistiken mit grep
echo "SYSTEM-LOG ANALYSE BERICHT" > analysebericht.txt
echo "=========================" >> analysebericht.txt
echo "" >> analysebericht.txt
echo "Zeitraum: 15.01.2024 08:00-09:45" >> analysebericht.txt
echo "Analysiert am: $(date)" >> analysebericht.txt
echo "" >> analysebericht.txt
echo "STATISTIKEN:" >> analysebericht.txt
echo "ERROR-Meldungen: $(grep -c "ERROR" system_log.txt)" >> analysebericht.txt
echo "WARNING-Meldungen: $(grep -c "WARNING" system_log.txt)" >> analysebericht.txt
echo "INFO-Meldungen: $(grep -c "INFO" system_log.txt)" >> analysebericht.txt
echo "" >> analysebericht.txt
echo "ZEITVERTEILUNG DER PROBLEME:" >> analysebericht.txt
echo "8 Uhr: $(grep -c "08:.*ERROR\|08:.*WARNING" system_log.txt) Probleme" >> analysebericht.txt
echo "9 Uhr: $(grep -c "09:.*ERROR\|09:.*WARNING" system_log.txt) Probleme" >> analysebericht.txt

# Öffne den Bericht in vim zur manuellen Vervollständigung
vim analysebericht.txt
```

**In vim vervollständige den Bericht:**
- Gehe ans Ende mit `G`
- Füge hinzu:

```
DETAILANALYSE:
==============

PATTERNS UND TRENDS:
- Probleme konzentrierten sich auf 8:15 und 9:00 Uhr
- Alle kritischen Services haben Selbstheilungsmechanismen
- Backup-System benötigt manuelle Überwachung

EMPFOHLENE AKTIONEN:
1. Backup-Script auf Robustheit prüfen
2. Monitoring für apache2 und Datenbank verstärken
3. Ressourcenverbrauch überwachen (CPU/RAM/Disk)

RISIKOBEWERTUNG: NIEDRIG
- Alle Ausfälle wurden schnell behoben
- Redundante Systeme funktionieren
- Manuelle Eingriffe minimal erforderlich
```

**Profi-Tipp - grep in vim:**
Sogar in vim kannst du grep verwenden:
- In vim: `:!grep "ERROR" system_log.txt`
- Das führt grep aus und zeigt das Ergebnis in vim an

**Fragen zur Aufgabe 6:**
1. Wie kombinierst du grep mit Ausgabeumleitung, um Suchergebnisse in eine Datei zu speichern?
2. Warum ist `grep -C 2` bei der Fehleranalyse besonders wertvoll?
3. Wie navigierst du in vim schnell zwischen Dateianfang und -ende?
4. Erkläre den Workflow: Warum erst grep, dann vim?

**Screenshot-Aufgabe 6:**
Screenshot deines selbst erstellten Analyseberichts in vim.

---

### Abschluss-Challenge: Webserver-Log-Analyse

**Erstelle eine realistische Webserver-Logdatei:**

```bash
cat > webserver.log << 'EOF'
192.168.1.100 - - [15/Jan/2024:08:00:15 +0100] "GET /index.html HTTP/1.1" 200 1234
192.168.1.105 - - [15/Jan/2024:08:01:22 +0100] "GET /api/users HTTP/1.1" 200 567
10.0.0.50 - - [15/Jan/2024:08:02:33 +0100] "POST /login HTTP/1.1" 401 89
192.168.1.100 - - [15/Jan/2024:08:03:44 +0100] "GET /admin HTTP/1.1" 403 156
10.0.0.75 - - [15/Jan/2024:08:04:55 +0100] "GET /api/data HTTP/1.1" 500 0
192.168.1.105 - - [15/Jan/2024:08:05:11 +0100] "GET /images/logo.png HTTP/1.1" 200 4567
10.0.0.50 - - [15/Jan/2024:08:06:22 +0100] "POST /login HTTP/1.1" 200 234
192.168.1.200 - - [15/Jan/2024:08:07:33 +0100] "GET /api/status HTTP/1.1" 404 78
10.0.0.75 - - [15/Jan/2024:08:08:44 +0100] "GET /api/data HTTP/1.1" 500 0
192.168.1.100 - - [15/Jan/2024:08:09:55 +0100] "DELETE /api/user/123 HTTP/1.1" 200 12
EOF
```

**Deine Aufgabe als System-Administrator:**

**1. Verstehe das Logformat:**
```bash
head -1 webserver.log  # Erste Zeile anschauen
```
**Format:** IP - - [Zeitstempel] "HTTP-Request" Status-Code Größe

**2. Finde alle HTTP-Fehlercodes (4xx und 5xx):**
```bash
grep " [45][0-9][0-9] " webserver.log
```
**Was bedeutet dieser RegEx:**
- ` ` = Leerzeichen vor dem Status-Code
- `[45]` = Ziffer 4 oder 5
- `[0-9][0-9]` = zwei weitere Ziffern
- ` ` = Leerzeichen nach dem Status-Code

**3. Analysiere problematische IP-Adressen:**
```bash
# Alle Fehler von externen IPs (10.0.0.x):
grep " [45][0-9][0-9] " webserver.log | grep "10\.0\.0\."

# Alle Requests einer bestimmten IP:
grep "10\.0\.0\.75" webserver.log
```

**4. Finde verschiedene Arten von Problemen:**
```bash
grep " 401 " webserver.log  # Unauthorized (Anmeldefehler)
grep " 403 " webserver.log  # Forbidden (Zugriff verweigert)
grep " 404 " webserver.log  # Not Found (Seite nicht gefunden)
grep " 500 " webserver.log  # Internal Server Error (Server-Problem)
```

**5. Erstelle einen Sicherheitsbericht mit vim:**
```bash
vim sicherheitsbericht.txt
```

**Schreibe in vim einen strukturierten Bericht:**

```
WEBSERVER SICHERHEITSANALYSE
============================
Datum: 15.01.2024
Zeitraum: 08:00-08:10
Analysiert von: [Dein Name]

LOG-FORMAT VERSTEHEN:
IP-Adresse - - [Zeitstempel] "HTTP-Request" Status-Code Größe

KRITISCHE BEFUNDE:
==================

1. SERVER-ERRORS (5xx):
   - IP 10.0.0.75: Mehrfache 500-Fehler bei /api/data
   - Zeitpunkte: 08:04:55 und 08:08:44
   - Problem: API-Endpoint instabil oder überlastet

2. AUTHENTICATION-PROBLEME (4xx):
   - IP 10.0.0.50: 401 bei /login (08:02:33)
   - Danach erfolgreicher Login (08:06:22)
   - Mögliche Brute-Force oder Credential-Problem

3. ZUGRIFFSVERLETZUNGEN:
   - IP 192.168.1.100: 403 bei /admin (08:03:44)
   - Unbefugter Zugriff auf Admin-Bereich versucht

4. MISSING RESOURCES:
   - IP 192.168.1.200: 404 bei /api/status (08:07:33)
   - API-Endpoint existiert nicht oder wurde verschoben

VERDÄCHTIGE AKTIVITÄTEN:
========================
- IP 10.0.0.75: Wiederholte API-Aufrufe trotz 500-Errors
- IP 10.0.0.50: Login-Pattern (erst fehlgeschlagen, dann erfolgreich)
- IP 192.168.1.100: Admin-Zugriff versucht (interne IP!)

RISIKOBEWERTUNG:
===============
- HOCH: Wiederholte 500-Errors deuten auf System-Instabilität
- MITTEL: Failed Login mit nachfolgendem Success
- NIEDRIG: 404-Errors (normale Exploration)

EMPFOHLENE MASSNAHMEN:
=====================
1. SOFORT:
   - IP 10.0.0.75 temporär blockieren
   - API /api/data auf Stabilität prüfen
   - Login-Versuche von 10.0.0.50 überwachen

2. KURZFRISTIG:
   - Admin-Bereich zusätzlich absichern
   - Rate-Limiting für API-Endpoints implementieren
   - Monitoring für 500-Errors einrichten

3. LANGFRISTIG:
   - Intrusion Detection System (IDS) implementieren
   - Log-Analyse automatisieren
   - Backup-Strategien für kritische APIs
```

**6. Ergänze automatisierte Statistiken:**

Verlasse vim (`:wq`) und führe aus:

```bash
echo "" >> sicherheitsbericht.txt
echo "AUTOMATISIERTE STATISTIKEN:" >> sicherheitsbericht.txt
echo "==========================" >> sicherheitsbericht.txt
echo "Generiert am: $(date)" >> sicherheitsbericht.txt
echo "" >> sicherheitsbericht.txt
echo "Gesamte Requests: $(wc -l < webserver.log)" >> sicherheitsbericht.txt  
echo "Erfolgreiche Requests (2xx): $(grep -c " 2[0-9][0-9] " webserver.log)" >> sicherheitsbericht.txt
echo "Client-Fehler (4xx): $(grep -c " 4[0-9][0-9] " webserver.log)" >> sicherheitsbericht.txt
echo "Server-Fehler (5xx): $(grep -c " 5[0-9][0-9] " webserver.log)" >> sicherheitsbericht.txt
echo "" >> sicherheitsbericht.txt
echo "TOP PROBLEMATISCHE IPs:" >> sicherheitsbericht.txt
echo "$(grep " [45][0-9][0-9] " webserver.log | cut -d' ' -f1 | sort | uniq -c | sort -nr)" >> sicherheitsbericht.txt

# Öffne wieder in vim zur finalen Überprüfung
vim sicherheitsbericht.txt
```

**7. Erweiterte grep-Analyse:**
```bash
# Finde alle POST-Requests:
grep "POST" webserver.log

# Finde große Responses (über 1000 Bytes):
grep -E " [0-9]{4,} ?$" webserver.log

# Finde alle Requests zwischen 8:05 und 8:08:
grep "08:0[5-8]:" webserver.log
```

**Profi-Techniken kombinieren:**
```bash
# Pipe grep und vim:
grep " [45][0-9][0-9] " webserver.log > probleme.txt
vim probleme.txt

# In vim nach IP suchen:
# In vim: /10\.0\.0\.75
```

**Abschluss-Fragen:**
1. Erkläre den grep-Befehl `grep " [45][0-9][0-9] " webserver.log` - was genau macht er?
2. Wie würdest du in vim schnell zu einem bestimmten Abschnitt deines Berichts navigieren?
3. Welche Vorteile hat die Kombination von grep für die Analyse und vim für die Dokumentation?
4. Warum sind Backslashes in `grep "10\.0\.0\.75"` notwendig?

**Final-Screenshot:**
Screenshot deines fertigen Sicherheitsberichts in vim.

---

**Was du gelernt hast:**

**grep - Der Text-Detektiv:**
- Basis-Befehle für einfache Suchen
- Reguläre Ausdrücke für mächtige Mustersuche
- Optionen für Kontext und Filterung
- Praktische Anwendung in der Systemadministration

**vim - Der Text-Chirurg:**
- Modi-System verstehen und beherrschen
- Navigation ohne Maus
- Effiziente Text-Bearbeitung
- Suchen und Ersetzen in großen Dateien

**Kombination beider Tools:**
- Workflow: Analysieren → Dokumentieren → Überprüfen
- Automatisierung von Berichten
- Professionelle Problemlösung

**Deine neuen Skills:**
- Du kannst riesige Logdateien in Sekunden analysieren
- Du bearbeitest Konfigurationsdateien wie ein Profi
- Du dokumentierst Probleme strukturiert und nachvollziehbar
- Du arbeitest effizient ohne grafische Oberfläche

**Denk daran:**
grep und vim sind wie Werkzeuge in einer Werkstatt - je öfter du sie verwendest, desto geschickter wirst du. Übung macht den meister!

Verwende grep und vim regelmäßig in deinen täglichen Aufgaben - sie werden schnell zu unverzichtbaren Begleitern :D
