# Linux Praxis Challenge: sed & awk
*Für Windows 11 mit WSL (Windows Subsystem for Linux)*

---

## Überblick der Challenge

In dieser Challenge lernst du zwei der mächtigsten Werkzeuge für die automatisierte Textverarbeitung in Linux kennen: **sed** (Stream Editor) und **awk** (Programmiersprache für strukturierte Daten). Diese Tools sind unverzichtbar für jeden, der regelmäßig mit Textdateien, Logs oder Daten arbeitet.

**Was sind sed und awk genau?**
- **sed** ist ein "Stream Editor" - er verarbeitet Text zeilenweise, ohne eine Datei zu öffnen
- **awk** ist eine vollständige Programmiersprache, spezialisiert auf spaltenbasierte Daten
- Beide arbeiten nach dem Unix-Prinzip: Lesen von Standard-Input, Verarbeiten, Ausgabe an Standard-Output

**Warum sind diese Tools so wichtig?**
- **Automatisierung:** Textverarbeitung ohne manuelle Eingriffe
- **Effizienz:** Verarbeitung großer Dateien ohne viel Speicherverbrauch
- **Flexibilität:** Von einfachen Ersetzungen bis zu komplexen Datenanalysen
- **Universalität:** Auf jedem Linux/Unix-System verfügbar

**Aufbau der Challenge:**
1. **Teil 1:** sed - Stream Editor verstehen und anwenden (Grundlagenaufgabe/Verpflichtend)
2. **Teil 2:** awk - Strukturierte Datenverarbeitung meistern 
3. **Teil 3:** Beide Tools kombinieren für realistische Szenarien

**Lernpfad:**
Einfache Textmanipulation → Strukturierte Datenverarbeitung → Automatisierte Workflows

---

## Teil 1: sed - Der Stream Editor verstehen

### Was ist ein Stream Editor?

Ein **Stream Editor** wie sed verarbeitet Text **sequenziell** - Zeile für Zeile, von Anfang bis Ende. Anders als bei einem normalen Editor wie vim öffnest du nicht die Datei zur Bearbeitung, sondern sed liest jede Zeile, wendet deine Regeln an und gibt das Ergebnis aus.

**Das Stream-Konzept verstehen:**
```
Input → sed Verarbeitung → Output
Datei → Regel anwenden → Bildschirm/neue Datei
```

**Warum ist das so mächtig?**
- Funktioniert mit riesigen Dateien (Gigabytes)
- Kann in Pipelines integriert werden
- Verändert Original nicht (außer mit -i Option)
- Sehr schnell und speicherschonend

### sed Grundlagen: Der Pattern Space

sed arbeitet mit einem Konzept namens **Pattern Space** - einem internen Speicherbereich, in dem jede Zeile verarbeitet wird:

1. **Zeile lesen** → Pattern Space
2. **Befehle ausführen** → Zeile im Pattern Space bearbeiten  
3. **Ausgabe** → Zeile aus Pattern Space ausgeben
4. **Nächste Zeile** → Prozess wiederholen

**Grundsyntax verstehen:**
```bash
sed 'adresse befehl' datei.txt
```

- **adresse:** Welche Zeile(n) bearbeiten (optional)
- **befehl:** Was mit der Zeile machen
- **datei.txt:** Input-Datei

### Die wichtigsten sed-Befehle erklärt

**1. Substitute (s) - Ersetzen:**
```bash
sed 's/alt/neu/' datei.txt        # Ersetzt erstes Vorkommen pro Zeile
sed 's/alt/neu/g' datei.txt       # Ersetzt ALLE Vorkommen (global)
sed 's/alt/neu/2' datei.txt       # Ersetzt nur das 2. Vorkommen pro Zeile
sed 's/alt/neu/gi' datei.txt      # Global + case insensitive
```

**Was bedeutet das 'g' Flag?**
Ohne 'g' ersetzt sed nur das erste Vorkommen pro Zeile. Mit 'g' (global) werden alle Vorkommen in jeder Zeile ersetzt.

**2. Delete (d) - Löschen:**
```bash
sed '5d' datei.txt               # Löscht Zeile 5
sed '2,4d' datei.txt             # Löscht Zeilen 2 bis 4  
sed '/muster/d' datei.txt        # Löscht alle Zeilen die "muster" enthalten
sed '/^$/d' datei.txt            # Löscht leere Zeilen
```

**3. Insert (i) und Append (a) - Einfügen:**
```bash
sed '3i\Neue Zeile' datei.txt    # Fügt VOR Zeile 3 ein
sed '3a\Neue Zeile' datei.txt    # Fügt NACH Zeile 3 ein
sed '$a\Letzte Zeile' datei.txt  # Fügt am Dateiende ein
```

**4. Print (p) - Ausgabe steuern:**
```bash
sed -n '5p' datei.txt            # Zeigt NUR Zeile 5 (-n unterdrückt normale Ausgabe)
sed -n '2,4p' datei.txt          # Zeigt nur Zeilen 2-4
sed -n '/muster/p' datei.txt     # Zeigt nur Zeilen mit "muster"
```

**Adressen in sed verstehen:**
- **Zahl:** Bestimmte Zeile (z.B. `5`)
- **Bereich:** Mehrere Zeilen (z.B. `2,4`)
- **Muster:** Zeilen die Muster enthalten (z.B. `/ERROR/`)
- **$:** Letzte Zeile
- **Keine Adresse:** Alle Zeilen

---

### Aufgabe 1: sed Grundlagen - Ersetzen verstehen und anwenden

Erstelle eine Arbeitsumgebung für praktische Übungen:

```bash
cd ~
mkdir sed_awk_challenge
cd sed_awk_challenge
```

**Erstelle eine realistische Konfigurationsdatei:**

```bash
cat > webapp_config.txt << 'EOF'
# Web Application Configuration
server_port=8080
database_host=localhost
database_port=5432
debug_mode=true
log_level=INFO
max_connections=100
timeout=30
ssl_enabled=false
ssl_port=443
backup_enabled=false
backup_time=02:00
admin_email=admin@oldcompany.com
api_endpoint=http://api.oldcompany.com/v1
cache_size=512MB
session_timeout=3600
EOF
```

**Erstelle eine typische Logdatei:**

```bash
cat > system.log << 'EOF'
2024-01-15 09:30:22 INFO: System startup completed
2024-01-15 09:30:25 DEBUG: Configuration loaded from /etc/webapp.conf
2024-01-15 09:32:10 WARN: SSL certificate expires in 30 days
2024-01-15 09:35:45 ERROR: Database connection failed: timeout
2024-01-15 09:36:00 INFO: Retrying database connection
2024-01-15 09:36:05 INFO: Database connection established
2024-01-15 09:38:22 ERROR: Authentication failed for user: john.doe@company.com
2024-01-15 09:40:15 INFO: Scheduled backup started
2024-01-15 09:42:30 WARN: Memory usage high: 85% of available RAM
2024-01-15 09:45:10 ERROR: Backup process failed: insufficient disk space
2024-01-15 09:46:00 INFO: Cleanup process completed
EOF
```

**Jetzt teste sed Schritt für Schritt:**

1. **Einfache Ersetzung verstehen:**
```bash
# Zeige zuerst die Originaldatei
echo "=== ORIGINAL KONFIGURATION ==="
cat webapp_config.txt

# Ändere den Port (nur Ausgabe, Datei bleibt unverändert)
echo -e "\n=== PORT 8080 → 9090 ==="
sed 's/8080/9090/' webapp_config.txt

# Überprüfe: Originaldatei ist unverändert
echo -e "\n=== ORIGINAL PRÜFUNG ==="
grep "server_port" webapp_config.txt
```

2. **Globale Ersetzung (g-Flag) verstehen:**
```bash
# Ändere alle Vorkommen der Domain
echo "=== DOMAIN ÄNDERN (GLOBAL) ==="
sed 's/oldcompany\.com/newcompany.com/g' webapp_config.txt

# Erkläre warum der Punkt escaped wird:
echo -e "\n=== WARUM DER BACKSLASH? ==="
echo "Ohne Backslash (FALSCH):"
sed 's/oldcompany.com/MATCH/g' webapp_config.txt | grep MATCH
echo "Mit Backslash (RICHTIG):"
sed 's/oldcompany\.com/MATCH/g' webapp_config.txt | grep MATCH
```

3. **Case-insensitive Ersetzung:**
```bash
# Ändere INFO zu INFORMATION (unabhängig von Groß-/Kleinschreibung)
echo "=== CASE-INSENSITIVE ERSETZUNG ==="
sed 's/info/INFORMATION/gi' system.log
```

4. **Permanent speichern mit -i Option:**
```bash
# Erstelle eine Backup-Datei und ändere sie permanent
cp webapp_config.txt webapp_config_new.txt

echo "=== VOR DER ÄNDERUNG ==="
grep "server_port\|admin_email" webapp_config_new.txt

# Permanente Änderung mit -i
sed -i 's/8080/9090/' webapp_config_new.txt
sed -i 's/oldcompany\.com/newcompany.com/g' webapp_config_new.txt

echo "=== NACH DER ÄNDERUNG ==="
grep "server_port\|admin_email" webapp_config_new.txt
```

**Verstehe, was passiert ist:**
- **Ohne -i:** sed gibt nur das Ergebnis aus, Originaldatei bleibt unverändert
- **Mit -i:** sed ändert die Datei direkt
- **Backslash vor Punkt:** In regulären Ausdrücken ist '.' ein Platzhalter für "jedes Zeichen", '\.' bedeutet "der Punkt selbst"

**Fragen zur Aufgabe 1:**
1. **Erkläre den Unterschied:** Was passiert bei `sed 's/test/TEST/'` vs `sed 's/test/TEST/g'` wenn eine Zeile "test test test" enthält?
2. **Warum Backslash:** Warum schreibt man `oldcompany\.com` statt `oldcompany.com` in sed?
3. **Sicherheit:** Was ist der Vorteil, dass sed standardmäßig die Originaldatei nicht verändert?

**Screenshot-Aufgabe 1:**
Screenshot der Ausgabe von: `sed 's/oldcompany\.com/newcompany.com/g' webapp_config.txt`

---

### Aufgabe 2: sed Erweiterte Funktionen - Zeilen löschen und hinzufügen

**Erstelle eine gemischte Datei mit verschiedenen Inhaltstypen:**

```bash
cat > mixed_config.txt << 'EOF'
# Configuration file for production environment
# Generated on 2024-01-15

server_name=webapp-prod
server_port=8080

# Database settings
db_host=localhost
db_port=5432
db_name=production

# Debug settings (remove in production)
debug_mode=true
verbose_logging=true

# Cache configuration
cache_enabled=true
cache_size=1024MB

# Backup configuration
backup_enabled=false
backup_schedule=daily

# End of configuration
EOF
```

**Lerne erweiterte sed-Funktionen:**

1. **Zeilen löschen nach Mustern:**
```bash
echo "=== ORIGINAL DATEI ==="
cat -n mixed_config.txt  # -n zeigt Zeilennummern

echo -e "\n=== ENTFERNE ALLE KOMMENTARE ==="
sed '/^#/d' mixed_config.txt

echo -e "\n=== ENTFERNE LEERE ZEILEN ==="
sed '/^$/d' mixed_config.txt

echo -e "\n=== ENTFERNE KOMMENTARE UND LEERE ZEILEN ==="
sed -e '/^#/d' -e '/^$/d' mixed_config.txt
```

**Erkläre die Muster:**
- `/^#/d` - Lösche Zeilen die mit # beginnen (^ = Zeilenanfang)
- `/^$/d` - Lösche leere Zeilen (^$ = Anfang direkt gefolgt von Ende)
- `-e` - Führe mehrere sed-Befehle nacheinander aus

2. **Bestimmte Zeilenbereiche löschen:**
```bash
echo "=== LÖSCHE ZEILEN 5-8 ==="
sed '5,8d' mixed_config.txt

echo -e "\n=== LÖSCHE DEBUG-BEREICH ==="
sed '/# Debug settings/,/verbose_logging=true/d' mixed_config.txt
```

3. **Text einfügen (Insert und Append):**
```bash
echo "=== FÜGE HEADER EIN ==="
sed '1i\# Updated configuration - Version 2.0' mixed_config.txt

echo -e "\n=== FÜGE NACH JEDER SEKTION LEERZEILE EIN ==="
sed '/=true$/a\\' mixed_config.txt

echo -e "\n=== FÜGE AM ENDE EINE ZEILE EIN ==="
sed '$a\# Configuration loaded successfully' mixed_config.txt
```

**Verstehe die Insert/Append-Syntax:**
- `1i\text` - Insert: Füge vor Zeile 1 ein
- `$a\text` - Append: Füge nach letzter Zeile ($) ein
- `a\\` - Füge eine Leerzeile ein

4. **Nur bestimmte Zeilen anzeigen (Print):**
```bash
echo "=== NUR KONFIGURATIONSWERTE (KEINE KOMMENTARE) ==="
sed -n '/=/p' mixed_config.txt

echo -e "\n=== NUR ZEILEN 10-15 ==="
sed -n '10,15p' mixed_config.txt

echo -e "\n=== ERSTE UND LETZTE ZEILE ==="
sed -n -e '1p' -e '$p' mixed_config.txt
```

**Die -n Option verstehen:**
- Normalerweise gibt sed jede Zeile aus
- `-n` unterdrückt die normale Ausgabe
- `p` Befehl gibt dann nur bestimmte Zeilen aus
- Nützlich um sed wie grep zu verwenden

**Fragen zur Aufgabe 2:**
1. **Muster verstehen:** Was bedeutet `/^#/d` genau und warum funktioniert es für Kommentare?
2. **Bereichslöschung:** Wie löschst du alle Zeilen zwischen "START" und "END" einschließlich dieser Zeilen?
3. **Print vs grep:** Was ist der Unterschied zwischen `sed -n '/muster/p'` und `grep "muster"`?

**Screenshot-Aufgabe 2:**
Screenshot von: `sed -e '/^#/d' -e '/^$/d' mixed_config.txt`

---

## Teil 2: awk - Strukturierte Datenverarbeitung verstehen

### Was macht awk besonders?

**awk** ist keine einfache Textmanipulation wie sed, sondern eine vollständige **Programmiersprache** für strukturierte Daten. awk wurde speziell entwickelt, um mit **feldbasierten** Daten zu arbeiten - denke an CSV-Dateien, Logfiles mit Spalten oder tabellarische Berichte.

### Das Feld-Konzept verstehen

**Was sind Felder?**
awk teilt jede Zeile automatisch in **Felder** (Spalten) auf. Standardmäßig sind Felder durch Leerzeichen oder Tabs getrennt:

```
Beispielzeile: "John Doe 25 Engineer"
$1 = "John"    (erstes Feld)
$2 = "Doe"     (zweites Feld)  
$3 = "25"      (drittes Feld)
$4 = "Engineer" (viertes Feld)
$0 = ganze Zeile
```

**Field Separator (FS) ändern:**
```bash
awk -F, '{ print $1 }'  # Verwende Komma als Feldtrennzeichen
awk -F: '{ print $1 }'  # Verwende Doppelpunkt als Feldtrennzeichen
```

### awk-Grundstruktur verstehen

**Pattern-Action-Struktur:**
```bash
awk 'pattern { action }' datei.txt
```

- **pattern:** WANN soll die Aktion ausgeführt werden (optional)
- **action:** WAS soll gemacht werden

**Beispiele:**
```bash
awk '{ print $1 }'           # Für jede Zeile: drucke erstes Feld
awk '/ERROR/ { print $0 }'   # Nur für Zeilen mit "ERROR": drucke ganze Zeile
awk 'NR > 1 { print $1 }'   # Ab Zeile 2: drucke erstes Feld
```

### Wichtige awk-Variablen verstehen

**Eingebaute Variablen:**
- `$0` - Die komplette aktuelle Zeile
- `$1, $2, $3...` - Erstes, zweites, drittes Feld usw.
- `NF` - Number of Fields (Anzahl Felder in aktueller Zeile)
- `NR` - Number of Records (Aktuelle Zeilennummer, beginnt bei 1)
- `FS` - Field Separator (Feldtrennzeichen)
- `OFS` - Output Field Separator (Ausgabe-Feldtrennzeichen)

**Praktische Bedeutung:**
```bash
# NR für Zeilennummern
awk '{ print NR, $0 }'       # Jede Zeile mit Nummer ausgeben

# NF für Feldanzahl  
awk '{ print NF, $0 }'       # Jede Zeile mit Feldanzahl ausgeben

# Header überspringen
awk 'NR > 1 { print $1 }'   # Erste Zeile (Header) ignorieren
```

### BEGIN und END verstehen

**Spezielle Muster:**
- `BEGIN` - Wird VOR der ersten Zeile ausgeführt
- `END` - Wird NACH der letzten Zeile ausgeführt

```bash
awk 'BEGIN { print "Start" } { print $1 } END { print "Ende" }' datei.txt
```

**Praktischer Nutzen:**
- `BEGIN` - Header ausgeben, Variablen initialisieren
- `END` - Zusammenfassungen, Statistiken ausgeben

---

### Aufgabe 3: awk Grundlagen - Felder verstehen und verwenden

**Erstelle strukturierte Testdaten (CSV-Format):**

```bash
cat > mitarbeiter.csv << 'EOF'
Name,Position,Abteilung,Gehalt,Startdatum
Mueller,Max,Software Engineer,IT,75000,2023-01-15
Schmidt,Anna,Product Manager,Marketing,82000,2022-08-22
Weber,Peter,DevOps Engineer,IT,78000,2023-03-10
Johnson,Lisa,UX Designer,Design,65000,2023-02-01
Brown,Tom,Data Scientist,IT,85000,2022-11-30
Davis,Sarah,HR Manager,HR,70000,2021-05-15
Wilson,Mike,Backend Developer,IT,72000,2023-04-20
Garcia,Maria,Frontend Developer,IT,68000,2023-01-30
EOF
```

**Erstelle ein Access-Log (weltraumgetrennte Felder):**

```bash
cat > access.log << 'EOF'
192.168.1.100 user1 2024-01-15 10:30:22 GET /api/users 200 1234 0.120
192.168.1.105 user2 2024-01-15 10:31:15 POST /api/login 401 89 0.230
10.0.0.50 admin 2024-01-15 10:32:33 GET /admin/dashboard 200 5678 0.045
192.168.1.100 user1 2024-01-15 10:33:44 GET /api/products 200 2345 0.089
10.0.0.75 guest 2024-01-15 10:34:55 GET /api/data 500 0 2.450
192.168.1.200 user3 2024-01-15 10:35:11 DELETE /api/user/123 403 156 0.034
EOF
```

**Verstehe awk Schritt für Schritt:**

1. **Felder verstehen und ausgeben:**
```bash
echo "=== DIE CSV-DATEI VERSTEHEN ==="
echo "Zeige erste paar Zeilen mit Zeilennummern:"
head -4 mitarbeiter.csv | cat -n

echo -e "\n=== ALLE NAMEN AUSGEBEN (OHNE HEADER) ==="
awk -F, 'NR > 1 { print $1 }' mitarbeiter.csv

echo -e "\n=== VERSTEHE DAS FELD-KONZEPT ==="
echo "Erste Zeile aufgeteilt in Felder:"
head -2 mitarbeiter.csv | tail -1 | awk -F, '{ 
    print "Feld 1 (Name):", $1
    print "Feld 2 (Position):", $2  
    print "Feld 3 (Abteilung):", $3
    print "Feld 4 (Gehalt):", $4
    print "Feld 5 (Datum):", $5
    print "Komplette Zeile ($0):", $0
    print "Anzahl Felder (NF):", NF
}'
```

2. **Formatierte Ausgabe mit printf:**
```bash
echo "=== FORMATIERTE NAMENSLISTE ==="
awk -F, 'NR > 1 { printf "%-15s %-20s\n", $1, $2 }' mitarbeiter.csv

echo -e "\n=== GEHALTSLISTE FORMATIERT ==="
awk -F, 'NR > 1 { printf "%-15s %8s EUR\n", $1, $4 }' mitarbeiter.csv
```

**printf verstehen:**
- `%s` - String
- `%d` - Ganze Zahl  
- `%f` - Fließkommazahl
- `%-15s` - String, links ausgerichtet, 15 Zeichen breit
- `%8s` - String, rechts ausgerichtet, 8 Zeichen breit

3. **Access-Log analysieren (weltraumgetrennte Felder):**
```bash
echo "=== ACCESS-LOG FELDER VERSTEHEN ==="
echo "Feld-Struktur:"
head -1 access.log | awk '{ 
    print "IP ($1):", $1
    print "User ($2):", $2
    print "Datum ($3):", $3  
    print "Zeit ($4):", $4
    print "HTTP-Method ($5):", $5
    print "URL ($6):", $6
    print "Status ($7):", $7
    print "Bytes ($8):", $8
    print "Response-Zeit ($9):", $9
}'

echo -e "\n=== NUR IP-ADRESSEN ==="
awk '{ print $1 }' access.log

echo -e "\n=== NUR HTTP-STATUS-CODES ==="
awk '{ print $7 }' access.log
```

4. **Einfache Berechnungen:**
```bash
echo "=== DURCHSCHNITTSGEHALT BERECHNEN ==="
awk -F, 'NR > 1 { 
    summe += $4; 
    anzahl++ 
} 
END { 
    print "Gesamtsumme:", summe, "EUR"
    print "Anzahl Mitarbeiter:", anzahl
    print "Durchschnittsgehalt:", summe/anzahl, "EUR" 
}' mitarbeiter.csv

echo -e "\n=== RESPONSE-ZEITEN ANALYSIEREN ==="
awk '{ 
    total_time += $9; 
    count++ 
} 
END { 
    print "Requests gesamt:", count
    print "Gesamte Response-Zeit:", total_time, "s"
    print "Durchschnittliche Response-Zeit:", total_time/count, "s"
}' access.log
```

**Verstehe die Berechnungen:**
- `summe += $4` - Addiere Feld 4 zur Variable summe
- `anzahl++` - Erhöhe anzahl um 1
- `END` - Wird nach allen Zeilen ausgeführt
- Variablen werden automatisch mit 0 initialisiert

**Fragen zur Aufgabe 3:**
1. **NR verstehen:** Warum verwenden wir `NR > 1` bei CSV-Dateien und was würde ohne passieren?
2. **Field Separator:** Was passiert, wenn du `-F,` weglässt bei der CSV-Verarbeitung?
3. **printf vs print:** Erkläre den Unterschied zwischen `print $1, $4` und `printf "%-15s %8s\n", $1, $4`

**Screenshot-Aufgabe 3:**
Screenshot von: `awk -F, 'NR > 1 { printf "%-15s %8s EUR\n", $1, $4 }' mitarbeiter.csv`

---

### Aufgabe 4: awk Erweiterte Funktionen - Arrays und Gruppierungen

**Was sind Arrays in awk?**
Arrays in awk sind **assoziative Arrays** (wie Hash-Maps). Du kannst sie verwenden um Daten zu **gruppieren** und **aggregieren**:

```bash
# Syntax: array[schlüssel] = wert
verkäufe["Januar"] = 1000
verkäufe["Februar"] = 1200
```

**Erstelle erweiterte Testdaten:**

```bash
cat > verkaufsdaten.csv << 'EOF'
Datum,Produkt,Kategorie,Preis,Menge,Kunde_Typ,Region
2024-01-15,Laptop Pro,Elektronik,1299.99,2,Business,Nord
2024-01-15,Bürostuhl,Möbel,249.99,5,Business,Süd
2024-01-16,Smartphone,Elektronik,799.99,3,Privat,Ost
2024-01-16,Schreibtisch,Möbel,399.99,1,Business,West
2024-01-17,Tablet,Elektronik,449.99,4,Privat,Nord
2024-01-17,Monitor,Elektronik,299.99,2,Business,Süd
2024-01-18,Maus,Elektronik,45.99,10,Privat,Ost
2024-01-18,Lampe,Möbel,79.99,8,Privat,West
2024-01-19,Tastatur,Elektronik,129.99,6,Business,Nord
2024-01-19,Regal,Möbel,189.99,3,Business,Süd
EOF
```

**Lerne Arrays und erweiterte awk-Features:**

1. **Array-Grundlagen verstehen:**
```bash
echo "=== UMSATZ PRO KATEGORIE (ARRAY-BEISPIEL) ==="
awk -F, '
NR > 1 { 
    umsatz = $4 * $5  # Preis mal Menge
    kategorie_umsatz[$3] += umsatz  # Array: kategorie_umsatz["Elektronik"] += wert
}
END {
    print "Umsatz pro Kategorie:"
    for (kategorie in kategorie_umsatz) {
        printf "  %-12s: %8.2f EUR\n", kategorie, kategorie_umsatz[kategorie]
    }
}' verkaufsdaten.csv
```

**Verstehe was passiert:**
- `kategorie_umsatz[$3]` - Array mit Kategorie-Namen als Schlüssel
- `+= umsatz` - Addiere Umsatz zum bestehenden Wert
- `for (kategorie in kategorie_umsatz)` - Iteriere über alle Array-Keys

## Teil 3: sed und awk kombinieren - Realistische Workflows

### Warum sed und awk kombinieren?

**Die perfekte Arbeitsteilung:**
- **sed:** Datenbereinigung, Formatierung, einfache Transformationen
- **awk:** Analyse, Berechnungen, komplexe Auswertungen
- **Zusammen:** Vollständige Datenverarbeitungs-Pipeline

**Pipeline-Konzept:**
```
Rohdaten → sed (bereinigen) → awk (analysieren) → Bericht
```

### Aufgabe 5: Webserver-Log-Analyse komplett

**Erstelle eine realistische Webserver-Logdatei:**

```bash
cat > webserver_raw.log << 'EOF'
# Apache Access Log - January 15, 2024
# Format: IP - user [timestamp] "request" status size response_time
192.168.1.100 - user1 [15/Jan/2024:08:00:15 +0100] "GET /index.html HTTP/1.1" 200 1234 0.120
192.168.1.105 - user2 [15/Jan/2024:08:01:22 +0100] "GET /api/users HTTP/1.1" 200 567 0.045
10.0.0.50 - admin [15/Jan/2024:08:02:33 +0100] "POST /login HTTP/1.1" 401 89 0.230
# Suspicious activity block starts
192.168.1.100 - user1 [15/Jan/2024:08:03:44 +0100] "GET /admin HTTP/1.1" 403 156 0.012
10.0.0.75 - guest [15/Jan/2024:08:04:55 +0100] "GET /api/data HTTP/1.1" 500 0 2.450
192.168.1.105 - user2 [15/Jan/2024:08:05:11 +0100] "GET /images/logo.png HTTP/1.1" 200 4567 0.089
10.0.0.50 - admin [15/Jan/2024:08:06:22 +0100] "POST /login HTTP/1.1" 200 234 0.156
# Normal operation resumes
192.168.1.200 - user3 [15/Jan/2024:08:07:33 +0100] "GET /api/status HTTP/1.1" 404 78 0.034
10.0.0.75 - guest [15/Jan/2024:08:08:44 +0100] "GET /api/data HTTP/1.1" 500 0 3.120
192.168.1.100 - user1 [15/Jan/2024:08:09:55 +0100] "DELETE /api/user/123 HTTP/1.1" 200 12 0.067
# End of log
EOF
```

**Schritt 1: Datenbereinigung mit sed**

```bash
echo "=== SCHRITT 1: DATENBEREINIGUNG MIT SED ==="

# 1. Entferne Kommentarzeilen
echo "Entferne Kommentare..."
sed '/^#/d' webserver_raw.log > webserver_clean.log

echo "Bereinigte Daten:"
cat webserver_clean.log

# 2. Vereinfache Zeitstempel (extrahiere nur Uhrzeit)
echo -e "\n=== ZEITSTEMPEL VEREINFACHEN ==="
sed 's/\[.*:\([0-9][0-9]:[0-9][0-9]:[0-9][0-9]\)[^]]*\]/\1/' webserver_clean.log > webserver_time.log

echo "Mit vereinfachten Zeitstempeln:"
head -3 webserver_time.log

# 3. Vereinfache HTTP-Requests (extrahiere nur URL)
echo -e "\n=== HTTP-REQUESTS VEREINFACHEN ==="
sed 's/"[A-Z]* \([^ ]*\) HTTP[^"]*"/\1/' webserver_time.log > webserver_processed.log

echo "Vollständig verarbeitet:"
head -3 webserver_processed.log
```

**Verstehe die sed-Transformationen:**
- `/^#/d` - Lösche Kommentarzeilen
- `\([0-9][0-9]:[0-9][0-9]:[0-9][0-9]\)` - Gruppiere Uhrzeit-Muster
- `\1` - Verwende die erste Gruppe (die Uhrzeit)
- `"[A-Z]* \([^ ]*\) HTTP[^"]*"` - Extrahiere URL aus HTTP-Request

**Schritt 2: Analyse mit awk**

```bash
echo "=== SCHRITT 2: ANALYSE MIT AWK ==="

# Grundlegende Statistiken
awk '{
    requests++
    
    # Status-Code-Analyse
    if ($6 >= 400) {
        errors++
        error_ips[$1]++
    }
    
    # Response-Zeit-Analyse  
    if ($7 > 1.0) {
        slow_requests++
    }
    
    # Traffic-Analyse
    total_bytes += $5
    
    # IP-Statistiken
    ip_count[$1]++
    
    # URL-Statistiken
    url_count[$4]++
}
END {
    print "=== WEBSERVER-STATISTIKEN ==="
    print "=============================="
    print "Gesamt Requests:", requests
    print "Fehler (>=400):", errors, "(" (errors/requests)*100 "%)"
    print "Langsame Requests (>1s):", slow_requests
    print "Gesamttraffic:", total_bytes, "bytes"
    print "Eindeutige IPs:", length(ip_count)
    
    print "\n=== TOP FEHLER-IPS ==="
    for (ip in error_ips) {
        if (error_ips[ip] > 1) {
            printf "  %s: %d Fehler\n", ip, error_ips[ip]
        }
    }
    
    print "\n=== HÄUFIGSTE URLS ==="
    # Finde URLs mit mehr als 1 Aufruf
    for (url in url_count) {
        if (url_count[url] > 1) {
            printf "  %s: %d mal aufgerufen\n", url, url_count[url]
        }
    }
}' webserver_processed.log
```

**Schritt 3: Komplette Pipeline**

```bash
echo "=== SCHRITT 3: KOMPLETTE PIPELINE ==="

# Alles in einer Pipeline kombinieren
sed '/^#/d' webserver_raw.log | \
sed 's/\[.*:\([0-9][0-9]:[0-9][0-9]:[0-9][0-9]\)[^]]*\]/\1/' | \
sed 's/"[A-Z]* \([^ ]*\) HTTP[^"]*"/\1/' | \
awk '
BEGIN {
    print "=== WEBSERVER SECURITY REPORT ==="
    print "=================================="
    print "Analyse-Zeitpunkt:", strftime("%Y-%m-%d %H:%M:%S")
    print ""
}
{
    requests++
    
    # Detaillierte Analyse
    status_codes[$6]++
    
    # Verdächtige IP-Analyse (10.0.0.x Netzwerk)
    if ($1 ~ /^10\.0\.0\./) {
        suspicious_requests++
        suspicious_ips[$1]++
        if ($6 >= 400) suspicious_errors++
    }
    
    # Performance-Analyse
    response_times[NR] = $7
    total_time += $7
    
    # Endpoint-Analyse
    endpoint_requests[$4]++
    if ($6 >= 400) {
        endpoint_errors[$4]++
    }
}
END {
    print "GRUNDSTATISTIKEN:"
    print "Requests gesamt:", requests
    print "Verdächtige Requests (10.0.0.x):", suspicious_requests
    print "Verdächtige Fehler:", suspicious_errors
    print "Durchschn. Response-Zeit:", total_time/requests "s"
    
    print "\nSTATUS-CODE VERTEILUNG:"
    for (code in status_codes) {
        printf "  %s: %d (%.1f%%)\n", code, status_codes[code], (status_codes[code]/requests)*100
    }
    
    print "\nVERDÄCHTIGE IPS (10.0.0.x):"
    for (ip in suspicious_ips) {
        printf "  %s: %d Requests\n", ip, suspicious_ips[ip]
    }
    
    print "\nFEHLERHAFTE ENDPOINTS:"
    for (endpoint in endpoint_errors) {
        printf "  %s: %d Fehler von %d Requests\n", endpoint, endpoint_errors[endpoint], endpoint_requests[endpoint]
    }
    
    print "\n=== EMPFEHLUNGEN ==="
    if (suspicious_requests > 0) {
        print "- Überwache das 10.0.0.x Netzwerk genauer"
    }
    if (suspicious_errors > requests*0.1) {
        print "- Hohe Fehlerrate bei verdächtigen IPs"
    }
    print "- Analyse abgeschlossen"
}'
```

**Fragen zur Aufgabe 5:**
1. **Pipeline-Vorteile:** Warum ist es besser, sed für Bereinigung und awk für Analyse zu verwenden statt alles in einem Tool?
2. **Sed-Regex:** Erkläre die Regex `\[.*:\([0-9][0-9]:[0-9][0-9]:[0-9][0-9]\)[^]]*\]` für die Zeitstempel-Extraktion
3. **Awk-Performance:** Warum ist `length(ip_count)` ein eleganter Weg, um eindeutige IPs zu zählen?

**Screenshot-Aufgabe 5:**
Screenshot des kompletten Webserver Security Reports aus der Pipeline.

---

### Aufgabe 6: Business Intelligence mit CSV-Daten

**Erstelle eine umfangreiche Geschäftsdatenbank:**

```bash
cat > geschaeftsdaten.csv << 'EOF'
# Quartalsbericht Q1 2024 - Verkaufsdaten
Datum,Region,Verkäufer,Produkt,Kategorie,Stückzahl,Einzelpreis,Kundentyp,Zahlungsart,Verkaufskanal
2024-01-05,Nord,Johnson,Laptop Pro Max,Elektronik,15,1299.99,Business,Rechnung,Online
2024-01-05,Süd,Miller,Bürostuhl Premium,Möbel,25,249.99,Business,Rechnung,Filiale
2024-01-06,Ost,Wilson,iPhone 15,Elektronik,40,899.99,Privat,Karte,Online  
2024-01-06,West,Davis,Schreibtisch Electric,Möbel,8,599.99,Business,Karte,Filiale
2024-01-07,Nord,Johnson,iPad Pro,Elektronik,20,799.99,Privat,Bar,Filiale
2024-01-08,Süd,Miller,Monitor 4K Ultra,Elektronik,12,449.99,Business,Rechnung,Online
2024-01-08,Ost,Wilson,Gaming Maus RGB,Elektronik,60,79.99,Privat,Karte,Online
2024-01-09,West,Davis,Ergonomie Stuhl,Möbel,15,299.99,Business,Karte,Filiale
2024-01-10,Nord,Johnson,MacBook Air,Elektronik,30,1199.99,Privat,Karte,Online
2024-01-10,Süd,Miller,Designer Lampe,Möbel,35,129.99,Privat,Bar,Filiale
2024-01-11,Ost,Wilson,Mechanical Keyboard,Elektronik,18,199.99,Privat,Karte,Online
2024-01-12,West,Davis,Konferenztisch XXL,Möbel,3,1999.99,Business,Rechnung,Filiale
# Datenexport Ende
EOF
```

**Pipeline für Business Intelligence:**

```bash
echo "=== BUSINESS INTELLIGENCE PIPELINE ==="

# Schritt 1: Datenbereinigung mit sed
echo "Schritt 1: Datenbereinigung..."
sed -e '/^#/d' -e '/^$/d' geschaeftsdaten.csv | \
sed 's/[[:space:]]*$//' > saubere_daten.csv

echo "Bereinigte Daten (erste 3 Zeilen):"
head -3 saubere_daten.csv

# Schritt 2: Umfassende Geschäftsanalyse
echo -e "\n=== EXECUTIVE DASHBOARD ==="
awk -F, '
BEGIN {
    print "┌─────────────────────────────────────────────┐"
    print "│        Q1 2024 GESCHÄFTSBERICHT            │"  
    print "└─────────────────────────────────────────────┘"
    
    # Initialisierung
    total_revenue = 0
    total_units = 0
}

# Header überspringen
NR == 1 { next }

# Hauptverarbeitung
{
    # Umsatzberechnung
    revenue = $6 * $7
    total_revenue += revenue
    total_units += $6
    
    # Multi-dimensionale Analyse
    region_revenue[$2] += revenue
    verkäufer_revenue[$3] += revenue
    kategorie_revenue[$5] += revenue
    kundentyp_revenue[$8] += revenue
    zahlungsart_revenue[$9] += revenue
    kanal_revenue[$10] += revenue
    
    # Zähler für Durchschnittswerte
    region_deals[$2]++
    verkäufer_deals[$3]++
    
    # Beste Einzelgeschäfte tracking
    if (revenue > best_deal) {
        best_deal = revenue
        best_deal_info = $3 " - " $4 " (" $2 ")"
    }
    
    # Produkt-Performance
    produkt_revenue[$4] += revenue
    produkt_units[$4] += $6
}

END {
    print "\n📊 KERNKENNZAHLEN:"
    print "══════════════════════════════════════════════"
    printf "Gesamtumsatz:           %10.2f EUR\n", total_revenue
    printf "Verkaufte Einheiten:    %10d Stück\n", total_units  
    printf "Durchschn. Deal-Wert:   %10.2f EUR\n", total_revenue/(NR-1)
    printf "Bester Einzeldeal:      %10.2f EUR\n", best_deal
    printf "Details:                %s\n", best_deal_info
    
    print "\n🗺️  REGIONALE PERFORMANCE:"
    print "══════════════════════════════════════════════"
    for (region in region_revenue) {
        avg_deal = region_revenue[region] / region_deals[region]
        printf "%-8s: %8.2f EUR (%2d Deals, Ø %.2f EUR)\n", 
               region, region_revenue[region], region_deals[region], avg_deal
    }
    
    print "\n👤 VERKÄUFER-RANKING:"
    print "══════════════════════════════════════════════"
    for (person in verkäufer_revenue) {
        performance = verkäufer_revenue[person] / verkäufer_deals[person]
        printf "%-10s: %8.2f EUR (%2d Deals, Ø %.2f EUR)\n", 
               person, verkäufer_revenue[person], verkäufer_deals[person], performance
    }
    
    print "\n📦 KATEGORIE-MIX:"
    print "══════════════════════════════════════════════"
    for (kategorie in kategorie_revenue) {
        percentage = (kategorie_revenue[kategorie] / total_revenue) * 100
        printf "%-12s: %8.2f EUR (%5.1f%%)\n", 
               kategorie, kategorie_revenue[kategorie], percentage
    }
    
    print "\n💳 ZAHLUNGSARTEN:"
    print "══════════════════════════════════════════════"
    for (zahlung in zahlungsart_revenue) {
        percentage = (zahlungsart_revenue[zahlung] / total_revenue) * 100
        printf "%-10s: %8.2f EUR (%5.1f%%)\n", 
               zahlung, zahlungsart_revenue[zahlung], percentage
    }
    
    print "\n🛒 VERKAUFSKANÄLE:"
    print "══════════════════════════════════════════════"
    for (kanal in kanal_revenue) {
        percentage = (kanal_revenue[kanal] / total_revenue) * 100
        printf "%-10s: %8.2f EUR (%5.1f%%)\n", 
               kanal, kanal_revenue[kanal], percentage
    }
}' saubere_daten.csv

# Schritt 3: Spezialanalysen
echo -e "\n=== SPEZIALANALYSEN ==="

echo "🏆 TOP-PRODUKTE nach Umsatz:"
awk -F, 'NR > 1 { 
    revenue = $6 * $7
    product_revenue[$4] += revenue 
    product_units[$4] += $6
} 
END { 
    for (product in product_revenue) {
        printf "%-25s: %8.2f EUR (%d Stück)\n", product, product_revenue[product], product_units[product]
    }
}' saubere_daten.csv | sort -k2 -nr | head -5

echo -e "\n🎯 KUNDENTYP-ANALYSE:"
awk -F, 'NR > 1 {
    revenue = $6 * $7
    kunde = $8
    
    if (kunde == "Business") {
        business_revenue += revenue
        business_deals++
    } else {
        privat_revenue += revenue  
        privat_deals++
    }
}
END {
    print "Business-Kunden:"
    printf "  Umsatz:     %.2f EUR (%.1f%%)\n", business_revenue, (business_revenue/(business_revenue+privat_revenue))*100
    printf "  Deals:      %d (Ø %.2f EUR pro Deal)\n", business_deals, business_revenue/business_deals
    
    print "Privat-Kunden:"  
    printf "  Umsatz:     %.2f EUR (%.1f%%)\n", privat_revenue, (privat_revenue/(business_revenue+privat_revenue))*100
    printf "  Deals:      %d (Ø %.2f EUR pro Deal)\n", privat_deals, privat_revenue/privat_deals
}' saubere_daten.csv

# Schritt 4: Export für weitere Systeme
echo -e "\n=== DATENEXPORT ==="

# CSV für Buchhaltung
echo "Erstelle Buchhaltungs-Export..."
awk -F, 'BEGIN { OFS="," } 
NR == 1 { print "Datum", "Region", "Verkäufer", "Netto_Umsatz" }
NR > 1 { print $1, $2, $3, ($6 * $7) }' saubere_daten.csv > buchhaltung_export.csv

# JSON für Dashboard
echo "Erstelle Dashboard-Export..."
awk -F, '
BEGIN { 
    print "{"
    print "  \"verkaufsdaten\": ["
}
NR > 1 {
    revenue = $6 * $7
    if (NR > 2) print ","
    printf "    {\"region\":\"%s\", \"verkäufer\":\"%s\", \"umsatz\":%.2f, \"kategorie\":\"%s\"}", $2, $3, revenue, $5
}
END {
    print ""
    print "  ],"
    print "  \"generiert\": \"" strftime("%Y-%m-%d %H:%M:%S") "\""
    print "}"
}' saubere_daten.csv > dashboard_export.json

echo "📁 Export-Dateien erstellt:"
echo "  - buchhaltung_export.csv (Buchhaltungssystem)"
echo "  - dashboard_export.json (Web-Dashboard)"

# Cleanup
rm saubere_daten.csv
```

**Verständnis der komplexen awk-Strukturen:**
- **Multi-dimensionale Arrays:** `region_revenue[$2] += revenue`
- **Prozentberechnung:** `(wert / gesamt) * 100`
- **Formatierte Ausgabe:** `printf` mit festen Spaltenbreiten
- **String-Formatierung:** `strftime()` für Zeitstempel

**Fragen zur Aufgabe 6:**
1. **Business Logic:** Wie berechnest du den durchschnittlichen Deal-Wert pro Verkäufer?
2. **Export-Formate:** Warum sind verschiedene Export-Formate (CSV, JSON) wichtig?
3. **Performance:** Welche Vorteile hat die einmalige Datenverarbeitung gegenüber mehreren separaten Durchläufen?

**Screenshot-Aufgabe 6:**
Screenshot des Executive Dashboards mit allen Geschäftskennzahlen.

---

### Abschluss-Challenge: Automatisiertes Monitoring-System

**Erstelle ein komplettes Monitoring- und Reporting-System:**

```bash
cat > monitor_system.sh << 'EOF'
#!/bin/bash

# Automatisiertes Monitoring-System mit sed & awk
# Überwacht Systemlogs und erstellt Berichte

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔍 SYSTEM MONITORING & ANALYSIS FRAMEWORK"  
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Gestartet: $(date)"
echo

# Erstelle Mock-System-Logs für Demo
create_test_logs() {
    echo "📝 Erstelle Test-Logs..."
    
    cat > system_events.log << 'LOGEOF'
2024-01-15 09:00:01 INFO kernel: System boot completed
2024-01-15 09:00:05 INFO systemd: Started Network Manager
2024-01-15 09:00:10 WARN sshd: Failed password for invalid user admin from 192.168.1.100
2024-01-15 09:02:15 ERROR apache2: server reached MaxRequestWorkers setting
2024-01-15 09:02:20 INFO apache2: server restarted gracefully
2024-01-15 09:05:30 WARN disk: /dev/sda1 is 90% full
2024-01-15 09:10:45 ERROR mysql: connection timeout from 10.0.0.50
2024-01-15 09:10:50 INFO mysql: connection restored
2024-01-15 09:15:22 WARN security: multiple failed login attempts from 10.0.0.25
2024-01-15 09:20:33 ERROR backup: daily backup failed - insufficient space
2024-01-15 09:25:11 INFO cron: backup job rescheduled  
2024-01-15 09:30:44 WARN memory: RAM usage 95% - cleaning caches
2024-01-15 09:35:15 ERROR network: interface eth0 down
2024-01-15 09:35:20 INFO network: interface eth0 restored
LOGEOF

    cat > access_combined.log << 'LOGEOF'
# Combined Access Log with user agents and referrers
192.168.1.100 - user1 [15/Jan/2024:09:00:15] "GET /dashboard HTTP/1.1" 200 5432 0.120 "Mozilla/5.0" "direct"
10.0.0.50 - admin [15/Jan/2024:09:02:33] "POST /admin/login HTTP/1.1" 401 89 0.230 "curl/7.68" "script"  
192.168.1.105 - user2 [15/Jan/2024:09:05:11] "GET /api/data HTTP/1.1" 200 2345 0.089 "Python/3.9" "api_client"
10.0.0.25 - hacker [15/Jan/2024:09:07:44] "GET /admin/config HTTP/1.1" 403 156 0.012 "Nmap" "scan"
192.168.1.200 - user3 [15/Jan/2024:09:10:22] "DELETE /user/data HTTP/1.1" 500 0 2.450 "Mozilla/5.0" "webapp"
10.0.0.25 - hacker [15/Jan/2024:09:12:55] "POST /login HTTP/1.1" 401 45 0.890 "Hydra" "bruteforce"
192.168.1.100 - user1 [15/Jan/2024:09:15:33] "GET /profile HTTP/1.1" 200 1234 0.067 "Mozilla/5.0" "direct"
LOGEOF
    
    echo "✅ Test-Logs erstellt"
}

# Phase 1: Log-Bereinigung mit sed
cleanup_logs() {
    echo "🧹 Phase 1: Log-Bereinigung mit sed..."
    
    # System-Logs bereinigen
    sed -e '/^#/d' -e '/^$/d' system_events.log | \
    sed 's/^\([0-9-]* [0-9:]*\) \([A-Z]*\) \([^:]*\): \(.*\)/\1|\2|\3|\4/' > system_clean.log
    
    # Access-Logs bereinigen und normalisieren
    sed '/^#/d' access_combined.log | \
    sed 's/\[.*\]//' | \
    sed 's/"[^"]*"//' | \
    sed 's/  */ /g' > access_clean.log
    
    echo "✅ Logs bereinigt und normalisiert"
}

# Phase 2: System-Analyse mit awk
analyze_system() {
    echo "📊 Phase 2: System-Analyse..."
    
    awk -F'|' '
    BEGIN {
        print "╔════════════════════════════════════════╗"
        print "║          SYSTEM HEALTH REPORT         ║"
        print "╚════════════════════════════════════════╝"
    }
    {
        total_events++
        level_count[$2]++
        service_events[$3]++
        
        # Kritische Events identifizieren
        if ($2 == "ERROR") {
            error_count++
            error_services[$3]++
            print "🚨 ERROR:", $1, "-", $3, ":", $4 > "/dev/stderr"
        }
        
        if ($2 == "WARN") {
            warning_count++
            warning_services[$3]++
        }
        
        # Security-Events
        if ($4 ~ /login|password|security/) {
            security_events++
        }
        
        # Resource-Warnings
        if ($4 ~ /memory|disk|RAM/) {
            resource_warnings++
        }
    }
    END {
        print "\n📈 SYSTEM ÜBERSICHT:"
        print "═══════════════════════════════════════════"
        printf "Gesamt Events:        %d\n", total_events
        printf "Kritische Fehler:     %d\n", error_count
        printf "Warnungen:           %d\n", warning_count
        printf "Security Events:      %d\n", security_events  
        printf "Resource Warnings:    %d\n", resource_warnings
        
        print "\n📊 EVENT-LEVEL VERTEILUNG:"
        for (level in level_count) {
            printf "  %-8s: %3d (%4.1f%%)\n", level, level_count[level], (level_count[level]/total_events)*100
        }
        
        print "\n🔧 BETROFFENE SERVICES:"
        for (service in service_events) {
            printf "  %-12s: %2d Events", service, service_events[service]
            if (service in error_services) printf " (❌ %d Errors)", error_services[service]
            if (service in warning_services) printf " (⚠️  %d Warnings)", warning_services[service]
            print ""
        }
        
        print "\n🚨 EMPFEHLUNGEN:"
        if (error_count > 0) print "  • Sofortige Überprüfung der Services mit Fehlern"
        if (security_events > 2) print "  • Sicherheitsaudit durchführen"  
        if (resource_warnings > 0) print "  • Ressourcen-Überwachung verstärken"
        if (error_count == 0 && warning_count <= 2) print "  • System läuft stabil ✅"
    }' system_clean.log
}

# Phase 3: Security-Analyse
analyze_security() {
    echo -e "\n🔒 Phase 3: Security-Analyse..."
    
    awk '{
        ip = $1
        user = $3  
        status = $7
        user_agent = $9
        source = $10
        
        # IP-Tracking
        ip_requests[ip]++
        
        # Failed Authentication
        if (status == "401") {
            failed_auth[ip]++
            failed_users[user]++
        }
        
        # Suspicious User Agents
        if (user_agent ~ /Nmap|Hydra|curl/ && source ~ /scan|bruteforce|script/) {
            suspicious[ip]++
            attack_tools[user_agent]++
        }
        
        # Forbidden Access
        if (status == "403") {
            forbidden[ip]++
        }
        
        # Server Errors
        if (status == "500") {
            server_errors[ip]++
        }
    }
    END {
        print "╔════════════════════════════════════════╗"
        print "║           SECURITY REPORT             ║"  
        print "╚════════════════════════════════════════╝"
        
        print "\n🚨 VERDÄCHTIGE AKTIVITÄTEN:"
        print "═══════════════════════════════════════════"
        
        threat_level = 0
        
        if (length(suspicious) > 0) {
            print "⚠️  ATTACK TOOLS DETECTED:"
            for (ip in suspicious) {
                printf "  IP %s: %d suspicious requests\n", ip, suspicious[ip]
                threat_level += suspicious[ip]
            }
        }
        
        if (length(failed_auth) > 0) {
            print "\n🔑 FAILED AUTHENTICATION:"
            for (ip in failed_auth) {
                if (failed_auth[ip] > 2) {
                    printf "  IP %s: %d failed attempts ⚠️\n", ip, failed_auth[ip]
                    threat_level += failed_auth[ip]
                }
            }
        }
        
        if (length(forbidden) > 0) {
            print "\n🚫 FORBIDDEN ACCESS ATTEMPTS:"
            for (ip in forbidden) {
                printf "  IP %s: %d forbidden requests\n", ip, forbidden[ip]  
                threat_level += forbidden[ip]
            }
        }
        
        print "\n📊 THREAT ASSESSMENT:"
        if (threat_level == 0) {
            print "  🟢 LOW - No significant threats detected"
        } else if (threat_level <= 5) {
            print "  🟡 MEDIUM - Monitor suspicious activities"
        } else {
            print "  🔴 HIGH - Immediate action required!"
        }
        
        print "\n🛡️  RECOMMENDED ACTIONS:"
        if (length(suspicious) > 0) {
            print "  • Block IPs using attack tools"
            for (ip in suspicious) print "    - " ip
        }
        if (threat_level > 5) {
            print "  • Enable additional logging"
            print "  • Implement rate limiting"
            print "  • Review firewall rules"
        }
    }' access_clean.log
}

# Phase 4: Performance-Report
generate_performance_report() {
    echo -e "\n⚡ Phase 4: Performance-Report..."
    
    awk '{
        response_time = $8
        
        if (response_time != "" && response_time > 0) {
            total_time += response_time
            request_count++
            
            if (response_time > 2.0) {
                very_slow++
            } else if (response_time > 1.0) {
                slow++  
            } else if (response_time > 0.5) {
                medium++
            } else {
                fast++
            }
            
            # Track per endpoint
            endpoint = $6
            endpoint_times[endpoint] += response_time
            endpoint_count[endpoint]++
        }
    }
    END {
        if (request_count > 0) {
            avg_response = total_time / request_count
            
            print "╔════════════════════════════════════════╗"
            print "║         PERFORMANCE REPORT            ║"
            print "╚════════════════════════════════════════╝"
            
            printf "\n📊 RESPONSE TIME ANALYSIS:\n"
            printf "  Average Response Time: %.3f seconds\n", avg_response
            printf "  Total Requests: %d\n", request_count
            
            print "\n⏱️  PERFORMANCE DISTRIBUTION:"
            printf "  🟢 Fast    (<0.5s): %3d (%4.1f%%)\n", fast, (fast/request_count)*100
            printf "  🟡 Medium  (0.5-1s): %3d (%4.1f%%)\n", medium, (medium/request_count)*100  
            printf "  🟠 Slow    (1-2s):   %3d (%4.1f%%)\n", slow, (slow/request_count)*100
            printf "  🔴 Very Slow (>2s):  %3d (%4.1f%%)\n", very_slow, (very_slow/request_count)*100
            
            if (length(endpoint_times) > 0) {
                print "\n🎯 ENDPOINT PERFORMANCE:"
                for (endpoint in endpoint_times) {
                    avg_endpoint = endpoint_times[endpoint] / endpoint_count[endpoint]
                    printf "  %-20s: %.3fs avg (%d requests)\n", endpoint, avg_endpoint, endpoint_count[endpoint]
                }
            }
            
            print "\n📈 PERFORMANCE RECOMMENDATIONS:"
            if (avg_response > 1.0) {
                print "  • Overall performance needs improvement"
                print "  • Consider server optimization"
            }
            if (very_slow > 0) {
                print "  • Investigate very slow requests (>2s)"
            }
            if ((slow + very_slow) / request_count > 0.2) {
                print "  • 20%+ requests are slow - urgent optimization needed"
            }
            if (avg_response < 0.5) {
                print "  • Excellent performance ✅"
            }
        }
    }' access_clean.log
}

# Phase 5: Automated Report Generation
generate_final_report() {
    echo -e "\n📋 Phase 5: Final Report Generation..."
    
    # Kombinierter Report mit Zeitstempel
    {
        echo "╔══════════════════════════════════════════════════════════╗"
        echo "║                  SYSTEM MONITORING REPORT               ║"
        echo "║                Generated: $(date '+%Y-%m-%d %H:%M:%S')                 ║"
        echo "╚══════════════════════════════════════════════════════════╝"
        echo
        
        # Executive Summary
        total_events=$(wc -l < system_clean.log)
        error_events=$(grep "ERROR" system_clean.log | wc -l)
        total_requests=$(wc -l < access_clean.log)
        
        echo "🎯 EXECUTIVE SUMMARY:"
        echo "═══════════════════════════════════════════════════════════"
        printf "System Events:     %d\n" $total_events
        printf "Critical Errors:   %d\n" $error_events  
        printf "Web Requests:      %d\n" $total_requests
        
        if [ $error_events -eq 0 ]; then
            echo "Overall Status:    🟢 HEALTHY"
        elif [ $error_events -le 2 ]; then
            echo "Overall Status:    🟡 NEEDS ATTENTION"
        else
            echo "Overall Status:    🔴 CRITICAL"
        fi
        
        echo
        echo "📊 Detailed analysis follows below..."
        echo
    } > final_system_report.txt
    
    echo "✅ Executive Summary created"
    
    # Export für verschiedene Systeme
    echo "📤 Creating exports..."
    
    # JSON für Monitoring-Dashboard
    {
        echo "{"
        echo "  \"timestamp\": \"$(date -Iseconds)\","
        echo "  \"system_health\": {"
        echo "    \"total_events\": $total_events,"
        echo "    \"errors\": $error_events,"
        echo "    \"status\": \"$([ $error_events -eq 0 ] && echo 'healthy' || echo 'warning')\""
        echo "  },"
        echo "  \"web_traffic\": {"
        echo "    \"total_requests\": $total_requests"
        echo "  }"
        echo "}"
    } > monitoring_data.json
    
    # CSV für Trend-Analyse
    echo "timestamp,total_events,errors,requests" > trend_data.csv
    echo "$(date -Iseconds),$total_events,$error_events,$total_requests" >> trend_data.csv
    
    echo "✅ Export-Dateien erstellt:"
    echo "  📄 final_system_report.txt (Executive Report)"
    echo "  📊 monitoring_data.json (Dashboard Integration)"  
    echo "  📈 trend_data.csv (Trend Analysis)"
}

# Cleanup-Funktion
cleanup() {
    echo -e "\n🧹 Cleanup..."
    rm -f system_clean.log access_clean.log system_events.log access_combined.log
    echo "✅ Temporäre Dateien entfernt"
}

# Main Execution
main() {
    create_test_logs
    cleanup_logs
    analyze_system
    analyze_security  
    generate_performance_report
    generate_final_report
    cleanup
    
    echo
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "✅ MONITORING COMPLETE"
    echo "📊 Reports available in current directory"
    echo "🔄 Run this script regularly for continuous monitoring"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
}

# Script ausführen
main
EOF

# Script ausführbar machen und starten
chmod +x monitor_system.sh
echo "🚀 Starte Monitoring-System..."
./monitor_system.sh
```

**Überprüfe die generierten Berichte:**

```bash
echo "=== GENERIERTE REPORTS ==="
ls -la *.txt *.json *.csv 2>/dev/null || echo "Keine Report-Dateien gefunden"

if [ -f "final_system_report.txt" ]; then
    echo -e "\n=== EXECUTIVE SUMMARY ==="
    head -20 final_system_report.txt
fi

if [ -f "monitoring_data.json" ]; then
    echo -e "\n=== MONITORING JSON ==="
    cat monitoring_data.json
fi
```

**Abschluss-Fragen:**
1. **Komplexe Pipelines:** Wie organisierst du komplexe sed/awk-Workflows für bessere Wartbarkeit?
2. **Error Handling:** Welche Mechanismen würdest du für Fehlerbehandlung in Produktions-Scripts einbauen?
3. **Skalierung:** Wie würdest du dieses System für sehr große Log-Dateien (GB-Größe) optimieren?

**Final-Screenshot:**
Screenshot des kompletten Monitoring-System-Outputs mit allen Phasen.

---

## Zusammenfassung: Master-Level Expertise

Nach Abschluss dieser umfassenden Challenge bist du ein Experte in:

### **sed-Mastery:**
- **Stream-Processing-Konzepte:** Pattern Space, Adressierung, Pipeline-Integration
- **Erweiterte Textmanipulation:** Komplexe Regex, Multi-Command-Pipelines
- **Produktionsreife Datenbereinigung:** Log-Normalisierung, Format-Konvertierung
- **Performance-Optimierung:** Effiziente Ein-Pass-Verarbeitung großer Dateien

### **awk-Mastery:**
- **Programmiersprachen-Konzepte:** Variables, Arrays, Control Flow, Functions
- **Datenstruktur-Verarbeitung:** Multi-dimensionale Aggregation, Gruppierung
- **Business Intelligence:** KPI-Berechnung, Report-Generierung, Trend-Analyse
- **Export-Systeme:** CSV, JSON, formatierte Berichte für verschiedene Systeme

### **Integration & Automation:**
- **Pipeline-Architektur:** Modulare sed/awk-Kombinationen
- **Monitoring-Systeme:** Automatisierte Log-Analyse und Alerting
- **Data Processing Workflows:** ETL-Prozesse mit Unix-Tools
- **Production Scripting:** Robuste, wiederverwendbare Automatisierung

### **Professionelle Anwendungsbereiche:**
- **System Administration:** Log-Analyse, Performance-Monitoring, Security-Audits
- **Business Analytics:** Verkaufsdaten-Auswertung, KPI-Dashboards, Trend-Reports
- **DevOps Integration:** CI/CD-Pipeline-Unterstützung, Deployment-Monitoring
- **Data Engineering:** Datenbereinigung, Format-Transformation, Qualitätskontrolle

### **Nächste Schritte:**
Du kannst jetzt:
- **Komplexe Datenverarbeitungs-Workflows** von Grund auf entwickeln
- **Enterprise-Level Log-Analyse-Systeme** implementieren  
- **Automatisierte Business Intelligence** mit Unix-Tools erstellen
- **Performance-kritische Textverarbeitung** für große Datenmengen optimieren

### **Weiterführende Bereiche:**
- **Bash-Scripting Advanced:** Integration in größere Automatisierungs-Frameworks
- **Regular Expressions Master:** PCRE, erweiterte Pattern-Matching
- **Database Integration:** sed/awk mit SQL-Systemen kombinieren
- **Big Data Processing:** Hadoop, Spark mit Unix-Tool-Integration

**Gratulation!** Du beherrschst jetzt zwei der mächtigsten Tools der Unix-Welt und kannst praktisch jede Textverarbeitungs- und Datenanalyse-Aufgabe automatisieren. Diese Fähigkeiten bilden das Fundament für fortgeschrittene System-Administration und Data Engineering.

**Tipp für die Praxis:** Erstelle dir eine persönliche Bibliothek von sed/awk-Patterns für häufige Aufgaben. Die investierte Zeit in das Lernen dieser Tools zahlt sich täglich aus!
